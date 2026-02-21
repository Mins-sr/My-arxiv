# arXiv Daily Digest - 2026-02-21

Total papers: 150

---

## cs.CL

**50 papers**

### 1. Sink-Aware Pruning for Diffusion Language Models

**Authors:** Aidar Myrzakhan, Tianyi Li, Bowei Guo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17664v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17664v1)

**Summary:** Diffusion Language Models (DLMs) incur high inference cost due to iterative denoising, motivating efficient pruning. Existing pruning heuristics largely inherited from autoregressive (AR) LLMs, typically preserve attention sink tokens because AR sinks serve as stable global anchors. We show that this assumption does not hold for DLMs: the attention-sink position exhibits substantially higher variance over the full generation trajectory (measured by how the dominant sink locations shift across ti...

---

### 2. CLEF HIPE-2026: Evaluating Accurate and Efficient Person-Place Relation Extraction from Multilingual Historical Texts

**Authors:** Juri Opitz, Corina Raclé, Emanuela Boros, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17663v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17663v1)

**Summary:** HIPE-2026 is a CLEF evaluation lab dedicated to person-place relation extraction from noisy, multilingual historical texts. Building on the HIPE-2020 and HIPE-2022 campaigns, it extends the series toward semantic relation extraction by targeting the task of identifying person--place associations in multiple languages and time periods. Systems are asked to classify relations of two types - $at$ ("Has the person ever been at this place?") and $isAt$ ("Is the person located at this place around pub...

---

### 3. What Language is This? Ask Your Tokenizer

**Authors:** Clara Meister, Ahmetcan Yavuz, Pietro Lesci, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17655v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17655v1)

**Summary:** Language Identification (LID) is an important component of many multilingual natural language processing pipelines, where it facilitates corpus curation, training data analysis, and cross-lingual evaluation of large language models. Despite near-perfect performance on high-resource languages, existing systems remain brittle in low-resource and closely related language settings. We introduce UniLID, a simple and efficient LID method based on the UnigramLM tokenization algorithm, leveraging its pr...

---

### 4. Differences in Typological Alignment in Language Models' Treatment of Differential Argument Marking

**Authors:** Iskar Deng, Nathalia Xu, Shane Steinert-Threlkeld

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17653v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17653v1)

**Summary:** Recent work has shown that language models (LMs) trained on synthetic corpora can exhibit typological preferences that resemble cross-linguistic regularities in human languages, particularly for syntactic phenomena such as word order. In this paper, we extend this paradigm to differential argument marking (DAM), a semantic licensing system in which morphological marking depends on semantic prominence. Using a controlled synthetic learning method, we train GPT-2 models on 18 corpora implementing ...

---

### 5. Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting

**Authors:** Xiaohan Zhao, Zhaoyi Li, Yaxin Luo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17645v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17645v1)

**Summary:** Black-box adversarial attacks on Large Vision-Language Models (LVLMs) are challenging due to missing gradients and complex multimodal boundaries. While prior state-of-the-art transfer-based approaches like M-Attack perform well using local crop-level matching between source and target images, we find this induces high-variance, nearly orthogonal gradients across iterations, violating coherent local alignment and destabilizing optimization. We attribute this to (i) ViT translation sensitivity tha...

---

### 6. Unmasking the Factual-Conceptual Gap in Persian Language Models

**Authors:** Alireza Sakhaeirad, Ali Ma'manpoosh, Arshia Hemmat

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17623v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17623v1)

**Summary:** While emerging Persian NLP benchmarks have expanded into pragmatics and politeness, they rarely distinguish between memorized cultural facts and the ability to reason about implicit social norms. We introduce DivanBench, a diagnostic benchmark focused on superstitions and customs, arbitrary, context-dependent rules that resist simple logical deduction. Through 315 questions across three task types (factual retrieval, paired scenario verification, and situational reasoning), we evaluate seven Per...

---

### 7. The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?

**Authors:** Jayadev Billa

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17598v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17598v1)

**Summary:** Current speech LLMs largely perform implicit ASR: on tasks solvable from a transcript, they are behaviorally and mechanistically equivalent to simple Whisper$\to$LLM cascades. We show this through matched-backbone testing across four speech LLMs and six tasks, controlling for the LLM backbone for the first time. Ultravox is statistically indistinguishable from its matched cascade ($κ{=}0.93$); logit lens reveals literal text emerging in hidden states; LEACE concept erasure confirms text represen...

---

### 8. Modeling Distinct Human Interaction in Web Agents

**Authors:** Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17588v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17588v1)

**Summary:** Despite rapid progress in autonomous web agents, human involvement remains essential for shaping preferences and correcting agent behavior as tasks unfold. However, current agentic systems lack a principled understanding of when and why humans intervene, often proceeding autonomously past critical decision points or requesting unnecessary confirmation. In this work, we introduce the task of modeling human intervention to support collaborative web task execution. We collect CowCorpus, a dataset o...

---

### 9. KLong: Training LLM Agent for Extremely Long-horizon Tasks

**Authors:** Yue Liu, Zhiyuan Hu, Flood Sung, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17547v1)

**Summary:** This paper introduces KLong, an open-source LLM agent trained to solve extremely long-horizon tasks. The principle is to first cold-start the model via trajectory-splitting SFT, then scale it via progressive RL training. Specifically, we first activate basic agentic abilities of a base model with a comprehensive SFT recipe. Then, we introduce Research-Factory, an automated pipeline that generates high-quality training data by collecting research papers and constructing evaluation rubrics. Using ...

---

### 10. Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning

**Authors:** Jyotin Goel, Souvik Maji, Pratik Mazumder

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17546v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17546v1)

**Summary:** Instruction-following language models are trained to be helpful and safe, yet their safety behavior can deteriorate under benign fine-tuning and worsen under adversarial updates. Existing defenses often offer limited protection or force a trade-off between safety and utility. We introduce a training framework that adapts regularization in response to safety risk, enabling models to remain aligned throughout fine-tuning. To estimate safety risk at training time, we explore two distinct approaches...

---

### 11. Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability

**Authors:** Shashank Aggarwal, Ram Vikas Mishra, Amit Awekar

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17544v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17544v1)

**Summary:** In multi-agent IR pipelines for tasks such as search and ranking, LLM-based agents exchange intermediate reasoning in terms of Chain-of-Thought (CoT) with each other. Current CoT evaluation narrowly focuses on target task accuracy. However, this metric fails to assess the quality or utility of the reasoning process itself. To address this limitation, we introduce two novel measures: reusability and verifiability. We decouple CoT generation from execution using a Thinker-Executor framework. Reusa...

---

### 12. Using LLMs for Knowledge Component-level Correctness Labeling in Open-ended Coding Problems

**Authors:** Zhangqi Duan, Arnav Kankaria, Dhruv Kartik, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17542v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17542v1)

**Summary:** Fine-grained skill representations, commonly referred to as knowledge components (KCs), are fundamental to many approaches in student modeling and learning analytics. However, KC-level correctness labels are rarely available in real-world datasets, especially for open-ended programming tasks where solutions typically involve multiple KCs simultaneously. Simply propagating problem-level correctness to all associated KCs obscures partial mastery and often leads to poorly fitted learning curves. To...

---

### 13. The Anxiety of Influence: Bloom Filters in Transformer Attention Heads

**Authors:** Peter Balogh

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17526v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17526v1)

**Summary:** Some transformer attention heads appear to function as membership testers, dedicating themselves to answering the question "has this token appeared before in the context?" We identify these heads across four language models (GPT-2 small, medium, and large; Pythia-160M) and show that they form a spectrum of membership-testing strategies. Two heads (L0H1 and L0H5 in GPT-2 small) function as high-precision membership filters with false positive rates of 0-4\% even at 180 unique context tokens -- we...

---

### 14. Bridging the Domain Divide: Supervised vs. Zero-Shot Clinical Section Segmentation from MIMIC-III to Obstetrics

**Authors:** Baris Karacan, Barbara Di Eugenio, Patrick Thornton

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17513v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17513v1)

**Summary:** Clinical free-text notes contain vital patient information. They are structured into labelled sections; recognizing these sections has been shown to support clinical decision-making and downstream NLP tasks. In this paper, we advance clinical section segmentation through three key contributions. First, we curate a new de-identified, section-labeled obstetrics notes dataset, to supplement the medical domains covered in public corpora such as MIMIC-III, on which most existing segmentation approach...

---

### 15. What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data

**Authors:** Dimitri Staufer, Kirsten Morehouse

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17483v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17483v1)

**Summary:** Large language models (LLMs), and conversational agents based on them, are exposed to personal data (PD) during pre-training and during user interactions. Prior work shows that PD can resurface, yet users lack insight into how strongly models associate specific information to their identity. We audit PD across eight LLMs (3 open-source; 5 API-based, including GPT-4o), introduce LMP2 (Language Model Privacy Probe), a human-centered, privacy-preserving audit tool refined through two formative stud...

---

### 16. Small LLMs for Medical NLP: a Systematic Analysis of Few-Shot, Constraint Decoding, Fine-Tuning and Continual Pre-Training in Italian

**Authors:** Pietro Ferrazzi, Mattia Franzin, Alberto Lavelli, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17475v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17475v1)

**Summary:** Large Language Models (LLMs) consistently excel in diverse medical Natural Language Processing (NLP) tasks, yet their substantial computational requirements often limit deployment in real-world healthcare settings. In this work, we investigate whether "small" LLMs (around one billion parameters) can effectively perform medical tasks while maintaining competitive accuracy. We evaluate models from three major families-Llama-3, Gemma-3, and Qwen3-across 20 clinical NLP tasks among Named Entity Reco...

---

### 17. Auditing Reciprocal Sentiment Alignment: Inversion Risk, Dialect Representation and Intent Misalignment in Transformers

**Authors:** Nusrat Jahan Lia, Shubhashis Roy Dipta

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17469v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17469v1)

**Summary:** The core theme of bidirectional alignment is ensuring that AI systems accurately understand human intent and that humans can trust AI behavior. However, this loop fractures significantly across language barriers. Our research addresses Cross-Lingual Sentiment Misalignment between Bengali and English by benchmarking four transformer architectures. We reveal severe safety and representational failures in current alignment paradigms. We demonstrate that compressed model (mDistilBERT) exhibits 28.7%...

---

### 18. PEACE 2.0: Grounded Explanations and Counter-Speech for Combating Hate Expressions

**Authors:** Greta Damo, Stéphane Petiot, Elena Cabrio, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17467v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17467v1)

**Summary:** The increasing volume of hate speech on online platforms poses significant societal challenges. While the Natural Language Processing community has developed effective methods to automatically detect the presence of hate speech, responses to it, called counter-speech, are still an open challenge. We present PEACE 2.0, a novel tool that, besides analysing and explaining why a message is considered hateful or not, also generates a response to it. More specifically, PEACE 2.0 has three main new fun...

---

### 19. Entropy-Based Data Selection for Language Models

