# arXiv Daily Digest - 2026-07-03

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Distributed Attacks in Persistent-State AI Control

**Authors:** Josh Hills, Ida Caspary, Asa Cooper Stickland

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02514v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02514v1)

**Summary:** As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterativ...

---

### 2. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning

**Authors:** Matteo Boglioni, Thibault Rousset, Siva Reddy, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02513v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02513v1)

**Summary:** LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's...

---

### 3. Program-as-Weights: A Programming Paradigm for Fuzzy Functions

**Authors:** Wentao Zhang, Liliana Hotsko, Woojeong Kim, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02512v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02512v1)

**Summary:** Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P...

---

### 4. Online Safety Monitoring for LLMs

**Authors:** Mona Schirmer, Metod Jazbec, Alexander Timans, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02510v1)

**Summary:** Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...

---

### 5. ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning

**Authors:** Yanjun Zhao, Ruizhong Qiu, Tianxin Wei, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02509v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02509v1)

**Summary:** Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context windows, they often fail to use relevant evidence that is already present in the input, revealing a gap between context access and effective context utilization. In this work, we propose Recursive Evidence Replay as LLM Harness for Long-Context Reasoning (RECONTEXT), a training-free inference metho...

---

### 6. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates

**Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02507v1)

**Summary:** LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR resp...

---

### 7. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas

**Authors:** Yuxuan Li, Lingxi Xie, Xinyue Huo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02504v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02504v1)

**Summary:** Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integra...

---

### 8. DemoPSD: Disagreement-Modulated Policy Self-Distillation

**Authors:** Yunhe Li, Hao Shi, Wenhao Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02502v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02502v1)

**Summary:** On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamenta...

---

### 9. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials

**Authors:** Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02499v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02499v1)

**Summary:** Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general models, the choice of optimizer for training has largely remained unexplored, defaulting to Adam and its variants in the community. Here, we implement and systematically compare a class of recently proposed matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training Nequ...

---

### 10. G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models

**Authors:** Timo Bertram, Sidhant Bhavnani, Richard Freinschlag, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02491v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02491v1)

**Summary:** In this work, we focus on SE-RRMs, a symbol-equivariant instantiation of RRMs that exhibits improved extrapolation to larger problem sizes. We propose a neuro-symbolic approach, ``Guiding with Recurrent Reasoning Models'' (G-RRM), which integrates SE-RRMs with symbolic solvers for constraint satisfaction problems. SE-RRMs act as neural solvers that generate full solution proposals and guide classical symbolic solvers, such as backtracking or SAT-based methods like Glucose 4.1 and CaDiCaL 3.0.0, ...

---

### 11. Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning

**Authors:** Xuehui Wang, Xuankun Yang, Wei Shen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02484v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02484v1)

**Summary:** Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware ...

---

### 12. TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution

**Authors:** Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02469v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02469v1)

**Summary:** Software tests and code evolve together: a code change should be followed by new or updated tests that record the new software behavior. Yet existing test generation and update benchmarks often isolate the test from the code change, and rely on static metadata that does not verify whether a test is executable or semantically tied to the code change. This makes it difficult to evaluate whether a test automation agent understands how a code change should propagate into the test suite.   We introdu...

---

### 13. Human Capital, Not Model Benchmarks, Predicts Hybrid Intelligence in Forecasting

**Authors:** Vivienne Ming

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02467v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02467v1)

**Summary:** Whether pairing people with AI helps or hurts is usually reported as a single average effect. Using a real-money prediction market (Polymarket) as an objective, externally resolved benchmark, this pilot shows that the value of human-AI collaboration depends on a specific, measurable form of human capital. Analyzed at the level of the individual forecaster, hybrid performance is trimodal: most people either deferred to the model (matching it) or used it to rubber-stamp a prior guess (performing w...

---

### 14. Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs

**Authors:** Junhao Shi, Siyin Wang, Xiaopeng Yu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02466v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02466v1)

**Summary:** Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of expert demonstrations -- triplets of observations, instructions, and actions that are costly to collect at scale. We argue that this bottleneck stems from conflating two distinct learning objectives: acquiring physical competence (how to move) and acquiring semantic alignment (what to do). Crucially, only the latter requires language supervision. Building on this Decomposition Hypothesis, we propose Task-Agnost...

---

### 15. OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers

**Authors:** Donghyun Lee, Jitesh Chavan, Duy Nguyen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02461v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02461v1)

**Summary:** Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in...

---

### 16. Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation

**Authors:** Zhuowei Chen, Xiang Lorraine Li

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02460v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02460v1)

**Summary:** Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these appr...

---

### 17. EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments

**Authors:** Zhilin Wang, Han Song, Runzhe Zhan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02440v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02440v1)

**Summary:** Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive R...

---

### 18. Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study

**Authors:** Achint Mehta

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02436v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02436v1)

**Summary:** Agentic coding assistants are increasingly given extra capabilities, such as browser based testing tools and design oriented system prompts, on the assumption that more capability yields better software. This study tested that assumption directly. Ninety independent agent runs built the same application, a real time retrospective board, from one detailed specification, each scored on a fixed 14 criterion functional rubric (42 point maximum) and a visual quality review. The runs spanned several m...

---

### 19. Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach

**Authors:** Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02432v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02432v1)

**Summary:** Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that comb...

---

### 20. WorldSample: Closed-loop Real-robot RL with World Modelling

**Authors:** Yuquan Xue, Le Xu, Zeyi Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02431v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02431v1)

**Summary:** Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations. However, deploying RL on real robots remains constrained by high interaction costs, since each physical rollout is costly and reflects only one realized action-outcome path. To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for rea...

---

### 21. QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition

**Authors:** Quoc Bao Phan, Tuy Tan Nguyen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02426v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02426v1)

**Summary:** Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid qu...

---

### 22. Neuron-Aware Active Few-Shot Learning for LLMs

**Authors:** Zhuowei Chen, Liwei Chen, Christian Schunn, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02423v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02423v1)

**Summary:** Active Few-Shot Learning (AFSL) adapts LLMs to specialized domains by identifying the most valuable unlabeled samples for annotation and use as few-shot demonstrations, effectively reducing human annotation costs while promoting high performance. However, existing methods typically rely on output-level signals for sample identification, such as predictive entropy or semantic similarities with test-time data based on external embeddings, which often overlook models' internal dynamics, which could...

---

### 23. Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments

**Authors:** Xianhui Meng, Zirui Song, Yuchen Zhang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02407v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02407v1)

**Summary:** Large Language Models (LLMs) have demonstrated remarkable capabilities in 3D indoor synthesis for Manhattan environments. However, existing methods often fail to capture plausible object layout patterns in non-Manhattan settings, primarily because they struggle to model non-orthogonal spatial relationships, leading to high geometric violations and low physical fidelity. To address this challenge, we propose SPG-Layout, a novel text-driven framework designed to generate physically plausible indoo...

---

### 24. ACID: Action Consistency via Inverse Dynamics for Planning with World Models

**Authors:** Gawon Seo, Dongwon Kim, Suha Kwak

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02403v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02403v1)

**Summary:** Decision-time planning with action-conditioned world models has become a popular paradigm for embodied control. However, the standard planning cost judges a candidate solely by how close its predicted terminal state lies to the goal, leaving the realizability of the intermediate transitions unchecked -- a predicted trajectory can look convincing while the environment rollout drifts away from it. In this paper, we propose ACID, a decision-time planning framework that introduces cycle action consi...

---

### 25. Fast Multi-dimensional Refusal Subspaces via RFM-AGOP

**Authors:** Thomas Winninger

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02396v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02396v1)

**Summary:** Steering and monitoring activations in Large Language Models (LLMs) are increasingly used for both safety and interpretability. Early work assumed behaviours are encoded along single linear directions, but recent findings suggest complex behaviours, such as the refusal to answer harmful queries, live in multi-dimensional subspaces. However, existing methods for extracting these subspaces are computationally expensive, which becomes prohibitive on reasoning models who produce long reasoning trace...

---

### 26. Steerability via constraints: a substrate for scalable oversight of coding agents

**Authors:** Thomas Winninger

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02389v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02389v1)

**Summary:** Coding agents are capable; human oversight is the bottleneck. Unconstrained agents introduce security risks, erode codebase scalability, and make human review increasingly costly. We argue that the same methods used for decades to manage large human engineering teams: access control, network policies, strict coding conventions enforced by tooling; transfer directly to coding agents, and are cheaper (in token) than recent agentic scaffolding. We sketch a start-to-end system on this principle, and...

---

### 27. Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems

**Authors:** Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02376v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02376v1)

**Summary:** Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination p...

---

### 28. DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models

**Authors:** Xi Fang, Weijie Xu, Yingqiang Ge, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02374v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02374v1)

**Summary:** Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study whether such memory reshapes reasoning on open-ended questions where no single ground-truth answer exists. To quantify this effect, we introduce DRIFTLENS, a ground-truth-free framework that maps each ...

---

### 29. VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval

**Authors:** Cristian-Gabriel Florea, Stelian Spînu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02371v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02371v1)

**Summary:** Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time v...

---

### 30. Understanding Agent-Based Patching of Compiler Missed Optimizations

**Authors:** Batu Guan, Zirui Wang, Shaohua Li

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02370v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02370v1)

**Summary:** Compiler missed optimizations refer to cases in which compilers failed to optimize certain code. It takes many compiler developers' efforts to implement or patch such missed optimizations. In this paper, we present a systematic study of how well agents patch compiler missed optimizations. We identify a significant challenge that patching a missed optimization requires more than just fixing the reported case, and instead requires generalizing to similar cases. We construct a benchmark of real-wor...

---

### 31. World Wide Models: Literary Tools for Cultural AI

**Authors:** Nina Begus

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02369v1)

**Summary:** LLMs stage a new form of cultural encounter that is massive, automated, and monolingual. Literary disciplines have always negotiated cultural struggles with comparative reading of literature, narratological and poetic analysis, critical theory, world literature, and translation. These tools have now become indispensable for building culturally literate AI. The essay develops a layered framework toward more nuanced textual models and pluralistic interpretations of AI, emphasizing the natural inte...

---

### 32. The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent Geometry

**Authors:** Yuan Yuan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02368v1)

**Summary:** Evaluations of LLM personas via psychometric questionnaires typically rely on aggregate scores, discarding within-instance correlation structure. We test whether this geometric structure is intrinsic or frame-dependent. Constructing within-instance correlation matrices from IPIP-50 responses, we analyze geometry on SPD manifolds under manipulated question orderings in GPT-4o simulating American and Chinese-American personas. We find that persona expression comprises two dissociable components: a...

---

### 33. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 34. GAP-GDRNet: Geometry-Aware Monocular Visual Pose Sensing on a Single-Target Synthetic Spacecraft Dataset

**Authors:** Yonglong Zhang, Yang Liu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02360v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02360v1)

**Summary:** Monocular relative pose sensing is a central perception problem in non-cooperative rendezvous and on-orbit servicing. In spacecraft images, however, weak surface texture, thin appendages, illumination changes, and partial occlusion often leave only sparse and unstable geometric evidence. This article presents GAP-GDRNet, a geometry-aware attention-enhanced framework for monocular RGB-based 6D pose sensing. The method follows the geometry-guided direct regression paradigm of GDR-Net and modifies ...

---

### 35. SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces

**Authors:** Jinwei Hu, Yi Dong, Youcheng Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02345v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02345v1)

**Summary:** Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting ...

---

### 36. Self-Gating Attention for Efficient Time Series Forecasting

**Authors:** Dezheng Wang, Tong Chen, Wei Yuan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02344v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02344v1)

**Summary:** Transformer architectures have shown strong potential in time series forecasting, where multi-head self-attention is widely used to capture temporal dependencies across historical timestamps. However, standard self-attention has quadratic time and memory complexity with respect to the look-back length. This cost may limit its use in resource-constrained or high-throughput forecasting systems, where fast and memory-efficient inference is important. Through qualitative and quantitative analyses, w...

---

### 37. SelectTSL: Prompt-Guided Selective Target Sound Localization in Complex Scenarios

**Authors:** Ziyang Jiang, Yu Chen, Zexu Pan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02343v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02343v1)

**Summary:** Humans can selectively attend to a target sound and estimate its direction in complex scenarios, whereas such selective localization remains challenging for current deep learning-based systems. Sound source localization (SSL) has achieved remarkable success with deep learning, yet most methods localize all active sources without selectivity. Conversely, target sound extraction (TSE) extracts sources using multimodal prompts but typically fails to preserve the multichannel spatial information req...

---

### 38. Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics

**Authors:** Haonan Huang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02329v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02329v1)

**Summary:** Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to...

---

### 39. A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets

**Authors:** Wanyun Cui

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02303v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02303v1)

**Summary:** Linear-attention and state-space language models compress the prefix into a fixed-size recurrent state, yielding O(1) memory at the cost of a lossy exact memory: when many key--value associations compete, earlier facts are overwritten and needle recall degrades. Inspired by Complementary Learning Systems, we give linear attention a hippocampal complement. HOLA (Hippocampal Linear Attention) keeps the usual delta-rule state as a compressive memory and adds a bounded exact KV cache, forming a semi...

---

### 40. Generalization in offline RL: The structure is more important than the amount of pessimism

**Authors:** Max Weltevrede, Matthijs T. J. Spaan, Wendelin Böhmer

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02288v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02288v1)

**Summary:** While pessimism counteracts overestimation bias in offline reinforcement learning (RL), being overly conservative has been associated with hindering certain forms of generalization. However, in this paper we demonstrate that being overly pessimistic does not inherently prevent optimal generalization in contextual MDPs (CMDPs). Instead, we argue successful generalization depends not on the amount of pessimism, but whether the pessimistic structure respects the underlying symmetries of the optimal...

---

### 41. AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language Models

**Authors:** Rintaro Otsubo, Ryo Fujii, Reina Ishikawa, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02269v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02269v1)

**Summary:** Vision-Language Models (VLMs) have demonstrated immense promise in Spatio-Temporal Video Grounding (STVG). However, current evaluation protocols are largely confined to zero-shot assessments on general, daily-life benchmarks. This creates a critical disconnect from real-world applications in specialized fields, where models inevitably encounter rare visual concepts and complex spatio-temporal dynamics. Since exhaustive pre-training across infinite data distributions is infeasible, the ability to...

---

### 42. HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures

**Authors:** Ziyun Qiao, Yue Min, Ruining Chen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02266v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02266v1)

**Summary:** Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Tr...

---

### 43. AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

**Authors:** Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02255v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02255v1)

**Summary:** Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw ...

---

### 44. Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support

**Authors:** Seren Yenikent, Jack Vinijtrongjit, Katherine Ng

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02245v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02245v1)

**Summary:** Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system design...

---

### 45. Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages

**Authors:** A. Seza Doğruöz, Xixian Liao, Verena Blaschke, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02235v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02235v1)

**Summary:** LLM-as-a-Judge has become the dominant evaluation paradigm for many natural language generation tasks, due to shortcomings of conventional metrics and high correlations with human judgment, albeit mostly in English. There are now attempts to extend LLM-as-a-Judge to multilingual settings including low-resource languages. However, LLMs have limited proficiency in low-resource languages, and there is often no adequate human validation in these settings. To highlight the scope of the problem and cu...

---

### 46. Purified OPSD: On-Policy Self-Distillation Without Losing How to Think

**Authors:** Zhanming Shen, Jintao Tong, Shaotian Yan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02234v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02234v1)

**Summary:** On-policy self-distillation (OPSD) has emerged as a promising paradigm for improving LLM reasoning, where a privileged teacher with access to reference solutions provides token-level supervision on the student's own generated trajectories. However, we find that OPSD consistently fails on long chain-of-thought (long-CoT) reasoning models, yielding at best marginal gains while destabilizing the reflective reasoning capability these models depend on. Through a novel decomposition of the teacher's s...

---

### 47. Efficient Waste Sorting for Circular Economy: A Confidence-guided comparison between One-Vs-All and One-Vs-Rest Classification Strategies with Human-in-the-Loop for Automated Waste Sorting

**Authors:** Mohammed Fahad Ali, Dominique Briechle, Marit Briechle-Mathiszig, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02230v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02230v1)

**Summary:** The complexity of waste disposal regulations across European countries poses significant challenges for the residents and hinders the transition to a Circular Economy. In Germany, the proper sorting and disposal of household waste remains challenging across municipalities. Consequently, substantially reducing incorrectly disposed waste is vital for improving waste management and advancing the Circular Economy. AI-based waste sorting solutions can support residents through user-friendly tools, su...

---

### 48. CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation

**Authors:** Haokun Liu, Zhaoqi Ma, Yicheng Chen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02222v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02222v1)

**Summary:** Vision-Language Navigation has increasingly emphasized high-level instruction reasoning, memory, global map construction, and instruction decomposition, while the low-level action representation remains comparatively underexplored. We propose CoFL-S, a low-level vision-language-action framework that predicts a language-conditioned flow field over the robot's local visible sector and generates continuous trajectories by rolling out the predicted field. To train this low-level representation, we c...

---

### 49. Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks

**Authors:** Ravi Kant Sharma

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02210v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02210v1)

**Summary:** The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercep...

---

### 50. The Eticas AI Risk Taxonomy: Open Infrastructure for Operationalizing AI Audits

**Authors:** Gemma Galdon Clavell, Pablo Accuosto, Usman Gohar

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02201v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02201v1)

**Summary:** The rapid deployment of AI systems across high-stakes domains has created urgent demand for standardized evaluation, yet the field remains fragmented across competing risk taxonomies that catalog risks without showing how an audit is executed. At least 74 AI risk taxonomies exist, and almost all stop at the catalog. The hard part of auditing is not naming a risk but operationalizing it: turning it into a test run against a real system, a measured value, a calibrated severity, and a defensible gr...

---

## cs.CL

**50 papers**

### 1. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning

**Authors:** Matteo Boglioni, Thibault Rousset, Siva Reddy, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02513v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02513v1)

**Summary:** LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's...

---

### 2. Program-as-Weights: A Programming Paradigm for Fuzzy Functions

**Authors:** Wentao Zhang, Liliana Hotsko, Woojeong Kim, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02512v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02512v1)

**Summary:** Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P...

---

### 3. Online Safety Monitoring for LLMs

**Authors:** Mona Schirmer, Metod Jazbec, Alexander Timans, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02510v1)

**Summary:** Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...

---

### 4. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates

**Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02507v1)

**Summary:** LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR resp...

---

### 5. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas

**Authors:** Yuxuan Li, Lingxi Xie, Xinyue Huo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02504v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02504v1)

**Summary:** Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integra...

---

### 6. Towards Robustness against Typographic Attack with Training-free Concept Localization

