def gcd(m,n):
        if m<n:
            m, n = n, m
        while m % n != 0 :
            
            m, n = n, m % n

        return n

class Fraction:
    def __init__(self, top, bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError("Top and Bottom must be integers")
        div = gcd(top,bottom)
        self.num = top/div
        self.den = bottom/div


    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __repr__(self):
        return repr(self.num) + '/' + repr(self.den)
    

    def __add__(self,other):
        if isinstance(other,int):
            other = Fraction(other,1)
        
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return Fraction(new_num,new_den)

    def __radd__(self,other):
        other = Fraction(other,1)
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        

        return Fraction(new_num,new_den)

    def __iadd__(self,other):

        return self+other


    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den

        return Fraction(new_num, new_den)

    def __div__(self,other):
        new_num, new_den = other.den*self.num, other.num*self.den

        return Fraction(new_num, new_den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __eq__(self,other):
        first_num = self.num*other.den
        sec_num = self.den*other.num

        return first_num==sec_num

    def __ne__(self,other):
        first_num = self.num*other.den
        sec_num = self.den*other.num

        return first_num!=sec_num

    def __lt__(self,other):
        first_num = self.num*other.den
        sec_num = self.den*other.num

        return first_num<sec_num

    def __le__(self,other):
        first_num = self.num*other.den
        sec_num = self.den*other.num

        return first_num<=sec_num
    

y = Fraction(2,5)
z = Fraction(4,5)


