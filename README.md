# atm system 
- A simple ATM system with a Flask-based web interface, allowing:
- Select an existing account
- View balance (GET)
- Withdraw (POST)
- Deposit (POST)

# challenges
- After the initial deployment of the code, the HTM page was not found after all the required links. Understanding why this happened and changing the BP 
- Which cloud to use, and upload the project to the cloud
- Initially the project was saved in a subfolder so the cloud was unable to upload it properly in sync with the git. I was able to figure it out after using the internet.

# design descisions
- first I'm thinking about mvc, But in this project it is not necessary and complicates it
- After trying, I chose to simply write a project that has a separation between HTML and FLASK. In addition, I chose to use JS in the HTML pages to perform the actions after each user selection 
- use Render cloud 