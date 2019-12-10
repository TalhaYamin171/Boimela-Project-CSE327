from django.test import SimpleTestCase
from django.urls import reverse, resolve
from boimelawebApp.views import home, latest, navigation, StallListView, StallDetailView, StallCreateView, StallUpdateView, StallDeleteView

# Unit Tests for site urls


class HomeTest(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('boimelaApp-home')
        self.assertEquals(resolve(url).func, home)


class NavigationTest(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('boimelaApp-navigation')
        self.assertEquals(resolve(url).func, navigation)
