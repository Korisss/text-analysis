import matplotlib.pyplot as plt


def plot_text(name: str, text: list[tuple[str, int]]) -> None:
    plt.xticks(rotation=90)
    plt.title(name)
    plt.bar(*zip(*text))
    plt.show()


def plot_sounds(name: str, sounds: dict[str, int]) -> None:
    plt.xticks(rotation=90)
    plt.title(name)

    tuples = [(v, k) for k, v in sounds.items()]
    tuples.sort()
    tuples = [(v, k) for (k, v) in tuples]
    tuples.reverse()

    plt.bar(*zip(*tuples))
    plt.show()
