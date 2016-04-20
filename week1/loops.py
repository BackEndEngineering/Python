nameList = []
name = "none"

#while True:
while bool(name):
    name = input("Enter your name: ")

    if name:
        nameList.append(name)

while nameList:

    print("Hello, " + nameList.pop() + "!")
print("All done")
#List of Names

iters = 5
while iters:
    print("Iter numbers; " + str(iters))
    iters = iters - 1
