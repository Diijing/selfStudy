def areaPrinter(width, verti):
    triangle = (width * verti) / 2
    square = width * verti
    print("삼각형의 넓이 : {}".format(triangle))
    print("사각형의 넓이 : {}".format(square))

a = int(input('가로 길이:'))
b = int(input('세로 길이:'))

areaPrinter(a, b)