# **Hackord**
[![Generic badge](https://img.shields.io/badge/Python%20Version-3.10.4-blue.svg)](https://www.python.org/downloads/release/python-3104/)  
[![Generic badge](https://img.shields.io/badge/Hackord%20Version-V1.0.3-red.svg)](https://github.com/WieszakWare/Hackord/releases)  
## Powerful next-gen discord account generator made in python3.

![Hackord_Raid_Tool](https://user-images.githubusercontent.com/111588764/197583768-3f98952d-a024-4464-9425-6ff6ae446137.png)

&nbsp;  
## **FAQ**

**Q:** What is Hackord?  
**A:** Hackord is automation tool for creation of discord account. 

**Q:** Why this even exists? I can create accounts manually.  
**A:** Creating accounts manually is absolute hassle, and you can be heavily rate limited by discord or sometimes even blocked for several days! Hackord aims to automate this process and also to bypass discord's limits.

**Q:** How can I be sure that it's not a virus?  
**A:**  As Hackord is open source you can look yourself into code and check what it is really doing, so it would be kinda stupid from our side to do anything sketchy.

**Q:** Can I modify/redistribute Hackord?  
**A:** Hackord is licensed under [GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt), so it means, **yes**.

**Q:** How do I run this?  
**A:** Please refer to [Running Hackord](#running-hackord).

**Q:** Can you add feature `x` and `y`.  
**A:** If you want to propose some features you can join our [discord server](https://discord.com/invite/KCqrbVgSBF) and discuss them in [leafuware-suggestions](https://discord.com/channels/943896316373766174/1034132943284748388).

**Q:** I got problem, how the f\*\*\* am I supposed to fix it?  
**A:** First make sure you have [properly setup hackord](#running-hackord), if you believe you have done everything right, you can open new [issue](https://github.com/WieszakWare/Hackord/issues/new) here on github, but because not everyone have github you can also submit them on our [discord server](https://discord.com/invite/KCqrbVgSBF) in [leafuware-help](https://discord.com/channels/943896316373766174/1033350704972189716) channel.

**Q:** I have made some changes/fixes, can I submit them.  
**A:** **Of course!** We appreciate all help from our community and are open to any contribution made into our projects.


## **Running Hackord**
Some notes before we start.  
- Owner of Hackord is developing on Windows and because we don't have infinite time we can not test Hackord on Linux/Mac OS so if you happen to be running one of those and ran into issue, please report it as our goal is to make Hackord platform independent.  
- For now Hackord V1 relies on  `chromedriver`, because of first point, we can not test other binaries of chromedriver, so please replace it with binary corresponding to your system, you can download them from [official chromium website](https://chromedriver.chromium.org/downloads).
- For the sake of simplicity I am going to assume Hackord's folder is located on your desktop.

1. Download Hackord src.  
    *Option 1*: Download through github's interface.  
    ![Download Image](./README_images/download.png)  
    **Note: You have to extract files from zip file.**  

    *Option 2*: Download using git.
    ```
    git clone --depth 1 https://github.com/WieszakWare/Hackord.git
    ```
2. Install Python 3.10.4, for **Windows** and **Mac OS** we recommend to download it from [python's website](https://www.python.org/downloads/release/python-3104/), and for **Linux** users use package manager of your choice and install it from your repositories.
3. Open Terminal/Konsole for your system.  
    **Windows**: Start Menu -> Type `cmd`.  
    **Linux**: Idk, just open terminal of your choice, shell... bash or zsh. Doesn't really matter.  
    **Mac OS**: Idk, I don't use mac but you should have terminal somewhere.
4. Navigate to Hackord's folder.  
    NOTE: Make sure that you replace `[HACKORD_FOLDER]` with name of your Hackord folder.  
    **Windows**:
    ```
    cd %USERPROFILE%/Desktop/[HACKORD_FOLDER]
    ```
    **Linux**:
    ```
    cd ~/Desktop/[HACKORD_FOLDER]
    ```
    **Mac OS**:
    ```
    cd ~/Desktop/[HACKORD_FOLDER]
    ```
5. Now type
    ```
    python main.py
    ```
    to launch Hackord.  
    In case you get `command "python" not found`, make sure you have installed Python properly as shown in step number 2.
    If you get error `can't open file 'main.py'`, make sure you have navigated into Hackord's directory as shown in step number 4.

### **That's it!**
You have just installed Hackord!  
We hope that you are going to enjoy our program.
&nbsp;  
&nbsp;  
# **!!! DISCLAIMER !!!**
## **FOR EDUCATIONAL PURPOSES ONLY. HACKORD COMES WITH ABSOLUTELY NO WARRANTY. DEVELOPER/CONTRIBUTORS ARE NOT RESPONSIBLE FOR ANY DAMAGED CAUSED BY HACKORD OR ANY ACTION OF THE USER! USE IT AT YOUR OWN RISK!**
