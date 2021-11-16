import matplotlib.pyplot as plt
import math

"""
0.01 0.005 0.01 0.01 0.01 0.015
36 314 70
0.428 0.0175
0.01
"""


global a1, a2, b1, b2, c, d
global Ubx, W, Rn
global f0, ro
global Xbx



global x_list
global Sya, Sc, Sb
global Lmid, Dpr, Dpr_gost, d_gost
global Q, q, Wspiral

global M0, Rct, Rb, Rm, L

global XL, z, Rl

global I


def gost_round(Dpr: float) -> (float, float):
    Nom = [0.02, 0.025, 0.03, 0.032, 0.035, 0.04, 0.045, 0.05, 0.06, 0.063, 0.071, 0.08, 0.09, 0.1, 0.112, 0.12, 0.125,
           0.13, 0.14, 0.16, 0.18, 0.19, 0.2, 0.21, 0.224, 0.236, 0.25, 0.265, 0.28, 0.3, 0.315, 0.335, 0.355, 0.38,
           0.4, 0.425, 0.45, 0.475, 0.5, 0.53, 0.56, 0.6, 0.63, 0.67, 0.69, 0.71, 0.75, 0.77, 0.8, 0.83, 0.85, 0.9,
           0.93, 0.95, 1, 1.06, 1.08, 1.12, 1.18, 1.25, 1.32, 1.4, 1.45, 1.5, 1.56, 1.6, 1.7, 1.8, 1.9, 2, 2.12, 2.24,
           2.36, 2.44, 2.5]

    type2 = [0.027, 0.034, 0.04, 0.043, 0.047, 0.054, 0.061, 0.068, 0.081, 0.085, 0.095, 0.105, 0.117, 0.129, 0.143,
             0.153, 0.159, 0.165, 0.176, 0.199, 0.222, 0.234, 0.245, 0.258, 0.272, 0.285, 0.301, 0.319, 0.334, 0.355,
             0.371, 0.393, 0.414, 0.441, 0.462, 0.489, 0.516, 0.543, 0.569, 0.601, 0.632, 0.676, 0.706, 0.749, 0.77,
             0.79, 0.832, 0.854, 0.885, 0.916, 0.937, 0.99, 1.02, 1.041, 1.093, 1.155, 1.176, 1.217, 1.279, 1.351,
             1.423, 1.506, 1.557, 1.608, 1.67, 1.711, 1.813, 1.916, 2.018, 2.12, 2.243, 2.366, 2.488, 2.57, 2.631]

    if Dpr < Nom[0]:
        return [Nom[0], type2[0]]

    elif Dpr > Nom[-1]:
        return [Nom[-1], type2[-1]]

    for i in range(0, len(Nom) - 1):

        if Nom[i] <= Dpr <= Nom[i + 1]:

            if (Dpr - Nom[i]) < (Nom[i + 1] - Dpr):
                return [Nom[i], type2[i]]

            else:
                return [Nom[i + 1], type2[i + 1]]


def get_globals() -> None:
    # a1, a2, b1, b2, c ,d
    a1, a2, b1, b2, c, d = list(map(float, (input(f"Введите параметры"
                                                  "магнитопровода\n"
                                                  "через пробел в МЕТРАХ\n"
                                                  "a[1], a[2], b[1], b[2], c, d: ").strip().split())))

    print(f"\n{a1 = }, {a2 = }, {b1 = }, {b2 = }, {c = }, {d = }\n")
    globals().update({'a1': a1, 'a2': a2, 'b1': b1, 'b2': b2, 'c': c, 'd': d})

    # Ubx, W, Rn
    Ubx, W, Rn = list((map(float, (input("Введите параметры питающей сети\n"
                                         "через пробел в МЕТРАХ\n"
                                         "U[bx], W, R[n]: ").strip().split()))))

    print(f"\n{Ubx = }, {W = }{Rn = }\n")
    globals().update({'Ubx': Ubx, 'W': W, 'Rn': Rn})

    # f0, ro

    f0, ro = list((map(float, (input("Введите параметры катушки индуктивности\n"
                                     "через пробел в МЕТРАХ\n"
                                     "f[0], ro: ").strip().split()))))

    print(f"\n{f0 = }, {ro = }\n")
    globals().update({'f0': f0, 'ro': ro})

    # Xbx

    Xbx = float((input("Введите параметр якоря\n"
                       "X[bx]: (в МЕТРАХ)").strip()))

    print(f"\n{Xbx = }\n")
    globals().update({'Xbx': Xbx})


def set_globals(globals_dict) -> None:
    globals().update(globals_dict)


def ex_1() -> None:
    print("\nЗадание 1:")

    # Sya, Sc, Sb

    Sya = a2 * b2
    Sc = Sb = a1 * b1

    print(f"\n{Sya = }, {Sc = }, {Sb = }\n")
    globals().update({'Sya': Sya, 'Sb': Sb, 'Sc': Sc})