**Authors:** Bohan Liu, Wenqian Ye, Guangzhi Xiong, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02494v1)

**Summary:** Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability ...

---

### 7. Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning

**Authors:** Liyan Tang, Fangcong Yin, Greg Durrett

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02490v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02490v1)

**Summary:** Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement lear...

---

### 8. Audio-Based Understanding of Audiobook Narration Appeal

**Authors:** Shahar Elisha, Mariano Beguerisse-Díaz, Emmanouil Benetos

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02473v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02473v1)

**Summary:** Narration is central to the audiobook listening experience, shaping how listeners engage with and understand the content. This work explores how narration qualities shape an audiobook's appeal, noting that their effects can vary by genre, title, and audience. We extract vocal and acoustic features (e.g., tone, pace, loudness) from LibriVox using pre-trained audio models and analyse their relationship with consumption data (specifically, view-rate) and their interplay with genre and title. Despit...

---

### 9. TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution

**Authors:** Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02469v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02469v1)

**Summary:** Software tests and code evolve together: a code change should be followed by new or updated tests that record the new software behavior. Yet existing test generation and update benchmarks often isolate the test from the code change, and rely on static metadata that does not verify whether a test is executable or semantically tied to the code change. This makes it difficult to evaluate whether a test automation agent understands how a code change should propagate into the test suite.   We introdu...

---

### 10. Will Scaling Improve Social Simulation with LLMs?

**Authors:** Caleb Ziems, William Held, Su Doga Karaca, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02464v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02464v1)

**Summary:** Large Language Model (LLM) social simulations are a promising research method, but they are not yet faithful enough to be adopted widely. In this work, we investigate whether the current scaling paradigm in language modeling is likely to close these gaps, or whether simulation fidelity is orthogonal to general capabilities and therefore deserving of more research attention. We use scaling laws to study the relationship between LLMs' compute scale, general capability benchmarks, and the fidelity ...

---

### 11. Language Models as Measurement Apparatus for Culture

**Authors:** Kent K. Chang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02459v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02459v1)

**Summary:** Language models are increasingly used to quantify cultural phenomena, but what makes such measurement distinctively cultural? This paper argues that NLP work on culture is a material-discursive practice: the apparatus -- model, data, annotation, evaluation -- participates in constituting the cultural reality it measures, rather than passively recording it. Drawing on Karen Barad's concept of the agential cut -- the contingent boundary between phenomenon and instrument -- I show that the apparatu...

---

### 12. EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments

**Authors:** Zhilin Wang, Han Song, Runzhe Zhan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02440v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02440v1)

**Summary:** Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive R...

---

### 13. Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach

**Authors:** Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02432v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02432v1)

**Summary:** Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that comb...

---

### 14. The Future of NLP may not be at NLP Conferences: Scholarly Migration Patterns in Natural Language Processing

**Authors:** David Jurgens

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02416v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02416v1)

**Summary:** Natural Language Processing (NLP) has traditionally been published in its core disciplinary venues like ACL. However, advances in Large Language Models (LLMs) has led to a blurring of the disciplinary lines between NLP and general Machine Learning (ML), with authors regularly publishing in venues from both fields. Here, we ask whether the disciplinary center of gravity is shifting. Using NLP research published from 2010 to 2026 and studies of both established and new authors, we find that a migr...

---

### 15. Know Your Source: A Public Knowledge Store for Media Background Checks

**Authors:** Benjamin Nichols, Michael Schlichtkrull, Nedjma Ousidhoum

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02383v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02383v1)

**Summary:** LLM-based retrieval-augmented generation (RAG) is increasingly used for automated fact-checking (AFC) and related tasks. By grounding LLM outputs in retrieved evidence, RAG-based systems provide transparent justifications while allowing external information to be updated independently of the underlying model. However, existing approaches often assume retrieved evidence is reliable, although real-world information may be conflicting, outdated, and can originate from unreliable or biased sources. ...

---

### 16. HULAT2 at MER-TRANS 2026: Governed Multi-Agent Simplification for Spanish Easy-to-Read Generation

**Authors:** Lourdes Moreno, Paloma Martínez, Marco Antonio Sanchez-Escudero, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02381v1)

**Summary:** This paper describes the participation of HULAT2-UC3M in the Spanish track of MER-TRANS 2026, a shared task on multilingual Easy-to-Read translation. Three fully automatic Spanish runs were submitted. RUN1 and RUN2 used a LangGraph-based multi-agent workflow combining Gemini 2.5 Flash and RigoChat-7B-v2, parallel generation strategies, internal quality signals, Event-Condition-Action routing, controlled editing and traceable decisions. RUN1 used the base workflow, while RUN2 activated an additio...

---

### 17. World Wide Models: Literary Tools for Cultural AI

**Authors:** Nina Begus

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02369v1)

**Summary:** LLMs stage a new form of cultural encounter that is massive, automated, and monolingual. Literary disciplines have always negotiated cultural struggles with comparative reading of literature, narratological and poetic analysis, critical theory, world literature, and translation. These tools have now become indispensable for building culturally literate AI. The essay develops a layered framework toward more nuanced textual models and pluralistic interpretations of AI, emphasizing the natural inte...

---

### 18. SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces

**Authors:** Jinwei Hu, Yi Dong, Youcheng Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02345v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02345v1)

**Summary:** Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting ...

---

### 19. HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report

**Authors:** Minghao Li, Raghav Mittal, Sanjivni Rana, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02338v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02338v1)

**Summary:** Hierarchical Navigable Small World (HNSW) graphs serve as the industry standard due to their logarithmic complexity and strong empirical performance. However, HNSW relies on greedy graph traversal, a heuristic that provides no theoretical guarantees of correctness. In this paper, we propose a novel "Certify-then-Rectify" framework that bridges the gap between the speed of heuristic search and the rigor of exact retrieval. Rather than discarding HNSW, our approach first employs a distribution-fre...

---

### 20. On the Role of Directionality in Structural Generalization

**Authors:** Zichao Wei

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02307v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02307v1)

**Summary:** Several SLOG test categories explicitly involve directional distinctions (modifier position shifts, argument extraction positions), yet AM-Parser, the previous SOTA, uses an AM algebra whose operations do not encode direction. We redesign the symbolic backend around CCG directed types (deterministic CKY + single linear decoder, 30K learnable parameters). Under the same BERT-base encoder, the system achieves 75.9$\pm$6.4% LF exact match, surpassing AM-Parser (70.8$\pm$4.3%). Per SLOG's own catego...

---

### 21. HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures

**Authors:** Ziyun Qiao, Yue Min, Ruining Chen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02266v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02266v1)

**Summary:** Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Tr...

---

### 22. CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning

**Authors:** Dingling Xu, Ruobing Wang, Qingfei Zhao, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02262v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02262v1)

**Summary:** Reasoning Language Models (RLMs) have significantly improved performance on complex tasks by extending the reasoning chain. However, these chains are prone to containing factual errors, particularly in knowledge-intensive tasks. To address this issue, we propose CheckRLM, a framework that improves the reliability of the reasoning process through Retrieval-Augmented Generation (RAG) by timely checking and correcting factual errors. Specifically, CheckRLM extracts factual claims from the reasoning...

---

### 23. BamiBERT: A New BERT-based Language Model for Vietnamese

**Authors:** Dat Quoc Nguyen, Thinh Pham, Chi Tran, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02259v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02259v1)

**Summary:** In this paper, we introduce BamiBERT, a new BERT-based pre-trained language model for Vietnamese that addresses key limitations of PhoBERT -- the current de facto Vietnamese text encoder. Trained from scratch on a 129GB corpus of general-domain Vietnamese text for 20 epochs, BamiBERT supports an extended context length of up to 2048 tokens and operates directly on raw input, eliminating the need for external word segmentation. Across 8 Vietnamese benchmarks, it achieves the best score on 11 of 1...

---

### 24. AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

**Authors:** Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02255v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02255v1)

**Summary:** Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw ...

---

### 25. Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages

**Authors:** A. Seza Doğruöz, Xixian Liao, Verena Blaschke, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02235v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02235v1)

**Summary:** LLM-as-a-Judge has become the dominant evaluation paradigm for many natural language generation tasks, due to shortcomings of conventional metrics and high correlations with human judgment, albeit mostly in English. There are now attempts to extend LLM-as-a-Judge to multilingual settings including low-resource languages. However, LLMs have limited proficiency in low-resource languages, and there is often no adequate human validation in these settings. To highlight the scope of the problem and cu...

---

### 26. Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning

**Authors:** Congrui Du, Yang Zhang, Kaizhi Qian, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02214v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02214v1)

**Summary:** Instruction tuning for speech language models (SLMs) is substantially more challenging than for text-based large language models (LLMs), as it requires learning a new modality and a wide range of speech-specific instructions in addition to those supported by text LLMs. Existing SLM training approaches largely replicate the text LLM training paradigm by synthesizing large-scale speech pre-training and instruction-tuning datasets. However, this strategy is difficult to scale, since speech sequence...

---

### 27. Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation

**Authors:** Jijie Zhang, Zhe Ren, Quan Zhang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02182v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02182v1)

**Summary:** Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially ag...

---

### 28. HaloGuard 1.0: An Open Weights Constitutional Classifier for Multilingual AI Safety

**Authors:** Navaneeth Sangameswaran, Preetham S, Ashmiya Lenin

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02079v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02079v1)

**Summary:** We present HaloGuard 1.0, an open-weights implementation of the constitutional-classifier paradigm for input safety. It achieves state-of-the-art performance on English and multilingual prompt-safety benchmarks at roughly one-tenth the model size of current leading open guard models. The safety constitution is the organising structure of the corpus: a natural-language constitution of 46 policies and 2,940 subcategories drives synthetic data generation, with exhaustive one-to-one paired counterfa...

---

### 29. SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLM Responses

**Authors:** Anna Chorna

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02049v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02049v1)

**Summary:** Large Language Models are increasingly deployed in emotional-support contexts and crisis-related situations. Nevertheless, their cross-lingual abilities in these circumstances remain underexplored. Existing benchmarks emphasize multilingual performance but rarely examine crisis-related empathy and cultural grounding in low-to-mid-resource languages. We introduce SPLIT, a 500-prompt benchmark designed to evaluate LLM consistency in generating emotionally grounded responses across five categories:...

---

### 30. OpenSafeIntent: Evaluating Intent-Calibrated Safe Completion Across Dual-Use Prompt Sets

**Authors:** Rheeya Uppaal, Seungwoo Lyu, Selina Sung, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02047v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02047v1)

**Summary:** Safe completion requires models to provide useful assistance without enabling harm, but this behavior is difficult to evaluate with isolated prompts. We introduce OpenSafeIntent, a benchmark of controlled prompt-sets that vary intent while holding the underlying task fixed. Each datapoint contains benign, dual-use, and malicious variants of the same task. This design lets us evaluate whether models calibrate assistance across intent shifts, rather than merely appearing safe on average. Across a ...

---

### 31. PACE: A Proxy for Agentic Capability Evaluation

**Authors:** Yueqi Song, Lintang Sutawika, Jiarui Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02032v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02032v1)

**Summary:** Evaluating LLM agents on benchmarks like SWE-Bench and GAIA can be expensive, time-consuming, and requires complex infrastructure. A single evaluation can cost thousands of dollars and take days to complete. In contrast, non-agentic LLM benchmarks that test individual capabilities (e.g., reasoning, code generation) are fast and cheap to run. In this paper, we investigate whether performance on expensive agentic benchmarks can be accurately predicted by the performance on a small, carefully selec...

---

### 32. EduArt: An educational-level benchmark for evaluating art history knowledge in large language models

**Authors:** Gianmarco Spinaci, Lukas Klic, Giovanni Colavizza

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02007v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02007v1)

**Summary:** Large language models now score near ceiling on general benchmarks, but these aggregate measures reveal little about how models behave within single disciplines. Existing art-focused evaluations rely on synthetic questions and rarely report item-level properties. This paper introduces EduArt, an educational-level benchmark for art-historical knowledge and visual reasoning in multimodal LLMs. EduArt comprises 871 human-authored questions from Italian secondary-school exercises and US Advanced Pla...

---

### 33. Using embeddings to predict spoken word duration and pitch in Mandarin monosyllabic words

**Authors:** Xiaoyun Jin, Mirjam Ernestus, R. Harald Baayen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02002v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02002v1)

**Summary:** Time-normalized f0 contours of Mandarin words in conversational speech have been shown to be predictable in part from their contextualized embeddings (CEs). The present study investigates whether CEs also predict spoken word duration for 7470 tokens of Mandarin monosyllabic CV words extracted from a Mandarin corpus of spontaneous speech. We show that CEs indeed are predictive for duration, above chance level, not only at the type level, but also at the level of individual tokens, as indicated by...

---

### 34. Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing

**Authors:** Siyuan Li, Youyuan Zhang, Ruitong Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01978v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01978v1)

**Summary:** Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, but rarely control the semantic boundary of each edit. Our pilot analyses of post-edit behaviors and internal neuronal activities reveal a scope gap behind reliable edits: instance-level success neither...

---

### 35. Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization

**Authors:** Jan Drchal

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01972v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01972v1)

**Summary:** Large language models (LLMs) are often asked to produce JSON conforming to a fixed schema, powering information extraction, tool calling, agentic planning, and knowledge-graph construction. Measuring how closely an output matches a gold reference is essential yet surprisingly hard: exact match is brittle, text similarity ignores structure, and an LLM judge is expensive, opaque, and non-deterministic. We address this with Object Aligner (OA), an open-source Python library that scores two JSON obj...

---

### 36. Towards a Phonology-Informed Evaluation of Multilingual TTS

**Authors:** Sneha Ray Barman, Neeraj Kumar Sharma, Shakuntala Mahanta

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01965v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01965v1)

**Summary:** Neural TTS systems can sound natural across languages, but naturalness does not guarantee the preservation of sound contrasts that distinguish words from their grammatical forms. Standard metrics like MOS do not test for this. We propose a classifier-based framework that audits TTS output against language-specific phonological patterns using human speech as a benchmark. Testing Assamese advanced tongue root (ATR) vowel harmony with Meta's MMS TTS, we show that a classifier trained on human speec...

---

### 37. Beyond Supervised Clarification: Input Rewriting with LLMs for Dialogue Discourse Parsing

**Authors:** Yiming Liu, Ziyue Zhang, Zhichao Xu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01964v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01964v1)

**Summary:** Rewriting inputs to improve frozen downstream models has become a common strategy in modern NLP pipelines. Prior work on incremental dialogue discourse parsing (DDP) shows that supervised clarification models can rewrite fragmentary or underspecified utterances, such as resolving ellipsis or references, to improve parsing accuracy. In this work, we revisit this idea under realistic deployment conditions, where no clarification supervision is available and the clarifier must rely on zero-shot pro...

---

### 38. NAVER LABS Europe Submission to the Instruction-following 2026 Short Track

**Authors:** Marcely Zanon Boito, Hemant Yadav, Jean-Luc Meunier, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01960v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01960v1)

**Summary:** In this paper, we describe NAVER LABS Europe's submission to the instruction-following speech processing short track at IWSLT 2026. We participate again in the constrained setting, developing systems capable of jointly performing ASR, ST, and SQA from English speech into Chinese, Italian, and German. Building on our previous submission, ranked first in last year's short track, we update our multi-stage training pipeline by replacing the speech projector with SpeechMapper, a method for learning a...

---

### 39. Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism

**Authors:** Minjong Cheon

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01951v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01951v1)

**Summary:** Large language models (LLMs) are increasingly consulted on contested scientific questions, raising the concern that they will sycophantically retreat from established consensus when a user signals doubt -- drifting toward a false balance that treats settled science as one view among several. We test this across three open instruction-tuned models (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B), three consensus-science domains (climate, vaccines, evolution), and single- and multi-turn settings, combining ...

---

### 40. PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation

**Authors:** Peng Yun, Shouwang Huang, Hao Li, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01938v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01938v1)

**Summary:** Manipulating fast and dynamically moving targets in unstructured 3D environments remains challenging for embodied AI. Existing visual-language-action models and world models struggle with accurate 3D geometry and physically meaningful forecasting. We propose PhysMani, a framework that couples a physics-principled 3D Gaussian world model with a future-aware action policy model. The world model learns a divergence-free Gaussian velocity field via online optimization for fast and physically grounde...

---

### 41. AIriskEval-edu: New Dataset for Risk Assessment in AI-mediated K-12 Educational Explanations

**Authors:** Javier Irigoyen, Roberto Daza, Francisco Jurado, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01934v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01934v1)

**Summary:** This work introduces AIriskEval-edu-db2, a new dataset designed to train and evaluate auditors based on LLMs for an explainable pedagogical risk assessment in instructional content for grades K-12. The dataset comprises 1,639 explanations from 170 curated ScienceQA questions, covering science, language arts, and social sciences. For each question, the dataset includes an explanation written by a human teacher alongside 11 explanations generated by LLM-simulated teacher profiles associated with d...

---

### 42. TUDUM: A Turkish-Thinking Reasoning Pipeline for Qwen3.5-27B

**Authors:** Baran Bingol, Bahaeddin Turkoglu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01927v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01927v1)

**Summary:** This paper presents TUDUM (Türkçe Düşünen Üretken Model), a project pipeline for adapting a Qwen-family 27B thinking model toward Turkish reasoning. The central problem is not only to answer Turkish prompts in Turkish, but to make the explicit reasoning trace itself Turkish. A thinking model may translate a Turkish prompt into an English-centered internal or visible scratchpad, solve the problem mostly in English, and only localize the final answer. TUDUM instead treats the generated <think>...<...

---

### 43. The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization Across Universal Dependencies

**Authors:** Kim Gerdes

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01899v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01899v1)

**Summary:** Dependency length minimization (DLM) is a well-documented processing universal, but previous studies report a single mean dependency distance (MDD) per language, obscuring variation across syntactic relation types. We analyze 122 languages in UD and SUD (version 2.17), showing that DLM operates on two distinct levels. Grammar-driven optimization targets functional dependencies (det, case, aux), which are universally short (mean 1.71, $σ$ = 0.33) and invariant across typologically diverse languag...

---

### 44. Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters

**Authors:** Tianjian Yang, Meng Li

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01893v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01893v1)

**Summary:** Speculative decoding accelerates autoregressive generation by drafting a block of tokens that the target model verifies left-to-right, committing only the longest accepted prefix. Block (DLM-style) drafters predict the whole block in parallel, which is fast but trained with a full-block cross-entropy that supervises every position against the gold continuation -- even though inference discards every token after the first rejection. Recent acceptance-aware objectives patch this by reweighting the...

---

