# arXiv Daily Digest - 2026-11-02

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention

**Authors:** Ales Kubicek, Andrea Caciolai, Liangzu Peng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42147v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42147v1)

**Summary:** Agentic workflows are increasingly shifting towards long-horizon tasks, such as open-ended scientific work, where models benefit from long context windows. However, at ultra-long context (above 1M tokens), full attention is prohibitively expensive. A promising approach is sparse attention, in which a dedicated indexer selects a subset of keys for the attention. Yet current methods of indexing either still have quadratic cost in context size or lose accuracy at ultra-long context scale. We addres...

---

### 2. Hierarchical World Models with Implicit Dynamics

**Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42146v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42146v1)

**Summary:** Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from l...

---

### 3. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

**Authors:** Shengguang Wu, Suning Huang, Cherie Ho, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42141v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42141v1)

**Summary:** Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises ...

---

### 4. ACCT: Asymmetric Cross-LLM Context Transfer

**Authors:** Yuzhe Liu, Haolin Tian, Tonghan Wang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42116v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42116v1)

**Summary:** In real-world deployments, large language model (LLM) systems are increasingly evolving from single-model invocation toward heterogeneous deployments in which different models are dynamically invoked for inference. When the same context is reused across models, however, each newly selected target model typically has to process it again, repeatedly incurring substantial computational costs. Therefore, we propose ACCT (Asymmetric Cross-LLM Context Transfer), which targets KV cache transfer between...

---

### 5. Subquadratic Attention with a Hierarchical Tree-Structured Indexer

**Authors:** Leon Lufkin, Cutter Dawes, Alexander Speicher, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42112v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42112v1)

**Summary:** The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadrati...

---

### 6. CausalWAM: Learning the Causes of Actions in World Action Models

**Authors:** Juntao Cheng, Jinzhou Tang, Fan Feng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42096v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42096v1)

**Summary:** World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant latent variables), as the model could just as well learn to imitate in this way wh...

---

### 7. The Knowledge Layer Model (KLM): Evidence-Visible AI Output, Routing Diagnostics, and Negative Results

**Authors:** Omer Asim Ozturk, Cihan Aydiner

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42066v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42066v1)

**Summary:** AI answers require more than apparent correctness: reviewers need to inspect their recorded basis. We introduce the Knowledge Layer Model (KLM), an open, implementation-neutral specification for inference records with versioned epistemic assessments, evidence relations, and explicit unknowns. SEDIM, the knowledge and evidence architecture of Nage AI OS, is a reference implementation. We reference KLM v0.3 (repository tag v0.3.0). Empirical material consists of separate internal experiments, not ...

---

### 8. CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness

**Authors:** Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42054v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42054v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail to reinforce high-quality reasoning. Existing causality metrics assess CoT causality by perturbing the CoT, such as deleting reasoning steps or injecting errors, and measuring changes...

---

### 9. Near-Optimal Second-Order Convex Finite-Sum Optimization under Individual Smoothness

**Authors:** Xinliang Zhang, Lesi Chen, Zonghan Li, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42040v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42040v1)

**Summary:** We study the stochastic second-order oracle complexity of solving smooth convex finite-sum optimization with $n$ components. Very recently, Tsedenov \& Kovalev (2026) showed that the minimax optimal complexity under averaged smoothness and convexity is $\tildeΘ(n + n^{6/7} ε^{-2/7})$ by establishing nearly matching upper and lower bounds. In this paper, we show that individual smoothness and convexity provably enable further acceleration, where the lower complexity bound is $Ω(n+ n^{5/7} ε^{-2/7...

---

### 10. Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice

**Authors:** Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42039v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42039v1)

**Summary:** Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? We audit six widely deployed LLMs from four providers on smoking cessation, a domain with codified clini- cal guidance and substantial public-health stakes, by putting the same four cessation questions to twelve user personas that differ in life stage, self-described expertise, and smoking history, for ...

---

### 11. Learning Clean Generative Processes from Noisy Measurements

**Authors:** Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42036v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42036v1)

**Summary:** We study how to learn a generative model of clean images using only noisy observations. Diffusion processes and their generalizations to non-Gaussian noise require posterior predictions at every noise level. We first show that it is possible to learn these predictions from independent noisy views using Noise2Noise regression, but only at or above the noise level of the training data. To learn the predictions below that level, needed to generate clean images, we impose consistency: a prediction s...

---

### 12. There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?

**Authors:** Rhea Sanjay Sukthanker, Pashmina Cameron

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42030v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42030v1)

**Summary:** Looping re-applies a block of layers so that each token passes through the block more than once. Adding a loop to a trained model is attractive because it leaves the parameter count, and hence the disk size, the memory footprint and the training cost unchanged. Unfortunately, every generated token pays for the loop. Re-applying m of N layers makes each token about (N+m)/N times as expensive. Loops that a model learns during large-scale pretraining justify this price, but whether loops added afte...

---

### 13. Know When the Equation Is Wrong: Structural Uncertainty for LLM-Guided Symbolic Regression under Extrapolation

**Authors:** Mostafa Cham, Bayu Adhi Tama, Jianwu Wang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42024v1)

**Summary:** Large language models (LLMs) can help discover mathematical equations from data, but most LLM-guided symbolic regression methods focus on a single best equation without quantifying uncertainty over alternative functional forms. This is challenging because distinct equations can fit the observed data similarly while producing substantially different extrapolations. Our experiments on the LLM-SRBench dataset show that standard conformal intervals achieve nominal in-distribution coverage but freque...

---

### 14. TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents

**Authors:** Xiangyu Kong, Ruirui Yang, Xia Hou

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42004v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42004v1)

**Summary:** Multi-turn negotiation remains a challenging problem for large language model (LLM) agents. While LLMs can conduct natural-language dialogue, existing benchmarks predominantly assess only agreement rates, overlooking whether negotiated commitments actually create value once executed. To address this gap, we introduce TradeWar, a multi-country simulation benchmark that translates negotiation dialogues into concrete tariff and trade-share policies, enforces capacity and network constraints during ...

---

### 15. AutoAnalysis: An automated, self-updating meta-analysis of human-AI collaboration

**Authors:** Michelle Vaccaro, Abdullah Almaatouq, Thomas W. Malone

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42001v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42001v1)

**Summary:** As generative artificial intelligence (AI) becomes more capable and widely used, understanding when and how humans should work with these systems is becoming increasingly important. However, the empirical evidence in this space offers conflicting recommendations, which leaves individuals and organizations without clear guidance on when to combine human and AI capabilities. Existing meta-analyses can help reconcile these findings, but they require substantial manual effort and cannot readily inco...

---

### 16. SecPO: Principled Adversarial Training for Prompt Injection Security

**Authors:** Sizhe Chen, Yibo Peng, Jaewon Chang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41998v1)

**Summary:** Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under adaptive prompt injections. One reason is that DPO anchors the model around the undefended reference model, which is insecure. We show an idealized reference model---an injection-invaria...

---

### 17. DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention

**Authors:** Zhangchi Feng, Harry Jiang, Yangyifei Luo, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41994v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41994v1)

**Summary:** Linear attention scales linearly with sequence length, but its finite-state memory can limit long-context retrieval. In gated linear recurrences, memory retention depends on state decay, which is shaped jointly by gate parameters A_log and dt_bias and by input activations. In controlled Gated DeltaNet (GDN) experiments, both parameters remain highly correlated with their initial values after training, highlighting the importance of initialization. Therefore, we introduce Dual-Axis Memory Initial...

---

### 18. ID2Pattern: Pretraining Generalizable Identity Behavior Patterns for Transaction Risk Foundation Models

**Authors:** Ze Zhao, Haoyu Jiang, Weiyu Han, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41988v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41988v1)

**Summary:** Large-scale behavioral pretraining offers a promising route to generalizable representations in online payment systems. However, high-cardinality identity fields such as card, device, and account IDs, though rich in behavioral signals, remain underexploited. Their continually growing vocabularies and limited semantic meaning make existing vocabulary-based and semantics-based encodings ill-suited. Their generalizable signal lies not in specific values, but in the identity behavior patterns they e...

---

### 19. When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity

**Authors:** Jun Liu, Dajie Sun, Zhenglun Kong, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41970v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41970v1)

**Summary:** World-action models increasingly apply test-time scaling, spending extra inference computation on candidate selection and adaptive allocation to improve control. Such gains are credible only when candidates carry exploitable signal, nominal compute savings become real speedup, and evaluation stays reliable. We audit all three on Cosmos Policy and RoboCasa with a premise-first, pre-registered methodology. On clean data, a learned value selector is 1.66 pp worse than random; a hindsight oracle gai...

---

### 20. Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity

**Authors:** Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41968v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41968v1)

**Summary:** Weight pruning can reduce the storage and inference cost of large language models (LLMs), but preserving quality at high sparsity levels remains challenging. Existing methods face a quality-cost trade-off in this regime. One-shot pruning is cheap but degrades sharply as sparsity increases, even when followed by post-pruning recovery. A growing line of work instead optimizes the mask directly from the dense model under the end-to-end objective; among these methods, [Lee et al.,2026], the recent s...

---

### 21. Chronos-2: A foundation model for multivariate time series forecasting

**Authors:** Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41956v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41956v1)

**Summary:** Accurate forecasting with uncertainty quantification is critical in a variety of scientific applications ranging from epidemiology and economics to energy systems and earth sciences. Yet most forecasting models still need to be developed and trained separately for each domain-specific dataset. Time series foundation models (TSFMs) aim to remove this limitation and enable the application of the same model across domains through large-scale pretraining. However, most existing TSFMs treat each time...

---

### 22. Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions

**Authors:** Ning E, Changde Du, Yizhuo Lu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41951v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41951v1)

**Summary:** Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with the multidimensional mental representations underlying human similarity judgements. We build on a previously established behavior-derived semantic embedding space, in which objects ar...

---

### 23. Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning

**Authors:** Zhuguanyu Wu, Congjia Chen, Ruihao Gong, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41949v1)

**Summary:** Few-step flow models generate samples through a handful of large denoising transitions. Applying GRPO to such models requires introducing stochasticity into the denoising transitions, and when a single transition spans a wide range of noise levels, the choice of the resulting stochastic policy becomes a major factor in optimization. Recent constructions constrain the policy to preserve the target flow coefficients, but this constraint admits a family of policies and offers no criterion for choos...

---

### 24. Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI

**Authors:** Lorenzo Mazza, Ariel Rodriguez, Stefanie Speidel

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41946v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41946v1)

**Summary:** Embodied surgical AI requires reliable multimodal data, yet surgical data collection remains costly, difficult to repeat, and strongly dependent on the hardware setup. We present Sensorium, an open-source Python library for recording, processing, annotating, and curating multimodal surgical data from configurable robot and sensor streams using the Robot Operating System (ROS) and ROS2 middleware. The library combines operator-facing data acquisition, configurable processing, semantic annotation,...

---

### 25. Observable-Specific Validity Tests for Scientific AI: Controlled Approximations and Intervention Response

**Authors:** Xiaoshn Nee, Haobo Zhong, Xiaomin Ni

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41939v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41939v1)

**Summary:** An approximation can reproduce an energy while missing its response, or satisfy an error tolerance without being certified by a given bound. We formulate observable-specific validity records for scientific artificial intelligence (AI) that link a reduction to its reference model, error measure, tolerance, parameter domain, and transformations or interventions. Explicit displacement and velocity certificates for a singularly perturbed oscillator recover distinct convergence orders and provide suf...

---

### 26. Structure-Aware Skill Retrieval and Arbitration for Optimization Modeling

**Authors:** Anran Liu, Benzhao Hou, Zongsheng Cao, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41909v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41909v1)

**Summary:** Large Language Models (LLMs) can turn natural-language optimization tasks into solver-checked answers, but current agents remain brittle under narrative rewrites and often store reusable experience at the instance level. We introduce \textsc{ArchOR}, an archetype-centric skill agent that builds on \textsc{OptSkills} by adding two retrieval-focused modules. \emph{Centroid-Aware Representation Learning} (CARL) refines the ordering of cached skill representations through a low-rank prototype residu...

---

### 27. ReX-GG: a LLM Ensemble Pipeline for Relation-extraction and Graph Generation

**Authors:** Giacomo Magnifico, Eduard Barbu

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41901v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41901v1)

**Summary:** Current LLM ensemble frameworks focus on multi-step setups with additional modules for answer ranking, often opting for token and span analysis rather than structured outputs, leading to heavyweight architectures with potential fail states along the pipeline. Faster, lighter solutions are more vulnerable to hallucination propagation and can lack output control in more complex pipelines. This paper proposes a customisable, lightweight ensemble workflow of coordinated Large Language Models that le...

---

### 28. Using Machine Learning to Measure Self-Efficacy Belief Through Learners' Interaction Traces in Technology-Enhanced Learning

**Authors:** Maeva Somny, Linda Chouati, Marie Lefevre

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41900v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41900v1)

**Summary:** Self-efficacy beliefs play a critical role in learners' performance, academic choices, and, more broadly, in their future career trajectories. As Technology-Enhanced Learning (TEL) environments have demonstrated strong potential for supporting both performance and motivation, investigating self-efficacy within such environments is of particular interest, especially for implementing remedial practices as early as possible to support learners' self-efficacy beliefs. Our research aims to develop a ...

---

### 29. General-purpose foundation models surpass specialized ones on chemical property prediction tasks

**Authors:** Stepan N. Ostarkov, Gregorii A. Semakin, Ivan A. Bespalov, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41899v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41899v1)

**Summary:** Foundation models (FMs) learn reusable representations from large collections of unlabeled data. In chemistry the corresponding data mainly consists of molecular structures, which are abundant, whereas experimental measurements are scarce. Chemical FMs such as ChemBERTa and MoLFormer were therefore trained on diverse molecular structures to enable fine-tuning on small experimental datasets (less than 100 datapoints in most realistic scenarios) and subsequent property prediction. At the same time...

---

### 30. Automated Keyword Generation Using LLMs in a High-Volume Data Virtualization Service

**Authors:** Saiful Khan, Yiwen Xing, Joyraj Chakraborty, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41893v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41893v1)

**Summary:** In modern data infrastructure, a data virtualization service (DVS) allows users to create many versions of source datasets for different processing tasks. For example, a multivariate or multi-modality dataset can be used for different machine learning tasks (e.g., classification, detection, segmentation, forecasting, and so on). Data selection, participation, integration, and preprocessing in different tasks result in many virtual datasets [Khan et al., SSC 2026]. Meanwhile, different users need...

---

### 31. Fuzzy selective state model for forecasting the dynamics of consumer preferences

**Authors:** P. A. Golovinski, A. A. Drobyshev, A. O. Shatalova

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41879v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41879v1)

**Summary:** We consider forecasting the dynamics of consumer preferences of retail chain customers. A customer's preference is described by a triangular fuzzy number. The evolution of the preference over time is governed by a Mamba-type selective state space model whose hidden state is a triangular number, with computations carried out in M.G.~Matveev's two-component algebra of fuzzy numbers. The recurrence parameters are computed from crisp features, while the fuzzy part of the model remains linear with no...

---

### 32. AI evaluators favor job applications written by certain AI models, independent of candidate quality

**Authors:** Nicolò Pagan, Michael Andreas Ebling, Stefania Ionescu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41866v1)

**Summary:** Job applicants increasingly use large language models (LLMs) to write cover letters, while employers deploy LLMs to screen them. In this all-AI setting, we ask whether the \emph{choice of model} affects hiring outcomes independently of candidate qualifications. We introduce a multi-model auditing framework pairing eleven LLM writer agents with nine API-hosted evaluator agents across ten job descriptions and fifty candidates per job. Four findings emerge. First, we identify a generative preferenc...

---

### 33. Learning to Interact and Direct: Co-Evolving Video Director Agents

**Authors:** Yingzhao Jian, Zhongan Wang, Yuxuan Hou, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41865v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41865v1)

**Summary:** Video director agents orchestrate multistage production to realize users' creative visions. Emerging research on their self-evolution advances screenplay planning effectively. However, the mutual reinforcement between directing and user interaction remains largely overlooked. Improved interaction clarifies user intent and informs workflow refinement, while more reliable execution shifts collaboration from troubleshooting to creative decisions. To this end, we introduce LIT (Learning to Interact ...

---

### 34. SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding in Conversational XAI

**Authors:** Van Bach Nguyen, Qianli Wang, Nils Feldhus, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41856v1)

**Summary:** Conversational explainable AI (ConvXAI) agents often use GUS-style architectures with separate modules for intent recognition, dialogue management, and template-based response generation. While faithful to the underlying XAI methods, these pipelines are hard to adapt and often struggle with context-dependent follow-up questions. We present SimXAI, a lightweight LLM-centric conversational layer that replaces these modules with a single tool-calling LLM that bridges access to existing XAI resource...

---

### 35. Dynamical Memory Transformer: Selective Recurrent Memories with Constant Cost Attention

**Authors:** Yannis Bendi-Ouis, Xavier Hinaut

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41850v1)

**Summary:** Transformers retain an explicit history of the sequence, allowing attention to directly retrieve past representations. However, the size of the KV-Cache and the cost of a new token increase with the context length. State Space Models compress the past into a fixed-size recurrent state, at the cost of reduced addressability. We present the Dynamical Memory Transformer (DMT), a hybrid architecture that separates sequence encoding from information reading. The encoder uses several memory units, eac...

---

### 36. ReuScope: Auditing Data Reuse and Evaluation Sensitivity in Capsule Vision 2024

**Authors:** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41835v1)

**Summary:** We develop ReuScope, a protocol for auditing data reuse and evaluation sensitivity, using Capsule Vision 2024 as a case study. It combines measurements of data relationships with two comparisons: changing the evaluation population while holding predictions fixed, and changing training data while holding evaluation fixed. Byte-identical files cross the public training-validation boundary, and all 41 Kvasir-Capsule recordings that contribute frames occur in both partitions. Shared source recording...

---

### 37. RECAST: REconstruction of Chain-of-Thought via Auditable Structured Traces

**Authors:** Qi Wang, Kang Xu, Chengcheng Wan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41813v1)

**Summary:** Large closed-source reasoning models expose only their final answers. The intermediate reasoning that produces those answers is hidden behind API surfaces, tool-call policies, and safety filters. Existing chain-of-thought (CoT) extraction methods assume a side channel: a visible reasoning field, a scratchpad carried through tool calls, or a signed/encrypted reasoning block. We reproduce three representative state-of-the-art extraction methods and find that, on Claude-Sonnet-5.5 accessed through ...

---

### 38. Backpropagation-free Deep Learning for Time-Series Classification

**Authors:** Miha Kapš, Blaž Bertalanič, Carolina Fortuna

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41805v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41805v1)

**Summary:** Deep neural networks for time series classification (TSC) are trained almost exclusively by error backpropagation, which imposes update locking and the weight-transport problem. Backpropagation-free learning rules such as Direct Feedback Alignment (DFA), Direct Random Target Projection (DRTP), and the diffusion-inspired NoProp relax these constraints but have been evaluated almost exclusively on 2D image benchmarks. We adapt these three learners to univariate TSC with 1D convolutional architectu...

---

### 39. Accurate and Auditable ECG Classification via Visibility Graph Neural Networks

**Authors:** Artur Xavier, Guilherme Henrique Gomes Evangelista, Aitazaz Khan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41795v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41795v1)

**Summary:** Physicians read electrocardiograms (ECGs) from waveform shape and timing, yet accurate deep-learning classifiers rarely show which waveform regions drive their predictions. We introduce LYNX-ECG, a graph neural network that represents each heartbeat as a sparse visibility graph of timestamped turning points. On CODE-Test, LYNX-ECG reaches a macro F1 score of 0.889, outperforming five baselines including the ECGFounder foundation model, while its graphs need about 14% of the storage of graphs bui...

---

### 40. Whose Values, Which Contexts, and What Signals? Grounding Cultural Value Alignment with Re3Culture

**Authors:** Jing Yao, Hyunjin Hwang, Weihua Zheng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41793v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41793v1)

**Summary:** Cultural value alignment requires not only model optimization but also a well-specified target grounded in real-human evidence. Yet how such targets should be grounded in human data remains largely unexplored, raising three fundamental questions: (1) whose values should be represented? (2) where should cultural values be observed? and (3) what signals reveal underlying values? We investigate these questions through Re3Culture, a large-scale dataset linking (i) Representative communities: 700+ hu...

---

### 41. Implicit Assumptions About Tasks in Continual Learning

**Authors:** Kathrin Korte, Christian Metzner, Akshay Bedhotiya, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41792v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41792v1)

**Summary:** Continual learning is the study of how a model accumulates knowledge from data received over time, rather than all at once. In practice, this is typically achieved by dividing a dataset into tasks and presenting them sequentially. Explanations of the resulting measurements take into account factors such as the similarity between segments, the rate at which the data changes and the order of presentation. Each of these factors can be defined in terms of the underlying data, the partition imposed o...

---

### 42. Different Models, Shared Failures: Auditing Frozen-Encoder Pools for Medical Segmentation

**Authors:** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41790v1)

**Summary:** Average segmentation accuracy and model count do not reveal whether models fail on the same cases. We present CoFailMed, an audit of correlated failures in pretrained-encoder pools for medical segmentation. Across five 2D tasks, we evaluate 11 public pretrained encoders (a controlled sample, not a census) using frozen features and separately trained $1\times 1$ readouts with four seeds per encoder. Shared-checkpoint pairs have the highest mean per-case Dice correlation. An expanded 17-encoder an...

---

### 43. Clinical-Protocol-Aware Cyber Resilience for Connected Clinical Technologies Under AI-Enabled Adversarial Conditions

**Authors:** Pranav Patel, Siva Kannathasan, Prerak Patel, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41784v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41784v1)

**Summary:** Healthcare increasingly relies on connected medical devices, clinical information systems, cloud services, and distributed-care technologies, creating cybersecurity risks across clinical workflows. AI-enabled capabilities can accelerate vulnerability discovery and attack-path analysis, increasing the need to limit compromise propagation. This paper proposes a clinical-protocol-aware cyber-resilience framework based on bounded clinical micro-networks and controlled interconnections. The framework...

---

### 44. Multimodal In-Context Learning with Explicit Rule Induction

**Authors:** Yuquan Li, Xinyang Jiang, Yuhao Xue, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41754v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41754v1)

**Summary:** A central challenge in multimodal in-context learning (MICL) arises from tasks that are ill-defined without context and require uncovering the underlying rules from demonstrations. Existing methods predominantly treat MICL as direct input-output mapping, overlooking the importance of explicitly inducing and reasoning over such rules, limiting both performance and interpretability. We propose ERIM, Explicit Rule-Induction for Multimodal In-Context Learning, a unified framework that enhances MICL ...

---

### 45. Latent-Lens: Visual Perception in Small Language Models Through Latent Communication

**Authors:** Mo Shahdloo, Faegheh Sardari, Mathew Salvaris

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41751v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41751v1)

**Summary:** Bridging independent vision-language models (VLMs) and small language models (SLMs) in a modular multi-agent system typically forces them to exchange information as discrete text, which creates a lossy bottleneck for spatial and fine-grained details. This constraint is especially acute for SLMs, whose limited capacity makes them more reliant on the quality of the input signal. Recent latent-communication methods exchange states between language models. How a VLM can pass visual information to a ...

---

### 46. Simple Features Beat Most AI Control Monitors

**Authors:** Shubhrangshu Debsarkar, Valmik Nahata

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41713v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41713v1)

**Summary:** AI control relies on monitors to catch a capable model that sabotages its work. These monitors are evaluated on their ability to differentiate honest from backdoored code. We show that on a standard evaluation dataset, simple features beat most monitors without ever running the code, outranking 20 of 24 open-weight models prompted as monitors. The dataset gives its labels away in two ways. People wrote the honest solutions and older language models the backdoors, so the style of the code reveals...

