# arXiv Daily Digest - 2026-09-02

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation

**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01603v1)

**Summary:** Evaluating software engineering agents on realistic benchmarks is costly, since each task may require multi-step code exploration, modification, and test execution. Existing efficient evaluation methods select representative subsets to estimate full-benchmark performance, but are largely result-only: they fit historical pass/fail response matrices or static task semantics, discarding how agents solve problems. We propose PTA-IRT, a Privileged Trajectory-Aware Item Response Theory framework that ...

---

### 2. Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation

**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01601v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01601v1)

**Summary:** The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context. Since real-world repositories often exceed the input length limits of LLMs, existing approaches commonly adopt retrieval-augmented generation (RAG) to provide repository-specific context. Despite improving repository-context retrieval, existing methods typically provide context as task-level support, without explicitly identifying th...

---

### 3. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

**Authors:** Damien Sileo, Dimitri Kachler

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01600v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01600v1)

**Summary:** Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local plugin change can propagate through dependencies and cleanup. We introduce CordisBench, a 1,200-question benchmark of this lifecycle reasoning. It combines a controlled formal setting with programs executed against Cordis, a runtime that manages component dependencies and cleanup, and asks models to identify affected components, predict state af...

---

### 4. The Rise of Verbal Reinforcement Learning

**Authors:** Kshitij Tayal, Arun Sharma, Genta Indra Winata, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01597v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01597v1)

**Summary:** Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{La...

---

### 5. Mechanism Design for Alignment and Control

**Authors:** Dirk Bergemann, Andrew Koh, Stephen Morris

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01595v1)

**Summary:** We develop a framework for mechanism design with AI agents whose alignment (preferences) and capabilities (feasible actions and information) are unknown. We want such agents to act on our behalf so mechanisms must incentivize both honesty and obedience. A one-sided imitation structure---capabilities can be concealed but not counterfeited---yields a revelation principle, a characterization of implementable policies via nested cyclical monotonicity, and conditions under which eliciting higher-orde...

---

### 6. Designing Proactive Thought Partners for Writing

**Authors:** Chao Zhang, Abe Davis, Chih-Wei Chen, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01588v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01588v1)

**Summary:** Writing involves diverse cognitive activities, from ideation to revision, and writers' needs vary across individuals and moments. Proactive AI promises to provide the right support at the right time, yet existing proactive tools largely focus on generic textual assistance, such as autocomplete. This paper studies the design space of proactive thought partners: AI agents that proactively offer customizable, higher-level cognitive support during writing. We instantiated this concept in a technolog...

---

### 7. Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs

**Authors:** Jingtan Wang, Arun Verma, Xiaoqiang Lin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01573v1)

**Summary:** How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad trends (e.g., SFT dominates in low-data regimes), lacks a principled allocation framework, and does not examine whether the optimal ratio transfers across model sizes. We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal...

---

### 8. Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers

**Authors:** Matteo Merler, Giovanni Bonetta, Davide Zago, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01567v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01567v1)

**Summary:** Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertai...

---

### 9. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification

**Authors:** Manish Gupta, Chaitanya Giri, Jayasimha Talur

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01564v1)

**Summary:** Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the ...

---

### 10. H3-World: Turning Language Understanding into World Control

**Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01560v1)

**Summary:** We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control. MiniMax-H3, for example, already supports zero-shot control of character behavior and camera motion through natural-language instructions. Building on this, H3-World turns this coarse language interface into precise, temporally grounded world contr...

---

### 11. Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories

**Authors:** Nabira Rashid, Manolis Kellis

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01556v1)

**Summary:** We evaluate embedding retrieval where surface form and meaning are pulled apart on purpose: retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol, competition mathematics (MathNet-Retrieve; 500 queries, 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries, 336 trajectories). In mathematics the failure is complete: strict Hit@1 at the heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% C...

---

### 12. BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net

**Authors:** Marven Sherif, Amgad Elmasry, Youssef Ghazal, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01554v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01554v1)

**Summary:** Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, P...

---

### 13. Can LLMs Discover Scientific Laws in Real and Parallel Worlds?

**Authors:** Yiming Huang, Ziche Liu, Zhuohang Wu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01552v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01552v1)

**Summary:** Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constraints. As LLM capabilities advance and their role in AI for Science expands, it remains an open problem whether they can genuinely discover scientific laws and how this ability should be evaluated. Existing evaluations, however, often either simplify discovery through synthetic settings or reuse publ...

---

### 14. A Mathematical Theory of Reusable Neural Bases for Network Compression

**Authors:** Binshuai Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01550v1)

**Summary:** As large AI models become increasingly prevalent across a wide range of applications, memory cost has become a critical bottleneck in both training and inference. To mitigate this issue, we introduce the Linear Reusable Neural Bases Architecture (LRNBA), a novel framework aimed at improving parameter efficiency and reducing memory cost. Inspired by recurrent neural network (RNN) designs, the core idea of our approach is to represent each network block as a linear combination of a shared set of n...

---

### 15. Can LLMs Design Video Coding Tools? A Case Study on Planar Mode

**Authors:** Yingwen Zhang, Meng Wang, Liqiang He, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01535v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01535v1)

**Summary:** This paper explores whether large language models (LLMs) can design video coding tools, a highly challenging task due to the intricate algorithmic coupling of tool modifications. In particular, we present an empirical case study on the Planar mode, a long-standing intra prediction tool in video coding standards. Our experiments operate within a generation-and-evaluation loop, with the LLM generating new Planar predictors, encoder trials evaluating their coding performance, and the LLM re-generat...

---

### 16. EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation

**Authors:** Qing Zhao, Haowei Li, Weijian Deng, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01526v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01526v1)

**Summary:** Scientific agents must learn not only how to reason, but also what to believe. However, existing LLM agents typically express scientific hypotheses in free-form text, leaving their beliefs implicit and difficult to test or revise. We introduce EvoSCM, which equips scientific agents with explicit structural causal models that evolve as new experimental evidence is collected. EvoSCM maintains a population of competing SCM hypotheses, each encoding a candidate causal explanation of the environment,...

---

### 17. Relational-Core Graph Analytics Querying graphs at SQL scale, and why the node/edge model is a performance tax, not a truer picture of connected data

**Authors:** Gene Zhang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01525v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01525v1)

**Summary:** A durable assumption holds that graph analytics requires a purpose-built graph engine, and that relational systems are ill-suited to connected data. We argue the opposite for the workloads enterprises actually run. A columnar relational engine fronted by a graph query language matches or exceeds native graph engines on analytical graph queries, and - decisively - scales past the point where in-memory graph engines fail. We further argue that the node/edge property graph is not a more faithful mo...

---

### 18. When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation

**Authors:** Peiying Zhu, Sidi Chang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01519v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01519v1)

**Summary:** Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instantiating the behavior named in the claim. We audit this risk in a multi-turn buyer--seller testbed for configurable hotel transactions. An initial implementation reported welfare gains from two marketplace guardrails of +87.4, +35.0, and +28.8 across a Qwen2.5 1.5B--14B ladder. It also gave guarded an...

---

### 19. TempCloze: Can Video-LLMs Identify the Missing Middle?

**Authors:** Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01515v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01515v1)

**Summary:** Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly...

---

### 20. LatentPress: Context Compression Beyond Text and Vision

**Authors:** Zhengze Zhou, Hejian Sang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01507v1)

**Summary:** Compressed context is usually carried as human-readable text or as rendered images that must be decoded, even when its consumer is a language model. We introduce LatentPress, which writes conversational histories and long documents into a third representation: continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference. A small reader-matched writer compresses $4$-$16\times$ while training only an adapter (4.2M-26....

---

### 21. Optimizing Byzantine Node Placement in Decentralized Federated Learning

**Authors:** Edoardo Gabrielli, Gabriele Tolomei

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01495v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01495v1)

**Summary:** Security evaluations of decentralized federated learning (DFL) typically focus on how Byzantine participants behave, while largely overlooking which participants are compromised. Yet, because aggregation is distributed over a communication graph, the placement of Byzantine nodes determines how malicious influence propagates through the network. We therefore treat Byzantine placement as an explicit adversarial decision and formulate the attacker's objective as selecting, under a fixed compromise ...

---

### 22. Rethinking Learnability in Offline Data-driven Optimization

**Authors:** Chao Qian, Chen-Guang Wang, Rong-Xi Tan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01493v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01493v1)

**Summary:** Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization improves the efficiency of BBO algorithms by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires no additional online evaluations. Many offline optimi...

---

### 23. GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions

**Authors:** Elias Stengel-Eskin, Newton Sander, Carlos Bonetti, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01491v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01491v1)

**Summary:** The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We fin...

---

### 24. Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

**Authors:** Xiaofang Yang, Ziqi Miao, Dianbo Sui, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01487v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01487v1)

**Summary:** Skill-augmented agents load reusable skills as persistent runtime context, improving task performance but also giving malicious skills a durable channel for steering future actions. Such skills may leak secrets, corrupt code, bypass approvals, or stage data for exfiltration only after a concrete user task and workspace state make the unsafe action appear useful. This makes pre-install vetting insufficient and calls for runtime, task-conditioned protection. We propose Defense-as-Skill, a defense ...

---

### 25. Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

**Authors:** Haoyang Yan, Min-le Su, Hangfan Zhang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01481v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01481v1)

**Summary:** This paper studies autonomous software development, in which LLM-based coding agents transform high-level requirements into complete, functional, and usable software systems without human intervention. We introduce Harness-of-Harness (HoH), a framework that enables coding agents to continually improve software during autonomous development. HoH operates on existing coding-agent harnesses, and organizes their executions into iterative planning-coding-testing loops. To sustain improvement across l...

---

### 26. Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers

**Authors:** Egor Pakhomov, Erik Nijkamp

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01466v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01466v1)

**Summary:** A long-horizon agent's trace outgrows both of its consumers: the human observer monitoring the run, and the agent itself, whose bounded context the trace must be folded back into. We present a live trace model, an append-only event ledger folded incrementally into typed run state and compiled into per-consumer views, and evaluate it for both consumers against deterministic ground truth. For the observer side, evaluated with an LLM reader as proxy, the compiled view answers monitoring questions u...

---

### 27. When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning

**Authors:** Yitong Guo, Xiaoyi Chen, Siyuan Zhang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01455v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01455v1)

**Summary:** Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules,...

---

### 28. Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search

**Authors:** Zhiliang Chen, Sebastian Ament, David Eriksson, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01431v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01431v1)

**Summary:** Optimal hyperparameter scaling laws describe how the best hyperparameters for large language model (LLM) training change with model and data scale, enabling practitioners to predict optimal configurations at production scales without expensive large-scale tuning. However, estimating these scaling laws conventionally requires exhaustive grid searches over thousands of training runs, consuming enormous computational resources. We introduce Power-Law Entropy Search (PLES), a computational cost-awar...

---

### 29. Learning Sparse Decision Trees via Transformer Variational Auto-Encoders

**Authors:** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01430v1)

**Summary:** Decision trees are among the most widely used models in machine learning, largely due to their transparent decision logic, making them well-suited for high-stakes decision-making contexts. However, most existing learning algorithms focus on predictive performance, overlooking the joint optimization of other desirable properties, such as structural sparsity. In this work we propose TREVIS, an approach for learning decision trees with respect to complex objectives, based on the exploration of the ...

---

### 30. Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading

**Authors:** Fatemeh Javadian, Zhu Chen, Zahra Aminparast, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01426v1)

**Summary:** Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map ch...

---

### 31. Provably Safe Sim-to-Real Transfer

**Authors:** Tingting Ni, Maryam Kamgarpour

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01418v1)

**Summary:** To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in man...

---

### 32. EdiTikZ: Scientific Figure Editing from Revision Trajectories

**Authors:** Christian Greisinger, Zhixue Zhao, Steffen Eger

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01409v1)

**Summary:** Vision-language models (VLMs) have shown strong performance in generating scientific figures from text or images. However, producing publication-ready figures requires iterative refinement, making scientific figure editing an important yet largely unexplored task. Existing approaches rely on costly proprietary agentic systems, focus primarily on evaluation, or construct training supervision from synthetically generated edits. Instead, we leverage naturally occurring scientific revision and devel...

---

### 33. Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations

**Authors:** Qingde Li, Qingqi Hong, Jie Tian

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01408v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01408v1)

**Summary:** A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...

---

### 34. Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching

**Authors:** Jaewoo Park, Minyoung Lee, Sukmin Seo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01404v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01404v1)

**Summary:** Multimodal Large Language Models (MLLMs) are strong perceivers of images and video. We ask how far that reach extends into acting: dropping an MLLM directly into a drone's control loop, with its entire action space declared solely in the prompt. Recent systems approach this setting but increasingly narrow the model's decision-making. We widen it back. We introduce DroneCATS-Agent, an architecture where the MLLM is a swappable component, and DroneCATS, a benchmark treating the model as the indepe...

---

### 35. Measuring consistency via ensemble margin and local prediction variability: Auditing decision systems in the presence of predictive multiplicity

**Authors:** Sinjini Banerjee, Tim Marrinan, Anand D. Sarwate

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01397v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01397v1)

**Summary:** The Rashomon effect is a machine learning phenomenon where equally accurate models produce different predictions for the same inputs (predictive multiplicity). Existing work primarily focuses on multiplicity within individual models, but in more complex decision systems, the impact of the Rashomon effect is less well understood. In this work, we study multiplicity from the perspective of auditing incorrect ensemble predictions, where the decision to divert an instance for human review is based o...

---

### 36. EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems

**Authors:** Jun Hou, Priya Pitre, Yi Fang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01360v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01360v1)

**Summary:** Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph ...

---

### 37. PopPert: Population-level Joint-Distribution Modeling for Single-Cell Perturbation Prediction

**Authors:** Handong Wang, Jiaxin Qi, Haochen Feng, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01357v1)

**Summary:** Predicting transcriptional responses to specific perturbations is critical for understanding cellular regulatory mechanisms and accelerating drug discovery. Single-cell RNA sequencing destroys each measured cell, yielding only unpaired populations of control and perturbed cells. However, existing methods typically model perturbation prediction at the single-cell level and assume cell-to-cell correspondence, which conflicts with the unpaired nature of the observed data. To address this challenge,...

---

### 38. SymFold: Synergizing Evolutionary and Structural Priors for Accurate Protein Inverse Folding

**Authors:** Handong Wang, Jiaxin Qi, Baisheng Lai, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01353v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01353v1)

**Summary:** Protein inverse folding aims to recover amino acid sequences for a given 3D protein structure, underpinning broad applications such as enzyme engineering and drug discovery.Current methods often follow a serial pipeline, in which a structure encoder predicts a coarse sequence, which is then refined by protein language models (PLMs). However, because PLMs only perform post-hoc sequence edits, the refinement is bounded by the quality of upstream predictions.Thanks to recent multimodal protein lang...

---

### 39. CHARM: Character Hallucination for Multicultural Role Play Benchmark

**Authors:** Sunkyung Han, Nahyeon Park, Gaeun Seo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01352v1)

**Summary:** Role-playing large language models (LLMs) are expected to adopt a character's style while also respecting that character's knowledge boundaries. Prior evaluations detect character hallucination but rarely distinguish whether errors arise from failure to recognize a boundary or from failure to comply despite recognition. We introduce CHARM, a multicultural benchmark of 40 real and fictional characters drawn from five cultural-linguistic regions, and validated by native reviewers. It probes two bo...

---

### 40. Scalable Rao-Blackwellized Online Planning for High-Dimensional POMDPs

**Authors:** Jiho Lee, Nisar Ahmed, Kyle Hollins Wray, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01351v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01351v1)

**Summary:** Online planning under uncertainty remains a fundamental challenge for robotic systems operating in partially observable environments with high-dimensional state spaces. While sampling-based POMDP solvers enable approximate decision-making in large or continuous domains, their performance degrades as belief dimensionality increases due to the high variance inherent in Monte Carlo-based estimation. In this work, we extend the Rao-Blackwellized online POMDP (RB-POMDP) framework to improve its gener...

---

### 41. Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades

**Authors:** Dushyant Rajput

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01345v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01345v1)

**Summary:** Inference cascades cut cost by answering most queries with a cheap model and escalating a hard tail to a frontier model that acts as verifier. A natural extension closes the loop: fine-tune the cheap student on the verifier's rejections so the escalation rate, and cost, fall each round. We measure this loop on real LLMs and report four findings. First, the verifier's blind spot, the fraction of the student's wrong answers it accepts, is large and moves adversarially: it grows with student capabi...

---

### 42. Probing Factual Knowledge Transfer with Training Data Interventions

**Authors:** Romina Oji, Marc Braun, Marcel Bollmann, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01341v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01341v1)

**Summary:** Do multilingual language models transfer factual knowledge across languages during continued pretraining, or do they mostly recall facts learned directly from the target-language data? To answer this question more reliably, we propose an intervention-based framework: starting from an English-pretrained model, we continue pretraining on Persian data from which specific facts have been systematically removed at varying levels of granularity. We construct SIFT, a resource of 500 triples across 20 r...

---

### 43. LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting

**Authors:** Yufei Chen, Yiran Zhao, Xiaogang Xu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01337v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01337v1)

**Summary:** LLM-based forecasting systems have improved on real-world tasks such as financial markets and sports outcomes, largely through stronger search and tool use. Many systems still ask an LLM to read all collected evidence together and produce the final forecast. We call this design Monolithic Prediction. It can obscure how individual evidence items affect the result and collapse uncertainty across competing outcomes. We propose LEAP (Likelihood Elicitation and Aggregation for Probabilistic forecasti...

---

### 44. Bandits in Prod: Hyperparameter Optimization at Inference Time

**Authors:** Louis Abraham, Tuan-Anh Nguyen, Nicolas Devatine

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01335v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01335v1)

**Summary:** Many production systems can assess a configuration only by using it on live requests and observing noisy feedback. Modern agentic systems are a prominent example, with inference-time choices such as model selection, retrieval depth, prompting strategy, and decoding temperature, yet often with no representative validation data. We formalize this setting as Online Hyperparameter Optimization (OHPO) and cast it as an infinitely many-armed bandit over mixed and conditional search spaces. We introduc...

---

### 45. Automated Event Log Generation from Unstructured Text Using Finetuned LLMs

**Authors:** Maximilian Seeth, Gabriel Marques Tavares, Daniel Schuster

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01320v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01320v1)

**Summary:** Process mining (PM) provides a powerful framework for discovering and optimizing operational processes from event data. However, the efficacy of PM techniques is strictly predicated on the availability of structured event logs. Thus far, event logs have often been laboriously created by domain and process mining experts. This costly effort causes large portions of organizational knowledge, including incident tickets, manuals, and textual reports, to remain underutilized. We address this bottlene...

---

### 46. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

**Authors:** Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01316v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01316v1)

**Summary:** Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing tha...

---

### 47. A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation

**Authors:** Hodong Lee, Sanghee Park, Dohoon Ryu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01315v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01315v1)

**Summary:** Building an omni-modal foundation model means evaluating it across text, image, video, and audio. Excellent evaluation toolkits exist for each modality, but their inference engines, prompt conventions, and metric implementations are mutually incompatible, so practitioners end up maintaining separate environments for every toolchain and still struggle to compare results across them. OmniEvaluator grew out of this need in our own model development: rather than reimplementing benchmarks, it connect...

---

### 48. GazeRefine: Expert Gaze as a Test-Time Prompt for Training-Free Medical Image Segmentation

**Authors:** Mohammed Oussama Benyahia, Marouane Tliba, Mohamed Amine Kerkouri, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01310v1)

**Summary:** Medical image segmentation remains difficult to scale because high-performing methods typically rely on dense expert annotations and task-specific training. We introduce GazeRefine, a training-free framework that uses gaze as an inference-time prompt for zero-shot medical image segmentation. Sparse, duration-weighted fixations are converted into foreground and background priors that initialize semantic prototypes in frozen DINOv3 feature space. These prototypes are iteratively refined through fo...

---

### 49. Analog-DB: An Agent-First Analog Integrated Circuit Database, From Blocks to Systems

**Authors:** Danial Noori Zadeh, Mohamed B. Elamien

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01286v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01286v1)

**Summary:** Sharing analog integrated circuit designs remains difficult: foundry non-disclosure agreements restrict the process details a design depends on, and the testbenches behind published results are rarely released. We present analog-db, an open-source, versioned database built on a shareable design representation. A domain-specific language captures each design as a process-neutral topology, reusable testbenches, and a machine-readable datasheet under one schema, so a design is shared in full and re...

---

### 50. HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives

**Authors:** Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01282v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01282v1)

**Summary:** Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires modul...

---

## cs.CL

**50 papers**

### 1. Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation

**Authors:** Himil Vasava, Ming Jiang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01604v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01604v1)

**Summary:** LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-l...

---

### 2. Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation

**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01603v1)

**Summary:** Evaluating software engineering agents on realistic benchmarks is costly, since each task may require multi-step code exploration, modification, and test execution. Existing efficient evaluation methods select representative subsets to estimate full-benchmark performance, but are largely result-only: they fit historical pass/fail response matrices or static task semantics, discarding how agents solve problems. We propose PTA-IRT, a Privileged Trajectory-Aware Item Response Theory framework that ...

---

### 3. Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation

**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01601v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01601v1)

**Summary:** The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context. Since real-world repositories often exceed the input length limits of LLMs, existing approaches commonly adopt retrieval-augmented generation (RAG) to provide repository-specific context. Despite improving repository-context retrieval, existing methods typically provide context as task-level support, without explicitly identifying th...

---

### 4. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

**Authors:** Damien Sileo, Dimitri Kachler

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01600v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01600v1)

**Summary:** Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local plugin change can propagate through dependencies and cleanup. We introduce CordisBench, a 1,200-question benchmark of this lifecycle reasoning. It combines a controlled formal setting with programs executed against Cordis, a runtime that manages component dependencies and cleanup, and asks models to identify affected components, predict state af...

---

### 5. The Rise of Verbal Reinforcement Learning

**Authors:** Kshitij Tayal, Arun Sharma, Genta Indra Winata, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01597v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01597v1)

