#!/usr/bin/env python

"""
Calculates a seed correlation mask

Usage:
  seed_correlation_cmd.py [options] <func.nii.gz> <rois.nii.gz> <mask.nii.gz> <output.nii.gz>

Arguments:
    <func.nii.gz>    The functional 4D nifti files
    <rois.nii.gz>    The rois mask or atlas
    <mask.nii.gz>    A brainmask for the functional file
    <output.nii.gz>  Output filename

Options:
  --roi-number INT   Index [default: 1] of the ROI to use
  --debug            Debug logging in Erin's very verbose style
  -h,--help          Print help


DETAILS
Written for the SciNet HCP summer school
"""

# this is the scipy stack, e.g., MATLAB 4 no $
import numpy as np
import scipy as sp
import nibabel as nib
import sys
import os
from docopt import docopt

def main():
    global DRYRUN

    arguments = docopt(__doc__)
    funcfile = arguments['<func.nii.gz>']
    rois = arguments['<rois.nii.gz>']
    mask = arguments['<mask.nii.gz>']
    outputname = arguments['<output.nii.gz>']
    roi = arguments['--roi-number']
    DEBUG = arguments['--debug']

    if DEBUG: print(arguments)


    # nibabel has a look into the data
    func_nib = nib.load(funcfile)
    affine = func_nib.get_affine()
    header = func_nib.get_header()

    # get the dimensions for the fMRI file
    dims = func_nib.shape

    # use get data to extract the data from it
    func_data = func_nib.get_data()

    # reshape to voxels * timepoints (4D --> 2D)
    func_data = func_data.reshape(dims[0]*dims[1]*dims[2], dims[3])

    # now do the same thing for rois
    rois_data = nib.load(rois).get_data()
    mask_data = nib.load(mask).get_data()

    ## fail now if the rois and func file don't match in dimensions
    if not rois_data.shape[0:2] == dims[0:2]:
        sys.exit('{} and {} do not match in dimensions'.format(data, seed))
    if not mask_data.shape[0:2] == dims[0:2]:
        sys.exit('{} and {} do not match in dimensions'.format(data, mask))

    rois_data = rois_data.reshape(dims[0]*dims[1]*dims[2], 1)
    mask_data = mask_data.reshape(dims[0]*dims[1]*dims[2], 1)

    ## add a mask to get rid of the weird bits
    idx_mask = np.where(mask_data > 0)[0]
    print('{} voxels in brainmask'.format(idx_mask.shape))

    # get the seed time series
    print('unique rois are {}'.format(np.unique(rois_data)))
    idx = np.where(rois_data == int(roi))[0]
    print('{} voxels have roi number {}'.format(idx.shape, roi))
    idx_masked = np.intersect1d(idx,idx_mask)
    if idx_masked.shape[0] > 0:
        ts = np.mean(func_data[idx_masked, :], axis=0)
    else:
        sys.exit('roi {} is not inside the brainmask'.format(roi))

    # make an output matrix
    output = np.zeros(dims[0]*dims[1]*dims[2])

    # correlate seed against all voxels
    for i in np.arange(len(idx_mask)):
        output[idx_mask[i]] = np.corrcoef(ts, func_data[idx_mask[i], :])[0][1]

    # get back to 4D
    output_3D = np.reshape(output, (dims[0], dims[1], dims[2], 1))

    # write the results into a NIFTI file
    output_img = nib.nifti1.Nifti1Image(output_3D, affine)
    output_img.to_filename(outputname)

if __name__ == '__main__':
    main()
