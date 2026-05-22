# arXiv Daily Digest - 2026-05-22

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22817v1)

**Summary:** Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po...

---

### 2. The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning

**Authors:** Vishal Rajput

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22800v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22800v1)

**Summary:** Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching p...

---

### 3. Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models

**Authors:** Krishnakumar Balasubramanian

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22795v1)

**Summary:** We propose and analyze a conservative drifting method for one-step generative modeling. The method replaces the original displacement-based drifting velocity by a kernel density estimator (KDE)-gradient velocity, namely the difference of the kernel-smoothed data score and the kernel-smoothed model score. This velocity is a gradient field, addressing the non-conservatism issue identified for general displacement-based drifting fields. We prove continuous-time finite-particle convergence bounds fo...

---

### 4. MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

**Authors:** Qianshu Cai, Yonggang Zhang, Xianzhang Jia, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22794v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22794v1)

**Summary:** Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artif...

---

### 5. Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

**Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22791v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22791v1)

**Summary:** Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state, reducing sequence mixing to linear time and decoding to constant memory. The hard part is not just what to forget, but how to edit this compressed memory without scrambling existing associations. Delta-rule models subtract the current read before writing a new value, and Kimi Delta Attention (KDA) sharpens forgetting with channel-wise decay. But the active edit still uses a single scalar gate to...

---

### 6. LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

**Authors:** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22786v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22786v1)

**Summary:** Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque c...

---

### 7. DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

**Authors:** Yunpeng Dong, Jingkai He, Yuze Hou, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22781v1)

**Summary:** LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs.   This paper observes that subsequent checkpoints in AI ag...

---

### 8. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis

**Authors:** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22776v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22776v1)

**Summary:** Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed...

---

### 9. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data

**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22775v1)

**Summary:** Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated flight deck assistance, yet two challenges persist: handling frequent data missingness from blinks and tracking failures, and efficiently modeling long-range temporal dependencies. We propose MambaGaze, a framework that addresses these challenges through 1) XMD encoding, which augments raw features ...

---

### 10. CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation

**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22774v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22774v1)

**Summary:** Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundation models pre-trained on millions of clinical recordings offer rich representations, but cannot be directly applied to wearable devices due to sensor configuration mismatch and task differences. In this paper, we propose CogAdapt, a framework that adapts clinical ECG foundation models to wearable cog...

---

### 11. Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals

**Authors:** Yu Tang, Muhammad Zakwan, Efe Balta, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22773v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22773v1)

**Summary:** The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combinatorial complexity of the problem, rendering it intractable for conventional mixed-integer linear programming solvers. This paper proposes an event-based \gls{DRL} approach to solve FJSP with random job arrivals. Specifically, we employ the Proximal Policy Optimization algorithm and use lightweight M...

---

### 12. Reducing Political Manipulation with Consistency Training

**Authors:** Long Phan, Devin Kim, Alexander Pan, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22771v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22771v1)

**Summary:** Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refer to this phenomenon as covert political bias and identify 7 categories of techniques through which it operates. We propose two metrics for covert bias: Sentiment Consistency measures symmetry in rhetoric and framing across paired political prompts; Helpfulness Consistency measures symmetric depth a...

---

### 13. Understanding Data Temporality Impact on Large Language Models Pre-training

**Authors:** Pilchen Hippolyte, Fabre Romain, Signe Talla Franck, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22769v1)

**Summary:** Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we study the impact of pre-training dynamics on the acquisition of time-sensitive factual knowledge, focusing specifically on data ordering. Our main contributions are twofold. First, we introduce a comprehensive benchmark of over 7,000 temporally grounded questions and an evaluation protocol that ena...

---

### 14. Advancing Mathematics Research with AI-Driven Formal Proof Search

**Authors:** George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22763v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22763v1)

**Summary:** Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in languages like Lean. We perform the first large-scale evaluation of this method's ability to solve open problems. Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in comb...

---

### 15. Towards a General Intelligence and Interface for Wearable Health Data

**Authors:** Girish Narayanswamy, Maxwell A. Xu, A. Ali Heydari, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22759v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22759v1)

**Summary:** While ubiquitous wearable sensors capture a wealth of behavioral and physiological information, effectively transforming these signals into personalized health insights is challenging. Specifically, converting low-level sensor data into representations capable of characterizing higher-level states is difficult due to high phenotypic diversity and variation in individual baseline health, physiology, and lifestyle factors. Moreover, collecting wearable data paired with health outcome annotations i...

---

### 16. Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization

**Authors:** Adis Alihodžić, Eva Tuba, Milan Tuba

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22749v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22749v1)

**Summary:** Modern smart grids rely on dense measurement infrastructures, communication links, and intelligent field devices. Although this improves supervision and control, it also increases vulnerability to cyber-physical disruptions. Operators must distinguish physical incidents, such as faults or line disturbances, from malicious actions, such as false data injection or unauthorized command execution. This chapter investigates this problem using the well-known MSU/ORNL Power System Attack Dataset. The p...

---

### 17. Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning

**Authors:** Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22748v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22748v1)

**Summary:** Autonomous systems have achieved superhuman performance in isolation or simulation, yet they remain brittle in shared, dynamic real-world spaces. This failure stems from the dominant single-agent paradigm for physical applications, where other actors are ignored or treated as environmental noise, preventing effective coordination. Here we show that multi-agent reinforcement learning provides the essential safety scaffolding required for real-world interaction. Using high-speed quadrotor racing a...

---

### 18. Proxy-Based Approximation of Shapley and Banzhaf Interactions

**Authors:** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22738v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22738v1)

**Summary:** Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed and accuracy. To overcome this limitation, we introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction. On a theoretical level, we derive a polynomial-time generalization of interventional TreeSHAP t...

---

### 19. The Distillation Game: Adaptive Attacks & Efficient Defenses

**Authors:** Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22737v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22737v1)

**Summary:** Distillation attacks create a deployment trade-off for model providers: the same outputs that make a model more useful can also make it easier to imitate. We study this trade-off through a minimax game between a utility-constrained teacher and an adaptive student. Our framework yields tractable one-sided response rules: an adaptive evaluation rule in which the student reweights high-value examples, and a teacher-side defense template that suppresses outputs most useful for distillation. From a c...

---

### 20. HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools

**Authors:** Edwin Jose

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22733v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22733v1)

**Summary:** Every Python function deployed as an LLM tool must today exist in two forms: an HTTP endpoint for human-facing clients and CI pipelines, and an MCP tool registration for agent runtimes such as Claude and Cursor. These representations share business logic yet diverge in all the surrounding machinery (routing, validation, serialisation, streaming, and schema maintenance), and they drift apart as the underlying code evolves. We present HarnessAPI, a Python framework that eliminates this duplication...

---

### 21. Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models

**Authors:** Juergen Dietrich

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22732v1)

**Summary:** We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model (LLM) pipeline. Using a Bundestag plenary speech by Felix Banaszak (51 segments, 245 s) as a case study, we compare three analysis modalities: (1) emotion2vec_plus_large, an acoustic speech emotion recognition (SER) model whose continuous Arousal and Valence values are derived via post-hoc Russell C...

---

### 22. Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation

**Authors:** Dong Nie

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22731v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22731v1)

**Summary:** Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed through their loss functions: maximum likelihood, policy gradients, forward KL, reverse KL, or related objective-level variants. We study a complementary factor: the state distribution on which supervision is applied. For an autoregressive policy, a state is a prompt plus generated prefix. SFT trains on fixed dataset states, while RL and on-policy dist...

---

### 23. The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler

**Authors:** Md Sahil Akhtar, Aymane El Gadarri, Vivek F. Farias, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22723v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22723v1)

**Summary:** A central error measure in Gaussian DDPMs is the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. This quantity is especially relevant for procedures such as classifier guidance, which perturb the entire reverse trajectory rather than only the terminal sample. Prior analyses show that standard isotropic reverse covariances suffer an unavoidable $Ω(1/T)$ path-KL error as the number of denoising steps $T$ grows. We show that matching the full poste...

---

### 24. Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts

**Authors:** Andrii Kryshtal

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22720v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22720v1)

**Summary:** AI models are already deployed in societies affected by armed conflict, and journalists, humanitarian workers, governments and ordinary citizens rely on them for information or for their work processes. No established practice exists for checking whether their outputs can make those conflicts worse. We tested nine model configurations from four providers (OpenAI, Anthropic, DeepSeek, xAI) on 90 multi-turn scenarios designed to surface misaligned behaviour in conflict contexts: false equivalence ...

---

### 25. Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators

**Authors:** Zachary Novack, Stephen Brade, Haven Kim, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22717v1)

**Summary:** Interactive streaming music generation promises the use of generative models for live performance and co-creation that is impossible with offline models. However, SOTA models exist in the discrete-AR regime, requiring industrial levels of compute for both training and inference. In this work, we investigate whether audio diffusion models, with their wide support in the open-source community but non-streaming bidirectional nature, can be repurposed efficiently into interactive models accessible o...

---

### 26. Parametric Modular Answer Set Programs Made Declarative

**Authors:** Jorge Fandinno, Yuliya Lierler, Torsten Schaub

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22716v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22716v1)

**Summary:** In this paper, we explore the concept of modularity in first-order answer set programming (ASP). We introduce a new formalism called parametric modular logic programs, which allows defining subprograms with parameters and intensionality statements. We demonstrate how this formalism can capture the semantics of clingo-programs with collective control, a feature that enables structuring and instantiating subprograms. We provide theoretical foundations for modular ASP, illustrate its usefulness, an...

---

### 27. AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild

**Authors:** Baiyu Chen, Zechen Li, Wilson Wongso, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22715v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22715v1)

**Summary:** As wearable and mobile devices become increasingly embedded in daily life, they offer a practical way to continuously sense human motion in the wild. But inertial signals are highly dependent on the sensing setup, including body location, mounting position, sensor orientation, device hardware, and sampling protocol. This setup dependence makes it difficult to learn motion representations that transfer across devices and datasets, and limits the broader use of wearable IMUs beyond closed-set reco...

---

### 28. AMEL: Accumulated Message Effects on LLM Judgments

**Authors:** Sid-ali Temkit

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22714v1)

**Summary:** Large language models are routinely used as automated evaluators: to review code, moderate content, or score outputs, often with many items passing through one conversation. We ask whether the polarity of prior conversation history biases subsequent judgments, an effect we call the accumulated message effect on LLM judgments (AMEL). Across 75,898 API calls to 11 models from 4 providers (OpenAI, Anthropic, Google, and four open-source models), we present identical test items in isolation or follo...

---

### 29. Abstraction for Offline Goal-Conditioned Reinforcement Learning

**Authors:** Clarisse Wibault, Alexander Goldie, Antonio Villares, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22711v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22711v1)

**Summary:** Markov Decision Processes (MDPs) often exhibit significant redundancy due to symmetries and shared structure across state-goal pairs in real-world Goal-Conditioned Reinforcement Learning (GCRL). While hierarchical policies have been motivated for horizon reduction via temporal abstraction in offline GCRL, we demonstrate that hierarchy also enables absolute abstraction. By introducing relativised options as well as distinct representations for different levels of the hierarchy, we demonstrate how...

---

### 30. Beyond the Org Chart: AI and the Transformation of Invisible Work

**Authors:** Stephanie Rosenthal, Shamsi Iqbal

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22707v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22707v1)

**Summary:** An increasing number of news and research articles report that AI adoption is allowing professionals to blur and extend the boundaries of their corporate roles. With the goal of understanding how work processes might be changing in an AI-forward company, we interviewed 24 product-focused individuals at a large technology firm about how AI has impacted their own work, their work within their product team, and their professional interactions. Our conversations suggest that AI is not only changing ...

---

### 31. Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments

**Authors:** Hoang-Dung Bui, Abhish Khanal, Raihan Islam Arnob, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22693v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22693v1)

**Summary:** Autonomous robot teams navigating partially known environments face costly backtracking when ground robots encounter blocked roads that are only revealed upon physical traversal. We address this with Scout-Assisted Planning, a heterogeneous planning framework in which scouting Unmanned Aerial Vehicles proactively gather environmental information to improve Unmanned Ground Vehicle navigation. To focus scouting on the most consequential edges, we propose Information Gain-based Action Pruning, whic...

---

### 32. Forecasting Scientific Progress with Artificial Intelligence

**Authors:** Sean Wu, Pan Lu, Yupeng Chen, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22681v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22681v1)

**Summary:** Artificial intelligence (AI) is increasingly embedded in scientific discovery, yet whether it can anticipate scientific progress remains unclear. To study this question, we introduce a temporally grounded evaluation framework for forecasting scientific progress under controlled knowledge constraints. We present CUSP (Cutoff-conditioned Unseen Scientific Progress), a multi-disciplinary and event-level benchmark that evaluates scientific forecasting in AI systems through feasibility assessment, me...

---

### 33. Swift Sampling: Selecting Temporal Surprises via Taylor Series

**Authors:** Dahye Kim, Bhuvan Sachdeva, Karan Uppal, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22678v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22678v1)

**Summary:** While most frames in long-form video are redundant, the critical information resides in temporal surprises: moments where the actual visual features deviate from their predicted evolution. Inspired by the human brain's predictive coding, we introduce Swift Sampling, an elegant, training-free frame selection algorithm that automatically identifies high-information moments in a video. Specifically, we model a video as a differentiable trajectory in the visual latent space and compute the velocity ...

---

### 34. Is Capability a Liability? More Capable Language Models Make Worse Forecasts When It Matters Most

**Authors:** Nick Merrill, Jaeho Lee, Ezra Karger

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22672v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22672v1)

**Summary:** We document inverse scaling in LLMs on forecasting problems whose underlying time series exhibit superlinear growth and tail risk of regime change, a structure common in finance and epidemiology. On these tasks, more capable models produce worse distributional forecasts. The pattern appears on ForecastBench-Sim (FBSim), a contamination-free, simulated-world benchmark we release, in forecasting synthetic SIR epidemics with a matched linear control, and replicates in real-world datasets on COVID-1...

---

### 35. WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

**Authors:** Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22664v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22664v1)

**Summary:** LLM agents are increasingly expected to carry out end-to-end workflows, producing complete artifacts from high-level user instructions. To meet enterprise needs, frontier AI labs have developed agents that can construct entire spreadsheets from scratch. This is especially relevant in finance, where core workflows such as financial modeling, forecasting, and scenario analysis are commonly conducted through spreadsheets. Yet, existing spreadsheet benchmarks do not measure this advanced capability,...

---

### 36. Claw AI Lab: An Autonomous Multi-Agent Research Team

**Authors:** Fan Wu, Cheng Chen, Zhenshan Tan, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22662v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22662v1)

**Summary:** We present Claw AI Lab, a lab-native autonomous research platform that advances automated research from a hidden prompt-to-paper pipeline into an interactive AI laboratory. Rather than centering the system around a single agent or a fixed serial workflow, we allow users to instantiate a full research team from one prompt, with customizable roles, collaborative workflows, real-time monitoring, artifact inspection, and rollback/resume control through a unified dashboard. The platform also supports...

---

### 37. Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora

**Authors:** Maciej Skorski

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22660v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22660v1)

**Summary:** Moral language is subtle and culturally variable, making it difficult to translate faithfully across languages. Idiomatic expressions, slang, and cultural references introduce hard-to-avoid translation artifacts. Yet automated moral values classification depends on language-specific annotated corpora that exist almost exclusively in English. We investigate whether LLM-based translation can bridge this gap, taking Polish as a test case. Using $\sim$50k morally-annotated social media posts from a ...

---

### 38. AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters

**Authors:** Hanjun Luo, Zhimu Huang, Sylvia Chung, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22645v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22645v1)

**Summary:** Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts. Yet current benchmarks fix the prompt and only evaluate T2I models, leaving the prompting proficiency of this upstream component entirely unmeasured. We introduce AtelierEval, the first unified benchmark that quantifies prompting proficiency across 360 expert-crafted tasks. Grounded in a cognitive view, it spans three task...

---

### 39. Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

**Authors:** Banghao Chi, Yining Xie, Mingyuan Wu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22642v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22642v1)

**Summary:** Spreadsheet systems (e.g., Microsoft Excel, Google Sheets) play a central role in modern data-centric workflows. As AI agents grow increasingly capable of automating complex tasks, such as controlling computers and generating presentations, building an AI-driven spreadsheet agent has emerged as a promising research direction. Most existing spreadsheet agents rely on specialized prompting over general-purpose LLMs; while this design has potentials on simple spreadsheet operations, it struggles to...

---

### 40. More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts

**Authors:** Víctor Yeste, Paolo Rosso

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22641v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22641v1)

**Summary:** Detecting Schwartz values in political text is difficult because implicit cues often depend on surrounding arguments and fine-grained distinctions between neighboring values. We study when context and explicit moral knowledge help sentence-level value detection. Using the ValuesML/Touch{é} ValueEval format, we compare sentence, window, and full-document inputs; no-RAG and retrieval-augmented settings with a curated moral knowledge base; supervised DeBERTa-v3-base/large encoders; and zero-shot LL...

---

### 41. Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents

**Authors:** Ting Liu

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22634v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22634v1)

**Summary:** Skills are increasingly used to package agent instructions, workflows, scripts, and reference materials. In enterprise settings, however, skills often need to express more than task guidance: they must make goals, input boundaries, permissions, evidence requirements, output contracts, quality criteria, verification steps, human approval points, and handoff rules inspectable. This paper proposes contractual skills, a GovernSpec-inspired design framework for organizing SKILL.md files as readable t...

---

### 42. Healthcare LLM Benchmarks Are Only as Good as Their Explicit Assumptions

**Authors:** Naveen Raman, Santiago Cortes-Gomez, Mateo Dulce Rubio, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22612v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22612v1)

**Summary:** Benchmarks are necessary for healthcare evaluation, but are not sufficient for predicting deployment performance. Our position is that the evaluation--deployment gap arises not because of poorly designed benchmarks, but from implicit assumptions about how users interact with models that cannot be surfaced from benchmarks alone. To make this precise, we propose a classification of assumptions into two categories: task, which can be tested from conversation data alone, and outcome, which requires ...

---

### 43. Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

**Authors:** Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22608v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22608v1)

**Summary:** Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. This autonomy poses serious challenges for overseeing and assessing agent behavior. Most current tools are limited, focusing on observability with basic evaluation capabilities or imposing static, hand-crafted error taxonomies that cannot adapt to new domains. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. It pro...

---

### 44. Innovations in Cardless Artificial Intelligence Banking: A Comprehensive Framework for Cyber Secure and Fraud Mitigation using Machine Learning Algorithms

**Authors:** Md Israfeel

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22604v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22604v1)

**Summary:** The advent of cardless artificial intelligence (AI) banking heralds a paradigm shift in the financial landscape, offering users unprecedented security and convenience. This paper outlines a comprehensive framework designed to enhance cybersecurity, introduce auto-generated virtual cards, and mitigate fraud risks within cardless AI banking systems. The framework envisions a future banking architecture that employs AI-powered data cryptography to create secure virtual cards for seamless transactio...

---

### 45. Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents

**Authors:** Minghui Ma, Bin Guo, Runze Yang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22602v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22602v1)

**Summary:** Persuasive dialogue requires reasoning about others' latent mental states, a capability known as Theory of Mind (ToM). However, due to reliance on simple prompting strategies and insufficient ToM knowledge, existing LLMs often fail to capture the intrinsic dependencies among mental states, leading to fragmented representations and unstable reasoning. To address these challenges, we introduce the ToM-based Persuasive Dialogue (ToM-PD) task, grounded in the Belief-Desire-Intention (BDI) framework,...

---

### 46. MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy

**Authors:** Jiaxu Wang, Junhao He, Jingkai Sun, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22597v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22597v1)

**Summary:** Learning real-world dynamics from visual observations is crucial for various domains. A common strategy is to calibrate simulators by estimating physical parameters, yet accuracy is ultimately bounded by the underlying physical models, which often assume materials are homogeneous and isotropic. Even if reasonable, real-world objects typically exhibit mild anisotropy and heterogeneity. After the near-isotropic backbone is well calibrated, these residual effects become the key bottleneck for furth...

---

### 47. SceneAligner: 3D-Grounded Floorplan Localization in the Wild

**Authors:** Junhyeong Cho, Ruojin Cai, Hadar Averbuch-Elor

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22581v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22581v1)

**Summary:** Many public buildings provide floorplans with a "you are here" indicator to help visitors orient themselves. Floorplan localization seeks to computationally replicate this capability by determining where visual observations were captured within a floorplan. However, existing methods typically assume controlled small-scale environments and precise vectorized floorplans, limiting their ability to operate in large-scale buildings and rasterized floorplans. In this work, we present an approach for p...

---

### 48. Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion

**Authors:** Meimingwei Li, Yuanhao Ding, Esteban Garces Arias, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22579v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22579v1)

**Summary:** Recent work has identified a counterintuitive phenomenon termed "Hyperfitting", where fine-tuning Large Language Models (LLMs) to near-zero training loss on small datasets surprisingly enhances open-ended generation quality and mitigates repetition in greedy decoding. While effective, the underlying mechanism remains poorly understood, with the extremely low-entropy output distributions suggesting a potential equivalence to simple temperature scaling. In this work, we demonstrate that this pheno...

---

### 49. VGenST-Bench: A Benchmark for Spatio-Temporal Reasoning via Active Video Synthesis

**Authors:** Jinho Park, Youbin Kim, Hogun Park, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22570v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22570v1)

**Summary:** Spatio-temporal reasoning is a core capability for Multimodal Large Language Models (MLLMs) operating in the real world. As such, evaluating it precisely has become an essential challenge. However, existing spatio-temporal reasoning benchmark datasets primarily rely on static image sets or passively curated video data, which limits the evaluation of fine-grained reasoning capabilities. In this paper, we introduce VGenST-Bench, a video benchmark that employs generative models to actively synthesi...

---

### 50. Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard

**Authors:** Sahar Abdelnabi, Chris Hicks, Konrad Rieck, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22568v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22568v1)

**Summary:** The benchmarks used to evaluate AI agents in security-critical roles suffer from crucial weaknesses. Building on recent empirical evidence, we characterize three core challenges that undermine security evaluations: benchmark vulnerabilities, temporal staleness, and runtime uncertainty. We then outline practical directions toward building more robust and trustworthy evaluation frameworks.

---

## cs.CL

**50 papers**

### 1. Tokenisation via Convex Relaxations

**Authors:** Jan Tempus, Philip Whittington, Craig W. Schmidt, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22821v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22821v1)

**Summary:** Tokenisation is an integral part of the current NLP pipeline. Current tokenisation algorithms such as BPE and Unigram are greedy algorithms -- they make locally optimal decisions without considering the resulting vocabulary as a whole. We instead formulate tokeniser construction as a linear program and solve it using convex optimisation tools, yielding a new algorithm we call ConvexTok. We find ConvexTok consistently improves intrinsic tokenisation metrics and the bits-per-byte (BpB) achieved by...

---

### 2. Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22817v1)

**Summary:** Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po...

---

### 3. Evaluating Commercial AI Chatbots as News Intermediaries

**Authors:** Mirac Suzgun, Emily Shen, Federico Bianchi, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22785v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22785v1)

