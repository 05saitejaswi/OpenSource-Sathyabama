
import turtle 

painter = turtle.Turtle()

painter.pencolor("brown")

 # Let's go counterclockwise this time 
    
painter.pencolor("gray")
for i in range(60):
    painter.forward(180)
    painter.left(121)

   
painter.pencolor("green")
for i in range(60):
    painter.forward(180)
    painter.right(121)
    
    painter.pencolor("gray")
for i in range(60):
    painter.backward(180)
    painter.left(121)
painter.pencolor("gray")
for i in range(60):
    painter.backward(180)
    painter.right(121)
 
    
turtle.done()