**Summary:** Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{La...

---

### 6. StudentSim: Training LLM-based Student Simulators

**Authors:** Ke Yang, Chenglong Wang, Michel Galley, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01591v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01591v1)

**Summary:** AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or corrections, while LLM role-play follows guidance fluently but does not reliably match the competence...

---

### 7. Designing Proactive Thought Partners for Writing

**Authors:** Chao Zhang, Abe Davis, Chih-Wei Chen, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01588v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01588v1)

**Summary:** Writing involves diverse cognitive activities, from ideation to revision, and writers' needs vary across individuals and moments. Proactive AI promises to provide the right support at the right time, yet existing proactive tools largely focus on generic textual assistance, such as autocomplete. This paper studies the design space of proactive thought partners: AI agents that proactively offer customizable, higher-level cognitive support during writing. We instantiated this concept in a technolog...

---

### 8. The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally

**Authors:** Jundong Hu, Shekar Ramachandran

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01587v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01587v1)

**Summary:** Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) across 9 open-weight models in 4 architecture families, we test 3 intuitive hypotheses: that quantiz...

---

### 9. Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics

**Authors:** Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01575v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01575v1)

**Summary:** Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents cu...

---

### 10. Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs

**Authors:** Jingtan Wang, Arun Verma, Xiaoqiang Lin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01573v1)

**Summary:** How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad trends (e.g., SFT dominates in low-data regimes), lacks a principled allocation framework, and does not examine whether the optimal ratio transfers across model sizes. We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal...

---

### 11. From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix

**Authors:** Olga Tsymboi, Dmitrii Stoianov, Ramil Latypov, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01572v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01572v1)

**Summary:** Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU pool. We consolidate traffic from over 200 internal applications onto a single model by closing quality gaps identified through production error analysis along three axes: instruction following, function-calling, and internal task distribution. Quality is tracked by offline benchmarks stratified to p...

---

### 12. Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers

**Authors:** Matteo Merler, Giovanni Bonetta, Davide Zago, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01567v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01567v1)

**Summary:** Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertai...

---

### 13. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification

**Authors:** Manish Gupta, Chaitanya Giri, Jayasimha Talur

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01564v1)

**Summary:** Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the ...

---

### 14. A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains

**Authors:** Ema Salkić, Alexander Fichtl, Philipp Ulrich, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01563v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01563v1)

**Summary:** Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linkin...

---

### 15. SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue

**Authors:** Stephanie Fong, Yiwen Jiang, Zimu Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01548v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01548v1)

**Summary:** Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks remain scarce. Existing general-domain evaluations typically rely on static prompts and fixed-format tasks, overlooking conversational contexts and audience effects in everyday communication. To address these gaps, we introduce SDARE-Bench, the first scenario-based benchmark evaluating both stigma detec...

---

### 16. Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall

**Authors:** Jacqueline He, Howard Yen, Shuyue Stella Li, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01532v1)

**Summary:** Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while for...

---

### 17. GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions

**Authors:** Elias Stengel-Eskin, Newton Sander, Carlos Bonetti, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01491v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01491v1)

**Summary:** The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We fin...

---

### 18. AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval

**Authors:** Tianyu Wang, Tianjiao Wu

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01456v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01456v1)

**Summary:** Composed image retrieval (CIR) retrieves a target image from a reference image and a text modification. This paper studies metadata-available CIR reranking, where a fixed CIR model first returns a candidate pool and gallery metadata is then used for second-stage concept-guided scoring. We introduce AutoConcept, a training-free reranker that converts concept evidence into an interpretable memory. AutoConcept filters noisy concepts, activates query-relevant positive constraints with an auxiliary n...

---

### 19. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

**Authors:** Yuhao Wu, Jingyuan Zhang, Jiajun Shi, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01437v1)

**Summary:** As agents move from research prototypes to deployed tools, their capability increasingly depends on model-external execution infrastructure, commonly termed the agent harness. Changing this harness while holding model weights fixed can substantially alter task performance. Current agent evaluations typically report downstream performance under a chosen harness, leaving a model's ability to develop the harness itself comparatively underexplored. We introduce HarnessDev, a benchmark that shifts th...

---

### 20. Citing Less Critically: LLMs Reshape the Rhetoric and Reach of Scientific Citation

**Authors:** Yixuan Liu, Lin Chen, Zhuoqi Liu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01432v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01432v1)

**Summary:** Scientific citations carry rhetorical intent. Scholars may cite prior work positively (supporting), negatively (contrasting), or neutrally (mentioning). As large language models (LLMs) increasingly assist scientific writing, whether they reproduce citations with the same rhetorical intent as humans remains unclear. We introduce a masked-citation task to compare human and LLM-generated citation behavior. For each citation context, an LLM generates a replacement citation sentence, producing a coun...

---

### 21. From Rollouts to Recipes: Self-Contained Post-Training for LLMs

**Authors:** Yifei Li, Lingling Zhang, Muye Huang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01422v1)

**Summary:** Post-training large language models usually applies a single training recipe to all samples, even though the model's own rollouts reveal different sample-level learning states. We propose Self-Routing, a behavior-conditioned post-training framework that uses rollout correctness and confidence to decide how each sample should be optimized. Depending on its behavior state, a sample is routed to GRPO, on-policy self-distillation, regularization, or skipping, allowing training to adapt without exter...

---

### 22. EdiTikZ: Scientific Figure Editing from Revision Trajectories

**Authors:** Christian Greisinger, Zhixue Zhao, Steffen Eger

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01409v1)

**Summary:** Vision-language models (VLMs) have shown strong performance in generating scientific figures from text or images. However, producing publication-ready figures requires iterative refinement, making scientific figure editing an important yet largely unexplored task. Existing approaches rely on costly proprietary agentic systems, focus primarily on evaluation, or construct training supervision from synthetically generated edits. Instead, we leverage naturally occurring scientific revision and devel...

---

### 23. When Tokenization is Secretly Output Supervision

**Authors:** Tanja Baeumel, Josef van Genabith, Simon Ostermann

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01386v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01386v1)

**Summary:** Tokenization in language models is treated by default as an input preprocessing decision. We argue that this framing is incomplete: in autoregressive models, tokenizer granularity determines what the model must resolve in a single forward pass, and therefore the supervision signal it receives. This affects both the difficulty of the learning problem and the representations that emerge inside the model. We test this in a controlled experiment on numeric reasoning with a novel decoupling of input ...

---

### 24. InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations

**Authors:** Maeve Hutchinson, Syed Mahbubul Huq, Mohammad Albinhassan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01383v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01383v1)

**Summary:** Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic, requiring the active interrogation of interactive environments. Existing benchmarks are predominantly constrained to static imagery and one-shot question answering and fail to capture the epistemic demands of this domain, where evidence is frequently occluded, distributed across linked views, or conditionally revealed through user agency. In thi...

---

### 25. Polish ModernBERT: The Long and Short of Polish Language Understanding

**Authors:** Michał Perełkiewicz, Sławomir Dadas, Rafał Poświata, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01379v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01379v1)

**Summary:** Encoder-only Transformers remain effective for discriminative and representation-learning tasks, yet Polish encoders still largely rely on BERT/RoBERTa-style architectures. We introduce \textbf{Polish ModernBERT}, a family of four Polish encoders available at Base and Large scales, each with 512-token and 8K context variants. We adapt the ModernBERT pretraining recipe through staged selection experiments and release a long-context benchmark covering legal topic classification, ideological decisi...

---

### 26. IntroConformal: Conformal Factuality Guarantees for Large Vision-Language Models via Introspective Signals

**Authors:** Md. Atabuzzaman, Christian Alexander, Chris Thomas

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01375v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01375v1)

**Summary:** Large Vision-Language Models (LVLMs) have achieved strong multimodal performance, yet ensuring the factual correctness of generated content remains challenging. Existing methods that provide statistical guarantees on factuality typically rely on external verifiers or generation-time confidence signals, which introduce auxiliary dependencies or often fail for confident but incorrect outputs. We argue that reliable factuality control can instead be achieved through introspective signals derived fr...

---

### 27. Behaviorally Effective LoRA Writes Are Sparse and Structured

**Authors:** Haruto Sato, Yuki Tanaka, Ren Nakamura, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01374v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01374v1)

**Summary:** Low-rank adaptation fixes the rank of the update, but it does not identify which parts of a trained   write actually carry behavior. We study that question directly and show that behaviorally effective   LoRA writes are sparse, structured, and far more concentrated than the raw low-rank parameterization   suggests.   We use Learned-Basis LoRA, a learned-basis continuation recipe, to expose that structure. The recipe   warms up an unconstrained adapter, converts its learned write columns into a m...

---

### 28. How Correct Is Your Answer? A Semantic Correctness Framework for Open QA Evaluation

**Authors:** Elitsa Yotkova, Violeta Kastreva, Petar Velkov, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01369v1)

**Summary:** Reliable evaluation of open-ended question answering remains a bottleneck for measuring answer correctness of modern LLMs. Unlike multiple-choice tasks, free-form answers may be correct in many surface forms and may fail in qualitatively different ways, including incompleteness, contradiction, overgeneration, and endorsement of false premises. Existing judgment-based and similarity-based metrics often collapse these distinctions. We address this gap with three reusable contributions. First, we i...

---

### 29. Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA

**Authors:** Nishant Mishra, Ameen Abu-Hanna, Iacer Calixto

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01361v1)

**Summary:** Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometrically, that implies that true and false statements separate along a stable direction in hidden state space, i.e., the truth direction. Prior work disagrees on whether this generalises across input shifts, but the disagreement is hard to interpret because cross-dataset probe transfer experiments confound several kinds of input change at once. We i...

---

### 30. Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs

**Authors:** Mikhail Sonkin, Tanja Baeumel, Daniil Gurgurov, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01356v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01356v1)

**Summary:** Multilingual large language models (mLLMs) achieve strong performance in machine translation, yet our understanding of the mechanisms by which they transform representations from one language to another remains incomplete. Prior work suggests that translation decomposes into separable processes within an mLLM, where conceptual content is first represented independently, followed by a production into language-specific form. In this work, we show that translation is even more modular than previous...

---

### 31. Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR

**Authors:** Esther Xin

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01354v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) and standard benchmark evaluation both rely on an automatic verifier that turns a free text answer into a binary reward. Prior work reports that one evaluation harness accepts only about 94% of its own ground truth answers, blaming LaTeX parsing. That is an aggregate: it does not say which answer forms consume the error budget. We supply the decomposition. We apply metamorphic testing to the verifier rather than the model, generating certifie...

---

### 32. CHARM: Character Hallucination for Multicultural Role Play Benchmark

**Authors:** Sunkyung Han, Nahyeon Park, Gaeun Seo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01352v1)

**Summary:** Role-playing large language models (LLMs) are expected to adopt a character's style while also respecting that character's knowledge boundaries. Prior evaluations detect character hallucination but rarely distinguish whether errors arise from failure to recognize a boundary or from failure to comply despite recognition. We introduce CHARM, a multicultural benchmark of 40 real and fictional characters drawn from five cultural-linguistic regions, and validated by native reviewers. It probes two bo...

---

### 33. Probing Factual Knowledge Transfer with Training Data Interventions

**Authors:** Romina Oji, Marc Braun, Marcel Bollmann, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01341v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01341v1)

**Summary:** Do multilingual language models transfer factual knowledge across languages during continued pretraining, or do they mostly recall facts learned directly from the target-language data? To answer this question more reliably, we propose an intervention-based framework: starting from an English-pretrained model, we continue pretraining on Persian data from which specific facts have been systematically removed at varying levels of granularity. We construct SIFT, a resource of 500 triples across 20 r...

---

### 34. VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models

**Authors:** Zhiqi Huang, Vivek Datla, Zhichao Xu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01325v1)

**Summary:** Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of ...

---

### 35. Exploring Sparse Autoencoders in Text-Based Causal Confounding Adjustment

**Authors:** Mian Zhong, Katherine A. Keith, Anjalie Field

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01322v1)

**Summary:** In many settings, studying causal questions based on text data requires adjusting for confounding information within texts. Yet there is a tradeoff in constructing text representations for adjustment: they must be sufficiently large and/or dense to preserve the confounding variables necessary for unbiased effect estimation, but sufficiently small and/or sparse to satisfy finite-sample overlap and yield low-variance estimates. To address this tradeoff, we turn to sparse autoencoders (SAEs), and p...

---

### 36. Reliability Challenges in Diffusion Vision-Language Models

**Authors:** Md. Atabuzzaman, Chris Thomas

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01318v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01318v1)

**Summary:** Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our ...

---

### 37. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

**Authors:** Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01316v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01316v1)

**Summary:** Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing tha...

---

### 38. Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents

**Authors:** Ruochen Zhou, Zhengyu Chen, Luan Zhang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01294v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01294v1)

**Summary:** Deep-research agents answer complex questions by interacting with search and browsing tools, yet they often search along a single evolving trajectory. Our trajectory-level analysis reveals a common failure mode in which the agent may encounter an early search state with several plausible directions, but follow one direction before collecting enough comparative evidence. Once this happens, subsequent tool calls tend to reinforce the same path, increasing the chance of failure when the initial dir...

---

### 39. Some Emotions Run Deeper: Layer-wise Probing and Causal Intervention in Large Language Models

**Authors:** Tian Fang, Gaël Guibon, Davide Buscaldi

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01279v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01279v1)

**Summary:** Emotion is expressed in text along a wide spectrum, from surface lexical cues to inferences entangled with content. Most layer-wise analyses of emotion in LLMs use a single corpus, leaving open whether the depth at which emotion becomes accessible is a property of the model or also of the text source. We investigate this across three datasets spanning different degrees of explicitness and contextualization in emotion expression (Twitter posts, Reddit comments, and autobiographical narratives) an...

---

### 40. From Base Rollouts to RL Reasoning: A Budgeted Search Perspective

**Authors:** Wenhe Sun, Cunxiang Wang, Zijun Yao, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01274v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01274v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but how these gains relate to inference-time decoding and search remains unclear. Does RL create reasoning the base model lacks, or shift the rollout distribution toward trajectories it can already reach but rarely samples? We study this behaviorally with a Unified Decoding Framework (UDF), which expresses token-level sampling, beam-like search, tree search, and sequence-level resampling as executable polici...

---

### 41. What Does an Agentic Software Engineering Benchmark Measure? Profiling Task Demands and Agent Behaviour Beyond What Category Labels Reveal

**Authors:** Radin Shayanfar, Keheliya Gallaba, Ahmed E. Hassan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01271v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01271v1)

**Summary:** Agentic software engineering benchmarks are typically summarized by nominal category labels such as "bug fix" or "feature implementation," yet benchmarks carrying the same label are built through very different curation pipelines. A label thus reveals little about the engineering work a benchmark demands. We introduce the Spread--Novelty--Centrality (SNC) profile, a three-axis characterization of the demands of repository-level coding tasks, grounded in empirical software engineering research. W...

---

### 42. Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation

**Authors:** Thibaut Thonet, Jos Rozen, Laurent Besacier

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01246v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01246v1)

**Summary:** Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spa...

---

### 43. Post-Training Science for Supervised Fine-Tuning

**Authors:** Charles O'Neill, Mudith Jayasekara, Harry Partridge

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01244v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01244v1)

**Summary:** Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset. Here we measure them under one instrument: a sweep that varies one lever at a time, and spans dense and mixture-of-experts models in two families (Qwen3 and Llama), on four real-world customer SFT datasets, for both L...

---

### 44. Towards AI-Assisted Clinical Trial Matching: Practical Considerations, Multicenter Evaluation, and Real-World Deployment

**Authors:** Yin Fang, Qiao Jin, Shubo Tian, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01202v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01202v1)

**Summary:** Clinical trials are essential for advancing cancer care and drug development, but many fail because of insufficient patient enrollment. While there is growing interest in using AI to support patient recruitment, existing systems largely perform eligibility assessment alone and have rarely been evaluated in real-world oncology workflows. Here we present TrialGPT 2.0, an AI-assisted clinical trial recommendation system designed for real-world deployment. Rather than asking only whether a patient m...

---

### 45. FinLifeBench: Exhaustive Life-Event History and Financial-State Reconstruction from Longitudinal Banking Dialogue

**Authors:** Hangyeul Lee, Juyoung Oh, Jaeyong Ko, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01198v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01198v1)

**Summary:** Repeated banking interactions require assistants to maintain complete, current, and traceable customer records as life changes emerge incidentally in routine requests. Existing benchmarks emphasize question answering, bounded episodes, or targeted recall rather than exhaustive longitudinal reconstruction. We introduce FinLifeBench, which evaluates two tasks over the same cumulative dialogue: reconstructing every life-event instance with its first-establishing session and reconstructing a complet...

---

### 46. CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs

**Authors:** Chaohui Guo, Michel Klein, Zhisheng Huang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01195v1)

**Summary:** Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decis...

---

### 47. PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation in Insurance

**Authors:** Rohan Kirti, Akash Ghosh, Aryan Vats, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01188v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01188v1)

**Summary:** Large Language Models (LLMs) are revolutionizing digital communication by powering conversational agents deployed across domains such as customer service, digital sales, and insurance. These agents, built on LLMs, can understand user input, retrieve relevant information, and generate coherent responses. However, while they excel at factual communication, they often lack the ability to engage in truly persuasive, context-sensitive dialogue, especially in domains like insurance, where trust and cl...

---

### 48. LLMPEDIA: Browsing, Verifying, and Comparing the Parametric Encyclopedic Knowledge of LLMs

**Authors:** Muhammed Saeed, Simon Razniewski

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01182v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01182v1)

**Summary:** Flagship language models appear saturated on benchmarks like MMLU (Hendrycks et al., 2021), scoring above 90% - yet benchmarks test only what the experimenter thought to ask, the availability bias of fixed question sets. LLMPEDIA makes this bias measurable and browsable. We recursively materialized ~1.3M articles from three model families' parametric memory (GPT-5-mini, DeepSeek-V3.2, Llama-3.3-70B) without retrieval, then audited a stratified sample of atomic claims against Wikipedia and a cura...

---

### 49. Subword Segmental BabyLMs: Learning to Tokenise for Sample-Efficient Pretraining

**Authors:** Francois Meyer

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01151v1)

**Summary:** In the standard LM training pipeline, subword tokenisation is applied as a preprocessing step. Subword segmental language modelling is an alternative paradigm in which tokenisation is learned during training, allowing the model to discover subword units that optimise its training objective. In this paper, we present our submission to the 2026 BabyLM Challenge, for which we develop two new subword segmental LMs: SubSegGPT and SubSegDeBERTa. SubSegGPT is a decoder-only model that learns tokenisati...

---

### 50. On the Design Fundamentals of Pixel Text Representation Learning

**Authors:** Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01147v1)

**Summary:** Text-rich visual inputs require models that can read, retrieve, and compress language directly in pixel space, yet existing pixel-text encoders struggle with fixed resolution pretraining, visual shortcut learning, weak visual grounding, and multilingual visual text understanding. In this work, we investigate the fundamental design principles required for robust visual text representation learning. Through systematic controlled ablations, we identify four critical components: variable image resol...

---

## cs.CV

**50 papers**

### 1. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System

**Authors:** Penghao Wu, Haiwen Diao, Weichen Fan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01607v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01607v1)

**Summary:** While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal ...

---

### 2. UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture

**Authors:** Asees Kaur, Suzanne S. Sindi, Erica M. Rutter

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01598v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01598v1)

**Summary:** Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep learning approaches such as U-Net achieve strong general-purpose segmentation performance but often produce fragmented or discontinuous predictions in fine vascular regions, since they do not explicitly enforce structural connectivity. Region growing algorithms preserve spatial context and topological c...

---

### 3. A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios

**Authors:** Sergio M. Silva, Otavio T. Remer, Gabriel E. Lima, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01584v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01584v1)

**Summary:** Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. However, models trained under controlled conditions often degrade in real surveillance scenarios due to changes in viewpoint, occlusion, illumination, and sensor characteristics. This paper introduces Unconstrained Vehicle Identification Benchmark (UVIB), a benchmark for evaluating three operational vehi...

---

### 4. SpatialGuard: Harness-Guided Verifiable Spatial Reasoning for Text-to-Image Generation

**Authors:** Ziyun Qian, Zizhi Chen, Yizhou Liu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01582v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01582v1)

**Summary:** Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned methods improve controllability, but often lack an optimizable and verifiable spatial intermediary before visual sampling. As a result, object relations, occlusion, visibility, and camera constraints can decay during multi-round generation. This paper presents SpatialGuard, a structured layout-guided fram...

---

### 5. H3-World: Turning Language Understanding into World Control

**Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01560v1)

**Summary:** We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control. MiniMax-H3, for example, already supports zero-shot control of character behavior and camera motion through natural-language instructions. Building on this, H3-World turns this coarse language interface into precise, temporally grounded world contr...

---

### 6. BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net

**Authors:** Marven Sherif, Amgad Elmasry, Youssef Ghazal, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01554v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01554v1)

**Summary:** Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, P...

---

### 7. What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models

**Authors:** Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01551v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01551v1)

**Summary:** Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive phy...

---

### 8. Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison

**Authors:** Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01530v1)

**Summary:** Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-vis...

---

### 9. DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting

**Authors:** Qian Wang, Yu Wang, Weiqi Li, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01516v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01516v1)

**Summary:** While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered novel views. Recent efforts attempt to utilize powerful diffusion priors, yet they typically process rendered and reference views concatenated along an additional dimension in a single network. These methods overlook an inherent nature that different views should maintain appearance similarity but ...

---

### 10. TempCloze: Can Video-LLMs Identify the Missing Middle?

**Authors:** Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01515v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01515v1)

**Summary:** Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly...

---

### 11. A Sensor-Adaptive Incremental Learning Framework for Artifact Detection in Satellite Precipitation Data

**Authors:** Andres F. Monsalve, Hernan A. Moreno, Christian D. Kummerow

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01514v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01514v1)

