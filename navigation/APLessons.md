---
layout: page 
title: AP Learnings
permalink: /APLessons/
---

# College Board Test Review

## Question 15

Question: Which of the following is a true statement about Internet communication?

My Answer: **A.** Devices from different manufacturers are required to run the same operating system to communicate over the Internet.

Correct Answer: **C.** Every device connected to the Internet is assigned an Internet protocol (IP) address.

Explanation: The IP address uniquely identifies devices on the Internet, allowing them to send and receive data. Devices do not need to run the same operating system to communicate because the Internet uses standardized communication protocols like TCP/IP that work across different systems.

## Question 18

Question: A population researcher is interested in predicting the number of births that will occur in a particular community. She created a computer model that uses data from the past ten years, including number of residents and the number of babies born. The model predicted that there would be 200 births last year, but the actual number of births last year was only 120. Which of the following strategies is LEAST likely to provide a more accurate prediction?

My Answer: **A.** Gathering data for additional years to try to identify patterns in birth rates.

Correct Answer: **C.** Removing as many details from the model as possible so that calculations can be performed quickly.

Explanation: **I misread the question.** Simplifying the model to prioritize speed over accuracy is least likely to improve the prediction. By removing details, the model becomes less representative of the factors that influence birth rates, such as population demographics or historical trends, leading to less accurate predictions. While faster calculations might be convenient, they do not help the model make better predictions.In contrast **A** (gathering more data) provides additional insights and improves the model’s reliability by identifying long-term patterns.

## Question 19

Question: A library of e-books contains metadata for each book. The metadata are intended to help a search feature find books that users are interested in. Which of the following is LEAST likely to be contained in the metadata of each e-book?

My Answer: **D.** The genre of the e-book (e.g., comedy, fantasy, romance, etc.)

Correct Answer: **A.** An archive containing previous versions of the e-book

Explanation: Metadata refers to data that describes other data, providing essential information to help users find, organize, and understand the content. In the case of e-books, metadata typically includes the author, title, publication date, and genre. Option A is least likely to be included in the metadata. Metadata is primarily concerned with details about the current version of the e-book, not its previous versions. While some systems may track versions, an archive of past versions is typically stored separately and not considered part of the e-book's core metadata.

## Question 21

Question: The following question uses a robot in a grid of squares. The robot is represented by a triangle, which is initially facing right.

My Answer: **A.** 

Correct Answer: **B.**

Explanation: Pay a closer look at the right rotations. **Easy fix**

## Question 22

Question: A student is creating a procedure to determine whether the weather for a particular month was considered very hot. The procedure takes as input a list containing daily high temperatures for a particular month. The procedure is intended to return true if the daily high temperature was at least 90 degrees for a majority of days in the month and return false otherwise. Which of the following can be used to replace missing code so that the procedure works as intended?

My Answer: **C.** total < 0.5 * counter


Correct Answer: **B.** counter > 0.5 * total

Explanation: Pay closer attention to what the question is askings, **Easy fix**

## Question 23

Question: The following figures represent different ways of configuring a network of physically linked computers labeled P, Q, R, and S. A line between two computers indicates that the computers can communicate directly with each other. In which configuration is it NOT possible to have redundant routing between computers P and S?

My Answer: **C.** 


Correct Answer: **B.** 

Explanation: Redundant routing is impossible if there is only one possible path from one device to another. There is only one possible path from P to S (P to R to Q to S).

## Question 24

Question: Byte pair encoding is a data encoding technique. The encoding algorithm looks for pairs of characters that appear in the string more than once and replaces each instance of that pair with a corresponding character that does not appear in the string. The algorithm saves a list containing the mapping of character pairs to their corresponding replacement characters. For example, the string Open quotation, "THIS_IS_THE_BEST_WISH" can be encoded as "%#_#_%BEST_W#H" by replacing all the instances of "TH" with "%" and replacing al instances of "IS" with "#". Which of the following statements about byte pair encoding is true?

