Months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        if type(day) == str:
            day = day.split('.')
            self.day = int(day[0])
            self.month = int(day[1])
            self.year = int(day[2])
        else:
            self.day = day
            self.month = month
            self.year = year
        
    def __str__(self):
            return str(self.day).rjust(2, '0') + '.' + str(self.month).rjust(2, '0') + '.' + str(self.year).rjust(4, '0')
    
    def LeapYear(self):
        return self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)
        
    def __int__(self):
        days = (self.year - 1) * 365 + (self.year - 1) // 4 - (self.year - 1) // 100 + (self.year - 1) // 400
        for i in range(self.month):
            if i == 2:
                days += self.LeapYear()
            days += Months[i]
        days += self.day  
        return days
    
    def __sub__(self, other):
        return int(self) - int(other)
            
            
n = Date(input())
m = Date(input())
print(m - n)