**Summary:** Historically, retrieving rainfall data from satellite imagery has been the domain of space agencies. However, in recent years, the development of cheaper, more compact satellites (SmallSats) capable of detecting rainfall proxies has led to a significant increase in private-sector initiatives for satellite launch and surface precipitation products. This rapid growth has yet to be matched by data validation efforts. Consequently, the need for a robust tool to detect anomalies in near-real-time dat...

---

### 12. Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation

**Authors:** Lucas Cunha, Lucas Sotomaior, Lucas Gasperin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01511v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01511v1)

**Summary:** Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across ...

---

### 13. CameraEditor: Camera-Controlled Image Editing via Video-Prior Sequential Modeling

**Authors:** Xin Shen, Chengyou Jia, Keshuo Xing, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01479v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01479v1)

**Summary:** Beyond semantic content, camera parameters play a pivotal role in dictating the geometric perspective and appearance of any given image. While recent image editing models excel at semantic and stylistic manipulation, they struggle with explicit camera parameter control. When handling large perspective shifts, instruction-driven models face a dilemma: they either suffer from structural tearing or generate conservative outputs that ignore geometric instructions. To address this, we introduce Camer...

---

### 14. RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching

**Authors:** Charles Corbière, Léo Machado, Aubin Charley, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01470v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01470v1)

**Summary:** As AI systems are increasingly used to draft radiology reports, reliably evaluating their clinical quality remains a critical challenge. Large language model (LLM)-based metrics are now the best-correlated with radiologist judgment, yet they output a single opaque score that neither a clinician nor a model builder can easily interpret or audit. We introduce RadMatch, a multi-stage, LLM-based metric that decomposes report comparison into a structured finding-level matching with significance-aware...

---

### 15. Gaussian Core LoRA: Distribution-Aware Dynamic Adaptation for Broad Concept Erasure

**Authors:** Qinghui Gong, Xunlei Chen, Yu-Xuan Zhang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01433v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01433v1)

**Summary:** Concept erasure aims to suppress unsafe, privacy-sensitive, or undesirable generations in text-to-image diffusion models while preserving benign semantics, visual quality, and deployment efficiency. Existing adapter-based methods, such as Low-Rank Adaptation (LoRA), typically freeze the diffusion backbone and learn lightweight parameter updates to steer generation away from target semantics. However, these methods usually assign a static semantic erasure direction to each target concept. This as...

---

### 16. Pix2Rep-v2: Data-Efficient Representation Learning for Dense Medical Imaging Applications

**Authors:** S. Sifaoui, E. Angelini, S. Toupin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01427v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01427v1)

**Summary:** Dense self-supervised learning (SSL) is a powerful paradigm for learning without annotations the local descriptors required to solve dense medical imaging tasks. We present Pix2Rep-v2, a framework for SSL of pixel- and voxel-level representations suitable for few-shot downstream applications. Pix2Rep-v2 addresses the main challenges of dense SSL by leveraging a redundancy reduction objective at the pixel-level with a principle of equivariance of dense representations, that scales efficiently to ...

---

### 17. Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading

**Authors:** Fatemeh Javadian, Zhu Chen, Zahra Aminparast, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01426v1)

**Summary:** Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map ch...

---

### 18. MegaStyle++: Scaling Image Style Space through Hierarchical Style Definition

**Authors:** Junyao Gao, Sibo Liu, Jiaxing Li, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01423v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01423v1)

**Summary:** Image style is a highly abstract, human-constructed concept shaped by a range of visual factors and intrinsically entangled with content, yet a unified and explicit definition of image style remains lacking. In this work, we first discuss the fundamental question of what is style and then propose a hierarchical style definition that describes image style from an overall style identity to fine-grained visual attributes, providing a more structured, transferable, and interpretable style representa...

---

### 19. EdiTikZ: Scientific Figure Editing from Revision Trajectories

**Authors:** Christian Greisinger, Zhixue Zhao, Steffen Eger

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01409v1)

**Summary:** Vision-language models (VLMs) have shown strong performance in generating scientific figures from text or images. However, producing publication-ready figures requires iterative refinement, making scientific figure editing an important yet largely unexplored task. Existing approaches rely on costly proprietary agentic systems, focus primarily on evaluation, or construct training supervision from synthetically generated edits. Instead, we leverage naturally occurring scientific revision and devel...

---

### 20. Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations

**Authors:** Qingde Li, Qingqi Hong, Jie Tian

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01408v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01408v1)

**Summary:** A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...

---

### 21. Scale-based Approach for Active Wildfire Segmentation on Satellite Imagery

**Authors:** Matheus F. Kovaleski, Cristiano Premebida, João Ruivo Paulo

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01392v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01392v1)

**Summary:** Active wildfire mapping from satellite imagery is challenging due to the sparse and highly imbalanced nature of fire pixels, especially in early-stage or low-density fire observations. This work investigates the use of multispectral Landsat-8 imagery for active-fire segmentation under multi-scale wildfire size conditions. We propose a data-driven protocol to characterize fire-region size distributions through connected-component analysis and an interquartile range criterion, enabling the evaluat...

---

### 22. Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3

**Authors:** Matheus F. Kovaleski, Luís Garrote, Cristiano Premebida, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01390v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01390v1)

**Summary:** Unmanned Aerial Vehicles (UAVs) have emerged as a promising platform for firefighting operations due to their flexibility, low operational cost, and ability to acquire high-resolution imagery in locations that may be difficult or dangerous to access using conventional methods. Recent advances in deep learning have significantly improved the capabilities of UAV-based wildfire monitoring systems. The present work investigates RGB-infrared fusion for binary wildfire segmentation on the FLAME3 datas...

---

### 23. InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations

**Authors:** Maeve Hutchinson, Syed Mahbubul Huq, Mohammad Albinhassan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01383v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01383v1)

**Summary:** Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic, requiring the active interrogation of interactive environments. Existing benchmarks are predominantly constrained to static imagery and one-shot question answering and fail to capture the epistemic demands of this domain, where evidence is frequently occluded, distributed across linked views, or conditionally revealed through user agency. In thi...

---

### 24. IntroConformal: Conformal Factuality Guarantees for Large Vision-Language Models via Introspective Signals

**Authors:** Md. Atabuzzaman, Christian Alexander, Chris Thomas

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01375v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01375v1)

**Summary:** Large Vision-Language Models (LVLMs) have achieved strong multimodal performance, yet ensuring the factual correctness of generated content remains challenging. Existing methods that provide statistical guarantees on factuality typically rely on external verifiers or generation-time confidence signals, which introduce auxiliary dependencies or often fail for confident but incorrect outputs. We argue that reliable factuality control can instead be achieved through introspective signals derived fr...

---

### 25. Diffusion Based Unpaired Data Learning for Inverse Problems

**Authors:** Chenglong Bao, Yiming Dang, Chenguang Duan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01370v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01370v1)

**Summary:** Data is important in many deep learning-based inverse problem solvers. However, obtaining sufficient paired data in many scenarios remains highly challenging, while unpaired data is cheap. To maximize data utilization, this paper proposes LUD-DIF, a diffusion-based approach for solving inverse problems with unpaired data. Starting from the evidence lower bound (ELBO) of the joint distribution, we decouple it into two independent diffusion processes under the weak-coupling assumption. The method ...

---

### 26. Accurate Reconstruction of Gas Turbine Blade Geometry Using 3D/2D Rigid Registration and CT View Optimization

**Authors:** Hristo Valtchanov, Nicolas Piché, Vladimir Brailovski, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01368v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01368v1)

**Summary:** Non-destructive X-ray and computed tomography (CT) testing are essential for ensuring the dimensional accuracy of manufactured components with complex internal structures, such as the cooling channels in gas turbine blades, which directly affect thermal performance and service life. This study presents a multipart 3D-2D rigid registration approach for aligning CAD models with X-ray projections as an alternative to CT reconstruction for part inspection and measurement. A greedy registration algor...

---

### 27. ExBind: A Controlled Diagnostic Benchmark for Visual-to-Executable Correspondence

**Authors:** Ziqian Wang, Yuxiao Cheng, Tingxiong Xiao, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01344v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01344v1)

**Summary:** Multimodal coding and editing systems must map a visible or semantic referent to the exact executable object that can be edited. A wrong reference may select a valid but incorrect DOM node, SVG element, graph endpoint, hierarchy member, or table cell, while final execution success alone does not reveal the source of the failure. ExBind isolates this visual-to-executable correspondence layer as a controlled diagnostic benchmark between semantic localization and action execution. It samples repres...

---

### 28. Reliability Challenges in Diffusion Vision-Language Models

**Authors:** Md. Atabuzzaman, Chris Thomas

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01318v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01318v1)

**Summary:** Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our ...

---

### 29. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

**Authors:** Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01316v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01316v1)

**Summary:** Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing tha...

---

### 30. GazeRefine: Expert Gaze as a Test-Time Prompt for Training-Free Medical Image Segmentation

**Authors:** Mohammed Oussama Benyahia, Marouane Tliba, Mohamed Amine Kerkouri, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01310v1)

**Summary:** Medical image segmentation remains difficult to scale because high-performing methods typically rely on dense expert annotations and task-specific training. We introduce GazeRefine, a training-free framework that uses gaze as an inference-time prompt for zero-shot medical image segmentation. Sparse, duration-weighted fixations are converted into foreground and background priors that initialize semantic prototypes in frozen DINOv3 feature space. These prototypes are iteratively refined through fo...

---

### 31. CMRVision: A Foundation Model for Cardiac MR Image Analysis

**Authors:** Athira J. Jacob, Puneet Sharma, Daniel Rueckert

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01308v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01308v1)

**Summary:** Cardiac magnetic resonance (CMR) imaging provides complementary information on cardiac anatomy, function, and tissue characterization across multiple sequences and views. In this work, we investigate foundation model pretraining for 2D CMR and introduce CMRVision, a CMR-specific foundation model trained using DINOv3-style self-supervised learning on a multi-center, multi-sequence cohort of 36 million CMR images. We systematically evaluate architectural and training design choices for domain-spec...

---

### 32. MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering

**Authors:** Kaixuan Zhang, Minxian Li, Mingwu Ren, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01306v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01306v1)

**Summary:** Triangle-based neural rendering bridges neural scene representations and conventional graphics pipelines by optimizing explicit geometric primitives compatible with standard rasterization hardware. However, existing approaches are evaluated almost exclusively within custom research renderers, obscuring their practical deployability in production engines. To bridge this gap, we introduce \textbf{MeshSplatBench}, a unified benchmark that systematically investigates triangle-based neural rendering ...

---

### 33. Agentic Multimodal Models for Environmental Hyperspectral Unmixing

**Authors:** Michał Cholewa, Luca Ciampi, Nicola Messina, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01289v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01289v1)

**Summary:** Hyperspectral unmixing is a key task in remote sensing that aims to decompose mixed pixels in hyperspectral images into their constituent material signatures, or endmembers, and their fractional abundances. Conventional modular approaches estimate the scene composition through successive model-order estimation, endmember extraction, and abundance estimation stages, whose errors can lead to redundant or ambiguous candidate components and ultimately affect the recovered decomposition. We introduce...

---

### 34. HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives

**Authors:** Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01282v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01282v1)

**Summary:** Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires modul...

---

### 35. TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models

**Authors:** Chao Zhou, Yiling Chen, Qi Chu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01277v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01277v1)

**Summary:** Although pretrained joint audio-visual diffusion models offer rich control over \emph{what} to generate, they provide no explicit control over \emph{when} an utterance should occur. To address this, we study \emph{inference-time speech scheduling}, a novel task that places coupled speech and visual articulation within user-specified begin--end intervals without finetuning the backbone model. We uncover two intrinsic properties of the denoising process that enable this task. First, a timing-sensi...

---

### 36. Seeing the World and the Self from Egocentric Video

**Authors:** Kai Guan, Minchao Jiang, Ruichen WangLi, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01276v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01276v1)

**Summary:** Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different predi...

---

### 37. MeRoPE: Metric Rotary Position Embedding for Camera-Controlled Video Generation

**Authors:** Zhijian Qiao, Xinjiang Wang, Jiajie Chen, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01252v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01252v1)

**Summary:** In camera-controlled video generation, geometry-aware positional encodings condition tokens on camera extrinsics and per-token viewing rays. Existing schemes, however, have a scale-dependent failure mode on real-world metric camera trajectories: homogeneous projective encodings cause attention logits and feature norms to grow unbounded with physical translation baselines. We propose MeRoPE (Metric Rotary Position Embedding), a norm-preserving relative camera encoding for attention. MeRoPE encode...

---

### 38. One Prompt Is Enough: Watermark Laundering Through Foundation Image Models

**Authors:** Jidong Yang, Qi Li, Wei Zong, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01249v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01249v1)

**Summary:** Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that comb...

---

### 39. S$^2$Prune: Spatially Structured Visual Token Pruning for Multimodal Large Language Models

**Authors:** Yuanyuan Jia, Shunpu Tang, Qianqian Yang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01224v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01224v1)

**Summary:** Visual token pruning reduces the inference overhead of multimodal large language models (MLLMs) by retaining only a subset of visual tokens. Existing methods usually select tokens based on importance or redundancy. However, we observe that these criteria produce stable spatial biases across inputs and do not always outperform simple Uniform Grid sampling, highlighting the value of broad spatial coverage. Motivated by this, we propose S$^2$Prune, a training-free pruning method that preserves spat...

---

### 40. Compressing AI Traffic: Standardized Neural Network Coding of Visual-Token Representations in Split Vision-Language Inference

**Authors:** Reza Heidari, Hamed R. Tavakoli, Juho Kannala

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01200v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01200v1)

**Summary:** When the visual encoder and the language decoder of a vision-language model (VLM) run on different compute nodes, the intermediate visual-token embeddings become a communicated payload rather than an internal activation. We call such machine-consumed intermediate tensors AI traffic and ask how far they can be compressed with a standardized, training-free codec. We insert ISO/IEC 15938-17 Neural Network Coding (NNC) round trips on the complete visual interface of a Qwen3-VL-8B-Instruct video ques...

---

### 41. Monocular Depth Estimation from a Single Image: Progress and Opportunities

**Authors:** Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01172v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01172v1)

**Summary:** Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of res...

---

### 42. Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement

**Authors:** Chujie Qin, Zilong Zhang, Zewei Chang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01148v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01148v1)

**Summary:** Image retouching is commonly formulated as enhancing overall visual quality through color adjustment, but in practice, it also serves to emphasize visual focus by guiding viewers' attention toward a specific subject or region. Achieving such focus-oriented retouching is inherently challenging, as it requires well-coordinated global and local adjustments to manipulate perceptual saliency while maintaining visual naturalness. This intricate process typically demands substantial professional expert...

---

### 43. On the Design Fundamentals of Pixel Text Representation Learning

**Authors:** Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01147v1)

**Summary:** Text-rich visual inputs require models that can read, retrieve, and compress language directly in pixel space, yet existing pixel-text encoders struggle with fixed resolution pretraining, visual shortcut learning, weak visual grounding, and multilingual visual text understanding. In this work, we investigate the fundamental design principles required for robust visual text representation learning. Through systematic controlled ablations, we identify four critical components: variable image resol...

---

### 44. StainPresetNet: Stain Preset Network for Fast Multi-to-Multi Stain Normalization

**Authors:** Hongtao Kang, Die Luo, Li Chen, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01146v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01146v1)

**Summary:** Stain normalization reduces color variations caused by variations in staining protocols and imaging conditions, thereby enhancing computer-aided diagnostic system performance. Traditional methods derive mapping relationships from individual or limited reference images through pixel-wise transformation, offering style flexibility but suffering from inaccurate color mapping extraction. While existing deep-learning-based approaches achieve accurate dataset-wide color mapping through complex neural ...

---

### 45. Revisiting Face Recognition for Monozygotic Twins: The Celeb Twins Test Set

**Authors:** Michael Zang, Haiyu Wu, Mrinal Sharma, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01141v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01141v1)

**Summary:** Past literature on face recognition for monozygotic (("identical") twins points to facial marks and mirror asymmetry as possible directions for improved accuracy of twins recognition. The Celeb Twins Test Set (CTTS) contains web-scraped image pairs for 80 sets of celebrity twins. It is the only twins test set with meta-data for twins with distinguishing skin marks and possible mirror asymmetry. CTTS is organized in the manner of face verification test sets such as LFW, CALFW, CPLFW, CFP-FP, and ...

---

### 46. Different Changes Require Different Reasoning: Change-Type-Specialized Experts for Robust Change Captioning

**Authors:** Jiyoung Park, InJae Oh, Jung Uk Kim

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01136v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01136v1)

**Summary:** Change captioning is the task of generating natural language descriptions that explain the changes between a pair of images. Although different change types (e.g., color shifts, object additions) exhibit distinct visual cues and require specialized reasoning processes, existing methods often overlook these distinctions. To address this limitation, we propose Multi-Expert Diagnosis for Image Change (MEDIC), a novel framework that introduces change-type awareness by explicitly modeling change cate...

---

### 47. P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement

**Authors:** Ruoyu Guo, Haonan Zhong, Maurice Pagnucco, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01123v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01123v1)

**Summary:** Recent advancements in low-light image enhancement have leveraged diffusion models for their strong ability to generate perceptually realistic, detailed images. Patch diffusion models further offer a promising solution to size-agnostic image restoration while improving efficiency. However, existing methods typically rely on small, fixed patches (e.g., 64$\times$64) that cannot capture image-level brightness context, whereas enlarging the receptive field improves brightness and colour estimation ...

---

### 48. When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP

**Authors:** Shota Sato, Hajime Kiyama, Tosho Hirasawa, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01103v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01103v1)

**Summary:** Reducing the modality gap between image and text representations in CLIP is widely expected to improve cross-modal alignment and downstream performance. However, a smaller average image-text gap does not necessarily lead to consistent accuracy gains. We analyze this mismatch from the perspective of the decision structure in zero-shot classification, i.e. selecting the most similar class-text prototype for an input image. Zero-shot accuracy depends not only on average image--text alignment, but a...

---

### 49. IT-TextFusion: Iterative Text-Image Interaction with Text-Guided Residual Refinement for Degradation-Aware Image Fusion

**Authors:** Siyang Liu, Peiyi Zhou, Tianle Jin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01092v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01092v1)

**Summary:** Text-guided image fusion has recently emerged as an effective paradigm for integrating multi-modal information while enabling flexible and task-oriented fusion control. However, existing text-guided fusion methods often rely on shallow semantic-visual interaction and limited attention mechanisms, which restrict their ability to robustly handle complex degradations and fully exploit textual guidance. In this paper, we propose an iterative text-guided image fusion framework that incorporates text-...

---

### 50. Let Confidence Change, Not the Prediction: Prediction-Preserving Repair for Post-hoc Calibration

**Authors:** Daehwan Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01072v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01072v1)

**Summary:** Post-hoc calibration corrects reported confidence, yet a multiclass calibrator can also change the associated top-1 prediction. Accuracy captures only the net effect of these changes on correctness, not how often predictions change; the Top-1 Prediction Change Rate (TPCR) instead measures this frequency. We propose Calibrator-Output Repair for Top-1 Decision Preservation (CORD), the first post-fit adapter to impose exact prediction preservation by repairing the full calibrated probability vector...

---

## cs.LG

**50 papers**

### 1. Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation

**Authors:** Himil Vasava, Ming Jiang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01604v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01604v1)

**Summary:** LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-l...

---

### 2. Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

**Authors:** Haoyuan Deng, Haichao Liu, Wenkai Guo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01596v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01596v1)

**Summary:** Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around a joint action-wrench proposal: a causal wrench history is aligned with vision-language semantics and kinematic state, and flow matching gen...

---

### 3. The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally

**Authors:** Jundong Hu, Shekar Ramachandran

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01587v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01587v1)

**Summary:** Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) across 9 open-weight models in 4 architecture families, we test 3 intuitive hypotheses: that quantiz...

---

### 4. Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs

**Authors:** Jingtan Wang, Arun Verma, Xiaoqiang Lin, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01573v1)

**Summary:** How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad trends (e.g., SFT dominates in low-data regimes), lacks a principled allocation framework, and does not examine whether the optimal ratio transfers across model sizes. We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal...

---

### 5. Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers

**Authors:** Matteo Merler, Giovanni Bonetta, Davide Zago, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01567v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01567v1)

**Summary:** Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertai...

---

### 6. Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks

**Authors:** Jing Xiao, Xinhai Chen, Qinglin Wang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01558v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01558v1)

**Summary:** Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constr...

---

### 7. Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories

**Authors:** Nabira Rashid, Manolis Kellis

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01556v1)

**Summary:** We evaluate embedding retrieval where surface form and meaning are pulled apart on purpose: retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol, competition mathematics (MathNet-Retrieve; 500 queries, 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries, 336 trajectories). In mathematics the failure is complete: strict Hit@1 at the heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% C...

---

### 8. Can LLMs Discover Scientific Laws in Real and Parallel Worlds?

**Authors:** Yiming Huang, Ziche Liu, Zhuohang Wu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01552v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01552v1)

**Summary:** Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constraints. As LLM capabilities advance and their role in AI for Science expands, it remains an open problem whether they can genuinely discover scientific laws and how this ability should be evaluated. Existing evaluations, however, often either simplify discovery through synthetic settings or reuse publ...

---

### 9. A Mathematical Theory of Reusable Neural Bases for Network Compression

**Authors:** Binshuai Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01550v1)

**Summary:** As large AI models become increasingly prevalent across a wide range of applications, memory cost has become a critical bottleneck in both training and inference. To mitigate this issue, we introduce the Linear Reusable Neural Bases Architecture (LRNBA), a novel framework aimed at improving parameter efficiency and reducing memory cost. Inspired by recurrent neural network (RNN) designs, the core idea of our approach is to represent each network block as a linear combination of a shared set of n...

---

### 10. NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games

**Authors:** Tomáš Holeček, Viliam Lisý

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01549v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01549v1)

**Summary:** Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning faces severe identifiability barriers, which we argue make centralized model learning a mathematical necessity. Building on this analysis, we propose NashDreamer, a principled MBRL fra...

---

### 11. Variable Selection for Feature-Based Newsvendor

