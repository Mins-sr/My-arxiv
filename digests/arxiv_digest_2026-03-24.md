# arXiv Daily Digest - 2026-03-24

Total papers: 350

---

## cs.AI

**50 papers**

### 1. WorldCache: Content-Aware Caching for Accelerated Video World Models

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22286v1)

**Summary:** Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

---

### 2. End-to-End Training for Unified Tokenization and Latent Denoising

**Authors:** Shivam Duggal, Xingjian Bai, Zongze Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22283v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22283v1)

**Summary:** Latent diffusion models (LDMs) enable high-fidelity synthesis by operating in learned latent spaces. However, training state-of-the-art LDMs requires complex staging: a tokenizer must be trained first, before the diffusion model can be trained in the frozen latent space. We propose UNITE - an autoencoder architecture for unified tokenization and latent diffusion. UNITE consists of a Generative Encoder that serves as both image tokenizer and latent generator via weight sharing. Our key insight is...

---

### 3. UniMotion: A Unified Framework for Motion-Text-Vision Understanding and Generation

**Authors:** Ziyi Wang, Xinshun Wang, Shuang Chen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22282v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22282v1)

**Summary:** We present UniMotion, to our knowledge the first unified framework for simultaneous understanding and generation of human motion, natural language, and RGB images within a single architecture. Existing unified models handle only restricted modality subsets (e.g., Motion-Text or static Pose-Image) and predominantly rely on discrete tokenization, which introduces quantization errors and disrupts temporal continuity. UniMotion overcomes both limitations through a core principle: treating motion as ...

---

### 4. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22281v1)

**Summary:** Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning ove...

---

### 5. 3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing

**Authors:** Haoyu Zhen, Xiaolong Li, Yilin Zhao, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22279v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22279v1)

**Summary:** Large Language Models (LLMs) and Vision Language Models (VLMs) have shown impressive reasoning abilities, yet they struggle with spatial understanding and layout consistency when performing fine-grained visual editing. We introduce a Structured Reasoning framework that performs text-conditioned spatial layout editing via scene-graph reasoning. Given an input scene graph and a natural-language instruction, the model reasons over the graph to generate an updated scene graph that satisfies the text...

---

### 6. TiCo: Time-Controllable Training for Spoken Dialogue Models

**Authors:** Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22267v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22267v1)

**Summary:** We propose TiCo, a simple post-training method for enabling spoken dialogue models (SDMs) to follow time-constrained instructions and generate responses with controllable duration. This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. However, despite their strong ability to generate natural spoken responses, existing models lack time awareness and struggle to follow...

---

### 7. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

**Authors:** Changxiao Cai, Gen Li

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22248v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22248v1)

**Summary:** Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, ...

---

### 8. One Model, Two Markets: Bid-Aware Generative Recommendation

**Authors:** Yanchen Jiang, Zhe Feng, Christopher P. Mah, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22231v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22231v1)

**Summary:** Generative Recommender Systems using semantic ids, such as TIGER (Rajput et al., 2023), have emerged as a widely adopted competitive paradigm in sequential recommendation. However, existing architectures are designed solely for semantic retrieval and do not address concerns such as monetization via ad revenue and incorporation of bids for commercial retrieval. We propose GEM-Rec, a unified framework that integrates commercial relevance and monetization objectives directly into the generative seq...

---

### 9. SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation

**Authors:** Sashuai Zhou, Qiang Zhou, Junpeng Ma, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22228v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22228v1)

**Summary:** Recent advances in text-to-image (T2I) generation via reinforcement learning (RL) have benefited from reward models that assess semantic alignment and visual quality. However, most existing reward models pay limited attention to fine-grained spatial relationships, often producing images that appear plausible overall yet contain inaccuracies in object positioning. In this work, we present \textbf{SpatialReward}, a verifiable reward model explicitly designed to evaluate spatial layouts in generate...

---

### 10. Dyadic: A Scalable Platform for Human-Human and Human-AI Conversation Research

**Authors:** David M. Markowitz

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22227v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22227v1)

**Summary:** Conversation is ubiquitous in social life, but the empirical study of this interactive process has been thwarted by tools that are insufficiently modular and unadaptive to researcher needs. To relieve many constraints in conversation research, the current tutorial presents an overview and introduction to a new tool, Dyadic (https://www.chatdyadic.com/), a web-based platform for studying human-human and human-AI conversations using text-based or voice-based chats. Dyadic is distinct from other pl...

---

### 11. Evaluating the Reliability and Fidelity of Automated Judgment Systems of Large Language Models

**Authors:** Tom Biskupski, Stephan Kleber

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22214v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22214v1)

**Summary:** A Large Language Model (LLM) as judge evaluates the quality of victim Machine Learning (ML) models, specifically LLMs, by analyzing their outputs. An LLM as judge is the combination of one model and one specifically engineered judge prompt that contains the criteria for the analysis. The resulting automation of the analysis scales up the complex evaluation of the victim models' free-form text outputs by faster and more consistent judgments compared to human reviewers. Thus, quality and security ...

---

### 12. SPA: A Simple but Tough-to-Beat Baseline for Knowledge Injection

**Authors:** Kexian Tang, Jiani Wang, Shaowen Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22213v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22213v1)

**Summary:** While large language models (LLMs) are pretrained on massive amounts of data, their knowledge coverage remains incomplete in specialized, data-scarce domains, motivating extensive efforts to study synthetic data generation for knowledge injection. We propose SPA (Scaling Prompt-engineered Augmentation), a simple but tough-to-beat baseline that uses a small set of carefully designed prompts to generate large-scale synthetic data for knowledge injection. Through systematic comparisons, we find tha...

---

### 13. CayleyPy-4: AI-Holography. Towards analogs of holographic string dualities for AI tasks

**Authors:** A. Chervov, F. Levkovich-Maslyuk, A. Smolensky, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22195v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22195v1)

**Summary:** This is the fourth paper in the CayleyPy project, which applies AI methods to the exploration of large graphs. In this work, we suggest the existence of a new discrete version of holographic string dualities for this setup, and discuss their relevance to AI systems and mathematics. Many modern AI tasks -- such as those addressed by GPT-style language models or RL systems -- can be viewed as direct analogues of predicting particle trajectories on graphs. We investigate this problem for a large fa...

---

### 14. Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement

**Authors:** Junrong Guo, Shancheng Fang, Yadong Qu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22187v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22187v1)

**Summary:** Recent advances in Multimodal Large Language Models (MLLMs) have enabled automated generation of structured layouts from natural language descriptions. Existing methods typically follow a code-only paradigm that generates code to represent layouts, which are then rendered by graphic engines to produce final images. However, they are blind to the rendered visual outcome, making it difficult to guarantee readability and aesthetics. In this paper, we identify visual feedback as a critical factor in...

---

### 15. Enhancing Document-Level Machine Translation via Filtered Synthetic Corpora and Two-Stage LLM Adaptation

**Authors:** Ireh Kim, Tesia Sker, Chanwoo Kim

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22186v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22186v1)

**Summary:** In Machine Translation, Large Language Models (LLMs) have generally underperformed compared to conventional encoder-decoder systems and thus see limited adoption. However, LLMs excel at modeling contextual information, making them a natural fit for document-level translation tasks where coherence across sentences is crucial. Despite this potential, document-level MT with LLMs faces two key challenges: (1) the scarcity of large-scale, high-quality document-level parallel data; and (2) the propens...

---

### 16. MARCUS: An agentic, multimodal vision-language model for cardiac diagnosis and management

**Authors:** Jack W O'Sullivan, Mohammad Asadi, Lennart Elbe, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22179v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22179v1)

**Summary:** Cardiovascular disease remains the leading cause of global mortality, with progress hindered by human interpretation of complex cardiac tests. Current AI vision-language models are limited to single-modality inputs and are non-interactive. We present MARCUS (Multimodal Autonomous Reasoning and Chat for Ultrasound and Signals), an agentic vision-language system for end-to-end interpretation of electrocardiograms (ECGs), echocardiograms, and cardiac magnetic resonance imaging (CMR) independently a...

---

### 17. Calibeating Made Simple

**Authors:** Yurong Chen, Zhiyi Huang, Michael I. Jordan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22167v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22167v1)

**Summary:** We study calibeating, the problem of post-processing external forecasts online to minimize cumulative losses and match an informativeness-based benchmark. Unlike prior work, which analyzed calibeating for specific losses with specific arguments, we reduce calibeating to existing online learning techniques and obtain results for general proper losses. More concretely, we first show that calibeating is minimax-equivalent to regret minimization. This recovers the $O(\log T)$ calibeating rate of Fos...

---

### 18. Multimodal Survival Analysis with Locally Deployable Large Language Models

**Authors:** Moritz Gögl, Christopher Yau

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22158v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22158v1)

**Summary:** We study multimodal survival analysis integrating clinical text, tabular covariates, and genomic profiles using locally deployable large language models (LLMs). As many institutions face tight computational and privacy constraints, this setting motivates the use of lightweight, on-premises models. Our approach jointly estimates calibrated survival probabilities and generates concise, evidence-grounded prognosis text via teacher-student distillation and principled multimodal fusion. On a TCGA coh...

---

### 19. Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation

**Authors:** Kejia Liu, Haoyang Zhou, Ruoyu Xu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22153v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22153v1)

**Summary:** Recent advances in cross-view geo-localization (CVGL) methods have shown strong potential for supporting unmanned aerial vehicle (UAV) navigation in GNSS-denied environments. However, existing work predominantly focuses on matching UAV views to onboard map tiles, which introduces an inherent trade-off between accuracy and storage overhead, and overlooks the importance of the UAV's heading during navigation. Moreover, the substantial discrepancies and varying overlaps in cross-view scenarios have...

---

### 20. More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice

**Authors:** Yuta Tsuchiya, Yukino Baba

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22152v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22152v1)

**Summary:** Just as people improve decision-making by consulting diverse human advisors, they can now also consult with multiple AI systems. Prior work on group decision-making shows that advice aggregation creates pressure to conform, leading to overreliance. However, the conditions under which multi-AI consultation improves or undermines human decision-making remain unclear. We conducted experiments with three tasks in which participants received advice from panels of AIs. We varied panel size, within-pan...

---

### 21. Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding

**Authors:** Yunzhuo Sun, Xinyue Liu, Yanyang Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22121v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22121v1)

**Summary:** Text-driven video moment retrieval (VMR) remains challenging due to limited capture of hidden temporal dynamics in untrimmed videos, leading to imprecise grounding in long sequences. Traditional methods rely on natural language queries (NLQs) or static image augmentations, overlooking motion sequences and suffering from high computational costs in Transformer-based architectures. Existing approaches fail to integrate subtitle contexts and generated temporal priors effectively, we therefore propo...

---

### 22. On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation

**Authors:** Kexin Huang, Haoming Meng, Junkang Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22117v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22117v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning capabilities of large language models. While existing analyses identify that RLVR-induced changes are sparse, they primarily focus on the \textbf{magnitude} of these updates, largely overlooking their \textbf{direction}. In this work, we argue that the direction of updates is a more critical lens for understanding RLVR's effects, which can be captured by the signed, token-level log probability differen...

---

### 23. SpecTM: Spectral Targeted Masking for Trustworthy Foundation Models

**Authors:** Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22097v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22097v1)

**Summary:** Foundation models are now increasingly being developed for Earth observation (EO), yet they often rely on stochastic masking that do not explicitly enforce physics constraints; a critical trustworthiness limitation, in particular for predictive models that guide public health decisions. In this work, we propose SpecTM (Spectral Targeted Masking), a physics-informed masking design that encourages the reconstruction of targeted bands from cross-spectral context during pretraining. To achieve this,...

---

### 24. GSEM: Graph-based Self-Evolving Memory for Experience Augmented Clinical Reasoning

**Authors:** Xiao Han, Yuzheng Fan, Sendong Zhao, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22096v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22096v1)

**Summary:** Clinical decision-making agents can benefit from reusing prior decision experience. However, many memory-augmented methods store experiences as independent records without explicit relational structure, which may introduce noisy retrieval, unreliable reuse, and in some cases even hurt performance compared to direct LLM inference. We propose GSEM (Graph-based Self-Evolving Memory), a clinical memory framework that organizes clinical experiences into a dual-layer memory graph, capturing both the d...

---

### 25. A Context Engineering Framework for Improving Enterprise AI Agents based on Digital-Twin MDP

**Authors:** Xi Yang, Aurelie Lozano, Naoki Abe, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22083v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22083v1)

**Summary:** Despite rapid progress in AI agents for enterprise automation and decision-making, their real-world deployment and further performance gains remain constrained by limited data quality and quantity, complex real-world reasoning demands, difficulties with self-play, and the lack of reliable feedback signals. To address these challenges, we propose a lightweight, model-agnostic framework for improving LLM-based enterprise agents via offline reinforcement learning (RL). The proposed Context Engineer...

---

### 26. On the Failure of Topic-Matched Contrast Baselines in Multi-Directional Refusal Abliteration

**Authors:** Valentin Petrov

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22061v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22061v1)

**Summary:** Inasmuch as the removal of refusal behavior from instruction-tuned language models by directional abliteration requires the extraction of refusal-mediating directions from the residual stream activation space, and inasmuch as the construction of the contrast baseline against which harmful prompt activations are compared has been treated in the existing literature as an implementation detail rather than a methodological concern, the present work investigates whether a topically matched contrast b...

---

### 27. Uncertainty-guided Compositional Alignment with Part-to-Whole Semantic Representativeness in Hyperbolic Vision-Language Models

**Authors:** Hayeon Kim, Ji Ha Jang, Junghun James Kim, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22042v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22042v1)

**Summary:** While Vision-Language Models (VLMs) have achieved remarkable performance, their Euclidean embeddings remain limited in capturing hierarchical relationships such as part-to-whole or parent-child structures, and often face challenges in multi-object compositional scenarios. Hyperbolic VLMs mitigate this issue by better preserving hierarchical structures and modeling part-whole relations (i.e., whole scene and its part images) through entailment. However, existing approaches do not model that each ...

---

### 28. Future-Interactions-Aware Trajectory Prediction via Braid Theory

**Authors:** Caio Azevedo, Stefano Sabatini, Sascha Hornauer, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22035v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22035v1)

**Summary:** To safely operate, an autonomous vehicle must know the future behavior of a potentially high number of interacting agents around it, a task often posed as multi-agent trajectory prediction. Many previous attempts to model social interactions and solve the joint prediction task either add extensive computational requirements or rely on heuristics to label multi-agent behavior types. Braid theory, in contrast, provides a powerful exact descriptor of multi-agent behavior by projecting future trajec...

---

### 29. ROM: Real-time Overthinking Mitigation via Streaming Detection and Intervention

**Authors:** Xinyan Wang, Xiaogeng Liu, Chaowei Xiao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22016v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22016v1)

**Summary:** Large Reasoning Models (LRMs) achieve strong accuracy on challenging tasks by generating long Chain-of-Thought traces, but suffer from overthinking. Even after reaching the correct answer, they continue generating redundant reasoning steps. This behavior increases latency and compute cost and can also lead to answer drift. Existing mitigation methods either require training-heavy backbone modification or rely on hand-crafted heuristics that do not truly capture overthinking patterns. We propose ...

---

### 30. SegMaFormer: A Hybrid State-Space and Transformer Model for Efficient Segmentation

**Authors:** Duy D. Nguyen, Phat T. Tran-Truong

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22002v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22002v1)

**Summary:** The advent of Transformer and Mamba-based architectures has significantly advanced 3D medical image segmentation by enabling global contextual modeling, a capability traditionally limited in Convolutional Neural Networks (CNNs). However, state-of-the-art Transformer models often entail substantial computational complexity and parameter counts, which is particularly prohibitive for volumetric data and further exacerbated by the limited availability of annotated medical imaging datasets. To addres...

---

### 31. λ-GELU: Learning Gating Hardness for Controlled ReLU-ization in Deep Networks

**Authors:** Cristian Pérez-Corral, Alberto Fernández-Hernández, Jose I. Mestre, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21991v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21991v1)

**Summary:** Gaussian Error Linear Unit (GELU) is a widely used smooth alternative to Rectifier Linear Unit (ReLU), yet many deployment, compression, and analysis toolchains are most naturally expressed for piecewise-linear (ReLU-type) networks. We study a hardness-parameterized formulation of GELU, f(x;λ)=xΦ(λ x), where Φ is the Gaussian CDF and λ \in [1, infty) controls gate sharpness, with the goal of turning smooth gated training into a controlled path toward ReLU-compatible models. Learning λ is non-tri...

---

### 32. TREX: Trajectory Explanations for Multi-Objective Reinforcement Learning

**Authors:** Dilina Rajapakse, Juan C. Rosero, Ivana Dusparic

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21988v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21988v1)

**Summary:** Reinforcement Learning (RL) has demonstrated its ability to solve complex decision-making problems in a variety of domains, by optimizing reward signals obtained through interaction with an environment. However, many real-world scenarios involve multiple, potentially conflicting objectives that cannot be easily represented by a single scalar reward. Multi-Objective Reinforcement Learning (MORL) addresses this limitation by enabling agents to optimize several objectives simultaneously, explicitly...

---

### 33. LRC-WeatherNet: LiDAR, RADAR, and Camera Fusion Network for Real-time Weather-type Classification in Autonomous Driving

**Authors:** Nour Alhuda Albashir, Lars Pernickel, Danial Hamoud, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21987v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21987v1)

**Summary:** Autonomous vehicles face major perception and navigation challenges in adverse weather such as rain, fog, and snow, which degrade the performance of LiDAR, RADAR, and RGB camera sensors. While each sensor type offers unique strengths, such as RADAR robustness in poor visibility and LiDAR precision in clear conditions, they also suffer distinct limitations when exposed to environmental obstructions. This study proposes LRC-WeatherNet, a novel multi-sensor fusion framework that integrates LiDAR, R...

---

### 34. SecureBreak -- A dataset towards safe and secure models

**Authors:** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21975v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21975v1)

**Summary:** Large language models are becoming pervasive core components in many real-world applications. As a consequence, security alignment represents a critical requirement for their safe deployment. Although previous related works focused primarily on model architectures and alignment methodologies, these approaches alone cannot ensure the complete elimination of harmful generations. This concern is reinforced by the growing body of scientific literature showing that attacks, such as jailbreaking and p...

---

### 35. Parameter-Efficient Fine-Tuning for Medical Text Summarization: A Comparative Study of Lora, Prompt Tuning, and Full Fine-Tuning

**Authors:** Ulugbek Shernazarov, Rostislav Svitsov, Bin Shi

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21970v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21970v1)

**Summary:** Fine-tuning large language models for domain-specific tasks such as medical text summarization demands substantial computational resources. Parameter-efficient fine-tuning (PEFT) methods offer promising alternatives by updating only a small fraction of parameters. This paper compares three adaptation approaches-Low-Rank Adaptation (LoRA), Prompt Tuning, and Full Fine-Tuning-across the Flan-T5 model family on the PubMed medical summarization dataset. Through experiments with multiple random seeds...

---

### 36. Suiren-1.0 Technical Report: A Family of Molecular Foundation Models

**Authors:** Junyi An, Xinyu Lu, Yun-Fei Shi, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21942v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21942v1)

**Summary:** We introduce Suiren-1.0, a family of molecular foundation models for the accurate modeling of diverse organic systems. Suiren-1.0 comprising three specialized variants (Suiren-Base, Suiren-Dimer, and Suiren-ConfAvg) is integrated within an algorithmic framework that bridges the gap between 3D conformational geometry and 2D statistical ensemble spaces. We first pre-train Suiren-Base (1.8B parameters) on a 70M-sample Density Functional Theory dataset using spatial self-supervision and SE(3)-equiva...

---

### 37. Chronological Contrastive Learning: Few-Shot Progression Assessment in Irreversible Diseases

**Authors:** Clemens Watzenböck, Daniel Aletaha, Michaël Deman, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21935v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21935v1)

**Summary:** Quantitative disease severity scoring in medical imaging is costly, time-consuming, and subject to inter-reader variability. At the same time, clinical archives contain far more longitudinal imaging data than expert-annotated severity scores. Existing self-supervised methods typically ignore this chronological structure. We introduce ChronoCon, a contrastive learning approach that replaces label-based ranking losses with rankings derived solely from the visitation order of a patient's longitudin...

---

### 38. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

**Authors:** Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21933v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21933v1)

**Summary:** The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training ...

---

### 39. Guideline-grounded retrieval-augmented generation for ophthalmic clinical decision support

**Authors:** Shuying Chen, Sen Cui, Zhong Cao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21925v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21925v1)

**Summary:** In this work, we propose Oph-Guid-RAG, a multimodal visual RAG system for ophthalmology clinical question answering and decision support. We treat each guideline page as an independent evidence unit and directly retrieve page images, preserving tables, flowcharts, and layout information. We further design a controllable retrieval framework with routing and filtering, which selectively introduces external evidence and reduces noise. The system integrates query decomposition, query rewriting, retr...

---

### 40. Deep Reinforcement Learning and The Tale of Two Temporal Difference Errors

**Authors:** Juan Sebastian Rojas, Chi-Guhn Lee

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21921v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21921v1)

**Summary:** The temporal difference (TD) error was first formalized in Sutton (1988), where it was first characterized as the difference between temporally successive predictions, and later, in that same work, formulated as the difference between a bootstrapped target and a prediction. Since then, these two interpretations of the TD error have been used interchangeably in the literature, with the latter eventually being adopted as the standard critic loss in deep reinforcement learning (RL) architectures. I...

---

### 41. SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation

**Authors:** Linkuan Zhou, Yinghao Xia, Yufei Shen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21904v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21904v1)

**Summary:** Unsupervised Domain Adaptation (UDA) is essential for deploying medical segmentation models across diverse clinical environments. Existing methods are fundamentally limited, suffering from semantically unaware feature alignment that results in poor distributional fidelity and from pseudo-label validation that disregards global anatomical constraints, thus failing to prevent the formation of globally implausible structures. To address these issues, we propose SHAPE (Structure-aware Hierarchical U...

---

### 42. Not All Layers Are Created Equal: Adaptive LoRA Ranks for Personalized Image Generation

**Authors:** Donald Shenaj, Federico Errica, Antonio Carta

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21884v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21884v1)

**Summary:** Low Rank Adaptation (LoRA) is the de facto fine-tuning strategy to generate personalized images from pre-trained diffusion models. Choosing a good rank is extremely critical, since it trades off performance and memory consumption, but today the decision is often left to the community's consensus, regardless of the personalized subject's complexity. The reason is evident: the cost of selecting a good rank for each LoRA component is combinatorial, so we opt for practical shortcuts such as fixing t...

---

### 43. SmaAT-QMix-UNet: A Parameter-Efficient Vector-Quantized UNet for Precipitation Nowcasting

**Authors:** Nikolas Stavrou, Siamak Mehrkanoon

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21879v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21879v1)

**Summary:** Weather forecasting supports critical socioeconomic activities and complements environmental protection, yet operational Numerical Weather Prediction (NWP) systems remain computationally intensive, thus being inefficient for certain applications. Meanwhile, recent advances in deep data-driven models have demonstrated promising results in nowcasting tasks. This paper presents SmaAT-QMix-UNet, an enhanced variant of SmaAT-UNet that introduces two key innovations: a vector quantization (VQ) bottlen...

---

### 44. P^2O: Joint Policy and Prompt Optimization

**Authors:** Xinyu Lu, Kaiqi Zhang, Jinglin Yang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21877v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21877v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful paradigm for enhancing the reasoning capabilities of Large Language Models (LLMs). However, vanilla RLVR suffers from inefficient exploration, particularly when confronting "hard samples" that yield nearzero success rates. In such scenarios, the reliance on sparse outcome rewards typically results in zero-advantage estimates, effectively starving the model of supervision signals despite the high informational value o...

---

### 45. Manifold-Aware Exploration for Reinforcement Learning in Video Generation

**Authors:** Mingzhe Zheng, Weijie Kong, Yue Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21872v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21872v1)

**Summary:** Group Relative Policy Optimization (GRPO) methods for video generation like FlowGRPO remain far less reliable than their counterparts for language models and images. This gap arises because video generation has a complex solution space, and the ODE-to-SDE conversion used for exploration can inject excess noise, lowering rollout quality and making reward estimates less reliable, which destabilizes post-training alignment. To address this problem, we view the pre-trained model as defining a valid ...

---

### 46. Adversarial Camouflage

**Authors:** Paweł Borsukiewicz, Daniele Lunghi, Melissa Tessa, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21867v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21867v1)

**Summary:** While the rapid development of facial recognition algorithms has enabled numerous beneficial applications, their widespread deployment has raised significant concerns about the risks of mass surveillance and threats to individual privacy. In this paper, we introduce \textit{Adversarial Camouflage} as a novel solution for protecting users' privacy. This approach is designed to be efficient and simple to reproduce for users in the physical world. The algorithm starts by defining a low-dimensional ...

