
%% Psnr measurement after down, up scaling by matlab's BICUBIC
compute_psnr_for_SR(4,'SR_testing_datasets/Set5', '*.png')

%% PSNR measurement of A and B, A: Original, B: down, up scaled from A by matlab bicubic
compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', '*.png', 'SR_testing_datasets_matlab/Set5', '*.png')

%% PSNR measurement of A and B, A: Original, B: down, up scaled from A by python opencv bicubic
compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', '*.png', 'SR_testing_datasets_cv2/Set5', '*.png')

%% PSNR measurement of A and B, A: Original, B: down, up scaled from A by Fake matlab(writen by python) bicubic
compute_psnr_for_SR(4, 'SR_testing_datasets/Set5', '*.png', 'SR_testing_datasets_Fake_Matlab/Set5', '*.png')




