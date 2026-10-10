Title: The Amusement Park Ticket Classifier

Problem Statement:

You are hired by a local amusement park to write a Python function named calculate_ticket_price that decides how much a visitor pays for admission based on their age, whether it is a weekend, and if they have a local discount coupon.

The park's rules are as follows:
Base Ticket Prices:
Children (under 12 years old): $10
Adults (ages 12 to 64): $20
Seniors (age 65 and older): $12

Weekend Surcharge:
If it is a weekend (is_weekend = True), add $5 to the ticket price for everyone except seniors (seniors do not pay weekend surcharges).

Local Discount Coupon:
If the visitor has a local coupon (has_coupon = True), subtract $3 from their total ticket price, but the price can never go below $0.

Invalid Inputs:
If the age is less than 0, print "Invalid age!" and return -1.
Write a function calculate_ticket_price(age, is_weekend, has_coupon) that takes these three inputs and returns the final ticket price as a number.

Component 2: Explanation of Assessment

This homework problem is designed to assess a student's ability to combine conditional statements (if, elif, else) with multiple variables and boolean logic. It poses a realistic real-world scenario where multiple conditions interact with each other, requiring the learner to carefully track how age, weekend status, and coupons change a single starting price step by step.
I anticipate the most challenging part for students will be handling the exceptions correctly—specifically making sure seniors do not get charged the weekend surcharge, and ensuring that a price does not drop below $0 if someone has a coupon. By overcoming this difficulty, students will learn how to structure nested conditionals logically without accidentally skipping or double-counting rules.
