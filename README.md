# Log-Analysis-2

## Project Description

Log-Analysis project is about connecting to a database and inserting the data into the database from the .sql file using python-psycopg2 and database postgresql and python.
Then retrieving the data from the databse for the questiones listed below.

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

## Requirements

1. Virtual Box.

2. Vagrant.

3. Python 2.7 or above.

## Local Development:

### Terminal commands for installation.

* First install vagrant by using command "sudo apt-get install vagrant".

* Install virtualbox by using command "sudo apt-get install virtualbox".

* Clone this repository.

* vagrant init hashicrop/precise64(varies with system).

* vagrant up.

* vagrant ssh.

* sudo apt-get install postgresql.

* sudo apt-get install python-psycopg2.

* Create a role(vagrant).

* create a database(news).

* Download the data from the link given below. https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

* Unzip the data to folder location.

* From terminal go to location cd /vagrant.

* Add the data into the database(news) by command 
"psql -d news -f newsdata.sql"

* Run your python file by python filename.py .

## output
![surya2.png](https://github.com/dasarisurya/Log-Analysis-2/blob/master/output.png)