### 45. PairCoder++: Pair Programming as a Universal Paradigm for Verified Code-Driven Multimodal and Structured-Artifact Generation

**Authors:** Junhao Chen, Xiang Li, Mingjin Chen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01883v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01883v1)

**Summary:** Code is the medium through which large language models generate structured artifacts: charts, scientific figures, vector graphics, CAD models, 3D scenes, and hardware designs are all produced by writing programs. In this regime single pass inference is brittle, because the compiler, renderer, or simulator that decides whether the artifact exists is invisible to the model. We present PairCoder, which grounds review in the toolchain and realizes it as two agent pair programming: a Driver agent wri...

---

### 46. SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use

**Authors:** Jiayin Zhu, Kelong Mao, Yudong Guo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01874v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01874v1)

**Summary:** Skills are becoming a reusable operational layer for LLM agents, encoding SOPs, domain rules, tool workflows, scripts, and validation routines. In realistic skill repositories, overlapping skills make reliable skill-use difficult. Final verifier success is too coarse for both evaluation and training, since an agent may pass through trial and error while selecting distractor skills, skipping required steps, composing workflows incorrectly or omitting final checks. We introduce SkillCoach, a self-...

---

### 47. Safety Targeted Embedding Exploit via Refinement

**Authors:** Joshua Adrian Cahyono

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01859v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01859v1)

**Summary:** Safety training for large language models (LLMs) is conducted predominantly in English, leaving uncertain how well safety mechanisms generalize to low-resource languages and mixed-language code-switching. We show that this creates an epistemic gap in which models confidently generate harmful responses for inputs that fall outside the distribution of their safety training. To study this phenomenon, we introduce STEER (Safety Targeted Embedding Exploit via Refinement), a gradient-guided attack tha...

---

### 48. Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts

**Authors:** Valentin J. J. Kreileder, Johannes Reisinger, Andreas Fischer

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01852v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01852v1)

**Summary:** Retrieval-Augmented Generation (RAG) systems use the question-answering capabilities of Large Language Models (LLMs) to access information outside their parameters. We evaluate if cluster-based semantic chunking improves retrieval and answer quality compared to fixed-size and recursive chunking evaluating on long, structured academic theses using the Retrieval Augmented Generation Assessment (RAGAs) framework. RAGAs based faithfulness shows limited reliability in this setup. Performance on fixed...

---

### 49. Non-synchronism in Global Usage of Research Methods in Library and Information Science from 1990 to 2019

**Authors:** Chengzhi Zhang, Liang Tian

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01833v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01833v1)

**Summary:** The global development of Library and Information Science (LIS) is influenced by various factors such as the economy, society, culture, discipline, tradition, and more. Consequently, the research methods of LIS vary greatly among countries. To better understand these differences, we conducted a study of 5,281 research papers from 81 countries published in internationally representative journals over the past thirty years. We manually annotated the research methods used in some articles through c...

---

### 50. Pre-Flight: A Benchmark for Evaluating Large Language Models on Aviation Operational Knowledge

**Authors:** Alex Brooker, Tim Hughes

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01829v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01829v1)

**Summary:** Large language models (LLMs) are increasingly proposed for aviation business operations, from documentation and training generation to customer facing assistants. General purpose benchmarks do not measure whether a model reasons safely and correctly about aviation specific operational knowledge, and the high stakes, regulated nature of the domain makes that gap consequential. We present Pre-Flight, an open source benchmark of 300 multiple choice questions drawn from international standards and a...

---

## cs.CV

**50 papers**

### 1. WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory

**Authors:** Hanlin Wang, Hao Ouyang, Qiuyu Wang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02517v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02517v1)

**Summary:** We present WorldDirector, a highly controllable video world model framework designed for persistent dynamic object memory and unrestricted viewpoint exploration. Unlike existing world models that entangle physical dynamics with pixel rendering and rely on continuous visual observation to sustain motion, our framework explicitly decouples semantic motion orchestration from visual generation. By leveraging an LLM to coordinate 3D trajectories with camera movements and subsequently employing these ...

---

### 2. Alignment Is All You Need For X-to-4D Generation

**Authors:** Qiaowei Miao, Kehan Li, Yawei Luo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02516v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02516v1)

**Summary:** Generative diffusion models excel at synthesizing high-quality images, videos, and 3D content under multimodal control. However, arbitrary user-defined modality-to-4D (X-to-4D) generation remains challenging due to the high cost of constructing diverse datasets and the limited scalability of existing methods. This paper presents Align4D, a flexible framework that translates any-modal input into coherent video-3D pairs, using video to guide 4D motion and 3D data to shape 4D geometry. Align4D intr...

---

### 3. PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

**Authors:** Haofei Xu, Rundi Wu, Philipp Henzler, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02515v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02515v1)

**Summary:** State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre...

---

### 4. From SRA to Self-Flow: Data Augmentation or Self-Supervision?

**Authors:** Dengyang Jiang, Mengmeng Wang, Harry Yang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02508v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02508v1)

**Summary:** Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different ...

---

### 5. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas

**Authors:** Yuxuan Li, Lingxi Xie, Xinyue Huo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02504v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02504v1)

**Summary:** Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integra...

---

### 6. Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots

**Authors:** Ling Xu, Chuyu Han, Borui Li, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02501v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02501v1)

**Summary:** Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on...

---

### 7. Seek to Segment: Active Perception for Panoramic Referring Segmentation

**Authors:** Song Tang, Shuming Hu, Xincheng Shuai, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02497v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02497v1)

**Summary:** Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruc...

---

### 8. Towards Robustness against Typographic Attack with Training-free Concept Localization

**Authors:** Bohan Liu, Wenqian Ye, Guangzhi Xiong, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02494v1)

**Summary:** Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability ...

---

### 9. Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning

**Authors:** Liyan Tang, Fangcong Yin, Greg Durrett

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02490v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02490v1)

**Summary:** Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement lear...

---

### 10. GeoMix: Descriptor-Free Visual Localization via Global Context and Multi-Detector Training

**Authors:** Yejun Zhang, Xinjue Wang, Zihan Wang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02486v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02486v1)

**Summary:** Descriptor-free visual localization eliminates high-dimensional descriptor storage, preserves scene privacy, and simplifies map maintenance, yet its accuracy still lags far behind descriptor-based pipelines. We identify this gap to insufficient geometric discriminability in geometry-only matching. Without visual appearance, current methods underutilize local geometry cues, lack the global context among keypoints, and overfit to a single keypoint detector. We further observe that descriptor-free ...

---

### 11. Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning

**Authors:** Xuehui Wang, Xuankun Yang, Wei Shen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02484v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02484v1)

**Summary:** Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware ...

---

### 12. EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$

**Authors:** Jingtao Xu, Zizhuo Lin, Jianwen Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02479v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02479v1)

**Summary:** While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods a...

---

### 13. Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment

**Authors:** Ziyao Wang, Maonan Wang, Yucheng He, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02471v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02471v1)

**Summary:** Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR approaches often prioritize visual realism while overlooking their impact on subsequent analytical tasks, leading to semantic drift and degraded downstream performance. To address this issue, we propose Geo-Anchored Cloud Removal (GACR), a unified framework that jointly ensures faithful reconstructio...

---

### 14. OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers

**Authors:** Donghyun Lee, Jitesh Chavan, Duy Nguyen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02461v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02461v1)

**Summary:** Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in...

---

### 15. MARVEL: Margin-Aware Robust von Mises-Fischer Expert Learning for Long-Tailed Out-of-Distribution Detection

**Authors:** A. S. Anudeep, Vaanathi Sundaresan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02435v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02435v1)

**Summary:** For clinical deployment, it is essential that automated diagnostic systems remain reliable when confronted with previously unseen cases, yet deep models routinely misclassify out-of-distribution (OOD) inputs with high confidence, underscoring the need for more robust OOD detection methods. Although substantial effort has been devoted to improving model robustness, most of the existing literature assumes balanced datasets, evaluates OOD detection on coarse or non-clinical OOD sources, or lacks co...

---

### 16. Self-Auditing Residual Drifting for Pathology-Preserving Accelerated Knee MRI

**Authors:** Qing Lyu, Jianxu Wang, Mohammad Kawas, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02428v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02428v1)

**Summary:** Accelerated magnetic resonance imaging reduces acquisition time, but reconstruction from undersampled k-space can blur diagnostically relevant structures or introduce failures that are not captured by global image metrics. We propose SA-RDM-DC, a Self-Auditing Residual generative Drifting Model with Data Consistency for accelerated knee MRI. The method adapts the newly proposed generative drifting paradigm to accelerated MRI by training a physics-conditioned drift field from the zero-filled reco...

---

### 17. Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs

**Authors:** Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02425v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02425v1)

**Summary:** Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment int...

---

### 18. Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing

**Authors:** Anqi Tang, Wenhao Sun, Zhaoqiang Liu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02421v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02421v1)

**Summary:** Text-guided image editing aims to modify visual content according to a target prompt while preserving the background. Recent inversion-free image editing frameworks such as FlowEdit have demonstrated strong editing capability without requiring inversion. Empirically, FlowEdit can achieve substantial semantic changes under appropriate hyperparameter settings. However, we observe that under certain global attribute shifts, the editing trajectory may not effectively move away from the source distri...

---

### 19. LIME: Learning Intent-aware Camera Motion from Egocentric Video

**Authors:** Boyang Sun, Jiajie Li, Yung-Hsu Yang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02417v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02417v1)

**Summary:** Autonomous robots often need to move their camera before they can act: to inspect an object, reveal an occluded region, or obtain a view that responds to a user's intent. While vision-language navigation translates instructions to base motion and vision-language-action policies map instructions to manipulation actions, language-conditioned camera motion remains comparatively underexplored as a first-class action. We formulate language-conditioned camera motion generation: given a current RGB obs...

---

### 20. Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments

**Authors:** Xianhui Meng, Zirui Song, Yuchen Zhang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02407v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02407v1)

**Summary:** Large Language Models (LLMs) have demonstrated remarkable capabilities in 3D indoor synthesis for Manhattan environments. However, existing methods often fail to capture plausible object layout patterns in non-Manhattan settings, primarily because they struggle to model non-orthogonal spatial relationships, leading to high geometric violations and low physical fidelity. To address this challenge, we propose SPG-Layout, a novel text-driven framework designed to generate physically plausible indoo...

---

### 21. Object-centric LeJEPA

**Authors:** Jakob Geusen, Ender Konukoglu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02404v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02404v1)

**Summary:** Image encoders trained with LeJEPA can deliver strong features for downstream tasks, but, like other image-level self-supervised methods, typically require large training datasets. Aligning representations at the level of objects rather than whole scenes promises greater data efficiency, but doing this in a completely self-supervised way, effectively jointly partitioning a scene and representing its objects, is unstable: the two are locked in a cyclic dependency, partitioning requires meaningful...

---

### 22. ACID: Action Consistency via Inverse Dynamics for Planning with World Models

**Authors:** Gawon Seo, Dongwon Kim, Suha Kwak

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02403v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02403v1)

**Summary:** Decision-time planning with action-conditioned world models has become a popular paradigm for embodied control. However, the standard planning cost judges a candidate solely by how close its predicted terminal state lies to the goal, leaving the realizability of the intermediate transitions unchecked -- a predicted trajectory can look convincing while the environment rollout drifts away from it. In this paper, we propose ACID, a decision-time planning framework that introduces cycle action consi...

---

### 23. Show Me Examples: Inferring Visual Concepts from Image Sets

**Authors:** Nick Stracke, Kolja Bauer, Stefan Andreas Baumann, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02402v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02402v1)

**Summary:** Vision-language models (VLMs) can follow complex textual instructions, yet they struggle to reason from purely visual context. In particular, current models fail to infer shared concepts from sets of example images and apply them to new inputs. We introduce Visual Concept Inference from Sets (VICIS), a task that evaluates this capability. Given a small context set of images sharing a concept and a query image, the model must generate new images that preserve the context-defined concept while rem...

---

### 24. Transformer Geometry Observatory TGO-II: Representational Similarity Observatory

**Authors:** Kaustubh Kapil, Kishor P. Upla

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02386v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02386v1)

**Summary:** While Vision Transformers have achieved remarkable success across computer vision and language applications, the geometric evolution of their internal representations throughout training remains insufficiently understood. Existing analyses primarily focus on attention mechanisms and downstream performance, leaving the evolution of representation geometry largely unexplored. In this work, we present Transformer Geometry Observatory-II (TGO-II), a representation geometry analysis framework designe...

---

### 25. Representation Distribution Matching for One-Step Visual Generation

**Authors:** Lan Feng, Wuyang Li, Eloi Zablocki, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02375v1)

**Summary:** We elucidate the design space of Representation Distribution Matching (RDM), our name for the paradigm that trains a one-step image generator by matching generated and reference feature distributions under frozen pretrained encoders. We identify two design axes, how the distributions are compared and the representations they are compared in, and controlled studies along them yield three findings. First, the classical MMD, which could not train convincing generators a decade ago, becomes a strong...

---

### 26. Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis

**Authors:** Federico Lincetto, Gianluca Agresti, Mattia Rossi, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02372v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02372v1)

**Summary:** Neural rendering techniques allow for accurate reconstruction of the geometry and color appearance of 3D scenes. Some methods have extended their use to additional imaging modalities, such as multispectral, infrared, or polarimetric data. However, all of these approaches require expensive sensors and calibrated setups to capture new multimodal frames for each new scene. We propose Spectral and Polarimetric Implicit Learned Representation (SPoILeR), a novel method to obtain multi-view consistent ...

---

### 27. VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval

**Authors:** Cristian-Gabriel Florea, Stelian Spînu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02371v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02371v1)

**Summary:** Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time v...

---

### 28. GAP-GDRNet: Geometry-Aware Monocular Visual Pose Sensing on a Single-Target Synthetic Spacecraft Dataset

**Authors:** Yonglong Zhang, Yang Liu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02360v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02360v1)

**Summary:** Monocular relative pose sensing is a central perception problem in non-cooperative rendezvous and on-orbit servicing. In spacecraft images, however, weak surface texture, thin appendages, illumination changes, and partial occlusion often leave only sparse and unstable geometric evidence. This article presents GAP-GDRNet, a geometry-aware attention-enhanced framework for monocular RGB-based 6D pose sensing. The method follows the geometry-guided direct regression paradigm of GDR-Net and modifies ...

---

### 29. The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection

**Authors:** Jincheng Tang, Yilong Zhu, Zhengyuan Xie, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02322v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02322v1)

**Summary:** Vision-Language-Action (VLA) models have shown remarkable promise in generalized robotic manipulation. However, their spatial generalization remains fragile. We argue that simply increasing the number of viewpoints is insufficient. Models often fall into the trap of Shortcut Learning, latching onto spurious correlations (e.g., fixed relative poses between objects or between the camera and robot base) rather than learning true spatial relationships. In this work, we propose a data-centric solutio...

---

### 30. NEvo: Neural-Guided Evolutionary Video Synthesis for Dynamic Visual Selectivity

**Authors:** Yingtian Tang, Sogand Salehi, Ming Zhou, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02317v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02317v1)

**Summary:** The human brain processes dynamic visual input through hierarchically organized, functionally specialized regions. While recent in silico brain encoding models can synthesize optimal stimuli to probe selectivity in different brain regions, prior work has been largely limited to static images, leaving dynamic visual processing underexplored. We introduce a novel neural-guided video synthesis framework that generates stimuli optimized for target brain regions across visual cortex. Our method perfo...

---

### 31. InvSplat: Inverse Feed-Forward Scene Splatting

**Authors:** Polina Karpikova, Wenjing Bian, Haofei Xu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02301v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02301v1)

**Summary:** Inverse rendering aims to recover both 3D geometry and physically meaningful material properties from images, enabling applications such as relighting and novel view synthesis. Optimization-based methods achieve high fidelity but require costly per-scene fitting, while image-space learning-based approaches often suffer from multi-view inconsistencies and lack an explicit 3D representation for stable novel view rendering. We present a feed-forward multi-view reconstruction framework for inverse r...

---

### 32. Search-based Testing of Vision Language Models for In-Car Scene Understanding

**Authors:** Lev Sorokin, Chen Yang, Ken E. Friedl, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02300v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02300v1)

**Summary:** In the automotive domain, in-car scene understanding (ISU) enables the detection of safety-critical events, such as driver distraction, and supports drivers or passengers by analyzing the in-car scene and adapting the environment (e.g., ambient lighting). The industry is increasingly exploring vision-language models (VLMs) to interpret camera-recorded in-car scenes and extract information for downstream reasoning tasks. However, VLMs may generate incomplete, erroneous, or misleading scene descri...

---

### 33. Dual-Selective Network for Domain-Incremental Change Detection

**Authors:** Yuzhi He, Junxi Huang, Haorui Wu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02299v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02299v1)

**Summary:** Domain-incremental change detection (DICD) continuously adapts models to new geographic domains while preserving prior knowledge. However, a structural mismatch exists: the label space remains fixed while domain characteristics vary drastically. Consequently, incremental models struggle to maintain stable spatial change representations across domains. Existing strategies, such as replay-based or regularization-based methods, often fail to scale to long domain sequences, leading to knowledge degr...

---

### 34. Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation

**Authors:** Andrei-Marian Ungureanu, Stelian Spînu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02298v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02298v1)

**Summary:** Autonomous drones are rapidly transforming modern warfare and civil applications alike. This paper presents the development of an integrated intelligent drone system designed to serve as a personal assistant. Leveraging the DJI Tello drone platform, we implemented a modular architecture that integrates three core artificial intelligence functionalities: facial detection, facial recognition, and depth estimation from monocular vision. A web-based interface enables seamless drone control and real-...

---

### 35. Optimizing Visual Generative Models via Distribution-wise Rewards

**Authors:** Ruihang Li, Mengde Xu, Shuyang Gu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02291v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02291v1)

**Summary:** Conventional reinforcement learning strategies for visual generation typically employ sample-wise reward functions, yet this practice frequently results in reward hacking that degrades image diversity and introduces visual anomalies. To address these limitations, we present a novel framework that finetunes generative models using distribution-wise rewards, ensuring better alignment with real-world data distributions. Unlike rewards that evaluate samples individually, distribution-wise reward acc...

---

### 36. DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing

**Authors:** Zhaokai Wang, Mingxin Liu, Zirun Zhu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02290v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02290v1)

**Summary:** Recent image generation and editing models can produce visually appealing natural images, yet they remain unreliable when the target image is a knowledge-intensive diagram whose correctness depends on disciplinary concepts, symbolic structure, and precise spatial relations. We introduce DisciplineGen-1M, a million-scale multidisciplinary dataset that supports text-to-image generation and image editing. It contains 1.2M samples spanning mathematics, physics, chemistry, biology, geography, compute...

