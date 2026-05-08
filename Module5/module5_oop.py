class NumberStorage:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        for index, number in enumerate(self.numbers, start=1):
            if number == x:
                return index
        return -1


def main():
    n = int(input("Enter N: "))

    storage = NumberStorage()

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        storage.insert(number)

    x = int(input("Enter X: "))

    print(storage.search(x))


if __name__ == "__main__":
    main()