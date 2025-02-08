# a. Display all the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# c. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# d. Print n stars on one line
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()
for i in range(1, n + 1):
    print('*' * i)

"""
A.
FOR i FROM 1 TO 20 STEP 2 DO
    PRINT i ON THE SAME LINE
END FOR
PRINT A NEW LINE
B.
FOR i FROM 0 TO 100 STEP 10 DO
    PRINT i ON THE SAME LINE
END FOR
PRINT A NEW LINE
C.
FOR i FROM 20 TO 1 STEP -1 DO
    PRINT i ON THE SAME LINE
END FOR
PRINT A NEW LINE
D.
INPUT n AS INTEGER
FOR i FROM 1 TO n DO
    PRINT i STARS ON A NEW LINE
END FOR

"""