---

### 47. Advancing Clinical Trial Outcome Prediction with Domain-Specific Large Language Models

**Authors:** Burak Bakkar, Hana Moalla, Mohamed Salem Jedidi, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41710v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41710v1)

**Summary:** Clinical trial failures are a major barrier to efficient drug development, incurring substantial costs and delaying patient access to effective therapies. Structured approaches such as the Hierarchical Interaction Network (HINT) predict trial outcomes by explicitly modelling interactions between drugs, diseases and protocols, but make limited use of the free text in trial registrations. We evaluate two domain-specific language models, BioBERT (108M parameters) and BioMistral (7B parameters), for...

---

### 48. TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents

**Authors:** Rui Yu, Chong Mu, Jinchuan Zhang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41697v1)

**Summary:** Training interactive language agents from terminal outcomes poses three coupled problems: which task and state continuations to sample, how to assign delayed feedback to decisions, and how to aggregate token losses for multi-token actions. We present TSBPO, a tree-structured sampling-to-update paradigm that addresses these problems within one training loop. A likelihood-fitted Root/Branch allocator uses retained task and state evidence to target continuations likely to produce contrasting termin...

---

### 49. When the Past Shapes Action: Understanding Embodied Memory

**Authors:** Siqi Li, Ziyi Bai, Xinrun Xu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41688v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41688v1)

**Summary:** Recent advances in generative foundation models have expanded the capabilities of embodied AI, enabling increasingly general navigation, manipulation, and long-horizon task execution. However, effective interaction with dynamic environments requires more than only strong perception and reasoning: agents must act with partial knowledge and retain, retrieve, and update information from past observations, actions, and experiences. This survey examines embodied memory as a mechanism for preserving d...

---

### 50. OT-CAL: Optimal-Transport-Guided Adaptive Sample Selection for Efficient Visual Learning

**Authors:** Suryansh Talukdar, Jin Soung Yoo

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41677v1)

**Summary:** Deep neural networks for image recognition are typically trained using mini-batches, with a forward pass to compute predictions and losses followed by a more computationally expensive backward pass to update model parameters. However, not all training samples contribute equally to learning, suggesting that computation can be reduced by performing backward passes only on informative samples. The challenge is that sample informativeness changes throughout training: difficult samples may be valuabl...

---

## cs.CL

**50 papers**

### 1. Latent Reasoning in Continuous Space for Unified Multimodal Models

**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42149v1)

**Summary:** Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space,...

---

### 2. Flide: Accelerating Decision Inference with Exact State Forking

**Authors:** Bobo Li, Jiajia Song, Hao Fei, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42148v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42148v1)

**Summary:** Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide, an efficient and exact inference engine that decouples the logical tree structure ...

---

### 3. DecisionRank: On-Policy Distillation for Decision-Model Rerankers

**Authors:** Yanran Wu, Dian Yu, Chongyang Bai, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42128v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42128v1)

**Summary:** Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the student determines the ranking using scores from the first-token position. To bridge this gap, we introduce DecisionRank, a decision model trained through item-space on-policy distilla...

---

### 4. Subquadratic Attention with a Hierarchical Tree-Structured Indexer

**Authors:** Leon Lufkin, Cutter Dawes, Alexander Speicher, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42112v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42112v1)

**Summary:** The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadrati...

---

### 5. RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language Models

**Authors:** Guangfu Guo, Xiaoqian Lu, Linsey Pang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42084v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42084v1)

**Summary:** Continuous diffusion language models show promising potential in text generation tasks, but are prone to problems such as text repetition, semantic drift, and generation quality degradation when the generation length exceeds the training length. To address these challenges, we propose RangeSWA, a training-free length extrapolation method. The method combines local sliding-window attention, remote block summaries, and dynamic content retrieval to preserve local details and support long-range cont...

---

### 6. The Knowledge Layer Model (KLM): Evidence-Visible AI Output, Routing Diagnostics, and Negative Results

**Authors:** Omer Asim Ozturk, Cihan Aydiner

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42066v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42066v1)

**Summary:** AI answers require more than apparent correctness: reviewers need to inspect their recorded basis. We introduce the Knowledge Layer Model (KLM), an open, implementation-neutral specification for inference records with versioned epistemic assessments, evidence relations, and explicit unknowns. SEDIM, the knowledge and evidence architecture of Nage AI OS, is a reference implementation. We reference KLM v0.3 (repository tag v0.3.0). Empirical material consists of separate internal experiments, not ...

---

### 7. PersonaChatBench: Evaluating Chat Assistants with Diverse Simulated Users

**Authors:** Zheyuan Deng, Taoran Li, Jingwen Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42060v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42060v1)

**Summary:** Conversational assistants are expected to help people with diverse backgrounds, preferences, and communication styles. Yet evaluations centered on a single cooperative user provide limited insight into how reliably an assistant serves users with different personas. We introduce PersonaChatBench, a framework for evaluating task competence and responsiveness to diverse user needs. PersonaChatBench pairs the same underlying task with multiple simulated users, each guided by a private persona card t...

---

### 8. CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness

**Authors:** Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42054v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42054v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail to reinforce high-quality reasoning. Existing causality metrics assess CoT causality by perturbing the CoT, such as deleting reasoning steps or injecting errors, and measuring changes...

---

### 9. Asynchronous Flow Map Language Models

**Authors:** Chanhyuk Lee, Wonjung Kim, Patrick Pynadath, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42018v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42018v1)

**Summary:** The order in which tokens are predicted in language modeling has a profound impact on the quality of generated sequences. Autoregressive and masked diffusion models iteratively fill in tokens and can exploit such orderings across generation steps, but how to leverage an ordering for one-step parallel language modeling is unclear. We introduce asynchronous flow map language models (aFMLMs), which incorporate prediction order into one-step modeling by learning the flow maps of asynchronous flows. ...

---

### 10. TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish

**Authors:** Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Nur Yağmur Tuncer, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42010v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42010v1)

**Summary:** This paper presents TurnTurk-GPT, a text-based turn-taking predictor for Turkish obtained by fine-tuning a Turkish GPT-2 model with the TurnGPT objective on synthetic and real dialogue, and evaluates it on real Turkish conversation against rule baselines, a zero-shot Turkish language model and a widely used multilingual end-of-turn detector. Evaluation uses word-level decision points on unpunctuated, lower-cased text approximating the output of streaming speech recognisers, recording-disjoint an...

---

### 11. Less Loss, Fixed Weights: Logit Corrections for Forgetting

**Authors:** Hanyu Yang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42000v1)

**Summary:** When a language model is fine-tuned to follow instructions, or further pretrained on a new subject, it often gets worse at predicting standard web text. This is known as "forgetting." We ask whether this loss can be undone by simple, fixed adjustments to the model's final token predictions. Across 14 pairs of base and derived models, from 1B to 7B parameters, we fitted a fixed bonus or penalty for each token (a vocabulary bias), alone or together with a temperature. On text held out from correct...

---

### 12. DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention

**Authors:** Zhangchi Feng, Harry Jiang, Yangyifei Luo, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41994v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41994v1)

**Summary:** Linear attention scales linearly with sequence length, but its finite-state memory can limit long-context retrieval. In gated linear recurrences, memory retention depends on state decay, which is shaped jointly by gate parameters A_log and dt_bias and by input activations. In controlled Gated DeltaNet (GDN) experiments, both parameters remain highly correlated with their initial values after training, highlighting the importance of initialization. Therefore, we introduce Dual-Axis Memory Initial...

---

### 13. Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions

**Authors:** Ning E, Changde Du, Yizhuo Lu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41951v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41951v1)

**Summary:** Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with the multidimensional mental representations underlying human similarity judgements. We build on a previously established behavior-derived semantic embedding space, in which objects ar...

---

### 14. Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents

**Authors:** Shuyang Zhang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41905v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41905v1)

**Summary:** An agent that must call several tools to fulfill a request fails when the tool retriever omits any one of them, yet tool retrievers are mostly built and evaluated on queries requiring a single tool. We compare representatives of six retrieval structures (flat lexical and dense retrieval, LLM query decomposition, LLM-navigated hierarchies, server-then-tool matching, dependency graphs, and trained set-level retrievers) across two multi-tool testbeds: 345 AppWorld queries with expert dependency lab...

---

### 15. How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces

**Authors:** Donghang Duan, Qingyu Liu, Yifei Liu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41885v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41885v1)

**Summary:** Large language model (LLM)-based agents interact with external tools through protocols such as the Model Context Protocol (MCP), producing tool-call traces that may expose behavioral signals about users. In this work, we systematically study the risk of user-profile inference from MCP tool-call traces, where observers infer user attributes from protocol-valid tool interactions without access to user conversations. We introduce PrivacyTrace, a benchmark containing 1,000 synthetic user profiles an...

---

### 16. Text as an Index for Zero-Shot Cross-Domain Knowledge Tracing

**Authors:** Yin Yi, Haiping Ma, Siyu Song, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41883v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41883v1)

**Summary:** Knowledge tracing (KT) predicts a student's next response from their history. New platforms often have question texts but no response logs for training, motivating zero-shot cross-domain KT. Existing transfer and cold-start methods use question semantics, but cross-platform semantic discrepancies limit transferability. We propose TIZSKT, which separates behavioral sequence modeling from domain-local historical evidence construction and uses text as an index rather than a directly transferable pr...

---

### 17. SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding in Conversational XAI

**Authors:** Van Bach Nguyen, Qianli Wang, Nils Feldhus, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41856v1)

**Summary:** Conversational explainable AI (ConvXAI) agents often use GUS-style architectures with separate modules for intent recognition, dialogue management, and template-based response generation. While faithful to the underlying XAI methods, these pipelines are hard to adapt and often struggle with context-dependent follow-up questions. We present SimXAI, a lightweight LLM-centric conversational layer that replaces these modules with a single tool-calling LLM that bridges access to existing XAI resource...

---

### 18. Iterated Integrals as Lexical Fingerprints: Path Signature Embeddings for Lexical Similarity

**Authors:** Raj Shekhar Singh, Pratham Agarwal

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41855v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41855v1)

**Summary:** While sentence embeddings are primarily designed for semantic generalization, their latent geometry implicitly encodes surface-level lexical properties, a relationship that remains poorly understood. Shallow pooling methods discard word order, while deep Transformer models obscure these lexical alignments behind computational complexity and uninterpretable spaces. We propose constructing sentence embeddings via the path signature of Word2Vec trajectories, leveraging the iterated integrals of rou...

---

### 19. Peeling the Matryoshka: Extracting Ontological Structure from Retrieval Embeddings

**Authors:** Eunchan Kim, Inwhee Joe

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41785v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41785v1)

**Summary:** Taxonomy construction is essential for knowledge-intensive NLP yet remains costly: clustering-based methods (i) need careful per-corpus tuning and yield unstable hierarchies, while LLM-based pipelines (ii) depend on expensive task-specific training that does not transfer across domains. We report an empirical finding that bears on both: in Matryoshka Representation Learning (MRL) embeddings, where each leading prefix is itself a usable, coarser vector, prefix length aligns with the coarse-to-fin...

---

### 20. Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought

**Authors:** Dicong Yu, Wenhua Wang, Tian Wang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41769v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41769v1)

**Summary:** Reasoning distillation is widely used to transfer the reasoning capabilities of large language models to smaller students through teacher-generated supervision. In the black-box setting, however, teachers may expose only final answers and brief solutions, leaving intermediate calculations and validity conditions unavailable and thus limiting the reasoning supervision available for distillation. We propose Stepwise Querying, which elicits step-specific explanations without requiring access to the...

---

### 21. Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable Components

**Authors:** Yukiya Horiba, Hakaze Cho, Takahiro Yakoh

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41743v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41743v1)

**Summary:** Task Vectors (TVs) provide a compact way to steer large language models, but they are typically treated as atomized directions merely extracted from hidden states, leaving their internal functional structure poorly understood. Motivated by prior work that decomposes in-context learning into Task Recognition (TR) and Task Learning (TL), we ask whether a single TV can likewise be decomposed into functionally meaningful components. We formulate a TR/TL-based decomposition from candidate-label unemb...

---

### 22. Leakage-Controlled Structure-Preserving Augmentation and Template-Aware Evaluation for Bangla Symptom-Based Disease Prediction

**Authors:** Sabah Nushra, Shovan Samanta Turzo, Moinul Hossain, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41733v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41733v1)

**Summary:** Bangla symptom-based disease prediction is commonly evaluated on a small, imbalanced structured benchmark containing many profiles that differ by only one or two symptoms. We test whether train-only asymmetric Bernoulli perturbation improves classification using 725 unique profiles spanning 85 diseases and 172 binary symptoms. Experiments use ten repeated real-profile holdouts and parent-grouped inner cross-validation. The 2 x 2 design separates augmentation from hyperparameter tuning, with exac...

---

### 23. From Training Exposure to Membership Evidence: A Controlled Study of OLMo 2

**Authors:** Ali Banaei, Muhammad Shahab Shahzad, Gerald Q. Maguire, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41732v1)

**Summary:** Whether a language model was trained on a document matters for copyright, privacy, and benchmark contamination. Yet most membership-inference (MI) evaluations on language models collect members and non-members after the fact, so success may reflect distribution shift and failure is inconclusive. We re-ran OLMo 2 1B's official 50-billion-token mid-training stage, replacing selected training chunks with documents from 7,814 pairs matched on domain and difficulty. For each pair, a coin flip determi...

---

### 24. UpLoop: Training Looped Transformers via Upcycling at No Extra Pretraining Compute

**Authors:** Cheng Liang, Tengfei Zhang, Ya Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41720v1)

**Summary:** Looped language models can strengthen reasoning through repeated computation with shared weights, increasing execution depth without adding independent parameters. However, each additional pass increases training floating-point operations (FLOPs), making these gains more expensive to obtain. To address this cost, we propose UpLoop, a pretraining schedule that uses upcycling to train looped Transformers while exactly matching a standard dense baseline in final parameter count, total training toke...

---

### 25. GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs

**Authors:** Minh-Nam Tran, Abulhair Saparov

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41704v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41704v1)

**Summary:** The needle-in-a-haystack (NIAH) benchmark was introduced as a test for measuring a model's ability to find small relevant facts within a very large body of input text. However, existing NIAH benchmarks each suffer from one or more of the following limitations: (1) reliance on synthetic data, so their evaluations may not generalize to real-world settings; (2) reuse of previously published datasets, leading to the risk of benchmark contamination; (3) dependence on manual annotation, which requires...

---

### 26. Precision--Recall Trade-off on the Inference Level for LLMs in Grammatical Error Correction

**Authors:** Ryszard Staruch, Filip Graliński

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41698v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41698v1)

**Summary:** Large language models (LLMs) have recently been adopted for Grammatical Error Correction (GEC), achieving strong performance via both full fine-tuning and prompt-based approaches. As probabilistic sequence models, LLMs expose inference-time parameters that directly modify token generation behavior; however, their potential for controlling GEC-specific trade-offs has not been systematically studied. In this work, we investigate decoding strategies for grammatical error correction. We show that th...

---

### 27. TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents

**Authors:** Rui Yu, Chong Mu, Jinchuan Zhang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41697v1)

**Summary:** Training interactive language agents from terminal outcomes poses three coupled problems: which task and state continuations to sample, how to assign delayed feedback to decisions, and how to aggregate token losses for multi-token actions. We present TSBPO, a tree-structured sampling-to-update paradigm that addresses these problems within one training loop. A likelihood-fitted Root/Branch allocator uses retained task and state evidence to target continuations likely to produce contrasting termin...

---

### 28. Does Reasoning Make Language Models Agree?

**Authors:** Mila Gorecki, Moritz Hardt

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41691v1)

**Summary:** Language models face two opposing concerns: monoculture, in which models err in correlated ways, and multiplicity, in which equally accurate models make conflicting decisions. The rise of reasoning models has complicated this debate: On the one hand, reasoning may increase model agreement if models anchor on the same salient features or follow similar reasoning paths. On the other hand, stochastic reasoning traces may introduce additional branch points leading to more diverse predictions. We res...

---

### 29. When Steering Shifts Discourse: Identifying and Intervening on Discourse-Level Changes due to Activation Steering in LLMs

**Authors:** Shivam Adarsh, Hetianyu Huang, Lau Safin, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41661v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41661v1)

**Summary:** Activation steering is an inference-time technique used to control or modify the behavior, tone, or safety properties of a large language model (LLM) without retraining the model's weights or editing its input prompt, but simply by adding a vector to its residual-stream activations. However, activation steering also changes the generated text in unintended ways, unrelated to intended behavior change, that are not well understood. Prior work has measured these changes only through coarse signals ...

---

### 30. GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning

**Authors:** Chanseul Cho, Noori Bae, Dongheon Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41629v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has recently been extended to vision-language models (VLMs), yet its effectiveness remains limited for text-rich reasoning tasks. We highlight a key factor contributing to this limitation: models frequently arrive at correct final answers despite misperceiving visual information during intermediate steps. We define this phenomenon as Correct-but-Visually-Misgrounded Reasoning (CVMR). Because standard RLVR rewards only final-answer correctness...

---

### 31. Saidzoda-Tajik-LFM-2.6B: Adapting a 2.6B Hybrid Model to Tajik Tool Calling, and What Continued Pretraining Takes Away

**Authors:** Tohir Saidzoda, Nekruz Maxudov, Bedil Karimov, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41576v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41576v1)

**Summary:** We release Saidzoda-Tajik-LFM-2.6B, a Tajik adaptation of the 2.6B-parameter hybrid model LFM2.5-2.6B-Base, built for tool calling in Tajik on modest hardware. The recipe has two stages: LoRA continued pretraining (CPT) on 1,485,319 cleaned Tajik web documents for 3 epochs, then one epoch of supervised fine-tuning (SFT) on a mix of machine-translated Tajik tool calls, English tool calls kept as replay, and Tajik instructions. On a 174-item tool-calling test set built from BFCL v3 and machine-tra...

---

### 32. BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion

**Authors:** Ruurd J. A. Kuiper, Robert A. Bagheri

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41574v1)

**Summary:** Unlike autoregressive (AR) models, diffusion language models (DLMs) permit parallel token updates, flexible generation, and bidirectional attention, but leading systems rely on costly pretraining or full-model fine-tuning. We present Build Your Own DLM (BYOD), a generalizable LoRA-only recipe for parameter-efficient AR-to-DLM conversion. Without architecture-specific tuning, BYOD induces diffusion generation in Gemma 2 9B, Llama 3.1 8B, Qwen2.5 7B, and Ministral 8B; to our knowledge, this is the...

---

### 33. SCRBench: Beyond Equivalence Checking for Semantic Change Reasoning in Code

**Authors:** Omid Saghatchian, Ali Mahzoun, Khashayar Etemadi, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41562v1)

**Summary:** Understanding how code changes affect program semantics is a core aspect of code reasoning in language models. It is commonly evaluated by asking whether two programs are semantically equivalent, but a yes/no answer does not reveal whether a model knows which code change caused a semantic difference, or which sequence of code changes produced the modified program. We study two tasks that ask these questions directly, diagnosing semantic change and reconstructing sequences of code changes, alongs...

---

### 34. Digital sovereignty in professional translation workflows: a case study of migrating from Windows to Linux

**Authors:** Michael Farrell

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41561v1)

**Summary:** This study examines digital sovereignty in professional translation through a screening of computer-assisted translation tools and translation management systems, and a case study of migrating a translator's workstation from Windows to Linux. The framework combines three principles - Control, Continuity and Exit - with three practical requirements: native Linux operation, independence from mandatory external services, and independent access to essential data and resources. Drawing on documentary...

---

### 35. CEFR Level Assessment across Languages and Text Granularities

**Authors:** Eugene Matsumura, Yuki Arase

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41553v1)

**Summary:** Automatic assessment of textual CEFR levels is an important task in educational natural language processing. However, accurate CEFR level prediction remains challenging due to the naturally imbalanced distribution of CEFR levels and the ambiguous boundaries between adjacent levels. To address these challenges, we propose a unified training objective that combines focal loss with supervised contrastive learning. Focal loss mitigates class imbalance by emphasizing underrepresented and difficult ex...

---

### 36. Enhancing Knowledge Entity Relation Extraction in Abstracts and Full-text Content of Academic Articles Using Large Language Models

**Authors:** Yingyi Zhang, Chengzhi Zhang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41552v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41552v1)

**Summary:** This study investigates the effectiveness of large pre-trained language models (LLMs) for knowledge entity relation extraction (KERE) from academic papers. Existing studies have examined individual types of LLM-based strategies and evaluated model performance using metrics such as precision and recall. To provide a broader evaluation, this study investigates multiple strategies, including closed-source LLM-based CoT prompting, LoRA-adapted open-source LLMs, LLM-enhanced small pre-trained languag...

---

### 37. DAPS: Dependency-Aware Premise Selection for LLM Theorem Proving

**Authors:** Zixuan Chen, Wenyuan Jiang, Junling Wang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41536v1)

**Summary:** LLM-based theorem proving in Lean 4 has advanced rapidly, but provers are difficult to leverage newly contributed lemmas, because retrieval skews toward popular foundational lemmas, leaving the right premises buried among hundreds of thousands of candidates. Existing neural selectors rank candidates by semantic similarity, with three intrinsic limitations: frequency-skewed retrieval, isolated pairwise ranking, and degradation on out-of-distribution queries such as competition problems and inform...

---

### 38. Enhancing Sentiment Classification on Small Datasets through Data Augmentation and Transfer Learning

**Authors:** Mahmoud S. Mayaleh, Samer A. Mayaleh

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41518v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41518v1)

**Summary:** Small-scale sentiment classification often suffers from data scarcity, which limits the generalization ability of the models. This study evaluates and compares the effectiveness of three data augmentation strategies: Easy Data Augmentation (EDA), back-translation, and contextual token substitution (nlpaug-style), with both traditional machine learning classifiers (Logistic Regression, Random Forest) and transformer-based models (BERT). We perform a comprehensive empirical comparison with low-res...

---

### 39. Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation

**Authors:** Alexandros Christoforos, Chadbourne Davis, Paul Raj

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41487v1)

**Summary:** Long-context diffusion repeatedly pays for both token interaction and feed-forward computation. We formulate these costs as two separate budgets: the edges available to an attention graph and the experts activated for each token. This view connects local, dilated, and global attention with conditional expert computation without assuming that sparsity alone preserves document-level information. We specify normalized masked attention, distinguish denoising depth from sampling iterations, and deriv...

---

### 40. KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents

**Authors:** Jinkyeong Choi, Chaebin Jeong, Junsung Jeon, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41482v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41482v1)

**Summary:** Recursive textual memory can carry earlier errors into later updates, yet task performance alone does not establish memory reliability. We define self-consistency bias as the persistence of incorrect claims already present in the incoming memory. We present KEEPER, a comparative analysis of four auxiliary objectives along information-content and update-sensitivity axes within a shared recursive interface, examining how supervision targets relate to agent performance. Among evaluated conditions, ...

---

### 41. KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise

**Authors:** Jonas Loos, Oliver Eberle

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41480v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41480v1)

**Summary:** Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated? To better understand this, we evaluate whether the change in model behavior arises only during the generation of the answer tokens where the change manifests, or whether altered processing of previous tokens causes it via the attention mechanism. For this, we patch the KV cache from a LoRA fine-tuned model into the unmodified base model, and vice versa. Our results show that for some behavio...

---

### 42. A prospective randomized study of patient-centered AI for clinical visit preparation

**Authors:** Xincheng Tan, Matthew Thompson, Xiang Ji, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41437v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41437v1)

