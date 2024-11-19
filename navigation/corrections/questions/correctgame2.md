---
layout: page 
title: Corrections Game
permalink: /correctionsgame2/
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
       <div id="question-1-display" class="question-1-display-text">A population researcher is interested in predicting the number of births that will occur in a particular community. She created a computer model that uses data from the past ten years, including number of residents and the number of babies born. The model predicted that there would be 200 births last year, but the actual number of births last year was only 120. Which of the following strategies is LEAST likely to provide a more accurate prediction?
       </div>
   </div>


<button id="answer-a" class="button">A. Gathering data for additional years to try to identify patterns in birth rates</button>
<div id="summary-a" class="summary" style="display:none;">
  Good try. Gathering additional data may help the simulation to provide a more accurate prediction.
</div>

<button id="answer-b" class="button">B. Refining the model used in the computer simulation to more closely reflect the data from the past ten years
</button>
<div id="summary-b" class="summary" style="display:none;">
  Good try. Refining the model used in the simulation may help provide a more accurate prediction.
</div>

<button id="answer-c" class="button">C. Removing as many details from the model as possible so that calculations can be performed quickly</button>
<div id="summary-c" class="summary" style="display:none;">
  Brilliant. Removing details from the model may help it run quickly, but is unlikely to provide more accurate results.
</div>

<button id="answer-d" class="button">D. Taking into consideration more information about the community, such as the ages of residents</button>
<div id="summary-d" class="summary" style="display:none;">
  Good try. Gathering additional data may help the simulation provide a more accurate prediction.
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
