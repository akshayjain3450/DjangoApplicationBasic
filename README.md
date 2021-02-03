# DjangoApplicationBasic
Basic Django Application : SignUP, LoginIN, GetData (10 Users)

## Setting up this Application on your local machine
 1. Create a virtual environment(for Linux-Ubuntu 20.04) <br />
 Command: python3 -m pip install --user virtualenv <br />
 2. Clone the repository in the same virtual environment <br />
 Command: git clone https://github.com/akshayjain3450/DjangoApplicationBasic.git <br />
 3. Activate the virtual environment <br />
 Command: source virtualenv/activate/bin <br />
 4. Install Dependencies <br />
 Command: pip3 install -r requirements.txt <br />
 5. Configure the Database of the application on local machine <br />
 Command: python3 manage.py makemigrations <br />
 Command: python3 manage.py migrate <br />
 6. Run Application <br />
 Command: python3 manage.py runserver <br />
<br /> <br />

## URLS:
1. Home Page: http://127.0.0.1:8000/ <br />
Here you can visit Register Yourself! <br /> or can Sign IN (if already registered) <br />
2. Registration/Signup: http://127.0.0.1:8000/accounts/signup <br /> 
Enter Details: Full Name, Email, Username, Role, Password and click on SignUP! <br />
3. Sign In: http://127.0.0.1:8000/ <br />
4. After Signing In you can use Get Details of Employees Function by clicking on Get Employee Details <br />