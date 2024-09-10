from scraper import scrape_cs_scripts
from github_search import search_github_file
from tqdm import tqdm

if __name__ == "__main__":
    # Start by scraping C# scripts with a single progress bar
    print("Starting the scraping process...")

    # Create a progress bar for the entire process
    with tqdm(total=100, desc="Overall Progress", unit="step") as progress_bar:
        # Step 1: Execute web scraping to get the list of C# scripts
        cs_scripts = scrape_cs_scripts(progress_bar)

        # Limit the number of script names to 5
        if cs_scripts:
            cs_scripts = cs_scripts[:5]  # Limit to the first 5 scripts

            # Step 2: Search for the files on GitHub
            search_github_file(cs_scripts, progress_bar)
        else:
            print("No C# scripts found during scraping.")
