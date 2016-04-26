"""
Easy Mode item #1
"""

sentence = "List Comprehensions are the Greatest!"
vowels = ('a','e','i','o','u')
#non_list = []
#for l in sentence:
#    if not l in vowels:
#        non_list.append(l)
#nonvowels = ''.join(non_list)

nonvowels = ''.join([l for l in sentence if not l in vowels])

print(nonvowels)

"""
Easy Mode item #2
"""

grades = {'Inara': {'Homework 1': 90, 'Homework 2': 94, 'Homework 3': 90}, 'Mal': {'Homework 1': 50, 'Homework 2': 100, 'Homework 3': 60}, 'Simon': {'Homework 1': 98, 'Homework 2': 96, 'Homework 3': 96}, 'River': {'Homework 1': 100, 'Homework 2': 100, 'Homework 3': 0}}
average_score = {}
for name in grades:
    total = 0
    for assigment in grades[name]:
        total += grades[name][assigment]
    average = total/3
    average_score[name] = average
print(average_score)

dictionary = {name: sum(grades[name].values())/len(grades[name]) for name in grades}
print(dictionary)

"""
Easy Mode item #3 not able to call Ventura, pet detective!
"""

words = []
with open('/usr/share/dict/words', 'r') as f:
    # for line in if:
    #     word = line.strip()
    #     if word.endswith("ace"):
    words = [line.strip() for line in f if line.endswith('ace\n')]

print(words)
