# Experiment 29: Basic Git Operations

## 1. Introduction
Git is a version control system used to track changes in files and manage projects.

## 2. Check Git Version
```bash
git --version
```
Shows the installed Git version.

## 3. Git Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
Used to set username and email.

To check configuration:
```bash
git config --list
```

## 4. Initialize Repository
```bash
git init
```
Creates a new Git repository in the current folder.

## 5. Check Status
```bash
git status
```
Shows modified, untracked and staged files.

## 6. Add Files
```bash
git add filename
git add .
```
Adds files to the staging area.

## 7. Commit Changes
```bash
git commit -m "Initial commit"
```
Saves the changes with a message.

## 8. Check Commit History
```bash
git log
git log --oneline
```
Shows the previous commits.

## 9. Check Differences
```bash
git diff
git diff --staged
```
Shows the changes made in files.

## 10. Remove a File
```bash
git rm filename
```
Removes a file from the repository.

## 11. Rename a File
```bash
git mv oldname newname
```
Used to rename a file.

## 12. Restore Changes
```bash
git restore filename
git restore --staged filename
```
Used to discard file changes or unstage a file.

## 13. .gitignore
Example:
```gitignore
*.pyc
__pycache__/
.env
```
It tells Git which files to ignore.

## Conclusion
In this experiment, I learned basic Git commands used to create a repository, add files, commit changes and manage project files.
