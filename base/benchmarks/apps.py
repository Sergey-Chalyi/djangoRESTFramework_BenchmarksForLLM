from django.apps import AppConfig

from base import settings
from benchmarks.utils import load_test_data


class BenchmarksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'benchmarks'

    def ready(self):
        """
        This method is called when the application is ready to perform any initialization tasks.
        It checks if the DEBUG setting is enabled and, if so, attempts to load test data.
        If the DEBUG setting is disabled, it prints a message indicating that test data loading is skipped.

        Parameters:
        None

        Returns:
        None
        """
        if settings.DEBUG:
            try:
                load_test_data()
                print("Test data loaded successfully.")
            except FileNotFoundError as e:
                print(e)
        else:
            print("DEBUG is False. Test data loading skipped.")
