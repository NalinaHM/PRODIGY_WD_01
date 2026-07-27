/* ==========================================================================
   TASK-03: TIC-TAC-TOE GAME ENGINE & AI
   ========================================================================== */

export function initTicTacToe() {
  const grid = document.getElementById('tttGrid');
  const statusText = document.getElementById('tttStatus');
  const resetBtn = document.getElementById('tttResetBtn');
  const pvpBtn = document.getElementById('modePVP');
  const aiBtn = document.getElementById('modeAI');
  const scoreXEl = document.getElementById('scoreX');
  const scoreOEl = document.getElementById('scoreO');
  const scoreDrawEl = document.getElementById('scoreDraw');

  if (!grid || !statusText) return;

  let board = Array(9).fill('');
  let currentPlayer = 'X';
  let isGameActive = true;
  let gameMode = 'pvp'; // 'pvp' or 'ai'
  let scores = { X: 0, O: 0, Draw: 0 };

  const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
  ];

  const updateScores = () => {
    if (scoreXEl) scoreXEl.textContent = scores.X;
    if (scoreOEl) scoreOEl.textContent = scores.O;
    if (scoreDrawEl) scoreDrawEl.textContent = scores.Draw;
  };

  const renderBoard = () => {
    grid.innerHTML = '';
    board.forEach((val, idx) => {
      const cell = document.createElement('div');
      cell.className = 'ttt-cell';
      cell.dataset.index = idx;
      if (val !== '') {
        cell.classList.add('taken', val === 'X' ? 'cell-x' : 'cell-o');
        cell.textContent = val;
      }
      cell.addEventListener('click', () => handleCellClick(idx));
      grid.appendChild(cell);
    });
  };

  const checkWinner = (currentBoard) => {
    for (let pattern of winPatterns) {
      const [a, b, c] = pattern;
      if (currentBoard[a] && currentBoard[a] === currentBoard[b] && currentBoard[a] === currentBoard[c]) {
        return { winner: currentBoard[a], pattern };
      }
    }
    if (currentBoard.every(cell => cell !== '')) {
      return { winner: 'Draw' };
    }
    return null;
  };

  const handleCellClick = (index) => {
    if (board[index] !== '' || !isGameActive) return;

    makeMove(index, currentPlayer);

    const result = checkWinner(board);
    if (result) {
      handleGameOver(result);
      return;
    }

    // Switch Player
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    statusText.textContent = `Player ${currentPlayer}'s Turn`;

    // AI Move if AI Mode
    if (gameMode === 'ai' && currentPlayer === 'O' && isGameActive) {
      setTimeout(makeAIMove, 400);
    }
  };

  const makeMove = (index, player) => {
    board[index] = player;
    renderBoard();
  };

  const handleGameOver = (result) => {
    isGameActive = false;
    if (result.winner === 'Draw') {
      statusText.textContent = "🤝 It's a Draw!";
      scores.Draw++;
    } else {
      statusText.textContent = `🎉 Player ${result.winner} Wins!`;
      scores[result.winner]++;
      
      // Highlight winning cells
      if (result.pattern) {
        result.pattern.forEach(idx => {
          const cell = grid.children[idx];
          if (cell) cell.classList.add('winning-cell');
        });
      }
    }
    updateScores();
  };

  // Minimax Unbeatable AI Engine
  const makeAIMove = () => {
    const bestMove = minimax(board, 'O').index;
    if (bestMove !== undefined) {
      handleCellClick(bestMove);
    }
  };

  const minimax = (newBoard, player) => {
    const availSpots = newBoard.map((val, idx) => val === '' ? idx : null).filter(val => val !== null);
    const winResult = checkWinner(newBoard);

    if (winResult) {
      if (winResult.winner === 'X') return { score: -10 };
      if (winResult.winner === 'O') return { score: 10 };
      if (winResult.winner === 'Draw') return { score: 0 };
    }

    const moves = [];
    for (let i = 0; i < availSpots.length; i++) {
      const idx = availSpots[i];
      const move = {};
      move.index = idx;
      newBoard[idx] = player;

      if (player === 'O') {
        const result = minimax(newBoard, 'X');
        move.score = result.score;
      } else {
        const result = minimax(newBoard, 'O');
        move.score = result.score;
      }

      newBoard[idx] = '';
      moves.push(move);
    }

    let bestMove;
    if (player === 'O') {
      let bestScore = -10000;
      for (let i = 0; i < moves.length; i++) {
        if (moves[i].score > bestScore) {
          bestScore = moves[i].score;
          bestMove = i;
        }
      }
    } else {
      let bestScore = 10000;
      for (let i = 0; i < moves.length; i++) {
        if (moves[i].score < bestScore) {
          bestScore = moves[i].score;
          bestMove = i;
        }
      }
    }

    return moves[bestMove];
  };

  const resetGame = () => {
    board = Array(9).fill('');
    currentPlayer = 'X';
    isGameActive = true;
    statusText.textContent = "Player X's Turn";
    renderBoard();
  };

  // Event Listeners for Mode Buttons
  if (pvpBtn) {
    pvpBtn.addEventListener('click', () => {
      gameMode = 'pvp';
      pvpBtn.classList.add('active');
      if (aiBtn) aiBtn.classList.remove('active');
      resetGame();
    });
  }

  if (aiBtn) {
    aiBtn.addEventListener('click', () => {
      gameMode = 'ai';
      aiBtn.classList.add('active');
      if (pvpBtn) pvpBtn.classList.remove('active');
      resetGame();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', resetGame);
  }

  resetGame();
}
