# AI in Cybersecurity and Cloud Computing

Lecture slides and labs for course **314341: AI in Cybersecurity and Cloud Computing**,
Faculty of Information Technology, Ajloun National University, Jordan.

**Instructor:** Dr. Mohammed Tawfik, Head of the Department of Cyber Security and Cloud Computing ·
ORCID [0009-0004-7622-5991](https://orcid.org/0009-0004-7622-5991)

The course is written for students of cyber security, computer science, software engineering and AI who meet
artificial intelligence for the first time. It is applied: no mathematics beyond simple division, and every
concept is shown on a security case (phishing, malware, intrusions, account takeover, fraud, cloud attacks).
Each concept slide has a definition, an explanation, a drawn example and what it means for a SOC analyst.

## Chapters

| # | Chapter | Slides (PowerPoint) | PDF |
|---|---------|--------------------|-----|
| 1a | What Is AI and Machine Learning | [pptx](slides/Chapter1a_What_Is_AI_and_ML.pptx) | [pdf](slides/Chapter1a_What_Is_AI_and_ML.pdf) |
| 1b | Deep Learning, Generative AI, Agents and Uses | [pptx](slides/Chapter1b_DL_GenAI_Agents_and_Uses.pptx) | [pdf](slides/Chapter1b_DL_GenAI_Agents_and_Uses.pdf) |
| 2 | AI in Cybersecurity: uses, cases and the data behind them | [pptx](slides/Chapter2_AI_in_Cybersecurity.pptx) | [pdf](slides/Chapter2_AI_in_Cybersecurity.pdf) |
| 3 | Security Data Processing: from logs to a ready dataset | [pptx](slides/Chapter3_Security_Data_Processing.pptx) | [pdf](slides/Chapter3_Security_Data_Processing.pdf) |
| 4 | Training and Testing an AI Detector (with a complete Python example) | [pptx](slides/Chapter4_Training_and_Testing.pptx) | [pdf](slides/Chapter4_Training_and_Testing.pdf) |
| 5 | Deep Learning, Large Language Models and AI Agents | [pptx](slides/Chapter5_Deep_Learning_LLMs_and_Agents.pptx) | [pdf](slides/Chapter5_Deep_Learning_LLMs_and_Agents.pdf) |
| 6 | AI and Cloud Security, and Attacks on LLMs | [pptx](slides/Chapter6_Cloud_Security_and_LLM_Attacks.pptx) | [pdf](slides/Chapter6_Cloud_Security_and_LLM_Attacks.pdf) |

Speaker notes in every PowerPoint file contain the explanation, answers to class activities and sources.

## Labs

The **[Lab Manual](labs/Lab_Manual_314341.pdf)** ([docx](labs/Lab_Manual_314341.docx)) has 18 labs. Each lab gives the objective,
tools, data, numbered steps, questions and what to hand in. No-code labs use [Orange Data Mining](https://orangedatamining.com)
and free web tools; Python labs run in Google Colab in the browser, with nothing to install.

| Lab | Title | Chapter | Tool | Notebook |
|-----|-------|---------|------|----------|
| 1 | Meet AI: train your first model | 1 | Teachable Machine |  |
| 2 | A first look at security data | 2 | Orange |  |
| 3 | A phishing-website detector with a decision tree | 2 | Orange |  |
| 4 | An SMS spam detector that reads text | 2 | Orange (Text add-on) |  |
| 5 | A phishing e-mail detector | 2 | Python | [Lab05_Phishing_Email_Text.ipynb](labs/Lab05_Phishing_Email_Text.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab05_Phishing_Email_Text.ipynb) |
| 6 | Finding SSH brute-force attacks in real logs | 3 | Python | [Lab06_SSH_Brute_Force_Logs.ipynb](labs/Lab06_SSH_Brute_Force_Logs.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab06_SSH_Brute_Force_Logs.ipynb) |
| 7 | Preparing intrusion data | 3 | Orange |  |
| 8 | Cleaning and preparing a login table | 3 | Python | [Lab08_Cleaning_Login_Data.ipynb](labs/Lab08_Cleaning_Login_Data.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab08_Cleaning_Login_Data.ipynb) |
| 9 | Train, test and judge an IDS | 4 | Orange |  |
| 10 | Complete example: an AI intrusion detector | 4 | Python | [Chapter4_Complete_Example.ipynb](labs/Chapter4_Complete_Example.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Chapter4_Complete_Example.ipynb) |
| 11 | Card fraud and the accuracy trap | 4 | Python | [Lab11_Fraud_Imbalanced_Data.ipynb](labs/Lab11_Fraud_Imbalanced_Data.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab11_Fraud_Imbalanced_Data.ipynb) |
| 12 | Android malware detection with a random forest | 4 | Python | [Lab12_Android_Malware.ipynb](labs/Lab12_Android_Malware.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab12_Android_Malware.ipynb) |
| 13 | Inside a neural network | 5 | TensorFlow Playground, Orange |  |
| 14 | Generative AI as a SOC assistant | 5 | Any chatbot |  |
| 15 | Prompt injection with Gandalf | 5 | gandalf.lakera.ai |  |
| 16 | Investigating a cloud account with CloudTrail | 6 | Python | [Lab16_CloudTrail_Investigation.ipynb](labs/Lab16_CloudTrail_Investigation.ipynb) · [Open in Colab](https://colab.research.google.com/github/kmkholm/ai-cybersecurity-cloud-course/blob/main/labs/Lab16_CloudTrail_Investigation.ipynb) |
| 17 | Cloud misconfiguration: flaws.cloud | 6 | Browser |  |
| 18 | Threat-modelling a university chatbot | 6 | OWASP Top 10 for LLM Applications |  |

Data made for the course (invented records) is in [`labs/data`](labs/data): `dirty_logins.csv` (Lab 8) and
`cloudtrail_events.json` (Lab 16); the notebooks load it from this repository. The other labs use public datasets:
[Phishing Email Detection](https://www.kaggle.com/datasets/subhajournal/phishingemails),
[Web Page Phishing Detection](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset),
[SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset),
[Network Intrusion Detection](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection),
[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud),
[Android Malware Dataset for Machine Learning](https://www.kaggle.com/datasets/shashwatwork/android-malware-dataset-for-machine-learning)
and [Loghub](https://github.com/logpai/loghub) OpenSSH logs.
The Chapter 4 example is also available as a plain script: [`labs/Chapter4_Complete_Example.py`](labs/Chapter4_Complete_Example.py).

## Note

Names, IP addresses (documentation ranges 203.0.113.0/24 and 198.51.100.0/24) and numbers in the examples are
invented for teaching unless a slide says otherwise. Practise attacks only on systems you own or are allowed to test.

© Dr. Mohammed Tawfik, Ajloun National University.