**Authors:** Hongming Li, Yang Liu, Chao Huang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17465v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17465v1)

**Summary:** Modern language models (LMs) increasingly require two critical resources: computational resources and data resources. Data selection techniques can effectively reduce the amount of training data required for fine-tuning LMs. However, their effectiveness is closely related to computational resources, which always require a high compute budget. Owing to the resource limitations in practical fine-tuning scenario, we systematically reveal the relationship between data selection and uncertainty estim...

---

### 20. ABCD: All Biases Come Disguised

**Authors:** Mateusz Nowak, Xavier Cadet, Peter Chin

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17445v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17445v1)

**Summary:** Multiple-choice question (MCQ) benchmarks have been a standard evaluation practice for measuring LLMs' ability to reason and answer knowledge-based questions. Through a synthetic NonsenseQA benchmark, we observe that different LLMs exhibit varying degrees of label-position-few-shot-prompt bias, where the model either uses the answer position, the label in front of the answer, the distributions of correct answers present in the few-shot prompt, or a combination of all to answer each MCQ question....

---

### 21. AIDG: Evaluating Asymmetry Between Information Extraction and Containment in Multi-Turn Dialogue

**Authors:** Adib Sakhawat, Fardeen Sadab, Rakin Shahriar

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17443v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17443v1)

**Summary:** Evaluating the strategic reasoning capabilities of Large Language Models (LLMs) requires moving beyond static benchmarks to dynamic, multi-turn interactions. We introduce AIDG (Adversarial Information Deduction Game), a game-theoretic framework that probes the asymmetry between information extraction (active deduction) and information containment (state maintenance) in dialogue. We propose two complementary tasks: AIDG-I, measuring pragmatic strategy in social deduction, and AIDG-II, measuring c...

---

### 22. Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study

**Authors:** Dylan Bouchard, Mohit Singh Chauhan, Viren Bajaj, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17431v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17431v1)

**Summary:** Uncertainty quantification has emerged as an effective approach to closed-book hallucination detection for LLMs, but existing methods are largely designed for short-form outputs and do not generalize well to long-form generation. We introduce a taxonomy for fine-grained uncertainty quantification in long-form LLM outputs that distinguishes methods by design choices at three stages: response decomposition, unit-level scoring, and response-level aggregation. We formalize several families of consis...

---

### 23. Evaluating Extremely Low-Resource Machine Translation: A Comparative Study of ChrF++ and BLEU Metrics

**Authors:** Sanjeev Kumar, Preethi Jyothi, Pushpak Bhattacharyya

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17425v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17425v1)

**Summary:** Evaluating machine translation (MT) quality in extremely low-resource language (ELRL) scenarios poses unique challenges, as widely used metrics such as BLEU, effective in high-resource settings, often misrepresent quality in data-scarce contexts. This work presents a comparative analysis of BLEU, an n-gram-based metric, and ChrF++, a character-based metric, for MT evaluation in ELRL settings. We examine how each metric responds to translation artifacts, including hallucinations, repetition, sour...

---

### 24. Diverse Word Choices, Same Reference: Annotating Lexically-Rich Cross-Document Coreference

**Authors:** Anastasia Zhukova, Felix Hamborg, Karsten Donnay, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17424v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17424v1)

**Summary:** Cross-document coreference resolution (CDCR) identifies and links mentions of the same entities and events across related documents, enabling content analysis that aggregates information at the level of discourse participants. However, existing datasets primarily focus on event resolution and employ a narrow definition of coreference, which limits their effectiveness in analyzing diverse and polarized news coverage where wording varies widely. This paper proposes a revised CDCR annotation scheme...

---

### 25. DAVE: A Policy-Enforcing LLM Spokesperson for Secure Multi-Document Data Sharing

**Authors:** René Brinkhege, Prahlad Menon

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17413v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17413v1)

**Summary:** In current inter-organizational data spaces, usage policies are enforced mainly at the asset level: a whole document or dataset is either shared or withheld. When only parts of a document are sensitive, providers who want to avoid leaking protected information typically must manually redact documents before sharing them, which is costly, coarse-grained, and hard to maintain as policies or partners change. We present DAVE, a usage policy-enforcing LLM spokesperson that answers questions over priv...

---

### 26. The Role of the Availability Heuristic in Multiple-Choice Answering Behaviour

**Authors:** Leonidas Zotos, Hedderik van Rijn, Malvina Nissim

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17377v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17377v1)

**Summary:** When students are unsure of the correct answer to a multiple-choice question (MCQ), guessing is common practice. The availability heuristic, proposed by A. Tversky and D. Kahneman in 1973, suggests that the ease with which relevant instances come to mind, typically operationalised by the mere frequency of exposure, can offer a mental shortcut for problems in which the test-taker does not know the exact answer. Is simply choosing the option that comes most readily to mind a good strategy for answ...

---

### 27. RPDR: A Round-trip Prediction-Based Data Augmentation Framework for Long-Tail Question Answering

**Authors:** Yiming Zhang, Siyue Zhang, Junbo Zhao, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17366v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17366v1)

**Summary:** Long-tail question answering presents significant challenges for large language models (LLMs) due to their limited ability to acquire and accurately recall less common knowledge. Retrieval-augmented generation (RAG) systems have shown great promise in mitigating this limitation by integrating external retrieval mechanisms. However, dense retrieval models often face the same difficulties when generalizing to rare or niche knowledge. In this study, we introduce RPDR, a novel data augmentation fram...

---

### 28. WebFAQ 2.0: A Multilingual QA Dataset with Mined Hard Negatives for Dense Retrieval

**Authors:** Michael Dinzinger, Laura Caspari, Ali Salman, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17327v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17327v1)

**Summary:** We introduce WebFAQ 2.0, a new version of the WebFAQ dataset, containing 198 million FAQ-based natural question-answer pairs across 108 languages. Compared to the previous version, it significantly expands multilingual coverage and the number of bilingual aligned QA pairs to over 14.3M, making it the largest FAQ-based resource. Unlike the original release, WebFAQ 2.0 uses a novel data collection strategy that directly crawls and extracts relevant web content, resulting in a substantially more di...

---

### 29. Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation

**Authors:** Bogdan Kostić, Conor Fallon, Julian Risch, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17316v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17316v1)

**Summary:** The rapid advancement of Large Language Models (LLMs) has established standardized evaluation benchmarks as the primary instrument for model comparison. Yet, their reliability is increasingly questioned due to sensitivity to shallow variations in input prompts. This paper examines how controlled, truth-conditionally equivalent lexical and syntactic perturbations affect the absolute performance and relative ranking of 23 contemporary LLMs across three benchmarks: MMLU, SQuAD, and AMEGA. We employ...

---

### 30. ArXiv-to-Model: A Practical Study of Scientific LM Training

**Authors:** Anuj Gupta

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17288v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17288v1)

**Summary:** While frontier large language models demonstrate strong reasoning and mathematical capabilities, the practical process of training domain-specialized scientific language models from raw sources remains under-documented. In this work, we present a detailed case study of training a 1.36B-parameter scientific language model directly from raw arXiv LaTeX sources spanning mathematics, computer science, and theoretical physics. We describe an end-to-end pipeline covering metadata filtering, archive va...

---

### 31. Representation Collapse in Machine Translation Through the Lens of Angular Dispersion

**Authors:** Evgeniia Tokarchuk, Maya K. Nachesa, Sergey Troshin, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17287v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17287v1)

**Summary:** Modern neural translation models based on the Transformer architecture are known for their high performance, particularly when trained on high-resource datasets. A standard next-token prediction training strategy, while widely adopted in practice, may lead to overlooked artifacts such as representation collapse. Previous works have shown that this problem is especially pronounced in the representation of the deeper Transformer layers, where it often fails to efficiently utilize the geometric spa...

---

### 32. Towards Cross-lingual Values Assessment: A Consensus-Pluralism Perspective

**Authors:** Yukun Chen, Xinyu Zhang, Jialong Tang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17283v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17283v1)

**Summary:** While large language models (LLMs) have become pivotal to content safety, current evaluation paradigms primarily focus on detecting explicit harms (e.g., violence or hate speech), neglecting the subtler value dimensions conveyed in digital content. To bridge this gap, we introduce X-Value, a novel Cross-lingual Values Assessment Benchmark designed to evaluate LLMs' ability to assess deep-level values of content from a global perspective. X-Value consists of more than 5,000 QA pairs across 18 lan...

---

### 33. Quantifying and Mitigating Socially Desirable Responding in LLMs: A Desirability-Matched Graded Forced-Choice Psychometric Study

**Authors:** Kensuke Okada, Yui Furukawa, Kyosuke Bunji

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17262v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17262v1)

**Summary:** Human self-report questionnaires are increasingly used in NLP to benchmark and audit large language models (LLMs), from persona consistency to safety and bias assessments. Yet these instruments presume honest responding; in evaluative contexts, LLMs can instead gravitate toward socially preferred answers-a form of socially desirable responding (SDR)-biasing questionnaire-derived scores and downstream conclusions. We propose a psychometric framework to quantify and mitigate SDR in questionnaire-b...

---

### 34. Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy

**Authors:** Bianca Raimondi, Maurizio Gabbrielli

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17229v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17229v1)

**Summary:** The black-box nature of Large Language Models necessitates novel evaluation frameworks that transcend surface-level performance metrics. This study investigates the internal neural representations of cognitive complexity using Bloom's Taxonomy as a hierarchical lens. By analyzing high-dimensional activation vectors from different LLMs, we probe whether different cognitive levels, ranging from basic recall (Remember) to abstract synthesis (Create), are linearly separable within the model's residu...

---

### 35. From Labor to Collaboration: A Methodological Experiment Using AI Agents to Augment Research Perspectives in Taiwan's Humanities and Social Sciences

**Authors:** Yi-Chih Huang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17221v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17221v1)

**Summary:** Generative AI is reshaping knowledge work, yet existing research focuses predominantly on software engineering and the natural sciences, with limited methodological exploration for the humanities and social sciences. Positioned as a "methodological experiment," this study proposes an AI Agent-based collaborative research workflow (Agentic Workflow) for humanities and social science research. Taiwan's Claude.ai usage data (N = 7,729 conversations, November 2025) from the Anthropic Economic Index ...

---

### 36. What Makes a Good Doctor Response? An Analysis on a Romanian Telemedicine Platform

**Authors:** Adrian Cosma, Cosmin Dumitrache, Emilian Radoi

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17194v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17194v1)

**Summary:** Text-based telemedicine has become a common mode of care, requiring clinicians to deliver medical advice clearly and effectively in writing. As platforms increasingly rely on patient ratings and feedback, clinicians face growing pressure to maintain satisfaction scores, even though these evaluations often reflect communication quality more than clinical accuracy. We analyse patient satisfaction signals in Romanian text-based telemedicine. Using a sample of 77,334 anonymised patient question--doc...

---

### 37. The Emergence of Lab-Driven Alignment Signatures: A Psychometric Framework for Auditing Latent Bias and Compounding Risk in Generative AI

