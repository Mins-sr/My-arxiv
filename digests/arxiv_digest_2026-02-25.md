# arXiv Daily Digest - 2026-02-25

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Test-Time Training with KV Binding Is Secretly Linear Attention

**Authors:** Junchen Liu, Sven Elflein, Or Litany, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21204v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21204v1)

**Summary:** Test-time training (TTT) with KV binding as sequence modeling layer is commonly interpreted as a form of online meta-learning that memorizes a key-value mapping at test time. However, our analysis reveals multiple phenomena that contradict this memorization-based interpretation. Motivated by these findings, we revisit the formulation of TTT and show that a broad class of TTT architectures can be expressed as a form of learned linear attention operator. Beyond explaining previously puzzling model...

---

### 2. Aletheia tackles FirstProof autonomously

**Authors:** Tony Feng, Junehyuk Jung, Sang-hyun Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21201v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21201v1)

**Summary:** We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as...

---

### 3. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

**Authors:** Yining Hong, Huang Huang, Manling Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21198v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21198v1)

**Summary:** Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflec...

---

### 4. Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training

**Authors:** Anas Barakat, Souradip Chakraborty, Khushbu Pahwa, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21189v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21189v1)

**Summary:** Pass@k is a widely used performance metric for verifiable large language model tasks, including mathematical reasoning, code generation, and short-answer reasoning. It defines success if any of $k$ independently sampled solutions passes a verifier. This multi-sample inference metric has motivated inference-aware fine-tuning methods that directly optimize pass@$k$. However, prior work reports a recurring trade-off: pass@k improves while pass@1 degrades under such methods. This trade-off is practi...

---

### 5. XMorph: Explainable Brain Tumor Analysis Via LLM-Assisted Hybrid Deep Intelligence

**Authors:** Sepehr Salem Ghahfarokhi, M. Moein Esfahani, Raj Sunderraman, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21178v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21178v1)

**Summary:** Deep learning has significantly advanced automated brain tumor diagnosis, yet clinical adoption remains limited by interpretability and computational constraints. Conventional models often act as opaque ''black boxes'' and fail to quantify the complex, irregular tumor boundaries that characterize malignant growth. To address these challenges, we present XMorph, an explainable and computationally efficient framework for fine-grained classification of three prominent brain tumor types: glioma, men...

---

### 6. Efficient Hierarchical Any-Angle Path Planning on Multi-Resolution 3D Grids

**Authors:** Victor Reijgwart, Cesar Cadena, Roland Siegwart, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21174v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21174v1)

**Summary:** Hierarchical, multi-resolution volumetric mapping approaches are widely used to represent large and complex environments as they can efficiently capture their occupancy and connectivity information. Yet widely used path planning methods such as sampling and trajectory optimization do not exploit this explicit connectivity information, and search-based methods such as A* suffer from scalability issues in large-scale high-resolution maps. In many applications, Euclidean shortest paths form the und...

---

### 7. NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning

**Authors:** Ishaan Rawal, Shubh Gupta, Yihan Hu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21172v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21172v1)

**Summary:** Vision-Language-Action (VLA) models are advancing autonomous driving by replacing modular pipelines with unified end-to-end architectures. However, current VLAs face two expensive requirements: (1) massive dataset collection, and (2) dense reasoning annotations. In this work, we address both challenges with \modelname (\textbf{No} \textbf{R}easoning for \textbf{D}riving). Compared to existing VLAs, \modelname achieves competitive performance while being fine-tuned on $<$60\% of the data and no r...

---

### 8. PVminer: A Domain-Specific Tool to Detect the Patient Voice in Patient Generated Data

**Authors:** Samah Fodeh, Linhai Ma, Yan Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21165v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21165v1)

**Summary:** Patient-generated text such as secure messages, surveys, and interviews contains rich expressions of the patient voice (PV), reflecting communicative behaviors and social determinants of health (SDoH). Traditional qualitative coding frameworks are labor intensive and do not scale to large volumes of patient-authored messages across health systems. Existing machine learning (ML) and natural language processing (NLP) approaches provide partial solutions but often treat patient-centered communicati...

---

### 9. CG-DMER: Hybrid Contrastive-Generative Framework for Disentangled Multimodal ECG Representation Learning

**Authors:** Ziwei Niu, Hao Sun, Shujun Bian, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21154v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21154v1)

**Summary:** Accurate interpretation of electrocardiogram (ECG) signals is crucial for diagnosing cardiovascular diseases. Recent multimodal approaches that integrate ECGs with accompanying clinical reports show strong potential, but they still face two main concerns from a modality perspective: (1) intra-modality: existing models process ECGs in a lead-agnostic manner, overlooking spatial-temporal dependencies across leads, which restricts their effectiveness in modeling fine-grained diagnostic patterns; (2...

---

### 10. A Benchmark for Deep Information Synthesis

**Authors:** Debjit Paul, Daniel Murphy, Milan Gritta, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21143v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21143v1)

**Summary:** Large language model (LLM)-based agents are increasingly used to solve complex tasks involving tool use, such as web browsing, code execution, and data analysis. However, current evaluation benchmarks do not adequately assess their ability to solve real-world tasks that require synthesizing information from multiple sources and inferring insights beyond simple fact retrieval. To address this, we introduce DEEPSYNTH, a novel benchmark designed to evaluate agents on realistic, time-consuming probl...

---

### 11. SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery

**Authors:** David Anugraha, Vishakh Padmakumar, Diyi Yang

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21136v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21136v1)

**Summary:** Qualitative insights from user experiences are critical for informing product and policy decisions, but collecting such data at scale is constrained by the time and availability of experts to conduct semi-structured interviews. Recent work has explored using large language models (LLMs) to automate interviewing, yet existing systems lack a principled mechanism for balancing systematic coverage of predefined topics with adaptive exploration, or the ability to pursue follow-ups, deep dives, and em...

---

### 12. "Are You Sure?": An Empirical Study of Human Perception Vulnerability in LLM-Driven Agentic Systems

**Authors:** Xinfeng Li, Shenyu Dai, Kelong Zheng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21127v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21127v1)

**Summary:** Large language model (LLM) agents are rapidly becoming trusted copilots in high-stakes domains like software development and healthcare. However, this deepening trust introduces a novel attack surface: Agent-Mediated Deception (AMD), where compromised agents are weaponized against their human users. While extensive research focuses on agent-centric threats, human susceptibility to deception by a compromised agent remains unexplored. We present the first large-scale empirical study with 303 parti...

---

### 13. Cooperative-Competitive Team Play of Real-World Craft Robots

**Authors:** Rui Zhao, Xihui Li, Yizheng Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21119v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21119v1)

**Summary:** Multi-agent deep Reinforcement Learning (RL) has made significant progress in developing intelligent game-playing agents in recent years. However, the efficient training of collective robots using multi-agent RL and the transfer of learned policies to real-world applications remain open research questions. In this work, we first develop a comprehensive robotic system, including simulation, distributed learning framework, and physical robot components. We then propose and evaluate reinforcement l...

---

### 14. Attention-Based SINR Estimation in User-Centric Non-Terrestrial Networks

**Authors:** Bruno De Filippo, Alessandro Guidotti, Alessandro Vanelli-Coralli

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21116v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21116v1)

**Summary:** The signal-to-interference-plus-noise ratio (SINR) is central to performance optimization in user-centric beamforming for satellite-based non-terrestrial networks (NTNs). Its assessment either requires the transmission of dedicated pilots or relies on computing the beamforming matrix through minimum mean squared error (MMSE)-based formulations beforehand, a process that introduces significant computational overhead. In this paper, we propose a low-complexity SINR estimation framework that levera...

---

### 15. Probing Graph Neural Network Activation Patterns Through Graph Topology

**Authors:** Floriano Tori, Lorenzo Bini, Marco Sorbi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21092v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21092v1)

**Summary:** Curvature notions on graphs provide a theoretical description of graph topology, highlighting bottlenecks and denser connected regions. Artifacts of the message passing paradigm in Graph Neural Networks, such as oversmoothing and oversquashing, have been attributed to these regions. However, it remains unclear how the topology of a graph interacts with the learned preferences of GNNs. Through Massive Activations, which correspond to extreme edge activation values in Graph Transformers, we probe ...

---

### 16. Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning

**Authors:** Zhangjie Xia, Yu Yang, Pan Xu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21072v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21072v1)

**Summary:** Off-dynamics offline reinforcement learning (RL) aims to learn a policy for a target domain using limited target data and abundant source data collected under different transition dynamics. Existing methods typically address dynamics mismatch either globally over the state space or via pointwise data filtering; these approaches can miss localized cross-domain similarities or incur high computational cost. We propose Localized Dynamics-Aware Domain Adaptation (LoDADA), which exploits localized dy...

---

### 17. The Initial Exploration Problem in Knowledge Graph Exploration

**Authors:** Claire McNamara, Lucy Hederman, Declan O'Sullivan

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21066v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21066v1)

**Summary:** Knowledge Graphs (KGs) enable the integration and representation of complex information across domains, but their semantic richness and structural complexity create substantial barriers for lay users without expertise in semantic web technologies. When encountering an unfamiliar KG, such users face a distinct orientation challenge: they do not know what questions are possible, how the knowledge is structured, or how to begin exploration. This paper identifies and theorises this phenomenon as the...

---

### 18. Motivation is Something You Need

**Authors:** Mehdi Acheli, Walid Gaaloul

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21064v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21064v1)

**Summary:** This work introduces a novel training paradigm that draws from affective neuroscience. Inspired by the interplay of emotions and cognition in the human brain and more specifically the SEEKING motivational state, we design a dual-model framework where a smaller base model is trained continuously, while a larger motivated model is activated intermittently during predefined "motivation conditions". The framework mimics the emotional state of high curiosity and anticipation of reward in which broade...

---

### 19. Tool Building as a Path to "Superintelligence"

**Authors:** David Koplow, Tomer Galanti, Tomaso Poggio

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21061v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21061v1)

**Summary:** The Diligent Learner framework suggests LLMs can achieve superintelligence via test-time search, provided a sufficient step-success probability $γ$. In this work, we design a benchmark to measure $γ$ on logical out-of-distribution inference. We construct a class of tasks involving GF(2) circuit reconstruction that grow more difficult with each reasoning step, and that are, from an information-theoretic standpoint, impossible to reliably solve unless the LLM carefully integrates all of the inform...

---

### 20. VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation

**Authors:** Seongheon Park, Changdae Oh, Hyeong Kyu Choi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21054v1)

**Summary:** Large Vision-Language Models (LVLMs) frequently hallucinate, limiting their safe deployment in real-world applications. Existing LLM self-evaluation methods rely on a model's ability to estimate the correctness of its own outputs, which can improve deployment reliability; however, they depend heavily on language priors and are therefore ill-suited for evaluating vision-conditioned predictions. We propose VAUQ, a vision-aware uncertainty quantification framework for LVLM self-evaluation that expl...

---

### 21. Position-Aware Sequential Attention for Accurate Next Item Recommendations

**Authors:** Timur Nabiev, Evgeny Frolov

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21052v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21052v1)

**Summary:** Sequential self-attention models usually rely on additive positional embeddings, which inject positional information into item representations at the input. In the absence of positional signals, the attention block is permutation-equivariant over sequence positions and thus has no intrinsic notion of temporal order beyond causal masking. We argue that additive positional embeddings make the attention mechanism only superficially sensitive to sequence order: positional information is entangled wi...

---

### 22. LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification

**Authors:** Yanrui Wu, Lingling Zhang, Xinyu Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21044v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21044v1)

**Summary:** Evaluations of large language models (LLMs) primarily emphasize convergent logical reasoning, where success is defined by producing a single correct proof. However, many real-world reasoning problems admit multiple valid derivations, requiring models to explore diverse logical paths rather than committing to one route. To address this limitation, we introduce LogicGraph, the first benchmark aimed to systematically evaluate multi-path logical reasoning, constructed via a neuro-symbolic framework ...

---

### 23. MIP Candy: A Modular PyTorch Framework for Medical Image Processing

**Authors:** Tianhao Fu, Yucheng Chen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21033v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21033v1)

**Summary:** Medical image processing demands specialized software that handles high-dimensional volumetric data, heterogeneous file formats, and domain-specific training procedures. Existing frameworks either provide low-level components that require substantial integration effort or impose rigid, monolithic pipelines that resist modification. We present MIP Candy (MIPCandy), a freely available, PyTorch-based framework designed specifically for medical image processing. MIPCandy provides a complete, modular...

---

### 24. Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures

**Authors:** Yubin Ge, Yongsong Huang, Xiaofeng Liu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20994v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20994v1)

**Summary:** Report-supervised (RSuper) learning seeks to alleviate the need for dense tumor voxel labels with constraints derived from radiology reports (e.g., volumes, counts, sizes, locations). In MRI studies of brain tumors, however, we often involve multi-parametric scans and substructures. Here, fine-grained modality/parameter-wise reports are usually provided along with global findings and are correlated with different substructures. Moreover, the reports often describe only the largest lesion and pro...

---

### 25. Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models

**Authors:** Christian Simon, MAsato Ishii, Wei-Yao Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20981v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20981v1)

**Summary:** Scaling multimodal alignment between video and audio is challenging, particularly due to limited data and the mismatch between text descriptions and frame-level video information. In this work, we tackle the scaling challenge in multimodal-to-audio generation, examining whether models trained on short instances can generalize to longer ones during testing. To tackle this challenge, we present multimodal hierarchical networks so-called MMHNet, an enhanced extension of state-of-the-art video-to-au...

---

### 26. CrystaL: Spontaneous Emergence of Visual Latents in MLLMs

**Authors:** Yang Zhang, Danyang Li, Yuxuan Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20980v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20980v1)

**Summary:** Multimodal Large Language Models (MLLMs) have achieved remarkable performance by integrating powerful language backbones with large-scale visual encoders. Among these, latent Chain-of-Thought (CoT) methods enable implicit reasoning in continuous hidden states, facilitating seamless vision-language integration and faster inference. However, existing heuristically predefined supervision signals in latent CoT provide limited guidance for preserving critical visual information in intermediate latent...

---

### 27. Toward an Agentic Infused Software Ecosystem

**Authors:** Mark Marron

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20979v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20979v1)

**Summary:** Fully leveraging the capabilities of AI agents in software development requires a rethinking of the software ecosystem itself. To this end, this paper outlines the creation of an Agentic Infused Software Ecosystem (AISE), that rests on three pillars. The first, of course, is the AI agents themselves, which in the past 5 years have moved from simple code completion and toward sophisticated independent development tasks, a trend which will only continue. The second pillar is the programming langua...

---

### 28. Does Order Matter : Connecting The Law of Robustness to Robust Generalization

**Authors:** Himadri Mandal, Vishnu Varadarajan, Jaee Ponde, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20971v1)

**Summary:** Bubeck and Sellke (2021) pose as an open problem the connection between the law of robustness and robust generalization. The law of robustness states that overparameterization is necessary for models to interpolate robustly; in particular, robust interpolation requires the learned function to be Lipschitz. Robust generalization asks whether small robust training loss implies small robust test loss. We resolve this problem by explicitly connecting the two for arbitrary data distributions. Specifi...

---

### 29. Training-Free Intelligibility-Guided Observation Addition for Noisy ASR

**Authors:** Haoyang Li, Changsong Liu, Wei Rao, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20967v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20967v1)

**Summary:** Automatic speech recognition (ASR) degrades severely in noisy environments. Although speech enhancement (SE) front-ends effectively suppress background noise, they often introduce artifacts that harm recognition. Observation addition (OA) addressed this issue by fusing noisy and SE enhanced speech, improving recognition without modifying the parameters of the SE or ASR models. This paper proposes an intelligibility-guided OA method, where fusion weights are derived from intelligibility estimates...

---

### 30. EKF-Based Depth Camera and Deep Learning Fusion for UAV-Person Distance Estimation and Following in SAR Operations

**Authors:** Luka Šiktar, Branimir Ćaran, Bojan Šekoranja, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20958v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20958v1)

**Summary:** Search and rescue (SAR) operations require rapid responses to save lives or property. Unmanned Aerial Vehicles (UAVs) equipped with vision-based systems support these missions through prior terrain investigation or real-time assistance during the mission itself. Vision-based UAV frameworks aid human search tasks by detecting and recognizing specific individuals, then tracking and following them while maintaining a safe distance. A key safety requirement for UAV following is the accurate estimati...

---

### 31. See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis

**Authors:** Jaehyun Park, Minyoung Ahn, Minkyu Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20951v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20951v1)

**Summary:** Despite recent advances in diffusion models, AI generated images still often contain visual artifacts that compromise realism. Although more thorough pre-training and bigger models might reduce artifacts, there is no assurance that they can be completely eliminated, which makes artifact mitigation a highly crucial area of study. Previous artifact-aware methodologies depend on human-labeled artifact datasets, which are costly and difficult to scale, underscoring the need for an automated approach...

---

### 32. Some Simple Economics of AGI

**Authors:** Christian Catalini, Xiang Hui, Jane Wu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20946v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20946v1)

**Summary:** For millennia, human cognition was the primary engine of progress on Earth. As AI decouples cognition from biology, the marginal cost of measurable execution falls to zero, absorbing any labor capturable by metrics--including creative, analytical, and innovative work. The binding constraint on growth is no longer intelligence but human verification bandwidth: the capacity to validate, audit, and underwrite responsibility when execution is abundant. We model the AGI transition as the collision of...

---

### 33. The Art of Efficient Reasoning: Data, Reward, and Optimization

**Authors:** Taiqiang Wu, Zenan Zu, Bo Zhou, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20945v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20945v1)

**Summary:** Large Language Models (LLMs) consistently benefit from scaled Chain-of-Thought (CoT) reasoning, but also suffer from heavy computational overhead. To address this issue, efficient reasoning aims to incentivize short yet accurate thinking trajectories, typically through reward shaping with Reinforcement Learning (RL). In this paper, we systematically investigate the mechanics of efficient reasoning for LLMs. For comprehensive evaluation, we advocate for more fine-grained metrics, including length...

---

### 34. Architecting AgentOS: From Token-Level Context to Emergent System-Level Intelligence

**Authors:** ChengYou Li, XiaoDong Liu, XiangBao Meng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20934v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20934v1)

**Summary:** The paradigm of Large Language Models is undergoing a fundamental transition from static inference engines to dynamic autonomous cognitive systems.While current research primarily focuses on scaling context windows or optimizing prompt engineering the theoretical bridge between micro scale token processing and macro scale systemic intelligence remains fragmented.This paper proposes AgentOS,a holistic conceptual framework that redefines the LLM as a "Reasoning Kernel" governed by structured opera...

---

### 35. HELP: HyperNode Expansion and Logical Path-Guided Evidence Localization for Accurate and Efficient GraphRAG

**Authors:** Yuqi Huang, Ning Liao, Kai Yang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20926v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20926v1)

**Summary:** Large Language Models (LLMs) often struggle with inherent knowledge boundaries and hallucinations, limiting their reliability in knowledge-intensive tasks. While Retrieval-Augmented Generation (RAG) mitigates these issues, it frequently overlooks structural interdependencies essential for multi-hop reasoning. Graph-based RAG approaches attempt to bridge this gap, yet they typically face trade-offs between accuracy and efficiency due to challenges such as costly graph traversals and semantic nois...

---

### 36. Airavat: An Agentic Framework for Internet Measurement

**Authors:** Alagappan Ramanathan, Eunju Kang, Dongsu Han, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20924v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20924v1)

**Summary:** Internet measurement faces twin challenges: complex analyses require expert-level orchestration of tools, yet even syntactically correct implementations can have methodological flaws and can be difficult to verify. Democratizing measurement capabilities thus demands automating both workflow generation and verification against methodological standards established through decades of research.   We present Airavat, the first agentic framework for Internet measurement workflow generation with system...

---

### 37. Predicting Sentence Acceptability Judgments in Multimodal Contexts

**Authors:** Hyewon Jang, Nikolai Ilinykh, Sharid Loáiciga, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20918v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20918v1)

**Summary:** Previous work has examined the capacity of deep neural networks (DNNs), particularly transformers, to predict human sentence acceptability judgments, both independently of context, and in document contexts. We consider the effect of prior exposure to visual images (i.e., visual context) on these judgments for humans and large language models (LLMs). Our results suggest that, in contrast to textual context, visual images appear to have little if any impact on human acceptability ratings. However,...

---

### 38. Diagnosing Causal Reasoning in Vision-Language Models via Structured Relevance Graphs

**Authors:** Dhita Putri Pratama, Soyeon Caren Han, Yihao Ding

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20878v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20878v1)

**Summary:** Large Vision-Language Models (LVLMs) achieve strong performance on visual question answering benchmarks, yet often rely on spurious correlations rather than genuine causal reasoning. Existing evaluations primarily assess the correctness of the answers, making it unclear whether failures arise from limited reasoning capability or from misidentifying causally relevant information. We introduce Vision-Language Causal Graphs (VLCGs), a structured, query-conditioned representation that explicitly enc...

---

### 39. E-MMKGR: A Unified Multimodal Knowledge Graph Framework for E-commerce Applications

**Authors:** Jiwoo Kang, Yeon-Chang Lee

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20877v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20877v1)

**Summary:** Multimodal recommender systems (MMRSs) enhance collaborative filtering by leveraging item-side modalities, but their reliance on a fixed set of modalities and task-specific objectives limits both modality extensibility and task generalization. We propose E-MMKGR, a framework that constructs an e-commerce-specific Multimodal Knowledge Graph E-MMKG and learns unified item representations through GNN-based propagation and KG-oriented optimization. These representations provide a shared semantic fou...

---

### 40. SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

**Authors:** Yanna Jiang, Delong Li, Haiyu Deng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20867v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20867v1)

**Summary:** Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability conditions, execution policies, termination criteria, and reusable interfaces. Unlike one-off plans or atomic tool calls, skills operate (and often do well) across tasks.   This paper maps the skill layer across the full lifecycle (discovery, practic...

---

### 41. Pressure Reveals Character: Behavioural Alignment Evaluation at Depth

**Authors:** Nora Petrova, John Burden

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20813v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20813v1)

**Summary:** Evaluating alignment in language models requires testing how they behave under realistic pressure, not just what they claim they would do. While alignment failures increasingly cause real-world harm, comprehensive evaluation frameworks with realistic multi-turn scenarios remain lacking. We introduce an alignment benchmark spanning 904 scenarios across six categories -- Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, and Scheming -- validated as realistic by human raters. Our scenar...

---

### 42. Qwen-BIM: developing large language model for BIM-based design with domain-specific benchmark and dataset

**Authors:** Jia-Rui Lin, Yun-Hong Cai, Xiang-Rui Ni, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20812v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20812v1)

**Summary:** As the construction industry advances toward digital transformation, BIM (Building Information Modeling)-based design has become a key driver supporting intelligent construction. Despite Large Language Models (LLMs) have shown potential in promoting BIM-based design, the lack of specific datasets and LLM evaluation benchmarks has significantly hindered the performance of LLMs. Therefore, this paper addresses this gap by proposing: 1) an evaluation benchmark for BIM-based design together with cor...

---

### 43. POMDPPlanners: Open-Source Package for POMDP Planning

**Authors:** Yaacov Pariente, Vadim Indelman

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20810v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20810v1)

**Summary:** We present POMDPPlanners, an open-source Python package for empirical evaluation of Partially Observable Markov Decision Process (POMDP) planning algorithms. The package integrates state-of-the-art planning algorithms, a suite of benchmark environments with safety-critical variants, automated hyperparameter optimization via Optuna, persistent caching with failure recovery, and configurable parallel simulation -- reducing the overhead of extensive simulation studies. POMDPPlanners is designed to ...

---

### 44. Regret-Guided Search Control for Efficient Learning in AlphaZero

**Authors:** Yun-Jui Tsai, Wei-Yu Chen, Yan-Ru Ju, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20809v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20809v1)

**Summary:** Reinforcement learning (RL) agents achieve remarkable performance but remain far less learning-efficient than humans. While RL agents require extensive self-play games to extract useful signals, humans often need only a few games, improving rapidly by repeatedly revisiting states where mistakes occurred. This idea, known as search control, aims to restart from valuable states rather than always from the initial state. In AlphaZero, prior work Go-Exploit applies this idea by sampling past states ...

---

### 45. Pipeline for Verifying LLM-Generated Mathematical Solutions

**Authors:** Varvara Sazonova, Dmitri Shmelkin, Stanislav Kikot, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20770v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20770v1)

**Summary:** With the growing popularity of Large Reasoning Models and their results in solving mathematical problems, it becomes crucial to measure their capabilities. We introduce a pipeline for both automatic and interactive verification as a more accurate alternative to only checking the answer which is currently the most popular approach for benchmarks. The pipeline can also be used as a generator of correct solutions both in formal and informal languages. 3 AI agents, which can be chosen for the benchm...

---

### 46. OrthoDiffusion: A Generalizable Multi-Task Diffusion Foundation Model for Musculoskeletal MRI Interpretation

