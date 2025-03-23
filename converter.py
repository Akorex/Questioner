import pandas as pd

# Read JSON from file
json_filename = "nigerian_trivia_questions.json"  # Change this to your JSON file
csv_filename = "output.csv"

df = pd.read_json(json_filename)  # Load JSON file into DataFrame
df.to_csv(csv_filename, index=False)  # Convert to CSV

print(f"CSV file '{csv_filename}' has been created successfully.")