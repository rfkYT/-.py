print('Внимание! Программма не будет работать без установленного модуля "Tkinter"')
INP = int(input('Введи число:\n1 - игра "Камень, ножницы, бумага"\n2 - календарь\n3 - калькулятор\n4 - игра "Прямоугольник"\n5 - игра "Палочки"\n6 - игра "Квест"\n7 - старая версия игры "Палочки" без графического интерфейса\n'))
if INP == 1:
    import tkinter
    from tkinter.messagebox import *
    import time
    import random
    print('Внимание! Игра "Камень, ножницы, бумага" может выдать при первой попытке ошибку! Не обращайте внимания и наслаждайтесь дальше!;)')
    def rock():
        S_but["bg"] = "light grey"
        global player
        K_but["bg"] = "green"
        N_but["bg"] = "red"
        B_but["bg"] = "red"
        player = "Камень"
        S_but["state"] = "normal"
    def scissors():
        S_but["bg"] = "light grey"
        global player
        N_but["bg"] = "green"
        K_but["bg"] = "red"
        B_but["bg"] = "red"
        player = "Ножницы"
        S_but["state"] = "normal"
    def paper(): 
        S_but["bg"] = "light grey"
        global player
        B_but["bg"] = "green"
        K_but["bg"] = "red"
        N_but["bg"] = "red"
        player = "Бумага"
        S_but["state"] = "normal"
    def generate():
        S_but["bg"] = "green"
        B_but["bg"] = "light grey"
        K_but["bg"] = "light grey"
        N_but["bg"] = "light grey"
        global AI, player
        rand = random.randint(1,4)
        if rand == 1:
            AI = "Камень"
        elif rand == 2:
            AI = "Ножницы"
        elif rand == 3:
            AI = "Бумага"
        t3['text'] = "Выбор ИИ: " + AI
        t3.update()    
        if AI == player:
            print("Ничья.")
            tkinter.messagebox.showinfo('Результат', "Ничья")    
        if AI == "Камень" and player == "Ножницы":
            print ("ИИ победил.")
            tkinter.messagebox.showinfo('Результат', "ИИ победил")
        if AI == "Камень" and player == "Бумага":
            print ("Ты победил.")
            tkinter.messagebox.showinfo('Результат', "Ты победил")    
        if AI == "Ножницы" and player == "Камень":
            print ("Ты победил.")
            tkinter.messagebox.showinfo('Результат', "Ты победил")
        if AI == "Ножницы" and player == "Бумага":
            print ("ИИ победил.")
            tkinter.messagebox.showinfo('Результат', "ИИ победил.")
        if AI == "Бумага" and player == "Камень":
            print ("ИИ победил.")
            tkinter.messagebox.showinfo('Результат', "ИИ победил")
        if AI == "Бумага" and player == "Ножницы":
            print ("Ты победил.")
            tkinter.messagebox.showinfo('Результат', "Ты победил")
    root = tkinter.Tk()
    root.title("Камень, ножницы, бумага.")
    root.geometry('308x175')
    t1 = tkinter.Label(root, text = "Игрок", fg = "black", font = ("Comic Sans MS", 12))
    t1.grid(row = 0, column = 1)
    K_but = tkinter.Button(root, text = "Камень", fg = "black", font = ("Comic Sans MS", 12), command = rock)
    K_but.grid(row = 1, column = 0)
    N_but = tkinter.Button(root, text = "Ножницы", fg = "black", font = ("Comic Sans MS", 12), command = scissors)
    N_but.grid(row = 1, column = 1)
    B_but = tkinter.Button(root, text = "Бумага", fg = "black", font = ("Comic Sans MS", 12), command = paper)
    B_but.grid(row = 1, column = 2)
    t2 = tkinter.Label(root, text = "ИИ", fg = "black", font = ("Comic Sans MS", 12))
    t2.grid(row = 2, column = 1)
    S_but = tkinter.Button(root, text = "Сгенерировать", fg = "black", font = ("Comic Sans MS", 12), command = generate)
    S_but["state"] = "disabled"
    S_but.grid(row = 3, column = 1)
    t3 = tkinter.Label(root, text = "Выбор ИИ:", fg = "black", font = ("Comic Sans MS", 12))
    t3.grid(row = 4, column = 1)
    root.mainloop()
