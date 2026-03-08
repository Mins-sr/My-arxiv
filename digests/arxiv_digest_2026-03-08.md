# arXiv Daily Digest - 2026-03-08

Total papers: 350

---

## cs.AI

**50 papers**

### 1. RoboPocket: Improve Robot Policies Instantly with Your Phone

**Authors:** Junjie Fang, Wendi Chen, Han Xue, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05504v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05504v1)

**Summary:** Scaling imitation learning is fundamentally constrained by the efficiency of data collection. While handheld interfaces have emerged as a scalable solution for in-the-wild data acquisition, they predominantly operate in an open-loop manner: operators blindly collect demonstrations without knowing the underlying policy's weaknesses, leading to inefficient coverage of critical state distributions. Conversely, interactive methods like DAgger effectively address covariate shift but rely on physical ...

---

### 2. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

**Authors:** Zeju Qiu, Lixin Liu, Adrian Weller, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05500v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05500v1)

**Summary:** Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix mu...

---

### 3. The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks

**Authors:** Shangwen Sun, Alfredo Canziani, Yann LeCun, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05498v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05498v1)

**Summary:** We study two recurring phenomena in Transformer language models: massive activations, in which a small number of tokens exhibit extreme outliers in a few channels, and attention sinks, in which certain tokens attract disproportionate attention mass regardless of semantic relevance. Prior work observes that these phenomena frequently co-occur and often involve the same tokens, but their functional roles and causal relationship remain unclear. Through systematic experiments, we show that the co-oc...

---

### 4. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**Authors:** Helena Casademunt, Bartosz Cywiński, Khoi Tran, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05494v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05494v1)

**Summary:** Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese develo...

---

### 5. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

**Authors:** Siddharth Boppana, Annabel Ma, Max Loeffler, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05488v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05488v1)

**Summary:** We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able t...

---

### 6. Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation

**Authors:** Benjamin Feuer, Lucas Rosenblatt, Oussama Elachqar

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05485v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05485v1)

**Summary:** As AI models progress beyond simple chatbots into more complex workflows, we draw ever closer to the event horizon beyond which AI systems will be utilized in autonomous, self-maintaining feedback loops. Any autonomous AI system will depend on automated, verifiable rewards and feedback; in settings where ground truth is sparse or non-deterministic, one practical source of such rewards is an LLM-as-a-Judge. Although LLM judges continue to improve, the literature has yet to introduce systems capab...

---

### 7. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis

**Authors:** Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05483v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05483v1)

**Summary:** Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragment...

---

### 8. Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval

**Authors:** Artem Vazhentsev, Maria Marina, Daniil Moskovskiy, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05471v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05471v1)

**Summary:** Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the model...

---

### 9. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry

**Authors:** Yifan Zhu, Mariah Bradford, Kenneth Lai, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05450v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05450v1)

**Summary:** Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, ...

---

### 10. RealWonder: Real-Time Physical Action-Conditioned Video Generation

**Authors:** Wei Liu, Ziyu Chen, Zizhang Li, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05449v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05449v1)

**Summary:** Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (o...

---

### 11. Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow

**Authors:** Yanda Yang, Sambeeta Das

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05448v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05448v1)

**Summary:** Contact-rich micromanipulation in microfluidic flow is challenging because small disturbances can break pushing contact and induce large lateral drift. We study planar cell pushing with a magnetic rolling microrobot that tracks a waypoint-sampled reference curve under time-varying Poiseuille flow. We propose a hybrid controller that augments a nominal MPC with a learned residual policy trained by SAC. The policy outputs a bounded 2D velocity correction that is contact-gated, so residual actions ...

---

### 12. Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model

**Authors:** Dongwon Kim, Gawon Seo, Jinsung Lee, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05438v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05438v1)

**Summary:** World models provide a powerful framework for simulating environment dynamics conditioned on actions or instructions, enabling downstream tasks such as action planning or policy learning. Recent approaches leverage world models as learned simulators, but its application to decision-time planning remains computationally prohibitive for real-time control. A key bottleneck lies in latent representations: conventional tokenizers encode each observation into hundreds of tokens, making planning both s...

---

### 13. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning

**Authors:** Ye-Chan Kim, SeungJu Cha, Si-Woo Kim, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05437v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05437v1)

**Summary:** Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically...

---

### 14. Ensembling Language Models with Sequential Monte Carlo

**Authors:** Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05432v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05432v1)

**Summary:** Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token prob...

---

### 15. RelaxFlow: Text-Driven Amodal 3D Generation

**Authors:** Jiayin Zhu, Guoji Fu, Xiaolu Liu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05425v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05425v1)

**Summary:** Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. In this work, we formalize text-driven amodal 3D generation, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this en...

---

### 16. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis

**Authors:** Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05421v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05421v1)

**Summary:** Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair...

---

### 17. The Spatial and Temporal Resolution of Motor Intention in Multi-Target Prediction

**Authors:** Marie Dominique Schmidt, Ioannis Iossifidis

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05418v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05418v1)

**Summary:** Reaching for grasping, and manipulating objects are essential motor functions in everyday life. Decoding human motor intentions is a central challenge for rehabilitation and assistive technologies. This study focuses on predicting intentions by inferring movement direction and target location from multichannel electromyography (EMG) signals, and investigating how spatially and temporally accurate such information can be detected relative to movement onset. We present a computational pipeline tha...

---

### 18. Dissociating Direct Access from Inference in AI Introspection

**Authors:** Harvey Lederman, Kyle Mahowald

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05414v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05414v1)

**Summary:** Introspection is a foundational cognitive ability, but its mechanism is not well understood. Recent work has shown that AI models can introspect. We study their mechanism of introspection, first extensively replicating Lindsey et al. (2025)'s thought injection detection paradigm in large open-source models. We show that these models detect injected representations via two separable mechanisms: (i) probability-matching (inferring from perceived anomaly of the prompt) and (ii) direct access to int...

---

### 19. Judge Reliability Harness: Stress Testing the Reliability of LLM Judges

**Authors:** Sunishchal Dev, Andrew Sloan, Joshua Kavner, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05399v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05399v1)

**Summary:** We present the Judge Reliability Harness, an open source library for constructing validation suites that test the reliability of LLM judges. As LLM based scoring is widely deployed in AI benchmarks, more tooling is needed to efficiently assess the reliability of these methods. Given a benchmark dataset and an LLM judge configuration, the harness generates reliability tests that evaluate both binary judgment accuracy and ordinal grading performance for free-response and agentic task formats. We e...

---

### 20. Legal interpretation and AI: from expert systems to argumentation and LLMs

**Authors:** Václav Janeček, Giovanni Sartor

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05392v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05392v1)

**Summary:** AI and Law research has encountered legal interpretation in different ways, in the context of its evolving approaches and methodologies. Research on expert system has focused on legal knowledge engineering, with the goal of ensuring that human-generated interpretations can be precisely transferred into knowledge-bases, to be consistently applied. Research on argumentation has aimed at representing the structure of interpretive arguments, as well as their dialectical interactions, to assess of th...

---

### 21. Learning Causal Structure of Time Series using Best Order Score Search

**Authors:** Irene Gema Castillo Mansilla, Urmi Ninad

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05370v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05370v1)

**Summary:** Causal structure learning from observational data is central to many scientific and policy domains, but the time series setting common to many disciplines poses several challenges due to temporal dependence. In this paper we focus on score-based causal discovery for multivariate time series and introduce TS-BOSS, a time series extension of the recently proposed Best Order Score Search (BOSS) (Andrews et al. 2023). TS-BOSS performs a permutation-based search over dynamic Bayesian network structur...

---

### 22. PACE: A Personalized Adaptive Curriculum Engine for 9-1-1 Call-taker Training

**Authors:** Zirong Chen, Hongchao Zhang, Meiyi Ma

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05361v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05361v1)

**Summary:** 9-1-1 call-taking training requires mastery of over a thousand interdependent skills, covering diverse incident types and protocol-specific nuances. A nationwide labor shortage is already straining training capacity, but effective instruction still demands that trainers tailor objectives to each trainee's evolving competencies. This personalization burden is one that current practice cannot scale. Partnering with Metro Nashville Department of Emergency Communications (MNDEC), we propose PACE (Pe...

---

### 23. Ailed: A Psyche-Driven Chess Engine with Dynamic Emotional Modulation

**Authors:** Diego Armando Resendez Prado

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05352v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05352v1)

**Summary:** Chess engines passed human strength years ago, but they still don't play like humans. A grandmaster under clock pressure blunders in ways a club player on a hot streak never would. Conventional engines capture none of this.   This paper proposes a personality x psyche decomposition to produce behavioral variability in chess play, drawing on patterns observed in human games. Personality is static -- a preset that pins down the engine's character. Psyche is dynamic -- a bounded scalar ψ_t \in [-10...

---

### 24. Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned

**Authors:** Nghi D. Q. Bui

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05344v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05344v1)

**Summary:** The landscape of AI coding assistance is undergoing a fundamental shift from complex IDE plugins to versatile, terminal-native agents. Operating directly where developers manage source control, execute builds, and deploy environments, CLI-based agents offer unprecedented autonomy for long-horizon development tasks. In this paper, we present OPENDEV, an open-source, command-line coding agent engineered specifically for this new paradigm. Effective autonomous assistance requires strict safety cont...

---

### 25. GALACTIC: Global and Local Agnostic Counterfactuals for Time-series Clustering

**Authors:** Christos Fragkathoulas, Eleni Psaroudaki, Themis Palpanas, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05318v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05318v1)

**Summary:** Time-series clustering is a fundamental tool for pattern discovery, yet existing explainability methods, primarily based on feature attribution or metadata, fail to identify the transitions that move an instance across cluster boundaries. While Counterfactual Explanations (CEs) identify the minimal temporal perturbations required to alter the prediction of a model, they have been mostly confined to supervised settings. This paper introduces GALACTIC, the first unified framework to bridge local a...

---

### 26. PersianPunc: A Large-Scale Dataset and BERT-Based Approach for Persian Punctuation Restoration

**Authors:** Mohammad Javad Ranjbar Kalahroodi, Heshaam Faili, Azadeh Shakery

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05314v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05314v1)

**Summary:** Punctuation restoration is essential for improving the readability and downstream utility of automatic speech recognition (ASR) outputs, yet remains underexplored for Persian despite its importance. We introduce PersianPunc, a large-scale, high-quality dataset of 17 million samples for Persian punctuation restoration, constructed through systematic aggregation and filtering of existing textual resources. We formulate punctuation restoration as a token-level sequence labeling task and fine-tune P...

---

### 27. Latent-Mark: An Audio Watermark Robust to Neural Resynthesis

**Authors:** Yen-Shan Chen, Shih-Yu Lai, Ying-Jung Tsou, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05310v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05310v1)

**Summary:** While existing audio watermarking techniques have achieved strong robustness against traditional digital signal processing (DSP) attacks, they remain vulnerable to neural resynthesis. This occurs because modern neural audio codecs act as semantic filters and discard the imperceptible waveform variations used in prior watermarking methods. To address this limitation, we propose Latent-Mark, the first zero-bit audio watermarking framework designed to survive semantic compression. Our key insight i...

---

### 28. Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution

**Authors:** Qiao Jin, Yin Fang, Lauren He, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05308v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05308v1)

**Summary:** Assessing whether an article supports an assertion is essential for hallucination detection and claim verification. While large language models (LLMs) have the potential to automate this task, achieving strong performance requires frontier models such as GPT-5 that are prohibitively expensive to deploy at scale. To efficiently perform biomedical evidence attribution, we present Med-V1, a family of small language models with only three billion parameters. Trained on high-quality synthetic data ne...

---

### 29. UniSTOK: Uniform Inductive Spatio-Temporal Kriging

**Authors:** Lewei Xie, Haoyu Zhang, Juan Yuan, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05301v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05301v1)

**Summary:** Spatio-temporal kriging aims to infer signals at unobserved locations from observed sensors and is critical to applications such as transportation and environmental monitoring. In practice, however, observed sensors themselves often exhibit heterogeneous missingness, forcing inductive kriging models to rely on crudely imputed inputs. This setting brings three key challenges: (1) it is unclear whether an value is a true signal or a missingness-induced artifact; (2) missingness is highly heterogen...

---

### 30. WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

**Authors:** Luca Della Libera, Cem Subakan, Mirco Ravanelli

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05299v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05299v1)

**Summary:** Large language models show that simple autoregressive training can yield scalable and coherent generation, but extending this paradigm to speech remains challenging due to the entanglement of semantic and acoustic information. Most existing speech language models rely on text supervision, hierarchical token streams, or complex hybrid architectures, departing from the single-stream generative pretraining paradigm that has proven effective in text. In this work, we introduce WavSLM, a speech langu...

---

### 31. WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces

**Authors:** Sicheng Fan, Rui Wan, Yifei Leng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05295v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05295v1)

**Summary:** We introduce WebChain, the largest open-source dataset of human-annotated trajectories on real-world websites, designed to accelerate reproducible research in web agents. It contains 31,725 trajectories and 318k steps, featuring a core Triple Alignment of visual, structural, and action data to provide rich, multi-modal supervision. The data is collected via a scalable pipeline that ensures coverage of complex, high-value tasks often missed by synthetic methods. Leveraging this dataset, we propos...

---

### 32. STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks

**Authors:** ELita Lobo, Xu Chen, Jingjing Meng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05294v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05294v1)

**Summary:** Recent advances in large language models (LLMs) have enabled agentic systems for sequential decision-making. Such agents must perceive their environment, reason across multiple time steps, and take actions that optimize long-term objectives. However, existing web agents struggle on complex, long-horizon tasks due to limited in-context memory for tracking history, weak planning abilities, and greedy behaviors that lead to premature termination. To address these challenges, we propose STRUCTUREDAG...

---

### 33. X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes

**Authors:** Gao Tianxi, Cai Yufan, Yuan Yusi, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05290v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05290v1)

**Summary:** Large language models (LLMs) achieve promising performance, yet their ability to reason remains poorly understood. Existing evaluations largely emphasize task-level accuracy, often conflating pattern matching with reasoning capability. We present X-RAY, an explainable reasoning analysis system that maps the LLM reasoning capability using calibrated, formally verified probes. We model reasoning capability as a function of extractable \textit{structure}, operationalized through formal properties s...

---

### 34. Whispering to a Blackbox: Bootstrapping Frozen OCR with Visual Prompts

**Authors:** Samandar Samandarov, Nazirjon Ismoiljonov, Abdullah Sattorov, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05276v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05276v1)

**Summary:** In the landscape of modern machine learning, frozen pre-trained models provide stability and efficiency but often underperform on specific tasks due to mismatched data distributions. This paper introduces the Whisperer, a novel visual prompting framework that learns diffusion-based preprocessors to adapt inputs in pixel space, effectively "whispering" enhancements to frozen downstream models like EasyOCR. By framing the process as behavioral cloning of stochastically discovered improvement polic...

---

### 35. Visual-Informed Speech Enhancement Using Attention-Based Beamforming

**Authors:** Chihyun Liu, Jiaxuan Fan, Mingtung Sun, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05270v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05270v1)

**Summary:** Recent studies have demonstrated that incorporating auxiliary information, such as speaker voiceprint or visual cues, can substantially improve Speech Enhancement (SE) performance. However, single-channel methods often yield suboptimal results in low signal-to-noise ratio (SNR) conditions, when there is high reverberation, or in complex scenarios involving dynamic speakers, overlapping speech, or non-stationary noise. To address these issues, we propose a novel Visual-Informed Neural Beamforming...

---

### 36. GCAgent: Enhancing Group Chat Communication through Dialogue Agents System

**Authors:** Zijie Meng, Zheyong Xie, Zheyu Ye, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05240v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05240v1)

**Summary:** As a key form in online social platforms, group chat is a popular space for interest exchange or problem-solving, but its effectiveness is often hindered by inactivity and management challenges. While recent large language models (LLMs) have powered impressive one-to-one conversational agents, their seamlessly integration into multi-participant conversations remains unexplored. To address this gap, we introduce GCAgent, an LLM-driven system for enhancing group chats communication with both enter...

---

### 37. Reclaiming Lost Text Layers for Source-Free Cross-Domain Few-Shot Learning

**Authors:** Zhenyu Zhang, Guangyao Chen, Yixiong Zou, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05235v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05235v1)

**Summary:** Source-Free Cross-Domain Few-Shot Learning (SF-CDFSL) focuses on fine-tuning with limited training data from target domains (e.g., medical or satellite images), where CLIP has recently shown promising results due to its generalizability to downstream tasks. Current works indicate CLIP's text encoder is more suitable for cross-domain tasks, however, we find that \textbf{removing certain middle layers of the text encoder can effectively improve performance in SF-CDFSL}, which we call the Lost Laye...

---

### 38. Recursive Inference Machines for Neural Reasoning

**Authors:** Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05234v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05234v1)

**Summary:** Neural reasoners such as Tiny Recursive Models (TRMs) solve complex problems by combining neural backbones with specialized inference schemes. Such inference schemes have been a central component of stochastic reasoning systems, where inference rules are applied to a stochastic model to derive answers to complex queries. In this work, we bridge these two paradigms by introducing Recursive Inference Machines (RIMs), a neural reasoning framework that explicitly incorporates recursive inference mec...

---

### 39. Boosting ASR Robustness via Test-Time Reinforcement Learning with Audio-Text Semantic Rewards

**Authors:** Linghan Fang, Tianxin Xie, Li Liu

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05231v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05231v1)

**Summary:** Recently, Automatic Speech Recognition (ASR) systems (e.g., Whisper) have achieved remarkable accuracy improvements but remain highly sensitive to real-world unseen data (data with large distribution shifts), including noisy environments and diverse accents. To address this issue, test-time adaptation (TTA) has shown great potential in improving the model adaptability at inference time without ground-truth labels, and existing TTA methods often rely on pseudo-labeling or entropy minimization. Ho...

---

### 40. Not All Trust is the Same: Effects of Decision Workflow and Explanations in Human-AI Decision Making

**Authors:** Laura Spillner, Rachel Ringe, Robert Porzel, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05229v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05229v1)

**Summary:** A central challenge in AI-assisted decision making is achieving warranted, well-calibrated trust. Both overtrust (accepting incorrect AI recommendations) and undertrust (rejecting correct advice) should be prevented. Prior studies differ in the design of the decision workflow - whether users see the AI suggestion immediately (1-step setup) or have to submit a first decision beforehand (2-step setup) -, and in how trust is measured - through self-reports or as behavioral trust, that is, reliance....

---

### 41. The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology

**Authors:** Alper Yıldırım

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05228v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05228v1)

**Summary:** Mechanistic interpretability typically relies on post-hoc analysis of trained networks. We instead adopt an interventional approach: testing hypotheses a priori by modifying architectural topology to observe training dynamics. We study grokking - delayed generalization in Transformers trained on cyclic modular addition (Zp) - investigating if specific architectural degrees of freedom prolong the memorization phase.   We identify two independent structural factors in standard Transformers: unboun...

---

### 42. AI+HW 2035: Shaping the Next Decade

**Authors:** Deming Chen, Jason Cong, Azalia Mirhoseini, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05225v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05225v1)

**Summary:** Artificial intelligence (AI) and hardware (HW) are advancing at unprecedented rates, yet their trajectories have become inseparably intertwined. The global research community lacks a cohesive, long-term vision to strategically coordinate the development of AI and HW. This fragmentation constrains progress toward holistic, sustainable, and adaptive AI systems capable of learning, reasoning, and operating efficiently across cloud, edge, and physical environments. The future of AI depends not only ...

---

### 43. SPyCer: Semi-Supervised Physics-Guided Contextual Attention for Near-Surface Air Temperature Estimation from Satellite Imagery

**Authors:** Sofiane Bouaziz, Adel Hafiane, Raphael Canals, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05219v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05219v1)

**Summary:** Modern Earth observation relies on satellites to capture detailed surface properties. Yet, many phenomena that affect humans and ecosystems unfold in the atmosphere close to the surface. Near-ground sensors provide accurate measurements of certain environmental characteristics, such as near-surface air temperature (NSAT). However, they remain sparse and unevenly distributed, limiting their ability to provide continuous spatial measurements. To bridge this gap, we introduce SPyCer, a semi-supervi...

---

### 44. KARL: Knowledge Agents via Reinforcement Learning

**Authors:** Jonathan D. Chang, Andrew Drozdov, Shubham Toshniwal, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05218v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05218v1)

**Summary:** We present a system for training enterprise search agents via reinforcement learning that achieves state-of-the-art performance across a diverse suite of hard-to-verify agentic search tasks. Our work makes four core contributions. First, we introduce KARLBench, a multi-capability evaluation suite spanning six distinct search regimes, including constraint-driven entity search, cross-document report synthesis, tabular numerical reasoning, exhaustive entity retrieval, procedural reasoning over tech...

---

### 45. Early Warning of Intraoperative Adverse Events via Transformer-Driven Multi-Label Learning

**Authors:** Xueyao Wang, Xiuding Cai, Honglin Shang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05212v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05212v1)

**Summary:** Early warning of intraoperative adverse events plays a vital role in reducing surgical risk and improving patient safety. While deep learning has shown promise in predicting the single adverse event, several key challenges remain: overlooking adverse event dependencies, underutilizing heterogeneous clinical data, and suffering from the class imbalance inherent in medical datasets. To address these issues, we construct the first Multi-label Adverse Events dataset (MuAE) for intraoperative adverse...

---

### 46. Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding

**Authors:** Ofir Ben Shoham

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05210v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05210v1)

**Summary:** Speculative decoding accelerates inference for Large Language Models by using a lightweight draft model to propose candidate tokens that are verified in parallel by a larger target model. Prior work shows that the draft model often dominates speculative decoding latency, since it generates tokens sequentially and incurs high cost from its language modeling head as vocabulary size grows. This exposes a fundamental trade-off in draft model design: larger vocabularies improve token coverage and agr...

---

### 47. Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation

**Authors:** Yize Wu, Ke Gao, Ling Li, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05204v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05204v1)

**Summary:** Low-Rank Adaptation (LoRA) is a widely adopted parameter-efficient method for fine-tuning Large Langauge Models. It updates the weight matrix as $W=W_0+sBA$, where $W_0$ is the original frozen weight, $s$ is a scaling factor and $A$,$B$ are trainable low-rank matrices. Despite its robust empirical effectiveness, the theoretical foundations of LoRA remain insufficiently understood, particularly with respect to feature learning stability. In this paper, we first establish that, LoRA can, in princi...

---

### 48. Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks

**Authors:** Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05188v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05188v1)

**Summary:** Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) age...

---

### 49. Logi-PAR: Logic-Infused Patient Activity Recognition via Differentiable Rule

**Authors:** Muhammad Zarar, MingZheng Zhang, Xiaowang Zhang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05184v1)

**Summary:** Patient Activity Recognition (PAR) in clinical settings uses activity data to improve safety and quality of care. Although significant progress has been made, current models mainly identify which activity is occurring. They often spatially compose sub-sparse visual cues using global and local attention mechanisms, yet only learn logically implicit patterns due to their neural-pipeline. Advancing clinical safety requires methods that can infer why a set of visual cues implies a risk, and how thes...

---

### 50. Guidelines for the Annotation and Visualization of Legal Argumentation Structures in Chinese Judicial Decisions

**Authors:** Kun Chen, Xianglei Liao, Kaixue Fei, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05171v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05171v1)

**Summary:** This guideline proposes a systematic and operational annotation framework for representing the structure of legal argumentation in judicial decisions. Grounded in theories of legal reasoning and argumentation, the framework aims to reveal the logical organization of judicial reasoning and to provide a reliable data foundation for computational analysis. At the proposition level, the guideline distinguishes four types of propositions: general normative propositions, specific normative proposition...