---

### 47. Tacit Knowledge Management with Generative AI: Proposal of the GenAI SECI Model

**Authors:** Naoshi Uchihira

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21866v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21866v1)

**Summary:** The emergence of generative AI is bringing about a significant transformation in knowledge management. Generative AI has the potential to address the limitations of conventional knowledge management systems, and it is increasingly being deployed in real-world settings with promising results. Related research is also expanding rapidly. However, much of this work focuses on research and practice related to the management of explicit knowledge. While fragmentary efforts have been made regarding the...

---

### 48. Adaptive Video Distillation: Mitigating Oversaturation and Temporal Collapse in Few-Step Generation

**Authors:** Yuyang You, Yongzhi Li, Jiahui Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21864v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21864v1)

**Summary:** Video generation has recently emerged as a central task in the field of generative AI. However, the substantial computational cost inherent in video synthesis makes model distillation a critical technique for efficient deployment. Despite its significance, there is a scarcity of methods specifically designed for video diffusion models. Prevailing approaches often directly adapt image distillation techniques, which frequently lead to artifacts such as oversaturation, temporal inconsistency, and m...

---

### 49. Reasoning or Rhetoric? An Empirical Analysis of Moral Reasoning Explanations in Large Language Models

**Authors:** Aryan Kasat, Smriti Singh, Aman Chadha, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21854v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21854v1)

**Summary:** Do large language models reason morally, or do they merely sound like they do? We investigate whether LLM responses to moral dilemmas exhibit genuine developmental progression through Kohlberg's stages of moral development, or whether alignment training instead produces reasoning-like outputs that superficially resemble mature moral judgment without the underlying developmental trajectory. Using an LLM-as-judge scoring pipeline validated across three judge models, we classify more than 600 respo...

---

### 50. Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection

**Authors:** Junhyeok Rui Cha, Woohyun Cha, Jaeyong Shin, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21853v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21853v1)

**Summary:** This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Unlike prior methods that typically rely on domain randomization over a fixed finite set of parameters, the proposed approach injects state-dependent perturbations into the input joint torque during forward simulation. These perturbations are designed to simulate a broader spectrum of reality gaps than standard parameter randomization without requiring additional trai...

---

## cs.CL

**50 papers**

### 1. WorldCache: Content-Aware Caching for Accelerated Video World Models

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22286v1)

**Summary:** Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

---

### 2. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22281v1)

**Summary:** Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning ove...

---

### 3. TiCo: Time-Controllable Training for Spoken Dialogue Models

**Authors:** Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22267v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22267v1)

**Summary:** We propose TiCo, a simple post-training method for enabling spoken dialogue models (SDMs) to follow time-constrained instructions and generate responses with controllable duration. This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. However, despite their strong ability to generate natural spoken responses, existing models lack time awareness and struggle to follow...

---

### 4. Greater accessibility can amplify discrimination in generative AI

**Authors:** Carolin Holtermann, Minh Duc Bui, Kaitlyn Zhou, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22260v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22260v1)

**Summary:** Hundreds of millions of people rely on large language models (LLMs) for education, work, and even healthcare. Yet these models are known to reproduce and amplify social biases present in their training data. Moreover, text-based interfaces remain a barrier for many, for example, users with limited literacy, motor impairments, or mobile-only devices. Voice interaction promises to expand accessibility, but unlike text, speech carries identity cues that users cannot easily mask, raising concerns ab...

---

### 5. MemDLM: Memory-Enhanced DLM Training

**Authors:** Zehua Pei, Hui-Ling Zhen, Weizhe Lin, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22241v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22241v1)

**Summary:** Diffusion Language Models (DLMs) offer attractive advantages over Auto-Regressive (AR) models, such as full-attention parallel decoding and flexible generation. However, they suffer from a notable train-inference mismatch: DLMs are trained with a static, single-step masked prediction objective, but deployed through a multi-step progressive denoising trajectory. We propose MemDLM (Memory-Enhanced DLM), which narrows this gap by embedding a simulated denoising process into training via Bi-level Op...

---

### 6. Dyadic: A Scalable Platform for Human-Human and Human-AI Conversation Research

**Authors:** David M. Markowitz

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22227v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22227v1)

**Summary:** Conversation is ubiquitous in social life, but the empirical study of this interactive process has been thwarted by tools that are insufficiently modular and unadaptive to researcher needs. To relieve many constraints in conversation research, the current tutorial presents an overview and introduction to a new tool, Dyadic (https://www.chatdyadic.com/), a web-based platform for studying human-human and human-AI conversations using text-based or voice-based chats. Dyadic is distinct from other pl...

---

### 7. Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease

**Authors:** Abner Hernandez, Eunjung Yeo, Kwanghee Choi, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22225v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22225v1)

**Summary:** The limited availability of dysarthric speech data makes cross-lingual detection an important but challenging problem. A key difficulty is that speech representations often encode language-dependent structure that can confound dysarthria detection. We propose a representation-level language shift (LS) that aligns source-language self-supervised speech representations with the target-language distribution using centroid-based vector adaptation estimated from healthy-control speech. We evaluate th...

---

### 8. Gumbel Distillation for Parallel Text Generation

**Authors:** Chi Zhang, Xixi Hu, Bo Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22216v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22216v1)

**Summary:** The slow, sequential nature of autoregressive (AR) language models has driven the adoption of parallel decoding methods. However, these non-AR models often sacrifice generation quality as they struggle to model the complex joint distribution of token sequences. To narrow this performance gap, we introduce Gumbel Distillation, a novel distillation technique that enables parallel decoders to learn this distribution effectively. Our method leverages the Gumbel-Max trick to create a deterministic ma...

---

### 9. SPA: A Simple but Tough-to-Beat Baseline for Knowledge Injection

**Authors:** Kexian Tang, Jiani Wang, Shaowen Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22213v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22213v1)

**Summary:** While large language models (LLMs) are pretrained on massive amounts of data, their knowledge coverage remains incomplete in specialized, data-scarce domains, motivating extensive efforts to study synthetic data generation for knowledge injection. We propose SPA (Scaling Prompt-engineered Augmentation), a simple but tough-to-beat baseline that uses a small set of carefully designed prompts to generate large-scale synthetic data for knowledge injection. Through systematic comparisons, we find tha...

---

### 10. Enhancing Document-Level Machine Translation via Filtered Synthetic Corpora and Two-Stage LLM Adaptation

**Authors:** Ireh Kim, Tesia Sker, Chanwoo Kim

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22186v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22186v1)

**Summary:** In Machine Translation, Large Language Models (LLMs) have generally underperformed compared to conventional encoder-decoder systems and thus see limited adoption. However, LLMs excel at modeling contextual information, making them a natural fit for document-level translation tasks where coherence across sentences is crucial. Despite this potential, document-level MT with LLMs faces two key challenges: (1) the scarcity of large-scale, high-quality document-level parallel data; and (2) the propens...

---

### 11. The Semantic Ladder: A Framework for Progressive Formalization of Natural Language Content for Knowledge Graphs and AI Systems

**Authors:** Lars Vogt

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22136v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22136v1)

**Summary:** Semantic data and knowledge infrastructures must reconcile two fundamentally different forms of representation: natural language, in which most knowledge is created and communicated, and formal semantic models, which enable machine-actionable integration, interoperability, and reasoning. Bridging this gap remains a central challenge, particularly when full semantic formalization is required at the point of data entry. Here, we introduce the Semantic Ladder, an architectural framework that enable...

---

### 12. Multiperspectivity as a Resource for Narrative Similarity Prediction

**Authors:** Max Upravitelev, Veronika Solopova, Jing Yang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22103v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22103v1)

**Summary:** Predicting narrative similarity can be understood as an inherently interpretive task: different, equally valid readings of the same text can produce divergent interpretations and thus different similarity judgments, posing a fundamental challenge for semantic evaluation benchmarks that encode a single ground truth. Rather than treating this multiperspectivity as a challenge to overcome, we propose to incorporate it in the decision making process of predictive systems. To explore this strategy, w...

---

### 13. Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison

**Authors:** Caio Vicentino

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22075v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22075v1)

**Summary:** We present a controlled empirical comparison between autoregressive (AR) and masked diffusion (MDLM) language models. Both models are trained on identical data (50M tokens from TinyStories), identical compute budget (20,000 steps, batch size 32, sequence length 512), and identical hardware (NVIDIA H100 80GB), isolating the generation paradigm as the sole variable. We report three findings. First, both paradigms achieve comparable training throughput (~50K tokens/second), with MDLM requiring only...

---

### 14. Dual-Space Knowledge Distillation with Key-Query Matching for Large Language Models with Vocabulary Mismatch

**Authors:** Stella Eva Tsiapali, Cong-Thanh Do, Kate Knill

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22056v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22056v1)

**Summary:** Large language models (LLMs) achieve state-of-the-art (SOTA) performance across language tasks, but are costly to deploy due to their size and resource demands. Knowledge Distillation (KD) addresses this by training smaller Student models to mimic larger Teacher models, improving efficiency without significant performance loss. Dual-Space Knowledge Distillation with Cross-Model Attention (DSKD-CMA) has emerged as a SOTA method for KD between LLMs with distinct tokenizers, yet its internal workin...

---

### 15. ROM: Real-time Overthinking Mitigation via Streaming Detection and Intervention

**Authors:** Xinyan Wang, Xiaogeng Liu, Chaowei Xiao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22016v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22016v1)

**Summary:** Large Reasoning Models (LRMs) achieve strong accuracy on challenging tasks by generating long Chain-of-Thought traces, but suffer from overthinking. Even after reaching the correct answer, they continue generating redundant reasoning steps. This behavior increases latency and compute cost and can also lead to answer drift. Existing mitigation methods either require training-heavy backbone modification or rely on hand-crafted heuristics that do not truly capture overthinking patterns. We propose ...

---

### 16. Retrieving Climate Change Disinformation by Narrative

**Authors:** Max Upravitelev, Veronika Solopova, Charlott Jakob, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22015v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22015v1)

**Summary:** Detecting climate disinformation narratives typically relies on fixed taxonomies, which do not accommodate emerging narratives. Thus, we re-frame narrative detection as a retrieval task: given a narrative's core message as a query, rank texts from a corpus by alignment with that narrative. This formulation requires no predefined label set and can accommodate emerging narratives. We repurpose three climate disinformation datasets (CARDS, Climate Obstruction, climate change subset of PolyNarrative...

---

### 17. On the Challenges and Opportunities of Learned Sparse Retrieval for Code

**Authors:** Simon Lupart, Maxime Louis, Thibault Formal, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22008v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22008v1)

**Summary:** Retrieval over large codebases is a key component of modern LLM-based software engineering systems. Existing approaches predominantly rely on dense embedding models, while learned sparse retrieval (LSR) remains largely unexplored for code. However, applying sparse retrieval to code is challenging due to subword fragmentation, semantic gaps between natural-language queries and code, diversity of programming languages and sub-tasks, and the length of code documents, which can harm sparsity and lat...

---

### 18. SecureBreak -- A dataset towards safe and secure models

**Authors:** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21975v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21975v1)

**Summary:** Large language models are becoming pervasive core components in many real-world applications. As a consequence, security alignment represents a critical requirement for their safe deployment. Although previous related works focused primarily on model architectures and alignment methodologies, these approaches alone cannot ensure the complete elimination of harmful generations. This concern is reinforced by the growing body of scientific literature showing that attacks, such as jailbreaking and p...

---

### 19. Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe

**Authors:** Xixi Wu, Qianguo Sun, Ruiyang Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21972v1)

**Summary:** Reinforcement Learning (RL) is essential for evolving Large Language Models (LLMs) into autonomous agents capable of long-horizon planning, yet a practical recipe for scaling RL in complex, multi-turn environments remains elusive. This paper presents a systematic empirical study using TravelPlanner, a challenging testbed requiring tool orchestration to satisfy multifaceted constraints. We decompose the agentic RL design space along 5 axes: reward shaping, model scaling, data composition, algorit...

---

### 20. Parameter-Efficient Fine-Tuning for Medical Text Summarization: A Comparative Study of Lora, Prompt Tuning, and Full Fine-Tuning

**Authors:** Ulugbek Shernazarov, Rostislav Svitsov, Bin Shi

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21970v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21970v1)

**Summary:** Fine-tuning large language models for domain-specific tasks such as medical text summarization demands substantial computational resources. Parameter-efficient fine-tuning (PEFT) methods offer promising alternatives by updating only a small fraction of parameters. This paper compares three adaptation approaches-Low-Rank Adaptation (LoRA), Prompt Tuning, and Full Fine-Tuning-across the Flan-T5 model family on the PubMed medical summarization dataset. Through experiments with multiple random seeds...

---

### 21. BHDD: A Burmese Handwritten Digit Dataset

**Authors:** Swan Htet Aung, Hein Htet, Htoo Say Wah Khaing, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21966v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21966v1)

**Summary:** We introduce the Burmese Handwritten Digit Dataset (BHDD), a collection of 87,561 grayscale images of handwritten Burmese digits in ten classes. Each image is 28x28 pixels, following the MNIST format. The training set has 60,000 samples split evenly across classes; the test set has 27,561 samples with class frequencies as they arose during collection. Over 150 people of different ages and backgrounds contributed samples. We analyze the dataset's class distribution, pixel statistics, and morpholo...

---

### 22. SLURP-TN : Resource for Tunisian Dialect Spoken Language Understanding

**Authors:** Haroun Elleuch, Salima Mdhaffar, Yannick Estève, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21940v1)

**Summary:** Spoken Language Understanding (SLU) aims to extract the semantic information from the speech utterance of user queries. It is a core component in a task-oriented dialogue system. With the spectacular progress of deep neural network models and the evolution of pre-trained language models, SLU has obtained significant breakthroughs. However, only a few high-resource languages have taken advantage of this progress due to the absence of SLU resources. In this paper, we seek to mitigate this obstacle...

---

### 23. Ara-Best-RQ: Multi Dialectal Arabic SSL

**Authors:** Haroun Elleuch, Ryan Whetten, Salima Mdhaffar, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21900v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21900v1)

**Summary:** We present Ara-BEST-RQ, a family of self-supervised learning (SSL) models specifically designed for multi-dialectal Arabic speech processing. Leveraging 5,640 hours of crawled Creative Commons speech and combining it with publicly available datasets, we pre-train conformer-based BEST-RQ models up to 600M parameters. Our models are evaluated on dialect identification (DID) and automatic speech recognition (ASR) tasks, achieving state-of-the-art performance on the former while using fewer paramete...

---

### 24. Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

**Authors:** Xi Xuan, Wenxin Zhang, Zhiyu Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21875v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21875v1)

**Summary:** Speech deepfake source verification systems aims to determine whether two synthetic speech utterances originate from the same source generator, often assuming that the resulting source embeddings are independent of speaker traits. However, this assumption remains unverified. In this paper, we first investigate the impact of speaker factors on source verification. We propose a speaker-disentangled metric learning (SDML) framework incorporating two novel loss functions. The first leverages Chebysh...

---

### 25. Riding Brainwaves in LLM Space: Understanding Activation Patterns Using Individual Neural Signatures

**Authors:** Ajan Subramanian, Sumukh Bettadapura, Rohan Sathish

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21847v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21847v1)

**Summary:** Consumer-grade EEG is entering everyday devices, from earbuds to headbands, raising the question of whether language models can be adapted to individual neural responses. We test this by asking whether frozen LLM representations encode person-specific EEG signals, directions in activation space that predict one person's brain activity but not another's. Using word-level EEG from 30 participants reading naturalistic sentences (ZuCo corpus), we train a separate linear probe for each person, mappin...

---

### 26. Select, Label, Evaluate: Active Testing in NLP

**Authors:** Antonio Purificato, Maria Sofia Bucarelli, Andrea Bacciu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21840v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21840v1)

**Summary:** Human annotation cost and time remain significant bottlenecks in Natural Language Processing (NLP), with test data annotation being particularly expensive due to the stringent requirement for low-error and high-quality labels necessary for reliable model evaluation. Traditional approaches require annotating entire test sets, leading to substantial resource requirements. Active Testing is a framework that selects the most informative test samples for annotation. Given a labeling budget, it aims t...

---

### 27. Instruction Set and Language for Symbolic Regression

**Authors:** Ezequiel Lopez-Rubio, Mario Pascual-Gonzalez

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21836v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21836v1)

**Summary:** A fundamental but largely unaddressed obstacle in Symbolic regression (SR) is structural redundancy: every expression DAG with admits many distinct node-numbering schemes that all encode the same expression, each occupying a separate point in the search space and consuming fitness evaluations without adding diversity. We present IsalSR (Instruction Set and Language for Symbolic Regression), a representation framework that encodes expression DAGs as strings over a compact two-tier alphabet and co...

---

### 28. Politics of Questions in News: A Mixed-Methods Study of Interrogative Stances as Markers of Voice and Power

**Authors:** Bros Victor, Barbini Matilde, Gerard Patrick, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21823v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21823v1)

**Summary:** Interrogatives in news discourse have been examined in linguistics and conversation analysis, but mostly in broadcast interviews and relatively small, often English-language corpora, while large-scale computational studies of news rarely distinguish interrogatives from declaratives or differentiate their functions. This paper brings these strands together through a mixed-methods study of the "Politics of Questions" in contemporary French-language digital news. Using over one million articles pub...

---

### 29. The Presupposition Problem in Representation Genesis

**Authors:** Yiling Wu

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21745v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21745v1)

**Summary:** Large language models are the first systems to achieve high cognitive performance without clearly undergoing representation genesis: the transition from a non-representing physical system to one whose states guide behavior in a content-sensitive way. Prior cognitive systems had already made this transition before we could examine it, and philosophy of mind treated genesis as a background condition rather than an explanatory target. LLMs provide a case that does not clearly involve this transitio...

---

### 30. The Reasoning Error About Reasoning: Why Different Types of Reasoning Require Different Representational Structures

**Authors:** Yiling Wu

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21736v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21736v1)

**Summary:** Different types of reasoning impose different structural demands on representational systems, yet no systematic account of these demands exists across psychology, AI, and philosophy of mind. I propose a framework identifying four structural properties of representational systems: operability, consistency, structural preservation, and compositionality. These properties are demanded to different degrees by different forms of reasoning, from induction through analogy and causal inference to deducti...

---

### 31. EvoIdeator: Evolving Scientific Ideas through Checklist-Grounded Reinforcement Learning

**Authors:** Andreas Sauter, Yuyue Zhao, Jacopo Urbani, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21728v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21728v1)

**Summary:** Scientific idea generation is a cornerstone of autonomous knowledge discovery, yet the iterative evolution required to transform initial concepts into high-quality research proposals remains a formidable challenge for Large Language Models (LLMs). Existing Reinforcement Learning (RL) paradigms often rely on rubric-based scalar rewards that provide global quality scores but lack actionable granularity. Conversely, language-based refinement methods are typically confined to inference-time promptin...

---

### 32. SemEval-2026 Task 12: Abductive Event Reasoning: Towards Real-World Event Causal Inference for Large Language Models

**Authors:** Pengfei Cao, Mingxuan Yang, Yubo Chen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21720v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21720v1)

**Summary:** Understanding why real-world events occur is important for both natural language processing and practical decision-making, yet direct-cause inference remains underexplored in evidence-rich settings. To address this gap, we organized SemEval-2026 Task 12: Abductive Event Reasoning (AER).\footnote{The task data is available at https://github.com/sooo66/semeval2026-task12-dataset.git} The task asks systems to identify the most plausible direct cause of a target event from supporting evidence. We fo...

---

### 33. Probing How Scalable Table Data Enhances General Long-Context Reasoning

**Authors:** Huaibing Xie, Guoliang Zhao, Yang Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21719v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21719v1)

**Summary:** As real-world tasks grow increasingly complex, long-context reasoning has become a core capability for Large Language Models (LLMs). However, few studies explore which data types are effective for long-context reasoning and why. We find that structured table data with periodic structures shows strong potential for long-context reasoning. Motivated by this observation, we mathematically analyze tabular dependency structures using mutual information, revealing periodic non-vanishing dependencies i...

---

### 34. Thinking Deeper, Not Longer: Depth-Recurrent Transformers for Compositional Generalization

**Authors:** Hung-Hsuan Chen

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21676v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21676v1)

**Summary:** Standard Transformers have a fixed computational depth, fundamentally limiting their ability to generalize to tasks requiring variable-depth reasoning, such as multi-hop graph traversal or nested logic. We propose a depth-recurrent Transformer that decouples computational depth from parameter count by iteratively applying a shared-weight Transformer block in latent space -- enabling the model to trade recurrence steps for deeper reasoning at inference time. Our architecture incorporates three me...

---

### 35. Optimizing Multi-Agent Weather Captioning via Text Gradient Descent: A Training-Free Approach with Consensus-Aware Gradient Fusion

**Authors:** Shixu Liu

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21673v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21673v1)

**Summary:** Generating interpretable natural language captions from weather time series data remains a significant challenge at the intersection of meteorological science and natural language processing. While recent advances in Large Language Models (LLMs) have demonstrated remarkable capabilities in time series forecasting and analysis, existing approaches either produce numerical predictions without human-accessible explanations or generate generic descriptions lacking domain-specific depth. We introduce...

---

### 36. TAMTRL: Teacher-Aligned Reward Reshaping for Multi-Turn Reinforcement Learning in Long-Context Compression

**Authors:** Li Wang, Yandong Wang, Xin Yu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21663v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21663v1)

**Summary:** The rapid progress of large language models (LLMs) has led to remarkable performance gains across a wide range of tasks. However, when handling long documents that exceed the model's context window limit, the entire context cannot be processed in a single pass, making chunk-wise processing necessary. This requires multiple turns to read different chunks and update memory. However, supervision is typically provided only by the final outcome, which makes it difficult to evaluate the quality of mem...

---

### 37. A Comparative Analysis of LLM Memorization at Statistical and Internal Levels: Cross-Model Commonalities and Model-Specific Signatures

**Authors:** Bowen Chen, Namgi Han, Yusuke Miyao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21658v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21658v1)

**Summary:** Memorization is a fundamental component of intelligence for both humans and LLMs. However, while LLM performance scales rapidly, our understanding of memorization lags. Due to limited access to the pre-training data of LLMs, most previous studies focus on a single model series, leading to isolated observations among series, making it unclear which findings are general or specific. In this study, we collect multiple model series (Pythia, OpenLLaMa, StarCoder, OLMo1/2/3) and analyze their shared o...

---

### 38. Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks

**Authors:** Yiliang Song, Hongjun An, Jiangan Chen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21636v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21636v1)

**Summary:** Public benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed. We frame this benchmark-centered regime as Silicon Bureaucracy and AI Test-Oriented Education, and argue that it rests on a fragile assumption: that benchmark scores directly reflect genuine generalization. In practice, however, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from moder...

---

### 39. PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection

**Authors:** Hyoseok Park, Yeonsang Park

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21576v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21576v1)

**Summary:** Long-context LLM inference is bottlenecked not by compute but by the O(n) memory bandwidth cost of scanning the KV cache at every decode step -- a wall that no amount of arithmetic scaling can break. Recent photonic accelerators have demonstrated impressive throughput for dense attention computation; however, these approaches inherit the same O(n) memory scaling as electronic attention when applied to long contexts. We observe that the real leverage point is the coarse block-selection step: a me...

---

### 40. DATASHI: A Parallel English-Tashlhiyt Corpus for Orthography Normalization and Low-Resource Language Processing

**Authors:** Nasser-Eddine Monir, Zakaria Baou

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21571v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21571v1)

**Summary:** DATASHI is a new parallel English-Tashlhiyt corpus that fills a critical gap in computational resources for Amazigh languages. It contains 5,000 sentence pairs, including a 1,500-sentence subset with expert-standardized and non-standard user-generated versions, enabling systematic study of orthographic diversity and normalization. This dual design supports text-based NLP tasks - such as tokenization, translation, and normalization - and also serves as a foundation for read-speech data collection...

---

### 41. SynSym: A Synthetic Data Generation Framework for Psychiatric Symptom Identification

**Authors:** Migyeong Kang, Jihyun Kim, Hyolim Jeon, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21529v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21529v1)

**Summary:** Psychiatric symptom identification on social media aims to infer fine-grained mental health symptoms from user-generated posts, allowing a detailed understanding of users' mental states. However, the construction of large-scale symptom-level datasets remains challenging due to the resource-intensive nature of expert labeling and the lack of standardized annotation guidelines, which in turn limits the generalizability of models to identify diverse symptom expressions from user-generated text. To ...

---

### 42. CatRAG: Functor-Guided Structural Debiasing with Retrieval Augmentation for Fair LLMs

