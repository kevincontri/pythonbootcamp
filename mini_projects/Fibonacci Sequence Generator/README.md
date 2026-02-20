## Fibonacci Sequence Generator

### Overview
This Python script generates Fibonacci numbers using arbitrary input.  
The user can choose to display either the **Nth Fibonacci number** or the **sequence up to N terms**.  
Results can optionally be saved to a `.txt` file with a timestamp.

### Features
- Generate the Nth Fibonacci number
- Generate the sequence up to N terms
- Quiet mode (raw output) and verbose mode (extra details)
- Save results to a file with a custom filename, optionally.

### How to use
Run the script with arguments:
```bash
python fibonacci.py -n <number> -c <choice> [options]
```
`-n` : Number of terms or position in the sequence (must be > 0)

`-c` / `--choice` : 1 = Nth Fibonacci number, 2 = Sequence up to N

`-s` / `--save` : Save the result to a .txt file

`-f` / `--file` : Specify output filename (default: fibonacci_seq.txt)

`-q` / `--quiet` : Print raw output only

`-v` / `--verbose` : Print extra details
