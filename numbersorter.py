# Program 1: Number Sorter
# Create a program that ask 4 numbers.
# Print the 4 numbers from highest to lowest using only if-else statement.

print("Hello, kindly put your 4 numbers below for me to arrange it from highest to lowest.")

# Steps
#1. Ask for 4 numbers
num1= float(input("Enter your first number: "))
num2= float(input("Enter your second number: "))
num3= float(input("Enter your third number: "))
num4= float(input("Enter your fourth number: "))

#2. Arrange from highest to lowest
def high_to_low(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        if num2 >= num3 and num3 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num2}, {num3}, and {num4}.")
        elif num2 <= num3 and num2 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num3}, {num2}, and {num4}.")
        elif num2 <= num4 and num2 >= num3:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num4}, {num2}, and {num3}.")
        elif num2 >= num4 and num4 >= num3:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num2}, {num4}, and {num3}.")
        elif num4 >= num3 and num3 >= num2:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num4}, {num3}, and {num2}.")
        else:
            if num3 >= num4 and num4 >= num2: 
                print(f"\nThank you! Your arrangement is as follows: {num1}, {num3}, {num4}, and {num2}.")


    if num2 >= num1 and num2 >= num3 and num2 >= num4:
        if num1>= num4 and num4 >= num3:
            print(f"\nThank you! Your arrangement is as follows: {num2}, {num1}, {num4}, and {num3}.")   
        elif num1 <= num4 and num4 >= num3:
            print(f"\nThank you! Your arrangement is as follows: {num2}, {num4}, {num1}, and {num3}.")
        elif num1 >= num3 and num3 >= num4:
            print (f"\Thank you! Your arrangement is as follows: {num2}, {num1}, {num3}, and {num4}.")
        elif num1 <= num3 and num1 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num2}, {num3}, {num1}, and {num4}.")
        elif num3 >= num4 and num4 >= num1:
            print(f"\nThank you! Your arrangement is as follows: {num2}, {num3}, {num4}, and {num1}.")
        else:
            if num3 <= num4 and num3 >= num1:
                print(f"\nThank you! Your arrangement is as follows: {num2}, {num4}, {num3}, and {num1}.")

    if num3 >= num1 and num3 >= num2 and num3 >=num4:
        if num2 >= num4 and num4 >= num1:
            print(f'\nThank you! Your arrangement is as follows: {num3}, {num2}, {num4}, and {num1}.')
        elif num4 >= num2 and num2 >= num1:
            print(f"\nThank you! Your arrangement is as follows: {num3}, {num4}, {num2}, and {num1}.")
        elif num4 >= num1 and num1 >= num2:
            print(f"\nThank you! Your arrangement is as follows: {num3}, {num4}, {num1}, and {num2}.")
        elif num4 <= num1 and num2 >= num1:
            print(f"\nThank you! Your arrangement is as follows: {num3}, {num2}, {num1}, and {num4}.")
        elif num1 <= num2 and num1 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num3}, {num2}, {num1}, and {num4}.")
        elif num1 >= num4 and num4 >= num2:
            print(f"\nThank you! Your arrangement is as follows: {num3}, {num1}, {num4}, and {num2}.")
        else:
            if num1 >= num2 and num2 >= num4:
                print(f"\nThank you! Your arrangement is as follows: {num3}, {num1}, {num2}, and {num4}.")
    
    if num4 >= num1 and num4 >= num2 and num4 >= num3:
        if num3 >= num2 and num2 >= num1:
            print(f"\nThank you! Your arrangement is as follows: {num4}, {num3}, {num2}, and {num1}.")
        elif num2 >= num1 and num1 >= num3:
            print(f"\nThank you! Your arrangement is as follows: {num4}, {num2}, {num1}, and {num3}.")
        elif num2 >= num3 and num3 >= num1:
            print(f"\nThank you! Your arrangement is as follows: {num4}, {num2}, {num3}, and {num1}.")
        elif num1 <= num3 and num1 >=num2:
            print(f"\nThank you! Your arrangement is as follows: {num4}, {num3}, {num1}, and {num2}.")
        elif num1 >= num3 and num3 >= num2:
            print(f"\nThank you! Your arrangement is as follows: {num4}, {num1}, {num3}, and {num2}.")
        else:
            if num1 >= num2 and num2 >= num3:
                print(f"\nThank you! Your arrangement is as follows: {num4}, {num1}, {num2}, and {num3}.")
#3. What if theres equal numbers?
def equal_numbers(num1, num2, num3, num4):
        if num1 == num2 and num3 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num2}, {num3}, and {num4} \n or \n {num1}, {num3}, and {num4}.")
        elif num1 == num2 and num4 >= num3:
            print(f"\nThank you1 Your arrangement is as follows: {num1}, {num2}, {num4}, and {num3} \n or \n {num1}, {num4}, and {num3}.")
        elif num1 == num3 and num2 >= num4:
            print(f"\nThank you! Your arrangement is as follows: {num1}, {num3}, {num2}, and {num4} \n or \n {num1}, {num2}, and {num4}.")
        else:
            if num3 == num4 and num2 >= num1:
                print(f"\nThank you! Your arrangement is as follows: {num3}, {num4}, {num2}, and {num1} \n or \n {num3}, {num2}, and {num1}.")

high = high_to_low(num1, num2, num3, num4)
equal = equal_numbers(num1, num2, num3, num4)

