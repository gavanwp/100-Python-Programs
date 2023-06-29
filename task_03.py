

def is_leap(year):
    leap = False
    leap_year = True
    
    # Write your logic here
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
               return leap_year
            else:
                return leap
        else:
          return  leap_year
    else:            
        return leap

year = int(input())
print(is_leap(year))