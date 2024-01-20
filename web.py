# web.py

from flask import Flask
import threading
import time
import asyncio
from bot import main

app = Flask(__name__)

@app.route('/')
def home():
    return f'Server for {bot_name}'

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    # Start the Flask app and bot in separate threads
    server_thread = threading.Thread(target=run)
    server_thread.start()

    asyncio.run(main())

    @app.route('/uptime-robot')
    def uptime_robot():
        return 'Uptime Robot - Keep alive!'

    while True:
        print("Keepalive check.")
        time.sleep(60)
