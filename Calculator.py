#Aakanksha Mokhriwale
#CodSoft Internship
#Task 2 - CALCULATOR 

#For Display
print()
print("-----------------------------------------------------------------------------------------------------------------------------")
print("\t"*7, " ***CALCULATOR***")
print("-----------------------------------------------------------------------------------------------------------------------------") 
print()

#Choices of Operations to do for user
print("Choices :")
print("\t 1.Addition")
print("\t 2.Subtraction")
print("\t 3.Multiplication")
print("\t 4.Division")
print("\t 5.Exit")
print()


#Asking for a choice from user and continuing till the user chooses the option to exit
#Taking Two input numbers and displaying result
Flag = True
while Flag == True:
    ch=int(input("Enter your choice (1-5) -- "))
    print()
    if ch==1:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)+int(num2))
        print()
    elif ch==2:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)-int(num2))
        print()
    elif ch==3:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)*int(num2))
        print()
    elif ch==4:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , float(num1)/float(num2))
        print()
    elif ch==5:
        Flag = False
        print("Thank Youu !!")
    else:
        print("Wrong Input !! Try Again ...")
        print()

