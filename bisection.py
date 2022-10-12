import math

count = 0

def targrtFunc(x):
    return 1 - x - math.sin(x)


def bisection(a, b, e):
    global count
    c = (a + b) / 2
    if targrtFunc(c) == 0:
        return c
    elif (b - a) / 2 < e:
        return c
    else:
        if targrtFunc(a) * targrtFunc(c) > 0:
            count += 1
            return bisection(c, b, e)
        else:
            count += 1
            return bisection(a, c, e)


def main():
    print(bisection(0, 1, 0.00000001))
    print(count)


if __name__ == '__main__':
    main()
