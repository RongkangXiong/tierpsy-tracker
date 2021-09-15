# Installation from source

> This is the preferred installation method if you want to have constant updates and/or contribute to Tierpsy's development.

- Download Python >= 3.6 using [anaconda](https://www.anaconda.com/download/) or [miniconda](https://conda.io/miniconda.html).
- Install [git](https://git-scm.com/). [Here](https://gist.github.com/derhuerst/1b15ff4652a867391f03) are some instructions to install it. [GitHub Desktop](https://desktop.github.com/) is also an option if you prefer a graphical interface.
- Install a [C compiler compatible with cython](http://cython.readthedocs.io/en/latest/src/quickstart/install.html). In Windows, you can use [Visual C++ 2015 Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). In OSX, we recommend to download XCode from the AppStore.
- Follow the OS-specific instructions below.

### MacOS
- Open a Terminal prompt and execute the following commands:
```bash
git clone https://github.com/Tierpsy/tierpsy-tracker
cd tierpsy-tracker
conda env create --file tierpsy_macosx.yml #[MacOS]
conda activate tierpsy
pip install -e .
tierpsy_gui
```
> Fork the repo instead of cloning if you want to contribute to Tierpsy's development.

Tested on Mojave.

### Windows 10
- Clone the repository in a folder named `tierpsy-tracker`. You can do this either:
    - via a git prompt
    - with your browser: `Clone or Download` -> `Download ZIP`, then unzip and rename the folder
    - with your browser: `Clone or Download` -> `Open in Desktop`, then continue with [GitHub Desktop](https://desktop.github.com/)
- Open the Anaconda prompt, move to the `tierpsy-tracker` folder using the `cd` command appropriately, and type:
```bash
conda env create -f tierpsy_windows.yml #[Windows 10]
conda activate tierpsy
pip install -e .
tierpsy_gui
```

#### Troubleshooting
- Make sure you have an up-to-date version of conda. To update conda, `conda update -n base -c defaults conda`. We tested on `conda 4.8.2`.
- Try the alternative command `conda env create -f tierpsy_windows_conda4_5_11.yml`
- `pip install -e .` has been known to fail with an error stating that `command 'cl.exe' failed: No such file or directory`. See the [Known Issues](ISSUES.md) for a solution.
- Windows machines without a CUDA enabled GPU: see the [Known Issues](ISSUES.md).

### Linux
- Open a shell and type:
```bash
git clone https://github.com/Tierpsy/tierpsy-tracker
cd tierpsy-tracker
conda create -n tierpsy #[optional]
conda activate tierpsy #[optional]
conda install --file requirements.txt
pip install -e .
tierpsy_gui
```
