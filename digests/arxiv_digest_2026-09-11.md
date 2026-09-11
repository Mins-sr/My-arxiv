# arXiv Daily Digest - 2026-09-11

Total papers: 350

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

## cs.CL

**50 papers**

### 1. Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

**Authors:** Atindra Jha, Margaret Li, Jure Leskovec, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11917v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11917v1)

**Summary:** As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert coun...

---

### 2. Distance generalization in transformers: why bother with positional encoding?

**Authors:** Daniel Henrik Nevermann, Claudius Gros

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11913v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11913v1)

**Summary:** Out-of-distribution length generalization, namely to extrapolate a task from short to longer context, has been studied intensively for transformers. Here we focus on distance generalization, which probes performance when inter-token distances are changed between training and inference, while keeping a fixed context length. We construct two synthetic delay copy tasks, both involving finite distances between source and recall, where tokens are copied either fully or selectively, and test models on...

---

### 3. MindTopo: Can Foundation Models Reason in Topological Space?

**Authors:** Yunfei Ge, Anbang Liu, Qineng Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11900v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11900v1)

**Summary:** Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity...

---

### 4. Nuha-Speech: Building General-Purpose Arabic Speech-LLMs

**Authors:** Yingzhi Wang, Reem Alhazzani, Muhammad Alqurishi

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11892v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11892v1)

**Summary:** As Speech Large Language Models (speech-LLMs) become increasingly multilingual, Arabic remains significantly underrepresented, highlighting the need for dedicated infrastructure to train and evaluate Arabic speech-LLMs.   To address this gap, we introduce Nuha-Speech, a comprehensive initiative to develop general-purpose Arabic speech-LLMs spanning dataset construction, model training, and systematic evaluation. Specifically, we constructed a large-scale Arabic Speech Question-Answering (SQA) co...

---

### 5. Domain-Specific Hallucination Detection in Large Language Models

**Authors:** Varun Teja Chundru, Debasmita Biswas

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11878v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11878v1)

**Summary:** Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summ...

---

### 6. Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens

**Authors:** Carl Edwards, Edward De Brouwer, Xiner Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11877v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11877v1)

**Summary:** Many biological discovery problems require experiments to be selected sequentially under constrained budgets. CRISPR screening is a prominent example, as exhaustive perturbation testing is often infeasible and candidate perturbations must instead be prioritized over multiple experimental rounds. Despite the importance of this problem, existing benchmarks for adaptive hit discovery remain limited in scale and diversity. Here, we introduce AssayBench-Loop, a large-scale benchmark for adaptive hit ...

---

### 7. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

**Authors:** Yi Duan, Ying Liu, Zirui Tang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11873v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11873v1)

**Summary:** Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement. N...

---

### 8. Augustinian BabyLM: What Ostensive Definition Can and Cannot Teach a Small Language Model

**Authors:** Lisa Bylinina

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11870v1)

**Summary:** A language model normally begins training with random word embeddings: whatever 'banana' means must be learned from training corpora. I implement St. Augustine's picture of word learning, meaning by ostension, for a small masked language model (DeBERTa) trained on 10M words: before training, visually grounded tokens receive embeddings derived from the image regions they label; other tokens start random. Visual initialization leaves a measurable imprint that lasts until the end of training. At th...

---

### 9. Epistemic orientation predicts legislative effectiveness among members of the US Congress

**Authors:** Segun Aroyehun, Stephan Lewandowsky, David Garcia

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11865v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11865v1)

**Summary:** Truth and evidence-based communication provide important foundations for democratic governance, accountability, and collective decision-making. Prior work shows that evidence-oriented language in US congressional floor speeches has declined since the mid-1970s, alongside broader changes in legislative productivity and polarization. This study shifts the analysis from congressional sessions to individual members of Congress to examine whether epistemic orientation varies systematically across leg...

---

### 10. RetroThinker: Enabling Retrospective Thinking in Speech LLMs

**Authors:** Yi-Jen Shih, Puyuan Peng, Abdelrahman Mohamed, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11864v1)

**Summary:** Speech large language models (SpeechLLMs) offer reduced latency and retain paralinguistic nuances that are typically lost in cascaded automatic speech recognition (ASR) and text-based LM architectures. However, they continue to lag behind text-only LLMs on complex reasoning tasks, while real-time spoken interaction imposes strict latency constraints. Although prior works employ Chain-of-Thought (CoT) and concurrent reasoning to enhance reasoning capabilities without inducing prohibitive delays, ...

---

### 11. IndicTriMix: Developing Language Identification Datasets and Models for Tri-Language Code-Mixing

**Authors:** Pruthwik Mishra, Rudra Trivedi, Avi Patel, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11851v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11851v1)

**Summary:** Language identification in code-mixed text, largely observed in social media, is highly essential when users frequently switch between multiple languages within a single utterance. Accurately identifying the languages of code-mixed tokens becomes an urgent necessity. Traditional language identification models, designed for monolingual text, are not well suited for token-level language identification in code-mixed settings. We formulate the task as a sequence labeling problem and fine-tune contex...

---

### 12. Target leakage, not model class, explains reported accuracy in survey-based cardiovascular screening: a leakage-tiered audit of glass-box and tabular foundation models

**Authors:** Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11838v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11838v1)

**Summary:** Cardiovascular screening models trained on national health surveys routinely report areas under the receiver operating characteristic curve (AUROC) near 0.89. We asked whether that accuracy reflects learning or target leakage, whether tabular foundation models change the answer, and whether the properties deployment requires survive joint examination. We benchmarked ten classifiers spanning linear, tree-ensemble, neural, glass-box, and tabular foundation classes for prevalent myocardial infarcti...

---

### 13. SpecGuard: Inference-Time Backdoor Detection For Free

**Authors:** Rui Wen, Ahmed Salem, Andrew Paverd, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11799v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11799v1)

**Summary:** Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about t...

---

### 14. Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language Models on English Yoruba Code-Switched Speech

**Authors:** Chibuzor Okocha, Christan Earl Grant

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11786v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11786v1)

**Summary:** Automatic speech recognition (ASR) systems and audio language models (audio LMs) now report low error rates on monolingual benchmarks, but their behavior on code switched speech in low resource, diacritic rich languages remains poorly characterized. We present a switch aware evaluation of eleven modern systems (six ASR models and five audio LMs) on English Yoruba code-switched speech, using a deterministic 2000 utterance evaluation set and a shared scoring pipeline. Beyond word error rate (WER),...

---

### 15. Whisper-Based Speech Transcription from Videos Across Multiple Languages for Cross-Cultural Understanding

**Authors:** Michael Picheny

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11772v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11772v1)

**Summary:** Cross-cultural understanding has become increasingly important in today's highly connected, cross-national world. The success of LLM-based technologies is now driving the development of automated tools to aid understanding for nonnative people trying to succeed in cross-cultural environments. Building such automated tools is often done by leveraging in-thewild text, audio, and video data. This paper presents techniques for improving speech recognition-based transcript creation in multiple langua...

---

### 16. The widening evaluation gap in medical large language model research 2023 to 2026

**Authors:** Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11770v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11770v1)

**Summary:** Large language models are superseded every few quarters; clinical evidence takes years. We asked whether medical research is keeping pace with the systems it evaluates. PubMed returned 11,628 records for January 2023 to June 2026 across fourteen clinical domains, growing 45-fold; 2.5% used a randomised, controlled or prospective design. Evaluation lag, from a study's newest named model release to its own publication, widened from 1.33 to 6.08 quarters. Because discontinued models age mechanicall...

---

### 17. Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving News Framing

**Authors:** Yi Liu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11769v1)

**Summary:** Large language models (LLMs) are increasingly used to analyze and rewrite news, yet current framing studies mainly evaluate generation, detection, or whether rewritten text appears more neutral. They do not directly show whether a model can undo a known framing transformation while keeping the facts fixed. We introduce a controlled inversion test over three established textual realizations of framing: evaluative lexis, agency realization, and information salience. Across 60 news articles and thr...

---

### 18. A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients

**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11768v1)

**Summary:** Per-token gating of forward/reverse KL losses has become a standard technique for on-policy knowledge distillation (OPD), but existing methods such as EOPD (Jin et al., 2026) and ToDi (Jung et al., 2025) each fix a single gating signal and a single gating direction, and the two have never been compared directly. We introduce a four-coefficient parameterization lambda_t = sigma(a * h_t + b * u(x) + c + d * gap_t) in which direction-aligned proxies of EOPD and ToDi appear as one-dimensional (1D) r...

---

### 19. Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs

**Authors:** Jordi Luque, Fernando López, Aleix Sant

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11762v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11762v1)

**Summary:** Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder differ by an order of magnitude in update norm. Single-pool per-layer methods suffer \emph{cross-component budget collapse}, dragging word error rate (WER) far from flat global clipping or collapsing ...

---

### 20. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

**Authors:** Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11758v1)

**Summary:** Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corpor...

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

### 23. The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge

**Authors:** Jordi Luque, Lorenzo Concina, Marco Matassoni, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11724v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11724v1)

**Summary:** This paper details the Eloquence team's approach to Task 2 of the 2nd MLC-SLM challenge at Interspeech 2026, which involves multilingual Multiple-Choice Question Answering (MCQA) across 21 languages. Three approaches are explored. First, we fine-tune Voxtral-Mini-3B via LoRA with cross-lingual data augmentation, ASR transcript augmentation and timestamp-aware audio cropping, achieving 0.72 macro-accuracy on evaluation Phase 2. Second, we apply multimodal in-context learning (ICL) to the frozen V...

---

### 24. Why Does Post-Training Quantization Work?

**Authors:** Yuxiang Chen, Michael Beyer, Jun Zhu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11716v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11716v1)

**Summary:** Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states. Naively, these errors should accumulate with depth and corrupt next-token prediction; randomly initialized models accumulate these discrepancies rapidly, whereas quantized pretrained models accumulate much less hidden-state error and largely maintain downstream task performance, even though they were never trained ...

---

### 25. Negative Self-Distillation: Learning to Reason by Avoiding Flaws

**Authors:** Rongcan Pei, Zhepei Wei, Shuyao Xu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11699v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11699v1)

**Summary:** On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expres...

---

### 26. Structured Transforms for Low-Overhead Quantization of Language Models

**Authors:** Daria Cherniuk, Alexander Rudikov, Boris Kashin, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11687v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11687v1)

**Summary:** We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms. The method retains the core factorization of each weight into two components -- one with bounded infinity norm and the other with bounded infinity norm after an orthogonal transformation -- but replaces the dense random orthogonal matrix with a sign-randomized Discrete Cosine Transform (DCT), re...

---

### 27. A Training-Free, Alignment-Free Approach to Corporate Intelligence: Application to SEC Filings

**Authors:** Jean-François Delpech

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11620v1)

**Summary:** High-dimensional dense text embeddings and large language models face real obstacles in financial-disclosure analysis: context-window limits, hallucination risk, high computational cost, and the arbitrary rotation of vector spaces across independently trained models. We present a training-free, alignment-free framework for corporate intelligence built on deterministic sparse seed vectors. Hashing word strings into a fixed high-dimensional basis places all documents and all temporal epochs in a c...

---

### 28. Complex-Text Robustness Evaluation and Failure Diagnosis for Low-Resource Multilingual Text-to-Speech

**Authors:** Tianlun Zuo, Ziyu Zhang, Tingzhi Mao, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11545v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11545v1)

**Summary:** Low-resource multilingual text-to-speech (TTS) systems have expanded language coverage, but their robustness under complex text inputs remains insufficiently diagnosed. Existing evaluations mainly focus on naturalness, speaker similarity, and content consistency using regular test sentences, while providing limited insight into how multilingual TTS systems fail when handling challenging inputs such as numbers, dates, named entities, long sentences, code-switched expressions, and punctuation-rela...

---

### 29. Structural priors for data-efficient language learning

**Authors:** Yana Veitsman, Jonas Mayer Martins, Jonathan Lautenschlager, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11505v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11505v1)

**Summary:** Efficient language learning requires methods to reduce the reliance on large data and computational resources. We investigate structural transfer: First training models on non-language data to induce useful priors for natural language. This approach is a form of weight initialization for multilingual language modeling. We evaluate transfer via next-token-prediction loss, weight shifts in the model, and downstream linguistic benchmarks. Several symbolic data types - notably music, probabilistic g...

---

### 30. ReGround: Grounding Reviewer Comments in Multimodal Evidence

**Authors:** Serwar Basch, Lizhen Qu, Iryna Gurevych

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11460v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11460v1)

**Summary:** Reviewer comments naturally relate to specific parts of the reviewed paper, yet grounding these comments to the underlying evidence is difficult due to long multimodal documents. Existing benchmarks do not capture this setting and largely focus on explicit, information-seeking queries. We introduce ReGround, a large-scale dataset for reviewer comment grounding that links 10,267 reviewer comments to 16,274 evidence in the original anonymous submission of 3,656 papers. We build on a simple observa...

---

### 31. Cross-Lingual Clinical Annotation Projection as Constrained Text Generation: A Six-Language Study

**Authors:** Álvaro Rey-Blanes, Francisco J. Moreno-Barea, Francisco J. Veredas

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11450v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11450v1)

**Summary:** Background: To determine whether cross-lingual clinical annotation projection can be formulated as a text-preserving, document-level generative task that produces verifiable character-level annotations for multilingual clinical corpus construction, and to characterize its robustness and computational trade-offs relative to candidate-based projection pipelines. Methods: We developed a constrained LLM projection workflow that inserts entity tags directly into immutable target-language text, follow...

---

### 32. SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations

**Authors:** Yu Wang, Yuchen Li, Rui Kong, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11414v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11414v1)

**Summary:** Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model. Although existing routers are effective in single-turn settings, they do not directly transfer to multi-turn dialogue, where routing performance critically depends on how historical context is segmented, retained, and incorporated into the current prompt. This introduces two fundamental challenges: preventing information loss and information confusion during cont...

---

### 33. TransClean: A Benchmark for Detecting and Extracting Clean Translations from Large Language Model Outputs

**Authors:** Shenbin Qian, Yves Scherrer

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11399v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11399v1)

**Summary:** Large language models (LLMs) are increasingly used for machine translation, yet their outputs often contain additional text beyond the translation itself, such as language labels, explanations or bilingual repetitions, which we term translation noise. Despite its prevalence, this problem lacks dedicated benchmarks and systematic study. We analyze over 790,000 translation outputs from 12 LLMs across 22 language pairs (LPs) and identify 12 recurring noise patterns, which we group into formatting a...

---

### 34. VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents

**Authors:** Peiyuan Gao, Gaoyuan Zhang, Haojie Qin, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11390v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11390v1)

**Summary:** State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present {\sf VikingRAG}, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. To further reduce token overhead of multi-ro...

---

### 35. SEAR: Segment-Evidence-Aware Routing for Weak-to-Strong Multilingual Speech MCQ

**Authors:** Huy Hoang Le, Long-Bao Nguyen, Minh Tri Dao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11355v1)

**Summary:** This paper describes our system for Task~2 of the second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge. We adapt Qwen3-Omni-30B-A3B-Instruct with a segment-evidence-aware data and post-training pipeline. A language model converts timestamped ASR into coherent event spans, which are expanded by a boundary margin and cropped from the original recording. We then synthesize complementary semantic MCQs with Qwen3.6-27B and acoustic MCQs with Gemini~3.1 Flash-Lite, followed by ...

---

### 36. On the Impact of Anonymization on the Performance of Large Language Models

**Authors:** Tobias Deußer, Max Hahnbück, Lorenz Sparrenberg, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11335v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11335v1)

**Summary:** As large language models are increasingly deployed in sensitive domains, anonymizing input data to protect personally identifiable information has become a critical practice. However, the impact of this anonymization on model utility is not well understood. This paper presents a systematic empirical study of the trade-off between privacy and performance. We evaluate five prominent language models across eleven diverse benchmarks, comparing their performance on original versus pseudonymized input...

---

### 37. E-CONAN (Entailment, CONtradition And Neutral) Benchmarks: Arabic Textual Entailment and Natural Inference Datasets

**Authors:** Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11334v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11334v1)

**Summary:** Natural Language Inference processes pairs of sentences to extract their semantic relations. NLI has been a hot research topic, integrated as a main component in other NLP applications. Despite significant advancements in textual inference across various languages all around the world, Arabic language still suffers from limited resources in this domain. To address this gap, this paper introduces E-CONAN benchmarks that are composed of sentences pairs from various sources: (1) automatically-trans...

---

### 38. The Semantic Elevation Operator and the Closure of the Undecidable Class under Preservation

**Authors:** Jose Pascual Gumbau Mezquita

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11326v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11326v1)

**Summary:** The undecidability of a program's static semantic properties is governed by Rice's theorem. Self-modifying systems, however, require analysing not whether a property holds now, but whether it is preserved when the system rewrites itself. We formalise this transition through a semantic elevation operator ΛΦ, which turns the static question "does x satisfy P?" into the dynamic question "is P preserved after x is transformed by Φ?". We prove that when Φ is intensional (depending on the source code,...

---

### 39. MultiHuSE: A Multimodal Dataset for Humour Styles and Emotions

**Authors:** Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11322v1)

**Summary:** Computational recognition of verbal humour remains a challenging task, requiring an understanding of language, delivery style, emotions, and cultural context. Most existing approaches focus on binary classification and lack datasets that capture psychological dimensions of humour alongside variations in expression. We introduce MultiHuSE, a multimodal dataset comprising 2,407 high-definition videos of 50 demographically diverse actors performing 1,463 text samples across four psychological humou...

---

### 40. Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation

**Authors:** Maria Frangiadaki, Dimitrios Damianos, Kosmas Kritsis, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11302v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11302v1)

**Summary:** Automatic Lyric Transcription (ALT) remains substantially more challenging than speech recognition due to melodic variability, rhythmic irregularity, and accompaniment interference. This is heightened in low-resource languages like Greek, where no prior benchmark for ALT exists. We present the first controlled study of Whisper adaptation for Greek ALT, investigating model scaling effects, task composition via multitask training in transcribe-translate ratios, and two-stage speech-to-singing adap...

---

### 41. Xiaomi-CocktailASR-1 Technical Report

**Authors:** Yiru Zhang, Hang Su, Lichun Fan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11274v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11274v1)

**Summary:** Recently, large language model (LLM) based ASR models have achieved significant progress, yet they generally lack support for multi-speaker scenarios, where the cocktail party problem remains a critical bottleneck for further advancing ASR. Existing TS-ASR methods, including end-to-end architectures with speaker embeddings and latest LLM-based explorations suffer from degraded single-speaker performance and the inability to reject when the target speaker is absent. In this paper, we propose Xiao...

---

### 42. INDRA: A New AI Tool for Exploring Tobacco, Fossil Fuel, and Chemical Industry Archives

**Authors:** Daniel Akselrad, Robert N. Proctor

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11261v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11261v1)

**Summary:** Five decades of litigation have disgorged hundreds of millions of pages of formerly secret business records from the tobacco industry, along with documents from the makers of drugs, chemicals, food, firearms, and fossil fuels. Yet these archives have been effectively inaccessible to general-purpose large language models (LLMs) because they have never been compiled into an LLM-readable corpus. Chatbots may be familiar with some of the materials contained in such archives but, with no direct acces...

---

### 43. MUtE: A Dual Framework for Concept Erasure and Counterfactual Interventions

**Authors:** Antoine Saillenfest

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11253v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11253v1)

**Summary:** Erasing concept-specific information from representations has been proven useful for mitigating bias or interpreting model decisions. The joint objective is to transform the original representations such that the target concept becomes unpredictable, while maximally preserving concept-unrelated information. In this work, we revisit the optimal bounds of concept erasure to derive a novel class of erasure functions that naturally induce a deterministic, dual counterfactual mapping. Bridging the ga...

