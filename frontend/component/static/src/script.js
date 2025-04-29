const micButton = document.getElementsByClassName('start-btn')[0];
const statusText = document.getElementsByClassName('status-text')[0];
const micButtonContent = document.getElementsByClassName('start-btn-content')[0];
const endPoint = 'http://localhost:9000/api/v1/rag/process'
let isListening = false;
let mediaRecorder;
let audioChunks = [];
const supportedMimeTypes = [
    'audio/mpeg',
    'audio/ogg;codecs=opus',
    'audio/mp4',
].filter(type => MediaRecorder.isTypeSupported(type));

micButton.addEventListener('click', async () => {
    try {
        if (!isListening) {
            const mimeType = supportedMimeTypes[0];
            console.log('Используемый формат:', mimeType);
            const stream = await navigator.mediaDevices.getUserMedia({
                audio: {
                    sampleRate: 16000,
                    channelCount: 1
                }
            });
            mediaRecorder = new MediaRecorder(stream, {
                mimeType: mimeType
            });

            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, {type: mimeType});
                const formData = new FormData();
                formData.append('audio', audioBlob, 'recording');

                try {
                    const response = await fetch(endPoint, {
                        method: 'POST', body: formData
                    });
                    if (!response.ok) throw new Error('Ошибка загрузки');
                    const wavBlob = await response.blob();
                    const wavUrl = URL.createObjectURL(wavBlob);
                    let player = document.getElementById('wav-player');
                    if (!player) {
                        player = document.createElement('audio');
                        player.id = 'wav-player';
                        player.controls = false;
                        player.style.display = "none";
                        document.body.appendChild(player);
                    }
                    player.src = wavUrl;
                    player.play();
                } catch (error) {
                    console.error('Ошибка:', error);
                    statusText.textContent = 'Ошибка соединения';
                }

                audioChunks = [];
            };
            mediaRecorder.start();
        } else {
            mediaRecorder.stop();
            const indicator = document.querySelector('.recording-indicator');
            if (indicator) indicator.remove();
        }
        isListening = !isListening;
        micButton.classList.toggle('pulse', isListening);
        statusText.textContent = isListening ? 'Слушаю...' : 'Обработка...';
        micButtonContent.textContent = isListening ? "" : "Начать";

    } catch (error) {
        console.error('Ошибка доступа к микрофону:', error);
        statusText.textContent = 'Доступ к микрофону запрещен';
    }
});
