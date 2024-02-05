Credit Approval System
Project Overview:
This project is a credit approval system implemented using Django 4+ and Django Rest Framework. The system assesses credit eligibility based on historical loan data and customer information.

Table of Contents:
Project Structure
Setup and Initialization
API Endpoints
Data Models
Data Ingestion
Credit Score Calculation
Error Handling
Testing
Running the Project
Additional Information
Project Structure:
The project follows the standard Django project structure with additional components for Dockerization and Celery integration for background tasks:
App/
|--loanproject
|   |-- migrations/
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|-- customerapp
|   |-- settings.py
|-- loanapp
|-- docker/
|   |-- Django Dockerfile
|   |-- Celery Dockerfile
|   |-- docker-compose.yml
|-- manage.py
|-- requirements.txt
App: Contains the Django app with models, views, and serializers.
docker: Contains Docker-related files (Dockerfiles and docker-compose.yml).
Setup and Initialization:
Requirements:
Docker
Docker Compose
Running the Project:
1. Clone the repository:
git clone https://github.com/Pgangothri/loan_approval
cd loanproject
2. Build and run the Docker containers:
docker-compose up --build
This command will set up the Django application, PostgreSQL database, and Celery for background tasks.
3. Apply database migrations:
docker-compose exec web python manage.py migrate
4. Ingest data from provided Excel files:
docker-compose exec web python manage.py ingest_data
5. The application is now ready to use.
API Endpoints:
/register: Add a new customer to the customer table.
/check-eligibility: Check loan eligibility based on credit score.
/create-loan: Process a new loan based on eligibility.
/view-loan/loan_id: View loan details and customer details.
/view-loans/customer_id: View all current loan details by customer id.
Data Models:
Customer: Represents customer information with attributes such as customer_id, first_name, last_name, etc.
Loan: Represents past and existing loans with attributes like loan_id, loan_amount, tenure, etc.
Data Ingestion:
Use the Django management command ingest_data to populate the database with data from provided Excel files.
Credit Score Calculation:
The credit score is calculated based on historical loan data, including past loans paid on time, the number of loans taken, loan activity in the current year, and approved loan volume.
Testing:
Unit tests have been written for critical components, especially the credit approval logic.
Additional Information
This project uses Django 3.2, Django Rest Framework, and Celery for background tasks.
Ensure that Docker and Docker Compose are installed before running the project.







