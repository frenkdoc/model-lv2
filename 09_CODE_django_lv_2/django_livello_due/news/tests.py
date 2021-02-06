from django.http import response
from django.test import TestCase
from django.urls import resolve, reverse
from news.views import home
from news.models import Giornalista
# Create your tests here.

# test sulla nostra funzione views "home" (news.home)
class homeViewTests(TestCase):
    """ una prima serie di test per verificare la corretta implementazione dela funzione home """

    def test_url_resolves_home_viws(self):
        view = resolve("/")
        self.assertEquals(view.func, home)


    def test_home_view_url_by_name(self):
        url = reverse("homeviews")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class GiornalistaTestCase(TestCase):

    def setUp(self):
        Giornalista.objects.create(nome="Guido", cognome="Van Rossum")
        

    def test_giornalista_str(self):
        giornalista = Giornalista.objects.get(nome="Guido")
        self.assertEquals(giornalista.__str__(), "Guido Van Rossum")