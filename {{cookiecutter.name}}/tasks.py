from invoke import task
from pathlib import Path


@task
def venv(c, force=False):
    """Create a virtual environment."""
    if Path("venv").exists() and not force:
        return None
    c.run("python3 -m venv venv --clear")
    c.run("venv/bin/pip install -r requirements.txt")
    c.run("venv/bin/jupyter nbextension install --sys-prefix --py nbgrader --overwrite")
    c.run("venv/bin/jupyter nbextension enable --sys-prefix --py nbgrader")
    c.run("venv/bin/jupyter serverextension enable --sys-prefix --py nbgrader")

@task
def grader(c):
    """Start a nbgrader instance."""
    c.run("venv/bin/jupyter notebook")