---

### 44. The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods

**Authors:** Ioanna Kaffeza, Efthymios Georgiou, Alexandros Potamianos

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11247v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11247v1)

**Summary:** Multimodal Sentiment Analysis (MSA) remains constrained by modality imbalance, yet the field continues to rely on optimization-based balancing methods that promise more than they deliver. We provide three contributions: 1) a unified evaluation framework testing gradient and loss-based balancing strategies under controlled settings; 2) a theoretical diagnosis explaining why these methods fail, as they conflate fitting speed with discriminative contribution; and 3) a research agenda toward held-ou...

---

### 45. Assessing the Reusability of Public Speech Resources for Low-Resource Languages: A Central Kurdish Case Study

**Authors:** Hiwa Asadpour

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11246v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11246v1)

**Summary:** Kurdish is spoken by millions of people, but little technology can read it aloud. A recent study released three Kurdish voices, 35 hours of recorded speech, and a paper describing the work, all free to download. This review checks how well those public files match the paper. The research is careful about its limits, but the files contain several problems: a settings file lists equipment that was never used, test recordings are left unlabeled among training data, and a coding fault mishandles lon...

---

### 46. OmniHallu: Unified Hallucination Detection for Cross-Modal Comprehension and Generation in Multimodal Large Language Models

**Authors:** Jianjiang Yang, Peihang Li, Shanqing Xu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11244v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11244v1)

**Summary:** While Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse tasks, they suffer from hallucinations where generated outputs contradict or misrepresent input semantics. Existing research typically addresses hallucination detection within a single modality or task type, limiting generalizability. We introduce OmniHallu, a unified hallucination detection framework spanning both comprehension and generation tasks across image, video, and audio modalities. We contri...

---

### 47. A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies

**Authors:** Tianxiang Zhou

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11231v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11231v1)

**Summary:** This paper presents SurgicalRoomAgent, a voice-interactive multi-agent system for smart operating rooms based on large language models (LLMs). The system achieves natural language understanding, device control, intraoperative recording, and surgical report generation through a layered architecture comprising a voice interaction pipeline (wake, ASR, turn detection, agent reasoning, TTS) and an agent core (skill registry, task planner, device manager). Three key technologies are investigated: (1) ...

---

### 48. REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving

**Authors:** Tuan Nguyen, Qiran Hu, Banruo Liu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11209v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11209v1)

**Summary:** Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memory, and token cost. Post-retrieval compression can reduce this cost, yet existing compressors often operate independently for each query, rely on auxiliary models or rewriting, and introduce online overhead that can offset the benefit of shorter prompts. We revisit RAG compressio...

---

### 49. Automated Identification of Competing Narratives in Political Discourse on Social Media

**Authors:** Sergej Wildemann, Erick Elejalde

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11202v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11202v1)

**Summary:** Social media platforms have become central to shaping political discourse, serving as arenas where narratives form and evolve, influencing public opinion. Identifying and analyzing these narratives, particularly when they compete across different political ideologies, is crucial for understanding the dynamics of modern political communication. This paper presents an unsupervised framework for identifying and characterizing competing narratives in political discourse on social media, focusing on ...

---

### 50. (Whose defaults?) Is artificial intelligence reorienting archaeological methods?

**Authors:** Lorenzo Cardarelli, Roberto Ragno

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11198v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11198v1)

**Summary:** Generative AI and the practice of "vibe coding" are changing how archaeologists carry out computational research, but their effects on the discipline's range of methods is still understudied. In this paper, we evaluate whether large language models (LLMs) are narrowing the variety of methods archaeologists use. We first analysed approximately 119,000 archaeology abstracts from Scopus, covering publications from 2010 to 2025. Using a locally run LLM, we identified the computational methods report...

---

## cs.CV

**50 papers**

### 1. SenseNova-U1.5: Towards Native Unified Visual Intelligence

**Authors:** Haiwen Diao, Jiahao Wang, Chenjing Ding, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11929v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11929v1)

**Summary:** We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K. For post-training, we optimize specialized experts for visual aesthe...

---

### 2. MindTopo: Can Foundation Models Reason in Topological Space?

**Authors:** Yunfei Ge, Anbang Liu, Qineng Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11900v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11900v1)

**Summary:** Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity...

---

### 3. Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding

**Authors:** Weitong Cai, Hang Zhang, Yukai Huang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11899v1)

**Summary:** Long-video understanding on edge devices must reason over hours of content under tight compute and bandwidth budgets. Subsampling visual tokens loses temporal structure, while text-only video memories lose fine-grained visual attributes. We observe a visual-textual duality: language memories carry long-range temporal structure better than dense frames, while pixels remain decisive for attribute-level perception. Building on this insight, we propose Caption-once, Frames-onDemand (CFD), a budget-a...

---

### 4. 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11894v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11894v1)

**Summary:** Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast bu...

---

### 5. Guided Super-Resolution of Digital Elevation Models with Diffusion-Based Image Generators

**Authors:** Armand Mihai Nicolicioiu, Dominik Narnhofer, Nando Metzger, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11886v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11886v1)

**Summary:** High-resolution digital surface models (DSMs) play an important role in urban analysis, 3D building reconstruction, and infrastructure monitoring, yet their availability remains limited due to the high cost and complexity of data acquisition. In contrast, coarse DSMs from commercial satellite missions are widely accessible, and high-resolution optical imagery is increasingly available from aerial and satellite platforms. We address the resulting mismatch in spatial resolution and propose a DSM s...

---

### 6. CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search

**Authors:** Yifan Yang, Zhaoyan Wang, Zheng Gao, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11884v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11884v1)

**Summary:** Zero-cost proxies rank architectures cheaply, but their reliability varies across search spaces. We introduce CoRA-NAS (COarse Ranking + Anchor-residual), a two-stage framework combining a static ranking prior with low-cost learning-curve refinement. CoRA-Rank aggregates capacity and structure-at-initialization proxies through an equal-weight log-rank consensus and a target-free consensus gate. CoRA-Refine samples anchors across this prior, extrapolates their early validation curves, and propaga...

---

### 7. Logit Refiner: Improving Visual Autoregressive Models via Intra-Scale Dependency Modeling

**Authors:** Meimingwei Li, Stefan Andreas Baumann, Felix Krause, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11804v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11804v1)

**Summary:** Visual Autoregressive Models (VAR) generate images through next-scale prediction, producing all tokens within each scale in parallel. We show that this parallel decoding constitutes a mean-field-style approximation that discards spatial dependencies among same-scale tokens, causing locally incoherent samples regardless of backbone capacity -- a limitation of the decoding rule. Addressing this limitation, we introduce the Logit Refiner, a lightweight autoregressive module that restores intra-scal...

---

### 8. Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need

**Authors:** Margaret Kostyrko, Yuxuan Xue, Garvita Tiwari, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11722v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11722v1)

**Summary:** The representation of 3D clothed humans as standardized 2D UV texture and displacement maps over an underlying body model has long been studied. This compact representation is enticing as it enables pretrained image networks to process, generate, and edit 3D avatars, but is only useful if scans are accurately aligned and brought into correspondence via high-fidelity registration. This prerequisite has never been met, which we argue explains the limited quality of prior UV-based methods for cloth...

---

### 9. MC-DeTra: Motion-Consistent Joint Object Detection and Socially-Aware Trajectory Forecasting in Bird's-Eye-View Images

**Authors:** Vladislav Diuzhev, Dmitry Yudin

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11717v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11717v1)

**Summary:** Unified models for object detection and trajectory forecasting aim to merge perception and prediction for autonomous driving, refining actor trajectories directly over shared bird's-eye-view (BEV) images rasterized from LiDAR and high-definition maps. Their accuracy on dynamic, moving actors, however, remains the hardest part of the task, and the strongest such model, DeTra, has no public implementation. We contribute an openly released DeTra reimplementation with documented approximations, and ...

---

### 10. Language-Augmented Semantic Priors for B-Spline Surface Fitting

**Authors:** Yunzhong Lou, Yusheng Luo, Jiahao Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11708v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11708v1)

**Summary:** The use of B-splines and Non-Uniform Rational B-Splines surfaces constitutes the mathematical foundation of contemporary computer-aided design (CAD) systems. Despite long-term progress, geometric kernels in traditional CAD still rely heavily on predetermined heuristic initialization for surface fitting and parameterization. Meanwhile, the procedural semantics and design intent encoded in modeling histories are largely ignored during geometry generation. This disconnect creates a gap between high...

---

### 11. Spectral Adapters for Segment Anything Model-based Segmentation of Colorectal Liver Metastases in Computed Tomography

**Authors:** Ramtin Mojtahedi, Mohammad Hamghalam, Jacob J. Peoples, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11703v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11703v1)

**Summary:** Accurate segmentation of colorectal liver metastases (CRLM) in contrast-enhanced computed tomography (CT) is important for response assessment, surgical planning, and follow-up. We propose two parameter-efficient spectral adapters for the Segment Anything Model (SAM): the Directional Spectral Adapter (DiSECT) and Spectral Instance-Guided Adapter (SiGA). DiSECT uses singular value decomposition of frozen weights to constrain residual updates to leading spectral directions, while SiGA adds global ...

---

### 12. Single-Stream Multi-Feature Fusion with Temporal Robustness for Gait Emotion Recognition

**Authors:** Shirong Lyu, Silu Quan, Yixuan Ding, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11680v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11680v1)

**Summary:** 3D skeleton-based gait emotion recognition faces high annotation costs, data scarcity, and poor generalization on heterogeneous data. This paper proposes SV-GCN, a single-stream multi-feature fusion framework with temporal invariance. We introduce intra-frame relative motion features to eliminate frame-rate sensitivity and embed heterogeneous cues at shallow layers, enabling early fusion without multi-stream complexity. For variable-length sequences, we design a global mask-guided valid-frame sp...

---

### 13. Multimodal Taxonomic Conditioning for Generative Plankton Imagery

**Authors:** Daniela Ivanova, Ozgu Goksu, Nicolas Pugeault

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11673v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11673v1)

**Summary:** Automated plankton imaging produces severely long-tailed datasets, where the rare taxa of greatest ecological interest have too few images to train or evaluate classifiers reliably. We generate synthetic plankton imagery conditioned on taxonomy: a CLIP encoder is adapted on a large plankton corpus with a ranked contrastive objective extended to deep, ragged taxonomies, then frozen to condition a parameter-efficient diffusion transformer. We evaluate synthetic sample quality on distributional fid...

---

### 14. Self-Supervised Cardiac Phase Detection via Single-Parameter Latent Orbits

**Authors:** John Bonnici, Matthew Baugh, Aleksandra Kulbaka, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11650v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11650v1)

**Summary:** Accurate identification of end-diastole (ED) and end-systole (ES) in echocardiography underpins the quantification of ventricular function, yet manual selection of these key frames is subjective and introduces clinically significant inter-operator variability. Recent self-supervised methods either prescribe strict periodic trajectories or learn an unconstrained low-dimensional motion subspace from reconstruction or registration objectives. The former offers interpretability but imposes restricti...

---

### 15. Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation

**Authors:** Jintao Zhang, Kai Jiang, Jintao Chen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11638v1)

**Summary:** We present Vidu S2, which comprises Vidu S2-Avatar, a real-time interactive digital-character model, and Vidu S2-Editing, a real-time video editing model. Moreover, we explore the feasibility of real-time spatial video generation for both Vidu S2-Avatar and Vidu S2-Editing. Compared with Vidu S1, Vidu S2-Avatar supports real-time 720p video generation, generation with dynamic references that can be updated at any moment, and stronger instruction following, such as dancing. Vidu S2-Editing suppor...

---

### 16. LangStreet: Persistent Language Fields for Anchor-Decoded Street Gaussians

**Authors:** Runyi Yang, Deheng Zhang, Xiaoye Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11616v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11616v1)

**Summary:** Language Gaussian fields implicitly assume that the primitive carrying semantics remains identifiable across views. This assumption breaks in scalable anchor-decoded representations, where persistent anchors generate view-conditioned child Gaussians whose geometry and appearance vary with the camera. We introduce Ours, a persistent language field for such structured Gaussian scenes. Our key idea is semantic ownership: transient children route observations, while persistent decoder slots and thei...

---

### 17. MMGait: Benchmarking and Unifying Gait Recognition across Heterogeneous Modalities

**Authors:** Saihui Hou, Chenye Wang, Qingyuan Cai, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11601v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11601v1)

**Summary:** Gait recognition is commonly studied using RGB videos or their derived silhouettes and poses. Yet human walking produces heterogeneous photometric, geometric, and motion cues that cannot be systematically examined with RGB-centered benchmarks. We present MMGait, a large-scale multi-sensor benchmark that brings visible, infrared, depth, LiDAR, and radar observations into sequence-level correspondence. It provides diverse modalities spanning appearance, contours, geometry, motion, and body structu...

---

### 18. OmniKVQuant: KV Cache Quantization for Omni-LLMs

**Authors:** Suho Yoo, Hyunjong Ok, Jongmin Choi, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11582v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11582v1)

**Summary:** As Omni-modal large language models (Omni-LLMs) take in audio, video and text together, their KV cache memory cost grows. KV cache quantization is the de facto approach in text-only LLMs, but its application to Omni-LLMs remains unexplored. In this paper, we analyze how TurboQuant, a representative rotation-based KV cache quantization method, behaves on multimodal caches and identify two critical issues: temporal key drift and heterogeneous value geometry. To address these, we propose OmniKVQuan...

---

### 19. Learn the Solid, Not the File: Canonical Inputs for Neural Networks on CAD Boundary Representations

**Authors:** Heinrich Jiang, Hager Yasser Mohamed, Alexander Hitt, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11573v1)

**Summary:** Boundary representation (B-rep) is the standard format used by modern CAD systems for parametric 3D models. It turns out, the exact same solid can be represented by different B-reps: for example, two engineers using different operations, a geometry kernel rebuilding the file, and an export setting repartitioning faces will lead to different B-reps even though the underlying solid remains the same.   We show that existing B-rep encoders are not robust to variation in the B-rep with the same solid...

---

### 20. A Comparative Evaluation of Pre-trained Convolutional Neural Networks for Melanoma Detection

**Authors:** Wagner Moreno Schmitz, Marco Antonio de Castro Barbosa, Thiago Magalhães Amaral, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11550v1)

**Summary:** Early diagnosis of melanoma is critical for improving patient survival rates. However, accurately distinguishing melanoma from other skin lesions remains a significant clinical challenge due to the high visual similarity among lesion types and variability in image acquisition conditions. Artificial intelligence, particularly machine learning, has emerged as a promising tool to support dermatological diagnosis by automating feature extraction from medical images. Among the available approaches, c...

---

### 21. World in World: Explore the World with World Models

**Authors:** Chenxi Song, Yanming Yang, Chi Zhang

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11548v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11548v1)

**Summary:** Autoregressive video world models enable interactive, long-horizon exploration, but flexible control remains challenging. Exploring a source video from new viewpoints requires the generated rollout to remain synchronised with the recorded event, place observed content in the requested view, plausibly complete newly exposed regions, and recover previously generated appearance on revisits. Existing methods typically address these requirements through task-specific modules or additional training. W...

---

### 22. Learning Interaction between Image and Layout Priors for Joint Image-Layout Generation in Design Templates

**Authors:** Shirong Yang, Bo Yang, Ying Cao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11519v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11519v1)

**Summary:** In this paper, we address the problem of graphic design template creation, which generates a background image and a layout of foreground elements over the background to form a harmonious composition from an input text.   Prior work on graphic design generation mostly adopts a sequential paradigm, where design elements are generated sequentially. We argue that such a sequential scheme falls short of faithfully capturing the dependency between the background and layout (and thus the joint image-la...

---

### 23. Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based Neuroevolution

**Authors:** Romain Claret, Arthur Gygax, Michael O'Neill, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11518v1)

**Summary:** Evolvable-Substrate HyperNEAT (ES-HyperNEAT), a bio-inspired indirect encoding that determines neuron placement and connection weights from spatial coordinates, exhibits a failure mode on MNIST as a diagnostic benchmark. Because input pixels map to a coordinate space centered at the origin, evolved networks converge on a small central cluster of input pixels, a spatial-concentration bias; prior work observed only 21% mean accuracy in this regime. Is this bias an optimization artifact or an archi...

---

### 24. LoopVAE: Recurrent Depth Across Scales for Visual Tokenization

**Authors:** Zhiying Lu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11516v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11516v1)

**Summary:** Hierarchical visual tokenizers typically allocate different processing blocks to different spatial scales. We ask how much of this computation can use the same parameters. LoopVAE reuses a scale- and loop-conditioned core within and across scales, while keeping resolution-changing transitions independent. A four-block core executes 28 block applications per encoder or decoder. On ImageNet-256, the 29M-parameter convolutional model reaches 0.28 rFID and 32.54 dB PSNR under an approximately 30-epo...

---

### 25. Prototype Matters: Modality-unified Prototype Self-distillation for Unsupervised Visible-infrared Person Re-identification

**Authors:** Menglin Wang, Xiaojin Gong

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11514v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11514v1)

**Summary:** Estimating reliable cross-modality association is crucial to unsupervised visible-infrared person re-ID. While optimal transport is shown to be a practical solution for cross-modality association, it suffers from the rigidness of hard label assignment without considering the impact of cluster noise. Moreover, enforcing only cross-modality contrast is also suboptimal, as it fails to jointly optimize the similarity relation within and across modality. In this paper, we propose a novel framework fo...

---

### 26. Harnessing Intrinsic Subject-Aware Attention for Controllable Multi-Subject Video Generation

**Authors:** Niange Yu, Ye Tian, Biaolong Chen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11507v1)

**Summary:** Multi-subject video generation faces two key challenges: uncontrollable fidelity strength and potential semantic drift. We address these by analyzing the internal mechanisms of Diffusion Transformers (DiTs). We found that certain attention blocks naturally form an Intrinsic Spatial Grounding Map (ISGM) that precisely locates reference subjects. Building on this insight, we propose Dual-phase Intrinsic Attention Leveraging (DIAL), a framework that uses these internal signals for both training and...

---

### 27. UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound

**Authors:** Weiying Chen, Yuchong Gao, Siyuan Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11506v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11506v1)

**Summary:** Three-dimensional ultrasound (US) is a safe, radiation-free complementary modality to CT and X-rays for longitudinal monitoring, yet its segmentation-derived partial point clouds are extremely artifact-laden. Consequently, it is challenging to recover a clean and complete anatomical structure from such US point clouds. In this paper, we present UBone3D, a novel framework based on physics-rectified conditional flow matching (CFM) that performs point cloud completion directly from partial US obser...

---

### 28. Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs

**Authors:** Zhiqi Li, Yuxuan Liao, Bo Zhu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11499v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11499v1)

**Summary:** Code world models represent worlds as executable programs, but this representation alone does not determine how to construct a complex world. We introduce Recursive Code World Models (RCWM), a framework for reconstructing complex 3D worlds in code from a single reference image. RCWM couples a Recursive Scene Program (RSP) representation with a construction solver that recursively calls itself. An RSP represents the executable world as compositional scene code, while each solver call follows the ...

---

### 29. FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation

**Authors:** Vladislav Bargatin, Alexander Yakovenko, Khaled Abud, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11486v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11486v1)

**Summary:** Optical flow methods typically rely on task-specific inductive biases, such as correlation volumes, feature warping, and iterative refinement, among others, to reach high accuracy. While effective, such biases constrain the model to predefined heuristics, which can limit its expressivity and lead to more complex pipelines and additional computational cost. We present FreeFlow, a hierarchical transformer built without any flow-specific components, using instead a single feed-forward encoder--deco...

---