**Authors:** Ravi Ranjan, Utkarsh Grover, Mayur Akewar, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21524v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21524v1)

**Summary:** Large Language Models (LLMs) are deployed in high-stakes settings but can show demographic, gender, and geographic biases that undermine fairness and trust. Prior debiasing methods, including embedding-space projections, prompt-based steering, and causal interventions, often act at a single stage of the pipeline, resulting in incomplete mitigation and brittle utility trade-offs under distribution shifts. We propose CatRAG Debiasing, a dual-pronged framework that integrates functor with Retrieval...

---

### 43. Generalizable Self-Evolving Memory for Automatic Prompt Optimization

**Authors:** Guanbao Liang, Yuanchen Bei, Sheng Zhou, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21520v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21520v1)

**Summary:** Automatic prompt optimization is a promising approach for adapting large language models (LLMs) to downstream tasks, yet existing methods typically search for a specific prompt specialized to a fixed task. This paradigm limits generalization across heterogeneous queries and prevents models from accumulating reusable prompting knowledge over time. In this paper, we propose MemAPO, a memory-driven framework that reconceptualizes prompt optimization as generalizable and self-evolving experience acc...

---

### 44. Triangulating Temporal Dynamics in Multilingual Swiss Online News

**Authors:** Bros Victor, Dufraisse Evan, Popescu Adrian, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21519v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21519v1)

**Summary:** Analyzing news coverage in multilingual societies can offer valuable insights into the dynamics of public discourse and the development of collective narratives, yet comprehensive studies that account for linguistic and cultural diversity within national media ecosystems remain limited, particularly in complex contexts such as Switzerland. This paper studies temporal trends in Swiss digital media across the country's three main linguistic regions, French, German, and Italian, using a triangulate...

---

### 45. Agentic Automation of BT-RADS Scoring: End-to-End Multi-Agent System for Standardized Brain Tumor Follow-up Assessment

**Authors:** Mohamed Sobhi Jabal, Jikai Zhang, Dominic LaBella, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21494v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21494v1)

**Summary:** The Brain Tumor Reporting and Data System (BT-RADS) standardizes post-treatment MRI response assessment in patients with diffuse gliomas but requires complex integration of imaging trends, medication effects, and radiation timing. This study evaluates an end-to-end multi-agent large language model (LLM) and convolutional neural network (CNN) system for automated BT-RADS classification. A multi-agent LLM system combined with automated CNN-based tumor segmentation was retrospectively evaluated on ...

---

### 46. Effective Strategies for Asynchronous Software Engineering Agents

**Authors:** Jiayi Geng, Graham Neubig

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21489v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21489v1)

**Summary:** AI agents have become increasingly capable at isolated software engineering (SWE) tasks such as resolving issues on Github. Yet long-horizon tasks involving multiple interdependent subtasks still pose challenges both with respect to accuracy, and with respect to timely completion. A natural approach to solving these long-horizon tasks in a timely manner is asynchronous multi-agent collaboration, where multiple agents work on different parts of the task at the same time. But effective application...

---

### 47. TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset and Preliminary Results with Scalable Data Mining In-the-Wild

**Authors:** Kai-Wei Chang, Yi-Cheng Lin, Huang-Cheng Chou, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21478v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21478v1)

**Summary:** Speech technologies have advanced rapidly and serve diverse populations worldwide. However, many languages remain underrepresented due to limited resources. In this paper, we introduce \textbf{TaigiSpeech}, a real-world speech intent dataset in Taiwanese Taigi (aka Taiwanese Hokkien/Southern Min), which is a low-resource and primarily spoken language. The dataset is collected from older adults, comprising 21 speakers with a total of 3k utterances. It is designed for practical intent detection sc...

---

### 48. Beyond Correlation: Refutation-Validated Aspect-Based Sentiment Analysis for Explainable Energy Market Returns

**Authors:** Wihan van der Heever, Keane Ong, Ranjan Satapathy, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21473v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21473v1)

**Summary:** This paper proposes a refutation-validated framework for aspect-based sentiment analysis in financial markets, addressing the limitations of correlational studies that cannot distinguish genuine associations from spurious ones. Using X data for the energy sector, we test whether aspect-level sentiment signals show robust, refutation-validated relationships with equity returns. Our pipeline combines net-ratio scoring with z-normalization, OLS with Newey West HAC errors, and refutation tests inclu...

---

### 49. DRTriton: Large-Scale Synthetic Data Reinforcement Learning for Triton Kernel Generation

**Authors:** Siqi Guo, Ming Lin, Tianbao Yang

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21465v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21465v1)

**Summary:** Developing efficient CUDA kernels is a fundamental yet challenging task in the generative AI industry. Recent researches leverage Large Language Models (LLMs) to automatically convert PyTorch reference implementations to CUDA kernels, significantly reducing the engineering efforts. State-of-the-art LLMs, such as GPT-5.2 and Claude-Sonnet-4.5, still struggle in this specific task. To address this challenge, we propose DRTriton, a scalable learning framework for training LLMs to convert PyTorch co...

---

### 50. DSPA: Dynamic SAE Steering for Data-Efficient Preference Alignment

**Authors:** James Wedgwood, Aashiq Muhamed, Mona T. Diab, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21461v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21461v1)

**Summary:** Preference alignment is usually achieved by weight-updating training on preference data, which adds substantial alignment-stage compute and provides limited mechanistic visibility. We propose Dynamic SAE Steering for Preference Alignment (DSPA), an inference-time method that makes sparse autoencoder (SAE) steering prompt-conditional. From preference triples, DSPA computes a conditional-difference map linking prompt features to generation-control features; during decoding, it modifies only token-...

---

## cs.CV

**50 papers**

### 1. WorldCache: Content-Aware Caching for Accelerated Video World Models

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22286v1)

**Summary:** Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

---

### 2. VideoDetective: Clue Hunting via both Extrinsic Query and Intrinsic Relevance for Long Video Understanding

**Authors:** Ruoliu Yang, Chu Wu, Caifeng Shan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22285v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22285v1)

**Summary:** Long video understanding remains challenging for multimodal large language models (MLLMs) due to limited context windows, which necessitate identifying sparse query-relevant video segments. However, existing methods predominantly localize clues based solely on the query, overlooking the video's intrinsic structure and varying relevance across segments. To address this, we propose VideoDetective, a framework that integrates query-to-segment relevance and inter-segment affinity for effective clue ...

---

### 3. End-to-End Training for Unified Tokenization and Latent Denoising

**Authors:** Shivam Duggal, Xingjian Bai, Zongze Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22283v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22283v1)

**Summary:** Latent diffusion models (LDMs) enable high-fidelity synthesis by operating in learned latent spaces. However, training state-of-the-art LDMs requires complex staging: a tokenizer must be trained first, before the diffusion model can be trained in the frozen latent space. We propose UNITE - an autoencoder architecture for unified tokenization and latent diffusion. UNITE consists of a Generative Encoder that serves as both image tokenizer and latent generator via weight sharing. Our key insight is...

---

### 4. UniMotion: A Unified Framework for Motion-Text-Vision Understanding and Generation

**Authors:** Ziyi Wang, Xinshun Wang, Shuang Chen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22282v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22282v1)

**Summary:** We present UniMotion, to our knowledge the first unified framework for simultaneous understanding and generation of human motion, natural language, and RGB images within a single architecture. Existing unified models handle only restricted modality subsets (e.g., Motion-Text or static Pose-Image) and predominantly rely on discrete tokenization, which introduces quantization errors and disrupts temporal continuity. UniMotion overcomes both limitations through a core principle: treating motion as ...

---

### 5. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22281v1)

**Summary:** Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning ove...

---

### 6. DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models

**Authors:** Zhide Zhong, Junfeng Li, Junjie He, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22280v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22280v1)

**Summary:** Vision-Language-Action (VLA) models map visual observations and language instructions directly to robotic actions. While effective for simple tasks, standard VLA models often struggle with complex, multi-step tasks requiring logical planning, as well as precise manipulations demanding fine-grained spatial perception. Recent efforts have incorporated Chain-of-Thought (CoT) reasoning to endow VLA models with a ``thinking before acting'' capability. However, current CoT-based VLA models face two cr...

---

### 7. 3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing

**Authors:** Haoyu Zhen, Xiaolong Li, Yilin Zhao, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22279v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22279v1)

**Summary:** Large Language Models (LLMs) and Vision Language Models (VLMs) have shown impressive reasoning abilities, yet they struggle with spatial understanding and layout consistency when performing fine-grained visual editing. We introduce a Structured Reasoning framework that performs text-conditioned spatial layout editing via scene-graph reasoning. Given an input scene graph and a natural-language instruction, the model reasons over the graph to generate an updated scene graph that satisfies the text...

---

### 8. The Dual Mechanisms of Spatial Reasoning in Vision-Language Models

**Authors:** Kelly Cui, Nikhil Prakash, Ayush Raina, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22278v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22278v1)

**Summary:** Many multimodal tasks, such as image captioning and visual question answering, require vision-language models (VLMs) to associate objects with their properties and spatial relations. Yet it remains unclear where and how such associations are computed within VLMs. In this work, we show that VLMs rely on two concurrent mechanisms to represent such associations. In the language model backbone, intermediate layers represent content-independent spatial relations on top of visual tokens corresponding ...

---

### 9. Repurposing Geometric Foundation Models for Multi-view Diffusion

**Authors:** Wooseok Jang, Seonghu Jeon, Jisang Han, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22275v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22275v1)

**Summary:** While recent advances in generative latent spaces have driven substantial progress in single-image generation, the optimal latent space for novel view synthesis (NVS) remains largely unexplored. In particular, NVS requires geometrically consistent generation across viewpoints, but existing approaches typically operate in a view-independent VAE latent space. In this paper, we propose Geometric Latent Diffusion (GLD), a framework that repurposes the geometrically consistent feature space of geomet...

---

### 10. DUO-VSR: Dual-Stream Distillation for One-Step Video Super-Resolution

**Authors:** Zhengyao Lv, Menghan Xia, Xintao Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22271v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22271v1)

**Summary:** Diffusion-based video super-resolution (VSR) has recently achieved remarkable fidelity but still suffers from prohibitive sampling costs. While distribution matching distillation (DMD) can accelerate diffusion models toward one-step generation, directly applying it to VSR often results in training instability alongside degraded and insufficient supervision. To address these issues, we propose DUO-VSR, a three-stage framework built upon a Dual-Stream Distillation strategy that unifies distributio...

---

### 11. GenOpticalFlow: A Generative Approach to Unsupervised Optical Flow Learning

**Authors:** Yixuan Luo, Feng Qiao, Zhexiao Xiong, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22270v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22270v1)

**Summary:** Optical flow estimation is a fundamental problem in computer vision, yet the reliance on expensive ground-truth annotations limits the scalability of supervised approaches. Although unsupervised and semi-supervised methods alleviate this issue, they often suffer from unreliable supervision signals based on brightness constancy and smoothness assumptions, leading to inaccurate motion estimation in complex real-world scenarios. To overcome these limitations, we introduce \textbf{\modelname}, a nov...

---

### 12. EgoGroups: A Benchmark For Detecting Social Groups of People in the Wild

**Authors:** Jeffri Murrugarra-Llerena, Pranav Chitale, Zicheng Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22249v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22249v1)

**Summary:** Social group detection, or the identification of humans involved in reciprocal interpersonal interactions (e.g., family members, friends, and customers and merchants), is a crucial component of social intelligence needed for agents transacting in the world. The few existing benchmarks for social group detection are limited by low scene diversity and reliance on third-person camera sources (e.g., surveillance footage). Consequently, these benchmarks generally lack real-world evaluation on how gro...

---

### 13. Riverine Land Cover Mapping through Semantic Segmentation of Multispectral Point Clouds

**Authors:** Sopitta Thurachen, Josef Taher, Matti Lehtomäki, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22230v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22230v1)

**Summary:** Accurate land cover mapping in riverine environments is essential for effective river management, ecological understanding, and geomorphic change monitoring. This study explores the use of Point Transformer v2 (PTv2), an advanced deep neural network architecture designed for point cloud data, for land cover mapping through semantic segmentation of multispectral LiDAR data in real-world riverine environments. We utilize the geometric and spectral information from the 3-channel LiDAR point cloud t...

---

### 14. Benchmarking Deep Learning Models for Aerial LiDAR Point Cloud Semantic Segmentation under Real Acquisition Conditions: A Case Study in Navarre

**Authors:** Alex Salvatierra, José Antonio Sanz, Christian Gutiérrez, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22229v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22229v1)

**Summary:** Recent advances in deep learning have significantly improved 3D semantic segmentation, but most models focus on indoor or terrestrial datasets. Their behavior under real aerial acquisition conditions remains insufficiently explored, and although a few studies have addressed similar scenarios, they differ in dataset design, acquisition conditions, and model selection. To address this gap, we conduct an experimental benchmark evaluating several state-of-the-art architectures on a large-scale aeria...

---

### 15. SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation

**Authors:** Sashuai Zhou, Qiang Zhou, Junpeng Ma, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22228v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22228v1)

**Summary:** Recent advances in text-to-image (T2I) generation via reinforcement learning (RL) have benefited from reward models that assess semantic alignment and visual quality. However, most existing reward models pay limited attention to fine-grained spatial relationships, often producing images that appear plausible overall yet contain inaccuracies in object positioning. In this work, we present \textbf{SpatialReward}, a verifiable reward model explicitly designed to evaluate spatial layouts in generate...

---

### 16. Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models

**Authors:** Meiqi Wu, Zhixin Cai, Fufangchen Zhao, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22212v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22212v1)

**Summary:** Video--based world models have emerged along two dominant paradigms: video generation and 3D reconstruction. However, existing evaluation benchmarks either focus narrowly on visual fidelity and text--video alignment for generative models, or rely on static 3D reconstruction metrics that fundamentally neglect temporal dynamics. We argue that the future of world modeling lies in 4D generation, which jointly models spatial structure and temporal evolution. In this paradigm, the core capability is i...

---

### 17. Mixture of Mini Experts: Overcoming the Linear Layer Bottleneck in Multiple Instance Learning

**Authors:** Daniel Shao, Joel Runevic, Richard J. Chen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22198v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22198v1)

**Summary:** Multiple Instance Learning (MIL) is the predominant framework for classifying gigapixel whole-slide images in computational pathology. MIL follows a sequence of 1) extracting patch features, 2) applying a linear layer to obtain task-specific patch features, and 3) aggregating the patches into a slide feature for classification. While substantial efforts have been devoted to optimizing patch feature extraction and aggregation, none have yet addressed the second point, the critical layer which tra...

---

### 18. PAM: A Pose-Appearance-Motion Engine for Sim-to-Real HOI Video Generation

**Authors:** Mingju Gao, Kaisen Yang, Huan-ang Gao, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22193v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22193v1)

**Summary:** Hand-object interaction (HOI) reconstruction and synthesis are becoming central to embodied AI and AR/VR. Yet, despite rapid progress, existing HOI generation research remains fragmented across three disjoint tracks: (1) pose-only synthesis that predicts MANO trajectories without producing pixels; (2) single-image HOI generation that hallucinates appearance from masks or 2D cues but lacks dynamics; and (3) video generation methods that require both the entire pose sequence and the ground-truth f...

---

### 19. A Backbone Benchmarking Study on Self-supervised Learning as a Auxiliary Task with Texture-based Local Descriptors for Face Analysis

**Authors:** Shukesh Reddy, Abhijit Das

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22190v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22190v1)

**Summary:** In this work, we benchmark with different backbones and study their impact for self-supervised learning (SSL) as an auxiliary task to blend texture-based local descriptors into feature modelling for efficient face analysis. It is established in previous work that combining a primary task and a self-supervised auxiliary task enables more robust and discriminative representation learning.   We employed different shallow to deep backbones for the SSL task of Masked Auto-Encoder (MAE) as an auxiliar...

---

### 20. Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement

**Authors:** Junrong Guo, Shancheng Fang, Yadong Qu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22187v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22187v1)

**Summary:** Recent advances in Multimodal Large Language Models (MLLMs) have enabled automated generation of structured layouts from natural language descriptions. Existing methods typically follow a code-only paradigm that generates code to represent layouts, which are then rendered by graphic engines to produce final images. However, they are blind to the rendered visual outcome, making it difficult to guarantee readability and aesthetics. In this paper, we identify visual feedback as a critical factor in...

---

### 21. ACPO: Counteracting Likelihood Displacement in Vision-Language Alignment with Asymmetric Constraints

**Authors:** Kaili Huang, Hongming Zhang, Rui Shen, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22165v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22165v1)

**Summary:** While Direct Preference Optimization (DPO) has become the de facto approach for aligning Large Vision-Language Models (LVLMs), it suffers from Likelihood Displacement, where the probability of both chosen and rejected responses collapses. This optimization flaw is especially detrimental in multimodal settings: the erosion of chosen likelihoods -- a failure we term Visual Anchor Collapse -- causes models to abandon visual evidence for strong language priors, precipitating significant hallucinatio...

---

### 22. dynActivation: A Trainable Activation Family for Adaptive Nonlinearity

**Authors:** Alois Bachmann

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22154v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22154v1)

**Summary:** This paper proposes $\mathrm{dynActivation}$, a per-layer trainable activation defined as $f_i(x) = \mathrm{BaseAct}(x)(α_i - β_i) + β_i x$, where $α_i$ and $β_i$ are lightweight learned scalars that interpolate between the base nonlinearity and a linear path and $\mathrm{BaseAct}(x)$ resembles any ReLU-like function. The static and dynamic ReLU-like variants are then compared across multiple vision tasks, language modeling tasks, and ablation studies. The results suggest that dynActivation vari...

---

### 23. Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation

**Authors:** Kejia Liu, Haoyang Zhou, Ruoyu Xu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22153v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22153v1)

**Summary:** Recent advances in cross-view geo-localization (CVGL) methods have shown strong potential for supporting unmanned aerial vehicle (UAV) navigation in GNSS-denied environments. However, existing work predominantly focuses on matching UAV views to onboard map tiles, which introduces an inherent trade-off between accuracy and storage overhead, and overlooks the importance of the UAV's heading during navigation. Moreover, the substantial discrepancies and varying overlaps in cross-view scenarios have...

---

### 24. OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation

**Authors:** Sijie Zhao, Feng Liu, Xueliang Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22148v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22148v1)

**Summary:** Earth Observation (EO) is essential for perceiving dynamic land surface changes, yet deploying autonomous EO in open environments is hindered by the immense diversity of multi-source data and heterogeneous tasks. While remote sensing agents have emerged to streamline EO workflows, existing tool-calling agents are confined to closed environments. They rely on pre-defined tools and are restricted to narrow scope, limiting their generalization to the diverse data and tasks. To overcome these limita...

---

### 25. DA-VAE: Plug-in Latent Compression for Diffusion via Detail Alignment

**Authors:** Xin Cai, Zhiyuan You, Zhoutong Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22125v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22125v1)

**Summary:** Reducing token count is crucial for efficient training and inference of latent diffusion models, especially at high resolution. A common strategy is to build high-compression image tokenizers with more channels per token. However, when trained only for reconstruction, high-dimensional latent spaces often lose meaningful structure, making diffusion training harder. Existing methods address this with extra objectives such as semantic alignment or selective dropout, but usually require costly diffu...

---

### 26. Biophysics-Enhanced Neural Representations for Patient-Specific Respiratory Motion Modeling

**Authors:** Jan Boysen, Hristina Uzunova, Heinz Handels, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22123v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22123v1)

**Summary:** A precise spatial delivery of the radiation dose is crucial for the treatment success in radiotherapy. In the lung and upper abdominal region, respiratory motion introduces significant treatment uncertainties, requiring special motion management techniques. To address this, respiratory motion models are commonly used to infer the patient-specific respiratory motion and target the dose more efficiently. In this work, we investigate the possibility of using implicit neural representations (INR) fo...

---

### 27. Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding

**Authors:** Yunzhuo Sun, Xinyue Liu, Yanyang Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22121v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22121v1)

**Summary:** Text-driven video moment retrieval (VMR) remains challenging due to limited capture of hidden temporal dynamics in untrimmed videos, leading to imprecise grounding in long sequences. Traditional methods rely on natural language queries (NLQs) or static image augmentations, overlooking motion sequences and suffering from high computational costs in Transformer-based architectures. Existing approaches fail to integrate subtitle contexts and generated temporal priors effectively, we therefore propo...

---

### 28. StreamingClaw Technical Report

**Authors:** Jiawei Chen, Zhe Chen, Chaoqun Du, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22120v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22120v1)

**Summary:** Applications such as embodied intelligence rely on a real-time perception-decision-action closed loop, posing stringent challenges for streaming video understanding. However, current agents suffer from fragmented capabilities, such as supporting only offline video understanding, lacking long-term multimodal memory mechanisms, or struggling to achieve real-time reasoning and proactive interaction under streaming inputs. These shortcomings have become a key bottleneck for preventing them from sust...

---

### 29. FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario

**Authors:** Hang Dai, Hongwei Fan, Han Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22102v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22102v1)

**Summary:** The increasing demand for augmented reality and robotics is driving the need for articulated object reconstruction with high scalability. However, existing settings for reconstructing from discrete articulation states or casual monocular videos require non-trivial axis alignment or suffer from insufficient coverage, limiting their applicability. In this paper, we introduce FreeArtGS, a novel method for reconstructing articulated objects under free-moving scenario, a new setting with a simple set...

---

### 30. Principled Steering via Null-space Projection for Jailbreak Defense in Vision-Language Models

**Authors:** Xingyu Zhu, Beier Zhu, Shuo Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22094v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22094v1)

**Summary:** As vision-language models (VLMs) are increasingly deployed in open-world scenarios, they can be easily induced by visual jailbreak attacks to generate harmful content, posing serious risks to model safety and trustworthy usage. Recent activation steering methods inject directional vectors into model activations during inference to induce refusal behaviors and have demonstrated effectiveness. However, a steering vector may both enhance refusal ability and cause over-refusal, thereby degrading mod...

---

### 31. P-Flow: Prompting Visual Effects Generation

**Authors:** Rui Zhao, Mike Zheng Shou

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22091v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22091v1)

**Summary:** Recent advancements in video generation models have significantly improved their ability to follow text prompts. However, the customization of dynamic visual effects, defined as temporally evolving and appearance-driven visual phenomena like object crushing or explosion, remains underexplored. Prior works on motion customization or control mainly focus on low-level motions of the subject or camera, which can be guided using explicit control signals such as motion trajectories. In contrast, dynam...

---

### 32. Adapting Point Cloud Analysis via Multimodal Bayesian Distribution Learning

**Authors:** Xingyu Zhu, Liang Yi, Shuo Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22070v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22070v1)

**Summary:** Multimodal 3D vision-language models show strong generalization across diverse 3D tasks, but their performance still degrades notably under domain shifts. This has motivated recent studies on test-time adaptation (TTA), which enables models to adapt online using test-time data. Among existing TTA methods, cache-based mechanisms are widely adopted for leveraging previously observed samples in online prediction refinement. However, they store only limited historical information, leading to progres...

---

### 33. SpatialBoost: Enhancing Visual Representation through Language-Guided Reasoning

**Authors:** Byungwoo Jeon, Dongyoung Kim, Huiwon Jang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22057v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22057v1)

**Summary:** Despite the remarkable success of large-scale pre-trained image representation models (i.e., vision encoders) across various vision tasks, they are predominantly trained on 2D image data and therefore often fail to capture 3D spatial relationships between objects and backgrounds in the real world, constraining their effectiveness in many downstream applications. To address this, we propose SpatialBoost, a scalable framework that enhances the spatial awareness of existing pre-trained vision encod...

---

### 34. FontCrafter: High-Fidelity Element-Driven Artistic Font Creation with Visual In-Context Generation

**Authors:** Wuyang Luo, Chengkai Tan, Chang Ge, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22054v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22054v1)

**Summary:** Artistic font generation aims to synthesize stylized glyphs based on a reference style. However, existing approaches suffer from limited style diversity and coarse control. In this work, we explore the potential of element-driven artistic font generation. Elements are the fundamental visual units of a font, serving as reference images for the desired style. Conceptually, we categorize elements into object elements (e.g., flowers or stones) with distinct structures and amorphous elements (e.g., f...

---

### 35. Uncertainty-guided Compositional Alignment with Part-to-Whole Semantic Representativeness in Hyperbolic Vision-Language Models

**Authors:** Hayeon Kim, Ji Ha Jang, Junghun James Kim, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22042v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22042v1)

**Summary:** While Vision-Language Models (VLMs) have achieved remarkable performance, their Euclidean embeddings remain limited in capturing hierarchical relationships such as part-to-whole or parent-child structures, and often face challenges in multi-object compositional scenarios. Hyperbolic VLMs mitigate this issue by better preserving hierarchical structures and modeling part-whole relations (i.e., whole scene and its part images) through entailment. However, existing approaches do not model that each ...

