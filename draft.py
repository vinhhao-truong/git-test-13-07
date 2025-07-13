# def printStudentInfo(name, age, school):
#     print(name, "hien tai dang", age, "tuoi va dang hoc o", school)


# printStudentInfo("Long", 18, "Le Quy Don")
# printStudentInfo("Hao", 18, "Tran Hung Dao")
# printStudentInfo("Tien", 17, "Nguyen Hien")
import math


class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.math = []

    def __str__(self):
        return "Em ten " + self.name + ", nam nay em " + str(self.age) + " tuoi."

    def math_recording(self, score):
        self.math.append(score)

    def get_math_avg(self):
        if len(self.math) == 0:
            return 0

        math_total = 0
        for i in range(len(self.math)):
            math_total += self.math[i]
        return math_total / len(self.math)


long = Student("Long", 18, "Le Quy Don")
tien = Student("Tien", 10, "Doi")

long.math_recording(10)
long.math_recording(3)
long.math_recording(7)
long.math_recording(8)

print(long)

# tien.math_recording(5)
# tien.math_recording(6)

# print(long.get_math_avg())
# print(tien.get_math_avg())

print("{0} {1}, {2}".format("long", "le", "hoang"))

print("hao-2")