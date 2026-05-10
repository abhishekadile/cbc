import typer
from rich import print
from rich.table import Table
from cbc_scanner.storage.scan_storage import list_scans, get_storage_base

app = typer.Typer()

@app.command()
def main():
    base = get_storage_base()
    print(f"[bold blue]Storage Base Directory:[/bold blue] {base}")
    
    scans = list_scans()
    print(f"[bold green]Total Scans Found:[/bold green] {len(scans)}\n")
    
    if scans:
        table = Table("Scan ID", "Date", "Images")
        for s in scans[:10]: # show last 10
            table.add_row(
                s.get("scan_id", "Unknown"), 
                s.get("created_at", "Unknown"),
                str(len(s.get("images", [])))
            )
        print(table)

if __name__ == "__main__":
    app()
