from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Configure logging to save the data to a file
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Log the collected data
        log_data = f"Username: {username}, Password: {password}"
        logging.info(log_data)

        # Refresh the page after logging
        return render_template('login.html')

    # Render the login page template for GET requests
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
