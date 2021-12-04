{ pkgs ? import <nixpkgs> {} }:
let
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.3.0";
  }) {};
  pyenv = mach-nix.mkPython {
    requirements = ''
    orgparse
    pypandoc
    '';
  };
in pkgs.mkShell {
  buildInputs = [ pkgs.pandoc pyenv ];
}
