# Installation with conda [deprecated]

> This method will install a discontinued version of Tierpsy Tracker (1.5.1).
> Unless you really need this version, we'd recommend installing Tierpsy Tracker
> either [with Docker](INSTALLATION_DOCKER.md) or [from source](INSTALLATION_SOURCE.md).

- Download python 3.6>= using [anaconda](https://www.anaconda.com/download/) or [miniconda](https://conda.io/miniconda.html) if you prefer a lighter installation.
- Open a Terminal in OSX or Linux. In Windows you need to open the Anaconda Prompt.
- [Optional] I would recommend to create and activate an [enviroment](https://conda.io/docs/user-guide/tasks/manage-environments.html) as:

```bash

conda create -n tierpsy

conda activate tierpsy #[Windows]
source activate tierpsy #[OSX or Linux]
```
- Finally, donwload the package from conda-forge
```bash
conda install -c conda-forge tierpsy numpy=1.16.3 pytables=3.5.1 opencv=3.4.8 pandas=0.24.2 #[Windows]
conda install tierpsy -c conda-forge tierpsy python=3.6 opencv=3.4.2 'pandas<1.0' #[OSX]
```
- After you can start tierpsy tracker by typing:
```bash
tierpsy_gui
```
Do not forget to activate the enviroment every time you start a new terminal session.

On OSX the first time `tierpsy_gui` is intialized it will create a file in the Desktop called tierpsy_gui.command. By double-cliking on this file tierpsy can be started without having to open a terminal.

#### Troubleshooting
- When installing from `conda`, you may get an error while the package `conda-forge::cloudpickle...` is installed, stating that `python3.6` couldn't be found. In this case, updating `conda` has been known to solve the issue. Alternatively, make sure to first install python 3.6, and then tierpsy, by executing:
```bash
conda install -c conda-forge python=3.6
conda install -c conda-forge tierpsy
```
- It seems that there might be some problems with some `opencv` versions available through `conda`. If you have problems reading video files or encounter error related with `import cv2`, then you can try to install opencv using pip as:
```bash
pip install opencv-python-headless
```
or specify the `opencv` version via:
```bash
conda install opencv=3.4.2 #[tested on MacOS]
```
- In Windows, the default anaconda channel does not have a valid `ffmpeg` version. Activate the tierpsy enviroment and use the conda-forge channel instead as:
```bash
conda install -c conda-forge ffmpeg
```