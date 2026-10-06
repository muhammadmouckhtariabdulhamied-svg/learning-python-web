"""Hermes Portable Agent: local-first, approval-gated laptop assistant."""
from __future__ import annotations
import json, os, platform, subprocess, sys, textwrap, urllib.parse, urllib.request, webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT / "workspace"
CONFIG_PATH = ROOT / "config.json"
DEFAULT_CONFIG = {"model": "qwen2.5-coder:1.5b", "ollama_url": "http://127.0.0.1:11434", "max_turns": 6}

SYSTEM = """You are Hermes, a careful local-first laptop assistant. Be concise and practical.
You use tools instead of pretending to do things. Never claim an action succeeded unless a tool confirms it.
Before any risky action (writing/deleting files, running commands, opening URLs), ask for user approval by using the tool.
Prefer read-only inspection first. Use the workspace folder unless the user explicitly names another location.
If a request is unclear or destructive, explain what you need and ask a focused question.
"""

def load_config():
    if CONFIG_PATH.exists():
        try: return {**DEFAULT_CONFIG, **json.loads(CONFIG_PATH.read_text(encoding="utf-8"))}
        except Exception: pass
    return DEFAULT_CONFIG.copy()

def approval(label: str) -> bool:
    answer = input(f"\n[APPROVAL REQUIRED] {label}\nAllow? [y/N]: ").strip().lower()
    return answer in {"y", "yes"}

def safe_path(raw: str) -> Path:
    p = Path(os.path.expandvars(os.path.expanduser(raw)))
    if not p.is_absolute(): p = WORKSPACE / p
    return p.resolve()

def tool_list_files(path="."):
    p = safe_path(path)
    if not p.exists(): return {"error": f"Not found: {p}"}
    if not p.is_dir(): return {"error": f"Not a directory: {p}"}
    return {"path": str(p), "items": [{"name": x.name, "type": "dir" if x.is_dir() else "file", "size": x.stat().st_size if x.is_file() else None} for x in sorted(p.iterdir())]}

def tool_read_file(path):
    p = safe_path(path)
    if not p.exists() or not p.is_file(): return {"error": f"File not found: {p}"}
    try: return {"path": str(p), "content": p.read_text(encoding="utf-8", errors="replace")[:20000]}
    except Exception as e: return {"error": str(e)}

def tool_write_file(path, content):
    p = safe_path(path)
    if not approval(f"Write {len(content)} characters to {p}"): return {"cancelled": True}
    try:
        p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8")
        return {"ok": True, "path": str(p), "bytes": len(content.encode())}
    except Exception as e: return {"error": str(e)}

def tool_run_powershell(command):
    if not approval(f"Run PowerShell command:\n{command}"): return {"cancelled": True}
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", command], text=True, capture_output=True, timeout=60)
        return {"returncode": out.returncode, "stdout": out.stdout[-12000:], "stderr": out.stderr[-6000:]}
    except Exception as e: return {"error": str(e)}

def tool_web_search(query):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HermesPortable/0.1"})
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
        import re
        links = re.findall(r'nofollow" class="result__a" href="(.*?)"[^>]*>(.*?)</a>', html)
        clean = lambda s: re.sub(r"<.*?>", "", s).replace("&amp;", "&")
        return {"query": query, "results": [{"title": clean(t), "url": u} for u,t in links[:8]]}
    except Exception as e: return {"error": str(e)}

def tool_open_url(url):
    if not approval(f"Open this URL in your browser?\n{url}"): return {"cancelled": True}
    webbrowser.open(url); return {"ok": True, "url": url}

TOOLS = {
 "list_files": ("List files in a directory. Relative paths use the portable workspace.", {"type":"object","properties":{"path":{"type":"string"}},"required":[]}, tool_list_files),
 "read_file": ("Read a text file (read-only). Relative paths use the portable workspace.", {"type":"object","properties":{"path":{"type":"string"}},"required":["path"]}, tool_read_file),
 "write_file": ("Create or replace a text file; requires approval.", {"type":"object","properties":{"path":{"type":"string"},"content":{"type":"string"}},"required":["path","content"]}, tool_write_file),
 "run_powershell": ("Run a PowerShell command; requires approval. Use only when needed.", {"type":"object","properties":{"command":{"type":"string"}},"required":["command"]}, tool_run_powershell),
 "web_search": ("Search the public web; returns result links.", {"type":"object","properties":{"query":{"type":"string"}},"required":["query"]}, tool_web_search),
 "open_url": ("Open a URL in the default browser; requires approval.", {"type":"object","properties":{"url":{"type":"string"}},"required":["url"]}, tool_open_url),
}

def ollama_chat(cfg, messages):
    payload = {"model": cfg["model"], "messages": messages, "stream": False, "tools": [{"type":"function","function":{"name":n,"description":d,"parameters":s}} for n,(d,s,_) in TOOLS.items()]}
    req = urllib.request.Request(cfg["ollama_url"] + "/api/chat", data=json.dumps(payload).encode(), headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=180) as r: return json.loads(r.read())

def main():
    WORKSPACE.mkdir(exist_ok=True)
    cfg = load_config()
    print("Hermes Portable Agent 0.1 | local-first laptop assistant")
    print(f"Model: {cfg['model']} | Workspace: {WORKSPACE}")
    print("Type /help for commands, /quit to exit. Risky actions always ask first.\n")
    messages = [{"role":"system","content": SYSTEM}]
    while True:
        try: user = input("You> ").strip()
        except (EOFError, KeyboardInterrupt): print(); break
        if not user: continue
        if user in {"/quit","/exit"}: break
        if user == "/help": print("Ask normally. Commands: /help, /reset, /quit. Put files in the workspace folder for safe access."); continue
        if user == "/reset": messages = [{"role":"system","content": SYSTEM}]; print("Conversation reset."); continue
        messages.append({"role":"user","content": user})
        try:
            for _ in range(cfg.get("max_turns", 6)):
                response = ollama_chat(cfg, messages)
                msg = response.get("message", {})
                messages.append(msg)
                calls = msg.get("tool_calls") or []
                if not calls:
                    print("\nHermes> " + (msg.get("content") or "(no response)")); break
                for call in calls:
                    fn = call.get("function", {}); name = fn.get("name"); args = fn.get("arguments", {})
                    if isinstance(args, str): args = json.loads(args)
                    if name not in TOOLS: result = {"error": "Unknown tool"}
                    else:
                        try: result = TOOLS[name][2](**args)
                        except Exception as e: result = {"error": str(e)}
                    messages.append({"role":"tool", "tool_name": name, "content": json.dumps(result)})
            else: print("Hermes> I stopped after the tool-step limit. Please continue if needed.")
        except urllib.error.URLError:
            print("\nHermes> I cannot reach Ollama. Install/start Ollama and pull the configured model, then try again.")
        except Exception as e: print(f"\nHermes> Error: {e}")

if __name__ == "__main__": main()