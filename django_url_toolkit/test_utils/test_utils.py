from __future__ import absolute_import, print_function, unicode_literals
from unittest import TestCase

from django.contrib.sites.models import Site
from django_url_toolkit.utils import make_absolute_url, get_current_site_absolute, append_querystring


class UtilsTest(TestCase):

    def setUp(self):
        super().setUp()
        self.site, _created = Site.objects.get_or_create(pk=1)

    def test_make_absolute_url(self):
        with self.subTest("test_make_absolute_url_with_absolute_path"):
            url = 'http://test.com'
            self.assertEqual(make_absolute_url(url), url)

        with self.subTest("test_make_absolute_url_without_absolute_path_and_is_secure"):
            url = '/test/'
            secure = True
            self.assertEqual(make_absolute_url(url, secure), 'https://' + str(self.site) + url)

        with self.subTest("test_make_absolute_url_without_absolute_path_and_not_secure"):
            url = '/test/'
            secure = False
            self.assertEqual(make_absolute_url(url, secure), 'http://' + str(self.site) + url)

        with self.subTest("test_make_absolute_url_without_absolute_path_and_none_secure"):
            url = '/test/'
            secure = None
            self.assertEqual(make_absolute_url(url, secure), 'http://' + str(self.site) + url)

    def test_get_current_site_absolute(self):
        with self.subTest("test_get_current_site_absolute_without_request_and_secure_false"):
            self.assertEqual(get_current_site_absolute(), 'http://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_without_request_and_secure_true"):
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"):
            if '://' in self.site.domain:
                self.site.domain = self.site.domain.split('://')[1]
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"):
            if '://' in self.site.domain:
                self.site.domain = self.site.domain.split('://')[1]
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"):
            if '://' in self.site.domain:
                self.site.domain = self.site.domain.split('://')[1]
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"):
            self.site.domain = self.site.domain + '/'
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site)[:-1])
            self.site.domain = str(self.site.domain)[:-1]

        with self.subTest("test_get_current_site_absolute_with_request"):
            from django.test.client import RequestFactory
            request = RequestFactory().request()
            self.assertEqual(request.is_secure(), False)
            self.assertEqual(get_current_site_absolute(request, secure=True), 'http://' + str(self.site))

        with self.subTest("test_get_current_site_absolute_with_slash_at_end"):
            self.site.domain = self.site.domain + '/'
            self.assertEqual(get_current_site_absolute(secure=True), 'https://' + str(self.site)[:-1])
            self.site.domain = str(self.site.domain)[:-1]

    def test_append_querystring(self):
        with self.subTest("test_append_querystring_without_next_url"):
            self.assertEqual(append_querystring(None, key=0), None)

        with self.subTest("test_append_querystring_with_next_url"):
            self.assertEqual(append_querystring('test', key=0), "test?key=0")

        with self.subTest("test_append_querystring_with_next_url_no_kwargs"):
            self.assertEqual(append_querystring('test'), "test")

        with self.subTest("test_append_querystring_next_url_with_?"):
            self.assertEqual(append_querystring('test?', key=0), "test?&key=0")

        with self.subTest("test_append_querystring_next_url_with_multiple_args"):
            self.assertEqual(append_querystring('test', key=0, key1=1, key2=2), "test?key=0&key1=1&key2=2")

        with self.subTest("test_append_querystring_next_url_with_multiple_args"):
            self.assertEqual(append_querystring('test?key3=3', key=0, key1=1, key2=2), "test?key3=3&key=0&key1=1&key2=2")


