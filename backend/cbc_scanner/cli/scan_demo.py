import typer
from rich import print
from cbc_scanner.acquisition.scan_runner import run_demo_multispectral

app = typer.Typer()

@app.command()
def main():
    print("[bold blue]Initiating demo multispectral scan...[/bold blue]")
    try:
        scan_id = run_demo_multispectral()
        print(f"[bold green]Scan complete![/bold green] Scan ID: {scan_id}")
    except Exception as e:
        print(f"[bold red]Error during scan:[/bold red] {e}")

if __name__ == "__main__":
    app()
