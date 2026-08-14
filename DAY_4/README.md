# Animation Mini Project

This is a simple Python animation program that displays a row of stars moving from left to right and then back again in the terminal.

## Description

The program uses indentation spaces to create the animation effect. The number of spaces increases until it reaches a limit and then decreases, making the stars move back and forth.

## Concepts Used

- Python `time` module
- Python `sys` module
- `while` loop
- `try-except`
- `KeyboardInterrupt`
- Conditional statements
- Variables
- String multiplication

## Program Code

    import time
    import sys

    indent = 0
    indent_increasing = True

    try:
        while True:
            print(' ' * indent, end='')
            print('********')

            time.sleep(0.1)

            if indent_increasing:
                indent = indent + 1

            if indent == 20:
                indent_increasing = False
            else:
                indent = indent - 1

            if indent == 0:
                indent_increasing = True

    except KeyboardInterrupt:
        sys.exit()

## Execution Flow

    Start
      ↓
    Set indent = 0
      ↓
    Set indent_increasing = True
      ↓
    Print ********
      ↓
    Wait for 0.1 seconds
      ↓
    Increase indentation
      ↓
    Reach indentation limit
      ↓
    Change direction
      ↓
    Decrease indentation
      ↓
    Reach indentation 0
      ↓
    Change direction again
      ↓
    Repeat animation
      ↓
    Press Ctrl + C
      ↓
    KeyboardInterrupt
      ↓
    Exit program

## Output

The program continuously displays:

    ********
     ********
      ********
       ********
        ********
         ********

The stars move across the terminal and then move back.

## How to Stop the Program

Press:

    Ctrl + C

The `KeyboardInterrupt` exception is handled using `try-except`, and `sys.exit()` is used to stop the program.

## Modules Used

### time

The `time.sleep(0.1)` function pauses the program for 0.1 seconds to create the animation effect.

### sys

The `sys.exit()` function is used to terminate the program when the user stops the animation.

## Author

**Sahil Ranade**

AIML Batch