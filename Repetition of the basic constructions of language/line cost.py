# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести стоимость aстроки.

# text = input()
# cost = len(text) * 60
# rub = cost // 100
# coin = cost % 100
# print(f"{rub} р. {coin} коп.")


text = input()
price = len(text) * 60
print(price// 100, 'р.', price%100, 'коп.')

# string = input()
# price = 60 * len(string)
# print(f'{price // 100} р. {price % 100} коп.')