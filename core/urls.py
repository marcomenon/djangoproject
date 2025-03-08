from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from allauth.account.decorators import secure_admin_login
from django.views.generic import TemplateView

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    # Se è attiva la modalità manutenzione in ambiente DEBUG,
    # impostiamo la root per mostrare la pagina maintenance.html
    if getattr(settings, 'MAINTENANCE_MODE', False):
        urlpatterns += [
            path('', TemplateView.as_view(template_name='maintenance.html'), name='maintenance'),
        ]
    else:
        # Altrimenti, usa il tuo URL principale (sostituisci 'your_app.urls' con il percorso corretto)
        urlpatterns += [
            #path('', include('your_app.urls')),
        ]
    
    # Aggiungi il percorso per l'admin e il debug toolbar in ambiente DEBUG
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In produzione il middleware gestisce eventuali pagine di manutenzione
    urlpatterns += [
        #path('', include('your_app.urls')),   Assicurati di sostituire 'your_app.urls' con i tuoi URL principali
    ]

