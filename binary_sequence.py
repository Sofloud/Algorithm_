class binary_sequence:
    def __init__(self, n):
        self.__site__ = n
        self.__elems = [0] * n
        
    def next(self):
        if 0 not in self.__elems:
            return False
        else:
            i = self.__site__ - 1
            while self.__elems[i] != 0:
                self.__elems[i] = 0
                i -= 1  
            self.__elems[i] = 1
            return True
    
    def __str__(self):
        return " ".join(map(str, self.__elems))
    
    
n = int(input())
seq = binary_sequence(n)
print(seq)
while seq.next():
    print(seq) 