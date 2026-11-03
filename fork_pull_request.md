# Experiment 31: Git Fork and Pull Request

## 1. Introduction
Fork and Pull Request are used to contribute to other people's projects on GitHub.

## 2. Fork a Repository
Fork is used to create a copy of another user's repository in our GitHub account.

Steps:
1. Open the repository on GitHub.
2. Click on the Fork option.
3. Select your GitHub account.

## 3. Clone the Forked Repository
```bash
git clone repository_url
```
Downloads the forked repository to our computer.

## 4. Add Upstream Remote
```bash
git remote add upstream original_repository_url
```
Connects our local repository with the original repository.

## 5. Check Remote
```bash
git remote -v
```
Shows all connected remote repositories.

## 6. Create a New Branch
```bash
git switch -c new_branch
```
Creates and switches to a new branch.

## 7. Add and Commit Changes
```bash
git add .
git commit -m "Added new changes"
```
Adds and saves the changes.

## 8. Push Changes
```bash
git push origin new_branch
```
Uploads the branch to our forked GitHub repository.

## 9. Create Pull Request
Steps:
1. Open your forked repository on GitHub.
2. Click on Compare & Pull Request.
3. Select the original repository as the base.
4. Add a title and description.
5. Click on Create Pull Request.

A Pull Request is used to request the owner to review and merge our changes into the original repository.

## 10. Conclusion
In this experiment, I learned how to fork a repository, clone it, make changes and create a Pull Request on GitHub.
