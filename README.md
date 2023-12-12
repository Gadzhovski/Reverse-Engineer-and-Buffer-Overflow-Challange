
# Buffer Overflow Exploit Example

This Python script is developed as part of a coursework for buffer overflow. It demonstrates the exploitation of a buffer overflow vulnerability in the `gradeGPT.x86` executable.

## Introduction

The script exploits identified vulnerabilities in `gradeGPT.x86`, an ELF 32-bit LSB executable. These vulnerabilities were discovered through reverse engineering using Ghidra. The primary focus is to exploit buffer overflow weaknesses to demonstrate the associated risks and underscore the importance of secure coding practices.

## Vulnerability Identification

Key vulnerabilities identified in the executable include:

- **Use of `gets` Function**: In the `load_username` function, which leads to potential buffer overflows due to lack of input size checking.
- **Potential Buffer Overflow in Indirect Calls**: In the `bof_island` function, which lacks bounds checking for indirect function calls.

## Exploit Script

The script constructs a payload that combines a buffer fill, the address of the `bof_island` function, and shellcode to open the `/etc/passwd_dummy` file. The payload is then written to the `h4x_those_grades!` file to trigger the buffer overflow and execute the shellcode.

![bof](https://github.com/Gadzhovski/BufferOverflowExample/assets/93713208/96844144-fa86-4329-9f43-e0012d9448a0)

## Disclaimer

This script is for educational purposes only and demonstrates the importance of secure coding practices. It should not be used for unauthorized testing or in any malicious manner.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Credits

Project developed by Radoslav Gadzhovski as part of coursework for the University of Greenwich.
