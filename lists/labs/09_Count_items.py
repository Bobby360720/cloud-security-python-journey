
# Lab 9 Count items
## Create a list of regions. Print its count with len(), add a region, and print the count again.

azure_regions = ["eastus", "westus", "centralus", "eastus2", "southcentralus"]
print("inital count:", len(azure_regions))

azure_regions.append("westus2")

print("updated count:", len(azure_regions))