'''
calculate the PSNR.
same as MATLAB's results
Based on this link.
https://github.com/xinntao/BasicSR/blob/master/metrics/calculate_PSNR_SSIM.py
'''


import math
import numpy as np
import cv2

from os import listdir
from os.path import join


def main():
    # Psnr measurement after down, up scaling by matlab's BICUBIC
    compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', 'SR_testing_datasets_matlab/Set5')

    # PSNR measurement of A and B, A: Original, B: down, up scaled from A by matlab bicubic
    compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', 'SR_testing_datasets_matlab/Set5')

    # PSNR measurement of A and B, A: Original, B: down, up scaled from A by python opencv bicubic
    compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', 'SR_testing_datasets_cv2/Set5')

    # PSNR measurement of A and B, A: Original, B: down, up scaled from A by Fake matlab(writen by python) bicubic
    compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', 'SR_testing_datasets_Fake_Matlab/Set5')


def compute_psnr_for_SR(scale_factor, GT_folder_dir, Target_folder_dir):
    folder_GT_dir = [join(GT_folder_dir, x) for x in sorted(listdir(GT_folder_dir))]
    folder_Gen_dir = [join(Target_folder_dir, x) for x in sorted(listdir(Target_folder_dir))]

    crop_border = scale_factor
    test_Y = True  # True: test Y channel only; False: test RGB channels
    PSNR_all = []

    for i, (GT_dir, Gen_dir) in enumerate(zip(folder_GT_dir, folder_Gen_dir)):
        im_GT = cv2.imread(GT_dir)
        im_Gen = cv2.imread(Gen_dir)

        # crop borders
        if im_GT.ndim == 3:
            cropped_GT = im_GT[crop_border:-crop_border, crop_border:-crop_border, :]
            cropped_Gen = im_Gen[crop_border:-crop_border, crop_border:-crop_border, :]
        elif im_GT.ndim == 2:
            cropped_GT = im_GT[crop_border:-crop_border, crop_border:-crop_border]
            cropped_Gen = im_Gen[crop_border:-crop_border, crop_border:-crop_border]
        else:
            raise ValueError('Wrong image dimension: {}. Should be 2 or 3.'.format(im_GT.ndim))

        if test_Y and im_GT.shape[2] == 3:  # evaluate on Y channel in YCbCr color space
            cropped_GT = bgr2ycbcr(cropped_GT)
            cropped_Gen = bgr2ycbcr(cropped_Gen)
        else:
            cropped_GT = cropped_GT
            cropped_Gen = cropped_Gen

        # calculate PSNR and SSIM
        PSNR = calculate_psnr(cropped_GT, cropped_Gen)
        PSNR_all.append(PSNR)

    print('total PSNR : {:.6f} dB'.format(sum(PSNR_all) / len(PSNR_all)))


def calculate_psnr(img1, img2):
    # img1 and img2 have range [0, 255]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))


def bgr2ycbcr(img, only_y=True):
    '''same as matlab rgb2ycbcr
    only_y: only return Y channel
    Input:
        uint8, [0, 255]
        float, [0, 1]
    '''
    in_img_type = img.dtype
    img.astype(np.float32)
    if in_img_type != np.uint8:
        img *= 255.
    # convert
    if only_y:
        rlt = np.dot(img, [24.966, 128.553, 65.481]) / 255.0 + 16.0
    else:
        rlt = np.matmul(img, [[24.966, 112.0, -18.214], [128.553, -74.203, -93.786],
                              [65.481, -37.797, 112.0]]) / 255.0 + [16, 128, 128]
    if in_img_type == np.uint8:
        rlt = rlt.round()
    else:
        rlt /= 255.
    return rlt.astype(in_img_type)


if __name__ == '__main__':
    main()
