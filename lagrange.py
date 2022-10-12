import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


my_font = fm.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=15)


def input_it():
    init_list = input().split()
    num_list = []
    for num in init_list:
        num_list.append(float(num))
    return num_list


def code_input():
    x_list = [1, 2, 3, 4, 5, 6, 10]
    y_list = [0.84147, 0.90930, 0.14112, -0.7568, -0.9589242, -0.279415, -0.544021]
    require_number = 4.5
    return x_list, y_list, require_number


def calcul_lnn(x_list, y_list, given_x):
    k = 0
    lnn = []
    while k < len(x_list):
        temp_1, temp_2 = 1.0, 1.0
        for i in range(len(x_list)):
            if i != k:
                temp_1 = temp_1 * (given_x - x_list[i])
                temp_2 = temp_2 * (x_list[k] - x_list[i])
            else:
                pass
        ln = temp_1 / temp_2
        lnn.append(ln)
        k += 1
    fx = 0.0
    for y, ln in zip(y_list, lnn):
        fx = fx + y * ln
    return fx


def get_some_fxs(x_list, y_list):
    fxs = []
    xs = []
    b = np.linspace(x_list[0], x_list[-1], 100)
    for x in b.flat:
        xs.append(x)
        fx = calcul_lnn(x_list, y_list, x)
        fxs.append(fx)
    return xs, fxs


def plot_it(x_list, y_list, xs, fxs, x, y):
    plt.style.use("seaborn-dark")
    a = np.linspace(x_list[0], x_list[-1], 100)
    #plt.plot(a, np.sin(a), label='精确曲线')
    plt.plot(xs, fxs, color='turquoise', label='拟合曲线', linestyle='--', linewidth=2)
    plt.plot(x_list, y_list, 'b+', label='原始精确点')
    #plt.scatter(x_list, y_list, label='原始精确点', color='k', linewidth=1)
    plt.scatter(x, y, label='计算点({:.2f},{:.2f})'.format(x, y), color='r', linewidth=2) 
    plt.title("拉格朗日插值拟合数据", fontproperties='simsun', fontsize=20)
    leg = plt.legend(fancybox=True, shadow=True, prop=my_font)
    leg.get_frame().set_alpha(0.6)
    plt.grid()
    plt.xlim(x_list[0]-len(x_list)/5, x_list[-1]+len(x_list)/5)
    plt.ylim(max(y_list, key=abs)-len(y_list)/10, max(y_list)+len(y_list)/10)
    plt.show()


def main():
    x_list, y_list, require_number = code_input()
    xs, fxs = get_some_fxs(x_list, y_list)
    y = calcul_lnn(x_list, y_list, require_number)
    plot_it(x_list, y_list, xs, fxs, require_number, y)


if __name__ == '__main__':
    main()
