# arXiv Daily Digest - 2026-08-07

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Learning When to Trust via Selective Context Preference Optimization

**Authors:** Xian Sun, Wei Chow, Yingshuo Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06377v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06377v1)

**Summary:** Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-contex...

---

### 2. Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering

**Authors:** Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06366v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06366v1)

**Summary:** Electronic health record (EHR) feature engineering is a major bottleneck in clinical research and AI, accounting for 39-45% of data scientists' workload. This is especially pronounced in heart failure, which affects an estimated 6.7 million U.S. adults and requires integrating fragmented EHR data with disease-specific, guideline-based clinical reasoning. Existing rule-based and large language model (LLM)-based approaches offer only partial automation with limited maintainability and evidence tra...

---

### 3. Investigating Artificial Intelligence Digital Sovereignty in Mobile Shopping Apps: A Case Study of Nigeria

**Authors:** George Grispos, Sajda Qureshi

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06364v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06364v1)

**Summary:** The use of e-commerce mobile applications is expanding in Nigeria, creating both opportunities and risks, including fraud and reduced user control over digital technologies, raising concerns about digital sovereignty. This research examines how Artificial Intelligence (AI) in Nigerian mobile applications affects digital sovereignty, examined through platform transparency as a key indicator of user awareness and control. Using an interpretive approach, the research combines the forensic analysis ...

---

### 4. An Optimal Agnostic PAC Algorithm

**Authors:** Markus Engelund Mathiasen, Jian Qian, Nikita Zhivotovskiy

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06363v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06363v1)

**Summary:** Let $H\subseteq\{-1,+1\}^X$ be a class of finite VC dimension $d\ge1$. Writing $L$ for the binary risk and $L^*=\min_{h\in H}L(h)$, we construct a learner achieving the statistically optimal risk bound: from an i.i.d.\ sample of size $n$, for every $0<δ\le 1/2$, with probability at least $1-δ$, \[   L(\widehat h)   \le L^*+ 7\cdot10^8\left(   \sqrt{\frac{L^*(d+\log(1/δ))}{n}}   +\frac{d+\log(1/δ)}{n}   \right). \] This settles the sample complexity of agnostic PAC learning up to universal consta...

---

### 5. AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games

**Authors:** Boning Li, Yu Chen, Longbo Huang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06362v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06362v1)

**Summary:** Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact...

---

### 6. The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping

**Authors:** Sarvesh Baskar, Zikui Cai, Shayan Shabihi, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06361v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06361v1)

**Summary:** Real-world video benchmarks provide broad coverage, but their fixed clips entangle event count, rate, duration, and visual complexity, making failure modes hard to isolate. While existing programmatic benchmarks offer better control, they score only the final answer rather than auditing reported events against executable ground truth. To bridge this gap, we introduce trace-grounded parametric profiling for event counting in three controlled video tasks: bouncing-ball wall contacts, visual blinks...

---

### 7. Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents

**Authors:** Praphul Chandra, Sujit Gujar, Ganesh Ghalme

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06353v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06353v1)

**Summary:** We give a formal mechanism design model for the continuous participatory governance of a deployed AI agent. The mechanism is built on the principle that governance should control an AI agent through resource allocation so as to make authorization self enforcing via compute budgets. The mechanism seeks to establish the Safe AI paradigm that compute is an effective governance lever. We situate our work as a compliance or commons overlay on a deployer. One governance period is an extensive form gam...

---

### 8. Challenges in Evaluating Explanation Methods for Static and Evolving Data

**Authors:** Jerzy Stefanowski

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06351v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06351v1)

**Summary:** This paper addresses the limitations of Explainable Artificial Intelligence (XAI) with respect to insufficient evaluation. They are illustrated through the DetoxAI image recognition system for bias detection and concept unlearning. Then, an example of a human-grounded evaluation of methods for explaining image classification is presented. The paper further explores methods for adapting explanations to evolving data streams with concept drift. Experiences with adapting counterfactuals for this pr...

---

### 9. TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories

**Authors:** Yunjia Qi, Zehua Yin, Xintong Shi, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06346v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06346v1)

**Summary:** LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and p...

---

### 10. Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data

**Authors:** Donna Hooshmand, Shubham Shahi, Cameron Barrie, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06331v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06331v1)

**Summary:** From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand. This is a knowledge-acquisition bottleneck that limits the scalability of analytic systems, keeps non-technical users dependent on experts, and is itself error-prone. We present TYTAN, a ...

---

### 11. Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents

**Authors:** Noam Koren, Roy Bar-Haim, Abigail Goldsteen

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06329v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06329v1)

**Summary:** Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations. We introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage, while providing actionable diagnostics of weaknesses. We validate the framework by demonstratin...

---

### 12. Does FLAIR super-resolution erase or hallucinate small white-matter lesions?

**Authors:** Zahra Khodakarami, Yue Li, Pulkit Khandelwal, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06311v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06311v1)

**Summary:** White matter hyperintensities (WMH), bright regions on Fluid-attenuated Inversion Recovery (FLAIR) scans are associated with cerebrovascular pathology and neurodegeneration. FLAIR is usually acquired with thick slices in clinical settings, giving it poor through-plane resolution. Super-resolution (SR) is a widely used method for recovering an isotropic volume from an anisotropic scan. Yet whether applying it prior to WMH segmentation preserves lesion content remains unknown: a model may erase sm...

---

### 13. Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations

**Authors:** Sagar Tamang, Ayush Vyas, Tabarakul Hazarika

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06305v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06305v1)

**Summary:** Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important class of documents -- financial statements, audit reports, regulatory returns -- this design is structurally unsound, and we make the argument measurable. On a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding spa...

---

### 14. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

**Authors:** Varun Ursekar, Apaar Shanker, Yash Maurya, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06301v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06301v1)

**Summary:** As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measu...

---

### 15. Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors

**Authors:** Arya Labroo, Mengjie Qian, Kate Knill

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06300v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06300v1)

**Summary:** Automatic speaking assessment systems are increasingly deployed in high-stakes settings to mark second language (L2) learners' speaking tests, making it critical to show that their scores depend on speaking proficiency rather than irrelevant speaker attributes such as first language (L1) or age. Transformer-based foundation models have improved the accuracy of these L2 speaking graders, but their black-box representations make fairness and interpretability analysis more difficult. Building on pr...

---

### 16. QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction

**Authors:** Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06294v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06294v1)

**Summary:** Cardiac arrest remains one of the most lethal conditions encountered in intensive care units. Despite the growing availability of electronic health record data, existing mortality prediction studies in this population largely depend on static summaries derived from early admission. Such approaches ignore the temporal progression of physiological deterioration and recovery that unfolds throughout a patient's ICU stay. To address this limitation, we introduce QuanTiMedAI, a quantum-agentic framewo...

---

### 17. BaKron: Efficient Quantization with Kronecker-Factored Hessians

**Authors:** Johann Birnick, Rayan Saab

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06291v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06291v1)

**Summary:** We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations. Two-sided Kronecker-factored Hessian approximations can additionally capture correlations across output coordinates, but applying GPTQ directly in the vectorized weight domain is computationally expensive. Building on the two-sided adaptive-rounding ...

---

### 18. The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images

**Authors:** Zhiheng Wang, Bo Peng, Lai Wei, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06270v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06270v1)

**Summary:** The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost. They may also repeatedly crop irrelevant regions and fail on questions that direct inference answers correctly. We ask whether the returned visual evidence causally affects the answer. To answer this question, we formulate visual tool-use as a c...

---

### 19. Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints

**Authors:** Omid Bazgir, Md Nasir, Jacob Hoffman, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06265v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06265v1)

**Summary:** Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.   We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility ...

---

### 20. Toward Deployable Bangla Sign Language Recognition with Expert-Validated Data and a Lightweight Attention-Based Model

**Authors:** Saad Ahmed, Md Khalid Syfullaha

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06252v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06252v1)

**Summary:** Deaf and hard-of-hearing people in Bangladesh communicate mainly through Bangla Sign Language (BdSL). Automatic BdSL recognition on personal devices could widen access to education and services. Existing systems use controlled-setting datasets without expert verification and heavyweight pretrained backbones unsuited to on-device use. We introduce RSBdSL38, 10,874 expert-validated images spanning all 38 BdSL hand signs, representing the 51 letters of the Bangla alphabet, recorded from real signer...

---

### 21. DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models

**Authors:** ZhiYan Hou, Xinyu Tang, Hongyan An, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06243v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06243v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models using automatically verifiable outcome signals, but these signals are typically sparse and at the sequence-level. On-policy self-distillation (OPSD) mitigates this sparsity by querying a privileged teacher at student-visited prefixes and providing dense token-level distributional supervision. Although this dense supervision alleviates signal sparsity, we find that standard OPSD stil...

---

### 22. PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation

**Authors:** Elad Yoshai, Natan T. Shaked

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06240v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06240v1)

**Summary:** Unpaired image-to-image translation must decide, per image, what to change and what to preserve without paired supervision. Many diffusion-based unpaired translators control preservation through a single global noise or guidance value applied across the image, which cannot separate content to keep from appearance to change. We present PRISM, a GAN-free flow-matching framework that replaces this global control with a learned per-feature gate. The gate's spatial prior is derived from each source f...

---

### 23. Depth-Guided Video Object Counting in Crowded Scenes

**Authors:** Yuanjing Xu, Xinyan Liu, Weidong Chen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06236v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06236v1)

**Summary:** Our primary objective is to advance video object counting in crowded scenes, aiming to robustly count all instances of a target category based on given text or visual prompts. Existing methods rely on RGB information, limiting their discriminative ability in crowded and occluded conditions. To address this, we propose a Depth-Guided Detector (DG-Det) along with a general post-processing pipeline. By integrating depth cues with multi-scale RGB-D cross-attention and explicit occlusion prediction, ...

---

### 24. From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks

**Authors:** Christo Kurisummoottil Thomas, Omar Hashash, Walid Saad

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06227v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06227v1)

**Summary:** Despite advances in artificial intelligence (AI) across multiple sectors, today's AI tools, including deep learning and generative AI, still fail when embedded into physical systems, such as robots and vehicles operating under real-world physical laws. This stems from their inability to maintain reliable world models for long-horizon planning under uncertainty and generalize to unseen scenarios. In this context, wireless networks, through pervasive sensing and communication, can orchestrate phys...

---

### 25. TS-RAG: Retrieval Augmented Generation for Time Series Forecasting

**Authors:** Yixiong Xiao, Congxi Xiao, Jingbo Zhou

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06223v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06223v1)

**Summary:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorporating relevant external information, retrieving similar time series sequences as references might also improve accuracy in time series forecasting tasks. However, most time series...

---

### 26. Continual Learning in Transition

**Authors:** Zhiyan Hou, Dan Zhang, Tao Feng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06216v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06216v1)

**Summary:** Classical continual learning (CL) has primarily focused on enabling models to update and retain knowledge through parameter-centric mechanisms, e.g., training strategies, architectural designs, and weight adaptation. However, emerging paradigms are reshaping the scope of CL beyond this traditional model adaptation view. For instance, on-policy learning broadens the space of update mechanisms; test-time training extends CL from the training phase to inference; and external harness components such...

---

### 27. What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)

**Authors:** Ro Encarnación, Tina Behzad, Emma Lurie, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06202v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06202v1)

**Summary:** Large language model (LLM) benchmark evaluations are routinely used to support claims about model safety, reliability, and deployment readiness. Yet most evaluations rely on a single access modality (model APIs), perform a single run per prompt, and report accuracy as the primary outcome metric, without accounting for conditions such as web search that may have effects on model behavior in deployment. We audit these assumptions for one of the most widely-used LLMs, comparing two modalities, Chat...

---

### 28. EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning

**Authors:** Zishan Xu, Zhiyuan Yao, Yuxin Chen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06197v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06197v1)

**Summary:** Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that replaces external environment interaction during training with world rehearsal. The policy alternates between acting and rehearsal: it first generates a tool call, then plays the role...

---

### 29. Comparative Approaches to Agent Retrieval over Large Skill Libraries

**Authors:** Indivara Kolluru, Nathan Sportsman

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06196v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06196v1)

**Summary:** Agents backed by large skill libraries must decide which skills to load and in what order. Loading the entire library into context is expensive and provides no structure for autonomous sequencing. We study two systems for this problem over a corpus of 690 skills: a hybrid ranker combining lexical and dense-embedding retrieval for sparse, on-demand loading, and a typed knowledge graph encoding workflow relations such as prerequisites, data flow, and ordering. On a set of 117 realistic, non-echoin...

---

### 30. MicroEvo: Knowledge-Guided LLM Sampling for Efficient Microarchitecture Design Space Exploration

**Authors:** Jia Xiong, Runkai Li, Chenxu Niu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06183v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06183v1)

**Summary:** Microarchitecture design space exploration suffers from expansive search spaces and expensive PPA evaluation, leaving only a small simulation budget for design decision-making. Existing methods perform blind search without considering microarchitectural dependencies and fail to learn from the iterative search effectively, leading to wasted evaluations and weak Pareto convergence. In this paper, we propose MicroEvo, a knowledge-guided framework that couples off-the-shelf LLMs with Monte Carlo Tre...

---

### 31. Schema-Guided Hierarchical Information Extraction and Semantic Evaluation Using Generative AI

**Authors:** Modhurita Mitra, Jan-Willem Versteeg, Maarten D. Schermer, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06167v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06167v1)

**Summary:** We present a schema-based framework for extracting complex, structured information from unstructured text documents using generative AI, followed by automated semantic evaluation of the extracted information against a gold standard. The schema, serving as an information model encoding domain knowledge, provides a unified, systematic, and consistent framework for extraction of hierarchical, nested information, with attributes of variable cardinality, and subsequent evaluation of the results. Info...

---

### 32. Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset

**Authors:** Eoin Cummins, Zhongyi Huang, Alexandre D'Hooge, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06165v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06165v1)

**Summary:** Existing audio-to-score (A2S) systems primarily focus on classical music, and the application to popular music remains underexplored. This paper first presents the new SheetSage-A2S Dataset, which includes 61 hours of audio with \texttt{**kern} score encodings for 9,468 clips originating from 6,066 unique songs, the first of its kind to facilitate A2S research for popular music. Additionally, we improve on existing A2S approaches by using data augmentation and MuQ, a pretrained feature-extractio...

---

### 33. iARCS: Iterative Agentic RL for Controllable 3D Scene Generation

**Authors:** Saugat Adhikari, Ashok Prasad Neupane, Pramish Paudel, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06161v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06161v1)

**Summary:** Synthetic 3D scene generation is increasingly used as a data source for computer vision and embodied AI, but existing generators often optimize perceptual realism without reliably satisfying task-critical functional constraints. This mismatch limits the usefulness of synthetic data for downstream training, where accessibility, traversability, and spatial rule compliance are often essential. We present iARCS, an iterative agentic reinforcement learning framework that adapts a pretrained scene gen...

---

### 34. Visual Grounding in Zero-Shot Vision-Language Control

**Authors:** J. de Curtò, Dayani Plasencia, Diego Sánchez, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06154v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06154v1)

**Summary:** Vision-language models (VLMs) are increasingly used as zero-shot controllers, but successful trajectories do not necessarily show that decisions are grounded in visual input: simulator dynamics and conservative action priors can produce favourable scores without meaningful perception. We investigate this with an input-ablation battery: blind-image controls, repeated identical inputs, lane-axis reflection, non-visual baselines, and pipeline-integrity checks. Across nine direct-action models, six ...

---

### 35. Learning Globally Reusable Skills for Coding Agents

**Authors:** Chen Yang, Jiashuo Tian, Ziqi Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06153v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06153v1)

**Summary:** Automated skill evolution enables Large Language Model (LLM) agents to continuously improve without expensive retraining. However, existing approaches typically treat skill evolution as a sequence of local updates, overlooking relationships among skills and often producing overfitted skill updates that fail to generalize across tasks. We propose GSE, a globalized skill evolution framework that jointly optimizes skill compatibility and skill generalization. To preserve consistency across the skil...

---

### 36. Reducing belief in conspiracy theories as they unfold using large language models

**Authors:** Thomas H. Costello, Nathaniel Rabb, Michael Nicholas Stagnaro, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06151v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06151v1)

**Summary:** The emergence of conspiracy theories in the wake of major events is a significant societal challenge. Here we test whether conversational dialogues with a large language model (LLM) can reduce belief in immediately unfolding conspiracies. In experiments conducted in the days following the July 2024 assassination attempt on Donald Trump and the September 2025 assassination of Charlie Kirk, U.S. adults (Experiment 1: N = 472; Experiment 2: N = 1035) holding conspiratorial views about the crisis ev...

---

### 37. CogVis: Must Open-Vocabulary Change Detection Perceive the Scene Anew for Every Query?

**Authors:** Zijie Wang, Chen Zhong, Wei He

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06150v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06150v1)

**Summary:** Earth-surface monitoring requires change detection models capable of recognizing arbitrary semantic categories. Open-Vocabulary Change Detection (OVCD) addresses this need. However, existing methods often entangle temporal perception, semantic discrimination, and region verification, causing unstable results and redundant computation. Inspired by human visual change perception, we propose CogVis, a cognitive memory-guided framework that reformulates OVCD as a perception-memory-verification parad...

---

### 38. PaDoc: Layout-Grounded Parallel Decoding for Document Parsing

**Authors:** Hao Yu, Jiabo Zhan, Kang Liu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06146v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06146v1)

**Summary:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at the cost of repeated visual prefills and fragmented page context. To retain full-page context while removing dependencies, we propose PaDoc, a layout-grounded parser that treats th...

---

### 39. FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows

**Authors:** Bo Deng, Kang Zhou, Lifan Guo, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06144v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06144v1)

**Summary:** Most agent benchmarks evaluate tasks independently and cannot measure whether experience from one task helps with later tasks. Existing self-evolution benchmarks do not jointly cover professional workflows, open-ended deliverables, and multi-aspect evaluation. We introduce FinEvo-Bench, a longitudinal benchmark with 120 real-case-grounded tasks, 20 business scenes across six financial domains. Institution-provided professional procedures define the required operations and constraints. Eligible i...

---

### 40. Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture

**Authors:** Leo Sambrook, Sampo Sovio

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06130v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06130v1)

**Summary:** AI agents performing cryptographic operations (signing Git commits, authenticating API calls, issuing certificates) currently store private keys in software-accessible locations: plaintext files, environment variables, or container memory. Any process with sufficient read privileges can extract the raw key material. A recent production incident demonstrated the practical severity: private keys were exfiltrated from a widely deployed framework via email injection in under five minutes. We aim to ...

---

### 41. Contextual Information Policy Optimization for Search Agents

**Authors:** Xingyu Guo, Wei Chen, Linlin Yang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06128v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06128v1)

**Summary:** Search agents extend large language models beyond static parametric memory by enabling them to acquire and use ex ternal evidence during multi-step reasoning. For knowledge intensive tasks involving complex or evolving information, their reliability depends not only on retrieving relevant ev idence but also on using it to guide subsequent reasoning. However, existing methods primarily reward final-answer cor rectness or intermediate progress, without directly assessing whether post-retrieval act...

---

### 42. Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts

**Authors:** Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06123v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06123v1)

**Summary:** Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically...

---

### 43. Is Self-Pretraining really useful to improve diagnosis in medical Time Series?

**Authors:** Omar Coser, Antonio Orvieto, Paolo Soda, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06122v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06122v1)

**Summary:** Inspired by recent evidence that transformer architectures benefit from Self-PreTraining (SPT) on long-context benchmarks, we investigate whether similar gains extend to multimodal, multivariate, and even simple univariate medical time series. Our objective is to assess the impact of SPT on the performance and scalability of transformer-based models across diverse medical applications, particularly under limited data conditions. We evaluate transformer architectures on three representative medic...

---

### 44. Mind the Gaps: Mixture-of-Minds for Human Simulation

**Authors:** Pranav Dahiya

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06115v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06115v1)

**Summary:** Predicting how a population will answer a new question is a long-standing goal. Statistical methods succeed at the level of the mass but falter at the level of the individual. Large language model simulators inherit this gap. They recover a population's central tendencies while flattening its heterogeneity, and they carry social biases and prompt brittleness that distort individual predictions. This paper introduces Anacreon, an audience simulation model that targets the individual level within ...

---

### 45. Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers

**Authors:** Haris Riaz, Hyungji Kim, Mihai Surdeanu

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06111v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06111v1)

**Summary:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraining and injects it across all three dominant PE families (absolute, relative, rotary), for both encoders and decoders, leaving self-attention and the rest of the architecture untouch...

---

### 46. From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems

**Authors:** Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06112v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06112v1)

**Summary:** Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research pr...

---

### 47. ECHO: A Locally-Deployable Agentic Health Assistant with Temporal Memory, Safety Guardrails, and Speech Assessment

**Authors:** Abdulkadir Külçe, Alihan Esen, Cağla Fikir, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06110v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06110v1)

**Summary:** This paper presents ECHO (Enhanced Care \& Health Observer), a locally-deployable conversational health assistant for long-term chronic care management. ECHO integrates three complementary software modules developed under shared supervision as a unified system. The core module is an agentic chatbot built on a ReAct loop orchestrated via LangGraph, equipped with 17 clinical tools and a temporal knowledge graph for persistent cross-session memory; it achieves a 94.9\% tool-execution pass rate acro...

---

### 48. Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied Financial Agents

**Authors:** Yuanhong Jiang, Jingjie Zou, Zhenghong Lin, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06108v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06108v1)

**Summary:** Investment competence is inherently personalized: the same market evidence can justify different actions for investors with different goals, horizons, portfolios, and risk boundaries. Yet financial LLMs are evaluated either by static question answering or by terminal profit and loss. The former omits agency; the latter cannot reveal whether a profitable action was grounded, profile-consistent, or merely lucky. We ask whether the community is using the wrong ruler for consequential agents.   We i...

---

### 49. Does Latent Context Help? A Controlled Evaluation of Inverse Reinforcement Learning in Arctic Shipping

**Authors:** Vaishnav Vaidheeswaran, Dilith Jayakody, Biruk Ambaw, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06105v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06105v1)

**Summary:** Artificial Intelligence (AI)-assisted navigation can help Arctic shipping adapt to rapidly changing sea-ice conditions, but reliable deployment requires reward models that are interpretable and robust to changing environments. Inverse reinforcement learning (IRL) provides a framework for recovering such rewards from vessel trajectories, while recent meta-IRL methods introduce latent context variables to capture behavioral heterogeneity. However, it remains unclear whether these latent representa...

---

### 50. Signal or Spurious Cue? A Randomized Audit of Survey-Country Metadata in LLM Social Inference

**Authors:** Yifan Lyu, Xinran Li, Jiaqi Qiao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06085v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06085v1)

