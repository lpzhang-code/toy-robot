# Toy Robot

- This project simulates a toy robot moving on a square table top that is 5 units by 5 units; we have used the OOP principle of encapsulation to organise the required attributes and functionality with a robot class.
- TDD was essential because it allowed us to be very clear about the behaviour of the robot, it sped up the development process, and allowed us to finish with an extensive test suite.
- The Single Responsibility Principle states that a class should have just one high level job and so there is only one reason to change that class, our code is consistent with this principle because the robot class simulates a robot moving on a square table top and no more.
- The Open/Closed Principle states that a class can only be changed in a way that doesn't break its dependents, this requires a degree of foresight in terms of strategically enabling extension points, we have split the behaviour of the robot into separate functions allowing for reuse in different combinations.

## How to Set Up

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
