from datetime import datetime
import argparse

"""
Fibonacci Sequence Generator
Generates either the first N numbers of the Fibonacci sequence
or the sequence up to a maximum value.
"""

def fib(n, choice):
    """Depending on the user's choice, provides the Nth Fibonacci number or the sequence up to N"""
    fibonacci = [0, 1]
    for i in range(n - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])

    if choice == 1:
        return fibonacci[n - 1]
    else:
        return fibonacci[:n]

def save_as_txt(filename, content):
    """Option to save the result in a .txt file, with a timestamp"""
    now = datetime.now()
    time = now.strftime("%Y-%m-%d at %H:%M %p")
    content = f"\n{content} --- Recorded at: {time}"
    with open(filename, "a+") as file:
        file.write(content)
    print("Saved the file as " + filename + " in this directory\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fibonacci Sequence Generator")
    parser.add_argument('-n', type=int, metavar='', required=True, help="Number of terms or position in the sequence (must be > 0)")
    parser.add_argument('-c', '--choice', metavar='', type=int, choices=[1, 2], required=True, help="1 = Nth Fibonacci number, 2 = Sequence up to N")
    parser.add_argument('-s', '--save', action="store_true", help="Save the result to a .txt file")
    parser.add_argument('-f', '--file', default="fibonacci_seq.txt", help="Output filename")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action="store_true", help="Print quiet")
    group.add_argument('-v', '--verbose', action="store_true", help="Print verbose")
    args = parser.parse_args()

    fib_seq = fib(args.n, args.choice)
    if args.choice == 1:
        if args.quiet:
            output = fib_seq
        elif args.verbose:
            output = f"The {args.n}th number in the Fibonacci sequence is {fib_seq}\nThe whole generated sequence is: {fib(args.n, 2)}"
        else:
            output = f"The number {args.n} of the Fibonacci sequence is: {fib_seq}"
    else:
        if args.quiet:
            output = fib_seq
        elif args.verbose:
            output = f"Generated sequence up to {args.n}: {fib(args.n, 2)}"
        else:
            output = f"First {args.n} numbers of the Fibonacci sequence: {fib_seq}"

    print(output)

    if args.save:
        save_as_txt(args.file, output)
