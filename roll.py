import random

playing = True
while True:
 choice = input('roll the dice(y/n): ')
 if choice == 'y':
    dice1 =  random.randit(1,6)
    dice2 = random.randit(1,6)
    print(f'({dice1}, {dice2}')
elif choice == 'n':
    print("congratulation you won🎉🎉🎉🎉🎉")
    break
else:
    print("null and void")