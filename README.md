# twitter-mining-workshop
This is a basic hands-on workshop on mining Twitter data using Python. Twitter public data offers a lot of possibilities in public health research and this workshop will be interesting to public health and informatics researchers, as well as everyone interested in social media data mining. The workshop doesn't require Python knowledge, because scripts and programming environment will be readily provided to attendees in a computer lab. Attendees will learn how to access public data on Twitter using Python programming language, how the data is structured (what is JSON format), how the data can be filtered, analyzed and graphed, and also how to export results into CSV format.

**Developer:** Dajun Tian
<br>Center for Biomedican Informatics
<br>Washington University in St. Louis

For the workshop the following technical requirements were used:
- WinPython-64bit-2.7.10.2 (portable version of Python, can be downloaded here http://winpython.github.io/)
- Python packages installed: twython, numpy, matplotlib. Packages matplotlib and numpy come with WinPython by default. You only need to download twython package (from here https://pypi.python.org/pypi/twython) and install it using "WinPython Control Panel" application inside WinPython folder.
After you install WinPython, which will be presented as a directory with a lot of files, run Spyder application from it and execute the provided scripts in order of steps.

Otherwise, you can install Python v2.7 or later version and make sure the packages above are installed as well.

###Before you run scripts:
- Create a developer account and an app in Twitter (see PowerPoint or PDF presentation)
- Take note of the 4 credentials you got when you created the account and app
- Populate the 4 variables in step1.. scripts with the credentials you got (same in "streaming twitter.py" script).

###Troubleshooting problems with scripts:
- If you encounter errors running scripts, try commenting out (just add # to beginning of line) on each line where it says "def on_error(self):        self.disconnect()"
- If the script takes a long time to execute, it may be related to the fact that it's pulling tweets in real-time, so you may have to wait a while, until the max amount of tweets is collected.
