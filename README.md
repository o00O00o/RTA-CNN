# An End-to-End Atrial Fibrillation Detection by A Novel Residual-Based Temporal Attention Convolutional Neural Network with Exponential Nonlinearity Loss
This repository provides source code of RTA-CNN for ECG signal classification and atrial fibrillation detection.


# Dataset
To evaluate our method, we used The dataset of [The 2017 PhysioNet Challenge][data_link]. The challenge aims to encourage the development of algorithms to classify, from a single short ECG lead recording (between 30 s and 60 s in length), whether the recording shows normal sinus rhythm, atrial fibrillation (AF), an alternative rhythm, or is too noisy to be classified.


# Requirements
* [Tensorflow][tensorflow_link] version >=1.13.1.
* [Keras][keras_link] version >=2.2.4
* Some basic python packages such as Numpy, Matplotlib, pandas.

[data_link]:https://physionet.org/content/challenge-2017/1.0.0/
[tensorflow_link]:https://www.tensorflow.org/
[keras_link]:https://keras.io/

# Usage
The experiments are all done in 4-fold cross-validation configuration.  
The directory hierarchy should be like this:  

    RTA-CNN/
    ├── folds
    │   ├── fold0
    │   │   ├── data
    │   │   ├── label
    │   │   ├── AF
    |   |   |   ├──data
    |   |   |   └── label
    │   │   ├── normal
    │   │   └── other
    │   ├── fold012
    │   │   ├── data
    │   │   └── label
    │   ├── fold013
    │   ├── fold023
    │   ├── fold123
    │   ├── fold1
    │   ├── fold2
    │   └── fold3
    └── logs
        ├── ex0
        │   └── models
        ├── ex1
        ├── ex2
        └── ex3

To train on fold 1,2,3 and validate on fold 0:  
```bash
python main.py --expeiment-index 0
```
