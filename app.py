from flask import Flask, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def show_last_24_hours():
    now = datetime.now()
    last_24_hours = now - timedelta(hours=24)

    formatted_now = now.strftime("%d %B %H:%M")
    formatted_last_24 = last_24_hours.strftime("%d %B %H:%M")

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Last 24 Hours</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: Arial, sans-serif;
                background: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color:black;
                text-align: center;
            }
            .container {
                font-size: 24px; /* Scales with viewport width */
                color: white;
                border-radius: 10px;
            }
        </style>
        <script>
            setTimeout(() => {
                window.location.reload();
            }, 60000); // Refresh every 60 seconds
        </script>
    </head>
    <body>
        <div class="container">
            <strong>{{ formatted_last_24 }}</strong> - <strong>{{ formatted_now }}</strong>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, formatted_now=formatted_now, formatted_last_24=formatted_last_24)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

