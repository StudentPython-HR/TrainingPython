class MyCustomException(Exception):
    pass
import operator
def main(input):
    input = str(input("Введите выражение, разделяя цифры и знаки пробелами: \n"))
    input1 = input.split()
    data = len(input1)
    if data == 3:
        pass
    else:
        exception()
    try:
        int(input1[0]) and int(input1[2])
    except:
        exception()
    a = int(input1[0])
    act = input1[1]
    b = int(input1[2])
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = ['+','-','*','/']
    if list1.count(a) and list1.count(b) and list2.count(act):
        pass
    else:
        exception()

    ops = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.floordiv}
    op_func = ops[act]
    result = op_func(a, b)
    print("результат:", result)
def exception():
    print("Формат математической операции не удовлетворяет заданию - два целых числа от 1 до 10 и один оператор (+, -, /, *)")
    raise MyCustomException("Формат математической операции не удовлетворяет заданию - два целых числа от 1 до 10 и один оператор (+, -, /, *)")

main(input)