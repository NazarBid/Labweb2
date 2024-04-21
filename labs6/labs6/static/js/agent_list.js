function fetchAgents(){
    fetch('/agents/', {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const agentList = document.getElementById("agentList");
        agentList.innerHTML = '';
        data.agents.forEach(agent => {
            const listItem = document.createElement('li');
            const detailsLink = document.createElement('a');
            detailsLink.href = `/agents/${agent.id}/`;
            detailsLink.textContent = 'Details';
            detailsLink.classList.add('buttonEnterClasses');
            listItem.innerHTML = `${agent.first_name} ${agent.last_name} `;
            listItem.appendChild(detailsLink);
            agentList.appendChild(listItem);
            agentList.appendChild(document.createElement('br'));
        });
    });
};



// Main event listener
document.addEventListener('DOMContentLoaded', () => {
    fetchAgents();
});