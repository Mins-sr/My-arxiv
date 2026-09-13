# arXiv Daily Digest - 2026-09-13

Total papers: 50

---

## cs.AI

**50 papers**

### 1. GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay

**Authors:** Boning Li, Longbo Huang

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11923v1)

**Summary:** Counterfactual regret minimization (CFR) is one of the few large numerical workloads that still runs faster on CPUs than on GPUs. Each iteration sweeps a game tree with up to billions of states in millions of small, interdependent gather and scatter steps issued through a generic tree interface. On a GPU every kernel finishes in microseconds, so kernel launches and framework dispatch dominate the run time, and prior GPU implementations have lost to optimized CPU code. We observe that for a fixed...

---

### 2. General Quantification of Covariate and Concept Shifts

**Authors:** Hongbo Chen, Li Charlie Xia

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11918v1)

**Summary:** Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging entropic optimal transport, we propose a key notion: $γ^{*}\!$-concept shifts, and derive a general ...

---

### 3. Can Edge-Deployable Vision-Language Models Identify Species?

**Authors:** William Zhou, Mayukha Siripuram, Xiao Yan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11916v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11916v1)

**Summary:** Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relevant class to evaluate for species identification. We test whether models in this deployment-relevant 2--8B range carry genuine taxonomic knowledge, evaluating four such VLMs (Qwen3-VL 2B/4B/8B, Gemma3 4B) against the domain-specific specialist BioCLIP (300M parameters) on a 96-species task, comparin...

---

### 4. Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

**Authors:** Masahiro Kato, Daiki Honma, Taka Kato

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11915v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11915v1)

**Summary:** Generative artificial intelligence changes how firms reach customers, but standard marketing data do not record how often users see and notice a firm's name in generated answers. We develop Generative Marketing Mix Modeling (GMMM) to estimate the causal effects of Generative Engine Optimization (GEO) and Generative Engine Marketing (GEM). For GEO, GMMM combines repeated generated answers with question counts, shares of use across generative systems, and notice probabilities. For GEM, it combines...

---

### 5. Artificial Id: Drive and Persistent Alignment in Agentic AI

**Authors:** Yakov Pyotr Shkolnikov

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11911v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11911v1)

**Summary:** Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current harnesses largely solve by hand: objectives, retries, verification, stopping rules and other behavioral transitions are specified externally. We propose an artificial id, an adaptive internal drive for determining whether behavior should continue, stop or change. In a minimal virtual Petri-dish expe...

---

### 6. MindTopo: Can Foundation Models Reason in Topological Space?

**Authors:** Yunfei Ge, Anbang Liu, Qineng Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11900v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11900v1)

**Summary:** Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity...

---

### 7. Domain-Specific Hallucination Detection in Large Language Models

**Authors:** Varun Teja Chundru, Debasmita Biswas

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11878v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11878v1)

**Summary:** Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summ...

---

### 8. Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens

**Authors:** Carl Edwards, Edward De Brouwer, Xiner Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11877v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11877v1)

**Summary:** Many biological discovery problems require experiments to be selected sequentially under constrained budgets. CRISPR screening is a prominent example, as exhaustive perturbation testing is often infeasible and candidate perturbations must instead be prioritized over multiple experimental rounds. Despite the importance of this problem, existing benchmarks for adaptive hit discovery remain limited in scale and diversity. Here, we introduce AssayBench-Loop, a large-scale benchmark for adaptive hit ...

---

### 9. On the Regularization Landscape for the Linear Recommendation Models

**Authors:** Dong Li, Zhenming Liu, Ruoming Jin, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11876v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11876v1)

**Summary:** Recently, a wide range of recommendation algorithms inspired by deep learning techniques have emerged as the performance leaders on several standard recommendation benchmarks. While these algorithms were built on different DL techniques (e.g., dropouts, autoencoder), they have similar performance and even similar cost functions. This paper studies whether the models' comparable performance are sheer coincidence, or they can be unified under a single framework. We find that all linear performance...

---

### 10. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

**Authors:** Yi Duan, Ying Liu, Zirui Tang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11873v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11873v1)

**Summary:** Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement. N...

---

### 11. RetroThinker: Enabling Retrospective Thinking in Speech LLMs

**Authors:** Yi-Jen Shih, Puyuan Peng, Abdelrahman Mohamed, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11864v1)

