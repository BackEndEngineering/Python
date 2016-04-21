# Populate the "prisoners" dictionary with data from user input
# prisoner +  <id>: <name>, cell: <cell>), ...)
# prisoners = [ {id: <ID>, name: <name>, cell: <cell>), ...}]
# created libary
#prisoners = {}
#ident = "default"

#while True: #fixme: what is our condition?

#    ident = input("Enter id:")
#    if ident == "":
#        prisoners[ident] = { "name": name, "cell": cell}
#    print(prisoners)

#    name = input("eneter Name: ")
#    cell = input("Cells:")

#    prisoners[ident] = { "name": name, "cell": cell}
#print(prisioners)
prisoners = {}

ident = "default"

# while <>:
#     while <>:
#         while <>:
#             continue

while ident:
    ident = input("Enter ID: ")
    if ident == "":
        continue

    name = input("Enter Name: ")
    cell = input("Cell: ")

    prisoners[ident] = { "name": name, "cell": cell }

    print(prisoners)
