from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Axolote Guimaraes',
            'email': 'guixoxoloti@gmail.com',
            'assunto': 'Alimentação melhor',
            'mensagem': 'lembre-se de arrumar algumas minhocas vivas para mim comer'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Axolote Guimaraes',
            'email': 'guixoxoloti@gmail.com'
        }
        requests = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(requests.status_code, 200)
