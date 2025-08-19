def dispatch_parcels(vehicle_id, *parcel_ids):
    if not parcel_ids:
        print(f"\nNo parcels assigned to vehicle {vehicle_id}.")
        return
    
    print(f"\nVehicle {vehicle_id} dispatched with parcels:")
    for pid in parcel_ids:
        print(f"- Parcel ID: {pid}")
    print(f"Total parcels: {len(parcel_ids)}")


# Example usage:

dispatch_parcels("V1001", "P123", "P124", "P125")

dispatch_parcels("V1002", "P200", "P201")

dispatch_parcels("V1003")  # No parcels assigned (edge case)
