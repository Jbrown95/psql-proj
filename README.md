The scope of this project is to answer 3 questions with a given database.
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

===============================
Step 1). Follow theses instructions given in the course to setup your system.
===============================
Installing the Virtual Machine:
In the next part of this course, you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called Vagrant(https://www.vagrantup.com/) and VirtualBox(https://www.virtualbox.org/wiki/Downloads) to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

Conceptual overview:
This video(https://www.youtube.com/watch?v=djnqoEO2rLc) offers a conceptual overview of virtual machines and Vagrant. You don't need to watch it to proceed, but you may find it informative.

Use a terminal:
You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com(https://git-scm.com/downloads).

For a refresher on using the Unix shell, look back at our Shell Workshop.

If you'd like to learn more about Git, take a look at our course about Git.

Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here(https://www.virtualbox.org/wiki/Downloads ). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com(https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.
Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: FSND-Virtual-Machine.zip(https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

Navigating to the FSND-Virtual-Machine directory and listing the files in it.
This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows.
Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

Starting the Ubuntu Linux installation with vagrant up.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

Logging into the Linux VM with vagrant ssh.
Wow, that worked!
If you've gotten logged into your Linux VM, congratulations. If not, take a look at the Troubleshooting section below.

The files for this course
Inside the VM, change directory to /vagrant and look around with ls.

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:

Running psql, the PostgreSQL command interface, inside the VM.
Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM.
Troubleshooting
I'm not sure if it worked.
If you can type vagrant ssh and log into your VM, then it worked! It's normal for the vagrant up process to display a lot of text in many colors, including sometimes scary-looking messages in red, green, and purple. If you get your shell prompt back at the end, and you can log in, it should be OK.

vagrant up is taking a long time. Why?
Because it's downloading a whole Linux operating system from the Internet.

I'm on Windows and getting an error about virtualization.
Sometimes other virtualization programs such as Docker or Hyper-V can interfere with VirtualBox. Try shutting these other programs down first.

In addition, some Windows PCs have settings in the BIOS or UEFI (firmware) or in the operating system that disable the use of virtualization. To change this, you may need to reboot your computer and access the firmware settings. A web search can help you find the settings for your computer and operating system. Unfortunately there are so many different versions of Windows and PCs that we can't offer a simple guide to doing this.

Why are we using a VM? It seems complicated.
It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.

I got some other error message.
If you're getting a specific textual error message, try looking it up on your favorite search engine. If that doesn't help, take a screenshot and post it to the discussion forums, along with as much detail as you can provide about the process you went through to get there.

If all else fails, try an older version.
Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from the Vagrant releases index(https://releases.hashicorp.com/vagrant/).

===============================
Step 2). The next step is still from the course, follow the following instructions.
===============================

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

Successfully logged into the virtual machine.
Download the data
Next, download the data here(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.


To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration(https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) into a fresh new directory and start it from there.

Explore the data
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

\dt — display tables — lists the tables that are available in the database.
\d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.
===============================
Step 3).
===============================

Download my file into the vagrant directory. It should contain the newsdata.sql file. after putting my project.py file into this folder, ssh into vagrant and cd into /vagrant. this will be a copy of the folder that holds the newsdata.sql. run my program by typing 'python3 project.py'. this should properly run my program, displaying answers to the three questions.
