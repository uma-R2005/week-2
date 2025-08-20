import csv

patients_file = 'patients.csv'

hypertension_patients = []
total_age = 0

with open(patients_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['diagnosis'] == 'Hypertension':
            hypertension_patients.append(row)
            total_age += int(row['age'])

print("Patients with Hypertension and their medications:")
for patient in hypertension_patients:
    print(f"- {patient['name']} : {patient['medication']}")

if hypertension_patients:
    avg_age = total_age / len(hypertension_patients)
    print(f"\nAverage age of hypertension patients: {avg_age:.1f} years")
else:
    print("No patients with Hypertension found.")
