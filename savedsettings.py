def load(name):
    file = open(f'{name}.sdss', 'r')
    file = file.read()
    return file

def save(name, val):
    file = open(f'{name}.sdss', 'w')
    file.write(val)

