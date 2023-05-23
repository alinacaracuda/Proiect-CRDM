import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website
url = "http://www.sha1-online.com/"

# Define the letters of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Create an empty list to store the results
results = []

# Iterate over each letter
for letter in alphabet:
    # Send a POST request to the website with the current letter as the input
    response = requests.post(url, data={"text": letter})
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the result element in the HTML
    result_element = soup.find("input", {"name": "sha1"})
    
    # Extract the SHA1 hash value from the result element
    sha1_hash = result_element.get("value") if result_element else "N/A"
    
    # Append the letter and its corresponding SHA1 hash to the results list
    results.append({"Letter": letter, "SHA1 Hash": sha1_hash})

# Create a pandas DataFrame from the results list
df = pd.DataFrame(results)

# Save the DataFrame to an Excel file
df.to_excel("sha1_results.xlsx", index=False)