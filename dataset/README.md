# Banglish
A Bilingual Dataset for Bangla and English Voice Commands

Colloquial Bangla has adopted many English words due to colonial influence. In conversational Bangla, it is quite common to speak in a mixture of English and Bangla. This phenomenon, prevalent in conversational language is known as code-switching (CS). CS is defined as the continuous alternation between two languages in a single conversation. Thus, in Bangla natural language processing, it is often necessary to map a single base command to its many different variants - spoken in multiple mixtures of English and Bangla. In order to facilitate this, we have curated a dataset centered around common browser commands.

## Dataset Structure
Our curated dataset contains 3840 audio samples (.wav files) obtained from 30 female and 30 male contributors. The audio files have undergone 1 form of pre-processing - extracting sound envelope. This pre-processing step simply removes regions of silence or "dead zones" usually present in the beginning and end of the audio file. The voice commands are divided into eleven classes. Ten classes define ten different commands, each with five intraclass variations representing five different ways of speaking the same command. One extra class termed “Miscellaneous Examples” consists of 14 misspoken commands to offset the correctly spoken commands with some invalid ones. The classes are listed as follows:

* Close Tab (5 intraclass variations)
* Close Window (5 intraclass variations)
* Switch Tab (5 intraclass variations)
* Open New Tab (5 intraclass variations)
* Minimise Window (5 intraclass variations)
* Maximise Window (5 intraclass variations)
* Restore Up (5 intraclass variations)
* Restore Down (5 intraclass variations)
* Refresh (5 intraclass variations)
* Take Cursor to Search (5 intraclass variations)
* Miscellaneous Examples (14 misspoken commands)

## Naming Convention
The files are named as follows: \
**c <class_label> v <variaton_label> <male/female> <age_of_speaker> <first_name>**
> class_label: values from **001 - 011** to represent 11 classes \
> variation_label: values from **001 - 005** for classes 1 through 10, and values from **001 - 014** for class 11 \
> male/female: **m** for male, **f** for female \
> age_of_speaker: the age of the speaker \
> contributor_no: the serial number of contributor \
> Example: **c001v001f23contributor001**

## Commands
| V# |          Computer Command 1:         |            Close Tab            |
|:---:|:------------------------------------:|:-------------------------------:|
|     |       English Transliteration:       |         Bangla sentence         |
| 1   |         Ei Tab ta Close koro         |        এই ট্যাব টা ক্লোজ কর       |
| 2   | Ekhon jei Tab e achi eita Close koro | এখন যেই ট্যাব এ আছি এইটা ক্লোজ কর |
| 3   |          Ei Tab bondho koro          |          এই ট্যাব বন্ধ কর         |
| 4   | Ekhon jei Tab e achi ta bondho koro  |   এখন যেই ট্যাব এ আছি তা বন্ধ কর  |
| 5   |          Tab ta bondho koro          |          ট্যাব টা বন্ধ কর         |

| V# |            Computer Command 2:           |            Close Window            |
|:---:|:----------------------------------------:|:----------------------------------:|
|     | English Transliteration:                 | Bangla sentence                    |
| 1   | Ei Window ta Close koro                  | এই উইন্ডো  টা ক্লোজ  কর              |
| 2   | Ekhon jei Window te achi eita Close koro | এখন যেই উইন্ডো  এ আছি এইটা ক্লোজ  কর |
| 3   | Ei Window bondho koro                    | এই উইন্ডো  বন্ধ কর                   |
| 4   | Ekhon jei Window te achi ta bondho koro  | এখন যেই উইন্ডো  তে আছি তা বন্ধ কর    |
| 5  | Window ta bondho koro                    | উইন্ডো টা বন্ধ কর                    |

| V# |         Computer Command 3:         |            Switch Tab            |
|:---:|:-----------------------------------:|:--------------------------------:|
|     | English Transliteration:            | Bangla sentence                  |
| 1  | Ei Tab theke arek Tab e jao         | এই ট্যাব থেকে আরেক ট্যাব এ যাও     |
| 2  | Tab Switch koro                     | ট্যাব সুইচ  কর                     |
| 3  | Ei Tab theke arek Tab e Switch koro | এই ট্যাব থেকে আরেক ট্যাব এ সুইচ  কর |
| 4  | Arek Tab e jao                      | আরেক ট্যাব এ যাও                  |
| 5  | Arek Tab e switch koro              | আরেক ট্যাব এ সুইচ  কর              |

| V# |    Computer Command 4:   |      Open New Tab     |
|:---:|:------------------------:|:---------------------:|
|     | English Transliteration: | Bangla sentence       |
| 1  | Notun Tab khulo          | নতুন ট্যাব খুলো          |
| 2  | Arekta Tab khulo         | আরেকটা ট্যাব খুলো       |
| 3  | Arekta Tab Open koro     | আরেকটা ট্যাব ওপেন করো  |
| 4  | New Tab Open koro        | নিউ ট্যাব ওপেন করো     |
| 5  | Notun Tab Open koro      | নতুন ট্যাব ওপেন করো     |

| V# |              Computer Command 5:             |             Minimise Window             |
|:---:|:--------------------------------------------:|:---------------------------------------:|
|     | English Transliteration:                     | Bangla sentence                         |
| 1  | Window ta minimise koro                      | উইন্ডোটা মিনিমাইজ করো                    |
| 2  | Window ta niche namao                        | উইন্ডোটা নিচে নামাও                      |
| 3  | Jei Window ta khola ache oita niche namao    | যেই উইন্ডোটা খোলা আছে ঐটা নিচে নামাও     |
| 4  | Jei Window ta open ache oita minimise koro   | যেই উইন্ডো টা ওপেন আছে ঐটা মিনিমাইজ করো  |
| 5  | Jei Window ta khola ache oita minimise koro  | যেই উইন্ডো টা খোলা আছে ঐটা মিনিমাইজ করো  |

