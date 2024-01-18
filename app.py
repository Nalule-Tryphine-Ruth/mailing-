from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'your_smtp_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = 'email@gmail.com'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')


    msg = Message('Thanks for subscribing!', recipients=[email])
    msg.body = 'Welcome to the mailing list for upcoming artists. We appreciate your support!'
    
    try:
        mail.send(msg)
        flash('Subscription successful! Thank you for joining.')
    except Exception as e:
        flash(f'Subscription failed. Error: {str(e)}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
