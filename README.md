# Unity Asset Hunter

Unity Asset Hunter is a Python tool designed for Unity asset developers to identify if their assets are being publicly shared on various platforms, such as GitHub. This can happen inadvertently when a game developer purchases an asset and uses it in a game that is later uploaded to a public repository. The tool aims to prevent piracy and unauthorized distribution of assets, ensuring that developers' hard work is protected. **Unity Asset Hunter** is intended for ethical use only and is not to be used for any malicious purposes.

## Features

- **Automated Asset Search**: Enter the URL of a Unity asset, and the tool will scrape the content page for every script file included in the package.
- **GitHub Integration**: Uses the GitHub API to search repositories for potential matches of the assets.
- **Results Sorting**: Reorders search results by the date of the last update, helping developers identify the most recent and potentially unauthorized uses.

## How It Works

1. **Enter the Unity Asset URL**: Provide the URL of the Unity asset you wish to check.
2. **Web Scraping**: The tool will web scrape the Unity package content page to gather a list of script files included in the asset.
3. **GitHub Search**: Utilizes the GitHub API to search for repositories containing files that match the scraped script files.
4. **Results Analysis**: Matches are listed and sorted by their last update date, allowing for a quick review of potentially unauthorized distributions.

## Installation

To use **Unity Asset Hunter**, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/otsotech/UnityAssetHunter.git
    cd UnityAssetHunter
    ```

2. **Install the Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool with Python:
    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to enter the Unity asset URL.

## Requirements

- Python 3.7 or higher
- GitHub API token (for searching public repositories)

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**Unity Asset Hunter** is designed for ethical use only. The tool should only be used to prevent piracy and unauthorized distribution of assets. The developers are not responsible for any misuse of this tool.

## Contact

For any inquiries or issues, please open an [issue](https://github.com/otsotech/UnityAssetHunter/issues) or contact the repository owner.

---

*Unity Asset Hunter* - Protecting Your Creative Work.
