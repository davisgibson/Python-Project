def add():
    print 'Enter your first number.'
    num1 = int(raw_input())
    x = 1
    y = 2
    list1 = []
    while x == 1:
        print 'Enter another number. If you would like to find the answer, type "add"'
        num = raw_input()
        if num != 'add':
            if y == 2:
                list1.append(num1)
                list1.append(num)
                y = 1
            elif y == 1:
                list1.append(num)
        if num == 'add':
            total = 0
            for i in list1:
                total = total + int(i)
            print 'Your answer is ' + str(total)
            x = 2
def average():
    print 'Enter a number'
    num1 = int(raw_input())
    x = 1
    y = 2
    list1 = []
    while x == 1:
        print 'Enter another number. If you would like to find the average, type "stop."'
        num = raw_input()
        if num != 'stop':
            if y == 2:
                list1.append(num1)
                list1.append(num)
                y = 1
            elif y == 1:
                list1.append(num)
        if num == 'stop':
            total = 0
            for i in list1:
                total = total + int(i)
            
            total = total / len(list1)
            print 'Your answer is ' + str(total)
            x = 2
def subtract():
    print 'Enter your first number.'
    num1 = int(raw_input())
    print 'Enter your second number.'
    num2 = int(raw_input())
    print 'would you like to 1.) First Number - Second Number or 2.) Second Number - First Number?'
    yes = raw_input()
    if yes == '1':
        num3 = num1 - num2
        print 'Your answer is ' + str(num3)
    if yes == '2':
        num3 = num2 - num1
        print 'Your answer is ' + str(num3)
def multiply():
    print 'Enter your first number.'
    num1 = int(raw_input())
    print 'Enter your second number.'
    num2 = int(raw_input())
    num3 = num1 * num2
    print 'Your answer is ' + str(num3)
def divide():
    print 'Enter your first number.'
    num1 = int(raw_input())
    print 'Enter your second number.'
    num2 = int(raw_input())
    print 'Would you like to do 1.) First Number / Second Number, or 2.) Second Number / First Number?'
    no = raw_input()
    if no == '1':
        num3 = num1 / num2
        print 'Your answer is ' + str(num3)
    if no == '2':
        num3 = num2 / num1
        print 'Your answer is ' + str(num3)
def pothag():
    print 'Enter the length of the first leg.'
    leg1 = int(raw_input())
    print 'Enter the length of the second leg. Press space and enter if there is no second leg.'
    leg2 = raw_input()
    if leg2 == ' ':
        print 'Enter the length of the hypotenuse.'
        hyp = int(raw_input())
        hyp = hyp * hyp
        leg1 = leg1 * leg1
        leg2 = hyp - leg1
        leg2 = leg2**.5
        print 'Your answer is ' + str(leg2)
    else:
        leg1 = leg1 * leg1
        leg2 = int(leg2) * int(leg2)
        leg3 = leg1 + int(leg2)
        leg3 = leg3**.5
        print 'The hypotenuse is ' + str(leg3)
def square():
    print 'Enter your base number.'
    num = int(raw_input())
    print 'to the power of-'
    num2 = int(raw_input())
    num3 = num**num2
    print 'Your answer is ' + str(num3)
def sqroot():
    print 'Enter a number you would like to find the square root of.'
    num = int(raw_input())
    num2 = num**.5
    print 'your answer is ' + str(num2)
x = 1
while(x==1):
    print ' '
    print ' '
    print 'Would you like to add, subtract, multiply, or divide? Type "more" for more options, or type "end" to end.'
    modifier = raw_input()
    if modifier == 'end':
        x=2
        print 'Ended!'
    if modifier == 'add':
        add()
    if modifier == 'subtract':
        subtract()
    if modifier == 'multiply':
        multiply()
    if modifier == 'divide':
        divide()
    if modifier == 'more':
        print 'Would you like to use the 1.) Pothagorean theorem, 2.) square something 3.) square root 4.) average'
        more = raw_input()
        if more == '1':
            pothag()
        if more == '2':
            square()
        if more == '3':
            sqroot()
        if more == '4':
            average()
        else:
            print 'Invalid input.'      