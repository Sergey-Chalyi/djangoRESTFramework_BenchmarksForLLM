from django.apps import AppConfig

from base import settings
from benchmarks.utils import load_test_data


class BenchmarksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'benchmarks'

    def ready(self):
        if settings.DEBUG:
            try:
                load_test_data()
                print("Test data loaded successfully.")
            except FileNotFoundError as e:
                print(e)
        else:
            print("DEBUG is False. Test data loading skipped.")
