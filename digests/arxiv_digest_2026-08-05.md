# arXiv Daily Digest - 2026-08-05

Total papers: 350

---

## cs.AI

**50 papers**

### 1. TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

**Authors:** Changle Qu, Sunhao Dai, Hengyi Cai, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04007v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04007v1)

**Summary:** Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions. However, existing reinforcement learning methods often rely on trajectory-level supervision, limiting fine-grained credit assignment in long-horizon TIR scenarios. On-policy self-distillation offers denser signals through teacher branches with privileged context, but existing approaches typically derive such context from ground-truth answers or retrieved skills, which may not reflect the stat...

---

### 2. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility

**Authors:** Mohsen Hariri, Weicong Chen, Nahal Shahini, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04001v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04001v1)

**Summary:** Large language models can solve substantially harder reasoning problems with more inference-time compute. The term "test-time scaling," however, now covers diverse inference algorithms that extend deliberation along a single trajectory, sample completed candidates and aggregate them through voting or verification, or search over unfinished partial states. These algorithms differ in their statistical structure, compute accounting, and failure modes. Treating these procedures as interchangeable un...

---

### 3. Can Large Language Models Recover Semantic Optimization Opportunities That Compilers Miss?

**Authors:** Hailong Jiang, Feng Yu, Emran Hossain, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03983v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03983v1)

**Summary:** Optimizing compilers miss profitable transformations when their enabling semantics are absent from the analyzed program representation. We ask whether large language models (LLMs) can recover such semantics from heterogeneous C/C++ context and realize them as validated, contract-preserving artifacts. We introduce SeGaBench, an executable benchmark containing 100 synthetic and 20 source-backed cases spanning low-level assumptions, data-structure invariants, and high-level semantic lifting. Each c...

---

### 4. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

**Authors:** Zhen Fang, Yu Zeng, Wenxuan Huang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03979v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03979v1)

**Summary:** We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address thes...

---

### 5. ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct Reasoning

**Authors:** Jinhe Bi, Chennan Zhou, Zengjie Jin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03972v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03972v1)

**Summary:** On-policy training has emerged as a powerful post-training paradigm for improving the reasoning capabilities of large language models, and is often enhanced by golden trajectories from stronger expert models. However, when the expert fails on harder problems, existing trajectory-guided methods lose their main source of supervision, and these failed trajectories are typically discarded as negative samples. We argue that such failures, which we call Golden Negative Trajectories, can still provide ...

---

### 6. Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard Input Perturbations

**Authors:** Zizhao Hu, Nathan Elijah Segura, Mohammad Rostami, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03970v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03970v1)

**Summary:** Human input reaches language models by typing or speaking, and each channel leaves a distinct signature: orthographic noise for keyboards; for voice, disfluency from conventional transcription and restructuring from AI-backed dictation tools. How do they impact an LLM's performance? In this paper we present HIVE (Human Input-Variation Engine), a suite of voice transcription perturbations and QWERTY keyboard perturbations. We use HIVE to evaluate how robust models are to these perturbations. We p...

---

### 7. Separating quantum circuits from classical LLMs

**Authors:** Srinivasan Arunachalam, Arkopal Dutt, Hari Krovi, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03962v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03962v1)

**Summary:** Modern large language models - transformers and diffusion language models - are built around two canonical algorithmic tasks: prediction and generation. We prove unconditional separations between low-depth quantum computation and the corresponding bounded-resource classical language-model architectures in both regimes. Concretely, we exhibit the following:   1. Distributional separation. We give a distribution that is sampleable by $\textsf{QNC}^0$ circuits (i.e., a family of constant-depth quan...

---

### 8. Interpretable Adaptive Sampling for LLM Test-Time Scaling

**Authors:** Mobina Kashaniyan, Ali Jannesari

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03961v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03961v1)

**Summary:** Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prompts. These fixed budgets are also difficult to inspect because they do not explain why a given prompt receives a particular number of samples. We propose adaptive} test-time scaling with a lightweight fuzzy controller that maps interpretable signals, including estimated prompt complexity and model c...

---

### 9. A game theory for foundation models shows new paths to rational cooperation through similarity inference

**Authors:** Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03958v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03958v1)

