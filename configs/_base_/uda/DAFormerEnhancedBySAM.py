uda = dict(
    type='DAFormerEnhancedBySAM',
    alpha=0.99,
    pseudo_threshold=0.968,
    pseudo_weight_ignore_top=0,
    pseudo_weight_ignore_bottom=0,
    imnet_feature_dist_lambda=0,
    imnet_feature_dist_classes=None,
    imnet_feature_dist_scale_min_ratio=None,
    mix='class',
    blur=True,
    color_jitter_strength=0.2,
    color_jitter_probability=0.2,
    debug_img_interval=100,
    print_grad_magnitude=False,
    milestone_full_supervised_on_sam=0,
    SAM=dict(
        sam_model=dict(model_type='vit_h',
                       checkpoint='/raid/wzq/code/0-experiment-platform/pretrained/SAM/original/sam_vit_h_4b8939.pth',
                       points_per_side=32,
                       pred_iou_thresh=0.8,
                       stability_score_thresh=0.8,
                       crop_n_layers=1,
                       crop_n_points_downscale_factor=2,
                       min_mask_region_area=100),
        device='cuda:0',
        num_cls=19,
        cls_area_threshold=1e4,
        iou_conf_threshold=0.8))
use_ddp_wrapper = True
