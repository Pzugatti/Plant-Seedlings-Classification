# Plant-Seedlings-Classification
The aim of this project is to use deep learning model to classify the plant seedling by using a supervised learning technique.

The data-set is available on Kaggle : (https://www.kaggle.com/c/plant-seedlings-classification/data).


## Data-set examination
### There are 12 species in the data-set which are shown below:
![xtrain_plant](https://user-images.githubusercontent.com/43289100/45993669-87d6f480-c0c2-11e8-86e7-cb5113af196b.png)

The data-set is split into two group, which are training and testing data.

### Graphic visualizes the total number for each species: 

![totalnum_species](https://user-images.githubusercontent.com/43289100/46394342-707bb500-c71b-11e8-97b1-8a3260c4c16d.PNG)

![no_species](https://user-images.githubusercontent.com/43289100/45995997-20727200-c0cd-11e8-8d1b-3b3ecfbbfbab.png)

According to the above graph, the highest number of the plant is Loose-Silky-Bent, and the lowest number of the plants are Maize and Common Wheat.


## Pre-processing dataset
The training and testing images have been processed by using OpenCV libraries that extracted the plant seedling only and removed the background noise. The filtering process depending on the HSV values, retaining green HSV parameters and convert back to RGB format, which means only the green colour remains and the rest of the colour are removed. The pre-processed image has been shown below:

![xtrain_image_processing](https://user-images.githubusercontent.com/43289100/46004555-c6ca7180-c0e5-11e8-895d-0ab270471a8b.png)

Then the training and testing dataset have been normalized by dividing 255.0 to limit the pixel values within 0 to 1 and the labels are one-hot-encoded.


## Convolutional neural network (CNN)
CNN is a good choice while dealing with the image data. Designed CNN architecture based on personal experience, knowledge and, most important, the machine learning community and forum helps. The time spent a lot on tuning the model hyper-parameters in order to achieve higher accuracy and lower residual for model training. So that the model predicting the unseen data will have a higher chance to obtain the correct result. Of course, there is plenty of other powerful CNN available such as AlexNet, ResNet and more, those networks may also suitable applying in this data-set.

### Model visualization:

![model](https://user-images.githubusercontent.com/43289100/46008456-64766e80-c0ef-11e8-9eb9-013068d8bc9f.png)


## Training the model with validation and training data-set
![psr_confusion_matrix](https://user-images.githubusercontent.com/43289100/46009006-e0bd8180-c0f0-11e8-9f7f-5c87650e1824.png)

The validation data-set is getting from the training data-set. For instance, the 100% training data-set split out its 10% data-set as validation data-set, which means 10 % treat as validation data-set and 90% treat as training data-set.

According to the confusion matrix, Sugar Beet and Black-Grass have misclassified obviously after the validation and training data-set fit into CNN model. There are 10 samples of Sugar Beet misclassified as Black-Grass, and 7 samples of Black-Grass misclassified as Sugar Beet. This means both plant images may having similar features that confuse the CNN model. The solution could be getting more data-set, apply alternative image processing techniques, more data augmentation or modified or change the current CNN.

![loss_acc_curve](https://user-images.githubusercontent.com/43289100/46009861-5fb3b980-c0f3-11e8-84a7-e96a491f37ce.png)

![cnn_result](https://user-images.githubusercontent.com/43289100/46395204-365fe280-c71e-11e8-8007-6068da075522.PNG)

Above graph showing the loss and accuracy of the training and validation data after both data-set fittings into the model. The x-axis is the epoch, the loss is decreasing and accuracy is increasing when epoch getting larger. At the end of the epoch, the validation accuracy is greater than the training accuracy that means the model doesn't overfit.


## Predict unseen data-set (testing data-set)
![kaggle_result](https://user-images.githubusercontent.com/43289100/46010578-c76b0400-c0f5-11e8-8d9e-b4ea9b19d403.PNG)
Above picture was getting from my Kaggle competition result. The trained model predicted the unseen data and the result shows 0.91939(92%) accuracy. The remaining 8% (100%- 92%) could be the Sugar Beet,Black-Grass, and a small number of other plants have misclassified.


## Summary
The Sugar Beet and Black-Grass misclassified after training causes the model unable to differentiate both of them and directly affecting the accuracy when predicting the unseen data. The solution could be getting more data-set, apply alternative image processing techniques, more data augmentation or modified or change the current CNN. This will be the future work.


# In my opinion
This Kaggle competition is challenging at least for me, because I just started to study this deep learning field a few months ago. I 'google' numerous blog,forum, documentation and more in order to let myself having intuition understanding how does deep learning work. Still, there are too many knowledge and techniques almost make me feels overwhelming. Anyway, it is great experience to know how to build a simple CNN and gain the significant skills. Even though deep learning network is quite hard to master, however, it could solve the real world problems, which make me feels exciting and motivating!


# Working enviroment
Google Colab
  - Keras 2.1.6
  - Python 3
  - Opencv 3.4.3
  - sklearn 0.19.2

