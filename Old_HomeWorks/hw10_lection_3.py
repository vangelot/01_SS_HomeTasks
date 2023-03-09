
from random import randint

n = randint(1, 100)

print("\033[38;2;201;100;59m Wellcome to the game \033[0;0m  \n "
      "you have to guess the number from \033[38;2;204;204;0m 1 to 100\033[0;0m\n"
      "you have \033[38;2;201;100;59m 6 attempts \033[0;0m\n"
      "good luck")
#print(n) #ця строка знадобиться для тесту

attempt_counter = 1
while attempt_counter <= 6:
    try:
        a = int(input("lets do "+str(attempt_counter)+" try: "))
    except:
        print("\nWrong input, you lost!!!")
        break
    if a == n:
        print("\n\033[38;2;124;252;0m YOU WIN!!! \033[0;0m")
        print("\nYou took ", attempt_counter, " attempts")
        break
    elif attempt_counter == 6:
        print("\n\033[38;2;255;160;122m YOU LOST!!! \033[0;0m")
        break
    else:
        if a > n:
            print("You entered Bigger number")
        else:
            print("You entered Smaller number")
        attempt_counter += 1


