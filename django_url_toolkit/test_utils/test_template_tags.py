from __future__ import absolute_import, print_function, unicode_literals

from unittest import TestCase

from django.contrib.sites.models import Site
from django.template import Context, Template


class StaticAbsoluteTemplateTagTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.site, _created = Site.objects.get_or_create(pk=1)

    def test_rendered(self):
        context = Context({'title': 'my_title'})
        template_to_render = Template(
            '{% load template_tags_django_url_toolkit %}'
            '{% static_absolute title %}'
        )
        static_url = 'http://example.com/static/'
        rendered_template = template_to_render.render(context)
        self.assertEqual(static_url + 'my_title', rendered_template)

