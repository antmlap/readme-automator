import datetime
import subprocess

# Step 1: Load current README content
with open("README.md", "r") as f:
    lines = f.readlines()

# Step 2: Create updated status line
today = datetime.date.today().strftime("%B %d, %Y")
status = f"⏰ Last updated: {today}\n🛠️ Currently working on: Folder Cleaner, PDF Renamer\n"

# Step 3: Replace the first two lines
lines[0:2] = [status, "\n"]

# Step 4: Save the updated README
with open("README.md", "w") as f:
    f.writelines(lines)

# Step 5: Git add, commit, and push
subprocess.run(["git", "add", "README.md"])
subprocess.run(["git", "commit", "-m", "Auto-update README"])
subprocess.run(["git", "push"])
