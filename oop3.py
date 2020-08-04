class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and flavor is {}".format(self.color, self.flavor)
        
        
jonagold = Apple("red", "sweet")
print(jonagold.color)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Nikhil") 
# Call the greeting method
print(some_person.greeting())


print(jonagold)

help(Apple)

print("Docstring!")

def to_seconds(hours, minutes, seconds):
    """Return the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds


help(to_seconds)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person."""
        print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)
