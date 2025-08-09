# Household Service Management Platform

This project showcases my ability to design and implement a **simple, clean, efficient, and fast REST API**, ensuring seamless communication between the frontend and backend while maintaining optimal performance.

## Overview
The **Household Service Management Platform** is a web-based application designed to streamline service management for multiple user roles: **Administrators**, **Customers**, and **Professionals**. The platform provides tailored dashboards for each role, enabling efficient service booking, management, and oversight. With a responsive design and robust backend, this application is ideal for managing household or professional services.

## Features
### Admin Features
- Manage users (Customers and Professionals).
- Oversee service bookings and platform activity.
- View detailed summaries and reports.

### Customer Features
- Register and log in to access personalized dashboards.
- Book services and view booking history.
- Manage personal profiles and preferences.

### Professional Features
- Manage assigned bookings and update service statuses.
- Edit and maintain professional profiles.
- View task summaries and schedules.

### General Features
- Secure user authentication and role-based access.
- Responsive design for seamless use on mobile and desktop devices.
- Intuitive user interface powered by Bootstrap.

## Technologies Used
- **Backend**: Python (Flask Framework)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite
- **Other Tools**: Jinja2 for templating, Flask-WTF for forms

## Project Structure
## Overview
This project is a web-based application designed to manage services and users. It supports multiple user roles, including administrators, customers, and professionals, each with their own dashboards and functionalities. The application provides features such as user registration, login, profile management, and service management.

## Features
- **Admin Dashboard**: Manage users, view summaries, and oversee the platform.
- **Customer Dashboard**: Book services, view bookings, and manage profiles.
- **Professional Dashboard**: Manage services, view assigned tasks, and update profiles.
- **Authentication**: User signup and login functionality for customers and professionals.
- **Responsive Design**: Frontend styled with Bootstrap for a mobile-friendly experience.

## Project Structure
- **`app.py`**: The main entry point for the application.
- **`backend/`**: Contains backend logic, including:
  - `controllers.py`: Likely handles routing and business logic.
  - `models.py`: Defines the database models.
- **`instance/`**: Contains instance-specific files, such as the SQLite database (`household.sqlite3`).
- **`static/`**: Contains static assets like CSS, JavaScript, fonts, and images.
  - `bootstrap/`: Bootstrap CSS files.
  - `css/`: Custom stylesheets.
  - `img/`: Images used in the application.
  - `js/`: JavaScript files.
  - `summary/`: Likely contains summary-related assets.
- **`templates/`**: HTML templates for rendering views, including:
  - `index.html`: Likely the homepage.
  - `login.html`: Login page.
  - `customer_dashboard.html`: Dashboard for customers.
  - `admin_dash.html`: Dashboard for administrators.
  - `prof_dash.html`: Dashboard for professionals.
  - Other templates for user profiles, signups, and service management.

## Prerequisites
- Python 3.x
- Flask (or another Python web framework)
- SQLite (for the database)
- Flask
- SQLAlchemy 
