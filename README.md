# offset-finder
Offset finder is a tool that automatically finds the buffer length required to overwrite the Instruction Pointer or Program Counter. It helps to perform Buffer Overflow Attack.

# Installation
### Requirements
* Python 2.x or 3.x
* Pyinstaller
* Git

Follow following commands on the terminal to install the offset-finder.

```
git clone https://github.com/neelpatel05/offset-finder.git
cd offset-finder/
pyinstaller --onefile pattern.py
sudo cp dist/pattern /usr/bin/
```

Note: This tool is only available for Linux operating system.

# Usage

The tools usage and available options 
```
usage: pattern [-h] [-l LENGTH] [-q QUERY]

Finds the offset required to overflow buffer

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        The length of pattern required
  -q QUERY, --query QUERY
                        The value of eip when input is the generated pattern

Enjoy overflowing buffer, but beware of canaries ;)
```

Following screenshots makes the usage of the tools very understandable.


![1](https://raw.githubusercontent.com/neelpatel05/offset-finder/master/screenshots/1.png)
![2](https://raw.githubusercontent.com/neelpatel05/offset-finder/master/screenshots/2.png)
