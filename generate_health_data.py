import pandas as pd
import numpy as np
import random
import datetime

# Function to generate health records

def generate_health_data(num_records):
    data = []
    locations = ['Soledad, Colombia']
    genders = ['Male', 'Female']

    for _ in range(num_records):
        record = {
            'record_id': len(data) + 1,
            'location': random.choice(locations),
            'age': random.randint(18, 80),
            'gender': random.choice(genders),
            'systolic_bp': random.randint(110, 180),  # Systolic Blood Pressure
            'diastolic_bp': random.randint(70, 120),  # Diastolic Blood Pressure
            'cholesterol': random.randint(150, 300),  # Cholesterol levels
            'weight': random.uniform(50.0, 150.0),   # Weight in kg
            'height': random.uniform(1.5, 2.0),      # Height in meters
            'smoking': random.choice(['Yes', 'No']),
            'alcohol_consumption': random.choice(['Yes', 'No']),
            'physical_activity': random.choice(['Low', 'Moderate', 'High']),
            'date_created': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(record)

    return pd.DataFrame(data)

# Generate data
if __name__ == '__main__':
    df = generate_health_data(2000)
    df.to_csv('health_data_soledad_colombia.csv', index=False)  # Save to CSV
