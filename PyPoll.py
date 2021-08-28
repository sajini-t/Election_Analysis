# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

#-----------------------------------------------------------
# Initialize and decalre all variables and list before opening the data file
# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Initialize County Name List
county_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Declare dictionary to hold County as key and votes cast per county as value
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County with largest turnout and its number of votes
county_name_largest = ""
county_count_largest = 0
county_largest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row
    # next(file referencing object skips the first row) 
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Get the county name for each row.
        county_name = row[1]
        # If the county name does not match any existing county...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
   #-----------------------------------------------------------
  
  
  # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n"
        f"\nCounty Votes:")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
   #-----------------------------------------------------------
                
        #Loop through county_votes dictionary to get county name, votes & calculate vote%        
        for county_name in county_votes:
            # Get county name(key) from the county_votes dictionary
            c_name = county_name
            # Get county votes(value) from the county_votes dictionary
            c_votes = county_votes[county_name]
            # Calculate county vote percentage for current county in county_votes dictionary
            c_vote_percentage = float(c_votes) / float(total_votes) * 100
            county_results = (f"\n{c_name}: {c_vote_percentage:.1f}% ({c_votes:,})")
            
            print(f"{county_results}")
            # Save county name, vote and percentage to text file
            txt_file.write(county_results)
   #-----------------------------------------------------------


            # Determine largest vote count and county
            # Determine if the votes is greater than the largest vote count.
            if(c_votes > county_count_largest) and (c_vote_percentage > county_largest_percentage):
                # If true then set county_count_count = c_votes and county_largest_percentage = c_vote_percentage.
                county_count_largest = c_votes
                county_largest_percentage = c_vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                county_name_largest = c_name

        #Largest county summary
        largest_county_summary = (
            f"\n\n-----------------------\n"
            f"Largest County Turnout: {county_name_largest}\n"
            f"-----------------------\n"
        )
        print(largest_county_summary)
        # Save county of largest turnout to text file
        txt_file.write(largest_county_summary)
        #------------------------------------------------------
        
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100                      
            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)
            #------------------------------------------------------
                        
            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percentage = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)







#________________________________________________________# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

#-----------------------------------------------------------
# Initialize and decalre all variables and list before opening the data file
# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Initialize County Name List
county_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Declare dictionary to hold County as key and votes cast per county as value
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County with largest turnout and its number of votes
county_name_largest = ""
county_count_largest = 0
county_largest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row
    # next(file referencing object skips the first row) 
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Get the county name for each row.
        county_name = row[1]
        # If the county name does not match any existing county...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
   #-----------------------------------------------------------
  
  
  # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n"
        f"\nCounty Votes:")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
   #-----------------------------------------------------------
                
        #Loop through county_votes dictionary to get county name, votes & calculate vote%        
        for county_name in county_votes:
            # Get county name(key) from the county_votes dictionary
            c_name = county_name
            # Get county votes(value) from the county_votes dictionary
            c_votes = county_votes[county_name]
            # Calculate county vote percentage for current county in county_votes dictionary
            c_vote_percentage = float(c_votes) / float(total_votes) * 100
            county_results = (f"\n{c_name}: {c_vote_percentage:.1f}% ({c_votes:,})")
            
            print(f"{county_results}")
            # Save county name, vote and percentage to text file
            txt_file.write(county_results)
   #-----------------------------------------------------------


            # Determine largest vote count and county
            # Determine if the votes is greater than the largest vote count.
            if(c_votes > county_count_largest) and (c_vote_percentage > county_largest_percentage):
                # If true then set county_count_count = c_votes and county_largest_percentage = c_vote_percentage.
                county_count_largest = c_votes
                county_largest_percentage = c_vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                county_name_largest = c_name

        #Largest county summary
        largest_county_summary = (
            f"\n\n-----------------------\n"
            f"Largest County Turnout: {county_name_largest}\n"
            f"-----------------------\n"
        )
        print(largest_county_summary)
        # Save county of largest turnout to text file
        txt_file.write(largest_county_summary)
        #------------------------------------------------------
        
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100                      
            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)
            #------------------------------------------------------
                        
            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percentage = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)







#________________________________________________________