**Summary:** AI chatbots are rapidly shaping how people encounter the news, yet no prior study has systematically measured how accurately these systems, with their proprietary search integrations and retrieval-synthesis pipelines, handle emerging facts across languages and regions. We present a 14-day (February 9-22, 2026) evaluation of six AI chatbots (Gemini 3 Flash and Pro, Grok 4, Claude 4.5 Sonnet, GPT-5 and GPT-4o mini) on 2,100 factual questions derived from same-day BBC News reporting across six regi...

---

### 4. Reducing Political Manipulation with Consistency Training

**Authors:** Long Phan, Devin Kim, Alexander Pan, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22771v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22771v1)

**Summary:** Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refer to this phenomenon as covert political bias and identify 7 categories of techniques through which it operates. We propose two metrics for covert bias: Sentiment Consistency measures symmetry in rhetoric and framing across paired political prompts; Helpfulness Consistency measures symmetric depth a...

---

### 5. Understanding Data Temporality Impact on Large Language Models Pre-training

**Authors:** Pilchen Hippolyte, Fabre Romain, Signe Talla Franck, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22769v1)

**Summary:** Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we study the impact of pre-training dynamics on the acquisition of time-sensitive factual knowledge, focusing specifically on data ordering. Our main contributions are twofold. First, we introduce a comprehensive benchmark of over 7,000 temporally grounded questions and an evaluation protocol that ena...

---

### 6. ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning

**Authors:** Md Shamim Ahmed, Farzaneh Firoozbakht, Lukas Galke Poech, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22734v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22734v1)

**Summary:** Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a different disease at age 13. Existing KGs such as PrimeKG, Hetionet, and iKraph do not encode when a finding becomes clinically relevant over the course of a disease. This limits their usefulness for longitudinal clinical reasoning and retrieval augmentation.   We introduce ChronoMedKG, a temporal ...

---

### 7. Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models

**Authors:** Juergen Dietrich

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22732v1)

**Summary:** We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model (LLM) pipeline. Using a Bundestag plenary speech by Felix Banaszak (51 segments, 245 s) as a case study, we compare three analysis modalities: (1) emotion2vec_plus_large, an acoustic speech emotion recognition (SER) model whose continuous Arousal and Valence values are derived via post-hoc Russell C...

---

### 8. AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild

**Authors:** Baiyu Chen, Zechen Li, Wilson Wongso, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22715v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22715v1)

**Summary:** As wearable and mobile devices become increasingly embedded in daily life, they offer a practical way to continuously sense human motion in the wild. But inertial signals are highly dependent on the sensing setup, including body location, mounting position, sensor orientation, device hardware, and sampling protocol. This setup dependence makes it difficult to learn motion representations that transfer across devices and datasets, and limits the broader use of wearable IMUs beyond closed-set reco...

---

### 9. AMEL: Accumulated Message Effects on LLM Judgments

**Authors:** Sid-ali Temkit

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22714v1)

**Summary:** Large language models are routinely used as automated evaluators: to review code, moderate content, or score outputs, often with many items passing through one conversation. We ask whether the polarity of prior conversation history biases subsequent judgments, an effect we call the accumulated message effect on LLM judgments (AMEL). Across 75,898 API calls to 11 models from 4 providers (OpenAI, Anthropic, Google, and four open-source models), we present identical test items in isolation or follo...

---

### 10. Tokenization with Split Trees

**Authors:** Craig W. Schmidt, Michael Krumdick, Adam Wiemerslage, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22705v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22705v1)

**Summary:** We introduce Tokenization with Split Trees (ToaST), a subword tokenization method that directly optimizes compression under a new recursive inference procedure. ToaST greedily splits each pretoken into a full binary tree using precomputed byte n-gram counts, independent of any vocabulary. Given a vocabulary, inference recursively descends each split tree and emits the first in-vocabulary node reached on each path. Vocabulary selection is formulated as an Integer Program (IP) that minimizes the t...

---

### 11. Self-Policy Distillation via Capability-Selective Subspace Projection

**Authors:** Guangya Hao, Yitong Shang, Yunbo Long, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22675v1)

**Summary:** Self-distillation bootstraps large language models (LLMs) by training on their own generations. However, existing methods either rely on external signals to curate self-generated outputs (e.g., correctness filtering, execution feedback, and reward search), which are costly and unavailable for the best-performing frontier models, or skip curation entirely and train on all raw outputs, an approach that is often domain-specific and hard to generalize. Both also share a deeper weakness that self-gen...

---

### 12. Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora

**Authors:** Maciej Skorski

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22660v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22660v1)

**Summary:** Moral language is subtle and culturally variable, making it difficult to translate faithfully across languages. Idiomatic expressions, slang, and cultural references introduce hard-to-avoid translation artifacts. Yet automated moral values classification depends on language-specific annotated corpora that exist almost exclusively in English. We investigate whether LLM-based translation can bridge this gap, taking Polish as a test case. Using $\sim$50k morally-annotated social media posts from a ...

---

### 13. Seeing the Poem: Image-Semantic Detection of AI-Generated Modern Chinese Poetry with MLLMs

**Authors:** Shanshan Wang, Fengying Ye, Hanjia Lyu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22654v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22654v1)

**Summary:** Previous detection studies have shown that LLMs cannot be effectively used as detectors, but these studies have not addressed modern Chinese poetry. Moreover, no relevant research has explored the performance of LLMs in detecting modern Chinese poetry. This paper evaluates and enhances the performance of LLMs as detectors for modern Chinese poetry, and proposes an image-semantic guided poetry detection method. Compared with traditional detection approaches, our method innovatively incorporates i...

---

### 14. Whose Voice Counts? Mapping Stakeholder Perspectives on AI Through Public Submissions to the U.S. Government

**Authors:** Alina Karakanta, Alex Christiansen, Tomás Dodds, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22650v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22650v1)

**Summary:** As artificial intelligence (AI) systems become more common in our daily lives, it is important to understand how different stakeholders comprehend and envisage the role that these technologies play in shaping social, political, and economic realities. In this paper, we investigate public perceptions of AI based on a corpus of letters submitted during the public consultation for the Trump Administration's US AI Action Plan. To this aim, we release a corpus cleaning pipeline and perform topic mode...

---

### 15. Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety

**Authors:** Piercosma Bisconti, Matteo Prandi, Federico Pierucci, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22643v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22643v1)

**Summary:** Background. Traditional safety benchmarks for language models evaluate generated text: whether a model outputs toxic language, reproduces bias, or follows harmful instructions. When models are deployed as agents, the safety-relevant object shifts from what the system says to what it does within an environment, and evaluating model responses under prompting is no longer sufficient to address the safety challenges posed by artificial intelligence. Recent developments have seen the rise of benchmar...

---

### 16. More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts

**Authors:** Víctor Yeste, Paolo Rosso

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22641v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22641v1)

**Summary:** Detecting Schwartz values in political text is difficult because implicit cues often depend on surrounding arguments and fine-grained distinctions between neighboring values. We study when context and explicit moral knowledge help sentence-level value detection. Using the ValuesML/Touch{é} ValueEval format, we compare sentence, window, and full-document inputs; no-RAG and retrieval-augmented settings with a curated moral knowledge base; supervised DeBERTa-v3-base/large encoders; and zero-shot LL...

---

### 17. The Double Dilemma in Multi-Task Radiology Report Generation: A Gradient Dynamics Analysis and Solution

**Authors:** Erjian Zhang, Yatong Hao, Liejun Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22635v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22635v1)

**Summary:** While multi-task learning based automatic radiology report generation (RRG) is widely adopted to ensure clinical consistency, most focus on architectural designs yet remain limited to coarse linear scalarization strategies. These strategies cannot effectively balance the hard constraints of discriminative clinical supervision with the smoothness requirements of report generation. To address these problems, we analyze the failure mechanism of linear scalarization from the perspective of gradient ...

---

### 18. Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework

**Authors:** Shourov Joarder, Diganta Sikdar, Ahsan Habib Akash, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22620v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22620v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning ability of LLMs, but often depends on external supervision from human annotations or gold-standard solutions. Reinforcement learning from internal feedback (RLIF) has recently emerged as a scalable unsupervised alternative, using signals extracted from the model itself. However, existing RLIF methods typically rely on a single internal reward, which can lead to reward hacking, entropy collapse, and deg...

---

### 19. Chinese sensorimotor and embodiment norms for 3,000 lexicalized concepts

**Authors:** Jing Chen, Gábor Parti, Yin Zhong, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22616v1)

**Summary:** Understanding how conceptual knowledge is grounded in bodily experience, and to what extent machine systems can acquire such knowledge without direct sensorimotor experience, are central questions in both cognitive science and embodied artificial intelligence research. Large-scale normative resources are essential for investigating these questions empirically, yet such resources remain sparse for non-Indo-European languages. We present a novel normative database for 3,000 lexicalized concepts in...

---

### 20. Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

**Authors:** Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22608v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22608v1)

**Summary:** Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. This autonomy poses serious challenges for overseeing and assessing agent behavior. Most current tools are limited, focusing on observability with basic evaluation capabilities or imposing static, hand-crafted error taxonomies that cannot adapt to new domains. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. It pro...

---

### 21. A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models

**Authors:** Jiayi Fu, Yuxia Wang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22586v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22586v1)

**Summary:** This tutorial develops diffusion models from the viewpoint of differential equations. We begin with the conditional Gaussian forward process and show that this path admits both an ordinary differential equation (ODE) representation and a stochastic differential equation (SDE) representation. Averaging the conditional process over the data distribution then yields marginalized forward ODE and SDE formulations that transport the data distribution $p_0=p_{\mathrm{data}}$ to a Gaussian prior $p_1=\m...

---

### 22. Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion

**Authors:** Meimingwei Li, Yuanhao Ding, Esteban Garces Arias, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22579v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22579v1)

**Summary:** Recent work has identified a counterintuitive phenomenon termed "Hyperfitting", where fine-tuning Large Language Models (LLMs) to near-zero training loss on small datasets surprisingly enhances open-ended generation quality and mitigates repetition in greedy decoding. While effective, the underlying mechanism remains poorly understood, with the extremely low-entropy output distributions suggesting a potential equivalence to simple temperature scaling. In this work, we demonstrate that this pheno...

---

### 23. LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance

**Authors:** Yuchun Fan, Bei Li, Peiguang Li, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22567v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22567v1)

**Summary:** Reinforcement learning has proven effective for enhancing multi-step reasoning in large language models (LLMs), yet its benefits have not fully translated to multilingual contexts. Existing methods struggle with a fundamental trade-off: prioritizing input-language consistency severely hampers reasoning quality, while prioritizing reasoning often leads to unintended language drift toward English. We address this challenge with LANG, a novel framework that leverages language-conditioned hints to g...

---

### 24. SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations

**Authors:** Shuaiqi Wang, Aadyaa Maddi, Zinan Lin, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22564v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22564v1)

**Summary:** Today, tool-calling agents are commonly evaluated or tested on static datasets of execution traces, including input commands, agent responses, and associated tool calls. However, internal production datasets are often insufficient or unusable for testing; for example, they may contain sensitive or proprietary data, or they may be too sparse to support comprehensive testing (especially pre-deployment). In these settings, practitioners are increasingly replacing or augmenting real datasets with sy...

---

### 25. One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation

**Authors:** Yevhen Kostiuk, Kenneth Enevoldsen

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22544v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22544v1)

**Summary:** Instruction embedding models have become common among state-of-the-art models, however are evaluated using a single prompt per task. The single-point evaluation ignores a main problem of the instruction-based approach namely: sensitivity to the phrasing of the instruction. We present an empirical study of prompt sensitivity across 6 embedding models, 11 datasets, and 15 task-specific prompts per dataset, a total of 990. We show that reported scores misrepresent the distribution of scores over pl...

---

### 26. Scene Abstraction for Lexical Semantics: Structured Representations of Situated Meaning

**Authors:** Yejin Cho, Katrin Erk

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22542v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22542v1)

**Summary:** Coffee and tea share many properties, yet they evoke strikingly different situations, atmospheres, and affective associations. These situated dimensions of word meaning are real and systematic, but they remain implicit in most computational representations of lexical meaning. We propose Scene Abstraction, a framework for constructing structured representations of the interpretive scenes that words participate in across usage contexts. Each scene consists of a Contextual Scene (Events, Entities, ...

---

### 27. SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation

**Authors:** Xiaolong Zhou, Yifei Liu, Ziyang Gong, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22536v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22536v1)

**Summary:** Multimodal Large Language Models (MLLMs) have made rapid progress in spatial intelligence, yet existing spatial reasoning benchmarks largely assume pristine visual inputs and overlook the degradations that commonly occur in real-world deployment, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This raises a fundamental question: how robust is the spatial intelligence of current MLLMs when visual observations are imperfect? To answer this question, we ...

---

### 28. Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning

**Authors:** Zihan Liang, Yufei Ma, Ben Chen, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22511v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22511v1)

**Summary:** Post-training has become the dominant recipe for turning a language model into a competent search-augmented reasoning agent. A line of recent work pushes its performance further by adding elaborate machinery on top of this standard pipeline. These augmentations import external supervision from stronger external systems, attach auxiliary modules such as process reward models or retrospective critics, restructure the rollout itself with tree search or multi-stage curricula, or shape the reward wit...

---

### 29. Reflecti-Mate: A Conversational Agent for Adaptive Decision-Making Support Through System 1 and System 2 Thinking

**Authors:** Morita Tarvirdians, Senthil Chandrasegaran, Hayley Hung, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22509v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22509v1)

**Summary:** Making high-stakes personal decisions involves cognitive, emotional, and intuitive processes, and individuals differ in how they allocate attention across these modes. Integration of these processes has shown to benefit decision making. Yet, most current decision-support systems focus primarily on supporting cognitive aspects, rather than adapting to the individual's thinking profile to support integration of different types of thoughts. In this study, we investigate an agent designed to encoura...

---

### 30. BeLink: Biomedical Entity Linking Meets Generative Re-Ranking

**Authors:** Darya Shlyk, Stefano Montanelli, Lawrence Hunter

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22501v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22501v1)

**Summary:** Despite recent progress, Biomedical Entity Linking (BEL) with large language models (LLMs) remains computationally inefficient and challenging to deploy in practical settings. In this work, we demonstrate that instruction-tuning of open-source generative models can offer an effective solution when applied at the re-ranking stage of the BEL pipeline. We propose a set-wise instruction-tuning formulation that enables fast and accurate candidate selection. Our method demonstrates strong performance ...

---

### 31. Polite on the Surface, Wrong in Practice: A Curated Dataset for Fixing Honorific Failures in Multilingual Bangla Generation

**Authors:** Md. Asaduzzaman Shuvo, Mahedi Hasan, Md. Tashin Parvez, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22487v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22487v1)

**Summary:** Recent advances in Multilingual Large Language Models (MLLMs) have significantly enhanced cross-lingual conversational capabilities, yet modeling culturally nuanced and context-dependent communication remains a critical bottleneck. Specifically, existing state-of-the-art models exhibit a severe pragmatic gap when handling structural variations, regional idioms, and honorific consistencies in low-resource contexts like Bangla. To address this limitation, we introduce a novel, culturally aligned i...

---

### 32. Structured-Sparse Attention for Entity Tracking with Subquadratic Sequence Complexity

**Authors:** Hangyue Zhao, Paul Caillon, Erwan Fagnou, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22476v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22476v1)

**Summary:** Entity tracking requires maintaining and updating latent states for entities and attributes over long sequences. Recent task-specific attention operators can compress deep Transformer stacks into a few layers by performing multi-hop state propagation within a single layer, but their dense evaluation remains expensive. We show that in this setting, learned attention is strongly structured: most mass concentrates in local block-diagonal neighborhoods with a light cross-block residue. Exploiting th...

---

### 33. In Silico Modeling of the RAMPHO Buffer: Dissociating Informational and Energetic Masking via Phonetic Entropy in Deep Neural Networks

**Authors:** Stefan Bleeck

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22465v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22465v1)

**Summary:** The fundamental challenge of listening in multi-talker environments is a cognitive bottleneck, defined by the Ease of Language Understanding (ELU) model as a failure within the RAMPHO episodic buffer. Current deep neural networks for speech enhancement optimize purely for physical acoustics, failing to account for the cognitive penalty of informational masking. Here, we present an in silico simulation of the RAMPHO buffer using the frame-by-frame phonetic entropy of a self-supervised acoustic mo...

---

### 34. From Correlation to Cause: A Five-Stage Methodology for Feature Analysis in Transformer Language Models

**Authors:** Caleb Munigety

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22462v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22462v1)

**Summary:** We propose a five-stage methodology for causal feature analysis in transformer language models (probe design, feature extraction, causal validation, robustness testing, and deployment integration) and demonstrate it end-to-end on GPT-2 small performing the Indirect Object Identification (IOI) task. Activation patching recovers the canonical IOI circuit (layer-9 head 9 alone gives recovery +1.02). A sparse autoencoder recovers per-name selective features with effect sizes of 30 to 50 activation u...

---

### 35. Cohesion-6K: An Arabic Dataset for Analyzing Social Cohesion and Conflict in Online Discourse

**Authors:** Aisha Ali Al-Athba, Wajdi Zaghouani

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22447v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22447v1)

**Summary:** The study of online discourse has become central to understanding societal polarization. While much research has focused on detecting overt toxicity, the subtle dynamics of social cohesion, meaning the interaction between divisive and unifying narratives, remain computationally underexplored (Bail, 2021; Gonzalez-Bailon and Lelkes, 2023). This paper presents Cohesion-6K, a manually and ChatGPT-assisted annotated dataset of six thousand Arabic public Facebook posts related to the Israeli Occupati...

---

### 36. Assisted Counterspeech Writing at the Crossroads of Hate Speech and Misinformation

**Authors:** Genoveffa Martone, Helena Bonaldi, Marco Guerini

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22435v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22435v1)

**Summary:** Hate speech and misinformation frequently co-occur online, amplifying prejudice and polarization. Given their scale, using Large Language Models (LLMs) to assist expert counterspeech (CS) writing has gained interest, yet prior work has addressed these phenomena separately. We bridge this gap by studying CS generation in contexts where both hate and misinformation co-occur. We test three knowledge-driven generation strategies: first we prompt an LLM with fact-checkers' guidelines and fact-checkin...

---

### 37. DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

**Authors:** Jianing Yin, Tan Tang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22411v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22411v1)

**Summary:** Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query. This workflow leaves downstream answerers to denoise retrieved candidates and reconstru...

---

### 38. Epicure: Navigating the Emergent Geometry of Food Ingredient Embeddings

**Authors:** Jakub Radzikowski, Josef Chen

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22391v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22391v1)

**Summary:** We present Epicure, a family of three sibling skip-gram ingredient embeddings retrained from scratch on a multilingual recipe corpus. We aggregate 4.14M recipes from 11 sources spanning seven languages, English, Chinese, Russian, Vietnamese, Spanish, Turkish, Indonesian, German, and Indian-English, and normalise the raw ingredient strings to 1,790 canonical entries via an LLM-augmented pipeline. A 203,508-edge ingredient-ingredient NPMI graph and an 80,019-edge typed FlavorDB ingredient-compound...

---

### 39. Unified Data Selection for LLM Reasoning

**Authors:** Xiaoyuan Li, Yubo Ma, Chengpeng Li, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22389v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22389v1)

**Summary:** Effectively training Large Language Models (LLMs) for complex, long-CoT reasoning is often bottlenecked by the need for massive high-quality reasoning data. Existing methods are either computationally expensive or fail to reliably distinguish high- from low-quality reasoning samples. To address this, we propose High-Entropy Sum (HES), a training-free metric that quantifies reasoning quality by summing only the entropy of the top (e.g., 0.5\%) highest-entropy tokens in each reasoning sample. We v...

---

### 40. Multi-Stage Training for Abusive Comment Detection in Indic Languages

**Authors:** Pranshu Rastogi, Madhav Mathur, Ramaneswaran S, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22380v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22380v1)

**Summary:** In recent years social media has become an increasingly popular tool for communication. People use it to share their ideas, exchange information, and discuss thoughts. Given its prevalence and widespread reach, social media must remain a safe space for people. Content generated on social media can be abusive and it has become increasingly important to detect such content. In this paper, we use a language-based preprocessing and an ensemble of several models and analyze their performance of abusi...

---

### 41. Boundary-targeted Membership Inference Attacks on Safety Classifiers

**Authors:** Anthony Hughes, Alexander Goldberg, Prince Jha, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22373v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22373v1)

**Summary:** Safety classifiers are essential safeguards within generative AI systems, filtering harmful content or identifying at-risk users when interacting with large language models. Despite their necessity, these models are trained on sensitive datasets including discussions of self-harm and mental health, raising important, yet poorly understood, privacy concerns. Membership inference attacks (MIAs) allow adversaries to infer membership of examples used to train models. In this work, we hypothesize tha...

---

### 42. Modeling Pathology-Like Behavioral Patterns in Language Models Through Behavioral Fine-Tuning

**Authors:** Nicola Milano, Davide Marocco

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22356v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22356v1)

**Summary:** Large language models are increasingly used as computational tools for modeling human-like behavior. We introduce a behavioral induction framework that modifies model policies through fine-tuning on structured decision-making tasks: using synthetic datasets inspired by maladaptive behavioral patterns, including depression and paranoia, we train transformer-based language models to consistently select specific classes of actions across diverse contexts. We then test whether this behavioral optimi...

---

### 43. TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation

**Authors:** Hanyu Guo, Jiedong Yang, Chao Chen, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22355v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22355v1)

**Summary:** Public transit route planning traditionally depends on structured map infrastructure and complex routing engines, and no existing dataset supports training models to bypass this dependency. We present TransitLM, a large-scale dataset of over 13 million transit route planning records from four Chinese cities covering 120,845 stations and 13,666 lines, released as a continual pre-training corpus and benchmark data for three evaluation tasks with complementary metrics. Experiments show that an LLM ...

---

### 44. Pattern-and-root inflectional morphology: the Arabic broken plural

**Authors:** Alexis Amid Neme, Eric Laporte

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22310v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22310v1)

**Summary:** We present a substantially implemented model of description of the inflectional morphology of Arabic nouns, with special attention to the management of dictionaries and other language resources by Arabic-speaking linguists. The breakthrough lies in the reversal of the traditional root-and-pattern Semitic model into pattern-and-root, giving precedence to patterns over roots. Our model includes broken plurals (BPs), i.e. plurals formed by modifying the stem. It is based on the traditional notions ...

---

### 45. Harder to Defend: Towards Chinese Toxicity Attacks via Implicit Enhancement and Obfuscation Rewriting

**Authors:** Jingyi Kang, Junyu Lu, Bo Xu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22258v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22258v1)

**Summary:** Large language models (LLMs) require robust toxicity evaluation beyond explicit wording. This setting remains underexplored in Chinese, where toxicity may combine semantic indirectness with surface obfuscation. We introduce Chinese Implicit Toxicity Attack (CITA), a controlled red-team evaluation and defense-data generation framework, not a deployable evasion tool. CITA uses three stages: (i) Harmful Intent Learning, (ii) Implicit Toxicity Enhancement, and (iii) Obfuscation Variant Rewriting, to...

---

