from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Nice', 'Fancy', 'Cool', 'Brand-New', 'Impressive',
              'Super-Awesome', 'Shiny', 'Portable', 'Improved', 'Pretty']
NOUNS = ['Anvil', 'Catapult', 'Fly-Swatter', 'JUUL', 'TV', 'Toilet Paper',
         'Hose', 'Mousetrap', 'Costume', 'Suprise-Item']


def generate_products():
    products = []
    for i in range(30):
        name = '{} {}'.format(sample(ADJECTIVES, k=1)[0],
                              sample(NOUNS, k=1)[0])
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = float('{0:.2f}'.format(uniform(0.0, 2.5)))
        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)
        products.append(prod)
    return products


def inventory_report(products):
    prod_names = [prod.name for prod in products]
    print("Unique Product names: ", len(set(prod_names)))

    avg_price = sum([prod.price for prod in products]) / len(products)
    avg_weight = sum([prod.weight for prod in products]) / len(products)
    avg_flammability = sum(
        [prod.flammability for prod in products]) / len(products)

    print(f"Average price: ${avg_price:.2f}")
    print(f"Average weight: {avg_weight:.1f} lbs")
    print(f"Average flammability: {avg_flammability:.2f}")

if __name__ == '__main__':
    inventory_report(generate_products())
