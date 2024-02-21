import importlib

from django.core.signals import setting_changed
from django.dispatch import receiver

from tests import settings as test_settings


@receiver(setting_changed)
def app_settings_reload_handler(**kwargs):
    if kwargs["setting"] in [
        "SITE_BASE_URL",
    ]:
        importlib.reload(test_settings)
