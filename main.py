from scraper import scrape_cs_scripts
from github_search import search_github_file
from tqdm import tqdm
from rich.console import Console  # Import Rich Console for formatted output

if __name__ == "__main__":
    # Initialize Rich console for formatted output
    console = Console()

    # Start by scraping C# scripts with a single progress bar
    console.print("[bold green]Starting the scraping process...[/bold green]")

    # Create a progress bar for the entire process
    with tqdm(total=100, desc="Overall Progress", unit="step") as progress_bar:
        # Step 1: Execute web scraping to get the list of C# scripts
        cs_scripts = scrape_cs_scripts(progress_bar)

        # Limit the number of script names to 5
        if cs_scripts:
            cs_scripts = cs_scripts[:5]  # Limit to the first 5 scripts

            # Step 2: Search for the files on GitHub
            repo_matches = search_github_file(cs_scripts, progress_bar)
            progress_bar.update(10)  # Final update to complete the bar

            # Display the results using rich console with hyperlinks
            console.print("\n[bold green]Repositories with matches:[/bold green]\n")
            for repo_url, details in repo_matches.items():
                repo_name = repo_url.split('/')[-1]  # Extract the repository name from the URL
                console.print(f"[link={repo_url}]{repo_name}[/link]: [bold]Matches:[/bold] {details['count']} [bold]Last Updated:[/bold] {details['last_updated']}\n")

        else:
            console.print("[bold red]No C# scripts found during scraping.[/bold red]")
