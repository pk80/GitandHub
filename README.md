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
        * [Glossary](#glossary-1)
        * [Qwiklabs Assessment](#qwiklabs-assessment-1)
    * [MODULE 3](#module-3)
        * [Introduction to GitHub](#introduction-to-GitHub)
        * [Using a Remote Repository](#using-a-remote-repository)
        * [Secure Shells & API Keys](#secure-shells--api-keys)
        * [Solving Conflicts](#solving-conflicts)
        * [Glossary](#glossary-2)
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
    on GitHub. For commands like git revert, you can then use the hash to refer to a specific commit.
    ```

### Branching and Merging

1. What is a branch?
    - A pointer to a particular commit
    - Represents an independent line of development in a project
    - Default branch when created is called master/main
    - Master/Main branch is know to be a good state of a project
    - New branch can be created to add a feature or fix something and develop there
    - Iterate your code in other branch until it works correctly without affecting the master/main branch
    - Only after code is ready, we would merge those changes to master/main
2. Creating New Branches
    - `git branch` command to list, create, delete and manipulate branches
    - `git checkout` command to restore a modified file back to latest commit
    - `git checkout` command to switch to a new branch
    - `git checkout` is used to check out the latest snapshot for both files and for branches
    - `git checkout -b` shortcut to create and check out to new branch
   ```text
   cd checks/
   git branch
   ----
   git branch new-feature
   git branch
   ----
   git checkout new-feature
   ----
   git checkout -b even-better-feature
   ----
   git log -2
   commit d....8e3482fa5.....59f0b96d7d167d363 (HEAD -> even-better-feature)
   ...
   commit 6....930db406........a963c8ea17162ce (new-feature, main)
   ```
3. Working with Branches
    - each branch is just a pointer to a specific commit in a series of snapshots
    - `gi branch -d` command deletes the branch
   ```text
   cd checks
   git status
   ----
   ls -l
   ----
   git checkout main
   git log -2
   ----
   ls -l
   ----
   git branch
   ----
   git branch -d new-feature
   error: The branch 'new-feature' is not fully merged.
   If you are sure you want to delete it, run 'git branch -D new-feature'.
   git branch -D even-better-feature
   ----
   git branch
   ----
   git branch -d even-better-feature
   ---
   git branch
   ```
4. Merging
    - Merging is the term git uses for combining branch data and history together
    - Once new feature in separate branch is in good shape, we merge them into main
    - `git merge` command takes the independent snapshots and history of one git branch and tangle them into another
    - git uses two algorithms to perform a merge:
        - fast-forward merge
        - three-way merge
   ```text
   git branch
   ----
   # fast-forward merge
   git merge even-better-feature
   Updating ae37c36..d07cbaa
   Fast-forward
    all_checks.py   | 1 +
    free_memeory.py | 7 +++++++
    2 files changed, 8 insertions(+)
    create mode 100644 free_memeory.py
   ----
   git log
   commit ......e3482fa5580c82459f0b96d7d167d363 (HEAD -> main, even-better-feature)
   Author: praveen <...............>
   Date:   Sat Mar 22 23:50:38 2025 +0530
   
       free memory first file
   
   commit ......0db4062f328da3122a963c8ea17162ce
   Author: praveen <...............>
   Date:   Sat Mar 22 23:41:02 2025 +0530
   
       added shabang
   
   commit ......b99035d493f05906ce4c8a226ce1eab
   Author: praveen <...............>
   Date:   Sat Mar 22 23:38:28 2025 +0530
   
       check first commit
   ----
   ```
5. Merge Conflicts
    - Edits to the same part of the same file causes merge conflicts
    - Resolve the conflict as show below and add file to commit
    - `git merge --abort` if you want to throw merge away and start over back to the previous commit before the merge
      ever happened
   ```text
   nano free_memory.py
   ---- change something and commit
   git commit -a -m 'Add comment to main()'
   ----
   git checkout even-better-feature
   ----
   nano free_memeory.py
   git commit -a -m 'Print everything ok'
   ----
   git checkout main
   ----
   git merge even-better-feature
   Auto-merging free_memeory.py
   CONFLICT (content): Merge conflict in free_memeory.py
   Automatic merge failed; fix conflicts and then commit the result.
   ---- CONFLICT
   git status
   On branch main
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
       both modified:   free_memeory.py
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ----
   nano free_memroy.py
   # thankfully git has added info to our files which parts of code are conflicting
   # make changes as required and save and close the file
   git add free_memory.py
   git status
   On branch main
   All conflicts fixed but you are still merging.
     (use "git commit" to conclude merge)
   
   Changes to be committed:
       modified:   free_memeory.py
   ----
   # editor opens with default commit message created with `git merge` command
   git commit
   [main 243694c] Merge branch 'even-better-feature'
   ----
   git log --graph --oneline
   *   243694c (HEAD -> main) Merge branch 'even-better-feature'
   |\  
   | * cca1b47 (even-better-feature) Print everything ok
   * | 4b3dd40 Add comment in main function.
   |/  
   * d07cbaa free memory first file
   * 61fe639 added shabang
   * ae37c36 check first commit
   ----
   ```
6. Cheat sheet
   ```text
   $ git branch
    can be used to list, create, or delete branches.
   
   $ git branch <name>
    can be used to create a new branch in your repository. 
   
   $ git branch -d <name>
    can be used to delete a branch from your repository.
   
   $ git branch -D <branch>
    forces a branch to be deleted.
   
   $ git checkout <branch>
    switches your current working branch.
   
   $ git checkout -b <new-branch>
    creates a new branch and makes it your current working branch. 
   
   $ git merge <branch>
    joins changes from one branch into another branch.
   
   $ git merge --abort
    can only be used after merge conflicts. This command will abort the merge and try to go back to the pre-merge state.
   
   $ git log --graph 
   prints an ASCII graph of the commit and merge history.
   
   $ git log --oneline
    prints each commit on a single line.
   ```

### Glossary

**Terms and definitions from Course 3, Module 2**

- **Branch**: A pointer to a particular commit, representing an independent line of development in a project
- **Commit** ID: An identifier next to the word commit in the log
- **Fast**-forward merge: A merge when all the commits in the checked out branch are also in the branch that's being
  merged
- **Head**: This points to the top of the branch that is being used
- **Master**: The default branch that Git creates for when a new repository initialized, commonly used to place the
  approved pieces of a project
- **Merge** conflict: This occurs when the changes are made on the same part of the same file, and Git won't know how to
  merge those changes
- **Rollback**: The act of reverting changes made to software to a previous state
- **Three-way merge**: A merge when the snapshots at the two branch tips with the most recent common ancestor, the
  commit before the divergence

### Qwiklabs Assessment

In this lab, you'll use your knowledge of Git and Git commit history to check out an existing repo and make some changes
to it. You'll also test what you learned about rolling back commits after bad changes in order to fix a script in the
repo and run it to produce the correct output.

**What you'll do**

1. Check the status and history of an existing Git repo
2. Create a branch
3. Modify content on the branch
4. Make rollback changes
5. Merge the branch

## MODULE 3

### Introduction to GitHub

1. Working with Remotes
    - Git is a distributed version control system
    - Distributed : each developer has a copy of the whole repository on their local machine
2. What is GitHub?
    - GitHub :
    - a web base git repository hosting service
    - is an online service for Git server hosting repositories
    - includes extra features like
        - bug tracking
        - wikis
        - task management
    - share and access repositories on the web and copy or clone them to our local computer
    - Other services like GitHub are
        - BitBucket
        - GitLab
    - For real configuration and development work, you should use a secure and private Git server, and limit the people
      authorized to work on it
3. Basic Interaction with GitHub
   ```text
   git clone <git-http-git-code>
   ----
   # make some changes
   git commit -a -m 'Add one or more lines to README'
   ----
   git push
   ----
   git config --global credential.helper cache
   ----
   git pull
   ----
   git pull
   ```

### Using a Remote Repository

1. What is a Remote?
   ```text
   git clone <http-code-git>
   ```
2. Working with Remotes
   ```text
   cd health-checks/
   git remote -v
      origin  https://GitHub.com/pk80/GitandHub.git (fetch)
      origin  https://GitHub.com/pk80/GitandHub.git (push)
   ----
   git remote show origin
      * remote origin
        Fetch URL: https://GitHub.com/pk80/GitandHub.git
        Push  URL: https://GitHub.com/pk80/GitandHub.git
        HEAD branch: main
        Remote branch:
          main tracked
        Local ref configured for 'git push':
          main pushes to main (up to date)
   ----
   git branch -r
     origin/main
   ----
   ```
3. Fetching New Changes
   ```text
   git remote show origin
   ----
   git fetch
   ----
   git log origin/main
   git status
   ----
   git merge origin/main
   ----
   git log
   ----
   ```
4. Updating the Local Repository
   ```text
   git pull
   ----
   git log -p -1
   ----
   git remote show origin
   ----
   git checkout <branch_name>
   ----
   ```
5. Git remotes
    - **git remote** : allows you to manage the set of repositories or “remotes” whose branches you track.
    - **git remote -v** : is similar to `git remote`, but adding the `-v` shows more information such as the remote
      URL.\
    - **git remote show <name>** : shows some information about a single remote repo.
    - **git remote update** : fetches updates for remotes or remote groups.
    - **git fetch** : can download objects and refs from a single repo, a single URL, or from several repositories at
      once.
    - **git branch -r** : lists remote branches and can be combined with other branch arguments to manage remote
      branches.

### Secure Shells & API Keys

1. What is a Secure Shell?
    - Secure shell (SSH) is a robust protocol for connecting to servers remotely
    - SSH secures data in interactive terminal sessions or file transfers. This encryption ensures that sensitive
      information remains confidential during communication.
    - SSH adheres to the principle of the least privilege, restricting users to specific hosts, enhancing security
    - Alternate ot SSH :
        - Telnet (exposes your typed commands, including passwords, to anyone on the network equipped with the right
          tools)
        - TLS (encrypts data within web browsers)
        - VPN (encryption but grant access to entire networks after connection)
        - VNS or GoToMyPc (focus on graphical user interfaces and desktop experiences)
    - Operation :
        - the SSH server
            - residing on the target server, establishes secure network connections, undergoes mutual authentication,
              and initiates encrypted login sessions or file transfers
        - the SSH client
            - establishes a connection to the SSH server, ensuring a secure interaction. The client makes requests, such
              as “log me in” or “copy this file.”
    - SSH Keys :
        - In the SSH protocol, an access credential is SSH Key
        - serves a similar purpose as usernames and passwords, although system administrators and power users typically
          use the keys to automate procedures and achieve single sign-on.
        - Displaying the fingerprint of an SSH key is a useful way to verify that you're using the correct key and that
          the remote server's key hasn't been tampered with.
        - To display the fingerprint of an SSH key, you can use the ssh-keygen command-line tool.
2. The SSH protocol
    - the word “shell” refers to a program that provides an interface for accessing another operating system
    - The Secure Shell network protocol, usually shorthanded to “SSH,” allows secure access to a computer over an
      unsecured network
    - What is a protocol ?
        - A protocol is a set of rules for how two things should communicate with each other.
        - these are usually published as open standards so that any given protocol can be implemented in various
          products
    - SSH Protocol :
        - SSH works on the principle of public-key encryption
        - The client and the server each generate a strong encryption key for any data that is passed between them.
          Then, that key gets split in half, with the client retaining one portion and the server keeping the other.
        - In SSH, the keys are split between a public key, the public half of the server’s encryption key, and the
          private key, which is stored only on the server.
        - This way, a user’s machine can encrypt a message using the public key, but only the connected server can
          decode it because only the server’s private key will successfully decrypt the message.
        - Using SSH, your keystrokes and the server’s responses are completely secure.
    - Using the SSH protocol
        - The SSH protocol is commonly used for logging in to servers remotely.
        - Used to encrypt file transfers and to log in to some network equipment, like routers.
        - Your private key is unique to you, it can serve as both authentication and encryption, so the server doesn’t
          need to ask you for a password.
        - Other uses :
            - Transferring files between client and server with SCP (Secure Copy Protocol) or SFTP (Secure File Transfer
              Protocol)
            - Forwarding network ports from server to client, or “tunneling”
            - Relaying your login to yet another server behind a firewall, sometimes referred to as a “jump box” or
              “bastion
              host”
            - Running graphical user interface (GUI) applications on a server but displaying them on a local client
3. Configuring SSH
    - When using Secure Shell (SSH), the client connects to the server on port 22
    - SSH configuration instructions will be different depending on your operating system and the implementation of SSH
    - But instructions for a client to generate its SSH key and connect to a server are more general
    - If you add a passphrase to your SSH key for added security, you can save the passphrase to an SSH agent, which is
      a program that manages SSH keys.
    - SSH will also ask you for a passphrase to protect your key. Many people choose not to use a passphrase because if
      you enter a passphrase here, you will be required to enter it every time your key is used. If you are on a machine
      that is not secure, however, someone who gains access to that computer will also have access to every system that
      uses that key.
    - After you have set your passphrase or declined the option, OpenSSH will then generate a random public/private key
      pair and save it. Depending on your hardware, this may take several seconds to complete. OpenSSH will then return
      a message that your key has been saved and display the fingerprint and a “randomart image” of your new key
   ```text
   # Generating your key pair
   # it will create a hidden directory called .ssh in your home directory b default
   # SSH will also ask you for a passphrase to protect your key
   ssh-keygen -t rsa -b 2048
   
   # Now that you have a key pair, you can connect to a host. The most basic form of the command to connect is
   ssh <username>@<hostname>
   ```
4. API Keys
    - An Application Programming Interface (API) key is an authentication token that allows you to call an API
    - It is frequently accompanied by a set of access rights that are specific to the API the key is linked to
    - The API key is usually randomly generated by the application and must be sent on every API call.
    - It serves as a distinctive identifier and offers a secure token for authentication.
    - Authentication and authorization :
        - authentication : making sure you’re who you say you are
            - When you are authenticating with API keys, you are ensuring that malicious users or applications can’t
              call an
              API and make unauthorized or authorized changes.
        - authorization : deciding which APIs you are allowed to call
            - When you are authorizing with API keys, you are also ensuring that you have the correct API call.
              Authorization will also check that the API key being used in the project is available.
    - How they are used :
        - As an HTTP parameter in the request URL : `GET https://myapp.com/api/users/list?apikey=12345678`
        - As an HTTP header sent with the request : `GET https://myapp.com/api/users/listX-API-Key: 12345678`
        - Posted to a specific authorization endpoint, which returns another token or a cookie to be sent with
          subsequent requests (rarely) : `POST https://myapp.com/api/auth{ “token”: “12345678” }`
    - Do not hardcode API keys into your application code, especially if it will be posted in a public repository
      like GitHub
    - Unfortunately, it happens every day. For this reason, many applications are moving away from API keys and toward
      OAuth, which requires the user to manually authorize an application before using it. With being extra cautious,
      you can make sure this does not happen to you
5. When to use API Keys
    - Managing access and safeguarding resources is where API keys come into play
    - Reasons why you might want to use API keys
        - To block anonymous traffic (protect your API from abuse and to ensure access to only authorized users)
        - To control the number of calls made to your API (to prevent your API from being overloaded and to ensure that
          it is available to all authorized users)
        - To identify usage patterns (to improve your API and to make sure that it is meeting the needs of your users)
        - To filter logs by API key (to troubleshoot problems with your API and to identify which users are using your
          API the most)
    - Reasons why you can not use API keys
        - Identifying individual users (API keys do not identify individual users; they identify entire projects)
        - Secure authorization (They should be used only to identify and control access to an API)
        - Identifying the creators of a project (Service Infrastructure doesn't provide a method to directly look up
          projects from API keys)
    - API keys serve as the link between the potential of APIs and the demand for restricted usage.
6. Public vs Private Keys
    - Asymmetric cryptography relies on public and private keys as its core building blocks to maintain data security
      and confidentiality in the face of dangers
    - What is a public key?
        - A public key is frequently employed to establish secure communication through data encryption or to validate
          the authenticity of a digital signature.
        - Safety is ensured because the public key comes from a trusted certificate authority, which gives digital
          certificates verifying the owner’s identity and key.
    - What is a private key?
        - A private key is a secret and secure key that must be kept confidential and protected.
        - Its role involves decryption and the creation of digital signatures, assuring the data's integrity and
          authenticity.
        - It is the counterpart of the public key and is shared to decrypt encoded information.
        - Any data encrypted using the private key can be decrypted using the corresponding public key.
    - How do public and private keys work together?
        - Public and private keys work together to ensure secure communication, data encryption, digital signatures, and
          key exchanges take place safely across various communication channels. This process encompasses
            - Key generation: A public and private key is generated for both the sender and receiver.
            - Key exchange: The public keys are exchanged between sender and receiver.
            - Encryption: The sender encrypts their data using the recipient's public key.
            - Transmitting encrypted data: The encrypted data is transmitted to the recipient.
            - Decryption: The recipient decrypts the message using their exclusive private key.

### Solving Conflicts

1. The Pull-Merge-Push Workflow
    ```text
    git add -p
    ----
    git commit -m '.....'
    ----
    git push
    ---- Rejected
    git pull
    ----
    git log --graph --oneline --all
    ----
    git log -p origin/master
    ---- make changes and fix the conflict here
    git add <filename> 
    git commit
    ---- provide extra information
    git push
    ----
    git log --graph --oneline
    ----
    ```
2. Pushing Remote Branches
    ```text
    git checkout -b <new_branch_name>
    ---- do some changes to one file
    ./runfile
    ---- if everything is ok
    git commit -a -m '...........'
    ---- again do some changes
    git commit -a -m '...........'
    ---- repeat couple of times like this
    git push -u origin <new_branch_name> 
    ----
    ```
3. Rebasing Your Changes
    - Rebase - changing the base commit that's used for the branch
    ```text
    git checkout main
    ----
    git pull
    ----
    git log --graph --oneline --all
    ----
    git checkout <branch_name>
    ----
    git rebase main
    ---- This will move <branch_name> on top of main branch
    git log --graph --oneline
    ----
    git checkout main
    ----
    git merge <branch_name>
    ----
    git push --delete origin <branch_name>
    ----
    git branch -d <branch_name>
    ----
    git push
    ----
    ```
4. Another Rebasing Example
    ```text
    ---- first do some changes to the file
    git commit -a -m '....................'
    ----
    git fetch
    ----
    git rebase origin/main
    ---- conflicts
    git add <file>
    git rebase --continue
    ----
    git log --graph --online
    ----
    git push
    ----
    ```
5. Best Practices for Collaboration
    - Always synchronize your branch before starting any work on your own
    - Avoid having very large changes that modify a lot of different things
    - When working on a big change, it makes sense to have a separate feature branch
    - Regularly merge changes made on the master branch back onto the feature branch
    - To maintain more than one version of a project at the same time, have the latest version of the project in the
      master branch, and the stable version of the project on a separate branch
    - Be very careful with the rebase, as it changes the history of the project. You shouldn't rebase changes that have
      been pushed to remote repos
    - Having good commit messages is important
6. Conflict Resolution
    - After running Git merge, a message will appear informing that a conflict occurred on the file.
    - Read the error messages that imply you cannot push your local changes to GitHub, especially the remote changes
      with
      Git pull.
    - Use the command line or GitHub Desktop to push the change to your branch on GitHub after you make a local clone of
      the
      repository for all other types of merge conflicts.
    - Before merging any commits to the master branch, push it into a remote repository so that collaborators can view
      the
      code, test it, and inform you that it’s ready for merging.
    - Use the Git rebase command to replay the new commits on top of the new base and then merge the feature branch back
      into the master.

### Glossary

**Terms and definitions from Course 3, Module 3**

- Application Programming Interface (API) key: This is an authentication token that calls an API, which is then called
  to identify the person, programmer, or program trying to access a website
- Computer protocols: Guidelines published as open standards so that any given protocol can be implemented in
  various
  products
- Distributed: Each developer has a copy of the whole repository on their local machine
- GitHub: A web-based Git repository hosting service, allowing users to share and access repositories on the web and
  copy or clone them to a local computer
- Merge: An operation that merges the origin/master branch into a local master branch
- Private key: A secret and secure cryptographic key that must be kept confidential and protected and is used to
  decrypt
  data that has been encrypted with the corresponding public key
- Public key: A safety cryptographic structure frequently employed to establish secure communication through data
  encryption or to validate the authenticity of a digital signature
- Rebasing: The base commit that's used for a branch is changed
- Remote branches: Git uses read-only branches to keep copies of the data that's stored in the remote repository
- Remote repositories: Repositories that allow developers to contribute to a project from their own workstations
  making
  changes to local copies of the project independently of one another
- Secure Shell (SSH): A robust protocol for connecting to servers remotely
- SSH client: This establishes a connection to the SSH server, ensuring a secure interaction, where the client makes
  access requests
- SSH key: An access credential
- SSH protocol: Standard commonly used for logging in to servers remotely on the principle of public-key encryption
  SSH server: This establishes secure network connections, undergoes mutual authentication, and initiates encrypted
  login sessions or file transfers

### Qwiklabs Assessment

In this lab, you'll practice the basics of interacting with GitHub. You'll practice setting up an account, logging in,
creating a repository, making changes on the local machine, and pushing changes back to the remote repository. We use
these git operations to share changes from the remote repository to the local repository and vice-versa.

**What you'll do**

1. Create a GitHub account
2. Create a git repository
3. Git clone to create a local copy on your local machine
4. Add a file to this repository
5. Create snapshot/snapshots of the local repository
6. Push the snapshots to the master branch

## MODULE 4

### Pul Requests

1. Collaboration
2. A Simple Pull Request on GitHub
    - Fork : A way of creating a copy of the given repository so that it belongs to our user
    - Pull Request : A commit or series of commits that you send to the owner of the repository so that they incorporate
      it into their tree
3. The Typical Pull Request Workflow on GitHub
   ```text
   git clone https://GitHub.com/<user>/<repo>.git
   ----
   cd <repo>
   ls -l
   ----
   git log
   ----
   git checkout -b add-readme
   ---- access file and make some changes
   git add <filename>
   git commit -m '............'
   ----
   git push -u origin add-readme
   ----
   ```
    - create pull request in gui of the GitHub
    - Always double check before creating a pull request that you are sending the right file
4. Updating an Existing Pull Request
    - if asked for any documentation update
    ```text
    nano <filename>
    ---- make some changes
    git commit -a -m 'added more information to the file'
    ----
    git push 
    ----
    ```
    - if we want to create new pull request, we need to create a new branch
5. Squashing Changes
    - As we know we shouldn't rewrite history when commits have been published, this is waved with pull requests, since
      it's only you who have cloned the repo.
    - using `squash` command to combine both commits gives another file to edit
    ```text
    # interactive command of rebase
    git rebase -i main
    ---- use squash in the edit
    # to see the latest commit and changes init
    git show
    ----
    # to see info about the current state
    git status
    ----
    git log --graph --oneline --all -4
    ----
    # replace old commits with new commits
    # use -f force push
    git push -f
    ----
    git log --graph --oneline --all -4
    ----
    ```
    - see the contents of the pull request in GitHub
6. Git Forks and Pull Requests
    - Pull Requests
        - Pull requests allow you to inform fellow contributors about changes that have been made to a branch in Git
            - Make changes to the file
            - Change the proposal and complete a description of the change
            - Click the Proposed File Change button to create a commit in the forked repo to send the change to the
              owner
            - Enter comments about the change
            - Click Create Pull Request
        - When creating multiple commits, a number next to the pull request serves as the identifier for accessing the
          pull requests in the future
    - Pull request merges
        - merge commits (all commits of feature branch to base(main) branch using `--no-ff` option)
        - squash and merge commits (multiple commits combined into single commit using `-ff` option)
        - merge message for a squash merge
        - rebase and merge commits
        - indirect merges

### Code Reviews

1. What are Code Reviews?
    - Going through someone else's code, documentation, or configuration and checking that it all makes sens and follows
      the expected patterns
    - The goal is to improve the project by making sure that changes are high quality.
    - They increase the number of eyes on code, increasing code quality and reduces amount of bugs
    - Coder V tool (used when the other person in at different location/zone) let us comment on someone else's code
    - Common code issues
        - unclear names
        - forgetting to add a test
        - forgetting to handle a specific condition
    - Code reviews are for making code better
2. The Code Review Workflow
    - After making changes to code, we'll ask the reviewer to check the code.
    - Reviewers will find something that needs improving, so they'll add comments that needs to be fixed and how.
    - When we get those comments, we'll address them by fixing
    - Then we mark it as resolved so that we know it's been taken care of. If not sure how to fix reply to the comment
      and ask for more information without making comment as resolved.
    - Once all comments are resolved and reviewer is satisfied, then they'll approve the change, and we'll be able to
      merge it.
    - Lot of python projects follow PEP8 coding style guide
3. How to use Code Reviews in GitHub
    ```text
    ---- do some changes to fix the reviewer comments then add and amend to previous commit
    git commit -a --amend
    ---- edit the original commit
    git status
    ----
    # forcing pushes is fine for PR branches as nobody else should have cloned it
    git push -f
    ----
    ```
4. More Information on Code Reviews
    - Common code review strategies
        - Pair programming
        - The email thread
        - Over the shoulder
        - Tool assisted
    - Pull request reviews
        - tips
            - be selective with reviewers
            - timely reviews
            - constructive feedback
            - detailed pull request description
            - interactive rebasing

### Managing Projects

1. Managing Collaboration
    - Clear documentation
    - If you're a project maintainer, it's important that you reply promptly to pull requests and don't let them
      stagnate.
    - It's important that you understand any changes you accept.
    - When it comes to coordinating who does what and when, a common strategy for active software projects is to use an
      `issue tracker`.
    - way of communication
        - mailing list
        - IRC channels
        - **Slack channels**
        - Telegram groups
2. Tracking Issues
    - Inbuilt in GitHub
3. Continuous Integration (CI/CD : continuous integration / continuous deployment(delivery))
4. Integration git and GitHub
    - If you don’t want to enter your username and password every time, you can store them in a file called .netrc in
      your home directory
    ```text
    machine GitHub.com
        login my-username
        password my-password
    
    machin api.GitHub.com
        login my-username
        password my-password
    ```
    - Command-line HTTPS with token
        - Instead of storing your password in plaintext in the .netrc file, you can generate a personal access token and
          use that in place of your password
    - Git Credential Manager (GCM)
        - A tool that securely stores your passwords and supplies them to Git without your intervention
    - SSH Authentication
        - To add your SSH key for use with GitHub
            - Find the public key you generated in the previous module (id_rsa.pub)
            - Open GitHub.com, Settings -> SSH & GPG Keys -> New SSH Key -> paste public key content
5. GitHub Project Management Tools
    - GitHub Projects
        - Projects can be created in a repository, and then issues can be added to them
        - create an adaptable spreadsheet, task-board, and road map which integrates with your issues and pull requests
        - can filter, sort, and group your issues and pull requests and customize to fit your team’s workflow
    - GitHub Issues
        - track tasks that you need to complete
        - an issue can be a bug, a feature request, or a housekeeping task (like upgrading a library to the latest
          version)
        - Issues can have extensive text and descriptions attached to them, including screenshots and snippets of code.
        - Issues can be discussed, commented on, assigned to people, and tagged
    - Traditional project management
6. Additional Tools

### Glossary

**Terms and definitions from Course 3, Module 4**

- **CI/CD**: The name for the entire continuous integration and continuous deployment system
- **Code reviews**: The deliberate and methodical gathering of other programmers to examine each other's code for errors
  to
  increase the code quality and reduces the amount of bugs
- **Continuous deployment (CD)**: New code is deployed often after it has been automatically built and tested
- **Continuous integration (CI)**: A system that will automatically build and test our code every time there's a change
- **Fix up**: The decision to discard commit messages for that commit
- **Forking**: A way of creating a copy of the given repository so that it belongs to our user
- **Indirect merges**: GitHub can merge a pull request automatically if the head branch is directly or indirectly merged
  into the base branch externally
- **Issue tracker (bug tracker)**: A tracker that shows tasks that need to be done, the state they're in and who's
  working
  on them
- **Merge commits**: All commits from the feature branch are added to the base branch
- **Pipelines**: The specific steps that need to run to obtain the desired result
- **Pull request**: A procedure where new code is examined before it is merged to create a branch or master branch
- **Squash commits**: The decision add commit messages together and an editor opens to make any necessary changes

### Qwiklabs Assessment

For this project, you'll need to fork an existing repository, fix a bug in a script, push your commit to GitHub, and
create a pull request with your commit.

**What you'll do**

1. Fork another repository
2. Commit changes to your own fork and create pull requests to the upstream repository
3. Gain familiarity with code reviews, and ensure that your fix runs fine on your system before creating the pull
   request
4. Describe your pull request

### IT Skills in action

- Implement version control using git and GitHub
- Branch and merge your work
- Secure and restore repositories
- Resolve code conflicts
- Run code reviews and manage pull requests
- Use versioning to track and manage projects

**The project**

Imagine you're part of an IT team responsible for developing and managing a software project. Your team is using Git
for version control, collaborating on coding tasks, and ensuring project success. Let's walk through the process step
by step.

**Project steps**

Before Version Control:  
Before diving into code, ensure your team is aligned on the project's scope, goals, and
responsibilities.

Version control systems:  
Choose GitHub as your version control system to track changes, collaborate effectively, and
maintain a history of your project.

Using git:  
Start by initializing a GitHub repository, committing your initial code, and using git status and git log to
manage and track changes.

Advanced git interaction:  
Use advanced commands like git diff to visualize changes, git stash to temporarily hide
changes, and git tag to mark significant milestones.

Undoing things:  
Use git reset and git revert to undo changes and address errors in a controlled manner.

Branching and merging:  
Create branches for feature development using git branch, switch between branches with git
checkout, and merge changes using git merge.

Secure shells & API keys:  
Ensure security by using SSH keys and managing sensitive data like API keys properly.

Solving conflicts:  
Resolve conflicts that arise from merging branches using git merge or pull requests.

Pull requests:  
Open pull requests to propose changes, review code, and discuss modifications with your team.

Code reviews:  
Participate in code reviews to maintain code quality, identify improvements, and ensure best practices.

Managing projects:  
Organize your project using project boards, milestones, and issues to track progress and prioritize
tasks.

**Putting it all together**

Imagine you're assigned to add a new feature to your project: a user authentication system. Here's how you'd apply your
skills:

Before version control:  
Working with your development team and stakeholders you define the feature's scope and
priorities. From the business requirements you develop user stories from which the team can build out tasks. Review the
tasks your team created and discuss expected outcomes.

Version control systems:  
You create a feature branch for the authentication system on the app's existing repository that
is already located on GitHub. Your team uses this new branch to begin to work on the tasks associated with the feature
request.All progress is tracked in real time and documented with comments in GitHub.

```text
# Create a new feature branch
git checkout -b feature/user-authentication
```

Advanced git interaction:  
You use git diff to view and compare code changes and look back at the history of changes.
When needed you can use git diff to compare whole branches as the feature becomes more robust. As you get closer to
completing the feature you create tags to mark development milestones. When feature release is approaching, you can use
a milestone to share progress with stakeholders.

```text
# View code changes
git diff
```

```text
# View commit history
git log
```

```text
# Create a new tag
git tag v1.0.0
```

```text
# Compare branches
git diff feature/user-authentication main
```

Undoing things:  
As you encounter issues, you have stable milestones you know you can restore back. You can stash away
pending changes or, safely undo changes using Git's commands.

```text
# Stash changes
git stash
```

```text
# Restore changes from stash
git stash pop
```

```text
# Undo changes in working directory
git checkout -- <file>
```

Branching and merging:  
Your team makes sure to keep up with branching and merging changes. The team tests their changes
in the feature branch to avoid introducing any issues or bugs into the main branch.

```text
# Merge changes from feature branch to main
git checkout main
git merge feature/user-authentication
```

```text
# Delete feature branch
git branch -d feature/user-authentication
```

Solving Conflicts:  
As code conflicts arise during merging, you attempt to automerge. When deeper conflicts arise, you
gather your team and address them collaboratively.

```text
# Attempt to automerge
git merge feature/user-authentication
```

```text
# Resolve conflicts manually
# Edit files to resolve conflicts
git add <resolved-files>
git commit -m "Resolved conflicts"
```

Pull requests and code reviews:  
One of your team members opens up a pull request for your feature branch. It is finally
time to merge our feature into the main branch. Automated tests run against the code in question and your team schedules
a code review. You prepare to gather and track feedback.

```text
# Push changes and open pull request
git push origin feature/user-authentication
```

```text
# Automated tests run in CI/CD pipeline
# Pull request is reviewed
# Feedback is addressed
```

Code reviews:  
All concerned parties participate in code reviews. Team members address the group and review their code
additions. Tests and metrics are also reviewed. The team collaborates at addressing feedback and ensuring high-quality
code.

Managing projects:   
Throughout the project, and even after development efforts have concluded, you continue to track the
progress of your feature using project boards, milestones, and issues. Development is iterative and your team will
continue to work on features as feedback and requests come in from stakeholders.

By applying your skills across the development life-cycle, you've successfully contributed to the project's growth and
demonstrated your expertise in IT and project management.

### Preparing your Resume

### Wrap Up