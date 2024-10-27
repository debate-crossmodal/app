document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('votacao-form');
    form.addEventListener('submit', handleVoteSubmission);
});

async function handleVoteSubmission(event) {
    event.preventDefault(); // Previne o comportamento padrão do formulário

    const formData = new FormData(event.target);
    const voto = formData.get('candidato'); // Captura o voto do usuário

    try {
        const response = await fetch('/api/votar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ voto: voto }),
        });

        if (response.ok) {
            alert('Seu voto foi enviado com sucesso!');
            // Limpa o formulário após a submissão
            document.getElementById('votacao-form').reset();
        } else {
            alert('Houve um erro ao enviar seu voto. Tente novamente.');
        }
    } catch (error) {
        console.error('Erro ao enviar o voto:', error);
        alert('Erro de rede. Verifique sua conexão e tente novamente.');
    }
}