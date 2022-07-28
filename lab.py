class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, 2023-year)

    def check_age(self):
        if self.age >= 19:
            return True
        else:
            return False


person3 = Person.details('wow', 2010)
person1 = Person('adult', 30)
person2 = Person('student', 15)


# class Point:

#     def __init__(self, x, y):
#         self.x = x  # x좌표
#         self.y = y  # y좌표


# class Rectangle:

#     def __init__(self, p1, p2):
#         self.p1 = p1  # 좌측 상단 좌표
#         self.p2 = p2  # 우측 하단 좌표

#     def get_area(self):
#         (self_a, self_b) = self.p1 #이렇게 하려면 이와 관련된 매직 메서드를 찾아봐야됨.
#         (self_c, self_d) = self.p2 # 그리고 이렇게 할 필요는 없음. UNPACKING이 안됨. 인스턴스는 패키징이니까 못쪼갬. 걍둬야됨.
#         return abs((self_a - self_c) * (self_b - self_d))

#     def get_perimeter(self):
#         (a, b) = self.p1
#         (c, d) = self.p2
#         return 2 * (abs(a-c)+abs(b-d))

#     def is_square(self):
#         (a, b) = self.p1
#         (c, d) = self.p2
#         if abs(a-c) == abs(b-d):
#             return True
#         else:
#             return False

class Point:

    def __init__(self, x, y):
        self.x = x  # x좌표
        self.y = y  # y좌표


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1  # 좌측 상단 좌표
        self.p2 = p2  # 우측 하단 좌표

    def get_area(self):
        # self.p1이 한 덩어리가 되고 여기의 x다 여서 .x가 됨
        (self_a, self_b) = self.p1.x, self.p1.y
        (self_c, self_d) = self.p2.x, self.p2.y  # . 은 상하위 관계? 포함관계 임
        return abs((self_a - self_c) * (self_b - self_d))

    def get_perimeter(self):
        (a, b) = self.p1.x, self.p1.y
        (c, d) = self.p2.x, self.p2.y
        return 2 * (abs(a-c)+abs(b-d))

    def is_square(self):
        (a, b) = self.p1.x, self.p1.y
        (c, d) = self.p2.x, self.p2.y
        if abs(a-c) == abs(b-d):
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(p1.y)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