### 46. IdioLink: Retrieving Meaning Beyond Words Across Idiomatic and Literal Expressions

**Authors:** Kai Golan Hashiloni, Daniel Fadlon, Lior Livyatan, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22247v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22247v1)

**Summary:** Idioms pose a fundamental challenge for language models, as their meaning cannot be inferred from surface form alone. Understanding such expressions, therefore, requires semantic abstraction beyond lexical overlap. We introduce IdioLink, a retrieval benchmark designed to test whether models can link idiomatic expressions to conceptually equivalent meanings expressed in literal or paraphrased forms. IdioLink comprises 10,700 documents and 2,140 queries, spanning 107 idioms with both literal and f...

---

### 47. GHI: Graphormer over Conditioned Hypergraph Incidence for Aspect-Based Sentiment Analysis

**Authors:** Yu Du, Wenlong Zhu, Xingze Li, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22228v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22228v1)

**Summary:** Aspect-based sentiment analysis (ABSA) requires models to bind sentiment evidence to the correct aspect, making it a natural testbed for fine-grained structural reasoning. We introduce GHI, a Graphormer-over-Conditioned-Hypergraph-Incidence framework that is designed as an incidence-based structural reasoning layer built on a bipartite topology. GHI represents diverse linguistic and semantic evidence as token--hyperedge incidence relations, allowing different structural signals to be incorporate...

---

### 48. Survive or Collapse: The Asymmetric Roles of Data Gating and Reward Grounding in Self-Play RL

**Authors:** Sophia Xiao Pu, Zhaotian Weng, Chengzhi Liu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22217v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22217v1)

**Summary:** Self-play reinforcement learning trains language models on their own generated tasks, co-evolving a proposer and solver without human labels. Recent systems report strong reasoning gains, but collapse and instability are widely observed and poorly understood. The dominant response treats this as a reward-design problem. We argue instead that self-play stability is governed by two distinct levers: a data-level gate that decides which proposer-generated tasks enter the training pool, and the rewar...

---

### 49. Audience Engagement with Arabic Women's Social Empowerment and Wellbeing: A Decadal Corpus

**Authors:** Wajdi Zaghouani, Mabrouka Bessghaier, MD. Rafiul Biswas, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22204v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22204v1)

**Summary:** This paper presents the Arabic Women and Society Corpus, a ten year collection of 252,487 public Arabic Facebook posts related to women's empowerment and social wellbeing. The corpus was collected from 51,660 pages across 77 countries between 2013 and 2024, resulting in more than 267 million user interactions. Each post includes engagement metrics such as shares, comments, and emotional reactions, providing a unique view of audience sentiment and social attention. The data were processed using a...

---

### 50. Evaluation of Chunking Strategies for Effective Text Embedding in Low-Resource Language on Agricultural Documents

**Authors:** Sovandara Chhoun, Pichdara Po, Sereiwathna Ros, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22203v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22203v1)

**Summary:** In this study, we compare the performance of four text chunking approaches: Recursive, Khmer-Aware, Sentence-Based, and LLM-Based within a Retrieval-Augmented Generation (RAG) framework applied to Khmer agricultural documents. The document chunks are encoded using the BGE-M3 multilingual embedding model and retrieved using the FAISS library. Performance is evaluated using four metrics: Average Retrieval Score (L2 distance), Answer Relevance, Khmer Coverage, and Khmer Intersection over Union, all...

---

## cs.CV

**50 papers**

### 1. Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs

**Authors:** Jongseo Lee, Hyuntak Lee, Sunghun Kim, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22823v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22823v1)

**Summary:** Video Large Language Models (Video-LLMs) have made rapid progress on temporal video understanding, yet many fail at a basic perceptual primitive: signed image-plane motion direction. On simple videos of a single object moving left, right, up, or down, most Video-LLMs perform near chance, with above-chance cases largely attributable to prediction biases rather than genuine direction understanding. We call this failure directional motion blindness. We localize the failure by tracing motion directi...

---

### 2. Cambrian-P: Pose-Grounded Video Understanding

**Authors:** Jihan Yang, Zifan Zhao, Xichen Pan, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22819v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22819v1)

**Summary:** Camera pose matters. The position and orientation of each viewpoint define a shared spatial coordinate frame that relates observations across video frames. Yet this signal is largely absent from multimodal LLMs (MLLMs) for video understanding, which process frames as isolated 2D snapshots, instead of the persistent scene humans perceive. We revisit pose as a lightweight supervisory signal and introduce Cambrian-P, a video MLLM augmented with per-frame learnable camera tokens and a pose regressio...

---

### 3. MotiMotion: Motion-Controlled Video Generation with Visual Reasoning

**Authors:** Lee Hsin-Ying, Hanwen Jiang, Yiqun Mei, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22818v1)

**Summary:** Current motion-controlled image-to-video generation models rigidly follow user-provided trajectories that are often sparse, imprecise, and causally incomplete. Such reliance often yields unnatural or implausible outcomes, especially by missing secondary causal consequences. To address this, we introduce MotiMotion, a novel framework that reformulates motion control as a reasoning-then-generation problem. To encourage causally grounded and commonsense-consistent interactions, we leverage a traini...

---

### 4. AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation

**Authors:** Wenxuan Guo, Xiuwei Xu, Yichen Liu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22816v1)

**Summary:** Vision-and-Language Navigation (VLN) requires an agent to ground language instructions to its own movement within a visual environment. While state-of-the-art methods leverage the reasoning capabilities of Vision-Language Models (VLMs) for end-to-end action prediction, they often lack an explicit and explainable understanding of the relationships between the agent, the instruction, and the scene. Conversely, explicitly building a scene map for heuristic planning is intuitively appealing but reli...

---

### 5. GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations

**Authors:** Wenxuan Guo, Ziyuan Li, Meng Zhang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22812v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22812v1)

**Summary:** Vision-Language-Action (VLA) models have shown strong potential for general-purpose robot manipulation by unifying perception and action. However, existing VLA systems primarily rely on textual instructions and struggle to resolve spatial ambiguity in complex scenes with multiple similar objects. To address this limitation, we introduce gesture as a parallel instruction modality and propose a Gesture-aware Vision-Language-Action model (GesVLA). Our approach encodes gesture features directly into...

---

### 6. Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving

**Authors:** Jiahao Wang, Bo Sun, Yijing Bai, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22809v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22809v1)

**Summary:** Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild vide...

---

### 7. DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders

**Authors:** Tianhang Wang, Yitong Chen, Wei Song, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22777v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22777v1)

**Summary:** Representation Autoencoders (RAEs) leverage frozen vision foundation models (VFMs) as tokenizer encoders, providing robust high-level representations that facilitate fast convergence and high-quality generation in latent diffusion models. However, freezing the VFM inherently constrains its spatial reconstruction capacity, limiting fine-grained generation and image editing; in contrast, incorporating reconstruction-oriented signals via fine-tuning disrupts the pretrained semantic space and degrad...

---

### 8. Synthetic Data Alone is Enough? Rethinking Data Scarcity in Pediatric Rare Disease Recognition

**Authors:** Ganlin Feng, Yuxi Long, Erin Lou, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22767v1)

**Summary:** Children with rare genetic diseases often exhibit distinctive facial phenotypes, yet developing computer vision systems for early diagnosis remains challenging due to extreme data scarcity, privacy constraints, and limited data sharing in pediatric settings. These challenges not only hinder automated diagnosis but also restrict the availability of visual resources for clinical genetic counseling. While prior work has shown that synthetic data can augment real datasets and preserve phenotype-leve...

---

### 9. Spectral Tail Auxiliary Learning for AI-Generated Image Detection

**Authors:** Xingyi Li, Jiahui Zhang, Yiheng Li, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22751v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22751v1)

**Summary:** As generative image models evolve rapidly, the perceptual gap between generated and real images continues to narrow, making AI-generated image detection increasingly challenging. Many existing methods exploit frequency-domain cues for detection, typically described as frequency-domain artifacts or high-frequency discrepancies. However, the specific and recurring spectral regularities remain insufficiently understood and characterized. In this paper, we systematically analyze the one-dimensional ...

---

### 10. WorldKV: Efficient World Memory with World Retrieval and Compression

**Authors:** Jung Yi, Minjae Kim, Paul Hyunbin Cho, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22718v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22718v1)

**Summary:** Autoregressive video diffusion models have enabled real-time, action-conditioned world generation. However, sustaining a persistent world, where revisiting a previously seen viewpoint yields consistent content, remains an open problem. Full KV-cache attention preserves this consistency but breaks real-time constraints: memory footprint and attention cost grow linearly with rollout length. Sliding window inference restores throughput but discards long-term consistency. We propose WorldKV, a train...

---

### 11. AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild

**Authors:** Baiyu Chen, Zechen Li, Wilson Wongso, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22715v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22715v1)

**Summary:** As wearable and mobile devices become increasingly embedded in daily life, they offer a practical way to continuously sense human motion in the wild. But inertial signals are highly dependent on the sensing setup, including body location, mounting position, sensor orientation, device hardware, and sampling protocol. This setup dependence makes it difficult to learn motion representations that transfer across devices and datasets, and limits the broader use of wearable IMUs beyond closed-set reco...

---

### 12. Cross-Domain Human Action Recognition from Multiview Motion and Textual Descriptions

**Authors:** Yannick Porto, Renato Martins, Thomas Chalumeau, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22697v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22697v1)

**Summary:** Robustness to domain changes is a key capability for effective deployment of human action recognition systems in real-world scenarios, where action categories at inference can present important domain shifts or even unseen actions from training. In this context, improving the recognition capabilities of Zero-Shot Action Recognition models (ZSAR), without requiring strong annotation efforts, remains a central challenge. Most ZSAR approaches assume that actions are observed under geometric conditi...

---

### 13. Improving Viewpoint-Invariance and Temporal Consistency for Action Detection

**Authors:** Yannick Porto, Renato Martins, Thomas Chalumeau, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22695v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22695v1)

**Summary:** Viewpoint change invariance and action temporal consistency are critical aspects for the effective deployment of human action detection of untrimmed videos. Existing appearance-based video detection methods often struggle with limited viewpoint diversity during training, while motion-based detection approaches frequently fail to model fine-grained temporal relationships across consecutive motion windows. This paper introduces a novel two-stage action detection approach designed to improve both v...

---

### 14. Conceptualizing Embeddings: Sparse Disentanglement for Vision-Language Models

**Authors:** Piotr Kubaty, Patryk Marszałek, Łukasz Struski, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22679v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22679v1)

**Summary:** Vision-language models learn powerful multimodal embeddings, yet their internal semantics remain opaque. While sparse autoencoders (SAEs) can extract interpretable features, they rely on expanding the representation dimension, which compromises the original geometry and introduces redundancy. We introduce CEDAR (Conceptual Embedding Disentanglement via Adaptive Rotation), a post-hoc method that reveals the compositional structure of pretrained embeddings without increasing dimensionality. By lea...

---

### 15. Swift Sampling: Selecting Temporal Surprises via Taylor Series

**Authors:** Dahye Kim, Bhuvan Sachdeva, Karan Uppal, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22678v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22678v1)

**Summary:** While most frames in long-form video are redundant, the critical information resides in temporal surprises: moments where the actual visual features deviate from their predicted evolution. Inspired by the human brain's predictive coding, we introduce Swift Sampling, an elegant, training-free frame selection algorithm that automatically identifies high-information moments in a video. Specifically, we model a video as a differentiable trajectory in the visual latent space and compute the velocity ...

---

### 16. Slimmable ConvNeXt: Width-Adaptive Inference for Efficient Multi-Device Deployment

**Authors:** Janek Haberer, Jon Eike Wilhelm, Olaf Landsiedel

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22677v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22677v1)

**Summary:** Deploying vision models across devices with varying resource constraints, or even on a single device where available compute fluctuates due to battery state, thermal throttling, or latency deadlines, typically requires training and maintaining separate models. Width-adaptive inference addresses this by training a single set of shared weights containing multiple nested subnetworks of increasing capacity, but prior CNN-based approaches required switchable batch normalization, while recent scalable...

---

### 17. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

**Authors:** Bing Hu, Zaijing Li, Rui Shao, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22671v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22671v1)

**Summary:** Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propos...

---

### 18. SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers

**Authors:** Javad Rajabi, Kimia Shaban, Koorosh Roohi, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22668v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22668v1)

**Summary:** Diffusion transformers (DiTs) have emerged as a dominant architecture for text-to-image generation, yet their performance drops when generating at resolutions beyond their training range. Existing training-free approaches mitigate this by modifying inference-time attention behavior, often through Rotary Position Embeddings (RoPE) extrapolation combined with attention scaling. However, these strategies apply a uniform and content-agnostic scaling across RoPE components with distinct frequency cha...

---

### 19. SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation

**Authors:** Zhenyu Lu, Liupeng Li, Jinpeng Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22658v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22658v1)

**Summary:** While large language models provide strong compositional reasoning, existing reasoning segmentation pipelines fail to transparently connect this reasoning to visual perception. Current methods, such as latent query alignment, are end-to-end yet opaque "black boxes". Conversely, textual localization readout is merely readable, not truly interpretable, often functioning as an unconstrained post-hoc step. To bridge this interpretability gap, we propose SegCompass, an end-to-end model that leverages...

---

### 20. Seeing the Poem: Image-Semantic Detection of AI-Generated Modern Chinese Poetry with MLLMs

**Authors:** Shanshan Wang, Fengying Ye, Hanjia Lyu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22654v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22654v1)

**Summary:** Previous detection studies have shown that LLMs cannot be effectively used as detectors, but these studies have not addressed modern Chinese poetry. Moreover, no relevant research has explored the performance of LLMs in detecting modern Chinese poetry. This paper evaluates and enhances the performance of LLMs as detectors for modern Chinese poetry, and proposes an image-semantic guided poetry detection method. Compared with traditional detection approaches, our method innovatively incorporates i...

---

### 21. What Does the Caption Really Say? Counterfactual Phrase Intervention for Compositional Data Selection in Vision-Language Pretraining

**Authors:** Hyejin Go, Semi Lee, Hyesong Choi

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22651v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22651v1)

**Summary:** CLIP-style contrastive pretraining typically curates web-scale image-text pairs using sample-level filtering signals, often based on pair-level alignment. We show that this signal saturates: once coarse mismatches are removed, stricter global filtering no longer tracks the compositional supervision provided by the retained captions. The reason is structural - a global score conflates whether a pair is broadly plausible with whether the individual object, attribute, and relation phrases inside th...

---

### 22. From Baseline to Follow-Up: Counterfactual Spine DXA Image Synthesis in UK Biobank Using a Causal Hierarchical Variational Autoencoder

**Authors:** Yilin Zhang, Nicholas C. Harvey, Nicholas R. Fuggle, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22649v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22649v1)

**Summary:** Dual-energy X-ray absorptiometry (DXA) is widely used for large-scale skeletal assessment, yet learning controllable and interpretable factor-specific anatomical variation remains challenging. We propose a metadata-conditioned causal hierarchical variational autoencoder (CHVAE) for causally consistent generation of anteroposterior (AP) spine DXA images from the UK Biobank (UKB). The model is trained on 3,743 raw AP spine scans from the first imaging visit and conditioned on basic participant att...

---

### 23. The Double Dilemma in Multi-Task Radiology Report Generation: A Gradient Dynamics Analysis and Solution

**Authors:** Erjian Zhang, Yatong Hao, Liejun Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22635v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22635v1)

**Summary:** While multi-task learning based automatic radiology report generation (RRG) is widely adopted to ensure clinical consistency, most focus on architectural designs yet remain limited to coarse linear scalarization strategies. These strategies cannot effectively balance the hard constraints of discriminative clinical supervision with the smoothness requirements of report generation. To address these problems, we analyze the failure mechanism of linear scalarization from the perspective of gradient ...

---

### 24. AtomicMotion: Learning Human Motion From Different Human Parts

**Authors:** Runzhen Liu, Chuhua Xian, Fa-Ting Hong

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22631v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22631v1)

**Summary:** Accurately reconstructing full-body poses from sparse head and hand trajectories is a foundational challenge for immersive AR/VR telepresence. Current methods often struggle with error accumulation and unnatural joint coordination, primarily because they treat the human body as a monolithic entity, thereby failing to capture the fine-grained ``atomic intents'' embedded in subtle signal variations and overlooking the inherent structural topology. To bridge this gap, we present AtomicMotion, a fra...

---

### 25. H-Flow: Self-supervised Human Scene Flow via Physics-inspired Joint Multi-modal Learning

**Authors:** Zhanbo Huang, Xiaoming Liu, Yu Kong

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22629v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22629v1)

**Summary:** Parametric human models capture global pose but cannot represent the non-rigid surface dynamics of clothing and soft tissue. Generic scene flow estimates dense motion but breaks down on articulated bodies, where pixel-level supervision is also intractable to acquire. We introduce H-Flow, a dense human scene flow that captures both skeletal kinematics and surface deformation. A unified multi-head transformer estimates flow from monocular video, jointly predicting pose and depth as companion outpu...

---

### 26. GLeVE: Graph-Guided Lesion Grounding with Proposal Verification in 3D CT

**Authors:** Shuo Jiang, Yuhao Hong, Chunbo Jiang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22619v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22619v1)

**Summary:** Grounding radiology report descriptions to 3D CT volumes is essential for verifiable clinical interpretation, yet remains challenging due to the semantic-spatial gap between free-text narratives and volumetric anatomy. Existing report-assisted and vision-language grounding methods typically rely on phrase-level alignment or dense pixel supervision, resulting in limited lesion-wise correspondence and suboptimal localization accuracy. We propose GLeVE, a graph-guided lesion grounding framework wit...

---

### 27. Enhancing Gaze Reasoning in Vision Foundation Models for Gaze Following

**Authors:** Shijing Wang, Yaping Huang, Chaoqun Cui, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22607v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22607v1)

**Summary:** Gaze following requires both scene understanding and gaze reasoning to localize the gaze target of an in-scene person. Recently, vision foundation models (VFMs) have demonstrated strong performance on this task, enabling simpler architectures while outperforming prior methods. However, we observe a key limitation of VFM-based approaches: while VFMs substantially improve scene understanding, they contribute little to gaze reasoning. As a result, existing methods often rely on semantically salient...

---

### 28. Decoupling Ego-Motion from Target Dynamics via Dual-Interval Motion Cues for UAV Detection

**Authors:** Liuyang Wang, Feitian Zhang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22605v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22605v1)

**Summary:** Object detection from Unmanned Aerial Vehicles (UAVs) is challenged by severe ego-motion, camera jitter, and large scale variations. While modern detectors perform well on static images, their direct application to UAV video often fails, particularly for small objects in dynamic scenes. Existing motion-based methods either rely on computationally expensive optical flow or use single-interval differencing, which is sensitive to jitter and limited in capturing diverse motion patterns. We propose a...

---

### 29. Rethinking Noise-Robust Training for Frozen Vision Foundation Models: A Cross-Dataset Benchmark with a Case Study of Small-Loss Failure

**Authors:** Zitong Li, Haoyu Wang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22591v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22591v1)

**Summary:** Frozen Vision Foundation Models (VFMs) with lightweight classification heads are increasingly used in medical imaging because they offer efficient and reproducible deployment. Yet noisy-label learning methods for this frozen-feature regime remain poorly understood, and most existing methods still rely on a small-loss assumption inherited from end-to-end training. We present a controlled benchmark of eight noisy-label methods across five medical datasets, three backbones, two noise types, and fiv...

---

### 30. SceneAligner: 3D-Grounded Floorplan Localization in the Wild

**Authors:** Junhyeong Cho, Ruojin Cai, Hadar Averbuch-Elor

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22581v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22581v1)

**Summary:** Many public buildings provide floorplans with a "you are here" indicator to help visitors orient themselves. Floorplan localization seeks to computationally replicate this capability by determining where visual observations were captured within a floorplan. However, existing methods typically assume controlled small-scale environments and precise vectorized floorplans, limiting their ability to operate in large-scale buildings and rasterized floorplans. In this work, we present an approach for p...

---

### 31. Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping

**Authors:** Chouaib Bencheikh Lehocine, Adam Lilja, Junsheng Fu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22578v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22578v1)

**Summary:** Online map estimation is a crucial component of autonomous driving systems that reduces the reliance on costly high-definition maps. State-of-the-art (SOTA) methods commonly predict map elements as ordered sequences of points that form polylines and polygons. The evaluation of these methods relies predominantly on mean average precision (mAP) based on thresholded Chamfer distance (CD). This framework lacks sensitivity to point ordering and provides limited granularity in assessing geometric qual...

---

### 32. SegGuidedNet: Sub-Region-Aware Attention Supervision for Interpretable Brain Tumor Segmentation

**Authors:** Hasaan Maqsood, Saif Ur Rehman Khan, Sebastian Vollmer, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22572v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22572v1)

**Summary:** Accurate segmentation of brain tumour sub-regions from multi-parametric MRI is critical for treatment planning yet remains challenging due to morphological variability, class imbalance, and overlapping appearances of tumour regions across imaging sequences. We propose SegGuidedNet, a three-dimensional residual encoder--decoder network introducing a novel SegAttentionGate module that explicitly supervises the decoder to produce spatially discriminative attention maps for each tumour sub-region ne...

---

### 33. VGenST-Bench: A Benchmark for Spatio-Temporal Reasoning via Active Video Synthesis

**Authors:** Jinho Park, Youbin Kim, Hogun Park, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22570v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22570v1)

**Summary:** Spatio-temporal reasoning is a core capability for Multimodal Large Language Models (MLLMs) operating in the real world. As such, evaluating it precisely has become an essential challenge. However, existing spatio-temporal reasoning benchmark datasets primarily rely on static image sets or passively curated video data, which limits the evaluation of fine-grained reasoning capabilities. In this paper, we introduce VGenST-Bench, a video benchmark that employs generative models to actively synthesi...

---

### 34. Cell Phantom Video Generation in Elliptical Fourier Descriptor Domain

**Authors:** Francesco Benedetto, Roberto Basla, Luca Magri, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22563v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22563v1)

**Summary:** Training Deep Neural Networks for tracking individual cells in biomedical videos requires a large amount of annotated data. The annotation of videos for cell tracking is very time consuming and often requires domain expertise; this explains the limited availability of public annotated data to address important medical problems like tissue repair or cancer treatment. Generating synthetic videos along with their Ground Truth annotations is a promising solution that relies, as a foundational first ...

---

### 35. GeoWeaver: Grounding Visual Tokens with Geometric Evidence before Scene Reasoning

**Authors:** Deshui Miao, Xingsen Huang, Yameng Gu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22558v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22558v1)

**Summary:** Spatio-temporal reasoning in vision-language models requires visual representations that preserve physical geometry rather than merely semantic appearance. Recent multimodal models incorporate geometric information through structural branches, 3D-aware supervision, reasoning-stage fusion, or long-horizon memory. While these approaches demonstrate the importance of geometry for spatial intelligence, they typically treat geometric cues as a shared signal across all visual tokens. We note that this...

---

### 36. FashionLens: Toward Versatile Fashion Image Retrieval via Task-Adaptive Learning

**Authors:** Haokun Wen, Xuemeng Song, Xinghao Xie, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22552v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22552v1)

