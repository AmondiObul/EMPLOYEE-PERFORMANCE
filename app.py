import streamlit as st
import numpy as np
import joblib

@st.cache_resource

def load_model():
    model = joblib.load('RF_MODEL.pkl')
    return model

st.cache_resource.clear()

st.title('EMPLOYEE PERFORMANCE APP')
st.subheader('This app categorizes an employees performance depending on their input features')

model=load_model()

if model:
    st.header('Please enter your details')

Age=st.number_input('Age',value=0)

Gender_encoded=st.selectbox('Gender',options=[(0,'Female'),(1,'Male')],format_func=lambda x: x[1])
Gender_encoded_values=Gender_encoded[0]

EmpJobRole_encoded=st.selectbox('Job Role', options=[(0,'Sales Executive'),(1,'Manager'),(2,'Developer'),(3,'Sales Representative'),(4,'Human Resources'),(5,'Senior Developer'),(6,'Data Scientist'),(7,'Senior Manager R&D'),(8,'Laboratory Technician'),(9,'Manufacturing Director'),(10,'Research Scientist'),(11,'Healthcare Representative'),(12,'Research Director'),(13,'Manager R&D'),(14,'Finance Manager'),(15,'Technical Architect'),(16,'Business Analyst'),(17,'Technical Lead'),(18,'Delivery Manager')],format_func=lambda x: x[1])
EmpJobRole_encoded_values=EmpJobRole_encoded[0]

EmpEducationLevel=st.selectbox ('EmpEducationalLevel',options=[(1,'Below College'),(2,'College'),(3,'Bachelor'),(4,'Master'),(5,'Doctor')], format_func=lambda x: x[1])
EmpEducationLevel_values=EmpEducationLevel[0]

EmpEnvironmentSatisfaction=st.selectbox('Job Environment Satisfaction Level',options=[(1,'Low'),(2,'Medium'),(3,'High'),(4,'Very High')], format_func=lambda x: x[1])
EmpEnvironmentSatisfaction_values=EmpEnvironmentSatisfaction[0]

EmpJobSatisfaction=st.selectbox('Job Satisfaction Level',options=[(1,'Low'),(2,'Medium'),(3,'High'),(4,'Very High')], format_func=lambda x: x[1])
EmpJobSatisfaction_values=[0]

NumCompaniesWorked=st.number_input('Number of Companies Worked',value=0)

EmpLastSalaryHikePercent=st.number_input('Last Salary Hike Percentage',value=0)

ExperienceYearsAtThisCompany=st.number_input('Number of years at INX Future Inc',value=0)

ExperienceYearsInCurrentRole=st.number_input('Number of years In current role',value=0)

YearsSinceLastPromotion=st.number_input('Number of years since last Promotion',value=0)

YearsWithCurrManager=st.number_input('Number of years working with current manager',value=0)

TotalWorkExperienceInYears=st.number_input('TotalWorkExperienceInYears',value=0)

TrainingTimesLastYear=st.number_input('TrainingTimesLastYear',value=0)

EmpHourlyRate=st.number_input('EmpHourlyRate',value=0)

EmpWorkLifeBalance=st.selectbox('Work Life Balance', options=[(2,'Good'),(3,'Better'),(4,'Best')], format_func=lambda x: x[1])
EmpWorkLifeBalance_values=EmpWorkLifeBalance[0]

input_data = np.array([
    float(Age), float(Gender_encoded_values), float(EmpJobRole_encoded_values),
    float(EmpEducationLevel_values), float(EmpEnvironmentSatisfaction_values[0]) if isinstance(EmpEnvironmentSatisfaction_values, list) else float(EmpEnvironmentSatisfaction_values),
    float(EmpJobSatisfaction_values[0]) if isinstance(EmpJobSatisfaction_values, list) else float(EmpJobSatisfaction_values),
    float(NumCompaniesWorked), float(EmpLastSalaryHikePercent), float(ExperienceYearsAtThisCompany),
    float(ExperienceYearsInCurrentRole), float(YearsSinceLastPromotion), float(YearsWithCurrManager),
    float(TotalWorkExperienceInYears), float(TrainingTimesLastYear), float(EmpHourlyRate), 
    float(EmpWorkLifeBalance_values)
])

if st.button('🔍 Predict Performance'):
    prediction = model.predict(input_data.reshape(1, -1))  

    # Mapping the model output to performance categories
    category_mapping = {
        1: 'Low Performance',
        2: 'Good Performance',
        3: 'Excellect Performance',
        4: 'Outstanding Performance'
    }

    performance_prediction = category_mapping.get(prediction[0], 'Unknown Category')  # Handles unexpected values

    st.subheader(f'Predicted Performance: {performance_prediction}')


st.write('Employee performance is key for organisation growth')