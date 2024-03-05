from random import randint
from sal_timer import timer

def main():
    level = get_level()
    print(f"Score: {mode(level)}")


def get_level():
    while True:
        try:
            level = int(input("Select level: [Easiest: 1 - Hardest: 4]\n"))
            if level in range(1, 4):
                break
            else:
                continue
        except ValueError:
            continue

    return level


def mode(level):
    while True:
        mode = input("Select mode: ['+', '-', '*', '/']\n")
        if mode not in ["+", "-", "*", "/"]:
            continue
        else:
            break
    if mode == "+":
        return add(level)


    elif mode == "-":
        return sub(level)

@timer
def add(l):
    score = 0

    for _ in range(10):
        x = randint(10 ** (l - 1), 10**l - 1)
        y = randint(10 ** (l - 1), 10**l - 1)
        ans = int(input(f"{x} + {y} = "))
        if ans == x + y:
            score += 1
            continue
        else:
            for tries in range(2):
                print("Try again")
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    break
                elif ans != x + y and tries == 0:
                    continue
                else:
                    print(f"{x} + {y} =", x + y)
    return score

@timer
def sub(l):
    score = 0
    for _ in range(10):
        x = randint(10 ** (l - 1), 10**l - 1)
        y = randint(10 ** (l - 1), 10**l - 1)

        if x > y:
            ans = int(input(f"{x} - {y} = "))
            if ans == x - y:
                score += 1
                continue
            else:
                for tries in range(2):
                    print("Try again")
                    ans = int(input(f"{x} - {y} = "))
                    if ans == x - y:
                        break
                    elif ans != x - y and tries == 0:
                        continue
                    else:
                        print(f"{x} + {y}=", x - y)

        else:
            ans = int(input(f"{y} - {x} = "))
            if ans == y - x:
                score += 1
                continue
            else:
                for tries in range(2):
                    print("Try again")
                    ans = int(input(f"{y} - {x} = "))
                    if ans == y - x:
                        break
                    elif ans != y - x and tries == 0:
                        continue
                    else:
                        print(f"{y} - {x} =", y - x)

    return score

if __name__ == "__main__":
    main()
