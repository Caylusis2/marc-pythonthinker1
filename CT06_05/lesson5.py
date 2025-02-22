# print("Hello from lesson 5")

# for i in range(2, 26, 2):
#     print(i)

# for i in range(8, 104, 8):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(3, 0, -1):
#     print("Ready!")

start= int(input("Give me a number"))
end= input("Give me a number")

if start > end:
    for i in range(start, end-1, -1):
        print(i)
else: 
    for i in range(end, start-1, -1):
        print(i)




