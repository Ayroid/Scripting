import os


def clone_or_pull_repo(repo_url, local_dir):
    if not os.path.exists(local_dir):
        os.system(f"git clone {repo_url} {local_dir}")
        print(f"Cloned {repo_url} to {local_dir}")
    else:
        os.chdir(local_dir)
        os.system("git pull")
        print(f"Pulled changes for {repo_url} in {local_dir}")


repositories = [
    {
        "url": "https://github.com/Ayroid/Ideos-Frontend",
        "dir": "/home/ayroid/Documents/Private/Projects/Ideos/Frontend",
    },
    {
        "url": "https://github.com/Ayroid/Ideos-Backend",
        "dir": "/home/ayroid/Documents/Private/Projects/Ideos/Backend",
    },
]

for repo in repositories:
    clone_or_pull_repo(repo["url"], repo["dir"])
