
# TASK N1
x = 3;
y = 5;
print(x, y)
print(type(y), type(x))
a = int(input("insert x: "))
b = int(input("insert y: "))
x = a
y = b
c = input('insert any noun: ')
d = input('insert any verb: ')
e = input('else one noun: ')
print(x, c, y, d, e)
print(type(x), type(y), type(a), type(b), type(c), type(d), type(e))

# TASK N2
# transform number in seconds to format HH:MM:SS
'''
FORMATTING EXAMPLE
print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))
print("{:>20} {:>20} {:>20}".format('my_param_1', 'my_param_2', 'my_param_3'))

ip = '192.168'
mask = 10
print(f"ip-params: {ip}, mask: {mask}")
'''
time = int(input ('insert number of sec: '))
h = int(time//3600)
m = int(time%3600//60)
s = int(time%3600%60)
print(f"{h}:{m}:{s}")

# # TASK N3
# # given number "n". Find summ n+nn+nnn.
n = (input('insert real number: n='))
print(f':{int(n) + int(n+n) + int(n+n+n)}')

# TASK N4
# insert real number. find greatest digit.
n = int(input('insert integer number >0: '))
a = -1 # any digit <0
while n > 10:
    b = n % 10
    n //= 10 # put off latest digit (eq. division on 10)
    if b > a:
        a = b
print(a)

TASK N5
'''
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение
 прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
 прибыль фирмы в расчете на одного сотрудника.
'''
profit = int(input('input your profit: '))
expense = int(input('input your expense: '))
if profit>expense:
    print ('your profit equal: ', profit-expense)
    print ('your profability equal: ', profit/expense)
    employee = int(input('input number of employee: '))
    print ('your profit per employee equal', profit/employee)
if profit<expense:
    print ('your expense equal: ', expense-profit)
if profit==expense:
    print ('your profit equal expenses')

# TASK N6
'''
Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который
общий результат спортсмена составить не менее b километров. Программа
должна принимать значения параметров a и b и выводить одно натуральное
число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''
a = int(input('input real number - initial: '))
b = int(input('input real number - target: '))
n = 1
while a<b:
    print (n, '- th day: ', a)
    a = a+a*0.1
    n = n+1
else:
    print(n, '- th day: ', a)
    print ('on the', n, '- th day the athlet take a goal: not less', b, 'km')