from django.test import SimpleTestCase
from django.urls import reverse, resolve
from boimelawebApp.views import home, latest, navigation, StallListView, StallDetailView, StallCreateView, StallUpdateView, StallDeleteView

# Unit Tests for site urls


class HomeTest(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('boimelaApp-home')
        self.assertEquals(resolve(url).func, home)


class NavigationTest(SimpleTestCase):
    def test_navigation_url_is_resolved(self):
        url = reverse('boimelaApp-navigation')
        self.assertEquals(resolve(url).func, navigation)

class LatestbookTest(SimpleTestCase):
    def test_latestbook_url_is_resolved(self):
        url = reverse('boimelawebApp-latest')
        self.assertEquals(resolve(url).func, latest)

class StallListViewTest(SimpleTestCase):
    def test_stalllist_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, StallListView)

class StallDetailViewTest(SimpleTestCase):
    def test_stalldetail_url_is_resolved(self):
        url = reverse('stall-detail')
        self.assertEquals(resolve(url).func.view_class, StallDetailView)

class StallCreateViewTest(SimpleTestCase):
    def test_stallcreate_url_is_resolved(self):
        url = reverse('stall-create')
        self.assertEquals(resolve(url).func.view_class, StallCreateView)

class StallUpdateViewTest(SimpleTestCase):
    def test_stallupdate_url_is_resolved(self):
        url = reverse('stall-update')
        self.assertEquals(resolve(url).func.view_class, StallUpdateView)

class SearchTest(SimpleTestCase):
    def test_search_url_is_resolved(self):
        url = reverse('boimelawebApp-search')
        self.assertEquals(resolve(url).func, searchposts)
