# password finder
# codeSwifz

import time

password = "342"

print("cracking paword....")

for i in range(1000):
    guess = str(i).zfill(3)
    print("Trying", guess)
    time.sleep(0.05)

    if guess == password:
        print("password cracked💀")
        print("password is :", guess)
        break