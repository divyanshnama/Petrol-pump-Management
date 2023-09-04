# PetrolPump-Management-System [DBMS]  

### FrontEnd
### Backend
### Project File Structure 
### How To Run
### Screenshots

### FrontEnd

- In this Project, frontend part is done by using famous Python library streamlit.

-  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.

- We can Perform operations such as Create, Read, Delete, Update aslso known as [CRUD] Operations.

- There is one user defined function which calculate Toltal Price in Tanker table and a Trigger which is preset in Employee table which get activated when someone Try to update Salary field if salary is less that 300000. 

### Backend

- In Backend creation of table and table population is done in MySQL 
- It also uses libraries such as Pandas, sql connector, Streamlit 
- It is mostly done Using Python Language. 

## Project File Structure 

### In Projets folder the following files are present 
* create_database.py --> This file is used to Create database Ptrolpump_Management  
* app.py --> This is the main file you need to run after creation of the databases. It has codes for GUI part.
*  databases.py --> This file has all the important function calls
* create.py --> It creates new table rows when you want to add new data.
* delete.py --> It has delete function implementation used for deleting any specific row in table.
* read.py --> It read data from table and send it to view function to display.
* update.py -->  It updates the data in the table.

## How TO RUN 
- First create databases using Create_database.py
- Install all the librarys
- run app.py file using command: "Python -m streamlit run app.py"


## Screenshots
<img width="881" alt="Screenshot 2023-09-04 111735" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/3f1b2cb9-0308-4c8f-9d61-34ab1a18b031">
<img width="853" alt="Screenshot 2023-09-04 111817" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/8b700ef7-52b1-45c6-990c-d516bf21e9f7">
<img width="860" alt="Screenshot 2023-09-04 111833" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/8d9020e0-3bf0-4be6-973a-e2d1037ea451">
<img width="860" alt="Screenshot 2023-09-04 111347" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/ee82b248-44ab-41fe-abca-baa7467a9350">
<img width="851" alt="Screenshot 2023-09-04 111500" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/f9a4643e-4c99-4219-ac1b-ec4d99cd60e6">
<img width="897" alt="Screenshot 2023-09-04 111524" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/c1f2b8eb-2a84-4707-8445-81807792fa17">
<img width="838" alt="Screenshot 2023-09-04 111608" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/f16ee450-389d-4669-92d5-5a6ce52496db">
<img width="848" alt="Screenshot 2023-09-04 111712" src="https://github.com/divyanshnama/Petrol-pump-Management/assets/104021285/8b8e15d3-60aa-43a0-8fa8-776152a8f679">

