import phonenumbers
from phonenumbers import gecoder
import time, random

def start_phone_tracer(target):
    print(f'[+] phonrTracer v2.1 - OSNT')
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace ...")
    p = phonenumbers.parse(target, None)
    r = gecoder.description_for_number(p)
    print(f"[+] Location: {r}")
    print(f"[+] Trace complete")
start_phone_tracer("0236336655")