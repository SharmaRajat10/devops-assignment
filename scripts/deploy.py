import os
import subprocess
import shutil
import time

REPO_URL = "https://github.com/SharmaRajat10/devops-assignment.git"
PROJECT_DIR = "project"

# Function 1
def clone_repo():

    if not os.path.exists(PROJECT_DIR):

        subprocess.run(
            ["git", "clone", REPO_URL, PROJECT_DIR],
            check=True
        )

        print("Repository cloned successfully!")

    else:

        subprocess.run(
            ["git", "-C", PROJECT_DIR, "pull", "origin", "main"],
            check=True
        )

        print("Repository updated successfully!")

  


# Function 2
def detect_language():

    app_path = os.path.join(PROJECT_DIR, "app")

    if os.path.exists(os.path.join(app_path, "index.html")):
        print("HTML application detected.")
        return "html"

    elif os.path.exists(os.path.join(app_path, "index.php")):
        print("PHP application detected.")
        return "php"

    else:
        print("No supported application found.")
        return None


# Function 3
def create_dockerfile(language):

    if language == "html":

        dockerfile = """

"""

    elif language == "php":

        dockerfile = """

"""

    else:
        print("Unsupported application.")
        return

    with open("Dockerfile", "w") as file:
        file.write(dockerfile)

    print("Dockerfile created successfully!")


# Main Function
if __name__ == "__main__":

    print("Starting Deployment...")

    clone_repo()

    language = detect_language()

    print("Detected Language:", language)

    if language:
        create_dockerfile(language)