from unittest import TestCase

from django.contrib.sites.models import Site
from django.template import Context, Template


class TemplateUrlToolkitTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.site, _created = Site.objects.update_or_create(
            pk=1, defaults={"domain": "www.mysite.com"}
        )

    def test_static_absolute(self):
        context = Context({})
        template_to_render = Template(
            "{% load url_toolkit %}" "{% static_absolute 'test/fb.png' %}"
        )
        rendered_template = template_to_render.render(context)
        self.assertEqual("http://www.mysite.com/static/test/fb.png", rendered_template)

    def test_prepend_site(self):
        context = Context({})
        template_to_render = Template(
            "{% load url_toolkit %}" "{{ '/test/fb.png'|prepend_site }}"
        )
        rendered_template = template_to_render.render(context)
        self.assertEqual("http://www.mysite.com/test/fb.png", rendered_template)
