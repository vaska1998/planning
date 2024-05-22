import click
import uvicorn


@click.group()
def cli():
    pass


@cli.command()
def sqlalchemy():
    uvicorn.run('api:app', host='0.0.0.0', port=7000, reload=True)


@cli.command()
def peewee():
    uvicorn.run('api_peewee:app', host='0.0.0.0', port=8000, reload=True)


cli.add_command(sqlalchemy)
cli.add_command(peewee)
cli()