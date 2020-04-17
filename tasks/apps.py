from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        """
        Импортируем сигналы на момент загрузки приложения
        """
        import tasks.signals