---

### 37. FlowCIR: Semantic Transport via Flow Matching for Zero-Shot Composed Image Retrieval

**Authors:** Zhenqi He, Ziqi Jiang, Yuanpei Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02284v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02284v1)

**Summary:** Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image by editing a reference image with a natural-language instruction, without relying on domain-specific annotated triplets. Most existing ZS-CIR methods rely on textual inversion to translate the reference image into pseudo-text tokens and then compose them with the instruction via simple concatenation in the text space, which can be lossy and brittle for fine-grained semantics. In this work, we propose a new paradigm, name...

---

### 38. AGVBench: A Reliability-Oriented Benchmark of Data Augmentation for Vein Recognition

**Authors:** Haiyang Li, Yuming Fu, Qun Song, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02271v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02271v1)

**Summary:** Vein recognition is a secure biometric technology often constrained by limited annotated data and imaging variations. While data augmentation mitigates this, strategies designed for natural images may disrupt the fine-grained topology and textures essential for identity discrimination. We present AGVBench, which evaluates 30 representative augmentation strategies on five public palm- and finger-vein datasets with seven backbone architectures, covering classic CNNs, vision transformers, and vein-...

---

### 39. AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language Models

**Authors:** Rintaro Otsubo, Ryo Fujii, Reina Ishikawa, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02269v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02269v1)

**Summary:** Vision-Language Models (VLMs) have demonstrated immense promise in Spatio-Temporal Video Grounding (STVG). However, current evaluation protocols are largely confined to zero-shot assessments on general, daily-life benchmarks. This creates a critical disconnect from real-world applications in specialized fields, where models inevitably encounter rare visual concepts and complex spatio-temporal dynamics. Since exhaustive pre-training across infinite data distributions is infeasible, the ability to...

---

### 40. ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection

**Authors:** Ningning Han, Lei Fan, Jia Guo, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02252v1)

**Summary:** The deployment of Industrial Anomaly Detection (IAD) in real-world manufacturing frequently encounters a challenging cold-start bottleneck, in which limited normal samples fail to represent the full normal distribution and only a few anomalies are available. Under such a regime, existing methods struggle to form compact normal boundaries and fail to effectively exploit supervised signals from rare defects. To address this challenge, we propose Anomaly-Rectified Cold-start AD (ArcAD), a plug-and-...

---

### 41. When Token Compression Breaks: Structural Pruning vs. Token Reduction for Robust ViT Segmentation under High Compression

**Authors:** Tien-Phat Nguyen, Ngai-Man Cheung

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02237v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02237v1)

**Summary:** Vision Transformers (ViTs) are strong backbones for semantic segmentation, but their computational cost limits deployment. Recent token compression methods for efficient transformer-based segmentation reduce this cost by decreasing the number of tokens. However, existing evaluations primarily focus on low-to-moderate compression, leaving their behavior under aggressive compression and corrupted inputs unclear. Meanwhile, structural pruning provides an orthogonal route to efficiency by removing r...

---

### 42. Efficient Waste Sorting for Circular Economy: A Confidence-guided comparison between One-Vs-All and One-Vs-Rest Classification Strategies with Human-in-the-Loop for Automated Waste Sorting

**Authors:** Mohammed Fahad Ali, Dominique Briechle, Marit Briechle-Mathiszig, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02230v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02230v1)

**Summary:** The complexity of waste disposal regulations across European countries poses significant challenges for the residents and hinders the transition to a Circular Economy. In Germany, the proper sorting and disposal of household waste remains challenging across municipalities. Consequently, substantially reducing incorrectly disposed waste is vital for improving waste management and advancing the Circular Economy. AI-based waste sorting solutions can support residents through user-friendly tools, su...

---

### 43. DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation

**Authors:** Zijun Li, Yimin Zhou, Jia Sun, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02220v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02220v1)

**Summary:** Diffusion-based generative AI has achieved remarkable success in e-commerce applications such as virtual try-on, poster generation, and product background synthesis. However, when making online purchasing decisions for apparel, consumers also desire the freedom to examine specific detail regions of interest, such as collars, cuffs, and fabric textures, yet existing methods have not explicitly studied this setting. We therefore formalize a new, non-template task: Fashion Detail Generation with fo...

---

### 44. MedSaab-US: A Backpropagation-Free Multi-Scale Wavelet-Saab Framework for Thyroid Nodule Segmentation in Ultrasound Images

**Authors:** Mohammad Amanour Rahman

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02209v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02209v1)

**Summary:** Deep learning (DL) methods dominate thyroid nodule segmentation in ultrasound (US) images, achieving high Dice scores but at the cost of millions of parameters, GPU-dependent training via backpropagation, and limited mathematical tractability. These limitations impede deployment in resource-constrained environments. In this paper, we propose MedSaab-US, a backpropagation-free segmentation framework grounded in the Green Learning paradigm. MedSaab-US extracts multi-scale spatial-frequency feature...

---

### 45. RadiomicNet: A Hybrid Radiomics-Guided Lightweight Architecture for Interpretable Medical Image Segmentation

**Authors:** Mohammad Amanour Rahman

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02185v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02185v1)

**Summary:** Deep learning has achieved remarkable performance in medical image segmentation, yet it suffers from critical limitations: mathematical intractability, substantial parameter requirements, and lack of clinical interpretability. We propose RadiomicNet, a novel two-stream hybrid architecture that enhances standard deep learning by integrating handcrafted radiomics features directly into the segmentation learning process. The key contribution is the Radiomics Attention Gate (RAG), which leverages Gr...

---

### 46. Efficient PEFT Methods with Adaptive Checkpointing for Vision Models and VLMs on Resource Constrained Consumer-GPUs

**Authors:** Altay Toktassyn, Jurn-Gyu Park

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02158v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02158v1)

**Summary:** Modern pretrained vision models achieve strong accuracy but demand substantial GPU memory for fine-tuning, making edge deployment impractical. This paper compares five parameter-efficient fine-tuning (PEFT) methods (Full FT, LoRA, AdaLoRA, QLoRA, BitFit) on Transformers- (ViT-Small, TinyViT) and Mamba-based vision backbones (Vim-Small, MambaVision-T) under an on-device VRAM budget (e.g., 2 GB), together with three gradient-checkpointing strategies (none, static, and a proposed memory-budget-awar...

---

### 47. Patient-Specific Articulated Digital Twins from a Single Full-Body CT Scan

**Authors:** Han Zhang, Boyang Zhao, Mathias Unberath

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02156v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02156v1)

**Summary:** Patient-specific anatomical models provide individualized context for surgical planning, image-guided intervention, and algorithm development. However, most CT-derived models are static: they preserve the body configuration captured at scan time, but cannot represent how the same anatomy would appear after patient repositioning. This limitation is especially important for radiographic imaging, where appearance depends jointly on imaging geometry and patient pose. We present a proof-of-concept fo...

---

### 48. SAMoR: Motion Modelling for Articulated Objects of Any Skeleton and Topology

**Authors:** Yuhao Zhang, Gerard Pons-Moll, Tolga Birdal

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02148v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02148v1)

**Summary:** Modeling motion for articulated objects of arbitrary skeleton topology remains difficult: existing motion generators target a fixed human skeleton, and prior adaptations either fail to share a vocabulary across rigs or discard motion detail through global pooling. Our key observation is that while joint-level motion does not correspond cleanly across species, motion of functional joint groups does: a human arm, a wolf foreleg, and a bird wing share motion structure despite differing joint counts...

---

### 49. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 50. AdaCount: Training-Free Similarity-Guided Spatial and Feature Adaptation for Zero-Shot Object Counting

**Authors:** Muhammad Ibraheem Siddiqui, Muhammad Haris Khan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02139v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02139v1)

**Summary:** Zero-shot object counting (ZOC) aims to count instances of arbitrary object categories specified only through textual prompts. Recent training-free approaches leverage foundation models such as SAM to reformulate counting as a prompt-driven segmentation task, eliminating the need for costly counting-specific training data with point-level annotations. More recently, SAM3 introduced promptable concept segmentation, enabling the zero-shot segmentation of all instances corresponding to a text-defin...

---

## cs.LG

**50 papers**

### 1. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning

**Authors:** Matteo Boglioni, Thibault Rousset, Siva Reddy, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02513v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02513v1)

**Summary:** LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's...

---

### 2. Program-as-Weights: A Programming Paradigm for Fuzzy Functions

**Authors:** Wentao Zhang, Liliana Hotsko, Woojeong Kim, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02512v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02512v1)

**Summary:** Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P...

---

### 3. Online Safety Monitoring for LLMs

**Authors:** Mona Schirmer, Metod Jazbec, Alexander Timans, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02510v1)

**Summary:** Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...

---

### 4. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates

**Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02507v1)

**Summary:** LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR resp...

---

### 5. DemoPSD: Disagreement-Modulated Policy Self-Distillation

**Authors:** Yunhe Li, Hao Shi, Wenhao Liu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02502v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02502v1)

**Summary:** On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamenta...

---

### 6. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials

**Authors:** Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02499v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02499v1)

**Summary:** Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general models, the choice of optimizer for training has largely remained unexplored, defaulting to Adam and its variants in the community. Here, we implement and systematically compare a class of recently proposed matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training Nequ...

---

### 7. Controllable Sim Agents with Behavior Latents

**Authors:** Juanwu Lu, Junyu Zhu, Ziran Wang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02496v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02496v1)

**Summary:** Realistic traffic simulation requires agents that imitate logged behavior and can also be steered along interpretable axes. Such controllability enables engineers to isolate variables, reproduce specific edge cases, and test autonomous systems without real-world risk. We introduce Controllable Neural Variational Agents (CNeVA), a controllable simulated-agent framework that learns to infer a per-agent Gaussian behavior latent from per-channel discounted returns via a closed-form conjugate variati...

---

### 8. OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers

**Authors:** Donghyun Lee, Jitesh Chavan, Duy Nguyen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02461v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02461v1)

**Summary:** Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in...

---

### 9. Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation

**Authors:** Zhuowei Chen, Xiang Lorraine Li

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02460v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02460v1)

**Summary:** Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these appr...

---

### 10. Understanding the Robustness of Distributed Self-Supervised Learning Frameworks Against Non-IID Data

**Authors:** Xuanyu Chen, Nan Yang, Shuai Wang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02447v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02447v1)

**Summary:** Recent research has introduced distributed self-supervised learning (D-SSL) approaches to leverage vast amounts of unlabeled decentralized data. However, D-SSL faces the critical challenge of data heterogeneity, and there is limited theoretical understanding of how different D-SSL frameworks respond to this challenge. To fill this gap, we present a rigorous theoretical analysis of the robustness of D-SSL frameworks under non-IID (non-independent and identically distributed) settings. Our results...

---

### 11. Optimal Stabilizer Testing and Learning with Limited Quantum Memory

**Authors:** Srinivasan Arunachalam, Louis Schatzki

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02444v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02444v1)

**Summary:** We study stabilizer state testing and learning with limited coherent quantum memory. Here an algorithm sequentially receives copies of an unknown $n$-qubit state, but may keep only $k$ qubits of coherent quantum memory between measurements. With unrestricted memory, seminal work of Gross, Nezami and Walter showed how to test $n$-qubit stabilizer states using $6$ copies, which is dimension independent, unlike the learning complexity of $Θ(n)$. We show that this testing-vs-learning separation is l...

---

### 12. Extreme Adaptive Transformer for Time Series Forecasting

**Authors:** Sanjeev Shrestha, Hui Liu, Yifan Zhang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02437v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02437v1)

**Summary:** Time series forecasting remains challenging when the underlying data contain rare but critical extreme events. This issue is particularly important in hydrologic forecasting, where streamflow distributions are often highly skewed and extreme peaks can have substantial impacts on flood monitoring, water resource management, and early warning systems. Although Transformer-based forecasting models have achieved strong performance by modeling long-range temporal dependencies, they typically treat al...

---

### 13. QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition

**Authors:** Quoc Bao Phan, Tuy Tan Nguyen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02426v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02426v1)

**Summary:** Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid qu...

---

### 14. Neuron-Aware Active Few-Shot Learning for LLMs

**Authors:** Zhuowei Chen, Liwei Chen, Christian Schunn, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02423v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02423v1)

**Summary:** Active Few-Shot Learning (AFSL) adapts LLMs to specialized domains by identifying the most valuable unlabeled samples for annotation and use as few-shot demonstrations, effectively reducing human annotation costs while promoting high performance. However, existing methods typically rely on output-level signals for sample identification, such as predictive entropy or semantic similarities with test-time data based on external embeddings, which often overlook models' internal dynamics, which could...

---

### 15. LIME: Learning Intent-aware Camera Motion from Egocentric Video

**Authors:** Boyang Sun, Jiajie Li, Yung-Hsu Yang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02417v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02417v1)

**Summary:** Autonomous robots often need to move their camera before they can act: to inspect an object, reveal an occluded region, or obtain a view that responds to a user's intent. While vision-language navigation translates instructions to base motion and vision-language-action policies map instructions to manipulation actions, language-conditioned camera motion remains comparatively underexplored as a first-class action. We formulate language-conditioned camera motion generation: given a current RGB obs...

---

### 16. Q-GAIN: A Python Package for Machine Learning and Physically Informed Analysis Applications

**Authors:** M. Doris, S. Guo, S. M. Koh, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02413v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02413v1)

**Summary:** Here we describe the quantum gas analysis and inference (Q-GAIN) Python package, which enables rapid deployment of machine learning (ML) and physics-informed analysis techniques for cold-atom experiments. Out of the box, Q-GAIN implements classification, object detection, and physics-informed metrics for feature detection in images of atomic Bose-Einstein condensates (BECs). Q-GAIN encourages a natural, module-based workflow: starting with data loading and preprocessing, followed by ML-based fea...

---

### 17. Object-centric LeJEPA

**Authors:** Jakob Geusen, Ender Konukoglu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02404v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02404v1)

**Summary:** Image encoders trained with LeJEPA can deliver strong features for downstream tasks, but, like other image-level self-supervised methods, typically require large training datasets. Aligning representations at the level of objects rather than whole scenes promises greater data efficiency, but doing this in a completely self-supervised way, effectively jointly partitioning a scene and representing its objects, is unstable: the two are locked in a cyclic dependency, partitioning requires meaningful...

---

### 18. Fast Multi-dimensional Refusal Subspaces via RFM-AGOP

**Authors:** Thomas Winninger

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02396v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02396v1)

**Summary:** Steering and monitoring activations in Large Language Models (LLMs) are increasingly used for both safety and interpretability. Early work assumed behaviours are encoded along single linear directions, but recent findings suggest complex behaviours, such as the refusal to answer harmful queries, live in multi-dimensional subspaces. However, existing methods for extracting these subspaces are computationally expensive, which becomes prohibitive on reasoning models who produce long reasoning trace...

---

### 19. WattGPU: Predicting Inference Power and Latency on Unseen GPUs and LLMs

**Authors:** Mauricio Fadel Argerich, Jonathan Fürst, Marta Patiño-Martínez

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02391v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02391v1)

**Summary:** Large Language Model (LLM) inference workloads are a rapidly growing contributor to data center energy consumption. Optimizing these deployments requires matching specific LLMs to the most efficient GPUs, but operators currently lack the tools to do so without exhaustively profiling each combination. While some predictive models exist, they still require profiling data and struggle to generalize to hardware unseen during training. To address this, we introduce \textit{WattGPU}, featuring two pre...

---

### 20. DecompRL: Solving Harder Problems by Learning Modular Code Generation

**Authors:** Juliette Decugis, Fabian Gloeckle, Francis Bach, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02390v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02390v1)

**Summary:** How can Large Language Models (LLMs) solve problems they currently cannot? Repeated sampling scales test-time compute but GPU cost grows linearly with attempts, while reinforcement learning (RL) with verifiable rewards improves single-attempt accuracy at the expense of sample diversity. Both strategies ultimately fail when the base policy has near-zero probability of producing a correct solution: no amount of sampling or gradient signal can overcome a search space that is simply too large. We ta...

---

### 21. Bringing Agentic Search to Earth Observation Data Discovery

**Authors:** Minghan Yu, Youran Sun, Chugang Yi, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02387v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02387v1)

**Summary:** NASA and its data centers hold thousands of geoscience datasets and tools like Worldview, Giovanni, the Science Discovery Engine, and Harmony. Finding the right one is hard even for domain experts. We present an agentic search system, deployed as a public service for the geoscience community, that takes a natural-language research query and returns the matching datasets and tools. We demonstrate that, in the era of large language models, the latent value of knowledge graphs (KGs) can be substant...

---

### 22. Transformer Geometry Observatory TGO-II: Representational Similarity Observatory

**Authors:** Kaustubh Kapil, Kishor P. Upla

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02386v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02386v1)

**Summary:** While Vision Transformers have achieved remarkable success across computer vision and language applications, the geometric evolution of their internal representations throughout training remains insufficiently understood. Existing analyses primarily focus on attention mechanisms and downstream performance, leaving the evolution of representation geometry largely unexplored. In this work, we present Transformer Geometry Observatory-II (TGO-II), a representation geometry analysis framework designe...

---

### 23. The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent Geometry

**Authors:** Yuan Yuan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02368v1)

**Summary:** Evaluations of LLM personas via psychometric questionnaires typically rely on aggregate scores, discarding within-instance correlation structure. We test whether this geometric structure is intrinsic or frame-dependent. Constructing within-instance correlation matrices from IPIP-50 responses, we analyze geometry on SPD manifolds under manipulated question orderings in GPT-4o simulating American and Chinese-American personas. We find that persona expression comprises two dissociable components: a...

---

### 24. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 25. Self-Gating Attention for Efficient Time Series Forecasting

**Authors:** Dezheng Wang, Tong Chen, Wei Yuan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02344v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02344v1)

**Summary:** Transformer architectures have shown strong potential in time series forecasting, where multi-head self-attention is widely used to capture temporal dependencies across historical timestamps. However, standard self-attention has quadratic time and memory complexity with respect to the look-back length. This cost may limit its use in resource-constrained or high-throughput forecasting systems, where fast and memory-efficient inference is important. Through qualitative and quantitative analyses, w...

---

### 26. HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report

**Authors:** Minghao Li, Raghav Mittal, Sanjivni Rana, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02338v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02338v1)

**Summary:** Hierarchical Navigable Small World (HNSW) graphs serve as the industry standard due to their logarithmic complexity and strong empirical performance. However, HNSW relies on greedy graph traversal, a heuristic that provides no theoretical guarantees of correctness. In this paper, we propose a novel "Certify-then-Rectify" framework that bridges the gap between the speed of heuristic search and the rigor of exact retrieval. Rather than discarding HNSW, our approach first employs a distribution-fre...

