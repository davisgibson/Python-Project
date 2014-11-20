print 'Enter two numbers.'
num1 = int(raw_input())
num2 = int(raw_input())

def add():
    num3 = num1 + num2
    print 'Your answer is ' + str(num3)
def subtract():
    print 'would you like to 1.) First Number - Second Number or 2.) Second Number - First Number?'
    yes = raw_input()
    if yes == '1':
        num3 = num1 - num2
        print 'Your answer is ' + str(num3)
    if yes == '2':
        num3 = num2 - num1
        print 'Your answer is ' + str(num3)
def multiply():
    num3 = num1 * num2
    print 'Your answer is ' + str(num3)
def divide():
    print 'Would you like to do 1.) First Number / Second Number, or 2.) Second Number / First Number?'
    no = raw_input()
    if no == '1':
        num3 = num1 / num2
        print 'Your answer is ' + str(num3)
    if no == '2':
        num3 = num2 / num1
        print 'Your answer is ' + str(num3)

print 'Would you like to add, subtract, multiply, or divide? Type "more" for more options.'
modifier = raw_input()
if modifier == 'add':
    add()
if modifier == 'subtract':
    subtract()
if modifier == 'multiply':
    multiply()
if modifier == 'divide':
    divide()
if modifier == 'more':
    print 'Would you like to use the 1.) Pothagorean theorem, 2.)'
    more = raw_input()
    if more == 1:
        print 'Enter the length of the first leg.'
        leg1 = int(raw_input())
        print 'Enter the length of the second leg.'