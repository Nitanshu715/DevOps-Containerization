
# Git Workflow and Branching Practical

## Overview
This project demonstrates fundamental Git operations including repository cloning, file tracking, committing changes, branching, and merging. It provides a clear understanding of how version control systems manage code evolution and collaboration.

## Objective
The objective of this practical is to understand and implement core Git workflows such as creating commits, managing branches, tracking changes, and merging feature work into the main branch.

## Tools and Technologies
- Git
- GitHub
- Windows Command Prompt

## Repository Cloning
The repository was cloned from GitHub to the local system to begin the workflow.

git clone https://github.com/Nitanshu715/DevOps-Containerization.git

## Branch Inspection
Branches were inspected using Git commands to understand the repository structure.

git branch -a

## File Creation and Commit
A new file was created and committed to the repository.

echo test2 > test2.txt
git add .
git commit -m "test2"

## Commit History
The commit history was analyzed using:

git log --oneline
git log --oneline --graph

This helped visualize the sequence of commits and branch structure.

## Branch Creation
A new feature branch was created to simulate development workflow.

git checkout -b featureA

## Feature Development
A new file was added in the feature branch and committed.

echo feature work > feature.txt
git add .
git commit -m "feature added"

## Branch Divergence
The commit graph was analyzed again to observe divergence between main and feature branch.

## Merging
The feature branch was merged back into the main branch.

git checkout main
git merge featureA

## Observations
- Git efficiently tracks changes across commits
- Branching enables parallel development
- Commit history visualization helps understand workflow
- Merging integrates feature work into main branch

## Conclusion
This practical demonstrates essential Git workflows used in real-world development environments. It highlights the importance of version control, structured branching, and proper commit management in software development.

## Result
The repository successfully incorporated changes from a feature branch into the main branch, demonstrating a complete Git workflow cycle.

