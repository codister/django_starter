# django_starter

In this tutorial we'll be setting up a virtual server to run a Django project via PostgreSQL + gunicorn + nginx.

## Clone this project

Clone this project to your computer by:

	git clone git@github.com:hyperknot/django_starter.git

## Setting up the server

### Create VPS

1. Order on [VULTR](http://www.vultr.com/?ref=6815091) (affiliate link), or on DigitalOcean. (I recommend VULTR)

2. Choose the $5 version in whichever location is closest to your users. For Europe I recommend Amsterdam. Select 32-bit, Ubuntu 14.04.
	![image](https://i.imgur.com/OYYfHkT.png)

3. Select SSH keys if you have one. Strongly recommended!
	![image](https://i.imgur.com/ujuArbI.png)

4. Wait for confirmation email, remember server IP address.
	![image](https://i.imgur.com/QuVKu0k.png)

### Log in via SSH

Linux/OS X: start terminal, type 

	ssh root@108.61.189.98

Windows, download [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) + [WinSCP](https://winscp.net/eng/download.php), configure connection, log in using Putty.

If you have set up SSH keys, you should not be asked to enter password. If not, you can see your initial password on the Vultr manage server page:

![image](https://i.imgur.com/g8KhZDd.png)

Finally, once you are in, you should see something like this.

![image](https://i.imgur.com/HOWzVQS.png)

### Update packages

This is not needed on VULTR as all new orders are updated, but not all providers are like this.

	apt-get update
	apt-get dist-upgrade

### Configure SSH

You can avoid most automatic hacking attempts by changing your SSH port from default. If you have an SSH key, you should also disable password based authentication.

#### If you do not have an SSH key (common on Windows)

Run `nano /etc/ssh/sshd_config` and change the port line to something different, between 10000 and 65000, for example 23232. Save the file using `Ctrl + X`, say `Y`. Now, restart the ssh server by running: `service ssh restart`

Change your ssh configuration in Putty to use port 23232.

#### If you have an SSH key

If you didn't import it via the VULTR web interface, you can do so from command line  by (you might need `brew install ssh-copy-id` or `apt-get install ssh-copy-id` first): 

	ssh-copy-id root@108.61.189.98

Now that you have set up your SSH keys, you should make your SSH config stronger. We will disable login via password authentication (but allow root for now).

Go to the `deploy/server-conf` directory and use scp to upload the `sshd_config` file to the server.

	 cd deploy/server-conf/
	 scp sshd_config root@45.32.239.52:/etc/ssh/sshd_config
	
Log in to the server via SSH and issue the following command:

	service ssh restart
	
Press Ctrl + D to exit the ssh session.
	
	
#### Save the server to your SSH config (Linux/OS X only)

Edit the file: `~/.ssh/config` and insert the following into it (substitute with your server's IP address):

```
Host my-little-server
  HostName 108.61.189.98
  user root
  port 23232
```

Now try connecting to your server simply with `ssh my-little-server`


### Create a linux user

Create a Linux user which will run our application.

On the server, run `adduser starter`, and give any password you prefer. Just press return to skip the rest of the questions.

```
root@vultr:~# adduser starter
Adding user `starter' ...
Adding new group `starter' (1000) ...
Adding new user `starter' (1000) with group `starter' ...
Creating home directory `/home/starter' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
No password supplied
Enter new UNIX password:
Retype new UNIX password:
No password supplied
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for starter
Enter the new value, or press ENTER for the default
	Full Name []:
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n]
```

### Install and configure PostgreSQL

On your server, run `apt-get install postgresql-9.3`, press y when asked.

Change PostgreSQL authentication settings:

	echo "local all all peer" > /etc/postgresql/9.3/main/pg_hba.conf
	
Restart the PostgreSQL service:

	service postgresql restart

Now we will use `su` to run the following commands as `postgres` user. 
	
	root@vultr:~# su - postgres
	postgres@vultr:~$ createuser starter --createdb

Press Ctrl + D to return to the root session.


### Install and configure Nginx

On your server, run `apt-get install nginx` and press y when asked.

Upload the nginx configs. Run the scp commands on your computer from `deploy/server-conf/`:

	scp nginx.conf my-little-server:/etc/nginx/
	scp mime.types my-little-server:/etc/nginx/

On the server, restart nginx

	service nginx restart
	
### Install various packages

On your server, run `apt-get install supervisor python-virtualenv python-dev libpq-dev build-essential` and press y when asked.


## Set up the Django project

### Create the directories for the project

On the server, run the following commands:

	cd /home/starter/
	mkdir -p web/logs web/media web/static	

### Clone / upload your project to the server

You can either upload your project by a rsync, or using a GUI app (like WinSCP), or by settings up Git deployment (read-only) keys for your server on Github / Bitbucket.

I recommend setting up Git deployment keys, but it'd be outside the scope of this tutorial, so we will just use rsync to copy our project files to the server.

Run the following command on your computer:

	cd .. # until you are outside django_starter project
	rsync -avz --delete django_starter/ my-little-server:/home/starter/web/app/
	
This synchronizes the contents of your django_starter folder to your server's /home/starter/web/app/ folder.

### Create the virtualenv

	cd /home/starter/web/app
	virtualenv venv
	venv/bin/pip install -r requirements/production.txt
	

	

supervisor /etc/supervisor/conf.d/*.conf