### 30. Pre- and Post-Treatment Brain Metastases Segmentation Using nnU-Net with Post-Processing for BraTS 2026

**Authors:** Haobin Liu, Xin Wang

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11477v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11477v1)

**Summary:** Brain metastases exhibit high inter-lesion variability in size, enhancement pattern, and post-treatment appearance, making volumetric segmentation of both pre- and post-treatment cases the central challenge of the BraTS 2026 Task 1 (Brain Metastases). We build a pragmatic pipeline on a 5-fold nnU-Net ResEnc-L ensemble, in which each fold is trained independently for 1,000 epochs with the standard Dice + cross-entropy loss on 1,296 four-modality training cases. This ensemble is followed by a rule...

---

### 31. BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration

**Authors:** Qianliang Wu, Haobo Jiang, Guangwei Gao, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11472v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11472v1)

**Summary:** Reliable non-rigid point cloud correspondences are important for deformable anatomical registration, embodied perception and manipulation, and dynamic 3D reconstruction. Coarse-to-fine methods reduce computational cost by selecting the top-\(K\) coarse regions. However, this pruning may remove weak but correct hypotheses and restrict fine matching to an incomplete search space. We present \paper, a two-stage generative solver that maintains the complete soft matching matrix at both coarse and hi...

---

### 32. BruNet: A Cross-Domain Transfer Framework for Bruise Segmentation

**Authors:** Qiming Wang, Richard J. Motley, Ebube E. Obi, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11463v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11463v1)

**Summary:** Segmenting bruises is a challenging task in medical imaging due to limited data and annotations, diffuse boundaries, and highly variable appearance. In this work, we propose BruNet, a segmentation framework that combines a ViT-based visual encoder (a self-supervised DINOv3 or a pretrained LingBot-Vision backbone) with a SAM-based mask decoder. BruNet is trained on the HAM10000 skin lesion dataset and evaluated on a separate bruise dataset without additional fine-tuning. Although a small number o...

---

### 33. Multi-Modal Controlled Coherent Motion Generation

**Authors:** Yifei Liu, Qiong Cao, Hongwei Yi, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11439v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11439v1)

**Summary:** It is natural for humans to walk and talk simultaneously. This paper tackles the challenge of replicating such natural behaviors in 3D avatar motion generation driven by concurrent multimodal inputs, such as a text description of a man walking alongside speech audio. Existing methods, constrained by the scarcity of aligned multimodal data, typically combine motions from individual modalities sequentially or through weighted sums. However, they often result in mismatched or unrealistic movements....

---

### 34. Hologram Representation via Quadratic Phase Gaussian Splatting

**Authors:** Haolong Wang, Yicheng Zhan, Kaan Akşit, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11434v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11434v1)

**Summary:** We introduce Complex-Valued Quadratic Phase Gaussian (CVQPG), a novel hologram representation method that replaces standard 2D Gaussian representations used in 2D Gaussian Splatting with 2D quadratic phase functions. CVQPG incorporates additional learnable parameters to control the curvature of these bases. We evaluate our approach against state-of-the-art methods, exceeding the visual quality by +0.19 dB (RGB) and +0.33 dB (grayscale) on average in holographic reconstructions. Specifically, our...

---

### 35. DINO-Med: A Unified Patch-Based Adaptation Framework for Multi-Modal Medical Image Analysis Applied to Liver Fibrosis Staging

**Authors:** Boya Wang, Ruizhe Li, Chao Chen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11380v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11380v1)

**Summary:** Adapting natural-image foundation models like DINOv3 to multi-modal medical imaging is challenging due to the significant domain gap between natural color images and multi-channel medical scans. We present a unified, patch-based framework that processes raw multimodal imaging through training-free registration, automated localization, and mask-filtered patch extraction. This architecture culminates in a hierarchical strategy that aggregates patch-level insights into subject-level diagnostics. Us...

---

### 36. Brain-PACE: A Deep Siamese MRI Framework for Modelling Longitudinal Brain Acceleration

**Authors:** Samuel Maddox, Jacob Newman, Saber Sami, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11378v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11378v1)

**Summary:** Brain age estimation has become a popular research proxy for assessing brain health and disease, yet longitudinal trajectories of brain ageing are still poorly defined, and clinical use is limited. Building on existing Siamese longitudinal frameworks, we develop Brain-Predicted Age Acceleration (Brain-PACE) to directly estimate the pace of structural brain ageing from paired T1-weighted MRI. Brain-PACE identified accelerated ageing in $42.6$% of participants with mild cognitive impairment. Faste...

---

### 37. Vision Transformer-Based Multi-Level Feature Fusion for Multi-Label Sewer Defect Classification

**Authors:** Xu Fang, Zhuoran Wang, Qing Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11375v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11375v1)

**Summary:** Automated classification of sewer defects is essential for infrastructure condition assessment and maintenance decision-making, but existing deep learning methods struggle to balance classification accuracy and computational complexity in large-scale multi-label scenarios. This study develops Sewer-Transformer-ML, a hierarchical vision Transformer with multi-level feature fusion, together with two lightweight architectures, Sewer-MobileNet-ML and Sewer-Mobile-TransNet, for resource-constrained i...

---

### 38. R4Tun: LLM-guided adaptive segmental tunnel lining segmentation in point clouds

**Authors:** Xinghui Tao, Zehao Ye, Guangming Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11360v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11360v1)

**Summary:** Automated inspection of segmental tunnel linings requires adaptive segmentation from 3D point clouds, yet expert-tuned pipelines often degrade when tunnel conditions vary. This paper presents R4Tun, a large language model (LLM)-driven adaptation framework that extends an expert-designed pipeline (SAM4Tun) with bounded parameter tuning informed by structured context: memory ($m$), state ($s$), and knowledge ($k$). Evaluated on 30 selected Seg2Tunnel subsets (13 regular, 17 complex) across three L...

---

### 39. Predictive Multi-Landmark OCT Tracking for Increased Motion Robustness

**Authors:** Konrad Reuter, Suresh Guttikonda, Chaitali Uday Karekar, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11330v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11330v1)

**Summary:** Optical coherence tomography is a promising modality for markerless motion tracking due to its high spatial resolution and inherent depth perception. However, existing OCT-based tracking approaches are limited in terms of trackable velocity, particularly when multiple landmarks are tracked sequentially for 6D pose estimation. In this work, we present a predictive tracking approach that propagates positional updates between multiple tracked landmarks to obtain a global pose prediction. This enabl...

---

### 40. MultiHuSE: A Multimodal Dataset for Humour Styles and Emotions

**Authors:** Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11322v1)

**Summary:** Computational recognition of verbal humour remains a challenging task, requiring an understanding of language, delivery style, emotions, and cultural context. Most existing approaches focus on binary classification and lack datasets that capture psychological dimensions of humour alongside variations in expression. We introduce MultiHuSE, a multimodal dataset comprising 2,407 high-definition videos of 50 demographically diverse actors performing 1,463 text samples across four psychological humou...

---

### 41. Mi-Ripple: Restoring Images Degraded by Iterative AI Editing

**Authors:** Jiayin Chen, Yicheng Xu, Muting Wang

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11317v1)

**Summary:** Iterative reference-conditioned image editing can introduce grid-like and granular textures, commonly described as digital ripple. We present Mi-Ripple, a diagnosis-guided restoration workflow that suppresses this digital ripple while protecting image structure. Mi-Ripple separates periodic lattice artifacts from content-entangled granular texture, then combines selective spectral notching, structure-aware smoothing, and cleaned-reference regeneration. This separation enables low-distortion filt...

---

### 42. GRIPNet: Gaussian Radial Intensity Prior Guided Architecture for Pulmonary Nodule Detection in CT

**Authors:** Haojie Yang, Ran Su

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11312v1)

**Summary:** Lung cancer causes more deaths than any other malignancy, and low-dose CT screening is the main pathway to early diagnosis. That pathway hinges on the smallest lesions, yet nodules below six millimeters remain hard to detect, because most methods treat a nodule as a generic object and ignore the imaging physics behind its appearance. We show that this appearance is highly regular. Intensity peaks at the geometric center of a nodule and decays radially in a Gaussian pattern, and a fit to 18,218 a...

---

### 43. Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

**Authors:** Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11310v1)

**Summary:** We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen.   We identify two key design choices. First, placing prompt tokens at...

---

### 44. SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views

**Authors:** Langxu Zhao, Zuan Gu, Yingdan Zhang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11279v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11279v1)

**Summary:** With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Exte...

---

### 45. Order-Aware 2.5D Multiple Instance Learning for Preoperative MRI-Based Perineural Invasion Risk Assessment in Intrahepatic Cholangiocarcinoma

**Authors:** Hyunsu Go, Youngung Han, Kyeonghun Kim, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11271v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11271v1)

**Summary:** Perineural invasion (PNI) is an adverse histopathologic marker in intrahepatic cholangiocarcinoma (ICC), but it is usually confirmed only after resection. Preoperative T2-weighted MRI may provide noninvasive imaging cues predictive of PNI, although labels are available only at the patient level without slice- or voxel-level annotations. We propose Order-Aware Slab Multiple Instance Learning (OAS-MIL), a weakly supervised framework for patient-level PNI prediction. Each tumor-centered MRI crop is...

---

### 46. Improving Faint Object Detection for Space Situational Awareness with Variational Autoencoders

**Authors:** Angela Cratere, Luca Ghilardi, Vishnu Reddy, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11269v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11269v1)

**Summary:** We present a deep-learning pipeline for enhancing the detection of faint moving objects in optical space situational awareness (SSA) imagery through automated star removal and background reconstruction. Detecting low signal-to-noise ratio (SNR) objects remains extremely challenging in optical observations, particularly in the cislunar (X-GEO) environment, where structured sky backgrounds, dense stellar fields, and scattered moonlight significantly degrade the performance of classical detection a...

---

### 47. Uncertainty DMD: Restoring Diversity in Few-Step Autoregressive Video Distillation

**Authors:** Zixuan Duan, Xunzhi Xiang, Yabo Chen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11265v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11265v1)

**Summary:** Few-step distillation improves the efficiency of autoregressive (AR) video generation, but often causes diversity collapse: under the same prompt, different noise samples tend to produce highly similar videos with weakened motion dynamics. We analyze this degradation in Distribution Matching Distillation (DMD)-distilled AR video generators and find that, in the autoregressive setting, it takes the form of a structured uncertainty collapse: the mode-seeking bias of DMD maps different noise sample...

---

### 48. AI-Powered Flare Combustion Efficiency Estimation

**Authors:** Afeefa Azam, Iyyakutti Iyappan Ganapathi, Fares Ossama Abdelhafez, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11262v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11262v1)

**Summary:** Achieving high combustion efficiency in flare stacks is crucial for adhering to regulatory standards and controlling the release of hydrocarbons into the environment. Traditional instruments like gas analyzers and hyperspectral cameras are expensive, fragile, and require frequent calibration, which makes them impractical for remote or budget constrained industrial sites. We propose an innovative solution that combines a lightweight vision-language encoder with a compact multi-layer perceptron to...

---

### 49. OmniHallu: Unified Hallucination Detection for Cross-Modal Comprehension and Generation in Multimodal Large Language Models

**Authors:** Jianjiang Yang, Peihang Li, Shanqing Xu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11244v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11244v1)

**Summary:** While Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse tasks, they suffer from hallucinations where generated outputs contradict or misrepresent input semantics. Existing research typically addresses hallucination detection within a single modality or task type, limiting generalizability. We introduce OmniHallu, a unified hallucination detection framework spanning both comprehension and generation tasks across image, video, and audio modalities. We contri...

---

### 50. From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models

**Authors:** Meng Luo, Yicheng Liu, Jiahao Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11242v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11242v1)

**Summary:** Video generation has advanced to produce visually compelling and temporally coherent results. Yet, whether these models can genuinely think with video--executing symbolic rules, respecting physical laws, and pursuing intentional goals--remains an open question. Existing benchmarks only partially address this, often conflating visual quality with cognitive correctness. We introduce VWG-Bench (Video World Generalist Benchmark), a comprehensive benchmark spanning 9 reasoning dimensions and 38 fine-...

---

## cs.LG

**50 papers**

### 1. General Quantification of Covariate and Concept Shifts

**Authors:** Hongbo Chen, Li Charlie Xia

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11918v1)

**Summary:** Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging entropic optimal transport, we propose a key notion: $γ^{*}\!$-concept shifts, and derive a general ...

---

### 2. Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

**Authors:** Atindra Jha, Margaret Li, Jure Leskovec, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11917v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11917v1)

**Summary:** As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert coun...

---

### 3. Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

**Authors:** Masahiro Kato, Daiki Honma, Taka Kato

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11915v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11915v1)

**Summary:** Generative artificial intelligence changes how firms reach customers, but standard marketing data do not record how often users see and notice a firm's name in generated answers. We develop Generative Marketing Mix Modeling (GMMM) to estimate the causal effects of Generative Engine Optimization (GEO) and Generative Engine Marketing (GEM). For GEO, GMMM combines repeated generated answers with question counts, shares of use across generative systems, and notice probabilities. For GEM, it combines...

---

### 4. From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good

**Authors:** Nitesh V. Chawla, Paulo Benanti

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11910v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11910v1)

**Summary:** Artificial Intelligence does more than create a governance problem. It can also reveal where institutions have already failed to provide responsiveness, belonging, care, and accountability. Once deployed, AI becomes an intervention in those conditions. It can repair, compound, substitute for, or conceal the failures it encounters. Responsible AI must therefore evaluate both the system and the institutional rupture into which it is introduced. The move from principles to protocols is already unde...

---

### 5. TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription

**Authors:** Akshaj Gupta, Hwi Joo Park, Andrea Guzman, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11904v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11904v1)

**Summary:** Automatic Music Transcription (AMT) for guitar remains limited by three challenges: existing systems often fail to capture expressive techniques such as slides, bends, and percussive hits; they often assign notes to incorrect string-fret combinations; and they are typically trained on clean recordings, limiting their generalization to noisy real-world audio. To address these challenges, we propose TART, a modular four-stage audio-to-tablature pipeline consisting of (1) an audio-to-MIDI transcrip...

---

### 6. CausalArena: Benchmarking Causal Discovery in the Foundation Model Era

**Authors:** Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11897v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11897v1)

**Summary:** Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence of causal discovery foundation models (CDFMs) further complicates evaluation: performance may refle...

---

### 7. 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11894v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11894v1)

**Summary:** Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast bu...

---

### 8. CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search

**Authors:** Yifan Yang, Zhaoyan Wang, Zheng Gao, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11884v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11884v1)

**Summary:** Zero-cost proxies rank architectures cheaply, but their reliability varies across search spaces. We introduce CoRA-NAS (COarse Ranking + Anchor-residual), a two-stage framework combining a static ranking prior with low-cost learning-curve refinement. CoRA-Rank aggregates capacity and structure-at-initialization proxies through an equal-weight log-rank consensus and a target-free consensus gate. CoRA-Refine samples anchors across this prior, extrapolates their early validation curves, and propaga...

---

### 9. Domain-Specific Hallucination Detection in Large Language Models

**Authors:** Varun Teja Chundru, Debasmita Biswas

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11878v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11878v1)

**Summary:** Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summ...

---

### 10. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

**Authors:** Yi Duan, Ying Liu, Zirui Tang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11873v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11873v1)

**Summary:** Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement. N...

---

### 11. Evaluating Time-Series Foundation Models and Multimodal Dietary Context for CGM Forecasting

**Authors:** Bowen Zhang, Hsiu-Wen Cheng, Hongyu Yang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11872v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11872v1)

**Summary:** Continuous glucose monitoring (CGM) provides high-frequency measurements of glucose dynamics and enables short-term glucose forecasting for diabetes management. Although time-series foundation models have shown strong general forecasting ability, their effectiveness for CGM prediction and the added value of multimodal dietary context remain unclear. We conduct a comprehensive empirical study using eight public CGM datasets spanning Type 1 diabetes, Type 2 diabetes, and non-diabetes populations. ...

---

### 12. AdamX: Cosine similarity meets gradient descent

**Authors:** Francisco Caldas, Ruben Belo, Cláudia Soares

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11867v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11867v1)

**Summary:** We introduce AdamX, a first-order optimizer that incorporates cosine similarity as an adaptive mechanism for controlling update magnitudes. The proposed method is scalable, model-agnostic, and straightforward to integrate into existing training pipelines. We further introduce a variance rectification scheme that promotes smoother optimization during the early stages of training. Overall, we provide empirical evidence that AdamX achieves competitive convergence rates across a range of benchmark d...

---

### 13. Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models

**Authors:** Rodion Krjutškov, Eduard Barbu, Nikos Sakkas, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11860v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11860v1)

**Summary:** Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility managers and building operators to interpret. Explainable Artificial Intelligence (XAI) techniques address this opacity, but traditional XAI dashboards require substantial technical expertise and provide limited flexibility for dynamic, context-aware inquiry. Conversational XAI systems offer a promising ...

---

### 14. Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport

**Authors:** Luyi Jia, Boyan Zhang, Yilun Liu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11842v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11842v1)

**Summary:** Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motivated by optimal transport, helps explain strong baselines but remains model-agnostic and ignores prediction error. Here we introduce a model-aware schedule construction based on fiberwise optimal transport. At a fixed time and state on the probability path, compatible signal/noise decompositions form...

---

### 15. Near-Optimal Reinforcement Learning with Multi-Step Transition Lookahead

**Authors:** Corentin Pla, Hugo Richard, Marc Abeille, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11807v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11807v1)

**Summary:** We study reinforcement learning (RL) with transition look-ahead, where the agent may observe which states would be visited upon playing any sequence of $\ell$ actions before deciding its course of action. Although look-ahead can substantially improve achievable performance, it is known that optimal planning with multi-step transition look-ahead is NP-hard, but this hardness was established using discount factors arbitrarily close to one. It was therefore unknown whether the problem remains hard ...

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

### 18. Dynamic language model representations for multi-objective reaction optimisation

**Authors:** Joshua W. Sin, David Ming Segura, Bojana Ranković, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11790v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11790v1)

**Summary:** Optimising chemical reactions across multiple objectives, such as yield, selectivity, and safety, is central to chemical synthesis, and model-driven approaches depend critically on how reaction components are represented. Established featurisations are either chemically uninformative, as with one-hot encodings, or, as with molecular descriptors, do not readily extend across chemically distinct components. For structurally and functionally diverse components, it is therefore unclear what a shared...

---

### 19. Predicting Privacy Leakage from Weight Spectral Density

**Authors:** Richard J. Preen, Jim Smith

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11780v1)

**Summary:** Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive shadow models, making large-scale privacy evaluation impractical. In this work, we investigate whether inexpensive spectral metrics derived from the heavy-tailed self-regularisation framework can serve as proxies for MIA vulnerability. We evaluate several WeightWatcher spectral metrics on image and...

---

### 20. Differentially Private EEG Feature Anonymization: A Privacy-Utility Case Study in Clinical Neurophysiology

**Authors:** Noman Sadiq, Mohsen Toorani

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11777v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11777v1)

**Summary:** Clinical electroencephalography (EEG) data are valuable for healthcare research and for developing artificial intelligence (AI)-based clinical decision-support systems, but EEG recordings and derived features may contain sensitive patient-specific information. This creates privacy risks when data are reused, analyzed, or shared across clinical and research environments. Conventional anonymization methods are often insufficient for high-dimensional biomedical signals, since removing direct identi...

---

### 21. A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients

**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11768v1)

**Summary:** Per-token gating of forward/reverse KL losses has become a standard technique for on-policy knowledge distillation (OPD), but existing methods such as EOPD (Jin et al., 2026) and ToDi (Jung et al., 2025) each fix a single gating signal and a single gating direction, and the two have never been compared directly. We introduce a four-coefficient parameterization lambda_t = sigma(a * h_t + b * u(x) + c + d * gap_t) in which direction-aligned proxies of EOPD and ToDi appear as one-dimensional (1D) r...

