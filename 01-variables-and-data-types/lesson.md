A variable is a placeholder used to store data in a program. Variables make code more reusable, easier to read, and easier to maintain because values can be stored in one location and referenced throughout the program.

Variable Naming Rules

Variables can contain:

Letters (a-z, A-Z)
Numbers (0-9)
Underscores (_)

Variables cannot:

Start with a number
Contain spaces
Use special characters such as @, #, %, or !
Valid Variable Names
storage_account = "PythonStorage"
account_id = "1234"
resourceGroup = "rg-prod"

Invalid Variable Names
1storage_account = "PythonStorage"
storage account = "PythonStorage"
storage-account = "PythonStorage"

Tips
Use descriptive variable names that clearly explain what the data represents.
Avoid using Python keywords as variable names.
Read error messages carefully. Tracebacks help identify where an error occurred in your code.
Bad Example
x = "Production"

Better Example
subscription_name = "Production"

Common Errors
Misspelling Variable Names
storage_account = "PythonStorage"

print(storage_acount)


Output:

NameError: name 'storage_acount' is not defined


The variable was created as:

storage_account


but referenced as:

storage_acount


Notice the missing "c".

Examples
storage_account = "PythonStorage"
account_id = "1234"

print(storage_account)
print(account_id)

Data Types
Strings

Strings are a sequence of characters enclosed in quotation marks.

Examples:

name = "John"
subscription = "Production"
message = "Learning Python variables is fun!"


Strings can contain:

Letters
Numbers
Symbols
Spaces

Example:

description = "Azure Storage Account"

Integers

Integers are whole numbers without decimal places.

Examples:

vm_count = 25
failed_logins = 12
risk_score = 100

Floats

Floats are numbers that contain decimal places.

Examples:

cpu_usage = 75.5
storage_size = 10.25

Booleans

Booleans represent one of two values:

True
False


Examples:

mfa_enabled = True
public_access = False
encrypted = True

Architect Feedback

One thing I'd add because you're targeting Cloud Security Architecture:

## Real-World Cloud Security Examples

| Variable | Purpose |
|-----------|----------|
| subscription_name | Azure subscription |
| resource_group | Resource group name |
| public_access | Storage account exposure |
| mfa_enabled | MFA status |
| risk_score | Calculated security risk |


