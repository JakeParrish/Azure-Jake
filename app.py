
from flask import Flask, render_template, request
from dash import dcc, html, Input, Output, callback
from flask_sqlalchemy import SQLAlchemy as SQL
from datetime import datetime
import pyodbc as odbc
import pandas as pd

app = Flask(__name__)

cnn_azure = (
    r"Driver={SQL Server};Server=pip-it-sharepoint-prod-eastus;"
)
#app.config['SQLALCHEMY_DATABASE_URI'] = "pip-it-sharepoint-prod-eastus"

# DRIVER_NAME = 'SQL SERVER'
# SERVER_NAME = 'pip-it-sharepoint-prod-eastus'
# DATABASE_NAME = 'dbo.Employees & Emails'

# connection_string = f"""
#     DRIVER = {{{DRIVER_NAME}}};
#     SERVER = {SERVER_NAME};
#     DATABASE = {DATABASE_NAME};
#     Trust_Connection=yes;
#     uid = 'pkoza'
#     pwd = 'xAgLBmu#7bSeeYt' 

# """
#Initialize

@app.route("/")
def main():
    # conn = odbc.connection(connection_string)
    # print(conn)
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form():
    Employee_Name = request.form.get("Employee-Name")
    Employer_Name = request.form.get("Employer-Name")
    Work_Order_Lead = request.form.get("Work-Order-Lead")
    Company_Supervisor = request.form.get("Company-Supervisor")
    Work_Order_Manager = request.form.get("Work-Order-Manager")
    Purpose_For_Request = request.form.get("Purpose-For-Request")
    Training_Title = request.form.get("Training-Title")
    Training_Start_Date = request.form.get("Training-Start-Date")
    Training_End_Date = request.form.get("Training-End-Date")
    Certification = request.form.get("Certification")
    Travel_City = request.form.get("Travel-City")
    Travel_State = request.form.get("Travel-State")
    Travel_Start_Date = request.form.get("Travel-Start-Date")
    Travel_End_Date = request.form.get("Travel-End-Date")
    Training_Cost = request.form.get("Training-Cost")
    MIE_Rate_75 = request.form.get("75-MIE-Rate")
    MIE_Rate = request.form.get("MIE-Rate")
    Lodging_Rate = request.form.get("Lodging-Rate")
    Est_Per_Diem = request.form.get("Est_Per_Diem")
    Est_Lodge_Tax_Fees = request.form.get("Est-Lodge-Tax-Fees")
    Round_Mileage_Cost = request.form.get("Round-Mileage-Cost")
    Est_Ground_Trans_Fees = request.form.get("Est-Ground-Trans-Fees")
    Est_Airfair_Price = request.form.get("Est-Airfair_Price")
    Baggage_Fees = request.form.get("Baggage_Fees")
    Est_Car_Rental_Price = request.form.get("Est-Car-Rental-Price")
    Est_Fuel_Cost = request.form.get("Est-Fuel-Cost")
    Other_Cost = request.form.get("Other_Cost")
    return render_template("form.html", Employee_Name=Employee_Name, Employer_Name=Employer_Name, Work_Order_Lead=Work_Order_Lead, Company_Supervisor=Company_Supervisor, Work_Order_Manager=Work_Order_Manager, Purpose_For_Request=Purpose_For_Request, Training_Title=Training_Title, Training_Start_Date=Training_Start_Date, Training_End_Date= Training_End_Date, Certification=Certification, Travel_City=Travel_City, Travel_State=Travel_State, Travel_Start_Date=Travel_Start_Date, Travel_End_Date=Travel_End_Date, Training_Cost=Training_Cost, MIE_Rate_75=MIE_Rate_75, MIE_Rate=MIE_Rate, Lodging_Rate=Lodging_Rate, Est_Per_Diem=Est_Per_Diem, Est_Lodge_Tax_Fees=Est_Lodge_Tax_Fees, Round_Mileage_Cost=Round_Mileage_Cost, Est_Ground_Trans_Fees=Est_Ground_Trans_Fees, Est_Airfair_Price=Est_Airfair_Price, Baggage_Fees=Baggage_Fees, Est_Car_Rental_Price=Est_Car_Rental_Price, Est_Fuel_Cost=Est_Fuel_Cost, Other_Cost=Other_Cost)
