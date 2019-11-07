from math import *
def basic(operation):
    if(operation == "1"):
        evaluation = 0
        n = input("How many numbers would you like to add? ")
    elif(operation == "2"):
        n = input("How many numbers would you like to subtract? ")
    elif(operation == "3"):
        evaluation = 1
        n = input("How many numbers would you like to multiply? ")
    nums = []
    for i in range(int(n)):
        num = input("- ")
        print(type(num))
        nums.append(num)
    if(operation == "2"):
        evaluation = nums[0]
    for i in range(len(nums)):
        if(operation == "1"):
            evaluation+=int(nums[i])
        elif(operation == "2"):
            evaluation = int(evaluation) - int(nums[i])
        elif(operation == "3"):
            evaluation*=int(nums[i])
    print(str(evaluation));
    
def integrate(c, function, n, a, b):
    #Riemann Sum
    summationVal = 0
    for i in range(1, n + 1):
        summationVal += f(a + ((i - (1/2)) * ((b - a) / n)), function)
    deltaX = ((b - a) / n)
    integral = summationVal * deltaX
    print("Integral is " + str(c * integral))

def f(x, function):
    for i in range(len(function)):
        if(function[i] == "^"):
            return x ** int(function[i + 1])
def root():
    num = int(input("What is the number you would like to find the square root of? "))
    lowerNum = 0
    higherNum = 0
    for i in range(1000):
        if((i ** 2) == num):
            print("sqrt(" + str(num) + ") = " + str(i))
        elif(i ** 2 < num and ((i + 1) ** 2 > num)):
            lowerNum = i
            higherNum = i + 1
            print("Between " + str(i) + " and " + str(i + 1))
            num2 = num / lowerNum
            print("Rough estimation of sqrt(" + str(num) + ") = " + str( (lowerNum + num2) / 2 ))
def derive():
    function = input("What function would you like to derive? ")
    #Using the formal definition:
    #limit as h apporaches 0 of ((f(x + h) - f(x) ) / h)
    x = int(input("Where would you like to find the derivative? "))
    h = 0.000000000000001
    print("d/dx[" + function + "] ~ " + str(((f(x + h, function) - f(x, function)) / h)))

def divide():
    print("What number would you like to divide? ")
    num1 = float(input("- "))
    print("What would wou like to divide it by? ")
    num2 = float(input("- "))
    print(str(num1 / num2))  

operation = 0
while operation != "Q":
    print("-----------------------------------------")
    print("Basic Calulator with Integral computation")
    print("-----------------------------------------")
    print("(1): +")
    print("(2): -")
    print("(3): x")
    print("(4): /")
    print("(5): square root")
    print("(6): derivative (using formal definition; not extremely accurate)")
    print("(7): integral (using rectangles with Riemann Sum)")
    print("(8): average(mean)")
    print("(Q): Quit program \n")
    operation = input("What operation would you like to perform? ")
    if operation == "1" or operation == "2" or operation == "3":
        basic(operation)
    elif operation == "4":
        divide()
    elif operation == "5":
        root()
    elif operation == "6":
        derive()
    elif operation == "7":
        function = input("What function would you like to evaluate? ")
        #default leading coefficient is 1
        constant = 1
        if(function[0] != "x"):
            constant = int(function[0])
            function = function[1:len(function):]
        lowerBound = int(input("What would you like your lower bound to be? "))
        upperBound = int(input("What would you like your upper bound to be? "))
        rect = int(input("How many rectangles should be used? "))
        integrate(constant, function, rect, lowerBound, upperBound)
    elif operation == "8":
        list1 = []
        n = int(input("How many numbers would you like to find the average of? "))
        for i in range(n):
            num = int(input((str(i + 1) + ": " )))
            list1.append(num)
        sum = 0
        for i in range(len(list1)):
            sum+=list1[i]
        average = sum / n
        print("The average of " + str(list1) + " is " + str(average))
    elif operation != "Q":
        print("Retry with a valid option. ")

