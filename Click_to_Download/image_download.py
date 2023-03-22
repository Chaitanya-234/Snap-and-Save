from flask import Flask, render_template, request, jsonify, redirect
import cv2
import numpy as np
import requests
import urllib.request
from io import BytesIO
from PIL import Image
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import urllib.request
import os 
from PIL import Image

API_KEY = "AIzaSyByQd2lFQt_cUbNv7dihFZW9zVRzISrCeE"
SEARCH_ENGINE_ID = "66bdb8ac7adc3412e"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('downsearch') == 'Download':
            query = request.form.get("search")
            url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&searchType=image&q={query}"
            response = requests.get(url)
            data = response.json()
            # Extract the URL of the first image in the search results
            image_url = data["items"][0]["link"]
            # Display the image using a Python library like PIL or OpenCV
            # Retrieve the image data from the URL and open it with PIL
            image_data = urllib.request.urlopen(image_url).read()
            image = Image.open(BytesIO(image_data))
            file = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
            if file:
                abs_path = os.path.abspath(file.name)
                image.save(abs_path)
        else:
            return '<h1>wrong</h1>'

    return render_template('index.html')