---

### 22. SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control

**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11752v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11752v1)

**Summary:** For industrial content risk control, the real deployment constraint is not average accuracy but how much risk can be auto-handled under high precision and second-level latency. We present SIRF (Spec-Internalized Risk Foundation Model), which internalizes a platform's complex policies, synthesized without additional human annotation via EntiGraph, MAGA rewriting and account-level chain-of-thought (CoT), into the weights via continued pretraining (CPT), so rules are applied at high precision under...

---

### 23. Sparsity Regularized and Robust Mean Variance Portfolio Selection Under Ellipsoidal Uncertainty

**Authors:** Deniz Akkaya, Emre Can Yayla, Buse Şen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11749v1)

**Summary:** We investigate mean-variance portfolio selection with an $\ell_0$-penalty to promote sparsity in asset allocations. Uncertainty in the mean return vector is incorporated through an ellipsoidal uncertainty set, yielding a robust sparse optimization framework. We characterize the structure of both local and global minimizers and exploit these properties in the risk minimization and return maximization formulations. Building on this structural insight, we develop a branch-and-bound algorithm tailor...

---

### 24. Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs

**Authors:** Joseph Kanichai, Tiziano De Matteis, Animesh Trivedi

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11744v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11744v1)

**Summary:** Prefix caching can reduce the time to first token (TTFT) of long-context LLM requests by reusing previously computed key-value (KV) states, but for short prefixes or fast GPUs, recomputation can be faster than loading from an external cache. We characterize this tradeoff in vLLM across GPU, CPU, and NVMe tiers using synthetic workloads, long-context benchmarks, production traces, and find that cache performance depends on transfer granularity, intermediate memory use, and when transfers enter th...

---

### 25. LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation

**Authors:** Dongfang Zhao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11739v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11739v1)

**Summary:** Large language model serving costs scale directly with output sequence length, yet standard preference alignment often inflates response verbosity without improving utility. We study whether the parameterization of post-training updates affects generation length: low-rank subspaces alter sequence length without modifying the alignment loss. We present LOCUS, a method that selects a task-aware low-rank adaptation subspace to minimize output-token cost subject to a utility constraint. Within this ...

---

### 26. ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI

**Authors:** Zhengran Ji, Jonathan Hyun, Boyuan Chen

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11737v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11737v1)

**Summary:** Collective intelligence depends not only on the capabilities of individual members, but also on how those members are organized. Yet artificial multi-agent systems are typically assembled using fixed organizational structures, even when the physical tasks they perform impose fundamentally different coordination requirements. Here we show that principles from human organization theory can be operationalized to organize large, heterogeneous collectives of embodied artificial agents. We introduce O...

---

### 27. Learning structural balance of graphs from quantum spectral features

**Authors:** Stefano Scali, Oleksandr Kyriienko

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11736v1)

**Summary:** We develop a quantum approach to spectral feature extraction from the density of states (DOS) of a problem-dependent Hamiltonian, and apply it to machine learning on signed graphs. We propose to embed a signed graph as an Ising model instance with positive and negative interactions, and use the standardized moments of the Ising DOS as features for learning. We show that these moments count signed closed walks, are switching-invariant, and are size-free by construction. As a benchmark, we target ...

---

### 28. Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion

**Authors:** Jian Zhou, Xingyu Zhang, Rui Ma, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11733v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11733v1)

**Summary:** Muscle-driven locomotion provides a physically grounded approach to generating realistic human movement. However, achieving both physiological plausibility and adaptability to changes in musculoskeletal capacity and external disturbances remains a fundamental challenge. To address this limitation, we propose a Reflex-Informed Neuromuscular Reinforcement Learning framework for muscle-driven locomotion. Within this framework, a fixed phase-dependent reflex controller serves as the underlying neuro...

---

### 29. Why Does Post-Training Quantization Work?

**Authors:** Yuxiang Chen, Michael Beyer, Jun Zhu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11716v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11716v1)

**Summary:** Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states. Naively, these errors should accumulate with depth and corrupt next-token prediction; randomly initialized models accumulate these discrepancies rapidly, whereas quantized pretrained models accumulate much less hidden-state error and largely maintain downstream task performance, even though they were never trained ...

---

### 30. Generalization Analysis of Distributed Kernel-based Robust Gradient Descent Algorithms

**Authors:** Jun-Yi Meng, Zheng-Chu Guo, Yuan Mao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11712v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11712v1)

**Summary:** In this paper, we investigate the generalization performance of distributed gradient descent algorithms in a reproducing kernel Hilbert space under a robust loss function $l_σ$. By exploiting the spectral characterization of gradient descent together with the intrinsic properties of robust loss functions, we establish optimal learning rates for the distributed kernel-based robust gradient descent (DKRGD) algorithm with an appropriately chosen scale parameter $σ$. The proposed parameter choice of...

---

### 31. Negative Self-Distillation: Learning to Reason by Avoiding Flaws

**Authors:** Rongcan Pei, Zhepei Wei, Shuyao Xu, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11699v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11699v1)

**Summary:** On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expres...

---

### 32. Geospatial Foundation Models Capture Health-Relevant Dimensions of Place Beyond Conventional Social Risk Indices

**Authors:** Nathaniel Hendrix, Carl Y. Zhang, Chris Heitzig, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11689v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11689v1)

**Summary:** Area-based social risk indices summarize residents' socioeconomic conditions but incompletely capture physical features of place that may affect health. We evaluated whether numerical representations of physical place produced by four geospatial foundation model families from 2022 satellite data explained residual variance in tract-level associations between the Area Deprivation Index, Social Deprivation Index, and Social Vulnerability Index with health outcomes. We used LightGBM to predict vari...

---

### 33. Multimodal Taxonomic Conditioning for Generative Plankton Imagery

**Authors:** Daniela Ivanova, Ozgu Goksu, Nicolas Pugeault

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11673v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11673v1)

**Summary:** Automated plankton imaging produces severely long-tailed datasets, where the rare taxa of greatest ecological interest have too few images to train or evaluate classifiers reliably. We generate synthetic plankton imagery conditioned on taxonomy: a CLIP encoder is adapted on a large plankton corpus with a ranked contrastive objective extended to deep, ragged taxonomies, then frozen to condition a parameter-efficient diffusion transformer. We evaluate synthetic sample quality on distributional fid...

---

### 34. Learnware and AI Model Management System

**Authors:** Zhi-Hua Zhou

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11656v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11656v1)

**Summary:** The transition from file storage to database management systems transformed stored data into managed resources. AI now faces an analogous transition from AI model storage to AI model management. Existing model pools essentially serve as \textit{AI model storage systems}. What is needed instead are \textit{AI model management systems} that enable models trained by different developers, for different tasks, with different data, and under different objectives to be identified, reused, and even asse...

---

### 35. Musec: MomentUm SpEctral Clipping for Stable Muon-type Training

**Authors:** Zhuanghua Liu, Menglian Wang, Luo Luo

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11655v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11655v1)

**Summary:** Muon has emerged as a highly effective optimizer for large language model training, often achieving superior convergence and performance compared with the widely adopted Adam and AdamW optimizers. Nevertheless, Muon is prone to training instability due to its spectral flattening, manifested by loss spikes and unbounded growth of model weights. Existing approaches primarily rely on weight or attention-logit clipping, which require architecture-specific modifications and do not directly address in...

---

### 36. RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate Time Series Imputation

**Authors:** Ramiro Valdes Jara, David Chapman, Adam Meyers

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11648v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11648v1)

**Summary:** Multivariate time series imputation (MTSI) aims to recover missing values in temporal data composed of multiple interdependent variables. This problem is central to real-world applications such as healthcare monitoring, traffic networks, and energy systems. Recent diffusion-based approaches have shown strong potential for probabilistic imputation by learning to generate missing values through iterative denoising. However, most existing approaches perform diffusion directly in the original data s...

---

### 37. ZipCodec: Ultra-Low-Frame-Rate Streaming Speech Coding

**Authors:** Luca Della Libera, Cem Subakan, Mirco Ravanelli

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11642v1)

**Summary:** Neural audio codecs are a fundamental component of modern speech generation systems. While recent codecs achieve increasingly low bitrates, reducing frame rate remains challenging, as each token must preserve more information while maintaining reconstruction quality. We present ZipCodec, a streaming neural speech codec operating at 6.25 Hz and 0.80 kbps with a theoretical latency of 160 ms. Our approach combines large-scale WavLM distillation with a redesigned transformer-based architecture, a s...

---

### 38. LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics

**Authors:** Mariia Baranova, Adrien Petralia, Etienne Le Naour, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11639v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11639v1)

**Summary:** The energy transition is reshaping residential electricity consumption through the increasing adoption of distributed generation, electrified appliances, and demand-response programs. Understanding these evolving behaviors requires access to granular smart-meter data for applications such as load forecasting, appliance detection, and demand-side flexibility analysis. However, such data are subject to strict access restrictions and data-protection regulations. Thus, realistic synthetic alternativ...

---

### 39. Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation

**Authors:** Jintao Zhang, Kai Jiang, Jintao Chen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11638v1)

**Summary:** We present Vidu S2, which comprises Vidu S2-Avatar, a real-time interactive digital-character model, and Vidu S2-Editing, a real-time video editing model. Moreover, we explore the feasibility of real-time spatial video generation for both Vidu S2-Avatar and Vidu S2-Editing. Compared with Vidu S1, Vidu S2-Avatar supports real-time 720p video generation, generation with dynamic references that can be updated at any moment, and stronger instruction following, such as dancing. Vidu S2-Editing suppor...

---

### 40. Distributed Optimization of Modular Production Systems using Model-based Reinforcement Learning with Inverse Models

**Authors:** Andreas Schwung, Steve Yuwono, Sofiene Lassoued, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11615v1)

**Summary:** This paper presents a novel approach for data-driven self-learning control of highly flexible, modular manufacturing systems. Specifically, we employ a novel framework for model-based reinforcement learning which introduces approximate inverse process models within the training of reinforcement policies. This approach disentangles the learning of actuation dynamics and the dynamics in state space, resulting in RL-based training solely within the task space. We propose a lightweight feedforward a...

---

### 41. Identifiability of Nonnegative Tensor Decompositions via Positive Scattering

**Authors:** Haoming Wang, Ming Yuan

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11606v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11606v1)

**Summary:** Identifiability of tensor decompositions is often established through linear-algebraic conditions on the factor families. For nonnegative decompositions, however, positivity provides additional information that is not captured by dimension and independence alone: nonnegative terms cannot cancel, and their supports constrain competing decompositions. We introduce a positive scattering term that quantifies this additional source of identifiability and combine it with the dimension budget underlyin...

---

### 42. A distribution-free certification framework for trustworthy crash-severity prediction

**Authors:** Amir Rafe, Subasish Das

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11592v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11592v1)

**Summary:** Crash-severity models inform screening, dispatch and site prioritization, yet are deployed without a finite-sample statement of what one prediction means. Off-the-shelf guarantees fail here, because the features that make crash severity distinctive defeat them: the KABCO outcome is ordinal, the recorded label is a field assessment agreeing with medical severity about half the time, erring in a structured way, and deployment crosses jurisdictions and years calibration never saw. We develop a cert...

---

### 43. A Dataset and Model for Imputing Water Surface Elevation on a Large and Extremely Sparse Spatiotemporal Graph

**Authors:** Ruben Cartuyvels, Karim Douch, Gabriele Bertoli, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11580v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11580v1)

**Summary:** Continuous monitoring of water surface elevation across river networks is critical for flood forecasting, water resource management, and understanding the global water cycle. Yet, the scarcity of in situ gauges across much of the globe constrains the development of reliable modeling frameworks. Satellite altimetry has the potential to alleviate this problem but its use is currently hindered by sparse temporal coverage. To this end, we introduce AmazonSWE, a dataset for training and evaluating la...

---

### 44. Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)

**Authors:** Harshdeep Singh, Yurui Zhu, Giovanni Colavizza, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11569v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11569v1)

**Summary:** We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs perform text-to-SPARQL generation given only automatically derived structured metadata and small graph samples, rather than task-specific fine-tuning? We integrate VoID descriptions and ShEx schemas into a retrieval-augmented generation (RAG) pipeline and ablate KG-derived conte...

---

### 45. Particle GFlowNets: Rethinking Generative Marginalization Models

**Authors:** Tiago da Silva, Diego Mesquita, Salem Lahlou

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11538v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11538v1)

**Summary:** Generative Marginalization Models (MaMs) have been recently introduced as efficient neural sampling models for any-order autoregressive modelling of discrete distributions. By learning both the marginal and conditional probabilities of a persistent-block Gibbs sampler, MaMs enable fast posterior evaluation with a single neural network forward pass. While prior work has considered MaMs to be distinct from Generative Flow Networks (GFlowNets), a well-established paradigm for inference in discrete ...

---

### 46. Risk-Averse Decision Making with Multi-Level Reliability Guarantees

**Authors:** Amirmohammad Farzaneh, Osvaldo Simeone

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11524v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11524v1)

**Summary:** Many applications in engineering, including wireless broadcasting, require designs that provide performance certificates at different target outage levels. This paper studies the problem of maximizing the weighted average of such certificates in the presence of uncertainty about the true system state. The problem is shown to be equivalent to an optimization over nested prediction sets, connecting to the literature on conformal prediction and extending prior art on single-level risk-averse decisi...

---

### 47. Generalized Score Matching for Parameter Estimation on Convex Domains

**Authors:** Nishanth Shetty, Saisuchith Mahajan, Chandra Sekhar Seelamantula

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11521v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11521v1)

**Summary:** Maximum likelihood (ML) estimation is a principled and statistically efficient approach for learning probabilistic models. However, for unnormalized models, ML estimation requires evaluating the partition function and differentiating through it, which may not always be tractable. Score matching provides a practically viable alternative that circumvents this obstacle by fitting the score in a way that eliminates dependence on the normalizing constant. We derive the generalized score matching obje...

---

### 48. Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based Neuroevolution

**Authors:** Romain Claret, Arthur Gygax, Michael O'Neill, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11518v1)

**Summary:** Evolvable-Substrate HyperNEAT (ES-HyperNEAT), a bio-inspired indirect encoding that determines neuron placement and connection weights from spatial coordinates, exhibits a failure mode on MNIST as a diagnostic benchmark. Because input pixels map to a coordinate space centered at the origin, evolved networks converge on a small central cluster of input pixels, a spatial-concentration bias; prior work observed only 21% mean accuracy in this regime. Is this bias an optimization artifact or an archi...

---

### 49. Structural priors for data-efficient language learning

**Authors:** Yana Veitsman, Jonas Mayer Martins, Jonathan Lautenschlager, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11505v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11505v1)

**Summary:** Efficient language learning requires methods to reduce the reliance on large data and computational resources. We investigate structural transfer: First training models on non-language data to induce useful priors for natural language. This approach is a form of weight initialization for multilingual language modeling. We evaluate transfer via next-token-prediction loss, weight shifts in the model, and downstream linguistic benchmarks. Several symbolic data types - notably music, probabilistic g...

---

### 50. DeFiFlowBench: Benchmarking and Improving Safe Executability in Natural-Language DeFi Workflow Synthesis

**Authors:** Abhinav Rajeev Kumar, Harshit Arora, Varun Singh, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11504v1)

**Summary:** A structurally valid DeFi workflow can still authorize a costly trade. We introduce DeFiFlowBench, a benchmark of 207 team-authored prompts for natural-language DeFi workflow synthesis. It measures graph coverage, configuration completeness, and declared safety predicates, then tests supported trade configurations on a local EVM. Direct, constrained, and few-shot prompting produce 14-19 unsafe held-out executions per configuration under a fixed 5% price-impact cap. A slippage bound derived from ...

---

## cs.NE

**50 papers**

### 1. Predicting Privacy Leakage from Weight Spectral Density

**Authors:** Richard J. Preen, Jim Smith

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11780v1)

**Summary:** Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive shadow models, making large-scale privacy evaluation impractical. In this work, we investigate whether inexpensive spectral metrics derived from the heavy-tailed self-regularisation framework can serve as proxies for MIA vulnerability. We evaluate several WeightWatcher spectral metrics on image and...

---

### 2. Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based Neuroevolution

**Authors:** Romain Claret, Arthur Gygax, Michael O'Neill, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11518v1)

**Summary:** Evolvable-Substrate HyperNEAT (ES-HyperNEAT), a bio-inspired indirect encoding that determines neuron placement and connection weights from spatial coordinates, exhibits a failure mode on MNIST as a diagnostic benchmark. Because input pixels map to a coordinate space centered at the origin, evolved networks converge on a small central cluster of input pixels, a spatial-concentration bias; prior work observed only 21% mean accuracy in this regime. Is this bias an optimization artifact or an archi...

---

### 3. GeoTrussRover: Morphological Computation with Contact-Semantic Control Primitives

**Authors:** Muyuan Ma, Yi Zhang, Yang Yang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11361v1)

**Summary:** Reconfigurable robots can change their contact geometry when a fixed body cannot negotiate an obstacle. A variable-geometry truss (VGT) distributes this shape change through a load-bearing structure, but coupling it to a mobile base creates a high-dimensional coordination problem. GeoTrussRover combines an electrically actuated VGT, a wheeled base, and contact-semantic morphology planning and control. We solve one source traversal and extract four contact-semantic primitives that describe coordi...

---

### 4. Solving Few-Shot Multiobjective Multitask Optimization via Iterative Sequential Transfer

**Authors:** Tingyang Wei, Haofeng Wu, Ananda Phan Iman, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11228v1)

**Summary:** Applying knowledge transfer across multiple optimization tasks, multitask optimization (MTO) emerges as a promising approach to solving synergistic optimization tasks simultaneously. However, the development of effective knowledge transfer mechanisms in MTO fundamentally relies on aligning elite solution distributions across tasks. This dependency creates a critical bottleneck in few-shot optimization regimes, as restricted evaluation budgets impede the identification of elite solution distribut...

---

### 5. Phases in a class of associative memories via hidden neurons

**Authors:** Toshihiro Ota, Masato Taki

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10976v1)

**Summary:** Associative memory in the Hopfield network is attractor dynamics in a disordered many-body system, and higher-order and exponential extensions turn its retrieval update into softmax attention. The polynomial and exponential regimes have been analyzed by different methods, with no common architecture in which to ask what fixes the storage scale. In this paper we study the bipartite architecture of Krotov and Hopfield, which we call the class $H$, whose model is fixed by a Lagrangian for each laye...

---

### 6. Fractional-order hardware for neuromorphic computing: Is the order really the problem?

**Authors:** Christof Teuscher

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10882v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10882v1)

**Summary:** Does a neuromorphic system need a true power-law memory kernel, and if so, can anyone build one? Neuromorphic systems process signals spanning many timescales at once, from milliseconds to tens of seconds. Integer-order circuits buy each additional timescale with an additional state variable. Fractional-order dynamics offer a different bargain: one operator whose power-law kernel carries a continuum of timescales, tuned by one parameter, the order alpha. A fractional derivative is non-local, so ...

---

### 7. Training Trajectories Determine Circuit Removability in Annealable Soft-Prior Transformers

**Authors:** Zonglin Yang, Ziming Zhao, Wei Tang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10287v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10287v1)

**Summary:** Soft positional priors can help small Transformers learn retrieval circuits, but it is unclear whether the resulting circuits remain functional once the prior is removed. We test this with an annealable soft-prior Transformer whose attention biases can be learned, faded, or zeroed during training and evaluation. On associative recall, unforced models perform well with the prior active ($0.772 \pm 0.020$) but collapse at zero gate ($0.095 \pm 0.009$). Smooth fade-to-zero training preserves high z...

