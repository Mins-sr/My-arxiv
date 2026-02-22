# arXiv Daily Digest - 2026-02-22

Total papers: 350

---

## cs.AI

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

### 3. MARS: Margin-Aware Reward-Modeling with Self-Refinement

**Authors:** Payel Bhattacharjee, Osvaldo Simeone, Ravi Tandon

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17658v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17658v1)

**Summary:** Reward modeling is a core component of modern alignment pipelines including RLHF and RLAIF, underpinning policy optimization methods including PPO and TRPO. However, training reliable reward models relies heavily on human-labeled preference data, which is costly and limited, motivating the use of data augmentation. Existing augmentation approaches typically operate at the representation or semantic level and remain agnostic to the reward model's estimation difficulty. In this paper, we propose M...

---

### 4. Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting

**Authors:** Xiaohan Zhao, Zhaoyi Li, Yaxin Luo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17645v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17645v1)

**Summary:** Black-box adversarial attacks on Large Vision-Language Models (LVLMs) are challenging due to missing gradients and complex multimodal boundaries. While prior state-of-the-art transfer-based approaches like M-Attack perform well using local crop-level matching between source and target images, we find this induces high-variance, nearly orthogonal gradients across iterations, violating coherent local alignment and destabilizing optimization. We attribute this to (i) ViT translation sensitivity tha...

---

### 5. FAMOSE: A ReAct Approach to Automated Feature Discovery

**Authors:** Keith Burghardt, Jienan Liu, Sadman Sakib, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17641v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17641v1)

**Summary:** Feature engineering remains a critical yet challenging bottleneck in machine learning, particularly for tabular data, as identifying optimal features from an exponentially large feature space traditionally demands substantial domain expertise. To address this challenge, we introduce FAMOSE (Feature AugMentation and Optimal Selection agEnt), a novel framework that leverages the ReAct paradigm to autonomously explore, generate, and refine features while integrating feature selection and evaluation...

---

### 6. Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting

**Authors:** Xinghong Fu, Yanhong Li, Georgios Papaioannou, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17634v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17634v1)

**Summary:** Learning time series foundation models has been shown to be a promising approach for zero-shot time series forecasting across diverse time series domains. Insofar as scaling has been a critical driver of performance of foundation models in other modalities such as language and vision, much recent work on time series foundation modeling has focused on scaling. This has resulted in time series foundation models with hundreds of millions of parameters that are, while performant, inefficient and exp...

---

### 7. When to Trust the Cheap Check: Weak and Strong Verification for Reasoning

**Authors:** Shayan Kiyani, Sima Noorani, George Pappas, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17633v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17633v1)

**Summary:** Reasoning with LLMs increasingly unfolds inside a broader verification loop. Internally, systems use cheap checks, such as self-consistency or proxy rewards, which we call weak verification. Externally, users inspect outputs and steer the model through feedback until results are trustworthy, which we call strong verification. These signals differ sharply in cost and reliability: strong verification can establish trust but is resource-intensive, while weak verification is fast and scalable but no...

---

### 8. SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer

**Authors:** Nathan S. de Lara, Florian Shkurti

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17632v1)

**Summary:** Modern offline Reinforcement Learning (RL) methods find performant actor-critics, however, fine-tuning these actor-critics online with value-based RL algorithms typically causes immediate drops in performance. We provide evidence consistent with the hypothesis that, in the loss landscape, offline maxima for prior algorithms and online maxima are separated by low-performance valleys that gradient-based fine-tuning traverses. Following this, we present Score Matched Actor-Critic (SMAC), an offline...

---

### 9. Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs

**Authors:** Luke Huang, Zhuoyang Zhang, Qinghao Hu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17616v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17616v1)

**Summary:** Reinforcement learning (RL) is widely used to improve large language models on reasoning tasks, and asynchronous RL training is attractive because it increases end-to-end throughput. However, for widely adopted critic-free policy-gradient methods such as REINFORCE and GRPO, high asynchrony makes the policy-gradient estimator markedly $\textbf{higher variance}$: training on stale rollouts creates heavy-tailed importance ratios, causing a small fraction of samples to dominate updates. This amplifi...

---

### 10. Towards Anytime-Valid Statistical Watermarking

**Authors:** Baihe Huang, Eric Xu, Kannan Ramchandran, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17608v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17608v1)

**Summary:** The proliferation of Large Language Models (LLMs) necessitates efficient mechanisms to distinguish machine-generated content from human text. While statistical watermarking has emerged as a promising solution, existing methods suffer from two critical limitations: the lack of a principled approach for selecting sampling distributions and the reliance on fixed-horizon hypothesis testing, which precludes valid early stopping. In this paper, we bridge this gap by developing the first e-value-based ...

---

### 11. AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing

**Authors:** Jianda Du, Youran Sun, Haizhao Yang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17607v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17607v1)

**Summary:** PDEs are central to scientific and engineering modeling, yet designing accurate numerical solvers typically requires substantial mathematical expertise and manual tuning. Recent neural network-based approaches improve flexibility but often demand high computational cost and suffer from limited interpretability. We introduce \texttt{AutoNumerics}, a multi-agent framework that autonomously designs, implements, debugs, and verifies numerical solvers for general PDEs directly from natural language d...

---

### 12. Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery

**Authors:** Jowaria Khan, Anindya Sarkar, Yevgeniy Vorobeychik, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17605v1)

**Summary:** In many real-world settings, such as environmental monitoring, disaster response, or public health, with costly and difficult data collection and dynamic environments, strategically sampling from unobserved regions is essential for efficiently uncovering hidden targets under tight resource constraints. Yet, sparse and biased geospatial ground truth limits the applicability of existing learning-based methods, such as reinforcement learning. To address this, we propose a unified geospatial discove...

---

### 13. MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models

**Authors:** Hojung Jung, Rodrigo Hormazabal, Jaehyeong Jo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17602v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17602v1)

**Summary:** Molecular generation with diffusion models has emerged as a promising direction for AI-driven drug discovery and materials science. While graph diffusion models have been widely adopted due to the discrete nature of 2D molecular graphs, existing models suffer from low chemical validity and struggle to meet the desired properties compared to 1D modeling. In this work, we introduce MolHIT, a powerful molecular graph generation framework that overcomes long-standing performance limitations in exist...

---

### 14. The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?

**Authors:** Jayadev Billa

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17598v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17598v1)

**Summary:** Current speech LLMs largely perform implicit ASR: on tasks solvable from a transcript, they are behaviorally and mechanistically equivalent to simple Whisper$\to$LLM cascades. We show this through matched-backbone testing across four speech LLMs and six tasks, controlling for the LLM backbone for the first time. Ultravox is statistically indistinguishable from its matched cascade ($κ{=}0.93$); logit lens reveals literal text emerging in hidden states; LEACE concept erasure confirms text represen...

---

### 15. AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games

**Authors:** Lance Ying, Ryan Truong, Prafull Sharma, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17594v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17594v1)

**Summary:** Rigorously evaluating machine intelligence against the broad spectrum of human general intelligence has become increasingly important and challenging in this era of rapid technological advance. Conventional AI benchmarks typically assess only narrow capabilities in a limited range of human activity. Most are also static, quickly saturating as developers explicitly or implicitly optimize for them. We propose that a more promising way to evaluate human-like general intelligence in AI systems is th...

---

### 16. Conditional Flow Matching for Continuous Anomaly Detection in Autonomous Driving on a Manifold-Aware Spectral Space

**Authors:** Antonio Guillen-Perez

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17586v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17586v1)

**Summary:** Safety validation for Level 4 autonomous vehicles (AVs) is currently bottlenecked by the inability to scale the detection of rare, high-risk long-tail scenarios using traditional rule-based heuristics. We present Deep-Flow, an unsupervised framework for safety-critical anomaly detection that utilizes Optimal Transport Conditional Flow Matching (OT-CFM) to characterize the continuous probability density of expert human driving behavior. Unlike standard generative approaches that operate in unstab...

---

### 17. Be Wary of Your Time Series Preprocessing

**Authors:** Sofiane Ennadir, Tianze Wang, Oleg Smirnov, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17568v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17568v1)

**Summary:** Normalization and scaling are fundamental preprocessing steps in time series modeling, yet their role in Transformer-based models remains underexplored from a theoretical perspective. In this work, we present the first formal analysis of how different normalization strategies, specifically instance-based and global scaling, impact the expressivity of Transformer-based architectures for time series representation learning. We propose a novel expressivity framework tailored to time series, which q...

---

### 18. A Hybrid Federated Learning Based Ensemble Approach for Lung Disease Diagnosis Leveraging Fusion of SWIN Transformer and CNN

**Authors:** Asif Hasan Chowdhury, Md. Fahim Islam, M Ragib Anjum Riad, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17566v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17566v1)

**Summary:** The significant advancements in computational power cre- ate a vast opportunity for using Artificial Intelligence in different ap- plications of healthcare and medical science. A Hybrid FL-Enabled Ensemble Approach For Lung Disease Diagnosis Leveraging a Combination of SWIN Transformer and CNN is the combination of cutting-edge technology of AI and Federated Learning. Since, medi- cal specialists and hospitals will have shared data space, based on that data, with the help of Artificial Intellige...

---

### 19. ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment

**Authors:** Hongjue Zhao, Haosen Sun, Jiangtao Kong, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17560v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17560v1)

**Summary:** Activation steering, or representation engineering, offers a lightweight approach to align large language models (LLMs) by manipulating their internal activations at inference time. However, current methods suffer from two key limitations: \textit{(i)} the lack of a unified theoretical framework for guiding the design of steering directions, and \textit{(ii)} an over-reliance on \textit{one-step steering} that fail to capture complex patterns of activation distributions. In this work, we propose...

---

### 20. Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis

**Authors:** Minheng Chen, Jing Zhang, Tong Chen, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17557v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17557v1)

**Summary:** Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, viol...

---

### 21. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

**Authors:** Xiaoliang Fu, Jiaye Lin, Yangyi Fang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17550v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17550v1)

**Summary:** Existing Reinforcement Learning with Verifiable Rewards (RLVR) algorithms, such as GRPO, rely on rigid, uniform, and symmetric trust region mechanisms that are fundamentally misaligned with the complex optimization dynamics of Large Language Models (LLMs). In this paper, we identify three critical challenges in these methods: (1) inefficient gradient utilization caused by the binary cutoff of hard clipping, (2) insensitive probability mass arising from uniform ratio constraints that ignore the t...

---

### 22. KLong: Training LLM Agent for Extremely Long-horizon Tasks

**Authors:** Yue Liu, Zhiyuan Hu, Flood Sung, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17547v1)

**Summary:** This paper introduces KLong, an open-source LLM agent trained to solve extremely long-horizon tasks. The principle is to first cold-start the model via trajectory-splitting SFT, then scale it via progressive RL training. Specifically, we first activate basic agentic abilities of a base model with a comprehensive SFT recipe. Then, we introduce Research-Factory, an automated pipeline that generates high-quality training data by collecting research papers and constructing evaluation rubrics. Using ...

---

### 23. Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability

**Authors:** Shashank Aggarwal, Ram Vikas Mishra, Amit Awekar

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17544v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17544v1)

**Summary:** In multi-agent IR pipelines for tasks such as search and ranking, LLM-based agents exchange intermediate reasoning in terms of Chain-of-Thought (CoT) with each other. Current CoT evaluation narrowly focuses on target task accuracy. However, this metric fails to assess the quality or utility of the reasoning process itself. To address this limitation, we introduce two novel measures: reusability and verifiability. We decouple CoT generation from execution using a Thinker-Executor framework. Reusa...

---

### 24. Toward a Fully Autonomous, AI-Native Particle Accelerator

**Authors:** Chris Tennant

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17536v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17536v1)

**Summary:** This position paper presents a vision for self-driving particle accelerators that operate autonomously with minimal human intervention. We propose that future facilities be designed through artificial intelligence (AI) co-design, where AI jointly optimizes the accelerator lattice, diagnostics, and science application from inception to maximize performance while enabling autonomous operation. Rather than retrofitting AI onto human-centric systems, we envision facilities designed from the ground u...

---

### 25. Systematic Evaluation of Single-Cell Foundation Model Interpretability Reveals Attention Captures Co-Expression Rather Than Unique Regulatory Signal

**Authors:** Ihor Kendiukhov

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17532v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17532v1)

**Summary:** We present a systematic evaluation framework - thirty-seven analyses, 153 statistical tests, four cell types, two perturbation modalities - for assessing mechanistic interpretability in single-cell foundation models. Applying this framework to scGPT and Geneformer, we find that attention patterns encode structured biological information with layer-specific organisation - protein-protein interactions in early layers, transcriptional regulation in late layers - but this structure provides no incre...

---

### 26. Position: Evaluation of ECG Representations Must Be Fixed

**Authors:** Zachary Berger, Daniel Prakah-Asante, John Guttag, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17531v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17531v1)

**Summary:** This position paper argues that current benchmarking practice in 12-lead ECG representation learning must be fixed to ensure progress is reliable and aligned with clinically meaningful objectives. The field has largely converged on three public multi-label benchmarks (PTB-XL, CPSC2018, CSN) dominated by arrhythmia and waveform-morphology labels, even though the ECG is known to encode substantially broader clinical information. We argue that downstream evaluation should expand to include an asses...

---

### 27. Enhancing Large Language Models (LLMs) for Telecom using Dynamic Knowledge Graphs and Explainable Retrieval-Augmented Generation

**Authors:** Dun Yuan, Hao Zhou, Xue Liu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17529v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17529v1)

**Summary:** Large language models (LLMs) have shown strong potential across a variety of tasks, but their application in the telecom field remains challenging due to domain complexity, evolving standards, and specialized terminology. Therefore, general-domain LLMs may struggle to provide accurate and reliable outputs in this context, leading to increased hallucinations and reduced utility in telecom operations.To address these limitations, this work introduces KG-RAG-a novel framework that integrates knowle...

---

### 28. The Anxiety of Influence: Bloom Filters in Transformer Attention Heads

**Authors:** Peter Balogh

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17526v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17526v1)

