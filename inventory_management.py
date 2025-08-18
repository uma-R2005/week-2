def input_inventories():
    inventories = {}
    n = int(input("How many store branches? "))
    for i in range(1, n + 1):
        print(f"\nEnter items for Branch {i} (comma-separated):")
        items = input().strip().lower().split(",")
        items = {item.strip() for item in items if item.strip()}
        inventories[f"Branch {i}"] = items
    return inventories

def all_items(inventories):
    result = set()
    for items in inventories.values():
        result |= items
    return result

def common_items(inventories):
    all_sets = list(inventories.values())
    if not all_sets:
        return set()
    common = all_sets[0]
    for s in all_sets[1:]:
        common &= s
    return common

def unique_items_per_branch(inventories):
    unique = {}
    for branch, items in inventories.items():
        others = set()
        for b, itms in inventories.items():
            if b != branch:
                others |= itms
        unique[branch] = items - others
    return unique

def main():
    inventories = input_inventories()

    print("\nAll items across branches:")
    print(sorted(all_items(inventories)))

    print("\nItems common to all branches:")
    common = common_items(inventories)
    print(sorted(common) if common else "None")

    print("\nUnique items per branch:")
    unique = unique_items_per_branch(inventories)
    for branch, items in unique.items():
        print(f"{branch}: {sorted(items) if items else 'None'}")

if __name__ == "__main__":
    main()
