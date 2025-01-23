This Django project implements a comprehensive user authentication system with features including login, signup, password management, and user profile functionality.
FEATURES:
1. User Authentication
Login with username or email
Secure password management
Authentication-based access control

2. Pages
Login Page
Sign Up Page
Forgot Password
Change Password
User Dashboard
User Profile

TECHNICAL REQUIREMENTS:
Python 3.8+
Django 5.1+

INSTALLATION:

1. Clone the repository:
   git clone <repository-url>
   cd <project-directory>

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  (# On Windows, use `venv\Scripts\activate`)

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

KEY IMPLEMENTATION DETAILS:
Uses Django's built-in authentication system
Implements custom forms and views for authentication flows
Includes email-based password reset functionality
Secure password validation and error handling