**Summary:** Some transformer attention heads appear to function as membership testers, dedicating themselves to answering the question "has this token appeared before in the context?" We identify these heads across four language models (GPT-2 small, medium, and large; Pythia-160M) and show that they form a spectrum of membership-testing strategies. Two heads (L0H1 and L0H5 in GPT-2 small) function as high-precision membership filters with false positive rates of 0-4\% even at 180 unique context tokens -- we...

---

### 29. LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights

**Authors:** Kasun Dewage, Marianna Pensky, Suranadi De Silva, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17510v1)

**Summary:** We introduce CRAFT (Cross-layer Rank Adaptation via Frozen Tucker), a parameter-efficient fine-tuning (PEFT) method that applies Tucker tensor decomposition to pre-trained attention weight matrices stacked across transformer layers and trains only small square adaptation matrices on the resulting frozen Tucker factors. Existing tensor-based PEFT methods decompose gradient updates: LoTR applies Tucker decomposition with shared factor matrices, while SuperLoRA groups and reshapes $ΔW$ across layer...

---

### 30. Pareto Optimal Benchmarking of AI Models on ARM Cortex Processors for Sustainable Embedded Systems

**Authors:** Pranay Jain, Maximilian Kasper, Göran Köber, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17508v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17508v1)

**Summary:** This work presents a practical benchmarking framework for optimizing artificial intelligence (AI) models on ARM Cortex processors (M0+, M4, M7), focusing on energy efficiency, accuracy, and resource utilization in embedded systems. Through the design of an automated test bench, we provide a systematic approach to evaluate across key performance indicators (KPIs) and identify optimal combinations of processor and AI model. The research highlights a nearlinear correlation between floating-point op...

---

### 31. Learning with Boolean threshold functions

**Authors:** Veit Elser, Manish Krishan Lal

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17493v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17493v1)

**Summary:** We develop a method for training neural networks on Boolean data in which the values at all nodes are strictly $\pm 1$, and the resulting models are typically equivalent to networks whose nonzero weights are also $\pm 1$. The method replaces loss minimization with a nonconvex constraint formulation. Each node implements a Boolean threshold function (BTF), and training is expressed through a divide-and-concur decomposition into two complementary constraints: one enforces local BTF consistency bet...

---

### 32. Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection

**Authors:** Yichen Lu, Siwei Nie, Minlong Lu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17484v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17484v1)

**Summary:** Image Copy Detection (ICD) aims to identify manipulated content between image pairs through robust feature representation learning. While self-supervised learning (SSL) has advanced ICD systems, existing view-level contrastive methods struggle with sophisticated edits due to insufficient fine-grained correspondence learning. We address this limitation by exploiting the inherent geometric traceability in edited content through two key innovations. First, we propose PixTrace - a pixel coordinate t...

---

### 33. What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data

**Authors:** Dimitri Staufer, Kirsten Morehouse

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17483v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17483v1)

**Summary:** Large language models (LLMs), and conversational agents based on them, are exposed to personal data (PD) during pre-training and during user interactions. Prior work shows that PD can resurface, yet users lack insight into how strongly models associate specific information to their identity. We audit PD across eight LLMs (3 open-source; 5 API-based, including GPT-4o), introduce LMP2 (Language Model Privacy Probe), a human-centered, privacy-preserving audit tool refined through two formative stud...

---

### 34. Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge

**Authors:** Wyatt Benno, Alberto Centelles, Antoine Douchet, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17452v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17452v1)

**Summary:** We present Jolt Atlas, a zero-knowledge machine learning (zkML) framework that extends the Jolt proving system to model inference. Unlike zkVMs (zero-knowledge virtual machines), which emulate CPU instruction execution, Jolt Atlas adapts Jolt's lookup-centric approach and applies it directly to ONNX tensor operations. The ONNX computational model eliminates the need for CPU registers and simplifies memory consistency verification. In addition, ONNX is an open-source, portable format, which makes...

---

### 35. Beyond Pipelines: A Fundamental Study on the Rise of Generative-Retrieval Architectures in Web Research

**Authors:** Amirereza Abbasi, Mohsen Hooshmand

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17450v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17450v1)

**Summary:** Web research and practices have evolved significantly over time, offering users diverse and accessible solutions across a wide range of tasks. While advanced concepts such as Web 4.0 have emerged from mature technologies, the introduction of large language models (LLMs) has profoundly influenced both the field and its applications. This wave of LLMs has permeated science and technology so deeply that no area remains untouched. Consequently, LLMs are reshaping web research and development, transf...

---

### 36. WarpRec: Unifying Academic Rigor and Industrial Scale for Responsible, Reproducible, and Efficient Recommendation

**Authors:** Marco Avolio, Potito Aghilar, Sabino Roccotelli, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17442v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17442v1)

**Summary:** Innovation in Recommender Systems is currently impeded by a fractured ecosystem, where researchers must choose between the ease of in-memory experimentation and the costly, complex rewriting required for distributed industrial engines. To bridge this gap, we present WarpRec, a high-performance framework that eliminates this trade-off through a novel, backend-agnostic architecture. It includes 50+ state-of-the-art algorithms, 40 metrics, and 19 filtering and splitting strategies that seamlessly t...

---

### 37. Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study

**Authors:** Dylan Bouchard, Mohit Singh Chauhan, Viren Bajaj, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17431v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17431v1)

**Summary:** Uncertainty quantification has emerged as an effective approach to closed-book hallucination detection for LLMs, but existing methods are largely designed for short-form outputs and do not generalize well to long-form generation. We introduce a taxonomy for fine-grained uncertainty quantification in long-form LLM outputs that distinguishes methods by design choices at three stages: response decomposition, unit-level scoring, and response-level aggregation. We formalize several families of consis...

---

### 38. Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking

**Authors:** Afroditi Kolomvaki, Fangshuo Liao, Evan Dramko, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17423v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17423v1)

**Summary:** We investigate the convergence guarantee of two-layer neural network training with Gaussian randomly masked inputs. This scenario corresponds to Gaussian dropout at the input level, or noisy input training common in sensor networks, privacy-preserving training, and federated learning, where each user may have access to partial or corrupted features. Using a Neural Tangent Kernel (NTK) analysis, we demonstrate that training a two-layer ReLU network with Gaussian randomly masked inputs achieves li...

---

### 39. A Privacy by Design Framework for Large Language Model-Based Applications for Children

**Authors:** Diana Addae, Diana Rogachova, Nafiseh Kahani, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17418v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17418v1)

**Summary:** Children are increasingly using technologies powered by Artificial Intelligence (AI). However, there are growing concerns about privacy risks, particularly for children. Although existing privacy regulations require companies and organizations to implement protections, doing so can be challenging in practice. To address this challenge, this article proposes a framework based on Privacy-by-Design (PbD), which guides designers and developers to take on a proactive and risk-averse approach to techn...

---

### 40. Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers

**Authors:** Bingqian Li, Bowen Zheng, Xiaolei Wang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17410v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17410v1)

**Summary:** Large language models (LLMs) have shown great promise in recommender systems, where supervised fine-tuning (SFT) is commonly used for adaptation. Subsequent studies further introduce preference learning to incorporate negative samples into the training process. However, existing methods rely on sequence-level, offline-generated negatives, making them less discriminative and informative when adapting LLMs to recommendation tasks with large negative item spaces. To address these challenges, we pro...

---

### 41. A Contrastive Variational AutoEncoder for NSCLC Survival Prediction with Missing Modalities

**Authors:** Michele Zanitti, Vanja Miskovic, Francesco Trovò, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17402v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17402v1)

**Summary:** Predicting survival outcomes for non-small cell lung cancer (NSCLC) patients is challenging due to the different individual prognostic features. This task can benefit from the integration of whole-slide images, bulk transcriptomics, and DNA methylation, which offer complementary views of the patient's condition at diagnosis. However, real-world clinical datasets are often incomplete, with entire modalities missing for a significant fraction of patients. State-of-the-art models rely on available ...

---

### 42. A High-Level Survey of Optical Remote Sensing

**Authors:** Panagiotis Koletsis, Vasilis Efthymiou, Maria Vakalopoulou, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17397v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17397v1)

**Summary:** In recent years, significant advances in computer vision have also propelled progress in remote sensing. Concurrently, the use of drones has expanded, with many organizations incorporating them into their operations. Most drones are equipped by default with RGB cameras, which are both robust and among the easiest sensors to use and interpret. The body of literature on optical remote sensing is vast, encompassing diverse tasks, capabilities, and methodologies. Each task or methodology could warra...

---

### 43. SpectralGCD: Spectral Concept Selection and Cross-modal Representation Learning for Generalized Category Discovery

**Authors:** Lorenzo Caselli, Marco Mistretta, Simone Magistri, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17395v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17395v1)

**Summary:** Generalized Category Discovery (GCD) aims to identify novel categories in unlabeled data while leveraging a small labeled subset of known classes. Training a parametric classifier solely on image features often leads to overfitting to old classes, and recent multimodal approaches improve performance by incorporating textual information. However, they treat modalities independently and incur high computational cost. We propose SpectralGCD, an efficient and effective multimodal approach to GCD tha...

---

### 44. Voice-Driven Semantic Perception for UAV-Assisted Emergency Networks

**Authors:** Nuno Saavedra, Pedro Ribeiro, André Coelho, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17394v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17394v1)

**Summary:** Unmanned Aerial Vehicle (UAV)-assisted networks are increasingly foreseen as a promising approach for emergency response, providing rapid, flexible, and resilient communications in environments where terrestrial infrastructure is degraded or unavailable. In such scenarios, voice radio communications remain essential for first responders due to their robustness; however, their unstructured nature prevents direct integration with automated UAV-assisted network management. This paper proposes SIREN...

---

### 45. Visual Model Checking: Graph-Based Inference of Visual Routines for Image Retrieval

**Authors:** Adrià Molina, Oriol Ramos Terrades, Josep Lladós

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17386v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17386v1)

**Summary:** Information retrieval lies at the foundation of the modern digital industry. While natural language search has seen dramatic progress in recent years largely driven by embedding-based models and large-scale pretraining, the field still faces significant challenges. Specifically, queries that involve complex relationships, object compositions, or precise constraints such as identities, counts and proportions often remain unresolved or unreliable within current frameworks. In this paper, we propos...

---

### 46. Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature

**Authors:** Angelo Porrello, Pietro Buzzega, Felix Dangel, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17385v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17385v1)

**Summary:** Task Arithmetic yields a modular, scalable way to adapt foundation models. Combining multiple task vectors, however, can lead to cross-task interference, causing representation drift and degraded performance. Representation drift regularization provides a natural remedy to disentangle task vectors; however, existing approaches typically require external task data, conflicting with modularity and data availability constraints (e.g., privacy requirements). We propose a dataless approach by framing...

---

### 47. A feature-stable and explainable machine learning framework for trustworthy decision-making under incomplete clinical data

**Authors:** Justyna Andrys-Olek, Paulina Tworek, Luca Gherardini, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17364v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17364v1)

**Summary:** Machine learning models are increasingly applied to biomedical data, yet their adoption in high stakes domains remains limited by poor robustness, limited interpretability, and instability of learned features under realistic data perturbations, such as missingness. In particular, models that achieve high predictive performance may still fail to inspire trust if their key features fluctuate when data completeness changes, undermining reproducibility and downstream decision-making. Here, we presen...

---

### 48. What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?

**Authors:** Boyang Ma, Hechuan Guo, Peizhuo Lv, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17345v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17345v1)

**Summary:** Embodied AI systems (e.g., autonomous vehicles, service robots, and LLM-driven interactive agents) are rapidly transitioning from controlled environments to safety critical real-world deployments. Unlike disembodied AI, failures in embodied intelligence lead to irreversible physical consequences, raising fundamental questions about security, safety, and reliability. While existing research predominantly analyzes embodied AI through the lenses of Large Language Model (LLM) vulnerabilities or clas...

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

## cs.CV

**50 papers**

### 1. OpenEarthAgent: A Unified Framework for Tool-Augmented Geospatial Agents

**Authors:** Akashah Shabbir, Muhammad Umer Sheikh, Muhammad Akhtar Munir, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17665v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17665v1)

**Summary:** Recent progress in multimodal reasoning has enabled agents that can interpret imagery, connect it with language, and perform structured analytical tasks. Extending such capabilities to the remote sensing domain remains challenging, as models must reason over spatial scale, geographic structures, and multispectral indices while maintaining coherent multi-step logic. To bridge this gap, OpenEarthAgent introduces a unified framework for developing tool-augmented geospatial agents trained on satelli...

---

### 2. When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

**Authors:** Yu Fang, Yuchun Feng, Dong Jing, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17659v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17659v1)

**Summary:** Vision-Language-Action models (VLAs) promise to ground language instructions in robot control, yet in practice often fail to faithfully follow language. When presented with instructions that lack strong scene-specific supervision, VLAs suffer from counterfactual failures: they act based on vision shortcuts induced by dataset biases, repeatedly executing well-learned behaviors and selecting objects frequently seen during training regardless of language intent. To systematically study it, we intro...

---

### 3. Human-level 3D shape perception emerges from multi-view learning

**Authors:** Tyler Bonnen, Jitendra Malik, Angjoo Kanazawa

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17650v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17650v1)

**Summary:** Humans can infer the three-dimensional structure of objects from two-dimensional visual inputs. Modeling this ability has been a longstanding goal for the science and engineering of visual intelligence, yet decades of computational methods have fallen short of human performance. Here we develop a modeling framework that predicts human 3D shape inferences for arbitrary objects, directly from experimental stimuli. We achieve this with a novel class of neural networks trained using a visual-spatial...

---

### 4. Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting

**Authors:** Xiaohan Zhao, Zhaoyi Li, Yaxin Luo, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17645v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17645v1)

**Summary:** Black-box adversarial attacks on Large Vision-Language Models (LVLMs) are challenging due to missing gradients and complex multimodal boundaries. While prior state-of-the-art transfer-based approaches like M-Attack perform well using local crop-level matching between source and target images, we find this induces high-variance, nearly orthogonal gradients across iterations, violating coherent local alignment and destabilizing optimization. We attribute this to (i) ViT translation sensitivity tha...

