from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./templates'))

template = env.get_template('torrc.example')


print(template.render(nickname="Test"))

