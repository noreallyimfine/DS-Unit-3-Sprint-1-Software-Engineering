import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product(self):
        """Test default product price being 10"""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        self.assertEqual(prod.explode(), '...boom!')

    def test_custom_product(self):
        """Test custom product attributes and methods"""
        prod = Product("Test2 Product", price=50, weight=25, flammability=2.5)
        self.assertEqual(prod.price, 50)
        self.assertEqual(prod.weight, 25)
        self.assertEqual(prod.flammability, 2.5)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!')


class AcmeReportTest(unittest.TestCase):
    """Making sure Acme reports are accurate!"""
    def test_default_num_products(self):
        """Test generate products actually generates 30 products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test all generated names are legal names"""
        prod_names = [prod.name for prod in generate_products()]
        for prod in prod_names:
            splt = prod.split()
            self.assertIn(splt[0], ADJECTIVES)
            self.assertIn(splt[1], NOUNS)

if __name__ == '__main__':
    unittest.main()
