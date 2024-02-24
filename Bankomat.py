data_card = {"pin_card": 5577, "balance": 1000, "card_number": "8600000011119999", "phone_number": ""}

def main():  
    """Eng birinchi funksiya: ya'ni bunda siz kerakli tilni tanlaysiz !!! """
    print()
    language = input("""Tilni Tanlang : Выберите Язык : Choose Language : 

        1. Uzbek tili : Узбекский язык : Uzbek Language
        2. Русский язык : Rus tili : Russian Language
        3. English language : Английский язык : Ingliz tili
    >>> """)
    if language == "1":
        return uz()

    elif language == "2":
        return ru()

    elif language == "3":
        return eng()
    else:
        print("No'tog'ri son kiritdingiz !!!")
        return main()
# O'zbek tili menyusi

# karta balansi
def card_balance():
    """O'zbek tilida kartaning balansini ko'rish funksiyasi"""
    print()
    print(f"Sizning 💳kartangizdagi💳 mablag' {data_card['balance']}💲")
    print()
    print("Ortga qaytish funksiyasi 👇")
    card_balance_back = input("""
        1. Bitta ortga qaytish
        2. Tilni tanlashga qaytish
    >>>>""")

    if card_balance_back == '1':
        return service_uz()
    elif card_balance_back == '2':
        return main()
    else:
        print('Siz kiritgan son yo\'q!!!')
        return card_balance()

# pul yechish 
def check(money):
    """Bunda balansdagi pulni 1.01 ga kopaytirganda pul yetishini bilib oladigan funksiya"""
    if data_card['balance'] >= money * 1.01:
        return True
    else:
        return False

def pul_kiritish(x , language):
    """Bu kartdan yechilgan summani hamda balansdagi summani aytadi"""
    if language == 'uz':
        if check(x):
            result = data_card['balance'] - x * 1.01
            data_card['balance'] = result
            print(f"""
                Kartadan Yechildi: {x *1.01}
                Kartada Qolgan Pul: {result}
            """)
            return service_uz()
        else: 
            print()
            print(f"Xatolik, kartangizda mablag' yetarli emas !!! Kartezda {data_card['balance']}💲 mavjud")
            return get_money()

    elif language == 'ru':
        if check(x):
            result = data_card['balance'] - x * 1.01
            data_card['balance'] = result
            print(f"""
                Взятие деньги с карты: {x *1.01}
                Оставшиеся деньги: {result}
            """)
            return service_ru()
        else: 
            print()
            print(f"Ошибка, недостаточна деньги !!! Ваш баланс {data_card['balance']}💲")
            return get_money_ru()

    elif language == 'eng':
            if check(x):
                result = data_card['balance'] - x * 1.01
                data_card['balance'] = result
                print(f"""
                    Removed from your card: {x *1.01}
                    Balance in your card: {result}
                """)
                return service_eng()
            else: 
                print()
                print(f"Error, not enough money !!! Balance is {data_card['balance']}💲 ")
                return get_money_eng()
    


def get_money():
    """O'zbek tilida pul yechib olish"""
    global data_card
    def reply():
        """Ortga qaytish funksiyasi"""
        ty = input("""
        0. Orqaga qaytish
        back. Xizmatni tugatish
        >>>> """)
        if ty == "0":
            return get_money()

        elif ty == "back":
            return main()

        else:
            print("Error")
            return reply()
    ty = int(input("""
        1. 50 $
        2. 100 $
        3. 200 $
        4. 400 $
        5. 500 $
        6. Boshqa summa
        >>>"""))

    # pul yechish 
    if ty > data_card['balance']:
        print()
        print("Kartangizda💳 yetarli mablag' mavjud emas!")
        return reply()
        # 1
    if ty == 1:
        return pul_kiritish(50 , language='uz')

    elif ty == 2:
        return pul_kiritish(100 , language='uz')
    elif ty == 3:
        return pul_kiritish(200, language='uz')

    elif ty == 4:
        return pul_kiritish(400, language='uz')

    elif ty == 5:
        return pul_kiritish(500, language='uz')
    elif ty == 6:
        money = float(input("Pul miqdorini kiriting = "))
        if money > data_card['balance']:
            print("Kartangizda💳 yetarli mablag' mavjud emas!")
            pul_solish = input("""
                Kartangizga pul solasizmi ?
                    1. HA
                    2. YO'Q
            >>> """)
            if pul_solish == '1':
                return fill_card_uz()
            elif pul_solish == '2':
                return service_uz()
            else:
                return get_money() 
        return pul_kiritish(float(money),language='uz')
    else:
        return get_money()
        

