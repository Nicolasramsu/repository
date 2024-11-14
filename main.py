import subprocess
import time

def main():
    while True:
        # Run tests and save results to a log file
        subprocess.run(['python', 'test_automation.py'])
        # Make automatic commits and push to the remote repository
        subprocess.run(['python', 'git_automation.py'])
        # Wait for 5 minutes before checking again
        time.sleep(300)

if __name__ == '__main__':
    main()
#soy la monda mijo