**Summary:** Speech large language models (SpeechLLMs) offer reduced latency and retain paralinguistic nuances that are typically lost in cascaded automatic speech recognition (ASR) and text-based LM architectures. However, they continue to lag behind text-only LLMs on complex reasoning tasks, while real-time spoken interaction imposes strict latency constraints. Although prior works employ Chain-of-Thought (CoT) and concurrent reasoning to enhance reasoning capabilities without inducing prohibitive delays, ...

---

### 12. Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models

**Authors:** Rodion Krjutškov, Eduard Barbu, Nikos Sakkas, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11860v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11860v1)

**Summary:** Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility managers and building operators to interpret. Explainable Artificial Intelligence (XAI) techniques address this opacity, but traditional XAI dashboards require substantial technical expertise and provide limited flexibility for dynamic, context-aware inquiry. Conversational XAI systems offer a promising ...

---

### 13. From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge

**Authors:** Wenkang Wei, Yuan Fang, Renhe Jiang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11859v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11859v1)

**Summary:** How does a language model's dependence on query-routing information and target knowledge change as it answers a question? We study this question through layerwise interventions on the hidden state at the end of the question. Across Qwen, Llama, and Gemma, we compare country-continent questions with noun, adjective, and code answers while keeping several fitted measurements distinct. A pair-conditioned request direction describes which country is queried in natural single-country questions; a glo...

---

### 14. Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport

**Authors:** Luyi Jia, Boyan Zhang, Yilun Liu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11842v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11842v1)

**Summary:** Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motivated by optimal transport, helps explain strong baselines but remains model-agnostic and ignores prediction error. Here we introduce a model-aware schedule construction based on fiberwise optimal transport. At a fixed time and state on the probability path, compatible signal/noise decompositions form...

---

### 15. Understanding Operator Attitudes Toward AI-Supported Decision Making in Maritime Operations

**Authors:** Doreen Jirak, Armeen Saroukanoff, Dirk van Rooy

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11805v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11805v1)

**Summary:** Maritime Autonomous Surface Ships (MASS) and AI- supported decision assistants are expected to transform maritime operations, but their safe integration depends on how maritime professionals perceive and trust such systems. This paper presents a survey study on maritime stakeholders' attitudes toward an AI-supported assistant in collision-avoidance scenarios. Participants evaluated technology anxiety, trust in automation, and explanation quality using established and adapted questionnaires, comp...

---

### 16. Logit Refiner: Improving Visual Autoregressive Models via Intra-Scale Dependency Modeling

**Authors:** Meimingwei Li, Stefan Andreas Baumann, Felix Krause, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11804v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11804v1)

**Summary:** Visual Autoregressive Models (VAR) generate images through next-scale prediction, producing all tokens within each scale in parallel. We show that this parallel decoding constitutes a mean-field-style approximation that discards spatial dependencies among same-scale tokens, causing locally incoherent samples regardless of backbone capacity -- a limitation of the decoding rule. Addressing this limitation, we introduce the Logit Refiner, a lightweight autoregressive module that restores intra-scal...

---

### 17. Thinking with Looped Flows

**Authors:** Ayhan Suleymanzade, Chanhyuk Lee, Floor Eijkelboom, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11801v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11801v1)

**Summary:** Humans and machines often solve harder problems by spending more time on computation. In deep learning, looped models implement this idea during inference by recurrently updating a hidden state. In practice, however, their training backpropagates through only one or a few updates, making it hard to train early updates to support future ones. We propose looped flows, an approach that sidesteps this issue by training the recurrence with local denoising objectives. By imposing temporal association ...

---

### 18. Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language Models on English Yoruba Code-Switched Speech

**Authors:** Chibuzor Okocha, Christan Earl Grant

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11786v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11786v1)

**Summary:** Automatic speech recognition (ASR) systems and audio language models (audio LMs) now report low error rates on monolingual benchmarks, but their behavior on code switched speech in low resource, diacritic rich languages remains poorly characterized. We present a switch aware evaluation of eleven modern systems (six ASR models and five audio LMs) on English Yoruba code-switched speech, using a deterministic 2000 utterance evaluation set and a shared scoring pipeline. Beyond word error rate (WER),...

---

### 19. Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving News Framing

**Authors:** Yi Liu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11769v1)

