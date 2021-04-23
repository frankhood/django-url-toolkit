from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import StaticNode

from django_url_toolkit.utils import make_absolute_url

register = template.Library()


@register.filter
def prepend_site(value):
    return make_absolute_url(value)


class StaticFilesAbsoluteNode(StaticNode):

    def url(self, context):
        path = self.path.resolve(context)
        static_url = static(path)
        return make_absolute_url(static_url)


@register.tag('static_absolute')
def do_static_absolute(parser, token):
    return StaticFilesAbsoluteNode.handle_token(parser, token)
