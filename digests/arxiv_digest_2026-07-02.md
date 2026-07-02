# arXiv Daily Digest - 2026-07-02

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Measuring the Gap Between Human and LLM Research Ideas

**Authors:** Ziyu Chen, Yilun Zhao, Arman Cohan

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01233v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01233v1)

**Summary:** LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-generated ideas from human researchers? To characterize this gap, we build a large-scale evaluation framework for ideation from high-quality human research papers. For each paper, we reverse-engineer a small set of closely related prior works that likely inspired its core idea. LLMs are then prompted...

---

### 2. Language-Critique Imitation Learning from Suboptimal Demonstrations

**Authors:** Chih-Han Yang, Dai-Jie Wu, Yun-Ping Huang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01225v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01225v1)

**Summary:** Prior work on imitation learning from suboptimal demonstrations typically relies on compressed supervision signals such as confidence estimates, discriminator scores, or importance weights. These scalar signals are inherently limited, as they cannot explicitly express intermediate reasoning about task progress, failure modes, or corrective actions. We propose a language-critique framework for imitation learning from suboptimal demonstrations that instead leverages natural language as a structure...

---

### 3. AutoMem: Automated Learning of Memory as a Cognitive Skill

**Authors:** Shengguang Wu, Hao Zhu, Yuhui Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01224v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01224v1)

**Summary:** Memory expertise is a learned skill: knowing what to encode, when to retrieve, and how to organize knowledge--a capacity known in cognitive science as metamemory. We bring this perspective to LLMs by treating memory management as a trainable skill. We promote file-system operations to first-class memory actions alongside task actions, letting the model itself decide how to manage its memory. This memory skill improves along two axes: the structure that supports it (prompts, file schemas, action ...

---

### 4. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States

**Authors:** Ben Slivinski, Michael Saldivar

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01223v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01223v1)

**Summary:** When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a...

---

### 5. The State-Prediction Separation Hypothesis

**Authors:** Giovanni Monea, Nathan Godey, Kianté Brantley, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01218v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01218v1)

**Summary:** Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining experiments across various scales. Our experiments show that state-prediction separation consistently off...

---

### 6. FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model

**Authors:** Chenyang Ma, Yue Yang, Radu Corcodel, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01212v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01212v1)

**Summary:** Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect high-quality real-world demonstrations. To address extreme long-h...

---

### 7. Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?

**Authors:** Zhi Chen, Zhensu Sun, Yuling Shi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01211v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01211v1)

**Summary:** Repository-level performance-optimization benchmarks such as GSO, SWE-Perf and SWE-fficiency evaluate coding agents by applying patches to real repositories and comparing runtime against unoptimized baselines and official reference patches. Their leaderboard scores are increasingly used as evidence of coding-agent progress, but those scores can conflate runtime instability, benchmark-specific scoring rules, and how many tasks are already solved by at least one public submission. We audit these i...

---

### 8. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation

**Authors:** Shayan Talaei, Abhinav Chinta, Devvrit Khatri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01208v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01208v1)

**Summary:** Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, ...

---

### 9. GPU-Parallel Linearization Error Bounds for Real-Time Robust Optimal Control of Nonlinear and Neural Network Dynamics

**Authors:** Jeffrey Fang, Keyi Shen, Anutam Srinivasan, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01203v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01203v1)

**Summary:** This paper studies real-time robust optimal control for uncertain nonlinear systems, where linear time-varying (LTV) approximations make planning tractable but require sound linearization error bounds (LEBs) to guarantee robust constraint satisfaction. We develop tight, differentiable, GPU-parallel LEBs for LTV approximations of nonlinear and neural network (NN) dynamics. For analytic dynamics, we introduce path-based Hessian bounds that are tighter than standard interval methods. For NN dynamic...

---

### 10. World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video

**Authors:** Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01202v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01202v1)

**Summary:** We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS represent...

---

### 11. Optimal Resource Utilization for Autonomous Laboratory Orchestrators

**Authors:** Austin McDannald, Julia Tisaranni, Howie Joress

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01188v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01188v1)

**Summary:** In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely different question. This can be challenging when dealing with real-world hardware constraints, especially so when there are multiple instruments with different capacities and throughputs. Here we demonstrate a 2-step method to address resource utilization for our autonomous platform for metal-organic framew...

---

### 12. Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations

**Authors:** Mehul Damani, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01181v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01181v1)

**Summary:** RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current RLVR methods optimize only what can be objectively scored, often neglecting subjective, non-verifiable aspects of human-like outputs, such as style and structure. This limitation leads to well-documented failure modes such as diversity collapse, unnatural-sounding responses, and reward hacking. We pr...

---

### 13. Diffusion-GR2: Diffusion Generative Reasoning Re-ranker

**Authors:** Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01170v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01170v1)

**Summary:** Generative reasoning re-rankers achieve strong recommendation accuracy by emitting a chain-of-thought before re-ordering a candidate list, but they are slow at inference: an autoregressive (AR) decoder spends one sequential forward pass per reasoning token, and the reasoning trace far exceeds the ranking it produces. To reduce this cost, block-diffusion language models decode many positions in parallel over a few denoising steps and are substantially faster, yet naively converting an AR re-ranke...

---

### 14. Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity

**Authors:** Brett Reynolds

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01153v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01153v1)

**Summary:** Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judg...

---

### 15. Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search

**Authors:** Binglin Ji, Anindya Sarkar, Hengchang Lu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01144v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01144v1)

**Summary:** While generative models have enabled training-free reward alignment, current methods typically excel in local exploration within narrow regions of the underlying distribution. These approaches struggle when preferences are unknown a priori and only revealed through sequential feedback-a scenario demanding broad exploration to uncover high-utility regions. To address this, we propose Sequentially-Controlled Interactive Multi-Particle Flow-Maps (IMPFM), a framework for sample-efficient online feed...

---

### 16. Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains

**Authors:** Changguo Jia, Tianqi Zhao, Runzhi He, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01136v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01136v1)

**Summary:** Agent skills package reusable operational knowledge for Large Language Model (LLM) agents, yet as they grow in scope, they become dependency-bearing artifacts whose identities, versions, and provenance remain implicit. This opacity already causes duplicated dependencies and inconsistent installations, exposing a gap that dependency management has yet to close. We introduce Agent Skill Supply Chains (ASSCs) to characterize mixed skill-package-service dependency graphs and help close this gap. Bor...

---

### 17. Autonomous Scientific Discovery via Iterative Meta-Reflection

**Authors:** Bingchen Zhao, Sara Beery, Oisin Mac Aodha

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01131v1)

**Summary:** Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. ...

---

### 18. Muon as a Residual Connection

**Authors:** Hao Huang

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01124v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01124v1)

**Summary:** Muon has recently emerged as one of the most effective optimizers for training large neural networks, yet its empirical success has been explained from several different perspectives. In this paper, we propose a simple mechanistic interpretation: Muon can be understood as an implicit residual connection during training. Specifically, orthogonalizing the update can sacrifice some immediate gradient fidelity while improving representation preservation for downstream layers. We study this trade-off...

---

### 19. Towards Developing a Multimodal Chat Assistant for University Stakeholders: RAG-based Approach

**Authors:** Md Abu Hanif Shaikh, Abdullah Al Shafi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01115v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01115v1)

**Summary:** University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-based chatbots are unable to handle complex, domain-specific queries and are not well-equipped to adapt to evolving institutional policies. As a fill-in-the-gap solution, we present the multimodal university chatbot with retrieval-augmented generation. The system combines the large language model with...

---

### 20. FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement

**Authors:** Haoran Hao, Shahram Najam Syed, Jeffrey Ichnowski, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01111v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01111v1)

**Summary:** Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning dat...

---

### 21. CausalMix: Data Mixture as Causal Inference for Language Model Training

**Authors:** Zinan Tang, Yukun Zhang, Shaomian Zheng, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01104v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01104v1)

**Summary:** In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address thi...

---

### 22. Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering

**Authors:** James C. Davis, Paschal C. Amusuo, Tanmay Singla, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01087v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01087v1)

**Summary:** Generative AI is shifting software engineering from a practice organized around scarce implementation effort toward one organized around abundant, low-cost code production. This shift changes the central engineering problem: not whether AI can generate useful code, but how engineers organize architectures, tools, evidence, and feedback loops so that AI-mediated development remains inspectable, correctable, and maintainable.   We study this problem through a first-person case study: a 12-week dev...

---

### 23. LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models

**Authors:** Arpita Nema, Hanwei Zhu, Xi Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01086v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01086v1)

**Summary:** The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 dive...

---

### 24. Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use

**Authors:** Song-Lin Lv, Weiming Wu, Rui Zhu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01084v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01084v1)

**Summary:** While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem setting characterized by distributional shifts across query, action, observation, and domain dimensions. To systematically diagnose its impact, we construct a controlled sandbox enviro...

---

### 25. Staleness-Learning Rate Scaling Laws for Asynchronous RLHF

**Authors:** Jingwei Song, Haofeng Xu, Jie Xiao, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01083v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01083v1)

**Summary:** High-throughput RLHF systems often decouple rollout generation from policy optimization, leading to the use of stale rollouts during learner updates. In this work, we study the effect of such staleness in asynchronous GRPO. We make the behavior policy explicit in the GRPO surrogate objective and distinguish between the surrogate-gradient mapping used by the learner and the true total derivative of a distribution-dependent population objective. Under assumptions of local boundedness, distribution...

---

### 26. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory

**Authors:** Zhishang Xiang, Zerui Chen, Yunbo Tang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01071v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01071v1)

**Summary:** Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlo...

---

### 27. Agentic generation of verifiable rules for deterministic, self-expanding reaction classification

**Authors:** Daniel Armstrong, Maarten Dobbelaere, Valentas Olikauskas, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01061v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01061v1)

**Summary:** Computer-assisted synthesis planning breaks target molecules into accessible precursors using large libraries of reaction rules that assign each transformation a deterministic, interpretable label. But chemistry is long-tailed, making manual encoding intractable, and existing tools rely on fixed rulesets that cannot adapt to new chemistries. Here we present a fully automated pipeline in which a multi-agent framework of large language models (LLMs) classifies reactions and writes the rules themse...

---

### 28. DART-VLN: Test-Time Memory Decay and Anti-Loop Regularization for Discrete Vision-Language Navigation

**Authors:** Shaoheng Zhang, Zhichen Li, Jie Mei

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01043v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01043v1)

**Summary:** Memory-based discrete vision-language navigation (VLN) agents must act under partial observability, yet even strong frozen backbones remain vulnerable at test time. Two common failure modes are stale historical evidence at memory readout and inefficient local backtracking during action selection. We present DART-VLN, a training-free test-time control framework for discrete VLN. DART-VLN combines Test-Time Memory Decay, a read-side memory reweighting rule that suppresses stale and redundant evide...

---

### 29. EchoRisk: A Multicentre Echocardiography Dataset and Benchmark for Cardio-Oncology

**Authors:** Grigorios Kalliatakis, Georgia Karanasiou, Georgios Manikis, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01039v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01039v1)

**Summary:** Therapy-induced cardiotoxicity is the leading non-oncological cause of treatment interruption in breast cancer patients, yet early, automated risk stratification from routine cardiac imaging remains an unsolved problem. We present EchoRisk, the first curated, multicentre, longitudinal echocardiography dataset with explicit cardiotoxicity labels, released as the primary technical reference for the EchoRisk-MICCAI 2026 challenge. The dataset comprises 422 patients enrolled in the EU-funded CARDIOC...

---

### 30. Behavior-Adaptive Conversational Agents: Toward a Fluid Personality Framework

**Authors:** Hasibur Rahman, Smit Desai

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01034v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01034v1)

**Summary:** Large language model (LLM)-based conversational agents (CAs) are now ubiquitous, creating new opportunities for AI-mediated behavior change. Their capacity to project nuanced personalities and adopt diverse metaphorical roles raises a design question: how should an agent's persona and personality be calibrated to the moment? Recent evidence suggests that (i) moderate personality expression outperforms low or high extremes on trust, enjoyment, and intention to adopt in goal-oriented tasks, and (i...

---

### 31. PedNStream: Scalable Network Flow Simulation for Pedestrian Traffic Management

**Authors:** Weiming Mai, Dorine Duives, Serge Hoogendoorn

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01021v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01021v1)

**Summary:** Large-scale crowd management requires pedestrian simulations that are both computationally efficient and compatible with feedback-based control. However, most open-source tools are either microscopic or not designed for network-scale closed-loop evaluation. This paper presents PedNStream (Pedestrian Network Flow Simulation), an open-source, Python-native simulator for macroscopic pedestrian network loading based on the Link Transmission Model (LTM). The framework extends LTM-based pedestrian mod...

---

### 32. Reading Order Inference for Complex Document Layouts

**Authors:** Iddo Hakim, Sharva Gogawale, Omer Ventura, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01018v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01018v1)

**Summary:** Reading order inference remains a critical bottleneck in the digitization of complex historical manuscripts, where pages contain multiple spatially interleaved reading streams, the canonical example being the Glossa Ordinaria layout, in which a central text is surrounded by commentaries that wrap around it in non-rectangular, non-convex regions. We present a training-free, graph-based framework: each OCR text line becomes a node in a directed candidate-transition graph, edges are scored by a wei...

---

### 33. Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads

**Authors:** Aryo Pradipta Gema, Beatrice Alex, Pasquale Minervini

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01002v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01002v1)

**Summary:** In long-context use, large language models frequently synthesize answers from the meaning of a relevant context span rather than literally copy-pasting them. Identifying which attention heads perform this synthesis matters for interpreting long-context model behavior. Yet existing detectors miss these heads by construction: they reward heads whose attended token matches the generated token, a literal-copy criterion that captures where a head reads but not what it writes through its output-value ...

---

### 34. SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests

**Authors:** Yaoqi Guo, Yang Liu, Jie M. Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00990v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00990v1)

**Summary:** Large language model (LLM)-based software engineering agents are increasingly developed to resolve software issues by generating patches from issue reports and code repositories. Bug reproduction tests (BRTs) are an important building block for such agents and have been shown useful for patch validation. However, it remains unclear whether BRTs can also help the more central stage of patch generation. We first conduct a preliminary study and find that directly using advanced BRT generators to gu...

---

### 35. SenseWalk: Agent-Based Semantic Trajectory Simulation Powered by Large Language Models in Zoned Environments

**Authors:** Ziyue Lin, Xinhang Xie, Kangyi Wang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00989v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00989v1)

**Summary:** Semantic trajectory analysis has recently emerged as an approach for modeling human movement by capturing implicit patterns and behaviors through semantic information (e.g., visitors' profiles and goals) beyond raw spatial paths to better understand why people move in certain ways. However, analyzing semantic trajectories in real-world scenarios remains challenging, as collecting high-quality data is costly and often lacks rich semantic information. Meanwhile, existing simulation tools require s...

---

### 36. TRCGL-Net: A Long-Tailed Multi-Label Chest X-Ray Classification Framework with Generative Data Augmentation and Label Co-Occurrence Modeling

**Authors:** Tong Shao, Hongshun Ling, Li Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00975v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00975v1)

**Summary:** Chest X-ray multi-label classification is a core task in intelligent medical imaging diagnosis. However, real clinical data often exhibit extreme long-tailed distributions, leading to degraded performance on rare diseases in tail classes. This issue is not only driven by data scarcity but also by two intrinsic factors:1) attenuation of tail-class lesion representations under complex anatomical backgrounds, and 2) dominance of head classes in modeling label co-occurrence relationships. To address...

---

### 37. Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering

**Authors:** Louis Donaldson, Connor Walker, Koorosh Aslansefat, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00972v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00972v1)

**Summary:** Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-Augmented Generation (RAG) framework in which planner, evaluator and generator stages produce uncertainty signals derived from semantic divergence and generator self-evaluation. These signals are propagated through a Bayesian Network (BN) to estimate system-level uncertainty and ...

---

### 38. Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations

**Authors:** Alexander Chemeris, Ming Jin, Randall Balestriero

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00956v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00956v1)

**Summary:** Time-series models are often evaluated by what they can forecast or classify, but those scores do not show whether their representations preserve the process state a user may want to inspect: event timing, phase, amplitude, frequency, or regime variables. We introduce Aionoscope, a generator-based diagnostic tool for debugging latent-state accessibility in frozen time-series representations. Aionoscope separates process generation from observation rendering, producing seeded synthetic streams wi...

---

### 39. Learning Cardiac Motion Priors for Implicit Neural Representations

**Authors:** Andrew Bell, George Webber, Andrew P King, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00955v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00955v1)

**Summary:** Implicit neural representations (INRs) are well suited to cardiac motion estimation, providing continuous, compact representations of motion fields. However, fitting an INR to each image sequence is time-consuming and sensitive to the optimisation trajectory. Learned priors can help guide optimisation towards plausible motion fields and enable faster adaptation, but learning priors for cardiac motion INRs remains under-explored. In this work, we compare four strategies for learning cardiac motio...

---

### 40. Post-Training Pruning for Diffusion Transformers

**Authors:** Chengzhi Hu, Xuewen Liu, Jing Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00927v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00927v1)

**Summary:** Diffusion Transformers (DiTs) have demonstrated impressive performance in image generation but suffer from substantial computational overhead and resource consumption. Post-training pruning offers a promising solution; however, due to DiTs' unique architectural design and parameter distribution, traditional pruning methods are inapplicable, leading to significant performance degradation. Specifically, prior methods developed for LLMs, which derive metrics through a series of approximations, ampl...

---

### 41. Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm

**Authors:** Midhun Parakkal Unni, Samuel Kaski

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00926v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00926v1)

**Summary:** Generalizing machine learning models to environments that differ from their training distribution remains a critical hurdle, particularly when data from the target domain is entirely or partially unavailable. We propose Generative Meta-Learning with Human Feedback (GMHF), a novel framework that bridges this domain gap by leveraging expert intuition to guide data synthesis. Grounded in a theoretical analysis of generalization error, we derive bounds demonstrating that aligning the distribution of...

---

### 42. Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

**Authors:** Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00924v1)

**Summary:** Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization ...

---

### 43. From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives

**Authors:** Aayush Aluru, Chloe Ho, Muhammad Hammouri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00918v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00918v1)

**Summary:** Although large language models (LLMs) have demonstrated impressive creative fiction generation, they struggle to maintain narrative consistency and coherent plot lines in long-form stories. In this work, we introduce a unified framework for long-form narrative generation and verification. MAGNET, a multi-agent goal-driven narrative engine for storytelling, generates stories with persona-grounded character agents that propose actions based on a shared world state and evolving story goals, while A...

---

### 44. Valdi: Value Diffusion World Models

**Authors:** Christopher Lindenberg, Kashyap Chitta

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00917v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00917v1)

**Summary:** World models can enable Model Predictive Control (MPC), but this requires dynamics prediction that is both fast enough for online use and expressive enough to represent uncertain futures. Diffusion models offer a natural mechanism for modeling uncertain dynamics, yet their iterative inference procedure makes them difficult to use for low-latency latent planning. We bridge this gap with Value Diffusion World Models (Valdi), combining end-to-end online training for MPC with a latent diffusion dyna...

---

### 45. Two AI Metrics Diverged: Will it Make All the Difference?

**Authors:** Alex Fogelson, Zachary A. Brown, Hans Gundlach, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00913v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00913v1)

**Summary:** As exponential compute scaling continues, will the capabilities of frontier AI models outstrip what is accessible to developers on a small fixed budget? Or will capabilities converge, with "meek models inheriting the earth"? Building on Gundlach et al. (2025b), we show that the answer depends on how we value and measure AI capabilities. We discuss conventional performance measures and show that, while validation loss shows a shrinking gap, on other metrics frontier models grow their lead forever...

---

### 46. DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors

**Authors:** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00889v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00889v1)

**Summary:** We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single p...

---

### 47. Improving Sparse-View 3DGS Generalization via Flat Minima Optimization

**Authors:** Kangmin Seo, Sangeek Hyun, MinKyu Lee, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00885v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00885v1)

**Summary:** Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small par...

---

### 48. Self-Evolving Agents with Anytime-Valid Certificates

