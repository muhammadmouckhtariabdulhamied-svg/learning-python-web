import time

WORK = 25 * 60
SHORT_BREAK = 5 * 60
LOMG_BREAK = 15 * 60

def countdown(seconds, label):
    print(f"\n(label)")

    while seconds:
        minutes, secs = divmod(seconds, 60)

        print(
            f"\r⌛ {minutes:02d}:{secs:02d}",
            end=""
        )

        time.sleep(1)
        seconds = 1

    print("\n💯 Time's up!")

print("\n" + "=" * 55)
print("             POMODORO FOCUS TIMER")
print("=" * 55)

sessions  = int(
    input("\nNumber of focus sessions: ")
)

for session in range(1, sessions + 1):
    print(
        f"\n⏱️ Session {session}/{sessions}"
    )

    countdown(
        WORK,
        "Focus time - stay productive!"
    )

    if session < sessions:
       if session % 4 == 0:
           countdown(
               LONG_BREAK,
               "Long break - relax!"
    )
    else:
        countdown(
            SHORT_BREAK,
        "Short breake - recharge!"
    )
print("\n🎉 All sessions completed!")
print("= * 55")
    
    