from random import randint
# from string import digits
from faker import Faker


def rand_ratio():
    return randint(840, 950), randint(473, 573)


fake = Faker('pt-BR')


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=8),
        'descripition': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'serving': fake.random_number(digits=2, fix_len=True),
        'serving_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        },
        'category': fake.word(),
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


# if__name__ == '__main__':
#     from pprint import pprint
#     pprint(make_recipe())
