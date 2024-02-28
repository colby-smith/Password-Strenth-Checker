# Password-Strenth-Checker
## About
A simple program that takes the input of a users password and outputs improvements, if any, it can make. Utilising constant variables, basic python arithmatic and functions, as well as error logic.

## Prerequisites
To use this program effectivly make sure you have installed:
* Python 3.12.2
* bash or zsh

## Installing python 3.12.2
If you're on Linux, there are some dependencies you'll need before installing pyenv. Run these commands to install them:

1. Only run these if you're using a linux sytem.
```
sudo apt update
sudo apt install -y build-essential zlib1g-dev libssl-dev
sudo apt install -y libreadline-dev libbz2-dev libsqlite3-dev libffi-dev

```
2. Run this to instal pyenv with webi.
```
curl -sS https://webi.sh/pyenv | sh
```
3. Open your ~/.bashrc file in VS Code. You can do so by typing:
```
code ~/.bashrc
```
If you're using Mac.
```
code ~/.zshrc
```
4. Add these lines to the bottom of the file in this order:
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

5. Finally close and reopen your terminal.

## Usage
To use this simple tool simply follow the instructions below:

1. Change into the repository directory in your shell.

2. Create a folder called **passwords**.

3. Create a .txt file called **password**.

4. Save the changes using *ctrl+S* for windows and *command+S* on mac.

5. Finally run the program by typing **python main.py** and hitting enter, if an error occurs run **python3 main.py** instead.