**Summary:** Fashion image retrieval is a cornerstone of modern e-commerce systems. A unified framework that supports diverse query formats and search intentions is highly desired in practice. However, existing approaches focus on narrow retrieval tasks and do not fully capture such diversity. Therefore, in this work, we aim to develop a unified framework capable of handling diverse realistic fashion retrieval scenarios, achieving truly versatile fashion image retrieval. To establish a data foundation, we fi...

---

### 37. MOTOR: A Multimodal Dataset for Two-Wheeler Rider Behavior Understanding

**Authors:** Varun A. Paturkar, Shankar Gangisetty, C. V. Jawahar

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22550v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22550v1)

**Summary:** Two-wheelers account for a disproportionately high share of road fatalities in the Global South. Research on two-wheeler rider behavior, however, lags far behind four-wheelers, where multimodal datasets have driven major advances in Advanced Driver Assistance Systems (ADAS). To address this gap, we present the MOtorized TwO-wheeler Rider (MOTOR) dataset, the first large-scale, multi-view, multimodal resource dedicated to two-wheelers in dense, unstructured traffic. MOTOR comprises 1,629 sequence...

---

### 38. Case-Aware Medical Image Classification with Multimodal Knowledge Graphs and Reliability-Guided Refinement

**Authors:** Yiming Xu, Yixuan Liu, Yuhang Zhang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22547v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22547v1)

**Summary:** Deep learning has brought significant progress to medical image classification, yet most existing methods still rely on isolated visual evidence and cannot effectively leverage similar cases or external knowledge. In clinical practice, diagnosis is typically supported by historical similar cases and their associated symptoms. To simulate this diagnostic process, we propose a framework that performs case-aware reasoning using multimodal knowledge graphs for explainable medical image diagnosis. Gi...

---

### 39. Segment Anything with Motion, Geometry, and Semantic Adaptation for Complex Nonlinear Visual Object Tracking

**Authors:** Deyi Zhu, Yuji Wang, Yong Liu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22538v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22538v1)

**Summary:** Traditional visual object tracking (VOT) methods typically rely on task-specific supervised training, limiting their generalization to unseen objects and challenging scenarios with distractors, occlusion, and nonlinear motion. Recent vision foundation models, exemplified by SAM 2, learn strong video understanding priors from large-scale pretraining and offer a promising foundation for building more robust and generalizable trackers. However, directly applying SAM 2 to VOT remains suboptimal, as ...

---

### 40. SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation

**Authors:** Xiaolong Zhou, Yifei Liu, Ziyang Gong, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22536v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22536v1)

**Summary:** Multimodal Large Language Models (MLLMs) have made rapid progress in spatial intelligence, yet existing spatial reasoning benchmarks largely assume pristine visual inputs and overlook the degradations that commonly occur in real-world deployment, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This raises a fundamental question: how robust is the spatial intelligence of current MLLMs when visual observations are imperfect? To answer this question, we ...

---

### 41. LACO: Adaptive Latent Communication for Collaborative Driving

**Authors:** Tianhao Chen, Yuheng Wu, Dongman Lee

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22504v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22504v1)

**Summary:** Collaborative driving aims to improve safety and efficiency by enabling connected vehicles to coordinate under partial observability. Recent approaches have evolved from sharing visual features for perception to exchanging language-based reasoning through foundation models for behavioral coordination. Though communicating in language provides intuitive information, it introduces two challenges: high latency caused by autoregressive decoding and information loss caused by compressing rich interna...

---

### 42. Training-Free Fine-Grained Semantic Segmentations in Low Data Regimes: A FungiTastic Baseline

**Authors:** Sebastian Cavada, Francesco Pelosin, Lapo Faggi

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22492v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22492v1)

**Summary:** Fine-grained semantic segmentation requires both precise localization and discrimination between visually similar classes. In FungiTastic, this problem is further complicated by a long-tailed distribution and strong variation in image acquisition conditions. We propose a training-free two-stage framework that decouples segmentation from classification. SAM3 first produces class-agnostic mushroom masks using macro-taxonomic prompts, and DINOv3 then assigns fine-grained labels through prototype ma...

---

### 43. Supervised Classification Heads as Semantic Prototypes: Unlocking Vision-Language Alignment via Weight Recycling

**Authors:** David Méndez, Roberto Confalonieri, Natalia Díaz Rodríguez

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22484v1)

**Summary:** Vision-Language Models (VLMs) excel at tasks like zero-shot classification and cross-modal retrieval by mapping images and text to a shared space, but this requires expensive end-to-end training with massive paired datasets. Current post-hoc alignment methods reduce computational costs by connecting pretrained encoders through lightweight mappings, yet still demand substantial paired data. In this work, we investigate the potential of repurposing the classification heads of pretrained vision mod...

---

### 44. Matching with Deliberation: Test-Time Evolutionary Hierarchical Multi-Agents for Zero-Shot Compositional Image Retrieval

**Authors:** Xingtian Pei, Yukun Song, Changwei Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22478v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22478v1)

**Summary:** Zero-Shot Compositional Image Retrieval (ZS-CIR) requires both preserving the visual continuity of the reference image and faithfully executing the semantic variables specified in the modification text, which constitutes the core challenge of the task. Existing methods often suffer from Perception Myopia in a single space, or fall into Logic Drift in iterative collaboration due to the perception ceiling of the underlying retriever. To address this issue, we propose a one-stop hierarchical Percep...

---

### 45. MaSC: A Masked Similarity Metric for Evaluating Concept-Driven Generation

**Authors:** Patryk Bartkowiak, Lennart Petersen, Bartosz Kotrys, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22469v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22469v1)

**Summary:** Evaluating single-concept personalization in text-to-image diffusion requires measuring both concept preservation, which captures identity fidelity to a reference, and prompt following, which captures whether the generated scene matches the prompt. Existing metrics commonly compute these signals using global image or text-image embeddings, such as CLIP-I, DINO, and CLIP-T. We show that such metrics correlate poorly with human perception because they attend to the image as a whole instead of sepa...

---

### 46. SADGE: Structure and Appearance Domain Gap Estimation of Synthetic and Real Data

**Authors:** Patryk Bartkowiak, Bartosz Kotrys, Dominik Michels, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22467v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22467v1)

**Summary:** We propose SADGE, a quantitative similarity metric that predicts the performance of synthetic image datasets for common computer vision tasks without downstream model training. Estimating whether a synthetic dataset will lead to a model that performs well on real-world data remains a bottleneck in model development. Existing evaluation metrics (e.g., PSNR, FID, CLIP) primarily measure semantic alignment between real and synthetic images (Appearance Similarity Score). Less commonly, structural si...

---

### 47. Making the Discrete Continuous: Synthetic RAW Augmentations for Fine-Grained Evaluation of Person Detection Performance in Low Light

**Authors:** Valeria Pais, Malena Mendilaharzu, Daniele Faccio, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22455v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22455v1)

**Summary:** Real-world deployment of AI vision models is both fueled and limited by the data available for training and testing. Real datasets are sparse and uneven: long-tailed or unbalanced distributions hinder generalization, and the low number of samples in low density regions makes it hard to run evaluations. Synthetic data can fill these gaps, providing us with a way to sample the input space more continuously and improve data coverage for benchmarks. Focusing on the autonomous driving safety-critical...

---

### 48. Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts

**Authors:** Zhen Sun, Yongjian Guo, Haoran Sun, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22446v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22446v1)

**Summary:** While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity ass...

---

### 49. Time-varying rPPG signal separation via block-sparse signal model

**Authors:** Kosuke Kurihara, Yoshihiro Maeda, Daisuke Sugimura, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22425v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22425v1)

**Summary:** Remote photoplethysmography (rPPG) enables non-contact measurement of cardiac pulse signals by analyzing subtle color changes in facial videos. Nevertheless, extracting rPPG signals remains challenging because of their extremely weak signal strength and susceptibility to illumination noise. In this paper, we propose an rPPG signal extraction method that exploits the quasi-periodic characteristics of rPPG signals. Our approach models quasi-periodicity of the rPPG signal, which arises from the sta...

---

### 50. Moment-Reenacting: Inverse Motion Degradation with Cross-shutter Guidance

**Authors:** Ji Xiang, Lin Guixu, Yin Zhengwei, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22423v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22423v1)

**Summary:** Motion degradation, manifested as blur in global shutter (GS) images or rolling shutter (RS) distortion in RS counterparts, remains a fundamental challenge in computational imaging, especially under fast motion or low-light conditions. While prior works have treated blur decomposition and RS temporal super-resolution as separate tasks, this separation fails to exploit their intrinsic complementarity. In this paper, we propose a unified framework to invert motion degradation and reenact imaging m...

---

## cs.LG

**50 papers**

### 1. Tokenisation via Convex Relaxations

**Authors:** Jan Tempus, Philip Whittington, Craig W. Schmidt, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22821v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22821v1)

**Summary:** Tokenisation is an integral part of the current NLP pipeline. Current tokenisation algorithms such as BPE and Unigram are greedy algorithms -- they make locally optimal decisions without considering the resulting vocabulary as a whole. We instead formulate tokeniser construction as a linear program and solve it using convex optimisation tools, yielding a new algorithm we call ConvexTok. We find ConvexTok consistently improves intrinsic tokenisation metrics and the bits-per-byte (BpB) achieved by...

---

### 2. Integrable Elasticity via Neural Demand Potentials

**Authors:** Carlos Heredia, Daniel Roncel

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22820v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22820v1)

**Summary:** We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing elasticities to be derived exactly from the learned demand surface. On the Dominick's beer dataset, ICDN improves out-of-sample generalization over a directed log-log benchmark and yields more stable, economically plausible elasticity estimates, especially for weakly identified ...

---

### 3. Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22817v1)

**Summary:** Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po...

---

### 4. Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration

**Authors:** Lily Goli, Justin Kerr, Daniele Reda, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22814v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22814v1)

**Summary:** Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotte...

---

### 5. The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning

**Authors:** Vishal Rajput

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22800v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22800v1)

**Summary:** Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching p...

---

### 6. Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models

**Authors:** Krishnakumar Balasubramanian

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22795v1)

**Summary:** We propose and analyze a conservative drifting method for one-step generative modeling. The method replaces the original displacement-based drifting velocity by a kernel density estimator (KDE)-gradient velocity, namely the difference of the kernel-smoothed data score and the kernel-smoothed model score. This velocity is a gradient field, addressing the non-conservatism issue identified for general displacement-based drifting fields. We prove continuous-time finite-particle convergence bounds fo...

---

### 7. MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

**Authors:** Qianshu Cai, Yonggang Zhang, Xianzhang Jia, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22794v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22794v1)

**Summary:** Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artif...

---

### 8. LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

**Authors:** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22786v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22786v1)

**Summary:** Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque c...

---

### 9. FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection

**Authors:** Huanchi Wang, Zihang Huang, Yifang Tian, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22779v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22779v1)

**Summary:** Production systems generate millions of log lines daily, yet most anomaly detectors operate at the session or window-level, flagging groups of lines rather than identifying the specific message responsible. This coarse granularity forces operators to inspect many routine lines per alert. Message-level detection offers finer granularity, but remains challenging. A single event template may correspond to both normal and anomalous messages, failures arise from heterogeneous subsystems, and line-lev...

---

### 10. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis

**Authors:** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22776v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22776v1)

**Summary:** Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed...

---

### 11. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data

**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22775v1)

**Summary:** Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated flight deck assistance, yet two challenges persist: handling frequent data missingness from blinks and tracking failures, and efficiently modeling long-range temporal dependencies. We propose MambaGaze, a framework that addresses these challenges through 1) XMD encoding, which augments raw features ...

---

### 12. CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation

**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22774v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22774v1)

**Summary:** Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundation models pre-trained on millions of clinical recordings offer rich representations, but cannot be directly applied to wearable devices due to sensor configuration mismatch and task differences. In this paper, we propose CogAdapt, a framework that adapts clinical ECG foundation models to wearable cog...

---

### 13. Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation

**Authors:** Samson Gourevitch, Yazid Janati, Dario Shariatian, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22765v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22765v1)

**Summary:** Discrete diffusion models are often trained through clean-data prediction, but the prediction can be used in different ways to define the reverse dynamics. In Masked Diffusion Models (MDM) these choices largely coincide, whereas in Uniform Diffusion Models (UDM) they do not. We show that the standard plug-in bridge parameterization for UDM is not optimized by the denoising posterior, but by a leave-one-out posterior that predicts each clean token without using its own noisy observation. This ide...

---

### 14. Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees

**Authors:** Christian Janos Lebeda, David Erb, Tudor Cebere, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22756v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22756v1)

**Summary:** Random forests are widely used in fields involving sensitive tabular data, but existing approaches to enforcing differential privacy (DP) typically degrade performance to the point of impracticality. In this paper, we introduce Lumberjack, a differentially private random forest algorithm that achieves substantially higher utility by constructing large random decision trees and then applying aggressive, privacy-preserving pruning to retain only sufficiently populated nodes. A key component of our...

---

### 15. Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization

**Authors:** Adis Alihodžić, Eva Tuba, Milan Tuba

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22749v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22749v1)

**Summary:** Modern smart grids rely on dense measurement infrastructures, communication links, and intelligent field devices. Although this improves supervision and control, it also increases vulnerability to cyber-physical disruptions. Operators must distinguish physical incidents, such as faults or line disturbances, from malicious actions, such as false data injection or unauthorized command execution. This chapter investigates this problem using the well-known MSU/ORNL Power System Attack Dataset. The p...

---

### 16. Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning

**Authors:** Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22748v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22748v1)

**Summary:** Autonomous systems have achieved superhuman performance in isolation or simulation, yet they remain brittle in shared, dynamic real-world spaces. This failure stems from the dominant single-agent paradigm for physical applications, where other actors are ignored or treated as environmental noise, preventing effective coordination. Here we show that multi-agent reinforcement learning provides the essential safety scaffolding required for real-world interaction. Using high-speed quadrotor racing a...

---

### 17. Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier

**Authors:** Berk Hayta, Hannah Laus, Simon Mittermaier, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22746v1)

**Summary:** Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are predicted by a learned neural network mapping. However, this approach can lead to computational challenges, as Dirichlet expected objectives are more complex than standard supervised learning losses, ...

---

### 18. SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation

**Authors:** Javad Parsa, Enis Simsar, Amir Joudaki, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22743v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22743v1)

**Summary:** Parameter-efficient fine-tuning enables fast personalization of text-to-image diffusion models, but composing multiple custom concepts remains challenging due to representation interference. Existing modular methods either rely on expensive post-hoc fusion or freeze adaptation subspaces, which limit expressiveness and concept fidelity. To address this trade-off, we propose Sequential regularized LoRA (SeqLoRA), a constrained continual learning framework that jointly optimizes both LoRA factors v...

---

### 19. Ternary Decision Trees with Locally-Adaptive Uncertainty Zones

**Authors:** William Smits

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22740v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22740v1)

**Summary:** Decision trees partition the feature space using hard binary thresholds, assigning identical confidence to instances far from a decision boundary and to those directly on it. We introduce ternary decision trees, which augment each split node with an uncertainty zone of half-width delta centered on the optimal threshold. Instances in this zone receive predictions formed by weighted blending of both child subtrees and are flagged as boundary-uncertain, signaling that downstream applications may tr...

---

### 20. Proxy-Based Approximation of Shapley and Banzhaf Interactions

**Authors:** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22738v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22738v1)

**Summary:** Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed and accuracy. To overcome this limitation, we introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction. On a theoretical level, we derive a polynomial-time generalization of interventional TreeSHAP t...

---

### 21. The Distillation Game: Adaptive Attacks & Efficient Defenses

**Authors:** Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22737v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22737v1)

**Summary:** Distillation attacks create a deployment trade-off for model providers: the same outputs that make a model more useful can also make it easier to imitate. We study this trade-off through a minimax game between a utility-constrained teacher and an adaptive student. Our framework yields tractable one-sided response rules: an adaptive evaluation rule in which the student reweights high-value examples, and a teacher-side defense template that suppresses outputs most useful for distillation. From a c...

---

### 22. Optimization over the intersection of manifolds

**Authors:** Yan Yang, Bin Gao, Ya-xiang Yuan

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22736v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22736v1)

**Summary:** Optimization over the intersection of two manifolds arises in a broad range of applications, but is hindered by the coupled geometry of the feasible region. In this paper, we prove that the regularities -- clean intersection and intrinsic transversality -- are equivalent, which yields a tractable projection onto the tangent space of the intersection. Therefore, we propose a geometric method that employs a retraction on only one manifold and updates the iterate along two orthogonal directions. Sp...

---

### 23. Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation

**Authors:** Dong Nie

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22731v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22731v1)

**Summary:** Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed through their loss functions: maximum likelihood, policy gradients, forward KL, reverse KL, or related objective-level variants. We study a complementary factor: the state distribution on which supervision is applied. For an autoregressive policy, a state is a prompt plus generated prefix. SFT trains on fixed dataset states, while RL and on-policy dist...

---

### 24. Multiple Neural Operators Achieve Near-Optimal Rates for Multi-Task Learning

**Authors:** Adrien Weihs, Hayden Schaeffer

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22724v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22724v1)

**Summary:** We study the approximation and statistical complexity of learning collections of operators in a shared multi-task setting, with a focus on the Multiple Neural Operators (MNO) architecture. For broad classes of Lipschitz multiple operator maps, we derive near-optimal upper bounds for approximation and statistical generalization. On the lower-bound side, we establish a curse of parametric complexity and prove corresponding minimax rates. Together, these results show that shared representations acr...

---

### 25. The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler

**Authors:** Md Sahil Akhtar, Aymane El Gadarri, Vivek F. Farias, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22723v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22723v1)

**Summary:** A central error measure in Gaussian DDPMs is the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. This quantity is especially relevant for procedures such as classifier guidance, which perturb the entire reverse trajectory rather than only the terminal sample. Prior analyses show that standard isotropic reverse covariances suffer an unavoidable $Ω(1/T)$ path-KL error as the number of denoising steps $T$ grows. We show that matching the full poste...

---

### 26. Reading Task Failure Off the Activations: A Sparse-Feature Audit of GPT-2 Small on Indirect Object Identification

**Authors:** Mahdi Nasermoghadasi

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22719v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22719v1)

**Summary:** We report a small, reproducible audit of which sparse-autoencoder (SAE) features of GPT-2 small fire differently on failed versus successful trials of the Indirect Object Identification (IOI) task. On 300 prompts, GPT-2 small reaches 79.7% accuracy; 146 of the 24,576 features in the layer-8 residual-stream SAE release of Bloom (2024) clear a Holm-corrected significance threshold and 105 reach a large effect size (|Cohen's d| > 0.8). The strongest single correlate of failure -- feature 17,491, d=...

---

### 27. Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators

**Authors:** Zachary Novack, Stephen Brade, Haven Kim, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22717v1)

**Summary:** Interactive streaming music generation promises the use of generative models for live performance and co-creation that is impossible with offline models. However, SOTA models exist in the discrete-AR regime, requiring industrial levels of compute for both training and inference. In this work, we investigate whether audio diffusion models, with their wide support in the open-source community but non-streaming bidirectional nature, can be repurposed efficiently into interactive models accessible o...

---

### 28. AMEL: Accumulated Message Effects on LLM Judgments

**Authors:** Sid-ali Temkit

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22714v1)

**Summary:** Large language models are routinely used as automated evaluators: to review code, moderate content, or score outputs, often with many items passing through one conversation. We ask whether the polarity of prior conversation history biases subsequent judgments, an effect we call the accumulated message effect on LLM judgments (AMEL). Across 75,898 API calls to 11 models from 4 providers (OpenAI, Anthropic, Google, and four open-source models), we present identical test items in isolation or follo...

---

### 29. Abstraction for Offline Goal-Conditioned Reinforcement Learning

**Authors:** Clarisse Wibault, Alexander Goldie, Antonio Villares, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22711v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22711v1)

**Summary:** Markov Decision Processes (MDPs) often exhibit significant redundancy due to symmetries and shared structure across state-goal pairs in real-world Goal-Conditioned Reinforcement Learning (GCRL). While hierarchical policies have been motivated for horizon reduction via temporal abstraction in offline GCRL, we demonstrate that hierarchy also enables absolute abstraction. By introducing relativised options as well as distinct representations for different levels of the hierarchy, we demonstrate how...

---

### 30. Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary Signals

**Authors:** Shuo Yang, Jinda Lu, Chiyu Ma, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22703v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22703v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a central paradigm for scaling LLM reasoning, yet its optimization often suffers from training instability and suboptimal convergence. Through a systematic dissection of clipping-based GRPO-style objectives, we identify the rigid clipping decision induced by hard clipping as a key practical bottleneck in the studied RLVR setups. Specifically, our analysis suggests that informative signals can lie in the near-boundary region jus...

---

### 31. Posterior Collapse as Automatic Spectral Pruning

**Authors:** Johannes Hirn

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22691v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22691v1)

**Summary:** We show that posterior collapse in $β$-VAEs implements automatic spectral pruning. A latent mode collapses if its contribution to reconstruction is below the cutoff set by $β$. Equilibrium solutions with different $β$ thus reveal a cascade of collapses as latent modes decouple from least to most useful.   We derive this as a consequence of the loss via a Landau stability analysis. We define a latent-rescaling-invariant order parameter that ranks active latent modes and whose collapse thresholds ...

---

### 32. ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification

**Authors:** José Alberto Rodríguez, Luis Balderas, Miguel Lastra, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22684v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22684v1)

**Summary:** Time Series Foundation Models (TSFMs) have become a new component of the state-of-the-art in general time series forecasting. However, adapting them to specialized classification tasks remains constrained by two interconnected challenges: the quadratic cost of standard attention mechanisms and the inability to disentangle the structural components underlying time series variability. This technical report introduces ChronoVAE-HOPE, a next-generation TSFM that reconciles massive generalization wit...

---

### 33. Conceptualizing Embeddings: Sparse Disentanglement for Vision-Language Models

**Authors:** Piotr Kubaty, Patryk Marszałek, Łukasz Struski, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22679v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22679v1)

**Summary:** Vision-language models learn powerful multimodal embeddings, yet their internal semantics remain opaque. While sparse autoencoders (SAEs) can extract interpretable features, they rely on expanding the representation dimension, which compromises the original geometry and introduces redundancy. We introduce CEDAR (Conceptual Embedding Disentanglement via Adaptive Rotation), a post-hoc method that reveals the compositional structure of pretrained embeddings without increasing dimensionality. By lea...

---

### 34. Holographic functions and neural networks

**Authors:** Balazs Szegedy

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22666v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22666v1)

**Summary:** A fuzzy Boolean function is a map $f:\cube^n\to [0,1]$, where $n\in\mathbb N$. We introduce and compare three ways of saying that such a function has bounded complexity. The first is a sampling property: the value $f(x)$ can be recovered, up to small error and with high probability, from the values of a bounded number of randomly chosen coordinates of $x$. We call this the holographic property. The second is a structural property: $f$ is uniformly close to a bounded-degree polynomial in boundedl...

---

### 35. SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation

**Authors:** Zhenyu Lu, Liupeng Li, Jinpeng Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22658v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22658v1)

