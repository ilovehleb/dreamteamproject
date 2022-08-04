#Calc
while True:
    print("\n"
        "Ввод 'Q' останавливает программу."
          "\n")
    a = input('Введите первое число:  ')
    if a=="q" or a=="Q":
        break
    x = input('Знак действия:  ')
    if x!='+' and x!='-' and x!='*' and x!='/':
        print("\n"
              "Не верный знак."
              "\n")
        continue
    if x=="q" or x=="Q":
        break
    b = input('Введите второе число:  ')
    if b=="q" or b=="Q":
        break
    if a=="q" or a=="Q" or x=="q" or x=="Q" or b=="q" or b=="Q":
        break
    elif x=="+":
        print("\n"
              "Ответ:  ",int(a)+int(b))
    elif x=="-":
        print("\n"
              "Ответ:  ",int(a)-int(b))
    elif x=="*":
        print("\n"
              "Ответ:  ",int(a)*int(b))
    else:
        if b=='0':
            print("Делить на ноль нельзя!")
        else:
            print("\n"
                  "Ответ:  ",int(a)/int(b))
