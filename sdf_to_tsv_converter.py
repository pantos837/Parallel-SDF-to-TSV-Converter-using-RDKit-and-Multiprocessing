
from rdkit import Chem
import pandas as pd
from multiprocessing import Pool
from itertools import islice

# Specify the input SDF file and output TSV file
input_sdf_file = 'my_input_file.sdf'
output_tsv_file = 'my_output_file.tsv'

# Function to process a single molecule
def process_molecule(mol):
    if mol:
        compound_id = mol.GetProp('_Name')
        smiles = Chem.MolToSmiles(mol)
        return [compound_id, smiles]
    else:
        return None

# Initialize a Pandas DataFrame to store the data
data = []

# Process the SDF file in parallel using multiple processes
def main():
    suppl = Chem.SDMolSupplier(input_sdf_file)
    with Pool(processes=4) as pool:  # Adjust the number of processes as needed
        for mol in suppl:
            data.append(process_molecule(mol))

    # Create a DataFrame from the collected data
    df = pd.DataFrame([x for x in data if x is not None], columns=['Compound_ID', 'SMILES'])

    # Export the DataFrame to the TSV file
    df.to_csv(output_tsv_file, sep='\t', header=True, index=False)

if __name__ == "__main__":
    try:
        main()
        print(f"Conversion completed.")
    except ValueError as e:
        print(f"Error: {e}")

