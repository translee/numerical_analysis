import numpy as np
import sys

def input_matrix():
    """输入矩阵"""

    n = input("请输入方程组阶数(输入q退出): ")
    if n == 'q':
        sys.exit()
    try:
        n = int(n) 
        dict = {}
        for hang in range(n):
            hang_lst = list((input("请输入增广矩阵的第{}行(元素之间用空格分隔): ".
                format(hang+1)).split(' ')))
            new_hang_lst = []
            for string in hang_lst:
                new_hang_lst.append(int(string))
            dict.update({'hang{}'.format(hang):new_hang_lst})
        array = []
        for value in dict.values():
            array.append(value)
        axb = np.array(array, dtype=float).reshape(n, n+1)
        return axb, n
    except:
        return 404, 404


def xiaoyuan(a, n):
    """列主元并消去"""

    k = 0
    try:
        while k <= n - 1:
            for i in range(k, n):
                if max([a[q][k] for q in range(n)], key=abs) == 0:
                    print('有一列系数全为0')
                    return 0
                    break
                elif a[i][k] == max([a[q][k] for q in range(n)], key=abs):
                    a[[k,i], :] = a[[i,k], :]
                    for j in range(k+1, n):
                        tem = a[j][k]
                        for h in range(n+1):
                            a[j][h] = a[j][h] - tem / a[k][k] * a[k][h]
                else:
                    pass
            k += 1
        return a
    except:
        return np.zeros(n * (n + 1)).reshape(n, n + 1)


def huidai(a, n):
    """回代求出X"""

    #创建与解X大小相同的矩阵备用
    x = np.arange(n, dtype=float)

    for p in range(n-1,-1,-1):
        hsakl = np.array([sum(a[p][e] * x[e] for e in range(p+1,n))], dtype=float)
        x[p] = (a[p][n] - hsakl[0]) / a[p][p]
    return x


def print_result(xs):
    """输出最终结果"""
    count = 1
    for jie in xs:
        print("X{}={:.2f}".format(count, jie))
        count += 1


def main():
    axb, n = input_matrix()
    while n == 404:
        print("输入错误！\n")
        input_matrix()
    x_y_matrix = xiaoyuan(axb, n)
    if x_y_matrix == np.zero(n * (n + 1)).reshape(n, n + 1):
        print("消元失败，请检查输入！")
    xs = huidai(x_y_matrix, n)
    print_result(xs)

while True:
    main()
pause = input()
