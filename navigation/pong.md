---
layout: page 
title: Pong
Description: Pong
permalink: /pong/
---

# 🏓 Pong Game


<div style="text-align: center;">
  <canvas id="pong" width="600" height="400" style="border:1px solid #000;"></canvas>
</div>

<script>
  const canvas = document.getElementById("pong");
  const ctx = canvas.getContext("2d");

  const paddleWidth = 10, paddleHeight = 100;
  let paddle1Y = (canvas.height - paddleHeight) / 2;
  let paddle2Y = (canvas.height - paddleHeight) / 2;
  let ballX = canvas.width / 2, ballY = canvas.height / 2;
  let ballSpeedX = 3, ballSpeedY = 3;
  let paddle1Speed = 0;

  function drawRect(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
  }

  function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();
  }

  function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballSpeedX = -ballSpeedX;
  }

  function moveBall() {
    ballX += ballSpeedX;
    ballY += ballSpeedY;

    if (ballY + 10 > canvas.height || ballY - 10 < 0) {
      ballSpeedY = -ballSpeedY;
    }

    if (ballX + 10 > canvas.width) {
      if (ballY > paddle2Y && ballY < paddle2Y + paddleHeight) {
        ballSpeedX = -ballSpeedX;
      } else {
        resetBall();
      }
    }

    if (ballX - 10 < 0) {
      if (ballY > paddle1Y && ballY < paddle1Y + paddleHeight) {
        ballSpeedX = -ballSpeedX;
      } else {
        resetBall();
      }
    }
  }

  function movePaddle2() {
    const paddle2Speed = 3;
    if (ballY < paddle2Y + paddleHeight / 2) {
      paddle2Y -= paddle2Speed;
    } else if (ballY > paddle2Y + paddleHeight / 2) {
      paddle2Y += paddle2Speed;
    }
  }

  function movePaddle1() {
    paddle1Y += paddle1Speed;
    if (paddle1Y < 0) paddle1Y = 0;
    if (paddle1Y > canvas.height - paddleHeight) paddle1Y = canvas.height - paddleHeight;
  }

  document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
      paddle1Speed = -5;
    } else if (event.key === "ArrowDown") {
      paddle1Speed = 5;
    }
  });

  document.addEventListener("keyup", function(event) {
    if (event.key === "ArrowUp" || event.key === "ArrowDown") {
      paddle1Speed = 0;
    }
  });

  function gameLoop() {
    drawRect(0, 0, canvas.width, canvas.height, "#000"); // Background
    drawRect(0, paddle1Y, paddleWidth, paddleHeight, "#fff"); // Left Paddle
    drawRect(canvas.width - paddleWidth, paddle2Y, paddleWidth, paddleHeight, "#fff"); // Right Paddle
    drawCircle(ballX, ballY, 10, "#fff"); // Ball

    moveBall();
    movePaddle2();
    movePaddle1();
  }

  setInterval(gameLoop, 1000 / 60); // 60 frames per second
</script>

 <script>
  // Prevent the default bahavior the arrow
  window.addEventListener("keydown", function(e) {
    if (["ArrowUp", "ArrowDown", "ArrowRight"].includes(e.key))
      e.preventDefault();
   });
   </script>