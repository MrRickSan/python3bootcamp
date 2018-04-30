from random import choice
# We can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f"{laugh} {person}"

    return get_laugh

laugh_at = make_laugh_at_func("Linda")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())