elif INP == 2:
    a = int(input("Введи номер больше ноля: "))
    if a < 0:
        print("Ошибка")
    else:
        b = a % 7
        if b == 0:
            print("Понедельник")
        elif b == 1:
            print("Вторник")
        elif b == 2:
            print("Среда")
        elif b == 3:
            print("Четверг")
        elif b == 4:
            print("Пятница")
        elif b == 5:
            print("Суббота")
        elif b == 6:
            print("Воскресенье")
    c = int(input("Введи номер от 1 до 12: "))
    if c < 0 or c > 12:
        print("Ошибка")
    else:
        if c == 1:
            print("Январь - зима")
        if c == 2:
            print("Февраль - зима")
        if c == 3:
            print("Март - весна")
        if c == 4:
            print("Апрель - весна")
        if c == 5:
            print("Май - весна")
        if c == 6:
            print("Июнь - лето")
        if c == 7:
            print("Июль - лето")
        if c == 8:
            print("Август - лето")
        if c == 9:
            print("Сентябрь - осень")
        if c == 10:
            print("Октябрь - осень")
        if c == 11:
            print("Ноябрь - осень")
        if c == 12:
            print("Декабрь - зима")
elif INP == 3:
    import tkinter
    def one():
        txtDispley.insert(tkinter.END, 1)
    def two():
        txtDispley.insert(tkinter.END, 2)    
    def three():
        txtDispley.insert(tkinter.END, 3)    
    def four():
        txtDispley.insert(tkinter.END, 4)
    def five():
        txtDispley.insert(tkinter.END, 5)
    def six():
        txtDispley.insert(tkinter.END, 6)
    def seven():
        txtDispley.insert(tkinter.END, 7)
    def eight():
        txtDispley.insert(tkinter.END, 8)
    def nine():
        txtDispley.insert(tkinter.END, 9)    
    def zero():
        txtDispley.insert(tkinter.END, 0)
    def plus():
        txtDispley.insert(tkinter.END, "+")
    def equally():
        result = eval(txtDispley.get())
        txtDispley.insert(tkinter.END, "=" + str(result))
        equallyButton['state'] = 'disable'
        txtDispley['state'] = 'readonly'
    def minus():
        txtDispley.insert(tkinter.END, "-")
    def split():
        txtDispley.insert(tkinter.END, "/")
    def multiplication():
        txtDispley.insert(tkinter.END, "*")
    def delet():
        equallyButton['state'] = 'normal'
        txtDispley['state'] = 'normal'
        txtDispley.delete(0, tkinter.END)
    calculator = tkinter.Tk()
    calculator.title("Калькулятор")
    calculator.geometry('275x379')
    txtDispley = tkinter.Entry(calculator)
    txtDispley.grid(row = 0, column = 0, columnspan = 4)
    oneButton = tkinter.Button(calculator, text = "1", fg = "black", height = 5, width = 5, command = one)
    oneButton.grid(row = 1, column = 0)
    twoButton = tkinter.Button(calculator, text = "2", fg = "black", height = 5, width = 5, command = two)
    twoButton.grid(row = 1, column = 1)
    threeButton = tkinter.Button(calculator, text = "3", fg = "black", height = 5, width = 5, command = three)
    threeButton.grid(row = 1, column = 2)
    fourButton = tkinter.Button(calculator, text = "4", fg = "black", height = 5, width = 5, command = four)
    fourButton.grid(row = 2, column = 0)
    fiveButton = tkinter.Button(calculator, text = "5", fg = "black", height = 5, width = 5, command = five)
    fiveButton.grid(row = 2, column = 1)
    sixButton = tkinter.Button(calculator, text = "6", fg = "black", height = 5, width = 5, command = six)
    sixButton.grid(row = 2, column = 2)
    sevenButton = tkinter.Button(calculator, text = "7", fg = "black", height = 5, width = 5, command = seven)
    sevenButton.grid(row = 3, column = 0)
    eightButton = tkinter.Button(calculator, text = "8", fg = "black", height = 5, width = 5, command = eight)
    eightButton.grid(row = 3, column = 1)
    nineButton = tkinter.Button(calculator, text = "9", fg = "black", height = 5, width = 5, command = nine)
    nineButton.grid(row = 3, column = 2)
    zeroButton = tkinter.Button(calculator, text = "0", fg = "black", height = 5, width = 5, command = zero)
    zeroButton.grid(row = 4, column = 1)
    plusButton = tkinter.Button(calculator, text = "+", fg = "black", height = 5, width = 5, command = plus)
    plusButton.grid(row = 4, column = 0)
    deleteButton = tkinter.Button(calculator, text = "Delete", fg = "black", height = 5, width = 5, command = delet)
    deleteButton.grid(row = 4, column = 2)
    minusButton = tkinter.Button(calculator, text = "-", fg = "black", height = 5, width = 5, command = minus)
    minusButton.grid(row = 1, column = 3)
    splitButton = tkinter.Button(calculator, text = "/", fg = "black", height = 5, width = 5, command = split)
    splitButton.grid(row = 2, column = 3)
    multiplicationButton = tkinter.Button(calculator, text = "*", fg = "black", height = 5, width = 5, command = multiplication)
    multiplicationButton.grid(row = 3, column = 3)
    equallyButton = tkinter.Button(calculator, text = "=", fg = "black", height = 5, width = 5, command = equally)
    equallyButton.grid(row = 4, column = 3)
    calculator.mainloop()
