import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn import metrics

class evaluate_model:

    def __init__(self):
        self.message = 'Running'

    def __repr__(self):
        return self.message

    @staticmethod
    def plot_loss_acc_curves(history):
        """Plot the loss and accuracy curves for training and validation data"""
        fig, ax = plt.subplots(2,1)
        ax[0].plot(history.history['loss'], color='b', label="Training loss")
        ax[0].plot(history.history['val_loss'], color='r', label="validation loss",axes =ax[0])
        legend = ax[0].legend(loc='best', shadow=True)

        ax[1].plot(history.history['acc'], color='b', label="Training accuracy")
        ax[1].plot(history.history['val_acc'], color='r',label="Validation accuracy")
        legend = ax[1].legend(loc='best', shadow=True)
        plt.show()

    @staticmethod
    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=90)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()

    @staticmethod
    def Clf_report(model,Ytrue,YPred):
        print("Classification report for classifier %s:\n%s\n"
              % (model, metrics.classification_report(Ytrue, YPred)))
