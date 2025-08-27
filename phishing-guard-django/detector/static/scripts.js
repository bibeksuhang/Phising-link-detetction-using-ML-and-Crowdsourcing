document.addEventListener('DOMContentLoaded', function() {
    const predictForm = document.getElementById("predictForm");
    const resultBox = document.getElementById("resultBox");
    const feedbackForm = document.getElementById("feedbackForm");
    const feedbackUrl = document.getElementById("feedbackUrl");

    // Handle prediction form submission
    predictForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const url = document.getElementById("urlInput").value;
        resultBox.innerHTML = "🔄 Checking...";
        feedbackForm.style.display = "none";

        fetch(predictForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "url=" + encodeURIComponent(url)
        })
        .then(res => res.json())
        .then(data => {
            if (data.prediction) {
                const isPhishing = data.prediction === 'bad';
                resultBox.innerHTML = `<span class="${isPhishing ? 'phishing' : 'safe'}">
                    ${isPhishing ? '🚨 Phishing URL Detected' : '✅ This URL looks Safe'}
                </span>`;
                feedbackUrl.value = url;
                feedbackForm.style.display = "block";
            } else {
                resultBox.innerHTML = `❌ Error: ${data.error}`;
            }
        })
        .catch(error => {
            resultBox.innerHTML = `❌ Error: ${error.message}`;
        });
    });

    // Handle feedback form submission
    feedbackForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const url = feedbackUrl.value;
        const label = e.submitter.value;

        fetch(feedbackForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `url=${encodeURIComponent(url)}&label=${label}`
        })
        .then(res => res.json())
        .then(data => {
            resultBox.innerHTML += `<br>💾 ${data.message}`;
            feedbackForm.style.display = "none";
        })
        .catch(error => {
            resultBox.innerHTML += `<br>❌ Feedback error: ${error.message}`;
        });
    });
});