elif INP == 4:
    m = int(input("Введи количество строчек: "))
    n = int(input("Введи количество столбцов: "))
    k = int(input("Введи число, расположение которого ты хочешь знать: "))
    a = k // n + 1
    b = k % n
    if k % n == 0:
        b = n
        a = k // n
    print("Строка", a, "\nСтолбец", b)
elif INP == 5:
    import tkinter
    import random
    sticks = 20
    window = tkinter.Tk()
    window.geometry("550x200")
    def S1():
        global sticks
        sticks -= 1
        stick.config(text = sticks*"|")
        if sticks <= 0:
            stick.config(text = "ПК победил")
            stick.place(x = 145, y = 70)
            butt4['state'] = 'disable'
            butt1['state'] = 'disable'
            butt2['state'] = 'disable'
            butt3['state'] = 'disable'
        butt4['state'] = 'normal'
        butt1['state'] = 'disable'
        butt2['state'] = 'disable'
        butt3['state'] = 'disable'
    def S2():
        global sticks
        sticks -= 2
        stick.config(text = sticks*"|")
        if sticks <= 0:
            stick.config(text = "ПК победил")
            stick.place(x = 145, y = 70)
            butt4['state'] = 'disable'
            butt1['state'] = 'disable'
            butt2['state'] = 'disable'
            butt3['state'] = 'disable'
        butt4['state'] = 'normal'
        butt1['state'] = 'disable'
        butt2['state'] = 'disable'
        butt3['state'] = 'disable'
    def S3():
        global sticks
        sticks -= 3
        stick.config(text = sticks*"|")
        if sticks <= 0:
            stick.config(text = "ПК победил")
            stick.place(x = 145, y = 70)
            butt4['state'] = 'disable'
            butt1['state'] = 'disable'
            butt2['state'] = 'disable'
            butt3['state'] = 'disable'
        butt4['state'] = 'normal'
        butt1['state'] = 'disable'
        butt2['state'] = 'disable'
        butt3['state'] = 'disable'
    def S4():
        global sticks
        if sticks > 4:
            sticks -= random.randint(1,3)
            stick.config(text = sticks*"|")
        elif sticks == 4:
            sticks -= 3
            stick.config(text = sticks*"|")
        elif sticks == 3:
            sticks -= 2
            stick.config(text = sticks*"|")
        elif sticks == 2:
            sticks -= 1
            stick.config(text = sticks*"|")
        elif sticks == 1:
            sticks -= 1
            stick.config(text = sticks*"|")
        if sticks <= 0:
            stick.config(text = "Игрок победил")
            stick.place(x = 145, y = 70)
            butt4['state'] = 'disable'
            butt1['state'] = 'disable'
            butt2['state'] = 'disable'
            butt3['state'] = 'disable'
        butt4['state'] = 'disable'
        butt1['state'] = 'normal'
        butt2['state'] = 'normal'
        butt3['state'] = 'normal'
    text1 = tkinter.Label(window, text = "Сколько палочек будем брать?")
    text1.place(x = 185, y = 0)
    butt1 = tkinter.Button(window, text = "1", fg = "black", command = S1)
    butt1.place(x = 210, y = 30)
    butt2 = tkinter.Button(window, text = "2", fg = "black", command = S2)
    butt2.place(x = 265, y = 30)
    butt3 = tkinter.Button(window, text = "3", fg = "black", command = S3)
    butt3.place(x = 320, y = 30)
    stick = tkinter.Label(window, text = sticks * '|')
    stick.config(font = ("Arial Bold", 30, "bold"))
    stick.place(x = 125, y = 60)
    butt4 = tkinter.Button(window, text = "Ввод ПК", fg = "black", command = S4)
    butt4.place(x = 250, y = 120)
    butt4['state'] = 'disable'
    window.resizable(0,0)
    window.title("Палочки")
    window.mainloop()
