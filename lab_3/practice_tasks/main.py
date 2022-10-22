from jinja2 import Template, Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("template.html")
