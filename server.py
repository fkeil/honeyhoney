from quart import Quart, request, render_template
import logging

app = Quart(__name__)

# Configure logging to save the data to a file and print to console
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s')

log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
log_console_handler.setFormatter(formatter)

app.logger.addHandler(log_console_handler)

@app.route('/', methods=['GET', 'POST'])
async def login():
    if request.method == 'POST':
        # Get all available information about the client
        client_info = {
            'client_ip': request.remote_addr,
            'user_agent': request.headers.get('User-Agent'),
            'referrer': request.headers.get('Referer'),
            'form_data': await request.form,
            'args': request.args,
            'cookies': request.cookies
        }

        # Log the collected data to file
        log_message = f"Client Information: {client_info}"
        logging.info(log_message)

        # Print the collected data to console
        print(log_message)

        # Refresh the page after logging
        return await render_template('login.html')

    # Render the login page template for GET requests
    return await render_template('login.html')

if __name__ == '__main__':
    # Run the app with Uvicorn using the import string
    import uvicorn
    uvicorn.run("your_filename:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