**Authors:** Dusan Bosnjakovic

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17127v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17127v1)

**Summary:** As Large Language Models (LLMs) transition from standalone chat interfaces to foundational reasoning layers in multi-agent systems and recursive evaluation loops (LLM-as-a-judge), the detection of durable, provider-level behavioral signatures becomes a critical requirement for safety and governance. Traditional benchmarks measure transient task accuracy but fail to capture stable, latent response policies -- the ``prevailing mindsets'' embedded during training and alignment that outlive individu...

---

### 38. Projective Psychological Assessment of Large Multimodal Models Using Thematic Apperception Tests

**Authors:** Anton Dzega, Aviad Elyashar, Ortal Slobodin, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17108v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17108v1)

**Summary:** Thematic Apperception Test (TAT) is a psychometrically grounded, multidimensional assessment framework that systematically differentiates between cognitive-representational and affective-relational components of personality-like functioning. This test is a projective psychological framework designed to uncover unconscious aspects of personality. This study examines whether the personality traits of Large Multimodal Models (LMMs) can be assessed through non-language-based modalities, using the So...

---

### 39. BankMathBench: A Benchmark for Numerical Reasoning in Banking Scenarios

**Authors:** Yunseung Lee, Subin Kim, Youngjun Kwak, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17072v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17072v1)

**Summary:** Large language models (LLMs)-based chatbots are increasingly being adopted in the financial domain, particularly in digital banking, to handle customer inquiries about products such as deposits, savings, and loans. However, these models still exhibit low accuracy in core banking computations-including total payout estimation, comparison of products with varying interest rates, and interest calculation under early repayment conditions. Such tasks require multi-step numerical reasoning and context...

---

### 40. Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression

**Authors:** Akira Sakai, Yuma Ichikawa

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17063v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17063v1)

**Summary:** Sub-bit model compression seeks storage below one bit per weight; as magnitudes are aggressively compressed, the sign bit becomes a fixed-cost bottleneck. Across Transformers, CNNs, and MLPs, learned sign matrices resist low-rank approximation and are spectrally indistinguishable from an i.i.d. Rademacher baseline. Despite this apparent randomness, most weights retain their initialization signs; flips primarily occur via rare near-zero boundary crossings, suggesting that sign-pattern randomness ...

---

### 41. ALPS: A Diagnostic Challenge Set for Arabic Linguistic & Pragmatic Reasoning

**Authors:** Hussein S. Al-Olimat, Ahmad Alshareef

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17054v1)

**Summary:** While recent Arabic NLP benchmarks focus on scale, they often rely on synthetic or translated data which may benefit from deeper linguistic verification. We introduce ALPS (Arabic Linguistic & Pragmatic Suite), a native, expert-curated diagnostic challenge set probing Deep Semantics and Pragmatics, capabilities that complement specialized large-scale benchmarks. While broad-coverage benchmarks prioritize scale and multi-task coverage, ALPS targets the depth of linguistic understanding through 53...

---

### 42. RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models

**Authors:** Yunseok Han, Yejoon Lee, Jaeyoung Do

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17053v1)

**Summary:** Large Reasoning Models (LRMs) exhibit strong performance, yet often produce rationales that sound plausible but fail to reflect their true decision process, undermining reliability and trust. We introduce a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy. To o...

---

### 43. Evaluating Cross-Lingual Classification Approaches Enabling Topic Discovery for Multilingual Social Media Data

**Authors:** Deepak Uniyal, Md Abul Bashar, Richi Nayak

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17051v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17051v1)

**Summary:** Analysing multilingual social media discourse remains a major challenge in natural language processing, particularly when large-scale public debates span across diverse languages. This study investigates how different approaches for cross-lingual text classification can support reliable analysis of global conversations. Using hydrogen energy as a case study, we analyse a decade-long dataset of over nine million tweets in English, Japanese, Hindi, and Korean (2013--2022) for topic discovery. The ...

---

### 44. Large Language Models Persuade Without Planning Theory of Mind

**Authors:** Jared Moore, Rasmus Overmark, Ned Cooper, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17045v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17045v1)

**Summary:** A growing body of work attempts to evaluate the theory of mind (ToM) abilities of humans and large language models (LLMs) using static, non-interactive question-and-answer benchmarks. However, theoretical work in the field suggests that first-personal interaction is a crucial part of ToM and that such predictive, spectatorial tasks may fail to evaluate it. We address this gap with a novel ToM task that requires an agent to persuade a target to choose one of three policy proposals by strategicall...

---

### 45. ReIn: Conversational Error Recovery with Reasoning Inception

**Authors:** Takyoung Kim, Jinseok Nam, Chandrayee Basu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17022v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17022v1)

**Summary:** Conversational agents powered by large language models (LLMs) with tool integration achieve strong performance on fixed task-oriented dialogue datasets but remain vulnerable to unanticipated, user-induced errors. Rather than focusing on error prevention, this work focuses on error recovery, which necessitates the accurate diagnosis of erroneous dialogue contexts and execution of proper recovery plans. Under realistic constraints precluding model fine-tuning or prompt modification due to signific...

---

### 46. Arcee Trinity Large Technical Report

**Authors:** Varun Singh, Lucas Krauss, Sami Jaghouar, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17004v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17004v1)

**Summary:** We present the technical report for Arcee Trinity Large, a sparse Mixture-of-Experts model with 400B total parameters and 13B activated per token. Additionally, we report on Trinity Nano and Trinity Mini, with Trinity Nano having 6B total parameters with 1B activated per token, Trinity Mini having 26B total parameters with 3B activated per token. The models' modern architecture includes interleaved local and global attention, gated attention, depth-scaled sandwich norm, and sigmoid routing for M...

---

### 47. Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History

**Authors:** Serin Kim, Sangam Lee, Dongha Lee

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17003v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17003v1)

**Summary:** Large language models have advanced web agents, yet current agents lack personalization capabilities. Since users rarely specify every detail of their intent, practical web agents must be able to interpret ambiguous queries by inferring user preferences and contexts. To address this challenge, we present Persona2Web, the first benchmark for evaluating personalized web agents on the real open web, built upon the clarify-to-personalize principle, which requires agents to resolve ambiguity based on...

---

### 48. Sonar-TS: Search-Then-Verify Natural Language Querying for Time Series Databases

**Authors:** Zhao Tan, Yiji Zhao, Shiyu Wang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17001v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17001v1)

**Summary:** Natural Language Querying for Time Series Databases (NLQ4TSDB) aims to assist non-expert users retrieve meaningful events, intervals, and summaries from massive temporal records. However, existing Text-to-SQL methods are not designed for continuous morphological intents such as shapes or anomalies, while time series models struggle to handle ultra-long histories. To address these challenges, we propose Sonar-TS, a neuro-symbolic framework that tackles NLQ4TSDB via a Search-Then-Verify pipeline. ...

---

### 49. Exploring LLMs for User Story Extraction from Mockups

**Authors:** Diego Firmenich, Leandro Antonelli, Bruno Pazos, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.16997v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16997v1)

**Summary:** User stories are one of the most widely used artifacts in the software industry to define functional requirements. In parallel, the use of high-fidelity mockups facilitates end-user participation in defining their needs. In this work, we explore how combining these techniques with large language models (LLMs) enables agile and automated generation of user stories from mockups. To this end, we present a case study that analyzes the ability of LLMs to extract user stories from high-fidelity mockup...

---

### 50. Characterizing the Predictive Impact of Modalities with Supervised Latent-Variable Modeling

**Authors:** Divyam Madaan, Sumit Chopra, Kyunghyun Cho

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.16979v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16979v1)

**Summary:** Despite the recent success of Multimodal Large Language Models (MLLMs), existing approaches predominantly assume the availability of multiple modalities during training and inference. In practice, multimodal data is often incomplete because modalities may be missing, collected asynchronously, or available only for a subset of examples. In this work, we propose PRIMO, a supervised latent-variable imputation model that quantifies the predictive impact of any missing modality within the multimodal ...

---

## cs.LG

**50 papers**

### 1. Sink-Aware Pruning for Diffusion Language Models

**Authors:** Aidar Myrzakhan, Tianyi Li, Bowei Guo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17664v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17664v1)

**Summary:** Diffusion Language Models (DLMs) incur high inference cost due to iterative denoising, motivating efficient pruning. Existing pruning heuristics largely inherited from autoregressive (AR) LLMs, typically preserve attention sink tokens because AR sinks serve as stable global anchors. We show that this assumption does not hold for DLMs: the attention-sink position exhibits substantially higher variance over the full generation trajectory (measured by how the dominant sink locations shift across ti...

---

### 2. MARS: Margin-Aware Reward-Modeling with Self-Refinement

**Authors:** Payel Bhattacharjee, Osvaldo Simeone, Ravi Tandon

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17658v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17658v1)

**Summary:** Reward modeling is a core component of modern alignment pipelines including RLHF and RLAIF, underpinning policy optimization methods including PPO and TRPO. However, training reliable reward models relies heavily on human-labeled preference data, which is costly and limited, motivating the use of data augmentation. Existing augmentation approaches typically operate at the representation or semantic level and remain agnostic to the reward model's estimation difficulty. In this paper, we propose M...

---

### 3. Mine and Refine: Optimizing Graded Relevance in E-commerce Search Retrieval

**Authors:** Jiaqi Xi, Raghav Saboo, Luming Chen, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17654v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17654v1)

**Summary:** We propose a two-stage "Mine and Refine" contrastive training framework for semantic text embeddings to enhance multi-category e-commerce search retrieval. Large scale e-commerce search demands embeddings that generalize to long tail, noisy queries while adhering to scalable supervision compatible with product and policy constraints. A practical challenge is that relevance is often graded: users accept substitutes or complements beyond exact matches, and production systems benefit from clear sep...

---

### 4. Multi-Round Human-AI Collaboration with User-Specified Requirements

**Authors:** Sima Noorani, Shayan Kiyani, Hamed Hassani, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17646v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17646v1)

**Summary:** As humans increasingly rely on multiround conversational AI for high stakes decisions, principled frameworks are needed to ensure such interactions reliably improve decision quality. We adopt a human centric view governed by two principles: counterfactual harm, ensuring the AI does not undermine human strengths, and complementarity, ensuring it adds value where the human is prone to err. We formalize these concepts via user defined rules, allowing users to specify exactly what harm and complemen...

---

### 5. Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting

**Authors:** Xiaohan Zhao, Zhaoyi Li, Yaxin Luo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17645v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17645v1)

**Summary:** Black-box adversarial attacks on Large Vision-Language Models (LVLMs) are challenging due to missing gradients and complex multimodal boundaries. While prior state-of-the-art transfer-based approaches like M-Attack perform well using local crop-level matching between source and target images, we find this induces high-variance, nearly orthogonal gradients across iterations, violating coherent local alignment and destabilizing optimization. We attribute this to (i) ViT translation sensitivity tha...

---

### 6. A.R.I.S.: Automated Recycling Identification System for E-Waste Classification Using Deep Learning

