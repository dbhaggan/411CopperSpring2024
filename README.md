# 411CopperSpring2024
---
# Setup the Django environment locally on Windows
1. Clone the 411CopperSpring2024 Repository to your local machine.  

2. Create a folder inside the 411CopperSpring2024 repo you just cloned.
   ```mkdir virtualenv```
 
3. Create the virtual environment
   ```python -m venv virtualenv```

4. Activate the virtual environment
   ```cd virtualenv\Scripts```
   ```.\activate```
   On windows due to security, certain scripts cannot be run
   Use this link to help over come the issue: https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell 
   For more information use the following link: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4

5. Once the virtual environment is activated you will now need to install the required 
   ```python -m pip install -r requirements.txt```

6. Navigate to the 411CopperSpring2024 Git repo that you just cloned.

7. In the local repo, there will be a percussatsight folder, navigate to that

8. In the percussatsight folder, run the following to get the app running on your local machine
   ```python manage.py runserver localhost:8080```

9. After the development server is initialized, in the browser go to 
   ```localhost:8080```

---
# Setup the Django environment locally on Linux
1. Clone the 411CopperSrping2024 Repository to your local machine.

2. Create a folder inside the 411CopperSpring2024 repo you just cloned. 
   ```mkdir virtualenv```

3. Install the utility needed to created the virtualenv. 
   ```pip3 install virtualenv```

4. Create the virtual environment.
   ```virtualenv (directory inside the cloned repo)```
   ```virtualenv virtualenv```

5. Activate the virtual environment. 
   ```source virtualenv/bin/activate```

6. Navigate to the 411CopperSpring2024/percussatsight directory. 

7. With the virtual environment currently active, install the requirements.txt. 
   ```pip3 install --upgrade pip```
   ```pip3 install -r requirements.txt```

8. If you haven't already, please install mysqlclient through the commands:
	```sudo apt-get install libmysqlclient-dev```
	```pip3 install mysqlclient```
Then verify installation with
	```pip3 show mysqlclient```


9. You should now be able to run the demo server to view a demo site.
   ```python manage.py runserver localhost:8080```

10. In the browser you can type localhost:8080 in the search bar and that should take you to the site.






From here, all Chris saw was the "Welcome to Vue" File. Here's what he had to do to actually see the percussatsight homepage (though it wasn't rendered properly):

docker-compose up -d
pip3 install -r requirements.txt (from the directory "requirements.txt" was in)

Then, I commented out the HOST IP from percussatsight/percussatsight/settings.py, and replaced the IP address with 127.0.0.1

Then I ran
python3 manage.py runserver

I got a red warning message, but it was fine. I then went to the IP address listed in the terminal.
