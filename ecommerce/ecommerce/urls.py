ccccccco.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact/",views.homepage),
    path("",views.homepage),
    path("product/",views.product),
]

