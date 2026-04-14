
# Git and GitHub SSH Setup and Workflow

## Overview
This project demonstrates the complete setup of Git version control along with secure authentication to GitHub using SSH keys. It also covers repository initialization, branching workflow, and pushing code to a remote repository using SSH.

## Objective
The objective of this implementation is to establish a secure and efficient workflow for version control using Git and GitHub, eliminating the need for password-based authentication.

## Tools and Technologies
- Git
- GitHub
- SSH (Secure Shell)
- Windows Command Prompt

## Git Configuration
Global Git identity was configured to associate commits with the user:

git config --global user.name "Nitanshu Tak"
git config --global user.email "nitanshutak070105@gmail.com"

## SSH Key Generation
A new SSH key pair was generated using the ED25519 algorithm:

ssh-keygen -t ed25519 -C "nitanshutak070105@gmail.com"

The keys were stored in the default location inside the .ssh directory.

## SSH Key Management
The public key was retrieved and added to GitHub to enable secure authentication. This allows communication between the local system and GitHub without requiring passwords.

## SSH Connection Verification
The connection to GitHub was verified using:

ssh -T git@github.com

Successful authentication confirms that the SSH setup is correctly configured.

## Local Repository Setup
A new local repository was initialized:

git init

A README file was created and added to the repository, followed by an initial commit.

## Branching Workflow
A feature branch was created to simulate a real-world development workflow:

git checkout -b feature-branch

Changes were made and committed within the branch.

## Remote Repository Integration
A remote repository was created on GitHub and linked using SSH:

git remote add origin git@github.com:Nitanshu715/git-ssh-apr7.git

## Code Push
The code was pushed to the remote repository:

git push -u origin main
git push origin feature-branch

## Verification
The repository was verified on GitHub, ensuring that both the main branch and feature branch were successfully uploaded.

## Observations
- SSH authentication eliminates the need for repeated login
- Git provides efficient version control and tracking
- Branching enables parallel development workflows
- Remote repositories allow collaboration and backup

## Conclusion
This implementation demonstrates a complete Git workflow using SSH-based authentication. It ensures secure communication with GitHub, supports efficient version control, and enables structured development using branches. This setup is widely used in modern software development and DevOps practices.

