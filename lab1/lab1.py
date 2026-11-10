import time

import subprocess

CSI = "\x1b["
ZERO = f"{CSI}0G"
ERASE = f"{CSI}2K"
RESET = f"{CSI}0m"

print("Task 1")

time.sleep(3)

def background_flag(width_back):
        for i in range(width_back):
            print(f"{CSI}48;5;{29}m{'    ' * width_back}{RESET}", flush=True)
            time.sleep(0.1)

def circle(diameter, width_back):
    print(f"{CSI}H")
    center = width_back // 2
    offset = center - diameter // 2
    diam_changing = diameter - 2 * cnt
    red_color = f"{CSI}48;5;{124}m"
    green_color = f"{CSI}48;5;{29}m"
    cnt = 10
    print(f"{CSI}1B")
    for i in range(10):
        if i < 4:
            cnt -= 2        
            print(f"{CSI}1B{green_color}\
                    {' ' * (offset + cnt)}\
                    {red_color}\
                    {' ' * (diam_changing)}\
                    {ZERO}", end='',flush=True)
            time.sleep(0.1)
        elif i < 5:
            cnt -= 1        
            print(f"{CSI}1B{green_color}\
                    {' ' * (offset + cnt)}\
                    {red_color}\
                    {' ' * (diam_changing)}\
                    {ZERO}", end='', flush=True)
            time.sleep(0.1)
        elif i == 5:
            print(f"{CSI}1B{green_color}\
                    {' ' * (offset + cnt)}\
                    {red_color}\
                    {' ' * (diam_changing)}\
                    {ZERO}", end='', flush=True)
            time.sleep(0.1)
        elif i < 7:
            cnt += 1        
            print(f"{CSI}1B{green_color}\
                    {' ' * (offset + cnt)}\
                    {red_color}\
                    {' ' * (diam_changing)}\
                    {ZERO}", end='', flush=True)
            time.sleep(0.1)
        else:
            cnt += 2        
            print(f"{CSI}1B{green_color}\
                    {' ' * (offset + cnt)}\
                    {red_color}\
                    {' ' * (diam_changing)}\
                    {ZERO}", end='', flush=True)
            time.sleep(0.1)


background_flag(16)
circle(28, 64)
print(f"{RESET}{ZERO}{CSI}7B")
time.sleep(3)

print("Task 2")

print(f"{RESET}{ZERO}{CSI}7B")

time.sleep(3)

def pattern():
    backgrnd = f"{CSI}48;5;{45}m " 
    print(f"{ZERO}")
    print(f"{CSI}7B")
    time.sleep(0.1)
    for i in range(5):
        print(f"{ZERO}{backgrnd}{CSI}1A", end='',flush=True)
        time.sleep(0.1)
    print(f"{ZERO}")
    for i in range(12):    
        print(f"{backgrnd}", end='',flush=True)
        time.sleep(0.1)
    print(f"{CSI}1D", end='',flush=True)
    for i in range(2):
        print(f"{CSI}1B{backgrnd}{CSI}1D", end='',flush=True)
        time.sleep(0.1)
    for i in range(6):
        print(f"{CSI}1D{backgrnd}{CSI}1D", end='', flush=True)
        time.sleep(0.1)
    for i in range(3):
            print(f"{CSI}1B{backgrnd}{CSI}1D", end='',flush=True)
            time.sleep(0.1)
    for i in range(12):    
            print(f"{backgrnd}", end='',flush=True)
            time.sleep(0.1)

pattern()

print(f"{RESET}{ZERO}{CSI}7B")
time.sleep(3)

print("Task 3")

print(f"{RESET}{ZERO}{CSI}7B")

time.sleep(3)

subprocess.run(["cls"], shell=True)

print(f"{RESET}{ZERO}{CSI}7B")

def progress_bar(width, num_tasks):
    for task in range(num_tasks):
        for filled in range(width):
            bar = f"{'#' * filled}{'-' * (width - filled - 1)}"
            print(f"{ZERO}{ERASE}{task + 1}:{bar}", end = "", flush = True)
            time.sleep(1)
 
progress_bar(4, 3)

time.sleep(3)

print(f"{RESET}{ZERO}{CSI}7B")

print("Task 4")

time.sleep(3)

print(f"{RESET}{ZERO}{CSI}7B")

a = [float(n) for n in open('sequence.txt')]

sum1 = sum(abs(n) for n in a[:125])
sum2 = sum(abs(n) for n in a[125:250])

total = sum1 + sum2

p1 = sum1 / total * 100
p2 = sum2 / total * 100

def diagram1(length):
    for filled in range(length):
        bar = f"{f"{CSI}48;5;{208}m#" * filled}{'-' * (length - filled - 1)}"
        print(f"{ZERO}{bar}{RESET}", end='', flush = True)
        time.sleep(0.1)

def diagram2(length):
    for filled in range(length):
        bar = f"{f"{CSI}48;5;{177}m#" * filled}{'-' * (length - filled - 1)}"
        print(f"{ZERO}{bar}{RESET}", end='', flush = True)
        time.sleep(0.1)

if __name__ == '__main__':
    diagram1(int(p1))
    print(f"{p1}%")
    diagram2(int(p2))
    print(f"{p2}%")