def ex_2() -> None:
    print("\nЗадание 2:")

    # Lmid, Dpr, Dpr_gost, d_gost

    Lmid = 2 * (a1 + b1) + math.pi * b1
    Dpr = ((4 * Lmid * ro * W) / (math.pi * Rn)) ** 0.5
    Dpr_gost, d_gost = gost_round(Dpr)

    print(f"\n{Lmid = }м, {Dpr = }мм, {Dpr_gost = }мм, {d_gost = }мм")
    globals().update({'Lmid': Lmid, 'Dpr': Dpr, 'Dpr_gost': Dpr_gost, 'd_gost': d_gost})

    # Q, q, Wspiral

    Q = d * c
    q = (math.pi / 4) * ((d_gost / 1000) ** 2)
    Wspiral = Q * f0 / q

    print(f"\n{Q = }м^2, {q = }м^2, {Wspiral = }\n")
    globals().update({'Q': Q, 'q': q, 'Wspiral': Wspiral})


def ex_3() -> None:
    print("\nЗадание 3:")

    # M0, Rct, Rb, Rm, L

    M0 = 4 * math.pi * (10 ** (-7))
    Rct = 0
    Rb = (2 * Xbx) / (M0 * Sb)
    Rm = Rb + Rct
    L = (Wspiral ** 2) / Rm

    print(f"\n{M0 = } Гн/м, {Rct = }, {Rb = }, {Rm = }, {L = } Гн\n")
    globals().update({'M0': M0, 'Rct': Rct, 'Rb': Rb, 'Rm': Rm, 'L': L})

    y_list = [((Wspiral ** 2) * M0 * Sb * 1000) / (2 * Xbx_tmp) for Xbx_tmp in x_list]

    draw(x_list, y_list, name_x='Xbx, м', name_y='L, мГн')


def ex_4() -> None:
    print("\nЗадание 4:")

    # Xl, z,Rl

    Xl = W * L
    Rl = 0
    z = ((Rn + Rl) ** 2 + (Xl ** 2)) ** 0.5

    print(f"\n{Xl = }, {z = } Ом, {Rl = } Ом\n")
    globals().update({'Xl': Xl, 'z': z, 'Rl': Rl})

    y_list = [((Rn ** 2) + (((Wspiral ** 2) * M0 * W * Sb) / (2 * Xbx_tmp)) ** 2) ** 0.5 for Xbx_tmp in x_list]

    draw(x_list, y_list, name_x='Xbx, м', name_y='Z, Ом')


def ex_5() -> None:
    print("\nЗадание 5:")

    # I

    I = (Ubx / ((Rn ** 2 + ((Wspiral ** 2 * M0 * W * Sb) / (2 * Xbx)) ** 2) ** 0.5)) * 1000

    print(f"\n{I = } мА\n")
    globals().update({'I': I})

    y_list = [(Ubx / ((Rn ** 2 + ((Wspiral ** 2 * M0 * W * Sb) / (2 * Xbx_tmp)) ** 2) ** 0.5)) * 1000 for Xbx_tmp in
              x_list]

    draw(x_list, y_list, name_x='Xbx, м', name_y='I, мA')


def draw(x: list, y: list, name_x: str, name_y: str) -> None:
    with open(f"rk2 {name_x} - {name_y}.txt", "w") as f:
        f.write("n;x;y\n")
        for i in range(len(x)):
            f.write(f"{i};{x[i]};{y[i]}\n")
    plt.grid()

    plt.ylabel(name_y)
    plt.xlabel(name_x)

    plt.plot(x, y, 'ro')
    for i, i_xy in enumerate(zip(x, y)):
        i_x, i_y = i_xy
        if i >= len(x) / 2:
            plt.text(i_x, i_y, f"({i_x}, {round(i_y, 3)})   ", horizontalalignment='right')
        else:
            plt.text(i_x, i_y, f"   ({i_x}, {round(i_y, 3)})", horizontalalignment='left')
    plt.plot(x, y)
    plt.savefig(f"rk2 {name_x} - {name_y}.txt.png")
    plt.show()
    plt.clf()
    plt.cla()


if __name__ == '__main__':
    globals_dict = {'a1': 0.01, 'a2': 0.005, 'b1': 0.01, 'b2': 0.01, 'c': 0.01, 'd': 0.015, 'Ubx': 36, 'W': 314, 'Rn': 70, 'f0': 0.428, 'ro': 0.0175, 'Xbx': 0.00001}
    set_globals(globals_dict)
    #get_globals()
    
    x_list = []
    koefs = [0.5, 0.7, 0.8, 0.9, 1, 1.2, 1.4, 1.6, 1.8]
    tmp1 = str(Xbx).split('.')
    if len(tmp1) == 2:
        for koef in koefs:
            x_list.append(round(Xbx * koef, len(tmp1[1]) + 1))
    else:
        for koef in koefs:
            x_list.append(Xbx * koef)
    globals().update({'x_list': x_list})

    # get_globals()
    ex_1()
    ex_2()
    ex_3()
    ex_4()
    ex_5()

# Xl = W * L
# Z = (Rn**2 + Xl**2)**0.5


# I = Ubx / Z


# x = [0.005, 0.007,0.008, 0.009, 0.01, 0.012, 0.014,  0.016, 0.018]

# 3
# L = (Wspiral**2 * M0 * Sb) / (2 * Xbx)
# 4
# z = (Rn**2 + ((Wspiral**2 * M0 * W * Sb) / (2 * Xbx))**2)**0.5
# 5
# I = Ubx / ((Rn**2 + ((Wspiral**2 * M0 * W * Sb) / (2 * Xbx))**2)**0.5)
