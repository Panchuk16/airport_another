from werkzeug.security import generate_password_hash

# Введите пароль, который вы хотите проверить
password = "your_password_here"
password_hash = generate_password_hash(password)

# Выведет длину сгенерированного хеша
print(len(password_hash))