# 1. Add our dependencies
import csv
import os

# 2. Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# 3. Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 4. Open the election results and read the file.
with open(file_to_load) as election_data:

# 5. Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # 6. Read and print the header row
    # next(file referencing object skips the first row) 
    headers = next(file_reader)
    print(headers)

#________________________________________________________