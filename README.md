# GitandHub

<!-- TOC -->

* [GitandHub](#gitandhub)
    * [MODULE 1](#module-1)
        * [Introduction](#introduction)
        * [Before Version Control](#before-version-control)
        * [Version Control Systems](#version-control-systems)
        * [Using Git](#using-git)
        * [Qwiklabs Assessment](#qwiklabs-assessment)
    * [MODULE 2](#module-2)
        * [Advanced Git Interaction](#advanced-git-interaction)
        * [Undoing Things](#undoing-things)
        * [Branching and Merging](#branching-and-merging)
        * [Qwiklabs Assessment](#qwiklabs-assessment-1)
    * [MODULE 3](#module-3)
        * [Introduction to GitHub](#introduction-to-github)
        * [Using a Remote Repository](#using-a-remote-repository)
        * [Secure Shells & API Keys](#secure-shells--api-keys)
        * [Solving Conflicts](#solving-conflicts)
        * [Qwiklabs Assessment](#qwiklabs-assessment-2)
    * [MODULE 4](#module-4)
        * [Pul Requests](#pul-requests)
        * [Code Reviews](#code-reviews)
        * [Managing Projects](#managing-projects)
        * [Qwiklabs Assessment](#qwiklabs-assessment-3)
        * [Preparing your Resume](#preparing-your-resume)
        * [Wrap Up](#wrap-up)

<!-- TOC -->

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
    - `patch` command will allow us to apply changes from diff file
    - we use this method for following reasons
        - original code could have changed
        - `patch` command can detect that there were changes made to the file and will do its best to apply the diff
          anyway
        - structure, it's easy even for larger files
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
4. Practical Application of diff and patch
    - `return` statements are only used inside functions
        - change current to a function
        - use `sys` module to ext
    - original copy is to compared with fixed copy
    - then generate diff copy
    - finally use `patch` command to apply changes to original file

### Version Control Systems

1. What is Version Control?
    - Keeps track of the changes we make to our files
    - With it, we can know when the changes were made and who made them
    - It also lets us easily revert a change
    - It makes collaboration easier by allowing us to merge changes from different sources
    - It keeps track of all different versions of files that we create as we save our changes
    - They always access the history of our files
    - `commit` a single change, changes/edits made to single/multiple files treating as collection of edits
    - `commit` provides mechanism to record why changes were made
    - VCS is a key part of managing code
    - VCS also is used to store configuration files, documentation, data files or any other content that we may need to
      track
2. Version Control and Automation
    - VCS is helpful, even at times if you don't need to share your scripts or collaborate with other
    - A version control system can function a lot like a time machine, giving you insights into the decisions of the
      past
    - So, nothing you do is lost with VCS
    - It's generally better to quickly roll back to working version and stop errors before spending time figuring what
      went wrong
    - Which means `you can curb the fix after the bleeding has stopped`
3. What is Git?
    - Git is a VCS created in 2005 by `Linus Torvalds`
    - Git is a free open source system
    - Instead of centralizing around a single server, Git has a distributed architecture
    - Git works as a standalone program as a server and as a client
    - Git clients can communicate with Git servers over network using HTTP, SSH or Git's own special protocol
    - Git website https://git-scm.com (scm stands for Source Control Management)
    - There are other VCS programs like Subversion or Mercurial
4. Installing Git
    - installation
    ```text
    apt install git 
    or
    yum install git
    ...
    git --version
    ```
    - IDEs : Atom, Notepad++, VScode etc...
5. Installing Git on Windows
    - installation
    - download software bundle and install

### Using Git

1. First steps with Git
    - Follow along
    ```text
    # configurations for tracking by VCS
    git config --global user.email '<your email>'
    git config --global user.name '<your name>'
    ...
    # initialise an empty git repository in current directory
    mkdir checks
    cd checks
    git init
    ...
    # git repository folder
    ls -la .git/
    ...
    # to make git track untracked files add them to git project
    git add some_file.py
    # to get information about current working tree and pending changes
    git status
    # commit to the git directory
    git commit
    ```
    - The area outside the git directory is working tree
    - Working tree is the current version of your project
    - Staging area (index): A file maintained by Git that contains all the information about what files and changes
      are going to go into your next commit
2. Tracking Files
    - Any Git project consists
        - git directory (history of file/changes)
        - working tree (current state of project)
        - staging are (changes marked for next commit)
    - Tracked files are part of the snapshots(commits)
        - modified (made changes but not committed)
        - staged (ready for a commit, next snapshot)
        - committed (stored in a snapshot in git directory)
    - Untracked files are not the part of snapshots
    ```text
    ls -l
    git status
    ...
    git add <modified file>
    git commit -m 'some message about the commit'
    ```
3. The Basic Git Workflow
    - The commit without message will be aborted (meaning no commit will happen)
    ```text
    mkdir scripts
    cd scripts
    git init
    # current configuration of git
    git config -l
    ... after some changes
    git status
    git add <modified file>
    git commit -m 'message about commit'
    git status
    ```
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