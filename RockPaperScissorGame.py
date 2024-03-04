#CodSoft Internship
#Aakanksha Mokhriwale 

#Task 4 - Rock Paper Scissors Game



from random import *
print("________________________________________ ** ROCK - PAPER - SCISSORS ** ____________________________________________________")
print()

#List of Our Options to Play
choice= ["Rock" , "Paper" , "Scissors"]

#Asking User for how much points they want to play
pt=int(input("For how many points you want to play : "))
print()

#Creating and Maintaining User and Computer's Point
UserPts=0
CPts=0

#Displaying Three Options from the user can choose from
print("1.Rock \n2.Paper \n3.Scissors\n")

print("ALL THE BEST !\n")

#Taking Inputs from User
#Calculating Points 
for i in range(pt):
    opt=input("Enter your Choice : ")
    comp=choice[randint(0,2)]
    if opt==comp:
        print("Tie !")
        print()
    elif opt=="1":
        if comp=="Paper":
            CPts+=1
            print("Computer gets a point !")
        elif comp=="Scissor":
            UserPts+=1
            print("You get a point")
        print()
    elif opt=="2":
        if comp=="Rock":
            UserPts+=1
            print("You get a point !")
        elif comp=="Scissor":
            CPts+=1
            print("Computer gets a point")
        print()
    elif opt=="3":
        if comp=="Rock":
            CPts+=1
            print("Computer gets a point !")
        elif comp=="Paper":
            UserPts+=1
            print("You get a point")
        print()
    else:
        print("Enter a correct choice !!")


#Displaying Scores
print("YOUR SCORE :" , UserPts ,"\t\t", "COMPUTER'S SCORE:" , CPts)
print()

#Declaring the Winner
if UserPts==CPts:
    print("Its a Tie ")
elif UserPts>CPts:
    print("Congo ! You are a winner !!")
else:
    print("Computer Wins... !")


    
            
