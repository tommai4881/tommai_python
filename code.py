import os

def doomsday(y):
    """
    Returns the day of the week for the doomsday of the given year.
    The doomsday is a date that always falls on the same weekday for a given year, eg. last day of February, Pi day, 9-5 at 7-Eleven (May 9 (VE Day), July 11 (St Benedict's Day), September 5 (school starts in Vietnam), November 7 (October Revolution Day)), same day same month if even months not February.
    """
    if y > 1582: 
        a = (2 + y + y // 4 - y // 100 + y // 400) % 7
    else: 
        a = (y + y // 4) % 7
    
    doomsday_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Jumu'ah", "Sabbath"]
    # Jumu'ah is because Muslims pray on Fridays
    # Sabbath is because Jewish people must not work on Saturdays
    return doomsday_days[a]
    
def leap(y):
    """
    Determines whether a given year is a leap year.
    """
    if y > 1582:
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    else:
        return y % 4 == 0

def easter(y):
    """
    Returns the date of Easter for the given year using the Gaussian algorithm.
    """
    a = y % 19
    b = y % 4
    c = y % 7
    if y > 1582:
        k = y // 100
        p = (13 + 8 * k) // 25
        q = k // 4
        M = (15 - p + k - q) % 30
        N = (4 + k - q) % 7
    else:
        M = 15
        N = 6
    
    d = (19 * a + M) % 30
    e = (2 * b + 4 * c + 6 * d + N) % 7
    day = 22 + d + e  # March
    month = 3
    if day > 31:
        day = d + e - 9  # April
        month += 1
        
    if (d == 28 and e == 6 and (11 * M + 11) % 30 < 19):
        day = 18
        month = 4
        
    if (d == 29 and e == 6):
        day = 19
        month = 4
        
    return (day, month)

def memorial(y):
    """
    Returns the date for Jehovah's Witnesses' Memorial of Christ's Death, the only holiday of Jehovah Witnesses,
    who don't celebrate Easter nor Christmas nor birthdays (which they believe to be of pagan origin).
    This is originally based on algorithm on the BCP found in https://almanac.oremus.org/easter/computus/.
    """
    g = y%19+1
    if y>1582:
        s = (y-1600)//100-(y-1600)//400
        l = (8*(y//100-14))//25
        p = (3-11*g+s-l)%30
        if p == 29 or (p == 28 and g > 11):
            p -= 1
    else:
        p = (26-11*g)%30
    
    m = p-1

    if m<11: #March
        day = m+21
        month = 3
    else: # April
        day = m-10
        month = 4
    return day, month

def pascha(y):
    """
    Returns the date of Orthodox Easter for the given year using Meeus' Julian algorithm.
    """
    a = y % 4
    b = y % 7
    c = y % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    f = d + e + 114
    month = f // 31
    day = f % 31 + 1
    if day == 32: # 1 April = 32 March
        day -= 31
        month += 1
    return day, month

def dominical(y):
    """
    Returns the dominical letter(s) for the given year.
    The dominical letter indicates the Sunday of a given year.
    """
    if y > 1582: 
        a = (2 + y + y // 4 - y // 100 + y // 400) % 7
    else: 
        a = (y + y // 4) % 7
        
    if leap(y):
        dominical_letters = ["DC", "CB", "BA", "AG", "GF", "FE", "ED"]
    else:
        dominical_letters = ["C", "B", "A", "G", "F", "E", "D"]
        
    if y != 1582:
        return dominical_letters[a]
    else: 
        return "GC"  # The year the Gregorian Calendar started: 4 October 1582 is the day before... 15 October 1582!
    
def indiction(y):
    """
    Returns the indiction cycle for a given year, used in historical calendar systems.
    """
    return (y+2)%15+1

def solar(y):
    """
    Returns the solar cycle for a given year, used in certain calendrical systems.
    """
    return (y+8)%28+1

def epact(y):
    """
    Returns the epact for a given year, used in determining the date of Easter.
    """
    return y%19+1

def julianperiod(y):
    """
    Returns the Julian Period for a given year, a chronological system used in astronomy.
    """
    return y+4713

def sexagenary(y):
    """
    I am a native Vietnamese programmer, so I prefer cat over rabbit in 2023, 2011, etc.
    But as I respect other traditions of sinophone like VN. I add parentheses to add alternate animals.
    Returns the stem and branch of the sexagenary cycle for a given year.
    The sexagenary cycle is used in Chinese astrology and Vietnamese tradition.
    """
    a = (y-3)
    stem = a%10
    stem_letter = ["Water", "Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water"]
    # 甲乙 = wood; 丙丁 = fire; 戊己 = earth; 庚辛 = metal; 壬癸 = water
    branch = a%12
    animals = ["Pig (Boar)", "Rat", "Ox", "Tiger", "Cat (Rabbit)", "Dragon", "Snake", "Horse", "Goat (Sheep)", "Monkey", "Rooster", "Dog"]
    # Rabbit replaces cat if you are outside Vietnam. Sheep if you are from Japan.
    return stem_letter[stem], animals[branch]

def lectionary(y):
    """
    This program is written to determine lectionary cycle.
    Returns the lectionary cycle (Sunday and weekday) for the given year.
    """
    s = y%3
    sunday = ['C','A','B']
    w = y%2
    weekday = ['EVEN', 'ODD']
    return sunday[s], weekday[w]

def clear_screen():
    """
    Clears the console screen, depending on the operating system (Windows or Unix-like systems).
    """
    # Clears the screen depending on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')

def DST_switch(y):
    """
    Returns the DST start and end dates for the US and EU based on the year's doomsday.
    """
    day_of_week = doomsday(y)
    
    us_dst_start, us_dst_end, eu_dst_start, eu_dst_end, au_nz_dst_start, au_nz_dst_end = None, None, None, None, None, None
    
    # Vietnam doesn't observe DST.
    # DST start: 
    # + USA: At 2am ST (3am DT) on 2nd Sunday of March
    # + EU: At 8am Vietnam time (1am UTC) on last Sunday of March
    # + NZ: At 9pm Vietnam time on the day before first Sunday of October (= 2am NZST (3am NZDT) on the next day)
    # + AU (South Australia): At 11:30pm Vietnam time on the day before first Sunday of October (= 2am ACST (3am ACDT) on the next day) 
    # + AU (NSW, ACT, Victoria, Tasmania): At 11pm Vietnam time on the day before first Sunday of October (= 2am AEST (3am AEDT) on the next day) 
    #   (applicable for South Australia, NSW, ACT, Victoria n Tasmania)
    # DST end:
    # + USA: At 2am DT (1am ST) on 1st Sunday of November
    # + EU: At 8am Vietnam time (1am UTC) on last Sunday of October
    # + NZ: At 9pm Vietnam time on the day before first Sunday of April (= 3am NZDT (2am NZST) on the next day)
    # + AU (South Australia): At 10:30pm Vietnam time on the day before first Sunday of April (= 2am ACDT (1am ACST) on the next day) 
    # + AU (NSW, ACT, Victoria, Tasmania): At 10pm Vietnam time on the day before first Sunday of April (= 2am AEDT (1am AEST) on the next day) 

    if day_of_week == "Thursday":
        us_dst_start, us_dst_end = "10 March", "3 November"
        eu_dst_start, eu_dst_end = "31 March", "27 October"
        au_nz_dst_end, au_nz_dst_start = "7 April", "6 October" 
        # End first then start due to seasonal reversal in AU/NZ
    elif day_of_week == "Jumu'ah":  # Friday
        us_dst_start, us_dst_end = "9 March", "2 November"
        eu_dst_start, eu_dst_end = "30 March", "26 October"
        au_nz_dst_end, au_nz_dst_start = "6 April", "5 October"
    elif day_of_week == "Sabbath":  # Saturday
        us_dst_start, us_dst_end = "8 March", "1 November"
        eu_dst_start, eu_dst_end = "29 March", "25 October"
        au_nz_dst_end, au_nz_dst_start = "5 April", "4 October"
    elif day_of_week == "Sunday":
        us_dst_start, us_dst_end = "14 March", "7 November"
        eu_dst_start, eu_dst_end = "28 March", "31 October"
        au_nz_dst_end, au_nz_dst_start = "4 April", "3 October"
    elif day_of_week == "Monday":
        us_dst_start, us_dst_end = "13 March", "6 November"
        eu_dst_start, eu_dst_end = "27 March", "30 October"
        au_nz_dst_end, au_nz_dst_start = "3 April", "2 October"
    elif day_of_week == "Tuesday":
        us_dst_start, us_dst_end = "12 March", "5 November"
        eu_dst_start, eu_dst_end = "26 March", "29 October"
        au_nz_dst_end, au_nz_dst_start = "2 April", "1 October"
    elif day_of_week == "Wednesday":
        us_dst_start, us_dst_end = "11 March", "6 November"
        eu_dst_start, eu_dst_end = "25 March", "29 October"
        au_nz_dst_end, au_nz_dst_start = "1 April", "7 October"
    
    return {
        "US_DST_start": us_dst_start,
        "US_DST_end": us_dst_end,
        "EU_DST_start": eu_dst_start,
        "EU_DST_end": eu_dst_end,
        "AU_NZ_DST_end": au_nz_dst_end,
        "AU_NZ_DST_start": au_nz_dst_start
    }

if __name__=="__main__":
    # This is the main program.
    while True:
        try:
            clear_screen()
            y = int(input("Insert a year: "))
            easter_date = easter(y)
            zodiac = sexagenary(y)
            reading = lectionary(y)
            pascha_date = pascha(y)
            jw_memorial_date = memorial(y)
            
            dst_info = DST_switch(y)
            us_dst_start = dst_info['US_DST_start']
            us_dst_end = dst_info['US_DST_end']
            eu_dst_start = dst_info['EU_DST_start']
            eu_dst_end = dst_info['EU_DST_end']
            au_nz_dst_end = dst_info['AU_NZ_DST_end']
            au_nz_dst_start = dst_info['AU_NZ_DST_start']
            
            print(f"Doomsday for {y} is {doomsday(y)}.")
            print(f"{y} is a {'leap' if leap(y) else 'normal'} year.")
            print(f"Dominical letter: {dominical(y)}")
            print(f"Jehovah's Witnesses' Memorial of Jesus' Death is on {'March' if jw_memorial_date[1] == 3 else 'April'} {jw_memorial_date[0]}.")
            print(f"Easter is on {'March' if easter_date[1] == 3 else 'April'} {easter_date[0]}.")
            if y>1582:
                print(f"Pascha is on {'March' if pascha_date[1] == 3 else 'April'} {pascha_date[0]}.")
                print(f"Delta: {y//100 - y//400 - 2}")
                
            print(f"\nIndiction: {indiction(y)}; Solar Cycle: {solar(y)}; Epact Cycle: {epact(y)}")
            if solar(y)==2: # The latest Birkat Hachama was in 2009, the next Birkat Hachama will be 2037
                print(f"---This is the year of Birkat Hachama.---")
                
            print(f"Julian Period: {julianperiod(y)}; Year of the {zodiac[0]} {zodiac[1]}.")
            print(f"\nVietnamese Calendar: {y+2879}; Buddhist Calendar: {y+544}")
            print(f"Jewish Calendar: {y+3760} (until Rosh Hashanah) / {y+3761} (since Rosh Hashanah)")
            print(f"This year has {'2 Adars' if ((7*(y+3760)+1)%19<7) else '1 Adar'}.")
            print(f"Byzantine Calendar: {y+5508} (to {'Julian August 31' if y>1582 else 'August 31'}) / {y+5509} (from {'Julian September 1' if y>1582 else 'September 1'})")
            print(f"Hijri Calendar (around 1 January): {(y-622)*33//32}")
            print(f"\nLectionary Cycle: {reading[0]} {reading[1]}")

            print(f"\nIn the USA, the DST starts at 2am ST (3am DT) local time {us_dst_start}\n(corresponding 12:30pm (from Newfoundland), 1pm (from AT), 2pm (from ET), 3pm (from CT), \n4pm (from MT except Arizona and Yukon), 5pm (from PT), 6pm (from AKT), \n7pm (from Aleut) Vietnam time)\nand ends at 2am DT (1am ST) local time {us_dst_end}\n(corresponding 11:30am (from Newfoundland), 12pm (from AT), \n1pm (from ET), 2pm (from CT), 3pm (from MT except Arizona and Yukon), \n4pm (from PT), 5pm (from AKT), 6pm (from Aleut) Vietnam time)")

            print(f"\nIn Europe, the DST starts at 8am Vietnam time {eu_dst_start}\nand ends at 8am Vietnam time {eu_dst_end}")

            print(f"\nIn AU and NZ, the DST ends at 2am local Australian time and 3am New Zealand time {au_nz_dst_end}\n(corresponding 9pm (from NZ), 10pm (from Southeast Australia) \nand 10:30pm (from South Australia) Vietnam time the previous day) \nand starts at 2am local time {au_nz_dst_end}\n(corresponding 9pm (from NZ), 11pm (from Southeast Australia) \nand 11:30pm (from South Australia) Vietnam time the previous day)")
            
            print("\n------------")
            if input("Press 'y' to try again: ").lower() != 'y':
                input("This ends the program. Press RETURN key to exit.")
                break
        except ValueError: # If it's not an integer and error screen appears.
            input("Wrong! Press RETURN key to try again")
