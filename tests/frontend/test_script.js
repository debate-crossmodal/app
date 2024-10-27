document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("votacaoForm");
    const submitButton = document.getElementById("submitBtn");
    const feedbackMessage = document.getElementById("feedbackMessage");

    // Evento de envio do formulário
    form.addEventListener("submit", function(event) {
        event.preventDefault();  // Impede o envio padrão do formulário

        // Coleta os dados do formulário
        const formData = new FormData(form);
        const votos = [];
        
        // Validação dos dados
        for (let [key, value] of formData.entries()) {
            if (!value) {
                feedbackMessage.textContent = "Por favor, preencha todas as preferências.";
                feedbackMessage.style.color = "red";
                return;
            }
            votos.push(value);
        }

        // Envio dos dados para o backend
        fetch('/processar_votacao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ votos: votos })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao enviar os votos.');
            }
            return response.json();
        })
        .then(data => {
            feedbackMessage.textContent = "Votos enviados com sucesso! Resultados: " + JSON.stringify(data);
            feedbackMessage.style.color = "green";
        })
        .catch(error => {
            feedbackMessage.textContent = "Erro: " + error.message;
            feedbackMessage.style.color = "red";
        });
    });
});