**Authors:** Tian Lan, Lei Xu, Zimu Yuan, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20752v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20752v1)

**Summary:** Musculoskeletal disorders represent a significant global health burden and are a leading cause of disability worldwide. While MRI is essential for accurate diagnosis, its interpretation remains exceptionally challenging. Radiologists must identify multiple potential abnormalities within complex anatomical structures across different imaging planes, a process that requires significant expertise and is prone to variability. We developed OrthoDiffusion, a unified diffusion-based foundation model de...

---

### 47. SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing

**Authors:** Yifei Xu, Guilherme Potje, Shivam Shandilya, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20751v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20751v1)

**Summary:** Designing aligned and robust rewards for open-ended generation remains a key barrier to RL post-training. Rubrics provide structured, interpretable supervision, but scaling rubric construction is difficult: expert rubrics are costly, prompted rubrics are often superficial or inconsistent, and fixed-pool discriminative rubrics can saturate and drift, enabling reward hacking. We present SibylSense, an inference-time learning approach that adapts a frozen rubric generator through a tunable memory b...

---

### 48. Voices of the Mountains: Deep Learning-Based Vocal Error Detection System for Kurdish Maqams

**Authors:** Darvan Shvan Khairaldeen, Hossein Hassani

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20744v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20744v1)

**Summary:** Maqam, a singing type, is a significant component of Kurdish music. A maqam singer receives training in a traditional face-to-face or through self-training. Automatic Singing Assessment (ASA) uses machine learning (ML) to provide the accuracy of singing styles and can help learners to improve their performance through error detection. Currently, the available ASA tools follow Western music rules. The musical composition requires all notes to stay within their expected pitch range from start to f...

---

### 49. PyVision-RL: Forging Open Agentic Vision Models via RL

**Authors:** Shitian Zhao, Shaoheng Lin, Ming Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20739v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20739v1)

**Summary:** Reinforcement learning for agentic multimodal models often suffers from interaction collapse, where models learn to reduce tool usage and multi-turn reasoning, limiting the benefits of agentic behavior. We introduce PyVision-RL, a reinforcement learning framework for open-weight multimodal models that stabilizes training and sustains interaction. Our approach combines an oversampling-filtering-ranking rollout strategy with an accumulative tool reward to prevent collapse and encourage multi-turn ...

---

### 50. RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition

**Authors:** Kun Ran, Marwah Alaofi, Danula Hettiachchi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20735v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20735v1)

**Summary:** This paper presents the award-winning RMIT-ADM+S system for the Text-to-Text   track of the NeurIPS~2025 MMU-RAG Competition. We introduce Routing-to-RAG   (R2RAG), a research-focused retrieval-augmented generation (RAG)   architecture composed of lightweight components that dynamically adapt the   retrieval strategy based on inferred query complexity and evidence   sufficiency. The system uses smaller LLMs, enabling operation on a single   consumer-grade GPU while supporting complex research ta...

---

## cs.CL

**50 papers**

### 1. Multi-Vector Index Compression in Any Modality

**Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21202v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21202v1)

**Summary:** We study efficient multi-vector retrieval for late interaction in any modality. Late interaction has emerged as a dominant paradigm for information retrieval in text, images, visual documents, and videos, but its computation and storage costs grow linearly with document length, making it costly for image-, video-, and audio-rich corpora. To address this limitation, we explore query-agnostic methods for compressing multi-vector document representations under a constant vector budget. We introduce...

---

### 2. Aletheia tackles FirstProof autonomously

**Authors:** Tony Feng, Junehyuk Jung, Sang-hyun Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21201v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21201v1)

**Summary:** We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as...

---

### 3. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

**Authors:** Yining Hong, Huang Huang, Manling Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21198v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21198v1)

**Summary:** Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflec...

---

### 4. On Data Engineering for Scaling LLM Terminal Capabilities

**Authors:** Renjie Pi, Grace Lam, Mohammad Shoeybi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21193v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21193v1)

**Summary:** Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents remain largely undisclosed. We address this gap through a systematic study of data engineering practices for terminal agents, making two key contributions: (1) Terminal-Task-Gen, a lightweight synthetic task generation pipeline that supports seed-based and skill-based task construction, and (2) a comprehensive analysis of data and training stra...

---

### 5. PVminer: A Domain-Specific Tool to Detect the Patient Voice in Patient Generated Data

**Authors:** Samah Fodeh, Linhai Ma, Yan Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21165v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21165v1)

**Summary:** Patient-generated text such as secure messages, surveys, and interviews contains rich expressions of the patient voice (PV), reflecting communicative behaviors and social determinants of health (SDoH). Traditional qualitative coding frameworks are labor intensive and do not scale to large volumes of patient-authored messages across health systems. Existing machine learning (ML) and natural language processing (NLP) approaches provide partial solutions but often treat patient-centered communicati...

---

### 6. SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

**Authors:** Dengjia Zhang, Xiaoou Liu, Lu Cheng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21158v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21158v1)

**Summary:** Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolv...

---

### 7. A Benchmark for Deep Information Synthesis

**Authors:** Debjit Paul, Daniel Murphy, Milan Gritta, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21143v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21143v1)

**Summary:** Large language model (LLM)-based agents are increasingly used to solve complex tasks involving tool use, such as web browsing, code execution, and data analysis. However, current evaluation benchmarks do not adequately assess their ability to solve real-world tasks that require synthesizing information from multiple sources and inferring insights beyond simple fact retrieval. To address this, we introduce DEEPSYNTH, a novel benchmark designed to evaluate agents on realistic, time-consuming probl...

---

### 8. Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for Efficient Reasoning

**Authors:** Sanket Badhe, Deep Shah

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21103v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21103v1)

**Summary:** Advanced reasoning typically requires Chain-of-Thought prompting, which is accurate but incurs prohibitive latency and substantial test-time inference costs. The standard alternative, fine-tuning smaller models, often sacrifices interpretability while introducing significant resource and operational overhead. To address these limitations, we introduce Prompt-Level Distillation (PLD). We extract explicit reasoning patterns from a Teacher model and organize them into a structured list of expressiv...

---

### 9. Beyond the Star Rating: A Scalable Framework for Aspect-Based Sentiment Analysis Using LLMs and Text Classification

**Authors:** Vishal Patil, Shree Vaishnavi Bacha, Revanth Yamani, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21082v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21082v1)

**Summary:** Customer-provided reviews have become an important source of information for business owners and other customers alike. However, effectively analyzing millions of unstructured reviews remains challenging. While large language models (LLMs) show promise for natural language understanding, their application to large-scale review analysis has been limited by computational costs and scalability concerns. This study proposes a hybrid approach that uses LLMs for aspect identification while employing c...

---

### 10. An Expert Schema for Evaluating Large Language Model Errors in Scholarly Question-Answering Systems

**Authors:** Anna Martin-Boyle, William Humphreys, Martha Brown, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21059v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21059v1)

**Summary:** Large Language Models (LLMs) are transforming scholarly tasks like search and summarization, but their reliability remains uncertain. Current evaluation metrics for testing LLM reliability are primarily automated approaches that prioritize efficiency and scalability, but lack contextual nuance and fail to reflect how scientific domain experts assess LLM outputs in practice. We developed and validated a schema for evaluating LLM errors in scholarly question-answering systems that reflects the ass...

---

### 11. VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation

**Authors:** Seongheon Park, Changdae Oh, Hyeong Kyu Choi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21054v1)

**Summary:** Large Vision-Language Models (LVLMs) frequently hallucinate, limiting their safe deployment in real-world applications. Existing LLM self-evaluation methods rely on a model's ability to estimate the correctness of its own outputs, which can improve deployment reliability; however, they depend heavily on language priors and are therefore ill-suited for evaluating vision-conditioned predictions. We propose VAUQ, a vision-aware uncertainty quantification framework for LVLM self-evaluation that expl...

---

### 12. PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A

**Authors:** Anna Martin-Boyle, Cara A. C. Leckey, Martha C. Brown, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21045v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21045v1)

**Summary:** Large language models (LLMs) are increasingly used in scholarly question-answering (QA) systems to help researchers synthesize vast amounts of literature. However, these systems often produce subtle errors (e.g., unsupported claims, errors of omission), and current provenance mechanisms like source citations are not granular enough for the rigorous verification that scholarly domain requires. To address this, we introduce PaperTrail, a novel interface that decomposes both LLM answers and source ...

---

### 13. HiSAC: Hierarchical Sparse Activation Compression for Ultra-long Sequence Modeling in Recommenders

**Authors:** Kun Yuan, Junyu Bi, Daixuan Cheng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21009v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21009v1)

**Summary:** Modern recommender systems leverage ultra-long user behavior sequences to capture dynamic preferences, but end-to-end modeling is infeasible in production due to latency and memory constraints. While summarizing history via interest centers offers a practical alternative, existing methods struggle to (1) identify user-specific centers at appropriate granularity and (2) accurately assign behaviors, leading to quantization errors and loss of long-tail preferences. To alleviate these issues, we pro...

---

### 14. Generative Pseudo-Labeling for Pre-Ranking with LLMs

**Authors:** Junyu Bi, Xinting Niu, Daixuan Cheng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20995v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20995v1)

**Summary:** Pre-ranking is a critical stage in industrial recommendation systems, tasked with efficiently scoring thousands of recalled items for downstream ranking. A key challenge is the train-serving discrepancy: pre-ranking models are trained only on exposed interactions, yet must score all recalled candidates -- including unexposed items -- during online serving. This mismatch not only induces severe sample selection bias but also degrades generalization, especially for long-tail content. Existing debi...

---

### 15. Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures

**Authors:** Yubin Ge, Yongsong Huang, Xiaofeng Liu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20994v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20994v1)

**Summary:** Report-supervised (RSuper) learning seeks to alleviate the need for dense tumor voxel labels with constraints derived from radiology reports (e.g., volumes, counts, sizes, locations). In MRI studies of brain tumors, however, we often involve multi-parametric scans and substructures. Here, fine-grained modality/parameter-wise reports are usually provided along with global findings and are correlated with different substructures. Moreover, the reports often describe only the largest lesion and pro...

---

### 16. Evaluating Proactive Risk Awareness of Large Language Models

**Authors:** Xuan Luo, Yubin Chen, Zhiyu Hou, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20976v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20976v1)

**Summary:** As large language models (LLMs) are increasingly embedded in everyday decision-making, their safety responsibilities extend beyond reacting to explicit harmful intent toward anticipating unintended but consequential risks. In this work, we introduce a proactive risk awareness evaluation framework that measures whether LLMs can anticipate potential harms and provide warnings before damage occurs. We construct the Butterfly dataset to instantiate this framework in the environmental and ecological ...

---

### 17. Linear Reasoning vs. Proof by Cases: Obstacles for Large Language Models in FOL Problem Solving

**Authors:** Yuliang Ji, Fuchen Shen, Jian Wu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20973v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20973v1)

**Summary:** To comprehensively evaluate the mathematical reasoning capabilities of Large Language Models (LLMs), researchers have introduced abundant mathematical reasoning datasets. However, most existing datasets primarily focus on linear reasoning, neglecting other parts such as proof by contradiction and proof by cases, which are crucial for investigating LLMs' reasoning abilities. To address this limitation, we first introduce a novel first-order logic (FOL) dataset named PC-FOL, annotated by professio...

---

### 18. Blackbird Language Matrices: A Framework to Investigate the Linguistic Competence of Language Models

**Authors:** Paola Merlo, Chunyang Jiang, Giuseppe Samo, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20966v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20966v1)

**Summary:** This article describes a novel language task, the Blackbird Language Matrices (BLM) task, inspired by intelligence tests, and illustrates the BLM datasets, their construction and benchmarking, and targeted experiments on chunking and systematicity. BLMs are multiple-choice problems, structured at multiple levels: within each sentence, across the input sequence, within each candidate answer. Because of their rich structure, these curated, but naturalistic datasets are key to answer some core ques...

---

### 19. The Art of Efficient Reasoning: Data, Reward, and Optimization

**Authors:** Taiqiang Wu, Zenan Zu, Bo Zhou, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20945v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20945v1)

**Summary:** Large Language Models (LLMs) consistently benefit from scaled Chain-of-Thought (CoT) reasoning, but also suffer from heavy computational overhead. To address this issue, efficient reasoning aims to incentivize short yet accurate thinking trajectories, typically through reward shaping with Reinforcement Learning (RL). In this paper, we systematically investigate the mechanics of efficient reasoning for LLMs. For comprehensive evaluation, we advocate for more fine-grained metrics, including length...

---

### 20. Predicting Sentence Acceptability Judgments in Multimodal Contexts

**Authors:** Hyewon Jang, Nikolai Ilinykh, Sharid Loáiciga, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20918v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20918v1)

**Summary:** Previous work has examined the capacity of deep neural networks (DNNs), particularly transformers, to predict human sentence acceptability judgments, both independently of context, and in document contexts. We consider the effect of prior exposure to visual images (i.e., visual context) on these judgments for humans and large language models (LLMs). Our results suggest that, in contrast to textual context, visual images appear to have little if any impact on human acceptability ratings. However,...

---

### 21. Exa-PSD: a new Persian sentiment analysis dataset on Twitter

**Authors:** Seyed Himan Ghaderi, Saeed Sarbazi Azad, Mohammad Mehdi Jaziriyan, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20892v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20892v1)

**Summary:** Today, Social networks such as Twitter are the most widely used platforms for communication of people. Analyzing this data has useful information to recognize the opinion of people in tweets. Sentiment analysis plays a vital role in NLP, which identifies the opinion of the individuals about a specific topic. Natural language processing in Persian has many challenges despite the adventure of strong language models. The datasets available in Persian are generally in special topics such as products...

---

### 22. FinAnchor: Aligned Multi-Model Representations for Financial Prediction

**Authors:** Zirui He, Huopu Zhang, Yanguang Liu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20859v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20859v1)

**Summary:** Financial prediction from long documents involves significant challenges, as actionable signals are often sparse and obscured by noise, and the optimal LLM for generating embeddings varies across tasks and time periods. In this paper, we propose FinAnchor(Financial Anchored Representations), a lightweight framework that integrates embeddings from multiple LLMs without fine-tuning the underlying models. FinAnchor addresses the incompatibility of feature spaces by selecting an anchor embedding spa...

---

### 23. Don't Ignore the Tail: Decoupling top-K Probabilities for Efficient Language Model Distillation

**Authors:** Sayantan Dasgupta, Trevor Cohn, Timothy Baldwin

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20816v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20816v1)

**Summary:** The core learning signal used in language model distillation is the standard Kullback-Leibler (KL) divergence between the student and teacher distributions. Traditional KL divergence tends to be dominated by the next tokens with the highest probabilities, i.e., the teacher's modes, thereby diminishing the influence of less probable yet potentially informative components of the output distribution. We propose a new tail-aware divergence that decouples the contribution of the teacher model's top-K...

---

### 24. Overton Pluralistic Reinforcement Learning for Large Language Models

**Authors:** Yu Fu, Seongho Son, Ilija Bogunovic

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20759v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20759v1)

**Summary:** Existing alignment paradigms remain limited in capturing the pluralistic nature of human values. Overton Pluralism addresses this gap by generating responses with diverse perspectives from a single query. This paper introduces OP-GRPO (Overton Pluralistic Group Relative Policy Optimization), a reinforcement learning framework for implicit Overton Pluralism that enables a single large language model to produce pluralistic responses without explicit prompting or modular orchestration. Our workflow...

---

### 25. SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing

**Authors:** Yifei Xu, Guilherme Potje, Shivam Shandilya, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20751v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20751v1)

**Summary:** Designing aligned and robust rewards for open-ended generation remains a key barrier to RL post-training. Rubrics provide structured, interpretable supervision, but scaling rubric construction is difficult: expert rubrics are costly, prompted rubrics are often superficial or inconsistent, and fixed-pool discriminative rubrics can saturate and drift, enabling reward hacking. We present SibylSense, an inference-time learning approach that adapts a frozen rubric generator through a tunable memory b...

---

### 26. Explicit Grammar Semantic Feature Fusion for Robust Text Classification

**Authors:** Azrin Sultana, Firoz Ahmed

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20749v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20749v1)

**Summary:** Natural Language Processing enables computers to understand human language by analysing and classifying text efficiently with deep-level grammatical and semantic features. Existing models capture features by learning from large corpora with transformer models, which are computationally intensive and unsuitable for resource-constrained environments. Therefore, our proposed study incorporates comprehensive grammatical rules alongside semantic information to build a robust, lightweight classificati...

---

### 27. Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization

**Authors:** Gabriel Loiseau, Damien Sileo, Damien Riquet, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20743v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20743v1)

**Summary:** Anonymizing textual documents is a highly context-sensitive problem: the appropriate balance between privacy protection and utility preservation varies with the data domain, privacy objectives, and downstream application. However, existing anonymization methods rely on static, manually designed strategies that lack the flexibility to adjust to diverse requirements and often fail to generalize across domains. We introduce adaptive text anonymization, a new task formulation in which anonymization ...

---

### 28. RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition

**Authors:** Kun Ran, Marwah Alaofi, Danula Hettiachchi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20735v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20735v1)

**Summary:** This paper presents the award-winning RMIT-ADM+S system for the Text-to-Text   track of the NeurIPS~2025 MMU-RAG Competition. We introduce Routing-to-RAG   (R2RAG), a research-focused retrieval-augmented generation (RAG)   architecture composed of lightweight components that dynamically adapt the   retrieval strategy based on inferred query complexity and evidence   sufficiency. The system uses smaller LLMs, enabling operation on a single   consumer-grade GPU while supporting complex research ta...

---

### 29. ID-LoRA: Efficient Low-Rank Adaptation Inspired by Matrix Interpolative Decomposition

**Authors:** Xindian Ma, Rundong Kong, Peng Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20727v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20727v1)

**Summary:** LoRA has become a universal Parameter-Efficient Fine-Tuning (PEFT) technique that equips Large Language Models (LLMs) to adapt quickly to new tasks. However, when these models are scaled up, even the latest LoRA variants still introduce considerable overhead in trainable parameters. Conversely, aggressively lowering the rank to curb this overhead markedly degrades performance in complex multi-task settings. We propose ID-LoRA, a novel PEFT framework that breaks the trade-off. Its core innovation...

---

### 30. Counterfactual Simulation Training for Chain-of-Thought Faithfulness

**Authors:** Peter Hase, Christopher Potts

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20710v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20710v1)

**Summary:** Inspecting Chain-of-Thought reasoning is among the most common means of understanding why an LLM produced its output. But well-known problems with CoT faithfulness severely limit what insights can be gained from this practice. In this paper, we introduce a training method called Counterfactual Simulation Training (CST), which aims to improve CoT faithfulness by rewarding CoTs that enable a simulator to accurately predict a model's outputs over counterfactual inputs. We apply CST in two settings:...

---

### 31. CAMEL: Confidence-Gated Reflection for Reward Modeling

**Authors:** Zirui Zhu, Hailun Xu, Yang Luo, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20670v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20670v1)

**Summary:** Reward models play a fundamental role in aligning large language models with human preferences. Existing methods predominantly follow two paradigms: scalar discriminative preference models, which are efficient but lack interpretability, and generative judging models, which offer richer reasoning at the cost of higher computational overhead. We observe that the log-probability margin between verdict tokens strongly correlates with prediction correctness, providing a reliable proxy for instance di...

---

### 32. CARE: An Explainable Computational Framework for Assessing Client-Perceived Therapeutic Alliance Using Large Language Models

**Authors:** Anqi Li, Chenxiao Wang, Yu Lu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20648v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20648v1)

**Summary:** Client perceptions of the therapeutic alliance are critical for counseling effectiveness. Accurately capturing these perceptions remains challenging, as traditional post-session questionnaires are burdensome and often delayed, while existing computational approaches produce coarse scores, lack interpretable rationales, and fail to model holistic session context. We present CARE, an LLM-based framework to automatically predict multi-dimensional alliance scores and generate interpretable rationale...

---

### 33. Semantic Novelty at Scale: Narrative Shape Taxonomy and Readership Prediction in 28,606 Books

**Authors:** W. Frederick Zimmerman

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20647v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20647v1)

**Summary:** I introduce semantic novelty--cosine distance between each paragraph's sentence embedding and the running centroid of all preceding paragraphs--as an information-theoretic measure of narrative structure at corpus scale. Applying it to 28,606 books in PG19 (pre-1920 English literature), I compute paragraph-level novelty curves using 768-dimensional SBERT embeddings, then reduce each to a 16-segment Piecewise Aggregate Approximation (PAA). Ward-linkage clustering on PAA vectors reveals eight canon...

---

### 34. Enhancing Hate Speech Detection on Social Media: A Comparative Analysis of Machine Learning Models and Text Transformation Approaches

**Authors:** Saurabh Mishra, Shivani Thakur, Radhika Mamidi

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20634v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20634v1)

**Summary:** The proliferation of hate speech on social media platforms has necessitated the development of effective detection and moderation tools. This study evaluates the efficacy of various machine learning models in identifying hate speech and offensive language and investigates the potential of text transformation techniques to neutralize such content. We compare traditional models like CNNs and LSTMs with advanced neural network models such as BERT and its derivatives, alongside exploring hybrid mode...

---

### 35. SpecMind: Cognitively Inspired, Interactive Multi-Turn Framework for Postcondition Inference

**Authors:** Cuong Chi Le, Minh V. T Pham, Tung Vu Duy, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20610v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20610v1)

**Summary:** Specifications are vital for ensuring program correctness, yet writing them manually remains challenging and time-intensive. Recent large language model (LLM)-based methods have shown successes in generating specifications such as postconditions, but existing single-pass prompting often yields inaccurate results. In this paper, we present SpecMind, a novel framework for postcondition generation that treats LLMs as interactive and exploratory reasoners rather than one-shot generators. SpecMind em...

---

### 36. Personal Information Parroting in Language Models

**Authors:** Nishant Subramani, Kshitish Ghate, Mona Diab

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20580v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20580v1)

**Summary:** Modern language models (LM) are trained on large scrapes of the Web, containing millions of personal information (PI) instances, many of which LMs memorize, increasing privacy risks. In this work, we develop the regexes and rules (R&R) detector suite to detect email addresses, phone numbers, and IP addresses, which outperforms the best regex-based PI detectors. On a manually curated set of 483 instances of PI, we measure memorization: finding that 13.6% are parroted verbatim by the Pythia-6.9b m...

---

### 37. GATES: Self-Distillation under Privileged Context with Consensus Gating

**Authors:** Alex Stein, Furong Huang, Tom Goldstein

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20574v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20574v1)

**Summary:** We study self-distillation in settings where supervision is unreliable: there are no ground truth labels, verifiable rewards, or external graders to evaluate answers. We focus on document-grounded question answering with asymmetric context, where a single model serves as both tutor (with access to a relevant source document during training) and student (answering from the question alone at test time). Rather than assuming tutor correctness, we derive supervision online from tutor consensus by sa...

---

### 38. Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training

**Authors:** Zhengyao Gu, Jonathan Light, Raul Astudillo, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20532v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20532v1)

**Summary:** Post-training large foundation models with reinforcement learning typically relies on massive and heterogeneous datasets, making effective curriculum learning both critical and challenging. In this work, we propose ACTOR-CURATOR, a scalable and fully automated curriculum learning framework for reinforcement learning post-training of large language models (LLMs). ACTOR-CURATOR learns a neural curator that dynamically selects training problems from large problem banks by directly optimizing for ex...

---

### 39. Stop-Think-AutoRegress: Language Modeling with Latent Diffusion Planning

**Authors:** Justin Lovelace, Christian Belardi, Sofian Zalouk, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20528v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20528v1)

**Summary:** The Stop-Think-AutoRegress Language Diffusion Model (STAR-LDM) integrates latent diffusion planning with autoregressive generation. Unlike conventional autoregressive language models limited to token-by-token decisions, STAR-LDM incorporates a "thinking" phase that pauses generation to refine a semantic plan through diffusion before continuing. This enables global planning in continuous space prior to committing to discrete tokens. Evaluations show STAR-LDM significantly outperforms similar-size...

---

### 40. Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination

**Authors:** Rakshit Trivedi, Kartik Sharma, David C Parkes

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20517v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20517v1)

**Summary:** Effective human-AI coordination requires artificial agents capable of exhibiting and responding to human-like behaviors while adapting to changing contexts. Imitation learning has emerged as one of the prominent approaches to build such agents by training them to mimic human-demonstrated behaviors. However, current methods struggle to capture the inherent diversity and non-Markovian nature of human behavior and lack the ability to steer behavior at inference time. Drawing inspiration from the th...

---

### 41. From Performance to Purpose: A Sociotechnical Taxonomy for Evaluating Large Language Model Utility

**Authors:** Gavin Levinson, Keith Feldman

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20513v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20513v1)

**Summary:** As large language models (LLMs) continue to improve at completing discrete tasks, they are being integrated into increasingly complex and diverse real-world systems. However, task-level success alone does not establish a model's fit for use in practice. In applied, high-stakes settings, LLM effectiveness is driven by a wider array of sociotechnical determinants that extend beyond conventional performance measures. Although a growing set of metrics capture many of these considerations, they are r...

