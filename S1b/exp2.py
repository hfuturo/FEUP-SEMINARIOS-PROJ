# import pandas as pd

# from rdkit import Chem
# from PaDEL_pywrapper import PaDEL

# supplier = Chem.SDMolSupplier("data/exp2/521106.sdf", removeHs=False)
# mols = [mol for mol in supplier if mol is not None]

# padel = PaDEL(descriptors=[])

# df = padel.calculate(mols, show_banner=True, njobs=1)

# print(df.head())
# print(df.shape())

from padelpy import padeldescriptor
import pandas as pd

# padeldescriptor(
#     mol_dir='data/exp2/521106.sdf',              # input SDF
#     d_file='data/exp2/descriptors_output.csv',     # output CSV file
#     fingerprints=True,                   # include fingerprints
#     retainorder=True,                    # keep molecule order
#     standardizenitro=True,               # fix nitro groups automatically
#     removesalt=True,                     # remove salts if present
#     threads=2                            # number of CPU threads
# )

df = pd.read_csv("data/exp2/descriptors_output.csv")
print(df.shape)
print(df.head())