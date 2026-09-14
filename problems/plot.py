import matplotlib.pyplot as plt


def data_plotting(title, x_bar, y_bar, x_label, y_label, stacked=False):
    """Plot normal or stacked bar chart."""

    plt.figure(figsize=(12, 6))

    if stacked:
        bottom = [0] * len(x_bar)

        for team, values in y_bar.items():
            plt.bar(x_bar, values, bottom=bottom, label=team)
            bottom = [a + b for a, b in zip(bottom, values)]

        plt.legend()
    else:
        plt.bar(x_bar, y_bar)

    plt.title(title, fontweight="bold")
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()