**Authors:** Dhruv Talwar, Harsh Desai, Wendong Yin, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17642v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17642v1)

**Summary:** Traditional electronic recycling processes suffer from significant resource loss due to inadequate material separation and identification capabilities, limiting material recovery. We present A.R.I.S. (Automated Recycling Identification System), a low-cost, portable sorter for shredded e-waste that addresses this efficiency gap. The system employs a YOLOx model to classify metals, plastics, and circuit boards in real time, achieving low inference latency with high detection accuracy. Experimental...

---

### 7. FAMOSE: A ReAct Approach to Automated Feature Discovery

**Authors:** Keith Burghardt, Jienan Liu, Sadman Sakib, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17641v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17641v1)

**Summary:** Feature engineering remains a critical yet challenging bottleneck in machine learning, particularly for tabular data, as identifying optimal features from an exponentially large feature space traditionally demands substantial domain expertise. To address this challenge, we introduce FAMOSE (Feature AugMentation and Optimal Selection agEnt), a novel framework that leverages the ReAct paradigm to autonomously explore, generate, and refine features while integrating feature selection and evaluation...

---

### 8. Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting

**Authors:** Xinghong Fu, Yanhong Li, Georgios Papaioannou, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17634v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17634v1)

**Summary:** Learning time series foundation models has been shown to be a promising approach for zero-shot time series forecasting across diverse time series domains. Insofar as scaling has been a critical driver of performance of foundation models in other modalities such as language and vision, much recent work on time series foundation modeling has focused on scaling. This has resulted in time series foundation models with hundreds of millions of parameters that are, while performant, inefficient and exp...

---

### 9. When to Trust the Cheap Check: Weak and Strong Verification for Reasoning

**Authors:** Shayan Kiyani, Sima Noorani, George Pappas, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17633v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17633v1)

**Summary:** Reasoning with LLMs increasingly unfolds inside a broader verification loop. Internally, systems use cheap checks, such as self-consistency or proxy rewards, which we call weak verification. Externally, users inspect outputs and steer the model through feedback until results are trustworthy, which we call strong verification. These signals differ sharply in cost and reliability: strong verification can establish trust but is resource-intensive, while weak verification is fast and scalable but no...

---

### 10. SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer

**Authors:** Nathan S. de Lara, Florian Shkurti

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17632v1)

**Summary:** Modern offline Reinforcement Learning (RL) methods find performant actor-critics, however, fine-tuning these actor-critics online with value-based RL algorithms typically causes immediate drops in performance. We provide evidence consistent with the hypothesis that, in the loss landscape, offline maxima for prior algorithms and online maxima are separated by low-performance valleys that gradient-based fine-tuning traverses. Following this, we present Score Matched Actor-Critic (SMAC), an offline...

---

### 11. Catastrophic Forgetting Resilient One-Shot Incremental Federated Learning

**Authors:** Obaidullah Zaland, Zulfiqar Ahmad Khan, Monowar Bhuyan

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17625v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17625v1)

**Summary:** Modern big-data systems generate massive, heterogeneous, and geographically dispersed streams that are large-scale and privacy-sensitive, making centralization challenging. While federated learning (FL) provides a privacy-enhancing training mechanism, it assumes a static data flow and learns a collaborative model over multiple rounds, making learning with \textit{incremental} data challenging in limited-communication scenarios. This paper presents One-Shot Incremental Federated Learning (OSI-FL)...

---

### 12. Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs

**Authors:** Luke Huang, Zhuoyang Zhang, Qinghao Hu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17616v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17616v1)

**Summary:** Reinforcement learning (RL) is widely used to improve large language models on reasoning tasks, and asynchronous RL training is attractive because it increases end-to-end throughput. However, for widely adopted critic-free policy-gradient methods such as REINFORCE and GRPO, high asynchrony makes the policy-gradient estimator markedly $\textbf{higher variance}$: training on stale rollouts creates heavy-tailed importance ratios, causing a small fraction of samples to dominate updates. This amplifi...

---

### 13. Guarding the Middle: Protecting Intermediate Representations in Federated Split Learning

**Authors:** Obaidullah Zaland, Sajib Mistry, Monowar Bhuyan

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17614v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17614v1)

**Summary:** Big data scenarios, where massive, heterogeneous datasets are distributed across clients, demand scalable, privacy-preserving learning methods. Federated learning (FL) enables decentralized training of machine learning (ML) models across clients without data centralization. Decentralized training, however, introduces a computational burden on client devices. U-shaped federated split learning (UFSL) offloads a fraction of the client computation to the server while keeping both data and labels on ...

---

### 14. Towards Anytime-Valid Statistical Watermarking

**Authors:** Baihe Huang, Eric Xu, Kannan Ramchandran, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17608v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17608v1)

**Summary:** The proliferation of Large Language Models (LLMs) necessitates efficient mechanisms to distinguish machine-generated content from human text. While statistical watermarking has emerged as a promising solution, existing methods suffer from two critical limitations: the lack of a principled approach for selecting sampling distributions and the reliance on fixed-horizon hypothesis testing, which precludes valid early stopping. In this paper, we bridge this gap by developing the first e-value-based ...

---

### 15. AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing

**Authors:** Jianda Du, Youran Sun, Haizhao Yang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17607v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17607v1)

**Summary:** PDEs are central to scientific and engineering modeling, yet designing accurate numerical solvers typically requires substantial mathematical expertise and manual tuning. Recent neural network-based approaches improve flexibility but often demand high computational cost and suffer from limited interpretability. We introduce \texttt{AutoNumerics}, a multi-agent framework that autonomously designs, implements, debugs, and verifies numerical solvers for general PDEs directly from natural language d...

---

### 16. Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery

**Authors:** Jowaria Khan, Anindya Sarkar, Yevgeniy Vorobeychik, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17605v1)

**Summary:** In many real-world settings, such as environmental monitoring, disaster response, or public health, with costly and difficult data collection and dynamic environments, strategically sampling from unobserved regions is essential for efficiently uncovering hidden targets under tight resource constraints. Yet, sparse and biased geospatial ground truth limits the applicability of existing learning-based methods, such as reinforcement learning. To address this, we propose a unified geospatial discove...

---

### 17. Asymptotic Smoothing of the Lipschitz Loss Landscape in Overparameterized One-Hidden-Layer ReLU Networks

**Authors:** Saveliy Baturin

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17596v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17596v1)

**Summary:** We study the topology of the loss landscape of one-hidden-layer ReLU networks under overparameterization. On the theory side, we (i) prove that for convex $L$-Lipschitz losses with an $\ell_1$-regularized second layer, every pair of models at the same loss level can be connected by a continuous path within an arbitrarily small loss increase $ε$ (extending a known result for the quadratic loss); (ii) obtain an asymptotic upper bound on the energy gap $ε$ between local and global minima that vanis...

---

### 18. Asymptotically Optimal Sequential Testing with Markovian Data

**Authors:** Alhad Sethi, Kavali Sofia Sagar, Shubhada Agrawal, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17587v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17587v1)

**Summary:** We study one-sided and $α$-correct sequential hypothesis testing for data generated by an ergodic Markov chain. The null hypothesis is that the unknown transition matrix belongs to a prescribed set $P$ of stochastic matrices, and the alternative corresponds to a disjoint set $Q$. We establish a tight non-asymptotic instance-dependent lower bound on the expected stopping time of any valid sequential test under the alternative. Our novel analysis improves the existing lower bounds, which are eithe...

---

### 19. Conditional Flow Matching for Continuous Anomaly Detection in Autonomous Driving on a Manifold-Aware Spectral Space

**Authors:** Antonio Guillen-Perez

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17586v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17586v1)

**Summary:** Safety validation for Level 4 autonomous vehicles (AVs) is currently bottlenecked by the inability to scale the detection of rare, high-risk long-tail scenarios using traditional rule-based heuristics. We present Deep-Flow, an unsupervised framework for safety-critical anomaly detection that utilizes Optimal Transport Conditional Flow Matching (OT-CFM) to characterize the continuous probability density of expert human driving behavior. Unlike standard generative approaches that operate in unstab...

---

### 20. Canonicalizing Multimodal Contrastive Representation Learning

**Authors:** Sharut Gupta, Sanyam Kansal, Stefanie Jegelka, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17584v1)

**Summary:** As models and data scale, independently trained networks often induce analogous notions of similarity. But, matching similarities is weaker than establishing an explicit correspondence between the representation spaces, especially for multimodal models, where consistency must hold not only within each modality, but also for the learned image-text coupling. We therefore ask: given two independently trained multimodal contrastive models (with encoders $(f, g)$ and $(\widetilde{f},\widetilde{g})$) ...

---

### 21. Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction

**Authors:** Lunjia Hu, Kevin Tian, Chutong Yang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17577v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17577v1)

**Summary:** Omniprediction is a learning problem that requires suboptimality bounds for each of a family of losses $\mathcal{L}$ against a family of comparator predictors $\mathcal{C}$. We initiate the study of omniprediction in a multiclass setting, where the comparator family $\mathcal{C}$ may be infinite. Our main result is an extension of the recent binary omniprediction algorithm of [OKK25] to the multiclass setting, with sample complexity (in statistical settings) or regret horizon (in online settings...

---

### 22. Be Wary of Your Time Series Preprocessing

**Authors:** Sofiane Ennadir, Tianze Wang, Oleg Smirnov, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17568v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17568v1)

**Summary:** Normalization and scaling are fundamental preprocessing steps in time series modeling, yet their role in Transformer-based models remains underexplored from a theoretical perspective. In this work, we present the first formal analysis of how different normalization strategies, specifically instance-based and global scaling, impact the expressivity of Transformer-based architectures for time series representation learning. We propose a novel expressivity framework tailored to time series, which q...

---

### 23. Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning

**Authors:** Hien Dang, Pratik Patil, Alessandro Rinaldo

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17565v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17565v1)

**Summary:** Self-distillation (SD) is the process of retraining a student on a mixture of ground-truth labels and the teacher's own predictions using the same architecture and training data. Although SD has been empirically shown to often improve generalization, its formal guarantees remain limited. We study SD for ridge regression in unconstrained setting in which the mixing weight $ξ$ may be outside the unit interval. Conditioned on the training data and without any distributional assumptions, we prove th...

---

### 24. Revisiting Weight Regularization for Low-Rank Continual Learning

**Authors:** Yaoyue Zheng, Yin Zhang, Joost van de Weijer, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17559v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17559v1)

**Summary:** Continual Learning (CL) with large-scale pre-trained models (PTMs) has recently gained wide attention, shifting the focus from training from scratch to continually adapting PTMs. This has given rise to a promising paradigm: parameter-efficient continual learning (PECL), where task interference is typically mitigated by assigning a task-specific module during training, such as low-rank adapters. However, weight regularization techniques, such as Elastic Weight Consolidation (EWC)-a key strategy i...

---

### 25. A Theoretical Framework for Modular Learning of Robust Generative Models

