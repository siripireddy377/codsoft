import click
from tasks import TaskManager

manager = TaskManager()

@click.group()
def cli():
    """Command-line interface for task management."""
    pass

@cli.command()
@click.argument('title')
@click.argument('description')
def add(title, description):
    """Add a new task with TITLE and DESCRIPTION."""
    manager.add_task(title, description)
    click.echo(f"Task '{title}' added!")

@cli.command()
def list():
    """List all tasks with their status."""
    tasks = manager.list_tasks()
    print("Debug: Retrieved tasks:", tasks) 
    if not tasks:
        click.echo("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else "✗"
            click.echo(f"{i}. {task.title} - {task.description} [{status}]")

@cli.command()
@click.argument('index', type=int)
def complete(index):
    """Mark a task as completed by its INDEX."""
    if manager.mark_task_completed(index):
        click.echo(f"Task {index} marked as completed!")
    else:
        click.echo("Invalid task index.")

if __name__ == '__main__':
    cli()