# Sms xabarnoma. O'zbek tiliga
def phone_message():
    """Telefon raqamni kartaga ulash yoki raqamni o'zgartirish funksiyasi"""
    for x in data_card:
              
        # telefon raqami yo'q bolsa agar
        if data_card['phone_number'] == "":
            check_phoneNumber = input("""Kartangizga💳 nomeriz📞📲 ulanmagan!!! Ulashni📞 xoxlaysizmi ? 
                1. Ha ✅
                2. Yo'q (bitta ortga)
                3. Tilni tanlashga qaytish
            >>>""")
            if check_phoneNumber == '1':
                phone_number = (input("Telefon nomerizni kriting: "))
                if len(phone_number) == 9:
                    if phone_number != int or phone_number != float:
                        data_card['phone_number'] = int(phone_number )
                        print()
                        print(f"Kartangiz💳  telefon nomerga ulandi📞📲 . Sizning nomeriz +998{data_card['phone_number']}")
                        print()
                        return service_uz()
                    else:
                        print('Xatolik , nomer raqamdan iborat bo‘lishi kerak')
                        return phone_message()
                else:
                    print()
                    print("Telefon nomer 9 ta sondan iborat bo'lishi shart !!! Mobil operatoringizni ham yozishni unutmang !!!")
                    print()

                # shu yerdan nomerni 9ta raqamdan iboratligini tekshirish 
                    
            elif check_phoneNumber == '2':
                return service_uz()
            elif check_phoneNumber == '3':
                return main()
            else:
                print("Tepada👆 ko'rsatilgan sonlardan birini tanlang iltimos !!!")
                print()
                return service_uz()
        else:
            print("Sizda allaqachon telefon raqam ulangan !!!")
            print()
            rename_phone = input(""" Telefon raqamingizni o'zgartirishni xoxlaysizmi ?
                1. Ha
                2. Yo'q
            >>> """)
            if rename_phone == '1':
                data_card['phone_number'] = input("Yangi nomerizni kiriting : ")
                print(f"Nomeringiz muvaffaqqiyatli o'zgartirildi !!! Sizning tel nomeriz {data_card['phone_number']}")
                print()
            elif rename_phone == '2':
                return service_uz()
            else:
                print("Tepada ko'rsatilgan sonlardan birini kiriting. Ogoh bo'ling !!!")
                return service_uz()


# kartani toldirish funksiyasi

def fill_card_uz():
    amount_money_youwant = float(input("Nech pul to'ldirmoqchisiz  =  "))
    data_card['balance'] += amount_money_youwant
    print(f"Balansizga pul tushdi. Endi sizning balansingiz  {data_card['balance']}💲")
    return service_uz()

# o'zbek servisi
def service_uz():
    """O'zbek tili uchun maxsus servislar"""
    service = input(
        """
        Service turini tanglang:
            1. Karta Balansi 💳
            2. Pul yechish 💸
            3. SMS Xabarnoma ✍️
            4. Kartani to'ldirish 💰
            5. Pin-Kodni o'zgartirish 
            6. Exit 
        >>>>> """
    )
    if service == '1':
        return card_balance()
    elif service == '2':
        return get_money()
    elif service == '3':
        return phone_message()
    elif service == '4':
        return fill_card_uz()
    elif service == '5':
        return change_pin_uz()
    elif service == '6':
        return main()
    else:
        return service_uz()

