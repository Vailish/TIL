s_triangle = '3 4 5'
a, b, c = sorted(list(map(int, s_triangle.split())))

if a == b == c:
    print('정삼각형')
elif (a == b and a == c) or (b == c, b == a) or (c == a, c == b):
    print('이등변삼각형')
else:
    if a**2 + b**2 == c**2:
        print('직각삼각형')
    elif a + b > c:
        print('삼각형')
    else:
        print('삼각형 아님')