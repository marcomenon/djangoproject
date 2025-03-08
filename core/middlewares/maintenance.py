from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import ipaddress

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se DEBUG=False, mostra il sito normalmente
        if not settings.DEBUG:
            return self.get_response(request)

        # Se MAINTENANCE_MODE è disattivato, mostra il sito normalmente
        if not settings.MAINTENANCE_MODE:
            return self.get_response(request)

        host = request.get_host().split(':')[0]
        ip_address = request.META.get('REMOTE_ADDR', '')

        # Controlla se l'host è consentito
        if host in settings.ALLOWED_MAINTENANCE_HOSTS:
            return self.get_response(request)

        # Controlla se l'IP è tra quelli autorizzati
        if ip_address in settings.ALLOWED_MAINTENANCE_IPS:
            return self.get_response(request)

        # Altrimenti, mostra la pagina di manutenzione
        return render(request, "maintenance.html", status=503)