def change_pin_uz():
    print()
    print(f"Hozirda sizning pin-kodingiz: {data_card['pin_card']}")
    print()
    change = input(""" 💳Kartangizni pin-kodini o'zgartirasizmi :
        1. HA
        2. YO'Q ( 1ta ortga )
    >>> """)
    if change == '1':
        new_pin = int(input('Yangi pin-kodni💳  kiriting : '))
        while True:
            check_new_pin = int(input('Yuqoridaki pin-kodi qaytadan kiriting : '))
            if new_pin != check_new_pin:
                print('Pin-kod noto`g`ri 💳❌. Pin kodingiz bir biri bilan bir xil emas!')
                return change_pin_uz()
            else:
                data_card['pin_card'] = check_new_pin
                print()
                print(f"Sizning pin-kodingiz muvaffaqqiyatli o'zgartirildi 👇 !!!")
                print(f"Sizning yangi pin kodiz : {data_card['pin_card']}")
                return service_uz()
    elif change == '2':
        return service_uz()
    else:
        print('Xatolik 🚫!!! Tepada ko\'rsatilgan sonlardan birini kiriting!')
        return change_pin_uz()


# o'zbek tili tanlandi
def uz():
    """O'zbek tili tanlandi"""
    print("Siz O'ZBEK tilini tanladingiz !!!")
    n = 5
    pin_code = int(input("Pin kodni kiriting: "))

    while n > 1 and pin_code != data_card['pin_card']:
        print(f"Pin kod xato ❌ >>> Qaytatdan kiriting sizda {n-1}ta urinish qoldi")
        pin_code = int(input("Pin kodni kiriting: "))
        if pin_code == data_card['pin_card']:
            return service_uz()
        n-=1
    if pin_code == data_card['pin_card']:
        return service_uz()

    print("Kartangiz blok bo'ldi. Qaytatdan RUN qiling !!!")
    print()
    return main()





# Rus tili menyusi
def ru():
    """Был выбран русский язык"""
    print("Вы выбрали РУССКОГО языка !!!")
    n = 5
    pin_code = int(input("Введите пин-код: "))

    while n > 1 and pin_code != data_card['pin_card']:
        print(f"Не правильный код ❌ >>> Введите код занова. У вас осталось {n-1} попыток")
        pin_code = int(input("Введите пин-код: "))
        if pin_code == data_card['pin_card']:
            return service_ru()
        n-=1
    if pin_code == data_card['pin_card']:
        return service_ru()

    print("Ваша карта заблокирована. Зделайте RUN занова !!!")
    print()
    return main()


# rus tilda pul toldirish
def fill_card_ru():
    amount_money_youwant = float(input("Сколько вы хотите пополнить ?  =  "))
    data_card['balance'] += amount_money_youwant
    print(f"Деньги упали на баланс. Теперь ваш баланс  {data_card['balance']}💲")
    return service_ru()
# rus tiili servisi
def service_ru():
    """Русские сервиси"""
    service = input(
        """
        Выберите тип услуги:
            1. Баланс карты 💳
            2. Снять деньги 💸
            3. СМС сообщения ✍️
            4. Заполнение карты 💰
            5. Изменить пин код карты 💳
            6. Возврат в главное меню 🏠
        >>>>> """
    )
    if service == '1':
        return card_balance_ru()
    elif service == '2':
        return get_money_ru()
    elif service == '3':
        return phone_message_ru()
    elif service == '4':
        return fill_card_ru()
    elif service == '5':
        return change_pin_ru()
    elif service == '6':
        return main()
    else:
        return service_eng()

