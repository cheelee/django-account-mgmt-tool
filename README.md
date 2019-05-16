#Online Accounts Management Tool

A Django-Bootstrap 4 web application prototype for personal management of online accounts and login information.

## Overview

This is a personal project to help me locally manage the many online accounts that I have. The idea is to allow me to be better able to track account passwords, payment schedules, password change schedules. My goals are to:

*  make something useful for myself, and maybe others;
*  experience the process of building a web-based tool, and along with it build for myself an understanding of best practices for full-stack web development.

I plan for this project to also serve as a personal case-study and workflow documentation for bringing a Django web project to life. Please see [this repository](https://github.com/cheelee/django-setup-support) for scripts that help me bring up an empty Django project template with my frequently-desired features for me to build on.

## License

Please refer to the [license document](LICENSE).

The specific configuration of [DataTables](https://datatables.net/) used and included in this repository was released under the [MIT License](https://datatables.net/license/mit) (local repo [link](account_tool/static/DataTables/DataTables_License.txt)).

## The Tool

Note that this prototype is a work-in-progress, and while it is functional there are many desired feature sets I would like to see developed for it.

### Quick Start

#### Requirements

* Mac OS X or Linux system.
* Python 3 installed with associated virtualenv support.

#### Setup

1. Clone or fork your own copy of the Github repo.
2. Run the <em>setup.sh</em> script. Requires an internet connection. This script:
    * creates the python virtual environment;
    * sets up the necessary python environment using the <em>requirements.txt</em> file;
    * downloads the necessary external packages;
    * creates the required Django app static environment. 
3. <em>source env/bin/activate</em>
4. <em>python manage.py migrate</em>
4. <em>python manage.py runserver</em>
5. Visit <em>127.0.0.1:8000</em> on any browser. The following welcome screen should show up with some test content available for use.
![Welcome Screen](docs/images/WelcomeScreen.png)
6. Please refer to the documentation for [further information on what the tool does](docs/Usage.md).

### Current Prototype Features

* User Authentication
* Lists Online Accounts (see Model for details) in paginated, re-orderable table.
* Visit accounts via URL link.
* Click on entries to enable full detailed view of records, and edit them.
* Specify another record in database as authentication-linked (e.g. if an online account X allows for Google authentication, you can associate the record for X with the record for Google.)
* Create new records.

### Desired Tool Features

* Secure deployment to a local resource (e.g. USB stick.) I personally wouldn't attempt to deploy this on an online service like AWS even if I could somehow make it secure.
* Analysis Tool to chart payment history, and display a timeline for upcoming expected payments.
* Printing of records to a PDF file. Sometimes having a paper copy is just more helpful.
* Marking records as defunct.
* Ability to delete records from the database.
* Ability to set up a user account. As opposed to running as an administrator account. There are no plans to make this a multi-user tool.
* A more systematic continuous testing regime for the tool based on best practices.

### Further Documentation

* Tool usage documentation ([Usage.md](docs/Usage.md))
* DataTables package configuration ([DataTablesConfiguration.md](docs/DataTablesConfiguration.md))
* Meta Documentation - Transition from an empty Django Template to this Tool Implementation. ([Transition.md](docs/Transition.md))

