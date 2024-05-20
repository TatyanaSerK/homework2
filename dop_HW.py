grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

new_grades = []                      #создаем список для записи средней оценки
for i in grades:                     #высчитываем среднее
    sred = sum(i) / len(i)
    new_grades.append(sred)          #записываем значение в список

result_dict = {}                     #новый словарь для конечного результата
sort_student = sorted(students)      #сортируем студентов по алфавиту (будет список)

for i in range(len(sort_student)):   #объединяем полученные списки в словарь
    result_dict[sort_student[i]] = new_grades[i]

print(result_dict)




