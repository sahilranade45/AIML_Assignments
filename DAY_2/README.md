# Python Vault Mini Project

This is a simple Python mini project based on Python operators. The program uses different levels to demonstrate arithmetic operations such as addition, multiplication, subtraction, division, floor division, modulus, and exponentiation.

## Description

The player starts with a fixed amount of energy and progresses through seven levels. At each level, the user provides input and the program performs an operation on the energy.

At the end, the vault is unlocked and the final results are displayed.

## Concepts Used

- Variables
- `input()`
- Type conversion using `int()`
- Arithmetic operators
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Modulus (`%`)
- Exponentiation (`**`)
- `f-string`
- User input and output

## Program Code

    # Level 1 - Energy Core

    energy = 10

    print("\nLEVEL 1 — ENERGY CORE")
    print(f"You start with {energy} energy.")

    found = int(input("You found an energy crystal worth: "))

    energy = energy + found

    print("Energy collected!")
    print(f"Your energy is now: {energy}")


    # Level 2 - Power Boost

    print("\nLEVEL 2 — POWER BOOST")

    boost = int(input("Choose your power multiplier (1–5): "))

    powered_energy = energy * boost

    print("POWER ACTIVATED!")
    print(f"Your energy became: {powered_energy}")


    # Level 3 - Laser Wall

    print("\nLEVEL 3 — LASER WALL")

    laser_cost = int(input("How much energy does the laser wall cost? "))

    remaining = powered_energy - laser_cost

    print("Laser wall disabled!")
    print(f"Energy remaining: {remaining}")


    # Level 4 - Team Up

    print("\nLEVEL 4 — TEAM UP")

    team_size = int(input("How many hackers are in your team? "))

    share = remaining / team_size

    print(f"Each hacker gets {share:.2f} energy.")


    # Level 5 - Build the Squad

    print("\nLEVEL 5 — BUILD THE SQUAD")

    energy_per_hacker = int(input("Energy required per hacker: "))

    full_hackers = remaining // energy_per_hacker

    print(f"You can fully power {full_hackers} hackers.")


    # Level 6 - Leftover Energy

    print("\nLEVEL 6 — LEFTOVER ENERGY")

    leftover = remaining % energy_per_hacker

    print(f"Energy left unused: {leftover}")


    # Level 7 - Final Vault

    print("\nLEVEL 7 — THE FINAL VAULT")

    power_level = int(input("Enter your final power level: "))

    final_power = power_level ** 2

    print(f"Your final power is: {final_power}")


    # Escape

    print("\n" + "=" * 45)
    print("VAULT UNLOCKED!")
    print("=" * 45)

    print(f"""
    🏆 MISSION COMPLETE!

    🔋 Final energy      : {remaining}
    👥 Full hackers      : {full_hackers}
    ♻️ Leftover energy   : {leftover}
    ⚡ Final power       : {final_power}

    You didn't just learn operators.
    You used them to build something. 🐍

    WELCOME TO PYTHON.
    """)

## Execution Flow

    Start
      ↓
    Level 1: Add energy crystal
      ↓
    Level 2: Multiply energy
      ↓
    Level 3: Subtract laser cost
      ↓
    Level 4: Divide energy among team
      ↓
    Level 5: Calculate fully powered hackers
      ↓
    Level 6: Calculate leftover energy
      ↓
    Level 7: Calculate final power using exponentiation
      ↓
    Display final results
      ↓
    Vault Unlocked

## Sample Output

    LEVEL 1 — ENERGY CORE
    You start with 10 energy.
    You found an energy crystal worth: 30
    Energy collected!
    Your energy is now: 40

    LEVEL 2 — POWER BOOST
    Choose your power multiplier (1–5): 3
    POWER ACTIVATED!
    Your energy became: 120

    LEVEL 3 — LASER WALL
    How much energy does the laser wall cost? 20
    Laser wall disabled!
    Energy remaining: 100

    LEVEL 4 — TEAM UP
    How many hackers are in your team? 2
    Each hacker gets 50.00 energy.

    LEVEL 5 — BUILD THE SQUAD
    Energy required per hacker: 30
    You can fully power 3 hackers.

    LEVEL 6 — LEFTOVER ENERGY
    Energy left unused: 10

    LEVEL 7 — THE FINAL VAULT
    Enter your final power level: 10
    Your final power is: 100

    =============================================
    VAULT UNLOCKED!
    =============================================

    🏆 MISSION COMPLETE!

    🔋 Final energy      : 100
    👥 Full hackers      : 3
    ♻️ Leftover energy   : 10
    ⚡ Final power       : 100

    You didn't just learn operators.
    You used them to build something. 🐍

    WELCOME TO PYTHON.

## Operator Demonstration

| Level | Operator | Purpose |
|---|---|---|
| Level 1 | `+` | Add energy |
| Level 2 | `*` | Multiply energy |
| Level 3 | `-` | Subtract laser cost |
| Level 4 | `/` | Divide energy among team |
| Level 5 | `//` | Calculate full hackers |
| Level 6 | `%` | Calculate leftover energy |
| Level 7 | `**` | Calculate final power |

## Technologies Used

- Python

## Author

**Sahil Ranade**

AIML Batch