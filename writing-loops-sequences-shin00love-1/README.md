[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3943116&assignment_repo_type=AssignmentRepo)
# Technical HW: Writing Loops & Sequences
Please complete the following functions. You can test by running the 'pytest' command.

## Problem 1: squared_sum

Write a function ```squared_sum``` in pseudocode or python that takes an array of numbers as input and outputs the following:

| **Example call** | **Returns** |
| -------------- | --------- |
| `squared_sum ([])` | `0` |
| `squared_sum ([5, -2, 3])` | `38` |
| `squared_sum ([-3, 4])` | `25` |
| `squared_sum ([7, -1, 15, 0])` | `275` |


## Problem 2: mix

Write a function `mix` in pseudocode or python that takes two strings as parameters and returns one array with the first element from the first array, and the second element from the second array, and every other element thereafter.

| **Example call** | **Returns** |
| -------------- | --------- |
| `mix(hello, there)` | `htehlelroe` |
| `mix(1234, abcd)` | `1a2b3c4d` |
| `mix(12, abcd)` | `1a2bcd` |
| `mix(1234, ab)` | `1a2b34` |

## Getting started

### Develop online

Click the "Work in Repl.it" button. Edit the file. To run, see the commands below.

### Develop in PyCharm

With this option, you can develop on your laptop. You will need to install PyCharm (or another IDE) and git. PyCharm has some built-in git support.

## Testing
The tests are failing right now because the functions aren't outputting the correct information. Fixing this up will make the tests green.

### Setup
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

### Run commands
To run just your main code:
`python3 hello.py`

To run all the tests:
`pytest`

### Submitting
Commit & push your repo! The instructor will receive a pull request for grading.
