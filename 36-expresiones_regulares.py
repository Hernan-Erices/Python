#re se usa para trabajar con expresiones regulares (existen mas) pero este es el mas comun
import re

# Lista de expresiones regulares con ejemplos y explicaciones:

# 1. Coincide con una dirección de correo electrónico
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_example = "example@example.com"
print(re.match(email_regex, email_example))  # Coincide con correos válidos

# 2. Coincide con un número de teléfono en formato (123) 456-7890
phone_regex = r'\(\d{3}\) \d{3}-\d{4}'
phone_example = "(123) 456-7890"
print(re.match(phone_regex, phone_example))  # Coincide con números de teléfono

# 3. Coincide con una fecha en formato DD/MM/YYYY
date_regex = r'\b\d{2}/\d{2}/\d{4}\b'
date_example = "25/12/2023"
print(re.match(date_regex, date_example))  # Coincide con fechas válidas

# 4. Coincide con una URL
url_regex = r'https?://(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_example = "https://www.example.com"
print(re.match(url_regex, url_example))  # Coincide con URLs válidas

# 5. Coincide con una dirección IP (IPv4)
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ip_example = "192.168.1.1"
print(re.match(ip_regex, ip_example))  # Coincide con direcciones IP válidas

# 6. Coincide con palabras que comienzan con una letra mayúscula
capital_word_regex = r'\b[A-Z][a-z]*\b'
capital_word_example = "Python"
print(re.match(capital_word_regex, capital_word_example))  # Coincide con palabras capitalizadas

# 7. Coincide con números enteros positivos o negativos
integer_regex = r'-?\d+'
integer_example = "-123"
print(re.match(integer_regex, integer_example))  # Coincide con números enteros

# 8. Coincide con códigos postales de 5 dígitos
zipcode_regex = r'\b\d{5}\b'
zipcode_example = "12345"
print(re.match(zipcode_regex, zipcode_example))  # Coincide con códigos postales

# 9. Coincide con contraseñas que tengan al menos 8 caracteres, incluyendo una letra mayúscula, una minúscula y un número
password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
password_example = "Password123"
print(re.match(password_regex, password_example))  # Coincide con contraseñas seguras

# 10. Coincide con etiquetas HTML simples
html_tag_regex = r'<([a-zA-Z]+)>(.*?)</\1>'
html_example = "<title>Example</title>"
print(re.match(html_tag_regex, html_example))  # Coincide con etiquetas HTML

# Ejemplo de uso de re.search:

# 1. Buscar una dirección de correo electrónico en un texto
email_text = "Mi correo es example@example.com para contacto."
print(re.search(email_regex, email_text))  # Encuentra el correo en el texto

# 2. Buscar un número de teléfono en un texto
phone_text = "Llámame al (123) 456-7890 cuando puedas."
print(re.search(phone_regex, phone_text))  # Encuentra el número de teléfono en el texto

# 3. Buscar una fecha en un texto
date_text = "La reunión es el 25/12/2023 en la oficina."
print(re.search(date_regex, date_text))  # Encuentra la fecha en el texto

# 4. Buscar una URL en un texto
url_text = "Visita nuestro sitio web en https://www.example.com para más información."
print(re.search(url_regex, url_text))  # Encuentra la URL en el texto

# 5. Buscar una dirección IP en un texto
ip_text = "El servidor está en la IP 192.168.1.1."
print(re.search(ip_regex, ip_text))  # Encuentra la dirección IP en el texto

# 6. Buscar palabras que comienzan con una letra mayúscula en un texto
capital_word_text = "Python es un lenguaje de programación."
print(re.search(capital_word_regex, capital_word_text))  # Encuentra la primera palabra capitalizada

# 7. Buscar números enteros positivos o negativos en un texto
integer_text = "El saldo es de -123 dólares."
print(re.search(integer_regex, integer_text))  # Encuentra el número entero en el texto

# 8. Buscar códigos postales de 5 dígitos en un texto
zipcode_text = "Mi código postal es 12345."
print(re.search(zipcode_regex, zipcode_text))  # Encuentra el código postal en el texto

# 9. Buscar contraseñas seguras en un texto
password_text = "La contraseña segura es Password123."
print(re.search(password_regex, password_text))  # Encuentra la contraseña en el texto

# 10. Buscar etiquetas HTML simples en un texto
html_text = "El título de la página es <title>Example</title>."
print(re.search(html_tag_regex, html_text))  # Encuentra la etiqueta HTML en el texto


# Ejemplo de uso de re.findall:
# 1. Encontrar todas las direcciones de correo electrónico en un texto
email_text = "Contacta a example@example.com o info@test.com para más información."
print(re.findall(email_regex, email_text))  # Encuentra todas las direcciones de correo

# 2. Encontrar todos los números de teléfono en un texto
phone_text = "Mis números son (123) 456-7890 y (987) 654-3210."
print(re.findall(phone_regex, phone_text))  # Encuentra todos los números de teléfono

# 3. Encontrar todas las fechas en un texto
date_text = "Las fechas importantes son 25/12/2023 y 01/01/2024."
print(re.findall(date_regex, date_text))  # Encuentra todas las fechas

# 4. Encontrar todas las URLs en un texto
url_text = "Visita https://www.example.com o http://test.org para más detalles."
print(re.findall(url_regex, url_text))  # Encuentra todas las URLs

# 5. Encontrar todas las direcciones IP en un texto
ip_text = "Las IPs del servidor son 192.168.1.1 y 10.0.0.1."
print(re.findall(ip_regex, ip_text))  # Encuentra todas las direcciones IP

# 6. Encontrar todas las palabras que comienzan con una letra mayúscula en un texto
capital_word_text = "Python y Java son lenguajes de programación populares."
print(re.findall(capital_word_regex, capital_word_text))  # Encuentra todas las palabras capitalizadas

# 7. Encontrar todos los números enteros positivos o negativos en un texto
integer_text = "Los valores son -123, 456 y 789."
print(re.findall(integer_regex, integer_text))  # Encuentra todos los números enteros

# 8. Encontrar todos los códigos postales de 5 dígitos en un texto
zipcode_text = "Los códigos postales son 12345 y 67890."
print(re.findall(zipcode_regex, zipcode_text))  # Encuentra todos los códigos postales

# 9. Encontrar todas las contraseñas seguras en un texto
password_text = "Las contraseñas seguras son Password123 y Secure456."
print(re.findall(password_regex, password_text))  # Encuentra todas las contraseñas seguras

# 10. Encontrar todas las etiquetas HTML simples en un texto
html_text = "El contenido incluye <title>Example</title> y <h1>Header</h1>."
print(re.findall(html_tag_regex, html_text))  # Encuentra todas las etiquetas HTML