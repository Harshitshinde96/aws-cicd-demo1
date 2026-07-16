# AWS CI/CD Deployment Flow

## 📌 Project Overview
This project demonstrates an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline. The core objective is to show how code changes can be automatically deployed to a cloud environment without manual intervention. In this specific project, pushing code to a source repository automatically triggers a process to deploy and run the latest version of our Python application on an AWS EC2 instance using GitHub Actions.

## 🏗️ Architecture Design
The deployment architecture operates in the following sequential steps:
1. **Code Modification & Push:** A developer makes changes to the application and pushes the updated code to the `main` branch of the GitHub repository.
2. **Pipeline Trigger:** GitHub Actions detects the push event and automatically launches the predefined deployment workflow.
3. **Environment Setup:** The automation workflow provisions a temporary Ubuntu runner environment, sets up Python 3.11, and installs the required dependencies (Paramiko).
4. **Secure Cloud Connection:** Using securely stored credentials, the workflow establishes a secure shell (SSH) connection directly to the target AWS EC2 instance.
5. **Code Synchronization:** Once connected to the EC2 server, the deployment script ensures that the latest version of the repository is either cloned or pulled onto the server.
6. **Application Execution:** Finally, the latest version of the Python application is executed on the AWS EC2 instance.

## 🧰 AWS Services Utilized
- **AWS EC2 (Elastic Compute Cloud):** Serves as the hosting and execution environment for the Python application.

## 🔐 Security Best Practices Implemented
- **GitHub Secrets:** Secure credentials (EC2_HOST, EC2_USERNAME, PRIVATE_KEY) are stored securely in GitHub Secrets and never exposed in the repository.
- **SSH Key Pairs:** Uses RSA private keys to securely establish an SSH connection between the GitHub Actions runner and the EC2 instance, avoiding password-based authentication.
- **Auto Add Policy:** Uses secure host key policies (with Paramiko) for connecting to the EC2 server.

## 📂 Repository Contents
- `.github/workflows/python-app.yml`: GitHub Actions pipeline definition for automating the build and deploy process.
- `app.py`: The main Python application that parses `students.json` and outputs the top student's name and marks.
- `deploy.py`: The Python deployment script that authenticates to the EC2 instance via SSH, updates the repository, and executes the application.
- `requirements.txt`: Contains the required Python dependencies (e.g., `paramiko`) for the deployment process.
- `students.json`: JSON data file containing sample student records.

## 🚀 Verification & Testing
To verify the automated deployment:
1. Make a modification to the code (e.g., update the marks in `students.json`).
2. Commit and push the changes to the `main` branch.
3. Navigate to the **Actions** tab in the GitHub repository to monitor the pipeline execution.
4. Verify that the final step executes `python3 app.py` on the EC2 instance successfully.