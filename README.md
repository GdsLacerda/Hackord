# Hackord v1 [ v2 Coming Soon ]
### A new powerfull tool for automatic account creation of [Discord](https://discord.com/) accounts

Before asking for help please read FAQ.  
Do you want to get touch in touch with us?  
Join our [discord server](https://discord.gg/KCqrbVgSBF)!

### FAQ  
**Q:** What is Hackord?  
**A:** Hackord is open source advenced Discord raid tool / account generator.

**Q:** Is it a virus?  
**A:** No it isn't, and if you don't trust us, you can look at [source code](https://github.com/WieszakWare/Hackord) of our program or even run/compile from [source](#how-to-runcompile-from-source)!

**Q:** Hey you can change this and this and...  
**A:** If you would like to change/patch something in Hackord, you can always fork this project and create pull request.

**Q:** Is Linux/MacOS supported?  
**A:** For now we are not planning to add Linux/MacOS support, but we included intrustion on how to run from source for MacOS and linux too, so if you want you should be able to try, but we do not promise that code will be working on those platforms.

**Q:** Can I republish/modify this project?  
**A:** This project is licensed under [GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).

### How to run/compile from source.
Don't trust our pre-compiled binaries?  
Here we will teach you how you can run from source code.  
Note for Linux users: As your case is a little bit diffrent documentation (or kinda lack of it) has been moved to [Running under Linux Section](#running-under-linux).  
Also as we mentioned in [FAQ](#faq), we are creating Hackord for windows and MacOS/Linux is not supported. While we give instruction on how run it, we can't be 100% if it is going to run under those platforms. And we are not planning on adding support any time soon.

#### Downloading Python (Windows/MacOS)
Hackord is using Python 3.10.4.  
You can download it from [official python website.](https://www.python.org/downloads/release/python-3104/).  
Also make sure you have `Add Python 3.10.4 to PATH` checked at the bottom.  
Now to make sure you have installed python,  
- **On Windows**: Press Windows button and search for `cmd` or `Command Prompt`.
- **On MacOS**: Idk, I don't use it just open your terminal.
And type `python --version` or `python3.10 --version`. if you see output saying that python version is 3.10.4 it means that you have sucessfully installed python, if not then it means that you have screwd something up. And please don't create issues or beg for help with installing python, just google the tutorial.

#### Downloading code and preparing envrioment (Windows/MacOS)
Now to download source code go to [code tab](https://github.com/WieszakWare/Hackord). Under the green `Code \/` menu, you can click `Download ZIP`. Now unzip the contest and for simplify documentation I will have path pointent to your desktop.
MACOS NOTE: In [Drivers](https://github.com/WieszakWare/Hackord) folder, replace chrome driver with Chrome Driver for MacOS, you can download it from [official chrome webiste](https://chromedriver.chromium.org/) and replace gecko driver witb Firefox Driver for MacOS, you can download it from [official firefox github page](https://github.com/mozilla/geckodriver/releases).  
Once you have unziped you can execute the following commands:  
NOTE: Replace the path to Hackord with your own path, and replace python with python3 or python3.10 if it is the command you have python bind to.  
For Windows:
```
cd C:\Users\USER_USERNAME\Desktop\Hackord
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
venv\Scripts\deactivate
```
For MacOS:
```
cd ~/Desktop/Hackord
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
venv/bin/deactivate
```

#### Running code (Windows/MacOS)
Now everytime you want to launch Hackord from source you have to type following command.
Windows:
```
cd C:\Users\USER_USERNAME\Desktop\Hackord && venv\Scripts\activate && python main.py && venv\Scripts\deactivate
```
MacOS:
```
cd ~/Desktop/Hackord && venv/bin/activate && python main.py && venv/bin/deactivate
```