**Authors:** Biswa Sengupta

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00871v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00871v1)

**Summary:** Self-evolving agents violate the assumption behind most learning-theoretic guarantees: the data, evaluator, components, and hypothesis space are produced by the policy being updated. We present \textbf{SEA}, an architecture that confines self-modification to a small steering adapter and a versioned harness around a \emph{frozen} base model and admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget. Five loop controllers compos...

---

### 49. CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models

**Authors:** Qizhi Jiang, Shuo Wang, Pei Ke, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00862v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00862v1)

**Summary:** Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods predominantly apply uniform length reduction or rely on coarse-grained difficulty estimation, often leading to performance degradation on difficult problems. To address this limitation, we pro...

---

### 50. Meta-Transfer Learning for mmWave Beam Alignment

**Authors:** Ahmet Nuri Cevik, Sinem Coleri

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00860v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00860v1)

**Summary:** Millimeter-wave (mmWave) beam alignment plays a critical role in next-generation wireless systems, yet its efficient implementation remains challenging. Meta-learning and transfer learning have been explored to enable deep learning-based beam prediction models to rapidly adapt to unseen environments; however, existing meta-learning approaches adapt the entire network and are trained from random initialization, leading to a large number of updated parameters and a high meta-training cost, while t...

---

## cs.CL

**50 papers**

### 1. Measuring the Gap Between Human and LLM Research Ideas

**Authors:** Ziyu Chen, Yilun Zhao, Arman Cohan

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01233v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01233v1)

**Summary:** LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-generated ideas from human researchers? To characterize this gap, we build a large-scale evaluation framework for ideation from high-quality human research papers. For each paper, we reverse-engineer a small set of closely related prior works that likely inspired its core idea. LLMs are then prompted...

---

### 2. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

**Authors:** Zijian Zhang, Rizhen Hu, Athanasios Glentis, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01232v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01232v1)

**Summary:** Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that trai...

---

### 3. AutoMem: Automated Learning of Memory as a Cognitive Skill

**Authors:** Shengguang Wu, Hao Zhu, Yuhui Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01224v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01224v1)

**Summary:** Memory expertise is a learned skill: knowing what to encode, when to retrieve, and how to organize knowledge--a capacity known in cognitive science as metamemory. We bring this perspective to LLMs by treating memory management as a trainable skill. We promote file-system operations to first-class memory actions alongside task actions, letting the model itself decide how to manage its memory. This memory skill improves along two axes: the structure that supports it (prompts, file schemas, action ...

---

### 4. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States

**Authors:** Ben Slivinski, Michael Saldivar

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01223v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01223v1)

**Summary:** When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a...

---

### 5. The State-Prediction Separation Hypothesis

**Authors:** Giovanni Monea, Nathan Godey, Kianté Brantley, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01218v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01218v1)

**Summary:** Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining experiments across various scales. Our experiments show that state-prediction separation consistently off...

---

### 6. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation

**Authors:** Shayan Talaei, Abhinav Chinta, Devvrit Khatri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01208v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01208v1)

**Summary:** Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, ...

---

### 7. Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations

**Authors:** Mehul Damani, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01181v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01181v1)

**Summary:** RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current RLVR methods optimize only what can be objectively scored, often neglecting subjective, non-verifiable aspects of human-like outputs, such as style and structure. This limitation leads to well-documented failure modes such as diversity collapse, unnatural-sounding responses, and reward hacking. We pr...

---

### 8. QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling

**Authors:** Michael Y. Li, Anthony Zhan, Kanishk Gandhi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01179v1)

**Summary:** Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independently, wasting inference compute on redundant solutions. This waste seems unavoidable. After all, independence is what makes parallel sampling trivial to scale. However, this tradeoff is not fundamental: there is a rich design space of samplers that generate correlated but exact samples entirely in p...

---

### 9. Disentangling Speaker and Language Effects in Cross-Lingual Speaker Verification for Iberian Languages

**Authors:** Pol Buitrago, Javier Hernando

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01161v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01161v1)

**Summary:** Cross-lingual speaker verification (SV) systems typically exhibit performance degradation when enrollment and test utterances are spoken in different languages. However, standard evaluation protocols confound language mismatch with inter-speaker variability, as evaluation is generally performed with different speakers across languages.   In this work, we introduce a bilingual same-speaker evaluation set for five Iberian languages, enabling analysis of cross-lingual SV under constant speaker iden...

---

### 10. Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity

**Authors:** Brett Reynolds

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01153v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01153v1)

**Summary:** Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judg...

---

### 11. AGC-Bench: Measuring Artificial General Creativity

**Authors:** Roger Beaty, Vijeta Deshpande, Clin K. Y. Lai, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01152v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01152v1)

**Summary:** Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to LLMs, but a unified benchmark of AI creativity remains elusive. We introduce AGC-Bench, an artificial general creativity benchmark built from a systematic review of the AI creativity literature (3,101 papers screened, 497 benchmarks identified), paired with an agentic harness that converts idiosyncra...

---

### 12. $\text{Log}_\text{b}$Quant: Quantizing Language Models in Logarithmic Space

**Authors:** Jeremias Bohn, Tizian Dippold, Mahdi Koubaa, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01127v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01127v1)

**Summary:** Quantization has become an invaluable tool to reduce memory requirements and inference speed of modern language models, in particular to make them available for consumer setups and edge devices. While previous work has primarily focused on uniform quantization codebooks, such approaches are prone to suboptimal representations due to low-frequency high-magnitude weights. We introduce Log$_\text{b}$Quant, a novel logarithmic quantization approach with adjustable bases, to adapt to common parameter...

---

### 13. Towards Developing a Multimodal Chat Assistant for University Stakeholders: RAG-based Approach

**Authors:** Md Abu Hanif Shaikh, Abdullah Al Shafi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01115v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01115v1)

**Summary:** University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-based chatbots are unable to handle complex, domain-specific queries and are not well-equipped to adapt to evolving institutional policies. As a fill-in-the-gap solution, we present the multimodal university chatbot with retrieval-augmented generation. The system combines the large language model with...

---

### 14. CausalMix: Data Mixture as Causal Inference for Language Model Training

**Authors:** Zinan Tang, Yukun Zhang, Shaomian Zheng, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01104v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01104v1)

**Summary:** In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address thi...

---

### 15. Clinician-Level Agreement Without Clinical Caution: LLM Evaluator Limits in Medical AI Benchmarking

**Authors:** William Philipp, Finn Fassbender, Thorsten Langer, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01103v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01103v1)

**Summary:** Open-response evaluation provides stronger clinical validity than multiple-choice benchmarks but creates a scoring bottleneck that motivates automated LLM-asa-Judge approaches. Whether such evaluators replicate clinical calibration and caution, however, remains untested. We introduce MedQADE, the first standardised open-response clinical benchmark for German, a major clinical language lacking native evaluation infrastructure, comprising 3,800 items annotated by ten practising physicians and nine...

---

### 16. Message Passing Enables Efficient Reasoning

**Authors:** Xuecheng Liu, Daman Arora, Gokul Swamy, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01077v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01077v1)

**Summary:** While inference-time scaling has improved the reasoning abilities of large language models (LLMs), the need to generate long chains-of-thought (CoTs) is a computational bottleneck. Thus, in contrast to sequential scaling methods like CoT, recent parallel scaling techniques instead use fork and join (FJ) primitives to divide work across multiple LLM threads. However, in the fork-join paradigm, threads are typically transient and do not communicate pointwise with one another which limits scalabili...

---

### 17. Agentic generation of verifiable rules for deterministic, self-expanding reaction classification

**Authors:** Daniel Armstrong, Maarten Dobbelaere, Valentas Olikauskas, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01061v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01061v1)

**Summary:** Computer-assisted synthesis planning breaks target molecules into accessible precursors using large libraries of reaction rules that assign each transformation a deterministic, interpretable label. But chemistry is long-tailed, making manual encoding intractable, and existing tools rely on fixed rulesets that cannot adapt to new chemistries. Here we present a fully automated pipeline in which a multi-agent framework of large language models (LLMs) classifies reactions and writes the rules themse...

---

### 18. Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates

**Authors:** Elias Najarro, Ane Espeseth, Eleni Nisioti, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01047v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01047v1)

**Summary:** Complexity and interpretability rarely coincide: systems rich enough for complex behaviours to emerge are usually too opaque to question, while transparent ones are too simple for anything complex to emerge. A single large language model (LLM) is a static artefact, hardly exhibiting any of the emergent properties we associate with life. This changes through interaction: populations of LLMs display emergent dynamics absent from isolated models. Furthermore, LLMs can be endowed with persistent mem...

---

### 19. Behavior-Adaptive Conversational Agents: Toward a Fluid Personality Framework

**Authors:** Hasibur Rahman, Smit Desai

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01034v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01034v1)

**Summary:** Large language model (LLM)-based conversational agents (CAs) are now ubiquitous, creating new opportunities for AI-mediated behavior change. Their capacity to project nuanced personalities and adopt diverse metaphorical roles raises a design question: how should an agent's persona and personality be calibrated to the moment? Recent evidence suggests that (i) moderate personality expression outperforms low or high extremes on trust, enjoyment, and intention to adopt in goal-oriented tasks, and (i...

---

### 20. Evidence-Supported Credit Risk Report Generation Using News-Centric Financial Knowledge Graphs

**Authors:** Rocio Jimenez-Villen, Ziwei Xu, Ying Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01023v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01023v1)

**Summary:** Financial markets evolve in response to real-world events reported in news, yet these drivers often remain implicit in text. To better explain market dynamics, event-market relations must be explicitly modeled through factual, company-centric, and environment-aware knowledge graphs. We present FinKG-News, a framework that automatically constructs such graphs by extracting news events as anchors linked to companies. Using FinKG-News as grounded evidence that integrates events, news, and company d...

---

### 21. Reading Order Inference for Complex Document Layouts

**Authors:** Iddo Hakim, Sharva Gogawale, Omer Ventura, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01018v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01018v1)

**Summary:** Reading order inference remains a critical bottleneck in the digitization of complex historical manuscripts, where pages contain multiple spatially interleaved reading streams, the canonical example being the Glossa Ordinaria layout, in which a central text is surrounded by commentaries that wrap around it in non-rectangular, non-convex regions. We present a training-free, graph-based framework: each OCR text line becomes a node in a directed candidate-transition graph, edges are scored by a wei...

---

### 22. Understanding Large Language Models

**Authors:** Yannik Keller, Thomas Eisenmann

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01006v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01006v1)

**Summary:** Large Language Models (LLMs) represent one of the most significant advances in AI and natural language processing in recent years. Still, many pressing questions about their mechanisms, capabilities, and relationship to human cognition remain highly debated. This chapter aims to outline our current understanding of LLMs by discussing recent evidence on emerging capabilities and their mechanistic implementation within processing layers. We begin with a concise overview of the Transformer architec...

---

### 23. Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads

**Authors:** Aryo Pradipta Gema, Beatrice Alex, Pasquale Minervini

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01002v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01002v1)

**Summary:** In long-context use, large language models frequently synthesize answers from the meaning of a relevant context span rather than literally copy-pasting them. Identifying which attention heads perform this synthesis matters for interpreting long-context model behavior. Yet existing detectors miss these heads by construction: they reward heads whose attended token matches the generated token, a literal-copy criterion that captures where a head reads but not what it writes through its output-value ...

---

### 24. KnowledgeDebugger -- an Exploration Tool for Knowledge Localization and Editing in Transformers

**Authors:** Eric Benz, Lennart Stöpler, Nikolai Bolik, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01000v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01000v1)

**Summary:** Recent research has increasingly focused on understanding how Transformers store and process knowledge, as well as how this knowledge can be edited. Research work in this area is often conducted in two phases: first, phenomena are explored on individual samples. Then, when results appear promising, more statistically robust experiments follow. To support the first phase, we propose KnowledgeDebugger, a GUI-based exploration tool for knowledge localization and editing in Transformers. Our tool - ...

---

### 25. Svarna: An Open Corpus Workbench for Modern Greek

**Authors:** Stergios Chatzikyriakidis

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00970v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00970v1)

**Summary:** This paper introduces Svarna, a free, open-source, web-based corpus workbench for modern Greek. Svarna integrates five databases covering various registers, institutional, literary, dialectal, social media, and historical, to provide a total of more than 507 million words and around 29 million sentences. This platform addresses the chronic gaps in Greek language technology. Although various corpus resources exist, they are scattered across different platforms, and in many cases, institutional ac...

---

### 26. Quantifying the Affective Gap: A Zero-Shot Evaluation of LLMs on Fine-Grained Emotion Taxonomies

**Authors:** Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00968v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00968v1)

**Summary:** Emotion recognition in natural language is a foundational challenge in affective computing, with critical implications for human-computer interaction, mental health support, and conversational AI. This paper presents a rigorous, unified zero-shot evaluation of three leading commercial large language models: Claude (claude-sonnet-4-6), ChatGPT (GPT-5.4), and Gemini (gemini-2.5-flash). The models were queried through their respective production APIs as of April 2026 on a fine-grained 13-class emot...

---

### 27. Persona Non Grata: LLM Persona-Driven Generations in MCQA are Unstable in Distinct Dimensions

**Authors:** César Guerra-Solano, Xiang Lorraine Li

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00937v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00937v1)

**Summary:** Persona-driven generations (PDGs) have seen prolific use in research and industry applications, where a large language model (LLM) takes on a 'persona' while completing some task. While persona expressed through free-form text (like dialogue) has substantial work investigating stability or consistency, relatively, persona expressed in non-text-heavy outputs (like in multiple-choice question answering, or MCQA) is often overlooked. We work to address this gap, seeking to understand the instabilit...

---

### 28. Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

**Authors:** Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00924v1)

**Summary:** Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization ...

---

### 29. From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives

**Authors:** Aayush Aluru, Chloe Ho, Muhammad Hammouri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00918v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00918v1)

**Summary:** Although large language models (LLMs) have demonstrated impressive creative fiction generation, they struggle to maintain narrative consistency and coherent plot lines in long-form stories. In this work, we introduce a unified framework for long-form narrative generation and verification. MAGNET, a multi-agent goal-driven narrative engine for storytelling, generates stories with persona-grounded character agents that propose actions based on a shared world state and evolving story goals, while A...

---

### 30. Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents

**Authors:** Ádám Kovács, Bowei He, Xue Liu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00895v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00895v1)

**Summary:** Hallucination detection for retrieval-augmented generation (RAG) is usually evaluated on natural-language document evidence. However, grounded generation systems increasingly rely on structured inputs: source code, developer-tool output, markdown documents, tables, and repository metadata. We introduce a unified benchmark for span-level hallucination detection over code, tool output, structured documents, and existing natural-language RAG datasets. The benchmark is built by starting from grounde...

---

### 31. MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages

**Authors:** Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00890v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00890v1)

**Summary:** Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development. We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems. For many medium- and lower-resource European languages, this is the largest openly available pre-training resource. On a broad multilingua...

---

### 32. How Ethos and Pathos Appeals Resonate in Reader Interpretations of Social Media Messages

**Authors:** Ewelina Gajewska, Katarzyna Budzynska, Jaroslaw Chudziak, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00873v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00873v1)

**Summary:** Rhetorical strategies and their influence on audiences are often studied through social media posts and comments. However, this focus overlooks the universal audience, which is the majority of readers who remain silent and do not explicitly express how a message affects them. This study investigates how two classical modes of persuasion, ethos and pathos, resonate in the silent audience's interpretations of meaning. Using a dataset of social media sentences paired with human-written interpretati...

---

### 33. Self-Evolving Agents with Anytime-Valid Certificates

**Authors:** Biswa Sengupta

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00871v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00871v1)

**Summary:** Self-evolving agents violate the assumption behind most learning-theoretic guarantees: the data, evaluator, components, and hypothesis space are produced by the policy being updated. We present \textbf{SEA}, an architecture that confines self-modification to a small steering adapter and a versioned harness around a \emph{frozen} base model and admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget. Five loop controllers compos...

---

### 34. Dynamic Bidirectional Pattern Memory: A Production-Scale Empirical Characterisation of Inference-Time Gating in Clinical NLP

**Authors:** Ali H. Lazem, William Teahan

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00870v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00870v1)

**Summary:** We study inference-time pattern-memory gating in a production-scale clinical natural language processing (NLP) pipeline. The pipeline pairs a generator (Llama-3.3 70B) proposing extractions with a verifier (MMed-Llama-3.1 70B) accepting or rejecting them, over 167,034 PMC-Patients narratives, and adds a lightweight memory that learns at deployment which extractions to filter, so the verifier need not re-examine candidates already seen to fail. We report four findings. First, learning filtering r...

---

### 35. CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models

**Authors:** Qizhi Jiang, Shuo Wang, Pei Ke, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00862v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00862v1)

**Summary:** Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods predominantly apply uniform length reduction or rely on coarse-grained difficulty estimation, often leading to performance degradation on difficult problems. To address this limitation, we pro...

---

### 36. Recovering Input Text from Hidden States: Study of Gradient-Based Inversion of Decoder-Only Language Models

**Authors:** Mikołaj Słowikowski, Maciej Witold Majewski

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00852v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00852v1)

**Summary:** This work studies the hidden-state inversion problem: recovering the original input token sequence of a decoder-only language model from its last-layer hidden states. Rather than treating inversion as a one-shot reconstruction, we study it as a continuous embedding-space optimisation in which a soft proxy is driven towards the leaked target without any hard-token projection during the search, and a token is committed only once, at the end of the inner loop. This design choice has two consequence...

---

### 37. The Course of News Events: A Comparison of Bottom-Up and Top-Down Approaches for Collecting Text-Based Data about Disasters

**Authors:** Brielen Madureira, Andreas Niekler, Mariana Madruga de Brito

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00849v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00849v1)

**Summary:** News articles are an important source of information on disaster impacts and adaptation. A key methodological challenge in socio-environmental studies is how to select a representative data sample. Two approaches are common: querying news databases top-down with the aid of an existing disaster inventory or using NLP methods to cluster news texts bottom-up based on temporal and spatial features. Using a dataset of German news about landslides worldwide, we compare these approaches and discuss var...

---

### 38. MetaHOPE: A Metaphor-Oriented Evaluation Framework for Analysing MT and LLM Translation Errors

**Authors:** Jiahui Liang, Lifeng Han

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00848v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00848v1)

**Summary:** In this opinion paper, we propose MetaHOPE, an error severity-aware annotation framework for evaluating metaphor translations. Metaphors present challenges for machine translation (MT) and natural language understanding and processing (NLU, NLP), because it presents the features of semantic complexity, contextual dependency, and cultural embeddings that can lead to ambiguity issues for NLP models. To investigate how state-of-the-art NLP models perform on translating metaphors, we select three re...

---

### 39. What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It

**Authors:** Ananto Nayan Bala

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00725v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00725v1)

**Summary:** Retrieval-augmented generation (RAG) under a fixed reader-context budget forces a selection problem: of the evidence retrieved, only a fraction can be shown to the reader. We argue that document recall -- the standard retrieval metric -- is the wrong quantity to optimize in this regime, and we make two contributions. First, as a general contribution, we introduce answer-in-context, a diagnostic that measures whether a gold answer survives as a contiguous span in the packed reader context (not th...

---

### 40. MSQA: A Natively Sourced Multilingual and Multicultural SimpleQA Benchmark

**Authors:** Xianru Chen, Yukai Huang, Mingxiang Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00724v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00724v1)

**Summary:** Multilingual fluency often invites a stronger assumption: a model that can speak a user's language must also understand the culture encoded by that language. We call this the Illusion of Cultural Alignment. To test this assumption directly, we introduce MSQA, a benchmark of 1,064 natively sourced questions across 11 language groups, five cultural dimensions, and three difficulty tiers. Unlike translated benchmarks, MSQA targets locally grounded knowledge and reduces shortcuts from English-centri...

---

### 41. Self-conditioned Flow Map Language Models via Fixed-point Flows

**Authors:** Jaehoon Yoo, Wonjung Kim, Floor Eijkelboom, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00714v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00714v1)

