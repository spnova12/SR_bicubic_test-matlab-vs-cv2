function compute_psnr_for_SR(up_scale, GT_folder_dir, GT_type, Target_folder_dir,  TF_type)

total_psnr = 0.0;

GF = orderfields(dir(fullfile(GT_folder_dir, GT_type))); 
%% ========================================================================
if (nargin == 3)
    GF = dir(fullfile(GT_folder_dir, GT_type)); 
    
    for k = 1:numel(GF)
        %% read ground truth image
        im  = imread(fullfile(GT_folder_dir,GF(k).name));

        %%
        im_gnd = modcrop(im, up_scale);
        im_gnd = single(im_gnd)/255;

        %% bicubic interpolation
        im_l = imresize(im_gnd, 1/up_scale, 'bicubic');
        im_b = imresize(im_l, up_scale, 'bicubic');

        %% remove border
        im_gnd = shave(uint8(im_gnd * 255), [up_scale, up_scale]);
        im_b = shave(uint8(im_b * 255), [up_scale, up_scale]);

        %% compute PSNR (on illuminance only)
        psnr_bic = compute_psnr(im_gnd,im_b);
        total_psnr = psnr_bic + total_psnr;
    end
%% ========================================================================
elseif (nargin == 5)
    
    TF = orderfields(dir(fullfile(Target_folder_dir, TF_type)));
            
    for k = 1:numel(GF)
        %% read ground truth image
        im  = imread(fullfile(GT_folder_dir,GF(k).name));
        im2 = imread(fullfile(Target_folder_dir, TF(k).name));
        
        %%
        im_gnd = modcrop(im, up_scale);
        im_gnd = single(im_gnd)/255;
             
        im_gnd2 = modcrop(im2, up_scale);
        im_gnd2 = single(im_gnd2)/255;

        %% remove border
        im_gnd = shave(uint8(im_gnd * 255), [up_scale, up_scale]);
        im_gnd2 = shave(uint8(im_gnd2 * 255), [up_scale, up_scale]);

        %% compute PSNR (on illuminance only)
        psnr_bic = compute_psnr(im_gnd,im_gnd2);
        
        %% final result
        total_psnr = psnr_bic + total_psnr;
    end
%% ========================================================================
end

%% show results
fprintf('total PSNR : %f dB\n', total_psnr/numel(GF));


