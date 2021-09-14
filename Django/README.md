PROJECT - GROUP DATA & ANALYTICS:
    In-memory analytics is an approach to querying data when it resides in a computer’s random access memory (RAM), as opposed to querying data that is stored on physical disks.  This results in vastly shortened query response times, allowing analytic applications to support faster business decisions.

REQUIREMENTS (Prerequisites):
    Python 3.6 and up.

INSTALLATION:
    * for ubuntu:
        1. Installing venv:
            sudo apt install python3-venv
        2. Creating an environment (venv):
            python3 -m venv venv
        3. Activating the venv:
            source venv/bin/activate

    * for windows:
        1. Installing virtualenv:
            pip install virtualenv
        2. Creating an environment (venv):
            virtualenv venv
        3. Activating the venv:
            venv\Scripts\activate

    * Installing requirements in venv:
        for ubuntu:
            pip3 install -r requirements.txt
        for windows:
            pip install -r requirements.txt

RUNNING THE TESTS:
    * for ubuntu:
        python3 manage.py test
    * for windows:
        python manage.py test

RUNNING THE SERVER:
    * for ubuntu:
        1. python3 manage.py migrate
        2. python3 manage.py runserver
    * for windows:
        1. python manage.py migrate
        2. python manage.py runserver

HOW TO CONTRIBUTE:
    Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate. If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

    Steps to contribute:
    1. Fork this repository (link to repository)
    2. Create your feature branch (git checkout -b feature/fooBar)
    3. Commit your changes (git commit -am 'Add some fooBar')
    4. Push to the branch (git push origin feature/fooBar)
    5. Create a new Pull Request
    
    Additionally you can create another document called CONTRIBUTING.md which gives instructions about how to contribute.

    Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

AUTHORS:
    Yugdeep Riar - yugdeepriar@gmail.com

CREDITS:
    A heartfelt thank you to @Pranav_sir and @Trishant_sir for the encouragement I needed to get this idea off the ground and start writing!
