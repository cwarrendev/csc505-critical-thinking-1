# WarrenFit Plate Loader

Repository: https://github.com/cwarrendev/csc505-critical-thinking-1

A command-line plate loading calculator for CSC505 - Module 1 Critical Thinking, built for loading my Smith machine barbell. When you know the total weight you want to lift, it works out which standard weight plates (45, 35, 25, 10, 5, and 2.5 lb) to load on each side of the bar to get there, with no mental math between sets. Because a Smith machine bar usually weighs less than a standard 45 lb Olympic bar, the bar weight is an input: enter your machine's effective bar weight, or press Enter to use the 45 lb default. If the target cannot be loaded exactly, it returns the closest loadable weight below the target instead of rejecting the input.

## Requirements

- Python 3 (standard library only, no packages to install)

## Running the script

```
python plate_calculator.py
```

The script prompts for a target weight and an optional bar weight (press Enter to use the default 45 lb bar):

```
WarrenFit Plate Loader
Target weight (lb): 185
Bar weight (lb, blank for 45):
Per side:
  1 x 45 lb
  1 x 25 lb
Bar loads to 185 lb.
```

If the target is not exactly loadable, the output notes that the result is the closest weight below it. Inputs must satisfy 0 < bar ≤ target ≤ 1500, and non-numeric input is reported as an input error.

## Project files

- [plate_calculator.py](plate_calculator.py) - the calculator: `plan_plates()` holds the planning logic, `main()` handles the CLI.
- [developer_report.md](developer_report.md) - developer report covering the purpose, tools, challenges, planned improvements, and lessons learned.
- [execution_output.txt](execution_output.txt) - captured output from a sample run.
- [screenshots/](screenshots/) - screenshots of the script running.

## Author

Chris Warren
