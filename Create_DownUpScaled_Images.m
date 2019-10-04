
GT_folder_dir = 'SR_testing_datasets/Set5';
GT_type = '*.png';
output_dir = 'SR_testing_datasets_matlab/Set5';
up_scale = 4;

%% create ouput's folder
mkdir(output_dir)

%% create down scaled image
GF = dir(fullfile(GT_folder_dir, GT_type)); 
for k = 1:numel(GF)
    %% read ground truth image
    img_name = fullfile(GT_folder_dir,GF(k).name);
    fprintf('%s\n', img_name); 
    im = imread(img_name);
    
    im = single(im)/255;
    
    %% bicubic interpolation
    im_l = imresize(im, 1/up_scale, 'bicubic');
    im_b = imresize(im_l, up_scale, 'bicubic');
    
    imwrite(im_b, fullfile(output_dir,GF(k).name));
end


