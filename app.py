from app import create_app


app = create_app()


@app.shell_context_processor
def make_shell_context():
    """
    Allows customisation of the context of '> flask shell'

    Fill dict with <'item': item>.
    """
    return {}