**Summary:** Self-conditioning is a core technique that enhances continuous flow-based language models, where the model learns to denoise generated text by conditioning on its own denoising estimate. While empirically successful, its performance improvements are poorly understood. Moreover, there is growing interest in the use of few-step generators based on flow maps, for which how to leverage self-conditioning is unclear. Here, we show that flow language models with self-conditioning solve a fixed-point it...

---

### 42. YOMI-Bench: A Benchmark for Evaluating Kanji Reading and Phonological Understanding of LLMs for Japanese

**Authors:** Ryota Mibayashi, Hiroya Takamura, Hitomi Yanaka

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00664v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00664v1)

**Summary:** We propose YOMI-Bench, a benchmark for evaluating kanji reading and phonological understanding of large language models (LLMs) for Japanese. In Japanese, a single kanji character often has multiple possible readings, making it difficult to infer the correct reading from surface-level text alone. Due to these linguistic characteristics, it is empirically known that LLMs exhibit low performance in kanji reading for Japanese. The proposed YOMI-Bench consists of four tasks specifically designed to e...

---

### 43. Faithful by Definition: Emotion Analysis via Natural Semantic Metalanguage Explications

**Authors:** Frank Xing, Erik Cambria

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00661v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00661v1)

**Summary:** Explanations for emotion classifiers are usually produced post hoc, with no guarantee that they reflect the computation behind the label. We present an explication interface for event-based emotion analysis. A parser maps the input text to an explication, a short script in the closed vocabulary of Natural Semantic Metalanguage organized into twelve typed slots, and a fixed decision list of rules transcribed from published semantic definitions computes the label from the explication alone. The fa...

---

### 44. Auditing Forgetting in Limited Memory Language Models

**Authors:** Arya Raeesi, Hanna Roed

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00605v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00605v1)

**Summary:** Limited Memory Language Models (LMLMs) externalize factual knowledge to a database to enable deletion-based unlearning without retraining. Existing evaluations measure post-deletion correctness in aggregate and cannot tell whether a deleted fact persists through residual parametric memory, alternative retrieval paths, or near-neighbor retrieval artifacts. We propose a causal auditing framework that holds the model fixed and varies the database state at inference time across three interventions: ...

---

### 45. "Don't Say It!": Constraints, Compliance, and Communication when Language Models Play Taboo

**Authors:** Sara Candussio, Francesca Padovani, Daniel Scalena, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00601v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00601v1)

**Summary:** The game of Taboo requires describing a target word without using a set of forbidden words, so that other players can guess it. This deceptively simple task combines strict lexical constraints with the need for communicatively effective descriptions, making it a compelling playground for examining how LLMs navigate competing demands at inference time. We evaluate two open-weight models under conditions that intervene at progressively deeper levels of the generative process, from prompting to gen...

---

### 46. Multi-Turn Agentic Scientific Literature Search via Workflow Induction

**Authors:** Jisen Li, Bingxuan Li, Nanyi Jiang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00597v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00597v1)

**Summary:** Scientific literature search often requires more than retrieving papers from a single query: users' intents are underspecified, preference-dependent, and evolve through interaction. Existing search agents typically rely on fixed pipelines or implicit language-only reasoning, making their search strategies difficult to control, inspect, and refine. We introduce PaperPilot, a multi-turn literature search agent that frames scientific search as workflow induction. Given an anchor paper and a user qu...

---

### 47. Low Perplexity is Repetition: A One-Dimensional Self-Conditioning Attractor in Continuous Diffusion LMs

**Authors:** Shuai Zhang, Zijie Chen, Hongliang He, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00588v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00588v1)

**Summary:** Continuous diffusion language models such as ELF report record-low generative perplexity (Gen-PPL). We find a catch: these models repeat far more than human text, and Gen-PPL rewards rather than penalizes that repetition, so its low scores overstate quality. Strip the repetition and ELF-B's Gen-PPL rises from $19.5$ to $27.7$; the smallest model even posts the best Gen-PPL because it repeats most. We trace the repetition to its source: a contractive attractor along a \emph{single direction} in t...

---

### 48. Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign Images Combine

**Authors:** Jiaxian Lv, Shiyao Cui, Yingkang Wang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00576v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00576v1)

**Summary:** Multi-image content has become an increasingly prevalent form of visual communication in social media, giving rise to a new safety issue, multi-image implicit toxicity (MIIT), where each image appears benign in isolation, but harmful semantics emerge when the images are interpreted jointly. MIIT is particularly challenging for existing commercial moderation APIs and models due to the lack of explicit risky cues in each image. This paper aims to study how to identify MIIT. We first provide a form...

---

### 49. Dual-Confidence Contrastive Decoding for Retrieval-Augmented Generation

**Authors:** Raymond Li, Md Tawkat Islam Khondaker, Amirhossein Abaskohi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00570v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00570v1)

**Summary:** Retrieval-augmented generation (RAG) increasingly requires models to answer questions from multiple retrieved documents, where only some sources are relevant and the retrieved bundle may contain stale, noisy, or conflicting evidence. Existing contrastive decoding methods primarily focus on resolving conflicts between the model's internal memory and the retrieved context. In contrast, we study the complementary problem of intra-context conflict in multi-document RAG. To evaluate this setting, we ...

---

### 50. A Task-State Representation for Long-Horizon Mobile GUI Agents

**Authors:** Yujie Zheng, Zikang Liu, Xin Zhao, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00502v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00502v1)

**Summary:** While long-horizon mobile GUI agents typically rely on thought-action-observation loops, they struggle to separate persistent task states from transient screen observations. As execution histories grow, this entanglement imposes a severe context burden, causing agents to forget initial requirements, hallucinate progress, or repeatedly interact with stale interfaces. To address this, we introduce Task-State Representation (TSR), a training-free framework that explicitly decouples task state from ...

---

## cs.CV

**50 papers**

### 1. Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models

**Authors:** Yue Han, Chong Li, Zhening Liu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01222v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01222v1)

**Summary:** Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data with rich surface appearance. In contrast, visual generative models are trained on datasets several orders of magnitude larger and excel at modeling complex visual patterns. Motivated by this gap, we introduce Ink3D, a framework that bridges 3D generation with large-scale video generative models to s...

---

### 2. Linkify: Learning from Interface-Augmented Assembly Graphs

**Authors:** Anushrut Jignasu, Daniele Grandi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01205v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01205v1)

**Summary:** We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have focused largely on isolated parts or monolithic assemblies, the rich geometric information at the interfaces between parts, where function is realized, remains underexplored. We address this gap by recomputing high-fidelity interface geometry for the Fusion 360 Gallery Assembly dataset, correcting mi...

---

### 3. World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video

**Authors:** Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01202v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01202v1)

**Summary:** We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS represent...

---

### 4. Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning

**Authors:** Hongxing Li, Xiufeng Huang, Dingming Li, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01191v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01191v1)

**Summary:** Fine-grained visual reasoning remains challenging for vision-language models, especially when small but critical visual cues are buried in high-resolution images. Existing approaches rely on repeated cropping or test-time visual search to introduce local evidence, but they typically do not explicitly distinguish perception from reasoning. In this paper, we propose Perceive-to-Reason (P2R), a unified framework that formulates fine-grained visual reasoning as a two-stage process: the model first l...

---

### 5. High-dimensional Embedding Prior for Noisy K-space Domain MRIReconstruction

**Authors:** Yu Guan, Tianjia Huang, Qinrong Cai, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01176v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01176v1)

**Summary:** Magnetic resonance imaging (MRI) reconstruction under realistic acquisition conditions can be fundamentally viewed as estimating the underlying k-space distribution from incomplete and noise-corrupted measurements. While diffusion models have recently shown strong potential as generative prior for inverse problems,existingapproachesstruggletohandlenoisyreconstruction settings, especially when operating directly in k-space domain. In this work, we propose a unified high-dimensional k-space recons...

---

### 6. Structured 4D Latent Predictive Model for Robot Planning

**Authors:** Zhiyi Li, Peilin Wu, Xiaoshen Han, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01166v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01166v1)

**Summary:** Video predictive models are emerging as a powerful paradigm in robotics, offering a promising path toward task generalization, long-horizon planning, and flexible decision-making. However, prevailing approaches often operate on 2D video sequences, inherently lacking the 3D geometric understanding necessary for precise spatial reasoning and physical consistency. We introduce a Structured 4D Latent Predictive Model, which predicts the evolution of a scene's 3D structure in a structured latent spac...

---

### 7. EquiSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation

**Authors:** Tatiana Gaintseva, Akshit Achara, Gregory Slabaugh, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01147v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01147v1)

**Summary:** Text-to-image diffusion models power everyday creative tasks, but they still reproduce the demographic biases in their training data. On common prompts such as ``a photo of a nurse,'' ``a photo of a CEO'', they skew their outputs toward one gender, driven by the statistics of training data rather than anything in the text. Existing debiasing methods show promise in narrow settings but require retraining, batch-level control, or prompt-specific tuning, limiting their scalability. We propose \emph...

---

### 8. Relation-Centric Open-Vocabulary 3D Gaussian Segmentation

**Authors:** Eunsung Cha, Hyunjoon Lee, Jaesik Park

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01140v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01140v1)

**Summary:** Open-vocabulary 3D Gaussian segmentation is challenging because it requires language understanding for diverse queries and accurate separation of Gaussians along object boundaries. Prior approaches either embed language knowledge into individual Gaussians to improve query responsiveness or optimize per-Gaussian instance features to encode object identity. However, these strategies may produce noisy Gaussian segmentations or rely on cost-inefficient per-scene optimization. We propose PairGS, a fr...

---

### 9. SD-RouteFusion: Ego-Trajectory Prediction with SD-Map Route Conditioning

**Authors:** Sviatoslav Voloshyn, Bruno K. W. Martens, Wangxin Liu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01139v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01139v1)

**Summary:** This paper presents SD-RouteFusion, a deployable end-to-end ego-trajectory prediction method that fuses a front-facing camera, vehicle kinematics, and a navigation route derived from a Standard Definition (SD) map. Unlike approaches that rely on High Definition (HD) map geometry, SD-RouteFusion aligns the learning objective with scalable and production-ready SD-map route inputs, enabling route-aware prediction without requiring HD-map infrastructure. First, we demonstrate that SD-map route prior...

---

### 10. Towards Metric-Agnostic Trajectory Forecasting

**Authors:** Markus Knoche, Daan de Geus, Bastian Leibe

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01133v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01133v1)

**Summary:** Accurate trajectory forecasting of surrounding traffic participants is a core capability for autonomous driving, enabling vehicles to anticipate behavior and plan safe maneuvers. We observe that current state-of-the-art forecasting models on Argoverse 2 and the Waymo Open Motion Dataset tailor their training objectives to the different benchmark metrics. Because these metrics encourage conflicting behavior, we propose a paradigm change for trajectory forecasting: training models with metric-agno...

---

### 11. Autonomous Scientific Discovery via Iterative Meta-Reflection

**Authors:** Bingchen Zhao, Sara Beery, Oisin Mac Aodha

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01131v1)

**Summary:** Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry. Furthermore, while they generate hypotheses iteratively, they largely lack the ability to explicitly synthesize their own accumulated findings to uncover complex, interconnected phenomena. ...

---

### 12. MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models

**Authors:** Jiale Li, Sihan Chen, Mengyuan Liu

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01117v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01117v1)

**Summary:** Video Large Language Models (VideoLLMs) have shown strong progress in video understanding, yet they still suffer from hallucinations that are inconsistent with visual evidence. Existing benchmarks mainly focus on object hallucination or coarse action perception, leaving a key video-specific problem underexplored: motion hallucination, in which models infer human motions that are absent from the video. We present MoHallBench, a benchmark for diagnosing motion hallucination in VideoLLMs. MoHallBen...

---

### 13. CPDDNet: Color-Polarization Denoising and Demosaicking Network

**Authors:** Qihang Zhang, Yusuke Monno, Masayuki Tanaka, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01100v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01100v1)

**Summary:** Color-polarization imaging using a color-polarization filter array (CPFA) sensor captures both texture (color intensity) and physical (polarization) information of the scene in a single shot, enabling various applications in computer vision. However, the raw mosaic output from a CPFA sensor often suffers from severe noise and resolution loss, especially under low-light conditions. Existing methods generally focus on either denoising or demosaicking tasks, failing to capture the coupling between ...

---

### 14. LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models

**Authors:** Arpita Nema, Hanwei Zhu, Xi Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01086v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01086v1)

**Summary:** The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 dive...

---

### 15. Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation

**Authors:** Chi Zhang, Penglin Cai, Ziheng Xi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01067v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01067v1)

**Summary:** As an essential modality for dexterous and contact-rich tasks, tactile sensing provides precise force feedback that cannot be reliably inferred from vision. However, limited by hardware and data collection systems, existing datasets with tactility remain small in scale and narrow in contact coverage. Meanwhile, Vision-Language-Action (VLA) models with tactile modality are constrained on dynamics-agnostic post-training, which limits the performance ceiling on downstream tasks. In this paper, we p...

---

### 16. GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision

**Authors:** Dianyu Wang, Yidan Zhang, Peirong Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01050v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01050v1)

**Summary:** Recent multimodal large language models (MLLMs) have shown strong cross-modal understanding and coordinate generation abilities in visual grounding. However, transferring these abilities to remote sensing visual grounding (RSVG) remains challenging. High-resolution remote sensing images usually cover large-scale scenes, where targets are often extremely small and surrounded by numerous visually similar distractors. Meanwhile, queries often contain multiple clues, such as reference objects, spati...

---

### 17. GenAU: Language-Grounded Industrial Anomaly Understanding with Vision-Language Models

**Authors:** Hongkuan Zhou, Tristan Rehm, Nadeem Nazer, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01049v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01049v1)

**Summary:** Industrial inspection requires more than binary anomaly detection: a practical system should determine whether an anomaly exists, localize the defective region, identify the defect type, and provide interpretable visual evidence. Existing CLIP-based methods detect and localize anomalies well but offer limited language-level defect understanding, while instruction-tuned vision-language models can describe defects but do not natively produce pixel-level masks. We introduce GenAU, a Generalist visi...

---

### 18. EchoRisk: A Multicentre Echocardiography Dataset and Benchmark for Cardio-Oncology

**Authors:** Grigorios Kalliatakis, Georgia Karanasiou, Georgios Manikis, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01039v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01039v1)

**Summary:** Therapy-induced cardiotoxicity is the leading non-oncological cause of treatment interruption in breast cancer patients, yet early, automated risk stratification from routine cardiac imaging remains an unsolved problem. We present EchoRisk, the first curated, multicentre, longitudinal echocardiography dataset with explicit cardiotoxicity labels, released as the primary technical reference for the EchoRisk-MICCAI 2026 challenge. The dataset comprises 422 patients enrolled in the EU-funded CARDIOC...

---

### 19. Reading Order Inference for Complex Document Layouts

**Authors:** Iddo Hakim, Sharva Gogawale, Omer Ventura, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01018v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01018v1)

**Summary:** Reading order inference remains a critical bottleneck in the digitization of complex historical manuscripts, where pages contain multiple spatially interleaved reading streams, the canonical example being the Glossa Ordinaria layout, in which a central text is surrounded by commentaries that wrap around it in non-rectangular, non-convex regions. We present a training-free, graph-based framework: each OCR text line becomes a node in a directed candidate-transition graph, edges are scored by a wei...

---

### 20. SuperFlex: Deformable Superquadrics for Point Cloud Decomposition

**Authors:** Gabriel Tavernini, Elisabetta Fedele, Tiago Novello, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01015v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01015v1)

**Summary:** Superquadrics have proven to provide a compact, geometrically meaningful representation for 3D objects. However, existing methods suffer from limited reconstruction accuracy, are restricted to rigid primitives, and lack robustness to partial point clouds. In this work, we present SuperFlex, an enhanced framework that expands the expressive power and applicability of superquadric decompositions. First, we introduce a novel loss formulation which significantly improves reconstruction accuracy. Sec...

---

### 21. Foundation Models vs. Radiomics for Lung Computed Tomography: A Benchmark of Feature Extractors, Classification Heads, and Segmentation Choices

**Authors:** Nils Neukirch, Martin Maurer, Nils Strodthoff

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01001v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01001v1)

**Summary:** Radiomics is the established approach for CT-based lung cancer phenotyping, yet comparisons with foundation models rarely isolate contributions of feature extractor, classification head, and segmentation choice, or test cross-cohort robustness. We benchmark five feature extractors (Curia, Curia-2, DINOv3, Radiomics2D, Radiomics3D), seven classification heads (TabPFN, TabICL, XGBoost, CatBoost, Random Forest, logistic regression, Ridge), and three segmentation regimes on five tasks: tumor volume ...

---

### 22. AVSR-Diff: Scale-Agnostic Diffusion Priors for Temporally Consistent Arbitrary-Scale Video Super-Resolution

**Authors:** Geunhyuk Youk, Jeonghyeok Do, Dayeon Kim, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00987v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00987v1)

**Summary:** Diffusion models have significantly advanced video super-resolution (VSR) but remain largely constrained to fixed upsampling scales. Conversely, while coordinate-based arbitrary-scale VSR methods offer scale flexibility, they inherently suffer from severe over-smoothing at large scaling factors. Integrating generative priors with continuous decoding is promising but currently hindered by severe temporal flickering caused by the stochasticity of diffusion sampling. To address this, we propose AVS...

---

### 23. QCA: Query- and Content-Aware Keyframe Selection for Long Video Understanding

**Authors:** Jun Peng, Baiyang Song, Jie Li, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00983v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00983v1)

**Summary:** Video understanding is often plagued by severe temporal redundancy, where processing dense frame sequences is both semantically inefficient and computationally expensive. This challenge is further amplified when only a small subset of frames is truly relevant to the given query. In this paper, we propose a Query- and Content-Aware (QCA) keyframe selection framework that can select a compact yet information-rich set of frames from long videos. QCA first partitions the video into temporal segments...

---

### 24. Privacy-Preserving Depth-Only Open-Vocabulary 3D Semantic Segmentation Via Uncertainty-Guided Test-Time Optimization

**Authors:** Xuying Huang, Sicong Pan, Maren Bennewitz

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00978v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00978v1)

**Summary:** Privacy-preserving perception is a critical requirement for deploying 3D scene understanding systems in real-world indoor environments, yet it remains underexplored in open-vocabulary 3D semantic segmentation. Existing methods typically rely on obtaining rich semantic cues from RGB images, which may expose privacy-sensitive visual information. Depth-only 3D geometry provides a privacy-preserving alternative, but the absence of appearance-based semantic cues makes open-vocabulary predictions high...

---

### 25. TRCGL-Net: A Long-Tailed Multi-Label Chest X-Ray Classification Framework with Generative Data Augmentation and Label Co-Occurrence Modeling

**Authors:** Tong Shao, Hongshun Ling, Li Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00975v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00975v1)

**Summary:** Chest X-ray multi-label classification is a core task in intelligent medical imaging diagnosis. However, real clinical data often exhibit extreme long-tailed distributions, leading to degraded performance on rare diseases in tail classes. This issue is not only driven by data scarcity but also by two intrinsic factors:1) attenuation of tail-class lesion representations under complex anatomical backgrounds, and 2) dominance of head classes in modeling label co-occurrence relationships. To address...

---

### 26. QuaMoE-DRF: Proactive Beam and Rate Adaptation via Multimodal Dynamic Radio Map Forecasting in ISAC Networks

**Authors:** Zhihan Zeng, Kaihe Wang, Zhongpei Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00974v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00974v1)

**Summary:** Static radio maps provide location-dependent propagation priors, but they cannot capture short-term blockage caused by moving objects. Direct sensing-assisted beam prediction is also limited because a beam index discards SINR margins, MCS thresholds, BS alternatives, and communication-equivalent neighboring beams. This paper proposes QuaMoE-DRF, a quality-aware multimodal dynamic radio map forecasting framework for proactive beam and rate adaptation in ISAC networks. Its core representation is a...

---

### 27. Slope-Guided Mamba and Angular-Refined Transformer for Light Field Super-Resolution

