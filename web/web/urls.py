from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
     url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^blog/', include('zinnia.urls', namespace='blog')),
    url(r'^comments/', include('django_comments.urls')),
]
