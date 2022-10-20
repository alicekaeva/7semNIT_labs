from jinja2 import Template


def add_spaces(text):
    return " ".join(text)


def writing(n):
    if n == 1 or n % 10 == 1:
        return 'дисциплина'
    elif n == 2 or n % 10 == 2 or n == 3 or n % 10 == 3 or n == 4 or n % 10 == 4:
        return 'дисциплины'
    else:
        return 'дисциплин'


f_template = open('ind_test_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
student = [
    ["Алина", "Бизнес-информатика", ["Базы данных", "Программирование", "Статистика"], "ж", "38.03.05"],
    ["Вадим", "Экономика", ["Информатика", "Теория игр", "Статистика", "Экономика", "Эконометрика"], "м", "38.03.01"],
    ["Ксения", "Экономика", ["Информатика", "Теория игр", "Статистика"], "ж", "38.03.01"]
]
template.globals['add_spaces'] = add_spaces
template.globals['writing'] = writing
result_html = template.render(user=student[1], n=len(student[1][2]), add_spaces=add_spaces, writing=writing)
f = open('test.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