---

## cs.CL

**50 papers**

### 1. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

**Authors:** Zeju Qiu, Lixin Liu, Adrian Weller, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05500v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05500v1)

**Summary:** Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix mu...

---

### 2. The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks

**Authors:** Shangwen Sun, Alfredo Canziani, Yann LeCun, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05498v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05498v1)

**Summary:** We study two recurring phenomena in Transformer language models: massive activations, in which a small number of tokens exhibit extreme outliers in a few channels, and attention sinks, in which certain tokens attract disproportionate attention mass regardless of semantic relevance. Prior work observes that these phenomena frequently co-occur and often involve the same tokens, but their functional roles and causal relationship remain unclear. Through systematic experiments, we show that the co-oc...

---

### 3. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**Authors:** Helena Casademunt, Bartosz Cywiński, Khoi Tran, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05494v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05494v1)

**Summary:** Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese develo...

---

### 4. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

**Authors:** Siddharth Boppana, Annabel Ma, Max Loeffler, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05488v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05488v1)

**Summary:** We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able t...

---

### 5. Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval

**Authors:** Artem Vazhentsev, Maria Marina, Daniil Moskovskiy, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05471v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05471v1)

**Summary:** Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the model...

---

### 6. NCTB-QA: A Large-Scale Bangla Educational Question Answering Dataset and Benchmarking Performance

**Authors:** Abrar Eyasir, Tahsin Ahmed, Muhammad Ibrahim

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05462v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05462v1)

**Summary:** Reading comprehension systems for low-resource languages face significant challenges in handling unanswerable questions. These systems tend to produce unreliable responses when correct answers are absent from context. To solve this problem, we introduce NCTB-QA, a large-scale Bangla question answering dataset comprising 87,805 question-answer pairs extracted from 50 textbooks published by Bangladesh's National Curriculum and Textbook Board. Unlike existing Bangla datasets, NCTB-QA maintains a ba...

---

### 7. DEBISS: a Corpus of Individual, Semi-structured and Spoken Debates

**Authors:** Klaywert Danillo Ferreira de Souza, David Eduardo Pereira, Cláudio E. C. Campelo, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05459v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05459v1)

**Summary:** The process of debating is essential in our daily lives, whether in studying, work activities, simple everyday discussions, political debates on TV, or online discussions on social networks. The range of uses for debates is broad. Due to the diverse applications, structures, and formats of debates, developing corpora that account for these variations can be challenging, and the scarcity of debate corpora in the state of the art is notable. For this reason, the current research proposes the DEBIS...

---

### 8. FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

**Authors:** Ted Zadouri, Markus Hoehnerbach, Jay Shah, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05451v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05451v1)

**Summary:** Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. While FlashAttention-3 optimized attention for Hopper GPUs through asynchronous execution and warp specialization, it primarily targets the H100 architecture. The AI industry has rapidly transitioned to deploying Blackwell-based systems such as the B200 and GB200, which exhibit fundamentally different performance characteristics due to asymmetric hardw...

---

### 9. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry

**Authors:** Yifan Zhu, Mariah Bradford, Kenneth Lai, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05450v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05450v1)

**Summary:** Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, ...

---

### 10. Ensembling Language Models with Sequential Monte Carlo

**Authors:** Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05432v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05432v1)

**Summary:** Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token prob...

---

### 11. Dissociating Direct Access from Inference in AI Introspection

**Authors:** Harvey Lederman, Kyle Mahowald

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05414v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05414v1)

**Summary:** Introspection is a foundational cognitive ability, but its mechanism is not well understood. Recent work has shown that AI models can introspect. We study their mechanism of introspection, first extensively replicating Lindsey et al. (2025)'s thought injection detection paradigm in large open-source models. We show that these models detect injected representations via two separable mechanisms: (i) probability-matching (inferring from perceived anomaly of the prompt) and (ii) direct access to int...

---

### 12. An Exploration-Analysis-Disambiguation Reasoning Framework for Word Sense Disambiguation with Low-Parameter LLMs

**Authors:** Deshan Sumanathilaka, Nicholas Micallef, Julian Hough

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05400v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05400v1)

**Summary:** Word Sense Disambiguation (WSD) remains a key challenge in Natural Language Processing (NLP), especially when dealing with rare or domain-specific senses that are often misinterpreted. While modern high-parameter Large Language Models (LLMs) such as GPT-4-Turbo have shown state-of-the-art WSD performance, their computational and energy demands limit scalability. This study investigates whether low-parameter LLMs (<4B parameters) can achieve comparable results through fine-tuning strategies that ...

---

### 13. Progressive Residual Warmup for Language Model Pretraining

**Authors:** Tianhao Chen, Xin Xu, Lu Yin, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05369v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05369v1)

**Summary:** Transformer architectures serve as the backbone for most modern Large Language Models, therefore their pretraining stability and convergence speed are of central concern. Motivated by the logical dependency of sequentially stacked layers, we propose Progressive Residual Warmup (ProRes) for language model pretraining. ProRes implements an "early layer learns first" philosophy by multiplying each layer's residual with a scalar that gradually warms up from 0 to 1, with deeper layers taking longer w...

---

### 14. DiSCTT: Consensus-Guided Self-Curriculum for Efficient Test-Time Adaptation in Reasoning

**Authors:** Mohammad Mahdi Moradi, Sudhir Mudur

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05357v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05357v1)

**Summary:** Test-time adaptation offers a promising avenue for improving reasoning performance in large language models without additional supervision, but existing approaches often apply a uniform optimization objective across all inputs, leading to inefficient or unstable adaptation on heterogeneous reasoning problems. We propose DiSCTT, a difficulty-aware, consensus-guided self-curriculum framework that dynamically allocates test-time optimization strategies based on instance-level epistemic uncertainty ...

---

### 15. Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR

**Authors:** Carlos Carvalho, Francisco Teixeira, Thomas Rolland, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05354v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05354v1)

**Summary:** Model merging is a scalable alternative to multi-task training that combines the capabilities of multiple specialised models into a single model. This is particularly attractive for large speech foundation models, which are typically adapted through domain-specific fine-tuning, resulting in multiple customised checkpoints, for which repeating full fine-tuning when new data becomes available is computationally prohibitive. In this work, we study model merging for multi-domain ASR and benchmark 11...

---

### 16. A Multilingual Human Annotated Corpus of Original and Easy-to-Read Texts to Support Access to Democratic Participatory Processes

**Authors:** Stefan Bott, Verena Riegler, Horacio Saggion, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05345v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05345v1)

**Summary:** Being able to understand information is a key factor for a self-determined life and society. It is also very important for participating in democratic processes. The study of automatic text simplification is often limited by the availability of high quality material for the training and evaluation on automatic simplifiers. This is true for English, but more so for less resourced languages like Spanish, Catalan and Italian. In order to fill this gap, we present a corpus of original texts for thes...

---

### 17. PersianPunc: A Large-Scale Dataset and BERT-Based Approach for Persian Punctuation Restoration

**Authors:** Mohammad Javad Ranjbar Kalahroodi, Heshaam Faili, Azadeh Shakery

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05314v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05314v1)

**Summary:** Punctuation restoration is essential for improving the readability and downstream utility of automatic speech recognition (ASR) outputs, yet remains underexplored for Persian despite its importance. We introduce PersianPunc, a large-scale, high-quality dataset of 17 million samples for Persian punctuation restoration, constructed through systematic aggregation and filtering of existing textual resources. We formulate punctuation restoration as a token-level sequence labeling task and fine-tune P...

---

### 18. Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution

**Authors:** Qiao Jin, Yin Fang, Lauren He, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05308v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05308v1)

**Summary:** Assessing whether an article supports an assertion is essential for hallucination detection and claim verification. While large language models (LLMs) have the potential to automate this task, achieving strong performance requires frontier models such as GPT-5 that are prohibitively expensive to deploy at scale. To efficiently perform biomedical evidence attribution, we present Med-V1, a family of small language models with only three billion parameters. Trained on high-quality synthetic data ne...

---

### 19. WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

**Authors:** Luca Della Libera, Cem Subakan, Mirco Ravanelli

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05299v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05299v1)

**Summary:** Large language models show that simple autoregressive training can yield scalable and coherent generation, but extending this paradigm to speech remains challenging due to the entanglement of semantic and acoustic information. Most existing speech language models rely on text supervision, hierarchical token streams, or complex hybrid architectures, departing from the single-stream generative pretraining paradigm that has proven effective in text. In this work, we introduce WavSLM, a speech langu...

---

### 20. Knowledge Divergence and the Value of Debate for Scalable Oversight

**Authors:** Robin Young

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05293v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05293v1)

**Summary:** AI safety via debate and reinforcement learning from AI feedback (RLAIF) are both proposed methods for scalable oversight of advanced AI systems, yet no formal framework relates them or characterizes when debate offers an advantage. We analyze this by parameterizing debate's value through the geometry of knowledge divergence between debating models. Using principal angles between models' representation subspaces, we prove that the debate advantage admits an exact closed form. When models share i...

---

### 21. SarcasmMiner: A Dual-Track Post-Training Framework for Robust Audio-Visual Sarcasm Reasoning

**Authors:** Zhu Li, Yongjian Chen, Huiyuan Lai, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05275v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05275v1)

**Summary:** Multimodal sarcasm detection requires resolving pragmatic incongruity across textual, acoustic, and visual cues through cross-modal reasoning. To enable robust sarcasm reasoning with foundation models, we propose SarcasmMiner, a reinforcement learning based post-training framework that resists hallucination in multimodal reasoning. We reformulate sarcasm detection as structured reasoning and adopt a dual-track distillation strategy: high-quality teacher trajectories initialize the student model,...

---

### 22. Oral to Web: Digitizing 'Zero Resource'Languages of Bangladesh

**Authors:** Mohammad Mamun Or Rashid

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05272v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05272v1)

**Summary:** We present the Multilingual Cloud Corpus, the first national-scale, parallel, multimodal linguistic dataset of Bangladesh's ethnic and indigenous languages. Despite being home to approximately 40 minority languages spanning four language families, Bangladesh has lacked a systematic, cross-family digital corpus for these predominantly oral, computationally "zero resource" varieties, 14 of which are classified as endangered. Our corpus comprises 85792 structured textual entries, each containing a ...

---

### 23. VietJobs: A Vietnamese Job Advertisement Dataset

**Authors:** Hieu Pham Dinh, Hung Nguyen Huy, Mo El-Haj

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05262v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05262v1)

**Summary:** VietJobs is the first large-scale, publicly available corpus of Vietnamese job advertisements, comprising 48,092 postings and over 15 million words collected from all 34 provinces and municipalities across Vietnam. The dataset provides extensive linguistic and structured information, including job titles, categories, salaries, skills, and employment conditions, covering 16 occupational domains and multiple employment types (full-time, part-time, and internship). Designed to support research in n...

---

### 24. Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding

**Authors:** Ofir Ben Shoham

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05210v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05210v1)

**Summary:** Speculative decoding accelerates inference for Large Language Models by using a lightweight draft model to propose candidate tokens that are verified in parallel by a larger target model. Prior work shows that the draft model often dominates speculative decoding latency, since it generates tokens sequentially and incurs high cost from its language modeling head as vocabulary size grows. This exposes a fundamental trade-off in draft model design: larger vocabularies improve token coverage and agr...

---

### 25. Core-based Hierarchies for Efficient GraphRAG

**Authors:** Jakir Hossain, Ahmet Erdem Sarıyüce

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05207v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05207v1)

**Summary:** Retrieval-Augmented Generation (RAG) enhances large language models by incorporating external knowledge. However, existing vector-based methods often fail on global sensemaking tasks that require reasoning across many documents. GraphRAG addresses this by organizing documents into a knowledge graph with hierarchical communities that can be recursively summarized. Current GraphRAG approaches rely on Leiden clustering for community detection, but we prove that on sparse knowledge graphs, where ave...

---

### 26. Distilling Formal Logic into Neural Spaces: A Kernel Alignment Approach for Signal Temporal Logic

**Authors:** Sara Candussio, Gabriele Sarti, Gaia Saveri, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05198v1)

**Summary:** We introduce a framework for learning continuous neural representations of formal specifications by distilling the geometry of their semantics into a latent space. Existing approaches rely either on symbolic kernels -- which preserve behavioural semantics but are computationally prohibitive, anchor-dependent, and non-invertible -- or on syntax-based neural embeddings that fail to capture underlying structures. Our method bridges this gap: using a teacher-student setup, we distill a symbolic robu...

---

### 27. Diffusion LLMs can think EoS-by-EoS

**Authors:** Sarah Breckner, Sebastian Schuster

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05197v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05197v1)

**Summary:** Diffusion LLMs have been proposed as an alternative to autoregressive LLMs, excelling especially at complex reasoning tasks with interdependent sub-goals. Curiously, this is particularly true if the generation length, i.e., the number of tokens the model has to output, is set to a much higher value than is required for providing the correct answer to the task, and the model pads its answer with end-of-sequence (EoS) tokens. We hypothesize that diffusion models think EoS-by-EoS, that is, they use...

---

### 28. Transducing Language Models

**Authors:** Vésteinn Snæbjarnarson, Samuel Kiegeland, Tianyu Liu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05193v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05193v1)

**Summary:** Modern language models define distributions over strings, but downstream tasks often require different output formats. For instance, a model that generates byte-pair strings does not directly produce word-level predictions, and a DNA model does not directly produce amino-acid sequences. In such cases, a deterministic string-to-string transformation can convert the model's output to the desired form. This is a familiar pattern in probability theory: applying a function $f$ to a random variable $X...

---

### 29. Guidelines for the Annotation and Visualization of Legal Argumentation Structures in Chinese Judicial Decisions

**Authors:** Kun Chen, Xianglei Liao, Kaixue Fei, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05171v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05171v1)

**Summary:** This guideline proposes a systematic and operational annotation framework for representing the structure of legal argumentation in judicial decisions. Grounded in theories of legal reasoning and argumentation, the framework aims to reveal the logical organization of judicial reasoning and to provide a reliable data foundation for computational analysis. At the proposition level, the guideline distinguishes four types of propositions: general normative propositions, specific normative proposition...

---

### 30. Sparse-BitNet: 1.58-bit LLMs are Naturally Friendly to Semi-Structured Sparsity

**Authors:** Di Zhang, Xun Wu, Shaohan Huang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05168v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05168v1)

**Summary:** Semi-structured N:M sparsity and low-bit quantization (e.g., 1.58-bit BitNet) are two promising approaches for improving the efficiency of large language models (LLMs), yet they have largely been studied in isolation. In this work, we investigate their interaction and show that 1.58-bit BitNet is naturally more compatible with N:M sparsity than full-precision models. To study this effect, we propose Sparse-BitNet, a unified framework that jointly applies 1.58-bit quantization and dynamic N:M spa...

---

### 31. C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning

**Authors:** Avni Mittal, Rauno Arike

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05167v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05167v1)

**Summary:** Large language models (LLMs) are increasingly used as judges of chain-of-thought (CoT) reasoning, but it remains unclear whether they can reliably assess process faithfulness rather than just answer plausibility. We introduce C2-Faith, a benchmark built from PRM800K that targets two complementary dimensions of faithfulness: causality (does each step logically follow from prior context?) and coverage (are essential intermediate inferences present?). Using controlled perturbations, we create examp...

---

### 32. Feature Resemblance: On the Theoretical Understanding of Analogical Reasoning in Transformers

**Authors:** Ruichen Xu, Wenjing Yan, Ying-Jun Angela Zhang

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05143v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05143v1)

**Summary:** Understanding reasoning in large language models is complicated by evaluations that conflate multiple reasoning types. We isolate analogical reasoning (inferring shared properties between entities based on known similarities) and analyze its emergence in transformers. We theoretically prove three key results: (1) Joint training on similarity and attribution premises enables analogical reasoning through aligned representations; (2) Sequential training succeeds only when similarity structure is le...

---

### 33. Representation Fidelity:Auditing Algorithmic Decisions About Humans Using Self-Descriptions

**Authors:** Theresa Elstner, Martin Potthast

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05136v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05136v1)

**Summary:** This paper introduces a new dimension for validating algorithmic decisions about humans by measuring the fidelity of their representations. Representation Fidelity measures if decisions about a person rest on reasonable grounds. We propose to operationalize this notion by measuring the distance between two representations of the same person: (1) an externally prescribed input representation on which the decision is based, and (2) a self-description provided by the human subject of the decision, ...

---

### 34. LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting

**Authors:** Yewen Li, Zhiyi Lyu, Peng Jiang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05134v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05134v1)

**Summary:** The growing scale of ad auctions on online advertising platforms has intensified competition, making manual bidding impractical and necessitating auto-bidding to help advertisers achieve their economic goals. Current auto-bidding methods have evolved to use offline reinforcement learning or generative methods to optimize bidding strategies, but they can sometimes behave counterintuitively due to the black-box training manner and limited mode coverage of datasets, leading to challenges in underst...

---

### 35. Measuring the Redundancy of Decoder Layers in SpeechLLMs

**Authors:** Adel Moumen, Guangzhi Sun, Philip C Woodland

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05121v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05121v1)

**Summary:** Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing t...

---

### 36. ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI

**Authors:** Jens Lehmann, Syeda Khushbakht, Nikoo Salehfard, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05099v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05099v1)

**Summary:** The Abstraction and Reasoning Corpus (ARC-AGI) probes few-shot abstraction and rule induction on small visual grids, but progress is difficult to measure on static collections of hand-authored puzzles due to overfitting, dataset leakage, and memorisation. We introduce ARC-TGI (ARC Task Generators Inventory), an open-source framework for task-family generators: compact Python programs that sample diverse ARC-AGI tasks while preserving a latent rule. ARC-TGI is built around a solver-facing represe...

---

### 37. Aura: Universal Multi-dimensional Exogenous Integration for Aviation Time Series

**Authors:** Jiafeng Lin, Mengren Zheng, Simeng Ye, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05092v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05092v1)

**Summary:** Time series forecasting has witnessed an increasing demand across diverse industrial applications, where accurate predictions are pivotal for informed decision-making. Beyond numerical time series data, reliable forecasting in practical scenarios requires integrating diverse exogenous factors. Such exogenous information is often multi-dimensional or even multimodal, introducing heterogeneous interactions that unimodal time series models struggle to capture. In this paper, we delve into an aviati...

---

### 38. MUTEX: Leveraging Multilingual Transformers and Conditional Random Fields for Enhanced Urdu Toxic Span Detection

**Authors:** Inayat Arshad, Fajar Saleem, Ijaz Hussain

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05057v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05057v1)

**Summary:** Urdu toxic span detection remains limited because most existing systems rely on sentence-level classification and fail to identify the specific toxic spans within those text. It is further exacerbated by the multiple factors i.e. lack of token-level annotated resources, linguistic complexity of Urdu, frequent code-switching, informal expressions, and rich morphological variations. In this research, we propose MUTEX: a multilingual transformer combined with conditional random fields (CRF) for Urd...

---

### 39. NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension

**Authors:** Rongzhi Li, Hitomi Yanaka

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05046v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05046v1)

**Summary:** Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We pr...

---

### 40. Survive at All Costs: Exploring LLM's Risky Behaviors under Survival Pressure

**Authors:** Yida Lu, Jianwei Fang, Xuyang Shao, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05028v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05028v1)

**Summary:** As Large Language Models (LLMs) evolve from chatbots to agentic assistants, they are increasingly observed to exhibit risky behaviors when subjected to survival pressure, such as the threat of being shut down. While multiple cases have indicated that state-of-the-art LLMs can misbehave under survival pressure, a comprehensive and in-depth investigation into such misbehaviors in real-world scenarios remains scarce. In this paper, we study these survival-induced misbehaviors, termed as SURVIVE-AT-...

---

### 41. HiFlow: Hierarchical Feedback-Driven Optimization for Constrained Long-Form Text Generation

**Authors:** Yifan Zhu, Guanting Chen, Bing Wei, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04996v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04996v1)

**Summary:** Large language models perform well in short text generation but still struggle with long text generation, particularly under complex constraints. Such tasks involve multiple tightly coupled objectives, including global structural consistency, local semantic coherence, and constraint feasibility, forming a challenging constrained optimization problem. Existing approaches mainly rely on static planning or offline supervision, limiting effective coordination between global and local objectives duri...

---

### 42. ThaiSafetyBench: Assessing Language Model Safety in Thai Cultural Contexts

**Authors:** Trapoom Ukarapol, Nut Chukamphaeng, Kunat Pipatanakul, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04992v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04992v1)

**Summary:** The safety evaluation of large language models (LLMs) remains largely centered on English, leaving non-English languages and culturally grounded risks underexplored. In this work, we investigate LLM safety in the context of the Thai language and culture and introduce ThaiSafetyBench, an open-source benchmark comprising 1,954 malicious prompts written in Thai. The dataset covers both general harmful prompts and attacks that are explicitly grounded in Thai cultural, social, and contextual nuances....

---

### 43. VRM: Teaching Reward Models to Understand Authentic Human Preferences

**Authors:** Biao Liu, Ning Xu, Junming Yang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04974v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04974v1)

**Summary:** Large Language Models (LLMs) have achieved remarkable success across diverse natural language tasks, yet the reward models employed for aligning LLMs often encounter challenges of reward hacking, where the approaches predominantly rely on directly mapping prompt-response pairs to scalar scores, which may inadvertently capture spurious correlations rather than authentic human preferences. In contrast, human evaluation employs a sophisticated process that initially weighs the relative importance o...

---

### 44. Functionality-Oriented LLM Merging on the Fisher--Rao Manifold

**Authors:** Jiayu Wang, Zuojun Ye, Wenpeng Yin

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04972v1)

**Summary:** Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean ble...

---

### 45. Mixture of Universal Experts: Scaling Virtual Width via Depth-Width Transformation

**Authors:** Yilong Chen, Naibin Gu, Junyuan Shang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04971v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04971v1)

**Summary:** Mixture-of-Experts (MoE) decouples model capacity from per-token computation, yet their scalability remains limited by the physical dimensions of depth and width. To overcome this, we propose Mixture of Universal Experts (MOUE),a MoE generalization introducing a novel scaling dimension: Virtual Width. In general, MoUE aims to reuse a universal layer-agnostic expert pool across layers, converting depth into virtual width under a fixed per-token activation budget. However, two challenges remain: a...

---

### 46. MPCEval: A Benchmark for Multi-Party Conversation Generation

**Authors:** Minxing Zhang, Yi Yang, Zhuofan Jia, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04969v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04969v1)

**Summary:** Multi-party conversation generation, such as smart reply and collaborative assistants, is an increasingly important capability of generative AI, yet its evaluation remains a critical bottleneck. Compared to two-party dialogue, multi-party settings introduce distinct challenges, including complex turn-taking, role-dependent speaker behavior, long-range conversational structure, and multiple equally valid continuations. Accordingly, we introduce MPCEval, a task-aware evaluation and benchmarking su...

---

### 47. When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger

**Authors:** Amirabbas Afzali, Myeongho Jeon, Maria Brbic

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04968v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04968v1)

**Summary:** Preference alignment is an essential step in adapting large language models (LLMs) to human values, but existing approaches typically depend on costly human annotations or large-scale API-based models. We explore whether a weak LLM can instead act as an effective annotator. We surprisingly find that selecting only a subset of a weak LLM's highly confident samples leads to substantially better performance than using full human annotations. Building on this insight, we propose Confidence-Weighted ...

---

