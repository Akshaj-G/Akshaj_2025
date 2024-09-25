---
layout: post
title: About
permalink: /about/
toc: True
comments: True
---

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #FFFFFF;
        color: #FFFFFF;
        margin: 20px;
        line-height: 1.6;
    }

<style>
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>

Creator of Student 2025

# Who am I?
> Hi my name is Akshaj, I'm a sophomore at Del Norte High School. I'm 15 years old. I have dad, mom and a brother who is 7 years old.

---

<!-- <img src="{{site.baseurl}}/images/akshajg.jpg" height="200" width="200" class="center"> - correct format -->



# Why am I interested in Computer Science
 > I am enrolled in Computer Science Principles, due to my interest in learning and further pursuing a career in Technology. 


>>The computer science skills I learn from this class would be valuable as I want to use it to assist me in future projects. I want to combine my interest in Finance and Computer Science to create a project. 

# Sports
>- I play on JV Tennis
- I enjoy playing basketball
- I like the 49ers and the golden state warriors
<!-- - Luckily never broke a bone in my body
I also enjoy watching sports -->

---

<!-- <img src="{{site.baseurl}}/images/mytennis.jpg" height="200" width="200" class="center"> correct format-->

<!--# Clubs/Experience
>- Akshaya Patra - 3rd year
- DECA - 2nd year
- Academic League - 2nd year
- JV Tennis - 2nd year
- Restoring Rainbows - 1st year-->

# Linkedin

>[Connect with me on LinkedIn](https://www.linkedin.com/in/akshaj-gurugubelli-11a66129b/)

>[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/akshaj-gurugubelli-11a66129b/)

# My journey so far....
<div id="gallery-container" style="text-align: center;">
  <img id="gallery-image" src="../images/gallery/akshajg1.jpg" alt="Image Gallery" style="width: 300px; height: auto,cursor: pointer; box-shadow: 20px 20px 20px rgba(25, 150, 500, 50.3); border-radius: 500%;">
  <br>
  <button id="prev-btn"><---</button>
  <button id="next-btn">---></button>
</div>
 
<script>
    // Array of image filenames located in the 'images' directory
    const imageFilenames = [
        "akshajg1.jpg",
        "akshajg2.jpg",
        "mytennis.jpg"

    ];

    let currentIndex = 0;  // To keep track of the currently displayed image

    // Reference to the gallery image element
    const galleryImage = document.getElementById('gallery-image');

    // Function to update the displayed image
    function updateImage() {
        galleryImage.src = `../images/gallery/${imageFilenames[currentIndex]}`;
        galleryImage.alt = imageFilenames[currentIndex];
    }

    // Event listeners for the buttons
    document.getElementById('prev-btn').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : imageFilenames.length - 1;
        updateImage();
    });

    document.getElementById('next-btn').addEventListener('click', function() {
        currentIndex = (currentIndex < imageFilenames.length - 1) ? currentIndex + 1 : 0;
        updateImage();
    });
</script>

# Chat Bot

<style>
    .chat-container {
        width: 400px;
        height: 500px;
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        font-family: Arial, sans-serif;
    }

    .chat-box {
        flex-grow: 1;
        overflow-y: auto;
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .message {
        margin: 5px 0;
        padding: 8px 12px;
        border-radius: 10px;
        display: inline-block;
    }

    .user-message {
        background-color: #cce5ff;
        align-self: flex-end;
    }

    .bot-message {
        background-color: #e2e2e2;
        align-self: flex-start;
    }

    .input-box {
        display: flex;
    }

    .input-box input {
        flex-grow: 1;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .input-box button {
        padding: 10px 20px;
        margin-left: 10px;
        border: none;
        background-color: #28a745;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }

    .input-box button:hover {
        background-color: #218838;
    }
</style>

<script>
    const botResponses = {
        "how are you": "I'm just a bot, but thanks for asking! How can I assist you?",
        "what is your name": "I'm an advanced chatbot here to help you out!",
        "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "what is the meaning of life": "42, according to Douglas Adams! What do you think?",
        "who created you": "I was created by a talented developer!",
    };

    function addMessage(content, className) {
        const chatBox = document.querySelector('.chat-box');
        const message = document.createElement('div');
        message.classList.add('message', className);
        message.textContent = content;
        chatBox.appendChild(message);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function getBotResponse(userMessage) {
        const cleanedMessage = userMessage.toLowerCase().trim();
        if (botResponses[cleanedMessage]) {
            return botResponses[cleanedMessage];
        } else {
            return "I don't have an answer for that. Can you ask something else?";
        }
    }

    function handleUserInput() {
        const input = document.querySelector('input');
        const userMessage = input.value.trim();
        if (userMessage !== "") {
            addMessage(userMessage, 'user-message');
            input.value = '';

            setTimeout(() => {
                const botMessage = getBotResponse(userMessage);
                addMessage(botMessage, 'bot-message');
            }, 1000);
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        const button = document.querySelector('button');
        const input = document.querySelector('input');
        button.addEventListener('click', handleUserInput);
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                handleUserInput();
            }
        });
    });
</script>

<div class="chat-container">
    <div class="chat-box"></div>
    <div class="input-box">
        <input type="text" placeholder="Type your message...">
        <button>Send</button>
    </div>
</div>

<button class="shadow-button">Click Me</button>


