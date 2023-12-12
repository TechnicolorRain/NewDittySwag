import os

# List of files to be merged
files = ['post_launch_strategy.md', 'information_gap_analysis.md', 'human_intervention_tasks.md', 'business_plan_management.md']

# Create a new file and write the contents of the other files into it
with open('comprehensive_document.md', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write('\n')