const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score');
const highScoreElement = document.getElementById('high-score');
const finalScoreElement = document.getElementById('final-score');
const gameOverScreen = document.getElementById('game-over');
const startScreen = document.getElementById('start-screen');
const startBtn = document.getElementById('start-btn');
const restartBtn = document.getElementById('restart-btn');

// Game configuration
const gridSize = 20;
const tileCount = canvas.width / gridSize;

// Game state
let snake = [{ x: 10, y: 10 }];
let food = {};
let dx = 0;
let dy = 0;
let score = 0;
let highScore = localStorage.getItem('snakeHighScore') || 0;
let gameRunning = false;
let gameLoop = null;

// Initialize high score display
highScoreElement.textContent = highScore;

// Generate random food position
function generateFood() {
    food = {
        x: Math.floor(Math.random() * tileCount),
        y: Math.floor(Math.random() * tileCount)
    };
    
    // Make sure food doesn't spawn on snake
    for (let segment of snake) {
        if (segment.x === food.x && segment.y === food.y) {
            generateFood();
            return;
        }
    }
}

// Draw functions
function drawSnake() {
    ctx.fillStyle = '#667eea';
    snake.forEach((segment, index) => {
        if (index === 0) {
            // Head
            ctx.fillStyle = '#764ba2';
        } else {
            ctx.fillStyle = '#667eea';
        }
        ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
    });
}

function drawFood() {
    ctx.fillStyle = '#e74c3c';
    ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
}

function clearCanvas() {
    ctx.fillStyle = '#f0f0f0';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// Game logic
function moveSnake() {
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    
    // Check wall collision
    if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
        gameOver();
        return;
    }
    
    // Check self collision
    for (let segment of snake) {
        if (head.x === segment.x && head.y === segment.y) {
            gameOver();
            return;
        }
    }
    
    snake.unshift(head);
    
    // Check food collision
    if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreElement.textContent = score;
        generateFood();
    } else {
        snake.pop();
    }
}

function update() {
    if (!gameRunning) return;
    
    clearCanvas();
    moveSnake();
    drawFood();
    drawSnake();
}

function gameOver() {
    gameRunning = false;
    clearInterval(gameLoop);
    
    // Update high score
    if (score > highScore) {
        highScore = score;
        highScoreElement.textContent = highScore;
        localStorage.setItem('snakeHighScore', highScore);
    }
    
    finalScoreElement.textContent = score;
    gameOverScreen.classList.remove('hidden');
}

function startGame() {
    // Reset game state
    snake = [{ x: 10, y: 10 }];
    dx = 0;
    dy = 0;
    score = 0;
    scoreElement.textContent = score;
    gameRunning = true;
    
    // Hide screens
    startScreen.classList.add('hidden');
    gameOverScreen.classList.add('hidden');
    
    // Generate food
    generateFood();
    
    // Start game loop
    gameLoop = setInterval(update, 100);
    update();
}

function changeDirection(newDx, newDy) {
    // Prevent reversing into itself
    if (dx === -newDx && dy === -newDy) return;
    if (dx === 0 && dy === 0) {
        dx = newDx;
        dy = newDy;
        return;
    }
    dx = newDx;
    dy = newDy;
}

// Keyboard controls
document.addEventListener('keydown', (e) => {
    if (!gameRunning && e.key !== 'Enter') return;
    
    switch(e.key) {
        case 'ArrowUp':
            e.preventDefault();
            changeDirection(0, -1);
            break;
        case 'ArrowDown':
            e.preventDefault();
            changeDirection(0, 1);
            break;
        case 'ArrowLeft':
            e.preventDefault();
            changeDirection(-1, 0);
            break;
        case 'ArrowRight':
            e.preventDefault();
            changeDirection(1, 0);
            break;
    }
});

// Button controls
startBtn.addEventListener('click', startGame);
restartBtn.addEventListener('click', startGame);

// Mobile/touch controls
document.getElementById('up-btn').addEventListener('click', () => {
    if (gameRunning) changeDirection(0, -1);
});
document.getElementById('down-btn').addEventListener('click', () => {
    if (gameRunning) changeDirection(0, 1);
});
document.getElementById('left-btn').addEventListener('click', () => {
    if (gameRunning) changeDirection(-1, 0);
});
document.getElementById('right-btn').addEventListener('click', () => {
    if (gameRunning) changeDirection(1, 0);
});

// Initial food generation (for visual)
generateFood();
clearCanvas();
drawFood();


