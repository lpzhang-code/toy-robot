# Toy Robot

## Set Up

Create a special environment for this project so that it works the same regardless of the machine on which it is run

`cd` into the project folder and begin by installing `virtualenv`

```
pip install virtualenv
```

Create and activate the virtual environment (env)

```
virtualenv -p python3 env

. env/bin/activate
```

Install packages into the virtual environment

```
pip install -r requirements.txt
```

Turn off the virtual environment when you are done

```
deactivate
```

## How to Run

## Reasoning

- single responsibility principle
- open/closed principle, broken logic into different functions allowing for extension
- using dictionary to store X,Y,F for code readability, furthermore lookups are in constant time
