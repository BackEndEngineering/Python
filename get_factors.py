#Create a function to find the factors of an integer

#Create a function that finds the factors of a given number, and returns a list of tuples with those factors.

#For instance, get_factors(12) would return [(1, 12), (2, 6), (3, 4)]

def returning_a_tuple(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           t = (i, int(x/i))
           mytuple = tuple(t)
           print(mytuple)

num = int(input("Enter a number: "))
print(returning_a_tuple(num))
