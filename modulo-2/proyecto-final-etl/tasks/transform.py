from prefect import task

@task
def transform(data):
    transform_data = data
    return transform_data