My Answer: **B.** Byte pair encoding is an example of a lossy transformation because some pairs of characters are replaced by a single character.


Correct Answer: **C.** Byte pair encoding is an example of a lossless transformation because an encoded string can be restored to its original version.


Explanation: **Easy Fix**. Byte pair encoding (BPE) is a lossless transformation, meaning that it can be reversed to recover the original data without any loss. In BPE, pairs of characters that appear frequently are replaced with a new character, but the key detail is that the list of replacements (the mapping of the pairs to new characters) is saved. This allows the original string to be reconstructed by reversing the replacements.


## Question 25

Question: Byte pair encoding is a data encoding technique. The encoding algorithm looks for pairs of characters that appear in the string more than once and replaces each instance of that pair with a corresponding character that does not appear in the string. The algorithm saves a list containing the mapping of character pairs to their corresponding replacement characters. For example, the string Open quotation, "THIS_IS_THE_BEST_WISH" can be encoded as "%#_#_%BEST_W#H" by replacing all the instances of "TH" with "%" and replacing al instances of "IS" with "#". For which of the following strings is it NOT possible to use byte pair encoding to shorten the string’s length?


My Answer: **A.** "BANANA"


Correct Answer: **B.** "LEVEL_UP"


Explanation: LEVEL_UP would not be possible to use byte pair encoding to shorten the string’s length as there are no pair of letters that appear in the string more than once.

## Question 26

Question: The grid below contains a robot represented as a triangle, initially facing up. The robot can move into a white or gray square but cannot move into a black region. Which of the following replacements for missing code can be used to move the robot to the gray square?

My Answer: **C.** 


Correct Answer: **A.** 


Explanation: The code I chose would force the robot to go forward near the end instead of tking a right turn as it could still go forward. If it takes a right turn whenever possible, it would take right turn near the end and reach the gray area. **Easy Fix**, pay attention.

## Question 27

Question: A student wrote the following code for a guessing game. While debugging the code, the student realizes that the loop never terminates. The student plans to insert the instruction Win, left arrow, true somewhere in the code. Where could Win, left arrow, true be inserted so that the code segment works as intended?

My Answer: **A.** Between line 6 and line 7


Correct Answer: **B.** Between line 9 and line 10


Explanation: Inserting Win, left arrow, true between line 9 and line 10 will cause the loop to terminate when the guess is correct.

## Question 28

Question: A text-editing application uses binary sequences to represent each of 200 different characters. What is the minimum number of bits needed to assign a unique bit sequence to each of the possible characters?

My Answer: **B.** 6


Correct Answer: **D.** 8


Explanation: A Math error. We need atleast 200, 2 to the power of 6 only allows 64, while 2 to the power of 8 allows 256 different combinations. **Easy fix** 

## Question 30

Question: A video-streaming service maintains a database of information about its customers and the videos they have watched. The program below analyzes the data in the database and compares the number of viewers of science fiction videos to the number of viewers of videos of other genres. It uses the procedure Analysis "category" which returns the number of unique users who viewed videos of a given category in the past year. The Analysis procedure takes approximately 1 hour to return a result, regardless of the number of videos of the given genre. All other operations happen nearly instantaneously. Which of the following best approximates the amount of time it takes the program to execute? CODE PROVIDED

My Answer: **A.** 1 hour


Correct Answer: **D.** 5 hours


Explanation: Each call to the Analysis procedure requires one hour of program execution time. The procedure is called once before the loop, and then four times inside the loop (once for each of the four entries in One word, genre List). Therefore, the program will take approximately 5 hours to execute.**Easy fix** 

## Question 37

Question: The two code segments below are each intended to display the average of the numbers in the list One word, num List. Assume that One word, num List contains more than one value. Which of the following best describes the two code segments? CODE PROVIDED

My Answer: **D.** Both code segments display the correct average, but code segment II requires more arithmetic operations than code segment I.


Correct Answer: **C.** Both code segments display the correct average, but code segment I requires more arithmetic operations than code segment II.


