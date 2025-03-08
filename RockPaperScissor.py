import random

def Try_again():
    user_input = int(input("try again? 1.yes 2.no :: "))
    if user_input == 1:
        user_choice = int(input("1.Rock 2.paper 3.scissor :: "))
        RPS_choice(user_choice)
    elif user_input == 2:
        print("see you next time! ")
        return
    else:
        print("invalid input")
        Try_again()

def RPS_choice(X):
    choices = random.choice(["Rock", "Paper", "Scissor"])
    # 1 : rock// 2: paper// 3: scissor

    match X:
        case 1:
            if choices == "Rock":
                print("Computer chose Rock too!")
                Try_again()
            elif choices == "Paper":
                print("Computer chose Paper, You lost hahaha")
                Try_again()
            elif choices == "Scissor":
                print("Computer chose Scissor, you win! GG.")
                Try_again()
            else:
                print("invalid input")
                Try_again()
        case 2:
            if choices == "Rock":
                print("Computer chose Rock, you lost hahaha")
                Try_again()
            elif choices == "Paper":
                print("Computer chose Paper too!")
                Try_again()
            elif choices == "Scissor":
                print("Computer chose Scissor, you win! GG.")
                Try_again()
            else:
                print("invalid input")
                Try_again()
        case 3:
            if choices == "Rock":
                print("Computer chose Rock, you lost hahaha")
                Try_again()
            elif choices == "Paper":
                print("Computer chose Paper, you win! GG.")
                Try_again()
            elif choices == "Scissor":
                print("Computer chose Scissor too!")
                Try_again()
            else:
                print("invalid input")
                Try_again()
        case _:
            print("invalid input")
            Try_again()

print("Welcome to Rock Paper Scissor !!")
user_choice = int(input("1.Rock 2.paper 3.scissor :: "))
RPS_choice(user_choice)
