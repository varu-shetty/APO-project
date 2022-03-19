{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bad4bafd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "url = 'http://localhost:5000/results'\n",
    "r = requests.post(url,json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400})\n",
    "\n",
    "print(r.json())"
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