def change_pin_ru():
    print()
    print(f"В настоящее время ваш пин-код: {data_card['pin_card']}")
    print()
    change = input(""" 💳 Меняете ли вы пин-код карты :
        1. ДА
        2. НЕТ (1 назад)
    >>> """)
    if change == '1':
        new_pin = int(input('Введите новый пин-код💳 : '))
        while True:
            check_new_pin = int(input('Повторно введите указанный выше PIN-код : '))
            if new_pin != check_new_pin:
                print('Пин-код неправильный 💳❌. Ваш пин-код не совпадает!')
                return change_pin_ru()
            else:
                data_card['pin_card'] = check_new_pin
                print()
                print(f"Ваш пин-код успешно изменен 👇!!!")
                print(f"Ваш пин код : {data_card['pin_card']}")
                return service_ru()
    elif change == "2":
        return service_ru()
    else:
        print("ВВедите 1 или 2 !!!")
        return change_pin_ru() 


def card_balance_ru():
    """Увидеть баланс карты"""
    print()
    print(f"Баланс на вашей 💳карты💳 {data_card['balance']}💲")
    print()
    print("Назад 👇")
    card_balance_back = input("""
        1. Назад на услуги
        2. Выбрать другой язык
    >>>>""")

    if card_balance_back == '1':
        return service_ru()
    elif card_balance_back == '2':
        return main()
    else:
        print('Нет такого числа!!!')
        return service_ru()
# pul yechish
def get_money_ru():
    """Вывод на русском языке"""
    def reply():
        """"orqaga qaytish funi"""
        ty = input("""
        0. Назад
        back. закончить
        >>>> """)
        if ty == "0":
            return get_money()

        elif ty == "back":
            return main()

        else:
            print("Error")
            return reply()
    ty = int(input("""
        1. 50 $
        2. 100 $
        3. 200 $
        4. 400 $
        5. 500 $
        6. Другая сумма
        >>>"""))

    # pul yechish boshlandi
    if ty > data_card['balance']:
        print("На вашей 💳карты💳 не достаточна деньги!")
        return reply()
        # 1
    if ty > data_card['balance']:
        print("Kartangizda💳 yetarli mablag' mavjud emas!")
        return reply()
        # 1
    if ty == 1:
        return pul_kiritish(50, language='ru')
    elif ty == 2:
        return pul_kiritish(100, language='ru')
    elif ty == 3:
        return pul_kiritish(200, language='ru')
    elif ty == 4:
        return pul_kiritish(400, language='ru')
    elif ty== 5:
        return pul_kiritish(500, language='ru')
    elif ty == 6:
        money = float(input("Напишите сумму денег = "))
        if money > data_card['balance']:
            print("На вашей карте 💳 недостаточно деньги!")
            pul_solish = input("""
                А вы хотите пополнить баланс ?
                    1. ДА
                    2. НЕТ
            """)
            if pul_solish == '1':
                return fill_card_ru()
            elif pul_solish == '2':
                return service_ru()
            return get_money()
        return pul_kiritish(float(money),language='ru')
    else:
        return get_money_ru()


