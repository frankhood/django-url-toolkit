# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def append_querystring(next_url: str, **kwargs):
    """
    Append passed couple of key,value as querystring to next_url address given
    Ex. append_querystring("game/?t=47326443",**{'next_url':'/registration/',session_id="43276832"})
    """
    if next_url:
        kwargs = kwargs or {}
        for key, value in kwargs.items():
            if not next_url.find('?') == -1:
                next_url = "%s&%s=%s" % (next_url, key, value)
            else:
                next_url = "%s?%s=%s" % (next_url, key, value)
    return next_url


def get_current_site_absolute(request=None, secure: bool = False):
    from django.contrib.sites.models import Site
    from django.contrib.sites.shortcuts import get_current_site
    from django.conf import settings

    if request:
        current_site = get_current_site(request)
        current_schema = 'https' if request.is_secure() else 'http'
    else:
        current_site = Site.objects.get_current()
        current_schema = 'https' if secure else 'http'
    absolute_domain = getattr(settings, "SITE_BASE_URL", None)
    if absolute_domain is None:
        absolute_domain = current_site.domain

    if '://' not in absolute_domain:
        absolute_domain = '{schema}://{domain}'.format(
            schema=current_schema,
            domain=absolute_domain,
        )
    if absolute_domain[-1] == '/':
        absolute_domain = absolute_domain[:-1]
    return absolute_domain


def make_absolute_url(url: str, secure: bool = None):
    if '://' in url:
        return url
    if secure is None:
        from django.conf import settings
        secure = getattr(settings, 'IS_HTTPS', False)
    current_domain = get_current_site_absolute(secure=secure)
    return current_domain + url
