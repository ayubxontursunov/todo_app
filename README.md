# Todo App

<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" alt="Django Logo" width="100"/>

A simple and intuitive web application for managing your daily tasks. This Django-based app allows you to add, view, and delete tasks with ease.

## Features

- **Add Tasks**: Create new tasks with a title and description.
- **View Tasks**: Display a list of all tasks ordered by date.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Responsive Design**: Clean and modern UI with Bootstrap.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/) (included via CDN)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
   ```

2. **Install Dependencies**
```sh
pip install django
```

3. **Apply Migrations**

```sh
python manage.py migrate
```

4. **Run the Server**

```sh
python manage.py runserver
```

## Usage
1. Access the Application
 - Open your web browser and navigate to `http://127.0.0.1:8000/`.

2. Add a Task

 - Fill out the form with the task details and click 'Submit'.

3. Delete a Task
 - Click the remove button next to the task you want to delete.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
