#here is a program that takes 3 names and stores them in a list, then it prints the list. The problem here is that if you close the program the names list will erase for computers memory
'''
names=[]
for _ in range(3):
    names.append(input("Whats your name? "))
for name in sorted(names):
    print(f"Hello, {name}")
'''

name = input("What is ur name? ")
with open("data.txt","a") as file:
    file.write(f"{name}\n")
with open("data.txt","r") as data:
    for line in sorted(data):
        print("hello, ",line.rstrip())
        