---

### 27. On the Role of Directionality in Structural Generalization

**Authors:** Zichao Wei

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02307v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02307v1)

**Summary:** Several SLOG test categories explicitly involve directional distinctions (modifier position shifts, argument extraction positions), yet AM-Parser, the previous SOTA, uses an AM algebra whose operations do not encode direction. We redesign the symbolic backend around CCG directed types (deterministic CKY + single linear decoder, 30K learnable parameters). Under the same BERT-base encoder, the system achieves 75.9$\pm$6.4% LF exact match, surpassing AM-Parser (70.8$\pm$4.3%). Per SLOG's own catego...

---

### 28. One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective

**Authors:** Juan Agustín Duque, Sergio García Heredia, Vinicius Hernandes, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02292v1)

**Summary:** Neural quantum states (NQS) provide a flexible and scalable framework for approximating quantum many-body wavefunctions. Among NQS parameterizations, autoregressive models are especially attractive because they enable exact, independent sampling from the Born distribution, avoiding the autocorrelation and mixing issues of Markov chain methods. Yet their optimization remains comparatively underexplored: Adam is a scalable method but ignores function space geometry, while stochastic reconfiguratio...

---

### 29. Optimizing Visual Generative Models via Distribution-wise Rewards

**Authors:** Ruihang Li, Mengde Xu, Shuyang Gu, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02291v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02291v1)

**Summary:** Conventional reinforcement learning strategies for visual generation typically employ sample-wise reward functions, yet this practice frequently results in reward hacking that degrades image diversity and introduces visual anomalies. To address these limitations, we present a novel framework that finetunes generative models using distribution-wise rewards, ensuring better alignment with real-world data distributions. Unlike rewards that evaluate samples individually, distribution-wise reward acc...

---

### 30. Generalization in offline RL: The structure is more important than the amount of pessimism

**Authors:** Max Weltevrede, Matthijs T. J. Spaan, Wendelin Böhmer

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02288v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02288v1)

**Summary:** While pessimism counteracts overestimation bias in offline reinforcement learning (RL), being overly conservative has been associated with hindering certain forms of generalization. However, in this paper we demonstrate that being overly pessimistic does not inherently prevent optimal generalization in contextual MDPs (CMDPs). Instead, we argue successful generalization depends not on the amount of pessimism, but whether the pessimistic structure respects the underlying symmetries of the optimal...

---

### 31. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**Authors:** Juwei Shen, Yujie Wu, Changwen Chen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02283v1)

**Summary:** In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs. Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions. We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewin...

---

### 32. HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures

**Authors:** Ziyun Qiao, Yue Min, Ruining Chen, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02266v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02266v1)

**Summary:** Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Tr...

---

### 33. Aggregation with Exponential Weights is Optimal in Expectation

**Authors:** Mikael Møller Høgsgaard, Patrick Rebeschini, Tobias Wegel

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02247v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02247v1)

**Summary:** The aggregation with exponential weights (AEW) estimator is not fully understood in the basic setting of model selection aggregation with squared loss. In particular, whether it is minimax-rate optimal in expectation for large enough fixed temperatures and under random design has been an open problem since its introduction, which was explicitly posed by Lecué and Mendelson (2013). In this paper, we settle this problem by showing that \emph{without} requiring a Bernstein-type assumption, the AEW ...

---

### 34. Purified OPSD: On-Policy Self-Distillation Without Losing How to Think

**Authors:** Zhanming Shen, Jintao Tong, Shaotian Yan, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02234v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02234v1)

**Summary:** On-policy self-distillation (OPSD) has emerged as a promising paradigm for improving LLM reasoning, where a privileged teacher with access to reference solutions provides token-level supervision on the student's own generated trajectories. However, we find that OPSD consistently fails on long chain-of-thought (long-CoT) reasoning models, yielding at best marginal gains while destabilizing the reflective reasoning capability these models depend on. Through a novel decomposition of the teacher's s...

---

### 35. An Additive MLP-GNN Framework for Characterizing Chemical and Structural Contributions to Aqueous Solubility

**Authors:** Sampreeti Bhattacharya, Arkaprava Roy

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02212v1)

**Summary:** Aqueous solubility is a key property in early-stage drug discovery, but most predictive models merge physicochemical descriptors and molecular graph information into a single representation, obscuring whether a prediction is driven by global chemistry, molecular structure, or both. We present an additive deep-learning framework that keeps these two sources of information separate throughout training: physicochemical descriptors are encoded by a multilayer perceptron (the chemical branch) and mol...

---

### 36. Prediction Sets for Counterfactual Decisions: Coverage, Optimality, and Conformal Prediction

**Authors:** Yurui Zheng, Ying Jin

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02206v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02206v1)

**Summary:** Predictions are increasingly used to guide high-stakes decisions, from treatment selection to policy making. To ensure reliability with imperfect predictions, uncertainty quantification methods such as conformal prediction build prediction sets with coverage guarantees. However, statistical validity alone does not immediately determine the decisions to take, nor the optimality thereof. This gap is especially delicate in counterfactual settings where the outcome that materializes depends on the a...

---

### 37. Self-explainable Operator Learning for Discovering Spatial Patterns in Functional Data

**Authors:** Mojgan Alishiri, Amirhossein Arzani

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02203v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02203v1)

**Summary:** Operator learning has emerged as a powerful tool for modeling complex physical systems in functional spaces. However, their neural network-based architectures make them opaque models, obscuring the reasoning behind their predictions. In this work, we introduce a self-explainable operator learning framework that overcomes this challenge by reformulating operator learning as a linear combination of generalized functional linear models expressed through integral equations. Exploiting the additive d...

---

### 38. Fourier Preconditioning for Neural Feature Learning

**Authors:** Preston Pitzer, Anish Pradhan, Harpreet S. Dhillon

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02199v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02199v1)

**Summary:** Mutual information (MI)-inspired feature learning techniques are capable of generating low-dimensional embeddings that retain nonlinear dependence structures, but direct estimations of MI suffer from noisy probability distribution estimates in the low-data regime. The H-Score objective, computed from second-order statistics, provides a practical proxy metric for training feature extraction networks. We prove that H-Score is invariant to invertible transformations in the unrestricted functional s...

---

### 39. Online Resource Allocation with Continuous Random Consumption: Regret under Degeneracy

**Authors:** Jiawei Zhang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02196v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02196v1)

**Summary:** We study online resource allocation when both rewards and consumption sizes may be continuously distributed. Requests arrive sequentially and must be accepted or rejected irrevocably under fixed resource capacities. Each request belongs to one of finitely many observable types; conditional on an observable request type, both the reward and the scalar size are random, and the realized size scales a fixed type-specific resource-consumption vector. The model allows the deterministic fluid relaxatio...

---

### 40. An Optimisation Framework for the Well-Conditioned Training of Physics-Informed Neural Networks

**Authors:** Joseph Webb, Sadok Jerad, Coralia Cartis

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02194v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02194v1)

**Summary:** Physics-informed neural networks (PINNs) have emerged as a promising route to solve partial differential equations, yet they have struggled to reach the precision of classical solvers. The obstacle is increasingly understood to be one of optimisation, owing to the severely ill-conditioned loss landscape. We present $\textbf{DSGNAR}$: Doubly-Sketched Gauss-Newton with Adaptive Ratio, a scalable second-order optimisation framework that confronts this ill-conditioning and, in doing so, obtains unpr...

---

### 41. Privacy-Preserving and Verifiable Approximate Distributed Coded Computing

**Authors:** Xavier Martínez-Luaña, Alba Gude-Santos, Manuel Fernández-Veiga, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02187v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02187v1)

**Summary:** Distributed machine learning enables collaborative model training without centralizing data, but it also exposes learning processes to privacy leakage and malicious manipulation. Existing defenses typically address these threats in isolation and are often tailored to specific learning paradigms or model architectures, limiting their applicability in realistic deployments. In particular, federated learning and decentralized learning exhibit distinct adversarial surfaces that are rarely addressed ...

---

### 42. Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation

**Authors:** Jijie Zhang, Zhe Ren, Quan Zhang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02182v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02182v1)

**Summary:** Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially ag...

---

### 43. A rubric-based controlled comparison of frontier language models on expert-authored clinical reasoning tasks

**Authors:** Samiha A. Ismail, Fan X. Chen, Ali Merali

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02175v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02175v1)

**Summary:** Multiple-choice medical benchmarks are increasingly saturated, and recent rubric-based evaluations such as HealthBench have shown that open-ended clinical performance is far from solved - its "Hard" subset top score remains 32%. We present a small, deliberately difficult evaluation dataset of five clinician-authored clinical scenarios spanning four specialties (anaesthesia, internal/family medicine, emergency medicine, and obstetrics), each accompanied by an atomic, weighted, MECE rubric (25-62 ...

---

### 44. Dynamic Neural Graph Encoding of Inference Processes in Deep Weight Space

**Authors:** Di Wu, Huan Liu, Zhixiang Chi, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02166v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02166v1)

**Summary:** The rapid advancements in using neural networks as implicit data representations have attracted significant interest in developing machine learning methods that analyze and process the weight spaces of other neural networks. However, efficiently handling these highdimensional weight spaces remains challenging. Existing methods often overlook the sequential nature of layer-by-layer processing in neural network inference. In this work, we propose a novel approach using dynamic graphs to represent ...

---

### 45. Tight Lower Bounds for the Multi-Secretary Problem via Bellman Certificates

**Authors:** Jiawei Zhang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02150v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02150v1)

**Summary:** This paper studies additive regret in the multi-secretary problem, defined as the gap between the expected offline prophet reward and the reward of the best online policy. Prior work established \(O(\log T)\) regret for bounded-density distributions with connected support and \(O((\log T)^2)\) upper bounds for bounded-density distributions with support gaps. It was unknown whether the extra logarithmic factor is necessary even in the one-resource model. We prove that it is necessary. For a mixtu...

---

### 46. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 47. Probing Chemical Language Models: Effects of Pre-training and Fine-tuning

**Authors:** Anna Karnysheva, Dietrich Klakow, Ji-Ung Lee

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02140v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02140v1)

**Summary:** Chemical language models (CLMs) are trained with linearized representations such as SMILES, yet it remains unclear which chemically meaningful substructures they encode. To foster a better understanding of CLMs, we conduct a systematic study and probe for 78 molecular substructures across eight pre-trained and six randomly initialized models. We furthermore study how fine-tuning on chemical downstream tasks affects the learned representations of molecular substructures. Our results show that pre...

---

### 48. ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning

**Authors:** Yilie Huang, Wenpin Tang, Xun Yu Zhou

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02137v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02137v1)

**Summary:** We study timestep allocation for score-based diffusion sampling, where a learned reverse-time dynamics is discretized on a finite grid. Uniform and hand-crafted schedules are standard choices, but they rely on fixed prescriptions and can therefore be suboptimal. To address this limitation, we propose Adaptive Reparameterized Time (ART), a continuous-time control formulation that learns a time change by treating the speed of the sampling clock as the control, so that a uniform grid on the learned...

---

### 49. AbsoluteDegradation: A Physics-Inspired Synthetic Film-Degradation Pipeline and Archival Film Restoration Benchmark

**Authors:** Mikołaj Jastrzębski, Dawid Glinkowski, Dawid Zieliński, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02131v1)

**Summary:** Restoring archival film remains a fundamentally challenging problem due to the absence of paired training data and the lack of standardized evaluation benchmarks. Pristine versions of deteriorated footage are physically unrecoverable, requiring supervised methods to rely on synthetic data that often fail to capture the complex, temporally coherent nature of real film degradation. At the same time, existing real-world datasets are limited in scale, quality, and accessibility, hindering reliable e...

---

### 50. Population-Scale Segmentation of Penile Tissue in DIXON MRI using Deep Learning for Quantitative Phenotyping in Male Reproductive Health

**Authors:** Jan Ernsting, Gunnar Paul Kordes, Nils Johannaber, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02127v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02127v1)

**Summary:** Penile measurement is clinically relevant across male reproductive and urogenital health, including conditions such as micropenis, congenital and endocrine disorders, and sexual or urinary dysfunction. However, quantitative assessment of penile size has relied mainly on external length or circumference measurements, which are difficult to standardize, sensitive to measurement conditions, and unable to capture the internal portion of the penis. MRI enables volumetric assessment of the whole penis...

---

## cs.NE

**50 papers**

### 1. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 2. Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem

**Authors:** Zitouni Rania, Mostefai Mounir Sofiane, Tati Youcef, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02315v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02315v1)

**Summary:** The one-dimensional bin packing problem (1D-BPP) is a canonical NP-hard combinatorial optimization problem with broad industrial applications. We propose RL-HGGA, a hybrid algorithm that integrates Falkenauer's Hybrid Grouping Genetic Algorithm (HGGA) with a tabular Q-learning controller. Rather than applying genetic operators at fixed probabilities, a Q-learning agent dynamically selects among eight macro-actions -- including BPCX crossover, light and heavy mutation, Martello-Toth local search,...

---

### 3. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**Authors:** Juwei Shen, Yujie Wu, Changwen Chen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02283v1)

**Summary:** In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs. Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions. We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewin...

---

### 4. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 5. Electronic Bursting Neuron: design, equations and hardware implementation

**Authors:** Lev V. Takaishvili, Vladimir I. Ponomarenko, Maksim V. Kornilov, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02122v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02122v1)

**Summary:** Electronic neurons are a keystone for construction of the spiking neural networks which have numerous applications in neuroprosthetics, artificial memory, intensive calculations etc. A number of concepts of electronic neurons has been already proposedm with some of them implemented in hardware. However, new schemes are of significant interest since the existing ones do not fit all requirements: either they are too complex and expensive in realization, or they are not able to demonstrate all dema...

---

### 6. Evolutionary Wave Function Collapse

**Authors:** Dipika Rajesh, Ahmed Khalifa, Julian Togelius

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02082v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02082v1)

**Summary:** Wave Function Collapse (WFC) is a widely used procedural content generation method that learns local adjacency constraints from example inputs to generate larger outputs. In this paper, we explore combining WFC with evolutionary search by evolving the small input examples used by WFC rather than directly evolving complete levels. In this approach, WFC acts as a genotype-to-phenotype mapping. The generated levels are then evaluated through domain-specific fitness functions. We evaluate the method...

---

### 7. Mechanism and Stability Analysis of Metabolic Closed-Loop Metaheuristics

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01551v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01551v1)

**Summary:** This paper studies the Metabolic Multi-Agent Optimizer (MMAO) at the framework level rather than at the implementation or benchmark level. The central question is whether the metabolic resource loop of private energy, communal budget, role drift, and lifecycle turnover has a framework-level interpretation beyond narrative metaphor. We introduce a generic MMAO state model that abstracts away domain-specific move operators while retaining the resource bookkeeping that defines the framework. Under ...

---

### 8. MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01539v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01539v1)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation...

---

### 9. BFF: Simple explanations for complex phenomena

**Authors:** Charlotte Knierim, Luca Versari, Robert Obryk, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01483v1)

**Summary:** The ''Computational Life'' paper (Agüera y Arcas et al., 2024) argues that paired interactions in a computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found at least as easily using simple mutation random walks in program space. We also explore the claim that capping the maximum ''depth'' and ''width'' of the ancestry tree stops self-replicators...

---

### 10. MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00846v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00846v1)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic cont...

---

### 11. From Consistency to Collaborative Discovery: MFEA-CoD for Multitask Novelty Search

**Authors:** Jiao Liu, Yanchi Li, Hua Yu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00761v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00761v2)

**Summary:** Evolutionary multitasking (EMT) has shown strong capability in solving multiple optimization problems simultaneously by exploiting latent inter-task consistency, such as similarities in promising solutions or search directions. However, most existing EMT studies remain focused on objective-driven optimization, where such consistency is mainly used to accelerate convergence toward predefined optima. In this paper, we move EMT from consistency to collaborative discovery and propose a multifactoria...

---

### 12. Self-Organized Learning in Oscillatory Neural Networks with Memristive Signed Couplings

**Authors:** Riley Acker, Aman Desai, Garrett Kenyon, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00286v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00286v1)

**Summary:** Oscillatory neural networks (ONNs) have emerged as a promising neuromorphic architecture, leveraging coupled dynamical systems to perform computation and represent information through phase relationships. Their interactions can be designed to support intrinsic energy-minimizing dynamics, enabling tasks such as associative memory and optimization, and positioning them as a candidate architecture for continuous learning and inference. We present a neuromorphic primitive implemented using memristiv...

---

### 13. EVOTS: Evolutionary Transformer Search for Time Series Forecasting

**Authors:** AbdElRahman ElSaid, Damir Pulatov

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00154v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00154v1)

**Summary:** Evolutionary neural architecture design for multivariate time-series forecasting remains underexplored, with most approaches relying on fixed Transformer architectures despite substantial variation across tasks and forecasting settings. This paper introduces an evolutionary neural architecture search framework for discovering task-adaptive Transformer-like models for time-series forecasting (EVOTS). Architectures are encoded using a modular genome representation that enables flexible composition...

---

### 14. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 15. Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

**Authors:** Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31789v1)

**Summary:** Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associ...

---

### 16. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 17. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31584v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31584v1)

**Summary:** This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...

---

### 18. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 19. Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization

**Authors:** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30836v1)

**Summary:** Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, w...

---

### 20. Why can genetic algorithms work in high-dimensional search spaces?

**Authors:** Stephen Whitelam

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30619v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30619v1)

**Summary:** We show that the effective dynamics of the elitist $(1+M)$ genetic algorithm is, in the limit of small mutations, clipped gradient descent on the loss in the presence of anisotropic Gaussian white noise. In expectation, therefore, a simple mutation-selection genetic algorithm follows the gradient of the loss, without explicit calculation of gradients and without averaging over loss evaluations. The genetic algorithm is slower than gradient descent because of the noise that acts in directions tra...

---

### 21. Computing the Integral R2 Indicator by Perspective Mapping and Box Decomposition

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30530v3) | 📄 [PDF](https://arxiv.org/pdf/2606.30530v3)

**Summary:** The continuous integral R2 indicator is a Pareto-compliant refinement of the classical finite-weight-vector R2 indicator, used in performance assessment, bounded archiving for a-posteriori multi-objective optimization, and skyline selection in databases. This work introduces a bidirectional perspective mapping between continuous integral R2 computation and integration over unions of anchored axis-aligned boxes. After translating the ideal point of a minimization problem to the origin, approximat...

---

### 22. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30450v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30450v1)

**Summary:** This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. ...

---

### 23. From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent

**Authors:** Haoliang Han

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30191v1)

