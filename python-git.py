# print (" how many lines do you want ")
# lines = int(input("enter the line amount"))
# for i in range(1,lines):
#     print("*" * i)

# rows = 5

# # Upper pyramid
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2*i - 1))


# # Lower inverted pyramid
# for i in range(rows-1, 0, -1):
#     print(" " * (rows - i) + "*" * (2*i - 1))
row = 8

for i in range(row):
    for j in range(row):
        if i == 0 or i == row - 1 or j == 0 or j == row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

         