**Authors:** Corinna Cortes, Mehryar Mohri, Yutao Zhong

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17554v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17554v1)

**Summary:** Training large-scale generative models is resource-intensive and relies heavily on heuristic dataset weighting. We address two fundamental questions: Can we train Large Language Models (LLMs) modularly-combining small, domain-specific experts to match monolithic performance-and can we do so robustly for any data mixture, eliminating heuristic tuning? We present a theoretical framework for modular generative modeling where a set of pre-trained experts are combined via a gating mechanism. We defin...

---

### 26. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

**Authors:** Xiaoliang Fu, Jiaye Lin, Yangyi Fang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17550v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17550v1)

**Summary:** Existing Reinforcement Learning with Verifiable Rewards (RLVR) algorithms, such as GRPO, rely on rigid, uniform, and symmetric trust region mechanisms that are fundamentally misaligned with the complex optimization dynamics of Large Language Models (LLMs). In this paper, we identify three critical challenges in these methods: (1) inefficient gradient utilization caused by the binary cutoff of hard clipping, (2) insensitive probability mass arising from uniform ratio constraints that ignore the t...

---

### 27. Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning

**Authors:** Jyotin Goel, Souvik Maji, Pratik Mazumder

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17546v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17546v1)

**Summary:** Instruction-following language models are trained to be helpful and safe, yet their safety behavior can deteriorate under benign fine-tuning and worsen under adversarial updates. Existing defenses often offer limited protection or force a trade-off between safety and utility. We introduce a training framework that adapts regularization in response to safety risk, enabling models to remain aligned throughout fine-tuning. To estimate safety risk at training time, we explore two distinct approaches...

---

### 28. Adaptive Decentralized Composite Optimization via Three-Operator Splitting

**Authors:** Xiaokai Chen, Ilya Kuruzov, Gesualdo Scutari

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17545v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17545v1)

**Summary:** The paper studies decentralized optimization over networks, where agents minimize a sum of {\it locally} smooth (strongly) convex losses and plus a nonsmooth convex extended value term. We propose decentralized methods wherein agents {\it adaptively} adjust their stepsize via local backtracking procedures coupled with lightweight min-consensus protocols. Our design stems from a three-operator splitting factorization applied to an equivalent reformulation of the problem. The reformulation is endo...

---

### 29. genriesz: A Python Package for Automatic Debiased Machine Learning with Generalized Riesz Regression

**Authors:** Masahiro Kato

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17543v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17543v1)

**Summary:** Efficient estimation of causal and structural parameters can be automated using the Riesz representation theorem and debiased machine learning (DML). We present genriesz, an open-source Python package that implements automatic DML and generalized Riesz regression, a unified framework for estimating Riesz representers by minimizing empirical Bregman divergences. This framework includes covariate balancing, nearest-neighbor matching, calibrated estimation, and density ratio estimation as special c...

---

### 30. IRIS: Learning-Driven Task-Specific Cinema Robot Arm for Visuomotor Motion Control

**Authors:** Qilong Cheng, Matthew Mackay, Ali Bereyhi

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17537v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17537v1)

**Summary:** Robotic camera systems enable dynamic, repeatable motion beyond human capabilities, yet their adoption remains limited by the high cost and operational complexity of industrial-grade platforms. We present the Intelligent Robotic Imaging System (IRIS), a task-specific 6-DOF manipulator designed for autonomous, learning-driven cinematic motion control. IRIS integrates a lightweight, fully 3D-printed hardware design with a goal-conditioned visuomotor imitation learning framework based on Action Chu...

---

### 31. Position: Evaluation of ECG Representations Must Be Fixed

**Authors:** Zachary Berger, Daniel Prakah-Asante, John Guttag, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17531v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17531v1)

**Summary:** This position paper argues that current benchmarking practice in 12-lead ECG representation learning must be fixed to ensure progress is reliable and aligned with clinically meaningful objectives. The field has largely converged on three public multi-label benchmarks (PTB-XL, CPSC2018, CSN) dominated by arrhythmia and waveform-morphology labels, even though the ECG is known to encode substantially broader clinical information. We argue that downstream evaluation should expand to include an asses...

---

### 32. Provably Explaining Neural Additive Models

**Authors:** Shahaf Bassan, Yizhak Yisrael Elboher, Tobias Ladner, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17530v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17530v1)

**Summary:** Despite significant progress in post-hoc explanation methods for neural networks, many remain heuristic and lack provable guarantees. A key approach for obtaining explanations with provable guarantees is by identifying a cardinally-minimal subset of input features which by itself is provably sufficient to determine the prediction. However, for standard neural networks, this task is often computationally infeasible, as it demands a worst-case exponential number of verification queries in the numb...

---

### 33. The Anxiety of Influence: Bloom Filters in Transformer Attention Heads

**Authors:** Peter Balogh

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17526v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17526v1)

**Summary:** Some transformer attention heads appear to function as membership testers, dedicating themselves to answering the question "has this token appeared before in the context?" We identify these heads across four language models (GPT-2 small, medium, and large; Pythia-160M) and show that they form a spectrum of membership-testing strategies. Two heads (L0H1 and L0H5 in GPT-2 small) function as high-precision membership filters with false positive rates of 0-4\% even at 180 unique context tokens -- we...

---

### 34. Variational inference via radial transport

**Authors:** Luca Ghafourpour, Sinho Chewi, Alessio Figalli, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17525v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17525v1)

**Summary:** In variational inference (VI), the practitioner approximates a high-dimensional distribution $π$ with a simple surrogate one, often a (product) Gaussian distribution. However, in many cases of practical interest, Gaussian distributions might not capture the correct radial profile of $π$, resulting in poor coverage. In this work, we approach the VI problem from the perspective of optimizing over these radial profiles. Our algorithm radVI is a cheap, effective add-on to many existing VI schemes, s...

---

### 35. LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights

**Authors:** Kasun Dewage, Marianna Pensky, Suranadi De Silva, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17510v1)

**Summary:** We introduce CRAFT (Cross-layer Rank Adaptation via Frozen Tucker), a parameter-efficient fine-tuning (PEFT) method that applies Tucker tensor decomposition to pre-trained attention weight matrices stacked across transformer layers and trains only small square adaptation matrices on the resulting frozen Tucker factors. Existing tensor-based PEFT methods decompose gradient updates: LoTR applies Tucker decomposition with shared factor matrices, while SuperLoRA groups and reshapes $ΔW$ across layer...

---

### 36. Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models

**Authors:** Wen-Tse Chen, Jiayu Chen, Fahim Tajwar, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17497v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17497v1)

**Summary:** Learning from self-sampled data and sparse environmental feedback remains a fundamental challenge in training self-evolving agents. Temporal credit assignment mitigates this issue by transforming sparse feedback into dense supervision signals. However, previous approaches typically depend on learning task-specific value functions for credit assignment, which suffer from poor sample efficiency and limited generalization. In this work, we propose to leverage pretrained knowledge from large languag...

---

### 37. Learning with Boolean threshold functions

**Authors:** Veit Elser, Manish Krishan Lal

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17493v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17493v1)

**Summary:** We develop a method for training neural networks on Boolean data in which the values at all nodes are strictly $\pm 1$, and the resulting models are typically equivalent to networks whose nonzero weights are also $\pm 1$. The method replaces loss minimization with a nonconvex constraint formulation. Each node implements a Boolean threshold function (BTF), and training is expressed through a divide-and-concur decomposition into two complementary constraints: one enforces local BTF consistency bet...

---

### 38. Linear Convergence in Games with Delayed Feedback via Extra Prediction

**Authors:** Yuma Fujimoto, Kenshi Abe, Kaito Ariu

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17486v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17486v1)

**Summary:** Feedback delays are inevitable in real-world multi-agent learning. They are known to severely degrade performance, and the convergence rate under delayed feedback is still unclear, even for bilinear games. This paper derives the rate of linear convergence of Weighted Optimistic Gradient Descent-Ascent (WOGDA), which predicts future rewards with extra optimism, in unconstrained bilinear games. To analyze the algorithm, we interpret it as an approximation of the Extra Proximal Point (EPP), which i...

---

### 39. Variational Grey-Box Dynamics Matching

**Authors:** Gurjeet Sangra Singh, Frantzeska Lavda, Giangiacomo Mercatali, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17477v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17477v1)

**Summary:** Deep generative models such as flow matching and diffusion models have shown great potential in learning complex distributions and dynamical systems, but often act as black-boxes, neglecting underlying physics. In contrast, physics-based simulation models described by ODEs/PDEs remain interpretable, but may have missing or unknown terms, unable to fully describe real-world observations. We bridge this gap with a novel grey-box method that integrates incomplete physics models directly into genera...

---

### 40. ABCD: All Biases Come Disguised

**Authors:** Mateusz Nowak, Xavier Cadet, Peter Chin

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17445v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17445v1)

**Summary:** Multiple-choice question (MCQ) benchmarks have been a standard evaluation practice for measuring LLMs' ability to reason and answer knowledge-based questions. Through a synthetic NonsenseQA benchmark, we observe that different LLMs exhibit varying degrees of label-position-few-shot-prompt bias, where the model either uses the answer position, the label in front of the answer, the distributions of correct answers present in the few-shot prompt, or a combination of all to answer each MCQ question....

---

### 41. Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study

**Authors:** Dylan Bouchard, Mohit Singh Chauhan, Viren Bajaj, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17431v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17431v1)

**Summary:** Uncertainty quantification has emerged as an effective approach to closed-book hallucination detection for LLMs, but existing methods are largely designed for short-form outputs and do not generalize well to long-form generation. We introduce a taxonomy for fine-grained uncertainty quantification in long-form LLM outputs that distinguishes methods by design choices at three stages: response decomposition, unit-level scoring, and response-level aggregation. We formalize several families of consis...

---

### 42. Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking

**Authors:** Afroditi Kolomvaki, Fangshuo Liao, Evan Dramko, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17423v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17423v1)

**Summary:** We investigate the convergence guarantee of two-layer neural network training with Gaussian randomly masked inputs. This scenario corresponds to Gaussian dropout at the input level, or noisy input training common in sensor networks, privacy-preserving training, and federated learning, where each user may have access to partial or corrupted features. Using a Neural Tangent Kernel (NTK) analysis, we demonstrate that training a two-layer ReLU network with Gaussian randomly masked inputs achieves li...

---

### 43. SpectralGCD: Spectral Concept Selection and Cross-modal Representation Learning for Generalized Category Discovery

**Authors:** Lorenzo Caselli, Marco Mistretta, Simone Magistri, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17395v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17395v1)

**Summary:** Generalized Category Discovery (GCD) aims to identify novel categories in unlabeled data while leveraging a small labeled subset of known classes. Training a parametric classifier solely on image features often leads to overfitting to old classes, and recent multimodal approaches improve performance by incorporating textual information. However, they treat modalities independently and incur high computational cost. We propose SpectralGCD, an efficient and effective multimodal approach to GCD tha...

---

### 44. MDP Planning as Policy Inference

