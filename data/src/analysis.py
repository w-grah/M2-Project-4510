import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv('data/survey_2024.csv', skiprows=[1])

# Mapping course IDs to names
mapping = {
    'Q35_1': 'Professionalism & Leadership',
    'Q35_5': 'Data Analytics',
    'Q35_2': 'Adv Tax Business Entities',
    'Q35_4': 'Financial Auditing',
    'Q35_3': 'Professional Ethics',
    'Q35_8': 'Business Law',
    'Q35_9': 'Accounting Research',
    'Q35_10': 'Adv Management Accounting'
}

# Clean and Calculate
rank_columns = list(mapping.keys())
subset = df[rank_columns].rename(columns=mapping)
subset = subset.apply(pd.to_numeric, errors='coerce')
rankings = subset.mean().sort_values()

# Create the Figure
plt.figure(figsize=(10, 6))
rankings.plot(kind='barh', color='#154734') 
plt.gca().invert_yaxis()
plt.title('2024 MAcc Course Rankings (Lower Score = Higher Preference)')
plt.xlabel('Average Rank (1 is Best)')
plt.tight_layout()

# Save output
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/rank_order.png')
