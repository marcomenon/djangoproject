from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Funzione modalità manutenzione
def is_maintenance_mode():
    return not settings.DEBUG and getattr(settings, 'MAINTENANCE_MODE', False)

# Accesso all'admin con autenticazione sicura (Allauth)
from allauth.account.decorators import secure_admin_login
admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

# URL principali
main_urlpatterns = [
    # path('', include('your_app.urls')),  # <-- Sostituisci con il nome della tua app principale
]

urlpatterns = [
    path('accounts/', include('allauth.urls')),
]

# Se il sito è in modalità manutenzione e NON è in DEBUG, mostra solo la pagina di manutenzione
if is_maintenance_mode():
    urlpatterns += [
        path('', TemplateView.as_view(template_name='maintenance.html'), name='maintenance'),
    ]
else:
    urlpatterns += main_urlpatterns

# Configurazione in modalità DEBUG
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    # Aggiunta gestione file statici e media in DEBUG
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
