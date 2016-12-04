![AutomataTranslator](https://github.com/allexlima/PyBestfit/blob/master/img/icon.png?raw=true)
### Welcome to PyBestfit
### Memory Allocation Simulation using best fit Algorithm

This Software can be used as an educational approach for simulation of memory allocation algorithms. 
Although initially __just best fit has been implemented__ here, you can contribute with this project 
forking and send pull requests with improvements made. 

This was an final project presented at UniNorte Laureate University through __Operating Systems__ discipline, 
ministered by _Prof.ª Ângela Lima, M.Sc_.

#### A short intro about best fit algorithm

The best fit deals with an algorithm that searches the first closest memory block size of process size to alloc it one. 
And as an advantage, best fit provide a memory utilization more optimized. 

You can find a quickly content about more allocation algorithms accessing the last item of [References](https://github.com/allexlima/PyBestfit#references). 
For a deep reading about this subject, I recommend the two firsts items of [References](https://github.com/allexlima/PyBestfit#references).

### Index

1. [Repo structure](https://github.com/allexlima/PyBestfit#repo-structure) 
2. [Workspace tips](https://github.com/allexlima/PyBestfit#workspace-tips)
3. [Requirements](https://github.com/allexlima/PyBestfit#requirements)
4. [Setup](https://github.com/allexlima/PyBestfit#setup)
5. [Basic usage](https://github.com/allexlima/basic-usage)
6. [References](https://github.com/allexlima/PyBestfit#references)

#### Repo structure

    .
    ├── img
    │   ├── about.png
    │   ├── github.png
    │   ├── icon_old.png
    │   └── icon.png
    ├── nano_os
    │   ├── __init__.py
    │   ├── memory.py
    │   ├── processor.py
    │   └── support.py
    ├── LICENSE    
    ├── README.md
    ├── interface.ui     
    ├── interface.py   
    ├── ui_manager.py 
    ├── cli_testing.py    
    └── app.py


#### Workspace tips

I advise you to use these tools to make easier your work and save time:

1. Some unix-based OS as [Debian](http://debian.org), [Ubuntu](http://www.ubuntu.com/) or [OSX](http://www.apple.com/in/osx/);
2. [PyCharm IDE](https://www.jetbrains.com/pycharm) (it's [free for students](https://www.jetbrains.com/student/));
3. Read about [PyQt](https://nikolak.com/pyqt-qt-designer-getting-started/) can be helpful.

### Requirements [not pip-installable]

1. **Python 2.7.x** 

    Download Python 2.7.x interpreter [here](https://www.python.org/).

2. **PyQt4** 

    * If you are using a Debian-based system, you can install it using the following command:

        ```bash
        $ sudo apt-get install python-qt4
        ```
     
    * If you are using OS X:
    
        ```bash
        $ brew install pyqt
        ```
    * You can also find a compatible version for your system in [oficial PyQt website](https://www.riverbankcomputing.com/software/pyqt/download).

#### Setup

1. Clone the repo

    ```bash
	$ git clone https://github.com/allexlima/PyBestfit.git
	$ cd PyBestfit/
	```

2. Run **PyBestfit**
    
    ```bash
	$ python app.py
    ```
    
    - If you want run without graphical interface, enjoy yourself with `cli_testing.py` example.

#### Basic usage

1. Running `app.py`, this window will open:

    ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/1.png?raw=true)

2. You must click on the __Create__ button to generate pseudo-random values, then you can to browse through tabs:
    
    - Memory values:
    
        ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/2.png?raw=true)
        
    - Processes values
    
        ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/3.png?raw=true)
        
    - And logs:
    
        ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/4.png?raw=true)
        
3. Now, clicking in __Memory Alloc__ button, you will allocate the generated process in a memory spaces 
through the best fit algorithm. 

    ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/5.png?raw=true)
    
    ![](https://github.com/allexlima/PyBestfit/blob/master/img/screenshots/6.png?raw=true)

4. To generate new values, click in __Update__ button.

5. __Testing mode__ can be checked to use pre-defined values in memory block sizes.
These values ara in `SIZES` list, available in `nano_os/support.py`.

#### References

1. Tanenbaum, A. S., & Bos, H. (2014). _Modern operating systems_. Prentice Hall Press.
2. Maziero, C. A. (2013). _Sistemas Operacionais: Conceitos e Mecanismos_. Online: http://dainf.ct.utfpr.edu.br/~maziero/lib/exe/fetch.php/so:so-cap09.
3. Summerfield, M. (2007). _Rapid GUI programming with Python and Qt: the definitive guide to PyQt programming_. Pearson Education.

##### Support links

- https://nikolak.com/pyqt-qt-designer-getting-started/
- https://www.tutorialspoint.com/operating_system/os_memory_allocation_qa2.htm

---

Developed by [Allex Lima](http://allexlima.com), [Daniel Bispo](https://github.com/danielbispov/), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python 2.7.x](https://www.python.org/) and [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)! 
###### Copyright © 2016 [PyBestfit](https://github.com/allexlima/PyBestfit) - Licensed by MIT LICENSE.
