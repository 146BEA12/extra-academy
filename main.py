print("Здравсвтуйте, заполните пожалйста анкету:) ")
first_name = input("Пожалуйста ведите ваше имя: ")
second_name = input("Пожалуйста ведите вашу фамилию: ")
birth_year = input("Пожалуйста ведите ваш год рождения: ")
question_1 = input("Вы гражданин Казахстана? ")
question_2 = input("Семейное положение? ")

full_name = first_name + " " + second_name

age = 2023 - int(birth_year)

print("Ваши данные: ")
print("Ваше полное ФИО: ", full_name)
print("Ваш возраст: ", age)
print("Ваш ответ на первый вопрос: ", question_1)
print("Ваш ответ на второй вопрос: ", question_2)