**Summary:** Survey-country metadata can improve an LLM's forecast of an individual response when informative, yet the same cue may redirect the forecast when assigned at random. A within-record audit tests whether disclosing a random label's uniform, record-independent origin reduces its country-directed uptake, and whether verified survey country lowers held-out Brier loss. Independent population anchors and recorded human answers measure direction and consequence across five fixed API models, six countrie...

---

## cs.CL

**50 papers**

### 1. Learning When to Trust via Selective Context Preference Optimization

**Authors:** Xian Sun, Wei Chow, Yingshuo Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06377v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06377v1)

**Summary:** Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-contex...

---

### 2. The Bitter Lesson of Tool Calling

**Authors:** Ishan Patel, Sahil Sen, Elias Lumer, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06370v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06370v1)

**Summary:** Tool use transforms LLMs into agents that act beyond their training data, and for code-capable models, programmatic tool calling extends this further by replacing rigid JSON calls with scripts that chain and parallelize naturally. However, a systematic evaluation of tools as code on an established benchmark across current and prior model generations under real-world task conditions has not been conducted. In this work, we empirically compare programmatic tool calling (PTC) to native JSON tool ca...

---

### 3. AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games

**Authors:** Boning Li, Yu Chen, Longbo Huang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06362v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06362v1)

**Summary:** Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact...

---

### 4. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

**Authors:** Fanzhe Meng, Guoxin Chen, Jiale Zhao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06352v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06352v1)

**Summary:** Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a...

---

### 5. RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer

**Authors:** Xinye Wang, Junxiao Liu, Shujian Huang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06347v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06347v1)

**Summary:** Multilingual reasoning transfer is crucial for extending reasoning capabilities of large language models (LLMs) beyond high-resource languages. On-policy self-distillation (OPSD) and its variants have emerged as a promising paradigm, providing dense token-level supervision on student-generated rollouts, yet their objectives do not explicitly prioritize reasoning signals most critical to cross-lingual transfer. We characterize that target-language reasoning comprises the generation of both surfac...

---

### 6. Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents

**Authors:** Noam Koren, Roy Bar-Haim, Abigail Goldsteen

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06329v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06329v1)

**Summary:** Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations. We introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage, while providing actionable diagnostics of weaknesses. We validate the framework by demonstratin...

---

### 7. Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents

**Authors:** Tao Wang, Qihao Yang, Rongjiao Liang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06312v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06312v1)

**Summary:** Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, such as China GB/T standards, offer a representative testbed: they are lengthy, highly structured, and governed by explicit rules for scope, terminology, normative wording, and cross-section consistency. Existing benchmarks focus on domain knowledge and question answering, largely overlooking intrinsic...

---

### 8. RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction

**Authors:** Chenglong Wang, Ziming Zhu, Yifu Huo, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06310v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06310v1)

**Summary:** Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a...

---

### 9. Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations

**Authors:** Sagar Tamang, Ayush Vyas, Tabarakul Hazarika

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06305v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06305v1)

**Summary:** Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important class of documents -- financial statements, audit reports, regulatory returns -- this design is structurally unsound, and we make the argument measurable. On a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding spa...

---

### 10. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

**Authors:** Varun Ursekar, Apaar Shanker, Yash Maurya, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06301v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06301v1)

**Summary:** As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measu...

---

### 11. NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering

**Authors:** Jonas Gann, Michael Gertz

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06292v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06292v1)

**Summary:** Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence. Moreover, missing user-specific context is rarely detected systematically, often leading to incomplete or incorrect output.   We propose NeSy-RAG, a modular neuro-symbolic RAG framework...

---

### 12. Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents

**Authors:** Jiaming Wei, Zekun Wu, Adriano Koshiyama, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06171v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06171v1)

**Summary:** Web agents observe a browser through text, pixels, or both, and the choice is usually fixed once for all tasks. We measure six observation modes across eight site-model combinations (cells) on VisualWebArena and WebArena and ask what choosing per task would buy. The modes are complementary: each solves tasks the others miss, they fail in structurally different ways, and the best choice reverses between task sets. The obvious prize, an oracle that picks a winning mode for every task, looks large ...

---

### 13. Schema-Guided Hierarchical Information Extraction and Semantic Evaluation Using Generative AI

**Authors:** Modhurita Mitra, Jan-Willem Versteeg, Maarten D. Schermer, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06167v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06167v1)

**Summary:** We present a schema-based framework for extracting complex, structured information from unstructured text documents using generative AI, followed by automated semantic evaluation of the extracted information against a gold standard. The schema, serving as an information model encoding domain knowledge, provides a unified, systematic, and consistent framework for extraction of hierarchical, nested information, with attributes of variable cardinality, and subsequent evaluation of the results. Info...

---

### 14. Decolonizing Linguistic Policies in Automated Speech Recognition: A Framework for Cross-Culturally Competent Speech AI

**Authors:** Jay L. Cunningham, Mark Atta Mensah, Richard Martinez, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06141v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06141v1)

**Summary:** This paper focuses on automatic speech recognition (ASR) and ASR-mediated voice interfaces that shape access to public services, healthcare, and education. We argue that persistent failures for low-resource, Indigenous, and non-standard language varieties are not only technical errors, but also implicit linguistic policies that reproduce colonial language hierarchies. Drawing on linguistic capital, raciolinguistic ideology, language policy research, and decolonial computing, we show how data, me...

---

### 15. Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts

**Authors:** Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06123v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06123v1)

**Summary:** Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically...

---

### 16. Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers

**Authors:** Haris Riaz, Hyungji Kim, Mihai Surdeanu

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06111v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06111v1)

**Summary:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraining and injects it across all three dominant PE families (absolute, relative, rotary), for both encoders and decoders, leaving self-attention and the rest of the architecture untouch...

---

### 17. From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems

**Authors:** Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06112v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06112v1)

**Summary:** Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research pr...

---

### 18. ECHO: A Locally-Deployable Agentic Health Assistant with Temporal Memory, Safety Guardrails, and Speech Assessment

**Authors:** Abdulkadir Külçe, Alihan Esen, Cağla Fikir, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06110v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06110v1)

**Summary:** This paper presents ECHO (Enhanced Care \& Health Observer), a locally-deployable conversational health assistant for long-term chronic care management. ECHO integrates three complementary software modules developed under shared supervision as a unified system. The core module is an agentic chatbot built on a ReAct loop orchestrated via LangGraph, equipped with 17 clinical tools and a temporal knowledge graph for persistent cross-session memory; it achieves a 94.9\% tool-execution pass rate acro...

---

### 19. Training-Free Token-Level Steering for LLM Personalized Co-Writing

**Authors:** Wenhao Mao, Chengbin Hou, Weixiao Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06069v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06069v1)

**Summary:** While Large Language Models (LLMs) show great promise for personalization, they often lack specialized domain knowledge. Conventional solutions like fine-tuning struggle with high computational costs and rapid data updates, while Retrieval-Augmented Generation fails to provide fine-grained, token-level steering. Furthermore, chat-based interfaces remain dominant, whereas productive co-writing paradigms have not yet been well exploited beyond the coding domain. To this end, we introduce SteerWrit...

---

### 20. LangChoiceBench: Measuring and Explaining Programming-Language Choice in LLMs

**Authors:** Lukas Twist, Twm Stone, Helen Yannakoudakis, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06041v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06041v1)

**Summary:** Large language models (LLMs) have been shown to exhibit strong Python preferences when generating project-level code, but there is currently no systematic way to measure this behaviour across new models. To bridge this gap, we introduce LangChoiceBench, a project-level code-generation benchmark for measuring Python preference, recommendation-implementation consistency, and language diversity. LangChoiceBench covers 28 projects across seven software areas where Python is often a poor default. We ...

---

### 21. FormBharo: Designing and Evaluating a Voice Agent for Conversational Form Filling in Rural India

**Authors:** Aman Dalmia, Sanskriti Midha, Jigar Doshi

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06027v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06027v1)

**Summary:** In India, almost every social benefit starts with a form, yet the people who need these benefits most are often unable to read or write. Reaching them requires a spoken conversation. Today that work falls to frontline health workers who enroll beneficiaries one at a time, a poor use of stretched capacity. We built FormBharo ("fill the form" in Hindi), a voice agent that fills a structured form over a phone call under tight latency and cost budgets by pairing Large Language Models (LLMs) with det...

---

### 22. EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?

**Authors:** Zirui Wang, Jiaqi Wang, Qinghan Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06022v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06022v1)

**Summary:** Epitopes determine where antibodies bind antigens and shape downstream therapeutic properties such as functional blockade and escape resistance, making epitope understanding central to antibody drug discovery. Although large language models (LLMs) have shown strong biomedical reasoning ability, it remains unclear whether they can infer epitope information directly from antigen and antibody sequences. Existing epitope resources typically focus on isolated prediction tasks or rely on specialized s...

---

### 23. Clinical Communication Processing with Models Trained on LLM-Generated Synthetic Data: A Structured Survey and Novel Application Case Studies

**Authors:** Alexander Apartsin, Yehudit Aperstein

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05993v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05993v1)

**Summary:** Much clinical value is conveyed not through structured records but through communication: exchanges in which patients describe symptoms, clinicians reason and give instructions, ambulances hand over to emergency departments, and nurses pass on a shift. Such language differs from tabular data because meaning depends on speaker role, intent, causality, uncertainty, omission, and channel noise. Healthcare natural language processing must therefore interpret information as conveyed rather than coded...

---

### 24. Causal Episodic Memory for Feedback-Driven Agent Repair

**Authors:** Khang Nhat Hoang Vo, Tam Minh Chu, Anh Trac Duc Dinh, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05906v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05906v1)

**Summary:** LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions. We study whether finalized repair outcomes can improve subsequent Text-to-SQL episodes without parameter updates. We introduce MERIT, a training-free agent that maintains an online dual-polarity memory of oracle-verified corrections and observed unsuccessful directions. Under oracle-assisted benchmark feedback, only memories from earlier finalized episodes are eligible fo...

---

### 25. AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents

**Authors:** Weikai Xu, Yunren Feng, Haoxiang Lei, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05891v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05891v1)

**Summary:** Mobile GUI agents can operate apps through pixel perception and touch actions, making them a promising interface for collecting and improving long-horizon mobile interaction policies. However, real trajectories are difficult to obtain for sensitive apps and privacy-critical operations. At the same time, existing simulated environments are costly to scale up, and GUI world models still suffer from unstable generation, limited modality coverage, and inconsistent action-transition logic. To address...

---

### 26. The em-dash em-beds in Congress: A population-level rise in em-dash frequency in U.S. congressional press releases at the dawn of the large-language-model era, 2021-2025

**Authors:** Przemysław Czuma

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05889v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05889v1)

**Summary:** Large language models (LLMs) can leave small stylistic traces in text written with their help. The most discussed is the em-dash (U+2014), especially the unspaced form word---word, which is normal in typeset English prose but unusual in U.S. press writing, where AP style calls for spaced dashes. This study asks whether that trace is measurable in congressional press releases. In a preregistered design (OSF: 10.17605/OSF.IO/U5NEY), 146,239 scraper-sourced releases from 480 House and Senate office...

---

### 27. The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents

**Authors:** Shayell Aharon Salomon Amir Shaked Matan Noga

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05884v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05884v1)

**Summary:** Existing guidance identifies excessive agency, excessive permission, weak task-bound authorization, and inadequate agent controls as important risks. Control frameworks also describe capabilities for constraining, authorizing, observing, validating, and responding to agent activity. Yet security programs still need a way to manage persistent deployed instances that span components and outlive any one event.   We propose the agentic posture vulnerability (APV) as a task-conditioned vulnerability-...

---

### 28. Personalized Deep Research Query Refinement with Graph-Scaffolded Evidence Grounding

**Authors:** Soojin Yoon, Dongha Lee

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05876v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05876v1)

**Summary:** User requests serve as research specifications for deep research agents, shaping what evidence to seek and how to synthesize it. In personalized deep research, these specifications must additionally reflect user goals, constraints, preferences, and evaluation criteria. User context can be incorporated either within the deep research pipeline or into the research specification provided as its input. We focus on the latter, refining the user request into a personalized research specification befor...

---

### 29. MACRO: Markov Chain Routing of Transformer Layers

**Authors:** Paweł Batorski, Abtin Pourhadi, Akylgali Aitaza, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05872v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05872v1)

**Summary:** Standard Large Language Models (LLMs) execute layers sequentially. Dynamic layer routing, i.e. search for a different execution path through layers involving layer repetitions, skips and other moves, can improve performance. Existing routing approaches often require updating model weights, running expensive search loops per test instance, or demand ground-truth labels during inference. In this work, we propose Markov Chain Routing of Transformer Layers (MACRO), a framework that learns task-speci...

---

### 30. Mapping Similarity Spaces across Embedding Models with Synthetic Query Probing

**Authors:** Marcin Rozmus, Peter van der Putten

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05857v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05857v1)

**Summary:** Retrieval-Augmented Generation systems rely on similarity scores to retrieve relevant content, yet scores are not directly comparable across embedding models due to differing geometric properties, complicating model migration and limiting threshold reuse. We study how similarity scores can be related by learning mappings between score distributions rather than embeddings. We introduce Synthetic Query Probing, generating queries from documents to create controlled query-chunk pairs, enabling larg...

---

### 31. MameLoshnLM: Yiddish Language Model and Evaluation Benchmark

**Authors:** Uri Katz, Omer Goldman, Tomasz Limisiewicz, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05850v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05850v1)

**Summary:** We present MameLoshnLM, the first open-source 8B-parameter language model built specifically for Yiddish. Despite Yiddish's rich textual tradition, its limited digital presence and the scarcity of reliable evaluation resources have constrained progress in Yiddish language modeling. Existing multilingual corpora and benchmarks are often poor proxies for the language, containing substantial amounts of noisy, machine-translated, and misclassified text. We address these gaps by introducing Oytser, a...

---

### 32. Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding

**Authors:** Xiaofeng Wang, Kakam Chong, Shuai Xiao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05832v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05832v1)

**Summary:** Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each dialogue turn and failing to account for the rationale of potential strategies. Inspired by the Theory of Planned Behavior, we propose the Think-Strategy-Response (TSR) framework, which decomposes soc...

---

### 33. MoCA: Implicit Social Context Analysis

**Authors:** Wenhao Xu, Kaiwen Zhang, Hao Li, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05825v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05825v1)

**Summary:** Human social communication, such as affection and intent, is often conveyed in highly implicit ways, where underlying meanings are expressed through indirect, socially and culturally grounded signals rather than explicit statements. Such implicit social contexts are pervasive in real-world interactions, yet there remains a lack of a formal and systematic framework for studying them. In this paper, we introduce Implicit Social Context Analysis (MoCA), a novel task that systematically models impli...

---

### 34. Decomposed Entailment for Factuality Checking and Hallucination Detection

**Authors:** Achir Oukelmoun, Nasredine Semmar, Gaël De Chalendar

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05823v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05823v1)

**Summary:** The reliability of Large Language Models (LLMs) is often compromised by factual inconsistencies, including hallucinations---cases where generated content is not supported by the underlying source. We present HallDetect, a lightweight, reference-free, and black-box framework for hallucination detection that we evaluate not only on summarization but across a broader range of source-grounded generation settings. HallDetect builds on decomposition-based factuality evaluation: generated content is de...

---

### 35. M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding

**Authors:** Hong Jiang, Junnan Zhu, Jingwang Huang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05817v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05817v1)

**Summary:** Metaphor enables the understanding of abstract concepts through cross-domain mappings while conveying affective attitudes. In multimodal scenarios, visual and textual information jointly construct Target--Source mappings, requiring both conceptual understanding and cross-modal reasoning. However, existing benchmarks mainly evaluate metaphor understanding through isolated subtasks and lack evidence-grounded explanations, making it difficult to assess whether models establish mappings grounded in ...

---

### 36. When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

**Authors:** Linfang Shang, Ming Xu, Yiding Sun, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05810v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05810v1)

**Summary:** Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We furthe...

---

### 37. Hierarchical Latent Prediction for Language Models

**Authors:** Chang Shi, Tim Pearce, Manan Tomar, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05806v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05806v1)

**Summary:** While standard Next-Token Prediction (NTP) lays the foundation of language model pre- training, its teacher-forced training paradigm may not be optimal for long-horizon reasoning and planning. Recent works such as Multi-Token Prediction (MTP) and Next-Latent prediction (NextLat) try to mitigate the problem through predicting multiple future tokens and self-supervised prediction in the latent space. However, those auxiliary objectives either have a limited horizon or suffer from compounding error...

---

### 38. On-Policy Delta Distillation for Multilingual Math Reasoning

**Authors:** Byeongho Heo, Jaehui Hwang, Sangdoo Yun, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05802v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05802v1)

**Summary:** On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD$^2$), for mathematical reasoning in English, Korean, and Japanese. OPD$^2$ improves OPD by using the probability gap between a post-trained teacher and its base model as the learning signal. Experiments with Qwen3 show that OPD$^2$ consiste...

---

### 39. Predicting Task Difficulty Without Rollouts

**Authors:** Stefan Krsteski, Charlotte Meyer

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05797v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05797v1)

**Summary:** Task difficulty dictates an agent's likelihood of success, and estimating it without rollouts means forecasting this directly from a task description before executing costly simulations in stateful environments. Reliable estimates would therefore allow environment designers to calibrate evaluation benchmarks and construct progressive training curricula. This becomes increasingly important as agents move into long-horizon domains, where empirical trial-and-error is a severe computational bottlene...

---

### 40. Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation

**Authors:** Tirth Bhatt, Naren Kumar S, Mayank Singh

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05785v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05785v1)

**Summary:** Multilingual text embedding models are commonly adapted using a single training objective across diverse tasks, despite different tasks requiring fundamentally different optimization strategies. We introduce Task-Conditional Flow Matching (TCFM), a multilingual embedding adaptation framework that selectively applies Flow Matching to translation tasks while optimizing retrieval, classification, and pair-classification tasks with objectives better aligned to their learning dynamics. TCFM further c...

---

### 41. GROM: Gradient-Free Rapid One-Shot Machine Unlearning

**Authors:** Paweł Batorski, Przemysław Spurek, Paul Swoboda

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05783v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05783v1)

**Summary:** Machine unlearning has become a critical capability for safely removing specific, sensitive knowledge from large language models (LLMs). Current state-of-the-art approaches primarily rely on iterative, training-time unlearning via fine-tuning. However, even when utilizing parameter-efficient dimensionality reduction techniques like LoRA, gradient-based optimization remains computationally expensive and lacks explicit analytical formulations. It can also leave the targeted knowledge merely hidden...

---

### 42. How to Recognize New Words: A Comparison Between Context Biasing Methods and Speech LLMs

**Authors:** Christian Huber, Alexander Waibel

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05759v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05759v1)

**Summary:** Recognizing new and rare words - named entities, acronyms, domain specific special words, and other items scarce in training data - remains a key challenge for automatic speech recognition (ASR). We compare two strategies for this: context biasing methods, where an ASR model is extended such that during inference a word list can be supplied, and speech large language models (LLMs) prompted with context directly. We evaluate two context biasing methods based on Whisper against three speech LLMs a...

---

### 43. Once a Response, Always a Response: Detecting LLM-generated Text via Latent Prompt Restoration

**Authors:** Hongrui Bao, Yubing Ren, Yanan Cao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05741v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05741v1)

**Summary:** Large language models (LLMs) can generate fluent and convincing text at scale, creating growing risks for misinformation dissemination, educational misuse, and platform governance. These concerns make robust detection of machine-generated text increasingly necessary. Recent zero-shot detectors mainly exploit probability-based statistical discrepancies, but they do not explicitly account for the training process of LLMs, which leaves a distinct generation mechanism insufficiently modeled and limi...

---

### 44. Unified Agent: Managing Interactions across Devices

**Authors:** Xinshuang Liu, Runfa Blark Li, Shaoxiu Wei, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05729v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05729v1)

**Summary:** As capabilities rapidly increase, AI agents can move from running inside one app to acting across a user's devices over time. Yet existing agent systems still fall short in this scenario. This is because observations are scattered across devices and moments, but mainstream systems are not designed around this fact: a single agent that treats devices as tools lacks effective state management for all devices across time, and multi-agent systems coordinate across agents but do not maintain the comp...

---

### 45. Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation

**Authors:** Yuma Asato, Kiyoaki Shirai, Natthawut Kertkeidkachorn

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05726v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05726v1)

**Summary:** Large Language Models (LLMs) are often used as evaluators of text quality, known as LLM-as-a-Judge, which can outperform conventional automatic evaluation metrics that rely on reference texts. However, LLM evaluators tend to generate particular scores regardless of the context of the evaluated text, which is known as scoring bias. This study proposes a novel method to mitigate this scoring bias. An LLM is instructed to randomly generate number tokens, and the latent numerical bias of the LLM is ...

---

### 46. Sparse Mutual Information Graph Averaging for Improving Random Indexing Embeddings

**Authors:** Sriram Loganathan, Gokul Anand, Aung Bo Bo, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05724v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05724v1)

**Summary:** Sparse word embedding pipelines can avoid dense co-occurrence matrix materialization, dense factorization, and gradient training while still relying on sparse global corpus statistics. This paper studies Random Indexing (RI) vectors refined by weighted averaging on a sparse Positive Pointwise Mutual Information (PPMI) graph. On a fairytales corpus, the covered semantic analogy set consists of 272 Google family- category questions. On this family subset, PPMI top-K graph averaging repairs a weak ...

---

### 47. DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model

**Authors:** Wenhao Lin, Chenyu Yu, Xingwei Lin, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05695v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05695v1)

**Summary:** As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a crit...

---

### 48. Answer First, Reason Later: Commitment Order in Diffusion LLMs

**Authors:** Jewon Yeom, Jaewon Sok, Seonghyeon Park, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05687v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05687v1)

**Summary:** Masked diffusion language models (dLLMs) can commit tokens in any order -- a freedom marketed as their core advantage over autoregressive decoding. We show that on reasoning tasks this freedom is instead the axis of failure. Logging every commitment during decoding of LLaDA-8B on GSM8K, we find that unconstrained (pure) decoding commits the final answer at 15-24% of the trajectory while half the reasoning region is still masked, and collapses to answer-only outputs on up to 90% of problems as th...

---

### 49. Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs

**Authors:** Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05660v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05660v1)

**Summary:** As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem. Recent trajectory-based methods seek this signal in layerwise residual-stream displacements, which capture how representations change while attenuating some stable, token-specific information. However, displacement omits the state from which an update originates, whereas restoring the full state risks reintr...

---

### 50. Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution

**Authors:** Sichun Luo, Yi Huang, Guanzhi Deng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05651v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05651v1)

**Summary:** Large language model (LLM)-driven evolution has shown promise for program search and algorithm discovery, but relying on strong models throughout long evolutionary runs is costly. A natural alternative is to combine cheap and strong models under a fixed inference budget. However, existing approaches typically allocate models at the level of individual queries or mutation steps, overlooking that evolutionary search is \textit{stateful}: each generated candidate changes the population from which s...

