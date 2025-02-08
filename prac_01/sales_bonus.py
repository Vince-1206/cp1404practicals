"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Calculating bonus for a single input
sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15

print(f"Bonus: ${bonus:.2f}")

#Loop

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15

    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("Thank you. Program terminated.")

"""
DISPLAY "Enter sales: $"
GET sales

WHILE sales is greater than or equal to 0
    IF sales is less than 1000 THEN
        bonus = sales * 0.10
    ELSE
        bonus = sales * 0.15
    ENDIF
    DISPLAY "Bonus: $" and bonus formatted to 2 decimal places

    DISPLAY "Enter sales: $"
    GET sales
ENDWHILE

DISPLAY "Thank you. Program terminated."
"""