**Authors:** Zhaoliang Yuan, Jie Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01544v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01544v1)

**Summary:** Feature-based newsvendor models use observable covariates to tailor inventory decisions, aiming to balance holding and shortage costs under demand uncertainty. However, high-dimensional feature sets often hinder interpretability and inflate data collection and implementation costs. This paper studies variable selection for the feature-based newsvendor problem under a hard cardinality constraint on the number of selected features. We formulate the resulting $\ell_0$-constrained empirical newsvend...

---

### 12. Quantum Sparse Autoencoders for Q-Matrix Estimation in Cognitive Diagnosis

**Authors:** Arif Hassan Zidan, Yi Pan, Bowen Guo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01537v1)

**Summary:** Q-matrices play a central role in cognitive diagnosis within educational data mining (EDM), specifying which latent skills each assessment item requires. Data-driven Q-matrix estimation remains challenging when assessments involve many correlated skills and when real response patterns depart from idealized generative assumptions. We introduce a novel quantum sparse autoencoder (QSAE) for Q-matrix estimation, which, to the best of our knowledge, is the first application of quantum machine learnin...

---

### 13. Sierpiński--Knopp Wasserstein Distance for Persistence Diagrams and Applications to 2-Wasserstein Approximation

**Authors:** Sebastien Tchitchek, Julien Tierny

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01528v1)

**Summary:** This paper introduces the Sierpiński-Knopp (SK) Wasserstein distance, a fast metric between persistence diagrams. The SK-Wasserstein distance, denoted $d_{\mathrm{SK}}$, maps diagram points and their diagonal projections to the unit interval via the Sierpiński-Knopp space-filling curve on the upper diagonal triangle. The encoded point sets are then efficiently matched via one-dimensional optimal assignment, in \(O(N\log N)\) steps, yielding an explicit diagonal-aware point assignment between the...

---

### 14. LatentPress: Context Compression Beyond Text and Vision

**Authors:** Zhengze Zhou, Hejian Sang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01507v1)

**Summary:** Compressed context is usually carried as human-readable text or as rendered images that must be decoded, even when its consumer is a language model. We introduce LatentPress, which writes conversational histories and long documents into a third representation: continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference. A small reader-matched writer compresses $4$-$16\times$ while training only an adapter (4.2M-26....

---

### 15. Optimizing Byzantine Node Placement in Decentralized Federated Learning

**Authors:** Edoardo Gabrielli, Gabriele Tolomei

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01495v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01495v1)

**Summary:** Security evaluations of decentralized federated learning (DFL) typically focus on how Byzantine participants behave, while largely overlooking which participants are compromised. Yet, because aggregation is distributed over a communication graph, the placement of Byzantine nodes determines how malicious influence propagates through the network. We therefore treat Byzantine placement as an explicit adversarial decision and formulate the attacker's objective as selecting, under a fixed compromise ...

---

### 16. Rethinking Learnability in Offline Data-driven Optimization

**Authors:** Chao Qian, Chen-Guang Wang, Rong-Xi Tan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01493v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01493v1)

**Summary:** Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization improves the efficiency of BBO algorithms by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires no additional online evaluations. Many offline optimi...

---

### 17. Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds

**Authors:** Clinton Enwerem, John S. Baras, Calin Belta

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01453v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01453v1)

**Summary:** Dexterous manipulation policies learned by imitation are typically evaluated for robustness to variation in scenes, objects, or instructions, but their performance across task execution speeds is less often examined. This leaves open how much temporal robustness a learner retains relative to the expert it imitates. We compare an expert and learner under the same task conditions, initial-condition draws, and speedup factors. We instantiate the evaluation in ParcelStow, a contact-rich task in whic...

---

### 18. Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning

**Authors:** Mariia Drozdova, Aidan Sirbu, Pietro Miotti, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01449v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01449v1)

**Summary:** Diffusion models and recursive reasoners are both iterative, but they carry information across iterations differently. We add a persistent hidden state to a diffusion denoiser and remove its timestep conditioning, leaving a single shared update that can be run to arbitrary depth. The result is an anytime solver: accuracy keeps improving with inference depth far beyond the rollout lengths and backpropagation window used in training, reaching 99.90% exact solve on Sudoku-Extreme. We also obtain 98...

---

### 19. Edge-Girth as a Structural Edge Feature for Graph Neural Networks

**Authors:** Lilian Marey, Charlotte Laclau

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01441v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01441v1)

**Summary:** Graph neural networks (GNN) based on message passing are provably no more powerful than the one-dimensional Weisfeiler--Leman colour-refinement test (1-WL): two graphs it cannot tell apart receive identical representations, however deep or wide the network. A common remedy augments node or edge features with precomputed structural descriptors, most often counts of a fixed small subgraph such as triangles or longer cycles, but such counts require committing in advance to the size of the substruct...

---

### 20. Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search

**Authors:** Zhiliang Chen, Sebastian Ament, David Eriksson, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01431v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01431v1)

**Summary:** Optimal hyperparameter scaling laws describe how the best hyperparameters for large language model (LLM) training change with model and data scale, enabling practitioners to predict optimal configurations at production scales without expensive large-scale tuning. However, estimating these scaling laws conventionally requires exhaustive grid searches over thousands of training runs, consuming enormous computational resources. We introduce Power-Law Entropy Search (PLES), a computational cost-awar...

---

### 21. Learning Sparse Decision Trees via Transformer Variational Auto-Encoders

**Authors:** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01430v1)

**Summary:** Decision trees are among the most widely used models in machine learning, largely due to their transparent decision logic, making them well-suited for high-stakes decision-making contexts. However, most existing learning algorithms focus on predictive performance, overlooking the joint optimization of other desirable properties, such as structural sparsity. In this work we propose TREVIS, an approach for learning decision trees with respect to complex objectives, based on the exploration of the ...

---

### 22. TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution

**Authors:** Ruocan Wei

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01428v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01428v1)

**Summary:** Large Language Model (LLM) agents based on the ReAct paradigm have demonstrated remarkable capabilities in tool use and task execution. However, ReAct suffers from a fundamental efficiency problem: every query triggers a complete reasoning loop from scratch, and similar queries repeat identical steps without leveraging historical experience. We propose TRIAGE,a three-level routing framework that reduces token consumption by reusing historical execution trajectories. Its core innovation is TaaS (...

---

### 23. Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading

**Authors:** Fatemeh Javadian, Zhu Chen, Zahra Aminparast, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01426v1)

**Summary:** Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map ch...

---

### 24. CATeye: Coupled Attribute-Topology Invariance Learning for Voucher Abuse Detection

**Authors:** Tian Tian, Shuaicheng Niu, Hao Kuang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01425v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01425v1)

**Summary:** Voucher abuse poses a major challenge in e-commerce, where malicious users exploit promotional vouchers for profit. Unfortunately, fraud patterns evolve rapidly over time and across regions, causing distribution shifts that degrade existing detection models unless retrained frequently. To tackle this, we propose the Coupled Attribute-Topology Invariance Learning framework (CATeye). The key challenge arises from coupled attribute-topology shift, where edges built from attribute proximity cause en...

---

### 25. Provably Safe Sim-to-Real Transfer

**Authors:** Tingting Ni, Maryam Kamgarpour

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01418v1)

**Summary:** To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in man...

---

### 26. Predicting Subsurface Abnormalities Growth using Physics-Informed Neural Networks

**Authors:** Mehrdad Shafiei Dizaji, Hoda Azari

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01417v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01417v1)

**Summary:** The research explores the pioneering integration of Physics-Informed Neural Networks (PINNs) into the domain of Ground-Penetrating Radar (GPR) data prediction. This research presents a detailed development framework for a specialized PINN model, proficient at interpreting and forecasting GPR data, much like how medical imaging models predict tumor behavior. By harnessing the synergy between deep learning algorithms and the physical laws governing subsurface structures or in medical terms, human ...

---

### 27. On the Reliability of Generative Augmentation: A Wasserstein-Based Theoretical and Empirical Study

**Authors:** Chathurika S Abeykoon, Mathias Nthiani Muia, Mallory Goldstein

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01410v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01410v1)

**Summary:** Generative data augmentation is widely used to mitigate class imbalance, yet its theoretical effect on downstream generalization remains poorly understood. In this work, we develop a statistical framework for conditional generative augmentation and analyze its impact on classification risk. We formalize augmentation as a distribution-mixing process and show that the resulting risk distortion is controlled by both the augmentation strength and the class-conditional Wasserstein discrepancy between...

---

### 28. Contribution-Aware Bandwidth Allocation for Multimodal Split Learning

**Authors:** Iason Ofeidis, Leandros Tassiulas

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01406v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01406v1)

**Summary:** Multimodal models are increasingly the default option for perception at the network edge, yet they are trained almost entirely in the datacenter, because a client holding several sensor streams cannot host an encoder per modality. Split Learning makes such training feasible by keeping only the first layers on the device, at the cost of an uplink that must carry smashed activations for every modality at every step. Existing compression schemes give each modality the same keep-ratio, so the shared...

---

### 29. Measuring consistency via ensemble margin and local prediction variability: Auditing decision systems in the presence of predictive multiplicity

**Authors:** Sinjini Banerjee, Tim Marrinan, Anand D. Sarwate

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01397v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01397v1)

**Summary:** The Rashomon effect is a machine learning phenomenon where equally accurate models produce different predictions for the same inputs (predictive multiplicity). Existing work primarily focuses on multiplicity within individual models, but in more complex decision systems, the impact of the Rashomon effect is less well understood. In this work, we study multiplicity from the perspective of auditing incorrect ensemble predictions, where the decision to divert an instance for human review is based o...

---

### 30. Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA

**Authors:** Nishant Mishra, Ameen Abu-Hanna, Iacer Calixto

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01361v1)

**Summary:** Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometrically, that implies that true and false statements separate along a stable direction in hidden state space, i.e., the truth direction. Prior work disagrees on whether this generalises across input shifts, but the disagreement is hard to interpret because cross-dataset probe transfer experiments confound several kinds of input change at once. We i...

---

### 31. Exact Risk-Complexity Laws for Projective Boundaries in Scenario Optimization and Distribution-Free Certification

**Authors:** Giuseppe C. Calafiore

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01355v1)

**Summary:** Scenario optimization, conformal prediction, and related distribution-free certification methods use finite samples to construct decisions or prediction sets with violation-risk guarantees for fresh observations. In several classical settings, the conditional violation risk follows an exact beta law, whose tail has a beta-binomial representation and whose parameter is a support, calibration, or compression dimension. This paper identifies the deterministic boundary mechanism behind these formula...

---

### 32. Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR

**Authors:** Esther Xin

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01354v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) and standard benchmark evaluation both rely on an automatic verifier that turns a free text answer into a binary reward. Prior work reports that one evaluation harness accepts only about 94% of its own ground truth answers, blaming LaTeX parsing. That is an aggregate: it does not say which answer forms consume the error budget. We supply the decomposition. We apply metamorphic testing to the verifier rather than the model, generating certifie...

---

### 33. Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades

**Authors:** Dushyant Rajput

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01345v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01345v1)

**Summary:** Inference cascades cut cost by answering most queries with a cheap model and escalating a hard tail to a frontier model that acts as verifier. A natural extension closes the loop: fine-tune the cheap student on the verifier's rejections so the escalation rate, and cost, fall each round. We measure this loop on real LLMs and report four findings. First, the verifier's blind spot, the fraction of the student's wrong answers it accepts, is large and moves adversarially: it grows with student capabi...

---

### 34. SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers

**Authors:** Shaowen Wang, Ge Zhang, Kairong Luo, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01343v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01343v1)

**Summary:** Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matchi...

---

### 35. mzCache: On-Device LLM Memory Management under Multitasking

**Authors:** Hongseung Yu, Minsung Kim, Jongseok Park, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01338v1)

**Summary:** On-device mobile Large Language Model (LLM) inference is gaining significant attention. However, mobile devices operate in highly dynamic multitasking environments where users frequently switch between applications. This creates memory pressure, forcing LLM memory (model weights and KV cache) to be evicted by the operating system. When a new inference request arrives, the inference system must restore the evicted memory through slow storage reads or recompute the entire KV cache, severely degrad...

---

### 36. Bandits in Prod: Hyperparameter Optimization at Inference Time

**Authors:** Louis Abraham, Tuan-Anh Nguyen, Nicolas Devatine

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01335v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01335v1)

**Summary:** Many production systems can assess a configuration only by using it on live requests and observing noisy feedback. Modern agentic systems are a prominent example, with inference-time choices such as model selection, retrieval depth, prompting strategy, and decoding temperature, yet often with no representative validation data. We formalize this setting as Online Hyperparameter Optimization (OHPO) and cast it as an infinitely many-armed bandit over mixed and conditional search spaces. We introduc...

---

### 37. Exploring Sparse Autoencoders in Text-Based Causal Confounding Adjustment

**Authors:** Mian Zhong, Katherine A. Keith, Anjalie Field

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01322v1)

**Summary:** In many settings, studying causal questions based on text data requires adjusting for confounding information within texts. Yet there is a tradeoff in constructing text representations for adjustment: they must be sufficiently large and/or dense to preserve the confounding variables necessary for unbiased effect estimation, but sufficiently small and/or sparse to satisfy finite-sample overlap and yield low-variance estimates. To address this tradeoff, we turn to sparse autoencoders (SAEs), and p...

---

### 38. Matched Queries for Curvature and Density at Branching Junctions

**Authors:** Ziqi Zhao, Qingjian Ni

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01319v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01319v1)

**Summary:** At a junction, a score field can reveal weighted tangent rays, yet these first-order quantities do not determine how individual branches bend or how their densities change away from the center. Recovering this missing information is necessary for describing local continuation beyond a single point, but finite observations must separate branchwise second-order effects while allowing error in the estimated center. We address this inverse problem using matched score queries at noise scales $σ$ and ...

---

### 39. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

**Authors:** Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01316v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01316v1)

**Summary:** Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing tha...

---

### 40. One-Layer Transformer Provably Learns Multiclass One-Nearest Neighbor in Context

**Authors:** Skanda Athreya, Yutong Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01311v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01311v1)

**Summary:** We extend recent work establishing an equivalence between one-layer transformers and nearest-neighbor classifiers in the binary setting to the multiclass case. By leveraging the simplex encoding, we show that one-layer transformers with an argmax classification head behave identically to a one-nearest-neighbor classifier in the multiclass setting. This closes a gap left by prior work, whose multiclass result relied on a non-standard rounding-based approach rather than the typical argmax head use...

---

### 41. GazeRefine: Expert Gaze as a Test-Time Prompt for Training-Free Medical Image Segmentation

**Authors:** Mohammed Oussama Benyahia, Marouane Tliba, Mohamed Amine Kerkouri, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01310v1)

**Summary:** Medical image segmentation remains difficult to scale because high-performing methods typically rely on dense expert annotations and task-specific training. We introduce GazeRefine, a training-free framework that uses gaze as an inference-time prompt for zero-shot medical image segmentation. Sparse, duration-weighted fixations are converted into foreground and background priors that initialize semantic prototypes in frozen DINOv3 feature space. These prototypes are iteratively refined through fo...

---

### 42. Relational Task Generation Language: A Declarative Specification Framework for Relational Deep Learning

**Authors:** Oleksii Kolesnichenko, Jakub Peleška, Gustav Šír

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01292v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01292v1)

**Summary:** Relational Deep Learning (RDL) has become a powerful paradigm for learning from multi-tabular data. However, manually defining RDL prediction tasks is a laborious process that frequently results in data leakage. To address this issue, we introduce Relational Task Generation Language (RTGL) - an open-source declarative language that streamlines RDL task formulation by abstracting away low-level SQL details. We showcase RTGL by reconstructing existing RDL benchmark tasks and uncovering their incon...

---

### 43. The Constitutional Coverage Trilemma in AI Governance

**Authors:** Natalija Mitic, Soona Sedahmed A. O., Mamadou Selly Ly, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01275v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01275v1)

**Summary:** Frontier AI systems function as \emph{constitutional institutions}: each deployed model encodes an implicit ranking among safety, helpfulness, honesty, autonomy, and equity. We ask whether the supply of frontier constitutional types covers human demand. Combining a paraphrase-controlled audit of the as-shipped default constitutions of $23$ frontier LLM archetypes with a pairwise-tradeoff study of $1{,}649$ US participants on the same instrument, we report three facts. \emph{Demand is broad}: it ...

---

### 44. Position: Privacy Is a Claim, Not a Property of Synthetic Data

**Authors:** Jiachen Zhao, Antonia Januszewicz, Taeho Jung

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01273v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01273v1)

**Summary:** Synthetic data has become a common component of machine learning research. While widely adopted, its use in privacy-sensitive contexts has quietly shifted from a claim of residual inference risk under stated assumptions to an appearance-based property inferred from data generation itself. In this position paper, we argue that this shift reflects an implicit change in community standards for what counts as sufficient privacy evidence, rather than a misunderstanding of well-established privacy pri...

---

### 45. Solving In-Table Prediction Problems by Deep Neural Networks with Performance Evaluation Using Synthetic Data

**Authors:** Xiao Zhao, Daniela Oelke

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01262v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01262v1)

**Summary:** Tabular deep learning (TDL) leverages neural networks (NN) to extract patterns from tabular data. Traditional TDL methods follow a supervised learning paradigm, where a target feature is explicitly given. In this work, however, we explore a different approach by employing deep NNs to learn relationships among individual columns within a given table. We investigate whether NNs can predict the values of arbitrarily selected columns in a given table based on the remaining known columns. We call thi...

---

### 46. Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents

**Authors:** Liming Pu, Xiaoxia Li, Yifu Liu, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01245v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01245v1)

**Summary:** Reinforcement learning is a natural way to post-train LLM agents for long-horizon interactive tasks judged only by end-of-task verification, yet a shared belief holds that outcome-only RL soon hits a ceiling on small open models. Recent work therefore compensates around the training with denser rewards, SFT priors, skill libraries, curated memory, or multi-agent orchestration. We argue the ceiling is an artifact of two failures of common practice. Signal starvation: group-relative RL with sparse...

---

### 47. Post-Training Science for Supervised Fine-Tuning

**Authors:** Charles O'Neill, Mudith Jayasekara, Harry Partridge

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01244v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01244v1)

**Summary:** Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset. Here we measure them under one instrument: a sweep that varies one lever at a time, and spans dense and mixture-of-experts models in two families (Qwen3 and Llama), on four real-world customer SFT datasets, for both L...

---

### 48. From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs

**Authors:** Jie Chen, Xiangqian Yu, Yanchao Lian, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01240v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01240v1)

**Summary:** Scaling Transformers has driven large gains in language modeling, but transplanting this to behavior-sequence modeling in production ranking is challenging: recommendation differs in signal quality, where behavior sequences are noisy, temporally irregular, and sparsely supervised, and in computation asymmetry, where each request scores many candidates against one shared user history under tight latency budgets. We propose ReST, a recommendation-native Transformer scaling framework. For signal qu...

---

### 49. Multi-Head Self Attention is a Parameter Identification Mechanism

**Authors:** W. Ross Morrow

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01231v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01231v1)

**Summary:** We prove that a multi-head scaled dot product attention can be viewed as a parameter identification strategy. The ratio of unidentified parameters to the total number of parameters scales like the reciprocal of the number of heads ($1/2 \to 1/(2H)$), meaning models with more heads are structurally more identified. A subtle side effect of the mathematics observation that attention can never be fully identified. Similarly we also show that some bias terms can have no effect on softmax-based attent...

---

### 50. REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs

**Authors:** Riyaaz Shaik, Chandru Venkataraman

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01215v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01215v1)

**Summary:** Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's d...

---

## cs.NE

**50 papers**

### 1. Rethinking Learnability in Offline Data-driven Optimization

**Authors:** Chao Qian, Chen-Guang Wang, Rong-Xi Tan, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01493v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01493v1)

**Summary:** Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization improves the efficiency of BBO algorithms by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires no additional online evaluations. Many offline optimi...

---

### 2. Neural Symbollic Regression Using Deep Learning and Sparse Modelling

**Authors:** Ravi Kumar U, Sumitra S

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01102v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01102v1)

**Summary:** Symbolic Regression (SR) seeks to find succinct mathematical expressions that represent the fundamental relationships within data, providing interpretability and scientific understanding that exceeds that of black-box models. Nevertheless, traditional methods like Genetic Programming face challenges with scalability and are highly sensitive to noise, while sparse regression techniques such as SINDy rely significantly on predetermined feature libraries. In this work, we present a Neural Symbolic ...

---

### 3. Web Price Extraction: State of the Art and an Adaptive Browserless Implementation

**Authors:** Evgeniia Kositsyna, Jorge Lloret-Gazo

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01030v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01030v1)

**Summary:** Price extraction from websites is a key task for market monitoring, price comparison, and business analytics in e-commerce. Existing approaches can be broadly divided into four groups, and understanding their trade-offs in accuracy and scalability is essential for selecting suitable extraction strategies. Classical methods rely on manually written wrappers and rule induction from labeled pages, offering high accuracy but adapting poorly to structural changes and requiring considerable maintenanc...

---

### 4. Denoising Diffusion Generative Models Secretly Calculate Attentions

**Authors:** Farzan Haddadi, Leila Monfared, Ebrahim Rezaii, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00885v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00885v1)

**Summary:** Denoising diffusion models are the dominant architecture for image generation, whereas most natural language generation and modeling are primarily handled by well-known transformer architectures employing attention mechanism. Here, we show that diffusion models also inherently use an attention mechanism very similar to that of transformers. Therefore, attention emerges as a universal machine learning principle, based on a general training objective. We also show similarities in basic functional ...

---

### 5. Self-Reports Are Not Verification: Environment-Grounded Auditing of LLM Operators in Evolutionary Search

**Authors:** Enrong Pan, Ryan Zhou, Ting Hu

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00652v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00652v1)

