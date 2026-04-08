document.getElementById('serve-btn').addEventListener('click', async () => {
    const codeInput = document.getElementById('code-input').value;
    const chatWindow = document.getElementById('chat-window');

    if (!codeInput) {
        alert("Enter some code first, donkey!");
        return;
    }

    // Add User Message to UI
    chatWindow.innerHTML += `<div class="message user">${codeInput}</div>`;
    
    try {
        const response = await fetch('/review', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: codeInput })
        });

        const data = await response.json();

        // Add Gordon's Response to UI
        chatWindow.innerHTML += `<div class="message bot">${data.reply}</div>`;
        
        // Auto-scroll to bottom
        chatWindow.scrollTop = chatWindow.scrollHeight;

    } catch (error) {
        console.error("Error:", error);
    }
});