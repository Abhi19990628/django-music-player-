from django.contrib import admin # type: ignore
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Music_player.urls'))
]
