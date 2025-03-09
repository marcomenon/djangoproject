# Usa un'immagine Python leggera
FROM python:3.12-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia i file di dipendenze
COPY pyproject.toml poetry.lock ./

# Installa dipendenze con uv
RUN pip install --no-cache-dir uv && uv pip install --system --upgrade pip && uv sync

# Copia il codice del progetto
COPY . .

# Espone la porta 8000 per Django
EXPOSE 8000

# Comando di avvio con Gunicorn
CMD ["gunicorn", "-c", "gunicorn.conf.py", "core.wsgi:application"]
