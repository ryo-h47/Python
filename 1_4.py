quiz_list=[
    ["What is the real name of the character, Krista?", "Annie", "Mikasa", "Historia", 3],
    ["Who is Toji's son?", "Megumi", "Yuji", "Panda", 1],
    ["What devil is the character, Power?", "Blood", "Bomb", "Gun", 1]
]

import random
random.shuffle(quiz_list)

for quiz in quiz_list:
    print("[Quiz]")
    print(quiz[0])
    for i in range(3):
        no=i+1
        print(str(no) + ": " + quiz[no])

    user=int(input("What is your answer?"))

    ans=quiz[4]
    if(user==ans):
        print("Correct!")
    else:
        print("Wrong...the answer is " + quiz[ans])

        print("---")