# tel raqamini ulash 
def phone_message_ru():
    """Функция привязки номера телефона к карте или смены номера"""
    for x in data_card:
              
        # telefon raqami yo'q bolsa agar
        if data_card['phone_number'] == "":
            check_phoneNumber = input("""Ваш 💳  номер📞📲 не привязан к вашей карте!!! Хотите подключиться? 
                1. Да ✅
                2. Нет (1 раз назад)
                3. Вернуться к выбору языка
            >>>""")
            if check_phoneNumber == '1':
                phone_number = (input("Введите свой номер телефона📞📲 : "))
                if len(phone_number) == 9:
                    if phone_number != int:
                        data_card['phone_number'] = int(phone_number )
                        print(f"Ваша карта💳 успешнa привязана к номеру телефона📞📲 . Ваш номер +998{data_card['phone_number']}")
                        print()
                        back = input("""Назад :
                            1. Назад (1 раз)
                            2. Вернуться к выбору языка
                        >>> """)
                        if back == '1':
                            return service_ru()
                        elif back == '2':
                            return main()
                        else:
                            print("Напишите, пожалуйста, одну из цифр выше !!!")
                    else:
                        print('Ошибка, номер должно быть числом !!!')
                        return phone_message_ru()
                else:
                    print()
                    print("Номер телефона должен состоять из 9 символов!!!")
                    print()
                    return phone_message_ru()
                    
                    
            elif check_phoneNumber == '2':
                return service_ru()
            elif check_phoneNumber == '3':
                return main()
            else:
                print("Пожалуйста, выберите один из номеров, указанных выше👆!!!")
                print()
                print()
                return phone_message_ru()
        else:
            print("У вас уже есть номер телефона📞📲 подключен !!!")
            print()
            rename_phone = input(""" Вы хотите изменить свой номер телефона?
                1. ДА
                2. Нет
            >>> """)
            if rename_phone == '1':
                data_card['phone_number'] = input("Введите ваш новый номер : ")
                print(f"Ваш номер успешно изменен !!! Ваш телефон номер +998{data_card['phone_number']}")
                print()
                return service_ru()
            elif rename_phone == '2':
                return service_ru()
            else:
                print("Введите одно из чисел, указанных выше. Будьте в курсе!!!")
                return phone_message_ru()


# Ingliz tili menyusi
def eng():
    """English menu"""
    print("You have choosen English language !!!")
    n = 5
    pin_code = int(input("Enter your pin-code: "))

    while n > 1 and pin_code != data_card['pin_card']:
        print(f"Wron pin-code ❌ >>> Try once more. You have {n-1} attempts")
        pin_code = int(input("Enter your pin-code: "))
        if pin_code == data_card['pin_card']:
            return service_eng()
        n-=1
    if pin_code == data_card['pin_card']:
        return service_eng()

    print("Your card have blocked. Do RUN again !!!")
    print()
    return main()


# rus tiili servisi
def service_eng():
    """English language services"""
    """ingliz tili servislar"""
    service = input(
        """
        Select service type :
            1. Card Balance 💳
            2. Get money 💸
            3. SMS message ✍️
            4. Fill the card 💰
            5. Change pin-code
            6. Exit
        >>>>> """
    )
    if service == '1':
        return card_balance_eng()
    elif service == '2':
        return get_money_eng()
    elif service == '3':
        return phone_message_eng()
    elif service == '4':
        return fill_card_eng()
    elif service == '5':
        return change_pin_eng()
    elif service == '6':
        return main()
    else:
        return service_eng()

def change_pin_eng():
    print()
    print(f"Your pin-code : {data_card['pin_card']}")
    print()
    change = input(""" 💳 Do you change your card PIN code? :
        1. YES
        2. NO (1 step back)
    >>> """)
    if change == '1':
        new_pin = int(input('Enter your pin-code💳 : '))
        while True:
            check_new_pin = int(input('Re-enter the above PIN code : '))
            if new_pin != check_new_pin:
                print('The pin code is incorrect 💳❌. Your PIN code does not match!')
                return change_pin_eng()
            else:
                data_card['pin_card'] = check_new_pin
                print()
                print(f"Your pin code has been successfully changed 👇!!!")
                print(f"Now is your pin-code is : {data_card['pin_card']}")
                return service_eng()
    elif change == "2":
        return service_eng()
    else:
        print("Wrong command!! Please enter a correct number.")
        return change_pin_eng()

def card_balance_eng():
    """see your card balance"""
    print()
    print(f"Balance of your 💳card💳 {data_card['balance']}💲")
    print()
    print("Back 👇")
    card_balance_back = input("""
        1. Back to services
        2. Choose another language
    >>>>""")

    if card_balance_back == '1':
        return service_eng()
    elif card_balance_back == '2':
        return main()
    else:
        print('You have written wrong number!!!')
        return service_eng()