---

### 8. Structural Fusion of Bayesian Networks with Limited Treewidth Using Genetic Algorithms

**Authors:** Pablo Torrijos, José A. Gámez, José M. Puerta

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10276v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10276v1)

**Summary:** This paper introduces an evolutionary computation approach for consensus in structural Bayesian Network (BN) fusion under the constraint of limited treewidth. The consensus BN aims to reconcile multiple input BNs into a single one that retains key structural features present in the original networks. Treewidth, a graph-based parameter associated with computationally tractable inference, is utilized to restrict the complexity of the resulting network. A genetic algorithm is proposed to look for a...

---

### 9. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 10. Teacher Geometry Shapes Learnability in Teacher-Student Networks

**Authors:** Kai J. Sandbrink, Flavio Martinelli, Alexander van Meegen, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09595v1)

**Summary:** Teacher-student systems, in which a teacher neural network generates training labels so that a student neural network can learn to implement the same function, are widely used as an abstract setting to study learning. However, the structure of the teachers is often overlooked by assuming randomly-generated, normally-distributed parameters. This hides substantial variation in how learnable different teachers are. We formalize learnability as the success rate of converging to the global minimum, a...

---

### 11. Robust Industrial Cyber Physical Classification Using Neuromorphic Temporal Embeddings and Hybrid SNN XGBoost Under Machine Unlearning Attacks

**Authors:** Ammar Kamoona, Sajad Koushkbaghi, Mahdi Jalili, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09564v1)

**Summary:** The digitalisation of electrical distribution networks has increased the exposure of power-grid infrastructure to cyber attacks. Existing intrusion detection systems (IDSs), however, often rely on computationally expensive deep learning models that are difficult to deploy at the edge. Periodic retraining also exposes these systems to machine unlearning attacks, where selective data removal can degrade detection performance. We propose a hybrid Spiking Neural Network (SNN) and XGBoost architectur...

---

### 12. Gradland: On Phenomenal Experience, Differentiated Across Many Dimensions

**Authors:** David Balduzzi

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09306v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09306v1)

**Summary:** This paper investigates the hypothesis that the first-order structure of physical interactions, i.e. gradients or Jacobians, characterizes the structure of phenomenal experience. It does so in an idealized world inhabited by neural networks, Gradland, where the physics are known and the functions are (mostly) differentiable. The paper introduces two measures of Jacobian structure: effective rank and cohesion, based on Kirchhoff complexity. Applying the measures to a series of worked examples sho...

---

### 13. Why shared attention vectors fail: a case for outcome-indexed tuning

**Authors:** Lenard Dome

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08615v1)

**Summary:** Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for ...

---

### 14. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**Authors:** Xiangnan Zhang, Jingxin Liu, Ranqi Lu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08070v2) | 📄 [PDF](https://arxiv.org/pdf/2609.08070v2)

**Summary:** The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historica...

---

### 15. Emergent Charging Coordination in Electric Delivery Fleets

**Authors:** Javier Vales-Alonso, Juan J. Alcaraz

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07689v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07689v1)

**Summary:** In electric delivery fleets, mid-shift charging is non-trivial: each vehicle must decide when, where and how much to charge to finish on time with battery above a safety floor. The choices are coupled: queues build where too many vehicles pick the same station. Prior work resolves this coupling with central dispatching, precomputed schedules or reservations, machinery that charging infrastructure rarely supports. Instead, we use a family of learning agents under purely local control: every vehic...

---

### 16. Photonic reservoir computing with dimensionally compressed readout

**Authors:** Gerald Kobi, Mohab Abdalla, Miguel C. Soriano, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07418v1)

**Summary:** This work addresses a hardware constraint in reservoir computing: the limited size of the readout layer imposed by systems with a physical readout. We investigate a strategy to accommodate this constraint based on random projection, which compresses high-dimensional reservoir states into a lower-dimensional subspace while preserving key properties of the source space and information- processing capabilities. To evaluate this approach, we compare a small, standalone time delay reservoir against a...

---

### 17. Formation of structural attractors in neuromorphic systems

**Authors:** Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin, et al.

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.06826v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06826v1)

**Summary:** This paper examines the theory of Invariant Structural Learning (ISL), which proposes a non-optimization approach to concept formation. Learning is interpreted as convergence to structural attractors in a hypergraph space, rather than as the minimization of a global loss function. The paper presents the ISL model, including its mathematical formalization, computational verification, and a hypothetical neurobiological interpretation. The mathematical section introduces the formal apparatus of the...

---

### 18. Threshold-Based Selection for Continuous Optimization: A Leaf-Abscission Instantiation

**Authors:** Nasser Khalili

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.10588v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10588v1)

**Summary:** This paper formalizes threshold-based selection as an evaluation-gating architecture in which each incumbent is tested before variation and a replacement is generated and evaluated only when contextual pressure exceeds intrinsic strength. The mechanism is instantiated as Leaf Abscission Optimization (LAO), using rank-based strength, a phenological seasonal signal, diversity modulation, environmental pressure, and a base regrowth kernel. A blocked two-to-the-fourth-power factorial analysis at dim...

---

### 19. Linear Algebra Foundations of Efficient Attention: A Phase Reversal in Rank Collapse Under SVD Compression

**Authors:** Anjaneya Teja Sarma Kalvakolanu

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.06341v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06341v1)

**Summary:** Linear algebra provides the framework of concepts (matrix rank, singular value decomposition (SVD), and eigendecomposition) that modern artificial intelligence employs to encode, compress, and propagate information through neural networks. This paper unifies fourteen separate peer-reviewed works analyzing the usage of these techniques in the context of transformer-based foundation model research, focusing on three areas of the topic: derivations and properties of self-attention matrices' output ...

---

### 20. Programmable Cellular Automata

**Authors:** Ahmed Khalifa, Muhammad Umair Nasir, Matthew Siper, et al.

**Published:** 2026-09-05

🔗 [Paper](http://arxiv.org/abs/2609.06102v2) | 📄 [PDF](https://arxiv.org/pdf/2609.06102v2)

**Summary:** Cellular automata is a local computation paradigm where complex behavior can arise from local interactions between simple functions. This paradigm has been used to explain many systems such as biological processes, traffic simulation, computer networks, etc. In games, cellular automata have been used in games such as SimCity and for the generation of spatial content such as caves or dungeons. However, creating effective local rules is hard and unintuitive. Cellular automata can be effectively ev...

---

### 21. Minimizing the Effect of Sleep Deprivation in the Forward-Forward Algorithm

**Authors:** Joy Datta, Puja Saha, Rawhatur Rabbi, et al.

**Published:** 2026-09-05

🔗 [Paper](http://arxiv.org/abs/2609.06042v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06042v1)

**Summary:** This paper addresses the challenge posed by sleep deprivation in the Forward-Forward algorithm, where separating the two passes in this algorithm and imbalancing the data processing in the passes is considered an imitation of the cognitive processes observed in humans suffering from sleep deprivation. Previous research has demonstrated that sleep deprivation in the Forward-Forward algorithm has a catastrophic effect on learning efficacy. To mitigate this issue, we explore several approaches; the...

---

### 22. What Makes a Redundant Representation Remember? Lineage Isolation, Not Masking

**Authors:** Jia Huang, Yangjun Ou

**Published:** 2026-09-04

🔗 [Paper](http://arxiv.org/abs/2609.05304v1) | 📄 [PDF](https://arxiv.org/pdf/2609.05304v1)

**Summary:** Memory-based evolutionary algorithms for dynamic optimization often carry a redundant second copy of the genotype and expose only one copy to the objective, on the assumption that the shielded copy accumulates information about past optima. We show this assumption is false as usually implemented, and identify the structural property that actually determines whether the shielded copy retains information. We formalize such methods as a gated dual-copy representation with two independent design axe...

---

### 23. Large Language Models with At Most One Spike per Neuron

**Authors:** Zhuoya Zhao, Parsa Omidi, Aref Jafari, et al.

**Published:** 2026-09-04

🔗 [Paper](http://arxiv.org/abs/2609.05151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.05151v1)

**Summary:** Leveraging their inherent sparse event-driven computation, spiking neural networks (SNNs) offer a promising path toward energy-efficient large language models (LLMs). Time-to-first-spike (TTFS) coding generates at most one spike per neuron within a time window, yielding extremely low firing rates. However, conventional TTFS SNNs are restricted to specific structures, making it challenging to encode certain blocks in LLM -- such as layer normalization and matrix multiplication --using TTFS. To ov...

---

### 24. Towards Efficient Evaluation of Evolutionary Transfer Optimization: Case Studies on Task-Parameterized Applications

**Authors:** Yanchen Li, Xiaoming Xue, Kay Chen Tan

**Published:** 2026-09-04

🔗 [Paper](http://arxiv.org/abs/2609.05040v1) | 📄 [PDF](https://arxiv.org/pdf/2609.05040v1)

**Summary:** As evolutionary transfer optimization (ETO) scales to larger collections of related tasks, problem evaluation can become a major source of runtime growth. This work studies problem-side evaluation scaling in task-parameterized applications and reformulates application-specific serial computations into forms suitable for parallel execution. We organize evaluation scaling into two levels: the number of evaluated tasks and the workload within each task. In multi-task optimization, matrix-recursive ...

---

### 25. Axonal delay dispersion decides whether a neuron detects an event or a sequence, and predicts cortical column diameter

**Authors:** Cheng Bi, Jipeng Sun

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04195v1)

**Summary:** Cortical neurons fire sparsely -- often fewer than one spike per sensory window -- making rate coding insufficient and temporal coding a necessity. That conduction delays convert firing order into synchrony is long established. What governs which class of temporal feature a neuron detects -- one volley of coincident input, or two in a particular order -- has not been examined. We propose a delay-signature framework in which the axonal conduction delays converging on a dendritic branch constitute...

---

### 26. Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks

**Authors:** Shivang Rawat, Mirko Morello, Flaviano Morone, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04134v1)

**Summary:** Temporal integration gives continuous-time recurrent networks memory, but in deep stacks it also delays bottom-up signals and attenuates top-down errors. We develop Recursive Quadrature Filters (RQFs), biologically motivated complex-valued temporal filters that are a special case of diagonal state-space models (SSMs), and ask whether this failure mode can be addressed by making each layer's bottom-up input prospective. Starting from an energy model, we derive the RQF dynamics and show that each ...

---

### 27. Genetic Algorithms for Tractable Bayesian Network Fusion via Pre-Fusion Edge Pruning

**Authors:** Pablo Torrijos, José A. Gámez, José M. Puerta, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03724v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03724v1)

**Summary:** Bayesian Network (BN) fusion combines multiple input networks into a single structure, balancing dependency preservation with computational tractability. While unrestricted fusion retains all dependencies, it often results in overly complex networks with high treewidth, which affects inference scalability. Limited fusion mitigates this by pruning edges to control treewidth but risks overfitting to input-specific noise and omitting dependencies from the original BNs. This paper introduces a conse...

---

### 28. Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language

**Authors:** Julian Truetsch, Felix Hauser, Christoph Stiller, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03677v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03677v1)

**Summary:** Understanding the composition of large-scale autonomous driving datasets is essential for safety, robustness, and reliable operation across domains. For example, domain shift between locations could lead to the operating environment being misaligned with the training data, resulting in potentially dangerous performance degradation. Yet, existing data analysis pipelines largely rely on metadata, predefined labels, or manual inspection, which provide limited semantic insight or do not scale. This ...

---

### 29. Efficient Constant Optimization for Symbolic Regression with GPU-Accelerated Tree-Based Genetic Programming

**Authors:** Hao Mao, Xu Tony Liu, Shuai Lu, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03352v1)

**Summary:** Constant optimization refines the numerical coefficients of candidate expressions in tree-based genetic programming for symbolic regression. But its per-generation cost has led modern GPU-accelerated frameworks to omit it or restrict it to lightweight forms. We present a GPU-resident, batched Levenberg--Marquardt solver that optimizes constants across a structurally heterogeneous population of expression trees using a fixed number of population-wide CUDA launches per iteration. Reverse-mode auto...

---

### 30. CompEvo: Competition-Induced Evolution for Multi-Agent in News-Driven Time Series Forecasting

**Authors:** Yuxuan Zhang, Yangyang Feng, Yong Guan, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.09195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09195v1)

**Summary:** News-driven time series forecasting uses evolving textual events together with historical observations to predict future values, supporting applications such as market risk monitoring and resource scheduling. In multi-agent settings, two challenges still remain. The first is degeneration of thought, where agents converge to similar evidence-seeking behaviors. The second is insufficient theoretical grounding, where strategy updates are often heuristic and lack a principled formulation. To address...

---

### 31. H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression

**Authors:** Anchit Mulye, Rhythm Baghel, Sujay Kumar Ingle, et al.

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02684v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02684v1)

**Summary:** Deploying 3D point cloud models on edge hardware such as the NVIDIA Jetson Orin Nano is severely constrained by compute and memory budgets. Existing compression methods require access to the model's original source code, rendering them inapplicable to the Open Neural Network Exchange (ONNX) binaries commonly distributed by vendors and model repositories. We present \textbf{H3DNAS}, a hardware-aware model compression framework that operates directly on ONNX computational graphs without requiring ...

---

### 32. Model-Free Surrogate-Assisted Neural Architecture Search for Evolving Variable-Length Dense Blocks

**Authors:** Asif Ameer, Maryam Bashir, Irfan Younas, et al.

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02460v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02460v1)

**Summary:** Neural Architecture Search (NAS) has emerged as a powerful paradigm for automatically designing deep neural networks; however, its practical adoption is often limited by substantial computational cost. To alleviate expensive full-training evaluations, surrogate-based methods have been introduced to estimate network performance efficiently. Nevertheless, existing approaches-particularly model-based surrogates-require training many candidate architectures and involve additional optimization overhe...

---

### 33. Semantics-Guided Automatic Tensorization for Multiobjective Evolutionary Algorithms: A Multi-Agent Framework

**Authors:** Zhenyu Liang, Beichen Huang, Bowen Zheng, et al.

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02387v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02387v1)

**Summary:** Multiobjective evolutionary algorithms (MOEAs) naturally expose population-level parallelism, but many mature implementations encode their computation in sequential program structures designed for central processing units. Exploiting modern tensor computing platforms therefore requires more than direct code translation: the implementation must be restructured without changing the defining optimization mechanism of the underlying MOEA. We formulate automatic tensorization for MOEAs as semantics-g...

---

### 34. LLM-Driven Joint Evolution of Coupled Heuristics Components for Routing Optimization

**Authors:** Juntao Wei, Yangming Zhou, Zhibin Jiang, et al.

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02353v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02353v1)

**Summary:** Heuristic design for combinatorial optimization remains heavily reliant on expert knowledge, while existing large language model (LLM)-enhanced evolutionary methods typically evolve isolated algorithmic components, even when one determines the search state on which another operates. This paper proposes LLM-driven Heuristic Components Joint Generation (LLM-HCJG), a population-based framework that jointly generates and co-evolves interdependent heuristic components under a shared design blueprint....

---

### 35. Memory as an Energy Landscape---Hopfield

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02195v1)

**Summary:** This chapter reconstructs the Hopfield network as a physical theory of memory rather than merely an early neural-network algorithm. It begins with the problem as it stood before 1982-threshold logic, Hebbian association, correlation memories, and recurrent binary networks-and isolates what Hopfield's synthesis added: a dynamical definition of content-addressable memory, a symmetric recurrent architecture with a Lyapunov function, a Hebbian embedding of patterns in its couplings, and a physical a...

---

### 36. Neural Logic, Invariance, and the Retina---McCulloch and Pitts

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02183v1)

**Summary:** This chapter reconstructs the McCulloch-Pitts program as a physics of neural computation rather than the familiar cartoon of a binary neuron. The 1943 logical calculus is developed in both directions: given a net, characterize the propositions realized by its activity; given an admissible logical expression, construct a net that realizes it. We recover the original distinction between thresholded excitatory summation and absolute inhibitory veto-one the weighted-threshold form cannot preserve fo...

---

### 37. Reinforcement learning to choose optimizers

**Authors:** Martin van der Schelling, Deepesh Toshniwal, Miguel A. Bessa

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01811v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01811v1)

**Summary:** No single optimization method is uniformly best for all problems, and the most suitable optimizer choice can change during a run. Existing approaches that change optimizer during execution typically predetermine part of the strategy: the portfolio is restricted to one algorithm class, the switch occurs once at a fixed time, or the frequency of decisions is treated as a hyperparameter rather than a learned one. We introduce "Reinforcement Learning to Choose Optimizers", which formulates the optim...

---

### 38. Dictionary-Guided Mutation Operators for Automated HDL Repair

**Authors:** Maisha Mastora, Dean Sullivan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01775v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01775v1)

**Summary:** Automated repair of Hardware Description Language (HDL) designs remains challenging due to the large search space of candidate repairs and the strict syntactic and semantic constraints imposed by HDL grammars. Generic mutation strategies overwhelmingly generate syntactically invalid candidates that waste compilation and simulation budget, while synthesis-driven and template-based approaches impose their own constraints on generality and portability. In this paper, we propose a dictionary-guided ...

---

### 39. CircuitsDNA: Discovering Unconventional Multi-Accuracy Arithmetic Circuits via Evolutionary Synthesis

**Authors:** Ruichen Qi, Junyi Luo, Xinting Jiang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01735v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01735v1)

**Summary:** Emerging edge AI workloads increasingly require arithmetic units that can trade computational accuracy for efficiency on demand. However, existing approximate arithmetic circuits are typically fixed-accuracy or rely on predefined structures for runtime configurability. This work introduces CircuitsDNA, an evolutionary framework that automatically evolves accuracy-configurable arithmetic circuits supporting multiple accuracy modes within a single circuit. It integrates three key features: 1) mult...

---

### 40. Rethinking Learnability in Offline Data-driven Optimization

**Authors:** Chao Qian, Chen-Guang Wang, Rong-Xi Tan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01493v2) | 📄 [PDF](https://arxiv.org/pdf/2609.01493v2)

**Summary:** Black-Box Optimization (BBO) has broad applications, while traditional algorithms such as evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization has been the most popular paradigm to improve the efficiency of BBO, by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires...

---

### 41. Neural Symbollic Regression Using Deep Learning and Sparse Modelling

**Authors:** Ravi Kumar U, Sumitra S

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01102v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01102v1)

**Summary:** Symbolic Regression (SR) seeks to find succinct mathematical expressions that represent the fundamental relationships within data, providing interpretability and scientific understanding that exceeds that of black-box models. Nevertheless, traditional methods like Genetic Programming face challenges with scalability and are highly sensitive to noise, while sparse regression techniques such as SINDy rely significantly on predetermined feature libraries. In this work, we present a Neural Symbolic ...

---

### 42. Web Price Extraction: State of the Art and an Adaptive Browserless Implementation

**Authors:** Evgeniia Kositsyna, Jorge Lloret-Gazo

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01030v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01030v1)

**Summary:** Price extraction from websites is a key task for market monitoring, price comparison, and business analytics in e-commerce. Existing approaches can be broadly divided into four groups, and understanding their trade-offs in accuracy and scalability is essential for selecting suitable extraction strategies. Classical methods rely on manually written wrappers and rule induction from labeled pages, offering high accuracy but adapting poorly to structural changes and requiring considerable maintenanc...

---

### 43. Denoising Diffusion Generative Models Secretly Calculate Attentions

**Authors:** Farzan Haddadi, Leila Monfared, Ebrahim Rezaii, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00885v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00885v1)