---

### 5. IntRec: Intent-based Retrieval with Contrastive Refinement

**Authors:** Pourya Shamsolmoali, Masoumeh Zareapoor, Eric Granger, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17639v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17639v1)

**Summary:** Retrieving user-specified objects from complex scenes remains a challenging task, especially when queries are ambiguous or involve multiple similar objects. Existing open-vocabulary detectors operate in a one-shot manner, lacking the ability to refine predictions based on user feedback. To address this, we propose IntRec, an interactive object retrieval framework that refines predictions based on user feedback. At its core is an Intent State (IS) that maintains dual memory sets for positive anch...

---

### 6. CORAL: Correspondence Alignment for Improved Virtual Try-On

**Authors:** Jiyoung Kim, Youngjin Shin, Siyoon Jin, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17636v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17636v1)

**Summary:** Existing methods for Virtual Try-On (VTON) often struggle to preserve fine garment details, especially in unpaired settings where accurate person-garment correspondence is required. These methods do not explicitly enforce person-garment alignment and fail to explain how correspondence emerges within Diffusion Transformers (DiTs). In this paper, we first analyze full 3D attention in DiT-based architecture and reveal that the person-garment correspondence critically depends on precise person-garme...

---

### 7. Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery

**Authors:** Jowaria Khan, Anindya Sarkar, Yevgeniy Vorobeychik, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17605v1)

**Summary:** In many real-world settings, such as environmental monitoring, disaster response, or public health, with costly and difficult data collection and dynamic environments, strategically sampling from unobserved regions is essential for efficiently uncovering hidden targets under tight resource constraints. Yet, sparse and biased geospatial ground truth limits the applicability of existing learning-based methods, such as reinforcement learning. To address this, we propose a unified geospatial discove...

---

### 8. Art2Mus: Artwork-to-Music Generation via Visual Conditioning and Large-Scale Cross-Modal Alignment

**Authors:** Ivan Rinaldi, Matteo Mendula, Nicola Fanelli, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17599v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17599v1)

**Summary:** Music generation has advanced markedly through multimodal deep learning, enabling models to synthesize audio from text and, more recently, from images. However, existing image-conditioned systems suffer from two fundamental limitations: (i) they are typically trained on natural photographs, limiting their ability to capture the richer semantic, stylistic, and cultural content of artworks; and (ii) most rely on an image-to-text conversion stage, using language as a semantic shortcut that simplifi...

---

### 9. FR-GESTURE: An RGBD Dataset For Gesture-based Human-Robot Interaction In First Responder Operations

**Authors:** Konstantinos Foteinos, Georgios Angelidis, Aggelos Psiris, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17573v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17573v1)

**Summary:** The ever increasing intensity and number of disasters make even more difficult the work of First Responders (FRs). Artificial intelligence and robotics solutions could facilitate their operations, compensating these difficulties. To this end, we propose a dataset for gesture-based UGV control by FRs, introducing a set of 12 commands, drawing inspiration from existing gestures used by FRs and tactical hand signals and refined after incorporating feedback from experienced FRs. Then we proceed with...

---

### 10. RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward

**Authors:** Qiucheng Wu, Jing Shi, Simon Jenni, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17558v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17558v1)

**Summary:** Recent advances in multimodal large language models (MLLMs) have shown great potential for extending vision-language reasoning to professional tool-based image editing, enabling intuitive and creative editing. A promising direction is to use reinforcement learning (RL) to enable MLLMs to reason about and execute optimal tool-use plans within professional image-editing software. However, training remains challenging due to the lack of reliable, verifiable reward signals that can reflect the inher...

---

### 11. Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis

**Authors:** Minheng Chen, Jing Zhang, Tong Chen, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17557v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17557v1)

**Summary:** Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, viol...

---

### 12. Neural Implicit Representations for 3D Synthetic Aperture Radar Imaging

**Authors:** Nithin Sugavanam, Emre Ertin

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17556v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17556v1)

**Summary:** Synthetic aperture radar (SAR) is a tomographic sensor that measures 2D slices of the 3D spatial Fourier transform of the scene. In many operational scenarios, the measured set of 2D slices does not fill the 3D space in the Fourier domain, resulting in significant artifacts in the reconstructed imagery. Traditionally, simple priors, such as sparsity in the image domain, are used to regularize the inverse problem. In this paper, we review our recent work that achieves state-of-the-art results in ...

---

### 13. GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking

**Authors:** Zixu Cheng, Da Li, Jian Hu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17555v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17555v1)

**Summary:** Video reasoning requires understanding the causal relationships between events in a video. However, such relationships are often implicit and costly to annotate manually. While existing multimodal large language models (MLLMs) often infer event relations through dense captions or video summaries for video reasoning, such modeling still lacks causal understanding. Without explicit causal structure modeling within and across video events, these models suffer from hallucinations during the video re...

---

### 14. LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs

**Authors:** Behzad Bozorgtabar, Dwarikanath Mahapatra, Sudipta Roy, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17535v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17535v1)

**Summary:** Medical vision-language models (VLMs) are strong zero-shot recognizers for medical imaging, but their reliability under domain shift hinges on calibrated uncertainty with guarantees. Split conformal prediction (SCP) offers finite-sample coverage, yet prediction sets often become large (low efficiency) and class-wise coverage unbalanced-high class-conditioned coverage gap (CCV), especially in few-shot, imbalanced regimes; moreover, naively adapting to calibration labels breaks exchangeability and...

---

### 15. FoundationPose-Initialized 3D-2D Liver Registration for Surgical Augmented Reality

**Authors:** Hanyuan Zhang, Lucas He, Runlong He, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17517v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17517v1)

**Summary:** Augmented reality can improve tumor localization in laparoscopic liver surgery. Existing registration pipelines typically depend on organ contours; deformable (non-rigid) alignment is often handled with finite-element (FE) models coupled to dimensionality-reduction or machine-learning components. We integrate laparoscopic depth maps with a foundation pose estimator for camera-liver pose estimation and replace FE-based deformation with non-rigid iterative closest point (NICP) to lower engineering...

---

### 16. Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection

**Authors:** Yichen Lu, Siwei Nie, Minlong Lu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17484v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17484v1)

**Summary:** Image Copy Detection (ICD) aims to identify manipulated content between image pairs through robust feature representation learning. While self-supervised learning (SSL) has advanced ICD systems, existing view-level contrastive methods struggle with sophisticated edits due to insufficient fine-grained correspondence learning. We address this limitation by exploiting the inherent geometric traceability in edited content through two key innovations. First, we propose PixTrace - a pixel coordinate t...

---

### 17. QuPAINT: Physics-Aware Instruction Tuning Approach to Quantum Material Discovery

**Authors:** Xuan-Bac Nguyen, Hoang-Quan Nguyen, Sankalp Pandey, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17478v1)

**Summary:** Characterizing two-dimensional quantum materials from optical microscopy images is challenging due to the subtle layer-dependent contrast, limited labeled data, and significant variation across laboratories and imaging setups. Existing vision models struggle in this domain since they lack physical priors and cannot generalize to new materials or hardware conditions. This work presents a new physics-aware multimodal framework that addresses these limitations from both the data and model perspecti...

---

### 18. 4D Monocular Surgical Reconstruction under Arbitrary Camera Motions

**Authors:** Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17473v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17473v1)

**Summary:** Reconstructing deformable surgical scenes from endoscopic videos is challenging and clinically important. Recent state-of-the-art methods based on implicit neural representations or 3D Gaussian splatting have made notable progress. However, most are designed for deformable scenes with fixed endoscope viewpoints and rely on stereo depth priors or accurate structure-from-motion for initialization and optimization, limiting their ability to handle monocular sequences with large camera motion in rea...

---

### 19. EAGLE: Expert-Augmented Attention Guidance for Tuning-Free Industrial Anomaly Detection in Multimodal Large Language Models

**Authors:** Xiaomeng Peng, Xilang Huang, Seon Han Choi

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17419v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17419v1)

**Summary:** Industrial anomaly detection is important for smart manufacturing, but many deep learning approaches produce only binary decisions and provide limited semantic explanations. Multimodal large language models (MLLMs) can potentially generate fine-grained, language-based analyses, yet existing methods often require costly fine-tuning and do not consistently improve anomaly detection accuracy compared to lightweight specialist detectors. We propose expert-augmented attention guidance for industrial ...

---

### 20. A High-Level Survey of Optical Remote Sensing

**Authors:** Panagiotis Koletsis, Vasilis Efthymiou, Maria Vakalopoulou, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17397v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17397v1)

**Summary:** In recent years, significant advances in computer vision have also propelled progress in remote sensing. Concurrently, the use of drones has expanded, with many organizations incorporating them into their operations. Most drones are equipped by default with RGB cameras, which are both robust and among the easiest sensors to use and interpret. The body of literature on optical remote sensing is vast, encompassing diverse tasks, capabilities, and methodologies. Each task or methodology could warra...

---

### 21. SpectralGCD: Spectral Concept Selection and Cross-modal Representation Learning for Generalized Category Discovery

**Authors:** Lorenzo Caselli, Marco Mistretta, Simone Magistri, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17395v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17395v1)

**Summary:** Generalized Category Discovery (GCD) aims to identify novel categories in unlabeled data while leveraging a small labeled subset of known classes. Training a parametric classifier solely on image features often leads to overfitting to old classes, and recent multimodal approaches improve performance by incorporating textual information. However, they treat modalities independently and incur high computational cost. We propose SpectralGCD, an efficient and effective multimodal approach to GCD tha...

---

### 22. DRetHTR: Linear-Time Decoder-Only Retentive Network for Handwritten Text Recognition

**Authors:** Changhun Kim, Martin Mayr, Thomas Gorges, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17387v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17387v1)

**Summary:** State-of-the-art handwritten text recognition (HTR) systems commonly use Transformers, whose growing key-value (KV) cache makes decoding slow and memory-intensive. We introduce DRetHTR, a decoder-only model built on Retentive Networks (RetNet). Compared to an equally sized decoder-only Transformer baseline, DRetHTR delivers 1.6-1.9x faster inference with 38-42% less memory usage, without loss of accuracy. By replacing softmax attention with softmax-free retention and injecting multi-scale sequen...

---

### 23. Tree crop mapping of South America reveals links to deforestation and conservation

**Authors:** Yuchang Jiang, Anton Raichuk, Xiaoye Tong, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17372v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17372v1)

**Summary:** Monitoring tree crop expansion is vital for zero-deforestation policies like the European Union's Regulation on Deforestation-free Products (EUDR). However, these efforts are hindered by a lack of highresolution data distinguishing diverse agricultural systems from forests. Here, we present the first 10m-resolution tree crop map for South America, generated using a multi-modal, spatio-temporal deep learning model trained on Sentinel-1 and Sentinel-2 satellite imagery time series. The map identif...

---

### 24. Application and Evaluation of the Common Circles Method

**Authors:** Michael Quellmalz, Mia Kvåle Løvmo, Simon Moser, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17353v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17353v1)

**Summary:** We investigate the application of the common circle method for estimating sample motion in optical diffraction tomography (ODT) of sub-millimeter sized biological tissue. When samples are confined via contact-free acoustical force fields, their motion must be estimated from the captured images. The common circle method identifies intersections of Ewald spheres in Fourier space to determine rotational motion. This paper presents a practical implementation, incorporating temporal consistency const...

---

### 25. Polaffini: A feature-based approach for robust affine and polyaffine image registration

**Authors:** Antoine Legouhy, Cosimo Campo, Ross Callaghan, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17337v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17337v1)

**Summary:** In this work we present Polaffini, a robust and versatile framework for anatomically grounded registration. Medical image registration is dominated by intensity-based registration methods that rely on surrogate measures of alignment quality. In contrast, feature-based approaches that operate by identifying explicit anatomical correspondences, while more desirable in theory, have largely fallen out of favor due to the challenges of reliably extracting features. However, such challenges are now si...

---

### 26. Leveraging Contrastive Learning for a Similarity-Guided Tampered Document Data Generation Pipeline

**Authors:** Mohamed Dhouib, Davide Buscaldi, Sonia Vanier, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17322v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17322v1)

**Summary:** Detecting tampered text in document images is a challenging task due to data scarcity. To address this, previous work has attempted to generate tampered documents using rule-based methods. However, the resulting documents often suffer from limited variety and poor visual quality, typically leaving highly visible artifacts that are rarely observed in real-world manipulations. This undermines the model's ability to learn robust, generalizable features and results in poor performance on real-world ...

---

### 27. The Sound of Death: Deep Learning Reveals Vascular Damage from Carotid Ultrasound

**Authors:** Christoph Balada, Aida Romano-Martinez, Payal Varshney, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17321v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17321v1)

**Summary:** Cardiovascular diseases (CVDs) remain the leading cause of mortality worldwide, yet early risk detection is often limited by available diagnostics. Carotid ultrasound, a non-invasive and widely accessible modality, encodes rich structural and hemodynamic information that is largely untapped. Here, we present a machine learning (ML) framework that extracts clinically meaningful representations of vascular damage (VD) from carotid ultrasound videos, using hypertension as a weak proxy label. The mo...

---

### 28. Attachment Anchors: A Novel Framework for Laparoscopic Grasping Point Prediction in Colorectal Surgery

**Authors:** Dennis N. Schneider, Lars Wagner, Daniel Rueckert, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17310v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17310v1)

**Summary:** Accurate grasping point prediction is a key challenge for autonomous tissue manipulation in minimally invasive surgery, particularly in complex and variable procedures such as colorectal interventions. Due to their complexity and prolonged duration, colorectal procedures have been underrepresented in current research. At the same time, they pose a particularly interesting learning environment due to repetitive tissue manipulation, making them a promising entry point for autonomous, machine learn...

---

### 29. Physics Encoded Spatial and Temporal Generative Adversarial Network for Tropical Cyclone Image Super-resolution

