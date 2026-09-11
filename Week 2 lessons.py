print("Week 2 Coding")

#Sequential Control Flow
first = 3
second = 4
third = 5
print(first,second,third)
first,second,third = third,second,first
print(first,third)

#Conditional Control Flow: Boolean variable type
True == 1
False == 0
print(True+True)

#Conditional Control Flow: if/ elif/ else statement
food = "Fries"
price = 0.0
if food == "Burger":
    print("you chose burger")
    print("please pay me $8")
    price = 8.0
elif food == "Fries": 
    print("you chose fries")
    print("please pay me $2")
    price = 2.0
else:
    print("Sorry your choice is not available")

#Conditional Control Flow: Boolean expression
#To evaluates to either True or False

#Iteration (Loop) Control: while
walk_circle = 0
while walk_circle < 90:
    walk_circle = walk_circle + 1
print("Walking Completed")
print(walk_circle)

#Iteration (Loop) Control: infinite loops
#Forget to increment "Walk_circle" = Dead loop, program 'hanging', quit program execution: restart, Crtl + C
#Useful - while True = continuous input loop, server or event listener, game loop

#iteration (Loop) Control: for
walk_circle = 0
for walk_circle in range(5):
    print(walk_circle)
print("Walking Completed")
print(walk_circle)

#Break Statement
walk_circle = 0
for walk_circle in range (1,10):
    print(walk_circle)
    if walk_circle == 5:
        break
print("Walking Completed")
print(walk_circle)

#Continue Statement
walk_circle = 0
for walk_circle in range (1,10):
    if walk_circle == 5:
        continue
    print(walk_circle)
print("Walking Completed")
print(walk_circle)