**Summary:** Denoising diffusion models are the dominant architecture for image generation, whereas most natural language generation and modeling are primarily handled by well-known transformer architectures employing attention mechanism. Here, we show that diffusion models also inherently use an attention mechanism very similar to that of transformers. Therefore, attention emerges as a universal machine learning principle, based on a general training objective. We also show similarities in basic functional ...

---

### 44. Diffusion models for eye-gaze trajectory generation using position and velocity representations

**Authors:** Laxman Basnet, Alexander Szorkovszky, Pedro G. Lind, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.05522v1) | 📄 [PDF](https://arxiv.org/pdf/2609.05522v1)

**Summary:** Eye-tracking data are expensive to collect, requiring specialized hardware and controlled laboratory conditions, and difficult to share because of privacy constraints. We address this using two complementary denoising diffusion probabilistic models (DDPMs) for unconditional generation of eye-gaze dynamics from visual-search data. Both use an identical FiLM-conditioned one-dimensional U-Net with self-attention (19.35,M parameters), trained on 8,s sliding-window sequences from 28 participants. One...

---

### 45. Self-Reports Are Not Verification: Environment-Grounded Auditing of LLM Operators in Evolutionary Search

**Authors:** Enrong Pan, Ryan Zhou, Ting Hu

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00652v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00652v1)

**Summary:** Language model agents increasingly propose actions, observe external feedback, and explain their own behavior. Their confidence and rationales are convenient monitoring signals, but convenience is not verification. We introduce an environment-grounded audit in which every intermediate proposal receives an exact outcome. A language model operates an evolutionary Contexto search whose feedback function assigns every valid guess an exact rank without human annotation. Across 200 runs spanning five ...

---

### 46. GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning

**Authors:** Wenjian Wu, Zesheng Jia, Jiaying Tang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00577v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00577v1)

**Summary:** Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely attributable to weak modeling of local geometric structures and the fact that conflicting task selections are handled only after action generation. To address these limitations, we propose...

---

### 47. Investigating Hyperparameter Optimization and Transferability for ES-HyperNEAT: A TPE Approach

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00449v2) | 📄 [PDF](https://arxiv.org/pdf/2609.00449v2)

**Summary:** Neuroevolution of Augmenting Topologies (NEAT) and its advanced version, Evolvable-Substrate HyperNEAT (ES-HyperNEAT), have shown great potential in developing neural networks. However, their effectiveness heavily depends on the selection of hyperparameters. This study investigates the optimization of ES-HyperNEAT hyperparameters using the Tree-structured Parzen Estimator (TPE) on the MNIST classification task, exploring a search space of over 3 billion potential combinations. TPE effectively na...

---

### 48. Where Should Experience Live? Hierarchical Hebbian Memory for Continual Vision Transformers

**Authors:** Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00358v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00358v1)

**Summary:** Vision Transformers provide strong visual representations but typically rely on slowly updated parameters, limiting their ability to organize newly acquired information across different memory timescales. This work proposes \textit{Hierarchical Hebbian Memory}, a three-level memory architecture composed of rapid Working Memory, persistent Routed Episodic Memory, and slower Semantic Memory. A learned controller regulates memory contribution, read and write routing, plasticity, retention, and cons...

---

### 49. Flawed in Nature, Perfect through Evolution

**Authors:** J. M. Diederik Kruijssen

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00129v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00129v1)

**Summary:** The performance of artificial intelligence (AI) and machine learning (ML) models degrades when the problem they were trained on drifts. This is a near-universal feature of real-world problems, which often change unpredictably. Biological evolution has achieved intelligence by overcoming this obstacle through natural selection acting on heritable variation. AI/ML techniques have long incorporated forms of natural selection, but it has been challenging to maintain model diversity as optimization n...

---

### 50. Conjoint Audio-to-Spikes Encoding and Processing for Efficient Neuromorphic Speech Recognition

**Authors:** Valentin M. Meunier, Amélie Gruel, Pierre Lewden, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30792v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30792v1)

**Summary:** Obtaining data from neuromorphic sensors and processing it with Spiking Neural Networks is a promising solution to lower the energy cost of artificial intelligence. The current rarity of natively neuromorphic datasets promotes the development of software tools to translate input sensory data into spikes. However, highly bio-mimetic simulators can be challenging to implement on digital hardware. In this work, we evaluate the neuromorphic encoding and subsequent classification of audio into spikes...

---

## q-bio.NC

**50 papers**

### 1. pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches

**Authors:** M. Marzulli, A. Angiolelli, C. Mannino, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11530v1)

**Summary:** The analysis of neuronal avalanches offers insights into brain dynamics utilizing the framework of criticality, but the reproducibility and comparability of studies are limited by the use of fragmented, lab-specific scripts. To address this issue, we introduce pyAvalanches, an open-source Python package providing a standardized, end-to-end pipeline for avalanche analysis from electrophysiological recordings (e.g., electroencephalography-EEG). Starting from the detection of neuronal avalanches th...

---

### 2. Degeneracy along the sensorimotor hierarchy: motor control within a framework larger than redundancy

**Authors:** Florent Paclet, Paul Duprat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11325v1)

**Summary:** Motor control has described the surplus of solutions available to the nervous system as redundancy, a term that names duplication: interchangeable elements, robust to loss but incapable of differential adaptation. Biology has had a second term for twenty-five years. Degeneracy names elements that are not interchangeable and are nonetheless isofunctional with respect to a given output, and it supports adaptability, since non-identical elements necessarily diverge in some context. Circuit neurosci...

---

### 3. The Platonic brain bridge hypothesis: human brain networks as an architectural prior for omni models

**Authors:** Pengfei Zhang, Biao Tian, Xiangang Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10947v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10947v1)

**Summary:** We propose the Platonic brain bridge hypothesis: omni models, which process video, audio and text jointly like the brain, converge on brain-like representations, and the correspondence is bidirectional. From model to brain, brain-likeness of seven omni models is stable across participants, and our encoding models on their internal hidden states rank first on the Algonauts 2025 out-of-distribution leaderboard. From brain to model, three contributions follow. Brain-MoE gives seven cortical network...

---

### 4. Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model

**Authors:** Daniel Semchin, Emile d'Angremont, Hao Ding, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10890v1)

**Summary:** Parkinson's disease is clinically and biologically heterogeneous, yet its spatiotemporal progression remains poorly characterized. We present a connectome-constrained disease progression model that jointly estimates subject-specific disease time and data-driven subtypes from longitudinal morphometry. Applied to 85 imaging and clinical biomarkers from the Parkinson's Progressive Markers Initiative (PPMI) cohort, the model recovers four morphologically distinct progression subtypes. We validate th...

---

### 5. Cortical information transfer reveals conserved hemispherical network dynamics across human handedness

**Authors:** Yago Emanoel Ramos, José Garcia Vivas Miranda

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10870v1)

**Summary:** Whether human motor and brain lateralization arises from fundamentally distinct neural architectures or emerges from conserved network dynamics remains a central question at the intersection of network science and neurobiology. Conventional measures of cortical activation often fail to resolve how directed information exchange adapts to manual preference during complex motor tasks. This ambiguity leaves it unclear whether left-handed individuals possess atypical neural organization or follow sha...

---

### 6. BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10518v1)

**Summary:** fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain...

---

### 7. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 8. EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding

**Authors:** Muchen Li, Anglin Liu, Xuetian Gao, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09728v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09728v1)

**Summary:** Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by s...

---

### 9. Emergence of criticality in models of real neurons

**Authors:** David P. Carcamo, Christopher W. Lynn

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09438v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09438v1)

**Summary:** Critical systems sit near boundaries between qualitatively distinct behaviors. When inferring models of neural activity, this proximity to criticality is thought to require the precise tuning of parameters. Here, we show that as the number of neurons increases, criticality can emerge naturally without fine-tuning. When computing observable statistics from parameters (the forward problem), some small regions in parameter space map to large regions in statistics space. These special parameters are...

---

### 10. XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

**Authors:** Yang Qiao, Junjie Wu, Deqiang Qiu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09388v1)

**Summary:** Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional co...

---

### 11. Hi-M imaging of chromatin architecture in adult Drosophila brain cryosections

**Authors:** Christel Elkhoury Youhanna, Julie Garona, Marie Schaeffer, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08776v1)

**Summary:** Hi-M combines fluorescence in situ hybridization (FISH), automated microfluidics, sequential imaging, and computational chromatin tracing to measure the three-dimensional organization of selected genomic regions in single cells. This chapter describes a Hi-M workflow adapted for cryosections of adult Drosophila melanogaster brains, enabling chromatin tracing while preserving tissue architecture and cell identity. The protocol covers Oligopaint library design and amplification, fixation, brain di...

---

### 12. Why shared attention vectors fail: a case for outcome-indexed tuning

**Authors:** Lenard Dome

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08615v1)

**Summary:** Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for ...

---

### 13. An Evidence-Aware Framework for EEG Microstate Analysis: Improved Sensitivity to Alzheimer's Disease and Ageing

**Authors:** Kaidong Wu, Haili Ye, Ptolemaios G Sarrigiannis, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08500v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08500v1)

**Summary:** Electroencephalography (EEG) microstate analysis commonly converts each scalp topography into a winner-take-all hard label and summarises the resulting sequence using duration, occurrence, coverage, transitions, and symbolic complexity. Although interpretable, this readout discards evidence strength, assignment ambiguity, and low-confidence periods. We introduce a template evidence trajectory framework that retains, at each sampled Global Field Power (GFP) peak, the evidence for all templates or...

---

### 14. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**Authors:** Xiangnan Zhang, Jingxin Liu, Ranqi Lu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08070v2) | 📄 [PDF](https://arxiv.org/pdf/2609.08070v2)

**Summary:** The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historica...

---

### 15. Fisher-Rao Distance Detects Shifts in Kinematic Profiles under Cognitive Load

**Authors:** Joseph Vero, Elizabeth B Torres

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07696v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07696v1)

**Summary:** Motor control research involves the study of movement kinematics derived from the positional trajectories that complex motions describe. In natural, unconstrained motions requiring cognitive and memory processes in real time, the temporal speed profiles are not bell-shaped, may have multiple maxima and the peaks distribution is best fit by the continuous gamma family with two parameters, the shape and the scale. As the stochastic processes described by complex motion trajectories are non-station...

---

### 16. Fisher Information Metric as a model-free measure of proximity to criticality in neural systems

**Authors:** Yuewei Du, Alberto Liardi, Hardik Rajpal, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07624v1)

**Summary:** Critical phenomena are widespread across many disciplines and have recently become a topic of deep interest in the study of biological and artificial neural networks. A distinct signature of criticality is the emergence of avalanches with power-law-distributed sizes and durations. However, empirically estimating the critical exponents remains challenging, and their interpretation is often model-dependent. In this work, we demonstrate how the Fisher Information Metric (FIM), a measure of generali...

---

### 17. Homeostasis Revisited and Reformulated Through Hidden Markov Model Control

**Authors:** Rubén Moreno-Bote

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07508v1)

**Summary:** A common formalization of homeostasis is the free energy principle, a framework that defines a set of desired observation values, or critical states, that the agent should reach or remain close to. Under the free energy principle, an agent should act to maximize the probability of receiving the desired observations. Here we revisit the common approach of solving the problem of maximizing the log probability of the desired observations by maximizing a variational lower bound, the so-called negati...

---

### 18. Revisiting the Aerts-Broekaert-Smets quantum model of the liar paradox

**Authors:** Massimiliano Sassoli de Bianchi

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09228v1)

**Summary:** The quantum model of the two-sentence liar paradox proposed by Aerts, Broekaert, and Smets is an early example of the use of quantum formalism to describe cognitive dynamics. Our reconstruction is primarily pedagogical in intent, but it also leads to a number of clarifications, and to some new observations, concerning the structure of the model. Rewriting the model in Dirac notation, we make explicit the distinction between truth values originating from a decision and from semantic inference, an...

---

### 19. Determinants of hyperparameter robustness in connectome reservoir computing

**Authors:** Miles Walter Churchland, Raul de Palma Aristides, Jordi Garcia-Ojalvo, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07355v1)

**Summary:** Reservoir computing provides a controlled setting for studying how recurrent network architectureshapes computation: input signals are projected into a high-dimensional state space by a fixed nonlinear dynamical system, and only the readout is trained. However, reservoir performance can be dependent on hyperparameters; this paper asks which recurrent network features support robustness to those parameter changes. We characterize computational performance using memory capacity (MC), truncated sin...

---

### 20. Adaptive Entangled Game Modules in Artificial General Intelligence

**Authors:** Haochen Li, Xinshuai Guo, Jingdong Ouyang, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09226v1)

**Summary:** We introduce a probability-wave framework for modeling the collective behavior of interacting adaptive agents, deriving testable eigenmodes through a generalized behavioral intelligence (GBI) nonlocal probability-wave equation. This framework captures a broad range of human intelligence behaviors with analytical mechanisms and offers an indirect method to examine the Liu-Chen-Ao (LCA) hypothesis of nonlocal entangled nerve fibers in the brain through collective trader behaviors. Our empirical an...

---

### 21. Formation of structural attractors in neuromorphic systems

**Authors:** Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin, et al.

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.06826v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06826v1)

**Summary:** This paper examines the theory of Invariant Structural Learning (ISL), which proposes a non-optimization approach to concept formation. Learning is interpreted as convergence to structural attractors in a hypergraph space, rather than as the minimization of a global loss function. The paper presents the ISL model, including its mathematical formalization, computational verification, and a hypothetical neurobiological interpretation. The mathematical section introduces the formal apparatus of the...

---

### 22. A Roadmap for MEG Foundation Models

**Authors:** Philipp Thölke, Hamza Abdelhedi, Yorguin Mantilla-Ramos, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04461v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04461v1)

**Summary:** Foundation models are beginning to reshape brain-signal analysis by moving the field beyond task-specific decoding pipelines toward reusable models pretrained on broad neural datasets. Magnetoencephalography (MEG) is a compelling but still underdeveloped target for this shift: it captures human cortical dynamics at millisecond resolution while offering stronger spatial interpretability than EEG, making it especially valuable for source-resolved studies of perception, language, cognition, and cli...

---

### 23. Axonal delay dispersion decides whether a neuron detects an event or a sequence, and predicts cortical column diameter

**Authors:** Cheng Bi, Jipeng Sun

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04195v1)

**Summary:** Cortical neurons fire sparsely -- often fewer than one spike per sensory window -- making rate coding insufficient and temporal coding a necessity. That conduction delays convert firing order into synchrony is long established. What governs which class of temporal feature a neuron detects -- one volley of coincident input, or two in a particular order -- has not been examined. We propose a delay-signature framework in which the axonal conduction delays converging on a dendritic branch constitute...

---

### 24. Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks

**Authors:** Shivang Rawat, Mirko Morello, Flaviano Morone, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04134v1)

**Summary:** Temporal integration gives continuous-time recurrent networks memory, but in deep stacks it also delays bottom-up signals and attenuates top-down errors. We develop Recursive Quadrature Filters (RQFs), biologically motivated complex-valued temporal filters that are a special case of diagonal state-space models (SSMs), and ask whether this failure mode can be addressed by making each layer's bottom-up input prospective. Starting from an energy model, we derive the RQF dynamics and show that each ...

---

### 25. High-Order Triadic Functional Connectivity in the Brain and Beyond

**Authors:** Qiang Li, Masoud Seraji, Yu-Ping Wang, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03987v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03987v1)

**Summary:** Here, we report high-order functional network connectivity as a promising way for studying the brain connectome. Traditional functional connectivity approaches capture only pairwise relationships between brain regions, overlooking complex multivariate dependencies that underlie cognition and behavior. First, we demonstrated that high-order interactions capture more information and can distinguish between resting-state and task-state brain activity. Second, we introduce a matrix-based entropy-fun...

---

### 26. Inferring Affective Consciousness in an Artificial Agent: A Case Study

**Authors:** Mark Solms, St John Grimbly, Bruce Bassett, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03883v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03883v1)

**Summary:** Creatures that display 'hedonic place preference behaviour' are thought by many scientists to experience feelings, on the assumption that their attraction to pleasure-producing substances which lack nutritional value (e.g. cocaine, morphine) cannot easily be attributed to unconscious instinctual behaviour. In this paper, we discuss how a simple artificial agent that instantiates attributes of an affective system engaging in felt uncertainty about its intrinsic needs in relation to environmental ...

---

### 27. Tensor-based Brain Surface Modeling and Analysis

**Authors:** Moo K. Chung, Keith J. Worsley, Steve Robbins, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03302v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03302v1)

**Summary:** We present a unified computational approach to tensor-based morphometry in detecting the brain surface shape differences between two clinical groups based on magnetic resonance images. Our approach is novel in a sense that we combined surface modeling, surface data smoothing and statistical analysis in a coherent unified mathematical framework. The cerebral cortex has the topology of a 2D highly convoluted sheet. Between two different clinical groups, the local surface area and curvature of the ...

---

### 28. A Common Measure of Communication for Speech Brain-Computer Interfaces

**Authors:** Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02887v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02887v1)

**Summary:** Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so their reported scores are rarely comparable. Underlying this measurement problem are two unresolved ques...

---

### 29. Prediction emerges in RNNs trained for perception

**Authors:** Akanksha Gupta, Alejandro Tabas

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02739v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02739v1)

**Summary:** The brain is highly proficient at making sense of noisy and ambiguous sensory inputs. Predictive processing hypothesises that this ability relies on prediction. However, it is unclear why the brain would have evolved to predict the sensory world, a computationally expensive process, in order to aid perception. Here we use simulations to argue that prediction naturally emerges in systems optimised for perception. We train recurrent neural networks (RNNs) to denoise a tokenised version of Bach's c...

---

### 30. Fungal Memory and Minimal Cognition

**Authors:** Kristina Šekrst

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02345v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02345v1)

**Summary:** This paper argues that fungal mycelial networks exhibit minimal cognition through memory-integrated adaptive regulation. Drawing on cybernetic and enactivist frameworks, I develop a non-representational account of memory as the organism's capacity to modulate behavior based on temporally extended environmental coupling. I propose four operational criteria for minimal cognition: feedback-guided regulation of behavior, maintenance of internal viability conditions, structural modulation based on pa...

---

### 31. Mus siliconus: A Neuro-Musculoskeletal Digital Twin of the Mouse Integrating Neural Dynamics, Biomechanics, and Tactile Sensing

**Authors:** Satoshi Oota, Hideo Yokota, Hiroki Mori

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02243v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02243v1)

**Summary:** Digital twin technologies could transform neuroscience and biomedicine by creating predictive computational representations of living organisms. However, most animal digital twins model neural circuits, anatomy, or biomechanics separately rather than integrating the processes that generate behavior. We argue that animal digital twins should instead be conceived as embodied dynamical systems that unify neural activity, body mechanics, sensory feedback, and environmental interactions.   We propose...

---

### 32. Memory as an Energy Landscape---Hopfield

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02195v1)

**Summary:** This chapter reconstructs the Hopfield network as a physical theory of memory rather than merely an early neural-network algorithm. It begins with the problem as it stood before 1982-threshold logic, Hebbian association, correlation memories, and recurrent binary networks-and isolates what Hopfield's synthesis added: a dynamical definition of content-addressable memory, a symmetric recurrent architecture with a Lyapunov function, a Hebbian embedding of patterns in its couplings, and a physical a...

---

### 33. Neural Logic, Invariance, and the Retina---McCulloch and Pitts

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02183v1)

**Summary:** This chapter reconstructs the McCulloch-Pitts program as a physics of neural computation rather than the familiar cartoon of a binary neuron. The 1943 logical calculus is developed in both directions: given a net, characterize the propositions realized by its activity; given an admissible logical expression, construct a net that realizes it. We recover the original distinction between thresholded excitatory summation and absolute inhibitory veto-one the weighted-threshold form cannot preserve fo...

