import random

while True:

    print("welcome to Stone Paper Scissor game!!🎮🚀")

    print("only three attempts are possible😁")

    choices=["stone", "paper" ,"scissor"]

    user_score=0
    computer_score=0

    attempts=1

    while attempts<=3:

        computer_choice=random.choice(choices)

        user_choice=input(f"attempt{attempts} - enter your choice:").lower()

        if user_choice not in choices:
            print("enter valid name😁!!")
            break

        print(f"your choice is(👨🏻) -{user_choice}")
        print(f"computer choice is(🖥️) -{computer_choice}")

        if user_choice==computer_choice:
            print("tie!!😉")

        elif user_choice=="stone" and computer_choice=="scissor":
            print("you won!!🏆")
            user_score+=10
            break
        elif user_choice=="paper" and computer_choice=="stone":
            print("you won!!🏆")
            user_score+=10
            break
        elif user_choice=="scissor" and computer_choice=="paper":
            print("you won!!🏆")
            user_score+=10
            break

        else:
            print("you lose , bad luck!!🙁")
            computer_score+=10

        attempts+=1

    if attempts>3:
        print("game over!!❌😩")

    print(f"your final score is(👨🏻) - {user_score} 🎉")
    print(f"computer final score is(🖥️) - {computer_score} 🎉")


    print("You want to play again? 😇(yes/no)") 
    if input().lower()=="yes":  
        continue
    else:
        print("Thanks for playing!!✌️")
        break




