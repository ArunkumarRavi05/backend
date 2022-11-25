# Validate phone number
import re

validate_phone_number_pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
if re.match(validate_phone_number_pattern, "+1 212.456.7890"): # Returns Match object
    print("Valid Number")
else:
    print("Invalid Number")