**Summary:** While large language models provide strong compositional reasoning, existing reasoning segmentation pipelines fail to transparently connect this reasoning to visual perception. Current methods, such as latent query alignment, are end-to-end yet opaque "black boxes". Conversely, textual localization readout is merely readable, not truly interpretable, often functioning as an unconstrained post-hoc step. To bridge this interpretability gap, we propose SegCompass, an end-to-end model that leverages...

---

### 36. The Secretary Problem with a Stochastic Precursor

**Authors:** Franziska Eberle, Alexander Lindermayr

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22653v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22653v1)

**Summary:** In learning-augmented online algorithms, predictions are usually valued for what they say: a value estimate, a solution, or an algorithmic recommendation. This paper shows that predictions can also be valuable solely due to their arrival time. We study the fundamental secretary problem augmented with a stochastic precursor: a content-free signal that is guaranteed to arrive no later than the best item, but is otherwise stochastically timed. The signal does not carry any additional information; n...

---

### 37. From Baseline to Follow-Up: Counterfactual Spine DXA Image Synthesis in UK Biobank Using a Causal Hierarchical Variational Autoencoder

**Authors:** Yilin Zhang, Nicholas C. Harvey, Nicholas R. Fuggle, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22649v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22649v1)

**Summary:** Dual-energy X-ray absorptiometry (DXA) is widely used for large-scale skeletal assessment, yet learning controllable and interpretable factor-specific anatomical variation remains challenging. We propose a metadata-conditioned causal hierarchical variational autoencoder (CHVAE) for causally consistent generation of anteroposterior (AP) spine DXA images from the UK Biobank (UKB). The model is trained on 3,743 raw AP spine scans from the first imaging visit and conditioned on basic participant att...

---

### 38. Why SGD is not Brownian Motion: A New Perspective on Stochastic Dynamics

**Authors:** Igor Ignashin, Anna Radovskaya, Andrew Semenov, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22644v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22644v1)

**Summary:** Stochastic Gradient Descent (SGD) is commonly modeled as a Langevin process, assuming that minibatch noise acts as Brownian motion. However, this approximation relies on a continuous-time limit and a sqrt(eta) noise scaling that does not match the discrete SGD update at finite learning rate. In this work, we propose an alternative formulation of SGD as deterministic dynamics in a fluctuating loss landscape induced by minibatch sampling. Starting directly from the discrete update, we derive a mas...

---

### 39. More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts

**Authors:** Víctor Yeste, Paolo Rosso

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22641v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22641v1)

**Summary:** Detecting Schwartz values in political text is difficult because implicit cues often depend on surrounding arguments and fine-grained distinctions between neighboring values. We study when context and explicit moral knowledge help sentence-level value detection. Using the ValuesML/Touch{é} ValueEval format, we compare sentence, window, and full-document inputs; no-RAG and retrieval-augmented settings with a curated moral knowledge base; supervised DeBERTa-v3-base/large encoders; and zero-shot LL...

---

### 40. The Double Dilemma in Multi-Task Radiology Report Generation: A Gradient Dynamics Analysis and Solution

**Authors:** Erjian Zhang, Yatong Hao, Liejun Wang, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22635v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22635v1)

**Summary:** While multi-task learning based automatic radiology report generation (RRG) is widely adopted to ensure clinical consistency, most focus on architectural designs yet remain limited to coarse linear scalarization strategies. These strategies cannot effectively balance the hard constraints of discriminative clinical supervision with the smoothness requirements of report generation. To address these problems, we analyze the failure mechanism of linear scalarization from the perspective of gradient ...

---

### 41. A note on convergence of Wasserstein policy optimization

**Authors:** David Šiška, Yufei Zhang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22622v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22622v1)

**Summary:** Wasserstein Policy Optimization (WPO) is a recently proposed reinforcement learning algorithm that leverages Wasserstein gradient flows to optimize stochastic policies in continuous action spaces. Despite its empirical success, the theoretical convergence properties of WPO in environments with continuous state and action spaces have yet to be fully established. In this note, we argue that WPO within the framework of entropy-regularised Markov Decision Processes converges linearly. This is done b...

---

### 42. UNAD+: An Explainable Hybrid Framework for Unknown Network Attack Detection

**Authors:** Saif Alzubi, Frederic Stahl

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22621v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22621v1)

**Summary:** The detection of previously unseen network attacks remains a major challenge for intrusion detection systems. Although supervised learning methods often perform well on known attack classes, they are limited when new attack types are not represented in the training data. Unsupervised methods are more suitable for detecting zero-day attacks, as they do not require labelled attack samples, but they often suffer from high false positive rates, which limits their real-world usefulness. This paper pr...

---

### 43. Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework

**Authors:** Shourov Joarder, Diganta Sikdar, Ahsan Habib Akash, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22620v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22620v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning ability of LLMs, but often depends on external supervision from human annotations or gold-standard solutions. Reinforcement learning from internal feedback (RLIF) has recently emerged as a scalable unsupervised alternative, using signals extracted from the model itself. However, existing RLIF methods typically rely on a single internal reward, which can lead to reward hacking, entropy collapse, and deg...

---

### 44. Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery

**Authors:** Halil Alperen Gozeten, Xuechen Zhang, Emrullah Ildiz, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22613v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22613v1)

**Summary:** Recent LLM-guided evolutionary search methods have shown that iterative program mutation can discover strong algorithms, but they typically optimize each task independently, even when related tasks share reusable structure. We introduce Evolutionary Multi-Task Optimization (EMO) for LLM-guided program discovery, and propose EMO-STA (Shared-Then-Adapt), a two-stage framework that first evolves a shared archive of executable programs across a task family and then adapts selected shared candidates ...

---

### 45. Healthcare LLM Benchmarks Are Only as Good as Their Explicit Assumptions

**Authors:** Naveen Raman, Santiago Cortes-Gomez, Mateo Dulce Rubio, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22612v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22612v1)

**Summary:** Benchmarks are necessary for healthcare evaluation, but are not sufficient for predicting deployment performance. Our position is that the evaluation--deployment gap arises not because of poorly designed benchmarks, but from implicit assumptions about how users interact with models that cannot be surfaced from benchmarks alone. To make this precise, we propose a classification of assumptions into two categories: task, which can be tested from conversation data alone, and outcome, which requires ...

---

### 46. Benchmarking Machine Learning Architectures for Antimicrobial Stewardship in Pediatric ICUs

**Authors:** Niklas Raehse, Luregn J. Schlapbach, Daphné Chopard

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22611v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22611v1)

**Summary:** Antimicrobial stewardship (AMS) is critical in pediatric intensive care units (PICUs), where diagnostic uncertainty often drives broad-spectrum antibiotic use, increasing antimicrobial resistance and potential long-term harms. Machine learning offers a promising approach for identifying patient-level opportunities for stewardship interventions from electronic health record data, yet prior work has focused largely on adult populations and static tabular representations. We present a systematic be...

---

### 47. Innovations in Cardless Artificial Intelligence Banking: A Comprehensive Framework for Cyber Secure and Fraud Mitigation using Machine Learning Algorithms

**Authors:** Md Israfeel

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22604v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22604v1)

**Summary:** The advent of cardless artificial intelligence (AI) banking heralds a paradigm shift in the financial landscape, offering users unprecedented security and convenience. This paper outlines a comprehensive framework designed to enhance cybersecurity, introduce auto-generated virtual cards, and mitigate fraud risks within cardless AI banking systems. The framework envisions a future banking architecture that employs AI-powered data cryptography to create secure virtual cards for seamless transactio...

---

### 48. MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy

**Authors:** Jiaxu Wang, Junhao He, Jingkai Sun, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22597v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22597v1)

**Summary:** Learning real-world dynamics from visual observations is crucial for various domains. A common strategy is to calibrate simulators by estimating physical parameters, yet accuracy is ultimately bounded by the underlying physical models, which often assume materials are homogeneous and isotropic. Even if reasonable, real-world objects typically exhibit mild anisotropy and heterogeneity. After the near-isotropic backbone is well calibrated, these residual effects become the key bottleneck for furth...

---

### 49. Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network

**Authors:** Sayan Mitra, Ege Yuceel, Noah Giles, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22596v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22596v1)

**Summary:** Robotic tasks are typically specified by a tuple of factors, such as the object to be grasped, the obstacles to be avoided, the color of the target, and so on. Collecting expert demonstrations for every combination of factor values grows combinatorially. We present factored diffusion policies: a single shared diffusion network trained with per-factor null-token dropout, whose score decomposes additively across factors at inference. Under approximate conditional independence between factors given...

---

### 50. Do Deep Ensembles Actually Capture Uncertainty in Graph Neural Networks?

**Authors:** Pedro C. Vieira, Pedro Ribeiro, Viacheslav Borovitskiy

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22593v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22593v1)

**Summary:** While deep ensembles are widely considered to be the default method for uncertainty quantification in deep learning, their effectiveness for graph-structured data is often simply assumed based on successes in domains like computer vision. We investigate standard deep ensembles specifically for message-passing graph neural networks. Benchmarking across seven datasets representing varied tasks and complexities, we reveal that ensembles provide surprisingly little improvement over a single model. I...

---

## cs.NE

**50 papers**

### 1. Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22817v1)

**Summary:** Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po...

---

### 2. Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection

**Authors:** Giancarlo P. Gamberi, Calebe P. Bianchini

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22527v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22527v1)

**Summary:** Negative Selection Algorithms (NSAs), inspired by the self/non-self discrimination mechanism of the human immune system, have been widely employed in anomaly detection. However, their effectiveness is often constrained by the efficiency of detector generation. This paper presents the Quantum Genetic Negative Selection Algorithm (QGNSA), a novel approach that integrates a Quantum Genetic Algorithm (QGA) into the EvoSeedRNSA algorithm, replacing its classical evolutionary optimization process. The...

---

### 3. Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology

**Authors:** Nils Leutenegger

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22401v1)

**Summary:** Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus pres...

---

### 4. Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions

**Authors:** Gabriel Kronberger, Fabricio Olivetti de Franca, Deaglan J. Bartlett, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22374v1)

**Summary:** Symbolic regression with genetic programming (GPSR) may suffer from overfitting and structural bloat, especially when noise is present. In this paper we evaluate description length (DL) and fractional Bayes factor (FBF) criteria as principled, data-efficient alternatives to heuristics for selecting compact expressions that generalise well. We implement DL using a Fisher-information-based parameter encoding and compare it to AIC and BIC across multiple datasets, including noisy synthetic benchmar...

---

### 5. Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture

**Authors:** Joy Bose

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22206v1)

**Summary:** The Thousand Brains Theory (TBT) and its open-source Monty framework model object recognition through sensorimotor inference -- identifying objects by actively moving a sensor across their surface and building evidence contact by contact. The current implementation encodes each contact as a dense floating-point vector. While Monty tracks inter-step displacement and accumulates evidence across contacts, it treats the feature activation pattern at each contact as an unordered set - the directional...

---

### 6. Exact Uniform L1 Spacing for Solow-Polasky Diversity on Lines and Ordered Pareto Fronts

**Authors:** Michael T. M. Emmerich, Mahboubeh Nezhadmoghaddam, Jesús Guillermo Falcón Cardona

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21922v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21922v1)

**Summary:** We study fixed-cardinality maximization of the inverse-matrix Solow--Polasky diversity, equivalently finite metric magnitude for the exponential kernel, on one-dimensional and ordered metric sets. The analysis starts from the known finite-line gap formula for the exponential kernel, which writes the excess inverse-matrix diversity as a sum of functions of consecutive gaps. Building on this formula, the main interval theorem proves that, for every $k\geq 2$, the unique maximizing $k$-point subset...

---

### 7. Engineering Hybrid Physics-Informed Neural Networks for Next-Generation Electricity Systems: A State-of-the-Art Review

**Authors:** Joseph Nyangon

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21903v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21903v1)

**Summary:** The integration of machine learning with domain-specific physics is transforming the design, monitoring, and control of electricity systems, where data scarcity, limited interpretability, and the need to enforce physical laws constrain purely data-driven models. Physics-informed machine learning (PIML) addresses these limitations by embedding governing equations directly into the learning process, yielding accurate, efficient, and scalable solutions for Industry 4.0 applications. This article re...

---

### 8. Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos

**Authors:** Lucas Fernandez Sarmiento

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21648v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21648v1)

**Summary:** We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos. Dropout shifts the perfect-alignment fixed point, making the depth scale for information propagation finite even at critical initialization. We derive critical and crossover scaling laws for correlation decay and establish that smooth activations and kinked, ReLU-like activations constitute distinct universality classes, with different critical exponents and a universal two-parameter ...

---

### 9. Approximation Theory for Neural Networks: Old and New

**Authors:** Soumendu Sundar Mukherjee, Himasish Talukdar

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21451v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21451v1)

**Summary:** Universal approximation theorems provide a mathematical explanation for the expressive power of neural networks. They assert that, under mild conditions on the activation function, feedforward neural networks are dense in broad function classes, such as continuous functions on compact subsets of $\mathbb{R}^d$, $L^p$ spaces, or Sobolev spaces. Over the past four decades, these qualitative universality results have evolved into a rich quantitative theory addressing approximation rates, parameter ...

---

### 10. How to Build Marcus's Algebraic Mind: Algebro-Deterministic Substrate over Galois Fields

**Authors:** Hiroyuki Chuma, Kanji Otsuk, Yoichi Sato

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21379v2) | 📄 [PDF](https://arxiv.org/pdf/2605.21379v2)

**Summary:** In The Algebraic Mind, Gary Marcus identified three components essential for any adequate cognitive architecture: operations over variables, recursively structured representations, and a distinction between mental representations of individuals and kinds. He argued that standard multilayer perceptrons supported none of these, acknowledging that a neural implementation using registers and treelets, constructed via developmental programs rather than gradient descent, remained a programmatic conjec...

---

### 11. Genetic Programming with Transformer-Based Mutation for Approximate Circuit Design

**Authors:** Ondrej Galeta, Lukas Sekanina

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21055v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21055v1)

**Summary:** A recent trend is to leverage machine learning models to improve the evolutionary design and optimization process. We propose a novel transformer-based mutation operator for Cartesian genetic programming (CGP) for the automated design of approximate arithmetic circuits. We introduce a hybrid scheme for CGP in which the proposed mutation operator is switched with the standard mutation operator to prevent stagnation of the circuit approximation process. We also develop a new training scheme for th...

---

### 12. Convergence Analysis of Evolution Strategies for Mixed-Integer Optimization

**Authors:** Ryoki Hamano, Kento Uchida, Shinichi Shirakawa

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21000v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21000v1)

**Summary:** Mixed-integer extensions of evolution strategies (ES) that discretize selected coordinates of sampled continuous vectors often impose a lower bound on the standard deviation of integer variables to prevent premature convergence. While these methods show promising empirical results, this handling can slow the convergence of continuous variables, and its impact has lacked a clear theoretical account. In this paper, we provide a convergence analysis of evolution strategies for mixed-integer optimiz...

---

### 13. Privacy-Preserving Distributed Optimization Under Time Constraints Using Secure Multi-Party Computation and Evolutionary Algorithms

**Authors:** Sebastian Gruber, Tobias Harzfeld, Christoph G. Schuetz, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20944v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20944v1)

**Summary:** In distributed optimization, multiple parties collaborate to find an optimal solution to a problem. Privacy-preserving distributed optimization uses techniques, such as secure multi-party computation (MPC), to protect the private inputs of each party. In time-critical settings, the runtime overhead introduced by privacy-preserving computations may prevent the optimization from finishing within the deadline. This paper presents an approach for privacy-preserving distributed optimization in time-c...

---

### 14. E-ReCON: An Energy- and Resource-Efficient Precision-Configurable Sparse nvCIM Macro for Conventional and Spiking Neural Edge Inference

**Authors:** Ankit Kumar Tenwar, Mukul Lokhande, Santosh Kumar Vishvakarma

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20717v1)

**Summary:** This work presents E-ReCON, a 16 Kb energy and resource-efficient digital compute-in-memory (DCIM) macro based on a compact 3T1R ReRAM bitcell for edge-AI inference. The proposed bitcell occupies only 0.85 um^2 and supports reliable AND-based in-memory multiplication for both conventional convolutional neural network (CNN) and spiking neural network (SNN) workloads. To reduce accumulation overhead, a novel interleaved 10T/28T adder tree is introduced, reducing transistor count and power consumpt...

---

### 15. Weight Decay Regimes in Grokking Transformers: Cheap Online Diagnostics

**Authors:** Lucky Verma

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20441v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20441v1)

**Summary:** Transformers trained on modular arithmetic exhibit sharp transitions between memorization, generalization, and collapse. We show that weight decay acts as a scalar empirical control parameter for these regimes, and introduce two cheap online diagnostics, mean pairwise attention-head cosine similarity and entropy standard deviation, that track training dynamics from attention activations alone and complement loss-landscape diagnostics at lower compute cost. Across eleven experimental conditions a...

---

### 16. What Do Evolutionary Coding Agents Evolve?

**Authors:** Nico Pelleriti, Sree Harsha Nelaturu, Zhanke Zhou, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20086v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20086v1)

**Summary:** Recent work pairs LLMs with evolutionary search to iteratively generate, modify, and select code using task-specific feedback. These systems have produced strong results in mathematical discovery and algorithm design, yet a fundamental question remains: what do they actually evolve? Progress is typically summarized by the best score a run reaches under a task-specific evaluator, but that score can reflect several different mechanisms: new algorithmic structure, re-tuning an existing strategy, re...

---

### 17. Training Neural Networks with Optimal Double-Bayesian Learning

**Authors:** Vy Bui, Hang Yu, Karthik Kantipudi, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20009v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20009v1)

**Summary:** Backpropagation with gradient descent is a common optimization strategy employed by most neural network architectures in machine learning. However, finding optimal hyperparameters to guide training has proven challenging. While it is widely acknowledged that selecting appropriate parameters is crucial for avoiding overfitting and achieving unbiased outcomes, this choice remains largely based on empirical experiments and experience. This paper presents a new probabilistic framework for the learni...

---

### 18. Reconfigurable Nonlinear Photonic Networks for In-Situ Learning and Memory Formation via Driven-Dissipative Dynamics

**Authors:** Isaac Yorke

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19911v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19911v1)

**Summary:** Photonic neuromorphic computing offers a promising route to overcoming the limitations of conventional von Neumann architectures by exploiting the high bandwidth, low latency, and massive parallelism of optical systems. However, most existing implementations rely on fixed dynamical substrates such as classic reservoir computing, where learning is restricted to external readout layers and memory is limited to transient fading effects. In this work, I propose a Reconfigurable Nonlinear Photonic De...

---

### 19. Multi-population Diversity-guided Genetic Algorithm for Feature Selection in Network Intrusion Detection

**Authors:** Chunzhen Li

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19864v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19864v1)

**Summary:** Network Intrusion Detection System is a critical means of ensuring cybersecurity. However, existing Genetic Algorithm-based feature selection methods face several limitations when dealing with high-dimensional redundant traffic features. For example, population diversity is difficult to maintain, and evolutionary operators lack guidance. To solve these problems, this study proposes the Multi-Population Diversity-Guided Genetic Algorithm (MPDGGA). First, we build a chained multi-population evolut...

---

### 20. optimize_anything: A Universal API for Optimizing any Text Parameter

**Authors:** Lakshya A Agrawal, Donghyun Lee, Shangyin Tan, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19633v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19633v1)

**Summary:** Can a single LLM-based optimization system match specialized tools across fundamentally different domains? We show that when optimization problems are formulated as improving a text artifact evaluated by a scoring function, a single AI-based optimization system-supporting single-task search, multi-task search with cross-problem transfer, and generalization to unseen inputs-achieves state-of-the-art results across six diverse tasks. Our system discovers agent architectures that nearly triple Gemi...

---

### 21. Closed-form predictive coding via hierarchical Gaussian filters

**Authors:** Aleksandrs Baskakovs, Sylvain Estebe, Kenneth Enevoldsen, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20293v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20293v1)

**Summary:** Predictive coding (PC) offers a local and biologically grounded alternative to backpropagation in the training of artificial neural networks, yet to date, it remains slower, and performance degrades sharply as network depth increases. We trace both problems to a single simplification: current PC networks fix the precision matrix to the identity, discarding precision-weighted prediction errors that the variational derivation requires to be fast, local, and Bayesian. We close this gap by expressin...

---

### 22. Scalable, Energy-Efficient Optical-Neural Architecture for Multiplexed Deepfake Video Detection

**Authors:** Parnian Ghapandar Kashani, Shiqi Chen, Aydogan Ozcan

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19360v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19360v1)

**Summary:** The rapid proliferation of AI-generated visual media has created an urgent need for efficient, trustworthy deepfake detection systems. However, existing deep learning-based detection methods rely on computationally intensive and energy-demanding inference algorithms, limiting their scalability. Here, we present a hybrid digital-analog deepfake video detection framework that combines a lightweight digital front-end with a spatially multiplexed optical decoding back-end for massively parallel anal...

---

### 23. Information Processing Capacity of Stationary Physical Systems: Theory, Data-efficient Estimation Methods, and Photonic Demonstration

**Authors:** Rahul Uma Ramachandran, Serge Massar

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19152v2) | 📄 [PDF](https://arxiv.org/pdf/2605.19152v2)

**Summary:** Physical computing systems provide a promising route toward hardware-native machine learning, but their computational capabilities remain difficult to characterize in a principled, task-independent, and data-efficient way. We extend the Information Processing Capacity (IPC) framework to stationary physical computing systems and establish several fundamental results: individual capacities are bounded between zero and one, their sum over a complete basis is bounded by the number of readouts, and n...

---

### 24. GOAL: Graph-based Objective-Aligned Diffusion Solvers for Dynamic Multi-Objective Optimization

**Authors:** Xingyu Li

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19119v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19119v1)

**Summary:** Existing neural combinatorial optimization solvers frame solution search as imitation of optimal decisions, inherently limiting their utility to single-objective minimization and static constraints. We propose GOAL, a conditioned diffusion solver over relational graph representations that enables controllable decision generations by conditioning on human-specified objectives. We introduce a heterogeneous graph encoding in which distinct edge types, corresponding to different classes of constrain...

---

### 25. Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data

**Authors:** Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18557v1)

**Summary:** The brain learns abstract representations of high-dimensional sensory input, but the plasticity rules that enable such learning are unknown. We study biologically plausible algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to investigate how deep neural networks learn the intrinsic hierarchical structure of high-dimensional data. We focus on two types of local learning rules that avoid both a long convergence time and the use of a symmetric error network. The first t...

---

### 26. When Fireflies Cluster; Enhancing Automatic Clustering via Centroid-Guided Firefly Optimization

**Authors:** MKA Ariyaratne, Azwirman Gusrialdi, Yury Nikulin, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18460v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18460v1)

**Summary:** This work presents a novel variant of the Firefly Algorithm (FA) for data clustering, addressing limitations of traditional methods like K-Means that struggle with non-uniform cluster shapes, densities, and the need for pre-defining the number of clusters. The proposed algorithm introduces a centroid movement strategy and a multi-objective fitness function that balances compactness, separation, and a novel TSP-based navigation penalty. It automatically estimates the optimal number of clusters an...

