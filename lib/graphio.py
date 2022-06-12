import matplotlib.pyplot as plt

handler = [[], []]


def get_graph(plot: plt, name: str,
              x_label: str, y_label: str,
              data: list,
              settings: list):
    # settings list -> [(0) capsize: float, (1) elinewidth: float, (2) dot_size: float,
    #                   (3) dot_color: str,
    #                   (4) has_errors: bool, (5) new_fig: bool]

    # data list -> [(0) x: list, (1) y: list,
    #               (2) error_x: list, (3) error_y: list]

    if settings[5]:
        plot.figure()

    plot.xlabel(x_label)
    plot.ylabel(y_label)

    if settings[4]:
        handle = plot.errorbar(data[0], data[1],
                               xerr=data[2], yerr=data[3],
                               capsize=settings[0], elinewidth=settings[1], ls='none')
        handler[0].append(handle)
        handler[1].append(name)

    plot.scatter(data[0], data[1], s=settings[2], color=settings[3])


def handle_legend(plot: plt):
    plot.legend(handles=handler[0], labels=handler[1])
