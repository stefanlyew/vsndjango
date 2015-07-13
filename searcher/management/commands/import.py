from django.core.management.base import BaseCommand, CommandError
from searcher.models import VSNDataParser

class Command(BaseCommand):
    help = 'Imports Vehicle Records from CSV'

    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        parser = VSNDataParser(settings.STATICFILES_DIRS + '/vsn_data.csv')
        parser.parse()