**Authors:** David Tolpin

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17375v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17375v1)

**Summary:** We cast episodic Markov decision process (MDP) planning as Bayesian inference over _policies_. A policy is treated as the latent variable and is assigned an unnormalized probability of optimality that is monotone in its expected return, yielding a posterior distribution whose modes coincide with return-maximizing solutions while posterior dispersion represents uncertainty over optimal behavior. To approximate this posterior in discrete domains, we adapt variational sequential Monte Carlo (VSMC) ...

---

### 45. A feature-stable and explainable machine learning framework for trustworthy decision-making under incomplete clinical data

**Authors:** Justyna Andrys-Olek, Paulina Tworek, Luca Gherardini, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17364v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17364v1)

**Summary:** Machine learning models are increasingly applied to biomedical data, yet their adoption in high stakes domains remains limited by poor robustness, limited interpretability, and instability of learned features under realistic data perturbations, such as missingness. In particular, models that achieve high predictive performance may still fail to inspire trust if their key features fluctuate when data completeness changes, undermining reproducibility and downstream decision-making. Here, we presen...

---

### 46. 2Mamba2Furious: Linear in Complexity, Competitive in Accuracy

**Authors:** Gabriel Mongaras, Eric C. Larson

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17363v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17363v1)

**Summary:** Linear attention transformers have become a strong alternative to softmax attention due to their efficiency. However, linear attention tends to be less expressive and results in reduced accuracy compared to softmax attention. To bridge the accuracy gap between softmax attention and linear attention, we manipulate Mamba-2, a very strong linear attention variant. We first simplify Mamba-2 down to its most fundamental and important components, evaluating which specific choices make it most accurate...

---

### 47. Shortcut learning in geometric knot classification

**Authors:** Djordje Mihajlovic, Davide Michieletto

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17350v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17350v1)

**Summary:** Classifying the topology of closed curves is a central problem in low dimensional topology with applications beyond mathematics spanning protein folding, polymer physics and even magnetohydrodynamics. The central problem is how to determine whether two embeddings of a closed arc are equivalent under ambient isotopy. Given the striking ability of neural networks to solve complex classification tasks, it is therefore natural to ask if the knot classification problem can be tackled using Machine Le...

---

### 48. Partial Optimality in the Preordering Problem

**Authors:** David Stein, Jannik Irmai, Bjoern Andres

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17346v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17346v1)

**Summary:** Preordering is a generalization of clustering and partial ordering with applications in bioinformatics and social network analysis. Given a finite set $V$ and a value $c_{ab} \in \mathbb{R}$ for every ordered pair $ab$ of elements of $V$, the preordering problem asks for a preorder $\lesssim$ on $V$ that maximizes the sum of the values of those pairs $ab$ for which $a \lesssim b$. Building on the state of the art in solving this NP-hard problem partially, we contribute new partial optimality con...

---

### 49. From Subtle to Significant: Prompt-Driven Self-Improving Optimization in Test-Time Graph OOD Detection

**Authors:** Luzhi Wang, Xuanshuo Fu, He Zhang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17342v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17342v1)

**Summary:** Graph Out-of-Distribution (OOD) detection aims to identify whether a test graph deviates from the distribution of graphs observed during training, which is critical for ensuring the reliability of Graph Neural Networks (GNNs) when deployed in open-world scenarios. Recent advances in graph OOD detection have focused on test-time training techniques that facilitate OOD detection without accessing potential supervisory information (e.g., training data). However, most of these methods employ a one-p...

---

### 50. SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework

**Authors:** Rong Fu, Zijian Zhang, Wenxin Zhang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17330v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17330v1)

**Summary:** Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system empl...

---

## stat.ML

**50 papers**

### 1. When to Trust the Cheap Check: Weak and Strong Verification for Reasoning

**Authors:** Shayan Kiyani, Sima Noorani, George Pappas, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17633v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17633v1)

**Summary:** Reasoning with LLMs increasingly unfolds inside a broader verification loop. Internally, systems use cheap checks, such as self-consistency or proxy rewards, which we call weak verification. Externally, users inspect outputs and steer the model through feedback until results are trustworthy, which we call strong verification. These signals differ sharply in cost and reliability: strong verification can establish trust but is resource-intensive, while weak verification is fast and scalable but no...

---

### 2. Towards Anytime-Valid Statistical Watermarking

**Authors:** Baihe Huang, Eric Xu, Kannan Ramchandran, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17608v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17608v1)

**Summary:** The proliferation of Large Language Models (LLMs) necessitates efficient mechanisms to distinguish machine-generated content from human text. While statistical watermarking has emerged as a promising solution, existing methods suffer from two critical limitations: the lack of a principled approach for selecting sampling distributions and the reliance on fixed-horizon hypothesis testing, which precludes valid early stopping. In this paper, we bridge this gap by developing the first e-value-based ...

---

### 3. SOLVAR: Fast covariance-based heterogeneity analysis with pose refinement for cryo-EM

**Authors:** Roey Yadgar, Roy R. Lederman, Yoel Shkolnisky

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17603v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17603v1)

**Summary:** Cryo-electron microscopy (cryo-EM) has emerged as a powerful technique for resolving the three-dimensional structures of macromolecules. A key challenge in cryo-EM is characterizing continuous heterogeneity, where molecules adopt a continuum of conformational states. Covariance-based methods offer a principled approach to modeling structural variability. However, estimating the covariance matrix efficiently remains a challenging computational task. In this paper, we present SOLVAR (Stochastic Op...

---

### 4. Asymptotically Optimal Sequential Testing with Markovian Data

**Authors:** Alhad Sethi, Kavali Sofia Sagar, Shubhada Agrawal, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17587v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17587v1)

**Summary:** We study one-sided and $α$-correct sequential hypothesis testing for data generated by an ergodic Markov chain. The null hypothesis is that the unknown transition matrix belongs to a prescribed set $P$ of stochastic matrices, and the alternative corresponds to a disjoint set $Q$. We establish a tight non-asymptotic instance-dependent lower bound on the expected stopping time of any valid sequential test under the alternative. Our novel analysis improves the existing lower bounds, which are eithe...

---

### 5. Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction

**Authors:** Lunjia Hu, Kevin Tian, Chutong Yang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17577v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17577v1)

**Summary:** Omniprediction is a learning problem that requires suboptimality bounds for each of a family of losses $\mathcal{L}$ against a family of comparator predictors $\mathcal{C}$. We initiate the study of omniprediction in a multiclass setting, where the comparator family $\mathcal{C}$ may be infinite. Our main result is an extension of the recent binary omniprediction algorithm of [OKK25] to the multiclass setting, with sample complexity (in statistical settings) or regret horizon (in online settings...

---

### 6. Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning

**Authors:** Hien Dang, Pratik Patil, Alessandro Rinaldo

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17565v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17565v1)

**Summary:** Self-distillation (SD) is the process of retraining a student on a mixture of ground-truth labels and the teacher's own predictions using the same architecture and training data. Although SD has been empirically shown to often improve generalization, its formal guarantees remain limited. We study SD for ridge regression in unconstrained setting in which the mixing weight $ξ$ may be outside the unit interval. Conditioned on the training data and without any distributional assumptions, we prove th...

---

### 7. A Theoretical Framework for Modular Learning of Robust Generative Models

**Authors:** Corinna Cortes, Mehryar Mohri, Yutao Zhong

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17554v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17554v1)

**Summary:** Training large-scale generative models is resource-intensive and relies heavily on heuristic dataset weighting. We address two fundamental questions: Can we train Large Language Models (LLMs) modularly-combining small, domain-specific experts to match monolithic performance-and can we do so robustly for any data mixture, eliminating heuristic tuning? We present a theoretical framework for modular generative modeling where a set of pre-trained experts are combined via a gating mechanism. We defin...

---

### 8. genriesz: A Python Package for Automatic Debiased Machine Learning with Generalized Riesz Regression

**Authors:** Masahiro Kato

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17543v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17543v1)

**Summary:** Efficient estimation of causal and structural parameters can be automated using the Riesz representation theorem and debiased machine learning (DML). We present genriesz, an open-source Python package that implements automatic DML and generalized Riesz regression, a unified framework for estimating Riesz representers by minimizing empirical Bregman divergences. This framework includes covariate balancing, nearest-neighbor matching, calibrated estimation, and density ratio estimation as special c...

---

### 9. Variational inference via radial transport

**Authors:** Luca Ghafourpour, Sinho Chewi, Alessio Figalli, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17525v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17525v1)

**Summary:** In variational inference (VI), the practitioner approximates a high-dimensional distribution $π$ with a simple surrogate one, often a (product) Gaussian distribution. However, in many cases of practical interest, Gaussian distributions might not capture the correct radial profile of $π$, resulting in poor coverage. In this work, we approach the VI problem from the perspective of optimizing over these radial profiles. Our algorithm radVI is a cheap, effective add-on to many existing VI schemes, s...

---

### 10. Gaussian surrogates do well on Poisson inverse problems

**Authors:** Alexandra Spitzer, Lorenzo Baldassari, Valentin Derbanot, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17274v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17274v1)

**Summary:** In imaging inverse problems with Poisson-distributed measurements, it is common to use objectives derived from the Poisson likelihood. But performance is often evaluated by mean squared error (MSE), which raises a practical question: how much does a Poisson objective matter for MSE, even at low dose? We analyze the MSE of Poisson and Gaussian surrogate reconstruction objectives under Poisson noise. In a stylized diagonal model, we show that the unregularized Poisson maximum-likelihood estimator ...

---

### 11. MGD: Moment Guided Diffusion for Maximum Entropy Generation

**Authors:** Etienne Lempereur, Nathanaël Cuvelle--Magar, Florentin Coeurdoux, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17211v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17211v1)

**Summary:** Generating samples from limited information is a fundamental problem across scientific domains. Classical maximum entropy methods provide principled uncertainty quantification from moment constraints but require sampling via MCMC or Langevin dynamics, which typically exhibit exponential slowdown in high dimensions. In contrast, generative models based on diffusion and flow matching efficiently transport noise to data but offer limited theoretical guarantees and can overfit when data is scarce. W...

---

### 12. Anti-causal domain generalization: Leveraging unlabeled data

**Authors:** Sorawit Saengkyongam, Juan L. Gamella, Andrew C. Miller, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17187v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17187v1)

**Summary:** The problem of domain generalization concerns learning predictive models that are robust to distribution shifts when deployed in new, previously unseen environments. Existing methods typically require labeled data from multiple training environments, limiting their applicability when labeled data are scarce. In this work, we study domain generalization in an anti-causal setting, where the outcome causes the observed covariates. Under this structure, environment perturbations that affect the cova...

---

### 13. When More Experts Hurt: Underfitting in Multi-Expert Learning to Defer

**Authors:** Shuqi Liu, Yuzhou Cao, Lei Feng, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17144v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17144v1)

