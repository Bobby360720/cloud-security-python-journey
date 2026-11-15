# Challenge — Azure Inventory Report

# 1. Three separate lists
fintech_regions = ["eastus", "westus", "central"]
fintech_vms = ["frontdoor", "api", "appservice", "private_endpoint", "database"]
fintech_storage = ["internal_storage", "public_storage"]

# 2. Labeled totals using len()
print("Total Azure Regions:", len(fintech_regions))
print("Total Virtual Machines:", len(fintech_vms))
print("Total Storage Accounts:", len(fintech_storage))

print("-" * 30)

# 3. Display every item under the appropriate heading
print("Azure Regions")
for region in fintech_regions:
    print("-", region)

print("\nVirtual Machines")
for vm in fintech_vms:
    print("-", vm)

print("\nStorage Accounts")
for storage in fintech_storage:
    print("-", storage)

# Add a VM and verify that both the count and the inventory update.
fintech_vms.append("fintech-ai-vm")

print("\nUpdated Virtual Machines")
print("Total Virtual Machines:", len(fintech_vms))

for vm in fintech_vms:
    print("-", vm)