**Authors:** Ruoyi Zhang, Jiawei Yuan, Lujia Ye, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17277v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17277v1)

**Summary:** High-resolution satellite imagery is indispensable for tracking the genesis, intensification, and trajectory of tropical cyclones (TCs). However, existing deep learning-based super-resolution (SR) methods often treat satellite image sequences as generic videos, neglecting the underlying atmospheric physical laws governing cloud motion. To address this, we propose a Physics Encoded Spatial and Temporal Generative Adversarial Network (PESTGAN) for TC image super-resolution. Specifically, we design...

---

### 30. Unified Latents (UL): How to train your latents

**Authors:** Jonathan Heek, Emiel Hoogeboom, Thomas Mensink, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17270v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17270v1)

**Summary:** We present Unified Latents (UL), a framework for learning latent representations that are jointly regularized by a diffusion prior and decoded by a diffusion model. By linking the encoder's output noise to the prior's minimum noise level, we obtain a simple training objective that provides a tight upper bound on the latent bitrate. On ImageNet-512, our approach achieves competitive FID of 1.4, with high reconstruction quality (PSNR) while requiring fewer training FLOPs than models trained on Sta...

---

### 31. EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection

**Authors:** Hung Mai, Loi Dinh, Duc Hai Nguyen, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17260v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17260v1)

**Summary:** Recent advances in foundation video generators such as Sora2, Veo3, and other commercial systems have produced highly realistic synthetic videos, exposing the limitations of existing detection methods that rely on shallow embedding trajectories, image-based adaptation, or computationally heavy MLLMs. We propose EA-Swin, an Embedding-Agnostic Swin Transformer that models spatiotemporal dependencies directly on pretrained video embeddings via a factorized windowed attention design, making it compa...

---

### 32. A Multi-modal Detection System for Infrastructure-based Freight Signal Priority

**Authors:** Ziyan Zhang, Chuheng Wei, Xuanpeng Zhao, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17252v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17252v1)

**Summary:** Freight vehicles approaching signalized intersections require reliable detection and motion estimation to support infrastructure-based Freight Signal Priority (FSP). Accurate and timely perception of vehicle type, position, and speed is essential for enabling effective priority control strategies. This paper presents the design, deployment, and evaluation of an infrastructure-based multi-modal freight vehicle detection system integrating LiDAR and camera sensors. A hybrid sensing architecture is...

---

### 33. Inferring Height from Earth Embeddings: First insights using Google AlphaEarth

**Authors:** Alireza Hamoudzadeh, Valeria Belloni, Roberta Ravanelli

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17250v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17250v1)

**Summary:** This study investigates whether the geospatial and multimodal features encoded in \textit{Earth Embeddings} can effectively guide deep learning (DL) regression models for regional surface height mapping. In particular, we focused on AlphaEarth Embeddings at 10 m spatial resolution and evaluated their capability to support terrain height inference using a high-quality Digital Surface Model (DSM) as reference. U-Net and U-Net++ architectures were thus employed as lightweight convolutional decoders...

---

### 34. HiMAP: History-aware Map-occupancy Prediction with Fallback

**Authors:** Yiming Xu, Yi Yang, Hao Cheng, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17231v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17231v1)

**Summary:** Accurate motion forecasting is critical for autonomous driving, yet most predictors rely on multi-object tracking (MOT) with identity association, assuming that objects are correctly and continuously tracked. When tracking fails due to, e.g., occlusion, identity switches, or missed detections, prediction quality degrades and safety risks increase. We present \textbf{HiMAP}, a tracking-free, trajectory prediction framework that remains reliable under MOT failures. HiMAP converts past detections i...

---

### 35. GASS: Geometry-Aware Spherical Sampling for Disentangled Diversity Enhancement in Text-to-Image Generation

**Authors:** Ye Zhu, Kaleb S. Newman, Johannes F. Lutzeyer, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17200v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17200v1)

**Summary:** Despite high semantic alignment, modern text-to-image (T2I) generative models still struggle to synthesize diverse images from a given prompt. This lack of diversity not only restricts user choice, but also risks amplifying societal biases. In this work, we enhance the T2I diversity through a geometric lens. Unlike most existing methods that rely primarily on entropy-based guidance to increase sample dissimilarity, we introduce Geometry-Aware Spherical Sampling (GASS) to enhance diversity by exp...

---

### 36. EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models

**Authors:** Yahong Wang, Juncheng Wu, Zhangkai Ni, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17196v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17196v1)

**Summary:** Multimodal large language models (MLLMs) incur substantial inference cost due to the processing of hundreds of visual tokens per image. Although token pruning has proven effective for accelerating inference, determining when and where to prune remains largely heuristic. Existing approaches typically rely on static, empirically selected layers, which limit interpretability and transferability across models. In this work, we introduce a matrix-entropy perspective and identify an "Entropy Collapse ...

---

### 37. Texo: Formula Recognition within 20M Parameters

**Authors:** Sicheng Mao

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17189v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17189v1)

**Summary:** In this paper we present Texo, a minimalist yet highperformance formula recognition model that contains only 20 million parameters. By attentive design, distillation and transfer of the vocabulary and the tokenizer, Texo achieves comparable performance to state-of-the-art models such as UniMERNet-T and PPFormulaNet-S, while reducing the model size by 80% and 65%, respectively. This enables real-time inference on consumer-grade hardware and even in-browser deployment. We also developed a web appl...

---

### 38. Selective Training for Large Vision Language Models via Visual Information Gain

**Authors:** Seulbi Lee, Sangheum Hwang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17186v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17186v1)

**Summary:** Large Vision Language Models (LVLMs) have achieved remarkable progress, yet they often suffer from language bias, producing answers without relying on visual evidence. While prior work attempts to mitigate this issue through decoding strategies, architectural modifications, or curated instruction data, they typically lack a quantitative measure of how much individual training samples or tokens actually benefit from the image. In this work, we introduce Visual Information Gain (VIG), a perplexity...

---

### 39. NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting

**Authors:** Jiwei Shan, Zeyu Cai, Yirui Li, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17182v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17182v1)

**Summary:** Visual simultaneous localization and mapping (V-SLAM) is a fundamental capability for autonomous perception and navigation. However, endoscopic scenes violate the rigidity assumption due to persistent soft-tissue deformations, creating a strong coupling ambiguity between camera ego-motion and intrinsic deformation. Although recent monocular non-rigid SLAM methods have made notable progress, they often lack effective decoupling mechanisms and rely on sparse or low-fidelity scene representations, ...

---

### 40. BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning

**Authors:** Siyuan Liang, Yongcheng Jing, Yingjie Wang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17168v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17168v1)

**Summary:** Research on backdoor attacks against multimodal contrastive learning models faces two key challenges: stealthiness and persistence. Existing methods often fail under strong detection or continuous fine-tuning, largely due to (1) cross-modal inconsistency that exposes trigger patterns and (2) gradient dilution at low poisoning rates that accelerates backdoor forgetting. These coupled causes remain insufficiently modeled and addressed. We propose BadCLIP++, a unified framework that tackles both ch...

---

### 41. B$^3$-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates

**Authors:** Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17134v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17134v1)

**Summary:** Interactive 3D Gaussian Splatting (3DGS) segmentation is essential for real-time editing of pre-reconstructed assets in film and game production. However, existing methods rely on predefined camera viewpoints, ground-truth labels, or costly retraining, making them impractical for low-latency use. We propose B$^3$-Seg (Beta-Bernoulli Bayesian Segmentation for 3DGS), a fast and theoretically grounded method for open-vocabulary 3DGS segmentation under camera-free and training-free conditions. Our a...

---

### 42. 3D Scene Rendering with Multimodal Gaussian Splatting

**Authors:** Chi-Shiang Gau, Konstantinos D. Polyzos, Athanasios Bacharis, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17124v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17124v1)

**Summary:** 3D scene reconstruction and rendering are core tasks in computer vision, with applications spanning industrial monitoring, robotics, and autonomous driving. Recent advances in 3D Gaussian Splatting (GS) and its variants have achieved impressive rendering fidelity while maintaining high computational and memory efficiency. However, conventional vision-based GS pipelines typically rely on a sufficient number of camera views to initialize the Gaussian primitives and train their parameters, typicall...

---

### 43. Benchmarking the Effects of Object Pose Estimation and Reconstruction on Robotic Grasping Success

**Authors:** Varun Burde, Pavel Burget, Torsten Sattler

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17101v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17101v1)

**Summary:** 3D reconstruction serves as the foundational layer for numerous robotic perception tasks, including 6D object pose estimation and grasp pose generation. Modern 3D reconstruction methods for objects can produce visually and geometrically impressive meshes from multi-view images, yet standard geometric evaluations do not reflect how reconstruction quality influences downstream tasks such as robotic manipulation performance. This paper addresses this gap by introducing a large-scale, physics-based ...

---

### 44. ComptonUNet: A Deep Learning Model for GRB Localization with Compton Cameras under Noisy and Low-Statistic Conditions

**Authors:** Shogo Sato, Kazuo Tanaka, Shojun Ogasawara, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17085v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17085v1)

**Summary:** Gamma-ray bursts (GRBs) are among the most energetic transient phenomena in the universe and serve as powerful probes for high-energy astrophysical processes. In particular, faint GRBs originating from a distant universe may provide unique insights into the early stages of star formation. However, detecting and localizing such weak sources remains challenging owing to low photon statistics and substantial background noise. Although recent machine learning models address individual aspects of the...

---

### 45. Cross Pseudo Labeling For Weakly Supervised Video Anomaly Detection

**Authors:** Lee Dayeon, Kim Dongheyong, Park Chaewon, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17077v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17077v1)

**Summary:** Weakly supervised video anomaly detection aims to detect anomalies and identify abnormal categories with only video-level labels. We propose CPL-VAD, a dual-branch framework with cross pseudo labeling. The binary anomaly detection branch focuses on snippet-level anomaly localization, while the category classification branch leverages vision-language alignment to recognize abnormal event categories. By exchanging pseudo labels, the two branches transfer complementary strengths, combining temporal...

---

### 46. Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression

**Authors:** Akira Sakai, Yuma Ichikawa

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17063v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17063v1)

**Summary:** Sub-bit model compression seeks storage below one bit per weight; as magnitudes are aggressively compressed, the sign bit becomes a fixed-cost bottleneck. Across Transformers, CNNs, and MLPs, learned sign matrices resist low-rank approximation and are spectrally indistinguishable from an i.i.d. Rademacher baseline. Despite this apparent randomness, most weights retain their initialization signs; flips primarily occur via rare near-zero boundary crossings, suggesting that sign-pattern randomness ...

---

### 47. Cholec80-port: A Geometrically Consistent Trocar Port Segmentation Dataset for Robust Surgical Scene Understanding

**Authors:** Shunsuke Kikuchi, Atsushi Kouno, Hiroki Matsuzaki

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17060v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17060v1)

**Summary:** Trocar ports are camera-fixed, pseudo-static structures that can persistently occlude laparoscopic views and attract disproportionate feature points due to specular, textured surfaces. This makes ports particularly detrimental to geometry-based downstream pipelines such as image stitching, 3D reconstruction, and visual SLAM, where dynamic or non-anatomical outliers degrade alignment and tracking stability. Despite this practical importance, explicit port labels are rare in public surgical datase...

---

### 48. StructCore: Structure-Aware Image-Level Scoring for Training-Free Unsupervised Anomaly Detection

**Authors:** Joongwon Chae, Lihui Luo, Yang Liu, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17048v1)

**Summary:** Max pooling is the de facto standard for converting anomaly score maps into image-level decisions in memory-bank-based unsupervised anomaly detection (UAD). However, because it relies on a single extreme response, it discards most information about how anomaly evidence is distributed and structured across the image, often causing normal and anomalous scores to overlap.   We propose StructCore, a training-free, structure-aware image-level scoring method that goes beyond max pooling. Given an anom...

---

### 49. Amber-Image: Efficient Compression of Large-Scale Diffusion Transformers

**Authors:** Chaojie Yang, Tian Li, Yue Zhang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17047v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17047v1)

**Summary:** Diffusion Transformer (DiT) architectures have significantly advanced Text-to-Image (T2I) generation but suffer from prohibitive computational costs and deployment barriers. To address these challenges, we propose an efficient compression framework that transforms the 60-layer dual-stream MMDiT-based Qwen-Image into lightweight models without training from scratch. Leveraging this framework, we introduce Amber-Image, a series of streamlined T2I models. We first derive Amber-Image-10B using a tim...

---

### 50. PartRAG: Retrieval-Augmented Part-Level 3D Generation and Editing

**Authors:** Peize Li, Zeyu Zhang, Hao Tang

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17033v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17033v1)

**Summary:** Single-image 3D generation with part-level structure remains challenging: learned priors struggle to cover the long tail of part geometries and maintain multi-view consistency, and existing systems provide limited support for precise, localized edits. We present PartRAG, a retrieval-augmented framework that integrates an external part database with a diffusion transformer to couple generation with an editable representation. To overcome the first challenge, we introduce a Hierarchical Contrastiv...

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

## cs.NE

**50 papers**

### 1. Learning under noisy supervision is governed by a feedback-truth gap

**Authors:** Elan Schonfeld, Elias Wisnia

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16829v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16829v1)

**Summary:** When feedback is absorbed faster than task structure can be evaluated, the learner will favor feedback over truth. A two-timescale model shows this feedback-truth gap is inevitable whenever the two rates differ and vanishes only when they match. We test this prediction across neural networks trained with noisy labels (30 datasets, 2,700 runs), human probabilistic reversal learning (N = 292), and human reward/punishment learning with concurrent EEG (N = 25). In each system, truth is defined opera...

---

### 2. End-user validation of BRIGHT with custom-developed graphical user interface applied to cervical cancer brachytherapy

**Authors:** Leah R. M. Dickhoff, Ellen M. Kerkhof, Heloisa H. Deuzeman, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16321v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16321v1)

