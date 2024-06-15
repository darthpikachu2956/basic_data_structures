# Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Посчитал средний балл каждого ученика
aver_aaron = sum(grades[0]) / len(grades[0])
aver_bilbo = sum(grades[1]) / len(grades[1])
aver_johnny = sum(grades[2]) / len(grades[2])
aver_khendrik = sum(grades[3]) / len(grades[3])
aver_steve = sum(grades[4]) / len(grades[4])

# Перевёл множество в список, чтобы к нему далее можно было обращаться
students = list(students)
# создал пустой словарь, как было сказано в задании, а затем обновил его, взяв данные из "бывшего" множества
average = {}
average.update({students[4]: aver_aaron, students[1]: aver_bilbo, students[0]: aver_johnny,
                students[3]: aver_khendrik, students[2]: aver_steve})

# отсортировал имена учеников по алфавиту
students = sorted(students)
# объединил имена учеников с помощью zip(), создавая кортежи; затем снова преобразовал всё это в словарь.
# без этого значения выводились упорядоченно, а ключи нет, тем самым запутывая информацию о баллах учеников.
average = dict(zip(students, [aver_aaron, aver_bilbo, aver_johnny, aver_khendrik, aver_steve]))
print(average)
