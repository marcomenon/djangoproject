import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120  # Timeout delle richieste
accesslog = "-"  # Log di accesso in stdout
errorlog = "-"   # Log di errore in stdout
loglevel = "info"
