#  Python Lists

A **list** is an ordered, mutable collection of items. Each item has a position, called an **index**. Lists can contain duplicate values, and you can change their contents after creating them. Use a plural name such as `motorcycles` or `storage_accounts` when it describes the collection clearly.

## Create a list and access its items

```python
motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles[0])   # honda
print(motorcycles[-1])  # suzuki
print(f"My first motorcycle was a {motorcycles[0].title()}.")
```

Python starts counting indexes at `0`. Negative indexes count backward from the end, so `-1` selects the last item.

## Change, add, and remove items

Each example assumes you start with `motorcycles = ["honda", "yamaha", "suzuki"]`.

| Goal | Python | Result |
|---|---|---|
| Replace the first item | `motorcycles[0] = "ducati"` | Replaces `"honda"` with `"ducati"` |
| Add an item to the end | `motorcycles.append("ducati")` | Adds `"ducati"` as the fourth item |
| Delete an item by index | `del motorcycles[1]` | Deletes `"yamaha"` |
| Remove and keep the last item | `popped_motorcycle = motorcycles.pop()` | Removes `"suzuki"` and stores it in `popped_motorcycle` |
| Remove and keep an item by index | `first_owned = motorcycles.pop(0)` | Removes `"honda"` and stores it in `first_owned` |
| Remove an item by value | `motorcycles.remove("yamaha")` | Removes the first occurrence of `"yamaha"` |

You can also store the value you want to remove in a variable, then use that variable in a message.

```python
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

removed_motorcycle = "ducati"
motorcycles.remove(removed_motorcycle)
print(f"I removed {removed_motorcycle.title()} from the list.")
```

## Sort, count, and loop through a list

```python
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.sort()               # Alphabetical order
motorcycles.sort(reverse=True)   # Reverse alphabetical order

print(f"Total motorcycles: {len(motorcycles)}")

for motorcycle in motorcycles:
    print(motorcycle.title())
```

`sort()` changes the order of the existing list. `len()` gives you the number of items. The loop runs its indented line once for each item, assigning the current item to `motorcycle` each time.


#  Python Lists

| Lab | Practice | Success check |
|---|---|---|
| 1. Create a list | Create `azure_regions` with three sample Azure regions. Print the list. | All three regions appear in the order you entered them. |
| 2. Access items | Print the first region with `[0]` and the last with `[-1]`. Use one of those expressions in an f-string. | The first and last regions are correct, and the f-string includes the expected region. |
| 3. Replace an item | Create a list of three VM names. Replace the second name by assigning a new value at index `1`. | The second name changes and the list still has three items. |
| 4. Append an item | Create a list of two storage account names. Add a third with `append()`. | The new name appears at the end. |
| 5. Delete by index | Create a list of three VM names. Use `del` to delete the second VM. | The first and third names remain in their original order. |
| 6. Remove and keep an item | Use `pop()` to remove the last VM from a fresh list and print the returned name. Reset the list and repeat with `pop(0)`. | Each run prints the removed name and shows that it’s gone from the list. |
| 7. Remove by value | Create a list of storage account names with one duplicate. Store the duplicate name in a variable, pass it to `remove()`, and print a message using that variable. | Only the first occurrence is removed, and the message names the account. |
| 8. Sort a list | Start with VM names in mixed order. Run `sort()` and print the list. Then run `sort(reverse=True)` and print it again. | You see alphabetical order followed by reverse alphabetical order. |
| 9. Count items | Create a list of regions. Print its count with `len()`, add a region, and print the count again. | The count increases by one without changing the reporting code. |
| 10. Loop through a list | Use a `for` loop to print the VM names under a **Virtual Machines** heading. | Each VM appears once on its own line. |

## Final challenge — Azure Inventory Report

After you finish the labs, start with a blank Python file. Complete the challenge without referring to the lesson or your lab code.

1. Create three separate lists for Azure regions, virtual machines, and storage accounts.
2. Print a labeled total for each list using `len()`.
3. Use a `for` loop for each list to display every item under the appropriate heading.
4. Add one VM to your sample data and rerun the report. Verify that the VM count increases by one and the new VM appears under **Virtual Machines**.

**Mark Day 2 complete** when all ten labs meet their success checks, the report passes all four requirements, and you can explain in your own words how `len()` counts resources and a `for` loop processes them one at a time.

**Cloud security connection.** This count-and-iterate pattern carries over to Azure inventory, RBAC reviews, and storage audits. In a later lab, the Azure SDK or an API can supply the resources you’re entering by hand today.