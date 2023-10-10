import pandas as pd
import random

# Create a DataFrame with character names and terrain
data = {'CharacterName': ['Arwen', 'Frodo', 'Gimli', 'Legolas'],
        'Terrain': ['Forest', 'Mountain', 'Swamp', 'Village']}
df = pd.DataFrame(data)

# Define a function to calculate stamina adjustment based on terrain
def calculate_stamina_adjustment(terrain):
    if terrain == 'Forest':
        return 10
    elif terrain == 'Mountain':
        return -20
    elif terrain == 'Swamp':
        return -30
    elif terrain == 'Village':
        return 15
    else:
        return 0  # Handle unknown terrains here

# Apply the function to calculate stamina adjustment
df['Stamina Adjustment'] = df['Terrain'].apply(calculate_stamina_adjustment)

# Add a random value to adjusted stamina
df['Stamina'] = 100  # Initial stamina for all characters
df['Stamina'] += df['Stamina Adjustment'] + [random.randint(-5, 5) for _ in range(len(df))]

# Display the DataFrame
print(df)
