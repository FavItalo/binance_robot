# binance_robot
My attempt to create a robot for cryptocurrency trading. The idea is to use several indicators for the machine decision on buying and selling. On short term, the goal is to set a few indicators and simulate trading without money. On medium term, develop strategies and trade with money on computer based platform. On a far future, develop a bunch of indicators that interact with each other and dock the bot in a cloud service to run 24/7.

## Pre-steps:

- Set PYTHONPATH to the current repository directory
- Use `setup/environment_setup.yml` to create conda environment with respective dependecies

## Repository structure

- `bin/` folder to store binaries used by some applications like x13-arima-seats models or any webdriver, if needed. (does not upload to git)
- `setup/` folder to store files used to prepare the directory for any needing. Files for binaries installation or folder creation.
- `src/` folder where the magic happens. Here are the codes with processes and functions used by the bot.
- `src/examples` folder with any example created to test any future implamentation to the bot. These examples files should be stored for future research and report learning steps.
- `src/functions` folder with codes used as auxiliary processes to the main function, other auxiliary functions or models. These go from the basic to the more advanced auxiliary codes
- `src/processing` folder with processes like the main code or other models concurrent to the main application. 