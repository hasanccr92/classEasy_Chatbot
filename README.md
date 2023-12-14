<heading>Short Documentation<heading>

1. Git clone this repo and in a terminal, do- "pip install -r requirements.txt"
2. Delete the vectordb.pkl file. Also delete the pdf file and follow step 6.
3. Go to platform.openai.com and sign up/login.
4. Obtain the API key from the pop-up menu on the left.
5. Open the whole repo in an IDE, open the inference.py file and enter your API key. 
6. The data on which you want to train is the 'merged.pdf'. Put your own PDF here and change the name in vecDBmaker.py. Or you can just rename the pdf file.
7. Run vecDBmaker.py. It will create a vector database in .pkl format.
8. Open a terminal from inside the folder and do- "streamlit run inference.py"
9. If any dependency issue occurs, pip install that one.
10. For any queries or improvements, please contact!
