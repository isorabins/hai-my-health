input_file_path = '/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/compiled_conditions.csv'
output_file_path = '/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/converted.csv'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        condition, description = line.strip().split(',', 1)  # Split on the first comma only
        outfile.write(f'"{condition}","{description}"\n')  # Enclose fields in quotes and write


