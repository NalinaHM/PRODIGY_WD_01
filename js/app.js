/* ==========================================================================
   PRODIGY INFOTECH WEB SUITE - MASTER APP ENTRY POINT
   ========================================================================== */

import { initNavbar } from './navbar.js';
import { initStopwatch } from './stopwatch.js';
import { initTicTacToe } from './tictactoe.js';
import { initPortfolio } from './portfolio.js';
import { initWeather } from './weather.js';

document.addEventListener('DOMContentLoaded', () => {
  console.log('⚡ Initializing Prodigy InfoTech Web Application Suite...');

  // Initialize all 5 Task modules
  initNavbar();     // Task 01: Landing & Nav Menu
  initStopwatch();  // Task 02: Stopwatch App
  initTicTacToe();  // Task 03: Tic-Tac-Toe Game
  initPortfolio();  // Task 04: Developer Portfolio
  initWeather();    // Task 05: Weather Dashboard

  console.log('✅ All 5 Task modules loaded successfully.');
});
