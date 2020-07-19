#**DevOps Core Fundamental Project**

The brief for this project was "To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training."

This means that I was to create a web app that was capable of taking input from a user and using it to create,
read, update and delete data stored in a database. Relevant data was then to be returned to and visible on the app.


**Minimum Requirements were as follows:**

1. A Trello board (or equivalent Kanban board tech) 
 
2. A relational database with at least two tables and one relationship
 
3. Clear Documentation from a design phase
 
4. A functional CRUD application created in Python
 
5. A functioning front-end website and integrated API's, using Flask
 
6. Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine


###**Functionality**

To address this brief and these requirements, I designed a web app which allows users to register and log in whereby
they would be asked to answer 5 riddles. The login details and answers given to the riddles would then be stored in a
database, across two tables, and used to inform the user of their results.

The User Stories for this project were as follows:

1. As a user, I want to be able to register my details so that answers I give are logged against my profile

2. As a user, I want to be able to update my user details so that if my email address changes, I can use my new one to 
   access my account
   
3. As a user, I want to have the ability to delete my account so know that my details aren't being held longer than I
   want them to be
   
4. As a user, I want to see points accrued for correct answers so I can see my total so far

5. As a user, I want to see links to each available page so I can easily navigate the site

6. As a user, I want the riddles I answer to be updated on a regular basis so I am kept interested on an ongoing basis

7. As a user, I want to be able to see a league table so I can compare my score against other users

The images below show how these user stories had the MoSCoW Method applied, the tasks created to answer these user
stories and how Agile sprints were used to set timescales for completion against groups of tasks.

![Imgur](https://i.imgur.com/HWD9pad.png)

![Imgur](https://i.imgur.com/SSWIfME.png)


###**Database**

To cover the requirement on using a relational database, I designed the following tables:

![Imgur](https://i.imgur.com/G8oY5x0.png)

As you can see from the diagram above, the relationship between these tables comes from the UserID in the 'posts' table
and the ID in the 'users' table.


###**Technology**

As per the project brief, I have implemented the following technologies based on the training recieved over the last 5
weeks:

* Kanban Board on Trello
* Python as the chosen programming language
* Flask as a framework with HTML for web pages
* Git provides version control
* GCP SQL Server using mySQL to hold and run databases
* GCP Compute Engine cloud server for Linux VM
* Jenkins provides CI functionality


###**CI Pipeline**

Below is my CI Pipeline for this project detailing process flow and all relevant technology involved
 
![Imgur](https://i.imgur.com/mhPU0Xs.jpg)
 
As you can see from the diagram, the process is as follows:

* Source code written and held on Linux Ubuntu VM
* Code is pushed to GitHub repository on a regular basis or once any significant change is completed
* Task completion noted on Trello and next task ascertained
* This cycle continues until web app is ready to be run
* Jenkins runs build and reports back any build errors
* Jenkins will check every minute for any changes in GitHub repository
* Any changes will be implemented by Jenkins in next build


###**Front-End Design**

The first page a user will see upon reaching the site is the homepage:

![Imgur](https://i.imgur.com/Cq1RFgw.jpg)

On a first visit, the customer would click the 'Register' link which would take them to the registration page:

![Imgur](https://i.imgur.com/ezP184u.jpg)

Upon completion of the registration form, which will push relevant data to the 'users' table in the DB, they will be
asked to log in:

![Imgur](https://i.imgur.com/EoWo3Kn.jpg)

Once logged in, the user will automatically be directed to the 'riddles' page where they will answer the questions set:

![Imgur](https://i.imgur.com/QlCAR27.jpg)

Clicking the 'Submit' button pushes the answers given into the 'posts' table in the DB and directs the user to the
'results' page:

![Imgur](https://i.imgur.com/kLGdo74.jpg)

At any point after login, a user can view their previous answers by going to the 'results' page or give new ones on the
'riddles' page. They can also go to the 'account' page to update or delete their account:

![Imgur](https://i.imgur.com/rvFSYvk.jpg)

Updating user details will return the user to the 'home' page and deleting takes us back to the registration page.

Logging out will return the user to the 'login' page.