---

### 36. DTVI: Dual-Stage Textual and Visual Intervention for Safe Text-to-Image Generation

**Authors:** Binhong Tan, Zhaoxin Wang, Handing Wang

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22041v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22041v1)

**Summary:** Text-to-Image (T2I) diffusion models have demonstrated strong generation ability, but their potential to generate unsafe content raises significant safety concerns. Existing inference-time defense methods typically perform category-agnostic token-level intervention in the text embedding space, which fails to capture malicious semantics distributed across the full token sequence and remains vulnerable to adversarial prompts. In this paper, we propose DTVI, a dual-stage inference-time defense fram...

---

### 37. GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction

**Authors:** Youwen Yuan, Xi Zhao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22036v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22036v1)

**Summary:** Reconstructing translucent objects from multi-view images is a difficult problem. Previously, researchers have used differentiable path tracing and the neural implicit field, which require relatively large computational costs. Recently, many works have achieved good reconstruction results for opaque objects based on a 3DGS pipeline with much higher efficiency. However, such methods have difficulty dealing with translucent objects, because they do not consider the optical properties of translucen...

---

### 38. Tuning Real-World Image Restoration at Inference: A Test-Time Scaling Paradigm for Flow Matching Models

**Authors:** Purui Bai, Junxian Duan, Pin Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22027v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22027v1)

**Summary:** Although diffusion-based real-world image restoration (Real-IR) has achieved remarkable progress, efficiently leveraging ultra-large-scale pre-trained text-to-image (T2I) models and fully exploiting their potential remain significant challenges. To address this issue, we propose ResFlow-Tuner, an image restoration framework based on the state-of-the-art flow matching model, FLUX.1-dev, which integrates unified multi-modal fusion (UMMF) with test-time scaling (TTS) to achieve unprecedented restor...

---

### 39. 6D Robotic OCT Scanning of Curved Tissue Surfaces

**Authors:** Suresh Guttikonda, Maximilian Neidhardt, Vidas Raudonis, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22012v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22012v1)

**Summary:** Optical coherence tomography (OCT) is a non-invasive volumetric imaging modality with high spatial and temporal resolution. For imaging larger tissue structures, OCT probes need to be moved to scan the respective area. For handheld scanning, stitching of the acquired OCT volumes requires overlap to register the images. For robotic scanning and stitching, a typical approach is to restrict the motion to translations, as this avoids a full hand-eye calibration, which is complicated by the small fie...

---

### 40. SegMaFormer: A Hybrid State-Space and Transformer Model for Efficient Segmentation

**Authors:** Duy D. Nguyen, Phat T. Tran-Truong

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22002v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22002v1)

**Summary:** The advent of Transformer and Mamba-based architectures has significantly advanced 3D medical image segmentation by enabling global contextual modeling, a capability traditionally limited in Convolutional Neural Networks (CNNs). However, state-of-the-art Transformer models often entail substantial computational complexity and parameter counts, which is particularly prohibitive for volumetric data and further exacerbated by the limited availability of annotated medical imaging datasets. To addres...

---

### 41. STENet: Superpixel Token Enhancing Network for RGB-D Salient Object Detection

**Authors:** Jianlin Chen, Gongyang Li, Zhijiang Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21999v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21999v1)

**Summary:** Transformer-based methods for RGB-D Salient Object Detection (SOD) have gained significant interest, owing to the transformer's exceptional capacity to capture long-range pixel dependencies. Nevertheless, current RGB-D SOD methods face challenges, such as the quadratic complexity of the attention mechanism and the limited local detail extraction. To overcome these limitations, we propose a novel Superpixel Token Enhancing Network (STENet), which introduces superpixels into cross-modal interactio...

---

### 42. LRC-WeatherNet: LiDAR, RADAR, and Camera Fusion Network for Real-time Weather-type Classification in Autonomous Driving

**Authors:** Nour Alhuda Albashir, Lars Pernickel, Danial Hamoud, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21987v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21987v1)

**Summary:** Autonomous vehicles face major perception and navigation challenges in adverse weather such as rain, fog, and snow, which degrade the performance of LiDAR, RADAR, and RGB camera sensors. While each sensor type offers unique strengths, such as RADAR robustness in poor visibility and LiDAR precision in clear conditions, they also suffer distinct limitations when exposed to environmental obstructions. This study proposes LRC-WeatherNet, a novel multi-sensor fusion framework that integrates LiDAR, R...

---

### 43. Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model

**Authors:**  SII-GAIR, Sand. ai,  :, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21986v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21986v1)

**Summary:** We present daVinci-MagiHuman, an open-source audio-video generative foundation model for human-centric generation. daVinci-MagiHuman jointly generates synchronized video and audio using a single-stream Transformer that processes text, video, and audio within a unified token sequence via self-attention only. This single-stream design avoids the complexity of multi-stream or cross-attention architectures while remaining easy to optimize with standard training and inference infrastructure. The mode...

---

### 44. GeoFusion-CAD: Structure-Aware Diffusion with Geometric State Space for Parametric 3D Design

**Authors:** Xiaolei Zhou, Chuangjie Fang, Jie Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21978v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21978v1)

**Summary:** Parametric Computer-Aided Design (CAD) is fundamental to modern 3D modeling, yet existing methods struggle to generate long command sequences, especially under complex geometric and topological dependencies. Transformer-based architectures dominate CAD sequence generation due to their strong dependency modeling, but their quadratic attention cost and limited context windowing hinder scalability to long programs. We propose GeoFusion-CAD, an end-to-end diffusion framework for scalable and structu...

---

### 45. BHDD: A Burmese Handwritten Digit Dataset

**Authors:** Swan Htet Aung, Hein Htet, Htoo Say Wah Khaing, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21966v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21966v1)

**Summary:** We introduce the Burmese Handwritten Digit Dataset (BHDD), a collection of 87,561 grayscale images of handwritten Burmese digits in ten classes. Each image is 28x28 pixels, following the MNIST format. The training set has 60,000 samples split evenly across classes; the test set has 27,561 samples with class frequencies as they arose during collection. Over 150 people of different ages and backgrounds contributed samples. We analyze the dataset's class distribution, pixel statistics, and morpholo...

---

### 46. Unified Spatiotemporal Token Compression for Video-LLMs at Ultra-Low Retention

**Authors:** Junhao Du, Jialong Xue, Anqi Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21957v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21957v1)

**Summary:** Video large language models (Video-LLMs) face high computational costs due to large volumes of visual tokens. Existing token compression methods typically adopt a two-stage spatiotemporal compression strategy, relying on stage-specific metrics and an implicit assumption of spatiotemporal separability. Under extremely low retention ratios, however, such approaches often result in unbalanced allocation and loss of visual evidence essential for question answering. We reformulate token compression a...

---

### 47. Group3D: MLLM-Driven Semantic Grouping for Open-Vocabulary 3D Object Detection

**Authors:** Youbin Kim, Jinho Park, Hogun Park, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21944v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21944v1)

**Summary:** Open-vocabulary 3D object detection aims to localize and recognize objects beyond a fixed training taxonomy. In multi-view RGB settings, recent approaches often decouple geometry-based instance construction from semantic labeling, generating class-agnostic fragments and assigning open-vocabulary categories post hoc. While flexible, such decoupling leaves instance construction governed primarily by geometric consistency, without semantic constraints during merging. When geometric evidence is view...

---

### 48. GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction

**Authors:** Ayesh Abu Lehyeh, Xiaohan Zhang, Ahmad Arrabi, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21943v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21943v1)

**Summary:** Accurate and fast localization is vital for safe autonomous navigation in GPS-denied areas. Fine-Grained Cross-View Geolocalization (FG-CVG) aims to estimate the precise 2-Degree-of-Freedom (2-DoF) location of a ground image relative to a satellite image. However, current methods force a difficult trade-off, with high-accuracy models being slow for real-time use. In this paper, we introduce GeoFlow, a new approach that offers a lightweight and highly efficient framework that breaks this accuracy...

---

### 49. FeatDistill: A Feature Distillation Enhanced Multi-Expert Ensemble Framework for Robust AI-generated Image Detection

**Authors:** Zhilin Tu, Kemou Li, Fengpeng Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21939v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21939v1)

**Summary:** The rapid iteration and widespread dissemination of deepfake technology have posed severe challenges to information security, making robust and generalizable detection of AI-generated forged images increasingly important. In this paper, we propose FeatDistill, an AI-generated image detection framework that integrates feature distillation with a multi-expert ensemble, developed for the NTIRE Challenge on Robust AI-Generated Image Detection in the Wild. The framework explicitly targets three pract...

---

### 50. MultiBind: A Benchmark for Attribute Misbinding in Multi-Subject Generation

**Authors:** Wenqing Tian, Hanyi Mao, Zhaocheng Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21937v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21937v1)

**Summary:** Subject-driven image generation is increasingly expected to support fine-grained control over multiple entities within a single image. In multi-reference workflows, users may provide several subject images, a background reference, and long, entity-indexed prompts to control multiple people within one scene. In this setting, a key failure mode is cross-subject attribute misbinding: attributes are preserved, edited, or transferred to the wrong subject. Existing benchmarks and metrics largely empha...

---

## cs.LG

**50 papers**

### 1. WorldCache: Content-Aware Caching for Accelerated Video World Models

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22286v1)

**Summary:** Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

---

### 2. End-to-End Training for Unified Tokenization and Latent Denoising

**Authors:** Shivam Duggal, Xingjian Bai, Zongze Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22283v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22283v1)

**Summary:** Latent diffusion models (LDMs) enable high-fidelity synthesis by operating in learned latent spaces. However, training state-of-the-art LDMs requires complex staging: a tokenizer must be trained first, before the diffusion model can be trained in the frozen latent space. We propose UNITE - an autoencoder architecture for unified tokenization and latent diffusion. UNITE consists of a Generative Encoder that serves as both image tokenizer and latent generator via weight sharing. Our key insight is...

---

### 3. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22281v1)

**Summary:** Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning ove...

---

### 4. The Dual Mechanisms of Spatial Reasoning in Vision-Language Models

**Authors:** Kelly Cui, Nikhil Prakash, Ayush Raina, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22278v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22278v1)

**Summary:** Many multimodal tasks, such as image captioning and visual question answering, require vision-language models (VLMs) to associate objects with their properties and spatial relations. Yet it remains unclear where and how such associations are computed within VLMs. In this work, we show that VLMs rely on two concurrent mechanisms to represent such associations. In the language model backbone, intermediate layers represent content-independent spatial relations on top of visual tokens corresponding ...

---

### 5. Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels

**Authors:** Alexandra Zelenin, Alexandra Zhuravlyova

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22276v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22276v1)

**Summary:** Weight-Decomposed Low-Rank Adaptation (DoRA) extends LoRA by decoupling weight magnitude from direction, but its forward pass requires the row-wise norm of W + sBA, a computation that every major framework we surveyed implements by materializing the dense [d_out, d_in] product BA. At d_in = 8192 and rank r = 384, a single module's norm requires about 512 MB of transient working memory in bf16, making high-rank DoRA costly and often infeasible on common single-GPU setups once hundreds of adapted ...

---

### 6. Decoupling Exploration and Policy Optimization: Uncertainty Guided Tree Search for Hard Exploration

**Authors:** Zakaria Mhammedi, James Cohan

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22273v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22273v1)

**Summary:** The process of discovery requires active exploration -- the act of collecting new and informative data. However, efficient autonomous exploration remains a major unsolved problem. The dominant paradigm addresses this challenge by using Reinforcement Learning (RL) to train agents with intrinsic motivation, maximizing a composite objective of extrinsic and intrinsic rewards. We suggest that this approach incurs unnecessary overhead: while policy optimization is necessary for precise task execution...

---

### 7. Characterizing High-Capacity Janus Aminobenzene-Graphene Anode for Sodium-Ion Batteries with Machine Learning

**Authors:** Claudia Islas-Vargas, L. Ricardo Montoya, Carlos A. Vital-José, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22254v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22254v1)

**Summary:** Sodium-ion batteries require anodes that combine high capacity, low operating voltage, fast Na-ion transport, and mechanical stability, which conventional anodes struggle to deliver. Here, we use the SpookyNet machine-learning force field (MLFF) together with all-electron density-functional theory calculations to characterize Na storage in aminobenzene-functionalized Janus graphene (Na$_x$AB) at room-temperature. Simulations across state of charge reveal a three-stage storage mechanism-site-spec...

---

### 8. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

**Authors:** Changxiao Cai, Gen Li

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22248v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22248v1)

**Summary:** Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, ...

---

### 9. ShapDBM: Exploring Decision Boundary Maps in Shapley Space

**Authors:** Luke Watkin, Daniel Archambault, Alex Telea

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22235v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22235v1)

**Summary:** Decision Boundary Maps (DBMs) are an effective tool for visualising machine learning classification boundaries. Yet, DBM quality strongly depends on the dimensionality reduction (DR) technique and high dimensional space used for the data points. For complex ML datasets, DR can create many mixed classes which, in turn, yield DBMs that are hard to use. We propose a new technique to compute DBMs by transforming data space into Shapley space and computing DR on it. Compared to standard DBMs computed...

---

### 10. One Model, Two Markets: Bid-Aware Generative Recommendation

**Authors:** Yanchen Jiang, Zhe Feng, Christopher P. Mah, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22231v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22231v1)

**Summary:** Generative Recommender Systems using semantic ids, such as TIGER (Rajput et al., 2023), have emerged as a widely adopted competitive paradigm in sequential recommendation. However, existing architectures are designed solely for semantic retrieval and do not address concerns such as monetization via ad revenue and incorporation of bids for commercial retrieval. We propose GEM-Rec, a unified framework that integrates commercial relevance and monetization objectives directly into the generative seq...

---

### 11. Noise Titration: Exact Distributional Benchmarking for Probabilistic Time Series Forecasting

**Authors:** Qilin Wang

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22219v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22219v1)

**Summary:** Modern time series forecasting is evaluated almost entirely through passive observation of single historical trajectories, rendering claims about a model's robustness to non-stationarity fundamentally unfalsifiable. We propose a paradigm shift toward interventionist, exact-statistical benchmarking. By systematically titrating calibrated Gaussian observation noise into known chaotic and stochastic dynamical systems, we transform forecasting from a black-box sequence matching game into an exact di...

---

### 12. Gumbel Distillation for Parallel Text Generation

**Authors:** Chi Zhang, Xixi Hu, Bo Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22216v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22216v1)

**Summary:** The slow, sequential nature of autoregressive (AR) language models has driven the adoption of parallel decoding methods. However, these non-AR models often sacrifice generation quality as they struggle to model the complex joint distribution of token sequences. To narrow this performance gap, we introduce Gumbel Distillation, a novel distillation technique that enables parallel decoders to learn this distribution effectively. Our method leverages the Gumbel-Max trick to create a deterministic ma...

---

### 13. Evaluating the Reliability and Fidelity of Automated Judgment Systems of Large Language Models

**Authors:** Tom Biskupski, Stephan Kleber

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22214v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22214v1)

**Summary:** A Large Language Model (LLM) as judge evaluates the quality of victim Machine Learning (ML) models, specifically LLMs, by analyzing their outputs. An LLM as judge is the combination of one model and one specifically engineered judge prompt that contains the criteria for the analysis. The resulting automation of the analysis scales up the complex evaluation of the victim models' free-form text outputs by faster and more consistent judgments compared to human reviewers. Thus, quality and security ...

---

### 14. SPA: A Simple but Tough-to-Beat Baseline for Knowledge Injection

**Authors:** Kexian Tang, Jiani Wang, Shaowen Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22213v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22213v1)

**Summary:** While large language models (LLMs) are pretrained on massive amounts of data, their knowledge coverage remains incomplete in specialized, data-scarce domains, motivating extensive efforts to study synthetic data generation for knowledge injection. We propose SPA (Scaling Prompt-engineered Augmentation), a simple but tough-to-beat baseline that uses a small set of carefully designed prompts to generate large-scale synthetic data for knowledge injection. Through systematic comparisons, we find tha...

---

### 15. Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs

**Authors:** Kangqi Ni, Wenyue Hua, Xiaoxiang Shi, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22206v1)

**Summary:** Multi-agent applications often execute complex tasks as multi-stage workflows, where each stage is an LLM call whose output becomes part of context for subsequent steps. Existing LLM serving systems largely assume homogeneous clusters with identical model replicas. This design overlooks the potential of heterogeneous deployments, where models of different sizes and capabilities enable finer trade-offs between latency and performance. However, heterogeneity introduces new challenges in scheduling...

---

### 16. CayleyPy-4: AI-Holography. Towards analogs of holographic string dualities for AI tasks

**Authors:** A. Chervov, F. Levkovich-Maslyuk, A. Smolensky, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22195v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22195v1)

**Summary:** This is the fourth paper in the CayleyPy project, which applies AI methods to the exploration of large graphs. In this work, we suggest the existence of a new discrete version of holographic string dualities for this setup, and discuss their relevance to AI systems and mathematics. Many modern AI tasks -- such as those addressed by GPT-style language models or RL systems -- can be viewed as direct analogues of predicting particle trajectories on graphs. We investigate this problem for a large fa...

---

### 17. Revisiting Quantum Code Generation: Where Should Domain Knowledge Live?

**Authors:** Oscar Novo, Oscar Bastidas-Jossa, Alberto Calvo, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22184v1)

**Summary:** Recent advances in large language models (LLMs) have enabled the automation of an increasing number of programming tasks, including code generation for scientific and engineering domains. In rapidly evolving software ecosystems such as quantum software development, where frameworks expose complex abstractions, a central question is how best to incorporate domain knowledge into LLM-based assistants while preserving maintainability as libraries evolve.   In this work, we study specialization strat...

---

### 18. Calibeating Made Simple

**Authors:** Yurong Chen, Zhiyi Huang, Michael I. Jordan, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22167v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22167v1)

**Summary:** We study calibeating, the problem of post-processing external forecasts online to minimize cumulative losses and match an informativeness-based benchmark. Unlike prior work, which analyzed calibeating for specific losses with specific arguments, we reduce calibeating to existing online learning techniques and obtain results for general proper losses. More concretely, we first show that calibeating is minimax-equivalent to regret minimization. This recovers the $O(\log T)$ calibeating rate of Fos...

---

### 19. Causal Evidence that Language Models use Confidence to Drive Behavior

**Authors:** Dharshan Kumaran, Nathaniel Daw, Simon Osindero, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22161v1)

**Summary:** Metacognition -- the ability to assess one's own cognitive performance -- is documented across species, with internal confidence estimates serving as a key signal for adaptive behavior. While confidence can be extracted from Large Language Model (LLM) outputs, whether models actively use these signals to regulate behavior remains a fundamental question. We investigate this through a four-phase abstention paradigm.Phase 1 established internal confidence estimates in the absence of an abstention o...

---

### 20. Data Curation for Machine Learning Interatomic Potentials by Determinantal Point Processes

**Authors:** Joanna Zou, Youssef Marzouk

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22160v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22160v1)

**Summary:** The development of machine learning interatomic potentials faces a critical computational bottleneck with the generation and labeling of useful training datasets. We present a novel application of determinantal point processes (DPPs) to the task of selecting informative subsets of atomic configurations to label with reference energies and forces from costly quantum mechanical methods. Through experiments with hafnium oxide data, we show that DPPs are competitive with existing approaches to const...

---

### 21. Multimodal Survival Analysis with Locally Deployable Large Language Models

**Authors:** Moritz Gögl, Christopher Yau

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22158v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22158v1)

**Summary:** We study multimodal survival analysis integrating clinical text, tabular covariates, and genomic profiles using locally deployable large language models (LLMs). As many institutions face tight computational and privacy constraints, this setting motivates the use of lightweight, on-premises models. Our approach jointly estimates calibrated survival probabilities and generates concise, evidence-grounded prognosis text via teacher-student distillation and principled multimodal fusion. On a TCGA coh...

---

### 22. RAMPAGE: RAndomized Mid-Point for debiAsed Gradient Extrapolation

**Authors:** Abolfazl Hashemi

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22155v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22155v1)

**Summary:** A celebrated method for Variational Inequalities (VIs) is Extragradient (EG), which can be viewed as a standard discrete-time integration scheme. With this view in mind, in this paper we show that EG may suffer from discretization bias when applied to non-linear vector fields, conservative or otherwise. To resolve this discretization shortcoming, we introduce RAndomized Mid-Point for debiAsed Gradient Extrapolation (RAMPAGE) and its variance-reduced counterpart, RAMPAGE+ which leverages antithet...

---

### 23. dynActivation: A Trainable Activation Family for Adaptive Nonlinearity

**Authors:** Alois Bachmann

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22154v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22154v1)

**Summary:** This paper proposes $\mathrm{dynActivation}$, a per-layer trainable activation defined as $f_i(x) = \mathrm{BaseAct}(x)(α_i - β_i) + β_i x$, where $α_i$ and $β_i$ are lightweight learned scalars that interpolate between the base nonlinearity and a linear path and $\mathrm{BaseAct}(x)$ resembles any ReLU-like function. The static and dynamic ReLU-like variants are then compared across multiple vision tasks, language modeling tasks, and ablation studies. The results suggest that dynActivation vari...

---

### 24. Computationally lightweight classifiers with frequentist bounds on predictions

**Authors:** Shreeram Murali, Cristian R. Rojas, Dominik Baumann

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22128v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22128v1)

**Summary:** While both classical and neural network classifiers can achieve high accuracy, they fall short on offering uncertainty bounds on their predictions, making them unfit for safety-critical applications. Existing kernel-based classifiers that provide such bounds scale with $\mathcal O (n^{\sim3})$ in time, making them computationally intractable for large datasets. To address this, we propose a novel, computationally efficient classification algorithm based on the Nadaraya-Watson estimator, for whos...

---

### 25. On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation

**Authors:** Kexin Huang, Haoming Meng, Junkang Wu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22117v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22117v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning capabilities of large language models. While existing analyses identify that RLVR-induced changes are sparse, they primarily focus on the \textbf{magnitude} of these updates, largely overlooking their \textbf{direction}. In this work, we argue that the direction of updates is a more critical lens for understanding RLVR's effects, which can be captured by the signed, token-level log probability differen...

---

### 26. SpecTM: Spectral Targeted Masking for Trustworthy Foundation Models

**Authors:** Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22097v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22097v1)

**Summary:** Foundation models are now increasingly being developed for Earth observation (EO), yet they often rely on stochastic masking that do not explicitly enforce physics constraints; a critical trustworthiness limitation, in particular for predictive models that guide public health decisions. In this work, we propose SpecTM (Spectral Targeted Masking), a physics-informed masking design that encourages the reconstruction of targeted bands from cross-spectral context during pretraining. To achieve this,...

---

### 27. MIHT: A Hoeffding Tree for Time Series Classification using Multiple Instance Learning

**Authors:** Aurora Esteban, Amelia Zafra, Sebastián Ventura

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22074v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22074v1)

**Summary:** Due to the prevalence of temporal data and its inherent dependencies in many real-world problems, time series classification is of paramount importance in various domains. However, existing models often struggle with series of variable length or high dimensionality. This paper introduces the MIHT (Multi-instance Hoeffding Tree) algorithm, an efficient model that uses multi-instance learning to classify multivariate and variable-length time series while providing interpretable results. The algori...

---

### 28. On the Failure of Topic-Matched Contrast Baselines in Multi-Directional Refusal Abliteration

**Authors:** Valentin Petrov

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22061v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22061v1)

**Summary:** Inasmuch as the removal of refusal behavior from instruction-tuned language models by directional abliteration requires the extraction of refusal-mediating directions from the residual stream activation space, and inasmuch as the construction of the contrast baseline against which harmful prompt activations are compared has been treated in the existing literature as an implementation detail rather than a methodological concern, the present work investigates whether a topically matched contrast b...

---

### 29. AnimalCLAP: Taxonomy-Aware Language-Audio Pretraining for Species Recognition and Trait Inference

**Authors:** Risa Shinoda, Kaede Shiohara, Nakamasa Inoue, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22053v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22053v1)

**Summary:** Animal vocalizations provide crucial insights for wildlife assessment, particularly in complex environments such as forests, aiding species identification and ecological monitoring. Recent advances in deep learning have enabled automatic species classification from their vocalizations. However, classifying species unseen during training remains challenging. To address this limitation, we introduce AnimalCLAP, a taxonomy-aware language-audio framework comprising a new dataset and model that incor...

---

### 30. MAGPI: Multifidelity-Augmented Gaussian Process Inputs for Surrogate Modeling from Scarce Data

**Authors:** Atticus Rex, Elizabeth Qian, David Peterson

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22050v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22050v1)

