# offset-finder
Offset finder is a tool that automatically finds the buffer length required to overwrite the Instruction Pointer or Program Counter. It helps to perform Buffer Overflow Attack.

Following two python scripts are used.
1) Using "create_string.py" create a random string of length greater than required by the binary
2) Using GDB find the value in EIP after the binary is crashed.
3) Using "offset_finder.py" find the offset required to overwrite the EIP register.

Following screenshots makes it easy to understand the steps

![1](https://raw.githubusercontent.com/neelpatel05/offset-finder/master/screenshots/1.png)
![2](https://raw.githubusercontent.com/neelpatel05/offset-finder/master/screenshots/2.png)
![3](https://raw.githubusercontent.com/neelpatel05/offset-finder/master/screenshots/3.png)