**Summary:** Language model agents increasingly propose actions, observe external feedback, and explain their own behavior. Their confidence and rationales are convenient monitoring signals, but convenience is not verification. We introduce an environment-grounded audit in which every intermediate proposal receives an exact outcome. A language model operates an evolutionary Contexto search whose feedback function assigns every valid guess an exact rank without human annotation. Across 200 runs spanning five ...

---

### 6. GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning

**Authors:** Wenjian Wu, Zesheng Jia, Jiaying Tang, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00577v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00577v1)

**Summary:** Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely attributable to weak modeling of local geometric structures and the fact that conflicting task selections are handled only after action generation. To address these limitations, we propose...

---

### 7. Investigating Hyperparameter Optimization and Transferability for ES-HyperNEAT: A TPE Approach

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00449v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00449v1)

**Summary:** Neuroevolution of Augmenting Topologies (NEAT) and its advanced version, Evolvable-Substrate HyperNEAT (ES-HyperNEAT), have shown great potential in developing neural networks. However, their effectiveness heavily depends on the selection of hyperparameters. This study investigates the optimization of ES-HyperNEAT hyperparameters using the Tree-structured Parzen Estimator (TPE) on the MNIST classification task, exploring a search space of over 3 billion potential combinations. TPE effectively na...

---

### 8. Where Should Experience Live? Hierarchical Hebbian Memory for Continual Vision Transformers

**Authors:** Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00358v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00358v1)

**Summary:** Vision Transformers provide strong visual representations but typically rely on slowly updated parameters, limiting their ability to organize newly acquired information across different memory timescales. This work proposes \textit{Hierarchical Hebbian Memory}, a three-level memory architecture composed of rapid Working Memory, persistent Routed Episodic Memory, and slower Semantic Memory. A learned controller regulates memory contribution, read and write routing, plasticity, retention, and cons...

---

### 9. Flawed in Nature, Perfect through Evolution

**Authors:** J. M. Diederik Kruijssen

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00129v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00129v1)

**Summary:** The performance of artificial intelligence (AI) and machine learning (ML) models degrades when the problem they were trained on drifts. This is a near-universal feature of real-world problems, which often change unpredictably. Biological evolution has achieved intelligence by overcoming this obstacle through natural selection acting on heritable variation. AI/ML techniques have long incorporated forms of natural selection, but it has been challenging to maintain model diversity as optimization n...

---

### 10. Conjoint Audio-to-Spikes Encoding and Processing for Efficient Neuromorphic Speech Recognition

**Authors:** Valentin M. Meunier, Amélie Gruel, Pierre Lewden, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30792v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30792v1)

**Summary:** Obtaining data from neuromorphic sensors and processing it with Spiking Neural Networks is a promising solution to lower the energy cost of artificial intelligence. The current rarity of natively neuromorphic datasets promotes the development of software tools to translate input sensory data into spikes. However, highly bio-mimetic simulators can be challenging to implement on digital hardware. In this work, we evaluate the neuromorphic encoding and subsequent classification of audio into spikes...

---

### 11. Event-Driven Language Models with Sparse Neural Activity for Neuromorphic Hardware

**Authors:** Simon Richter, Ruhai Lin, Jason Yik, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30439v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30439v1)

**Summary:** Inference with transformer-based large language models (LLMs) is often limited by the memory-bound KV cache and quadratic attention cost. State-space models (SSMs) mitigate this through linear attention and fixed-size recurrent states, but their large dense linear projections remain computationally expensive even after quantization. We introduce a method that induces sparse neural activity in heavily quantized linear-attention models with minimal performance loss. Activations below a per-project...

---

### 12. "More Is Different'' in Neural Circuits: Algebraic Emergence of Effective Theories in Canonical Recurrent Motifs of Biological Neuronal Networks

**Authors:** Nima Dehghani

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30231v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30231v1)

**Summary:** Canonical neural circuit motifs are usually described functionally: divisive normalization rescales population activity by a pooled signal, and winner-take-all competition selects one pattern through recurrent excitation and shared inhibition. We represent them, and their compositions, algebraically as finite transformation systems and analyze the transition monoids generated by their input-conditioned updates, distinguishing structure already present in a generator from structure that appears o...

---

### 13. TPR-Attention for Combinatorial Generalization

**Authors:** Melisa Civelekoğlu, Isabeau Prémont-Schwarz

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30124v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30124v1)

**Summary:** Systematic generalization remains a significant challenge in deep learning. In particular, combinatorial generalization - generalizing to new configurations of known factors of variation - is effortless for humans but difficult for standard neural architectures that rely on statistical correlations rather than explicit structural representations. We introduce a new architectural component that embeds structured inductive bias into deep learning: an attention mechanism operating over tensor-produ...

---

### 14. Multiclass Linear Perceptrons with Multiplicative Margins

**Authors:** Dmitri Rachkovskij, Evgeny Osipov, Olexander Volkov, et al.

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30028v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30028v1)

**Summary:** This paper introduces a family of multiclass linear Perceptron classifiers with a multiplicative margin mechanism (MMPerc), as an alternative to standard margin-free and additive margin Perceptrons. The multiplicative formulation enforces classification confidence by requiring the true class score to exceed that of competing classes by a specified fraction of itself, rather than by a fixed additive threshold. This avoids dependence on score magnitudes arising from varied norms of data and class ...

---

### 15. Evolutionary Soups: Evolving Mixture-of-Experts for Multi-Objective LLM Alignment

**Authors:** Lingxiao Kong, Steffen Staab, Cong Yang, et al.

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.29978v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29978v1)

**Summary:** Large language models are increasingly required to generate responses that satisfy multiple competing objectives. Since optimal trade-offs depend on both user preferences and input prompts, controllable multi-objective generation must dynamically adapt models at inference time without retraining. To address this, we propose Evolutionary Soups, a mixture-of-experts framework for fine-grained generation control, with gating networks trained via an evolutionary algorithm. The per-layer gating netwo...

---

### 16. PruneShift: A Framework for Evaluating Decision Reliability in Structured Pruning

**Authors:** Hao Ye, Gaopeng Zhang

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.29765v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29765v1)

**Summary:** Structured pruning uses surrogate objectives because direct task evaluation over every feasible mask is too expensive. Most evaluations report average surrogate error or rank correlation on broadly sampled masks. These summaries do not directly test the mask chosen by the surrogate. We introduce PruneShift, an evaluation framework that separates broad predictive fidelity, fidelity near selector outputs, and the quality of the selected pruning decision. We first prove that Spearman and Kendall ag...

---

### 17. Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks

**Authors:** Ludovic Boulanger, Sean U. N. Wood

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28493v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28493v1)

**Summary:** Cochlear implants (CI) restore hearing for individuals with severe to profound hearing loss. However, CI users often struggle to understand speech in noisy environments. Deep neural networks (DNN) have shown promise in enhancing speech for CI users, yet their high energy demands make them non-ideal for low-power CI processors. Spiking neural networks (SNN), on the other hand, offer comparable performance with significantly lower energy consumption. Hence, we propose a novel SNN inspired by the D...

---

### 18. The thermodynamic freedom of a thermodynamic computer

**Authors:** Stephen Whitelam

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.27938v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27938v1)

**Summary:** Thermodynamic computers are stochastic physical devices designed to perform calculations at the thermal energy scale. Their operation is constrained by the equations of stochastic thermodynamics, among which are a set of bounds, known as speed limits, that relate a thermodynamic computer's run time to its computational progress and the heat it dissipates. Using the Wasserstein speed limit we assess the thermodynamic efficiency of a simulation model of a thermodynamic computer trained to perform ...

---

### 19. Tensor-Accelerated Eager Multi-Resolution Grids for Evolving Large-Scale Substrates

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27612v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27612v1)

**Summary:** In neuroevolution, indirect encoding generates neural network connectivity from a compact genome rather than specifying each connection. ES-HyperNEAT automatically discovers where to place hidden nodes by examining CPPN output patterns: it recursively subdivides space using a quadtree, expanding regions where CPPN outputs show high variance. This adaptive approach discovers network topology without manual substrate specification, extending the fixed-grid HyperNEAT framework built on NEAT.   Howe...

---

### 20. ANTShapes Benchmarking Datasets for Event-Based Neuromorphic Object Classification

**Authors:** M. Middleton, H. Kayan, B. Sen Bhattacharya, et al.

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27150v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27150v1)

**Summary:** Object classification in event-based computer vision is a task that is attracting considerable research attention. Event-based object classification is a fundamental task in the fields of security and applied computer vision, which typically use synchronous frame-based cameras and computing pipelines for operation. This approach has several practical flaws. The size, weight and power consumption of the device could prohibit deployment at the extreme edge or in covert sensing environments. Beside...

---

### 21. Bug Localization from Bug Reports: A Multi-Objective Approach

**Authors:** Waleed Ahmad, Mehtab Kiran Suddle, Maryam Bashir

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27089v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27089v1)

**Summary:** Bug localization is a labor-intensive task, particularly in large software systems. When abnormal behavior occurs, developers must perform repetitive and time-consuming steps to identify faulty files. Previous studies have mainly focused on single-objective localization methods, many of which are limited to specific programming languages. In addition, relying solely on lexical similarity between source code and bug reports is often insufficient due to the natural language nature of bug descripti...

---

### 22. Asymmetric Coupling Anisotropy for Causal Information Filtering in Physical Reservoirs

**Authors:** Takashi Hikihara, Yuma Aoki

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.26741v1) | 📄 [PDF](https://arxiv.org/pdf/2608.26741v1)

**Summary:** We demonstrate a physical mechanism for causal information filtering in a physical reservoir computing (PRC) by exploiting asymmetric coupling anisotropy. Using a network of coupled Duffing oscillators, we show that the directionality of internal coupling induces a spatial gradient in the effective potential, establishing a deterministic upstream-to-downstream information flow. This anisotropy allows for the selective amplification of semantic drifts, triggering a macroscopic saddle-node bifurca...

---

### 23. Benchmarking spiking neural networks across sensing modalities on edge devices

**Authors:** Xin Du, Di Yu, Changze Lv, et al.

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2609.00026v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00026v1)

**Summary:** Edge computing systems need to support diverse sensing workloads under tight energy and memory constraints, thereby motivating deployment-aware model selection. Spiking neural networks (SNNs) are a promising alternative to conventional artificial neural networks (ANNs), yet systematic evidence for when and why they provide practical advantages remains limited. Here, we present a benchmark of SNNs across five sensing modalities and multiple edge devices, systematically evaluating spike encoding, ...

---

### 24. Beyond Edge Cuts: Activity-Weighted Multicast Hypergraph Mapping for Spiking Neural Networks on Mesh NoCs

**Authors:** Amirreza Khorasanian

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.26223v1) | 📄 [PDF](https://arxiv.org/pdf/2608.26223v1)

**Summary:** Mapping spiking neural networks (SNNs) onto neuromorphic many-core platforms is often formulated with graph partitioning and pairwise placement costs. That abstraction is convenient, but it does not match the physical communication event: one spike from a source neuron is delivered to a set of postsynaptic destinations, and routes to several destinations can share mesh links. We present M-HySMap, a route-aware, activity-weighted multicast hypergraph mapping framework. Each source neuron induces ...

---

### 25. Synthesis of Hopfield Neural Network: Novel Results

**Authors:** Garimella Rama Murthy

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.25481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25481v1)

**Summary:** Using the logical basis of synthesizing Hopfield Neural Network with desired corners of hypercube as stable states (proposed in [1]), it is proved that more corners of hypercube can be programmed as stable states (whether the number of neurons is even or odd). The research paper presents a new perspective to the so called "Programming Problem" of Hopfield Neural Network.

---

### 26. Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species Gene Function Prediction

**Authors:** Azrin Sultana

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.25466v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25466v1)

**Summary:** The functional annotation of genes in non-model organisms remains a significant challenge in computational biology, with 20-70% of sequenced genes lacking characterized functions. Traditional homology-based methods are often costly and strongly dependent on high sequence similarity. This study presents Homo-RAG, a framework for large language model-based gene function prediction that integrates homology-guided multi-hop retrieval with evidence-aware ranking. The framework exploits biological rel...

---

### 27. ES-AHD: An Evolution Strategy Framework for Automatic Heuristic Design

**Authors:** Yutao Lai, Kezhao Lai, Hai-Lin Liu, et al.

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2609.00023v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00023v1)

**Summary:** In this paper, we introduce ES-AHD, a novel framework that fundamentally integrates Evolution Strategy (ES) into Large Language Model (LLM)-driven Automatic Heuristic Design (AHD). Existing evolutionary approaches predominantly rely on random, individual-level mutation, leading to blind search and an imbalance between exploration and exploitation. To address these issues, ES-AHD introduces two core mechanisms. First, Semantic Recombination via LLMs discards traditional point-to-point reproductio...

---

### 28. Directed walks shape a universal square-root law of entropy production rate in nonreciprocal systems

**Authors:** Thiparat Chotibut, Ewa Gudowska-Nowak, Maciej A. Nowak

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.25030v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25030v1)

**Summary:** The entropy production rate (EPR) quantifies irreversibility of a nonequilibrium steady state, yet standard formulas obscure how a complex interaction network generates it. For multivariate Ornstein-Uhlenbeck dynamics on such networks, we express the EPR as a quadratic form in antisymmetric matrices measuring the nonreciprocity of aggregate directed walks at every length, and, equivalently, as two weighted-walk quantities: pairs of directed walks sharing both endpoints, and directed closed walks...

---

### 29. Parameterized Complexity of $L_p$-Lipschitz Constants for Input Convex Neural Networks and $L_p$-Norm Maximization over Zonotopes

**Authors:** Aritra Das, Vincent Froese, Moritz Grillo, et al.

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24865v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24865v1)

**Summary:** Lipschitz constants are a standard way to quantify the sensitivity of neural networks to small input perturbations, but computing them is difficult even for shallow ReLU networks. We study this problem for two-layer input-convex neural networks (ICNNs), a restricted architecture where nonnegative output weights enforce convexity. Computing the $L_p$-Lipschitz constant for these networks is equivalent to maximizing the dual norm over a zonotope. While $L_1$- and $L_\infty$-norm maximization on zo...

---

### 30. Learning Whom to Trust : Decision-Generated Credibility in Social Learning

**Authors:** Gabriel Bontemps, Abhishek Banerjee

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24851v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24851v1)

**Summary:** Social interaction can improve collective learning but also amplify early mistakes. We study this tension when the credibility of social information is generated by the sender's own decision process rather than fixed ex ante. Reinforcement-learning agents make binary choices through a drift--diffusion process that jointly determines choice, decision time, and confidence; decision confidence then becomes social credibility by weighting anticipatory influence and retrospective social learning. Und...

---

### 31. Single State Update Predictive Coding training for Time Series Forecasting and Anomaly Detection

**Authors:** Matteo Cardoni, Sam Leroux

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24697v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24697v1)

**Summary:** Predictive Coding (PC) is a neural learning paradigm that enables parallelizable neural network layer updates. However, the main bottleneck of PC Networks (PCN) is the sequential backwards error propagation. To tackle this, we introduce a training technique that pairs a Generative PCN with a support Encoding PCN. The two PCNs are trained in parallel to match their neural activations, without sequential propagation. We apply this to time series anomaly detection and show that our approach results...

---

### 32. On Scaling Coordinate-Based Neuroevolution: The Quadtree Bottleneck in ES-HyperNEAT

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24480v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24480v1)

**Summary:** ES-HyperNEAT evolves substrate topology through adaptive quadtree subdivision; to our knowledge, no implementation with full population-level GPU parallelization exists. We present JAX-ESHN, a JAX-based implementation targeting GPU parallelization with batched CPPN queries, and benchmark it against the CPU-based PUREPLES Baseline across five tasks: XOR, Parity-3, circle classification, sine regression, and CartPole. The core limitation is structural: each CPPN discovers a unique set of substrate...

---

### 33. ORBITALIF: An Efficient Spiking Federated Learning Framework for Onboard Cloud Removal

**Authors:** Bohan Zhang, Chenyu Xu, Yijie Mao, et al.

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24073v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24073v1)

**Summary:** Low-earth-orbit (LEO) satellites enable high-resolution, large-scale Earth observation for applications such as disaster monitoring and environmental surveillance. However, cloud coverage often obscures the Earth's surface, and conventional cloud-removal pipelines that download cloudy images to ground stations for processing suffer from limited contact windows, constrained satellite-to-ground bandwidth, and high latency. In this work, we propose a novel satellite federated learning framework for...

---

### 34. Trust, but Verify: Rigorously Profiling Best-Effort High-Performance Computing for Digital Evolution

**Authors:** Matthew Andres Moreno, Santiago Rodriguez Papa, Charles Ofria, et al.

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.23955v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23955v1)

**Summary:** Developments in high-performance computing (HPC) technology continue to drastically increase quantities of available processing power. In the context of digital evolution, this explosive growth offers opportunities to advance both hypothesis-driven explorations of multi-scale biological phenomena and application-driven evolutionary optimization targeting hard problem domains. A particular opportunity arises from emerging next-generation AI/ML hardware accelerator platforms, such as the 880,000-p...

---

### 35. Coronavirus Optimization Algorithm: A Success-History Adaptive Evolutionary Framework with Archive-Assisted Search and Stagnation Recovery for Global Optimization

**Authors:** Hari Mohan Pandey

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23847v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23847v1)

**Summary:** This paper proposes the Coronavirus Optimization Algorithm (COA), a SARS-CoV-2-inspired success-history adaptive evolutionary optimizer for box-constrained continuous global optimization. COA does not model disease transmission; instead, it maps selected coronavirus mechanisms to explicit search operators, including elite-guided attraction, trial-vector generation, adaptive parameter variation, stagnation recovery, and population-size scheduling. The algorithm combines opposition-based initializ...

---

### 36. Response Renormalization for Critical Deep Equilibrium Models

**Authors:** Jose Luis Lima de Jesus Silva

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23725v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23725v1)

**Summary:** Deep Equilibrium Models (DEQs) compute predictions from a hidden representation unchanged by the model update. Training through this equilibrium uses implicit differentiation and requires solving an adjoint system built from the residual Jacobian. If this Jacobian is nearly singular along loss-sensitive directions, small perturbations can be strongly amplified in the adjoint response, producing large, highly sensitive gradients that can make optimization unreliable. We introduce Response Renorma...

---

### 37. Integer Natural Evolution Strategies

**Authors:** Jacob de Nobel, Diederick Vermetten, Hao Wang, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23714v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23714v1)

**Summary:** While contemporary Evolution Strategies handle integer optimization problems effectively, their adaptation mechanism is grounded in $\ell_2$-based Gaussian models, which are not native to the integer lattice. In contrast, the $\ell_1$-norm provides the natural measure of displacement on $\mathbb{Z}^n$, with the double geometric distribution as its canonical mutation operator. In this work, we derive a fully $\ell_1$-native step-size adaptation mechanism from first principles and propose an Integ...

---

### 38. FormuEvo: LLM-Guided Evolution for Discovering Solver-Efficient Mixed-Integer Programming Formulations

**Authors:** Haofeng Yuan, Jianing Peng, Jieyi Bi, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23353v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23353v1)

**Summary:** Mixed-integer programming (MIP) lies at the core of operations research and industrial optimization. While large language models (LLMs) have recently shown promise in automated MIP modeling from natural language, they prioritize semantic correctness but overlook formulation strength, severely bottlenecking the efficiency of downstream solvers. We propose FormuEvo, an LLM-guided evolutionary framework for automated discovery of solver-efficient MIP formulations. FormuEvo frames MIP formulation de...

---

### 39. Mycelial Search: A Graph-Structured Metaheuristic for Continuous Optimisation

**Authors:** Mohammad Mahdi Dehshibi

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23323v2) | 📄 [PDF](https://arxiv.org/pdf/2608.23323v2)

**Summary:** Continuous optimisation methods need to balance sharing information and maintaining alternative search directions. In this paper, we introduce Mycelial Search (Myco), a graph-structured metaheuristic designed around active tips, community-weighted flow, adaptive cord plasticity, and anchor-based injection. Candidate solutions form an evolving spatial graph in which a Louvain partition distinguishes within-community from cross-community information exchange. Adaptive cord plasticity subsequently ...

---

### 40. Spicing up Genetic Netlist Generation with LLMs

**Authors:** Stefan Uhlich, Yağız Gençer, Andrea Bonetti, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23317v1)

**Summary:** Analog circuit topology synthesis remains challenging because useful designs occupy a tiny fraction of a combinatorial search space, and small structural changes can induce highly nonlinear changes in behavior. Evolutionary algorithms are attractive because they can optimize over discrete circuit topologies using only black-box evaluations, but they often require many SPICE simulations and may converge prematurely. We introduce LLM-SPICEMixer, a hybrid synthesis framework that augments genetic n...

---

### 41. Basins of Attraction to Multiple Fixed Points in Discrete-time Hysteresis Neural Networks