elif INP == 2020:
    print("Не напоминай...")
elif INP == 6:
    print("             *Квест*")
    print("   Главный вход")
    print("1 - Деньги")
    print("2 - СМЕРТЬ")
    print("3 - Счастье")
    print("4 - Выиграть сейчас")
    a = int(input("Введите один из вариантов: "))
    if a <= 0 or a > 4:
        print("Ошибка")
    if a == 1:
        print("Деньги")
        print("Из-за денег у вас много проблем...")
        print("       ИГРА ОКОНЧЕНА   :(")
    if a == 2:
        print("СМЕРТЬ")
        print("1 - Быстрая смерть")
        print("2 - Медленная смерть")
        b = int(input("Введите номер смерти: "))
        if b == 1:
            print("Медленная смерть")
            print("Вас убил предатель")
            print("       ИГРА ОКОНЧЕНА   :(")
        if b == 2:
            print("Медленная смерть")
            print("1 - Умереть от старости")
            print("2 - Умереть сейчас")
            c = int(input("Введите медленную смерть: "))
            if c == 1:
                print("Умереть от старости")
                print("Вы умрёте\nНо потом")
                print("       ВЫ ВЫИГРАЛИ :)")
            if c == 2:
                print("Умереть сейчас")
                print("Вы медленно и мучительно умираете")
                print("       ИГРА ОКОНЧЕНА   :(")
    if a == 3:
        print("Счастье")
        print("Счастье исправило проблемы")
        print("       ВЫ ВЫИГРАЛИ :)")
    if a == 4:
        print("Нельзя так играть...")
        print("       Игра окончена   :(")
    print("Спасибо за то что дошли до конца!")
    print("          **** **** **** **** ")
    print("             * *  *    * *  * ")
    print("          **** *  * **** *  * ")
    print("          *    *  * *    *  * ")
    print("          **** **** **** **** ")
elif INP == 7:
    import random
    a = int(input("Введите количество палочек игрока: "))
    player = []
    for i in range(3):
        player.append(int(input("Введите количество палочек: ")))
    print ("Ваши палочки:", player)
    S = 0
    while S != a:
        AI = [] 
        S = 0
        for i in range(3):
            b = random.randint(0, a)
            AI.append(b)
            S = S + b
    print ("Палочки ИИ:", AI)
    score_player = 0
    score_AI = 0
    for i in range(3):
        if player[i] > AI[i]:
            score_player += 2
            score_AI += 1
        elif player[i] < AI[i]:
            score_AI += 2
            score_player += 1
    if score_player == score_AI:
        print("*******Ничья*********")
    elif score_player > score_AI:
        print("******Вы выиграли*******")
    elif score_player < score_AI:
        print("******Вы проиграли******")
else:
    print("Что-то не так, наверное вы ввели не то число")
print("Оцените игру от 0 до 5")
d = int(input("Введите оценку: "))
if d > 5 or d < 0:
    print("Ошибка")
else:
    if d == 0:
        print("Мало, очень мало...")
    elif d == 1:
        print("Я тебе не нравлюсь?")
    elif d == 2:
        print("Это не 5 звёзд.")
    elif d == 3:
        print("Неплохо.")
    elif d == 4:
        print("Хорошо.")
    elif d == 5:
        print("Эта большая оценка...")
print("Спасибо!")