**Summary:** Patients often arrive at brief, time-constrained clinical visits unsure of what to expect or ask, and millions of adults now turn to general-purpose AI chatbots to prepare beforehand. Yet whether conversational AI improves visit readiness remains unclear. We designed a large language model (LLM)-based visit preparation agent to guide patients before an appointment by gathering clinical context, setting visit expectations, providing relevant health information, building a prioritized list of ques...

---

### 43. BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed?

**Authors:** Anirudh Phukan, Tanya Goyal, Danish Pruthi

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41435v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41435v1)

**Summary:** Given that AI agents can search the web broadly and deeply in real time, it is tempting to conclude that their outputs account for recent world events. We show that this conclusion does not hold in practice. While agents can search and easily find recent changes, the correctness of their responses depends on whether they search and what they search for. Popular agentic search benchmarks like BrowseComp cannot expose failures wherein agents do not recognize their own assumptions that should be ve...

---

### 44. Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents

**Authors:** Haoqing Wang, Xiaoyi Zhang, Sicheng Fan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41432v1)

**Summary:** Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and-keyboard actions can impose a human-interaction prior, requiring repeated screen interpretation while leaving the computer's semantic and programmatic capabilities underexposed. We argue for exposing these capabilities and letting models choose and combine them. We introduce Hybrid Computer Use (HCU), a unified interfa...

---

### 45. SparseGDN: Chunk Sparse in Linear Attention

**Authors:** Jiedong Zhuang, Peng Zhao, Jialin Tang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41420v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41420v1)

**Summary:** Gated Delta Networks (GDNs) offer linear-time sequence modeling, yet long-context prefill remains costly due to dense intra-chunk computation, recurrent-state updates, and intermediate state storage. We introduce SparseGDN, a hardware-aware framework that combines structured intra-chunk approximation with input-dependent recurrent-event selection while producing outputs for every token. A block-adjacent solver reduces local Delta-solve computation, while a dynamic selector allocates recurrent-up...

---

### 46. ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science

**Authors:** Wenliang Liang, Zhiyuan Ning, Haolin Chen, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41396v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41396v1)

**Summary:** In AI for Science scenarios, experimental design and method reproduction require retrieving protocols that satisfy multiple interdependent constraints, yet existing benchmarks lack systematic evaluation of this capability. To address this gap, we introduce ProSearch, a benchmark for multi-constraint protocol retrieval in experimental science. ProSearch has three key features: (1) realism, with queries grounded in real experimental records and expert-defined templates; (2) complexity, with 60 exp...

---

### 47. Comparative Evaluation of LLM-Based Review Paradigms for Academic Paper Quality Assessment

**Authors:** Fan Huang, Hongyu Zhou

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41391v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41391v1)

**Summary:** Growing submission volumes have renewed interest in using large language models (LLMs) to support peer review. It remains unclear how such evaluation should be structured, how much the model matters, and whether LLM scores predict research impact. We evaluate five paradigms across three input representations and three LLMs on 232 stratified ICLR 2025 submissions. Direct absolute rating matches comparative ranking on rank correlation with human scores, yet compresses most predictions above the ac...

---

### 48. What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning

**Authors:** Ezza Ali, Sehrish Bibi, Momina Moetesum, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41366v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41366v1)

**Summary:** Training-free expert pruning makes two decisions: which experts to remove, and what the layer computes when its router still selects a removed expert. Published methods change both at once. Holding the mask fixed, we compare replacement operators from three families on OLMoE, DeepSeek-V2-Lite and Moonlight, with Granite as a fourth router, using paired, multiplicity-corrected tests. The largest effect is a choice usually left implicit: the survivors' gate scale. On routers trained without top-k ...

---

### 49. SERIAL-7: Deriving, Realizing, and Preserving Machine-Verifiable Outputs Across Representations

**Authors:** Youngkyung Seo, MiHyeon Kim, Jisoo Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41308v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41308v1)

**Summary:** Large language models increasingly generate structured outputs consumed by programs and downstream systems, where semantic correctness alone does not guarantee reliable execution. We introduce SERIAL-7, a Korean-English benchmark built around an executable verification framework for machine-verifiable generation across seven representations. Using 177 validated canonical artifacts, SERIAL-7 separates semantic derivation (Derive), constrained artifact generation (Realize), and cross-representatio...

---

### 50. From Transcription to Reformulation: Defining and Benchmarking Grounded Generative Speech Recognition

**Authors:** Qing Wang, Qihan Hu, Hang Lv, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41292v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41292v1)

**Summary:** Speech language models have expanded automatic speech recognition (ASR) from transcription to general speech-to-text generation. Yet existing benchmarks still assume a single ground-truth transcript per utterance, an assumption that struggles when models produce readable, formatted, or structured outputs. In this work, we introduce Grounded Generative Speech Recognition (GSR), reformulating speech recognition as generating semantically grounded text instead of a single transcript. We define a gr...

---

## cs.CV

**50 papers**

### 1. GazeRIB: Systematic Evaluation of Multi-Reader Gaze-Guided Chest X-ray Learning

**Authors:** Nattakorn Kittisut, Roy M. Gabriel, Marly van Assen, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42152v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42152v1)

**Summary:** Radiologists' visual attention can supervise medical image learning, but how reader panel composition affects its value remains untested. We evaluated GazeRIB (Gaze-guided Radiologist-Informed Blackout), which masks unviewed regions during training and uses unmasked images at inference. Eight experts repeatedly read the same 80 chest X-rays (CXRs). We compared individual readers with three-, five- and eight-reader panels across seven architectures and 10 seeds, evaluating 910 models on a separat...

---

### 2. Latent Reasoning in Continuous Space for Unified Multimodal Models

**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42149v1)

**Summary:** Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space,...

---

### 3. SemEllipsoid: Semantic-aware Shape Abstraction with Ellipsoid

**Authors:** Kuankuan Cheng, Haocheng Yuan, Changjian Li

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42145v1)

**Summary:** Representing 3D shapes using a set of primitives - known as shape abstraction - is an actively studied problem in computer graphics with wide applications in shape understanding, analysis, and simulation due to the compactness and computational efficiency of the primitive-based representation. Prior work has primarily focused on geometry-aware shape abstraction, where the objective is to approximate the input shape with a minimal set of primitives while preserving geometric fidelity. However, th...

---

### 4. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

**Authors:** Shengguang Wu, Suning Huang, Cherie Ho, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42141v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42141v1)

**Summary:** Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises ...

---

### 5. ReLift: Dense 3D Tracking as Lifted Trajectory Repair

**Authors:** Assaf Singer, Maroun Khriesh, Noam Rotstein, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42136v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42136v1)

**Summary:** Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision. We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded segments simply interpolated, already rival dedicated 3D trackers using the same ge...

---

### 6. A Better Critic Matters for Distribution Matching Distillation

**Authors:** Zongze Wu, Xianbang Wang, Zhengyang Geng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42135v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42135v1)

**Summary:** Distribution Matching Distillation (DMD) trains a few-step student using the difference between a teacher's score and an online critic's estimate of the student distribution's score. We investigate what the critic needs, in capacity and in information, to provide a reliable training signal. On the capacity side, controlled experiments across seven SiT model sizes on ImageNet show that increasing teacher size while keeping a small critic fixed can degrade student quality and cause training collap...

---

### 7. Rethinking Asymmetry in Self-Supervised 3D Geometry Learning

**Authors:** Gyeongjin Kang, Freeman Cheng, Botao Ye, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42092v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42092v1)

**Summary:** Self-supervised learning relies on asymmetry between what a model observes and what it must explain. Recent methods learn 3D geometry from unposed images by predicting cameras and scene structure, then rendering held-out views. To avoid trivial solutions, they impose this asymmetry in the input space, restricting how views interact through separate branches or masked attention. We revisit this design with geometric accuracy, rather than rendering quality, as the main objective. When a held-out v...

---

### 8. Think in 360°: Benchmarking and Bootstrapping Panoramic Video Reasoning

**Authors:** Lidong Lu, Lidong Zou, Xinyi Mao, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42082v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42082v1)

**Summary:** A panoramic video captures all directions around the camera, but relevant evidence can appear in different directions and at different times. Understanding it requires models to connect observations across the viewing sphere and time. We introduce PanoVideoBench, the first manually annotated benchmark for comprehensive panoramic video understanding. Its 1,000 questions span five categories and 15 question types, with diagnostic annotations for target search and panoramic capabilities. Evaluation...

---

### 9. REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

**Authors:** Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42053v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42053v1)

**Summary:** Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative brain (foundation models) with a reactive cerebellum (fast policies) seems natural for embodied systems, two obstacles remain: methods are built and scored on incompatible stacks, and their asynchron...

---

### 10. Learning Clean Generative Processes from Noisy Measurements

**Authors:** Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42036v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42036v1)

**Summary:** We study how to learn a generative model of clean images using only noisy observations. Diffusion processes and their generalizations to non-Gaussian noise require posterior predictions at every noise level. We first show that it is possible to learn these predictions from independent noisy views using Noise2Noise regression, but only at or above the noise level of the training data. To learn the predictions below that level, needed to generate clean images, we impose consistency: a prediction s...

---

### 11. Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation

**Authors:** Jiahua Xu, Yijie Fang, Nannan Wang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42031v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42031v1)

**Summary:** Autoregressive video generation enables efficient inference through streaming prediction. However, existing methods are typically restricted to fixed sampling steps, limiting the flexibility to balance generation quality and efficiency, while one-step generation suffers from degraded visual quality and error accumulation over long sequences, leading to content drift and generation collapse. To address these issues, we propose Any Forcing, a unified framework for achieving Any-Step Generality and...

---

### 12. GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation

**Authors:** Yuqi Li, Junming Liu, Bowen Hu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42002v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42002v1)

**Summary:** Video generation models synthesize realistic motion, but can they respond correctly to changes in initial geometry? We introduce GeoFlip, a video generation benchmark centered on physical outcome flips induced by geometry. With shared physical settings and textual prompts held fixed, GeoFlip applies controlled interventions to support extent, object placement, and mechanism configuration, constructing paired scenes with contrasting reference events, such as remaining stable versus falling or tip...

---

### 13. MoETok: Sparse Expert Routing for 1D Visual Tokenizers

**Authors:** Jiahao Guo, Bao Tang, Haoxiang Cao, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41992v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41992v1)

**Summary:** Modern visual tokenizers aim to preserve fine-grained visual details while learning high-level semantic representations for downstream generation and understanding. Query-based 1D visual tokenizers encode images into flexible latent sequences, yet how individual learnable queries gather and encode image information remains poorly understood. We reveal that these queries spontaneously develop complementary roles under semantic supervision: a small set of Content queries captures high-level semant...

---

### 14. FoAViS: Analyzing Learned Fixation Strategies in a Foveated Active Vision System

**Authors:** Valentin Hassler, Jonathan Henrich, Yohaï-Eliel Berreby, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41987v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41987v1)

**Summary:** Human vision is foveated and active: resolution is highest at the fovea and falls off towards the periphery, and fixations are actively directed to locations of interest. Building a machine system that processes information in the same way lets us study gaze behavior in a controlled setting where the system's components and objectives are known. The emergence of gaze characteristics can therefore be examined systematically, which may in turn inform our understanding of biological vision. This re...

---

### 15. TwinPast: Benchmarking Historical Evidence Use in Streaming Video Understanding with Evidence Contrastive Video Pairs

**Authors:** Haotian Yang, Yong Chen, Cheng Peng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41983v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41983v1)

**Summary:** High accuracy on streaming video benchmarks does not establish whether a model uses visual history. Our review of OVO-Bench and StreamingBench finds that recent frames suffice for 32% of sampled historical questions, while models also answer many questions correctly from the question and options alone. We introduce TwinPast to test whether answers correctly follow changes in history, using 350 human-reviewed video pairs spanning five historical tasks. Each pair holds the recent video context, qu...

---

### 16. IGDA-ICMH: an Importance Guided Feature and Network Dual Adaptation Framework towards Image Compression for Machine and Human Vision

**Authors:** Yanbo Gao, Xinyu Zhao, Shuai Li, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41924v1)

**Summary:** With the surge of machine vision applications, image compression for both machine and human vision (ICMH) has become an important research area. Existing studies mainly focus on task-specific adaptation or multi-task joint optimization, yet they often overlook the unequal contributions of different features and network layers to downstream machine vision tasks. To address this issue, we first quantitatively investigate the impact of different feature and network layers on machine vision performa...

---

### 17. Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos

**Authors:** Wendong Bu, Tinghong Ye, Qizhou Wang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41877v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41877v1)

**Summary:** Scaling humanoid motion foundation models is constrained by the scarcity of diverse, robot-executable data and by the difficulty of jointly learning from heterogeneous multimodal inputs while supporting real-time closed-loop control. We present Movens-5M, constructed from raw Internet videos through clip generation, quality filtering, semantic annotation, motion recovery, and physical refinement with humanoid retargeting and execution verification. It contains 15 million human-motion sequences a...

---

### 18. Open-Weight MLLMs Cannot Compare What They Cannot Name

**Authors:** Wenxin Su, Anna Kreshuk

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41841v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41841v1)

**Summary:** Multimodal Large Language Models (MLLMs) are increasingly capable of understanding images and performing complex visual reasoning, suggesting the possibility of using them to automate biological image analysis. This need is becoming increasingly urgent as advances in technology continue to generate ever larger and more diverse microscopy datasets, already exceeding the scale at which manual visual analysis is feasible. With the final aim to use MLLMs for visual comparison of complex phenotypes, ...

---

### 19. ReuScope: Auditing Data Reuse and Evaluation Sensitivity in Capsule Vision 2024

**Authors:** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41835v1)

**Summary:** We develop ReuScope, a protocol for auditing data reuse and evaluation sensitivity, using Capsule Vision 2024 as a case study. It combines measurements of data relationships with two comparisons: changing the evaluation population while holding predictions fixed, and changing training data while holding evaluation fixed. Byte-identical files cross the public training-validation boundary, and all 41 Kvasir-Capsule recordings that contribute frames occur in both partitions. Shared source recording...

---

### 20. ObjectGuidedMap: An Object-Aware Model for Robust Bird's Eye View Map Prediction in High-Occlusion Scenarios

**Authors:** Christian Bohn, Harsh Yadav, Klaus Friedrichs, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41834v1)

**Summary:** Accurate BEV map prediction is a critical component of autonomous driving systems, enabling downstream planning and control. Recent approaches such as Mask2Map achieve strong performance by predicting vectorized, instance-level map elements directly from multi-view images. However, existing BEV map prediction models operate largely independently of object-level scene understanding, despite the fact that traffic participants frequently occlude or implicitly encode information about road geometry....

---

### 21. PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization

**Authors:** Hanqiao Ye, Yuzhou Liu, Mengqi Rong, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41833v1)

**Summary:** Camera localization methods are mostly multi-stage pipelines relying on dedicated and complex maps that are costly to construct, store, and maintain over time. Alternatively, well-structured maps that organize scenes with compact yet expressive primitives are often readily available, providing rich structural and semantic cues that humans can interpret. However, their potential for direct camera localization remains largely unexplored due to the significant modality gap between map primitives an...

---

### 22. A Patch is More Than a Token

**Authors:** Zixiong Wang, Haiping Ma

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41814v1)

**Summary:** Vision Transformers represent each image patch through a canonical token produced under one observation condition. That token is a powerful interface, but it is still one realized state of the patch. We introduce PMTT, which establishes two foundations: a patch representation object can extend from one canonical state to a canonical-centered Representation State Family, and identity-preserving variation opens Patch-Level Local Feature Space. We develop four parts of this representation program. ...

---

### 23. Different Models, Shared Failures: Auditing Frozen-Encoder Pools for Medical Segmentation

**Authors:** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41790v1)

**Summary:** Average segmentation accuracy and model count do not reveal whether models fail on the same cases. We present CoFailMed, an audit of correlated failures in pretrained-encoder pools for medical segmentation. Across five 2D tasks, we evaluate 11 public pretrained encoders (a controlled sample, not a census) using frozen features and separately trained $1\times 1$ readouts with four seeds per encoder. Shared-checkpoint pairs have the highest mean per-case Dice correlation. An expanded 17-encoder an...

---

### 24. Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition

**Authors:** Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41789v1)

**Summary:** Multi-head attention in Vision Transformers (ViTs) allows independent attention patterns across heads, but without explicit regularization, heads may learn redundant patterns rather than complementary roles. Correlation-based penalties encourage head disentanglement, yet apply uniform regularization across all training samples. In face recognition (FR), hard samples whose embeddings lie close to competing identities are critical for optimization and generalization. Motivated by this, we propose ...

---

### 25. WorkIng: A Real-World and Synthetic Highway Work-Zone Benchmark Dataset for Autonomous Navigation

**Authors:** Xujun Xie, Dominik Rößle, Adithya Mohan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41772v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41772v1)

**Summary:** Highway work zones are critical edge cases for autonomous vehicles (AVs), combining atypical geometries and jurisdiction-specific regulations that existing benchmarks fail to capture: real-world datasets lack 360° multi-modal, full-scene 3D work zone annotation, and no single recorded site can span the layouts and regulatory variants needed for generalizable models. We present WorkIng, a dual-domain benchmark and training resource. WorkIng-Highway provides a 360° multi-modal work zone benchmark ...

---

### 26. Measuring What Matters: A Causal Reliance Score for Histopathology Image Segmentation

**Authors:** Samuel Thomas, Daniel Tweneboah Anyimadu, Ahmed Karam Eldaly, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41763v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41763v1)

**Summary:** Reliable histopathology segmentation requires models that rely on pathology-relevant structures rather than spurious background correlations. In this work, we argue that improving architectures alone is insufficient if models continue to rely on spurious correlations rather than pathology-relevant features. We introduce a causality-inspired evaluation framework based on controlled interventions that explicitly probes model sensitivity to foreground tissue structure and background/domain variatio...

---

### 27. SAR-TS-BERT: Physics-Guided Self-Supervised Pre-Training With Polarimetric Features for SAR Time-Series Crop Classification

**Authors:** Jieqiu Wang, Yuhan Zhang, Bo Zheng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41728v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41728v1)

**Summary:** Multitemporal synthetic aperture radar (SAR) imagery provides continuous, cloud-free observations of crop phenology for agricultural monitoring in cloudy and rainy regions, yet high-accuracy classification typically requires extensive labeled samples. Although self-supervised pre-training mitigates label dependency in remote sensing, existing frameworks primarily target optical imagery or generic spatial SAR scenes, underutilizing temporal backscatter dynamics and polarimetric scattering mechani...

---

### 28. Nereus: A Large-Scale Underwater Dataset for Fine-Grained Attribute Understanding and Grounded Counting Perception

**Authors:** Jingtao Deng, Zihao Jin, Yuehe Chen, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41705v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41705v1)

**Summary:** Underwater imagery records rich ecological information and supports applications such as science communication, fishery monitoring, ecological conservation, and oceanographic research. Beyond general scene understanding, these applications require models to recognize fine-grained biological traits and reason over spatially grounded evidence. However, existing underwater datasets often provide coarse category labels, generic captions, or total-count supervision, which limits their use for organis...

---

### 29. Retrieval-Augmented Initialization with Dual-Guided Inversion for Flow-Based Inverse Problem Solvers

**Authors:** Hansam Cho, Seoung Bum Kim

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41695v1)

**Summary:** Flow models have recently emerged as powerful generative priors for solving inverse problems. Despite their success, most existing flow-based inverse problem solvers initialize the reconstruction process with random Gaussian noise. However, recent studies in image generation have shown that the choice of initial noise can significantly influence generation outcomes. The role of initialization as a distinct design choice in flow-based inverse problem solving remains comparatively underexplored. I...

---

### 30. OT-CAL: Optimal-Transport-Guided Adaptive Sample Selection for Efficient Visual Learning

**Authors:** Suryansh Talukdar, Jin Soung Yoo

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41677v1)

**Summary:** Deep neural networks for image recognition are typically trained using mini-batches, with a forward pass to compute predictions and losses followed by a more computationally expensive backward pass to update model parameters. However, not all training samples contribute equally to learning, suggesting that computation can be reduced by performing backward passes only on informative samples. The challenge is that sample informativeness changes throughout training: difficult samples may be valuabl...

---

### 31. A Self-Supervised Pose Estimation Approach for Construction Machines

**Authors:** Alaa Alshubbak, Daniel Görges

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41673v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41673v1)

**Summary:** Pose estimation is a computer vision task used to estimate a skeleton of dynamic systems to predict future movements. Most of the research in this direction is based on a supervised learning approach which requires a massive amount of labeled datasets. In this paper, a self-supervised three-stage model based on a contrastive learning approach is introduced for estimating a skeleton of dynamic construction machines; such as excavators without using any labeled images for the first stage. The whol...

---

### 32. OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System

**Authors:** Seungwon Choi

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41671v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41671v1)

**Summary:** Visual-inertial odometry (VIO) is a fundamental topic in robotics research. Beyond research, VIO has been adopted in a wide range of products. In this manuscript, we present OpenVIO, an open-source VIO system for research and practical applications. It is released under the MIT license. OpenVIO supports pinhole and fisheye cameras and extends this support to stitched 360° images. We describe each part of the system together with its design considerations. We also report benchmark results with ot...

---

### 33. Enhancing Medical Lesion Segmentation via Several Simple Modules

**Authors:** Ruichen Li, Zhao Yao

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41652v1)

**Summary:** This work introduces three lightweight enhancement modules for medical lesion segmentation to improve clinical applicability, particularly under data-scarce and computationally constrained environments. Current mainstream methods struggle with the lack of high-quality annotations for rare pathologies, which often leads to severe morphological distortions during inference, despite achieving seemingly ideal DSC scores. Furthermore, the isolated development of individual segmentation tasks restrict...

---

### 34. When Depth Lies: Benchmarking Vision-Language Models on Mirror-Induced RGB-D Ambiguity

**Authors:** Hao Yin, Tianchen Guo, Heming Du, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41651v1)

**Summary:** Vision-language models (VLMs) have made significant progress in spatial reasoning, particularly by integrating RGB images with depth data, which is often assumed to faithfully reflect physical distances. However, mirrors violate this assumption: they distort depth readings while reproducing object appearances, making reflections difficult to distinguish from real objects. As existing benchmarks rarely consider such reflective scenarios, VLM performance in mirror scenes remains largely unexplored...

---

### 35. TADP: Dual-Branch Temporally Adaptive Differential Privacy for Expression-Aware Video Anonymization

**Authors:** Feng Xu, Xun Li, Lars Petersson, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41642v1)

**Summary:** We present TADP, a temporally adaptive differential privacy (DP) framework for inference-time privacy-preserving video generation under fixed-length clip-replacement adjacency. TADP uses a dual-branch design to extract identity and expression representations, clips and privatizes both branches with temporally adaptive Gaussian mechanisms whose noise scales depend only on preceding privatized releases within the same clip and are bounded below by history-uniform calibrated minima, and accounts fo...

---

### 36. GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning

**Authors:** Chanseul Cho, Noori Bae, Dongheon Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41629v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has recently been extended to vision-language models (VLMs), yet its effectiveness remains limited for text-rich reasoning tasks. We highlight a key factor contributing to this limitation: models frequently arrive at correct final answers despite misperceiving visual information during intermediate steps. We define this phenomenon as Correct-but-Visually-Misgrounded Reasoning (CVMR). Because standard RLVR rewards only final-answer correctness...

---

### 37. Attention Maps Know When to Think: Training-Free Difficulty-Aware Chain-of-Thought for Reasoning Segmentation

**Authors:** Chanseul Cho, Jaesung Jun, Dongheon Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41618v1)

**Summary:** Chain-of-Thought (CoT) prompting has become a standard reasoning strategy in Multi-modal Large Language Models (MLLMs), showing strong performance in complex vision-language tasks such as reasoning segmentation. However, our analysis reveals that indiscriminate CoT usage can lead to degraded performance by inducing unnecessary reasoning, a phenomenon we term overthinking. In reasoning segmentation, overthinking often leads to misalignment between the query's intent and visual grounding. To addre...

