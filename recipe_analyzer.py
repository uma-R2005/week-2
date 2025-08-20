def process_recipes(input_file, output_file, ingredient_to_count):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        total_recipes = 0
        matching_recipes = 0
        matching_names = []

        for line in lines:
            total_recipes += 1
            name, ingredients_str = line.strip().split("|")
            ingredients = ingredients_str.split(",")
            if ingredient_to_count.lower() in (ing.lower() for ing in ingredients):
                matching_recipes += 1
                matching_names.append(name)

        summary = (
            f"Total recipes: {total_recipes}\n"
            f"Recipes containing '{ingredient_to_count}': {matching_recipes}\n"
            f"Recipe names: {', '.join(matching_names) if matching_names else 'None'}\n"
        )

        with open(output_file, "w") as file:
            file.write(summary)

        print(f"\nSummary written to {output_file}:\n")
        print(summary)

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    print("Recipe Ingredient Search")
    ingredient = input("Enter an ingredient to search for: ").strip()
    if not ingredient:
        print("No ingredient entered. Exiting.")
        return

    process_recipes("recipes.txt", "summary.txt", ingredient)


if __name__ == "__main__":
    main()