Explanation: Both code segments display the correct average. Code segment I requires more arithmetic operations because it performs the operation sum divided by LENGTH, open parenthesis, num List, close parenthesis within the loop, while code segment II performs the same operation only once. **Easy fix** 

## Question 40

Question: Grades in a computer science course are based on total points earned on a midterm exam and a final exam. The teacher provides a way for students to improve their course grades if they receive high scores on the final exam: if a student’s final exam score is greater than the student’s midterm exam score, the final exam score replaces the midterm exam score in the calculation of total points. The table below shows two students’ scores on the midterm and final exams and the calculated total points each student earns. Khalil does better on the midterm exam than on the final exam, so his original midterm and final exam scores are added to compute his total points. Josefina does better on the final exam than on the midterm exam, so her final exam score replaces her midterm exam score in the total points calculation. The teacher has data representing the scores of thousands of students. For each student, the data contain the student name, the midterm exam score, the final exam score, and the result of the total points calculation. Which of the following could be determined from the data? A TABLE PROVODED

- I. The average total points earned per student
- II. The average increase in total points per student as a result of the score replacement policy
- III. The proportion of students who improved their total points as a result of the score replacement policy

My Answer: **B.** I and II only


Correct Answer: **D.** I, II, and III


Explanation: The average total points earned per student can be determined using the result of the total points calculation for each student. The average increase in total points per student as a result of the score replacement policy can be determined by calculating the differences between each student score before and after the replacement policy was applied. The proportion of students who improved their total points as a result of the score replacement policy can be determined by comparing the midterm and final scores for each student with the result of the total points calculation. Got confused with the wording, I thought that they were refering to the entire class

## Question 43

Question: An online retailer uses an algorithm to sort a list of n items by price. The table below shows the approximate number of steps the algorithm takes to sort lists of different sizes. Based on the values in the table, which of the following best characterizes the algorithm for very large values of n ? A TABLE PROVODED

My Answer: **B.** The algorithm runs, but not in reasonable time.


Correct Answer: **A.** The algorithm runs in reasonable time.


Explanation: The pattern in the table appears to indicate that there are n squared steps for a list containing n items. This number of steps is a polynomial and therefore the algorithm runs in reasonable time. 

## Question 45

Question: A NAND gate is a type of logic gate that produces an output of false only when both of its two inputs are true. Otherwise, the gate produces an output of true. Which of the following Boolean expressions correctly models a NAND gate with inputs P and Q ?

My Answer: **D.** NOT (P OR Q)


Correct Answer: **C.** NOT (P AND Q)

Explanation: The expression P AND Q evaluates to true when both P and Q are true, and evaluates to false otherwise. Therefore, the expression NOT P AND Q evaluates to false when both P and Q are true, and evaluates to true otherwise. I was confused with the function of NOT outside the parenthesis

## Question 46

Question: A student wants to create an algorithm that can determine, given any program and program input, whether or not the program will go into an infinite loop for that input. The problem the student is attempting to solve is considered an undecidable problem. Which of the following is true?

My Answer: **C.** It is possible to create an algorithm that will solve the problem for all programs and inputs, but the algorithm will not run in reasonable time.


Correct Answer: **D.** It is not possible to create an algorithm that will solve the problem for all programs and inputs.


Explanation: An undecidable problem is one in which no algorithm can be constructed that always leads to a correct yes-or-no answer. I need to better understand this

## Question 50

Question: The procedure below searches for the value target in list. It returns true if target is found and returns false otherwise. Which of the following are true statements about the procedure?

- I. It implements a binary search.
- II. It implements a linear search.
- III. It only works as intended when list is sorted.

My Answer: **A.** I only


Correct Answer: **B.** II only


Explanation: The procedure implements a linear search, which sequentially compares each element of the list with the target value. The list does not need to be sorted because the procedure checks list elements until either the target is found or it reaches the end of the list. **Easy fix**.

## Question 51

