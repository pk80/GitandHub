# GitandHub

<!-- TOC -->

* [GitandHub](#gitandhub)
    * [MODULE 1](#module-1)
        * [Introduction](#introduction)
        * [Before Version Control](#before-version-control)
        * [Version Control Systems](#version-control-systems)
        * [Using Git](#using-git)
        * [Glossary](#glossary)
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
    - Good commit message
        - helpful to commit audience in mind
        - specific rules by company
        - sections
            - first line, short summary followed by blank line
            - next, full description of changes (why & how it is important)
    - `git log` command is used to display these commit messages
    ```text
    cat example_commit.txt
    ...
    git log
    commit 5ed482c636ac2d5a79dd33cb559241c4cc8dd288 (HEAD -> main, origin/main)
    Author: praveen <praveen.goprog@gmail.com>
    Date:   Fri Mar 21 23:59:46 2025 +0530
    
        m1_anatomy-of-commit
    
    commit b8fdb22d97e6f3dd05076ef92047297248a04c2c
    Author: praveen <praveen.goprog@gmail.com>
    Date:   Fri Mar 21 23:43:31 2025 +0530
    
        added content in readme
    :
    ```
    - `5ed482c636ac2d5a79dd33cb559241c4cc8dd288` : commit identifier
    - `(HEAD -> main)` : Head indicator is point to the master branch
    - `Author: ......` : show the name and email of the person committed
    - `Date: ...` : date on which the message was committed
    - `    m1_.....` : message in the commit
5. Cheat sheet
    ```text
    # Git config command
    $ git config --global user.email "....."
    $ git config --global user.name "....."
    
    # Git init command
    $ git init
    
    # Git ls -la command
    $ ls -la
    $ ls -l .git/
    
    # Git add command
    $ git add <untracked/modified file>
    
    # Git status command
    $ git status
    
    # Git commit command
    $ git commit
    ```

### Glossary

* Commit: A command to make edits to multiple files and treat that collection of edits as a single change
* Commit files: A stage where the changes made to files are safely stored in a snapshot in the Git directory
* Commit message: A summary and description with contextual information on the parts of the code or configuration of the
* commit change
* Diff: A command to find the differences between two files
* DNS zone file: A configuration file that specifies the mappings between IP addresses and host names in your network
* Git: A free open source version control system available for installation on Unix based platforms, Windows and macOS
* Git directory: A database for a Git project that stores the changes and the change history
* Git log: A log that displays commit messages
* Git staging area: A file maintained by Git that contains all the information about what files and changes are going to
* go into the next commit
* Modified files: A stage where changes have been made to a file, but the have not been stored or committed
* Patch: A command that can detect that there were changes made to the file and will do its best to apply the changes
* Repository: An organization system of files that contain separate software projects
* Source Control Management (SCM): A tool similar to VCS to store source code
* Stage files: A stage where the changes to files are ready to be committed
* Tracked: A file’s changes are recorded
* Untracked: A file’s changes are not recorded
* Version control systems (VCS): A tool to safely test code before releasing it, allow multiple people collaborate on
  the
* same coding projects together, and stores the history of that code and configuration

### Qwiklabs Assessment

In this scenario, you are a project lead in an IT company. You and your team are working on a huge project, which
consists of multiple functionalities and modules. This project is evolving over time and so your team is expecting a lot
of code revisions. In this lab, you'll learn how to use a distributed version control system called Git. You'll also
discover how to connect to a VM instance, install Git, and configure your Git user information. Next, you'll create a
local Git repository, add a file to the repository, and do some basic operations like adding a file, editing files, and
making commits.

**What you'll do**

- Create a git repository.
- Add files to this repository
- Edit the files
- Commit the changes to the repository.
    ```text
    # Install Git
    sudo apt update
    sudo apt install git
    git --version
    ...
    # Initialize new repository
    mkdir my-git-repo
    cd my-git-repo
    git init
    ...
    # Configure Git
    git config --global user.name '<your name>'
    git config --global user.email '<your email>'
    
    warning: user.name has multiple values
    error: cannot overwrite multiple values with a single value
           Use a regexp, --add or --replace-all to change user.name.
    ...
    # Git Operations
    nano README
    This is my first repository.
    Ctrl+o, Enter and Ctrl+x
    git status
    git add README
    git commit
    This is my firs commit!
    Ctrl+o, Enter and Ctrl+x
    nano README
    A repository is a location where all the files of a particular project are stored.
    Ctrl+o, Enter and Ctrl+x
    git status
    git diff README
    git add README
    git status
    git commit -m "This is my second commit."
    git log
    ```

## MODULE 2

### Advanced Git Interaction

1. Using Git Locally
2. Skipping the Staging Area
    - `git commit -a` : to stage any changes to tracked files and commit them in one step
    ```text
    git commit -a -m 'message.....' # a small change and want to skip the staging step
    git commit -a
    git commit -a
    git commit -m 'final message....'
    ```
    - Git uses the HEAD alias to represent the currently checked-out snapshot of your project
3. Getting More Information form the user / about our changes
    ```text
    # log patch flag show associated patches
    git log -p
    # take commit id and shows it
    git show <commit id>
    git log --stat
    git diff
    git add -p
    git diff
    git diff --staged
    git commit -m '......'
    ```
4. Deleting and Renaming Files
    ```text
    ls -l
    ...
    # rm will delete file, do not allow from being tracked by git 
    # and file is staged to commit
    git rm <filename>
    ls -l
    ...
    git status
    ...
    git commit -m 'Delete unneeded processes file'
    ...
    # rename a file
    # and file is staged to commit
    git mv <old_filename> <new_filename>
    git status
    ...
    git commit -m 'New name for old_filename'
    ...
    echo .DS_STORE > .gitignore
    ls -la
    ...
    git add .gitignore
    git commit -m 'Add a gitignore file, ignoring .DS_STORE files'
    ```
5. Cheat sheet
    ```text
    $ git commit -a
     automatically stages the files that have been locally modified. 
     New files which have not been published yet are not affected.
    $ git log -p
     produces patch text that displays the lines of code that were 
     changed in each commit in the current repo. 
    $ git show
     shows you one or more object(s) such as blobs, trees, tags, and commits.
    $ git diff
     is similar to the Linux `diff` command, and can show the changes 
     between commits, changes between the working tree and index, 
     changes between two trees, changes from a merge, and so on.
    $ git diff --staged
     is an alias of $ git diff --cached, which  shows all staged 
     files compared to the named commit.
    $ git add -p
     allows a user to interactively review patches before adding to 
     the current commit.
    $ git mv
     is similar to the Linux `mv` command. This command can move or 
     rename a file, directory, or symlink.
    $ git rm 
     is similar to the Linux `rm` command. This command deletes or 
     removes a file from the working tree.
    ```

### Undoing Things

1. Undoing Changes Before Committing
    - If you have made any additional changes to a file after you've staged it, you can restore the file to the earlier
      stage version.
    - If you need to check out individual changes instead of whole file, you can do that using the `-p` flag. This will
      ask you change by change if you want to go back to the previous snapshot or not
    ```text
    git status
    # revert changes to modified file before they are staged for commit
    git checkout <filename>
    git status
    ...
    exe_out > output.txt
    git add *
    git status
    # unstage
    git restore --staged <filename>
    # unstage / restore changes in a file after committed to git
    git reset HEAD output.txt
    Unstaged changes after reset:
    ...
    git satus
    git commit -m 'it should be os.path.exists'
    ```
2. Amending commits
    - update the commit by `--amend` command
    - `git --amend` is okay for fixing up local commits
    - Avoid amending commits that have already been made public
    - but you should not use it on public commits (pushed to public/shared repo)
    - because as it rewrites, leads to confusion when working with other people
    - remember, fixing up a local commit with amend is great, and you can push it to a shared repository after you fixed
      it
    ```text
    cd changes/
    touch auto-update.py
    touch gather-information.sh
    ls -l
    ----
    git status
    
    git add auto-update.py
    git commit -m 'Add two new scripts'
    ----
    git status
    On branch main
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   ../README.md
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            gather-information.sh
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ----
    git add gather-information.sh
    git commit --amend
    [main 56586c7] Add two files
    Date: Sat Mar 22 03:03:22 2025 +0530
    2 files changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 changes/auto-update.py
    create mode 100644 changes/gather-information.sh
    ```
3. Rollbacks
    - `git revert` command will undo and creates a new commit containing inversion of all changes made in bad commit in
      order to cancel them
      out
    -
    ```text
    cd changes
    nano all_checks.py
    ----
    git commit -a -m 'Add call to disk_full function'
    ----
    ./all_checks.py
    Traceback (most recent call last):
      File "/Users/praveen/PycharmProjects/GitandHub/./changes/all_checks.py", line 23, in <module>
        main()
        ~~~~^^
      File "/Users/praveen/PycharmProjects/GitandHub/./changes/all_checks.py", line 15, in main
        if disk_full():
           ^^^^^^^^^
    NameError: name 'disk_full' is not defined
    ----
    git revert HEAD
    # update and quit the commit message with reason 
    ----
    ./all_checks.py
    Everything OK!
    ----
    # log of last 2 entries
    git log -p -2
    ```
4. Identifying a commit
    - commit id is a 40 char id called hash, calculated using SHA1
    - these hash codes are used to guarantee the consistency of our repository means that we get exactly what we expect
    ```text
    git log -1
    # e3c0478ed90f3de8c1e2648ae6e95e54429bcda4
    git show <commit id>
    git show e3 # not enough
    git show e3c0 # enough
    git revert e3c0
    git revert 7d71
    git show 7d1de19
    ```
5. Cheat sheet

    ```markdown
    **Study guide: Git Revert**
    When writing and committing code, making mistakes is a common occurrence. Thankfully, there are
    multiple ways for you to revert or undo your mistakes. Take a look at the helpful commands below.
    
    **git checkout**
    is used to switch branches. For example, you might want to pull from your main branch.
    In this case, you would use the command git checkout main. This will switch to your main branch,
    allowing you to pull. Then you could switch to another branch by using the command git checkout <branch>.
    
    **git reset**
    can be somewhat difficult to understand. Say you have just used the command git add. to stage all of
    your changes, but then you decide that you are not ready to stage those files. You could use the command
    git reset to undo the staging of your files.
    
    There are some other useful articles online, which discuss more aggressive approaches to
    resetting the repo
    (Git repository). As discussed in this article, doing a hard reset can be extremely dangerous.
    With a hard reset, you run the risk of losing your local changes. There are safer ways to achieve the same effect.
    For example, you could run git stash, which will temporarily shelve or stash your current changes. This way,
    your current changes are kept safe, and you can come back to them if needed.
    
    **git commit --amend**
    is used to make changes to your most recent commit after-the-fact, which can be useful for making notes about or
    adding files to your most recent commit. Be aware that this git --amend command rewrites and replaces your previous
    commit, so it is best not to use this command on a published commit.
    
    **git revert**
    makes a new commit which effectively rolls back a previous commit. Unlike the git reset command which rewrites
    your commit history, the git revert command creates a new commit which undoes the changes in a specific commit.
    Therefore, a revert command is generally safer than a reset command.
    
    For more information on these and other methods to undo something in Git, checkout this
    [Git Basics - Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) article.
    
    Additionally, there are some interesting considerations about how git object data is stored, such as the usage of SHA-1.
    
    SHA-1 is what’s known as a hash function, a cryptographic function that generates a digital fingerprint of a file.  
    Theoretically, it’s impossible for two different files to have the same SHA-1 hash, which means that SHA-1 can be
    used for two things:
    
    - Confirming that the contents of a file have not changed (digital signature).
    - Serving as an identifier for the file itself (a token or fingerprint).
    
    Git calculates a hash for every commit. Those hashes are displayed by commands like git log or in various pages
    on Github. For commands like git revert, you can then use the hash to refer to a specific commit.
    ```

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