---

## cs.CV

**50 papers**

### 1. Does FLAIR super-resolution erase or hallucinate small white-matter lesions?

**Authors:** Zahra Khodakarami, Yue Li, Pulkit Khandelwal, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06311v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06311v1)

**Summary:** White matter hyperintensities (WMH), bright regions on Fluid-attenuated Inversion Recovery (FLAIR) scans are associated with cerebrovascular pathology and neurodegeneration. FLAIR is usually acquired with thick slices in clinical settings, giving it poor through-plane resolution. Super-resolution (SR) is a widely used method for recovering an isotropic volume from an anisotropic scan. Yet whether applying it prior to WMH segmentation preserves lesion content remains unknown: a model may erase sm...

---

### 2. UQ-Loc: Uncertainty-Aware LiDAR Scene Coordinate Regression

**Authors:** Jacek Komorowski

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06307v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06307v1)

**Summary:** LiDAR-based Scene Coordinate Regression (SCR) maps point clouds directly to 3D scene coordinates, enabling precise 6-DoF localisation without explicit map retrieval. However, existing methods produce deterministic predictions, discarding aleatoric uncertainty that could improve robustness and downstream decision-making. We present UQ-Loc, which extends the LightLoc architecture with an anisotropic Gaussian covariance head that predicts a full 3x3 positive-definite covariance matrix per voxel. Tr...

---

### 3. TLNM: Externally Validated Tooth Detection, Numbering and Segmentation from Smartphone Photographs Using Mask R-CNN

**Authors:** Arash Nedaei, Henna Tiensuu, Elina Väyrynen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06275v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06275v1)

**Summary:** Oral health issues affect billions globally, but the cost and limited access to professional dental care hinder preventive oral healthcare. Research relies on clinical-grade radiographs or intraoral camera images, unavailable for public self-screening. This study introduces a tooth localisation and numbering model for smartphone photographs. We developed a customised Mask Region-based Convolutional Neural Network (Mask R-CNN) pipeline trained on 1,272 annotated smartphone images. To address vari...

---

### 4. OTLesMix: Wasserstein Barycenter and Optimal Transport Map for Synthetic Lesion Generation with Diverse Shapes and Locations

**Authors:** Robin Trombetta, Carole Lartizien

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06264v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06264v1)

**Summary:** The development of deep learning over the past decade has revolutionized medical imaging segmentation, allowing the extraction of precise descriptors from large volumes to characterize pathologies. Data augmentation is a technique widely regarded as a way to improve model training. It includes simple transformations like spatial operations or intensity modifications, but also more advanced synthesis techniques. Their goal is to generate new realistic samples from an existing dataset to diversify...

---

### 5. MASS: Multiplayer World Models with Authoritative Shared State

**Authors:** Ziqi Cai, Siqi Yang, Yimu Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06257v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06257v1)

**Summary:** Current video world models struggle in multiplayer environments because they entangle world state with view-dependent visual latents, leading to redundant compute, view inconsistencies, and poor scalability. We propose MAS (Multiplayer world models with Authoritative Shared State) to resolve this limitation. Inspired by multiplayer game architectures, MAS disentangles world dynamics and view rendering. A learned Logic Engine advances a global, authoritative typed state from joint actions without...

---

### 6. Toward Deployable Bangla Sign Language Recognition with Expert-Validated Data and a Lightweight Attention-Based Model

**Authors:** Saad Ahmed, Md Khalid Syfullaha

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06252v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06252v1)

**Summary:** Deaf and hard-of-hearing people in Bangladesh communicate mainly through Bangla Sign Language (BdSL). Automatic BdSL recognition on personal devices could widen access to education and services. Existing systems use controlled-setting datasets without expert verification and heavyweight pretrained backbones unsuited to on-device use. We introduce RSBdSL38, 10,874 expert-validated images spanning all 38 BdSL hand signs, representing the 51 letters of the Bangla alphabet, recorded from real signer...

---

### 7. PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation

**Authors:** Elad Yoshai, Natan T. Shaked

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06240v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06240v1)

**Summary:** Unpaired image-to-image translation must decide, per image, what to change and what to preserve without paired supervision. Many diffusion-based unpaired translators control preservation through a single global noise or guidance value applied across the image, which cannot separate content to keep from appearance to change. We present PRISM, a GAN-free flow-matching framework that replaces this global control with a learned per-feature gate. The gate's spatial prior is derived from each source f...

---

### 8. Depth-Guided Video Object Counting in Crowded Scenes

**Authors:** Yuanjing Xu, Xinyan Liu, Weidong Chen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06236v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06236v1)

**Summary:** Our primary objective is to advance video object counting in crowded scenes, aiming to robustly count all instances of a target category based on given text or visual prompts. Existing methods rely on RGB information, limiting their discriminative ability in crowded and occluded conditions. To address this, we propose a Depth-Guided Detector (DG-Det) along with a general post-processing pipeline. By integrating depth cues with multi-scale RGB-D cross-attention and explicit occlusion prediction, ...

---

### 9. EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation

**Authors:** Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06231v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06231v1)

**Summary:** Emotion shapes how viewers interpret a scene, yet existing video generators entangle global atmosphere, affect-bearing semantic cues, and temporal progression within a single text condition. We present EmoWorld, a framework that decouples these factors within a frozen flow-matching video diffusion transformer (Video DiT). A one-time preparation stage extracts layer-specific affect directions and a reusable cue library from geometry-preserving neutral and emotion-edited panoramas. At inference, V...

---

### 10. Reversible Unlearnable Examples: Towards the Copyright Protection in Deep Learning Era

**Authors:** Binze Wang, Jinyu Tian, Xingrun Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06211v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06211v1)

**Summary:** Significant advancements in deep learning have been made possible by the utilization of large datasets, underscoring the critical importance of copyright protection. Adding meticulously designed perturbations to examples, making them unlearnable has become a crucial approach for safeguarding data copyright. Existing methods for creating unlearnable examples overlook the risk of data leakage, which can threaten data ownership. Thus, copyright protection in deep learning faces two main threats: il...

---

### 11. CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection

**Authors:** Nima Hatami, Karim Faez, Saeed Sharifian, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06205v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06205v1)

**Summary:** RGB--T object detection exploits the complementary strengths of visible and infrared imagery, supporting robust perception in low-light, adverse-weather, and complex multi-scale environments. However, existing methods still suffer from insufficient cross-modal interaction, unstable fusion from modality distribution gaps, and the high computational cost of heavy attention-based architectures. To address these issues, CFGPNet is proposed, a Cross-Attention-Based Fused Gradient Programmed Network f...

---

### 12. HOPE: Hand-Object Pressure Estimation from Monocular Videos

**Authors:** Subin Jeon, Byungjun Kim, Hanbyul Joo

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06192v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06192v1)

**Summary:** Estimating physical pressure from vision is essential for understanding contact-rich hand-object interaction. However, prior vision-based pressure estimation methods are largely limited to planar surfaces and single image input, making them difficult to apply to dynamic hand-object interaction with diverse objects. We instead formulate pressure estimation as a hand-centric video prediction problem with monocular video as input. This formulation predicts temporally evolving per-vertex normal pres...

---

### 13. EvReflection: Event-Driven Micro-Dynamics for Reflection Removal

**Authors:** Jiaxiao Wang, Dachun Kai, Huyue Zhu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06184v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06184v1)

**Summary:** Despite remarkable progress in reflection removal, current methods primarily exploit static image priors from a single frame and still suffer from severe residual artifacts due to the inherent ambiguity between the reflection and transmission layers. In this paper, we propose leveraging event signals to break this ambiguity. By employing event cameras to capture micro-dynamics, we reveal the differential motion between these two layers. We thereby present a novel event-driven reflection removal ...

---

### 14. Support Operation Factorization: Compositional Readout of Frozen Vision Encoders under Controlled Interventions

**Authors:** Zhongyao Wang, Wanli Ouyang, Taoyong Cui, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06174v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06174v1)

**Summary:** Compositional analysis of frozen vision encoders should determine both what changed and where it changed. Standard factor probes score these axes separately, however, and can reward multiple operations that reuse the same predicted slot. We call this failure operation laundering. We introduce an injectively aligned leave-one-cell-out protocol over support x operation grids and SO-OPF, a readout that factors cell energy into support salience and a competitive operation posterior. This formulation...

---

### 15. Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments

**Authors:** Giorgio Tonetti, Laurent Kneip, Abel Gawel, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06170v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06170v1)

**Summary:** Hierarchical 3D scene graphs are a promising representation for high-level spatial reasoning in autonomous mobile platforms. However, existing extraction frameworks typically rely on purely local visual clustering or strict geometric heuristics, such as wall-separated rooms, which fail in open-plan or arbitrarily-structured environments. We propose Prior-SG, a task- and prior-driven framework that casts scene graph generation fundamentally as a probabilistic alignment problem. As the robot explo...

---

### 16. BendTwin: Robust Dense-to-Sparse Physical Reconstruction with Bending-Aware Differentiable Spring-Mass Models

**Authors:** Yixiong Jing, Qi Wang, Lin Chen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06164v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06164v1)

**Summary:** Reconstructing objects with mechanical properties from video observations enables physically consistent dynamic prediction, benefiting robotics planning and interaction. Existing spring--mass based physical driven reconstruction approaches offer efficient and differentiable physical reconstruction, but they typically rely on axial springs alone. Such formulations oversimplify the underlying structural mechanics and can become mechanically under-constrained when the physical graph is coarsened, l...

---

### 17. Visual Grounding in Zero-Shot Vision-Language Control

**Authors:** J. de Curtò, Dayani Plasencia, Diego Sánchez, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06154v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06154v1)

**Summary:** Vision-language models (VLMs) are increasingly used as zero-shot controllers, but successful trajectories do not necessarily show that decisions are grounded in visual input: simulator dynamics and conservative action priors can produce favourable scores without meaningful perception. We investigate this with an input-ablation battery: blind-image controls, repeated identical inputs, lane-axis reflection, non-visual baselines, and pipeline-integrity checks. Across nine direct-action models, six ...

---

### 18. CogVis: Must Open-Vocabulary Change Detection Perceive the Scene Anew for Every Query?

**Authors:** Zijie Wang, Chen Zhong, Wei He

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06150v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06150v1)

**Summary:** Earth-surface monitoring requires change detection models capable of recognizing arbitrary semantic categories. Open-Vocabulary Change Detection (OVCD) addresses this need. However, existing methods often entangle temporal perception, semantic discrimination, and region verification, causing unstable results and redundant computation. Inspired by human visual change perception, we propose CogVis, a cognitive memory-guided framework that reformulates OVCD as a perception-memory-verification parad...

---

### 19. Learning visual representations for compositional analysis of artworks and photographs

**Authors:** Fatemeh Behrad, Tinne Tuytelaars, Johan Wagemans

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06142v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06142v1)

**Summary:** Composition, the deliberate arrangement of visual elements, is central to how meaning, emotion, and aesthetic quality are conveyed in artwork, yet it remains among the least formalized dimensions of visual understanding. Prior work highlights a persistent gap in learning meaningful compositional representations, attributing it to semantic bias and suggesting that human-inspired approaches may be key. We compare two parallel paradigms for composition analysis: a human-inspired method grounded in ...

---

### 20. Patient Pose Assessment Using a CT-Based Framework for Synthetic Data Generation

**Authors:** Manuel Laufer, Dominik Mairhöfer, Malte Sieren, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06126v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06126v1)

**Summary:** An adequate diagnostic quality of radiographs is essential for reliable diagnoses and treatment planning. The patient's pose during radiography is one of the most important factors determining the diagnostic quality. Since patient positioning is difficult and not standardized, an automated AI-based approach using depth images to automatically assess the patient's pose before the radiograph has been taken would be helpful. Due to regulatory hurdles, however, it is difficult in practice to acquire...

---

### 21. Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training

**Authors:** Rui Li, Yuanzhi Liang, Ke Hao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06125v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06125v1)

**Summary:** Latent reward models can supervise visual diffusion models without decoding intermediate states into pixel space. This makes alignment with human preferences more efficient. However, existing latent reward models output only scalar scores. They do not estimate the uncertainty of each prediction. The generator therefore cannot determine which feedback is reliable. This can drive optimization in the wrong direction and lead to reward hacking. We propose \textsc{SURE}, a unified latent-space framew...

---

### 22. Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction

**Authors:** Hongyu Zhou, Zorah Lähner

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06117v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06117v1)

**Summary:** 3D Gaussian splatting (3DGS) has emerged as a widely-used tool for novel view synthesis, offering real-time rendering in a sparse representation. However, the method's reliance on structure-from-motion initialization and photometric optimization can lead to suboptimal geometric reconstruction, particularly for objects with high specularity. In this work, we investigate the integration of geometric priors, in the form of predicted normal and depth maps, into the 3DGS framework to improve the reco...

---

### 23. Dense-Cast: A lightweight ensemble of deep learning architectures for precipitation nowcasting

**Authors:** Gourav Jyoti Kalita, Hidam Kumarjit Singh

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06082v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06082v1)

**Summary:** Proper short-term forecasting of precipitation is crucial in disaster management and preparedness. Nonetheless, the variability and nonlinearity of precipitation make short-term forecasting challenging for meteorologists. Moreover, capturing temporal dependencies in spatiotemporal data is a challenge in precipitation nowcasting. In this article, we introduce a lightweight deep learning model for half-hourly precipitation nowcasting. This model has been designed by incorporating the DenseNet arch...

---

### 24. Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal Case

**Authors:** Shilin Hu, Jingyi Xu, Dimitris Samaras, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06075v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06075v1)

**Summary:** Commercial vision-language models are reshaping computer vision, with visual priors broad enough to rival task-specific systems. This raises a natural question: do they reduce the need for classic, physics-informed low-level vision? We study this through shadow removal, a problem shaped by scene geometry, illumination, materials, and occluders, where paired shadow and shadow-free data are hard to collect at scale. We find that a commercial generative editor, used directly, can produce clean shad...

---

### 25. The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents

**Authors:** Weiwei Li, Junzhuo Liu, Tong Chu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06065v1)

**Summary:** GUI agents are commonly trained offline from successful interaction trajectories. Standard training decomposes each trajectory into prefix-action pairs: the agent predicts an action from the current screen and interaction history, while the subsequent observation is discarded. This removes the rationale of why an action is correct: the evidence often appears only on the subsequent screen. For example, to enable Soft Wrap, the agent should click Edit or View, but nothing reveals this until the me...

---

### 26. Bar-JEPA: Extracting Values from Bar Chart with Joint-Embedding Predictive Architecture

**Authors:** Poonam Poonam, Alexander Epple, Timo Ropinski

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06062v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06062v1)

**Summary:** Bar charts are commonly used in data visualization, and while they are easily understood by humans, it is non-trivial to extract the underlying data computationally. For a machine-learning-based approach, training chart de-rendering models usually requires labeled, real-world data. Labeling data is a time consuming task, which is why annotated data is scarce. Models can learn more efficiently when provided with features of high semantic quality, which a joint-embedding predictive architecture (J...

---

### 27. Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval

**Authors:** Zelong Sun, Jun Wang, Kaicheng Yang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06060v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06060v1)

**Summary:** Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates. Recent methods mitigate this limitation by generating Chain-of-Thought (CoT) rationales to enrich the query representation. However, s...

---

### 28. DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval

**Authors:** Xi Chen, Xu Chen, Xiangyang Jia, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06059v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06059v1)

**Summary:** With the rapid growth of Earth observation technologies, remote sensing archives are rapidly expanding, making remote sensing image-text retrieval (RS-ITR) increasingly important. However, continual RS-ITR remains challenging because scale variation and distribution shifts in RS aggravate cross-modal alignment space distortion, making it difficult for existing continual learning (CL) methods to support reliable continual retrieval. To address this challenge, we propose DARAD, a dual-adapter and ...

---

### 29. Integrating Implicit and Explicit Relational Biases through Graph-Based Multiple Instance Learning: A Case Study in Skin Lesion Diagnosis

**Authors:** Rafał Buler, Jakub Buler, Maciej Bobowicz, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06037v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06037v1)

**Summary:** Relational inductive biases are essential for capturing structural dependencies among data. This study investigates a dual-level relational framework for image classification, bridging the gap between implicit representation learning and explicit structural modelling. We begin by establishing a baseline using an EfficientNetB3 architecture. To move beyond standard convolutional biases, we adopt a patch-based strategy, employing a convolutional masked autoencoder to learn implicit inter-patch rel...

---

### 30. PaCoNet: Deep Data Extraction for Parallel Coordinates

**Authors:** Poonam Poonam, Hannah Kniesel, Pere-Pau Vázquez, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06030v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06030v1)

**Summary:** Extracting data from visualizations has long challenged computer vision, with current research focused on bar, line, and pie charts, among other low-dimensional visualizations. However, parallel coordinates as a widely used high-dimensional data visualization approach, remain largely unexplored in this context. As parallel coordinate plots can quickly become cluttered and difficult to interpret when poorly designed or densely populated, automated data extraction from such visualizations is of pa...

---

### 31. Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion: A Controlled Study of Evidence Geometry, Training Coverage, and Compute

**Authors:** Shijie Hao, Weining Zhang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06014v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06014v1)

**Summary:** Should a completion model spend extra test-time compute by iterating, or spend a similar parameter budget on a wider one-shot predictor? The answer is easily confounded by denoising curricula, corruption augmentation, capacity, and unpaired evaluation. We study this question in LiDAR semantic scene completion by comparing a one-shot predictor, a parameter-matched wider predictor, and a weight-tied multigrid refiner initialized from the same frozen predictor. The protocol separates coherent regio...

---

### 32. Wan-Animate-2: Pushing the Application Boundaries of Character Animation

**Authors:** Guangyuan Wang, Li Hu, Dechao Meng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06009v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06009v1)

**Summary:** Character image animation remains a foundational yet challenging task in computer vision. Existing approaches can be broadly categorized into three paradigms: methods based on explicit motion representations suffer from extraction errors and identity drift; methods based on implicit motion features lose fine-grained dynamics through compression; and in-context learning approaches avoid intermediate representations but incur prohibitive computational costs. Furthermore, all current systems are de...

---

### 33. Universal Concept Disruption for SAM3 Image Segmentation

**Authors:** Hao Wang, Yuxuan Zhang, Wei Yang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05983v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05983v1)

**Summary:** SAM3 extends promptable segmentation from geometry-driven mask prediction to open-vocabulary concept segmentation, where a text-conditioned grounding model decides whether a concept is present and segments all matching instances. While this presence-gated design improves concept-level prediction, its adversarial robustness remains unexplored. In this paper, we introduce Universal Concept Disruption (UCD), the first universal cross-concept adversarial attack tailored to SAM3 image segmentation. U...

---

### 34. Multi-Year Geospatial Reasoning using Interannually-Consistent Historical Predictions as a Free Input Modality

**Authors:** Syed Roshaan Ali Shah, Kasper Bonte, David Bekaert, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05979v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05979v1)

**Summary:** Machine learning, and deep networks in particular, are increasingly used to derive higher-level Earth observation (EO) products such as annual land-cover and crop-type maps. Many are generated operationally: each year a new acquisition is processed, typically with the same model, extending a multi-year archive. In the process these systems accumulate two kinds of useful signal that are almost never fed back into the model: the system's own archive of past predictions, and ancillary layers produc...

---

### 35. Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model

**Authors:** Haoning Yang, Xinyuan Chen, Yaohui Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05976v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05976v1)

**Summary:** Recently, diffusion models have made great progress in video generation. However, most existing video diffusion models are trained with short videos, and degrade when extrapolated to long videos, struggling to maintain long-range temporal coherence while retaining diverse motions. To generate consistent, high-quality and dynamic long videos, we propose Diff-VF, a training-free, plug-and-play and model-agnostic framework that converts existing short-video diffusion backbones into long-video gener...

---

### 36. Topology-Aware Neighborhood Learning for Source-Free Cross-Scene Hyperspectral Image Classification

**Authors:** Qingmei Li, Juepeng Zheng, Jiarui Zhang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05964v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05964v1)

**Summary:** Domain adaptation has advanced cross-scene hyperspectral image classification, significantly improving discriminative capability in complex scenarios. However, privacy rules or storage limits often block access to data from the source domain. Conventional domain adaptation methods become impractical, severely restricting their utility in realistic remote sensing scenarios. To tackle this challenge, we propose a topology-aware source-free learning framework. We first introduce the entropy momentu...

---

### 37. Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models

**Authors:** Maulik Chevli, Johannes Brandt, Rickmer Braren, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05960v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05960v1)

**Summary:** Routine CT interpretation is inherently comprehensive, capturing incidental findings across the entire scan volume. 3D CT foundation models could assist this process by providing generalizable representations of anatomy and pathology. To evaluate their diagnostic breadth, we benchmark ten frozen CT encoders across three cohorts of thoracic CT scans, including an unseen internal clinical dataset, using $k$-nearest neighbors, zero-shot prompting, and linear probing. We find no universal state-of-t...

---

### 38. Training a Conditioned Video Game Agent on a VLM Annotated Dataset

**Authors:** Katrin Schmid, Iuri Frosio

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05954v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05954v1)

**Summary:** Reinforcement Learning (RL) is a powerful but far from easy-to-use technique for policy learning. In the specific case of video games, access to the game engine is required to get rewards for training (e.g. to collect rewards from the environment). Furthermore, the proper identification and weighting of the rewards generally requires a difficult trial-and-error approach. Lastly, rewards are often sparse and understanding how they eventually affect the learned policy is a non-trivial exercise. To...

---

### 39. VLMs for Videogame Data Annotation

**Authors:** Katrin Schmid, Iuri Frosio

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05949v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05949v1)

**Summary:** Vision Language Models (VLMs) and Artificial Intelligence (AI) agents have revolutionized how engineers approach complex problems in real-world applications. Their adoption in video games is on the other hand limited by the extreme variability of the synthetic scenarios and their poor compliance with real-world physics. Here we investigate the use of VLMs for annotating video game frame sequences with reward signals, a task with several potential applications including, among others, conditioned...

---

### 40. GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models

**Authors:** Shuai Wang, Yaxin Feng, Xuekun Jiang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05948v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05948v1)

**Summary:** Physics engines facilitate large-scale training and evaluation for embodied intelligence, while generative video world models are emerging as implicit simulators of future states and interactions. However, existing evaluations of physical fidelity are often conducted in isolation and rely heavily on perceptual similarity or human judgments, providing limited insight into which physical principles or parameters are violated. We introduce GAUGE, a real-world-grounded diagnostic benchmark for joint...

---

### 41. Respect Your Zero-Shot Uncertainty: Conservative Calibration for Test-Time-Adapted Vision-Language Models

**Authors:** Jingyan Jiang, Yaru Sun, Xiao Chen, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05945v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05945v1)