---

### 27. Mapping the Fitness Landscape: A Structure-Guided Approach to Multi-Modal Optimization

**Authors:** Meng Xiang, Pei Yan

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18351v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18351v1)

**Summary:** Multimodal optimization requires finding many optima rather than merely keeping a diverse population. Yet most niching-based evolutionary algorithms rely on distances or density estimators without explicitly recovering the underlying peak--basin organization in the decision space, which can lead to pseudo-multimodality: many distinct individuals ultimately collapse into only a few basins. We introduce Chaotic Landscape-Decoding Evolution (CLDE), a decision-space-centric framework that turns mult...

---

### 28. Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in Spiking Neural Networks

**Authors:** Alessio Caviglia, Filippo Marostica, Alessandro Savino, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18003v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18003v1)

**Summary:** Deploying adaptive intelligence at the edge remains challenging due to the high computational and energy cost of training neural models. Spiking Neural Networks (SNNs) offer a promising alternative, but enabling on-device learning requires hardware-algorithm co-design. This paper presents SPIKER-LL, an FPGA-based SNN accelerator that extends the open-source Spiker+ inference architecture with efficient support for the STSF local learning rule. Through targeted microarchitectural extensions, SPIK...

---

### 29. Adaptive Stochastic Natural Gradient Method for Safe Optimization on Binary Space

**Authors:** Kento Uchida, Ryoki Hamano, Masahiro Nomura, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.17925v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17925v1)

**Summary:** Optimization problems in real-world applications across the medical and engineering domains often involve potential risks when evaluating candidate solutions. Safe optimization aims to perform optimization while suppressing unsafe solution evaluations in such situations. For continuous search spaces, there exist safe optimization methods based on evolutionary computation. However, the algorithm development of safe optimization methods for binary search spaces has not been adequately addressed. I...

---

### 30. Stability and Discretization Error of State Space Model Neural Operators

**Authors:** Abderrahim Bendahi, Adrien Fradin, Johan Peralez, et al.

**Published:** 2026-05-17

🔗 [Paper](http://arxiv.org/abs/2605.18905v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18905v1)

**Summary:** Neural operators have emerged as a powerful, discretization-invariant framework for solving partial differential equations (PDEs). Although established approaches like the Deep Operator Network (DeepONet) have successfully achieved universal approximation for operators, and architectures such as Fourier Neural Operators (FNOs) have shown algebraic convergence rates, a precise theoretical connection between the continuous theory and its discrete numerical implementation remains a challenge. Speci...

---

### 31. Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks: a computational account with clinical predictions

**Authors:** Esila Keskin

**Published:** 2026-05-17

🔗 [Paper](http://arxiv.org/abs/2605.17399v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17399v1)

**Summary:** Von Economo neurons (VENs) are selectively lost in behavioural-variant frontotemporal dementia (bvFTD) and reduced in autism spectrum conditions (ASC), yet their computational role in social learning remains unexplained. We train a spiking neural network (the VENCircuit) embedding VEN-like projection neurons (K=40, 2% of total) in a recurrent pyramidal circuit across 50 matched random initialisations with and without VENs. The network is trained on a controlled binary classification task; we mak...

---

### 32. Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets

**Authors:** Kamil Kashif, Robert Ślepaczuk

**Published:** 2026-05-17

🔗 [Paper](http://arxiv.org/abs/2605.17307v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17307v1)

**Summary:** This study develops and evaluates a deep reinforcement learning framework for dynamic portfolio allocation across global equity markets. The Soft Actor-Critic algorithm is used to learn continuous portfolio weights within a Markov Decision Process, incorporating transaction costs, turnover penalties, and diversification constraints into the reward function. Five model configurations are compared, varying in reward formulation, policy structure (flat versus hierarchical Dirichlet), portfolio cons...

---

### 33. Evolutionary Extreme Learning Machine of ab-initio Energy Landscapes for Crystal Structure Prediction using Manta Ray Optimization with Levy Flight

**Authors:** Adrian Rubio-Solis

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.17148v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17148v1)

**Summary:** The Manta Ray Foraging Optimization algorithm (MRFO) has proven to be a powerful heuristic strategy in the optimal solution of a large number of engineering problems. In this paper, an improvement of MRFO with Levy Flight is suggested for the training of extreme learning machines (ELMs) whose basic model is a Single Layer Feedforward Network (SLFN). The proposed methodology that we called Evolutionary EELM-MRFO-LF for short is implemented to the prediction of unrelaxed and relaxed formation ener...

---

### 34. Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip

**Authors:** Eric Oliveira Gomes, Damien Rontani

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.16114v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16114v1)

**Summary:** We propose a scalable neuromorphic architecture based on spiking dynamics emerging from the autonomous time-continuous evolution of clockless (asynchronous) digital circuits. Implemented on commercially available field-programmable gate arrays (FPGAs), our system implements networks of interacting Boolean spiking neurons with configurable excitatory and inhibitory synaptic weights. A complete processing pipeline enables efficient handling of spike-encoded data for solving machine-learning tasks....

---

### 35. MO-CAPO: Multi-Objective Cost-Aware Prompt Optimization

**Authors:** Jan Büssing, Moritz Schlager, Timo Heiß, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.18869v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18869v1)

**Summary:** Large language models (LLMs) achieve strong performance across a wide range of tasks but are highly sensitive to prompt design, motivating the need for automatic prompt optimization. Existing methods predominantly focus on performance alone, ignoring competing objectives such as inference cost or latency. At the same time, existing work on multi-objective prompt optimization relies on off-the-shelf NSGA-II, ignoring optimization efficiency. As a remedy, we introduce MO-CAPO, a novel multi-object...

---

### 36. Thermodynamic Networks: Harnessing Non-Equilibrium Steady States for Computation

**Authors:** Patryk Lipka-Bartosik, Gianmichele Blasi, Javier Lalueza Puértolas, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15985v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15985v1)

**Summary:** We introduce thermodynamic networks, a general framework for autonomous, physics-based computation using non-equilibrium steady states. These networks are modeled as a collection of finite-size reservoirs that exchange conserved quantities--such as electric charge or molecular number--while relaxing to a non-equilibrium steady state, which encodes the solution of a computational problem. We identify Negative Differential Conductance (NDC) as the critical physical property governing the computati...

---

### 37. Diversified Residual Symbolic Regression

**Authors:** Koki Ikeda, Masahiro Nomura, Ryoki Hamano

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15809v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15809v1)

**Summary:** Symbolic regression (SR) aims to discover explicit mathematical expressions that explain observed data and is widely used in domains where interpretability is essential. Because interpretability requires expressions to reflect meaningful regularities, SR is sensitive to observations that deviate from the dominant relationship. Such irregular observations, or outliers, are common in real-world data and can hinder SR from identifying underlying regularities. Robust regression mitigates this by dow...

---

### 38. Structure Abstraction and Generalization in a Hippocampal-Entorhinal Inspired World Model

**Authors:** Tianqiu Zhang, Muyang Lyu, Xiao Liu, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15733v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15733v1)

**Summary:** Humans abstract experiences into structured representations to facilitate pattern inference and knowledge transfer. While the hippocampal-entorhinal (HPC-MEC) circuit is known to represent both spatial and conceptual spaces, the mechanisms for concurrently extracting abstract structures from continuous, high-dimensional dynamics remain poorly understood. We propose a brain-inspired hierarchical model that simultaneously infers latent transitions and constructs a predictive visual world model. Ou...

---

### 39. General-Purpose Co-Evolutionary Construction of Parallel Algorithm Portfolios for Multi-Objective Binary Optimization

**Authors:** Zhiyuan Wang, Shengcai Liu, Shaofeng Zhang, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15729v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15729v1)

**Summary:** Despite recent progress in constructing generalizable parallel algorithm portfolios (PAPs), no general-purpose approach is yet available for multi-objective binary optimization problems (MOBOPs). To fill this gap, this paper proposes domain-agnostic co-evolution of parameterized search for multi-objective binary optimization~(DACMO), which features two technical innovations. First, we propose a neural instance representation architecture that decouples domain-invariant and instance-specific feat...

---

### 40. Bridging Silicon and the Hippocampus: Algebro-Deterministic Memory "VaCoAl" as a Substrate for Vector-HaSH and TEM

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15652v4) | 📄 [PDF](https://arxiv.org/pdf/2605.15652v4)

**Summary:** Vector-HaSH and the Tolman-Eichenbaum Machine (TEM) propose the hippocampal-entorhinal circuit factorizes memory via a grid-cell scaffold for compositional replay. Concurrently, human iEEG shows sharp-wave ripples gate recall and multi-hop replay fidelity decays multiplicatively. Yet, these fields lack a shared algebraic foundation. We introduce VaCoAl, an algebro-deterministic hyperdimensional memory architecture built on Galois-field linear-feedback shift registers. Its deterministic Galois-fi...

---

### 41. Towards Code-Oriented LM Embeddings for Surrogate-Assisted Neural Architecture Search

**Authors:** Pranav Somu, Advay Balakrishnan, Stepan Kravtsov, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15649v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15649v1)

**Summary:** Developing effective surrogates (performance predictors) for Neural Architecture Search (NAS) typically requires expensive fine-tuning or the engineering of complex representations. We propose a low-cost embedding strategy that leverages the inductive bias of Language Models (LMs) to eliminate these overheads. By representing architectures as PyTorch class definition text, we demonstrate that off-the-shelf LMs act as competitive feature extractors without NAS-specialized fine-tuning. The final p...

---

### 42. Perforated Neural Networks for Keyword Spotting

**Authors:** Vishy Gopal, Aris Ilias Goutis, Ralph Crewe, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15647v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15647v1)

**Summary:** Edge machine learning presents a unique set of constraints not encountered in cloud-scale model deployment: strict memory budgets, limited compute, and non-negotiable accuracy thresholds must all be satisfied simultaneously. Existing compression and optimization techniques can trade one resource for another, but rarely improve both accuracy and model size at the same time. This paper presents the application of Perforated Backpropagation to keyword spotting on the Edge Impulse platform, an exper...

---

### 43. On the Stability of Growth in Structural Plasticity

**Authors:** Lute Lillo, Nick Cheney

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.15435v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15435v1)

**Summary:** Standard deep-learning pipelines usually choose the network architecture before training and keep it fixed throughout optimization. In contrast, a model can also be adapted by editing its structure during training, for example by pruning existing hidden-neuron units or growing new ones. Although growth is appealing for adaptive and continual systems, we show that it is not simply the inverse of pruning. Pruning selects among units that have participated in training from the start, whereas growth...

---

### 44. NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework

**Authors:** Alessio Caviglia, Filippo Marostica, Roberta Bardini, et al.

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.15058v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15058v1)

**Summary:** The rapid expansion of spiking neural networks (SNNs) has led to a proliferation of training algorithms that differ widely in biological inspiration, computational structure, and hardware suitability. Despite this progress, the field lacks a unified, fine-grained taxonomy that systematically organizes these approaches and clarifies their conceptual relationships. This survey provides a comprehensive taxonomy of SNN training algorithms, spanning surrogate-gradient backpropagation, local and three...

---

### 45. First Mathematical Runtime Analyses of Multi-Objective Evolutionary Algorithms for Multi-Valued Decision Variables

**Authors:** Mingfeng Li, Zheng Cheng, Weijie Zheng, et al.

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14836v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14836v1)

**Summary:** Problems defined on binary decision spaces have been intensively studied in the theory of multi-objective evolutionary algorithms (MOEAs). In contrast, no mathematical runtime analyses exist so far for MOEAs dealing with decision variables that take a finite number $r > 2$ of values, despite the prevalence of such problems in practice. In this work, we begin to fill this research gap. We analyze how the classic SEMO algorithm with unit-strength local mutation computes the Pareto front of an $r$-...

---

### 46. An Amortized Efficiency Threshold for Comparing Neural and Heuristic Solvers in Combinatorial Optimization

**Authors:** Sohaib Afifi

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14624v2) | 📄 [PDF](https://arxiv.org/pdf/2605.14624v2)

**Summary:** A common critique of neural combinatorial-optimization solvers is that they are less energy-efficient than CPU metaheuristics, given the operational energy cost of training them on GPUs. This paper examines the inferential step from "training is expensive" to "neural solvers are net-inefficient", which is where the critique actually goes wrong. Training the network costs a large fixed amount of GPU energy; running the metaheuristic costs a small amount of CPU energy on every instance, repeated a...

---

### 47. Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning

**Authors:** Taebong Kim, Youngsik Hong, Minsik Kim, et al.

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14386v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14386v1)

**Summary:** We present Darwin Family, a framework for training-free evolutionary merging of large language models via gradient-free weight-space recombination. We ask whether frontier-level reasoning performance can be improved without additional training, by reorganizing latent capabilities already encoded in existing checkpoints. Darwin introduces three key ideas: (i) a 14-dimensional adaptive merge genome enabling fine-grained component- and block-level recombination; (ii) MRI-Trust Fusion, which adaptiv...

---

### 48. Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders

**Authors:** William Lehn-Schiøler, Magnus Ruud Kjær, Rahul Thapa, et al.

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13930v2) | 📄 [PDF](https://arxiv.org/pdf/2605.13930v2)

**Summary:** EEG foundation models achieve state-of-the-art clinical performance, yet the internal computations driving their predictions remain opaque: a barrier to clinical trust. We apply TopK Sparse Autoencoders (SAEs) across three architecturally distinct EEG transformers: SleepFM, REVE, and LaBraM to extract sparse feature dictionaries from their embeddings. By grounding these features in a clinical taxonomy (abnormality, age, sex, and medication), we benchmark monosemanticity and entanglement across a...

---

### 49. Dual-axis attribution of zebrafish tectal microcircuits for energy-efficient and robust neurocomputing

**Authors:** Ningping Li, Hao Zhang, Yi Zhou

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13924v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13924v1)

**Summary:** Biological neural circuits contain specialized substructures that support distinct computational functions, yet many bio-inspired neural networks borrow biological motifs without identifying their circuit-level origins. In this study, we investigate whether zebrafish tectal microcircuits can be attributed along two computational axes: energy-efficient information processing and robustness-preserving stabilization. We reconstruct a directed zebrafish-inspired retinotectal microcircuit graph and v...

---

### 50. Texture Regenerating and Grafting Using Genome-Driven Neural Cellular Automata

**Authors:** Mirela-Magdalena Catrina, Ioana Cristina Plajer, Alexandra Băicoianu

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13630v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13630v1)

**Summary:** This study significantly advances multi-texture synthesis using Neural Cellular Automata (NCAs) by introducing a novel training methodology that enables robust self-regeneration of textures in damaged regions. This inherent healing mechanism, essential for dynamic and adaptive systems, extends beyond traditional computer graphics applications, highlighting the fundamental self-organizing properties of NCAs. Furthermore, we present a versatile grafting technique, enabling the seamless combination...

---

## q-bio.NC

**50 papers**

### 1. Efficient coding under constraint drives neural systems towards criticality and sloppiness

**Authors:** He Xiao, Xinyue Zhao, Weikang Wang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22598v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22598v1)

**Summary:** It is widely accepted that the brain operates near a critical state, characterized by neural avalanches that follow power-law distributions. However, the functional rationale for why neural systems attain criticality remains unclear. Here, we present a theoretical framework that links efficient coding to criticality in neural populations. Using a Gaussian population coding model, we demonstrate that maximizing Fisher information under resource constraints naturally leads to the emergence of soft...

---

### 2. Learning sequence timing and control of replay speed in networks of spiking neurons

**Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22523v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22523v1)

**Summary:** Processing sequential inputs is a fundamental brain function, underlying tasks such as sensory perception, language, and motor control. A challenge in sequence processing is to represent not only the order of events, but also their precise timing. While existing computational models can learn sequential structure, many lack biologically plausible mechanisms to encode element-specific timing and to flexibly control the speed of sequence replay. The spiking Temporal Memory (sTM) model, a biologica...

---

### 3. Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology

**Authors:** Nils Leutenegger

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22401v1)

**Summary:** Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus pres...

---

### 4. A simple model of co-emergence of grid and place fields

**Authors:** Zhaoze Wang, Genela Morris, Dori Derdikman, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21356v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21356v1)

**Summary:** Grid cells in the medial entorhinal cortex and place cells in the hippocampus together support spatial navigation. The two regions are reciprocally connected, and there is a chicken-and-egg problem for how both arise and reinforce each other during development. Current computational accounts either derive one type from the other or use network dynamics to model the emergence of one type in isolation. We introduce a unified recurrent network model that instantiates Dale's Law (every neuron is eit...

---

### 5. Stimulus symmetries can confound representational similarity analyses

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21324v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21324v1)

**Summary:** What can representational similarity matrices (RSMs) tell us about a neural code? As the popularity of these summary statistics grows, so too does the need for a more complete characterization of their properties. Here, we show that symmetries in network inputs can confound RSM-based analyses. Stimulus symmetries render many representations functionally equivalent, but these different configurations can lead to different RSMs. These different RSMs reflect qualitatively different representational...

---

### 6. Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

**Authors:** Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20496v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20496v1)

**Summary:** The Strong Platonic Representation Hypothesis suggests that representational convergence in artificial neural networks can be harnessed constructively: embeddings can be translated across models through a universal latent space without paired data. We ask whether an analogous geometry can be recovered across human brains. Using fMRI data from the Natural Scenes Dataset, we propose a self-supervised encoder that learns subject-specific embeddings from brain data alone by exploiting repeated stimu...

---

### 7. Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment

**Authors:** Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20127v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20127v1)

**Summary:** Artificial vision models are often evaluated against the human visual cortex by measuring how accurately their internal representations predict brain responses. However, prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered. Here, we introduce a unified framework for evaluating both model-brain and brain-brain alignment by identifying the response dimensions recovered by prediction. Using repeated fMRI measurements, we first identify targ...

---

### 8. Performance of low vision individuals when selecting a target with head-pointing in virtual reality

**Authors:** Camille Bordeau, Célia Passerel, Ambre Denis-Noël, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19816v1)

**Summary:** Purpose: To investigate psychophysically the ability of low vision individuals with central visual field loss (CFL) to perform a visually-guided pointing task in a virtual reality environment. Methods: Patients with CFL (n=25, ages = 67-90 years) and normally-sighted controls (n=26, ages = 67-85 years) had to select a target (2{\textdegree} diameter dot) with a head-contingent cursor (6{\textdegree} diameter reticle).  Target selection occurred when target was validly pointed at for 1.5 seconds....

---

### 9. BCI-sift: An automated feature selection toolbox for Brain Computer Interface applications

**Authors:** Elena C Offenberg, Dirk Keller, Mariska J Vansteensel, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19646v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19646v1)

**Summary:** Advancements in clinical Brain-Computer Interfaces (BCIs) depend on precise and reliable signal interpretation. However, the high-dimensional and noisy nature of data captured from both implanted and non-implanted BCIs poses significant challenges, motivating the use of feature selection algorithms. We introduce BCI-sift (BCI Systematic and Interpretable Feature Tuning), a Python-based toolbox designed to streamline the application of diverse optimization algorithms to BCI datasets for identifyi...

---

### 10. Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay

**Authors:** Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19352v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19352v1)

**Summary:** Understanding how humans and artificial intelligence systems predict and plan by interacting with their environment is a fundamental challenge at the intersection of neuroscience and machine learning. Most brain-encoding studies focus on aligning artificial models with brain activity during language comprehension or passive visual processing, while interactive brain-alignment studies have to date been largely limited to reinforcement-learning (RL) agents and theory-based models. To address this ...

---

### 11. Computational Auditory Periphery Models: the Return of the Rodent

**Authors:** Morgan Thienpont, F. Deloche, S. Keshishzadeh, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19070v2) | 📄 [PDF](https://arxiv.org/pdf/2605.19070v2)

**Summary:** Animal experiments have provided many insights on auditory function, notably in cases of sensorineural hearing loss (SNHL). However, it is not always clear how these findings translate to the human auditory system in clinically relevant contexts. Cross-species computational models of the auditory periphery can help bridge the gap between non-invasive human diagnostics and experimental evidence from animal studies. In this work we adapted a 1-D nonlinear cochlear transmission-line model designed ...

---

### 12. Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs

**Authors:** Srinivas Ravishankar, Virginia de Sa

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19048v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19048v1)

**Summary:** While intracortical Brain-Computer Interfaces (iBCIs) that decode imagined handwriting have achieved high communication rates for Latin scripts, they rely on observing every character in the alphabet during training. This poses a challenge in scaling to logographic languages (e.g., Chinese, Japanese), where the character set exceeds thousands of classes. The limitation highlights a fundamental question in motor neuroscience: does the motor cortex represent handwriting through the composition of ...

---

### 13. Toward an Origin of Human Randomness: Interaction-Driven Enhancement in the Rock-Paper-Scissors Game

**Authors:** Song-Ju Kim, Shoma Ohara, Hiroaki Kurokawa

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18616v1)

**Summary:** Human-generated randomness is constrained by cognitive, motor, and strategic biases. This study examines how these constraints appear in individual behavior and how they may be modified through interaction with another human. We analyzed repeated rock-paper-scissors data from 9 participants, yielding 108 human-human matches and 216 individual player sequences. Using Lempel-Ziv complexity (LZC), we compared human-human sequences with the RNG-opponent condition. In the RNG-opponent condition, the ...

---

### 14. Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data

**Authors:** Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18557v1)

**Summary:** The brain learns abstract representations of high-dimensional sensory input, but the plasticity rules that enable such learning are unknown. We study biologically plausible algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to investigate how deep neural networks learn the intrinsic hierarchical structure of high-dimensional data. We focus on two types of local learning rules that avoid both a long convergence time and the use of a symmetric error network. The first t...

---

### 15. Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG with Controlled Internal and External Attention Conditions

**Authors:** Yuwen Zeng, Dengzhe Hou, Zhang Zhang, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18251v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18251v1)

**Summary:** Self-initiated attention shifts play a critical role in voluntary behavior but are difficult to study due to the absence of explicit temporal markers. While previous studies have examined their neural correlates, it remains unclear how multi-dimensional electroencephalography (EEG) features contribute to their characterization within an interpretable computational framework. In this study, we build on an experimental paradigm developed in our previous work, which enables controlled comparison be...

---

### 16. Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function

**Authors:** Mario Senden, Leonardo Dalla Porta, Jan Fousek, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18118v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18118v1)

**Summary:** Contemporary computational neuroscience features two prominent modeling traditions. Bottom-up whole-brain modeling (WBM) builds biophysically detailed simulations of brain structure and dynamics, whereas top-down neuroconnectionism optimizes deep neural networks for functional performance. Each has achieved remarkable success yet remains incomplete with WBMs lacking functional competence and neuroconnectionist models showing limited biological grounding. Here we propose functional whole-brain mo...

---

### 17. Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks: a computational account with clinical predictions

**Authors:** Esila Keskin

**Published:** 2026-05-17

🔗 [Paper](http://arxiv.org/abs/2605.17399v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17399v1)

**Summary:** Von Economo neurons (VENs) are selectively lost in behavioural-variant frontotemporal dementia (bvFTD) and reduced in autism spectrum conditions (ASC), yet their computational role in social learning remains unexplained. We train a spiking neural network (the VENCircuit) embedding VEN-like projection neurons (K=40, 2% of total) in a recurrent pyramidal circuit across 50 matched random initialisations with and without VENs. The network is trained on a controlled binary classification task; we mak...

---

### 18. Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity

**Authors:** Prashant C. Raju

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.17199v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17199v1)

