# 🏦 Bank Management System

A command-line based Bank Management System built using Python. This project allows users to perform basic banking operations such as account creation, deposits, withdrawals, account updates, and account deletion. Account data is stored persistently using a JSON file, ensuring that information remains available even after the program is closed.

## Features

* Create a new bank account
* Deposit money into an account
* Withdraw money from an account
* View account details
* Update account information
* Delete an account
* Random account number generation
* JSON-based data storage

## Concepts Used

* Object-Oriented Programming (OOP)
* Classes and Objects
* Class Methods
* Private Methods
* File Handling
* JSON Data Management
* Exception Handling
* List Comprehensions
* Random Module
* Pathlib Module

## How It Works

User account information is stored in a JSON file as key-value pairs. When the program starts, the stored data is loaded from the file. Any changes made through banking operations are automatically updated and saved back to the JSON database.

The project uses a `Bank` class to organize all banking functionalities in a structured manner. Private methods are used for internal operations such as updating the database and generating account numbers, while class methods help perform tasks that are shared across all instances of the class.

## Future Improvements

* Transaction History
* PIN Encryption
* Account Search Functionality
* Interest Calculation
* SQLite Database Integration
* Graphical User Interface (GUI)