**Summary:** How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer r...

---

### 24. Semantics-Aware Bilevel Co-Evolution: Towards Automated Multicomponent Algorithm Design

**Authors:** Zhiyao Zhang, Shenghao Wu, Xingyu Wu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29953v1)

**Summary:** LLM-assisted evolutionary search (LES) has emerged as a promising paradigm for automated algorithm design. However, existing methods usually suffer from two inherent limitations when facing the automated design of real-world complex algorithms that usually consist of multiple components. The first limitation is that they either focus on modifying entire algorithms, making it difficult to reuse high-quality components, or concentrate on component refinement within a limited set of predefined mult...

---

### 25. Evolutionary Hyperparameter Optimization to Find Lightweight CNN Models for Autonomous Steering

**Authors:** Devson Butani, Ryan Kaddis, Chan-Jin Chung

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29684v1)

**Summary:** This research investigates the optimization of Convolutional and Dense Neural Networks (CNNs and DNNs) for autonomous steering using the (N+M) Evolution Strategy (ES) with the 1/5th success rule. The primary objective is to develop a lightweight CNN based model capable of real-time steering angle prediction, mimicking human driving behavior on predefined paths. The ES algorithm automates hyperparameter tuning, dynamically adjusting parameters such as filter sizes and layer configurations. Data c...

---

### 26. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 27. Supervised Hebbian learning in Deep Counterstream Associative Networks

**Authors:** Andreas Knoblauch

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29528v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29528v1)

**Summary:** Modern machine learning applications employ deep neural networks training with the error backpropagation algorithm. Although this algorithm is very effective, it lacks biological realism. For example, backpropagation requires symmetric connectivity, and a separate neural processing channel for error signals. Prior works have therefore proposed a number of more realistic alternatives for error backpropagation. However, most of them still suffer from demanding preassumptions that may be not fulfil...

---

### 28. When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**Authors:** Zhengqi Pei, Qingming Huang, Shuhui Wang

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29354v1)

**Summary:** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the a...

---

### 29. Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs

**Authors:** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, et al.

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29254v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29254v1)

**Summary:** Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reaso...

---

### 30. Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning

**Authors:** Reza Ahmadvand, Sarah Safura Sharif, Yaser Mike Banad

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29099v1)

**Summary:** Artificial neural networks (ANN) provide accurate continuous-valued representation, whereas spiking neural networks (SNN) offer event-driven temporal processing, yet both paradigms face limitations when value encoding and timing dynamics must be learned within a single computational structure. This paper introduces a network based on Unified Complex-valued Neuron (UCN), a new neural computational model that integrates continuous activation and phase-driven event generation through an asymmetric ...

---

### 31. Road to scalability for efficient graph search on massively parallel neuromorphic hardware

**Authors:** Oskar von Seeler, Elena C. Offenberg, Carlo Michaelis, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28907v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28907v1)

**Summary:** Efficient computation of shortest paths in weighted graphs is a fundamental problem with many applications. Neuromorphic hardware platforms promise massively parallel, efficient computation, changing parallelism tradeoffs. In this work, we introduce NEURO-MAPP (Neuromorphic-based Min-Add Parallel Propagation), a distributed shortest path algorithm designed to use the local computation and network communication available in neuromorphic systems. We provide an optimized implementation of the algor...

---

### 32. Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28662v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28662v1)

**Summary:** The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studie...

---

### 33. Analysis of Parameter Settings for the Bat Algorithm Using Variance Evolution

**Authors:** Xin-She Yang, Mehmet Karamanoglu

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28644v1)

**Summary:** Parameter settings in evolutionary algorithms and metaheuristics are important because such parameter values can influence the performance of algorithms under evaluation. For a given algorithm, there are many different numerical experiments to show that the algorithm can work well in practice; however, in most cases there is no theoretical analysis of parameter settings. In this work, we show that theoretical analysis using the theory of dynamical systems and evolution of population variance can...

---

### 34. Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

**Authors:** Binh Nguyen, Colleen Josephson, Mircea Teodorescu, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28600v1)

**Summary:** Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement le...

---

### 35. Comparing Scalar Objective Functions for Multi-Criteria Engineering Optimization

**Authors:** Olaf Frommann

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28541v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28541v1)

**Summary:** Scalar objective functions are required when a multi-criteria optimization problem must yield a single preferred design rather than only a Pareto set. The choice of scalarization influences which compromise is selected, how preference parameters are interpreted, and whether non-supported Pareto regions can be reached. This paper compares four formulations for normalized bi-criteria minimization: weighted sums, achievement scalarizing functions, desirability functions, and a fuzzy-logic-based for...

---

### 36. MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28109v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28109v1)

**Summary:** Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a comm...

---

### 37. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 38. Co-Optimization of Analog Kolmogorov-Arnold Networks for Low-Power Function Approximation in Flexible Electronics

**Authors:** Paula Carolina Lozano Duarte, Georgios Zervakis, Mehdi Tahoori, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27892v1)

**Summary:** Wearable devices and Internet of Things (IoT) sensors require on-sensor processing of biosignals and environmental data, including computationally demanding operations such as nonlinear activation functions for neural network inference, sensor calibration curves to map raw readings to physical units, and signal preprocessing functions like logarithmic compression and power operations for feature extraction. These functions exhibit significant complexity, often involving transcendental operations...

---

### 39. Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring

**Authors:** Muhammad Hamza

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.30676v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30676v1)

**Summary:** Deploying spiking neural networks (SNNs) on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies either neglect neuronal criticality or rely on convex relaxations of the inherently combinatorial pruning problem whose fractional masks, upon binarisation, destroy accuracy at moderate-to-high sparsity. We present Criticality-Constrained Quadratic Pruning (CQP), a native PyTorch pipeline that fuses weight magnitude with surrog...

---

### 40. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 41. DE-2LS: Differential Evolution with Lightweight Late Local Search for Constrained Numerical Optimization

**Authors:** Dikshit Chauhan, Anupam Trivedi

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27764v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27764v1)

**Summary:** Constrained single-objective numerical optimization requires a careful balance among feasibility, objective convergence, and computational efficiency under a fixed function-evaluation budget. This paper proposes DE-2LS, a late-stage, locally search-enhanced variant of differential evolution built on the RDEx framework. The proposed method preserves the original RDEx components, including mutation and crossover operators, success-history adaptation, archive mechanism, population-size reduction, a...

---

### 42. DE-2LS: Differential Evolution with Late-Stage local-search for Unconstrained Single-Objective Numerical Optimization

**Authors:** Dikshit Chauhan

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27762v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27762v1)

**Summary:** Unconstrained single-objective numerical optimization requires a careful balance among global exploration, late-stage exploitation, and function-evaluation efficiency. This paper presents DE-2LS, a late-stage, local-search-enhanced differential evolution framework built on RDEx for unconstrained single-objective optimization with variable bounds. The proposed method preserves the original RDEx evolutionary search engine and introduces two conservative refinements: a smoothed exploitation-biased ...

---

### 43. Multi-Objective Molecular Generation with Frequency-Controlled Evolutionary Dynamics

**Authors:** Elia Colleoni, Paolo Guida, Didier Barradas-Bautista, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27467v1)

**Summary:** Molecule generation methods that leverage generative models have been successfully applied to drug discovery. However, they often require extensive pre-training, suffer statistical biases in the training data, and might suffer from limited interpretability of generated chemical structures. In this work, we introduce SpectralMol, an algorithm based on evolutionary computation that processes chemical structures as a compact matrix of Fourier coefficients, projected onto a fixed basis to generate p...

---

### 44. CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention

**Authors:** Sayak Dutta

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27229v2) | 📄 [PDF](https://arxiv.org/pdf/2606.27229v2)

**Summary:** Recurrent models must forget in order to remember, yet the state of the art decides what to erase without consulting what is stored -- the gate sees only the arriving token, not the memory it is about to modify. This memory-blind gating is one of three coupled defects in the leading delta-rule architecture (GDN-2): the value-axis erase mask wastes parameters at the scale of the value projection, and -- as we prove -- mathematically prevents the WY-form triangular chunk solver that makes recurren...

---

### 45. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 46. Random Walk on Bézier Curves for Global Optimization

**Authors:** Jinpeng Wang, Xingguo Xu, Yujing Sun, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26714v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26714v1)

**Summary:** Balancing exploration and exploitation remains a central challenge in metaheuristic optimization. To address this issue, this paper proposes Bézier Walk Evolution (BWE), a geometry-driven optimization framework that reformulates evolutionary search as adaptive trajectory construction in the decision space. BWE integrates Bézier curve modeling with a distance-aware random walk mechanism to generate topology-guided search trajectories. By adaptively varying the curve order during evolution, the pr...

---

### 47. Three-Objective Integral R2 Subset Selection: NP-Hardness and Submodular Approximation

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26591v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26591v1)

**Summary:** Selecting a fixed number of representative points from a finite Pareto-front approximation is a fundamental post-processing task in multiobjective optimization. This paper studies this problem for the integral R2 indicator in three objectives, where the indicator is defined as the integral of the lower envelope of weighted Tchebycheff scalarizations over the two-dimensional weight simplex. We provide two complementary algorithmic results. On the positive side, we show that the integral R2 improv...

---

### 48. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

**Authors:** Alex Iacob, Andrej Jovanović, William F. Shen, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26294v2) | 📄 [PDF](https://arxiv.org/pdf/2606.26294v2)

**Summary:** Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves. This ignores a central feature of evolution: species adapt as their environments change with them. We aim to bring the same principle to recursive self-improvement, making evaluation part of the im...

---

### 49. EvoFlock: evolved inverse design of multi-agent motion

**Authors:** Craig Reynolds

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25280v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25280v1)

**Summary:** This paper describes an automatic method for adjusting or tuning models of multi-agent motion. Simulating the motion of bird flocks, human crowds, vehicle traffic, and other multi-agent systems is a widely used technique. These simulations model the behavior of a single group member (bird, human, or vehicle). The group behaviors (flock, crowd, traffic) emerge from interactions between group members. These models typically have many numerical control parameters. Even if each parameter is intuitiv...

---

### 50. Spatial Partial Functionalization of Neural Networks based on Noise Fields

**Authors:** Shuhei Ikemoto, Fabio DallaLibera

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24588v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24588v1)

**Summary:** Noise in neural computation is typically regarded as a disturbance, but its spatial distribution may also actively regulate which parts of a network participate in computation. This paper investigates the spatial partial functionalization of Noise-modulated Neural Networks using noise fields. We first present an activation function suitable for this goal, the crossing activation function, using the sample-level, statistical-level, and analytical-level implementations, and examine parameter reuse...

---

## q-bio.NC

**50 papers**

### 1. A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps

**Authors:** Barada Sahu, Shivesh Pandey

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01400v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01400v1)

**Summary:** Deep multimodal brain-encoding models now predict fMRI responses to naturalistic video with high accuracy. Whether their predicted neural signals also forecast behavioral engagement is unknown. We run TRIBE, the winning model of the 2025 Algonauts brain-encoding challenge (Llama-3.2 + V-JEPA2 + Wav2Vec-BERT), on 48 YouTube videos and reduce its predicted cortical response to a per-second engagement curve, the global field power. Correlated against each video's "most replayed" heatmap, a passivel...

---

### 2. DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00851v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00851v1)

**Summary:** Brain activity spans single-neuron, population, and network levels, and core questions in neural coding require moving between them. Yet current tools target a single paradigm and incompatible data formats, leaving cross-level questions hard to address. We present DRIADA, an open-source Python framework that unifies neural signals and time-aligned behavior in a shared data model, so selectivity testing, dimensionality reduction, and network analysis operate within a unified workflow. We evaluate...

---

### 3. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00397v1)

**Summary:** Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...

---

### 4. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 5. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 6. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v1)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 7. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 8. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 9. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 10. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 11. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 12. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 13. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 14. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 15. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 16. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 17. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

### 18. Weight geometry governs functional memory in complex systems

**Authors:** Elkaïoum M. Moutuou, Habib Benali

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25826v1)

**Summary:** Complex systems, from gene regulatory networks to neural circuits and transportation infrastructures, exhibit rich functional behaviour that topology alone does not capture. Here we show that functional memory exhibits a universal organisational regularity: in every biological, ecological, social, and technological domain studied, real interaction strengths organise memory at greater hierarchical depth than random weight assignment on the same topology, across thirty-four networks spanning sever...

---

### 19. Meta-learning as a principle for human-like visual representations

**Authors:** Can Demircan, Marcel Binz, Alireza Modirshanechi, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.28399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28399v1)

**Summary:** The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few obse...

---

### 20. A pilot study examining transcranial photobiomodulation therapy intervention in college students with insomnia

**Authors:** Jiangshan He, Lianghua Zhang, Dan Liang, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24668v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24668v1)

**Summary:** College students commonly report insufficient sleep and poor sleep quality, with ~30% meeting insomnia criteria, posing significant threats to their physical growth, cognitive development, and overall well-being, as well as imposing a substantial economic burden on society [1]. The hyperarousal model of insomnia [2] emphasizes that hyperarousal across cognitive, emotional, and physiological domains mutually reinforces one another. Neuroimaging studies have further identified prefrontal hypoactiv...

---

### 21. EEG Interpretation Across Chant Listening: A Single-Subject Pilot Investigation Using Spectral and Functional Connectivity Analysis

**Authors:** Prerna Singh, Aishwarya Ghosh, Neelam Sinha, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24406v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24406v1)

**Summary:** This technical report presents an EEG-based investigation of neural activity across five auditory conditions: Resting State (RS), Shiv Tandav Stotra (STS), Mahasudarshan Mantra (MM), Aum Chant, and Tanpura Listening. EEG recordings acquired from a healthy 5-year-old participant were analyzed using spectral power estimation and functional connectivity measures based on the weighted Phase Lag Index (wPLI). Spectral analysis revealed condition-specific modulation of neural oscillatory activity, wit...

---

### 22. Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**Authors:** Xavier Vasques, Paul Barbaste, Olivier Oullier

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24394v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24394v1)

**Summary:** Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (fea...

---

### 23. Graph-based analysis of inflammatory profiles in New Onset Refractory Status Epilepticus (NORSE)

**Authors:** Linon Denis, Martin Guillemaud, Vincent Navarro, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24351v1)

**Summary:** Background and Objectives: Cryptogenic new-onset refractory status epilepticus (cNORSE) represents one of the most severe forms of status epilepticus, occurring in patients without prior neurological disease, and remaining of unknown aetiology despite extensive diagnostic evaluation. Emerging evidence supports a role for immune dysregulation in cNORSE; however, marked heterogeneity in inflammatory signatures has been reported, complicating the selection of targeted immunotherapies. Therefore, a ...

---

### 24. The Morality Game: An online multiplayer platform to standardize, expedite, and expand research on cooperation

**Authors:** Gregory N. Stanley, Alan Yang, Liam Tsimhoni, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24037v1)

**Summary:** This paper presents the Morality Game, a platform designed to standardize and accelerate research on cooperation and morality through game theory-based experiments. The Morality Game functions as a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process. It allows researchers to launch customized online multiplayer experiments with zero coding, using game trees to simulate moral dilemmas. The platform automates part...

---

### 25. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 26. The adaptive nature of confirmation bias

**Authors:** Dorje C. Brody, Karl J. Friston, Bernhard K. Meister, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23325v1)

**Summary:** In this paper, the phenomenon generally classified as confirmation bias is formulated on the space of square-root probabilities (or equivalently, using the structures of quantum probability). In this framework, observations are modelled by matrices, rather than random variables on a probability space. In the problem of binary hypothesis testing, an optimal evidence choice minimises the expected error probability. We show that the resulting optimal choice of evidence leads to a confirmation bias,...

---

### 27. Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg

**Authors:** Helio V. Cabral, Giacomo Valli, Roberto Zanotti, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23066v1)

**Summary:** Common synaptic input is considered a fundamental principle of motor neuron control and represents the dominant component of the neural drive transmitted from the motor neurons to muscle. Recent advances in High-Density surface Electromyography (HDsEMG) and motor unit (MU) decomposition algorithms have enabled the concurrent identification of increasingly large populations of MUs and substantially expanded the possibility of estimating common synaptic input from MU spike trains, making this appr...

---

### 28. SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings

**Authors:** Yisi S. Zhang, Daniel Y. Takahashi

**Published:** 2026-06-21

🔗 [Paper](http://arxiv.org/abs/2606.22695v1) | 📄 [PDF](https://arxiv.org/pdf/2606.22695v1)

**Summary:** Mapping the directed flow of information between brain regions -- their effective connectivity -- is central to understanding brain function, yet large-scale recordings sample only a fraction of the brain at a time: sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established directed-connectivity methods (Granger causality, dynamic causal modeling, partial directed coherence, PDC) require all regions to be recorded ...

---

### 29. DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**Authors:** Jayadratha Gayen, Bradly Alicea

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21940v1)

**Summary:** Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed...

---

### 30. Dynamic Computerized Tumbling-E Testing for Temporal Reliability of Human Sequential Perceptual Decisions

**Authors:** Avneek Sandhu, Bin Hu

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21818v1)

**Summary:** OBJECTIVES: Visual acuity and tumbling-E tasks are often treated as static threshold measures, yet sequential perceptual decisions unfold over time. A computerized tumbling-E task preserves response latency, timeouts, and stimulus-size adaptation, creating a temporal reliability dataset rather than only a chart-line score. This matters for human-AI comparison because the Temporal Hallucination Index (THI) shows how static accuracy can obscure delays, drift, persistence, and unstable convergence....

---

### 31. Mostly-monocular responses and other visual functions in a multiscale network model of Macaque V1

**Authors:** Zhuo-Cheng Xiao, Kevin K. Lin, Lai-Sang Young

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21785v2) | 📄 [PDF](https://arxiv.org/pdf/2606.21785v2)

**Summary:** Visual signals from the two eyes merge gradually as they pass through the primary visual cortex (V1). Here we use a computational model of Macaque V1 to study the first stage of this integration along the magnocellular pathway, in layer 4C$α$, aiming to infer neuroanatomical origins of binocular response. It is known that neurons in layer 4C$α$ are predominantly monocular, though some do exhibit varying degrees of binocularity. We find (1) the emergence of narrow binocular strips along borders o...

---

### 32. Delay coordinates synchronization and induces abrupt transition in excitable networks

**Authors:** Bruno R. R. Boaretto, Kalel L. Rossi, Lyle E. Muller, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21703v1)

