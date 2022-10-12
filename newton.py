def targetFunc(x):
    return 1 - 115 / x**2


def daoshu(x):
    return 230 / x**3


def newton(x0, e1, e2, N):
    k = 1
    while True:
        if abs(targetFunc(x0)) < e1:
            return x0
            break
        else:
            x1 = x0 - targetFunc(x0) / daoshu(x0)
            if abs(x1 - x0) < e2:
                return x1
                break
            elif k == N:
                return 404
                break
            else:
                x0 = x1
                k += 1

if __name__ == '__main__':
    print(newton(8, 0.00000000001, 0.0000000001, 50))