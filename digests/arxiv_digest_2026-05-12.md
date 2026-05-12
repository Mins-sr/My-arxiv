# arXiv Daily Digest - 2026-05-12

Total papers: 350

---

## cs.AI

**50 papers**

### 1. ELF: Embedded Language Flows

**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10938v1)

**Summary:** Diffusion and flow-based models have become the de facto approaches for generating continuous data, e.g., in domains such as images and videos. Their success has attracted growing interest in applying them to language modeling. Unlike their image-domain counterparts, today's leading diffusion language models (DLMs) primarily operate over discrete tokens. In this paper, we show that continuous DLMs can be made effective with minimal adaptation to the discrete domain. We propose Embedded Language ...

---

### 2. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10934v1)

**Summary:** Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are eff...

---

### 3. Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition

**Authors:** Md. Sultan Al Rayhan, Maheen Islam

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10916v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10916v1)

**Summary:** Recognition of handwritten Bangla compound characters remains a challenging problem due to complex character structures, large intra-class variation, and limited availability of high-quality annotated data. Existing Bangla handwritten character recognition systems often struggle to generalize across diverse writing styles, particularly for compound characters containing intricate ligatures and diacritical variations. In this work, we propose a confidence-guided diffusion augmentation framework f...

---

### 4. Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace

**Authors:** Simon Yu, Derek Chong, Ananjan Nandi, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10913v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10913v1)

**Summary:** We introduce Shepherd, a functional programming model that formalizes meta-agent operations on target agents as functions, with core operations mechanized in Lean. Shepherd records every agent-environment interaction as a typed event in a Git-like execution trace, enabling any past state to be forked and replayed. The system forks the agent process and its filesystem $5\times$ faster than Docker, achieving $>95\%$ prompt-cache reuse on replay. We demonstrate the model through three applications....

---

### 5. Engineering Robustness into Personal Agents with the AI Workflow Store

**Authors:** Roxana Geambasu, Mariana Raykova, Pierre Tholoniat, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10907v1)

**Summary:** The dominant paradigm for AI agents is an "on-the-fly" loop in which agents synthesize plans and execute actions within seconds or minutes in response to user prompts. We argue that this paradigm short-circuits disciplined software engineering (SE) processes -- iterative design, rigorous testing, adversarial evaluation, staged deployment, and more -- that have delivered the (relatively) reliable and secure systems we use today. By focusing on rapid, real-time synthesis, are AI agents effectively...

---

### 6. DataMaster: Towards Autonomous Data Engineering for Machine Learning

**Authors:** Yaxin Du, Xiyuan Yang, Zhifan Zhou, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10906v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10906v1)

**Summary:** As model families, training recipes, and compute budgets become increasingly standardized, further gains in machine learning systems depend increasingly on data. Yet data engineering remains largely manual and ad hoc: practitioners repeatedly search for external datasets, adapt them to existing pipelines, validate candidate data through downstream training, and carry forward lessons from prior attempts. We study task-conditioned autonomous data engineering, where an autonomous agent improves a f...

---

### 7. Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why

**Authors:** Mohammadreza Armandpour, Fatih Ilhan, David Harrison, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10889v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10889v1)

**Summary:** On-policy distillation offers dense, per-token supervision for training reasoning models; however, it remains unclear under which conditions this signal is beneficial and under which it is detrimental. Which teacher model should be used, and in the case of self-distillation, which specific context should serve as the supervisory signal? Does the optimal choice vary from one token to the next? At present, addressing these questions typically requires costly training runs whose aggregate performan...

---

### 8. Shields to Guarantee Probabilistic Safety in MDPs

**Authors:** Linus Heck, Filip Macák, Roman Andriushchenko, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10888v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10888v1)

**Summary:** Shielding is a prominent model-based technique to ensure safety of autonomous agents. Classical shielding aims to ensure that nothing bad ever happens and comes with strong guarantees about safety and maximal permissiveness. However, shielding systems for probabilistic safety, where something bad is allowed to happen with an acceptable probability, has proven to be more intricate. This paper presents a formal framework that conservatively extends classical shields to probabilistic safety. In thi...

---

### 9. LoKA: Low-precision Kernel Applications for Recommendation Models At Scale

**Authors:** Liang Luo, Yinbin Ma, Quanyu Zhu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10886v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10886v1)

**Summary:** Recent GPU generations deliver significantly higher FLOPs using lower-precision arithmetic, such as FP8. While successfully applied to large language models (LLMs), its adoption in large recommendation models (LRMs) has been limited. This is because LRMs are numerically sensitive, dominated by small matrix multiplications (GEMMs) followed by normalization, and trained in communication-intensive environments. Applying FP8 directly to LRMs often degrades model quality and prolongs training time. T...

---

### 10. AssayBench: An Assay-Level Virtual Cell Benchmark for LLMs and Agents

**Authors:** Edward De Brouwer, Carl Edwards, Alexander Wu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10876v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10876v1)

**Summary:** Recent advances in machine learning and large-scale biological data collections have revived the prospect of building a virtual cell, a computational model of cellular behavior that could accelerate biological discovery. One of the most compelling promises of this vision is the ability to perform in silico phenotypic screens, in which a model predicts the effects of cellular perturbations in unseen biological contexts. This task combines heterogeneous textual inputs with diverse phenotypic outpu...

---

### 11. CADBench: A Multimodal Benchmark for AI-Assisted CAD Program Generation

**Authors:** Anna C. Doris, Jacob Thomas Sony, Ghadi Nehme, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10873v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10873v1)

**Summary:** Recovering editable CAD programs from images or 3D observations is central to AI-assisted design, but progress is difficult to measure because existing evaluations are fragmented across datasets, modalities, and metrics. We introduce CADBench, a unified benchmark for multimodal CAD program generation. CADBench contains 18,000 evaluation samples spanning six benchmark families derived from DeepCAD, Fusion 360, ABC, MCB, and Objaverse; five input modalities including clean meshes, noisy meshes, si...

---

### 12. Attractor-Vascular Coupling Theory: Formal Grounding and Empirical Validation for AAMI-Standard Cuffless Blood Pressure Estimation from Smartphone Photoplethysmography

**Authors:** Timothy Oladunni, Farouk Ganiyu Adewumi

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10871v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10871v1)

**Summary:** This work proposes Attractor-Vascular Coupling Theory (AVCT), a mathematical framework showing that cardiac attractor geometry encodes blood pressure (BP) information sufficient for AAMI-standard estimation, and validates the theory through a calibrated cuffless BP model using photoplethysmography (PPG). AVCT is grounded in Cardiac Stability Theory and operationalized using Takens delay embedding and attractor morphology extraction. Two theorems, one proposition, and one corollary formally justi...

---

### 13. Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory

**Authors:** Mingxi Zou, Zhihan Guo, Langzhang Liang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10870v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10870v1)

**Summary:** Long-horizon language agents must operate under limited runtime memory, yet existing memory mechanisms often organize experience around descriptive criteria such as relevance, salience, or summary quality. For an agent, however, memory is valuable not because it faithfully describes the past, but because it preserves the distinctions between histories that must remain separated under a fixed budget to support good decisions. We cast this as a decision-centric rate-distortion problem, measuring m...

---

### 14. BEACON: A Multimodal Dataset for Learning Behavioral Fingerprints from Gameplay Data

**Authors:** Ishpuneet Singh, Gursmeep Kaur, Uday Pratap Singh Atwal, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10867v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10867v1)

**Summary:** Continuous authentication in high-stakes digital environments requires datasets with fine-grained behavioral signals under realistic cognitive and motor demands. But current benchmarks are often limited by small scale, unimodal sensing or lack of synchronised environmental context. To address this gap, this paper introduces BEACON ( Behavioral Engine for Authentication \& Continuous Monitoring), a large-scale multimodal dataset that captures diverse skill tiers in competitive \textit{Valorant} g...

---

### 15. BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD

**Authors:** Haozhe Zhang, Kaichen Liu, Miaomiao Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10865v1)

**Summary:** Industrial Computer-Aided Design (CAD) code generation requires models to produce executable parametric programs from visual or textual inputs. Beyond recognizing the outer shape of a part, this task involves understanding its 3D structure, inferring engineering parameters, and choosing CAD operations that reflect how the part would be designed and manufactured. Despite the promise of Multimodal large language models (MLLMs) for this task, they are rarely evaluated on whether these capabilities ...

---

### 16. The Generalized Turing Test: A Foundation for Comparing Intelligence

**Authors:** Daniel Mitropolsky, Susan S. Hong, Riccardo Neumarker, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10851v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10851v1)

**Summary:** We introduce the Generalized Turing Test (GTT), a formal framework for comparing the capabilities of arbitrary agents via indistinguishability. For agents A and B, we define the Turing comparator A $\geq$ B to hold if B, acting as a distinguisher, cannot reliably distinguish between interactions with A (instructed to imitate B) and another instance of B. This yields a dataset- and task-agnostic notion of relative intelligence. We study the comparator's structure, including conditions under which...

---

### 17. Rethinking Agentic Search with Pi-Serini: Is Lexical Retrieval Sufficient?

**Authors:** Tz-Huan Hsu, Jheng-Hong Yang, Jimmy Lin

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10848v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10848v1)

**Summary:** Does a lexical retriever suffice as large language models (LLMs) become more capable in an agentic loop? This question naturally arises when building deep research systems. We revisit it by pairing BM25 with frontier LLMs that have better reasoning and tool-use abilities. To support researchers asking the same question, we introduce Pi-Serini, a search agent equipped with three tools for retrieving, browsing, and reading documents. Our results show that, on BrowseComp-Plus, a well-configured lex...

---

### 18. Training-Free Cultural Alignment of Large Language Models via Persona Disagreement

**Authors:** Huynh Trung Kiet, Dao Sy Duy Minh, Tuan Nguyen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10843v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10843v1)

**Summary:** Large language models increasingly mediate decisions that turn on moral judgement, yet a growing body of evidence shows that their implicit preferences are not culturally neutral. Existing cultural alignment methods either require per-country preference data and fine-tuning budgets or assume white-box access to model internals that commercial APIs do not expose. In this work, we focus on this realistic black-box, public-data-only regime and observe that within-country sociodemographic disagreeme...

---

### 19. Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories

**Authors:** Yixuan Yang, Mehak Arora, Ryan Zhang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10840v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10840v1)

**Summary:** We present Clin-JEPA, a multi-phase co-training framework for joint-embedding predictive (JEPA) pretraining on EHR patient trajectories. JEPA architectures have enabled latent-space planning in robotics and high-quality representation learning in vision, but extending the paradigm to EHR data -- to obtain a single backbone that simultaneously forecasts patient trajectories and serves diverse downstream risk-prediction tasks without per-task fine-tuning -- remains an open challenge. Existing JEPA...

---

### 20. From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World

**Authors:** Pedro Conde, Henrique Branquinho, Valerio Mazzone, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10834v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10834v1)

**Summary:** AI pentesting agents are increasingly credible as offensive security systems, but current benchmarks still provide limited guidance on which will perform best in real-world targets. Existing evaluation protocols assess and optimize for predefined goals such as capture-the-flag, remote code execution, exploit reproduction, or trajectory similarity, in simplified or narrow settings. These tools are valuable for measuring bounded capabilities, yet they do not adequately capture the complexity, open...

---

### 21. MMVIAD: Multi-view Multi-task Video Understanding for Industrial Anomaly Detection

**Authors:** Xiran Zhao, Jing Jin, Yan Bai, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10833v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10833v1)

**Summary:** Industrial anomaly detection is critical for manufacturing quality control, yet existing datasets mainly focus on static images or sparse views, which do not fully reflect continuous inspection processes in real industrial scenarios. We introduce MMVIAD (Multi-view Multi-task Video Industrial Anomaly Detection), to the best of our knowledge the first continuous multi-view video dataset for industrial anomaly detection and understanding, together with a benchmark for multi-task evaluation. MMVIAD...

---

### 22. SLIM: Sparse Latent Steering for Interpretable and Property-Directed LLM-Based Molecular Editing

**Authors:** Mingxu Zhang, Yuhan Li, Lujundong Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10831v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10831v1)

**Summary:** Large language models possess strong chemical reasoning capabilities, making them effective molecular editors. However, property-relevant information is implicitly entangled across their dense hidden states, providing no explicit handle for property control: a substantial fraction of edits fail to improve or even degrade target properties. To address these issues, we propose SLIM (Sparse Latent Interpretable Molecular editing), a plug-and-play framework that decomposes the editor's hidden states...

---

### 23. The First Drop of Ink: Nonlinear Impact of Misleading Information in Long-Context Reasoning

**Authors:** Muhan Gao, Zih-Ching Chen, Kuan-Hao Huang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10828v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10828v1)

**Summary:** As large language models are increasingly deployed in retrieval-augmented generation and agentic systems that accumulate extensive context, understanding how distracting information affects long-context performance becomes critical. Prior work shows that semantically relevant yet misleading documents degrade performance, but the quantitative relationship between the proportion of distractors and performance remains unstudied. In this work, we systematically vary the hard-distractor proportion in...

---

### 24. MaD Physics: Evaluating information seeking under constraints in physical environments

**Authors:** Moksh Jain, Mehdi Bennani, Johannes Bausch, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10820v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10820v1)

**Summary:** Scientific discovery is fundamentally a resource-constrained process that requires navigating complex trade-offs between the quality and quantity of measurements due to physical and cost constraints. Measurements drive the scientific process by revealing novel phenomena to improve our understanding. Existing benchmarks for evaluating agents for scientific discovery focus on either static knowledge-based reasoning or unconstrained experimental design tasks, and do not capture the ability to make ...

---

### 25. ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models

**Authors:** Zuojin Tang, Haoyun Liu, Xinyuan Chang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10819v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10819v1)

**Summary:** Vision-language-action (VLA) models remain constrained by the scarcity of action-labeled robot data, whereas action-free videos provide abundant evidence of how the physical world changes. Latent action models offer a promising way to extract such priors from videos, but reconstruction-trained latent codes are not necessarily suitable for policy generation: they may predict future observations while lacking the structure needed to be reused or generated coherently with robot actions. We introduc...

---

### 26. CLEF: EEG Foundation Model for Learning Clinical Semantics

**Authors:** Peng Cao, Ali Mirzazadeh, Jong Woo Lee, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10817v1)

**Summary:** Clinical EEG interpretation requires reasoning over full EEG sessions and integrating signal patterns with clinical context. Existing EEG foundation models are largely designed for short-window decoding and do not incorporate clinical context. We introduce CLEF, a clinically grounded long-context EEG foundation model. CLEF represents EEG sessions as 3D multitaper spectrogram tokens, enabling tractable Transformer modeling at session scale, and aligns embeddings with neurologist reports and struc...

---

### 27. Policy Gradient Methods for Non-Markovian Reinforcement Learning

**Authors:** Avik Kar, Siddharth Chandak, Rahul Singh, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10816v1)

**Summary:** We study policy gradient methods for reinforcement learning in non-Markovian decision processes (NMDPs), where observations and rewards depend on the entire interaction history. To handle this dependence, the agent maintains an internal state that is recursively updated to provide a compact summary of past observations and actions. In contrast to approaches that treat the agent state dynamics as fixed or learn it via predictive objectives, we propose a reward-centric formulation that jointly opt...

---

### 28. Probing Cross-modal Information Hubs in Audio-Visual LLMs

**Authors:** Jihoo Jung, Chaeyoung Jung, Ji-Hoon Kim, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10815v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10815v1)

**Summary:** Audio-visual large language models (AVLLMs) have recently emerged as a powerful architecture capable of jointly reasoning over audio, visual, and textual modalities. In AVLLMs, the bidirectional interaction between audio and video modalities introduces intricate processing dynamics, necessitating a deeper understanding of their internal mechanisms. However, unlike extensively studied text-only or large vision language models, the internal workings of AVLLMs remain largely unexplored. In this pap...

---

### 29. NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation

**Authors:** Jinhang Xu, Qiyuan Zhu, Yujun Wu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10813v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10813v1)

**Summary:** LLM-powered multi-agent systems can now automate the full research pipeline from ideation to paper writing, but a fundamental question remains: automation for whom? Researchers operate under different resource configurations, hold different methodological preferences, and target different output formats. A system that produces uniform outputs regardless of these differences will systematically under-serve every individual user, making personalization a precondition for research automation to be ...

---

### 30. Switching-Geometry Analysis of Deflated Q-Value Iteration

**Authors:** Donghwan Lee

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10811v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10811v1)

**Summary:** This paper develops a joint spectral radius (JSR) framework for analyzing rank-one deflated Q-value iteration (Q-VI) in discounted Markov decision process control. Focusing on an all-ones residual correction, we interpret the resulting algorithm through the geometry of switching systems and, to the best of our knowledge, give the first JSR-based convergence analysis of deflated Q-VI for policy optimization problems. Our analysis reveals that the standard Q-VI switching system model has JSR exact...

---

### 31. Threat Modelling using Domain-Adapted Language Models: Empirical Evaluation and Insights

**Authors:** Saba Pourhanifeh, AbdulAziz AbdulGhaffar, Ashraf Matrawy

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10808v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10808v1)

**Summary:** Large Language Models(LLMs) are increasingly explored for cybersecurity applications such as vulnerability detection. In the domain of threat modelling, prior work has primarily evaluated a number of general-purpose Large Language Models under limited prompting settings. In this study, we extend the research area of structured threat modelling by systematically evaluating domain-adapted language models of different sizes to their general counterparts. We use both LLMs and Small Language Models(S...

---

### 32. PhyGround: Benchmarking Physical Reasoning in Generative World Models

**Authors:** Juyi Lin, Arash Akbari, Yumei He, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10806v1)

**Summary:** Generative world models are increasingly used for video generation, where learned simulators are expected to capture the physical rules that govern real-world dynamics. However, evaluating whether generated videos actually follow these rules remains challenging. Existing physics-focused video benchmarks have made important progress, but they still face three key challenges, including the coarse evaluation frameworks that hide law-specific failures, response biases and fatigue that undermine the ...

---

### 33. Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge

**Authors:** Wenbo Zhang, Lijinghua Zhang, Liner Xiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10805v1)

**Summary:** Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational...

---

### 34. New AI-Driven Tools for Enhancing Campus Well-being: A Prevention and Intervention Approach

**Authors:** Jinwen Tang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10804v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10804v1)

**Summary:** Campus well-being underpins academic success, yet many universities lack effective methods for monitoring satisfaction and detecting mental health risks. This dissertation addresses these gaps through prevention (improving feedback collection) and intervention (advancing mental health detection), unified under an integrated framework. For prevention, we developed TigerGPT, a personalized survey chatbot leveraging LLMs to engage users in context-aware conversations grounded in conversational desi...

---

### 35. The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies

**Authors:** Gabriel Garcia

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10799v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10799v1)

**Summary:** Corruption studies, the primary tool for evaluating chain-of-thought (CoT) faithfulness, identify which chain positions are "computationally important" by measuring accuracy when steps are replaced with errors. We identify a systematic confound: for chains with explicit terminal answer statements, the dominant format in standard benchmarks, corruption studies detect where the answer text appears, not where computation occurs.   A within-dataset format ablation provides the key evidence: on stand...

---

### 36. Interpretable Machine Learning for Football Performance Analysis: Evidence of Limited Transferability from Elite Leagues to University Competition

**Authors:** Yu-Fang Tsai, Yu-Jen Chen, Kok-Hua Tan, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10796v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10796v1)

**Summary:** Machine learning has become increasingly prevalent in football performance analysis, yet most studies prioritize predictive accuracy while implicitly assuming that learned performance determinants and their interpretations are transferable across competition levels. Whether interpretability remains reliable under domain shift-from elite to university football remains largely unexplored. This study investigates whether performance determinants learned from elite competitions are structurally tran...

---

### 37. Can You Keep a Secret? Involuntary Information Leakage in Language Model Writing

**Authors:** Ari Holtzman, Peter West

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10794v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10794v1)

**Summary:** Language models are deployed in settings that require compartmentalization: system prompts should not be disclosed, chain-of-thought reasoning is hidden from users, and sensitive data passes through shared contexts. We test whether models can keep prompted information out of their writing. We give each model a secret word with instructions not to reveal it, then ask it to write a story. A second model tries to identify the secret from the story in a binary discrimination test. The secret word ne...

---

### 38. PathISE: Learning Informative Path Supervision for Knowledge Graph Question Answering

**Authors:** Shengxiang Gao, Chao Lei, Jey Han Lau, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10791v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10791v1)

**Summary:** Knowledge Graph Question Answering (KGQA) aims to answer user questions by reasoning over Knowledge Graphs (KGs). Recent KGQA methods mainly follow the retrieval-augmented generation paradigm to ground Large Language Models~(LLMs) with structured knowledge from KGs. However, training effective models to retrieve question-relevant evidence from KGs typically requires high-quality intermediate supervision signals, such as question-relevant paths or subgraphs, which are time- and resource-intensive...

---

### 39. ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox

**Authors:** Yuanyang Li, Xue Yang, Longyue Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10787v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10787v1)

**Summary:** Current LLM agents are proficient at calling isolated APIs but struggle with the "last mile" of commercial software automation. In real-world scenarios, tools are not independent; they are atomic, interdependent, and prone to environmental noise. We introduce $\textbf{ComplexMCP}$, a benchmark designed to evaluate agents in these rigorous conditions. Built on the Model Context Protocol (MCP), $\textbf{ComplexMCP}$ provides over 300 meticulously tested tools derived from 7 stateful sandboxes, ran...

---

### 40. TrajPrism: A Multi-Task Benchmark for Language-Grounded Urban Trajectory Understanding

**Authors:** Lihuan Li, Wilson Wongso, Baiyu Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10782v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10782v1)

**Summary:** Urban mobility is naturally expressed both as trajectories in space and as natural-language descriptions of travel intent, constraints, and preferences. However, prior work rarely evaluates these two modalities together on the same real-world trajectories: trajectory modeling often stays geometry-centric, while language-centric mobility benchmarks frequently target route planning and tool use rather than fine-grained, verifiable alignment between text and the underlying route. We introduce TrajP...

---

### 41. Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenizatio

**Authors:** Xuanyu Zhu, Yan Bai, Yang Shi, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10780v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10780v1)

**Summary:** Representation autoencoders that reuse frozen pretrained vision encoders as visual tokenizers have achieved strong reconstruction and generation quality. However, existing methods universally extract features from only the last encoder layer, discarding the rich hierarchical information distributed across intermediate layers. We show that low-level visual details survive in the last layer merely as attenuated residuals after multiple layers of semantic abstraction, and that explicitly fusing mul...

---

### 42. Towards a Large Language-Vision Question Answering Model for MSTAR Automatic Target Recognition

**Authors:** David F. Ramirez, Tim L. Overman, Kristen Jaskie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10772v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10772v1)

**Summary:** Large language-vision models (LLVM), such as OpenAI's ChatGPT and GPT-4, have gained prominence as powerful tools for analyzing text and imagery. The merging of these data domains represents a significant paradigm shift with far-reaching implications for automatic target recognition (ATR). Recent transformer-based LLVM research has shown substantial improvements for geospatial perception tasks. Our study examines the application of LLVM to remote sensing image captioning and visual question-answ...

---

### 43. MPerS: Dynamic MLLM MixExperts Perception-Guided Remote Sensing Scene Segmentation

**Authors:** Ziyi Wang, Xianping Ma, Ziyao Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10769v1)

**Summary:** The multimodal fusion of images and scene captions has been extensively explored and applied in various fields. However, when dealing with complex remote sensing (RS) scenes, existing studies have predominantly concentrated on architectural optimizations for integrating textual semantic information with visual features, while largely neglecting the generation of high-quality RS captions and the investigation of their effectiveness in multimodal semantic fusion.In this context, we propose the Dyn...

---

### 44. Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning

**Authors:** Tao Hu, Da-Wei Zhou

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10765v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10765v1)

**Summary:** Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world deployment often requires continual capability expansion across sequential tasks. In such scenarios, Multimodal Continual Instruction Tuning (MCIT) aims to acquire new capabilities while limiting catastrophic forgetting. Existing methods mainly follow a module-composition paradigm: they maintain task-level prompts or LoRA experts and dynamically route or aggregate a subset of them at in...

---

### 45. Break the Brake, Not the Wheel: Untargeted Jailbreak via Entropy Maximization

**Authors:** Mengqi He, Xinyu Tian, Xin Shen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10764v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10764v1)

