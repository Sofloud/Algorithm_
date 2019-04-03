class Fraction:
    def __init__(self, a = 0, b = 1):
        if type(a) == Fraction:
            self.a = a.a
            self.b = a.b
        elif type(a) == str and b == 1:
            if ' ' in a:
                a = a.split()
                self.a = int(a[0])
                self.b = int(a[1])  
                self.reduce()
            elif '/' in a:
                a = a.split('/')
                self.a = int(a[0])
                self.b = int(a[1])  
                self.reduce()
        elif type(a) == int:
            self.a = a
            self.b = b
        self.reduce()
            
    def __str__(self):
        if self.b != 1:
            return str(self.a) + "/" + str(self.b)
        else:
            return str(self.a)
    
    def reduce(self):
        if self.b < 0:
            self.a *= -1
            self.b *= -1
        x, y = self.a, self.b
        while y != 0:
            x, y = y, x % y
        self.a = self.a // x
        self.b = self.b // x
    
    def __truediv__(self, other):
        if type(other) == Fraction:
            return Fraction(self.a * other.b, self.b * other.a)
        if type(other) == int:
            return Fraction(self.a, self.b * other)
        if type(other) == float:
            return self.a / (self.b * other)
    
    def __rtruediv__(self, other):
        if type(other) == float:
            return other * self.b / self.a
        else:
            return Fraction(other) / self
    
    def __itruediv__(self, other):
        self = self / other
        return self
    
 
file = open('input.txt', 'r')
exec(file.read())
file.close()