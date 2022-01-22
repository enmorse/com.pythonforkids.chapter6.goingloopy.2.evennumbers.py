# Create a loop that prints even numbers until it
# reaches your age or, if your age is an odd number,
# prints out odd numbers until it reaches your age.

def my_age(age):
    for i in range(0, age):
        if i % 3 == 0:
            print(i)


my_age(39)
