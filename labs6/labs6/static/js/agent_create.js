function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('agentForm');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const form = document.getElementById('agentForm');
    const formData = new FormData(form);

    fetch('/agents/create/', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        window.location.href = '/agents/';
    })
    .catch(error => {
        console.error('Error:', error);
    });
    });
});