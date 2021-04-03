"""
Write a function called mul_time that takes a Time object and a number and returns a new Time object 
that contains the product of the original Time and the number.
"""

class Time():
   def __init__(self,hour,minute,second):
       self.hour=hour
       self.minute=minute
       self.second=second

def mul_time(time,n):
    mul_time=time()
    mul_time.hour=time.hour * n
    mul_time.minute=time.minute * n
    mul_time.second=time.second * n

    remainder_s=mul_time.second % 60
    quotient_s=mul_time.second//60
    mul_time.second =remainder_s
    mul_time.minute += quotient_s

    remainder_m=mul_time.minute % 60
    quotient_m=mul_time.minute // 60
    mul_time.minute=remainder_m
    mul_time.hour +=quotient_m

    return mul_time

