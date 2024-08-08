import os
import sys
import pathlib
import employee_attrition

PACKAGE_ROOT = pathlib.Path(employee_attrition.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, 'datasets')

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'


FEATURES_TO_DROP = ['Age', 'BusinessTravel', 'DailyRate', 'Department',
       'DistanceFromHome', 'EducationField', 'EmployeeCount',
       'EmployeeNumber', 'Gender', 'HourlyRate',
       'JobLevel', 'JobRole','MonthlyRate', 'NumCompaniesWorked',
       'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours',
        'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany','Education' ]

FEATURES_TO_MAP = ['MaritalStatus']
FEATURES_TO_LOG_TRANSFORM = ['MonthlyIncome','YearsInCurrentRole','YearsSinceLastPromotion','TotalWorkingYears']


MAPPINGS = {
            'MaritalStatus': {'Single':1, 'Married':2, 'Divorced':2},
            }


TARGET = 'Attrition'


MODEL_NAME = 'classification.pkl'
MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_model')

