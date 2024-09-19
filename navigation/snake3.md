---
layout: page 
title: Snake
permalink: /snake3/
---
# Hi

</style>
</head>
<body>
<div id="gameContainer">
    <canvas id="snakeGame" width="400" height="400"></canvas>
</div>

<script>
    // JavaScript Snake Game Code
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");

    const modes = {
        CLASSIC: 'classic',
        SPEED: 'speed',
        INFINITE: 'infinite',
        SLOW: 'slow'
    };
    let currentMode = modes.CLASSIC;  // Change this to switch modes

    let snake = [{ x: 200, y: 200 }];
    let direction = { x: 10, y: 0 };
    let food = { x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10 };
    let score = 0;
    let speed = 100; // Default speed
    let gameInterval;

    document.addEventListener("keydown", changeDirection);

    function startGame() {
        clearInterval(gameInterval);
        gameInterval = setInterval(gameLoop, speed);
    }

    function gameLoop() {
        if (checkGameOver()) {
            clearInterval(gameInterval);
            return;
        }

        clearCanvas();
        moveSnake();
        drawFood();
        drawSnake();
    }

    function clearCanvas() {
        ctx.fillStyle = "#ADD8E6";  // Light blue background
        ctx.fillRect(0, 0, canvas.width, canvas.height);  // Fill the entire canvas with the background color
    }

    function drawSnake() {
        snake.forEach(part => {
            ctx.fillStyle = "green";
            ctx.fillRect(part.x, part.y, 10, 10);
        });
    }

    function moveSnake() {
        const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };
        
        // Infinite Mode: Wrap around
        if (currentMode === modes.INFINITE) {
            head.x = (head.x + canvas.width) % canvas.width;
            head.y = (head.y + canvas.height) % canvas.height;
        }

        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score++;
            food = { x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10 };
            if (currentMode === modes.SPEED) {
                speed = Math.max(50, speed - 10);  // Increase speed
                clearInterval(gameInterval);
                gameInterval = setInterval(gameLoop, speed);
            }
        } else {
            snake.pop();
        }

        if (currentMode !== modes.INFINITE) {
            const head = snake[0];
            const hitWall = head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height;
            if (hitWall) return true;
        }

        const hitSelf = snake.slice(1).some(part => part.x === head.x && part.y === head.y);
        if (hitSelf) return true;

        return false;
    }

    function drawFood() {
        ctx.fillStyle = "red";
        ctx.fillRect(food.x, food.y, 10, 10);
    }

    function changeDirection(event) {
        const key = event.keyCode;
        if (key === 37 && direction.x === 0) { direction = { x: -10, y: 0 }; }
        if (key === 38 && direction.y === 0) { direction = { x: 0, y: -10 }; }
        if (key === 39 && direction.x === 0) { direction = { x: 10, y: 0 }; }
        if (key === 40 && direction.y === 0) { direction = { x: 0, y: 10 }; }
    }

    function checkGameOver() {
        if (currentMode === modes.CLASSIC || currentMode === modes.SPEED) {
            const head = snake[0];
            const hitWall = head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height;
            const hitSelf = snake.slice(1).some(part => part.x === head.x && part.y === head.y);

            if (hitWall || hitSelf) {
                ctx.fillStyle = "black";
                ctx.font = "20px Arial";
                ctx.fillText("Game Over!", canvas.width / 2 - 50, canvas.height / 2);
                return true;
            }
        }
        return false;
    }

    // Start the game initially
    startGame();
</script>

<script>
    // JavaScript Snake Game Code
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");

    let snake = [{ x: 200, y: 200 }];
    let direction = { x: 10, y: 0 };
    let food = { x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10 };
    let score = 0;
    let mode = 'classic';  // Mode can be 'classic', 'speed', or 'largeFood'
    let speed = 100; // Default speed for classic mode
    let interval = setInterval(gameLoop, speed);

    document.addEventListener("keydown", changeDirection);

    function gameLoop() {
        if (checkGameOver()) return;

        clearCanvas();
        moveSnake();
        drawFood();
        drawSnake();
    }

    function clearCanvas() {
        ctx.fillStyle = "#ADD8E6";  // Light blue background
        ctx.fillRect(0, 0, canvas.width, canvas.height);  // Fill the entire canvas with the background color
    }

    function drawSnake() {
        snake.forEach(part => {
            ctx.fillStyle = "green";
            ctx.fillRect(part.x, part.y, 10, 10);
        });
    }

    function moveSnake() {
        const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };
        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score++;
            if (mode === 'largeFood') {
                snake.push(snake[snake.length - 1]); // Grow the snake
            }
            food = { x: Math.floor(Math.random() * 40) * 10, y: Math.floor(Math.random() * 40) * 10 };
            if (mode === 'speed') {
                clearInterval(interval);
                speed = Math.max(50, speed - 10); // Increase speed
                interval = setInterval(gameLoop, speed);
            }
        } else {
            snake.pop();
        }
    }

    function drawFood() {
        ctx.fillStyle = mode === 'largeFood' ? "orange" : "red"; // Different color for large food mode
        ctx.fillRect(food.x, food.y, 10, 10);
    }

    function changeDirection(event) {
        const key = event.keyCode;
        if (key === 37 && direction.x === 0) { direction = { x: -10, y: 0 }; }
        if (key === 38 && direction.y === 0) { direction = { x: 0, y: -10 }; }
        if (key === 39 && direction.x === 0) { direction = { x: 10, y: 0 }; }
        if (key === 40 && direction.y === 0) { direction = { x: 0, y: 10 }; }
    }

    function checkGameOver() {
        const head = snake[0];
        const hitWall = head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height;
        const hitSelf = snake.slice(1).some(part => part.x === head.x && part.y === head.y);

        if (hitWall || hitSelf) {
            ctx.fillStyle = "black";
            ctx.font = "20px Arial";
            ctx.fillText("Game Over!", canvas.width / 2 - 50, canvas.height / 2);
            return true;
        }
        return false;
    }
</script>

<style>
    #snakeGame {
        border: 2px solid black;
        background-color: #ADD8E6; /* Light blue background for canvas */
    }
</style>