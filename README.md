# Forestry-TabPy
Tableau is a famous tool in research community. While it offers some existing functionalities for data analysis, these may not always meet the needs of researchers
Therefore, the Forestry-TabPy comes in handy, it contains some Python scripts that aim to preprocess the data (csv), discover strong relationship among attributes, and also allow to do some advanced analyses such as KMeans clustering.


## How to run
You can skip step #1 and #2 if you already installed python and pip
1. Install python (python <= 3.11 required) by downloading https://www.python.org/downloads/release/python-3118/

2. Download and install pip:

    - Download: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - Install: python3 get-pip.py

3. Go to the Forestry-TabPy folder. Ex: `cd Forestry-TabPy`

4. Install virtual environment package: `pip install virtualenv`

5. Create virtual environment for the project: `python3 -m venv venv`

6. Activate the virtual environment:

    - On Windows: `venv\Scripts\activate`

    - On Unix or MacOS: `source venv/bin/activate`

7. Install dependency libraries: `pip install -r requirements.txt`

