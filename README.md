
# To-Do List API Project

This is a Django-based To-Do List API application, allowing users to create, read, update, and delete their tasks. The project utilizes the Django REST Framework (DRF) for API development and includes advanced features like filtering, searching, ordering, and authentication for secure access to tasks.

## **Project Structure**

Here's an overview of the main components in this project:

```
To_Do_List/
│
├── db.sqlite3               # SQLite database file for local development
├── manage.py                # Django's command-line utility for project management
├── tasks/                   # Main app containing the core logic
│   ├── permissions.py       # Custom permissions for secure access to tasks
│   ├── serializers.py       # DRF serializers for data validation and transformation
│   ├── views.py             # API views for handling task operations (CRUD)
│   ├── urls.py              # URL routes for task-related API endpoints
│   ├── models.py            # Django models defining the Task schema
│   ├── tests.py             # Unit tests for the API functionality
│   ├── signals.py           # Signal handling for task-related events
│   └── ...                  # Other standard Django app files
│
├── To_Do_List/              # Project configuration folder
│   ├── settings.py          # Project-wide settings and configurations
│   ├── urls.py              # Main URL routing file
│   └── ...                  # Other standard Django project files
```

## **Features**

- **CRUD Operations**: Create, Read, Update, and Delete tasks using the API endpoints.
- **Authentication**: Secure access to task operations using Django's authentication system.
- **Permissions**: Custom permissions to ensure only the owner of a task can modify or delete it.
- **Filtering, Searching, and Ordering**: Filter tasks by due date and user, search through task titles and descriptions, and order tasks by creation or due date.
- **Throttling**: Rate-limiting on requests to prevent abuse.

## **Installation and Setup**

### **Prerequisites**

- Python 3.x
- Virtualenv (recommended)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/id-sidhu/To_Do_List-Api.git
cd To_Do_list-Api
cd To_Do_List
```

### **Step 2: Create a Virtual Environment**

It's recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**

Make sure to have `pip` installed, then run:

```bash
pip install -r requirements.txt
```

> **Note**: If `requirements.txt` is not working, manually install dependencies like Django and Django REST Framework:
```bash
pip install django djangorestframework django-filter
```

### **Step 4: Run Migrations**

Apply the migrations to set up the database schema.

```bash
python manage.py migrate
```

### **Step 5: Create a Superuser**

To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

### **Step 6: Run the Server**

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the application.

## **Usage**

### **API Endpoints**

The main endpoints of the To-Do List API are as follows:

- **GET /tasks/tasks**: Retrieve all tasks (with filtering, searching, and ordering support).
- **POST /tasks/tasks**: Create a new task.
- **GET /tasks/tasks/<id>/**: Retrieve details of a specific task.
- **PUT /tasks/tasks/<id>/**: Update an existing task.
- **DELETE /tasks/tasks/<id>/**: Delete a specific task.

### **Authentication**

Most endpoints require authentication. Use the `/admin/` panel to manage users or generate tokens if using token-based authentication.

### **Admin Panel**

Access the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage tasks and users. Ensure you have created a superuser to log in.

## **Testing**

To run the tests, use Django's test command:

```bash
python manage.py test tasks
```

This will execute all unit tests defined in `tasks/tests.py`.

## **Contributing**

Contributions are welcome! Please fork the repository and create a pull request with your changes.