**Summary:** Learning to Defer (L2D) enables a classifier to abstain from predictions and defer to an expert, and has recently been extended to multi-expert settings. In this work, we show that multi-expert L2D is fundamentally more challenging than the single-expert case. With multiple experts, the classifier's underfitting becomes inherent, which seriously degrades prediction performance, whereas in the single-expert setting it arises only under specific conditions. We theoretically reveal that this stems ...

---

### 14. Semi-Supervised Learning on Graphs using Graph Neural Networks

**Authors:** Juntong Chen, Claire Donnat, Olga Klopp, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17115v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17115v1)

**Summary:** Graph neural networks (GNNs) work remarkably well in semi-supervised node regression, yet a rigorous theory explaining when and why they succeed remains lacking. To address this gap, we study an aggregate-and-readout model that encompasses several common message passing architectures: node features are first propagated over the graph then mapped to responses via a nonlinear function. For least-squares estimation over GNNs with linear graph convolutions and a deep ReLU readout, we prove a sharp n...

---

### 15. Online Learning with Improving Agents: Multiclass, Budgeted Agents and Bandit Learners

**Authors:** Sajad Ashkezari, Shai Ben-David

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17103v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17103v1)

**Summary:** We investigate the recently introduced model of learning with improvements, where agents are allowed to make small changes to their feature values to be warranted a more desirable label. We extensively extend previously published results by providing combinatorial dimensions that characterize online learnability in this model, by analyzing the multiclass setup, learnability in a bandit feedback setup, modeling agents' cost for making improvements and more.

---

### 16. M-estimation under Two-Phase Multiwave Sampling with Applications to Prediction-Powered Inference

**Authors:** Dan M. Kluger, Stephen Bates

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16933v1)

**Summary:** In two-phase multiwave sampling, inexpensive measurements are collected on a large sample and expensive, more informative measurements are adaptively obtained on subsets of units across multiple waves. Adaptively collecting the expensive measurements can increase efficiency but complicates statistical inference. We give valid estimators and confidence intervals for M-estimation under adaptive two-phase multiwave sampling. We focus on the case where proxies for the expensive variables -- such as ...

---

### 17. Poisson-MNL Bandit: Nearly Optimal Dynamic Joint Assortment and Pricing with Decision-Dependent Customer Arrivals

**Authors:** Junhui Cai, Ran Chen, Qitao Huang, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16923v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16923v1)

**Summary:** We study dynamic joint assortment and pricing where a seller updates decisions at regular accounting/operating intervals to maximize the cumulative per-period revenue over a horizon $T$. In many settings, assortment and prices affect not only what an arriving customer buys but also how many customers arrive within the period, whereas classical multinomial logit (MNL) models assume arrivals as fixed, potentially leading to suboptimal decisions. We propose a Poisson-MNL model that couples a contex...

---

### 18. A statistical perspective on transformers for small longitudinal cohort data

**Authors:** Kiana Farhadyar, Maren Hackenberg, Kira Ahrens, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16914v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16914v1)

**Summary:** Modeling of longitudinal cohort data typically involves complex temporal dependencies between multiple variables. There, the transformer architecture, which has been highly successful in language and vision applications, allows us to account for the fact that the most recently observed time points in an individual's history may not always be the most important for the immediate future. This is achieved by assigning attention weights to observations of an individual based on a transformation of t...

---

### 19. ML-driven detection and reduction of ballast information in multi-modal datasets

**Authors:** Yaroslav Solovko

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16876v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16876v1)

**Summary:** Modern datasets often contain ballast as redundant or low-utility information that increases dimensionality, storage requirements, and computational cost without contributing meaningful analytical value. This study introduces a generalized, multimodal framework for ballast detection and reduction across structured, semi-structured, unstructured, and sparse data types. Using diverse datasets, entropy, mutual information, Lasso, SHAP, PCA, topic modelling, and embedding analysis are applied to ide...

---

### 20. On the Mechanism and Dynamics of Modular Addition: Fourier Features, Lottery Ticket, and Grokking

**Authors:** Jianliang He, Leda Wang, Siyu Chen, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16849v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16849v1)

**Summary:** We present a comprehensive analysis of how two-layer neural networks learn features to solve the modular addition task. Our work provides a full mechanistic interpretation of the learned model and a theoretical explanation of its training dynamics. While prior work has identified that individual neurons learn single-frequency Fourier features and phase alignment, it does not fully explain how these features combine into a global solution. We bridge this gap by formalizing a diversification condi...

---

### 21. Beyond Procedure: Substantive Fairness in Conformal Prediction

**Authors:** Pengqi Liu, Zijun Yu, Mouloud Belbahri, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16794v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16794v1)

**Summary:** Conformal prediction (CP) offers distribution-free uncertainty quantification for machine learning models, yet its interplay with fairness in downstream decision-making remains underexplored. Moving beyond CP as a standalone operation (procedural fairness), we analyze the holistic decision-making pipeline to evaluate substantive fairness-the equity of downstream outcomes. Theoretically, we derive an upper bound that decomposes prediction-set size disparity into interpretable components, clarifyi...

---

### 22. Synthetic-Powered Multiple Testing with FDR Control

**Authors:** Yonghoon Lee, Meshi Bashari, Edgar Dobriban, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16690v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16690v1)

**Summary:** Multiple hypothesis testing with false discovery rate (FDR) control is a fundamental problem in statistical inference, with broad applications in genomics, drug screening, and outlier detection. In many such settings, researchers may have access not only to real experimental observations but also to auxiliary or synthetic data -- from past, related experiments or generated by generative models -- that can provide additional evidence about the hypotheses of interest. We introduce SynthBH, a synth...

---

### 23. Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models

**Authors:** Yu Xie, Ludwig Winkler, Lixin Sun, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16634v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16634v1)

**Summary:** The rare-event sampling problem has long been the central limiting factor in molecular dynamics (MD), especially in biomolecular simulation. Recently, diffusion models such as BioEmu have emerged as powerful equilibrium samplers that generate independent samples from complex molecular distributions, eliminating the cost of sampling rare transition events. However, a sampling problem remains when computing observables that rely on states which are rare in equilibrium, for example folding free ene...

---

### 24. Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study

**Authors:** Nail B. Khelifa, Richard E. Turner, Ramji Venkataramanan

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16601v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16601v1)

**Summary:** Machine learning models are increasingly trained or fine-tuned on synthetic data. Recursively training on such data has been observed to significantly degrade performance in a wide range of tasks, often characterized by a progressive drift away from the target distribution. In this work, we theoretically analyze this phenomenon in the setting of score-based diffusion models. For a realistic pipeline where each training round uses a combination of synthetic data and fresh samples from the target ...

---

### 25. Sequential Membership Inference Attacks

**Authors:** Thomas Michel, Debabrota Basu, Emilie Kaufmann

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16596v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16596v1)

**Summary:** Modern AI models are not static. They go through multiple updates in their lifecycles. Thus, exploiting the model dynamics to create stronger Membership Inference (MI) attacks and tighter privacy audits are timely questions. Though the literature empirically shows that using a sequence of model updates can increase the power of MI attacks, rigorous analysis of the `optimal' MI attacks is limited to static models with infinite samples. Hence, we develop an `optimal' MI attack, SeMI*, that uses th...

---

### 26. Separating Oblivious and Adaptive Models of Variable Selection

**Authors:** Ziyun Chen, Jerry Li, Kevin Tian, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16568v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16568v1)

**Summary:** Sparse recovery is among the most well-studied problems in learning theory and high-dimensional statistics. In this work, we investigate the statistical and computational landscapes of sparse recovery with $\ell_\infty$ error guarantees. This variant of the problem is motivated by \emph{variable selection} tasks, where the goal is to estimate the support of a $k$-sparse signal in $\mathbb{R}^d$. Our main contribution is a provable separation between the \emph{oblivious} (``for each'') and \emph{...

---

### 27. Optimal training-conditional regret for online conformal prediction

**Authors:** Jiadong Liang, Zhimei Ren, Yuxin Chen

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16537v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16537v1)

**Summary:** We study online conformal prediction for non-stationary data streams subject to unknown distribution drift. While most prior work studied this problem under adversarial settings and/or assessed performance in terms of gaps of time-averaged marginal coverage, we instead evaluate performance through training-conditional cumulative regret. We specifically focus on independently generated data with two types of distribution shift: abrupt change points and smooth drift.   When non-conformity score fu...

---

### 28. Functional Decomposition and Shapley Interactions for Interpreting Survival Models

**Authors:** Sophie Hanna Langbein, Hubert Baniecki, Fabian Fumagalli, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16505v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16505v1)

**Summary:** Hazard and survival functions are natural, interpretable targets in time-to-event prediction, but their inherent non-additivity fundamentally limits standard additive explanation methods. We introduce Survival Functional Decomposition (SurvFD), a principled approach for analyzing feature interactions in machine learning survival models. By decomposing higher-order effects into time-dependent and time-independent components, SurvFD offers a previously unrecognized perspective on survival explanat...

---

### 29. Learning Preference from Observed Rankings

**Authors:** Yu-Chang Chen, Chen Chian Fuh, Shang En Tsai

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16476v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16476v1)

**Summary:** Estimating consumer preferences is central to many problems in economics and marketing. This paper develops a flexible framework for learning individual preferences from partial ranking information by interpreting observed rankings as collections of pairwise comparisons with logistic choice probabilities. We model latent utility as the sum of interpretable product attributes, item fixed effects, and a low-rank user-item factor structure, enabling both interpretability and information sharing acr...

---

### 30. GICDM: Mitigating Hubness for Reliable Distance-Based Generative Model Evaluation

**Authors:** Nicolas Salvy, Hugues Talbot, Bertrand Thirion

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16449v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16449v1)

**Summary:** Generative model evaluation commonly relies on high-dimensional embedding spaces to compute distances between samples. We show that dataset representations in these spaces are affected by the hubness phenomenon, which distorts nearest neighbor relationships and biases distance-based metrics. Building on the classical Iterative Contextual Dissimilarity Measure (ICDM), we introduce Generative ICDM (GICDM), a method to correct neighborhood estimation for both real and generated data. We introduce a...

---

### 31. Learning with Locally Private Examples by Inverse Weierstrass Private Stochastic Gradient Descent

**Authors:** Jean Dufraiche, Paul Mangold, Michaël Perrot, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16436v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16436v1)

**Summary:** Releasing data once and for all under noninteractive Local Differential Privacy (LDP) enables complete data reusability, but the resulting noise may create bias in subsequent analyses. In this work, we leverage the Weierstrass transform to characterize this bias in binary classification. We prove that inverting this transform leads to a bias-correction method to compute unbiased estimates of nonlinear functions on examples released under LDP. We then build a novel stochastic gradient descent alg...

---

### 32. Machine Learning in Epidemiology

**Authors:** Marvin N. Wright, Lukas Burk, Pegah Golchian, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16352v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16352v1)

