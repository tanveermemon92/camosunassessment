# data_setup.py
import pandas as pd

def load_camosun_program_enrollment():
    data = {
        "Program Area": [
            "Arts and Sciences",
            "Business and Management",
            "Developmental",
            "Education",
            "Engineering and Applied Sciences",
            "Health",
            "Human and Social Services",
            "Personal Improvement and Leisure",
            "Visual and Performing Arts",
        ],
        "2020-21": [6160, 770, 30, 1415, 155, 75, 215, 840, 955],
        "2021-22": [6485, 955, 80, 1465, 150, 90, 45, 935, 1035],
        "2022-23": [7590, 1400, 450, 1365, 135, 130, 50, 1030, 1140],
        "2023-24": [7895, 1475, 370, 1370, 140, 85, 85, 1265, 1210],
    }
    return pd.DataFrame(data)

def load_sector_comparison():
    data = {
        "Institution": [
            "BC Colleges Average",
            "Kwantlen Polytechnic",
            "Langara College",
            "UVic",
            "UBC",
            "SFU",
            "National Average",
        ],
        "International Decline %": [-55, -60, -50, -40, -28, -32, -27],
        "Healthcare Program Growth %": [20, 25, 22, 8, 6, 7, 10],
    }
    return pd.DataFrame(data)
