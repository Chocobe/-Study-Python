def print_intro():
    print('==========================================')
    print('==                                      ==')
    print('==         Calculator by Python         ==')
    print('==                                      ==')
    print('==========================================')

def calculate(values, operators):
    formula = f'{values[0]}'
    result = values[0]

    for index in range(1, len(values)):
        operator = operators[index - 1]
        rhs = values[index]
        formula = f'{formula} {operator} {rhs}'

        if operator == '+':
            result += rhs
        elif operator == '-':
            result -= rhs
        elif operator == '*':
            result *= rhs
        elif operator == '/':
            result /= rhs
        elif operator == '//':
            result //= rhs
        else:
            print('잘못된 연산자가 있습니다.')

    return f'{formula} = {result}'

def printResult(result):
    print('\n==========================================\n')
    print(f'결과: {result}')
    print('프로그램을 종료합니다.')

def run():
    data = {
        'values': [],
        'operators': [],
    }

    while True:
        newValue = int(input('\n> 숫자를 입력해 주세요: '))
        data['values'].append(newValue)

        print('\n(계산을 실행하려면 "run" 을 입력해주세요)')
        newOperator = input('> 연산자를 입력해주세요: ')

        if (newOperator == '='):
            result = calculate(data['values'], data['operators'])
            printResult(result)
            return

        data['operators'].append(newOperator)

print_intro()
run()
