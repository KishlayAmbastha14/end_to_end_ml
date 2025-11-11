document.getElementById('cropForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    console.log("🚀 Form intercepted by JS");

    const button = document.getElementById('predictButton');
    const buttonText = button.querySelector('.button-text');
    const buttonLoader = button.querySelector('.button-loader');
    const resultbox = document.getElementById('result');
    const resultContent = document.getElementById('resultContent');

    // --- 1. Show Loading State ---
    buttonText.style.display = 'none';
    buttonLoader.style.display = 'inline-block';
    button.disabled = true;
    resultbox.style.display = 'none';

    // --- 2. Collect Form Data ---
    const formData = {
        N: parseFloat(document.getElementById('N').value),
        P: parseFloat(document.getElementById('P').value),
        K: parseFloat(document.getElementById('K').value),
        temperature: parseFloat(document.getElementById('temperature').value),
        humidity: parseFloat(document.getElementById('humidity').value),
        ph: parseFloat(document.getElementById('ph').value),
        rainfall: parseFloat(document.getElementById('rainfall').value)
    };

    // Emojis for better display
    const cropEmojis = {
        'rice': '🌾', 'maize': '🌽', 'jute': '🌿', 'cotton': '☁️', 'coffee': '☕',
        'papaya': '🥭', 'orange': '🍊', 'apple': '🍎', 'watermelon': '🍉',
        'grapes': '🍇', 'mango': '🥭', 'banana': '🍌', 'pomegranate': '🍓',
        'lentil': '🌱', 'blackgram': '🌱', 'mungbean': '🌱', 'mothbeans': '🌱',
        'pigeonpeas': '🌱', 'kidneybeans': '🌱', 'chickpea': '🌱'
    };

    try {
        // --- 3. Make API Call ---
        const response = await  fetch('https://crop-recommendations-kj8m.onrender.com/predict',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(formData)
        });
        const result = await response.json();

        // --- 4. Handle Response ---
        if (response.ok) {
            const cropName = result.prediction_crop;
            const emoji = cropEmojis[cropName.toLowerCase()] || '🌱';
            resultContent.innerHTML = `
                <p class="text-2xl font-bold text-emerald-700 mb-2">${emoji} ${cropName}</p>
                <p class="text-gray-600">This crop is best suited for the provided conditions.</p>
            `;
        } else {
            resultContent.innerHTML = `
                <p class="text-red-700 font-semibold">Error: ${result.error || 'Server Error'}</p>
            `;
        }

        resultbox.style.display = 'block';
        resultbox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        console.error("Error:", error);
        resultContent.innerHTML = `
            <p class="text-red-700 font-semibold">Error: Unable to connect to the server.</p>
        `;
        resultbox.style.display = 'block';
    } finally {
        // --- 5. Reset Button ---
        button.disabled = false;
        buttonText.style.display = 'inline';
        buttonLoader.style.display = 'none';
    }
});
