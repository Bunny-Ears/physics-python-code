import matplotlib.pyplot as plt
import matplotlib as mp


def main() -> None:
    print("Hello from test-plot!")
    print((mp.get_backend()))
    plt.plot(1, 2)
    plt.xlabel("t")
    plt.ylabel("h")
    plt.show()
