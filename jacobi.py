import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import MultipleLocator


def input_matrix(augmented_matrix):  
    b = augmented_matrix[:,-1]
    A = augmented_matrix[:,:-1]
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D_1 = np.linalg.inv(D)
    B_j = -D_1 @ (L + U)
    b_j = D_1 @ b 
    return B_j, b_j


def caculate(B_j, b_j, x0, N):
    i = 0
    xk_list = []
    while i <= N:
        xk = B_j @ x0 + b_j
        xk_list.append(xk)
        x0 = xk 
        i += 1
    return xk_list
         

def plot_result(xk_list, N):
    x_num = np.size(xk_list[0])
    xs = []
    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    for i in range(x_num):
        xs.append(i+1)
    for i in range(N):
        ax.plot(xs, xk_list[i], label=r"$\{x\}$"+"$^{}$".format(i+1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    xlabels = [r'$x_{}$'.format(num) for num in range(x_num+1)]
    ax.set_xticklabels(xlabels)
    leg = plt.legend(fancybox=True, shadow=True, fontsize='large')
    plt.title("Jacobi迭代", fontproperties='simsun', fontsize=20)
    ax.grid()
    plt.show()


def main():
    augmented_matrix = np.array([[4,-1,0,2],[-1,4,-1,6],[0,-1,4,2]])
    B_j, b_j = input_matrix(augmented_matrix)
    x0 = np.array([0,0,0])
    N = 5
    re_list = caculate(B_j, b_j, x0, N)
    plot_result(re_list, N)


if __name__ == '__main__':
    main()
