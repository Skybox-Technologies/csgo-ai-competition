{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs.python37Packages; [
    jupyter jupyterlab tensorflow_2 numpy pandas matplotlib tensorflow-tensorboard_2
    pygame
  ];
}
