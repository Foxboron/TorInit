from jinja2 import Environment, FileSystemLoader, meta
import yaml
try:
    import ipaddress
except ImportError:
    import ipaddr as ipaddress


load = FileSystemLoader('./templates')

env = Environment(loader=load)

template = env.loader.get_source(env, "torrc.example")


variables = meta.find_undeclared_variables(env.parse(template))
options = yaml.load(open("options.yaml", "r").read())

def check_ip(val):
    try:
        if len(val.split(":")) == 2:
            ip, port = val.split(":")
            int(port)
        else:
            ip = val
        ipaddress.ip_address(ip)
        return val
    except Exception as e:
        raise e


def check_policy(val):
    """Make sub-menu to input several
       policy lines. Join them together
       to form the output"""
    pass


def hash_function(val):
    """Not sure how this can be done safe"""
    pass


_type = {"string": str,
         "integer": int,
         "ip": check_ip,
         "policy":  check_policy,
         "password": hash_function}


def get_input(inn=None, type=None, option=None):
    if option.get("message"):
        print(option["message"], end="")
    stdin = input("Give me a %s: " % str(inn))
    try:
        ret = _type[type](stdin)
        return ret
    except Exception as e:
        print(e)
        print("Nope sorry, wrong type")

def main():
    print('''Make neat menu!''')
    print("Available templates:\n")
    print("".join(load.list_templates()))
    print("")

    _out_map = {}

    for i in variables:
        if i in list(options.keys()):
            v = get_input(inn=i, option=options[i], type=options[i]["type"])
            _out_map[i] = v


    template = env.get_template('torrc.example')
    print("\n\n---------------")
    print(template.render(**_out_map))

def choose_options(l):
    options = dict(enumerate(l, start=1))
    print("\n".join("{0}) {1}".format(*i) for i in options.items()))
    inn = input("Select a template: ")
    if int(inn) in list(options.keys()):
        return options[int(inn)]
    else:
        print("Not an valid option!")

print(choose_options(["options1", "options"]))


