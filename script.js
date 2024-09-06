async function downloadVideo() {
    const videoLink = document.getElementById('video-link').value;
    
    if (!videoLink) {
        alert('Please paste a video link!');
        return;
    }

    const response = await fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ link: videoLink })
    });

    const data = await response.json();

    if (response.ok) {
        alert(data.message);
        // Optionally, you can start downloading the video file automatically:
        // window.location.href = `/path/to/downloaded/video/${data.filename}`;
    } else {
        alert('Error: ' + data.error);
    }
}

