# GitandHub

## MODULE 1

### Introduction

1. Introduction
    - Keep track of the different versions of your code and configuration files using version control systems or VCSs
    - VCSs allows us to rollback when mistakes happen also help us collaborate with others
    - Popular VCS is Git and GitHub is a service

2. Welcome to course
    - About the course

### Before Version Control

1. Keeping historical copies
    - These copies will let you see what project was like before and go back to that version if current version is wrong
    - They also let you see the progress of changes over time and help you understand why the changes was made
    - First, make the copy
    - Second, usually make a copy of whole thing, even if you're changing small part
    - Third, mailing to your colleagues about your changes
2. Diffing Files
    - `diff` command line tool show differences between two files / directories in few formats
    - output includes only the lines that are different between two files
    - There are a lot of other tools to compare files.
        - Ex: wdiff (highlights words changed instead of lines)
        - Ex: meld, KDiff3, or vimdiff (graphical tools display diffs side by side using colors)
   ```shell
   diff diffs/rearrange_1.py diffs/rearrange_2.py 
   ```
    - In the output:
        - `7c7` indicates the section that has changed
            - number at beginning indicates line number in first file
            - alphabet `c` means line was changed
            - alphabet `a` means line was added
        - `<` indicates line was removed (old line)
        - `---` separates the file changes
        - `>` indicates line was added (new line)
   ```shell
   diff -u diffs/rearrange_1.py diffs/rearrange_2.py 
   ```
    - In the input:
        - `-u` is used to tell `diff` to show differences in another format
        - u stands for unified format
    - In the output:
        - `-` and `+` are coexisted one after other like in pairs
        - `-` indicates line was removed
        - `+` indicates line was added
3. Applying changes
   - 
   ```shell
   cat diffs/cpu_usage.py
   ```
   ```shell
   diff -u diffs/cpu_usage.py diffs/cpu_usage_fixed.py > diffs/cpu_usage.diff
   ```
   ```shell
   cat diffs/cpu_usage.diff
   ```
   ```shell
   patch diffs/cpu_usage.py < diffs/cpu_usage.diff
   ```
      ```shell
   cat diffs/cpu_usage.py
   ```
4. Practical Application of diff and path

### Version Control Systems

1. What is Version Control?
2. Version Control and Automation
3. What is Git?
4. Installing Git
5. Installing Git on Windows

### Using Git

1. First steps with Git
2. Tracking Files
3. The Basic Git Workflow
4. Anatomy of commit message

### Qwiklabs Assessment

## MODULE 2

### Advanced Git Interaction

- Using Git Locally
- Skipping the Staging Area
- Getting More Information form the user / about our changes
- Deleting and Renaming Files

### Undoing Things

- Undoing Changes Before Committing
- Amending commits
- Rollbacks
- Identifying a commit

### Branching and Merging

- What is a branch?
- Creating New Branches
- Working with Branches
- Merging
- Merge Conflicts

### Qwiklabs Assessment

## MODULE 3

### Introduction to GitHub

- Working with Remotes
- What is GitHub?
- Basic Interaction with GitHub

### Using a Remote Repository

- What is a Remote?
- Working with Remotes
- Fetching New Changes
- Updating the Local Repository

### Secure Shells & API Keys

- What is a Secure Shell?
- The SSH protocol
- Configuring SSH
- API Keys
- When to use API Keys
- Public vs Private Keys

### Solving Conflicts

- The Pull-Merge-Push Workflow
- Pushing Remote Branches
- Rebasing Your Changes
- Another Rebasing Example
- Best Practices for Collaboration
- Conflict Resolution

### Qwiklabs Assessment

## MODULE 4

### Pul Requests

- Collaboration
- A Simple Pull Request on GitHub
- The Typical Pull Request Workflow on GitHub
- Updating an Existing Pull Request
- Squashing Changes
- Git Forks and Pull Requests

### Code Reviews

- What are Code Reviews?
- The Code Review Workflow
- How to use Code Reviews in GitHub
- More Information on Code Reviews

### Managing Projects

- Managing Collaboration
- Tracking Issues
- Continuous Integration
- Integration git and GitHub
- GitHub Project Management Tools
- Additional Tools

### Qwiklabs Assessment

### Preparing your Resume

### Wrap Up