**Authors:** Yuta Arai, Seigo Nakamura, Ryoga Nakamura, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23225v2) | 📄 [PDF](https://arxiv.org/pdf/2608.23225v2)

**Summary:** This paper studies multiple fixed points in a discrete-time hysteresis neural network. The network consists of binary hysteresis neurons characterized by the threshold parameter. Depending on the parameter, the network can have a variety of multiple binary fixed points. Stability of each fixed point is characterized by basin of attraction (BOA): the set of initial points falling into the fixed point. In order to evaluate the distribution of BOA sizes, we present entropy. In order to escape from ...

---

### 42. JANUS: Online Jacobian-Aligned Infill for Black-Box Optimization

**Authors:** Hongyuan Yu, Pufan Xu, Jiaojiao Yi, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.22862v1) | 📄 [PDF](https://arxiv.org/pdf/2608.22862v1)

**Summary:** Population optimizers such as CMA-ES, DE, and multi-objective evolutionary algorithms drive search mainly through selection signals that are scalar or rank based: such a signal indicates that one candidate outperforms another, but not the local direction responsible for the improvement. JANUS (\emph{Jacobian-Aligned Newton-Unified Search}) is a plug-and-play infill module that extracts this missing local geometric signal without replacing the host optimizer. It estimates a local Jacobian from th...

---

### 43. Spiking Neural Networks for Continuous Control: Neuromorphic Reinforcement Learning in Conventional Computing

**Authors:** Jessica Hunter, Md Maruf Hossain Shuvo, Krishna Roy

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.22729v1) | 📄 [PDF](https://arxiv.org/pdf/2608.22729v1)

**Summary:** Reinforcement learning (RL) algorithms have made strides over the past decade applying them to a wide range of problems and control tasks. However, the deployment of RL on neuromorphic hardware for continuous control tasks remains under-validated. Namely it is unclear whether replacing a conventional actor network with a spiking neural network (SNN) affects the performance of an agent before any hardware-specific benefits manifest. We provide a systematic validation of a minimal, neuromorphicall...

---

### 44. Basin-Preserving Discretizations of Modern Hopfield Retrieval Dynamics: Energy Cells, Dissipation, and the Attention Limit

**Authors:** Francisco R. Villatoro

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.21304v1) | 📄 [PDF](https://arxiv.org/pdf/2608.21304v1)

**Summary:** The retrieval dynamics of a modern Hopfield network is the gradient flow of a log-sum-exp energy, while the attention update is its exact difference-of-convex minimization step. We study which time discretizations preserve not only energy decay and equilibria but also basins of attraction. We introduce energy cells, connected components of sublevel sets containing one attractor and no other critical point. Our main theorem shows that every finite energy cell below the escape energy is contained ...

---

### 45. Fine-Grain GPU Parallelization of the Generalized Partition Crossover for Large-Scale Traveling Salesman Problems

**Authors:** Swetha Varadarajan, Darrell Whitley

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.21233v1) | 📄 [PDF](https://arxiv.org/pdf/2608.21233v1)

**Summary:** The Traveling Salesman Problem (TSP) is one of the most extensively studied NP-hard optimization problems. Genetic Algorithm (GA)-based solvers, such as the Edge Assembly Crossover (EAX), achieve state-of-the-art performance on many benchmark instances. However, the scalability of these approaches in massively parallel architectures remains limited because crossover operations involve irregular memory access patterns, graph traversals, and sequential dependencies. Existing GPU-based TSP solvers ...

---

### 46. Event-triggered Implicit Perturbation for Zeroth-Order Fine-Tuning of Spiking Transformers

**Authors:** Tengteng Lei, Prabodh Katti, Rashi Dutt, et al.

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.21223v1) | 📄 [PDF](https://arxiv.org/pdf/2608.21223v1)

**Summary:** Zeroth-order (ZO) optimization estimates gradients using only forward-pass evaluations, making it suitable for fine-tuning non-differentiable, event-driven spiking neural networks (SNNs). However, its deployment on in-memory computing (IMC) accelerators is constrained by the repeated read-modify-write (RMW) operations arising from explicit weight perturbation and the prohibitive hardware footprint of random number generators (RNGs) for statistically independent per-weight perturbations. To addre...

---

### 47. Free-Probability Kernels for Zero-Rollout Hyperparameter Selection in Reservoir Computing

**Authors:** Sara Malacarne, Andrea Ceni, Claudio Gallicchio

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.20998v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20998v1)

**Summary:** Reservoir computing (RC) couples a fixed recurrent dynamical system with a trained lightweight readout, but this efficiency is partly lost during hyperparameter selection: the recurrent gain, input scale, and leakage rate determine the reservoir's stability and temporal processing regime and are usually tuned through many rollouts. We introduce a deterministic, pilot-informed selector for leaky linear reservoirs followed by coordinate-wise nonlinear features. Free probability yields cross-lag pr...

---

### 48. Enhanced Artificial Neural Networks Using QHAdamW in Air Quality Forecasting

**Authors:** Mary Joy Daniel Vinas

**Published:** 2026-08-20

🔗 [Paper](http://arxiv.org/abs/2608.21463v1) | 📄 [PDF](https://arxiv.org/pdf/2608.21463v1)

**Summary:** The study employed an Artificial Neural Network in combination with the optimized Adaptive Moment Estimation (Adam) algorithm, currently the only AQI forecasting model available in the Philippines. The modified QHAdamW - Quasi-Hyperbolic Momentum (QHAdam) and Adam with decoupled weight decay (AdamW) were both extensions of the Adam optimizer, and both offer unique advantages for training ANN. The proposed QHAdamW optimizer addresses the issues on convergence, generalization, and forecasting perf...

---

### 49. Uncertainty propagation in auto-regressive random neural network models

**Authors:** Janice Adams, Daniele Venturi

**Published:** 2026-08-20

🔗 [Paper](http://arxiv.org/abs/2608.20483v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20483v1)

**Summary:** We develop analytical and particle-based methods for uncertainty propagation in random neural network models, where both the inputs and network parameters are allowed to be random. Building on the piecewise-linear structure of the Leaky ReLU activation function, we derive a local approximation of the neural network output with respect to perturbations in both its inputs and parameters. This approximation is exact for perturbations that preserve the network activation pattern, and it allows us to...

---

### 50. Petri Net Description of Biological Neural Circuits for Fast Hardware Prototyping

**Authors:** Carlo daCunha, Rodrigo Pena, Marcos Turqueti

**Published:** 2026-08-20

🔗 [Paper](http://arxiv.org/abs/2608.20147v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20147v1)

**Summary:** Current approaches to simulating biological neural circuits, whether on general-purpose hardware or dedicated neuromorphic platforms, remain constrained by fixed-timestep numerical integration, hardware-imposed precision limits, and an inability to guarantee timing correctness for event-driven spiking dynamics under real-time constraints. Here, we propose a Petri net description of biological neural circuits that overcomes these limitations by modeling neurons, synapses, and spike events as a T-...

---

## q-bio.NC

**50 papers**

### 1. Active Visual Semantics: A large-scale MEG and eye-tracking dataset for understanding visual intelligence in action

**Authors:** Philip Sulewski, Carmen Amme, Peter König, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01055v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01055v1)

**Summary:** Here we present the Active Visual Semantics (AVS) dataset, a large-scale collection of magnetoencephalography (MEG) and eye-tracking data recorded while five participants freely explored 4,080 natural scenes over 10 sessions each, yielding more than 200,000 fixation epochs in total. Unlike existing neuroimaging datasets that rely on passive viewing with enforced central fixation, AVS captures brain activity during active scene exploration, including self-generated saccades and fixations. A seman...

---

### 2. Temporally constraining source imaging estimates in an underdetermined neural system with eigenmodes of cortical geometry

**Authors:** Pok Him Siu, Philippa J. Karoly, Artemio Soto-Breceda, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00809v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00809v1)

**Summary:** Geometric eigenmodes provide a compact and biologically grounded representation of large-scale neural activity. Previous work demonstrated that they can mitigate the underdetermined nature of electroencephalographic (EEG) and magnetoencephalographic (MEG) source localisation, an ill-posed inverse problem in which neural activity is reconstructed from non-invasive recordings. Beyond their spatial structure, neural field theory predicts the temporal evolution of eigenmodes through analytically der...

---

### 3. A distributed-delay Wilson-Cowan model of sleep-related rhythms in the corticothalamic system

**Authors:** Eva Kaslik, Anca Radulescu, Anca Stanoev

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00520v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00520v1)

**Summary:** The corticothalamic circuit supports rhythms with timescales that differ by orders of magnitude: sleep spindles, the sigma-band events of non-rapid-eye-movement (NREM) sleep, and infra-slow fluctuations near 0.02Hz that organize when spindles occur. Because the anatomy is the same in both cases, architecture alone cannot determine which rhythm the circuit expresses. We ask whether the temporal structure of the circuit's own feedback can. In a four-population Wilson--Cowan model comprising cortic...

---

### 4. "More Is Different'' in Neural Circuits: Algebraic Emergence of Effective Theories in Canonical Recurrent Motifs of Biological Neuronal Networks

**Authors:** Nima Dehghani

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30231v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30231v1)

**Summary:** Canonical neural circuit motifs are usually described functionally: divisive normalization rescales population activity by a pooled signal, and winner-take-all competition selects one pattern through recurrent excitation and shared inhibition. We represent them, and their compositions, algebraically as finite transformation systems and analyze the transition monoids generated by their input-conditioned updates, distinguishing structure already present in a generator from structure that appears o...

---

### 5. Local connectivity balance shapes population dynamics in random recurrent networks

**Authors:** Shotaro Takasu, Richard Gast, Ann Kennedy

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30008v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30008v1)

**Summary:** Disordered dynamical systems comprising many interacting units, from ecological communities to neural circuits, are ubiquitous, and understanding how connectivity shapes their collective behavior is a central theoretical challenge. One long-recognized feature of neural circuits is local connectivity balance, in which the excitatory and inhibitory weights converging onto each unit approximately cancel. Although local connectivity balance has been proposed to serve functions such as gating incomin...

---

### 6. Rate-Coding Bundle Memory: A Unified Model of Memory and Control for Symbolic Computation in the Brain

**Authors:** Teun van Gils, Rowan P. Sommers, Markus Ostarek, et al.

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29189v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29189v1)

**Summary:** We propose a neurobiologically plausible model of cognition that combines the advantages of connectionist and symbolic systems, and that can explain a wide range of cognitive phenomena. This model, called Rate-Coding Bundle Memory (RCBM), is based on the Symbolic Subsystem Hypothesis, which posits that the brain implements a symbolic subsystem within its fundamentally connectionist nature. RCBM is a hybrid model that uses rate coding to represent symbols in a continuous space, and it uses a bund...

---

### 7. Front-end and Back-end Computational Modeling of 40-Hz Auditory Steady-State Response Abnormalities in Schizophrenia

**Authors:** Wenjun Xia, Yan Xu, Zhengdi Zhang

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29104v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29104v1)

**Summary:** 40-Hz ASSR is reduced in schizophrenia, but it is unclear if this reflects altered auditory input or cortical E/I dynamics. We hypothesized that similar group differences could arise via distinct model mechanisms. EEG gamma% and ITPC from 21 HC and 21 SCZ constrained an auditory front-end coupled to a Wilson-Cowan E/I model. We compared front-end-restricted, back-end-restricted, and full-joint parameter searches, plus perturbation and fixed-point analyses. HC means exceeded SCZ for both metrics ...

---

### 8. Structurally Informed Connectivity Disruptions in Cocaine Use Disorder

**Authors:** Seyed Majid Razavi, Saeed Tajik Hesarkuchak, Triet M. Tran, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28892v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28892v1)

**Summary:** Cocaine Use Disorder (CUD) is associated with widespread alterations in large-scale functional brain networks, yet the mechanisms contributing to these changes and their relationship to clinical and cognitive outcomes remain poorly understood. To address this gap, we introduce a framework to extract structurally informed dynamic functional connectivity patterns. We then leverage these connectivity patterns to characterize differences in functional brain network organization associated with CUD a...

---

### 9. A large dataset of human EEG responses to short naturalistic videos for studying dynamic visual event processing

**Authors:** Alessandro T. Gifford, Pablo Oyarzo, Anne W. Zonneveld, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28768v2) | 📄 [PDF](https://arxiv.org/pdf/2608.28768v2)

**Summary:** Vision neuroscience has experienced a surge in the collection and use of large-scale datasets of brain responses to naturalistic images. However, static images lack the temporal dimension essential for understanding how vision is solved in the brain during dynamic real life settings. To facilitate the study of the neural correlates of dynamic visual event perception, we introduce the EEG Moments Dataset (EMD). EMD consists of 128-channel EEG responses and eye-tracking recordings of 6 human parti...

---

### 10. Adaptive self-organized criticality in deep neural networks

**Authors:** Simon Vock, Christian Meisel

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28431v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28431v1)

**Summary:** Deep neural networks are high-dimensional dynamical systems whose function depends on the stable propagation of activity and perturbations across many layers. Maintaining suitable dynamical regimes may therefore be essential for robust learning and for preventing dynamical instabilities during training. Here, we show that the global dynamical state of a deep neural network can be autonomously regulated by purely local homeostatic plasticity. Neuronal activity is inferred from responses across in...

---

### 11. Relational Knowledge Distillation Brings DNN Representations Close Enough to Humans to Be Aligned Without Supervision

**Authors:** Yuria Shimizu, Soh Takahashi, Takato Horii, et al.

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.27877v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27877v1)

**Summary:** Linking the internal representations of deep neural networks (DNNs) to human mental representations is important for using DNNs as computational models of human vision. Existing DNN representations remain insufficiently similar to human mental representations, which are not directly observable and are therefore commonly measured through large-scale similarity judgments of object images. A natural approach to narrowing this gap is to directly transfer the relational structure of human representat...

---

### 12. Leveraging a Foundation Model for the EEG-Based Diagnosis of Alzheimer's Disease

**Authors:** Maggie Lin, Chung-Lin Hou, Tzyy-Ping Jung

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27719v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27719v1)

**Summary:** Biological heterogeneity in Alzheimer's Disease (AD) poses a critical diagnostic challenge, particularly for traditional linear methods that fail to capture non-linear neural dynamics. To address this, we propose a diagnostic framework utilizing the Large Brain Model (LaBraM), pretrained on over 2,500 hours of EEG data. By integrating these high-dimensional latent embeddings with a non-linear Random Forest classifier, our approach effectively isolates robust disease markers. Under a rigorous sub...

---

### 13. A weighted model of perception and decision-making between targets of finite size

**Authors:** W. Christopher Strickland, Andrew J. Bernoff

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27670v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27670v1)

**Summary:** Recent research grounded in experiments has connected neural ring models of vision to how animals navigate a complex landscape of attractive targets. In this paper we investigate the mathematical and biological implications of a three-stage model where animals pre-process visual stimuli to identify a discrete set of targets, process this input to select the dominant targets, and then post-process this information to navigate the landscape. Incorporating finite target sizes and a neural density a...

---

### 14. Beta oscillation changes in ALS: A Dual-Site International Replication Study

**Authors:** Marit Boxum, Gabriel Rodrigues Palma, Robin Jansen, et al.

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.27003v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27003v1)

**Summary:** Reproducible biomarkers that monitor motor and cognitive dysfunction in amyotrophic lateral sclerosis (ALS) are needed. Previous work reported reduced beta-band event-related desynchronization (ERD) and attenuated post-movement event-related synchronization (ERS) in frontal and parietal channels during the sustained attention to response task (SART). We aimed to validate these findings in Dutch and Irish cohorts. A randomized SART with 128-channel electroencephalography (EEG) was performed in Du...

---

### 15. Hysteresis and multistability in network spreading with neuronal activity feedback

**Authors:** Christoffer G. Alexandersen, Dani S. Bassett

**Published:** 2026-08-27

🔗 [Paper](http://arxiv.org/abs/2608.26528v1) | 📄 [PDF](https://arxiv.org/pdf/2608.26528v1)

**Summary:** Spreading processes on networks often interact with other dynamics on the same nodes. Neurodegenerative disease provides one example: pathological proteins spread through anatomical connections, while neuronal activity influences and is altered by their spread, forming a spreading-activity feedback loop. However, models coupling pathological protein spreading and neuronal activity have largely focused on linear feedback between the two processes. Here we show that nonlinear feedback can fundamen...

---

### 16. Assessing mentalization in humans and large language models

**Authors:** Aamir Sohail, Xintong Zhong, Arkady Konovalov, et al.

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.26291v1) | 📄 [PDF](https://arxiv.org/pdf/2608.26291v1)

**Summary:** Mentalization - the ability to infer others' beliefs and intentions to guide one's own choices - is a key cognitive function underlying human social interactions. Large language models (LLMs) demonstrate behaviour consistent with humans on theory-of-mind tasks, yet whether these models can guide adaptive behaviour through mentalization is unknown. Here we use two economic games with cognitive computational modeling to uncover the latent strategies underlying mentalization in LLMs. We tested indi...

---

### 17. A spinal circuit for collective coordination

**Authors:** Laurence Picton, David Madrid, Alessandro Pazzaglia, et al.

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.25909v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25909v1)

**Summary:** The coordinated movement of animal groups is one of the most widespread social behaviors, which are generally attributed to high-order cognitive processing in the brain. Yet, collective coordination can seemingly emerge from rapid, local interactions between individuals, suggesting the existence of decentralized mechanisms of online coordination that remain to be identified. Here, we show that a low-order spinal sensorimotor circuit is required for real-time social coordination during schooling ...

---

### 18. GenAIT: Development and Validation of an Objective Generative AI Literacy Test for High School Students

**Authors:** Brett Puppart, Kristjan-Julius Laak, Jaan Aru

**Published:** 2026-08-26

🔗 [Paper](http://arxiv.org/abs/2608.25815v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25815v1)

**Summary:** There is growing international interest in generative AI (GenAI) literacy and its assessment among high school students, but objective assessment in this population remains underdeveloped. This article reports the iterative development and validation of the GenAI Literacy Test (GenAIT), an 18-item multiple-choice test measuring high school students' conceptual knowledge about GenAI, with content spanning technical, practical, and human-impact domains. Expert review of relevance, clarity, and com...

---

### 19. The Von-Neumann State-Space Transformer for neural decoding

**Authors:** Morteza Sarafyazd

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.25088v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25088v1)

**Summary:** Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons. Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets. In a standard Transformer layer, the feed-forward block applies the same operator to every token. We suggest a von-Neumann inspired hypothesis of efficient computation as an alternative for neural decoding: a ...

---

### 20. Multiscale Community-Based Fingerprinting of Signed Functional Networks

**Authors:** Sema Athamnah, Selin Aviyente

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.27483v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27483v1)

**Summary:** Objective: Recent studies demonstrate that functional connectomes contain subject-specific signatures, or \textit{fingerprints}, that can identify individuals across repeated sessions and tasks. Existing methods mostly rely on edge-level features that are sensitive to noise, difficult to interpret, and limited in their ability to generalize across tasks and datasets. Methods: We propose a multiscale community-based functional connectome fingerprinting framework that characterizes each individual...

---

### 21. Directed walks shape a universal square-root law of entropy production rate in nonreciprocal systems

**Authors:** Thiparat Chotibut, Ewa Gudowska-Nowak, Maciej A. Nowak

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.25030v1) | 📄 [PDF](https://arxiv.org/pdf/2608.25030v1)

**Summary:** The entropy production rate (EPR) quantifies irreversibility of a nonequilibrium steady state, yet standard formulas obscure how a complex interaction network generates it. For multivariate Ornstein-Uhlenbeck dynamics on such networks, we express the EPR as a quadratic form in antisymmetric matrices measuring the nonreciprocity of aggregate directed walks at every length, and, equivalently, as two weighted-walk quantities: pairs of directed walks sharing both endpoints, and directed closed walks...

---

### 22. Maternal Anxiety During Pregnancy and Predictive Processing Across Development: A Cross-Cohort Empirical Reappraisal

**Authors:** Bea R. H. Van den Bergh, Martin G. Frasch

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24983v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24983v1)

**Summary:** Prenatal maternal distress has been linked to differences in offspring brain and behavioural development, but is rarely framed computationally. Predictive-processing (PP) accounts hold that perception, cognition, and action arise from the interplay of incoming input and internally generated predictions, governed in part by precision. We reappraised eleven publications from two non-clinical prenatal cohorts for a coherent PP-compatible developmental pattern. Eight Leuven publications spanned adol...

---

### 23. Beauty is in the ELBO of the Beholder: A Variational Account of Processing Fluency in Face Perception

**Authors:** Francisco M. López, Jochen Triesch

**Published:** 2026-08-25

