import os
import shutil
import sys
import datetime
import argparse


SERVER_PATH = "T:\\"
# INTERVAl = "600"
IGNORE_LIST = [__name__, ".venv", ".idea", "__pycache__"]


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        if item not in IGNORE_LIST:
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
                print("[sunsetgit] Copying {}...".format(s.split("\\")[-1]))


def create_commit():
    print("[sunsetgit] Starting create new commit")
    dir_name = os.getcwd().split("\\")[-1]
    try:
        os.mkdir(SERVER_PATH + "\\" + dir_name + "_commits")
    except FileExistsError:
        pass
    high_commit_level = SERVER_PATH + "\\" + dir_name + "_commits"
    try:
        os.mkdir(high_commit_level + "\\COMMIT " + datetime.datetime.now().strftime("%d-%m-%Y, %H-%M"))
    except FileExistsError:
        pass
    commit_level = high_commit_level + "\\COMMIT " + datetime.datetime.now().strftime("%d-%m-%Y, %H-%M")
    copytree(os.getcwd(), commit_level)
    print("[sunsetgit] Commit created!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument('action', nargs='?', default='мир')
    args = parser.parse_args()

    if args.action == "commit":
        create_commit()
    else:
        print("[sunsetgit] Invalid argument! Try \"local_commit commit \"")
