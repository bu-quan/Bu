# 1. Git is a local version control system, while GitHub is an online platform.
# 2. The Terminal is the program used to access the Command Line.
# 3. A local repository is stored on your computer, while a remote repository is stored online.
# 4. Version control tracks and manages changes to files over time.
# 5. The staging area holds files marked for inclusion in the next commit.
# 6. Adds changes from your working directory to the staging area.
# 7. Saves the staged changes to your local Git repository with a message.
# 8. Uploads your local commits to a remote repository like GitHub.
# 9. Shows which files are staged, unstaged, or untracked.
# 10. Fetches and merges changes from a remote repository into your local one.
# 11. Prints the current working directory’s path.
# 12. Lists all files and folders in the current directory.
# 13. Changes the current working directory.
# 14. Opens a simple terminal text editor to create or edit files.
# 15. Creates a new empty file or updates an existing file’s timestamp.
# 16. Moves or renames files and directories.
# 17. Deletes files or directories permanently.
# 18. Displays the contents of a file in the terminal.
'''
1. pwd
2. ls
3. cd ~/python_decal/brianna_repo
git pull
4. mv homework.py ~/python_decal/judy_decal/homework/
5. cd ~/python_decal/judy_decal/homework/
6. cat homework.py
7. git add .
git commit -m 
git push
8. git pull
git push
9. cd ~/Recents/
'''
def checkDataType(x):
    return type(x).__name__
checkDataType(True)

def evenOrOdd(x):
    if x%2==1:
        return 'Odd'
    else:
        return 'Even'
evenOrOdd(3)

def sumWithLoop(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
sumWithLoop([1,2,3])

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list
duplicateList([1,2])

def square(num):
    return num * num
square(6)


