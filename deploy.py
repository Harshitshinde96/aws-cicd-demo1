import os
import paramiko
import io
import sys
import warnings

# Suppress the harmless CryptographyDeprecationWarning from Paramiko
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

host = os.environ.get("EC2_HOST")
username = os.environ.get("EC2_USERNAME")
private_key = os.environ.get("PRIVATE_KEY")

if not all([host, username, private_key]):
    print("Error: Missing required environment variables.")
    sys.exit(1)

print(f"Starting Deployment to {host}...")

try:
    key = paramiko.RSAKey.from_private_key(io.StringIO(private_key))
except Exception as e:
    print(f"Error parsing private key: {e}")
    sys.exit(1)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=host, username=username, pkey=key)
    print("SSH Connection Established Successfully.")

    # UPDATED COMMANDS: Idempotent execution (Clones if missing, Pulls if exists)
    # Be sure to replace YOUR_GITHUB_USERNAME below!
    commands = [
        # Notice the 2>&1 added to the end of the git commands
        "if [ ! -d '/home/ec2-user/aws-python-deployment-demo' ]; then git clone https://github.com/Harshitshinde96/aws-cicd-demo1.git /home/ec2-user/aws-python-deployment-demo 2>&1; fi",
        "cd /home/ec2-user/aws-python-deployment-demo && git pull origin main 2>&1",
        "cd /home/ec2-user/aws-python-deployment-demo && python3 app.py"
    ]

    for command in commands:
        print(f"\nExecuting: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        
        if out:
            print(out)
        if err:
            print(f"WARNING/ERROR: {err}")
            
        # FIX FOR THE 'NONETYPE' CRASH: Explicitly close the streams
        stdin.close()
        stdout.close()
        stderr.close()

    print("\nDeployment Completed Successfully!")

except Exception as e:
    print(f"Deployment Failed: {e}")
    sys.exit(1)
finally:
    client.close()
