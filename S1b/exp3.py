from rdkit import Chem
from gspan_mining.gspan import gSpan

def sdf_tp_gspan(sdf_file, output_file):
    suppl = Chem.SDMolSupplier(sdf_file)
    with open(output_file, "w") as f:
        for i,mol in enumerate(suppl):
            if mol is None:
                continue
            f.write(f"t # {i}\n")

            atom_map = {}
            for index,atom in enumerate(mol.GetAtoms()):
                atom_map[atom.GetIdx()] = index
                f.write(f"v {index} {atom.GetSymbol()}\n")

            for bond in mol.GetBonds():
                a1 = atom_map[bond.GetBeginAtomIdx()]
                a2 = atom_map[bond.GetEndAtomIdx()]
                bond_type = int(bond.GetBondTypeAsDouble())
                f.write(f"e {a1} {a2} {bond_type}\n")

def run_gspan():
    gs = gSpan(
        database_file_name="data/exp3/Compound_422.txt",
        min_support=5,
        verbose=0,
    )
    gs.run()

    with open("data/exp3/output.txt", "w") as f:
        for subgraph in gs._frequent_subgraphs:
            f.write(str(subgraph))
            f.write("\n\n")

if __name__ == "__main__":
    # sdf_tp_gspan("data/exp3/24826799.sdf", "data/exp3/molecules.gspan")
    run_gspan()
