from admin_tools.dashboard.dashboards import *
from admin_tools.dashboard.registry import *
from django.apps.config import AppConfig


class AdminToolsDashboardConfig(AppConfig):
    """ Admin tools dashboard app configuration """
    name = 'admin_tools_dashboard'
    label = 'admin_tools.dashboard'

    def ready(self):
        """ Actions when django's app registry is ready """
        pass

