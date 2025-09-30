# WinSupport
## Customer Support AI Agent, Tekedia

WinSupport is a powerful AI agent that takes your business information in a form of PDF and based on content answer your customers. No need for manual customer support when Winsupport can handle customer fast and 24/7

## Features
- Upload your custom knowledge, No size limit
- Chat Screen to query from provided PDF
- Multiple PDF supported



> Before cloning the project, Make sure that you are a part of Tekedia Institute
> As this code only works on the servers allowed by Tekedia
> Also make sure you have followed the pre-steps provided by Tekedia 
> so that you can run this code on Tekedia Pre-Configured Servers
> Thanks

## Setup the project on Tekedia Server
Login to your ssh provided by Tekedia, You can use Putty or Windows Terminal, 

#### Connect to Tekedia Server
Type the following command with your username
`ssh <username>@<tekedia_server_ip_address>`
For Example
`ssh student1@123.456.789.0`

Welcome to your personal space in Tekedia Server

#### Clone Project Repo
Head to your project folder, Command
`cd htdocs/<domainname>`
Here `domain name` is either your custom domain or Tekedia provided domain
For Example
`cd htdocs/student.zenvus.com`

Clone the Github Repo by the command
`git clone https://github.com/Blucera/demo-winsupport.git .`

#### Making the build and Running the Container
Run the command
`podman-compose build --no-cache`
This will build your code, Installing all the dependencies required for the AI Agent to run in your personal envoirenment.

After the build is complete, We have to start the container, Before that Tekedia Institute have provided you a `port number` on which you have to run your container. We have to add the `port number` assigned by Tekedia to your `docker-compose.yml` file.

For that run
`nano docker-compose.yml`

And you will see this
```
version: "3.9"

services:
  winsupport:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "<your_port>:8501"
    environment:
      # Tell your app where to reach Ollama
      OLLAMA_HOST: http://172.17.0.1:11434
    extra_hosts:
      - "host.docker.internal:172.17.0.1"
    restart: unless-stopped
```

Here replace `<your_port>` with the port number assigned by Tekedia. Hit `Ctrl + X`, Then `Y` then `Enter` and your file is saved.

Now you can run the command
`podman-compose up -d`

And your code is running on your domain. You can also check if the container is successfully running by typing
`podman ps` 
It will show your container.