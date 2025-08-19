import webbrowser
from threading import Timer
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid operation"

# HTML template as a string
html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple Calculator</title>
</head>
<body>
  <h2>Calculator</h2>
  <form method="post">
    Number 1: <input type="number" step="any" name="num1" required><br><br>
    Number 2: <input type="number" step="any" name="num2" required><br><br>
    Operation:
    <select name="operation" required>
      <option value="add">Add</option>
      <option value="subtract">Subtract</option>
      <option value="multiply">Multiply</option>
      <option value="divide">Divide</option>
    </select><br><br>
    <input type="submit" value="Calculate">
  </form>

  {% if result is not none %}
    <h3>Result: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]
            result = calculate(num1, num2, operation)
        except ValueError:
            result = "Invalid input! Please enter valid numbers."
    return render_template_string(html, result=result)

if __name__ == "__main__":
    # Open the browser after a short delay
    Timer(1, open_browser).start()
    app.run(debug=True)