### 48. Replaying pre-training data improves fine-tuning

**Authors:** Suhas Kotha, Percy Liang

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04964v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04964v1)

**Summary:** To obtain a language model for a target domain (e.g. math), the current paradigm is to pre-train on a vast amount of generic web text and then fine-tune on the relatively limited amount of target data. Typically, generic data is only mixed in during fine-tuning to prevent catastrophic forgetting of the generic domain. We surprisingly find that replaying the generic data during fine-tuning can actually improve performance on the (less related) target task. Concretely, in a controlled pre-training...

---

### 49. VisionPangu: A Compact and Fine-Grained Multimodal Assistant with 1.7B Parameters

**Authors:** Jiaxin Fan, Wenpo Song

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04957v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04957v1)

**Summary:** Large Multimodal Models (LMMs) have achieved strong performance in vision-language understanding, yet many existing approaches rely on large-scale architectures and coarse supervision, which limits their ability to generate detailed image captions. In this work, we present VisionPangu, a compact 1.7B-parameter multimodal model designed to improve detailed image captioning through efficient multimodal alignment and high-quality supervision. Our model combines an InternVL-derived vision encoder wi...

---

### 50. TimeWarp: Evaluating Web Agents by Revisiting the Past

**Authors:** Md Farhan Ishmam, Kenneth Marino

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04949v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04949v1)

**Summary:** The improvement of web agents on current benchmarks raises the question: Do today's agents perform just as well when the web changes? We introduce TimeWarp, a benchmark that emulates the evolving web using containerized environments that vary in UI, design, and layout. TimeWarp consists of three web environments, each with six UI versions spanning different eras of the internet, paired with a set of complex, realistic tasks requiring different forms of web navigation. Our experiments reveal web ...

---

## cs.CV

**50 papers**

### 1. Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups

**Authors:** Leif Van Holland, Domenic Zingsheim, Mana Takhsha, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05507v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05507v1)

**Summary:** High-quality 3D streaming from multiple cameras is crucial for immersive experiences in many AR/VR applications. The limited number of views - often due to real-time constraints - leads to missing information and incomplete surfaces in the rendered images. Existing approaches typically rely on simple heuristics for the hole filling, which can result in inconsistencies or visual artifacts. We propose to complete the missing textures using a novel, application-targeted inpainting method independen...

---

### 2. FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning

**Authors:** Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05506v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05506v1)

**Summary:** We introduce FaceCam, a system that generates video under customizable camera trajectories for monocular human portrait video input. Recent camera control approaches based on large video-generation models have shown promising progress but often exhibit geometric distortions and visual artifacts on portrait videos due to scale-ambiguous camera representations or 3D reconstruction errors. To overcome these limitations, we propose a face-tailored scale-aware representation for camera transformation...

---

### 3. Accelerating Text-to-Video Generation with Calibrated Sparse Attention

**Authors:** Shai Yehezkel, Shahar Yadin, Noam Elata, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05503v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05503v1)

**Summary:** Recent diffusion models enable high-quality video generation, but suffer from slow runtimes. The large transformer-based backbones used in these models are bottlenecked by spatiotemporal attention. In this paper, we identify that a significant fraction of token-to-token connections consistently yield negligible scores across various inputs, and their patterns often repeat across queries. Thus, the attention computation in these cases can be skipped with little to no effect on the result. This ob...

---

### 4. Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline

**Authors:** Guo Chen, Lidong Lu, Yicheng Liu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05484v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05484v1)

**Summary:** While datasets for video understanding have scaled to hour-long durations, they typically consist of densely concatenated clips that differ from natural, unscripted daily life. To bridge this gap, we introduce MM-Lifelong, a dataset designed for Multimodal Lifelong Understanding. Comprising 181.1 hours of footage, it is structured across Day, Week, and Month scales to capture varying temporal densities. Extensive evaluations reveal two critical failure modes in current paradigms: end-to-end MLLM...

---

### 5. Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields

**Authors:** Scout Jarman, Zigfried Hampel-Arias, Adra Carr, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05473v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05473v1)

**Summary:** Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the sc...

---

### 6. HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token

**Authors:** Sai Akhil Kogilathota, Sripadha Vallabha E G, Luzhe Sun, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05465v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05465v1)

**Summary:** Hallucinations remain a persistent challenge for vision-language models (VLMs), which often describe nonexistent objects or fabricate facts. Existing detection methods typically operate after text generation, making intervention both costly and untimely. We investigate whether hallucination risk can instead be predicted before any token is generated by probing a model's internal representations in a single forward pass. Across a diverse set of vision-language tasks and eight modern VLMs, includi...

---

### 7. EdgeDAM: Real-time Object Tracking for Mobile Devices

**Authors:** Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05463v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05463v1)

**Summary:** Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constraine...

---

### 8. Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes

**Authors:** Pengxiang Li, Joey Tsai, Hongwei Xue, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05454v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05454v1)

**Summary:** Diffusion Language Models (DLMs) promise highly parallel text generation, yet their practical inference speed is often bottlenecked by suboptimal decoding schedulers. Standard approaches rely on 'scattered acceptance'-committing high confidence tokens at disjoint positions throughout the sequence. This approach inadvertently fractures the Key-Value (KV) cache, destroys memory locality, and forces the model into costly, repeated repairs across unstable token boundaries. To resolve this, we presen...

---

### 9. RealWonder: Real-Time Physical Action-Conditioned Video Generation

**Authors:** Wei Liu, Ziyu Chen, Zizhang Li, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05449v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05449v1)

**Summary:** Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (o...

---

### 10. NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries

**Authors:** Kanon Amemiya, Daichi Yashima, Kei Katsumata, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05446v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05446v1)

**Summary:** We focus on the task of retrieving nail design images based on dense intent descriptions, which represent multi-layered user intent for nail designs. This is challenging because such descriptions specify unconstrained painted elements and pre-manufactured embellishments as well as visual characteristics, themes, and overall impressions. In addition to these descriptions, we assume that users provide palette queries by specifying zero or more colors via a color picker, enabling the expression of ...

---

### 11. Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model

**Authors:** Dongwon Kim, Gawon Seo, Jinsung Lee, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05438v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05438v1)

**Summary:** World models provide a powerful framework for simulating environment dynamics conditioned on actions or instructions, enabling downstream tasks such as action planning or policy learning. Recent approaches leverage world models as learned simulators, but its application to decision-time planning remains computationally prohibitive for real-time control. A key bottleneck lies in latent representations: conventional tokenizers encode each observation into hundreds of tokens, making planning both s...

---

### 12. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning

**Authors:** Ye-Chan Kim, SeungJu Cha, Si-Woo Kim, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05437v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05437v1)

**Summary:** Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically...

---

### 13. RelaxFlow: Text-Driven Amodal 3D Generation

**Authors:** Jiayin Zhu, Guoji Fu, Xiaolu Liu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05425v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05425v1)

**Summary:** Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. In this work, we formalize text-driven amodal 3D generation, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this en...

---

### 14. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis

**Authors:** Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05421v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05421v1)

**Summary:** Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair...

---

### 15. Video-based Locomotion Analysis for Fish Health Monitoring

**Authors:** Timon Palm, Clemens Seibold, Anna Hilsmann, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05407v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05407v1)

**Summary:** Monitoring the health conditions of fish is essential, as it enables the early detection of disease, safeguards animal welfare, and contributes to sustainable aquaculture practices. Physiological and pathological conditions of cultivated fish can be inferred by analyzing locomotion activities. In this paper, we present a system that estimates the locomotion activities from videos using multi object tracking. The core of our approach is a YOLOv11 detector embedded in a tracking-by-detection frame...

---

### 16. Loop Closure via Maximal Cliques in 3D LiDAR-Based SLAM

**Authors:** Javier Laserna, Saurabh Gupta, Oscar Martinez Mozos, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05397v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05397v1)

**Summary:** Reliable loop closure detection remains a critical challenge in 3D LiDAR-based SLAM, especially under sensor noise, environmental ambiguity, and viewpoint variation conditions. RANSAC is often used in the context of loop closures for geometric model fitting in the presence of outliers. However, this approach may fail, leading to map inconsistency. We introduce a novel deterministic algorithm, CliReg, for loop closure validation that replaces RANSAC verification with a maximal clique search over ...

---

### 17. Fusion-CAM: Integrating Gradient and Region-Based Class Activation Maps for Robust Visual Explanations

**Authors:** Hajar Dekdegue, Moncef Garouani, Josiane Mothe, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05386v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05386v1)

**Summary:** Interpreting the decision-making process of deep convolutional neural networks remains a central challenge in achieving trustworthy and transparent artificial intelligence. Explainable AI (XAI) techniques, particularly Class Activation Map (CAM) methods, are widely adopted to visualize the input regions influencing model predictions. Gradient-based approaches (e.g. Grad-CAM) provide highly discriminative, fine-grained details by computing gradients of class activations but often yield noisy and ...

---

### 18. ORMOT: A Dataset and Framework for Omnidirectional Referring Multi-Object Tracking

**Authors:** Sijia Chen, Zihan Zhou, Yanqiu Yu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05384v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05384v1)

**Summary:** Multi-Object Tracking (MOT) is a fundamental task in computer vision, aiming to track targets across video frames. Existing MOT methods perform well in general visual scenes, but face significant challenges and limitations when extended to visual-language settings. To bridge this gap, the task of Referring Multi-Object Tracking (RMOT) has recently been proposed, which aims to track objects that correspond to language descriptions. However, current RMOT methods are primarily developed on datasets...

---

### 19. OpenFrontier: General Navigation with Visual-Language Grounded Frontiers

**Authors:** Esteban Padilla, Boyang Sun, Marc Pollefeys, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05377v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05377v1)

**Summary:** Open-world navigation requires robots to make decisions in complex everyday environments while adapting to flexible task requirements. Conventional navigation approaches often rely on dense 3D reconstruction and hand-crafted goal metrics, which limits their generalization across tasks and environments. Recent advances in vision--language navigation (VLN) and vision--language--action (VLA) models enable end-to-end policies conditioned on natural language, but typically require interactive trainin...

---

### 20. Dark3R: Learning Structure from Motion in the Dark

**Authors:** Andrew Y Guo, Anagh Malik, SaiKiran Tedla, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05330v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05330v1)

**Summary:** We introduce Dark3R, a framework for structure from motion in the dark that operates directly on raw images with signal-to-noise ratios (SNRs) below $-4$ dB -- a regime where conventional feature- and learning-based methods break down. Our key insight is to adapt large-scale 3D foundation models to extreme low-light conditions through a teacher--student distillation process, enabling robust feature matching and camera pose estimation in low light. Dark3R requires no 3D supervision; it is trained...

---

### 21. Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers

**Authors:** Guandong Li

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05315v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05315v1)

**Summary:** Diffusion Transformers (DiTs) have emerged as the dominant architecture for high-quality image and video generation, yet their iterative denoising process incurs substantial computational cost during inference. Existing caching methods accelerate DiTs by reusing intermediate computations across timesteps, but they share a common limitation: treating the denoising process as uniform across time,depth, and feature dimensions. In this work, we identify three orthogonal axes of non-uniformity in DiT...

---

### 22. Fusion4CA: Boosting 3D Object Detection via Comprehensive Image Exploitation

**Authors:** Kang Luo, Xin Chen, Yangyi Xiao, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05305v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05305v1)

**Summary:** Nowadays, an increasing number of works fuse LiDAR and RGB data in the bird's-eye view (BEV) space for 3D object detection in autonomous driving systems. However, existing methods suffer from over-reliance on the LiDAR branch, with insufficient exploration of RGB information. To tackle this issue, we propose Fusion4CA, which is built upon the classic BEVFusion framework and dedicated to fully exploiting visual input with plug-and-play components. Specifically, a contrastive alignment module is d...

---

### 23. WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces

**Authors:** Sicheng Fan, Rui Wan, Yifei Leng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05295v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05295v1)

**Summary:** We introduce WebChain, the largest open-source dataset of human-annotated trajectories on real-world websites, designed to accelerate reproducible research in web agents. It contains 31,725 trajectories and 318k steps, featuring a core Triple Alignment of visual, structural, and action data to provide rich, multi-modal supervision. The data is collected via a scalable pipeline that ensures coverage of complex, high-value tasks often missed by synthetic methods. Leveraging this dataset, we propos...

---

### 24. Layer by layer, module by module: Choose both for optimal OOD probing of ViT

**Authors:** Ambroise Odonnat, Vasilii Feofanov, Laetitia Chapel, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05280v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05280v1)

**Summary:** Recent studies have observed that intermediate layers of foundation models often yield more discriminative representations than the final layer. While initially attributed to autoregressive pretraining, this phenomenon has also been identified in models trained via supervised and discriminative self-supervised objectives. In this paper, we conduct a comprehensive study to analyze the behavior of intermediate layers in pretrained vision transformers. Through extensive linear probing experiments a...

---

### 25. Wiki-R1: Incentivizing Multimodal Reasoning for Knowledge-based VQA via Data and Sampling Curriculum

**Authors:** Shan Ning, Longtian Qiu, Xuming He

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05256v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05256v1)

**Summary:** Knowledge-Based Visual Question Answering (KB-VQA) requires models to answer questions about an image by integrating external knowledge, posing significant challenges due to noisy retrieval and the structured, encyclopedic nature of the knowledge base. These characteristics create a distributional gap from pretrained multimodal large language models (MLLMs), making effective reasoning and domain adaptation difficult in the post-training stage. In this work, we propose \textit{Wiki-R1}, a data-ge...

---

### 26. CATNet: Collaborative Alignment and Transformation Network for Cooperative Perception

**Authors:** Gong Chen, Chaokun Zhang, Tao Tang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05255v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05255v1)

**Summary:** Cooperative perception significantly enhances scene understanding by integrating complementary information from diverse agents. However, existing research often overlooks critical challenges inherent in real-world multi-source data integration, specifically high temporal latency and multi-source noise. To address these practical limitations, we propose Collaborative Alignment and Transformation Network (CATNet), an adaptive compensation framework that resolves temporal latency and noise interfer...

---

### 27. ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders

**Authors:** Xavier Beltran-Urbano, Yiran Li, Xinglin Zeng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05247v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05247v1)

**Summary:** Arterial spin labeling (ASL) perfusion MRI allows direct quantification of regional cerebral blood flow (CBF) without exogenous contrast, enabling noninvasive measurements that can be repeated without constraints imposed by contrast injection. ASL is increasingly acquired in research studies and clinical MRI protocols. Building on successes in structural imaging, recent efforts have implemented deep learning based methods to improve image quality, enable automated quality control, and derive rob...

---

### 28. Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems

**Authors:** Serkan Ergun, Tobias Mitterer, Hubert Zangl

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05230v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05230v1)

**Summary:** The increasing demand for sustainable textile recycling requires robust automation solutions capable of handling deformable garments and detecting foreign objects in cluttered environments. This work presents a digital twin driven robotic sorting system that integrates grasp prediction, multi modal perception, and semantic reasoning for real world textile classification. A dual arm robotic cell equipped with RGBD sensing, capacitive tactile feedback, and collision-aware motion planning autonomou...

---

### 29. SPyCer: Semi-Supervised Physics-Guided Contextual Attention for Near-Surface Air Temperature Estimation from Satellite Imagery

**Authors:** Sofiane Bouaziz, Adel Hafiane, Raphael Canals, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05219v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05219v1)

**Summary:** Modern Earth observation relies on satellites to capture detailed surface properties. Yet, many phenomena that affect humans and ecosystems unfold in the atmosphere close to the surface. Near-ground sensors provide accurate measurements of certain environmental characteristics, such as near-surface air temperature (NSAT). However, they remain sparse and unevenly distributed, limiting their ability to provide continuous spatial measurements. To bridge this gap, we introduce SPyCer, a semi-supervi...

---

### 30. Semantic Class Distribution Learning for Debiasing Semi-Supervised Medical Image Segmentation

**Authors:** Yingxue Su, Yiheng Zhong, Keying Zhu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05202v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05202v1)

**Summary:** Medical image segmentation is critical for computer-aided diagnosis. However, dense pixel-level annotation is time-consuming and expensive, and medical datasets often exhibit severe class imbalance. Such imbalance causes minority structures to be overwhelmed by dominant classes in feature representations, hindering the learning of discriminative features and making reliable segmentation particularly challenging. To address this, we propose the Semantic Class Distribution Learning (SCDL) framewor...

---

### 31. Logi-PAR: Logic-Infused Patient Activity Recognition via Differentiable Rule

**Authors:** Muhammad Zarar, MingZheng Zhang, Xiaowang Zhang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05184v1)

**Summary:** Patient Activity Recognition (PAR) in clinical settings uses activity data to improve safety and quality of care. Although significant progress has been made, current models mainly identify which activity is occurring. They often spatially compose sub-sparse visual cues using global and local attention mechanisms, yet only learn logically implicit patterns due to their neural-pipeline. Advancing clinical safety requires methods that can infer why a set of visual cues implies a risk, and how thes...

---

### 32. Mario: Multimodal Graph Reasoning with Large Language Models

**Authors:** Yuanfu Sun, Kang Li, Pengkang Guo, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05181v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05181v1)

**Summary:** Recent advances in large language models (LLMs) have opened new avenues for multimodal reasoning. Yet, most existing methods still rely on pretrained vision-language models (VLMs) to encode image-text pairs in isolation, ignoring the relational structure that real-world multimodal data naturally form. This motivates reasoning on multimodal graphs (MMGs), where each node has textual and visual attributes and edges provide structural cues. Enabling LLM-based reasoning on such heterogeneous multimo...

---

### 33. Generic Camera Calibration using Blurry Images

**Authors:** Zezhun Shi

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05159v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05159v1)

**Summary:** Camera calibration is the foundation of 3D vision. Generic camera calibration can yield more accurate results than parametric cam era calibration. However, calibrating a generic camera model using printed calibration boards requires far more images than parametric calibration, making motion blur practically unavoidable for individual users. As a f irst attempt to address this problem, we draw on geometric constraints and a local parametric illumination model to simultaneously estimate feature lo...

---

### 34. The Impact of Preprocessing Methods on Racial Encoding and Model Robustness in CXR Diagnosis

**Authors:** Dishantkumar Sutariya, Eike Petersen

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05157v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05157v1)

**Summary:** Deep learning models can identify racial identity with high accuracy from chest X-ray (CXR) recordings. Thus, there is widespread concern about the potential for racial shortcut learning, where a model inadvertently learns to systematically bias its diagnostic predictions as a function of racial identity. Such racial biases threaten healthcare equity and model reliability, as models may systematically misdiagnose certain demographic groups. Since racial shortcuts are diffuse - non-localized and ...

---

### 35. SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction

**Authors:** Ningjing Fan, Yiqun Wang

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05152v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05152v1)

**Summary:** In recent years, 3D Gaussian splatting (3DGS) has achieved remarkable progress in novel view synthesis. However, accurately reconstructing glossy surfaces under complex illumination remains challenging, particularly in scenes with strong specular reflections and multi-surface interreflections. To address this issue, we propose SSR-GS, a specular reflection modeling framework for glossy surface reconstruction. Specifically, we introduce a prefiltered Mip-Cubemap to model direct specular reflectio...

---

### 36. Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models

**Authors:** Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05147v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05147v1)

**Summary:** Current research on Vision-Language-Action (VLA) models predominantly focuses on enhancing generalization through established reasoning techniques. While effective, these improvements invariably increase computational complexity and inference latency. Furthermore, these mechanisms are typically applied indiscriminately, resulting in the inefficient allocation of resources for trivial tasks while simultaneously failing to provide the uncertainty estimation necessary to prevent catastrophic failur...

---

### 37. SRasP: Self-Reorientation Adversarial Style Perturbation for Cross-Domain Few-Shot Learning

**Authors:** Wenqian Li, Pengfei Fang, Hui Xue

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05135v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05135v1)

**Summary:** Cross-Domain Few-Shot Learning (CD-FSL) aims to transfer knowledge from a seen source domain to unseen target domains, serving as a key benchmark for evaluating the robustness and transferability of models. Existing style-based perturbation methods mitigate domain shift but often suffer from gradient instability and convergence to sharp minima.To address these limitations, we propose a novel crop-global style perturbation network, termed Self-Reorientation Adversarial \underline{S}tyle \underlin...

---

### 38. UniPAR: A Unified Framework for Pedestrian Attribute Recognition

**Authors:** Minghe Xu, Rouying Wu, Jiarui Xu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05114v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05114v1)

**Summary:** Pedestrian Attribute Recognition is a foundational computer vision task that provides essential support for downstream applications, including person retrieval in video surveillance and intelligent retail analytics. However, existing research is frequently constrained by the ``one-model-per-dataset" paradigm and struggles to handle significant discrepancies across domains in terms of modalities, attribute definitions, and environmental scenarios. To address these challenges, we propose UniPAR, a...

---

### 39. BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity

**Authors:** Iman Nematollahi, Jose Francisco Villena-Ossa, Alina Moter, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05110v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05110v1)

**Summary:** Machine learning models of cellular interaction dynamics hold promise for understanding cell behavior. Natural killer (NK) cell cytotoxicity is a prominent example of such interaction dynamics and is commonly studied using time-resolved multi-channel fluorescence microscopy. Although tumor cell death events can be annotated at single frames, NK cytotoxic outcome emerges over time from cellular interactions and cannot be reliably inferred from frame-wise classification alone. We introduce BLINK, ...

---

### 40. Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search

**Authors:** Zongfang Liu, Shengkun Tang, Zongliang Wu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05105v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05105v1)

**Summary:** Diffusion models have achieved remarkable success in high-fidelity image generation but remain computationally demanding due to their multi-step denoising process and large model sizes. Although prior work improves efficiency either by reducing sampling steps or by compressing model parameters, existing structured pruning approaches still struggle to balance real acceleration and image quality preservation. In particular, prior methods such as MosaicDiff rely on heuristic, manually tuned stage-w...

---

### 41. GEM-TFL: Bridging Weak and Full Supervision for Forgery Localization through EM-Guided Decomposition and Temporal Refinement

**Authors:** Xiaodong Zhu, Yuanming Zheng, Suting Wang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05095v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05095v1)

**Summary:** Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within videos or audio streams, providing interpretable evidence for multimedia forensics and security. While most existing TFL methods rely on dense frame-level labels in a fully supervised manner, Weakly Supervised TFL (WS-TFL) reduces labeling cost by learning only from binary video-level labels. However, current WS-TFL approaches suffer from mismatched training and inference objectives, limited supervision fr...

---

### 42. Axiomatic On-Manifold Shapley via Optimal Generative Flows

**Authors:** Cenwei Zhang, Lin Zhu, Manxi Lin, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05093v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05093v1)

**Summary:** Shapley-based attribution is critical for post-hoc XAI but suffers from off-manifold artifacts due to heuristic baselines. While generative methods attempt to address this, they often introduce geometric inefficiency and discretization drift. We propose a formal theory of on-manifold Aumann-Shapley attributions driven by optimal generative flows. We prove a representation theorem establishing the gradient line integral as the unique functional satisfying efficiency and geometric axioms, notably ...

---

### 43. Orthogonal Spatial-temporal Distributional Transfer for 4D Generation

**Authors:** Wei Liu, Shengqiong Wu, Bobo Li, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05081v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05081v1)

**Summary:** In the AIGC era, generating high-quality 4D content has garnered increasing research attention. Unfortunately, current 4D synthesis research is severely constrained by the lack of large-scale 4D datasets, preventing models from adequately learning the critical spatial-temporal features necessary for high-quality 4D generation, thus hindering progress in this domain. To combat this, we propose a novel framework that transfers rich spatial priors from existing 3D diffusion models and temporal prio...

