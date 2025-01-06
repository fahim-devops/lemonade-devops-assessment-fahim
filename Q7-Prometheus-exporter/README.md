# RabbitMQ Prometheus Exporter

This Prometheus exporter connects to the RabbitMQ HTTP API and periodically reads the following information about all queues in all vhosts:
- Total count of messages (`messages`)
- Count of ready messages (`messages_ready`)
- Count of unacknowledged messages (`messages_unacknowledged`)

It then exports the following metrics:
- `rabbitmq_individual_queue_messages{host,vhost,name}`
- `rabbitmq_individual_queue_messages_ready{host,vhost,name}`
- `rabbitmq_individual_queue_messages_unacknowledged{host,vhost,name}`

where `host` is the RabbitMQ hostname, `vhost` is the RabbitMQ vhost, and `name` is the name of the queue.

## Prerequisites

- Python 3.x
- RabbitMQ with the management plugin enabled
- Prometheus server

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/rabbitmq-prometheus-exporter.git
   cd rabbitmq-prometheus-exporter

## Installation

Install the required dependencies:
```
pip install -r requirements.txt 
```

## Set the environment variables:

```
export RABBITMQ_HOST=localhost
export RABBITMQ_USER=rabbitmq
export RABBITMQ_PASSWORD=rabbitmq123
```

## Running the Exporter

```
python exporter.py
```

The exporter will start an HTTP server on port 8000 by default and expose the metrics for Prometheus to scrape.

## Configuration
The exporter uses the following environment variables for configuration:

RABBITMQ_HOST: The hostname of the RabbitMQ server.
RABBITMQ_USER: The username for RabbitMQ HTTP API authentication.
RABBITMQ_PASSWORD: The password for RabbitMQ HTTP API authentication.

Prometheus Configuration
Add the following job to  Prometheus configuration file (prometheus.yml):

```
scrape_configs:
  - job_name: 'rabbitmq'
    static_configs:
      - targets: ['localhost:8000']

```

Adjust the targets field to match the host and port where the exporter is running.

Example Metrics
The exporter will expose metrics similar to the following:

```
rabbitmq_individual_queue_messages{host="rabbitmq.example.com",vhost="/",name="queue1"} 10
rabbitmq_individual_queue_messages_ready{host="rabbitmq.example.com",vhost="/",name="queue1"} 5
rabbitmq_individual_queue_messages_unacknowledged{host="rabbitmq.example.com",vhost="/",name="queue1"} 2
```

## Troubleshooting
Ensure that the RabbitMQ management plugin is enabled and accessible.
Verify the environment variables are correctly set.
Check the logs for any error messages or issues.