---

### 38. DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction

**Authors:** Fan Zhu, Zhisong Xu, Ziyu Chen, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41602v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41602v1)

**Summary:** RGB-D SLAM requires accurate online tracking, high-quality rendering, and geometrically consistent reconstruction. Existing Gaussian SLAM methods mainly optimize Gaussian primitives with photometric, depth, or local frame-to-model constraints, which are often insufficient in indoor scenes with weak textures, large planar structures, noisy depth, and long trajectories. The resulting maps may suffer from pose drift, surface thickness artifacts, noisy normals, and blurred structural boundaries. We ...

---

### 39. Scout-Refine-Correct: Teaching Flow Models to Refine Their Own Samples

**Authors:** Sergey Karpukhin, Aibek Alanov

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41598v1)

**Summary:** The quality of image generation models trained with diffusion or flow matching is largely fixed by the training budget: at inference, the only available lever is the number of sampling steps, and additional steps improve quality only up to a point. We present a training recipe, Scout-Refine-Correct (SRC), that instead gives a flow-matching generator a genuine inference-time refinement capability. At each sampling step the model takes a scout rollout -- $K$ steps ahead along its own trajectory --...

---

### 40. TopoHyperClinicalGraph: A Geometry and Topology-Aware Multimodal Framework for Cancer Survival Prediction

**Authors:** Noaman Khan, Zubair Shah

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41556v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41556v1)

**Summary:** We developed TopoHyperClinicalGraph, a multimodal framework combining hyperbolic tissue geometry, persistent topology and clinical graph learning for cancer survival prediction. Pre-extracted UNI2-h features are reduced from 1,536 to 1,024 dimensions using training-fold PCA. A pathology backbone combines hyperbolic neighborhoods with Lorentz-centroid attention pooling. Once frozen, its survival logits are adjusted using persistence descriptors from up to 64 landmarks per slide and sampling contr...

---

### 41. TACO: Trajectory-Aware Curvature Observation for Memorization Localization and Mitigation in Diffusion Models

**Authors:** Ruxi Gu, Zilei Wang, Wei Wang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41520v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41520v1)

**Summary:** Text-to-image diffusion models can reproduce memorized training content within localized image regions, making precise localization essential for targeted mitigation. However, curvature observations at a single denoising state can contain transient responses, while spatially uniform mitigation may disrupt prompt-relevant content. We present Trajectory-Aware Curvature Observation (TACO), a unified framework for local memorization detection and mitigation in diffusion models. Our empirical analysi...

---

### 42. Parameter-Efficient Fine-Tuning of Transformer Encoders for Audio-Image-Symbolic Music Retrieval

**Authors:** Eliseo Fuentes-Martinez, Antonio Hidalgo-Centeno, Jorge Calvo-Zaragoza, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41512v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41512v1)

**Summary:** Score-based multimodal music retrieval requires representations that are both discriminative within each modality and compatible across audio recordings, sheet music images, and symbolic scores. This paper investigates the effectiveness of parameter-efficient fine-tuning (PEFT) for adapting pretrained music encoders and examines whether modality-specific improvements translate into better multimodal representations. We compare full fine-tuning, LoRA, and QLoRA across nine pretrained audio, image...

---

### 43. VoxLution: Evolving Voxels for High-Fidelity 3D Scene Generation

**Authors:** Daoyi Gao, Xinyi Zhang, Alexey Bokhovkin, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41501v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41501v1)

**Summary:** High-resolution 3D indoor scene generation is crucial for immersive applications such as virtual reality, spatial computing, and robotics simulation. We introduce VoxLution, a coarse-to-fine transformer-based approach that generates high-fidelity indoor scenes with rich details, overcoming the overly smooth geometry typical of existing generative models. First, we generate a low-resolution spatial layout; then, based on this structural information, we progressively refine the scene geometry loca...

---

### 44. VariaFlow: Uncertainty-Aware Flow Matching for Unsupervised Anomaly Detection

**Authors:** Arnela Hadzic, Martin Urschler, Cosmin I. Bercea

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41494v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41494v1)

**Summary:** Reconstruction-based anomaly detection no longer fails at reconstruction. Generative models produce high-quality pseudo-healthy reconstructions, and the remaining difficulty is the step of scoring residuals. The residual between a scan and its reconstruction has two indistinguishable sources, genuine pathology and the anatomical variation that separates one healthy brain from another. Scoring against a single reconstruction treats both as anomalous, inflating false positives where healthy anatom...

---

### 45. BDNet: Fast-slow thinking is all you need

**Authors:** Chenzhi Zheng, Zhuoran Zheng

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41485v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41485v1)

**Summary:** We present BDNet, a hierarchical image-classification backbone built around fast image features and slow statistical references. Its baseline deformation operator (BDO) transforms the deviation of a feature from a stage-specific reference through a low-rank projection and a learned channel scale. Rather than computing pairwise token similarity, the branch operates directly on baseline-relative residuals with complexity linear in the token count. Each of four reference buffers accumulates detache...

---

### 46. Beyond Trial-and-Error: A Geospatial-Guided Active Reasoning Framework for Robust Aerial Vision-and-Language Navigation

**Authors:** Jiawei Ge, Wenkang Gong, Jiuxin Cao, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41446v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41446v1)

**Summary:** Aerial Vision-and-Language Navigation (VLN) requires UAVs to locate language-specified goals in large-scale urban environments, where objects often appear small and visually ambiguous from high-altitude viewpoints. Existing methods largely follow a reactive paradigm common in indoor VLN, repeatedly updating navigation states from local observations while underutilizing the geospatial structure that remains stable during navigation. As a result, visually similar distractors can cause a reactive g...

---

### 47. FlexReader: Towards Adaptive Decoding Paths for Efficient Arbitrary-Length Scene Text Recognition

**Authors:** Zhibin Ma, Pengwen Dai, Zhigang Yao, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41426v1)

**Summary:** Existing Scene Text Recognition (STR) models are inherently coupled with a specific decoding strategy by their training paradigms, limiting their flexibility in deployment across diverse recognition scenarios. In this paper, we propose FlexReader, an STR model that supports multiple decoding strides, enabling a single model to achieve an optimal accuracy-efficiency trade-off across different datasets. Specifically, we first introduce a Sub-string Perception module to perceive the target sub-stri...

---

### 48. SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models

**Authors:** Haesung Lee, Insu Han

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41408v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41408v1)

**Summary:** Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms. Weight quantization is a natural remedy, yet post-training quantization (PTQ) recipes inherited from large language models degrade when applied to VLAs at ultra-low precision. Existing low-bit PTQ methods often fail to explicitly account for the structure of downstream operations and allocate precision without considering its effect on t...

---

### 49. DUGO: Dual-Scale Gaussian Memory for Online Temporal Action Localization in Egocentric Procedural Videos

**Authors:** Mohammed Aman Bhuiyan, Md. Sazzad Hossain Adib, Samiul Basir Bhuiyan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41402v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41402v1)

**Summary:** Online Temporal Action Localization (OnTAL) aims to detect and localize action instances from untrimmed streaming videos in real time. Unlike offline approaches, OnTAL models have no access to future frames and cannot go back and refine earlier predictions, which makes the task considerably harder given the strict real-time constraints and narrow temporal window available. Most existing OnTAL methods lean on either brief anchor-based context or a single-scale memory of past frames, which limits ...

---

### 50. Parse Before You Execute: Efficient Spatial Reasoning with Executable Primitives

**Authors:** Xiwei Liu, Yulong Li, Xinling Zhuang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41389v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41389v1)

**Summary:** Spatial reasoning in Vision-Language Models (VLMs) has increasingly benefited from tool-integrated pipelines that ground computation in explicit geometry. However, existing systems often compile queries into relatively open-ended artifacts, such as code, task constraints, tool plans, or gathered evidence, leaving what must be resolved before execution under-specified. This can lead to unnecessary tool acquisition and iterative refinement, while still producing plausible reasoning traces from inc...

---

## cs.LG

**50 papers**

### 1. Latent Reasoning in Continuous Space for Unified Multimodal Models

**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42149v1)

**Summary:** Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space,...

---

### 2. Counting on Dummies: Privacy Amplification with Observable Counts and Truncated Batches

**Authors:** Vitaly Feldman, Audra McMillan, Kunal Talwar

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42139v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42139v1)

**Summary:** In many practical deployments of Differentially Private Stochastic Gradient Descent (DP-SGD), the server processes data in batches. Randomly sampling these batches allows for better privacy bounds via privacy amplification results. Most sampling schemes with provable privacy amplification, including Poisson sampling and random allocation, result in variable batch sizes. The privacy guarantee of these schemes requires that the batch sizes are not revealed. In distributed settings, the server perf...

---

### 3. A Better Critic Matters for Distribution Matching Distillation

**Authors:** Zongze Wu, Xianbang Wang, Zhengyang Geng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42135v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42135v1)

**Summary:** Distribution Matching Distillation (DMD) trains a few-step student using the difference between a teacher's score and an online critic's estimate of the student distribution's score. We investigate what the critic needs, in capacity and in information, to provide a reliable training signal. On the capacity side, controlled experiments across seven SiT model sizes on ImageNet show that increasing teacher size while keeping a small critic fixed can degrade student quality and cause training collap...

---

### 4. Instance-dependent sequential limits as an exact information ledger

**Authors:** Akshay Balsubramani

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42133v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42133v1)

**Summary:** Instance-dependent limits for bandit regret, sequential tests, best-arm identification and Markov decision processes are proved by one chain. It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations. Only the first step is an identity. This work writes the chain as an exact ledger. By the chain rule, data processing loses exactly a conditional d...

---

### 5. Physiological Trajectories and Observation Patterns in ICU Mortality Prediction: Transportability Under Changing Measurement Conditions

**Authors:** Benjamin T. Pike

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42126v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42126v1)

**Summary:** Objective: To distinguish the transferable predictive value of physiological trajectories from that of observation patterns in ICU mortality prediction, and to assess whether measurement timing affects performance independently of observation quantity.   Materials and Methods: In-hospital mortality was predicted at 48 hours using MIMIC-III, MIMIC-IV, and eICU. Nested representations progressively integrated latest-value snapshots (R1), longitudinal physiological summaries (R2), and measurement f...

---

### 6. Gradient Descent on Two ReLU Neurons: Global Landscape and Bifurcation Dynamics

**Authors:** Binghua Li, Mengzhe Li, Denny Wu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42118v1)

**Summary:** Understanding how gradient descent learns features remains a central challenge in neural network theory. We study this question in a minimal multi-index setting that already exhibits rich multi-phase gradient dynamics: a well-specified two-neuron ReLU teacher-student model under isotropic Gaussian inputs, trained by population gradient flow from small initialization. We show that the dynamics are organized by two directions: the "easy" bisector direction, which carries the leading signal, and th...

---

### 7. Fast Privacy Loss Accounting for Random Allocation via Multiscale FFT

**Authors:** Vitaly Feldman, Moshe Shenfeld

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42117v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42117v1)

**Summary:** In the random allocation sampling scheme each user's data is used in $k$ steps chosen randomly and uniformly from a sequence of $t$ steps. This scheme is known to improve on Poisson sampling in private optimization and in communication-efficient aggregation. The existing privacy loss distribution (PLD) accountant for this scheme runs in time quadratic in the inverse of the accuracy parameter $α$ (Feldman and Shenfeld, 2026). We give an algorithm, \emph{multiscale FFT}, that represents likelihood...

---

### 8. SATFRONT: Detecting Atmospheric Fronts with Satellite Data using Machine Learning

**Authors:** Ioannis Dravilas, Miruna Stoicescu, Roope Tervo, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42111v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42111v1)

**Summary:** Atmospheric fronts are associated with much of the high-impact weather in the mid-latitudes, yet their identification and classification remain largely manual and subjective. Existing deep learning approaches rely primarily on gridded reanalysis or forecast data, limiting their applicability to satellite observations available for time-critical applications. We introduce SATFRONT, a machine learning framework for detecting cold, warm, and occluded fronts over Europe from geostationary satellite ...

---

### 9. Regret-Optimal Wasserstein-Robust Linear Regression

**Authors:** Sloan Nietert, Daniel Kuhn

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42109v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42109v1)

**Summary:** Distributionally robust optimization (DRO) minimizes worst-case risk under distributional uncertainty, but its decisions can be suboptimal in terms of their excess risk, or regret. We study this gap for multivariate least-squares regression, assuming that the observed source law and unknown target law differ by an adversarial 2-Wasserstein perturbation of size $\varepsilon$. We first identify the asymptotic complexity of robust decision-making in the $\varepsilon \to 0$ limit, characterized by a...

---

### 10. Hard Constraint Projection in a Physics Informed Neural Network (Burgers)

**Authors:** Miranda J S Horne, Peter K Jimack, Amirul Khan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42106v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42106v1)

**Summary:** Physics informed machine learning provides a framework to study and simulate fluid dynamics, potentially at a fraction of the computational cost of traditional numerical methods, with the goal of improving the explainability, accuracy and robustness of purely data driven machine learning methods. In this work, we extend the hard constraint projection (HCP) method developed by Chen et al. [Journal of Computational Physics, 445, 110624, 2021] from a linear partial differential equation (PDE) to a ...

---

### 11. Hyperbolic Inverse Reinforcement Learning

**Authors:** Iulia Rusu, Anoop Praturu, Sergei Gepshtein, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42104v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42104v1)

**Summary:** Inverse reinforcement learning (IRL) seeks to infer the reward function underlying observed behavior, but its predictive accuracy and interpretability depend on how that reward is computed from the underlying features. While prior IRL reward functions have been implemented through a variety of techniques including linear weights, neural networks, or other function approximators, none make assumptions about the geometry of the underlying feature space. Inspired by geometric organization observed ...

---

### 12. Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments

**Authors:** Philipp Bordne, André Biedenkapp

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42100v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42100v1)

**Summary:** Deep reinforcement learning (RL) is a powerful framework for sequential decision-making. Despite many high-profile successes in recent years, deep RL is known to be brittle. An emerging line of research attributes this brittleness to a loss of plasticity in neural networks. However, plasticity loss has so far been understudied in stochastic environments. We study this interplay systematically, training SAC agents on three DeepMind Control tasks augmented with controlled levels of observation and...

---

### 13. Cost-Aware Stopping for Freeze-Thaw Bayesian Optimization: When Does One-Step Lookahead Suffice?

**Authors:** Long Vu, Jongseong Brad Choi, Binoy Ravindran, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42085v1)

**Summary:** Freeze-thaw Bayesian optimization (BO) evaluates candidates in resumable increments but usually stops at a budget or convergence test. We maximize a budget-free utility, the best observed score minus a cost per increment, with a one-step lookahead: advance the candidate with the largest expected improvement (EI) under a fixed surrogate, and stop once no EI exceeds the cost. This rule, EI stopping, never falls below stopping immediately in expected utility, yet it can stop too early. We construct...

---

### 14. Differentially Private Synthetic Data from Sliced Chebyshev Moments

**Authors:** Lucas Rosenblatt, R. Teal Witter, Christopher Musco

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42081v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42081v1)

**Summary:** Research on practical differentially private (DP) synthetic data has largely focused on methods that approximately preserve low-dimensional marginals of a target distribution, and can thus only hope to preserve higher-dimensional, global structure as a lucky by-product. At the same time, existing methods that target global accuracy guarantees pay a price exponential in the data dimension, $d$.   In this work, we address this ``curse of dimensionality'' by presenting a new DP synthetic data algor...

---

### 15. RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks

**Authors:** Xin Ming Li, Peng Hu

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42068v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42068v1)

**Summary:** Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its loca...

---

### 16. Exact Theory and Optimal Stepsizes for Stochastic Gradient Descent in Smooth Convex Minimization

**Authors:** Benjamin Grimmer, Qining Shen

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42048v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42048v1)

**Summary:** This work considers the design of stepsize schedules for stochastic gradient descent in smooth convex optimization. Throughout, we assume that gradient noise is conditionally zero-mean with bounded variance. Among problems with dimension $d\geq N+1$, we provide an exact worst-case analysis of the expected suboptimality of stochastic gradient descent's final iterate. Our analysis applies to any (potentially nonconstant) schedule of $N$ stepsizes in $[0,1.5]^N$. Here, exact means that we provide a...

---

### 17. A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo

**Authors:** Muhammad Saeed, Dmitry Mikhaylov, Mohamed H. Alhosani, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42042v1)

**Summary:** Acoustic indices are widely used as rapid proxies for biodiversity, but they summarise the distribution of sound energy rather than the species producing it and often track richness poorly. We revise and test an Acoustic Biodiversity Index (ABI) built from species-level detections. Its primary form, ABI_E, is Shannon diversity of detections normalised by the regional species pool expected at the site and season (H / ln S_ref); temporal stability T is reported as a separate component. We first be...

---

### 18. Learning Clean Generative Processes from Noisy Measurements

**Authors:** Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42036v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42036v1)

**Summary:** We study how to learn a generative model of clean images using only noisy observations. Diffusion processes and their generalizations to non-Gaussian noise require posterior predictions at every noise level. We first show that it is possible to learn these predictions from independent noisy views using Noise2Noise regression, but only at or above the noise level of the training data. To learn the predictions below that level, needed to generate clean images, we impose consistency: a prediction s...

---

### 19. There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?

**Authors:** Rhea Sanjay Sukthanker, Pashmina Cameron

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42030v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42030v1)

**Summary:** Looping re-applies a block of layers so that each token passes through the block more than once. Adding a loop to a trained model is attractive because it leaves the parameter count, and hence the disk size, the memory footprint and the training cost unchanged. Unfortunately, every generated token pays for the loop. Re-applying m of N layers makes each token about (N+m)/N times as expensive. Loops that a model learns during large-scale pretraining justify this price, but whether loops added afte...

---

### 20. Empirical Evaluation of Quantum Kernel Methods for Classification: A Comparative Study with Classical Kernels

**Authors:** Ronak Bhalgami

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42029v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42029v1)

**Summary:** Quantum kernel methods are the most concrete near-term proposal for quantum machine learning on classical data, yet published benchmarks disagree on whether they outperform tuned classical kernels, and the disagreement cannot be resolved from the literature because the comparisons are not protocol-controlled. We argue that the obstacle is one of measurement, not theory: the usual setup fixes the quantum feature map's data scaling while grid-searching the classical kernel's hyperparameters, recom...

---

### 21. CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning

**Authors:** Yanming Zhang, Eric Papenhausen, Klaus Mueller

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42028v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42028v1)

**Summary:** Reinforcement learning is a powerful paradigm for training autonomous agents and has achieved impressive performance in complex environments. However, this success often comes at the cost of interpretability, diminishing trust and complicating efforts to debug and improve agent behavior. To address these challenges, we introduce CausalXRL, a novel framework for explainable reinforcement learning (XRL). A key feature of CausalXRL is its use of causal graph reasoning, which provides transparent, s...

---

### 22. A Neural Network Approach towards Real-Time Knot Point Density Estimates for the Nonlinear Quadrotor

**Authors:** Jasmine Ratchford, Raffaele Romagnoli, Mark H. Klein

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42027v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42027v1)

**Summary:** Spline representations provide a compact way to approximate continuous trajectories using a finite number of parameters. When approximating trajectories generated by dynamical systems, the efficiency of a spline representation depends strongly on the placement of knot points. Uniform knot distributions often lead to inefficient representations, requiring either unnecessary control points or producing poor approximations in regions where the trajectory varies rapidly. In this work we propose a le...

---

### 23. GhostPrefix: Synchronization-Free Universal Prefix Attacks for ASR Manipulation

**Authors:** Shengding Liu, Ashwin Innuganti, Qiben Yan

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42026v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42026v1)

**Summary:** We present GhostPrefix, the first synchronization-free universal adversarial prefix attack against automatic speech recognition (ASR) systems. Unlike prior audio attacks, which are typically crafted per utterance, require synchronization with the victim waveform, or target narrow objectives, GhostPrefix learns a short, reusable audio segment prepended to arbitrary live speech to exert real-time control over ASR outputs without knowledge of the future utterance or temporal alignment. A key challe...

---

### 24. Know When the Equation Is Wrong: Structural Uncertainty for LLM-Guided Symbolic Regression under Extrapolation

**Authors:** Mostafa Cham, Bayu Adhi Tama, Jianwu Wang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42024v1)

**Summary:** Large language models (LLMs) can help discover mathematical equations from data, but most LLM-guided symbolic regression methods focus on a single best equation without quantifying uncertainty over alternative functional forms. This is challenging because distinct equations can fit the observed data similarly while producing substantially different extrapolations. Our experiments on the LLM-SRBench dataset show that standard conformal intervals achieve nominal in-distribution coverage but freque...

---

### 25. When Does Jacobian Fine-Tuning Stabilize Neural PDE Emulators?

**Authors:** Shreeyam Bangera, Manya Gupta

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42013v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42013v1)

**Summary:** Neural emulators of chaotic PDEs are trained on one-step prediction but deployed autoregressively, where their errors compound. Jacobian-based regularisers aim to curb this growth, but in a chaotic system part of the growth is physical and cannot be trained away. We separate the two sources of this error with a first-order decomposition. We compare the emulator's error with a counterfactual that propagates the same one-step mistakes through the solver's Jacobian, giving an amplification ratio: t...

---

### 26. Less Loss, Fixed Weights: Logit Corrections for Forgetting

**Authors:** Hanyu Yang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42000v1)

**Summary:** When a language model is fine-tuned to follow instructions, or further pretrained on a new subject, it often gets worse at predicting standard web text. This is known as "forgetting." We ask whether this loss can be undone by simple, fixed adjustments to the model's final token predictions. Across 14 pairs of base and derived models, from 1B to 7B parameters, we fitted a fixed bonus or penalty for each token (a vocabulary bias), alone or together with a temperature. On text held out from correct...

---

### 27. New Lower Bounds for Private PAC Learning

**Authors:** Prathamesh Dharangutte, Amartya Sanyal

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41980v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41980v1)

**Summary:** We study realizable PAC learning under approximate differential privacy, and give a framework for proving lower bounds on its sample complexity. We construct classes with identical VC and Littlestone dimensions but different private sample complexities at common privacy and accuracy parameters, showing that these dimensions do not determine the sample complexity, even for improper learners. To address this we introduce the Independent Class Packing (ICP) parameter, the largest total sample compl...

---

### 28. When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning

**Authors:** Eduardo C. Garrido-Merchán

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41962v1)

**Summary:** Reinforcement learning and game theory describe the same object from two sides. Game theory says what a rational outcome of a strategic interaction is; reinforcement learning says how an agent could reach one through experience. The two literatures nevertheless keep separate vocabularies for identical structures, and the treatments that bridge them present the correspondence as analogy rather than theorem. This monograph supplies the theorems. A game is a Markov decision process in three distinc...

---

### 29. Robust Learning of Multi-Index Models under Logconcave Distributions via Weak Partial Learners

**Authors:** Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41961v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41961v1)

**Summary:** We develop a new algorithmic framework for learning Boolean concept classes under logconcave distributions. Our framework applies to broad families of multi-index models and yields significantly faster robust learners than were previously known in these settings. It extends to partial classification and testable learning. Consequently, we obtain improved learners for several fundamental concept classes, including functions of halfspaces and multiclass linear classifiers, under logconcave margina...

---

### 30. WASABI: Wasserstein Sampling via Bridge Interpolants

**Authors:** Sebastian Salazar, Dilum Fernando, Michal Kucer, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41958v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41958v1)

