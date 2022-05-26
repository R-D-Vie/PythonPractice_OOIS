from __future__ import print_function, division

from datetime import datetime


def main():

    print("For people born on these dates:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)
    print(bday1)
    print(bday2)

    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)


if __name__ == '__main__':
    main()
    