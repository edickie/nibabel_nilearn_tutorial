
# nibabel_nilearn_tutorial
Materials for an intro to neuroimaging in python tutorial from, orignally given at the Compute Ontario Summer School Toronto, july 2017

## Connecting to the SciNet jupyter hub..

First you need to ssh to one of the niagara nodes to clone this repo

```sh
ssh USERNAME@niagara.scinet.utoronto.ca
git clone 
mkdir ~/.conda/envs
ln -s /scinet/course/ss2018/3_bm/1_mripython/conda_envs/coss2018_mri ~/.conda/envs/coss2018_mri
```

Open a terminal on your laptop (can be mobaxterm on a Windows laptops)
(with USERNAME replaced by your compute username)

You will be prompted for you SciNet PASSWORD

```sh
ssh -L8888:tds04:8000 USERNAME@niagara.scinet.utoronto.ca -N
```

Once if you did this properly. It will look like nothing happend. **KEEP THIS TERMINAL OPEN**. And point your local browser to "localhost:8888

# If not using the SciNet jupyter hub, you can build the environment for this tutorial 

## building the python environment for this tutorial..

Step 1.. start anaconda or miniconda..

Note in the example below..we are naming our environment "mripython" but you can call it whatever you want

```
conda create -n mripython3.5 python=3.5
source activate mripython3.5
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
source activate mripython3.6
conda install scikit-learn
conda install seaborn
pip install nibabel
pip install -U nilearn
conda install docopt
conda install jupyter
```

## FYI when doing this on the CAMH SCC cluster here are the lines you need

```sh
## loads conda
module load PYTHON/3.6

## create the conda env into ${HOME}/.conda/envs/ with name 3.6_nilearn_01
conda create -n 3.6_nilearn_01 python=3.6

## activates that conda environment
source activate 3.6_nilearn_01

## install the packages - note jupyter is needed for us to be able to use it on jyputer hub
conda install jupyter
conda install scikit-learn
conda install seaborn
pip install nibabel
pip install nilearn
conda install docopt

## adds the 3.6_nilearn_01 environment to the kernels available by jupyter hub
python -m ipykernel install --user --name 3.6_nilearn_01 --display-name "Python (3.6_nilearn_01)"

## deactivate the conda environment
source deactivate
```

## FYI when doing this on SciNet...there are a couple of little changes you can do

+ you need to load the python/*anaconda* module first
+ here we specified the full path to the conda env we want to build

```
module load python/3.6.4-anaconda5.1.0
conda create -p /scinet/course/ss2018/3_bm/1_mripython/conda_envs/coss2018_mri python=3.6
source activate /scinet/course/ss2018/3_bm/1_mripython/conda_envs/coss2018_mri
conda install -c conda-forge nilearn
conda install seaborn
conda install docopt
conda install jupyter
pip install qbatch  # an extra package for running things in parallel on the GPC
source deactivate
```
