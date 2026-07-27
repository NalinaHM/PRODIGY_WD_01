// Task 05: Live Weather API & Fallback Engine
document.addEventListener('DOMContentLoaded', () => {
  const cityInput = document.getElementById('cityInput');
  const searchBtn = document.getElementById('searchBtn');
  const cityName = document.getElementById('cityName');
  const currentDate = document.getElementById('currentDate');
  const temp = document.getElementById('temp');
  const desc = document.getElementById('desc');
  const weatherIcon = document.getElementById('weatherIcon');
  const humidity = document.getElementById('humidity');
  const wind = document.getElementById('wind');
  const pressure = document.getElementById('pressure');
  const uv = document.getElementById('uv');
  const forecastGrid = document.getElementById('forecastGrid');

  const mockData = {
    'London': { temp: 18, desc: 'Light Rain', icon: '🌧️', humidity: '82%', wind: '14 km/h', pressure: '1012 hPa', uv: '3 (Low)' },
    'New York': { temp: 24, desc: 'Partly Cloudy', icon: '⛅', humidity: '55%', wind: '10 km/h', pressure: '1018 hPa', uv: '6 (Moderate)' },
    'Tokyo': { temp: 28, desc: 'Sunny', icon: '☀️', humidity: '60%', wind: '8 km/h', pressure: '1009 hPa', uv: '8 (High)' },
    'Paris': { temp: 21, desc: 'Clear Sky', icon: '🌤️', humidity: '48%', wind: '12 km/h', pressure: '1015 hPa', uv: '5 (Moderate)' }
  };

  function getDayName(offset) {
    const d = new Date();
    d.setDate(d.getDate() + offset);
    return d.toLocaleDateString('en-US', { weekday: 'short' });
  }

  async function search(city) {
    if (!city.trim()) return;
    cityName.textContent = `Searching ${city}...`;

    try {
      const apiKey = 'bd5e378503939ddaee76f12ad7a97608';
      const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&units=metric&appid=${apiKey}`);
      if (res.ok) {
        const data = await res.json();
        renderReal(data);
        return;
      }
    } catch (e) {
      console.log('Fallback active');
    }

    const key = Object.keys(mockData).find(k => k.toLowerCase() === city.toLowerCase()) || 'London';
    renderMock(city, mockData[key]);
  }

  function renderReal(data) {
    cityName.textContent = `${data.name}, ${data.sys.country}`;
    currentDate.textContent = new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
    temp.textContent = `${Math.round(data.main.temp)}°C`;
    desc.textContent = data.weather[0].description;
    weatherIcon.textContent = getEmoji(data.weather[0].icon);
    humidity.textContent = `${data.main.humidity}%`;
    wind.textContent = `${Math.round(data.wind.speed * 3.6)} km/h`;
    pressure.textContent = `${data.main.pressure} hPa`;
    uv.textContent = '5 (Moderate)';
    renderForecast(data.main.temp);
  }

  function renderMock(c, mock) {
    cityName.textContent = c.charAt(0).toUpperCase() + c.slice(1);
    currentDate.textContent = new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
    temp.textContent = `${mock.temp}°C`;
    desc.textContent = mock.desc;
    weatherIcon.textContent = mock.icon;
    humidity.textContent = mock.humidity;
    wind.textContent = mock.wind;
    pressure.textContent = mock.pressure;
    uv.textContent = mock.uv;
    renderForecast(mock.temp);
  }

  function getEmoji(code) {
    if (code.includes('01')) return '☀️';
    if (code.includes('02') || code.includes('03')) return '⛅';
    if (code.includes('09') || code.includes('10')) return '🌧️';
    if (code.includes('11')) return '⛈️';
    return '🌤️';
  }

  function renderForecast(baseTemp) {
    forecastGrid.innerHTML = '';
    const icons = ['☀️', '⛅', '🌧️', '🌤️', '⛈️'];

    for (let i = 1; i <= 5; i++) {
      const t = baseTemp + Math.sin(i) * 3;
      const el = document.createElement('div');
      el.className = 'forecast-item';
      el.innerHTML = `
        <div class="f-day">${getDayName(i)}</div>
        <div class="f-icon">${icons[i % icons.length]}</div>
        <div class="f-temp">${Math.round(t)}°C</div>
      `;
      forecastGrid.appendChild(el);
    }
  }

  searchBtn.addEventListener('click', () => search(cityInput.value || 'London'));
  cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') search(cityInput.value || 'London');
  });

  search('London');
});
