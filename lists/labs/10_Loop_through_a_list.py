# Lab 10 Loop through a list

## Use a for loop to print the VM names under a Virtual Machines heading.

vms = ['app_vm', 'bd_vm', 'mcp_vm']

# Print the heading once before the loop begins
print("Virtual Manchines")

# Loop through the list and print each VM on its own line
for vm in vms:
    print(vm)