/* ==========================================================================
   TASK-02: STOPWATCH ENGINE & LAP MANAGER
   ========================================================================== */

export function initStopwatch() {
  const display = document.getElementById('stopwatchDisplay');
  const msDisplay = document.getElementById('stopwatchMsDisplay');
  const startBtn = document.getElementById('stopwatchStartBtn');
  const lapBtn = document.getElementById('stopwatchLapBtn');
  const resetBtn = document.getElementById('stopwatchResetBtn');
  const lapList = document.getElementById('lapList');

  if (!display || !startBtn) return;

  let startTime = 0;
  let elapsedTime = 0;
  let timerInterval = null;
  let isRunning = false;
  let laps = [];

  // Format time into MM:SS:CC (Centiseconds)
  const formatTime = (timeInMs) => {
    const minutes = Math.floor(timeInMs / 60000);
    const seconds = Math.floor((timeInMs % 60000) / 1000);
    const centiseconds = Math.floor((timeInMs % 1000) / 10);

    const pad = (num) => num.toString().padStart(2, '0');
    return {
      main: `${pad(minutes)}:${pad(seconds)}`,
      ms: `.${pad(centiseconds)}`
    };
  };

  const updateDisplay = () => {
    const formatted = formatTime(elapsedTime);
    display.textContent = formatted.main;
    if (msDisplay) msDisplay.textContent = formatted.ms;
  };

  const renderLaps = () => {
    if (!lapList) return;
    lapList.innerHTML = '';

    if (laps.length === 0) {
      lapList.innerHTML = `<li class="lap-item" style="justify-content: center; color: var(--text-dim);">No laps recorded yet</li>`;
      return;
    }

    // Identify fastest and slowest lap (if > 1 lap)
    let minTime = Infinity;
    let maxTime = -1;

    if (laps.length > 1) {
      laps.forEach(lap => {
        if (lap.duration < minTime) minTime = lap.duration;
        if (lap.duration > maxTime) maxTime = lap.duration;
      });
    }

    laps.slice().reverse().forEach(lap => {
      const li = document.createElement('li');
      li.className = 'lap-item';

      if (laps.length > 1) {
        if (lap.duration === minTime) li.classList.add('best-lap');
        else if (lap.duration === maxTime) li.classList.add('worst-lap');
      }

      const lapFormatted = formatTime(lap.duration);
      const totalFormatted = formatTime(lap.total);

      li.innerHTML = `
        <span>Lap ${lap.number}</span>
        <span>+${lapFormatted.main}${lapFormatted.ms}</span>
        <span style="color: var(--text-muted);">${totalFormatted.main}${totalFormatted.ms}</span>
      `;
      lapList.appendChild(li);
    });
  };

  // Button Listeners
  startBtn.addEventListener('click', () => {
    if (!isRunning) {
      // Start
      isRunning = true;
      startTime = Date.now() - elapsedTime;
      timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        updateDisplay();
      }, 10);

      startBtn.innerHTML = `Pause`;
      startBtn.className = 'btn control-btn btn-pause';
      if (lapBtn) lapBtn.disabled = false;
    } else {
      // Pause
      isRunning = false;
      clearInterval(timerInterval);
      startBtn.innerHTML = `Resume`;
      startBtn.className = 'btn control-btn btn-start';
    }
  });

  if (lapBtn) {
    lapBtn.addEventListener('click', () => {
      if (!isRunning && elapsedTime === 0) return;
      const previousTotal = laps.length > 0 ? laps[laps.length - 1].total : 0;
      const lapDuration = elapsedTime - previousTotal;

      laps.push({
        number: laps.length + 1,
        duration: lapDuration,
        total: elapsedTime
      });
      renderLaps();
    });
  }

  resetBtn.addEventListener('click', () => {
    isRunning = false;
    clearInterval(timerInterval);
    elapsedTime = 0;
    laps = [];
    updateDisplay();
    renderLaps();

    startBtn.innerHTML = `Start`;
    startBtn.className = 'btn control-btn btn-start';
    if (lapBtn) lapBtn.disabled = true;
  });

  updateDisplay();
  renderLaps();
}
