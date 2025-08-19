def schedule_post(content, **options):
    print("\nScheduled Post:")
    print(f"Content: {content}")
    for key, value in options.items():
        print(f"{key.capitalize()}: {value}")

# --- User Input ---
text = input("Enter post content: ")
tags = input("Enter hashtags (optional): ")
location = input("Enter location (optional): ")
privacy = input("Enter privacy setting (public/private): ")

schedule_post(
    text,
    tags=tags if tags else "None",
    location=location if location else "None",
    privacy=privacy if privacy else "public"
)