**Summary:** Large language models (LLMs) are increasingly used to analyze and rewrite news, yet current framing studies mainly evaluate generation, detection, or whether rewritten text appears more neutral. They do not directly show whether a model can undo a known framing transformation while keeping the facts fixed. We introduce a controlled inversion test over three established textual realizations of framing: evaluative lexis, agency realization, and information salience. Across 60 news articles and thr...

---

### 20. A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients

**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11768v1)

**Summary:** Per-token gating of forward/reverse KL losses has become a standard technique for on-policy knowledge distillation (OPD), but existing methods such as EOPD (Jin et al., 2026) and ToDi (Jung et al., 2025) each fix a single gating signal and a single gating direction, and the two have never been compared directly. We introduce a four-coefficient parameterization lambda_t = sigma(a * h_t + b * u(x) + c + d * gap_t) in which direction-aligned proxies of EOPD and ToDi appear as one-dimensional (1D) r...

---

### 21. SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control

**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11752v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11752v1)

**Summary:** For industrial content risk control, the real deployment constraint is not average accuracy but how much risk can be auto-handled under high precision and second-level latency. We present SIRF (Spec-Internalized Risk Foundation Model), which internalizes a platform's complex policies, synthesized without additional human annotation via EntiGraph, MAGA rewriting and account-level chain-of-thought (CoT), into the weights via continued pretraining (CPT), so rules are applied at high precision under...

---

### 22. LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation

**Authors:** Dongfang Zhao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11739v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11739v1)

**Summary:** Large language model serving costs scale directly with output sequence length, yet standard preference alignment often inflates response verbosity without improving utility. We study whether the parameterization of post-training updates affects generation length: low-rank subspaces alter sequence length without modifying the alignment loss. We present LOCUS, a method that selects a task-aware low-rank adaptation subspace to minimize output-token cost subject to a utility constraint. Within this ...

---

### 23. ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI

**Authors:** Zhengran Ji, Jonathan Hyun, Boyuan Chen

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11737v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11737v1)

**Summary:** Collective intelligence depends not only on the capabilities of individual members, but also on how those members are organized. Yet artificial multi-agent systems are typically assembled using fixed organizational structures, even when the physical tasks they perform impose fundamentally different coordination requirements. Here we show that principles from human organization theory can be operationalized to organize large, heterogeneous collectives of embodied artificial agents. We introduce O...

---

### 24. Continuous-Time Acoustic Modelling with Neural Controlled Differential Equations

**Authors:** Mattias Cross, Minghui Zhao, Anton Ragni

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11725v1)

**Summary:** Text-to-speech (TTS) models commonly address text--speech alignment by expanding phone-level encoder states to frame-level decoder inputs using predicted durations. While this length-regulation step resolves alignment structurally, this use of duration typically changes only where and how often latent states appear, not the values of the states themselves. This paper proposes a continuous-time mechanism for duration-aware acoustic modelling in TTS using neural controlled differential equations (...

---

### 25. A Time-Based Readout for Vector-Matrix Multiplication in Fully Analog Memristive SNNs

**Authors:** Elia Mateu-Barriendos, Álvaro Gómez-Pau, Josep Rius, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11713v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11713v1)

**Summary:** Artificial neural networks rely on vector-matrix multiplications (VMMs), whose implementation in von Neumann architectures is dominated by costly data movement between memory and processing units. Spiking neural networks (SNNs) mitigate this bottleneck by performing in-memory, analog VMMs using memristive crossbar arrays. However, conventional current-mode readout circuits incur significant area and power overhead.   This work proposes a fully analog readout architecture based on voltage-to-time...

---

### 26. When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making

**Authors:** Ken Chen, Wei Wang, Sachith Seneviratne, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11709v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11709v1)

**Summary:** When multiple LLM agents yield conflicting answers, the decision-making process dictates whether agent diversity improves performance or merely compounds shared errors. Existing collective decision-making methods, including voting, electoral rules, and LLM judges, rely on forward reasoning: they map evidence to labels in one direction. Although these methods can combine diverse forward traces, they still aggregate estimates that share this evidence-to-label factorization and can inherit correlat...

---

### 27. Language-Augmented Semantic Priors for B-Spline Surface Fitting

**Authors:** Yunzhong Lou, Yusheng Luo, Jiahao Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11708v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11708v1)

