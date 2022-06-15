from flask import Flask, render_template, request
from dash import dcc, html, Input, Output, callback


app = Flask(__name__)


@app.route("/")
def main():
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
    return render_template("form.html", name=Employee_Name)
