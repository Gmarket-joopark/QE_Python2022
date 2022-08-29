
#for number in range(1, 11):
#  print("Number {}".format(number))


#temp_f = 40
#while temp_f > 32:
#    print("The water is {} degrees.".format(temp_f))
#    temp_f -= 1

#temp_f = 40
#while temp_f > 32:
#    print("The water is {} degrees.".format(temp_f))
#    temp_f -= 1
#    if temp_f == 33:
#        break

#for number in range(1,11):
#    if number == 7:
#        print("We're skipping number 7.")
#        continue
#    print("This is the number {}.".format(number))

#for number in range(1,11):
#    if number == 3:
#        pass
#    else:
#        print("The number is {}.".format(number))

on = True
def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)

def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)

def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

# enclose selection into while loop

while on:
    operation = input("Please type +, -, *, /, or q: ")
    if operation == '+':
        add()

    elif operation == '-':
        subtraction()

    elif operation == '*':
        multiply()

    elif operation == '/':
        divide()

    elif operation == 'q':
        calc_on = False

    else:
        print("That operation is not available.  ")
