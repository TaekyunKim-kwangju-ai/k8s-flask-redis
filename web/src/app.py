import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)
HOST_NAME = os.getenv('HOSTNAME')

@app.route('/')
def index():
    r.incr('visit_count')
    visit_count = r.get('visit_count').decode('utf-8')
    return f'{HOST_NAME}, 웹 페이지 방문 횟수: {visit_count}회'

if __name__ == '__main__':
    app.run()