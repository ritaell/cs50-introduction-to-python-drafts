'''
i = 3
while i != 0:
    print("meow")
    i = i - 1


i = 0
while i < 3:
    print("meow")
    i += 1 #-> i = i + 1

for i in range(3):
    print("meow")

print("meow\n" * 3 end="")
'''


 

while True:
    n = int(input("how many meows do you want? "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")

