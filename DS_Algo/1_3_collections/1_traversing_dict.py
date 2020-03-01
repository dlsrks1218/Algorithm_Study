d = dict(c = '!', b = 'world', a = 'hello')
for key in sorted(d.keys()):
    print(key, d[key])


def hello():
    print('hello')

def world():
    print('world')



action = 'h'

functions = dict(h=hello, w=world)
functions[action]()