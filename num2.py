import matplotlib.pyplot as plt
import math

"""
0.01 0.005 0.01 0.01 0.01 0.015
36 314 70
0.428 0.0175
0.01
"""

global x_list

global a, b, E, W, Xbx
global Ubx, W, Rn

def get_globals() -> None:
    a, b, E, Xbx, Ubx, Rn, W = list(map(float, (input(f"Введите параметры"
                                                "конденсатора\n"
                                                "через пробел в мм и Ом\n"
                                                "a, b, E, Xbx, Ubx, Rn, W: ").strip().split())))

    print(f"\n{a = }, {b = }, {E = }, {Xbx = }, {Ubx = }, {Rn = }, {W = }\n")
    globals().update({'a': a, 'b': b, 'E': E, 'Xbx': Xbx, 'Ubx': Ubx, 'Rn': Rn, 'W': W})


def set_globals(globals_dict) -> None:
    globals().update(globals_dict)


def ex() -> None:
    # S 
    S = a * b 
    E0 = 8.85 * (10 ** -15)
    C = (E * E0 * S) / Xbx
    print(f"\nC = {C * 10**9} нФ\n")
    
    y_list = [(E * E0 * S * 10**9) / Xbx_tmp for Xbx_tmp in x_list] 
    draw(x_list, y_list, name_x='Xbx, мм', name_y='C, нФ')
    
    print(((Xbx) / (E* E0 * S * W)) ** -1)
    Uout = (Ubx * Rn) / ((Rn**2 + ((Xbx) / (E * E0 * S * W))**2)**0.5) 
    print(f"\n{Uout = } В\n")
    
    y_list = [(Ubx * Rn) / ((Rn**2 + ((Xbx_tmp) / (E* E0 * S * W))**2)**0.5) for Xbx_tmp in x_list]
    draw(x_list, y_list, name_x='Xbx, мм', name_y='Uвых, В')


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
    #globals_dict = {'a': 71, 'b': 71, 'E': 1, 'Xbx': 0.01, 'Ubx': 36, 'Rn': 30000, 'W': 10**5}
    #set_globals(globals_dict)
    get_globals()

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

    ex()