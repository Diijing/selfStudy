garo = int(input('가로 길이 입력:'))
sero = int(input('세로 길이 입력:'))

triangleArea = garo*sero/2
squareArea = garo*sero

print('-'*10 + 'Result' + '-'*10)
print('삼각형 넓이 : %f' % triangleArea)
print('사각형 넓이 : %f' % squareArea)
print('사각형 넓이 : %.2f' % triangleArea)
print('사각형 넓이 : %.2f' % squareArea)


