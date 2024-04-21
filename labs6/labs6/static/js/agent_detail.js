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


const deleteAgentButton = document.getElementById("deleteAgentButton");
deleteAgentButton.addEventListener("click", () => {
  e.preventDefault();
  const agentId =  agent.id ;
  const singleAgentUrl = `/agents/${agentId}/`;
  deleteAgent(singleAgentUrl);
});

function deleteAgent(url) {
  fetch(url, {
    method: "DELETE",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    window.location.href = '/agents/';
  });
}