**Summary:** Sampling from Boltzmann distributions is a fundamental problem in physics, chemistry, and biology. We introduce WAsserstein SAmpling via Bridge Interpolants (WASABI), a method that trains a diffusion model to generate samples from a target Boltzmann distribution given access only to the energy function. WASABI minimizes the KL divergence between the distribution generated by its diffusion model and the Boltzmann target using Wasserstein gradient flows. This approach builds on a principle underly...

---

### 31. Chronos-2: A foundation model for multivariate time series forecasting

**Authors:** Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41956v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41956v1)

**Summary:** Accurate forecasting with uncertainty quantification is critical in a variety of scientific applications ranging from epidemiology and economics to energy systems and earth sciences. Yet most forecasting models still need to be developed and trained separately for each domain-specific dataset. Time series foundation models (TSFMs) aim to remove this limitation and enable the application of the same model across domains through large-scale pretraining. However, most existing TSFMs treat each time...

---

### 32. Shock Loading Accesses Reaction Pathways beyond Accelerated Thermolysis

**Authors:** Mingjie Wen, Jiahe Han, Zihan Zhou, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41955v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41955v1)

**Summary:** Thermolysis and shock loading can produce similar major stable products in energetic materials, despite different chemical evolution and reaction pathways. Here, we develop EMFF-MACE, a reactive machine-learning potential for C/H/N/O energetic materials, enabling thermolysis simulations of 20 materials and shock simulations of 10 on a common potential energy surface. Comparisons at matched normalized reaction progress reveal divergent chemical states and local structural environments. Mean react...

---

### 33. Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning

**Authors:** Zhuguanyu Wu, Congjia Chen, Ruihao Gong, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41949v1)

**Summary:** Few-step flow models generate samples through a handful of large denoising transitions. Applying GRPO to such models requires introducing stochasticity into the denoising transitions, and when a single transition spans a wide range of noise levels, the choice of the resulting stochastic policy becomes a major factor in optimization. Recent constructions constrain the policy to preserve the target flow coefficients, but this constraint admits a family of policies and offers no criterion for choos...

---

### 34. Observable-Specific Validity Tests for Scientific AI: Controlled Approximations and Intervention Response

**Authors:** Xiaoshn Nee, Haobo Zhong, Xiaomin Ni

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41939v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41939v1)

**Summary:** An approximation can reproduce an energy while missing its response, or satisfy an error tolerance without being certified by a given bound. We formulate observable-specific validity records for scientific artificial intelligence (AI) that link a reduction to its reference model, error measure, tolerance, parameter domain, and transformations or interventions. Explicit displacement and velocity certificates for a singularly perturbed oscillator recover distinct convergence orders and provide suf...

---

### 35. Binary Sparse Codes: Where are we on Energy Efficient Representations?

**Authors:** Jose Miguel Ramos, Luis SaCouto, Andreas Wichert

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41933v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41933v1)

**Summary:** Biological neural systems achieve impressive computational capabilities under tight metabolic constraints, relying on sparse cortical representations that minimise total neural activity. This combination of efficiency and representational power has motivated growing interest in sparse coding as a computational strategy for artificial systems. Artificial models designed to produce binary sparse codes span three broad paradigms, theoretical methods grounded in efficient coding, deep learning metho...

---

### 36. Variance Reduction for Decentralized Stochastic Optimization with Multiple Local Updates

**Authors:** Jie Liu, Nicola Bastianello, Wenying Xu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41927v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41927v1)

**Summary:** Multiple local updates are widely used in decentralized optimization to enhance communication efficiency, often in conjunction with stochastic gradients when exact gradient computation is costly. However, such algorithms generally converge only to a neighborhood of the optimum, whose size depends on the stepsize and the variance of gradient noise. Variance reduction has been incorporated into ADMM-based methods to achieve exact convergence in expectation, but their stepsizes typically scale inve...

---

### 37. Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective

**Authors:** Yuxin Chen, Yuejie Chi, Jianqing Fan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41903v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41903v1)

**Summary:** Reinforcement learning (RL) embodies a foundational paradigm for sequential decision-making in the face of uncertainty. The rapid growth of model complexity in emerging applications has significantly amplified the challenges of achieving data-efficient RL, particularly in sample-starved scenarios where data collection may be costly, time-consuming, or even high-stakes. Consequently, understanding and improving the data efficiency of RL algorithms has become a central problem of both fundamental ...

---

### 38. On k-nearest-neighbor regression in metric spaces

**Authors:** László Györfi, Vladimir G. Pestov, Harro Walk, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41896v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41896v1)

**Summary:** We study mean squared consistency of k-nearest-neighbor regression for metric space valued features. For a fixed feature distribution mu with atomless distance distributions, we describe how neighbor selection redistributes probability through the density of a uniformly chosen neighbor of an independent query. This gives separate conditions for the approximation error and the conditional response variance, and weakens Stone's domination condition when stronger response moments are available. In ...

---

### 39. On-Chain Behavioral Signatures for Classifying Centralized Exchange Addresses on Ethereum Using Proof-of-Reserves

**Authors:** Seongchan Park, Hyunho Jeon, Byungsoo Kang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41888v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41888v1)

**Summary:** Centralized exchanges (CEXs) are key gateways between traditional finance and digital asset markets, yet identifying their blockchain addresses remains challenging. Existing approaches often rely on opaque attribution labels or treat exchanges as secondary classification targets, leaving generalization to unseen exchanges insufficiently examined. This study develops a classification framework using Proof-of-Reserves (PoR) disclosures, with 3,033,857 Ethereum addresses from 15 CEXs and five Non-C...

---

### 40. Learning Nonlocal Interactions in Large-Scale Heterogeneous Metamaterials through Scientific Machine Learning

**Authors:** Dex Doksoo Lee, Jehyeon Shin, Yue Yu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41887v1)

**Summary:** In multiscale systems, nonlocal interactions among spatially distributed constituents can unlock collective, potentially emergent behavior irreducible to individual constituent responses. Beyond characterization, nonlocality in multiscale systems is increasingly viewed as a design element across fracture mechanics, wave physics, and disordered systems. Existing nonlocality theories provide rigorous descriptions and mechanistic insight, but often require prescribed analytic forms, range, symmetri...

---

### 41. Text as an Index for Zero-Shot Cross-Domain Knowledge Tracing

**Authors:** Yin Yi, Haiping Ma, Siyu Song, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41883v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41883v1)

**Summary:** Knowledge tracing (KT) predicts a student's next response from their history. New platforms often have question texts but no response logs for training, motivating zero-shot cross-domain KT. Existing transfer and cold-start methods use question semantics, but cross-platform semantic discrepancies limit transferability. We propose TIZSKT, which separates behavioral sequence modeling from domain-local historical evidence construction and uses text as an index rather than a directly transferable pr...

---

### 42. Overcoming the Representational Limitations of Amplitude Encoding for Quantum Neural Networks

**Authors:** Vincent Gurgul, David Prinz

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41824v1)

**Summary:** Quantum Neural Networks (QNNs) offer a framework for learning functions from classical data, but their expressive power depends critically on how inputs are encoded into quantum states. Angle encoding can require resources that scale with the number of features, whereas amplitude encoding represents $d$ features using only $\mathcal{O}(\log_2 d)$ qubits. This compactness comes at a representational cost: normalization makes conventional amplitude encoding invariant to nonzero real rescaling of t...

---

### 43. Trainable Vector Quantization for Large Language Models

**Authors:** Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41822v1)

**Summary:** Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference. However, extreme compression deteriorates model performance, which is challenging to recover due to the discrete nature of VQ parameters. Existing methods employ training-free approaches that are limited to layer-wise reconstruction loss minimization. To address this limitation, we propose TVQ, a novel method that leverages straight-throug...

---

### 44. ElTab: Elastically Looped Tabular Transformers

**Authors:** Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41819v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41819v1)

**Summary:** Tabular transformer models such as TabPFN achieve strong predictive performance but incur substantial inference costs, making them difficult to deploy in resource-constrained settings. While looped transformers reduce parameter count through weight sharing, they can lose significant predictive power when stopped early. To address this challenge, we introduce the Elastically Looped Tabular Transformer (ElTab), a single model trained to operate across different computational budgets through superv...

---

### 45. DIFFNAS: Predictor-Free Neural Architecture Search via Diffusion Model and Zero-Cost Evaluation

**Authors:** Yize Sun, Hanzhang Ma, Zixin Wu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41818v1)

**Summary:** Neural Architecture Search (NAS) has advanced the automated design of deep networks, but remains computationally expensive due to reliance on model training or performance predictors. We introduce DIFFNAS, a predictor-free NAS framework that leverages a discrete graph diffusion model guided by zero-cost performance proxies. Unlike prior diffusion-based NAS methods that require learned performance predictors, DIFFNAS conditions the generative process on training-free metrics such as MeCo and SWAP...

---

### 46. Continual Reinforcement Learning Is an Integration Problem

**Authors:** Nis Meinert, Jakob Gawlikowski, Edward Grant, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41809v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41809v1)

**Summary:** This paper presents an opinionated set of ten desiderata intended to inform the design and evaluation of reinforcement-learning agents that learn continually throughout a continuing lifetime. We use these desiderata to examine a representative selection of existing approaches. Progress on individual desiderata is valuable, but the longer-term aim should be to integrate all ten within a single agent. To our knowledge, no published evaluation has yet provided evidence for such an integration. Like...

---

### 47. Exploring Bad Minima in Transfer Learning

**Authors:** Mina Remeli

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41807v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41807v1)

**Summary:** Transfer learning is a highly successful learning paradigm in deep learning which leverages knowledge from one task and applies it to another. Despite its success, the necessary conditions for knowledge transfer are unclear and require further research. In this dissertation, our aim is to understand transferability a little better by answering the following question: Does good generalization on a source task necessarily imply transferability to a related target task? We hypothesize the answer is...

---

### 48. Backpropagation-free Deep Learning for Time-Series Classification

**Authors:** Miha Kapš, Blaž Bertalanič, Carolina Fortuna

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41805v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41805v1)

**Summary:** Deep neural networks for time series classification (TSC) are trained almost exclusively by error backpropagation, which imposes update locking and the weight-transport problem. Backpropagation-free learning rules such as Direct Feedback Alignment (DFA), Direct Random Target Projection (DRTP), and the diffusion-inspired NoProp relax these constraints but have been evaluated almost exclusively on 2D image benchmarks. We adapt these three learners to univariate TSC with 1D convolutional architectu...

---

### 49. What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer

**Authors:** Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41803v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41803v1)

**Summary:** Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited, attacks or anomalies make up 16% to 86% of the test samples, no evaluation varies that share, and six report no test on data from a second benchmark or source. We ask what such evaluations hide. On the AgentDrift and AgentDojo benchmarks we test trained detectors that read tool identities, behavior, call sequences, step embeddings or text, and a released LLM...

---

### 50. Towards Out-of-Distribution Uncertainty Quantification for Machine-Learned Interatomic Potentials via Pre-Training

**Authors:** Stefan P. Schmid, Tobias Setzer, Maximilian Scheurer

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41801v1)

**Summary:** Informative uncertainty quantification (UQ) is essential for the practical deployment of machine-learned interatomic potentials (MLIPs), as it provides insight into their reliability across chemical space. Although numerous post-hoc uncertainty estimation methods for MLIPs have recently been proposed, most have been trained in low-data regimes, restricting their applicability to narrow domains of interest. Inspired by the emergence of foundational MLIPs, we propose pre-training uncertainty estim...

---

## cs.NE

**50 papers**

### 1. Proof-Carrying Evolution: Black-Box Search, White-Box Flight

**Authors:** Amit Jain, Sergio Sanchez-Hurtado, Victor Rodriguez-Fernandez, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42043v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42043v1)

**Summary:** We study whether a language model can help design controllers whose behavior can be formally checked. In proof-carrying evolution (PCE), a search proposes controllers together with their certificates. Their mathematical forms are fixed; a proposer chooses their numerical parameters together. Certificate checks guide selection, and only a certified candidate can be returned. The deployed artifact is a control law and its certificate; the language model is used only during design. We compare four ...

---

### 2. In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents

**Authors:** Xuning He, Kai Fan, Runyu Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41291v1)

**Summary:** Long-horizon LLM agents play an important role in solving complex and sustained tasks, with ever-growing interaction contexts. However, these accumulated contexts will raise substantial computational cost and obscure key decision-relevant evidence. Existing methods typically train external compressors or context-management agents to rewrite context as shorter hard-token sequences, but such external selection may not align with the LLM's evolving representation and is necessarily lossy. In this p...

---

### 3. Input-dependent Neuromodulation Enhances Mixed-Signal Neuromorphic Hardware

**Authors:** Aashman Mehta, AbdelQader AlKilany, Dan F. M. Goodman, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41265v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41265v1)

**Summary:** Gating mechanisms allow a fixed neural network to adapt its computation to the current input by dynamically modulating its effective parameters. In the brain, neuromodulation uses this principle to move neural circuits between dynamical regimes, and deep learning exploits input-dependent gating, e.g., in gated recurrent networks and self-attention. Input-dependent modulation has also recently been shown to improve spiking neural networks, with particularly strong benefits in small, parameter-lim...

---

### 4. Memory and Recall of Color Images Using Neural Networks-1 - The Cue-Ball Model based on the Associative Memory Mechanism -

**Authors:** Hiroshi Inazawa

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41108v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41108v1)

**Summary:** This paper presents a neural network model for storing and recalling color images of different sizes using the Cue BallRecall Net systems [1,2,3,4,5]. The Cue Ball system consists of a Recall Net composed of multiple memory neurons each responsible for memorizing a single, distinct memory and a large number of neurons that represent image patterns. The images used in this study [6] consist of ten images(see Appendix). The pixel values of these images were converted into digital values and used f...

---

### 5. Local Budget Benefits, Population Commitment, and Solver Performance: A DGO Case Study with Controlled DE Transfer

**Authors:** Shiqi Li

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41099v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41099v1)

**Summary:** An evaluated candidate can improve a local search step, alter the population used by later steps, and affect a solver's final result. We distinguish these three questions using Da Gou Gun Optimization (DGO), a population optimizer designed for this study. Its JQ100 configuration evaluates an interpolation candidate during a two-sided probe. We define local budget value, population commitment effects and complete-policy performance, and give an exact example in which a locally better commitment l...

---

### 6. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

**Authors:** Jiongfan Yang, Weichen Fan, Haiwen Diao, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40647v1)

**Summary:** Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length o...

---

### 7. Dynamic Powergrid Optimization with FPGA-based Neuromorphic Higher-order Ising Machines

**Authors:** Saptarshi Maiti, Shantanu Chakrabartty, Chetan Singh Thakur

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40522v1)

**Summary:** The advent of large, high-density FPGAs such as the AMD Versal enables efficient hardware implementation of neuromorphic Ising machines, unlocking unprecedented performance for complex combinatorial optimizations. A critical application for this computing paradigm is dynamic powergrid optimization, specifically Distribution Network Reconfiguration (DNR), which seeks to mitigate severe resistive losses and reduce electricity costs by optimizing network switch configurations in real time. This pap...

---

### 8. AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn

**Authors:** Daniel Levine, David van Dijk, Kenneth Kay

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40757v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40757v1)

**Summary:** Humans and animals have a unique capacity to generalize and learn in novel circumstances, including "0-shot" inference (ZI) and continual learning (CL) -- two powerful cognitive abilities. Despite this importance, efforts to model ZI and CL are seriously limited in several ways. First, existing models typically lack components critical to ZI and CL in the brain, namely, strong inductive biases (for ZI) and autonomous control of learning (for CL). Second, models can be less tractable to analysis ...

---

### 9. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization

**Authors:** Jianghan Zhu, Cong Zhang, Ni Zhang, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40023v1)

**Summary:** Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We introduce HEMO, which makes the AOD harness itself a self-evolving optimization tar...

---

### 10. AI at a Turning Point: From ChatGPT through Neural Networks to Neuromorphic AI

**Authors:** Volker Kempe

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39796v1)

**Summary:** The tension between the established technologies of connectionist AI and their neuromorphic challengers is attracting growing attention, above all because of the enormous energy demand of the former and the low power consumption of the latter. Developing and running large AI models consumes gigawatt- to terawatt-hours of energy, while the human brain operates on a continuous 20 watts. Spiking neural networks (SNNs) counter this energy demand with a frugal approach and bring elements of self-orga...

---

### 11. Diagnosing Optimizer-Landscape Interaction via Representation in Subset Selection Multitasking: Evidence from Piano Fingering

**Authors:** Ananda Phan Iman, Tingyang Wei, Chang Wook Ahn

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39779v1)

**Summary:** Continuous relaxations are commonly used as an encoding scheme for evolutionary multitasking optimization (EMTO), allowing heterogeneous tasks to be optimized within a unified search space. However, these continuous representations fundamentally reshape the induced fitness landscape, and their impact on optimization behavior and knowledge transfer remains underexplored. In this work, we bridge the gap by analyzing the interaction between the representation-induced fitness landscape and optimizer...

---

### 12. Hardware-Aware Model Inversion in Memristive Spiking Neural Networks

**Authors:** Pablo Sorrentino, Fernando M. Quintana, Erika Covi, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39688v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39688v1)

**Summary:** Hardware-accelerated spiking neural networks (SNNs) implemented on memristive crossbar arrays offer significant gains in energy efficiency, while device variability and analog noise are sometimes assumed to hinder information extraction. However, whether these hardware effects improve, preserve, or degrade privacy after deployment remains largely unexplored. Therefore, we ask whether model-inversion leakage characterized on an SNN remains representative after the same model is mapped to a non-id...

---

### 13. GC-LIF: Spiking Group-Equivariant Neural Network With Group-Coupled Membrane Dynamics

**Authors:** Nhan Trong Luu, Duong Trung Luu, Thang Cong Truong

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39601v1)

**Summary:** Spiking neural networks (SNNs) promise event-driven, low-power inference, but on vision tasks they still acquire rotation invariance only through data augmentation. Group-equivariant CNNs build such symmetries into the architecture, yet a faithful spiking analogue is missing: a leaky integrate-and-fire (LIF) neuron placed after a $G$-equivariant convolution can break equivariance through its membrane recurrence. We give a necessary and sufficient condition for this not to happen. The layer is eq...

---

### 14. FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss

**Authors:** Hina Otake, Shinei Arakawa, Keitaro Tanaka, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39423v1)

**Summary:** Formula-Driven Supervised Learning (FDSL) enables vision pre-training without real images, but existing methods cast pre-training as classification on discretized labels, discarding continuity in the generative process. We propose Formula-Driven Supervised Metric Learning (FDSML), which derives relational supervision from image-generation parameters beyond discrete class labels. FDSML combines FineFractalDB, our refined fractal dataset with higher intra-class variation and more stable structures...

---

### 15. MulClip: A table-free activation function with monotonic and folding regimes for reservoir computing on microcontrollers

**Authors:** Guren Matsumura, Masato Takemoto, Shinzo Koyama

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39343v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39343v1)

**Summary:** This letter proposes MulClip, a lightweight activation function for reservoir computing (RC) on microcontrollers (MCUs). In a ring reservoir, a representative sparse RC topology, multiply-accumulate operations are few, and evaluating tanh accounted for 75% of the state-update time on a Cortex-M4. MulClip introduces curvature into the response using only comparison, absolute value, multiplication, and subtraction, and places its clipping threshold not at the extremum but at the point where the re...

---

### 16. The Power Watershed as a Differentiable Segmentation Layer

**Authors:** Galia Akl, Laurent Najman, Hugues Talbot

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38516v1)

**Summary:** Can a Watershed transform, the classical tool of morphological segmentation, be placed at the end of a deep network and trained through? The Power Watershed (PW) is the limit of the seeded Random Walker (RW) as p grows to infinity with edge weights raised to the power p. At every finite p the RW solves a sparse positive-definite linear system and is exactly differentiable with respect to the edge weights and the unaries through one adjoint solve; its multi-label form costs one right-hand side pe...

---

### 17. FPGAFly: A 166.7k-Neuron Fruit-Fly Connectome on One FPGA via Deferred Spike Expansion and Shared-Codeword States

**Authors:** YE Ziyang

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38118v1)

**Summary:** Synapse-resolution fruit-fly (Drosophila) connectomes enable neuron-by-neuron simulation of entire insect nervous systems, yet whole-brain models still require computationally demanding software or multiple neuromorphic chips, and single FPGAs support only small or statistical networks. Scaling to the full connectome, per-synapse spike expansion scales queue traffic with fan-out up to 11.2k, while 41-bit neuron states require 6.83 Mbit, exceeding the 6.27 Mbit on-chip block static RAM (BSRAM) of...

---

### 18. SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory

**Authors:** Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37601v1)

**Summary:** Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register wit...

---

### 19. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

**Authors:** Joseph Natter, Long Vu, Yifan Zhang, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37598v1)

**Summary:** Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. E...

---

### 20. GNBG-C: A Unified and Configurable Benchmark Generator for Constrained Continuous Optimization

**Authors:** Ali Ghasemzadeh, Erfan Babakhani, Armin Khosravi, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37590v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37590v1)

**Summary:** Many real-world optimization tasks are governed not only by what should be optimized, but also by what is allowed: a solution must first satisfy physical, operational, safety, budgetary, or structural requirements before its objective value becomes meaningful. Yet benchmark design for constrained continuous optimization often treats these restrictions as fixed properties of predefined test instances. Existing generators and benchmark suites provide essential foundations for reproducible comparis...

---

### 21. Every route counts, but some count more: a max-plus view of the C. elegans brain

**Authors:** Emma Reyner-Fuentes, Sebastian Rudolph, Carmen Peláez-Moreno, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37587v1)

**Summary:** Brains do not simply add up every signal they receive: they select which routes dominate. Yet connectomes are usually analyzed with tools that sum over all paths and place neural states in Euclidean spaces, blurring the feedback circuits that may sustain internal states. Here we treat neural signaling as routing instead of diffusion and describe it with max-plus algebra, in which signals accumulate along a path and the strongest route prevails. We propose a model in which the functional connecto...

---

### 22. Autonomous fixed-wing interception using reinforcement learning

**Authors:** Daan van Hamersveld, Ewoud Smeur, Iurii Kriachko

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37470v1)

**Summary:** Medium altitude, long endurance unmanned aerial systems such as Shahed-type strike drones are an unanswered threat in modern conflicts. Conventional air defense systems are too expensive to provide a feasible large-scale solution. Quadcopter interceptors are a cheap, battle-proven alternative, but their extremely limited flight time restricts them to low altitude targets at short range, whereas fixed-wing platforms have the endurance to reach higher altitude targets from longer distances. Howeve...

---

### 23. Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?

**Authors:** Sichun Luo, Yi Huang, Mukai Li, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37276v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37276v1)

**Summary:** Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substantial execution costs. We investigate how evaluation budgets can be allocated across these two roles. Our experiments show that sparse feedback can sustain productive evolution, while additional targeted evaluation impro...

---

### 24. Physiology-Informed Audio Quality and Listening Effort Estimation

**Authors:** Niall McGuire, Dimitra Emmanouilidou

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36865v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36865v1)

**Summary:** Audio systems aim to maximise the listener's perceived quality, traditionally evaluated through mean opinion scoring (MOS), a subjective process that is slow, costly, and collected only after playback. Machine learning now predicts MOS directly from the audio, but in generalising across participants it tends to discard the subject variance that defines individual perception. Neurophysiological measures may offer a complementary signal taken directly from the listener, objective, implicit, and co...

---

### 25. Characterizing Privacy Leakage in Spiking Neural Networks: A Systematic Analysis of Temporal Dynamics, Stochasticity, Neuronal Dynamics and Learning Mechanisms

**Authors:** Ayana Moshruba, Maryam Parsa

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36243v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36243v1)

