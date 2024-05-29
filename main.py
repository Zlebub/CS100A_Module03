# Examples
# Adding lists
'''first = ['this','is','a','list']
evens = [2,4,6,8,10]
students = ['abigail','ben','christi','dave']

print(first)
# what happens when we add two lists?
print(evens + students)
# Fancy things I can do with a list
evens = [2*x for x in range(1,6)]

for e in evens:
    print(str(e) + ' is 2 * ' + str(int(e/2)))
# My programs
# Adding to the list
team = []

player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)
team.sort()

print('your team is: ')
for p in team:
    print("\t" + p)

if 'Xavier' in team:
    print("I can't wait to play")
else:
    print("Put me in coach, I'm ready to play.")
# Tuples
team=[('Rowan', 2, 'pg'), 
    ('Garrett', 10, 'sg'), 
    ('JT', 11, 'c'), 
    ('Miguel', 14, 'pf'), 
    ('Liam', 20, 'sf')
]

for player in team:
    # break out the parts for each player
    (name, number, position) = player
    print('starting at ' + position + ', number ' + str(number) + ', ' + name)
# Grocery
glist = []
gtotal = []
gitem = ''
while gitem != 'done':
    gitem = input('Enter a grocery item, or enter done to finish: ')
    if gitem != 'done':
        glist.append(gitem)
print('Time to buy your groceries! ')
while len(glist) != 0:
    gitem = input('What have you gotten? ')
    if gitem in glist:
        glist.pop(gitem)
    gcost = input('Whats the price? ')
    gquan = input('How many? ')
    greceipt = (gitem, gcost, gquan)
    gtotal.append(greceipt)
print('You have successfully gotten your groceries! Heres what you got: ')
print(gtotal)
'''
# base for math tutoring system
import random as rand
equstore = []
def genequ():   # a frankly terrible way to choose which mathematical operation to use
    global res
    global equ
    num1 = rand.randint(1, 20)
    num2 = rand.randint(1, 20)
    equsym = rand.randint(1, 4)
    if equsym == 1:
        equ = print(f'What is {num1} + {num2}')
        res = (num1+num2)
    elif equsym == 2:
        equ = print(f'What is {num1} - {num2}')
        res = (num1-num2)
    elif equsym == 3:
        equ = print(f'What is {num1} * {num2}')
        res = (num1*num2)
    elif equsym == 4:
        equ = print(f'What is {num1} / {num2}')
        res = (num1/num2)
       
i = 1
mname=input('What is your name? ')  # the actual program start
while i <= 10:
    genequ()
    ures=int(input('Please enter the answer: '))
    ans = 'True'
    fans = ures
    while ures != res:
        print('Sorry, try again')
        ans = 'False'
        ures=int(input('Please enter the answer: '))
    equstore.append(equ, fans, ans)
    i = i + 1
print('Alright, lets see what problems you had, what you first answered, and whether that was correct or not.')
print(equstore)