from django.db import models
from .managers import ImportProcessManager


# Create your models here.
class ImportProcess(models.Model):
    thunder_id = models.PositiveIntegerField(
        verbose_name='Thundering frame id',
        unique=True,
        editable=False,
        default=0,
        help_text='This value is being calculated by Manager when creating task'
    )
    start_date = models.DateTimeField(auto_now_add=True)

    objects = ImportProcessManager()


class ImportProcessLog(models.Model):
    """
    Simple Log entry object.
    """
    class Level(object):
        DEBUG = 100
        INFO = 300
        WARNING = 500
        ERROR = 700

        @classmethod
        def to_choices(cls):
            return (
                (cls.DEBUG, 'DEBUG'),
                (cls.INFO, 'INFO'),
                (cls.WARNING, 'WARNING'),
                (cls.ERROR, 'ERROR'),
            )

    process = models.ForeignKey(ImportProcess)
    entry_date = models.DateTimeField(auto_now_add=True)
    level = models.PositiveSmallIntegerField(choices=Level.to_choices(), default=Level.INFO)
    message = models.TextField()



