# Item Catalog Project - Udacity FSND Nanodegree

## Description 

This is the third project for the **Udacity Full Stack Nanodegree**. The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provides a user registration and authentication system. This project uses persistent data storage to create a *RESTful* web application that allows users to perform *Create*, *Read*, *Update*, and *Delete* operations.

A user does not need to be logged in in order to read the categories or items uploaded. However, users who created an item are the only users allowed to update or delete the item that they created.

This program uses third-party auth with **Google** or **Facebook**. Some of the technologies used to build this application include **Flask** and **SQLalchemy**.

## Getting Started


### Prerequisites

The project code requires the following software:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/)
* [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
* Python version 2



### Installing

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/)
2. Clone the [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
3. Clone this repo into the catlog/ directory found in the vagrant directory
4. Launch the Vagrant VM with `vagrant up`
5. Log into Vagrant VM with `vagrant ssh`
6. From the main directory run `sudo pip install -r requirements.txt`

## Running the program

Follow the steps below to run the program :

* If first time running, you must create the database with `python database_setup.py` and populate it with `python model.py`
* Run application with `python application.py` from within its directory
* Go to http://localhost:8000 to access the application

## Authors

* **Mohamed BOUSETTA MAHJOUB** - *Initial work* - [MedMahj](https://github.com/MedMahj/)





