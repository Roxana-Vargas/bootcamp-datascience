from prefect import task

@task
def load(data):
    load_data = data
    