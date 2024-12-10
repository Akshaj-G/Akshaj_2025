---
layout: page 
title: Corrections Game
permalink: /correctionsgame1/
---

<link rel="stylesheet" href="{{site.baseurl}}/navigation/corrections/correctgame.css">

<script>
document.addEventListener('DOMContentLoaded', function () {
    // Add click event listeners to each button to toggle the corresponding summary
    document.getElementById('answer-a').addEventListener('click', function() {
        toggleSummary('summary-a');
    });

    document.getElementById('answer-b').addEventListener('click', function() {
        toggleSummary('summary-b');
    });

    document.getElementById('answer-c').addEventListener('click', function() {
        toggleSummary('summary-c');
    });

    document.getElementById('answer-d').addEventListener('click', function() {
        toggleSummary('summary-d');
    });

    // Function to toggle visibility of the summary div
    function toggleSummary(id) {
        const summary = document.getElementById(id);
        if (summary.style.display === "none" || summary.style.display === "") {
            summary.style.display = "block";  // Show the summary
        } else {
            summary.style.display = "none";   // Hide the summary
        }
    }
});
</script>

<div class="question1-container">
   <h1>College Board Review</h1>

<div class="question-1">
       <div id="question-1" class="question-1-text">Question 1</div>
       <div id="question-1-display" class="question-1-display-text">Which of the following is a true statement about Internet communication?
       </div>
   </div>


<button id="answer-a" class="button">A. Devices from different manufacturers are required to run the same operating system to communicate over the Internet.</button>
<div id="summary-a" class="summary" style="display:none;">
  Good try. Devices from different manufacturers do not need the same operating system to communicate over the Internet, as long as they follow the same protocols like TCP/IP.
</div>

<button id="answer-b" class="button">B. Every device connected to the Internet is assigned a digital certificate by a certificate authority.</button>
<div id="summary-b" class="summary" style="display:none;">
  Good try. Not every device is assigned a digital certificate; digital certificates are typically used for secure communication, such as with websites (SSL/TLS).
</div>

<button id="answer-c" class="button">C. Every device connected to the Internet is assigned an Internet protocol (IP) address.</button>
<div id="summary-c" class="summary" style="display:none;">
  Brilliant. Every device on the Internet is assigned a unique IP address to identify it and allow communication.
</div>

<button id="answer-d" class="button">D. Every device connected to the Internet requires a high-bandwidth connection to enable redundant routing to each device.</button>
<div id="summary-d" class="summary" style="display:none;">
  Good try. Not all devices need high-bandwidth connections, and redundant routing can occur without requiring high bandwidth.
</div>

   <style>
   .question1-container {
       font-family: Arial, sans-serif;
       margin: 0 auto;
       padding: 20px;
       max-width: 800px;
       text-align: center;
       box-shadow: 0 4px 8px rgba(0, 0, 255, 0.2); /* Blue shadow for main container */
       border-radius: 10px;
   }

   .button {
   font-size: 1.5em; /* Make the font size larger */
   color: #333333; /* Dark grey color */
   text-shadow: 1px 1px 5px rgba(0, 0, 255, 0.4); /* Blue shadow for label */
   margin-bottom: 20px;
   }
   
   .button label {
   font-size: 1.5em; /* Make the font size larger */
   color: #333333; /* Dark grey color */
   text-shadow: 1px 1px 5px rgba(0, 0, 255, 0.4); /* Blue shadow for label */
   }
   .button {
   font-size: 1.5em; /* Increase font size */
   color: #333333; /* Dark grey text color */
   text-shadow: 1px 1px 5px rgba(0, 0, 255, 0.4); /* Blue shadow for text */
   background-color: #007bff; /* Button background color (optional) */
   padding: 10px 20px; /* Add padding for better appearance */
   border: none;
   border-radius: 8px;
   cursor: pointer;
   box-shadow: 0 4px 6px rgba(0, 0, 255, 0.3); /* Blue shadow around button */
   transition: box-shadow 0.3s ease;
   }


   .button:hover {
   box-shadow: 0 6px 12px rgba(100, 100, 255, 50.4); /* Stronger shadow on hover */
   }

   </style>

 <style>
    
    .game-container {
      margin: 20px auto;
      width: 60%;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .button {
      margin: 10px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>


 <div id="question-container" style="text-align: center;">
   <page id="quiz-rotation-button" src="../corrections/question/correctgame1.jpg" alt="questions" >
   <br>
   <button id="prev-btn"><---</button>
   <button id="next-btn">---></button>
 </div>
  
 <script>
     // Array of image filenames located in the 'images' directory
     const questionFilenames = [
         "correctgame1.jpg",
         "correctgame2.jpg",
         "correctgame3.jpg"
 
     ];
     
     let currentIndex = 0;  // To keep track of the currently displayed image

    // Reference to the gallery image element
    const galleryImage = document.getElementById('quiz-rotation-button');

    // Function to update the displayed image
    function updatePage() {
        galleryImage.src = `../corrections/question/${questionFilenames[currentIndex]}`;
        galleryImage.alt = questionFilenames[currentIndex];
    }

    // Event listeners for the buttons
    document.getElementById('prev-btn').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : questionFilenames.length - 1;
        updatePage();
    });

    document.getElementById('next-btn').addEventListener('click', function() {
        currentIndex = (currentIndex < questionFilenames.length - 1) ? currentIndex + 1 : 0;
        updatePage();
    });
</script>