**Summary:** Memory systems can store vastly different amounts of information despite similar hardware constraints. Here, we show that superior spatial memory emerges from a discrete stiffening of hippocampal population geometry-a transition from disorganized to crystalline collective coding. Comparing food-caching chickadees to non-caching zebra finches, we found that the caching hippocampus maintains a topologically rigid, "crystalline" geometry with significantly higher geometric stability (Shesha 0.245 v...

---

### 19. MIRAGE: Robust multi-modal architectures translate fMRI-to-image models from vision to mental imagery

**Authors:** Reese Kneeland, Cesar Kadir Torrico Villanueva, Jordyn Ojeda, et al.

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.17198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17198v1)

**Summary:** To be useful for downstream applications, vision decoding models that are trained to reconstruct seen images from human brain activity must be able to generalize to internally generated visual representations, i.e., mental images. In an analysis of the recently released NSD-Imagery dataset, we demonstrated that while some modern vision decoders can perform quite well on mental image reconstruction, some fail, and that state-of-the-art (SOTA) performance on seen image reconstruction is no guarant...

---

### 20. Effort as Ceiling, Not Dial: Reasoning Budget Does Not Modulate Cognitive Cost Alignment Between Humans and Large Reasoning Models

**Authors:** Yueqing Hu, Tianhong Wang

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.16938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16938v1)

**Summary:** Large Reasoning Models (LRMs) generate chain-of-thought traces whose length tracks human reaction times across cognitive tasks, but recent debate questions whether this alignment reflects genuine computational structure or surface verbosity. We test whether the alignment varies with inference-time reasoning effort. Across GPT-OSS-20B and GPT-OSS-120B, three effort levels, and six reasoning tasks, within-task and cross-task alignment remain invariant: Bayes Factors lean toward the null, and mean ...

---

### 21. A Mathematical Characterization of Neural Activation Induced by Temporal Interference Stimulation

**Authors:** Esteban Paduro, Antoine Chaillet, Mario Sigalotti

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.16761v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16761v1)

**Summary:** Temporal Interference Stimulation (TIS) is a non-invasive neuromodulation technique in which two high-frequency sinusoidal currents with slightly different frequencies generate a low-frequency envelope that can activate deep neural structures. This study investigates the conditions under which TIS elicits action potentials in a single neuron modeled by the FitzHugh-Nagumo system. This research integrates phase-plane analysis and geometric singular perturbation to develop a mathematical framework...

---

### 22. EmoMind: Decoding Affective Captions from Human Brain fMRI

**Authors:** Bilal A. Mohammed, Lin Gu, Ruogo Fang

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.16739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16739v1)

**Summary:** Decoding visual experience from brain activity has advanced substantially, but cur- rent brain-to-text systems largely recover semantic content while discarding affect. Additionally, language models can generate emotional text when prompted with categorical labels, but such labels collapse rich inter-subject variability into coarse discrete bins. We present EmoMind, the first end-to-end pipeline for decoding affective captions directly from fMRI signals. EmoMind first retrieves a semanti- cally ...

---

### 23. The Complex Brain Hypothesis: Resolving the Entropy-Content Conundrum in Minimal Phenomenal Experience

**Authors:** Jonas Mago, Edmundo Lopez-Sola, Jakub Vohryzek, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.16146v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16146v1)

**Summary:** Minimal Phenomenal Experiences (MPEs) are states of consciousness in which wakefulness is preserved but phenomenal content is low or absent. The Entropic Brain Hypothesis (EBH) is a model of conscious processes that regards the entropy of spontaneous brain activity as a marker of 'phenomenal richness', exemplified by high-content psychedelic experiences (HCPEs). Yet recent human neuroimaging studies of MPEs induced by meditation -- and possibly 5-MeO-DMT -- suggest that these states, defined by ...

---

### 24. Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex

**Authors:** Idan Daniel Grosbard, Mor Geva, Galit Yovel

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.16468v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16468v1)

**Summary:** A central goal in understanding human vision is to uncover the visual features that drive neuronal activity. A growing body of work has used artificial neural networks as encoding models to predict cortical responses to natural images, revealing the visual content that activates category-selective regions. However, existing approaches are largely correlational and treat the encoder as a black box, leaving open which image features drive each voxel's response. We introduce Mechanistically Interpr...

---

### 25. From Observed Viability to Internal Predictive Approximation: A Single-Subject Latent-Space Analysis of Gait Dynamics Under Occlusal Constraint

**Authors:** Jacques Raynal, Pierre Slangen, Elsa Raynal, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15862v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15862v1)

**Summary:** Adaptive biomechanical systems may show similar observable gait performance while differing in latent organization and longitudinal behavior. This study examines whether an observed longitudinal transformation of gait organization can be approximated within a predictive latent-space framework, without claiming clinical prediction or causal occlusal effects.   Using an exploratory single-subject design in a Parkinsonian participant, gait was recorded with instrumented insoles during two sessions ...

---

### 26. Beyond Flickering: Introducing Code-Modulated Motion Visual Evoked Potentials for Brain-Computer Interfacing

**Authors:** Hanneke Scheppink, Rainer Herpers, Jordy Thielen, et al.

**Published:** 2026-05-15

🔗 [Paper](http://arxiv.org/abs/2605.15801v1) | 📄 [PDF](https://arxiv.org/pdf/2605.15801v1)

**Summary:** A code-modulated motion visual evoked potential (c-MVEP) for brain-computer interfacing (BCI) is presented in this study. This paradigm uses pseudo-random sequences to visually stimulate objects using motion as an alternative to flickering. In an offline experiment of this study, EEG data were recorded and compared during sequential stimulation of a single object under four conditions: c-MVEP, code-modulated visual evoked potential (c-VEP), steady-state motion visual evoked potential (SSMVEP), a...

---

### 27. REALM: Retrospective Encoder Alignment for LFP Modeling

**Authors:** Peicheng Wu, Zhenyu Bu, Runze Ma, et al.

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14867v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14867v1)

**Summary:** Spike activity has been the dominant neural signal for behavior decoding due to its high spatial and temporal resolution. However, as brain-computer interfaces (BCIs) move toward high channel counts and wireless operation, the high sampling frequency of spike signals becomes a bottleneck due to high power and bandwidth requirements. Local field potentials (LFPs) represent a different spatial-temporal scale of brain activity compared to spikes, offering key advantages including improved long-term...

---

### 28. Are cortical microcircuits optimized for information flux? -- A simulation-based reverse engineering study

**Authors:** Claus Metzner, Ali Ghebleh, Karin Prebeck, et al.

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14680v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14680v1)

**Summary:** A sufficiently large information flux in recurrent neural networks, quantified by the mutual information between successive network states, is considered a prerequisite for rich information processing capabilities. This raises the question of whether biological neural networks, such as cortical microcolumns, may be structurally organized to enhance information flux. To investigate this possibility, we study a simplified model of the cortical layer 5 architecture, in which a densely and strongly ...

---

### 29. Multiple mechanisms of rhythm switching in recurrent neural networks with adaptive time constants

**Authors:** Yutaka Yamaguti, Shota Nakamura

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14388v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14388v1)

**Summary:** Although recurrent neural networks (RNNs) trained on cognitive tasks have become a widely used framework for studying neural computation, the internal mechanisms by which RNNs switch between rhythms across multiple frequency bands, and how these mechanisms relate to neuronal time constants, have not been systematically analyzed. We trained leaky integrator RNNs with neuron-specific learnable time constants on a four-band (theta, alpha, beta, gamma) rhythm-switching task and analyzed 20 independe...

---

### 30. Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation

**Authors:** Wilten Nicola, Sue Ann Campbell

**Published:** 2026-05-14

🔗 [Paper](http://arxiv.org/abs/2605.14319v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14319v1)

**Summary:** Firing rate fluctuations in neural populations are observed experimentally over multiple time scales, in single neurons, across trials when elicited by stimuli, and across populations. In this work, we examine how firing rate fluctuations emerge in networks of coupled integrate-and-fire neurons as a function of the initial distribution of voltages in networks with time-varying inputs. We analytically derive an approximation for the evolution of the instantaneous population rate or flux as a func...

---

### 31. Do Language Models Align with Brains? Prediction Scores Are Not Enough

**Authors:** Xiao Jia

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.14025v1) | 📄 [PDF](https://arxiv.org/pdf/2605.14025v1)

**Summary:** Brain-language model comparisons often interpret neural prediction scores as evidence that model representations capture brain-relevant language computation. We asked whether language models align with brains, and whether prediction scores are enough to support that claim, using L-PACT, a source-audited framework that evaluates predictive, relational, mechanism-stripping, and reliability-bounded evidence. Across primary naturalistic language neural datasets and derived language-model representat...

---

### 32. Characterizing Universal Object Representations Across Vision Models

**Authors:** Florian P. Mahner, Johannes Roth, Ka Chun Lam, et al.

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13675v1)

**Summary:** Deep neural networks trained with different architectures, objectives, and datasets have been reported to converge on similar visual representations. However, what remains unknown is which visual properties models actually converge on and which factors may underlie this convergence. To address this, we decompose the object similarity structure of 162 diverse vision models into a small set of non-negative dimensions. To determine universal versus model-specific dimensions, we then estimate how of...

---

### 33. Embodied Neurocomputation: A Framework for Interfacing Biological Neural Cultures with Scaled Task-Driven Validation

**Authors:** Johnson Zhou, Daniel Tanneberg, Forough Habibollahi, et al.

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13315v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13315v1)

**Summary:** Biological neural networks (BNNs) have been established as a powerful and adaptive substrate that offer the potential for incredibly energy and data efficient information processing with distinct learning mechanisms. Yet a core challenge to utilizing BNN for neurocomputation is determining the optimal encoding and decoding mechanisms between the traditional silicon computing interface and the living biology. Here, we propose an Embodied Neurocomputation framework as a systems-level approach to t...

---

### 34. Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale

**Authors:** John R. Minnick, Jesus Gonzalez-Ferrer, Kamran Hussain, et al.

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.12999v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12999v1)

**Summary:** Closed-loop brain-computer interfaces often require both a forecast of upcoming neural population activity and a readout of the animal's behavioral state. A single Mamba forecaster, trained only on next-step spike counts at Neuropixels scale, can deliver both in one forward pass. A lightweight per-session linear head reading the model's predicted rates decodes behavior better than the same linear classifier reading the raw spike counts, under matched temporal context. We test on the Steinmetz vi...

---

### 35. SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting

**Authors:** John R. Minnick, Jinghui Geng, Kamran Hussain, et al.

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.12992v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12992v1)

**Summary:** Neural population models, which predict the joint firing of many simultaneously recorded neurons forward in time, are typically evaluated by a single aggregate Pearson correlation $r$ between predicted and actual spike counts, a number that masks critical structure. We argue that how we evaluate spike forecasting matters as much as what we build, and introduce SpikeProphecy, the first large-scale benchmark for causal, autoregressive spike-count forecasting on real electrophysiology recordings. O...

---

### 36. Feature Visualization Recovers Known Cortical Selectivity from TRIBE v2

**Authors:** Stuart Bladon, Brinnae Bent

**Published:** 2026-05-13

🔗 [Paper](http://arxiv.org/abs/2605.13904v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13904v1)

**Summary:** Brain encoder models predict cortical fMRI responses from the internal activations of pretrained vision and language networks, and are typically evaluated by held-out prediction accuracy. This is a useful signal for training but a poor one for interpretation: it tells us an encoder fits the data without telling us whether it has internalized the functional organization of the brain. We propose feature visualization -- gradient ascent on the encoder's predicted activation for a target region of i...

---

### 37. State-Space NTK Collapse Near Bifurcations

**Authors:** James Hazelden, Eric Shea-Brown

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12763v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12763v1)

**Summary:** Rich feature learning in tasks that unfold over time often requires the model to pass through bifurcations, constituting qualitative changes in the underlying model dynamics. We develop a local theory of gradient descent near these transitions through the empirical state-space neural tangent kernel (sNTK). Our central finding is that bifurcations both dominate and simplify learning dynamics: near bifurcations, we can reduce sNTK to a rank-one operator corresponding to learning in a classical nor...

---

### 38. Predictive Coding Light+: learning to predict visual sequences with spike timing-dependent plasticity and synaptic delays

**Authors:** Antony W. N'dri, Thomas Barbier, Céline Teulière, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12732v1)

**Summary:** The ability to predict the future is of great value for biological and artificial cognitive systems alike. However, successfully predicting the future typically requires maintaining a memory of the recent past. It is currently unclear how biological or artificial spiking neural networks can learn to maintain past sensory information to help predict the future. Here we propose Predictive Coding Light+ (PCL+), a spiking neural network architecture for unsupervised sequence processing that learns r...

---

### 39. Human face perception reflects inverse-generative and naturalistic discriminative objectives

**Authors:** Wenxuan Guo, Heiko H. Schütt, Kamila Maria Jozwik, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12619v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12619v1)

**Summary:** The perceptual representations supporting our ability to recognize faces remain a computational mystery. Deep neural networks offer mechanistic hypotheses for human face perception, but theoretically distinct models often make indistinguishable representational predictions for randomly sampled faces. To expose diagnostic differences among these hypotheses, we compared six neural network models sharing an architecture but trained on distinct tasks, using face pairs optimized to elicit contrasting...

---

### 40. Letting the neural code speak: Automated characterization of monkey visual neurons through human language

**Authors:** Vedang Lad, Katrin Franke, Tamar Rott Shaham, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12485v2) | 📄 [PDF](https://arxiv.org/pdf/2605.12485v2)

**Summary:** Understanding what individual neurons encode is a core question in neuroscience. In primary visual cortex (V1), mathematical models (e.g., Gabor functions) capture neural selectivity, but no comparable framework exists for higher areas. We show that natural language can fill this role: across macaque V1 and V4, the selectivity of most neurons is captured by concise, verifiable semantic descriptions. Using digital twins of V1 and V4, we develop a closed-loop framework that translates each neuron'...

---

### 41. Empirical scaling laws in balanced networks with conductance-based synapses

**Authors:** Vicky Zhu, Gabriel Ocker, Robert Rosenbaum

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12404v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12404v1)

**Summary:** Strongly coupled, recurrent, balanced network models have been successful in describing and predicting many phenomena observed in cortical neural recordings. However, most balanced network models use current-based synapse models in place of more realistic, conductance-based models. Conductance-based synapse models predict unrealistically small membrane potential variability. On the other hand, introducing realistic levels of spike time correlations to models with current-based synapses predicts ...

---

### 42. From Organization to Viability: A Multi-Level Analysis of Gait Dynamics Under Occlusal Constraint

**Authors:** Jacques Raynal, Pierre Slangen, Elsa Raynal, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.13893v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13893v1)

**Summary:** Clinical interpretation often assumes that observable performance provides sufficient information about the organization of an adaptive system. However, similar observable performance may correspond to distinct latent organizations. This study extends a previous multi-level framework by introducing a fourth analytical level centered on longitudinal viability. Using an exploratory single-case design in a Parkinsonian patient, gait data were recorded with instrumented insoles under three occlusal ...

---

### 43. From Clever Hans to Scientific Discovery: Interpreting EEG Foundational Transformers with LRP

**Authors:** Justus Meyer zu Bexten, Nico Scherf, Bogdan Franczyk, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11885v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11885v1)

**Summary:** Emerging foundation models (FMs) in electroencephalography (EEG) promise a path to scale deep learning in diagnostics and brain-computer interfaces despite data scarcity, yet their opaque nature remains a barrier to wider adoption. We investigate attention-aware Layer-wise relevance propagation (LRP) as a post-hoc attribution method for EEG-FMs, extending LRP's use on convolutional neural network (CNN)-based EEG models to the Transformer architectures that current FMs are based on. We find that ...

---

### 44. Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization

**Authors:** Zhaotian Gu, Molan Li, Jie Su, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11718v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11718v1)

**Summary:** The spatial and functional organization of the primate visual cortex is a fundamental problem in neuroscience. While recent computational frameworks like the Topographic Deep Artificial Neural Network (TDANN) have successfully modeled spatial organization in the ventral stream, the computational origins of the dorsal stream's distinct topographies, such as direction-selective maps in the middle temporal (MT) area, remain largely unresolved. In this work, we present a spatiotemporal TDANN to inve...

---

### 45. Accounting for Missed Events in the Bayesian Modeling of IP3R Multimodal Gating

**Authors:** Schayma Ben Marzougui, Audrey Denizot, Hugues Berry

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11675v1)

**Summary:** The Inositol 1,4,5-trisphosphate receptor channel (IP 3 R) is an important calcium channel involved in calcium-induced calcium release, playing a prominent role in intracellular calcium signaling. However, accurately characterizing its gating behavior remains a challenge, particularly due to the temporal resolution of patch clamp techniques that is not large enough to detect all short-lived events. This limitation can significantly bias the inference of kinetic models describing the receptor act...

---

### 46. Consciousness as Uncommon Self-Knowledge: A Synergistic Information Framework

**Authors:** Krti Tallam

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.13884v1) | 📄 [PDF](https://arxiv.org/pdf/2605.13884v1)

**Summary:** We propose uncommon self-knowledge (USK) as a candidate criterion for consciousness: synergistic information a system carries about itself that exists only in the joint of its subsystems and is destroyed by decomposition. Drawing on Gottwald's partition-lattice grounding of Partial Information Decomposition (PID), where redundancy corresponds to Aumann's common knowledge and synergy to the gap between separate and joint observation, we propose the synergistic component of self-directed informati...

---

### 47. On periodic distributed representations using Fourier embeddings

**Authors:** Jakeb Chouinard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10818v2) | 📄 [PDF](https://arxiv.org/pdf/2605.10818v2)

**Summary:** Periodic signals are critical for representing physical and perceptual phenomena. Scalar, real angular measures, e.g., radians and degrees, result in difficulty processing and distinguishing nearby angles, especially when their absolute difference exceeds pi. We can avoid this problem by using real-valued, periodic embeddings in high-dimensional space. These representations also allow us to control the nature of their dot product similarities, allowing us to construct a variety of different kern...

---

### 48. Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning

**Authors:** Alexandra Voce, Emmanouil Giannakakis, Claudia Clopath

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10356v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10356v1)

**Summary:** The cerebellum and cerebral cortex form tightly coupled circuits thought to support flexible and efficient temporal processing. How this interaction shapes cortical learning dynamics, and whether such heterogeneous modularity can benefit artificial systems, remains unclear. Here, we augment a recurrent neural network (RNN) with a cerebellar-inspired feedforward module and evaluate the resulting architecture on temporal tasks of varying difficulty. The cortico-cerebellar RNN (CB-RNN) learns faste...

---

### 49. Positive Alignment: Artificial Intelligence for Human Flourishing

**Authors:** Ruben Laukkonen, Seb Krier, Chloé Bakalar, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10310v2) | 📄 [PDF](https://arxiv.org/pdf/2605.10310v2)

**Summary:** Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and n...

---

### 50. Joint sparse coding and temporal dynamics support context reconfiguration

**Authors:** Qianqian Shi, Yue Che, Faqiang Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10178v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10178v1)

**Summary:** Adaptive behavior requires the brain to transition between distinct contexts while maintaining representations of prior experience. The ability to reconfigure neural representations without erasing previously acquired knowledge is central to learning in dynamic environments, yet the neural mechanisms that support this balance remain unclear. Understanding these mechanisms is also critical for addressing catastrophic forgetting in artificial systems designed for lifelong learning. Here, we identi...

---

## stat.ML

**50 papers**

### 1. The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning

**Authors:** Vishal Rajput

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22800v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22800v1)

**Summary:** Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching p...

---

### 2. Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models

**Authors:** Krishnakumar Balasubramanian

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22795v1)

**Summary:** We propose and analyze a conservative drifting method for one-step generative modeling. The method replaces the original displacement-based drifting velocity by a kernel density estimator (KDE)-gradient velocity, namely the difference of the kernel-smoothed data score and the kernel-smoothed model score. This velocity is a gradient field, addressing the non-conservatism issue identified for general displacement-based drifting fields. We prove continuous-time finite-particle convergence bounds fo...

---

### 3. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis

**Authors:** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22776v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22776v1)

**Summary:** Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed...

---

### 4. Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation

**Authors:** Samson Gourevitch, Yazid Janati, Dario Shariatian, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22765v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22765v1)

**Summary:** Discrete diffusion models are often trained through clean-data prediction, but the prediction can be used in different ways to define the reverse dynamics. In Masked Diffusion Models (MDM) these choices largely coincide, whereas in Uniform Diffusion Models (UDM) they do not. We show that the standard plug-in bridge parameterization for UDM is not optimized by the denoising posterior, but by a leave-one-out posterior that predicts each clean token without using its own noisy observation. This ide...

---

### 5. Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier

**Authors:** Berk Hayta, Hannah Laus, Simon Mittermaier, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22746v1)

**Summary:** Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are predicted by a learned neural network mapping. However, this approach can lead to computational challenges, as Dirichlet expected objectives are more complex than standard supervised learning losses, ...

---

### 6. Proxy-Based Approximation of Shapley and Banzhaf Interactions

**Authors:** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22738v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22738v1)

**Summary:** Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed and accuracy. To overcome this limitation, we introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction. On a theoretical level, we derive a polynomial-time generalization of interventional TreeSHAP t...

---

### 7. Multiple Neural Operators Achieve Near-Optimal Rates for Multi-Task Learning

**Authors:** Adrien Weihs, Hayden Schaeffer

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22724v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22724v1)

**Summary:** We study the approximation and statistical complexity of learning collections of operators in a shared multi-task setting, with a focus on the Multiple Neural Operators (MNO) architecture. For broad classes of Lipschitz multiple operator maps, we derive near-optimal upper bounds for approximation and statistical generalization. On the lower-bound side, we establish a curse of parametric complexity and prove corresponding minimax rates. Together, these results show that shared representations acr...

---

### 8. Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion

**Authors:** Meimingwei Li, Yuanhao Ding, Esteban Garces Arias, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22579v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22579v1)

**Summary:** Recent work has identified a counterintuitive phenomenon termed "Hyperfitting", where fine-tuning Large Language Models (LLMs) to near-zero training loss on small datasets surprisingly enhances open-ended generation quality and mitigates repetition in greedy decoding. While effective, the underlying mechanism remains poorly understood, with the extremely low-entropy output distributions suggesting a potential equivalence to simple temperature scaling. In this work, we demonstrate that this pheno...

---

### 9. A Martingale Kernel Independence Test

**Authors:** Felix Laumann, Zhaolu Liu, Mauricio Barahona

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22549v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22549v1)

**Summary:** The Hilbert-Schmidt Independence Criterion (HSIC) and its joint-independence extension $d\mathrm{HSIC}$ are degenerate $V$-statistics whose data-dependent weighted-$χ^2$ null limits force a permutation calibration that multiplies the per-test cost by the number of permutations, in practice two orders of magnitude. Adapting the recent martingale MMD construction for two-sample testing to the (joint) independence problem, we introduce two studentised statistics whose null distributions are standar...

