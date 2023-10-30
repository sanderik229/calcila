try:
    RestartCalcul = 'q'
    while RestartCalcul == 'q':
        import math
        Number_1 = int (input("Введите число"))
        оperation = input ("Введите операцию") 
        Number_2 = int (input("Введите число")) 
        sin = math.sin
        cos = math.cos
        tag = math.tan
        root = (Number_1 ** 0.5)
        factorial = math.factorial 
        if оperation == '+': 
            print (Number_1 + Number_2) 
        elif   оperation == '-': 
            print (Number_1 - Number_2) 
        elif оperation == "*": 
            print (Number_1 * Number_2) 
        elif оperation == '/': 
            if Number_1 == 0:
                print ("Ошибка: деление на 0 невозможно!") 
            else:
                print (Number_1 / Number_2)
                
        elif оperation == '**': 
            print (Number_1 ** Number_2)
        elif оperation == '%': 
            print (Number_1 % Number_2)
        elif  оperation == "син" :
            print (math.sin (Number_1))
        elif оperation == 'кос':
            print (math.cos(Number_1))
        elif оperation == 'таг':
            print (math.tan (Number_1))
        elif оperation == 'корень':
            print (Number_1 ** 0.5)
        elif оperation == "факториал":
            print (math.factorial (Number_1))
        else: 
            print ("Ошибка")
        RestartCalcul = input("Введите 'q' чтобы начать заново")
except (ValueError,SyntaxError,ZeroDivisionError):
    print("Ошибка")