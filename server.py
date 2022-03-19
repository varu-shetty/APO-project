{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ba4e570",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from flask import Flask, request\n",
    "import numpy as np\n",
    "import pickle\n",
    "import pandas as pd\n",
    "import flasgger\n",
    "from flasgger import Swagger\n",
    "\n",
    "app=Flask(__name__)\n",
    "Swagger(app)\n",
    "\n",
    "pickle_in = open(\"classifier.pkl\",\"rb\")\n",
    "classifier=pickle.load(pickle_in)\n",
    "\n",
    "@app.route('/')\n",
    "def welcome():\n",
    "    return \"Welcome All\"\n",
    "\n",
    "@app.route('/predict',methods=[\"Get\"])\n",
    "def predict_note_authentication():\n",
    "    Class=request.args.get(\"Class\")\n",
    "    prediction=classifier.predict([[Class]])\n",
    "    print(prediction)\n",
    "    return \"Hello The answer is\"+str(prediction)\n",
    "\n",
    "@app.route('/predict_file',methods=[\"POST\"])\n",
    "def predict_note_file():\n",
    "    \"\"\"Let's Authenticate the Banks Note \n",
    "    This is using docstrings for specifications.\n",
    "    ---\n",
    "    parameters:\n",
    "      - name: file\n",
    "        in: formData\n",
    "        type: file\n",
    "        required: true\n",
    "      \n",
    "    responses:\n",
    "        200:\n",
    "            description: The output values\n",
    "        \n",
    "    \"\"\"\n",
    "    df_test=pd.read_csv(request.files.get(\"file\"))\n",
    "    print(df_test.head())\n",
    "    prediction=classifier.predict(df_test)\n",
    "    \n",
    "    return str(list(prediction))\n",
    "\n",
    "if __name__=='__main__':\n",
    "    app.run(host='0.0.0.0',port=8000)\n",
    "    \n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
