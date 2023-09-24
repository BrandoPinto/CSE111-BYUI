#Week02
#The previous lesson’s prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:

#1.Gets the current date from the computer’s operating system.
#2.Opens a text file named volumes.txt for appending.
#3.Appends to the end of the volumes.txt file one line of text that contains the following five values:
    #a.current date
    #b.width of the tire
    #c.aspect ratio of the tire
    #d.diameter of the wheel
    #e.volume of the tire

import math
from datetime import datetime

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

total = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

print(f"\nThe approximante volume is: {total: .2f} liters")

total = round(total, 2)
today = datetime.now()
today = f"{today: %Y-%m-%d}"

with open('volumes.txt', "a") as volume_file:
    volume_file.write(f"\nCurrent date: {str(today)}"
                      f"\nWidth = {str(w)}"
                      f"\nAspect ratio of the tire is = {str(a)}"
                      f"\nDiameter of the wheel is = {str(d)}"
                      f"\nVolume of the tire is = {str(total)}")