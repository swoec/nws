"""nws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from nw import views as nw_view
admin.autodiscover()


urlpatterns = [
    #url(r'^$',nw_view.index),#pay attention to this version
    url(r'^$',nw_view.home1,name='home'),
    url(r'^add/(\d+)/(\d+)/$',nw_view.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$',nw_view.add2,name='add2'),
    url(r'^home/$',nw_view.indexs1,name='index2'),
    url(r'^sum/$',nw_view.indexsum,name='sum'),
    url(r'^summ/$',nw_view.summ,name='summ'),
    url(r'^admin/', admin.site.urls),
]
