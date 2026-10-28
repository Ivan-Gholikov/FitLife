user_name = input("Добрый день, как Вас зовут? ")
user_age = int(input("Сколько Вам лет? "))
user_weight = float(input("Какой у Вас вес в кг? "))
# Теперь запрашиваем сразу в метрах
user_height_m = float(input("Какой у вас рост в метрах? "))

bmi = user_weight / (user_height_m ** 2)

water_ml = user_weight * 30
water_l = water_ml / 1000

print(f"Отчёт для пользователя: {user_name}, возраст: {user_age}")
print(f"Твой индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчёт окончен. Будьте здоровы!")