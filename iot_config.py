def configure_device(device_name, **settings):
    print(f"\nConfiguring device: {device_name}")
    if settings:
        print("Applied Settings:")
        for key, value in settings.items():
            print(f"- {key}: {value}")
    else:
        print("No settings provided.")

# --- User Input ---
device = input("Enter device name: ")
brightness = input("Enter brightness level (0-100): ")
color = input("Enter color (e.g., blue, white): ")
mode = input("Enter mode (e.g., reading, night): ")

configure_device(
    device,
    brightness=brightness,
    color=color,
    mode=mode
)
