HOW TO RUN THE PROGRAM

1. Open Docker Desktop and wait for it to load
2. Open Git Bash, Windows Power Shell or cmd and type:

cd <path-to-your project>

for example: 

cd /c/python-missing-page-numbers 

if you will have to copy the path from somewhere in Windows and you use Git Bash, change "\" to "/"

3. Type another command for the first usage:

docker-compose up --build

and wait

4. For another usages just type:

docker-compose up

HOW TO USE IT 

1. Change data.csv in the way that is shown with example data
2. Go to the http://localhost:8008/docs and choose the GET method, you should have all the information listed
3. Alternatively to step 2, you can just shortcut and go to the http://localhost:8008/