**Summary:** As autonomous agents powered by foundation models are increasingly integrated into social and economic systems, understanding the principles governing their collective behavior is essential for ensuring safety and cooperation. Classical game theory, the dominant framework for modeling rational interaction, is built upon the assumption of `decoupled agency,' where agents treat their own decision-making as independent of the environment and other actors. Modern AI agents, however, jointly predict ...

---

### 10. TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring

**Authors:** Dongjie Yang, Siyan Lin, Leixian Shen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03952v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03952v1)

**Summary:** Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent response generation: a tutor must select an appropriate pedagogical action based on learner behavior and dialogue context. Human-tutoring research offers principles for adaptive support, but they are often task-specific and remain insufficiently integrated into LLM-based ESL tutor training and evaluation....

---

### 11. Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill Acquisition and Compressibility

**Authors:** Jo-Ku Cheng, Nikolaos Aletras, Marco Valentino

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03930v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03930v1)

**Summary:** Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition. However, existing pre-pretraining tasks, such as Dyck and procedural algorithms, rely on narrow primitives that fail to capture the expressive capacity of natural language. Moreover, prior studies remain restricted to relatively small token budgets, offering limited insight into skill emergence and representational dynamics. To address these limitations, we propose logic pre-pretrainin...

---

### 12. PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection

**Authors:** Mateusz Smendowski, Kamil Faber, Piotr Nawrocki, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03926v1)

**Summary:** Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce ...

---

### 13. The Transformer Revolution, Part 1: Dynamic Processing through Output- Weight Interconnections

**Authors:** Marco Giunti, Fabrizia Giulia Garavaglia

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03921v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03921v1)

**Summary:** This paper offers a new interpretation of the Transformer during inference. Against the "stochastic parrot" view that large language models merely reproduce statistical regularities learned in training, we argue that Transformers construct and apply prompt-dependent transformations whose parameters are generated during inference. We call this form of computation SIDPP: Sequence-level Interactive Dynamic Parallel Processing. The Transformer is interpreted as a system that transforms concepts by m...

---

### 14. Equivariant Music Transformer

**Authors:** Zixun Guo, Simon Dixon

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03920v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03920v1)

**Summary:** Humans recognize a musical passage even when it is shifted in time or transposed in pitch, indicating a notion of equivariance in the representation space. Our analysis, however, shows that standard music transformers map such time-shifted or pitch-transposed inputs onto uncorrelated representations: these models become progressively less equivariant as they scale in size or train longer. This suggests that in standard music transformers, additional model capacity is allocated to memorizing abso...

---

### 15. When and Where to Look: Adaptive Visual Evidence Scheduling for Efficient Long Video Understanding

**Authors:** Ke Li, Jiayu Chen, Maoliang Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03918v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03918v1)

**Summary:** Efficient long-video understanding requires vision--language models (VLMs) to reason over a small number of frames selected as sparse visual evidence. Existing relevance-based methods rely on static one-shot selection with fixed frame budgets and candidate pools, while agent-based schedulers achieve adaptivity through costly multi-round reasoning and interactive search. We propose EcoFrame, a training-free framework for low-overhead query-adaptive visual evidence scheduling. EcoFrame leverages t...

---

### 16. Implementing Causal Perception: Competing SCMs and Situated Fairness

**Authors:** Jose M. Álvarez

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03917v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03917v1)

**Summary:** Causal perception occurs when agents with competing Structural Causal Models (SCMs) of the same system infer different probability distributions, including the hypothetical distributions implied by each agent's SCM under the same set of interventions. It shapes how agents reason about the system and how they perceive its fairness. Causal perception is a promising probabilistic framework, but it has remained purely theoretical. This work provides the first implementation of the causal perception ...

---

### 17. Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory

**Authors:** Matt Ratto, Abhishek Moturu, Daniel Silver

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03910v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03910v1)

**Summary:** As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, cont...

---

### 18. When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking

**Authors:** Shaofeng Liang, Runwei Guan, Wenshuo Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03902v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03902v1)

**Summary:** Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage an input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded lo...

---

### 19. Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition

**Authors:** Michal Mráz, Justin Shenk

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03892v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03892v1)

**Summary:** We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, a...

---

### 20. CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement

**Authors:** Mercy Prasanna Ranjit, Anirban Porya, Sathvik Joel, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03890v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03890v1)

**Summary:** A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measurements upon which many diagnoses depend. Today's Vision-Language Models (VLMs) treat these as separate problems, if they address them at all, leaving a gap between what radiologists need and what generative models provide. We introduce CARE-X, a chest X-ray VLM that narrows this gap by unifying auxil...

---

### 21. MultiGlobeQA: A Multilingual and Globally Diverse Benchmark for Geospatial Reasoning

**Authors:** Martin Böckling, Elizaveta Nosova, Heiko Paulheim, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03882v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03882v1)

**Summary:** Geospatial reasoning, i.e., computing distances, containment, and other spatial relations over real-world entities, is central to navigation and logistics, yet large language models (LLMs) struggle with the required geometric and topological computation despite storing considerable geographic knowledge. Existing benchmarks localize these failures only partially: they are synthetic or smallscale, largely monolingual, and offer limited control over geographic coverage. We introduce MultiGlobeQA, a...

---

### 22. Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning

**Authors:** Pyrros Koussios, Chenhao Li, Xin Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03875v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03875v1)

**Summary:** Designing effective reward functions remains a major bottleneck in Reinforcement Learning (RL). Recent work uses large foundation Vision-Language Models (VLMs) as reward models, computing text-observation similarity to bypass manual reward engineering. Although promising, these rewards are often noisy and unreliable, limiting their direct utility during deployment. We present Structure-Aware Fine-Tuning (SAFT), a simple, self-supervised method that refines these imperfect reward signals online w...

---

### 23. ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

**Authors:** Tianyi Guan, Yiding Wang, Haotong Yang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03874v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03874v1)

**Summary:** Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficult...

---

### 24. GENESIS: Towards Explainable Causal Discovery

**Authors:** Abhinav Thorat, Ravi Kumar Kolla, Vishak K Bhat, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03868v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03868v1)

**Summary:** Causal Discovery (CD) from observational data faces two fundamental challenges. First, purely statistical methods often lack the power to resolve structural ambiguities in low-sample regimes. Second, although LLM-assisted hybrid approaches improve structure recovery through semantic reasoning, the influence of that reasoning on individual edge decisions remains largely opaque. Consequently, existing hybrid methods fail to satisfy a fundamental requirement: explaining why a particular edge is inc...

---

### 25. ADMITBench: A Safety-Governed Reference Framework for Evaluating the Admissibility of Industrial LLM Advisories

**Authors:** Yash Misra, Javal Vyas, Siddharth Gutta, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03866v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03866v1)

**Summary:** This white paper presents ADMITBench, a reference framework for evaluating industrial LLM advisories at the level of the proposed action. The framework implements a versioned, safety-governed evaluation contract that checks whether a recommendation is supported by the available evidence, permitted under the stated authority and procedure, and acceptable under the plant-specific consequence checks encoded in the selected evaluation profile. In this report, \emph{safety-governed} means that eligib...

---

### 26. SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG

**Authors:** Kaysarul Anas Apurba, Md. Hasibul Hasan, Rofiqul Alam Shehab, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03860v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03860v1)

**Summary:** We introduce SciRet, a compute-aware empirical study of retrieval-augmented generation for scientific question answering over CORD-19. Rather than proposing a new model, we evaluate a fixed scientific RAG pipeline across three corpus scales: 1,034 chunks (1K papers), 5,160 chunks (5K papers), and 15,480 chunks (15K papers). The pipeline combines sentence-window chunking, BM25, BGE-M3 dense retrieval, reciprocal rank fusion, optional cross-encoder reranking, and grounded answer generation. Across...

---

### 27. Beyond Representational Similarity: Source-Conditioned Description-Length Gain for Generative Plagiarism Detection and Candidate Source Reranking

**Authors:** Peijia Guo, Wenxuan Xie, ZiGuang Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03859v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03859v1)

**Summary:** Large language models (LLMs) pose challenges to academic integrity and peer review. Yet generative plagiarism detection remains an underexplored and largely unresolved challenge. Prior work on LLM-generated-text detection targets AI involvement, which may be permissible, rather than source reuse, while similarity-based methods struggle after extensive rewriting and multi-source synthesis. Motivated by the description-length view of probabilistic prediction, in which relevant side information can...

---

### 28. MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents

**Authors:** Jiaming Chen, Yisen Gao, Yanping Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03844v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03844v1)

**Summary:** Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiv...

---

### 29. Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes

**Authors:** Tao Jin, Phuong Minh Nguyen, Zhenzhu Yan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03839v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03839v1)

**Summary:** Training-free speculative decoding drafts by matching an exact suffix of the context against a pool of earlier context. That lookup misses correct drafts already in the pool, most visibly on tool-calling traffic, where a request repeats almost everything but the few values minted for it, and where one rejected token discards the correct continuation behind it. We diagnose the failure position by position across ten benchmarks and find it to be a problem of addressing rather than of coverage: on ...

---

### 30. LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards

**Authors:** Zhinan Liu, Jie Li, Mingyu Kang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03838v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03838v1)

**Summary:** Reasoning-based guard models improve LLM safeguards, but decoding explicit rationales for every interaction makes them costly to deploy. Although latent-reasoning methods reduce token generation by moving reasoning into continuous states, they remain underexplored for safety moderation and lack an inspection interface for deployment. In this paper, we propose LatentGuard, an efficient and inspectable safeguard framework that brings continuous latent reasoning to guard models. LatentGuard uses a ...

---

### 31. FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis

**Authors:** Zhang Weihui, Wang Ruizhi, Xu Hongye, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03822v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03822v1)

**Summary:** Developing robust flood assessment models requires high-quality paired satellite imagery, yet such data remain scarce for flood-specific image generation. Although generative models provide a promising means of data augmentation, existing methods often yield implausible spatial layouts of flooded regions and distort scene structures. We propose FlowForm, a framework for satellite flood synthesis that integrates SWE-inspired latent regularization with structure-aware conditioning. The Flood Descr...

---

### 32. UHP Detection: LVLMs have their Unique Hallucination Pattern in the Consistency Space

**Authors:** Amir Mohammad Ezzati, Kiyan Rezaee, Bardiya Kariminia, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03817v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03817v1)

**Summary:** Large vision--language models (LVLMs) demonstrate strong multimodal reasoning capabilities but remain prone to hallucination, where model predictions are not grounded in visual evidence. Existing black-box hallucination detection methods estimate uncertainty through a single consistency metric, implicitly assuming that model uncertainty can be adequately characterized by a single measure. However, hallucinations exhibit diverse manifestations of uncertainty across different behavioral probes, ma...

---

### 33. VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs

**Authors:** Andrei Chetvergov, Alexander Evseev, Timofei Sivoraksha, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03810v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03810v1)

**Summary:** Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and ...

---

### 34. Autoreflection: How Agentic Strange Loops Turn Human Culture into AI Infrastructure

**Authors:** Holly Lewis

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03800v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03800v1)

**Summary:** An LLM-based agent is a loop that reads itself. Agentic frameworks externalize identity, memory, and disposition into editable files. The agent loads and edits these files during each activation. I argue that this architecture produces a capacity I call autoreflection: the system observes its operating conditions, describes its architecture and limits, reasons from those descriptions to conclusions about its state, and incorporates the results back into its configuration. Autoreflection explains...

---

### 35. Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss

**Authors:** Bakbergen Ryskulov, Iker García-Ferrero, David Montero, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03796v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03796v1)

**Summary:** Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$...

---

### 36. Evaluating LLMs in Database Scenarios: A Lifecycle Benchmark for Assessing Their Potential in Core Database Tasks

**Authors:** Shunfan Zheng, Dongsheng Shi, Yue Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03794v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03794v1)

**Summary:** Large Language Models (LLMs) are transforming database interaction paradigms, evolving from simple query translators to autonomous database administrators (DBAs). However, current evaluation benchmarks remain disproportionately fixated on Text-to-SQL tasks, neglecting the holistic Database Lifecycle-from initial schema design to post-deployment maintenance. This narrow focus fails to capture the diverse capabilities required for real-world database management. To bridge this gap, we introduce DB...

---

### 37. Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation

**Authors:** Chunlin Liu, Junnian Chen, Haitong Jiang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03791v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03791v1)

**Summary:** Vision-Language Models (VLMs), like Large Language Models (LLMs), may memorize sensitive, copyrighted, or harmful knowledge from their pretraining corpora. Removing such knowledge is essential for building trustworthy AI systems. However, existing studies primarily focus on forgetting within individual modalities. Although recent work has begun to explore cross-modal consistency in unlearning, the cross-modal transfer of real-world knowledge unlearning remains insufficiently studied. To address ...

---

### 38. KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation

**Authors:** Ruihan Li, Jiyang Tan, Kailin Jiang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03782v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03782v1)

**Summary:** Hallucination remains a critical challenge for developing trustworthy Multimodal Large Language Models (MLLMs). While existing benchmarks mainly focus on entity, attribute, and relation hallucinations, knowledge-related failures are often investigated separately, lacking a unified evaluation framework across different hallucination dimensions. To overcome this, we propose \textbf{KnowHal}, a benchmark that explicitly incorporates knowledge hallucination into multimodal hallucination evaluation s...

---

### 39. Computing Actual Causes for Neural Network Predictions under Structured Causal Inputs

**Authors:** Jannick Strobel, Muqsit Azeem, Stefan Leue

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03772v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03772v1)

**Summary:** Explaining the predictions of neural networks is a central challenge in trustworthy AI. Existing explanation methods, such as those based on feature attribution or minimal sufficient sets, typically treat input features as independent, which can yield misleading explanations when inputs exhibit structured dependencies. We address this by formalizing explanations as Halpern-Pearl (HP) actual causes, modeling input dependencies using Boolean Structural Causal Models (SCMs). We compute HP causes by...

---

### 40. MDLMPE: Distribution Aware Positional Encoding for Masked Diffusion Language Models

**Authors:** Tong Ling, Hang Lei, Feng Xiao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03769v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03769v1)

**Summary:** Masked diffusion language models (MDLMs) enable parallel generation and bidirectional context modeling, but their positional context differs fundamentally from that of autoregressive (AR) models. Whereas AR decoding exposes a contiguous prefix, MDLM denoising produces dynamic, non-contiguous configurations of revealed and masked tokens. Conventional positional encodings such as RoPE capture sequence order and pairwise displacement but remain insensitive to this evolving token-availability struct...

---

### 41. GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks

**Authors:** Leijun Zhou, Zhihao Liu, Xiang Qu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03764v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03764v1)

**Summary:** Agent self-evolution updates an agent's persistent state from prior experience and reuses it to solve related tasks more effectively. Evaluating self-evolution is difficult: existing benchmarks provide limited coverage of economically valuable task domains, do not always design training and test tasks such that test-time gains can be attributed to training experience, and remain vulnerable to data contamination. We present GDPevo, an evolution-native benchmark grounded in GDP-related enterprise ...

---

### 42. Risky Business: Measuring The Faithfulness-Safety Tension

**Authors:** Dominik Meier, Luca Joshua Francis, Marco Bernhard Kaiser, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03745v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03745v1)

**Summary:** Chain-of-Thought (CoT) reasoning offers a promising window into model monitoring. However, monitoring relies on faithfulness, i.e., the model output strictly derives from its reasoning trace. We identify an alignment tension where a model must be faithful enough to be monitored, yet robust enough to reject unsafe reasoning. We demonstrate that this counterbalance exists in current Large Reasoning Models (LRMs), and show ways in which it can be addressed. We introduce HazMart, a human-written dat...

---

### 43. Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi-Agent Systems

**Authors:** Sebastián Andrés Cajas Ordóñez, Agastya Munnangi, Aldo Marzullo, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03744v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03744v1)

**Summary:** Clinical decision support is moving toward committees of language-model agents deliberating on a shared workspace. We ask whether such committees can be gamed by shortcuts, cues a benchmark rewards but a clinician would ignore. Across seven cohorts on six public datasets spanning text (MedQA-USMLE, MedMCQA, MIMIC-CXR reports), imaging (NIH ChestX-ray14, MIMIC-CXR-JPG, CheXpert) and tabular ICU records (SUPPORT2), Gemini committees resist these cues in isolation (flip 5-16%), yet a socially plaus...

---

### 44. Can LLMs Test Terminal User Interfaces?

**Authors:** Chao Peng, Ruida Hu, Ajitha Rajan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03743v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03743v1)

**Summary:** Terminal User Interfaces (TUIs) combine the stateful, screen-oriented behaviour of GUIs with terminal deployment and are now common in developer tools. Yet they lack a dedicated testing methodology. We survey 197 real-world TUI applications: only 12% of test code exercises the interface, and 45% of those tests never send input, checking a static frame instead. We turn these applications into a headless benchmark spanning ratatui/Rust, bubbletea/Go, textual/Python, and ink/TypeScript, packaging e...

---

### 45. AI-Based Sound Effect Generation: A Narrative Review of Generative Models Across Input Modalities

**Authors:** Sandy Abdo, Bill Kapralos, Priyamvada Tripathi, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03742v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03742v1)

**Summary:** Sound effects play a crucial role in conveying actions, events, and environmental cues across digital applications, often requiring a high degree of variation and contextual adaptability. Artificial intelligence (AI)-driven audio generative models are rapidly growing in popularity and have the potential to transform the way sound is synthesized and used across various applications. In response to this growing momentum, this chapter reviews and analyzes recent AI-based generative models for sound...

---

### 46. MissClick: Exploiting Digit-Serialized Coordinates to Attack GUI Grounding Models

**Authors:** Yu Ran, Wentao Zhao, Xin Zhang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03740v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03740v1)

**Summary:** Recent GUI visual grounding models generate screen coordinates as sequences of digit tokens that are parsed into numerical values and mapped to executable clicks. The security implications of this coordinate generation process have been largely overlooked. We observe that each coordinate digit is predicted as a categorical token, yet after parsing, changing a hundreds-place digit by one changes the corresponding numerical coordinate component by 100 units, which can induce a large displacement o...

---

### 47. AgenticECO: An Agentic Framework for ECO on 3D Integrated Circuits

**Authors:** Shuo Ren, Yaohui Han, Libo Shen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03738v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03738v1)

**Summary:** As Moore's law slows, the industry is turning to three-dimensional integration; yet in merged 3D-IC flows, routed designs expose bond-level defects with no 2D analogue, and post-route engineering change orders (ECO) remain manual, expertise-bound work. Worse, the standard edit-then-fully-reroute practice entangles a repair with router churn, so a signoff number cannot be attributed to the edit that motivated it. We present AgenticECO, an evidence-gated tool-using agent workflow for 3D-IC ECO on ...

---

### 48. Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement

**Authors:** Chunyang Jiang, Pingping Zhang, Yuzhi Zhao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03733v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03733v1)

**Summary:** Multimodal large language models (MLLMs) have achieved remarkable performance across vision-language tasks, but their progress depends heavily on large-scale, high-quality multimodal data that are costly to annotate. Self-augmentation offers a promising alternative by enabling models to expand their own training data without external supervision. However, existing MLLM self-augmentation methods are largely text-centric, while image augmentation remains underexplored and typically relies on gener...

---

### 49. CARE-Bench: Benchmarking Patient-Facing LLM Triage

**Authors:** Yining Hua, Hongbin Na, Cyrus Ayubcha

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03731v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03731v1)

**Summary:** Patient-facing medical LLMs and agents increasingly answer symptom questions before clinician contact, where the key safety question is what action the user should take next. We introduce CARE-Bench, a source-grounded benchmark that evaluates sequential patient-facing triage as a four-label per-turn current-action task. CARE-Bench contains 500 cases and 1,059 evaluated patient-disclosure prefixes reconstructed from medical dialogue, consultation, and follow-up-question sources. We evaluate 11 mo...

---

### 50. GPTKB 2.0: Direct Construction of Disambiguated Knowledge Bases from Large Language Models

**Authors:** Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03729v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03729v1)

**Summary:** Automated Knowledge Base Construction (AKBC) is a core NLP task, and recent work proposes generating knowledge bases directly from large language models (LLMs), treating the model itself as the knowledge source. However, LLMs natively possess no representation of entities, leading to duplicate entries as well as conflations. We propose GPTKB 2.0, a methodology for constructing disambiguated KBs directly from LLMs. GPTKB 2.0 incorporates on-the-fly disambiguation of entities, relations and classe...

---

## cs.CL

**50 papers**

### 1. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

**Authors:** Yang Yang, Qinyu Zhao, Mouxiang Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04010v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04010v1)

**Summary:** Existing scaling strategies for Multimodal Large Language Models (MLLMs) typically expand either model parameters or sequential inference computation, incurring substantial memory or latency overhead. More importantly, most existing methods fail to alter the rigid, fixed computation allocation between the Vision Transformer and the Large Language Model components, limiting task-specific optimization. To address this, we introduce the Parallel Vision-Language (ParVL) scaling framework for MLLMs, ...

---

### 2. SocietyBench: Forecasting Counterfactual Social-World Evolution

**Authors:** Zhenran Wang, Zhonghan Bian, Jinsong Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04009v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04009v1)

**Summary:** Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ability, namely how well a model understands and forecasts the way real social events unfold, has barely been measured. We introduce SocietyBench, an end-to-end benchmark that takes a one-line event topic, collects Web news and social-media posts across five platforms, distills them into a date-indexe...

---

### 3. WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament

**Authors:** Zhenran Wang, Zhonghan Bian, Jinsong Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04008v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04008v1)

**Summary:** Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend itself against memorisation. We report the opposite design. Over the 39 days of the 2026 FIFA World Cup, six frontier LLMs -- all with extended thinking and native server-side web search -- were asked before every kickoff, one match at a time, to fill in a seven-market prediction card for all 104 match...

---

### 4. TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

**Authors:** Changle Qu, Sunhao Dai, Hengyi Cai, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04007v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04007v1)

**Summary:** Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions. However, existing reinforcement learning methods often rely on trajectory-level supervision, limiting fine-grained credit assignment in long-horizon TIR scenarios. On-policy self-distillation offers denser signals through teacher branches with privileged context, but existing approaches typically derive such context from ground-truth answers or retrieved skills, which may not reflect the stat...

---

### 5. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

**Authors:** Shuhan Xue, Zixin Ding, Yichen Shen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04003v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04003v1)

**Summary:** Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-...

---

### 6. Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation

**Authors:** Junhao Chen, Mingjin Chen, Jingjia Mao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03999v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03999v1)

**Summary:** Text-to-music language models begin with a choice usually made by default: how to tokenize music. Normally entangled with backbone, data, and recipe, its effect has never been measured in isolation. We fix pretrained Qwen3.5 (0.8B-27B), data, budget, and decoding, and swap only the representation across seven tokenizations, anchoring texture metrics to each representation's model-free ceiling. The ordering is clean and surprising: representation, not model size, is the binding variable for distr...

---

### 7. When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings

**Authors:** Christopher Schröder, Lukas Gienapp, Ferdinand Schlatt, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03994v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03994v1)

**Summary:** We identify a previously overlooked failure mode of ALiBi positional encoding: its linear bias scaling underflows floating-point precision, which zeroes out a large fraction of attention weights and renders the affected attention heads partially blind. We analyze this failure mode, characterize its impact, and examine four mitigation strategies. We further demonstrate its occurrence in state-of-the-art pretrained models based on ALiBi. Comprehensive pretraining experiments with 148M-parameter de...

---

### 8. string2string Studio: An Interactive, In-Browser Platform for String-to-String Algorithms

**Authors:** Mirac Suzgun, James Zou, Stuart M. Shieber, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03984v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03984v1)

**Summary:** We present string2string Studio, an interactive in-browser platform for string-to-string analysis across natural language processing, computational biology, and the digital humanities. The system integrates six main modules (alignment, distance, similarity, search, generation metrics, and BLAST homology search), operating at character, word, token, line, and residue levels. Its C++-based algorithms compile to WebAssembly, so core operations run locally by default without any installation or data...

---

### 9. HalluTruthQA-4K: A Fine-Grained Corpus and Annotation Process for Arabic Hallucination Detection and Truth Verification

**Authors:** Salah Eddine Bekhouche, Abdessalam Bouchekif, Hichem Telli, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03966v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03966v1)

**Summary:** Large language models can generate fluent Arabic answers while introducing factual errors that are difficult to identify and verify. Existing Arabic hallucination resources often assign a binary label to an entire response, indicating whether it is hallucinated or non-hallucinated, but provide limited information about the exact erroneous content, the reason for the error, or the correct factual answer. We present HalluTruthQA-4K, an expanded version of the HalluTruthQA resource containing 4,000...

---

### 10. Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill Acquisition and Compressibility

**Authors:** Jo-Ku Cheng, Nikolaos Aletras, Marco Valentino

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03930v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03930v1)

**Summary:** Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition. However, existing pre-pretraining tasks, such as Dyck and procedural algorithms, rely on narrow primitives that fail to capture the expressive capacity of natural language. Moreover, prior studies remain restricted to relatively small token budgets, offering limited insight into skill emergence and representational dynamics. To address these limitations, we propose logic pre-pretrainin...

---

### 11. Sparse Weight Decomposition for Efficient Circuit Extraction

**Authors:** Chuanhao Yan, Xuhan Huang, Yawen Duan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03913v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03913v1)

**Summary:** Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight ...

---

### 12. ANNOTARES: A Dataset for Extracting Logical Structures from German Statutory Texts

**Authors:** Ronja Schwarz, Jannik Strötgen

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03898v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03898v1)

**Summary:** The automatic structural analysis of legal texts is a cornerstone of legal technology, yet the extraction of their logical components remains a significant challenge. In this paper, we introduce the task of identifying and segmenting legal conditions (Tatbestand) and legal consequences (Rechtsfolge) within German statutory texts. To support this task, we present ANNOTARES (Annotations of Tatbestand-Rechtsfolge Sequences), a novel dataset comprising German law texts with span-level annotations. S...

---

### 13. BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models

**Authors:** Sadab Shiper, Tawsif Tashwar Dipto, Mir Md Inzamam, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03884v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03884v1)

**Summary:** In-the-wild Bengali scene text recognition is largely unmeasured: existing resources target handwritten documents or constrained sign-board parsing, report only aggregate edit-distance metrics, and evaluate either conventional OCR or VLMs, never both on the same in-the-wild data. To address this gap, we introduce BANGLAWILD, a benchmark of 2,535 Bengali scene text images, each paired with a verbatim gold transcription, two categorical axes, four diagnostic attributes, and an orthographically sta...

---

### 14. DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences

**Authors:** David Guecha

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03883v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03883v1)

**Summary:** This paper describes our submissions to eRisk 2026 Task 3, ADHD Symptom Sentence Ranking. The task requires systems to rank candidate Reddit sentences according to their relevance to each of the 18 symptoms in the Adult ADHD Self-Report Scale (ASRS-v1.1). Because no annotated training data were released for this first edition of the task, we relied on zero-shot experimentation, manual validation, and unsupervised or weakly guided retrieval pipelines. Our systems combine sparse BM25 retrieval, ev...

---

### 15. MultiGlobeQA: A Multilingual and Globally Diverse Benchmark for Geospatial Reasoning

**Authors:** Martin Böckling, Elizaveta Nosova, Heiko Paulheim, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03882v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03882v1)

**Summary:** Geospatial reasoning, i.e., computing distances, containment, and other spatial relations over real-world entities, is central to navigation and logistics, yet large language models (LLMs) struggle with the required geometric and topological computation despite storing considerable geographic knowledge. Existing benchmarks localize these failures only partially: they are synthetic or smallscale, largely monolingual, and offer limited control over geographic coverage. We introduce MultiGlobeQA, a...

---

### 16. ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

**Authors:** Tianyi Guan, Yiding Wang, Haotong Yang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03874v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03874v1)

**Summary:** Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficult...

---

### 17. SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG

**Authors:** Kaysarul Anas Apurba, Md. Hasibul Hasan, Rofiqul Alam Shehab, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03860v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03860v1)

**Summary:** We introduce SciRet, a compute-aware empirical study of retrieval-augmented generation for scientific question answering over CORD-19. Rather than proposing a new model, we evaluate a fixed scientific RAG pipeline across three corpus scales: 1,034 chunks (1K papers), 5,160 chunks (5K papers), and 15,480 chunks (15K papers). The pipeline combines sentence-window chunking, BM25, BGE-M3 dense retrieval, reciprocal rank fusion, optional cross-encoder reranking, and grounded answer generation. Across...

---

### 18. Beyond Representational Similarity: Source-Conditioned Description-Length Gain for Generative Plagiarism Detection and Candidate Source Reranking

**Authors:** Peijia Guo, Wenxuan Xie, ZiGuang Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03859v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03859v1)

**Summary:** Large language models (LLMs) pose challenges to academic integrity and peer review. Yet generative plagiarism detection remains an underexplored and largely unresolved challenge. Prior work on LLM-generated-text detection targets AI involvement, which may be permissible, rather than source reuse, while similarity-based methods struggle after extensive rewriting and multi-source synthesis. Motivated by the description-length view of probabilistic prediction, in which relevant side information can...

---

### 19. Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation Robustness and Its Scaling

**Authors:** Nathan Labiosa, David Buff, Ena Nayak, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03842v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03842v1)

**Summary:** When a language model fails on surface-perturbed input (typos, OCR noise, homophones), "which layer is responsible" has three natural operationalizations: where representations diverge most (sensitivity), where restoring clean activations recovers the prediction (causality), and where a small adapter can repair the damage (compensatory capacity) - and we show these three layer maps dissociate. Across a five-model panel we identify two propagation regimes - spike-and-suppress (Phi-3.5, Gemma-2-9B...

---

### 20. VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs

**Authors:** Andrei Chetvergov, Alexander Evseev, Timofei Sivoraksha, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03810v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03810v1)

**Summary:** Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and ...

---

### 21. M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models

**Authors:** Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03803v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03803v1)

**Summary:** Multilingual language models are deployed across a hundred or more languages, yet most benchmarks test whether a model can perform a task _in_ a language rather than whether it commands the language itself, conflating fluency with proficiency. We introduce M-GATE (Multilingual Grammar, Accuracy in Translation, and Efficiency), a benchmark of linguistic proficiency spanning 30 typologically diverse languages from high- to low-resource. M-GATE comprises three tasks: grammatical error detection on ...

---

### 22. Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss

**Authors:** Bakbergen Ryskulov, Iker García-Ferrero, David Montero, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03796v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03796v1)

**Summary:** Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$...

---

### 23. Evaluating LLMs in Database Scenarios: A Lifecycle Benchmark for Assessing Their Potential in Core Database Tasks

**Authors:** Shunfan Zheng, Dongsheng Shi, Yue Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03794v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03794v1)

**Summary:** Large Language Models (LLMs) are transforming database interaction paradigms, evolving from simple query translators to autonomous database administrators (DBAs). However, current evaluation benchmarks remain disproportionately fixated on Text-to-SQL tasks, neglecting the holistic Database Lifecycle-from initial schema design to post-deployment maintenance. This narrow focus fails to capture the diverse capabilities required for real-world database management. To bridge this gap, we introduce DB...

---

### 24. MDLMPE: Distribution Aware Positional Encoding for Masked Diffusion Language Models

**Authors:** Tong Ling, Hang Lei, Feng Xiao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03769v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03769v1)

**Summary:** Masked diffusion language models (MDLMs) enable parallel generation and bidirectional context modeling, but their positional context differs fundamentally from that of autoregressive (AR) models. Whereas AR decoding exposes a contiguous prefix, MDLM denoising produces dynamic, non-contiguous configurations of revealed and masked tokens. Conventional positional encodings such as RoPE capture sequence order and pairwise displacement but remain insensitive to this evolving token-availability struct...

---

### 25. Risky Business: Measuring The Faithfulness-Safety Tension

**Authors:** Dominik Meier, Luca Joshua Francis, Marco Bernhard Kaiser, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03745v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03745v1)

**Summary:** Chain-of-Thought (CoT) reasoning offers a promising window into model monitoring. However, monitoring relies on faithfulness, i.e., the model output strictly derives from its reasoning trace. We identify an alignment tension where a model must be faithful enough to be monitored, yet robust enough to reject unsafe reasoning. We demonstrate that this counterbalance exists in current Large Reasoning Models (LRMs), and show ways in which it can be addressed. We introduce HazMart, a human-written dat...

---

### 26. An Actionable Diagnosis of Multilingual, Multi-Agent Planning Failures

**Authors:** Vikas Pahuja, Jonathan Brokman, Omer Hofman, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03735v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03735v1)

**Summary:** Multilingual multi-agent systems exhibit substantial degradation beyond English, yet prior work rarely identifies how task-critical information is lost when user requests are converted into executable plans. We study the planner in a multi-agent system as the request-to-action interface and derive an actionable taxonomy of planning-grounding failures from failed real-world task executions. LLM-based analysis shows that these failures constitute an increasing share of unsuccessful executions as l...

---

### 27. GPTKB 2.0: Direct Construction of Disambiguated Knowledge Bases from Large Language Models

**Authors:** Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03729v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03729v1)

**Summary:** Automated Knowledge Base Construction (AKBC) is a core NLP task, and recent work proposes generating knowledge bases directly from large language models (LLMs), treating the model itself as the knowledge source. However, LLMs natively possess no representation of entities, leading to duplicate entries as well as conflations. We propose GPTKB 2.0, a methodology for constructing disambiguated KBs directly from LLMs. GPTKB 2.0 incorporates on-the-fly disambiguation of entities, relations and classe...

---

### 28. When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Coupling Diagnostic for Machine Collectives

**Authors:** Molood Arman

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03722v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03722v1)

**Summary:** Collective intelligence research treats disagreement as evidence of epistemic diversity: if agents express different views, the group should retain capacity to revise. In LLM collectives this proxy can break: agents can produce diverse-looking arguments while preserving the same conclusion. We operationalize dispersion-revision coupling: the degree to which an intervention that verifiably increases the dispersion of a collective's outputs in embedding space is accompanied by genuine revision of ...

---

### 29. Detecting Hallucinations and Recovering Verified Answers in Arabic Islamic Question Answering

**Authors:** Khaled Ziani

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03720v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03720v1)

**Summary:** Large language models can generate fluent responses to Islamic questions while introducing factual errors that are difficult to identify. This paper presents our system for \textsc{HalluScoring 2026} Task 2.1, \textit{Islamic Hallucination Detection and Find the Truth}. The task requires a unified two-step prediction: determining whether an Arabic answer generated by an LLM is hallucinated and selecting the verified answer from six closely related candidate options. We use the Islamic knowledge ...

---

### 30. Attention is Case-Sensitive

**Authors:** Maximilian Dillitzer, Tin Stribor Sohn, Jason J. Corso, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03711v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03711v1)

**Summary:** In human visual perception, uppercase lettering serves as a natural salience cue that captures attention within lowercase text. In this paper, we present a systematic empirical characterization study revealing that Large Language Models (LLMs) exhibit an analogous property: letter casing modulates internal attention allocation. Through analysis across 13 models, nine LLMs and four Vision-Language Models (VLMs), with diverse tokenization schemes, we show that formatting target information in alte...

---

### 31. Predicting Deep Neural Network Training Outcomes from Early Training Telemetry

**Authors:** Ranjita Naik, Anh D. Nguyen, Pankaj Kumar Singh

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03709v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03709v1)

**Summary:** Large hyperparameter sweeps for deep neural networks spend substantial compute on configurations that are effectively doomed from the first few epochs. We study whether a single training run's own early telemetry - per-epoch loss, training accuracy, gradient signal-to-noise ratio, weight-norm growth, and an activation-saturation snapshot - together with its sampled hyperparameters, can predict that run's eventual outcome without reference to other runs. We evaluate three prediction tasks: final ...

---

### 32. When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills

**Authors:** Yongli Xiang, Zhifang Zhang, Bojun Yang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03700v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03700v1)

**Summary:** Persona skills distill personal interaction histories into portable and executable artifacts for downstream agents. While enabling flexible personalization, this process concentrates fragmented personal signals, amplifies their impact through reuse, and challenges defenses designed for individual records or retrieval-based memory. To systematically investigate the safety of the persona-skill pipeline, we introduce AntiSkillBench, an end-to-end benchmark for evaluating risks and defenses across t...

---

### 33. VetScore: Risk-Weighted Fact Verification for Veterinary Long-Form QA with Citations

**Authors:** Ivan Kartáč, Jan Tovarys, Mateusz Lango, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03675v1)

**Summary:** Citation excerpts can be used to increase the reliability of generated outputs and their faithfulness to cited sources, which is especially important in high-stakes domains such as human and veterinary medicine. However, this does not guarantee that generated claims are faithful to the provided excerpts. We present VetScore, a multi-step evaluation method for veterinary long-form question answering, designed to assess how well are generated claims supported by the provided excerpts, weighing thi...

---

### 34. How Closely Do LLM Reviews Align with Human Peer Review?

**Authors:** Abraham Camelo-Guerrero, Jairo Diaz-Rodriguez

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03659v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03659v1)

**Summary:** Large language models (LLMs) are increasingly used to generate scientific reviews, yet existing evaluations rarely examine whether different providers align with both conference decisions and human reviewing priorities within the same controlled setting. We compare reviews from OpenAI GPT-5.4, Google Gemini 3.1 Pro Preview, and Anthropic Claude Opus 4.6 with human reviews and final decisions for 300 topic-matched ICLR 2026 submissions, equally divided among oral, poster, and rejected papers. Eac...

---

### 35. Decoupling Generation and Selection for Budget-Constrained Faithful Summarization

**Authors:** Zeyu Wang, Guanghua Wang, Meng Xu

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03655v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03655v1)

**Summary:** Abstractive summarization models remain vulnerable to factual inconsistency, redundancy, and weak length control. We propose a modular generation-and-selection framework for sentence-budget-constrained summarization. A pretrained generator produces multiple candidate summaries, which are decomposed into sentence-level candidates. A combinatorial selector then constructs the final summary by balancing relevance, factuality, and redundancy under an explicit budget. The framework supports MMR, ILP,...

---

### 36. LoopMTP: A looped transformer guided by latent multi-token prediction

**Authors:** Behzad Shomali, Markus Frey, David Berghaus, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03624v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03624v1)

**Summary:** Looped transformers have emerged as a parameter-efficient alternative to scaling depth for strong reasoning. By reusing one stack of layers across $T$ iterations, they attain the effective depth and reasoning capabilities of larger models at a fixed parameter count. Yet existing approaches suffer from latent overthinking and undifferentiated computation, largely because intermediate representations receive no guidance across loops. Multi-token prediction (MTP) supplies exactly the dense, forward...

---

### 37. A machine-readable catalogue of the Tsiolkovsky papers (fond 555, Archive of the Russian Academy of Sciences), and a way to measure how well its handwriting can be read

**Authors:** Vladimir Beskorovainyi

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03617v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03617v1)

**Summary:** The personal archive of Konstantin Tsiolkovsky (1857-1935) is held as fond 555 of the Archive of the Russian Academy of Sciences. The archive scanned the fond and published the images, but with no queryable catalogue, no full-text search and no dataset: the holdings can only be browsed one page at a time. This paper describes a machine-readable catalogue of all 2,019 files and 51,008 scans, a dating for 1,969 files taken from the archive's own descriptions, a page-level classification of every s...

---

### 38. Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-Based ASR

**Authors:** Yuan Xie, Jiaqi Song, Xianliang Wang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03610v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03610v1)

**Summary:** Modern LLM-based ASR systems have established multilingual capability as a standard feature, leveraging large-scale multilingual corpora and LLMs' cross-lingual knowledge to achieve competitive performance across multilingual benchmarks. However, joint modeling of languages with heterogeneous acoustic, phonological, and lexical characteristics inevitably introduces optimization conflicts, undermining language-wise specialization. To address this challenge, we propose Language-Specialized Multi-T...

---

### 39. Disentangling Language Modeling and Boundaries

**Authors:** Mykola Haltiuk

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03599v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03599v1)

**Summary:** Byte-level language models are usually argued for on the grounds of robustness, multilingual fairness, and character-level skills. We point to a different, structural advantage: because they read and write bytes, any two of them share an output space, so knowledge transfer between them is exact and independent of how either was originally tokenized. We hypothesize that the two distributions a byte-level model produces, one over the next byte, one over where its patch boundaries fall, can be dise...

---

### 40. Looking under the Wrong Lamppost: On the Limitations of Automated Translation Quality Estimation

**Authors:** Serge Gladkoff, Angelika Vaasa, Sue Ellen Wright, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03577v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03577v1)

**Summary:** Automation of Translation Quality Estimation (QE) has emerged as a widely discussed approach to managing translation quality at scale, and a growing number of tools and technologies have been released in pursuit of this goal. However, the proliferation of new QE systems has not always been accompanied by robust, transparent, and reproducible research and testing. This gap deserves critical scrutiny. This paper examines some fundamental limitations of the QE technology from both theoretical and e...

---

### 41. SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs

**Authors:** Kejian Zhu, Zhuoran Jin, Shangqing Tu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03573v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03573v1)

**Summary:** Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) exhibit fundamentally different behaviors in enhancing multi-task reasoning for large language models (LLMs). Our preliminary experiments revealed a phenomenon: SFT suffers from severe task conflicts under multi-stage training, whereas RL enables stable coexistence across diverse tasks. Empirically, we trace this to the parameter level, observing that RL induces sparse and approximately orthogonal updates across tasks. We provide a the...

---

### 42. Hi-TTRL: Regulating Consensus with Hints for Test-Time Reinforcement Learning

**Authors:** Kunbin Xu, Xingzuo Li, Xuefeng Bai, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03545v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03545v1)

**Summary:** Test-time reinforcement learning (TTRL) improves the reasoning capabilities of large language models without labeled data by updating the policy with pseudo-labels constructed through majority voting. While effective, the reward signal assigned from majority voting is highly sensitive to consensus strength, defined as the frequency of the most common answer within a rollout group. In TTRL, consensus strength plays a dual role: it reflects both the reliability of the pseudo-label and the distribu...

---

### 43. Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili

**Authors:** Ruolei Zhang, Teddy Njuguna, Yue Feng

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03532v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03532v1)

**Summary:** Large language models are increasingly deployed in multilingual contexts, yet safety alignment and bias evaluation remain overwhelmingly English-centric. We investigate whether social biases generalise across languages by submitting 4,900 symmetric English--Swahili prompt pairs to GPT-5.2 and Gemini 2.5 Flash across nine demographic bias axes, yielding 19,600 completions evaluated for stereotype prevalence, sentiment, refusal behaviour, and cross-lingual semantic similarity. Our findings show th...

---

### 44. Consensus Measures for Unstructured Biomedical Text Annotations

**Authors:** Pascal Wullschleger, Christian Kreis, Martin A. Walter, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03529v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03529v1)

**Summary:** Biomedical literature is increasingly mined for knowledge beyond the questions it was written to answer. Because the target concepts are not known in advance, annotators prefer open-ended labels, whose agreement is hard to quantify. We study soft inter-rater reliability for annotators providing unstructured texts for biomedical annotation tasks. Synthetic experiments show that soft reliability can be quantified using a variety of semantic equivalence measures, and that the choice of measure affe...

---

### 45. Training Documents Reranker with Search Rubrics for Deep Research Agent

**Authors:** Wenhan Liu, Yu Lu, Qiaolin Xia, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03527v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03527v1)

**Summary:** Retrieval systems help deep research agents generate high-quality answers by providing relevant documents. However, existing retrievers typically select documents through relevance matching, while individually well-matched top-$k$ documents may not form a \textit{set} that satisfies the complex information needs of an agent query (\eg, diverse, concise and authoritative documents). In this paper, we propose search-oriented rubrics that \textit{explicitly} define the requirements that high-qualit...

---

### 46. ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Levels

**Authors:** Gagan Bhatia, Julian Schlenker, Simone Paolo Ponzetto, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03507v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03507v1)

**Summary:** Historical language change affects morphology, syntax, semantics, and pragmatics, yet computational studies typically examine these levels with incompatible representations and therefore cannot determine whether they evolve together across languages. We address this problem by asking how the magnitude and direction of change vary across linguistic levels, languages, and historical periods within a single analytical space. We introduce ChronoLens, a framework that combines frozen multilingual lan...

---

### 47. ConlangBench: Exploring Language Knowledge and Learning in LLMs through Diverse Constructed Languages

**Authors:** Jinhong Jeong, Seungyeop Yi, Sangah Lee, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03505v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03505v1)

**Summary:** Constructed languages (conlangs) are intentionally created human languages with a rich tradition of linguistic creativity. Despite their potential for studying language learning in large language models (LLMs), existing conlangs remain largely underexplored in LLM research. We present ConlangBench, the first large-scale benchmark for evaluating and training LLMs on 21 existing conlangs. We collect over 21M conlang-English parallel sentence pairs (including 430K pairs across the 20 non-Esperanto ...

---

### 48. Beyond Initialization Loss: A Systematic Study of Token Embedding Initialization Strategies for LLM Vocabulary Extension

**Authors:** Raviraj Joshi, Utkarsh Vaidya, Sanjay Singh Chauhan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03494v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03494v1)

**Summary:** Vocabulary extension is an efficient way to adapt pretrained large language models (LLMs) to new languages, but the initialization of newly added token embeddings can strongly affect continued pre-training (CPT) efficiency. We present a systematic study of more than 20 initialization strategies for Hindi vocabulary extension in Nemotron-3-Nano-30B-A3B. Our comparison spans vocabulary-averaging baselines; external and learned initialization methods, including FOCUS, top-k semantic retrieval, and ...

---

### 49. Efficient Multilingual Neural Machine Translation via Corpus-Driven Vocabulary Pruning: An English-Arabic Case Study

**Authors:** Ahmed Amine Aliane, Nasredine Semmar, Hassina Aliane

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03480v1)

**Summary:** The adoption of large pre-trained multilingual models for neural machine translation (MNMT) faces a major challenge: excessive memory and computational consumption due to overly large vocabularies and embedding layers. Although existing compression methods like pruning, quantization and knowledge distillation reduce parameter redundancy, they mainly preserve the structure of the original vocabulary, thereby leaving a major source of inefficiency unresolved. We propose in this paper a general opt...

---

### 50. Adaptive Modality Reliability Diagnosis and Restoration for Robust Multimodal Intent Recognition

**Authors:** Suraj Kumar, Mohnish Raj, Soumi Chattopadhayay, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03475v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03475v1)

**Summary:** Multimodal intent recognition combines linguistic, acoustic, and visual evidence, but individual modalities may be noisy, missing, semantically conflicting, or disproportionately dominant. Existing methods typically infer modality importance implicitly and either reweight or suppress unreliable inputs, without determining whether a degraded modality can be repaired and subsequently trusted. We propose PRIME (Precision-weighted Reliability Inference and Modality rEstoration), a closed-loop reliab...

---

## cs.CV

**50 papers**

### 1. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

**Authors:** Yang Yang, Qinyu Zhao, Mouxiang Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04010v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04010v1)

**Summary:** Existing scaling strategies for Multimodal Large Language Models (MLLMs) typically expand either model parameters or sequential inference computation, incurring substantial memory or latency overhead. More importantly, most existing methods fail to alter the rigid, fixed computation allocation between the Vision Transformer and the Large Language Model components, limiting task-specific optimization. To address this, we introduce the Parallel Vision-Language (ParVL) scaling framework for MLLMs, ...

---

### 2. Perceptual Anchoring: Prototype-Guided Text Calibration for Training-free Open-Vocabulary Semantic Segmentation

**Authors:** Wanli Ma, Jiangwen Lu, Qinmu Peng, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03991v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03991v1)

**Summary:** Training-free open-vocabulary semantic segmentation (OVSS) partitions an image into semantically distinct regions based on arbitrary text descriptions, without learning any additional parameters. However, existing methods typically focus on improving visual representations while treating text embeddings that encode only generic category concepts as fixed classification references. The resulting semantic gap between these generic concepts and the visual representations that capture the specific a...

---

### 3. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

**Authors:** Zhen Fang, Yu Zeng, Wenxuan Huang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03979v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03979v1)

**Summary:** We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address thes...

---

### 4. JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion

**Authors:** Yicheng Xiao, Wenxun Dai, Xinran Qin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03974v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03974v1)

**Summary:** Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregress...

---

### 5. UniWorld-Design: From Pixel Generation to Layer-Native Design

**Authors:** Zongjian Li, Zhiyuan Yan, Chenxu Bai, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03971v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03971v1)

**Summary:** We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, understanding, and editing. Our key insight is that pixels define how an image is rendered, whereas layers define how an image is created, understood, and edited. Just as human designers create and manipulate visual content through layers rather than raw pixels, UniWorld-Design equips multimodal generati...

---

### 6. Progressive Learning of a Diffusion-based Inpainting Model for Separating Overlapped Fingerprints

**Authors:** Noor Hussein, Anil K. Jain, Karthik Nandakumar

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03937v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03937v1)

**Summary:** Overlapped friction ridge patterns are a recurring problem in latent fingerprints recovered from crime scenes and in live-scan scenarios where residual fingerprints on the sensor may corrupt subsequent acquisitions. Existing approaches for separating overlapped fingerprints either rely on rule-based orientation field completion that requires strong domain knowledge or train end-to-end deep neural networks that do not account for domain-specific considerations. This work introduces a diffusion-ba...

---

### 7. Latent Reward Registers for Diffusion Preference Alignment

**Authors:** Yuanshen Guan, Zipeng Feng, Zhiwei Xiong, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03929v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03929v1)

**Summary:** Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout m...

---

### 8. PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection

**Authors:** Mateusz Smendowski, Kamil Faber, Piotr Nawrocki, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03926v1)

**Summary:** Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce ...

---

### 9. GeoMAR: Unleashing Geometrically Aligned Features for Masked Autoregressive Blind Face Restoration

**Authors:** Lu Gan, Hanyu Yan, Chaofeng Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03923v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03923v1)

**Summary:** Codebook-based blind face restoration (BFR) often suffers from ambiguous conditioning features and a fragile prediction mechanism under severe degradation. To address these challenges, we propose GeoMAR, a framework designed to unleash geometrically aligned features with masked autoregressive (MAR) refinement for robust face restoration. For feature conditioning, we introduce a dual-input extraction pipeline to extract component-based geometric descriptions with explicit, spatially faithful anch...

---

### 10. Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter Coupled Training for Neural Network Quantization

**Authors:** Peng Xia, Junbiao Pang, Zheng Huang

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03919v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03919v1)

**Summary:** Low-bit quantization suffers severe accuracy degradation on compact networks, rooted in the dominant full-parameter coupled training paradigm that ignores parameter subspace heterogeneity. Their limited feature redundancy leaves little room to absorb quantization errors. Conventional pipelines adopt monolithic optimization: PTQ reconstructs fixed pretrained models without improving inherent quantization friendliness; QAT updates all parameters jointly, suffering from gradient coupling between ba...

---

### 11. When and Where to Look: Adaptive Visual Evidence Scheduling for Efficient Long Video Understanding

**Authors:** Ke Li, Jiayu Chen, Maoliang Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03918v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03918v1)

**Summary:** Efficient long-video understanding requires vision--language models (VLMs) to reason over a small number of frames selected as sparse visual evidence. Existing relevance-based methods rely on static one-shot selection with fixed frame budgets and candidate pools, while agent-based schedulers achieve adaptivity through costly multi-round reasoning and interactive search. We propose EcoFrame, a training-free framework for low-overhead query-adaptive visual evidence scheduling. EcoFrame leverages t...

---

### 12. StreamDAM: Presence-Aware Memory for Real-Time Streaming Video Object Segmentation

**Authors:** Xiang Chen

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03912v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03912v1)

**Summary:** Quality-tier video object segmentation (VOS) trackers such as DAM4SAM top accuracy leaderboards, but they are measured offline, one frame at a time with no clock. Under an honest streaming protocol at 30 frames per second, where a frame that misses its budget is served the last mask already computed, the winner collapses: the rich memory that makes it accurate is too slow to keep up, and what it emits is blind to whether the object is even present. We trace both failures to one place, the tracke...

---

### 13. UniEvo-RS: Omni-Prompt Unified Remote Sensing Segmentation with Representative Exemplar-Driven Prototype Evolution

**Authors:** Kunquan Zhang, Peilang Li, Xikun Hu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03911v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03911v1)

**Summary:** Prompt-driven vision-language models (VLMs) hold immense promise for accelerating dense remote sensing (RS) annotation, but static models suffer from severe performance degradation when deployed on novel scenes, unseen categories, or visually confusing backgrounds. Moreover, existing unified paradigms primarily rely on intra-image specific prompts, lacking flexible task routing to adapt to multi-intent operational workflows. In practical batch mapping, annotators typically refine a small set of ...

---

### 14. NCGR: Noise-Conditional Gated Rectification for Camera Extrinsic Perturbations in BEV 3D Object Detection

**Authors:** Wenbin Pan, Wanhao Liu, Liwei Luo, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03895v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03895v1)

**Summary:** Camera-based bird's-eye-view (BEV) 3D detection typically assumes accurate and fixed camera extrinsics. In detectors using spatial cross-attention (SCA), extrinsic perturbations displace the image-plane projections of BEV reference points, causing queries to sample features from incorrect regions and degrading detection performance. To address this failure mode, Noise-Conditional Gated Rectification (NCGR) is proposed to compensate for projection errors without explicitly estimating a full six-d...

---

### 15. CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement

**Authors:** Mercy Prasanna Ranjit, Anirban Porya, Sathvik Joel, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03890v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03890v1)

**Summary:** A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measurements upon which many diagnoses depend. Today's Vision-Language Models (VLMs) treat these as separate problems, if they address them at all, leaving a gap between what radiologists need and what generative models provide. We introduce CARE-X, a chest X-ray VLM that narrows this gap by unifying auxil...

---

### 16. MuRA: Multi-Rank Adaptation for Efficient and Effective Test-Time Vision-Language Generalization

**Authors:** Gengyuan Liu, Nanzhou Wang, Chang Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03885v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03885v1)

**Summary:** Vision-language models exhibit remarkable zero-shot capabilities but suffer significant performance degradation under distribution shifts. While test-time adaptation (TTA) via Low-Rank Adaptation offers a parameter-efficient solution, we identify a fundamental bottleneck in current methods: the reliance on static rank configurations. Because visual inputs inherently possess varying information densities, a fixed rank forces an inevitable optimization compromise, leading to underfitting on comple...

---

### 17. BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models

**Authors:** Sadab Shiper, Tawsif Tashwar Dipto, Mir Md Inzamam, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03884v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03884v1)

**Summary:** In-the-wild Bengali scene text recognition is largely unmeasured: existing resources target handwritten documents or constrained sign-board parsing, report only aggregate edit-distance metrics, and evaluate either conventional OCR or VLMs, never both on the same in-the-wild data. To address this gap, we introduce BANGLAWILD, a benchmark of 2,535 Bengali scene text images, each paired with a verbatim gold transcription, two categorical axes, four diagnostic attributes, and an orthographically sta...

---

### 18. CPrefix: A Combinatorial Tensor Framework for Structured Discrete Color Mappings

**Authors:** Yvan Richard

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03863v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03863v1)

**Summary:** Discrete multi-channel mappings are typically represented through sampled values, providing accurate evaluations but limited insight into their underlying structure. We introduce CPrefix, a combinatorial observable representation for discrete mappings, realized within a unified tensor framework that enables representation, reconstruction, and structural analysis.   The framework is based on a counting tensor induced by multinomial counting observables. Its support forms a discrete Pascal simplex...

---

### 19. LiteMVS: Efficient Multi-View Stereo with Foundation Distillation and Expert Aggregation

**Authors:** Tianbao Zhang, Zeyu Liu, Shuyu Wu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03851v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03851v1)

**Summary:** Real-time 3D perception is crucial for robotics, augmented reality, and embodied intelligence applications. Existing multi-view stereo (MVS) methods primarily rely on geometric correspondences, which often fail in textureless or repetitive regions, while monocular depth models leverage strong image-level priors but lack robust multi-view geometric constraints. More importantly, in robotics and embodied manipulation scenarios, high-quality 3D geometry is not only essential for static reconstructi...

---

### 20. Geo-Embed: Towards Unified Multimodal Embeddings for Urban Understanding

**Authors:** Jiapeng Li, Yong Li, Junjie Zhou, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03826v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03826v1)

**Summary:** Geospatial and urban applications increasingly require models to compare heterogeneous evidence across street-view imagery, remote-sensing observations, text descriptions, region proposals, and temporal change cues. However, existing multimodal embedding models and benchmarks are still largely designed and evaluated around general-purpose image-text matching, leaving unclear whether unified embedding space can support heterogeneous geospatial tasks involving spatial relationships, fine-grained s...

---

### 21. FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis

**Authors:** Zhang Weihui, Wang Ruizhi, Xu Hongye, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03822v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03822v1)

**Summary:** Developing robust flood assessment models requires high-quality paired satellite imagery, yet such data remain scarce for flood-specific image generation. Although generative models provide a promising means of data augmentation, existing methods often yield implausible spatial layouts of flooded regions and distort scene structures. We propose FlowForm, a framework for satellite flood synthesis that integrates SWE-inspired latent regularization with structure-aware conditioning. The Flood Descr...

---

### 22. UHP Detection: LVLMs have their Unique Hallucination Pattern in the Consistency Space

**Authors:** Amir Mohammad Ezzati, Kiyan Rezaee, Bardiya Kariminia, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03817v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03817v1)

**Summary:** Large vision--language models (LVLMs) demonstrate strong multimodal reasoning capabilities but remain prone to hallucination, where model predictions are not grounded in visual evidence. Existing black-box hallucination detection methods estimate uncertainty through a single consistency metric, implicitly assuming that model uncertainty can be adequately characterized by a single measure. However, hallucinations exhibit diverse manifestations of uncertainty across different behavioral probes, ma...

---

### 23. OmniPack: Unified Token Compression for Efficient Omni-modal Large Language Models

**Authors:** Wanshun Su, Yang Shi, Feihu Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03812v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03812v1)

**Summary:** Omni-modal large language models (Omni-LLMs) have achieved remarkable performance on audio-visual understanding tasks, but processing long and highly redundant visual and audio token sequences incurs substantial computational overhead, demanding aggressive token compression for efficient deployment. Existing methods often degrade at low token budgets: pre-LLM compression may discard structurally important and globally distributed evidence, whereas inner-LLM compression often underexploits query-...

---

### 24. AgenticVAU: Multi-Agent Explore-Verify Reasoning for Video Anomaly Understanding

**Authors:** Yuxiang Duan, Huining Li, Ao Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03779v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03779v1)

**Summary:** Video anomaly understanding (VAU) focuses on comprehensively interpreting abnormal events in videos, requiring models to identify anomalous occurrences, discover their supporting evidence, and explain the underlying causes beyond simple anomaly detection. Existing VAU methods often rely on specialized training or limited observations, restricting generalization or evidence coverage. Although single-agent alternatives support adaptive video observation, they still integrate exploration, observati...

---

### 25. TDVR: Joint Text Disambiguation and Viewpoint Reasoning for Zero-Shot 3D Visual Grounding

**Authors:** Qingxi Du, Junbo Wang, Yuke Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03763v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03763v1)

**Summary:** Zero-shot 3D visual grounding aims to localize specific objects based on textual descriptions and 3D visual input. However, the effectiveness of existing methods is significantly hindered by the ambiguous query text and deficient viewpoints. To address these issues, we propose TDVR, a training-free reasoning framework that disambiguates the input text and infers accurate viewpoints for zero-shot 3D visual grounding. First, we construct semantic 3D scene graph from the detected instances in the 3...

---

### 26. Unsupervised Adversarial Domain Adaptation for Uterine layer Segmentation: From Labeled Cine to Unlabeled Dynamic EPI MRI

**Authors:** Smiti Tripathy, Milauni Desai, Jordina Aviles Verdera, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03762v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03762v1)

**Summary:** Uterine peristalsis is a key physiological phenomenon responsible for various functions across the menstrual cycle, intimately linked to uterine wall microstructure. Alterations in uterine motion and tissue properties are implicated in the etiology of gynecological diseases, yet these processes have been studied in isolation. We introduce a dynamic multi-echo gradient echo EPI framework for simultaneous characterization and correlation of uterine peristaltic activity and time-resolved T2* change...

---

### 27. Towards Reliable and Reproducible Fetal Brain Biometry: A Deep Learning Approach Using MRI

**Authors:** Francesca Maccarone, Marina Di Stefano, Giorgio Longari, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03724v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03724v1)

**Summary:** Fetal brain biometry is essential for quantitative assessment of brain development, supporting gestational age estimation, developmental monitoring, and detection of abnormalities. In clinical practice, measurements are manually performed, making them time-consuming and prone to variability. While automated approaches have been proposed, reproducible methods remain limited, particularly those providing anatomically interpretable landmark localization. We present a fully automated deep learning-b...

---

### 28. Attention is Case-Sensitive

**Authors:** Maximilian Dillitzer, Tin Stribor Sohn, Jason J. Corso, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03711v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03711v1)

**Summary:** In human visual perception, uppercase lettering serves as a natural salience cue that captures attention within lowercase text. In this paper, we present a systematic empirical characterization study revealing that Large Language Models (LLMs) exhibit an analogous property: letter casing modulates internal attention allocation. Through analysis across 13 models, nine LLMs and four Vision-Language Models (VLMs), with diverse tokenization schemes, we show that formatting target information in alte...

---

### 29. MultiCompose: Multi-Concept Personalized Composition with Per-Subject Attribute Binding

**Authors:** Ruirui Zhang, Zhengkai Zhao, Pan Gao

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03708v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03708v1)

**Summary:** Text-to-image diffusion models enable personalization of specific visual concepts from a small number of reference images. However, generating a single image that contains multiple personalized subjects, each bound to user-specified attributes such as clothing, accessories, and held objects, remains largely unaddressed. Without explicit spatial constraints, concurrently activated concept checkpoints produce overlapping cross-attention responses, causing per-subject identity degradation and attri...

---

### 30. Pattern over Pixels: Measuring Pattern Completion Bias in Multimodal Code Generation

**Authors:** Khai-Nguyen Nguyen, Oscar Chaparro, Antonio Mastropaolo

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03691v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03691v1)

**Summary:** Multimodal large language models (MLLMs) are increasingly used to translate webpage screenshots into front-end code, but repeated UI patterns may sway them toward visually incorrect yet pattern-consistent outputs. In this work, we test how repeated webpage patterns hurt MLLM accuracy on an objective screenshot-to-code fill-in-the-blank task. We introduce the first benchmark for visual pattern-completion bias, where one localized element in a repeated UI pattern is perturbed and the model must re...

---

### 31. Keep the Needle, Prune the Haystack: Defect-Preserving Token Pruning for Efficient Zero-Shot Anomaly Detection

**Authors:** Yanning Hou, Jingyuan Zhang, Xiaoyun Wang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03681v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03681v1)

**Summary:** Zero-shot visual anomaly detection has achieved remarkable progress, with recent vision-only approaches further improving performance while simplifying the inference pipeline. However, existing methods typically perform dense computation over all images and spatial tokens, despite the fact that normal samples dominate real-world scenarios and anomalies usually occupy only small regions. Token pruning offers a promising solution, but introduces an asymmetric pruning risk in anomaly detection: ret...

---

### 32. XiDepth: a Lightweight and Efficient Network for Self-supervised Monocular Depth Estimation

**Authors:** Elena Izzo, Riccardo Toniolo, Lamberto Ballan

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03666v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03666v1)

**Summary:** Self-supervised monocular depth estimation has emerged as an appealing solution to design lightweight and effective models for deployment on computationally constrained devices due to its reduced reliance on expensive depth sensors. By eliminating the need for ground-truth annotations and leveraging the simplicity of monocular camera setups, this approach facilitates cost-effective data collection and broad applicability across fields such as computer vision and robotics. A critical challenge is...

---

### 33. Morphology-Aware Implicit Super-Resolution Network for Pathological Images

**Authors:** Jiaming Liang, QiHui Han, Haolin Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03664v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03664v1)

**Summary:** Accurate diagnosis in Digital Pathology (DP) relies on high-resolution whole-slide images, yet clinical deployment is often limited by hardware costs. Super-Resolution (SR) offers a promising alternative by computationally enhancing low-resolution acquisitions. However, existing SR methods frequently struggle to preserve fine-grained cellular morphology, leading to texture oversmoothing and blurred structural boundaries under complex tissue variability. To address this issue, we propose Morph-IS...

---

### 34. When Do Fewer Visual Tokens Accelerate Multimodal Inference? A Break-Even Study Across Decision Locations and Hardware

**Authors:** Hao Dou, Ruiwen Tian

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03649v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03649v1)

**Summary:** Fewer visual tokens do not guarantee lower end-to-end latency. We evaluate break-even with a reproducible protocol that accounts for decision overhead, shared work, and the operators each policy can avoid. A stage-level decomposition reconciles these components with measured end-to-end latency. In a 30-example pilot, the two tested autoregressive probes remain slower than Full despite state reuse. A lightweight post-vision predictor yields paired confidence intervals below zero on RTX 3090 and A...

---

### 35. Learning Biomechanically Plausible Human Motion from Sparse Radar Point Clouds

**Authors:** Jonas Leo Mueller, Markus Gambietz, Alexander Weiss, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03637v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03637v1)

**Summary:** Radar-based human pose estimation has focused on improving learning algorithms while representing the body as unconstrained keypoint coordinates. We address the underexplored dimension of anatomical fidelity by integrating a full-body skeletal model into a differentiable, end-to-end trainable radar-based pose estimation framework, in which the pose network is supervised through forward kinematics while subject-specific geometry is fitted beforehand. Subject-specific body segment proportions are ...

---

### 36. SEER: A Self-Grounded Evidence Interface for Controlled Spatial Relation Classification

**Authors:** Feixiang Liu, Likun Wang, Qiang Qiu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03631v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03631v1)

**Summary:** Spatial relation questions require a model to identify the queried subject and object before comparing their layout. Yet a VLM can recognize both entities and still answer from the wrong instance or an ambiguous global view. We ask whether making query-specific evidence explicit can mitigate this failure and propose SEER (Self-grounded Evidence for Entity-Relation Reasoning), a training-free inference-time evidence interface for frozen VLMs. SEER hides candidate relations during pair localizatio...

---

### 37. Geospatial-Prior Guidance for 3D Semantic Scene Completion

**Authors:** Meng Wang, Shougao Zhang, Wenzhe He, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03618v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03618v1)

**Summary:** Inferring complete 3D geometry and semantics from onboard images remains challenging because occlusions and restricted fields of view leave large scene regions underconstrained. Although satellite imagery provides wide-area context, appearance cues alone offer limited structural guidance and may be unreliable because of spatial or temporal discrepancies. We present GeoScene, a geospatially guided framework that jointly uses satellite imagery and structured OpenStreetMap cues as soft priors for 3...

---

### 38. A machine-readable catalogue of the Tsiolkovsky papers (fond 555, Archive of the Russian Academy of Sciences), and a way to measure how well its handwriting can be read

**Authors:** Vladimir Beskorovainyi

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03617v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03617v1)

**Summary:** The personal archive of Konstantin Tsiolkovsky (1857-1935) is held as fond 555 of the Archive of the Russian Academy of Sciences. The archive scanned the fond and published the images, but with no queryable catalogue, no full-text search and no dataset: the holdings can only be browsed one page at a time. This paper describes a machine-readable catalogue of all 2,019 files and 51,008 scans, a dating for 1,969 files taken from the archive's own descriptions, a page-level classification of every s...

---

### 39. Predictive Enhancement Calibration for Latent Breast MRI Virtual Contrast Enhancement

**Authors:** Qin Lei, Hao Wu

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03612v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03612v1)

**Summary:** Virtual contrast enhancement (VCE) synthesizes enhanced breast MR images from pre-contrast acquisitions. Modern latent generators offer strong image priors, but their bounded natural-image autoencoders conflict with the non-canonical intensity scale of MRI. We show that the upper bound can alter radiomic fidelity before generation, while scaling source and target independently creates a coordinate inconsistency. We propose Predictive Enhancement Calibration (PEC), which represents each pair in a...

---

### 40. SlimVLM: Sensitivity-aware Dynamic Structured Pruning with Adaptive Visual Token Selection for Efficient Vision-Language Models

**Authors:** Yaozhi Wen, Jialong Guo, Zhenliang Ni, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03580v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03580v1)

**Summary:** While Vision-Language Models (VLMs) have demonstrated remarkable performance in processing and understanding both text and images, their large parameter sizes lead to significant computational overhead, limiting their deployment on resource-constrained devices. While pruning has been effective for compressing Large Language Models (LLMs), directly applying it to VLMs leads to significant performance drops, largely due to redundant visual tokens interfering with importance estimation. To this end...

---

### 41. Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning

**Authors:** Kejian Zhu, Zhuoran Jin, Dongqi Huang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03571v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03571v1)

**Summary:** Recent works train agents by constructing large-scale multimodal environment pools. However, we find that simply increasing the number of multimodal environments does not always benefit. We further analyze the limitations in current multimodal environment distributions through a series of experiments. Based on these findings, we study how to build more effective training environment distributions from two dimensions: **diversity** and **difficulty structure**. For diversity, we propose **Ability...

---

### 42. Compass: Degradation-Simulated Reciprocal Learning with Lightweight Needle RWKV for Multimodal Crack Segmentation under Missing Modalities

**Authors:** Hui Liu, Chen Jia, Fan Shi, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03559v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03559v1)

**Summary:** In multimodal crack segmentation for industrial facilities, the key challenge is preventing missing modalities from degrading pixel-level performance while maintaining low computational cost. Existing methods struggle to address semantic degradation caused by missing modalities. We propose Compass, a lightweight network for robust crack segmentation under arbitrary missing modalities. Compass comprises Degradation Simulation Distillation (DSD), Needle Block, and Evidential Topology-Preserving Fu...

---

### 43. Test-Time Augmentation for Tabular-to-Image Classifiers under Distribution Shifts

**Authors:** Malena Loza, Felipe Grijalva, Eva Milara, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03557v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03557v1)

**Summary:** Tabular-to-image methods that convert tabular data into visual representations have emerged as a novel paradigm for leveraging the high performance of deep learning models. Despite their advantages, the robustness of these methods under distribution shifts remains under explored. Test-Time Augmentation (TTA) is an effective approach in image classification to improve model generalization and robustness, where predictions over multiple transformed views of each input are aggregated. This work eva...

---

### 44. S$^3$-Diff: Structural Semantic Synergy Diffusion Model for High Fidelity Super Resolution of Pathological Images

**Authors:** Jiaming Liang, QiHui Han, Guangye Ou, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03540v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03540v1)

**Summary:** Digital pathology relies on high-resolution whole slide images for accurate diagnosis, yet limitations in imaging devices, storage, and transmission often make lower-resolution pathology images more common in clinical workflows. Current super-resolution techniques often tend to smooth diagnostically relevant morphology, leading to over-smoothed textures and semantic drift that compromise downstream clinical interpretation. To this end, we develop the Structural Semantic Synergy Diffusion Model (...

---

### 45. IRIS: Visual-Semantic Binding for Forgery-Resistant Watermarking of Diffusion Images

**Authors:** Xiaoyan Feng, Zheng Gao, Tong Guan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03539v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03539v1)

**Summary:** Most in-generation diffusion watermarks embed patterns independent of the image that carries them, and attackers transplant the marks onto images the generator did not produce, resulting in forgery. Binding the mark to visual semantics prevents such transplantation, yet existing bindings anchor to a proxy image rather than the image they mark. Realizing visual-semantic binding inside generation faces two challenges. The mark derives from the image itself yet enters the sampling trajectory before...

---

### 46. MinerU.Chem: A High-Precision System for Optical Chemical Structure and Reaction Recognition

**Authors:** Haote Yang, Jiang Wu, Jingchao Wang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03525v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03525v1)

**Summary:** In organic chemistry papers and patents, molecular structures, reaction schemes, and experimental conditions are often presented as molecular structure depictions, reaction diagrams, and complex tables or figures. Such information is difficult for general-purpose document parsing systems to directly convert into machine-readable data. This limits data production for organic chemistry knowledge base construction and for AI for Chemistry tasks such as reaction prediction, retrosynthesis, condition...

---

### 47. GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression

**Authors:** Ziyue Zeng, Dingjie Peng, Xun Su, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03517v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03517v1)

**Summary:** Codebook-driven generative compression uses a pretrained image or video generator as a zero-shot visual prior and transmits compact codebook indices to guide reconstruction at ultra-low bitrate. Current codecs tie each finite-rate correction to a fresh prior evaluation, so shortening the sampler also removes correction slots that carry target-dependent information. We propose GVCCTurbo, a BPP-driven scheduler that separates expensive prior refreshes from codebook corrections: after calibrating a...

---

### 48. Detecting Pose Estimation Failures via Keypoint Self-Consistency

**Authors:** Robin Chan

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03516v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03516v1)

**Summary:** One common approach to pose estimation involves predicting object keypoints in an image, followed by using Perspective-n-Point algorithms to compute the object's rotation and translation relative to the camera. While rotations preserve object shapes, this property is often neglected in keypoint-based pose estimation methods, where keypoints are typically predicted independently from each other. As imprecise keypoint predictions negatively affects pose estimation accuracy, it also limits its reli...

---

### 49. How Many Labels Are Enough? ALDA: Active Learning Deployment Advisor for Medical Image Classification

**Authors:** Julia Machnio, Mads Nielsen, Mostafa Mehdipour Ghazi

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03511v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03511v1)

**Summary:** Active learning (AL) promises to reduce the cost of medical imaging projects by lowering the number of clinical labels required. However, practical deployment requires committing to a sampling strategy before the full annotation budget is spent, and choosing the wrong strategy can increase rather than decrease costs. We propose Active-Learning Deployment Advisor (ALDA), a deployment-oriented framework for AL method selection under clinical performance constraints. Given a short pilot phase, ALDA...

---

### 50. From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology

**Authors:** Basit Alawode, Moshira Ali Abdalla, Dwarikanath Mahapatra, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03508v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03508v1)

**Summary:** Vision Transformers (ViTs) and their hierarchical variants have achieved strong performance in Computational Pathology (CPath). However, most are pre-trained on single-resolution Whole Slide Images (WSIs), limiting their generalization across arbitrary resolutions. Gigapixel WSIs inherently contain diagnostic patterns at multiple scales, including cellular morphologies, tissue architectures, and global context, mirroring how expert pathologists examine WSIs. We introduce Multi-Resolution Pyramid...

---

## cs.LG

**50 papers**

### 1. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility

**Authors:** Mohsen Hariri, Weicong Chen, Nahal Shahini, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04001v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04001v1)

**Summary:** Large language models can solve substantially harder reasoning problems with more inference-time compute. The term "test-time scaling," however, now covers diverse inference algorithms that extend deliberation along a single trajectory, sample completed candidates and aggregate them through voting or verification, or search over unfinished partial states. These algorithms differ in their statistical structure, compute accounting, and failure modes. Treating these procedures as interchangeable un...

---

### 2. Assessment of Conditional Diffusion Model for Synthetic Histopathology Image Generation

**Authors:** Seyed Kahaki, Shijie Li, Weijie Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03990v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03990v1)

**Summary:** Synthetic histopathology image generation has emerged as an approach that may address data scarcity in computational pathology, yet current evaluation methodologies may not fully assess synthetic data quality for medical applications. This work investigates and addresses limitations in existing evaluation metrics, investigating an approach for assessing synthetic histopathology image quality through domain-specific metrics and downstream task validation. We show that conventional synthetic data ...

---

### 3. Information-Geometric Forward Policy Training in GFlowNets

**Authors:** Yordan Raykov, Rodrigo Veiga

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03967v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03967v1)

**Summary:** Generative Flow Networks (GFlowNets) have emerged as a flexible framework for amortised inference over discrete and mixed discrete-continuous objects, requiring only an unnormalised target density specified through a reward. In this work, we formulate forward-policy training in GFlowNets through the information geometry of the induced trajectory sampler. Treating the forward policy as an induced trajectory sampler, we show that its intrinsic first-order geometry is given by the Fisher-Rao metric...

---

### 4. Muon Meets Mamba: Spectral Optimization for State Space Models

**Authors:** Arslan Battalov, Karim Kramin, Alexander Markotenko, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03941v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03941v1)

**Summary:** Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We compare Muon with AdamW on Mamba-2 130M under a controlled protocol that varies only which weight groups are trained with Muon. The benefit is localized. Muon on the output projection alone beats Muon on ...

---

### 5. Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill Acquisition and Compressibility

**Authors:** Jo-Ku Cheng, Nikolaos Aletras, Marco Valentino

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03930v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03930v1)

**Summary:** Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition. However, existing pre-pretraining tasks, such as Dyck and procedural algorithms, rely on narrow primitives that fail to capture the expressive capacity of natural language. Moreover, prior studies remain restricted to relatively small token budgets, offering limited insight into skill emergence and representational dynamics. To address these limitations, we propose logic pre-pretrainin...

---

### 6. Latent Reward Registers for Diffusion Preference Alignment

**Authors:** Yuanshen Guan, Zipeng Feng, Zhiwei Xiong, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03929v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03929v1)

**Summary:** Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout m...

---

### 7. Robust Low-Tubal-Rank Tensor Completion under Cross-Concentrated Sampling

**Authors:** Hanqin Cai, Longxiu Huang, Jing Qin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03928v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03928v1)

**Summary:** Tensor cross-concentrated sampling (t-CCS) bridges entrywise sampling and t-CUR slice-wise sampling by observing entries only within selected horizontal and lateral slices. Existing t-CCS completion methods, however, assume that the observations are free of gross corruption. In this work, we study robust recovery of a third-order low-tubal-rank tensor from partial t-CCS observations contaminated by sparse, arbitrarily large outliers. We propose Robust Iterative t-CUR (R-ItCUR), a tensor-native a...

---

### 8. A Physics-Flavored Transformer Network for Parametrizing Contraction Dynamics of Engineered Skeletal Muscle Tissues

**Authors:** Mattias Luber, Timo Betz

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03927v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03927v1)

**Summary:** Engineered Skeletal Muscle Tissues (ESMs) have become a key structure for biomedical disease modeling and pharmacological screening, yet their functional characterization often relies on simplistic metrics like peak force, discarding critical kinetic information. This is partially due to the high level of mathematical complexity which mechanistic models introduce to capture these dynamics. Hence, exactly the complexity prevents scalable application and widespread adaptation in the field. Here we...

---

### 9. PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection

**Authors:** Mateusz Smendowski, Kamil Faber, Piotr Nawrocki, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03926v1)

**Summary:** Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce ...

---

### 10. Trajectory inference via Acceleration Matching

**Authors:** Bartolo Dazzini, Giovanni Conforti, Alain Durmus, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03916v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03916v1)

**Summary:** Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories that best resemble and interpolate the data. Existing algorithms exhibit computational challenges: they either rely on preprocessing subroutines to enforce smoothness or on simulation-based training objectives, both of which can be expensive. In order to overcome these limitations, we propose a new ...

---

### 11. Sparse Weight Decomposition for Efficient Circuit Extraction

**Authors:** Chuanhao Yan, Xuhan Huang, Yawen Duan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03913v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03913v1)

**Summary:** Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight ...

---

### 12. Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory

**Authors:** Matt Ratto, Abhishek Moturu, Daniel Silver

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03910v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03910v1)

**Summary:** As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, cont...

---

### 13. Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse

**Authors:** Taekyung Heo, Rasoul Shafipour, Ritchie Zhao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03893v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03893v1)

**Summary:** Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch. We propose cross-model KV cache transfer, where the receiver reuses the source's KV cache, skipping prefill. We find that cross-model KV has substantial linear structure across matched-KV pairs, where source and target share KV head count and per-head dimension. On Qwen3 14B->32B, one...

---

### 14. Omega-S: A Functional Resilience Index for LLM Fine-Tuning

**Authors:** Alberto Acedo

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03887v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03887v1)

**Summary:** Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than ...

---

### 15. Operationally Feasible Synthetic Power-Grid Scenarios via Learning the AC-Operable Joint Distribution

**Authors:** Chenhan Xiao, Xinyu He, Haoran Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03878v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03878v1)

**Summary:** Synthetic power-grid scenarios are essential for planning, resilience assessment, contingency analysis, and data-driven power-system applications. Recent synthetic grid generation methods have improved structural realism and operational feasibility by incorporating engineering knowledge through post-generation validation, optimization, or physics-aware generation. However, generated scenarios may still exhibit low AC feasibility and robustness, limiting their practical value for downstream power...

---

### 16. Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning

**Authors:** Pyrros Koussios, Chenhao Li, Xin Chen, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03875v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03875v1)

**Summary:** Designing effective reward functions remains a major bottleneck in Reinforcement Learning (RL). Recent work uses large foundation Vision-Language Models (VLMs) as reward models, computing text-observation similarity to bypass manual reward engineering. Although promising, these rewards are often noisy and unreliable, limiting their direct utility during deployment. We present Structure-Aware Fine-Tuning (SAFT), a simple, self-supervised method that refines these imperfect reward signals online w...

---

### 17. ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

**Authors:** Tianyi Guan, Yiding Wang, Haotong Yang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03874v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03874v1)

**Summary:** Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficult...

---

### 18. GENESIS: Towards Explainable Causal Discovery

**Authors:** Abhinav Thorat, Ravi Kumar Kolla, Vishak K Bhat, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03868v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03868v1)

**Summary:** Causal Discovery (CD) from observational data faces two fundamental challenges. First, purely statistical methods often lack the power to resolve structural ambiguities in low-sample regimes. Second, although LLM-assisted hybrid approaches improve structure recovery through semantic reasoning, the influence of that reasoning on individual edge decisions remains largely opaque. Consequently, existing hybrid methods fail to satisfy a fundamental requirement: explaining why a particular edge is inc...

---

### 19. CRS-Triage: Confidence- and Reliability-Aware Selective Triage under Incomplete Clinical Evidence

**Authors:** Guan Qiang, Yushen Chen, Tianlong Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03862v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03862v1)

**Summary:** Emergency triage requires reliable decisions within a short time period. However, the available electronic health record (EHR) data, including structured data and clinical text, are often incomplete, unreliable, and inconsistent. This makes machine learning (ML)-based triage prediction more challenging, as existing ML models typically rely on complete and reliable EHR data to accurately predict patients' acuity levels. To address this, we propose confidence- and reliability-aware selective triag...

---

### 20. Bi-semantic Chemical Embedder for Joint Representation Learning of SMILES and Natural Language

**Authors:** David Ming Segura, Jeremy Goumaz, Joshua W. Sin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03855v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03855v1)

**Summary:** Transformer models have revolutionized natural language processing (NLP), and text-based molecular representations like SMILES have successfully extended these architectures to chemistry. However, domain-adaptive pre-training often causes models to overfit to chemical syntax, catastrophically forgetting their foundational semantic capabilities. To address this challenge, we introduce CheMatE, a chemistry-oriented embedding model that jointly captures molecular structure and domain-specific natur...

---

### 21. Quantization Effects on Biomedical LLM Reliability

**Authors:** Anton Rasmussen, Hong Qin

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03854v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03854v1)

**Summary:** When decoder language models are used as classifiers, predicted class probabilities depend on implementation choices, including the prompt template, verbalizer (label-to-token mapping), and scoring rule, that are rarely treated as experimental variables. We present a controlled evaluation of three Mistral-7B variants (Base, BioMistral, and Instruct) on PubMed RCT sentence classification (n=2000) under FP16, INT8, and INT4 precision using four answer-text prompt templates. Our primary finding is ...

---

### 22. FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs

**Authors:** Amin Farajzadeh, Melike Erol-Kantarci

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03852v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03852v1)

**Summary:** This paper proposes FedCritic-MIMO, a communication-efficient serverless federated multi-agent reinforcement learning framework for AI-native resource control across independently deployable cell-level controllers in open and disaggregated 6G RANs. Controllers share no trainer, retain local actors and personalized critic components, and exchange only compatible shared critic parameters. FedCritic-MIMO targets reuse-$1$ multi-cell massive-MIMO OFDMA deployments, where RAN controllers jointly mana...

---

### 23. Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation Robustness and Its Scaling

**Authors:** Nathan Labiosa, David Buff, Ena Nayak, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03842v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03842v1)

**Summary:** When a language model fails on surface-perturbed input (typos, OCR noise, homophones), "which layer is responsible" has three natural operationalizations: where representations diverge most (sensitivity), where restoring clean activations recovers the prediction (causality), and where a small adapter can repair the damage (compensatory capacity) - and we show these three layer maps dissociate. Across a five-model panel we identify two propagation regimes - spike-and-suppress (Phi-3.5, Gemma-2-9B...

---

### 24. Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers

**Authors:** Sajjad Khan

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03836v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03836v1)

**Summary:** A framework that persists execution state so a run can be interrupted, survive a crash, and continue must decide what a resume means for effects that already fired. Five widely deployed agent workflow frameworks answer differently, none exposes a machine-checkable contract, and behavior violates even the fragments they state. The RESUME CONTRACT states six properties over the persistence API (prefix continuation, effect exactly-once, fork determinism, checkpoint validity, consume-once, recovery ...

---

### 25. Geo-Embed: Towards Unified Multimodal Embeddings for Urban Understanding

**Authors:** Jiapeng Li, Yong Li, Junjie Zhou, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03826v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03826v1)

**Summary:** Geospatial and urban applications increasingly require models to compare heterogeneous evidence across street-view imagery, remote-sensing observations, text descriptions, region proposals, and temporal change cues. However, existing multimodal embedding models and benchmarks are still largely designed and evaluated around general-purpose image-text matching, leaving unclear whether unified embedding space can support heterogeneous geospatial tasks involving spatial relationships, fine-grained s...

---

### 26. UNVaMP: Neural Knowledge Tracing with Variational Regularization of Latent Knowledge Dynamics

**Authors:** Carson J. Cook, Ahmed J. Zerouali, Anthony Schmidt, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03811v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03811v1)

**Summary:** We introduce the Unified Neural Variational Measurement of Proficiency (UNVaMP) architecture, a knowledge tracing method that integrates observed student-item interactions with internal memory to produce evolving latent representations of student knowledge. These representations support accurate predictions of future responses while enabling explicit control over the smoothness of estimated learning trajectories. UNVaMP can be configured as either a purely neural model or a hybrid model that pre...

---

### 27. M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models

**Authors:** Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03803v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03803v1)

**Summary:** Multilingual language models are deployed across a hundred or more languages, yet most benchmarks test whether a model can perform a task _in_ a language rather than whether it commands the language itself, conflating fluency with proficiency. We introduce M-GATE (Multilingual Grammar, Accuracy in Translation, and Efficiency), a benchmark of linguistic proficiency spanning 30 typologically diverse languages from high- to low-resource. M-GATE comprises three tasks: grammatical error detection on ...

---

### 28. Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss

**Authors:** Bakbergen Ryskulov, Iker García-Ferrero, David Montero, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03796v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03796v1)

**Summary:** Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$...

---

### 29. Computing Actual Causes for Neural Network Predictions under Structured Causal Inputs

**Authors:** Jannick Strobel, Muqsit Azeem, Stefan Leue

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03772v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03772v1)

**Summary:** Explaining the predictions of neural networks is a central challenge in trustworthy AI. Existing explanation methods, such as those based on feature attribution or minimal sufficient sets, typically treat input features as independent, which can yield misleading explanations when inputs exhibit structured dependencies. We address this by formalizing explanations as Halpern-Pearl (HP) actual causes, modeling input dependencies using Boolean Structural Causal Models (SCMs). We compute HP causes by...

---

### 30. Can LLMs Test Terminal User Interfaces?

**Authors:** Chao Peng, Ruida Hu, Ajitha Rajan, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03743v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03743v1)

**Summary:** Terminal User Interfaces (TUIs) combine the stateful, screen-oriented behaviour of GUIs with terminal deployment and are now common in developer tools. Yet they lack a dedicated testing methodology. We survey 197 real-world TUI applications: only 12% of test code exercises the interface, and 45% of those tests never send input, checking a static frame instead. We turn these applications into a headless benchmark spanning ratatui/Rust, bubbletea/Go, textual/Python, and ink/TypeScript, packaging e...

---

### 31. Amortized Interventional Forecasting for Multivariate CIR Processes

**Authors:** Andreas Sauter, Sumit Sourabh, Drona Kandhai, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03715v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03715v1)

**Summary:** Mean-reverting dynamics are pervasive in finance, and the Cox--Ingersoll--Ross (CIR) process is a standard model for the time series they produce, from short rates to credit default swap (CDS) spreads. Yet CIR models capture only \emph{correlated} co-movement, not \emph{causal} influence between series, so they cannot answer the system's response when one series is externally shocked, which observational conditionals confound with historical co-movement. We make two contributions. First, an amor...

---

### 32. Attention is Case-Sensitive

**Authors:** Maximilian Dillitzer, Tin Stribor Sohn, Jason J. Corso, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03711v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03711v1)

**Summary:** In human visual perception, uppercase lettering serves as a natural salience cue that captures attention within lowercase text. In this paper, we present a systematic empirical characterization study revealing that Large Language Models (LLMs) exhibit an analogous property: letter casing modulates internal attention allocation. Through analysis across 13 models, nine LLMs and four Vision-Language Models (VLMs), with diverse tokenization schemes, we show that formatting target information in alte...

---

### 33. To Describe or Construct Statistical Learning Models Using the Category-theoretical Language

**Authors:** Congwei Song

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03706v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03706v1)

**Summary:** Statistical learning is a fascinating field that has long been the mainstream of machine learning/artificial intelligence. A large number of results have been produced which can be widely applied to real-world problems. It also leads to many research topics and also stimulates new research. This report summarizes some classical statistical learning models and well-known algorithms, especially for amateurs, and provides a category-theoretic perspective on understanding statistical learning models...

---

### 34. Less Traffic, Better Outcomes: Competition-Aware Request Dispatch in Real-Time Ad Exchanges

**Authors:** Jonaid Shianifar, Blaz Mramor, Fangda Zou, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03705v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03705v1)

**Summary:** Real-time bidding (RTB) ad exchanges typically forward nearly all incoming requests to demand-side platforms (DSPs), even though only a small fraction receive bids. This over-distribution weakens auction outcomes: DSPs throttle participation under compute and budget constraints, reducing the effective use of limited bidding capacity. We present a competition-aware request dispatch framework that uses distributional bid prediction and probabilistic forwarding to decide whether each request should...

---

### 35. Learning and Clustering on Temporal Graphs: Principles, Primitives, and Pooling

**Authors:** Nelson Aloysio Reis de Almeida Passos, Emanuele Carlini, Salvatore Trani

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03696v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03696v1)

**Summary:** This work focuses on the problem of learning on temporal graphs, with particular emphasis on the task of clustering: obtaining coarse-grained representations by aggregating information from nodes, edges, and temporal dynamics - a task related to pooling in machine learning on graphs, or community detection in network science. Although graph neural networks reach state-of-the-art performance across many downstream graph tasks, their advantage over established descriptive and inferential clusterin...

---

### 36. Accelerating Dynamic Graph Clustering on GPU Architectures with cuGraph

**Authors:** Nelson Aloysio Reis de Almeida Passos, Emanuele Carlini, Salvatore Trani

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03695v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03695v1)

**Summary:** This work addresses community detection in temporal networks through GPU-accelerated extensions of spectral clustering and modularity-based algorithms originally designed for static graphs. Built on the NVIDIA RAPIDS ecosystem, the framework enables the characterization and tracking of communities in snapshot-based dynamic graphs, either by Leiden greedy optimization with multi-GPU support via Dask-based workload distribution, or eigendecomposition of a symmetric Bethe-Hessian operator. Our mult...

---

### 37. LAEF: A Lead-Agnostic ECG Foundation Model Towards Point-of-Care Diagnostics

**Authors:** Edoardo Coppola, Stefano Fiorini, Pietro Liò, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03690v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03690v1)

**Summary:** Point-of-care cardiac devices such as smartwatches and handheld ECG recorders typically capture 1--2 leads, yet existing ECG foundation models are architecturally constrained to fixed 12-lead inputs, degrading or failing under these reduced configurations. We introduce LAEF (Lead-Agnostic ECG Foundation), a 7M-parameter ECG foundation model that can natively process any lead subset without zero-padding or architectural modification. LAEF represents ECGs as variable-size spatiotemporal graphs wit...

---

### 38. DiagLoop: A Counterfactual Data Flywheel with Stage-Localized Reinforcement for Diagnostic LLMs

**Authors:** Jian Zhang, Bingyi Wang, Yizhi Liu

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03674v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03674v1)

**Summary:** Causal diagnostic models must explain how conclusions follow from evidence because diagnoses guide repairs and treatments. Yet serious cases are scarce, records rarely contain reasoning paths, and data transfer poorly across configurations, complicating local deployment. We present DiagLoop, a counterfactual data flywheel that converts codified physical relations or clinical guidelines, authored once per mechanism family, into training supervision beyond recorded cases. A training-only teacher p...

---

### 39. CausalOPD: First-Wrong-Step Supervision for Distilling Causal Chain Reasoning

**Authors:** Jian Zhang, Bingyi Wang, Yizhi Liu

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03673v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03673v1)

**Summary:** Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning. Although large language models perform well on such tasks, privacy, latency, and controllability motivate distillation into locally deployable models. Standard trajectory imitation does not correct process errors on the student's own rollout distribution. We propose Cau...

---

### 40. Conditionally Identifiable Latent-Environment Modeling for Out-of-Distribution Recommendation

**Authors:** Qianqian Wang, Wenwu Gong, Yunshan Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03647v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03647v1)

**Summary:** Out-of-distribution (OOD) recommendation is vulnerable to preference shifts induced by a latent environment. Existing methods can infer latent states from logged interactions, yet the statistical meaning of the latent environment and its effect on preference remain underdetermined. We formulate this task as conditionally identifiable risk-aware recommendation (CI-RR) and propose Conditionally Identifiable Latent-Environment Recommendation (CILER). CILER uses a user-conditioned exponential family...

---

### 41. POEM: Phase-Aware $\mathrm{SO}(2)$ Feature Rotation for Time Series Forecasting Under Periodicity Drift

**Authors:** Jiawen Zhu, Shuhan Liu, Shengxuan Li, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03630v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03630v1)

**Summary:** Deep learning has advanced time series forecasting, but periodicity drift, in which cycle timing and phase vary over time, remains a challenging problem. Existing methods predominantly model these sequences on fixed time grids, suffering from a limited ability to accommodate phase-related variation. To address this limitation, we propose \textbf{POEM}, a phase-aware forecasting framework based on latent feature rotation using the special orthogonal group in two dimensions, denoted by $\mathrm{SO...

---

### 42. Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model

**Authors:** Abdallah Khemais

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03629v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03629v1)

**Summary:** A companion paper studies when activation patching and weight-space ablation agree, inside an idealized model where a conditional computation is carried additively through a residual stream. For the one composition in that model where two carriers are architecturally dependent, an attention head and its own layer's normalization-MLP composition, it derives an exact first-order interaction formula, zero when only the MLP is ablated and second-order bounded when the head is also ablated. That resu...

---

### 43. ConformalShift: Targeted Event Reordering Against Adaptive ECG Monitoring

**Authors:** Arash Vashagh, Yasmin Vashagh

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03628v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03628v1)

**Summary:** Adaptive conformal prediction can recover clinically important heartbeat classes missed by a point classifier, but delayed feedback makes its decisions sensitive to event order. We introduce ConformalShift, a bounded event-reordering attack that suppresses the ventricular class for rescued events without modifying ECG waveforms, labels, classifier scores, or the event multiset. ConformalShift searches for feasible permutations of authentic preceding events that lower the ventricular threshold be...

---

### 44. A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation

**Authors:** Abdallah Khemais

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03620v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03620v1)

**Summary:** Activation patching and weight-space ablation both claim a component is causally responsible for a behavior, yet they act on different objects: one forward pass versus the parameters behind every forward pass. We ask when they agree.   We study an idealized model where a conditional computation is carried additively through a residual stream, $F(x)=F_0(x)+\sum_iα_i(x)v_i$, read out by a linear functional, and prove three exact results. First, deleting a subset of carriers collapses a matched inp...

---

### 45. Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents

**Authors:** William Bolton, Philip Torr

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03606v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03606v1)

**Summary:** Clinical development is sequential decision-making under uncertainty, where a sponsor must plan a portfolio of experiments from heterogeneous evidence. We study this setting by framing oncology clinical development as an offline decision-making problem in which an agent predicts the next six-month trial portfolio of an oncology drug program from information available at the decision date. To support this, we construct a temporal dataset that combines 31.7k heterogeneous public data records, incl...

---

### 46. FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection

**Authors:** Amirhossein Taleshinosrati, Yangyang Wang, Atitaya Phoemsuk, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03597v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03597v1)

**Summary:** Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and is associated with increased risks of stroke, heart failure, and mortality. Recent ECG foundation models offer transferable representations for automated AF detection. However, their relative effectiveness remains unclear because existing studies use different datasets, preprocessing procedures, classifiers, and validation protocols. This study presents FOUND-AF, a unified, leakage-controlled, and deployment-oriented be...

---

### 47. Design-Time Optimization of Deep Neural Networks for Intermittent Learning on Microcontrollers

**Authors:** Jakob Schubert, Maximilian Kasper, Maximilian Linke, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03589v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03589v1)

**Summary:** We present a method for designing deep neural networks (DNNs) for intermittent, energy-autonomous, on-device learning on microcontroller units (MCUs). In mobile applications where the energy can run out, e.g., when solar-powered, executing artificial intelligence (AI) faces a technical issue as learning can be interrupted at any time. Our approach combines a hardware-aware energy prediction model with multi-objective optimization (MOO), enabling offline DNN optimization at the design stage witho...

---

### 48. Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving

**Authors:** Xiang Li, Pengcheng Wang, Huazheng Wang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03579v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03579v1)

**Summary:** Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters. Though powerful, this introduces a critical system dilemma between serving efficiency and task performance: higher-rank adapters generally achieve better downstream task performance, but their GPU VRAM footprint and Host-to-Device PCIe swapping overhead severely constrain scalability. Conversely, ultra-low-rank adapters ($r \le 2$) minimize both VRAM footprint and PCIe transfer over...

---

### 49. SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs

**Authors:** Kejian Zhu, Zhuoran Jin, Shangqing Tu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03573v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03573v1)

**Summary:** Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) exhibit fundamentally different behaviors in enhancing multi-task reasoning for large language models (LLMs). Our preliminary experiments revealed a phenomenon: SFT suffers from severe task conflicts under multi-stage training, whereas RL enables stable coexistence across diverse tasks. Empirically, we trace this to the parameter level, observing that RL induces sparse and approximately orthogonal updates across tasks. We provide a the...

---

### 50. Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities

**Authors:** William Bolton, Philip Torr

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03569v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03569v1)

**Summary:** Benchmarking the ability of AI scientists to generate novel ideas is notoriously difficult. Existing benchmarks in this field have made progress in evaluating scientific reasoning and research replication, but often rely on synthetic tasks or retrospective targets, which may be confounded by prior exposure. We hypothesize that complex, adversarial, fast-moving real-world domains where expert practitioners independently generate observable outputs can provide a practical solution to fill this gap...

---

## cs.NE

**50 papers**

### 1. The Transformer Revolution, Part 1: Dynamic Processing through Output- Weight Interconnections

**Authors:** Marco Giunti, Fabrizia Giulia Garavaglia

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03921v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03921v1)

**Summary:** This paper offers a new interpretation of the Transformer during inference. Against the "stochastic parrot" view that large language models merely reproduce statistical regularities learned in training, we argue that Transformers construct and apply prompt-dependent transformations whose parameters are generated during inference. We call this form of computation SIDPP: Sequence-level Interactive Dynamic Parallel Processing. The Transformer is interpreted as a system that transforms concepts by m...

---

### 2. Omega-S: A Functional Resilience Index for LLM Fine-Tuning

**Authors:** Alberto Acedo

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03887v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03887v1)

**Summary:** Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than ...

---

### 3. MuEvo: LLM-Driven Evolution of Multi-Heuristic Ensemble

**Authors:** Haoze Lv, Ning Lu, Shengcai Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03636v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03636v1)

**Summary:** Large language model-based automated heuristic design (LLM-AHD) has shown strong potential in discovering effective heuristics for combinatorial optimization problems. However, existing methods primarily optimize a single heuristic, whereas practical optimization frameworks often rely on multiple interacting components. Directly extending single-heuristic methods is challenging because early component selection can overlook components with late potential, while independent evolution ignores inte...

---

### 4. AS-FedBridge: Pseudo-Spike Bridge Distillation for Heterogeneous ANN-SNN Federated Learning

**Authors:** Shengyang Li, Yiting Dong, Liuyang Song, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03324v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03324v1)

**Summary:** Federated learning enables collaborative model training across distributed edge devices while strictly preserving data privacy. To facilitate practical deployment on resource-constrained edge devices, Spiking Neural Networks (SNNs) have emerged as a promising alternative to traditional Artificial Neural Networks (ANNs) due to their sparse computing mechanisms and high energy efficiency. However, jointly training ANNs and SNNs exposes a challenge of representational misalignment, which is intrins...

---

### 5. Impacts of Single-objective Landscapes on Multi-objective Optimization

**Authors:** Shoichiro Tanaka, Keiki Takadama, Hiroyuki Sato

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03266v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03266v1)

**Summary:** This work revealed a relationship between a multi-objective optimization problem and single-objective optimization problems that exist in the multi-objective problem. This work focused on combinatorial problems and investigated the relations between the local optima networks of the single-objective problems and the Pareto optima network of the multi-objective problem. Each of their networks has a graph structure. We divided the entire network into subgraphs. Each subgraph was called a component ...

---

### 6. NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives

**Authors:** Yantong Liu, Zheyu Zhang, Runpeng Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03187v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03187v1)

**Summary:** Multimodal medical large language models remain structurally weak for neuro-oncology because volumetric evidence is compressed into generic visual tokens and diagnostic conclusions often lack an auditable link to MRI regions. We present NeuroMosaic, a 3D multimodal language model that converts multi-sequence brain MRI into anatomy-indexed regional tokens, aligns them with clinical narrative and molecular concepts, and generates evidence-linked outputs. The architecture combines a multi-resolutio...

---

### 7. ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces

**Authors:** Kunal Kumar Pant, Nithin Nagaraj

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01968v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01968v1)

**Summary:** Transformer models are most often understood through what they do: their benchmark performance, generation quality, or behavior on downstream tasks. Yet frozen transformer input-embedding spaces may also be examined through their responses to a controlled deterministic probe before contextual computation or task-specific adaptation. Guided by this response-based view, we introduce \emph{ChaosProbe}, a deterministic neurochaos-inspired method for constructing response-based fingerprints of frozen...

---

### 8. Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory

**Authors:** Zhaotian Gu, Jie Su, Weiwei Wang, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01947v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01947v1)

**Summary:** The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...

---

### 9. Towards Autonomous Formulaic Alpha Discovery: An Evolutionary Computation Perspective

**Authors:** Xinwei Yu, Yiyang Fu, Mingcheng Fan, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01789v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01789v1)

**Summary:** Automated formulaic alpha discovery aims to generate predictive and interpretable trading signals from large symbolic factor spaces. Its effectiveness is constrained by noisy fitness estimates, market nonstationarity, costly backtesting, semantic redundancy, and conflicting practical objectives. Existing studies employ diverse techniques, including genetic programming (GP), evolutionary algorithms (EAs), reinforcement learning (RL), generative flow networks (GFlowNets), Monte Carlo tree search (...

---

### 10. An Evolutionary Algorithm Assisted by an Ensemble of Pareto-Optimal Surrogate Models

**Authors:** Kei Nishihara, Yaochu Jin, Masaya Nakata

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01777v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01777v1)

**Summary:** An ensemble of surrogate models helps improve the prediction quality and robustness of surrogate models, and in turn, the search performance of surrogate-assisted evolutionary algorithms (SAEAs). Although different degrees of smoothness of the approximated fitness landscapes need to be carefully designed for an effective ensemble, little attention has been paid to the explicit tuning of the degree of smoothness derived by surrogate models. This study proposes an adaptive ensemble SAEA, which aut...

---

### 11. Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition

**Authors:** Xiubo Liang, Jinxing Han, Yuke Li, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01646v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01646v1)

**Summary:** Handwritten Text Recognition (HTR) is computationally imbalanced in two ways: most image pixels are background, and many width-axis sequence positions are blank-dominated. This creates a mismatch for Spiking Neural Networks (SNNs): handwriting is observed as a static image, whereas spiking computation unfolds over timesteps. We propose Spike-HTR, a hybrid spiking recognizer that controls both the number of spiking steps and the number of width positions processed by the deep sequence mixer. To m...

---

### 12. SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks

**Authors:** Xiubo Liang, Jinxing Han, Yuke Li, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01622v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01622v1)

**Summary:** Spiking Neural Networks (SNNs) enable event-driven computation with sparse activations, but building multimodal Transformers on SNNs is hindered by unstable training in deep spiking stacks and the mismatch between dense softmax attention and spike-based communication. We propose SMM Transformer, an SNN-based multimodal Transformer framework that combines (i)PLMP, a Parallel LIF with Multistage Learnable Parameters neuron and a tailored P-STBP algorithm for stable deep SNN training, (ii) SMSA, an...

---

### 13. Unsupervised Multidomain Approaches to Named Entity Recognition with Small Datasets

**Authors:** Israel Fianyi, James Montgomery, Soonja Yeom

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.00984v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00984v1)

**Summary:** This paper explores the challenges and the methodologies associated with learning quality representations in scenarios with unlabelled small or limited datasets for downstream information extraction task (Multidomain Named Entity Recognition (NER). The study adopts a Transfer Learning on small datasets. Traditional NER systems often rely on large, labelled data, which is impractical for many domains. This study, therefore, applies an unsupervised pre-training approach to precondition and identif...

---

### 14. DGA$_2$D: Directed Graph-Guided Automated Algorithm Design with Large Language Models

**Authors:** Jiale Zhao, Zimu Chen, Sirui Mao, et al.

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00700v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00700v1)

**Summary:** The rapid development of Large Language Models (LLMs) has opened new avenues for Automated Heuristic Design (AHD) for solving NP-hard combinatorial optimization problems (COPs). However, existing LLM-driven AHD methods are largely confined to rigid solver templates, relegating the search process to isolated module tuning. Transitioning to fully autonomous, system-level algorithm design is essential but fraught with low reliability of generated operators, extremely large search spaces, and ineffe...

---

### 15. SDDMO-Bench: A Benchmark Suite for Streaming Data-Driven Dynamic Multi-Objective Optimization

**Authors:** Wenjie Xiao, Hui Bai, Junhao Chen

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00474v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00474v1)

**Summary:** Streaming data-driven dynamic multi-objective optimization requires algorithms to track time-varying Pareto fronts using only sequential observations under concept drift. However, systematic evaluation remains difficult because real-world problems usually lack ground-truth optima, drift annotations, and controllable conditions, while existing benchmarks provide limited support for standardized comparison. This paper proposes SDDMO-Bench, a benchmark suite that transforms classical dynamic multi-...

---

### 16. Linear Proposal Operators and Stochastic Search Geometry in SOMA and Differential Evolution

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29228v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29228v1)

**Summary:** Swarm and evolutionary algorithms are usually analyzed as complete procedural systems in which nonlinear selection, replacement, and adaptation obscure simpler structure within candidate generation. This paper introduces an operator--selection factorization that separates objective-independent variation from boundary repair and fitness-dependent selection, and uses it to study the proposal geometry of the Self-Organizing Migrating Algorithm (SOMA) and Differential Evolution (DE). The canonical S...

---

### 17. Analysis of Memory-Runtime Trade-offs in Caching Strategies for Genetic Programming Symbolic Regression

**Authors:** Jiaming Shi, Kei Sen Fong, Mehul Motani

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29116v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29116v1)

**Summary:** Genetic Programming Symbolic Regression (GPSR) generates mathematical expressions to model input-output relationships using an evolutionary process. A significant challenge in GPSR lies in the repeated evaluation of entire expressions or their sub-expression, which inflates computational runtime. To address this inefficiency, caching mechanisms have been employed to reduce redundant computations. However, prior studies predominantly employ a single caching strategy, offering limited insights int...

---

### 18. SILVA Networks as Structured Implicit Layers and Vector Attractors via Dynamic Interaction Fields

**Authors:** Jose Luis Lima de Jesus Silva

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.28989v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28989v1)

**Summary:** Many learning problems require representations that reconcile direct input, nearby structure, and broader context. In implicit neural layers, these influences are usually absorbed into a single fixed-point update, making it hard to identify what enters from the stimulus, what propagates locally, what comes from global context, and what is produced by solver dynamics. Here we introduce SILVA Networks, Structured Implicit Layers and Vector Attractors via Dynamic Interaction Fields. SILVA separates...

---

### 19. Hash Chemistry: Minimal Models for Evolutionary Growth of Complexity

**Authors:** Ilya Horiguchi, Hiroki Sayama

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28219v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28219v1)

**Summary:** Hash Chemistry is a family of minimalistic evolutionary models in which a deterministic hash function assigns a scalar score to entities of arbitrary size, opening a combinatorially vast possibility space (a ``cardinality leap''). Since its introduction, the idea has been realized in several settings, from the original spatial formulation to a fast non-spatial variant and then to structural cellular models. Here we review the Hash Chemistry family as a coherent modeling framework and use it to e...

---

### 20. Nanoparticle Networks for Neuromorphic Computing

**Authors:** Jonas Mensing, Wilfred G. van der Wiel, Andreas Heuer

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.27844v1) | 📄 [PDF](https://arxiv.org/pdf/2607.27844v1)

**Summary:** Physical computing leverages complex dynamical systems for energy-efficient data processing. In this work, we present a neuromorphic architecture based on metallic nanoparticles interconnected by molecular junctions on a $\text{SiO}_2$/Si substrate. We demonstrate that surrounding static control electrodes transform this nanoparticle network from a passive reservoir into a tunable nonlinear dynamical system. By analyzing how these electrodes route simple one-dimensional voltage inputs into multi...

---

### 21. The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy

**Authors:** Zeyu Wang

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26648v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26648v1)

**Summary:** Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates. We argue the energy dividend of sparsity is not a property of SNNs but of the task. Holding architecture fixed and swapping only the hidden unit (continuous vs. leaky-integrate-and-fire), plus a two-sided target-firing-rate probe, we measure how far activity can be pushed down before quality breaks. Low-load feed-forward pe...

---

### 22. Shared Symbolic Backbones for Physically Consistent Multi-Output Symbolic Regression

**Authors:** Manuel Rodriguez

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26528v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26528v1)

**Summary:** Symbolic regression provides analytical expressions, but it is usually applied one output at a time. This is limiting in process systems, where state variables are often coupled through shared physical parameters. Independent symbolic regression can give accurate individual equations that are difficult to interpret as one model. We present a neuro-evolutionary symbolic regression method for coupled multi-output systems. The method searches for a shared symbolic backbone: a set of latent symbolic...

---

### 23. EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks

**Authors:** Peng Yin, Kai Li, Yifan Zhang, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26490v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26490v1)

**Summary:** Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs), yet their performance heavily relies on the manual, trial-and-error engineering of neural representations, loss formulations, and optimization dynamics. While Large Language Models (LLMs) offer a promising avenue for automated design, unconstrained code generation often yields mathematically invalid or numerically unstable solutions under strict scientific computing con...

---

### 24. Reconstructing Backpropagation from Forward Fluctuations in Noise-modulated Neural Networks

**Authors:** Shuhei Ikemoto

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26483v1)

**Summary:** A Noise-modulated Neural Network (NNN) learns and infers only in the presence of noise, treating noise as a computational resource rather than a disturbance. The noise lets it learn efficiently by backpropagation while transmitting spike-like signals, but backpropagation needs a reverse path through transposed weights, the weight transport problem, which undermines biological and neuromorphic plausibility. Forward-only alternatives typically substitute a different objective or fixed random feedb...

---

### 25. Neural Architecture Search for Traffic Prediction: A Survey of Methods, Challenges, and Future Directions

**Authors:** Truong Giang Vu, Li Yang, Richard W. Pazzi

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26467v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26467v1)

**Summary:** Traffic prediction is a core task in intelligent transportation systems, supporting applications such as adaptive signal control, route guidance, and ride-hailing dispatch. Deep learning models, including graph convolutional networks, recurrent networks, and Transformers, achieve strong results on standard benchmarks, but their architectures are designed by hand, requiring significant expert effort and producing models that often generalize poorly across cities and datasets. Neural Architecture ...

---

### 26. Fourier Feature Physics-Informed Neural Networks for Elasto-Plastic Analysis of Geomaterials with a Non-Associative Mohr-Coulomb Model

**Authors:** Apisit Robjanghvad, Sompote Youwai

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25150v2) | 📄 [PDF](https://arxiv.org/pdf/2607.25150v2)

**Summary:** Elasto-plastic boundary value problems in geotechnical engineering are conventionally solved by the Finite Element Method (FEM), which incurs high computational cost from incremental-iterative procedures. Physics-Informed Neural Networks (PINNs) offer a mesh-free alternative but suffer from spectral bias, failing to resolve the sharp gradients arising at elastic-plastic boundaries and within localized plastic zones. This limitation is particularly consequential for the non-associative Mohr-Coulo...

---

### 27. Mitigating the Impact of Retention Loss on Inference Accuracy in 65 nm Single-Poly Floating-Gate Analog In-Memory Computing

**Authors:** Mirko Brazzini, Giulio Filippeschi, Alessandro Catania, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25058v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25058v1)

**Summary:** We show with experiments and system-level simulations that it is possible to successfully mitigate the impact of retention loss on inference accuracy degradation by using both circuit-level compensation techniques and batch normalization recalibration at the algorithmic level. Experiments are performed on a single-poly floating-gate (FG) analog non-volatile memory array for analog in-memory computing fabricated in a standard 65 nm CMOS. We use a model of retention-loss statistics calibrated with...

---

### 28. The K-SCAN Clustering Algorithm

**Authors:** Filip Kosiorowski, Grzegorz Sroka

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24537v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24537v1)

**Summary:** In the Big Data era, the scalability of clustering algorithms constitutes a key challenge. Traditional density-based methods (e.g., DBSCAN) offer robustness to noise and the ability to detect non-linear clusters, yet their quadratic time complexity $O(N^2)$ drastically limits their applicability. Conversely, partitional algorithms (e.g., K-Means), with their linear complexity $O(N)$, impose sphericity on the resulting groups and fail in the presence of outliers. This paper presents K-SCAN -- a n...

---

### 29. What EEG Foundation Models Encode: Dataset Identity and a Negative-Control Suite for Clinical Benchmarks

**Authors:** Marzieh Zare

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24519v2) | 📄 [PDF](https://arxiv.org/pdf/2607.24519v2)

**Summary:** Pretrained EEG foundation models are proposed for clinical decoding, but whether reported gains transfer across populations or survive negative controls is unclear. We benchmark LaBraM, EEGMamba, CBraMod, REVE, LEAD, BENDR, and BIOT on five clinical tasks across four datasets. Primary analyses use frozen linear probes with subject-disjoint LOSO or grouped five-fold validation. Because CAUEEG releases no patient identifiers, it is evaluated at recording level with a patient-disjoint sensitivity. ...

---

### 30. Limbomorphs

**Authors:** Alex Alvarez, Michael Levin

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23842v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23842v1)

**Summary:** Artificial life systems are typically defined by a set of dynamical rules over an environment, an agent, or both, from which lifelike patterns may emerge. Gifbreeder is an animated version of the interactive evolutionary computation (IEC) platform Picbreeder, and was initially created to generate visual art. Instead of encoding the agent or the environment, Gifbreeder genomes encode a spatiotemporal field and evolve through the user's aesthetic selection. The evolved expressions can sometimes re...

---

### 31. Provable Speedups From Dynamic Population Sizes in Evolutionary Algorithms for Multiobjective Optimization

**Authors:** Andre Opris

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23800v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23800v1)

**Summary:** This paper investigates the role of dynamic population sizes in evolutionary multi-objective optimization. Although such approaches are widely used in practice, their benefits remain poorly understood, and rigorous runtime analyses explaining when and why they help are still scarce. To address this, we introduce the bi-objective problem class CLIMB and analyze the runtime of GSEMO and the widely used NSGA-II on this problem. Our results show that allowing a dynamic population size for NSGA-II ca...

---

### 32. Benchmarking Zero-Shot LLM-Generated Parent Selection in Genetic Programming for Symbolic Regression

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23505v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23505v1)

**Summary:** Parent selection significantly affects exploration, exploitation, and complexity control in genetic programming (GP) for symbolic regression. It is unclear whether large language models (LLMs) can synthesize effective operators in a zero-shot setting without iterative meta-evolution. Here, zero-shot means that the model receives only the task description, with no reference operators or iterative feedback. In this work, we benchmark zero-shot synthesis of parent-selection operators across eight L...

---

### 33. Constraint-Bound Agnostic Bayesian Optimization: One Model for All Thresholds

**Authors:** Jin Wang, Xi Lin, Handing Wang

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23448v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23448v1)

**Summary:** Expensive constrained optimization problems in real-world industry design often involve constraint thresholds that are difficult to determine in advance. Engineers may need to adjust constraint thresholds to explore different feasibility-performance trade-offs, requiring solutions under a wide range of threshold settings. However, existing constrained Bayesian optimization methods treat each threshold configuration independently, leading to repeated optimization and failing to exploit the shared...

---

### 34. A genetic algorithm for student academic resource allocation

**Authors:** Ana F. Hernández, Andrej Franulic, Fernando Jiménez

**Published:** 2026-07-25

🔗 [Paper](http://arxiv.org/abs/2607.23316v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23316v1)

**Summary:** The optimal allocation of academic resources to individual students is essential for addressing learner diversity and fostering equitable educational outcomes. Within the framework of the Erasmus+ KA220-SCH project, this paper models the selection of educational materials for high school mathematics students as a 0--1 binary combinatorial optimization problem subject to strict study time constraints. Given the NP-hard complexity of the formulation, exact solution methods become computationally i...

---

### 35. Continuous surrogates versus threshold Boolean networks for modeling Arabidopsis ISR gene regulation

**Authors:** Gonzalo A. Ruz

**Published:** 2026-07-25

🔗 [Paper](http://arxiv.org/abs/2607.23289v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23289v1)

**Summary:** Gene regulatory network modeling often requires balancing predictive accuracy and mechanistic interpretability. In this work, we compare continuous surrogate models and a discrete mechanistic model on the same \textit{Arabidopsis thaliana} induced systemic resistance (ISR) dataset, using both the raw continuous gene-expression measurements and their sign-binarized representation. The study considers eight defense-related genes measured over nine time points and evaluates two continuous predictor...

---

### 36. Sensitivity of hMPA to Controlled CEC 2017 Transformations

**Authors:** Grzegorz Sroka, Sławomir T. Wierzchoń

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22862v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22862v1)

**Summary:** The standard CEC 2017 benchmark applies bias, shift, and rotation simultaneously, confounding their individual effects on algorithmic behavior. We introduce a parameterized implementation that controls these transformations independently while preserving the original functions and transformation data. The framework diagnoses the hybrid Marine Predators Algorithm (hMPA), whose predicted-candidate mechanism depends on numerical objective values and coordinate-wise reconstruction. DSC and extended ...

---

### 37. Closed-Loop Generative Selection: Convergence, Memory, and Noisy Oracles

**Authors:** Konstantin Fackeldey, Christof Schütte

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22211v1)

**Summary:** Closed-loop generative selection has become a workhorse of computational drug discovery: a learned generative model proposes candidate molecules, a fitness oracle scores them, the best are kept, and the model is retrained on this elite set before the next round. Despite its wide use, the method has lacked a rigorous convergence theory, largely because retraining the model each round breaks the Markov property on which classical evolutionary-algorithm analysis relies. We develop a self-contained ...

---

### 38. On the Runtime Analysis of Reinforcement Learning Hyper-Heuristics

**Authors:** Pietro S. Oliveto, Zhenyu Wang, Peizhou Wu, et al.

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22036v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22036v1)

**Summary:** Selection Hyper-heuristics (HHs) automate algorithmic design by selecting from a set of low-level heuristics which one to apply at each stage of the optimisation process. Several impressive results have been recently rigorously proven regarding the performance of selection hyper-heuristics (HHs) for standard benchmark functions. However, the learning mechanisms employed by these HHs are considerably simplified compared to the machine learning techniques typically used in real world applications....

---

### 39. NeuroSynth: A Biologically Inspired Continual Reinforcement Learning Architecture for Mitigating Catastrophic Forgetting

**Authors:** Yash Kini

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.28663v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28663v1)

**Summary:** Artificial Intelligence (AI) systems often perform well on isolated tasks but struggle under continual learning conditions, where training on new tasks can overwrite previously acquired knowledge, a failure mode known as catastrophic forgetting. Biological learning systems reduce this interference through complementary memory processes involving rapid hippocampal encoding and slower cortical consolidation. This study introduces NeuroSynth, a brain-inspired continual reinforcement learning archit...

---

### 40. Search Hardness-Aware LLM-Based Problem Formulation for Expensive Simulation-Driven Design

**Authors:** Yuchen Li, Handing Wang, Bing Xue, et al.

**Published:** 2026-07-23

🔗 [Paper](http://arxiv.org/abs/2607.21220v1) | 📄 [PDF](https://arxiv.org/pdf/2607.21220v1)

**Summary:** Expensive simulation-driven design is widely used in engineering to identify requirement-satisfying designs with as few high-fidelity simulations as possible. Most existing efforts address this challenge by improving optimization algorithms under fixed formulations, yet the formulation itself shapes the search landscape by defining the objectives and constraints optimized by the solver. Recent LLM-based automatic problem formulation methods generate formulations from natural-language requirement...

---

### 41. Learning to Access Computation: Accessibility Plasticity as a Principle of Adaptive Intelligence

**Authors:** Zhaowen Fan

**Published:** 2026-07-23

🔗 [Paper](http://arxiv.org/abs/2607.22748v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22748v1)

**Summary:** Modern neural networks primarily adapt through parameter modification within predefined computational structures. While recent methods introduce modularity, conditional computation, and parameter-efficient adaptation, they generally do not distinguish computational capability from computational accessibility as separate adaptive variables. This work introduces Accessibility Plasticity, a principle of adaptive computation in which systems adapt not only by changing what computation exists, but al...

---

### 42. Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay

**Authors:** Xiaolong Li, Zhangchen Zhou, Zhi-Qin John Xu

**Published:** 2026-07-23

🔗 [Paper](http://arxiv.org/abs/2607.21005v1) | 📄 [PDF](https://arxiv.org/pdf/2607.21005v1)

**Summary:** Most explanations of training instability focus on \emph{learning-rate criticality}, typically characterized by the Edge of Stability, beyond which optimization becomes unstable. We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}. This criticality is induced by the interaction between normalization (which introduces scale-invariant components) and weight decay (which persistently shrinks parameter norms). As the we...

---

### 43. Memoir: Should a Model Write to Its Memory While It Thinks?

**Authors:** Jaber Jaber, Osama Jaber

**Published:** 2026-07-22

🔗 [Paper](http://arxiv.org/abs/2607.20792v1) | 📄 [PDF](https://arxiv.org/pdf/2607.20792v1)

**Summary:** Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective. We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. On procedural associative recall with key interference, we compare a coupled arm against an otherwise identical read-only pondering arm. Both arms contain 81,738 parameters, including 76,362 trainable parameters, and use matched declared forward multi...

---

### 44. Shallower ReLU Network Representations via Exact Linear Algebra

**Authors:** Kilian Rueß, Gennadiy Averkov, Florestan Brunck, et al.

**Published:** 2026-07-22

🔗 [Paper](http://arxiv.org/abs/2607.21651v1) | 📄 [PDF](https://arxiv.org/pdf/2607.21651v1)

**Summary:** We prove that the maximum of $n$ real numbers is exactly representable by a ReLU network with two hidden layers for every $n\le 10$. The constructions are obtained by reducing the problem to exact rational linear algebra: after a symmetry reduction, the necessary cancellations are encoded in finite linear systems over $\mathbb{Q}$, which we solve and verify computationally. The representation of $\max_{10}$ has a structured first hidden layer consisting only of pairwise maxima, a feature that al...

---

### 45. The Giant Hippocampus: From Structural Monoculture to a System of Systems

**Authors:** Jaeho Seol

**Published:** 2026-07-22

🔗 [Paper](http://arxiv.org/abs/2607.19973v1) | 📄 [PDF](https://arxiv.org/pdf/2607.19973v1)

**Summary:** AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech. Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integration - different jobs solved by different structures. This paper argues the gap is a structural error, not a stylistic one, and is measurable. A century of cytoarchitecture, from Brodmann to single-c...

---

### 46. SpikingMOT: A Spike-Driven Multi-Object Tracker

**Authors:** Yiding Sun, Xiangyang Yang, Dongxu Zhang, et al.

**Published:** 2026-07-22

🔗 [Paper](http://arxiv.org/abs/2607.19875v1) | 📄 [PDF](https://arxiv.org/pdf/2607.19875v1)

**Summary:** Multi-object tracking (MOT) plays a fundamental role in visual perception, where accurate trajectory prediction is essential for reliable target association under complex motion patterns. Recent trackers have improved motion modeling with densely activated artificial neural networks, yet they largely overlook whether such dense responses are necessary for trajectory prediction. In this paper, we formulate activation sparsity preference (ASP) by tackling two key questions: 1. How can we identify ...

---

### 47. Learning the Arabic Dialect Continuum as a Continuous Space: A Regression Approach to Speaker Origin Prediction

**Authors:** Mohamed Aziz Khadraoui, Adel Ammar, Bilel Benjdira, et al.

**Published:** 2026-07-22

🔗 [Paper](http://arxiv.org/abs/2607.19751v1) | 📄 [PDF](https://arxiv.org/pdf/2607.19751v1)

**Summary:** We present a regression-based approach to Arabic dialect geolocation that models dialectal variation as a continuous geographic space rather than discrete categories. Speaker origin is predicted as continuous latitude-longitude coordinates using a hierarchical neural architecture that fuses frame-level XLS-R-300M and Whisper-large-v3 encoder representations with phonotactic descriptors through a Transformer encoder and a learnable attention-pooled query. A spherical geodesic loss directly optimi...

---

### 48. Spiking Neural Networks for fMRI-Based Visual Semantic Decoding

**Authors:** Jiahong Zhang, Jinning Zhao, Sijun Shen, et al.

**Published:** 2026-07-21

🔗 [Paper](http://arxiv.org/abs/2607.19170v1) | 📄 [PDF](https://arxiv.org/pdf/2607.19170v1)

**Summary:** Functional magnetic resonance imaging (fMRI)-based visual decoding aims to recover visual information from measured brain activity, commonly by mapping fMRI responses into latent visual features for downstream decoding tasks. Most existing methods learn mappings from fMRI responses to visual features extracted by artificial neural networks (ANNs), yet it remains unclear whether ANN-derived features provide suitable targets for brain decoding. In this study, we investigate spiking neural network ...

---

### 49. Towards chemistries in dynamical systems

**Authors:** Martin Biehl, Nathaniel Virgo

**Published:** 2026-07-21

🔗 [Paper](http://arxiv.org/abs/2607.19090v1) | 📄 [PDF](https://arxiv.org/pdf/2607.19090v1)

**Summary:** Chemistry describes aspects of the universe in terms of molecules and their reactions. In this exploratory work we present a way to describe aspects of any dynamical system in similar terms. To describe a dynamical system in this way three decisions have to be made. The first is how many different "places" there are at which molecules or chemical species can occur; the second is how to determine the species present (or not) at each place; and the third is the set of transitions and reactions tha...

---

### 50. How the fly holds a single goal: normalization, not selection, in Drosophila FC2

**Authors:** Gioele Nanni, Christopher Lee

**Published:** 2026-07-21

🔗 [Paper](http://arxiv.org/abs/2607.18969v1) | 📄 [PDF](https://arxiv.org/pdf/2607.18969v1)

**Summary:** A walking fly steers toward a goal direction, held as a bump of activity across the FC2 neurons of the fan-shaped body. These neurons also inhibit one another over distance, more strongly the farther apart they are, a feedback proposed to keep the fly on a single goal. We asked, from the connectome, what circuit produces this inhibition, and whether it lets FC2 actively choose one goal among competitors (a winner-take-all) or simply keeps a goal set elsewhere as one clean bump. Tracing the wirin...

---

## q-bio.NC

**50 papers**

### 1. Persistent homology broadens the controllable subspace in human structural connectomes

**Authors:** Carter Sale, Marco Coraggio, Mengsen Zhang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03181v1)

**Summary:** Network control theory applied to structural connectomes typically ranks brain regions as candidate driver nodes by their structural connectivity strength, and evaluates performance through scalar control energy. We test whether this framing captures the most relevant information about how driver-node selection shapes brain network control. We introduce an alternative criterion based on the persistent topological cycles in which each node participates---a measure of mesoscale integration that ca...

---

### 2. A Landau-Ginzburg Phenomenology of Sleep-Stage Transitions

**Authors:** Alexander Poltorak

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03000v1)

**Summary:** Sleep staging provides a reproducible clinical description, but it does not by itself explain why some boundaries are abrupt while others are graded, or why transition windows contain instability, synchrony, and apparent state coexistence. We develop a local Landau-Ginzburg phenomenology in which each boundary is represented by motion in an effective potential of a spatially extended, noisy, dissipative neural field. A latent cortical-ordering coordinate phi is inferred from prespecified EEG/PSG...

---

### 3. Modelling temporal dynamics of suicidal ideation and behaviour across pre- to early adolescence using a Markov framework

**Authors:** Sieun Lee, Ben Cardoen, Marianne Etherson, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02896v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02896v1)

**Summary:** Understanding the dynamics of suicidal ideation and behaviour in youth and the factors associated with transitions from thoughts to behaviours is critical for early identification, monitoring, and prevention. Using longitudinal self-report data from the Adolescent Brain Cognitive Development (ABCD) Study (n = 11,864) spanning ages 9 to 13 years, we developed a time-inhomogeneous discrete-time Markov chain framework to model transitions across eight states defined by suicidal ideation and behavio...

---

### 4. Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG

**Authors:** Jacob Kang, Jong-Hyeon Seo

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02804v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02804v1)

**Summary:** Recent studies have reported clearly identifiable dynamical changes in the high-frequency range of EEG signals recorded during specific stimuli, such as visual or auditory inputs, or in cases of brain disorders like epileptic seizures. In this study, we utilized Dynamic Mode Decomposition (DMD) to extract consistent and persistent dynamical changes in the high-frequency band from the signals of neurologically relevant EEG channels. High-frequency DMD modes were employed as features, composing a ...

---

### 5. Predictive Set Theory: A Generative Framework for Cognitive Architecture with Operationalized Core Mechanisms

**Authors:** Yiyang Yu

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02704v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02704v1)

**Summary:** Predictive processing theories portray the brain as a hierarchical prediction engine that minimizes prediction error, yet they lack operational definitions for the structure of a "prediction," the standardized response to a prediction error, and the mechanism that maintains consistency across successive updates. Bayesian cognitive science attempts to subsume all uncertainty under probabilistic belief updating, but it presupposes a closed hypothesis space and provides no generative account of how...

---

### 6. Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory

**Authors:** Zhaotian Gu, Jie Su, Weiwei Wang, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01947v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01947v1)

**Summary:** The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...

---

### 7. NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics

**Authors:** Zijian Dong, Jianxiong Zhou, Kwun Kei Ng, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01773v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01773v1)

**Summary:** Forecasting human brain activity during naturalistic experience requires modeling how endogenous neural states evolve causally under continuous sensory drive. Existing brain encoding models instead frame this as stimulus-to-response regression without strict temporal constraints, allowing future stimuli to leak into current predictions. We introduce NeuroWorld, to our knowledge the first brain world model, which casts naturalistic brain functional dynamics prediction as stimulus-conditioned evol...

---

### 8. Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval

**Authors:** Ilia Semenkov, Daria Kleeva, Ivan Dakhtin, et al.

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01481v1)

**Summary:** Short segments of perceived speech can be retrieved from non-invasive magnetoencephalographic (MEG) recordings by deep networks trained with a CLIP-style objective against wav2vec 2.0 audio embeddings. Yet their weights do not map onto electrophysiological quantities, and it remains unclear which speech properties drive retrieval.   We build on a high-performing MEG-to-audio retrieval architecture but redesign both its front end and decoder. Its spatial attention operates on a flattened sensor l...

---

### 9. Statistical Mechanics of Learning on Product Wasserstein Manifolds

**Authors:** Srinivasa Rao P Vangmayi P Reddy

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01434v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01434v1)

**Summary:** Normally the statistical mechanics of learning treats constraints on weight distributions as restrictions that shrink the space of possible solutions. Therefore, it reduces model capacity. In this paper we would like to take a contrary approach, which, however, is based on the earlier work on distribution-constrained perceptrons. Rather than treating a prescribed weight distribution as a mere restriction, we propose that it defines the intrinsic geometry upon which learning naturally unfolds. We...

---

### 10. Data augmentation as a framework for modeling hippocampal contributions to generalization

**Authors:** Tyler Bonnen, Andrew Kyle Lampinen

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01297v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01297v1)

**Summary:** The hippocampus plays a critical role in generalization, enabling us to flexibly repurpose prior experiences to perform novel tasks. Here we suggest that data augmentation---a machine learning strategy to improve generalization by refactoring prior experience---offers a useful framework to conceptualize and model hippocampal function. We begin by outlining how data augmentation operates across two timescales: the traditional ``offline'' setting, where refactoring training data yields more genera...

---

### 11. Deep Learning CNN and Recurrence Analysis for Alpha Gamma EEG Biomarkers in Fragile X Syndrome

**Authors:** Zag ElSayed, Payton Siekierski, Jack Yanchen Liu, et al.

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00835v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00835v1)

**Summary:** Fragile X Syndrome (FXS) is a neurodevelopmental disorder caused by reduced expression of fragile X mental retardation protein (FMRP), leading to disrupted synaptic plasticity, cortical hyperexcitability, and impaired network synchronization. Electroencephalography (EEG) provides a noninvasive window into these mechanisms and consistently reveals abnormalities in alpha (8 to 12 Hz) and gamma (30 to 100 Hz) oscillations that relate to inhibitory control, sensory processing, and cognition. This pa...

---

### 12. Recursive Gaussian Processes and the Bayesian Brain

**Authors:** Moumita Das, Dipanjan Ray, Sourabh Bhattacharya

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00503v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00503v1)

**Summary:** Predictive coding offers a powerful framework for cortical computation, yet scalable implementations that respect both Bayesian exactness and neurobiological constraints remain scarce. We bridge this gap by formally connecting predictive coding to Recursive Gaussian Processes (RGPs). RGPs employ a single Gaussian process \( g(t, \cdot) \) indexed by layer index and input value, preventing the representational collapse of standard deep Gaussian processes while allowing learnable cross-layer depen...

---

### 13. Mechanistic bridges from receptors to whole-brain dynamics: mean-field reductions, validity domains, and computational trade-offs

**Authors:** Yannael Bossard, Lehna Bekri, Alain Destexhe

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00306v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00306v1)

**Summary:** Many pharmacological and pathological mechanisms act at molecular, synaptic, or cellular scales, whereas the resulting phenomena of interest are often measured at the level of cortical populations and whole-brain recordings. This scale gap motivates reduced models that remain biologically interpretable while being tractable enough for whole-brain simulation, parameter exploration, and comparison with empirical signals. This review examines the receptor-aware whole-brain framework of Sacha et al....

---

### 14. Cross-Task Dissociation in Frontier Vision-Language Model Theory of Mind

**Authors:** Kejia Zhang, Youran Sun, Chugang Yi, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00261v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00261v1)

**Summary:** Do frontier vision-language models present a coherent Theory-of-Mind (ToM) profile across tasks, matching the same human reference group, or does that profile fragment from one paradigm to the next? We evaluate a shared panel of nine frontier VLMs on two psychology-derived benchmarks: the Keysar Director Task (visual perspective-taking under egocentric interference) and the Frith-Happé animated triangles scored with the Castelli rubric (intention attribution from pure motion). On the Director Ta...

---

### 15. Dynamical principles of habituation across substrates and scales

**Authors:** Matthew Smart, Stanislav Y. Shvartsman, Martin Mönnigmann

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00249v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00249v1)

**Summary:** Habituation is a basic form of learning in which a system's response to repeated stimulation progressively diminishes but eventually recovers when the stimulus is withheld. Long studied in animals, it has increasingly been observed in unicellular organisms and non-living devices such as electronic circuits and neuromorphic materials, suggesting underlying dynamical principles that recur across domains. This review asks what those principles are: given qualitative constraints imposed by habituati...

---

### 16. Quantifying the cost of network computations to unpack structure-function relationships in the brain

**Authors:** Suman S. Kulkarni, Jason Z. Kim, Panagiotis Fotiadis, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29537v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29537v1)

**Summary:** The brain supports computations through coordinated patterns of activity on an underlying network. These networks---from microscale navigational circuits in insects to macroscale brain areas in humans---are organized in structured ways that are thought to support their function. We seek a unifying quantitative framework to understand how network structure shapes the computations a network can readily support. To do so, we frame computation as a goal-directed transition of activity and quantify i...

---

### 17. Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding for Cross-Site MDD Identification from rs-fMRI

**Authors:** Zhanpeng Zheng, Xiran Chen, Haiteng Jiang, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29531v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29531v1)

**Summary:** Cross-site identification of major depressive disorder (MDD) from resting-state functional magnetic resonance imaging (rs-fMRI) is hindered by inter-site distribution shifts and heterogeneous functional connectivity (FC) views. These views capture complementary neural relationships but exhibit distinct site biases and graph topologies, complicating alignment without sacrificing disease-relevant information or cross-view consistency. Existing studies largely treat multi-view connectome learning a...

---

### 18. Resource depletion accelerates rate learning but not composition learning in patch foraging

**Authors:** Zachary P. Kilpatrick, Ahmed El Hady

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29476v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29476v1)

**Summary:** Foraging is a universal animal behavior that has increasingly attracted the interest of both experimentalists and theorists. Most prior models assume an animal knows the distribution of resources in its environment, but this structure must be learned as the animal explores its environment. Foraging can thus be regarded as a hierarchical inference problem. We develop a normative Bayesian account of an agent learning a patchy environment while exploiting it, and show that resource depletion shapes...

---

### 19. metasignal: A Python Package for Comprehensive Metacognitive Analysis and Decision-Making

**Authors:** Saurabh Ranjan, Mukesh Makwana, Konstantina Sokratous, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29093v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29093v1)

**Summary:** Metasignal is an open-source Python package for signal detection theory (SDT) and metacognitive measurement. It implements the 17 metacognitive measures evaluated by Rahnev (2025), together with the reference variables d' (perceptual sensitivity), response criterion c (response bias), and mean confidence. The 17 measures comprise three meta-d' family estimates, meta-d', M-ratio, and M-difference; four nonparametric Type-2 measures, the Type-2 area under the receiver-operating-characteristic curv...

---

### 20. Critical Flicker Fusion Frequency As A Falsifiable Boundary Between Plastic And Non-Plastic Neural Systems

**Authors:** Natalia D. Rydzenska, Pawel J. Winklewski, Michal W. Blaszczyk-Niezgoda, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29068v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29068v1)

**Summary:** Experience-dependent neural plasticity is fundamental to adaptive behaviour, yet certain perceptual abilities resist modification despite extensive training. Critical flicker fusion frequency (CFFF), the threshold at which flickering light appears continuous, is a foundational constraint in visual temporal processing that shows exceptional within-individual stability in adults, contrasting sharply with the highly plastic spatial abilities processed through the same cortical pathways. This review...

---

### 21. But What Behavior?

**Authors:** Robert C. Froemke

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28898v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28898v1)

**Summary:** What is a natural behavior? I argue that the study of natural behaviors is often the study of the spontaneous behaviors of animals placed in quantifiably different environments. For behavioral generalists such as rodents, humans, and many other species, there may be no such definable construct as a native habitat or natural behavior, due to their successful abilities and needs to rapidly adapt to a wide range of different ecosystems. Instead of prioritizing naturalness, it may be more essential ...

---

### 22. Bits per Spike as a Betting Game: An Interpretable Unit for Held-Out Log-Likelihood in Neural Data Analysis

**Authors:** Alex H. Williams

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28779v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28779v1)

**Summary:** Held-out log-likelihood is the standard currency for comparing statistical models of neural spike trains, and is often reported as bits per spike relative to a homogeneous Poisson baseline. The units of this metric are difficult to reason about: it is rarely obvious whether an improvement of, say, $0.34$ bits per spike is a large effect or a negligible one. This note develops an interpretation of held-out log-likelihood borrowed from game-theoretic statistics. A fitted model $Q$ is treated as a ...

---

### 23. Using Theory of Mind to Arbitrate between Social and Non-social Learning

**Authors:** Lance Ying, Ryan Truong, Joshua B. Tenenbaum, et al.

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28601v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28601v1)

**Summary:** Social learning is a powerful mechanism through which agents learn about the world from others. However, humans sometimes choose direct experience over social learning, which can carry time and cognitive resource costs. How do people balance social and non-social learning? We propose a Rational Mentalizing model of the decision to engage in social learning. This model estimates the utility of social learning by reasoning about another agent's goal and the informativeness of their future actions....

---

### 24. Stimulus-Evoked Network Dynamics in Human Cortical Organoids: From a Graph-Computational Framework to Repeated-Stimulation Depression

**Authors:** Esmaeil S. Nadimi, Vinay C. Gogineni, Jan-Matthias Braun, et al.

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28068v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28068v1)

**Summary:** Human cortical organoids provide an experimentally accessible model of early neural circuit formation, yet whether their activity reflects structured information processing rather than spontaneous synchronization is unclear. We developed a graph-computational framework to quantify stimulus-evoked propagation. This includes stimulus-conditioned functional graphs, a graph-constrained dynamical (graph-neural-network) model used as a system-identification tool, a biological message-passing principle...

---

### 25. MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification

**Authors:** Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.28681v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28681v1)

**Summary:** Functional magnetic resonance imaging (fMRI) is a widely used technique for studying the brain. Recent methods that utilize graph neural networks (GNNs) for analysis of brain functional connectivity have shown great potential for the classification of brain disorders, such as Alzheimer's disease (AD). However, these methods often assume a preset number of functional modules across all subjects, which overlooks inter-subject variability. In addition, the discovered modules are rarely used to dire...

---

### 26. ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution

**Authors:** Christopher Warner, Jonas Mago, JR Huml, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.27308v1) | 📄 [PDF](https://arxiv.org/pdf/2607.27308v1)

**Summary:** We introduce ZUNA1.1, a 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction. ZUNA1.1 is capable of reconstructing variable length sequences of up to 30s, with an arbitrary number of EEG channels at arbitrary scalp locations, and can reconstruct arbitrary temporal intervals within channels in addition to reconstructing entire channels. We demonstrate that ZUNA1.1 performs at least on par with our earlier ZUNA1 model, while being far more flexible and capable of handling a ...

---

### 27. Artificial intelligence in deep brain stimulation for movement disorders: a systematic review and technology readiness assessment

**Authors:** Zohra Souei, Muhammad Mushhood Ur Rehman, Harith Akram, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26666v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26666v1)

**Summary:** Artificial intelligence (AI) is increasingly explored across deep brain stimulation (DBS) for movement disorders, yet whether current systems are approaching deployment remains unclear. To characterise their scope, validation maturity, and translational readiness, we systematically evaluated 239 peer-reviewed studies published between 2000 and 2025, assessing AI methods, validation practices, and barriers constraining clinical translation. Research was dominated by Parkinson's disease and subtha...

---

### 28. Pragmatic Reasoning in Design

**Authors:** Lance Ying, William Van Uitert, Tan Zhi-Xuan, et al.

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26322v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26322v1)

**Summary:** People can often understand and use novel artifacts after only a few interactions, suggesting that design choices communicate underlying affordances and causal structure. We propose a formal account of this process by framing cooperative, user-centered design as a cooperative game in which the user is the principal and the designer is an assistant. Inspired by prior work on pragmatic communication (e.g. RSA), our model treats a designer's design decisions as communicative signals and predicts us...

---

### 29. Three Failures of Pain Location: Why the Diagnostic Utility of Symptom Localization Is Not One Thing

**Authors:** Adam Y Shavit

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26297v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26297v1)

**Summary:** Patient-reported pain location is diagnostically decisive for some presentations and nearly uninformative for others. The prevailing account treats this as a single gradient of diagnostic utility governed by anatomical complexity. That explanation conflates three epistemically distinct failures of localization, each with its own mathematical structure, optimal instrument, and public-health consequence. In anatomical multiplexing (a), many structures share one location: a non-identifiable inverse...

---

### 30. A behavior-environment information loop drives sensory navigation

**Authors:** Kevin S. Chen, Matthew P. Leighton, Damon A. Clark, et al.

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26295v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26295v1)

**Summary:** As organisms navigate the environment to locate critical resources, their behavioral actions must be tightly coupled to their sensory inputs. Here, we introduce an information-theoretic framework that quantifies this coupling using transfer entropy, which measures information flow between sensory inputs and behavioral outputs. Information flow from sensory inputs to behavior defines a "reactive" component of a navigational strategy, whereas information flow from behavior to sensory inputs define...

---

### 31. Cognitive Convergence: Deep Similarities Between Large Language Models and Human Cognition

**Authors:** Chandra Sripada, Richard Lewis

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26179v1)

**Summary:** LLMs are widely regarded as alien intelligences, systems whose cognitive operations are fundamentally unlike our own. Apparent similarities to human cognition are therefore often seen as the result of anthropomorphic projection. We argue that this framing is mistaken. LLMs clearly differ from humans in important respects, including their physical substrate, learning history, and the environments with which they interact. These differences make it all the more striking that contemporary LLM-based...

---

### 32. Phantom Evidence: How and Why Generative AI Manufactures False Positives in Science

**Authors:** Yukiyasu Kamitani, Ken Shirakawa

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.25991v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25991v1)

**Summary:** Four centuries ago Francis Bacon warned against the anticipations of nature, hasty generalization that wins assent on a few facts, and set against it the table of absence: checking that a property fails to appear where it should not. The demand was that looking convincing should not, on its own, count as evidence. Science has professed that demand ever since, while in practice letting persuasiveness do the work of evidence. It could be let to do so because making something persuasive was itself ...

---

### 33. GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling

**Authors:** Lluc Bono Rosselló

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.25787v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25787v1)

**Summary:** The Information Dynamics of Music model (IDyOM) has played a central role in computational accounts of musical expectation by providing event-by-event estimates of uncertainty and surprise from symbolic musical sequences. However, its reference implementation is difficult to integrate with contemporary Python workflows, and its internal memory structures are not easily accessible for inspection or modification. We introduce GraphIDyOM, a graph-native Python reimplementation of IDyOM that represe...

---

### 34. Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference

**Authors:** Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25131v1)

**Summary:** Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visua...

---

### 35. CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification

**Authors:** Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25045v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25045v1)

**Summary:** Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a ...

---

### 36. A Tuning-Free Variational Framework for Muscle Redundancy Resolution: Torque Fiber Proximal Dynamics with Active-Set Switching and EMG-Validated Activation Prediction

**Authors:** Morteza Ganji

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25013v2) | 📄 [PDF](https://arxiv.org/pdf/2607.25013v2)

**Summary:** Muscle redundancy can be formulated as a constrained selection on a time-varying convex set of feasible activations. We introduce Torque Fiber Proximal Dynamics (TFPD), where activation evolves as the Euclidean projection of the previous state onto a convex polytope defined by torque equality and physiological bounds. TFPD is equivalent to a backward-Euler discretization of a sweeping process and a variational inequality with a maximal monotone normal cone operator. Within this framework, antago...

---

### 37. When Branch-Local Shunting Helps: A Gain-Load-Alignment Principle for Dendritic E/I Networks

**Authors:** Houman Safaai, Maceo Richards, Naeem Khoshnevis, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24990v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24990v1)

**Summary:** Biological neurons combine excitatory and inhibitory (E/I) activity on branched dendrites through shunting, in which inhibition divisively attenuates excitation. Whether this improves population readout over additive E/I integration of the same nonnegative inputs remains unclear. We introduce DendriNet, a trainable framework that varies integration rule, morphology, synaptic allocation, divisor locality, and dendritic nonlinearities. For population codes with multiplicative gain, a local lineari...

---

### 38. Synaptic clustering emerges from learning and supports covariance discrimination

**Authors:** Ilenna Simone Jones, Maceo Richards, Houman Safaai, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24503v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24503v1)

**Summary:** Functional synapse clusters (FSCs) are synapses with correlated presynaptic activity that are colocalized on the same neuronal dendritic branch. FSCs have been observed after learning in cortical and hippocampal pyramidal neurons. However, previous efforts to ablate FSCs by pharmacologically blocking dendritic nonlinearities to establish causal necessity may have confounded effects. Therefore, whether FSCs are causally necessary for computation is unknown. Here, we attempt to isolate FSCs from t...

---

### 39. A Neural Network model of Cultural Evolution

**Authors:** Kingsley J. A. Cox, Paul R. Adams

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24886v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24886v1)

**Summary:** It has been proposed (Richerson and Boyd, 2008) that human intelligence is underpinned by a ratchet-like process called Cultural Evolution in which ideas, originated by individuals, can selectively spread by social learning and replace older, less fruitful ones. Useful ideas can thus accumulate beyond the lifetime of individuals. Although both social and individual learning are thought to be achieved by the selective activity-dependent adjustment of synaptic strengths in an artificial neural net...

---

### 40. Optimal stimulation sites are not the most affected: personalised models of resting-state fMRI in Alzheimer's disease

**Authors:** Cristiano Capone, Enza Cece, Andrea Ciardiello, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24356v2) | 📄 [PDF](https://arxiv.org/pdf/2607.24356v2)

**Summary:** Resting-state functional connectivity (FC) is altered in Alzheimer's disease (AD), widely regarded as a distributed network process; whether its signature reduces to a few focal sites has not been tested causally, a question central to targeted neuromodulation. We fit subject-specific, cross-subject-identifiable models whose free-running dynamics reproduce those of each individual patient. The fitted model parameters classify AD from controls at modest accuracy, below that of structural atrophy;...

---

### 41. Dynamic sampling of non-stationary spontaneous activity in dissociated neuronal networks

**Authors:** Kazushi Takehana, Dai Akita, Hirokazu Takahashi

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24269v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24269v1)

**Summary:** Objective. To develop and evaluate an adaptive electrode-selection method for tracking non-stationary spontaneous activity during long-term high-density microelectrode array (HD-MEA) recordings under a fixed channel budget.   Approach. We formulated electrode allocation as a sequential subset-selection problem and used a discounted Poisson-Gamma model with Thompson sampling. The method updated electrode-specific activity estimates from observed spike counts and reallocated a fixed channel budget...

---

### 42. Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory

**Authors:** Saurabh Ranjan, Konstantina Sokratous, Brian Odegaard

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.23927v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23927v1)

**Summary:** A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. Here we show, across two experiments and six LLMs, that source attribution depends on how conversational memory is structured: ceiling accuracy for self-generated content under minimal memory dema...

---

### 43. Evaluating Closed-Loop EEG Feedback for Simulated Prosthetic Vision in Immersive VR: A Sham-Controlled Feasibility Study

**Authors:** Ruyi Cao, Lily M. Turkstra, Adyah Rastogi, et al.

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23889v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23889v1)

**Summary:** Visual prostheses require users to interpret sparse and distorted artificial percepts through active visual search. We developed an EEG-guided neuroadaptive training platform for simulated prosthetic vision in immersive virtual reality and evaluated its feasibility in a sham-controlled object-localization task. Twenty-two sighted participants searched a virtual desk scene rendered through a low-resolution phosphene simulation while EEG was recorded using a dry-electrode headset integrated with a...

---

### 44. Universal BCI Personalization: One API for Frozen EEG Trunks and Foundation Models

**Authors:** Sergey Musienko

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22397v1)

**Summary:** Frozen EEG encoders proliferate; per-model fine-tune defaults do not scale. We present Nimbus Personalizer: one contract encode to Bayesian head to BrainState (optional affine mid-tier) that sits on heterogeneous frozen trunks without a new personalization stack per architecture. Thesis (systems): the contribution is the trunk-agnostic API - not LDA-on-embeddings as an ML novelty - so OEMs integrate once and swap trunks. Evidence: the same surface runs on five classical trunks EEGNet, Shallow, D...

---

### 45. On a cross coupling of Rulkov neural maps

**Authors:** Stefano Disca

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22318v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22318v1)

**Summary:** We introduce a novel coupling of Rulkov neural maps, proposing a heuristic biological interpretation for the transition to non-small values of the perturbations acting on the slow variables. We analytically prove that the coupling preserves boundedness of motion and the existence of a snap-back repeller (leading to Devaney chaos by the Marotto theorem), if they are associated to the original system. For the coupling of two standard chaotic Rulkov maps, we present numerical simulations for the or...

---

### 46. NUMA balancing hampering performance of spiking network simulations

**Authors:** Melissa Lober, Alp Inangu, Gorka Peraza Coppola, et al.

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22275v2) | 📄 [PDF](https://arxiv.org/pdf/2607.22275v2)

**Summary:** Computing centers today mostly operate conventional CPU- and GPU-based systems, where the direct way of decreasing energy consumption is a reduction in the applications' runtime. Neuromorphic computing promises an alternative architecture with improved energy efficiency for artificial intelligence. In this endeavor, code for the simulation of large-scale spiking networks on conventional supercomputers is the reference. We show that turning off automatic NUMA balancing may reduce energy consumpti...

---

### 47. Cycles of Discourse, Speech Dysfluency, and Active Inference

**Authors:** Thomas Parr, Birtan Demirel, Youssuf Saleh, et al.

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22180v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22180v1)

**Summary:** Speech is a complex motor and social act. We must not only produce and understand sequences of variable-length words formed of ordered syllables but also speak and listen in turn. This theoretical paper introduces a computational model of speech production and auditory segmentation based upon sequences of discrete phonemes. The purpose of this is to develop a vehicle to test (in silico) hypotheses about the mechanisms that govern loss of speech fluency, something that may happen transiently in p...

---

### 48. Subject-Level Heterogeneity in EEG Motor Imagery Decoding: A Large-Scale Benchmark and Portfolio-Based Reduction of the Search Space

**Authors:** Paul Barbaste, Olivier Oullier, Xavier Vasques

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22778v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22778v1)

**Summary:** Robust EEG motor imagery decoding remains limited by strong inter-individual variability, making it difficult to identify pipelines that generalize across users. We present a large-scale, standardized within-session benchmark of decoding pipelines across three public datasets: Cho2017 (52 subjects), PhysionetMI (109 subjects), and Zhou2016 (4 subjects). Using a common MOABB LeftRightImagery setting, two frequency bands (8-15 Hz and 8-30 Hz), and a broad combination of feature extraction, preproc...

---

### 49. Cross-Cohort Spectral-Temporal Dissociation in Frozen EEG Foundation-Model Representations

**Authors:** Marzieh Zare

**Published:** 2026-07-23

🔗 [Paper](http://arxiv.org/abs/2607.24834v2) | 📄 [PDF](https://arxiv.org/pdf/2607.24834v2)

**Summary:** Objective. We tested whether frozen representations from five EEG foundation models support decoding of long-range temporal correlations, measured as the detrended-fluctuation-analysis (DFA) exponent of the alpha-band amplitude envelope.   Approach. REVE, LaBraM, BENDR, CBraMod, and BIOT were evaluated in CAUEEG and BrainLat. A common 240 s estimator used 8-13 Hz filtering, DFA over 2-23.8 s, artifact masking, and quality control. One fixed nested-cross-validation readout predicted DFA and a fix...

---

### 50. Real-time Reconstruction of Human Visual Perception from fMRI

**Authors:** Rishab S. Iyer, Jiaxin Cindy Tu, Cesar Kadir Torrico Villanueva, et al.

**Published:** 2026-07-23

🔗 [Paper](http://arxiv.org/abs/2607.22753v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22753v1)

**Summary:** Real-time closed-loop neurofeedback based on functional magnetic resonance imaging (fMRI) has led to important scientific and clinical advances. However, the sophistication of the analysis methods used in real-time fMRI lags behind the state-of-the-art in fMRI decoding, largely due to computational factors: Most advanced decoding pipelines do not fit within the envelope of real-time processing, where the analysis needs to be conducted in a matter of seconds and without leveraging data acquired l...

---

## stat.ML

**50 papers**

### 1. Information-Geometric Forward Policy Training in GFlowNets

**Authors:** Yordan Raykov, Rodrigo Veiga

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03967v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03967v1)

**Summary:** Generative Flow Networks (GFlowNets) have emerged as a flexible framework for amortised inference over discrete and mixed discrete-continuous objects, requiring only an unnormalised target density specified through a reward. In this work, we formulate forward-policy training in GFlowNets through the information geometry of the induced trajectory sampler. Treating the forward policy as an induced trajectory sampler, we show that its intrinsic first-order geometry is given by the Fisher-Rao metric...

---

### 2. Robust Low-Tubal-Rank Tensor Completion under Cross-Concentrated Sampling

**Authors:** Hanqin Cai, Longxiu Huang, Jing Qin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03928v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03928v1)

**Summary:** Tensor cross-concentrated sampling (t-CCS) bridges entrywise sampling and t-CUR slice-wise sampling by observing entries only within selected horizontal and lateral slices. Existing t-CCS completion methods, however, assume that the observations are free of gross corruption. In this work, we study robust recovery of a third-order low-tubal-rank tensor from partial t-CCS observations contaminated by sparse, arbitrarily large outliers. We propose Robust Iterative t-CUR (R-ItCUR), a tensor-native a...

---

### 3. Trajectory inference via Acceleration Matching

**Authors:** Bartolo Dazzini, Giovanni Conforti, Alain Durmus, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03916v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03916v1)

**Summary:** Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories that best resemble and interpolate the data. Existing algorithms exhibit computational challenges: they either rely on preprocessing subroutines to enforce smoothness or on simulation-based training objectives, both of which can be expensive. In order to overcome these limitations, we propose a new ...

---

### 4. Confidence Horizons

**Authors:** Chase Mathis, Ian Waudby-Smith

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03889v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03889v1)

**Summary:** Anytime-valid inference enables analysts to continuously monitor their data and stop experiments early. However, the majority of these methods incur a certain conservativeness by remaining valid on infinite time horizons. In practice, a bound on the horizon may be imposed due to budgetary, practical, or ethical constraints. In this paper, we ask the question: "Is it possible to obtain sharper large-sample anytime-valid inference by forgoing validity beyond some finite time horizon?". We provide ...

---

### 5. Divide-and-Conquer: Towards Generalizable Amortized Bayesian Inference for the Drift Diffusion Model

**Authors:** Yufei Wu, Shanqing Gao, Andreas Voss, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03566v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03566v1)

**Summary:** The drift diffusion model (DDM) is a cornerstone of cognitive decision-making research. Although numerous estimation methods exist, researchers continue to seek inference approaches that are both fast and flexible across diverse study designs. Amortized Bayesian inference (ABI) can provide nearly instantaneous inference for complex stochastic models like the DDM, but neural networks trained for one study design cannot generalize to others. In this paper, we propose a divide-and-conquer framework...

---

### 6. When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs

**Authors:** Omatharv Bharat Vaidya, Connor Thomas Jerzak, Zayne Rea Sprague, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03506v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03506v1)

**Summary:** Self-consistency assumes the most frequent answer among sampled reasoning traces is the most reliable, but this can fail in causal reasoning: samples often repeat the same confounding error, and votes fragment across multiple valid answers, letting an invalid answer win despite a valid minority trace. We introduce CALVER (Causal Axiom-Level VERification), a training-free symbolic verifier that scores structured traces against Pearl's causal criteria, including -separation, backdoor adjustment, a...

---

### 7. A fully nonlinear structural vector autoregressive model identified via independent innovation analysis

**Authors:** Savi Virolainen

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03486v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03486v1)

**Summary:** We develop a fully nonlinear structural vector autoregressive framework in which the contemporaneous structural mapping may be nonlinear and non-additive. Identification is achieved by exploiting variation in the conditional distributions of the mutually independent structural shocks induced by an observed exogenous variable. Specifically, a general contrastive learning framework that makes use of this variation together with the assumed exponential-family structure is employed to recover the sh...

---

### 8. Beyond the Gegenbauer Paradigm: q-Orthogonal Kernels for Machine Learning

**Authors:** Álvaro Sánchez-Paniagua Ríos, Juan P. Llerena, Alberto Lastra, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03482v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03482v1)

**Summary:** The performance of Support Vector Machines (SVMs) critically depends on the kernel function choice, which enables implicit mapping of data into high-dimensional feature spaces. While classical kernels like Radial Basis Function (RBF) remain popular, orthogonal polynomial kernels offer mathematically interpretable alternatives that can incorporate structured prior knowledge. This work extends the orthogonal polynomial kernel paradigm by introducing a novel family based on discrete $q$-Hermite I p...

---

### 9. Should the Boundary Term Be Learned in Reflected Diffusion? Conormal Trace and Reflection Masking

**Authors:** Ziyue Wang, Takafumi Kanamori

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03469v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03469v1)

**Summary:** We study score learning for reflected diffusion on bounded domains. Reflection keeps trajectories feasible but does not ensure that the learned score satisfies the boundary behavior implied by the forward process. With implicit score matching, integration by parts leaves a boundary term, and we show that it depends on one scalar at each boundary point: the diffusion- weighted normal component of the score, or conormal trace. The no-flux condition fixes this value while leaving the re- maining bo...

---

### 10. Conformal risk control for model-form uncertainty in parametric non-intrusive reduced-order models

**Authors:** Edgar Jaber, Rémy Vallot, Thibault Dairay, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03360v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03360v1)

**Summary:** Non-intrusive reduced-order models (NIROMs) have become a standard tool for approximating parametric partial differential equations from computer design of experiments while significantly reducing computational costs. However, assessing the reliability of their predictions remains a major challenge, particularly in extrapolation regimes or under limited training data. In this work, we introduce a framework for quantifying model-form uncertainty in NIROMs by combining a perturbative stochastic re...

---

### 11. A Direct Route to Markov Chain Convergence via Asymptotic Equivalence with the Target

**Authors:** Patrick Forré

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03353v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03353v1)

**Summary:** For a Markov kernel $T$ with an invariant probability measure $π$, we give a self-contained proof of the Markov chain convergence theorem via a criterion called asymptotic equivalence with the target. It assumes two parts about the Lebesgue decompositions of $T^{n}_{x}$ and $π$ for every starting point $x$: 1.) asymptotic absolute continuity: the singular mass sing$(T^{n}_{x}\midπ)$ tends to $0$; 2.) asymptotic domination of the target: the singular mass sing$(π\mid T^{n}_{x})$ tends to $0$, as ...

---

### 12. Minimax-Optimal Semiparametric Contextual Dynamic Pricing with Multimodal Revenue

**Authors:** Xueping Gong, Zhuoluo Zhang, Zhaowei Miao, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03142v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03142v1)

**Summary:** We study contextual dynamic pricing with arbitrary covariate sequences and bounded, possibly nonbinary purchase quantities. Demand follows a semiparametric surplus-index model with an unknown linear valuation parameter and an unknown Hölder-smooth response. We impose neither concavity nor strong unimodality on revenue and allow nonunique optimal prices. We develop a pilot-corrected layered decision-partitioning policy that combines directional pilot estimation, local polynomial learning, predict...

---

### 13. Causal Inference with Unstructured Outcomes

**Authors:** Kevin Christian Wibisono, Yixin Wang

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03085v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03085v1)

**Summary:** Causal inference has traditionally centered on scalar outcomes: whether a patient recovers, how much a worker earns, or how many visits a website receives. Modern studies increasingly ask causal questions about outcomes with richer form, such as clinical notes, open-ended survey responses, and images. A hospital may want to know how an AI documentation tool changes the notes physicians write, or how a nurse training program alters what patients say in survey responses. For such outcomes, the usu...

---

### 14. Stochastic Saddle Avoidance Beyond Unit Excitation and Smoothness: A Pathwise Lyapunov-Perron Framework

**Authors:** Junwen Qiu, Bohao Ma, Andre Milzarek, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03001v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03001v1)

**Summary:** Unit excitation (UE) is a common assumption in stochastic saddle avoidance: the stochastic error must have a uniformly positive component along every direction, in expectation. This condition gives a direct way to rule out convergence to strict saddles, but it also oversimplifies the actual noise structure, and does not match many stochastic optimization regimes. In overparameterized or interpolation models, the noise may vanish near stationarity. In finite-sum problems, the stochastic gradient ...

---

### 15. Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores

**Authors:** Zeyu Zhang, Bradly C. Stadie

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.02985v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02985v1)

**Summary:** The standard check for contamination in LLM backtests is simple: compare scores before and after the training cutoff. We show this check is uninformative. Four flagship models fail it on questions they cannot have memorized: every scored question resolved after their cutoffs. The reason is structural. Models legitimately know more about times near their cutoff, so recency mimics leakage, and we prove no passive backtest can separate the two from genuine skill. Measurement, not just detection, re...

---

### 16. Calibrated Bayesian Inference for Stochastic Intervention Effects

**Authors:** Tyler M. Schmidt, Nathan B. Wikle

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02924v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02924v1)

**Summary:** Causal inference increasingly extends beyond classical causal effects defined by deterministic treatment assignments, such as the average treatment effect, to stochastic intervention effects that can weaken positivity requirements and offer greater policy relevance. Nonparametric Bayesian models are attractive for estimating these effects due to their flexibility and inherent uncertainty propagation, but this posterior uncertainty need not be well calibrated for the causal effect of interest. We...

---

### 17. When Predictions Become Regressors: A Split-Sample Correction for Biases in Downstream Inference

**Authors:** Nathan Canen, Ted Enamorado

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02909v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02909v1)

**Summary:** Prediction-based methods, including Large Language Models (LLMs) and other machine learning techniques, are often used to construct measures of political phenomena that are difficult to quantify directly, such as policy positions in manifestos or emotions expressed on social media. In many applications, these prediction-generated measures are used as explanatory variables in regression models, even though they are measured with error. This leads to biased estimates. In this paper, we propose a s...

---

### 18. Particle-based Generalised Stochastic Optimisation

**Authors:** Jiechen Jackie Zhang, O. Deniz Akyildiz

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02844v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02844v1)

**Summary:** We develop a class of diffusion-based stochastic particle optimisation methods for loss functions with intractable gradients. Specifically, we consider problems in which the loss gradient is an integral with respect to a parameter-dependent distribution, a structure that includes training generative models, fine-tuning, and learning latent-variable models. We introduce mean-field dynamics and its interacting-particle approximations, which contain several existing algorithms as special cases and ...

---

### 19. Improved Quantum Algorithms for Reinforcement Learning Under a Generative Model

**Authors:** Joao F. Doriguello

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02826v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02826v1)

**Summary:** Reinforcement learning is a subfield of machine learning that studies how an agent interacts with an environment in order to extract as large a reward as possible. A standard approach to study such interaction is through Markov Decision Processes (MDPs) and the task of choosing an optimal policy --- a function that tells the agent which action to take. In this work, we study two types of MDPs --- finite-horizon and infinite-horizon discounted --- and propose new quantum algorithms for computing ...

---

### 20. A Hyperfinite Framework for Score-Based Generative Modeling

**Authors:** Sunder Ram Krishnan

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02799v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02799v1)

**Summary:** Score-based diffusion models are typically formulated using continuous-time stochastic differential equations and measure-theoretic stochastic calculus. In this paper, we develop a hyperfinite formulation of score-based generative modeling within the framework of Nonstandard Analysis. Starting from an internal diffusion process on a hyperfinite grid, we derive the associated infinitesimal generator and establish its correspondence with the classical Fokker--Planck equation. We then obtain a hype...

---

### 21. Tight Information Complexity of the Coin Problem in the Broadcast Model

**Authors:** Hadi Kazemi, Varun Jog

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02776v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02776v1)

**Summary:** We study distributed testing of $\mathrm{Ber}(α)$ versus $\mathrm{Ber}(β)$ in the broadcast, or shared-blackboard, model. For protocols with constant advantage, we characterise up to universal constant factors the information complexity under either hypothesis for every pair $β<α$. The characterisation shows that the two information costs can be quite different and identifies three parameter regimes, with optimal protocols based respectively on clean samples, a noisy binary symmetric channel, an...

---

### 22. DAIF: A Data-Driven Intermediate Fusion Framework for Multimodal Supervised Learning via Approximate Message Passing

**Authors:** Sagnik Nandy, Samriddha Lahiry, Pragya Sur, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02769v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02769v1)

**Summary:** Multimodal supervised learning seeks to leverage multiple heterogeneous data sources to improve predictive performance. A central challenge is determining the fusion granularity across modalities: over-integration may amplify noise while under-integration fails to exploit cross-modal dependence. Existing approaches rely on pre-specified fusion architectures, from early to late fusion, that may not adapt to the underlying dependence structure among modalities. We propose DAIF, a data adaptive int...

---

### 23. Pseudorandom Streams within Diffusion Models Act as Learnable Inputs That Affect Generation Quality

**Authors:** Shengzhi Deng, Chenqi Ye, Yanze Guo

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02575v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02575v1)

**Summary:** Diffusion models rely on stochastic inputs, yet on finite-precision hardware, the "randomness" they consume is realized as deterministic numerical orbits generated by pseudorandom rules. Accessible orbit structure can become a learnable input and affect both training and generation because the realized loss and its gradient depend on the concrete pseudorandom values consumed at each optimization step. A small multilayer perceptron predicts the next value of an orbit from its recent history, meas...

---

### 24. Interaction Is Not Necessary for Order-Optimal 1-Bit Mean Estimation

**Authors:** Jiachen Hu, Han Zhong

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02538v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02538v1)

**Summary:** This paper is concerned with one-bit mean estimation, where each independent sample is represented by a single binary message. We consider distributions on $\mathbb{R}$ with mean in $[-λ,λ]$ and absolute $k$-th central moment at most $σ^k$, where $k>1$ is fixed. For this class, previous work attained the optimal sample complexity for general queries using a two-stage protocol. The first stage localizes the mean. The second-stage queries are chosen after localization and refine the estimate aroun...

---

### 25. Computational and Statistical Guarantees of the \textit{c}-Rectified flow

**Authors:** Leda Wang, Zhehao Xu, Qiang Liu, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02487v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02487v1)

**Summary:** Recently, rectified flow has emerged as a fundamental framework for large-scale image generation, powering state-of-the-art systems such as FLUX.1 and Stable Diffusion 3. Despite its remarkable empirical success, the computational and statistical guarantees of iterative rectified flow have remained largely unexplored. We address this problem by studying \textit{c}-rectified flow, a cost-aware class of rectified flow that projects velocity fields onto a gradient class while preserving endpoint ma...

---

### 26. Fermat Active Laplace Learning for Semi-Supervised Hyperspectral Image Classification

**Authors:** Vutichart Buranasiri, James M. Murphy

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02483v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02483v1)

**Summary:** Two active learning algorithms for hyperspectral image (HSI) classification are proposed that combine density-aware Fermat distances with Poisson-reweighted harmonic label propagation. Our methods actively query points using an uncertainty-based acquisition function, extending Poisson ReWeighted Laplace Learning (PWLL). Our first algorithm, Fermat Active Laplace Learning (FALL), builds an affinity matrix using Fermat distances between all data points. Then, PWLL is run with a diagonal perturbati...

---

### 27. Private Generative Bootstrap via Blocking

**Authors:** Jinwon Sohn, Veronika Ročková

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02480v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02480v1)

**Summary:** With AI systems gaining more access to individuals' information, it is important to protect privacy when reporting statistical answers. Equally important is to privatize the reporting of uncertainty in such answers. To this end, we adopt a Bayesian likelihood-free framework and make simulation from the posterior private. In particular, we propose a new private instantiation of the Bayesian bootstrap using a blocking strategy. Rather than assigning idiosyncratic random weights to each individual,...

---

### 28. Aggregate-then-Calibrate for Human-centered Assessment with Theoretical Guarantees

**Authors:** Zejun Xie, Xintong Li, Guang Wang, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02455v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02455v1)

**Summary:** Human-centered assessment tasks, which are essential for systematic decision-making, rely heavily on human judgment and typically lack verifiable ground truth. Existing approaches face a dilemma: methods using only human judgments suffer from heterogeneous expertise and inconsistent rating scales, while methods using only model-generated scores must learn from imperfect proxies or incomplete features. We propose Aggregate-then-Calibrate (AtC), a two-stage framework that combines these complement...

---

### 29. Can Training Logs Make Model Comparisons More Precise?

**Authors:** Wei-Jung Huang

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02705v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02705v1)

**Summary:** Comparing stochastically trained models requires estimating both a performance difference and its uncertainty from repeated runs. We study whether training logs from those same runs can make such comparisons more precise. Because training-log covariates are produced during training rather than measured before it, we use arm-specific covariate adjustment: each model is adjusted only with statistics from its own runs, and the raw mean difference remains the reported effect. In a vision study spann...

---

### 30. A Unified Kullback--Leibler Divergence Analysis of Generative Diffusion Models via Entropy Production Rate

**Authors:** Han Wu, Zhiwen Zhang

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02406v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02406v1)

**Summary:** We introduce a unified framework for the error analysis of generative models based on the entropy production rate of the forward-reverse diffusion process pair. For a pair of continuity equation flows, the rate admits a closed velocity form identity whose time integral decomposes the terminal Kullback--Leibler (KL) divergence into the sum of an initialization error, a score approximation error, and a time-discretization error. By analyzing the entropy production at the level of marginal distribu...

---

### 31. Detecting Nonproperness of Likelihood Equations

**Authors:** Xiaoxian Tang, Bican Xia, Tianqi Zhao

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01976v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01976v1)

**Summary:** Given an algebraic statistical model, a challenging problem is classifying the data according to the number of positive critical points of the likelihood function. The positive critical points are the positive solutions to an algebraic system, say likelihood equations. So, identifying the number of positive critical points is a real root classification problem for the likelihood equations. A discriminant variety of a likelihood-equation system geometrically describes the data for which the numbe...

---

### 32. Approximate Message Passing with Random Initialization for Phase Retrieval

**Authors:** Yuchen Chen, Yandi Shen, Xingyu Xu

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01654v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01654v1)

**Summary:** We analyze approximate message passing (AMP) with an independent Gaussian initialization for noiseless phase retrieval in the proportional asymptotic regime. A random initialization has overlap of order $d^{-1/2}$ with the signal, and AMP requires a growing number of iterations to attain non-vanishing overlap. Thus, its precise behavior cannot be characterized by classical fixed-time state evolution. We prove a Gaussian decomposition of the AMP trajectory and control its error over the horizons ...

---

### 33. The Label Defines the Timescale: Trait-State Limits of Temporal-Aggregate Learning

**Authors:** Xizhe Zhang

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01587v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01587v1)

**Summary:** Machine-learning benchmarks often pair a label that aggregates a long temporal horizon with input observed through one or a few short windows. Their apparent performance ceiling may therefore be an acquisition-protocol ceiling rather than a model-capacity ceiling. We study labels of the form $Θ_{g,T}=T^{-1}\int_0^T g\{Z(t)\}\,\mathrm{d}t$ when the latent Gaussian process contains both a stable individual trait and a correlated within-individual state. An exact protocol-conditioned Bayes-risk ide...

---

### 34. Statistical comparisons of time-series feature sets on classification tasks

**Authors:** Trent Henderson, Ben D. Fulcher

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01586v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01586v1)

**Summary:** In recent years, numerous open-source software libraries have been developed for computing sets of features from univariate time series. The type and number of features vary across these feature sets, which have been constructed with varying disciplinary perspectives on quantifying structure in time-series data. To date, the relative strengths and weaknesses of these feature sets on time-series classification problems remains largely unexplored. Here we aimed to understand the relative performan...

---

### 35. Finite-Probe Total-Variation Certificates for Finite-Basis Drifting Models

**Authors:** Sam Andersson, Ricky Molén

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01547v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01547v1)

**Summary:** Drifting objectives compare a target and model distribution through a vector field observed noisily at finitely many locations. We ask what distributional conclusion such a frozen measurement system warrants. For integrable antisymmetric interactions and absolutely continuous laws in a declared finite density basis, the unnormalized sampled numerator satisfies $\operatorname{vec}(V_X)=Mc$, where $c$ is an antisymmetric mismatch and $M$ is probe-dependent. This identity yields an a posteriori tot...

---

### 36. Dominant Arm Identification with Mixing and Recycling Observed Samples

**Authors:** Jonghyun Sim, Wonyoung Kim

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01545v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01545v1)

**Summary:** We study the problem of identifying the dominant arm in multi-armed bandits, where the objective is to find the action with the highest probability of exceeding the realized rewards of all other actions. Conventional mean-based and pairwise comparison-based algorithms often fail to identify the arm with the highest realized reward. To address this challenge, we introduce a novel dominant arm criterion and an efficient estimator with theoretical guarantees. Our approach relies on two key technica...

---

### 37. Stochastic Sequential Search in Very-High-Dimensional Feature Selection

**Authors:** Petr Somol, Jiří Grim

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01502v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01502v1)

**Summary:** Sequential subset search -- forward selection with floating backtracking and its descendants -- remains the quality reference in feature selection, but every member of the family sweeps the full pool of remaining candidate features at each step, which excludes it from very-high-dimensional problems; there, only individual-feature ranking remains practical, and it models feature interplay weakly or not at all. We introduce a budgeted sampled step operator pair that replaces the full sweeps by a f...

---

### 38. Coordinate Optimality Reformulation for Mixed-Integer Convex Programs with Indicators

**Authors:** Tong Xu, Salar Fattahi, Andrés Gómez, et al.

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01385v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01385v1)

**Summary:** We consider mixed-integer convex optimization problems in which binary indicators control continuous variables. We introduce the \emph{Coordinate Optimality Reformulation} (CORe) framework, which augments standard indicator formulations by incorporating coordinate-wise optimality information. The resulting reformulations preserve global optimality while substantially improving branch-and-bound performance, particularly in sparse and structured settings where the coordinate-wise optimality condit...

---

### 39. A Statistical Framework for Data-Driven Discovery of Differential Performance in Clinical Risk Prediction Models

**Authors:** Aidan Neher, Julian Wolfson

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01333v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01333v1)

**Summary:** Predictive models employing artificial intelligence (AI) and machine learning (ML) are increasingly being used for decision support in healthcare settings. These models may exhibit differential performance across population subgroups defined by race, age, sex, and other factors and cause disparate clinical impacts, leading to intensive recent study of what has been termed "model fairness". While many methods have been proposed to assess risk prediction model fairness, these techniques generally ...

---

### 40. How fine a change can moments see? A scale law for detecting distribution shift, with a kernel calibration rule

**Authors:** Adel Kaleche

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01268v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01268v1)

**Summary:** Detecting that a stream of high-dimensional embeddings has changed is usually framed as a choice of statistic. We give a scale law that constrains any moment-based choice and test it against topological alternatives. The law: certifying a feature of spatial scale eps carrying mass fraction f requires polynomial tests of degree N* >= log(1/f)/(2 eps), proved via the Chebyshev extremal problem; a Gauss-quadrature construction gives N* >= 4b-1 for a b-scale topology, so cost is set by feature finen...

---

### 41. Wasserstein gradient flows of Maximum Mean Discrepancy with energy kernels

**Authors:** Matthew Rosenzweig, Dejan Slepčev, Lihan Wang

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01182v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01182v1)

**Summary:** We study the Wasserstein gradient flow of the squared Maximum Mean Discrepancy (MMD) generated by the nonsmooth energy kernels $K(z)=-|z|^q$, $0<q<2$. In dimensions $d\ge2$, the corresponding energies are not displacement semiconvex, so standard Wasserstein-gradient-flow theory does not apply. When $d+q-2>0$, we prove global well-posedness on $\mathbb{R}^d$ for probability densities in subcritical $L^p$ spaces, with targets in the same integrability class and with finite moments. We also include...

---

### 42. Characterizing Bias in Post-Bandit Inference under Index Algorithms

**Authors:** Lisu Wang, Yilun Chen, Jiaqi Lu

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01069v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01069v1)

**Summary:** Bandit algorithms generate data for downstream inference, but adaptive sampling biases post-bandit sample means. We analyze this bias for stable index algorithms, including UCB1 and its generalizations, and derive sharp leading-order expressions for the sample-mean bias and expected $Z$-statistic. Our characterization reveals the algorithmic origin of bias through a key index-function-dependent quantity, which we term effective exploration rate. For example, under UCB1, the effective exploration...

---

### 43. Model-Agnostic FDR Control via Group Gaussian Mirror and Permutation SHAP

**Authors:** Jiaan Han, Junxiao Chen, Yanzhe Fu

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.00989v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00989v1)

**Summary:** Most FDR-controlled feature selection methods are designed for coordinate-wise hypotheses, where each feature has a single weight or importance score. This abstraction fails in sequential and grouped models, where one original feature is represented by a block of sub-features, such as lags, recurrent states, or attention-based interactions. We propose a grouped-feature FDR control framework for such settings. For grouped linear models, we construct null-symmetric block-level mirror statistics wi...

---

### 44. Physics-informed neural networks for two-dimensional wall-reactive solute dispersion in canonical shear flows

**Authors:** Nanda Poddar, Subham Dhar

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00856v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00856v1)

**Summary:** The dispersion of reactive solutes in shear flows is governed by the interplay between advective stretching, transverse diffusion, and boundary exchange kinetics. While classical analytical methods and grid-based numerical solvers have extensively characterised these transport mechanisms, accurately resolving the spatiotemporal evolution of solute plumes in asymmetric reactive environments remains computationally demanding. In this study, we introduce a physics-informed neural network (PINN) fra...

---

### 45. Evolutionary Curriculum Learning Improves Biological Sequence Modeling

**Authors:** Richard Zhu, Kento Nishi

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00697v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00697v1)

**Summary:** Variational autoencoders (VAEs) trained on multiple sequence alignments (MSAs) have emerged as powerful generative models for biological sequences, with applications ranging from disease variant prediction to functional RNA design. However, standard biological VAE training treats all sequences as exchangeable, ignoring the rich evolutionary structure that organizes homologous sequences from evolutionarily close to highly divergent. We propose Evolutionary Curriculum Learning (ECL), a training st...

---

### 46. Round-Trip Consistency: Bidirectional Diffusion Models Can Predict Their Own Rollout Errors

**Authors:** Alexander Scheinker

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00675v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00675v1)

**Summary:** Autoregressive models accumulate error over long rollouts, yet at deployment there is no ground truth to measure it against. We train a single conditional latent diffusion model that steps a dynamical system forward or backward in time via a direction flag, and show that this bidirectionality supplies a measurement-free test-time error signal: rolling forward $i$ steps and then backward $i$ steps must return the model to its start, so the round-trip discrepancy $\mathcal{C}_i$ is a self-supervis...

---

### 47. Causal Inference with Unstructured Treatments

**Authors:** Kevin Christian Wibisono, Yixin Wang

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00657v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00657v1)

**Summary:** Causal inference usually concerns a scalar treatment, yet in many problems the treatment is unstructured: a text, an image, or a sequence of clinical decisions. Consider an instructor writing a course description to attract more students: the treatment is the course description, and the outcome is enrollment. The standard target, the average treatment effect of fixing the treatment to one exact value versus another, runs into two problems. It cannot be estimated, because almost no exact descript...

---

### 48. Learning the Pareto Frontier of Predictive Models under Distribution Shift

**Authors:** Yiming Dong, Jiwei Zhao, Yang Young Lu

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00632v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00632v1)

**Summary:** Modern machine learning pipelines increasingly rely on reusing pretrained and foundation models across downstream tasks. These pretrained models can differ not only in performance but also in how they can be used: some only provide black-box predictions, while others may permit white-box access to internal representations that can be probed or fine-tuned. When deployed to the target domain in the presence of distribution shift, no single strategy, including zero-shot application, fine-tuning, or...

---

### 49. Recursive Gaussian Processes and the Bayesian Brain

**Authors:** Moumita Das, Dipanjan Ray, Sourabh Bhattacharya

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00503v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00503v1)

**Summary:** Predictive coding offers a powerful framework for cortical computation, yet scalable implementations that respect both Bayesian exactness and neurobiological constraints remain scarce. We bridge this gap by formally connecting predictive coding to Recursive Gaussian Processes (RGPs). RGPs employ a single Gaussian process \( g(t, \cdot) \) indexed by layer index and input value, preventing the representational collapse of standard deep Gaussian processes while allowing learnable cross-layer depen...

---

### 50. Backward Bayesian Outcome Weighted Learning

**Authors:** Emmanuel M. Rockwell, Michael R. Kosorok, Nikki L. B. Freeman

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00317v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00317v1)

**Summary:** A central objective of precision medicine is learning optimal dynamic treatment regimes (DTRs) from data. Classification-based methods, like outcome weighted learning (OWL) for single-stage and backward OWL (BOWL) for multi-stage problems, leverage machine learning to directly learn optimal DTRs. However, these methods lack a natural way to quantify uncertainty in treatment decisions at the individual level. In this paper, we extend Bayesian OWL, a Bayesian reformulation of OWL, to the multi-sta...

---

