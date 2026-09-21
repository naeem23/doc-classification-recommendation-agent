import typer

app = typer.Typer()

@app.command()
def hello():
    print("Classification app is alive.")

if __name__ == "__main__":
    app()
