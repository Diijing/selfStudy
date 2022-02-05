name = input('이름 입력: ')
email = input('메일 입력: ')
ied = input('아이디 입력: ')
password = input('비밀번호 입력: ')
juminFrond = input('주민번호 앞자리 입력: ')
juminBack = input('주민번호 뒷자리 입력: ')
address = input('주소 입력: ')

print('비밀번호 : {}'.format('*' * len(password)))
print('주민번호 : {} - {}{}'.format(juminFrond, juminBack[0], '*' * len(juminBack[1:])))


