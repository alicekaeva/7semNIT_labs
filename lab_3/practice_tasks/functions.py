from jinja2 import Template
import matplotlib.pyplot as plt


def f_x(x, n_var):
    if n_var == 0:
        return x ** 3 - 6 * x ** 2 + x + 5
    elif n_var == 1:
        return x ** 2 - 5 * x + 1
    elif n_var == 2:
        return 1 / (x ** 2 + 1)


def create_pict(x, y):
    line = plt.plot(x, y)
    plt.setp(line, color="blue", linewidth=2)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("pict.jpg")
    return "pict.jpg"


n_var = 1
list_f = ["f(x)", "y(x)", "z(x)"]

a = -2
b = 6
n = 30
h = (abs(a) + abs(b)) / n
x_list = [a + (i * h) for i in range(n + 1)]
f_list = [f_x(x, n_var) for x in x_list]

name_pict = create_pict(x_list, f_list)

f_template = open('functions_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
template.globals["len"] = len
template.globals["round"] = round
f = open('functions.html', 'w', encoding='utf-8-sig')
result_html = template.render(x=x_list, y=f_list, pict=name_pict, n_var=n_var, list_f=list_f, a=a, b=b, n=n)
f.write(result_html)
f.close()