**Summary:** Spiking neural networks (SNNs) encode information not only in whether neurons fire but also in when they fire, and this temporal dimension shapes what a trained network reveals about its training data. Biologically inspired firing patterns can reduce membership leakage in SNNs without changing the network architecture, which positions temporal dynamics as a design variable for privacy. A change in firing behavior, however, alters stochasticity, spike timing, neuronal response, and the learning p...

---

### 26. Dynamical coarse-graining of neural-network training

**Authors:** Lin-Juan Wang, Da Li, Huiling Duan, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36180v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36180v1)

**Summary:** Dynamical coarse-graining of neural networks gives macroscopic observables and enables training to be predicted, and controlled in a state space far smaller than the parameter space. In this paper, we first define the learning operator following the training law of neural networks and establish a descent theorem for the learning operator, which serves to determine whether the operator is sufficient to characterize the learning dynamics. Then the exact closure theorem and the dynamic coarse-grain...

---

### 27. TRON: Transferring Naturally Evolved Network Architectures into Neuroevolution

**Authors:** Konstantinos Zacharopoulos, Alexandra Bekou, Jose M Serradell, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35647v1)

**Summary:** Neural architecture search (NAS) is challenging because of the vast, non-linear space of artificial neural network (ANN) topologies. Evolutionary methods can generate architectures, but their effectiveness is limited by difficulties in preserving functional organization during mutation and recombination. Naturally evolved biological networks may provide organizational principles that support adaptation and evolvability. Here, we introduce TRON (TRansfer Of Natural networks), a neuroevolution fra...

---

### 28. Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean

**Authors:** Per Kristian Lehre

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35595v2) | 📄 [PDF](https://arxiv.org/pdf/2610.35595v2)

**Summary:** LLMs now prove hard theorems in Lean. Can they also design algorithms and prove their correctness and efficiency? LLM-guided design of optimisation heuristics (such as AlphaEvolve) is purely empirical. Automated theorem provers with LLMs prove given statements. So far, there has been little evidence that LLMs can do both: design an algorithm and guarantee its efficiency by a mathematical proof. We present a staged pipeline modelled after research methodology in design and analysis of evolutionar...

---

### 29. An Interactive Evolutionary Multiobjective Optimization Algorithm Based on Interpretable Active Preference Learning

**Authors:** Thomas Quadt, Boris Čule, Roy Lindelauf, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35470v1)

**Summary:** Many decision-making tasks are inherently multi-objective. Interactive evolutionary multi-objective optimization algorithms (iEMOAs) are particularly well-suited to help the decision-maker find their most preferred solution. However, many of these algorithms employ black-box preference models. For high-stakes decision-making tasks, like healthcare and defense, a high level of transparency is needed, for instance to support accountability. We propose an interpretable iEMOA which uses active learn...

---

### 30. Understanding the Co-evolutionary Solution Exchange of the MOEA/D: Already the Smallest Communication Radius Gives the Best-Possible Speed-Up

**Authors:** Benjamin Doerr, Moaad Elmoutassim, Martin S. Krejca, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35373v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35373v1)

**Summary:** Besides domination-based algorithms such as the NSGA-II, the decomposition-based MOEA/D is one of the most popular and successful optimization heuristic for multi-objective problems. It decomposes the problem into several, single-objective subproblems. By solving these in a co-evolutionary manner and archiving non-dominated solutions, it approximates or computes the Pareto front. Interestingly, so far no advantages from the co-evolutionary communication of subproblem solutions were proven. In th...

---

### 31. A Dynamic Decomposition Strategy for the MOEA/D With Proven Performance Guarantees

**Authors:** Benjamin Doerr, Martin S. Krejca, Noé Weeks

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35334v1)

**Summary:** The MOEA/D is one of the most successful multi-objective evolutionary algorithms. It operates by decomposing the optimization problem into single-objective subproblems, which are then solved in a co-evolutionary manner. The performance of the MOEA/D depends critically on this decomposition. In this work, we propose a novel way to adjust this decomposition on the fly, for the case of discrete bi-objective optimization. Different from all previous works in this direction, we support our new algori...

---

### 32. Intellectual Property Protection of Hyperdimensional Computing Classifiers: Black-Box Ownership Verification via Model Watermarking

**Authors:** Hamed Poursiami, Farshad Soleiman, Ahmad Tahmasivand, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.34942v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34942v1)

**Summary:** Hyperdimensional computing (HDC) offers efficient learning and inference for resource-constrained systems, yet ownership verification of its models remains underexplored. We present the first systematic investigation of model watermarking in HDC by adapting backdoor-based embedding to three classifiers with different prototype-learning mechanisms. Across four benchmarks, with conventional neural networks as references, we examine whether watermarks can be learned without compromising task accura...

---

### 33. One Mean Log-Mel Vector per Phoneme: Simple and Fast Text Injection for Speech Recognition

**Authors:** Albert Zeyer, Davyd Naveriani, Dorian Koch, et al.

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34623v1)

**Summary:** Text injection trains speech recognition models on unpaired text alongside paired audio. We feed the speech encoder synthetic input derived from text so the whole model learns from it. Previously, we synthesized this input with a frozen text-to-speech (TTS) model. Here, a simple lookup table replaces the TTS model: a mean log-mel vector (or one-hot encoding) per phoneme, repeated for a random duration drawn from alignment statistics, with silence between words. Training is 1.8 times faster than ...

---

### 34. Edge-Centric Adaptive Neural Activation via Parametric Tanh Functions

**Authors:** Andreas Falkenberg

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34154v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34154v1)

**Summary:** Within the broader landscape of artificial intelligence architectures, this paper introduces a compact, edge-centric neural framework that resolves the computational bottlenecks of modern edge-activated paradigms like Kolmogorov-Arnold Networks (KANs) while retaining their expressiveness over traditional Multi-Layer Perceptrons (MLPs). While KANs demonstrate remarkable representational capacity by placing learnable univariate functions on connection edges rather than hidden nodes, their reliance...

---

### 35. Functional Superoscillations in a Wave Processor

**Authors:** Yuntian Wang, Md Sadman Sakib Rahman, Aydogan Ozcan

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34111v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34111v1)

**Summary:** Physical wave processors are constrained by diffraction, but the bandwidth of the mathematical functions they implement need not be set by it. Here, we demonstrate continuous and multiplexed optical processing of superoscillatory functions, in which a scalar argument is encoded onto a wavefront and a fixed diffractive wave processor synthesizes optical responses that approximate the corresponding function outputs in parallel. Unlike conventional superoscillatory optics that generates predetermin...

---

### 36. ChroNoC: A Tableless TDM Circuit-Switched NoC With Delay-Aware Deployment for Time-Sensitive Neuromorphic Computing

**Authors:** Mohammad Rasoul Roshanshah, Mehdi Modarressi, Saeed Safari

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34083v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34083v1)

**Summary:** Time-sensitive neuromorphic architectures require predictable interconnects to preserve precise event timing. Statically scheduled time-division-multiplexed (TDM) circuit-switched networks-on-chip (NoCs) provide deterministic latency at the cost of linear configuration-memory scaling with schedule depth. Furthermore, jointly optimizing task placement, routing, and scheduling creates an intractable combinatorial search space. Existing deployment frameworks also ignore algorithmic axonal delays by...

---

### 37. Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome

**Authors:** John R. Minnick, Jesus Gonzalez-Ferrer, Jinghui Geng, et al.

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33881v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33881v1)

**Summary:** Connectomes now map the neurons and synapses of an adult fly's brain and nerve cord, but how much of behaviour follows from the wiring is unknown. Here we turn one such connectome into a spiking network of 172,433 neurons with a published brain model's untuned parameters, and run it alone and inside a simulated body. Two fixed rules join them: odours and looming objects drive sensory neurons, and motor neurons move the legs. Alone, the network passes a signal to the motor neurons it is known to ...

---

### 38. Optimal Connectivity of Random Boolean Networks for Reservoir Computing

**Authors:** Christopher Michael Skeide Vibe, Aliaksandr Hubin, Stefano Nichele

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33498v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33498v1)

**Summary:** Reservoir computing shifts the focus from training a system's internal dynamics to designing dynamics that expose useful computational capabilities via linear projection. We study random Boolean networks as reservoirs: cellular automata with random recurrent wiring and a random rule at each node. Their main parameter is the connectivity, the mean number of edges into a node. Without input, these networks pass from ordered to chaotic dynamics at a connectivity of 2, where their dynamics are expec...

---

### 39. Freezing Mechanism and Topology Dependence of Information Flow Structure in Small-Scale Particle Swarm Optimization

**Authors:** Zhenglong Xiang, Hongrun Wu, Yu Xue, et al.

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33421v1)

**Summary:** The neighborhood topology of particle swarm optimization (PSO) determines information propagation and regulates the exploration-exploitation balance. However, existing evaluation methods based on fitness and spatial diversity fail to characterize the dynamic evolution internal interaction structure of the population. To address this gap, this paper focuses on small-scale PSO (20-50 particles) with regular topologies and models the iterative process as a dynamic weighted influence graph. We const...

---

### 40. MOSHO: A Native Discrete Shark-Inspired Metaheuristic for Hardware-Aware Neural Architecture Search

**Authors:** Nazim Abdeerhmane Aouni, Zakaria Soualah Mohammed, Maroua Ogab, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.33358v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33358v1)

**Summary:** Hardware-aware neural architecture search (NAS) requires jointly optimizing predictive accuracy and device-specific latency over discrete search spaces. While multi-objective swarm optimizers show promise, continuous formulations such as the Multi-Objective White Shark Optimizer (MOWSO) can suffer from quantization noise when rounded to integer-encoded architecture vectors. To address this limitation, we propose MOSHO (Multi-Objective Shark Hunting Optimization), a native discrete metaheuristic ...

---

### 41. PAFS: Perturbation-Aware Firing Scaffolds for Robust Event-Based SNNs

**Authors:** Ning Liu, Jun Sun, Hao Guo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32409v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32409v1)

**Summary:** Event-based spiking neural networks (SNNs) encode information through temporal firing dynamics, but the same stateful computation makes their predictions sensitive to event loss, timestamp jitter, and speed variation. These perturbations alter evidence accumulation, yet late-layer firing trajectories can retain error-diagnostic structure that is absent from the final logits alone. We introduce Perturbation-Aware Firing Scaffolds (PAFS), a labeled post-training calibration method that exploits th...

---

### 42. Searching with Sparse Histories: Cross-Task Architecture Search from Incomplete Search Logs and Zero-Cost Proxies

**Authors:** Yuefeng Xu, Jun Yu

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32179v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32179v1)

**Summary:** Neural architecture search (NAS) is expensive, but cross-task transfer can reduce costs by reusing knowledge from previous tasks. However, existing methods struggle with sparse search histories and task-specific transfer failures. We propose a method, a risk-robust strategy that combines sparse source logs with zero-cost proxies through champion-based initialization and joint pairwise-ranker pretraining. On TransNAS-Bench-101, the proposal mitigates severe worst-case failures, reducing worst-10%...

---

### 43. A Resource-Efficient and Precision-Scalable FPGA Accelerator for Spiking Neural Networks Using Minifloat Arithmetic

**Authors:** Ali Mehrabi, Philip C. Jose

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32052v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32052v1)

**Summary:** Spiking neural networks (SNNs) are well suited to event-driven edge intelligence, but the arithmetic complexity, memory footprint, and power consumption associated with conventional floating-point implementations can limit their deployment on resource-constrained hardware. This paper presents a precision-scalable and resource-efficient SNN hardware accelerator architecture based on parameterized minifloat arithmetic. The proposed architecture implements recurrent leaky integrate-and-fire (LIF) n...

---

### 44. RobustNCL: Robustifying Neuromorphic Continual Learning under Transient Faults with Lightweight Detect-and-Cure Strategy

**Authors:** Rachmad Vidya Wicaksana Putra, Shuochen Zhou, Muhammad Shafique

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31954v1)

**Summary:** In neural networks, continual learning (CL) is a prominent approach for enabling deployed systems to adapt to dynamic operational environments by effectively learning from new unseen data at runtime. Recently, the neuromorphic continual learning (NCL) concept has emerged as an energy-efficient alternative to CL by leveraging sparse event-based operations. However, NCL performance can be undermined by transient faults in the hardware platforms, which may come from high-energy particle strikes at ...

---

### 45. ENCL: Enabling Efficient Neuromorphic Continual Learning with Local Learning Rule and Sub-Network Freezing Strategy

**Authors:** Rachmad Vidya Wicaksana Putra, Shuochen Zhou, Hassan Raza, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31927v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31927v1)

**Summary:** Continual learning (CL) in neural networks is a promising learning approach for updating the knowledge of deployed systems based on new data encountered at run time, that have not been learned during the offline training phase. To enable their power/energy-efficient CL processing, neuromorphic continual learning (NCL) concept with sparse event-based operations have recently been introduced. However, state-of-the-art NCL methods typically employ the memory-hungry data/experience replay, coupled w...

---

### 46. First hardware demonstration of a continuous-state probabilistic computer with programmable energy-defined sampling

**Authors:** Chao Fang, Hsuan Yao Tu, Yihan He, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31339v1)

**Summary:** Probabilistic computing has proved useful for combinatorial optimization, but conventional implementations rely on binary stochastic units and sigmoid-based updates. Extending these systems to continuous variables requires binary encoding. Here we introduce a continuous probabilistic computer (CPC) whose continuous probabilistic bits sample bounded states from conditional distributions defined by local energies. Separating random-source generation from conditional sampling provides a route to us...

---

### 47. AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments

**Authors:** Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31326v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31326v1)

**Summary:** Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present AgenticEvolve, an evolutionary program search framework in which each island is run by a persistent large language model agent. Between evaluations, the agent designs and runs experiments on the candidate program. To measure t...

---

### 48. HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning

**Authors:** Sudipta Paul, Pengrui Quan, Aounon Kumar, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30042v1)

**Summary:** Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls th...

---

### 49. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v2) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v2)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 50. Probing Spatial and Spectral Grounding in EEG Foundation Models

**Authors:** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29367v1)

**Summary:** EEG foundation models are advancing at an unprecedented pace, yet their evaluation is driven by downstream accuracy, which reveals little about whether their predictions rely on physiologically interpretable signal structure. We introduce a set of perturbation probes in two grounding axes: spatial grounding in channel identity and topographic locality, and spectral grounding in oscillatory content and waveform morphology. We apply these probes to five published EEG foundation models across motor...

---

## q-bio.NC

**50 papers**

### 1. Hyperbolic embedding of higher-order simplicial networks

**Authors:** Martin Guillemaud, Vito Latora, Mario Chavez

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41684v1)

**Summary:** Many biological interactions involve groups rather than pairs, as when several proteins assemble into a multi-protein complex. Simplicial complexes naturally capture these collective interactions. Existing hyperbolic embeddings represent network hierarchy and similarity through a few interpretable coordinates, but rely only on pairwise links: they cannot distinguish three units engaged in a common interaction from three units connected only in pairs. We introduce here the hyperbolic higher-order...

---

### 2. Expression of White and Gray Matter Autism Functional Network Connectivity Signatures in Infancy

**Authors:** Qiang Li, Jingyu Liu, Zening Fu, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40839v1)

**Summary:** Functional connectivity studies have provided valuable insights into altered brain organization in autism spectrum disorder (ASD). However, most functional connectivity studies focus exclusively on either gray matter (GM) regions or white matter (WM) tracts and examine specific age groups, rather than investigating their functional interactions across brain development. This limits our understanding of how GM-WM functional interactions evolve developmentally and may obscure important aspects of ...

---

### 3. A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening

**Authors:** Zach Paris, Emily Finn

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40511v1)

**Summary:** Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial electrophysiology and f...

---

### 4. Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI

**Authors:** Serwan Jassim, Victoria Bosch, Daniel Anthes, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40280v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40280v1)

**Summary:** Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any representation derive...

---

### 5. Recognition of auditory objects from continuous and ultra-sparse spike streams in neuromorphic devices

**Authors:** Leonardo E. S. Tavares, Kevin D. Sargent, Jon T. Sakata, et al.

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38564v1)

**Summary:** Energy consumption is a major concern for modern artificial intelligence (AI) applications. The brain is thought to achieve energy-efficient computation through sparse coding schemes. By emulating the spiking dynamics of the brain, neuromorphic chips hold the potential to realize energy-efficient AI. In this work, we use birdsong to demonstrate that auditory object recognition can be achieved using ultra-sparse coding. Feature-detecting neurons tuned to short temporal features ($\sim$37 ms), sam...

---

### 6. REVBRAIN: Real-time Probabilistic EEG Forecasting Using Residual Vector Quantization

**Authors:** Hanna Pankka, Jaakko Lehtinen, Timo Roine

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38558v1)

**Summary:** Real-time forecasting of resting-state EEG signals is required by applications like brain-state-dependent stimulation, where computer generated actions are coupled with ongoing neural oscillations. Recently, the deep learning model WaveNet was proposed for the forecasting task. It shows superior accuracy compared to the prevailing method, the linear autoregressive (AR) model, and provides a built-in uncertainty measure due to its probabilistic modeling framework. However, inference using WaveNet...

---

### 7. Data Amount Heterogeneity Improves Performance in Federated Learning for Neuroimaging

**Authors:** Paul Kurian, Tamoghna Chattopadhyay, Abhijith Shaji, et al.

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38172v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38172v1)

**Summary:** Federated Learning (FL) allows for secure analysis of distributed data without data sharing. We and others have successfully applied FL to neuroimaging tasks, such as Alzheimer's disease classification from structural magnetic resonance imaging (MRI). FL trains a deep learning model locally at each site, encrypts the local model parameters and sends them to a federation controller that aggregates the local models under homomorphic encryption, the resulting community model is sent back to the sit...

---

### 8. Solitary movement style predicts collective foraging while whom to follow emerges only in company

**Authors:** Hiroshi Higashi

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37978v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37978v1)

**Summary:** How far can behaviour inside a group, and the group's performance, be predicted from members measured while alone? We tested this on three public datasets of human collective foraging (621, 128 and 1,133 participants). A low-dimensional individual representation estimated from private-phase movement was mapped onto behaviour inside the group through a mapping learned on other participants. Private information processing was stable between the two halves of a session (split-half reliability, the ...

---

### 9. Every route counts, but some count more: a max-plus view of the C. elegans brain

**Authors:** Emma Reyner-Fuentes, Sebastian Rudolph, Carmen Peláez-Moreno, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37587v1)

**Summary:** Brains do not simply add up every signal they receive: they select which routes dominate. Yet connectomes are usually analyzed with tools that sum over all paths and place neural states in Euclidean spaces, blurring the feedback circuits that may sustain internal states. Here we treat neural signaling as routing instead of diffusion and describe it with max-plus algebra, in which signals accumulate along a path and the strongest route prevails. We propose a model in which the functional connecto...

---

### 10. Sufficiency Theorem and Closed-Form Posterior for a Windowed Change Point Detection Task

**Authors:** Payton Hanks, Rishidev Chaudhuri, Timothy D. Hanks

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37486v1)

**Summary:** To function effectively in a changing world, agents must detect changes and act on them in a timely fashion. We study this in the context of a change point detection task in which clicks arrive from a Poisson process whose rate changes at an unknown time. An agent must declare the change within a detection window of fixed width or the trial ends in a miss. Here we prove a window sufficiency theorem, which states that the posterior probability of a change depends only on the clicks within the mos...

---

### 11. Local learning is all you need: brain-aligned predictive coding networks

**Authors:** Dirk Gütlin, Ryszard Auksztulewicz, Adrien Doerig

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37327v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37327v1)

**Summary:** Predictive Coding (PC) is an influential account of how brain representations emerge through hierarchical, local, self-supervised prediction-based learning, without requiring globally propagated error signals. Despite extensive evidence supporting PC, a striking paradox persists: computational models built on these biologically grounded principles have consistently failed to match state-of-the-art Deep Neural Networks in performance and brain-alignment. Here, we show that this paradox can be ove...

---

### 12. Exploring Neural Dynamics with Time Delays: A Numerical and Bifurcation Analysis Approach

**Authors:** Martin R Nelson, Jonathan J Crofts

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36920v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36920v1)

**Summary:** The Wilson-Cowan model is a classic example of a ``neural mass model'' - a simplified yet powerful way to describe the activity of large networks of neurons. It is particularly interesting because, even in its relatively simple form, it can produce a surprising variety of behaviours, from steady rhythms to complex oscillations. A key factor influencing these dynamics is the presence of time delays, reflecting the time it takes for signals to travel between neurons. This article offers an accessi...

---

### 13. Neuronal Identity as an Organizational Basis for Analyzing Neural Population Dynamics

**Authors:** Seungjae Han, Joshua Yedam You, Soi Kim, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36745v1)

**Summary:** Individual neurons exhibit diverse molecular, morphological, and electrophysiological properties that shape their distinct roles in neural circuits. While these multimodal features are largely shared across individuals, they remain an underutilized source of information in analyzing neural population dynamics. We posit that these shared biological profiles provide a common reference for relating neural dynamics across subjects and recording sessions. Our framework leverages this structure by rou...

---

### 14. The geometry of cognition: from neural populations to neurotechnology

**Authors:** Lucas Bayones, Devika Narain, Roman Rossi-Pool

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36541v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36541v1)

**Summary:** Cognition is implemented by distributed neural populations whose collective activity evolves through structured, low-dimensional state spaces. In this review, we survey the analytical and conceptual tools used to study latent population dynamics in biological neural networks. We begin with single-unit coding, which remains essential for interpreting neuronal selectivity, and then review population-level approaches, including population vectors, cosine similarity, principal component analysis and...

---

### 15. CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments

**Authors:** Kianté Fernandez, Caitlin Chen, Jialu Zhou, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36484v1)

**Summary:** Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, ...

---

### 16. Stationary Action Principles for Neuronal Growth

**Authors:** Nathan Brodeur, Cristian Staii

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36463v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36463v1)

**Summary:** Neuronal growth is guided by biochemical, mechanical, and geometrical cues while being influenced by stochastic fluctuations in cytoskeletal dynamics, adhesion, and growth cone sensing. Here, we develop two complementary variational descriptions of mechanically guided axonal growth. First, for neurons growing on periodic parallel micropatterns, we use Langevin and Fokker--Planck models to derive a stochastic path action incorporating deterministic substrate guidance and random fluctuations. The ...

---

### 17. Hierarchical connectivity sets the upper critical dimension of neural avalanches

**Authors:** W. A. Zúñiga-Galindo

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36404v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36404v1)

**Summary:** Neural avalanches with size exponent $3/2$ are usually explained by mean-field critical branching, which for short-range coupling requires dimension $N\ge4$. We show that hierarchical connectivity removes this constraint. In a $p$-adic version of the Buice--Cowan field theory, a coupling that decays by $p^{-(N+σ)}$ per hierarchical level selects the Taibleson--Vladimirov operator, and the critical theory is ultrametric directed percolation with upper critical dimension $N_c=2σ$. Exact simulation...

---

### 18. p-Adic statistical field theory of fluctuation effects in hierarchical neural networks

**Authors:** W. A. Zúñiga-Galindo

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36400v1)

**Summary:** The Buice-Cowan field theory [PRE 75, 051919 (2007)] describes fluctuations and correlations of neural activity through a path integral whose mean-field limit is the Wilson-Cowan equation and whose critical behavior belongs to the directed percolation class. In its continuum limit the neurons are the points of a Euclidean space and activity spreads by ordinary diffusion, which encodes neither the hierarchical organization of cortical networks nor their small-world property. We formulate a versio...

---

### 19. SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding

**Authors:** Matea Tashkovska, Naël Ouerghemi, Haozhe Qi, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36384v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36384v1)

**Summary:** Perceiving human body motion is critical for multimodal systems that understand and assist people. Yet current evaluations of Multimodal Large Language Models (MLLMs) largely focus on objects, scenes, and coarse actions, leaving their ability to reason about the body itself poorly assessed. This is especially challenging from the egocentric perspective, in which the body is only partially visible and motion must be inferred from occluded and temporally distributed cues. We introduce SOMA, a benc...