Question: Which of the following is an example of symmetric encryption?

My Answer: **D.** Juan writes a message to send to Kelly and slides the message through a slot in the front of Kelly’s locker. Juan knows that Kelly has not shared her locker combination with anyone, so no one other than Kelly will be able to read the message.


Correct Answer: **B.** Finn and Gwen develop a system that maps each letter of the alphabet to a unique symbol using a secret key. Finn uses the key to write a message to Gwen where each letter is replaced with the corresponding symbol. Gwen uses the key to map each symbol back to the original letter.


Explanation: This is an example of symmetric encryption because the secret key is used for both encryption and decryption of messages. I was confused with the wording in the options, and I have to learn more about this

## Question 55

Question: A student wrote the procedure below, which is intended to ask whether a user wants to keep playing a game. The procedure does not work as intended. Which of the following best describes the result of running the procedure? CODE PROVIDED

My Answer: **A.** The procedure returns true when the user inputs the value "y" and returns false otherwise.


Correct Answer: **D.** The procedure returns false no matter what the input value is.


Explanation: The expression response =  y AND response = yes. always evaluates to false because it is not possible for the variable response to be equal to both y and yes. Therefore, the procedure will always
return false. Still need to learn more on this

## Question 58

Question: Which of the following are true statements about how the Internet enables crowdsourcing?

- I. The Internet can provide crowdsourcing participants access to useful tools, information, and professional knowledge.
- II. The speed and reach of the Internet can lower geographic barriers, allowing individuals from different locations to contribute to projects.
- III. Using the Internet to distribute solutions across many users allows all computational problems to be solved in reasonable time, even for very large input sizes.

My Answer: **C.** II and III Only


Correct Answer: **A.** I and II Only


Explanation: The Internet can provide tools, information, and knowledge to crowdsourcing participants and can lower geographic barriers to potential participants. However, there exist problems that cannot be solved in reasonable time, even with a distributed approach. Still need to gain better understaning on why it isn't III

## Question 60

Question: Which of the following are ways in which a programmer can use abstraction to manage the complexity of a program? Select two answers.

My Answer: **B. and D.** Replacing longer variable names with shorter variable names to reduce typing errors AND Replacing the string variables One word, name 1, One word, name 2, One word, name 3, and One word, name 4 with a list of strings
called names


Correct Answer: **A. and D.** Replacing each instance of repeated code with a call to a procedure


Explanation: A is the answer as Placing repeated code with procedure calls is an example of a procedural abstraction that may make it easier for a programmer to manage the complexity of a program. B is not the answer as Using shorter variable names would not help a programmer to manage the complexity of a program. In general, meaningful variable names help programmers better understand programs.

## Question 61

Question: Two different schools maintain data sets about their currently enrolled students. No individual student is enrolled at both schools. Each line of data contains information, separated by commas, about one student. The two schools would like to combine their data to make a single data set. Which of the following can be done with the combined data? East and West High School DATA PROVIDED

My Answer: **B. and C.** The schools can determine the average number of days students are absent. AND The schools can determine which ZIP code is represented by the most students.

Correct Answer: **A. and B.** The schools can create a single list of student names, sorted by last name.


Explanation: A is the answer as it is possible to create a single list of student names, sorted by last name. Both data formats provide the first and last names of each student. C is not the answer as East High School provides the ZIP code of each student, but West High School does not.

## Question 66

Question: The procedure Smallest is intended to return the least value in the list numbers. The procedure does not work as intended. CODE PROVIDED

My Answer: **B. and C.** theList = [20,10,30,40] AND theList = [30,40,20,10]

Correct Answer: **C. and D.** theList = [40,30,20,10]

Explanation: D is the answer as the procedure returns the first number it encounters that is less than the first number in the list. For the list [40,30,20,10], the procedure returns 3 0, which is not the least value in the list. B is not the answer as for the list [20,10,30,40] 10 is the first value smaller than the first number in the list, so the procedure returns the correct value 10.
