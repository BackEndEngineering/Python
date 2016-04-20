


personList = []
colorList = []
ageList = []
mylist = ""
print("""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        |||^^^^^|||^^^||||^^^||^^^^^^^^|||||||||||||||||||||||||||||||||||
       ||||^^|^^^|||^^^^^^^^||||||^^||||||||||||||^^^^^||^^^|||||^||||||||
       ||||^^||^^^|||||^^|||||||||^^|||^||||||^|||^|||^||^||^||||^||||||||
       ||||^^|||^^^^|||^^|||||||||^^|||^||||||^|||^|||^||^|||^|||^||||||||
       ||||^^^^^^^|||||^^|||||||||^^|||^^^^^^^^|||^^||^||^||||^||^||||||||
       ||||^^||||||||||^^|||||||||^^|||^||||||^|||^|||^||^|||||^|^||||||||
       ||||^^||||||||||^^|||||||||^^|||^||||||^|||^|||^||^||||||^^||||||||
       ||||^^||||||||||^^||||||||||||||^||||||^|||^^^^^||^||||||^^||||||||
       ||||^^|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
       |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
       |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
       _____________________Welcome to Python_____________________________""")
print("Welcome to PYTHON PRISON CAMP!")
name = input("What is your name:")
print("Welcome, Officer "+name+"!")
print("The object of the game is to capture the prisoner 666 that escaped from his prison cell 13.")
choice = input("You life will be in danger! Do you still want to play this game y/n?")
if choice == "Y":
    while "y" in mylist.lower():
        print("Then give me the names of people you care about?")
        person = input("Give me a name?:")
        color = input("What is their favorite color?:")
        age = input("How old is this person?:")
        User[key_list] = { "Give me a name?": person, "What is their favorite color?": color, "How old is this person?": age}
        mylist = input("Do you want to continue adding people that you care about? Please y/n ")
        ageList.append(age)
        personList.append(person)
        colorList.append(color)
        if "y" in mylist.lower():
            continue
    while personList:
        print("You will be sorry! You friends have been capture")
        print("person:" + personList.pop() + " color:" + colorList.pop() + " age:" + ageList.pop(), end=' --- ')
        print("")









#while True:
#    name = input("what is your name?:")
#    color = input("what is your favorite color?:")
#    Age = input("How old are you?:")
#    User[ident] = { "what is your name?": name, "what is your favorite color?": color, "How old are you?": Age}
#    mylist = input("Do you want to continue adding people? Please type yes or no. ")

#    if mylist in ("No", "no", "NO"):
#        if len("No", "no", "NO") == 0:
#            print(input)
#            break
#        print(mylist)
#    if name in ("yes", "Yes", "YES"):
#        continue
