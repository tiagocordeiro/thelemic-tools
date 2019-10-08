from django.test import TestCase, Client, RequestFactory

from .views import index


# Create your tests here.
class IndexViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/')

        response = index(request)
        self.assertEqual(response.status_code, 200)
