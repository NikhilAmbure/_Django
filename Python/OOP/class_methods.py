
class Eat:
    print("No")

# __doc__ -> documentation
class ABC(Eat):
    """This is ABC class for nothing"""

    def random():
        pass

print(ABC.__doc__)


# __dict__
print(ABC.__dict__)

# __name__
print(ABC.__name__)

# __module__
# When we import function from other file
print(ABC.__module__)

# __bases__
# Gives the inherited class
print(ABC.__bases__)