**Summary:** Supervised machine learning describes the practice of fitting a parameterized model to labeled input-output data. Supervised machine learning methods have demonstrated promise in learning efficient surrogate models that can (partially) replace expensive high-fidelity models, making many-query analyses, such as optimization, uncertainty quantification, and inference, tractable. However, when training data must be obtained through the evaluation of an expensive model or experiment, the amount of t...

---

### 31. RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning

**Authors:** Dong Heon Cho, Boyuan Chen

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22039v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22039v1)

**Summary:** Differentiable simulators enable gradient-based optimization of soft robots over material parameters, control, and morphology, but accurately modeling real systems remains challenging due to the sim-to-real gap. This issue becomes more pronounced when geometry is itself a design variable. System identification reduces discrepancies by fitting global material parameters to data; however, when constitutive models are misspecified or observations are sparse, identified parameters often absorb geome...

---

### 32. On the Interplay of Priors and Overparametrization in Bayesian Neural Network Posteriors

**Authors:** Julius Kobialka, Emanuel Sommer, Chris Kolb, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22030v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22030v1)

**Summary:** Bayesian neural network (BNN) posteriors are often considered impractical for inference, as symmetries fragment them, non-identifiabilities inflate dimensionality, and weight-space priors are seen as meaningless. In this work, we study how overparametrization and priors together reshape BNN posteriors and derive implications allowing us to better understand their interplay. We show that redundancy introduces three key phenomena that fundamentally reshape the posterior geometry: balancedness, wei...

---

### 33. Do Papers Match Code? A Benchmark and Framework for Paper-Code Consistency Detection in Bioinformatics Software

**Authors:** Tianxiang Xu, Xiaoyan Zhu, Xin Lai, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22018v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22018v1)

**Summary:** Ensuring consistency between research papers and their corresponding software implementations is fundamental to software reliability and scientific reproducibility. However, this problem remains underexplored, particularly in the domain of bioinformatics, where discrepancies between methodological descriptions in papers and their actual code implementations are prevalent. To address this gap, this paper introduces a new task, namely paper-code consistency detection, and curates a collection of 4...

---

### 34. AdditiveLLM2: A Multi-modal Large Language Model for Additive Manufacturing

**Authors:** Peter Pak, Amir Barati Farimani

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22017v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22017v1)

**Summary:** This work presents AdditiveLLM2 a multi-modal, domain adapted large language model built upon the instruction tuned variant of the Gemma 3 model using a relatively small dataset of around 50 million tokens. The dataset (AdditiveLLM2-OA) consists of open-access additive manufacturing journal articles with data extracted for the domain adaptive pretraining and visual instruction tuning processes. Various stages of the developed model are evaluated with the Additive-Manufacturing-Benchmark which co...

---

### 35. ROM: Real-time Overthinking Mitigation via Streaming Detection and Intervention

**Authors:** Xinyan Wang, Xiaogeng Liu, Chaowei Xiao

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22016v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22016v1)

**Summary:** Large Reasoning Models (LRMs) achieve strong accuracy on challenging tasks by generating long Chain-of-Thought traces, but suffer from overthinking. Even after reaching the correct answer, they continue generating redundant reasoning steps. This behavior increases latency and compute cost and can also lead to answer drift. Existing mitigation methods either require training-heavy backbone modification or rely on hand-crafted heuristics that do not truly capture overthinking patterns. We propose ...

---

### 36. A plug-and-play approach with fast uncertainty quantification for weak lensing mass mapping

**Authors:** Hubert Leterme, Andreas Tersenov, Jalal Fadili, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22006v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22006v1)

**Summary:** Upcoming stage-IV surveys such as Euclid and Rubin will deliver vast amounts of high-precision data, opening new opportunities to constrain cosmological models with unprecedented accuracy. A key step in this process is the reconstruction of the dark matter distribution from noisy weak lensing shear measurements.   Current deep learning-based mass mapping methods achieve high reconstruction accuracy, but either require retraining a model for each new observed sky region (limiting practicality) or...

---

### 37. CRPS-Optimal Binning for Conformal Regression

**Authors:** Paolo Toccaceli

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22000v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22000v1)

**Summary:** We propose a method for non-parametric conditional distribution estimation based on partitioning covariate-sorted observations into contiguous bins and using the within-bin empirical CDF as the predictive distribution. Bin boundaries are chosen to minimise the total leave-one-out Continuous Ranked Probability Score (LOO-CRPS), which admits a closed-form cost function with $O(n^2 \log n)$ precomputation and $O(n^2)$ storage; the globally optimal $K$-partition is recovered by a dynamic programme i...

---

### 38. λ-GELU: Learning Gating Hardness for Controlled ReLU-ization in Deep Networks

**Authors:** Cristian Pérez-Corral, Alberto Fernández-Hernández, Jose I. Mestre, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21991v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21991v1)

**Summary:** Gaussian Error Linear Unit (GELU) is a widely used smooth alternative to Rectifier Linear Unit (ReLU), yet many deployment, compression, and analysis toolchains are most naturally expressed for piecewise-linear (ReLU-type) networks. We study a hardness-parameterized formulation of GELU, f(x;λ)=xΦ(λ x), where Φ is the Gaussian CDF and λ \in [1, infty) controls gate sharpness, with the goal of turning smooth gated training into a controlled path toward ReLU-compatible models. Learning λ is non-tri...

---

### 39. TREX: Trajectory Explanations for Multi-Objective Reinforcement Learning

**Authors:** Dilina Rajapakse, Juan C. Rosero, Ivana Dusparic

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21988v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21988v1)

**Summary:** Reinforcement Learning (RL) has demonstrated its ability to solve complex decision-making problems in a variety of domains, by optimizing reward signals obtained through interaction with an environment. However, many real-world scenarios involve multiple, potentially conflicting objectives that cannot be easily represented by a single scalar reward. Multi-Objective Reinforcement Learning (MORL) addresses this limitation by enabling agents to optimize several objectives simultaneously, explicitly...

---

### 40. BOOST-RPF: Boosted Sequential Trees for Radial Power Flow

**Authors:** Ehimare Okoyomon, Christoph Goebel

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21977v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21977v1)

**Summary:** Accurate power flow analysis is critical for modern distribution systems, yet classical solvers face scalability issues, and current machine learning models often struggle with generalization. We introduce BOOST-RPF, a novel method that reformulates voltage prediction from a global graph regression task into a sequential path-based learning problem. By decomposing radial networks into root-to-leaf paths, we leverage gradient-boosted decision trees (XGBoost) to model local voltage-drop regulariti...

---

### 41. SecureBreak -- A dataset towards safe and secure models

**Authors:** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21975v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21975v1)

**Summary:** Large language models are becoming pervasive core components in many real-world applications. As a consequence, security alignment represents a critical requirement for their safe deployment. Although previous related works focused primarily on model architectures and alignment methodologies, these approaches alone cannot ensure the complete elimination of harmful generations. This concern is reinforced by the growing body of scientific literature showing that attacks, such as jailbreaking and p...

---

### 42. Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe

**Authors:** Xixi Wu, Qianguo Sun, Ruiyang Zhang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21972v1)

**Summary:** Reinforcement Learning (RL) is essential for evolving Large Language Models (LLMs) into autonomous agents capable of long-horizon planning, yet a practical recipe for scaling RL in complex, multi-turn environments remains elusive. This paper presents a systematic empirical study using TravelPlanner, a challenging testbed requiring tool orchestration to satisfy multifaceted constraints. We decompose the agentic RL design space along 5 axes: reward shaping, model scaling, data composition, algorit...

---

### 43. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

**Authors:** Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21933v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21933v1)

**Summary:** The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training ...

---

### 44. The Golden Subspace: Where Efficiency Meets Generalization in Continual Test-Time Adaptation

**Authors:** Guannan Lai, Da-Wei Zhou, Zhenguo Li, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21928v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21928v1)

**Summary:** Continual Test-Time Adaptation (CTTA) aims to enable models to adapt online to unlabeled data streams under distribution shift without accessing source data. Existing CTTA methods face an efficiency-generalization trade-off: updating more parameters improves adaptation but severely reduces online inference efficiency. An ideal solution is to achieve comparable adaptation with minimal feature updates; we call this minimal subspace the golden subspace. We prove its existence in a single-step adapt...

---

### 45. Deep Reinforcement Learning and The Tale of Two Temporal Difference Errors

**Authors:** Juan Sebastian Rojas, Chi-Guhn Lee

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21921v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21921v1)

**Summary:** The temporal difference (TD) error was first formalized in Sutton (1988), where it was first characterized as the difference between temporally successive predictions, and later, in that same work, formulated as the difference between a bootstrapped target and a prediction. Since then, these two interpretations of the TD error have been used interchangeably in the literature, with the latter eventually being adopted as the standard critic loss in deep reinforcement learning (RL) architectures. I...

---

### 46. Structural Concentration in Weighted Networks: A Class of Topology-Aware Indices

**Authors:** L. Riso, M. G. Zoia

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21918v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21918v1)

**Summary:** This paper develops a unified framework for measuring concentration in weighted systems embedded in networks of interactions. While traditional indices such as the Herfindahl-Hirschman Index capture dispersion in weights, they neglect the topology of relationships among the elements receiving those weights. To address this limitation, we introduce a family of topology-aware concentration indices that jointly account for weight distributions and network structure. At the core of the framework lie...

---

### 47. A Latent Representation Learning Framework for Hyperspectral Image Emulation in Remote Sensing

**Authors:** Chedly Ben Azizi, Claire Guilloteau, Gilles Roussel, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21911v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21911v1)

**Summary:** Synthetic hyperspectral image (HSI) generation is essential for large-scale simulation, algorithm development, and mission design, yet traditional radiative transfer models remain computationally expensive and often limited to spectrum-level outputs. In this work, we propose a latent representation-based framework for hyperspectral emulation that learns a latent generative representation of hyperspectral data. The proposed approach supports both spectrum-level and spatial-spectral emulation and ...

---

### 48. A Novel Method for Enforcing Exactly Dirichlet, Neumann and Robin Conditions on Curved Domain Boundaries for Physics Informed Machine Learning

**Authors:** Suchuan Dong, Yuchuan Zhang

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21909v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21909v1)

**Summary:** We present a systematic method for exactly enforcing Dirichlet, Neumann, and Robin type conditions on general quadrilateral domains with arbitrary curved boundaries. Our method is built upon exact mappings between general quadrilateral domains and the standard domain, and employs a combination of TFC (theory of functional connections) constrained expressions and transfinite interpolations. When Neumann or Robin boundaries are present, especially when two Neumann (or Robin) boundaries meet at a v...

---

### 49. SparseDVFS: Sparse-Aware DVFS for Energy-Efficient Edge Inference

**Authors:** Ziyang Zhang, Zheshun Wu, Jie Liu, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21908v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21908v1)

**Summary:** Deploying deep neural networks (DNNs) on power-sensitive edge devices presents a formidable challenge. While Dynamic Voltage and Frequency Scaling (DVFS) is widely employed for energy optimization, traditional model-level scaling is often too coarse to capture intra-inference variations, whereas fine-grained operator-level scaling suffers from prohibitive performance degradation due to significant hardware switching latency. This paper presents SparseDVFS, a fine-grained, sparse-aware DVFS frame...

---

### 50. Not All Layers Are Created Equal: Adaptive LoRA Ranks for Personalized Image Generation

**Authors:** Donald Shenaj, Federico Errica, Antonio Carta

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21884v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21884v1)

**Summary:** Low Rank Adaptation (LoRA) is the de facto fine-tuning strategy to generate personalized images from pre-trained diffusion models. Choosing a good rank is extremely critical, since it trades off performance and memory consumption, but today the decision is often left to the community's consensus, regardless of the personalized subject's complexity. The reason is evident: the cost of selecting a good rank for each LoRA component is combinatorial, so we opt for practical shortcuts such as fixing t...

---

## cs.NE

**50 papers**

### 1. PreferRec: Learning and Transferring Pareto Preferences for Multi-objective Re-ranking

**Authors:** Wei Zhou, Wuyang Li, Junkai Ji, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22073v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22073v1)

**Summary:** Multi-objective re-ranking has become a critical component of modern multi-stage recommender systems, as it tasked to balance multiple conflicting objectives such as accuracy, diversity, and fairness. Existing multi-objective re-ranking methods typically optimize aggregate objectives at the item level using static or handcrafted preference weights. This design overlooks that users inherently exhibit Pareto-optimal preferences at the intent level, reflecting personalized trade-offs among objectiv...

---

### 2. Optimal Memory Encoding Through Fluctuation-Response Structure

**Authors:** Lianxiang Cui, Kohei Nakajima, Kazuyuki Aihara

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21666v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21666v1)

**Summary:** Physical reservoir computing exploits the intrinsic dynamics of physical systems for information processing, while keeping the internal dynamics fixed and training only linear readouts; yet the role of input encoding remains poorly understood. We show that optimal input encoding is a geometric problem governed by the system's fluctuation-response structure. By measuring steady-state fluctuations and linear response, we derive an analytical criterion for the input direction that maximizes task-sp...

---

### 3. Evolutionary Biparty Multiobjective UAV Path Planning: Problems and Empirical Comparisons

**Authors:** Kesheng Chen, Wenjian Luo, Xin Lin, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21544v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21544v1)

**Summary:** Unmanned aerial vehicles (UAVs) have been widely used in urban missions, and proper planning of UAV paths can improve mission efficiency while reducing the risk of potential third-party impact. Existing work has considered all efficiency and safety objectives for a single decision-maker (DM) and regarded this as a multiobjective optimization problem (MOP). However, there is usually not a single DM but two DMs, i.e., an efficiency DM and a safety DM, and the DMs are only concerned with their resp...

---

### 4. Compressive single-pixel imaging via a wavelength-multiplexed spatially incoherent diffractive optical processor

**Authors:** Xiao Wang, Yiyang Wu, Yuntian Wang, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21456v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21456v1)

**Summary:** Despite offering high sensitivity, a high signal-to-noise ratio, and a broad spectral range, single-pixel imaging (SPI) is limited by low measurement efficiency and long data-acquisition times. To address this, we propose a wavelength-multiplexed, spatially incoherent diffractive optical processor combined with a compact/shallow digital artificial neural network (ANN) to implement compressive SPI. Specifically, we model the bucket detection process in conventional SPI as a linear intensity trans...

---

### 5. Elite Lanes: Evolutionary Generation of Realistic Small-Scale Road Networks

**Authors:** Artur Morys-Magiera, Marek Długosz, Paweł Skruch

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20964v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20964v1)

**Summary:** We present a comparative study of methods for generating realistic, constrained small- to medium-scale road networks with built-in redundancy. In this research, we evaluate the proposed Evolutionary Algorithm (EA) with connectivity and redundancy constraints against the Wave Function Collapse (WFC) method - commonly used in procedural terrain generation for games - and swarm algorithms: Particle Swarm (PSO) and Gray Wolf (GWO). Our focus is on producing realistic, redundant road networks suitabl...

---

### 6. MOELIGA: a multi-objective evolutionary approach for feature selection with local improvement

**Authors:** Leandro Vignolo, Matias Gerard

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20934v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20934v1)

**Summary:** Selecting the most relevant or informative features is a key issue in actual machine learning problems. Since an exhaustive search is not feasible even for a moderate number of features, an intelligent search strategy must be employed for finding an optimal subset, which implies considering how features interact with each other in promoting class separability. Balancing feature subset size and classification accuracy constitutes a multi-objective optimization challenge. Here we propose MOELIGA, ...

---

### 7. Semantic Sections: An Atlas-Native Feature Ontology for Obstructed Representation Spaces

**Authors:** Hossein Javidnia

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20867v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20867v1)

**Summary:** Recent interpretability work often treats a feature as a single global direction, dictionary atom, or latent coordinate shared across contexts. We argue that this ontology can fail in obstructed representation spaces, where locally coherent meanings need not assemble into one globally consistent feature. We introduce an atlas-native replacement object, the semantic section: a transport-compatible family of local feature representatives defined over a context atlas. We formalize semantic sections...

---

### 8. Decoupling Numerical and Structural Parameters: An Empirical Study on Adaptive Genetic Algorithms via Deep Reinforcement Learning for the Large-Scale TSP

**Authors:** Hongyu Wang, Yuhan Jing, Yibing Shi, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20702v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20702v1)

**Summary:** Proper parameter configuration is a prerequisite for the success of Evolutionary Algorithms (EAs). While various adaptive strategies have been proposed, it remains an open question whether all control dimensions contribute equally to algorithmic scalability. To investigate this, we categorize control variables into numerical parameters (e.g., crossover and mutation rates) and structural parameters (e.g., population size and operator switching), hypothesizing that they play distinct roles. This p...

---

### 9. A Unified Phase-native Computational Principle Governs Hippocampal Spike Timing and Neural Coding

**Authors:** Reza Ahmadvand, Sara Safura Sharif, Yaser Mike Banad

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19690v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19690v1)

**Summary:** Hippocampal neurons exhibit precise phase locking to network oscillations, but the computational principle governing this temporal precision is still unclear. Neural information is conveyed jointly by firing rates and spike timing, but existing models treat these dimensions separately, limiting mechanistic interpretation of spike-field coupling and its reported association with spectral features such as the aperiodic slope. Here we show that hippocampal phase locking emerges from a fundamental d...

---

### 10. Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement

**Authors:** Quilee Simeon

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18497v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18497v1)

**Summary:** Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. We present a covariance-based method for estimating the weight matrix of a recurrent neural network from sparse, partial measurements across multiple recording sessions. By accumulating pairwise covariance estimates across sessions where different subsets of neurons are observed, we reconstruct the full connectivity matrix without requiring simultaneous recording of all neurons....

---

### 11. ALIGN: Adversarial Learning for Generalizable Speech Neuroprosthesis

**Authors:** Zhanqi Zhang, Shun Li, Bernardo L. Sabatini, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18299v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18299v1)

**Summary:** Intracortical brain-computer interfaces (BCIs) can decode speech from neural activity with high accuracy when trained on data pooled across recording sessions. In realistic deployment, however, models must generalize to new sessions without labeled data, and performance often degrades due to cross-session nonstationarities (e.g., electrode shifts, neural turnover, and changes in user strategy). In this paper, we propose ALIGN, a session-invariant learning framework based on multi-domain adversar...

---

### 12. Constrained Hybrid Metaheuristic: A Universal Framework for Continuous Optimisation

**Authors:** Piotr A. Kowalski, Szymon Kucharczyk, Jacek Mańdziuk

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18295v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18295v1)

**Summary:** This paper presents the constrained Hybrid Metaheuristic (cHM) algorithm as a general framework for continuous optimisation. Unlike many existing metaheuristics that are tailored to specific function classes or problem domains, cHM is designed to operate across a broad spectrum of objective functions, including those with unknown, heterogeneous, or complex properties such as non-convexity, non-separability, and varying smoothness. We provide a formal description of the algorithm, highlighting it...

---

### 13. Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI

**Authors:** Houston Haynes

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18104v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18104v1)

**Summary:** Prevailing AI training infrastructure assumes reverse-mode automatic differentiation over IEEE-754 arithmetic. The memory overhead of training relative to inference, optimizer complexity, and structural degradation of geometric properties through training are consequences of this arithmetic substrate. This paper develops an alternative training architecture grounded in three prior results: the Dimensional Type System and Deterministic Memory Management framework [6], which establishes stack-elig...

---

### 14. Large Language Models as a Semantic Interface and Ethical Mediator in Neuro-Digital Ecosystems: Conceptual Foundations and a Regulatory Imperative

**Authors:** Alexander V. Shenderuk-Zhidkov, Alexander E. Hramov

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17444v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17444v1)

**Summary:** This article introduces and substantiates the concept of Neuro-Linguistic Integration (NLI), a novel paradigm for human-technology interaction where Large Language Models (LLMs) act as a key semantic interface between raw neural data and their social application. We analyse the dual nature of LLMs in this role: as tools that augment human capabilities in communication, medicine, and education, and as sources of unprecedented ethical risks to mental autonomy and neurorights. By synthesizing insig...

---

### 15. A Synthesizable RTL Implementation of Predictive Coding Networks

**Authors:** Timothy Oh

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18066v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18066v1)

**Summary:** Backpropagation has enabled modern deep learning but is difficult to realize as an online, fully distributed hardware learning system due to global error propagation, phase separation, and heavy reliance on centralized memory. Predictive coding offers an alternative in which inference and learning arise from local prediction-error dynamics between adjacent layers. This paper presents a digital architecture that implements a discrete-time predictive coding update directly in hardware. Each neural...

---

### 16. Quadratic Surrogate Attractor for Particle Swarm Optimization

**Authors:** Maurizio Clemente, Marcello Canova

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17163v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17163v1)

**Summary:** This paper presents a particle swarm optimization algorithm that leverages surrogate modeling to replace the conventional global best solution with the minimum of an n-dimensional quadratic form, providing a better-conditioned dynamic attractor for the swarm. This refined convergence target, informed by the local landscape, enhances global convergence behavior and increases robustness against premature convergence and noise, while incurring only minimal computational overhead. The surrogate-augm...

---

### 17. Optimization-Embedded Active Multi-Fidelity Surrogate Learning for Multi-Condition Airfoil Shape Optimization

**Authors:** Isaac Robledo, Alberto Vilariño, Arnau Miró, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17057v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17057v1)

**Summary:** Active multi-fidelity surrogate modeling is developed for multi-condition airfoil shape optimization to reduce high-fidelity CFD cost while retaining RANS-level accuracy. The framework couples a low-fidelity-informed Gaussian process regression transfer model with uncertainty-triggered sampling and a synchronized elitism rule embedded in a hybrid genetic algorithm. Low-fidelity XFOIL evaluations provide inexpensive features, while sparse RANS simulations are adaptively allocated when predictive ...

---

### 18. Attractor-Keyed Memory

**Authors:** Natalia G. Berloff

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17049v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17049v1)

**Summary:** Physical selectors (lasers choosing a mode, Ising machines settling on a ground state, condensates occupying a spin state) produce high-dimensional signatures at the moment of decision: full field amplitudes, multimode interference patterns, or scattering responses. These signatures are richer than the winner's index, yet they are routinely discarded. We show that when the signatures are repeatable across trials (stereotyped) and linearly independent across routes, a single linear decoder compil...

---

### 19. Linearized Bregman Iterations for Sparse Spiking Neural Networks

**Authors:** Daniel Windhager, Bernhard A. Moser, Michael Lunglmayr

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16462v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16462v1)

**Summary:** Spiking Neural Networks (SNNs) offer an energy efficient alternative to conventional Artificial Neural Networks (ANNs) but typically still require a large number of parameters. This work introduces Linearized Bregman Iterations (LBI) as an optimizer for training SNNs, enforcing sparsity through iterative minimization of the Bregman distance and proximal soft thresholding updates. To improve convergence and generalization, we employ the AdaBreg optimizer, a momentum and bias corrected Bregman var...

---

### 20. Deep Reinforcement Learning-Assisted Automated Operator Portfolio for Constrained Multi-objective Optimization

**Authors:** Shuai Shao, Ye Tian, Shangshang Yang, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16401v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16401v1)

**Summary:** Constrained multi-objective optimization problems (CMOPs) are of great significance in the context of practical applications, ranging from scientific to engineering domains. Most existing constrained multi-objective evolutionary algorithms (CMOEAs) usually employ fixed operators all the time, which exhibit poor versatility in handling various CMOPs. Therefore, some recent studies have focused on adaptively selecting the best operators for the current population states during the search process. ...

---

### 21. Surrogate-Assisted Genetic Programming with Rank-Based Phenotypic Characterisation for Dynamic Multi-Mode Project Scheduling

**Authors:** Yuan Tian, Yi Mei, Mengjie Zhang

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16286v1)

**Summary:** The dynamic multi-mode resource-constrained project scheduling problem (DMRCPSP) is of practical importance, as it requires making real-time decisions under changing project states and resource availability. Genetic Programming (GP) has been shown to effectively evolve heuristic rules for such decision-making tasks; however, the evolutionary process typically relies on a large number of simulation-based fitness evaluations, resulting in high computational cost. Surrogate models offer a promising...

---

### 22. Analytically tractable model of synaptic crowding explains emergent small-world structure and network dynamics

**Authors:** Makoto Fukushima

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19320v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19320v1)

**Summary:** Neural circuits must balance local connectivity constraints against the need for global integration. Here we introduce a minimal wiring rule motivated by synaptic crowding: as a neuron accumulates incoming connections, each additional synapse becomes progressively harder to form. This single-parameter model admits an exact finite-size solution for the induced in-degree distribution and yields simple scaling laws: mean connectivity grows only logarithmically with network size while variance remai...

---

### 23. EvoIQA - Explaining Image Distortions with Evolved White-Box Logic

**Authors:** Ruchika Gupta, Illya Bakurov, Nathan Haut, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15887v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15887v1)

