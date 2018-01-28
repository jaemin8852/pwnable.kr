from pwn import *
import time
 
host = "pwnable.kr"
port = 9007
 
con = remote(host, port)
 
print con.recv()
time.sleep(3)        #starting in 3 sec...
 
 
for i in range(100):    #find 100 counterfeit coins
    con.recvuntil("N=")
    n = int(con.recvuntil(" "))
    con.recv()
 
    print n
    high = n
    low = 1
    coin = -1
    
    while 1:
 
        mid = (low + high) / 2
        num = ""
        #Omission of termination condition
        
        if coin > 0:
            con.sendline(coin)
            print "send : " + coin
        else:
            for j in range(low, mid+1):
                num += "{0} ".format(j)
            print "send : " + num
            con.sendline(num)
        
        recv = con.recvuntil("\n")
        print "recv : " + recv
 
        if recv.find("Correct") != -1:
            break
        elif int(recv) == 9:
            if coin > -1:
                continue
            else:
                coin = num
                continue
        elif int(recv) % 10 != 0:
            high = mid

