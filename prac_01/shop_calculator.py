total_price = 0

# input
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# total
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total price exceeds $100
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

"""
SET total_price TO 0
INPUT number_of_items AS INTEGER
WHILE number_of_items < 0 DO
    PRINT "Invalid number of items!"
    INPUT number_of_items AS INTEGER
END WHILE
FOR i FROM 1 TO number_of_items DO
    INPUT price AS FLOAT
    total_price = total_price + price
END FOR
IF total_price > 100 THEN
    total_price = total_price * 0.9
END IF
PRINT "Total price for {number_of_items} items is ${total_price:.2f}"

"""