# pul yechish
def get_money_eng():
    """Remove money from you card"""
    def reply():
        """funksiyani qayta ishlatadi"""
        ty = input("""
        0. Back
        back. Exit.Over
        >>>> """)
        if ty == "0":
            return get_money()

        elif ty == "back":
            return main()

        else:
            print("Error")
            return reply()
    ty = int(input("""
        1. 50 $
        2. 100 $
        3. 200 $
        4. 400 $
        5. 500 $
        6. Another sum
        >>>"""))

    # pul yechish boshlandi
    if ty > data_card['balance']:
        print("There is not enough money on your 💳card💳!")
        # 1
    if ty > data_card['balance']:
        print("Kartangizda💳 yetarli mablag' mavjud emas!")
        return reply()
        # 1
    if ty == 1:
        return pul_kiritish(50, language='eng')

    elif ty == 2:
        return pul_kiritish(100, language='eng')
    elif ty == 3:
        return pul_kiritish(200, language='eng')

    elif ty == 4:
        return pul_kiritish(400, language='eng')

    elif ty== 5:
        return pul_kiritish(500, language='eng')
    elif ty == 6:
        money = float(input("Write amount of money = "))
        if money > data_card['balance']:
            print("Your card💳  does not have enough money !")
            pul_solish = input("""
                Do you want to fill your card ?
                    1. YES
                    2. NO
            """)
            if pul_solish == '1':
                return fill_card_ru()
            elif pul_solish == '2':
                return service_ru()
            else:
                print('Error')
                return service_eng()
        return pul_kiritish(float(money),language='ru')
    else:
        print('Wrong number! Try again...')
        print()
        return get_money_eng()

        # sms xabarnoma ulanganligini tekshirihs
def phone_message_eng():
    """Function of changing a private number to a phone using a card"""
    for x in data_card:
              
        # telefon raqami yo'q bolsa agar
        if data_card['phone_number'] == "":
            check_phoneNumber = input("""Your 💳 number📞📲 is not linked to your card!!! Want to connect?
                1. Yes ✅
                2. No (back 1 step)
                3. Return to language section
            >>> """)
            if check_phoneNumber == '1':
                phone_number = (input("Enter your phone number📞📲 : "))
                if len(phone_number) == 9:
                    if phone_number != int:
                        data_card['phone_number'] = int(phone_number )
                        print(f"Your card💳 is successfully linked to your phone number📞📲 . Your number is +998{data_card['phone_number']}")
                        print()
                        return service_eng()
                    else:
                        print('Error, number must be a number!!!')
                        return phone_message_eng()
                else:
                    print()
                    print('The length of the code should be 9 digits!!!')
                    print()
                    return phone_message_eng()
                    
                    
            elif check_phoneNumber == '2':
                return service_eng()
            elif check_phoneNumber == '3':
                return main()
            else:
                print("Please choose one of the numbers listed above👆!!!")
                print()
                print()
                return service_eng()
        else:
            print("You already have a phone number📞📲 connected!!!")
            print()
            rename_phone = input(""" Do you want to change your phone number?
                1. YES
                2. NO
            >>> """)
            if rename_phone == '1':
                data_card['phone_number'] = input("Enter your new number : ")
                print(f"Your number has been successfully changed !!! Your number is +998{data_card['phone_number']}")
                print()
                return service_eng()
            elif rename_phone == '2':
                return service_eng()
            else:
                print("Enter one of the numbers shown above. Stay up to date!!!")
                return service_eng()

def fill_card_eng():
    """Bu funksiya kartaga pul soladi"""
    amount_money_youwant = float(input("How much money you want to fill ?  =  "))
    data_card['balance'] += amount_money_youwant
    print(f"Money fell on balance. Now your balance is  {data_card['balance']}💲")
    return service_eng()


if __name__ == "__main__":
    main()