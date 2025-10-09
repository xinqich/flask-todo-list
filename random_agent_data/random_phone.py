import random

def random_phone():
    d = [str(random.randrange(10)) for _ in range(10)]
    return '+7' + ''.join(d)