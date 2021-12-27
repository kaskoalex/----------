print('Напишите слово, которое нужно угадать')
hidden_word = input()
# академия

print('Напишите вопрос, ответом на который является загаданное слово')
question = input()
# вызшее учебное заведение

user_word_number_letters = len(hidden_word) * "*"

print('Укажите количество попыток')
number = int(input())


def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]

    return new_user_word

user_char_number = [""]
flag = 0
while True:

    secret_word = hidden_word
    user_word = user_word_number_letters
    print(question)
    print('Угадываемое слово: ', user_word)

    while user_word != secret_word:

        print('У вас осталось ', (number-flag), ' попыток. Введите букву.')
        S = input()
        user_char = S.lower()
        flag = flag + 1

        for i in range(len(user_char_number)):
            
            if user_char_number[i] == user_char:
                print("Вы уже задавали эту букву, задайте другую")
                flag = flag - 1
                break            
            
        user_char_number.append(user_char)



        if len(user_char) != 1:
            continue
        if ord(user_char) < 1040 or ord(user_char) > 1103:
            print('Вводите пожалуйста буквы русского алфавита.')
            flag -= 1
            continue
        if flag >= number:
            print('Ваше количество попыток использовано, начинаем с начала!')
            continue

        new_user_word = update_user_word(secret_word, user_word, user_char)

        if user_word == new_user_word:

            print('К сожалению такой буквы нет в слове.')
        else:

            print('Поздравляем, такая буква есть в слове.')

        user_word = new_user_word
        print(user_word)

    print('Ура, вы угадали слово!')
    flag=0
    continue