---

### 10. Generative Modeling by Value-Driven Transport

**Authors:** Pablo Moreno-Muñoz, Adrian Müller, Gergely Neu

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22507v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22507v1)

**Summary:** We propose a new framework for generative modeling based on a discrete-time stochastic control formulation of measure transport. Adapting classic results from control theory, we formulate our problem as a linear program whose dual variables correspond to the \emph{optimal value function} of the control problem, which directly encodes the optimal control policy. Exploiting this LP formulation, we develop an efficient simulation-free primal-dual algorithm for computing approximately optimal value ...

---

### 11. Do Not Trust The Auctioneer: Learning to Bid in Feedback-Manipulated Auctions

**Authors:** Luigi Foscari, Matilde Tullii, Vianney Perchet

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22438v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22438v1)

**Summary:** Shilling is the use of artificial bids to make competition appear stronger and push prices upward. We study repeated first-price auctions in which shilling affects feedback but not allocation: the learner wins or loses against the real competing bid, but after a loss observes the maximum of the real bid and an independent shill bid. Thus the manipulation changes what the learner observes and hence how it learns to bid, without changing the outcome of the current auction. We analyze regret with r...

---

### 12. Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions

**Authors:** Gabriel Kronberger, Fabricio Olivetti de Franca, Deaglan J. Bartlett, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22374v1)

**Summary:** Symbolic regression with genetic programming (GPSR) may suffer from overfitting and structural bloat, especially when noise is present. In this paper we evaluate description length (DL) and fractional Bayes factor (FBF) criteria as principled, data-efficient alternatives to heuristics for selecting compact expressions that generalise well. We implement DL using a Fisher-information-based parameter encoding and compare it to AIC and BIC across multiple datasets, including noisy synthetic benchmar...

---

### 13. Departure from Regularity: Degree Heterogeneity and Eigengap as the Structural Drivers of ASE-LSE Latent Subspace Disagreement

**Authors:** Minh Triet Pham, Ian Gallagher

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22346v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22346v1)

**Summary:** Two of the most widely used methods for analysing graph data, Adjacency Spectral Embedding and Laplacian Spectral Embedding, often produce different results when applied to the same network. Yet the structural reasons behind this disagreement remain incompletely understood. This paper provides a structural account. We show that regularity is a sufficient condition for perfect agreement: when every node has the same number of connections, the two methods produce identical latent subspaces. Any de...

---

### 14. From Sequential Nodes to GPU Batches: Parallel Branch and Bound for Optimal $k$-Sparse GLMs

**Authors:** Jiachang Liu, Andrea Lodi

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22188v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22188v1)

**Summary:** GPUs have significantly accelerated first-order methods for large-scale optimization, especially in continuous optimization. However, this success has not transferred cleanly to problems with discrete variables, combinatorial structure, and nonlinear objectives, such as certifying optimal solutions for cardinality-constrained generalized linear models. Major challenges include the sequential processing of heterogeneous nodes in branch and bound (BnB) and frequent data movement between the CPU an...

---

### 15. From Betting to Empirical Bernstein LIL

**Authors:** Francesco Orabona

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22124v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22124v1)

**Summary:** This is a verbatim copy of a technical report I wrote in 2017-2018 to obtain the law of the iterated logarithm using the guarantee on the wealth of an online betting strategy.

---

### 16. Aerodynamic force reconstruction using physics-informed Gaussian processes

**Authors:** Gledson Rodrigo Tondo, Igor Kavrakov, Guido Morgenthal

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22111v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22111v1)

**Summary:** Accurate modeling of aerodynamic loads is essential for understanding and predicting the responses of complex structural systems. However, these models often rely on simplifications of the true physical forces, introducing assumptions that can limit their accuracy. Validating such models becomes particularly challenging in the presence of noisy or incomplete data. To address this, we introduce a probabilistic physics-informed machine learning approach designed to reconstruct the underlying aerod...

---

### 17. Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks

**Authors:** Margalit Glasgow, Joan Bruna

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22010v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22010v1)

**Summary:** We consider one-hidden layer neural networks trained in the feature-learning regime using gradient descent, and relate the output of the finite-width network $f_{\hatρ_t^m}$ to its infinite-width counterpart $f_{ρ_t^{MF}}$, which evolves in the mean-field dynamics.   While constant-time horizon bounds for $\|f_{ρ_t^{MF}} - f_{\hatρ_t^m}\|$ may be obtained via standard Grönwall estimates, the long-time behavior of the fluctuation is a more delicate matter. Uniform-in-time bounds often rely on (lo...

---

### 18. Robust Statistical Estimators with Bounded Empirical Sensitivity

**Authors:** Valentio Iverson, Gautam Kamath, Argyris Mouzakis, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21860v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21860v1)

**Summary:** We introduce a new measure of robustness for statistical estimators, which we call \emph{empirical sensitivity}. An estimator $\hat θ$ has bounded empirical sensitivity if, with high probability over a dataset $X = (X_1, \dots, X_n) \sim \mathcal{D}^{\otimes n}$, for any dataset $Y$ obtained by modifying at most $ηn$ points in $X$, we have that $\hat θ(Y)$ is close to $\hat θ(X)$.   We study bounds on this quantity for the prototypical problem of Gaussian mean estimation. We prove new lower boun...

---

### 19. Causal Discovery in Structural VAR Models Under Equal Noise Variance

**Authors:** SeyedSina Seyedi HasanAbadi, Fahimeh Arab, Erfan Nozari, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21846v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21846v1)

**Summary:** Causal discovery from multivariate time series is challenging when causal effects may occur both across time and within the same sampling interval. This issue is especially important in applications such as neuroscience, where the sampling rate may be coarse relative to the underlying dynamics and contemporaneous effects need not form an acyclic graph. We study causal discovery in linear Gaussian structural VAR models under an equal noise variance assumption, meaning that the structural noise te...

---

### 20. Truncated Neural Likelihood Estimation for Simulation-Based Inference in State-Space Models

**Authors:** Kostas Tsampourakis, Víctor Elvira

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21805v1)

**Summary:** State-space models (SSMs) are powerful probabilistic tools for modeling time-varying systems with latent dynamics. Inference in SSMs involves the estimation of latent states and parameters. In this work, we focus on parameter inference, which for SSMs is in general a very challenging problem due to the intractability of the likelihood. Recently, neural estimation methods, such as sequential neural likelihood (SNL), have shown promising results in Bayesian inference problems. In this paper, we sh...

---

### 21. Three Costs of Amortizing Gaussian Process Inference with Neural Processes

**Authors:** Robin Young

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21798v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21798v1)

**Summary:** Neural processes amortize Gaussian process inference, replacing the exact $O(n^3)$ posterior with a learned $O(n)$ map from context sets to predictive distributions. For a class of latent neural processes, we bound the Kullback--Leibler (KL) divergence between the GP and LNP predictives, decomposing it into three interpretable sources, namely label contamination as the neural process uses label values to estimate a quantity that is label-independent in the exact GP, an information bottleneck bec...

---

### 22. Targeted maximum likelihood estimation of vaccine effectiveness and immune correlates in test-negative design studies with missing data

**Authors:** Leah I. B. Andrews, Lars van der Laan, Peter B. Gilbert

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21793v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21793v1)

**Summary:** The test-negative design (TND) is a resource-efficient observational study design that can assess vaccine effectiveness and exposure-proximal immune correlates of disease. The TND enrolls symptomatic individuals seeking diagnostic testing and compares case status by an exposure variable, such as vaccination status or immune marker level, that is measured at testing. While the TND reduces confounding by healthcare-seeking behavior, other sources of confounding may remain. TND studies may also hav...

---

### 23. MMD-Balls as Credal Sets: A PAC-Bayesian Framework for Epistemic Uncertainty in Test-Time Adaptation

**Authors:** Ahanaf Hasan Ariq

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21783v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21783v1)

**Summary:** Test-time adaptation (TTA) methods improve model performance under distribution shift but lack formal guarantees connecting shift magnitude to prediction reliability. We develop a PAC-Bayesian framework yielding generalization bounds explicitly parameterized by the maximum mean discrepancy (MMD) between source and target distributions. Our principal contribution is interpreting MMD-balls around the source distribution as credal sets in Walley's imprecise probability theory, yielding natural epis...

---

### 24. On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents

**Authors:** Oliver Mortensen, Mohammad Sadegh Talebi

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21763v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21763v1)

**Summary:** We study risk-sensitive reinforcement learning in finite discounted MDPs, where a generative model of the MDP is assumed to be available. We consider a family or risk measures called the optimized certainty equivalent (OCE), which includes important risk measures such as entropic risk, CVaR, and mean-variance. Our focus is on the sample complexities of learning the optimal state-action value function (value learning) and an optimal policy (policy learning) under recursive OCE. We provide an exac...

---

### 25. Support-aware offline policy selection for advertising marketplaces

**Authors:** Prashant Shekhar, Caroline Howard

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21736v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21736v1)

**Summary:** Logged advertising auctions make offline reserve-price evaluation attractive but risky. Replay tables can identify policies with large apparent yield gains, yet they can also hide weak threshold support, multiple-comparison effects, subgroup harm, and bidder-response uncertainty. Existing replay and off-policy evaluation methods estimate or rank policy values, but they do not directly answer the operational question of whether the available evidence is strong enough to justify validation. This p...

---

### 26. Representation Gap: Explaining the Unreasonable Effectiveness of Neural Networks from a Geometric Perspective

**Authors:** David Perera, Victor Moura, Lais Isabelle Alves dos Santos, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21692v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21692v1)

**Summary:** Characterizing precisely the asymptotic generalization error of neural networks using parameters that can be estimated efficiently is a crucial problem in machine learning, which relies heavily on heuristics and practitioners' intuition to make key design choices. In order to mitigate this issue, we introduce the Representation Gap, a metric closely related to the generalization error, but admitting better-behaved asymptotic dynamics. Focusing on equivariant diffusion models and leveraging resul...

---

### 27. Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos

**Authors:** Lucas Fernandez Sarmiento

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21648v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21648v1)

**Summary:** We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos. Dropout shifts the perfect-alignment fixed point, making the depth scale for information propagation finite even at critical initialization. We derive critical and crossover scaling laws for correlation decay and establish that smooth activations and kinked, ReLU-like activations constitute distinct universality classes, with different critical exponents and a universal two-parameter ...

---

### 28. Distribution-free root cause analysis

**Authors:** Rohan Hore, Aaditya Ramdas

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21627v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21627v1)

**Summary:** We study distribution-free root cause analysis in multi-stream data, where an evolving underlying system is observed through multiple data streams that may each undergo distributional changes at unknown timepoints. In such settings, the stream exhibiting the earliest change provides a natural starting point for investigating the underlying cause, which we refer to as the root-cause index. Leveraging conformal $p$-values, we propose a novel framework, Conformal Root Cause Analysis (CROC), which c...

---

### 29. Variance Reduction for Expectations with Diffusion Teachers

**Authors:** Jesse Bettencourt, Xindi Wu, Matan Atzmon, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21489v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21489v1)

**Summary:** Pretrained diffusion models serve as frozen teachers feeding downstream pipelines such as text-to-3D, single-step distillation, and data attribution. The teacher gradients these pipelines consume are Monte Carlo (MC) expectations over noise levels and Gaussian noise samples; their estimator variance dominates compute cost because each draw requires expensive upstream work (rendering, simulation, encoding). We introduce CARV, a compute-aware variance-accounting framework that motivates a hierarch...

---

### 30. Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

**Authors:** Dayal Singh Kalra, Maissam Barkeshli

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21486v1)

**Summary:** Hyperparameter transfer allows extrapolating optimal optimization hyperparameters from small to large scales, making it critical for training large language models (LLMs). This is done either by fitting a scaling law to the hyperparameters or by a judicious choice of parameterization, such as Maximal Update ($μ$P), that renders optimal hyperparameters approximately scale invariant. In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the qual...

---

### 31. Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment

**Authors:** Alim Igilik

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21437v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21437v1)

**Summary:** Standard approaches to forecasting the weekly number of earthquakes on a spatial grid rely on the Poisson distribution with a single global dispersion assumption. We show that this assumption is systematically violated in seismic data from Central Asia (2010-2024), where a likelihood-ratio test with boundary correction strongly rejects the Poisson hypothesis (p < 10^{-179}).   The main contribution of this work is the EarthquakeNet architecture, which provides an endogenous per-cell estimate of ...

---

### 32. Memorisation, convergence and generalisation in generative models

**Authors:** Antoine Maillard, Sebastian Goldt

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21402v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21402v1)

**Summary:** Generative neural networks learn how to produce highly realistic images from a large, but finite number of examples - or do they simply memorise their training set? To settle this question, Kadkhodaie, Guth, Simoncelli and Mallat (ICLR '24) trained diffusion models independently on disjoint subsets of a dataset and showed that they converge to nearly the same density when the number of training images is large enough. This result raises two basic questions: how much data do you need for converge...

---

### 33. On the Regularity and Generalization of One-Step Wasserstein-guided Generative Models for PDE-Induced Measures

**Authors:** Likun Lin, Zhongjian Wang, Jack Xin, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21388v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21388v1)

**Summary:** Despite the remarkable empirical success of generative models, the available theory on their statistical accuracy in scientific computing remains largely pessimistic. This paper develops a theoretical framework for understanding the regularity of transport maps and the generalization properties of one-step Wasserstein-guided generative models for PDE-induced probability measures. We consider normalized target densities associated with linear elliptic and parabolic equations on bounded domains, a...

---

### 34. $L^2$ over Wasserstein: Statistical Analysis for Optimal Transport

**Authors:** Riccardo Passeggeri, Rohan M. Shenoy, Pengcheng Ye

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21365v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21365v1)

**Summary:** Optimal transport provides an inherently geometric and highly structured framework for studying spaces of probability measures, supplying a rich theoretical toolkit for contemporary statistics, machine learning, and generative modelling. In applications, however, the measures of interest are almost never known precisely, calling for a theory of optimal transport that accounts for statistical uncertainty. We construct such a framework, lifting the classical theory to the setting of random probabi...

---

### 35. Semiparametric Efficient Bilevel Gradient Estimation

**Authors:** Fares El Khoury, Houssam Zenati, Nathan Kallus, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21341v1)

**Summary:** Functional bilevel methods estimate a lower-level function and plug it into a hypergradient, but this plug-in gradient can retain first-order bias when the lower-level problem is learned nonparametrically. To remove this bias, we develop a semiparametric debiasing theory for population bilevel gradients based on the efficient influence function. This perspective leads to a cross-fitted orthogonal hypergradient estimator for which we establish asymptotic normality together with uniform control ov...

---

### 36. Large-Step Training Dynamics of a Two-Factor Linear Transformer Model

**Authors:** Krishnakumar Balasubramanian

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21292v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21292v1)

**Summary:** Gradient-flow analyses show that simplified linear transformers can learn the in-context linear-regression algorithm, but they do not explain the finite-step behavior of gradient descent at large learning rates. Motivated by empirical work on high-learning-rate transformer instabilities and by the cubic-map phase diagram for quadratic regression, we study an exactly reducible one-prompt linear-transformer training problem. After normalization, the dynamics reduce to a two-factor product map with...

---

### 37. Theoretical guidelines for annealed Langevin dynamics in compositional simulation-based inference

**Authors:** Camille Touron, Gabriel V. Cardoso, Julyan Arbel, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21253v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21253v1)

**Summary:** Compositional score-based approaches to simulation-based inference (SBI) approximate the posterior over a shared parameter given $n$ independent observations by aggregating individually learned posterior scores: currently, there are two main propositions of such methods (Geffner et al. (2023), Linhart et al. (2026)). As the resulting composite score does not correspond to the score of any distribution along the forward diffusion path of the true multi-observation posterior, sampling from it via ...

---

### 38. Federated LoRA Fine-Tuning for LLMs via Collaborative Alignment

**Authors:** Shuaida He, Liwen Chen, Long Feng

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21217v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21217v1)

**Summary:** Low-rank adaptation (LoRA) has emerged as a powerful tool for parameter-efficient fine-tuning of large language models (LLMs). This paper studies LoRA under a federated learning setting, enabling collaborative fine-tuning across clients while preserving parameter efficiency. We focus on a highly heterogeneous regime in which clients share only partial structure and a substantial subset may be contaminated. We propose Collaborative Low-rank Alignment and Identifiable Recovery (CLAIR), a contamina...

---

### 39. Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling

**Authors:** Jongchan Park

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21557v1)

**Summary:** Conventional wisdom holds that large-batch training is fundamentally incompatible with Reinforcement Learning (RL) - beyond a modest threshold, increasing batch sizes typically yields diminishing returns or performance degradation due to the inherent non-stationarity of the data distribution. We challenge this view by observing that non-stationarity is not a fixed property of RL, but evolves throughout training: early stages exhibit rapid behavioral shifts that demand small batches for plasticit...

---

### 40. A Rigorous, Tractable Measure of Model Complexity

**Authors:** Oskar Allerbo, Thomas B. Schön

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21167v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21167v1)

**Summary:** An accurate assessment of a model's complexity is crucial for topics such as interpretation, generalization, and model selection. However, most existing complexity measures either rely on heuristic assumptions or are computationally prohibitive. In this paper, we present a mathematically rigorous yet easy-to-compute measure of model complexity that is based on the similarities between the model gradients across inputs. It is thus well-defined for any parametric model, but also for kernel-based n...

---

### 41. Improved Guarantees for Constrained Online Convex Optimization via Self-Contraction

**Authors:** Dhruv Sarkar, Abhishek Sinha

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21107v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21107v1)

**Summary:** We consider Constrained Online Convex Optimization (COCO) with adversarially chosen constraints. At each round, the learner chooses an action before observing the loss and constraint function for that round. The goal is to achieve small static regret against the best point satisfying all constraints while also controlling cumulative constraint violation ($\mathsf{CCV}$). For strongly convex losses, state-of-the-art algorithms achieve $O(\log T)$ regret and $O(\sqrt{T \log T})$ $\mathsf{CCV}.$ Th...

---

### 42. Expectation Consistency Loss: Rethink Confidence Calibration under Covariate Shift

**Authors:** Jinzong Dong, Zhaohui Jiang, Bo Yang

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21552v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21552v1)

**Summary:** Confidence calibration for classification models is vital in safety-critical decision-making scenarios and has received extensive attention. General confidence calibration methods assume training and test data are independent and identically distributed, limiting their effectiveness under covariate shifts. Previous calibration methods under covariate shift struggle with class-wise or canonical calibrations and often rely on unstable importance weighting when density ratios are large or unbounded...

---

### 43. Divide et Calibra: Multiclass Local Calibration via Vector Quantization

**Authors:** Cesare Barbera, Lorenzo Perini, Giovanni De Toni, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21060v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21060v1)

**Summary:** Accurate and well-calibrated Machine Learning (ML) models are mandatory in high-stakes settings, yet effective multiclass calibration remains challenging: global approaches assume calibration errors are homogeneous across the latent space, while local methods often rely on latent-space dimensionality reduction, which leads to information loss. To address these issues, we propose a compositional approach to multiclass calibration, where region-specific calibration maps are constructed from shared...

---

### 44. Conditioning Gaussian Processes on Almost Anything

**Authors:** Henry Moss, Lachlan Astfalck, Thomas Cowperthwaite, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21041v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21041v1)

**Summary:** Gaussian processes (GPs) offer a principled probabilistic model over functions, but exact inference is restricted to the linear-Gaussian regime. We establish an explicit equivalence between GPs and a class of linear diffusion models, recasting predictive sampling as an ODE with closed-form Gaussian dynamics and a likelihood-dependent guidance term that admits a simple Monte Carlo approximation. In the linear-Gaussian setting, we recover standard GP conditioning exactly; beyond conjugacy, the sam...

---

### 45. Local Covariate Selection for Average Causal Effect Estimation without Pretreatment and Causal Sufficiency Assumptions

**Authors:** Zeyu Liu, Zheng Li, Feng Xie, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21548v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21548v1)

**Summary:** We study the problem of selecting covariates for unbiased estimation of the total causal effect.Existing approaches typically rely on global causal structure learning over all variables, or on strong assumptions such as causal sufficiency - where observed variables share no latent confounders - or the pretreatment assumption, which limits covariates to those unaffected by the treatment or outcome. These requirements are often unrealistic in practice, and global learning becomes computationally p...

---

### 46. Concentration of General Stochastic Approximation Under Heavy-Tailed Markovian Noise

**Authors:** Shubhada Agrawal, Siva Theja Maguluri, Martin Zubeldia

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20999v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20999v1)

**Summary:** We establish maximal concentration bounds for the iterates generated by stochastic approximation algorithms with general step sizes, where the noise has a finite-state Markovian component plus a Martingale-difference component. When the Martingale-difference noise is bounded, we show that the tail of the error can be sub-Gaussian, sub-Weibull, or something lighter than any Pareto but heavier than any Weibull, depending on the step size sequence and on whether the random operator is almost surely...

---

### 47. Frequency-Domain Regularized Adversarial Alignment for Transferable Attacks against Closed-Source MLLMs

**Authors:** Leitao Yuan, Qinghua Mao, Daizong Liu, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21541v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21541v1)

**Summary:** Multimodal large language models (MLLMs) remain vulnerable to transfer-based targeted attacks, where perturbations optimized on open-source surrogate encoders can generalize to closed-source MLLMs. A key challenge for improving adversarial transferability is to effectively capture the intrinsic visual focus shared across different models, such that perturbations align with transferable semantic cues rather than surrogate-specific behaviors. However, existing methods suffer from spatial-domain fe...

---

### 48. LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging

**Authors:** Yassine Maziane, Ammar Mahran, Artavazd Maranjyan, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20866v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20866v1)

**Summary:** Communication is a major bottleneck in distributed learning, especially in large-scale settings and in federated learning environments with slow links. Three standard ways to reduce this cost are communication compression, local training, and communication-computation overlap. Methods that combine these ingredients are used in practice and have been found to be effective for large-scale training, but there is little theory for methods that combine all three. We study a heterogeneous-compute sett...

---

### 49. Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers

**Authors:** Nikhil Nayak, Julia White, Urchade Zaratiana, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20756v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20756v1)

**Summary:** Preconditioned optimizers are central to language model training, but their stochastic update rules are usually treated as direct approximations to population preconditioned descent. We show that this view misses two finite-sample biases. First, the gradient and preconditioner are typically estimated from the same minibatch, introducing gradient--preconditioner coupling bias. Second, even when the preconditioner estimate is unbiased, its inverse or inverse-root is generally biased because invers...

---

### 50. Everywhere Valid Bounds on False Discovery Proportions in Conformal Inference

**Authors:** Ziang Song, Ying Jin, Emmanuel J. Candès

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20726v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20726v1)

**Summary:** Modern applications of conformal inference to multiple testing problems, such as outlier detection and candidate selection, often involve selecting test samples whose conformal p-values fall below a threshold. The quality of such methods is often measured by the false discovery proportion (FDP), defined as the fraction of incorrect selections. Existing approaches typically control the expected value of the FDP, using methods such as the Benjamini-Hochberg procedure. This approach fails to provid...

---

