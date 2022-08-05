#Calc


while True:
    print("\n"
        "Ввод 'Q' останавливает программу."
          "\n")


    a = input('Введите первое число:  ')
    if a=="q" or a=="Q":
        break
    if not a.isdigit():
        print("\n"
              'Не является числом!'
              "\n____________________")
        continue


    x = input('Знак действия(+,-,*,/,**,sqrt):  ')
    if x!='+' and x!='-' and x!='*' and x!='/' and x!='**' and x!='sqrt':
        print("\n"
              "Не верный знак."
              "\n________________")
        continue
    if x=="q" or x=="Q":
        break


    b = input('Введите второе число:  ')
    if b=="q" or b=="Q":
        break
    if not b.isdigit():
        print("\n"
              'Не является числом!'
              "\n____________________")
        continue


    if x=="+":
        print("Ответ:  ", str(int(a)+int(b)))


    elif x=="-":
        print("Ответ:  ", str(int(a)-int(b)))


    elif x=="*":
        print("Ответ:  ", str(int(a)*int(b)))


    elif x=='**':
        print("Ответ:  ", str(int(a)**int(b)))


    elif x=='sqrt':
        print("Ответ:  ", int(b)**(1/int(a)))


    else:
        if b=='0':
            print("Делить на ноль нельзя!")
        else:
            print("Ответ:  ", int(a)/int(b))