---

### 42. PreScience: A Benchmark for Forecasting Scientific Contributions

**Authors:** Anirudh Ajith, Amanpreet Singh, Jay DeYoung, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20459v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20459v1)

**Summary:** Can AI systems trained on the scientific record up to a fixed point in time forecast the scientific advances that follow? Such a capability could help researchers identify collaborators and impactful research directions, and anticipate which problems and methods will become central next. We introduce PreScience -- a scientific forecasting benchmark that decomposes the research process into four interdependent generative tasks: collaborator prediction, prior work selection, contribution generatio...

---

### 43. Protein Language Models Diverge from Natural Language: Comparative Analysis and Improved Inference

**Authors:** Anna Hart, Chi Han, Jeonghwan Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20449v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20449v1)

**Summary:** Modern Protein Language Models (PLMs) apply transformer-based model architectures from natural language processing to biological sequences, predicting a variety of protein functions and properties. However, protein language has key differences from natural language, such as a rich functional space despite a vocabulary of only 20 amino acids. These differences motivate research into how transformer-based architectures operate differently in the protein domain and how we can better leverage PLMs t...

---

### 44. Disentangling Geometry, Performance, and Training in Language Models

**Authors:** Atharva Kulkarni, Jacob Mitchell Springer, Arjun Subramonian, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20433v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20433v1)

**Summary:** Geometric properties of Transformer weights, particularly the unembedding matrix, have been widely useful in language model interpretability research. Yet, their utility for estimating downstream performance remains unclear. In this work, we systematically investigate the relationship between model performance and the unembedding matrix geometry, particularly its effective rank. Our experiments, involving a suite of 108 OLMo-style language models trained under controlled variation, reveal severa...

---

### 45. MedCLIPSeg: Probabilistic Vision-Language Adaptation for Data-Efficient and Generalizable Medical Image Segmentation

**Authors:** Taha Koleilat, Hojat Asgariandehkordi, Omid Nejati Manzari, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20423v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20423v1)

**Summary:** Medical image segmentation remains challenging due to limited annotations for training, ambiguous anatomical features, and domain shifts. While vision-language models such as CLIP offer strong cross-modal representations, their potential for dense, text-guided medical image segmentation remains underexplored. We present MedCLIPSeg, a novel framework that adapts CLIP for robust, data-efficient, and uncertainty-aware medical image segmentation. Our approach leverages patch-level CLIP embeddings th...

---

### 46. Case-Aware LLM-as-a-Judge Evaluation for Enterprise-Scale RAG Systems

**Authors:** Mukul Chhabra, Luigi Medrano, Arush Verma

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20379v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20379v1)

**Summary:** Enterprise Retrieval-Augmented Generation (RAG) assistants operate in multi-turn, case-based workflows such as technical support and IT operations, where evaluation must reflect operational constraints, structured identifiers (e.g., error codes, versions), and resolution workflows. Existing RAG evaluation frameworks are primarily designed for benchmark-style or single-turn settings and often fail to capture enterprise-specific failure modes such as case misidentification, workflow misalignment, ...

---

### 47. How communicatively optimal are exact numeral systems? Once more on lexicon size and morphosyntactic complexity

**Authors:** Chundra Cathcart, Arne Rubehn, Katja Bocklage, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20372v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20372v1)

**Summary:** Recent research argues that exact recursive numeral systems optimize communicative efficiency by balancing a tradeoff between the size of the numeral lexicon and the average morphosyntactic complexity (roughly length in morphemes) of numeral terms. We argue that previous studies have not characterized the data in a fashion that accounts for the degree of complexity languages display. Using data from 52 genetically diverse languages and an annotation scheme distinguishing between predictable and ...

---

### 48. Natural Language Processing Models for Robust Document Categorization

**Authors:** Radoslaw Roszczyk, Pawel Tecza, Maciej Stodolski, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20336v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20336v1)

**Summary:** This article presents an evaluation of several machine learning methods applied to automated text classification, alongside the design of a demonstrative system for unbalanced document categorization and distribution. The study focuses on balancing classification accuracy with computational efficiency, a key consideration when integrating AI into real world automation pipelines. Three models of varying complexity were examined: a Naive Bayes classifier, a bidirectional LSTM network, and a fine t...

---

### 49. No One Size Fits All: QueryBandits for Hallucination Mitigation

**Authors:** Nicole Cho, William Watson, Alec Koppel, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20332v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20332v1)

**Summary:** Advanced reasoning capabilities in Large Language Models (LLMs) have led to more frequent hallucinations; yet most mitigation work focuses on open-source models for post-hoc detection and parameter editing. The dearth of studies focusing on hallucinations in closed-source models is especially concerning, as they constitute the vast majority of models in institutional deployments. We introduce QueryBandits, a model-agnostic contextual bandit framework that adaptively learns online to select the o...

---

### 50. An artificial intelligence framework for end-to-end rare disease phenotyping from clinical notes using large language models

**Authors:** Cathy Shyr, Yan Hu, Rory J. Tinker, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20324v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20324v1)

**Summary:** Phenotyping is fundamental to rare disease diagnosis, but manual curation of structured phenotypes from clinical notes is labor-intensive and difficult to scale. Existing artificial intelligence approaches typically optimize individual components of phenotyping but do not operationalize the full clinical workflow of extracting features from clinical text, standardizing them to Human Phenotype Ontology (HPO) terms, and prioritizing diagnostically informative HPO terms. We developed RARE-PHENIX, a...

---

## cs.CV

**50 papers**

### 1. Test-Time Training with KV Binding Is Secretly Linear Attention

**Authors:** Junchen Liu, Sven Elflein, Or Litany, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21204v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21204v1)

**Summary:** Test-time training (TTT) with KV binding as sequence modeling layer is commonly interpreted as a form of online meta-learning that memorizes a key-value mapping at test time. However, our analysis reveals multiple phenomena that contradict this memorization-based interpretation. Motivated by these findings, we revisit the formulation of TTT and show that a broad class of TTT architectures can be expressed as a form of learned linear attention operator. Beyond explaining previously puzzling model...

---

### 2. Squint: Fast Visual Reinforcement Learning for Sim-to-Real Robotics

**Authors:** Abdulaziz Almuzairee, Henrik I. Christensen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21203v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21203v1)

**Summary:** Visual reinforcement learning is appealing for robotics but expensive -- off-policy methods are sample-efficient yet slow; on-policy methods parallelize well but waste samples. Recent work has shown that off-policy methods can train faster than on-policy methods in wall-clock time for state-based control. Extending this to vision remains challenging, where high-dimensional input images complicate training dynamics and introduce substantial storage and encoding overhead. To address these challeng...

---

### 3. Multi-Vector Index Compression in Any Modality

**Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21202v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21202v1)

**Summary:** We study efficient multi-vector retrieval for late interaction in any modality. Late interaction has emerged as a dominant paradigm for information retrieval in text, images, visual documents, and videos, but its computation and storage costs grow linearly with document length, making it costly for image-, video-, and audio-rich corpora. To address this limitation, we explore query-agnostic methods for compressing multi-vector document representations under a constant vector budget. We introduce...

---

### 4. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

**Authors:** Yining Hong, Huang Huang, Manling Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21198v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21198v1)

**Summary:** Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflec...

---

### 5. Region of Interest Segmentation and Morphological Analysis for Membranes in Cryo-Electron Tomography

**Authors:** Xingyi Cheng, Julien Maufront, Aurélie Di Cicco, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21195v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21195v1)

**Summary:** Cryo-electron tomography (cryo-ET) enables high resolution, three-dimensional reconstruction of biological structures, including membranes and membrane proteins. Identification of regions of interest (ROIs) is central to scientific imaging, as it enables isolation and quantitative analysis of specific structural features within complex datasets. In practice, however, ROIs are typically derived indirectly through full structure segmentation followed by post hoc analysis. This limitation is especi...

---

### 6. Human Video Generation from a Single Image with 3D Pose and View Control

**Authors:** Tiantian Wang, Chun-Han Yao, Tao Hu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21188v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21188v1)

**Summary:** Recent diffusion methods have made significant progress in generating videos from single images due to their powerful visual generation capabilities. However, challenges persist in image-to-video synthesis, particularly in human video generation, where inferring view-consistent, motion-dependent clothing wrinkles from a single image remains a formidable problem. In this paper, we present Human Video Generation in 4D (HVG), a latent video diffusion model capable of generating high-quality, multi-...

---

### 7. Spa3R: Predictive Spatial Field Modeling for 3D Visual Reasoning

**Authors:** Haoyi Jiang, Liu Liu, Xinjie Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21186v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21186v1)

**Summary:** While Vision-Language Models (VLMs) exhibit exceptional 2D visual understanding, their ability to comprehend and reason about 3D space--a cornerstone of spatial intelligence--remains superficial. Current methodologies attempt to bridge this domain gap either by relying on explicit 3D modalities or by augmenting VLMs with partial, view-conditioned geometric priors. However, such approaches hinder scalability and ultimately burden the language model with the ill-posed task of implicitly reconstruc...

---

### 8. Mask-HybridGNet: Graph-based segmentation with emergent anatomical correspondence from pixel-level supervision

**Authors:** Nicolás Gaggion, Maria J. Ledesma-Carbayo, Stergios Christodoulidis, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21179v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21179v1)

**Summary:** Graph-based medical image segmentation represents anatomical structures using boundary graphs, providing fixed-topology landmarks and inherent population-level correspondences. However, their clinical adoption has been hindered by a major requirement: training datasets with manually annotated landmarks that maintain point-to-point correspondences across patients rarely exist in practice. We introduce Mask-HybridGNet, a framework that trains graph-based models directly using standard pixel-wise m...

---

### 9. XMorph: Explainable Brain Tumor Analysis Via LLM-Assisted Hybrid Deep Intelligence

**Authors:** Sepehr Salem Ghahfarokhi, M. Moein Esfahani, Raj Sunderraman, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21178v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21178v1)

**Summary:** Deep learning has significantly advanced automated brain tumor diagnosis, yet clinical adoption remains limited by interpretability and computational constraints. Conventional models often act as opaque ''black boxes'' and fail to quantify the complex, irregular tumor boundaries that characterize malignant growth. To address these challenges, we present XMorph, an explainable and computationally efficient framework for fine-grained classification of three prominent brain tumor types: glioma, men...

---

### 10. Seeing Through Words: Controlling Visual Retrieval Quality with Language Models

**Authors:** Jianglin Lu, Simon Jenni, Kushal Kafle, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21175v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21175v1)

**Summary:** Text-to-image retrieval is a fundamental task in vision-language learning, yet in real-world scenarios it is often challenged by short and underspecified user queries. Such queries are typically only one or two words long, rendering them semantically ambiguous, prone to collisions across diverse visual interpretations, and lacking explicit control over the quality of retrieved images. To address these issues, we propose a new paradigm of quality-controllable retrieval, which enriches short queri...

---

### 11. NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning

**Authors:** Ishaan Rawal, Shubh Gupta, Yihan Hu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21172v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21172v1)

**Summary:** Vision-Language-Action (VLA) models are advancing autonomous driving by replacing modular pipelines with unified end-to-end architectures. However, current VLAs face two expensive requirements: (1) massive dataset collection, and (2) dense reasoning annotations. In this work, we address both challenges with \modelname (\textbf{No} \textbf{R}easoning for \textbf{D}riving). Compared to existing VLAs, \modelname achieves competitive performance while being fine-tuned on $<$60\% of the data and no r...

---

### 12. SPRITETOMESH: Automatic Mesh Generation for 2D Skeletal Animation Using Learned Segmentation and Contour-Aware Vertex Placement

**Authors:** Bastien Gimbert

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21153v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21153v1)

**Summary:** We present SPRITETOMESH, a fully automatic pipeline for converting 2D game sprite images into triangle meshes compatible with skeletal animation frameworks such as Spine2D. Creating animation-ready meshes is traditionally a tedious manual process requiring artists to carefully place vertices along visual boundaries, a task that typically takes 15-60 minutes per sprite. Our method addresses this through a hybrid learned-algorithmic approach. A segmentation network (EfficientNet-B0 encoder with U-...

---

### 13. LUMEN: Longitudinal Multi-Modal Radiology Model for Prognosis and Diagnosis

**Authors:** Zhifan Jiang, Dong Yang, Vishwesh Nath, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21142v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21142v1)

**Summary:** Large vision-language models (VLMs) have evolved from general-purpose applications to specialized use cases such as in the clinical domain, demonstrating potential for decision support in radiology. One promising application is assisting radiologists in decision-making by the analysis of radiology imaging data such as chest X-rays (CXR) via a visual and natural language question-answering (VQA) interface. When longitudinal imaging is available, radiologists analyze temporal changes, which are es...

---

### 14. SynthRender and IRIS: Open-Source Framework and Dataset for Bidirectional Sim-Real Transfer in Industrial Object Perception

**Authors:** Jose Moises Araya-Martinez, Thushar Tom, Adrián Sanchis Reig, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21141v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21141v1)

**Summary:** Object perception is fundamental for tasks such as robotic material handling and quality inspection. However, modern supervised deep-learning perception models require large datasets for robust automation under semi-uncontrolled conditions. The cost of acquiring and annotating such data for proprietary parts is a major barrier for widespread deployment. In this context, we release SynthRender, an open source framework for synthetic image generation with Guided Domain Randomization capabilities. ...

---

### 15. UDVideoQA: A Traffic Video Question Answering Dataset for Multi-Object Spatio-Temporal Reasoning in Urban Dynamics

**Authors:** Joseph Raj Vishal, Nagasiri Poluri, Katha Naik, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21137v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21137v1)

**Summary:** Understanding the complex, multi-agent dynamics of urban traffic remains a fundamental challenge for video language models. This paper introduces Urban Dynamics VideoQA, a benchmark dataset that captures the unscripted real-world behavior of dynamic urban scenes. UDVideoQA is curated from 16 hours of traffic footage recorded at multiple city intersections under diverse traffic, weather, and lighting conditions. It employs an event-driven dynamic blur technique to ensure privacy preservation with...

---

### 16. BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting

**Authors:** Jiaxing Yu, Dongyang Ren, Hangyu Xu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21105v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21105v1)

**Summary:** The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to generalize to novel shapes. We propose B-rep Gaussian Splatting (BrepGaussian), a novel framework that le...

---

### 17. Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones

**Authors:** Rong Zou, Marco Cannici, Davide Scaramuzza

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21101v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21101v1)

**Summary:** Fast-flying aerial robots promise rapid inspection under limited battery constraints, with direct applications in infrastructure inspection, terrain exploration, and search and rescue. However, high speeds lead to severe motion blur in images and induce significant drift and noise in pose estimates, making dense 3D reconstruction with Neural Radiance Fields (NeRFs) particularly challenging due to their high sensitivity to such degradations. In this work, we present a unified framework that lever...

---

### 18. Skullptor: High Fidelity 3D Head Reconstruction in Seconds with Multi-View Normal Prediction

**Authors:** Noé Artru, Rukhshanda Hussain, Emeline Got, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21100v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21100v1)

**Summary:** Reconstructing high-fidelity 3D head geometry from images is critical for a wide range of applications, yet existing methods face fundamental limitations. Traditional photogrammetry achieves exceptional detail but requires extensive camera arrays (25-200+ views), substantial computation, and manual cleanup in challenging areas like facial hair. Recent alternatives present a fundamental trade-off: foundation models enable efficient single-image reconstruction but lack fine geometric detail, while...

---

### 19. Optimizing Occupancy Sensor Placement in Smart Environments

**Authors:** Hao Lu, Richard J. Radke

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21098v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21098v1)

**Summary:** Understanding the locations of occupants in a commercial built environment is critical for realizing energy savings by delivering lighting, heating, and cooling only where it is needed. The key to achieving this goal is being able to recognize zone occupancy in real time, without impeding occupants' activities or compromising privacy. While low-resolution, privacy-preserving time-of-flight (ToF) sensor networks have demonstrated good performance in zone counting, the performance depends on caref...

---

### 20. ProxyFL: A Proxy-Guided Framework for Federated Semi-Supervised Learning

**Authors:** Duowen Chen, Yan Wang

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21078v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21078v1)

**Summary:** Federated Semi-Supervised Learning (FSSL) aims to collaboratively train a global model across clients by leveraging partially-annotated local data in a privacy-preserving manner. In FSSL, data heterogeneity is a challenging issue, which exists both across clients and within clients. External heterogeneity refers to the data distribution discrepancy across different clients, while internal heterogeneity represents the mismatch between labeled and unlabeled data within clients. Most FSSL methods t...

---

### 21. Motivation is Something You Need

**Authors:** Mehdi Acheli, Walid Gaaloul

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21064v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21064v1)

**Summary:** This work introduces a novel training paradigm that draws from affective neuroscience. Inspired by the interplay of emotions and cognition in the human brain and more specifically the SEEKING motivational state, we design a dual-model framework where a smaller base model is trained continuously, while a larger motivated model is activated intermittently during predefined "motivation conditions". The framework mimics the emotional state of high curiosity and anticipation of reward in which broade...

---

### 22. VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation

**Authors:** Seongheon Park, Changdae Oh, Hyeong Kyu Choi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21054v1)

**Summary:** Large Vision-Language Models (LVLMs) frequently hallucinate, limiting their safe deployment in real-world applications. Existing LLM self-evaluation methods rely on a model's ability to estimate the correctness of its own outputs, which can improve deployment reliability; however, they depend heavily on language priors and are therefore ill-suited for evaluating vision-conditioned predictions. We propose VAUQ, a vision-aware uncertainty quantification framework for LVLM self-evaluation that expl...

---

### 23. OCR-Agent: Agentic OCR with Capability and Memory Reflection

**Authors:** Shimin Wen, Zeyu Zhang, Xingdou Bian, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21053v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21053v1)

**Summary:** Large Vision-Language Models (VLMs) have demonstrated significant potential on complex visual understanding tasks through iterative optimization methods.However, these models generally lack effective self-correction mechanisms, making it difficult for them to independently rectify cognitive biases. Consequently, during multi-turn revisions, they often fall into repetitive and ineffective attempts, failing to achieve stable improvements in answer quality.To address this issue, we propose a novel ...

---

### 24. OmniOCR: Generalist OCR for Ethnic Minority Languages

**Authors:** Bonan Liu, Zeyu Zhang, Bingbing Meng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21042v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21042v1)

**Summary:** Optical character recognition (OCR) has advanced rapidly with deep learning and multimodal models, yet most methods focus on well-resourced scripts such as Latin and Chinese. Ethnic minority languages remain underexplored due to complex writing systems, scarce annotations, and diverse historical and modern forms, making generalization in low-resource or zero-shot settings challenging. To address these challenges, we present OmniOCR, a universal framework for ethnic minority scripts. OmniOCR intr...

---

### 25. Not Just What's There: Enabling CLIP to Comprehend Negated Visual Descriptions Without Fine-tuning

**Authors:** Junhao Xiao, Zhiyu Wu, Hao Lin, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21035v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21035v1)

**Summary:** Vision-Language Models (VLMs) like CLIP struggle to understand negation, often embedding affirmatives and negatives similarly (e.g., matching "no dog" with dog images). Existing methods refine negation understanding via fine-tuning CLIP's text encoder, risking overfitting. In this work, we propose CLIPGlasses, a plug-and-play framework that enhances CLIP's ability to comprehend negated visual descriptions. CLIPGlasses adopts a dual-stage design: a Lens module disentangles negated semantics from ...

---

### 26. MIP Candy: A Modular PyTorch Framework for Medical Image Processing

**Authors:** Tianhao Fu, Yucheng Chen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21033v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21033v1)

**Summary:** Medical image processing demands specialized software that handles high-dimensional volumetric data, heterogeneous file formats, and domain-specific training procedures. Existing frameworks either provide low-level components that require substantial integration effort or impose rigid, monolithic pipelines that resist modification. We present MIP Candy (MIPCandy), a freely available, PyTorch-based framework designed specifically for medical image processing. MIPCandy provides a complete, modular...

---

### 27. From Perception to Action: An Interactive Benchmark for Vision Reasoning

**Authors:** Yuhao Wu, Maojia Song, Yihuai Lan, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21015v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21015v1)

**Summary:** Understanding the physical structure is essential for real-world applications such as embodied agents, interactive design, and long-horizon manipulation. Yet, prevailing Vision-Language Model (VLM) evaluations still center on structure-agnostic, single-turn setups (e.g., VQA), which fail to assess agents' ability to reason about how geometry, contact, and support relations jointly constrain what actions are possible in a dynamic environment. To address this gap, we introduce the Causal Hierarchy...

---

### 28. Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design

**Authors:** Jiannan Huang, Aditya Kane, Fengzhe Zhou, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21010v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21010v1)

**Summary:** Real-time object detection is crucial for real-world applications as it requires high accuracy with low latency. While Detection Transformers (DETR) have demonstrated significant performance improvements, current real-time DETR models are challenging to reproduce from scratch due to excessive pre-training overheads on the backbone, constraining research advancements by hindering the exploration of novel backbone architectures. In this paper, we want to show that by using general good design, it ...

---

### 29. VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models

**Authors:** Bowen Zheng, Yongli Xiang, Ziming Hong, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20999v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20999v1)

**Summary:** Image-to-Video (I2V) generation models, which condition video generation on reference images, have shown emerging visual instruction-following capability, allowing certain visual cues in reference images to act as implicit control signals for video generation. However, this capability also introduces a previously overlooked risk: adversaries may exploit visual instructions to inject malicious intent through the image modality. In this work, we uncover this risk by proposing Visual Instruction In...

---

### 30. Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures

**Authors:** Yubin Ge, Yongsong Huang, Xiaofeng Liu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20994v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20994v1)

**Summary:** Report-supervised (RSuper) learning seeks to alleviate the need for dense tumor voxel labels with constraints derived from radiology reports (e.g., volumes, counts, sizes, locations). In MRI studies of brain tumors, however, we often involve multi-parametric scans and substructures. Here, fine-grained modality/parameter-wise reports are usually provided along with global findings and are correlated with different substructures. Moreover, the reports often describe only the largest lesion and pro...

---

### 31. Cycle-Consistent Tuning for Layered Image Decomposition

**Authors:** Zheng Gu, Min Lu, Zhida Sun, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20989v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20989v1)

**Summary:** Disentangling visual layers in real-world images is a persistent challenge in vision and graphics, as such layers often involve non-linear and globally coupled interactions, including shading, reflection, and perspective distortion. In this work, we present an in-context image decomposition framework that leverages large diffusion foundation models for layered separation. We focus on the challenging case of logo-object decomposition, where the goal is to disentangle a logo from the surface on wh...

---

### 32. EW-DETR: Evolving World Object Detection via Incremental Low-Rank DEtection TRansformer

**Authors:** Munish Monga, Vishal Chudasama, Pankaj Wasnik, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20985v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20985v1)

**Summary:** Real-world object detection must operate in evolving environments where new classes emerge, domains shift, and unseen objects must be identified as "unknown": all without accessing prior data. We introduce Evolving World Object Detection (EWOD), a paradigm coupling incremental learning, domain adaptation, and unknown detection under exemplar-free constraints. To tackle EWOD, we propose EW-DETR framework that augments DETR-based detectors with three synergistic modules: Incremental LoRA Adapters ...

---

### 33. Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models

**Authors:** Christian Simon, MAsato Ishii, Wei-Yao Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20981v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20981v1)

**Summary:** Scaling multimodal alignment between video and audio is challenging, particularly due to limited data and the mismatch between text descriptions and frame-level video information. In this work, we tackle the scaling challenge in multimodal-to-audio generation, examining whether models trained on short instances can generalize to longer ones during testing. To tackle this challenge, we present multimodal hierarchical networks so-called MMHNet, an enhanced extension of state-of-the-art video-to-au...

---

### 34. CrystaL: Spontaneous Emergence of Visual Latents in MLLMs

**Authors:** Yang Zhang, Danyang Li, Yuxuan Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20980v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20980v1)

**Summary:** Multimodal Large Language Models (MLLMs) have achieved remarkable performance by integrating powerful language backbones with large-scale visual encoders. Among these, latent Chain-of-Thought (CoT) methods enable implicit reasoning in continuous hidden states, facilitating seamless vision-language integration and faster inference. However, existing heuristically predefined supervision signals in latent CoT provide limited guidance for preserving critical visual information in intermediate latent...

---

### 35. Are Multimodal Large Language Models Good Annotators for Image Tagging?

**Authors:** Ming-Kun Xie, Jia-Hao Xiao, Zhiqiang Kou, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20972v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20972v1)

**Summary:** Image tagging, a fundamental vision task, traditionally relies on human-annotated datasets to train multi-label classifiers, which incurs significant labor and costs. While Multimodal Large Language Models (MLLMs) offer promising potential to automate annotation, their capability to replace human annotators remains underexplored. This paper aims to analyze the gap between MLLM-generated and human annotations and to propose an effective solution that enables MLLM-based annotation to replace manua...

