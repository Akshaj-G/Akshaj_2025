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
    if (summary.style.display === "none") {
      summary.style.display = "block";
    } else {
      summary.style.display = "none";
    }
  }
  
