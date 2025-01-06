import os
import time
import requests
from prometheus_client import start_http_server, Gauge


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')


rabbitmq_individual_queue_messages = Gauge(
    'rabbitmq_individual_queue_messages', 'Total count of messages in the queue',
    ['host', 'vhost', 'name']
)
rabbitmq_individual_queue_messages_ready = Gauge(
    'rabbitmq_individual_queue_messages_ready', 'Count of ready messages in the queue',
    ['host', 'vhost', 'name']
)
rabbitmq_individual_queue_messages_unacknowledged = Gauge(
    'rabbitmq_individual_queue_messages_unacknowledged', 'Count of unacknowledged messages in the queue',
    ['host', 'vhost', 'name']
)

def fetch_queue_data():
    url = f'http://{RABBITMQ_HOST}:15672/api/queues'
    response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
    if response.status_code != 200:
        raise Exception(f"Failed to fetch queue data: {response.status_code} {response.text}")
    return response.json()

def update_metrics():
    try:
        queues = fetch_queue_data()
        for queue in queues:
            host = RABBITMQ_HOST
            vhost = queue['vhost']
            name = queue['name']
            messages = queue['messages']
            messages_ready = queue['messages_ready']
            messages_unacknowledged = queue['messages_unacknowledged']

            rabbitmq_individual_queue_messages.labels(host, vhost, name).set(messages)
            rabbitmq_individual_queue_messages_ready.labels(host, vhost, name).set(messages_ready)
            rabbitmq_individual_queue_messages_unacknowledged.labels(host, vhost, name).set(messages_unacknowledged)
    except Exception as e:
        print(f"Error updating metrics: {e}")

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus exporter started on port 8000")

    while True:
        update_metrics()
        time.sleep(30)