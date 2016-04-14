import webbrowser
import time

break_count=1
total_breaks=3

print("This program started on "+time.ctime())
#The details of how time.ctime, webbrowser works is hidden from us
#The concept is called Abstraction
while (break_count<=3):
    time.sleep(60*60*2) #delay for 2 hours
    webbrowser.open("https://www.youtube.com/watch?v=VRJ7BEsmuDY")
    break_count=break_count+1
print("This is opening a browser for the lasttime on "+time.ctime())
