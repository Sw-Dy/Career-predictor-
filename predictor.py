import pickle
import numpy as np

# Load the saved machine learning model
with open('career_path_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define label encoders for categorical data
label_encoders = {
    'remote': ['Remote', 'In office'],
    'motivation_level': ['Low', 'Medium', 'High'],
    'work_life_balance': ['Unbalanced', 'Balanced'],
    'work_environment': ['Competitive', 'Collaborative and supportive', 'Independent'],
    'preferred_location': ['Urban', 'Rural', 'Suburban'],
    'travel_willingness': ['Low', 'Medium', 'High'],
    'career_growth': ['Low', 'Medium', 'High'],
    'work_hours_flexibility': ['Not important', 'Important'],
    'company_size_preference': ['Startups', 'MNCs', 'Medium-sized enterprises'],
    'preferred_industry': ['Technology', 'Education', 'Finance', 'Healthcare', 'Other'],
    'team_structure': ['Individual contributor', 'Small teams', 'Large teams'],
    'job_stability': ['Low', 'High'],
    'training_opportunities': ['Not important', 'Important'],
    'ethical_values': ['Neutral', 'Align with personal values', 'Not a priority'],
    'preferred_work_style': ['Structured', 'Unstructured', 'Hybrid'],
    'communication_style': ['Formal', 'Informal', 'Mixed'],
}

# Define a mapping from numerical predictions to career path names
career_path_mapping = {
    0: "Data Scientist",
    1: "Management Consultant",
    2: "Marketing Management",
    3: "Machine Learning Engineer",
    4: "Artificial Intelligence Specialist",
    5: "Engineering Management",
    6: "Blockchain Developer",
    7: "Investment Banker",
    8: "Product Management",
    9: "Software Architect",
    10: "Doctor",
    11: "Cybersecurity Specialist",
    12: "Finance Professional",
    13: "Business Analyst",
    14: "Data Engineer",
    15: "DevOps Engineer",
    16: "Systems Manager",
    17: "Lawyer",
    18: "Human Resources Specialist",
    19: "Chartered Accountant"
}

def encode_features(input_data):
    # Convert categorical features into numerical
    for i, (key, categories) in enumerate(label_encoders.items()):
        input_data[i + 6] = categories.index(input_data[i + 6])  # Start at index 6 for categorical data
    return np.array([input_data])

def predict_career(data):
    data = encode_features(data)
    prediction = model.predict(data)
    
    # Convert the numerical prediction to the corresponding career path name
    career_path = career_path_mapping.get(prediction[0], "Unknown Career Path")
    
    return career_path