---

### 20. Temporal smoothness constraints on efficient neurobiological codes imply temporal specialization

**Authors:** John J. Vastola, Samuel J. Gershman

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36272v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36272v1)

**Summary:** Neurobiological circuits may be energy efficient in part because there is a division of labor: different subsystems compute or represent different things. In light of this, it is interesting that a major difference between subsystems is the time scale on which they typically vary. Here, we argue that temporal smoothness constraints---the idea that it may be energetically costly for systems to vary much more quickly than their typical time scale---imply a certain division of labor with respect to...

---

### 21. MtReNIRS: A Self-Supervised Foundation Model for Transferable Neurovascular Representations

**Authors:** Tony Chae, Kleanthis Avramidis, Dimitra Emmanouilidou, et al.

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.36159v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36159v1)

**Summary:** Functional near-infrared spectroscopy (fNIRS) offers a promising approach for monitoring the hemodynamic correlates of neural activity in naturalistic settings. However, existing modeling methods for fNIRS are largely confined to small-scale, single-session data with low sampling rates, driven by high heterogeneity in acquisition devices and optode montages. In addition, the complex spatiotemporal structure of fNIRS signals further restricts model scalability and transferability across settings....

---

### 22. On the stability of learning

**Authors:** John J. Vastola

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35856v1)

**Summary:** Learning algorithms are usually analyzed under the assumption that informative gradients are continuously available. But this is not always true---learning signals in biological neural networks, for example, may be sparse, local, and only intermittently available at any given synapse. In this work, we show that if gradient information is noisy and only intermittently available, learning may be unstable. In particular, even if average learning dynamics converge to the correct optimum, variance in...

---

### 23. A theory of noisy linear recurrent neural network learning dynamics

**Authors:** John J. Vastola, Kanaka Rajan

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35785v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35785v1)

**Summary:** Biological neural networks are noisy: their dynamics involve difficult-to-predict fluctuations which are likely due not just to chaos, but also to a variety of low-level biophysical processes. Despite the omnipresence of intrinsic noise, its theoretical consequences are incompletely understood, especially in the context of learning. For example, does noise meaningfully shape representation learning, or is it better viewed as a nuisance factor whose presence or absence changes little about what s...

---

### 24. Phase response approach to networked neural activity models with delays

**Authors:** Martin R Nelson, Jonathan J Crofts

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35638v1)

**Summary:** Networks of delay-coupled neural mass models alternate between synchrony and anti-phase locking as the delay between brain regions increases. The origin of these delay-dependent bands has remained unclear. Here, we show that a single function, the phase interaction function $H$ of an isolated node, predicts where the bands occur and explains why they repeat. For a Wilson--Cowan model with intra-nodal delay $τ$ and inter-nodal delay $ρ$, we compute the limit cycle and phase response, and hence $H...

---

### 25. Comparing Measurements of Pictorial Depth: Conditions for Placing Methods, Observers and Depiction Styles on One Scale

**Authors:** Adam Y. Shavit

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35200v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35200v1)

**Summary:** Two observers can agree about what lies in front in a picture yet report different amounts of apparent depth. People report pictorial depth by judging which of two points looks nearer, setting a probe to match a surface, adjusting relative sizes, or rating three-dimensionality. Two such methods can agree closely without sharing a unit. We ask when different methods, observers, depiction styles and viewing conditions can share one scale. Each set of scores, a measurement block, is a graph node. T...

---

### 26. Retrieval-Augmented Parkinson's Disease Classification from Resting-State Functional Connectivity

**Authors:** Tara Niknam, Sana Hassan Imam, Daniel Kristanto

**Published:** 2026-10-26

🔗 [Paper](http://arxiv.org/abs/2610.35107v1) | 📄 [PDF](https://arxiv.org/pdf/2610.35107v1)

**Summary:** Altered resting-state functional connectivity (FC) is a candidate marker for the diagnosis of Parkinson's disease (PD). Publicly available PD datasets, however, are small and fragmented across sites, scanners and clinical criteria. Transfer learning mitigates data scarcity by reusing a model trained on larger cohorts, but represents their knowledge primarily through a single set of weights shared by all individuals. Motivated by precision neuroimaging, we propose a retrieval-augmented classifica...

---

### 27. Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Captures Future Volitional Action in Drosophila

**Authors:** Declan Kutscher, Reece Keller, Alyn Kirsch, et al.

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34638v1)

**Summary:** Animals have a remarkable capacity for autonomy---driven by intrinsic motivation---without external sensory cues or extrinsic objectives, yet the computational mechanisms behind this ability largely remain a mystery. We combine whole-brain recordings in the fruit fly (Drosophila melanogaster), which reveal neural representations of spontaneous exploratory decisions more than 10 seconds in advance, with a neuromechanical digital twin to test whether optimizing intrinsic goals yields realistically...

---

### 28. Analysis of Biomarkers from Visual Explorations in Individuals Suspected to Be in the Prodromal Phase of Parkinson's Disease

**Authors:** Maria F. Alcala-Durand, J. Camilo Puerta-Acevedo, Valle Pérez del Olmo, et al.

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34524v1)

**Summary:** Identifying prodromal Parkinson's Disease is a precondition for any future treatment that modifies the course of the disease, since such therapies would ideally act on the initial pathogenic events, early enough to delay the clinical onset of the disease rather than only slow its progression. In this work, a visual exploration model is retrained on an expanded corpus. Without any further training or threshold recalibration, it is then tested on an enriched cohort of patients with high risk of be...

---

### 29. The dominance of feedback mechanisms for perception in the central visual field: the flip tilt illusion by backward masking and the Feedforward-Feedback-Verify-reWeight algorithm

**Authors:** Li Zhaoping

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34455v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34455v1)

**Summary:** The flip tilt illusion is the misperception of the orientation of the alignment between a pair of dots by 90 degrees. It occurs when the dot-pair contains one black dot and one white dot, is typically visible only in the peripheral visual field. It is predicted by the central-peripheral dichotomy (CPD) theory. Along the visual pathway from retina to downstream stages, our brain admits only a tiny fraction of visual input information for recognition due to a processing bottleneck that starts from...

---

### 30. New developments in the geometry and topology of 3D head-direction coding

**Authors:** Jean Laurens

**Published:** 2026-10-25

🔗 [Paper](http://arxiv.org/abs/2610.34106v1) | 📄 [PDF](https://arxiv.org/pdf/2610.34106v1)

**Summary:** The head-direction (HD) system is a neuronal compass that represents head orientation in 3D. Its encoding of 3D head orientation can be decomposed into a multiplexed representation of 2D head tilt relative to gravity and 1D head orientation in the horizontal plane (azimuth). Defining azimuth during 3D motion is not trivial, and recent studies have indicated that the HD system implements a so-called dual-axis/tilted-azimuth (DA/TA) rule, a representation that is well supported experimentally but ...

---

### 31. Multitask Interactions in Recurrent Dynamics across 100 Cognitive Tasks

**Authors:** Sílvia García-Hernández, Leema Hamid, Manuel Brenner

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33926v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33926v1)

**Summary:** The brain continually learns tasks with very different computational demands. Recurrent neural networks (RNNs) have been used as dynamical surrogates for studying task solutions, with recent work extending this approach to joint training on multitask batteries. However, it remains unclear how tasks interact as these batteries grow in scale and heterogeneity: under what conditions do they transfer or interfere with one another, and how do these effects relate to task complexity and model structur...

---

### 32. Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome

**Authors:** John R. Minnick, Jesus Gonzalez-Ferrer, Jinghui Geng, et al.

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33881v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33881v1)

**Summary:** Connectomes now map the neurons and synapses of an adult fly's brain and nerve cord, but how much of behaviour follows from the wiring is unknown. Here we turn one such connectome into a spiking network of 172,433 neurons with a published brain model's untuned parameters, and run it alone and inside a simulated body. Two fixed rules join them: odours and looming objects drive sensory neurons, and motor neurons move the legs. Alone, the network passes a signal to the motor neurons it is known to ...

---

### 33. Efficiency--Complexity Tradeoff and Constrained Percolation

**Authors:** Yuliy Baryshnikov, Efe Onaran

**Published:** 2026-10-24

🔗 [Paper](http://arxiv.org/abs/2610.33864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33864v1)

**Summary:** We study the efficiency--complexity tradeoff for resource-limited agents through directed first-passage percolation. Nonnegative i.i.d. edge weights represent physical energy expenditure, while the logarithmic size of a constrained path family measures representational complexity. For translation-invariant families, a path-joining property yields deterministic large-distance costs in rational directions and joint convexity in constraint parameter and direction, under suitable moment and feasibil...

---

### 34. ZENO: Nonlinear filtering with Zakai Equation Neural Operators

**Authors:** Aaditya Prasad, Steven W. Flavell, Brian DePasquale

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32926v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32926v1)

**Summary:** State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differential equation (SPDE) that combines the forward Kolmogorov operator (known as the Fokker-Planck equation) with observed likelihood updates. Although solving these high-dimensional SPDEs is often impossible analytically and i...

---

### 35. Neural-DISCO: Source-Conditioned Counterfactual Editing of Neural Population Activity

**Authors:** Nico Policzer, James Ho, Joseph Soo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.33145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33145v1)

**Summary:** Understanding how neural activity encodes behavioral and sensory variables is a key challenge in systems neuroscience. This requires models that go beyond predicting activity from labels and instead support source-conditioned counterfactual editing: given a recorded source response, we should be able to edit one measured behavioral or stimulus label and predict how neural activity would change while preserving other observed labels and source-specific variability not explained by the labels. Her...

---

### 36. Estimation of the Cyclopean Eye from Binocular Free Visual Explorations

**Authors:** Maria F. Alcala-Durand, J. Camilo Puerta-Acevedo, Julián D. Arias-Londoño, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32564v1)

**Summary:** Binocular video-oculography records separate signals for each eye, yet human visual processing and oculomotor control operate relative to a single, virtual cyclopean eye. This study addresses the estimation of the cyclopean eye during binocular free visual exploration, a target-free paradigm widely used for the screening of neurological disorders. Using eye-tracking data collected at 1 kHz from 113 participants across three cohorts (patients with Parkinson's Disease, age-matched healthy controls...

---

### 37. From Heterogeneity to Function: Enhanced Modular Dynamic Range in Hierarchical Brain Networks

**Authors:** Filipe V. Torres, Mauro Copelli, Leonardo L. Gollo

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32328v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32328v1)

**Summary:** Hierarchical and modular organization defines brain architecture, yet how it supports flexible computation and functional specialization remains unclear. Although dynamic range is a hallmark of efficient information processing, its distribution across modules and hierarchical levels remains largely unexplored. Here, we show that hierarchical-modular networks naturally generate heterogeneous modular dynamics and firing rates, extending regimes of critical-like dynamics with enhanced intrinsic tim...

---

### 38. Phase-based Edge Coupling: Modeling Overlapping Functional Architectures and High-Order Edge-to-Edge Interactions in EEG Networks

**Authors:** Chengcheng Wu, Zichen Shi, Jiayang Xu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32286v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32286v1)

**Summary:** Network neuroscience has traditionally relied on node-centric approaches, which are inherently limited in capturing the brain's overlapping functional architectures and higher-order edge-to-edge interactions. The emerging edge-centric paradigm addresses this gap by shifting the analytical unit from nodes to edges. However, while edge-centric models have been established for DTI and fMRI, comparable EEG methodologies have yet to be developed. In this study, we proposed a Phase-based Edge-centric ...

---

### 39. Virtual Placebo: a scoping review of control conditions in randomized controlled trials of psychological immersive virtual reality interventions

**Authors:** Madis Vasser, Mary-Ann Kubre, Kadi Tulver, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32232v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32232v1)

**Summary:** Research on immersive virtual reality (IVR) as a therapeutic tool is growing rapidly, with randomized controlled trials (RCTs) now commonplace. Yet the control conditions in many of these studies that claim strong specific IVR effects vary from usual care to active immersive experiences, making it difficult to draw clinically meaningful conclusions. We conducted a scoping review of recent literature on psychological IVR interventions to assess the main forms of control conditions used and their ...

---

### 40. A Mathematical Theory of the Jacobian Lens

**Authors:** Mitchell Ostrow, Daoyuan Qian, Toni Liu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31955v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31955v1)

**Summary:** Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026). This method identified linear directions in the hidden states of frontier language models that had properties reminiscent of working memory-like representations. However, it is unclear what mechanistic properties of such features make them detectable to the J-lens. To this end, we introduce a mathematical theory of the J-lens, and show that it preferentially identifies coher...

---

### 41. Dynamics of random recurrent neural networks: colored noise and sublinear activations

**Authors:** German Mato, Facundo Rigatuso, Gonzalo Torroba

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31575v1)

**Summary:** We study the dynamics of recurrent neural networks with random couplings, sublinear odd activation functions, and temporally correlated noise. Using large N methods, we determine stationary correlations and distinguish the loss of local linear stability from the onset of chaos, characterized by a positive largest Lyapunov exponent. These thresholds delimit an intermediate regime in which local instability coexists with asymptotic stability under a common noise history. Their separation depends o...

---

### 42. Music Between Two Minds: Individual Signatures, Shared States, and the Emergence of Creative Interaction

**Authors:** Tatsuya Daikoku, Risa Kobayashi, Rina Tabuchi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31131v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31131v1)

**Summary:** Some of the most valued forms of human creativity arise between people-in conversation, collaboration, and improvised music-yet how two minds jointly regulate the flow of novelty in real time remains unknown. Here we examined the information dynamics of interpersonal improvisation using 986 professional jazz improvisations. Pitch-based fluctuations of uncertainty and surprise behaved as signatures of individual identity: the two partners differed within 90% of takes, performers were identifiable...

---

### 43. Simulated transcranial ultrasound of human language cortex: verifying heard speech needs far less data and signal than decoding it

**Authors:** Omer Shalev

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.33093v1) | 📄 [PDF](https://arxiv.org/pdf/2610.33093v1)

**Summary:** Functional ultrasound could image cortical blood volume through the temporal bone, but the skull leaves a weak signal, and task-evoked cortical imaging through the intact adult skull has not yet been shown. We built a voxel-specific Monte Carlo link-budget simulation of a probe on the left temple and used it to degrade public fMRI of three people who heard 15 hours of stories. On the same anatomical voxels we trained a published state-of-the-art fMRI language decoder (Tang et al., 2023) and two ...

---

### 44. Gate-Based Feature Importance in Simulation-Based Inference for EEG: A Cautionary Tale

**Authors:** Shrivatsa Deshmukh, Sasha Brenner, Thomas R. Knösche, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30364v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30364v1)

**Summary:** Simulation-based inference (SBI) provides a powerful way to fit mechanistic models to data, but offers little insight into which information in the data shapes the inferred parameter values. It could therefore benefit from robust and inexpensive interpretability methods. Learned weighting mechanisms such as feature gates provide a potential route to low-cost interpretability, although their interpretation assumes that predictive training reveals which inputs drive performance. We examined this a...

---

### 45. The medium is the message: How neurometabolic entanglement generates conscious experience

**Authors:** Terrence W. Deacon, Miguel Garcia-Valdecasas, Michael Jacob

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30217v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30217v1)

**Summary:** Most neuroscientific accounts of consciousness assume that conscious experience is constituted by the information conveyed between neurons. The physical-chemical details of the metabolic and physiological processes that convey this information are correspondingly presumed to be relevant only insofar as they support the organization of information processes. We describe an alternative perspective that denies this presumed independence of the processing of neural information and the metabolic-phys...

---

### 46. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v2) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v2)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 47. Vagus nerve stimulation strengthens beta- and gamma-rate auditory steady-state responses in rat cortex

**Authors:** Shinichi Kumagai, Tomoyo Isoguchi Shiramatsu, Karin Oshima, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29042v1)

**Summary:** Background: Gamma entrainment using sensory stimulation (GENUS) is under study as a treatment for neurological disease, but cortical engagement is variable. Vagus nerve stimulation (VNS) modulates cortical state and sound-evoked beta-gamma activity, suggesting that it may strengthen responses to rhythmic sensory input. Objective: To determine whether VNS strengthens auditory steady-state responses across beta and gamma rates and whether the effect depends on cortical region and sensory drive. Me...

---

### 48. A Reverse-Gold Theorem: Positive-Data Identification by Substrate-Bounded Contrastive Learners

**Authors:** Rakesh Sengupta

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28747v2) | 📄 [PDF](https://arxiv.org/pdf/2610.28747v2)

**Summary:** Gold's theorem shows that no learner can identify an arbitrary language in a superfinite class from positive presentations alone. We prove a positive result of a different shape. Fix an innate \emph{recursive contrast operator} $R$ mapping any string to a finite set of structurally bounded perturbations of it, and a discriminative scorer of bounded capacity trained by InfoNCE-style contrastive estimation \citep{vandenoord2018,macollins2018} on self-generated perturbations. Under a faithfulness c...

---

### 49. What I Disbelieve: Quantifying Belief With Negative Ranking Functions

**Authors:** Hanbin Go, Britt Anderson

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28357v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28357v1)

**Summary:** A challenge in exploring the psychology of human uncertainty is its measurement and quantification. Prior work has focused almost exclusively on probability, while the formal theories developed in philosophy are rarely tested. We tested Wolfgang Spohn's ranking theory, a normative account in which belief is graded by ordinal ranks of disbelief that combine by minimization rather than addition, as a descriptive model of human belief. Across six experiments, participants assigned ranks of disbelie...

---

### 50. Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle

**Authors:** John E Pearson

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27235v2) | 📄 [PDF](https://arxiv.org/pdf/2610.27235v2)

**Summary:** Friston's free energy principle holds that a system separated from its environment by a Markov blanket (a boundary whose states statistically screen its interior from its exterior) can be treated as performing approximate Bayesian inference, and that such blankets arise wherever coupling is short-range. We test this blanket condition in a concrete nonlinear pattern-forming system: self-replicating spots in a reaction-diffusion model that persist, compete, reproduce, and die. Directed boundary ex...

---

## stat.ML

**50 papers**

### 1. Instance-dependent sequential limits as an exact information ledger

**Authors:** Akshay Balsubramani

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42133v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42133v1)

**Summary:** Instance-dependent limits for bandit regret, sequential tests, best-arm identification and Markov decision processes are proved by one chain. It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations. Only the first step is an identity. This work writes the chain as an exact ledger. By the chain rule, data processing loses exactly a conditional d...

---

### 2. Gradient Descent on Two ReLU Neurons: Global Landscape and Bifurcation Dynamics

**Authors:** Binghua Li, Mengzhe Li, Denny Wu, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42118v1)

**Summary:** Understanding how gradient descent learns features remains a central challenge in neural network theory. We study this question in a minimal multi-index setting that already exhibits rich multi-phase gradient dynamics: a well-specified two-neuron ReLU teacher-student model under isotropic Gaussian inputs, trained by population gradient flow from small initialization. We show that the dynamics are organized by two directions: the "easy" bisector direction, which carries the leading signal, and th...

---

### 3. Regret-Optimal Wasserstein-Robust Linear Regression

**Authors:** Sloan Nietert, Daniel Kuhn

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42109v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42109v1)

**Summary:** Distributionally robust optimization (DRO) minimizes worst-case risk under distributional uncertainty, but its decisions can be suboptimal in terms of their excess risk, or regret. We study this gap for multivariate least-squares regression, assuming that the observed source law and unknown target law differ by an adversarial 2-Wasserstein perturbation of size $\varepsilon$. We first identify the asymptotic complexity of robust decision-making in the $\varepsilon \to 0$ limit, characterized by a...

---

### 4. CausalWAM: Learning the Causes of Actions in World Action Models

**Authors:** Juntao Cheng, Jinzhou Tang, Fan Feng, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42096v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42096v1)

**Summary:** World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant latent variables), as the model could just as well learn to imitate in this way wh...

---

### 5. Cost-Aware Stopping for Freeze-Thaw Bayesian Optimization: When Does One-Step Lookahead Suffice?

**Authors:** Long Vu, Jongseong Brad Choi, Binoy Ravindran, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42085v1)

**Summary:** Freeze-thaw Bayesian optimization (BO) evaluates candidates in resumable increments but usually stops at a budget or convergence test. We maximize a budget-free utility, the best observed score minus a cost per increment, with a one-step lookahead: advance the candidate with the largest expected improvement (EI) under a fixed surrogate, and stop once no EI exceeds the cost. This rule, EI stopping, never falls below stopping immediately in expected utility, yet it can stop too early. We construct...

---

### 6. Near-Optimal Second-Order Convex Finite-Sum Optimization under Individual Smoothness

**Authors:** Xinliang Zhang, Lesi Chen, Zonghan Li, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42040v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42040v1)

**Summary:** We study the stochastic second-order oracle complexity of solving smooth convex finite-sum optimization with $n$ components. Very recently, Tsedenov \& Kovalev (2026) showed that the minimax optimal complexity under averaged smoothness and convexity is $\tildeΘ(n + n^{6/7} ε^{-2/7})$ by establishing nearly matching upper and lower bounds. In this paper, we show that individual smoothness and convexity provably enable further acceleration, where the lower complexity bound is $Ω(n+ n^{5/7} ε^{-2/7...

---

### 7. On Statistical-Computational Gaps in Graph Combinatorial Testing Problems

**Authors:** Ikjun Choi, Pratik Patil, Alessandro Rinaldo

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41995v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41995v1)

**Summary:** We study high-dimensional graph combinatorial hypothesis testing problems in which a signal is supported on the edge set of an unknown subgraph drawn from a class invariant under vertex relabeling. For Gaussian observations, we characterize sharp statistical and computational thresholds (at polynomial order) for the signal magnitude required for strong detection across various combinatorial graph alternatives. Our analysis is based on bounding the second moments of the full and low-degree likeli...

---

### 8. WASABI: Wasserstein Sampling via Bridge Interpolants

**Authors:** Sebastian Salazar, Dilum Fernando, Michal Kucer, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41958v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41958v1)

**Summary:** Sampling from Boltzmann distributions is a fundamental problem in physics, chemistry, and biology. We introduce WAsserstein SAmpling via Bridge Interpolants (WASABI), a method that trains a diffusion model to generate samples from a target Boltzmann distribution given access only to the energy function. WASABI minimizes the KL divergence between the distribution generated by its diffusion model and the Boltzmann target using Wasserstein gradient flows. This approach builds on a principle underly...

---

### 9. Chronos-2: A foundation model for multivariate time series forecasting

**Authors:** Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41956v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41956v1)

**Summary:** Accurate forecasting with uncertainty quantification is critical in a variety of scientific applications ranging from epidemiology and economics to energy systems and earth sciences. Yet most forecasting models still need to be developed and trained separately for each domain-specific dataset. Time series foundation models (TSFMs) aim to remove this limitation and enable the application of the same model across domains through large-scale pretraining. However, most existing TSFMs treat each time...

---

### 10. Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective

**Authors:** Yuxin Chen, Yuejie Chi, Jianqing Fan, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41903v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41903v1)

**Summary:** Reinforcement learning (RL) embodies a foundational paradigm for sequential decision-making in the face of uncertainty. The rapid growth of model complexity in emerging applications has significantly amplified the challenges of achieving data-efficient RL, particularly in sample-starved scenarios where data collection may be costly, time-consuming, or even high-stakes. Consequently, understanding and improving the data efficiency of RL algorithms has become a central problem of both fundamental ...

---

### 11. Bethe Hessian Recovery through the Kesten-Stigum Regime

**Authors:** Dingding Dong, Theo McKenzie

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41802v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41802v1)