**Summary:** Multi-objective optimisation using BRIGHT has proven insightful and effective in prostate cancer brachytherapy treatment planning. BRachytherapy via artificially Intelligent GOMEA-Heuristic based Treatment planning (BRIGHT) generates multiple treatment plans, each with a different trade-off between tumour coverage and organs-at-risk sparing. BRIGHT was recently extended to cervical cancer brachytherapy. In this study, we present a novel, custom-developed graphical user interface (GUI) that enabl...

---

### 3. Evolutionary Context Search for Automated Skill Acquisition

**Authors:** Qi Sun, Stefan Nielsen, Rio Yokota, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16113v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16113v1)

**Summary:** Large Language Models cannot reliably acquire new knowledge post-deployment -- even when relevant text resources exist, models fail to transform them into actionable knowledge without retraining. Retrieval-Augmented Generation attempts to bridge this gap by surfacing relevant documents at inference time, yet similarity-based retrieval often fails to identify context that actually improves task performance. We introduce Evolutionary Context Search (ECS), an evolutionary method that searches conte...

---

### 4. Heuristic Search as Language-Guided Program Optimization

**Authors:** Mingxin Yu, Ruixiao Yang, Chuchu Fan

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16038v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16038v1)

**Summary:** Large Language Models (LLMs) have advanced Automated Heuristic Design (AHD) in combinatorial optimization (CO) in the past few years. However, existing discovery pipelines often require extensive manual trial-and-error or reliance on domain expertise to adapt to new or complex problems. This stems from tightly coupled internal mechanisms that limit systematic improvement of the LLM-driven design process. To address this challenge, we propose a structured framework for LLM-driven AHD that explici...

---

### 5. B-DENSE: Branching For Dense Ensemble Network Learning

**Authors:** Cherish Puniani, Tushar Kumar, Arnav Bendre, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15971v1)

**Summary:** Inspired by non-equilibrium thermodynamics, diffusion models have achieved state-of-the-art performance in generative modeling. However, their iterative sampling nature results in high inference latency. While recent distillation techniques accelerate sampling, they discard intermediate trajectory steps. This sparse supervision leads to a loss of structural information and introduces significant discretization errors. To mitigate this, we propose B-DENSE, a novel framework that leverages multi-b...

---

### 6. Evolutionary Systems Thinking -- From Equilibrium Models to Open-Ended Adaptive Dynamics

**Authors:** Dan Adler

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15957v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15957v1)

**Summary:** Complex change is often described as "evolutionary" in economics, policy, and technology, yet most system dynamics models remain constrained to fixed state spaces and equilibrium-seeking behavior. This paper argues that evolutionary dynamics should be treated as a core system-thinking problem rather than as a biological metaphor. We introduce Stability-Driven Assembly (SDA) as a minimal, non-equilibrium framework in which stochastic interactions combined with differential persistence generate en...

---

### 7. CDRL: A Reinforcement Learning Framework Inspired by Cerebellar Circuits and Dendritic Computational Strategies

**Authors:** Sibo Zhang, Rui Jing, Liangfu Lv, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15367v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15367v1)

**Summary:** Reinforcement learning (RL) has achieved notable performance in high-dimensional sequential decision-making tasks, yet remains limited by low sample efficiency, sensitivity to noise, and weak generalization under partial observability. Most existing approaches address these issues primarily through optimization strategies, while the role of architectural priors in shaping representation learning and decision dynamics is less explored. Inspired by structural principles of the cerebellum, we propo...

---

### 8. Web-Scale Multimodal Summarization using CLIP-Based Semantic Alignment

**Authors:** Mounvik K, N Harshit

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14889v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14889v1)

**Summary:** We introduce Web-Scale Multimodal Summarization, a lightweight framework for generating summaries by combining retrieved text and image data from web sources. Given a user-defined topic, the system performs parallel web, news, and image searches. Retrieved images are ranked using a fine-tuned CLIP model to measure semantic alignment with topic and text. Optional BLIP captioning enables image-only summaries for stronger multimodal coherence.The pipeline supports features such as adjustable fetch ...

---

### 9. GOT-JEPA: Generic Object Tracking with Model Adaptation and Occlusion Handling using Joint-Embedding Predictive Architecture

**Authors:** Shih-Fang Chen, Jun-Cheng Chen, I-Hong Jhuo, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14771v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14771v1)

**Summary:** The human visual system tracks objects by integrating current observations with previously observed information, adapting to target and scene changes, and reasoning about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for training targets, which limits robustness and generalization in unseen scenarios, and their occlusion reasoning remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in generalization and oc...

---

### 10. Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts

**Authors:** Buze Zhang, Jinkai Tao, Zilang Zeng, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14490v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14490v1)

**Summary:** Large Language Models (LLMs) have achieved remarkable progress, with Parameter-Efficient Fine-Tuning (PEFT) emerging as a key technique for downstream task adaptation. However, existing PEFT methods mainly operate in Euclidean space, fundamentally limiting their capacity to capture complex geometric structures inherent in language data. While alternative geometric spaces, like hyperbolic geometries for hierarchical data and spherical manifolds for circular patterns, offer theoretical advantages,...

---

### 11. Revisiting the Platonic Representation Hypothesis: An Aristotelian View

**Authors:** Fabian Gröger, Shuo Wen, Maria Brbić

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14486v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14486v1)

**Summary:** The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are confounded by network scale: increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a...

---

### 12. Selective Synchronization Attention

**Authors:** Hasi Hays

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14445v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14445v1)

**Summary:** The Transformer architecture has become the foundation of modern deep learning, yet its core self-attention mechanism suffers from quadratic computational complexity and lacks grounding in biological neural computation. We propose Selective Synchronization Attention (SSA), a novel attention mechanism that replaces the standard dot-product self-attention with a closed-form operator derived from the steady-state solution of the Kuramoto model of coupled oscillators. In SSA, each token is represent...

---

### 13. Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces

**Authors:** William L. Tong, Ege Cakar, Cengiz Pehlevan

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14404v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14404v1)

**Summary:** Recent years have witnessed meteoric progress in reasoning models: neural networks that generate intermediate reasoning traces (RTs) before producing a final output. Despite the rapid advancement, our understanding of how RTs support reasoning, and the limits of this paradigm, remain incomplete. To promote greater clarity, we introduce PITA: a novel large-scale dataset of over 23 million statements in propositional logic and their corresponding proofs. As a benchmark for robust reasoning, we foc...

---

### 14. An effective Genetic Programming Hyper-Heuristic for Uncertain Agile Satellite Scheduling

**Authors:** Yuning Chen, Junhua Xue, Wangqi Gu, et al.

**Published:** 2026-02-15

🔗 [Paper](http://arxiv.org/abs/2602.15070v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15070v1)

**Summary:** This paper investigates a novel problem, namely the Uncertain Agile Earth Observation Satellite Scheduling Problem (UAEOSSP). Unlike the static AEOSSP, it takes into account a range of uncertain factors (e.g., task profit, resource consumption, and task visibility) in order to reflect the reality that the actual information is inherently unknown beforehand. An effective Genetic Programming Hyper-Heuristic (GPHH) is designed to automate the generation of scheduling policies. The evolved schedulin...

---

### 15. Evolving Multi-Channel Confidence-Aware Activation Functions for Missing Data with Channel Propagation

**Authors:** Naeem Shahabi Sani, Ferial Najiantabriz, Shayan Shafaei, et al.

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13864v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13864v1)

**Summary:** Learning in the presence of missing data can result in biased predictions and poor generalizability, among other difficulties, which data imputation methods only partially address. In neural networks, activation functions significantly affect performance yet typical options (e.g., ReLU, Swish) operate only on feature values and do not account for missingness indicators or confidence scores. We propose Three-Channel Evolved Activations (3C-EA), which we evolve using Genetic Programming to produce...

---

### 16. A Unified Physics-Informed Neural Network for Modeling Coupled Electro- and Elastodynamic Wave Propagation Using Three-Stage Loss Optimization

**Authors:** Suhas Suresh Bharadwaj, Reuben Thomas Thovelil

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13811v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13811v1)

**Summary:** Physics-Informed Neural Networks present a novel approach in SciML that integrates physical laws in the form of partial differential equations directly into the NN through soft constraints in the loss function. This work studies the application of PINNs to solve a one dimensional coupled electro-elastodynamic system modeling linear piezoelectricity in stress-charge form, governed by elastodynamic and electrodynamic equations. Our simulation employs a feedforward architecture, mapping space-time ...

---

### 17. OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery

**Authors:** Qi Liu, Wanjing Ma

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13769v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13769v1)

**Summary:** Automating scientific discovery in complex, experiment-driven domains requires more than iterative mutation of programs; it demands structured hypothesis management, environment interaction, and principled reflection. We present OR-Agent, a configurable multi-agent research framework designed for automated exploration in rich experimental environments. OR-Agent organizes research as a structured tree-based workflow that explicitly models branching hypothesis generation and systematic backtrackin...

---

### 18. Discrete Gene Crossover Accelerates Solution Discovery in Quality-Diversity Algorithms

**Authors:** Joshua Hutchinson, J. Michael Herrmann, Simón C. Smith

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13730v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13730v1)

**Summary:** Quality-Diversity (QD) algorithms aim to discover diverse, high-performing solutions across behavioral niches. However, QD search often stagnates as incremental variation operators struggle to propagate building blocks across large populations. Existing mutation operators rely on gradual variation to solutions, limiting their ability to efficiently explore regions of the search space distant from parent solutions or to spread beneficial genetic material through the population. We propose a mutat...

---

### 19. Fast Surrogate Learning for Multi-Objective UAV Placement in Motorway Intelligent Transportation System

**Authors:** Weian Guo, Shixin Deng, Wuzhao Li, et al.

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13564v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13564v1)

**Summary:** We address multi-objective unmanned aerial vehicle (UAV) placement for motorway intelligent transportation systems, where deployments must balance coverage, link quality, and UAV count under geometric constraints. We construct a reproducible benchmark from highD motorway recordings with recording-level splits and generate Pareto-optimal labels via NSGA-II. A preference rule yields deployable targets while preserving multi-objective evaluation. We train fast surrogate models that map unordered ve...

---

### 20. Evolutionary design of thermodynamic logic gates and their heat emission

**Authors:** Stephen Whitelam

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13410v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13410v1)

**Summary:** Landauer's principle bounds the heat generated by logical operations, but in practice the thermodynamic cost of computation is dominated by the control systems that implement logic. CMOS gates dissipate energy far above the Landauer bound, while laboratory demonstrations of near-Landauer erasure rely on external measurement or feedback systems whose energy costs exceed that of the logic operation by many orders of magnitude. Here we use simulations to show that a genetic algorithm can program a ...

---

### 21. Learning to Approximate Uniform Facility Location via Graph Neural Networks

**Authors:** Chendi Qian, Christopher Morris, Stefanie Jegelka, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13155v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13155v1)

**Summary:** There has been a growing interest in using neural networks, especially message-passing neural networks (MPNNs), to solve hard combinatorial optimization problems heuristically. However, existing learning-based approaches for hard combinatorial optimization tasks often rely on supervised training data, reinforcement learning, or gradient estimators, leading to significant computational overhead, unstable training, or a lack of provable performance guarantees. In contrast, classical approximation ...

---

### 22. Which Algorithms Can Graph Neural Networks Learn?

**Authors:** Solveig Wittig, Antonis Vasileiou, Robert R. Nerem, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13106v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13106v1)

**Summary:** In recent years, there has been growing interest in understanding neural architectures' ability to learn to execute discrete algorithms, a line of work often referred to as neural algorithmic reasoning. The goal is to integrate algorithmic reasoning capabilities into larger neural pipelines. Many such architectures are based on (message-passing) graph neural networks (MPNNs), owing to their permutation equivariance and ability to deal with sparsity and variable-sized inputs. However, existing wo...

---

### 23. Synaptic Activation and Dual Liquid Dynamics for Interpretable Bio-Inspired Models

**Authors:** Mónika Farsang, Radu Grosu

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13017v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13017v1)

**Summary:** In this paper, we present a unified framework for various bio-inspired models to better understand their structural and functional differences. We show that liquid-capacitance-extended models lead to interpretable behavior even in dense, all-to-all recurrent neural network (RNN) policies. We further demonstrate that incorporating chemical synapses improves interpretability and that combining chemical synapses with synaptic activation yields the most accurate and interpretable RNN models. To asse...

---

### 24. Machine Learning-Based Classification of Jhana Advanced Concentrative Absorption Meditation (ACAM-J) using 7T fMRI

**Authors:** Puneet Kumar, Winson F. Z. Yang, Alakhsimar Singh, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13008v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13008v1)

**Summary:** Jhana advanced concentration absorption meditation (ACAM-J) is related to profound changes in consciousness and cognitive processing, making the study of their neural correlates vital for insights into consciousness and well-being. This study evaluates whether functional MRI-derived regional homogeneity (ReHo) can be used to classify ACAM-J using machine-learning approaches. We collected group-level fMRI data from 20 advanced meditators to train the classifiers, and intensive single-case data fr...

---

### 25. EPRBench: A High-Quality Benchmark Dataset for Event Stream Based Visual Place Recognition

**Authors:** Xiao Wang, Xingxing Xiong, Jinfeng Gao, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12919v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12919v1)

**Summary:** Event stream-based Visual Place Recognition (VPR) is an emerging research direction that offers a compelling solution to the instability of conventional visible-light cameras under challenging conditions such as low illumination, overexposure, and high-speed motion. Recognizing the current scarcity of dedicated datasets in this domain, we introduce EPRBench, a high-quality benchmark specifically designed for event stream-based VPR. EPRBench comprises 10K event sequences and 65K event frames, col...

---

### 26. Reverse Delegated Training and Private Inference via Perfectly-Secure Quantum Homomorphic Encryption

**Authors:** Sergio A. Ortega, Miguel A. Martin-Delgado

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12712v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12712v1)

**Summary:** Quantum machine learning in cloud environments requires protecting sensitive data while enabling remote computation. Here we demonstrate the first realistic implementations of a perfectly-secure quantum homomorphic encryption (QHE) scheme applied to quantum neural networks (QNN). Using efficient Clifford+$T$ decomposition, we implement quantum convolutional neural networks for two complementary scenarios: (i) reverse delegated training, where encrypted data from multiple providers trains a user'...

