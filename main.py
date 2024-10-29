import ping3
import os
import re

def ip():
    global q
    q = input("Who to ping?: ")
    response = ping3.ping(q)
    if response is None or response is False:
        print("Invalid address")
    else:
        global command
        command = 'tracert ' + q
        tracert_output = os.popen(command).read()
        trace_list = re.split('\n+', tracert_output)
        my_line = trace_list[-4]
        ip = my_line.split()[-1]
        q = ip
        print("The closest router is: " + q)
        size()

def size():
    global s
    s = input("How many bytes?: ")
    if s.isdigit() and 0 <= int(s) <= 1500:
        num()
    else:
        print("Invalid number, must be a non-negative digit and below 1500")
        size()

def num():
    x = input("How many times?: ")
    if x.isdigit():
        code(int(x), int(s))
    else:
        print("Invalid number")
        num()

def code(count, size):
    a = 0.0
    for _ in range(count):
        response = ping3.ping(q, size=size)
        if response is not None:
            print(float(response))
            a += response
        else:
            print("Ping request timed out")

ip()
