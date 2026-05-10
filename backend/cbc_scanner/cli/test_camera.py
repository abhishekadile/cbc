import typer
from rich import print
from cbc_scanner.hardware.device_status import get_camera_instance

app = typer.Typer()

@app.command()
def main():
    print("[bold blue]Testing Camera Connection...[/bold blue]")
    try:
        cam = get_camera_instance()
        success = cam.test()
        status = cam.get_status()
        if success:
            print(f"[bold green]Success![/bold green] Camera connected: {status}")
        else:
            print("[bold red]Failed to connect to camera.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error testing camera:[/bold red] {e}")

if __name__ == "__main__":
    app()
