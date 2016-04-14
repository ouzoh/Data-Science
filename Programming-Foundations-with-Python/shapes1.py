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
        fega.right(120)
        fega.forward(60)
        k=0
        while (k<3):
            fega.right(45)
            fega.forward(50)
            k=k+1       
        i=i+1
    
    window.exitonclick()
draw_multisquare()
