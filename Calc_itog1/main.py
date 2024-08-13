class MyCustomException(Exception):
    pass
import operator
def main(input: str):
    input = str(input("Введите выражение, разделяя цифры и знаки пробелами: \n"))
    input1 = input.split()
    data = len(input1)
    if data == 3:
        pass
    else:
        raise MyCustomException("Формат математической операции не удовлетворяет заданию - два целых числа от 1 до 10 и один оператор (+, -, /, *)")

    try:
        int(input1[0]) and int(input1[2])
    except:
        raise MyCustomException("Формат математической операции не удовлетворяет заданию - два целых числа от 1 до 10 и один оператор (+, -, /, *)")

    a = int(input1[0])
    act = input1[1]
    b = int(input1[2])
    list = ['+','-','*','/']
    if 1 <= a <= 10 and 1 <= b <= 10 and list.count(act):
        pass
    else:
        raise MyCustomException("Формат математической операции не удовлетворяет заданию - два целых числа от 1 до 10 и один оператор (+, -, /, *)")

    ops = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.floordiv}
    op_func = ops[act]
    result = str(op_func(a, b))
    print("результат:", result)

main(input)
