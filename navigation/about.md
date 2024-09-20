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
- I also enjoy watching sports -->

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
  <img id="gallery-image" src="../images/gallery/akshajg1.jpg" alt="Image Gallery" style="width: 300px; height: auto;">
  <br>
  <button id="prev-btn">Previous</button>
  <button id="next-btn">Next</button>
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
