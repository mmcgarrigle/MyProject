**DevOps Core Fundamental Project**

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


**Functionality**

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

![Trello1](https://onedrive.live.com/?cid=10082C236ED5B987&id=10082C236ED5B987%215171&parId=10082C236ED5B987%21434&o=OneUp)

![Trello2](https://onedrive.live.com/?cid=10082C236ED5B987&id=10082C236ED5B987%215172&parId=10082C236ED5B987%21434&o=OneUp)


**Database**

To cover the requirement on using a relational database, I designed the following tables:

![Tables](https://onedrive.live.com/?cid=10082C236ED5B987&id=10082C236ED5B987%215179&parId=10082C236ED5B987%21105&o=OneUp)

As you can see from the diagram above, the relationship between these tables comes from the UserID in the 'posts' table
and the ID in the 'users' table.