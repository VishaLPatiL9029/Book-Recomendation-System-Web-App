from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import logging

# Configure the logging settings

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)




if __name__ == "__main__":
    app.run(host = "0.0.0.0")