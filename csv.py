import csv

input_file_path = '/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/condition_from_GPT.txt '
output_csv_file_path = '/Users/isorabins/Desktop/health.csv'

with open(input_file_path, 'r') as input_file, open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Condition", "Description"])  # CSV header
    
    current_condition = None
    current_description = []
    
    for line in input_file:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        # Check if the line contains a new condition
        if ":" in line:  # Assuming every new condition contains a colon
            if current_condition:  # Write the previous condition and description to the CSV
                writer.writerow([current_condition, " ".join(current_description)])
                
            current_condition, description_part = line.split(":", 1)
            current_condition = current_condition.strip()
            current_description = [description_part.strip()]
        else:
            # Continuation of the description
            current_description.append(line.strip())
    
    # Don't forget to write the last condition and description to the CSV
    if current_condition and current_description:
        writer.writerow([current_condition, " ".join(current_description)])

print(f"CSV file created at: {output_csv_file_path}")