**Summary:** In the age of digital epidemiology, epidemiologists are faced by an increasing amount of data of growing complexity and dimensionality. Machine learning is a set of powerful tools that can help to analyze such enormous amounts of data. This chapter lays the methodological foundations for successfully applying machine learning in epidemiology. It covers the principles of supervised and unsupervised learning and discusses the most important machine learning methods. Strategies for model evaluation...

---

### 33. The Implicit Bias of Adam and Muon on Smooth Homogeneous Neural Networks

**Authors:** Eitan Gronich, Gal Vardi

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16340v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16340v1)

**Summary:** We study the implicit bias of momentum-based optimizers on homogeneous models. We first extend existing results on the implicit bias of steepest descent in homogeneous models to normalized steepest descent with an optional learning rate schedule. We then show that for smooth homogeneous models, momentum steepest descent algorithms like Muon (spectral norm), MomentumGD ($\ell_2$ norm), and Signum ($\ell_\infty$ norm) are approximate steepest descent trajectories under a decaying learning rate sch...

---

### 34. Regret and Sample Complexity of Online Q-Learning via Concentration of Stochastic Approximation with Time-Inhomogeneous Markov Chains

**Authors:** Rahul Singh, Siddharth Chandak, Eric Moulines, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16274v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16274v1)

**Summary:** We present the first high-probability regret bound for classical online Q-learning in infinite-horizon discounted Markov decision processes, without relying on optimism or bonus terms. We first analyze Boltzmann Q-learning with decaying temperature and show that its regret depends critically on the suboptimality gap of the MDP: for sufficiently large gaps, the regret is sublinear, while for small gaps it deteriorates and can approach linear growth. To address this limitation, we study a Smoothed...

---

### 35. On sparsity, extremal structure, and monotonicity properties of Wasserstein and Gromov-Wasserstein optimal transport plans

**Authors:** Titouan Vayer

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16265v2) | 📄 [PDF](https://arxiv.org/pdf/2602.16265v2)

**Summary:** This note gives a self-contained overview of some important properties of the Gromov-Wasserstein (GW) distance, compared with the standard linear optimal transport (OT) framework. More specifically, I explore the following questions: are GW optimal transport plans sparse? Under what conditions are they supported on a permutation? Do they satisfy a form of cyclical monotonicity? In particular, I present the conditionally negative semi-definite property and show that, when it holds, there are GW o...

---

### 36. Bayesian Quadrature: Gaussian Processes for Integration

**Authors:** Maren Mahsereci, Toni Karvonen

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16218v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16218v1)

**Summary:** Bayesian quadrature is a probabilistic, model-based approach to numerical integration, the estimation of intractable integrals, or expectations. Although Bayesian quadrature was popularised already in the 1980s, no systematic and comprehensive treatment has been published. The purpose of this survey is to fill this gap. We review the mathematical foundations of Bayesian quadrature from different points of view; present a systematic taxonomy for classifying different Bayesian quadrature methods a...

---

### 37. Multi-Agent Combinatorial-Multi-Armed-Bandit framework for the Submodular Welfare Problem under Bandit Feedback

**Authors:** Subham Pokhriyal, Shweta Jain, Vaneet Aggarwal

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16183v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16183v1)

**Summary:** We study the \emph{Submodular Welfare Problem} (SWP), where items are partitioned among agents with monotone submodular utilities to maximize the total welfare under \emph{bandit feedback}. Classical SWP assumes full value-oracle access, achieving $(1-1/e)$ approximations via continuous-greedy algorithms. We extend this to a \emph{multi-agent combinatorial bandit} framework (\textsc{MA-CMAB}), where actions are partitions under full-bandit feedback with non-communicating agents. Unlike prior sin...

---

### 38. Conjugate Learning Theory: Uncovering the Mechanisms of Trainability and Generalization in Deep Neural Networks

**Authors:** Binchuan Qi

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16177v2) | 📄 [PDF](https://arxiv.org/pdf/2602.16177v2)

**Summary:** In this work, we propose a notion of practical learnability grounded in finite sample settings, and develop a conjugate learning theoretical framework based on convex conjugate duality to characterize this learnability property. Building on this foundation, we demonstrate that training deep neural networks (DNNs) with mini-batch stochastic gradient descent (SGD) achieves global optima of empirical risk by jointly controlling the extreme eigenvalues of a structure matrix and the gradient energy, ...

---

### 39. Empirical Cumulative Distribution Function Clustering for LLM-based Agent System Analysis

**Authors:** Chihiro Watanabe, Jingyu Sun

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16131v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16131v1)

**Summary:** Large language models (LLMs) are increasingly used as agents to solve complex tasks such as question answering (QA), scientific debate, and software development. A standard evaluation procedure aggregates multiple responses from LLM agents into a single final answer, often via majority voting, and compares it against reference answers. However, this process can obscure the quality and distributional characteristics of the original responses. In this paper, we propose a novel evaluation framework...

---

### 40. Feature-based morphological analysis of shape graph data

**Authors:** Murad Hossen, Demetrio Labate, Nicolas Charon

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16120v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16120v1)

**Summary:** This paper introduces and demonstrates a computational pipeline for the statistical analysis of shape graph datasets, namely geometric networks embedded in 2D or 3D spaces. Unlike traditional abstract graphs, our purpose is not only to retrieve and distinguish variations in the connectivity structure of the data but also geometric differences of the network branches. Our proposed approach relies on the extraction of a specifically curated and explicit set of topological, geometric and directiona...

---

### 41. Quantifying and Attributing Submodel Uncertainty in Stochastic Simulation Models and Digital Twins

**Authors:** Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16099v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16099v1)

**Summary:** Stochastic simulation is widely used to study complex systems composed of various interconnected subprocesses, such as input processes, routing and control logic, optimization routines, and data-driven decision modules. In practice, these subprocesses may be inherently unknown or too computationally intensive to directly embed in the simulation model. Replacing these elements with estimated or learned approximations introduces a form of epistemic uncertainty that we refer to as submodel uncertai...

---

### 42. Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training

**Authors:** Kevin Wang, Hongqian Niu, Didong Li

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16065v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16065v1)

**Summary:** Generative Artificial Intelligence (AI), such as large language models (LLMs), has become a transformative force across science, industry, and society. As these systems grow in popularity, web data becomes increasingly interwoven with this AI-generated material and it is increasingly difficult to separate them from naturally generated content. As generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier...

---

### 43. Partial Identification under Missing Data Using Weak Shadow Variables from Pretrained Models

**Authors:** Hongyu Chen, David Simchi-Levi, Ruoxuan Xiong

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16061v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16061v1)

**Summary:** Estimating population quantities such as mean outcomes from user feedback is fundamental to platform evaluation and social science, yet feedback is often missing not at random (MNAR): users with stronger opinions are more likely to respond, so standard estimators are biased and the estimand is not identified without additional assumptions. Existing approaches typically rely on strong parametric assumptions or bespoke auxiliary variables that may be unavailable in practice. In this paper, we deve...

---

### 44. Fast Online Learning with Gaussian Prior-Driven Hierarchical Unimodal Thompson Sampling

**Authors:** Tianchi Zhao, He Liu, Hongyin Shi, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15972v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15972v1)

**Summary:** We study a type of Multi-Armed Bandit (MAB) problems in which arms with a Gaussian reward feedback are clustered. Such an arm setting finds applications in many real-world problems, for example, mmWave communications and portfolio management with risky assets, as a result of the universality of the Gaussian distribution. Based on the Thompson Sampling algorithm with Gaussian prior (TSG) algorithm for the selection of the optimal arm, we propose our Thompson Sampling with Clustered arms under Gau...

---

### 45. Robust Stochastic Gradient Posterior Sampling with Lattice Based Discretisation

**Authors:** Zier Mensch, Lars Holdijk, Samuel Duffield, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15925v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15925v1)

**Summary:** Stochastic-gradient MCMC methods enable scalable Bayesian posterior sampling but often suffer from sensitivity to minibatch size and gradient noise. To address this, we propose Stochastic Gradient Lattice Random Walk (SGLRW), an extension of the Lattice Random Walk discretization. Unlike conventional Stochastic Gradient Langevin Dynamics (SGLD), SGLRW introduces stochastic noise only through the off-diagonal elements of the update covariance; this yields greater robustness to minibatch size whil...

---

### 46. Certified Per-Instance Unlearning Using Individual Sensitivity Bounds

**Authors:** Hanna Benarroch, Jamal Atif, Olivier Cappé

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15602v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15602v1)

**Summary:** Certified machine unlearning can be achieved via noise injection leading to differential privacy guarantees, where noise is calibrated to worst-case sensitivity. Such conservative calibration often results in performance degradation, limiting practical applicability. In this work, we investigate an alternative approach based on adaptive per-instance noise calibration tailored to the individual contribution of each data point to the learned solution. This raises the following challenge: how can o...

---

### 47. Uniform error bounds for quantized dynamical models

**Authors:** Abdelkader Metakalard, Fabien Lauer, Kevin Colin, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15586v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15586v1)

**Summary:** This paper provides statistical guarantees on the accuracy of dynamical models learned from dependent data sequences. Specifically, we develop uniform error bounds that apply to quantized models and imperfect optimization algorithms commonly used in practical contexts for system identification, and in particular hybrid system identification. Two families of bounds are obtained: slow-rate bounds via a block decomposition and fast-rate, variance-adaptive, bounds via a novel spaced-point strategy. ...

---

### 48. Scenario Approach with Post-Design Certification of User-Specified Properties

**Authors:** Algo Carè, Marco C. Campi, Simone Garatti

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15568v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15568v1)

**Summary:** The scenario approach is an established data-driven design framework that comes equipped with a powerful theory linking design complexity to generalization properties. In this approach, data are simultaneously used both for design and for certifying the design's reliability, without resorting to a separate test dataset. This paper takes a step further by guaranteeing additional properties, useful in post-design usage but not considered during the design phase. To this end, we introduce a two-lev...

---

### 49. Fixed-Horizon Self-Normalized Inference for Adaptive Experiments via Martingale AIPW/DML with Logged Propensities

**Authors:** Gabriel Saco

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15559v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15559v1)

**Summary:** Adaptive randomized experiments update treatment probabilities as data accrue, but still require an end-of-study interval for the average treatment effect (ATE) at a prespecified horizon. Under adaptive assignment, propensities can keep changing, so the predictable quadratic variation of AIPW/DML score increments may remain random. When no deterministic variance limit exists, Wald statistics normalized by a single long-run variance target can be conditionally miscalibrated given the realized var...

---

### 50. Functional Central Limit Theorem for Stochastic Gradient Descent

**Authors:** Kessang Flamand, Victor-Emmanuel Brunel

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15538v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15538v1)

**Summary:** We study the asymptotic shape of the trajectory of the stochastic gradient descent algorithm applied to a convex objective function. Under mild regularity assumptions, we prove a functional central limit theorem for the properly rescaled trajectory. Our result characterizes the long-term fluctuations of the algorithm around the minimizer by providing a diffusion limit for the trajectory. In contrast with classical central limit theorems for the last iterate or Polyak-Ruppert averages, this funct...

---

