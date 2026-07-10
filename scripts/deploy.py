import os
import subprocess
import shutil
import time

REPO_URL = "https://github.com/SharmaRajat10/devops-assignment.git"
PROJECT_DIR = "project"

# Function 1
def clone_repo():

    if not os.path.exists(PROJECT_DIR):

        print("Cloning repository...")

        subprocess.run(
            ["git", "clone", REPO_URL, PROJECT_DIR],
            check=True
        )

        print("Repository cloned successfully!")

    else:

        print("Repository already exists. Pulling latest changes...")

        subprocess.run(
            ["git", "-C", PROJECT_DIR, "pull", "origin", "main"],
            check=True
        )

        print("Repository updated successfully!")
  


# Function 2
def detect_language():

    app_path = os.path.join(PROJECT_DIR, "app")

    print("Checking path:", app_path)

    print("App folder exists:", os.path.exists(app_path))

    print("HTML exists:", os.path.exists(os.path.join(app_path, "index.html")))

    print("PHP exists:", os.path.exists(os.path.join(app_path, "index.php")))

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


#Function 4
IMAGE_NAME = "devops-app"

def build_docker_image():

    print("Building Docker image...")

    result = subprocess.run(
        ["docker", "build", "-t", IMAGE_NAME, "."],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode == 0:
        print("Docker image built successfully!")
    else:
        print("Docker build failed!")


# Function 5: Deploy to Kubernetes
def deploy_to_kubernetes():

    print("Deploying application to Kubernetes...")

    result = subprocess.run(
        ["kubectl", "apply", "-f", "k8s"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode == 0:
        print("Application deployed successfully!")
    else:
        print("Kubernetes deployment failed!")

# Function 6: Monitor Repository
def monitor_repository():

    print("Monitoring repository...")

    while True:

        result = subprocess.run(
            ["git", "-C", PROJECT_DIR, "pull", "origin", "main"],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if "Already up to date." not in result.stdout:

            print("Changes detected!")

            language = detect_language()

            if language:
                create_dockerfile(language)
                build_docker_image()
                deploy_to_kubernetes()

        time.sleep(30)

# Main Function
if __name__ == "__main__":

    print("Starting Deployment...")

    clone_repo()

    language = detect_language()

    print("Detected Language:", language)

    if language:
        create_dockerfile(language)
        build_docker_image()
        deploy_to_kubernetes()
        monitor_repository()