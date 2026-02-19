
import mpmath
from datetime import datetime

"""
Enter an irrational constant number and a number of decimal places and
the program will generate that constant's number up to the given number of decimal places.
The built-in 'math' library allows precision up to a very limited number of decimal places,
whereas mpmath allows an arbitrary number of decimal places, making the program more scalable.
Programmed with mpmath library, setting a limit precision of 1000 to avoid performance issues.
At the end the user can choose to save the result given in a .txt file for later use.
"""

CONSTANTS = {"pi": ("Pi", mpmath.pi),
             "e": ("Euler's Number", mpmath.e),
             "phi": ("Phi (Golden Ratio)", mpmath.phi),
             "gamma": ("Euler-Mascheroni constant", mpmath.euler),
             "catalan": ("Catalan's constant", mpmath.catalan),
             "apery": ("Apéry's constant", mpmath.apery)}


def format_num(num, const):
    mpmath.mp.dps = num + 1
    return "\n{} number with {} decimal places:\n --- {} --- \n".format(const[0], num, const[1])


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


def choose_constant():
    const = "wrong"
    while const not in CONSTANTS:
        for key, value in CONSTANTS.items():
            print(" | " + value[0] + " - Type " + "'" + key + "'")
        const = input("\nWhat irrational constant will you choose? ").lower()
        if const not in CONSTANTS:
            print("\nNot a valid constant!\n")

    return const, CONSTANTS[const]


def save_as_txt(filename, content):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d at %H%p")
    content = f"\n{content} --- Recorded at: {time}"
    with open(filename, "a+") as file:
        file.write(content)
    print("Saved the file as " + filename + " in this directory")


print("\nHello! Choose an irrational constant and then choose how many decimal places would you like that number to go up to!\n")
key, const = choose_constant()
places = validate_num()
result = format_num(places, const)
print(format_num(places, const))

save = "wrong"
while save not in ['y', 'yes', 'n', 'no']:
    save = input("Would you like to save this result in .txt file? Type 'Y' or 'N': ").lower()
if save in ['y', 'yes']:
    filename = f"{key}_decimal_manipulation.txt"
    content = result
    save_as_txt(filename, content)