---

### 27. Energy-Aware Spike Budgeting for Continual Learning in Spiking Neural Networks for Neuromorphic Vision

**Authors:** Anika Tabassum Meem, Muntasir Hossain Nadid, Md Zesun Ahmed Mia

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.12236v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12236v1)

**Summary:** Neuromorphic vision systems based on spiking neural networks (SNNs) offer ultra-low-power perception for event-based and frame-based cameras, yet catastrophic forgetting remains a critical barrier to deployment in continually evolving environments. Existing continual learning methods, developed primarily for artificial neural networks, seldom jointly optimize accuracy and energy efficiency, with particularly limited exploration on event-based datasets. We propose an energy-aware spike budgeting ...

---

### 28. CL API: Real-Time Closed-Loop Interactions with Biological Neural Networks

**Authors:** David Hogan, Andrew Doherty, Boon Kien Khoo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11632v1)

**Summary:** Biological neural networks (BNNs) are increasingly explored for their rich dynamics, parallelism, and adaptive behavior. Beyond understanding their function as a scientific endeavour, a key focus has been using these biological systems as a novel computing substrate. However, BNNs can only function as reliable information-processing systems if inputs are delivered in a temporally and structurally consistent manner. In practice, this requires stimulation with precisely controlled structure, micro...

---

### 29. Evolution With Purpose: Hierarchy-Informed Optimization of Whole-Brain Models

**Authors:** Hormoz Shahrzad, Niharika Gajawelli, Kaitlin Maile, et al.

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11398v2) | 📄 [PDF](https://arxiv.org/pdf/2602.11398v2)

**Summary:** Evolutionary search is well suited for large-scale biophysical brain modeling, where many parameters with nonlinear interactions and no tractable gradients need to be optimized. Standard evolutionary approaches achieve an excellent fit to MRI data; however, among many possible such solutions, it finds ones that overfit to individual subjects and provide limited predictive power. This paper investigates whether guiding evolution with biological knowledge can help. Focusing on whole-brain Dynamic ...

---

### 30. Predictive Associative Memory: Retrieval Beyond Similarity Through Temporal Co-occurrence

**Authors:** Jason Dury

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11322v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11322v1)

**Summary:** Current approaches to memory in neural systems rely on similarity-based retrieval: given a query, find the most representationally similar stored state. This assumption -- that useful memories are similar memories -- fails to capture a fundamental property of biological memory: association through temporal co-occurrence. We propose Predictive Associative Memory (PAM), an architecture in which a JEPA-style predictor, trained on temporal co-occurrence within a continuous experience stream, learns ...

---

### 31. Interactive LLM-assisted Curriculum Learning for Multi-Task Evolutionary Policy Search

**Authors:** Berfin Sakallioglu, Giorgia Nadizar, Eric Medvet

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.10891v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10891v1)

**Summary:** Multi-task policy search is a challenging problem because policies are required to generalize beyond training cases. Curriculum learning has proven to be effective in this setting, as it introduces complexity progressively. However, designing effective curricula is labor-intensive and requires extensive domain expertise. LLM-based curriculum generation has only recently emerged as a potential solution, but was limited to operate in static, offline modes without leveraging real-time feedback from...

---

### 32. Amortized Inference of Neuron Parameters on Analog Neuromorphic Hardware

**Authors:** Jakob Kaiser, Eric Müller, Johannes Schemmel

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.10763v2) | 📄 [PDF](https://arxiv.org/pdf/2602.10763v2)

**Summary:** Our work utilized a non-sequential simulation-based inference algorithm to provide an amortized neural density estimator, which approximates the posterior distribution for seven parameters of the adaptive exponential integrate-and-fire neuron model of the analog neuromorphic BrainScaleS-2 substrate. We constrained the large parameter space by training a binary classifier to predict parameter combinations yielding observations in regimes of interest, i.e. moderate spike counts. We compared two ne...

---

### 33. MindPilot: Closed-loop Visual Stimulation Optimization for Brain Modulation with EEG-guided Diffusion

**Authors:** Dongyang Li, Kunpeng Xie, Mingyang Wu, et al.

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.10552v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10552v1)

**Summary:** Whereas most brain-computer interface research has focused on decoding neural signals into behavior or intent, the reverse challenge-using controlled stimuli to steer brain activity-remains far less understood, particularly in the visual domain. However, designing images that consistently elicit desired neural responses is difficult: subjective states lack clear quantitative measures, and EEG feedback is both noisy and non-differentiable. We introduce MindPilot, the first closed-loop framework t...

---

### 34. ImprovEvolve: Ask AlphaEvolve to Improve the Input Solution and Then Improvise

**Authors:** Alexey Kravatskiy, Valentin Khrulkov, Ivan Oseledets

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10233v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10233v1)

**Summary:** Recent advances in LLM-guided evolutionary computation, particularly AlphaEvolve, have demonstrated remarkable success in discovering novel mathematical constructions and solving challenging optimization problems. In this article, we present ImprovEvolve, a simple yet effective technique for enhancing LLM-based evolutionary approaches such as AlphaEvolve. Given an optimization problem, the standard approach is to evolve program code that, when executed, produces a solution close to the optimum. ...

---

### 35. Sparse Axonal and Dendritic Delays Enable Competitive SNNs for Keyword Classification

**Authors:** Younes Bouhadjar, Emre Neftci

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09746v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09746v1)

**Summary:** Training transmission delays in spiking neural networks (SNNs) has been shown to substantially improve their performance on complex temporal tasks. In this work, we show that learning either axonal or dendritic delays enables deep feedforward SNNs composed of leaky integrate-and-fire (LIF) neurons to reach accuracy comparable to existing synaptic delay learning approaches, while significantly reducing memory and computational overhead. SNN models with either axonal or dendritic delays achieve up...

---

### 36. From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet

**Authors:** Radib Bin Kabir, Tawsif Tashwar Dipto, Mehedi Ahamed, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09717v1)

**Summary:** Spiking Neural Networks (SNNs) are increasingly studied as energy-efficient alternatives to Convolutional Neural Networks (CNNs), particularly for edge intelligence. However, prior work has largely emphasized large-scale models, leaving the design and evaluation of lightweight CNN-to-SNN pipelines underexplored. In this paper, we present the first systematic benchmark of lightweight SNNs obtained by converting compact CNN architectures into spiking networks, where activations are modeled with Le...

---

### 37. Provably robust learning of regression neural networks using $β$-divergences

**Authors:** Abhik Ghosh, Suryasis Jana

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08933v1)

**Summary:** Regression neural networks (NNs) are most commonly trained by minimizing the mean squared prediction error, which is highly sensitive to outliers and data contamination. Existing robust training methods for regression NNs are often limited in scope and rely primarily on empirical validation, with only a few offering partial theoretical guarantees. In this paper, we propose a new robust learning framework for regression NNs based on the $β$-divergence (also known as the density power divergence) ...

---

### 38. A Methodology for Effective Surrogate Learning in Complex Optimization

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08825v1)

**Summary:** Solving complex problems requires continuous effort in developing theory and practice to cope with larger, more difficult scenarios. Working with surrogates is normal for creating a proxy that realistically models the problem into the computer. Thus, the question of how to best define and characterize such a surrogate model is of the utmost importance. In this paper, we introduce the PTME methodology to study deep learning surrogates by analyzing their Precision, Time, Memory, and Energy consump...

---

### 39. Enhancing Genetic Algorithms with Graph Neural Networks: A Timetabling Case Study

**Authors:** Laura-Maria Cornei, Mihaela-Elena Breabăn

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08619v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08619v1)

**Summary:** This paper investigates the impact of hybridizing a multi-modal Genetic Algorithm with a Graph Neural Network for timetabling optimization. The Graph Neural Network is designed to encapsulate general domain knowledge to improve schedule quality, while the Genetic Algorithm explores different regions of the search space and integrates the deep learning model as an enhancement operator to guide the solution search towards optimality. Initially, both components of the hybrid technique were designed...

---

### 40. Do physics-informed neural networks (PINNs) need to be deep? Shallow PINNs using the Levenberg-Marquardt algorithm

**Authors:** Muhammad Luthfi Shahab, Imam Mukhlash, Hadi Susanto

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08515v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08515v2)

**Summary:** This work investigates the use of shallow physics-informed neural networks (PINNs) for solving forward and inverse problems of nonlinear partial differential equations (PDEs). By reformulating PINNs as nonlinear systems, the Levenberg-Marquardt (LM) algorithm is employed to efficiently optimize the network parameters. Analytical expressions for the neural network derivatives with respect to the input variables are derived, enabling accurate and efficient computation of the Jacobian matrix requir...

---

### 41. A Multi-objective Evolutionary Algorithm Based on Bi-population with Uniform Sampling for Neural Architecture Search

**Authors:** Yu Xue, Pengcheng Jiang, Chenchen Zhu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08513v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08513v1)

**Summary:** Neural architecture search (NAS) automates neural network design, improving efficiency over manual approaches. However, efficiently discovering high-performance neural network architectures that simultaneously optimize multiple objectives remains a significant challenge in NAS. Existing methods often suffer from limited population diversity and inadequate exploration of the search space, particularly in regions with extreme complexity values. To address these challenges, we propose MOEA-BUS, an ...

---

### 42. Approximating Matrix Functions with Deep Neural Networks and Transformers

**Authors:** Rahul Padmanabhan, Simone Brugiapaglia

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.07800v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07800v1)

**Summary:** Transformers have revolutionized natural language processing, but their use for numerical computation has received less attention. We study the approximation of matrix functions, which map scalar functions to matrices, using neural networks including transformers. We focus on functions mapping square matrices to square matrices of the same dimension. These types of matrix functions appear throughout scientific computing, e.g., the matrix exponential in continuous-time Markov chains and the matri...

---

### 43. Generative structural elucidation from mass spectra as an iterative optimization problem

**Authors:** Mrunali Manjrekar, Runzhong Wang, Samuel Goldman, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07709v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07709v1)

**Summary:** Liquid chromatography tandem mass spectrometry (LC-MS/MS) is a critical analytical technique for molecular identification across metabolomics, environmental chemistry, and chemical forensics. A variety of computational methods have emerged for structural annotation of spectral features of interest, but many of these features cannot be confidently annotated with reference structures or spectra. Here, we introduce FOAM (Formula-constrained Optimization for Annotating Metabolites), a computational ...

---

### 44. On the Infinite Width and Depth Limits of Predictive Coding Networks

**Authors:** Francesco Innocenti, El Mehdi Achour, Rafal Bogacz

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07697v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07697v1)

**Summary:** Predictive coding (PC) is a biologically plausible alternative to standard backpropagation (BP) that minimises an energy function with respect to network activities before updating weights. Recent work has improved the training stability of deep PC networks (PCNs) by leveraging some BP-inspired reparameterisations. However, the full scalability and theoretical basis of these approaches remains unclear. To address this, we study the infinite width and depth limits of PCNs. For linear residual net...

---

### 45. Optimizing Chlorination in Water Distribution Systems via Surrogate-assisted Neuroevolution

**Authors:** Rivaaj Monsia, Daniel Young, Olivier Francon, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07299v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07299v1)

**Summary:** Ensuring the microbiological safety of large, heterogeneous water distribution systems (WDS) typically requires managing appropriate levels of disinfectant residuals including chlorine. WDS include complex fluid interactions that are nonlinear and noisy, making such maintenance a challenging problem for traditional control algorithms. This paper proposes an evolutionary framework to this problem based on neuroevolution, multi-objective optimization, and surrogate modeling. Neural networks were e...

---

### 46. Evolving LLM-Derived Control Policies for Residential EV Charging and Vehicle-to-Grid Energy Optimization

**Authors:** Vishesh Purnananda, Benjamin John Wruck, Mingyu Guo

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07275v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07275v1)

**Summary:** This research presents a novel application of Evolutionary Computation to the domain of residential electric vehicle (EV) energy management. While reinforcement learning (RL) achieves high performance in vehicle-to-grid (V2G) optimization, it typically produces opaque "black-box" neural networks that are difficult for consumers and regulators to audit. Addressing this interpretability gap, we propose a program search framework that leverages Large Language Models (LLMs) as intelligent mutation o...

---

### 47. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 48. Sparse Spike Encoding of Channel Responses for Energy Efficient Human Activity Recognition

**Authors:** Eleonora Cicciarella, Riccardo Mazzieri, Jacopo Pegoraro, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06766v1)

**Summary:** ISAC enables pervasive monitoring, but modern sensing algorithms are often too complex for energy-constrained edge devices. This motivates the development of learning techniques that balance accuracy performance and energy efficiency. Spiking Neural Networks (SNNs) are a promising alternative, processing information as sparse binary spike trains and potentially reducing energy consumption by orders of magnitude. In this work, we propose a spiking convolutional autoencoder (SCAE) that learns tail...

---

### 49. Structural bias in multi-objective optimisation

**Authors:** Jakub Kudela, Niki van Stein, Thomas Bäck, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06742v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06742v1)

**Summary:** Structural bias (SB) refers to systematic preferences of an optimisation algorithm for particular regions of the search space that arise independently of the objective function. While SB has been studied extensively in single-objective optimisation, its role in multi-objective optimisation remains largely unexplored. This is problematic, as dominance relations, diversity preservation and Pareto-based selection mechanisms may introduce or amplify structural effects.   In this paper, we extend the...

---

### 50. Green Optimization: Energy-aware Design of Metaheuristics by Using Machine Learning Surrogates to Cope with Real Problems

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06610v2) | 📄 [PDF](https://arxiv.org/pdf/2602.06610v2)

**Summary:** Addressing real-world optimization challenges requires not only advanced metaheuristics but also continuous refinement of their internal mechanisms. This paper explores the integration of machine learning in the form of neural surrogate models into metaheuristics through a recent lens: energy consumption. While surrogates are widely used to reduce the computational cost of expensive objective functions, their combined impact on energy efficiency, algorithmic performance, and solution accuracy re...

---

## q-bio.NC

**50 papers**

### 1. Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis

**Authors:** Minheng Chen, Jing Zhang, Tong Chen, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17557v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17557v1)

