# Bash Homework 1
Due: Tuesday September 13th by Class time.

## Friendly Warning

- Folder names, paths, filenames are all case sensitive. 
- Nearly every assignment I ask you to do the same things. 
- For example: 
    - Create a folder called `homework_X` and put it in the `/xyz` folder.
    - Then write a script called `abc-1.sh` and put it the `homework_X` folder.
- Then I will log in to your server and try to execute:
    - `/xyz/homework_X/abc-1.sh`
- If it runs then great, if it doesn't then something was named wrong:
    - `/xyz/homework_Y/abc-1.sh`
    - `/xyz/homework-X/abc-1.sh`
    - `/xyz/homework_X/abd-1.sh`
- It's the same concept as:
    - `https://googe.com` is NOT
    - `https://google.com` 
- One character wrong means I don't find it (and I don't grade it). 
- So read carefully and if I didn't specify a name for your files, you may want to ask. 

## Prep Work

- Make sure there is a user: `griffin` on your server with the password `2D2016!!!` and sudo access (if there is not it will mean an automatic zero for this assignment because ... I can't grade it if I can't log in).
- Log into your server and `cd /opt` 
- You will need to be `root` to edit the `/opt` folder
- Clone your github repository in the `/opt/` folder. 
- Make a folder called `assignments` in your github repo.

- ![][folder] /opt
    - ![][folder] /your4103repo
        - ![][folder] /assignments

### Work Flow (Still Prep)

You can get your work done however you want as long as your scripts end up:

1. On github.
2. On your server at the prescribed path. 

**Method 1** - Editing locally:

- Assuming the above steps are complete and you cloned your github repo.
- Using gitbash create a local folder called `homework-01` in the `assignments` folder of your repo.
- Keep working locally in gitbash (in your `homework-01` folder) and forget about the server or github for now.
- Write all your scripts (naming them correctly) in this folder.
- You can use any editor to get this done since your local and not connecting via SFTP.
- Once finished you should have a directory structure like this:

- ![][folder] /your4103repo
    - ![][folder] /assignments
        - ![][folder] /homework-01 
            - ![][script] command_args.sh
            - ![][script] myrandom.sh
            - ![][script] versiona.sh
            - ![][script] versionb.sh

- Then from here ![][folder] /your4103repo run:
    - `git add -A`
    - `git comit -m "adding homework 1"`
    - `git push origin master`
- This should put all your files on github.

- Now lets pull your files down from github onto your server:
    - Login to your server and goto directory `/opt`
        - Run `git clone git@github.com:yourusername/your4103repo.git`
    - If your repo is already there:
        - `cd  /opt/your4103repo`
        - `git pull`

**Method 2** - Editing on the server:

- Login to your server and goto directory `/opt`
- Run `git clone git@github.com:yourusername/your4103repo.git`
- If your repo is already there, then pull in any updates:
    - `cd  /opt/your4103repo`
    - `git pull`

- Now connect via the `npp-ftp` plugin.

| Notepad ++ Connect via SFTP|
|:----------------:|
| Click the "cog" wheel to open profile settings: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/183u17421b3s3u012p3Z/npp1.png?X-CloudApp-Visitor-Id=1094421) |
| Create a new profile: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/1a2s0w1s2i0M3a1d1T3h/npp2.png?X-CloudApp-Visitor-Id=1094421) |
| Choose that profile to log in: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/422h3Q0X093r1w473Z2c/npp3.png?X-CloudApp-Visitor-Id=1094421) |

- Create a folder called `homework-01` in the `/opt/your4103repo/assignments` folder via the notepad++ interface.
- Create all your scripts in your `homework-01` folder using notepad++.
- Your directory structure should look like the following:

- ![][folder] /your4103repo
    - ![][folder] /assignments
        - ![][folder] /homework-01 
            - ![][script] command_args.sh
            - ![][script] myrandom.sh
            - ![][script] versiona.sh
            - ![][script] versionb.sh
            
- Now that the server is all set, we need to push our changes to github.
- Log in to your server and go to `/opt/your4130repo`
- From your github repo folder run:
    - `git add -A`
    - `git comit -m "adding homework 1"`
    - `git push origin master`

## Write Scripts 

### Script 1

- Create a script called `command_args.sh` which will read in all command line arguments and print them out.
- For example `$ ./command_args.sh arg1 "hello" 44` would print out:

```
command_args.sh
(contents of arg1)
hello
44
```



### Script 2


- Create a script which will print a random word. There is a file containing a list of words on your system (usually /usr/share/dict/words or /usr/dict/words). Hint: Piping will be useful here.
- Name this script: `myrandom.sh` and when run, should print out 1 random word to std out.


### Script 3 

- Create a script which will take a filename as its first argument and create a dated copy of the file. eg. if the file was named `file1.txt` it would create a copy such as `2016-01-28_file1.txt`. (To achieve this you will probably want to play with command substitution and the command date).
- Name this script `versiona.sh`.

### Script 4

- Using the script from `versiona.sh`, see if you can get it so that the date is after the name of the file (eg. file1_2016-01-28.txt (The command `basename` can be useful here.)
- Name this script `versionb.sh`. 

[folder]: https://d3vv6lp55qjaqc.cloudfront.net/items/3W1y1J0U2W2A2N3P2D1V/folder.gif?X-CloudApp-Visitor-Id=1094421 "Folder Alt"
[script]: https://d3vv6lp55qjaqc.cloudfront.net/items/2F2A3E2T2b061P2a1v3P/script.gif?X-CloudApp-Visitor-Id=1094421 "Script Alt"
[text]: https://d3vv6lp55qjaqc.cloudfront.net/items/0h1U2s1B040P141F0R0u/text.gif?X-CloudApp-Visitor-Id=1094421 "text alt"
[python]: https://d3vv6lp55qjaqc.cloudfront.net/items/092A1b1N3w16020g3e3S/py.gif?X-CloudApp-Visitor-Id=1094421 "python alt"