**Summary:** Test-time adaptation (TTA) can improve the recognition accuracy of vision-language models under distribution shift, but often degrades calibration, making predictive confidence unreliable for downstream decision-making. Many existing label-free calibration approaches are either coupled to prompt optimization or rely on logit-range statistics that provide only a coarse characterization of the predictive distribution. We show that TTA can increase confidence and reduce entropy even when the top-1 ...

---

### 42. MirrorNet: Can Medical Image Anonymization Really Protect Patient Identity?

**Authors:** Attila Simkó

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05938v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05938v1)

**Summary:** Medical images are routinely de-identified---names, dates, and other metadata removed---and then shared for research, teaching, and public benchmarks under the assumption that this renders them anonymous. Such de-identification protects the metadata but not the pixels, and---apart from scans that directly contain facial structures---whether the image content itself identifies the patient has received little scrutiny. We investigate this question by learning a cycle-consistent correspondence betw...

---

### 43. Floating Radiance Networks

**Authors:** Krzysztof Byrski, Rafał Tobiasz, Grzegorz Wilczyński, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05920v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05920v1)

**Summary:** Recent advances in neural scene representations enable photorealistic novel-view synthesis, yet most methods remain tightly coupled to a single rendering paradigm, limiting their versatility and integration with conventional graphics workflows. We introduce Floating Radiance Networks (FlaRe), a neural scene representation combining explicit ray-traceable geometry with continuous neural radiance functions. A scene is represented by floating planar generalized Gaussian primitives, each carrying a ...

---

### 44. Mapping Armenian Paris: Extracting and Geocoding Commercial Advertisements from the 20th-Century Diaspora Press

**Authors:** Chahan Vidal-Gorène, Seda Kirakosyan, Edita Matevosyan

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05911v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05911v1)

**Summary:** This paper presents an end-to-end, IIIF-based pipeline that turns the digitised Armenian press of France into an interactive map of the 20th-century Parisian Armenian commercial community. On each page, commercial advertisements are located, read, and parsed into structured records, which are then geocoded and placed on the map. Western Armenian is under-resourced and unsupported by off-the-shelf layout and OCR models, so the pipeline uses vision-language models (VLMs) as a data-bootstrapping st...

---

### 45. Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models

**Authors:** Haodong Yan, Junfeng Li, Junjie He, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05903v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05903v1)

**Summary:** Mainstream World-Action Models (WAMs) adapt pretrained video generation models (VGMs) for robot control, transferring their learned dynamics prior for action prediction. These VGMs are typically trained in a variational autoencoder (VAE) latent space. However, the VAE latent space is optimized for pixel reconstruction, which rewards fine appearance detail and leaves the action prediction fragile under visual shifts. Recent works build WAMs in semantic latent space, which are more robust to appea...

---

### 46. To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generation

**Authors:** Xiaobin Huang, Zilong Huang, Yang Luo, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05879v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05879v1)

**Summary:** Text-driven 3D generation has advanced rapidly in creating large-scale outdoor environments and detailed indoor scenes, but these domains are usually synthesized independently, lacking the correspondence required for a coherent urban world. We present HoloWorld, a unified indoor-outdoor urban world generation framework built on a continuously updated cross-scale world context. Initializing from a user description, HoloWorld progressively represents and updates the diverse world information, from...

---

### 47. MAVISEG: Manifold Propagation and Visual Prototypes for Zero-Shot Open-Vocabulary Segmentation in Diffusion Transformers

**Authors:** Rajatsubhra Chakraborty, Xujun Che, Ritabrata Chakraborty, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05878v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05878v1)

**Summary:** Text-to-image diffusion transformers learn about objects and scenes by learning to generate them, making them strong candidates for training-free zero-shot open-vocabulary semantic segmentation. State-of-the-art attribution methods score each pixel independently, comparing its features against a fixed text-derived class representation, whether as an output-space similarity or as a cross-attention weight. This discards structured signals the model itself exposes: the temporal structure of the gen...

---

### 48. D-CLOT: Double Closed Loop Optimal Transport for Unsupervised Action Segmentation

**Authors:** Elena Bueno-Benito, Mariella Dimiccoli

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05877v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05877v1)

**Summary:** Optimal transport (OT) has emerged as an effective framework for unsupervised action segmentation. Yet, in existing OT-based methods, the latent action prototypes that define the OT costs are not re-estimated from the refined frame geometry. Instead, they evolve solely through gradients from the pseudo-label loss. We identify this \emph{representation--prototype inconsistency} as a central bottleneck, particularly around ambiguous transitions and for short or infrequent actions. To address this ...

---

### 49. Shape-Aware Oriented Bounding Box (OBB) to Horizontal Bounding Box (HBB) Conversion

**Authors:** Badha Rathna Sabhapathy, Gotam Dahiya, Vishesh Vatsal

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05858v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05858v1)

**Summary:** Accurate object detection in aerial and satellite imagery is dependent upon the bounding box representation. This is especially true for spatially oriented objects such as ships or aircrafts. Oriented Bounding Boxes (OBB) have a tighter fit and more robust non-max suppression compared to Horizontal Bounding Boxes (HBB), any current post-processing conversion from OBB to HBB either introduces excess empty and background space or removes data from the detection. This paper introduces a novel appro...

---

### 50. DTRNet: Dual Text-Radical Decoding for Handwritten Chinese Text Recognition with Faked Character Detection

**Authors:** Runrui Li, Lin Zhu, Hua Huang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05848v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05848v1)

**Summary:** In K-12 educational scenarios, handwritten Chinese text recognition should not only transcribe student writing, but also detect faked characters. However, existing recognition models are usually confined to a predefined set of normal characters and therefore cannot explicitly identify faked characters. Existing detection methods exhibit complementary limitations: character-level methods provide interpretable structural evidence but suffer from low efficiency, whereas line-level methods are effic...

---

## cs.LG

**50 papers**

### 1. Learning When to Trust via Selective Context Preference Optimization

**Authors:** Xian Sun, Wei Chow, Yingshuo Wang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06377v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06377v1)

**Summary:** Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-contex...

---

### 2. Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering

**Authors:** Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06366v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06366v1)

**Summary:** Electronic health record (EHR) feature engineering is a major bottleneck in clinical research and AI, accounting for 39-45% of data scientists' workload. This is especially pronounced in heart failure, which affects an estimated 6.7 million U.S. adults and requires integrating fragmented EHR data with disease-specific, guideline-based clinical reasoning. Existing rule-based and large language model (LLM)-based approaches offer only partial automation with limited maintainability and evidence tra...

---

### 3. An Optimal Agnostic PAC Algorithm

**Authors:** Markus Engelund Mathiasen, Jian Qian, Nikita Zhivotovskiy

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06363v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06363v1)

**Summary:** Let $H\subseteq\{-1,+1\}^X$ be a class of finite VC dimension $d\ge1$. Writing $L$ for the binary risk and $L^*=\min_{h\in H}L(h)$, we construct a learner achieving the statistically optimal risk bound: from an i.i.d.\ sample of size $n$, for every $0<δ\le 1/2$, with probability at least $1-δ$, \[   L(\widehat h)   \le L^*+ 7\cdot10^8\left(   \sqrt{\frac{L^*(d+\log(1/δ))}{n}}   +\frac{d+\log(1/δ)}{n}   \right). \] This settles the sample complexity of agnostic PAC learning up to universal consta...

---

### 4. AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games

**Authors:** Boning Li, Yu Chen, Longbo Huang

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06362v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06362v1)

**Summary:** Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact...

---

### 5. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

**Authors:** Fanzhe Meng, Guoxin Chen, Jiale Zhao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06352v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06352v1)

**Summary:** Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a...

---

### 6. Scalable estimation of VARMA models

**Authors:** Daniel Paulin, Victor Elvira

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06340v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06340v1)

**Summary:** Vector autoregressive moving-average (VARMA) models have long been considered impractical beyond moderate dimensions: the likelihood is non-convex, the parametrization is identified only up to equivalence, and every evaluation costs a pass over the entire series. Yet their moving-average term captures with a few parameters what a pure autoregression matches only with many lags. We introduce an estimation framework that removes this computational barrier: each optimization iteration is independen...

---

### 7. Optimal Rates for Learning with Monotone Adversaries

**Authors:** Anay Mehrotra

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06337v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06337v1)

**Summary:** A monotone adversary observes an i.i.d. labeled sample and appends a finite number of further examples of its choice, every one of them labeled correctly by the target hypothesis. The learner sees a uniform shuffle of the combined sample and is scored on the original distribution. Every example is correctly labeled, but the insertions depend on the clean sample, so the combined sample is not exchangeable. Larsen, Pabbaraju, and Shetty, who introduced this model, showed that empirical risk minimi...

---

### 8. RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction

**Authors:** Chenglong Wang, Ziming Zhu, Yifu Huo, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06310v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06310v1)

**Summary:** Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a...

---

### 9. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

**Authors:** Varun Ursekar, Apaar Shanker, Yash Maurya, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06301v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06301v1)

**Summary:** As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measu...

---

### 10. On-Policy Self-Distillation without Any Supervision

**Authors:** Yijiang Li, Bingyang Wang, Yijun Liang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06296v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06296v1)

**Summary:** On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including ground-truth signals, environmental feedback, or guidance from larger models, and therefore fall short of genuine "self"-distillation. In this study, we show that on-policy self-distillation can be achieved using only a model's own generations via internal consistency. We propose Unsupervised On-Polic...

---

### 11. BaKron: Efficient Quantization with Kronecker-Factored Hessians

**Authors:** Johann Birnick, Rayan Saab

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06291v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06291v1)

**Summary:** We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations. Two-sided Kronecker-factored Hessian approximations can additionally capture correlations across output coordinates, but applying GPTQ directly in the vectorized weight domain is computationally expensive. Building on the two-sided adaptive-rounding ...

---

### 12. Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data

**Authors:** Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06288v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06288v1)

**Summary:** This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly quantifies the probability that a specific patient will experience extended survival time under treatment versus control. We reformulate IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts. The framework incorporates a pri...

---

### 13. The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity

**Authors:** Iosif Lytras, Nikolaos Makras, Sotirios Sabanis

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06283v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06283v1)

**Summary:** We study the problem of sampling from target distributions whose potentials are simultaneously non-smooth, subject to superlinear gradient growth, and non-convex. We introduce the Subgradient Tamed Unadjusted Langevin Algorithm (SG-TULA), a discretisation of the Langevin diffusion that operates directly on subgradients, without relying on computationally demanding smoothing procedures. To handle the superlinear regime, taming techniques are employed to produce a stable, explicit scheme. We deriv...

---

### 14. Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning

**Authors:** Farzana Nasrin

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06276v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06276v1)

**Summary:** Persistence diagrams (PDs) provide stable and interpretable summaries of multiscale topological structure. While substantial progress has been made in the statistical analysis of PDs, existing literature often treats diagrams as static objects and provide limited frameworks for probabilistic modeling and stochastic evolution on PD space. We introduce a reinforcement learning framework for stochastic dynamics on PD space, where diagrams evolve through topology aware local edit operations. The dyn...

---

### 15. Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints

**Authors:** Omid Bazgir, Md Nasir, Jacob Hoffman, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06265v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06265v1)

**Summary:** Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.   We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility ...

---

### 16. OTLesMix: Wasserstein Barycenter and Optimal Transport Map for Synthetic Lesion Generation with Diverse Shapes and Locations

**Authors:** Robin Trombetta, Carole Lartizien

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06264v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06264v1)

**Summary:** The development of deep learning over the past decade has revolutionized medical imaging segmentation, allowing the extraction of precise descriptors from large volumes to characterize pathologies. Data augmentation is a technique widely regarded as a way to improve model training. It includes simple transformations like spatial operations or intensity modifications, but also more advanced synthesis techniques. Their goal is to generate new realistic samples from an existing dataset to diversify...

---

### 17. Hypothesis Testing with Conditional Queries: Learnability and the Value of Interaction

**Authors:** Zonghuan Xu

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06262v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06262v1)

**Summary:** Model evaluations may fix all tests before observing any responses or select later tests using earlier responses. We study this choice in a conditional-query model on a finite outcome space $\mathcal{X}$ with $|\mathcal{X}|=N$. We first ask which pairs of distribution classes can be reliably distinguished. We then ask how many additional queries are required to match an adaptive tester when all queried events must be fixed in advance. We show that learnability holds if and only if the two classe...

---

### 18. RxnCLF: Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction

**Authors:** Yiting Zheng, Cheng Fang, Anthony Donofrio, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06259v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06259v1)

**Summary:** Reaction yield prediction remains challenging because labeled data are scarce and reaction space is both combinatorially large and sparsely populated, limiting the generalization of existing reaction representations. String-, fingerprint-, and graph-based reaction encodings only partially capture chemical transformations, making accurate prediction difficult for reactions with complex substrates. We propose reaction contrastive learning foundation (RxnCLF), a self-supervised contrastive framewor...

---

### 19. MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction

**Authors:** Dohyun Ku, Min Gu Kwak, Francisco J. Pasquel, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06253v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06253v1)

**Summary:** Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large language model adapted through continual pretraining, supervised fine-tuning, and structured retrieval, together with MetaboLLM-GIN, which converts generated biochemical descriptions into metabolite graphs for patient-level prediction using a graph isomorphism network. Across four backbone families, Metab...

---

### 20. Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification

**Authors:** Alex Buna, Shirley Xiaoqi Liu, Patrick Rebeschini

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06250v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06250v1)

**Summary:** In overparameterised classification, training data can be linearly separable even when the underlying distribution is not. In this setting, gradient descent (GD) on the logistic loss diverges in norm while converging in direction to a max-margin interpolating classifier, whose implicit bias can be statistically suboptimal. In this work, we show that early stopping can overcome this suboptimality: in a Gaussian mixture model with label-flipping noise, GD stopped at an appropriate oracle time achi...

---

### 21. A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance

**Authors:** Fardin Afdideh, Fernando Seoane, Farhad Abtahi

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06246v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06246v1)

**Summary:** Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragmented across technique families, model classes, and deployment contexts, making it difficult to compare methods or describe how a trained model has been modified. This survey synthesiz...

---

### 22. Timestep-Conditioned Transformers for Global Weather Forecasting

**Authors:** Sam Levang, Fran Bartolic, Ty Dickinson, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06241v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06241v1)

**Summary:** Existing machine-learning weather forecasting models rely on predetermined and fixed autoregressive timesteps. The choice of model timestep involves a fundamental trade-off: shorter timesteps (e.g. 1 to 6 hours) finely resolve atmospheric dynamics within the diurnal cycle but increase error accumulation for a given forecast horizon, while longer timesteps (e.g. 24 hours) reduce error accumulation but limit the usability of short-range forecasts where sub-daily predictability is high. In this wor...

---

### 23. TS-RAG: Retrieval Augmented Generation for Time Series Forecasting

**Authors:** Yixiong Xiao, Congxi Xiao, Jingbo Zhou

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06223v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06223v1)

**Summary:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorporating relevant external information, retrieving similar time series sequences as references might also improve accuracy in time series forecasting tasks. However, most time series...

---

### 24. Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation

**Authors:** Alperen Kenan, Paul Bremner, Manuel Giuliani

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06221v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06221v1)

**Summary:** Learning from demonstration (LfD) provides a developmental framework through which robots can develop motor skills by observing and imitating human dynamics, reducing reliance on explicit programming to teach a skill to a robot. The resulting human-like robot motion is recognised as a key factor in building trust and enabling natural collaboration in human-robot interaction. This paper presents a framework for learning human-like robot motion from demonstration, including data collection, probab...

---

### 25. Muon on the Stiefel Manifold Admits an Exact Closed-Form Update

**Authors:** Mikhail Solonko, Molozhavenko Alexander, Maxim Rakhuba

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06218v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06218v1)

**Summary:** We study Muon, a recently proposed matrix-aware optimization method, in the context of the Stiefel manifold. This manifold consists of matrices with orthonormal columns and is ubiquitous in machine learning and scientific computing. Existing extensions of Muon to this manifold rely on heuristic, approximate, or iterative updates with varying computational efficiency. We show that the corresponding Stiefel Muon update admits an exact closed-form solution and use this result to develop Skewon, a p...

---

### 26. Continual Learning in Transition

**Authors:** Zhiyan Hou, Dan Zhang, Tao Feng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06216v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06216v1)

**Summary:** Classical continual learning (CL) has primarily focused on enabling models to update and retain knowledge through parameter-centric mechanisms, e.g., training strategies, architectural designs, and weight adaptation. However, emerging paradigms are reshaping the scope of CL beyond this traditional model adaptation view. For instance, on-policy learning broadens the space of update mechanisms; test-time training extends CL from the training phase to inference; and external harness components such...

---

### 27. Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal Prediction

**Authors:** Anton Conrad, Rustam Isaev, Denis Belomestny, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06206v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06206v1)

**Summary:** Conformal prediction endows arbitrary black-box predictors with finite-sample, distribution-free marginal coverage, yet marginal validity can hide severe covariate-specific miscalibration, while exact distribution-free conditional coverage is finite-sample unattainable. Randomly localized conformal prediction (RLCP) mitigates this gap by calibrating near the test point while preserving marginal coverage. Existing theory, however, lacks finite-sample guarantees for the realized localized set that...

---

### 28. Handling Missing Data in Probabilistic Regression Trees

**Authors:** Taiane Schaedler Prass, Alisson Silva Neimaier, Guilherme Pumi

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06195v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06195v1)

**Summary:** Probabilistic Regression Trees (PRTrees) are a smooth and consistent alternative to classical regression trees, producing continuous predictions through probabilistic split assignments. This paper extends the PRTree framework to accommodate missing predictor values directly during tree construction, eliminating the need for prior imputation. Three strategies are proposed, each exploiting the available information differently: a uniform-probability approach, a partial-observation approach, and a ...

---

### 29. On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities

**Authors:** TaeHo Yoon, Nicolas Loizou

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06182v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06182v1)

**Summary:** We study stochastic extragradient (SEG) methods for solving monotone variational inequality problems (VIPs) over a feasible set. Although extragradient is a foundational algorithm for VIPs and its deterministic convergence theory is well developed, its stochastic counterpart remains less understood. Most existing analyses focus on independent-sample SEG (I-SEG) and assume either that the domain is compact or that the variance of the stochastic operator is uniformly bounded. The behavior of same-...

---

### 30. SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic Language Models

**Authors:** Hoda Fakharzadehjahromy, Emil Wiman, Andreas Bueff, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06179v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06179v1)

**Summary:** Preference optimisation has proven effective for improving large language models but typically relies on costly human preference annotations. Extending these methods to morphologically rich, low-resource languages remains challenging because such annotations are scarce. We present SAGA (Score-weighted Adaptive Generation Alignment), a parser-guided preference optimisation framework that replaces human labels with dependency-parser supervision. SAGA converts parser judgements into preference pair...

---

### 31. Threshold-Based Early Stopping of Accumulations in Neural Networks with Binary Activation

**Authors:** Quentin Luquet de Saint-Germain, Massil Ait Abdeslam, Jean Pierre David

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06177v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06177v1)

**Summary:** Binary neural networks are very attractive for constrained deployment, enabling small footprint and low-power inference. For binary activations, the dot products become sign-controlled additions or subtractions, but the number of operations is unchanged. Indeed, every neuron or output channel still accumulates all of its input, even though only the sign will be retained, which is often wasteful. As the accumulation progresses, the running partial sum frequently drifts so far from zero that its f...

---

### 32. Verifiable Regularity Criterion for Conditional Expectation Operators and Conditional Mean Embeddings with Applications to Nonparametric Regression, Bayesian Inverse Problems, and Koopman Operators

**Authors:** Maximiliano Hertel, Ilja Klebanov, Manuel Schaller, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06155v1)

**Summary:** Conditional expectation operators (CEOs) and their associated conditional mean embeddings (CMEs) play a central role across applied mathematics and machine learning, appearing in nonparametric regression, Bayesian inverse problems, and Koopman operator theory. A fundamental question is when a CEO maps a function space on $\mathcal{Y}$ into a prescribed function space on $\mathcal{X}$, particularly a reproducing kernel Hilbert space (RKHS). We show that such mapping properties are characterized b...

---

### 33. SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models

**Authors:** Yi He, Zhengkang Guan, Anpeng Wu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06137v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06137v1)

**Summary:** Tabular data are ubiquitous in real-world applications and are crucial for data-driven prediction and decision-making across science, industry, finance, healthcare, and public services. Tabular foundation models (TFMs) have emerged as a promising paradigm for general-purpose tabular learning, offering reusable predictors across diverse datasets and substantially reducing the need for task-specific training, tuning, and model development. However, their practical deployment remains constrained by...

---

### 34. LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm

**Authors:** Anjali Gangadhar Katageria, Shobha Rani, Raghu Nandan Sengupta

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06135v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06135v1)

**Summary:** Large Language Models (LLMs) such as ChatGPT and Claude are widely used for information retrieval and problem-solving. Recent work has focused on improving scheduling algorithms to boost throughput while maintaining low latency. However, these approaches often assume Poisson request arrivals with constant rates - an assumption that fails to reflect the inherently bursty and dynamic nature of real-world traffic. We propose a lightweight extension to the state-of-the-art WAIT algorithm [1], which ...

---

### 35. Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture

**Authors:** Leo Sambrook, Sampo Sovio

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06130v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06130v1)

**Summary:** AI agents performing cryptographic operations (signing Git commits, authenticating API calls, issuing certificates) currently store private keys in software-accessible locations: plaintext files, environment variables, or container memory. Any process with sufficient read privileges can extract the raw key material. A recent production incident demonstrated the practical severity: private keys were exfiltrated from a widely deployed framework via email injection in under five minutes. We aim to ...

---

### 36. Is Self-Pretraining really useful to improve diagnosis in medical Time Series?

**Authors:** Omar Coser, Antonio Orvieto, Paolo Soda, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06122v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06122v1)

**Summary:** Inspired by recent evidence that transformer architectures benefit from Self-PreTraining (SPT) on long-context benchmarks, we investigate whether similar gains extend to multimodal, multivariate, and even simple univariate medical time series. Our objective is to assess the impact of SPT on the performance and scalability of transformer-based models across diverse medical applications, particularly under limited data conditions. We evaluate transformer architectures on three representative medic...

---

### 37. From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems

**Authors:** Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06112v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06112v1)

**Summary:** Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research pr...

---

### 38. Kastor: An efficient fine-tuning strategy for generative emulation of PDE simulations

**Authors:** Guillaume Couairon, Alexis Jacq, Yu-Han Wu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06107v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06107v1)

**Summary:** Machine learning offers a promising avenue to accelerate physical simulations by replacing computationally expensive traditional Partial Differential Equation (PDE) solvers with fast, differentiable surrogate models. However, standard auto-regressive ML emulators often suffer from error accumulation over long horizons and struggle to capture the stochasticity of complex physical systems. In this paper, we propose Kastor, a comprehensive methodology to adapt a deterministic physics foundation mod...

---

### 39. Does Latent Context Help? A Controlled Evaluation of Inverse Reinforcement Learning in Arctic Shipping

