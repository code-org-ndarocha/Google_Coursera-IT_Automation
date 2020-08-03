class Piglet:
    def speak(self):
        print("oink oink")
        
        
hamlet = Piglet()
hamlet.speak()


class PigletNext:
    name = "piglet"
    def speak(self):
        print("Oink I'm {}! Oink!".format(self.name))
        
hamlet = PigletNext()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = PigletNext()
petunia.name = "Petunia"
petunia.speak()

class PigletTwo:
    years = 0
    def pig_years(self):
        return self.years*18
    
piggy = PigletTwo()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())


