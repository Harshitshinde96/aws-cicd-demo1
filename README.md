# AWS CI/CD Deployment Flow

## High-Level Concept
This project demonstrates an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline. The core objective is to show how code changes can be automatically deployed to a cloud environment without manual intervention. In this specific AWS project, we have built a mechanism where pushing code to a source repository automatically triggers a process to deploy and run the latest version of our application on an AWS EC2 (Elastic Compute Cloud) instance.

## What We Have Done
We have bridged the gap between local development and cloud deployment by setting up an automated pipeline. Instead of manually logging into a server, pulling the code, and running the application, we configured a CI/CD workflow to handle this end-to-end. We utilized GitHub Actions as our automation engine and an AWS EC2 instance as our hosting environment. Secure credentials and keys were configured to ensure that the automation server can safely communicate with our cloud infrastructure.

## Project Flow
The flow of this deployment architecture operates in the following sequential steps:

1. **Code Modification & Push:** A developer makes changes to the application and pushes the updated code to the `main` branch of the GitHub repository.
2. **Pipeline Trigger:** GitHub Actions detects the push event and automatically launches the predefined deployment workflow.
3. **Environment Setup:** The automation workflow provisions a temporary runner environment, sets up Python, and installs any required dependencies needed for the deployment process.
4. **Secure Cloud Connection:** Using securely stored credentials (such as the host address, username, and SSH private key), the workflow establishes a secure shell (SSH) connection directly to the target AWS EC2 instance.
5. **Code Synchronization:** Once connected to the EC2 server, the deployment script ensures that the latest version of the repository is either cloned (if it's the first time) or pulled (updating an existing directory) onto the server.
6. **Application Execution:** Finally, the latest version of the Python application is executed on the AWS EC2 instance, completing the automated deployment lifecycle.