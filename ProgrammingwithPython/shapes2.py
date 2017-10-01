import turtle
def draw_multishapes():
    #We need a screen
    #We can make the screen any color
    #e.g. purple
    window=turtle.Screen()
    window.bgcolor("purple")
    
    fega=turtle.Turtle()
    fega.shape("turtle")
    fega.color("green")
    fega.speed(1)
    
    i=j=l=m=k=0
    while (i<6):
        fega.forward(30)
        fega.right(-60)
        i=i+1
    while (j<6):
        fega.forward(30)
        fega.right(60)
        j=j+1
    while (l<6*(60/10)):
        fega.forward(15)
        fega.right(10)
        l=l+1
    while (m<6*(60/10)):
        fega.forward(15)
        fega.right(-10)
        m=m+1    
    jodi=turtle.Turtle()
    jodi.shape("arrow")
    jodi.color("red")
    jodi.circle(100)
    jodi.circle(-100)
    
    yaya=turtle.Turtle()
    yaya.shape("arrow")
    yaya.color("black")
    while (k<100):
        yaya.speed(6)
        yaya.forward(100)
        yaya.right(120-k/10)
        k=k+1
    window.exitonclick()
    
draw_multishapes()
