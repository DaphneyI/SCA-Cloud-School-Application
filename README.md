# A docker image that displays a flask based webapp

### Application tree
- Created the flask app, docker file and requirements.txt in the same directory
- The requirements.txt file contains all the dependencies for the web application
- Since this is a simple web application, i decided against making sub directories for the templates and static file and just applied those directly in the app.py file.


### The Dockerfile
- Used a lightweight base image (python:3.9.6-alpine) to keep the image lightweight as well,
- Set a working directory,
- Included run commands for installing the dependencies,
- Copied relevant files into the working directory,
- Specified commands to be executed whenever an instance of th image is run.


### Building the image and container
In the directory with the dockerfile in the CLI, i ran the following commands:
``` 
  docker build -t sca .        *builds the image*
```
```
  docker images               *checks that the image is in directory of local images*
```
```
  docker run -p 5000:5000 sca    *creates an instance of the image, exposing port 5000 of the local host to port 5000 of the container(flask default)*
```


### Testing the application
In another terminal, i sent an http get request to the server by running the curl command
```
curl localhost:5000
```
This displayed the return value of function binded to the home route.\
I also navigated to the address below to view my application in a web browser
```
localhost:5000
```
In the terminal where my docker container was running, i got an http response with status code 200 ok, indicating the success of the request.


### Pushing to dockerhub
ran  the commands
```
  docker login -u <username>     *logs in to dockerhub*
```
```
  docker tag sca <username>/sca-cloud-school-application     *tags the image*
```
```
  docker push <username>/sca-cloud-school-application     *creates a repo in dockerhub with the same name*
````

You can access the image on [dockerhub](https://https://hub.docker.com/repository/docker/daphdocker/sca-cloud-school-application)







