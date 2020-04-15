@app.cli.command()
@click.option(
    "--workers", "-w", type=int, help="Number of celery server workers to fire up"
)
def worker(workers):
    """Starts a Superset worker for async SQL query execution."""
    logging.info(
        "The 'superset worker' command is deprecated. Please use the 'celery "
        "worker' command instead."
    )
    if workers:
        celery_app.conf.update(CELERYD_CONCURRENCY=workers)
    elif config.get("SUPERSET_CELERY_WORKERS"):
        celery_app.conf.update(
            CELERYD_CONCURRENCY=config.get("SUPERSET_CELERY_WORKERS")
        )

    worker = celery_app.Worker(optimization="fair")
    worker.start()
