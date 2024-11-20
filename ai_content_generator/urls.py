from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls', namespace='content')),
    path('chat/', include('drm_chat.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('stackflow/', include('questionflow.urls', namespace='questionflow')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
     path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
