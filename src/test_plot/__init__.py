import matplotlib as mp
import matplotlib.pyplot as plt


def main() -> None:
    print("Hello from test-plot!")
    print(mp.get_backend())
    plt.plot(1, 2)
    plt.xlabel("t")
    plt.ylabel("h")
    plt.show()