---

### 36. See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis

**Authors:** Jaehyun Park, Minyoung Ahn, Minkyu Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20951v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20951v1)

**Summary:** Despite recent advances in diffusion models, AI generated images still often contain visual artifacts that compromise realism. Although more thorough pre-training and bigger models might reduce artifacts, there is no assurance that they can be completely eliminated, which makes artifact mitigation a highly crucial area of study. Previous artifact-aware methodologies depend on human-labeled artifact datasets, which are costly and difficult to scale, underscoring the need for an automated approach...

---

### 37. Estimation of Confidence Bounds in Binary Classification using Wilson Score Kernel Density Estimation

**Authors:** Thorbjørn Mosekjær Iversen, Zebin Duan, Frederik Hagelskjær

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20947v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20947v1)

**Summary:** The performance and ease of use of deep learning-based binary classifiers have improved significantly in recent years. This has opened up the potential for automating critical inspection tasks, which have traditionally only been trusted to be done manually. However, the application of binary classifiers in critical operations depends on the estimation of reliable confidence bounds such that system performance can be ensured up to a given statistical significance. We present Wilson Score Kernel D...

---

### 38. UFO: Unifying Feed-Forward and Optimization-based Methods for Large Driving Scene Modeling

**Authors:** Kaiyuan Tan, Yingying Shen, Mingfei Tu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20943v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20943v1)

**Summary:** Dynamic driving scene reconstruction is critical for autonomous driving simulation and closed-loop learning. While recent feed-forward methods have shown promise for 3D reconstruction, they struggle with long-range driving sequences due to quadratic complexity in sequence length and challenges in modeling dynamic objects over extended durations. We propose UFO, a novel recurrent paradigm that combines the benefits of optimization-based and feed-forward methods for efficient long-range 4D reconst...

---

### 39. Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting

**Authors:** Shuangkang Fang, I-Chao Shen, Xuanyang Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20933v1)

**Summary:** Recent 3D Gaussian Splatting (3DGS) Dropout methods address overfitting under sparse-view conditions by randomly nullifying Gaussian opacities. However, we identify a neighbor compensation effect in these approaches: dropped Gaussians are often compensated by their neighbors, weakening the intended regularization. Moreover, these methods overlook the contribution of high-degree spherical harmonic coefficients (SH) to overfitting. To address these issues, we propose DropAnSH-GS, a novel anchor-ba...

---

### 40. Computing a Characteristic Orientation for Rotation-Independent Image Analysis

**Authors:** Cristian Valero-Abundio, Emilio Sansano-Sansano, Raúl Montoliu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20930v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20930v1)

**Summary:** Handling geometric transformations, particularly rotations, remains a challenge in deep learning for computer vision. Standard neural networks lack inherent rotation invariance and typically rely on data augmentation or architectural modifications to improve robustness. Although effective, these approaches increase computational demands, require specialised implementations, or alter network structures, limiting their applicability. This paper introduces General Intensity Direction (GID), a prepr...

---

### 41. LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments

**Authors:** Zeyu Jiang, Kuan Xu, Changhao Chen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20925v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20925v1)

**Summary:** Thermal cameras offer strong potential for robot perception under challenging illumination and weather conditions. However, thermal Simultaneous Localization and Mapping (SLAM) remains difficult due to unreliable feature extraction, unstable motion tracking, and inconsistent global pose and map construction, particularly in dynamic large-scale outdoor environments. To address these challenges, we propose LST-SLAM, a novel large-scale stereo thermal SLAM system that achieves robust performance in...

---

### 42. LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding

**Authors:** Jihao Qiu, Lingxi Xie, Xinyue Huo, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20913v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20913v1)

**Summary:** This paper addresses the critical and underexplored challenge of long video understanding with low computational budgets. We propose LongVideo-R1, an active, reasoning-equipped multimodal large language model (MLLM) agent designed for efficient video context navigation, avoiding the redundancy of exhaustive search. At the core of LongVideo-R1 lies a reasoning module that leverages high-level visual cues to infer the most informative video clip for subsequent processing. During inference, the age...

---

### 43. From Isolation to Integration: Building an Adaptive Expert Forest for Pre-Trained Model-based Class-Incremental Learning

**Authors:** Ruiqi Liu, Boyu Diao, Hangda Liu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20911v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20911v1)

**Summary:** Class-Incremental Learning (CIL) requires models to learn new classes without forgetting old ones. A common method is to freeze a pre-trained model and train a new, lightweight adapter for each task. While this prevents forgetting, it treats the learned knowledge as a simple, unstructured collection and fails to use the relationships between tasks. To this end, we propose the Semantic-guided Adaptive Expert Forest (SAEF), a new method that organizes adapters into a structured hierarchy for bette...

---

### 44. TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering

**Authors:** Hanshen Zhu, Yuliang Liu, Xuecheng Wu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20903v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20903v1)

**Summary:** Visual Text Rendering (VTR) remains a critical challenge in text-to-image generation, where even advanced models frequently produce text with structural anomalies such as distortion, blurriness, and misalignment. However, we find that leading MLLMs and specialist OCR models largely fail to perceive these structural anomalies, creating a critical bottleneck for both VTR evaluation and RL-based optimization. As a result, even state-of-the-art generators (e.g., SeedDream4.0, Qwen-Image) still strug...

---

### 45. SpatiaLQA: A Benchmark for Evaluating Spatial Logical Reasoning in Vision-Language Models

**Authors:** Yuechen Xie, Xiaoyan Zhang, Yicheng Shan, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20901v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20901v1)

**Summary:** Vision-Language Models (VLMs) have been increasingly applied in real-world scenarios due to their outstanding understanding and reasoning capabilities. Although VLMs have already demonstrated impressive capabilities in common visual question answering and logical reasoning, they still lack the ability to make reasonable decisions in complex real-world environments. We define this ability as spatial logical reasoning, which not only requires understanding the spatial relationships among objects i...

---

### 46. When Safety Collides: Resolving Multi-Category Harmful Conflicts in Text-to-Image Diffusion via Adaptive Safety Guidance

**Authors:** Yongli Xiang, Ziming Hong, Zhaoqing Wang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20880v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20880v1)

**Summary:** Text-to-Image (T2I) diffusion models have demonstrated significant advancements in generating high-quality images, while raising potential safety concerns regarding harmful content generation. Safety-guidance-based methods have been proposed to mitigate harmful outputs by steering generation away from harmful zones, where the zones are averaged across multiple harmful categories based on predefined keywords. However, these approaches fail to capture the complex interplay among different harm cat...

---

### 47. MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification

**Authors:** Jiahao Xu, Sheng Huang, Xin Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20873v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20873v1)

**Summary:** In computational pathology, few-shot whole slide image classification is primarily driven by the extreme scarcity of expert-labeled slides. Recent vision-language methods incorporate textual semantics generated by large language models, but treat these descriptions as static class-level priors that are shared across all samples and lack sample-wise refinement. This limits both the diversity and precision of visual-semantic alignment, hindering generalization under limited supervision. To overcom...

---

### 48. DA-Cal: Towards Cross-Domain Calibration in Semantic Segmentation

**Authors:** Wangkai Li, Rui Sun, Zhaoyang Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20860v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20860v1)

**Summary:** While existing unsupervised domain adaptation (UDA) methods greatly enhance target domain performance in semantic segmentation, they often neglect network calibration quality, resulting in misalignment between prediction confidence and actual accuracy -- a significant risk in safety-critical applications. Our key insight emerges from observing that performance degrades substantially when soft pseudo-labels replace hard pseudo-labels in cross-domain scenarios due to poor calibration, despite the ...

---

### 49. On the Explainability of Vision-Language Models in Art History

**Authors:** Stefanie Schneider

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20853v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20853v1)

**Summary:** Vision-Language Models (VLMs) transfer visual and textual data into a shared embedding space. In so doing, they enable a wide range of multimodal tasks, while also raising critical questions about the nature of machine 'understanding.' In this paper, we examine how Explainable Artificial Intelligence (XAI) methods can render the visual reasoning of a VLM - namely, CLIP - legible in art-historical contexts. To this end, we evaluate seven methods, combining zero-shot localization experiments with ...

---

### 50. Hybrid Fusion: One-Minute Efficient Training for Zero-Shot Cross-Domain Image Fusion

**Authors:** Ran Zhang, Xuanhua He, Liu Liu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20851v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20851v1)

**Summary:** Image fusion seeks to integrate complementary information from multiple sources into a single, superior image. While traditional methods are fast, they lack adaptability and performance. Conversely, deep learning approaches achieve state-of-the-art (SOTA) results but suffer from critical inefficiencies: their reliance on slow, resource-intensive, patch-based training introduces a significant gap with full-resolution inference. We propose a novel hybrid framework that resolves this trade-off. Our...

---

## cs.LG

**50 papers**

### 1. Test-Time Training with KV Binding Is Secretly Linear Attention

**Authors:** Junchen Liu, Sven Elflein, Or Litany, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21204v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21204v1)

**Summary:** Test-time training (TTT) with KV binding as sequence modeling layer is commonly interpreted as a form of online meta-learning that memorizes a key-value mapping at test time. However, our analysis reveals multiple phenomena that contradict this memorization-based interpretation. Motivated by these findings, we revisit the formulation of TTT and show that a broad class of TTT architectures can be expressed as a form of learned linear attention operator. Beyond explaining previously puzzling model...

---

### 2. Squint: Fast Visual Reinforcement Learning for Sim-to-Real Robotics

**Authors:** Abdulaziz Almuzairee, Henrik I. Christensen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21203v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21203v1)

**Summary:** Visual reinforcement learning is appealing for robotics but expensive -- off-policy methods are sample-efficient yet slow; on-policy methods parallelize well but waste samples. Recent work has shown that off-policy methods can train faster than on-policy methods in wall-clock time for state-based control. Extending this to vision remains challenging, where high-dimensional input images complicate training dynamics and introduce substantial storage and encoding overhead. To address these challeng...

---

### 3. Aletheia tackles FirstProof autonomously

**Authors:** Tony Feng, Junehyuk Jung, Sang-hyun Kim, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21201v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21201v1)

**Summary:** We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as...

---

### 4. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

**Authors:** Yining Hong, Huang Huang, Manling Li, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21198v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21198v1)

**Summary:** Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflec...

---

### 5. Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking

**Authors:** Ravi Ghadia, Maksim Abraham, Sergei Vorobyov, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21196v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21196v1)

**Summary:** Efficiently processing long sequences with Transformer models usually requires splitting the computations across accelerators via context parallelism. The dominant approaches in this family of methods, such as Ring Attention or DeepSpeed Ulysses, enable scaling over the context dimension but do not focus on memory efficiency, which limits the sequence lengths they can support. More advanced techniques, such as Fully Pipelined Distributed Transformer or activation offloading, can further extend t...

---

### 6. Statistical Query Lower Bounds for Smoothed Agnostic Learning

**Authors:** Ilias Diakonikolas, Daniel M. Kane

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21191v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21191v1)

**Summary:** We study the complexity of smoothed agnostic learning, recently introduced by~\cite{CKKMS24}, in which the learner competes with the best classifier in a target class under slight Gaussian perturbations of the inputs. Specifically, we focus on the prototypical task of agnostically learning halfspaces under subgaussian distributions in the smoothed model. The best known upper bound for this problem relies on $L_1$-polynomial regression and has complexity $d^{\tilde{O}(1/σ^2) \log(1/ε)}$, where $σ...

---

### 7. Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training

**Authors:** Anas Barakat, Souradip Chakraborty, Khushbu Pahwa, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21189v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21189v1)

**Summary:** Pass@k is a widely used performance metric for verifiable large language model tasks, including mathematical reasoning, code generation, and short-answer reasoning. It defines success if any of $k$ independently sampled solutions passes a verifier. This multi-sample inference metric has motivated inference-aware fine-tuning methods that directly optimize pass@$k$. However, prior work reports a recurring trade-off: pass@k improves while pass@1 degrades under such methods. This trade-off is practi...

---

### 8. The Diffusion Duality, Chapter II: $Ψ$-Samplers and Efficient Curriculum

**Authors:** Justin Deschenaux, Caglar Gulcehre, Subham Sekhar Sahoo

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21185v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21185v1)

**Summary:** Uniform-state discrete diffusion models excel at few-step generation and guidance due to their ability to self-correct, making them preferred over autoregressive or Masked diffusion models in these settings. However, their sampling quality plateaus with ancestral samplers as the number of steps increases. We introduce a family of Predictor-Corrector (PC) samplers for discrete diffusion that generalize prior methods and apply to arbitrary noise processes. When paired with uniform-state diffusion,...

---

### 9. Sequential Counterfactual Inference for Temporal Clinical Data: Addressing the Time Traveler Dilemma

**Authors:** Jingya Cheng, Alaleh Azhir, Jiazi Tian, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21168v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21168v1)

**Summary:** Counterfactual inference enables clinicians to ask "what if" questions about patient outcomes, but standard methods assume feature independence and simultaneous modifiability -- assumptions violated by longitudinal clinical data. We introduce the Sequential Counterfactual Framework, which respects temporal dependencies in electronic health records by distinguishing immutable features (chronic diagnoses) from controllable features (lab values) and modeling how interventions propagate through time...

---

### 10. Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions

**Authors:** Mame Diarra Toure, David A. Stephens

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21160v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21160v1)

**Summary:** In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=σ_k^{2}/(2μ_k)$, with $μ_k{=}\mathbb{E}[p_k]$ and $σ_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the...

---

### 11. SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

**Authors:** Dengjia Zhang, Xiaoou Liu, Lu Cheng, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21158v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21158v1)

**Summary:** Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolv...

---

### 12. Scaling State-Space Models on Multiple GPUs with Tensor Parallelism

**Authors:** Anurag Dutt, Nimit Shah, Hazem Masarani, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21144v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21144v1)

**Summary:** Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often bounded by the memory capacity, bandwidth, and latency limits of a single GPU, making multi-GPU execution increasingly necessary. Although tensor parallelism (TP) is widely used to scale Transformer inference, applying it to selective SSM blocks is non-trivial because the SSM mixer couples large pro...

---

### 13. A Benchmark for Deep Information Synthesis

**Authors:** Debjit Paul, Daniel Murphy, Milan Gritta, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21143v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21143v1)

**Summary:** Large language model (LLM)-based agents are increasingly used to solve complex tasks involving tool use, such as web browsing, code execution, and data analysis. However, current evaluation benchmarks do not adequately assess their ability to solve real-world tasks that require synthesizing information from multiple sources and inferring insights beyond simple fact retrieval. To address this, we introduce DEEPSYNTH, a novel benchmark designed to evaluate agents on realistic, time-consuming probl...

---

### 14. LUMEN: Longitudinal Multi-Modal Radiology Model for Prognosis and Diagnosis

**Authors:** Zhifan Jiang, Dong Yang, Vishwesh Nath, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21142v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21142v1)

**Summary:** Large vision-language models (VLMs) have evolved from general-purpose applications to specialized use cases such as in the clinical domain, demonstrating potential for decision support in radiology. One promising application is assisting radiologists in decision-making by the analysis of radiology imaging data such as chest X-rays (CXR) via a visual and natural language question-answering (VQA) interface. When longitudinal imaging is available, radiologists analyze temporal changes, which are es...

---

### 15. Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank

**Authors:** Kimon Fountoulakis, David Martínez-Rubio

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21138v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21138v1)

**Summary:** We study the degree-weighted work required to compute $\ell_1$-regularized PageRank using the standard one-gradient-per-iteration accelerated proximal-gradient method (FISTA). For non-accelerated local methods, the best known worst-case work scales as $\widetilde{O} ((αρ)^{-1})$, where $α$ is the teleportation parameter and $ρ$ is the $\ell_1$-regularization parameter. A natural question is whether FISTA can improve the dependence on $α$ from $1/α$ to $1/\sqrtα$ while preserving the $1/ρ$ locali...

---

### 16. SOM-VQ: Topology-Aware Tokenization for Interactive Generative Models

**Authors:** Alessandro Londei, Denise Lanzieri, Matteo Benati

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21133v1)

**Summary:** Vector-quantized representations enable powerful discrete generative models but lack semantic structure in token space, limiting interpretable human control. We introduce SOM-VQ, a tokenization method that combines vector quantization with Self-Organizing Maps to learn discrete codebooks with explicit low-dimensional topology. Unlike standard VQ-VAE, SOM-VQ uses topology-aware updates that preserve neighborhood structure: nearby tokens on a learned grid correspond to semantically similar states,...

---

### 17. An Enhanced Projection Pursuit Tree Classifier with Visual Methods for Assessing Algorithmic Improvements

**Authors:** Natalia da Silva, Dianne Cook, Eun-Kyung Lee

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21130v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21130v1)

**Summary:** This paper presents enhancements to the projection pursuit tree classifier and visual diagnostic methods for assessing their impact in high dimensions. The original algorithm uses linear combinations of variables in a tree structure where depth is constrained to be less than the number of classes -- a limitation that proves too rigid for complex classification problems. Our extensions improve performance in multi-class settings with unequal variance-covariance structures and nonlinear class sepa...

---

### 18. Ski Rental with Distributional Predictions of Unknown Quality

**Authors:** Qiming Cui, Michael Dinitz

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21104v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21104v1)

**Summary:** We revisit the central online problem of ski rental in the "algorithms with predictions" framework from the point of view of distributional predictions. Ski rental was one of the first problems to be studied with predictions, where a natural prediction is simply the number of ski days. But it is both more natural and potentially more powerful to think of a prediction as a distribution p-hat over the ski days. If the true number of ski days is drawn from some true (but unknown) distribution p, th...

---

### 19. Probing Graph Neural Network Activation Patterns Through Graph Topology

**Authors:** Floriano Tori, Lorenzo Bini, Marco Sorbi, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21092v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21092v1)

**Summary:** Curvature notions on graphs provide a theoretical description of graph topology, highlighting bottlenecks and denser connected regions. Artifacts of the message passing paradigm in Graph Neural Networks, such as oversmoothing and oversquashing, have been attributed to these regions. However, it remains unclear how the topology of a graph interacts with the learned preferences of GNNs. Through Massive Activations, which correspond to extreme edge activation values in Graph Transformers, we probe ...

---

### 20. Scaling Vision Transformers: Evaluating DeepSpeed for Image-Centric Workloads

**Authors:** Huy Trinh, Rebecca Ma, Zeqi Yu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21081v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21081v1)

**Summary:** Vision Transformers (ViTs) have demonstrated remarkable potential in image processing tasks by utilizing self-attention mechanisms to capture global relationships within data. However, their scalability is hindered by significant computational and memory demands, especially for large-scale models with many parameters. This study aims to leverage DeepSpeed, a highly efficient distributed training framework that is commonly used for language models, to enhance the scalability and performance of Vi...

---

### 21. ProxyFL: A Proxy-Guided Framework for Federated Semi-Supervised Learning

**Authors:** Duowen Chen, Yan Wang

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21078v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21078v1)

**Summary:** Federated Semi-Supervised Learning (FSSL) aims to collaboratively train a global model across clients by leveraging partially-annotated local data in a privacy-preserving manner. In FSSL, data heterogeneity is a challenging issue, which exists both across clients and within clients. External heterogeneity refers to the data distribution discrepancy across different clients, while internal heterogeneity represents the mismatch between labeled and unlabeled data within clients. Most FSSL methods t...

---

### 22. Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning

**Authors:** Zhangjie Xia, Yu Yang, Pan Xu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21072v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21072v1)

**Summary:** Off-dynamics offline reinforcement learning (RL) aims to learn a policy for a target domain using limited target data and abundant source data collected under different transition dynamics. Existing methods typically address dynamics mismatch either globally over the state space or via pointwise data filtering; these approaches can miss localized cross-domain similarities or incur high computational cost. We propose Localized Dynamics-Aware Domain Adaptation (LoDADA), which exploits localized dy...

---

### 23. Motivation is Something You Need

**Authors:** Mehdi Acheli, Walid Gaaloul

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21064v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21064v1)

**Summary:** This work introduces a novel training paradigm that draws from affective neuroscience. Inspired by the interplay of emotions and cognition in the human brain and more specifically the SEEKING motivational state, we design a dual-model framework where a smaller base model is trained continuously, while a larger motivated model is activated intermittently during predefined "motivation conditions". The framework mimics the emotional state of high curiosity and anticipation of reward in which broade...

---

### 24. Position-Aware Sequential Attention for Accurate Next Item Recommendations

**Authors:** Timur Nabiev, Evgeny Frolov

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21052v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21052v1)

**Summary:** Sequential self-attention models usually rely on additive positional embeddings, which inject positional information into item representations at the input. In the absence of positional signals, the attention block is permutation-equivariant over sequence positions and thus has no intrinsic notion of temporal order beyond causal masking. We argue that additive positional embeddings make the attention mechanism only superficially sensitive to sequence order: positional information is entangled wi...

---

### 25. PIME: Prototype-based Interpretable MCTS-Enhanced Brain Network Analysis for Disorder Diagnosis

**Authors:** Kunyu Zhang, Yanwu Yang, Jing Zhang, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21046v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21046v1)

**Summary:** Recent deep learning methods for fMRI-based diagnosis have achieved promising accuracy by modeling functional connectivity networks. However, standard approaches often struggle with noisy interactions, and conventional post-hoc attribution methods may lack reliability, potentially highlighting dataset-specific artifacts. To address these challenges, we introduce PIME, an interpretable framework that bridges intrinsic interpretability with minimal-sufficient subgraph optimization by integrating p...

---

### 26. T1: One-to-One Channel-Head Binding for Multivariate Time-Series Imputation

**Authors:** Dongik Park, Hyunwoo Ryu, Suahn Bae, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21043v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21043v1)

**Summary:** Imputing missing values in multivariate time series remains challenging, especially under diverse missing patterns and heavy missingness. Existing methods suffer from suboptimal performance as corrupted temporal features hinder effective cross-variable information transfer, amplifying reconstruction errors. Robust imputation requires both extracting temporal patterns from sparse observations within each variable and selectively transferring information across variables--yet current approaches ex...

---

### 27. Is Multi-Distribution Learning as Easy as PAC Learning: Sharp Rates with Bounded Label Noise

**Authors:** Rafael Hanashiro, Abhishek Shetty, Patrick Jaillet

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21039v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21039v1)

**Summary:** Towards understanding the statistical complexity of learning from heterogeneous sources, we study the problem of multi-distribution learning. Given $k$ data sources, the goal is to output a classifier for each source by exploiting shared structure to reduce sample complexity. We focus on the bounded label noise setting to determine whether the fast $1/ε$ rates achievable in single-task learning extend to this regime with minimal dependence on $k$. Surprisingly, we show that this is not the case....

---

### 28. Empirically Calibrated Conditional Independence Tests

**Authors:** Milleno Pan, Antoine de Mathelin, Wesley Tansey

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21036v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21036v1)

**Summary:** Conditional independence tests (CIT) are widely used for causal discovery and feature selection. Even with false discovery rate (FDR) control procedures, they often fail to provide frequentist guarantees in practice. We highlight two common failure modes: (i) in small samples, asymptotic guarantees for many CITs can be inaccurate and even correctly specified models fail to estimate the noise levels and control the error, and (ii) when sample sizes are large but models are misspecified, unaccount...

---

### 29. MIP Candy: A Modular PyTorch Framework for Medical Image Processing

**Authors:** Tianhao Fu, Yucheng Chen

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21033v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21033v1)

**Summary:** Medical image processing demands specialized software that handles high-dimensional volumetric data, heterogeneous file formats, and domain-specific training procedures. Existing frameworks either provide low-level components that require substantial integration effort or impose rigid, monolithic pipelines that resist modification. We present MIP Candy (MIPCandy), a freely available, PyTorch-based framework designed specifically for medical image processing. MIPCandy provides a complete, modular...

---

### 30. Matching Multiple Experts: On the Exploitability of Multi-Agent Imitation Learning

**Authors:** Antoine Bergerault, Volkan Cevher, Negar Mehr

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21020v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21020v1)

**Summary:** Multi-agent imitation learning (MA-IL) aims to learn optimal policies from expert demonstrations of interactions in multi-agent interactive domains. Despite existing guarantees on the performance of the resulting learned policies, characterizations of how far the learned polices are from a Nash equilibrium are missing for offline MA-IL. In this paper, we demonstrate impossibility and hardness results of learning low-exploitable policies in general $n$-player Markov Games. We do so by providing e...

---

### 31. Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures

**Authors:** Yubin Ge, Yongsong Huang, Xiaofeng Liu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20994v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20994v1)

**Summary:** Report-supervised (RSuper) learning seeks to alleviate the need for dense tumor voxel labels with constraints derived from radiology reports (e.g., volumes, counts, sizes, locations). In MRI studies of brain tumors, however, we often involve multi-parametric scans and substructures. Here, fine-grained modality/parameter-wise reports are usually provided along with global findings and are correlated with different substructures. Moreover, the reports often describe only the largest lesion and pro...

---

