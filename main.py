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
    print("Put me in coach, I'm ready to play.")'''
# Grocery
