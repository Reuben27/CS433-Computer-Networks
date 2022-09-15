# CS433 Computer Networks

## Assignment 1

### Network Application using Socket Programming

The goal was to develop a simple remote file system service (RFS) and understand the principles of layered network architecture. Following are the steps to compile and execute the code:

- You must have [Python](https://www.python.org/) and pip installed on your laptop/desktop. Run the following commands to check the whether you have them installed or not.
```
python --version
pip --version
```

- You must also have [git](https://git-scm.com/) installed on your laptop/desktop. Run the following command to check the same.
```
git --version
``` 

- Clone this git repository. Run git branch to ensure you are on the main branch. Enter Assignment 1 folder.
```
git clone https://github.com/Reuben27/CS433-Computer-Networks.git
git branch
cd "Assignment 1"
```

- Enter the server folder and the run the server file.
```
cd server
python server.py
```

- Open a separate terminal window and go to Assignment 1 folder. Enter the client folder.
```
cd client
python client.py
```
