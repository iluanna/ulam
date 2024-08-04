from flask import Flask, request, render_template_string
from encoder_decoder import EnDec

app = Flask(__name__)
endec = EnDec()


def render_form(result=None, error=None, activity=''):
    return render_template_string('''
        <form method="post">
            <input type="text" name="user_input" placeholder="Enter text to {{ activity }}">
            <input type="submit" value="Submit">
        </form>
        {% if result %}
            <p>Result: {{ result }}</p>
        {% elif error %}
            <p style="color:red;">Error: {{ error }}</p>
        {% endif %}
    ''', result=result, error=error, activity=activity)


@app.route('/v1/encode', methods=['GET', 'POST'])
def encode():
    activity = "encode"
    if request.method == 'POST':
            user_input = request.form['user_input']
            try:
                result = endec.encode_text(user_input)
                return render_form(result=result, activity=activity)
            except Exception as e:
                error = str(e)
                return render_form(error=error, activity=activity)
    return render_form(activity=activity)


@app.route('/v1/decode', methods=['GET', 'POST'])
def decode():
    activity = "decode"
    if request.method == 'POST':
            user_input = request.form['user_input']
            user_input = user_input.replace('\\n', '\n')
            try:
                result = endec.decode_text(user_input)
                return render_form(result=result, activity=activity)
            except Exception as e:
                error = str(e)
                return render_form(error=error, activity=activity)
    return render_form(activity=activity)


if __name__ == '__main__':
    app.run(debug=True)
