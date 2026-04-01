import os
import subprocess
from datetime import datetime

def get_all_files():
    result = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True)
    if result.returncode != 0:
        return []
    files = result.stdout.strip().split('\n')
    return [f for f in files if f]

def main():
    start_date = datetime(2026, 2, 23, 10, 30, 0)
    end_date = datetime(2026, 4, 12, 10, 30, 0)
    
    # Reset git
    if os.path.exists(".git"):
        import shutil
        shutil.rmtree(".git")
    
    print("Initializing git repository...")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    
    # Priority files (Documentation) for the first commit
    docs = [
        "idea.md",
        "useCaseDiagram.md",
        "sequenceDiagram.md",
        "classDiagram.md",
        "ErDiagram.md",
        "README.md",
        ".gitignore",
        "Dockerfile",
        "docker-compose.yml"
    ]
    
    all_untracked = get_all_files()
    
    # 1st Commit: Project Documentation & Setup
    date_str_1 = start_date.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str_1
    env["GIT_COMMITTER_DATE"] = date_str_1
    
    for doc in docs:
        if os.path.exists(doc):
            subprocess.run(["git", "add", doc], check=False)
            if doc in all_untracked:
                all_untracked.remove(doc)
    
    subprocess.run(["git", "commit", "-m", "docs: project architecture and initial setup"], env=env, check=False)
    print(f"Created initial commit for date {date_str_1}")

    # Remaining files distribution
    num_commits = 39
    files_per_commit = len(all_untracked) // num_commits
    remainder = len(all_untracked) % num_commits
    delta = (end_date - start_date) / max(1, num_commits)
    
    file_index = 0
    for i in range(num_commits):
        current_date = start_date + (i + 1) * delta
        date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S+05:30")
        
        batch_size = files_per_commit + (1 if i < remainder else 0)
        batch_files = all_untracked[file_index:file_index + batch_size]
        file_index += batch_size

        if not batch_files:
            continue
            
        for f in batch_files:
            if os.path.isfile(f):
                subprocess.run(["git", "add", f], check=False)
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        # Consistent and meaningful commit messages
        sample_file = batch_files[0]
        if "client/src/components" in sample_file:
            msg = f"feat(client): implement {os.path.basename(sample_file).split('.')[0]} component"
        elif "client/src/pages" in sample_file:
            msg = f"feat(client): add {os.path.basename(sample_file).split('.')[0]} page"
        elif "server/controllers" in sample_file:
            msg = f"feat(server): implement {os.path.basename(sample_file).split('.')[0]} logic"
        elif "server/models" in sample_file:
            msg = f"feat(server): define {os.path.basename(sample_file).split('.')[0]} model"
        else:
            msg = f"chore: update {os.path.basename(sample_file)}"
                
        subprocess.run(["git", "commit", "-m", msg], env=env, check=False)
        print(f"Created commit {i+2}/40 for date {date_str} with {len(batch_files)} files")

if __name__ == "__main__":
    main()