**Summary:** Recent studies show that gradient-based universal image jailbreaks on vision-language models (VLMs) exhibit little or no cross-model transferability, casting doubt on the feasibility of transferable multimodal jailbreaks. We revisit this conclusion under a strictly untargeted threat model without enforcing a fixed prefix or response pattern. Our preliminary experiment reveals that refusal behavior concentrates at high-entropy tokens during autoregressive decoding, and non-refusal tokens already ...

---

### 46. MATRA: Modeling the Attack Surface of Agentic AI Systems -- OpenClaw Case Study

**Authors:** Tim Van hamme, Thomas Vissers, Javier Carnerero-Cano, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10763v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10763v1)

**Summary:** LLMs are increasingly deployed as autonomous agents with access to tools, databases, and external services, yet practitioners (across different sectors) lack systematic methods to assess how known threat classes translate into concrete risks within a specific agentic deployment. We present MATRA, a pragmatic threat modeling framework for agentic AI systems that adapts established risk assessment methodology to systematically assess how known LLM threats translate into deployment-specific risks. ...

---

### 47. GridProbe: Posterior-Probing for Adaptive Test-Time Compute in Long-Video VLMs

**Authors:** Mohamed Eltahir, Lama Ayash, Ali Habibullah, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10762v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10762v1)

**Summary:** Long-video understanding in VLMs is bottlenecked by a single monolithic forward pass over thousands of frames at quadratic attention cost. A common mitigation is to first select a small subset of informative frames before the forward pass; common for training-free selectors via auxiliary encoder-space similarities. Such signals are capped by contrastive pretraining, which usually fails on reasoning-heavy queries (negation, cross-frame counting, holistic summarization). We propose GridProbe, an e...

---

### 48. The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents

**Authors:** Xinrun Wang, Chang Yang, He Zhao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10754v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10754v1)

**Summary:** LLM-based foundation agents that perceive, reason, and act across thousands of reasoning steps are rapidly becoming the dominant paradigm for deploying artificial intelligence in open-ended, long-horizon complex tasks. Despite this significance, the field remains overwhelmingly engineering-driven. Engineering practice has converged on useful primitives (tool loops, memory banks, harnesses, reflection steps), yet these are assembled by empirical trial and error rather than from first principles. ...

---

### 49. Provable Sparse Inversion and Token Relabel Enhanced One-shot Federated Learning with ViTs

**Authors:** Li Shen, Xiaolei Hao, Qinglun Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10748v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10748v1)

**Summary:** One-Shot Federated Learning, where a central server learns a global model in a single communication round, has emerged as a promising paradigm. However, under extremely non-IID settings, existing data-free methods often generate low-quality data that suffers from severe semantic misalignment with ground-truth labels. To overcome these issues, we propose a novel Federated Model Inversion and Token Relabel (FedMITR) framework, which trains the global model by fully exploiting all patches of synthe...

---

### 50. Geospatial-Temporal Sensemaking of Remote Sensing Activity Detections with Multimodal Large Language Model

**Authors:** David F. Ramirez, Tim Overman, Kristen Jaskie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10739v1)

**Summary:** We introduce SMART-HC-VQA, a Sentinel-2-based visual question answering dataset derived from the IARPA SMART Heavy Construction dataset, designed for spatiotemporal analysis of human activity. The dataset transforms construction-site annotations, construction-type labels, temporal-phase labels, geographic metadata, and observation relationships into natural language question-answer triplets. This approach redefines the existing dataset as a temporally extended automatic target recognition and vi...

---

## cs.CL

**50 papers**

### 1. ELF: Embedded Language Flows

**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10938v1)

**Summary:** Diffusion and flow-based models have become the de facto approaches for generating continuous data, e.g., in domains such as images and videos. Their success has attracted growing interest in applying them to language modeling. Unlike their image-domain counterparts, today's leading diffusion language models (DLMs) primarily operate over discrete tokens. In this paper, we show that continuous DLMs can be made effective with minimal adaptation to the discrete domain. We propose Embedded Language ...

---

### 2. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices

**Authors:** Chenyang Song, Weilin Zhao, Xu Han, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10933v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10933v1)

**Summary:** While Mixture-of-Experts (MoE) scales model capacity without proportionally increasing computation, its massive total parameter footprint creates significant storage and memory-access bottlenecks, which hinder efficient end-side deployment that simultaneously requires high performance, low computational cost, and small storage overhead. To achieve these properties, we present DECO, a sparse MoE architecture designed to match the performance of dense Transformers under identical total parameter b...

---

### 3. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning

**Authors:** Junhao Shen, Teng Zhang, Xiaoyan Zhao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10923v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10923v1)

**Summary:** Large language model agents increasingly rely on external skills to solve complex tasks, where skills act as modular units that extend their capabilities beyond what parametric memory alone supports. Existing methods assume external skills either accumulate as persistent guidance or internalized into the policy, eventually leading to zero-skill inference. We argue this assumption is overly restrictive, since with limited parametric capacity and uneven marginal contribution across skills, the opt...

---

### 4. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

**Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10912v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10912v1)

**Summary:** Large language and vision-language models increasingly power agents that act on a user's behalf through command-line interface (CLI) harnesses. However, most agent benchmarks still rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks, leaving open whether agents can complete realistic long-horizon work in the runtimes where they are deployed. This work presents WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks span...

---

### 5. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards

**Authors:** Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10899v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10899v1)

**Summary:** Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outputs lack ground-truth answers, their trajectories span many tool-augmented decisions, and standard post-training offers little mechanism for turning past attempts into reusable experience. In this work, we argue that rubrics should serve not merely as final-answer evaluators, but as the shared interf...

---

### 6. Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking

**Authors:** Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10893v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10893v1)

**Summary:** Large vision-language models suffer from visual ungroundedness: they can produce a fluent, confident, and even correct response driven entirely by language priors, with the image contributing nothing to the prediction. Existing confidence estimation methods cannot detect this, as they observe model behavior under normal inference with no mechanism to determine whether a prediction was shaped by the image or by text alone. We introduce BICR (Blind-Image Contrastive Ranking), a model-agnostic conf...

---

### 7. Neural at ArchEHR-QA 2026: One Method Fits All: Unified Prompt Optimization for Clinical QA over EHRs

**Authors:** Abrar Majeedi, Viswanatha Reddy Gajjala, Sai Prasanna Teja Reddy Bogireddy, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10877v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10877v1)

**Summary:** Automated question answering (QA) over electronic health records (EHRs) demands precise evidence retrieval, faithful answer generation, and explicit grounding of answers in clinical notes. In this work, we present Neural1.5, our method for the ArchEHR-QA 2026 shared task at CL4Health@LREC 2026, which comprises four subtasks: question interpretation, evidence identification, answer generation, and evidence alignment. Our approach decouples the task into independent, modular stages and employs DSP...

---

### 8. Compute Where it Counts: Self Optimizing Language Models

**Authors:** Yash Akhauri, Mohamed S. Abdelfattah

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10875v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10875v1)

**Summary:** Efficient LLM inference research has largely focused on reducing the cost of each decoding step (e.g., using quantization, pruning, or sparse attention), typically applying a uniform computation budget to every generated token. In practice, token difficulty varies widely, so static compression can over-compute on easy steps and under-compute on hard ones. We study dynamic budget allocation for autoregressive decoding: learning how much computation to spend per token from within a single model.  ...

---

### 9. DGPO: Beyond Pairwise Preferences with Directional Consistent Groupwise Optimization

**Authors:** Mengyi Deng, Zhiwei Li, Xin Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10863v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10863v1)

**Summary:** Although Large Language Models (LLMs) have made remarkable progress, current preference optimization methods still struggle to align directional consistency while preserving reasoning diversity. To address this limitation, we propose Directional-Groupwise Preference Optimization (DGPO), a lightweight framework that aggregates supervision signals at the group level and explicitly models direction-aware alignment through multi-candidate comparisons. DGPO organizes forward and reverse question-answ...

---

### 10. RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems

**Authors:** Joel Rorseth, Parke Godfrey, Lukasz Golab, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10862v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10862v1)

**Summary:** This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set of rules that subsume all others. We further demonstrate novel applications of these rules for LLM safety, specifically to test the resiliency of safety training and effectiveness of adversarial prompt injections.

---

### 11. Learning More from Less: Exploiting Counterfactuals for Data-Efficient Chart Understanding

**Authors:** Jianzhu Bao, Haozhen Zhang, Kuicai Dong, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10855v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10855v1)

**Summary:** Vision-Language Models (VLMs) have demonstrated remarkable progress in chart understanding, largely driven by supervised fine-tuning (SFT) on increasingly large synthetic datasets. However, scaling SFT data alone is inefficient and overlooks a key property of charts: charts are programmatically generated visual artifacts, where small, code-controlled visual changes can induce drastic shifts in semantics and correct answers. Learning this counterfactual sensitivity requires VLMs to discriminate f...

---

### 12. Grounded Satirical Generation with RAG

**Authors:** Oona Itkonen, Yuxin Su, Linyao Du, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10853v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10853v1)

**Summary:** Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for grounded satire generation that uses Retrieval-Augmented Generation (RAG) over current news to produce satirical dictionary definitions in the Finnish context. We also introduce a new task-specific evaluation framework and annotate 100 generated definitions with six human annotator...

---

### 13. The Generalized Turing Test: A Foundation for Comparing Intelligence

**Authors:** Daniel Mitropolsky, Susan S. Hong, Riccardo Neumarker, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10851v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10851v1)

**Summary:** We introduce the Generalized Turing Test (GTT), a formal framework for comparing the capabilities of arbitrary agents via indistinguishability. For agents A and B, we define the Turing comparator A $\geq$ B to hold if B, acting as a distinguisher, cannot reliably distinguish between interactions with A (instructed to imitate B) and another instance of B. This yields a dataset- and task-agnostic notion of relative intelligence. We study the comparator's structure, including conditions under which...

---

### 14. Rethinking Agentic Search with Pi-Serini: Is Lexical Retrieval Sufficient?

**Authors:** Tz-Huan Hsu, Jheng-Hong Yang, Jimmy Lin

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10848v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10848v1)

**Summary:** Does a lexical retriever suffice as large language models (LLMs) become more capable in an agentic loop? This question naturally arises when building deep research systems. We revisit it by pairing BM25 with frontier LLMs that have better reasoning and tool-use abilities. To support researchers asking the same question, we introduce Pi-Serini, a search agent equipped with three tools for retrieving, browsing, and reading documents. Our results show that, on BrowseComp-Plus, a well-configured lex...

---

### 15. BabelDOC: Better Layout-Preserving PDF Translation via Intermediate Representation

**Authors:** Qi Yang, Xiangyao Ma, Xiao Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10845v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10845v1)

**Summary:** As global cross-lingual communication intensifies, language barriers in visually rich documents such as PDFs remain a practical bottleneck. Existing document translation pipelines face a tension between linguistic processing and layout preservation: text-oriented Computer-Assisted Translation (CAT) systems often discard structural metadata, while document parsers focus on extraction and do not support faithful re-rendering after translation. We introduce BabelDOC, an Intermediate Representation ...

---

### 16. Training-Free Cultural Alignment of Large Language Models via Persona Disagreement

**Authors:** Huynh Trung Kiet, Dao Sy Duy Minh, Tuan Nguyen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10843v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10843v1)

**Summary:** Large language models increasingly mediate decisions that turn on moral judgement, yet a growing body of evidence shows that their implicit preferences are not culturally neutral. Existing cultural alignment methods either require per-country preference data and fine-tuning budgets or assume white-box access to model internals that commercial APIs do not expose. In this work, we focus on this realistic black-box, public-data-only regime and observe that within-country sociodemographic disagreeme...

---

### 17. Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents

**Authors:** Shijue Huang, Hangyu Guo, Chenxin Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10832v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10832v1)

**Summary:** Multimodal deep search requires an agent to solve open-world problems by chaining search, tool use, and visual reasoning over evolving textual and visual context. Two bottlenecks limit current systems. First, existing tool-use harnesses treat images returned by search, browsing, or transformation as transient outputs, so intermediate visual evidence cannot be re-consumed by later tools. Second, training data is usually built by fixed curation recipes that cannot track the target agent's evolving...

---

### 18. SLIM: Sparse Latent Steering for Interpretable and Property-Directed LLM-Based Molecular Editing

**Authors:** Mingxu Zhang, Yuhan Li, Lujundong Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10831v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10831v1)

**Summary:** Large language models possess strong chemical reasoning capabilities, making them effective molecular editors. However, property-relevant information is implicitly entangled across their dense hidden states, providing no explicit handle for property control: a substantial fraction of edits fail to improve or even degrade target properties. To address these issues, we propose SLIM (Sparse Latent Interpretable Molecular editing), a plug-and-play framework that decomposes the editor's hidden states...

---

### 19. Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge

**Authors:** Wenbo Zhang, Lijinghua Zhang, Liner Xiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10805v1)

**Summary:** Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational...

---

### 20. The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies

**Authors:** Gabriel Garcia

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10799v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10799v1)

**Summary:** Corruption studies, the primary tool for evaluating chain-of-thought (CoT) faithfulness, identify which chain positions are "computationally important" by measuring accuracy when steps are replaced with errors. We identify a systematic confound: for chains with explicit terminal answer statements, the dominant format in standard benchmarks, corruption studies detect where the answer text appears, not where computation occurs.   A within-dataset format ablation provides the key evidence: on stand...

---

### 21. Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

**Authors:** Jeonghye Kim, Jiwon Jeon, Dongsheng Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10781v1)

**Summary:** Self-distillation has emerged as a powerful framework for post-training LLMs, where a teacher conditioned on extra information guides a student without it, both from the same model. While this guidance is useful when the student has failed, on successful rollouts, the same mechanism instead overwrites the student's choices and suppresses it's own reasoning. Therefore, we propose reading the original self-distillation signal in reverse: when the student succeeds along a path the teacher would not...

---

### 22. LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments

**Authors:** Chiyu Zhang, Huiqin Yang, Bendong Jiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10779v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10779v1)

**Summary:** The rapid proliferation of LLM-based autonomous agents in real operating system environments introduces a new category of safety risk beyond content safety: behavior jailbreak, where an adversary induces an agent to execute dangerous OS-level operations with irreversible consequences. Existing benchmarks either evaluate safety at the semantic layer alone, missing physical-layer harms, or fail to isolate test cases, letting earlier runs contaminate later ones. We present LITMUS (LLM-agents In-OS ...

---

### 23. Conformity Generates Collective Misalignment in AI Agents Societies

**Authors:** Giordano De Marzo, Alessandro Bellina, Claudio Castellano, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10721v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10721v1)

**Summary:** Artificial intelligence safety research focuses on aligning individual language models with human values, yet deployed AI systems increasingly operate as interacting populations where social influence may override individual alignment. Here we show that populations of individually aligned AI agents can be driven into stable misaligned states through conformity dynamics. Simulating opinion dynamics across nine large language models and one hundred opinion pairs, we find that each agent's behavior...

---

### 24. Why Low-Resource NLP Needs More Than Cross-Lingual Transfer: Lessons Learned from Luxembourgish

**Authors:** Fred Philippy, Siwen Guo, Jacques Klein, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10714v1)

**Summary:** Cross-lingual transfer has become a central paradigm for extending natural language processing (NLP) technologies to low-resource languages. By leveraging supervision from high-resource languages, multilingual language models can achieve strong task performance with little or no labeled target-language data. However, it remains unclear to what extent cross-lingual transfer can substitute for language-specific efforts. In this paper, we synthesize prior research findings and data collection resul...

---

### 25. Step Rejection Fine-Tuning: A Practical Distillation Recipe

**Authors:** Igor Slinko, Ilia Zavidnyi, Egor Bogomolov, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10674v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10674v1)

**Summary:** Rejection Fine-Tuning (RFT) is a standard method for training LLM agents, where unsuccessful trajectories are discarded from the training set. In the context of SWE-bench tasks, this corresponds to filtering out runs where the submitted patch does not pass the tests. However, this approach discards unresolved trajectories, even though they form a large portion of all trajectories for hard tasks and even then may be partially correct. In this work, we propose Step Rejection Fine-Tuning (SRFT) - a...

---

### 26. Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions

**Authors:** Diancheng Kang, Zheyuan Liu, Ningshan Ma, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10664v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10664v1)

**Summary:** Activation steering controls language model behavior by adding directions to internal representations at inference time, but standard residual-stream steering can fail in stateful dialogue. We identify KV-cache contamination as a key failure mode: steered token states are stored and repeatedly reused, turning a local perturbation into cumulative coherence degradation. To address this challenge, we propose Gated Cropped Attention-Delta steering (GCAD), which extracts steering signals from system-...

---

### 27. When Can Digital Personas Reliably Approximate Human Survey Findings?

**Authors:** Mumin Jia, Yilin Chen, Divya Sharma, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10659v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10659v1)

**Summary:** Digital personas powered by Large Language Models (LLMs) are increasingly proposed as substitutes for human survey respondents, yet it remains unclear when they can reliably approximate human survey findings. We answer this question using the LISS panel, constructing personas from respondents' background variables and pre-2023 survey histories, then testing them against the same respondents' held-out post-cutoff answers. Across four persona architectures, three LLMs, and two prediction tasks, we...

---

### 28. A Single-Layer Model Can Do Language Modeling

**Authors:** Zanmin Wang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10643v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10643v1)

**Summary:** Modern language models scale depth by stacking layers, each holding its own state - a per-layer KV cache in transformers, a per-layer matrix in Mamba, Gated DeltaNet (GDN), RWKV, and xLSTM. Biological systems lean heavily on recurrence rather than on stacking. We ask how far that shape can go on language modeling. We propose Grounded Prediction Networks (GPN): one state vector revisited at every step through a single recurrent block - one FFN, one shared matrix memory. At 130M parameters, a 1-la...

---

### 29. Towards Understanding Continual Factual Knowledge Acquisition of Language Models: From Theory to Algorithm

**Authors:** Haoyu Wang, Yifan Shang, Zhongxiang Sun, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10640v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10640v1)

**Summary:** Continual Pre-Training (CPT) is essential for enabling Language Models (LMs) to integrate new knowledge without erasing old. While classical CPT techniques like data replay have become the standard paradigm, the mechanisms underlying how LMs acquire and retain facts over time, termed as continual Factual Knowledge Acquisition (cFKA), remain unclear. In this work, we present a theoretical framework that characterizes the training dynamics of cFKA using a single-layer Transformer, offering a unifi...

---

### 30. Intrinsic Guardrails: How Semantic Geometry of Personality Interacts with Emergent Misalignment in LLMs

**Authors:** Krishak Aneja, Manas Mittal, Anmol Goel, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10633v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10633v1)

**Summary:** Fine-tuning Large Language Models (LLMs) on benign narrow data can sometimes induce broad harmful behaviors, a vulnerability termed emergent misalignment (EM). While prior work links these failures to specific directions in the activation space, their relationship to the model's broader persona remains unexplored. We map the latent personality space of LLMs through established psychometric profiles like the Big Five, Dark Triad, and LLM-specific behaviors (e.g. evil, sycophancy), and show that t...

---

### 31. Interpretable Coreference Resolution Evaluation Using Explicit Semantics

**Authors:** Bruno Gatti, Giuliano Martinelli, Roberto Navigli

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10627v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10627v1)

**Summary:** Coreference resolution is typically evaluated using aggregate statistical metrics such as CoNLL-F1, which measure structural overlap between predicted and gold clusters. While widely used, these metrics offer limited diagnostic insights, penalizing errors without revealing whether a system struggles with specific semantic categories, such as people, locations, or events, and making it difficult to interpret model capabilities or derive actionable improvements. We address this gap by introducing ...

---

### 32. MulTaBench: Benchmarking Multimodal Tabular Learning with Text and Image

**Authors:** Alan Arazi, Eilam Shapira, Shoham Grunblat, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10616v1)

**Summary:** Tabular Foundation Models have recently established the state of the art in supervised tabular learning, by leveraging pretraining to learn generalizable representations of numerical and categorical structured data. However, they lack native support for unstructured modalities such as text and image, and rely on frozen, pretrained embeddings to process them. On established Multimodal Tabular Learning benchmarks, we show that tuning the embeddings to the task improves performance. Existing benchm...

---

### 33. Responsible Benchmarking of Fairness for Automatic Speech Recognition

**Authors:** Felix Herron, Ange Richard, François Portet, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10615v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10615v1)

**Summary:** Many studies have shown automatic speech processing (ASR) systems have unequal performance across speakergroups (SG's). However, the manner in which such studies arrive at this conclusion is inconsistent. To pave the wayfor more reliable results in future studies, we lay out best practices for benchmarking ASR fairness based on literaturefrom machine learning fairness, social sciences, and speech science. We first describe the importance of preciselythe fairness hypothesis being interrogated, an...

---

### 34. Measuring Embedding Sensitivity to Authorial Style in French: Comparing Literary Texts with Language Model Rewritings

**Authors:** Benjamin Icard, Lila Sainero, Alice Breton, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10606v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10606v1)

**Summary:** Large language models (LLMs) can convincingly imitate human writing styles, yet it remains unclear how much stylistic information is encoded in embeddings from any language model and retained after LLM rewriting. We investigate these questions in French, using a controlled literary dataset to quantify the effect of stylistic variation via changes in embedding dispersion. We observe that embeddings reliably capture authorial stylistic features and that these signals persist after rewriting, while...

---

### 35. Where do aspectual variants of light verb constructions belong?

**Authors:** Aggeliki Fotopoulou, Eric Laporte, Takuya Nakamura

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10605v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10605v1)

**Summary:** Expressions with an aspectual variant of a light verb, e.g. 'take on debt' vs. 'have debt', are frequent in texts but often difficult to classify between verbal idioms, light verb constructions or compositional phrases. We investigate the properties of such expressions with a disputed membership and propose a selection of features that determine more satisfactory boundaries between the three categories in this zone, assigning the expressions to one of them.

---

### 36. LLARS: Enabling Domain Expert & Developer Collaboration for LLM Prompting, Generation and Evaluation

**Authors:** Philipp Steigerwald, Mara Stieler, Jennifer Burghardt, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10593v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10593v1)

**Summary:** We demonstrate LLARS (LLM Assisted Research System), an open-source platform that bridges the gap between domain experts and developers for building LLM-based systems. It integrates three tightly connected modules into an end-to-end pipeline: Collaborative Prompt Engineering for real-time co-authoring with version control and instant LLM testing, Batch Generation for configurable output production across user-selected prompts $\times$ models $\times$ data with cost control, and Hybrid Evaluation...

---

### 37. VISTA: A Generative Egocentric Video Framework for Daily Assistance

**Authors:** Yu-Hsiang Liu, Yu-Chien Tang, An-Zi Yen

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10579v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10579v1)

**Summary:** Training AI agents to proactively assist humans in daily activities, from routine household tasks to urgent safety situations, requires large-scale visual data. However, capturing such scenarios in the real world is often difficult, costly, or unsafe, and physics-based simulators lack the visual fidelity needed to transfer learned behaviors to real settings. Therefore, we introduce VISTA, a video synthesis system that produces high-fidelity egocentric videos as training and evaluation data for A...

---

### 38. ThreatCore: A Benchmark for Explicit and Implicit Threat Detection

**Authors:** Davide Bruni, Carlo Bardazzi, Maurizio Tesconi

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10563v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10563v1)

**Summary:** Threat detection in Natural Language Processing lacks consistent definitions and standardized benchmarks, and is often conflated with broader phenomena such as toxicity, hate speech, or offensive language. In this work, we introduce ThreatCore, a public available benchmark dataset for fine-grained threat detection that distinguishes between explicit threats, implicit threats, and non-threats. The dataset is constructed by aggregating multiple publicly available resources and systematically re-an...

---

### 39. ICT-NLP at SemEval-2026 Task 3: Less Is More -- Multilingual Encoder with Joint Training and Adaptive Ensemble for Dimensional Aspect Sentiment Regression

**Authors:** Liyuan Huang, Jiawei He, Wutao Shen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10560v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10560v1)

**Summary:** This paper describes our system to SemEval-2026 Task 3 Track A Subtask 1 on Dimensional Aspect Sentiment Regression (DimASR). We propose a lightweight and resource-efficient system built entirely on multilingual pre-trained encoders, without relying on LLMs or external corpora. We adopt joint multilingual and multi-domain training to facilitate cross-lingual transfer and alleviate data sparsity, introduce a bounded regression transformation that improves training stability while constraining pre...

---

### 40. Multi-domain Multi-modal Document Classification Benchmark with a Multi-level Taxonomy

