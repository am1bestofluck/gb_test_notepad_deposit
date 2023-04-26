from enum import Enum, auto


class MainTopics(Enum):
    car = auto()
    driver = auto()


def main():
    a = MainTopics.car
    b = MainTopics.driver
    print(a)
    print(b)


if __name__ == "__main__":
    main()
