# Parallel-SDF-to-TSV-Converter-using-RDKit-and-Multiprocessing
Features
    Parallel Processing: Utilizes the multiprocessing module to process multiple molecules concurrently, enhancing conversion speed.
    RDKit Integration: Makes use of RDKit's capabilities for handling chemical structures, including converting molecules to SMILES notation.
    Customizable: Easily adjustable to the number of processes required for parallel processing.

This Python script leverages the RDKit chemistry toolkit and multiprocessing to efficiently convert chemical structure data from Structure Data Files (SDF) to a Tab-Separated Values (TSV) format. The conversion includes extracting compound IDs and SMILES representations of molecules.
Features

    Parallel Processing: Utilizes the multiprocessing module to process multiple molecules concurrently, enhancing conversion speed.
    RDKit Integration: Makes use of RDKit's capabilities for handling chemical structures, including converting molecules to SMILES notation.
    Customizable: Easily adjustable to the number of processes required for parallel processing.


Requirements

    Python 3.x
    RDKit
    Pandas


Usage

    Specify the input SDF file (input_sdf_file) and output TSV file (output_tsv_file).
    Execute the script, and it will process the molecules in parallel, creating a TSV file with compound IDs and SMILES.
    