**Authors:** Denghao Ma, Qing Liu, Zulong Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10550v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10550v1)

**Summary:** Document classification forms the backbone of modern enterprise content management, yet existing benchmarks remain trapped in oversimplified paradigms -- single domain settings with flat label structures -- that bear little resemblance to the hierarchical, multi-modal, and cross-domain nature of real-world business documents. This gap not only misrepresents practical complexity but also stifles progress toward industrially viable document intelligence. To bridge this gap, we construct the first ...

---

### 41. Where Does Long-Context Supervision Actually Go? Effective-Context Exposure Balancing

**Authors:** Jinchang Zhu, Jindong Li, Chengyu Zou, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10544v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10544v1)

**Summary:** Long-context adaptation is often viewed as window scaling, but this misses a token-level supervision mismatch: in packed training with document masking, each target token's effective context remains short. We introduce EXACT, a supervision-allocation objective that assigns extra weight to long effective-context targets by inverse frequency within the long tail. Across seven Qwen/LLaMA CPT configurations, EXACT improves all 28 trained/extrapolated NoLiMa and RULER comparisons. On Qwen2.5-0.5B, No...

---

### 42. Mela: Test-Time Memory Consolidation based on Transformation Hypothesis

**Authors:** Lungchuan Chen

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10537v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10537v1)

**Summary:** Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human brain, yet it remains largely unexplored as a design principle for modern sequence models. In this work, we leverage established neuroscientific theories of memory consolidation and cross-frequency coupling to propose the Hierarchical Memory Module (HMM), a neural memory architecture composed of two functionally distinct sub...

---

### 43. Collective Alignment in LLM Multi-Agent Systems: Disentangling Bias from Cooperation via Statistical Physics

**Authors:** Cristiano De Nobili

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10528v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10528v1)

**Summary:** We investigate the emergent collective dynamics of LLM-based multi-agent systems on a 2D square lattice and present a model-agnostic statistical-physics method to disentangle social conformity from intrinsic bias, compute critical exponents, and probe the collective behavior and possible phase transitions of multi-agent systems. In our framework, each node of an $L\!\times\!L$ lattice hosts an identical LLM agent holding a binary state ($+1$/$-1$, mapped to yes/no) and updating it by querying th...

---

### 44. Infinite Mask Diffusion for Few-Step Distillation

**Authors:** Jaehoon Yoo, Wonjung Kim, Chanhyuk Lee, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10518v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10518v1)

**Summary:** Masked Diffusion Models (MDMs) have emerged as a promising alternative to autoregressive models in language modeling, offering the advantages of parallel decoding and bidirectional context processing within a simple yet effective framework. Specifically, their explicit distinction between masked tokens and data underlies their simple framework and effective conditional generation. However, MDMs typically require many sampling iterations due to factorization errors stemming from simultaneous toke...

---

### 45. Learning Less Is More: Premature Upper-Layer Attention Specialization Hurts Language Model Pretraining

**Authors:** Jinchang Zhu, Jindong Li, Yuwen Hao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10504v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10504v1)

**Summary:** A causal-decoder block is hierarchical: lower layers build the residual basis that upper layers attend over. We identify a failure mode in GPT pretraining: upper layers commit to sharp attention patterns before lower-layer features stabilize. We call this premature upper-layer attention specialization. Temporarily slowing only upper-layer Q/K projections during early training improves final perplexity and downstream accuracy without altering other parameters; it prevents upper attention from col...

---

### 46. DeepRefine: Agent-Compiled Knowledge Refinement via Reinforcement Learning

**Authors:** Haoyu Huang, Jiaxin Bai, Shujie Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10488v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10488v1)

**Summary:** Agent-compiled knowledge bases provide persistent external knowledge for large language model (LLM) agents in open-ended, knowledge-intensive downstream tasks. Yet their quality is systematically limited by \emph{incompleteness}, \emph{incorrectness}, and \emph{redundancy}, manifested as missing evidence or cross-document links, low-confidence or imprecise claims, and ambiguous or coreference resolution issues. Such defects compound under iterative use, degrading retrieval fidelity and downstrea...

---

### 47. Coherency through formalisations of Structured Natural Language, A case study on FRETish

**Authors:** Joost J. Joosten, Marina López Chamosa, Sofía Santiago Fernández

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10462v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10462v1)

**Summary:** Formalisation is the process of writing system requirements in a formal language. These requirements mostly originate in Natural Language. In the field of Formal Methods, formalisation is often identified as one of the most delicate and complicated steps in the verification process. Not seldomly, formalisation tools and environments choose various levels of requirement descriptions: Natural Language, Technical Language, Diagram Representations and Formal Language, to mention a few. In the litera...

---

### 48. SlimSpec: Low-Rank Draft LM-Head for Accelerated Speculative Decoding

**Authors:** Anton Plaksin, Sergei Krutikov, Sergei Skvortsov, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10453v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10453v1)

**Summary:** Speculative decoding speeds up autoregressive generation in Large Language Models (LLMs) through a two-step procedure, where a lightweight draft model proposes tokens which the target model then verifies in a single forward pass. Although the drafter network is small in modern architectures, its LM-head still performs projection to a large vocabulary, becoming one of the major computational bottlenecks. In prior work this issue has been predominantly addressed via static or dynamic vocabulary tr...

---

### 49. StereoTales: A Multilingual Framework for Open-Ended Stereotype Discovery in LLMs

**Authors:** Pierre Le Jeune, Étienne Duchesne, Weixuan Xiao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10442v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10442v1)

**Summary:** Multilingual studies of social bias in open-ended LLM generation remain limited: most existing benchmarks are English-centric, template-based, or restricted to recognizing pre-specified stereotypes. We introduce StereoTales, a multilingual dataset and evaluation pipeline for systematically studying the emergence of social bias in open-ended LLM generation. The dataset covers 10 languages and 79 socio-demographic attributes, and comprises over 650k stories generated by 23 recent LLMs, each annota...

---

### 50. Can Language Models Analyze Data? Evaluating Large Language Models for Question Answering over Datasets

**Authors:** Andreas Xenofontos, Pavlos Fafalios

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10419v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10419v1)

**Summary:** This paper investigates the effectiveness of large language models (LLMs) in answering questions over datasets. We examine their performance in two scenarios: (a) directly answering questions given a dataset file as input, and (b) generating SQL queries to answer questions given the schema of a relational database. We also evaluate the impact of different prompting strategies on model performance. The study includes both state-of-the-art LLMs and smaller language models that require fewer resour...

---

## cs.CV

**50 papers**

### 1. Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping

**Authors:** Haoyuan Sun, Jing Wang, Yuxin Song, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10937v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10937v1)

**Summary:** Recently, post-training methods based on reinforcement learning, with a particular focus on Group Relative Policy Optimization (GRPO), have emerged as the robust paradigm for further advancement of text-to-image (T2I) models. However, these methods are often prone to reward hacking, wherein models exploit biases in imperfect reward functions rather than yielding genuine performance gains. In this work, we identify that normalization could lead to miscalibration and directly removing the prompt-l...

---

### 2. Personal Visual Context Learning in Large Multimodal Models

**Authors:** Zihui Xue, Ami Baid, Sangho Kim, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10936v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10936v1)

**Summary:** As wearable devices like smart glasses integrate Large Multimodal Models (LMMs) into the continuous first-person visual streams of individual users, the evolution of these models into true personal assistants hinges on visual personalization: the ability to reason over visual information unique to the wearer. We formalize this capability as Personal Visual Context Learning (Personal VCL), the prompt-time capability of using user-specific visual context to resolve personalized queries. To systema...

---

### 3. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10934v1)

**Summary:** Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are eff...

---

### 4. Pixal3D: Pixel-Aligned 3D Generation from Images

**Authors:** Dong-Yang Li, Wang Zhao, Yuxin Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10922v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10922v1)

**Summary:** Recent advances in 3D generative models have rapidly improved image-to-3D synthesis quality, enabling higher-resolution geometry and more realistic appearance. Yet fidelity, which measures pixel-level faithfulness of the generated 3D asset to the input image, still remains a central bottleneck. We argue this stems from an implicit 2D-3D correspondence issue: most 3D-native generators synthesize shape in canonical space and inject image cues via attention, leaving pixel-to-3D associations ambiguo...

---

### 5. Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition

**Authors:** Md. Sultan Al Rayhan, Maheen Islam

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10916v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10916v1)

**Summary:** Recognition of handwritten Bangla compound characters remains a challenging problem due to complex character structures, large intra-class variation, and limited availability of high-quality annotated data. Existing Bangla handwritten character recognition systems often struggle to generalize across diverse writing styles, particularly for compound characters containing intricate ligatures and diacritical variations. In this work, we propose a confidence-guided diffusion augmentation framework f...

---

### 6. CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models

**Authors:** Wenxuan Song, Han Zhao, Fuhao Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10903v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10903v1)

**Summary:** This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhan...

---

### 7. Counterfactual Stress Testing for Image Classification Models

**Authors:** Moritz Stammel, Fabio De Sousa Ribeiro, Raghav Mehta, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10894v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10894v1)

**Summary:** Deep learning models in medical imaging often fail when deployed in new clinical environments due to distribution shifts in demographics, scanner hardware, or acquisition protocols. A central challenge is underspecification, where models with similar validation performance exhibit divergent real-world failure modes. Although stress testing has emerged as a tool to assess this, current methods typically rely on simple, uninformed perturbations (e.g., brightness or contrast changes), which fail to...

---

### 8. Count Anything at Any Granularity

**Authors:** Chang Liu, Haoning Wu, Weidi Xie

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10887v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10887v1)

**Summary:** Open-world object counting remains brittle: despite rapid advances in vision-language models (VLMs), reliably counting the objects a user intends is far from solved. We argue that a central reason is that counting granularity is left implicit; users may refer to a specific identity, an attribute, an instance type, a category, or an abstract concept, yet most methods treat "what to count" as a single, category-level matching problem. In this work, we redefine open-world counting as multi-grained ...

---

### 9. Geometry-aware Prototype Learning for Cross-domain Few-shot Medical Image Segmentation

**Authors:** Feifan Song, Yuntian Bo, Haofeng Zhang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10885v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10885v1)

**Summary:** Cross-domain few-shot medical image segmentation (CD-FSMIS) requires a model to generalise simultaneously to novel anatomical categories and unseen imaging domains from only a handful of annotated examples. Existing prototypical approaches inevitably entangle anatomical structure with domain-specific appearance variations, and thus lack a stable reference for reliable matching under domain shift. We observe that the geometric structure of human anatomy constitutes a reliable, domain-transferable...

---

### 10. CADBench: A Multimodal Benchmark for AI-Assisted CAD Program Generation

**Authors:** Anna C. Doris, Jacob Thomas Sony, Ghadi Nehme, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10873v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10873v1)

**Summary:** Recovering editable CAD programs from images or 3D observations is central to AI-assisted design, but progress is difficult to measure because existing evaluations are fragmented across datasets, modalities, and metrics. We introduce CADBench, a unified benchmark for multimodal CAD program generation. CADBench contains 18,000 evaluation samples spanning six benchmark families derived from DeepCAD, Fusion 360, ABC, MCB, and Objaverse; five input modalities including clean meshes, noisy meshes, si...

---

### 11. BEACON: A Multimodal Dataset for Learning Behavioral Fingerprints from Gameplay Data

**Authors:** Ishpuneet Singh, Gursmeep Kaur, Uday Pratap Singh Atwal, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10867v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10867v1)

**Summary:** Continuous authentication in high-stakes digital environments requires datasets with fine-grained behavioral signals under realistic cognitive and motor demands. But current benchmarks are often limited by small scale, unimodal sensing or lack of synchronised environmental context. To address this gap, this paper introduces BEACON ( Behavioral Engine for Authentication \& Continuous Monitoring), a large-scale multimodal dataset that captures diverse skill tiers in competitive \textit{Valorant} g...

---

### 12. BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD

**Authors:** Haozhe Zhang, Kaichen Liu, Miaomiao Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10865v1)

**Summary:** Industrial Computer-Aided Design (CAD) code generation requires models to produce executable parametric programs from visual or textual inputs. Beyond recognizing the outer shape of a part, this task involves understanding its 3D structure, inferring engineering parameters, and choosing CAD operations that reflect how the part would be designed and manufactured. Despite the promise of Multimodal large language models (MLLMs) for this task, they are rarely evaluated on whether these capabilities ...

---

### 13. Masked Generative Transformer Is What You Need for Image Editing

**Authors:** Wei Chow, Linfeng Li, Xian Sun, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10859v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10859v1)

**Summary:** Diffusion models dominate image editing, yet their global denoising mechanism entangles edited regions with surrounding context, causing modifications to propagate into areas that should remain intact. We propose a fundamentally different approach by leveraging Masked Generative Transformers (MGTs), whose localized token-prediction paradigm naturally confines changes to intended regions. We present EditMGT, an MGT-based editing framework that is the first of its kind. Our approach employs multi-...

---

### 14. Is Your Driving World Model an All-Around Player?

**Authors:** Lingdong Kong, Ao Liang, Tianyi Yan, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10858v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10858v1)

**Summary:** Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally. Some generate photorealistic textures but violate basic physics; others maintain geometric consistency but fail when subjected to closed-loop planning. This disconnect exposes a critical gap: the field evaluates how real generated worlds appear, but rarely whether they behave realistically. We introduce WorldLens, a unified benchmark that measures world-model fidelity across th...

---

### 15. Verification Mirage: Mapping the Reliability Boundary of Self-Verification in Medical VQA

**Authors:** Ruinan Jin, Beidi Zhao, Myeongkyun Kang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10850v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10850v1)

**Summary:** Self-verification, re-invoking the same vision language model (VLM) in a fresh context to check its own generated answer, is increasingly used as a default safety layer for medical visual question answering (VQA). We argue that this practice is fundamentally unreliable. We introduce [METHOD NAME], a diagnostic framework for mapping the reliability boundary of medical VLM self-verification by decomposing verifier behavior into discrimination capability and agreement bias. Because the verifier and...

---

### 16. BabelDOC: Better Layout-Preserving PDF Translation via Intermediate Representation

**Authors:** Qi Yang, Xiangyao Ma, Xiao Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10845v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10845v1)

**Summary:** As global cross-lingual communication intensifies, language barriers in visually rich documents such as PDFs remain a practical bottleneck. Existing document translation pipelines face a tension between linguistic processing and layout preservation: text-oriented Computer-Assisted Translation (CAT) systems often discard structural metadata, while document parsers focus on extraction and do not support faithful re-rendering after translation. We introduce BabelDOC, an Intermediate Representation ...

---

### 17. Transcoda: End-to-End Zero-Shot Optical Music Recognition via Data-Centric Synthetic Training

**Authors:** Daniel Dratschuk, Paul Swoboda

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10835v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10835v1)

**Summary:** Optical Music Recognition (OMR), the task of transcribing sheet music into a structured textual representation, is currently bottlenecked by a lack of large-scale, annotated datasets of real scans. This forces models to rely on either few-shot transfer or synthetic training pipelines that remain overly simplistic. A secondary challenge is encoding non-uniqueness: in the popular Humdrum **kern format for transcribing music, multiple different text encodings can render into the same visual sheet m...

---

### 18. MMVIAD: Multi-view Multi-task Video Understanding for Industrial Anomaly Detection

**Authors:** Xiran Zhao, Jing Jin, Yan Bai, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10833v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10833v1)

**Summary:** Industrial anomaly detection is critical for manufacturing quality control, yet existing datasets mainly focus on static images or sparse views, which do not fully reflect continuous inspection processes in real industrial scenarios. We introduce MMVIAD (Multi-view Multi-task Video Industrial Anomaly Detection), to the best of our knowledge the first continuous multi-view video dataset for industrial anomaly detection and understanding, together with a benchmark for multi-task evaluation. MMVIAD...

---

### 19. Predicting 3D structure by latent posterior sampling

**Authors:** Azmi Haider, Dan Rosenbaum

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10830v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10830v1)

**Summary:** The remarkable achievements of both generative models of 2D images and neural field representations for 3D scenes present a compelling opportunity to integrate the strengths of both approaches. In this work, we propose a methodology that combines a NeRF-based representation of 3D scenes with probabilistic modeling and reasoning using diffusion models. We view 3D reconstruction as a perception problem with inherent uncertainty that can thereby benefit from probabilistic inference methods. The cor...

---

### 20. ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models

**Authors:** Zuojin Tang, Haoyun Liu, Xinyuan Chang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10819v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10819v1)

**Summary:** Vision-language-action (VLA) models remain constrained by the scarcity of action-labeled robot data, whereas action-free videos provide abundant evidence of how the physical world changes. Latent action models offer a promising way to extract such priors from videos, but reconstruction-trained latent codes are not necessarily suitable for policy generation: they may predict future observations while lacking the structure needed to be reused or generated coherently with robot actions. We introduc...

---

### 21. PhyGround: Benchmarking Physical Reasoning in Generative World Models

**Authors:** Juyi Lin, Arash Akbari, Yumei He, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10806v1)

**Summary:** Generative world models are increasingly used for video generation, where learned simulators are expected to capture the physical rules that govern real-world dynamics. However, evaluating whether generated videos actually follow these rules remains challenging. Existing physics-focused video benchmarks have made important progress, but they still face three key challenges, including the coarse evaluation frameworks that hide law-specific failures, response biases and fatigue that undermine the ...

---

### 22. Rapid Forest Fuel Load Estimation via Virtual Remote Sensing and Metric-Scale Feed-Forward 3D Reconstruction

**Authors:** Quanyun Wu, Kyle Gao, Wentao Sun, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10789v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10789v1)

**Summary:** Accurate quantification of forest coverage and combustible biomass (fuel load) is critical for wildfire risk assessment and ecosystem management. However, traditional methods relying on airborne LiDAR or field surveys are cost-prohibitive and time-intensive, while satellite imagery often lacks the vertical resolution required for canopy volume analysis. This paper proposes a novel, automated pipeline for rapid forest inventory using virtual remote sensing data derived from Google Earth Studio (G...

---

### 23. Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenizatio

**Authors:** Xuanyu Zhu, Yan Bai, Yang Shi, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10780v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10780v1)

**Summary:** Representation autoencoders that reuse frozen pretrained vision encoders as visual tokenizers have achieved strong reconstruction and generation quality. However, existing methods universally extract features from only the last encoder layer, discarding the rich hierarchical information distributed across intermediate layers. We show that low-level visual details survive in the last layer merely as attenuated residuals after multiple layers of semantic abstraction, and that explicitly fusing mul...

---

### 24. Towards a Large Language-Vision Question Answering Model for MSTAR Automatic Target Recognition

**Authors:** David F. Ramirez, Tim L. Overman, Kristen Jaskie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10772v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10772v1)

**Summary:** Large language-vision models (LLVM), such as OpenAI's ChatGPT and GPT-4, have gained prominence as powerful tools for analyzing text and imagery. The merging of these data domains represents a significant paradigm shift with far-reaching implications for automatic target recognition (ATR). Recent transformer-based LLVM research has shown substantial improvements for geospatial perception tasks. Our study examines the application of LLVM to remote sensing image captioning and visual question-answ...

---

### 25. MPerS: Dynamic MLLM MixExperts Perception-Guided Remote Sensing Scene Segmentation

**Authors:** Ziyi Wang, Xianping Ma, Ziyao Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10769v1)

**Summary:** The multimodal fusion of images and scene captions has been extensively explored and applied in various fields. However, when dealing with complex remote sensing (RS) scenes, existing studies have predominantly concentrated on architectural optimizations for integrating textual semantic information with visual features, while largely neglecting the generation of high-quality RS captions and the investigation of their effectiveness in multimodal semantic fusion.In this context, we propose the Dyn...

---

### 26. Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning

**Authors:** Tao Hu, Da-Wei Zhou

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10765v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10765v1)

**Summary:** Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world deployment often requires continual capability expansion across sequential tasks. In such scenarios, Multimodal Continual Instruction Tuning (MCIT) aims to acquire new capabilities while limiting catastrophic forgetting. Existing methods mainly follow a module-composition paradigm: they maintain task-level prompts or LoRA experts and dynamically route or aggregate a subset of them at in...

---

### 27. Break the Brake, Not the Wheel: Untargeted Jailbreak via Entropy Maximization

**Authors:** Mengqi He, Xinyu Tian, Xin Shen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10764v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10764v1)

**Summary:** Recent studies show that gradient-based universal image jailbreaks on vision-language models (VLMs) exhibit little or no cross-model transferability, casting doubt on the feasibility of transferable multimodal jailbreaks. We revisit this conclusion under a strictly untargeted threat model without enforcing a fixed prefix or response pattern. Our preliminary experiment reveals that refusal behavior concentrates at high-entropy tokens during autoregressive decoding, and non-refusal tokens already ...

---

### 28. GridProbe: Posterior-Probing for Adaptive Test-Time Compute in Long-Video VLMs

**Authors:** Mohamed Eltahir, Lama Ayash, Ali Habibullah, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10762v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10762v1)

**Summary:** Long-video understanding in VLMs is bottlenecked by a single monolithic forward pass over thousands of frames at quadratic attention cost. A common mitigation is to first select a small subset of informative frames before the forward pass; common for training-free selectors via auxiliary encoder-space similarities. Such signals are capped by contrastive pretraining, which usually fails on reasoning-heavy queries (negation, cross-frame counting, holistic summarization). We propose GridProbe, an e...

---

### 29. RadThinking: A Dataset for Longitudinal Clinical Reasoning in Radiology

**Authors:** Wenxuan Li, Pedro R. A. S. Bassi, Xinze Zhou, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10761v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10761v1)

**Summary:** Cancer screening is a reasoning task. A radiologist observes findings, compares them to prior scans, integrates clinical context, and reaches a diagnostic conclusion confirmed by pathology. We present RadThinking, a Visual Question Answering (VQA) dataset that makes this reasoning explicit and trainable. RadThinking releases VQA pairs at three difficulty tiers. Foundation VQAs are atomic perception questions. Single-step reasoning VQAs apply one clinical rule. Compositional VQAs require multi-st...

---

### 30. Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models

**Authors:** Andreas Bergmeister, Stefanie Jegelka, Nikolas Nüsken, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10759v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10759v1)

**Summary:** Diffusion and flow-matching models scale because pretraining is supervised regression: a clean sample is noised analytically, and a model regresses against a closed-form target. RL post-training aligns the model with a reward. In image generation, this makes samples compose objects correctly, render text legibly, and match human preferences. Existing methods rely on costly SDE rollouts, reward gradients, or surrogate losses, sacrificing pretraining's regression structure. We show that the struct...

---

### 31. TINS: Test-time ID-prototype-separated Negative Semantics Learning for OOD Detection

**Authors:** Yifeng Yang, Jubo Feng, Jing Xu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10756v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10756v1)

**Summary:** Vision-language models enable OOD detection by comparing image alignment with ID labels and negative semantics. Existing negative-label-based methods mainly rely on static negative labels constructed before inference, limiting their ability to cover diverse and evolving OOD concepts. Although test-time expansion provides a natural solution, naively learning negative semantics from potential OOD samples may introduce hard ID contamination. To address this issue, we propose a \textbf{T}est-time \t...

---

### 32. C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving

**Authors:** Kefei Tian, Yuansheng Lian, Kai Yang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10744v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10744v1)

**Summary:** Safety-critical planning in complex environments, particularly at urban intersections, remains a fundamental challenge for autonomous driving. Existing methods, whether rule-based or data-driven, frequently struggle to capture complex scene semantics, infer potential risks, and make reliable decisions in rare, high-risk situations. While vision-language models (VLMs) offer promising approaches for safe decision-making in these environments, most current approaches lack reflective and causal reas...

---

### 33. Geospatial-Temporal Sensemaking of Remote Sensing Activity Detections with Multimodal Large Language Model

**Authors:** David F. Ramirez, Tim Overman, Kristen Jaskie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10739v1)

**Summary:** We introduce SMART-HC-VQA, a Sentinel-2-based visual question answering dataset derived from the IARPA SMART Heavy Construction dataset, designed for spatiotemporal analysis of human activity. The dataset transforms construction-site annotations, construction-type labels, temporal-phase labels, geographic metadata, and observation relationships into natural language question-answer triplets. This approach redefines the existing dataset as a temporally extended automatic target recognition and vi...

---

### 34. iPay: Integrated Payment Action Recognition via Multimodal Networks and Adaptive Spatial Prior Learning

**Authors:** Kaicong Huang, Weiheng Oh, Thomas Guggisberg, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10732v1)

