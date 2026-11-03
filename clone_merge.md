# Experiment 30: Git Clone, Branch and Merge

## 1. Introduction
Git allows us to copy repositories, create branches and merge changes.

## 2. Clone a Repository
```bash
git clone repository_url
```
Used to download a remote repository to our computer.

## 3. Check Branches
```bash
git branch
```
Shows all local branches.

## 4. Create a New Branch
```bash
git branch branch_name
```
Creates a new branch.

## 5. Switch Branch
```bash
git switch branch_name
```
Used to switch from one branch to another.

We can also create and switch to a branch using:
```bash
git switch -c branch_name
```

## 6. Rename a Branch
```bash
git branch -m new_name
```
Changes the current branch name.

## 7. Merge Branches
First switch to the branch where changes are to be merged.
```bash
git switch main
git merge branch_name
```
Merges the changes of another branch into the current branch.

## 8. Delete a Branch
```bash
git branch -d branch_name
```
Deletes a merged branch.

## 9. Conclusion
In this experiment, I learned how to clone repositories, create and switch branches, merge changes and delete branches.