**Summary:** Neuronal communication is inherently time-delayed, due to the finite speed of signal propagation. Although often considered challenging or disruptive, such time delays can also endow neural circuits with useful capabilities. Here, we show that delays in excitatory connections between excitable neurons coordinate their synchronization patterns by creating self-sustained oscillations that may be out-of-phase or in-phase. The emergence of these oscillations leads to an abrupt, explosive, transition...

---

### 33. Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks

**Authors:** Stephen Coombes, Rüdiger Thul, Stefan Ruschel, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21508v1)

**Summary:** We develop a theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model as an analytically tractable event-based description of neural dynamics. For networks with fixed delays, we derive self-consistency conditions for phase-locked states and an associated linear stability theory formulated directly in terms of spike-time perturbations. The framework is illustrated for a delayed autapse, a reciprocally coupled two-cell network, and spatially structured rings wit...

---

### 34. Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity

**Authors:** Ch. Meessen

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21432v1)

**Summary:** We construct a minimal but biologically plausible spiking neuron model operating in discrete time, combining multiplicative spike-timing-dependent plasticity (WSTDP), divisive normalization of synaptic integration, homeostatic threshold adaptation, and a one-step refractory period. We show that this normalization admits a biologically plausible dendritic implementation in which each binary junction operates using only locally available information.   Assembling excitatory-inhibitory pairs of suc...

---

### 35. Relational Gaze Transitions During Encoding Predict Episodic Recall of Naturalistic Scenes

**Authors:** Hugo Rydel, Alex Kafkas

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20844v1)

**Summary:** Remembering a visual scene requires organizing distinct details into a cohesive event. This study investigates whether relation-guided gaze transitions provide a behavioural marker of this cognitive organization during episodic encoding and retrieval. By applying scene graph annotations to eye-tracking data, we measured whether gaze moved between objects that were meaningfully related within complex scenes. This approach allowed us to quantify relational scanning within naturalistic environments...

---

### 36. Synchronization modes in bipartite oscillator networks

**Authors:** Pau Pomés, Bastian Pietras, Ernest Montbrió

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20345v1)

**Summary:** Collective oscillations in neuronal systems often arise from interactions between excitatory and inhibitory populations rather than from recurrent coupling within a single ensemble. Motivated by the coexistence of strongly and partially synchronized regimes in such systems, we study the Kuramoto Sakaguchi model on a bipartite network. Despite its minimal structure, the model exhibits rich collective dynamics, including both continuous and discontinuous transitions from full synchrony to partial ...

---

### 37. Quadratic Forms for Measuring Geometric Trees in 3-dimensional Space

**Authors:** Yossi Bokor Bleile, Emanuele Cortinovis, Herbert Edelsbrunner, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20096v1)

**Summary:** Tree-like structures appear in many areas of science, and their shapes can help understand the underlying processes they drive or that give rise to them.   By thinking of these structures as geometric graphs in $\mathbb{R}^3$, we gain access to tools from computational geometry and topology to study them.   In this paper, we adopt the theory of quadratic forms to measure the directional spread of geometric graphs, and we introduce the hexplot model -- equipped with a metric derived from the Fish...

---

### 38. Robust probabilistic measurement of structural-functional module consistency in infant brain development

**Authors:** Lingbin Bian, Feihong Liu, Qian Wang, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.19739v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19739v1)

**Summary:** Brain network is commonly divided into modules for analyzing their functionally segregated roles for group-level analysis in neuroimaging studies. Here, we introduce stochastic modules within brain networks for a robust probabilistic measurement of structural-functional module consistency (SFMC) in a group of subjects. Specifically, a stochastic module can be regarded as the chance of a brain region across subjects potentially being assigned to a group-level sub-network, characterized as an assi...

---

### 39. Retrieval-Based Brain Decoding by Alignment, not Complexity

**Authors:** Matteo Ciferri, Matteo Ferrante, Nicola Toschi

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.19081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19081v1)

**Summary:** A prominent theory in cognitive science suggests that concepts in the brain are organized as high-dimensional vectors, with semantic meaning captured by directions and relative angles in this space. Brain decoding is the effort of reconstructing or retrieving stimuli (or their representations) from neural activity and involves finding a function that approximates how the brain represents concepts. This motivates the investigation of contrastive objectives as biologically plausible candidates to ...

---

### 40. Dissecting emerging slow rhythms in delay-coupled neural oscillators

**Authors:** Xinxin Qie, Matteo Martin, Shenquan Liu, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.20733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20733v1)

**Summary:** Synaptic transmission delays are ubiquitous in neural circuits and can alter the dynamical repertoire of coupled oscillators quantitatively and qualitatively. Here, we demonstrate that delayed coupling in inhibitory networks introduces an effective slow-fast structure in the phase-difference dynamics, generating low-frequency components that are not due to intrinsic cellular properties, and we show that this behavior is not specific to a particular model structure. The origin of this generic phe...

---

### 41. Can neurons speak? Semantic narration of vision at single-cell resolution

**Authors:** Arnau Marin-Llobet, Richard Hakim, Sara Matias, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.18667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.18667v1)

**Summary:** Identifying what individual neurons encode in higher-order visual cortex is an open problem. Responses resist intuitive parameterization, and the deep-network embeddings used in their place are black boxes. Here, we introduce NEURRATOR, a framework that decodes spiking activity into free-form natural-language narration of the viewed scene at single-neuron resolution. A learned encoder maps spike trains from arbitrary subsets of simultaneously-recorded neurons into the patch-embedding space of a ...

---

### 42. A frozen rate operator from the complete larval connectome: degree and weight govern the gross response, exact wiring governs input routing and mushroom-body modes

**Authors:** Stavros Therianos

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17745v2) | 📄 [PDF](https://arxiv.org/pdf/2606.17745v2)

**Summary:** Connectome-constrained models now reproduce neural activity in several systems, yet each inherits a circuit's degree and weight statistics along with its exact wiring, leaving open which dynamical properties the wiring fixes beyond those statistics. We separate the two by running the complete larval Drosophila connectome, 2'825 neurons in its strongly connected core, as a frozen leaky-tanh rate operator with no single-neuron parameter fitted, and comparing it against a degree-and-weight-matched ...

---

### 43. BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17742v1)

**Summary:** Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than...

---

### 44. Ten Years of the Stochastic Resonance Model of Tinnitus: From Phantom Perception to Adaptive Sensory Optimization

**Authors:** Patrick Krauss, Achim Schilling

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17736v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17736v1)

**Summary:** Subjective tinnitus - the perception of sound in the absence of an external acoustic stimulus - remains one of the most debated phenomena in auditory neuroscience. In 2016, the stochastic resonance (SR) model was introduced as an alternative account of tinnitus-related neuronal hyperactivity, proposing that internally generated neural noise is adaptively upregulated to restore information transmission after hearing loss. Rather than interpreting increased spontaneous activity as maladaptive, the...

---

### 45. Embodiment Shapes Rolling Behavior in a Multimodal Infant Model

**Authors:** Leon Philipp, Francisco M. López, Jochen Triesch

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17456v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17456v1)

**Summary:** Rolling over is one of the earliest milestones in infant motor development, reflecting the emergence of coordinated, whole-body sensorimotor control. Here, we conduct a computational study of infant rolling using MIMo, a virtual infant embodiment equipped with proprioception and vestibular sensation. MIMo learns supine-to-prone rolls with reinforcement learning. Interestingly, the learned behaviors capture developmental trends and coordination patterns consistent with those reported in real infa...

---

### 46. Adaptive inference and function vectors in deep transformers

**Authors:** Ravin Raj, Gautam Reddy

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16694v1)

**Summary:** Transformers are widely used as a general-purpose substrate for learning complex correlations between a large collection of coupled variables, but their internal mechanisms have remained mysterious. We introduce a theory of a deep transformer as a mean-field interacting system that implements distributed inference, subject to constraints on communication, locality and depth. We show that such a system can exploit internal state representations ('function vectors') to infer a latent context varia...

---

### 47. Learning Hybrid Biophysical Neuron Models with Neural ODEs

**Authors:** Jonas Beck, Michael Deistler, Dóra Viktória Molnár, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16693v1)

**Summary:** Biophysical neuron models link measurements of neural activity to underlying cellular mechanisms. Yet, a central challenge is that the kinetics of many ion channels are poorly characterized, and practical simplifications -- omitting channels or reducing morphological detail -- introduce systematic gaps between model and biology. Bridging these gaps requires approaches that can flexibly discover unmodeled dynamics while preserving mechanistic interpretability. Here, we introduce a hybrid modeling...

---

### 48. Infant Spontaneous Movement Noise Improves Exploration in Deep RL

**Authors:** Francisco M. López, Markus R. Ernst, Francisco Cruz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16590v2) | 📄 [PDF](https://arxiv.org/pdf/2606.16590v2)

**Summary:** Exploration in deep reinforcement learning (RL) is commonly implemented as temporally uncorrelated white noise. However, recent works show that temporally correlated colored noise can improve exploration efficiency by producing smooth trajectories with better coverage of the state space. We inquire whether action noise inspired by infant spontaneous movements can also improve exploration in deep RL. We find that the power spectral densities of babies' end-effector velocities follow a colored noi...

---

### 49. Sex-based Network-Specific Differences in Connectomes: A Krakencoder-Based Analysis

**Authors:** Vibhashree S H, Debanjali Bhattacharya, Vamshi Krishna Kancharla, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16294v1)

**Summary:** This study examines how deficiencies in one brain connectome modality propagate to the other, using the Krakencoder as a simulation framework. Structural and functional connectomes from 702 healthy participants in the Human Connectome Project were analyzed, with the impact of each of the Yeo-7 functional networks assessed separately. Seven scenarios were considered, each involving the removal of a single network while the remaining networks were preserved. The resulting perturbations in cross-mo...

---

### 50. EEGDash: An open-source platform for machine learning on public neurophysiological data

**Authors:** Bruno Aristimunha, Aviv Dotan, Pierre Guetschel, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.16041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16041v1)

**Summary:** Public neurophysiological datasets are increasingly accessible but remain hard to reuse: turning one into a trained model still takes thousands of lines of code for download, loading, format repair, windowing, and evaluation, and a dataset that meets metadata standards can still fail to load. EEG-Dash is a software resource that catalogues 791 publicly archived recordings (39,778 participants, over 86,051 hours) spanning electroencephalography (EEG), magnetoencephalography (MEG), intracranial EE...

---

## stat.ML

**50 papers**

### 1. Online Safety Monitoring for LLMs

**Authors:** Mona Schirmer, Metod Jazbec, Alexander Timans, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02510v1)

**Summary:** Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with mor...

---

### 2. The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent Geometry

**Authors:** Yuan Yuan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02368v1)

**Summary:** Evaluations of LLM personas via psychometric questionnaires typically rely on aggregate scores, discarding within-instance correlation structure. We test whether this geometric structure is intrinsic or frame-dependent. Constructing within-instance correlation matrices from IPIP-50 responses, we analyze geometry on SPD manifolds under manipulated question orderings in GPT-4o simulating American and Chinese-American personas. We find that persona expression comprises two dissociable components: a...

---

### 3. Cross-Audit Projection for Model Risk Prediction

**Authors:** Yijian Huang

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02328v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02328v1)

**Summary:** For training-data-based model risk prediction, $K$-fold cross-validation~(CV) is widely used to mitigate the well-known over-optimism of the empirical risk and is often regarded as reliable. However, for binary classification via empirical risk minimization, our numerical studies reveal a surprising phenomenon: $K$-fold CV may perform poorly in estimating class-specific risks, even worse than the empirical estimator. We perform a higher-order asymptotic analysis showing that $K$-fold CV may conv...

---

### 4. Aggregation with Exponential Weights is Optimal in Expectation

**Authors:** Mikael Møller Høgsgaard, Patrick Rebeschini, Tobias Wegel

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02247v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02247v1)

**Summary:** The aggregation with exponential weights (AEW) estimator is not fully understood in the basic setting of model selection aggregation with squared loss. In particular, whether it is minimax-rate optimal in expectation for large enough fixed temperatures and under random design has been an open problem since its introduction, which was explicitly posed by Lecué and Mendelson (2013). In this paper, we settle this problem by showing that \emph{without} requiring a Bernstein-type assumption, the AEW ...

---

### 5. An Additive MLP-GNN Framework for Characterizing Chemical and Structural Contributions to Aqueous Solubility

**Authors:** Sampreeti Bhattacharya, Arkaprava Roy

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02212v1)

**Summary:** Aqueous solubility is a key property in early-stage drug discovery, but most predictive models merge physicochemical descriptors and molecular graph information into a single representation, obscuring whether a prediction is driven by global chemistry, molecular structure, or both. We present an additive deep-learning framework that keeps these two sources of information separate throughout training: physicochemical descriptors are encoded by a multilayer perceptron (the chemical branch) and mol...

---

### 6. Prediction Sets for Counterfactual Decisions: Coverage, Optimality, and Conformal Prediction

**Authors:** Yurui Zheng, Ying Jin

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02206v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02206v1)

**Summary:** Predictions are increasingly used to guide high-stakes decisions, from treatment selection to policy making. To ensure reliability with imperfect predictions, uncertainty quantification methods such as conformal prediction build prediction sets with coverage guarantees. However, statistical validity alone does not immediately determine the decisions to take, nor the optimality thereof. This gap is especially delicate in counterfactual settings where the outcome that materializes depends on the a...

---

### 7. Conformal Bayes for Two-Sided Censored Gaussian Regression under Label Shift

**Authors:** Seungjin Choi

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02173v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02173v1)

**Summary:** Prediction under label shift becomes nonstandard when responses are censored. In a two-sided censored Gaussian model, latent values below $L$ and above $U$ are recorded at the boundary values, so the observed predictive distribution is mixed, with atoms at $L$ and $U$ and a continuous density on $(L,U)$. In this paper we develop conformal Bayes for this mixed-space setting by combining posterior predictive tilting with weighted conformal calibration. Under a two-sided Tobit Gaussian Bayesian pre...

---

### 8. Sequential Structure-Sensitive Residual Diagnostics for PDE Inverse Problems

**Authors:** Ieva Kazlauskaite

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02101v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02101v1)

**Summary:** Computational models in science and engineering are often assessed by checking whether the residual norm is consistent with the assumed noise level. This can be misleading in smoothing inverse problems: structured model errors may be attenuated in observation space, leaving residual magnitudes below practitioner discrepancy thresholds while coherent residual patterns remain. As a result, residual-norm diagnostics can accept fitted models that still give biased parameters, predictions, or quantit...

---

### 9. Born Discrete, Made Smooth: Variational Formulation of Shallow Neural Networks

**Authors:** Matej Benko, Pierre Bousquet, Iwona Chlebicka, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02003v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02003v1)

**Summary:** Although neural networks are remarkably effective, their underlying optimization principles remain theoretically elusive, often characterized by non-convex landscapes and stochastic heuristics. In this work, we propose a paradigm shift by replacing the discrete training problem of shallow neural networks with a well-posed continuum variational surrogate. We identify a family of $λ$-convex functionals over parameter densities in weighted Sobolev spaces and prove that these variational problems ar...

---

### 10. Moment-Based Selection of Multiresponse Linear Mixed-Effects Models

**Authors:** Yifan Chen, Yuedong Wang, Guo Yu

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01971v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01971v1)

**Summary:** We propose MOMENT (\textbf{MO}ment-Based \textbf{M}ixed-\textbf{E}ffects Selectio\textbf{N} and Es\textbf{T}imation), a stage-wise moment-based framework that exploits second-order cross-moment identities to select and estimate the random-effects covariance matrix and fixed-effects coefficients. By inducing sparsity through its diagonal under a positive semidefinite constraint, the random-effects selection problem reduces to a smooth constrained convex optimization problem that can be solved eff...

---

### 11. Autorelevance function and other feature relevance measures for univariate time series

**Authors:** Julian Cardenas, Jamie Arjona, Pedro Delicado

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01959v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01959v1)

**Summary:** We propose a model agnostic methodology to measure lag relevance in machine learning forecasting models applied to univariate time series. Particularly, we are working in the context of time series using the frameworks of Ghost variables and Shapley values, together with additive importance measures, to introduce the auto-relevance and partial auto-relevance functions as the lag importance values. Additionally, we propose a novel method to replace absent features in coalition based methods with ...

---

### 12. Statistical Properties of $k$-means Clustering for Data Missing Completely at Random

**Authors:** Xin Guan

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01945v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01945v1)

**Summary:** The classical $k$-means clustering cannot be directly used to incomplete data, and existing $k$-means-based clustering for missing data primarily focus on improving the practical accuracy of clustering, whereas most of them lack theoretical guarantees in the asymptotic sense. In this paper, we investigate the statistical properties of $k$-means clustering in the presence of missing data. We first establish the $\sqrt{n}$-excess risk bound and prove the consistency of the estimated cluster center...

---

### 13. Regularized Variational and Spectral Log-Density-Ratio Estimation in the Gaussian Location Model

**Authors:** Francis Bach

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01895v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01895v1)

**Summary:** We study ridge-regularized log-density-ratio estimation in the Gaussian location model with a common covariance matrix. By affine invariance, the model is written as q $\sim$ N(0, I), p $\sim$ N($Δ$, I), with linear features, where $Δ$ is a mean vector. The variational estimator is the empirical Kullback-Leibler (KL) log-normalized fit with a squared L2-penalty on its nonconstant coefficient, and the spectral estimator recently introduced in [1] replaces a single variational problem by a continu...

---

### 14. Role-Aware Neural Convex Divergence Heads for Asymmetric Representation Learning

**Authors:** He Huang, Lu Shen, Yunfeng Huang, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01762v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01762v1)

**Summary:** Many representation learning problems involve directed relations, such as lexical entailment, sentence entailment, ontology hierarchy, and citation links. Standard Euclidean, cosine, and Mahalanobis heads are symmetric, while generic neural scorers can model directionality but provide limited geometric structure. This paper proposes a role-aware neural convex divergence head for asymmetric representation learning. The head applies source- and target-role projections before evaluating an input-co...

---

### 15. Identifiability Limits of Physics-Informed Inference for Spatial Stochastic Dynamics from Static Snapshots

**Authors:** Rujie Gu, Ray Zirui Zhang, Christopher E. Miles

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01749v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01749v1)

**Summary:** Despite increasing scale and resolution, many biological measurements remain destructive, revealing only spatial information rather than the dynamics it encodes. By combining flexible representations with mechanistic constraints, physics-informed machine learning offers a promising route to inferring these dynamics from static snapshots. Motivated by subcellular imaging of gene expression, we ask when a static spatial pattern of molecules can identify spatially varying diffusivity, creation, des...

---

### 16. Full Bayesian Reinforcement Learning via LF-IBIS

