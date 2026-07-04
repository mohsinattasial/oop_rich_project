import time
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.progress import Progress


class StudentDashboard(Table):
    
    def __init__(self, project_name, **kwargs):
       
        title_text = Text(f"Project: {project_name}", style="bold magenta")
        
        super().__init__(title=title_text, show_lines=True, **kwargs)
        
       
        self.add_column("Team Member", style="bold cyan")
        self.add_column("Assigned Task", style="green")
        self.add_column("Status", style="yellow")

    # Add a new task to the dashboard
    def add_member_task(self, name, task, is_done=False):
        # Check if the task is finished
        if is_done:
            status_display = "[bold green]Completed[/]"
        else:
            status_display = "[bold red]Pending[/]"
            
        self.add_row(name, task, status_display)


if __name__ == "__main__":
    # Create console to print output
    console = Console()
    
    console.print("\n[bold yellow]System Initializing...[/]")
    
    # Show a loading bar
    with Progress() as progress:
        loading_task = progress.add_task("[cyan]Loading project data...", total=100)
        
        while not progress.finished:
            progress.update(loading_task, advance=20)
            time.sleep(0.5) # Fake delay
            
    # Create the dashboard object
    dashboard = StudentDashboard("OOP Final Term - Rich Library")
    
    # Add group member data
    dashboard.add_member_task("Mohsin", "Custom Code & UML Diagram", True)
    dashboard.add_member_task("Qazi Reyan", "Report Writing & Analysis", True)
    dashboard.add_member_task("Rehan Bukhari", "Presentation Preparation", True)
    
    # Put the table inside a box (Panel)
    final_output = Panel(dashboard, title="[bold blue]Group Status[/]", expand=False)
    
    # Print the final result
    console.print(final_output)
