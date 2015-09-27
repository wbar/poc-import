from django.db import models
from django.db import transaction
from .settings import THUNDERING_FRAME_WIDTH

import time


class ImportProcessManager(models.Manager):
    """
    Manager used to create import process and handling thundering herd problem.
    """
    def create_process(self):
        """
        Method used to create Process object.

        :return: None if already process created in thundering frame
        """
        thunder_frame_id = int(time.time() / THUNDERING_FRAME_WIDTH) * THUNDERING_FRAME_WIDTH
        with transaction.atomic():
            obj, created = self.get_or_create(thunder_id=thunder_frame_id)
        if created:
            from .tasks import start_import_process
            start_import_process.delay(obj.id)

        return obj if created else None
