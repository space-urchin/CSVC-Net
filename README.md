# BVC-Net: Bilingual Voice Command Detection using Deep LSTM Networks

Colloquial Bengali has adopted many English words due to colonial influence. In conversational Bengali, it is quite common to speak in a mixture of English and Bengali. Thus, in Bengali Automatic Speech Recognition (ASR), it is often necessary to map a single base command to its many different variants - spoken in multiple mixtures of English and Bengali. The work done in this domain has been primarily focused on single word classification and is unable to understand the complex semantic relationships displayed in sentences. This paper presents a newly curated dataset which consists of 10 different computer commands. This dataset contains not only single sentence commands spoken in a mixture of English and Bengali but also multiple English-Bengali variations of each command. In addition, it also proposes a bilingual LSTM based solution to consider such variance in spoken computer commands. It has achieved 92\% training accuracy and 91.52\% test accuracy on the curated dataset. 

## Dataset Preparation
All audio samples are converted to the ‘.wav’ format, having a mono (single) channel, and sampled at 16kHz with a bitrate of 512kbps. The audio samples then pass through a series of feature extraction and data augmentation processes as mentioned below:

* Extract Sound Envelope
* Waveform Transforms
	- Pitch Shift
	- Time Stretch
	- Add Gaussian Noise
* Extract MFCC features
* Spectrogram Transform
	- Frequency Mask


## Our Model Architecture
In order to establish a model that can generalise on our dataset, it is necessary to process the audio samples sequentially and then learn from them the complex semantic relationships present in each command. To achieve this, we have employed the use of Recurrent Neural Networks. There are several derivations of RNNs, such as Gated Recurrent Unit (GRU), unidirectional LSTM and bidirectional LSTM (BLSTM). GRUs and LSTMs are superior to traditional RNN and have similar performance. BLSTMs undoubtedly perform better than LSTMs; however, they are more computationally complex and expensive. Thus, we decided to settle on a unidirectional LSTM based model that provides both a lightweight and robust solution. 
