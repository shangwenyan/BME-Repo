from calendar import c
from typing import Type


def add(a, b):
    try:
        return a + c
    except TypeError:
        print("variable not found, using default")
        return a + b
def main():
    print(add(1, 3))

if __name__ == "__main__":
    main()