**Summary:** Automated transit payment analysis is vital for scalable fare auditing and passenger analytics, yet practice still relies on limited manual inspection. Prior vision- and skeleton-based methods remain brittle under noisy onboard surveillance and often depend on poorly generalizable handcrafted features. Building on the success of graph convolutional networks in human action recognition, we observe that skeleton features excel at modeling global spatiotemporal dependencies but tend to underemphasi...

---

### 35. Qwen-Image-2.0 Technical Report

**Authors:** Bing Zhao, Chenfei Wu, Deqing Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10730v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10730v1)

**Summary:** We present Qwen-Image-2.0, an omni-capable image generation foundation model that unifies high-fidelity generation and precise image editing within a single framework. Despite recent progress, existing models still struggle with ultra-long text rendering, multilingual typography, high-resolution photorealism, robust instruction following, and efficient deployment, especially in text-rich and compositionally complex scenarios. Qwen-Image-2.0 addresses these challenges by coupling Qwen3-VL as the ...

---

### 36. AllocMV: Optimal Resource Allocation for Music Video Generation via Structured Persistent State

**Authors:** Huimin Wang, Leilei Ouyang, Chang Xia, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10723v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10723v1)

**Summary:** Generating long-horizon music videos (MVs) is frequently constrained by prohibitive computational costs and difficulty maintaining cross-shot consistency. We propose AllocMV, a hierarchical framework formulating music video synthesis as a Multiple-Choice Knapsack Problem (MCKP). AllocMV represents the video's persistent state as a compact, structured object comprising character entities, scene priors, and sharing graphs, produced by a global planner prior to realization. By estimating segment sa...

---

### 37. Heteroscedastic Diffusion for Multi-Agent Trajectory Modeling

**Authors:** Guillem Capellera, Antonio Rubio, Luis Ferraz, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10717v1)

**Summary:** Multi-agent trajectory modeling traditionally focuses on forecasting, often neglecting more general tasks like trajectory completion, which is essential for real-world applications such as correcting tracking data. Existing methods also generally predict agents' states without offering any state-wise measure of heteroscedastic uncertainty. Moreover, popular multi-modal sampling methods lack error probability estimates for each generated scene under the same prior observations, which makes it dif...

---

### 38. UAV-Assisted Scan-to-Simulation for Landslides Using Physics-Informed Gaussian Splatting

**Authors:** Zhenyu Liang, Jack C. P. Cheng

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10715v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10715v1)

**Summary:** Landslide monitoring and simulation play an important role in urban safety assessment and disaster prevention. Existing landslide simulation pipelines typically rely on digital elevation model and mesh-based representations, which are suitable for geometric analysis, but often lack visual realism. This limitation reduces their effectiveness in interactive applications, hazard communication, and public education. In this paper, we propose a UAV-based scan-to-simulation framework that bridges phot...

---

### 39. TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering

**Authors:** Zhenyu Liang, Xiao Zhang, Tianchao Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10705v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10705v1)

**Summary:** Transmissive scenes are ubiquitous in daily life, yet reconstructing and rendering them remains highly challenging due to the inherent entanglement between near-field reflections from the surrounding environment on the transmissive surface, and the transmitted content of the scene behind it. This coupling gives rise to dual surface geometries and dual radiance components within each observation, posing ambiguities for standard methods. We present TransmissiveGS, a novel framework for disentangle...

---

### 40. Not Blind but Silenced: Rebalancing Vision and Language via Adversarial Counter-Commonsense Equilibrium

**Authors:** Qingxin Xiao, Peilin Zhao, Yangyang Zhao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10676v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10676v1)

**Summary:** During MLLM decoding, attention often abnormally concentrates on irrelevant image tokens. While existing research dismisses this as invalid noise and forcibly redirects attention to compel focusing on key image information, we argue these tokens are critical carriers of visual and narrative logic, and such coercive corrections exacerbate visual-language imbalance. Adopting a "decoding-as-game" perspective, we reveal that hallucinations stem from an equilibrium imbalance between linguistic priors...

---

### 41. Neuromorphic Monocular Depth Estimation with Uncertainty Modeling

**Authors:** Viktor Bergkvist, Felix Rydell, Per-Erik Forssén, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10675v1)

**Summary:** Event cameras offer distinct advantages over conventional frame-based sensors, including microsecond-level temporal resolution, high dynamic range, and low bandwidth. In this paper, we predict per-pixel depth distributions from monocular event streams using deep neural networks. We estimate uncertainty using Gaussian, log-normal, and evidential learning frameworks. We compare six event representations: spatio-temporal voxel grids with 1, 5, 10, and 20 temporal bins, the Compact Spatio-Temporal R...

---

### 42. bViT: Investigating Single-Block Recurrence in Vision Transformers for Image Recognition

**Authors:** Michal Byra, Pawel Olszowiec, Grzegorz Stefanski, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10661v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10661v1)

**Summary:** Vision Transformers (ViTs) are built by stacking independently parameterized blocks, but it remains unclear how much of this depth requires layer specific transformations and how much can be realized through recurrent computation. We study this question with bViT, a single-block recurrent ViT in which one transformer block is applied repeatedly to process an image. This architecture preserves the iterative structure of a deep ViT while removing layer specific block parameterization, providing a ...

---

### 43. GenMed: A Pairwise Generative Reformulation of Medical Diagnostic Tasks

**Authors:** Hantao Zhang, Weidong Guo, Yuhe Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10645v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10645v1)

**Summary:** Data-driven medical AI is traditionally formulated as a discriminative mapping from input $X$ to output $Y$ via a learned function $f$, which does not generalize well across heterogeneous data and modalities encountered in real-world clinical settings. In this work, we propose a fundamentally different, generative paradigm. We model the joint distribution $P(X,Y)$ using diffusion models and reframe inference as a test-time output optimization problem. By guiding the generative process to match o...

---

### 44. LLaVA-CKD: Bottom-Up Cascaded Knowledge Distillation for Vision-Language Models

**Authors:** Nikolaos Gkalelis, Vasileios Mezaris

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10641v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10641v1)

**Summary:** Large Vision-Language Models (VLMs) are successful in addressing a multitude of vision-language understanding tasks, such as Visual Question Answering (VQA), but their memory and compute requirements remain a concern for practical deployment. A promising class of techniques for mitigating this concern is Knowledge Distillation, where knowledge from a high-capacity Teacher network is transferred to a considerably smaller Student network. However, the capacity gap between the two networks is both ...

---

### 45. Product-of-Gaussian-Mixture Diffusion Models for Joint Nonlinear MRI Reconstruction

**Authors:** Laurenz Nagler, Martin Zach, Thomas Pock

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10629v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10629v1)

**Summary:** Recently, diffusion models have attracted considerable attention for magnetic resonance image reconstruction due to their high sample quality. However, most existing methods rely on large networks with opaque time-conditioning mechanisms, and require offline coil sensitivity estimation. This results in limited interpretability of the reconstruction process and reduced flexibility in the acquisition setup. To address these limitations, we jointly reconstruct the image and the coil sensitivities b...

---

### 46. Hypergraph-Enhanced Training-Free and Language-Free Few-Shot Anomaly Detection

**Authors:** Guohuan Xie, Xin He, Dingying Fan, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10628v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10628v1)

**Summary:** Few-shot anomaly detection (FSAD) has made significant strides, yet existing methods still face critical challenges: (i) dependence on task- or dataset-specific training/fine-tuning, (ii) reliance on language supervision or carefully hand-crafted prompts, and (iii) limited robustness across domains. In this paper, we introduce HyperFSAD, a novel FSAD framework that is training-free, language-free, and robust across domains, offering a powerful solution to these challenges. Built upon DINOv3 and ...

---

### 47. Vocabulary Hijacking in LVLMs: Unveiling Critical Attention Heads by Excluding Inert Tokens to Mitigate Hallucination

**Authors:** Yangneng Chen, Junlin Li, Weijun Yao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10622v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10622v1)

**Summary:** Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal tasks, yet their reliability is persistently undermined by hallucinations-generating text that contradicts visual input. Recent studies often attribute these errors to inadequate visual attention. In this work, we analyze the attention mechanisms via the logit lens, uncovering a distinct anomaly we term Vocabulary Hijacking. We discover that specific visual tokens, defined as Inert Tokens, disproportionately att...

---

### 48. MulTaBench: Benchmarking Multimodal Tabular Learning with Text and Image

**Authors:** Alan Arazi, Eilam Shapira, Shoham Grunblat, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10616v1)

**Summary:** Tabular Foundation Models have recently established the state of the art in supervised tabular learning, by leveraging pretraining to learn generalizable representations of numerical and categorical structured data. However, they lack native support for unstructured modalities such as text and image, and rely on frozen, pretrained embeddings to process them. On established Multimodal Tabular Learning benchmarks, we show that tuning the embeddings to the task improves performance. Existing benchm...

---

### 49. Segment Anything with Robust Uncertainty-Accuracy Correlation

**Authors:** Hongyou Zhou, Marc Toussaint, Ling Shao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10603v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10603v1)

**Summary:** Despite strong zero-shot performance, SAM is unreliable under domain shift due to Mask-level Confidence Confusion (MCC), where a single IoU-based mask score fails to reflect pixel-wise reliability near boundaries. Motivated by the contrast between texture-biased shortcuts in neural networks and shape-centric processing in human vision, we model out-of-domain variation as appearance shifts and non-rigid deformations that jointly stress calibration. We propose Segment Anything with Robust Uncertai...

---

### 50. Thinking with Novel Views: A Systematic Analysis of Generative-Augmented Spatial Intelligence

**Authors:** Yanbing Zhang, Bo Wang, Jianhui Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10588v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10588v1)

**Summary:** Current Large Multimodal Models (LMMs) struggle with spatial reasoning tasks requiring viewpoint-dependent understanding, largely because they are confined to a single, static observation. We propose Thinking with Novel Views (TwNV), a paradigm that integrates generative novel-view synthesis into the reasoning loop: a Reasoner LMM identifies spatial ambiguity, instructs a Painter to synthesize an alternative viewpoint, and re-examines the scene with the additional evidence. Through systematic ex...

---

## cs.LG

**50 papers**

### 1. ELF: Embedded Language Flows

**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10938v1)

**Summary:** Diffusion and flow-based models have become the de facto approaches for generating continuous data, e.g., in domains such as images and videos. Their success has attracted growing interest in applying them to language modeling. Unlike their image-domain counterparts, today's leading diffusion language models (DLMs) primarily operate over discrete tokens. In this paper, we show that continuous DLMs can be made effective with minimal adaptation to the discrete domain. We propose Embedded Language ...

---

### 2. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10934v1)

**Summary:** Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are eff...

---

### 3. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices

**Authors:** Chenyang Song, Weilin Zhao, Xu Han, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10933v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10933v1)

**Summary:** While Mixture-of-Experts (MoE) scales model capacity without proportionally increasing computation, its massive total parameter footprint creates significant storage and memory-access bottlenecks, which hinder efficient end-side deployment that simultaneously requires high performance, low computational cost, and small storage overhead. To achieve these properties, we present DECO, a sparse MoE architecture designed to match the performance of dense Transformers under identical total parameter b...

---

### 4. Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime

**Authors:** Albert Alcalde, Leon Bungert, Konstantin Riedl, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10931v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10931v1)

**Summary:** Transformers with self-attention modules as their core components have become an integral architecture in modern large language and foundation models. In this paper, we study the evolution of tokens in deep encoder-only transformers at inference time which is described in the large-token limit by a mean-field continuity equation. Leveraging ideas from the convergence analysis of interacting multi-particle systems, with particles corresponding to tokens, we prove that the token distribution rapid...

---

### 5. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning

**Authors:** Junhao Shen, Teng Zhang, Xiaoyan Zhao, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10923v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10923v1)

**Summary:** Large language model agents increasingly rely on external skills to solve complex tasks, where skills act as modular units that extend their capabilities beyond what parametric memory alone supports. Existing methods assume external skills either accumulate as persistent guidance or internalized into the policy, eventually leading to zero-skill inference. We argue this assumption is overly restrictive, since with limited parametric capacity and uneven marginal contribution across skills, the opt...

---

### 6. Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges

**Authors:** Usman A. Khan, Joseph W. Durham

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10917v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10917v1)

**Summary:** We consider anonymous multi-agent path finding (MAPF) where a set of robots is tasked to travel to a set of targets on a finite, connected graph. We show that MAPF can be cast as a special class of multi-marginal optimal transport (MMOT) problems with an underlying Markovian structure, under which the exponentially large MMOT collapses to a linear program (LP) polynomial in size. Focusing on the anonymous setting, we establish conditions under which the corresponding LP is feasible, totally unim...

---

### 7. Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis

**Authors:** Richie Yeung, Aleks Kissinger, Rob Cornish

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10910v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10910v1)

**Summary:** We consider the problem of synthesizing Clifford quantum circuits for devices with all-to-all qubit connectivity. We approach this task as a reinforcement learning problem in which an agent learns to discover a sequence of elementary Clifford gates that reduces a given symplectic matrix representation of a Clifford circuit to the identity. This formulation permits a simple learning curriculum based on random walks from the identity. We introduce a novel neural network architecture that is equiva...

---

### 8. Revisiting Policy Gradients for Restricted Policy Classes: Escaping Myopic Local Optima with $k$-step Policy Gradients

**Authors:** Alex DeWeese, Guannan Qu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10909v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10909v1)

**Summary:** This work revisits standard policy gradient methods used on restricted policy classes, which are known to get stuck in suboptimal critical points. We identify an important cause for this phenomenon to be that the policy gradient is itself fundamentally myopic, i.e. it only improves the policy based on the one-step $Q$-function. In this work, we propose a generalized $k$-step policy gradient method that couples the randomness within a $k$-step time window and can escape the myopic local optima in...

---

### 9. DataMaster: Towards Autonomous Data Engineering for Machine Learning

**Authors:** Yaxin Du, Xiyuan Yang, Zhifan Zhou, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10906v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10906v1)

**Summary:** As model families, training recipes, and compute budgets become increasingly standardized, further gains in machine learning systems depend increasingly on data. Yet data engineering remains largely manual and ad hoc: practitioners repeatedly search for external datasets, adapt them to existing pipelines, validate candidate data through downstream training, and carry forward lessons from prior attempts. We study task-conditioned autonomous data engineering, where an autonomous agent improves a f...

---

### 10. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers

**Authors:** Nikita Kezins, Urbas Ekka, Pascal Berrang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10901v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10901v1)

**Summary:** Guardrail Classifiers defend production language models against harmful behavior, but although results seem promising in testing, they provide no formal guarantees. Providing formal guarantees for such models is hard because "harmful behavior" has no natural specification in a discrete input space: and the standard epsilon-ball properties used in other domains do not carry semantic meaning. We close this gap by shifting verification from the discrete input space to the classifier's pre-activatio...

---

### 11. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards

**Authors:** Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10899v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10899v1)

**Summary:** Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outputs lack ground-truth answers, their trajectories span many tool-augmented decisions, and standard post-training offers little mechanism for turning past attempts into reusable experience. In this work, we argue that rubrics should serve not merely as final-answer evaluators, but as the shared interf...

---

### 12. V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction

**Authors:** Marcin Kostrzewa, Sebastian Tomczak, Roman Furman, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10896v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10896v1)

**Summary:** Corporate bankruptcy prediction is a high-stakes financial task characterized by severe class imbalance and multi-horizon forecasting demands. Public datasets supporting it remain scarce and small: widely used free benchmarks contain between 6,000 and 80,000 company-year observations, while larger resources are behind subscription paywalls. To address this gap, we introduce V4FinBench, a benchmark of over one million company-year records from the Visegràd Group (V4) economies (2006-2021), with 1...

---

### 13. Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why

**Authors:** Mohammadreza Armandpour, Fatih Ilhan, David Harrison, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10889v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10889v1)

**Summary:** On-policy distillation offers dense, per-token supervision for training reasoning models; however, it remains unclear under which conditions this signal is beneficial and under which it is detrimental. Which teacher model should be used, and in the case of self-distillation, which specific context should serve as the supervisory signal? Does the optimal choice vary from one token to the next? At present, addressing these questions typically requires costly training runs whose aggregate performan...

---

### 14. LoKA: Low-precision Kernel Applications for Recommendation Models At Scale

**Authors:** Liang Luo, Yinbin Ma, Quanyu Zhu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10886v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10886v1)

**Summary:** Recent GPU generations deliver significantly higher FLOPs using lower-precision arithmetic, such as FP8. While successfully applied to large language models (LLMs), its adoption in large recommendation models (LRMs) has been limited. This is because LRMs are numerically sensitive, dominated by small matrix multiplications (GEMMs) followed by normalization, and trained in communication-intensive environments. Applying FP8 directly to LRMs often degrades model quality and prolongs training time. T...

---

### 15. Neural Weight Norm = Kolmogorov Complexity

**Authors:** Tiberiu Musat

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10878v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10878v1)

**Summary:** Why does weight decay work? We prove that, in any fixed-precision regime, the smallest weight norm of a looped neural network outputting a binary string equals the Kolmogorov complexity of that string, up to a logarithmic factor. This implies that weight decay induces a prior matching Solomonoff's universal prior, the optimal prior over computable functions, up to a polynomial factor. The result is norm-agnostic: in fixed precision, every weight norm collapses to the non-zero parameter count up ...

---

### 16. AssayBench: An Assay-Level Virtual Cell Benchmark for LLMs and Agents

**Authors:** Edward De Brouwer, Carl Edwards, Alexander Wu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10876v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10876v1)

**Summary:** Recent advances in machine learning and large-scale biological data collections have revived the prospect of building a virtual cell, a computational model of cellular behavior that could accelerate biological discovery. One of the most compelling promises of this vision is the ability to perform in silico phenotypic screens, in which a model predicts the effects of cellular perturbations in unseen biological contexts. This task combines heterogeneous textual inputs with diverse phenotypic outpu...

---

### 17. Compute Where it Counts: Self Optimizing Language Models

**Authors:** Yash Akhauri, Mohamed S. Abdelfattah

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10875v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10875v1)

**Summary:** Efficient LLM inference research has largely focused on reducing the cost of each decoding step (e.g., using quantization, pruning, or sparse attention), typically applying a uniform computation budget to every generated token. In practice, token difficulty varies widely, so static compression can over-compute on easy steps and under-compute on hard ones. We study dynamic budget allocation for autoregressive decoding: learning how much computation to spend per token from within a single model.  ...

---

### 18. Attractor-Vascular Coupling Theory: Formal Grounding and Empirical Validation for AAMI-Standard Cuffless Blood Pressure Estimation from Smartphone Photoplethysmography

**Authors:** Timothy Oladunni, Farouk Ganiyu Adewumi

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10871v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10871v1)

**Summary:** This work proposes Attractor-Vascular Coupling Theory (AVCT), a mathematical framework showing that cardiac attractor geometry encodes blood pressure (BP) information sufficient for AAMI-standard estimation, and validates the theory through a calibrated cuffless BP model using photoplethysmography (PPG). AVCT is grounded in Cardiac Stability Theory and operationalized using Takens delay embedding and attractor morphology extraction. Two theorems, one proposition, and one corollary formally justi...

---

### 19. BEACON: A Multimodal Dataset for Learning Behavioral Fingerprints from Gameplay Data

**Authors:** Ishpuneet Singh, Gursmeep Kaur, Uday Pratap Singh Atwal, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10867v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10867v1)

**Summary:** Continuous authentication in high-stakes digital environments requires datasets with fine-grained behavioral signals under realistic cognitive and motor demands. But current benchmarks are often limited by small scale, unimodal sensing or lack of synchronised environmental context. To address this gap, this paper introduces BEACON ( Behavioral Engine for Authentication \& Continuous Monitoring), a large-scale multimodal dataset that captures diverse skill tiers in competitive \textit{Valorant} g...

---

### 20. Masked Generative Transformer Is What You Need for Image Editing

**Authors:** Wei Chow, Linfeng Li, Xian Sun, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10859v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10859v1)

**Summary:** Diffusion models dominate image editing, yet their global denoising mechanism entangles edited regions with surrounding context, causing modifications to propagate into areas that should remain intact. We propose a fundamentally different approach by leveraging Masked Generative Transformers (MGTs), whose localized token-prediction paradigm naturally confines changes to intended regions. We present EditMGT, an MGT-based editing framework that is the first of its kind. Our approach employs multi-...

---

### 21. The Generalized Turing Test: A Foundation for Comparing Intelligence

**Authors:** Daniel Mitropolsky, Susan S. Hong, Riccardo Neumarker, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10851v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10851v1)

**Summary:** We introduce the Generalized Turing Test (GTT), a formal framework for comparing the capabilities of arbitrary agents via indistinguishability. For agents A and B, we define the Turing comparator A $\geq$ B to hold if B, acting as a distinguisher, cannot reliably distinguish between interactions with A (instructed to imitate B) and another instance of B. This yields a dataset- and task-agnostic notion of relative intelligence. We study the comparator's structure, including conditions under which...

---

### 22. Conditional anomaly detection methods for patient-management alert systems

**Authors:** Michal Valko, Gregory Cooper, Amy Seybert, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10847v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10847v1)

**Summary:** Anomaly detection methods can be very useful in identifying unusual or interesting patterns in data. A recently proposed conditional anomaly detection framework extends anomaly detection to the problem of identifying anomalous patterns on a subset of attributes in the data. The anomaly always depends (is conditioned) on the value of remaining attributes. The work presented in this paper focuses on instance-based methods for detecting conditional anomalies. The methods rely on the distance metric...

---

### 23. Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories

**Authors:** Yixuan Yang, Mehak Arora, Ryan Zhang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10840v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10840v1)

**Summary:** We present Clin-JEPA, a multi-phase co-training framework for joint-embedding predictive (JEPA) pretraining on EHR patient trajectories. JEPA architectures have enabled latent-space planning in robotics and high-quality representation learning in vision, but extending the paradigm to EHR data -- to obtain a single backbone that simultaneously forecasts patient trajectories and serves diverse downstream risk-prediction tasks without per-task fine-tuning -- remains an open challenge. Existing JEPA...

---

### 24. Transcoda: End-to-End Zero-Shot Optical Music Recognition via Data-Centric Synthetic Training

**Authors:** Daniel Dratschuk, Paul Swoboda

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10835v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10835v1)

**Summary:** Optical Music Recognition (OMR), the task of transcribing sheet music into a structured textual representation, is currently bottlenecked by a lack of large-scale, annotated datasets of real scans. This forces models to rely on either few-shot transfer or synthetic training pipelines that remain overly simplistic. A secondary challenge is encoding non-uniqueness: in the popular Humdrum **kern format for transcribing music, multiple different text encodings can render into the same visual sheet m...

---

### 25. SLIM: Sparse Latent Steering for Interpretable and Property-Directed LLM-Based Molecular Editing

**Authors:** Mingxu Zhang, Yuhan Li, Lujundong Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10831v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10831v1)

**Summary:** Large language models possess strong chemical reasoning capabilities, making them effective molecular editors. However, property-relevant information is implicitly entangled across their dense hidden states, providing no explicit handle for property control: a substantial fraction of edits fail to improve or even degrade target properties. To address these issues, we propose SLIM (Sparse Latent Interpretable Molecular editing), a plug-and-play framework that decomposes the editor's hidden states...

---

### 26. Predicting 3D structure by latent posterior sampling

**Authors:** Azmi Haider, Dan Rosenbaum

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10830v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10830v1)

**Summary:** The remarkable achievements of both generative models of 2D images and neural field representations for 3D scenes present a compelling opportunity to integrate the strengths of both approaches. In this work, we propose a methodology that combines a NeRF-based representation of 3D scenes with probabilistic modeling and reasoning using diffusion models. We view 3D reconstruction as a perception problem with inherent uncertainty that can thereby benefit from probabilistic inference methods. The cor...

---

### 27. NoRIN: Backbone-Adaptive Reversible Normalization for Time-Series Forecasting

**Authors:** Shun Zhang, Yuyang Xiao

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10823v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10823v1)

**Summary:** Reversible instance normalization (RevIN) and its successors (Dish-TS, SAN, FAN) have become the de facto plug-in for time-series forecasting, yet the map they apply to each data point is strictly affine, $x \mapsto ax+b$, so they cannot reshape the underlying distribution -- heavy tails remain heavy and skewness remains uncorrected. We propose NoRIN, a non-linear reversible normalization based on the arcsinh-form Johnson $S_U$ transform with two shape parameters $(δ,\varepsilon)$ that control t...

