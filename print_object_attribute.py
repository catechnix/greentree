"""
Write a function called print_time that takes a Time object and prints it in the form hour:minute:second. 
"""

class Time():
   def __init__(self,hour,minute,second):
       self.hour=hour
       self.minute=minute
       self.second=second


present_time=Time(12,5,34)

def print_time(time):
    time_text="The present time is {:2d}:{:2d}:{:2d}"
    print(time_text.format(time.hour,time.minute,time.second))

print_time(present_time)