**Summary:** Traditional Image Quality Assessment (IQA) metrics typically fall into one of two extremes: rigid, hand-crafted mathematical models or "black-box" deep learning architectures that completely lack interpretability. To bridge this gap, we propose EvoIQA, a fully explainable symbolic regression framework based on Genetic Programming that Evolves explicit, human-readable mathematical formulas for image quality assessment (IQA). Utilizing a rich terminal set from the VSI, VIF, FSIM, and HaarPSI metri...

---

### 24. Towards Foundation Models for Consensus Rank Aggregation

**Authors:** Yijun Jin, Simon Klüttermann, Chiara Balestra, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15218v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15218v1)

**Summary:** Aggregating a consensus ranking from multiple input rankings is a fundamental problem with applications in recommendation systems, search engines, job recruitment, and elections. Despite decades of research in consensus ranking aggregation, minimizing the Kemeny distance remains computationally intractable. Specifically, determining an optimal aggregation of rankings with respect to the Kemeny distance is an NP-hard problem, limiting its practical application to relatively small-scale instances....

---

### 25. CATFormer: When Continual Learning Meets Spiking Transformers With Dynamic Thresholds

**Authors:** Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15184v1)

**Summary:** Although deep neural networks perform extremely well in controlled environments, they fail in real-world scenarios where data isn't available all at once, and the model must adapt to a new data distribution that may or may not follow the initial distribution. Previously acquired knowledge is lost during subsequent updates based on new data. a phenomenon commonly known as catastrophic forgetting. In contrast, the brain can learn without such catastrophic forgetting, irrespective of the number of ...

---

### 26. Towards Solving Polynomial-Objective Integer Programming with Hypergraph Neural Networks

**Authors:** Minshuo Li, Yaoxin Wu, Pavel Troubil, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19318v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19318v1)

**Summary:** Complex real-world optimization problems often involve both discrete decisions and nonlinear relationships between variables. Many such problems can be modeled as polynomial-objective integer programs, encompassing cases with quadratic and higher-degree variable interactions. Nonlinearity makes them more challenging than their linear counterparts. In this paper, we propose a hypergraph neural network (HNN) based method to solve polynomial-objective integer programming (POIP). Besides presenting ...

---

### 27. MorphSNN: Adaptive Graph Diffusion and Structural Plasticity for Spiking Neural Networks

**Authors:** Yongsheng Huang, Peibo Duan, Yujie Wu, et al.

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14285v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14285v1)

**Summary:** Spiking Neural Networks (SNNs) currently face a critical bottleneck: while individual neurons exhibit dynamic biological properties, their macro-scopic architectures remain confined within conventional connectivity patterns that are static and hierarchical. This discrepancy between neuron-level dynamics and network-level fixed connectivity eliminates critical brain-like lateral interactions, limiting adaptability in changing environments. To address this, we propose MorphSNN, a backbone framewor...

---

### 28. ST-ResGAT: Explainable Spatio-Temporal Graph Neural Network for Road Condition Prediction and Priority-Driven Maintenance

**Authors:** Mohsin Mahmud Topu, Azmine Toushik Wasi, Mahfuz Ahmed Anik, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.14107v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14107v1)

**Summary:** Climate-vulnerable road networks require a paradigm shift from reactive, fix-on-failure repairs to predictive, decision-ready maintenance. This paper introduces ST-ResGAT, a novel Spatio-Temporal Residual Graph Attention Network that fuses residual graph-attention encoding with GRU temporal aggregation to forecast pavement deterioration. Engineered for resource-constrained deployment, the framework translates continuous Pavement Condition Index (PCI) forecasts directly into the American Society ...

---

### 29. A Theory of Appropriateness That Accounts for Norms of Rationality

**Authors:** Joel Z. Leibo, Alexander Sasha Vezhnevets, Manfred Diaz, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.14050v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14050v1)

**Summary:** We propose a society-first theory of normative appropriateness where individuals, modeled as pre-trained actors with cognitive architectures analogous to Large Language Models (LLMs), generate behavior via predictive pattern completion. Our theory posits that individuals act by completing distributed symbolic patterns based on context, answering questions such as "What does a person such as I do in a situation such as this?". This sense-making mechanism provides a parsimonious account of the key...

---

### 30. MO-SAE:Multi-Objective Stacked Autoencoders Optimization for Edge Anomaly Detection

**Authors:** Lizhao Zhang, Shengsong Kong, Tao Guo, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13895v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13895v1)

**Summary:** Stacked AutoEncoders (SAE) have been widely adopted in edge anomaly detection scenarios. However, the resource-intensive nature of SAE can pose significant challenges for edge devices, which are typically resource-constrained and must adapt rapidly to dynamic and changing conditions. Optimizing SAE to meet the heterogeneous demands of real-world deployment scenarios, including high performance under constrained storage, low power consumption, fast inference, and efficient model updates, remains ...

---

### 31. Benchmarking the Energy Cost of Assurance in Neuromorphic Edge Robotics

**Authors:** Sylvester Kaczmarek

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13880v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13880v1)

**Summary:** Deploying trustworthy artificial intelligence on edge robotics imposes a difficult trade-off between high-assurance robustness and energy sustainability. Traditional defense mechanisms against adversarial attacks typically incur significant computational overhead, threatening the viability of power-constrained platforms in environments such as cislunar space. This paper quantifies the energy cost of assurance in event-driven neuromorphic systems. We benchmark the Hierarchical Temporal Defense (H...

---

### 32. Collapse or Preserve: Data-Dependent Temporal Aggregation for Spiking Neural Network Acceleration

**Authors:** Jiahao Qin

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13810v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13810v1)

**Summary:** Spike sparsity is widely believed to enable efficient spiking neural network (SNN) inference on GPU hardware. We demonstrate this is an illusion: five distinct sparse computation strategies on Apple M3 Max all fail to outperform dense convolution, because SIMD architectures cannot exploit the fine-grained, unstructured sparsity of i.i.d. binary spikes. Instead, we propose Temporal Aggregated Convolution (TAC), which exploits convolution linearity to pre-aggregate $K$ spike frames before a single...

---

### 33. Projection-Free Evolution Strategies for Continuous Prompt Search

**Authors:** Yu Cai, Canxi Huang, Xiaoyu He

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13786v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13786v1)

**Summary:** Continuous prompt search offers a computationally efficient alternative to conventional parameter tuning in natural language processing tasks. Nevertheless, its practical effectiveness can be significantly hindered by the black-box nature and the inherent high-dimensionality of the objective landscapes. Existing methods typically mitigate these challenges by restricting the search to a randomly projected low-dimensional subspace. However, the effectiveness and underlying motivation of the projec...

---

### 34. Sharpness Aware Surrogate Training for Spiking Neural Networks

**Authors:** Maximilian Nicholson

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.18039v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18039v1)

**Summary:** Surrogate gradients are a standard tool for training spiking neural networks (SNNs), but conventional hard forward or surrogate backward training couples a nonsmooth forward model with a biased gradient estimator. We study sharpness aware Surrogate Training (SAST), which applies sharpness aware Minimization (SAM) to a surrogate forward SNN trained by backpropagation. In this formulation, the optimization target is an ordinary smooth empirical risk, so the training gradient is exact for the auxil...

---

### 35. Equivalence of approximation by networks of single- and multi-spike neurons

**Authors:** Dominik Dold, Philipp Christian Petersen

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13478v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13478v1)

**Summary:** In a spiking neural network, is it enough for each neuron to spike at most once? In recent work, approximation bounds for spiking neural networks have been derived, quantifying how well they can fit target functions. However, these results are only valid for neurons that spike at most once, which is commonly thought to be a strong limitation. Here, we show that the opposite is true for a large class of spiking neuron models, including the commonly used leaky integrate-and-fire model with subtrac...

---

### 36. MXNorm: Reusing MXFP block scales for efficient tensor normalisation

**Authors:** Callum McLean, Luke Y. Prince, Alexandre Payot, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13180v1)

**Summary:** Matrix multiplication performance has long been the major bottleneck to scaling deep learning workloads, which has stimulated the design of new accelerators that use increasingly low-precision number formats. However, improvements in matrix multiplication performance have far outstripped improvements in performance on reductions and elementwise computations, which are still being performed in higher precision. In this work, we propose MXNorm, a drop-in replacement for RMSNorm that estimates the ...

---

### 37. Federated Few-Shot Learning on Neuromorphic Hardware: An Empirical Study Across Physical Edge Nodes

**Authors:** Steven Motta, Gioele Nanni

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13037v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13037v1)

**Summary:** Federated learning on neuromorphic hardware remains unexplored because on-chip spike-timing-dependent plasticity (STDP) produces binary weight updates rather than the floating-point gradients assumed by standard algorithms. We build a two-node federated system with BrainChip Akida AKD1000 processors and run approximately 1,580 experimental trials across seven analysis phases. Of four weight-exchange strategies tested, neuron-level concatenation (FedUnion) consistently preserves accuracy while el...

---

### 38. Finite Difference Flow Optimization for RL Post-Training of Text-to-Image Models

**Authors:** David McAllister, Miika Aittala, Tero Karras, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12893v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12893v1)

**Summary:** Reinforcement learning (RL) has become a standard technique for post-training diffusion-based image synthesis models, as it enables learning from reward signals to explicitly improve desirable aspects such as image quality and prompt alignment. In this paper, we propose an online RL variant that reduces the variance in the model updates by sampling paired trajectories and pulling the flow velocity in the direction of the more favorable image. Unlike existing methods that treat each sampling step...

---

### 39. SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks

**Authors:** Hongyang Shang, Shuai Dong, Yahan Yang, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12739v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12739v1)

**Summary:** Spiking Neural Networks (SNNs) have emerged as a biologically inspired alternative to conventional deep networks, offering event-driven and energy-efficient computation. However, their throughput remains constrained by the serial update of neuron membrane states. While many hardware accelerators and Compute-in-Memory (CIM) architectures efficiently parallelize the synaptic operation (W x I) achieving O(1) complexity for matrix-vector multiplication, the subsequent state update step still require...

---

### 40. Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks

**Authors:** Tianhao Qian, Zhuoxuan Li, Jinde Cao, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12354v2) | 📄 [PDF](https://arxiv.org/pdf/2603.12354v2)

**Summary:** Efficient deep learning traditionally relies on static heuristics like weight magnitude or activation awareness (e.g., Wanda, RIA). While successful in unstructured settings, we observe a critical limitation when applying these metrics to the structural pruning of deep vision networks. These contemporary metrics suffer from a magnitude bias, failing to preserve critical functional pathways. To overcome this, we propose a decoupled kinetic paradigm inspired by Alternating Gradient Flow (AGF), uti...

---

### 41. Pruning-induced phases in fully-connected neural networks: the eumentia, the dementia, and the amentia

**Authors:** Haining Pan, Nakul Aggarwal, J. H. Pixley

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12316v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12316v1)

**Summary:** Modern neural networks are heavily overparameterized, and pruning, which removes redundant neurons or connections, has emerged as a key approach to compressing them without sacrificing performance. However, while practical pruning methods are well developed, whether pruning induces sharp phase transitions in the neural networks and, if so, to what universality class they belong, remain open questions. To address this, we study fully-connected neural networks trained on MNIST, independently varyi...

---

### 42. Topological DeepONets and a generalization of the Chen-Chen operator approximation theorem

**Authors:** Vugar Ismailov

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11972v1)

**Summary:** Deep Operator Networks (DeepONets) provide a branch-trunk neural architecture for approximating nonlinear operators acting between function spaces. In the classical operator approximation framework, the input is a function $u\in C(K_1)$ defined on a compact set $K_1$ (typically a compact subset of a Banach space), and the operator maps $u$ to an output function $G(u)\in C(K_2)$ defined on a compact Euclidean domain $K_2\subset\mathbb{R}^d$. In this paper, we develop a topological extension in wh...

---

### 43. SNAP-V: A RISC-V SoC with Configurable Neuromorphic Acceleration for Small-Scale Spiking Neural Networks

**Authors:** Kanishka Gunawardana, Sanka Peeris, Kavishka Rambukwella, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11939v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11939v1)

**Summary:** Spiking Neural Networks (SNNs) have gained significant attention in edge computing due to their low power consumption and computational efficiency. However, existing implementations either use conventional System on Chip (SoC) architectures that suffer from memory-processor bottlenecks, or large-scale neuromorphic hardware that is inefficient and wasteful for small-scale SNN applications. This work presents SNAP-V, a RISC-V-based neuromorphic SoC with two accelerator variants: Cerebra-S (bus-bas...

---

### 44. An Evolutionary Algorithm with Probabilistic Annealing for Large-scale Sparse Multi-objective Optimization

**Authors:** Shuai Shao, Yuhao Sun, Xing Chen, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11874v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11874v1)

**Summary:** Large-scale sparse multi-objective optimization problems (LSMOPs) are prevalent in real-world applications, where optimal solutions typically contain only a few nonzero variables, such as in adversarial attacks, critical node detection, and sparse signal reconstruction. Since the function evaluation of LSMOPs often relies on large-scale datasets involving a large number of decision variables, the search space becomes extremely high-dimensional. The coexistence of sparsity and high dimensionality...

---

### 45. Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks

**Authors:** Yongqi Ding, Kunshan Yang, Linze Li, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11676v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11676v1)

**Summary:** Although the temporal spike dynamics of spiking neural networks (SNNs) enable low-power temporal pattern capture capabilities, they also incur inherent inconsistencies that severely compromise representation. In this paper, we perform dual consistency optimization via Stable Spike to mitigate this problem, thereby improving the recognition performance of SNNs. With the hardware-friendly ``AND" bit operation, we efficiently decouple the stable spike skeleton from the multi-timestep spike maps, th...

---

### 46. Quantum mechanical framework for quantization-based optimization: from Gradient flow to Schroedinger equation

**Authors:** Jinwuk Seok, Changsik Cho

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11536v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11536v1)

**Summary:** This work presents a quantum mechanical framework for analyzing quantization-based optimization algorithms. The sampling process of the quantization-based search is modeled as a gradient-flow dissipative system, leading to a Hamilton-Jacobi-Bellman (HJB) representation. Through a suitable transformation of the objective function, this formulation yields the Schroedinger equation, which reveals that quantum tunneling enables escape from local minima and guarantees access to the global optimum. By...

---

### 47. COMIC: Agentic Sketch Comedy Generation

**Authors:** Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11048v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11048v1)

**Summary:** We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the system employs a population of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and improvement. A key contribution is the introduction of LLM critics aligned with real viewer preferences through the analysis of a c...

---

### 48. ForwardFlow: Simulation only statistical inference using deep learning

**Authors:** Stefan Böhringer

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10991v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10991v1)

**Summary:** Deep learning models are being used for the analysis of parametric statistical models based on simulation-only frameworks. Bayesian models using normalizing flows simulate data from a prior distribution and are composed of two deep neural networks: a summary network that learns a sufficient statistic for the parameter and a normalizing flow that conditional on the summary network can approximate the posterior distribution. Here, we explore frequentist models that are based on a single summary ne...

---

### 49. Efficient Approximation to Analytic and $L^p$ functions by Height-Augmented ReLU Networks

**Authors:** ZeYu Li, FengLei Fan, TieYong Zeng

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11128v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11128v1)

**Summary:** This work addresses two fundamental limitations in neural network approximation theory. We demonstrate that a three-dimensional network architecture enables a significantly more efficient representation of sawtooth functions, which serves as the cornerstone in the approximation of analytic and $L^p$ functions. First, we establish substantially improved exponential approximation rates for several important classes of analytic functions and offer a parameter-efficient network design. Second, for t...

---

### 50. Multi-objective Genetic Programming with Multi-view Multi-level Feature for Enhanced Protein Secondary Structure Prediction

**Authors:** Yining Qian, Lijie Su, Meiling Xu, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.12293v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12293v1)

**Summary:** Predicting protein secondary structure is essential for understanding protein function and advancing drug discovery. However, the intricate sequence-structure relationship poses significant challenges for accurate modeling. To address these, we propose MOGP-MMF, a multi-objective genetic programming framework that reformulates PSSP as an automated optimization task focused on feature selection and fusion. Specifically, MOGP-MMF introduces a multi-view multi-level representation strategy that int...

---

## q-bio.NC

**50 papers**

### 1. Brain Learning Principles Utilizing Non-Ideal Factors in Neural Circuits

**Authors:** Da-Zheng Feng, Hao-Xuan Du

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21542v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21542v1)

**Summary:** The human brain achieves its remarkable computational prowess not despite its inherent non-ideal factors noise, heterogeneity, structural irregularities, decentralized plasticity, systematic errors, and chaotic dynamics but precisely because of them. This paper systematically demonstrates that these traits, long dismissed as imperfections in classical neuroscience and eliminated in digital engineering, are evolutionary design principles that endow the brain with robustness, adaptability, and cre...

---

### 2. Can we automatize scientific discovery in the cognitive sciences?

**Authors:** Akshay K. Jagadish, Milena Rmus, Kristin Witte, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.20988v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20988v1)

**Summary:** The cognitive sciences aim to understand intelligence by formalizing underlying operations as computational models. Traditionally, this follows a cycle of discovery where researchers develop paradigms, collect data, and test predefined model classes. However, this manual pipeline is fundamentally constrained by the slow pace of human intervention and a search space limited by researchers' background and intuition. Here, we propose a paradigm shift toward a fully automated, in silico science of t...

---

### 3. A sub-Riemannian model of the motor cortex with Wasserstein distance

**Authors:** Jawad Ali, Giovanna Citti, Alessandro Sarti

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20756v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20756v1)

**Summary:** This study aims to better understand the functional geometry of the motor cortex, starting from different sources of experimental evidence. Recent studies have proved that cells of the primary motor cortex (M1) are sensitive to short hand trajectories called fragments. Here, we propose a sub-Riemannian higher-dimensional geometry accounting for geometric and kinematic properties. Due to the constraints of the geometry, horizontal curves naturally satisfy a relation between geometric and kinemati...

---

### 4. Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration

**Authors:** Jianwei Chen, Zhengyang Miao, Wenjie Cai, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20680v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20680v1)

**Summary:** Integrating structural and functional connectomes remains challenging because their relationship is non-linear and organized over nested modular hierarchies. We propose a hierarchical multiscale structure-function coupling framework for connectome integration that jointly learns individualized modular organization and hierarchical coupling across structural connectivity (SC) and functional connectivity (FC). The framework includes: (i) Prototype-based Modular Pooling (PMPool), which learns modal...

---

### 5. Transcranial Alternating Current Stimulation (tACS) for patients with Post-Stroke Anomia: Preliminary Data on Picture Naming Performance

**Authors:** Maria Martzoukou, Nefeli K. Dimitriou, Binbin Xu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20476v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20476v1)

**Summary:** The present study evaluated the effectiveness of transcranial alternating current stimulation (tACS) treating patients with post-stroke anomia using a picture-naming task and a Single-Case Experimental Design (SCED). A right-handed 38-year-old woman with a left-hemisphere stroke and a left-handed 54-year-old man with a right-hemisphere stroke underwent an eight-week treatment program. Specifically, they participated in a picture-naming task three times a week, alternating between sessions with a...

---

### 6. Problem difficulty and waiting time shape the level of detail and temporal organization of visual strategies in human planning

**Authors:** Mattia Eluchans, Giovanni Pezzulo

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19881v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19881v1)

**Summary:** Planning entails identifying sequences of actions to reach a goal, yet we still have incomplete knowledge of how problem constraints, such as difficulty and available time, influence the visual strategies supporting plan construction, both in terms of coverage of the to-be-executed plans and its temporal organization. To fill this gap, we recorded participants' cursor and eye movements in a multi-target problem solving task on a grid. We manipulated two orthogonal dimensions: problem difficulty,...

---

### 7. Multimodal branched transport infers anatomically aligned brain reaction maps

**Authors:** Cristian Mendico

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19761v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19761v1)

**Summary:** How external stimulation is transformed into distributed reaction patterns remains unresolved at the level of propagation architecture. Existing large-scale control models quantify transition costs on prescribed networks but do not infer the routing map itself from source and target activity. Here we combine task-related blood-oxygen-level-dependent responses, source-reconstructed electrophysiology and tractography-derived anisotropy to estimate stimulation and reaction measures, define an anato...

---

### 8. Branched Optimal Transport for Stimulus to Reaction Brain Mapping

**Authors:** Cristian Mendico

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19751v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19751v1)

**Summary:** A central problem in systems neuroscience is to determine how an external stimulation is propagated through the brain so as to produce a reaction. Current deterministic and stochastic control models quantify transition costs between brain states on a prescribed network, but do not treat the transport network itself as an unknown. Here we propose a variational framework in which the inferred object is a graph/current connecting a stimulation source measure to a reaction target measure. The model ...

---

### 9. A Unified Phase-native Computational Principle Governs Hippocampal Spike Timing and Neural Coding

**Authors:** Reza Ahmadvand, Sara Safura Sharif, Yaser Mike Banad

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19690v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19690v1)

**Summary:** Hippocampal neurons exhibit precise phase locking to network oscillations, but the computational principle governing this temporal precision is still unclear. Neural information is conveyed jointly by firing rates and spike timing, but existing models treat these dimensions separately, limiting mechanistic interpretation of spike-field coupling and its reported association with spectral features such as the aperiodic slope. Here we show that hippocampal phase locking emerges from a fundamental d...

---

### 10. Curvature Sensitive Cells in the Modular Structures of The Visual Cortex

**Authors:** Giovanna Citti, Vasiliki Liontou

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19425v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19425v1)

**Summary:** We propose a model of the functional architecture of curvature-sensitive cells in the primary visual cortex. The model accounts for the modular and hierarchical organization of the cortex, the horizontal connectivity, and the shape of receptive profiles of these cells as Gabor-type filters. We construct a canonical affine subbundle of the cotangent bundle of the manifold of oriented contact elements of the retina as a geometric model for these cells, and show that this subbundle carries an Engel...

---

### 11. Hierarchical Latent Structure Learning through Online Inference

**Authors:** Ines Aitsahalia, Kiyohito Iigaya

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19139v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19139v1)

**Summary:** Learning systems must balance generalization across experiences with discrimination of task-relevant details. Effective learning therefore requires representations that support both. Online latent-cause models support incremental inference but assume flat partitions, whereas hierarchical Bayesian models capture multilevel structure but typically require offline inference. We introduce the Hierarchical Online Learning of Multiscale Experience Structure (HOLMES) model, a computational framework fo...

---

### 12. Resolving the Blow-Up: A Time-Dilated Numerical Framework for Multiple Firing Events in Mean-Field Neuronal Networks

**Authors:** Xu'an Dou, Louis Tao, Zhe Xue, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18475v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18475v1)

**Summary:** In large-scale excitatory neuronal networks, rapid synchronization manifests as {multiple firing events (MFEs)}, mathematically characterized by a finite-time blow-up of the neuronal firing rate in the mean-field Fokker-Planck equation. Standard numerical methods struggle to resolve this singularity due to the divergent boundary flux and the instantaneous nature of the population voltage reset. In this work, we propose a robust {multiscale numerical framework based on time dilation}. By transfor...

---

### 13. Unified Policy Value Decomposition for Rapid Adaptation

**Authors:** Cristiano Capone, Luca Falorsi, Andrea Ciardiello, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17947v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17947v1)

**Summary:** Rapid adaptation in complex control systems remains a central challenge in reinforcement learning. We introduce a framework in which policy and value functions share a low-dimensional coefficient vector - a goal embedding - that captures task identity and enables immediate adaptation to novel tasks without retraining representations. During pretraining, we jointly learn structured value bases and compatible policy bases through a bilinear actor-critic decomposition. The critic factorizes as Q = ...

---

### 14. Inhibitory normalization of error signals improves learning in neural circuits

**Authors:** Roy Henha Eyono, Daniel Levenstein, Arna Ghosh, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17676v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17676v1)

**Summary:** Normalization is a critical operation in neural circuits. In the brain, there is evidence that normalization is implemented via inhibitory interneurons and allows neural populations to adjust to changes in the distribution of their inputs. In artificial neural networks (ANNs), normalization is used to improve learning in tasks that involve complex input distributions. However, it is unclear whether inhibition-mediated normalization in biological neural circuits also improves learning. Here, we e...

---

### 15. Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity

**Authors:** Jiawen Kang, Kun Li, Dongrui Han, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17392v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17392v1)

**Summary:** Automated Alzheimer's Disease (AD) screening has predominantly followed the inductive paradigm of pattern recognition, which directly maps the input signal to the outcome label. This paradigm sacrifices construct validity of clinical protocol for statistical shortcuts. This paper proposes Agentic Cognitive Profiling (ACP), an agentic framework that realigns automated screening with clinical protocol logic across multiple cognitive domains. Rather than learning opaque mappings from transcripts to...

---

### 16. Beyond bouba/kiki: Multidimensional semantic signals are deeply woven into the fabric of natural language

