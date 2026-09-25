def check_package_id(package_id):

    """
    Function to evaluate package ID status.
    Returns:
    -    "low" for low-priority
         "high" for high-risk
         "processed" for valid ID packages
         "invalid" for invalid ID packages (0 or negative)
    """
    if package_id <= 0:
        return "invalid"
    elif package_id < 100:
        return "low"
    elif package_id > 1000:
        return "high"
    else:
        return "processed"
#Original queue of incoming package IDs
package_queue = [984, 1520, 2983, 0, 9912, 4871, 102, 3100]

#Create a shallow copy of the original queue to process
copy_queue = package_queue[:]
processed_packages = []

#Process package IDs
for package in package_queue:
    status = check_package_id(package)
    if status == "invalid":
        print(f"Package ID {package} is invalid. Skipping...")
        continue
    elif status == "low":
        print(f"Package ID {package} is low priority. Skipping...")
        continue
    elif status == "high":
        print(f"Package ID {package} is high risk. Alerting security...")
        break
    else:
        print(f"Package ID {package} is valid. Processing...")
        processed_packages.append(package)

    print("\nFinal Processed Packages:\n")
    print(processed_packages)

    print("\nOriginal Queue (before change):\n")
    print(package_queue)

    # Modify the original queue to demonstrate shallow copy behavior
    package_queue[1] = 8888

    print("\nModified Original Queue:\n")
    print(package_queue)

    print("\nCopy Queue (should not change):\n")
    print(copy_queue)






