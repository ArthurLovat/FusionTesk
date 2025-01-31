from django.test import TestCase

def add_num(num):
    return num + 1

class SimplesTestCase(TestCase):

    #roda toda vez
    def setUp(self):
        self.numero = 41

    #testa a unidade do codigo
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)
