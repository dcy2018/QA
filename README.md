# QANet-PyTorch

## Introduction

Re-implement [QANet](https://arxiv.org/pdf/1804.09541.pdf) with PyTorch.
Forked from Bangliu/QANet-PyTorch, just add dir'dataset' and change some paths in QANet_main.py.

## Requirement

spacy >= 2.0.16

visdom >= 0.1.8.9

gensim >= 3.8.3

GPU >= 16G for batchsize 32 (>=11G for batchsize 20)

SQuAD 1.1 dataset(train-v1.1.json and dev-v1.1.json)

Glove word_embedding file(glove.840B.300d.txt) and char_embedding file (glove.840B.300d-char.txt)

## Usage

Run `python3 QANet_main.py --batch_size 32 --epochs 30 --with_cuda --use_ema ` to train model with cuda.

Run `python3 QANet_main.py --batch_size 16 --epochs 3 --with_cuda --use_ema --debug` to debug with small batches data.

## **Performance**

With ema, 8 head attention, hidden size 128, QANet_andy.model,  30 epochs, batch_size 16:

F1: **80.49**
EM: **71.24**

Performance on validation set during 30 epochs:

<img src="https://github.com/BangLiu/QANet-PyTorch/blob/master/training.png" width="500" />


## Structure
QANet_main.py: code for training QANet.

trainer/QANet_trainer.py: trainer.

model/QANet_model.py: defines QANet.

data_loader/SQuAD.py: SQuAD 1.1 and 2.0 data loader.

Other codes are utils or neural network common modules library.


## Acknowledge
1. The QANet structure implementation is mainly based on https://github.com/hengruo/QANet-pytorch and https://github.com/andy840314/QANet-pytorch- and https://github.com/hackiey/QAnet-pytorch.
2. For a TensorFlow implementation, please refer to https://github.com/NLPLearn/QANet.
