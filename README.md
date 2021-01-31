# Wolt Backend assignment

A flask-driven restful API for the **[Wolt Backend assignment] (https://github.com/woltapp/summer2021-internship)**

## Technologies used

- **[Python3](https://www.python.org/downloads/)**
- **[Flask](flask.pocoo.org/)**
- **[Virtualenv](https://virtualenv.pypa.io/en/stable/)**

## Installation / Usage

- If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
- After this, ensure you have installed virtualenv globally as well. If not, run this:
  ```
      $ pip install virtualenv
  ```
- Git clone this repo to your PC

  ```
      $ git clone https://github.com/LinuzJ/wolt_backend_assignment-2021.git
  ```

- #### Dependencies

  1. Cd into your the cloned repo as such:

     ```
     $ cd wolt_backend_assignment-2021
     ```

  2. Create and fire up your virtual environment in python3:

     ```
     $ virtualenv -p python3 venv
     $ source venv/bin/activate
     ```

     You should now have the virtual envoirement set up and be ready for use!

- #### Install your requirements

  ```
  (venv)$ pip install flask
  ```

- #### Running It
  On your terminal, run the server using this one simple command:
  ```
  (venv)$ python app.py
  ```
  You can now access the app on your local browser by using
  ```
  http://localhost:5000//discovery?lat=60.1709&lon=24.941
  ```