**Authors:** Li Jin, Jian Huang, Junde Lu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00965v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00965v1)

**Summary:** Light Field Super-Resolution (LFSR) necessitates accurate modeling of spatial-angular correlations while preserving intrinsic 4D ray coherence. However, maintaining such high-dimensional consistency remains challenging, primarily due to two inherent limitations in prevailing modeling paradigms. First, spatial and angular dimensions are often modeled in a decoupled manner, restricting early cross-dimensional interaction and leading to geometric inconsistencies. Moreover, although continuous seque...

---

### 28. GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting

**Authors:** Haijie Yang, Zhenyu Zhang, Yixuan Dong, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00959v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00959v1)

**Summary:** Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation a...

---

### 29. Learning Cardiac Motion Priors for Implicit Neural Representations

**Authors:** Andrew Bell, George Webber, Andrew P King, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00955v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00955v1)

**Summary:** Implicit neural representations (INRs) are well suited to cardiac motion estimation, providing continuous, compact representations of motion fields. However, fitting an INR to each image sequence is time-consuming and sensitive to the optimisation trajectory. Learned priors can help guide optimisation towards plausible motion fields and enable faster adaptation, but learning priors for cardiac motion INRs remains under-explored. In this work, we compare four strategies for learning cardiac motio...

---

### 30. Dataset Biases and Shortcut Learning in Motion-Based AI-Generated Video Detection

**Authors:** Joren Michels, Lode Jorissen, Nick Michiels

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00948v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00948v1)

**Summary:** The visual quality of AI-generated videos has improved drastically in recent years, making it increasingly difficult for humans to distinguish between real and synthetic media. In this work, we evaluate the robustness and applicability of four state-of-the-art motion-based AI-generated video detectors. We identify significant preprocessing and sampling biases in these methods and demonstrate that they account for a substantial portion of their reported performance. Furthermore, we find that thes...

---

### 31. Post-Training Pruning for Diffusion Transformers

**Authors:** Chengzhi Hu, Xuewen Liu, Jing Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00927v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00927v1)

**Summary:** Diffusion Transformers (DiTs) have demonstrated impressive performance in image generation but suffer from substantial computational overhead and resource consumption. Post-training pruning offers a promising solution; however, due to DiTs' unique architectural design and parameter distribution, traditional pruning methods are inapplicable, leading to significant performance degradation. Specifically, prior methods developed for LLMs, which derive metrics through a series of approximations, ampl...

---

### 32. GMO-E$^2$DIT: Grounded Multi-Operation Editing for E-Commerce Images

**Authors:** Zipeng Guo, Xiaoan Liu, Lichen Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00920v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00920v1)

**Summary:** Real-world e-commerce image editing often requires multiple, localized, and auditable operations rather than global restyling. This compositional nature poses a dual challenge: models must precisely apply all requested edits to the correct regions while preserving unmodified content, even under ambiguous instructions. Existing one-shot editors conflate intent resolution, spatial grounding, and synthesis into a single step, frequently resulting in partial execution failures, which is unacceptable...

---

### 33. Condensing Large-Scale Datasets Directly with Minimal Information Loss

**Authors:** Xinyi Shang, Peng Sun, Bei Shi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00916v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00916v1)

**Summary:** Recent advancements in scaling dataset distillation rely heavily on decoupled information extraction pipelines, comprising SQUEEZE, RECOVER, and RELABEL stages. Despite their scalability to large-scale datasets, these methods suffer from prohibitive computational overhead and poor cross-architecture generalization. In this paper, we reveal the root cause of these bottlenecks: the implicit dual-compression process, from data to model and back to images, inherently induces severe information loss....

---

### 34. MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization

**Authors:** Jingchen Ni, Cangjin Yu, Dan Jiang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00902v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00902v1)

**Summary:** Driven by Artificial Intelligence-Generated Content (AIGC), the authenticity of audio-visual content is facing severe challenges. Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within untrimmed sequences. However, existing methods are limited by CNNs' local receptive fields or Transformers' quadratic complexity, while emerging linear models often struggle to balance global authentic context compression with local abrupt forgery perception. To address this, we...

---

### 35. DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors

**Authors:** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00889v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00889v1)

**Summary:** We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single p...

---

### 36. Geometry-Aware Cross-Height Channel Knowledge Map Prediction for UAV-Assisted Communications With Uncertainty-Guided 3D Sensing

**Authors:** Zhihan Zeng, Amir Hussain, Yue Xiu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00887v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00887v1)

**Summary:** Low-altitude Unmanned Aerial Vehicles (UAVs) often need to infer channel knowledge across a range of heights from only sparse observations collected at a few altitude layers. To address this challenge, this paper studies height-conditioned cross-height channel knowledge map (CKM) prediction for UAV-assisted communications in geometry-rich urban environments. We develop a geometry-aware conditional prediction framework that combines urban scene priors, sparse multi-altitude observations, and targ...

---

### 37. Beyond Pixel Overlap: A Framework for Decomposing Segmentation Evaluation Metrics

**Authors:** Youwei Pang, Xiaoqi Zhao

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00886v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00886v1)

**Summary:** Evaluation metrics are central to binary target segmentation because they determine how progress is measured, compared, and interpreted. In this paper, target denotes the task-defined positive region to be segmented rather than a generic foreground object. It may be salient, camouflaged, transparent, glass-like, mirror-like, shadow-like, lesion-like, or defined by other application-specific semantics. We treat existing metrics as compositions of modular design choices rather than isolated formul...

---

### 38. Improving Sparse-View 3DGS Generalization via Flat Minima Optimization

**Authors:** Kangmin Seo, Sangeek Hyun, MinKyu Lee, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00885v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00885v1)

**Summary:** Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small par...

---

### 39. OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping

**Authors:** Xudong Li, Mengdan Zhang, Peixian Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00881v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00881v1)

**Summary:** Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex quer...

---

### 40. EFlow: Learning Evidence Flow for Long-Video Reasoning with Adaptive Reflection

**Authors:** Wenhao Zhang, Kuanwei Lin, Xuyi Yang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00867v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00867v1)

**Summary:** Long-video reasoning is fundamentally constrained by how models acquire and utilize visual evidence. Existing tool-augmented video frameworks often interleave temporal grounding and answer reasoning within a single trajectory, causing early semantic hypotheses to bias evidence localization. We term this failure mode premature semantic commitment, where biased grounding retrieves incomplete evidence and incomplete evidence further reinforces incorrect reasoning. To address this issue, we propose ...

---

### 41. TrajLoc: Trajectory-Attention Localization for Multi-Object Motion Control

**Authors:** Omer Sela, Inbar Huberman-Spiegelglas, Michael Rotman, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00861v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00861v1)

**Summary:** Controlling the motion of multiple objects in image-to-video (I2V) generation requires preserving object identities while enforcing adherence to distinct target trajectories. This becomes particularly challenging as the number of objects increases and their paths intersect or occlude one another. Existing approaches entangle multiple trajectories within a shared, dense conditioning signal, making object-level correspondence difficult to preserve in crowded scenes. We depart from this paradigm an...

---

### 42. MoVA: Learning Asymmetric Dual Projections for Modular Long Video-Text Alignment

**Authors:** Peiyuan Zhu, Shaoan Xie, Zijian Li, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00858v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00858v1)

**Summary:** Contrastive pre-training has propelled video-text alignment, yet models often inherit the critical limitations of their image-text predecessors like CLIP, resulting in entangled representations. These challenges are severely exacerbated by two fundamental properties in the video domain: Temporal Misalignment, where textual descriptions often correlate only to specific, constrained temporal windows, leaving other frames text-irrelevant; and Semantic Asymmetry, which dictates a sparse, bidirection...

---

### 43. Mirror-Fusion Attention for Reflection-Aware Self-Supervised Representation Learning

**Authors:** Ruixin Li, Jin Liu, Yuling Shi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00850v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00850v1)

**Summary:** Most self-supervised learning (SSL) methods encourage invariance across augmentations, but strict flip invariance can suppress informative left--right correspondences in approximately bilateral data such as medical images and human faces. We propose Mirror-Fusion-Augmented Self-Supervised Learning (MFASSL), a Vision Transformer framework that injects a soft reflection prior into standard SSL without redesigning the backbone. MFASSL constructs mirror-paired views aligned to an estimated symmetry ...

---

### 44. Rethinking Multi-Label Image Classification With Deep Learning: Taxonomy, Challenge, and Outlook

**Authors:** Xuelin Zhu, Xiu-Shen Wei, Jiawei Ge, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00839v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00839v1)

**Summary:** Multi-label image classification (MLIC), a fundamental task in computer vision, focuses on identifying multiple objects or concepts within an image, underpinning numerous read-world applications, such as autonomous driving, disease diagnosis, recommendation system, and mobile service robot. Over the past decade, deep learning paradigms based on convolutional neural networks, recurrent neural networks, and Transformers have significantly advanced this field, owing to their powerful capability in ...

---

### 45. Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences

**Authors:** Zhenjia Li, Jinrang Jia, Yifeng Shi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00832v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00832v1)

**Summary:** A single panorama captures the full visual sphere from one camera center, yet confines users to looking around in place without enabling true scene exploration. Converting a single panorama into a persistent, renderable 3D representation for free-viewpoint navigation has attracted growing interest; existing methods either adopt iterative per-view completion that propagates inpainting results to update the underlying geometry, leading to progressive error accumulation and cumbersome multi-step pi...

---

### 46. Stitched Embeddings: A Unified Latent Space for 3D Garments and 2D Patterns

**Authors:** Andrea Sanchietti, Riccardo Marin, Bharat Lal Bhatnagar, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00829v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00829v1)

**Summary:** While garments are essential for realistic digital humans, their topological variety makes them much harder to model than parametric bodies. Traditional tailoring relies on 2D sewing patterns, yet bridging these patterns to 3D geometry currently requires physical simulations. We present Stitched Embeddings, the first simulation-free framework to unify 3D garment reconstruction and sewing pattern inference within a single bidirectional latent space. By leveraging the geometric priors of a pretrai...

---

### 47. Training-Free Debiasing of Diffusion Models via CLIP-Guided Denoising Optimization

**Authors:** Dain Kim, Jinseo Kim, Sungyong Baik

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00817v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00817v1)

**Summary:** Text-to-image diffusion models achieve impressive visual quality, yet demographic bias remains a challenge, as neutral prompts consistently produce stereotypical representations across gender and race. Existing approaches remain limited by costly retraining or by inference-time interventions that often degrade image quality and semantic alignment. We propose Text Embedding Steering (TES), a training-free framework that mitigates demographic bias by directly optimizing conditional text embeddings...

---

### 48. Towards High-Resolution Visual Perception via Hierarchical Entity Exploration

**Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00816v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00816v1)

**Summary:** High-resolution (HR) image perception remains a key challenge in multimodal large language models (MLLMs), as fine-grained details are often lost when the image is processed as a whole. Existing methods either require training to teach models where to look or heuristically divide the image into fixed regions, both of which struggle to generalize in complex HR scenes. In this work, we propose Hierarchical Entity Exploration (HEE), a training-free and model-agnostic framework that transforms stati...

---

### 49. Spotted: Location-informed Reidentification of Hyenas and Leopards in Camera Trap Surveys

**Authors:** Halil Sina Kelebek, Julia Hindel, Kobus Hoffman, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00804v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00804v1)

**Summary:** Animal re-identification (ReID) in camera-trap surveys remains challenging due to low image quality, strong variation in illumination and viewpoint, and highly imbalanced numbers of observations per individual. As a result, current ReID performance is often insufficient for fully automated use, and practical workflows typically depend on expert review of algorithmically proposed candidate matches. Moreover, most existing approaches focus almost exclusively on visual cues and overlook auxiliary i...

---

### 50. ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction

**Authors:** Yaofei Duan, Yuhao Huang, Tianyu Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00798v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00798v1)

**Summary:** Neoadjuvant chemotherapy (NAC) response prediction is clinically important for treatment stratification in breast cancer. However, robust pre-treatment pathological complete response (pCR) prediction remains challenging due to insufficient cross-modal modeling, multicenter imaging heterogeneity, and weak evidence-grounded interpretability. We propose ClinRAG-GRAPH, a Clinically informed Retrieval-Augmented Generation Graph framework, for pre-treatment pCR prediction from DCE-MRI, structured clin...

---

## cs.LG

**50 papers**

### 1. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

**Authors:** Zijian Zhang, Rizhen Hu, Athanasios Glentis, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01232v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01232v1)

**Summary:** Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that trai...

---

### 2. Language-Critique Imitation Learning from Suboptimal Demonstrations

**Authors:** Chih-Han Yang, Dai-Jie Wu, Yun-Ping Huang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01225v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01225v1)

**Summary:** Prior work on imitation learning from suboptimal demonstrations typically relies on compressed supervision signals such as confidence estimates, discriminator scores, or importance weights. These scalar signals are inherently limited, as they cannot explicitly express intermediate reasoning about task progress, failure modes, or corrective actions. We propose a language-critique framework for imitation learning from suboptimal demonstrations that instead leverages natural language as a structure...

---

### 3. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States

**Authors:** Ben Slivinski, Michael Saldivar

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01223v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01223v1)

**Summary:** When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a...

---

### 4. The State-Prediction Separation Hypothesis

**Authors:** Giovanni Monea, Nathan Godey, Kianté Brantley, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01218v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01218v1)

**Summary:** Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining experiments across various scales. Our experiments show that state-prediction separation consistently off...

---

### 5. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation

**Authors:** Shayan Talaei, Abhinav Chinta, Devvrit Khatri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01208v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01208v1)

**Summary:** Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, ...

---

### 6. TiRex-2: Generalizing TiRex to Multivariate Data and Streaming

**Authors:** Patrick Podest, Marco Pichler, Elias Bürger, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01204v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01204v1)

**Summary:** We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecasting is inherently sequential: observations arrive continuously, variables evolve jointly, and a subset of covariates is known ahead of time. Existing Transformer-based time series foundation models capture cross-variate dependencies but incur quadratic complexity in context length and require full-his...

---

### 7. GPU-Parallel Linearization Error Bounds for Real-Time Robust Optimal Control of Nonlinear and Neural Network Dynamics

**Authors:** Jeffrey Fang, Keyi Shen, Anutam Srinivasan, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01203v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01203v1)

**Summary:** This paper studies real-time robust optimal control for uncertain nonlinear systems, where linear time-varying (LTV) approximations make planning tractable but require sound linearization error bounds (LEBs) to guarantee robust constraint satisfaction. We develop tight, differentiable, GPU-parallel LEBs for LTV approximations of nonlinear and neural network (NN) dynamics. For analytic dynamics, we introduce path-based Hessian bounds that are tighter than standard interval methods. For NN dynamic...

---

### 8. Quantum vs. Classical Machine Learning: A Unified Empirical Comparison

**Authors:** Chuanming Yu, Jiaming Liu, Zihao Ge, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01197v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01197v1)

**Summary:** Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the evidence supporting the performance and advantages of quantum machine learning (QML) models relative to classical models is insufficient.To address this gap, this paper presents an empirical study on the performance of QML models and their classical counterparts. We compare seven model pairs spanning supe...

---

### 9. Neural Certificate Pricing for Combinatorial Optimization Problems

**Authors:** Jingyi Chen, Xinyuan Zhang, Xinwu Qian

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01185v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01185v1)

**Summary:** Combinatorial optimization (CO) problems are difficult because certifiable discrete structure induces exponential search. One needs to search over the set exponentially many candidates to certify optimality, however, the structural feasibility of a path, packing, or cover can be verified in polynomial time once supplied. In this study, we introduce Neural Certificate Pricing (NCP) that exploits this asymmetry under an unsupervised learning framework. A neural network is trained to predict certif...

---

### 10. Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations

**Authors:** Mehul Damani, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01181v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01181v1)

**Summary:** RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current RLVR methods optimize only what can be objectively scored, often neglecting subjective, non-verifiable aspects of human-like outputs, such as style and structure. This limitation leads to well-documented failure modes such as diversity collapse, unnatural-sounding responses, and reward hacking. We pr...

---

### 11. QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling

**Authors:** Michael Y. Li, Anthony Zhan, Kanishk Gandhi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01179v1)

**Summary:** Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independently, wasting inference compute on redundant solutions. This waste seems unavoidable. After all, independence is what makes parallel sampling trivial to scale. However, this tradeoff is not fundamental: there is a rich design space of samplers that generate correlated but exact samples entirely in p...

---

### 12. Decision-Aware Training for Sample-Based Generative Models

**Authors:** Kornelius Raeth, Nicole Ludwig

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01171v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01171v1)

**Summary:** Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. These models are commonly trained with strictly proper scoring rules, such as the energy score, which allocate their training signal in proportion to data density, with no awareness of where forecast errors are most costly for downstream decisions. We therefore propose decision-aware training for sampl...

---

### 13. Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation

**Authors:** Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01164v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01164v1)

**Summary:** Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require partial mesh storage for later sampling, limiting achievable compression. At the same time, novel view synthesis methods have shown that explicit collections of 3D Gaussians can be used to accurately...

---

### 14. A Lightweight Self-Supervised Learning Framework for Multivariate Time Series using Hierarchical-JEPA on ECG Data

**Authors:** Siwon Kim

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01145v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01145v1)

**Summary:** Data analysis in the medical domain often encounters scenarios involving a limited target dataset and a large, unannotated dataset with a general distribution. Under such circumstances, self-supervised learning (SSL) methods are highly effective for utilizing large datasets, making them a popular choice for electrocardiogram (ECG) analysis. This work presents the Event Reconstruction Joint-Embedding Predictive Architecture (ER-JEPA), a lightweight SSL framework for multivariate time series, whos...

---

### 15. Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search

**Authors:** Binglin Ji, Anindya Sarkar, Hengchang Lu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01144v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01144v1)

**Summary:** While generative models have enabled training-free reward alignment, current methods typically excel in local exploration within narrow regions of the underlying distribution. These approaches struggle when preferences are unknown a priori and only revealed through sequential feedback-a scenario demanding broad exploration to uncover high-utility regions. To address this, we propose Sequentially-Controlled Interactive Multi-Particle Flow-Maps (IMPFM), a framework for sample-efficient online feed...

---

### 16. GAIA: Geometry-Adaptive Operator Learning for Forward and Inverse Problems

**Authors:** Meenakshi Krishnan, Pranav Pulijala, Ke Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01128v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01128v1)

**Summary:** Operator learning for partial differential equations (PDEs) on arbitrary geometries builds fast neural surrogates for large-scale simulation. Although recent geometry-adaptive neural operators have made substantial progress, they are mainly designed for forward problems in which inputs and outputs share the same spatial domain. This limits their applicability for boundary value problems (BVPs) and inverse problems, where inputs and outputs may live on different domains. We introduce the Geometry...

---

### 17. ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces

**Authors:** Xun Dong, Yibo Xu, Naigang Wang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01125v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01125v1)

**Summary:** Zeroth-order (ZO) optimization enables fine-tuning large language models when backpropagation is unavailable or memory-prohibitive, but existing methods often perturb full model weights or randomly constructed low-dimensional subspaces, yielding high-variance estimates and limited performance. We propose ZO-Act, an activation-informed ZO fine-tuning method that restricts perturbations to a fixed low-rank subspace derived from input activations. For each linear layer, ZO-Act computes a small acti...

---

### 18. Muon as a Residual Connection

**Authors:** Hao Huang

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01124v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01124v1)

**Summary:** Muon has recently emerged as one of the most effective optimizers for training large neural networks, yet its empirical success has been explained from several different perspectives. In this paper, we propose a simple mechanistic interpretation: Muon can be understood as an implicit residual connection during training. Specifically, orthogonalizing the update can sacrifice some immediate gradient fidelity while improving representation preservation for downstream layers. We study this trade-off...

---

### 19. FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement

**Authors:** Haoran Hao, Shahram Najam Syed, Jeffrey Ichnowski, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01111v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01111v1)

**Summary:** Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning dat...

---

### 20. SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles

**Authors:** Miruna Cretu, John Bradshaw, Patricia Suriana, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01105v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01105v1)