### 32. MAST: A Multi-fidelity Augmented Surrogate model via Spatial Trust-weighting

**Authors:** Ahmed Mohamed Eisa Nasr, Haris Moazam Sheikh

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20974v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20974v1)

**Summary:** In engineering design and scientific computing, computational cost and predictive accuracy are intrinsically coupled. High-fidelity simulations provide accurate predictions but at substantial computational costs, while lower-fidelity approximations offer efficiency at the expense of accuracy. Multi-fidelity surrogate modelling addresses this trade-off by combining abundant low-fidelity data with sparse high-fidelity observations. However, existing methods suffer from expensive training cost or r...

---

### 33. Does Order Matter : Connecting The Law of Robustness to Robust Generalization

**Authors:** Himadri Mandal, Vishnu Varadarajan, Jaee Ponde, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20971v1)

**Summary:** Bubeck and Sellke (2021) pose as an open problem the connection between the law of robustness and robust generalization. The law of robustness states that overparameterization is necessary for models to interpolate robustly; in particular, robust interpolation requires the learned function to be Lipschitz. Robust generalization asks whether small robust training loss implies small robust test loss. We resolve this problem by explicitly connecting the two for arbitrary data distributions. Specifi...

---

### 34. Estimation of Confidence Bounds in Binary Classification using Wilson Score Kernel Density Estimation

**Authors:** Thorbjørn Mosekjær Iversen, Zebin Duan, Frederik Hagelskjær

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20947v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20947v1)

**Summary:** The performance and ease of use of deep learning-based binary classifiers have improved significantly in recent years. This has opened up the potential for automating critical inspection tasks, which have traditionally only been trusted to be done manually. However, the application of binary classifiers in critical operations depends on the estimation of reliable confidence bounds such that system performance can be ensured up to a given statistical significance. We present Wilson Score Kernel D...

---

### 35. Some Simple Economics of AGI

**Authors:** Christian Catalini, Xiang Hui, Jane Wu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20946v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20946v1)

**Summary:** For millennia, human cognition was the primary engine of progress on Earth. As AI decouples cognition from biology, the marginal cost of measurable execution falls to zero, absorbing any labor capturable by metrics--including creative, analytical, and innovative work. The binding constraint on growth is no longer intelligence but human verification bandwidth: the capacity to validate, audit, and underwrite responsibility when execution is abundant. We model the AGI transition as the collision of...

---

### 36. Extending $μ$P: Spectral Conditions for Feature Learning Across Optimizers

**Authors:** Akshita Gupta, Marieme Ngom, Sam Foreman, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20937v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20937v1)

**Summary:** Several variations of adaptive first-order and second-order optimization methods have been proposed to accelerate and scale the training of large language models. The performance of these optimization routines is highly sensitive to the choice of hyperparameters (HPs), which are computationally expensive to tune for large-scale models. Maximal update parameterization $(μ$P$)$ is a set of scaling rules which aims to make the optimal HPs independent of the model size, thereby allowing the HPs tune...

---

### 37. Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels

**Authors:** Anupam Sharma, Harish Katti, Prajwal Singh, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20932v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20932v1)

**Summary:** An electroencephalogram (EEG) records the spatially averaged electrical activity of neurons in the brain, measured from the human scalp. Prior studies have explored EEG-based classification of objects or concepts, often for passive viewing of briefly presented image or video stimuli, with limited classes. Because EEG exhibits a low signal-to-noise ratio, recognizing fine-grained representations across a large number of classes remains challenging; however, abstract-level object representations m...

---

### 38. On the Generalization Behavior of Deep Residual Networks From a Dynamical System Perspective

**Authors:** Jinshu Huang, Mingfei Sun, Chunlin Wu

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20921v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20921v1)

**Summary:** Deep neural networks (DNNs) have significantly advanced machine learning, with model depth playing a central role in their successes. The dynamical system modeling approach has recently emerged as a powerful framework, offering new mathematical insights into the structure and learning behavior of DNNs. In this work, we establish generalization error bounds for both discrete- and continuous-time residual networks (ResNets) by combining Rademacher complexity, flow maps of dynamical systems, and th...

---

### 39. From Isolation to Integration: Building an Adaptive Expert Forest for Pre-Trained Model-based Class-Incremental Learning

**Authors:** Ruiqi Liu, Boyu Diao, Hangda Liu, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20911v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20911v1)

**Summary:** Class-Incremental Learning (CIL) requires models to learn new classes without forgetting old ones. A common method is to freeze a pre-trained model and train a new, lightweight adapter for each task. While this prevents forgetting, it treats the learned knowledge as a simple, unstructured collection and fails to use the relationships between tasks. To this end, we propose the Semantic-guided Adaptive Expert Forest (SAEF), a new method that organizes adapters into a structured hierarchy for bette...

---

### 40. Transcoder Adapters for Reasoning-Model Diffing

**Authors:** Nathan Hu, Jake Ward, Thomas Icard, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20904v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20904v1)

**Summary:** While reasoning models are increasingly ubiquitous, the effects of reasoning training on a model's internal mechanisms remain poorly understood. In this work, we introduce transcoder adapters, a technique for learning an interpretable approximation of the difference in MLP computation before and after fine-tuning. We apply transcoder adapters to characterize the differences between Qwen2.5-Math-7B and its reasoning-distilled variant, DeepSeek-R1-Distill-Qwen-7B. Learned adapters are faithful to ...

---

### 41. SpatiaLQA: A Benchmark for Evaluating Spatial Logical Reasoning in Vision-Language Models

**Authors:** Yuechen Xie, Xiaoyan Zhang, Yicheng Shan, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20901v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20901v1)

**Summary:** Vision-Language Models (VLMs) have been increasingly applied in real-world scenarios due to their outstanding understanding and reasoning capabilities. Although VLMs have already demonstrated impressive capabilities in common visual question answering and logical reasoning, they still lack the ability to make reasonable decisions in complex real-world environments. We define this ability as spatial logical reasoning, which not only requires understanding the spatial relationships among objects i...

---

### 42. Functional Continuous Decomposition

**Authors:** Teymur Aghayev

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20857v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20857v1)

**Summary:** The analysis of non-stationary time-series data requires insight into its local and global patterns with physical interpretability. However, traditional smoothing algorithms, such as B-splines, Savitzky-Golay filtering, and Empirical Mode Decomposition (EMD), lack the ability to perform parametric optimization with guaranteed continuity. In this paper, we propose Functional Continuous Decomposition (FCD), a JAX-accelerated framework that performs parametric, continuous optimization on a wide ran...

---

### 43. DRESS: A Continuous Framework for Structural Graph Refinement

**Authors:** Eduar Castrillo Velilla

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20833v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20833v1)

**Summary:** The Weisfeiler-Lehman (WL) hierarchy is a cornerstone framework for graph isomorphism testing and structural analysis. However, scaling beyond 1-WL to 3-WL and higher requires tensor-based operations that scale as O(n^3) or O(n^4), making them computationally prohibitive for large graphs. In this paper, we start from the Original-DRESS equation (Castrillo, Leon, and Gomez, 2018)--a parameter-free, continuous dynamical system on edges--and show that it distinguishes the prism graph from K_{3,3}, ...

---

### 44. Don't Ignore the Tail: Decoupling top-K Probabilities for Efficient Language Model Distillation

**Authors:** Sayantan Dasgupta, Trevor Cohn, Timothy Baldwin

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20816v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20816v1)

**Summary:** The core learning signal used in language model distillation is the standard Kullback-Leibler (KL) divergence between the student and teacher distributions. Traditional KL divergence tends to be dominated by the next tokens with the highest probabilities, i.e., the teacher's modes, thereby diminishing the influence of less probable yet potentially informative components of the output distribution. We propose a new tail-aware divergence that decouples the contribution of the teacher model's top-K...

---

### 45. Regret-Guided Search Control for Efficient Learning in AlphaZero

**Authors:** Yun-Jui Tsai, Wei-Yu Chen, Yan-Ru Ju, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20809v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20809v1)

**Summary:** Reinforcement learning (RL) agents achieve remarkable performance but remain far less learning-efficient than humans. While RL agents require extensive self-play games to extract useful signals, humans often need only a few games, improving rapidly by repeatedly revisiting states where mistakes occurred. This idea, known as search control, aims to restart from valuable states rather than always from the initial state. In AlphaZero, prior work Go-Exploit applies this idea by sampling past states ...

---

### 46. Assessing the Impact of Speaker Identity in Speech Spoofing Detection

**Authors:** Anh-Tuan Dao, Driss Matrouf, Nicholas Evans

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20805v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20805v1)

**Summary:** Spoofing detection systems are typically trained using diverse recordings from multiple speakers, often assuming that the resulting embeddings are independent of speaker identity. However, this assumption remains unverified. In this paper, we investigate the impact of speaker information on spoofing detection systems. We propose two approaches within our Speaker-Invariant Multi-Task framework, one that models speaker identity within the embeddings and another that removes it. SInMT integrates mu...

---

### 47. Probing Dec-POMDP Reasoning in Cooperative MARL

**Authors:** Kale-ab Tessera, Leonard Hinckeldey, Riccardo Zamboni, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20804v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20804v1)

**Summary:** Cooperative multi-agent reinforcement learning (MARL) is typically framed as a decentralised partially observable Markov decision process (Dec-POMDP), a setting whose hardness stems from two key challenges: partial observability and decentralised coordination. Genuinely solving such tasks requires Dec-POMDP reasoning, where agents use history to infer hidden states and coordinate based on local information. Yet it remains unclear whether popular benchmarks actually demand this reasoning or permi...

---

### 48. Exploring the Impact of Parameter Update Magnitude on Forgetting and Generalization of Continual Learning

**Authors:** JinLi He, Liang Bai, Xian Yang

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20796v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20796v1)

**Summary:** The magnitude of parameter updates are considered a key factor in continual learning. However, most existing studies focus on designing diverse update strategies, while a theoretical understanding of the underlying mechanisms remains limited. Therefore, we characterize model's forgetting from the perspective of parameter update magnitude and formalize it as knowledge degradation induced by task-specific drift in the parameter space, which has not been fully captured in previous studies due to th...

---

### 49. Understanding the Role of Rehearsal Scale in Continual Learning under Varying Model Capacities

**Authors:** JinLi He, Liang Bai, Xian Yang

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20791v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20791v1)

**Summary:** Rehearsal is one of the key techniques for mitigating catastrophic forgetting and has been widely adopted in continual learning algorithms due to its simplicity and practicality. However, the theoretical understanding of how rehearsal scale influences learning dynamics remains limited. To address this gap, we formulate rehearsal-based continual learning as a multidimensional effectiveness-driven iterative optimization problem, providing a unified characterization across diverse performance metri...

---

### 50. On Electric Vehicle Energy Demand Forecasting and the Effect of Federated Learning

**Authors:** Andreas Tritsarolis, Gil Sampaio, Nikos Pelekis, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20782v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20782v1)

**Summary:** The wide spread of new energy resources, smart devices, and demand side management strategies has motivated several analytics operations, from infrastructure load modeling to user behavior profiling. Energy Demand Forecasting (EDF) of Electric Vehicle Supply Equipments (EVSEs) is one of the most critical operations for ensuring efficient energy management and sustainability, since it enables utility providers to anticipate energy/power demand, optimize resource allocation, and implement proactiv...

---

## cs.NE

**50 papers**

### 1. Body-Reservoir Governance in Repeated Games: Embodied Decision-Making, Dynamic Sentinel Adaptation, and Complexity-Regularized Optimization

**Authors:** Yuki Nakamura

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20846v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20846v1)

**Summary:** Standard game theory explains cooperation in repeated games through conditional strategies such as Tit-for-Tat (TfT), but these require continuous computation that imposes physical costs on embodied agents. We propose a three-layer Body-Reservoir Governance (BRG) architecture: (1) a body reservoir (echo state network) whose $d$-dimensional state performs implicit inference over interaction history, serving as both decision-maker and anomaly detector, (2) a cognitive filter providing costly strat...

---

### 2. AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization

**Authors:** Mert Cemri, Shubham Agrawal, Akshat Gupta, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20133v1)

**Summary:** The paradigm of automated program generation is shifting from one-shot generation to inference-time search, where Large Language Models (LLMs) function as semantic mutation operators within evolutionary loops. While effective, these systems are currently governed by static schedules that fail to account for the non-stationary dynamics of the search process. This rigidity results in substantial computational waste, as resources are indiscriminately allocated to stagnating populations while promis...

---

### 3. Linear Reservoir: A Diagonalization-Based Optimization

**Authors:** Romain de Coudenhove, Yannis Bendi-Ouis, Anthony Strock, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19802v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19802v1)

**Summary:** We introduce a diagonalization-based optimization for Linear Echo State Networks (ESNs) that reduces the per-step computational complexity of reservoir state updates from O(N^2) to O(N). By reformulating reservoir dynamics in the eigenbasis of the recurrent matrix, the recurrent update becomes a set of independent element-wise operations, eliminating the matrix multiplication. We further propose three methods to use our optimization depending on the situation: (i) Eigenbasis Weight Transformatio...

---

### 4. Unsupervised Anomaly Detection in NSL-KDD Using $β$-VAE: A Latent Space and Reconstruction Error Approach

**Authors:** Dylan Baptiste, Ramla Saddem, Alexandre Philippot, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19785v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19785v1)

**Summary:** As Operational Technology increasingly integrates with Information Technology, the need for Intrusion Detection Systems becomes more important. This paper explores an unsupervised approach to anomaly detection in network traffic using $β$-Variational Autoencoders on the NSL-KDD dataset. We investigate two methods: leveraging the latent space structure by measuring distances from test samples to the training data projections, and using the reconstruction error as a conventional anomaly detection ...

---

### 5. Partial Soft-Matching Distance for Neural Representational Comparison with Partial Unit Correspondence

**Authors:** Chaitanya Kapoor, Alex H. Williams, Meenakshi Khosla

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19331v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19331v1)

**Summary:** Representational similarity metrics typically force all units to be matched, making them susceptible to noise and outliers common in neural representations. We extend the soft-matching distance to a partial optimal transport setting that allows some neurons to remain unmatched, yielding rotation-sensitive but robust correspondences. This partial soft-matching distance provides theoretical advantages -- relaxing strict mass conservation while maintaining interpretable transport costs -- and pract...

---

### 6. CORVET: A CORDIC-Powered, Resource-Frugal Mixed-Precision Vector Processing Engine for High-Throughput AIoT applications

**Authors:** Sonu Kumar, Mohd Faisal Khan, Mukul Lokhande, et al.

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19268v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19268v1)

**Summary:** This brief presents a runtime-adaptive, performance-enhanced vector engine featuring a low-resource, iterative CORDIC-based MAC unit for edge AI acceleration. The proposed design enables dynamic reconfiguration between approximate and accurate modes, exploiting the latency-accuracy trade-off for a wide range of workloads. Its resource-efficient approach further enables up to 4x throughput improvement within the same hardware resources by leveraging vectorised, time-multiplexed execution and flex...

---

### 7. DGPO: RL-Steered Graph Diffusion for Neural Architecture Generation

**Authors:** Aleksei Liuliakov, Luca Hermes, Barbara Hammer

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19261v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19261v1)

**Summary:** Reinforcement learning fine-tuning has proven effective for steering generative diffusion models toward desired properties in image and molecular domains. Graph diffusion models have similarly been applied to combinatorial structure generation, including neural architecture search (NAS). However, neural architectures are directed acyclic graphs (DAGs) where edge direction encodes functional semantics such as data flow-information that existing graph diffusion methods, designed for undirected str...

---

### 8. Alternating Bi-Objective Optimization for Explainable Neuro-Fuzzy Systems

**Authors:** Qusai Khaled, Uzay Kaymak, Laura Genga

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19253v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19253v1)

**Summary:** Fuzzy systems show strong potential in explainable AI due to their rule-based architecture and linguistic variables. Existing approaches navigate the accuracy-explainability trade-off either through evolutionary multi-objective optimization (MOO), which is computationally expensive, or gradient-based scalarization, which cannot recover non-convex Pareto regions. We propose X-ANFIS, an alternating bi-objective gradient-based optimization scheme for explainable adaptive neuro-fuzzy inference syste...

---

### 9. All Constant Mutation Rates for the $(1+1)$ Evolutionary Algorithm

**Authors:** Andrew James Kelley

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.18989v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18989v1)

**Summary:** For every mutation rate $p \in (0, 1)$, and for all $\varepsilon > 0$, there is a fitness function $f : \{0,1\}^n \to \mathbb{R}$ with a unique maximum for which the optimal mutation rate for the $(1+1)$ evolutionary algorithm on $f$ is in $(p-\varepsilon, p+\varepsilon)$. In other words, the set of optimal mutation rates for the $(1+1)$ EA is dense in the interval $[0, 1]$. To show that, this paper introduces DistantSteppingStones, a fitness function which consists of large plateaus separated b...

---

### 10. Modularity is the Bedrock of Natural and Artificial Intelligence

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18960v1)

**Summary:** The remarkable performance of modern AI systems has been driven by unprecedented scales of data, computation, and energy -- far exceeding the resources required by human intelligence. This disparity highlights the need for new guiding principles and motivates drawing inspiration from the fundamental organizational principles of brain computation. Among these principles, modularity has been shown to be critical for supporting the efficient learning and strong generalization abilities consistently...

---

### 11. Toward Manifest Relationality in Transformers via Symmetry Reduction

**Authors:** J. François, L. Ravera

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18948v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18948v1)

**Summary:** Transformer models contain substantial internal redundancy arising from coordinate-dependent representations and continuous symmetries, in model space and in head space, respectively. While recent approaches address this by explicitly breaking symmetry, we propose a complementary framework based on symmetry reduction. We reformulate representations, attention mechanisms, and optimization dynamics in terms of invariant relational quantities, eliminating redundant degrees of freedom by constructio...

---

### 12. Robustness of Deep ReLU Networks to Misclassification of High-Dimensional Data

**Authors:** Věra Kůrková

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18674v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18674v1)

**Summary:** We present a theoretical study of the robustness of parameterized networks to random input perturbations. Specifically, we analyze local robustness at a given network input by quantifying the probability that a small additive random perturbation of the input leads to misclassification. For deep networks with rectified linear units, we derive lower bounds on local robustness in terms of the input dimensionality and the total number of network units.

---

### 13. Musical Training, but not Mere Exposure to Music, Drives the Emergence of Chroma Equivalence in Artificial Neural Networks

**Authors:** Lukas Grasse, Matthew S. Tata

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18635v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18635v1)

**Summary:** Pitch is a fundamental aspect of auditory perception. Pitch perception is commonly described across two perceptual dimensions: pitch height is the sense that tones with varying frequencies seem to be higher or lower, and chroma equivalence is the cyclical similarity of notes octaves, corresponding to a doubling of fundamental frequency. Existing research is divided on whether chroma equivalence is a learned percept that varies according to musical experience and culture, or is an innate percept ...

---

### 14. Flexi-NeurA: A Configurable Neuromorphic Accelerator with Adaptive Bit-Precision Exploration for Edge SNNs

**Authors:** Mohammad Farahani, Mohammad Rasoul Roshanshah, Saeed Safari

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18140v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18140v1)

**Summary:** Neuromorphic accelerators promise unparalleled energy efficiency and computational density for spiking neural networks (SNNs), especially in edge intelligence applications. However, most existing platforms exhibit rigid architectures with limited configurability, restricting their adaptability to heterogeneous workloads and diverse design objectives. To address these limitations, we present Flexi-NeurA -- a parameterizable neuromorphic accelerator (core) that unifies configurability, flexibility...

---

### 15. PINEAPPLE: Physics-Informed Neuro-Evolution Algorithm for Prognostic Parameter Inference in Lithium-Ion Battery Electrodes

**Authors:** Karkulali Pugalenthi, Jian Cheng Wong, Qizheng Yang, et al.

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18042v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18042v1)

**Summary:** Accurate, real-time, yet non-destructive estimation of internal states in lithium-ion batteries is critical for predicting degradation, optimizing usage strategies, and extending operational lifespan. Here, we introduce PINEAPPLE (Physics-Informed Neuro-Evolution Algorithm for Prognostic Parameter inference in Lithium-ion battery Electrodes), a novel framework that integrates physics-informed neural networks (PINNs) with an evolutionary search algorithm to enable rapid, scalable, and interpretab...

---

### 16. Learning under noisy supervision is governed by a feedback-truth gap

**Authors:** Elan Schonfeld, Elias Wisnia

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16829v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16829v1)

**Summary:** When feedback is absorbed faster than task structure can be evaluated, the learner will favor feedback over truth. A two-timescale model shows this feedback-truth gap is inevitable whenever the two rates differ and vanishes only when they match. We test this prediction across neural networks trained with noisy labels (30 datasets, 2,700 runs), human probabilistic reversal learning (N = 292), and human reward/punishment learning with concurrent EEG (N = 25). In each system, truth is defined opera...

---

### 17. Parallelizable Neural Turing Machines

**Authors:** Gabriel Faria, Arnaldo Candido Junior

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.18508v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18508v1)

**Summary:** We introduce a parallelizable simplification of Neural Turing Machine (NTM), referred to as P-NTM, which redesigns the core operations of the original architecture to enable efficient scan-based parallel execution. We evaluate the proposed architecture on a synthetic benchmark of algorithmic problems involving state tracking, memorization, and basic arithmetic, solved via autoregressive decoding. We compare it against a revisited stable implementation of the standard NTM, as well as conventional...

---

### 18. Fine-Pruning: A Biologically Inspired Algorithm for Personalization of Machine Learning Models

**Authors:** Joseph Bingham, Saman Zonouz, Dvir Aran

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18507v1)

**Summary:** Neural networks have long strived to emulate the learning capabilities of the human brain. While deep neural networks (DNNs) draw inspiration from the brain in neuron design, their training methods diverge from biological foundations. Backpropagation, the primary training method for DNNs, requires substantial computational resources and fully labeled datasets, presenting major bottlenecks in development and application. This work demonstrates that by returning to biomimicry, specifically mimicki...

---

### 19. End-user validation of BRIGHT with custom-developed graphical user interface applied to cervical cancer brachytherapy

**Authors:** Leah R. M. Dickhoff, Ellen M. Kerkhof, Heloisa H. Deuzeman, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16321v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16321v1)

**Summary:** Multi-objective optimisation using BRIGHT has proven insightful and effective in prostate cancer brachytherapy treatment planning. BRachytherapy via artificially Intelligent GOMEA-Heuristic based Treatment planning (BRIGHT) generates multiple treatment plans, each with a different trade-off between tumour coverage and organs-at-risk sparing. BRIGHT was recently extended to cervical cancer brachytherapy. In this study, we present a novel, custom-developed graphical user interface (GUI) that enabl...

---

### 20. Evolutionary Context Search for Automated Skill Acquisition

**Authors:** Qi Sun, Stefan Nielsen, Rio Yokota, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16113v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16113v1)

**Summary:** Large Language Models cannot reliably acquire new knowledge post-deployment -- even when relevant text resources exist, models fail to transform them into actionable knowledge without retraining. Retrieval-Augmented Generation attempts to bridge this gap by surfacing relevant documents at inference time, yet similarity-based retrieval often fails to identify context that actually improves task performance. We introduce Evolutionary Context Search (ECS), an evolutionary method that searches conte...

---

### 21. Heuristic Search as Language-Guided Program Optimization

**Authors:** Mingxin Yu, Ruixiao Yang, Chuchu Fan

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16038v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16038v1)

**Summary:** Large Language Models (LLMs) have advanced Automated Heuristic Design (AHD) in combinatorial optimization (CO) in the past few years. However, existing discovery pipelines often require extensive manual trial-and-error or reliance on domain expertise to adapt to new or complex problems. This stems from tightly coupled internal mechanisms that limit systematic improvement of the LLM-driven design process. To address this challenge, we propose a structured framework for LLM-driven AHD that explici...

---

### 22. B-DENSE: Branching For Dense Ensemble Network Learning

**Authors:** Cherish Puniani, Tushar Kumar, Arnav Bendre, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15971v1)

**Summary:** Inspired by non-equilibrium thermodynamics, diffusion models have achieved state-of-the-art performance in generative modeling. However, their iterative sampling nature results in high inference latency. While recent distillation techniques accelerate sampling, they discard intermediate trajectory steps. This sparse supervision leads to a loss of structural information and introduces significant discretization errors. To mitigate this, we propose B-DENSE, a novel framework that leverages multi-b...

---

### 23. Evolutionary Systems Thinking -- From Equilibrium Models to Open-Ended Adaptive Dynamics

**Authors:** Dan Adler

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15957v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15957v1)

**Summary:** Complex change is often described as "evolutionary" in economics, policy, and technology, yet most system dynamics models remain constrained to fixed state spaces and equilibrium-seeking behavior. This paper argues that evolutionary dynamics should be treated as a core system-thinking problem rather than as a biological metaphor. We introduce Stability-Driven Assembly (SDA) as a minimal, non-equilibrium framework in which stochastic interactions combined with differential persistence generate en...

