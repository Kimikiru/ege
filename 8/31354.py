from itertools import product
letters = sorted("СОЛНЦЕ")

last_index = 0

for index, comb in enumerate(product(letters, repeat=6), start=1):
    word = ''.join(comb)



    if index % 2 == 0:
        continue
    if word[0] in "ЦН":
        continue
    if word.count("Ц") != 1 or word.count("Н") != 1:
        continue

    last_index = index

print(last_index)






"""
Все шестибуквенные слова, составленные из букв С, О, Л, Н, Ц, Е, записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1. EEEEEE
2. ЕЕЕЕЕЛ
3. ЕЕЕЕЕН
4. EEEEEO
5. EEEEEC
6. ЕЕЕЕЕЦ
Определите, под каким номером в этом списке стоит последнее слово с нечётным номером, которое не начинается с букв Ц или Н и при этом содержит в своей записи ровно одну букву Ц и ровно одну букву Н.
Примечание. Слово - последовательность идущих подряд букв, не обязательно осмысленная.
"""