**Authors:** Vaishnav Vaidheeswaran, Dilith Jayakody, Biruk Ambaw, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06105v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06105v1)

**Summary:** Artificial Intelligence (AI)-assisted navigation can help Arctic shipping adapt to rapidly changing sea-ice conditions, but reliable deployment requires reward models that are interpretable and robust to changing environments. Inverse reinforcement learning (IRL) provides a framework for recovering such rewards from vessel trajectories, while recent meta-IRL methods introduce latent context variables to capture behavioral heterogeneity. However, it remains unclear whether these latent representa...

---

### 40. ML-for-ML

**Authors:** Yutong Zhao, Noga H. Rotman, Gianni Antichi, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06046v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06046v1)

**Summary:** AI training workloads are growing rapidly, making their time, energy, and infrastructure costs increasingly important. In shared cloud clusters, training and fine-tuning jobs compete with co-running workloads for network resources, while network mechanisms and ML training choices are typically optimized separately: networking controls how bytes move, whereas ML systems control when and how much communication occurs. We argue that this separation leaves end-to-end performance on the table.   We p...

---

### 41. Integrating Implicit and Explicit Relational Biases through Graph-Based Multiple Instance Learning: A Case Study in Skin Lesion Diagnosis

**Authors:** Rafał Buler, Jakub Buler, Maciej Bobowicz, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06037v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06037v1)

**Summary:** Relational inductive biases are essential for capturing structural dependencies among data. This study investigates a dual-level relational framework for image classification, bridging the gap between implicit representation learning and explicit structural modelling. We begin by establishing a baseline using an EfficientNetB3 architecture. To move beyond standard convolutional biases, we adopt a patch-based strategy, employing a convolutional masked autoencoder to learn implicit inter-patch rel...

---

### 42. Dynamic Graph Prompting via Topology-Routed Mixed-Curvature Experts

**Authors:** Quanxin Wang, Xuanting Xie, Bingheng Li, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06031v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06031v1)

**Summary:** Dynamic graph prompting freezes a pre-trained temporal backbone and adapts it to label-scarce downstream tasks using lightweight prompts. However, existing methods operate within a single, fixed embedding space. In this work, we reveal that temporal shifts in local clustering and degree heterogeneity actively reorganize the edge curvature spectrum---indicating that the optimal representation geometry dynamically evolves with local topology over time. We formalize this unaddressed mismatch as geo...

---

### 43. Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference

**Authors:** Jiming Su, Hantao Hua, Lujia Yin, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06025v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06025v1)

**Summary:** In simulation-in-the-loop decision-making systems, reinforcement learning (RL) inference is often constrained by simulator-side execution overhead, where workloads are highly dynamic and sensitive to runtime thread configurations. Existing multithreaded strategies struggle to match thread resources before or during execution, causing resource contention, scheduling overhead, and reduced throughput. Through empirical analysis, we identify the ratio of task execution time to scheduling time as the...

---

### 44. BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition

**Authors:** Bojing Hou, Ruohao Li, Yitong Zhu, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06023v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06023v1)

**Summary:** To address the limitations of video-based emotion recognition under ambiguous or socially masked behavioral cues, as well as the poor deployability of physiological signals, this paper proposes a reliability-aware physiology-to-video knowledge distillation framework, termed BioKD. The proposed framework leverages physiological signals as privileged information during training to guide a video-based student model in learning deep affective representations, while relying solely on non-intrusive vi...

---

### 45. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models

**Authors:** Jiale Han, Xiang Li, Jing Qian, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06020v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06020v1)

**Summary:** Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic ...

---

### 46. ProDVI: Programmatic Dynamics Priors for Value Network Initialization

**Authors:** Xinwei Liu, Junyuan Liang, Jianting Zhang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06015v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06015v1)

**Summary:** Deep Reinforcement Learning (RL) is notoriously sample inefficient. One contributing factor is that RL agents are typically initialized from scratch, forcing them to acquire task-relevant knowledge through online interaction. Existing approaches obtain informative initializations through pre-collected datasets, high-fidelity simulators, or meta-learning over related tasks, but these prerequisites may be difficult to access or even unavailable. In this paper, we propose Programmatic Dynamics Prio...

---

### 47. Do Tabular Foundation Models Agree with Themselves?

**Authors:** Christian Klötergens, Vijaya Krishna Yalavarthi, Lars Schmidt-Thieme, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06004v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06004v1)

**Summary:** Tabular Foundation Models (TFMs) are currently the best approach to tabular prediction problems. They are constructed as transformers that approximate the Bayesian posterior predictive distribution based on a pre-training prior. These univariate predictors can be converted into multivariate ones autoregressively by sampling one target and adding it to the features.   However, the faithfulness of the resulting joint has not been investigated. Furthermore, TFMs cannot be evaluated against the post...

---

### 48. A Unified Risk View of Uncertainty: Posterior Risk for Disentanglement and Evaluation Beyond Proxies

**Authors:** Frieder Wizgall, Georg Tirpitz, Moritz Seiler, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05995v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05995v1)

**Summary:** Reliable uncertainty estimates are critical in safety-sensitive applications, where understanding the sources of predictive uncertainty is essential. This often requires disentangling epistemic uncertainty from aleatoric uncertainty, yet these uncertainty types are not defined consistently across the literature, making it difficult to assess whether a method produces accurate uncertainty estimates. Evaluation is further complicated by the fact that ground-truth epistemic uncertainty is typically...

---

### 49. Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control

**Authors:** Xinwei Liu, Junyuan Liang, Jianting Zhang, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05989v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05989v1)

**Summary:** Sample-efficient policy learning from pixels is a long-standing challenge in reinforcement learning (RL). Recent dynamics-based representation learning methods have significantly improved the sample efficiency of model-free visual RL by learning dynamics-aware representations through auxiliary prediction performed either in latent space (self-prediction) or observation space (observation prediction). However, state-of-the-art methods from both categories still struggle on challenging visual cont...

---

### 50. AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

**Authors:** Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05987v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05987v1)

**Summary:** Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in ...

---

## cs.NE

**50 papers**

### 1. Threshold-Based Early Stopping of Accumulations in Neural Networks with Binary Activation

**Authors:** Quentin Luquet de Saint-Germain, Massil Ait Abdeslam, Jean Pierre David

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06177v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06177v1)

**Summary:** Binary neural networks are very attractive for constrained deployment, enabling small footprint and low-power inference. For binary activations, the dot products become sign-controlled additions or subtractions, but the number of operations is unchanged. Indeed, every neuron or output channel still accumulates all of its input, even though only the sign will be retained, which is often wasteful. As the accumulation progresses, the running partial sum frequently drifts so far from zero that its f...

---

### 2. A Special Point Skeleton Reconstruction Algorithm for Dynamic Multiobjective Optimization

**Authors:** GuangXian Gan, MinRong Chen

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06096v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06096v1)

**Summary:** To address the issue that existing dynamic multi-objective optimization algorithms mainly rely on individual migration or independent special point sampling after environmental changes, while failing to fully exploit the structural relationships among representative solutions, a Special Point Skeleton Reconstruction based Dynamic Multi-Objective Evolutionary Algorithm (SPSR-DMOEA) is proposed. First, the centroid, knee points, and extreme points are extracted from the Pareto optimal solution set...

---

### 3. Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05996v1)

**Summary:** Deep Belief Networks (DBNs) learn hierarchical generative models without class supervision. Here, we ask whether this purely unsupervised process nevertheless organizes internal representations according to the unknown data classes. We analyze successive layers of DBNs trained on MNIST, Fashion-MNIST, and KMNIST using the Generalized Discrimination Value (GDV), supervised probes applied only after training, a reconstruction-based measure of abstraction distance, effective dimensionality, and fre...

---

### 4. Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution

**Authors:** Sichun Luo, Yi Huang, Guanzhi Deng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05651v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05651v1)

**Summary:** Large language model (LLM)-driven evolution has shown promise for program search and algorithm discovery, but relying on strong models throughout long evolutionary runs is costly. A natural alternative is to combine cheap and strong models under a fixed inference budget. However, existing approaches typically allocate models at the level of individual queries or mutation steps, overlooking that evolutionary search is \textit{stateful}: each generated candidate changes the population from which s...

---

### 5. Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling

**Authors:** Sanjith Senthil, Rishidev Chaudhuri

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05464v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05464v1)

**Summary:** The pruning of network connections is key to brain function but, despite its importance, there exist few biologically-plausible pruning rules with demonstrated good performance. In this work we evaluate noise-prune, a recently introduced unsupervised local pruning rule for recurrent networks that uses noisy fluctuations to determine the importance of connections. Noise-prune has previously only been empirically tested on random networks without a specific computational function. We show that noi...

---

### 6. Quality Diversity for Reliable Data Driven Time-Use Optimization

**Authors:** Aneta Neumann, Ty Stanford, Dorothea Dumuid, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05230v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05230v1)

**Summary:** The daily allocation of the finite 24-hour time budget is strongly associated with physical, mental, and cognitive health. While predictive models can estimate the relationship between time-use compositions and health outcomes such as body mass index, life satisfaction, and cognition, most optimization approaches focus only on maximizing expected benefit and do not consider the uncertainty inherent in data-driven prediction. Ignoring uncertainty in health-related decisions can lead to unrealisti...

---

### 7. Universal Function Approximation via Diffractive Optical Processors: Physical Limits, Error Bounds, and Learnability

**Authors:** Md Sadman Sakib Rahman, Che-Yung Shen, Aydogan Ozcan

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04582v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04582v1)

**Summary:** We present a unified theoretical framework connecting classical universal approximation theory, Fourier-feature approximation, and diffractive optical processors. We show that phase-encoded diffractive processors implement finite Fourier-feature expansions whose mathematical completeness follows from Fourier/Stone-Weierstrass arguments, while their physical realizability is governed by finite coefficient synthesis through optimized spatially varying coherent point-spread functions (PSFs). Our an...

---

### 8. Emergence of Reputation-Based Cooperation in LLM Agents

**Authors:** Kazuya Horibe, Kenji Itao, Wataru Toyokawa

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04507v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04507v1)

**Summary:** Can cooperation among large language model (LLM) agents be evolutionarily stable against free-rider invasion? We study an indirect reciprocity donation game where LLM agents observe behavioral traces and donate on a continuous scale. Strategies, represented as natural language prompts, evolve through cultural transmission across generations. Across four LLM backends, robustness to free-rider invasion varies by more than an order of magnitude. The strongest predictor of this robustness is opponen...

---

### 9. A Counterexample to Fourier Alignment in Single-Neuron Modular Addition

**Authors:** Gautam Neelakantan Memana

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04451v2) | 📄 [PDF](https://arxiv.org/pdf/2608.04451v2)

**Summary:** We give a negative solution to MAIS-O60. We first construct an example in which an initially active ReLU neuron becomes completely inactive in finite time and thereafter remains frozen at a limit whose Fourier energy is equally distributed among all nonzero real frequency classes. The counterexample holds on an open set of initial conditions and therefore occurs with positive probability under Gaussian initialization. An appendix prepared by GPT-5.6 Sol strengthens the counterexample by showing ...

---

### 10. The Transformer Revolution, Part 1: Dynamic Processing through Output- Weight Interconnections

**Authors:** Marco Giunti, Fabrizia Giulia Garavaglia

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03921v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03921v1)

**Summary:** This paper offers a new interpretation of the Transformer during inference. Against the "stochastic parrot" view that large language models merely reproduce statistical regularities learned in training, we argue that Transformers construct and apply prompt-dependent transformations whose parameters are generated during inference. We call this form of computation SIDPP: Sequence-level Interactive Dynamic Parallel Processing. The Transformer is interpreted as a system that transforms concepts by m...

---

### 11. Omega-S: A Functional Resilience Index for LLM Fine-Tuning

**Authors:** Alberto Acedo

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03887v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03887v1)

**Summary:** Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than ...

---

### 12. MuEvo: LLM-Driven Evolution of Multi-Heuristic Ensemble

**Authors:** Haoze Lv, Ning Lu, Shengcai Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03636v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03636v1)

**Summary:** Large language model-based automated heuristic design (LLM-AHD) has shown strong potential in discovering effective heuristics for combinatorial optimization problems. However, existing methods primarily optimize a single heuristic, whereas practical optimization frameworks often rely on multiple interacting components. Directly extending single-heuristic methods is challenging because early component selection can overlook components with late potential, while independent evolution ignores inte...

---

### 13. AS-FedBridge: Pseudo-Spike Bridge Distillation for Heterogeneous ANN-SNN Federated Learning

**Authors:** Shengyang Li, Yiting Dong, Liuyang Song, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03324v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03324v1)

**Summary:** Federated learning enables collaborative model training across distributed edge devices while strictly preserving data privacy. To facilitate practical deployment on resource-constrained edge devices, Spiking Neural Networks (SNNs) have emerged as a promising alternative to traditional Artificial Neural Networks (ANNs) due to their sparse computing mechanisms and high energy efficiency. However, jointly training ANNs and SNNs exposes a challenge of representational misalignment, which is intrins...

---

### 14. Impacts of Single-objective Landscapes on Multi-objective Optimization

**Authors:** Shoichiro Tanaka, Keiki Takadama, Hiroyuki Sato

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03266v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03266v1)

**Summary:** This work revealed a relationship between a multi-objective optimization problem and single-objective optimization problems that exist in the multi-objective problem. This work focused on combinatorial problems and investigated the relations between the local optima networks of the single-objective problems and the Pareto optima network of the multi-objective problem. Each of their networks has a graph structure. We divided the entire network into subgraphs. Each subgraph was called a component ...

---

### 15. NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives

**Authors:** Yantong Liu, Zheyu Zhang, Runpeng Liu, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03187v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03187v1)

**Summary:** Multimodal medical large language models remain structurally weak for neuro-oncology because volumetric evidence is compressed into generic visual tokens and diagnostic conclusions often lack an auditable link to MRI regions. We present NeuroMosaic, a 3D multimodal language model that converts multi-sequence brain MRI into anatomy-indexed regional tokens, aligns them with clinical narrative and molecular concepts, and generates evidence-linked outputs. The architecture combines a multi-resolutio...

---

### 16. ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces

**Authors:** Kunal Kumar Pant, Nithin Nagaraj

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01968v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01968v1)

**Summary:** Transformer models are most often understood through what they do: their benchmark performance, generation quality, or behavior on downstream tasks. Yet frozen transformer input-embedding spaces may also be examined through their responses to a controlled deterministic probe before contextual computation or task-specific adaptation. Guided by this response-based view, we introduce \emph{ChaosProbe}, a deterministic neurochaos-inspired method for constructing response-based fingerprints of frozen...

---

### 17. Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory

**Authors:** Zhaotian Gu, Jie Su, Weiwei Wang, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01947v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01947v1)

**Summary:** The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...

---

### 18. Towards Autonomous Formulaic Alpha Discovery: An Evolutionary Computation Perspective

**Authors:** Xinwei Yu, Yiyang Fu, Mingcheng Fan, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01789v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01789v1)

**Summary:** Automated formulaic alpha discovery aims to generate predictive and interpretable trading signals from large symbolic factor spaces. Its effectiveness is constrained by noisy fitness estimates, market nonstationarity, costly backtesting, semantic redundancy, and conflicting practical objectives. Existing studies employ diverse techniques, including genetic programming (GP), evolutionary algorithms (EAs), reinforcement learning (RL), generative flow networks (GFlowNets), Monte Carlo tree search (...

---

### 19. An Evolutionary Algorithm Assisted by an Ensemble of Pareto-Optimal Surrogate Models

**Authors:** Kei Nishihara, Yaochu Jin, Masaya Nakata

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01777v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01777v1)

**Summary:** An ensemble of surrogate models helps improve the prediction quality and robustness of surrogate models, and in turn, the search performance of surrogate-assisted evolutionary algorithms (SAEAs). Although different degrees of smoothness of the approximated fitness landscapes need to be carefully designed for an effective ensemble, little attention has been paid to the explicit tuning of the degree of smoothness derived by surrogate models. This study proposes an adaptive ensemble SAEA, which aut...

---

### 20. Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition

**Authors:** Xiubo Liang, Jinxing Han, Yuke Li, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01646v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01646v1)

**Summary:** Handwritten Text Recognition (HTR) is computationally imbalanced in two ways: most image pixels are background, and many width-axis sequence positions are blank-dominated. This creates a mismatch for Spiking Neural Networks (SNNs): handwriting is observed as a static image, whereas spiking computation unfolds over timesteps. We propose Spike-HTR, a hybrid spiking recognizer that controls both the number of spiking steps and the number of width positions processed by the deep sequence mixer. To m...

---

### 21. SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks

**Authors:** Xiubo Liang, Jinxing Han, Yuke Li, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01622v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01622v1)

**Summary:** Spiking Neural Networks (SNNs) enable event-driven computation with sparse activations, but building multimodal Transformers on SNNs is hindered by unstable training in deep spiking stacks and the mismatch between dense softmax attention and spike-based communication. We propose SMM Transformer, an SNN-based multimodal Transformer framework that combines (i)PLMP, a Parallel LIF with Multistage Learnable Parameters neuron and a tailored P-STBP algorithm for stable deep SNN training, (ii) SMSA, an...

---

### 22. Unsupervised Multidomain Approaches to Named Entity Recognition with Small Datasets

**Authors:** Israel Fianyi, James Montgomery, Soonja Yeom

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.00984v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00984v1)

**Summary:** This paper explores the challenges and the methodologies associated with learning quality representations in scenarios with unlabelled small or limited datasets for downstream information extraction task (Multidomain Named Entity Recognition (NER). The study adopts a Transfer Learning on small datasets. Traditional NER systems often rely on large, labelled data, which is impractical for many domains. This study, therefore, applies an unsupervised pre-training approach to precondition and identif...

---

### 23. DGA$_2$D: Directed Graph-Guided Automated Algorithm Design with Large Language Models

**Authors:** Jiale Zhao, Zimu Chen, Sirui Mao, et al.

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00700v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00700v1)

**Summary:** The rapid development of Large Language Models (LLMs) has opened new avenues for Automated Heuristic Design (AHD) for solving NP-hard combinatorial optimization problems (COPs). However, existing LLM-driven AHD methods are largely confined to rigid solver templates, relegating the search process to isolated module tuning. Transitioning to fully autonomous, system-level algorithm design is essential but fraught with low reliability of generated operators, extremely large search spaces, and ineffe...

---

### 24. SDDMO-Bench: A Benchmark Suite for Streaming Data-Driven Dynamic Multi-Objective Optimization

**Authors:** Wenjie Xiao, Hui Bai, Junhao Chen

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00474v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00474v1)

**Summary:** Streaming data-driven dynamic multi-objective optimization requires algorithms to track time-varying Pareto fronts using only sequential observations under concept drift. However, systematic evaluation remains difficult because real-world problems usually lack ground-truth optima, drift annotations, and controllable conditions, while existing benchmarks provide limited support for standardized comparison. This paper proposes SDDMO-Bench, a benchmark suite that transforms classical dynamic multi-...

---

### 25. Linear Proposal Operators and Stochastic Search Geometry in SOMA and Differential Evolution

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29228v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29228v1)

**Summary:** Swarm and evolutionary algorithms are usually analyzed as complete procedural systems in which nonlinear selection, replacement, and adaptation obscure simpler structure within candidate generation. This paper introduces an operator--selection factorization that separates objective-independent variation from boundary repair and fitness-dependent selection, and uses it to study the proposal geometry of the Self-Organizing Migrating Algorithm (SOMA) and Differential Evolution (DE). The canonical S...

---

### 26. Analysis of Memory-Runtime Trade-offs in Caching Strategies for Genetic Programming Symbolic Regression

**Authors:** Jiaming Shi, Kei Sen Fong, Mehul Motani

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29116v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29116v1)

**Summary:** Genetic Programming Symbolic Regression (GPSR) generates mathematical expressions to model input-output relationships using an evolutionary process. A significant challenge in GPSR lies in the repeated evaluation of entire expressions or their sub-expression, which inflates computational runtime. To address this inefficiency, caching mechanisms have been employed to reduce redundant computations. However, prior studies predominantly employ a single caching strategy, offering limited insights int...

---

### 27. SILVA Networks as Structured Implicit Layers and Vector Attractors via Dynamic Interaction Fields

**Authors:** Jose Luis Lima de Jesus Silva

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.28989v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28989v1)

**Summary:** Many learning problems require representations that reconcile direct input, nearby structure, and broader context. In implicit neural layers, these influences are usually absorbed into a single fixed-point update, making it hard to identify what enters from the stimulus, what propagates locally, what comes from global context, and what is produced by solver dynamics. Here we introduce SILVA Networks, Structured Implicit Layers and Vector Attractors via Dynamic Interaction Fields. SILVA separates...

---

### 28. Hash Chemistry: Minimal Models for Evolutionary Growth of Complexity

**Authors:** Ilya Horiguchi, Hiroki Sayama

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28219v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28219v1)

**Summary:** Hash Chemistry is a family of minimalistic evolutionary models in which a deterministic hash function assigns a scalar score to entities of arbitrary size, opening a combinatorially vast possibility space (a ``cardinality leap''). Since its introduction, the idea has been realized in several settings, from the original spatial formulation to a fast non-spatial variant and then to structural cellular models. Here we review the Hash Chemistry family as a coherent modeling framework and use it to e...

---

### 29. Nanoparticle Networks for Neuromorphic Computing

**Authors:** Jonas Mensing, Wilfred G. van der Wiel, Andreas Heuer

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.27844v1) | 📄 [PDF](https://arxiv.org/pdf/2607.27844v1)

**Summary:** Physical computing leverages complex dynamical systems for energy-efficient data processing. In this work, we present a neuromorphic architecture based on metallic nanoparticles interconnected by molecular junctions on a $\text{SiO}_2$/Si substrate. We demonstrate that surrounding static control electrodes transform this nanoparticle network from a passive reservoir into a tunable nonlinear dynamical system. By analyzing how these electrodes route simple one-dimensional voltage inputs into multi...

---

### 30. Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling

**Authors:** Yuan Tian, Yi Mei, Mengjie Zhang

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.27698v1) | 📄 [PDF](https://arxiv.org/pdf/2607.27698v1)

**Summary:** In dynamic multi-mode project scheduling, activities have alternative execution modes and uncertain durations, while precedence relations and limited resources constrain their execution. Heuristic priority rules support fast online decisions, but their design requires substantial domain expertise. Genetic programming (GP) hyper-heuristics can automatically evolve such rules. Large language models (LLMs), meanwhile, provide a flexible interface for interpreting scheduling information and explaini...

---

### 31. The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy

**Authors:** Zeyu Wang

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26648v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26648v1)

**Summary:** Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates. We argue the energy dividend of sparsity is not a property of SNNs but of the task. Holding architecture fixed and swapping only the hidden unit (continuous vs. leaky-integrate-and-fire), plus a two-sided target-firing-rate probe, we measure how far activity can be pushed down before quality breaks. Low-load feed-forward pe...

