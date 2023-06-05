## Table of Contents

- [Cart functionality](#cart-functionality)
- [Authentication system](#authentication-system)
- [OTP code login](#otp-code-login)
- [Single page user profile](#single-page-user-profile)
- [Other functionalities](#other-functionalities)



##Cart functionality
Users are able to add products to their cart without logging in, but in order to submit the cart, a user account and login is required. Cart functionality is mainly handled on the front-end by saving product IDs within a cookie named "cart". When a user attempts to submit their cart, the product IDs and their respective quantities are sent to a Django REST framework view in a JSON format via AJAX. If the cart submission is successful, an order will be created and stored in the database.

##Authentication system
In this project, we have implemented a customized authentication system using JWT tokens, rather than using Django's built-in authentication system. These tokens are generated using the Jose library and are stored within cookies. A middleware is used to verify that the user is logged in by checking these cookies.

##OTP code login
Users can log in to the platform using an OTP(One time password) code that is sent to their preferred email or phone number. The code is generated using Python's random library and is saved to a Redis database, along with the user's information. The OTP codes are sent via email using Django's "send email" functionality, or alternatively via SMS using the Kavenegar API.

##Single page user profile
Upon logging into the website, users are granted access to their personalized profile page, which is created through the use of Django Rest framework on the backend and jQuery on the front-end. Through this page, users are able to edit their personal information, view their previous orders, and add or remove existing addresses as needed.

##Other functionalities
The platform also offers several additional features, such as a tree-based category system that allows for the creation of endless child categories through the use of self-relations. Additionally, there are three distinct user roles available: a product manager role, which can add and remove products; an operator role, which is responsible for order management; and a supervisor role, which has access to all administrative panels but cannot make edits to the system.Sales models are also there to help with creating difrent offers.