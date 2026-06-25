
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:

           if year % 400 == 0:
                return True
           else:
                return False
        else:
            return True
    else:
         return False
try:
    num=int(input('enter a year to check if its a leap year'))
    print(is_leap(num))
except ValueError:
    print("enter an inter not word")

