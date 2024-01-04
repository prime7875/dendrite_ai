from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder="templates")
# Sample data for initial testing
todos = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description for Task 1',
        'time': '10:00 AM'
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description for Task 2',
        'time': '2:30 PM'
    }
]

# Route to list all To-Do items
@app.route('/')
def list_todos():
    return render_template('list_todos.html', todos=todos)

# Route to add a new To-Do
@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        new_todo = {
            'id': len(todos) + 1,
            'title': request.form['title'],
            'description': request.form['description'],
            'time': request.form['time']
        }
        todos.append(new_todo)
        return redirect(url_for('list_todos'))
    return render_template('add_todo.html')

# Route to delete a To-Do
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('list_todos'))

# Route to edit a To-Do
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if request.method == 'POST':
        todo['title'] = request.form['title']
        todo['description'] = request.form['description']
        todo['time'] = request.form['time']
        return redirect(url_for('list_todos'))
    return render_template('edit_todo.html', todo=todo)

if __name__ == '__main__':
    app.run(debug=True)
