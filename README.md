# jwt-flask-proxy

This project enables a JWT access key generator in an HTTP proxy writen in Python 3.6 with Flask framework.

&nbsp;  
&nbsp;  
## README Map

- If you prefer to run the proxy manually, [install the requirements](README.md#set-up-and-install) and [run the proxy server](README.md#running-the-proxy-server).
- To play with the JWT Generator class, [install](README.md#set-up-and-install) and see the [class that generates Tokens](README.md#the-class-to-generate-jwt).
- If you prefer Docker, go to [Containerise with Dockerfile](README.md#containerise-with-the-dockerfile).
- To run Docker compose, jump to [Docker compose](README.md#run-the-docker-compose) instructions.
- About logs, please move to the corresponding topic, [Logs](README.md#logs).
- Instructions on advanced/technical documentation, go to [Documentation](README.md#documentation).
- For running tests, please see the corresponding chapter, [Automatic tests](README.md#automatic-tests).
- Or click to jump to the [To do](README.md#to-do) list.

## Set-up and install
_I recommend using [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) to run py manually._

Install the requirements:

    $ python3 -m pip install -r requirements.txt

_Note: The [proxy/config.py](proxy/config.py) file should not be in a public repo, but once the secret key is public, I kept the file to facilitate the review. Normally, I would instruct copying and editing [proxy/config.py.tpl](proxy/config.py.tpl)._

<!--
Rename/copy the configuration template file [proxy/config.py.tpl](proxy/config.py.tpl) to the actual config file as proxy/config.py. For security purposes, only the template is in this repo.  

    $ cp proxy/config.py.tpl proxy/config.py  

> **or**, if sed is available:

    $ sed 's/secret-key/place-your-secret-key-here/' proxy/config.py.tpl > proxy/config.py

Note: A generic SECRET\_KEY is in the config file, so **edit config.py with your prefered secret key**.
-->

## The class to generate JWT
Here we play a little with the python console and the created class to [generate JWT](proxy/Token.py), so lets get to the prompt:

    $ python3
    >>> from proxy.Token import Token
    >>> user = 'fernando@github.com'
    >>> t = Token(user)
    >>> t.jwt


## Running the proxy server
By default, the proxy runs on port 5000. This can be changed in the [config file](proxy/config.py).

    $ python3 -m proxy

At this point, we should be able to browse: http://localhost:5000/  
Please remember to hit Ctrl+c to stop the web server when done.


## Containerise with the Dockerfile
_I assume that you have docker engine running. If not, please see [Get Docker](https://docs.docker.com/get-docker/)._

If you rather run the proxy in a single container, run:

    $ docker run --rm -d -p 5000:5000 --name proxy $(docker build -f Dockerfile -t proxy -q .)

To know IP and Port to the containerised app:

    $ docker inspect proxy | grep -e IPAddr.*[0-9] -e HostPort | sed 's/[^0-9\.]//g' | sort -u

After this, we should be able to browse: http://\<container IP\>:5000/  

To stop container and clean image, use:

    $ docker stop proxy && docker image rm proxy


## Run the Docker compose
_I assume that you have docker compose installed. If not, please see [Install Docker Compose](https://docs.docker.com/compose/install/)._

If you prefer running compose, please execute:

    $ docker-compose up --abort-on-container-exit

Now, we should be able to browse http://localhost:5000/  
Please remember to hit Ctrl+c to stop the web server when done.

To clean files, use:

    $ docker container rm $(docker container ls -a | grep _proxy | cut -d' ' -f1)
    $ docker image rm $(docker image ls -a | grep _proxy | sed 's/ \+/ /'g | cut -d' ' -f3)


## Logs
By default, logs are recorded in the 'logs' directory in the the project's root. However,
if you [containerise](README.md#containerise-with-the-dockerfile) the proxy, 
logs will be inside the container. And if you [docker compose](README.md#run-the-docker-compose), 
the container will use the hosts' dirs as in [Running the proxy](README.md#running-the-proxy-server).

Please see [docs/logs](docs/logs) if you wish to access samples of the generated logs.


## Documentation
Please try from python console:

    $ python3
    >>> import proxy
    >>> help(proxy)

Or try from command line:

    $ python3 -c "import proxy; help(proxy.config)"

All documentation can be found in [docs](docs).


## Automatic tests

The basic test for this project is in Bash script using curl and it tests proxy running manually, containerised or composed:

    $ bash tests/curl-post.bash


Other tests can run using unittest/PyUnit. With the proxy running, please run:

    $ python3 -m unittest tests/test_*


## To do

* Configure rotation of log files.
* Review docstring in db.py.
* Review this README.

