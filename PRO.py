import random

answer = "y"

while answer == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[--1--]")
        print("[-----]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[-----]")
        print("[--1--]")
        print("[----2]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[3----]")
        print("[--1--]")
        print("[----2]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[3---4]")
        print("[--1--]")
        print("[----2]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[3---4]")
        print("[--1--]")
        print("[5---2]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[1---2]")
        print("[3---4]")
        print("[5---6]")
        print("[-----]")
    answer = input("press y to roll again and n to exit: ") 
    print("\n") 