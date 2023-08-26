# - якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
#
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"


while True :
    user_input = input('Enter Age: ')
    if user_input.isdigit():
        int_user_input = int(user_input)
        if '7' in str(int_user_input):
            print("Вам пощастить!")
        elif int_user_input <= 6:
            print("Де твої батьки?")
        elif int_user_input <= 16:
            print("Це фільм для дорослих!")
        elif int_user_input >= 65:
            print("Покажіть пенсійне посвідчення!")
        else:
            print("А білетів вже немає!")
        break
    else:
        print("Error!")