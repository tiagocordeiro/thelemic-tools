from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from .views import resh_hours_list


# Create your tests here.
class IndexViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()

    def test_resh_list_view(self):
        request = self.factory.get('/resh/hours')

        response = resh_hours_list(request)
        self.assertEqual(response.status_code, 200)

    def test_content_in_resh_list(self):
        response = self.client.get(reverse('resh_hours_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nascer do sol')
