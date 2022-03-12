import re
data = input()
pattern = r"(\d{2}\/[A-Z][a-z]{2}\/\d{4}\b)|(\d{2}\.[A-Z][a-z]{2}\.\d{4}\b)|(\d{2}\-[A-Z][a-z]{2}\-\d{4}\b)"
matches = re.findall(pattern, data)
matches = [item for tup in matches for item in tup if item != ""]

for current_match in matches:
    if "/" in current_match:
        current_match = current_match.split("/")
        print(f"Day: {current_match[0]}, Month: {current_match[1]}, Year: {current_match[2]}")
    elif "-" in current_match:
        current_match = current_match.split("-")
        print(f"Day: {current_match[0]}, Month: {current_match[1]}, Year: {current_match[2]}")
    elif "." in current_match:
        current_match = current_match.split(".")
        print(f"Day: {current_match[0]}, Month: {current_match[1]}, Year: {current_match[2]}")

