
# coding: utf-8

# # PingPong Game
# One morning at 6:00 AM, I just did this simple pong game from our childhood for my kids.

# In[1]:


import turtle
import os #if you want to use some sound for the game just add your wav sound clip where apropriate.


# In[2]:


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width =800, height=600)
wn.tracer(0)


# In[3]:


#Score
score_a = 0
score_b = 0


# In[4]:


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# In[5]:


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# In[6]:


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2


# In[7]:


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Ahmet Ferit: 0   Eralp: 0", align="center", font= ("Courier", 24, "normal"))


# In[8]:


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    

#Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# In[9]:


while True:
    wn.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay thunder.wav&")
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("afplay thunder.wav&")
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Ahmet Ferit: {} Eralp: {}".format(score_a, score_b), align="center", font= ("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Ahmet Ferit: {} Eralp: {}".format(score_a, score_b), align="center", font= ("Courier", 24, "normal"))
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40) :
        ball.setx(340)
        ball.dx *= -1
        #os.system("afplay thunder.wav&")
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40) :
        ball.setx(-340)
        ball.dx *= -1
        #os.system("afplay thunder.wav&")

