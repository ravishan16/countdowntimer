from invoke import task

@task
def deploy(c):
    c.run("aws s3 cp . s3://hackathon-timer/ --recursive")
