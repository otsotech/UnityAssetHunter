import os
import requests
import time
from dotenv import load_dotenv
from collections import defaultdict

def search_github_file(file_names, progress_bar):
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve GitHub token from environment variable
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("Error: GitHub token not found. Make sure it's defined in the .env file.")
        return

    # Initialize a dictionary to store repository matches
    repo_matches = defaultdict(lambda: {'count': 0, 'last_updated': ''})

    # Loop through each file name to search on GitHub
    for file_name in file_names:
        url = f"https://api.github.com/search/code?q=filename:{file_name}"
        headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        # Send a GET request to the GitHub API
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            search_results = response.json()
            items = search_results.get('items', [])

            for item in items:
                repo = item.get('repository', {})
                repo_url = repo.get('html_url', 'Unknown URL')
                updated_at = repo.get('updated_at', '')

                # Update the count of matches and the latest update date
                repo_matches[repo_url]['count'] += 1
                if updated_at and (updated_at > repo_matches[repo_url]['last_updated']):
                    repo_matches[repo_url]['last_updated'] = updated_at
        else:
            print(f"Error: Unable to search GitHub for {file_name}. Status code {response.status_code}")
            print(response.json().get('message', ''))

        # Add a delay to avoid hitting the rate limit
        time.sleep(2)  # Sleep for 2 seconds

        # Update the progress bar
        progress_bar.update(10)

    # Convert to a sorted list based on the number of matches and the latest update date
    sorted_repos = sorted(repo_matches.items(), key=lambda x: (-x[1]['count'], x[1]['last_updated']))

    print("\nRepositories with matches:\n")
    for repo, details in sorted_repos:
        print(f"Repository: {repo} - Matches: {details['count']} - Last Updated: {details['last_updated']}")
