#ICP2 700757522
#Program 1

#1.a)Write a program that takes two strings from the user: first_name, last_name. Pass these variables to fullname function that should return the (full name) For example:▪ First_name = “your first name”, last_name = “your last name” and ▪ Full_name = “your full name”
First_name = ( input("Your First Name : "))
last_name = (input("Your Last Name : "))
Full_Name = print(First_name + last_name)
#1.B)Write function named “string_alternative” that returns every other char in the full_name string. 
#Str = “Good evening”
#Output: Go vnn
def string_alternative(Str):
    output = ""
    for a in range(len(Str)):
        if a % 2 == 0:
            output += Str[a]
    return output
print(string_alternative("Good evening"))

#Program 2

#Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.Finally store the output in output.txt file. 
#Example:
#Input: a file includes two lines:1.Python Course 2.Deep Learning Course
file1 = open('input.txt', 'r')
counts = dict()
data = file1.read()
words = data.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

f = open('output.txt', 'w')
f.write(data)
f.write('\nword_count:\n')
for key, value in counts.items():
    f.write(f"{key}: {value}\n")
f.close()

#Program 3

# Write a program, which reads heights (inches.) of customers into a list and convert these heights to centimeters in a separate list using:
#1) Nested Interactive loop.
#2) List comprehensions

L1=list(map(float,input().split()))
L2=[]
for x in L1:
    x=x*2.54
    L2.append(x)
print(L2)

L1=list(map(float,input().split()))
L2=[x*2.54 for x in L1]
print(L2)

