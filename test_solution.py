import os
import subprocess
import pytest
import shutil

@pytest.fixture(scope="module")
def setup_teardown(tmpdir_factory):
    cwd = os.path.join(os.environ["HOME"],os.environ["NAME"])
    result = subprocess.run(["bash","init.sh"], capture_output=True, text=True,cwd=cwd)
    assert result.returncode == 0, f"init.sh failed: {result.stderr}"

    res = {
        "project_dir" : os.path.join(os.environ["HOME"],os.environ["NAME"]),
        "cwd" : os.path.join(os.environ["HOME"],os.environ["NAME"],"repo")
    }
    # import ipdb;ipdb.set_trace()
    result = subprocess.run(["bash", "solution.sh"], capture_output=True, text=True,cwd=res['project_dir'])
    res["solution.sh_stdout"] = result.stdout 
    res["solution.sh_stderr"] = result.stdout
    res["solution.sh_returncode"] = result.returncode
    # Yield the paths for test cases
    yield res
	
    if os.path.exists("/tmp/git-remote-repo"):
        shutil.rmtree("/tmp/git-remote-repo")
    if os.path.exists(res['cwd']):
        shutil.rmtree(res['cwd'])
    if res.get("solution.sh_stdout"):
        print("\n\nOutput of solution.sh")
        print("---------------------")
        print(res["solution.sh_stdout"])
        print(res["solution.sh_stderr"])

# Define the repository path (adjust this as needed)
home=os.environ.get('HOME')
name=os.environ.get('NAME')
REPO_PATH = os.path.join(home,name,"repo")

# Helper function to run git commands in the specific repository
def run_git_command(command,cwd):
    """ Helper function to run a git command in the specific repository """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True,cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

# Test case for checking the git username
def test_git_username(setup_teardown):
    """ Test if Git username is set correctly at the repository level """
    username = run_git_command(["git", "config", "--local", "user.name"],cwd=setup_teardown['cwd'])
    assert username == "Hacker Developer", "Git username is incorrect or not set locally."

# Test case for checking the git email
def test_git_email(setup_teardown):
    """ Test if Git email is set correctly at the repository level """
    email = run_git_command(["git", "config", "--local", "user.email"],cwd=setup_teardown['cwd'])
    assert email == "hacker.developer@hackercompany.com", "Git email is incorrect or not set locally."

# Test case for checking the commit message
def test_git_commit(setup_teardown):
    """ Test if commit with the correct message exists """
    last_commit_message = run_git_command(["git", "log", "-1", "--pretty=%B"],cwd=setup_teardown['cwd'])
    assert last_commit_message == "Initial Implementation", "The commit message is incorrect or no commit has been made."

# Test case for checking if changes are pushed to the remote origin
def test_git_push(setup_teardown):
    """ Test if changes are pushed to the remote origin """
    try:
        push_status = run_git_command(["git", "rev-list", "HEAD..origin/master", "--count"],cwd=setup_teardown['cwd'])
        assert push_status == "0", "Changes are not pushed to the remote origin."
    except Exception as e:
        pytest.fail(f"Failed to push changes: {str(e)}")
