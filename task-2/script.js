// Task 02: Stopwatch Engine & Lap Manager
document.addEventListener('DOMContentLoaded', () => {
  const timeDisplay = document.getElementById('timeDisplay');
  const msDisplay = document.getElementById('msDisplay');
  const startBtn = document.getElementById('startBtn');
  const lapBtn = document.getElementById('lapBtn');
  const resetBtn = document.getElementById('resetBtn');
  const lapsList = document.getElementById('lapsList');

  let startTime = 0;
  let elapsedTime = 0;
  let timerInterval = null;
  let isRunning = false;
  let laps = [];

  function formatTime(ms) {
    const mins = Math.floor(ms / 60000);
    const secs = Math.floor((ms % 60000) / 1000);
    const cs = Math.floor((ms % 1000) / 10);

    const pad = (n) => n.toString().padStart(2, '0');
    return {
      main: `${pad(mins)}:${pad(secs)}`,
      ms: `.${pad(cs)}`
    };
  }

  function updateDisplay() {
    const formatted = formatTime(elapsedTime);
    timeDisplay.textContent = formatted.main;
    msDisplay.textContent = formatted.ms;
  }

  function renderLaps() {
    lapsList.innerHTML = '';
    if (laps.length === 0) {
      lapsList.innerHTML = '<li class="empty-lap">No lap records yet</li>';
      return;
    }

    let minDur = Infinity;
    let maxDur = -1;

    if (laps.length > 1) {
      laps.forEach(l => {
        if (l.duration < minDur) minDur = l.duration;
        if (l.duration > maxDur) maxDur = l.duration;
      });
    }

    laps.slice().reverse().forEach(lap => {
      const li = document.createElement('li');
      li.className = 'lap-item';

      if (laps.length > 1) {
        if (lap.duration === minDur) li.classList.add('best');
        else if (lap.duration === maxDur) li.classList.add('worst');
      }

      const lapF = formatTime(lap.duration);
      const totalF = formatTime(lap.total);

      li.innerHTML = `
        <span>Lap ${lap.num}</span>
        <span>+${lapF.main}${lapF.ms}</span>
        <span>${totalF.main}${totalF.ms}</span>
      `;
      lapsList.appendChild(li);
    });
  }

  startBtn.addEventListener('click', () => {
    if (!isRunning) {
      isRunning = true;
      startTime = Date.now() - elapsedTime;
      timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        updateDisplay();
      }, 10);

      startBtn.textContent = 'Pause';
      startBtn.className = 'btn btn-pause';
      lapBtn.disabled = false;
    } else {
      isRunning = false;
      clearInterval(timerInterval);

      startBtn.textContent = 'Resume';
      startBtn.className = 'btn btn-start';
    }
  });

  lapBtn.addEventListener('click', () => {
    if (elapsedTime === 0) return;
    const prevTotal = laps.length > 0 ? laps[laps.length - 1].total : 0;
    const duration = elapsedTime - prevTotal;

    laps.push({
      num: laps.length + 1,
      duration: duration,
      total: elapsedTime
    });

    renderLaps();
  });

  resetBtn.addEventListener('click', () => {
    isRunning = false;
    clearInterval(timerInterval);
    elapsedTime = 0;
    laps = [];

    updateDisplay();
    renderLaps();

    startBtn.textContent = 'Start';
    startBtn.className = 'btn btn-start';
    lapBtn.disabled = true;
  });
});
