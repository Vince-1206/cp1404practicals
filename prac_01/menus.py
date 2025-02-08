# Get the user's name
name = input("Enter name: ")

# Display the menu
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)

# Get the user's choice
choice = input(">>> ").upper()

# Menu loop
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    # Display the menu again and get the next choice
    print(menu)
    choice = input(">>> ").upper()

# finished
print("Finished.")

"""
GET name
DISPLAY "(H)ello\n(G)oodbye\n(Q)uit"
GET choice
CONVERT choice to uppercase

WHILE choice is not equal to "Q"
    IF choice is equal to "H" THEN
        DISPLAY "Hello" and name
    ELSE IF choice is equal to "G" THEN
        DISPLAY "Goodbye" and name
    ELSE
        DISPLAY "Invalid choice"
    ENDIF
    DISPLAY "(H)ello\n(G)oodbye\n(Q)uit"
    GET choice
    CONVERT choice to uppercase
ENDWHILE

DISPLAY "Finished."

"""
