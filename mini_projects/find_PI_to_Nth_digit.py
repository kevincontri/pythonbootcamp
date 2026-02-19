
import mpmath

"""
Enter a number and the program will generate PI up to that many decimal places.
Programmed with mpmath library, setting a limit precision of 1000 to avoid performance issues.
The built-in math library allows pi precision up to 15 decimal places, whereas mpmath allows an
arbitrary number of decimal places, making the program more scalable.
"""

def format_pi(num):
    mpmath.mp.dps = num + 1 # Account for '3'.
    return f"\nPI number with {num} decimal places:\n --- {str(mpmath.pi)} --- \n"

def validate_num():
    while True:
        try:
            places = int(input("How many decimal places (0-1000)? "))
            if 0 <= places <= 1000:
                return places
            else:
                print("Please enter a number between 0 and 1000.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

places = validate_num()
print(format_pi(places))
import mpmath

