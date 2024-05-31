# Subjects-Enrollment-System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Subject Enrollment System** repository! This project is designed to manage and streamline the process of enrolling students in various subjects, featuring a user-friendly GUI built with Python.

## Features

- **User-Friendly GUI**: Intuitive and easy-to-use graphical user interface built with Python.
- **Student Registration and Login**: Allows students to register for an account and log in securely.
- **Password Management**: Students can change their passwords after logging in to ensure account security.
- **Subject Enrollment**: Enables students to enroll in subjects, view their current enrollments, and edit them as needed.
- **Administrative Access**: Teachers can enter the system as administrators to manage student data.
- **Student Management**: Administrators can organize students based on specific conditions and criteria.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:
   - Open your terminal and run the following command to clone the repository.
2. **Install dependencies**:
   - Install the required Python packages.
3. **Configure the application**:
   - Ensure the configuration settings in your Python files match your local setup.
4. **Run the application**:
   - Start the application by running the university Python file.

## Usage

### University System

1. **Student Menu**:
   - Students can access the student menu to perform various functions.
2. **Admin Menu**:
   - Admins can access the admin menu to perform administrative tasks.
3. **Browsing**:
   - Students and Admins can browse between menus.
4. **Matching I/O**:
   - Ensure I/O wording, coloring, and indentation match the sample provided.

### Student System

1. **Register a new student**:
   - Students can register, and their data is saved to a file.
2. **Log in**:
   - Students can log in, and their data is read from the file.
3. **RegEx for login and register**:
   - Use regular expressions for validating login and registration.
4. **Error Handling**:
   - Handle exceptions, errors, and logical scenarios appropriately.
5. **Matching I/O**:
   - Ensure I/O wording, coloring, and indentation match the sample provided.

### Student Course System

1. **Enroll in subjects**:
   - Students can enroll in a maximum of 4 subjects.
2. **Tracking**:
   - Subject enrollment is tracked.
3. **Remove a subject**:
   - Students can remove a subject by ID.
4. **Show subjects**:
   - Display the list of enrolled subjects.
5. **Change password**:
   - Students can change their password.
6. **Read/Write to file**:
   - Student and subject data are read from and written to a file.
7. **Error Handling**:
   - Handle exceptions, errors, and logical scenarios appropriately.
8. **Matching I/O**:
   - Ensure I/O wording, coloring, and indentation match the sample provided.

### Admin System

1. **Show students**:
   - Admins can list all students.
2. **Group students**:
   - Admins can group students according to their grades.
3. **Partition students**:
   - Admins can partition students as Pass/Fail.
4. **Remove a student**:
   - Admins can remove a student by ID.
5. **Clear file**:
   - Admins can remove all students and clear the file.
6. **Read/Write to file**:
   - Admins can read and write student and subject data from/to a file.
7. **Error Handling**:
   - Handle exceptions, errors, and logical scenarios appropriately.
8. **Matching I/O**:
   - Ensure I/O wording, coloring, and indentation match the sample provided.

### GUI Application (GUIUniApp)

1. **Login window**:
   - The login window works, and upon login, students are taken to the enrollment window using data from `students.data`.
2. **Enrollment window**:
   - Allows students to add subjects (maximum 4).
3. **Subjects window**:
   - Displays enrolled subjects in the subjects window.
4. **Exception window**:
   - Handles incorrect format exceptions and maximum 4 subjects exception.

## Configuration

The application saves student information in a file named `student.data`. Ensure that this file is correctly placed and accessible by the application.

## Contributing

Contributions are welcome! 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
