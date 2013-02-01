from auto_print.views import UploadPDFView
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    url(r'^upload_pdf/$', UploadPDFView.as_view(), name='pdf_upload'),
    url(r'^print_success/$', TemplateView.as_view(template_name='print_success.html'), name='print_success'),
    # url(r'^$', 'auto_print.views.home', name='home'),
    # url(r'^auto_print/', include('auto_print.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
