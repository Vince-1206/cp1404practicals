"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

"""
DISPLAY "Enter score: "
GET score

IF score is less than 0 OR score is greater than 100 THEN
    DISPLAY "Invalid score"
ELSE IF score is greater than or equal to 90 THEN
    DISPLAY "Excellent"
ELSE IF score is greater than or equal to 50 THEN
    DISPLAY "Passable"
ELSE
    DISPLAY "Bad"
ENDIF

"""