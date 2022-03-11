from invoke import task
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))

@task
def start(ctx):
    ctx.run(f'cd {dir_path}/src && flask run')

@task
def dev(ctx):
    ctx.run(f'cd {dir_path}/src && FLASK_ENV=development flask run')

@task
def test(ctx):
    ctx.run(f'export DEV_ENVIRON=True && pytest {dir_path}/src')

@task
def robot(ctx):
    ctx.run(f'robot {dir_path}/src/tests')

@task
def coverage(ctx):
    ctx.run(f'coverage run --branch -m pytest {dir_path}/src')

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report')

@task(coverage)
def coverage_html(ctx):
    ctx.run('coverage html')

@task
def lint(ctx):
    ctx.run(f'pylint {dir_path}/src')

@task
def format(ctx):
    ctx.run(f'autopep8 --in-place --recursive {dir_path}/src')