**Summary:** We present SynLaD, a latent diffusion framework for small-molecule generation that unifies ligand-based drug design objectives (what to make) with synthetic accessibility (how to make it). Current models typically optimize one objective at the expense of the other, creating a bottleneck for discovering high-scoring and synthesizable molecules. SynLaD combines reaction-constrained generation with pharmacophore-conditioned 3D design by learning a latent space that decodes to both 3D structures and...

---

### 21. CausalMix: Data Mixture as Causal Inference for Language Model Training

**Authors:** Zinan Tang, Yukun Zhang, Shaomian Zheng, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01104v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01104v1)

**Summary:** In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address thi...

---

### 22. Group-invariant Coresets for Data-efficient Active Learning

**Authors:** L. C. Ayres, J. C. M. Bermudez, S. J. M. de Almeida, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01089v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01089v1)

**Summary:** Active learning reduces labeling cost by querying the most informative unlabeled samples, but standard coreset methods ignore known data symmetries and can waste budget on transformed versions of the same instance. We propose GRINCO, a group-invariant coreset framework that performs acquisition in the quotient space induced by a transformation group, so that selection operates on orbits rather than raw samples. The method uses either canonical representatives or learned orbit-separating invarian...

---

### 23. Staleness-Learning Rate Scaling Laws for Asynchronous RLHF

**Authors:** Jingwei Song, Haofeng Xu, Jie Xiao, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01083v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01083v1)

**Summary:** High-throughput RLHF systems often decouple rollout generation from policy optimization, leading to the use of stale rollouts during learner updates. In this work, we study the effect of such staleness in asynchronous GRPO. We make the behavior policy explicit in the GRPO surrogate objective and distinguish between the surrogate-gradient mapping used by the learner and the true total derivative of a distribution-dependent population objective. Under assumptions of local boundedness, distribution...

---

### 24. When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting

**Authors:** Yahya Aalaila, Mouad Elhamdi, Gerrit Großmann, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01082v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01082v1)

**Summary:** Spatio-temporal point-process models must often generalise across space when local event histories are sparse. We study whether exogenous spatial context can compensate in such regimes. Using a fixed log-Gaussian Cox process backbone, we compare an event-only model with the same model augmented by AlphaEarth embeddings as linear spatial context. We evaluate spatial transfer on emergency medical services (EMS) forecasting across eight held-out regions, fixed forecast anchors, and a sweep over his...

---

### 25. Balancing Expressivity and Learnability in Quantum Kernel Bandit Optimization

**Authors:** Yuqi Huang, Vincent Y. F. Tan, Sharu Theresa Jose

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01080v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01080v1)