**Summary:** Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, viol...

---

### 2. Construction of a classification model for dementia among Brazilian adults aged 50 and over

**Authors:** F. S. Menezes, M. C. F. G. Barretto, E. Q. C. Garcia, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16887v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16887v1)

**Summary:** To build a dementia classification model for middle-aged and elderly Brazilians, implemented in Python, combining variable selection and multivariable analysis, using low-cost variables with modification potential. Observational study with a predictive modeling approach using a cross-sectional design, aimed at estimating the chances of developing dementia, using data from the Brazilian Longitudinal Study of Aging (ELSI-Brazil), involving 9,412 participants. Dementia was determined based on neuro...

---

### 3. A Systematic Evaluation of Sample-Level Tokenization Strategies for MEG Foundation Models

**Authors:** SungJun Cho, Chetan Gohil, Rukuang Huang, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16626v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16626v1)

**Summary:** Recent success in natural language processing has motivated growing interest in large-scale foundation models for neuroimaging data. Such models often require discretization of continuous neural time series data, a process referred to as 'tokenization'. However, the impact of different tokenization strategies for neural data is currently poorly understood. In this work, we present a systematic evaluation of sample-level tokenization strategies for transformer-based large neuroimaging models (LNM...

---

### 4. The Representational Alignment Hypothesis: Evidence for and Consequences of Invariant Semantic Structure Across Embedding Modalities

**Authors:** Akhil Ramidi, Kevin Scharp

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16584v1)

**Summary:** There is growing evidence that independently trained AI systems come to represent the world in the same way. In other words, independently trained embeddings from text, vision, audio, and neural signals share an underlying geometry. We call this the Representational Alignment Hypothesis (RAH) and investigate evidence for and consequences of this claim. The evidence is of two kinds: (i) internal structure comparison techniques, such as representational similarity analysis and topological data ana...

---

### 5. Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research

**Authors:** Chenda Duan, Yipeng Zhang, Sotaro Kanai, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16072v2) | 📄 [PDF](https://arxiv.org/pdf/2602.16072v2)

**Summary:** Epilepsy affects over 50 million people worldwide, and one-third of patients suffer drug-resistant seizures where surgery offers the best chance of seizure freedom. Accurate localization of the epileptogenic zone (EZ) relies on intracranial EEG (iEEG). Clinical workflows, however, remain constrained by labor-intensive manual review. At the same time, existing data-driven approaches are typically developed on single-center datasets that are inconsistent in format and metadata, lack standardized b...

---

### 6. Time-Varying Directed Interactions in Functional Brain Networks: Modeling and Validation

**Authors:** Nan Xu, Xiaodi Zhang, Wen-Ju Pan, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16004v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16004v1)

**Summary:** Understanding the dynamic nature of brain connectivity is critical for elucidating neural processing, behavior, and brain disorders. Traditional approaches such as sliding-window correlation (SWC) characterize time-varying undirected associations but do not resolve directional interactions, limiting inference about time-resolved information flow in brain networks. We introduce sliding-window prediction correlation (SWpC), which embeds a directional linear time-invariant (LTI) model within each s...

---

### 7. Energy budgets govern synaptic precision and its regulation during plasticity

**Authors:** James Malkin, Cian O'Donnell, Conor Houghton

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15787v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15787v1)

**Summary:** Synaptic transmission must balance the need for reliable signalling against the metabolic cost of achieving that reliability. How energetic constraints shape synaptic precision and its regulation during plasticity remains unclear. Here we develop an energy--constrained framework in which synapses minimise postsynaptic response variance subject to a fixed mean and an effective energy budget. Combinations of candidate physiological costs are used to estimate an energy cost for synaptic transmissio...

---

### 8. A golden-ratio partition of information and the balance between prediction and surprise: a neuro-cognitive route to antifragility

**Authors:** Pablo Padilla, Oliver López-Corona, Elvia Ramírez-Carrillo, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.15266v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15266v1)

**Summary:** Adaptive systems must strike a balance between prediction and surprise to thrive in uncertain environments. We propose an information-theoretic balance function, $ f(p) = -(1 - p)\ln(1 - p) + \ln p $, which quantifies the net informational gain from contrasting explained variance $p$ with unexplained novelty $(1 - p)$. This function is strictly concave on $(0,1)$ and reaches its unique maximum at $ p^* \approx 0.882$, revealing a regime where confidence is high but the residual uncertainty carri...

---

### 9. Drift-Diffusion Matching: Embedding dynamics in latent manifolds of asymmetric neural networks

**Authors:** Ramón Nartallo-Kaluarachchi, Renaud Lambiotte, Alain Goriely

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14885v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14885v1)

**Summary:** Recurrent neural networks (RNNs) provide a theoretical framework for understanding computation in biological neural circuits, yet classical results, such as Hopfield's model of associative memory, rely on symmetric connectivity that restricts network dynamics to gradient-like flows. In contrast, biological networks support rich time-dependent behaviour facilitated by their asymmetry. Here we introduce a general framework, which we term drift-diffusion matching, for training continuous-time RNNs ...

---

### 10. Evolutionarily Primitive Social Entities

**Authors:** Angelica Kaufmann

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14843v1)

**Summary:** Social entities only exist in virtue of collective acceptance or recognition, or acknowledgement by two or more individuals in the context of joint activities. Joint activities are made possible by the coordination of plans for action, and the coordination of plans for action is made possible by the capacity for collective intentionality. This paper investigates how primitive is the capacity that nonhuman animals have to create social entities, by individuating how primitive is the capacity for ...

---

### 11. Human-Aligned Evaluation of a Pixel-wise DNN Color Constancy Model

**Authors:** Hamed Heidari-Gorji, Raquel Gil Rodriguez, Karl R. Gegenfurtner

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13887v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13887v1)

**Summary:** We previously investigated color constancy in photorealistic virtual reality (VR) and developed a Deep Neural Network (DNN) that predicts reflectance from rendered images. Here, we combine both approaches to compare and study a model and human performance with respect to established color constancy mechanisms: local surround, maximum flux and spatial mean. Rather than evaluating the model against physical ground truth, model performance was assessed using the same achromatic object selection tas...

---

### 12. Metabolic cost of information processing in Poisson variational autoencoders

**Authors:** Hadi Vafaii, Jacob L. Yates

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13421v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13421v1)

**Summary:** Computation in biological systems is fundamentally energy-constrained, yet standard theories of computation treat energy as freely available. Here, we argue that variational free energy minimization under a Poisson assumption offers a principled path toward an energy-aware theory of computation. Our key observation is that the Kullback-Leibler (KL) divergence term in the Poisson free energy objective becomes proportional to the prior firing rates of model neurons, yielding an emergent metabolic ...

---

### 13. The Influence of Width Ratios on Structural Beauty in Male Faces

**Authors:** Benjamin Knopp, Theresa Tennstedt, Dominik Endres

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13368v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13368v1)

**Summary:** This study investigates the relationship between interocular distance relative to overall facial width (width ratio) and perceived subjective beauty in male faces. Building on the methodology of Pallett et al. (2010), who found that average proportions in female faces were rated as most attractive, the current study aimed to test this hypothesis in male faces. Faces from the Chicago Face Database (Ma et al., 2015) were morphed into average faces within three groups (with low, medium, and high wi...

---

### 14. Left-right asymmetry in predicting brain activity from LLMs' representations emerges with their formal linguistic competence

**Authors:** Laurent Bonnasse-Gahot, Christophe Pallier

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12811v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12811v1)

**Summary:** When humans and large language models (LLMs) process the same text, activations in the LLMs correlate with brain activity measured, e.g., with functional magnetic resonance imaging (fMRI). Moreover, it has been shown that, as the training of an LLM progresses, the performance in predicting brain activity from its internal activations improves more in the left hemisphere than in the right one. The aim of the present work is to understand which kind of competence acquired by the LLMs underlies the...

---

### 15. A consequence of failed sequential learning: A computational account of developmental amnesia

**Authors:** Qi Zhang

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12547v1)

**Summary:** Developmental amnesia, featured with severely impaired episodic memory and almost normal semantic memory, has been discovered to occur in children with hippocampal atrophy. This unique combination of characteristics seems to challenge the understanding that early loss of episodic memory may impede cognitive development and result in severe mental retardation. Although a few underlying mechanisms have been suggested, no computational model has been reported that is able to mimic the unique combin...

---

### 16. Conference Proceedings of the Inaugural Conference of the International Society for Tractography (IST 2025 Bordeaux)

**Authors:** Flavio Dell Acqua, Maxime Descoteaux, Graham Little, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.12410v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12410v1)

**Summary:** This collection comprises the abstracts presented during poster, power pitch and oral sessions at the Inaugural Conference of the International Society for Tractography (IST Conference 2025), held in Bordeaux, France, from October 13-16, 2025. The conference was designed to foster meaningful exchange and collaboration between disparate fields. The overall focus was on advancing research, innovation, and community in the common fields of interest: neuroanatomy, tractography methods and scientific...

---

### 17. TAVAE: A VAE with Adaptable Priors Explains Contextual Modulation in the Visual Cortex

**Authors:** Balázs Meszéna, Keith T. Murray, Julien Corbo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11956v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11956v1)

**Summary:** The brain interprets visual information through learned regularities, a computation formalized as probabilistic inference under a prior. The visual cortex establishes priors for this inference, some delivered through established top-down connections that inform low-level cortices about statistics represented at higher levels in the cortical hierarchy. While evidence shows that adaptation leads to priors reflecting the structure of natural images, it remains unclear whether similar priors can be ...

---

### 18. CL API: Real-Time Closed-Loop Interactions with Biological Neural Networks

**Authors:** David Hogan, Andrew Doherty, Boon Kien Khoo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11632v1)

**Summary:** Biological neural networks (BNNs) are increasingly explored for their rich dynamics, parallelism, and adaptive behavior. Beyond understanding their function as a scientific endeavour, a key focus has been using these biological systems as a novel computing substrate. However, BNNs can only function as reliable information-processing systems if inputs are delivered in a temporally and structurally consistent manner. In practice, this requires stimulation with precisely controlled structure, micro...

---

### 19. Defining causal mechanism in dual process theory and two types of feedback control

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11478v1)

**Summary:** Mental events are considered to supervene on physical events. A supervenient event does not change without a corresponding change in the underlying subvenient physical events. Since wholes and their parts exhibit the same supervenience-subvenience relations, inter-level causation has been expected to serve as a model for mental causation. We proposed an inter-level causation mechanism to construct a model of consciousness and an agent's self-determination. However, a significant gap exists betwe...

---

### 20. A Dynamical Microscope for Multivariate Oscillatory Signals: Validating Regime Recovery on Shared Manifolds

**Authors:** Łukasz Furman, Ludovico Minati, Włodzisław Duch

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11054v1)

**Summary:** Multivariate oscillatory signals from complex systems often exhibit non-stationary dynamics and metastable regime structure, making dynamical interpretation challenging. We introduce a ``dynamical microscope'' framework that converts multichannel signals into circular phase--amplitude features, learns a data-driven latent trajectory representation with an autoencoder, and quantifies dynamical regimes through trajectory geometry and flow field metrics. Using a coupled Stuart--Landau oscillator ne...

---

### 21. Learning Glioblastoma Tumor Heterogeneity Using Brain Inspired Topological Neural Networks

**Authors:** Ankita Paul, Wenyi Wang

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11234v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11234v1)

**Summary:** Accurate prognosis for Glioblastoma (GBM) using deep learning (DL) is hindered by extreme spatial and structural heterogeneity. Moreover, inconsistent MRI acquisition protocols across institutions hinder generalizability of models. Conventional transformer and DL pipelines often fail to capture the multi-scale morphological diversity such as fragmented necrotic cores, infiltrating margins, and disjoint enhancing components leading to scanner-specific artifacts and poor cross-site prognosis. We p...

---

### 22. Graph neural networks uncover structure and functions underlying the activity of simulated neural assemblies

**Authors:** Cédric Allier, Larissa Heinrich, Magdalena Schneider, et al.

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.13325v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13325v1)

**Summary:** Graph neural networks trained to predict observable dynamics can be used to decompose the temporal activity of complex heterogeneous systems into simple, interpretable representations. Here we apply this framework to simulated neural assemblies with thousands of neurons and demonstrate that it can jointly reveal the connectivity matrix, the neuron types, the signaling functions, and in some cases hidden external stimuli. In contrast to existing machine learning approaches such as recurrent neura...

---

### 23. ENIGMA: EEG-to-Image in 15 Minutes Using Less Than 1% of the Parameters

**Authors:** Reese Kneeland, Wangshu Jiang, Ugo Bruzadin Nunes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10361v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10361v1)

**Summary:** To be practical for real-life applications, models for brain-computer interfaces must be easily and quickly deployable on new subjects, effective on affordable scanning hardware, and small enough to run locally on accessible computing resources. To directly address these current limitations, we introduce ENIGMA, a multi-subject electroencephalography (EEG)-to-Image decoding model that reconstructs seen images from EEG recordings and achieves state-of-the-art (SOTA) performance on the research-gr...

---

### 24. UltraLIF: Fully Differentiable Spiking Neural Networks via Ultradiscretization and Max-Plus Algebra

**Authors:** Jose Marie Antonio Miñoza

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.11206v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11206v1)

**Summary:** Spiking Neural Networks (SNNs) offer energy-efficient, biologically plausible computation but suffer from non-differentiable spike generation, necessitating reliance on heuristic surrogate gradients. This paper introduces UltraLIF, a principled framework that replaces surrogate gradients with ultradiscretization, a mathematical formalism from tropical geometry providing continuous relaxations of discrete dynamics. The central insight is that the max-plus semiring underlying ultradiscretization n...

---

### 25. Popularity Feedback Constrains Innovation in Cultural Markets

**Authors:** Lucas Gautheron, Raja Marjieh, Dalton C. Conley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09997v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09997v1)

