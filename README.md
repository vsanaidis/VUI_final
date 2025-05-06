# VUI_final
This repository was created to upload the final project of our team
# INSTRUCTIONS
1) Make sure you have created a virtual environment
2) Activate the venv and run "rasa init", if you dont have rasa run "pip install rasa" and then "rasa init"
3) After initiating rasa, run "rasa train"
4) Then you can run either on shell **BUT IT IS RECOMMENDED** to host a local server so you can see the frontend
5) To run a local server, open three terminals on your vscode OR terminal
6) On the first terminal run rasa with the command : "rasa run --cors "*" --enable-api"
7) On the second terminal you should run rasa actions: "rasa run actions"
8) On the third terminal run your local server (Make sure you have python installed): "python -m http.server 8000"
9) Now you can visit the server, make sure that rasa is up and running
10) Visit the server at [http](http://localhost:8000/index.html), if having any issues check the manual.docx
