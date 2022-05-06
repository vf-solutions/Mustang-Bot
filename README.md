[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# Mustang-Bot

<!-- PROJECT LOGO -->
[<img src="assets/img/Cal-Poly-University-Seal.png" align="right" width="150">](https://github.com/Kaweees/Mustang-Bot)

Source code of Mustang Bot in the Cal Poly Class of 2026 Discord Server

<!-- BUILT WITH -->
### Built With

- Python 3:
  - Discord.py
  - async
  - os
  - psutil
  - virtualenv
- Visual Studio Code

# How to Use Mustang-Bot

## Method 1: Invite Link
In the case you are interested in just using the bot, you can invite the bot to your server by following [this link](https://discord.com/oauth2/authorize?client_id=957743101995274280&permissions=8&scope=bot).

## Method 2: Running it Locally

To get a local copy up and running follow these instructions.

### Prerequisites

- Working Python 3 >= 3.10.0 installation
  - [pip](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/) is working

- Visual Studio Code
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) Extension


### Installation

1. Create a Virtual Python Environment
    - Creating a Virtual Enviorment (Linux):
      ```sh
      virtualenv .venv
      source .venv/bin/activate
      ```
    - Creating a Virtual Enviorment (Windows):
      ```sh
      pip install virtualenv
      virtualenv .venv
      .venv/Scripts/activate
      ```
2. Clone the repo
    ```sh
    git clone https://github.com/Kaweees/Mustang-Bot.git
    ```
3. Install/update project requirments (administrator permissions may be required)
    ```sh
    pip install upgrade
    pip install -r requirements.txt
    ```

### Before Running
1. Configure the following environment variables in a `.env` file for the bot
  - `TOKEN`: (bot token)[https://discordpy.readthedocs.io/en/stable/discord.html]

### Running locally
1. Move to the root directory
    ```sh
    cd Mustang-Bot
    ```

2. Run the bot
    ```sh
    python boy.py
    ````

## Method 2: Hosting via Heroku

In the case you are interested in running the bot via Heroku, you can follow these instructions.

### Via Heroku CLI
1. Log onto Heroku.
    ```sh
    heroku login
    ```
2. Create a new application or open an existing application. Note the name of the application.
3. Go to `Settings > Add Build path > Python`
4. Install the Heroku CLI by following [this link](https://devcenter.heroku.com/articles/heroku-cli).
5. Move to the root directory
    ```sh
    cd Mustang-Bot
    ```
6. Create a `.env` file locally and configure it as in [Before Running](###Before-Running)
7. Push the files to a New or Exsisting Heroku App.
  - For a New App
    ```sh
    heroku create -a example-app
    ```
  - For an Existing App
    ```sh
    heroku git:remote -a "NAME_OF_HEROKU_APPLICATION_GOES_HERE"
    ```
8. Deploy the local `main` branch to Heroku remotely
  - For the local `main` branch
    ```sh
    git push heroku main
    ```
  - From a branch besides `main`
    ```sh
    git push heroku branch-name:main
    ```
11. The bot should be active after a few minutes. Enjoy!

### Via Heroku Website
1. Log onto Heroku.
2. Create a new application or open an existing application.
3. Go to `Deploy > Deployment method > Connect with GitHub` and add this repository. You must have access to this repository on a Github account for this to work, or access to a fork of this repository.
4. Go to `Deploy > Deploy Branch > Main Branch` to depoly the recent version of the Main branch.
5. Repeat steps 2-4 whenever the Main Branch is updated to have access the latest features of the bot.
6. Go to `Resources`. Press `Edit`, and hit the sliding button so that it is on and hit `Confirm`.
7. The bot should be active after a few minutes. Enjoy!

<!-- CONTRIBUTING -->
## Contributing

Contributions are always welcome! Please create a Pull Request and include a description of how your Pull Request will improve the overall robot code and what it does.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License. See `LICENSE.txt` for more information.

<!-- SUPPORT US -->
## Support Us!

Give this repo a ⭐️ if you found this project helpful!

## Acknowledgments

- [othneildrew's Best README Template](https://github.com/othneildrew/Best-README-Template)
- [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Kaweees/Mustang-Bot.svg?style=for-the-badge
[contributors-url]: https://github.com/Kaweees/Mustang-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kaweees/Mustang-Bot.svg?style=for-the-badge
[forks-url]: https://github.com/Kaweees/Mustang-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/Kaweees/Mustang-Bot.svg?style=for-the-badge
[stars-url]: https://github.com/Kaweees/Mustang-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kaweees/Mustang-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/Kaweees/Mustang-Bot/issues
[license-shield]: https://img.shields.io/github/license/Kaweees/Mustang-Bot.svg?style=for-the-badge
[license-url]: https://github.com/Kaweees/Mustang-Bot/blob/master/LICENSE.txt
