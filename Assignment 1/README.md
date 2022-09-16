# CS433 Computer Networks Assignment 1

## Network Application using Socket Programming
The goal was to develop a simple remote file system service (RFS) and understand the principles of layered network architecture. 

### Quickstart
Following are the steps to compile and execute the code:

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

- You should see the following output in your terminal (server).
```console
Server listening on port 6900
```

- Open a separate terminal window and go to Assignment 1 folder. Enter the client folder.
```
cd client
python client.py
```

- The connection between the client and server would have been established by now. You should see the following output in your terminal (client).
```console
Received the following from server:
  The following commands are supported:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD

The following encryption modes are available:
  1 - Plain Text
  2 - Substitute
  3 - Transpose
```

- The client will then ask for the command and the mode of encryption. 
```console
Enter command: CWD
Enter mode of encryption: 3
```

- The client will send the request to the server and the response from the server will be displayed on the terminal. The response will be the current working directory of the server.
```console
Status from the server:
 OK
Response from the server:
 E:\IITGn Academics\Semester VII\CS 433 - Computer Networks\CS433-Computer-Networks\Assignment 1\server
Connection Closed
```
