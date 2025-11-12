from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Car


class CarSubMenu(CMSAttachMenu):
    name = "Car sub-menu"

    def get_nodes(self, request):
        nodes = []
        for car in Car.objects.all():
            node = NavigationNode(
                car.name,
                car.absolute_url(),
                car.id
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(CarSubMenu)