---

### 32. Shared Symbolic Backbones for Physically Consistent Multi-Output Symbolic Regression

**Authors:** Manuel Rodriguez

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26528v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26528v1)

**Summary:** Symbolic regression provides analytical expressions, but it is usually applied one output at a time. This is limiting in process systems, where state variables are often coupled through shared physical parameters. Independent symbolic regression can give accurate individual equations that are difficult to interpret as one model. We present a neuro-evolutionary symbolic regression method for coupled multi-output systems. The method searches for a shared symbolic backbone: a set of latent symbolic...

---

### 33. EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks

**Authors:** Peng Yin, Kai Li, Yifan Zhang, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26490v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26490v1)

**Summary:** Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs), yet their performance heavily relies on the manual, trial-and-error engineering of neural representations, loss formulations, and optimization dynamics. While Large Language Models (LLMs) offer a promising avenue for automated design, unconstrained code generation often yields mathematically invalid or numerically unstable solutions under strict scientific computing con...

---

### 34. Reconstructing Backpropagation from Forward Fluctuations in Noise-modulated Neural Networks

**Authors:** Shuhei Ikemoto

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26483v1)

**Summary:** A Noise-modulated Neural Network (NNN) learns and infers only in the presence of noise, treating noise as a computational resource rather than a disturbance. The noise lets it learn efficiently by backpropagation while transmitting spike-like signals, but backpropagation needs a reverse path through transposed weights, the weight transport problem, which undermines biological and neuromorphic plausibility. Forward-only alternatives typically substitute a different objective or fixed random feedb...

---

### 35. Neural Architecture Search for Traffic Prediction: A Survey of Methods, Challenges, and Future Directions

**Authors:** Truong Giang Vu, Li Yang, Richard W. Pazzi

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26467v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26467v1)

**Summary:** Traffic prediction is a core task in intelligent transportation systems, supporting applications such as adaptive signal control, route guidance, and ride-hailing dispatch. Deep learning models, including graph convolutional networks, recurrent networks, and Transformers, achieve strong results on standard benchmarks, but their architectures are designed by hand, requiring significant expert effort and producing models that often generalize poorly across cities and datasets. Neural Architecture ...

---

### 36. Fourier Feature Physics-Informed Neural Networks for Elasto-Plastic Analysis of Geomaterials with a Non-Associative Mohr-Coulomb Model

**Authors:** Apisit Robjanghvad, Sompote Youwai

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25150v2) | 📄 [PDF](https://arxiv.org/pdf/2607.25150v2)

**Summary:** Elasto-plastic boundary value problems in geotechnical engineering are conventionally solved by the Finite Element Method (FEM), which incurs high computational cost from incremental-iterative procedures. Physics-Informed Neural Networks (PINNs) offer a mesh-free alternative but suffer from spectral bias, failing to resolve the sharp gradients arising at elastic-plastic boundaries and within localized plastic zones. This limitation is particularly consequential for the non-associative Mohr-Coulo...

---

### 37. Mitigating the Impact of Retention Loss on Inference Accuracy in 65 nm Single-Poly Floating-Gate Analog In-Memory Computing

**Authors:** Mirko Brazzini, Giulio Filippeschi, Alessandro Catania, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25058v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25058v1)

**Summary:** We show with experiments and system-level simulations that it is possible to successfully mitigate the impact of retention loss on inference accuracy degradation by using both circuit-level compensation techniques and batch normalization recalibration at the algorithmic level. Experiments are performed on a single-poly floating-gate (FG) analog non-volatile memory array for analog in-memory computing fabricated in a standard 65 nm CMOS. We use a model of retention-loss statistics calibrated with...

---

### 38. Lindblad-Inspired Multi-Timescale Reservoir Computing with Separable Rotation and Dissipation

**Authors:** Jyotiranjan Beuria, Amit Shukla

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2608.04028v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04028v1)

**Summary:** Echo-state networks enable efficient temporal learning by fixing the recurrent dynamics and training only a linear readout. However, conventional reservoirs typically accommodate signal mixing, memory retention, and stability within a single random recurrent matrix. Existing structured designs improve topology, norm preservation, leakage, or depth, but generally do not provide separate modal control of reversible mixing and irreversible forgetting together with a direct global stability guarante...

---

### 39. The K-SCAN Clustering Algorithm

**Authors:** Filip Kosiorowski, Grzegorz Sroka

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24537v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24537v1)

**Summary:** In the Big Data era, the scalability of clustering algorithms constitutes a key challenge. Traditional density-based methods (e.g., DBSCAN) offer robustness to noise and the ability to detect non-linear clusters, yet their quadratic time complexity $O(N^2)$ drastically limits their applicability. Conversely, partitional algorithms (e.g., K-Means), with their linear complexity $O(N)$, impose sphericity on the resulting groups and fail in the presence of outliers. This paper presents K-SCAN -- a n...

---

### 40. What EEG Foundation Models Encode: Dataset Identity and a Negative-Control Suite for Clinical Benchmarks

**Authors:** Marzieh Zare

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24519v2) | 📄 [PDF](https://arxiv.org/pdf/2607.24519v2)

**Summary:** Pretrained EEG foundation models are proposed for clinical decoding, but whether reported gains transfer across populations or survive negative controls is unclear. We benchmark LaBraM, EEGMamba, CBraMod, REVE, LEAD, BENDR, and BIOT on five clinical tasks across four datasets. Primary analyses use frozen linear probes with subject-disjoint LOSO or grouped five-fold validation. Because CAUEEG releases no patient identifiers, it is evaluated at recording level with a patient-disjoint sensitivity. ...

---

### 41. Limbomorphs

**Authors:** Alex Alvarez, Michael Levin

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23842v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23842v1)

**Summary:** Artificial life systems are typically defined by a set of dynamical rules over an environment, an agent, or both, from which lifelike patterns may emerge. Gifbreeder is an animated version of the interactive evolutionary computation (IEC) platform Picbreeder, and was initially created to generate visual art. Instead of encoding the agent or the environment, Gifbreeder genomes encode a spatiotemporal field and evolve through the user's aesthetic selection. The evolved expressions can sometimes re...

---

### 42. Provable Speedups From Dynamic Population Sizes in Evolutionary Algorithms for Multiobjective Optimization

**Authors:** Andre Opris

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23800v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23800v1)

**Summary:** This paper investigates the role of dynamic population sizes in evolutionary multi-objective optimization. Although such approaches are widely used in practice, their benefits remain poorly understood, and rigorous runtime analyses explaining when and why they help are still scarce. To address this, we introduce the bi-objective problem class CLIMB and analyze the runtime of GSEMO and the widely used NSGA-II on this problem. Our results show that allowing a dynamic population size for NSGA-II ca...

---

### 43. Benchmarking Zero-Shot LLM-Generated Parent Selection in Genetic Programming for Symbolic Regression

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23505v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23505v1)

**Summary:** Parent selection significantly affects exploration, exploitation, and complexity control in genetic programming (GP) for symbolic regression. It is unclear whether large language models (LLMs) can synthesize effective operators in a zero-shot setting without iterative meta-evolution. Here, zero-shot means that the model receives only the task description, with no reference operators or iterative feedback. In this work, we benchmark zero-shot synthesis of parent-selection operators across eight L...

---

### 44. Constraint-Bound Agnostic Bayesian Optimization: One Model for All Thresholds

**Authors:** Jin Wang, Xi Lin, Handing Wang

**Published:** 2026-07-26

🔗 [Paper](http://arxiv.org/abs/2607.23448v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23448v1)

**Summary:** Expensive constrained optimization problems in real-world industry design often involve constraint thresholds that are difficult to determine in advance. Engineers may need to adjust constraint thresholds to explore different feasibility-performance trade-offs, requiring solutions under a wide range of threshold settings. However, existing constrained Bayesian optimization methods treat each threshold configuration independently, leading to repeated optimization and failing to exploit the shared...

---

### 45. A genetic algorithm for student academic resource allocation

**Authors:** Ana F. Hernández, Andrej Franulic, Fernando Jiménez

**Published:** 2026-07-25

🔗 [Paper](http://arxiv.org/abs/2607.23316v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23316v1)

**Summary:** The optimal allocation of academic resources to individual students is essential for addressing learner diversity and fostering equitable educational outcomes. Within the framework of the Erasmus+ KA220-SCH project, this paper models the selection of educational materials for high school mathematics students as a 0--1 binary combinatorial optimization problem subject to strict study time constraints. Given the NP-hard complexity of the formulation, exact solution methods become computationally i...

---

### 46. Continuous surrogates versus threshold Boolean networks for modeling Arabidopsis ISR gene regulation

**Authors:** Gonzalo A. Ruz

**Published:** 2026-07-25

🔗 [Paper](http://arxiv.org/abs/2607.23289v1) | 📄 [PDF](https://arxiv.org/pdf/2607.23289v1)

**Summary:** Gene regulatory network modeling often requires balancing predictive accuracy and mechanistic interpretability. In this work, we compare continuous surrogate models and a discrete mechanistic model on the same \textit{Arabidopsis thaliana} induced systemic resistance (ISR) dataset, using both the raw continuous gene-expression measurements and their sign-binarized representation. The study considers eight defense-related genes measured over nine time points and evaluates two continuous predictor...

---

### 47. Sensitivity of hMPA to Controlled CEC 2017 Transformations

**Authors:** Grzegorz Sroka, Sławomir T. Wierzchoń

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22862v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22862v1)

**Summary:** The standard CEC 2017 benchmark applies bias, shift, and rotation simultaneously, confounding their individual effects on algorithmic behavior. We introduce a parameterized implementation that controls these transformations independently while preserving the original functions and transformation data. The framework diagnoses the hybrid Marine Predators Algorithm (hMPA), whose predicted-candidate mechanism depends on numerical objective values and coordinate-wise reconstruction. DSC and extended ...

---

### 48. Closed-Loop Generative Selection: Convergence, Memory, and Noisy Oracles

**Authors:** Konstantin Fackeldey, Christof Schütte

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22211v1)

**Summary:** Closed-loop generative selection has become a workhorse of computational drug discovery: a learned generative model proposes candidate molecules, a fitness oracle scores them, the best are kept, and the model is retrained on this elite set before the next round. Despite its wide use, the method has lacked a rigorous convergence theory, largely because retraining the model each round breaks the Markov property on which classical evolutionary-algorithm analysis relies. We develop a self-contained ...

---

### 49. On the Runtime Analysis of Reinforcement Learning Hyper-Heuristics

**Authors:** Pietro S. Oliveto, Zhenyu Wang, Peizhou Wu, et al.

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.22036v1) | 📄 [PDF](https://arxiv.org/pdf/2607.22036v1)

**Summary:** Selection Hyper-heuristics (HHs) automate algorithmic design by selecting from a set of low-level heuristics which one to apply at each stage of the optimisation process. Several impressive results have been recently rigorously proven regarding the performance of selection hyper-heuristics (HHs) for standard benchmark functions. However, the learning mechanisms employed by these HHs are considerably simplified compared to the machine learning techniques typically used in real world applications....

---

### 50. NeuroSynth: A Biologically Inspired Continual Reinforcement Learning Architecture for Mitigating Catastrophic Forgetting

**Authors:** Yash Kini

**Published:** 2026-07-24

🔗 [Paper](http://arxiv.org/abs/2607.28663v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28663v1)

**Summary:** Artificial Intelligence (AI) systems often perform well on isolated tasks but struggle under continual learning conditions, where training on new tasks can overwrite previously acquired knowledge, a failure mode known as catastrophic forgetting. Biological learning systems reduce this interference through complementary memory processes involving rapid hippocampal encoding and slower cortical consolidation. This study introduces NeuroSynth, a brain-inspired continual reinforcement learning archit...

---

## q-bio.NC

**50 papers**

### 1. Errorless Irrationality: A unified computational account of the inverse base-rate effect across predictive, observational, and unsupervised procedures

**Authors:** Lenard Dome, Andy J. Wills

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06149v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06149v1)

**Summary:** The inverse base-rate effect is a robust bias in how people resolve ambiguity between competing categories, and the most prominent theories explain it through prediction error. Across two experiments we progressively removed the elements of the predictive-learning design that supply such error signals: first by moving to observational learning, then to an unsupervised procedure in which category labels were not presented. The effect persisted--the irrational bias is independent of supervised lea...

---

### 2. Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05996v1)

**Summary:** Deep Belief Networks (DBNs) learn hierarchical generative models without class supervision. Here, we ask whether this purely unsupervised process nevertheless organizes internal representations according to the unknown data classes. We analyze successive layers of DBNs trained on MNIST, Fashion-MNIST, and KMNIST using the Generalized Discrimination Value (GDV), supervised probes applied only after training, a reconstruction-based measure of abstraction distance, effective dimensionality, and fre...

---

### 3. Convergent Evolution in Algorithmic Space

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05985v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05985v1)

**Summary:** In evolutionary biology, unrelated organisms can independently evolve similar structures when exposed to similar functional demands. Here we ask whether an analogous form of convergent evolution occurs during neural network training: do networks with different random initializations develop similar internal weight structures when trained on the same task? This question is technically nontrivial because hidden neurons can be arbitrarily permuted without changing the represented function, making d...

---

### 4. Complexity and Stability of Neural Activity Across Aging and Neurodegenerative Disease

**Authors:** Junjie Yu, Jianyu Zhang, Zian Pei, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05882v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05882v1)

**Summary:** Objective: EEG signals fluctuate continuously even within a fixed cognitive state, but an important question is whether the brain still reuses similar activity patterns to represent information over time. Methods: To address this, we model EEG as distributions of windowed activity patterns and quantify their temporal stability using Wasserstein distance, while intrinsic dimensionality captures representational complexity. Results: Across multi-task, lifespan, and clinical EEG datasets, we find t...

---

### 5. Two base rates, two weights: base-rate neglect has a second axis

**Authors:** Adam Y. Shavit

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05658v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05658v1)

**Summary:** Base-rate neglect is usually treated as one mistake: giving the prior too little weight. Turning the co-occurrences you see into a useful judgment, though, means correcting for two base rates, not one. The first is the familiar prior, how common the outcome is. The second is how common the cue itself is. Those are two separate mistakes, and a learner can make either one alone. Under-correcting the prior is classical base-rate neglect; under-correcting the cue is the cue-density effect of conting...

---

### 6. Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults

**Authors:** Christopher A. Johnson, Andria J. Farrens, Parastoo Ali Pour, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05635v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05635v1)

**Summary:** Transcutaneous spinal cord stimulation (tSCS) modulates spinal sensorimotor circuits primarily through activation of afferent networks. While prior work has emphasized locomotor performance and spinal excitability, how tSCS affects conscious proprioceptive perception and the extent to which such effects parallel changes in locomotor control remain unclear. We investigated the acute and training-related effects of tSCS on ankle proprioception and gait in unimpaired adults (n = 14), with an indepe...

---

### 7. From Local Learning to Global Prediction Through Layered Surprise Cascades

**Authors:** Andrew L. Smith, Linxing Preston Jiang, Jason K. Eshraghian, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05481v1)

**Summary:** Hierarchical predictive coding proposes a compelling hypothesis of brain computation, suggesting that the cortex builds layered predictions to minimize surprise. Yet most models rely on error-coding neurons or generative modeling of unclear biological plausibility. Here, we examine a biologically plausible framework in which the functional goals of predictive coding emerge from local contrastive learning and simple activity cancellation. Building on recent machine learning advances, we present a...

---

### 8. Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling

**Authors:** Sanjith Senthil, Rishidev Chaudhuri

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05464v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05464v1)

**Summary:** The pruning of network connections is key to brain function but, despite its importance, there exist few biologically-plausible pruning rules with demonstrated good performance. In this work we evaluate noise-prune, a recently introduced unsupervised local pruning rule for recurrent networks that uses noisy fluctuations to determine the importance of connections. Noise-prune has previously only been empirically tested on random networks without a specific computational function. We show that noi...

---

### 9. Toward a Dynamical Taxonomy of Insomnia: A Multiaxial Framework for Sleep-State Transitions and Architectural Failure

**Authors:** Alexander Poltorak

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05462v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05462v1)

**Summary:** Insomnia disorder is defined at the syndrome level, yet similar complaints can arise from different abnormalities in sleep regulation, state transition, state stabilization, spatial recruitment, architectural sequencing, and state perception. We propose a multiaxial dynamical framework whose principal contribution is organizational: a candidate profile is specified by the dynamical operation that fails, the sleep stage or boundary at which it fails, and its causal status. Objective sleep duratio...

---

### 10. The ethics of artificial intelligence in the life sciences: Universality, cultural diversity and an architecture of care

**Authors:** Jean-Pierre Changeux, Gustavo Deco, Morten L. Kringelbach

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05436v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05436v1)

**Summary:** The life sciences and health research have started to benefit from artificial intelligence, which raises ethical concerns that are real but, we argue, not special. Any science should be governed by values that rest on how the human brain is built and socialised rather than anything distinct to artificial intelligence. Importantly, the human brain has a different, much less costly computational architecture than these machines. This is achieved through the orchestration of a global neuronal works...

---

### 11. An entropic explanation of insistence on sameness in autism

**Authors:** Przemysław Śliwiński

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04616v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04616v1)

**Summary:** An information theory-based framework is proposed in attempt to explain insistence on sameness in autism as an instance of a general behavior pattern in which an individual tries to reduce surprise and uncertainty. It offers a new definition of autism as an impairment in which cognitive functions are restricted to discrimination, memorization and prediction of tangible properties of the environment. An analogy between insistence on sameness and constrained minimization of the entropy metric is o...

---

### 12. Time^2: A framework for the neural dynamics of visual perception

**Authors:** Laurent Caplette, Frédéric Gosselin

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04218v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04218v1)

**Summary:** Whenever we look at an object, we seem to perceive it immediately. However, this is not the case for two reasons. First, it takes hundreds of milliseconds for the brain to process visual information reaching the retina. Second, we have to look at an object for a certain amount of time to perceive it (and we typically look at it for hundreds of milliseconds) -- during that time, visual information is continuously received on our retinas. These facts together imply that visual information is both ...

---

### 13. Persistent homology broadens the controllable subspace in human structural connectomes

**Authors:** Carter Sale, Marco Coraggio, Mengsen Zhang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03181v1)

**Summary:** Network control theory applied to structural connectomes typically ranks brain regions as candidate driver nodes by their structural connectivity strength, and evaluates performance through scalar control energy. We test whether this framing captures the most relevant information about how driver-node selection shapes brain network control. We introduce an alternative criterion based on the persistent topological cycles in which each node participates---a measure of mesoscale integration that ca...

---

### 14. A Landau-Ginzburg Phenomenology of Sleep-Stage Transitions

**Authors:** Alexander Poltorak

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03000v1)

**Summary:** Sleep staging provides a reproducible clinical description, but it does not by itself explain why some boundaries are abrupt while others are graded, or why transition windows contain instability, synchrony, and apparent state coexistence. We develop a local Landau-Ginzburg phenomenology in which each boundary is represented by motion in an effective potential of a spatially extended, noisy, dissipative neural field. A latent cortical-ordering coordinate phi is inferred from prespecified EEG/PSG...

---

### 15. Modelling temporal dynamics of suicidal ideation and behaviour across pre- to early adolescence using a Markov framework

**Authors:** Sieun Lee, Ben Cardoen, Marianne Etherson, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02896v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02896v1)

**Summary:** Understanding the dynamics of suicidal ideation and behaviour in youth and the factors associated with transitions from thoughts to behaviours is critical for early identification, monitoring, and prevention. Using longitudinal self-report data from the Adolescent Brain Cognitive Development (ABCD) Study (n = 11,864) spanning ages 9 to 13 years, we developed a time-inhomogeneous discrete-time Markov chain framework to model transitions across eight states defined by suicidal ideation and behavio...

---

### 16. Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG

**Authors:** Jacob Kang, Jong-Hyeon Seo

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02804v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02804v1)

**Summary:** Recent studies have reported clearly identifiable dynamical changes in the high-frequency range of EEG signals recorded during specific stimuli, such as visual or auditory inputs, or in cases of brain disorders like epileptic seizures. In this study, we utilized Dynamic Mode Decomposition (DMD) to extract consistent and persistent dynamical changes in the high-frequency band from the signals of neurologically relevant EEG channels. High-frequency DMD modes were employed as features, composing a ...

---

### 17. Predictive Set Theory: A Generative Framework for Cognitive Architecture with Operationalized Core Mechanisms

**Authors:** Yiyang Yu

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02704v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02704v1)

**Summary:** Predictive processing theories portray the brain as a hierarchical prediction engine that minimizes prediction error, yet they lack operational definitions for the structure of a "prediction," the standardized response to a prediction error, and the mechanism that maintains consistency across successive updates. Bayesian cognitive science attempts to subsume all uncertainty under probabilistic belief updating, but it presupposes a closed hypothesis space and provides no generative account of how...

---

### 18. Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory

**Authors:** Zhaotian Gu, Jie Su, Weiwei Wang, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01947v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01947v1)

**Summary:** The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...

---

### 19. NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics

**Authors:** Zijian Dong, Jianxiong Zhou, Kwun Kei Ng, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.01773v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01773v1)

**Summary:** Forecasting human brain activity during naturalistic experience requires modeling how endogenous neural states evolve causally under continuous sensory drive. Existing brain encoding models instead frame this as stimulus-to-response regression without strict temporal constraints, allowing future stimuli to leak into current predictions. We introduce NeuroWorld, to our knowledge the first brain world model, which casts naturalistic brain functional dynamics prediction as stimulus-conditioned evol...

---

### 20. Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval

**Authors:** Ilia Semenkov, Daria Kleeva, Ivan Dakhtin, et al.

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01481v1)

**Summary:** Short segments of perceived speech can be retrieved from non-invasive magnetoencephalographic (MEG) recordings by deep networks trained with a CLIP-style objective against wav2vec 2.0 audio embeddings. Yet their weights do not map onto electrophysiological quantities, and it remains unclear which speech properties drive retrieval.   We build on a high-performing MEG-to-audio retrieval architecture but redesign both its front end and decoder. Its spatial attention operates on a flattened sensor l...

---

### 21. Statistical Mechanics of Learning on Product Wasserstein Manifolds

**Authors:** Srinivasa Rao P Vangmayi P Reddy

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01434v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01434v1)

**Summary:** Normally the statistical mechanics of learning treats constraints on weight distributions as restrictions that shrink the space of possible solutions. Therefore, it reduces model capacity. In this paper we would like to take a contrary approach, which, however, is based on the earlier work on distribution-constrained perceptrons. Rather than treating a prescribed weight distribution as a mere restriction, we propose that it defines the intrinsic geometry upon which learning naturally unfolds. We...

---

### 22. Data augmentation as a framework for modeling hippocampal contributions to generalization

**Authors:** Tyler Bonnen, Andrew Kyle Lampinen