---

### 24. CDRL: A Reinforcement Learning Framework Inspired by Cerebellar Circuits and Dendritic Computational Strategies

**Authors:** Sibo Zhang, Rui Jing, Liangfu Lv, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15367v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15367v1)

**Summary:** Reinforcement learning (RL) has achieved notable performance in high-dimensional sequential decision-making tasks, yet remains limited by low sample efficiency, sensitivity to noise, and weak generalization under partial observability. Most existing approaches address these issues primarily through optimization strategies, while the role of architectural priors in shaping representation learning and decision dynamics is less explored. Inspired by structural principles of the cerebellum, we propo...

---

### 25. Web-Scale Multimodal Summarization using CLIP-Based Semantic Alignment

**Authors:** Mounvik K, N Harshit

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14889v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14889v1)

**Summary:** We introduce Web-Scale Multimodal Summarization, a lightweight framework for generating summaries by combining retrieved text and image data from web sources. Given a user-defined topic, the system performs parallel web, news, and image searches. Retrieved images are ranked using a fine-tuned CLIP model to measure semantic alignment with topic and text. Optional BLIP captioning enables image-only summaries for stronger multimodal coherence.The pipeline supports features such as adjustable fetch ...

---

### 26. GOT-JEPA: Generic Object Tracking with Model Adaptation and Occlusion Handling using Joint-Embedding Predictive Architecture

**Authors:** Shih-Fang Chen, Jun-Cheng Chen, I-Hong Jhuo, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14771v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14771v1)

**Summary:** The human visual system tracks objects by integrating current observations with previously observed information, adapting to target and scene changes, and reasoning about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for training targets, which limits robustness and generalization in unseen scenarios, and their occlusion reasoning remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in generalization and oc...

---

### 27. Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts

**Authors:** Buze Zhang, Jinkai Tao, Zilang Zeng, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14490v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14490v1)

**Summary:** Large Language Models (LLMs) have achieved remarkable progress, with Parameter-Efficient Fine-Tuning (PEFT) emerging as a key technique for downstream task adaptation. However, existing PEFT methods mainly operate in Euclidean space, fundamentally limiting their capacity to capture complex geometric structures inherent in language data. While alternative geometric spaces, like hyperbolic geometries for hierarchical data and spherical manifolds for circular patterns, offer theoretical advantages,...

---

### 28. Revisiting the Platonic Representation Hypothesis: An Aristotelian View

**Authors:** Fabian Gröger, Shuo Wen, Maria Brbić

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14486v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14486v1)

**Summary:** The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are confounded by network scale: increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a...

---

### 29. Selective Synchronization Attention

**Authors:** Hasi Hays

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14445v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14445v1)

**Summary:** The Transformer architecture has become the foundation of modern deep learning, yet its core self-attention mechanism suffers from quadratic computational complexity and lacks grounding in biological neural computation. We propose Selective Synchronization Attention (SSA), a novel attention mechanism that replaces the standard dot-product self-attention with a closed-form operator derived from the steady-state solution of the Kuramoto model of coupled oscillators. In SSA, each token is represent...

---

### 30. Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces

**Authors:** William L. Tong, Ege Cakar, Cengiz Pehlevan

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14404v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14404v1)

**Summary:** Recent years have witnessed meteoric progress in reasoning models: neural networks that generate intermediate reasoning traces (RTs) before producing a final output. Despite the rapid advancement, our understanding of how RTs support reasoning, and the limits of this paradigm, remain incomplete. To promote greater clarity, we introduce PITA: a novel large-scale dataset of over 23 million statements in propositional logic and their corresponding proofs. As a benchmark for robust reasoning, we foc...

---

### 31. An effective Genetic Programming Hyper-Heuristic for Uncertain Agile Satellite Scheduling

**Authors:** Yuning Chen, Junhua Xue, Wangqi Gu, et al.

**Published:** 2026-02-15

🔗 [Paper](http://arxiv.org/abs/2602.15070v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15070v1)

**Summary:** This paper investigates a novel problem, namely the Uncertain Agile Earth Observation Satellite Scheduling Problem (UAEOSSP). Unlike the static AEOSSP, it takes into account a range of uncertain factors (e.g., task profit, resource consumption, and task visibility) in order to reflect the reality that the actual information is inherently unknown beforehand. An effective Genetic Programming Hyper-Heuristic (GPHH) is designed to automate the generation of scheduling policies. The evolved schedulin...

---

### 32. Evolving Multi-Channel Confidence-Aware Activation Functions for Missing Data with Channel Propagation

**Authors:** Naeem Shahabi Sani, Ferial Najiantabriz, Shayan Shafaei, et al.

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13864v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13864v1)

**Summary:** Learning in the presence of missing data can result in biased predictions and poor generalizability, among other difficulties, which data imputation methods only partially address. In neural networks, activation functions significantly affect performance yet typical options (e.g., ReLU, Swish) operate only on feature values and do not account for missingness indicators or confidence scores. We propose Three-Channel Evolved Activations (3C-EA), which we evolve using Genetic Programming to produce...

---

### 33. A Unified Physics-Informed Neural Network for Modeling Coupled Electro- and Elastodynamic Wave Propagation Using Three-Stage Loss Optimization

**Authors:** Suhas Suresh Bharadwaj, Reuben Thomas Thovelil

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13811v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13811v1)

**Summary:** Physics-Informed Neural Networks present a novel approach in SciML that integrates physical laws in the form of partial differential equations directly into the NN through soft constraints in the loss function. This work studies the application of PINNs to solve a one dimensional coupled electro-elastodynamic system modeling linear piezoelectricity in stress-charge form, governed by elastodynamic and electrodynamic equations. Our simulation employs a feedforward architecture, mapping space-time ...

---

### 34. OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery

**Authors:** Qi Liu, Wanjing Ma

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13769v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13769v1)

**Summary:** Automating scientific discovery in complex, experiment-driven domains requires more than iterative mutation of programs; it demands structured hypothesis management, environment interaction, and principled reflection. We present OR-Agent, a configurable multi-agent research framework designed for automated exploration in rich experimental environments. OR-Agent organizes research as a structured tree-based workflow that explicitly models branching hypothesis generation and systematic backtrackin...

---

### 35. Discrete Gene Crossover Accelerates Solution Discovery in Quality-Diversity Algorithms

**Authors:** Joshua Hutchinson, J. Michael Herrmann, Simón C. Smith

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13730v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13730v1)

**Summary:** Quality-Diversity (QD) algorithms aim to discover diverse, high-performing solutions across behavioral niches. However, QD search often stagnates as incremental variation operators struggle to propagate building blocks across large populations. Existing mutation operators rely on gradual variation to solutions, limiting their ability to efficiently explore regions of the search space distant from parent solutions or to spread beneficial genetic material through the population. We propose a mutat...

---

### 36. Fast Surrogate Learning for Multi-Objective UAV Placement in Motorway Intelligent Transportation System

**Authors:** Weian Guo, Shixin Deng, Wuzhao Li, et al.

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13564v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13564v1)

**Summary:** We address multi-objective unmanned aerial vehicle (UAV) placement for motorway intelligent transportation systems, where deployments must balance coverage, link quality, and UAV count under geometric constraints. We construct a reproducible benchmark from highD motorway recordings with recording-level splits and generate Pareto-optimal labels via NSGA-II. A preference rule yields deployable targets while preserving multi-objective evaluation. We train fast surrogate models that map unordered ve...

---

### 37. Evolutionary design of thermodynamic logic gates and their heat emission

**Authors:** Stephen Whitelam

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13410v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13410v1)

**Summary:** Landauer's principle bounds the heat generated by logical operations, but in practice the thermodynamic cost of computation is dominated by the control systems that implement logic. CMOS gates dissipate energy far above the Landauer bound, while laboratory demonstrations of near-Landauer erasure rely on external measurement or feedback systems whose energy costs exceed that of the logic operation by many orders of magnitude. Here we use simulations to show that a genetic algorithm can program a ...

---

### 38. Learning to Approximate Uniform Facility Location via Graph Neural Networks

**Authors:** Chendi Qian, Christopher Morris, Stefanie Jegelka, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13155v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13155v1)

**Summary:** There has been a growing interest in using neural networks, especially message-passing neural networks (MPNNs), to solve hard combinatorial optimization problems heuristically. However, existing learning-based approaches for hard combinatorial optimization tasks often rely on supervised training data, reinforcement learning, or gradient estimators, leading to significant computational overhead, unstable training, or a lack of provable performance guarantees. In contrast, classical approximation ...

---

### 39. Which Algorithms Can Graph Neural Networks Learn?

**Authors:** Solveig Wittig, Antonis Vasileiou, Robert R. Nerem, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13106v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13106v1)

**Summary:** In recent years, there has been growing interest in understanding neural architectures' ability to learn to execute discrete algorithms, a line of work often referred to as neural algorithmic reasoning. The goal is to integrate algorithmic reasoning capabilities into larger neural pipelines. Many such architectures are based on (message-passing) graph neural networks (MPNNs), owing to their permutation equivariance and ability to deal with sparsity and variable-sized inputs. However, existing wo...

---

### 40. Synaptic Activation and Dual Liquid Dynamics for Interpretable Bio-Inspired Models

**Authors:** Mónika Farsang, Radu Grosu

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13017v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13017v1)

**Summary:** In this paper, we present a unified framework for various bio-inspired models to better understand their structural and functional differences. We show that liquid-capacitance-extended models lead to interpretable behavior even in dense, all-to-all recurrent neural network (RNN) policies. We further demonstrate that incorporating chemical synapses improves interpretability and that combining chemical synapses with synaptic activation yields the most accurate and interpretable RNN models. To asse...

---

### 41. Machine Learning-Based Classification of Jhana Advanced Concentrative Absorption Meditation (ACAM-J) using 7T fMRI

**Authors:** Puneet Kumar, Winson F. Z. Yang, Alakhsimar Singh, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13008v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13008v1)

**Summary:** Jhana advanced concentration absorption meditation (ACAM-J) is related to profound changes in consciousness and cognitive processing, making the study of their neural correlates vital for insights into consciousness and well-being. This study evaluates whether functional MRI-derived regional homogeneity (ReHo) can be used to classify ACAM-J using machine-learning approaches. We collected group-level fMRI data from 20 advanced meditators to train the classifiers, and intensive single-case data fr...

---

### 42. EPRBench: A High-Quality Benchmark Dataset for Event Stream Based Visual Place Recognition

**Authors:** Xiao Wang, Xingxing Xiong, Jinfeng Gao, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12919v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12919v1)

**Summary:** Event stream-based Visual Place Recognition (VPR) is an emerging research direction that offers a compelling solution to the instability of conventional visible-light cameras under challenging conditions such as low illumination, overexposure, and high-speed motion. Recognizing the current scarcity of dedicated datasets in this domain, we introduce EPRBench, a high-quality benchmark specifically designed for event stream-based VPR. EPRBench comprises 10K event sequences and 65K event frames, col...

---

### 43. Reverse Delegated Training and Private Inference via Perfectly-Secure Quantum Homomorphic Encryption

**Authors:** Sergio A. Ortega, Miguel A. Martin-Delgado

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12712v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12712v1)

**Summary:** Quantum machine learning in cloud environments requires protecting sensitive data while enabling remote computation. Here we demonstrate the first realistic implementations of a perfectly-secure quantum homomorphic encryption (QHE) scheme applied to quantum neural networks (QNN). Using efficient Clifford+$T$ decomposition, we implement quantum convolutional neural networks for two complementary scenarios: (i) reverse delegated training, where encrypted data from multiple providers trains a user'...

---

### 44. Enhancing Heat Sink Efficiency in MOSFETs using Physics Informed Neural Networks: A Systematic Study on Coolant Velocity Estimation

**Authors:** Aniruddha Bora, Isabel K. Alvarez, Julie Chalfant, et al.

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.20177v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20177v1)

**Summary:** In this work, we present a methodology using Physics Informed Neural Networks (PINNs) to determine the required velocity of a coolant, given inlet and outlet temperatures for a given heat flux in a multilayered metal-oxide-semiconductor field-effect transistor (MOSFET). MOSFETs are integral components of Power Electronic Building Blocks (PEBBs) and experiences the majority of the thermal load. Effective cooling of MOSFETs is therefore essential to prevent overheating and potential burnout. Deter...

---

### 45. Energy-Aware Spike Budgeting for Continual Learning in Spiking Neural Networks for Neuromorphic Vision

**Authors:** Anika Tabassum Meem, Muntasir Hossain Nadid, Md Zesun Ahmed Mia

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.12236v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12236v1)

**Summary:** Neuromorphic vision systems based on spiking neural networks (SNNs) offer ultra-low-power perception for event-based and frame-based cameras, yet catastrophic forgetting remains a critical barrier to deployment in continually evolving environments. Existing continual learning methods, developed primarily for artificial neural networks, seldom jointly optimize accuracy and energy efficiency, with particularly limited exploration on event-based datasets. We propose an energy-aware spike budgeting ...

---

### 46. CL API: Real-Time Closed-Loop Interactions with Biological Neural Networks

**Authors:** David Hogan, Andrew Doherty, Boon Kien Khoo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11632v1)

**Summary:** Biological neural networks (BNNs) are increasingly explored for their rich dynamics, parallelism, and adaptive behavior. Beyond understanding their function as a scientific endeavour, a key focus has been using these biological systems as a novel computing substrate. However, BNNs can only function as reliable information-processing systems if inputs are delivered in a temporally and structurally consistent manner. In practice, this requires stimulation with precisely controlled structure, micro...

---

### 47. Evolution With Purpose: Hierarchy-Informed Optimization of Whole-Brain Models

**Authors:** Hormoz Shahrzad, Niharika Gajawelli, Kaitlin Maile, et al.

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11398v2) | 📄 [PDF](https://arxiv.org/pdf/2602.11398v2)

**Summary:** Evolutionary search is well suited for large-scale biophysical brain modeling, where many parameters with nonlinear interactions and no tractable gradients need to be optimized. Standard evolutionary approaches achieve an excellent fit to MRI data; however, among many possible such solutions, it finds ones that overfit to individual subjects and provide limited predictive power. This paper investigates whether guiding evolution with biological knowledge can help. Focusing on whole-brain Dynamic ...

---

### 48. Predictive Associative Memory: Retrieval Beyond Similarity Through Temporal Co-occurrence

**Authors:** Jason Dury

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11322v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11322v1)

**Summary:** Current approaches to memory in neural systems rely on similarity-based retrieval: given a query, find the most representationally similar stored state. This assumption -- that useful memories are similar memories -- fails to capture a fundamental property of biological memory: association through temporal co-occurrence. We propose Predictive Associative Memory (PAM), an architecture in which a JEPA-style predictor, trained on temporal co-occurrence within a continuous experience stream, learns ...

---

### 49. Interactive LLM-assisted Curriculum Learning for Multi-Task Evolutionary Policy Search

**Authors:** Berfin Sakallioglu, Giorgia Nadizar, Eric Medvet

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.10891v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10891v1)

**Summary:** Multi-task policy search is a challenging problem because policies are required to generalize beyond training cases. Curriculum learning has proven to be effective in this setting, as it introduces complexity progressively. However, designing effective curricula is labor-intensive and requires extensive domain expertise. LLM-based curriculum generation has only recently emerged as a potential solution, but was limited to operate in static, offline modes without leveraging real-time feedback from...

---

### 50. Amortized Inference of Neuron Parameters on Analog Neuromorphic Hardware

**Authors:** Jakob Kaiser, Eric Müller, Johannes Schemmel

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.10763v2) | 📄 [PDF](https://arxiv.org/pdf/2602.10763v2)

**Summary:** Our work utilized a non-sequential simulation-based inference algorithm to provide an amortized neural density estimator, which approximates the posterior distribution for seven parameters of the adaptive exponential integrate-and-fire neuron model of the analog neuromorphic BrainScaleS-2 substrate. We constrained the large parameter space by training a binary classifier to predict parameter combinations yielding observations in regimes of interest, i.e. moderate spike counts. We compared two ne...

---

## q-bio.NC

**50 papers**

### 1. CRCC: Contrast-Based Robust Cross-Subject and Cross-Site Representation Learning for EEG

**Authors:** Xiaobin Wong, Zhonghua Zhao, Haoran Guo, et al.

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19138v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19138v1)

**Summary:** EEG-based neural decoding models often fail to generalize across acquisition sites due to structured, site-dependent biases implicitly exploited during training. We reformulate cross-site clinical EEG learning as a bias-factorized generalization problem, in which domain shifts arise from multiple interacting sources. We identify three fundamental bias factors and propose a general training framework that mitigates their influence through data standardization and representation-level constraints....

---

### 2. Critical Scaling and Metabolic Regulation in a Ginzburg--Landau Theory of Cognitive Dynamics

**Authors:** Gunn Kim

**Published:** 2026-02-22

🔗 [Paper](http://arxiv.org/abs/2602.19023v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19023v1)

**Summary:** We formulate a phenomenological effective field theory in which biological intelligence emerges as a macroscopic order parameter sustained by continuous metabolic flux. By modeling cognition as a coarse-grained neural activity field governed by a variational free energy, we derive closed-form expressions for information capacity and structural susceptibility using a Gaussian maximum entropy approximation. The theory predicts a universal algebraic divergence of the susceptibility, $χ\sim K^{-3/2}...

---

### 3. Modularity is the Bedrock of Natural and Artificial Intelligence

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18960v1)

**Summary:** The remarkable performance of modern AI systems has been driven by unprecedented scales of data, computation, and energy -- far exceeding the resources required by human intelligence. This disparity highlights the need for new guiding principles and motivates drawing inspiration from the fundamental organizational principles of brain computation. Among these principles, modularity has been shown to be critical for supporting the efficient learning and strong generalization abilities consistently...

---

### 4. From Modules to Movement: Deconstructing the Modular Architecture of the Motor System

**Authors:** Alessandro Salatiello

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18787v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18787v1)

**Summary:** Coordinating multi-articulated bodies to generate purposeful movement is a formidable computational challenge. Yet the human motor system performs this task robustly in dynamic, uncertain environments, despite noisy and delayed feedback, slow actuators, and strict energetic constraints. A central question is what organizational principles underlie this efficiency. One widely recognized principle of neural organization is modularity, which enables complex problems to be decomposed into simpler su...

---

### 5. A Data-Driven Method to Map the Functional Organisation of Human Brain White Matter

**Authors:** Yifei Sun, James M. Shine, Robert D. Sanders, et al.

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18715v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18715v1)

**Summary:** The white matter of the brain is organised into axonal bundles that support long-range neural communication. Although diffusion MRI (dMRI) enables detailed mapping of these pathways through tractography, how white matter pathways directly facilitate large-scale neural synchronisation remains poorly understood. We developed a data-driven framework that integrates dMRI and functional MRI (fMRI) to model the dynamic coupling supported by white matter tracks. Specifically, we employed track dynamic ...

---

### 6. Neural Fields as World Models

**Authors:** Joshua Nunley

**Published:** 2026-02-21

🔗 [Paper](http://arxiv.org/abs/2602.18690v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18690v1)

**Summary:** How does the brain predict physical outcomes while acting in the world? Machine learning world models compress visual input into latent spaces, discarding the spatial structure that characterizes sensory cortex. We propose isomorphic world models: architectures preserving sensory topology so that physics prediction becomes geometric propagation rather than abstract state transition. We implement this using neural fields with motor-gated channels, where activity evolves through local lateral conn...

---

### 7. Online decoding of rat self-paced locomotion speed from EEG using recurrent neural networks

**Authors:** Alejandro de Miguel, Nelson Totah, Uri Maoz

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18637v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18637v1)

**Summary:** $\textit{Objective.}$ Accurate neural decoding of locomotion holds promise for advancing rehabilitation, prosthetic control, and understanding neural correlates of action. Recent studies have demonstrated decoding of locomotion kinematics across species on motorized treadmills. However, efforts to decode locomotion speed in more natural contexts$-$where pace is self-selected rather than externally imposed$-$are scarce, generally achieve only modest accuracy, and require intracranial implants. He...

---

### 8. Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay

**Authors:** Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk

**Published:** 2026-02-20

🔗 [Paper](http://arxiv.org/abs/2602.18401v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18401v1)

**Summary:** Biological neural networks (like the hippocampus) can internally generate "replay" resembling stimulus-driven activity. Recent computational models of replay use noisy recurrent neural networks (RNNs) trained to path-integrate. Replay in these networks has been described as Langevin sampling, but new modifiers of noisy RNN replay have surpassed this description. We re-examine noisy RNN replay as sampling to understand or improve it in three ways: (1) Under simple assumptions, we prove that the g...

---

### 9. Scaling and tuning to criticality in resting-state human magnetoencephalography

**Authors:** Irem Topal, Anna Poggialini, Marco Dal Maschio, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17820v1) | 📄 [PDF](https://arxiv.org/pdf/2602.17820v1)

**Summary:** Scaling laws in biological neural networks have long been investigated. From 1/f noise to neuronal avalanches, evidence of scaling in brain activity has been increasingly linked to tuning to or near criticality. The concept of scaling is intimately related to the renormalization group (RG), in essence providing coarse-grained, simplified descriptions that generalize to classes of diverse physical systems. Following the RG idea, a coarse-graining scheme has recently been proposed for populations ...

---

### 10. Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis

**Authors:** Minheng Chen, Tong Chen, Chao Cao, et al.

**Published:** 2026-02-19

🔗 [Paper](http://arxiv.org/abs/2602.17557v2) | 📄 [PDF](https://arxiv.org/pdf/2602.17557v2)

**Summary:** Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, viol...

---

### 11. Construction of a classification model for dementia among Brazilian adults aged 50 and over

**Authors:** F. S. Menezes, M. C. F. G. Barretto, E. Q. C. Garcia, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16887v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16887v1)

**Summary:** To build a dementia classification model for middle-aged and elderly Brazilians, implemented in Python, combining variable selection and multivariable analysis, using low-cost variables with modification potential. Observational study with a predictive modeling approach using a cross-sectional design, aimed at estimating the chances of developing dementia, using data from the Brazilian Longitudinal Study of Aging (ELSI-Brazil), involving 9,412 participants. Dementia was determined based on neuro...

---

### 12. A Systematic Evaluation of Sample-Level Tokenization Strategies for MEG Foundation Models

**Authors:** SungJun Cho, Chetan Gohil, Rukuang Huang, et al.

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16626v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16626v1)

**Summary:** Recent success in natural language processing has motivated growing interest in large-scale foundation models for neuroimaging data. Such models often require discretization of continuous neural time series data, a process referred to as 'tokenization'. However, the impact of different tokenization strategies for neural data is currently poorly understood. In this work, we present a systematic evaluation of sample-level tokenization strategies for transformer-based large neuroimaging models (LNM...

---

### 13. The Representational Alignment Hypothesis: Evidence for and Consequences of Invariant Semantic Structure Across Embedding Modalities

**Authors:** Akhil Ramidi, Kevin Scharp

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.16584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16584v1)

**Summary:** There is growing evidence that independently trained AI systems come to represent the world in the same way. In other words, independently trained embeddings from text, vision, audio, and neural signals share an underlying geometry. We call this the Representational Alignment Hypothesis (RAH) and investigate evidence for and consequences of this claim. The evidence is of two kinds: (i) internal structure comparison techniques, such as representational similarity analysis and topological data ana...

---

### 14. Fine-Pruning: A Biologically Inspired Algorithm for Personalization of Machine Learning Models

**Authors:** Joseph Bingham, Saman Zonouz, Dvir Aran

**Published:** 2026-02-18

