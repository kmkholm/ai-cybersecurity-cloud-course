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

- [`labs/Chapter4_Complete_Example.ipynb`](labs/Chapter4_Complete_Example.ipynb): train and test an AI intrusion
  detector in Python (pandas, scikit-learn). Open it in [Google Colab](https://colab.research.google.com), upload
  `Train_data.csv` from the Kaggle dataset
  [Network Intrusion Detection](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection), and run the cells.
- The same code as a plain script: [`labs/Chapter4_Complete_Example.py`](labs/Chapter4_Complete_Example.py).
- No-code labs use [Orange Data Mining](https://orangedatamining.com); the steps are on the lab slides of each chapter.

Public datasets used in the slides: Kaggle Phishing Email Detection, Web Page Phishing Detection, SMS Spam Collection,
Credit Card Fraud Detection, Network Intrusion Detection, and Loghub OpenSSH logs (links on the "Practice" slides).

## Note

Names, IP addresses (documentation ranges 203.0.113.0/24 and 198.51.100.0/24) and numbers in the examples are
invented for teaching unless a slide says otherwise. Practise attacks only on systems you own or are allowed to test.

© Dr. Mohammed Tawfik, Ajloun National University.
