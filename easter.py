def doomsday(y):
    if y>1582: 
        a = (2+y+y//4-y//100+y//400) % 7
    
    else: 
        a = (y+y//4) % 7
    
    doomsday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Jumu\'ah", "Sabbath"]
   # Jumu'ah is because Muslims pray on Fridays
   # Sabbath is because Jewish must not work on Saturdays
    return doomsday[a]
    
def leap(y):
   return (y%4 == 0 and y%400 != 0) or (y % 400 == 0) if y > 1582 else y % 4 == 0

def easter(y):
    """
    This function uses Gaussian Paschal algorithm to find Easter
    """
    a = y%19
    b = y%4
    c = y%7
    if y>1582:
        k = y//100
        p = (13+8*k)//25
        q = k//4
        M = (15-p+k-q)%30
        N = (4+k-q)%7
    
    else:
        M = 15
        N = 6
    
    d = (19*a+M)%30
    e = (2*b+4*c+6*d+N)%7
    day = 22+d+e # March
    month = 3
    if day > 31:
        day = d+e-9 #April
        month +=1
        
    if (d==28 and e==6 and (11*M+11)%30<19):
        day = 18
        month = 4
        
    if (d==29 and e==6):
        day = 19
        month = 4
        
    return (day, month)
    
def dominical(y):
    if y>1582: 
        a = (2+y+y//4-y//100+y//400) % 7
    
    else: 
        a = (y+y//4) % 7
        
    if leap(y):
        dominical = ["DC", "CB", "BA", "AG", "GF", "FE", "ED"]
        
    else:
        dominical = ["C", "B", "A", "G", "F", "E", "D"]
        
    if y !=1582:
        return dominical[a]
        
    else: 
        return "GC" 
        #The year the Gregorian Calendar started: 4 October 1582 is the day before... 15 October 1582!

y = 2024
easter = easter(y)
print(f"Doomsday for {y} is {doomsday(y)}.")
print(f"{y} is a {'leap' if leap(y) else 'normal'} year.")
print(f"Dominical letter: {dominical(y)}")
print(f"Easter is on {'March' if easter[1] == 3 else 'April'} {easter[0]}.")
