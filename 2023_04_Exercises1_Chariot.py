#Exercise 1: Famous Quote
def famous_quote():
    autor = "The Dude"
    quote = "'When you have such friends, you don't need enemies'."
    print(autor + " once said," + quote)

famous_quote()

#Exercise 2: Number Eight
def number_eight():
    a, b, c, d, e = 2, 4, 5, 6, 16
    print(a+d)
    print(a*b)
    print(c*a-a)
    print(int(e/a))
    print(a*b)

number_eight()

#Exercise 3: Formatting
def name_age():
    name = input("What's your name?:")
    age = input("How old are you?:")
    print("Hello " + name.title() + ". You are " + age + " years old.")
    Example2 = "Hello {}. You are {} years old."
    print(Example2.format(name.capitalize(),age))
    print(f"Hello {name.capitalize()}. You are {age} years old.")

name_age()

#Exercise 4: Swap
def swap_integer():
    a = input("Please enter a:")
    b = input("Please enter b:")
    print("a=" + a + ", b=" + b)
    a, b = b, a
    print("value of 'a' after swaping:" + a + " value of 'b' after swaping:" + b)

swap_integer()

#Exercise 5: Modulo check
def  check_numbers(number1, number2):
    if int(number1)%6 ==0 or int(number2)%6 == 0:
        print("At least one number is divisible by 6.")
    else:
        print("No number is divisible by 6.")
    if int(number1)%10 > 0 and int(number2)%10 > 0:
        print("Both numbers are not divisible by 10.")
    else:
        print("One or both number are divisible by 10.")
check_numbers (input("Enter one number:"), input("Enter a second number:"))

#Exercise 6: Summarizer
def sum_up(number1, number2):
    numbers = [(number1), (number2),()]
    x, y = int(number1), int(number2)+1
    total = sum(range(x,y))
    if number1 < number2:
        print("The sum of all numbers in range " + str(x) + "-" + str(number2) + " is " + str(total))
    else:
        numbers.append(input("Choose number 2 greater than number 1:"))
        z = int(numbers[-1])+1
        total2 =sum(range(x,z))
        print("The sum of all numbers in range " + str(x) + "-" + str(z) + " is " + str(total2))
sum_up(input("enter a number:"), input("Enter a second number:"))

#Exercise 7: String check












