import turtle

def draw_multisquare():

    window=turtle.Screen()
    window.bgcolor("purple")
    
    fega=turtle.Turtle()
    fega.shape("turtle")
    fega.color("green")
    fega.speed(0)
    
    i=0
    while (i<120):
        fega.right(120-2)
        fega.forward(200)   
        i=i+1
    
    window.exitonclick()
draw_multisquare()
