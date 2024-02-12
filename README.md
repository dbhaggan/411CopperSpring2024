# 411CopperSpring2024
---
# Setup the Django environment locally on Windows
1. Clone the 411CopperSpring2024 Repository to your local machine. 

2. Create a folder adjacent to the 411CopperSpring2024 repo you just clone.
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
