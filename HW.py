# Запитуємо розмір кави

coffee_size = input("Choose a coffee size (S, M, L): ").upper()

# Розшифровуємо повну назву розміру кави

if coffee_size == "S":
    full_name = "Small"
elif coffee_size == "M":
    full_name = "Medium"
elif coffee_size == "L":
    full_name = "Large"
else:
    full_name = "Unknown size"

# Запитуємо про побажання щодо цукру і перетворюємо інформацію в "з/без цукру"

sugar = input("Do you want sugar? (yes/no)").lower()
sugar_text = "with sugar" if sugar == "yes" else "without sugar"

# Виводимо замовлення

print(f"You ordered a {full_name} coffee {sugar_text}.")