---

### 34. Adversarial Vulnerabilities of Neural Biomarker Identification Systems

**Authors:** Polina Tapal, Bryce-Allen Bagley

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01856v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01856v1)

**Summary:** There is growing interest in the proposed use of EEG signals as biometric credentials, but thus far there has been little research on the reliability and security of such biometrics. Prior adversarial tests have focused on deep-learning classifiers and assumed attackers have full access to the classifier model. This has left unexamined other, more popular categories of neural signature methods as well as the more realistic case of an adversary having only black-box access to a classifier. In thi...

---

### 35. Interpretable Symptom Vectors for Depression in a Large Language Model

**Authors:** Fangyi Zhu, Ajay Subramanian, Allison Constant, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01832v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01832v1)

**Summary:** Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using me...

---

### 36. Slow-Fast Brain-Computer Interfaces: Preventing Neuroadaptive Overfitting in AI-Mediated Neural Interfaces

**Authors:** Aarthy Nagarajan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01767v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01767v1)

**Summary:** Artificial intelligence (AI) is transforming brain-computer interfaces (BCIs) from task-specific neural decoders into adaptive systems that complete language, smooth movement, regulate rehabilitation support and adjust stimulation. These capabilities can increase speed, fluency, usability and clinical reach, yet conventional performance metrics may overlook losses in intent fidelity, authorship, agency, therapeutic challenge and durable clinical benefit. I define neuroadaptive overfitting as a c...

---

### 37. Active Visual Semantics: A large-scale MEG and eye-tracking dataset for understanding visual intelligence in action

**Authors:** Philip Sulewski, Carmen Amme, Peter König, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01055v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01055v1)

**Summary:** Here we present the Active Visual Semantics (AVS) dataset, a large-scale collection of magnetoencephalography (MEG) and eye-tracking data recorded while five participants freely explored 4,080 natural scenes over 10 sessions each, yielding more than 200,000 fixation epochs in total. Unlike existing neuroimaging datasets that rely on passive viewing with enforced central fixation, AVS captures brain activity during active scene exploration, including self-generated saccades and fixations. A seman...

---

### 38. Pulling Illusion in Individuals with Neurological Disorders

**Authors:** Takeshi Tanabe, Satoshi Yamamoto, Toru Yamada, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.10566v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10566v1)

**Summary:** The pulling illusion induced by asymmetric vibration stimuli has attracted attention for its potential applications in rehabilitation and sensory assessment. However, the underlying mechanism of the pulling illusion remains unclear. This study addressed the central question of whether peripheral vibrotactile sensitivity alone is sufficient for the illusion to emerge or whether processing beyond basic vibration detection is also required. Neurological disorders can involve impairments at differen...

---

### 39. Temporally constraining source imaging estimates in an underdetermined neural system with eigenmodes of cortical geometry

**Authors:** Pok Him Siu, Philippa J. Karoly, Artemio Soto-Breceda, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00809v2) | 📄 [PDF](https://arxiv.org/pdf/2609.00809v2)

**Summary:** Geometric eigenmodes provide a compact and biologically grounded representation of large-scale neural activity. Previous work demonstrated that they can mitigate the underdetermined nature of electroencephalographic (EEG) and magnetoencephalographic (MEG) source localisation, an ill-posed inverse problem in which neural activity is reconstructed from non-invasive recordings. Beyond their spatial structure, neural field theory predicts the temporal evolution of eigenmodes through analytically der...

---

### 40. A distributed-delay Wilson-Cowan model of sleep-related rhythms in the corticothalamic system

**Authors:** Eva Kaslik, Anca Radulescu, Anca Stanoev

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00520v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00520v1)

**Summary:** The corticothalamic circuit supports rhythms with timescales that differ by orders of magnitude: sleep spindles, the sigma-band events of non-rapid-eye-movement (NREM) sleep, and infra-slow fluctuations near 0.02Hz that organize when spindles occur. Because the anatomy is the same in both cases, architecture alone cannot determine which rhythm the circuit expresses. We ask whether the temporal structure of the circuit's own feedback can. In a four-population Wilson--Cowan model comprising cortic...

---

### 41. "More Is Different'' in Neural Circuits: Algebraic Emergence of Effective Theories in Canonical Recurrent Motifs of Biological Neuronal Networks

**Authors:** Nima Dehghani

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30231v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30231v1)

**Summary:** Canonical neural circuit motifs are usually described functionally: divisive normalization rescales population activity by a pooled signal, and winner-take-all competition selects one pattern through recurrent excitation and shared inhibition. We represent them, and their compositions, algebraically as finite transformation systems and analyze the transition monoids generated by their input-conditioned updates, distinguishing structure already present in a generator from structure that appears o...

---

### 42. Local connectivity balance shapes population dynamics in random recurrent networks

**Authors:** Shotaro Takasu, Richard Gast, Ann Kennedy

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30008v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30008v1)

**Summary:** Disordered dynamical systems comprising many interacting units, from ecological communities to neural circuits, are ubiquitous, and understanding how connectivity shapes their collective behavior is a central theoretical challenge. One long-recognized feature of neural circuits is local connectivity balance, in which the excitatory and inhibitory weights converging onto each unit approximately cancel. Although local connectivity balance has been proposed to serve functions such as gating incomin...

---

### 43. Rate-Coding Bundle Memory: A Unified Model of Memory and Control for Symbolic Computation in the Brain

**Authors:** Teun van Gils, Rowan P. Sommers, Markus Ostarek, et al.

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29189v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29189v1)

**Summary:** We propose a neurobiologically plausible model of cognition that combines the advantages of connectionist and symbolic systems, and that can explain a wide range of cognitive phenomena. This model, called Rate-Coding Bundle Memory (RCBM), is based on the Symbolic Subsystem Hypothesis, which posits that the brain implements a symbolic subsystem within its fundamentally connectionist nature. RCBM is a hybrid model that uses rate coding to represent symbols in a continuous space, and it uses a bund...

---

### 44. Front-end and Back-end Computational Modeling of 40-Hz Auditory Steady-State Response Abnormalities in Schizophrenia

**Authors:** Wenjun Xia, Yan Xu, Zhengdi Zhang

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29104v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29104v1)

**Summary:** 40-Hz ASSR is reduced in schizophrenia, but it is unclear if this reflects altered auditory input or cortical E/I dynamics. We hypothesized that similar group differences could arise via distinct model mechanisms. EEG gamma% and ITPC from 21 HC and 21 SCZ constrained an auditory front-end coupled to a Wilson-Cowan E/I model. We compared front-end-restricted, back-end-restricted, and full-joint parameter searches, plus perturbation and fixed-point analyses. HC means exceeded SCZ for both metrics ...

---

### 45. Structurally Constrained Brain Network Dynamics Reveal Reduced Functional Flexibility in Cocaine Use Disorder

**Authors:** Seyed Majid Razavi, Saeed Tajik Hesarkuchak, Triet M. Tran, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28892v2) | 📄 [PDF](https://arxiv.org/pdf/2608.28892v2)

**Summary:** Cocaine Use Disorder (CUD) is associated with widespread alterations in large-scale functional brain networks, yet the mechanisms contributing to these changes and their relationship to clinical and cognitive outcomes remain poorly understood. To address this gap, we introduce a framework to extract structurally informed dynamic functional connectivity patterns. We then leverage these connectivity patterns to characterize differences in functional brain network organization associated with CUD a...

---

### 46. A large dataset of human EEG responses to short naturalistic videos for studying dynamic visual event processing

**Authors:** Alessandro T. Gifford, Pablo Oyarzo, Anne W. Zonneveld, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28768v2) | 📄 [PDF](https://arxiv.org/pdf/2608.28768v2)

**Summary:** Vision neuroscience has experienced a surge in the collection and use of large-scale datasets of brain responses to naturalistic images. However, static images lack the temporal dimension essential for understanding how vision is solved in the brain during dynamic real life settings. To facilitate the study of the neural correlates of dynamic visual event perception, we introduce the EEG Moments Dataset (EMD). EMD consists of 128-channel EEG responses and eye-tracking recordings of 6 human parti...

---

### 47. Adaptive self-organized criticality in deep neural networks

**Authors:** Simon Vock, Christian Meisel

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28431v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28431v1)

**Summary:** Deep neural networks are high-dimensional dynamical systems whose function depends on the stable propagation of activity and perturbations across many layers. Maintaining suitable dynamical regimes may therefore be essential for robust learning and for preventing dynamical instabilities during training. Here, we show that the global dynamical state of a deep neural network can be autonomously regulated by purely local homeostatic plasticity. Neuronal activity is inferred from responses across in...

---

### 48. Relational Knowledge Distillation Brings DNN Representations Close Enough to Humans to Be Aligned Without Supervision

**Authors:** Yuria Shimizu, Soh Takahashi, Takato Horii, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.27877v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27877v1)

**Summary:** Linking the internal representations of deep neural networks (DNNs) to human mental representations is important for using DNNs as computational models of human vision. Existing DNN representations remain insufficiently similar to human mental representations, which are not directly observable and are therefore commonly measured through large-scale similarity judgments of object images. A natural approach to narrowing this gap is to directly transfer the relational structure of human representat...

---

### 49. Leveraging a Foundation Model for the EEG-Based Diagnosis of Alzheimer's Disease

**Authors:** Maggie Lin, Chung-Lin Hou, Tzyy-Ping Jung

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27719v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27719v1)

**Summary:** Biological heterogeneity in Alzheimer's Disease (AD) poses a critical diagnostic challenge, particularly for traditional linear methods that fail to capture non-linear neural dynamics. To address this, we propose a diagnostic framework utilizing the Large Brain Model (LaBraM), pretrained on over 2,500 hours of EEG data. By integrating these high-dimensional latent embeddings with a non-linear Random Forest classifier, our approach effectively isolates robust disease markers. Under a rigorous sub...

---

### 50. A weighted model of perception and decision-making between targets of finite size

**Authors:** W. Christopher Strickland, Andrew J. Bernoff

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27670v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27670v1)

**Summary:** Recent research grounded in experiments has connected neural ring models of vision to how animals navigate a complex landscape of attractive targets. In this paper we investigate the mathematical and biological implications of a three-stage model where animals pre-process visual stimuli to identify a discrete set of targets, process this input to select the dominant targets, and then post-process this information to navigate the landscape. Incorporating finite target sizes and a neural density a...

---

## stat.ML

**50 papers**

### 1. General Quantification of Covariate and Concept Shifts

**Authors:** Hongbo Chen, Li Charlie Xia

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11918v1)

**Summary:** Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging entropic optimal transport, we propose a key notion: $γ^{*}\!$-concept shifts, and derive a general ...

---

### 2. Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

**Authors:** Masahiro Kato, Daiki Honma, Taka Kato

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11915v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11915v1)

**Summary:** Generative artificial intelligence changes how firms reach customers, but standard marketing data do not record how often users see and notice a firm's name in generated answers. We develop Generative Marketing Mix Modeling (GMMM) to estimate the causal effects of Generative Engine Optimization (GEO) and Generative Engine Marketing (GEM). For GEO, GMMM combines repeated generated answers with question counts, shares of use across generative systems, and notice probabilities. For GEM, it combines...

---

### 3. Evaluating Time-Series Foundation Models and Multimodal Dietary Context for CGM Forecasting

**Authors:** Bowen Zhang, Hsiu-Wen Cheng, Hongyu Yang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11872v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11872v1)

**Summary:** Continuous glucose monitoring (CGM) provides high-frequency measurements of glucose dynamics and enables short-term glucose forecasting for diabetes management. Although time-series foundation models have shown strong general forecasting ability, their effectiveness for CGM prediction and the added value of multimodal dietary context remain unclear. We conduct a comprehensive empirical study using eight public CGM datasets spanning Type 1 diabetes, Type 2 diabetes, and non-diabetes populations. ...

---

### 4. Quantitative Diffusive Limits for Singular Nonlocal Transport

**Authors:** Andrea Agazzi, Giuseppe Bruno, Federico Pasqualotto, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11837v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11837v1)

**Summary:** We study the nonlocal continuity equation \[ \partial_tμ_b =\operatorname{div}\!\left( μ_b\nabla\log\bigl((I-b^2Δ)^{-1}μ_b\bigr) \right) \] on a closed connected Riemannian manifold. For smooth strictly positive initial data, we prove that as $b \to 0$, its global solution converges to heat flow $μ(t)$ at the sharp, uniform-in-time rate \[ \sup_{t\ge0}\|μ_b(t)-μ(t)\|_{L^1}\le Cb^2. \] The key estimate is the uniform dissipation of a $b$-weighted higher-order resolvent energy, which yields expone...

---

### 5. Near-Optimal Reinforcement Learning with Multi-Step Transition Lookahead

**Authors:** Corentin Pla, Hugo Richard, Marc Abeille, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11807v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11807v1)

**Summary:** We study reinforcement learning (RL) with transition look-ahead, where the agent may observe which states would be visited upon playing any sequence of $\ell$ actions before deciding its course of action. Although look-ahead can substantially improve achievable performance, it is known that optimal planning with multi-step transition look-ahead is NP-hard, but this hardness was established using discount factors arbitrarily close to one. It was therefore unknown whether the problem remains hard ...

---

### 6. Sparsity Regularized and Robust Mean Variance Portfolio Selection Under Ellipsoidal Uncertainty

**Authors:** Deniz Akkaya, Emre Can Yayla, Buse Şen, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11749v1)

**Summary:** We investigate mean-variance portfolio selection with an $\ell_0$-penalty to promote sparsity in asset allocations. Uncertainty in the mean return vector is incorporated through an ellipsoidal uncertainty set, yielding a robust sparse optimization framework. We characterize the structure of both local and global minimizers and exploit these properties in the risk minimization and return maximization formulations. Building on this structural insight, we develop a branch-and-bound algorithm tailor...

---

### 7. Generalization Analysis of Distributed Kernel-based Robust Gradient Descent Algorithms

**Authors:** Jun-Yi Meng, Zheng-Chu Guo, Yuan Mao

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11712v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11712v1)

**Summary:** In this paper, we investigate the generalization performance of distributed gradient descent algorithms in a reproducing kernel Hilbert space under a robust loss function $l_σ$. By exploiting the spectral characterization of gradient descent together with the intrinsic properties of robust loss functions, we establish optimal learning rates for the distributed kernel-based robust gradient descent (DKRGD) algorithm with an appropriately chosen scale parameter $σ$. The proposed parameter choice of...

---

### 8. Stress-Testing Dynamical and Generative Downscaling Using Subseasonal Extreme Precipitation Forecasts

**Authors:** Mauricio Lima, Marika Koukoula, Romain Pilon, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11696v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11696v1)

**Summary:** Coarse spatial resolution limits the ability of subseasonal prediction models to resolve extreme precipitation. Downscaling with either dynamical or deep generative models can overcome this issue, but the comparative performance of these models for extremes across different atmospheric regimes remains poorly understood. In this work, we evaluate the Weather Research and Forecasting (WRF) model against a diffusion-based generative model by downscaling two physically distinct, extreme precipitatio...

---

### 9. RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate Time Series Imputation

**Authors:** Ramiro Valdes Jara, David Chapman, Adam Meyers

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11648v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11648v1)

**Summary:** Multivariate time series imputation (MTSI) aims to recover missing values in temporal data composed of multiple interdependent variables. This problem is central to real-world applications such as healthcare monitoring, traffic networks, and energy systems. Recent diffusion-based approaches have shown strong potential for probabilistic imputation by learning to generate missing values through iterative denoising. However, most existing approaches perform diffusion directly in the original data s...

---

### 10. Identifiability of Nonnegative Tensor Decompositions via Positive Scattering

**Authors:** Haoming Wang, Ming Yuan

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11606v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11606v1)

**Summary:** Identifiability of tensor decompositions is often established through linear-algebraic conditions on the factor families. For nonnegative decompositions, however, positivity provides additional information that is not captured by dimension and independence alone: nonnegative terms cannot cancel, and their supports constrain competing decompositions. We introduce a positive scattering term that quantifies this additional source of identifiability and combine it with the dimension budget underlyin...

---

### 11. A distribution-free certification framework for trustworthy crash-severity prediction

**Authors:** Amir Rafe, Subasish Das

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11592v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11592v1)

**Summary:** Crash-severity models inform screening, dispatch and site prioritization, yet are deployed without a finite-sample statement of what one prediction means. Off-the-shelf guarantees fail here, because the features that make crash severity distinctive defeat them: the KABCO outcome is ordinal, the recorded label is a field assessment agreeing with medical severity about half the time, erring in a structured way, and deployment crosses jurisdictions and years calibration never saw. We develop a cert...

---

### 12. Risk-Averse Decision Making with Multi-Level Reliability Guarantees

**Authors:** Amirmohammad Farzaneh, Osvaldo Simeone

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11524v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11524v1)

**Summary:** Many applications in engineering, including wireless broadcasting, require designs that provide performance certificates at different target outage levels. This paper studies the problem of maximizing the weighted average of such certificates in the presence of uncertainty about the true system state. The problem is shown to be equivalent to an optimization over nested prediction sets, connecting to the literature on conformal prediction and extending prior art on single-level risk-averse decisi...

---

### 13. Generalized Score Matching for Parameter Estimation on Convex Domains

**Authors:** Nishanth Shetty, Saisuchith Mahajan, Chandra Sekhar Seelamantula

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11521v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11521v1)

**Summary:** Maximum likelihood (ML) estimation is a principled and statistically efficient approach for learning probabilistic models. However, for unnormalized models, ML estimation requires evaluating the partition function and differentiating through it, which may not always be tractable. Score matching provides a practically viable alternative that circumvents this obstacle by fitting the score in a way that eliminates dependence on the normalizing constant. We derive the generalized score matching obje...

---

### 14. Improving the Sensitivity of Gravitational Wave Detection with Weighted Conformal Prediction

**Authors:** Ann-Kristin Malz, Gregory Ashton, Nicolo Colombo

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11401v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11401v1)

**Summary:** In the last decade, kilometre-scale interferometric gravitational-wave detectors have observed hundreds of compact binary mergers, the majority of which are binary black holes. However, the data are noise-dominated, and multiple independent search algorithms (pipelines) are used to enhance sensitivity and improve robustness. Rather than the standard approach of selecting the most significant pipeline output, we combine the outputs from all pipelines using a conformal prediction-based framework t...

---

### 15. Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

**Authors:** Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11310v1)

**Summary:** We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen.   We identify two key design choices. First, placing prompt tokens at...

---

### 16. A Hilbert-Valued Functional Decomposition Framework for Explaining Time-Dependent Outputs

**Authors:** Sophie Hanna Langbein, Niklas Koenen, Marvin N. Wright, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11295v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11295v1)

**Summary:** Feature-based explanations quantify features' influence on model predictions, but are primarily designed for scalar outputs. In many applications, however, outputs are functional or multivariate, such as time-dependent trajectories in demand forecasting. Consequently, existing approaches typically explain each output location independently, ignoring dependencies across the output components. We address this limitation by developing a unified framework for feature-based explanations of time-depen...

---

### 17. Hierarchical Clustering Can Jointly Satisfy Richness, Consistency, and Scale Invariance

**Authors:** Daichi Kuroda, Maximilien Dreveton, Matthias Grossglauser, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11173v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11173v1)

**Summary:** Despite its ubiquity, clustering lacks a universally accepted definition of what is a cluster. Kleinberg's Impossibility Theorem formalizes this difficulty by showing that no flat clustering method can simultaneously satisfy three natural axioms: scale invariance, richness, and consistency. In this paper, we ask whether this impossibility persists when the output is a hierarchy rather than a single partition. We show that, in contrast to the flat clustering setting, the hierarchical analog of th...

