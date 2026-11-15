# Lab 7 Remove by value

## Create a list of storage account names with one duplicate. Store the duplicate name in a variable, pass it to remove(), and print a message using that variable.
app_storages = ["HRStorage", "LegalStorage","HRStorage","DBStorage"]
print(app_storages)


app_storages.remove('HRStorage')
print(app_storages)
