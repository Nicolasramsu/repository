import json
import subprocess
import os

def load_config(config_file):
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def git_add_all():
    """Stage all changes in the repository."""
    subprocess.run(['git', 'add', '.'])

def git_commit(commit_message):
    """Commit changes with a meaningful message."""
    subprocess.run(['git', 'commit', '-m', commit_message])

def git_push(remote_repository):
    """Push changes to the remote repository."""
    subprocess.run(['git', 'push', remote_repository])

def main():
    config = load_config('config.json')
    git_add_all()
    git_commit(config['commit_message'])
    git_push(config['git_remote_repository'])

if __name__ == '__main__':
    main()
