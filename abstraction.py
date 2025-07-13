def biggestDivision(a, b, div):
    if a == b:
        return a

    if div == 1:
        return 1

    if a % div == 0 and b % div == 0:
        return div

    return biggestDivision(a, b, div - 1)


class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.denom = y
        self.value = x / y

    def __str__(self):
        return "{0} {1}".format(self.num, self.denom)

    def shorten(x, y):
        if y % x == 0:
            return [1, y / x]
        if x % y == 0:
            return [x / y, 1]

        bigDiv = biggestDivision(
            x, y, x - 1) if x < y else biggestDivision(x, y, y - 1)
        if bigDiv != 1:
            return [x / bigDiv, y / bigDiv]

        return [x, y]

    def add(self, x, y):
        if y == self.denom:
            return self.shorten(x + self.num, y)

        x1 = x * self.denom
        x2 = self.num * y
        newY = y * self.denom

        return self.shorten(x1 + x2, newY)


a, b = map(input().split())
x, y = map(input().split())

f = Fraction(a, b)

print(f.add(x, y))