---

### 28. Benchmarking Sensor-Fault Robustness in Forecasting

**Authors:** Alexander Windmann, Philipp Wittenberg, Gianluca Manca, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10822v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10822v1)

**Summary:** Cyber-physical system (CPS) forecasting models depend on sensor streams with noisy, biased, missing, or temporally misaligned readings, yet standard forecasting evaluation often selects models by nominal error without showing whether they remain robust under such faults. We introduce SensorFault-Bench, a shared CPS-grounded sensor-fault stress-test protocol for evaluating forecasting architectures and robustness-improvement methods, and an operational taxonomy organizing the method comparison. A...

---

### 29. MaD Physics: Evaluating information seeking under constraints in physical environments

**Authors:** Moksh Jain, Mehdi Bennani, Johannes Bausch, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10820v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10820v1)

**Summary:** Scientific discovery is fundamentally a resource-constrained process that requires navigating complex trade-offs between the quality and quantity of measurements due to physical and cost constraints. Measurements drive the scientific process by revealing novel phenomena to improve our understanding. Existing benchmarks for evaluating agents for scientific discovery focus on either static knowledge-based reasoning or unconstrained experimental design tasks, and do not capture the ability to make ...

---

### 30. On periodic distributed representations using Fourier embeddings

**Authors:** Jakeb Chouinard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10818v1)

**Summary:** Periodic signals are critical for representing physical and perceptual phenomena. Scalar, real angular measures, e.g., radians and degrees, result in difficulty processing and distinguishing nearby angles, especially when their absolute difference exceeds pi. We can avoid this problem by using real-valued, periodic embeddings in high-dimensional space. These representations also allow us to control the nature of their dot product similarities, allowing us to construct a variety of different kern...

---

### 31. Policy Gradient Methods for Non-Markovian Reinforcement Learning

**Authors:** Avik Kar, Siddharth Chandak, Rahul Singh, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10816v1)

**Summary:** We study policy gradient methods for reinforcement learning in non-Markovian decision processes (NMDPs), where observations and rewards depend on the entire interaction history. To handle this dependence, the agent maintains an internal state that is recursively updated to provide a compact summary of past observations and actions. In contrast to approaches that treat the agent state dynamics as fixed or learn it via predictive objectives, we propose a reward-centric formulation that jointly opt...

---

### 32. Likelihood scoring for continuations of mathematical text: a self-supervised benchmark with tests for shortcut vulnerabilities

**Authors:** Daniel Ranard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10810v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10810v1)

**Summary:** We introduce an automatically generated benchmark for predicting hidden text in technical papers. A paper supplies visible context $X$ and a hidden continuation $Y$; the evaluated model writes an auxiliary forecast string $Z$, and a separate scorer assigns next-token probability to $Y$ both with and without conditioning on $Z$. This gives a label-free test of whether $Z$ transmits information about the continuation, compared against controls where $Z$ is recent context rather than a forecast. Ou...

---

### 33. Mistake-Bounded Language Generation

**Authors:** Jon Kleinberg, Charlotte Peale, Omer Reingold

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10809v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10809v1)

**Summary:** We investigate the learning task of language generation in the limit, but shift focus from the traditional time-of-last-mistake metric of a generator's success to a new notion of "mistake-bounded generation." While existing results for language generation in the limit focus on guaranteeing eventual consistency, they are blind to the cumulative error incurred during the learning process. We address this by shifting the goal to minimizing the total number of invalid elements output by a generation...

---

### 34. LLMs for Secure Hardware Design and Related Problems: Opportunities and Challenges

**Authors:** Johann Knechtel, Ozgur Sinanoglu, Ramesh Karri

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10807v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10807v1)

**Summary:** The integration of Large Language Models (LLMs) into Electronic Design Automation (EDA) and hardware security is rapidly reshaping the semiconductor industry. While LLMs offer unprecedented capabilities in generating Register Transfer Level (RTL) code, automating testbenches, and bridging the semantic gap between high-level specifications and silicon, they simultaneously introduce severe vulnerabilities. This comprehensive review provides an in-depth analysis of the state-of-the-art in LLM-drive...

---

### 35. PhyGround: Benchmarking Physical Reasoning in Generative World Models

**Authors:** Juyi Lin, Arash Akbari, Yumei He, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10806v1)

**Summary:** Generative world models are increasingly used for video generation, where learned simulators are expected to capture the physical rules that govern real-world dynamics. However, evaluating whether generated videos actually follow these rules remains challenging. Existing physics-focused video benchmarks have made important progress, but they still face three key challenges, including the coarse evaluation frameworks that hide law-specific failures, response biases and fatigue that undermine the ...

---

### 36. The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies

**Authors:** Gabriel Garcia

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10799v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10799v1)

**Summary:** Corruption studies, the primary tool for evaluating chain-of-thought (CoT) faithfulness, identify which chain positions are "computationally important" by measuring accuracy when steps are replaced with errors. We identify a systematic confound: for chains with explicit terminal answer statements, the dominant format in standard benchmarks, corruption studies detect where the answer text appears, not where computation occurs.   A within-dataset format ablation provides the key evidence: on stand...

---

### 37. Muown: Row-Norm Control for Muon Optimization

**Authors:** Kai Lion, Florian Hübler, Bingcong Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10797v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10797v1)

**Summary:** Muon has emerged as a strong competitor to AdamW for language model pre-training, yet its behavior at scale is sensitive to weight decay. Recent work has observed that, for Muon without decoupled weight decay, the spectral norm of weight matrices drifts upward over training. Through a decomposition of the spectral norm into a row-magnitude factor and a row-coherence factor, we identify the former as the empirical driver of this drift under Muon, while the latter remains well-behaved along the tr...

---

### 38. Factual recall in linear associative memories: sharp asymptotics and mechanistic insights

**Authors:** Alessio Giorlandino, Sebastian Goldt, Antoine Maillard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10795v1)

**Summary:** Large language models demonstrate remarkable ability in factual recall, yet the fundamental limits of storing and retrieving input--output associations with neural networks remain unclear. We study these limits in a minimal setting: a linear associative memory that maps $p$ input embeddings in $\mathbb{R}^d$ to their corresponding~$d$-dimensional targets via a single layer, requiring each mapped input to be well separated from all other targets. Unlike in supervised classification, this strict s...

---

### 39. ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs

**Authors:** Chayne Thrash, Ali Abbasi, Soheil Kolouri

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10793v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10793v1)

**Summary:** Large language models (LLMs) are costly to deploy due to their large memory footprint and high inference cost. Weight-activation quantization can reduce these costs, but low-bit activation quantization remains difficult because activation outliers induce large quantization error. Recent rotation-based methods address this by applying orthogonal transformations that redistribute activation magnitude across dimensions, but existing approaches either require expensive end-to-end rotation training o...

---

### 40. Fixed-Point Neural Optimal Transport without Implicit Differentiation

**Authors:** Yesom Park, Eric Gelphman, Stanley Osher, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10792v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10792v1)

**Summary:** We propose an implicit neural formulation of optimal transport that eliminates adversarial min--max optimization and multi-network architectures commonly used in existing approaches. Our key idea is to parameterize a single potential in the Kantorovich dual and reformulate the associated c-transform as a proximal fixed-point problem. This yields a stable single-network framework in which dual feasibility is enforced exactly through proximal optimality conditions rather than adversarial training....

---

### 41. Elucidating Representation Degradation Problem in Diffusion Model Training

**Authors:** Zhipeng Yao, Dazhou Li, Zitong Zhang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10790v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10790v1)

**Summary:** Diffusion models have achieved remarkable success, yet their training remains inefficient due to a severe optimization bottleneck, which we term Representation Degradation. As noise levels increase, the outputs of the trained model exhibit progressive structural distortion, which can destabilize training and impair generation quality. Our analysis suggests that this instability is driven by mismatched target recoverability, which is associated with Neural Tangent Kernel (NTK) spectral weakening ...

---

### 42. MASS-DPO: Multi-negative Active Sample Selection for Direct Policy Optimization

**Authors:** Rohan Surana, Xintong Li, Sheldon Yu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10784v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10784v1)

**Summary:** Multi-negative preference optimization under the Plackett--Luce (PL) model extends Direct Preference Optimization (DPO) by leveraging comparative signals across one preferred and multiple rejected responses. However, optimizing over large negative pools is costly, and many candidates contribute redundant gradients due to their similar effects on policy updates. We introduce MASS-DPO, a multi-negative active sample selection method that derives a PL-specific Fisher-information objective for selec...

---

### 43. Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

**Authors:** Jeonghye Kim, Jiwon Jeon, Dongsheng Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10781v1)

**Summary:** Self-distillation has emerged as a powerful framework for post-training LLMs, where a teacher conditioned on extra information guides a student without it, both from the same model. While this guidance is useful when the student has failed, on successful rollouts, the same mechanism instead overwrites the student's choices and suppresses it's own reasoning. Therefore, we propose reading the original self-distillation signal in reverse: when the student succeeds along a path the teacher would not...

---

### 44. Locking Pretrained Weights via Deep Low-Rank Residual Distillation

**Authors:** Keitaro Sakamoto, Pierre Ablin, Federico Danieli, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10777v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10777v1)

**Summary:** The quality of open-weight language models has dramatically improved in recent years. Sharing weights greatly facilitates model adoption by enabling their use across diverse hardware and software platforms. They also allow for more open research and testing, to the extent that users can use them as checkpoints, fine-tune them according to their needs, and potentially redistribute them. In some cases, however, concerns on modifying these weights towards unauthorized uses may outweigh the pros of ...

---

### 45. On the global convergence of gradient descent for wide shallow models with bounded nonlinearities

**Authors:** Romain Petit, Clarice Poon, Gabriel Peyré

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10775v1)

**Summary:** A surprising phenomenon in the training of neural networks is the ability of gradient descent to find global minimizers of the training loss despite its non-convexity. Following earlier works, we investigate this behavior for wide shallow networks. Existing results essentially cover the case of ReLU activations and the case of sigmoid activations with scalar output weights. We study a large class of models that includes multi-head attention layers and two-layer sigmoid networks with vector outpu...

---

### 46. DynaMiCS: Fine-tuning LLMs with Performance Constraints using Dynamic Mixtures

**Authors:** Eleonora Gualdoni, Sonia Laguna, Louis Bethune, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10770v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10770v1)

**Summary:** Multi-domain fine-tuning of large language models requires improving performance on target domains while preserving performance on constrained domains, such as general knowledge, instruction following, or safety evaluations. Existing data mixing strategies rely on fixed heuristics or adaptive rules that cannot explicitly enforce preservation of such capabilities. We propose DynaMiCS, a dynamic mixture optimizer that casts multi-domain fine-tuning as a constrained optimization problem. At each up...

---

### 47. Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning

**Authors:** Tao Hu, Da-Wei Zhou

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10765v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10765v1)

**Summary:** Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world deployment often requires continual capability expansion across sequential tasks. In such scenarios, Multimodal Continual Instruction Tuning (MCIT) aims to acquire new capabilities while limiting catastrophic forgetting. Existing methods mainly follow a module-composition paradigm: they maintain task-level prompts or LoRA experts and dynamically route or aggregate a subset of them at in...

---

### 48. Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models

**Authors:** Andreas Bergmeister, Stefanie Jegelka, Nikolas Nüsken, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10759v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10759v1)

**Summary:** Diffusion and flow-matching models scale because pretraining is supervised regression: a clean sample is noised analytically, and a model regresses against a closed-form target. RL post-training aligns the model with a reward. In image generation, this makes samples compose objects correctly, render text legibly, and match human preferences. Existing methods rely on costly SDE rollouts, reward gradients, or surrogate losses, sacrificing pretraining's regression structure. We show that the struct...

---

### 49. Provable Sparse Inversion and Token Relabel Enhanced One-shot Federated Learning with ViTs

**Authors:** Li Shen, Xiaolei Hao, Qinglun Li, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10748v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10748v1)

**Summary:** One-Shot Federated Learning, where a central server learns a global model in a single communication round, has emerged as a promising paradigm. However, under extremely non-IID settings, existing data-free methods often generate low-quality data that suffers from severe semantic misalignment with ground-truth labels. To overcome these issues, we propose a novel Federated Model Inversion and Token Relabel (FedMITR) framework, which trains the global model by fully exploiting all patches of synthe...

---

### 50. AdaPaD: Adaptive Parallel Deflation for PEFT with Self-Correcting Rank Discovery

**Authors:** Barbara Su, Fangshuo Liao, Anastasios Kyrillidis

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10741v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10741v1)

**Summary:** Fine-tuning large language models with LoRA requires choosing a rank r before training starts. Existing approaches either extract rank-1 components sequentially, freezing each component's error permanently into every subsequent residual, or optimize the full low-rank factorization jointly with guarantees that describe only the joint update, not individual rank-1 directions. We present AdaPaD (Adaptive Parallel Deflation), which trains all rank-1 components simultaneously: each worker refines its...

---

## cs.NE

**50 papers**

### 1. Energy-Efficient Implementation of Spiking Recurrent Cells on FPGA

**Authors:** Pascal Harmeling, Florent De Geeter, Guillaume Drion

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10679v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10679v1)

**Summary:** Spiking Neural Networks (SNNs) can reduce energy consumption compared to conventional Artificial Neural Networks (ANNs) when spiking activity is sparse and the neuron model is hardware-friendly. However, biologically faithful models are often too costly to implement on FPGAs, whereas very simple models (e.g., IR/LIF) sacrifice part of the neuronal dynamics. In this work, we present an FPGA accelerator for an SNN using Spiking Recurrent Cell (SRC) neurons, providing a trade-off between biological...

---

### 2. A Theory of Multilevel Interactive Equilibrium in NeuroAI

**Authors:** Zhe Sage Chen, Quanyan Zhu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10505v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10505v1)

**Summary:** We propose a game-theoretic framework for adaptive multi-agent intelligent systems. Unlike classical game theory, which often treats strategies as primitive objects chosen by perfectly rational agents, the proposed framework provides a mathematical foundation for studying equilibrium in NeuroAI and can be viewed as an extension of game theory under relaxed assumptions, including partial observability, bounded computation, and uncertainty. At its core, Multilevel Interactive Equilibrium (MIE) gen...

---

### 3. Causal Explanations from the Geometric Properties of ReLU Neural Networks

**Authors:** Hector Woods, Philippa Ryan, Rob Alexander

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10396v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10396v1)

**Summary:** Neural networks have proved an effective means of learning control policies for autonomous systems, but these learned policies are difficult to understand due to the black-box nature of neural networks. This lack of interpretability makes safety assurance for such autonomous systems challenging. The fields of eXplainable Artificial Intelligence (XAI) and eXplainable Reinforcement Learning (XRL) aim to interpret the decision making processes of neural networks and autonomous agents, respectively....

---

### 4. Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization

**Authors:** Yukun Du, Haiyue Yu, Jiang Jiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10260v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10260v1)

**Summary:** Existing Meta-Black-Box Optimization (MetaBBO) methods focus on how to search when controlling optimizers, but largely overlook where to search. We propose MetaSG-SAEA, a bi-level MetaBBO framework for expensive constrained multi-objective optimization problems (ECMOPs), in which a meta-policy provides search guidance to the low-level Surrogate-Assisted Evolutionary Algorithm (SAEA). To achieve this, we introduce Max-Min Constraint-Calibrated Inequality (MM-CCI), a compact, problem-agnostic regi...

---

### 5. Joint sparse coding and temporal dynamics support context reconfiguration

**Authors:** Qianqian Shi, Yue Che, Faqiang Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10178v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10178v1)

**Summary:** Adaptive behavior requires the brain to transition between distinct contexts while maintaining representations of prior experience. The ability to reconfigure neural representations without erasing previously acquired knowledge is central to learning in dynamic environments, yet the neural mechanisms that support this balance remain unclear. Understanding these mechanisms is also critical for addressing catastrophic forgetting in artificial systems designed for lifelong learning. Here, we identi...

---

### 6. Prospective Compression in Human Abstraction Learning

**Authors:** Leonardo Hernandez Cano, Ivan Zareski, Luisa El Amouri, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09985v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09985v1)

**Summary:** A core challenge in program synthesis is online library learning: the incremental acquisition of reusable abstractions under uncertainty about future task demands. Existing algorithms treat library learning as retrospective compression over a static task distribution, where the learned library is determined by the corpus of past tasks. However, real-world learning domains are often non-stationary, with tasks arising from a generative process that evolves over time. We propose and test the hypoth...

---

### 7. Frequency Matching in Spiking Neural Networks for mmWave Sensing

**Authors:** Di Yu, Zhenyu Liao, Changze Lv, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09983v1)

**Summary:** Millimeter-wave (mmWave) sensing enables privacy-preserving, always-on edge perception, but its measurements are often sparse, temporally irregular, and corrupted by high-frequency noise. Existing mmWave pipelines predominantly rely on artificial neural networks (ANNs), which achieve robustness through extensive preprocessing or deep architectures, thereby limiting their efficiency on edge devices. In this work, we study spiking neural networks (SNNs) for mmWave sensing from a mechanism-data ali...

---

### 8. Parameter-Efficient Neuroevolution for Diverse LLM Generation: Quality-Diversity Optimization via Prompt Embedding Evolution

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09781v1)

**Summary:** Large Language Models exhibit mode collapse, producing homogeneous outputs that fail to explore valid solution spaces. We present QD-LLM, a framework for parameter-efficient neuroevolution that evolves prompt embeddings, compact neural interfaces (~32K parameters) that steer generation in frozen LLMs (70B+ parameters), within a Quality-Diversity (QD) optimization framework. Our contributions: (1) evolved prompt embeddings via gradient-free optimization enabling behavioral steering without model ...

---

### 9. EvoPref: Multi-Objective Evolutionary Optimization Discovers Diverse LLM Alignments Beyond Gradient Descent

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09777v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09777v1)

**Summary:** Gradient-based preference optimization methods for large language model (LLM) alignment suffer from preference collapse, converging to narrow behavioral modes while neglecting preference diversity. We introduce EvoPref, a multi-objective evolutionary algorithm that maintains populations of Low-Rank Adaptation (LoRA) adapters optimized across helpfulness, harmlessness, and honesty objectives using Non-dominated Sorting Genetic Algorithm II (NSGA-II) selection with archive-based diversity preserva...

---

### 10. Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09770v1)

**Summary:** Spike-based encodings are sparse and energy-efficient, but have largely been formulated probabilistically, disconnected from most signal processing literature. We recast spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. The proposed wavelets preserve the sparsity and locality of spiking representations, with reconstruction up to spike quantization and time discretization. We demonstrate reconstruction on ECG and audio datasets, achieving a...

---

### 11. LEVI: Stronger Search Architectures Can Substitute for Larger LLMs in Evolutionary Search

**Authors:** Temoor Tanveer

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09764v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09764v1)

**Summary:** LLM-guided evolutionary methods such as AlphaEvolve have proven effective in domains like math, systems research, and algorithmic discovery, but their reliance on frontier models makes each run expensive. We argue this is largely an artifact of how existing frameworks allocate search: archives that fail to preserve solution diversity force compensation through stronger mutation models; blind model use spends frontier dollars on local edits a smaller model could handle; and full-set evaluation wa...

---

### 12. Discovery of Nonlinear Dynamics with Automated Basis Function Generation

**Authors:** Mohammad Amin Basiri, Charles Nicholson

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09696v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09696v1)

**Summary:** Discovering governing equations from observational data remains a fundamental challenge in scientific modeling, particularly when the underlying mathematical structure is unknown. Traditional sparse identification methods like SINDy excel at discovering parsimonious models but require researchers to specify candidate basis functions a priori, a limitation that often leads to model failure when critical terms are omitted or when systems exhibit unconventional dynamics. Purely symbolic regression ...

---

### 13. RDEx-CASK: Cauchy Mutation, Archive, and Stagnation Kick for RDEx-CSOP

**Authors:**  Dikshant, Dikshit Chauhan, Chen Hao, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09652v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09652v1)

**Summary:** We extend RDEx-CSOP with 3 changes that target stagnation & late-stage variance, plus minor parameter tuning. The second scale factor in the standard branch is sampled independently from a truncated Cauchy. A small feasible-only JADE-style archive (|A|_max = 50) is added & sampled with probability |A|/(|A|+|P|). Per-individual stagnation counter triggers, after 180 no-improvement generations, three local overrides on standard branch: pull toward the global best, lift the archive sampling floor t...

---

### 14. Neuromorphic Reinforcement Learning for Quadruped Locomotion Control on Uneven Terrain

**Authors:** Zhuangyu Han, Abhronil Sengupta

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09595v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09595v1)

**Summary:** Reinforcement learning (RL) has enabled robust quadruped locomotion over complex terrain, but most learned controllers are trained offline with backpropagation in massively parallel simulation and deployed as fixed policies, limiting adaptation to terrain variation, payload changes, actuator wear, and other real-world conditions under onboard power constraints. Local learning provides a potential path toward energy-aware on-robot adaptation by replacing global backpropagation graphs with updates...

---

### 15. Sparsity Moves Computation: How FFN Architecture Reshapes Attention in Small Transformers

**Authors:** Gabriel Smithline, Chris Mascioli

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09403v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09403v1)

**Summary:** Architectural choices inside the Transformer feedforward network (FFN) block do not merely affect the block itself; they reshape the computations learned by the rest of the model. We study this effect in one-layer Transformers trained on digit addition with carry, modular arithmetic, and histogram counting. Comparing dense FFNs, gated linear units (GLUs), mixture-of-experts (MoE), and MoE-GLUs, we find that sparse MoE routing can shift computation from FFN to attention, with the strongest ablati...

---

### 16. Evolutionary Ensemble of Agents

**Authors:** Zongmin Yu, Liu Yang

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.09018v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09018v1)

**Summary:** We introduce Evolutionary Ensemble (EvE), a decentralized framework that organizes existing, highly capable coding agents into a live, co-evolving system for algorithmic discovery. Rather than reinventing the wheel within the "LLMs as optimizers" paradigm, EvE fixes the base agent substrate and focuses entirely on evolving the cumulative guidance and skills that dictate agent behaviors. By maintaining two co-evolving populations, namely functional code solvers and agent guidance states, the syst...

---

### 17. Drain-Vortex Optimization: A Population-Based Metaheuristic Inspired by Multi-Drain Free-Vortex Flow

**Authors:** Mohsen Omidi, Brian Vaughan

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08883v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08883v1)

**Summary:** This paper proposes Drain-Vortex Optimization (DVO), a population-based metaheuristic for continuous optimization. DVO models each candidate solution as a particle moving in a multi-drain vortex field. Its update rule decomposes motion into radial attraction toward selected drain centres and tangential rotation governed by a regularized free-vortex law. A three-phase mechanism switches between far-field exploration, spiral inward motion, and localized core exploitation according to the normalize...

---

### 18. AHD Agent: Agentic Reinforcement Learning for Automatic Heuristic Design

**Authors:** Haoze Lv, Ning Lu, Ziang Zhou, et al.

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08756v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08756v1)

**Summary:** Automatic heuristic design (AHD) has emerged as a promising paradigm for solving NP-hard combinatorial optimization problems (COPs). Recent works show that large language models (LLMs), when integrated into well-designed frameworks (i.e., LLM-AHD), can autonomously discover high-performing heuristics. However, existing LLM-AHD frameworks typically treat LLMs as passive generators within fixed workflows, where the model generates heuristics from manually designed, limited context. Such context ma...

---

### 19. Structure-Preserving Reconstruction of Convex Lipschitz Functionals on Hilbert Spaces from Finite Samples

**Authors:** Anastasis Kratsios

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08559v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08559v1)

**Summary:** Convex functionals are ubiquitous in applied analysis, appearing as value functions, risk measures, super-hedging prices, and loss functionals in machine learning. In many applications, however, the functional is only observed through finitely many exact pointwise evaluations. We ask whether a convex functional on a separable Hilbert space $H$ can be reconstructed, up to arbitrary uniform accuracy, by an explicit formula which preserves convexity and Lipschitz regularity and is finitely computab...

---

### 20. Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction

**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08022v1)

**Summary:** Spiking Neural Networks (SNNs) have been proposed as biologically plausible and energy-efficient alternatives to conventional Artificial Neural Networks (ANNs). However, the training of SNN usually relies on surrogate gradients due to the non-differentiability of the spike function, introducing approximation errors that accumulate across layers. To address this challenge, we extend the work on convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, wh...

---

### 21. Broken-symmetry shape discrimination on a driven Duffing ring

