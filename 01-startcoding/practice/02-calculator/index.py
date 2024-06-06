from components.Calculator import Calculator

Calculator()\
    .build(
        'intro', 
        '================================\n     프로그램을 시작합니다.\n================================\n'
    ).build(
        'ending', 
        '\n================================\n     프로그램을 종료합니다.\n================================'
    ).run()