**Authors:** Gexin Zhao

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17306v2) | 📄 [PDF](https://arxiv.org/pdf/2603.17306v2)

**Summary:** A foundational assumption in linguistics holds that the relationship between a word's sound and its meaning is arbitrary. Accumulating evidence from sound symbolism challenges this view, yet no study has systematically mapped the multidimensional semantic profile of every phonological unit within a language. Here we show that individual letter-phonemes in English carry structured, multidimensional semantic signals. Using a minimal-pair paradigm spanning all 220 pairwise letter contrasts, three l...

---

### 17. Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests

**Authors:** Christian A. Kothe, Sean Mullen, Michael V. Bronstein, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16741v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16741v1)

**Summary:** Objective. We establish a principled method for inferring mental health related psychometric variables from neural and behavioral data using the Implicit Association Test (IAT) as the data generation engine, aiming to overcome the limited predictive performance (typically under 0.7 AUC) of the gold-standard D-score method, which relies solely on reaction times.   Approach. We propose a sparse hierarchical Bayesian model that leverages multi-modal data to predict experiences related to mental ill...

---

### 18. The immediate effect of kangaroo mother care on Mother-infant inter-brain synchrony and infant brain function

**Authors:** Yu Liu, Jiayang Xu, Tianzi Wang, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16501v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16501v1)

**Summary:** Kangaroo mother care (KMC) is an intervention involving skin-to-skin contact that promotes physiological stability and supports long-term neurodevelopment in preterm infants. However, the underlying neurophysiological mechanisms remain unclear. We aimed to investigate the immediate effects of the first KMC on infants' brain function, mother-infant inter-brain synchrony, as well as their associations. Fifty-eight preterm infants (gestational age < 32 weeks or birth weight < 1500 g) and their moth...

---

### 19. Hippocampus mediates conceptual generalization of pain modulation

**Authors:** Dylan Sutterlin Guindon, Tor D Wager, Leonie Koban

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16288v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16288v1)

**Summary:** Pain is strongly influenced by expectations and learning from previous experience, such as in classical conditioning. Conditioned responses and expectations can generalize to perceptually and conceptually related cues, but how generalization influences pain experience and the neurobiological processing of pain remains unclear. We used fMRI and multilevel mediation analyses to address this question. Thirty-six human participants first learned to associate two visual cues from distinct conceptual ...

---

### 20. Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction

**Authors:** Saarang Panchavati, Uddhav Panchavati, Corey Arnold, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16281v1)

**Summary:** Electroencephalography (EEG) is a widely used tool for studying brain function, with applications in clinical neuroscience, diagnosis, and brain-computer interfaces (BCIs). Recent EEG foundation models trained on large unlabeled corpora aim to learn transferable representations, but their effectiveness remains unclear; reported improvements over smaller task-specific models are often modest, sensitive to downstream adaptation and fine-tuning strategies, and limited under linear probing. We hypot...

---

### 21. Early Pre-Stroke Detection via Wearable IMU-Based Gait Variability and Postural Drift Analysis

**Authors:** Chanakan Chaipan, Aueaphum Aueawatthanaphisut

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16178v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16178v1)

**Summary:** Early identification of individuals at risk of stroke remains a major clinical challenge, as prodromal motor im- pairments are often subtle and transient. In this pilot study, a wearable sensor-based framework is proposed for early pre- stroke risk screening using a single inertial measurement unit mounted on the sacral region to capture pelvic motion during gait and standing tasks. The pelvis is treated as a biomechanical proxy for global motor control, enabling the quantification of gait varia...

---

### 22. Analytically tractable model of synaptic crowding explains emergent small-world structure and network dynamics

**Authors:** Makoto Fukushima

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19320v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19320v1)

**Summary:** Neural circuits must balance local connectivity constraints against the need for global integration. Here we introduce a minimal wiring rule motivated by synaptic crowding: as a neuron accumulates incoming connections, each additional synapse becomes progressively harder to form. This single-parameter model admits an exact finite-size solution for the induced in-degree distribution and yields simple scaling laws: mean connectivity grows only logarithmically with network size while variance remai...

---

### 23. The Neuroscience of Transformers

**Authors:** Peter Koenig, Mario Negrello

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15339v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15339v1)

**Summary:** Neuroscience has long informed the development of artificial neural networks, but the success of modern architectures invites, in turn, the converse: can modern networks teach us lessons about brain function? Here, we examine the structure of the cortical column and propose that the transformer provides a natural computational analogy for multiple elements of cortical microcircuit organization. Rather than claiming a literal implementation of transformer equations in cortex, we develop a hypothe...

---

### 24. BCMI-Driven Motion Control Detection: EEG-Based Machine Learning and Interaction Entropy for High-Order Brain Networks

**Authors:** Jiajia Li, Fan Li, Jian Song

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15208v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15208v1)

**Summary:** This study investigates the cognitive motor control detection and the underlying neuroregulatory mechanisms during music-assisted simulated driving. Using a dynamic higher-order network model constructed with EEG-based cross-information entropy, we quantify the dynamic coordination within brain networks activated during both music listening and driving. This approach, which contrasts with previous static network analyses, provides novel insights into how musical stimuli modulate the complex inte...

---

### 25. D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing

**Authors:** Yuru Song, Qi Xin

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14597v1)

**Summary:** Autonomous LLM agents require structured long-term memory, yet current "append-and-evolve" systems like A-MEM face O(N^2) write-latency and excessive token costs. We introduce D-MEM (Dopamine-Gated Agentic Memory), a biologically inspired architecture that decouples short-term interaction from cognitive restructuring via a Fast/Slow routing system based on Reward Prediction Error (RPE). A lightweight Critic Router evaluates stimuli for Surprise and Utility. Routine, low-RPE inputs are bypassed o...

---

### 26. Deep probabilistic model synthesis enables unified modeling of whole-brain neural activity across individual subjects

**Authors:** William E. Bishop, Luuk W. Hesselink, Bernhard Englitz, et al.

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14161v1)

**Summary:** Many disciplines need quantitative models that synthesize experimental data across multiple instances of the same general system. For example, neuroscientists must combine data from the brains of many individual animals to understand the species' brain in general. However, typical machine learning models treat one system instance at a time. Here we introduce a machine learning framework, deep probabilistic model synthesis (DPMS), that leverages system properties auxiliary to the model to combine...

---

### 27. Human-like Object Grouping in Self-supervised Vision Transformers

**Authors:** Hossein Adeli, Seoyoung Ahn, Andrew Luo, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13994v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13994v1)

**Summary:** Vision foundation models trained with self-supervised objectives achieve strong performance across diverse tasks and exhibit emergent object segmentation properties. However, their alignment with human object perception remains poorly understood. Here, we introduce a behavioral benchmark in which participants make same/different object judgments for dot pairs on naturalistic scenes, scaling up a classical psychophysics paradigm to over 1000 trials. We test a diverse set of vision models using a ...

---

### 28. Equivalence of approximation by networks of single- and multi-spike neurons

**Authors:** Dominik Dold, Philipp Christian Petersen

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13478v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13478v1)

**Summary:** In a spiking neural network, is it enough for each neuron to spike at most once? In recent work, approximation bounds for spiking neural networks have been derived, quantifying how well they can fit target functions. However, these results are only valid for neurons that spike at most once, which is commonly thought to be a strong limitation. Here, we show that the opposite is true for a large class of spiking neuron models, including the commonly used leaky integrate-and-fire model with subtrac...

---

### 29. Developing the PsyCogMetrics AI Lab to Evaluate Large Language Models and Advance Cognitive Science -- A Three-Cycle Action Design Science Study

**Authors:** Zhiye Jin, Yibai Li, K. D. Joshi, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13126v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13126v1)

**Summary:** This study presents the development of the PsyCogMetrics AI Lab (psycogmetrics.ai), an integrated, cloud-based platform that operationalizes psychometric and cognitive-science methodologies for Large Language Model (LLM) evaluation. Framed as a three-cycle Action Design Science study, the Relevance Cycle identifies key limitations in current evaluation methods and unfulfilled stakeholder needs. The Rigor Cycle draws on kernel theories such as Popperian falsifiability, Classical Test Theory, and ...

---

### 30. Pulse desynchronization of neural populations by targeting the centroid of the limit cycle in phase space

**Authors:** Ramón Guevara, Marco Zenari, Giorgio Nicoletti, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12878v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12878v1)

**Summary:** The synchronized activity of neuronal populations can lead to pathological over-synchronization in conditions such as epilepsy and Parkinson disease. Such states can be desynchronized by brief electrical pulses. But when the underlying oscillating system is not known, as in most practical applications, to determine the specific times and intensities of pulses used for desynchronizaton is a difficult inverse problem. Here we propose a desynchronization scheme for neuronal models of bi-variate neu...

---

### 31. Dual-Laws Model for a theory of artificial consciousness

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12662v3) | 📄 [PDF](https://arxiv.org/pdf/2603.12662v3)

**Summary:** Objectively verifying the generative mechanism of consciousness is extremely difficult because of its subjective nature. As long as theories of consciousness focus solely on its generative mechanism, developing a theory remains challenging. We believe that broadening the theoretical scope and enhancing theoretical unification are necessary to establish a theory of consciousness. This study proposes seven questions that theories of consciousness should address: phenomena, self, causation, state, ...

---

### 32. Towards unified brain-to-text decoding across speech production and perception

**Authors:** Zhizhang Yuan, Yang Yang, Gaorui Zhang, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12628v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12628v1)

**Summary:** Speech production and perception are the main ways humans communicate daily. Prior brain-to-text decoding studies have largely focused on a single modality and alphabetic languages. Here, we present a unified brain-to-sentence decoding framework for both speech production and perception in Mandarin Chinese. The framework exhibits strong generalization ability, enabling sentence-level decoding when trained only on single-character data and supporting characters and syllables unseen during trainin...

---

### 33. Formation of Artificial Neural Assemblies by Biologically Plausible Inhibition Mechanisms

**Authors:** Lucas Hoff, Gustavo Soroka, Matheus Guimarães, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12416v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12416v1)

**Summary:** As proposed by Hebb's theory, neural assemblies are groups of excitatory neurons that fire synchronously and exhibit high synaptic density, representing external stimuli and supporting cognitive functions such as language and decision-making. Recently, a model called Assembly Calculus (AC) was proposed, enabling the formation of artificial neural assemblies through the $k$-winners-take-all selection process and Hebbian learning. Although the model is capable of forming assemblies according to He...

---

### 34. Neural network-based encoding in free-viewing fMRI with gaze-aware models

**Authors:** Dora Gozukara, Nasir Ahmad, Katja Seeliger, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11663v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11663v1)

**Summary:** Representations learned by convolutional neural networks (CNNs) exhibit a remarkable resemblance to information processing patterns observed in the primate visual system on large neuroimaging datasets collected under diverse, naturalistic visual stimulation, but with instruction for participants to maintain central fixation. This viewing condition, however, diverges significantly from ecologically valid visual behaviour, suppresses activity in visually active regions, and imposes substantial cog...

---

### 35. Miniaturized microscopes to study neural dynamics in freely-behaving animals

**Authors:** Weijian Zong, Weijian Yang

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11435v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11435v1)

**Summary:** Head-mounted miniaturized microscopes, commonly known as miniscopes, have undergone rapid development and seen widespread adoption over the past two decades, enabling the imaging of neural activity in freely-behaving animals such as rodents, songbirds, and non-human primates. These miniscopes facilitate numerous studies that are not feasible with head-fixed preparations. Recent advancements have enhanced their capabilities, allowing for faster imaging, larger fields of view, and deeper brain pen...

---

### 36. Human Navigation Behaviour and Brain Dynamics in Real-world Contexts

**Authors:** Pablo Fernandez Velasco, Antoine Coutrot, Hugo J. Spiers

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11347v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11347v1)

**Summary:** The study of navigation behaviour and the associated brain dynamics have been a focus increasing research over the last decades. Coinciding with this has been an increased focus on a more ecological understanding of cognition. Here we review recent research seeking to provide a more naturalistic, ecological understanding of human navigation behaviour and brain dynamics. Research in this area falls into four categories: testing navigation in real-world environments, analysis of data collected fro...

---

### 37. The macaque IT cortex but not current artificial vision networks encode object position in perceptually aligned coordinates

**Authors:** Elizaveta Yakubovskaya, Hamidreza Ramezanpour, Matteo Dunnhofer, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11248v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11248v1)

**Summary:** Efficient interaction with the visual world requires not only accurate object identification but also precise localization of objects in space. While spatial ("where") processing has traditionally been attributed to dorsal stream pathways, recent work has shown that object position can also be decoded from responses in ventral stream areas such as the inferior temporal (IT) cortex. However, because object position in these paradigms is tightly coupled to pixel-based location, it remains unclear ...

---

### 38. Uncovering statistical structure in large-scale neural activity with Restricted Boltzmann Machines

**Authors:** Nicolas Béreux, Giovanni Catania, Aurélien Decelle, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11032v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11032v1)

**Summary:** Large-scale electrophysiological recordings now allow simultaneous monitoring of thousands of neurons across multiple brain regions, revealing structured variability in neural population activity. Understanding how these collective patterns emerge from microscopic neural interactions requires models that are scalable, predictive, and interpretable. Statistical physics provides principled frameworks to address this complexity, including maximum-entropy models that offer transparent descriptions o...

---

### 39. Cross-Species Transfer Learning for Electrophysiology-to-Transcriptomics Mapping in Cortical GABAergic Interneurons

**Authors:** Theo Schwider, Ramin Ramezani

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11000v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11000v1)

**Summary:** Single-cell electrophysiological recordings provide a powerful window into neuronal functional diversity and offer an interpretable route for linking intrinsic physiology to transcriptomic identity. Here, we replicate and extend the electrophysiology-to-transcriptomics framework introduced by Gouwens et al. (2020) using publicly available Allen Institute Patch-seq datasets from both mouse and human cortex. We focus on GABAergic inhibitory interneurons to target a subclass structure (Lamp5, Pvalb...

---

### 40. Linear Readout of Neural Manifolds with Continuous Variables

**Authors:** Will Slatton, Chi-Ning Chou, SueYeon Chung

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10956v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10956v1)

**Summary:** Brains and artificial neural networks compute with continuous variables such as object position or stimulus orientation. However, the complex variability in neural responses makes it difficult to link internal representational structure to task performance. We develop a statistical-mechanical theory of regression capacity that relates linear decoding efficiency of continuous variables to geometric properties of neural manifolds. Our theory handles complex neural variability and applies to real d...

---

### 41. JEDI: Jointly Embedded Inference of Neural Dynamics

**Authors:** Anirudh Jamkhandi, Ali Korojy, Olivier Codol, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10489v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10489v1)

**Summary:** Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent n...

---

### 42. Curvature Blindness from Polarity Breaks and Orientation Channel Fragmentation in V1

**Authors:** Michael Menke

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09765v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09765v1)

**Summary:** We present a mathematical model of the curvature blindness illusion in which sinusoids appear as angular zigzags when drawn with alternating contrast polarity against a gray background. The model identifies two complementary mechanisms, both operating in V1. First, polarity channel separation: simple cells are selective for contrast polarity, and lateral connections link only same polarity neurons; where the line switches from darker than background to lighter than background at each peak and tr...

---

### 43. Efficient and robust control with spikes that constrain free energy

**Authors:** André Urbano, Pablo Lanillos, Sander Keemink

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09729v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09729v1)

**Summary:** Animal brains exhibit remarkable efficiency in perception and action, while being robust to both external and internal perturbations. The means by which brains accomplish this remains, for now, poorly understood, hindering our understanding of animal and human cognition, as well as our own implementation of efficient algorithms for control of dynamical systems.A potential candidate for a robust mechanism of state estimation and action computation is the free energy principle, but existing implem...

---

### 44. A Variational Latent Equilibrium for Learning in Neuronal Circuits

**Authors:** Simon Brandt, Paul Haider, Walter Senn, et al.

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09600v2) | 📄 [PDF](https://arxiv.org/pdf/2603.09600v2)

**Summary:** Brains remain unrivaled in their ability to recognize and generate complex spatiotemporal patterns. While AI is able to reproduce some of these capabilities, deep learning algorithms remain largely at odds with our current understanding of brain circuitry and dynamics. This is prominently the case for backpropagation through time (BPTT), the go-to algorithm for learning complex temporal dependencies. In this work we propose a general formalism to approximate BPTT in a controlled, biologically pl...

---

### 45. Decoding the decoder: Contextual sequence-to-sequence modeling for intracortical speech decoding

**Authors:** Michal Olak, Tommaso Boccato, Matteo Ferrante

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.20246v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20246v1)

**Summary:** Speech brain--computer interfaces require decoders that translate intracortical activity into linguistic output while remaining robust to limited data and day-to-day variability. While prior high-performing systems have largely relied on framewise phoneme decoding combined with downstream language models, it remains unclear what contextual sequence-to-sequence decoding contributes to sublexical neural readout, robustness, and interpretability. We evaluated a multitask Transformer-based sequence-...

---

### 46. Compact Dynamical Mean-Field Theory of Oscillator Networks

**Authors:** Kanishka Reddy

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09402v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09402v1)

**Summary:** We present a compact dynamical mean-field theory (DMFT) for large networks of coupled phase oscillators whose phases live on the circle $S^1$ and interact with both coherent mean-field coupling and quenched randomness. Starting from wrapped Langevin dynamics, we build a path-integral representation that keeps the $2π$-periodicity of the phases explicit. After averaging over the disorder in the thermodynamic limit, this construction reduces to a single-oscillator stochastic equation driven by a d...

---

### 47. Dreaming improves memorization in a Hopfield model with bounded synaptic strength

**Authors:** Enzo Marinari, Saverio Rossi, Francesco Zamponi

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09384v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09384v1)

**Summary:** The Hopfield model provides a paradigmatic framework for associative memory. Its classical implementation, based on the Hebbian learning rule, suffers from catastrophic forgetting: when one attempts storing too many patterns, the network fails to retrieve any of them. Yet, the Hebbian rule does not take into account that synaptic strength is bounded. Introducing this biologically plausible modification, known as "clipping", eliminates catastrophic forgetting; the model is now able to retrieve th...

---

### 48. Sampling on Discrete Spaces with Temporal Point Processes

**Authors:** Cameron A. Stewart, Maneesh Sahani

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09089v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09089v1)

**Summary:** Temporal point processes offer a powerful framework for sampling from discrete distributions, yet they remain underutilized in existing literature. We show how to construct, for any target multivariate count distribution with downward-closed support, a multivariate temporal point process whose event-count vector in a fixed-length sliding window converges in distribution to the target as time tends to infinity. Structured as a system of potentially coupled infinite-server queues with deterministi...

---

### 49. Diffusion of Neuromodulators for Temporal Credit Assignment

**Authors:** João Barretto-Bittar, Anna Levina, Emmanouil Giannakakis, et al.

**Published:** 2026-03-09

🔗 [Paper](http://arxiv.org/abs/2603.08949v1) | 📄 [PDF](https://arxiv.org/pdf/2603.08949v1)

**Summary:** Biological learning achieves temporal credit assignment despite sparse and imprecise feedback, often relying on neuromodulatory signals acting over space and time. Here, we introduce a learning mechanism in which error information diffuses locally through the network, similar to volume transmission of neuromodulators. This distributed modulation allows neurons to learn even in the absence of direct feedback, using the local concentration of the diffusing credit signal. Applied to recurrent spiki...

---

### 50. A Dynamical Systems and System Identification Framework for Phase Amplitude Coupling Analysis

**Authors:** Rajintha Gunawardena, Fei He

**Published:** 2026-03-09

🔗 [Paper](http://arxiv.org/abs/2603.08866v1) | 📄 [PDF](https://arxiv.org/pdf/2603.08866v1)

**Summary:** Phase-amplitude coupling (PAC), a form of cross-frequency interaction, has been implicated in various cognitive functions and, by extension, in neural communication and information integration. Accurately detecting and characterising PAC is essential for understanding its role in processes such as memory and attention. However, this remains a significant challenge. Most existing methods rely on variations in the temporal profile to detect PAC, but they often suffer from key limitations, most not...

---

## stat.ML

**50 papers**

### 1. Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels

**Authors:** Alexandra Zelenin, Alexandra Zhuravlyova

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22276v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22276v1)

**Summary:** Weight-Decomposed Low-Rank Adaptation (DoRA) extends LoRA by decoupling weight magnitude from direction, but its forward pass requires the row-wise norm of W + sBA, a computation that every major framework we surveyed implements by materializing the dense [d_out, d_in] product BA. At d_in = 8192 and rank r = 384, a single module's norm requires about 512 MB of transient working memory in bf16, making high-rank DoRA costly and often infeasible on common single-GPU setups once hundreds of adapted ...

---

### 2. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

**Authors:** Changxiao Cai, Gen Li

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22248v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22248v1)

**Summary:** Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, ...

---

### 3. Noise Titration: Exact Distributional Benchmarking for Probabilistic Time Series Forecasting

**Authors:** Qilin Wang

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22219v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22219v1)

**Summary:** Modern time series forecasting is evaluated almost entirely through passive observation of single historical trajectories, rendering claims about a model's robustness to non-stationarity fundamentally unfalsifiable. We propose a paradigm shift toward interventionist, exact-statistical benchmarking. By systematically titrating calibrated Gaussian observation noise into known chaotic and stochastic dynamical systems, we transform forecasting from a black-box sequence matching game into an exact di...

---

### 4. Identification of physiological shock in intensive care units via Bayesian regime switching models

**Authors:** Emmett B. Kendall, Jonathan P. Williams, Curtis B. Storlie, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22208v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22208v1)

**Summary:** Detection of occult hemorrhage (i.e., internal bleeding) in patients in intensive care units (ICUs) can pose significant challenges for critical care workers. Because blood loss may not always be clinically apparent, clinicians rely on monitoring vital signs for specific trends indicative of a hemorrhage event. The inherent difficulties of diagnosing such an event can lead to late intervention by clinicians which has catastrophic consequences. Therefore, a methodology for early detection of hemo...

---

### 5. Computationally lightweight classifiers with frequentist bounds on predictions

**Authors:** Shreeram Murali, Cristian R. Rojas, Dominik Baumann

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22128v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22128v1)

**Summary:** While both classical and neural network classifiers can achieve high accuracy, they fall short on offering uncertainty bounds on their predictions, making them unfit for safety-critical applications. Existing kernel-based classifiers that provide such bounds scale with $\mathcal O (n^{\sim3})$ in time, making them computationally intractable for large datasets. To address this, we propose a novel, computationally efficient classification algorithm based on the Nadaraya-Watson estimator, for whos...

---

### 6. MAGPI: Multifidelity-Augmented Gaussian Process Inputs for Surrogate Modeling from Scarce Data

**Authors:** Atticus Rex, Elizabeth Qian, David Peterson

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22050v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22050v1)

**Summary:** Supervised machine learning describes the practice of fitting a parameterized model to labeled input-output data. Supervised machine learning methods have demonstrated promise in learning efficient surrogate models that can (partially) replace expensive high-fidelity models, making many-query analyses, such as optimization, uncertainty quantification, and inference, tractable. However, when training data must be obtained through the evaluation of an expensive model or experiment, the amount of t...

---

### 7. On the Interplay of Priors and Overparametrization in Bayesian Neural Network Posteriors

**Authors:** Julius Kobialka, Emanuel Sommer, Chris Kolb, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22030v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22030v1)

**Summary:** Bayesian neural network (BNN) posteriors are often considered impractical for inference, as symmetries fragment them, non-identifiabilities inflate dimensionality, and weight-space priors are seen as meaningless. In this work, we study how overparametrization and priors together reshape BNN posteriors and derive implications allowing us to better understand their interplay. We show that redundancy introduces three key phenomena that fundamentally reshape the posterior geometry: balancedness, wei...

---

### 8. CRPS-Optimal Binning for Conformal Regression

**Authors:** Paolo Toccaceli

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.22000v1) | 📄 [PDF](https://arxiv.org/pdf/2603.22000v1)

**Summary:** We propose a method for non-parametric conditional distribution estimation based on partitioning covariate-sorted observations into contiguous bins and using the within-bin empirical CDF as the predictive distribution. Bin boundaries are chosen to minimise the total leave-one-out Continuous Ranked Probability Score (LOO-CRPS), which admits a closed-form cost function with $O(n^2 \log n)$ precomputation and $O(n^2)$ storage; the globally optimal $K$-partition is recovered by a dynamic programme i...

---

### 9. Structural Concentration in Weighted Networks: A Class of Topology-Aware Indices

**Authors:** L. Riso, M. G. Zoia

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21918v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21918v1)

