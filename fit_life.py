WAT_ML = 30
WAT_L = 1000

user_name = input("Добрый день, как Вас зовут? ")
user_age = int(input("Сколько Вам лет? "))
user_weight = float(
    input("Какой у Вас вес в кг? ").replace(" ", "").replace(",", "."))
user_height_m = float(
    input("Какой у вас рост в метрах? ").replace(" ", "").replace(",", "."))

bmi = user_weight / (user_height_m ** 2)

water_ml = user_weight * WAT_ML
water_l = water_ml / WAT_L

print(
    f"Отчёт для пользователя: {user_name}, возраст: {user_age}\n"
    f"Твой индекс массы тела: {bmi:.1f}\n"
    f"Рекомендуемая норма воды: {water_l:.1f} л в день\n"
    f"Расчёт окончен. Будьте здоровы!"
)
