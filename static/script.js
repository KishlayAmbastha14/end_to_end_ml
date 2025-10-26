document.getElementById('cropForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get UI elements
    const button = document.getElementById('predictButton');
    const buttonText = button.querySelector('.button-text');
    const buttonLoader = button.querySelector('.button-loader');
    const resultElement = document.getElementById('result');

    // --- 1. Show Loading State ---
    buttonText.textContent = 'Predicting...';
    buttonLoader.style.display = 'inline-block';
    button.disabled = true;
    resultElement.style.display = 'none'; // Hide previous result

    // --- 2. Prepare Form Data ---
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        // Ensure values are sent as numbers
        data[key] = parseFloat(value); 
    });

    // Emojis for a nicer result display
    const cropEmojis = {
        'rice': '🌾', 'maize': '🌽', 'jute': '🌿', 'cotton': '☁️', 'coffee': '☕', 
        'papaya': '🥭', 'orange': '🍊', 'apple': '🍎', 'watermelon': '🍉',
        'grapes': '🍇', 'mango': '🥭', 'banana': '🍌', 'pomegranate': '🍓',
        'lentil': '🌱', 'blackgram': '🌱', 'mungbean': '🌱', 'mothbeans': '🌱',
        'pigeonpeas': '🌱', 'kidneybeans': '🌱', 'chickpea': '🌱'
    };

    try {
        // --- 3. Make API Call ---
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            // Handle HTTP errors (e.g., 404, 500)
            throw new Error(`Network response was not ok (${response.status})`);
        }

        const result = await response.json();
        
        // --- 4. Display Success Result ---
        // Assuming your API returns: { "prediction_crop": "Rice" }
        const cropName = result.prediction_crop;
        
        // Find emoji (case-insensitive)
        const emoji = cropEmojis[cropName.toLowerCase()] || '🌱'; 
        
        resultElement.innerHTML = `<h3>Recommended Crop: ${emoji} ${cropName}</h3>`;
        resultElement.style.display = 'block'; // Show the result box

    } catch (error) {
        // --- 5. Display Error Result ---
        console.error("Error:", error);
        resultElement.innerHTML = `<h3>Error: Could not get prediction.</h3><p>${error.message}</p>`;
        resultElement.style.display = 'block';
    
    } finally {
        // --- 6. Reset Button State (always runs) ---
        buttonText.textContent = 'Predict Crop';
        buttonLoader.style.display = 'none';
        button.disabled = false;
    }
});