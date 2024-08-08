from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from src.employee_attrition.predict import generate_predictions


app = FastAPI(
    title='employee attrition prediction using API',
    description = 'A simple CI CD Demo',
    version  = '1.0'
)

origins=[
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class EmployeeAttrition(BaseModel):
    Age: int
    BusinessTravel: str
    DailyRate: int
    Department: str
    DistanceFromHome: int
    Education: int
    EducationField: str
    EmployeeCount: int
    EmployeeNumber: int
    EnvironmentSatisfaction: int
    Gender: str
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: str
    JobSatisfaction: int
    MaritalStatus: str
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    Over18: str
    OverTime: str
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StandardHours: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int


@app.get('/')
def index():
    return {'message': 'welcome to loan prediction app using API - CI CD Jenkins'}

@app.post('/prediction_api')
def predict(attrition_detail: EmployeeAttrition):
    data = attrition_detail.model_dump()
    print(data)
    prediction = generate_predictions(data)['prediction'][0]
    if prediction==0:
        pred = 'No Attrition'
    
    else:
        pred = 'Attrition'
    
    return {'status': pred}

@app.post('/prediction_ui')
def predict_gui(
    Age: int,
    BusinessTravel: str,
    DailyRate: int,
    Department: str,
    DistanceFromHome: int,
    Education: int,
    EducationField: str,
    EmployeeCount: int,
    EmployeeNumber: int,
    EnvironmentSatisfaction: int,
    Gender: str,
    HourlyRate: int,
    JobInvolvement: int,
    JobLevel: int,
    JobRole: str,
    JobSatisfaction: int,
    MaritalStatus: str,
    MonthlyIncome: int,
    MonthlyRate: int,
    NumCompaniesWorked: int,
    Over18: str,
    OverTime: str,
    PercentSalaryHike: int,
    PerformanceRating: int,
    RelationshipSatisfaction: int,
    StandardHours: int,
    StockOptionLevel: int,
    TotalWorkingYears: int,
    TrainingTimesLastYear: int,
    WorkLifeBalance: int,
    YearsAtCompany: int,
    YearsInCurrentRole: int,
    YearsSinceLastPromotion: int,
    YearsWithCurrManager: int,
):
    input_data = [Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
                   NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]

    cols = ['Age', 'BusinessTravel', 'DailyRate', 'Department',
       'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',
       'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
       'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
       'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
       'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager']

    data_dict = dict(zip(cols,input_data))
    prediction = generate_predictions([data_dict])['predictions'][0]
    if prediction == 0:
        pred = 'No Attrition'
    
    else:
        pred = 'Attrition'
    
    return {'status':pred}

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8005)

