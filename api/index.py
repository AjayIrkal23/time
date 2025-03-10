from datetime import datetime, timedelta

def handler(request):
    now = datetime.now()
    last_24_hours = now - timedelta(hours=24)

    formatted_now = now.strftime("%d %B %H:%M")
    formatted_last_24 = last_24_hours.strftime("%d %B %H:%M")

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Last 24 Hours</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: Arial, sans-serif;
                background: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color:black;
                text-align: center;
            }}
            .container {{
                font-size: 24px;
                color: white;
                border-radius: 10px;
            }}
        </style>
        <script>
            setTimeout(() => {{
                window.location.reload();
            }}, 60000);
        </script>
    </head>
    <body>
        <div class="container">
            <strong>{formatted_last_24}</strong> - <strong>{formatted_now}</strong>
        </div>
    </body>
    </html>
    """

    return Response(html_template, status=200, content_type='text/html')