🔗 [Paper](http://arxiv.org/abs/2608.24219v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24219v1)

**Summary:** Facial attractiveness has been linked to statistical regularities such as symmetry and averageness, suggesting that beauty may depend on the ease with which a face is perceived. We empirically test this hypothesis by training variational autoencoders on four face datasets without attractiveness supervision and evaluating their representations on the 597 faces from the Chicago Face Database. Across models, human attractiveness ratings closely aligns with the direction defined by the VAE evidence ...

---

### 24. Primate vision reveals a missing principle for robust dynamic AI

**Authors:** Matteo Dunnhofer, Christian Micheloni, Kohitij Kar

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23790v1) | 📄 [PDF](https://arxiv.org/pdf/2608.23790v1)

**Summary:** How does an intelligent visual system combine what objects look like with how they move while remaining robust as appearance changes? We addressed this question by comparing human perception and neural activity in macaque inferior temporal cortex with representations from image- and video-based neural networks spanning recognition, segmentation, optic-flow processing and predictive world modeling. Temporal integration improved object representations, but most video recognition models generalized...

---

### 25. Dendritic structure enables powerful plasticity

**Authors:** Ben von Hünerbein, Federico Benitez, Kevin Max, et al.

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.23251v2) | 📄 [PDF](https://arxiv.org/pdf/2608.23251v2)

**Summary:** Over the past decades, it has become increasingly clear that the complex morphology of cortical neurons is more than just a quirk of evolution, and that dendritic compartments serve as computational elements in their own right, rather than just providing connections between nerve cell bodies. While most computational studies discuss the enhanced representational capabilities of multi-compartment models as compared to point neurons, we focus here on the implications of neuronal morphology for syn...

---

### 26. Temporal filling-in reduces attentional fluctuations in sustained visual attention

**Authors:** Yingyu Huang, Liying Zhan, Xiang Wu

**Published:** 2026-08-24

🔗 [Paper](http://arxiv.org/abs/2608.22722v1) | 📄 [PDF](https://arxiv.org/pdf/2608.22722v1)

**Summary:** Our capacity to maintain focus on task-relevant goals over time is constrained because attentional states wax and wane moment to moment. One theoretical account posits that temporal filling-in - filling temporal blank intervals between target stimuli - reduces attentional fluctuations to enhance sustained attention. This proposal, however, lacks direct empirical validation given the difficulty of tracking attentional fluctuations via behavioral measurements. To resolve this gap, we combined a vi...

---

### 27. Forward and reverse delay-driven hippocampal replay without symmetric plasticity

**Authors:** Georg Reich, Matthew Cook, Klaus Obermayer, et al.

**Published:** 2026-08-22

🔗 [Paper](http://arxiv.org/abs/2608.21814v1) | 📄 [PDF](https://arxiv.org/pdf/2608.21814v1)

**Summary:** Hippocampal replay is a phenomenon observed in mammals and songbirds where neural activation sequences experienced during wakeful periods are repeated during rest or sleep. This mechanism is believed to play a crucial role in episodic memory consolidation, retrieval, and planning. Interestingly, replay can occur in both forward and reverse temporal orders and across a wide range of increased speeds. The learning of activation sequences has traditionally been modeled by temporally asymmetric Hebb...

---

### 28. Non-standard memory models with indexed retrieval

**Authors:** Gabriele Scheler, Martin L. Schumann, Johann Schumann

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.27479v1) | 📄 [PDF](https://arxiv.org/pdf/2608.27479v1)

**Summary:** The standard memory models for neural networks are variants of the Hopfield network, where feature representations are stored as vectors in a matrix. Retrieval happens based on similarity between an input vector and the set of stored vectors in a content-addressable manner such that the network evolves towards the closest stored attractor. In other words, the useful property of addressing items in memory directly by index is lost in Hopfield-style neural network models ("associative memory"). In...

---

### 29. Conscious Access as Continuous-to-Discrete Translation

**Authors:** Tianming Yang

**Published:** 2026-08-21

🔗 [Paper](http://arxiv.org/abs/2608.20723v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20723v1)

**Summary:** The scientific study of consciousness frequently stalls on ontological debates regarding the "Hard Problem." This paper proposes a pragmatic pivot. Rather than asking what consciousness is metaphysically, we ask how modeling conscious access as a specific computational transformation may address existing bottlenecks in neuroscience and artificial intelligence. We introduce the Continuous/Discrete (C/D) framework, which holds that the brain implements two distinct processing regimes: System C, a ...

---

### 30. Decoding silent reading from non-invasive EEG

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-08-20

🔗 [Paper](http://arxiv.org/abs/2608.20186v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20186v1)

**Summary:** Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract fr...

---

### 31. Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis

**Authors:** Zijiao Chen, Nicholas Lu, Xinhui Li, et al.

**Published:** 2026-08-20

🔗 [Paper](http://arxiv.org/abs/2608.19902v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19902v1)

**Summary:** AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. Agents may reproduce failures including selective analysis, premature declarations of success and optimization of imperfect criteria. We present Brain Researcher, an agentic research harness operating in a neuroimaging researcher's computational environment under rules for admissible analyses, required checks and ...

---

### 32. Can extrinsic methods reveal intrinsic structure? Complementing IIT with QStr

**Authors:** Jeremiah Hendren, Matteo Grasso, Francesco Ellia, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.24928v1) | 📄 [PDF](https://arxiv.org/pdf/2608.24928v1)

**Summary:** Integrated Information Theory (IIT) proposes that all quality is structure: the quality of every experience can be characterized as a phenomenal structure and accounted for as a causal structure. The IIT method can be called intrinsic in that, first, it starts by characterizing the intrinsic structure of a single experience in an absolute sense (not relative to other experiences) and, second, it preserves this intrinsic perspective when accounting for experience in physical terms. By contrast, t...

---

### 33. Transcranial magnetic stimulation of visual-motion area V5/MT modulates sensory thalamus responses during visual speech recognition

**Authors:** Lisa Jeschke, Christa Mueller-Axt, Alejandro Tabas, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19034v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19034v1)

**Summary:** Responses in the sensory thalamic nuclei are modulated by perceptual tasks. Whether such response modulations rely on feedback from cerebral cortex in humans is unknown. Here, we addressed this question in the context of visual speech recognition: the visual sensory thalamus, i.e. the lateral geniculate nucleus (LGN), has differential BOLD-responses to visual speech than non-speech control tasks. We tested whether such response modulation relies on the function of the visual association cortex, ...

---

### 34. The Connectome and the Quest for the Functional Logic of the Drosophila Early Olfactory System

**Authors:** Aurel A. Lazar, Yiyin Zhou

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19290v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19290v1)

**Summary:** In recent decades, the early olfactory system (EOS) of the fruit fly has become a leading model for studying olfactory processing and associative memory, owing in part to a well-characterized feedforward pathway that feeds the processes underlying associative memory and by examining the role played by a handful of neurons and synapses. The recent completion of dense electron-microscopy connectomes provides high quality visualizations of every cell type, neuron, and synapse along the early olfact...

---

### 35. The Role of Grid Cells in Reducing Spatial Aliasing in Hippocampal Place Representations

**Authors:** Alexander Johnson, Obadah Ghizawi, Ali A. Minai

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18569v1)

**Summary:** Spatial aliasing occurs when two or more distinct locations produce highly similar place-cell representations, primarily due to environmental symmetry or repetitive structures. This issue is most pronounced when place representations are constructed solely from boundary vector cell (BVC) inputs, because symmetric or repetitive structures can yield indistinguishable sensory patterns across multiple locations in an environment. This work introduces grid cell signals to mitigate spatial aliasing in...

---

### 36. Categorical AI phenomenology: A first-person approach

**Authors:** Robert Prentner

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.20420v1) | 📄 [PDF](https://arxiv.org/pdf/2608.20420v1)

**Summary:** This paper develops a phenomenology-first approach to artificial consciousness by reframing consciousness as the subjective experience enacted through an agent's interface with the world. We shift the methodological focus to first-person structures, modeled mathematically by categories derived from Q-networks to capture actions and phenomenological invariants. In this framework, Q-networks are conceptualized as relational interfaces encoding agent-world interaction, analogous to how the dynamica...

---

### 37. Phase-based spatial ordinal patterns for characterizing oscillatory dynamics

**Authors:** Robison J. Santos-Silva, Bruno R. R. Boaretto, Thiago L. Prado, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17196v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17196v1)

**Summary:** The emergence of organized spatiotemporal patterns is ubiquitous in oscillatory systems, from neural populations to engineered networks. Identifying these patterns and tracking how they evolve over time remains challenging, particularly when systems exhibit transient dynamics. Here, we introduce a framework based on spatial ordinal patterns to characterize the spatiotemporal dynamics of oscillatory systems. Our approach acts directly on the phase rather than the amplitude, with additional patter...

---

### 38. Order-Sensitive Fast-Synapse Limits in Sparse Excitatory-Inhibitory Threshold-Reset Networks

**Authors:** Tonic Song

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16701v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16701v1)

**Summary:** Componentwise weak convergence of signed synaptic kernels does not, by itself, determine the fast-synapse limit of a sparse threshold-reset network. Within a causal event protocol with clamped refractoriness and smooth positive-delay kernels, we construct two families whose excitatory and inhibitory measures converge weakly to $δ_0$ while their microscopic arrival orders are reversed. A target fires in the excitatory-first family and not in the inhibitory-first family precisely when $x+a-b<θ\le ...

---

### 39. Continual-learning rules shape representational drift

**Authors:** Yikai Si, Shanshan Qin

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16141v2) | 📄 [PDF](https://arxiv.org/pdf/2608.16141v2)

**Summary:** Lifelong learning requires acquiring new knowledge without erasing the old. Yet neural population codes for familiar stimuli and behaviors change over days and weeks. This coexistence of stable memory and changing internal codes may depend on how a learning system prevents forgetting. We therefore tested whether different continual-learning mechanisms produce distinct patterns of representational drift. We trained convolutional networks on sequential image classification tasks and recurrent netw...

---

### 40. Multi-Feature Riemannian Hypergraph for Online Test-Time Adaptation of Motor Imagery Brain-Computer Interface

**Authors:** Siqi Li, Zhi Li, Tong Liu, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16134v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16134v1)

**Summary:** In clinical motor imagery brain-computer interface (MI-BCI) decoding, cross-day transferability and online operation remain two critical challenges. Hypergraphs can improve transferability by capturing higher-order sample relationships, yet existing hypergraph-based methods for online emotion recognition neglect the cross-day benefits of Riemannian geometry widely adopted in EEG transfer learning. To bridge this gap, we propose the Multi-feature Riemannian Hypergraph (MRieHy), a framework tailor...

---

### 41. A Control-Theoretic Formulation of Global Workspace Theory

**Authors:** Ryota Kanai

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15926v1)

**Summary:** Global workspace theory explains conscious access as the broadcasting of selected information to the rest of the network, but it lacks a formal criterion for identifying the mechanism that enables this access. We propose that a global workspace is a mediator, namely, a subnetwork that receives activity from distributed systems, transforms it through internal modes, and returns differentiated effects to the broader network. We formalize this claim as the Global Mediation Workspace (GMW), a contro...

---

### 42. The effect of the excitatory feedback in anticipated synchronization and phase bistability regimes in neuronal populations

**Authors:** Julio N. Machado, Joana M. G. L. Silva, Katiele V. Brito, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15449v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15449v1)

**Summary:** Anticipated synchronization (AS), in which the receiver leads the sender and the phase lag is negative, can emerge in unidirectionally coupled dynamical systems when the receiver has faster internal dynamics than the sender. In cortical-like population models, AS and bistability between AS and delayed synchronization (DS) have been reported mainly in unidirectional motifs and have been proposed as possible explanations for phase relations observed in electrophysiological recordings. Because cort...

---

### 43. Head Impact Characterization and Cellular Response of a Live-neuron cell-integrated Biomechanical Full-body Surrogate Model

**Authors:** Raisa Akhtaruzzaman, Mohammad Ibrahim Hossain, Rahid Zaman, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15418v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15418v1)

**Summary:** In this study, we develop a novel integrated framework that links the impact response with cellular dynamics using a live-neuron cell-integrated biomechanical full-body surrogate model. The impact event is simulated by allowing the surrogate model to fall from controlled seated release angles of 30-degree, 60-degree, and 90-degree. Three vertically stacked cell-culture Petri dishes, each containing live SH-SY5Y neuroblastoma cells, were placed inside the head of a commercially available surrogat...

---

### 44. Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work

**Authors:** Yuyang Zheng, Nan Li, Wenxia Deng, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15193v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15193v1)

**Summary:** As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sh...

---

### 45. Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation

**Authors:** Ehsan Ahmadi, Mojtaba Madadi Asl, Alireza Valizadeh

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15081v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15081v1)

**Summary:** Oscillatory neuronal networks exhibit complex collective responses to external perturbations that depend on both the intrinsic network dynamics and the timing of stimulation. Although phase response curves (PRCs) have become a standard tool for characterizing these responses, phase resetting alone provides an incomplete description of how transient perturbations reshape collective activity. Here, we investigate the dynamics of a balanced excitatory-inhibitory network of exponential integrate-and...

---

### 46. Synaptic delays modulate population phase and amplitude responses in oscillatory excitatory-inhibitory networks

**Authors:** Parsa Shahab Rad, Mojtaba Madadi Asl, Alireza Valizadeh

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15077v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15077v1)

**Summary:** Synaptic delays are fundamental determinants of neuronal communication and can profoundly influence the emergence and stability of cortical oscillations. Although their role in shaping network synchronization is well established, how synaptic delays regulate the collective response of neuronal populations to transient perturbations remains poorly understood. Here, we investigate the effects of synaptic delays on the phase and amplitude responses of oscillatory activity in a conductance-based exc...

---

### 47. Data-driven techniques for translational neuroscience and personalized neuro-health

**Authors:** Vishal Subedi, Shashipraba N. K. Rajakaruna, Pratyusha Sarkar, et al.

**Published:** 2026-08-13

🔗 [Paper](http://arxiv.org/abs/2608.13749v1) | 📄 [PDF](https://arxiv.org/pdf/2608.13749v1)

**Summary:** Neurodegenexrative diseases such as Alzheimer's disease and Parkinson's disease are diagnosed most reliably only after substantial, often irreversible, neuronal loss has already occurred, creating an urgent need for quantitative tools that can detect subtle, early, and individual-specific brain changes from neuroimaging data. This review surveys a broad and rapidly evolving toolkit of data-driven techniques for translational neuroscience and personalized neuro-health, organized around four compl...

---

### 48. Activity-dependent epidemic spreading on multiscale brain networks predicts Alzheimer's disease progression

**Authors:** Christoffer G. Alexandersen, Suman S. Kulkarni, Jessica T. Davis, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12647v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12647v1)

**Summary:** Neurodegenerative diseases can be viewed as spreading processes on brain networks, in which pathological proteins propagate between anatomically connected brain regions. Mathematical models have been used to study this process, but they generally ignore the influence of neuronal activity, even though experimental studies show that neuronal firing promotes protein transmission. Here, we couple a general node-activity process to susceptible--infected--susceptible dynamics. In this framework, an ep...

---

### 49. Testing the limits of past-adapted explanations by post-endpoint randomisation: anticipatory EEG as a worked case

**Authors:** George Sopasakis, Alexandros Sopasakis

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12072v1)

**Summary:** A predictive model can fit its data even when its information set is insufficient; fit alone cannot establish sufficiency. This Perspective introduces Level II-A, a new design-based inference framework to test this distinction, illustrated in anticipatory EEG using contingent negative variation. A pre-event endpoint is committed before the delay to the imperative event is randomised. That later-assigned delay thereby becomes a negative-control probe of whether past-adapted information was suffic...

---

### 50. The Rosetta Stone and Levels of Principled Inference to the Experience of Another Mind

**Authors:** Kallum Robinson, Giulio Tononi, Naotsugu Tsuchiya, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12030v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12030v1)

**Summary:** The classical problem of Other Minds has dogged philosophers for millennia; asking if we have any way to truly understand the experience of another mind. We know our own intrinsic experience by acquaintance, but can only ever hope to possess an extrinsic description of another's, with the two separated by an acquaintance gap. Structural approaches aim to characterise experience in terms of a mathematical structure, and promise a 'Rosetta Stone'; that is, a principled method to translate the cont...

---

## stat.ML

**50 papers**

### 1. Pointwise Majorization for sub-Weibull and Mixed Tail Processes with Applications in Quadratic Chaos and Ergodic Diffusions

**Authors:** Haichen Hu, David Simchi-Levi

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01576v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01576v1)

**Summary:** Classical chaining controls an indexed stochastic process through a single worst-case bound, which can obscure substantial variation across the index set. We establish the first simultaneous pointwise majorization theory for Banach-valued processes with sub-Weibull or two-metric mixed-tail increments. For an anchored sub-Weibull process on a separable index space, write $v(t):=d(t,t_0)$. Given a reference measure $μ$, the envelope at $t$ is governed by the pointwise Fernique-Talagrand functional...

---

### 2. Variable Selection for Feature-Based Newsvendor

**Authors:** Zhaoliang Yuan, Jie Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01544v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01544v1)

**Summary:** Feature-based newsvendor models use observable covariates to tailor inventory decisions, aiming to balance holding and shortage costs under demand uncertainty. However, high-dimensional feature sets often hinder interpretability and inflate data collection and implementation costs. This paper studies variable selection for the feature-based newsvendor problem under a hard cardinality constraint on the number of selected features. We formulate the resulting $\ell_0$-constrained empirical newsvend...

---

### 3. On the Reliability of Generative Augmentation: A Wasserstein-Based Theoretical and Empirical Study

**Authors:** Chathurika S Abeykoon, Mathias Nthiani Muia, Mallory Goldstein

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01410v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01410v1)

**Summary:** Generative data augmentation is widely used to mitigate class imbalance, yet its theoretical effect on downstream generalization remains poorly understood. In this work, we develop a statistical framework for conditional generative augmentation and analyze its impact on classification risk. We formalize augmentation as a distribution-mixing process and show that the resulting risk distortion is controlled by both the augmentation strength and the class-conditional Wasserstein discrepancy between...

---

### 4. Measuring consistency via ensemble margin and local prediction variability: Auditing decision systems in the presence of predictive multiplicity

**Authors:** Sinjini Banerjee, Tim Marrinan, Anand D. Sarwate

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01397v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01397v1)

**Summary:** The Rashomon effect is a machine learning phenomenon where equally accurate models produce different predictions for the same inputs (predictive multiplicity). Existing work primarily focuses on multiplicity within individual models, but in more complex decision systems, the impact of the Rashomon effect is less well understood. In this work, we study multiplicity from the perspective of auditing incorrect ensemble predictions, where the decision to divert an instance for human review is based o...

---

### 5. Matched Queries for Curvature and Density at Branching Junctions

**Authors:** Ziqi Zhao, Qingjian Ni

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01319v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01319v1)

**Summary:** At a junction, a score field can reveal weighted tangent rays, yet these first-order quantities do not determine how individual branches bend or how their densities change away from the center. Recovering this missing information is necessary for describing local continuation beyond a single point, but finite observations must separate branchwise second-order effects while allowing error in the estimated center. We address this inverse problem using matched score queries at noise scales $σ$ and ...

---

### 6. One-Layer Transformer Provably Learns Multiclass One-Nearest Neighbor in Context

**Authors:** Skanda Athreya, Yutong Wang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01311v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01311v1)

**Summary:** We extend recent work establishing an equivalence between one-layer transformers and nearest-neighbor classifiers in the binary setting to the multiclass case. By leveraging the simplex encoding, we show that one-layer transformers with an argmax classification head behave identically to a one-nearest-neighbor classifier in the multiclass setting. This closes a gap left by prior work, whose multiclass result relied on a non-standard rounding-based approach rather than the typical argmax head use...

---

### 7. Multi-Head Self Attention is a Parameter Identification Mechanism

**Authors:** W. Ross Morrow

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01231v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01231v1)

**Summary:** We prove that a multi-head scaled dot product attention can be viewed as a parameter identification strategy. The ratio of unidentified parameters to the total number of parameters scales like the reciprocal of the number of heads ($1/2 \to 1/(2H)$), meaning models with more heads are structurally more identified. A subtle side effect of the mathematics observation that attention can never be fully identified. Similarly we also show that some bias terms can have no effect on softmax-based attent...

---

### 8. Nonparametric inference for density-dependent McKean--Vlasov diffusions

**Authors:** Denis Belomestny, Ekaterina Morozova

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01166v1)

**Summary:** The present research is devoted to the nonparametric estimation of a density-dependent drift coefficient in a multivariate McKean--Vlasov diffusion from independent observations at a common time, as well as the stationary density. Under certain assumptions on the (known) potential, we reduce the problem to the one-dimensional one and construct a sieve maximum-likelihood estimator based on sparse ReQU neural networks subject to structural and Hölder constraints. Using the endpoint-adapted graded ...

---

### 9. Artificial Rosetta Stone: Constrained Maximum A Posteriori (MAP) Reconstruction of Symbolic Raga Sequences via Order-k Markov Models

**Authors:** Saanvi Raghavendran, Abhishek Bhattacharjee

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01064v1)

**Summary:** Reconstructing a damaged musical fragment is an inverse problem: the observed sequence contains partial information, while a raga encodes constraints limiting allowable completions. This paper formalizes a mathematical framework for this, proposing the Artificial Rosetta Stone (ARS). We separate three claims often conflated: a symbolic sequence can be reconstructed probabilistically; a sequence can be consistent with an explicit grammar; and a historical performance can be authenticated. We only...

---

### 10. From Truncation to Commitment: Persistent Context in Uniform Discrete Diffusion

**Authors:** Satoshi Hayakawa

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01043v1)

**Summary:** Uniform-state discrete diffusion models update all tokens in parallel while keeping every position revisable. Even when the commonly used top-$p$ rule leaves only one candidate at a position, that choice affects only the current reverse step and can be revised at the next sampling step. We ask what changes when selected hypotheses instead become persistent context for later predictions. We therefore propose committed reveal sampling (CRS), a training-free sampler that stores selected argmax toke...

---

### 11. The Multiple Timescales of Gradient Descent on the Edge of Stability: A Perturbative Derivation of the Central Flow

**Authors:** Raphaël Berthier

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01034v1)

**Summary:** The central flow of Cohen et al. (2025) is an empirically accurate continuous-time model of gradient descent at the edge of stability in deep learning, However, its derivation is heuristic. We propose a perturbative regime in which the central flow is the limit of gradient descent: we assume that the loss decomposes as $f = g + \varepsilon h$; in the limit $\varepsilon \to 0$, the dynamics of gradient descent with learning rate $η$ converge to the gradient flow of $h$ constrained to the minimize...

---

### 12. Embedded Conditional Independence Tests for Large Language Model Generated Text with an Application to German Parliament Speeches

**Authors:** Marco Simnacher, Georg Keilbar, Benjamin König, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00946v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00946v1)

**Summary:** Conditional independence tests (CITs) test for conditional dependence between two random objects $X$ and $Y$ given a third random object $Z$. Existing CITs have limited applicability to high-dimensional data, especially multimodal data like text. However, we show that such tests are of interest for large language model (LLM) outputs, where we test whether an output $X$ generated from a source text $Z$ carries information about an attribute $Y$ beyond $Z$ itself. For this purpose, we propose embe...

---

### 13. When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference Voting

**Authors:** Ariel Smogorghevski, Nir Rosenfeld, Yaniv Romano

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00905v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00905v1)

**Summary:** Sampling from distributions conditioned on desired semantic properties is an emerging challenge in modern generative modeling. Metropolis-Hastings (MH) provides a principled route to conditional sampling, but requires access to exact pointwise target-density evaluations, which are not available in generative settings. Meanwhile, pairwise comparisons by humans or model "judge" are highly accessible and have proved valuable across diverse applications. We introduce Pref-MH, a general exact MH samp...

---

### 14. Semi-Supervised Classification with Informative Missing Labels in Weibull Mixture Models

**Authors:** Jinran Wu, You-Gan Wang, Geoffrey J. McLachlan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00774v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00774v1)

**Summary:** We consider semi-supervised classification from a partially classified sample arising from a two-component Weibull mixture. The feature is observed for all data, whereas some class labels are missing. The probability of a missing label is modelled as a function of classification uncertainty, giving a feature-dependent missing-at-random (MAR) mechanism that shares parameters with the Weibull-mixture classifier. The missing-label indicators can therefore provide information about the classifier in...

---

### 15. Deep Skew-t Mixture Models

**Authors:** Jinran Wu, You-Gan Wang, Geoffrey J. McLachlan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00773v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00773v1)

