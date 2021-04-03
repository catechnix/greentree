"""
In that case, it is not enough to carry once; we have to keep doing it until time.second is less than
sixty. One solution is to replace the if statements with while statements. 
That would make the function correct, but not very efficient.
Write a correct version of increment that doesn’t contain any loops.
"""

class Time():
   def __init__(self,hour,minute,second):
       self.hour=hour
       self.minute=minute
       self.second=second

# this is modifier function
def increment(time, seconds):
    time.second += seconds

    remainder_s=time.second % 60
    quotient_s=time.second//60
    time.second =remainder_s
    time.minute += quotient_s

    remainder_m=time.minute % 60
    quotient_m=time.minute // 60
    time.minute=remainder_m
    time.hour +=quotient_m
    
    return time