**Summary:** The use of B-splines and Non-Uniform Rational B-Splines surfaces constitutes the mathematical foundation of contemporary computer-aided design (CAD) systems. Despite long-term progress, geometric kernels in traditional CAD still rely heavily on predetermined heuristic initialization for surface fitting and parameterization. Meanwhile, the procedural semantics and design intent encoded in modeling histories are largely ignored during geometry generation. This disconnect creates a gap between high...

---

### 28. ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies

**Authors:** Jianming Ma, Rongjun Jin, Xiaxi Si, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11697v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11697v1)

**Summary:** Vision-Language-Action (VLA) and World-Action Models (WAMs) have demonstrated strong capabilities in general-purpose robotic manipulation, yet their generated actions may violate hard physical constraints and therefore be unsafe or infeasible for deployment. Existing safety approaches either optimize statistical safety objectives without deterministic per-step guarantees or correct unsafe actions only during inference, creating a mismatch between policy training and execution. We introduce ActSa...

---

### 29. COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization

**Authors:** Pingchen Lu, Xiangyi Wang, Xiang Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11682v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11682v1)

**Summary:** Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce \textbf{COBRA-Skills}, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, sele...

---

### 30. Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

**Authors:** Ruiqing Yue, Yu Cui, Zhuoyu Sun, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11677v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11677v1)

**Summary:** Self-evolving runtime harnesses can substantially improve the capabilities of large language model (LLM) agents and provide a promising paradigm for optimizing agent execution. Existing harness evolution methods typically rely on iterative search, repeatedly evaluating and revising candidate harnesses based on execution feedback from task instances. While this paradigm enables continuous harness optimization, it incurs substantial time overhead due to repeated agent executions and code modificat...

---

### 31. Geospatial AI, Dataverse Metadata, and the Study of Place-Based Government

**Authors:** Danny EBanks, Devika Jain

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11674v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11674v1)

**Summary:** Harvard Dataverse hosts over 150,000 research datasets, but the geographic information those datasets carry is entered as free text by depositors and has never been assembled into a searchable structure. We construct a knowledge graph from the repository's public data and metadata, organizing 102,650 datasets within a 215,985-node network of 528,003 edges linking datasets to keywords, publications, subjects, journals, and locations. Of those datasets, 43,991 (42.9 percent) carry at least one geo...

---

### 32. Warrant Theory

**Authors:** Khashayar Irani

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11667v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11667v1)

**Summary:** In this paper, we develop warrant theory as a philosophical discipline concerned with the inferential legitimacy of propositions within logical analysis. Warrant theory reconceptualises logic as a normative framework governing the conditions under which propositions may be introduced, accepted, rejected, and inferentially employed. Warrant is understood as inferential entitlement and is distinguished from truth, belief, and other psychological attitudes, while its relation to inferential use and...

---

### 33. Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents

**Authors:** Marica Notte, Ludovica Marinucci, Vieri Giuliano Santucci

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11660v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11660v1)

**Summary:** In recent years, artificial intelligence has made extraordinary progress thanks to large-scale models capable of generalization and the generation of complex outputs. However, transferring this potential into embodied agents reveals a significant limitation: the most advanced systems rely on pre-existing datasets and human feedback strategies that are powerful but insufficient in dynamic or unknown contexts. To adapt, an agent must acquire knowledge through direct interaction with its environmen...

---

### 34. ZipCodec: Ultra-Low-Frame-Rate Streaming Speech Coding

**Authors:** Luca Della Libera, Cem Subakan, Mirco Ravanelli

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11642v1)

**Summary:** Neural audio codecs are a fundamental component of modern speech generation systems. While recent codecs achieve increasingly low bitrates, reducing frame rate remains challenging, as each token must preserve more information while maintaining reconstruction quality. We present ZipCodec, a streaming neural speech codec operating at 6.25 Hz and 0.80 kbps with a theoretical latency of 160 ms. Our approach combines large-scale WavLM distillation with a redesigned transformer-based architecture, a s...

---

### 35. LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics

**Authors:** Mariia Baranova, Adrien Petralia, Etienne Le Naour, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11639v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11639v1)

**Summary:** The energy transition is reshaping residential electricity consumption through the increasing adoption of distributed generation, electrified appliances, and demand-response programs. Understanding these evolving behaviors requires access to granular smart-meter data for applications such as load forecasting, appliance detection, and demand-side flexibility analysis. However, such data are subject to strict access restrictions and data-protection regulations. Thus, realistic synthetic alternativ...

