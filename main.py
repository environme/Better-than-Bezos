import turtle
import random
import time
#import turtle random and time

#setup background
background = turtle.Screen()
background.bgcolor("lightpink")

#setup gameboard 
gameboard = turtle.Turtle()
gameboard.penup()
gameboard.setpos(00.0,00.0)

#function to draw grameboard
def box(turtle, amount):
  turtle.pd()
  turtle.speed(speed=0)
  for x in range(1,5):
    for x in range(1, amount+1):
      turtle.forward(75) 
      for x in range(1,5):
        turtle.left(90)
        turtle.forward(75)
    turtle.right(90)

box(gameboard, 4)


#instructions
print("\nWelcome to Better than Bezos!\nWill you match up against the all-consuming Jeff Bezos, the black turtle?"),
print("\nYou and Bezos will have a starting balance of $500. The first person to reach $600 WINS! Each turn, Bezos' money increases depending on how much he moves."),

#counter for money
total_money = 500

#function to print the current balance
def currentBalance(total_money):
  print("Balance: " + str(total_money))

#setup turtles
tina = turtle.Turtle()
tina.shape("turtle")
tina.hideturtle()
george = turtle.Turtle()
george.shape("turtle")
george.hideturtle()
computer = turtle.Turtle()
computer.shape("turtle")

#user chooses character
character = input("\nFirst, choose your character! (Type turtle or circle.)")
print("Nice choice, " + character + "!")

#if user chooses turtle
if character == "turtle":
  tina.showturtle()
  tina.shape("turtle")
  tina.color("white")
  tina.penup()
  character = tina

#if user chooses circle
if character == "circle":
  george.showturtle()
  george.shape("circle")
  george.color("white")
  george.penup()
  character = george

time.sleep(2)

#college or no college by random choice
#list for college or no college
firstPathInput = input("Will you go to college? Press enter to find out!")
firstPathList = ["college", "no college"]
firstPath = random.choice(firstPathList)

#list for jobs
noCollegeJobList = ["Starbucks", "Sephora", "Influencer"]
noCollegeJob = random.choice(noCollegeJobList)

#if collegethey pay $50 for tuition
if firstPath == "college":
  total_money -= 50
  print("\nYou will! You got accepted to DSST University.")
  print("But...you lost $50 from cost of tuition :(")
  print("Total balance: $" + str(total_money))
  print("\nNow roll the dice to continue!")
#if no college, they get a random job
else:
  print("\nYou didn't get accepted into any college :(")
  print("\nLuckily, you're not in crippling debt and can start woking.")
  print("Total balance: $" + str(total_money))
  if noCollegeJob == "Starbucks":
    print("\nYou got hired at Starbucks! You make $5 every other roll, and your first payday is right now")
    total_money += 5
    print("\nYour new balance is: $" + str(total_money))
    print("\nNow roll the dice, to continue your journey in life!")
  elif noCollegeJob == "Sephora":
    print("\nYou got hired at Sephora! You make $10 every other roll, and your first payday is right now")
    total_money += 10
    print("\nYour new balance is: $" + str(total_money))
    print("\nNow roll the dice, to continue life!")
  else:
    print("\nYou are a tik toker! Unfortunately, you aren't too popular yet, so you make $1 every other roll, and your first payday is right now")
    total_money += 1
    print("\nYour new balance is: $" + str(total_money))
    print("\nNow roll the dice to continue!")

#tracks how many spaces you have moved
moved_spaces = 0
totalRolls = 0
def moveOneSpace(turtle, dice):
  for i in range(1, dice+1):
    turtle.forward(75)
    if turtle.xcor() == 300 and turtle.ycor() == 0:
      turtle.right(90)
    if turtle.xcor() == 300 and turtle.ycor() == -300:
      turtle.right(90)
    if turtle.xcor() == 0 and turtle.ycor() == -300:
      turtle.right(90)

#function for the turtle to move forward
def move(turtle, moved_spaces, totalRolls):
  dice = random.randint(1, 4)
  print("You rolled a: " + str(dice))
  turtle.penup()
  moved_spaces += dice
  moveOneSpace(turtle, dice)


computerTotalMoney = 500
#function for the computer turtle to move forward
def computerMove(turtle, computerDice):
  #computerDice = random.randint(1,4)
  print("Bezos rolled a: " + str(computerDice))
  turtle.penup()
  moveOneSpace(turtle, computerDice)
  


#function for rolling the dice
def newRoll(moved_spaces, totalRolls):
  dice = random.randint(1,4)
  roll = input("Press enter to roll the dice: ")
  move(character, moved_spaces, totalRolls)
  computerMove(computer, computerDice)

