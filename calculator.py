# calculator.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

template = '''
<h2>Basic Calculator</h2>
<form method="POST">
    Number 1: <input name="num1"><br>
    Operator: <select name="op">
        <option>+</option>
        <option>-</option>
        <option>*</option>
        <option>/</option>
    </select><br>
    Number 2: <input name="num2"><br>
    <input type="submit" value="Calculate">
</form>
{% if result is not none %}
<p>Result: {{ result }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.form['num1'])
            n2 = float(request.form['num2'])
            op = request.form['op']
            if op == '+': result = n1 + n2
            elif op == '-': result = n1 - n2
            elif op == '*': result = n1 * n2
            elif op == '/': result = n1 / n2
        except:
            result = "Error!"
    return render_template_string(template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
