a = 10

def random():
    global a # Using outside scope var into def scope
    b = a + 10
    a = b

random()
print(a)