# To-Do List

## Description
This is a simple To-Do List web application built with Django. It allows users to manage tasks by creating, updating, deleting, and marking them as complete or incomplete. Tasks can also be categorized using tags.

## Features
- Add, update, delete tasks
- Mark tasks as complete/incomplete
- Set deadlines for tasks (optional)
- Organize tasks using tags
- Sidebar navigation for easy access to pages
- Tasks are ordered from incomplete to complete and newest to oldest
- Fully functional tag management

## Installation

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dkornit/todo-list
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the project in your browser at:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
### Home Page (http://127.0.0.1:8000/)
- Displays all tasks in order of priority (incomplete first, then complete, from newest to oldest).
- Allows adding, updating, deleting, and marking tasks as complete/incomplete.

### Tag List Page (http://127.0.0.1:8000/tags/)
- Displays a list of tags.
- Allows adding, updating, and deleting tags.

## Models
### Task
- `content` (str): Task description.
- `created_at` (datetime): Timestamp when the task was created.
- `deadline` (datetime, optional): Deadline for the task.
- `is_done` (bool): Marks whether the task is completed or not.
- `tags` (many-to-many): Related tags.

### Tag
- `name` (str): Tag name.

## Development Workflow
1. Create a new GitHub public repository.
2. Switch to the `dev` branch:
   ```bash
   git checkout -b dev
   ```
3. Implement the project.
4. Create a Pull Request (PR) from `dev` to `main`.
5. Attach screenshots of all pages directly in the PR.
6. Submit the PR link as the solution.
