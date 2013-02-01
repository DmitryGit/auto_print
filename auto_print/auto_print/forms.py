from auto_print.auto_print.models import Printer
from django import forms


class UploadPDFForm(forms.ModelForm):
#    pdf_file = forms.FileField(label='Upload file')
    class Meta:
        model = Printer