#pose question and check answer 
def checkAnswer(total_money):
  print("STOP!!! You must answer this question. If you get it right, you'll win money! If not, you'll loose money.")
  print("To answer, type A, B, C, or D (Remember to capitalize!)")

  #questions for the user
  questions = [
  "What would Mr. Temple order at Taco Bell? (A) grilled cheese burrito, B) chicken chalupa, C) apple epanada)",
  "What is Mr. Temple's favorite 2000s punk rock band? (A) One Direction, B) Fall Out Boy, C) Good Charlotte)",
  "What band does Mr. Temple think of when he drinks a Baja Blast? (A) One Republic, B) Good Charlotte, C) Green Day)",
  "If Mr. Temple had a mix tape, what would he call it? (A) Sounds from Temple, B) Trap or Die, C) Cocaine and Caviar)",
  "Who is Mr. Khan's favorite musical artist? (A) Da Baby, B) Lil Huddy, C) Drake, D) Lil Wayne)",
  "What is Mr. Khan's favorite TV show to binge on Netflix? (A) Friday Night Lights, B) The Office, C) Bling Empire)",
  "What car does Mr. Khan own? (A) Lamborghini, B) Bugatti, C) G-Wagon, D) Honda CRV)",
  "What was Mr. Khan's high school superlative? (A) Shiniest head, B) longest beard, C) Most Likely to Succeed, D) Most Likely to Fail)",
  ]

  #asks the user questions that they have to answer
  questionPicker = random.choice(questions)
  answer = input(questionPicker)
  index = questions.index(questionPicker)
  # question 1
  if index == 0:
    if answer =="A":
      print("That's correct! Now you know what to get Mr. Temple when you need to bribe him ;)")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ It's ok. I don't even know what taco bell is. you lost $10.")
      total_money -= 10
      print("\nYour new balance is: $" + str(total_money))
  # question 2
  if index == 1:
    if answer =="B":
      print("That's correct! Fall Out Boy is Mr. Temple's favorte band - what a weirdo ;)")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ I bet you guessed 1D because honoestly they are the best. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 3
  if index == 2:
    if answer =="B":
      print("That's correct! The fact that he thinks of a band when drinking a baja blast is kind of questionable...")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ Don't feel bad, I don't think anyone can really guess this one. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 4
  if index == 3:
    if answer =="A":
      print("That's correct! Sounds of Temple can imply Mr. Temple himself or the sounds of a literal temple LOL.")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ We suggested Trap or Die but its whatever. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 5
  if index == 4:
    if answer =="C":
      print("That's correct! I'm sure everyone knows this one :)")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 6
  if index == 5:
    if answer =="A":
      print("That's correct! I honestly don't even know what show this is :/")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ FRIENDS > THE OFFICE just saying. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 7
  if index == 6:
    if answer =="D":
      print("That's correct! It's ok Mr. Khan a CRV is still really cool :(")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ Mr. Khan wishes he has this car. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  # question 8
  if index == 7:
    if answer =="C":
      print("That's correct! I guess the superlative was accurate")
      if firstPath == "college":
        print("\n Because you answered correctly, you earned a scholarship! Your tuition is covered and you earned an extra $50. Congrats!")
        total_money += 50
        print("\nYour new balance is: $" + str(total_money))
      elif firstPath == "no college":
        print("\n Because you answered correctly, you earned a bonus! You earned $25.")
        total_money += 25
        print("\nYour new balance is: $" + str(total_money))
    else:
      print("Oop that's wrong :/ Come on you know better than this, smh. You lost $10.")
      total_money -= 100
      print("\nYour new balance is: $" + str(total_money))
  questions.remove(questionPicker)

pen = turtle.Turtle()
 
# draw eye on smiley face
def eye(col, rad):
  pen.down()
  pen.fillcolor(col)
  pen.begin_fill()
  pen.circle(rad)
  pen.end_fill()
  pen.up()
# 
def drawSmiley():
  # draw face
  pen.fillcolor('red')
  pen.begin_fill()
  pen.circle(100)
  pen.end_fill()
  pen.up()
  
  # draw eyes
  pen.goto(-40, 120)
  eye('white', 15)
  pen.goto(-37, 125)
  eye('black', 5)
  pen.goto(40, 120)
  eye('white', 15)
  pen.goto(40, 125)
  eye('black', 5)
  
  
  # draw mouth
  pen.goto(-40, 85)
  pen.down()
  pen.right(90)
  pen.circle(40, 180)
  pen.up()


while 1>0:
  
  computerDice = random.randint(1,4)
  newRoll(moved_spaces, totalRolls)
  totalRolls += 1
  for i in range(1, computerDice + 1):
    computerTotalMoney += 10
    if total_money == 600:
      print("YOU WIN! Congratulations big boy.")
      raise SystemExit()
    if computerTotalMoney  == 600:
      print("Bezos has $" + str(computerTotalMoney))
      print("OH NO! BIG BOY BEZOS CONSUMES ALL.")
      background.bgcolor("black")
      character.hideturtle()
      drawSmiley()
      raise SystemExit()
  print("Bezos has $" + str(computerTotalMoney))
  if totalRolls%2 == 0:
    checkAnswer(total_money)
  elif totalRolls == 3:
    secondPathInput = input("Will you get married? Press enter to find out!")
    secondPathList = ["marriage", "no marriage"]
    secondPath = random.choice(secondPathList)
    if secondPath == "marriage":
      print("You married the love of your life! But you have to pay for your wedding now")
      total_money -= 25
      print("Your new balance is: " + str(total_money))
    else: 
      print("#single forever")
      print("Fortunately you don't have to pay for a crappy wedding so your balance stays the same")
      print("Your total balance is: " + str(total_money))
  elif totalRolls == 5:
    thirdPathInput = input("Do you want kids? Let's find out")
    thirdPathList = ["1 Kid", "3 Kids", "10 Kids"]
    thirdPath = random.choice(secondPathList)
    if thirdPath == "1 Kid":
      print("You have 1 kid")
      total_money -= 80
      print("Your new balance is: " + str(total+money))
    elif thirdPath == "3 Kids": 
      print("You have 3 kids")
      total_money -= 90
      print("Your total balance is: " + str(total_money))
    else:
      print("You have 10 kids...Yikes")
      total_money -= 100
      print("Your total balance is: " + str(total_money))


#haha hello