**Summary:** Real-world creative processes ranging from art to science rely on social feedback-loops between selection and creation. Yet, the effects of popularity feedback on collective creativity remain poorly understood. We investigate how popularity ratings influence cultural dynamics in a large-scale online experiment where participants ($N = 1\,008$) iteratively \textit{select} images from evolving markets and \textit{produce} their own modifications. Results show that exposing the popularity of images...

---

### 26. Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release

**Authors:** Peter N. Taylor, Gerard Hall, Jonathan Horsley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09852v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09852v1)

**Summary:** Epileptic seizures are generated in cerebral networks that propagate ictal and interictal activity. The structure of cerebral networks underpinning epileptic activity can be inferred from diffusion-weighted MRI (DWI). However, publicly available DWI data in individuals with epilepsy are scarce, and processing is technically challenging due to scan-specific artifacts, limiting research progress. Here, we release raw DWI data from 216 individuals with epilepsy and 98 healthy controls. Subject iden...

---

### 27. Finite integration time can shift optimal sensitivity away from criticality

**Authors:** Sahel Azizpour, Viola Priesemann, Johannes Zierenberg, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09491v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09491v1)

**Summary:** Sensitivity to small changes in the environment is crucial for many real-world tasks, enabling living and artificial systems to make correct behavioral decisions. It has been shown that such sensitivity is maximized when a system operates near the critical point of a phase transition. However, proximity to criticality introduces large fluctuations and diverging timescales. Hence, to leverage the maximal sensitivity, it would require impractically long integration periods. Here, we analytically a...

---

### 28. Structural coarse-graining enables noise-robust functional connectivity and reveals hidden inter-subject variability

**Authors:** Izaro Fernandez-Iriondo, Antonio Jimenez-Marin, Jesus Cortes, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08910v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08910v1)

**Summary:** Functional connectivity estimates are highly sensitive to analysis choices and can be dominated by noise when the number of sampled time points is small relative to network dimensionality. This issue is particularly acute in fMRI, where scan resolution is limited. Because scan duration is constrained by practical factors (e.g., motion and fatigue), many datasets remain statistically underpowered for high-dimensional correlation estimation. We introduce a framework that combines diffusion-based s...

---

### 29. Universal Approximation Theorems for Dynamical Systems with Infinite-Time Horizon Guarantees

**Authors:** Abel Sagodi, Il Memming Park

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08640v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08640v2)

**Summary:** Universal approximation theorems establish the expressive capacity of neural network architectures. For dynamical systems, existing results are limited to finite time horizons or systems with a globally stable equilibrium, leaving multistability and limit cycles unaddressed. We prove that Neural ODEs achieve $\varepsilon$-$δ$ closeness -- trajectories within error $\varepsilon$ except for initial conditions of measure $< δ$ -- over the \emph{infinite} time horizon $[0,\infty)$ for three target c...

---

### 30. Linguistics and Human Brain: A Perspective of Computational Neuroscience

**Authors:** Fudong Zhang, Bo Chai, Yujie Wu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08275v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08275v2)

**Summary:** Elucidating the language-brain relationship requires bridging the methodological gap between the abstract theoretical frameworks of linguistics and the empirical neural data of neuroscience. Serving as an interdisciplinary cornerstone, computational neuroscience formalizes the hierarchical and dynamic structures of language into testable neural models through modeling, simulation, and data analysis. This enables a computational dialogue between linguistic hypotheses and neural mechanisms. Recent...

---

### 31. Bootstrapping Life-Inspired Machine Intelligence: The Biological Route from Chemistry to Cognition and Creativity

**Authors:** Giovanni Pezzulo, Michael Levin

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.08079v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08079v1)

**Summary:** Achieving advanced machine intelligence remains a central challenge in AI research, often approached through scaling neural architectures and generative models. However, biological systems offer a broader repertoire of strategies for adaptive, goal-directed behavior - strategies that emerged long before nervous systems evolved. This paper advocates a genuinely life-inspired approach to machine intelligence, drawing on principles from biology that enable robustness, autonomy, and open-ended probl...

---

### 32. Beyond Expertise: Stable Individual Differences in Predictive Eye-Hand Coordination

**Authors:** Emiko Shishido

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.07816v2) | 📄 [PDF](https://arxiv.org/pdf/2602.07816v2)

**Summary:** Human eye-hand coordination relies on internal forward models that predict future states and compensate for sensory delays. During line tracing, the gaze typically leads the hand through predictive saccades, yet the extent to which this predictive window reflects expertise or intrinsic individual traits remains unclear. In this study, I examined eye-hand coordination in professional calligraphers and non-experts performing a controlled line tracing task. The temporal coupling between saccade dis...

---

### 33. How does longer temporal context enhance multimodal narrative video processing in the brain?

**Authors:** Prachi Jindal, Anant Khandelwal, Manish Gupta, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07570v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07570v1)

**Summary:** Understanding how humans and artificial intelligence systems process complex narrative videos is a fundamental challenge at the intersection of neuroscience and machine learning. This study investigates how the temporal context length of video clips (3--12 s clips) and the narrative-task prompting shape brain-model alignment during naturalistic movie watching. Using fMRI recordings from participants viewing full-length movies, we examine how brain regions sensitive to narrative context dynamical...

---

### 34. Linguistic properties and model scale in brain encoding: from small to compressed language models

**Authors:** Subba Reddy Oota, Vijay Rowtula, Satya Sai Srinath Namburi, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07547v1)

**Summary:** Recent work has shown that scaling large language models (LLMs) improves their alignment with human brain activity, yet it remains unclear what drives these gains and which representational properties are responsible. Although larger models often yield better task performance and brain alignment, they are increasingly difficult to analyze mechanistically. This raises a fundamental question: what is the minimal model capacity required to capture brain-relevant representations? To address this que...

---

### 35. Training-Driven Representational Geometry Modularization Predicts Brain Alignment in Language Models

**Authors:** Yixuan Liu, Zhiyuan Ma, Likai Tang, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07539v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07539v1)

**Summary:** How large language models (LLMs) align with the neural representation and computation of human language is a central question in cognitive science. Using representational geometry as a mechanistic lens, we addressed this by tracking entropy, curvature, and fMRI encoding scores throughout Pythia (70M-1B) training. We identified a geometric modularization where layers self-organize into stable low- and high-complexity clusters. The low-complexity module, characterized by reduced entropy and curvat...

---

### 36. Cognitive algorithms and systems of episodic memory, semantic memory and their learnings

**Authors:** Qi Zhang

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07261v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07261v1)

**Summary:** Declarative memory, the memory that can be "declared" in words or languages, is made up of two dissociated parts: episodic memory and semantic memory. This dissociation has its neuroanatomical basis episodic memory is mostly associated with the hippocampus and semantic memory with the neocortex. The two memories, on the other hand, are closely related. Lesions in the hippocampus often result in various impairments of explicit memory, e.g., anterograde, retrograde and developmental amnesias, and ...

---

### 37. Extracting Root-Causal Brain Activity Driving Psychopathology from Resting State fMRI

**Authors:** Eric V. Strobl

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07233v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07233v1)

**Summary:** Neuroimaging studies of psychiatric disorders often correlate imaging patterns with diagnostic labels or composite symptom scores, yielding diffuse associations that obscure underlying mechanisms. We instead seek to identify root-causal maps -- localized BOLD disturbances that initiate pathological cascades -- and to link them selectively to symptom dimensions. We introduce a bilevel structural causal model that connects between-subject symptom structure to within-subject resting-state fMRI via ...

---

### 38. Behavior Score Prediction in Resting-State Functional MRI by Deep State Space Modeling

**Authors:** Javier Salazar Cavazos, Maximillian Egan, Krisanne Litinas, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07131v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07131v1)

**Summary:** Early clinical assessment of Alzheimer's disease relies on behavior scores that measure a subject's language, memory, and cognitive skills. On the medical imaging side, functional magnetic resonance imaging has provided invaluable insights into the neural pathways underlying Alzheimer's disease. While prior studies have used resting-state functional MRI by extracting functional connectivity matrices, these approaches neglect the temporal dynamics inherent in functional data. In this work, we pre...

---

### 39. Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space

**Authors:** Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05971v1)

**Summary:** Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to ...

---

### 40. BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction

**Authors:** Xuanhua Yin, Runkai Zhao, Lina Yao, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04512v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04512v1)

**Summary:** Naturalistic fMRI characterizes the brain as a dynamic predictive engine driven by continuous sensory streams. However, modeling the causal forward evolution in realistic neural simulation is impeded by the timescale mismatch between multimodal inputs and the complex topology of cortical networks. To address these challenges, we introduce BrainVista, a multimodal autoregressive framework designed to model the causal evolution of brain states. BrainVista incorporates Network-wise Tokenizers to di...

---

### 41. Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish

**Authors:** Jan-Matthis Lueckmann, Viren Jain, Michał Januszewski

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04492v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04492v1)

**Summary:** Constructing mechanistic models of neural circuits is a fundamental goal of neuroscience, yet verifying such models is limited by the lack of ground truth. To rigorously test model discovery, we establish an in silico testbed using neuromechanical simulations of a larval zebrafish as a transparent ground truth. We find that LLM-based tree search autonomously discovers predictive models that significantly outperform established forecasting baselines. Conditioning on sensory drive is necessary but...

---

### 42. Multi-Integration of Labels across Categories for Component Identification (MILCCI)

**Authors:** Noga Mudrik, Yuxi Chen, Gal Mishne, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04270v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04270v1)

**Summary:** Many fields collect large-scale temporal data through repeated measurements (trials), where each trial is labeled with a set of metadata variables spanning several categories. For example, a trial in a neuroscience study may be linked to a value from category (a): task difficulty, and category (b): animal choice. A critical challenge in time-series analysis is to understand how these labels are encoded within the multi-trial observations, and disentangle the distinct effect of each label entry a...

---

### 43. A computational account of dreaming: learning and memory consolidation

**Authors:** Qi Zhang

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04095v1)

**Summary:** A number of studies have concluded that dreaming is mostly caused by randomly arriving internal signals because "dream contents are random impulses", and argued that dream sleep is unlikely to play an important part in our intellectual capacity. On the contrary, numerous functional studies have revealed that dream sleep does play an important role in our learning and other intellectual functions. Specifically, recent studies have suggested the importance of dream sleep in memory consolidation, f...

---

### 44. FOVI: A biologically-inspired foveated interface for deep vision models

**Authors:** Nicholas M. Blauch, George A. Alvarez, Talia Konkle

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03766v1)

**Summary:** Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the...

---

### 45. A Minimal Task Reveals Emergent Path Integration and Object-Location Binding in a Predictive Sequence Model

**Authors:** Linda Ariel Ventura, Victoria Bosch, Tim C Kietzmann, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03490v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03490v1)

**Summary:** Adaptive cognition requires structured internal models representing objects and their relations. Predictive neural networks are often proposed to form such "world models", yet their underlying mechanisms remain unclear. One hypothesis is that action-conditioned sequential prediction suffices for learning such world models. In this work, we investigate this possibility in a minimal in-silico setting. Sequentially sampling tokens from 2D continuous token scenes, a recurrent neural network is train...

---

### 46. Systematic review of self-supervised foundation models for brain network representation using electroencephalography

**Authors:** Hannah Portmann, Yosuke Morishima

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03269v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03269v1)

**Summary:** Automated analysis of electroencephalography (EEG) has recently undergone a paradigm shift. The introduction of transformer architectures and self-supervised pretraining (SSL) has led to the development of EEG foundation models. These models are pretrained on large amounts of unlabeled data and can be adapted to a range of downstream tasks. This systematic review summarizes recent SSL-trained EEG foundation models that learn whole-brain representations from multichannel EEG rather than represent...

---

### 47. A Hitchhiker's Guide to Poisson Gradient Estimation

**Authors:** Michael Ibrahim, Hanqi Zhao, Eli Sennesh, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03896v1)

**Summary:** Poisson-distributed latent variable models are widely used in computational neuroscience, but differentiating through discrete stochastic samples remains challenging. Two approaches address this: Exponential Arrival Time (EAT) simulation and Gumbel-SoftMax (GSM) relaxation. We provide the first systematic comparison of these methods, along with practical guidance for practitioners. Our main technical contribution is a modification to the EAT method that theoretically guarantees an unbiased first...

---

### 48. Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging

**Authors:** Chetan Gohil, Oliver M. Cliff, James M. Shine, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03240v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03240v1)

**Summary:** Cognition is increasingly framed in terms of information processing, yet most fMRI analyses focus on activation or functional connectivity rather than quantifying how information is stored and transferred. To remedy this problem, we propose a framework for estimating measures of information processing: active information storage (AIS), transfer entropy (TE), and net synergy from task-based fMRI. AIS measures information maintained within a region, TE captures directed information flow, and net s...

---

### 49. Adversarial construction as a potential solution to the experiment design problem in large task spaces

**Authors:** Prakhar Godara, Frederick Callaway, Marcelo G. Mattar

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03172v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03172v1)

**Summary:** Despite decades of work, we still lack a robust, task-general theory of human behavior even in the simplest domains. In this paper we tackle the generality problem head-on, by aiming to develop a unified model for all tasks embedded in a task-space. In particular we consider the space of binary sequence prediction tasks where the observations are generated by the space parameterized by hidden Markov models (HMM). As the space of tasks is large, experimental exploration of the entire space is inf...

---

### 50. A Reproducible Framework for Bias-Resistant Machine Learning on Small-Sample Neuroimaging Data

**Authors:** Jagan Mohan Reddy Dwarampudi, Jennifer L Purks, Joshua Wong, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02920v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02920v1)

**Summary:** We introduce a reproducible, bias-resistant machine learning framework that integrates domain-informed feature engineering, nested cross-validation, and calibrated decision-threshold optimization for small-sample neuroimaging data. Conventional cross-validation frameworks that reuse the same folds for both model selection and performance estimation yield optimistically biased results, limiting reproducibility and generalization. Demonstrated on a high-dimensional structural MRI dataset of deep b...

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

