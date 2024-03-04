#CodSoft Internship
#Aakanksha Mokhriwale

#Task 5  - Contact Book

import pickle

MyFile=open("PhoneBook.dat","wb")

print("Welcome To Virtual Phone Book")
print("-----------------------------")

#Creates a PhoneBook File
def CreateMyFile(MyFile):
    PhoneBook={}
    print("Hey ! Add your Friend's Name and Phone Number here !!")
    while True:
        FrdName=input("Enter Your Friend's NAME :")
        FrdPhone=int(input("Enter Friend's PHONE NUMBER :"))
        PhoneBook[FrdName]=FrdPhone
        que=input("Want to add more Numbers of your Friend's :?(Yes/No)")
        if que.upper()=="NO":
            break
    pickle.dump(PhoneBook,MyFile)
    MyFile.close
    return

#Calling Function to Create a PhoneBook File
CreateMyFile(MyFile)
print("Your PhoneBook File Created Succesfully !")

#Reads your Phone Book (Friend Name: Phone Number)
def ReadPb(MyFile):
    print("See your phone Book ! It Contains:...")
    try:
        PhoneB=pickle.load(MyFile)
        for ch in PhoneB:
            print(ch,":",PhoneB[ch])
    except EOFError:
        print("**End Of Phone Book File**")
    MyFile.close()

#Adds a friend and his/her number in the Phone Book
def AddPb(MyFile):
    PhoneB=pickle.load(MyFile)
    MyFile.close()
    MyFile=open("PhoneBook.dat","wb")
    FrdName=input("Enter Your Friend's NAME :")
    FrdPhone=int(input("Enter Friend's PHONE NUMBER :"))
    PhoneB[FrdName]=FrdPhone
    pickle.dump(PhoneB,MyFile)
    print("Your Friends Name and Phone Number added Succesfully !")
    MyFile.close()
   

#Deletes a friend name and phone number from PhoneBook
def DelPb(MyFile):
    PhoneB=pickle.load(MyFile)
    MyFile.close()
    RemFrd=input("Enter you Friend NAME , whose number you want to delete:")
    if RemFrd in PhoneB:
        del PhoneB[RemFrd]
        MyFile=open("PhoneBook.dat","wb")
        pickle.dump(PhoneB,MyFile)
        MyFile.close()
    else:
        print("Oops , No Friend found in PhoneBook ")
    return

#Updates Phone number of a friend
def UpdPb(MyFile):
    PhoneB=pickle.load(MyFile)
    MyFile.close()
    FrdName=input("Enter Your Friend's NAME whose number you want to modify:")
    if FrdName in PhoneB:
        FrdPhone=int(input("Enter Friend's updated PHONE NUMBER :"))
        PhoneB[FrdName]=FrdPhone
        MyFile=open("PhoneBook.dat","wb")
        pickle.dump(PhoneB,MyFile)
        print(FrdName,"'s Phone Number updated Succesfully !")
    else:
        print("Oops , No such Friend Found .....")
    MyFile.close()
    return
   

#Menu
print("----------------------")
while True:
        print()
        print("\t\t\t~~~Phone Book Options !")
        print()
        print("1.READ your PhoneBook !!")
        print("2.INSERT a New Friend's Phone Number !")
        print("3.DELETE a Friend's Phone Number !")
        print("4.UPDATE a Freind's Phone Number !")
        print("5.EXIT")
        print("----------------------")
        que=input("Choose your option (1-5) ::")
        MyFile=open("PhoneBook.dat","rb")
        if que=="1":
            ReadPb(MyFile)
        elif que=="2":
            AddPb(MyFile)
        elif que=="3":
            DelPb(MyFile)
        elif que=="4":
            UpdPb(MyFile)
        elif que=="5":
            print("Exiting.......!!")
            print("Thank You ! Come Again")
            MyFile.close()
            break
        else:
            print("Sorry Wrong input ! Try to enter number from 1-5...")
           
MyFile.close()
