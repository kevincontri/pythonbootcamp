import math

"""
Enter a number and the program will generate PI up to that many decimal places.
Programmed with a limit to how far the program will go, due to limits on floating point precision.
"""

def format_pi(num):
    return f"\nPI number with {num} decimal places: \n --- {math.pi:.{num}f} --- \n"

def validate_num():
    while True:
        try:
            places = int(input("How many decimal places (0-15)? "))
            if 0 <= places <= 15:
                return places
            else:
                print("Please enter a number between 0 and 15.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

places = validate_num()
print(format_pi(places))
