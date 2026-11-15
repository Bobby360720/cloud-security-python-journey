# Lab 6  Remove and keep an item

## Use pop() to remove the last VM from a fresh list and print the returned name. Reset the list and repeat with pop(0).
vms = ["app_vm", "db_vm","fw_vm","waf_vm"]
print(vms)

removed_vm = vms.pop()
print(removed_vm)

removed_vm1 = vms.pop(0)
print(removed_vm1)

