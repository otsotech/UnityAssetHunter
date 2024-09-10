<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/logo_white.png">
  <source media="(prefers-color-scheme: light)" srcset=".github/logo.png">
  <img src=".github/logo_white.png" height="150"/>
</picture>
</p>

<h3 align="center">Protect Your Unity Assets with Unity Asset Hunter!</h3>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo stars](https://img.shields.io/github/stars/otsotech/UnityAssetHunter?style=flat&logo=github&color=f5f5f5)](https://github.com/otsotech/UnityAssetHunter)

Unity Asset Hunter is a Python tool designed for Unity asset developers to identify if their assets are being publicly shared on various platforms, such as GitHub. This tool helps prevent piracy and unauthorized distribution of assets, ensuring that developers' hard work is protected.

## At a Glance
- 🚀 **Automated Asset Search**: Quickly scans Unity asset URLs and retrieves all script files included in the package.
- 🌐 **GitHub Integration**: Utilizes the GitHub API to search repositories for potential matches of the assets.
- 📊 **Results Sorting**: Lists search results by the date of the last update, highlighting the most recent and potentially unauthorized uses.
- 🔐 **Secure and Ethical**: Intended for ethical use only to protect intellectual property.

## How to Help
- [⭐ Star](https://github.com/otsotech/UnityAssetHunter) the repo, leave a [review](#), and spread the word about the project!
- [Contribute](CONTRIBUTING.md) by submitting feature requests, bugs, or even your own PR.
- [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/otsotech) this project to support further development.

## Why Use Unity Asset Hunter?

For asset developers, it's crucial to protect their intellectual property from unauthorized distribution. Sometimes, developers who purchase assets may inadvertently include them in public repositories, not fully realizing this constitutes a breach of license terms. This often happens without malicious intent — a simple oversight by developers who do not fully consider the implications.

**Unity Asset Hunter** is designed to help asset creators monitor and detect where their assets are being publicly shared, even when done unintentionally. By providing a way to identify these instances quickly, the tool enables asset developers to take appropriate action, ensuring that their hard work remains protected and used according to its intended license.

## Setup
To get started with **Unity Asset Hunter**:

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
Run the tool with Python:
```bash
python main.py
```
Follow the on-screen prompts to enter the Unity asset URL.

## Requirements
- Python 3.7 or higher
- GitHub API token (for searching public repositories)

## Contributing
Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
**Unity Asset Hunter** is designed for ethical use only. The tool should only be used to prevent piracy and unauthorized distribution of assets. The developers are not responsible for any