---

### 36. MAPLE: Memory-Augmented Planning with Language and Evolution

**Authors:** Kesheng Chen, Yamin Hu, Wenjian Luo

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11636v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11636v1)

**Summary:** Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support. LLM-based optimization agents translate natural-language requirements into models or solver programs that established optimization tools can execute. This progress makes optimization more accessible, but real-world operations are dynamic: changing demand, resources, and priorities require updates to data, constraints, and objectives. Methods centered on isolated requests of...

---

### 37. Physics-Informed Neural Networks to Infer the Perpendicular Energy Conductivity in the Scrape-Off Layer of Stellarator Devices

**Authors:** J. Gallego, P. Protopapas, A. Bustos, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11628v1)

**Summary:** In this work, we develop an inverse Physics-Informed Neural Network (PINN) framework to infer the dependence of the scrape-off layer (SOL) perpendicular heat conductivity on plasma density and temperature, $κ_\perp(n,T)$. The method combines radial profile measurements of electron density and temperature with the residual of a reduced one-dimensional SOL transport equation, so that the inferred conductivity is constrained by both the measurements and the underlying transport model. Three neural ...

---

### 38. Distributed Optimization of Modular Production Systems using Model-based Reinforcement Learning with Inverse Models

**Authors:** Andreas Schwung, Steve Yuwono, Sofiene Lassoued, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11615v1)

**Summary:** This paper presents a novel approach for data-driven self-learning control of highly flexible, modular manufacturing systems. Specifically, we employ a novel framework for model-based reinforcement learning which introduces approximate inverse process models within the training of reinforcement policies. This approach disentangles the learning of actuation dynamics and the dynamics in state space, resulting in RL-based training solely within the task space. We propose a lightweight feedforward a...

---

### 39. Making Alternative Data Work: Context-Augmented LLMs for Financial Forecasting

**Authors:** Jihoon Kwon, Lawrence Liu, Daekyung Park, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11607v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11607v1)

**Summary:** When forecasting a firm's future financial performance, alternative data - data collected from non-traditional sources such as consumer transactions, web traffic, and prediction markets - can provide timely signals about firms' operating activities and broader market conditions. These signals may reveal information that is not captured by traditional public sources and can therefore provide complementary information for forecasting firms' future financial performance. However, firm-level alterna...

---

### 40. Learn the Solid, Not the File: Canonical Inputs for Neural Networks on CAD Boundary Representations

**Authors:** Heinrich Jiang, Hager Yasser Mohamed, Alexander Hitt, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11573v1)

**Summary:** Boundary representation (B-rep) is the standard format used by modern CAD systems for parametric 3D models. It turns out, the exact same solid can be represented by different B-reps: for example, two engineers using different operations, a geometry kernel rebuilding the file, and an export setting repartitioning faces will lead to different B-reps even though the underlying solid remains the same.   We show that existing B-rep encoders are not robust to variation in the B-rep with the same solid...

---

### 41. Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)

**Authors:** Harshdeep Singh, Yurui Zhu, Giovanni Colavizza, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11569v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11569v1)

**Summary:** We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs perform text-to-SPARQL generation given only automatically derived structured metadata and small graph samples, rather than task-specific fine-tuning? We integrate VoID descriptions and ShEx schemas into a retrieval-augmented generation (RAG) pipeline and ablate KG-derived conte...

---

### 42. A Comparative Evaluation of Pre-trained Convolutional Neural Networks for Melanoma Detection

**Authors:** Wagner Moreno Schmitz, Marco Antonio de Castro Barbosa, Thiago Magalhães Amaral, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11550v1)

**Summary:** Early diagnosis of melanoma is critical for improving patient survival rates. However, accurately distinguishing melanoma from other skin lesions remains a significant clinical challenge due to the high visual similarity among lesion types and variability in image acquisition conditions. Artificial intelligence, particularly machine learning, has emerged as a promising tool to support dermatological diagnosis by automating feature extraction from medical images. Among the available approaches, c...

---

### 43. Characterizing Job Power Elasticity for Power-Flexible AI Training

**Authors:** Philip Colangelo, Charles Dawson, Shayan Sengupta, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11542v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11542v1)

