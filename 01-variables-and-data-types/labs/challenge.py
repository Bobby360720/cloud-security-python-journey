print("=== Cloud Security Report ===")

subscription_name = "dev"
resource_group = "day1_challenge"
storage_account_name = "pythonstorage"
region = "centralus"
public_access = False
encryption_status = True
risk_score = 50 


print(f"Subscription Name: {subscription_name}")
print(f"Resource Group: {resource_group}")
print(f"Storage Account : {storage_account_name}") 
print(region)
print(f" Public Access : {public_access}")
print(f" Encryption Status : {encryption_status}")
print(f"Risk Score : {risk_score}")