| V# |              Computer Command 6:             |              Maximise Window             |
|:---:|:--------------------------------------------:|:----------------------------------------:|
|     | English Transliteration:                     | Bangla sentence                          |
| 1  | Window ta maximise koro                      | উইন্ডোটা ম্যাক্সিমাইজ করো                   |
| 2  | Window ta upore uthao                        | উইন্ডোটা উপরে উঠাও                        |
| 3  | Jei Window ta niche namano oita upore uthao  | যেই উইন্ডোটা নিচে নামানো ওটা উপরে উঠাও    |
| 4  | Jei Window ta open ache oita maximise koro   | যেই উইন্ডো টা ওপেন আছে ঐটা ম্যাক্সিমাইজ করো |
| 5  | Jei Window ta khola ache oita maximise koro  | যেই উইন্ডো টা খোলা আছে ঐটা ম্যাক্সিমাইজ করো |

|     V#    |              Computer Command 7:              |              Restore Up              |
|:----------:|:---------------------------------------------:|:------------------------------------:|
|            | English Transliteration:                      | Bangla sentence                      |
| 1         | Window ta boro koro                           | উইন্ডোটা বড় করো                       |
| 2         | Ekhon jei Window ta khola ache oita boro koro | এখন যেই উইন্ডোটা খোলা আছে ওটা বড় করো  |
| 3         | Window ta ekhon boro koro                     | উইন্ডোটা এখন বড় করো                   |
| 4         | Choto theke boro koro window ta               | ছোট থেকে বড় করো উইন্ডোটা              |
| 5         | Window ta Restore Up koro                     | উইন্ডোটা রিস্টোর আপ করো                |

| V# |               Computer Command 8:              |              Restore Down             |
|:---:|:----------------------------------------------:|:-------------------------------------:|
|     | English Transliteration:                       | Bangla sentence                       |
| 1  | Window ta choto koro                           | উইন্ডোটা  ছোট করো                      |
| 2  | Ekhon jei Window ta khola ache oita choto koro | এখন যেই উইন্ডোটা খোলা আছে ওটা ছোট করো  |
| 3  | Window ta ekhon choto koro                     | উইন্ডোটা এখন ছোট করো                   |
| 4  | Boro theke choto koro window ta                | বড় থেকে ছোট করো উইন্ডোটা               |
| 5  | Window ta Restore Down koro                    | উইন্ডোটা রিস্টোর ডাউন করো               |

|   V#   |    Computer Command 9:   |       Refresh       |
|:-------:|:------------------------:|:-------------------:|
|         | English Transliteration: | Bangla sentence     |
| 1      | Page ta Refresh koro     | পেজটা  রিফ্রেশ করো   |
| 2      | Page ta abar load koro   | পেজটা আবার লোড করো  |
| 3      | Refresh koro             | রিফ্রেশ করো          |
| 4      | Page ta reload koro      | পেজটা রিলোড করো     |
| 5      | Reload koro              | রিলোড করো           |

| V# |    Computer Command 10:    |   Take Cursor to Search |
|:---:|:--------------------------:|:------------------------:|
|     | English Transliteration:   | Bangla sentence    |
| 1  | Cursor ta search e nao     | কার্সরটা সার্চে নাও        |
| 2  | URL Box e cursor ta nao    | ইউআরএল বক্সে কার্সরটা নাও  |
| 3  | Cursor ta search box e nao | কার্সরটা সার্চ বক্সে নাও    |
| 4  | Search box e cursor ta nao | সার্চ বক্সে কার্সরটা নাও    |
| 5  | Cursor ta URL box e nao    | কার্সরটা ইউআরএল বক্সে নাও  |

|           V#          |        Computer Command 11:       |     Miscellaneous Examples     |
|:----------------------:|:---------------------------------:|:------------------------------:|
|                        | English Transliteration:          | Bangla sentence                |
| 1                     | Window ta theke kom light ashche  | উইন্ডোটা থেকে কম লাইট আসছে      |
| 2                     | Ei Tab ta kaaj korche na          | এই ট্যাবটা কাজ করছে না          |
| 3                     | Niche theke upore box ta uthao    | নিচে থেকে উপরে বক্সটা উঠাও      |
| 4                     | Window theke box ta shorao        | উইন্ডো থেকে বক্সটা সরাও          |
| 5                     | Cursor ta niche theke upore uthao | কার্সরটা নিচে থেকে উপরে উঠাও    |
| 6                     | Copy paste koro                   | কপি পেস্ট করো                   |
| 7                     | Tab ta oidike shorao              | ট্যাবটা ঐদিকে সরাও              |
| 8                     | Cut kore niche nao                | কাট করে নিচে নাও               |
| 9                     | URL ta enter koro                 | ইউআরএল টা এন্টার করো            |
| 10                     | Ei window er URL ta copy koro     | এই উইন্ডোর ইউআরএলটা কপি করো     |
| 11                     | Cursor ta niche namao             | কার্সরটা নিচে নামাও             |
| 12                     | Ei Tab theke baamer tab e jao     | এই ট্যাব থেকে বামের ট্যাব এ যাও  |
| 13                     | Ei Tab theke daaner tab e jao     | এই ট্যাব থেকে ডানের ট্যাব এ যাও  |
| 14                     | Notun window khulo                | নতুন উইন্ডো খুলো                  |
