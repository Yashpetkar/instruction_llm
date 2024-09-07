document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const input = document.getElementById('imageInput');
    const statusDiv = document.getElementById('status');
    const descriptionsDiv = document.getElementById('descriptions');

    statusDiv.innerText = '';
    descriptionsDiv.innerHTML = '';

    if (input.files.length < 1 || input.files.length > 4) {
        statusDiv.innerText = 'Please upload between 1 to 4 PNG files.';
        return;
    }

    const formData = new FormData();
    for (let i = 0; i < input.files.length; i++) {
        formData.append('images', input.files[i]);
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();

        if (response.ok) {
            result.descriptions.forEach((desc, idx) => {
                const para = document.createElement('p');
                para.textContent = `Image ${idx + 1}: ${desc}`;
                descriptionsDiv.appendChild(para);
            });
        } else {
            statusDiv.innerText = result.error || 'Error uploading images.';
        }
    } catch (error) {
        statusDiv.innerText = 'Error: ' + error.message;
    }
});
