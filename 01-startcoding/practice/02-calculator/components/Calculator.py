from components.Message import Message

class Calculator:
    def __init__(self):
        self.values: list[int] = []
        self.operators: list[str] = []


    def build(
        self, 
        type: str,
        message: str
    ):
        if type == 'intro':
            self.intro_message = Message(message)
        elif type == 'ending':
            self.ending_message = Message(message)

        return self


    def input_formula(self):
        while True:
            newValue = int(input('> 숫자를 입력해주세요: '))
            self.values.append(newValue)

            if len(self.values) == 2:
                return

            newOperator = input('> 연산자를 입력해주세요: ')
            self.operators.append(newOperator)


    def calculate(self):
        values = self.values
        operators = self.operators

        result = values[0]
        formula = f'{values[0]}'

        for index_of_values in range(1, len(values)):
            value = values[index_of_values]
            operator = operators[index_of_values - 1]

            if operator == '+':
                result += value
                formula = f'{formula} {operator} {value}'
            elif operator == '-':
                result -= value
                formula = f'{formula} {operator} {value}'
            elif operator == '*':
                result *= value
                formula = f'{formula} {operator} {value}'
            elif operator == '/':
                result /= value
                formula = f'{formula} {operator} {value}'
            elif operator == '//':
                result //= value
                formula = f'{formula} {operator} {value}'
            else:
                print('유효하지 않은 연산자가 있습니다.')
                return

        print(f'\n>>> 결과: {formula} = {result}')
        return result


    def run(self):
        intro_message = self.intro_message
        ending_message = self.ending_message

        if (intro_message):
            intro_message.printMessage()

        self.input_formula()
        result = self.calculate()

        if (ending_message):
            ending_message.printMessage()

        return result
