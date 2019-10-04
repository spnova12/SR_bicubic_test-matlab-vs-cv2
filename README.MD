SR_bicubic_test(matlab vs cv2)
================

This project compares the bicubic and psnr measurements in matlab and python's cv2.    

**Dependencies and Installation**  
* Python 3.6
* PyTorch 1.1
* Matlab
* opencv 3.4.2

**How to use code**  
1. Make Down and Up scaled Images by using bicubic in various ways.  
run Create_DownUpScaled_Images.m  
run Create_DownUpScaled_Images_cv2.py  
run Create_DownUpScaled_Images_fakeMatlab.py  

2. Calculate PSNR  
run Get_PSNR_demo.m  
run Get_PSNR_demo.py  


**Experiment result**  
Since the 'bicubic' and 'bgr2ycbcr' functions are different in cv2 and matlab,   
the values are different when measuring the PSNR of SR.

The link below explains why.  
<https://stackoverflow.com/questions/22092744/what-is-the-difference-between-opencvs-and-matlabs-bicubic-algorithm>

Original image  
![Alt text](SR_testing_datasets/Set5/bird.png "Original image")  
Matlab bicubic  
![Alt text](SR_testing_datasets_matlab/Set5/bird.png "Matlab bicubic")    
cv2 bicubic    
![Alt text](SR_testing_datasets_cv2/Set5/bird.png "cv2 bicubic")  
You can see the difference between the two results.  

But I thankfully found that the result of xinntao's python code is exactly the same as in matlab.
<https://github.com/xinntao>

PSNR(scale factor : 4, Set5)  

| Method   |      PSNR(dB)      |
|----------|:-------------:|
| down, up scaling by matlab's BICUBIC |  28.419690 | 
| down, up scaled from A by python opencv bicubic |    27.683244   | 
| down, up scaled from A by Fake matlab(writen by python) | 28.419690 | 

It can also be confirmed that the PSNR results of 'Get_PSNR_demo.m' and 'Get_PSNR_demo.py' are the same.