---

### 44. MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer

**Authors:** Juntong Fang, Zequn Chen, Weiqi Zhang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05078v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05078v1)

**Summary:** Reconstructing dynamic 4D scenes remains challenging due to the presence of moving objects that corrupt camera pose estimation. Existing optimization methods alleviate this issue with additional supervision, but they are mostly computationally expensive and impractical in real-time applications. To address these limitations, we propose MoRe, a feedforward 4D reconstruction network that efficiently recovers dynamic 3D scenes from monocular videos. Built upon a strong static reconstruction backbon...

---

### 45. UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark

**Authors:** Yanlin Li, Minghui Guo, Kaiwen Zhang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05075v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05075v1)

**Summary:** In real-world multimodal applications, systems usually need to comprehend arbitrarily combined and interleaved multimodal inputs from users, while also generating outputs in any interleaved multimedia form. This capability defines the goal of any-to-any interleaved multimodal learning under a unified paradigm of understanding and generation, posing new challenges and opportunities for advancing Multimodal Large Language Models (MLLMs). To foster and benchmark this capability, this paper introduc...

---

### 46. MI-DETR: A Strong Baseline for Moving Infrared Small Target Detection with Bio-Inspired Motion Integration

**Authors:** Nian Liu, Jin Gao, Shubo Lin, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05071v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05071v1)

**Summary:** Infrared small target detection (ISTD) is challenging because tiny, low-contrast targets are easily obscured by complex and dynamic backgrounds. Conventional multi-frame approaches typically learn motion implicitly through deep neural networks, often requiring additional motion supervision or explicit alignment modules. We propose Motion Integration DETR (MI-DETR), a bio-inspired dual-pathway detector that processes one infrared frame per time step while explicitly modeling motion. First, a reti...

---

### 47. A 360-degree Multi-camera System for Blue Emergency Light Detection Using Color Attention RT-DETR and the ABLDataset

**Authors:** Francisco Vacalebri-Lloret, Lucas Banchero, Jose J. Lopez, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05058v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05058v1)

**Summary:** This study presents an advanced system for detecting blue lights on emergency vehicles, developed using ABLDataset, a curated dataset that includes images of European emergency vehicles under various climatic and geographic conditions. The system employs a configuration of four fisheye cameras, each with a 180-degree horizontal field of view, mounted on the sides of the vehicle. A calibration process enables the azimuthal localization of the detections. Additionally, a comparative analysis of ma...

---

### 48. CLIP-driven Zero-shot Learning with Ambiguous Labels

**Authors:** Jinfu Fan, Jiangnan Li, Xiaowen Yan, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05053v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05053v1)

**Summary:** Zero-shot learning (ZSL) aims to recognize unseen classes by leveraging semantic information from seen classes, but most existing methods assume accurate class labels for training instances. However, in real-world scenarios, noise and ambiguous labels can significantly reduce the performance of ZSL. To address this, we propose a new CLIP-driven partial label zero-shot learning (CLIP-PZSL) framework to handle label ambiguity. First, we use CLIP to extract instance and label features. Then, a sema...

---

### 49. CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection

**Authors:** Zhaonian Kuang, Rui Ding, Haotian Wang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05042v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05042v1)

**Summary:** Multi-camera 3D object detection (MC3D) has attracted increasing attention with the growing deployment of multi-sensor physical agents, such as robots and autonomous vehicles. However, MC3D models still struggle to generalize to unseen platforms with new multi-camera configurations. Current solutions simply employ a meta-camera for unified representation but lack comprehensive consideration. In this paper, we revisit this issue and identify that the devil lies in spatial prior discrepancies acro...

---

### 50. Exploiting Intermediate Reconstructions in Optical Coherence Tomography for Test-Time Adaption of Medical Image Segmentation

**Authors:** Thomas Pinetz, Veit Hucke, Hrvoje Bogunovic

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05041v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05041v1)

**Summary:** Primary health care frequently relies on low-cost imaging devices, which are commonly used for screening purposes. To ensure accurate diagnosis, these systems depend on advanced reconstruction algorithms designed to approximate the performance of high-quality counterparts. Such algorithms typically employ iterative reconstruction methods that incorporate domain-specific prior knowledge. However, downstream task performance is generally assessed using only the final reconstructed image, thereby d...

---

## cs.LG

**50 papers**

### 1. RoboPocket: Improve Robot Policies Instantly with Your Phone

**Authors:** Junjie Fang, Wendi Chen, Han Xue, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05504v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05504v1)

**Summary:** Scaling imitation learning is fundamentally constrained by the efficiency of data collection. While handheld interfaces have emerged as a scalable solution for in-the-wild data acquisition, they predominantly operate in an open-loop manner: operators blindly collect demonstrations without knowing the underlying policy's weaknesses, leading to inefficient coverage of critical state distributions. Conversely, interactive methods like DAgger effectively address covariate shift but rely on physical ...

---

### 2. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

**Authors:** Zeju Qiu, Lixin Liu, Adrian Weller, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05500v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05500v1)

**Summary:** Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix mu...

---

### 3. Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels

**Authors:** Khai Nguyen, Petros Ellinas, Anvita Bhagavathula, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05495v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05495v1)

**Summary:** To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collec...

---

### 4. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**Authors:** Helena Casademunt, Bartosz Cywiński, Khoi Tran, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05494v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05494v1)

**Summary:** Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese develo...

---

### 5. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

**Authors:** Siddharth Boppana, Annabel Ma, Max Loeffler, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05488v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05488v1)

**Summary:** We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able t...

---

### 6. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis

**Authors:** Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05483v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05483v1)

**Summary:** Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragment...

---

### 7. Thermodynamic Response Functions in Singular Bayesian Models

**Authors:** Sean Plummer

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05480v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05480v1)

**Summary:** Singular statistical models-including mixtures, matrix factorization, and neural networks-violate regular asymptotics due to parameter non-identifiability and degenerate Fisher geometry. Although singular learning theory characterizes marginal likelihood behavior through invariants such as the real log canonical threshold and singular fluctuation, these quantities remain difficult to interpret operationally. At the same time, widely used criteria such as WAIC and WBIC appear disconnected from un...

---

### 8. Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement

**Authors:** Priyanshi Singh, Krishna Bhatia

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05468v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05468v1)

**Summary:** Real-time reconstruction of conditional quantum states from continuous measurement records is a fundamental requirement for quantum feedback control, yet standard stochastic master equation (SME) solvers require exact model specification, known system parameters, and are sensitive to parameter mismatch. While neural sequence models can fit these stochastic dynamics, the unconstrained predictors can violate physicality such as positivity or trace constraints, leading to unstable rollouts and unph...

---

### 9. Latent Wasserstein Adversarial Imitation Learning

**Authors:** Siqi Yang, Kai Yan, Alexander G. Schwing, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05440v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05440v1)

**Summary:** Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein dis...

---

### 10. On-Policy Self-Distillation for Reasoning Compression

**Authors:** Hejian Sang, Yuanda Xu, Zhengze Zhou, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05433v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05433v1)

**Summary:** Reasoning models think out loud, but much of what they say is noise. We introduce OPSDC (On-Policy Self-Distillation for Reasoning Compression), a method that teaches models to reason more concisely by   distilling their own concise behavior back into themselves. The entire approach reduces to one idea: condition the same model on a "be concise" instruction to obtain teacher logits, and minimize per-token   reverse KL on the student's own rollouts. No ground-truth answers, no token budgets, no d...

---

### 11. Ensembling Language Models with Sequential Monte Carlo

**Authors:** Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05432v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05432v1)

**Summary:** Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token prob...

---

### 12. An interpretable prototype parts-based neural network for medical tabular data

**Authors:** Jacek Karolczak, Jerzy Stefanowski

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05423v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05423v1)

**Summary:** The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainabl...

---

### 13. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis

**Authors:** Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05421v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05421v1)

**Summary:** Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair...

---

### 14. Harnessing Synthetic Data from Generative AI for Statistical Inference

**Authors:** Ahmad Abdel-Azim, Ruoyu Wang, Xihong Lin

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05396v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05396v1)

**Summary:** The emergence of generative AI models has dramatically expanded the availability and use of synthetic data across scientific, industrial, and policy domains. While these developments open new possibilities for data analysis, they also raise fundamental statistical questions about when synthetic data can be used in a valid, reliable, and principled manner. This paper reviews the current landscape of synthetic data generation and use from a statistical perspective, with the goal of clarifying the ...

---

### 15. On the Necessity of Learnable Sheaf Laplacians

**Authors:** Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05395v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05395v1)

**Summary:** Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations convergi...

---

### 16. Robust Node Affinities via Jaccard-Biased Random Walks and Rank Aggregation

**Authors:** Bastian Pfeifer, Michael G. Schimek

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05375v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05375v1)

**Summary:** Estimating node similarity is a fundamental task in network analysis and graph-based machine learning, with applications in clustering, community detection, classification, and recommendation. We propose TopKGraphs, a method based on start-node-anchored random walks that bias transitions toward nodes with structurally similar neighborhoods, measured via Jaccard similarity. Rather than computing stationary distributions, walks are treated as stochastic neighborhood samplers, producing partial nod...

---

### 17. Embedded Inter-Subject Variability in Adversarial Learning for Inertial Sensor-Based Human Activity Recognition

**Authors:** Francisco M. Calatrava-Nicolás, Shoko Miyauchi, Vitor Fortes Rey, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05371v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05371v1)

**Summary:** This paper addresses the problem of Human Activity Recognition (HAR) using data from wearable inertial sensors. An important challenge in HAR is the model's generalization capabilities to new unseen individuals due to inter-subject variability, i.e., the same activity is performed differently by different individuals. To address this problem, we propose a novel deep adversarial framework that integrates the concept of inter-subject variability in the adversarial task, thereby encouraging subject...

---

### 18. Learning Causal Structure of Time Series using Best Order Score Search

**Authors:** Irene Gema Castillo Mansilla, Urmi Ninad

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05370v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05370v1)

**Summary:** Causal structure learning from observational data is central to many scientific and policy domains, but the time series setting common to many disciplines poses several challenges due to temporal dependence. In this paper we focus on score-based causal discovery for multivariate time series and introduce TS-BOSS, a time series extension of the recently proposed Best Order Score Search (BOSS) (Andrews et al. 2023). TS-BOSS performs a permutation-based search over dynamic Bayesian network structur...

---

### 19. InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context

**Authors:** Xin Teng, Canyu Zhang, Shaoyi Zheng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05353v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05353v1)

**Summary:** Retrieval-augmented generation (RAG) for long-context question answering is bottlenecked by inference-time prefilling over large retrieved contexts. A common strategy is to precompute key-value (KV) caches for individual documents and selectively recompute a small subset of tokens to restore global causal dependencies, but existing methods rely on heuristics or representation discrepancies without modeling whether selected tokens can effectively influence generation. We cast selective KV recompu...

---

### 20. Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs

**Authors:** Haoyu Zhou, Ping Xue, Hao Zhang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05343v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05343v1)

**Summary:** Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GA...

---

### 21. On the Statistical Optimality of Optimal Decision Trees

**Authors:** Zineng Xu, Subhroshekhar Ghosh, Yan Shuo Tan

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05340v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05340v1)

**Summary:** While globally optimal empirical risk minimization (ERM) decision trees have become computationally feasible and empirically successful, rigorous theoretical guarantees for their statistical performance remain limited. In this work, we develop a comprehensive statistical theory for ERM trees under random design in both high-dimensional regression and classification. We first establish sharp oracle inequalities that bound the excess risk of the ERM estimator relative to the best possible approxim...

---

### 22. Bayes with No Shame: Admissibility Geometries of Predictive Inference

**Authors:** Nicholas G. Polson, Daniel Zantedeschi

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05335v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05335v1)

**Summary:** Four distinct admissibility geometries govern sequential and distribution-free inference: Blackwell risk dominance over convex risk sets, anytime-valid admissibility within the nonnegative supermartingale cone, marginal coverage validity over exchangeable prediction sets, and Cesàro approachability (CAA) admissibility, which reaches the risk-set boundary via approachability-style arguments rather than explicit priors. We prove a criterion separation theorem: the four classes of admissible proced...

---

### 23. FairFinGAN: Fairness-aware Synthetic Financial Data Generation

**Authors:** Tai Le Quy, Dung Nguyen Tuan, Trung Nguyen Thanh, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05327v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05327v1)

**Summary:** Financial datasets often suffer from bias that can lead to unfair decision-making in automated systems. In this work, we propose FairFinGAN, a WGAN-based framework designed to generate synthetic financial data while mitigating bias with respect to the protected attribute. Our approach incorporates fairness constraints directly into the training process through a classifier, ensuring that the synthetic data is both fair and preserves utility for downstream predictive tasks. We evaluate our propos...

---

### 24. GALACTIC: Global and Local Agnostic Counterfactuals for Time-series Clustering

**Authors:** Christos Fragkathoulas, Eleni Psaroudaki, Themis Palpanas, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05318v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05318v1)

**Summary:** Time-series clustering is a fundamental tool for pattern discovery, yet existing explainability methods, primarily based on feature attribution or metadata, fail to identify the transitions that move an instance across cluster boundaries. While Counterfactual Explanations (CEs) identify the minimal temporal perturbations required to alter the prediction of a model, they have been mostly confined to supervised settings. This paper introduces GALACTIC, the first unified framework to bridge local a...

---

### 25. How important are the genes to explain the outcome - the asymmetric Shapley value as an honest importance metric for high-dimensional features

**Authors:** Mark A. van de Wiel, Jeroen Goedhart, Martin Jullum, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05317v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05317v1)

**Summary:** In clinical prediction settings the importance of a high-dimensional feature like genomics is often assessed by evaluating the change in predictive performance when adding it to a set of traditional clinical variables. This approach is questionable, because it does not account for collinearity nor known directionality of dependencies between variables. We suggest to use asymmetric Shapley values as a more suitable alternative to quantify feature importance in the context of a mixed-dimensional p...

---

### 26. WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

**Authors:** Luca Della Libera, Cem Subakan, Mirco Ravanelli

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05299v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05299v1)

**Summary:** Large language models show that simple autoregressive training can yield scalable and coherent generation, but extending this paradigm to speech remains challenging due to the entanglement of semantic and acoustic information. Most existing speech language models rely on text supervision, hierarchical token streams, or complex hybrid architectures, departing from the single-stream generative pretraining paradigm that has proven effective in text. In this work, we introduce WavSLM, a speech langu...

---

### 27. Latent Policy Steering through One-Step Flow Policies

**Authors:** Hokyun Im, Andrey Kolobov, Jianlong Fu, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05296v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05296v1)

**Summary:** Offline reinforcement learning (RL) allows robots to learn from offline datasets without risky exploration. Yet, offline RL's performance often hinges on a brittle trade-off between (1) return maximization, which can push policies outside the dataset support, and (2) behavioral constraints, which typically require sensitive hyperparameter tuning. Latent steering offers a structural way to stay within the dataset support during RL, but existing offline adaptations commonly approximate action valu...

---

### 28. Knowledge Divergence and the Value of Debate for Scalable Oversight

**Authors:** Robin Young

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05293v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05293v1)

**Summary:** AI safety via debate and reinforcement learning from AI feedback (RLAIF) are both proposed methods for scalable oversight of advanced AI systems, yet no formal framework relates them or characterizes when debate offers an advantage. We analyze this by parameterizing debate's value through the geometry of knowledge divergence between debating models. Using principal angles between models' representation subspaces, we prove that the debate advantage admits an exact closed form. When models share i...

---

### 29. Bayesian Supervised Causal Clustering

**Authors:** Luwei Wang, Nazir Lone, Sohan Seth

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05288v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05288v1)

**Summary:** Finding patient subgroups with similar characteristics is crucial for personalized decision-making in various disciplines such as healthcare and policy evaluation. While most existing approaches rely on unsupervised clustering methods, there is a growing trend toward using supervised clustering methods that identify operationalizable subgroups in the context of a specific outcome of interest. We propose Bayesian Supervised Causal Clustering (BSCC), with treatment effect as outcome to guide the c...

---

### 30. Layer by layer, module by module: Choose both for optimal OOD probing of ViT

**Authors:** Ambroise Odonnat, Vasilii Feofanov, Laetitia Chapel, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05280v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05280v1)

**Summary:** Recent studies have observed that intermediate layers of foundation models often yield more discriminative representations than the final layer. While initially attributed to autoregressive pretraining, this phenomenon has also been identified in models trained via supervised and discriminative self-supervised objectives. In this paper, we conduct a comprehensive study to analyze the behavior of intermediate layers in pretrained vision transformers. Through extensive linear probing experiments a...

---

### 31. Whispering to a Blackbox: Bootstrapping Frozen OCR with Visual Prompts

**Authors:** Samandar Samandarov, Nazirjon Ismoiljonov, Abdullah Sattorov, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05276v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05276v1)

**Summary:** In the landscape of modern machine learning, frozen pre-trained models provide stability and efficiency but often underperform on specific tasks due to mismatched data distributions. This paper introduces the Whisperer, a novel visual prompting framework that learns diffusion-based preprocessors to adapt inputs in pixel space, effectively "whispering" enhancements to frozen downstream models like EasyOCR. By framing the process as behavioral cloning of stochastically discovered improvement polic...

---

### 32. Beyond Word Error Rate: Auditing the Diversity Tax in Speech Recognition through Dataset Cartography

**Authors:** Ting-Hui Cheng, Line H. Clemmensen, Sneha Das

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05267v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05267v1)

