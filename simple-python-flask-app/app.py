from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory list to store messages (resets when container restarts)
messages = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Interactive App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f0f4f8;
            color: #333;
        }
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; }
        input[type=text] {
            padding: 8px;
            width: 70%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 8px 16px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover { background-color: #2980b9; }
        ul { line-height: 1.8; }
        li { background-color: #ecf6ff; padding: 5px 10px; border-radius: 5px; margin-bottom: 5px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Flask Message Board</h1>
        <form method="POST" action="/add">
            <input type="text" name="message" placeholder="Type a message..." required>
            <button type="submit">Add</button>
        </form>

        <h2>Messages ({{ count }})</h2>
        <ul>
            {% for msg in messages %}
                <li>{{ msg }}</li>
            {% endfor %}
        </ul>

        <form method="POST" action="/clear">
            <button type="submit">Clear All</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE, messages=messages, count=len(messages))

@app.route('/add', methods=['POST'])
def add_message():
    msg = request.form.get('message')
    if msg:
        messages.append(msg)
    return home()

@app.route('/clear', methods=['POST'])
def clear_messages():
    messages.clear()
    return home()

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)