from django.contrib.sites.models import Site
from django.test import TestCase, override_settings

from url_toolkit import utils


class UtilsTest(TestCase):
    def setUp(self):
        super().setUp()
        self.site, _created = Site.objects.get_or_create(pk=1)

    def test_make_absolute_url(self):
        with self.subTest("test_make_absolute_url_with_absolute_path"):
            url = "http://test.com"
            self.assertEqual(utils.make_absolute_url(url), url)

        with self.subTest("test_make_absolute_url_without_absolute_path_and_is_secure"):
            url = "/test/"
            secure = True
            self.assertEqual(
                utils.make_absolute_url(url, secure), "https://" + str(self.site) + url
            )

        with self.subTest(
            "test_make_absolute_url_without_absolute_path_and_not_secure"
        ):
            url = "/test/"
            secure = False
            self.assertEqual(
                utils.make_absolute_url(url, secure), "http://" + str(self.site) + url
            )

        with self.subTest(
            "test_make_absolute_url_without_absolute_path_and_none_secure"
        ):
            url = "/test/"
            secure = None
            self.assertEqual(
                utils.make_absolute_url(url, secure), "http://" + str(self.site) + url
            )

    @override_settings(SITE_BASE_URL="https://exemple.com/")
    def test_make_absolute_url_with_SITE_BASE_URL(self):
        with self.subTest(
            "test_make_absolute_url_without_absolute_path_and_none_secure"
        ):
            url = "/test/"
            secure = None
            self.assertEqual(
                utils.make_absolute_url(url, secure), "https://exemple.com" + url
            )

    def test_get_current_site_absolute(self):
        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_false"
        ):
            self.assertEqual(
                utils.get_current_site_absolute(), "http://" + str(self.site)
            )

        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_true"
        ):
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site),
            )

        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"
        ):
            if "://" in self.site.domain:
                self.site.domain = self.site.domain.split("://")[1]
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site),
            )

        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"
        ):
            if "://" in self.site.domain:
                self.site.domain = self.site.domain.split("://")[1]
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site),
            )

        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"
        ):
            if "://" in self.site.domain:
                self.site.domain = self.site.domain.split("://")[1]
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site),
            )

        with self.subTest(
            "test_get_current_site_absolute_without_request_and_secure_true_and_not_absolute_path_in_site"
        ):
            self.site.domain = self.site.domain + "/"
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site)[:-1],
            )
            self.site.domain = str(self.site.domain)[:-1]

        with self.subTest("test_get_current_site_absolute_with_request"):
            from django.test.client import RequestFactory

            request = RequestFactory().request()
            self.assertEqual(request.is_secure(), False)
            self.assertEqual(
                utils.get_current_site_absolute(request, secure=True),
                "http://" + str(self.site),
            )

        with self.subTest("test_get_current_site_absolute_with_slash_at_end"):
            self.site.domain = self.site.domain + "/"
            self.assertEqual(
                utils.get_current_site_absolute(secure=True),
                "https://" + str(self.site)[:-1],
            )
            self.site.domain = str(self.site.domain)[:-1]

    def test_append_querystring(self):
        with self.subTest("test_append_querystring_without_next_url"):
            self.assertEqual(utils.append_querystring(None, key=0), None)

        with self.subTest("test_append_querystring_with_next_url"):
            self.assertEqual(utils.append_querystring("test", key=0), "test?key=0")

        with self.subTest("test_append_querystring_with_next_url_no_kwargs"):
            self.assertEqual(utils.append_querystring("test"), "test")

        with self.subTest("test_append_querystring_next_url_with_?"):
            self.assertEqual(utils.append_querystring("test?", key=0), "test?&key=0")

        with self.subTest("test_append_querystring_next_url_with_multiple_args"):
            self.assertEqual(
                utils.append_querystring("test", key=0, key1=1, key2=2),
                "test?key=0&key1=1&key2=2",
            )

        with self.subTest("test_append_querystring_next_url_with_multiple_args"):
            self.assertEqual(
                utils.append_querystring("test?key3=3", key=0, key1=1, key2=2),
                "test?key3=3&key=0&key1=1&key2=2",
            )
