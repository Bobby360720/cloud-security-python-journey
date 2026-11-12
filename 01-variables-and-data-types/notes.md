### Common Error: NameError

A NameError occurs when Python cannot find the name of a variable or function.

Example:
*  print("Hello")

* An error i observed in Lab 1, I captizle the P in print, which casused a error 
Also when I ran python3 lab1_resource_inventory.py ininntal i was in the wrong relative path 

use an f-string when you want to put a variable’s value inside a message. The f tells Python to evaluate what’s inside {} and insert the result into the text.

resource_name = "stprod001"
severity = "High"
risk_score = 95
public_access = True

print(f"Resource Name: {resource_name}")
print(f"Severity: {severity}")
print(f"Risk Score: {risk_score}")
print(f"Public Access: {public_access}")