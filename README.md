# CSVC-Net: Code-Switched Voice Command Classification using Deep CNN-LSTM Network

Colloquial Bengali has adopted many English words due to colonial influence. In conversational Bengali, it is quite common to speak in a mixture of English and Bengali, a phenomenon termed Code-switching (CS). To build a Voice Command Classifier in this era, when the usage of CS is ever-increasing, it is often necessary to map a single base command to its many different variants - spoken in multiple mixtures of languages. The works done with Bengali Speech have been primarily focused on single word classification and mostly incompetent to understand the complex semantic relationships displayed in sentences. This paper proposes 'CSVC-Net', a CNN-LSTM based architecture for classifying spoken commands containing code-switching between Bengali and English. To effectively reflect the scenario, it also presents a newly curated dataset named **"Banglish"** containing 3,840 audio files of spoken computer commands belonging to 11 classes and 64 variations in total. The proposed pipeline passes the input audio signal through a series of appropriate transformation and augmentation steps enabling the model to achieve an accuracy of 92.08\% on the curated dataset. Furthermore, the robustness of the proposed model has been justified by comparing compared with different architectures and tested under different noise levels with promising accuracy, which shows the applicability of the model in real-life scenarios.

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
Our proposed architecture is a CNN-LSTM model. It consists of three main components - a CNN block, a LSTM block and Time Distributed Dense Layers. To enhance the performance of the model, we also utilized Dropout and Batch Normalization layers in different parts. A detailed diagram of our model is as follows: [CSVC-Net.pdf](https://github.com/space-urchin/BVC-Net/files/6605139/CSVC-Net.pdf)


