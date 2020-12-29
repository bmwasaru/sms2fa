# Pewa

Finance your passions.

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/sms2fa-flask.git
   $ cd sms2fa-flask
   ```

1. Create a new virtual environment.

    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```bash
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```bash
        mkvirtualenv automated-survey
        ```

1. Install the dependencies.

    ```bash
    pip install -r requirements.txt
    ```


1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   Run `source .env` to export the environment variables.

1. Run the migrations.

    Our app uses SQLite, so you probably will not need to install additional software.

    ```bash
    python manage.py db upgrade
    ```

1. Make sure the tests succeed.

    ```bash
    $ coverage run manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```

1. Check it out at: [http://localhost:5000/](http://localhost:5000/).