**Authors:** Kaspar Anton Schindler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07475v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07475v1)

**Summary:** Distributed computational substrates rely on two elementary operations: bundling, the act of populating a shared physical medium with independently retrievable components, and binding, the act of composing components into outputs whose identity depends on their relations. We study these two primitives on the simplest closed substrate carrying a continuous symmetry, a cycle graph of N nodes, in two parameter regimes of a single master equation of motion. The linear regime sorts a temporal input a...

---

### 22. Discovering Ordinary Differential Equations with LLM-Based Qualitative and Quantitative Evaluation

**Authors:** Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07323v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07323v1)

**Summary:** Discovering governing differential equations from observational data is a fundamental challenge in scientific machine learning. Existing symbolic regression approaches rely primarily on quantitative metrics; however, real-world differential equation modeling also requires incorporating domain knowledge to ensure physical plausibility. To address this gap, we propose DoLQ, a method for discovering ordinary differential equations with LLM-based qualitative and quantitative evaluation. DoLQ employs...

---

### 23. Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability

**Authors:** Dengzhe Hou, Zihao Wu, Lingyu Jiang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07212v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07212v1)

**Summary:** Electroencephalography (EEG) is a cornerstone of brain-computer interfaces and clinical neuroscience, yet deep learning models are typically trained and evaluated under a single, unreported preprocessing pipeline. We formalize preprocessing choices as a counterfactual intervention space and show that EEG predictions are surprisingly unstable under this space: across six datasets spanning four paradigms, up to 42% of trial-level predictions flip when only the preprocessing changes, a variability ...

---

### 24. Direct-to-Event Spiking Neural Network Transfer

**Authors:** Nhan Trong Luu, Duong Trung Luu, Pham Ngoc Nam, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07207v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07207v1)

**Summary:** Spiking Neural Networks (SNNs) have gained increasing attention due to their potential for low-power computation on neuromorphic hardware. A widely adopted training strategy for SNNs is direct coding, which enable backpropagation on neuron implementations using continuous-valued surrogate activations. However, recent studies have shown that direct-coded SNNs remain substantially less energy-efficient than their event-based counterparts, limiting their practical deployment in energy sensitive sce...

---

### 25. Every Feedforward Neural Network Definable in an o-Minimal Structure Has Finite Sample Complexity

**Authors:** Anastasis Kratsios, Gregory Cousins, Haitz Sáez de Ocáriz Borde, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07097v1)

**Summary:** We show that, in a precise sense, a broad class of feedforward neural networks learn (have finite sample complexity) in the PAC model: every fixed finite feedforward architecture whose layers are definable in an o-minimal structure has finite sample complexity in the agnostic PAC setting, even with unbounded parameters. This covers standard fixed-size MLPs, CNNs, GNNs, and transformers with fixed sequence length, together with the operations and layers typically used in such architectures, inclu...

---

### 26. A Unified Measure-Theoretic View of Diffusion, Score-Based, and Flow Matching Generative Models

**Authors:** Aditya Ranganath, Mukesh Singhal

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06829v1)

**Summary:** We survey continuous-time generative modeling methods based on transporting a simple reference distribution to a data distribution via stochastic or deterministic dynamics. We present a unified framework in which diffusion models, score-based generative models, and flow matching are instances of learning a time-dependent vector field that induces a family of marginals $(ρ_t)_{t \in [0,1]}$ governed by continuity and Fokker-Planck equations. Such a unified theory is timely because these methods a...

---

### 27. The Causally Emergent Alignment Hypothesis: Causal Emergence Aligns with and Predicts Final Reward in Reinforcement Learning Agents

**Authors:** Federico Pigozzi, Michael Levin

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06746v1)

**Summary:** A hallmark of life on Earth is the ability of agents to exert causal power and be drivers of subsequent events. This is key to cognition at all scales. Causal emergence, measuring the degree to which an agent exerts unique predictive power on its future, is one consequence of causal power. Indeed, recent discoveries have shown that biological agents, even minimal ones, increase their causal emergence after learning new memories. However, there is a major knowledge gap regarding how causally emer...

---

### 28. CoupleEvo: Evolving Heuristics for Coupled Optimization Problems Using Large Language Models

**Authors:** Thomas Bömer, Bastian Amberg, Max Disselnmeyer, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06341v1)

**Summary:** Many real-world optimization problems consist of multiple tightly coupled subproblems whose solutions must be coordinated to achieve high overall performance. However, existing large language model driven automated heuristic design approaches are limited to single-problem settings. In this paper, we propose CoupleEvo. CoupleEvo proposes three evolutionary coordination strategies to evolve heuristics for coupled optimization problems: the sequential strategy evolves heuristics for one subproblem ...

---

### 29. Efficient event-driven retrieval in high-capacity kernel Hopfield networks

**Authors:** Akira Tamamori

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05978v2) | 📄 [PDF](https://arxiv.org/pdf/2605.05978v2)

**Summary:** High-capacity associative memory models, such as Kernel Logistic Regression (KLR) Hopfield networks, have demonstrated strong storage capabilities but typically rely on computationally expensive synchronous updates. This reliance poses a bottleneck for deployment on energy-efficient, event-driven neuromorphic hardware. In this paper, we investigate the asynchronous retrieval dynamics of KLR Hopfield networks. We show empirically that, under appropriately tuned kernel parameters, asynchronous seq...

---

### 30. MDN: Parallelizing Stepwise Momentum for Delta Linear Attention

**Authors:** Yulong Huang, Xiang Liu, Hongxiang Huang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05838v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05838v1)

**Summary:** Linear Attention (LA) offers a promising paradigm for scaling large language models (LLMs) to long sequences by avoiding the quadratic complexity of self-attention. Recent LA models such as Mamba2 and GDN interpret linear recurrences as closed-form online stochastic gradient descent (SGD), but naive SGD updates suffer from rapid information decay and suboptimal convergence in optimization. While momentum-based optimizers provide a natural remedy, they pose challenges in simultaneously achieving ...

---

### 31. Graph Normalization: Fast Binarizing Dynamics for Differentiable MWIS

**Authors:** Laurent Guigues

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05330v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05330v1)

**Summary:** We introduce Graph Normalization (GN), a principled dynamical system on graphs that serves as a differentiable approximation engine for the NP-hard Maximum Weight Independent Set (MWIS) problem. MWIS encompasses many combinatorial challenges, including optimal assignment, scheduling, set packing, and MAP inference in discrete Markov Random Fields. Unlike Belief Propagation, we prove GN always converges to a binary indicator of a Maximum Independent Set. GN realizes a fast quasi-Newton descent th...

---

### 32. S-LCG: Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization

**Authors:** Ahmed Qasim Mohammed, Haider Banka, Anamika Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05198v1)

**Summary:** This study presents a novel deterministic optimization algorithm based on a special variant of the Linear Congruential Generator (LCG). While conventional algorithms generally operate within the search space, the introduced technique follows a two-level architecture. In particular, an external loop that adaptively balances between exploration and exploitation, while the internal loop evaluates solutions. It is motivated by the intrinsic structure of the generator, the reason behind naming it the...

---

### 33. Direct From Darwin: Deriving Advanced Optimizers From Evolutionary First Principles

**Authors:** Daniel Grimmer

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05284v2) | 📄 [PDF](https://arxiv.org/pdf/2605.05284v2)

**Summary:** Evolutionary computation has long promised to deliver both high-performance optimization tools as well as rigorous scientific simulations of Darwinian evolution. However, modern algorithms frequently abandon evolutionary fidelity for physics-inspired heuristics or superficial biological metaphors. This paper derives a suite of advanced gradient-based optimization algorithms directly from evolutionary first principles. We introduce Darwinian Lineage Simulations (DLS) to prove that, in an asexual ...

---

### 34. On the Influence of the Feature Computation Budget on Per-Instance Algorithm Selection for Black-Box Optimization

**Authors:** Koen van der Blom, Diederick Vermetten

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04954v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04954v1)

**Summary:** Per-instance algorithm selection (PIAS) takes advantage of complementarity between a set of algorithms by deciding which algorithm to run on a given instance. This decision is based on features of the instances, which, in the context of black-box optimization (BBO), require a part of the optimization budget to be computed. This raises two questions: (a) from which fraction of the budget spent on feature computation does PIAS become worth it for BBO, and (b) which fraction of the budget optimizes...

---

### 35. DALight-3D: A Lightweight 3D U-Net for Brain Tumor Segmentation from Multi-Modal MRI

**Authors:** Nand Kumar Mishra, Dhruv Mishra, Dr Manu Pratap Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04518v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04518v1)

**Summary:** Automatic brain tumor segmentation from multi-modal MRI remains challenging because volumetric models often incur substantial computational cost. This paper presents DALight-3D, a compact 3D U-Net variant that combines depthwise separable 3D convolutions, identifier-conditioned normalization, cross-slice attention, and adaptive skip fusion. The method is evaluated on the Medical Segmentation Decathlon Task01 BrainTumour benchmark under matched optimization settings against standard 3D U-Net, Att...

---

### 36. Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment

**Authors:** Xin Wang, Zhuangzhi Gao, Hongyi Qin, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04309v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04309v1)

**Summary:** Understanding the neural mechanisms underlying visual computation has long been a central challenge in neuroscience. Recent alignment based approaches have improved the accuracy of decoding visual stimuli from brain activity, yet they provide limited insight into the neural computations that give rise to these improvements. To address this gap, we propose Dual-Tower Image-Neural Alignment (DINA), an interpretable contrastive framework for analyzing population level visual computations in primary...

---

### 37. QUIVER: Cost-Aware Adaptive Preference Querying in Surrogate-Assisted Evolutionary Multi-Objective Optimization

**Authors:** Florian A. D. Burnat

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04267v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04267v1)

**Summary:** Interactive multi-objective optimization systems face a budget allocation dilemma: one can spend resources on expensive objective evaluations or on eliciting decision-maker preferences that identify the relevant region of the Pareto set. Moreover, preference elicitation itself spans modalities with different information content and cognitive burden, ranging from cheap, noisy pairwise preference statements (PS) to richer but costlier indifference adjustments (IA).   We study cost-aware optimizati...

---

### 38. phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks

**Authors:** Stefan Fischer, Maliheh Hariri, Sebastian Otte

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04256v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04256v1)

**Summary:** Physical neural networks (PNNs) embed computation directly in material dynamics, including molecular, chemical, biological, photonic, memristive, and mechanical substrates. They are attractive for edge computing, especially at the extreme edge, where computation can be placed at the interface to sensing, actuation, or the physical process itself. However, PNNs are difficult to integrate into edge-cloud software stacks because each substrate exposes distinct interfaces, timing behavior, observabi...

---

### 39. Exact and Evolutionary Algorithms for Sequential Multi-Objective Transmission Topology Planning

**Authors:** Job Groeneveld, Miguel Muñoz, Jan Viebahn, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03753v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03753v1)

**Summary:** We address day-ahead transmission topology planning and congestion management as a sequential, multi-objective optimization problem and develop two complementary algorithms for it: an exact enumeration method and a tailored evolutionary heuristic. The problem is formulated with four operational objectives reflecting real TSO decision criteria: worst-case line loading under $N-1$ security, topological depth, number of switching actions, and time spent in non-reference topologies, over a 24-hour h...

---

### 40. Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks

**Authors:** Jatin Sharma, Dan F. M Goodman, Danyal Akarca

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03598v2) | 📄 [PDF](https://arxiv.org/pdf/2605.03598v2)

**Summary:** Understanding how biological and artificial neural networks implement computation from connectivity is a central problem in neuroscience and machine learning. In neural systems, structural and functional connectivity are known to diverge, motivating approaches that move beyond direct connections alone. Here, we show that the spatial and temporal function of recurrent neural networks (RNNs) trained on hierarchically modular tasks can be recovered by modelling the network as a graph and analysing ...

---

### 41. Physics-Modeled Neural Networks

**Authors:** Raul Felipe-Sosa, Angel Martin del Rey, Maria Flores Ceballos

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.08176v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08176v1)

**Summary:** We introduce \emph{Dynamical Physics-Modeled Neural Networks} (DynPMNNs), a continuous-time deep learning architecture in which each hidden layer is defined as the solution of an ordinary differential equation. Unlike classical feed-forward networks, this approach replaces static activation functions with time-evolving dynamical systems, providing a biologically inspired interpretation of hidden-layer behavior and enabling the integration of physically meaningful models. The framework is rigorou...

---

### 42. Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks

**Authors:** Hanson Hanxuan Mo

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03338v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03338v1)

**Summary:** Recurrent networks that store position, phase, or other continuous variables need state-space directions that remain neutral over long horizons. We give a symmetry-based account of when such neutral directions are guaranteed rather than merely tuned. For a finite-dimensional autonomous \(C^1\) vector field equivariant under a Lie group \(G\), we prove that any compact invariant set carrying a uniformly nondegenerate group-orbit bundle with stabilizer type \(H\) has, at points where the Lyapunov ...

---

### 43. Neuromorphic Control for 3D Navigation in Minecraft Using Genetic Algorithms

**Authors:** Eric Zipor

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02628v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02628v1)

**Summary:** The popular 2009 voxel based videogame, Minecraft, contains several distinct disciplines. One of which is "parkour," gameplay that focuses on traversing a world's environment with maximum efficiency. The Minecraft online community has turned the game's physics engine into dynamic puzzles, requiring players to masterfully manipulate motion mechanics through frame precise timing of keystrokes. Actions such as sprinting, sneaking, and mouse direction are all combined to clear specific difficult jum...

---

### 44. MPCS: Neuroplastic Continual Learning via Multi-Component Plasticity and Topology-Aware EWC

**Authors:** Joern Hentsch

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02509v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02509v1)

**Summary:** Continual learning systems face a fundamental tension between plasticity -- acquiring new knowledge  --  and stability  --  retaining prior knowledge. We introduce MPCS (Multi-Plasticity Continual System), a neuroplastic architecture that integrates eleven complementary mechanisms: task-driven neurogenesis, Fourier-encoded inputs, EWC regularization, meta-replay, mixed consolidation, hybrid gating, synapse pruning/regeneration, Hebbian updates, task similarity routing, adaptive growth control, a...

---

### 45. Combining Trained Models in Reinforcement Learning

**Authors:** Ujjwal Patil, Javad Ghofrani

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02159v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02159v1)

**Summary:** Deep reinforcement learning (DRL) has delivered strong results in domains such as Atari and Go, but it still suffers from high sample cost and weak transfer beyond the training setting. A common response is to reuse information from previously trained models through transfer, distillation, ensemble methods, or federated training instead of learning each target task from random initialization. The literature on these mechanisms is fragmented, and published comparisons are hard to interpret becaus...

---

### 46. HERCULES: Hardware-Efficient, Robust, Continual Learning Neural Architecture Search

**Authors:** Matteo Gambella, Fabrizio Pittorino, Manuel Roveri

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.04103v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04103v1)

**Summary:** Neural Architecture Search (NAS) has emerged as a powerful framework for automatically discovering neural architectures that balance accuracy and efficiency. However, as AI transitions from static benchmarks to real-world deployment, the traditional focus on hardware-aware efficiency is no longer sufficient. We observe that modern NAS methods, especially those that target edge AI, are evolving to address a triple objective: Efficiency, Robustness, and Continual Learning. While efficiency ensures...

---

### 47. SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors

**Authors:** Yahan Yang, Pradeep Kumar Gopalakrishnan, Chang Chip Hong, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01937v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01937v1)

**Summary:** Dynamic Vision Sensors (DVS) exhibit exceptional dynamic range and low power consumption, making them ideal for edge applications in the Internet of Video Things (IoVT). However, their output is often degraded by spurious Background Activity (BA) noise, leading to unnecessary computational overhead. This paper proposes SNNF, a near-sensor BA noise filter that integrates a compact Event-Based Binary Image (EBBI) representation, a parallel memory architecture, and a single-layer Spiking Neural Net...

---

### 48. Training Non-Differentiable Networks via Optimal Transport

**Authors:** An T. Le

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01928v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01928v1)

**Summary:** Neural networks increasingly embed non-differentiable components (spiking neurons, quantized layers, discrete routing, blackbox simulators, etc.) where backpropagation is inapplicable and surrogate gradients introduce bias. We present PolyStep, a gradient-free optimizer that updates parameters using only forward passes. Each step evaluates the loss at structured polytope vertices in a compressed subspace, computes softmax-weighted assignments over the resulting cost matrix, and displaces particl...

---

### 49. ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization

**Authors:** Kaiwen Tang, Di Yu, Jiaqi Zheng, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01866v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01866v1)

**Summary:** Spiking neural networks (SNNs) are promising for edge sensing due to their event-driven computation and temporal filtering capability. However, standard leaky integrate-and-fire (LIF) neurons communicate only through binary spikes, which severely limit representational capacity. Existing multi-level spiking neurons improve information transmission, but often rely on uniform quantization that mismatches membrane-potential distributions or introduces costly synaptic multiplications. In this paper,...

---

### 50. Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance

**Authors:** Anamika Paul Rupa, Anietie Andy

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01699v3) | 📄 [PDF](https://arxiv.org/pdf/2605.01699v3)

**Summary:** Recent attacks show that behavioural unlearning of large language models leaves internal traces recoverable by adversarial probes. We characterise where this retention lives and show it can be surgically removed without measurable capability cost. Our central protocol is a leave-one-out cross-sequence probe that tests whether a memorisation signature generalises across held-out sequences. The signature is real and consistent across scale: memorisation-specific gaps of +0.32, +0.19, +0.30 on Pyth...

---

## q-bio.NC

**50 papers**

### 1. On periodic distributed representations using Fourier embeddings

**Authors:** Jakeb Chouinard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10818v1)

**Summary:** Periodic signals are critical for representing physical and perceptual phenomena. Scalar, real angular measures, e.g., radians and degrees, result in difficulty processing and distinguishing nearby angles, especially when their absolute difference exceeds pi. We can avoid this problem by using real-valued, periodic embeddings in high-dimensional space. These representations also allow us to control the nature of their dot product similarities, allowing us to construct a variety of different kern...

---

### 2. Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning

**Authors:** Alexandra Voce, Emmanouil Giannakakis, Claudia Clopath

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10356v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10356v1)

**Summary:** The cerebellum and cerebral cortex form tightly coupled circuits thought to support flexible and efficient temporal processing. How this interaction shapes cortical learning dynamics, and whether such heterogeneous modularity can benefit artificial systems, remains unclear. Here, we augment a recurrent neural network (RNN) with a cerebellar-inspired feedforward module and evaluate the resulting architecture on temporal tasks of varying difficulty. The cortico-cerebellar RNN (CB-RNN) learns faste...

---

### 3. Positive Alignment: Artificial Intelligence for Human Flourishing

**Authors:** Ruben Laukkonen, Seb Krier, Chloé Bakalar, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10310v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10310v1)

**Summary:** Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and n...

---

### 4. Joint sparse coding and temporal dynamics support context reconfiguration

**Authors:** Qianqian Shi, Yue Che, Faqiang Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10178v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10178v1)

**Summary:** Adaptive behavior requires the brain to transition between distinct contexts while maintaining representations of prior experience. The ability to reconfigure neural representations without erasing previously acquired knowledge is central to learning in dynamic environments, yet the neural mechanisms that support this balance remain unclear. Understanding these mechanisms is also critical for addressing catastrophic forgetting in artificial systems designed for lifelong learning. Here, we identi...

---

### 5. Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09770v1)

**Summary:** Spike-based encodings are sparse and energy-efficient, but have largely been formulated probabilistically, disconnected from most signal processing literature. We recast spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. The proposed wavelets preserve the sparsity and locality of spiking representations, with reconstruction up to spike quantization and time discretization. We demonstrate reconstruction on ECG and audio datasets, achieving a...

---

### 6. Predictive and feedback signals differently shape the formation of group-level and individualized language representations

**Authors:** Shuguang Yang, Shaoyun Yu, Xin Jiang, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09409v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09409v1)

**Summary:** Adults vary greatly in how effectively they learn a new language, but the signals driving the learning processes and individual differences remain unclear. Over seven days, we tracked behavioral learning and collected fMRI data from 102 adults as they learned an artificial language with corrective feedback. We trained matched transformer models with prediction, feedback, or combined objectives and compared their internal representations to brain activity. Representations derived from the predict...

---

### 7. How Much is Brain Data Worth for Machine Learning?

**Authors:** Lane Lewis, Zhixin Wang, David Schwab, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09243v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09243v1)

**Summary:** If a person can solve a task, can measuring their brain make it easier to train a model to solve that task too? Recent NeuroAI work suggests that supplementing task training with neural recordings can modestly improve model performance and robustness. However, it is unclear when there should be a benefit from using neural data and how much benefit to expect. We formulate this question mathematically, and begin to address it theoretically using a simple, analytically tractable linear gaussian mod...

---

### 8. Meow-Omni 1: A Multimodal Large Language Model for Feline Ethology

**Authors:** Jucheng Hu, Zhangquan Chen, Yulin Chen, et al.

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.09152v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09152v1)

**Summary:** Deciphering animal intent is a fundamental challenge in computational ethology, largely because of semantic aliasing, the phenomenon where identical external signals (e.g., a cat's purr) correspond to radically different internal states depending on physiological context. Existing Multimodal Large Language Models (MLLMs) are blind to high-frequency biological time-series data, restricting them to superficial behavioural pattern matching rather than genuine latent-state reasoning. To bridge this ...

---

### 9. Automated Optical Density Normalization for Myelin Quantification: Cross-Modal Validation with 7T Ex Vivo MRI

**Authors:** Zahra Khodakarami, Sheina Emrani, Pulkit Khandelwal, et al.

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08711v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08711v1)

**Summary:** White matter hyperintensities (WMH) are bright regions on T2-weighted magnetic resonance imaging (MRI) scans and are associated with cerebrovascular pathology and neurodegeneration, including myelin loss. While Luxol Fast Blue histopathology provides visualization of myelin integrity, quantitative analysis requires measuring Optical Density as a proxy for myelin concentration. However, differences in laboratory protocols and tissue processing introduce staining variability that acts as systemati...

---

### 10. FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts

**Authors:** Josue Ortega Caro, Yongxu Zhang, Hannah M Batchelor, et al.

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08648v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08648v1)

**Summary:** Many biological systems evolve through continuous local dynamics while switching between latent regimes defined by learning, stimulus context, internal state, or developmental stage. These processes are often observed only as unpaired longitudinal snapshots: the same cells, neurons, or animals are not tracked as matched trajectories, even though population states are sampled across successive stages. This creates two coupled challenges. First, trajectories must respect curved low-dimensional man...

---

### 11. NeuralBench: A Unifying Framework to Benchmark NeuroAI Models

**Authors:** Hubert Banville, Stéphane d'Ascoli, Simon Dahan, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08495v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08495v1)

**Summary:** Deep learning and large public datasets have recently catalyzed the proliferation of AI models for processing brain recordings. However, systematically evaluating these models remains a challenge: not only do the preprocessing pipelines, training and finetuning approaches largely vary across studies, but their downstream evaluation is often limited to small sets of tasks and/or datasets. Here, we present NeuralBench: a unified framework for benchmarking AI models of brain activity. We accompany ...

---

### 12. Neurally-plausible radial basis kernels using distributed Fourier embeddings

**Authors:** Jakeb Chouinard

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08458v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08458v1)

**Summary:** Coherent, continuous spatial representations are critical for synthesizing physical and perceptual phenomena into a single representational space. Radial basis kernels provide a path forward for this type of distributed representation. In this work, we aim to characterize and analyze common radial basis kernels realizable in the neurally-plausible framework of spatial semantic pointers. Further, we analyze previous radial basis kernel work based on grid cell-like representations and demonstrate ...

---

### 13. Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners

**Authors:** Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08019v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08019v1)

**Summary:** Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match hu...

---

### 14. Dynamical mechanisms of flexible phase-locking in cortical theta oscillators

**Authors:** Yangyang Wang, Benjamin R. Pittman-Polletta

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08014v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08014v1)

**Summary:** Oscillatory activity in auditory cortex is thought to play a central role in auditory and speech processing by synchronizing neural rhythms to external acoustic features of the speech stream. To support this function, cortical oscillators must flexibly phase-lock to inputs spanning a wide range of timescales, including rhythms substantially slower than their intrinsic frequency. Here we identify a general dynamical mechanism by which intrinsic inhibitory currents operating on multiple timescales...

---

### 15. Learning Cross-Atlas Consistent Brain Disorder Representations via Disentangled Multi-Atlas Functional Connectivity Learning

