import hashlib
import pandas as pd

alphabet = "abcdefghijklmnopqrstuvwxyz"

results = []

for letter in alphabet:
    sha1_hash = hashlib.sha1(letter.encode()).hexdigest()

    results.append([letter, sha1_hash])

df = pd.DataFrame(results, columns=["Letter", "SHA1 Hash"])

df.to_excel("sha1_results1.xlsx", index=False)