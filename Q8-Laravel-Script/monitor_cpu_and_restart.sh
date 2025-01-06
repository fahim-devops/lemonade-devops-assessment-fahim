#!/bin/bash

# Function to get the current CPU usage
get_cpu_usage() {
    cpu_usage=$(mpstat 1 1 | awk '/Average:/ {print 100 - $NF}')
    echo $cpu_usage
}

# Function to restart the Laravel backend service
restart_laravel_service() {
    echo "CPU usage is above 80%. Restarting Laravel backend service..."
    sudo systemctl restart laravel-backend
    echo "Laravel backend service restarted."
}

# Main loop to monitor CPU usage
while true; do
    cpu_usage=$(get_cpu_usage)
    echo "Current CPU usage: $cpu_usage%"

    # Check if CPU usage exceeds 80%
    if (( $(echo "$cpu_usage > 80" | bc -l) )); then
        restart_laravel_service
    fi

    sleep 60
done