
# Buffer Overflow and Grade Decryption Challange

These Python scripts are developed as part of a university coursework involving buffer overflow exploitation and encrypted file decryption, targeting the `gradeGPT.x86` executable.

BOF.py: Buffer Overflow Exploit
This script demonstrates the exploitation of a buffer overflow vulnerability in gradeGPT.x86, an ELF 32-bit LSB executable. The vulnerabilities were identified through reverse engineering with Ghidra. Key vulnerabilities include the use of the gets function leading to potential buffer overflows, and potential buffer overflow in indirect function calls without bounds checking. The exploit constructs a payload combining a buffer fill, the address of the bof_island function, and shellcode to open the /etc/passwd_dummy file, which is then written to the h4x_those_grades! file to trigger the overflow and execute the shellcode.

grade_hack.py: Grade File Decryption
This script is designed to decrypt and format the contents of an encrypted grade.txt file. It employs multiple techniques to process different encryption levels within the file:

- Level One decryption uses direct ASCII interpretation.
- Level Two involves reversing a transformation and filtering for printable characters.
- Level Three uses XOR decryption with a user ID.
The decrypted grades are displayed with color-coded hex representation and explanations. This script begins with an ASCII art header and includes ANSI color codes for output formatting.

## Introduction

The `grade_hack.py' script is complementary to` `BOF.py`, focusing on the decryption and analysis of output files affected by the buffer overflow exploit. Together, these scripts provide a comprehensive educational tool to understand both the exploitation of vulnerabilities and the techniques for reversing such exploits' effects.

## Vulnerability Identification

Key vulnerabilities identified in the executable include:

- Buffer Overflow: Utilizes a vulnerable gets function and lacks bounds checking for indirect function calls.
- Encryption Handling: Demonstrates handling and reversing custom encryption methods embedded within binary files.

## Exploit Script

The BOF.py script constructs a payload that combines a buffer fill, the address of the `bof_island` function, and shellcode to open the `/etc/passwd_dummy` file. The payload is then written to the `h4x_those_grades!` file to trigger the buffer overflow and execute the shellcode.

![bof](https://github.com/Gadzhovski/BufferOverflowExample/assets/93713208/96844144-fa86-4329-9f43-e0012d9448a0)

grade_hack.py:

![hack](https://github.com/Gadzhovski/Reverse-Engineer-and-Buffer-Overflow-Challange/blob/main/grade_hack.png)

## Disclaimer

This script is for educational purposes only and demonstrates the importance of secure coding practices. It should not be used for unauthorized testing or in any malicious manner.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
