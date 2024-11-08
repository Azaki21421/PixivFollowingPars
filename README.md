# Pixiv Following Parser

This project includes two Python scripts utilizing Selenium and BeautifulSoup to automate data collection and following on [Pixiv](https://www.pixiv.net).

## Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Following Data Collection Script](#following-data-collection-script)
  - [Auto-Follow Script](#auto-follow-script)
- [Requirements](#requirements)
- [License](#license)

## Description

1. **Following Data Collection Script**:
   This script collects data on users you follow on Pixiv, including names and profile links. It saves the data in JSON format with the last processed page number, allowing it to resume from the last page if interrupted.

2. **Auto-Follow Script**:
   This script loads a JSON file with user links and automatically navigates to each profile, clicking the "Follow" button if available. It allows batch following of users from your collected following data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Azaki21421/PixivFollowingPars.git
    cd PixivFollowingPars
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have Google Chrome and [ChromeDriver](https://chromedriver.chromium.org/downloads) installed, matching your Chrome version.

## Usage

### Following Data Collection Script

1. Run `pixiv_following_scraper.py`:
    ```bash
    python pixiv_following_scraper.py
    ```
2. Enter your Pixiv user ID when prompted.
3. Log in to your Pixiv account in the opened browser window and click "Continue" once logged in.
4. The script will browse your following pages, collecting user info on each. If interrupted, it saves progress and resumes from the last processed page.
5. Data is saved to `pixiv_data.json` in the following format:
    ```json
    {
        "users": [
            {"name": "User1", "link": "https://www.pixiv.net/en/users/User_id"},
            {"name": "User2", "link": "https://www.pixiv.net/en/users/*some number*"}
        ],
        "last_page": 5
    }
    ```

### Auto-Follow Script

1. Run `pixiv_auto_follow.py`:
    ```bash
    python pixiv_auto_follow.py
    ```
2. Ensure `pixiv_data.json` with user links exists.
3. Log in to your Pixiv account in the opened browser window and click "Continue" once logged in.
4. The script navigates through each profile link and clicks the "Follow" button on each profile, if the button is available.

## Requirements

- **Python 3.8+**
- **Selenium**
- **BeautifulSoup4**
- **requests**
- **Google Chrome** and matching **ChromeDriver**

Install dependencies using `pip install -r requirements.txt`.


## License

This project is licensed under the GNU General Public License (GPL). See [LICENSE](LICENSE) for more details.
