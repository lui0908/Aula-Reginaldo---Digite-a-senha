
import unittest
from senha import contar_caracteres


class TestCalculadora(unittest.TestCase):

    def test_senha(self):
        self.assertEqual(contar_caracteres("oi"), 2)