**Summary:** This paper develops a unified framework for measuring concentration in weighted systems embedded in networks of interactions. While traditional indices such as the Herfindahl-Hirschman Index capture dispersion in weights, they neglect the topology of relationships among the elements receiving those weights. To address this limitation, we introduce a family of topology-aware concentration indices that jointly account for weight distributions and network structure. At the core of the framework lie...

---

### 10. On the Number of Conditional Independence Tests in Constraint-based Causal Discovery

**Authors:** Marc Franquesa Monés, Jiaqi Zhang, Caroline Uhler

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21844v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21844v1)

**Summary:** Learning causal relations from observational data is a fundamental problem with wide-ranging applications across many fields. Constraint-based methods infer the underlying causal structure by performing conditional independence tests. However, existing algorithms such as the prominent PC algorithm need to perform a large number of independence tests, which in the worst case is exponential in the maximum degree of the causal graph. Despite extensive research, it remains unclear if there exist alg...

---

### 11. A Job I Like or a Job I Can Get: Designing Job Recommender Systems Using Field Experiments

**Authors:** Guillaume Bied, Philippe Caillou, Bruno Crépon, et al.

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21699v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21699v1)

**Summary:** Recommendation systems (RSs) are increasingly used to guide job seekers on online platforms, yet the algorithms currently deployed are typically optimized for predictive objectives such as clicks, applications, or hires, rather than job seekers' welfare. We develop a job-search model with an application stage in which the value of a vacancy depends on two dimensions: the utility it delivers to the worker and the probability that an application succeeds. The model implies that welfare-optimal RSs...

---

### 12. Learning operators on labelled conditional distributions with applications to mean field control of non exchangeable systems

**Authors:** Samy Mekkaoui, Huyên Pham, Xavier Warin

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21683v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21683v1)

**Summary:** We study the approximation of operators acting on probability measures on a product space with prescribed marginal. Let $I$ be a label space endowed with a reference measure $λ$, and define $\cal M_λ$ as the set of probability measures on $I\times \mathbb{R}^d$ with first marginal $λ$. By disintegration, elements of $\cal M_λ$ correspond to families of labeled conditional distributions. Operators defined on this constrained measure space arise naturally in mean-field control problems with hetero...

---

### 13. CoNBONet: Conformalized Neuroscience-inspired Bayesian Operator Network for Reliability Analysis

**Authors:** Shailesh Garg, Souvik Chakraborty

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21678v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21678v1)

**Summary:** Time-dependent reliability analysis of nonlinear dynamical systems under stochastic excitations is a critical yet computationally demanding task. Conventional approaches, such as Monte Carlo simulation, necessitate repeated evaluations of computationally expensive numerical solvers, leading to significant computational bottlenecks. To address this challenge, we propose \textit{CoNBONet}, a neuroscience-inspired surrogate model that enables fast, energy-efficient, and uncertainty-aware reliabilit...

---

### 14. Neyman-Pearson multiclass classification under label noise via empirical likelihood

**Authors:** Qiong Zhang, Qinglong Tian, Pengfei Li

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21623v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21623v1)

**Summary:** In many classification problems, the costs of misclassifying observations from different classes can be highly unequal. The Neyman-Pearson multiclass classification (NPMC) framework addresses this issue by minimizing a weighted misclassification risk while imposing upper bounds on class-specific error probabilities. Existing NPMC methods typically assume that training labels are correctly observed. In practice, however, labels are often corrupted due to measurement error or annotation, and the e...

---

### 15. Rule-State Inference (RSI): A Bayesian Framework for Compliance Monitoring in Rule-Governed Domains

**Authors:** Abdou-Raouf Atarmla

**Published:** 2026-03-23

🔗 [Paper](http://arxiv.org/abs/2603.21610v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21610v1)

**Summary:** Existing machine learning frameworks for compliance monitoring -- Markov Logic Networks, Probabilistic Soft Logic, supervised models -- share a fundamental paradigm: they treat observed data as ground truth and attempt to approximate rules from it. This assumption breaks down in rule-governed domains such as taxation or regulatory compliance, where authoritative rules are known a priori and the true challenge is to infer the latent state of rule activation, compliance, and parametric drift from ...

---

### 16. A Generalised Exponentiated Gradient Approach to Enhance Fairness in Binary and Multi-class Classification Tasks

**Authors:** Maryam Boubekraoui, Giordano d'Aloisio, Antinisca Di Marco

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21393v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21393v1)

**Summary:** The widespread use of AI and ML models in sensitive areas raises significant concerns about fairness. While the research community has introduced various methods for bias mitigation in binary classification tasks, the issue remains under-explored in multi-class classification settings. To address this limitation, in this paper, we first formulate the problem of fair learning in multi-class classification as a multi-objective problem between effectiveness (i.e., prediction correctness) and multip...

---

### 17. Constrained Online Convex Optimization with Memory and Predictions

**Authors:** Mohammed Abdullah, George Iosifidis, Salah Eddine Elayoubi, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21375v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21375v1)

**Summary:** We study Constrained Online Convex Optimization with Memory (COCO-M), where both the loss and the constraints depend on a finite window of past decisions made by the learner. This setting extends the previously studied unconstrained online optimization with memory framework and captures practical problems such as the control of constrained dynamical systems and scheduling with reconfiguration budgets. For this problem, we propose the first algorithms that achieve sublinear regret and sublinear c...

---

### 18. Generalized Discrete Diffusion from Snapshots

**Authors:** Oussama Zekri, Théo Uscidda, Nicolas Boullé, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21342v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21342v1)

**Summary:** We introduce Generalized Discrete Diffusion from Snapshots (GDDS), a unified framework for discrete diffusion modeling that supports arbitrary noising processes over large discrete state spaces. Our formulation encompasses all existing discrete diffusion approaches, while allowing significantly greater flexibility in the choice of corruption dynamics. The forward noising process relies on uniformization and enables fast arbitrary corruption. For the reverse process, we derive a simple evidence l...

---

### 19. Closed-form conditional diffusion models for data assimilation

**Authors:** Brianna Binder, Assad Oberai

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21291v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21291v1)

**Summary:** We propose closed-form conditional diffusion models for data assimilation. Diffusion models use data to learn the score function (defined as the gradient of the log-probability density of a data distribution), allowing them to generate new samples from the data distribution by reversing a noise injection process. While it is common to train neural networks to approximate the score function, we leverage the analytical tractability of the score function to assimilate the states of a system with me...

---

### 20. Accelerate Vector Diffusion Maps by Landmarks

**Authors:** Sing-Yuan Yeh, Yi-An Wu, Hau-Tieng Wu, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21247v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21247v1)

**Summary:** We propose a landmark-constrained algorithm, LA-VDM (Landmark Accelerated Vector Diffusion Maps), to accelerate the Vector Diffusion Maps (VDM) framework built upon the Graph Connection Laplacian (GCL), which captures pairwise connection relationships within complex datasets. LA-VDM introduces a novel two-stage normalization that effectively address nonuniform sampling densities in both the data and the landmark sets. Under a manifold model with the frame bundle structure, we show that we can ac...

---

### 21. Domain Elastic Transform: Bayesian Function Registration for High-Dimensional Scientific Data

**Authors:** Osamu Hirose, Emanuele Rodola

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21235v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21235v1)

**Summary:** Nonrigid registration is conventionally divided into point set registration, which aligns sparse geometries, and image registration, which aligns continuous intensity fields on regular grids. However, this dichotomy creates a critical bottleneck for emerging scientific data, such as spatial transcriptomics, where high-dimensional vector-valued functions, e.g., gene expression, are defined on irregular, sparse manifolds. Consequently, researchers currently face a forced choice: either sacrifice s...

---

### 22. On the Role of Batch Size in Stochastic Conditional Gradient Methods

**Authors:** Rustem Islamov, Roman Machacek, Aurelien Lucchi, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21191v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21191v1)

**Summary:** We study the role of batch size in stochastic conditional gradient methods under a $μ$-Kurdyka-Łojasiewicz ($μ$-KL) condition. Focusing on momentum-based stochastic conditional gradient algorithms (e.g., Scion), we derive a new analysis that explicitly captures the interaction between stepsize, batch size, and stochastic noise. Our study reveals a regime-dependent behavior: increasing the batch size initially improves optimization accuracy but, beyond a critical threshold, the benefits saturate ...

---

### 23. ALMAB-DC: Active Learning, Multi-Armed Bandits, and Distributed Computing for Sequential Experimental Design and Black-Box Optimization

**Authors:** Foo Hui-Mean, Yuan-chin I Chang

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21180v1)

**Summary:** Sequential experimental design under expensive, gradient-free objectives is a central challenge in computational statistics: evaluation budgets are tightly constrained and information must be extracted efficiently from each observation. We propose \textbf{ALMAB-DC}, a GP-based sequential design framework combining active learning, multi-armed bandits (MAB), and distributed asynchronous computing for expensive black-box experimentation. A Gaussian process surrogate with uncertainty-aware acquisit...

---

### 24. Time-adaptive functional Gaussian Process regression

**Authors:** MD Ruiz-Medina, AE Madrid, A Torres-Signes, et al.

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21144v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21144v1)

**Summary:** This paper proposes a new formulation of functional Gaussian Process regression in manifolds, based on an Empirical Bayes approach, in the spatiotemporal random field context. We apply the machinery of tight Gaussian measures in separable Hilbert spaces, exploiting the invariance property of covariance kernels under the group of isometries of the manifold. The identification of these measures with infinite-product Gaussian measures is then obtained via the eigenfunctions of the Laplace-Beltrami ...

---

### 25. Stochastic approximation in non-markovian environments revisited

**Authors:** Vivek Shripad Borkar

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21091v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21091v1)

**Summary:** Based on some recent work of the author on stochastic approximation in non-markovian environments, the situation when the driving random process is non-ergodic in addition to being non-markovian is considered. Using this, we propose an analytic framework for understanding transformer based learning, specifically, the `attention' mechanism, and continual learning, both of which depend on the entire past in principle.

---

### 26. Gradient Descent with Projection Finds Over-Parameterized Neural Networks for Learning Low-Degree Polynomials with Nearly Minimax Optimal Rate

**Authors:** Yingzhen Yang, Ping Li

**Published:** 2026-03-22

🔗 [Paper](http://arxiv.org/abs/2603.21062v1) | 📄 [PDF](https://arxiv.org/pdf/2603.21062v1)

**Summary:** We study the problem of learning a low-degree spherical polynomial of degree $k_0 = Θ(1) \ge 1$ defined on the unit sphere in $\RR^d$ by training an over-parameterized two-layer neural network with augmented feature in this paper. Our main result is the significantly improved sample complexity for learning such low-degree polynomials. We show that, for any regression risk $\eps \in (0, Θ(d^{-k_0})]$, an over-parameterized two-layer neural network trained by a novel Gradient Descent with Projecti...

---

### 27. From Causal Discovery to Dynamic Causal Inference in Neural Time Series

**Authors:** Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20980v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20980v1)

**Summary:** Time-varying causal models provide a powerful framework for studying dynamic scientific systems, yet most existing approaches assume that the underlying causal network is known a priori - an assumption rarely satisfied in real-world domains where causal structure is uncertain, evolving, or only indirectly observable. This limits the applicability of dynamic causal inference in many scientific settings. We propose Dynamic Causal Network Autoregression (DCNAR), a two-stage neural causal modeling f...

---

### 28. Hard labels sampled from sparse targets mislead rotation invariant algorithms

**Authors:** Avrajit Ghosh, Bin Yu, Manfred Warmuth, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20967v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20967v1)

**Summary:** One of the most common machine learning setups is logistic regression. In many classification models, including neural networks, the final prediction is obtained by applying a logistic link function to a linear score. In binary logistic regression, the feedback can be either soft labels, corresponding to the true conditional probability of the data (as in distillation), or sampled hard labels (taking values $\pm 1$). We point out a fundamental problem that arises even in a particularly favorable...

---

### 29. Integrative Learning of Dynamically Evolving Multiplex Graphs and Nodal Attributes Using Neural Network Gaussian Processes with an Application to Dynamic Terrorism Graphs

**Authors:** Jose Rodriguez-Acosta, Sharmistha Guha, Lekha Patel, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20962v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20962v1)

**Summary:** Exploring the dynamic co-evolution of multiplex graphs and nodal attributes is a compelling question in criminal and terrorism networks. This article is motivated by the study of dynamically evolving interactions among prominent terrorist organizations, considering various organizational attributes like size, ideology, leadership, and operational capacity. Statistically principled integration of multiplex graphs with nodal attributes is significantly challenging due to the need to leverage share...

---

### 30. User Preference Modeling for Conversational LLM Agents: Weak Rewards from Retrieval-Augmented Interaction

**Authors:** Yuren Hao, Shuhaib Mehri, ChengXiang Zhai, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20939v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20939v1)

**Summary:** Large language models are increasingly used as personal assistants, yet most lack a persistent user model, forcing users to repeatedly restate preferences across sessions. We propose Vector-Adapted Retrieval Scoring (VARS), a pipeline-agnostic, frozen-backbone framework that represents each user with long-term and short-term vectors in a shared preference space and uses these vectors to bias retrieval scoring over structured preference memory. The vectors are updated online from weak scalar rewa...

---

### 31. Two Approaches to Direct Estimation of Riesz Representers

**Authors:** David Bruns-Smith

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20936v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20936v1)

**Summary:** The Riesz representer is a central object in semiparametric statistics and debiased/doubly-robust estimation. Two literatures in econometrics have highlighted the role for directly estimating Riesz representers: the automatic debiased machine learning literature (as in Chernozhukov et al., 2022b), and an independent literature on sieve methods for conditional moment models (as in Chen et al., 2014). These two literatures solve distinct optimization problems that in the population both have the R...

---

### 32. Stability of Sequential and Parallel Coordinate Ascent Variational Inference

**Authors:** Debdeep Pati

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20929v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20929v1)

**Summary:** We highlight a striking difference in behavior between two widely used variants of coordinate ascent variational inference: the sequential and parallel algorithms. While such differences were known in the numerical analysis literature in simpler settings, they remain largely unexplored in the optimization-focused literature on variational inference in more complex models. Focusing on the moderately high-dimensional linear regression problem, we show that the sequential algorithm, although typica...

---

### 33. Active Inference for Physical AI Agents -- An Engineering Perspective

**Authors:** Bert de Vries

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20927v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20927v1)

**Summary:** Physical AI agents, such as robots and other embodied systems operating under tight and fluctuating resource constraints, remain far less capable than biological agents in open-ended real-world environments. This paper argues that Active Inference (AIF), grounded in the Free Energy Principle, offers a principled foundation for closing that gap. We develop this argument from first principles, following a chain from probability theory through Bayesian machine learning and variational inference to ...

---

### 34. Bayesian Scattering: A Principled Baseline for Uncertainty on Image Data

**Authors:** Bernardo Fichera, Zarko Ivkovic, Kjell Jorner, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20908v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20908v1)

**Summary:** Uncertainty quantification for image data is dominated by complex deep learning methods, yet the field lacks an interpretable, mathematically grounded baseline. We propose Bayesian scattering to fill this gap, serving as a first-step baseline akin to the role of Bayesian linear regression for tabular data. Our method couples the wavelet scattering transform-a deep, non-learned feature extractor-with a simple probabilistic head. Because scattering features are derived from geometric principles ra...

---

### 35. Sparse Weak-Form Discovery of Stochastic Generators

**Authors:** Eshwar R A, Gajanan V. Honnavar

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20904v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20904v1)

**Summary:** We introduce a framework for the data-driven discovery of stochastic differential equations (SDEs) that unifies, for the first time, the weak-form integration-by-parts approach of Weak SINDy with the stochastic system identification goal of stochastic SINDy. The central novelty is the adoption of spatial Gaussian test functions $K_j(x)=\exp(-|x-x_j|^2/2h^2)$ in place of temporal test functions. Because the kernel weight $K_j(X_{t_n})$ is $\mathcal{F}_{t_n}$-measurable and the Brownian innovation...

---

### 36. Unfolding with a Wasserstein Loss

**Authors:** Katy Craig, Benjamin Faktor, Benjamin Nachman

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20903v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20903v1)

**Summary:** Data unfolding -- the removal of noise or artifacts from measurements -- is a fundamental task across the experimental sciences. Of particular interest are applications in physics, where the dominant approach is Richardson-Lucy (RL) deconvolution. The classical RL approach aims to find denoised data that, once passed through the noise model, is as close as possible to the measured data in terms of Kullback-Leibler (KL) divergence. This requires that the support of the measured data overlaps with...

---

### 37. Auto-differentiable data assimilation: Co-learning of states, dynamics, and filtering algorithms

**Authors:** Melissa Adrian, Daniel Sanz-Alonso, Rebecca Willett

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20891v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20891v1)

**Summary:** Data assimilation algorithms estimate the state of a dynamical system from partial observations, where the successful performance of these algorithms hinges on costly parameter tuning and on employing an accurate model for the dynamics. This paper introduces a framework for jointly learning the state, dynamics, and parameters of filtering algorithms in data assimilation through a process we refer to as auto-differentiable filtering. The framework leverages a theoretically motivated loss function...

---

### 38. Achieving $\widetilde{O}(1/ε)$ Sample Complexity for Bilinear Systems Identification under Bounded Noises

**Authors:** Hongyu Yi, Chenbei Lu, Jing Yu

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20819v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20819v1)

**Summary:** This paper studies finite-sample set-membership identification for discrete-time bilinear systems under bounded symmetric log-concave disturbances. Compared with existing finite-sample results for linear systems and related analyses under stronger noise assumptions, we consider the more challenging bilinear setting with trajectory-dependent regressors and allow marginally stable dynamics with polynomial mean-square state growth. Under these conditions, we prove that the diameter of the feasible ...

---

### 39. High-dimensional online learning via asynchronous decomposition: Non-divergent results, dynamic regularization, and beyond

**Authors:** Shixiang Liu, Zhifan Li, Hanming Yang, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20696v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20696v1)

**Summary:** Existing high-dimensional online learning methods often face the challenge that their error bounds, or per-batch sample sizes, diverge as the number of data batches increases. To address this issue, we propose an asynchronous decomposition framework that leverages summary statistics to construct a surrogate score function for current-batch learning. This framework is implemented via a dynamic-regularized iterative hard thresholding algorithm, providing a computationally and memory-efficient solu...

---

### 40. Breaking the $O(\sqrt{T})$ Cumulative Constraint Violation Barrier while Achieving $O(\sqrt{T})$ Static Regret in Constrained Online Convex Optimization

**Authors:** Haricharan Balasundaram, Karthick Krishna Mahendran, Rahul Vaze

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20671v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20671v1)

**Summary:** The problem of constrained online convex optimization is considered, where at each round, once a learner commits to an action $x_t \in \mathcal{X} \subset \mathbb{R}^d$, a convex loss function $f_t$ and a convex constraint function $g_t$ that drives the constraint $g_t(x)\le 0$ are revealed. The objective is to simultaneously minimize the static regret and cumulative constraint violation (CCV) compared to the benchmark that knows the loss functions and constraint functions $f_t$ and $g_t$ for al...

---

### 41. Sinkhorn Based Associative Memory Retrieval Using Spherical Hellinger Kantorovich Dynamics

**Authors:** Aratrika Mustafi, Soumya Mukherjee

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20656v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20656v1)

**Summary:** We propose a dense associative memory for empirical measures (weighted point clouds). Stored patterns and queries are finitely supported probability measures, and retrieval is defined by minimizing a Hopfield-style log-sum-exp energy built from the debiased Sinkhorn divergence. We derive retrieval dynamics as a spherical Hellinger Kantorovich (SHK) gradient flow, which updates both support locations and weights. Discretizing the flow yields a deterministic algorithm that uses Sinkhorn potentials...

---

### 42. Exponential Family Discriminant Analysis: Generalizing LDA-Style Generative Classification to Non-Gaussian Models

**Authors:** Anish Lakkapragada

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20655v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20655v1)

**Summary:** We introduce Exponential Family Discriminant Analysis (EFDA), a unified generative framework that extends classical Linear Discriminant Analysis (LDA) beyond the Gaussian setting to any member of the exponential family. Under the assumption that each class-conditional density belongs to a common exponential family, EFDA derives closed-form maximum-likelihood estimators for all natural parameters and yields a decision rule that is linear in the sufficient statistic, recovering LDA as a special ca...

---

### 43. LassoFlexNet: Flexible Neural Architecture for Tabular Data

**Authors:** Kry Yik Chau Lui, Cheng Chi, Kishore Basu, et al.

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20631v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20631v1)

**Summary:** Despite their dominance in vision and language, deep neural networks often underperform relative to tree-based models on tabular data. To bridge this gap, we incorporate five key inductive biases into deep learning: robustness to irrelevant features, axis alignment, localized irregularities, feature heterogeneity, and training stability. We propose \emph{LassoFlexNet}, an architecture that evaluates the linear and nonlinear marginal contribution of each input via Per-Feature Embeddings, and spar...

---

### 44. Interpretable Operator Learning for Inverse Problems via Adaptive Spectral Filtering: Convergence and Discretization Invariance

**Authors:** Hang-Cheng Dong, Pengcheng Cheng, Shuhuan Li

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20602v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20602v1)

**Summary:** Solving ill-posed inverse problems necessitates effective regularization strategies to stabilize the inversion process against measurement noise. While classical methods like Tikhonov regularization require heuristic parameter tuning, and standard deep learning approaches often lack interpretability and generalization across resolutions, we propose SC-Net (Spectral Correction Network), a novel operator learning framework. SC-Net operates in the spectral domain of the forward operator, learning a...

---

### 45. RECLAIM: Cyclic Causal Discovery Amid Measurement Noise

**Authors:** Muralikrishnna G. Sethuraman, Faramarz Fekri

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20585v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20585v1)

**Summary:** Uncovering causal relationships is a fundamental problem across science and engineering. However, most existing causal discovery methods assume acyclicity and direct access to the system variables -- assumptions that fail to hold in many real-world settings. For instance, in genomics, cyclic regulatory networks are common, and measurements are often corrupted by instrumental noise. To address these challenges, we propose RECLAIM, a causal discovery framework that natively handles both cycles and...

---

### 46. Generative Diffusion Model for Risk-Neutral Derivative Pricing

**Authors:** Nilay Tiwari

**Published:** 2026-03-21

🔗 [Paper](http://arxiv.org/abs/2603.20582v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20582v1)

**Summary:** Denoising diffusion probabilistic models (DDPMs) have emerged as powerful generative models for complex distributions, yet their use in arbitrage-free derivative pricing remains largely unexplored. Financial asset prices are naturally modeled by stochastic differential equations (SDEs), whose forward and reverse density evolution closely parallels the forward noising and reverse denoising structure of diffusion models.   In this paper, we develop a framework for using DDPMs to generate risk-neut...

---

### 47. Understanding Behavior Cloning with Action Quantization

**Authors:** Haoqun Cao, Tengyang Xie

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20538v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20538v1)

**Summary:** Behavior cloning is a fundamental paradigm in machine learning, enabling policy learning from expert demonstrations across robotics, autonomous driving, and generative models. Autoregressive models like transformer have proven remarkably effective, from large language models (LLMs) to vision-language-action systems (VLAs). However, applying autoregressive models to continuous control requires discretizing actions through quantization, a practice widely adopted yet poorly understood theoretically...

---

### 48. Does This Gradient Spark Joy?

**Authors:** Ian Osband

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20526v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20526v1)

**Summary:** Policy gradient computes a backward pass for every sample, even though the backward pass is expensive and most samples carry little learning value. The Delightful Policy Gradient (DG) provides a forward-pass signal of learning value: \emph{delight}, the product of advantage and surprisal (negative log-probability). We introduce the \emph{Kondo gate}, which compares delight against a compute price and pays for a backward pass only when the sample is worth it, thereby tracing a quality--cost Paret...

---

### 49. Delightful Distributed Policy Gradient

**Authors:** Ian Osband

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20521v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20521v1)

**Summary:** Distributed reinforcement learning trains on data from stale, buggy, or mismatched actors, producing actions with high surprisal (negative log-probability) under the learner's policy. The core difficulty is not surprising data per se, but \emph{negative learning from surprising data}. High-surprisal failures can dominate the update direction despite carrying little useful signal, while high-surprisal successes reveal opportunities the current policy would otherwise miss. The \textit{Delightful P...

---

### 50. CogFormer: Learn All Your Models Once

**Authors:** Jerry M. Huang, Lukas Schumacher, Niek Stevenson, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20520v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20520v1)

**Summary:** Simulation-based inference (SBI) with neural networks has accelerated and transformed cognitive modeling workflows. SBI enables modelers to fit complex models that were previously difficult or impossible to estimate, while also allowing rapid estimation across large numbers of datasets. However, the utility of SBI for iterating over varying modeling assumptions remains limited: changing parameterizations, generative functions, priors, and design variables all necessitate model retraining and hen...

---

