# DATASET PATH
dir = "/Volumes/Personal_Drive/Datasets/udacity-driving/dataset-2/"
dir3 = "/Volumes/Personal_Drive/Datasets/udacity-driving/dataset-3/"
dir2 = "/Volumes/Personal_Drive/Datasets/udacity-driving/dataset-1/"
val_dir = "/Volumes/Personal_Drive/Datasets/udacity-driving/steering_validation/"


# TRAINING
image_width = 320
image_height = 160
load_weights = True

model_path = "./steering/weights/own/trained-cai-v6.h5"
# model_path = "/Users/yongyangnie/Developer/self-driving-golf-cart/steering/weights/own/trained-cai-v6.h5"
# model_path = "./steering/weights/training/str-cai-self-v2.h5"

train_model_path = "./str-cai-self-v1.h5"
own_dataset_dirs = ["/Volumes/Personal_Drive/Datasets/golf-cart-dataset/part-1",
                    "/Volumes/Personal_Drive/Datasets/golf-cart-dataset/part-2",
                    "/Volumes/Personal_Drive/Datasets/golf-cart-dataset/part-3"]

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
