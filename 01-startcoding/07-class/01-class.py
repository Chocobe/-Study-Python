class Person:
    def __init__(
        self,
        name: str,
        age: int,
        job: str
    ):
        self.name = name
        self.age = age
        self.job = job

    def introduce(self):
        print(f'I\'m {self.name} and {self.age}')
        print(f'I am working in {self.job}')

miles = Person('Miles', 37, 'FrontEnd')
kim = Person('Kim', 33, 'BackEnd')

miles.introduce()
kim.introduce()
