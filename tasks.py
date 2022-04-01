from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(cxt):
    cxt.run("coverage run --branch -m pytest", pty=True)

@task
def coverage_report(cxt):
    cxt.run("coverage html", pty=True)
