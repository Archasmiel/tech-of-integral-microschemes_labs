import matplotlib.pyplot as plt
import lib.graphio as gio


plot_settings = [2, 0.5, 2, 'k', True, False]


def read_data(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [i.strip().split(' ') for i in f.readlines()]
        data[0][0], data[0][1] = float(data[0][0]), float(data[0][1])

    res, x, y = [], [], []
    for i in data:
        if i == data[0]:
            res.append(i)
        if i != data[0] and i != data[-1]:
            x.append(float(i[1]))
            y.append(float(i[0]))

        if i == data[-1]:
            res.append(x)
            res.append(y)
            res.append(i)

    minim, maxim = min(x), max(x)

    return [res[1], res[2], [res[0][1]] * len(res[2]), [res[0][0]] * len(res[1])], data[-1], minim, maxim


def plot_graph(filename: str):
    data, meas, minim, maxim = read_data(filename)
    print(f'{filename} = [{minim}, {maxim}]')

    gio.get_graph(plot=plt,
                  name=filename.split('.')[0].split('data')[1],
                  x_label=f'Uz, {meas[1]}',
                  y_label=f'C1, {meas[0]}',
                  data=data,
                  settings=plot_settings)


def main():
    plot_graph('data1.txt')
    plot_graph('data2.txt')
    gio.handle_legend(plt)
    plt.grid(visible=True, which='both', color='0.75', linestyle='-')
    plt.show()


if __name__ == '__main__':
    main()
