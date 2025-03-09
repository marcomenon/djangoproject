document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = document.documentElement.getAttribute('data-theme');
    if (savedTheme) {
      // Facoltativo: Puoi sincronizzare localStorage con il valore server-side
      localStorage.setItem('theme', savedTheme);
    }
  });

  function changeTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    // Se l'utente è loggato, invia una richiesta al server per salvare il tema
    fetch('/update_theme', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ theme: theme })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
  }