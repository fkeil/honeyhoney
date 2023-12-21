from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Configure logging to save the data to a file and print to console
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s')

#log_file_handler = logging.FileHandler('honeypot.log')
log_console_handler = logging.StreamHandler()

#log_file_handler.setLevel(logging.INFO)
log_console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')

#log_file_handler.setFormatter(formatter)
log_console_handler.setFormatter(formatter)

#app.logger.addHandler(log_file_handler)
app.logger.addHandler(log_console_handler)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get all available information about the client
        client_info = {
            'client_ip': request.remote_addr,
            'user_agent': request.user_agent.string,
            'referrer': request.referrer,
            'form_data': request.form,
            'args': request.args,
            'cookies': request.cookies
        }

        # Log the collected data to file
        log_message = f"Client Information: {client_info}"
        logging.info(log_message)

        # Print the collected data to console
        print(log_message)

        # Refresh the page after logging
        return render_template('login.html')

    # Render the login page template for GET requests
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
