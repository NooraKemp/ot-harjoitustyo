from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(cxt):
    cxt.run("coverage run --branch -m pytest")

@task
def coverage_report(cxt):
    cxt.run("coverage html")

@task
def lint(cxt):
    cxt.run("pylint src")

@task
def format(cxt):
    cxt.run("autopep8 --in-place --recursive src")