**Authors:** Stefano Masini, Cecilia Viscardi, Michela Baccini

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01741v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01741v1)

**Summary:** Reinforcement Learning (RL) is a sequential decision-making framework in which an agent learns optimal policies through interaction with an environment by maximizing cumulative rewards. Among RL methods, Bayesian Reinforcement Learning (BRL) addresses common practical challenges related to data scarcity by leveraging prior knowledge about the environment and sequential belief updates. However, most BRL approaches require an explicit likelihood function, which is frequently inaccessible or intrac...

---

### 17. Learning Effective Soliton Dynamics from Scattering Data

**Authors:** Seth Minor, Vanja Dukic, David M. Bortz

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01545v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01545v1)

**Summary:** The inverse scattering transform (IST) provides the standard theoretical framework for deriving soliton dynamics. Traditionally, such derivations have been of an analytical, rather than data-driven, nature. In this paper, we combine the conceptual framework of the IST with weak-form system identification methods to discover effective soliton dynamics directly from observed scattering data, without assuming prior knowledge of the scattering equations. Our method avoids parameterizing solitary wav...

---

### 18. Unveiling the Non-Monotonic Effect of Privacy on Generalization under Byzantine Robustness

**Authors:** Thomas Boudou, Batiste Le Bars, Nirupam Gupta, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01492v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01492v1)

**Summary:** Recent work has established a fundamental trilemma between Byzantine robustness, local differential privacy (LDP), and optimization error in distributed learning. We show that this trilemma does not universally extend to generalization error, but instead depends critically on the privacy regime. Specifically, in the high-noise regime (strong privacy), we prove that increasing privacy reduces the generalization error, i.e., there is no tension between robustness and privacy. In the low-noise regi...

---

### 19. How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size

**Authors:** Fabian Schaipp

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01487v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01487v1)

**Summary:** We propose a scaling law that takes into account model size and training data while explicitly splitting the latter into training steps and batch size (called three-term law). Fitting the proposed law on a large set of training runs, we find that it correctly recovers the scaling of the optimal batch size. Moreover, because it makes use of training runs with suboptimal batch size, our proposed law can be robustly fit with a significantly smaller amount of training runs. We further show that the ...

---

### 20. Conditional Inference Trees and Forests for Feature Selection

**Authors:** Robert Milletich, Justin Downes, Steve Goley, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01417v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01417v1)

**Summary:** Conditional inference trees (CIT) and conditional inference forests (CIF) reduce split-selection bias by testing features before choosing split thresholds, but repeated permutation tests and threshold searches can make these methods computationally expensive. We study CIT and CIF as top-$k$ feature-ranking methods for downstream prediction using real-data benchmarks, runtime ablations, and synthetic feature-recovery experiments. At a fixed node, if the features and permutation budget do not depe...

---

### 21. From Approximation to Emergence: A Theory of Deep Learning

**Authors:** Zhilin Zhao

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01311v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01311v1)

**Summary:** Deep learning has outgrown any single mathematical explanation. From Approximation to Emergence develops a unified, proof-oriented account of modern deep learning theory, tracing a path from the classical foundations of approximation, optimization, and generalization to the contemporary mechanisms of overparameterization, robustness, generative modeling, transformers, in-context learning, scaling laws, interpretability, alignment, and emergence. Rather than presenting isolated results, the book ...

---

### 22. Decision-Aware Training for Sample-Based Generative Models

**Authors:** Kornelius Raeth, Nicole Ludwig

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01171v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01171v1)

**Summary:** Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. These models are commonly trained with strictly proper scoring rules, such as the energy score, which allocate their training signal in proportion to data density, with no awareness of where forecast errors are most costly for downstream decisions. We therefore propose decision-aware training for sampl...

---

### 23. Characterizing and Identifying Separable Graphical Models

**Authors:** Christopher Meek, Kayvan Sadeghi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01057v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01057v1)

**Summary:** We study a broad class of graphical models whose independencies correspond to vertex separation in mixed graphs with directed, undirected, and bidirected edges, that are capable of encoding independence structures arising from feedback, latent and selection mechanisms. In particular, we introduce separable graphs, in which each missing edge implies the existence of a separating set for its endpoints, and essentially separable graphs, those graphs separation equivalent to a separable graph. We sh...

---

### 24. Function-Counting Theory for Low-Dimensional Data Structures

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01010v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01010v1)

**Summary:** The success of deep learning models in classification and regression is widely attributed to the low-dimensional structure that real-world data tend to exhibit, despite their high-dimensional representation. This work attempts to provide a mathematical framework for binary classification on low-dimensional data, building on Cover's (1965) function-counting theory. With our framework, we aim to address the question of how the low-dimensional structure of the data affects the classification capabi...

---

### 25. Deep Multitask Learning for Mixed-Type Outcomes with Shared Sparsity

**Authors:** Huichao Li, Tong Wang, Sanguo Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00995v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00995v1)

**Summary:** Most existing multitask learning approaches are limited by their reliance on task-specific loss functions tailored to the scale and type of each outcome. When outcomes differ across tasks, these losses are generally not directly comparable, which makes it difficult to formulate a unified objective and may limit information sharing across tasks. We propose a multitask transformation framework in which task-specific responses may differ through unknown monotone transformations. Motivated by high-d...

---

### 26. Hierarchical Variational Kalman Filtering

**Authors:** Shilei Li, Dawei Shi, Wei Zheng, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00877v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00877v1)

**Summary:** Traditional variational Kalman filtering with unknown noise statistics suffers from inconsistent process covariance estimation and slow convergence speed, limiting its practical utility. To address these issues, we introduce a surrogate variable representing the process-noise-free state, which enables explicit modeling and inference of process noise statistics. In addition, we reformulate the conventional coordinate ascent variation inference (CAVI) as a marginalized maximum a posteriori problem...

---

### 27. Convolutional Symmetric AutoEncoders: enhancing latent stability via differential geometry

**Authors:** G. Li Causi, N. Tonicello, L. Magri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00669v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00669v1)

**Summary:** Autoencoders (AEs) have emerged as powerful tools for non-linear dimensionality reduction, often surpassing traditional linear methods such as Proper Orthogonal Decomposition (POD) in scenarios characterized by slowly decaying Kolmogorov $n$-widths. In the realm of Reduced-Order Modelling (ROM), these models are increasingly utilized to learn low-dimensional representations of solution manifolds associated with parametric Partial Differential Equations (PDEs). However, the high expressivity of A...

---

### 28. Approximate full-conformal multi-task regression with reproducing kernels

**Authors:** Davidson Lova Razafindrakoto, Alain Celisse, Jérôme Lacaille

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00645v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00645v1)

**Summary:** Multi-task regression aims at jointly solving multiple regression problems, called tasks. Compared to solving each task separately, better performances can be achieved as long as the tasks are sufficiently related. Full-conformal prediction is a framework that formulates a data-dependent prediction-region containing the unknown output-vector at any prescribed confidence level. However, explicit computation of this prediction-region is intractable in general since it requires training infinitely ...

---

### 29. Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization

**Authors:** Xuefeng Liu, Mingxuan Cao, Qinan Huang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00531v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00531v1)

**Summary:** Scientific reasoning is an increasingly important capability of large language models, yet improving the robustness and efficiency of training such reasoning remains a key open challenge. We study this problem in instruction-based molecular optimization, where answer-only supervised fine-tuning (SFT) collapses multi-step reasoning and reinforcement learning with verifiable rewards (RLVR) suffers from sparse feedback. Reference-guided Policy Optimization mitigates both by anchoring policy updates...

---

### 30. From Structural Equation Modelling to Double Machine Learning: Robustness Analysis for Survey-Based Research

**Authors:** Ka Ching Chan, Qiana Liu, Sanjib Tiwari, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00512v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00512v1)

**Summary:** Structural equation modelling (SEM) is widely used in survey-based business and information systems research to assess latent constructs and theory-driven structural relationships. However, SEM path significance is obtained within a particular model specification and may not show whether findings remain stable under alternative estimation frameworks. This study develops and demonstrates a staged robustness analysis framework that connects SEM, ordinary least squares (OLS) regression, and Double ...

---

### 31. Prototype Language Models

**Authors:** Dan Ley, Giang Nguyen, Himabindu Lakkaraju, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00510v1)

**Summary:** Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Mode...

---

### 32. Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain Generalization

**Authors:** Peilin Liu, Ding-Xuan Zhou

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00479v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00479v1)

**Summary:** Transformer-based large models have demonstrated remarkable generalization abilities across different tasks by leveraging a context-aware attention module for in-context learning. With richer context, transformers adapt more effectively to the current use case without any parameter updates. However, the quadratic computational and memory complexity with respect to context length significantly slows data processing in softmax transformers. Linear transformers were proposed to address this issue b...

---

### 33. Neural Network-Based Estimation of Time-Dependent Parameters in AR(p) Processes

**Authors:** Agnieszka Kopeć, Paweł Przybyłowicz, Martyna Wiącek

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00470v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00470v1)

**Summary:** We investigate a forecasting framework based on a simple discrete-time dynamic model with coefficients varying in time. The parameters of the model are recovered within a deep learning framework, which makes it possible to retain a transparent parametric structure while simultaneously accounting for complex and nonstationary patterns in the observed phenomenon. Our analysis covers two specifications of the noise process. Besides the standard Gaussian setting, we also consider Laplace-distributed...

---

### 34. From Spectral Methods to Sample Complexity Bounds for Fourier Neural Operators

**Authors:** Nisha Chandramoorthy, Daniel Sanz-Alonso, Nathan Waniorek

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00320v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00320v1)

**Summary:** We establish approximation and learning guarantees for Fourier neural operators (FNOs) applied to time-$T$ solution operators of dissipative evolution equations. The analysis builds on the premise that FNOs can efficiently approximate and learn solution operators whenever these operators admit stable and accurate spectral discretizations. To formalize this idea, we introduce classes of evolution operators defined through spectral methods and derive FNO approximation bounds and polynomial sample ...

---

### 35. Entropy-Regularized Probabilistic Gates for Sparse Model Discovery in Scarce-Data Federated Learning

**Authors:** Krishna Harsha Kovelakuntla Huthasana, Alireza Olama, Andreas Lundell

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00275v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00275v1)

**Summary:** Federated Learning (FL) is a distributed machine learning (ML) paradigm with collaboration among multiple clients without sharing data. FL is challenging under data heterogeneity and partial client participation. Learning sparse models is useful for communication and computational efficiency in FL, but it is especially difficult in the small-sample high-dimensional regime (d >> N) where optimization can yield parameter configurations that fail to generalize to unseen test data. While magnitude-b...

---

### 36. eXact-Prior Variational Autoencoder (X-VAE): Learning Data-Adaptive Gaussian Mixture Priors for Latent Distributions

**Authors:** Qijun Chen, Shaofan Li

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.01275v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01275v1)

**Summary:** Variational Autoencoders (VAEs) commonly assume a standard isotropic Gaussian prior over the latent space, an assumption that often fails to capture the true distribution of latent representations for complex datasets. This mismatch can limit reconstruction accuracy, reduce sample quality, and constrain the expressive power of the learned latent space. We propose the eXact-Prior Variational Autoencoder (X-VAE), a framework that replaces the conventional standard normal prior with a Gaussian prio...

---

### 37. Distributionally Robust Linear Regression With Block Lewis Weights

**Authors:** Naren Sarayu Manoj, Kumar Kshitij Patel

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00252v1)

**Summary:** We present an algorithm for the group distributionally robust (GDR) least squares problem. Given $m$ groups, a parameter vector in $\mathbb{R}^d$, and stacked design matrices and responses $\mathbf{A}$ and $\mathbf{b}$, our algorithm obtains a $(1+\varepsilon)$-multiplicative optimal solution using $\widetilde{O}(\min\{\mathsf{rank}(\mathbf{A}),m\}^{1/3}\varepsilon^{-2/3})$ linear-system-solves of matrices of the form $\mathbf{A}^{\top}\mathbf{B}\mathbf{A}$ for block-diagonal $\mathbf{B}$. Our t...

---

### 38. Sample Complexities of Estimating Gumbel--Max Watermark Proportions with and without Reduction to Pivotal Statistics

**Authors:** Shuwen Chai, Qiaosen Wang

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00224v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00224v2)

**Summary:** Watermarking promises statistical traceability of large language model (LLM) uses, but real documents rarely arrive as purely human-written or purely LLM-generated. This motivates a quantitative question beyond detection: what proportion of a document is generated from a pre-specified watermarked LLM? We study this watermark proportion estimation problem under the Gumbel--max watermarking mechanism, treating the next-token prediction distributions as unknown and arbitrary nuisance parameters sub...

---

### 39. Homogenization of $\ell_2$-Adversarial Training in High-Dimensions: Exact Dynamics under Stochastic Gradient Descent

**Authors:** Fabrizzio Sabelli

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00207v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00207v1)

**Summary:** We develop a framework for analyzing the learning dynamics of $\ell_2$-adversarial training of single-index models on Gaussian mixtures in the high-dimensional limit under streaming stochastic gradient descent (SGD). We derive deterministic equivalents for a broad class of statistics of the SGD iterates, including the adversarial risk and distance to adversarial optimality, in terms of the solution to a system of ODEs. We use them to study two idealized learning rate schedules: the Polyak stepsi...

---

### 40. GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity

**Authors:** Yong Yi Bay, Kathleen A. Yearick

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00152v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00152v1)

**Summary:** Three of the most popular methods for training language models to reason look like three different tricks. They are not. All three adjust a single number: standard deviation, reflecting how much a prompt's sampled answers disagree. When such a model is trained, it answers each problem many times, and an automatic checker marks every answer right or wrong. The standard deviation of those marks measures the disagreement: largest when the answers split evenly between right and wrong, and zero when ...

---

### 41. Uniform-in-time Propagation-of-Chaos for Stein Variational Gradient Descent

**Authors:** Krishnakumar Balasubramanian, Sayan Banerjee, Anna Korba

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00149v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00149v1)

**Summary:** We study uniform-in-time propagation-of-chaos for continuous-time Stein Variational Gradient Descent (SVGD). Classical finite-time propagation-of-chaos estimates for mean-field systems typically deteriorate rapidly with time and therefore do not directly explain the long-time relation between the finite-particle system and its mean-field limit. We obtain two complementary classes of uniform-in-time propagation-of-chaos results.   For broad distributional metrics, we introduce a cutoff strategy w...

---

### 42. Random Reshuffling Dominates Stochastic Gradient Descent

**Authors:** Zijian Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32005v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32005v1)

**Summary:** Stochastic Gradient Descent ($\textsf{SGD}$) is one of the most classical optimization algorithms with favorable theoretical guarantees, yet the practical implementation of $\textsf{SGD}$ differs subtly from its well-known form and is often referred to as Shuffling Stochastic Gradient Descent ($\textsf{Shuffling SGD}$). A particularly popular strategy in $\textsf{Shuffling SGD}$ is Random Reshuffling ($\textsf{RR}$), which has achieved great empirical success across numerous experiments. Despite...

---

### 43. Signed-Permutation Coordinate Transport for RMSNorm Transformers

**Authors:** John Sweeney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31963v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31963v1)

**Summary:** Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...

---

### 44. Accelerating Conformal Prediction via Approximate Leave-One-Out

**Authors:** Jiachen Cong, Jingbo Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31915v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31915v1)

**Summary:** While conformal prediction provides a general framework for uncertainty quantification in predictive inference, its application is often limited by computational cost. Recent methods, including Jackknife+ and Jackknife-minmax, achieve faster computation by trading a slight loss of efficiency relative to full conformal prediction, but still requires computing leave-one-out refits for all observations. In this paper, we further accelerate conformal prediction by incorporating approximate leave-one...

---

### 45. Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models

**Authors:** Keivan Faghih Niresi, Alice Cicirello, Olga Fink

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31804v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31804v1)

**Summary:** Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-...

---

### 46. Policy Optimization Achieves Data-Dependent Regret Bounds in MDPs with Unknown Transitions

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31769v1)

**Summary:** We study policy optimization for online episodic tabular Markov decision processes with unknown transition kernels, aiming for best-of-both-worlds guarantees together with data-dependent regret bounds. Recent work (Dann et al., 2023; Li et al., 2026) has shown that policy optimization can adapt to both adversarial and stochastic losses with first-order, second-order, and path-length bounds, but only under known transitions, leaving open whether such data-dependent guarantees are achievable by po...

---

### 47. On Optimal Data Splitting for Split Conformal Prediction

**Authors:** Sayan Das, Bahram Yaghooti, Todd A. Kuffner, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31600v1)

**Summary:** Conformal prediction and its variants, including the split conformal prediction, provide a distribution-free framework for uncertainty quantification by constructing prediction intervals or sets with finite-sample coverage guarantees. The statistical efficiency of these intervals depends critically on how the data are split into training and calibration samples. Despite its practical importance, a principled characterization of the training-calibration split that minimizes prediction interval le...

---

### 48. On the Convergence of Self-Improving Online LLM Alignment

**Authors:** Xudong Wu, Pangpang Liu, Vaneet Aggarwal, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31524v1)

**Summary:** The Self-Improving Alignment (SAIL) algorithm addresses distribution shift by reducing a bilevel formulation of the problem to an efficient, single-level method. Empirically, SAIL has demonstrated strong performance on this task. However, a formal analysis of its convergence properties has been lacking. We identify a key theoretical challenge: the standard SAIL objective function is not guaranteed to be strongly concave due to unfavorable properties of its Hessian. To address this limitation, we...

---

### 49. Contextual Slate GLM Bandits with Limited Adaptivity

**Authors:** Tanmay Goyal, Sukruta Prakash Midigeshi, Gaurav Sinha

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31449v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31449v1)

**Summary:** We investigate the contextual slate bandit problem with generalized linear rewards under limited adaptivity. At each round, the learner is presented with $N$ sets of items, where each item is represented by a $d$-dimensional feature vector. The learner then constructs a slate by selecting one item per set; the resulting slate yields a scalar reward sampled from a Generalized Linear Model (GLM). We propose algorithms under two limited-adaptivity settings: (a) Batched and (b) Rarely-Switching. For...

---

### 50. Sequential sparse Gaussian process quantile regression

**Authors:** Hugo Nicolas, Olivier Le Maître

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31284v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31284v1)

**Summary:** Quantile regression aims to estimate the conditional quantiles of a response variable from observed data. In a Bayesian setting, Gaussian process quantile regression provides uncertainty quantification but faces significant computational challenges due to the nonconjugacy of the asymmetric Laplace likelihood and the cost of posterior inference. We develop a sparse Gaussian process framework in which the quantile function is represented through a reduced set of inducing variables and posterior in...

---

