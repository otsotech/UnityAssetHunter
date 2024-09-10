import os
import requests
import time
from dotenv import load_dotenv
from collections import defaultdict
from datetime import datetime

def search_github_file(file_names, progress_bar):
    # Load environment variables from .env file
    load_dotenv()
    
    # Retrieve GitHub token from environment variable
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        return {}

    # Initialize a dictionary to store repository matches
    repo_matches = defaultdict(lambda: {'count': 0, 'last_updated': None})

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
                repo_api_url = repo.get('url')  # This is the API URL for the repository

                # Update the count of matches
                repo_matches[repo_url]['count'] += 1

                # Get the latest update date for the repository
                if repo_api_url:
                    repo_response = requests.get(repo_api_url, headers=headers)
                    if repo_response.status_code == 200:
                        repo_data = repo_response.json()
                        updated_at = repo_data.get('updated_at')
                        if updated_at:
                            # Parse the datetime string and extract only the date
                            updated_date = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ").date()
                            if not repo_matches[repo_url]['last_updated'] or updated_date > repo_matches[repo_url]['last_updated']:
                                repo_matches[repo_url]['last_updated'] = updated_date
                
                # Add a delay to avoid hitting the rate limit
                time.sleep(2)  # Sleep for 2 seconds
        else:
            print(f"Error searching for {file_name}: {response.status_code}")
            continue

        # Update the progress bar
        progress_bar.update(10)

    # Convert to a sorted dictionary based on the number of matches and the latest update date
    sorted_repo_matches = dict(sorted(repo_matches.items(), key=lambda x: (-x[1]['count'], x[1]['last_updated'] or '')))
    return sorted_repo_matches