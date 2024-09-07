''' ITERATION 5

Module: Banning Analytics

This module provides a simple, reusable foundation for my analytics projects. 

Process:
In this fifth iteration, I update the byline to show the min, max, mean and stdev of client_satisfaction_scores and employee_satisfaction_scores.
'''

#####################################
# Import modules at the top
#####################################

import statistics

#####################################
# Declare global variables
#####################################

has_international_clients: bool = True
has_hybrid_work_schedule: bool = True
years_in_operation: int = 10
company_size: int = 10000
skills_offered: list = ["Data Analytics", "Machine Learning", "Business Intelligence"]
office_locations: list = ["New York", "Chicago", "Los Angeles"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
employee_satisfaction_scores: list = [3.9, 4.2, 4.8, 3.0, 4.4]

#####################################
# Calculate basic statistics
#####################################

min_client_score: float = min(client_satisfaction_scores)
max_client_score: float = max(client_satisfaction_scores)
mean_client_score: float = statistics.mean(client_satisfaction_scores)
stdev_client_score: float = statistics.stdev(client_satisfaction_scores)

min_employee_score: float = min(employee_satisfaction_scores)
max_employee_score: float = max(employee_satisfaction_scores)
mean_employee_score: float = statistics.mean(employee_satisfaction_scores)
stdev_employee_score: float = statistics.stdev(employee_satisfaction_scores)

#####################################
# Declare a global variable named byline
# Make it a multiline f-string to show our information
#####################################

byline: str = f"""
-------------------------------------------------------
Banning Analytics: Delivering Professional Insights
-------------------------------------------------------
Has International Clients:                         {has_international_clients}
Has Hybrid Work Schedule:                          {has_hybrid_work_schedule}
Years in Opperation:                               {years_in_operation}
Company Size:                                      {company_size}
Skills Offered:                                    {skills_offered}
Office Locations:                                  {office_locations}
Client Satisfaction Scores:                        {client_satisfaction_scores}
Minimum Client Satisfaction Score:                 {min_client_score}
Maximum Client Satisfaction Score:                 {max_client_score}
Mean Client Satisfaction Score:                    {mean_client_score}
Standard Deviation of Client Satisfaction Score:   {stdev_client_score}
Employee Satisfaction Scores:                      {employee_satisfaction_scores}
Minimum Employee Satisfaction Score:               {min_employee_score}
Maximum Employee Satisfaction Score:               {max_employee_score}
Mean Employee Satisfaction Score:                  {mean_employee_score}
Standard Deviation of Employee Satisfaction Score: {stdev_employee_score}
"""

#####################################
# Define the get_byline() function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional execution
#####################################

if __name__ == '__main__':
    main()
