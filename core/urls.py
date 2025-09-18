from django.contrib import admin
from django.urls import path
from vege.views import receipe, update_receipe, delete_receipe
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("delete-receipe/<id>/", delete_receipe, name="delete_receipe"),
    path("update-receipe/<id>/", update_receipe, name="update_receipe"),

    # Root shows recipes page
    path("", receipe, name="receipes"),
    path("home/", receipe, name="receipes"),
    # Home page separate
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
