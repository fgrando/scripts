# scripts

This repo contains some ideas and  quick'n dirty scripts for my personal projects.  
Please feel free to contribute and ask questions.




## latex: template to landle portrait and landscape pages
This template uses a background image for each mode (landscape and portrait).
Also, the headers and footers are always aligned with text (as in portrait mode), even in landscape pages.


## httpserver: small httpserver using python 3 embedded http.server
Can run commands from server by urls



## EmailSender.py: script to send emails with attachments.
Simple python email client (SMTP SSL) to send emails. It can send attachments now.
Tested with python2.7 and gmail account.
Example:
```
	sender = EmailSender("smtp.gmail.com", 465, "<youremail>@gmail.com", "<yourpassword>", log)

    ret = sender.send(["<destination>@gmail.com"], "simple email", "hello world")

    ret = sender.send(\
        [\
            "<destination>@gmail.com"\
        ],\
        "This email contains attachments",\
        "Lorem ipsum lalalala",\
        [\
            "/home/fgrando/fix_mouse.sh",\
            "/home/fgrando/Pictures/mypic.png",\
            "/home/fgrando/Desktop/file.pdf",\
            "/home/fgrando/Desktop/audio.mp3",\
            "/home/fgrando/Desktop/video.mp4",\
            "/home/fgrando/Desktop/zipped.zip"\
        ]\
    )
```


## log.py: Log facility for python scripts
Example:
```
	from log import *
	log = Log("example").get()
	log.info("hello!")
```
Output:

```
2020-03-22 09:57:10,010 - example - INFO - Log started with name: 'example' file: 'None' level: '10'
2020-03-22 09:57:10,010 - example - INFO - hello!
```


## TBD 