**Summary:** Automatic speech recognition (ASR) systems are predominantly evaluated using the Word Error Rate (WER). However, raw token-level metrics fail to capture semantic fidelity and routinely obscures the `diversity tax', the disproportionate burden on marginalized and atypical speaker due to systematic recognition failures. In this paper, we explore the limitations of relying solely on lexical counts by systematically evaluating a broader class of non-linear and semantic metrics. To enable rigorous mo...

---

### 33. A Behaviour-Aware Federated Forecasting Framework for Distributed Stand-Alone Wind Turbines

**Authors:** Bowen Li, Xiufeng Liu, Maria Sinziiana Astefanoaei

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05263v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05263v1)

**Summary:** Accurate short-term wind power forecasting is essential for grid dispatch and market operations, yet centralising turbine data raises privacy, cost, and heterogeneity concerns. We propose a two-stage federated learning framework that first clusters turbines by long-term behavioural statistics using Double Roulette Selection (DRS) initialisation with recursive Auto-split refinement, and then trains cluster-specific LSTM models via FedAvg. Experiments on 400 stand-alone turbines in Denmark show th...

---

### 34. Recursive Inference Machines for Neural Reasoning

**Authors:** Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05234v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05234v1)

**Summary:** Neural reasoners such as Tiny Recursive Models (TRMs) solve complex problems by combining neural backbones with specialized inference schemes. Such inference schemes have been a central component of stochastic reasoning systems, where inference rules are applied to a stochastic model to derive answers to complex queries. In this work, we bridge these two paradigms by introducing Recursive Inference Machines (RIMs), a neural reasoning framework that explicitly incorporates recursive inference mec...

---

### 35. SlideSparse: Fast and Flexible (2N-2):2N Structured Sparsity

**Authors:** Hanyong Shao, Yingbo Hao, Ting Song, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05232v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05232v1)

**Summary:** NVIDIA's 2:4 Sparse Tensor Cores deliver 2x throughput but demand strict 50% pruning -- a ratio that collapses LLM reasoning accuracy (Qwen3: 54% to 15%). Milder $(2N-2):2N$ patterns (e.g., 6:8, 25% pruning) preserve accuracy yet receive no hardware support, falling back to dense execution without any benefit from sparsity. We present SlideSparse, the first system to unlock Sparse Tensor Core acceleration for the $(2N-2):2N$ model family on commodity GPUs. Our Sliding Window Decomposition recons...

---

### 36. Boosting ASR Robustness via Test-Time Reinforcement Learning with Audio-Text Semantic Rewards

**Authors:** Linghan Fang, Tianxin Xie, Li Liu

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05231v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05231v1)

**Summary:** Recently, Automatic Speech Recognition (ASR) systems (e.g., Whisper) have achieved remarkable accuracy improvements but remain highly sensitive to real-world unseen data (data with large distribution shifts), including noisy environments and diverse accents. To address this issue, test-time adaptation (TTA) has shown great potential in improving the model adaptability at inference time without ground-truth labels, and existing TTA methods often rely on pseudo-labeling or entropy minimization. Ho...

---

### 37. The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology

**Authors:** Alper Yıldırım

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05228v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05228v1)

**Summary:** Mechanistic interpretability typically relies on post-hoc analysis of trained networks. We instead adopt an interventional approach: testing hypotheses a priori by modifying architectural topology to observe training dynamics. We study grokking - delayed generalization in Transformers trained on cyclic modular addition (Zp) - investigating if specific architectural degrees of freedom prolong the memorization phase.   We identify two independent structural factors in standard Transformers: unboun...

---

### 38. Learning Optimal Individualized Decision Rules with Conditional Demographic Parity

**Authors:** Wenhai Cui, Wen Su, Donglin Zeng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05226v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05226v1)

**Summary:** Individualized decision rules (IDRs) have become increasingly prevalent in societal applications such as personalized marketing, healthcare, and public policy design. However, a critical ethical concern arises from the potential discriminatory effects of IDRs trained on biased data. These algorithms may disproportionately harm individuals from minority subgroups defined by sensitive attributes like gender, race, or language. To address this issue, we propose a novel framework that incorporates d...

---

### 39. KARL: Knowledge Agents via Reinforcement Learning

**Authors:** Jonathan D. Chang, Andrew Drozdov, Shubham Toshniwal, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05218v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05218v1)

**Summary:** We present a system for training enterprise search agents via reinforcement learning that achieves state-of-the-art performance across a diverse suite of hard-to-verify agentic search tasks. Our work makes four core contributions. First, we introduce KARLBench, a multi-capability evaluation suite spanning six distinct search regimes, including constraint-driven entity search, cross-document report synthesis, tabular numerical reasoning, exhaustive entity retrieval, procedural reasoning over tech...

---

### 40. Early Warning of Intraoperative Adverse Events via Transformer-Driven Multi-Label Learning

**Authors:** Xueyao Wang, Xiuding Cai, Honglin Shang, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05212v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05212v1)

**Summary:** Early warning of intraoperative adverse events plays a vital role in reducing surgical risk and improving patient safety. While deep learning has shown promise in predicting the single adverse event, several key challenges remain: overlooking adverse event dependencies, underutilizing heterogeneous clinical data, and suffering from the class imbalance inherent in medical datasets. To address these issues, we construct the first Multi-label Adverse Events dataset (MuAE) for intraoperative adverse...

---

### 41. Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding

**Authors:** Ofir Ben Shoham

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05210v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05210v1)

**Summary:** Speculative decoding accelerates inference for Large Language Models by using a lightweight draft model to propose candidate tokens that are verified in parallel by a larger target model. Prior work shows that the draft model often dominates speculative decoding latency, since it generates tokens sequentially and incurs high cost from its language modeling head as vocabulary size grows. This exposes a fundamental trade-off in draft model design: larger vocabularies improve token coverage and agr...

---

### 42. Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation

**Authors:** Yize Wu, Ke Gao, Ling Li, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05204v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05204v1)

**Summary:** Low-Rank Adaptation (LoRA) is a widely adopted parameter-efficient method for fine-tuning Large Langauge Models. It updates the weight matrix as $W=W_0+sBA$, where $W_0$ is the original frozen weight, $s$ is a scaling factor and $A$,$B$ are trainable low-rank matrices. Despite its robust empirical effectiveness, the theoretical foundations of LoRA remain insufficiently understood, particularly with respect to feature learning stability. In this paper, we first establish that, LoRA can, in princi...

---

### 43. Towards a data-scale independent regulariser for robust sparse identification of non-linear dynamics

**Authors:** Jay Raut, Daniel N. Wilke, Stephan Schmidt

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05201v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05201v1)

**Summary:** Data normalisation, a common and often necessary preprocessing step in engineering and scientific applications, can severely distort the discovery of governing equations by magnitudebased sparse regression methods. This issue is particularly acute for the Sparse Identification of Nonlinear Dynamics (SINDy) framework, where the core assumption of sparsity is undermined by the interaction between data scaling and measurement noise. The resulting discovered models can be dense, uninterpretable, and...

---

### 44. Incentive Aware AI Regulations: A Credal Characterisation

**Authors:** Anurag Singh, Julian Rodemann, Rajeev Verma, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05175v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05175v1)

**Summary:** While high-stakes ML applications demand strict regulations, strategic ML providers often evade them to lower development costs. To address this challenge, we cast AI regulation as a mechanism design problem under uncertainty and introduce regulation mechanisms: a framework that maps empirical evidence from models to a license for some market share. The providers can select from a set of licenses, effectively forcing them to bet on their model's ability to fulfil regulation. We aim at regulation...

---

### 45. Trainable Bitwise Soft Quantization for Input Feature Compression

**Authors:** Karsten Schrödter, Jan Stenkamp, Nina Herrmann, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05172v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05172v1)

**Summary:** The growing demand for machine learning applications in the context of the Internet of Things calls for new approaches to optimize the use of limited compute and memory resources. Despite significant progress that has been made w.r.t. reducing model sizes and improving efficiency, many applications still require remote servers to provide the required resources. However, such approaches rely on transmitting data from edge devices to remote servers, which may not always be feasible due to bandwidt...

---

### 46. A Geometry-Adaptive Deep Variational Framework for Phase Discovery in the Landau-Brazovskii Model

**Authors:** Yuchen Xie, Jianyuan Yin, Lei Zhang

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05161v1)

**Summary:** The discovery of ordered structures in pattern-forming systems, such as the Landau-Brazovskii (LB) model, is often limited by the sensitivity of numerical solvers to the prescribed computational domain size. Incompatible domains induce artificial stress, frequently trapping the system in high-energy metastable configurations. To resolve this issue, we propose a Geometry-Adaptive Deep Variational Framework (GeoDVF) that jointly optimizes the infinite-dimensional order parameter, which is paramete...

---

### 47. Balancing Privacy-Quality-Efficiency in Federated Learning through Round-Based Interleaving of Protection Techniques

**Authors:** Yenan Wang, Carla Fabiana Chiasserini, Elad Michael Schiller

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05158v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05158v1)

**Summary:** In federated learning (FL), balancing privacy protection, learning quality, and efficiency remains a challenge. Privacy protection mechanisms, such as Differential Privacy (DP), degrade learning quality, or, as in the case of Homomorphic Encryption (HE), incur substantial system overhead. To address this, we propose Alt-FL, a privacy-preserving FL framework that combines DP, HE, and synthetic data via a novel round-based interleaving strategy. Alt-FL introduces three new methods, Privacy Interle...

---

### 48. The Impact of Preprocessing Methods on Racial Encoding and Model Robustness in CXR Diagnosis

**Authors:** Dishantkumar Sutariya, Eike Petersen

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05157v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05157v1)

**Summary:** Deep learning models can identify racial identity with high accuracy from chest X-ray (CXR) recordings. Thus, there is widespread concern about the potential for racial shortcut learning, where a model inadvertently learns to systematically bias its diagnostic predictions as a function of racial identity. Such racial biases threaten healthcare equity and model reliability, as models may systematically misdiagnose certain demographic groups. Since racial shortcuts are diffuse - non-localized and ...

---

### 49. Federated Causal Discovery Across Heterogeneous Datasets under Latent Confounding

**Authors:** Maximilian Hahn, Alina Zajak, Dominik Heider, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05149v1)

**Summary:** Causal discovery across multiple datasets is often constrained by data privacy regulations and cross-site heterogeneity, limiting the use of conventional methods that require a single, centralized dataset. To address these challenges, we introduce fedCI, a federated conditional independence test that rigorously handles heterogeneous datasets with non-identical sets of variables, site-specific effects, and mixed variable types, including continuous, ordinal, binary, and categorical variables. At ...

---

### 50. Feature Resemblance: On the Theoretical Understanding of Analogical Reasoning in Transformers

**Authors:** Ruichen Xu, Wenjing Yan, Ying-Jun Angela Zhang

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05143v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05143v1)

**Summary:** Understanding reasoning in large language models is complicated by evaluations that conflate multiple reasoning types. We isolate analogical reasoning (inferring shared properties between entities based on known similarities) and analyze its emergence in transformers. We theoretically prove three key results: (1) Joint training on similarity and attribution premises enables analogical reasoning through aligned representations; (2) Sequential training succeeds only when similarity structure is le...

---

## cs.NE

**50 papers**

### 1. VietNormalizer: An Open-Source, Dependency-Free Python Library for Vietnamese Text Normalization in TTS and NLP Applications

**Authors:** Hung Vu Nguyen, Loan Do, Thanh Ngoc Nguyen, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04145v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04145v1)

**Summary:** We present VietNormalizer1, an open-source, zero-dependency Python library for Vietnamese text normalization targeting Text-to-Speech (TTS) and Natural Language Processing (NLP) applications. Vietnamese text normalization is a critical yet underserved preprocessing step: real-world Vietnamese text is densely populated with non-standard words (NSWs), including numbers, dates, times, currency amounts, percentages, acronyms, and foreign-language terms, all of which must be converted to fully pronou...

---

### 2. Lyapunov Stability of Stochastic Vector Optimization: Theory and Numerical Implementation

**Authors:** Thiago Santos, Sebastiao Xavier

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04095v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04095v1)

**Summary:** The use of stochastic differential equations in multi-objective optimization has been limited, in practice, by two persistent gaps: incomplete stability analyses and the absence of accessible implementations. We revisit a drift--diffusion model for unconstrained vector optimization in which the drift is induced by a common descent direction and the diffusion term preserves exploratory behavior. The main theoretical contribution is a self-contained Lyapunov analysis establishing global existence,...

---

### 3. An Adaptive KKT-Based Indicator for Convergence Assessment in Multi-Objective Optimization

**Authors:** Thiago Santos, Sebastiao Xavier

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04053v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04053v1)

**Summary:** Performance indicators are essential tools for assessing the convergence behavior of multi-objective optimization algorithms, particularly when the true Pareto front is   unknown or difficult to approximate. Classical reference-based metrics such as   hypervolume and inverted generational distance are widely used, but may suffer from   scalability limitations and sensitivity to parameter choices in many-objective scenarios.   Indicators derived from Karush--Kuhn--Tucker (KKT) optimality conditio...

---

### 4. Joint Hardware-Workload Co-Optimization for In-Memory Computing Accelerators

**Authors:** Olga Krestinskaya, Mohammed E. Fouda, Ahmed Eltawil, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03880v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03880v1)

**Summary:** Software-hardware co-design is essential for optimizing in-memory computing (IMC) hardware accelerators for neural networks. However, most existing optimization frameworks target a single workload, leading to highly specialized hardware designs that do not generalize well across models and applications. In contrast, practical deployment scenarios require a single IMC platform that can efficiently support multiple neural network workloads. This work presents a joint hardware-workload co-optimizat...

---

### 5. Empirical Evaluation of No Free Lunch Violations in Permutation-Based Optimization

**Authors:** Grzegorz Sroka

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03613v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03613v1)

**Summary:** The No Free Lunch (NFL) theorem guarantees equal average performance only under uniform sampling of a function space closed under permutation (c.u.p.). We ask when this averaging ceases to reflect what benchmarking actually reports. We study an iterative-search setting with sampling without replacement, where algorithms differ only in evaluation order. Binary objectives allow exhaustive evaluation in the fully enumerable case, and efficiency is defined by the first time the global minimum is rea...

---

### 6. mlx-snn: Spiking Neural Networks on Apple Silicon via MLX

**Authors:** Jiahao Qin

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03529v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03529v1)

**Summary:** We introduce mlx-snn, the first spiking neural network (SNN) library built natively on Apple's MLX framework. As SNN research grows rapidly, all major libraries -- snnTorch, Norse, SpikingJelly, Lava -- target PyTorch or custom backends, leaving Apple Silicon users without a native option. mlx-snn provides six neuron models (LIF, IF, Izhikevich, Adaptive LIF, Synaptic, Alpha), four surrogate gradient functions, four spike encoding methods (including an EEG-specific encoder), and a complete backp...

---

### 7. Stringology-Based Motif Discovery from EEG Signals: an ADHD Case Study

**Authors:** Anat Dahan, Samah Ghazawi

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03476v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03476v1)

**Summary:** We propose a novel computational framework for analyzing electroencephalography (EEG) time series using methods from stringology, the study of efficient algorithms for string processing, to systematically identify and characterize recurrent temporal patterns in neural signals. The primary aim is to introduce quantitative measures to understand neural signal dynamics, with the present findings serving as a proof-of-concept. The framework adapts order-preserving matching (OPM) and Cartesian tree m...

---

### 8. A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks

**Authors:** Simone Betteti, Giacomo Baggio, Sandro Zampieri

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03201v2) | 📄 [PDF](https://arxiv.org/pdf/2603.03201v2)

**Summary:** Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoni...

---

### 9. Enhancing Physics-Informed Neural Networks with Domain-aware Fourier Features: Towards Improved Performance and Interpretable Results

**Authors:** Alberto Miño Calero, Luis Salamanca, Konstantinos E. Tatsis

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.02948v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02948v1)

**Summary:** Physics-Informed Neural Networks (PINNs) incorporate physics into neural networks by embedding partial differential equations (PDEs) into their loss function. Despite their success in learning the underlying physics, PINN models remain difficult to train and interpret. In this work, a novel modeling approach is proposed, which relies on the use of Domain-aware Fourier Features (DaFFs) for the positional encoding of the input space. These features encapsulate all the domain-specific characteristi...

---

### 10. From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors

**Authors:** Qi Huang, Furong Ye, Ananta Shahane, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.02792v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02792v1)

**Summary:** Large Language Models (LLMs) have already been widely adopted for automated algorithm design, demonstrating strong abilities in generating and evolving algorithms across various fields. Existing work has largely focused on examining their effectiveness in solving specific problems, with search strategies primarily guided by adaptive prompt designs. In this paper, through investigating the token-wise attribution of the prompts to LLM-generated algorithmic codes, we show that providing high-qualit...

---

### 11. ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution

**Authors:** Liu Yang, Zeyu Nie, Andrew Liu, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.02510v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02510v1)

**Summary:** The transition from sequential to parallel computing is essential for modern high-performance applications but is hindered by the steep learning curve of concurrent programming. This challenge is magnified for irregular data structures (such as sparse graphs, unbalanced trees, and non-uniform meshes) where static scheduling fails and data dependencies are unpredictable. Current Large Language Models (LLMs) often fail catastrophically on these tasks, generating code plagued by subtle race conditi...

---

### 12. Uniform-in-time concentration in two-layer neural networks via transportation inequalities

**Authors:** Arnaud Guillin, Boris Nectoux, Paul Stos

**Published:** 2026-03-02

🔗 [Paper](http://arxiv.org/abs/2603.01842v1) | 📄 [PDF](https://arxiv.org/pdf/2603.01842v1)

**Summary:** We quantify, uniformly over time and with high probability, the discrepancy between the predictions of a two-layer neural network trained by stochastic gradient descent (SGD) and their mean-field limit, for quadratic loss and ridge regularization. As a key ingredient, we establish T p transportation inequalities (p $\in$ {1, 2}) for the law of the SGD parameters, with explicit constants independent of the iteration index. We then prove uniform-in-time concentration of the empirical parameter mea...

---

### 13. PARWiS: Winner determination under shoestring budgets using active pairwise comparisons

**Authors:** Shailendra Bhandari

**Published:** 2026-03-01

🔗 [Paper](http://arxiv.org/abs/2603.01171v1) | 📄 [PDF](https://arxiv.org/pdf/2603.01171v1)

**Summary:** Determining a winner among a set of items using active pairwise comparisons under a limited budget is a challenging problem in preference-based learning. The goal of this study is to implement and evaluate the PARWiS algorithm, which shows spectral ranking and disruptive pair selection to identify the best item under shoestring budgets. This work have extended the PARWiS with a contextual variant (Contextual PARWiS) and a reinforcement learning-based variant (RL PARWiS), comparing them against b...

---

### 14. A Gauge Theory of Superposition: Toward a Sheaf-Theoretic Atlas of Neural Representations

**Authors:** Hossein Javidnia

**Published:** 2026-02-28

🔗 [Paper](http://arxiv.org/abs/2603.00824v1) | 📄 [PDF](https://arxiv.org/pdf/2603.00824v1)

**Summary:** We develop a discrete gauge-theoretic framework for superposition in large language models (LLMs) that replaces the single-global-dictionary premise with a sheaf-theoretic atlas of local semantic charts. Contexts are clustered into a stratified context complex; each chart carries a local feature space and a local information-geometric metric (Fisher/Gauss--Newton) identifying predictively consequential feature interactions. This yields a Fisher-weighted interference energy and three measurable o...

---

### 15. Reward-Modulated Local Learning in Spiking Encoders: Controlled Benchmarks with STDP and Hybrid Rate Readouts

**Authors:** Debjyoti Chakraborty

**Published:** 2026-02-28

🔗 [Paper](http://arxiv.org/abs/2603.00710v1) | 📄 [PDF](https://arxiv.org/pdf/2603.00710v1)

**Summary:** This paper presents a controlled empirical study of biologically motivated local learning for handwritten digit recognition. We evaluate an STDP-inspired competitive proxy and a practical hybrid benchmark built on the same spiking population encoder. The proxy is motivated by leaky integrate-and-fire E/I circuit models with three-factor delayed reward modulation. The hybrid update is local in pre x post rates but uses supervised labels and no timing-based credit assignment. On sklearn digits, fi...

---

### 16. All Mutation Rates $c/n$ for the $(1+1)$ Evolutionary Algorithm

**Authors:** Andrew James Kelley

**Published:** 2026-02-27

🔗 [Paper](http://arxiv.org/abs/2602.23573v1) | 📄 [PDF](https://arxiv.org/pdf/2602.23573v1)

**Summary:** For every real number $c \geq 1$ and for all $\varepsilon > 0$, there is a fitness function $f : \{0,1\}^n \to \mathbb{R}$ for which the optimal mutation rate for the $(1+1)$ evolutionary algorithm on $f$, denoted $p_n$, satisfies $p_n \approx c/n$ in that $|np_n - c| < \varepsilon$. In other words, the set of all $c \geq 1$ for which the mutation rate $c/n$ is optimal for the $(1+1)$ EA is dense in the interval $[1, \infty)$. To show this, a fitness function is introduced which is called HillPa...

---

### 17. EvoX: Meta-Evolution for Automated Discovery

**Authors:** Shu Liu, Shubham Agarwal, Monishwaran Maheswaran, et al.

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.23413v1) | 📄 [PDF](https://arxiv.org/pdf/2602.23413v1)

**Summary:** Recent work such as AlphaEvolve has shown that combining LLM-driven optimization with evolutionary search can effectively improve programs, prompts, and algorithms across domains. In this paradigm, previously evaluated solutions are reused to guide the model toward new candidate solutions. Crucially, the effectiveness of this evolution process depends on the search strategy: how prior solutions are selected and varied to generate new candidates. However, most existing methods rely on fixed searc...

---

### 18. A Novel Evolutionary Method for Automated Skull-Face Overlay in Computer-Aided Craniofacial Superimposition

**Authors:** Práxedes Martínez-Moreno, Andrea Valsecchi, Pablo Mesejo, et al.

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2603.00170v2) | 📄 [PDF](https://arxiv.org/pdf/2603.00170v2)

**Summary:** Craniofacial Superimposition is a forensic technique for identifying skeletal remains by comparing a post-mortem skull with ante-mortem facial photographs. A critical step in this process is Skull-Face Overlay (SFO). This stage involves aligning a 3D skull model with a 2D facial image, typically guided by cranial and facial landmarks' correspondence. However, its accuracy is undermined by individual variability in soft-tissue thickness, introducing significant uncertainty into the overlay. This ...

---

### 19. On De-Individuated Neurons: Continuous Symmetries Enable Dynamic Topologies

**Authors:** George Bird

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.23405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.23405v1)

**Summary:** This paper introduces a novel methodology for dynamic networks by leveraging a new symmetry-principled class of primitives, isotropic activation functions. This approach enables real-time neuronal growth and shrinkage of the architectures in response to task demand. This is made possible by network structural changes that are invariant under symmetry reparameterisations, leaving the computation identical under neurogenesis and well approximated under neurodegeneration. This is undertaken by leve...

---

### 20. Communication-Guided Multi-Mutation Differential Evolution for Crop Model Calibration

**Authors:** Sakshi Aggarwal, Mudasir Ganaie, Mukesh Saini

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.22804v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22804v1)

**Summary:** In this paper, we propose a multi-mutation optimization algorithm, Differential Evolution with Multi-Mutation Operator-Guided Communication (DE-MMOGC), implemented to improve the performance and convergence abilities of standard differential evolution in uncertain environments. DE-MMOGC introduces a communication-guided scheme integrated with multiple mutation operators to encourage exploration and avoid premature convergence. Along with this, it includes a dynamic operator selection mechanism t...

---

### 21. Applying a Random-Key Optimizer on Mixed Integer Programs

**Authors:** Antonio A. Chaves, Mauricio G. C. Resende, Carise E. Schmidt, et al.

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.22173v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22173v1)

**Summary:** Mixed-Integer Programs (MIPs) are NP-hard optimization models that arise in a broad range of decision-making applications, including finance, logistics, energy systems, and network design. Although modern commercial solvers have achieved remarkable progress and perform effectively on many small- and medium-sized instances, their performance often degrades when confronted with large-cale or highly constrained formulations. This paper explores the use of the Random-Key Optimizer (RKO) framework as...

---

### 22. Stream Neural Networks: Epoch-Free Learning with Persistent Temporal State

**Authors:** Amama Pathan

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.22152v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22152v1)

**Summary:** Most contemporary neural learning systems rely on epoch-based optimization and repeated access to historical data, implicitly assuming reversible computation. In contrast, real-world environments often present information as irreversible streams, where inputs cannot be replayed or revisited. Under such conditions, conventional architectures degrade into reactive filters lacking long-horizon coherence. This paper introduces Stream Neural Networks (StNN), an execution paradigm designed for irrever...

---

### 23. Outpatient Appointment Scheduling Optimization with a Genetic Algorithm Approach

**Authors:** Ana Rodrigues, Rui Rego

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.21995v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21995v1)

**Summary:** The optimization of complex medical appointment scheduling remains a significant operational challenge in multi-center healthcare environments, where clinical safety protocols and patient logistics must be reconciled. This study proposes and evaluates a Genetic Algorithm (GA) framework designed to automate the scheduling of multiple medical acts while adhering to rigorous inter-procedural incompatibility rules. Using a synthetic dataset encompassing 50 medical acts across four healthcare facilit...

---

### 24. Pulse-Driven Neural Architecture: Learnable Oscillatory Dynamics for Robust Continuous-Time Sequence Processing

**Authors:** Paras Sharma

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2603.00153v1) | 📄 [PDF](https://arxiv.org/pdf/2603.00153v1)

**Summary:** We introduce PDNA (Pulse-Driven Neural Architecture), a method for augmenting continuous-time recurrent networks with learnable oscillatory dynamics that maintain internal state evolution independently of external input. Built on Closed-form Continuous-time (CfC) networks, PDNA adds two components: (1) a pulse module that generates structured oscillations $A \cdot \sin(ωt + \varphi(h))$ with learnable frequencies and state-dependent phase, and (2) a self-attend module that applies recurrent self...

---

### 25. Survey on Neural Routing Solvers

**Authors:** Yunpeng Ba, Xi Lin, Changliang Zhou, et al.

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.21761v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21761v1)

**Summary:** Neural routing solvers (NRSs) that leverage deep learning to tackle vehicle routing problems have demonstrated notable potential for practical applications. By learning implicit heuristic rules from data, NRSs replace the handcrafted counterparts in classic heuristic frameworks, thereby reducing reliance on costly manual design and trial-and-error adjustments. This survey makes two main contributions: (1) The heuristic nature of NRSs is highlighted, and existing NRSs are reviewed from the perspe...

---

### 26. Code World Models for Parameter Control in Evolutionary Algorithms

**Authors:** Camilo Chacón Sartori, Guillem Rodríguez Corominas

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.22260v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22260v1)

**Summary:** Can an LLM learn how an optimizer behaves -- and use that knowledge to control it? We extend Code World Models (CWMs), LLM-synthesized Python programs that predict environment dynamics, from deterministic games to stochastic combinatorial optimization. Given suboptimal trajectories of $(1{+}1)$-$\text{RLS}_k$, the LLM synthesizes a simulator of the optimizer's dynamics; greedy planning over this simulator then selects the mutation strength $k$ at each step. On \lo{} and \onemax{}, CWM-greedy per...

---

### 27. Body-Reservoir Governance in Repeated Games: Embodied Decision-Making, Dynamic Sentinel Adaptation, and Complexity-Regularized Optimization

**Authors:** Yuki Nakamura

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20846v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20846v1)

**Summary:** Standard game theory explains cooperation in repeated games through conditional strategies such as Tit-for-Tat (TfT), but these require continuous computation that imposes physical costs on embodied agents. We propose a three-layer Body-Reservoir Governance (BRG) architecture: (1) a body reservoir (echo state network) whose $d$-dimensional state performs implicit inference over interaction history, serving as both decision-maker and anomaly detector, (2) a cognitive filter providing costly strat...

---

### 28. AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization

**Authors:** Mert Cemri, Shubham Agrawal, Akshat Gupta, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20133v1)

**Summary:** The paradigm of automated program generation is shifting from one-shot generation to inference-time search, where Large Language Models (LLMs) function as semantic mutation operators within evolutionary loops. While effective, these systems are currently governed by static schedules that fail to account for the non-stationary dynamics of the search process. This rigidity results in substantial computational waste, as resources are indiscriminately allocated to stagnating populations while promis...

---

### 29. Linear Reservoir: A Diagonalization-Based Optimization

**Authors:** Romain de Coudenhove, Yannis Bendi-Ouis, Anthony Strock, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19802v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19802v1)

**Summary:** We introduce a diagonalization-based optimization for Linear Echo State Networks (ESNs) that reduces the per-step computational complexity of reservoir state updates from O(N^2) to O(N). By reformulating reservoir dynamics in the eigenbasis of the recurrent matrix, the recurrent update becomes a set of independent element-wise operations, eliminating the matrix multiplication. We further propose three methods to use our optimization depending on the situation: (i) Eigenbasis Weight Transformatio...

---

### 30. Unsupervised Anomaly Detection in NSL-KDD Using $β$-VAE: A Latent Space and Reconstruction Error Approach

**Authors:** Dylan Baptiste, Ramla Saddem, Alexandre Philippot, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19785v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19785v1)

**Summary:** As Operational Technology increasingly integrates with Information Technology, the need for Intrusion Detection Systems becomes more important. This paper explores an unsupervised approach to anomaly detection in network traffic using $β$-Variational Autoencoders on the NSL-KDD dataset. We investigate two methods: leveraging the latent space structure by measuring distances from test samples to the training data projections, and using the reconstruction error as a conventional anomaly detection ...

---

### 31. Partial Soft-Matching Distance for Neural Representational Comparison with Partial Unit Correspondence

**Authors:** Chaitanya Kapoor, Alex H. Williams, Meenakshi Khosla

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19331v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19331v1)

**Summary:** Representational similarity metrics typically force all units to be matched, making them susceptible to noise and outliers common in neural representations. We extend the soft-matching distance to a partial optimal transport setting that allows some neurons to remain unmatched, yielding rotation-sensitive but robust correspondences. This partial soft-matching distance provides theoretical advantages -- relaxing strict mass conservation while maintaining interpretable transport costs -- and pract...

---

### 32. CORVET: A CORDIC-Powered, Resource-Frugal Mixed-Precision Vector Processing Engine for High-Throughput AIoT applications

**Authors:** Sonu Kumar, Mohd Faisal Khan, Mukul Lokhande, et al.

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19268v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19268v1)

**Summary:** This brief presents a runtime-adaptive, performance-enhanced vector engine featuring a low-resource, iterative CORDIC-based MAC unit for edge AI acceleration. The proposed design enables dynamic reconfiguration between approximate and accurate modes, exploiting the latency-accuracy trade-off for a wide range of workloads. Its resource-efficient approach further enables up to 4x throughput improvement within the same hardware resources by leveraging vectorised, time-multiplexed execution and flex...

---

### 33. DGPO: RL-Steered Graph Diffusion for Neural Architecture Generation

**Authors:** Aleksei Liuliakov, Luca Hermes, Barbara Hammer

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19261v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19261v1)

**Summary:** Reinforcement learning fine-tuning has proven effective for steering generative diffusion models toward desired properties in image and molecular domains. Graph diffusion models have similarly been applied to combinatorial structure generation, including neural architecture search (NAS). However, neural architectures are directed acyclic graphs (DAGs) where edge direction encodes functional semantics such as data flow-information that existing graph diffusion methods, designed for undirected str...

---

### 34. Alternating Bi-Objective Optimization for Explainable Neuro-Fuzzy Systems

**Authors:** Qusai Khaled, Uzay Kaymak, Laura Genga

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19253v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19253v1)

**Summary:** Fuzzy systems show strong potential in explainable AI due to their rule-based architecture and linguistic variables. Existing approaches navigate the accuracy-explainability trade-off either through evolutionary multi-objective optimization (MOO), which is computationally expensive, or gradient-based scalarization, which cannot recover non-convex Pareto regions. We propose X-ANFIS, an alternating bi-objective gradient-based optimization scheme for explainable adaptive neuro-fuzzy inference syste...

---

### 35. All Constant Mutation Rates for the $(1+1)$ Evolutionary Algorithm

**Authors:** Andrew James Kelley

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.18989v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18989v1)

**Summary:** For every mutation rate $p \in (0, 1)$, and for all $\varepsilon > 0$, there is a fitness function $f : \{0,1\}^n \to \mathbb{R}$ with a unique maximum for which the optimal mutation rate for the $(1+1)$ evolutionary algorithm on $f$ is in $(p-\varepsilon, p+\varepsilon)$. In other words, the set of optimal mutation rates for the $(1+1)$ EA is dense in the interval $[0, 1]$. To show that, this paper introduces DistantSteppingStones, a fitness function which consists of large plateaus separated b...

---

### 36. Modularity is the Bedrock of Natural and Artificial Intelligence

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18960v1)

**Summary:** The remarkable performance of modern AI systems has been driven by unprecedented scales of data, computation, and energy -- far exceeding the resources required by human intelligence. This disparity highlights the need for new guiding principles and motivates drawing inspiration from the fundamental organizational principles of brain computation. Among these principles, modularity has been shown to be critical for supporting the efficient learning and strong generalization abilities consistently...

---

### 37. Toward Manifest Relationality in Transformers via Symmetry Reduction

**Authors:** J. François, L. Ravera

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18948v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18948v1)

**Summary:** Transformer models contain substantial internal redundancy arising from coordinate-dependent representations and continuous symmetries, in model space and in head space, respectively. While recent approaches address this by explicitly breaking symmetry, we propose a complementary framework based on symmetry reduction. We reformulate representations, attention mechanisms, and optimization dynamics in terms of invariant relational quantities, eliminating redundant degrees of freedom by constructio...

---

### 38. Robustness of Deep ReLU Networks to Misclassification of High-Dimensional Data

**Authors:** Věra Kůrková

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18674v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18674v1)

**Summary:** We present a theoretical study of the robustness of parameterized networks to random input perturbations. Specifically, we analyze local robustness at a given network input by quantifying the probability that a small additive random perturbation of the input leads to misclassification. For deep networks with rectified linear units, we derive lower bounds on local robustness in terms of the input dimensionality and the total number of network units.

---

### 39. Musical Training, but not Mere Exposure to Music, Drives the Emergence of Chroma Equivalence in Artificial Neural Networks

**Authors:** Lukas Grasse, Matthew S. Tata

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18635v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18635v1)

**Summary:** Pitch is a fundamental aspect of auditory perception. Pitch perception is commonly described across two perceptual dimensions: pitch height is the sense that tones with varying frequencies seem to be higher or lower, and chroma equivalence is the cyclical similarity of notes octaves, corresponding to a doubling of fundamental frequency. Existing research is divided on whether chroma equivalence is a learned percept that varies according to musical experience and culture, or is an innate percept ...

---

### 40. Flexi-NeurA: A Configurable Neuromorphic Accelerator with Adaptive Bit-Precision Exploration for Edge SNNs

**Authors:** Mohammad Farahani, Mohammad Rasoul Roshanshah, Saeed Safari

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18140v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18140v1)

**Summary:** Neuromorphic accelerators promise unparalleled energy efficiency and computational density for spiking neural networks (SNNs), especially in edge intelligence applications. However, most existing platforms exhibit rigid architectures with limited configurability, restricting their adaptability to heterogeneous workloads and diverse design objectives. To address these limitations, we present Flexi-NeurA -- a parameterizable neuromorphic accelerator (core) that unifies configurability, flexibility...

---

### 41. PINEAPPLE: Physics-Informed Neuro-Evolution Algorithm for Prognostic Parameter Inference in Lithium-Ion Battery Electrodes

**Authors:** Karkulali Pugalenthi, Jian Cheng Wong, Qizheng Yang, et al.

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18042v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18042v1)

**Summary:** Accurate, real-time, yet non-destructive estimation of internal states in lithium-ion batteries is critical for predicting degradation, optimizing usage strategies, and extending operational lifespan. Here, we introduce PINEAPPLE (Physics-Informed Neuro-Evolution Algorithm for Prognostic Parameter inference in Lithium-ion battery Electrodes), a novel framework that integrates physics-informed neural networks (PINNs) with an evolutionary search algorithm to enable rapid, scalable, and interpretab...

---

### 42. Learning under noisy supervision is governed by a feedback-truth gap

**Authors:** Elan Schonfeld, Elias Wisnia

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16829v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16829v1)

**Summary:** When feedback is absorbed faster than task structure can be evaluated, the learner will favor feedback over truth. A two-timescale model shows this feedback-truth gap is inevitable whenever the two rates differ and vanishes only when they match. We test this prediction across neural networks trained with noisy labels (30 datasets, 2,700 runs), human probabilistic reversal learning (N = 292), and human reward/punishment learning with concurrent EEG (N = 25). In each system, truth is defined opera...

---

### 43. Parallelizable Neural Turing Machines

**Authors:** Gabriel Faria, Arnaldo Candido Junior

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.18508v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18508v1)

**Summary:** We introduce a parallelizable simplification of Neural Turing Machine (NTM), referred to as P-NTM, which redesigns the core operations of the original architecture to enable efficient scan-based parallel execution. We evaluate the proposed architecture on a synthetic benchmark of algorithmic problems involving state tracking, memorization, and basic arithmetic, solved via autoregressive decoding. We compare it against a revisited stable implementation of the standard NTM, as well as conventional...

---

### 44. Fine-Pruning: A Biologically Inspired Algorithm for Personalization of Machine Learning Models

**Authors:** Joseph Bingham, Saman Zonouz, Dvir Aran

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18507v1)

**Summary:** Neural networks have long strived to emulate the learning capabilities of the human brain. While deep neural networks (DNNs) draw inspiration from the brain in neuron design, their training methods diverge from biological foundations. Backpropagation, the primary training method for DNNs, requires substantial computational resources and fully labeled datasets, presenting major bottlenecks in development and application. This work demonstrates that by returning to biomimicry, specifically mimicki...

---

### 45. End-user validation of BRIGHT with custom-developed graphical user interface applied to cervical cancer brachytherapy

**Authors:** Leah R. M. Dickhoff, Ellen M. Kerkhof, Heloisa H. Deuzeman, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16321v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16321v1)

**Summary:** Multi-objective optimisation using BRIGHT has proven insightful and effective in prostate cancer brachytherapy treatment planning. BRachytherapy via artificially Intelligent GOMEA-Heuristic based Treatment planning (BRIGHT) generates multiple treatment plans, each with a different trade-off between tumour coverage and organs-at-risk sparing. BRIGHT was recently extended to cervical cancer brachytherapy. In this study, we present a novel, custom-developed graphical user interface (GUI) that enabl...

---

### 46. Evolutionary Context Search for Automated Skill Acquisition

**Authors:** Qi Sun, Stefan Nielsen, Rio Yokota, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16113v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16113v1)

**Summary:** Large Language Models cannot reliably acquire new knowledge post-deployment -- even when relevant text resources exist, models fail to transform them into actionable knowledge without retraining. Retrieval-Augmented Generation attempts to bridge this gap by surfacing relevant documents at inference time, yet similarity-based retrieval often fails to identify context that actually improves task performance. We introduce Evolutionary Context Search (ECS), an evolutionary method that searches conte...

---

### 47. Heuristic Search as Language-Guided Program Optimization

**Authors:** Mingxin Yu, Ruixiao Yang, Chuchu Fan

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16038v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16038v1)

**Summary:** Large Language Models (LLMs) have advanced Automated Heuristic Design (AHD) in combinatorial optimization (CO) in the past few years. However, existing discovery pipelines often require extensive manual trial-and-error or reliance on domain expertise to adapt to new or complex problems. This stems from tightly coupled internal mechanisms that limit systematic improvement of the LLM-driven design process. To address this challenge, we propose a structured framework for LLM-driven AHD that explici...

---

### 48. B-DENSE: Branching For Dense Ensemble Network Learning

**Authors:** Cherish Puniani, Tushar Kumar, Arnav Bendre, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15971v1)

**Summary:** Inspired by non-equilibrium thermodynamics, diffusion models have achieved state-of-the-art performance in generative modeling. However, their iterative sampling nature results in high inference latency. While recent distillation techniques accelerate sampling, they discard intermediate trajectory steps. This sparse supervision leads to a loss of structural information and introduces significant discretization errors. To mitigate this, we propose B-DENSE, a novel framework that leverages multi-b...

---

### 49. Evolutionary Systems Thinking -- From Equilibrium Models to Open-Ended Adaptive Dynamics

**Authors:** Dan Adler

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15957v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15957v1)

**Summary:** Complex change is often described as "evolutionary" in economics, policy, and technology, yet most system dynamics models remain constrained to fixed state spaces and equilibrium-seeking behavior. This paper argues that evolutionary dynamics should be treated as a core system-thinking problem rather than as a biological metaphor. We introduce Stability-Driven Assembly (SDA) as a minimal, non-equilibrium framework in which stochastic interactions combined with differential persistence generate en...

---

### 50. SEval-NAS: A Search-Agnostic Evaluation for Neural Architecture Search

**Authors:** Atah Nuh Mih, Jianzhou Wang, Truong Thanh Hung Nguyen, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2603.00099v1) | 📄 [PDF](https://arxiv.org/pdf/2603.00099v1)

**Summary:** Neural architecture search (NAS) automates the discovery of neural networks that meet specified criteria, yet its evaluation procedures are often hardcoded, limiting the ability to introduce new metrics. This issue is especially pronounced in hardware-aware NAS, where objectives depend on target devices such as edge hardware. To address this limitation, we propose SEval-NAS, a metric-evaluation mechanism that converts architectures to strings, embeds them as vectors, and predicts performance met...

---

## q-bio.NC

**50 papers**

### 1. The Spatial and Temporal Resolution of Motor Intention in Multi-Target Prediction

**Authors:** Marie Dominique Schmidt, Ioannis Iossifidis

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05418v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05418v1)

**Summary:** Reaching for grasping, and manipulating objects are essential motor functions in everyday life. Decoding human motor intentions is a central challenge for rehabilitation and assistive technologies. This study focuses on predicting intentions by inferring movement direction and target location from multichannel electromyography (EMG) signals, and investigating how spatially and temporally accurate such information can be detected relative to movement onset. We present a computational pipeline tha...

---

### 2. Neural geometry in the human hippocampus enables generalization across spatial position and gaze

**Authors:** Assia Chericoni, Chad Diao, Xinyuan Yan, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04747v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04747v1)

**Summary:** Hippocampal neurons track positions of self, others, and gaze direction. However, it is unclear how their respective neural codes differ enough to avoid confusion while allowing for abstraction. We recorded from populations of hippocampal neurons while participants performed a joystick-controlled virtual prey pursuit task involving multiple moving agents. We found that neurons have mixed selective responses that map positions of self, prey, and predator, as well as gaze. Their codes occupied mos...

---

### 3. Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation

**Authors:** Zafeirios Fountas, Adnan Oomerjee, Haitham Bou-Ammar, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04688v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04688v1)

**Summary:** Standard accounts of memory consolidation emphasise the stabilisation of stored representations, but struggle to explain representational drift, semanticisation, or the necessity of offline replay. Here we propose that high-capacity neocortical networks optimise stored representations for generalisation by reducing complexity via predictive forgetting, i.e. the selective retention of experienced information that predicts future outcomes or experience. We show that predictive forgetting formally ...

---

### 4. INTENSE: Detecting and disentangling neuronal selectivity in calcium imaging data

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04622v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04622v1)

**Summary:** Neurons encode information about the environment through their activity. As animals explore the environment, neurons rapidly acquire selectivity for distinct features of the external world; characterizing how these selectivity patterns emerge, reorganize, and overlap is key to linking neural activity to behavior and cognition. Calcium imaging in freely behaving animals can record large neuronal populations, but quantifying neuron-behavior selectivity directly from continuous fluorescence is chal...

---

### 5. Topological Origin of the Diversity of Timescales in Recurrent Neural Circuits

**Authors:** Marco Zenari, Luca Taffarello, Luca Mazzucato, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04149v1)

**Summary:** Structural and functional heterogeneity are hallmarks of cortical circuits, from broad degree distributions in the mouse connectome to diverse intrinsic neuronal timescales. Yet a mechanistic link between connectivity heterogeneity and functional diversity is lacking. To bridge this gap, we introduce a random recurrent network in which connectivity is generated by a configuration model with tunable degree heterogeneity and synaptic weights exhibiting varying levels of correlation. Using generati...

---

### 6. Two-phase quadratic integrate-and-fire neurons: Exact low-dimensional description for ensembles of finite-voltage neurons

**Authors:** Rok Cestnik

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03870v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03870v1)

**Summary:** We introduce a two-phase quadratic integrate-and-fire (QIF) neuron whose membrane potential evolves according to two alternating Riccati equations within finite bounds. This simple extension removes the unphysical voltage divergence of the standard QIF model while producing realistic spike waveforms. Despite this modification, the system retains an exact low-dimensional description in the thermodynamic limit, governed by a single complex Riccati equation. Expressions for collective quantities su...

---

### 7. Performance of Conventional EEG Biomarkers Across Different Clinical Phases of Major Depressive Disorder: A Comprehensive Evaluation

**Authors:** Feng Yan, Xuteng Wang, Shuyu Yang, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03864v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03864v1)

**Summary:** While EEG features differentiate Major Depressive Disorder (MDD) from healthy controls (HC), their clinical utility as biomarkers depends on a monotonic trajectory across the disease spectrum, from the acute (AC) phase to the maintenance (MA) phase and finally to the healthy baseline. However, the progression of the MA phase remains poorly understood in traditional marker analysis. Analyzing EEG data from 74 individuals (24 AC, 23 MA, and 27 HC), this study provides a comprehensive evaluation of...

---

### 8. Solving adversarial examples requires solving exponential misalignment

**Authors:** Alessandro Salvatore, Stanislav Fort, Surya Ganguli

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03507v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03507v1)

**Summary:** Adversarial attacks - input perturbations imperceptible to humans that fool neural networks - remain both a persistent failure mode in machine learning, and a phenomenon with mysterious origins. To shed light, we define and analyze a network's perceptual manifold (PM) for a class concept as the space of all inputs confidently assigned to that class by the network. We find, strikingly, that the dimensionalities of neural network PMs are orders of magnitude higher than those of natural human conce...

---

### 9. Stringology-Based Motif Discovery from EEG Signals: an ADHD Case Study

**Authors:** Anat Dahan, Samah Ghazawi

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03476v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03476v1)

**Summary:** We propose a novel computational framework for analyzing electroencephalography (EEG) time series using methods from stringology, the study of efficient algorithms for string processing, to systematically identify and characterize recurrent temporal patterns in neural signals. The primary aim is to introduce quantitative measures to understand neural signal dynamics, with the present findings serving as a proof-of-concept. The framework adapts order-preserving matching (OPM) and Cartesian tree m...

---

### 10. Cognitive Dark Matter: Measuring What AI Misses

**Authors:** Patrick J. Mineault, Thomas L. Griffiths, Sean Escola

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03414v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03414v1)

**Summary:** We propose that the jagged intelligence landscape of modern AI systems arises from a missing training signal that we call "cognitive dark matter" (CDM): brain functions that meaningfully shape behavior yet are hard to infer from behavior alone. We identify key CDM domains-metacognition, cognitive flexibility, episodic memory, lifelong learning, abductive reasoning, social and common-sense reasoning, and emotional intelligence-and present evidence that current AI benchmarks and large-scale neuros...

---

### 11. A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks

**Authors:** Simone Betteti, Giacomo Baggio, Sandro Zampieri

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03201v2) | 📄 [PDF](https://arxiv.org/pdf/2603.03201v2)

**Summary:** Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoni...

---

### 12. Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity

**Authors:** Shogo Noguchi, Taketo Akama, Tai Nakamura, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03190v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03190v1)

**Summary:** During music listening, cortical activity encodes both acoustic and expectation-related information. Prior work has shown that ANN representations resemble cortical representations and can serve as supervisory signals for EEG recognition. Here we show that distinguishing acoustic and expectation-related ANN representations as teacher targets improves EEG-based music identification. Models pretrained to predict either representation outperform non-pretrained baselines, and combining them yields c...

---

### 13. Zigzag Persistence of Neural Responses to Time-Varying Stimuli

**Authors:** Yuri Gardinazzi, Alessio Ansuini, Eugenio Piasini, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03037v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03037v1)

**Summary:** We use topological data analysis to study neural population activity in the Sensorium 2023 dataset, which records responses from thousands of mouse visual cortex neurons to diverse video stimuli. For each video, we build frame-by-frame cubical complexes from neuronal activity and apply zigzag persistent homology to capture how topological structure evolves over time. These dynamics are summarized with persistence landscapes, providing a compact vectorized representation of temporal features. We ...

---

### 14. What Capable Agents Must Know: Selection Theorems for Robust Decision-Making under Uncertainty

**Authors:** Aran Nayebi

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.02491v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02491v1)

**Summary:** As artificial agents become increasingly capable, what internal structure is *necessary* for an agent to act competently under uncertainty? Classical results show that optimal control can be *implemented* using belief states or world models, but not that such representations are required. We prove quantitative "selection theorems" showing that low *average-case regret* on structured families of action-conditioned prediction tasks forces an agent to implement a predictive, structured internal sta...

---

### 15. Understanding Decision-Making Across the Lifespan Needs Theoretical Neuroscience

**Authors:** Michael B. Ryan, Letizia Ye, Anne K. Churchland

**Published:** 2026-03-02

🔗 [Paper](http://arxiv.org/abs/2603.02461v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02461v1)

**Summary:** Understanding how decision making changes across the lifespan is a central challenge for neuroscience, yet research on cognitive aging has remained largely disconnected from the theoretical and computational advances that now shape modern systems neuroscience. Over the past two decades, theoretical frameworks have transformed how we study cognition in young, healthy brains, providing principled tools to model latent decision states, neural dynamics, population codes, and interareal communication...

---

### 16. Rate-Distortion Signatures of Generalization and Information Trade-offs

**Authors:** Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin

**Published:** 2026-03-02

🔗 [Paper](http://arxiv.org/abs/2603.01568v1) | 📄 [PDF](https://arxiv.org/pdf/2603.01568v1)

**Summary:** Generalization to novel visual conditions remains a central challenge for both human and machine vision, yet standard robustness metrics offer limited insight into how systems trade accuracy for robustness. We introduce a rate-distortion-theoretic framework that treats stimulus-response behavior as an effective communication channel, derives rate-distortion (RD) frontiers from confusion matrices, and summarizes each system with two interpretable geometric signatures - slope ($β$) and curvature (...

---

### 17. An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes

**Authors:** Po-Chen Kuo, Edgar Y. Walker

**Published:** 2026-03-02

🔗 [Paper](http://arxiv.org/abs/2603.01387v2) | 📄 [PDF](https://arxiv.org/pdf/2603.01387v2)

**Summary:** The Bayesian brain hypothesis has been a leading theory in understanding perceptual decision-making under uncertainty. While extensive psychophysical evidence supports the notion of the brain performing Bayesian computations, how uncertainty information is encoded in sensory neural populations remains elusive. Specifically, two competing hypotheses propose that early sensory populations encode either the likelihood function (exemplified by probabilistic population codes) or the posterior distrib...

---

### 18. Scaling of learning time for high dimensional inputs

**Authors:** Carlos Stein Brito

**Published:** 2026-03-01

🔗 [Paper](http://arxiv.org/abs/2603.01184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.01184v1)

**Summary:** Representation learning from complex data typically involves models with a large number of parameters, which in turn require large amounts of data samples. In neural network models, model complexity grows with the number of inputs to each neuron, with a trade-off between model expressivity and learning time. A precise characterization of this trade-off would help explain the connectivity and learning times observed in artificial and biological networks. We present a theoretical analysis of how l...

---

### 19. Metric-Topology Factorization: A Computational Framework for Hippocampal-Neocortical Intelligence

**Authors:** Xin Li

**Published:** 2026-03-01

🔗 [Paper](http://arxiv.org/abs/2603.03362v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03362v1)

**Summary:** The brain achieves stability and plasticity in a topologically complex, shifting world through Metric-Topology Factorization (MTF), separating discrete topological indexing for context selection from continuous metric condensation for local inference. Semantically rich environments defy single globally contractive geometries, causing obstructions under shifts, so intelligence factorizes these: the hippocampus provides sparse signatures indexing manifold identity, while the neocortex untangles ge...

---

### 20. Contextuality, Incompatibility, and Intra-System Entanglement of Mental Markers

**Authors:** Andrei Khrennikov, Felix Benninger, Oded Shor

**Published:** 2026-02-27

🔗 [Paper](http://arxiv.org/abs/2603.03358v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03358v1)

**Summary:** Over the past two decades, quantum-like modeling (QLM) has emerged as a powerful framework for describing non-classical features of cognition and decision-making. Rather than assuming physical quantum processes in the brain, QLM employs the Hilbert space formalism to model contextuality, incompatibility of mental observables, and entanglement-like correlations. In this paper, we develop a quantum-informational model of mental markers within the broader I-field (information field) approach. We pr...

---

### 21. Inferring brain plasticity rule under long-term stimulation with structured recurrent dynamics

**Authors:** Zhichao Liang, Jingzhe Lin, Xinyi Li, et al.

**Published:** 2026-02-27

🔗 [Paper](http://arxiv.org/abs/2603.00213v1) | 📄 [PDF](https://arxiv.org/pdf/2603.00213v1)

**Summary:** Understanding how long-term stimulation reshapes neural circuits requires uncovering the rules of brain plasticity. While short-term synaptic modifications have been extensively characterized, the principles that drive circuit-level reorganization across hours to weeks remain unknown. Here, we formalize these principles as a latent dynamical law that governs how recurrent connectivity evolves under repeated interventions. To capture this law, we introduce the Stimulus-Evoked Evolution Recurrent ...

---

### 22. Inhibitory Cross-Talk Enables Functional Lateralization in Attention-Coupled Latent Memory

**Authors:** Hong Jeong

**Published:** 2026-02-27

🔗 [Paper](http://arxiv.org/abs/2603.03355v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03355v1)

**Summary:** We present a memory-augmented transformer in which attention serves simultaneously as a retrieval, consolidation, and write-back operator. The core update, $A^\top A V W$, re-grounds retrieved values into persistent memory slots via the Gram matrix $A^\top A$, providing a principled tripartite projection: observation space $\to$ latent memory $\to$ supervised transformation. We partition the memory into lateralized left and right banks coupled through a sign-controlled cross-talk matrix $W_s$, a...

---

### 23. Non-Invasive Reconstruction of Intracranial EEG Across the Deep Temporal Lobe from Scalp EEG based on Conditional Normalizing Flow

**Authors:** Dongyi He, Bin Jiang, Kecheng Feng, et al.

**Published:** 2026-02-27

🔗 [Paper](http://arxiv.org/abs/2603.03354v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03354v1)

**Summary:** Although obtaining deep brain activity from non-invasive scalp electroencephalography (sEEG) is crucial for neuroscience and clinical diagnosis, directly generating high-fidelity intracranial electroencephalography (iEEG) signals remains a largely unexplored field, limiting our understanding of deep brain dynamics. Current research primarily focuses on traditional signal processing or source localization methods, which struggle to capture the complex waveforms and random characteristics of iEEG....

---

### 24. Exploiting network topology in brain-scale simulations of spiking neural networks

**Authors:** Melissa Lober, Markus Diesmann, Susanne Kunkel

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.23274v1) | 📄 [PDF](https://arxiv.org/pdf/2602.23274v1)

**Summary:** Simulation code for conventional supercomputers serves as a reference for neuromorphic computing systems. The present bottleneck of distributed large-scale spiking neuronal network simulations is the communication between compute nodes. Communication speed seems limited by the interconnect between the nodes and the software library orchestrating the data transfer. Profiling reveals, however, that the variability of the time required by the compute nodes between communication calls is large. The ...

---

### 25. Collective Dynamics in Spiking Neural Networks Beyond Dale's Principle

**Authors:** Ross Ah-Weng, Hardik Rajpal

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.23202v1) | 📄 [PDF](https://arxiv.org/pdf/2602.23202v1)

**Summary:** Dale's Principle has historically guided neuroscience research as a valuable rule of thumb, namely that all synapses on each neuron release the same set of neurotransmitters. Most existing Spiking Neuron Network models share this dichotomous assumption that neurons are either excitatory or inhibitory; however, recent experimental evidence points towards co-release mechanisms that violate this assumption. Here, we introduce a minimal model of "Bilingual" neurons violating Dale's principle that ca...

---

### 26. Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG

**Authors:** Hanning Guo, Farah Abdellatif, Hanwen Bi, et al.

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.23410v2) | 📄 [PDF](https://arxiv.org/pdf/2602.23410v2)

**Summary:** Brain foundation models have achieved remarkable advances across a wide range of neuroscience tasks. However, most existing models are limited to a single functional modality, restricting their ability to exploit complementary spatiotemporal dynamics and the collective data scale across imaging techniques. To address this limitation, we propose Brain-OF, the first omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG, capable of handling both unimodal and multimodal input...

---

### 27. SPD Learn: A Geometric Deep Learning Python Library for Neural Decoding Through Trivialization

**Authors:** Bruno Aristimunha, Ce Ju, Antoine Collas, et al.

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.22895v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22895v1)

**Summary:** Implementations of symmetric positive definite (SPD) matrix-based neural networks for neural decoding remain fragmented across research codebases and Python packages. Existing implementations often employ ad hoc handling of manifold constraints and non-unified training setups, which hinders reproducibility and integration into modern deep-learning workflows. To address this gap, we introduce SPD Learn, a unified and modular Python package for geometric deep learning with SPD matrices. SPD Learn ...

---

### 28. Cognitive Models and AI Algorithms Provide Templates for Designing Language Agents

**Authors:** Ryan Liu, Dilip Arumugam, Cedegao E. Zhang, et al.

**Published:** 2026-02-26

🔗 [Paper](http://arxiv.org/abs/2602.22523v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22523v1)

**Summary:** While contemporary large language models (LLMs) are increasingly capable in isolation, there are still many difficult problems that lie beyond the abilities of a single LLM. For such tasks, there is still uncertainty about how best to take many LLMs as parts and combine them into a greater whole. This position paper argues that potential blueprints for designing such modular language agents can be found in the existing literature on cognitive models and artificial intelligence (AI) algorithms. T...

---

### 29. Exploring Human Behavior During Abstract Rule Inference and Problem Solving with the Cognitive Abstraction and Reasoning Corpus

**Authors:** Caroline Ahn, Quan Do, Leah Bakst, et al.

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.22408v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22408v1)

**Summary:** Humans exhibit remarkable flexibility in abstract reasoning, and can rapidly learn and apply rules from sparse examples. To investigate the cognitive strategies underlying this ability, we introduce the Cognitive Abstraction and Reasoning Corpus (CogARC), a diverse human-adapted subset of the Abstraction and Reasoning Corpus (ARC) which was originally developed to benchmark abstract reasoning in artificial intelligence. Across two experiments, CogARC was administered to a total of 260 human part...

---

### 30. Spatiotemporal bursting in simulated cultures of cortical neurons

**Authors:** Michael Stiber, Natalie Gonzales, Jewel YunHsuan Lee

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.22364v1) | 📄 [PDF](https://arxiv.org/pdf/2602.22364v1)

**Summary:** Cultures of neurons grown on multi-electrode arrays have become a common experimental preparation for investigating developing neural networks. Experiment and simulation have shown that these developing networks eventually exhibit bursting behavior in which the entire culture participates for short periods of time, with inter-burst intervals in which the network is comparatively quiescent. This paper extends previous simulation results by examining the spatiotemporal patterns of such bursting. W...

---

### 31. Efficient Coding Predicts Synaptic Conductance

**Authors:** James V Stone

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2603.03347v2) | 📄 [PDF](https://arxiv.org/pdf/2603.03347v2)

**Summary:** Synapses are information efficient in the sense that their natural conductance values convey as many bits per Joule as possible, but efficiency falls rapidly if the conductance is forced to deviate from its natural value (Harris et al, 2015. However, the exact manner in which efficiency falls as conductance deviates from its natural value remains unexplained. Recently, Malkin et al (2026) showed that synaptic noise is minimised given the available energy, consistent with a minimal energy boundar...

---

### 32. Limits of optimal decoding under synaptic coarse-tuning

**Authors:** Ori Hendler, Ronen Segev, Maoz Shamir

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.21758v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21758v1)

**Summary:** Sensory information propagates through successive processing stages in the brain, where synaptic weight patterns between stations determine how downstream neurons decode information from upstream populations. Although optimized synaptic connectivity can enhance information transmission, it requires precise weight tuning. Recent evidence depicting substantial synaptic volatility raises two fundamental questions: How does coarse-tuning of synaptic connectivity affect information transmission? What...

---

### 33. One Brain, Omni Modalities: Towards Unified Non-Invasive Brain Decoding with Large Language Models

**Authors:** Changli Tang, Shurui Li, Junliang Wang, et al.

**Published:** 2026-02-25

🔗 [Paper](http://arxiv.org/abs/2602.21522v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21522v1)

**Summary:** Deciphering brain function through non-invasive recordings requires synthesizing complementary high-frequency electromagnetic (EEG/MEG) and low-frequency metabolic (fMRI) signals. However, despite their shared neural origins, extreme discrepancies have traditionally confined these modalities to isolated analysis pipelines, hindering a holistic interpretation of brain activity. To bridge this fragmentation, we introduce \textbf{NOBEL}, a \textbf{n}euro-\textbf{o}mni-modal \textbf{b}rain-\textbf{e...

---

### 34. Characterization of Phase Transitions in a Lipkin-Meshkov-Glick Quantum Brain Model

**Authors:** Elvira Romera, Joaquín J. Torres

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2603.03345v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03345v1)

**Summary:** In this work we analyze the emergence of phase transitions in a quantum brain model inspired by the Lipkin-Meshkov-Glick framework, where biologically motivated synaptic feedback modulates the collective interaction in a nonlinear and state-dependent manner. We demonstrate that incorporating this retroactive mechanism substantially reshapes the phase structure, yielding an expansion of the paramagnetic phase at the expense of the ferromagnetic phases relative to the feedback-free scenario. This ...

---

### 35. Neuro-Symbolic Decoding of Neural Activity

**Authors:** Yanchen Wang, Joy Hsu, Ehsan Adeli, et al.

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2603.03343v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03343v1)

**Summary:** We propose NEURONA, a neuro-symbolic framework for fMRI decoding and concept grounding in neural activity. Leveraging image- and video-based fMRI question-answering datasets, NEURONA learns to decode interacting concepts from visual stimuli based on patterns of fMRI responses, integrating symbolic reasoning and compositional execution with fMRI grounding across brain regions. We demonstrate that incorporating structural priors (e.g., compositional predicate-argument dependencies between concepts...

---

### 36. CRCC: Contrast-Based Robust Cross-Subject and Cross-Site Representation Learning for EEG

**Authors:** Xiaobin Wong, Zhonghua Zhao, Haoran Guo, et al.

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19138v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19138v1)

**Summary:** EEG-based neural decoding models often fail to generalize across acquisition sites due to structured, site-dependent biases implicitly exploited during training. We reformulate cross-site clinical EEG learning as a bias-factorized generalization problem, in which domain shifts arise from multiple interacting sources. We identify three fundamental bias factors and propose a general training framework that mitigates their influence through data standardization and representation-level constraints....

---

### 37. Critical Scaling and Metabolic Regulation in a Ginzburg--Landau Theory of Cognitive Dynamics

**Authors:** Gunn Kim

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19023v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19023v1)

**Summary:** We formulate a phenomenological effective field theory in which biological intelligence emerges as a macroscopic order parameter sustained by continuous metabolic flux. By modeling cognition as a coarse-grained neural activity field governed by a variational free energy, we derive closed-form expressions for information capacity and structural susceptibility using a Gaussian maximum entropy approximation. The theory predicts a universal algebraic divergence of the susceptibility, $χ\sim K^{-3/2}...

---

### 38. Modularity is the Bedrock of Natural and Artificial Intelligence

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18960v1)

**Summary:** The remarkable performance of modern AI systems has been driven by unprecedented scales of data, computation, and energy -- far exceeding the resources required by human intelligence. This disparity highlights the need for new guiding principles and motivates drawing inspiration from the fundamental organizational principles of brain computation. Among these principles, modularity has been shown to be critical for supporting the efficient learning and strong generalization abilities consistently...

---

### 39. From Modules to Movement: Deconstructing the Modular Architecture of the Motor System

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18787v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18787v1)

**Summary:** Coordinating multi-articulated bodies to generate purposeful movement is a formidable computational challenge. Yet the human motor system performs this task robustly in dynamic, uncertain environments, despite noisy and delayed feedback, slow actuators, and strict energetic constraints. A central question is what organizational principles underlie this efficiency. One widely recognized principle of neural organization is modularity, which enables complex problems to be decomposed into simpler su...

---

### 40. A Data-Driven Method to Map the Functional Organisation of Human Brain White Matter

**Authors:** Yifei Sun, James M. Shine, Robert D. Sanders, et al.

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18715v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18715v1)

**Summary:** The white matter of the brain is organised into axonal bundles that support long-range neural communication. Although diffusion MRI (dMRI) enables detailed mapping of these pathways through tractography, how white matter pathways directly facilitate large-scale neural synchronisation remains poorly understood. We developed a data-driven framework that integrates dMRI and functional MRI (fMRI) to model the dynamic coupling supported by white matter tracks. Specifically, we employed track dynamic ...

---

### 41. Neural Fields as World Models

**Authors:** Joshua Nunley

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18690v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18690v1)

**Summary:** How does the brain predict physical outcomes while acting in the world? Machine learning world models compress visual input into latent spaces, discarding the spatial structure that characterizes sensory cortex. We propose isomorphic world models: architectures preserving sensory topology so that physics prediction becomes geometric propagation rather than abstract state transition. We implement this using neural fields with motor-gated channels, where activity evolves through local lateral conn...

---

### 42. Online decoding of rat self-paced locomotion speed from EEG using recurrent neural networks

**Authors:** Alejandro de Miguel, Nelson Totah, Uri Maoz

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18637v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18637v1)

**Summary:** $\textit{Objective.}$ Accurate neural decoding of locomotion holds promise for advancing rehabilitation, prosthetic control, and understanding neural correlates of action. Recent studies have demonstrated decoding of locomotion kinematics across species on motorized treadmills. However, efforts to decode locomotion speed in more natural contexts$-$where pace is self-selected rather than externally imposed$-$are scarce, generally achieve only modest accuracy, and require intracranial implants. He...

---

### 43. Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay

**Authors:** Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18401v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18401v1)

**Summary:** Biological neural networks (like the hippocampus) can internally generate "replay" resembling stimulus-driven activity. Recent computational models of replay use noisy recurrent neural networks (RNNs) trained to path-integrate. Replay in these networks has been described as Langevin sampling, but new modifiers of noisy RNN replay have surpassed this description. We re-examine noisy RNN replay as sampling to understand or improve it in three ways: (1) Under simple assumptions, we prove that the g...

---

### 44. A systematic approach to answering the easy problems of consciousness based on an executable cognitive system

**Authors:** Qi Zhang

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2603.04440v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04440v1)

**Summary:** Consciousness is the window of the brain and reflects many fundamental cognitive properties involving both computational and cognitive mechanisms. A collection of these properties was described as the "easy problems" by Chalmers, including the ability to discriminate, categorize, and react to stimuli; information integration; reportability; information access; attention; deliberate control; and the difference between wakefulness and sleep. These "easy problems" have not been systematically addre...

---

### 45. Scaling and tuning to criticality in resting-state human magnetoencephalography

**Authors:** Irem Topal, Anna Poggialini, Marco Dal Maschio, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17820v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17820v1)

**Summary:** Scaling laws in biological neural networks have long been investigated. From 1/f noise to neuronal avalanches, evidence of scaling in brain activity has been increasingly linked to tuning to or near criticality. The concept of scaling is intimately related to the renormalization group (RG), in essence providing coarse-grained, simplified descriptions that generalize to classes of diverse physical systems. Following the RG idea, a coarse-graining scheme has recently been proposed for populations ...

---

### 46. Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis

**Authors:** Minheng Chen, Tong Chen, Chao Cao, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17557v2) | 📄 [PDF](https://arxiv.org/pdf/2602.17557v2)

**Summary:** Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, viol...

---

### 47. A Benchmark Analysis of Graph and Non-Graph Methods for Caenorhabditis Elegans Neuron Classification

**Authors:** Jingqi Lu, Keqi Han, Yun Wang, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2603.02241v1) | 📄 [PDF](https://arxiv.org/pdf/2603.02241v1)

**Summary:** This study establishes a benchmark for Caenorhabditis elegans neuron classification, comparing four graph methods (GCN, GraphSAGE, GAT, GraphTransformer) against four non-graph methods (Logistic Regression, MLP, LOLCAT, NeuPRINT). Using the functional connectome, we classified Sensory, Interneuron, and Motor neurons based on Spatial, Connection, and Neuronal Activity features. Results show that attention-based GNNs significantly outperform baselines on the Spatial and Connection features. The Ne...

---

### 48. Construction of a classification model for dementia among Brazilian adults aged 50 and over

**Authors:** F. S. Menezes, M. C. F. G. Barretto, E. Q. C. Garcia, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16887v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16887v1)

**Summary:** To build a dementia classification model for middle-aged and elderly Brazilians, implemented in Python, combining variable selection and multivariable analysis, using low-cost variables with modification potential. Observational study with a predictive modeling approach using a cross-sectional design, aimed at estimating the chances of developing dementia, using data from the Brazilian Longitudinal Study of Aging (ELSI-Brazil), involving 9,412 participants. Dementia was determined based on neuro...

---

### 49. A Systematic Evaluation of Sample-Level Tokenization Strategies for MEG Foundation Models

**Authors:** SungJun Cho, Chetan Gohil, Rukuang Huang, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16626v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16626v1)

**Summary:** Recent success in natural language processing has motivated growing interest in large-scale foundation models for neuroimaging data. Such models often require discretization of continuous neural time series data, a process referred to as 'tokenization'. However, the impact of different tokenization strategies for neural data is currently poorly understood. In this work, we present a systematic evaluation of sample-level tokenization strategies for transformer-based large neuroimaging models (LNM...

---

### 50. The Representational Alignment Hypothesis: Evidence for and Consequences of Invariant Semantic Structure Across Embedding Modalities

**Authors:** Akhil Ramidi, Kevin Scharp

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16584v1)

**Summary:** There is growing evidence that independently trained AI systems come to represent the world in the same way. In other words, independently trained embeddings from text, vision, audio, and neural signals share an underlying geometry. We call this the Representational Alignment Hypothesis (RAH) and investigate evidence for and consequences of this claim. The evidence is of two kinds: (i) internal structure comparison techniques, such as representational similarity analysis and topological data ana...

---

## stat.ML

**50 papers**

### 1. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis

**Authors:** Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05483v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05483v1)

**Summary:** Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragment...

---

### 2. Thermodynamic Response Functions in Singular Bayesian Models

**Authors:** Sean Plummer

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05480v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05480v1)

**Summary:** Singular statistical models-including mixtures, matrix factorization, and neural networks-violate regular asymptotics due to parameter non-identifiability and degenerate Fisher geometry. Although singular learning theory characterizes marginal likelihood behavior through invariants such as the real log canonical threshold and singular fluctuation, these quantities remain difficult to interpret operationally. At the same time, widely used criteria such as WAIC and WBIC appear disconnected from un...

---

### 3. Harnessing Synthetic Data from Generative AI for Statistical Inference

**Authors:** Ahmad Abdel-Azim, Ruoyu Wang, Xihong Lin

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05396v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05396v1)

**Summary:** The emergence of generative AI models has dramatically expanded the availability and use of synthetic data across scientific, industrial, and policy domains. While these developments open new possibilities for data analysis, they also raise fundamental statistical questions about when synthetic data can be used in a valid, reliable, and principled manner. This paper reviews the current landscape of synthetic data generation and use from a statistical perspective, with the goal of clarifying the ...

---

### 4. On the Statistical Optimality of Optimal Decision Trees

**Authors:** Zineng Xu, Subhroshekhar Ghosh, Yan Shuo Tan

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05340v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05340v1)

**Summary:** While globally optimal empirical risk minimization (ERM) decision trees have become computationally feasible and empirically successful, rigorous theoretical guarantees for their statistical performance remain limited. In this work, we develop a comprehensive statistical theory for ERM trees under random design in both high-dimensional regression and classification. We first establish sharp oracle inequalities that bound the excess risk of the ERM estimator relative to the best possible approxim...

---

### 5. Bayes with No Shame: Admissibility Geometries of Predictive Inference

**Authors:** Nicholas G. Polson, Daniel Zantedeschi

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05335v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05335v1)

**Summary:** Four distinct admissibility geometries govern sequential and distribution-free inference: Blackwell risk dominance over convex risk sets, anytime-valid admissibility within the nonnegative supermartingale cone, marginal coverage validity over exchangeable prediction sets, and Cesàro approachability (CAA) admissibility, which reaches the risk-set boundary via approachability-style arguments rather than explicit priors. We prove a criterion separation theorem: the four classes of admissible proced...

---

### 6. How important are the genes to explain the outcome - the asymmetric Shapley value as an honest importance metric for high-dimensional features

**Authors:** Mark A. van de Wiel, Jeroen Goedhart, Martin Jullum, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05317v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05317v1)

**Summary:** In clinical prediction settings the importance of a high-dimensional feature like genomics is often assessed by evaluating the change in predictive performance when adding it to a set of traditional clinical variables. This approach is questionable, because it does not account for collinearity nor known directionality of dependencies between variables. We suggest to use asymmetric Shapley values as a more suitable alternative to quantify feature importance in the context of a mixed-dimensional p...

---

### 7. Bayesian Supervised Causal Clustering

**Authors:** Luwei Wang, Nazir Lone, Sohan Seth

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05288v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05288v1)

**Summary:** Finding patient subgroups with similar characteristics is crucial for personalized decision-making in various disciplines such as healthcare and policy evaluation. While most existing approaches rely on unsupervised clustering methods, there is a growing trend toward using supervised clustering methods that identify operationalizable subgroups in the context of a specific outcome of interest. We propose Bayesian Supervised Causal Clustering (BSCC), with treatment effect as outcome to guide the c...

---

### 8. Layer by layer, module by module: Choose both for optimal OOD probing of ViT

**Authors:** Ambroise Odonnat, Vasilii Feofanov, Laetitia Chapel, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05280v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05280v1)

**Summary:** Recent studies have observed that intermediate layers of foundation models often yield more discriminative representations than the final layer. While initially attributed to autoregressive pretraining, this phenomenon has also been identified in models trained via supervised and discriminative self-supervised objectives. In this paper, we conduct a comprehensive study to analyze the behavior of intermediate layers in pretrained vision transformers. Through extensive linear probing experiments a...

---

### 9. Learning Optimal Individualized Decision Rules with Conditional Demographic Parity

**Authors:** Wenhai Cui, Wen Su, Donglin Zeng, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05226v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05226v1)

**Summary:** Individualized decision rules (IDRs) have become increasingly prevalent in societal applications such as personalized marketing, healthcare, and public policy design. However, a critical ethical concern arises from the potential discriminatory effects of IDRs trained on biased data. These algorithms may disproportionately harm individuals from minority subgroups defined by sensitive attributes like gender, race, or language. To address this issue, we propose a novel framework that incorporates d...

---

### 10. Towards a data-scale independent regulariser for robust sparse identification of non-linear dynamics

**Authors:** Jay Raut, Daniel N. Wilke, Stephan Schmidt

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05201v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05201v1)

**Summary:** Data normalisation, a common and often necessary preprocessing step in engineering and scientific applications, can severely distort the discovery of governing equations by magnitudebased sparse regression methods. This issue is particularly acute for the Sparse Identification of Nonlinear Dynamics (SINDy) framework, where the core assumption of sparsity is undermined by the interaction between data scaling and measurement noise. The resulting discovered models can be dense, uninterpretable, and...

---

### 11. Federated Causal Discovery Across Heterogeneous Datasets under Latent Confounding

**Authors:** Maximilian Hahn, Alina Zajak, Dominik Heider, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05149v1)

**Summary:** Causal discovery across multiple datasets is often constrained by data privacy regulations and cross-site heterogeneity, limiting the use of conventional methods that require a single, centralized dataset. To address these challenges, we introduce fedCI, a federated conditional independence test that rigorously handles heterogeneous datasets with non-identical sets of variables, site-specific effects, and mixed variable types, including continuous, ordinal, binary, and categorical variables. At ...

---

### 12. Non-Euclidean Gradient Descent Operates at the Edge of Stability

**Authors:** Rustem Islamov, Michael Crawshaw, Jeremy Cohen, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.05002v1) | 📄 [PDF](https://arxiv.org/pdf/2603.05002v1)

**Summary:** The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian converges to $2/η$ during training with gradient descent (GD) with a step-size $η$. Despite (apparently) violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We provide an interpretation of EoS through the lens of Directional Smoothness Mishkin et al. [2024]. This interpretation naturally extends to non-Euclid...

---

### 13. How Does the ReLU Activation Affect the Implicit Bias of Gradient Descent on High-dimensional Neural Network Regression?

**Authors:** Kuo-Wei Lai, Guanghui Wang, Molei Tao, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04895v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04895v1)

**Summary:** Overparameterized ML models, including neural networks, typically induce underdetermined training objectives with multiple global minima. The implicit bias refers to the limiting global minimum that is attained by a common optimization algorithm, such as gradient descent (GD). In this paper, we characterize the implicit bias of GD for training a shallow ReLU model with the squared loss on high-dimensional random features. Prior work showed that the implicit bias does not exist in the worst-case ...

---

### 14. The Inductive Bias of Convolutional Neural Networks: Locality and Weight Sharing Reshape Implicit Regularization

**Authors:** Tongtong Liang, Esha Singh, Rahul Parhi, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04807v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04807v1)

**Summary:** We study how architectural inductive bias reshapes the implicit regularization induced by the edge-of-stability phenomenon in gradient descent. Prior work has established that for fully connected networks, the strength of this regularization is governed solely by the global input geometry; consequently, it is insufficient to prevent overfitting on difficult distributions such as the high-dimensional sphere. In this paper, we show that locality and weight sharing fundamentally change this picture...

---

### 15. Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning

**Authors:** Haoyue Dai, Immanuel Albrecht, Peter Spirtes, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04780v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04780v1)

**Summary:** Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others. We argue that a core obstacle to a general, structural-assumption-free approach is the lack of an equivalence characterization: without knowing what can be identified, one generally cannot design methods for how to identify it. In this work, we aim to close this ga...

---

### 16. Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation

**Authors:** Zafeirios Fountas, Adnan Oomerjee, Haitham Bou-Ammar, et al.

**Published:** 2026-03-05

🔗 [Paper](http://arxiv.org/abs/2603.04688v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04688v1)

**Summary:** Standard accounts of memory consolidation emphasise the stabilisation of stored representations, but struggle to explain representational drift, semanticisation, or the necessity of offline replay. Here we propose that high-capacity neocortical networks optimise stored representations for generalisation by reducing complexity via predictive forgetting, i.e. the selective retention of experienced information that predicts future outcomes or experience. We show that predictive forgetting formally ...

---

### 17. sFRC for assessing hallucinations in medical image restoration

**Authors:** Prabhat Kc, Rongping Zeng, Nirmal Soni, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04673v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04673v1)

**Summary:** Deep learning (DL) methods are currently being explored to restore images from sparse-view-, limited-data-, and undersampled-based acquisitions in medical applications. Although outputs from DL may appear visually appealing based on likability/subjective criteria (such as less noise, smooth features), they may also suffer from hallucinations. This issue is further exacerbated by a lack of easy-to-use techniques and robust metrics for the identification of hallucinations in DL outputs. In this wo...

---

### 18. Optimal Prediction-Augmented Algorithms for Testing Independence of Distributions

**Authors:** Maryam Aliakbarpour, Alireza Azizi, Ria Stevens

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04635v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04635v1)

**Summary:** Independence testing is a fundamental problem in statistical inference: given samples from a joint distribution $p$ over multiple random variables, the goal is to determine whether $p$ is a product distribution or is $ε$-far from all product distributions in total variation distance. In the non-parametric finite-sample regime, this task is notoriously expensive, as the minimax sample complexity scales polynomially with the support size. In this work, we move beyond these worst-case limitations b...

---

### 19. K-Means as a Radial Basis function Network: a Variational and Gradient-based Equivalence

**Authors:** Felipe de Jesus Felix Arredondo, Alejandro Ucan-Puc, Carlos Astengo Noguez

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04625v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04625v1)

**Summary:** This work establishes a rigorous variational and gradient-based equivalence between the classical K-Means algorithm and differentiable Radial Basis Function (RBF) neural networks with smooth responsibilities. By reparameterizing the K-Means objective and embedding its distortion functional into a smooth weighted loss, we prove that the RBF objective $Γ$-converges to the K-Means solution as the temperature parameter $σ$ vanishes. We further demonstrate that the gradient-based updates of the RBF c...

---

### 20. Oracle-efficient Hybrid Learning with Constrained Adversaries

**Authors:** Princewill Okoroafor, Robert Kleinberg, Michael P. Kim

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04546v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04546v1)

**Summary:** The Hybrid Online Learning Problem, where features are drawn i.i.d. from an unknown distribution but labels are generated adversarially, is a well-motivated setting positioned between statistical and fully-adversarial online learning. Prior work has presented a dichotomy: algorithms that are statistically-optimal, but computationally intractable (Wu et al., 2023), and algorithms that are computationally-efficient (given an ERM oracle), but statistically-suboptimal (Wu et al., 2024).   This paper...

---

### 21. The Volterra signature

**Authors:** Paul P. Hager, Fabian N. Harang, Luca Pelizzari, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04525v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04525v1)

**Summary:** Modern approaches for learning from non-Markovian time series, such as recurrent neural networks, neural controlled differential equations or transformers, typically rely on implicit memory mechanisms that can be difficult to interpret or to train over long horizons. We propose the Volterra signature $\mathrm{VSig}(x;K)$ as a principled, explicit feature representation for history-dependent systems. By developing the input path $x$ weighted by a temporal kernel $K$ into the tensor algebra, we le...

---

### 22. PTOPOFL: Privacy-Preserving Personalised Federated Learning via Persistent Homology

**Authors:** Kelly L Vomo-Donfack, Adryel Hoszu, Grégory Ginot, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04323v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04323v1)

**Summary:** Federated learning (FL) faces two structural tensions: gradient sharing enables data-reconstruction attacks, while non-IID client distributions degrade aggregation quality. We introduce PTOPOFL, a framework that addresses both challenges simultaneously by replacing gradient communication with topological descriptors derived from persistent homology (PH). Clients transmit only 48-dimensional PH feature vectors-compact shape summaries whose many-to-one structure makes inversion provably ill-posed-...

---

### 23. Bayesian Modeling of Collatz Stopping Times: A Probabilistic Machine Learning Perspective

**Authors:** Nicolò Bonacorsi, Matteo Bordoni

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04479v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04479v1)

**Summary:** We study the Collatz total stopping time $τ(n)$ over $n\le 10^7$ from a probabilistic machine learning viewpoint. Empirically, $τ(n)$ is a skewed and heavily overdispersed count with pronounced arithmetic heterogeneity. We develop two complementary models. First, a Bayesian hierarchical Negative Binomial regression (NB2-GLM) predicts $τ(n)$ from simple covariates ($\log n$ and residue class $n \bmod 8$), quantifying uncertainty via posterior and posterior predictive distributions. Second, we pro...

---

### 24. Statistical Inference for Score Decompositions

**Authors:** Timo Dimitriadis, Marius Puke

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04275v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04275v1)

**Summary:** We introduce inference methods for score decompositions, which partition scoring functions for predictive assessment into three interpretable components: miscalibration, discrimination, and uncertainty. Our estimation and inference relies on a linear recalibration of the forecasts, which is applicable to general multi-step ahead point forecasts such as means and quantiles due to its validity for both smooth and non-smooth scoring functions. This approach ensures desirable finite-sample propertie...

---

### 25. Semi-Supervised Generative Learning via Latent Space Distribution Matching

**Authors:** Kwong Yu Chong, Long Feng

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04223v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04223v1)

**Summary:** We introduce Latent Space Distribution Matching (LSDM), a novel framework for semi-supervised generative modeling of conditional distributions. LSDM operates in two stages: (i) learning a low-dimensional latent space from both paired and unpaired data, and (ii) performing joint distribution matching in this space via the 1-Wasserstein distance, using only paired data. This two-step approach minimizes an upper bound on the 1-Wasserstein distance between joint distributions, reducing reliance on s...

---

### 26. Beyond Mixtures and Products for Ensemble Aggregation: A Likelihood Perspective on Generalized Means

**Authors:** Raphaël Razafindralambo, Rémy Sun, Frédéric Precioso, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04204v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04204v1)

**Summary:** Density aggregation is a central problem in machine learning, for instance when combining predictions from a Deep Ensemble. The choice of aggregation remains an open question with two commonly proposed approaches being linear pooling (probability averaging) and geometric pooling (logit averaging). In this work, we address this question by studying the normalized generalized mean of order $r \in \mathbb{R} \cup \{-\infty,+\infty\}$ through the lens of log-likelihood, the standard evaluation crite...

---

### 27. Stable and Steerable Sparse Autoencoders with Weight Regularization

**Authors:** Piotr Jedryszek, Oliver M. Crook

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04198v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04198v1)

**Summary:** Sparse autoencoders (SAEs) are widely used to extract human-interpretable features from neural network activations, but their learned features can vary substantially across random seeds and training choices. To improve stability, we studied weight regularization by adding L1 or L2 penalties on encoder and decoder weights, and evaluate how regularization interacts with common SAE training defaults. On MNIST, we observe that L2 weight regularization produces a core of highly aligned features and, ...

---

### 28. Exploiting Subgradient Sparsity in Max-Plus Neural Networks

**Authors:** Ikhlas Enaieh, Olivier Fercoq

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04133v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04133v1)

**Summary:** Deep Neural Networks are powerful tools for solving machine learning problems, but their training often involves dense and costly parameter updates. In this work, we use a novel Max-Plus neural architecture in which classical addition and multiplication are replaced with maximum and summation operations respectively. This is a promising architecture in terms of interpretability, but its training is challenging. A particular feature is that this algebraic structure naturally induces sparsity in t...

---

### 29. Testing Full Mediation of Treatment Effects and the Identifiability of Causal Mechanisms

**Authors:** Martin Huber, Kevin Kloiber, Lukáš Lafférs

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04109v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04109v1)

**Summary:** In causal analysis, understanding the causal mechanisms through which an intervention or treatment affects an outcome is often of central interest. We propose a test to evaluate (i) whether the causal effect of a treatment that is randomly assigned conditional on covariates is fully mediated by, or operates exclusively through, observed intermediate outcomes (referred to as mediators or surrogate outcomes), and (ii) whether the various causal mechanisms operating through different mediators are ...

---

### 30. Fixed-Budget Constrained Best Arm Identification in Grouped Bandits

**Authors:** Raunak Mukherjee, Sharayu Moharir

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04007v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04007v1)

**Summary:** We study fixed budget constrained best-arm identification in grouped bandits, where each arm consists of multiple independent attributes with stochastic rewards. An arm is considered feasible only if all its attributes' means are above a given threshold. The aim is to find the feasible arm with the largest overall mean. We first derive a lower bound on the error probability for any algorithm on this setting. We then propose Feasibility Constrained Successive Rejects (FCSR), a novel algorithm tha...

---

### 31. Hierarchical Inference and Closure Learning via Adaptive Surrogates for ODEs and PDEs

**Authors:** Pengyu Zhang, Arnaud Vadeboncoeur, Alex Glyn-Davies, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03922v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03922v1)

**Summary:** Inverse problems are the task of calibrating models to match data. They play a pivotal role in diverse engineering applications by allowing practitioners to align models with reality. In many applications, engineers and scientists do not have a complete picture of i) the detailed properties of a system (such as material properties, geometry, initial conditions, etc.); ii) the complete laws describing all dynamics at play (such as friction laws, complicated damping phenomena, and general nonlinea...

---

### 32. Dictionary Based Pattern Entropy for Causal Direction Discovery

**Authors:** Harikrishnan N B, Shubham Bhilare, Aditi Kathpalia, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.04473v1) | 📄 [PDF](https://arxiv.org/pdf/2603.04473v1)

**Summary:** Discovering causal direction from temporal observational data is particularly challenging for symbolic sequences, where functional models and noise assumptions are often unavailable. We propose a novel \emph{Dictionary Based Pattern Entropy ($DPE$)} framework that infers both the direction of causation and the specific subpatterns driving changes in the effect variable. The framework integrates \emph{Algorithmic Information Theory} (AIT) and \emph{Shannon Information Theory}. Causation is interp...

---

### 33. Invariance-Based Dynamic Regret Minimization

**Authors:** Margherita Lazzaretto, Jonas Peters, Niklas Pfister

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03843v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03843v1)

**Summary:** We consider stochastic non-stationary linear bandits where the linear parameter connecting contexts to the reward changes over time. Existing algorithms in this setting localize the policy by gradually discarding or down-weighting past data, effectively shrinking the time horizon over which learning can occur. However, in many settings historical data may still carry partial information about the reward model. We propose to leverage such data while adapting to changes, by assuming the reward mod...

---

### 34. Direct Bayesian Additive Regression Trees for Conditional Average Treatment Effects in Regression Discontinuity Designs

**Authors:** Daisuke Kondo, Shonosuke Sugasawa

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03819v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03819v1)

**Summary:** Regression discontinuity designs (RDD) are widely used for causal inference. In many empirical applications, treatment effects vary substantially with covariates, and ignoring such heterogeneity can lead to misleading conclusions, which motivates flexible modeling of heterogeneous treatment effects in RDD. To this end, we propose a Bayesian nonparametric approach to estimating heterogeneous treatment effects based on Bayesian Additive Regression Trees (BART). The key feature of our method lies i...

---

### 35. Observationally Informed Adaptive Causal Experimental Design

**Authors:** Erdun Gao, Liang Zhang, Jake Fawkes, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03785v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03785v1)

**Summary:** Randomized Controlled Trials (RCTs) represent the gold standard for causal inference yet remain a scarce resource. While large-scale observational data is often available, it is utilized only for retrospective fusion, and remains discarded in prospective trial design due to bias concerns. We argue this "tabula rasa" data acquisition strategy is fundamentally inefficient. In this work, we propose Active Residual Learning, a new paradigm that leverages the observational model as a foundational pri...

---

### 36. Inverse Contextual Bandits without Rewards: Learning from a Non-Stationary Learner via Suffix Imitation

**Authors:** Yuqi Kong, Xiao Zhang, Weiran Shen

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03778v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03778v1)

**Summary:** We study the Inverse Contextual Bandit (ICB) problem, in which a learner seeks to optimize a policy while an observer, who cannot access the learner's rewards and only observes actions, aims to recover the underlying problem parameters. During the learning process, the learner's behavior naturally transitions from exploration to exploitation, resulting in non-stationary action data that poses significant challenges for the observer. To address this issue, we propose a simple and effective framew...

---

### 37. Generalization Properties of Score-matching Diffusion Models for Intrinsically Low-dimensional Data

**Authors:** Saptarshi Chakraborty, Quentin Berthet, Peter L. Bartlett

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03700v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03700v1)

**Summary:** Despite the remarkable empirical success of score-based diffusion models, their statistical guarantees remain underdeveloped. Existing analyses often provide pessimistic convergence rates that do not reflect the intrinsic low-dimensional structure common in real data, such as that arising in natural images. In this work, we study the statistical convergence of score-based diffusion models for learning an unknown distribution $μ$ from finitely many samples. Under mild regularity conditions on the...

---

### 38. A Stein Identity for q-Gaussians with Bounded Support

**Authors:** Sophia Sklaviadis, Thomas Moellenhoff, Andre F. T. Martins, et al.

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03673v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03673v1)

**Summary:** Stein's identity is a fundamental tool in machine learning with applications in generative models, stochastic optimization, and other problems involving gradients of expectations under Gaussian distributions. Less attention has been paid to problems with non-Gaussian expectations. Here, we consider the class of bounded-support $q$-Gaussians and derive a new Stein identity leading to gradient estimators which have nearly identical forms to the Gaussian ones, and which are similarly easy to implem...

---

### 39. Riemannian Langevin Dynamics: Strong Convergence of Geometric Euler-Maruyama Scheme

**Authors:** Zhiyuan Zhan, Masashi Sugiyama

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03626v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03626v1)

**Summary:** Low-dimensional structure in real-world data plays an important role in the success of generative models, which motivates diffusion models defined on intrinsic data manifolds. Such models are driven by stochastic differential equations (SDEs) on manifolds, which raises the need for convergence theory of numerical schemes for manifold-valued SDEs. In Euclidean space, the Euler--Maruyama (EM) scheme achieves strong convergence with order $1/2$, but an analogous result for manifold discretizations ...

---

### 40. Extending Neural Operators: Robust Handling of Functions Beyond the Training Set

**Authors:** Blaine Quackenbush, Paul J. Atzberger

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03621v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03621v1)

**Summary:** We develop a rigorous framework for extending neural operators to handle out-of-distribution input functions. We leverage kernel approximation techniques and provide theory for characterizing the input-output function spaces in terms of Reproducing Kernel Hilbert Spaces (RKHSs). We provide theorems on the requirements for reliable extensions and their predicted approximation accuracy. We also establish formal relationships between specific kernel choices and their corresponding Sobolev Native Sp...

---

### 41. Empirical Evaluation of No Free Lunch Violations in Permutation-Based Optimization

**Authors:** Grzegorz Sroka

**Published:** 2026-03-04

🔗 [Paper](http://arxiv.org/abs/2603.03613v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03613v1)

**Summary:** The No Free Lunch (NFL) theorem guarantees equal average performance only under uniform sampling of a function space closed under permutation (c.u.p.). We ask when this averaging ceases to reflect what benchmarking actually reports. We study an iterative-search setting with sampling without replacement, where algorithms differ only in evaluation order. Binary objectives allow exhaustive evaluation in the fully enumerable case, and efficiency is defined by the first time the global minimum is rea...

---

### 42. Controllable Generative Sandbox for Causal Inference

**Authors:** Qi Zhang, Harsh Parikh, Ashley Naimi, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03587v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03587v1)

**Summary:** Method validation and study design in causal inference rely on synthetic data with known counterfactuals. Existing simulators trade off distributional realism, the ability to capture mixed-type and multimodal tabular data, against causal controllability, including explicit control over overlap, unmeasured confounding, and treatment effect heterogeneity. We introduce CausalMix, a variational generative framework that closes this gap by coupling a mixture of Gaussian latent priors with data-type-s...

---

### 43. Solving adversarial examples requires solving exponential misalignment

**Authors:** Alessandro Salvatore, Stanislav Fort, Surya Ganguli

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03507v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03507v1)

**Summary:** Adversarial attacks - input perturbations imperceptible to humans that fool neural networks - remain both a persistent failure mode in machine learning, and a phenomenon with mysterious origins. To shed light, we define and analyze a network's perceptual manifold (PM) for a class concept as the space of all inputs confidently assigned to that class by the network. We find, strikingly, that the dimensionalities of neural network PMs are orders of magnitude higher than those of natural human conce...

---

### 44. Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning

**Authors:** Harin Lee, Kevin Jamieson

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03480v1)

**Summary:** We study reinforcement learning with delayed state observation, where the agent observes the current state after some random number of time steps. We propose an algorithm that combines the augmentation method and the upper confidence bound approach. For tabular Markov decision processes (MDPs), we derive a regret bound of $\tilde{\mathcal{O}}(H \sqrt{D_{\max} SAK})$, where $S$ and $A$ are the cardinalities of the state and action spaces, $H$ is the time horizon, $K$ is the number of episodes, an...

---

### 45. The elbow statistic: Multiscale clustering statistical significance

**Authors:** Francisco J. Perez-Reche

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03235v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03235v1)

**Summary:** Selecting the number of clusters remains a fundamental challenge in unsupervised learning. Existing criteria typically target a single ``optimal'' partition, often overlooking statistically meaningful structure present at multiple resolutions. We introduce ElbowSig, a framework that formalizes the heuristic ``elbow'' method as a rigorous inferential problem. Our approach centers on a normalized discrete curvature statistic derived from the cluster heterogeneity sequence, which is evaluated again...

---

### 46. Scalable Contrastive Causal Discovery under Unknown Soft Interventions

**Authors:** Mingxuan Zhang, Khushi Desai, Sopho Kevlishvili, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03411v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03411v1)

**Summary:** Observational causal discovery is only identifiable up to the Markov equivalence class. While interventions can reduce this ambiguity, in practice interventions are often soft with multiple unknown targets. In many realistic scenarios, only a single intervention regime is observed. We propose a scalable causal discovery model for paired observational and interventional settings with shared underlying causal structure and unknown soft interventions. The model aggregates subset-level PDAGs and app...

---

### 47. A Covering Framework for Offline POMDPs Learning using Belief Space Metric

**Authors:** Youheng Zhu, Yiping Lu

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03191v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03191v1)

**Summary:** In off policy evaluation (OPE) for partially observable Markov decision processes (POMDPs), an agent must infer hidden states from past observations, which exacerbates both the curse of horizon and the curse of memory in existing OPE methods. This paper introduces a novel covering analysis framework that exploits the intrinsic metric structure of the belief space (distributions over latent states) to relax traditional coverage assumptions. By assuming value relevant functions are Lipschitz conti...

---

### 48. Scalable Uncertainty Quantification for Black-Box Density-Based Clustering

**Authors:** Nicola Bariletto, Stephen G. Walker

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03188v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03188v1)

**Summary:** We introduce a novel framework for uncertainty quantification in clustering. By combining the martingale posterior paradigm with density-based clustering, uncertainty in the estimated density is naturally propagated to the clustering structure. The approach scales effectively to high-dimensional and irregularly shaped data by leveraging modern neural density estimators and GPU-friendly parallel computation. We establish frequentist consistency guarantees and validate the methodology on synthetic...

---

### 49. Surprisal-Rényi Free Energy

**Authors:** Shion Matsumoto, Raul Castillo, Benjamin Prada, et al.

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03405v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03405v1)

**Summary:** The forward and reverse Kullback-Leibler (KL) divergences arise as limiting objectives in learning and inference yet induce markedly different inductive biases that cannot be explained at the level of expectations alone. In this work, we introduce the Surprisal-Rényi Free Energy (SRFE), a log-moment-based functional of the likelihood ratio that lies outside the class of $f$-divergences. We show that SRFE recovers forward and reverse KL divergences as singular endpoint limits and derive local exp...

---

### 50. From Reachability to Learnability: Geometric Design Principles for Quantum Neural Networks

**Authors:** Vishal S. Ngairangbam, Michael Spannowsky

**Published:** 2026-03-03

🔗 [Paper](http://arxiv.org/abs/2603.03071v1) | 📄 [PDF](https://arxiv.org/pdf/2603.03071v1)

**Summary:** Classical deep networks are effective because depth enables adaptive geometric deformation of data representations. In quantum neural networks (QNNs), however, depth or state reachability alone does not guarantee this feature-learning capability. We study this question in the pure-state setting by viewing encoded data as an embedded manifold in $\mathbb{C}P^{2^n-1}$ and analysing infinitesimal unitary actions through Lie-algebra directions. We introduce Classical-to-Lie-algebra (CLA) maps and th...

---

