from django.contrib import messages
from django.views.generic import TemplateView, RedirectView
from .models import ImportProcess


class IndexView(TemplateView):
    template_name = 'importing/index.html'


class ImportProcessView(RedirectView):
    permanent = False
    pattern_name = 'importing:index'

    def get(self, request, *args, **kwargs):
        obj = ImportProcess.objects.create_process()
        if obj:
            messages.add_message(request, messages.INFO, 'Import process were send!')
        else:
            messages.add_message(request, messages.WARNING, 'Import process were skipped due thundering limitations.')
        return super().get(request, *args, **kwargs)