**Published:** 2026-08-02

🔗 [Paper](http://arxiv.org/abs/2608.01297v1) | 📄 [PDF](https://arxiv.org/pdf/2608.01297v1)

**Summary:** The hippocampus plays a critical role in generalization, enabling us to flexibly repurpose prior experiences to perform novel tasks. Here we suggest that data augmentation---a machine learning strategy to improve generalization by refactoring prior experience---offers a useful framework to conceptualize and model hippocampal function. We begin by outlining how data augmentation operates across two timescales: the traditional ``offline'' setting, where refactoring training data yields more genera...

---

### 23. Deep Learning CNN and Recurrence Analysis for Alpha Gamma EEG Biomarkers in Fragile X Syndrome

**Authors:** Zag ElSayed, Payton Siekierski, Jack Yanchen Liu, et al.

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00835v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00835v1)

**Summary:** Fragile X Syndrome (FXS) is a neurodevelopmental disorder caused by reduced expression of fragile X mental retardation protein (FMRP), leading to disrupted synaptic plasticity, cortical hyperexcitability, and impaired network synchronization. Electroencephalography (EEG) provides a noninvasive window into these mechanisms and consistently reveals abnormalities in alpha (8 to 12 Hz) and gamma (30 to 100 Hz) oscillations that relate to inhibitory control, sensory processing, and cognition. This pa...

---

### 24. Recursive Gaussian Processes and the Bayesian Brain

**Authors:** Moumita Das, Dipanjan Ray, Sourabh Bhattacharya

**Published:** 2026-08-01

🔗 [Paper](http://arxiv.org/abs/2608.00503v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00503v1)

**Summary:** Predictive coding offers a powerful framework for cortical computation, yet scalable implementations that respect both Bayesian exactness and neurobiological constraints remain scarce. We bridge this gap by formally connecting predictive coding to Recursive Gaussian Processes (RGPs). RGPs employ a single Gaussian process \( g(t, \cdot) \) indexed by layer index and input value, preventing the representational collapse of standard deep Gaussian processes while allowing learnable cross-layer depen...

---

### 25. Mechanistic bridges from receptors to whole-brain dynamics: mean-field reductions, validity domains, and computational trade-offs

**Authors:** Yannael Bossard, Lehna Bekri, Alain Destexhe

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00306v2) | 📄 [PDF](https://arxiv.org/pdf/2608.00306v2)

**Summary:** Many pharmacological and pathological perturbations arise at molecular, synaptic, or cellular scales, but are observed through population and whole-brain signals. Cross-scale reductions must preserve relevant mechanisms while remaining tractable. This review asks which microscopic mechanisms remain explicit, interpretable, and testable after reduction, and what claims these models support. Using receptor-aware adaptive mean fields from the master-equation lineage as a worked case, we trace finit...

---

### 26. Cross-Task Dissociation in Frontier Vision-Language Model Theory of Mind

**Authors:** Kejia Zhang, Youran Sun, Chugang Yi, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00261v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00261v1)

**Summary:** Do frontier vision-language models present a coherent Theory-of-Mind (ToM) profile across tasks, matching the same human reference group, or does that profile fragment from one paradigm to the next? We evaluate a shared panel of nine frontier VLMs on two psychology-derived benchmarks: the Keysar Director Task (visual perspective-taking under egocentric interference) and the Frith-Happé animated triangles scored with the Castelli rubric (intention attribution from pure motion). On the Director Ta...

---

### 27. Dynamical principles of habituation across substrates and scales

**Authors:** Matthew Smart, Stanislav Y. Shvartsman, Martin Mönnigmann

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2608.00249v1) | 📄 [PDF](https://arxiv.org/pdf/2608.00249v1)

**Summary:** Habituation is a basic form of learning in which a system's response to repeated stimulation progressively diminishes but eventually recovers when the stimulus is withheld. Long studied in animals, it has increasingly been observed in unicellular organisms and non-living devices such as electronic circuits and neuromorphic materials, suggesting underlying dynamical principles that recur across domains. This review asks what those principles are: given qualitative constraints imposed by habituati...

---

### 28. Quantifying the cost of network computations to unpack structure-function relationships in the brain

**Authors:** Suman S. Kulkarni, Jason Z. Kim, Panagiotis Fotiadis, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29537v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29537v1)

**Summary:** The brain supports computations through coordinated patterns of activity on an underlying network. These networks---from microscale navigational circuits in insects to macroscale brain areas in humans---are organized in structured ways that are thought to support their function. We seek a unifying quantitative framework to understand how network structure shapes the computations a network can readily support. To do so, we frame computation as a goal-directed transition of activity and quantify i...

---

### 29. Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding for Cross-Site MDD Identification from rs-fMRI

**Authors:** Zhanpeng Zheng, Xiran Chen, Haiteng Jiang, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29531v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29531v1)

**Summary:** Cross-site identification of major depressive disorder (MDD) from resting-state functional magnetic resonance imaging (rs-fMRI) is hindered by inter-site distribution shifts and heterogeneous functional connectivity (FC) views. These views capture complementary neural relationships but exhibit distinct site biases and graph topologies, complicating alignment without sacrificing disease-relevant information or cross-view consistency. Existing studies largely treat multi-view connectome learning a...

---

### 30. Resource depletion accelerates rate learning but not composition learning in patch foraging

**Authors:** Zachary P. Kilpatrick, Ahmed El Hady

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29476v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29476v1)

**Summary:** Foraging is a universal animal behavior that has increasingly attracted the interest of both experimentalists and theorists. Most prior models assume an animal knows the distribution of resources in its environment, but this structure must be learned as the animal explores its environment. Foraging can thus be regarded as a hierarchical inference problem. We develop a normative Bayesian account of an agent learning a patchy environment while exploiting it, and show that resource depletion shapes...

---

### 31. metasignal: A Python Package for Comprehensive Metacognitive Analysis and Decision-Making

**Authors:** Saurabh Ranjan, Mukesh Makwana, Konstantina Sokratous, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29093v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29093v1)

**Summary:** Metasignal is an open-source Python package for signal detection theory (SDT) and metacognitive measurement. It implements the 17 metacognitive measures evaluated by Rahnev (2025), together with the reference variables d' (perceptual sensitivity), response criterion c (response bias), and mean confidence. The 17 measures comprise three meta-d' family estimates, meta-d', M-ratio, and M-difference; four nonparametric Type-2 measures, the Type-2 area under the receiver-operating-characteristic curv...

---

### 32. Critical Flicker Fusion Frequency As A Falsifiable Boundary Between Plastic And Non-Plastic Neural Systems

**Authors:** Natalia D. Rydzenska, Pawel J. Winklewski, Michal W. Blaszczyk-Niezgoda, et al.

**Published:** 2026-07-31

🔗 [Paper](http://arxiv.org/abs/2607.29068v1) | 📄 [PDF](https://arxiv.org/pdf/2607.29068v1)

**Summary:** Experience-dependent neural plasticity is fundamental to adaptive behaviour, yet certain perceptual abilities resist modification despite extensive training. Critical flicker fusion frequency (CFFF), the threshold at which flickering light appears continuous, is a foundational constraint in visual temporal processing that shows exceptional within-individual stability in adults, contrasting sharply with the highly plastic spatial abilities processed through the same cortical pathways. This review...

---

### 33. But What Behavior?

**Authors:** Robert C. Froemke

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28898v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28898v1)

**Summary:** What is a natural behavior? I argue that the study of natural behaviors is often the study of the spontaneous behaviors of animals placed in quantifiably different environments. For behavioral generalists such as rodents, humans, and many other species, there may be no such definable construct as a native habitat or natural behavior, due to their successful abilities and needs to rapidly adapt to a wide range of different ecosystems. Instead of prioritizing naturalness, it may be more essential ...

---

### 34. Bits per Spike as a Betting Game: An Interpretable Unit for Held-Out Log-Likelihood in Neural Data Analysis

**Authors:** Alex H. Williams

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28779v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28779v1)

**Summary:** Held-out log-likelihood is the standard currency for comparing statistical models of neural spike trains, and is often reported as bits per spike relative to a homogeneous Poisson baseline. The units of this metric are difficult to reason about: it is rarely obvious whether an improvement of, say, $0.34$ bits per spike is a large effect or a negligible one. This note develops an interpretation of held-out log-likelihood borrowed from game-theoretic statistics. A fitted model $Q$ is treated as a ...

---

### 35. Using Theory of Mind to Arbitrate between Social and Non-social Learning

**Authors:** Lance Ying, Ryan Truong, Joshua B. Tenenbaum, et al.

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28601v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28601v1)

**Summary:** Social learning is a powerful mechanism through which agents learn about the world from others. However, humans sometimes choose direct experience over social learning, which can carry time and cognitive resource costs. How do people balance social and non-social learning? We propose a Rational Mentalizing model of the decision to engage in social learning. This model estimates the utility of social learning by reasoning about another agent's goal and the informativeness of their future actions....

---

### 36. Stimulus-Evoked Network Dynamics in Human Cortical Organoids: From a Graph-Computational Framework to Repeated-Stimulation Depression

**Authors:** Esmaeil S. Nadimi, Vinay C. Gogineni, Jan-Matthias Braun, et al.

**Published:** 2026-07-30

🔗 [Paper](http://arxiv.org/abs/2607.28068v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28068v1)

**Summary:** Human cortical organoids provide an experimentally accessible model of early neural circuit formation, yet whether their activity reflects structured information processing rather than spontaneous synchronization is unclear. We developed a graph-computational framework to quantify stimulus-evoked propagation. This includes stimulus-conditioned functional graphs, a graph-constrained dynamical (graph-neural-network) model used as a system-identification tool, a biological message-passing principle...

---

### 37. MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification

**Authors:** Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.28681v1) | 📄 [PDF](https://arxiv.org/pdf/2607.28681v1)

**Summary:** Functional magnetic resonance imaging (fMRI) is a widely used technique for studying the brain. Recent methods that utilize graph neural networks (GNNs) for analysis of brain functional connectivity have shown great potential for the classification of brain disorders, such as Alzheimer's disease (AD). However, these methods often assume a preset number of functional modules across all subjects, which overlooks inter-subject variability. In addition, the discovered modules are rarely used to dire...

---

### 38. ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution

**Authors:** Christopher Warner, Jonas Mago, JR Huml, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.27308v1) | 📄 [PDF](https://arxiv.org/pdf/2607.27308v1)

**Summary:** We introduce ZUNA1.1, a 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction. ZUNA1.1 is capable of reconstructing variable length sequences of up to 30s, with an arbitrary number of EEG channels at arbitrary scalp locations, and can reconstruct arbitrary temporal intervals within channels in addition to reconstructing entire channels. We demonstrate that ZUNA1.1 performs at least on par with our earlier ZUNA1 model, while being far more flexible and capable of handling a ...

---

### 39. Artificial intelligence in deep brain stimulation for movement disorders: a systematic review and technology readiness assessment

**Authors:** Zohra Souei, Muhammad Mushhood Ur Rehman, Harith Akram, et al.

**Published:** 2026-07-29

🔗 [Paper](http://arxiv.org/abs/2607.26666v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26666v1)

**Summary:** Artificial intelligence (AI) is increasingly explored across deep brain stimulation (DBS) for movement disorders, yet whether current systems are approaching deployment remains unclear. To characterise their scope, validation maturity, and translational readiness, we systematically evaluated 239 peer-reviewed studies published between 2000 and 2025, assessing AI methods, validation practices, and barriers constraining clinical translation. Research was dominated by Parkinson's disease and subtha...

---

### 40. Pragmatic Reasoning in Design

**Authors:** Lance Ying, William Van Uitert, Tan Zhi-Xuan, et al.

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26322v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26322v1)

**Summary:** People can often understand and use novel artifacts after only a few interactions, suggesting that design choices communicate underlying affordances and causal structure. We propose a formal account of this process by framing cooperative, user-centered design as a cooperative game in which the user is the principal and the designer is an assistant. Inspired by prior work on pragmatic communication (e.g. RSA), our model treats a designer's design decisions as communicative signals and predicts us...

---

### 41. Three Failures of Pain Location: Why the Diagnostic Utility of Symptom Localization Is Not One Thing

**Authors:** Adam Y Shavit

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26297v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26297v1)

**Summary:** Patient-reported pain location is diagnostically decisive for some presentations and nearly uninformative for others. The prevailing account treats this as a single gradient of diagnostic utility governed by anatomical complexity. That explanation conflates three epistemically distinct failures of localization, each with its own mathematical structure, optimal instrument, and public-health consequence. In anatomical multiplexing (a), many structures share one location: a non-identifiable inverse...

---

### 42. A behavior-environment information loop drives sensory navigation

**Authors:** Kevin S. Chen, Matthew P. Leighton, Damon A. Clark, et al.

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26295v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26295v1)

**Summary:** As organisms navigate the environment to locate critical resources, their behavioral actions must be tightly coupled to their sensory inputs. Here, we introduce an information-theoretic framework that quantifies this coupling using transfer entropy, which measures information flow between sensory inputs and behavioral outputs. Information flow from sensory inputs to behavior defines a "reactive" component of a navigational strategy, whereas information flow from behavior to sensory inputs define...

---

### 43. Cognitive Convergence: Deep Similarities Between Large Language Models and Human Cognition

**Authors:** Chandra Sripada, Richard Lewis

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.26179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.26179v1)

**Summary:** LLMs are widely regarded as alien intelligences, systems whose cognitive operations are fundamentally unlike our own. Apparent similarities to human cognition are therefore often seen as the result of anthropomorphic projection. We argue that this framing is mistaken. LLMs clearly differ from humans in important respects, including their physical substrate, learning history, and the environments with which they interact. These differences make it all the more striking that contemporary LLM-based...

---

### 44. Phantom Evidence: How and Why Generative AI Manufactures False Positives in Science

**Authors:** Yukiyasu Kamitani, Ken Shirakawa

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.25991v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25991v1)

**Summary:** Four centuries ago Francis Bacon warned against the anticipations of nature, hasty generalization that wins assent on a few facts, and set against it the table of absence: checking that a property fails to appear where it should not. The demand was that looking convincing should not, on its own, count as evidence. Science has professed that demand ever since, while in practice letting persuasiveness do the work of evidence. It could be let to do so because making something persuasive was itself ...

---

### 45. GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling

**Authors:** Lluc Bono Rosselló

**Published:** 2026-07-28

🔗 [Paper](http://arxiv.org/abs/2607.25787v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25787v1)

**Summary:** The Information Dynamics of Music model (IDyOM) has played a central role in computational accounts of musical expectation by providing event-by-event estimates of uncertainty and surprise from symbolic musical sequences. However, its reference implementation is difficult to integrate with contemporary Python workflows, and its internal memory structures are not easily accessible for inspection or modification. We introduce GraphIDyOM, a graph-native Python reimplementation of IDyOM that represe...

---

### 46. Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference

**Authors:** Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25131v1)

**Summary:** Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visua...

---

### 47. CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification

**Authors:** Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25045v1) | 📄 [PDF](https://arxiv.org/pdf/2607.25045v1)

**Summary:** Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a ...

---

### 48. A Tuning-Free Variational Framework for Muscle Redundancy Resolution: Torque Fiber Proximal Dynamics with Active-Set Switching and EMG-Validated Activation Prediction

**Authors:** Morteza Ganji

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.25013v2) | 📄 [PDF](https://arxiv.org/pdf/2607.25013v2)

**Summary:** Muscle redundancy can be formulated as a constrained selection on a time-varying convex set of feasible activations. We introduce Torque Fiber Proximal Dynamics (TFPD), where activation evolves as the Euclidean projection of the previous state onto a convex polytope defined by torque equality and physiological bounds. TFPD is equivalent to a backward-Euler discretization of a sweeping process and a variational inequality with a maximal monotone normal cone operator. Within this framework, antago...

---

### 49. When Branch-Local Shunting Helps: A Gain-Load-Alignment Principle for Dendritic E/I Networks

**Authors:** Houman Safaai, Maceo Richards, Naeem Khoshnevis, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24990v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24990v1)

**Summary:** Biological neurons combine excitatory and inhibitory (E/I) activity on branched dendrites through shunting, in which inhibition divisively attenuates excitation. Whether this improves population readout over additive E/I integration of the same nonnegative inputs remains unclear. We introduce DendriNet, a trainable framework that varies integration rule, morphology, synaptic allocation, divisor locality, and dendritic nonlinearities. For population codes with multiplicative gain, a local lineari...

---

### 50. Synaptic clustering emerges from learning and supports covariance discrimination

**Authors:** Ilenna Simone Jones, Maceo Richards, Houman Safaai, et al.

**Published:** 2026-07-27

🔗 [Paper](http://arxiv.org/abs/2607.24503v1) | 📄 [PDF](https://arxiv.org/pdf/2607.24503v1)

**Summary:** Functional synapse clusters (FSCs) are synapses with correlated presynaptic activity that are colocalized on the same neuronal dendritic branch. FSCs have been observed after learning in cortical and hippocampal pyramidal neurons. However, previous efforts to ablate FSCs by pharmacologically blocking dendritic nonlinearities to establish causal necessity may have confounded effects. Therefore, whether FSCs are causally necessary for computation is unknown. Here, we attempt to isolate FSCs from t...

---

## stat.ML

**50 papers**

### 1. Scalable estimation of VARMA models

**Authors:** Daniel Paulin, Victor Elvira

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06340v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06340v1)

**Summary:** Vector autoregressive moving-average (VARMA) models have long been considered impractical beyond moderate dimensions: the likelihood is non-convex, the parametrization is identified only up to equivalence, and every evaluation costs a pass over the entire series. Yet their moving-average term captures with a few parameters what a pure autoregression matches only with many lags. We introduce an estimation framework that removes this computational barrier: each optimization iteration is independen...

---

### 2. Optimal Rates for Learning with Monotone Adversaries

**Authors:** Anay Mehrotra

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06337v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06337v1)

**Summary:** A monotone adversary observes an i.i.d. labeled sample and appends a finite number of further examples of its choice, every one of them labeled correctly by the target hypothesis. The learner sees a uniform shuffle of the combined sample and is scored on the original distribution. Every example is correctly labeled, but the insertions depend on the clean sample, so the combined sample is not exchangeable. Larsen, Pabbaraju, and Shetty, who introduced this model, showed that empirical risk minimi...

---

### 3. Learning Latent Memory States from Longitudinal Athlete Monitoring Data

**Authors:** Dae-Jin Lee

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06290v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06290v1)

**Summary:** We propose a new unit of analysis for longitudinal data: the Latent Memory Table. The scientific contribution is not the encoder. It is that table, treated as a reusable statistical object on the same footing as a matrix of principal-component scores, a table of estimated random effects, or a table of predicted probabilities. We estimate a statistical table that summarizes recent longitudinal history and is intended to be stored, queried, analysed and reused throughout the statistical workflow. ...

---

### 4. Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data

**Authors:** Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06288v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06288v1)

**Summary:** This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly quantifies the probability that a specific patient will experience extended survival time under treatment versus control. We reformulate IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts. The framework incorporates a pri...

---

### 5. The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity

**Authors:** Iosif Lytras, Nikolaos Makras, Sotirios Sabanis

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06283v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06283v1)

**Summary:** We study the problem of sampling from target distributions whose potentials are simultaneously non-smooth, subject to superlinear gradient growth, and non-convex. We introduce the Subgradient Tamed Unadjusted Langevin Algorithm (SG-TULA), a discretisation of the Langevin diffusion that operates directly on subgradients, without relying on computationally demanding smoothing procedures. To handle the superlinear regime, taming techniques are employed to produce a stable, explicit scheme. We deriv...

---

### 6. Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning

**Authors:** Farzana Nasrin

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06276v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06276v1)

**Summary:** Persistence diagrams (PDs) provide stable and interpretable summaries of multiscale topological structure. While substantial progress has been made in the statistical analysis of PDs, existing literature often treats diagrams as static objects and provide limited frameworks for probabilistic modeling and stochastic evolution on PD space. We introduce a reinforcement learning framework for stochastic dynamics on PD space, where diagrams evolve through topology aware local edit operations. The dyn...

---

### 7. Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification

**Authors:** Alex Buna, Shirley Xiaoqi Liu, Patrick Rebeschini

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06250v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06250v1)

**Summary:** In overparameterised classification, training data can be linearly separable even when the underlying distribution is not. In this setting, gradient descent (GD) on the logistic loss diverges in norm while converging in direction to a max-margin interpolating classifier, whose implicit bias can be statistically suboptimal. In this work, we show that early stopping can overcome this suboptimality: in a Gaussian mixture model with label-flipping noise, GD stopped at an appropriate oracle time achi...

---

### 8. Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal Prediction

**Authors:** Anton Conrad, Rustam Isaev, Denis Belomestny, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06206v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06206v1)

**Summary:** Conformal prediction endows arbitrary black-box predictors with finite-sample, distribution-free marginal coverage, yet marginal validity can hide severe covariate-specific miscalibration, while exact distribution-free conditional coverage is finite-sample unattainable. Randomly localized conformal prediction (RLCP) mitigates this gap by calibrating near the test point while preserving marginal coverage. Existing theory, however, lacks finite-sample guarantees for the realized localized set that...

---

### 9. Handling Missing Data in Probabilistic Regression Trees

**Authors:** Taiane Schaedler Prass, Alisson Silva Neimaier, Guilherme Pumi

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06195v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06195v1)

**Summary:** Probabilistic Regression Trees (PRTrees) are a smooth and consistent alternative to classical regression trees, producing continuous predictions through probabilistic split assignments. This paper extends the PRTree framework to accommodate missing predictor values directly during tree construction, eliminating the need for prior imputation. Three strategies are proposed, each exploiting the available information differently: a uniform-probability approach, a partial-observation approach, and a ...

---

### 10. Verifiable Regularity Criterion for Conditional Expectation Operators and Conditional Mean Embeddings with Applications to Nonparametric Regression, Bayesian Inverse Problems, and Koopman Operators

**Authors:** Maximiliano Hertel, Ilja Klebanov, Manuel Schaller, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06155v1)

**Summary:** Conditional expectation operators (CEOs) and their associated conditional mean embeddings (CMEs) play a central role across applied mathematics and machine learning, appearing in nonparametric regression, Bayesian inverse problems, and Koopman operator theory. A fundamental question is when a CEO maps a function space on $\mathcal{Y}$ into a prescribed function space on $\mathcal{X}$, particularly a reproducing kernel Hilbert space (RKHS). We show that such mapping properties are characterized b...

---

### 11. Deep Generalised Mixed Models: a Novel Neural Network Structure for Analysing Hierarchical Data

**Authors:** Nina van Gerwen, Dimitris Rizopoulos, Manon Hillegers, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05930v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05930v1)

