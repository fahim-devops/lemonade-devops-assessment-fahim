# Laravel Backend Service Monitor

This script monitors the CPU usage on a server and restarts the Laravel backend service if the CPU usage exceeds 80%. It is useful for ensuring the stability and performance of your Laravel application.

## Prerequisites

- Bash
- `mpstat` command (part of the `sysstat` package)
- `systemctl` command

## Installation

1. **Install the necessary tools:**

   Ensure that the `sysstat` package is installed on your system to use the `mpstat` command:

   ```
   sudo apt-get update
   sudo apt-get install sysstat
    ```

Ensure that systemctl is available to manage services.

Make the script executable:
```
chmod +x monitor_cpu_and_restart.sh
```

## Usage
Run the script:
```
./monitor_cpu_and_restart.sh
```
The script will start monitoring the CPU usage and will restart the Laravel backend service if the CPU usage exceeds 80%.

## Configuration
Service Name: Replace 'laravel-backend' in the script with the actual name of your Laravel service if it differs.


## Example
Here is an example of the script output when the CPU usage exceeds 80%:

```
Current CPU usage: 75.5%
Current CPU usage: 82.3%
CPU usage is above 80%. Restarting Laravel backend service...
Laravel backend service restarted.
```

## Troubleshooting

Ensure that the sysstat package is installed and the mpstat command is available.
Verify that the systemctl command is available and that you have the necessary permissions to restart the service.
Check the service name in the script and ensure it matches your Laravel service name.
