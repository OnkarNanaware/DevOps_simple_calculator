a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

def addition(a,b):
	result = a + b
	print("Addition: " + (result))

def subtraction(a,b):
    result = a - b
    print("Subtraction: " + (result))
    
def multiplication(a,b):
    result = a * b
    print("Multiplication: " + (result))
    
def divison(a,b):
    result = a / b
    print("Division: " + (result))
    
def modulus(a,b):
    result = a % b
    print("Modulus: " + (result))
    
addition(a,b)
subtraction(a,b)
multiplication(a,b)
division(a,b)
modulus(a,b)

administrator@administrator-OptiPlex-5060:~/33326$ git --version
git version 2.53.0
administrator@administrator-OptiPlex-5060:~/33326$ cd 33326_demo1
bash: cd: 33326_demo1: No such file or directory
administrator@administrator-OptiPlex-5060:~/33326$ mkdir 33326_demo1
administrator@administrator-OptiPlex-5060:~/33326$ cd 33326_demo1
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /home/administrator/33326/33326_demo1/.git/
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   calc.py

administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   calc.py

administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
fatal: your current branch 'master' does not have any commits yet
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "Initial program"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'administrator@administrator-OptiPlex-5060.(none)')
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   calc.py

administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
fatal: your current branch 'master' does not have any commits yet
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ ^C
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git config --global user.email "you@example.com"
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "Initial program"
[master (root-commit) ec4094e] Initial program
 1 file changed, 13 insertions(+)
 create mode 100644 calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master
nothing to commit, working tree clean
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit ec4094e719a48cccf96d54f23af9a801f7ac34fe (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log --oneline
ec4094e (HEAD -> master) Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "Added modulus"
On branch master
nothing to commit, working tree clean
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master
nothing to commit, working tree clean
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ got log
Command 'got' not found, but can be installed with:
sudo apt install got
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit ec4094e719a48cccf96d54f23af9a801f7ac34fe (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log --oneline
ec4094e (HEAD -> master) Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git show ec4094e719a48cccf96d54f23af9a801f7ac34fe
commit ec4094e719a48cccf96d54f23af9a801f7ac34fe (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program

diff --git a/calc.py b/calc.py
new file mode 100644
index 0000000..8115a2b
--- /dev/null
+++ b/calc.py
@@ -0,0 +1,13 @@
+a = int(input("Enter 1st number : "))
+b = int(input("Enter 2nd number : "))
+
+def addition(a,b):
+       result = a + b
+       print(result)
+       
+addition(a,b)  
+       
+       
+       
+       
+       
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit ec4094e719a48cccf96d54f23af9a801f7ac34fe (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git stATUS
git: 'stATUS' is not a git command. See 'git --help'.
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git status
On branch master
nothing to commit, working tree clean
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "Added modulus"
[master ad46db4] Added modulus
 1 file changed, 23 insertions(+), 3 deletions(-)
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit ad46db4445e4d32d915a4e8ef471cf05372fbc74 (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "Eliminated errors"
[master 42726e6] Eliminated errors
 1 file changed, 6 insertions(+), 6 deletions(-)
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit 42726e602c4870149826fc5fa9f29bd74123bc85 (HEAD -> master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:37:54 2026 +0530

    Eliminated errors

commit ad46db4445e4d32d915a4e8ef471cf05372fbc74
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git switch newbranch
fatal: invalid reference: newbranch
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git switch -c newbranch
Switched to a new branch 'newbranch'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "added new branch"
On branch newbranch
nothing to commit, working tree clean
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit 42726e602c4870149826fc5fa9f29bd74123bc85 (HEAD -> newbranch, master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:37:54 2026 +0530

    Eliminated errors

commit ad46db4445e4d32d915a4e8ef471cf05372fbc74
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git switch master
Switched to branch 'master'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git merge newbranch
Already up to date.
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit 42726e602c4870149826fc5fa9f29bd74123bc85 (HEAD -> master, newbranch)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:37:54 2026 +0530

    Eliminated errors

commit ad46db4445e4d32d915a4e8ef471cf05372fbc74
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git switch newbranch
M	calc.py
Switched to branch 'newbranch'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git add calc.py
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git commit -m "added sqrt"
[newbranch 2d768dc] added sqrt
 1 file changed, 6 insertions(+)
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit 2d768dc64b2253a922d96c5357ece82785d500bf (HEAD -> newbranch)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:50:55 2026 +0530

    added sqrt

commit 42726e602c4870149826fc5fa9f29bd74123bc85 (master)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:37:54 2026 +0530

    Eliminated errors

commit ad46db4445e4d32d915a4e8ef471cf05372fbc74
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git switch master
Switched to branch 'master'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git merge newbranch
Updating 42726e6..2d768dc
Fast-forward
 calc.py | 6 ++++++
 1 file changed, 6 insertions(+)
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git log
commit 2d768dc64b2253a922d96c5357ece82785d500bf (HEAD -> master, newbranch)
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:50:55 2026 +0530

    added sqrt

commit 42726e602c4870149826fc5fa9f29bd74123bc85
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:37:54 2026 +0530

    Eliminated errors

commit ad46db4445e4d32d915a4e8ef471cf05372fbc74
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:34:26 2026 +0530

    Added modulus

commit ec4094e719a48cccf96d54f23af9a801f7ac34fe
Author: administrator <you@example.com>
Date:   Tue Jul 21 13:17:33 2026 +0530

    Initial program
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git remote -v
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git remote add origin https://github.com/akshitakarnavat/33326_Assignment1.git
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git remote -v
origin	https://github.com/akshitakarnavat/33326_Assignment1.git (fetch)
origin	https://github.com/akshitakarnavat/33326_Assignment1.git (push)
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/akshitakarnavat/33326_Assignment1.git'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push origin master
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/akshitakarnavat/33326_Assignment1.git/'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push origin master
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/akshitakarnavat/33326_Assignment1.git/'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push origin master
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/akshitakarnavat/33326_Assignment1.git/'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push origin master
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/akshitakarnavat/33326_Assignment1.git/'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git remote add origin https://github.com/akshitakarnavat/33326_Assignment1.git
git branch -M main
git push -u origin main
error: remote origin already exists.
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/akshitakarnavat/33326_Assignment1.git/'
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ ^C
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ git push -u origin main
Username for 'https://github.com': akshitakarnavat
Password for 'https://akshitakarnavat@github.com': 
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 6 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (12/12), 1.16 KiB | 1.16 MiB/s, done.
Total 12 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/akshitakarnavat/33326_Assignment1.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
administrator@administrator-OptiPlex-5060:~/33326/33326_demo1$ 


	
	
	
	
	
