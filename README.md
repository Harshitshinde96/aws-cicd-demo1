# AWS CI/CD Python Deployment Demo

This repository demonstrates an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python application to an AWS EC2 instance using GitHub Actions.

## Project Overview

The project contains a simple Python application (`app.py`) that reads student data from a JSON file (`students.json`) and processes it. The main goal of this repository, however, is to demonstrate automated deployments to an AWS EC2 instance.

Whenever a push is made to the `main` branch, a GitHub Actions workflow triggers a deployment script (`deploy.py`) that securely connects to an AWS EC2 instance via SSH and runs the latest version of the application.

## Key Components

- **`app.py`**: The core application logic. It parses `students.json` to find and print specific student data.
- **`deploy.py`**: A Python script utilizing the `paramiko` library to establish an SSH connection to an AWS EC2 instance, clone/pull the latest code from the repository, and execute `app.py`.
- **`requirements.txt`**: Lists the project dependencies (i.e., `paramiko`).
- **`.github/workflows/python-app.yml`**: The GitHub Actions workflow file that sets up the Python environment, installs dependencies, and executes `deploy.py` securely using GitHub Secrets.

## Setup Instructions

To replicate or use this CI/CD pipeline, follow these steps:

### 1. AWS EC2 Setup
1. Launch an AWS EC2 instance (e.g., Amazon Linux 2023 or Ubuntu).
2. Ensure the instance has a Security Group allowing SSH (Port 22) access from GitHub Actions IP ranges or everywhere (0.0.0.0/0).
3. Make sure Python 3 and `git` are installed on the EC2 instance.

### 2. GitHub Secrets Configuration
In your GitHub repository, navigate to **Settings** > **Secrets and variables** > **Actions** and add the following repository secrets:
- `EC2_HOST`: The public IP address or DNS name of your EC2 instance.
- `EC2_USERNAME`: The SSH user for your EC2 instance (e.g., `ec2-user` for Amazon Linux or `ubuntu` for Ubuntu).
- `PRIVATE_KEY`: The PEM-formatted private key file contents (`.pem`) used to SSH into your EC2 instance.

### 3. Execution
Once the secrets are configured, any push to the `main` branch will automatically:
1. Trigger the GitHub Action workflow.
2. SSH into your EC2 instance using the provided secrets.
3. Clone or update the repository at `/home/ec2-user/aws-python-deployment-demo` (can be customized in `deploy.py`).
4. Execute `app.py` directly on the server, showing the output in the workflow logs.

You can monitor the deployment status and view the application's output in the **Actions** tab of your GitHub repository.