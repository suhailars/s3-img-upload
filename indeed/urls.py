from django.views.generic.base import TemplateView
from files.views import FilePolicyAPI, FileUploadCompleteHandler
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='upload.html'), name='upload-home'),
    url(r'^api/files/policy/$', FilePolicyAPI.as_view(), name='upload-policy'),
    url(r'^api/files/complete/$', FileUploadCompleteHandler.as_view(), name='upload-complete'),
]