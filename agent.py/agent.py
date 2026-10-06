import ollama
import pyttsx3
import os

# 1. Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speaking speed

def speak(text):
    print(f"\n🤖 Agent: {text}\n")
    engine.say(text)
    engine.runAndWait()

# 2. Define Tools for the Agent
def create_text_file(filename: str, content: str) -> str:
    """Creates a local text file with specified content."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"File '{filename}' created successfully."
    except Exception as e:
        return f"Failed to create file: {str(e)}"

# Map string tool names to Python functions
available_tools = {
    'create_text_file': create_text_file
}

# 3. Agent Execution Loop
def run_agent(user_prompt):
    messages = [
        {"role": "system", "content": "You are a helpful local voice assistant. Keep answers concise and clear."},
        {"role": "user", "content": user_prompt}
    ]

    # Send prompt + tools to Ollama
    response = ollama.chat(
        model='qwen2.5-coder:1.5b',
        messages=messages,
        tools=[create_text_file]
    )

    # Check if the model decided to use a tool
    if response.message.tool_calls:
        for tool in response.message.tool_calls:
            function_name = tool.function.name
            function_args = tool.function.arguments
            
            if function_name in available_tools:
                print(f"🔧 Executing Tool: {function_name}({function_args})")
                tool_output = available_tools[function_name](**function_args)
                
                # Append tool result and request final answer
                messages.append(response.message)
                messages.append({'role': 'tool', 'content': tool_output})
                
                final_response = ollama.chat(model='qwen2.5-coder:1.5b', messages=messages)
                speak(final_response.message.content)
    else:
        # Speak response directly
        speak(response.message.content)

# 4. Start the Loop
if __name__ == "__main__":
    speak("Agent ready. Type your command below.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        run_agent(user_input)