#import streamlit as st
#import requests

#print("Both libraries are installed and working!")
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
