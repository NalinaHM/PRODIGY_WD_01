// Task 03: Tic-Tac-Toe Game & Minimax AI Engine
document.addEventListener('DOMContentLoaded', () => {
  const grid = document.getElementById('grid');
  const statusMsg = document.getElementById('gameStatus');
  const resetBtn = document.getElementById('resetBtn');
  const pvpBtn = document.getElementById('pvpBtn');
  const aiBtn = document.getElementById('aiBtn');
  const scoreXEl = document.getElementById('scoreX');
  const scoreOEl = document.getElementById('scoreO');
  const scoreDrawEl = document.getElementById('scoreDraw');

  let board = Array(9).fill('');
  let currentPlayer = 'X';
  let isGameActive = true;
  let mode = 'pvp'; // 'pvp' or 'ai'
  let scores = { X: 0, O: 0, Draw: 0 };

  const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
  ];

  function renderBoard() {
    grid.innerHTML = '';
    board.forEach((val, idx) => {
      const cell = document.createElement('div');
      cell.className = 'cell';
      if (val !== '') {
        cell.classList.add('taken', val.toLowerCase());
        cell.textContent = val;
      }
      cell.addEventListener('click', () => handleClick(idx));
      grid.appendChild(cell);
    });
  }

  function checkWin(b) {
    for (let p of winPatterns) {
      const [a, bIdx, c] = p;
      if (b[a] && b[a] === b[bIdx] && b[a] === b[c]) {
        return { winner: b[a], pattern: p };
      }
    }
    if (b.every(cell => cell !== '')) return { winner: 'Draw' };
    return null;
  }

  function handleClick(idx) {
    if (board[idx] !== '' || !isGameActive) return;

    board[idx] = currentPlayer;
    renderBoard();

    const res = checkWin(board);
    if (res) {
      endGame(res);
      return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    statusMsg.textContent = `Player ${currentPlayer}'s Turn`;

    if (mode === 'ai' && currentPlayer === 'O' && isGameActive) {
      setTimeout(makeAIMove, 350);
    }
  }

  function makeAIMove() {
    const bestMove = minimax(board, 'O').index;
    if (bestMove !== undefined) {
      handleClick(bestMove);
    }
  }

  function minimax(newBoard, player) {
    const avail = newBoard.map((v, i) => v === '' ? i : null).filter(v => v !== null);
    const win = checkWin(newBoard);

    if (win) {
      if (win.winner === 'X') return { score: -10 };
      if (win.winner === 'O') return { score: 10 };
      if (win.winner === 'Draw') return { score: 0 };
    }

    const moves = [];
    for (let i = 0; i < avail.length; i++) {
      const idx = avail[i];
      const move = { index: idx };
      newBoard[idx] = player;

      if (player === 'O') {
        move.score = minimax(newBoard, 'X').score;
      } else {
        move.score = minimax(newBoard, 'O').score;
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
  }

  function endGame(res) {
    isGameActive = false;
    if (res.winner === 'Draw') {
      statusMsg.textContent = "🤝 Game Draw!";
      scores.Draw++;
    } else {
      statusMsg.textContent = `🎉 Player ${res.winner} Wins!`;
      scores[res.winner]++;
      if (res.pattern) {
        res.pattern.forEach(idx => {
          if (grid.children[idx]) grid.children[idx].classList.add('winner');
        });
      }
    }
    scoreXEl.textContent = scores.X;
    scoreOEl.textContent = scores.O;
    scoreDrawEl.textContent = scores.Draw;
  }

  function reset() {
    board = Array(9).fill('');
    currentPlayer = 'X';
    isGameActive = true;
    statusMsg.textContent = "Player X's Turn";
    renderBoard();
  }

  pvpBtn.addEventListener('click', () => {
    mode = 'pvp';
    pvpBtn.classList.add('active');
    aiBtn.classList.remove('active');
    reset();
  });

  aiBtn.addEventListener('click', () => {
    mode = 'ai';
    aiBtn.classList.add('active');
    pvpBtn.classList.remove('active');
    reset();
  });

  resetBtn.addEventListener('click', reset);

  reset();
});
