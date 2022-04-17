from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(cxt):
    cxt.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(cxt):
    cxt.run("coverage html", pty=True)

@task
def lint(cxt):
    cxt.run("pylint src", pty=True)

@task
def format(cxt):
    cxt.run("autopep8 --in-place --recursive src", pty=True)

@task
def build(cxt):
    cxt.run("python3 src/build.py", pty=True)
