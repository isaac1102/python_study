# Section02-1
# 파이썬 기초코딩
# Print 구문 예제

# 기본출력
print('Hello Python!')
print("Hello Python!!")
print("""Hello Python!!!""")
print('''Hello python!!!!''')

print()

# Separator 옵션 사용
# print문을 잘 사용할 수 있어야 한다. 
# 모든 옵션을 사용할 줄 알아야 함.

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep="@")

# end 옵션 사용
print('Welcome to ', end='')
print('the black Paradise', end=' ')
print('piano note')

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'me'))
print("{0} and {1} and {1}".format('You', 'Me'))
print("{a} and {b}".format(a="You", b="Me"))

print("%s's favor number is %d" %('Euijin', 7) )

print("Test1: %5d, price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(787, 6543.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=12334, b=1242.534))

print()

print('\'you\'')
print("'you'")
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('test')