**Authors:** Minheng Chen, Chao Cao, Jing Zhang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.07026v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07026v1)

**Summary:** Functional connectivity (FC) derived from resting-state fMRI is widely used to characterize large-scale brain network alterations in neurological and psychiatric disorders. However, FC construction critically depends on the choice of brain atlas, and different parcellations may emphasize distinct organizational features, leading to heterogeneous and sometimes inconsistent representations. Existing multi-atlas approaches partially alleviate this issue but often fuse atlas-derived features or pred...

---

### 16. Partitioning Neural Co-Variability

**Authors:** Skyler Thomas, Brandon J. Zhu, Kathleen E. Cullen, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06995v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06995v1)

**Summary:** Trial-to-trial variability of neural responses has been linked to important aspects of neural computation and is essential for understanding how neuronal populations respond. While current overdispersion models treat each neuron's gain as independent of each other, this assumption fails to capture the network statistics of neuronal populations. As no existing model can capture overdispersed structured spiking gain-modulation across a neural population, network-level gain covariance remains large...

---

### 17. Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?

**Authors:** Yukiyasu Kamitani

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06420v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06420v1)

**Summary:** Brain-DNN alignment is usually assessed through stimulus-level correspondence or stimulus-set geometry. Inspired by category theory, we operationalize a different question: do brain and model preserve the same candidate transformations among stimuli? We formalize this as approximate naturality: if a proxy-defined stimulus change is propagated through the brain side and then translated to the model side, the result should match translating first and then propagating, so that the naturality square...

---

### 18. A multi-scale information geometry reveals the structure of mutual information in neural populations

**Authors:** Simone Azeglio, Steeve Laquitaine, Ulisse Ferrari, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06304v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06304v1)

**Summary:** Understanding how neural population responses represent sensory information is a central problem in systems neuroscience. One approach is to define a representational geometry on stimulus space in which distances reflect how reliably stimuli can be distinguished from neural activity. However, different constructions of these distances can lead to qualitatively different conclusions about the neural code. Here, we show that a unique Riemannian representational geometry emerges from first principl...

---

### 19. Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience

**Authors:** Johannes Bertram, Luciano Dyballa, T. Anderson Keller, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05907v1)

**Summary:** Decoding approaches are widely used in neuroscience and machine learning to compare stimulus representations across neural systems, such as different brain regions, organisms, and deep learning models. Popular methods include decoding (perceptual) manifolds and alignment metrics such as Representational Similarity Analysis (RSA) and Dynamic Similarity Analysis (DSA), where similarity in decoding representations is interpreted as evidence for similar computation. This paper demonstrates a fundame...

---

### 20. Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior

**Authors:** Hanbo Xie, Akshay K. Jagadish, Lan Pan, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05091v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05091v1)

**Summary:** Computational cognitive models discovered using large language models have so far relied solely on behavioral data. However, it is well-known that models produced from the behavioral trajectory alone are typically under-determined. In this work, we explore the use of Think Aloud traces as an additional form of data constraint during automated model discovery. When applied to the domain of risky decision-making, we find that the models discovered with think-aloud achieve significantly improved pr...

---

### 21. A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions

**Authors:** Alessio Basti, Rikkert Hindriks, Ruggero Freddi, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04636v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04636v1)

**Summary:** Cross-frequency interactions are fundamental brain mechanisms for integrating information across temporal scales. However, accurate identification of these couplings is hindered by complex multi-frequency nonlinearities and by spurious, zero-lag artifacts caused by volume conduction. To our knowledge, conventional metrics lack a robust framework to characterize genuine interactions among multiple time series where a frequency of interest $f_N$ arises from the combination of $N-1$ components such...

---

### 22. Dissociating spatial frequency reliance from adversarial robustness advantages in neurally guided deep convolutional neural networks

**Authors:** Zhenan Shao, Tianyu Ren, Chengxiao Wang, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04443v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04443v1)

**Summary:** Deep convolutional neural networks (DCNNs) have rivaled humans on many visual tasks, yet they remain vulnerable to near-imperceptible perturbations generated by adversarial attacks. Recent work shows that aligning DCNN representations with human visual cortex activity improves adversarial robustness, but the mechanisms driving this advantage are unclear. One hypothesis suggests that neural alignment confers robustness by biasing models away from brittle high-frequency details and towards the low...

---

### 23. A foundation model of vision, audition, and language for in-silico neuroscience

**Authors:** Stéphane d'Ascoli, Jérémy Rapin, Yohann Benchetrit, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04326v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04326v1)

**Summary:** Cognitive neuroscience is fragmented into specialized models, each tailored to specific experimental paradigms, hence preventing a unified model of cognition in the human brain. Here, we introduce TRIBE v2, a tri-modal (video, audio and language) foundation model capable of predicting human brain activity in a variety of naturalistic and experimental conditions. Leveraging a unified dataset of over 1,000 hours of fMRI across 720 subjects, we demonstrate that our model accurately predicts high-re...

---

### 24. Neural Manifolds as Crystallized Embeddings: A Synthesis of the Free Energy Principle, Generalized Synchronization, and Hebbian Plasticity

**Authors:** Vikas N. O'Reilly-Shah

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04200v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04200v1)

**Summary:** The free energy principle casts perception as variational inference, but its biological implementation remains underspecified. In particular, the generalized-coordinate formalism should not be read as a literal claim that neurons compute arbitrary Taylor expansions. This paper argues that generalized synchronization provides the missing bottom-up mechanism. A contractive recurrent circuit driven by structured sensory input can synchronize to the driving dynamics. Under generic embedding conditio...

---

### 25. Cusped singularities organize mixed-mode oscillations in mutually inhibitory slow-fast systems

**Authors:** Morten Gram Pedersen

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03606v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03606v1)

**Summary:** Mutual inhibition is a common motif in neural systems. Here, we establish that cusped singularities - folded singularities located at cusp points of critical manifolds - provide a universal organizing mechanism for mixed-mode oscillations (MMOs) in coupled slow-fast systems with mutual inhibition. We show that the geometric setup of these systems generically satisfies the conditions required by established geometric singular perturbation theory and blow-up methods, guaranteeing that such cusped ...

---

### 26. Learning reveals invisible structure in low-rank RNNs

**Authors:** Yoav Ger, Omri Barak

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04115v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04115v1)

**Summary:** Learning in neural systems arises from synaptic changes that reshape the representations underlying behavior. While low-rank recurrent neural networks (RNNs) have emerged as a powerful framework for linking connectivity to function, a theoretical understanding of their learning process remains elusive. Here, we extend the low-rank framework from activity to learning by deriving gradient-descent dynamics directly in a reduced overlap space. We formulate a closed-form, low-dimensional system of OD...

---

### 27. NeuralSet: A High-Performing Python Package for Neuro-AI

**Authors:** Jean-Rémi King, Corentin Bel, Linnea Evanson, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.03169v2) | 📄 [PDF](https://arxiv.org/pdf/2605.03169v2)

**Summary:** Artificial intelligence (AI) is increasingly central to understanding how the brain processes information. However, the integration of neuroscience and modern AI is bottlenecked by a fragmented software ecosystem. Current tools are siloed by recording modality and optimized for small-scale, in-memory workflows, limiting the use of massive, naturalistic datasets. Here, we introduce NeuralSet, a Python framework that efficiently unifies the processing of diverse neural recordings (including fMRI, ...

---

### 28. Inferring Active Neural Circuits Using Diffusion Scores

**Authors:** Savik Kinger, Johannes Bertram, Luciano Dyballa, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02852v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02852v1)

**Summary:** In biological systems, neural circuits compute through directed, short-latency interactions whose effects unfold across multiple time scales and behavioral contexts. We address the problem of inferring these local, lag-specific interactions from sampled neural population activity under varying stimuli, without assuming a parametric form for the underlying dynamics. Our approach leverages denoising score models by estimating joint-window scores over consecutive activity snapshots (i.e., brain sta...

---

### 29. Online Generalised Predictive Coding

**Authors:** Mehran H. Z. Bazargani, Szymon Urbas, Adeel Razi, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02675v1)

**Summary:** This paper introduces an extension of generalised filtering for online applications. Generalised filtering refers to data assimilation schemes that jointly infer latent states, learn unknown model parameters, and estimate uncertainty in an integrated framework -- e.g., estimate state and observation noise -- at the same time (i.e., triple estimation). This framework appears across disciplines under different names, including variational Kalman-Bucy filtering in engineering, generalised predictiv...

---

### 30. Modeling sequential cognitive states via population level cortical dynamics

**Authors:** M Virginia Bolelli, Luca Greco, Dario Prandi

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02365v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02365v1)

**Summary:** In this work, we present a mathematical model for cyclic and sequential patterns of brain activity, combining heteroclinic dynamics with discrete neural-field models. We first show that spatial-discrete neural-field equations with biologically realistic equilibria cannot support heteroclinic cycles. On the other hand, heterocline dynamics often arise in Lotka-Volterra-type systems, but these equations do not directly correspond to neuronal processes. To address this, we use a version of the Univ...

---

### 31. Electroencephalography and Electromyography as a Non-Invasive Biomarker of Neural Regeneration: A Review of Central and Peripheral Nervous System Injury and Regeneration

**Authors:** Maryam Kheyrollah, Reza Khanbabaie, Chris Ullrich, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01767v1)

**Summary:** Regeneration of the nervous system after injury remains an important therapeutic objective, especially in the central nervous system (CNS), in which regeneration is restricted by both neuronal limitations as well as adverse extracellular environments. Conversely, the peripheral nervous system (PNS) displays enhanced regenerative capability in the presence of supportive Schwann cells (SC) and pro-growth stimuli. While the structure and molecular mechanisms are thoroughly understood, functional bi...

---

### 32. From Cortical Synchronous Rhythm to Brain Inspired Learning Mechanism: An Oscillatory Spiking Neural Network with Time-Delayed Coordination

**Authors:** Tingting Dan, Guorong Wu

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01656v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01656v1)

**Summary:** Human cognition emerges from coordinated spiking dynamics in distributed neural circuits, where information is encoded via both firing rates and precise spike timing determined by brain rhythms. Inspired by this notion, we propose a brain-inspired learning primitive in which cognition-level neural synchrony emerges through iterative bottom-up and top-down interactions between micro-scale dynamics of spiking neurons and a macro-scale mechanism of oscillatory synchronization. Specifically, we mode...

---

### 33. Measuring Understanding Through Discrete Compositional Knowledge Structures in Hierarchical Automata

**Authors:** Igor Balaz

**Published:** 2026-05-02

🔗 [Paper](http://arxiv.org/abs/2605.01430v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01430v1)

**Summary:** How do we measure genuine understanding in artificial cognitive systems? Current approaches face a measurement gap: probabilistic systems refine confidence gradually, practice-based systems compile knowledge through repeated execution, and neural systems distribute understanding across opaque embedding spaces. We propose that making understanding measurable requires architectures where understanding formation produces discrete, inspectable structural signatures. This paper presents hierarchical ...

---

### 34. Observable Performance Does Not Fully Reflect System Organization: A Multi-Level Analysis of Gait Dynamics Under Occlusal Constraint

**Authors:** Jacques Raynal, Pierre Slangen, Jacques Margerit

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00778v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00778v1)

**Summary:** In biomechanical systems, observable performance is often used as a proxy for underlying system organization. However, this assumption implicitly presumes a correspondence between output metrics and internal system states that may not hold in adaptive systems. In this study, the vertical dimension of occlusion (VDO) is considered as a constraint applied to an adaptive neuromechanical system, enabling the exploration of system-level responses under controlled variations. A single-case design in a...

---

### 35. Functional Connectivity-Guided Band Selection for Motor Imagery Brain-Computer Interfaces

**Authors:** Natália Araújo do Carmo, Aarthy Nagarajan

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00746v1)

**Summary:** Reliable control in motor imagery brain-computer interfaces (MI-BCIs) requires the precise decoding of user-specific neural rhythms, which vary significantly across individuals. The Common Spatial Pattern (CSP) algorithm is a cornerstone of MI-BCI decoding, yet its performance depends strongly on the spectral range of the input EEG data. Although Filter Bank CSP (FBCSP) extends this as a data-driven decoding framework, its frequency sub-bands are predefined rather than selected using subject-spe...

---

### 36. Robust volatility updates for Hierarchical Gaussian Filtering

**Authors:** Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade, et al.

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00966v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00966v1)

**Summary:** Hierarchical Gaussian Filtering (HGF) networks allow for efficient updating of posterior distributions (beliefs) about hidden states of an agent's environment. HGF parent nodes can target the mean or variance of their children. New information entering at input nodes leads to a cascade of belief updates across the network according to one-step update equations for each node's mean and precision (inverse variance). However, the original form of the update equations for variance-targeting parents(...

---

### 37. Intrinsic Brain Networks Underlying the Experience and Expression of Subclinical Anxiety

**Authors:** Shruti Kinger, Mrinmoy Chakrabarty

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00465v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00465v1)

**Summary:** Anxiety includes behavioural, physiological, and subjective components that do not always align, and it remains unclear whether these dimensions are supported by distinct intrinsic brain networks. Guided by the two-system framework, we tested whether resting-state functional connectivity (rsFC) differentiates these components in subclinical anxiety. Forty-seven young adults spanning a range of subclinical anxiety levels completed a threat anticipation task measuring behavioral responses (reactio...

---

### 38. SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding

**Authors:** YuSheng Lin, Ji-Hwa Tsai, Chun-Shu Wei

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00401v1)

**Summary:** Recent EEG-to-image retrieval methods leverage pretrained vision encoders and foveation-inspired priors, but typically assume a fixed, center-focused view. This center bias conflicts with content-driven human attention, creating a geometric-semantic dissociation between visual features and EEG responses. We propose SIMON, a saliency-aware multi-view framework for zero-shot EEG-to-image retrieval. SIMON combines foreground segmentation and saliency prediction to select fixation centers via Salien...

---

### 39. CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness

**Authors:** Haofei Yu, Yining Zhao, Lenore Blum, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2605.04097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04097v1)

**Summary:** Despite remarkable advances, today's AI systems remain narrow in scope, falling short of the flexible, adaptive, and multisensory intelligence that characterizes human capabilities. This gap has fueled longstanding debates about whether AI might one day achieve human-like generality or even consciousness, and whether theories of consciousness can inspire new architectures for AI. This paper presents an early blueprint for implementing a general AI system, CTM-AI, combining the Conscious Turing M...

---

### 40. Multisensory learning recruits visual neurons into an olfactory memory engram

**Authors:** Zeynep Okray, Nils Otto, Anna A. Cook, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.28007v1) | 📄 [PDF](https://arxiv.org/pdf/2604.28007v1)

**Summary:** Associating multiple sensory cues with a single experience or object is a fundamental process that improves object recognition and memory performance. However, neural mechanisms that bind sensory features during learning and augment memory expression are unknown. Here we demonstrate multisensory appetitive and aversive memory in Drosophila. Combining colours and odours improved memory performance, even when each sensory modality was tested alone. Temporal control of neuronal function revealed vi...

---

### 41. On Agentic Behavioral Modeling

**Authors:** Dirk Ostwald, Rasmus Bruckner, Franziska Usée, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27894v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27894v1)

**Summary:** Integrating theoretical neuroscience, decision theory, and probabilistic inference offers a promising route to understanding human cognition, yet concrete methodological bridges between agentic AI models and behavioral data analysis remain formally underdeveloped. We advance this synthesis under the framework of agentic behavioral modeling (ABM), which treats artificial agents as latent, generative hypotheses about cognitive mechanisms and evaluates them by their statistical adequacy in explaini...

---

### 42. Simulating Infant First-Person Sensorimotor Experience via Motion Retargeting from Babies to Humanoids

**Authors:** Francisco M. López, Hoshinori Kanazawa, Ondrej Fiala, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27583v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27583v1)

**Summary:** Motion retargeting from humans to human-like artificial agents is becoming increasingly important as humanoid robots grow more capable. However, most existing approaches focus only on reproducing kinematics and ignore the rich sensorimotor experience associated with human movement. In this work, we present a framework for simulating the multimodal sensorimotor experiences of infants using physical and virtual humanoids. From a single video, our method reconstructs the infant's body configuration...

---

### 43. A geometry aware framework enhances noninvasive mapping of whole human brain dynamics

**Authors:** Song Wang, Kexin Lou, Chen Wei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25592v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25592v1)

**Summary:** Non-invasive electrophysiology lacks methods that accurately reconstruct whole-brain spatiotemporal dynamics while incorporating individual cortical geometry, leaving current electroencephalography and magnetoencephalography source imaging limited by simplistic or biologically implausible priors. Here, we show that embedding participant-specific Geometric Basis Functions (GBFs), eigenmodes derived from each individual's cortical surface, provides a powerful anatomic constraint that resolves the ...

---

### 44. One-shot emergency psychiatric triage across 15 frontier AI chatbots

**Authors:** Veith Weilnhammer, Lennart Luettgau, Christopher Summerfield, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25415v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25415v1)

**Summary:** AI chatbots are increasingly used for health advice, but their performance in psychiatric triage remains undercharacterized. Psychiatric triage is particularly challenging because urgency must often be inferred from thoughts, behavior, and context rather than from objective findings.   We evaluated the performance of 15 frontier AI chatbots on psychiatric triage from realistic single-message disclosures using 112 clinical vignettes, each paired with 1 of 4 original benchmark triage labels: A, ro...

---

### 45. Independent-Component-Based Encoding Models of Brain Activity During Story Comprehension

**Authors:** Kamya Hari, Taha Binhuraib, Jin Li, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24942v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24942v1)

**Summary:** Encoding models provide a powerful framework for linking continuous stimulus features to neural activity; however, traditional voxelwise approaches are limited by measurement noise, inter-subject variability, and redundancy arising from spatially correlated voxels encoding overlapping neural signals. Here, we propose an independent component (IC)-based encoding framework that dissociates stimulus-driven and noise-driven signals in fMRI data. We decompose continuous fMRI data from naturalistic st...

---

### 46. Homology-based Morphometry of Brain Atrophy: Methods and Applications

**Authors:** Donato Quiccione, Mariam Pirashvili, Nathan Broomhead, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24714v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24714v1)

**Summary:** Understanding the structure of the brain, and how it changes with time and disease, is a core goal of structural neuroimaging. Contemporary approaches to structural brain analysis are dominated by voxel-wise, mass-univariate methods such as voxel-based morphometry (VBM). However, these techniques require images to be normalized to a standard template, which can obscure subject-specific geometric features. Normalization to a common stereotactic space can also be problematic when comparing groups ...

---

### 47. Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks

**Authors:** Kevin McKee, Thomas Hazy, Yicong Zheng, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24637v2) | 📄 [PDF](https://arxiv.org/pdf/2604.24637v2)

**Summary:** Block-sequential continual learning demands that a single model both protect prior solutions from catastrophic forgetting and efficiently infer at inference time which prior solution matches the current input without task labels. We present Functional Task Networks (FTN), a parameter-isolation method inspired by structural and dynamical motifs found in the mammalian neocortex. Similar to mixture-of-experts, this method uses a high dimensional, self-organizing binary mask over a large population ...

---

### 48. The Genetic and Environmental Architecture of the Human Functional Connectome

**Authors:** Tanu Raghav, Daniel Guerrero, Uttara Tipnis, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24614v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24614v1)

**Summary:** Functional connectivity varies across individuals due to genetic and environmental factors, yet classical twin models typically confound non-shared environment with measurement error and are largely limited to resting-state analyses. We hypothesized that: i) explicitly modeling measurement error from repeated fMRI sessions enables more accurate application of classical twin models (ACE/ADE) to functional connectivity; ii) model applicability depends on scan-length and parcellation granularity; i...

---

### 49. Sure About That Line? Approaching Confidence-Based, Real-Time Line Assignment in Reading Gaze Data

**Authors:** Franziska Kaltenberger, Wei-Ling Chen, Enkeleda Thaqi, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2605.00033v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00033v1)

**Summary:** Remote and webcam-based eye tracking in multi-line reading suffers from various noise factors and layout ambiguity, precisely where real-time reading support needs reliable, per-fixation line assignment. Prior work largely addresses this challenge post hoc or by restricting behavior (e.g., disallowing re-reading), undermining interactive use. We propose CONF-LA (Confidence-score-based Online Fixation-to-Line Assignment), a principled, low-latency approach that integrates knowledge about reading ...

---

### 50. Persistent and anti-persistent stride-to-stride fluctuations: an ARFIMA decomposition consistent with closed-loop sensorimotor control

**Authors:** Philippe Terrier

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24365v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24365v1)

**Summary:** Stride-to-stride fluctuations in human walking carry a fractal correlation structure that reverses sign under external cueing: self-paced gait is persistent, whereas metronomic or visually cued gait is anti-persistent. Three decades of detrended fluctuation analysis (DFA) have established this reversal as a scaling-exponent shift, but DFA cannot distinguish genuine long-memory dynamics from short-memory autoregressive moving-average (ARMA) processes that produce the same apparent exponent. We fi...

---

## stat.ML

**50 papers**

### 1. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10934v1)

**Summary:** Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are eff...

---

### 2. Revisiting Policy Gradients for Restricted Policy Classes: Escaping Myopic Local Optima with $k$-step Policy Gradients

**Authors:** Alex DeWeese, Guannan Qu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10909v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10909v1)

**Summary:** This work revisits standard policy gradient methods used on restricted policy classes, which are known to get stuck in suboptimal critical points. We identify an important cause for this phenomenon to be that the policy gradient is itself fundamentally myopic, i.e. it only improves the policy based on the one-step $Q$-function. In this work, we propose a generalized $k$-step policy gradient method that couples the randomness within a $k$-step time window and can escape the myopic local optima in...

---

### 3. Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge

**Authors:** Wenbo Zhang, Lijinghua Zhang, Liner Xiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10805v1)

**Summary:** Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational...

---

### 4. Factual recall in linear associative memories: sharp asymptotics and mechanistic insights

**Authors:** Alessio Giorlandino, Sebastian Goldt, Antoine Maillard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10795v1)

**Summary:** Large language models demonstrate remarkable ability in factual recall, yet the fundamental limits of storing and retrieving input--output associations with neural networks remain unclear. We study these limits in a minimal setting: a linear associative memory that maps $p$ input embeddings in $\mathbb{R}^d$ to their corresponding~$d$-dimensional targets via a single layer, requiring each mapped input to be well separated from all other targets. Unlike in supervised classification, this strict s...

---

### 5. When Are Trade-Off Functions Testable from Finite Samples?

**Authors:** Kaining Shi, Qiaosen Wang, Cong Ma

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10774v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10774v1)

**Summary:** We study finite-sample inference for the trade-off function of two unknown probability distributions, the function that traces the optimal type I/type II error frontier in binary testing. Given samples from distributions $P$ and $Q$, we consider the problem of testing whether their trade-off function lies above a benchmark curve $f_0$ or falls below a weaker benchmark $f_1$. Without structural restrictions, this problem is impossible uniformly over nonparametric classes. We identify a sharp cond...

---

### 6. What should post-training optimize? A test-time scaling law perspective

**Authors:** Muheng Li, Jian Qian, Wenlong Mou

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10716v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10716v1)

**Summary:** Large language models are increasingly deployed with test-time strategies: sample $N$ responses, score them with a reward model or verifier, and return the best. This deployment rule exposes a mismatch in post-training: standard objectives optimize the mean reward of a single response, whereas best-of-$N$ performance is governed by the upper tail of the reward distribution. Recent test-time-aware objectives partly address this mismatch, but typically assume that training can use the same per-pro...

---

### 7. Price of Quality: Sufficient Conditions for Sparse Recovery using Mixed-Quality Data

**Authors:** Youssef Chaabouni, David Gamarnik

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10713v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10713v1)

**Summary:** We study sparse recovery when observations come from mixed-quality sources: a small collection of high-quality measurements with small noise variance and a larger collection of lower-quality measurements with higher variance. For this heterogeneous-noise setting, we establish sample-size conditions for information-theoretic and algorithmic recovery. On the information-theoretic side, we show that it is sufficient for $(n_1, n_2)$ to satisfy a linear trade-off defining the Price of Quality: the n...

---

### 8. Natural Policy Gradient as Doubly Smoothed Policy Iteration: A Bellman-Operator Framework

**Authors:** Phalguni Nanda, Zaiwei Chen

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10671v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10671v1)

