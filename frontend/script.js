let chart;

document.getElementById('input-form').addEventListener('submit', async(e) => {
    e.preventDefault();
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('results').classList.add('hidden');

    const hour = parseInt(document.getElementById('hour').value);
    const day = parseInt(document.getElementById('day').value);
    const temp = parseFloat(document.getElementById('temp').value);
    const humidity = parseFloat(document.getElementById('humidity').value);

    try {
        const response = await fetch('http://127.0.0.1:8000/api/get_insights', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ hour, day_of_week: day, temperature: temp, humidity })
        });

        if (!response.ok) {
            const errText = await response.text();
            throw new Error(`Server error ${response.status}: ${errText || 'Check backend terminal'}`);
        }

        const data = await response.json();

        document.getElementById('predicted-value').textContent = `Predicted Usage: ${data.predicted_usage.toFixed(2)} kWh`;
        document.getElementById('recommendation').textContent = data.recommendation || 'Maintain current settings.';
        document.getElementById('explanation').textContent = data.explanation || 'No detailed explanation available.';

        const base = data.predicted_usage;
        const ctx = document.getElementById('energy-chart').getContext('2d');
        if (chart) chart.destroy();
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['-2h', '-1h', 'Now', '+1h', '+2h'],
                datasets: [{
                    label: 'Energy (kWh)',
                    data: [base - 4, base - 2, base, base + 1.5, base + 3],
                    borderColor: '#34d399',
                    backgroundColor: 'rgba(52, 211, 153, 0.3)',
                    tension: 0.4,
                    fill: true,
                    pointBackgroundColor: '#fff'
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { labels: { color: '#d1fae5' } } },
                scales: { x: { grid: { color: 'rgba(255,255,255,0.1)' } }, y: { grid: { color: 'rgba(255,255,255,0.1)' }, beginAtZero: false } }
            }
        });

        document.getElementById('results').classList.remove('hidden');
    } catch (err) {
        alert('❌ Connection Error: ' + err.message + '\n\nMake sure:\n1. Backend is running (uvicorn app:app --reload)\n2. No firewall blocking port 8000\n3. Check browser console for details');
        console.error(err);
    } finally {
        document.getElementById('loading').classList.add('hidden');
    }
});