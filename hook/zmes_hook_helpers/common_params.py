# list of variables that are common 
# do not include model specific variables 

ctx = None  # SSL context
logger = None  # logging handler
config = {}  # object that will hold config values
polygons = []  # will contain mask(s) for a monitor

# valid config keys and defaults
config_vals = {
        'secrets':{
            'section': 'general',
            'default': None,
            'type': 'string',
        },
         'base_data_path': {
            'section': 'general',
            'default': '/var/lib/zmeventnotification',
            'type': 'string'
        },
        'portal':{
            'section': 'general',
            'default': '',
            'type': 'string',
        },
        'api_portal':{
            'section': 'general',
            'default': '',
            'type': 'string',
        },
        'user':{
            'section': 'general',
            'default': None,
            'type': 'string'
        },
        'password':{
            'section': 'general',
            'default': None,
            'type': 'string'
        },
        'basic_user':{
            'section': 'general',
            'default': '',
            'type': 'string'
        },
        'basic_password':{
            'section': 'general',
            'default': '',
            'type': 'string'
        },
        'image_path':{
            'section': 'general',
            'default': '/var/lib/zmeventnotification/images',
            'type': 'string'
        },
        'detect_pattern':{
            'section': 'general',
            'default': '.*',
            'type': 'string'
        },
        'match_past_detections':{
            'section': 'general',
            'default': 'no',
            'type': 'string'
        },
        'past_det_max_diff_area':{
            'section': 'general',
            'default': '5%',
            'type': 'string'
        },
        'frame_id':{
            'section': 'general',
            'default': 'snapshot',
            'type': 'string'
        },
        'wait': {
            'section': 'general',
            'default':'0',
            'type': 'int'
        },

        'resize':{
            'section': 'general',
            'default': 'no',
            'type': 'string'
        },
        'delete_after_analyze':{
            'section': 'general',
            'default': 'no',
            'type': 'string',
        },
        'show_percent':{
            'section': 'general',
            'default': 'no',
            'type': 'string'
        },
        'allow_self_signed':{
            'section': 'general',
            'default': 'yes',
            'type': 'string'
        },
        'write_image_to_zm':{
            'section': 'general',
            'default': 'yes',
            'type': 'string'
        },
        'write_debug_image':{
            'section': 'general',
            'default': 'yes',
            'type': 'string'
        },
        'models':{
            'section': 'general',
            'default': 'yolo',
            'type': 'str_split'
        },
        'detection_mode': {
            'section':'general',
            'default':'all',
            'type':'string'
        },
        'import_zm_zones':{
            'section': 'general',
            'default': 'no',
            'type': 'string',
        },
        'poly_color':{
            'section': 'general',
            'default': '(127,140,141)',
            'type': 'eval'
        },

        # animation for push

        'create_animation':{
            'section': 'animation',
            'default': 'no',
            'type': 'string'
        },
        'animation_width':{
            'section': 'animation',
            'default': '400',
            'type': 'int'
        },
        'animation_retry_sleep':{
            'section': 'animation',
            'default': '15',
            'type': 'int'
        },
        'animation_max_tries':{
            'section': 'animation',
            'default': '3',
            'type': 'int'
        },

        # General ML
     

         'use_opencv_dnn_cuda':{
            'section':'ml',
            'default':'no',
            'type':'string'

        },

        'ml_gateway': {
            'section': 'ml',
            'default': None,
            'type': 'string'
        },

        'ml_fallback_local': {
            'section': 'ml',
            'default': 'no',
            'type': 'string'
        },
       
        'ml_user': {
            'section': 'ml',
            'default': None,
            'type': 'string'
        },
        'ml_password': {
            'section': 'ml',
            'default': None,
            'type': 'string'
        },
       

        # YOLO

        

        'yolo_type':{
            'section':'yolo',
            'default':'full',
            'type':'string'

        },
        'config':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/yolov3/yolov3.cfg',
            'type': 'string'
        },
        'weights':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/yolov3/yolov3.weights',
            'type': 'string'
        },
        'labels':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/yolov3/yolov3_classes.txt',
            'type': 'string'
        },
        'tiny_config':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/tinyyolo/yolov3-tiny.cfg',
            'type': 'string'
        },
        'tiny_weights':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/tinyyolo/yolov3-tiny.weights',
            'type': 'string'
        },
        'tiny_labels':{
            'section': 'yolo',
            'default': '/var/lib/zmeventnotification/models/tinyyolo/yolov3-tiny.txt',
            'type': 'string'
        },

        'yolo_min_confidence': {
            'section': 'yolo',
            'default': '0.4',
            'type': 'float'
        },
        
        # HOG
        'stride':{
            'section': 'hog',
            'default': '(4,4)',
            'type': 'eval'
        },
        'padding':{
            'section': 'hog',
            'default': '(8,8)',
            'type': 'eval'
        },
        'scale':{
            'key': 'scale',
            'section': 'hog',
            'default': '1.05',
            'type': 'string'
        },
        'mean_shift':{
            'section': 'hog',
            'default': '-1',
            'type': 'string'
        },

       # Face
        'face_num_jitters':{
            'section': 'face',
            'default': '0',
            'type': 'int',
        },
        'face_upsample_times':{
            'section': 'face',
            'default': '1',
            'type': 'int',
        },
        'face_model':{
            'section': 'face',
            'default': 'hog',
            'type': 'string',
        },
        'face_train_model':{
            'section': 'face',
            'default': 'hog',
            'type': 'string',
        },
         'face_recog_dist_threshold': {
            'section': 'face',
            'default': '0.6',
            'type': 'float'
        },
        'face_recog_knn_algo': {
            'section': 'face',
            'default': 'ball_tree',
            'type': 'string'
        },
        'known_images_path':{
            'section': 'face',
            'default': '/var/lib/zmeventnotification/known_faces',
            'type': 'string',
        },
        'unknown_images_path':{
            'section': 'face',
            'default': '/var/lib/zmeventnotification/unknown_faces',
            'type': 'string',
        },
        'unknown_face_name':{
            'section': 'face',
            'default': 'unknown face',
            'type': 'string',
        },
        'save_unknown_faces':{
            'section': 'face',
            'default': 'yes',
            'type': 'string',
        },

        'save_unknown_faces_leeway_pixels':{
            'section': 'face',
            'default': '50',
            'type': 'int',
        },

        # generic ALPR
        'alpr_service': {
            'section': 'alpr',
            'default': 'plate_recognizer',
            'type': 'string',
        },
        'alpr_url': {
            'section': 'alpr',
            'default': None,
            'type': 'string',
        },
        'alpr_key': {
            'section': 'alpr',
            'default': '',
            'type': 'string',
        },
        'alpr_use_after_detection_only': {
            'section': 'alpr',
            'type': 'string',
            'default': 'yes',
        },

         'alpr_pattern':{
            'section': 'general',
            'default': '.*',
            'type': 'string'
        },

        # Plate recognition specific
        'platerec_stats':{
            'section': 'alpr',
            'default': 'no',
            'type': 'string'
        },
        'platerec_regions':{
            'section': 'alpr',
            'default': None,
            'type': 'eval'
        },
        'platerec_min_dscore':{
            'section': 'alpr',
            'default': '0.3',
            'type': 'float'
        },
       
        'platerec_min_score':{
            'section': 'alpr',
            'default': '0.5',
            'type': 'float'
        },

        # OpenALPR specific
        'openalpr_recognize_vehicle':{
            'section': 'alpr',
            'default': '0',
            'type': 'int'
        },
        'openalpr_country':{
            'section': 'alpr',
            'default': 'us',
            'type': 'string'
        },
        'openalpr_state':{
            'section': 'alpr',
            'default': None,
            'type': 'string'
        },

        'openalpr_min_confidence': {
            'section': 'alpr',
            'default': '0.3',
            'type': 'float'
        },

        # OpenALPR command line specfic

         'openalpr_cmdline_binary':{
            'section': 'alpr',
            'default': 'alpr',
            'type': 'string'
        },
        
         'openalpr_cmdline_params':{
            'section': 'alpr',
            'default': '-j',
            'type': 'string'
        },
        'openalpr_cmdline_min_confidence': {
            'section': 'alpr',
            'default': '0.3',
            'type': 'float'
        },
       

    }
