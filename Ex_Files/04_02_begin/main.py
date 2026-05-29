from flask import Flask
import csv
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def Hello():
  return ("Hello, World!")

@app.route("/csv")
def csv_run():
  with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

  return laureates

@app.route("/csv_albert")
def csv_runner():
  albert = [] 
  with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)
  
  for laureate in laureates:
    if laureate["surname"] == "Einstein":
        albert.append(laureate)
        break

  return albert

app.run(debug=True)