
# Personal Expense Tracker

## Overview
Personal Expense Tracker is a full-stack web application designed to help users track and manage their personal expenses. Built with Django, React, and Docker, this application features a user-friendly interface for expense management, category organization, and data visualization.

## Features
- **User Authentication**: Secure login and registration system.
- **Expense Tracking**: Users can add, view, update, and delete expenses.
- **Category Management**: Organize expenses into customizable categories.
- **Data Visualization**: Visual representation of expenses for easy analysis.
- **Responsive Design**: Mobile-friendly interface for on-the-go access.

## Technology Stack
- **Backend**: Django (Python)
- **Frontend**: React (JavaScript)
- **Database**: SQLite
- **Containerization**: Docker
- **Deployment**: AWS Elastic Beanstalk

## Getting Started

### Prerequisites
- Docker
- Node.js
- Python

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/expense-tracker.git```

2. Navigate to the project directory:
   ```sh
   cd expense-tracker```

3. Build and run the Docker containers:

sh
Copy code
docker-compose up --build
Usage
After starting the application, navigate to http://localhost:3000 to access the React frontend, and http://localhost:8000 for the Django backend API (adjust the ports as necessary).

Testing
To run the unit tests for the Django backend:

sh
Copy code
docker exec -it backend-container python manage.py test
For the React frontend tests:

sh
Copy code
cd frontend
npm test
Deployment
For deployment on AWS Elastic Beanstalk, follow the AWS Elastic Beanstalk Documentation.

Contributing
Contributions are welcome! Please read our Contributing Guide for details on our code of conduct and the process for submitting pull requests to us.

License
This project is licensed under the MIT License.

Acknowledgments
Icons and images provided by FontAwesome
React framework by Facebook
Django framework by Django Software Foundation
Contact
Your Name - email@example.com

Project Link: https://github.com/yourusername/expense-tracker
