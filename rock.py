import random, re
dict = ["Rock","Paper","Scissors"]
pc_score = 0
my_score = 0

while True:
    pcchoice = random.randrange(1,3)
    mychoise = input("What is your choice (or write Exit to end game)")
    if mychoise.isdigit():
        if int(mychoise) <= 3:
            mychoice = dict[int(mychoise)-1]
            if mychoice == "Rock" and dict[pcchoice] == "Paper":
                print(mychoice + "vs." + dict[pcchoice] + ": You Lose")
                pc_score = pc_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))
            elif mychoice == "Rock" and dict[pcchoice] == "Scissors":
                print(mychoice + "vs." + dict[pcchoice] + ": You Win")
                my_score = my_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))

            elif mychoice == "Rock" and dict[pcchoice] == "Rock":
                print(mychoice + "vs." + dict[pcchoice] + ": Draw")
                print(" PC " + str(pc_score) + " | Player " + str(my_score))

            elif mychoice == "Paper" and dict[pcchoice] == "Paper":
                print(mychoice + "vs." + dict[pcchoice] + ": Draw")
                print(" PC " + str(pc_score) + " | Player " + str(my_score))
            elif mychoice == "Paper" and dict[pcchoice] == "Rock":
                print(mychoice + "vs." + dict[pcchoice] + ": You Win")
                my_score = my_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))
            elif mychoice == "Paper" and dict[pcchoice] == "Scissors":
                print(mychoice + "vs." + dict[pcchoice] + ": You Lose")
                pc_score = pc_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))

            elif mychoice == "Scissors" and dict[pcchoice] == "Paper":
                print(mychoice + "vs." + dict[pcchoice] + ": You Win")
                my_score = my_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))

            elif mychoice == "Scissors" and dict[pcchoice] == "Rock":
                print(mychoice + "vs." + dict[pcchoice] + ": You Lose")
                pc_score = pc_score + 1
                print(" PC " + str(pc_score) + " | Player " + str(my_score))

            elif mychoice == "Scissors" and dict[pcchoice] == "Scissors":
                print(mychoice + "vs." + dict[pcchoice] + ": Draw")
                print(" PC " + str(pc_score) + " | Player " + str(my_score))
        else:
            print("Incorrect input!!")


    else:
        print("Incorrect input!!")