**Summary:** We show that outlier eigenvectors of the Bethe Hessian achieve weak recovery in the stochastic block model down to the Kesten-Stigum threshold, for every fixed common expected degree $d>1$. This extends previous recovery guarantees, which required $d$ to be sufficiently large. This threshold is information-theoretically optimal for the symmetric two-community model and is conjectured to mark the limit of efficient recovery in broader symmetric models. Our result matches the recovery guarantees o...

---

### 12. PDE-Residual-Informed Kriging

**Authors:** Yu Tan, Shichang Du, Yongxiang Li

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41590v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41590v1)

**Summary:** Physics-informed Gaussian process (GP) methods provide a probabilistic framework for PDE solving. Existing approaches incorporate PDE information in different ways: pointwise conditioning uses the governing equation only at finitely many selected locations, globally constrained GPs restrict the admissible functions to satisfy the PDE exactly, and residual-penalized methods control the PDE mismatch over the whole domain through an additional penalty weight. What is still missing is a GP formulati...

---

### 13. Reliability-Weighted Direct Preference Optimization: Penalized Weights for Robust Preference Learning

**Authors:** Bin Luo, Param Venkat Vivek Kesireddy, Anil Vallepu

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41588v1)

**Summary:** Direct Preference Optimization (DPO) treats every reported comparison as correct, yet preference data contain   reversed, tied or otherwise noisy comparisons. RW-DPO gives each comparison an unknown reliability weight   $w_i\in[0,1]$ that enters the likelihood linearly -- DPO is $w\equiv1$, a reversed comparison $w_i=0$ -- and estimates   the weights jointly with the policy under a minimax-concave penalty on $-\log w_i$. The penalty keeps every   comparison the model agrees with at exactly $w_i=...

---

### 14. Conditional Neural SDEs for Financial Time-Series Generation

**Authors:** Sina Molavipour, Alireza M. Javid, Björn Löfdahl, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41405v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41405v1)

**Summary:** Conditional generation of time-series paths is a central problem in probabilistic modeling, where the goal is to simulate future trajectories that are both realistic and responsive to external context. It has direct applications in finance and economics. Neural stochastic differential equations provide a natural framework for this task by combining continuous-time stochastic dynamics with learnable drift and diffusion functions. However, directly modeling the target state can be unstable in cond...

---

### 15. Coarse-Graining Optimal Transport for Rollout-Free Post-Training of Flow Matching

**Authors:** Soon Hoe Lim, Aditi Gupta, Michael W. Mahoney, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41269v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41269v1)

**Summary:** Flow matching depends critically on the coupling used to pair source and target samples. Optimal transport (OT) couplings can reduce velocity conflict and straighten trajectories; but, in practice, challenges remain: the source comes from a continuous distribution, only a finite number of target samples data are accessible, and the neural network has finite capacity. For these reasons, making the coupling more OT-like may not consistently improve sampling quality, in particular in the low number...

---

### 16. Instrumental Transfer Learning for Solution Operators

**Authors:** Tongyu Li, Zhuoyuan Li, Ruoxu Tan

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41262v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41262v1)

**Summary:** Data-driven learning for the solution operator of a differential equation has broad scientific importance, but observations from a target system are often scarce and costly to collect. Related source systems may provide abundant observations under similar physical conditions, whereas even small changes in the governing equation can induce complex changes in the solution operator, making naive data pooling ineffective. We propose a structured transfer learning method that accounts for unknown spa...

---

### 17. Stochastic Mirror Descent under Dependent Observations

**Authors:** Gersende Fort, Anatoli Juditsky, Jiaming Liang

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41251v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41251v1)

**Summary:** We study the non-asymptotic convergence of Stochastic Mirror Descent (SMD) algorithm when the noisy first-order oracle is driven by dependent observations. Departing from the classical i.i.d. assumption underlying most existing guarantees, we introduce a flexible ``forgetting" condition that accommodates geometrically or polynomially dependent sequences. Under this condition we derive explicit finite-sample accuracy bounds for the averaged SMD iterates, recovering the classical $O(1/T)$ and $O(1...

---

### 18. A Unified Framework for Probability Estimation of Data-Dependent Events

**Authors:** Vitaly Feldman, Satyen Kale, Vinod Raman, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41244v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41244v1)

**Summary:** We study the general problem of estimating $D(\dde(S))$, the probability that an unknown distribution $D$ assigns to an event determined by a sample $S$ of $n$ i.i.d.\ draws from $D$ through a known mapping $\dde$. The estimation algorithm knows $\dde$ and $S$ but does not have access to any additional samples from $D$. This formulation captures classical missing mass, the data-dependent targets of adaptive data analysis and post-selection inference, and the test error of a data-trained predicto...

---

### 19. Adaptive Uncertainty Quantification on Simplicial Complexes with Conformalized Simplicial Neural Networks

**Authors:** Lekun Wang, Jaidev Goel, Yulia R. Gel, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41166v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41166v1)

**Summary:** Simplicial neural networks (SNNs) are powerful tools for prediction tasks on higher-order relational datasets stored on simplicial complexes (SCs), a higher-order generalization of graphs. However, SNNs usually lack rigorous uncertainty quantification (UQ), limiting their usefulness in high-stakes scenarios. We propose conformalized SNN (CF-SNN), a framework that, given a simplicial-complex entity with m prediction targets, generates prediction sets for all m targets simultaneously. Under mild a...

---

### 20. MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation

**Authors:** Aryan Das, Vinay Kumar Verma, Aakansha Mishra

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41104v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41104v1)

**Summary:** Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates. Muon nevertheless stores a separate momentum buffer, increasing persistent training memory. We propose Muon with Reused Teacher (Muon-RT), which reuses the teacher-student displacement to eliminate momentum buffers for hidden weight matrices. We show that this displacement encodes an exponentially weighted history of applied updates and smooths tempora...

---

### 21. Where, When, and How Many Bits? Scaling Laws for SGD with Stochastic Rounding

**Authors:** Zhichao Wang, Michael W. Mahoney

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.41074v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41074v1)

**Summary:** Low-precision training reduces computation but introduces additional rounding error. We theoretically study how stochastic rounding (SR) affects prediction risk as model size, training time, and precision change. We consider a two-layer linear network with a fixed random first layer, trained by mini-batch SGD on fresh Gaussian data with power-law spectra. At each SGD step, the features used in forward and backward computations are rounded independently. We prove matched upper and lower bounds on...

---

### 22. Omniprediction for All Mixable Proper Losses and Beyond

**Authors:** Junyan Liu, Haipeng Luo, Lillian J. Ratliff

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.41023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41023v1)

**Summary:** Omniprediction concerns the task of making predictions that are simultaneously accurate with respect to different losses. Earlier results by [CV09] show that in an online learning setting, $O(\log(|\mathcal{F}||\mathcal{L}|))$ regret is achievable simultaneously against every predictor in a finite predictor class $\mathcal{F}$ and for every loss in a finite class $\mathcal{L}$ of mixable proper losses, while recent advances [OKK25, FP26] show that $\widetilde{O}(\sqrt{T\log(|\mathcal{F}||\mathca...

---

### 23. Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning

**Authors:** Shashank Gupta, Pilhwa Lee

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.41022v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41022v1)

**Summary:** Latent world models allow reinforcement learning agents to learn policies from imagined trajectories, yet determining the optimal depth of model reliance remains a fundamental challenge. Fixed imagination horizons apply uniform prediction depths regardless of trajectory reliability, exposing target values to compounding model error or over-relying on critic approximations. We introduce density-guided bootstrap boundaries, a trajectory-dependent mechanism that adapts the depth of imagined returns...

---

### 24. Robust-by-Design Distributional Learning from Contaminated Samples

**Authors:** Nevena Gligić, Arya Farahi

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40884v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40884v1)

**Summary:** Modern data analysis pipelines increasingly rely on large datasets assembled through retrieval, scraping, automated filtering, and post-hoc curation, where the observed sample is often a contaminated mixture rather than the target population. Standard distributional objectives either ignore contamination and converge to the wrong target, or retain only a small trusted subset and discard most of the data. We study supervised and unsupervised learning when a clean reference sample is compared with...

---

### 25. Near-Optimal First-Order Regret for Bandits with Feedback Graphs

**Authors:** Mengxiao Zhang, Yuheng Zhang, Haipeng Luo, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40861v1)

**Summary:** We study first-order regret guarantees for adversarial bandits with a fixed, known directed feedback graph. For strongly observable graphs, [ACBDK15] establishes a minimax regret of $\widetildeΘ(\sqrt{αT})$, where $α$ denotes the independence number of the graph and $T$ denotes the horizon. On the other hand, the best existing first-order bound scales as $\widetilde{O}(\sqrt{(κ+1) L^\star})$ [LLZ20], where $κ$ denotes the clique partition number, satisfying $κ+1\geqα$, and $L^\star$ denotes the ...

---

### 26. An ODE-based Sampler for Discrete Diffusion Models

**Authors:** Samson Gourevitch, Yazid Janati, Eric Moulines, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40618v1)

**Summary:** The marginals of a continuous diffusion model can be reproduced by a deterministic ordinary differential equation (ODE), known as the probability flow ODE, which provides a foundation for accelerated sampling and consistency distillation. In this paper we address the question whether an analogous formulation exists for discrete diffusion models and answer it affirmatively by introducing exponential residual flows (ERFs). Our framework augments the discrete state with a continuous residual variab...

---

### 27. Self-regularization and structural adaptation of NPMLE for Gaussian mixture models in all dimensions

**Authors:** Yanjun Han, Yandi Shen, Yihong Wu

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40566v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40566v1)

**Summary:** We establish structural properties of the nonparametric maximum likelihood estimator (NPMLE) for $d$-dimensional Gaussian mixtures whose means lie in a hypercube. We show that, with high probability, the NPMLE based on $n$ independent observations self-regularizes by fitting a mixture model with $O((\frac{\log n}{\log\log n})^d)$ components, achieving the optimal model complexity without explicit model selection. Furthermore, the NPMLE exhibits a structural adaptation property: For data drawn fr...

---

### 28. Numerical Integration on Bounded Domains via Learned Reflected Diffusions

**Authors:** Kirill Korolev, Artur Goldman, Timofei Gritsaev, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40499v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40499v1)

**Summary:** We study high-dimensional integration on bounded convex domains. Given a non-negative integrand $r$, the goal is to estimate $Z=\int_{D}r(x)\,\mathrm dx$ on $D\subset\mathbb R^d$. Standard Quasi-Monte Carlo does not adapt its evaluation points to the integrand, while effective importance sampling requires a proposal that captures its concentration. Learned diffusion samplers can supply such a proposal, but existing methods are formulated on $\mathbb R^d$ and do not respect the domain constraint ...

---

### 29. Rural Readiness: Domain Generalization with Adversarially Chosen Domains

**Authors:** Cynthia Dwork, Andisheh Ghasemi, Lunjia Hu

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40468v1)

**Summary:** Predictive models trained at well-resourced data-rich institutions often fail when deployed in new populations. Motivated by the goal of building clinical diagnosis and decision-making algorithms for data-scarce rural populations using the general knowledge learned from data-rich hospitals, we formulate the fundamental question of \emph{domain generalization with adversarially chosen domains}, which asks a learner to perform on any unseen target domain nearly as well as the worst hypothesis cons...

---

### 30. Finite-Sample LTI System Identification from a Misspecified Finite Model Set

**Authors:** Nicolas Chatzikiriakos, Andrea Iannelli

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40387v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40387v1)

**Summary:** We consider the problem of finite-sample identification of an unknown LTI system from a finite hypothesis class. In contrast to existing results that assume the hypothesis class contains the true system, we consider the misspecified setting, where the true system does not belong to the hypothesis class. We first characterize the resulting estimation target and its dependence on the data-generation scheme. We then establish a finite-sample lower bound on the failure probability that any identific...

---

### 31. Optimal Neural Estimation for High-Dimensional Nonparametric Regression under Multisource Covariate Shift

**Authors:** Chenghao Xu, Haotian Xu, Shivam Kumar, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40331v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40331v1)

**Summary:** We study high-dimensional nonparametric regression under multisource covariate shift, where $\mathrm J$ sources of training data share a common regression function but differ in their covariate distributions, sample sizes, and noise variances. Our goal is to combine these sources to estimate the regression function accurately under a target covariate distribution. We propose an oracle weighted neural estimator and establish its minimax optimality up to logarithmic factors through matching upper ...

---

### 32. Statistical Analysis of Synthetic Data with Verification: A Linear Regression Framework

**Authors:** Heejune Sheen, Harrison H. Zhou

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40254v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40254v1)

**Summary:** Synthetic data are widely used for training modern AI systems. However, their statistical understanding remains limited. It is well recognized in statistics that repeated self-training on synthetic data can amplify errors inherited from pre-trained models, leading to model collapse. Verification plays a crucial role in selecting high-quality synthetic data to help prevent model collapse and improve model performance. We study verified self-training in a linear regression framework, where a pre-t...

---

### 33. Conformal Annotation with Randomized Expert Review: Application to Online Cell-Type Labeling

**Authors:** Xuhe Zhang, Zhi Huang, Ying Jin

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40252v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40252v1)

**Summary:** Artificial intelligence (AI) models can accelerate cell-type annotation in digital pathology, but safely scaling their use requires determining, with error control, which model-generated labels can be accepted without expert review. This is challenging in evolving workflows because cell morphology and type composition may change across tissue regions and slides, making one-time calibration unreliable. We propose Conformal Annotation with Randomized Expert review under Distribution shift (CARED),...

---

### 34. Certified Behavioral Retention for Continual Adaptation with Held-Out Anchors

**Authors:** Ahanaf Hasan Ariq, Abrar Shahid

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40740v1)

**Summary:** Continual adaptation requires deciding not only how to update a model, but whether to commit an update without exceeding a declared budget for changes to protected behavior. We introduce Certified Anchor-Based Adaptation (CABA), a candidate-agnostic post-update gate that reserves historical observations from candidate optimization, compares old and candidate policies on frozen representations, and selects the largest tested interpolation coefficient whose worst-anchor forward KL divergence remai...

---

### 35. Understanding axial attention in TSFMs through single location regression

**Authors:** Andrei-Tiberiu Pantea, Aymeric Dieuleveut

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40188v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40188v1)

**Summary:** Recent advances in Time Series Foundation Models (TSFMs) increasingly rely on axial attention mechanisms, but despite their empirical success, the theoretical properties of axial attention remain largely unexplored. To bridge this gap, we extend the Single Location Regression framework introduced in Marion et al. [2025] to 2D structured data, in order to study sparse information settings where a target depends on a small number of tokens. We formulate an analytically tractable axial attention-ty...

---

### 36. Hidden Disparities in Ranking: Category-Aware Fairness via Distributional Stability

**Authors:** Gayane Taturyan, Charlotte Laclau, Stephan Clémençon

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40182v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40182v1)

**Summary:** We study the problem of fair ranking in recommender systems. We provide a formal probabilistic framework in which ranking policies are distributions over permutations, and the utility of a user is the exposure given to the items they interact with, relative to that of an ideal ranking. We consider utility parity across user groups, as well as its category-aware refinement, conditional utility parity, which requires parity within each category of items. Following a recent view of fairness as dist...

---

### 37. Closing the Log Gap: Minimax-Optimal Regret for Episodic RL

**Authors:** Guy Zamir, Victor Boone, Matthew Zurek, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40165v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40165v1)

**Summary:** In this paper, we study the regret minimization problem in episodic tabular MDPs. Our algorithm achieves the first expected regret bound scaling as $\sqrt{H^3 S A K}$ for sufficiently large $K$, where $H$ is the episode length, $K$ is the number of episodes, and $S$ and $A$ are the numbers of states and actions, respectively. Our method is the first to match the minimax lower bound \emph{without extra polylog factors}. We introduce a variant of UCBVI which does not maintain strictly optimistic e...

---

### 38. Fisher Contrastive Learning to Mitigate Feature Suppression: A Case Study in Acute Promyelocytic Leukemia Diagnosis

**Authors:** Shushan Wu, Yongkai Chen, Xilin Gong, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40162v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40162v1)

**Summary:** Self-supervised contrastive learning (SSCL) learns representations by contrasting augmented views of the same sample, but it can exhibit feature suppression, where dominant or easy-to-learn factors suppress other class-relevant signals, degrading the performance of representations, particularly in high-dimensional data with heterogeneous features. We introduce Fisher Contrastive Learning (FCL), which uses a regularized Fisher trace criterion to address feature suppression. FCL learns embeddings ...

---

### 39. Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation

**Authors:** Raphael Kim, Michele Santacatterina, Ramin Zabih, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40056v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40056v1)

**Summary:** Reinforcement learning (RL) is increasingly used to train robust, adaptable systems across healthcare, e-commerce, and robotics. In these settings, legal, ethical, or logistical concerns may preclude certain key variables that drive decisions from being collected during deployment time. This gives rise to a setting known as runtime confounding: the logged data hold full observability, but deployment time lacks knowledge of certain variables, known as runtime confounders. Unlike single timepoint ...

---

### 40. Probabilistic Meshless Methods on Manifolds

**Authors:** Federico Pavesi, Noémie Jaquier, Antonio Candelieri

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39855v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39855v1)

**Summary:** Probabilistic meshless methods solve partial differential equations (PDEs) by placing a Gaussian process prior on the solution and conditioning it on the PDE at a finite set of collocation nodes. The posterior provides both an approximation of the solution and a Bayesian quantification of its error. While these methods are well established on Euclidean domains, their extension to manifolds lacks, to our knowledge, any convergence analysis. We extend them to compact manifolds and study their conv...

---

### 41. Deep Reinforcement Learning for Blind Passive Beamforming in RIS-Assisted MIMO Systems

**Authors:** Oumaïma Bounhar, Thomas Chêne, Ghaya Rekaya-Ben Othman, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39827v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39827v1)

**Summary:** Reconfigurable Intelligent Surfaces (RIS) are a promising solution for improving millimeter-wave (mmWave) communications by controlling signal propagation. Yet, selecting the optimal RIS configuration remains challenging due to the high-dimensional search space and signaling overhead. We propose a Deep Reinforcement Learning (DRL) framework for blind passive beamforming, where a Deep Q-Learning (DQL) agent learns an adaptive policy to select near-optimal RIS configurations while sounding only fe...

---

### 42. Bayes-Consistent Losses for Adaptive Inference in Classification

**Authors:** Shirley Xiaoqi Liu, Florence Regol, Antonios Valkanas, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39709v1)

**Summary:** Adaptive inference systems balance accuracy and inference cost by routing inputs to models with varying capabilities. Although jointly training models and routers is empirically more sample-efficient than training them separately, principled losses for joint training remain underexplored. We address this gap in a classification setting by proposing cost-sensitive hinge losses for jointly training classifiers with single-stage or cascade routers. Single-stage routers directly select a model per i...

---

### 43. Formalizing the Intrinsic Dimension of Objective Landscapes by a Generalized Notion of Co-dimension

**Authors:** Ernesto Araya, Gitta Kutyniok, Weilin Li, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39674v1)

**Summary:** In this work, we formalize the concept of intrinsic dimension of objective landscapes introduced in Li et al. (2018), which measures the structural complexity of learning problems by training along randomly generated subspaces. We define the intrinsic dimension of a set $Θ\subset\mathbb{R}^p$ as the minimal dimension $d_{\mathrm{int}}(Θ)$ such that a random plane of dimension $d_{\mathrm{int}}(Θ)$ in $\mathbb{R}^p$ intersects $Θ$ with probability one. We show that it is a generalized notion of c...

---

### 44. Emergence of the transformer architecture as the score of entropic laws of random measures

**Authors:** Giacomo Greco

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39614v1)

**Summary:** We show that the transformer architecture emerges as the score of last-token laws in a natural statistical model of language, where sentences are empirical measures of tokens, a language is a law on $P(S^d)$, and our prior belief is that sentences carry no structure at all. By the maximum-entropy principle, we select the law closest to this prior in relative entropy among those reproducing an observed sentence-level statistic. We discuss the relevance of the statistic in the posterior interactio...

---

### 45. TabCUQ: Context-Uncertainty Quantification for Tabular Foundation Models

**Authors:** Yuebei Shi, Molei Liu, Zijian Guo

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39558v1)

**Summary:** Tabular foundation models use in-context learning to estimate conditional expected outcomes and average treatment effects for specific groups of individuals. Using these estimates to guide scientific decisions requires reliable uncertainty quantification. The challenge is to account simultaneously for two sources of uncertainty: limited-context bias and context variation arising from the small labeled sample supplied at inference. Predictive spread does not directly quantify both sources of unce...

---

### 46. Non-Asymptotic Confidence Regions for Separable Nonlinear Models

**Authors:** Szabolcs Szentpéteri, Péter Kovács, Balázs Csanád Csáji

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39549v1)

**Summary:** This paper studies robust uncertainty quantification for separable nonlinear least squares (SNLLS) problems. We propose two identification methods, (i) Residual-Perturbed Gradient (RPG) and (ii) Global-Fit-Gap (GFG), to construct joint distribution-free confidence regions for both the linear and nonlinear parameters. By exploiting assumed group invariance of the noise (such as symmetry or exchangeability), we apply random perturbations (such as sign-changes or permutations) to build the regions ...

---

### 47. The Cost of Working Memory in Streaming Mean Estimation

**Authors:** Zeyu Wu, Zihao Wang, Minghua Deng

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39540v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39540v1)

**Summary:** A streaming estimator must compute from the evidence that fits in memory. We determine when storing an accurate mean is easier than computing it. For Gaussian mean estimation over the Euclidean unit ball in $\mathbb{R}^d$, we establish the minimax rate under squared error with $K$ persistent states, a known horizon, and a public time index: $\min\{1, K^{-2/d}+\frac{d}{n} (1+\frac{\log(ed)}{1+(\log K)/d})\}$. Unrestricted computation followed by $K$-level encoding has rate $\min\{1,d/n+K^{-2/d}\}...

---

### 48. Conic-Lifting for Learning-rate-free Convex Optimization

**Authors:** Julien Grand-Clément, Joon Kwon, Francesco Orabona

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39531v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39531v1)

**Summary:** A central topic in online and stochastic optimization is to design algorithms that do not require tuning of hyperparameters. Successful strategies in online learning include AdaGrad-style learning rates, Conic Blackwell algorithms, and parameter-free algorithms. However, these classes require different, often difficult, analyses. We develop a unifying family of Online Convex Optimization (OCO) algorithms that require no user-tuned learning rate on convex domains that may be unbounded. The constr...

---

### 49. INLA for Adaptive UAV Sampling of Radio Environment Maps in IoT Networks: Prior Width Governs Accuracy and Calibration

**Authors:** Changhao He, Kaichuang Yang, Xiaojuan Zhang

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40723v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40723v1)

**Summary:** We study adaptive UAV sampling for radio environment map (REM) construction from non-Gaussian IoT observations. Integrated nested Laplace approximation(INLA) updates a Matérn GMRF posterior, with waypoints selected by entropy pre-screening and Sherman--Morrison lookahead over the reachable set. We show that the likelihood-induced Skew-Normal correction has a sextic entropy effect, explaining its limited influence on waypoint selection. Across 19 retained ray-traced windows,Random and lawnmower s...

---

### 50. Safe Multi-Objective Reinforcement Learning: Zero Constraint Violation and Primal-Averaging Convergence

**Authors:** Chenxi Li, Yao Shu, Siyang Gao, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39409v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39409v1)

**Summary:** Many applications of multi-objective reinforcement learning (MORL) require policies that balance conflicting objectives while satisfying safety constraints. We study safe MORL with zero constraint violation throughout learning, covering both cumulative and stepwise constraints. A key challenge is to explore sufficiently under unknown dynamics and constraint costs without violating the constraints. For a given preference over objectives, we develop an algorithm to learn a safe Pareto optimal poli...

---

