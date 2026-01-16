{
  description = "Python environment with pip packages (e.g., ucimlrepo)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            (python.withPackages (ps: with ps; [
              pip
              setuptools
            ]))
          ];

          # Automatically install pip packages when entering the shell
          shellHook = ''
            if [ ! -d .venv ]; then
              python -m venv .venv
              source .venv/bin/activate
              pip install --upgrade pip
              pip install ucimlrepo numpy pandas matplotlib seaborn scikit-learn joblib jupyter
            else
              source .venv/bin/activate
            fi
            echo "✅ Python environment ready with ucimlrepo"
          '';
        };
      });
}
