from admin_tools.menu.menus import *
from django.apps.config import AppConfig


class AdminToolsMenuConfig(AppConfig):
    """ Admin tools menu app configuration """
    name = 'admin_tools.menu'
    label = 'admin_tools_menu'

    def ready(self):
        """ Actions when django's app registry is ready """
        pass

