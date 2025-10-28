import turtle
import time
import random
# start values being set
delay = 0.1
score = 0
high_score = 0
apples_eaten = 0

# Setup screen
wn = turtle.Screen()
wn.title("Math Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head Properties
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food Properties
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Math challenge function
def math_challenge(round_num):
    global score

    # Random operation
    ops = ['+', '-', '*', '/']
    op = random.choice(ops)

    # Make it harder each round
    min_num = 1 * round_num
    max_num = 10 * round_num
    a = random.randint(min_num, max_num)
    b = random.randint(min_num, max_num)

    # Make division clean
    if op == '/':
        a = a * b
        correct = round(a / b, 2)
    elif op == '*':
        correct = a * b
    elif op == '+':
        correct = a + b
    else:
        correct = a - b

    # Ask player
    question = f"Round {round_num}: What is {a} {op} {b}?"
    try:
        answer = turtle.textinput("Math Challenge!", question)
        if answer is None:
            turtle.textinput("Result", "No answer! -10 points.")
            score -= 10
        else:
            answer = float(answer)
            if round(answer, 2) == round(correct, 2):
                turtle.textinput("Result", "✅ Correct! +15 points!")
                score += 15
            else:
                turtle.textinput("Result", f"❌ Wrong! Answer was {correct}. -10 points.")
                score -= 10
    except:
        turtle.textinput("Result", "Invalid input! -10 points.")
        score -= 10

    # RE-ENABLE movement after question
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

# Keyboard setup
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Border collision
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        apples_eaten = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Courier", 24, "normal"))

    # Eat food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        apples_eaten += 1

        # Trigger math every 5 apples
        if apples_eaten % 5 == 0:
            round_num = apples_eaten // 5
            math_challenge(round_num)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Courier", 24, "normal"))

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            apples_eaten = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
