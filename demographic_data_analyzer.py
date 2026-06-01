import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # Replace None values below with your solutions

    race_count = None
    average_age_men = None
    percentage_bachelors = None
    higher_education_rich = None
    lower_education_rich = None
    min_work_hours = None
    rich_percentage = None
    highest_earning_country = None
    highest_earning_country_percentage = None
    top_IN_occupation = None

    if print_data:
        print("Race count:\n", race_count)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }