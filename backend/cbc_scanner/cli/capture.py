import typer
from rich import print
from cbc_scanner.acquisition.scan_runner import run_single_capture

app = typer.Typer()

@app.command()
def main():
    print("[bold blue]Initiating single capture...[/bold blue]")
    try:
        scan_id = run_single_capture()
        print(f"[bold green]Capture complete![/bold green] Scan ID: {scan_id}")
    except Exception as e:
        print(f"[bold red]Error during capture:[/bold red] {e}")

if __name__ == "__main__":
    app()
