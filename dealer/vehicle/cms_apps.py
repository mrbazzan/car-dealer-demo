from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .models import Car


@apphook_pool.register
class CarApp(CMSApp):
    name = "Car"
    _urls = ["vehicle.urls",]
    app_name = "vehicle"
