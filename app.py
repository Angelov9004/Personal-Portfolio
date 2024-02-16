from flask import Flask, render_template, request
from services import date_time
from services import smtp

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            user_data = request.form.to_dict()
            smtp.send_email(user_data)
            message = "Your message is submitted, You've sent it on"
            time = date_time.time()
            return render_template('success.html', message=message +" "+ time)
        except Exception as e:
            message = f"An error occurred: {str(e)}"
            return render_template('success.html', message=message)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)