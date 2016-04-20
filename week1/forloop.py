someNumbers = {1: "one", 2: "two", 3: "three", 4: "four"}

for num in someNumbers:
    print("my num is: " + str(num))
    print("my vaule is: " + someNumbers[num])
######
for num in someNumbers:
    if num == 3:
        continue
    print("my num is: " + str(num))
    print("my vaule is: " + someNumbers[num])
######

for num in range(0,20):
    if num % 3:
        continue
    print(str(num))

#########
for (num, sample) in someNumbers:
    if num == 3:
        continue
    print("my num is: " + str(num))
    print("my vaule is: " + someNumbers[num])
    #############
