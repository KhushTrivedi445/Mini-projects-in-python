import random
Pwin=0
Cwin=0

print("Welcome to the game of Rock🪨 Paper📄 Scissor✂")
name=input("What is your name?")
while Pwin!=5 and Cwin!=5:
    player=input("Please choose(Rock🪨/Paper📄/Scissor✂)").lower()
    if player=='rock' or player=='scissor' or player=='paper':
        comp = ['rock', 'scissor', 'paper']
        comp_player = random.choice(comp)

        print(f"{name}={player} and computer🖥={comp_player}")

        if (player==comp_player):
            print("draw")

        elif((player=='rock' and comp_player=='scissor') or
            (player == 'scissor' and comp_player == 'paper')or
            (player == 'paper' and comp_player == 'stone')):
            Pwin=Pwin+1
            print(f"{name} won the round🥳🎊")
            print(f"Player ={Pwin} and Computer={Cwin}")

        else:
            Cwin=Cwin+1
            print("computer won the round🥳🎊")
            print(f"Player ={Pwin} and Computer={Cwin}")

    else:
        print("Invalid choice❎❎")

if Pwin==5:
    print(f"{name} won the game🥳🥳🎊🎉👯‍")
else:
    print("Computer🖥 won the game🥳🥳🎊🎉👯‍")