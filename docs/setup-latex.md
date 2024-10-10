# Setup LaTeX

## Requirements

- Visual Studio Code, tested on version:
- LaTeX Workshop extension (`james-yu.latex-workshop`) in Visual Studio Code (Tested with: v10.5.0)

### Versions used for macOS

- Visual Studio Code:

```
1.92.2
fee1edb8d6d72a0ddff41e5f71a671c23ed924b9
arm64
```

- LaTeX Workshop: `v10.3.2`

## Windows

Article: [How to write LaTeX documents using Visual Studio Code](https://www.geekering.com/programming-languages/filipesalgueiro/how-to-write-latex-documents-using-visual-studio-code/)

### Steps

1. Download and install MiKTeX: https://miktex.org/
2. Install Perl: https://strawberryperl.com/
3. Open VS code
4. Create or open `tex` file
5. Compile it by pressing `Ctrl + S` in the opened `tex` file

### Proofed versions

- MiKTeX: One MiKTeX Utility 1.8 (MiKTeX 23.10)
- Perl: perl 5, version 38, subversion 0 (v5.38.0) built for MSWin32-x64-multi-thread

### Notes

##### Miktex updates

According to the article, you should open Miktex Console, check for updates, and perform the update. But when I did it, I could not build the tex files afterward, and it randomly crashed without any logs, even after restarting the computer.

## Linux (Ubuntu)

Article: [Compiling LaTeX with Ubuntu and Visual Studio Code](https://nevalsar.hashnode.dev/compiling-latex-with-ubuntu-and-visual-studio-code)

### Steps

1. Run:

```sh
apt install texlive-science texlive-latex-extra texlive-extra-utils latexmk texlive-publishers texlive-science
```

Or for full, which is better as the packages are downloaded with it, but it takes more time:

```sh
sudo apt-get install texlive-full
```

2. Open VS code and open `main.tex` in `tex` folder, where the project could be compiled
3. Compile it by pressing `Ctrl + S` in the `main.tex` file in the `tex` folder.

## macOS

YouTube video: [Install LaTeX Workshop and compile PDF in VSCode LaTeX (Mac)](https://www.youtube.com/watch?v=CmagZthwhaY)

### Steps

1. Download and install MiKTeX: https://miktex.org/
2. Open VS code
3. Create or open `tex` file
4. Compile it by pressing `Ctrl + S` in the opened `tex` file

### Install latexindent for code formatting

https://github.com/cmhughes/latexindent.pl

To install `latexindent`, run the following commands:

```sh
brew install perl
brew install cpanm

cpanm YAML::Tiny
cpanm File::HomeDir

brew install latexindent
```

### Trubleshooting

##### Add latex to PATH

To add latex to PATH, you can run the following command:

```sh
echo export 'PATH=~/bin:$PATH' >> ~/.zshrc
```

##### pdflatex did not succeed

Open MiKTeX Console and check for updates. Install them if there are any. Then, try to compile the `tex` file again.
