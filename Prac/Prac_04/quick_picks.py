import random

MINIMUM = 1
MAXIMUN = 45
PerLine = 6

def main():
    numbers = int(input("How many quick picks do you want?"))
    while numbers <= 0:
        print("Sorry! No result! ")
        numbers = int(input("How many quick picks do you want?"))

    for n in range(numbers):
        quick_picks = []
        for m in range(PerLine):
            number = random.randint(MINIMUM,MAXIMUN)
            while number in quick_picks:
                number = random.randint(MINIMUM,MAXIMUN)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))
main()