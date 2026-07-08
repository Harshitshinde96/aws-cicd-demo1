import os
import paramiko
import io
import sys

# 1. Fetch Secrets from GitHub Actions Environment
host = os.environ.get("EC2_HOST")
username = os.environ.get("EC2_USERNAME")
private_key = os.environ.get("PRIVATE_KEY")

if not all([host, username, private_key]):
    print("Error: Missing required environment variables (EC2_HOST, EC2_USERNAME, PRIVATE_KEY).")
    sys.exit(1)

print(f"Starting Deployment to {host}...")

# 2. Load the private key from string memory securely
try:
    key = paramiko.RSAKey.from_private_key(io.StringIO(private_key))
except Exception as e:
    print(f"Error parsing private key: {e}")
    sys.exit(1)

# 3. Initialize SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 4. Connect to EC2
    client.connect(hostname=host, username=username, pkey=key)
    print("SSH Connection Established Successfully.")

    # 5. Define Commands to run on the server
    commands = [
        "cd /home/ec2-user/aws-python-deployment-demo",
        "git pull origin main",
        "python3 app.py"
    ]

    # 6. Execute Commands
    for command in commands:
        print(f"\nExecuting: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        
        # Read standard output and error streams
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        
        if out:
            print(out)
        if err:
            print(f"WARNING/ERROR: {err}")

    print("\nDeployment Completed Successfully!")

except Exception as e:
    print(f"Deployment Failed: {e}")
    sys.exit(1)
finally:
    client.close()
