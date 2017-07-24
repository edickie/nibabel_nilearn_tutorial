# nibabel_nilearn_tutorial_2017
Materials for an intro to neuroimaging in python tutorial from Toronto, july 2017

## building the python environment for this tutorial..

Step 1.. start anaconda or miniconda..

Note in the example below..we are naming our environment "mripython" but you can call it whatever you want

```
conda create -n mripython3.5 python=3.5
source activate mripython
conda install -c conda-forge nilearn
conda install seaborn
conda install docopt
conda install jupyter
source deactivate
```

## Installing the newest version of nilearn

The version available in conda-forge is a year old.. newer released are available to pip install..

**Note: everything we will do in this tutorial has been tested with the above env**

```
conda create -n mripython3.6 python=3.6
source activate mripython
conda install scikit-learn
conda install seaborn
pip install nibabel
pip install -U nilearn
conda install docopt
conda install jupyter
```

## FYI when doing this on SciNet...there are a couple of little changes you can do

+ you need to load the anaconda3 module first
+ here we specified the full path to the conda env we want to build

```
module load anaconda3
conda create -p /scinet/course/ss2017/16_mripython/conda_envs/mripython3.5 python=3.5
source activate /scinet/course/ss2017/16_mripython/conda_envs/mripython3.5/
conda install -c conda-forge nilearn
conda install seaborn
conda install docopt
conda install jupyter
pip install qbatch  # an extra package for running things in parallel on the GPC
source deactivate
```

## the SciNet set-up script contains..

1. creates a sym-link from the tutorial conda env to your SciNet home
2. cp the the scripts into your SciNet 
3. link the data into your SciNet $SRATCH
