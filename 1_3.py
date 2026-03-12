import random
import time

win=0
draw=0
lose=0

for i in range(3):
    time.sleep(1)
    print("■ Rock-paper-scissors " + str(i+1) + "time")
    print("> 0:Rock 1:Scissors 2:Paper")

    com=random.randint(0,2)
    you=int(input("Which one do you choose?"))
    
    print("Computer's choise is: " + str(com))
    time.sleep(1)

    n=(com-you+3)%3

    if n==0:
        print("Draw")
        draw+=1
    elif(n==1):
        print("You win\(^o^)y")
        win+=1
    else:
        print("You lose(T_T)")
        lose+=1

    print("---")

time.sleep(1)
print("The result is")
time.sleep(1)
print(str(win) + "wins " + str(draw) + "draws " + str(lose) + "loses ")
time.sleep(1)
print("So the winner is...")
time.sleep(2)
if win>lose:
    print("You!!")
elif(win<lose):
    print("Computer...")
else:
    print("Both of you.")