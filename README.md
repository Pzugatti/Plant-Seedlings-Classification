# Plant-Seedling-Recognition
The aim of this project is to recognize the plant seedling on the farm and the data-set is available from Kaggle (https://www.kaggle.com/c/plant-seedlings-classification/data).

## Convolutional neural network (CNN)
In this project, CNN has been implemented that provides great handling for the image data. Design CNN architecture (26 layers) based on personal experience, knowledge and, most important, the machine learning community and forum help. The time spent a lot on tuning hyper-parameters in order to achieve higher accuracy and lower residual as well for model training. So that model predicting the unseen data will have higher chance to obtain correct result. Of course, there are plenty powerful CNN network available such as AlexNet, ResNet and more.

## Data-set examination
There are 12 species available in the data-set which are shown below:
![xtrain_plant](https://user-images.githubusercontent.com/43289100/45993669-87d6f480-c0c2-11e8-86e7-cb5113af196b.png)


Graphic visualizes the total number for each species: 

![no_species](https://user-images.githubusercontent.com/43289100/45995997-20727200-c0cd-11e8-8d1b-3b3ecfbbfbab.png)
According to above graph, the highest number of the plant is Loose-Silly-Bent, and also lowest number of the plants are Maize and Common Wheat.

## Pre-processing image
The train and test images have been processed by using OpenCV3
