from django.core.management.base import BaseCommand
from importing.models import ImportProcess


class Command(BaseCommand):
    help = 'Creates import process from external system'

    def handle(self, *args, **options):
        obj = ImportProcess.objects.create_process()
        if obj:
            self.stdout.write('Process created.')
        else:
            self.stdout.write('Process creation skipped thought thundering limitation')
