import time
import sys
import os
import hashlib
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow(text, d=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

clear()

slow("Booting universe simulation...", 0.05)
time.sleep(0.6)
slow("Loading stars ✨")
time.sleep(0.6)

slow("\nEnter your name to initialize reality:", 0.05)
name = input("> ").strip()

# Hash her name to make it "unique forever"
seed = int(hashlib.sha256(name.encode()).hexdigest(), 16)
random.seed(seed)

clear()
slow(f"Welcome, {name}.", 0.06)
time.sleep(0.8)

slow("\nRecalculating universe with you in it...\n", 0.05)
time.sleep(1)

# Generate starfield
width, height = 60, 20
stars = [[" " for _ in range(width)] for _ in range(height)]

points = []
for _ in range(len(name) * 3 + 10):
    x = random.randint(5, width - 6)
    y = random.randint(3, height - 4)
    points.append((x, y))
    stars[y][x] = "✦"

# Draw constellation lines
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    if abs(x2 - x1) <= 2 and abs(y2 - y1) <= 1:
        stars[y1][x1 + 1] = "─"

clear()
for row in stars:
    print("".join(row))
    time.sleep(0.05)

time.sleep(1.2)

slow("\nThis constellation didn’t exist before.", 0.06)
time.sleep(0.6)
slow("It was formed only after you entered your name.", 0.06)
time.sleep(0.8)

slow("\nAstronomers would name it something rare.", 0.05)
time.sleep(0.6)
slow(f"They’d call it:  ✨ {name.upper()} ✨", 0.07)

time.sleep(1.2)

slow("\nFun fact:", 0.06)
time.sleep(0.5)
slow("Every time I think of you,", 0.06)
slow("this universe expands a little more.", 0.06)

time.sleep(1)

slow("\nSome people change days.", 0.06)
slow("Some change lives.", 0.06)
slow("You changed my entire sky 🌌", 0.07)

time.sleep(1.2)

print("\n" + "★ " * 20)
slow("This program will never generate the same universe again.", 0.05)
slow("Just like you.", 0.06)
print("★ " * 20)
