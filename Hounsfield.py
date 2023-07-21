# Define the HU values and corresponding tissue types
HU_ranges = {
    -1000: 'Air',
    -100: 'Fat',
    0: 'Water',
    10: 'Body fluids (e.g. CSF)',
    20: 'Muscle',
    30: 'Blood or gray matter',
    45: 'Soft tissue',
    60: 'Gray matter',
    90: 'Blood (coagulated)',
    100: 'Iodinated contrast (low concentration)',
    300: 'Trabecular bone',
    600: 'Iodinated contrast (high concentration)',
    1000: 'Cortical bone'
}

# Ask the user to input a numerical HU value
HU = float(input('Enter a Hounsfield Unit (HU) value: '))

# Determine the corresponding tissue type based on the input HU value
tissue_type = None
for range_start, tissue in HU_ranges.items():
    if HU >= range_start:
        tissue_type = tissue
    else:
        break

# Print the result and a disclaimer
if tissue_type:
    print(f"The HU value corresponds to {tissue_type}.")
else:
    print("The input HU value does not correspond to any known tissue type.")
print("Please note that the results should be interpreted in the context of the clinical case and individual variations may occur.")

