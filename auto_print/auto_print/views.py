
from auto_print.auto_print.forms import UploadPDFForm
from django.conf import settings
from django.views.generic import FormView
import os



class UploadPDFView(FormView):

    form_class = UploadPDFForm
    template_name = 'upload_form.html'
    success_url = '/print_success/'

    def form_valid(self, form):
        printer = form.save()
        printer.print_file()
        return super(UploadPDFView, self).form_valid(form)

