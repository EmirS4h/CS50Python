class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size if self._size > 0 else "No Cookies"

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity can not be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def deposit(self, number_of_cookies: int):
        if self._size + number_of_cookies > self._capacity:
            raise ValueError("Capacity Limit")
        self._size += number_of_cookies

    def withdraw(self, number_of_cookies: int):
        if self._size - number_of_cookies < 0:
            raise ValueError("Not Enoguh Cookies to take from")
        self._size -= number_of_cookies


def main():
    jar = Jar(2)
    print(jar.capacity)
    print(jar.size)
    print(jar)
    jar.deposit(2)
    print(jar.size)
    print(jar)
    jar.withdraw(1)
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()