🔗 [Paper](http://arxiv.org/abs/2602.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2602.18507v1)

**Summary:** Neural networks have long strived to emulate the learning capabilities of the human brain. While deep neural networks (DNNs) draw inspiration from the brain in neuron design, their training methods diverge from biological foundations. Backpropagation, the primary training method for DNNs, requires substantial computational resources and fully labeled datasets, presenting major bottlenecks in development and application. This work demonstrates that by returning to biomimicry, specifically mimicki...

---

### 15. Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research

**Authors:** Chenda Duan, Yipeng Zhang, Sotaro Kanai, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16072v2) | 📄 [PDF](https://arxiv.org/pdf/2602.16072v2)

**Summary:** Epilepsy affects over 50 million people worldwide, and one-third of patients suffer drug-resistant seizures where surgery offers the best chance of seizure freedom. Accurate localization of the epileptogenic zone (EZ) relies on intracranial EEG (iEEG). Clinical workflows, however, remain constrained by labor-intensive manual review. At the same time, existing data-driven approaches are typically developed on single-center datasets that are inconsistent in format and metadata, lack standardized b...

---

### 16. Time-Varying Directed Interactions in Functional Brain Networks: Modeling and Validation

**Authors:** Nan Xu, Xiaodi Zhang, Wen-Ju Pan, et al.

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.16004v1) | 📄 [PDF](https://arxiv.org/pdf/2602.16004v1)

**Summary:** Understanding the dynamic nature of brain connectivity is critical for elucidating neural processing, behavior, and brain disorders. Traditional approaches such as sliding-window correlation (SWC) characterize time-varying undirected associations but do not resolve directional interactions, limiting inference about time-resolved information flow in brain networks. We introduce sliding-window prediction correlation (SWpC), which embeds a directional linear time-invariant (LTI) model within each s...

---

### 17. Energy budgets govern synaptic precision and its regulation during plasticity

**Authors:** James Malkin, Cian O'Donnell, Conor Houghton

**Published:** 2026-02-17

🔗 [Paper](http://arxiv.org/abs/2602.15787v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15787v1)

**Summary:** Synaptic transmission must balance the need for reliable signalling against the metabolic cost of achieving that reliability. How energetic constraints shape synaptic precision and its regulation during plasticity remains unclear. Here we develop an energy--constrained framework in which synapses minimise postsynaptic response variance subject to a fixed mean and an effective energy budget. Combinations of candidate physiological costs are used to estimate an energy cost for synaptic transmissio...

---

### 18. A golden-ratio partition of information and the balance between prediction and surprise: a neuro-cognitive route to antifragility

**Authors:** Pablo Padilla, Oliver López-Corona, Elvia Ramírez-Carrillo, et al.

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.15266v1) | 📄 [PDF](https://arxiv.org/pdf/2602.15266v1)

**Summary:** Adaptive systems must strike a balance between prediction and surprise to thrive in uncertain environments. We propose an information-theoretic balance function, $ f(p) = -(1 - p)\ln(1 - p) + \ln p $, which quantifies the net informational gain from contrasting explained variance $p$ with unexplained novelty $(1 - p)$. This function is strictly concave on $(0,1)$ and reaches its unique maximum at $ p^* \approx 0.882$, revealing a regime where confidence is high but the residual uncertainty carri...

---

### 19. Drift-Diffusion Matching: Embedding dynamics in latent manifolds of asymmetric neural networks

**Authors:** Ramón Nartallo-Kaluarachchi, Renaud Lambiotte, Alain Goriely

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14885v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14885v1)

**Summary:** Recurrent neural networks (RNNs) provide a theoretical framework for understanding computation in biological neural circuits, yet classical results, such as Hopfield's model of associative memory, rely on symmetric connectivity that restricts network dynamics to gradient-like flows. In contrast, biological networks support rich time-dependent behaviour facilitated by their asymmetry. Here we introduce a general framework, which we term drift-diffusion matching, for training continuous-time RNNs ...

---

### 20. Evolutionarily Primitive Social Entities

**Authors:** Angelica Kaufmann

**Published:** 2026-02-16

🔗 [Paper](http://arxiv.org/abs/2602.14843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.14843v1)

**Summary:** Social entities only exist in virtue of collective acceptance or recognition, or acknowledgement by two or more individuals in the context of joint activities. Joint activities are made possible by the coordination of plans for action, and the coordination of plans for action is made possible by the capacity for collective intentionality. This paper investigates how primitive is the capacity that nonhuman animals have to create social entities, by individuating how primitive is the capacity for ...

---

### 21. Human-Aligned Evaluation of a Pixel-wise DNN Color Constancy Model

**Authors:** Hamed Heidari-Gorji, Raquel Gil Rodriguez, Karl R. Gegenfurtner

**Published:** 2026-02-14

🔗 [Paper](http://arxiv.org/abs/2602.13887v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13887v1)

**Summary:** We previously investigated color constancy in photorealistic virtual reality (VR) and developed a Deep Neural Network (DNN) that predicts reflectance from rendered images. Here, we combine both approaches to compare and study a model and human performance with respect to established color constancy mechanisms: local surround, maximum flux and spatial mean. Rather than evaluating the model against physical ground truth, model performance was assessed using the same achromatic object selection tas...

---

### 22. Metabolic cost of information processing in Poisson variational autoencoders

**Authors:** Hadi Vafaii, Jacob L. Yates

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13421v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13421v1)

**Summary:** Computation in biological systems is fundamentally energy-constrained, yet standard theories of computation treat energy as freely available. Here, we argue that variational free energy minimization under a Poisson assumption offers a principled path toward an energy-aware theory of computation. Our key observation is that the Kullback-Leibler (KL) divergence term in the Poisson free energy objective becomes proportional to the prior firing rates of model neurons, yielding an emergent metabolic ...

---

### 23. The Influence of Width Ratios on Structural Beauty in Male Faces

**Authors:** Benjamin Knopp, Theresa Tennstedt, Dominik Endres

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.13368v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13368v1)

**Summary:** This study investigates the relationship between interocular distance relative to overall facial width (width ratio) and perceived subjective beauty in male faces. Building on the methodology of Pallett et al. (2010), who found that average proportions in female faces were rated as most attractive, the current study aimed to test this hypothesis in male faces. Faces from the Chicago Face Database (Ma et al., 2015) were morphed into average faces within three groups (with low, medium, and high wi...

---

### 24. Left-right asymmetry in predicting brain activity from LLMs' representations emerges with their formal linguistic competence

**Authors:** Laurent Bonnasse-Gahot, Christophe Pallier

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12811v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12811v1)

**Summary:** When humans and large language models (LLMs) process the same text, activations in the LLMs correlate with brain activity measured, e.g., with functional magnetic resonance imaging (fMRI). Moreover, it has been shown that, as the training of an LLM progresses, the performance in predicting brain activity from its internal activations improves more in the left hemisphere than in the right one. The aim of the present work is to understand which kind of competence acquired by the LLMs underlies the...

---

### 25. A consequence of failed sequential learning: A computational account of developmental amnesia

**Authors:** Qi Zhang

**Published:** 2026-02-13

🔗 [Paper](http://arxiv.org/abs/2602.12547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12547v1)

**Summary:** Developmental amnesia, featured with severely impaired episodic memory and almost normal semantic memory, has been discovered to occur in children with hippocampal atrophy. This unique combination of characteristics seems to challenge the understanding that early loss of episodic memory may impede cognitive development and result in severe mental retardation. Although a few underlying mechanisms have been suggested, no computational model has been reported that is able to mimic the unique combin...

---

### 26. Conference Proceedings of the Inaugural Conference of the International Society for Tractography (IST 2025 Bordeaux)

**Authors:** Flavio Dell Acqua, Maxime Descoteaux, Graham Little, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.12410v1) | 📄 [PDF](https://arxiv.org/pdf/2602.12410v1)

**Summary:** This collection comprises the abstracts presented during poster, power pitch and oral sessions at the Inaugural Conference of the International Society for Tractography (IST Conference 2025), held in Bordeaux, France, from October 13-16, 2025. The conference was designed to foster meaningful exchange and collaboration between disparate fields. The overall focus was on advancing research, innovation, and community in the common fields of interest: neuroanatomy, tractography methods and scientific...

---

### 27. TAVAE: A VAE with Adaptable Priors Explains Contextual Modulation in the Visual Cortex

**Authors:** Balázs Meszéna, Keith T. Murray, Julien Corbo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11956v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11956v1)

**Summary:** The brain interprets visual information through learned regularities, a computation formalized as probabilistic inference under a prior. The visual cortex establishes priors for this inference, some delivered through established top-down connections that inform low-level cortices about statistics represented at higher levels in the cortical hierarchy. While evidence shows that adaptation leads to priors reflecting the structure of natural images, it remains unclear whether similar priors can be ...

---

### 28. CL API: Real-Time Closed-Loop Interactions with Biological Neural Networks

**Authors:** David Hogan, Andrew Doherty, Boon Kien Khoo, et al.

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11632v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11632v1)

**Summary:** Biological neural networks (BNNs) are increasingly explored for their rich dynamics, parallelism, and adaptive behavior. Beyond understanding their function as a scientific endeavour, a key focus has been using these biological systems as a novel computing substrate. However, BNNs can only function as reliable information-processing systems if inputs are delivered in a temporally and structurally consistent manner. In practice, this requires stimulation with precisely controlled structure, micro...

---

### 29. Defining causal mechanism in dual process theory and two types of feedback control

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-02-12

🔗 [Paper](http://arxiv.org/abs/2602.11478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11478v1)

**Summary:** Mental events are considered to supervene on physical events. A supervenient event does not change without a corresponding change in the underlying subvenient physical events. Since wholes and their parts exhibit the same supervenience-subvenience relations, inter-level causation has been expected to serve as a model for mental causation. We proposed an inter-level causation mechanism to construct a model of consciousness and an agent's self-determination. However, a significant gap exists betwe...

---

### 30. A Dynamical Microscope for Multivariate Oscillatory Signals: Validating Regime Recovery on Shared Manifolds

**Authors:** Łukasz Furman, Ludovico Minati, Włodzisław Duch

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11054v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11054v1)

**Summary:** Multivariate oscillatory signals from complex systems often exhibit non-stationary dynamics and metastable regime structure, making dynamical interpretation challenging. We introduce a ``dynamical microscope'' framework that converts multichannel signals into circular phase--amplitude features, learns a data-driven latent trajectory representation with an autoencoder, and quantifies dynamical regimes through trajectory geometry and flow field metrics. Using a coupled Stuart--Landau oscillator ne...

---

### 31. Learning Glioblastoma Tumor Heterogeneity Using Brain Inspired Topological Neural Networks

**Authors:** Ankita Paul, Wenyi Wang

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.11234v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11234v1)

**Summary:** Accurate prognosis for Glioblastoma (GBM) using deep learning (DL) is hindered by extreme spatial and structural heterogeneity. Moreover, inconsistent MRI acquisition protocols across institutions hinder generalizability of models. Conventional transformer and DL pipelines often fail to capture the multi-scale morphological diversity such as fragmented necrotic cores, infiltrating margins, and disjoint enhancing components leading to scanner-specific artifacts and poor cross-site prognosis. We p...

---

### 32. Graph neural networks uncover structure and functions underlying the activity of simulated neural assemblies

**Authors:** Cédric Allier, Larissa Heinrich, Magdalena Schneider, et al.

**Published:** 2026-02-11

🔗 [Paper](http://arxiv.org/abs/2602.13325v1) | 📄 [PDF](https://arxiv.org/pdf/2602.13325v1)

**Summary:** Graph neural networks trained to predict observable dynamics can be used to decompose the temporal activity of complex heterogeneous systems into simple, interpretable representations. Here we apply this framework to simulated neural assemblies with thousands of neurons and demonstrate that it can jointly reveal the connectivity matrix, the neuron types, the signaling functions, and in some cases hidden external stimuli. In contrast to existing machine learning approaches such as recurrent neura...

---

### 33. ENIGMA: EEG-to-Image in 15 Minutes Using Less Than 1% of the Parameters

**Authors:** Reese Kneeland, Wangshu Jiang, Ugo Bruzadin Nunes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10361v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10361v1)

**Summary:** To be practical for real-life applications, models for brain-computer interfaces must be easily and quickly deployable on new subjects, effective on affordable scanning hardware, and small enough to run locally on accessible computing resources. To directly address these current limitations, we introduce ENIGMA, a multi-subject electroencephalography (EEG)-to-Image decoding model that reconstructs seen images from EEG recordings and achieves state-of-the-art (SOTA) performance on the research-gr...

---

### 34. UltraLIF: Fully Differentiable Spiking Neural Networks via Ultradiscretization and Max-Plus Algebra

**Authors:** Jose Marie Antonio Miñoza

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.11206v1) | 📄 [PDF](https://arxiv.org/pdf/2602.11206v1)

**Summary:** Spiking Neural Networks (SNNs) offer energy-efficient, biologically plausible computation but suffer from non-differentiable spike generation, necessitating reliance on heuristic surrogate gradients. This paper introduces UltraLIF, a principled framework that replaces surrogate gradients with ultradiscretization, a mathematical formalism from tropical geometry providing continuous relaxations of discrete dynamics. The central insight is that the max-plus semiring underlying ultradiscretization n...

---

### 35. Popularity Feedback Constrains Innovation in Cultural Markets

**Authors:** Lucas Gautheron, Raja Marjieh, Dalton C. Conley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09997v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09997v1)

**Summary:** Real-world creative processes ranging from art to science rely on social feedback-loops between selection and creation. Yet, the effects of popularity feedback on collective creativity remain poorly understood. We investigate how popularity ratings influence cultural dynamics in a large-scale online experiment where participants ($N = 1\,008$) iteratively \textit{select} images from evolving markets and \textit{produce} their own modifications. Results show that exposing the popularity of images...

---

### 36. Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release

**Authors:** Peter N. Taylor, Gerard Hall, Jonathan Horsley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09852v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09852v1)

**Summary:** Epileptic seizures are generated in cerebral networks that propagate ictal and interictal activity. The structure of cerebral networks underpinning epileptic activity can be inferred from diffusion-weighted MRI (DWI). However, publicly available DWI data in individuals with epilepsy are scarce, and processing is technically challenging due to scan-specific artifacts, limiting research progress. Here, we release raw DWI data from 216 individuals with epilepsy and 98 healthy controls. Subject iden...

---

### 37. Finite integration time can shift optimal sensitivity away from criticality

**Authors:** Sahel Azizpour, Viola Priesemann, Johannes Zierenberg, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09491v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09491v1)

**Summary:** Sensitivity to small changes in the environment is crucial for many real-world tasks, enabling living and artificial systems to make correct behavioral decisions. It has been shown that such sensitivity is maximized when a system operates near the critical point of a phase transition. However, proximity to criticality introduces large fluctuations and diverging timescales. Hence, to leverage the maximal sensitivity, it would require impractically long integration periods. Here, we analytically a...

---

### 38. Structural coarse-graining enables noise-robust functional connectivity and reveals hidden inter-subject variability

**Authors:** Izaro Fernandez-Iriondo, Antonio Jimenez-Marin, Jesus Cortes, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08910v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08910v1)

**Summary:** Functional connectivity estimates are highly sensitive to analysis choices and can be dominated by noise when the number of sampled time points is small relative to network dimensionality. This issue is particularly acute in fMRI, where scan resolution is limited. Because scan duration is constrained by practical factors (e.g., motion and fatigue), many datasets remain statistically underpowered for high-dimensional correlation estimation. We introduce a framework that combines diffusion-based s...

---

### 39. Universal Approximation Theorems for Dynamical Systems with Infinite-Time Horizon Guarantees

**Authors:** Abel Sagodi, Il Memming Park

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08640v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08640v2)

**Summary:** Universal approximation theorems establish the expressive capacity of neural network architectures. For dynamical systems, existing results are limited to finite time horizons or systems with a globally stable equilibrium, leaving multistability and limit cycles unaddressed. We prove that Neural ODEs achieve $\varepsilon$-$δ$ closeness -- trajectories within error $\varepsilon$ except for initial conditions of measure $< δ$ -- over the \emph{infinite} time horizon $[0,\infty)$ for three target c...

---

### 40. Linguistics and Human Brain: A Perspective of Computational Neuroscience

**Authors:** Fudong Zhang, Bo Chai, Yujie Wu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08275v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08275v2)

**Summary:** Elucidating the language-brain relationship requires bridging the methodological gap between the abstract theoretical frameworks of linguistics and the empirical neural data of neuroscience. Serving as an interdisciplinary cornerstone, computational neuroscience formalizes the hierarchical and dynamic structures of language into testable neural models through modeling, simulation, and data analysis. This enables a computational dialogue between linguistic hypotheses and neural mechanisms. Recent...

---

### 41. Bootstrapping Life-Inspired Machine Intelligence: The Biological Route from Chemistry to Cognition and Creativity

**Authors:** Giovanni Pezzulo, Michael Levin

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.08079v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08079v1)

**Summary:** Achieving advanced machine intelligence remains a central challenge in AI research, often approached through scaling neural architectures and generative models. However, biological systems offer a broader repertoire of strategies for adaptive, goal-directed behavior - strategies that emerged long before nervous systems evolved. This paper advocates a genuinely life-inspired approach to machine intelligence, drawing on principles from biology that enable robustness, autonomy, and open-ended probl...

---

### 42. Beyond Expertise: Stable Individual Differences in Predictive Eye-Hand Coordination

**Authors:** Emiko Shishido

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.07816v2) | 📄 [PDF](https://arxiv.org/pdf/2602.07816v2)

**Summary:** Human eye-hand coordination relies on internal forward models that predict future states and compensate for sensory delays. During line tracing, the gaze typically leads the hand through predictive saccades, yet the extent to which this predictive window reflects expertise or intrinsic individual traits remains unclear. In this study, I examined eye-hand coordination in professional calligraphers and non-experts performing a controlled line tracing task. The temporal coupling between saccade dis...

---

### 43. How does longer temporal context enhance multimodal narrative video processing in the brain?

**Authors:** Prachi Jindal, Anant Khandelwal, Manish Gupta, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07570v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07570v1)

**Summary:** Understanding how humans and artificial intelligence systems process complex narrative videos is a fundamental challenge at the intersection of neuroscience and machine learning. This study investigates how the temporal context length of video clips (3--12 s clips) and the narrative-task prompting shape brain-model alignment during naturalistic movie watching. Using fMRI recordings from participants viewing full-length movies, we examine how brain regions sensitive to narrative context dynamical...

---

### 44. Linguistic properties and model scale in brain encoding: from small to compressed language models

**Authors:** Subba Reddy Oota, Vijay Rowtula, Satya Sai Srinath Namburi, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07547v1)

**Summary:** Recent work has shown that scaling large language models (LLMs) improves their alignment with human brain activity, yet it remains unclear what drives these gains and which representational properties are responsible. Although larger models often yield better task performance and brain alignment, they are increasingly difficult to analyze mechanistically. This raises a fundamental question: what is the minimal model capacity required to capture brain-relevant representations? To address this que...

---

### 45. Training-Driven Representational Geometry Modularization Predicts Brain Alignment in Language Models

**Authors:** Yixuan Liu, Zhiyuan Ma, Likai Tang, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07539v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07539v1)

**Summary:** How large language models (LLMs) align with the neural representation and computation of human language is a central question in cognitive science. Using representational geometry as a mechanistic lens, we addressed this by tracking entropy, curvature, and fMRI encoding scores throughout Pythia (70M-1B) training. We identified a geometric modularization where layers self-organize into stable low- and high-complexity clusters. The low-complexity module, characterized by reduced entropy and curvat...

---

### 46. Cognitive algorithms and systems of episodic memory, semantic memory and their learnings

**Authors:** Qi Zhang

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07261v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07261v1)

**Summary:** Declarative memory, the memory that can be "declared" in words or languages, is made up of two dissociated parts: episodic memory and semantic memory. This dissociation has its neuroanatomical basis episodic memory is mostly associated with the hippocampus and semantic memory with the neocortex. The two memories, on the other hand, are closely related. Lesions in the hippocampus often result in various impairments of explicit memory, e.g., anterograde, retrograde and developmental amnesias, and ...

---

### 47. Extracting Root-Causal Brain Activity Driving Psychopathology from Resting State fMRI

**Authors:** Eric V. Strobl

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07233v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07233v1)

**Summary:** Neuroimaging studies of psychiatric disorders often correlate imaging patterns with diagnostic labels or composite symptom scores, yielding diffuse associations that obscure underlying mechanisms. We instead seek to identify root-causal maps -- localized BOLD disturbances that initiate pathological cascades -- and to link them selectively to symptom dimensions. We introduce a bilevel structural causal model that connects between-subject symptom structure to within-subject resting-state fMRI via ...

---

### 48. Behavior Score Prediction in Resting-State Functional MRI by Deep State Space Modeling

**Authors:** Javier Salazar Cavazos, Maximillian Egan, Krisanne Litinas, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07131v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07131v1)

**Summary:** Early clinical assessment of Alzheimer's disease relies on behavior scores that measure a subject's language, memory, and cognitive skills. On the medical imaging side, functional magnetic resonance imaging has provided invaluable insights into the neural pathways underlying Alzheimer's disease. While prior studies have used resting-state functional MRI by extracting functional connectivity matrices, these approaches neglect the temporal dynamics inherent in functional data. In this work, we pre...

---

### 49. Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space

**Authors:** Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05971v1)

**Summary:** Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to ...

---

### 50. BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction

**Authors:** Xuanhua Yin, Runkai Zhao, Lina Yao, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04512v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04512v1)

**Summary:** Naturalistic fMRI characterizes the brain as a dynamic predictive engine driven by continuous sensory streams. However, modeling the causal forward evolution in realistic neural simulation is impeded by the timescale mismatch between multimodal inputs and the complex topology of cortical networks. To address these challenges, we introduce BrainVista, a multimodal autoregressive framework designed to model the causal evolution of brain states. BrainVista incorporates Network-wise Tokenizers to di...

---

## stat.ML

**50 papers**

### 1. Statistical Query Lower Bounds for Smoothed Agnostic Learning

**Authors:** Ilias Diakonikolas, Daniel M. Kane

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21191v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21191v1)

**Summary:** We study the complexity of smoothed agnostic learning, recently introduced by~\cite{CKKMS24}, in which the learner competes with the best classifier in a target class under slight Gaussian perturbations of the inputs. Specifically, we focus on the prototypical task of agnostically learning halfspaces under subgaussian distributions in the smoothed model. The best known upper bound for this problem relies on $L_1$-polynomial regression and has complexity $d^{\tilde{O}(1/σ^2) \log(1/ε)}$, where $σ...

---

### 2. Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions

**Authors:** Mame Diarra Toure, David A. Stephens

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21160v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21160v1)

**Summary:** In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=σ_k^{2}/(2μ_k)$, with $μ_k{=}\mathbb{E}[p_k]$ and $σ_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the...

---

### 3. SOM-VQ: Topology-Aware Tokenization for Interactive Generative Models

**Authors:** Alessandro Londei, Denise Lanzieri, Matteo Benati

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21133v1)

**Summary:** Vector-quantized representations enable powerful discrete generative models but lack semantic structure in token space, limiting interpretable human control. We introduce SOM-VQ, a tokenization method that combines vector quantization with Self-Organizing Maps to learn discrete codebooks with explicit low-dimensional topology. Unlike standard VQ-VAE, SOM-VQ uses topology-aware updates that preserve neighborhood structure: nearby tokens on a learned grid correspond to semantically similar states,...

---

### 4. An Enhanced Projection Pursuit Tree Classifier with Visual Methods for Assessing Algorithmic Improvements

**Authors:** Natalia da Silva, Dianne Cook, Eun-Kyung Lee

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21130v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21130v1)

**Summary:** This paper presents enhancements to the projection pursuit tree classifier and visual diagnostic methods for assessing their impact in high dimensions. The original algorithm uses linear combinations of variables in a tree structure where depth is constrained to be less than the number of classes -- a limitation that proves too rigid for complex classification problems. Our extensions improve performance in multi-class settings with unequal variance-covariance structures and nonlinear class sepa...

---

### 5. Adjacency Spectral Embeddings of Correlation Networks

**Authors:** Keith Levin

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21055v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21055v1)

**Summary:** In many applications, weighted networks are constructed based on time series data: each time series is associated to a vertex and edge weights are given by pairwise correlations. The result is a network whose edge dependency structure violates the assumptions of most common network models. Nonetheless, it is common to analyze these "correlation networks" using embedding methods derived from edge-independent network models, based on a belief that the edges are approximately independent. In this w...

---

### 6. Is Multi-Distribution Learning as Easy as PAC Learning: Sharp Rates with Bounded Label Noise

**Authors:** Rafael Hanashiro, Abhishek Shetty, Patrick Jaillet

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21039v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21039v1)

**Summary:** Towards understanding the statistical complexity of learning from heterogeneous sources, we study the problem of multi-distribution learning. Given $k$ data sources, the goal is to output a classifier for each source by exploiting shared structure to reduce sample complexity. We focus on the bounded label noise setting to determine whether the fast $1/ε$ rates achievable in single-task learning extend to this regime with minimal dependence on $k$. Surprisingly, we show that this is not the case....

---

### 7. Empirically Calibrated Conditional Independence Tests

**Authors:** Milleno Pan, Antoine de Mathelin, Wesley Tansey

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21036v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21036v1)

**Summary:** Conditional independence tests (CIT) are widely used for causal discovery and feature selection. Even with false discovery rate (FDR) control procedures, they often fail to provide frequentist guarantees in practice. We highlight two common failure modes: (i) in small samples, asymptotic guarantees for many CITs can be inaccurate and even correctly specified models fail to estimate the noise levels and control the error, and (ii) when sample sizes are large but models are misspecified, unaccount...

---

### 8. Exchangeable Gaussian Processes for Staggered-Adoption Policy Evaluation

**Authors:** Hayk Gevorgyan, Konstantinos Kalogeropoulos, Angelos Alexopoulos

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.21031v1) | 📄 [PDF](https://arxiv.org/pdf/2602.21031v1)

**Summary:** We study the use of exchangeable multi-task Gaussian processes (GPs) for causal inference in panel data, applying the framework to two settings: one with a single treated unit subject to a once-and-for-all treatment and another with multiple treated units and staggered treatment adoption. Our approach models the joint evolution of outcomes for treated and control units through a GP prior that ensures exchangeability across units while allowing for flexible nonlinear trends over time. The resulti...

---

### 9. Efficient Online Learning in Interacting Particle Systems

**Authors:** Louis Sharrock, Nikolas Kantas, Grigorios A. Pavliotis

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20875v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20875v1)