**Summary:** Large language model (LLM) training is among the fastest-growing sources of electricity demand in modern data centers, and power availability is a primary bottleneck to continued AI infrastructure growth. Making the power consumption of these workloads flexible could unlock additional power for AI growth, limit increases in electricity prices, and improve the utilization of existing grid infrastructure. However, to realize this flexibility, we must first understand how the performance of trainin...

---

### 44. Prompt Revision as a Source of Cultural Bias in Text-to-Image Systems

**Authors:** Aleksandra Urman, Elsa Lichtenegger, Salima Jaoua, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11532v1)

**Summary:** Commercial text-to-image systems silently revise user prompts before generating images, a step users typically cannot disable or even see. Yet, existing audits of cultural bias examine only the final images and treat generation as a single pipeline, so they cannot tell where the bias originates. We introduce WORLDVIEW, a multilingual benchmark of 8,960 prompts across 15 languages and 31 language-context pairings. Using it, we audit the revision layer in three systems (DALL-E-3, Imagen-4, GPT-Ima...

---

### 45. Lightweight LiDAR-Based Cone Detection Framework Using Random Forest for Formula Student Driverless

**Authors:** Márk Mező-Kerekes, Péter Praksz, Chang Liu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11527v1)

**Summary:** Reliable, low-latency perception is crucial for Formula Student Driverless vehicles, yet many existing pipelines rely on deep learning and multi-sensor fusion, often requiring GPU acceleration. This paper presents a lightweight LiDAR-only perception pipeline tailored for CPU execution, combining ground removal, IMU-based motion compensation, DBSCAN clustering, and geometric feature-based Random Forest classification. Feature importance analysis reduced the model input from 12 to 7 features while...

---

### 46. Learning Interaction between Image and Layout Priors for Joint Image-Layout Generation in Design Templates

**Authors:** Shirong Yang, Bo Yang, Ying Cao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11519v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11519v1)

**Summary:** In this paper, we address the problem of graphic design template creation, which generates a background image and a layout of foreground elements over the background to form a harmonious composition from an input text.   Prior work on graphic design generation mostly adopts a sequential paradigm, where design elements are generated sequentially. We argue that such a sequential scheme falls short of faithfully capturing the dependency between the background and layout (and thus the joint image-la...

---

### 47. Extending SMT Solving with Non-Ground Clause Learning

**Authors:** Yasmine Briefs, Christoph Weidenbach

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11509v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11509v1)

**Summary:** Quantifier instantiation is currently the main approach to non-ground SMT solving: solvers generate ground instances and solve the resulting ground SMT problems with CDCL(T)-style reasoning. When a conflict is found, conflict analysis learns only a ground clause, even though the conflict comes from instances of non-ground clauses. Yet non-ground reasoning can give exponentially shorter proofs than purely ground reasoning. We propose a calculus that consists of ground instantiations, CDCL(T)-styl...

---

### 48. Structural priors for data-efficient language learning

**Authors:** Yana Veitsman, Jonas Mayer Martins, Jonathan Lautenschlager, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11505v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11505v1)

**Summary:** Efficient language learning requires methods to reduce the reliance on large data and computational resources. We investigate structural transfer: First training models on non-language data to induce useful priors for natural language. This approach is a form of weight initialization for multilingual language modeling. We evaluate transfer via next-token-prediction loss, weight shifts in the model, and downstream linguistic benchmarks. Several symbolic data types - notably music, probabilistic g...

---

### 49. ActMap: Single-Pass Uncertainty Quantification from Generation-Time Activation Maps

**Authors:** Jacopo Dardini, Roberta Calegari

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11498v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11498v1)

**Summary:** Practical uncertainty quantification (UQ) for large language models must decide,   from a single generation, whether a specific answer should be trusted. Existing   methods either sample multiple generations, read only output-token probabilities,   or reduce the model's internal computation to a single hidden state. We introduce   ActMap, a white-box representation that compresses the generation-time hidden-   state trajectory (every layer, every generated token) into a fixed $12 \times 32   \ti...

---

### 50. From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development

**Authors:** Reza Amirmoshiri, Faryad Sahneh, Yasser Jangjou

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11493v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11493v1)

**Summary:** Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. This knowledge is traditionally fragmented across functions and heterogeneous formats, causing traceability gaps and significant knowledge-management costs during technology transfer and regulatory filing. We present a modular agentic-AI platform that converts a heterogeneous corpus...

---