**Summary:** We investigate Gaussian process (GP) bandit optimization with quantum kernels, assuming the mean reward function lies in the reproducing kernel Hilbert space (RKHS) induced by the quantum kernel. This setting is motivated by NISQ-era tasks such as quantum control, state preparation and variational quantum algorithms. While quantum kernels can offer a `quantum advantage' via domain-specific inductive biases, naïvely using full, high-dimensional kernels increases model complexity and information g...

---

### 26. Message Passing Enables Efficient Reasoning

**Authors:** Xuecheng Liu, Daman Arora, Gokul Swamy, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01077v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01077v1)

**Summary:** While inference-time scaling has improved the reasoning abilities of large language models (LLMs), the need to generate long chains-of-thought (CoTs) is a computational bottleneck. Thus, in contrast to sequential scaling methods like CoT, recent parallel scaling techniques instead use fork and join (FJ) primitives to divide work across multiple LLM threads. However, in the fork-join paradigm, threads are typically transient and do not communicate pointwise with one another which limits scalabili...

---

### 27. GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache

**Authors:** Soosung Kim, Minjae Park, Eui-Young Chung, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01065v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01065v1)

**Summary:** The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit regime by progressively encoding residuals with small codebooks. However, most VQ methods still rely on standard $\ell_2$ $K$-means as the core codebook-learning primitive. We identify a subtle high-di...

---

### 28. Characterizing and Identifying Separable Graphical Models

**Authors:** Christopher Meek, Kayvan Sadeghi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01057v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01057v1)

**Summary:** We study a broad class of graphical models whose independencies correspond to vertex separation in mixed graphs with directed, undirected, and bidirected edges, that are capable of encoding independence structures arising from feedback, latent and selection mechanisms. In particular, we introduce separable graphs, in which each missing edge implies the existence of a separating set for its endpoints, and essentially separable graphs, those graphs separation equivalent to a separable graph. We sh...

---

### 29. The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology

**Authors:** Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01033v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01033v1)

**Summary:** Model organisms (MOs) - language models trained to exhibit undesired or unnatural behaviours - are frequently used as testbeds for evaluating white-box interpretability techniques. Current MOs are typically constructed via post-hoc supervised fine-tuning (SFT) on behavioural transcripts or synthetic documents. Prior research has shown that interpretability methods can easily identify hidden behaviours in these MOs. However, recent work suggests that such post-hoc training methods may make interp...

---

### 30. How Much Do RF Drone Benchmarks Overstate? A Controlled Study and Theory of Data Leakage in UAV Signal Identification

**Authors:** David Shulman

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01025v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01025v1)

**Summary:** Radio-frequency (RF) sensing is a central modality for counter-unmanned-aerial-system (counter-UAS) defence because it exploits the control, telemetry, and video links between a drone and its operator. Reported accuracies for RF-based drone detection and identification are often very high, but many are obtained using cross-validation that splits a small number of continuous recordings into short segments. This can place near-duplicate slices of the same recording in both training and test partit...

---

### 31. Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling

**Authors:** Yahya Aalaila, Gerrit Großmann, Sebastian Vollmer

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01022v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01022v1)

**Summary:** Spatiotemporal point processes (STPPs) model event data in continuous time and space, with applications in mobility, epidemiology, and public safety. Recent neural STPPs span expressive intensity models, conditional density models, continuous-time latent dynamics, normalizing-flow spatial decoders, and score-based generative mechanisms. Yet comparison remains fragile because implementations differ in preprocessing, coordinate normalization, splits, likelihood conventions, and evaluation protocol...

---

### 32. Generative Model Proposal based Particle Filtering for Data Assimilation

**Authors:** Chandni Nagda, Mayank Shrivastavam Gudrun Thorkelsdottir, Gan Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01012v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01012v1)

**Summary:** Data assimilation models state dynamics conditioned on sequential observations, and has wide-ranging scientific applications. In the filtering setting, the goal is to model the posterior over the current state given all observations so far. Classical solutions typically make simplifying distributional or functional assumptions, e.g., linear-Gaussian systems, which can be inaccurate in many scenarios. In principle, particle filters (PFs) remove these assumptions, yet often collapse in high dimens...

---

### 33. Function-Counting Theory for Low-Dimensional Data Structures

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01010v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01010v1)

**Summary:** The success of deep learning models in classification and regression is widely attributed to the low-dimensional structure that real-world data tend to exhibit, despite their high-dimensional representation. This work attempts to provide a mathematical framework for binary classification on low-dimensional data, building on Cover's (1965) function-counting theory. With our framework, we aim to address the question of how the low-dimensional structure of the data affects the classification capabi...

---

### 34. Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads

**Authors:** Aryo Pradipta Gema, Beatrice Alex, Pasquale Minervini

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01002v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01002v1)

**Summary:** In long-context use, large language models frequently synthesize answers from the meaning of a relevant context span rather than literally copy-pasting them. Identifying which attention heads perform this synthesis matters for interpreting long-context model behavior. Yet existing detectors miss these heads by construction: they reward heads whose attended token matches the generated token, a literal-copy criterion that captures where a head reads but not what it writes through its output-value ...

---

### 35. Foundation Models vs. Radiomics for Lung Computed Tomography: A Benchmark of Feature Extractors, Classification Heads, and Segmentation Choices

**Authors:** Nils Neukirch, Martin Maurer, Nils Strodthoff

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01001v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01001v1)

**Summary:** Radiomics is the established approach for CT-based lung cancer phenotyping, yet comparisons with foundation models rarely isolate contributions of feature extractor, classification head, and segmentation choice, or test cross-cohort robustness. We benchmark five feature extractors (Curia, Curia-2, DINOv3, Radiomics2D, Radiomics3D), seven classification heads (TabPFN, TabICL, XGBoost, CatBoost, Random Forest, logistic regression, Ridge), and three segmentation regimes on five tasks: tumor volume ...

---

### 36. Deep Multitask Learning for Mixed-Type Outcomes with Shared Sparsity

**Authors:** Huichao Li, Tong Wang, Sanguo Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00995v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00995v1)

**Summary:** Most existing multitask learning approaches are limited by their reliance on task-specific loss functions tailored to the scale and type of each outcome. When outcomes differ across tasks, these losses are generally not directly comparable, which makes it difficult to formulate a unified objective and may limit information sharing across tasks. We propose a multitask transformation framework in which task-specific responses may differ through unknown monotone transformations. Motivated by high-d...

---

### 37. Automatic Detection of Stress from Speech in the Trier Social Stress Test

**Authors:** Hanna Drimalla, Wieland R. Cremer, Christine Kraus, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00986v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00986v1)

**Summary:** Automatically detecting stress in speech provides an unobtrusive way to gain insights relevant to behavioral research or clinical assessment. This study investigates the automatic differentiation between a stressful and non-stressful situation, and the prediction of physiological and affective stress responses. Speech data was collected from 50 participants who either completed the Trier Social Stress Test (TSST) or a non-stressful control condition. With a processing pipeline that included spea...

---

### 38. Understanding How Humans Inject Knowledge into Machine Learning Workflows through Visual Analytics

**Authors:** Yiwen Xing, Philip Beaucamp, Joyraj Chakraborty, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00969v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00969v1)

**Summary:** Visual analytics (VA) plays an increasingly important role in supporting machine learning (ML) workflows. In the field of visualization, such approaches and techniques are referred to as VIS4ML. While ML models are mostly learned automatically, the corresponding ML workflows receive a variety of human inputs, such as data labelling, feature engineering, model architecture designing, hyper-parameter tuning, and so on. In this work, we surveyed over 200 VIS4ML papers to gain an understanding of ho...

---

### 39. Bridging Quantum Computing Paradigms toward Semiconductor Yield: A Controlled CV-versus-DV Comparison on Wafer-Map Defect Classification

**Authors:** Yeonhong Kim, Jonghyeok Im, Monu Nath Baitha, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00961v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00961v1)

**Summary:** Realizing quantum neural networks (QNNs) in industry requires knowing which quantum computing paradigm suits which task. Motivated by AI accelerators and high-bandwidth memory, where die stacking makes wafer-level defect screening central to yield, we study WM-811K wafer-map defect classification (eight classes), comparing the dominant paradigms, continuous-variable (CV) and discrete-variable (DV), under controlled conditions. To isolate the quantum circuit as the sole variable, a shared convolu...

---

### 40. LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning

**Authors:** Alexander Chemeris, Ming Jin, Randall Balestriero

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00958v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00958v1)

**Summary:** Time series are central to modern data mining applications, from industrial telemetry and server metrics to finance and physiology, yet time-series self-supervised learning often depends on view and augmentation choices that encode domain-specific invariances. We study how an SSL recipe behaves when its method-specific configuration is reused unchanged after the pretraining signal family changes, framing this as a fixed-recipe stress test rather than a comparison against optimally tuned methods....

---

### 41. Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations

**Authors:** Alexander Chemeris, Ming Jin, Randall Balestriero

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00956v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00956v1)

**Summary:** Time-series models are often evaluated by what they can forecast or classify, but those scores do not show whether their representations preserve the process state a user may want to inspect: event timing, phase, amplitude, frequency, or regime variables. We introduce Aionoscope, a generator-based diagnostic tool for debugging latent-state accessibility in frozen time-series representations. Aionoscope separates process generation from observation rendering, producing seeded synthetic streams wi...

---

### 42. Diffeomorphic Optimization

**Authors:** Ludwig Winkler, Andrew Leaver-Fay, Joseph Kleinhenz, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00947v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00947v1)

**Summary:** Generative models learn data distributions that reside on a low-dimensional manifold within a higher-dimensional ambient space. Optimizing differentiable objectives on this manifold is challenging: the ambient loss landscape is high-dimensional, rugged, and non-convex. Direct gradient descent, blind to the manifold's geometry, quickly drifts off it. Diffeomorphic optimization starts from the observation that diffusion and flow models provide a map from the data manifold to a much simpler base sp...

---

### 43. A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models

**Authors:** Siyi Wang, James Bailey, Ting Dang

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00946v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00946v1)

**Summary:** While prior work has explored emotion control in hybrid text-to-speech systems, the geometric properties of these modules, and their implications for steerability, remain poorly understood. We present the first comparative study of speech language model (SLM) and conditional flow-matching (CFM) modules as activation steering sites for mixed emotion speech synthesis. We first characterize emotion representations using linear probing and local intrinsic dimensionality (LID), and then evaluate sing...

---

### 44. Explainable AI for Cancer Drug Response Prediction: Beyond Univariate Feature Attributions

**Authors:** Martino Ciaperoni, Margherita Lalli, Simone Piaggesi, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00931v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00931v1)

**Summary:** Predicting cancer drug response from transcriptomic profiles is a cornerstone of precision oncology, yet the scientific value of machine learning models hinges not solely on predictive accuracy, but also on their capacity to generate reliable biological insights. Current explainability approaches in this setting are computationally costly, lack robustness, and reduce complex drug response to univariate gene importance scores, overlooking the coordinated gene activity that drives sensitivity and ...

---

### 45. Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm

**Authors:** Midhun Parakkal Unni, Samuel Kaski

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00926v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00926v1)

**Summary:** Generalizing machine learning models to environments that differ from their training distribution remains a critical hurdle, particularly when data from the target domain is entirely or partially unavailable. We propose Generative Meta-Learning with Human Feedback (GMHF), a novel framework that bridges this domain gap by leveraging expert intuition to guide data synthesis. Grounded in a theoretical analysis of generalization error, we derive bounds demonstrating that aligning the distribution of...

---

### 46. Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

**Authors:** Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00924v1)

**Summary:** Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization ...

---

### 47. Valdi: Value Diffusion World Models

**Authors:** Christopher Lindenberg, Kashyap Chitta

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00917v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00917v1)

**Summary:** World models can enable Model Predictive Control (MPC), but this requires dynamics prediction that is both fast enough for online use and expressive enough to represent uncertain futures. Diffusion models offer a natural mechanism for modeling uncertain dynamics, yet their iterative inference procedure makes them difficult to use for low-latency latent planning. We bridge this gap with Value Diffusion World Models (Valdi), combining end-to-end online training for MPC with a latent diffusion dyna...

---

### 48. Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization

**Authors:** Fei Wang, Chao Xue, Taoran Liu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00908v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00908v1)

**Summary:** Mixed-precision quantization (MPQ) has become a key technique for deploying large language models under stringent memory and compute constraints. We first identify a phenomenon that we term the Perplexity Illusion: layers ranked as important by perplexity-based sensitivity show little rank correlation with those that are most influential for complex reasoning performance, with Kendall $τ\approx 0$ in our analysis. We further reveal an Alignment-Diversity Tradeoff: using only target-task calibrat...

---

### 49. The Binary Tree Mechanism is Optimal for Approximate Differentially Private Continual Counting

**Authors:** Konstantina Bairaktari, Kasper Green Larsen

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00876v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00876v1)

**Summary:** Private continual counting is a fundamental problem in differential privacy: given a binary stream of length $n$, where each $1$ corresponds to the contribution of one individual, the goal is to release all running counts while protecting the privacy of each individual. The standard algorithm is the binary tree mechanism, whose Gaussian-noise variant achieves expected $\ell_\infty$ error proportional to $\log^{3/2} n$ for approximate differential privacy. Whether this dependence on the stream le...

---

### 50. Constrained Bayesian Optimisation with Multiple Information Sources

**Authors:** Hauke Maathuis, Roeland De Breuker, Saullo Castro, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00865v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00865v1)

**Summary:** Bayesian Optimisation (BO) under unknown constraints is particularly challenging when feasible regions are small. In such settings, existing methods that typically rely solely on evaluations of the true objective and constraints struggle to efficiently explore the design space. However, many real-world applications offer auxiliary data sources (e.g. surrogate models or simplified simulations) that can support early exploration. Despite this potential, their integration into constrained BO remain...

---

## cs.NE

**50 papers**

### 1. MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00846v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00846v1)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic cont...

---

### 2. From Consistency to Collaborative Discovery: MFEA-CoD for Multitask Novelty Search

**Authors:** Jiao Liu, Yanchi Li, Hua Yu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00761v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00761v1)

**Summary:** Evolutionary multitasking (EMT) has shown strong capability in solving multiple optimization problems simultaneously by exploiting latent inter-task consistency, such as similarities in promising solutions or search directions. However, most existing EMT studies remain focused on objective-driven optimization, where such consistency is mainly used to accelerate convergence toward predefined optima. In this paper, we move EMT from consistency to collaborative discovery and propose a multifactoria...

---

### 3. Self-Organized Learning in Oscillatory Neural Networks with Memristive Signed Couplings

**Authors:** Riley Acker, Aman Desai, Garrett Kenyon, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00286v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00286v1)

**Summary:** Oscillatory neural networks (ONNs) have emerged as a promising neuromorphic architecture, leveraging coupled dynamical systems to perform computation and represent information through phase relationships. Their interactions can be designed to support intrinsic energy-minimizing dynamics, enabling tasks such as associative memory and optimization, and positioning them as a candidate architecture for continuous learning and inference. We present a neuromorphic primitive implemented using memristiv...

---

### 4. EVOTS: Evolutionary Transformer Search for Time Series Forecasting

**Authors:** AbdElRahman ElSaid, Damir Pulatov

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00154v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00154v1)

**Summary:** Evolutionary neural architecture design for multivariate time-series forecasting remains underexplored, with most approaches relying on fixed Transformer architectures despite substantial variation across tasks and forecasting settings. This paper introduces an evolutionary neural architecture search framework for discovering task-adaptive Transformer-like models for time-series forecasting (EVOTS). Architectures are encoded using a modular genome representation that enables flexible composition...

---

### 5. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 6. Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

**Authors:** Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31789v1)

**Summary:** Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associ...

---

### 7. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 8. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31584v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31584v1)

**Summary:** This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...

---

### 9. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 10. Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization

**Authors:** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30836v1)

**Summary:** Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, w...

---

### 11. Why can genetic algorithms work in high-dimensional search spaces?

**Authors:** Stephen Whitelam

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30619v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30619v1)

**Summary:** We show that the effective dynamics of the elitist $(1+M)$ genetic algorithm is, in the limit of small mutations, clipped gradient descent on the loss in the presence of anisotropic Gaussian white noise. In expectation, therefore, a simple mutation-selection genetic algorithm follows the gradient of the loss, without explicit calculation of gradients and without averaging over loss evaluations. The genetic algorithm is slower than gradient descent because of the noise that acts in directions tra...

---

### 12. Computing the Integral R2 Indicator by Perspective Mapping and Box Decomposition

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30530v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30530v2)

**Summary:** The continuous integral R2 indicator is a Pareto-compliant refinement of the classical finite-weight-vector R2 indicator, used in performance assessment, bounded archiving for a-posteriori multi-objective optimization, and skyline selection in databases. This work introduces a bidirectional perspective mapping between continuous integral R2 computation and integration over unions of anchored axis-aligned boxes. After translating the ideal point of a minimization problem to the origin, approximat...

---

### 13. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30450v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30450v1)

**Summary:** This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. ...

---

### 14. From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent

**Authors:** Haoliang Han

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30191v1)

**Summary:** How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer r...

---

### 15. Semantics-Aware Bilevel Co-Evolution: Towards Automated Multicomponent Algorithm Design

**Authors:** Zhiyao Zhang, Shenghao Wu, Xingyu Wu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29953v1)

**Summary:** LLM-assisted evolutionary search (LES) has emerged as a promising paradigm for automated algorithm design. However, existing methods usually suffer from two inherent limitations when facing the automated design of real-world complex algorithms that usually consist of multiple components. The first limitation is that they either focus on modifying entire algorithms, making it difficult to reuse high-quality components, or concentrate on component refinement within a limited set of predefined mult...

---

### 16. Evolutionary Hyperparameter Optimization to Find Lightweight CNN Models for Autonomous Steering

**Authors:** Devson Butani, Ryan Kaddis, Chan-Jin Chung

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29684v1)

**Summary:** This research investigates the optimization of Convolutional and Dense Neural Networks (CNNs and DNNs) for autonomous steering using the (N+M) Evolution Strategy (ES) with the 1/5th success rule. The primary objective is to develop a lightweight CNN based model capable of real-time steering angle prediction, mimicking human driving behavior on predefined paths. The ES algorithm automates hyperparameter tuning, dynamically adjusting parameters such as filter sizes and layer configurations. Data c...

---

### 17. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 18. Supervised Hebbian learning in Deep Counterstream Associative Networks

**Authors:** Andreas Knoblauch

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29528v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29528v1)

**Summary:** Modern machine learning applications employ deep neural networks training with the error backpropagation algorithm. Although this algorithm is very effective, it lacks biological realism. For example, backpropagation requires symmetric connectivity, and a separate neural processing channel for error signals. Prior works have therefore proposed a number of more realistic alternatives for error backpropagation. However, most of them still suffer from demanding preassumptions that may be not fulfil...

---

### 19. When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**Authors:** Zhengqi Pei, Qingming Huang, Shuhui Wang

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29354v1)

**Summary:** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the a...

---

### 20. Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs

**Authors:** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, et al.

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29254v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29254v1)

**Summary:** Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reaso...

---

### 21. Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning

**Authors:** Reza Ahmadvand, Sarah Safura Sharif, Yaser Mike Banad

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29099v1)

**Summary:** Artificial neural networks (ANN) provide accurate continuous-valued representation, whereas spiking neural networks (SNN) offer event-driven temporal processing, yet both paradigms face limitations when value encoding and timing dynamics must be learned within a single computational structure. This paper introduces a network based on Unified Complex-valued Neuron (UCN), a new neural computational model that integrates continuous activation and phase-driven event generation through an asymmetric ...

---

### 22. Road to scalability for efficient graph search on massively parallel neuromorphic hardware

**Authors:** Oskar von Seeler, Elena C. Offenberg, Carlo Michaelis, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28907v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28907v1)

**Summary:** Efficient computation of shortest paths in weighted graphs is a fundamental problem with many applications. Neuromorphic hardware platforms promise massively parallel, efficient computation, changing parallelism tradeoffs. In this work, we introduce NEURO-MAPP (Neuromorphic-based Min-Add Parallel Propagation), a distributed shortest path algorithm designed to use the local computation and network communication available in neuromorphic systems. We provide an optimized implementation of the algor...

---

### 23. Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28662v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28662v1)

**Summary:** The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studie...

---

### 24. Analysis of Parameter Settings for the Bat Algorithm Using Variance Evolution

**Authors:** Xin-She Yang, Mehmet Karamanoglu

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28644v1)

**Summary:** Parameter settings in evolutionary algorithms and metaheuristics are important because such parameter values can influence the performance of algorithms under evaluation. For a given algorithm, there are many different numerical experiments to show that the algorithm can work well in practice; however, in most cases there is no theoretical analysis of parameter settings. In this work, we show that theoretical analysis using the theory of dynamical systems and evolution of population variance can...

---

### 25. Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

**Authors:** Binh Nguyen, Colleen Josephson, Mircea Teodorescu, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28600v1)

**Summary:** Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement le...

---

### 26. Comparing Scalar Objective Functions for Multi-Criteria Engineering Optimization

**Authors:** Olaf Frommann

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28541v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28541v1)

**Summary:** Scalar objective functions are required when a multi-criteria optimization problem must yield a single preferred design rather than only a Pareto set. The choice of scalarization influences which compromise is selected, how preference parameters are interpreted, and whether non-supported Pareto regions can be reached. This paper compares four formulations for normalized bi-criteria minimization: weighted sums, achievement scalarizing functions, desirability functions, and a fuzzy-logic-based for...

---

### 27. MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28109v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28109v1)

**Summary:** Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a comm...

---

### 28. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 29. Co-Optimization of Analog Kolmogorov-Arnold Networks for Low-Power Function Approximation in Flexible Electronics

**Authors:** Paula Carolina Lozano Duarte, Georgios Zervakis, Mehdi Tahoori, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27892v1)

**Summary:** Wearable devices and Internet of Things (IoT) sensors require on-sensor processing of biosignals and environmental data, including computationally demanding operations such as nonlinear activation functions for neural network inference, sensor calibration curves to map raw readings to physical units, and signal preprocessing functions like logarithmic compression and power operations for feature extraction. These functions exhibit significant complexity, often involving transcendental operations...

---

### 30. Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring

**Authors:** Muhammad Hamza

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.30676v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30676v1)

**Summary:** Deploying spiking neural networks (SNNs) on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies either neglect neuronal criticality or rely on convex relaxations of the inherently combinatorial pruning problem whose fractional masks, upon binarisation, destroy accuracy at moderate-to-high sparsity. We present Criticality-Constrained Quadratic Pruning (CQP), a native PyTorch pipeline that fuses weight magnitude with surrog...

---

### 31. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 32. DE-2LS: Differential Evolution with Lightweight Late Local Search for Constrained Numerical Optimization

**Authors:** Dikshit Chauhan, Anupam Trivedi

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27764v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27764v1)

**Summary:** Constrained single-objective numerical optimization requires a careful balance among feasibility, objective convergence, and computational efficiency under a fixed function-evaluation budget. This paper proposes DE-2LS, a late-stage, locally search-enhanced variant of differential evolution built on the RDEx framework. The proposed method preserves the original RDEx components, including mutation and crossover operators, success-history adaptation, archive mechanism, population-size reduction, a...

---

### 33. DE-2LS: Differential Evolution with Late-Stage local-search for Unconstrained Single-Objective Numerical Optimization

**Authors:** Dikshit Chauhan

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27762v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27762v1)

**Summary:** Unconstrained single-objective numerical optimization requires a careful balance among global exploration, late-stage exploitation, and function-evaluation efficiency. This paper presents DE-2LS, a late-stage, local-search-enhanced differential evolution framework built on RDEx for unconstrained single-objective optimization with variable bounds. The proposed method preserves the original RDEx evolutionary search engine and introduces two conservative refinements: a smoothed exploitation-biased ...

---

### 34. Multi-Objective Molecular Generation with Frequency-Controlled Evolutionary Dynamics

**Authors:** Elia Colleoni, Paolo Guida, Didier Barradas-Bautista, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27467v1)

**Summary:** Molecule generation methods that leverage generative models have been successfully applied to drug discovery. However, they often require extensive pre-training, suffer statistical biases in the training data, and might suffer from limited interpretability of generated chemical structures. In this work, we introduce SpectralMol, an algorithm based on evolutionary computation that processes chemical structures as a compact matrix of Fourier coefficients, projected onto a fixed basis to generate p...

---

### 35. CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention

**Authors:** Sayak Dutta

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27229v2) | 📄 [PDF](https://arxiv.org/pdf/2606.27229v2)

**Summary:** Recurrent models must forget in order to remember, yet the state of the art decides what to erase without consulting what is stored -- the gate sees only the arriving token, not the memory it is about to modify. This memory-blind gating is one of three coupled defects in the leading delta-rule architecture (GDN-2): the value-axis erase mask wastes parameters at the scale of the value projection, and -- as we prove -- mathematically prevents the WY-form triangular chunk solver that makes recurren...

---

### 36. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 37. Random Walk on Bézier Curves for Global Optimization

**Authors:** Jinpeng Wang, Xingguo Xu, Yujing Sun, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26714v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26714v1)

**Summary:** Balancing exploration and exploitation remains a central challenge in metaheuristic optimization. To address this issue, this paper proposes Bézier Walk Evolution (BWE), a geometry-driven optimization framework that reformulates evolutionary search as adaptive trajectory construction in the decision space. BWE integrates Bézier curve modeling with a distance-aware random walk mechanism to generate topology-guided search trajectories. By adaptively varying the curve order during evolution, the pr...

---

### 38. Three-Objective Integral R2 Subset Selection: NP-Hardness and Submodular Approximation

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26591v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26591v1)

**Summary:** Selecting a fixed number of representative points from a finite Pareto-front approximation is a fundamental post-processing task in multiobjective optimization. This paper studies this problem for the integral R2 indicator in three objectives, where the indicator is defined as the integral of the lower envelope of weighted Tchebycheff scalarizations over the two-dimensional weight simplex. We provide two complementary algorithmic results. On the positive side, we show that the integral R2 improv...

---

### 39. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

**Authors:** Alex Iacob, Andrej Jovanović, William F. Shen, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26294v2) | 📄 [PDF](https://arxiv.org/pdf/2606.26294v2)

**Summary:** Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves. This ignores a central feature of evolution: species adapt as their environments change with them. We aim to bring the same principle to recursive self-improvement, making evaluation part of the im...

---

### 40. EvoFlock: evolved inverse design of multi-agent motion

**Authors:** Craig Reynolds

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25280v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25280v1)

**Summary:** This paper describes an automatic method for adjusting or tuning models of multi-agent motion. Simulating the motion of bird flocks, human crowds, vehicle traffic, and other multi-agent systems is a widely used technique. These simulations model the behavior of a single group member (bird, human, or vehicle). The group behaviors (flock, crowd, traffic) emerge from interactions between group members. These models typically have many numerical control parameters. Even if each parameter is intuitiv...

---

### 41. Spatial Partial Functionalization of Neural Networks based on Noise Fields

**Authors:** Shuhei Ikemoto, Fabio DallaLibera

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24588v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24588v1)

**Summary:** Noise in neural computation is typically regarded as a disturbance, but its spatial distribution may also actively regulate which parts of a network participate in computation. This paper investigates the spatial partial functionalization of Noise-modulated Neural Networks using noise fields. We first present an activation function suitable for this goal, the crossing activation function, using the sample-level, statistical-level, and analytical-level implementations, and examine parameter reuse...

---

### 42. What Does a Pathological Speech Assessment Model Know about Acoustic Features? A Case Study on Oral and Oropharyngeal Cancer Patients

**Authors:** Tuan Nguyen, Corinne Fredouille, Alain Ghio, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24949v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24949v1)

**Summary:** This work investigates the interpretability of a Wav2Vec 2.0based speech intelligibility assessment model for oral and oropharyngeal cancer patients through canonical correlation analysis. By measuring the correlation between the model embeddings and eGeMAPS low-level descriptors (LLDs) as an interpretable reference, we analyze how acoustic information is encoded across the model layers. The analysis is conducted at two levels: individual LLDs layer-wise, and group-level: prosodic, spectral, and...

---

### 43. Distributed Quality-Diversity Search for Toxicity in Large Language Models

**Authors:** Onkar Shelar, Travis Desell

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24166v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24166v1)

**Summary:** Large Language Models remain vulnerable to adversarial prompts that elicit harmful responses, and scaling red-teaming to cover a broad range of failure modes is constrained by the cost of text generation and evaluation. We present \emph{ToxSearch-S}, a speciated extension of toxicity-focused evolutionary prompt search with incremental, embedding-driven niche maintenance, together with an MPI master-worker realization that centralizes population and species bookkeeping on rank~0 while offloading ...

---

### 44. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 45. It's Much Easier for Neural Networks to learn Game of Life Dynamics with the Right Activation Function: Polynomial Kolmogorov-Arnold Networks

**Authors:** Tashin Ahmed, Q. Tyrell Davis

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23587v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23587v1)

**Summary:** Previous work has found a gap between the scale of neural networks that reliably learn Conway's Game of Life, and minimal networks capable of representing the classic cellular automaton with hard-coded parameter values. Viewing neural network learning as a search process suggests a dependence on networks large enough to contain sub-networks with lucky initializations (sometimes known as 'winning tickets') that actually learn the task. In this work, we reorient our perspective from discovering Li...

---

### 46. An Open-Source LFSR-Based Stochastic Leaky Integrate-and-Fire Neuron in SkyWater 130 nm: Design, Stochastic Characterisation, and Rate Coding

**Authors:** Poornima Kumaresan, Santhosh Sivasubramani

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23532v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23532v1)

**Summary:** Stochastic spiking neurons trade exact arithmetic for controlled randomness, lowering area and tolerating input noise, which suits event-driven edge hardware. We present a compact, configurable stochastic leaky integrate-and-fire neuron in standard-cell CMOS on the SkyWater 130 nm process, released openly. A 16-bit configurable-polynomial linear-feedback shift register drives an eight-entry programmable activation table that sets a Bernoulli firing probability, and a saturating 16-bit leaky inte...

---

### 47. Local Pheromone Network: Sparse Local Learning with Multi-Scale Synaptic Trails, Consolidation, and Replay

**Authors:** Xingcheng Fu, Xianjun Chen, Zhihao Li

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.30669v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30669v1)

**Summary:** Backpropagation-trained dense neural networks are powerful function approximators, but they couple learning across many parameters and can overwrite previous associations when tasks conflict. This paper describes Local Pheromone Network, a small research prototype for sparse, local, manually updated neural networks. In Local Pheromone Network, each output unit reads only a fixed local neighborhood of input units subject to geometric distance and molecular-tag compatibility. Each synapse stores a...

---

### 48. EML Trees Are Universal Approximators

**Authors:** Joe Germany, Elie Abdo, Joseph Bakarji

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23179v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23179v1)

**Summary:** The recently introduced EML (Exp-Minus-Log) function acts as continuous analogue of NAND gates, providing a compositional building block capable of representing elementary functions. In this work, we study the expressive power of tree-structured compositions of EML functions. We show that such trees enjoy a universal approximation property for functions in $W^{k, \infty}$ for $k \in \mathbb N$, drawing on classical neural network approximation arguments while exploiting the ability to explicitly...

---

### 49. Decomposing Financial Market Dynamics via Mechanism Analysis in an Evolutionary Multi-Agent Simulation

**Authors:** Zhibao Chen

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23158v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23158v1)

**Summary:** Evolutionary agent-based markets (ABMs) couple several mechanisms -- who reproduces, how price forms, how biased the agents are, how consensus propagates -- yet these are usually fixed by convention, so it is unclear which mechanism controls which emergent property. In a coevolving, endogenous-price simulator with 120 heterogeneous behavioral agents, we make four mechanisms pluggable and run matched 3x20-seed interventions. We find the levers are largely separable. (1) Selection -> diversity: a ...

---

### 50. Self-Modulating Quantum Fast-Weight Programmers for Efficient Adaptive Sequential Learning

**Authors:** Samuel Yen-Chi Chen, Yifeng Peng, Kuo-Chung Peng, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.24933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24933v1)

**Summary:** Recent advances in quantum machine learning have motivated efficient models for sequential data processing. In this paper, we propose Self-Modulating Quantum Fast Weight Programmers, or Self-Modulating QFWP, which extends Quantum Fast Weight Programmers by introducing adaptive modulation over both newly generated fast-weight updates and historical fast-weight memory. Numerical results show that the proposed mechanism improves convergence stability and prediction performance across varying model ...

---

## q-bio.NC

**50 papers**

### 1. DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00851v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00851v1)

**Summary:** Brain activity spans single-neuron, population, and network levels, and core questions in neural coding require moving between them. Yet current tools target a single paradigm and incompatible data formats, leaving cross-level questions hard to address. We present DRIADA, an open-source Python framework that unifies neural signals and time-aligned behavior in a shared data model, so selectivity testing, dimensionality reduction, and network analysis operate within a unified workflow. We evaluate...

---

### 2. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00397v1)

**Summary:** Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...

---

### 3. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 4. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 5. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v1)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 6. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 7. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 8. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 9. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 10. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 11. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 12. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 13. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 14. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 15. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 16. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

### 17. Weight geometry governs functional memory in complex systems

**Authors:** Elkaïoum M. Moutuou, Habib Benali

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25826v1)

**Summary:** Complex systems, from gene regulatory networks to neural circuits and transportation infrastructures, exhibit rich functional behaviour that topology alone does not capture. Here we show that functional memory exhibits a universal organisational regularity: in every biological, ecological, social, and technological domain studied, real interaction strengths organise memory at greater hierarchical depth than random weight assignment on the same topology, across thirty-four networks spanning sever...

---

### 18. Meta-learning as a principle for human-like visual representations

**Authors:** Can Demircan, Marcel Binz, Alireza Modirshanechi, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.28399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28399v1)

**Summary:** The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few obse...

---

### 19. A pilot study examining transcranial photobiomodulation therapy intervention in college students with insomnia

**Authors:** Jiangshan He, Lianghua Zhang, Dan Liang, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24668v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24668v1)

**Summary:** College students commonly report insufficient sleep and poor sleep quality, with ~30% meeting insomnia criteria, posing significant threats to their physical growth, cognitive development, and overall well-being, as well as imposing a substantial economic burden on society [1]. The hyperarousal model of insomnia [2] emphasizes that hyperarousal across cognitive, emotional, and physiological domains mutually reinforces one another. Neuroimaging studies have further identified prefrontal hypoactiv...

---

### 20. EEG Interpretation Across Chant Listening: A Single-Subject Pilot Investigation Using Spectral and Functional Connectivity Analysis

**Authors:** Prerna Singh, Aishwarya Ghosh, Neelam Sinha, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24406v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24406v1)

**Summary:** This technical report presents an EEG-based investigation of neural activity across five auditory conditions: Resting State (RS), Shiv Tandav Stotra (STS), Mahasudarshan Mantra (MM), Aum Chant, and Tanpura Listening. EEG recordings acquired from a healthy 5-year-old participant were analyzed using spectral power estimation and functional connectivity measures based on the weighted Phase Lag Index (wPLI). Spectral analysis revealed condition-specific modulation of neural oscillatory activity, wit...

---

### 21. Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**Authors:** Xavier Vasques, Paul Barbaste, Olivier Oullier

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24394v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24394v1)

**Summary:** Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (fea...

---

### 22. Graph-based analysis of inflammatory profiles in New Onset Refractory Status Epilepticus (NORSE)

**Authors:** Linon Denis, Martin Guillemaud, Vincent Navarro, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24351v1)

**Summary:** Background and Objectives: Cryptogenic new-onset refractory status epilepticus (cNORSE) represents one of the most severe forms of status epilepticus, occurring in patients without prior neurological disease, and remaining of unknown aetiology despite extensive diagnostic evaluation. Emerging evidence supports a role for immune dysregulation in cNORSE; however, marked heterogeneity in inflammatory signatures has been reported, complicating the selection of targeted immunotherapies. Therefore, a ...

---

### 23. The Morality Game: An online multiplayer platform to standardize, expedite, and expand research on cooperation

**Authors:** Gregory N. Stanley, Alan Yang, Liam Tsimhoni, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24037v1)

**Summary:** This paper presents the Morality Game, a platform designed to standardize and accelerate research on cooperation and morality through game theory-based experiments. The Morality Game functions as a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process. It allows researchers to launch customized online multiplayer experiments with zero coding, using game trees to simulate moral dilemmas. The platform automates part...

---

### 24. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 25. The adaptive nature of confirmation bias

**Authors:** Dorje C. Brody, Karl J. Friston, Bernhard K. Meister, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23325v1)

**Summary:** In this paper, the phenomenon generally classified as confirmation bias is formulated on the space of square-root probabilities (or equivalently, using the structures of quantum probability). In this framework, observations are modelled by matrices, rather than random variables on a probability space. In the problem of binary hypothesis testing, an optimal evidence choice minimises the expected error probability. We show that the resulting optimal choice of evidence leads to a confirmation bias,...

---

### 26. Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg

**Authors:** Helio V. Cabral, Giacomo Valli, Roberto Zanotti, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23066v1)

**Summary:** Common synaptic input is considered a fundamental principle of motor neuron control and represents the dominant component of the neural drive transmitted from the motor neurons to muscle. Recent advances in High-Density surface Electromyography (HDsEMG) and motor unit (MU) decomposition algorithms have enabled the concurrent identification of increasingly large populations of MUs and substantially expanded the possibility of estimating common synaptic input from MU spike trains, making this appr...

---

### 27. SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings

**Authors:** Yisi S. Zhang, Daniel Y. Takahashi

**Published:** 2026-06-21

🔗 [Paper](http://arxiv.org/abs/2606.22695v1) | 📄 [PDF](https://arxiv.org/pdf/2606.22695v1)

**Summary:** Mapping the directed flow of information between brain regions -- their effective connectivity -- is central to understanding brain function, yet large-scale recordings sample only a fraction of the brain at a time: sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established directed-connectivity methods (Granger causality, dynamic causal modeling, partial directed coherence, PDC) require all regions to be recorded ...

---

### 28. DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**Authors:** Jayadratha Gayen, Bradly Alicea

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21940v1)

**Summary:** Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed...

---

### 29. Dynamic Computerized Tumbling-E Testing for Temporal Reliability of Human Sequential Perceptual Decisions

**Authors:** Avneek Sandhu, Bin Hu

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21818v1)

**Summary:** OBJECTIVES: Visual acuity and tumbling-E tasks are often treated as static threshold measures, yet sequential perceptual decisions unfold over time. A computerized tumbling-E task preserves response latency, timeouts, and stimulus-size adaptation, creating a temporal reliability dataset rather than only a chart-line score. This matters for human-AI comparison because the Temporal Hallucination Index (THI) shows how static accuracy can obscure delays, drift, persistence, and unstable convergence....

---

### 30. Mostly-monocular responses and other visual functions in a multiscale network model of Macaque V1

**Authors:** Zhuo-Cheng Xiao, Kevin K. Lin, Lai-Sang Young

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21785v2) | 📄 [PDF](https://arxiv.org/pdf/2606.21785v2)

**Summary:** Visual signals from the two eyes merge gradually as they pass through the primary visual cortex (V1). Here we use a computational model of Macaque V1 to study the first stage of this integration along the magnocellular pathway, in layer 4C$α$, aiming to infer neuroanatomical origins of binocular response. It is known that neurons in layer 4C$α$ are predominantly monocular, though some do exhibit varying degrees of binocularity. We find (1) the emergence of narrow binocular strips along borders o...

---

### 31. Delay coordinates synchronization and induces abrupt transition in excitable networks

**Authors:** Bruno R. R. Boaretto, Kalel L. Rossi, Lyle E. Muller, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21703v1)

**Summary:** Neuronal communication is inherently time-delayed, due to the finite speed of signal propagation. Although often considered challenging or disruptive, such time delays can also endow neural circuits with useful capabilities. Here, we show that delays in excitatory connections between excitable neurons coordinate their synchronization patterns by creating self-sustained oscillations that may be out-of-phase or in-phase. The emergence of these oscillations leads to an abrupt, explosive, transition...

---

### 32. Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks

**Authors:** Stephen Coombes, Rüdiger Thul, Stefan Ruschel, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21508v1)

**Summary:** We develop a theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model as an analytically tractable event-based description of neural dynamics. For networks with fixed delays, we derive self-consistency conditions for phase-locked states and an associated linear stability theory formulated directly in terms of spike-time perturbations. The framework is illustrated for a delayed autapse, a reciprocally coupled two-cell network, and spatially structured rings wit...

---

### 33. Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity

**Authors:** Ch. Meessen

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21432v1)

**Summary:** We construct a minimal but biologically plausible spiking neuron model operating in discrete time, combining multiplicative spike-timing-dependent plasticity (WSTDP), divisive normalization of synaptic integration, homeostatic threshold adaptation, and a one-step refractory period. We show that this normalization admits a biologically plausible dendritic implementation in which each binary junction operates using only locally available information.   Assembling excitatory-inhibitory pairs of suc...

---

### 34. Relational Gaze Transitions During Encoding Predict Episodic Recall of Naturalistic Scenes

**Authors:** Hugo Rydel, Alex Kafkas

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20844v1)

**Summary:** Remembering a visual scene requires organizing distinct details into a cohesive event. This study investigates whether relation-guided gaze transitions provide a behavioural marker of this cognitive organization during episodic encoding and retrieval. By applying scene graph annotations to eye-tracking data, we measured whether gaze moved between objects that were meaningfully related within complex scenes. This approach allowed us to quantify relational scanning within naturalistic environments...

---

### 35. Synchronization modes in bipartite oscillator networks

**Authors:** Pau Pomés, Bastian Pietras, Ernest Montbrió

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20345v1)

**Summary:** Collective oscillations in neuronal systems often arise from interactions between excitatory and inhibitory populations rather than from recurrent coupling within a single ensemble. Motivated by the coexistence of strongly and partially synchronized regimes in such systems, we study the Kuramoto Sakaguchi model on a bipartite network. Despite its minimal structure, the model exhibits rich collective dynamics, including both continuous and discontinuous transitions from full synchrony to partial ...

---

### 36. Quadratic Forms for Measuring Geometric Trees in 3-dimensional Space

**Authors:** Yossi Bokor Bleile, Emanuele Cortinovis, Herbert Edelsbrunner, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20096v1)

**Summary:** Tree-like structures appear in many areas of science, and their shapes can help understand the underlying processes they drive or that give rise to them.   By thinking of these structures as geometric graphs in $\mathbb{R}^3$, we gain access to tools from computational geometry and topology to study them.   In this paper, we adopt the theory of quadratic forms to measure the directional spread of geometric graphs, and we introduce the hexplot model -- equipped with a metric derived from the Fish...

---

### 37. Robust probabilistic measurement of structural-functional module consistency in infant brain development

**Authors:** Lingbin Bian, Feihong Liu, Qian Wang, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.19739v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19739v1)

**Summary:** Brain network is commonly divided into modules for analyzing their functionally segregated roles for group-level analysis in neuroimaging studies. Here, we introduce stochastic modules within brain networks for a robust probabilistic measurement of structural-functional module consistency (SFMC) in a group of subjects. Specifically, a stochastic module can be regarded as the chance of a brain region across subjects potentially being assigned to a group-level sub-network, characterized as an assi...

---

### 38. Retrieval-Based Brain Decoding by Alignment, not Complexity

**Authors:** Matteo Ciferri, Matteo Ferrante, Nicola Toschi

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.19081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19081v1)

**Summary:** A prominent theory in cognitive science suggests that concepts in the brain are organized as high-dimensional vectors, with semantic meaning captured by directions and relative angles in this space. Brain decoding is the effort of reconstructing or retrieving stimuli (or their representations) from neural activity and involves finding a function that approximates how the brain represents concepts. This motivates the investigation of contrastive objectives as biologically plausible candidates to ...

---

### 39. Dissecting emerging slow rhythms in delay-coupled neural oscillators

**Authors:** Xinxin Qie, Matteo Martin, Shenquan Liu, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.20733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20733v1)

**Summary:** Synaptic transmission delays are ubiquitous in neural circuits and can alter the dynamical repertoire of coupled oscillators quantitatively and qualitatively. Here, we demonstrate that delayed coupling in inhibitory networks introduces an effective slow-fast structure in the phase-difference dynamics, generating low-frequency components that are not due to intrinsic cellular properties, and we show that this behavior is not specific to a particular model structure. The origin of this generic phe...

---

### 40. Can neurons speak? Semantic narration of vision at single-cell resolution

**Authors:** Arnau Marin-Llobet, Richard Hakim, Sara Matias, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.18667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.18667v1)

**Summary:** Identifying what individual neurons encode in higher-order visual cortex is an open problem. Responses resist intuitive parameterization, and the deep-network embeddings used in their place are black boxes. Here, we introduce NEURRATOR, a framework that decodes spiking activity into free-form natural-language narration of the viewed scene at single-neuron resolution. A learned encoder maps spike trains from arbitrary subsets of simultaneously-recorded neurons into the patch-embedding space of a ...

---

### 41. Separating wiring-specific from statistical control of dynamics in a complete connectome

**Authors:** Stavros Therianos

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17745v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17745v1)

**Summary:** Electron-microscopy reconstruction now yields complete synaptic wiring diagrams, or connectomes, of entire small brains, including the larval Drosophila, the first insect brain reconstructed in full. How far a wiring diagram alone fixes a circuit's activity, as opposed to the finer physiological detail it does not record, is debated. We run a complete connectome as a fixed, rate-based dynamical operator in which no single-neuron parameter is fitted, so that, at one fixed dynamical regime, the mo...

---

### 42. BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17742v1)

**Summary:** Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than...

---

### 43. Ten Years of the Stochastic Resonance Model of Tinnitus: From Phantom Perception to Adaptive Sensory Optimization

**Authors:** Patrick Krauss, Achim Schilling

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17736v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17736v1)

**Summary:** Subjective tinnitus - the perception of sound in the absence of an external acoustic stimulus - remains one of the most debated phenomena in auditory neuroscience. In 2016, the stochastic resonance (SR) model was introduced as an alternative account of tinnitus-related neuronal hyperactivity, proposing that internally generated neural noise is adaptively upregulated to restore information transmission after hearing loss. Rather than interpreting increased spontaneous activity as maladaptive, the...

---

### 44. Embodiment Shapes Rolling Behavior in a Multimodal Infant Model

**Authors:** Leon Philipp, Francisco M. López, Jochen Triesch

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17456v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17456v1)

**Summary:** Rolling over is one of the earliest milestones in infant motor development, reflecting the emergence of coordinated, whole-body sensorimotor control. Here, we conduct a computational study of infant rolling using MIMo, a virtual infant embodiment equipped with proprioception and vestibular sensation. MIMo learns supine-to-prone rolls with reinforcement learning. Interestingly, the learned behaviors capture developmental trends and coordination patterns consistent with those reported in real infa...

---

### 45. Adaptive inference and function vectors in deep transformers

**Authors:** Ravin Raj, Gautam Reddy

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16694v1)

**Summary:** Transformers are widely used as a general-purpose substrate for learning complex correlations between a large collection of coupled variables, but their internal mechanisms have remained mysterious. We introduce a theory of a deep transformer as a mean-field interacting system that implements distributed inference, subject to constraints on communication, locality and depth. We show that such a system can exploit internal state representations ('function vectors') to infer a latent context varia...

---

### 46. Learning Hybrid Biophysical Neuron Models with Neural ODEs

**Authors:** Jonas Beck, Michael Deistler, Dóra Viktória Molnár, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16693v1)

**Summary:** Biophysical neuron models link measurements of neural activity to underlying cellular mechanisms. Yet, a central challenge is that the kinetics of many ion channels are poorly characterized, and practical simplifications -- omitting channels or reducing morphological detail -- introduce systematic gaps between model and biology. Bridging these gaps requires approaches that can flexibly discover unmodeled dynamics while preserving mechanistic interpretability. Here, we introduce a hybrid modeling...

---

### 47. Infant Spontaneous Movement Noise Improves Exploration in Deep RL

**Authors:** Francisco M. López, Markus R. Ernst, Francisco Cruz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16590v2) | 📄 [PDF](https://arxiv.org/pdf/2606.16590v2)

**Summary:** Exploration in deep reinforcement learning (RL) is commonly implemented as temporally uncorrelated white noise. However, recent works show that temporally correlated colored noise can improve exploration efficiency by producing smooth trajectories with better coverage of the state space. We inquire whether action noise inspired by infant spontaneous movements can also improve exploration in deep RL. We find that the power spectral densities of babies' end-effector velocities follow a colored noi...

---

### 48. Sex-based Network-Specific Differences in Connectomes: A Krakencoder-Based Analysis

**Authors:** Vibhashree S H, Debanjali Bhattacharya, Vamshi Krishna Kancharla, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16294v1)

**Summary:** This study examines how deficiencies in one brain connectome modality propagate to the other, using the Krakencoder as a simulation framework. Structural and functional connectomes from 702 healthy participants in the Human Connectome Project were analyzed, with the impact of each of the Yeo-7 functional networks assessed separately. Seven scenarios were considered, each involving the removal of a single network while the remaining networks were preserved. The resulting perturbations in cross-mo...

---

### 49. EEGDash: An open-source platform for machine learning on public neurophysiological data

**Authors:** Bruno Aristimunha, Aviv Dotan, Pierre Guetschel, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.16041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16041v1)

**Summary:** Public neurophysiological datasets are increasingly accessible but remain hard to reuse: turning one into a trained model still takes thousands of lines of code for download, loading, format repair, windowing, and evaluation, and a dataset that meets metadata standards can still fail to load. EEG-Dash is a software resource that catalogues 791 publicly archived recordings (39,778 participants, over 86,051 hours) spanning electroencephalography (EEG), magnetoencephalography (MEG), intracranial EE...

---

### 50. Task-guided cross-subject latent alignment: a multi-encoder-decoder VAE

**Authors:** Angeliki Papathanasiou, Jascha Achterberg, Thomas E. Nichols, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15989v1)

**Summary:** Aligning neural activity across subjects offers the promise of discovering shared computational principles and generalizable decoders. However, traditional alignment methods require shared stimuli across subjects, a constraint that limits applicability to naturalistic paradigms with limited or non-overlapping data. We introduce a Multi-Encoder-Decoder Variational Autoencoder (MED-VAE) that achieves cross-subject alignment without shared stimuli by anchoring representations to a common scaffold p...

---

## stat.ML

**50 papers**

### 1. Decision-Aware Training for Sample-Based Generative Models

**Authors:** Kornelius Raeth, Nicole Ludwig

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01171v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01171v1)

**Summary:** Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. These models are commonly trained with strictly proper scoring rules, such as the energy score, which allocate their training signal in proportion to data density, with no awareness of where forecast errors are most costly for downstream decisions. We therefore propose decision-aware training for sampl...

---

### 2. Characterizing and Identifying Separable Graphical Models

**Authors:** Christopher Meek, Kayvan Sadeghi

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01057v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01057v1)

**Summary:** We study a broad class of graphical models whose independencies correspond to vertex separation in mixed graphs with directed, undirected, and bidirected edges, that are capable of encoding independence structures arising from feedback, latent and selection mechanisms. In particular, we introduce separable graphs, in which each missing edge implies the existence of a separating set for its endpoints, and essentially separable graphs, those graphs separation equivalent to a separable graph. We sh...

---

### 3. Function-Counting Theory for Low-Dimensional Data Structures

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01010v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01010v1)

**Summary:** The success of deep learning models in classification and regression is widely attributed to the low-dimensional structure that real-world data tend to exhibit, despite their high-dimensional representation. This work attempts to provide a mathematical framework for binary classification on low-dimensional data, building on Cover's (1965) function-counting theory. With our framework, we aim to address the question of how the low-dimensional structure of the data affects the classification capabi...

---

### 4. Deep Multitask Learning for Mixed-Type Outcomes with Shared Sparsity

**Authors:** Huichao Li, Tong Wang, Sanguo Zhang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00995v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00995v1)

**Summary:** Most existing multitask learning approaches are limited by their reliance on task-specific loss functions tailored to the scale and type of each outcome. When outcomes differ across tasks, these losses are generally not directly comparable, which makes it difficult to formulate a unified objective and may limit information sharing across tasks. We propose a multitask transformation framework in which task-specific responses may differ through unknown monotone transformations. Motivated by high-d...

---

### 5. Hierarchical Variational Kalman Filtering

**Authors:** Shilei Li, Dawei Shi, Wei Zheng, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00877v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00877v1)

**Summary:** Traditional variational Kalman filtering with unknown noise statistics suffers from inconsistent process covariance estimation and slow convergence speed, limiting its practical utility. To address these issues, we introduce a surrogate variable representing the process-noise-free state, which enables explicit modeling and inference of process noise statistics. In addition, we reformulate the conventional coordinate ascent variation inference (CAVI) as a marginalized maximum a posteriori problem...

---

### 6. Convolutional Symmetric AutoEncoders: enhancing latent stability via differential geometry

**Authors:** G. Li Causi, N. Tonicello, L. Magri, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00669v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00669v1)

**Summary:** Autoencoders (AEs) have emerged as powerful tools for non-linear dimensionality reduction, often surpassing traditional linear methods such as Proper Orthogonal Decomposition (POD) in scenarios characterized by slowly decaying Kolmogorov $n$-widths. In the realm of Reduced-Order Modelling (ROM), these models are increasingly utilized to learn low-dimensional representations of solution manifolds associated with parametric Partial Differential Equations (PDEs). However, the high expressivity of A...

---

### 7. Approximate full-conformal multi-task regression with reproducing kernels

**Authors:** Davidson Lova Razafindrakoto, Alain Celisse, Jérôme Lacaille

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00645v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00645v1)

**Summary:** Multi-task regression aims at jointly solving multiple regression problems, called tasks. Compared to solving each task separately, better performances can be achieved as long as the tasks are sufficiently related. Full-conformal prediction is a framework that formulates a data-dependent prediction-region containing the unknown output-vector at any prescribed confidence level. However, explicit computation of this prediction-region is intractable in general since it requires training infinitely ...

---

### 8. Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization

**Authors:** Xuefeng Liu, Mingxuan Cao, Qinan Huang, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00531v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00531v1)

**Summary:** Scientific reasoning is an increasingly important capability of large language models, yet improving the robustness and efficiency of training such reasoning remains a key open challenge. We study this problem in instruction-based molecular optimization, where answer-only supervised fine-tuning (SFT) collapses multi-step reasoning and reinforcement learning with verifiable rewards (RLVR) suffers from sparse feedback. Reference-guided Policy Optimization mitigates both by anchoring policy updates...

---

### 9. From Structural Equation Modelling to Double Machine Learning: Robustness Analysis for Survey-Based Research

**Authors:** Ka Ching Chan, Qiana Liu, Sanjib Tiwari, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00512v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00512v1)

**Summary:** Structural equation modelling (SEM) is widely used in survey-based business and information systems research to assess latent constructs and theory-driven structural relationships. However, SEM path significance is obtained within a particular model specification and may not show whether findings remain stable under alternative estimation frameworks. This study develops and demonstrates a staged robustness analysis framework that connects SEM, ordinary least squares (OLS) regression, and Double ...

---

### 10. Prototype Language Models

**Authors:** Dan Ley, Giang Nguyen, Himabindu Lakkaraju, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00510v1)

**Summary:** Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Mode...

---

### 11. Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain Generalization

**Authors:** Peilin Liu, Ding-Xuan Zhou

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00479v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00479v1)

**Summary:** Transformer-based large models have demonstrated remarkable generalization abilities across different tasks by leveraging a context-aware attention module for in-context learning. With richer context, transformers adapt more effectively to the current use case without any parameter updates. However, the quadratic computational and memory complexity with respect to context length significantly slows data processing in softmax transformers. Linear transformers were proposed to address this issue b...

---

### 12. Neural Network-Based Estimation of Time-Dependent Parameters in AR(p) Processes

**Authors:** Agnieszka Kopeć, Paweł Przybyłowicz, Martyna Wiącek

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00470v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00470v1)

**Summary:** We investigate a forecasting framework based on a simple discrete-time dynamic model with coefficients varying in time. The parameters of the model are recovered within a deep learning framework, which makes it possible to retain a transparent parametric structure while simultaneously accounting for complex and nonstationary patterns in the observed phenomenon. Our analysis covers two specifications of the noise process. Besides the standard Gaussian setting, we also consider Laplace-distributed...

---

### 13. From Spectral Methods to Sample Complexity Bounds for Fourier Neural Operators

**Authors:** Nisha Chandramoorthy, Daniel Sanz-Alonso, Nathan Waniorek

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00320v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00320v1)

**Summary:** We establish approximation and learning guarantees for Fourier neural operators (FNOs) applied to time-$T$ solution operators of dissipative evolution equations. The analysis builds on the premise that FNOs can efficiently approximate and learn solution operators whenever these operators admit stable and accurate spectral discretizations. To formalize this idea, we introduce classes of evolution operators defined through spectral methods and derive FNO approximation bounds and polynomial sample ...

---

### 14. Entropy-Regularized Probabilistic Gates for Sparse Model Discovery in Scarce-Data Federated Learning

**Authors:** Krishna Harsha Kovelakuntla Huthasana, Alireza Olama, Andreas Lundell

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00275v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00275v1)

**Summary:** Federated Learning (FL) is a distributed machine learning (ML) paradigm with collaboration among multiple clients without sharing data. FL is challenging under data heterogeneity and partial client participation. Learning sparse models is useful for communication and computational efficiency in FL, but it is especially difficult in the small-sample high-dimensional regime (d >> N) where optimization can yield parameter configurations that fail to generalize to unseen test data. While magnitude-b...

---

### 15. Distributionally Robust Linear Regression With Block Lewis Weights

**Authors:** Naren Sarayu Manoj, Kumar Kshitij Patel

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00252v1)

**Summary:** We present an algorithm for the group distributionally robust (GDR) least squares problem. Given $m$ groups, a parameter vector in $\mathbb{R}^d$, and stacked design matrices and responses $\mathbf{A}$ and $\mathbf{b}$, our algorithm obtains a $(1+\varepsilon)$-multiplicative optimal solution using $\widetilde{O}(\min\{\mathsf{rank}(\mathbf{A}),m\}^{1/3}\varepsilon^{-2/3})$ linear-system-solves of matrices of the form $\mathbf{A}^{\top}\mathbf{B}\mathbf{A}$ for block-diagonal $\mathbf{B}$. Our t...

---

### 16. Sample Complexities of Estimating Gumbel--Max Watermark Proportions with and without Reduction to Pivotal Statistics

**Authors:** Shuwen Chai, Qiaosen Wang

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00224v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00224v1)

**Summary:** Watermarking promises a statistical trace of large language model (LLM) use, but real documents, after editing or paraphrasing, rarely arrive as purely human-written or purely machine-generated. This motivates a quantitative question beyond detection: what proportion of a document is generated from a pre-specified watermarked LLM? We study this watermark proportion estimation problem under the Gumbel--max watermarking mechanism, treating the next-token prediction (NTP) distributions as unknown a...

---

### 17. Homogenization of $\ell_2$-Adversarial Training in High-Dimensions: Exact Dynamics under Stochastic Gradient Descent

**Authors:** Fabrizzio Sabelli

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00207v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00207v1)

**Summary:** We develop a framework for analyzing the learning dynamics of $\ell_2$-adversarial training of single-index models on Gaussian mixtures in the high-dimensional limit under streaming stochastic gradient descent (SGD). We derive deterministic equivalents for a broad class of statistics of the SGD iterates, including the adversarial risk and distance to adversarial optimality, in terms of the solution to a system of ODEs. We use them to study two idealized learning rate schedules: the Polyak stepsi...

---

### 18. GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity

**Authors:** Yong Yi Bay, Kathleen A. Yearick

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00152v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00152v1)

**Summary:** Three of the most popular methods for training language models to reason look like three different tricks. They are not. All three adjust a single number: standard deviation, reflecting how much a prompt's sampled answers disagree. When such a model is trained, it answers each problem many times, and an automatic checker marks every answer right or wrong. The standard deviation of those marks measures the disagreement: largest when the answers split evenly between right and wrong, and zero when ...

---

### 19. Uniform-in-time Propagation-of-Chaos for Stein Variational Gradient Descent

**Authors:** Krishnakumar Balasubramanian, Sayan Banerjee, Anna Korba

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00149v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00149v1)

**Summary:** We study uniform-in-time propagation-of-chaos for continuous-time Stein Variational Gradient Descent (SVGD). Classical finite-time propagation-of-chaos estimates for mean-field systems typically deteriorate rapidly with time and therefore do not directly explain the long-time relation between the finite-particle system and its mean-field limit. We obtain two complementary classes of uniform-in-time propagation-of-chaos results.   For broad distributional metrics, we introduce a cutoff strategy w...

---

### 20. Random Reshuffling Dominates Stochastic Gradient Descent

**Authors:** Zijian Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32005v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32005v1)

**Summary:** Stochastic Gradient Descent ($\textsf{SGD}$) is one of the most classical optimization algorithms with favorable theoretical guarantees, yet the practical implementation of $\textsf{SGD}$ differs subtly from its well-known form and is often referred to as Shuffling Stochastic Gradient Descent ($\textsf{Shuffling SGD}$). A particularly popular strategy in $\textsf{Shuffling SGD}$ is Random Reshuffling ($\textsf{RR}$), which has achieved great empirical success across numerous experiments. Despite...

---

### 21. Signed-Permutation Coordinate Transport for RMSNorm Transformers

**Authors:** John Sweeney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31963v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31963v1)

**Summary:** Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...

---

### 22. Accelerating Conformal Prediction via Approximate Leave-One-Out

**Authors:** Jiachen Cong, Jingbo Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31915v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31915v1)

**Summary:** While conformal prediction provides a general framework for uncertainty quantification in predictive inference, its application is often limited by computational cost. Recent methods, including Jackknife+ and Jackknife-minmax, achieve faster computation by trading a slight loss of efficiency relative to full conformal prediction, but still requires computing leave-one-out refits for all observations. In this paper, we further accelerate conformal prediction by incorporating approximate leave-one...

---

### 23. Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models

**Authors:** Keivan Faghih Niresi, Alice Cicirello, Olga Fink

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31804v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31804v1)

**Summary:** Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-...

---

### 24. Policy Optimization Achieves Data-Dependent Regret Bounds in MDPs with Unknown Transitions

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31769v1)

**Summary:** We study policy optimization for online episodic tabular Markov decision processes with unknown transition kernels, aiming for best-of-both-worlds guarantees together with data-dependent regret bounds. Recent work (Dann et al., 2023; Li et al., 2026) has shown that policy optimization can adapt to both adversarial and stochastic losses with first-order, second-order, and path-length bounds, but only under known transitions, leaving open whether such data-dependent guarantees are achievable by po...

---

### 25. On Optimal Data Splitting for Split Conformal Prediction

**Authors:** Sayan Das, Bahram Yaghooti, Todd A. Kuffner, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31600v1)

**Summary:** Conformal prediction and its variants, including the split conformal prediction, provide a distribution-free framework for uncertainty quantification by constructing prediction intervals or sets with finite-sample coverage guarantees. The statistical efficiency of these intervals depends critically on how the data are split into training and calibration samples. Despite its practical importance, a principled characterization of the training-calibration split that minimizes prediction interval le...

---

### 26. On the Convergence of Self-Improving Online LLM Alignment

**Authors:** Xudong Wu, Pangpang Liu, Vaneet Aggarwal, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31524v1)

**Summary:** The Self-Improving Alignment (SAIL) algorithm addresses distribution shift by reducing a bilevel formulation of the problem to an efficient, single-level method. Empirically, SAIL has demonstrated strong performance on this task. However, a formal analysis of its convergence properties has been lacking. We identify a key theoretical challenge: the standard SAIL objective function is not guaranteed to be strongly concave due to unfavorable properties of its Hessian. To address this limitation, we...

---

### 27. Contextual Slate GLM Bandits with Limited Adaptivity

**Authors:** Tanmay Goyal, Sukruta Prakash Midigeshi, Gaurav Sinha

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31449v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31449v1)

**Summary:** We investigate the contextual slate bandit problem with generalized linear rewards under limited adaptivity. At each round, the learner is presented with $N$ sets of items, where each item is represented by a $d$-dimensional feature vector. The learner then constructs a slate by selecting one item per set; the resulting slate yields a scalar reward sampled from a Generalized Linear Model (GLM). We propose algorithms under two limited-adaptivity settings: (a) Batched and (b) Rarely-Switching. For...

---

### 28. Sequential sparse Gaussian process quantile regression

**Authors:** Hugo Nicolas, Olivier Le Maître

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31284v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31284v1)

**Summary:** Quantile regression aims to estimate the conditional quantiles of a response variable from observed data. In a Bayesian setting, Gaussian process quantile regression provides uncertainty quantification but faces significant computational challenges due to the nonconjugacy of the asymmetric Laplace likelihood and the cost of posterior inference. We develop a sparse Gaussian process framework in which the quantile function is represented through a reduced set of inducing variables and posterior in...

---

### 29. MNAR-$k$-means: A $k$-means Clustering for Data Missing Not at Random with Magnitude-Decaying Probability

**Authors:** Xin Guan

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31253v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31253v1)

**Summary:** The classical $k$-means clustering, based on distances computed from all data features, cannot be directly applied to incomplete data with missing values. A natural extension of $k$-means to missing data is to involve only the observed positions in clustering, which is equivalent to imputing missing values by corresponding cluster means. However, for data missing not at random (MNAR), since missingness is related to data values, such a mean-imputation-based method may lead to the distortion of e...

---

### 30. Learning Gaussian Graphical Models from a Glauber Trajectory Without Mixing

**Authors:** Eric Shen, Tony Wu, Mahbod Majid, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31230v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31230v1)

**Summary:** We study the task of learning the structure of a $d$-sparse Gaussian graphical model on $n$ variables from a single trajectory of Glauber dynamics. Beyond algorithmic considerations, many applications present temporally correlated observations rather than i.i.d.\ samples. In the classical i.i.d.\ setting, under comparably general sparsity and minimum edge-strength assumptions, sublinear-in-$n$ sample guarantees are known, but achieving them in polynomial-time remains open. Motivated in part by t...

---

### 31. Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?

**Authors:** Davy Guan, Lu Zhang, Asiri Wijesinghe, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31126v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31126v1)

**Summary:** Predicting biomolecular properties from limited labeled data is a central bottleneck in protein engineering and small-molecule design. As strong pretrained encoders now supply rich fixed-length representations, the difficulty has shifted from representation learning to building a data-efficient predictor for the few-shot regime. Tabular foundation models such as TabPFN3 and TabICL are unlikely candidates for this role: they are in-context learners pretrained on synthetic tables drawn from random...

---

### 32. Dynamic Gaussian Processes and the Vanilla-SPDE Exchange

**Authors:** Rui-Yang Zhang, Lachlan Astfalck, Edward Cripps, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31063v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31063v1)

**Summary:** Gaussian process inference is often limited by cubic computational costs, a challenge that becomes more pronounced in spatio-temporal settings where posterior inference is required over dense grids. While state-space SPDE formulations enable linear complexity in time, exact inference remains cubic in space and deteriorates further when observation locations are disjoint from the prediction locations, which inflates the number of considered spatial points. To address this, we propose the Vanilla-...

---

### 33. Multistage Defer Trees for Hybrid Interpretability: If at First You Can't Succeed, Tree Again

**Authors:** Zakk Heile, Hayden McTavish, Margo Seltzer, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.30995v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30995v1)

**Summary:** Recent work has shown that well-optimized individual decision trees can match complex black box models in some settings, primarily in noisy domains. For the remaining settings, however, complex ensembled compositions of trees often achieve higher accuracy at the cost of interpretability, leaving practitioners with difficult modeling decisions along an accuracy-interpretability tradeoff. Ideally, we would like to classify as much of the data as possible with one or a small number of trees, achiev...

---

### 34. Exponential-Family Tensor Completion via Nonconvex Dual Total-Variation Regularization

**Authors:** Wenfei Cao, Yang Chen, Qibin Zhao, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30958v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30958v1)

**Summary:** With the emergence of various tensor data, tensor completion from partial measurements has attracted widespread attention in data science and signal processing. Total Variation (TV) has been widely used as an effective regularization technique for tensor completion; however, theoretical studies on TV regularization in this context remain limited. In this work, we present a rigorous theoretical analysis of TV regularization for tensor completion. Specifically, we consider tensor completion under ...

---

### 35. SGD at the Edge of Stability: Stochastic Stabilization with Large Learning Rates

**Authors:** Konstantinos Emmanouilidis, Lachlan MacDonald, Salma Tarmoun, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30930v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30930v1)

**Summary:** Modern deep learning has been shown to operate at the edge of stability, routinely using learning rates far larger than those justified by classical optimization theory. Most prior analyses of the edge of stability phenomenon focus on deterministic gradient descent, leaving the stochastic setting largely unexplored. In this work, we provide sharp convergence guarantees for Stochastic Gradient Descent (SGD) applied to the multiclass cross-entropy loss, for both linear classifiers and two-layer ne...

---

### 36. Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback

**Authors:** Ved Sriraman, Peihan Liu, Daniel Hsu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30923v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30923v1)

**Summary:** Imitation Learning is a natural framework for learning in sequential decision-making systems and has emerged as the dominant paradigm through which we understand language model training. A central puzzle is that, while in theory offline IL can be horizon-free and optimal, in practice online methods such as on-policy distillation often outperform offline methods such as supervised fine-tuning. We propose a noisy expert model to explain this gap, in which the learner only has access to a noisy ver...

---

### 37. Dynamic Prediction of Alternating Recurrent Events via Neural Network

**Authors:** Abigail Loe, Susan Murry, Zhenke Wu

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30889v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30889v1)

**Summary:** Alternating recurrent events -- event-times of a specific nature that trigger a secondary refractory period -- occur in a wide-range of fields, including behavioral science, criminal justice, and biostatistics. Analysis of these events requires careful attention to the statistical nuance, including correlated observations and repeated outcomes subject to potential censoring. We develop an online dynamic prediction framework appropriate for predicting subsequent alternating recurrent events, by d...

---

### 38. A Stationary-Distribution Theory for Triplet-Based Plateau Search in Random Forest Ensemble-Size Selection

**Authors:** Andrey A. Dukhovny, Andrey M. Lange

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30837v1)

**Summary:** The number of trees is a central computational parameter in Random Forests: increasing it reduces finite-ensemble variability but increases training and prediction cost. Plateau-based tuning adapts this parameter through local comparisons of out-of-bag scores at a geometric triplet of tree counts. After the remaining hyperparameters have stabilized, however, the central triplet point need not converge to a deterministic value; instead, it fluctuates around a stationary regime.   This paper devel...

---

### 39. Geometric Dyson Brownian Motions and the Free Log-Normal Limit for a Non-Square Product of Random Matrices

**Authors:** Mufan Li, Jaume de Dios Pont, Mihai Nica, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30831v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30831v1)

**Summary:** We study the squared singular value spectrum of a product of non-square random matrices, a setting that also corresponds to the feature covariance eigenvalues of a deep linear neural network at initialization. We first take a proportional depth-width $d,n$ limit with the number of data points $m$ held fixed, and show that the resulting covariance eigenvalue process satisfies a geometric version of Dyson Brownian motion. We then take a second, sequential mean-field limit corresponding to the scal...

---

### 40. Separation Capacity of Scattering Networks

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30822v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30822v1)

**Summary:** In this paper, we attempt to enhance the theoretical understanding of convolutional neural networks (CNNs) as feature extractors in classification tasks by analyzing them through the lens of Cover's function-counting theory. Specifically, our focus lies on the notion of separation capacity, a combinatorial quantity derived from counting the number of realizable dichotomies (i.e., binary label assignments). Our contributions are threefold. First, we extend Cover's framework by establishing a conc...

---

### 41. Predictable GRPO: A Closed-Form Model of Training Dynamics

**Authors:** Rajat Ghosh, Datta Nimmaturi, Aryan Singhal, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30789v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30789v2)

**Summary:** We develop a first-principles reduced-order model of these dynamics. Under a single mean-field assumption that summarizes the policy by its expected reward, we reduce the GRPO update to a stochastically-forced damped oscillator whose mass, damping, and stiffness are fixed in closed form by the optimizer hyperparameters together with a single measured curvature scale -- momentum supplies the inertia, off-policy lag erodes the damping, and the group size enters, to leading order, as a noise temper...

---

### 42. Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models

**Authors:** Subramanyam Sahoo, Aman Chadha, Vinija Jain, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30627v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30627v1)

**Summary:** Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to exploit imperfections in a learned reward model. We challenge this intuition empirically and mechanistically. We train a Qwen3-14B policy under Direct Preference Optimisation (DPO) with three levels of conservatism ($β\in \{β_{\mathrm{lo}}, β_{\mathrm{mid}}, β_{\mathrm{hi}}\}$ derived from empirical l...

---

### 43. Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding Norms

**Authors:** Ziwei Su, Junyu Ren, Victor Veitch

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30625v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30625v1)

**Summary:** Contrastive embedding models trained with scale-invariant losses are typically paired with distance metrics like cosine similarity, effectively ignoring embedding magnitudes. However, surprisingly, empirical studies reveal that despite this, these "discarded" norms seem to correlate with semantic properties such as concept specificity, token frequency, and human uncertainty. In this work, we provide a formal theoretical framework explaining this phenomenon. By analyzing the optimization dynamics...

---

### 44. The Fundamental Limits of Valid Transport Map Estimation

**Authors:** Sivaraman Balakrishnan

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30574v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30574v1)

**Summary:** Many modern generative modeling methods, including diffusion models, normalizing flows, and flow matching, estimate transport maps or plans between distributions without explicitly targeting an optimal transport (OT) map. In applications like generative modeling, the transport cost itself is irrelevant, and this makes it natural to target maps which are more tractable from either a statistical or computational standpoint. In this short note, we formalize the task of estimating any valid transpor...

---

### 45. Convergence of Continual Learning in Homogeneous Deep Networks

**Authors:** Matan Schliserman, Gon Buzaglo, Itay Evron, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30559v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30559v1)

**Summary:** We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationary (single-task) deep models or continual linear models. We show that global convergence generally fails, even for simple models linear in data but nonlinear in parameters. Nevertheless, by leveraging results from nonconvex projection theory, we identify regularity properties of homogeneous deep netw...

---

### 46. ITSPACE: Monotone Gaussian Optimal Transport Updates

**Authors:** Woojoo Na, Jennifer Dy

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30523v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30523v1)

**Summary:** Covariance matrices serve as compact descriptors of feature distributions in many machine-learning pipelines, including domain adaptation and Gaussian embeddings. Under a centered Gaussian approximation, the unregularized Wasserstein-2 optimal-transport (OT) discrepancy admits a closed form on covariances given by the Bures-Wasserstein (BW) objective on the symmetric positive definite (SPD) cone. We propose ITSPACE (Iterative Transport for Stable Proximal Alignment of Covariance Embeddings), a p...

---

### 47. Doubly Robust Adaptive Conformal Inference for Causal Effects Under Temporal Dependence

**Authors:** Andreas Koukorinis, Ricardo Silva

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30500v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30500v1)

**Summary:** We propose doubly robust adaptive conformal inference (DR-ACI), which constructs prediction intervals for doubly robust pseudo-outcomes under temporal dependence.

---

### 48. Factorizable Normalizing Flows for parameter-dependent density morphing

**Authors:** Davide Valsecchi, Mauro Donegà, Rainer Wallny

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30489v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30489v1)

**Summary:** Normalizing Flows excel at modeling a single fixed density, yet many problems across the sciences, such as high energy physics, instead require modeling how that density deforms as a function of continuous parameters: the strength of a physical effect, a calibration constant, or a source of systematic uncertainty. Learning a separate flow for every parameter configuration quickly becomes intractable, since the number of joint settings grows exponentially with the number of parameters. We introdu...

---

### 49. Non-parametric recovery of causal diffusion mechanisms from steady-state observations

**Authors:** Richard Schwank, Mathias Drton

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30467v1)

**Summary:** We consider sparse multivariate stochastic systems that evolve in continuous time according to a causal mechanism and present methodology to recover the system's time-infinitesimal transition mechanism from mere cross-sectional data. This observational paradigm is motivated by applications such as gene expression analysis, where destructive experimental techniques may only allow recording data once over a cell's lifetime. Precisely, we assume the system follows a time-homogeneous diffusion proce...

---

### 50. Curvature-Weighted Gradient Diversity: A Noise Measure for Geometry-Adaptive SGD Schedules

**Authors:** Muhammad Hamza, Ayush Goel

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30455v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30455v1)

**Summary:** The standard convergence analysis of mini-batch stochastic gradient descent (SGD) models gradient noise using a single variance term that treats all parameter directions equally, ignoring the fact that noise in high-curvature directions has less impact because learning rates are already constrained there. We introduce Curvature-Weighted Gradient Diversity (CWGD), a geometry-aware measure that weights per-sample gradient diversity by the inverse square root of the Hessian, providing a tighter pro...

---

