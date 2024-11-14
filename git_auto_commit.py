import json
import subprocess
import sys

def load_config(file_path):
    """Loads configuration from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Configuration file not found.")
        sys.exit(1)

def git_auto_commit(config):
    """Makes an automatic Git commit and pushes to the remote repository."""
    try:
        # Add all changes
        subprocess.run(["git", "add", "."])
        
        # Commit changes
        commit_message = "Automatic commit"
        subprocess.run(["git", "commit", "-m", commit_message])
        
        # Push changes to the remote repository
        subprocess.run(["git", "push", "-u", "origin", config["git_branch"]])
        print("Changes committed and pushed successfully.")
    except Exception as e:
        print(f"Error committing and pushing changes: {e}")

if __name__ == "__main__":
    config_file = "config.json"
    config = load_config(config_file)
    git_auto_commit(config)