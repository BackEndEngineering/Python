


personList = []
colorList = []
ageList = []
mylist = ""
print("""
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||^^^^^|||^^^||||^^^||^^^^^^^^|||||||||||||||||||||||||||||||||||
        ||||^^|^^^|||^^^^^^^^||||||^^||||||||||||||^^^^^||^^^|||||^||||||||
        |||^^||^^^|||||^^||||||||||^^|||^||||||^|||^|||^||^||^||||^||||||||
        |||^^|||^^^^|||^^||||||||||^^|||^||||||^|||^|||^||^|||^|||^||||||||
        |||^^^^^^^|||||^^||||||||||^^|||^^^^^^^^|||^|||^||^||||^||^||||||||
        |||^^||||||||||^^||||||||||^^|||^||||||^|||^|||^||^|||||^|^||||||||
        |||^^||||||||||^^||||||||||^^|||^||||||^|||^|||^||^||||||^^||||||||
        |||^^||||||||||^^|||||||||||||||^||||||^|||^^^^^||^||||||^^||||||||
        |||^^||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
       _____________________Welcome to Python_____________________________""")
print("Welcome to PYTHON PRISON CAMP!")
name = input("What is your name:")
print("Welcome, Officer "+name+"!")
print("The object of the game is to capture the prisoner 666 that escaped from his prison cell 13.")
cont = input("You life will be in danger! Do you still want to play this game y/n?")
prisoners = []
while "y" in cont.lower():
    print("Then give me the names of people you care about?")
    person = color = age =''
    while not (person) or (len(person.split())< 2):
        person = input("Give me a name?:")
    if not person:
        print("Invalid input, please start again!")
    while not color:
        color = input("What is their favorite color?:")
    if not color:
        print("Invalid input, please start again!")
    while not age or not age.isdigit():
        age = input("How old is this person?:")
    if not age:
        print("Invalid input, please start again!")
        continue
    inmate = { "name": person, "fav_color": color, "age": age}
    cont = input("Do you want to continue adding people that you care about? Please y/n ")
    prisoners.append(inmate)
    print("You will be sorry! You friends have been capture")
while prisoners:
    inmate = prisoners.pop()
    print("person:" + inmate["name"] + " color:" + inmate["fav_color"] + " age:" + inmate["age"])
    print ("")





#len tells how many letters
#llen with splits count words




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
