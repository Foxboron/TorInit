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
        ipaddress.ip_address(val)
        return val
    except Exception as e:
        if ":" in val:
            try:
                # Would probably be better if we just checked
                # the lenght?
                ip, port = val.split(":")
                int(port)
                ipaddress.ip_address(ip)
                return val
            except: raise e
        else:
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



def get_input(inn=None, type=None):
    stdin = input("Give me a %s: " % str(inn))
    try:
        ret = _type[type](stdin)
        return ret
    except Exception as e:
        print(e)
        print("Nope sorry, wrong type")



print('''Make neat menu!''')
print("Available templates")
print("".join(load.list_templates()))


_out_map = {}

for i in variables:
    if i in list(options.keys()):
        v = get_input(inn=i, type=options[i]["type"])
        _out_map[i] = v


template = env.get_template('torrc.example')
print(template.render(**_out_map))




