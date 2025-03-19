# TaskByte

TaskByte is a web-based to-do list application built using Django, Jinja2, and Bootstrap. It is designed to help users efficiently manage their tasks with a simple and intuitive interface. The application is hosted on Koyeb and utilizes a PostgreSQL database, which is also hosted on the same web service.

You can access the live site at [TaskByte Website](https://itchy-shayne-taskbyte-be317291.koyeb.app/)

## Features
- Add, edit, and delete tasks
- Mark tasks as complete/incomplete
- Prioritize tasks for better organization
- Responsive design with Bootstrap
- User-friendly interface powered by Jinja2 templating

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** Jinja2, Bootstrap
- **Database:** PostgreSQL (default, can be configured for other databases)

## Installation for localhost

### Prerequisites
- Python 3.x installed
- pip package manager
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/taskbyte.git
   cd taskbyte
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Open your browser and visit `http://127.0.0.1:8000/` to use TaskByte.

## Usage
- Login/Register first and then navigate to the ToDos page to view your task list.
- Use the provided buttons to add, edit, or delete tasks.
- Tasks can be marked as completed or pending.


## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

