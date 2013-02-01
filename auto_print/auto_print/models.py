from django.conf import settings
from django.db import models
from django.utils.encoding import smart_str
import os


class Printer(models.Model):
    file = models.FileField('Upload file', upload_to='uploads/')

    def print_file(self):
        file_path = os.path.abspath(self.file.name)
        command = 'lp -o media="a4" -o sides=one-sided -d %s %s' % (settings.PRINTER_NAME, file_path)
        print "Runing command:",  command
        command = smart_str(command)
        os.system(command)