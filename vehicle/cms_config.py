from cms.app_base import CMSAppConfig

from .models import Car
from .views import car_detail_view

class _(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(Car, car_detail_view)]
