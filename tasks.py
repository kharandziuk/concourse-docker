from invoke import task


CI_NAME = 'compose'

@task
def ci_server(c):
    c.run('docker-compose up -d')


@task(ci_server)
def concourse_login(c):
    c.run(f'fly login -t {CI_NAME} -u test -p test -c http://localhost:8080')


@task(concourse_login)
def set_pipelines(c):
    c.run(f'fly -t {CI_NAME} set-pipeline -c pipeline.yml -p main')