---

### 18. How Wrong Can a Good Predictor Be? Diverging Updates with Vanishing Predictive KL

**Authors:** Qifu Wen, Shuaijun Liu, Zihan Zhou, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11132v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11132v1)

**Summary:** Accurate posterior prediction need not require accurate approximation of Bayesian updates. We prove that an unbounded gap between the update maps can coexist with vanishing predictive KL for every fixed finite $K\ge2$ in a stationary symmetric Gaussian HMM. Exact Bayesian mixing and an explicit deterministic radial filter act on the same $K-1$ belief coordinates. As $q\to0^+$, their separation in centered logits in the worst case grows at least linearly in the natural confidence scale $L_K(q)$, ...

---

### 19. Conformal-DRO: Distributionally Robust Optimization with Conformalized Ambiguity Set

**Authors:** Luhao Zhang, Shixiang Zhu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11073v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11073v1)

**Summary:** Data-driven distributionally robust optimization (DRO) typically treats the conditional outcome law as fixed and uses ambiguity sets to capture estimation error. This paper studies latent distributional heterogeneity, where each instance has an unobserved law but contributes only one observation, so uncertainty persists even if the mixture law is known. We propose Conformal-DRO, which uses nested conformal regions to construct an ambiguity set for the future latent law. Under exchangeability, th...

---

### 20. Importance Weighting for Unlabeled-unlabeled Learning under Distribution Shift

**Authors:** Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10994v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10994v1)

**Summary:** Unlabeled-unlabeled (UU) learning allows us to learn a binary classifier from two sets of unlabeled data with different class-priors. It is a general framework because it includes a wide variety of supervised learning such as positive-unlabeled (PU) learning, noisy label learning, and similarity-based learning. Existing UU learning assumes that the test and training distributions have the same class-conditional densities. However, this assumption rarely holds in practice due to distribution shif...

---

### 21. Phases in a class of associative memories via hidden neurons

**Authors:** Toshihiro Ota, Masato Taki

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10976v1)

**Summary:** Associative memory in the Hopfield network is attractor dynamics in a disordered many-body system, and higher-order and exponential extensions turn its retrieval update into softmax attention. The polynomial and exponential regimes have been analyzed by different methods, with no common architecture in which to ask what fixes the storage scale. In this paper we study the bipartite architecture of Krotov and Hopfield, which we call the class $H$, whose model is fixed by a Lagrangian for each laye...

---

### 22. AUC Maximization from Biased Positive-unlabeled Data with Confidence

**Authors:** Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10928v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10928v1)

**Summary:** Maximizing the area under the receiver operating characteristic curve (AUC) is a standard approach to imbalanced binary classification. Although positive and negative data are required for maximizing the AUC, negative data are often difficult to collect in some real-world applications due to privacy concerns or the need for specialized expertise to annotate them. Thus, AUC maximization from positive and unlabeled (PU) data has been attracting attention. Existing methods assume that labeled posit...

---

### 23. Relatively Smart II: Tractable or Semi-Supervised Instance-Optimal Learning

**Authors:** Shaddin Dughmi, Alireza F. Pour

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10886v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10886v1)

**Summary:** We continue the study of relatively smart learning, introduced by Dughmi and Pour (2026), which asks a supervised learner to compete, marginal by marginal, with every distribution-fixed error guarantee soundly certifiable from unlabeled data. They showed that the One-Inclusion Graph (OIG) learner is relatively smart with a quadratic sample-complexity blowup, and that no relatively smart learner can do better, leaving open whether ERM or another natural or tractable learner achieves comparable gu...

---

### 24. Learning Orthogonal Multi-Index Models Beyond Small Initialization: Incremental Learning, Competitive Dynamics and Symmetry

**Authors:** Mo Zhou, Weihang Xu, Simon S. Du, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10879v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10879v1)

**Summary:** Recent work has identified incremental learning in shallow networks trained on single-index and multi-index models. However, existing analyses often rely on simplifying settings, such as small initialization, correlation loss, or layer-wise training. These choices reduce neuron interactions and leave some feature learning dynamics under standard initialization unexplored. We study training dynamics for polynomial-width two-layer networks learning orthogonal multi-index targets under standard ini...

---

### 25. Flow Duality and Source Geometry for Categorical Generation

**Authors:** Etrit Haxholli

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10863v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10863v1)

**Summary:** Continuous and discrete flow matching are usually treated as separate constructions. This paper identifies a duality between them: projecting continuous convex-interpolant paths with one-hot targets through a position-wise argmax yields discrete convex-interpolant paths. The result requires source laws with appropriate coordinate symmetry and boundary regularity, and it makes the continuous source distribution an explicit design choice for categorical generation. We derive the induced discrete i...

---

### 26. Weighted Empirical Risk Minimization for Machine Learning under Long-Range Dependence: Exact Pathwise Rates and Learning-Error Geometry

**Authors:** Elina Moldavskaya

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10767v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10767v1)

**Summary:** We develop an exact almost-sure learning theory for smooth parametric models trained by regularly weighted empirical risk minimization on long-range dependent data. The training observations are generated from a fixed finite window of a stationary Gaussian sequence, and the sample weights are regularly varying. If the loss gradient at the population minimizer has Wiener-chaos rank $m$ and a nonzero low-frequency coefficient, then, in the long-memory interior regime, the finite-lag score reduces ...

---

### 27. Conformal Calibration Transfer

**Authors:** Achref Doula

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10737v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10737v1)

**Summary:** Conformal prediction converts point predictions into set-valued predictions with coverage guarantees under exchangeability between calibration and deployment data. We study conformal calibration transfer, where this requirement fails because labeled calibration is available only in a source space, while prediction sets are needed in a target space linked to the source through unlabeled paired observations (e.g., paired modalities or sensor changes). We propose Transported Conformal Calibration (...

---

### 28. A Quantum-Inspired Dequantization Method for Diagonally Weighted Matrix Functions: Application to Learning with Optimized Random Features

**Authors:** Natsuto Isogai, Mio Murao, Hayata Yamasaki

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10729v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10729v1)

**Summary:** Quantum-inspired classical algorithms have dequantized several quantum machine learning routines by replacing quantum linear-algebra subroutines with classical counterparts. However, the sampler based on quantum singular value transformation (QSVT) for learning with optimized random features is not covered by existing dequantization frameworks, because the matrix to be inverted is not itself available through sampling access. In this work, we develop a classical algorithm to address this type of...

---

### 29. Likelihood-free inference with nuisance parameters through normalizing flows

**Authors:** Phil Assheton

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10534v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10534v1)

**Summary:** We present a simple decomposition of a neural-network-based normalizing flow that naturally uncovers a pivotal statistic (or something close) in the presence of nuisance parameters, based only on a sample generator from the distribution of interest. We show that the statistic is near-pivotal in the sense of minimum average KL-divergence of its $p$-values versus uniform and we argue that it can be expected to have good power when the dimension of the statistic equals the dimension of the paramete...

---

### 30. A positive resolution of the gap-entropy conjecture

**Authors:** P. M. Aronow, Nathan Kallus, Patrick Lopatto

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10529v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10529v1)

**Summary:** We prove the gap-entropy conjecture for fixed-confidence best-arm identification with independent unit-variance Gaussian arms, means in $[0,1]$, and a unique optimal arm. For each suboptimal arm $i$, let $Δ_i=μ_*-μ_i$ be its gap from the optimal mean, and write $H=\sum_{i\ne *}Δ_i^{-2}$. Let $p_r$ be the fraction of $H$ contributed by arms with $2^{-(r+1)}<Δ_i\le2^{-r}$, and let $\mathrm{Ent}(I)=\sum_{r:p_r>0} p_r\log(1/p_r)$. Among all algorithms that identify the optimal arm with probability a...

---

### 31. An Exponential Deterministic--Randomized Gap in ERM-Oracle Complexity for Thresholds on an Unknown Order

**Authors:** Xuan Li

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10196v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10196v1)

**Summary:** Attias, Hanneke and Ramaswami (NeurIPS 2025) asked whether randomization provably reduces the oracle calls needed for online learning when the class is accessible only through an oracle. We study the instance they singled out: transductive online learning of thresholds on an unknown total order of T instances, with a consistency-type ERM oracle that returns a full concept consistent with a queried labeled set (or reports non-realizability). Our main result is a separation for a fixed natural ora...

---

### 32. A statistical approach to bias in zero-shot learning: the lens of handwriting recognition

**Authors:** Clarence Chew, Gim Siang Chia, Sukalpa Chanda, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10084v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10084v1)

**Summary:** Generalized zero-shot learning (GZSL) has emerged as an important paradigm for visual recognition systems that must generalize to classes that were not observed during training. Traditional GZSL techniques are limited by their applicability to a relatively small number of such unseen classes, scalability beyond which is challenging due to its well-known misclassification bias towards classes observed during training. In this work, we investigate the GZSL paradigm through the lens of zero-shot ha...

---

### 33. Optimal Value Inference for Reinforcement Learning

**Authors:** Nan Lu, Ethan Lee, James M. Robins, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09981v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09981v1)

**Summary:** We study offline inference for the optimal value in reinforcement learning. Two new nuisances are derived as fixed points of a self-induced Bellman equation, in which we approximate the maximum Bellman operator by its softmax correspondence. We propose a debiased estimator through the Neyman orthogonality and establish its asymptotic normality under diverging horizons even when the behavior policy changes with time, as long as the nuisances have the statistical rates that can be achieved by many...

---

### 34. Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending

**Authors:** Gijs A. F. Niewzwaag, Marijn G. S. Veth, Manuele Massei, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09945v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09945v1)

**Summary:** Machine learning-based credit scoring is increasingly central to Peer-to-Peer (P2P) lending, yet its resilience to adversarial manipulation, where applicants strategically alter self-reported inputs to secure favourable decisions, remains poorly understood. Most adversarial-robustness evidence comes from image and text domains and evaluates a single attack against a matching defence, offering little guidance on how defences generalise across attack types in tabular credit data. We address this w...

---

### 35. FlowCPO: A Unified Divergence View of Preference Alignment for Flow Models

**Authors:** Yansen Han, Shengyi Liao, Peng Sun, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09905v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09905v1)

**Summary:** Preference alignment for flow and diffusion models now spans online reinforcement learning and offline preference optimization, but the relation between these methods remains unclear. In particular, existing forward-process alignment methods require fresh samples from the current model, while offline methods based on fixed preference pairs rely primarily on positive-only fine-tuning or DPO-style likelihood-ratio surrogates. We organize these approaches through a divergence-based framework and in...

---

### 36. Beyond Conventional Federated Learning via High-Order Regularization

**Authors:** Alireza Kabgani, Masoud Ahookhosh

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09904v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09904v1)

**Summary:** Federated clients that perform several local optimization steps can return parameter displacements with widely different magnitudes. The quadratic regularization of FedProx grows linearly with displacement and therefore offers limited control over the contrast between ordinary and unusually large client movements. We here introduce HiFedProx, which replaces the quadratic penalty with a scale-matched power-type regularizer indexed by $p\geq2$. All powers have the same regularization-gradient magn...

---

### 37. A Unifying Perspective on Probabilities as Model Predictions

**Authors:** Benedikt Höltgen

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09855v1)

**Summary:** Although probabilistic statements are ubiquitous, foundational disagreements persist about their understanding, as exemplified by debates between Bayesians and frequentists; moreover, it is unclear when and why acting on them actually leads to desirable outcomes. Here, we argue that every probability is the output of a \emph{prediction method}, that is, it depends on both a particular way of constructing abstractions and a way of transforming them into predictions. Through this, we provide a uni...

---

### 38. Muon-C: Operator-Aligned Muon for Convolutional Kernels

**Authors:** Jiaxin Qing, Lexin Li

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09676v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09676v1)

**Summary:** Muon replaces matrix momentum with an approximately orthogonal polar direction, but its geometry depends on the matrix representation. For convolution, standard unfolding describes a local patch map rather than the convolution operator. We introduce Muon-C, an operator-aligned optimizer that represents kernel momentum as frequency-wise channel-transfer matrices, polarizes these blocks independently, and uses a critical Fourier grid to return updates exactly to the original finite kernel support....

---

### 39. Why Learning Rediscovers the Closed-Form Diagonal Regularizer

**Authors:** Jeahn Han, Pyojin Kim

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09656v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09656v1)

**Summary:** We identify a diagonal saturation principle in modal inverse problems: when truncation noise is isotropic, the Bayes-optimal Tikhonov shape is a closed-form power law Gamma_k proportional to lambda_k^|s| set by the prior alone, independent of the domain. Berry's random-wave conjecture decorrelates the truncation noise across modes, and Weyl's eigenvalue counting law supplies enough modes for the conclusion to survive empirical Berry violations. Together they predict an approximately flat loss la...

---

### 40. Distillation of Synthetic Data for Time Series Foundation Models

**Authors:** Niloy Biswas, Noureddine El Karoui

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09586v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09586v1)

**Summary:** Time series foundation models (TSFMs) are increasingly pre-trained on synthetically generated time series trajectories, where the data generating process is known. Current pre-training recipes are based on loss objectives which compare TSFM outputs to realized future values of each trajectory. We instead propose loss objectives which compare TSFM outputs to the conditional forecast distribution of each trajectory, a procedure we call synthetic data distillation (SDD). SDD corresponds to a Rao-Bl...

---

### 41. Learning with Synthetic Data via SGD in High-Dimensional Linear Regression

**Authors:** Jichu li, Difan Zou

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09572v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09572v1)

**Summary:** Synthetic data has become a promising way to scale model training beyond limited human-generated data but it may also induce strong model collapse (Dohmatob et al., 2024), where any fixed fraction of synthetic data prevents model performance from improving under data scaling, leaving a non-vanishing excess risk floor. In this paper, we study how synthetic data affects the generalization of one-pass SGD in high-dimensional linear regression with model shift. We establish finite-sample risk bounds...

---

### 42. High-probability guarantees for linear accessibility in feature superposition

**Authors:** Enrico Vompa

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09556v1)

**Summary:** Neural networks can leverage feature superposition to encode more concepts than dimensions, but cross-feature interference constrains the linear accessibility of simultaneously active features. By framing linear accessibility as a compressed sensing problem, we derive high-probability bounds for fixed supports under subgaussian noise, proving the sufficient dimension scales linearly ($d=O_{\varepsilon}(k \log m)$) rather than prior worst-case quadratic limits. We then validate these bounds acros...

---

### 43. Oracle Complexity of Stochastic Fixed-Point Equations with Nonexpansive Maps

**Authors:** Jelena Diakonikolas, Cristóbal Guzmán, David Martínez-Rubio

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09524v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09524v1)

**Summary:** We study the oracle complexity of computing a point with small fixed-point residual $\|T(x)-x\| \leq ε$, for a general norm $\|\cdot\|$ and a self-map $T$ of a compact convex set. We study this problem in the setting where $T$ is nonexpansive with respect to the same norm $\|\cdot\|$ and accessed via an unbiased stochastic oracle with bounded variance $σ^2$. We provide an algorithm that solves such instances for any norm with a weak Rademacher type $q > 1$, with high probability. The algorithm i...

---

### 44. Recovery Theory for Projected Power Iterations in Permutation Synchronization

**Authors:** Vahan Huroyan, Gilad Lerman

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09502v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09502v1)

**Summary:** We study the projected power method (PPM) for synchronizing \(n\) unknown permutations of \(m\) objects under a possibly sparse uniform corruption model. Each pair is observed with probability \(p\), and an observed measurement is uncorrupted with probability \(π_0\) and is otherwise an independent uniform permutation. Under \(\log m=o(npπ_0^2)\), we prove exact one-step recovery (with high probability) of each prescribed block for an independent estimate with a fixed positive majority of correc...

---

### 45. Gaussian Approximation for Multivariate Martingale Sums from Uniformly Ergodic Markov Chains

**Authors:** Yixuan Zhang, Qiaomin Xie

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09480v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09480v1)

**Summary:** We develop Gaussian approximation bounds in higher-order Wasserstein distance $W_p$, $p\geq2$, for sums of multivariate martingale differences generated by a uniformly ergodic Markov chain. Under an $L^{(2+η)p}$-moment condition with $η>0$, we establish the explicit bound $$ O\left( p^3 \|A\|_4^2 + pd^{1/4}\|A\|_2^{1/2}\|A\|_4^2 \right) $$ where $A\in\mathbb{R}^n$ collects the $L^{(2+η)p}$-sizes of the $n$ individual martingale increments. In the balanced-increment regime where the individual in...

---

### 46. Mode Coverage in Normalizing Flow Boltzmann Generators via Log-Ratio Variation

**Authors:** Qi Feng, Rongjie Lai, Di Qi, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09473v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09473v1)

**Summary:** Normalizing flow Boltzmann generators retain a tractable pushforward density, but training with forward KL depends on target samples that may be biased or omit modes. As a result, a flow can miss target mass while its observed importance weights give a high effective sample size. We introduce the log-ratio variation $\X_ω$, the mean absolute pairwise difference of the target-to-pushforward log-density ratio under a weighting measure $ω$, and use it to define KLXX, a new loss function. Two log-ra...

---

### 47. MiNCE: Nonparametric, Strongly Consistent Confidence Envelopes for Band-Limited Functions and their Smoothed Spectra

**Authors:** Balázs Csanád Csáji, Bálint Horváth

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09436v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09436v1)

**Summary:** Minimum-norm confidence envelope strategies offer a nonparametric approach to constructing nonasymptotic, simultaneous confidence regions for band-limited functions, exploiting the theory of Reproducing Kernel Hilbert Spaces (RKHS). While the finite-sample coverage guarantees of these envelopes have been established, their consistency has not been analyzed so far. In this paper, we study this construction, here termed the Minimum-Norm Confidence Envelope (MiNCE) framework, and establish the stro...

---

### 48. Tensor-Train Weak SINDy: Identifying High-Dimensional Nonlinear Dynamics

**Authors:** Will Houser, Vanja Dukic, David M. Bortz

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09434v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09434v1)

**Summary:** In recent years, weak-form methods have made significant advances in data-driven discovery of dynamical systems. However, in high-dimensional settings, current techniques can prove expensive in both computation and memory. In this work, we introduce TT-WSINDy, which combines techniques of the Multidimensional Approximation of Nonlinear Dynamics (MANDy) and Weak Sparse Identification of Nonlinear Dynamics (WSINDy) methods, implementing requisite computations in the tensor-train (TT) format. We de...

---

### 49. Nearly Tight Rademacher Bounds for Sparsely Activated Neural Networks

**Authors:** Xiaoyu Li, Zhizhou Sha, Jiaojiao Jiang, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09130v1)

**Summary:** An input may activate few hidden units even when different inputs collectively use an entire network. We study the statistical complexity of this input-dependent sparsity in the one-hidden-layer ReLU model of Awasthi et al. (COLT 2024). For width $s$, at most $k$ active units per input, and effective weight and bias bounds $W,B$, every size-$m$ sample in the class's fixed radius-$R$ input domain satisfies $\mathcal{R}(S)\le CWR\min\{k,\sqrt{sk/m}\log^{3/2}(2m)\}+kB/\sqrt m$. A support-preserving...

---

### 50. A Generalization of Amari's Bayesian Duality

**Authors:** Mohammad Emtiyaz Khan, Thomas Möllenhoff

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09126v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09126v1)

**Summary:** Amari's contributions to information geometry and machine learning are well known. Here, we revisit Amari's work on Bayesian duality which has not received as much attention. We connect Amari's Bayesian duality to a convex duality of Bayes' rule. Using this connection, we present a generalization of Amari's Bayesian duality and discuss its relevance for modern artificial intelligence.

---

