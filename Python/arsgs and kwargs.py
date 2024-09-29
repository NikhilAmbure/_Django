# args
# Only when we pass values
def sum(*nums):
    print(nums)
    return 0
print(sum(1, 2))


# Kwargs
# Passes dictionary
def conc(**kwargs):
    print(kwargs)
    return kwargs["first_name"]

print(conc(surname="Ambure", first_name="Nikhil", middle_name="P"))