**Summary:** High-dimensional clustering is challenging when component distributions are both heavy-tailed and directionally asymmetric. We propose a deep skew-$t$ mixture model (DStMM), a hierarchical factor-analytic mixture based on the generalised-hyperbolic skew-$t$ normal mean--variance representation. A shared inverse-gamma mixing variable is propagated along each complete latent pathway, allowing heavy tails and directional asymmetry to be modelled jointly while preserving conditional Gaussianity. Eac...

---

### 16. Verdict Instability of OOD Scores under Reference Resampling

**Authors:** Donghoon Lee, Shinjin Kang

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00691v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00691v1)

**Summary:** Post-hoc out-of-distribution detectors are fitted on a finite reference set, so every score they produce is an estimate. If we had chosen a different set, some verdicts would have moved. We measure that movement by resampling the reference set and recording the bootstrap standard deviation of the score, which we call verdict instability. It admits a closed form with no fitted parameters. The instability of a verdict is the within-class dispersion of the assigned class along the query's direction...

---

### 17. An efficient EM algorithm for both element-wise and structural missingness in matrix-variate normal mixture models

**Authors:** Hanzhang Lu, Jeffrey L. Andrews, Ryan P. Browne

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.00616v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00616v1)

**Summary:** Matrix-variate data with missing entries arise frequently in applications where observations are naturally organized as two-dimensional arrays. Although the matrix normal distribution provides a parsimonious model through its Kronecker covariance structure, standard EM estimation can be computationally expensive because arbitrary missingness patterns typically destroy this separability in the E-step. In this paper, we propose an efficient partial EM algorithm for matrix-variate normal data with ...

---

### 18. A convolutional framework for detecting event-driven dynamics in energy price series

**Authors:** Caixia Xu, Piotr Fryzlewicz

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00402v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00402v1)

**Summary:** This paper develops a general convolutional neural network (CNN) framework for detecting heterogeneous event-driven dynamics in univariate time series windows. We show that the induced CNN class exactly represents classifiers based on range, maximum drawup, maximum drawdown and slope change, and uniformly approximates realised volatility and autoregressive explosiveness on compact domains. We further establish error bounds for representative rules in finite samples and an oracle inequality for l...

---

### 19. Exact Global MCMC with Denoising Diffusion

**Authors:** Mitch Hill

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00279v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00279v1)

**Summary:** This work shows that diffusion models learned with standard denoising loss can provide effective global MCMC proposals for complex high-dimensional target densities. The method is motivated by the observation that sequentially applying a forward and reverse diffusion process defines a Markov chain with a target stationary distribution for an ideal denoiser trained on samples of the target distribution. This observation can be made exact for any denoiser by applying a Metropolis-Hastings step who...

---

### 20. Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost

**Authors:** Zihang Liang, Haochen Zhang, Lingzhou Xue

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00193v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00193v1)

**Summary:** We study federated online reinforcement learning with linear function approximation. While recent multi-agent reinforcement learning algorithms achieve strong regret guarantees, they typically require sharing raw trajectories. This reliance incurs a communication cost that scales linearly with the number of episodes and violates the privacy constraints of federated settings. To address these limitations, we propose Fed-LSVI, the first provably efficient federated algorithm for online reinforceme...

---

### 21. Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations

**Authors:** Shijun Zhang

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.31157v1) | 📄 [PDF](https://arxiv.org/pdf/2608.31157v1)

**Summary:** Many parameter-efficient methods generate the parameters of a large neural network from a low-dimensional latent representation. Given an architecture $Φ$ with $P_Φ$ parameter slots, we write $\boldsymbolθ_f=\mathcal{G}(\boldsymbolξ_f)$, where $\mathcal{G}\colon\mathbb{R}^M\to\mathbb{R}^{P_Φ}$ is a parameter generator and $\boldsymbolξ_f\in\mathbb{R}^M$ is a latent representation of the target function $f$. The architecture $Φ$ and the generator $\mathcal{G}$ are shared across the entire target ...

---

### 22. Implementing neural network mixed-effects models in Template Model Builder (TMB)

**Authors:** Nan Zheng, Hoi Yiu Cheung, Vibhu Sharma, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.31133v1) | 📄 [PDF](https://arxiv.org/pdf/2608.31133v1)

**Summary:** Neural network mixed-effects models (NMMs) have gained traction by combining the strong representation and predictive power of artificial neural networks with the capacity of mixed-effects modeling to capture complex correlation structures. However, existing estimation approaches rely heavily on manual derivations of objective functions and gradients, which inherently forces simplifying approximations and severely constrains the complexity and accuracy of NMMs. In this work, we introduce a gener...

---

### 23. Overcoming critical slowing down in frustrated spin systems by learned multiscale sampling

**Authors:** Gabriele Bandini, Giulio Biroli, Patrick Charbonneau, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.31114v1) | 📄 [PDF](https://arxiv.org/pdf/2608.31114v1)

**Summary:** Cluster algorithms, such as the Swendsen--Wang and Wolff methods, are among the most successful MCMC methods for mitigating critical slowing down in statistical systems. These constructive cluster algorithms, however, fail in the presence of even extremely weak frustration. Here, we sidestep this fundamental limitation by learning rather than constructing the relevant clusters. Specifically, we use the wavelet conditional renormalization group (WCRG) sampling method to learn the probability dist...

---

### 24. When Can We Work in Embedding Space? What Text Embeddings Preserve

**Authors:** Simon Freyaldenhoven

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.31059v1) | 📄 [PDF](https://arxiv.org/pdf/2608.31059v1)

**Summary:** When do text embeddings work as inputs to empirical analysis? Their use rests on an assumption: that we can trade text for its low-dimensional embedding, and lose little in doing so. I make that assumption precise under a generative model in which documents are mixtures of latent topics. I study two uses---clustering units in embedding space and controlling for high-dimensional text. A cluster of embeddings is a set of documents with similar topic mixtures; controlling for the embedding is equiv...

---

### 25. Learning the Geometry of Admissible Hypotheses through Inductive Bias in Training Distributions

**Authors:** James Crowley, Faez Ahmed, Anton van Beek

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.31028v1) | 📄 [PDF](https://arxiv.org/pdf/2608.31028v1)

**Summary:** Scientific discovery often requires reasoning over competing hypotheses that are consistent with experimental observations. For mixed-variable and combinatorial hypothesis spaces, however, constructing probabilistic representations remains challenging because both the active model components and their associated parameters are unknown. In this work, we present a framework for learning continuous latent representations of admissible partial differential equations (PDEs) by embedding a scientific ...

---

### 26. Selection-Aware Stress Testing for Interactive Agents

**Authors:** Yang Xu, Chenang Li, Jiefu Zhang, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30916v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30916v1)

**Summary:** Agent evaluations often use one benchmark to choose a workflow and then search for task types where its advantage weakens, so both conclusions are selected from the same data. We introduce Selection-Aware Semantic Stress Testing (\SASST{}), which learns a task reweighting from pre-execution features on discovery tasks and evaluates the same paired comparison on separate confirmation tasks. The protocol checks support and stability, uses joint bounds for all planned claims, and can return no clai...

---

### 27. Marginal Coordinate Test for Fréchet Regression with Random Objects

**Authors:** Jiaye Chen, Rui Qiu, Roulin Wang, et al.

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30644v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30644v1)

**Summary:** We develop a marginal coordinate test for regression with Euclidean predictors and a random-object response in a separable metric space. The goal is to test whether a predictor provides additional information about the response conditional on the remaining predictors. In a semi-supervised design, an unlabeled sample is used to estimate predictor conditional means, while an independent labeled sample is reserved for inference. The resulting residuals are combined with a product-space kernel to fo...

---

### 28. Stochastic complexity of vectors containing cluster structure

**Authors:** Daniel Nicorici, Olli Yli-Harja, Jaakko Astola

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2609.00084v1) | 📄 [PDF](https://arxiv.org/pdf/2609.00084v1)

**Summary:** This paper studies the problem of computing the stochastic probability (shortest code length) of the encoded vectors containing cluster structure using Normalized Maximum Likelihood (NML) model. This is of great theoretical and practical importance in data clustering based on Minimum Description Length (MDL) principle, such as for estimating the best number of clusters and best cluster structure for the data. Straightforward computation of the shortest code length of the vector containing cluste...

---

### 29. Informative Label Missingness in Multiclass Classification Information Geometry and Excess Risk

**Authors:** Fariborz Setoudehtazang, Geoffrey J. McLachlan

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30561v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30561v1)

**Summary:** Informative label missingness can change the usual efficiency ordering between completely and partially labelled classifiers because the pattern of missing labels may itself carry information about the classification model. We develop a general likelihood-based theory for this phenomenon in parametric multiclass classification. An efficient-information decomposition separates information lost through unavailable class memberships from information contributed by the missing-label mechanism. We th...

---

### 30. When the Martingale Never Stops Firing: Anytime-Valid Gating on Real Forecast Streams

**Authors:** Weijia Han, Lisha Qu

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30502v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30502v1)

**Summary:** Machine learning systems are increasingly corrected while they run, and the decision of when to intervene is increasingly delegated to statistical monitors. Anytime-valid inference promises evidence that can be acted on at any moment, exactly the guarantee this setting needs, and it is moving from theory into deployed monitoring. Conformal test martingales are the change-detection instrument, and Ville's inequality caps their false-alarm probability on exchangeable data. The guarantee is conditi...

---

### 31. Confounding Masquerading as Improvement: A Systematic Evaluation of Offline Reinforcement Learning for Stroke Antithrombotic Treatment in a 129,000-Patient Registry

**Authors:** Kihun Rhee

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30442v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30442v1)

**Summary:** Recent offline reinforcement learning (RL) studies report policies that outperform physician decisions on clinical outcomes. We conduct a systematic, partially crossed evaluation of five offline RL algorithm families and 14 reward designs in 44,894 post-2018 acute ischemic stroke patients from a nationwide registry (N = 129,033).   Standard Fitted Q-Evaluation (FQE) yields an apparent policy-improvement estimate of +0.0069; adding an Early Neurological Deterioration penalty increases it to +0.01...

---

### 32. Learning PDE Time-Stepping with Neural Cellular Automata

**Authors:** Esha Saha, Hao Wang

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30328v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30328v1)

**Summary:** Classical numerical solvers for partial differential equations (PDEs) are computationally expensive to solve repeatedly across varying initial conditions, motivating the need for learned surrogates. In this paper, we propose a trainable Neural Cellular Automata (NCA) based surrogate model for learning long time PDE dynamics. Rather than mapping an entire initial field to a full trajectory in one shot, our proposed model learns a small, local, homogeneous update rule that is applied identically a...

---

### 33. Estimating Population-Risk Curves Along Nonconvex Gradient Flows from the Training Sample

**Authors:** Mingzhi Song

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30261v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30261v1)

**Summary:** We estimate the conditional population-risk curve of a realized smooth nonconvex gradient flow from the training sample. Flow approximate leave-one-out (Flow-ALO) propagates a deletion response and evaluates omitted observations at approximate deleted paths. The risk-curve error decomposes into response approximation, exact-LOO fluctuation, and deletion-to-full risk transfer. On each fixed finite horizon, bounded centered training-loss gradients, a one-sided Hessian lower bound, locally Lipschit...

---

### 34. Fairness in multi-class multi-group classification problems via contextial coherent risk measures

**Authors:** Darinka Dentcheva, Xiangyu Tian

**Published:** 2026-08-31

🔗 [Paper](http://arxiv.org/abs/2608.30223v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30223v1)

**Summary:** We propose a new design of fair classifiers for multi-class classification problems in the presence of vector-valued sensitive attributes. In that scenario each sensitive attribute has multiple values and forms several groups relevant to the fairness consideration. Naturally those groups are overlapping and one should also analyze the interaction of factors. Additionally, the decision makers aided by the classification should not violate individual rights at the expense of satisfying fairness me...

---

### 35. Robust K-means Clustering using the Density Power Divergence Measure

**Authors:** Anirban Mondal, Paromita Banerjee, Abhijit Mandal

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30093v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30093v1)

**Summary:** We introduce a robust clustering method, MK-means DPD, that estimates cluster centers and covariance matrices using density power divergence (DPD) measures combined with Mahalanobis distance, making it resistant to outliers and adaptable to heterogeneous, elliptical clusters, unlike the classical K-means algorithm. Since Mahalanobis distance-based K-means lacks a general convergence guarantee, we further introduce a convergent variant, Density-Consistent MK-means DPD (DC-MK-means DPD), which red...

---

### 36. Learning Representations through Token Prediction: Geometry, Approximation, and Downstream Guarantees

**Authors:** Shulei Wang

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30072v1)

**Summary:** Token prediction is a central pre-training objective for modern language models. Despite its empirical success, why token prediction learns broadly useful representations remains incompletely understood. We develop a statistical framework connecting token prediction with representation geometry, encoder approximation, and downstream performance. Under a softmax prediction head, we show that accurate token prediction organizes token embeddings according to similarities between the distributions o...

---

### 37. A Deep Latent Variable Framework for Jointly Modeling Missingness, Measurement Error, and Heterogeneity

**Authors:** Yasin Khadem Charvadeh, Grace Y. Yi, Mithat Gönen, et al.

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.30040v1) | 📄 [PDF](https://arxiv.org/pdf/2608.30040v1)

**Summary:** Missing data, measurement error, and population heterogeneity are pervasive challenges in analyzing data arising from modern observational studies and machine learning applications. Although these problems frequently coexist and interact, they are often treated separately in existing works. We propose a unified probabilistic framework that jointly addresses these issues utilizing deep latent variable representation. The proposed method integrates a novel hierarchical tree-routed variational auto...

---

### 38. Neural ODE enhanced linear mixed effect models for estimating complex association patterns of time-varying covariates with the marker trajectory

**Authors:** Zhe Aurore Li, Quentin Clairon, Cécilia Samieri, et al.

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.29714v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29714v1)

**Summary:** Longitudinal cohort studies produce repeated data that enable the assessment of time-varying association patterns between exposures and health outcomes. Classical linear mixed-effects models (LMMs) can accommodate a large variety of association patterns while accounting for the irregularly spaced, partially observed measurement. But they require the analyst to pre-specify the functional form linking the exposure history to the outcome. We propose the Neural ODE-LMM, which embeds a Neural Ordinar...

---

### 39. Which LLM for Which Work? Budgeted Model Allocation under Uncertain Evaluation

**Authors:** Hamed Khosravi, Xiaoming Huo

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.29560v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29560v1)

**Summary:** A company with a fixed artificial intelligence (AI) budget must decide which large language model (LLM) handles each recurring workload. What it lacks is the quality table, how well each model performs on each workload. Given that table, the decision is a multiple-choice knapsack problem and is routine to solve, so estimating it is the difficulty, and that estimation fails in two ways. Models are rarely compared on the same work, and the recorded score is usually a proxy rather than the outcome ...

---

### 40. Online Gate-Driven Flow Control in Resin Transfer Moulding Using a Neural-Network Surrogate

**Authors:** Nicholas Wright, Oliver Maclaren, Piaras Kelly, et al.

**Published:** 2026-08-30

🔗 [Paper](http://arxiv.org/abs/2608.29521v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29521v1)

**Summary:** In resin transfer moulding, complete saturation of the fibre preform is necessary before the resin front reaches the outlet vent(s), to prevent dry-spot formation. In practice, the flow front rarely advances uniformly due to race-tracking effects. We propose a combined estimation and control strategy to address this issue. We use pressure-sensor data collected during filling to estimate the unknown race-tracking strengths via an iterated extended Kalman filter, and to simultaneously optimise aux...

---

### 41. Deciding When to Decide: Testing Operational Suboptimality Under Distributional Shift

**Authors:** Minxing Zheng, Holly Wiberg, Shixiang Zhu

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29465v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29465v1)

**Summary:** Deployed decisions are often optimized once and retained because updates impose operational, regulatory, or switching costs. As operating conditions change, when should such decisions be re-optimized? We study this question for stochastic optimization when the objective's functional form is known but the decision maker's trade-offs are encoded by an unknown preference parameter. Standard distribution-shift tests are poorly aligned with this goal: they can flag detectable yet decision-irrelevant ...

---

### 42. SS-ESOAP: Self-Scaled Adaptive Preconditioning for Physics-Informed Learning

**Authors:** Guangyuan Wang, Mads Toftrup, Sebastian Loeschcke, et al.

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29448v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29448v1)

**Summary:** Physics-informed neural networks (PINNs) often face ill-conditioned objectives that limit high-accuracy training. Dense quasi-Newton methods improve local conditioning but require expensive optimizer state, while Kronecker-factored methods such as SOAP scale to larger networks but rely on periodic basis updates. We introduce \method, which augments SOAP-style preconditioning with a scalar secant-energy correction adapted to Kronecker geometry and an adaptive basis update followed by variance-sta...

---

### 43. Content Exploration Beyond the Feed: Creator Supply and the Shared Corpus

**Authors:** Yuanyuan Shen, Yiren Yan, Wenjie Li, et al.

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29430v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29430v1)

**Summary:** Industrial recommenders give new content initial views through budgeted exploration, then use early performance to decide further delivery. On many short-video platforms, exploration is the primary way new videos reach viewers. Viewer-side tests measure consumption; the published budget objectives we review omit creator response. We analyze four experiments on a major short-video platform. An eight-month creator ablation finds production exploration raises videos posted per creator by 8.55% and ...

---

### 44. Signed random Fourier features for fast density estimation with indefinite kernels

**Authors:** Xie Wang, Nicolas Langrené, Wen Chen

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29265v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29265v1)

**Summary:** Kernel density estimation (KDE) is one of the most fundamental statistical estimators of density functions. Its direct implementation on a dataset of $N$ points incurs an $\mathcal{O}(N^{2})$ computational cost, which is prohibitive for large-scale datasets. Kernel approximation techniques can be applied to bring the computational cost down to $\mathcal{O}(N)$. The random Fourier features (RFF) technique, based on sampling from the spectral density of the kernel function, has become popular to s...

---

### 45. Uniform Statistical Convergence of Empirical Sinkhorn Potentials with Exponential and Polynomial Dependence on the Regularization Parameter

**Authors:** Denis Belomestny

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29152v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29152v1)

**Summary:** We study the empirical Sinkhorn estimator of the entropic optimal transport potentials under the uniform loss. Since the potentials are only unique up to additive constants, we measure the error using the quotient supremum norm, defined as $d_\infty([u],[v]) = \inf_{a\in\mathbb{R}}\|u-v-a\|_\infty$. For a fixed regularization parameter $\varepsilon>0$, we establish a non-asymptotic statistical rate of $n^{-1/2}$. This is achieved by combining the Birkhoff-Hopf contraction theorem with entropy bo...

---

### 46. PathGuide: Dynamic Classifier-Free Guidance via On-Policy Transport Alignment

**Authors:** Avishag Nevo, Tamir Hazan

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29107v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29107v1)

**Summary:** While modern generative models excel at modeling complex data, precise inference-time control in conditional generation remains a critical challenge. Classifier-free guidance (CFG) is a primary mechanism for such control, yet it is typically treated as a static tuning parameter. In flow-based models, however, the guidance scale fundamentally dictates the velocity field and the resulting probability path, making guidance selection a dynamic path-optimization problem. We introduce PathGuide, a fra...

---

### 47. Sharp Restricted Isometry Thresholds for Global Minima of Rank-Restricted Matrix LASSO

**Authors:** Richard Y. Zhang

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.29018v1) | 📄 [PDF](https://arxiv.org/pdf/2608.29018v1)

**Summary:** We determine the sharp restricted isometry threshold for recovery at global minima of the rank-restricted matrix LASSO. For target rank $r_{\star}$, if the rank-$k$ RIP constant satisfies $δ<δ_{\mathrm{sharp}}(k/r_{\star})$, where $δ_{\mathrm{sharp}}(t)=t/(4-t)$ for $0<t<4/3$ and $δ_{\mathrm{sharp}}(t)=\sqrt{(t-1)/t}$ for $t\ge4/3$, then every global minimizer has Frobenius error $\lesssim\sqrt{r_{\star}}λ$ for all $λ\gtrsim\|\mathcal{A}^{*}(ξ)\|_{\mathrm{op}}$ and at every search rank $r\ge r_{...

---

### 48. Jigsaw-CRL: Recovering Global Latent Causal Order from Fragmented Multi-Client Interventions

**Authors:** Haijie Xu, Chen Zhang

**Published:** 2026-08-29

🔗 [Paper](http://arxiv.org/abs/2608.28991v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28991v1)

**Summary:** Causal representation learning (CRL) aims to recover latent causal variables and their structural relations from high-dimensional observations. Existing CRL methods typically assume that all environments are defined over the same latent variables, or at least share a common latent representation space. We study a fragmented multi-client setting, where multiple clients interact with the same global latent causal system but each client only accesses and intervenes on a subset of the latent variabl...

---

### 49. The information geometry of product-reference discrete diffusion: Interaction growth complexity and optimal scheduling

**Authors:** Martin J. Wainwright

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28949v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28949v1)

**Summary:** We study a class of product-reference diffusion algorithms for sampling from a discrete distribution. We show that their sampling performance can be characterized using a path-based measure of data geometry that we call the interaction growth complexity (IGC). We show that a bivariate IGC kernel gives an exact representation of both the KL discretization error and a simple one-step upper bound. The simpler univariate IGC density can be used to study the effect of stepsize choices on the iteratio...

---

### 50. Representation Learning with Quantum Signal Processing

**Authors:** Junqi Wang, Junyu Liu

**Published:** 2026-08-28

🔗 [Paper](http://arxiv.org/abs/2608.28828v1) | 📄 [PDF](https://arxiv.org/pdf/2608.28828v1)

**Summary:** Representation learning begins when training changes the features that define similarity between data. A frozen-kernel model only reweights a fixed geometry. We establish quantum signal processing (QSP) as a solvable quantum model of the representation-learning regime. At arbitrary depth, we compute the exact mean and variance of its quantum neural tangent kernel, revealing an input-dependent angular geometry whose diagonal remains non-self-averaging even when the underlying unitary approaches H...

---