**Summary:** In this work, we show that natural policy gradient, a core algorithm in reinforcement learning, admits an exact formulation as a smoothed and averaged form of policy iteration. Specifically, we introduce doubly smoothed policy iteration (DSPI), a Bellman-operator framework in which each policy is obtained by applying a regularized greedy step to a weighted average of past $Q$-functions. DSPI includes policy iteration, dual-averaged policy iteration, natural policy gradient, and more general poli...

---

### 9. When Can Digital Personas Reliably Approximate Human Survey Findings?

**Authors:** Mumin Jia, Yilin Chen, Divya Sharma, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10659v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10659v1)

**Summary:** Digital personas powered by Large Language Models (LLMs) are increasingly proposed as substitutes for human survey respondents, yet it remains unclear when they can reliably approximate human survey findings. We answer this question using the LISS panel, constructing personas from respondents' background variables and pre-2023 survey histories, then testing them against the same respondents' held-out post-cutoff answers. Across four persona architectures, three LLMs, and two prediction tasks, we...

---

### 10. A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables

**Authors:** Zheng Li, Feng Xie, Shenglan Nie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10651v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10651v1)

**Summary:** Constraint-based causal discovery is widely used for learning causal structures, but heavy reliance on conditional independence (CI) testing makes it computationally expensive in high-dimensional settings. To mitigate this limitation, many divide-and-conquer frameworks have been proposed, but most assume causal sufficiency, i.e., no latent variables. In this paper, we show that divide-and-conquer strategies can be theoretically generalized beyond causal sufficiency to settings with latent variab...

---

### 11. Amortizing Causal Sensitivity Analysis via Prior Data-Fitted Networks

**Authors:** Emil Javurek, Dennis Frauen, Marie Brockschmidt, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10590v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10590v1)

**Summary:** Causal sensitivity analysis aims to provide bounds for causal effect estimates in the presence of unobserved confounding. However, existing methods for causal sensitivity analysis are per-instance procedures, meaning that changes to the dataset, causal query, sensitivity level, or treatment require new computation. Here, we instead present an in-context learning approach. Specifically, we propose an amortized approach to causal sensitivity analysis based on prior-data fitted networks. A key chal...

---

### 12. Affine Tracing: A New Paradigm for Probabilistic Linear Solvers

**Authors:** Disha Hegde, Marvin Pförtner, Jon Cockayne

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10566v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10566v1)

**Summary:** Probabilistic linear solvers (PLSs) return probability distributions that quantify uncertainty due to limited computation in the solution of linear systems. The literature has traditionally distinguished between Bayesian PLSs, which condition a prior on information obtained from projections of the linear system, and probabilistic iterative methods (PIMs), which lift classical iterative solvers to probability space. In this work we show this dichotomy to be false: Bayesian PLSs are a special case...

---

### 13. Simultaneous Long-tailed Recognition and Multi-modal Fusion for Highly Imbalanced Multi-modal Data

**Authors:** Heegeon Yoon, Heeyoung Kim

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10498v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10498v1)

**Summary:** Long-tailed distributions in class-imbalanced data present a fundamental challenge for deep learning models, which tend to be biased toward majority classes. While recent methods for long-tailed recognition have mitigated this issue, they are largely restricted to single-modal inputs and cannot fully exploit complementary information from diverse data sources. In this work, we introduce a new framework for long-tailed recognition that explicitly handles multi-modal inputs. Our approach extends m...

---

### 14. A PAC-Bayes Approach for Controlling Unknown Linear Discrete-time Systems

**Authors:** Yujia Luo, Ye Pu, Jonathan H. Manton, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10493v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10493v1)

**Summary:** This paper presents a PAC-Bayes framework for learning controllers for unknown stochastic linear discrete-time systems, where the system parameters are drawn from a fixed but unknown distribution. We derive a data-dependent high probability bound on the performance of any learned (stochastic) controller, and propose novel efficient learning algorithms with theoretical guarantees, which can be implemented for both finite and infinite controller spaces. Compared to prior work, our bound holds for ...

---

### 15. Real vs. Semi-Simulated: Rethinking Evaluation for Treatment Effect Estimation

**Authors:** George Panagopoulos

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10430v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10430v1)

**Summary:** Estimating heterogeneous treatment effects with machine learning has attracted substantial attention in both academic research and industrial practice. However, the two communities often evaluate models under markedly different conditions. Methodological work typically relies on semi-simulated benchmarks and metrics that require counterfactual outcomes, whereas real-world applications rely on observable metrics based on ranking or test outcomes. Despite the well-known gap between methodological ...

---

### 16. Multi-Fidelity Quantile Regression

**Authors:** Yixiang Liu, Yao Zhang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10406v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10406v1)

**Summary:** High-fidelity (HF) data are often expensive to collect and therefore scarce, making conditional quantiles difficult to estimate accurately. We propose a two-stage, model-agnostic method for multi-fidelity quantile regression. The central idea is a local quantile link: at each covariate value, the HF quantile is represented as a low-fidelity (LF) quantile evaluated at a covariate-dependent level. This reformulation reduces the problem to estimating the level function, which can be smoother than t...

---

### 17. Sharp feature-learning transitions and Bayes-optimal neural scaling laws in extensive-width networks

**Authors:** Minh-Toan Nguyen, Jean Barbier

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10395v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10395v1)

**Summary:** We study the information-theoretic limits of learning a one-hidden-layer teacher network with hierarchical features from noisy queries, in the context of knowledge transfer to a smaller student model. We work in the high-dimensional regime where the teacher width $k$ scales linearly with the input dimension $d$ -- a setting that captures large-but-finite-width networks and has only recently become analytically tractable. Using a heuristic leave-one-out decoupling argument, validated numerically ...

---

### 18. Regret Analysis of Guided Diffusion for Black-Box Optimization over Structured Inputs

**Authors:** Masaki Adachi, Anita Yang, Yakun Wang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10385v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10385v1)

**Summary:** Guided-diffusion black-box optimization (BO) has shown strong empirical performance on structured design problems such as molecules and crystals, but its regret behavior remains poorly understood. Existing BO regret analyses typically rely on maximum information gain, non-pretrained surrogate models, or exact acquisition maximization -- assumptions that break down in modern diffusion -- BO pipelines, where pretrained diffusion models serve as powerful priors over valid structures and acquisition...

---

### 19. Multifidelity Gaussian process regression for solving nonlinear partial differential equations

**Authors:** Fatima-Zahrae El-Boukkouri, Josselin Garnier, Olivier Roustant

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10383v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10383v1)

**Summary:** Solving nonlinear partial differential equations (PDEs) using kernel methods offers a compelling alternative to traditional numerical solvers. However, the performance of these methods strongly depends on the choice of kernel. In this work, as the available information is inherently multifidelity, we propose a kernel learning approach based on cokriging, leveraging empirical information from multifidelity simulations. In the first step, we fit a differentiable non-stationary kernel to an empiric...

---

### 20. Uncertainty in Physics and AI: Taxonomy, Quantification, and Validation

**Authors:** Manuel Haußmann, Ramon Winterhalder, Maria Ubiali

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10378v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10378v1)

**Summary:** Reliable uncertainty quantification is essential for the use of machine learning in physics, where scientific discoveries depend on validated probabilistic statements. We provide a structured overview of uncertainty quantification in ML for physics, introducing a unified taxonomy of uncertainty and clarifying the interpretation of predictive and inference uncertainties across frequentist and Bayesian frameworks. We discuss principled validation tools, including coverage, calibration, bias tests,...

---

### 21. Fast Training of Mixture-of-Experts for Time Series Forecasting via Expert Loss Integration

**Authors:** Btissame El Mahtout, Florian Ziel

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10330v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10330v1)

**Summary:** We propose a novel adaptive Mixture-of-Experts (MoE) framework for time series forecasting that enhances expert specialization by incorporating expert-specific loss information directly into the training process. Notably, the overall objective comprises the base forecasting loss and expert-specific losses, allowing expert-level prediction errors to jointly shape training alongside the global forecasting loss. This framework is further combined with a partial online learning strategy, enabling in...

---

### 22. Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation

**Authors:** Lucas Morisset, Alain Durmus, Adrien Hardy

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10290v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10290v1)

**Summary:** This paper aims at analyzing the regularization effect that data augmentation induces on supervised regression methods in the proportional regime, where the number of covariates grows proportionally to the number of samples. We provide a tight characterization of the test error, measured in mean squared error, in terms only of the population quantities of the true data, as well as first and second order statistics of the augmentation scheme. Our results are valid under misspecified feature maps,...

---

### 23. Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift

**Authors:** Bochao Li, Yao Fu, Wei Chen, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10289v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10289v1)

**Summary:** Offline-to-online learning aims to improve online decision-making by leveraging offline logged data. A central challenge in this setting is the distribution shift between offline and online environments. While some existing works attempt to leverage shifted offline data, they largely rely on UCB-type algorithms. Thompson sampling (TS) represents another canonical class of bandit algorithms, well known for its strong empirical performance and naturally suited to offline-to-online learning through...

---

### 24. Scalable Gaussian process inference via neural feature maps

**Authors:** Anthony Stephenson

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10285v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10285v1)

**Summary:** We present a theoretically grounded Gaussian process framework that leverages neural feature maps to construct expressive kernels. We show that the learned feature map can be interpreted as an optimal low-rank approximation to a Gram matrix derived from an implied RKHS, from which we establish consistency of the GP posterior. We further analyse the spectral properties of the induced kernels and introduce product feature-map kernels to address oversmoothing. This simple yet powerful approach enab...

---

### 25. Generalization Error Bounds for Picard-Type Operator Learning in Nonlinear Parabolic PDEs

**Authors:** Koichi Taniguchi, Sho Sonoda

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10277v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10277v1)

**Summary:** Operator learning for partial differential equations (PDEs) aims to learn solution operators on infinite-dimensional function spaces from finite-resolution data. In this setting, it is important for the learned model to be discretization-invariant, or resolution-robust, and to reflect PDE-specific structure. It is therefore natural to ask how such structure should be encoded in the model architecture, hypothesis class, or learning procedure. In this paper, we study operator learning for solution...

---

### 26. Extended Wasserstein-GAN Approach to Causal Distribution Learning: Density-Free Estimation and Minimax Optimality

**Authors:** Shu Tamano, Masaaki Imaizumi

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10206v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10206v1)

**Summary:** Distributional causal inference requires estimating not only average treatment effects but also interventional outcome distributions, including quantiles, tail risks, and policy-dependent uncertainty. As a method for distributional causal inference, generative adversarial network (GAN)-based counterfactual methods are flexible tools for this task. However, these methods have several limitations. First, the objectives of certain techniques do not coincide with the statistical risk of the identifi...

---

### 27. Hyperparameter Transfer for Dense Associative Memories

**Authors:** Roi Holtzman, Dmitry Krotov, Boris Hanin

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10164v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10164v1)

**Summary:** Dense Associative Memory (DenseAM) is a promising family of AI architectures that is represented by a neural network performing temporal dynamics on an energy landscape. While hyperparameter transfer methods are well-studied for feed-forward networks, these methods have not been developed for settings in which weights are shared across layers and within the layer, which is common in DenseAMs. Additionally, DenseAMs utilize rapidly peaking activation functions that are rarely used in feed-forward...

---

### 28. Coarsening Linear Non-Gaussian Causal Models with Cycles

**Authors:** Francisco Madaleno, Francisco C Pereira, Alex Markham

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10163v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10163v1)

**Summary:** Recent work on causal abstraction, in particular graphical approaches focusing on causal structure between clusters of variables, aims to summarize a high-dimensional causal structure in terms of a low-dimensional one. Existing methods for learning such summaries from data assume that both the high- and low-dimensional structures are acyclic, which is helpful for causal effect identification and reasoning but excludes many high-dimensional models and thus limits applicability. We show that in th...

---

### 29. PFN-TS: Thompson Sampling for Contextual Bandits via Prior-Data Fitted Networks

**Authors:** Yan Shuo Tan, Kenyon Ng, Ruizhe Deng, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10137v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10137v1)

**Summary:** Thompson sampling is a widely used strategy for contextual bandits: at each round, it samples a reward function from a Bayesian posterior and acts greedily under that sample. Prior-data fitted networks (PFNs), such as TabPFN v2+ and TabICL v2, are attractive candidates for this purpose because they approximate Bayesian posterior predictive distributions in a single forward pass. However, PFNs predict noisy future rewards, while Thompson sampling requires uncertainty over the latent mean reward f...

---

### 30. The two clocks and the innovation window: When and how generative models learn rules

**Authors:** Binxu Wang, Emma Lucia Byrnes Finn, Bingbin Liu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10019v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10019v1)

**Summary:** Generative models trained on finite data face a fundamental tension: their score-matching or next-token objective converges to the empirical training distribution rather than the population distribution we seek to learn. Using rule-valid synthetic tasks, we trace this tension across two training timescales: $τ_{\mathrm{rule}}$, the step at which generations first become rule-valid, and $τ_{\mathrm{mem}}$, the step at which models begin reproducing training samples. Focusing on parity and extendi...

---

### 31. Differentially Private Sampling from Distributions via Wasserstein Projection

**Authors:** Shokichi Takakura, Seng Pei Liew, Satoshi Hasegawa

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10015v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10015v1)

**Summary:** In this paper, we study the problem of sampling from a distribution under the constraint of differential privacy (DP). Prior works measure the utility of DP sampling with density ratio-based measures such as KL divergence. However, such formulations suffer from two key limitations: 1) they fail to capture the geometric structure of the support, and 2) they are not applicable when the supports of the distributions differ. To deal with these issues, we develop a novel framework for DP sampling wit...

---

### 32. Federated Language Models Under Bandwidth Budgets: Distillation Rates and Conformal Coverage

**Authors:** Prasanjit Dubey, Xiaoming Huo

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09986v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09986v1)

**Summary:** Training a language model on data scattered across bandwidth-limited nodes that cannot be centralized is a setting that arises in clinical networks, enterprise knowledge bases, and scientific consortia. We study the regime in which data must remain distributed across nodes, and ask what statistical guarantees are in principle achievable under explicit bandwidth budgets; we aim to characterize what is provably possible, not to demonstrate a deployment-ready system. Existing theory treats either t...

---

### 33. Consolidation-Expansion Operator Mechanics:A Unified Framework for Adaptive Learning

**Authors:** Debashis Guha

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09968v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09968v1)

**Summary:** Every adaptive learning system must alternate between two operations: consolidating what it already knows and expanding into new evidence. We propose \emph{Consolidation-Expansion Operator Mechanics} (OpMech), a framework that makes this structure precise. The central object is the \emph{order-gap} $\Ogap(θ; e)$, the degree to which a consolidation operator~$Q$ and an expansion operator~$P_e$ fail to commute at a given knowledge state. Because the order-gap is computable from the system's own tr...

---

### 34. Unified Approach for Weakly Supervised Multicalibration

**Authors:** Futoshi Futami, Takashi Ishida

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09857v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09857v1)

**Summary:** Multicalibration requires predicted scores to agree with label probabilities across rich families of subgroups and score-dependent tests, but existing methods require clean input-label pairs for evaluation and post-processing. This assumption fails in weakly supervised learning (WSL) regimes -- including positive-unlabeled, unlabeled-unlabeled, and positive-confidence learning -- where clean labels are costly or unavailable even though reliable uncertainty estimates may be crucial. We address th...

---

### 35. Supercharging Bayesian Inference with Reliable AI-Informed Priors

**Authors:** Jongwoo Choi, Sean O'Hagan

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09834v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09834v1)

**Summary:** Modern predictive systems encode beliefs that can act as useful prior information for statistical inference in data-limited settings. Using them for prior construction introduces a tradeoff: an informative prior built from a predictive model can sharpen inference from limited data, but also risks propagating error from the model into the posterior. We propose a framework for AI-informed prior elicitation that mitigates this tension by rectifying the AI-induced law that generates synthetic data b...

---

### 36. On Uniform Error Bounds for Kernel Regression under Non-Gaussian Noise

**Authors:** Johannes Teutsch, Oleksii Molodchyk, Marion Leibold, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09757v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09757v1)

**Summary:** Providing non-conservative uncertainty quantification for function estimates derived from noisy observations remains a fundamental challenge in statistical machine learning, particularly for applications in safety-critical domains. In this work, we propose novel non-asymptotic probabilistic uniform error bounds for kernel-based regression. Compared to related bounds in the literature that are restricted to (conditionally) independent sub-Gaussian noise, our bounds allow to consider a broad class...

---

### 37. Accelerating Power Method with Fast Sketching for Stronger Low-Rank Approximation

**Authors:** Shabarish Chenakkod, Michał Dereziński

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09755v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09755v1)

**Summary:** The power method is one of the most fundamental tools for extracting top principal components from data through low-rank matrix approximation. Yet, when the target rank is large, the cost of matrix multiplication associated with this procedure becomes a major bottleneck. We develop an algorithmic and theoretical framework for accelerating the power method using fast sketching, which is a popular paradigm in randomized linear algebra. Our framework leads to simple and provably efficient methods f...

---

### 38. LGB+: A Macroeconomic Forecasting Road Test

**Authors:** Philippe Goulet Coulombe

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09740v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09740v1)

**Summary:** Needless to say, linear dynamics are pervasive in economic time series, particularly autoregressive ones. While gradient boosting with trees excels at capturing nonlinearities, it is inefficient in small samples when much of the predictive content is linear, expending splits to approximate relationships better captured by simple linear terms. This paper proposes LGB+, a boosting procedure operating on a more inclusive set of basis functions. The idea comes in two flavors. LGB+ evaluates a tree a...

---

### 39. Learning stochastic multiscale models through normalizing flows

**Authors:** Anan Saha, Arnab Ganguly

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09718v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09718v1)

**Summary:** Many systems in physics, engineering, and biology exhibit multiscale stochastic dynamics, where low-dimensional slow variables evolve under the influence of high-dimensional fast processes. In practice, observations are often limited to a single trajectory of the slow component, while the fast dynamics remain unobserved, making statistical learning challenging. Approaches based on partial differential equations (PDE), such as Fokker-Planck formulations, aim to characterize the evolution of proba...

---

### 40. Quantifying the Risk-Return Tradeoff in Forecasting

**Authors:** Philippe Goulet Coulombe

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09712v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09712v1)

**Summary:** Average forecast accuracy is not the same as forecast reliability. I treat forecast loss differentials relative to a benchmark as a return series. I then evaluate these returns using risk-adjusted performance measures from finance, including the Sharpe ratio, Sortino ratio, Omega ratio, and drawdown-based metrics. I also introduce the Edge Ratio capturing a model's propensity to deliver uniquely informative predictions relative to the forecasting frontier. I apply this framework to U.S. macroeco...

---

### 41. Metropolis-Adjusted Diffusion Models

**Authors:** Kevin H. Lam, Tyler Farghly, Christopher Williams, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09654v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09654v1)

**Summary:** Sampling from score-based diffusion models incurs bias due to both time discretisation and the approximation of the score function. A common strategy for reducing this bias is to apply corrector steps based on the unadjusted Langevin algorithm (ULA) at each noise level within a predictor-corrector framework. However, ULA is itself a biased sampler, as it discretises a continuous diffusion process. In this work, we consider adjusted Langevin correctors that employ Metropolis--Hastings (MH) or Bar...

---

### 42. Minimax optimal submatrix detection: Sharp non-asymptotic rates

**Authors:** Parker Knight, Julien Chhor

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09569v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09569v1)

**Summary:** We consider the problem of detecting a hidden submatrix of size $s_1 \times s_2$ in a high-dimensional Gaussian matrix of size $d_1 \times d_2$. Under the null hypothesis, the observed matrix has i.i.d.\ entries with distribution $N(0,1)$. Under the alternative hypothesis, there exists an unknown submatrix of size $s_1 \times s_2$ with i.i.d.\ entries with distribution $N(μ, 1)$ for some $μ>0$, while all other entries outside the submatrix are i.i.d.\ $N(0,1)$. Specifically, we provide non-asymp...

---

### 43. Phases of Muon: When Muon Eclipses SignSGD

**Authors:** Elliot Paquette, Noah Marshall, Lucas Benigni, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09552v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09552v1)

**Summary:** Recently, Muon and related spectral optimizers have demonstrated strong empirical performance as scalable stochastic methods, often outperforming Adam. Yet their behaviour remains poorly understood. We analyze stochastic spectral optimizers, including Muon, on a high-dimensional matrix-valued least squares problem. We derive explicit deterministic dynamics that provide a tractable framework for studying learning behaviour with a focus on (stochastic) SignSVD, which Muon approximates, and (stocha...

---

### 44. HS-FNO: History-Space Fourier Neural Operator for Non-Markovian Partial Differential Equations

**Authors:** Lennon J. Shikhman

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09523v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09523v1)

**Summary:** Neural operators provide fast surrogate models for time-dependent partial differential equations, but their standard autoregressive use usually assumes that the instantaneous field $u(t,\cdot)$ is a complete state. This assumption fails for delay equations, distributed-memory systems, and other non-Markovian dynamics: two trajectories may agree at time $t$ and nevertheless have different futures because their histories differ. We introduce the History-Space Fourier Neural Operator (HS-FNO), a ne...

---

### 45. Empirical Bayes 1-bit matrix completion

**Authors:** Takeru Matsuda

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09509v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09509v1)

**Summary:** The problem of predicting unobserved entries in a binary matrix, known as 1-bit matrix completion, has found diverse applications in fields such as recommendation systems. In this study, we develop an empirical Bayes method for 1-bit matrix completion motivated by the Efron--Morris estimator, a matrix generalization of the James--Stein estimator that shrinks singular values toward zero. The proposed method exploits the underlying low-rank structure of binary matrices, drawing parallels with mult...

---

### 46. SEMASIA: A Large-Scale Dataset of Semantically Structured Latent Representations

**Authors:** Mario Edoardo Pandolfo, Enrico Grimaldi, Lorenzo Marinucci, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09485v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09485v1)

**Summary:** Latent representations learned by neural networks often exhibit semantic structure, where concept similarity is reflected by geometric proximity in embedding space. However, comparing such spaces across models remains difficult: changes in architecture, pretraining data, objective, or random seed can yield embeddings with similar content but incompatible geometry. This latent space alignment problem is central to interpretability, transfer and multimodal learning, federated systems, and semantic...

---

### 47. Proximal Path-Specific Inference

**Authors:** Yang Bai, Sihan Wu, Baoluo Sun, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09462v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09462v1)

**Summary:** Causal mediation analysis has been extended to estimate path-specific effects with multiple intermediate variables, isolating treatment effects through a mediator of interest while excluding pathways through its ancestors. Such analyses address bias from recanting witnesses, i.e., treatment-induced mediator-outcome confounders. However, existing methods typically rely on stringent assumptions precluding general unmeasured confounding, which are often violated in practice. In this paper, we relax...

---

### 48. Quantitative Local Convergence of Mean-Field Stein Variational Gradient Flow

**Authors:** Lénaïc Chizat, Maria Colombo, Roberto Colombo, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09456v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09456v1)

**Summary:** Stein Variational Gradient Descent (SVGD) is a deterministic interacting-particle method for sampling from a target probability measure given access to its score function. In the mean-field and continuous-time limit, it is known that the flow converges weakly toward the target, but no quantitative rate is known for the last iterate. In this paper, we establish quantitative local convergence in strong norms for this dynamics, when the interaction kernel is of Riesz type on the $d$-dimensional tor...

---

### 49. Optimal Regret for Single Index Bandits

**Authors:** Devdan Dey, Sujoy Bhore, Avishek Ghosh

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09454v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09454v1)

**Summary:** We study the $\textit{single-index bandit}$ problem, where rewards depend on an unknown one-dimensional projection of high-dimensional contexts through an unknown reward function. This model extends linear and generalized linear bandits to a nonparametric setting, and is particularly relevant when the reward function is not known in advance. While optimal regret guarantees are known for monotone reward functions, the general non-monotone case remains poorly understood, with the best known bound ...

---

### 50. Inverse Design for Conditional Distribution Matching

**Authors:** Ori Meidler, Shaul Tolkovsky, Or Zuk

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09439v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09439v1)

**Summary:** Generative models are powerful tools for sampling from a learned distribution $\mathcal{P}(Y \mid X)$, and inverse-design methods invert this map to find an input $x$ that produces a desired point output $y^*$. However, many design goals are naturally distributional rather than pointwise, incorporating the inherent uncertainty of $Y$ and targeting a specific form for it, a task not addressed by standard inverse design. To address this issue we introduce Conditional Distribution Matching (CDM), a...

---