**Summary:** The experience sampling method (ESM) is a longitudinal research design where participants report their thoughts, emotional states and behaviours multiple times a day. Our work is motivated by such data collected by the GrowIt! app, which was released to investigate daily emotions among adolescents during the COVID-19 pandemic. Current procedures to analyse ESM data face various challenges. While standard statistical techniques may not scale well to a high-dimensional setting, machine learning pr...

---

### 12. Fuzzy network jump models for soft dynamic clustering of graph-structured data

**Authors:** Federico P. Cortese

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05786v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05786v1)

**Summary:** We introduce a fuzzy network jump model for clustering time-varying observations indexed by the nodes of a weighted graph. The framework allows flexible graph representations with spatial and temporal regularization promoting smooth soft cluster assignments across connected nodes and consecutive time points. Estimation is performed through an efficient alternating optimization scheme that exploits the quadratic structure of the regularization terms. A simulation study covering different levels o...

---

### 13. Structured Dimension-Matched Joint Variational Transdimensional Inference

**Authors:** Pingping Yin, Xiyun Jiao

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05607v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05607v1)

**Summary:** Bayesian model selection couples a discrete model indicator with a model-specific continuous parameter space. We introduce structured dimension-matched variational transdimensional inference (SM-VTI) for finite enumerable model spaces. A rooted construction graph expresses a model as a sequence of local stop/child decisions. Each typed edge compiles a declared scientific parent-child edit into an exact native-coordinate dimension-matching lifting; an edge-conditioned flow then learns the residua...

---

### 14. Innovation-Residual Auditing of Autonomous Analysis Agents: Localization, Detection Limits, Error Control, and Identifiability

**Authors:** Ahmed Hassoon, Mark Dredze

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05490v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05490v1)

**Summary:** Autonomous agents now carry out entire data analyses, selecting cohorts, joining tables, and fitting models with little step-by-step supervision. When such an analysis turns out to be wrong, someone must determine which operation caused it. A recent approach does this without any labelled mistakes, learning instead from analyses known to be sound and flagging operations that depart from what that model predicts; how reliable such audits are has not been studied. This paper supplies that analysis...

---

### 15. Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty

**Authors:** Zhen Zhang, Amr Alanwar

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05454v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05454v1)

**Summary:** Probabilistic prediction heads in neural networks typically output either a Gaussian mixture or a single conformal region. Neither separates the distinct sources of uncertainty often present in real prediction tasks: a discrete choice among modes, bounded systematic drift within the chosen mode, and irreducible stochastic noise. We introduce the Hybrid Probabilistic Zonotope (HProbZ), an output head that represents these three sources as binary, bounded, and stochastic generators of a zonotope, ...

---

### 16. Risk-Aware Quantile Learning for Personalized Dynamic Treatment Regimes

**Authors:** Chunyin Lei, Annie Qu

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05434v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05434v1)

**Summary:** Sequential clinical decision-making often involves more than maximizing average efficacy. Clinicians may need to simultaneously optimize clinically relevant tails of the outcome distribution, control treatment-related risk, and choose among multiple treatment options. Existing quantile dynamic treatment regime (DTR) methods capture distributional features of treatment outcomes but remain largely restricted to efficacy-only objectives and binary treatments. To address these limitations, we propos...

---

### 17. The Loss Does Not See the Basis, but Adam Does

**Authors:** Devender Singh

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05136v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05136v1)

**Summary:** Gradient descent on a factored model $W = UV^\top$ is implicitly biased toward low-rank solutions, while Adam, starting from the same small initialization, is not. We trace the difference to the gauge symmetry of the loss, its invariance under $(U, V) \mapsto (UQ, VQ)$. Gradient flow's low-rank mechanism is available to an optimizer only if that optimizer is gauge-equivariant, a condition necessary for the transfer but not sufficient for low-rank recovery. Gradient descent, momentum, "shared-sca...

---

### 18. SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant

**Authors:** Adel Javanmard, David P. Woodruff, Vahab Mirrokni

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05127v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05127v1)

**Summary:** Achieving local differential privacy in distributed optimization while maintaining low communication cost remains challenging. Existing vector quantization methods, such as vqSGD, use high-dimensional geometric constructions but incur unfavorable dimension-dependent variance. In this work, we propose Subsampled Stochastic TurboQuant (SSTQ), a framework that combines overcomplete equal-norm tight frames, coordinate subsampling, and privacy-aware one-dimensional quantization. SSTQ includes two var...

---

### 19. Stable Density Ridges: Consistency and Convergence of Subspace Constrained Mean Shift

**Authors:** Wanli Qiao

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05112v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05112v1)

**Summary:** The Subspace Constrained Mean Shift (SCMS) algorithm is a popular nonparametric method for extracting density ridges, which serve as a low-dimensional representation of high-dimensional data. It is a widely held belief in the literature that SCMS trajectories converge to the classical density ridge, which we call the "static ridge", defined via the density gradient and the eigenvalues and eigenvectors of the density's Hessian. In this paper, we demonstrate that this assumption does not hold in g...

---

### 20. Representational separation between unitary and channel quantum generative models via shared classical randomness at shallow depth

**Authors:** Arunava Majumder, Marius Krumm, Hendrik Poulsen Nautrup, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05110v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05110v1)

**Summary:** Near-term quantum hardware limits circuit depth and often imposes geometrically local connectivity for quantum generative models, restricting the output distributions accessible to shallow unitary Born models. Introducing stochasticity into a unitary quantum Born model can improve the empirical generative performance of the resulting channel model and, for a restricted small-scale architecture, has been proven to represent a strictly larger family of distributions than its unitary counterpart. H...

---

### 21. Canonical Joint Energy-Based Model on CIFAR-10: failure modes and practical indistinguishability of Predictor-Corrector and SGLD samplers

**Authors:** Dmytro Knopov

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05025v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05025v1)

**Summary:** Joint Energy-Based Models (JEM) unify classification and generation within a single network and support out-of-distribution (OOD) detection. Canonical JEM training relies on stochastic gradient Langevin dynamics (SGLD); a theoretically motivated alternative, the Predictor-Corrector (PC) sampler, has not previously undergone a systematic replication test on the canonical model. We reproduce canonical JEM on WideResNet-28-10 without normalisation layers on two independent runs and test whether PC ...

---

### 22. Algorithm-Driven SVARs: Navigating the Wilderness of Big Data

**Authors:** Yucheng Yang, Tao Zha

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05017v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05017v1)

**Summary:** Every SVAR result is conditional on two choices: the restrictions that identify the shock and the variables on which they operate. The literature disciplines the first; the second is chosen by hand. We develop a Bayesian methodology that constructs information sets, uses an out-of-sample criterion, and retains the largest system it admits. Under recursive identification, output rises with housing production rather than household credit alone. For monetary policy, an anchor-free joint Bayesian pr...

---

### 23. Stochastic Emulation using Generalized Stratified Sampling for Performance-Based Risk Optimization of Structures

**Authors:** Isabela D. Rodrigues, Seymour M. J. Spence, Henrique M. Kroetz, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05006v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05006v1)

**Summary:** Metamodels are instrumental in reducing the computational burden associated with nested reliability analyses and optimization loops in Performance-Based Risk Optimization (PBRO) of structures under stochastic loads. In this context, stochastic emulators are particularly useful because they approximate response distributions while accounting for the intrinsic stochasticity of the simulator. Among these methods, Stochastic Polynomial Chaos Expansion (SPCE) is especially attractive because it does ...

---

### 24. A Unified Causal Inference Framework for the Desirability of Outcome Ranking Paradigm in Benefit-Risk Evaluation

**Authors:** Yuan Feng, Shiyu Shu, Yixin Fang, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05244v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05244v1)

**Summary:** We developed a unified covariate-adjusted causal inference framework for estimating the desirability of outcome ranking (DOOR) probability for benefit-risk evaluation in randomized trials and observational studies. The framework expresses the DOOR probability as a bilinear functional of the marginal ordinal outcome distributions under the two treatment strategies, estimates conditional ordinal distributions through sequential risk-set hazards, and derives the efficient influence function (EIF) o...

---

### 25. Marginal Matching Does Not License Factorized Sampling: Auditing Conditional Style Leakage in Factorized Generative Models

**Authors:** Duong Bach, Hai Nguyen Hong, Cuong Do

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05243v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05243v1)

**Summary:** Factorized generative models commonly regularize a latent style variable z_s by matching its marginal distribution to a fixed Gaussian prior and interpret this as evidence that the style representation is independent of class information. We show that this interpretation is incorrect. Matching only the marginal distribution places no constraint on the class-conditional distributions, allowing the latent style to remain highly predictive of the label despite appearing perfectly Gaussian in aggreg...

---

### 26. Variational Bounds for Perceptron Learning from Structured Data

**Authors:** Francesco Camilli, Pierluigi Contucci, Federica Gerace, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04882v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04882v1)

**Summary:** We introduce a variational approach to a finite-temperature continuous-spin perceptron trained on a Gaussian mixture. The model allows for a broad class of concave utilities and log-concave separable prior measures on the spins. By combining the interpolation method with log-concavity and concentration estimates, we derive lower and upper minimax variational bounds for the limiting quenched pressure. Remarkably, the two bounds differ only in the order of optimization of two variational parameter...

---

### 27. Nonparametric Goodness-of-fit Testing under Covariate Shift

**Authors:** Zhen Hou, Dong Xia

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04860v2) | 📄 [PDF](https://arxiv.org/pdf/2608.04860v2)

**Summary:** This paper develops procedures for nonparametric goodness-of-fit testing under covariate shift, where labelled data are drawn from a source population but goodness-of-fit is evaluated for a target population. The distribution mismatch is quantified by either a bounded moment condition or a sub-exponential tail condition on the target-to-source density ratio. Our method combines truncated importance-weighting kernel ridge regression with a multiplier bootstrap to construct confidence sets for the...

---

### 28. Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown Manifolds

**Authors:** Yizhu Wang, Mu Niu, Xiaochen Yang

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04827v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04827v1)

**Summary:** We introduce the Intrinsic Hybrid Latent Diffusion Model (ILDM), a generative framework that integrates probabilistic dimensionality reduction with geometry-aware diffusion on unknown manifolds. While diffusion models (DMs) have achieved state-of-the-art results in high-dimensional data synthesis, they rely on large training datasets and ignore intrinsic geometric structure. Latent diffusion models (LDMs) address the high dimensionality by learning a latent space, but they typically impose a Euc...

---

### 29. Quality Diversity for Reliable Data Driven Time-Use Optimization

**Authors:** Aneta Neumann, Ty Stanford, Dorothea Dumuid, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05230v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05230v1)

**Summary:** The daily allocation of the finite 24-hour time budget is strongly associated with physical, mental, and cognitive health. While predictive models can estimate the relationship between time-use compositions and health outcomes such as body mass index, life satisfaction, and cognition, most optimization approaches focus only on maximizing expected benefit and do not consider the uncertainty inherent in data-driven prediction. Ignoring uncertainty in health-related decisions can lead to unrealisti...

---

### 30. Personalized Federated Sparse Adaptation of Time-Series Foundation Models

**Authors:** Priyanka Nihalchandani, Naman Srivastava, Varun Ojha, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04695v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04695v1)

**Summary:** Federated adaptation of time-series foundation models (TSFMs) is attractive for building energy forecasting because meter data are private, distributed, and highly non-IID. However, a single parameter-sharing strategy is unlikely to serve all pretrained TSFMs or building clients: fully shared adapters can suppress building-specific temporal behavior, while fully local adaptation discards cross-building transfer. We propose a personalized federated sparse adaptation framework with a heterogeneous...

---

### 31. Automatic Statistical Test for Rationally Expressible Algorithms by Selective Inference, with Applications to Feature Selection

**Authors:** Teruyuki Katsuoka, Tomohiro Shiraishi, Shuichi Nishino, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04667v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04667v1)

**Summary:** Selective inference (SI) provides statistically valid $p$-values for hypotheses selected by applying an algorithm to the data, correcting for the bias that arises when the same data are used both to select and to test a hypothesis. Developing an SI procedure for a new algorithm, however, has required an expert to derive, and then implement, the selection event, i.e., the conditions under which the hypothesis is selected. Repeating this specialized effort for every new algorithm is why exact SI h...

---

### 32. An entropic explanation of insistence on sameness in autism

**Authors:** Przemysław Śliwiński

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04616v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04616v1)

**Summary:** An information theory-based framework is proposed in attempt to explain insistence on sameness in autism as an instance of a general behavior pattern in which an individual tries to reduce surprise and uncertainty. It offers a new definition of autism as an impairment in which cognitive functions are restricted to discrimination, memorization and prediction of tangible properties of the environment. An analogy between insistence on sameness and constrained minimization of the entropy metric is o...

---

### 33. Discretization and Statistical Consistency of Functional Flow Matching

**Authors:** Lennon J. Shikhman

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04531v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04531v1)

**Summary:** Functional flow matching is posed on distributions of functions but implemented from finitely many coefficients or point values. Under scattered or adaptive refinement, the resulting conditioning sigma-algebras need not be nested, so martingale convergence does not justify the sensor limit. We prove strong $L^2$ convergence of finite conditional velocity targets for every strongly consistent sequence of finite-rank reconstructions, with quantitative bounds for orthogonal projections and a point-...

---

### 34. An adaptive split-combine Gaussian mixture filter for nonlinear and multimodal state estimation

**Authors:** San Kim, Won Chang, Daniel B. Forger, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04430v2) | 📄 [PDF](https://arxiv.org/pdf/2608.04430v2)

**Summary:** Filtering combines model predictions with measurements to estimate the probability density function (PDF) of a system state over time. The PDF often becomes highly asymmetric and even multimodal in nonlinear systems with oscillatory or chaotic dynamics. Such non-Gaussian features violate the single-Gaussian assumption underlying Kalman-type filters. To address this problem, Gaussian mixture filtering has been proposed. However, accurately propagating mixture components and adaptively adjusting t...

---

### 35. Incremental Aggregation on the Grassmannian for Asynchronous Eigenspace Computation

**Authors:** Xiaolu Wang, Jiang Hu, Hoi-To Wai

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04406v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04406v1)

**Summary:** We study asynchronous optimization for finite-sum eigenspace computation in heterogeneous distributed systems. The theoretical foundations for asynchronous eigenspace computation remain scarce, with existing approaches offering limited coverage of dynamics directly on the Grassmannian under stale information. In this paper, we propose a Grassmannian incremental aggregation method that refreshes only arriving components and reuses cached gradients, retaining low per-update cost without global syn...

---

### 36. Non-asymptotic implicit bias of logistic regression at early-stage gradient descent dynamics

**Authors:** Han Bao

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04382v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04382v1)

**Summary:** Gradient descent has been of particular interest in modern machine learning beyond sole focus on optimization. Implicit bias emerging from optimization, though not being encoded by the learning objective, often prevents from overfitting to spurious patterns. A typical instance is the max-margin implicit bias of a linear classifier, widely established for exponentially tailed loss functions. Even after having a given dataset separated, the parameter vector continues to evolve towards the max-marg...

---

### 37. iStructTab: Structured Feature Sequencing for Multimodal Learning of Image and Tabular Data

**Authors:** Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Gyawali, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04348v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04348v1)

**Summary:** Multimodal learning of images and tabular data is often impaired by ineffective representations, resulting in redundancy, dispersion, and generalization problems. To tackle this challenge, we introduce Graph-Enhanced Descriptor Sequencing (GEDS), a structured feature sequencing algorithm grounded in principles from the Column Permutation Problem (CPP). GEDS refines statistical descriptors of the features through similarity graph-based computations, systematically determining an effective feature...

---

### 38. Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO

**Authors:** Mengyu Xu, Qiaoxin Yang, Zhihan Liu, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04339v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04339v1)

**Summary:** Large language models are increasingly used for information seeking, yet semantically equivalent questions phrased in different ways can receive answers of considerably different quality. System prompts are widely employed to steer response behavior, but they are typically optimized for average-case quality, so some question phrasings may still receive incomplete or low-quality answers. To address this, we formulate a constrained mixed-strategy GroupDRO framework for system-prompt selection. Ins...

---

### 39. Achieving First-Order Statistical Improvements in Data-Driven Optimization: From No-Free-Lunch to Amplified Decision Perturbation

**Authors:** Henry Lam, Tianyu Wang

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04312v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04312v1)

**Summary:** Recent proliferation of data-optimization integration has led to a range of methods that aim to improve the statistical performance of data-driven optimization decisions. However, while many of these methods are motivated intuitively from a robustness or regularization perspective, their resulting statistical benefits are often unclear and, even if available, are established on a case-by-case basis. We provide a systematic dissection of data-driven optimization formulations using the view of "di...

---

### 40. ArborEnum: Decision Tree Rashomon Sets over Continuous Features

**Authors:** Zakk Heile, Hayden McTavish, Margo Seltzer, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04310v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04310v1)

**Summary:** The Rashomon effect describes the phenomenon that many models can achieve nearly equivalent performance on the same learning task, with significant ramifications for robustness, feature importance, and customizability. These use cases motivate the computation of Rashomon sets: the set of all models whose regularized loss is near-optimal. Decision trees are one of the few model classes for which Rashomon sets can be fully enumerated, but this computation has always been conditional on a binarizat...

---

### 41. Sample Complexity of Multicalibration for Multilevel Properties

**Authors:** Jiuyao Lu, Krishnakumar Balasubramanian, Aleksandr Podkopaev, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04288v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04288v1)

**Summary:** Calibration requires a predictor to be unbiased after conditioning on its own predictions. Multicalibration asks for this guarantee simultaneously across a collection of groups. Many prediction tasks ask for several related features of the same conditional outcome distribution: variance is defined relative to the mean, skewness relative to both mean and variance, and conditional value at risk relative to a quantile. We study multicalibration for a sequence of $k$ properties in which each propert...

---

### 42. When Is a Conformal Guarantee Fair? Auditing Silent Subgroup Under-Coverage in Alzheimer's Disease Longitudinal Prediction

**Authors:** Lujia Zhong, Xinkai Wang, Shuo Huang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04254v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04254v1)

**Summary:** Longitudinal prediction of Alzheimer's disease biomarkers increasingly informs clinical decisions, and a forecast is only useful if it also reports how much to trust it. Conformal prediction supplies this by wrapping any forecaster in a prediction band with a finite-sample coverage guarantee under exchangeability. However, standard population-level conformal prediction guarantees only marginal coverage and may mask substantial under-coverage within clinically important subgroups. We introduce a ...

---

### 43. Multimodal Alignment Through Joint Kernel Entropic Gromov--Wasserstein Optimal Transport

**Authors:** Yixuan Florence Wu, Yilun Zhu, Naichen Shi

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04234v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04234v1)

**Summary:** We study the problem of aligning data from multiple modalities into a shared representation space, focusing on settings where strong pretrained unimodal encoders are available but cross-modal paired data are scarce. We propose a structure-preserving alignment framework, joint kernel entropic Gromov--Wasserstein Optimal Transport (JK-EGW), which maps multiple modalities into a common latent space by minimizing a quadratic optimal transport objective. JK-EGW leverages fine-grained similarity relat...

---

### 44. Information-Geometric Forward Policy Training in GFlowNets

**Authors:** Yordan Raykov, Rodrigo Veiga

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03967v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03967v1)

**Summary:** Generative Flow Networks (GFlowNets) have emerged as a flexible framework for amortised inference over discrete and mixed discrete-continuous objects, requiring only an unnormalised target density specified through a reward. In this work, we formulate forward-policy training in GFlowNets through the information geometry of the induced trajectory sampler. Treating the forward policy as an induced trajectory sampler, we show that its intrinsic first-order geometry is given by the Fisher-Rao metric...

---

### 45. Robust Low-Tubal-Rank Tensor Completion under Cross-Concentrated Sampling

**Authors:** HanQin Cai, Longxiu Huang, Jing Qin, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03928v2) | 📄 [PDF](https://arxiv.org/pdf/2608.03928v2)

**Summary:** Tensor cross-concentrated sampling (t-CCS) bridges entrywise sampling and t-CUR slice-wise sampling by observing entries only within selected horizontal and lateral slices. Existing t-CCS completion methods, however, assume that the observations are free of gross corruption. In this work, we study robust recovery of a third-order low-tubal-rank tensor from partial t-CCS observations contaminated by sparse, arbitrarily large outliers. We propose Robust Iterative t-CUR (R-ItCUR), a tensor-native a...

---

### 46. Trajectory inference via Acceleration Matching

**Authors:** Bartolo Dazzini, Giovanni Conforti, Alain Durmus, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03916v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03916v1)

**Summary:** Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories that best resemble and interpolate the data. Existing algorithms exhibit computational challenges: they either rely on preprocessing subroutines to enforce smoothness or on simulation-based training objectives, both of which can be expensive. In order to overcome these limitations, we propose a new ...

---

### 47. Confidence Horizons

**Authors:** Chase Mathis, Ian Waudby-Smith

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03889v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03889v1)

**Summary:** Anytime-valid inference enables analysts to continuously monitor their data and stop experiments early. However, the majority of these methods incur a certain conservativeness by remaining valid on infinite time horizons. In practice, a bound on the horizon may be imposed due to budgetary, practical, or ethical constraints. In this paper, we ask the question: "Is it possible to obtain sharper large-sample anytime-valid inference by forgoing validity beyond some finite time horizon?". We provide ...

---

### 48. Divide-and-Conquer: Towards Generalizable Amortized Bayesian Inference for the Drift Diffusion Model

**Authors:** Yufei Wu, Shanqing Gao, Andreas Voss, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03566v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03566v1)

**Summary:** The drift diffusion model (DDM) is a cornerstone of cognitive decision-making research. Although numerous estimation methods exist, researchers continue to seek inference approaches that are both fast and flexible across diverse study designs. Amortized Bayesian inference (ABI) can provide nearly instantaneous inference for complex stochastic models like the DDM, but neural networks trained for one study design cannot generalize to others. In this paper, we propose a divide-and-conquer framework...

---

### 49. When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs

**Authors:** Omatharv Bharat Vaidya, Connor Thomas Jerzak, Zayne Rea Sprague, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03506v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03506v1)

**Summary:** Self-consistency assumes the most frequent answer among sampled reasoning traces is the most reliable, but this can fail in causal reasoning: samples often repeat the same confounding error, and votes fragment across multiple valid answers, letting an invalid answer win despite a valid minority trace. We introduce CALVER (Causal Axiom-Level VERification), a training-free symbolic verifier that scores structured traces against Pearl's causal criteria, including -separation, backdoor adjustment, a...

---

### 50. A fully nonlinear structural vector autoregressive model identified via independent innovation analysis

**Authors:** Savi Virolainen

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03486v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03486v1)

**Summary:** We develop a fully nonlinear structural vector autoregressive framework in which the contemporaneous structural mapping may be nonlinear and non-additive. Identification is achieved by exploiting variation in the conditional distributions of the mutually independent structural shocks induced by an observed exogenous variable. Specifically, a general contrastive learning framework that makes use of this variation together with the assumed exponential-family structure is employed to recover the sh...

---

