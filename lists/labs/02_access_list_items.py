# lab 2: Access items

## Print the first region with [0] and the last with [-1]. Use one of those expressions in an f-string.

azure_regions = ["eastus", "westus", "centralus", "eastus2", "southcentralus"]
print(azure_regions) 

## Print the first region with [0]

azure_regions = ["eastus", "westus", "centralus", "eastus2", "southcentralus"]
print(azure_regions[0])

## Print the last region with [-1]

azure_regions = ["eastus", "westus", "centralus", "eastus2", "southcentralus"]
print(azure_regions[-1])

print(f"Which region needs remediation {azure_regions[2].title()}.") 