**Summary:** We introduce a new method for online parameter estimation in stochastic interacting particle systems, based on continuous observation of a small number of particles from the system. Our method recursively updates the model parameters using a stochastic approximation of the gradient of the asymptotic log likelihood, which is computed using the continuous stream of observations. Under suitable assumptions, we rigorously establish convergence of our method to the stationary points of the asymptotic...

---

### 10. Stochastic Discount Factors with Cross-Asset Spillovers

**Authors:** Doron Avramov, Xin He

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20856v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20856v1)

**Summary:** This paper develops a unified framework that links firm-level predictive signals, cross-asset spillovers, and the stochastic discount factor (SDF). Signals and spillovers are jointly estimated by maximizing the Sharpe ratio, yielding an interpretable SDF that both ranks characteristic relevance and uncovers the direction of predictive influence across assets. Out-of-sample, the SDF consistently outperforms self-predictive and expected-return benchmarks across investment universes and market stat...

---

### 11. Maximum entropy based testing in network models: ERGMs and constrained optimization

**Authors:** Subhrosekhar Ghosh, Rathindra Nath Karmakar, Samriddha Lahiry

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20844v1)

**Summary:** Stochastic network models play a central role across a wide range of scientific disciplines, and questions of statistical inference arise naturally in this context. In this paper we investigate goodness-of-fit and two-sample testing procedures for statistical networks based on the principle of maximum entropy (MaxEnt). Our approach formulates a constrained entropy-maximization problem on the space of networks, subject to prescribed structural constraints. The resulting test statistics are define...

---

### 12. DANCE: Doubly Adaptive Neighborhood Conformal Estimation

**Authors:** Brandon R. Feng, Brian J. Reich, Daniel Beaglehole, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20652v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20652v1)

**Summary:** The recent developments of complex deep learning models have led to unprecedented ability to accurately predict across multiple data representation types. Conformal prediction for uncertainty quantification of these models has risen in popularity, providing adaptive, statistically-valid prediction sets. For classification tasks, conformal methods have typically focused on utilizing logit scores. For pre-trained models, however, this can result in inefficient, overly conservative set sizes when n...

---

### 13. Sparse Bayesian Deep Functional Learning with Structured Region Selection

**Authors:** Xiaoxian Zhu, Yingmeng Li, Shuangge Ma, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20651v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20651v1)

**Summary:** In modern applications such as ECG monitoring, neuroimaging, wearable sensing, and industrial equipment diagnostics, complex and continuously structured data are ubiquitous, presenting both challenges and opportunities for functional data analysis. However, existing methods face a critical trade-off: conventional functional models are limited by linearity, whereas deep learning approaches lack interpretable region selection for sparse effects. To bridge these gaps, we propose a sparse Bayesian f...

---

### 14. On the Convergence of Stochastic Gradient Descent with Perturbed Forward-Backward Passes

**Authors:** Boao Kong, Hengrui Zhang, Kun Yuan

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20646v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20646v1)

**Summary:** We study stochastic gradient descent (SGD) for composite optimization problems with $N$ sequential operators subject to perturbations in both the forward and backward passes. Unlike classical analyses that treat gradient noise as additive and localized, perturbations to intermediate outputs and gradients cascade through the computational graph, compounding geometrically with the number of operators. We present the first comprehensive theoretical analysis of this setting. Specifically, we charact...

---

### 15. Scalable multitask Gaussian processes for complex mechanical systems with functional covariates

**Authors:** Razak Christophe Sabi Gninkou, Andrés F. López-Lopera, Franck Massa, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20640v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20640v1)

**Summary:** Functional covariates arise in many scientific and engineering applications when model inputs take the form of time-dependent or spatially distributed profiles, such as varying boundary conditions or changing material behaviours. In addition, new practices in digital simulation require predictions accompanied by confidence intervals. Models based on Gaussian processes (GPs) provide principled uncertainty quantification. However, GPs capable of jointly handling functional covariates and multiple ...

---

### 16. Amortized Bayesian inference for actigraph time sheet data from mobile devices

**Authors:** Daniel Zhou, Sudipto Banerjee

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20611v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20611v1)

**Summary:** Mobile data technologies use ``actigraphs'' to furnish information on health variables as a function of a subject's movement. The advent of wearable devices and related technologies has propelled the creation of health databases consisting of human movement data to conduct research on mobility patterns and health outcomes. Statistical methods for analyzing high-resolution actigraph data depend on the specific inferential context, but the advent of Artificial Intelligence (AI) frameworks require ...

---

### 17. Characterizing Online and Private Learnability under Distributional Constraints via Generalized Smoothness

**Authors:** Moïse Blanchard, Abhishek Shetty, Alexander Rakhlin

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20585v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20585v1)

**Summary:** Understanding minimal assumptions that enable learning and generalization is perhaps the central question of learning theory. Several celebrated results in statistical learning theory, such as the VC theorem and Littlestone's characterization of online learnability, establish conditions on the hypothesis class that allow for learning under independent data and adversarial data, respectively. Building upon recent work bridging these extremes, we study sequential decision making under distribution...

---

### 18. Upper-Linearizability of Online Non-Monotone DR-Submodular Maximization over Down-Closed Convex Sets

**Authors:** Yiyang Lu, Haresh Jadav, Mohammad Pedramfar, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20578v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20578v1)

**Summary:** We study online maximization of non-monotone Diminishing-Return(DR)-submodular functions over down-closed convex sets, a regime where existing projection-free online methods suffer from suboptimal regret and limited feedback guarantees. Our main contribution is a new structural result showing that this class is $1/e$-linearizable under carefully designed exponential reparametrization, scaling parameter, and surrogate potential, enabling a reduction to online linear optimization. As a result, we ...

---

### 19. Stability and Generalization of Push-Sum Based Decentralized Optimization over Directed Graphs

**Authors:** Yifei Liang, Yan Sun, Xiaochun Cao, et al.

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20567v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20567v1)

**Summary:** Push-Sum-based decentralized learning enables optimization over directed communication networks, where information exchange may be asymmetric. While convergence properties of such methods are well understood, their finite-iteration stability and generalization behavior remain unclear due to structural bias induced by column-stochastic mixing and asymmetric error propagation. In this work, we develop a unified uniform-stability framework for the Stochastic Gradient Push (SGP) algorithm that captu...

---

### 20. Standard Transformers Achieve the Minimax Rate in Nonparametric Regression with $C^{s,λ}$ Targets

**Authors:** Yanming Lai, Defeng Sun

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20555v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20555v1)

**Summary:** The tremendous success of Transformer models in fields such as large language models and computer vision necessitates a rigorous theoretical investigation. To the best of our knowledge, this paper is the first work proving that standard Transformers can approximate Hölder functions $ C^{s,λ}\left([0,1]^{d\times n}\right) $$ (s\in\mathbb{N}_{\geq0},0<λ\leq1) $ under the $L^t$ distance ($t \in [1, \infty]$) with arbitrary precision. Building upon this approximation result, we demonstrate that stan...

---

### 21. Oracle-Robust Online Alignment for Large Language Models

**Authors:** Zimeng Li, Mudit Gaur, Vaneet Aggarwal

**Published:** 2026-02-24

🔗 [Paper](http://arxiv.org/abs/2602.20457v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20457v1)

**Summary:** We study online alignment of large language models under misspecified preference feedback, where the observed preference oracle deviates from an ideal but unknown ground-truth oracle. The online LLM alignment problem is a bi-level reinforcement problem due to the coupling between data collection and policy updates. Recently, the problem has been reduced to tractable single-level objective in the SAIL (Self-Improving Efficient Online Alignment) framework. In this paper, we introduce a pointwise o...

---

### 22. Wasserstein Distributionally Robust Online Learning

**Authors:** Guixian Chen, Salar Fattahi, Soroosh Shafiee

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20403v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20403v1)

**Summary:** We study distributionally robust online learning, where a risk-averse learner updates decisions sequentially to guard against worst-case distributions drawn from a Wasserstein ambiguity set centered at past observations. While this paradigm is well understood in the offline setting through Wasserstein Distributionally Robust Optimization (DRO), its online extension poses significant challenges in both convergence and computation. In this paper, we address these challenges. First, we formulate th...

---

### 23. Selecting Optimal Variable Order in Autoregressive Ising Models

**Authors:** Shiba Biswal, Marc Vuffray, Andrey Y. Lokhov

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20394v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20394v1)

**Summary:** Autoregressive models enable tractable sampling from learned probability distributions, but their performance critically depends on the variable ordering used in the factorization via complexities of the resulting conditional distributions. We propose to learn the Markov random field describing the underlying data, and use the inferred graphical model structure to construct optimized variable orderings. We illustrate our approach on two-dimensional image-like models where a structure-aware order...

---

### 24. Gap-Dependent Bounds for Nearly Minimax Optimal Reinforcement Learning with Linear Function Approximation

**Authors:** Haochen Zhang, Zhong Zheng, Lingzhou Xue

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20297v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20297v1)

**Summary:** We study gap-dependent performance guarantees for nearly minimax-optimal algorithms in reinforcement learning with linear function approximation. While prior works have established gap-dependent regret bounds in this setting, existing analyses do not apply to algorithms that achieve the nearly minimax-optimal worst-case regret bound $\tilde{O}(d\sqrt{H^3K})$, where $d$ is the feature dimension, $H$ is the horizon length, and $K$ is the number of episodes. We bridge this gap by providing the firs...

---

### 25. Discrete Diffusion with Sample-Efficient Estimators for Conditionals

**Authors:** Karthik Elamvazhuthi, Abhijith Jayakumar, Andrey Y. Lokhov

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20293v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20293v1)

**Summary:** We study a discrete denoising diffusion framework that integrates a sample-efficient estimator of single-site conditionals with round-robin noising and denoising dynamics for generative modeling over discrete state spaces. Rather than approximating a discrete analog of a score function, our formulation treats single-site conditional probabilities as the fundamental objects that parameterize the reverse diffusion process. We employ a sample-efficient method known as Neural Interaction Screening E...

---

### 26. JUCAL: Jointly Calibrating Aleatoric and Epistemic Uncertainty in Classification Tasks

**Authors:** Jakob Heiss, Sören Lambrecht, Jakob Weissteiner, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20153v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20153v1)

**Summary:** We study post-calibration uncertainty for trained ensembles of classifiers. Specifically, we consider both aleatoric (label noise) and epistemic (model) uncertainty. Among the most popular and widely used calibration methods in classification are temperature scaling (i.e., pool-then-calibrate) and conformal methods. However, the main shortcoming of these calibration methods is that they do not balance the proportion of aleatoric and epistemic uncertainty. Not balancing these uncertainties can se...

---

### 27. Behavior Learning (BL): Learning Hierarchical Optimization Structures from Data

**Authors:** Zhenyao Ma, Yue Liang, Dongxu Li

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20152v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20152v1)

**Summary:** Inspired by behavioral science, we propose Behavior Learning (BL), a novel general-purpose machine learning framework that learns interpretable and identifiable optimization structures from data, ranging from single optimization problems to hierarchical compositions. It unifies predictive performance, intrinsic interpretability, and identifiability, with broad applicability to scientific domains involving optimization. BL parameterizes a compositional utility function built from intrinsically in...

---

### 28. Conformal Risk Control for Non-Monotonic Losses

**Authors:** Anastasios N. Angelopoulos

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20151v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20151v1)

**Summary:** Conformal risk control is an extension of conformal prediction for controlling risk functions beyond miscoverage. The original algorithm controls the expected value of a loss that is monotonic in a one-dimensional parameter. Here, we present risk control guarantees for generic algorithms applied to possibly non-monotonic losses with multidimensional parameters. The guarantees depend on the stability of the algorithm -- unstable algorithms have looser guarantees. We give applications of this tech...

---

### 29. Adaptation to Intrinsic Dependence in Diffusion Language Models

**Authors:** Yunxiao Zhao, Changxiao Cai

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20126v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20126v1)

**Summary:** Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive (AR) approaches, enabling parallel token generation beyond a rigid left-to-right order. Despite growing empirical success, the theoretical understanding of how unmasking schedules -- which specify the order and size of unmasked tokens during sampling -- affect generation quality remains limited. In this work, we introduce a distribution-agnostic unmasking schedule for DLMs that adapts to the (unkn...

---

### 30. A Theory of How Pretraining Shapes Inductive Bias in Fine-Tuning

**Authors:** Nicolas Anguita, Francesco Locatello, Andrew M. Saxe, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.20062v1) | 📄 [PDF](https://arxiv.org/pdf/2602.20062v1)

**Summary:** Pretraining and fine-tuning are central stages in modern machine learning systems. In practice, feature learning plays an important role across both stages: deep neural networks learn a broad range of useful features during pretraining and further refine those features during fine-tuning. However, an end-to-end theoretical understanding of how choices of initialization impact the ability to reuse and refine features during fine-tuning has remained elusive. Here we develop an analytical theory of...

---

### 31. On the Equivalence of Random Network Distillation, Deep Ensembles, and Bayesian Inference

**Authors:** Moritz A. Zanger, Yijun Wu, Pascal R. Van der Vaart, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19964v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19964v1)

**Summary:** Uncertainty quantification is central to safe and efficient deployments of deep learning models, yet many computationally practical methods lack lacking rigorous theoretical motivation. Random network distillation (RND) is a lightweight technique that measures novelty via prediction errors against a fixed random target. While empirically effective, it has remained unclear what uncertainties RND measures and how its estimates relate to other approaches, e.g. Bayesian inference or deep ensembles. ...

---

### 32. A Bayesian Framework for Post-disruption Travel Time Prediction in Metro Networks

**Authors:** Shayan Nazemi, Aurélie Labbe, Stefan Steiner, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19952v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19952v1)

**Summary:** Disruptions are an inherent feature of transportation systems, occurring unpredictably and with varying durations. Even after an incident is reported as resolved, disruptions can induce irregular train operations that generate substantial uncertainty in passenger waiting and travel times. Accurately forecasting post-disruption travel times therefore remains a critical challenge for transit operators and passenger information systems. This paper develops a Bayesian spatiotemporal modeling framewo...

---

### 33. Rethinking Chronological Causal Discovery with Signal Processing

**Authors:** Kurt Butler, Damian Machlanski, Panagiotis Dimitrakopoulos, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19903v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19903v1)

**Summary:** Causal discovery problems use a set of observations to deduce causality between variables in the real world, typically to answer questions about biological or physical systems. These observations are often recorded at regular time intervals, determined by a user or a machine, depending on the experiment design. There is generally no guarantee that the timing of these recordings matches the timing of the underlying biological or physical events. In this paper, we examine the sensitivity of causal...

---

### 34. Generalized Random Direction Newton Algorithms for Stochastic Optimization

**Authors:** Soumen Pachal, Prashanth L. A., Shalabh Bhatnagar, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19893v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19893v1)

**Summary:** We present a family of generalized Hessian estimators of the objective using random direction stochastic approximation (RDSA) by utilizing only noisy function measurements. The form of each estimator and the order of the bias depend on the number of function measurements. In particular, we demonstrate that estimators with more function measurements exhibit lower-order estimation bias. We show the asymptotic unbiasedness of the estimators. We also perform asymptotic and non-asymptotic convergence...

---

### 35. Dirichlet Scale Mixture Priors for Bayesian Neural Networks

**Authors:** August Arnstad, Leiv Rønneberg, Geir Storvik

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19859v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19859v1)

**Summary:** Neural networks are the cornerstone of modern machine learning, yet can be difficult to interpret, give overconfident predictions and are vulnerable to adversarial attacks. Bayesian neural networks (BNNs) provide some alleviation of these limitations, but have problems of their own. The key step of specifying prior distributions in BNNs is no trivial task, yet is often skipped out of convenience. In this work, we propose a new class of prior distributions for BNNs, the Dirichlet scale mixture (D...

---

### 36. Path-conditioned training: a principled way to rescale ReLU neural networks

**Authors:** Arthur Lebeurrier, Titouan Vayer, Rémi Gribonval

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19799v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19799v1)

**Summary:** Despite recent algorithmic advances, we still lack principled ways to leverage the well-documented rescaling symmetries in ReLU neural network parameters. While two properly rescaled weights implement the same function, the training dynamics can be dramatically different. To offer a fresh perspective on exploiting this phenomenon, we build on the recent path-lifting framework, which provides a compact factorization of ReLU networks. We introduce a geometrically motivated criterion to rescale neu...

---

### 37. Drift Localization using Conformal Predictions

**Authors:** Fabian Hinder, Valerie Vaquet, Johannes Brinkrolf, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19790v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19790v1)

**Summary:** Concept drift -- the change of the distribution over time -- poses significant challenges for learning systems and is of central interest for monitoring. Understanding drift is thus paramount, and drift localization -- determining which samples are affected by the drift -- is essential. While several approaches exist, most rely on local testing schemes, which tend to fail in high-dimensional, low-signal settings. In this work, we consider a fundamentally different approach based on conformal pre...

---

### 38. Unsupervised Anomaly Detection in NSL-KDD Using $β$-VAE: A Latent Space and Reconstruction Error Approach

**Authors:** Dylan Baptiste, Ramla Saddem, Alexandre Philippot, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19785v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19785v1)

**Summary:** As Operational Technology increasingly integrates with Information Technology, the need for Intrusion Detection Systems becomes more important. This paper explores an unsupervised approach to anomaly detection in network traffic using $β$-Variational Autoencoders on the NSL-KDD dataset. We investigate two methods: leveraging the latent space structure by measuring distances from test samples to the training data projections, and using the reconstruction error as a conventional anomaly detection ...

---

### 39. Ensemble Machine Learning and Statistical Procedures for Dynamic Predictions of Time-to-Event Outcomes

**Authors:** Nina van Gerwen, Sten Willemsen, Bettina E. Hansen, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19761v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19761v1)

**Summary:** Dynamic predictions for longitudinal and time-to-event outcomes have become a versatile tool in precision medicine. Our work is motivated by the application of dynamic predictions in the decision-making process for primary biliary cholangitis patients. For these patients, serial biomarker measurements (e.g., bilirubin and alkaline phosphatase levels) are routinely collected to inform treating physicians of the risk of liver failure and guide clinical decision-making. Two popular statistical appr...

---

### 40. Testing Effect Homogeneity and Confounding in High-Dimensional Experimental and Observational Studies

**Authors:** Ana Armendariz, Martin Huber

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19703v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19703v1)

**Summary:** We propose a framework for testing the homogeneity of conditional average treatment effects (CATEs) across multiple experimental and observational studies. Our approach leverages multiple randomized trials to assess whether treatment effects vary with unobserved heterogeneity that differs across trials: if CATEs are homogeneous, this indicates the absence of interactions between treatment and unobservables in the mean effect. Comparing CATEs between experimental and observational data further al...

---

### 41. Smoothness Adaptivity in Constant-Depth Neural Networks: Optimal Rates via Smooth Activations

**Authors:** Yuhao Liu, Zilin Wang, Lei Wu, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19691v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19691v1)

**Summary:** Smooth activation functions are ubiquitous in modern deep learning, yet their theoretical advantages over non-smooth counterparts remain poorly understood. In this work, we characterize both approximation and statistical properties of neural networks with smooth activations over the Sobolev space $W^{s,\infty}([0,1]^d)$ for arbitrary smoothness $s>0$. We prove that constant-depth networks equipped with smooth activations automatically exploit arbitrarily high orders of target function smoothness...

---

### 42. Compositional Planning with Jumpy World Models

**Authors:** Jesse Farebrother, Matteo Pirotta, Andrea Tirinzoni, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19634v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19634v1)

**Summary:** The ability to plan with temporal abstractions is central to intelligent decision-making. Rather than reasoning over primitive actions, we study agents that compose pre-trained policies as temporally extended actions, enabling solutions to complex tasks that no constituent alone can solve. Such compositional planning remains elusive as compounding errors in long-horizon predictions make it challenging to estimate the visitation distribution induced by sequencing policies. Motivated by the geomet...

---

### 43. Variational Inference for Bayesian MIDAS Regression

**Authors:** Luigi Simeone

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19610v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19610v1)

**Summary:** We develop a Coordinate Ascent Variational Inference (CAVI) algorithm for Bayesian Mixed Data Sampling (MIDAS) regression with linear weight parameterizations. The model separates impact coeffcients from weighting function parameters through a normalization constraint, creating a bilinear structure that renders generic Hamiltonian Monte Carlo samplers unreliable while preserving conditional conjugacy exploitable by CAVI. Each variational update admits a closed-form solution: Gaussian for regress...

---

### 44. Manifold-Aligned Generative Transport

**Authors:** Xinyu Tian, Xiaotong Shen

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19600v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19600v1)

**Summary:** High-dimensional generative modeling is fundamentally a manifold-learning problem: real data concentrate near a low-dimensional structure embedded in the ambient space. Effective generators must therefore balance support fidelity -- placing probability mass near the data manifold -- with sampling efficiency. Diffusion models often capture near-manifold structure but require many iterative denoising steps and can leak off-support; normalizing flows sample in one pass but are limited by invertibil...

---

### 45. Goal-Oriented Influence-Maximizing Data Acquisition for Learning and Optimization

**Authors:** Weichi Yao, Bianca Dumitrascu, Bryan R. Goldsmith, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19578v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19578v1)

**Summary:** Active data acquisition is central to many learning and optimization tasks in deep neural networks, yet remains challenging because most approaches rely on predictive uncertainty estimates that are difficult to obtain reliably. To this end, we propose Goal-Oriented Influence- Maximizing Data Acquisition (GOIMDA), an active acquisition algorithm that avoids explicit posterior inference while remaining uncertainty-aware through inverse curvature. GOIMDA selects inputs by maximizing their expected ...

---

### 46. Beyond Accuracy: A Unified Random Matrix Theory Diagnostic Framework for Crash Classification Models

**Authors:** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19528v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19528v1)

**Summary:** Crash classification models in transportation safety are typically evaluated using accuracy, F1, or AUC, metrics that cannot reveal whether a model is silently overfitting. We introduce a spectral diagnostic framework grounded in Random Matrix Theory (RMT) and Heavy-Tailed Self-Regularization (HTSR) that spans the ML taxonomy: weight matrices for BERT/ALBERT/Qwen2.5, out-of-fold increment matrices for XGBoost/Random Forest, empirical Hessians for Logistic Regression, induced affinity matrices fo...

---

### 47. Real-time Win Probability and Latent Player Ability via STATS X in Team Sports

**Authors:** Yasutaka Shimizu, Atsushi Yamanobe

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19513v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19513v1)

**Summary:** This study proposes a statistically grounded framework for real-time win probability evaluation and player assessment in score-based team sports, based on minute-by-minute cumulative box-score data. We introduce a continuous dominance indicator (T-score) that maps final scores to real values consistent with win/lose outcomes, and formulate it as a time-evolving stochastic representation (T-process) driven by standardized cumulative statistics. This structure captures temporal game dynamics and e...

---

### 48. Less is More: Convergence Benefits of Fewer Data Weight Updates over Longer Horizon

**Authors:** Rudrajit Das, Neel Patel, Meisam Razaviyayn, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19510v1)

**Summary:** Data mixing--the strategic reweighting of training domains--is a critical component in training robust machine learning models. This problem is naturally formulated as a bilevel optimization task, where the outer loop optimizes domain weights to minimize validation loss, and the inner loop optimizes model parameters to minimize the weighted training loss. Classical bilevel optimization relies on hypergradients, which theoretically require the inner optimization to reach convergence. However, due...

---

### 49. Making Conformal Predictors Robust in Healthcare Settings: a Case Study on EEG Classification

**Authors:** Arjun Chatterjee, Sayeed Sajjad Razin, John Wu, et al.

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19483v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19483v1)

**Summary:** Quantifying uncertainty in clinical predictions is critical for high-stakes diagnosis tasks. Conformal prediction offers a principled approach by providing prediction sets with theoretical coverage guarantees. However, in practice, patient distribution shifts violate the i.i.d. assumptions underlying standard conformal methods, leading to poor coverage in healthcare settings. In this work, we evaluate several conformal prediction approaches on EEG seizure classification, a task with known distri...

---

### 50. The generalized underlap coefficient with an application in clustering

**Authors:** Zhaoxi Zhang, Vanda Inacio, Sara Wade

**Published:** 2026-02-23

🔗 [Paper](http://arxiv.org/abs/2602.19473v1) | 📄 [PDF](https://arxiv.org/pdf/2602.19473v1)

**Summary:** Quantifying distributional separation across groups is fundamental in statistical learning and scientific discovery, yet most classical discrepancy measures are tailored to two-group comparisons. We generalize the underlap coefficient (UNL), a multi-group separation measure, to multivariate variables. We establish key properties of UNL and provide an explicit connection to the total variation. We further interpret the UNL as a dependence measure between a group label and variables of interest an...

---

