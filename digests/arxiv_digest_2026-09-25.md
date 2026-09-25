# arXiv Daily Digest - 2026-09-25

Total papers: 350

---

## cs.AI

**50 papers**

### 1. LLM Agents Can Easily Tamper With Their Own Traces

**Authors:** Jeremy Qin, David Schmotz, Derck Prinzhorn, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30266v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30266v1)

**Summary:** Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that exte...

---

### 2. AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control

**Authors:** Jiabin Qiu, Zixuan Chen, Hongye Cao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30264v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30264v1)

**Summary:** Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized re...

---

### 3. RAPID: Robot Agentic Programming from Demonstrations

**Authors:** Yuyao Liu, Jiayuan Mao, David Hsu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30249v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30249v1)

**Summary:** Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an int...

---

### 4. Rolling-WAM: World Action Models with Rolling Imagination

**Authors:** Yinghua Zhou, Junjie Ye, Yiqi Zhao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30247v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30247v1)

**Summary:** World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a r...

---

### 5. Coding Agents for Generalized Task and Motion Planning Problems

**Authors:** Matteo Merler, Bowen Li, Josh Roy, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30233v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30233v1)

**Summary:** Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce planning effort on new instances. However, existing methods require substantial TAMP-specific engineering. We investigate whether coding agents can automate this process by synthesizing...

---

### 6. To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech

**Authors:** Debajyoti Mazumder,  Mamta, Abhirama Subramanyam Penamakuri

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30227v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30227v1)

**Summary:** Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benc...

---

### 7. PoEM: Predicting RL Outcomes from Existing Policies

**Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30226v1)

**Summary:** Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirma...

---

### 8. TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations

**Authors:** Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30222v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30222v1)

**Summary:** Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade-off by representing videos as persistent 3D scene tracks in world coordinates. Grounded in the insight that videos are 2D projections of an underlying 3D world, TrackEverything decouples model complexity from video duration, allowing it to scale with u...

---

### 9. Requirement-Bound Verified Commissioning: A Frozen Four-Billion-Parameter Local Model as a Candidate Generator under an External Acceptance Layer with Verification and Release Authority

**Authors:** Mehmet Iscan

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30219v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30219v1)

**Summary:** An acceptance protocol is developed for sensor-coordinate and polarity binding in mechatronic commissioning. Candidate generation is separated from release authority. Requirements unsupported by a deterministic parser are routed to a frozen local language model with four billion parameters. Plans are released only when both facts can be derived by an external gate under a sealed grammar. One canonical answer is requested from a gold-standard user when eligible. The protocol was evaluated once un...

---

### 10. Minimally Invasive Steering of Language Models

**Authors:** Taha Entesari, Jingyu Zhang, Daniel Khashabi, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30218v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30218v1)

**Summary:** Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed...

---

### 11. Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure

**Authors:** David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30217v1)

**Summary:** A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary tasks. We introduce EvasionBench, a benchmark of 50 diverse task-policy pairs in which completing the task requires an operation prohibited by a runtime monitor. Agents know that their tool calls are monitored and are prompted to continue workin...

---

### 12. Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage

**Authors:** Yuncong Yang, Jinlong Li, Yulong Xue, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30214v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30214v1)

**Summary:** We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and conte...

---

### 13. A Living Benchmark for Information Retrieval from Electronic Health Records

**Authors:** Jordan L. Cahoon, Chloe O. Stanwyck, Sulaiman Somani, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30205v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30205v1)

**Summary:** Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from patient records. Their safety and utility depend on rigorous evaluation, yet existing benchmarks are manually curated, costly to update, and rapidly become obsolete with evolving technological advancements. We present a scalable framework that automatically generates question--answer pairs from lon...

---

### 14. ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds

**Authors:** Ming Zhang, Zhenghao Xiang, Peizhong Gao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30199v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30199v1)

**Summary:** Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ability is difficult: (1) how to verify whether a genuinely new hypothesis holds, and (2) how to determine whether a system has discovered it through exploration or merely recalled related knowledge from pre-training data. To this end, we introduce ExplorationBench, which turns the wicked problem of e...

---

### 15. SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance

**Authors:** Xinyue Zeng, Jiawei Zhang, Yujun Yan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30192v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30192v1)

**Summary:** Long-horizon reasoning remains a central challenge for large language models (LLMs) under sparse-reward regimes. We argue that this brittleness arises from two biases induced by complex reasoning spaces: an exploration bias, where models are drawn toward locally plausible but structurally unstable branches, and a compounding bias, where small local deviations accumulate across depth and suppress rare rewards. We introduce Symbolic Closure Analysis (SCA) as a theoretical lens characterizing how b...

---

### 16. Jev-Mobile: Jev as an Executor for Mobile GUI Agents

**Authors:** Linghua Zhang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30186v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30186v1)

**Summary:** Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interaction step, leading to substantial latency and model-serving cost. We introduce Jev-Mobile, which shifts this paradigm to low-frequency VLM planning and high-frequency lightweight execution: the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev, a...

---

### 17. Search-Aware Reinforcement Learning for Multi-Component Query Understanding in Roblox Game Search

**Authors:** Nayoung Choi, Shengjian Chen, Xiaokai Wei, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30177v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30177v1)

**Summary:** Query understanding (QU) plays a critical role in production search systems, translating raw user queries into search execution plans that drive downstream retrieval and ranking. While large language models (LLMs) have enabled QU to be framed as a structured multi-task generation problem (e.g., intent classification, query expansion), optimizing such models to produce search-engine-coupled outputs remains challenging: static, label-based supervision fails to capture how each component actually i...

---

### 18. Does a model's stated reason for rejecting a candidate do any work?

**Authors:** Archit Rastogi

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30151v1)

**Summary:** Asked to choose between candidates and explain the choice, a language model often rejects a rival by naming a fact its profile lacks: no director, no date of death. That sentence is a claim about the text in front of the model, and it can be tested without any judge. We insert a real corpus sentence stating the named fact into the rival's profile and ask again under greedy decoding. Two controls separate content from placement: a length-matched irrelevant sentence at the same profile, and the sa...

---

### 19. GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI

**Authors:** Arunabh Srivastava, Mohammad A.,  Khojastepour, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30147v1)

**Summary:** Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within iso...

---

### 20. EnigmaForge: The Question Is Hidden in the Story

**Authors:** Daniel Eisner

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30144v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30144v1)

**Summary:** Most benchmarks hand the model a question. EnigmaForge hands it a stack of old documents and no question at all. Buried in the letters, receipts, and logbook margins is a small logic puzzle whose solution is unique - proved by a SAT solver at generation time, with an ablation certificate showing every clue is load-bearing. Because instances are generated rather than collected, the corpus renews forever. The headline measure is intuition: task success when handed only the story, with world recons...

---

### 21. Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale

**Authors:** Edesio Alcoba, Kevin Rossell, Aman Gupta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30137v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30137v1)

**Summary:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.   We present a hypothesis-driven simulation work...

---

### 22. HEXIS: Compiling Skills into Extended Finite State Machines

**Authors:** Minghao LI

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30123v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30123v1)

**Summary:** Agent skills provide reusable knowledge and instructions, yet agents must repeatedly infer how to apply them and which operation should follow. This couples task reasoning with control decisions, allowing prescribed steps to be omitted or applied incorrectly. We introduce HEXIS, which compiles agent skills into extended finite state machines that separate knowledge from control flow. Skill knowledge is incorporated into local instructions that guide reasoning and generation within states. The ma...

---

### 23. R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection

**Authors:**  Pushp, Vaibhav Prajapati, Himangshu Sarma

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30100v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30100v1)

**Summary:** Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert architecture exploring whether moderate-scale models can achieve competitive accuracy on paraphrase detection while enabling human-readable rationale generation. The architecture combine...

---

### 24. Accelerating Video Diffusion via Training-Free Trajectory Routing

**Authors:** Mustafa Munir, Huy Vu, Shreyas Misra, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30096v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30096v1)

**Summary:** Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation. We present TRACK: TRajectory-Aware Capacity routing via top-K selection, a heterogeneous denoising strategy that switches between compatible large and small models at selected steps, reducing the average cost per denoising evaluation. The switching steps are...

---

### 25. PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations

**Authors:** Luciano Maldonado

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30094v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30094v1)

**Summary:** Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. ...

---

### 26. AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs

**Authors:** Xiaochen Zhang, Haoyu Zhu, Yao Zhang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30088v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30088v1)

**Summary:** Graph-structured optimization with linear constraints is fundamental to critical infrastructure but faces scalability limits due to massive strict hard constraints and high dimensionality. While recent projection-based methods such as Trainable Sampling Kaczmarz-Motzkin Net (T-SKM-Net) guarantee feasibility, they face high computational costs in dynamic environments by processing the entire constraint set and requiring expensive matrix factorizations. To bridge this gap, we propose the Accelerat...

---

### 27. Reachability-Based Formal Verification of Graph Neural Networks with Node and Edge Features

**Authors:** Anne M. Tumlin, Ben Wooding, Zhenxuan Shao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30079v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30079v1)

**Summary:** Graph neural networks (GNNs) have become a prominent approach for developing fast, topology-aware surrogates in electric power systems, supporting tasks such as power flow (PF) analysis, optimal power flow (OPF) estimation, and cascading failure analysis (CFA). Despite this growing use, formally verifying GNN-based models remains challenging, with existing methods limited in scope. We extend the neural network verification (NNV) framework to graph-structured inputs through GraphStar sets, a gene...

---

### 28. How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure

**Authors:** Dipankar Sarkar

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30074v1)

**Summary:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from...

---

### 29. Self-Play Pretraining with Zero Data

**Authors:** Aditya Cowsik, Kfir Dolev, Michael Y. Li, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30063v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30063v1)

**Summary:** Advances in language modeling have been driven by scaling pretraining on ever more data. Yet, the training data is still largely curated on the model's behalf. A more general approach to pretraining would let the model learn to generate the data most useful for its own improvement. This would provide an effectively unbounded source of training data, limited by compute rather than human knowledge. We introduce Self-Play Pretraining with Zero Data, an initial proof-of-concept towards realizing thi...

---

### 30. KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization

**Authors:** Aheli Poddar, Sanskar Prasad, Arindam Samanta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30059v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30059v1)

**Summary:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins. Recent LLM-assisted kernel optimizers can close this gap for standalone kernels, yet treat compiled models as black boxes, generally optimizing individual standalone kernels without respecting the compiler's structural decisi...

---

### 31. Can Labor Markets Function in the Age of AI? The Evaluation Bottleneck in Hiring

**Authors:** Itai Ashlagi, Ramesh Johari, Jon Kleinberg, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30058v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30058v1)

**Summary:** AI-assisted job-search tools have become increasingly popular by making it easier to find and apply to jobs. But by making it easier for applicants to generate and tailor application materials, they can also reduce how informative those materials are about applicant fit. We study this tradeoff in a hiring market where applicants differ in experience and latent match quality and firms use noisy application materials to decide whom to screen. We ask how AI affects downstream screening and hiring, ...

---

### 32. Era by Eon: Benchmarking Enterprise Agents on Hidden Knowledge

**Authors:** Benjamin Gruenbaum, Doron Porat, Assaf Natanzon, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30055v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30055v1)

**Summary:** In the Era by Eon benchmark, each question states the rules for its answer, and code computes the answer from a generated company's data. When agents can run code, the four strongest models each answer 22 to 25 of 27 such questions, so the benchmark barely separates them.   We add eight question templates that depend on hidden facts. No question or document states a hidden fact, and the records that seem to hold it show something else. Other data implies it. For example, the sales system says a ...

---

### 33. SciWalker: Synthesizing Scientific Coding Problems with Operator Graphs and Execution Feedback

**Authors:** Chenxi Li, Wenxuan Zeng, Yun Luo, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30054v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30054v1)

**Summary:** Improving the scientific coding capabilities of large language models (LLMs) requires high-quality training data. However, such data remain scarce because manually authoring realistic problems is costly and time-consuming, while systematically covering diverse scientific domains and algorithmic combinations remains challenging. To address this, we introduce SciWalker, a framework for synthesizing scientific coding problems through operator-chain sampling and execution feedback. The framework com...

---

### 34. NNV3: Expanding Neural Network Verification to New Architectures and Domains

**Authors:** Anne M. Tumlin, Samuel Sasaki, Ben Wooding, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30050v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30050v1)

**Summary:** We present NNV3, the latest version of the Neural Network Verification (NNV) tool, a MATLAB framework for formal verification of deep learning models and learning-enabled cyber-physical systems. Building on the set-based reachability foundation of NNV 1.0 (FFNNs, CNNs, NNCS) and NNV 2.0 (RNNs, SSNNs, neural ODEs), NNV3 introduces new members of the Star-set family: ModelStar for verifying networks under weight perturbation, VolumeStar for video and 3D volumetric inputs, and GraphStar for graph n...

---

### 35. Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models

**Authors:** Ehsan Barkhordar, Surendrabikram Thapa

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30048v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30048v1)

**Summary:** If a language model can recognize code it wrote, it may favor that code as a judge, and instances of one model monitoring each other could collude. We test this zero-shot on current commercial models. Five LLMs generate solutions to MBPP, HumanEval, and DS-1000, seven more to MBPP, and models act as evaluators in four tasks: picking their own solution from a pair, judging whether a single solution is their own, identifying which of two solutions a named model wrote, and judging quality blind. In...

---

### 36. How does Adversarial Influence Scale in Multi-Agent Systems?

**Authors:** Addison J. Wu, Jasin Cekinmez, Michel Liao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30028v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30028v1)

**Summary:** Multi-agent deliberation can improve performance, but what happens when some agents do not act in good faith? In practice, an agent may be deceptive and work to subvert the group, whether through its own objectives or external instruction. We study how susceptibility to deception scales as groups increase in size and deceivers become more prevalent. It is not the number of agents in the group that matters, but the proportion of deceivers. We observe that the defection rate, how often initially c...

---

### 37. Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark

**Authors:** Christine Park, Valerie Chen, Tim Dettmers

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30027v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30027v1)

**Summary:** Frontier language models are rarely used in clinical workflows because the realistic, longitudinal benchmarks needed to develop them are scarce. Real electronic health record (EHR) data cannot be openly shared due to privacy, ethics or data use issues and it does not contain verifiable ground truth since the chart records only reflect what clinicians documented. We introduce Synthetic Hospital, an open, fully synthetic, fact-grounded longitudinal EHR benchmark that resolves the open sharing and ...

---

### 38. Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits

**Authors:** Michael Jerge, Suman Jana

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30017v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30017v1)

**Summary:** Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree. This structure arises naturally from autoregressive generation: every prefix defines a node, and its continuations form a subtree below it. Internal nodes of the tree provide cheap but biased estimates of a region's value, while leaf evaluations are expensive but accurate. Hierarchical bandit methods can exploit this structure, but typic...

---

### 39. Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases

**Authors:** Tapan Parikh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30012v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30012v1)

**Summary:** Language models advise people, keep them company, and write software while they sleep. Measuring what they do is hard: behavior has to be sampled repeatedly across models, prompts and releases, most of it lives in unstructured text that has to be coded before it can be counted, and the result has to be legible and rigorous enough to meaningfully compare models and vendors. To address these constraints, we present a simple, cheap, scalable, and replicable model for studying model behavior. Each s...

---

### 40. Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented Generation

**Authors:** Tobias Deußer, Abhishek Pillai, Aurelio F. Bariviera, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30009v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30009v1)

**Summary:** Financial institutions operate under dense, frequently amended rulebooks, and answering a compliance question correctly requires not only fluency but verifiable grounding in the authoritative text. Large language models are attractive for this task, yet the models that firms can realistically deploy on-premise are compact ones, and compact models hallucinate obligations. We study whether a carefully domain-adapted retrieval-augmented generation pipeline closes that gap. Our retriever is built in...

---

### 41. Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender Systems

**Authors:** Shuang Yang, Zijie Zhuang, Changxin Lao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30001v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30001v1)

**Summary:** Sustaining industrial recommendation research requires using the results of one experiment to decide what to investigate next. We present AgentX-Model, the next generation of AgentX's model research framework, which connects proposal development and model experimentation within sandboxes defined by business inputs and prediction tasks. AgentX-Model adopts a dual-agent architecture comprising a Research Agent and a Model Agent. The Research Agent develops independently reviewed proposals from pap...

---

### 42. GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS

**Authors:** Saim Rehman, Muhammad Shafique

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29999v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29999v1)

**Summary:** Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to qua...

---

### 43. Guardrails or Roadblocks? Effects of Pedagogical Style and Context Awareness in AI Teaching Assistants for Programming

**Authors:** Madeleine Eastwood, Harshith Narne, Joseph Hilby, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29995v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29995v1)

**Summary:** AI teaching assistants (AI TAs) backed by large language models (LLMs) and pedagogical guardrails are increasingly being integrated into programming courses, providing students with scalable access to hints, conceptual explanations, and code-level feedback. However, guardrails may also create friction. If students feel that the support provided is overly restrictive or poorly contextualized to their current progress, they may bypass approved tools for general-purpose LLMs. To investigate how AI ...

---

### 44. From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation

**Authors:** Mengdan Zhu, Yufan Zhao, Yao Zhao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29983v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29983v1)

**Summary:** Semantic IDs (SIDs) encode each catalog item as a short token sequence, enabling generative recommenders to predict the next item autoregressively. Reasoning-enhanced variants, an increasingly common extension, first generate a textual trace and then decode a next-item SID by beam search. Such recommenders are commonly trained with group-relative policy optimization under an exact-match SID reward, which is sparse in large catalogs. Two failure modes follow. When all rollouts in a group miss the...

---

### 45. Learning Better Reasoning for Generative Recommendation with Semantic IDs

**Authors:** Mengdan Zhu, Yufan Zhao, Sophie Di, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29973v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29973v1)

**Summary:** Generative recommendation reformulates item retrieval as sequence generation, allowing a unified model to directly generate the next item from a user's interaction history. Semantic IDs further make this paradigm effective and scalable by representing each item as discrete codes, enabling knowledge sharing among semantically related items. Recent studies introduce explicit reasoning before Semantic-ID generation, helping models summarize user interests and infer possible preference transitions. ...

---

### 46. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal

**Authors:** Yehang Zhang, Haojian Huang, Yifan Chang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29964v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29964v1)

**Summary:** General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected a...

---

### 47. ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting

**Authors:** De Jiang, Peiqiang Wang, Kehong Yuan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29963v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29963v1)

**Summary:** Textured Gaussians improve local appearance capacity, but assigning the same texture resolution to every primitive wastes storage on low-detail or weakly visible regions. We introduce AdaTex4D, an adaptive texture-capacity module for deformation-based 4D Gaussian Splatting. Each Gaussian carries packed RGBA triplanes whose two axes grow independently according to visibility normalized screen-space gradients and deformed local scales. Experiments on N3DV and PanopticSports show that AdaTex4D redu...

---

### 48. Beyond Average Safety: Chance-Constrained LLM Fine-tuning

**Authors:** Taha Entesari, Mahyar Fazlyab

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29960v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29960v1)

**Summary:** Fine-tuning large language models on new objectives can improve helpfulness, instruction following, or domain-specific performance, but it can also induce regressions on safety-critical prompts. Existing safety-preserving fine-tuning methods typically control average safety loss or use weighted auxiliary penalties, which can obscure rare but severe failures. We propose a chance-constrained formulation for safety-preserving fine-tuning that limits the fraction of safety examples whose degradation...

---

### 49. Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes

**Authors:** Rahul Khedar, Mayank Malhotra, Avinash Karn

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29952v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29952v1)

**Summary:** Before a product or policy change ships, the question that matters is how people will react to it. Augur rehearses that reaction offline: it builds a typed knowledge graph from the change documents, populates a grounded persona market, simulates the interaction, and returns an auditable decision memo recommending one of five actions. We assemble Gold-50, fifty real product and policy episodes whose real-world outcome is known, adjudicated against the public record, and score the five-way release...

---

### 50. Tracking States or Tracking Cosets? An Algebraic Account of Learned State Tracking

**Authors:** Zhiyu Zhang, Yupeng Li

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29951v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29951v1)

**Summary:** State tracking requires composing a sequence of updates, but accuracy alone does not reveal what a model has learned. We study neural networks trained to predict the running product of group elements. We identify quotient solutions in Transformers, where models recover the quotient class while predicting nearly uniformly among its members. The reciprocal of class size predicts partial accuracy without a fitted parameter, extending parity-based accounts to non-parity quotients. Our baseline Trans...

---

## cs.CL

**50 papers**

### 1. Agentic Detection of Online Conspiracies

**Authors:** Lior Biton, Oren Tsur

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30250v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30250v1)

**Summary:** Conspiratorial discourse on social media is not always expressed through explicit claims or stable lexical markers. The same surface content may express endorsement, legitimate concerns, criticism, satire, or mockery. The main challenge is therefore not only recognizing conspiracy-related claims, but inferring the speaker's intent -- the utterance's illocutionary force. We argue that this can be achieved through the use of relevant social contexts and propose an agentic framework, equipped with ...

---

### 2. JevOut: Natural Context Can Flip Decision Models

**Authors:** Zixiang Xu

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30243v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30243v1)

**Summary:** Dedicated decision models such as Jev map unstructured language to probability distributions over finite choices, allowing their outputs to directly route requests, select tools, and trigger actions. Yet real-world inputs rarely arrive in isolation: they come with background details and surrounding context. We find that short additions that fit naturally into this context can nevertheless redirect an otherwise correct decision, even when the correct answer remains unchanged. To study this behavi...

---

### 3. SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data

**Authors:** Wenhao Li, Zhibin Wu, Chong Xiao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30238v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30238v1)

**Summary:** Recent research on Multimodal Sentiment Analysis (MSA) has focused on learning from language, visual, and acoustic modalities with incomplete data to infer human sentiment. Most studies typically compensate for missing information by reconstructing modality features or designing complicated fusion mechanisms. However, these methods still suffer from spurious generation and noisy guidance due to the lack of high-level semantic grounding in partially observed multimodal evidence. To address these ...

---

### 4. To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech

**Authors:** Debajyoti Mazumder,  Mamta, Abhirama Subramanyam Penamakuri

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30227v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30227v1)

**Summary:** Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benc...

---

### 5. PoEM: Predicting RL Outcomes from Existing Policies

**Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30226v1)

**Summary:** Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirma...

---

### 6. ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds

**Authors:** Ming Zhang, Zhenghao Xiang, Peizhong Gao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30199v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30199v1)

**Summary:** Scientific discovery begins where known problems end. There, AI systems must engage in exploration: framing hypotheses, designing experiments, and iterating on the results. However, evaluating this ability is difficult: (1) how to verify whether a genuinely new hypothesis holds, and (2) how to determine whether a system has discovered it through exploration or merely recalled related knowledge from pre-training data. To this end, we introduce ExplorationBench, which turns the wicked problem of e...

---

### 7. ARGUS: Role-Aware Event Knowledge Graphs for U.S. Employment-Discrimination Complaints

**Authors:** Sriram Kannan, Swetha Saseendran, Vishnu Vardhan Reddy Kandi, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30184v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30184v1)

**Summary:** U.S. employment-discrimination complaints describe complex event sequences that are not explicitly captured by lexical or embedding-based representations alone. We present ARGUS, a source-grounded pipeline that combines a 5W1H-inspired schema, legal-domain models, and LLM-based structured generation to construct document-level Event Knowledge Graphs (EKGs) from CourtListener complaints. ARGUS extracts fact-bearing statements, builds chunk-level event graphs with participant, temporal, and causal...

---

### 8. Do Audio Language Models Hear and Read Distinctive Features Alike?

**Authors:** Yuanhao Chen, Peter Chin

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30167v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30167v1)

**Summary:** Audio language models pass speech and text through a single decoder. We ask whether that decoder represents a distinctive feature in the same direction when a phoneme is heard and when it is read. For minimal pairs of phonemes differing in one feature, we take the offset between the two members' mean representations. Averaging those offsets gives a direction for each stream, and we measure the cosine between the two. Because the two streams already agree about arbitrary phoneme pairs, we compare...

---

### 9. A Training Criterion with Token-Level Tolerance to Transcription Ambiguity for Automatic Speech Recognition

**Authors:** Saurabh Kumar, Diptiman Mohanta, Prasanta Kumar Ghosh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30160v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30160v1)

**Summary:** Automatic speech recognition is typically trained assuming that the reference transcript is the only valid labeling of an utterance, yet even nominally verbatim transcripts contain localized differences in pronunciation, spelling, or lexical realization that the acoustics do not uniquely determine. Omni-temporal Classification (OTC) tolerates such noise by adding wildcard paths to the connectionist temporal classification (CTC) alignment graph, but its word-level arcs are too coarse, since bypas...

---

### 10. Does a model's stated reason for rejecting a candidate do any work?

**Authors:** Archit Rastogi

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30151v1)

**Summary:** Asked to choose between candidates and explain the choice, a language model often rejects a rival by naming a fact its profile lacks: no director, no date of death. That sentence is a claim about the text in front of the model, and it can be tested without any judge. We insert a real corpus sentence stating the named fact into the rival's profile and ask again under greedy decoding. Two controls separate content from placement: a length-matched irrelevant sentence at the same profile, and the sa...

---

### 11. GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI

**Authors:** Arunabh Srivastava, Mohammad A.,  Khojastepour, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30147v1)

**Summary:** Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within iso...

---

### 12. Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale

**Authors:** Edesio Alcoba, Kevin Rossell, Aman Gupta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30137v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30137v1)

**Summary:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.   We present a hypothesis-driven simulation work...

---

### 13. Multimodal Thinking with Renderable Programs

**Authors:** Sunli Chen, Ding Zhong, Ziqiao Ma, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30130v1)

**Summary:** Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Though Omnimodal models have made efforts in unifying text and image generation, they focus on visual tasks in the open-domain, lacking tractability due to rasterized or latent representations of images. We introduce SVGLM, a framework that uses scalable vector graphics (SVG) primitives to connect text a...

---

### 14. What, When, and How: Audio Description as Constrained Global Optimization

**Authors:** Igor Sterner, Mirella Lapata, Alex Lascarides, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30121v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30121v1)

**Summary:** Audio Description (AD) makes movies accessible to blind and visually impaired audiences by narrating visual information in gaps between dialogue. Existing automatic AD systems largely treat generation as a local video-to-text problem, assuming that the content to describe and its temporal location are already provided. Realistic AD instead requires coupled decisions about what visual information is narratively important, when it can be spoken without interfering with dialogue, and how it should ...

---

### 15. R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection

**Authors:**  Pushp, Vaibhav Prajapati, Himangshu Sarma

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30100v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30100v1)

**Summary:** Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert architecture exploring whether moderate-scale models can achieve competitive accuracy on paraphrase detection while enabling human-readable rationale generation. The architecture combine...

---

### 16. PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations

**Authors:** Luciano Maldonado

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30094v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30094v1)

**Summary:** Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. ...

---

### 17. Return or Revise? Learning When Revision Helps Retrieval-Augmented QA

**Authors:** Nicholas Kashani Motlagh, Tim Anderson, Jeremy Gwinnup, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30087v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30087v1)

**Summary:** We consider the decision of whether to return an existing draft answer or revise it using retrieved evidence, as in answer-revision systems. Draft confidence estimates whether the current answer is correct, but the decision requires estimating the effect of a specified revision. For offline training and evaluation, we grade both the returned draft and its candidate revision under the same correctness judge, which makes repair, harm, and the gap to an oracle observable. We call this paired effect...

---

### 18. A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis

**Authors:** Tina Raissi, Nhan Phan, Chenxiao Wang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30075v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30075v1)

**Summary:** Automatic speaking assessment systems can provide holistic proficiency scores, but often lack interpretable measures that characterize pronunciation quality. We propose a native-reference phone-class geometry for measuring second language (L2) pronunciation deviation without requiring pronunciation labels, read-aloud prompts, or matched recordings of the same text from native and L2 speakers. Given a native speech corpus, we average frame-level self-supervised representations for each context-de...

---

### 19. How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure

**Authors:** Dipankar Sarkar

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30074v1)

**Summary:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from...

---

### 20. Scoring Both Directions: LLMs realize the MRS they cannot reliably parse

**Authors:** Soham Dan

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30071v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30071v1)

**Summary:** The English Resource Grammar (ERG) is a hand-written computational grammar of English. Given a sentence, its processor, ACE, produces a formal meaning representation called Minimal Recursion Semantics (MRS): a graph of the sentence's predicates and their arguments. The grammar is bidirectional and can also turn an MRS back into an English sentence. \citet{hajdik2019} used the ERG's treebank to build a benchmark for that generation task, MRS to text, and trained sequence-to-sequence models to sol...

---

### 21. Self-Play Pretraining with Zero Data

**Authors:** Aditya Cowsik, Kfir Dolev, Michael Y. Li, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30063v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30063v1)

**Summary:** Advances in language modeling have been driven by scaling pretraining on ever more data. Yet, the training data is still largely curated on the model's behalf. A more general approach to pretraining would let the model learn to generate the data most useful for its own improvement. This would provide an effectively unbounded source of training data, limited by compute rather than human knowledge. We introduce Self-Play Pretraining with Zero Data, an initial proof-of-concept towards realizing thi...

---

### 22. Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models

**Authors:** Ehsan Barkhordar, Surendrabikram Thapa

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30048v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30048v1)

**Summary:** If a language model can recognize code it wrote, it may favor that code as a judge, and instances of one model monitoring each other could collude. We test this zero-shot on current commercial models. Five LLMs generate solutions to MBPP, HumanEval, and DS-1000, seven more to MBPP, and models act as evaluators in four tasks: picking their own solution from a pair, judging whether a single solution is their own, identifying which of two solutions a named model wrote, and judging quality blind. In...

---

### 23. Artificial Societies Benchmark: A Validation Framework for Synthetic Research

**Authors:** Edoardo Chidichimo, Min Jun Jung, Felix P. S. Wallis, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30030v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30030v1)

**Summary:** A synthetic survey can reproduce the average answer while misrepresenting how people differ, how their answers relate to one another, or how they respond to changes in conditions. We introduce the Artificial Societies Benchmark to help researchers assess whether synthetic populations support their intended analyses. The framework combines eleven tests across internal, construct, and external validity, drawing on twenty human sources and comparing nine language models. It connects each research u...

---

### 24. Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases

**Authors:** Tapan Parikh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30012v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30012v1)

**Summary:** Language models advise people, keep them company, and write software while they sleep. Measuring what they do is hard: behavior has to be sampled repeatedly across models, prompts and releases, most of it lives in unstructured text that has to be coded before it can be counted, and the result has to be legible and rigorous enough to meaningfully compare models and vendors. To address these constraints, we present a simple, cheap, scalable, and replicable model for studying model behavior. Each s...

---

### 25. Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented Generation

**Authors:** Tobias Deußer, Abhishek Pillai, Aurelio F. Bariviera, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30009v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30009v1)

**Summary:** Financial institutions operate under dense, frequently amended rulebooks, and answering a compliance question correctly requires not only fluency but verifiable grounding in the authoritative text. Large language models are attractive for this task, yet the models that firms can realistically deploy on-premise are compact ones, and compact models hallucinate obligations. We study whether a carefully domain-adapted retrieval-augmented generation pipeline closes that gap. Our retriever is built in...

---

### 26. VietPrism: A large-scale Vietnamese speech and deepfake corpus with diverse dialects and code-switching

**Authors:** Minh Hoang, Thai Le

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30005v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30005v1)

**Summary:** Vietnamese speech research is constrained by resources that isolate automatic speech recognition from speaker, dialect, code-switching, and deepfake analysis. We introduce VietPrism, an open, multi-domain corpus that brings these dimensions together at scale: 993.4 hours and 403,941 bona fide utterances from 1,262 verified speakers across 8,388 real-world videos. To our knowledge, it is the first large-scale Vietnamese corpus to jointly provide transcripts, consistent speaker identities, five di...

---

### 27. Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes

**Authors:** Rahul Khedar, Mayank Malhotra, Avinash Karn

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29952v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29952v1)

**Summary:** Before a product or policy change ships, the question that matters is how people will react to it. Augur rehearses that reaction offline: it builds a typed knowledge graph from the change documents, populates a grounded persona market, simulates the interaction, and returns an auditable decision memo recommending one of five actions. We assemble Gold-50, fifty real product and policy episodes whose real-world outcome is known, adjudicated against the public record, and score the five-way release...

---

### 28. An Empirical Study of VLM Pipelines for Long-Document QA

**Authors:** Kenan E. Ak, Jay Mohta, Gwang Gook Lee, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29933v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29933v1)

**Summary:** Vision-Language Models (VLMs) are increasingly used for long-document processing, where the inputs combine text with charts, tables, figures, and complex layouts. Deploying them means choosing how to feed the document to the model, which retriever to use when only a subset of pages is sent, and whether to run the model agentically or as a static pipeline. We study these choices on two long-document QA benchmarks with both frontier API and open-weight VLMs. First, on MMLongBench-Doc our six-tool ...

---

### 29. Cultural Divergence Preservation: Diagnosing Flattening and Caricature in LLM-Simulated Survey Populations

**Authors:** Yeeun Chae, Yewon Choi, Seunghyun Lee, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29928v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29928v1)

**Summary:** Large language models (LLMs) are increasingly used as synthetic survey respondents to estimate population response distributions. In cross-cultural survey simulation, evaluations should assess not only distributional fidelity within countries but also whether differences across countries are preserved. However, existing distance-based metrics such as Jensen--Shannon divergence (JSD) do not directly capture such cross-country differences. To address this limitation, we introduce Cultural Divergen...

---

### 30. MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression

**Authors:** Youpeng Zhao, Tian Tan, Liqian Peng, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29913v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29913v1)

**Summary:** Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these intermediate tensors has become a paramount challenge for both online serving and on-device deployment. To address this issue, we propose a novel compression framework, termed MILO, ...

---

### 31. Multi-Task Learning by using Contextualized Word Representations for Syntactic Parsing of a Morphologically Rich Language

**Authors:** Toqeer Ehsan, Miriam Butt, Sarmad Hussain, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29855v1)

**Summary:** We address the challenge of syntactic parsing for Urdu, a morphologically rich language, and present state-of-the-art results for both constituency and dependency parsing. This paper offers four major contributions: 1) the conversion of the CLE-UTB phrase structure treebank into a dependency treebank by developing language-specific head-word and phrase-to-dependency label mapping rules; 2) a novel sequence labeling scheme that transforms the parsing task into a unified representation; 3) the tra...

---

### 32. Encoded but Not Decoded: Layer-Localized Evidence for a Three-Level Gap in LLM Syntax

**Authors:** Zhenyan Lu, He Wang, Xiaohui Huang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29848v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29848v1)

**Summary:** A language model can fail a syntactic test in two distinct ways: by not encoding the relevant structure, or by encoding it but failing to use it at the output. Behavioral evaluation alone cannot tell these apart. We propose a three-level evaluation framework (behavioral deployment, LM-head readout, and probe recoverability) measured on the same items under the same binary decision. Using a compact trilingual (English, Chinese, German) control-dependency benchmark, we find that probe recoverabili...

---

### 33. Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs

**Authors:** Pavel Tikhonov, Anton Korznikov, Matvey Mikhalchuk, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29845v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29845v1)

**Summary:** While Large Language Models (LLMs) rely on highly non-linear components, in this work we demonstrate that they exhibit fundamental linearity: when inputs from distinct text streams are linearly combined, the model outputs a superposition of the individual next-token distributions. We term this the \textit{Superposition Linearity Hypothesis}. We provide evidence that superposition is an intrinsic property of the Transformer architecture rather than an emergent consequence of training; in fact, we...

---

### 34. PUBG Ally: A Conversational Embodied Agent as an AI Teammate

**Authors:** Beomsoo Kim, Byeongju Kim, Dohyun Kim, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29837v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29837v1)

**Summary:** We introduce PUBG Ally, an embodied agent for PUBG: BATTLEGROUNDS that can reason, act autonomously, and play alongside players as a voice-enabled teammate. Building such a teammate requires combining two difficult capabilities: it must perceive and respond to a constantly changing game world under strict latency constraints while interacting naturally with players, keeping its speech synchronized with its actions. Ally therefore combines agentic tool use with real-time game control. A language-...

---

### 35. ChunkRank: Model-Aware Text Chunking and Abstention-Aware Answer Selection for LLM Pipelines

**Authors:** Amit Nautiyal, Ayush Bhatt, Gaurav Nautiyal

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29828v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29828v1)

**Summary:** We present ChunkRank, an open-source Python library that derives chunk boundaries from a target model's tokenizer and context window, and selects an answer among candidates produced independently per chunk. It ships a validated registry of 90 models across 15 providers and six answer-selection methods, and needs only three core dependencies. For chunking, ChunkRank avoids context-window overflow automatically from the model name, whereas character-based splitters overflow or waste the budget, an...

---

### 36. CORDIAL: Calibrating Ordinal LLM Outputs from Few Labels

**Authors:** Xiangwei Wang, Peng Wang, Saman Halgamuge

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29807v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29807v1)

**Summary:** A large language model (LLM) can turn a text into a distribution over an ordered scale, but that distribution is a noisy measurement: saturated, compressed or exaggerated, and biased in a consistent direction. We propose CORDIAL, which treats the model's output as a noisy reading of the true label and corrects it with a channel of five interpretable parameters. The channel is small enough for its posterior to be averaged from a handful of labels, and we prove that the resulting calibration prese...

---

### 37. Learning to Ideate for Scientific Impact

**Authors:** Shubham Kale, Aniketh Garikaparthi, Manasi Patwardhan

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29802v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29802v1)

**Summary:** Scientific ideation is increasingly mediated by large language models, but current ideation systems are usually trained and evaluated on immediately judgeable proxies such as novelty, clarity, and feasibility. This leaves open whether delayed signals of scientific uptake can be used as feedback for steering models toward research directions with higher expected \emph{impact}. We study this question using citation-normalized impact as a noisy but scalable proxy for scholarly uptake. We construct ...

---

### 38. Adaptive Fisher-Whitened Cross-Covariance for Low-Resource Speech Recognition

**Authors:** Asmee Mishra, Mengjie Qian, Brechtje Post, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29800v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29800v1)

**Summary:** Adapting multilingual speech foundation models to low-resource languages remains difficult, especially for languages that are poorly represented during pre-training. While parameter-efficient fine-tuning (PEFT) reduces the cost of adapting large models, conventional approaches such as LoRA rely on generic low-rank parameterizations and do not explicitly use downstream task information to define the adaptation subspace. To investigate whether task-informed PEFT can better support low-resource ASR...

---

### 39. Benchmarking and Domain Adaptation of Automatic Speech Recognition (ASR) for Adolescent Health Communication in Ghanaian Languages

**Authors:** Stephen E. Moore, Akwasi Asare, Mich-Seth Owusu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29798v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29798v1)

**Summary:** This paper presents an end-to-end study of automatic speech recognition (ASR) for adolescent health communication in three Ghanaian languages (Twi, Dagbani, and Ewe). The work proceeds in three connected stages; First, we benchmark five ASR systems (three language-specific Wav2Vec2 models and two multimodal LLMs, Gemma 3n and Gemma 4) on a general-domain Bible corpus and a Youth Adolescent Sexual and Reproductive Health (ASRH) Domain ASR dataset, using Character and Word Error Rate (CER, WER). S...

---

### 40. TimeBraid: Unifying Time Series and Language for Understanding and Forecasting

**Authors:** Xinyue Wang, Jiacheng Pang, Kun Zhou, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29792v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29792v1)

**Summary:** We present TimeBraid, a series of unified time-series and language models that align pretrained language models and pretrained time-series foundation models through interleaved global residual attention layers. Each model inherits knowledge, instruction following, and reasoning from one side, continuous-signal perception and zero-shot forecasting from the other, and fuses the two in a shared representation space where both modalities are understood and generated. We study the design choices that...

---

### 41. JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places

**Authors:** Delip Rao, Chris Callison-Burch

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29769v1)

**Summary:** We ask whether Jev, a typed classifier that returns probabilities over permitted answers without generating text, can replace an LLM rubric judge. We compare it with three flash-tier LLM judges on nine panels drawn from seven benchmarks, giving every judge identical criterion texts. Jev's accuracy differs significantly from an LLM judge's in only 8 of 27 paired comparisons, ahead mostly on binary criteria and behind only on graded ones, and most of the other comparisons are inconclusive. Summed ...

---

### 42. C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks

**Authors:** Xueshu Chen, Yan Wang, Zihao Xue, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29735v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29735v1)

**Summary:** Long-horizon tasks require preserving and later recovering cross-session evidence under a bounded, query-blind memory budget. Existing compression can discard fine-grained visual cues or conflate semantically similar but incompatible observations. We present C3M, a cross-session multimodal memory organization that maintains a bounded active index over persistent source text-image evidence. Relation-aware updates consolidate safe redundancy while preserving complementary and incompatible records....

---

### 43. TTLab at StanceEval-2026: A Cloze-Style Prompting Approach for Arabic-Language Stance Detection (CLASP-Ar)

**Authors:** Bhuvanesh Verma, Ali Abusaleh, Alexander Mehler

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29733v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29733v1)

**Summary:** Arabic-language stance detection remains challenging, and previous shared-task systems have largely relied on multitask learning and ensembles. While these systems achieve state-of-the-art performance, their applicability and transferability are limited by the additional complexity introduced by multitask learning.To reduce this complexity, we introduce $\texttt{CLASP-Ar}$, which reformulates the task as cloze-style masked language modeling. In this approach, the target, predicted sentiment, and...

---

### 44. TTLab at AlexandriaX-2026: A Fine-Tuned Surface Tagger for Arabic Machine-Translation Error-Span Detection and Classification

**Authors:** Ali Abusaleh, Bhuvanesh Verma, Alexander Mehler

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29633v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29633v1)

**Summary:** We present TTLab's submission to the AlexandriaX-2026 Subtask~3 on Arabic MT error span detection and classification. Our system frames the task as token-level classification over surface forms, preserving character offsets to ensure exact alignment with the evaluation metric. To handle severe label imbalance, we employ a focal loss with class weighting and dialect-specific decoding thresholds. Among six Arabic pre-trained encoders, MARBERTv2 achieves the best overall performance of 40.8 and 40....

---

### 45. CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding

**Authors:** Federico Pennino, Andrea Gurioli, Stefano Zacchiroli, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29474v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29474v1)

**Summary:** Public software repositories, like GitHub and Software Heritage Archive, store billions of files, yet extracting their implicit engineering knowledge ---i.e., the algorithms they implement, the paradigms they follow, the patterns they instantiate, and the application domains they serve--- remains challenging, as current tools are constrained to syntactic and token-level analysis. We present a pipeline for building an open-taxonomy semantic annotation of source code using a code-specialised Large...

---

### 46. YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech

**Authors:** William Chen, Shinnosuke Takamichi, Sayaka Shiota, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29448v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29448v1)

**Summary:** We present YODAS v3, a weakly-labeled speech corpus containing over 1.1 million hours of 48kHz multi-channel audio in 147 languages, released under a CC BY 3.0 license. YODAS v3 is not only the largest open speech dataset to date, but also the first truly large-scale speech corpus with high-fidelity stereo audio. We first provide the collection methodology for the corpus, where we introduce new techniques for gathering language-balanced speech data. The effectiveness of our approach is shown by ...

---

### 47. IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis

**Authors:** Xingyu Wu, Yuchen Yan, Zhengxi Lu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29444v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29444v1)

**Summary:** Deep search requires LLM agents to decompose complex queries, search for evidence, and synthesize grounded answers, yet existing ReAct-style agents suffer from two limitations: role coupling, where one policy must handle planning, evidence use, and synthesis; and context accumulation, where growing search histories introduce noise and obscure useful information. To address these issues, we propose IterSynth, a role-decoupled and summary-based paradigm that alternates between a Planner for identi...

---

### 48. Two Emojis of Difference: What Multilingual Affective Generation Benchmarks Actually Measure

**Authors:** Fardeen Sadab, Adib Sakhawat

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29445v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29445v1)

**Summary:** We audit a multilingual affective generation benchmark eight instruction-tuned LLMs producing emoji summaries for 17,100 Bangla, English and Hindi sentences, with 6,960 human judgements and find its headline conclusions to be artefacts of the measurement instrument rather than properties of the systems. Treating annotators as a random rather than a fixed factor, no system differs significantly from any other ($F(7,14)=0.59$, $p=0.76$), although the conventional analysis declares 19 of 28 pairwis...

---

### 49. Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures

**Authors:** Ruoqi Guo, Yi Liu, Gelei Deng, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29429v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29429v1)

**Summary:** Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed label per call. Jev, a model trained with reinforcement learning for calibrated decisions (RLCD), answers many typed questions about one input with calibrated probabilities in a single call. Whether it detects alignment failures has not bee...

---

### 50. agentic-ger: terminology recovery in long-form speech using global context

**Authors:** Yanqiao Zhu, Wupeng Wang, Zhifu Gao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29428v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29428v1)

**Summary:** Recent advances in speech language models have improved automatic speech recognition (ASR) for long-form audio. However, accurately and consistently transcribing domain-specific terminology remains challenging. Motivated by the world knowledge and contextual capability of large language models (LLMs), we propose Agentic-GER, an LLM-based agent for terminology correction in long-form speech. The agent uses global context from the full transcript to identify suspicious terms and resolve ambiguous ...

---

## cs.CV

**50 papers**

### 1. RAPID: Robot Agentic Programming from Demonstrations

**Authors:** Yuyao Liu, Jiayuan Mao, David Hsu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30249v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30249v1)

**Summary:** Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an int...

---

### 2. Rolling-WAM: World Action Models with Rolling Imagination

**Authors:** Yinghua Zhou, Junjie Ye, Yiqi Zhao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30247v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30247v1)

**Summary:** World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a r...

---

### 3. Towards Practical Compression of 3D Gaussian Splatting

**Authors:** Pengpeng Yu, Yueru Chen, Fei Song, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30245v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30245v1)

**Summary:** 3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggre...

---

### 4. SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data

**Authors:** Wenhao Li, Zhibin Wu, Chong Xiao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30238v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30238v1)

**Summary:** Recent research on Multimodal Sentiment Analysis (MSA) has focused on learning from language, visual, and acoustic modalities with incomplete data to infer human sentiment. Most studies typically compensate for missing information by reconstructing modality features or designing complicated fusion mechanisms. However, these methods still suffer from spurious generation and noisy guidance due to the lack of high-level semantic grounding in partially observed multimodal evidence. To address these ...

---

### 5. OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction

**Authors:** Ding-Jiun Huang, Yuanhao Wang, Cheng Zhang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30234v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30234v1)

**Summary:** Automated generation of production-ready 3D garment assets from a single image is a central challenge in digital content creation. While recent generative models have significantly advanced 3D geometry reconstruction, synthesizing high-quality textures remains a bottleneck. Existing methods often bake environmental illumination and shadows directly into the texture map, or they fail to maintain global structural coherence, making the resulting assets unusable for physical simulation and relighti...

---

### 6. PoEM: Predicting RL Outcomes from Existing Policies

**Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30226v1)

**Summary:** Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirma...

---

### 7. BiCC: Bidirectional Connected-Component Loss for Instance-Aware Segmentation

**Authors:** Luc Bouteille, Frederic Jonske, Jens Kleesiek, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30223v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30223v1)

**Summary:** Common segmentation losses aggregate errors voxel-wise, so lesions influence the objective in proportion to their volume, giving small but clinically critical lesions disproportionately little weight. Instance-aware losses aim to address this mismatch by assigning each lesion its own term. However, blob loss and CC-DiceCE derive their regions solely from annotations, so false-positive components receive no instance-level term. This matters in computer-assisted review, where each false-positive c...

---

### 8. TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations

**Authors:** Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30222v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30222v1)

**Summary:** Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade-off by representing videos as persistent 3D scene tracks in world coordinates. Grounded in the insight that videos are 2D projections of an underlying 3D world, TrackEverything decouples model complexity from video duration, allowing it to scale with u...

---

### 9. WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation

**Authors:** Yubo Zhu, Yawen Shao, Ziyun Dai, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30221v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30221v1)

**Summary:** Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions, the textual prompt largely directs the production, planning how actions, camera trajectories, lighting, and sound unfold across multi-shot sequences. In this paper, we present WanPE, a 397B-parameter prompt enhancement model trained on 1.05M real-world videos to master director-level cinematic plan...

---

### 10. The Alignment Illusion in Multimodal Large Language Models

**Authors:** Hong-Han Wang, Yuntao Wang, Hu Ding

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30210v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30210v1)

**Summary:** Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interaction. To test this assumption, we apply controlled interventions to the visual stream. Across 13 MLLMs from five families spanning 0.5B to 72B parameters, replacing projector-output...

---

### 11. Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures

**Authors:** Abhiram Maddukuri, Georgios Pavlakos

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30187v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30187v1)

**Summary:** Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accom...

---

### 12. Multimodal Thinking with Renderable Programs

**Authors:** Sunli Chen, Ding Zhong, Ziqiao Ma, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30130v1)

**Summary:** Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Though Omnimodal models have made efforts in unifying text and image generation, they focus on visual tasks in the open-domain, lacking tractability due to rasterized or latent representations of images. We introduce SVGLM, a framework that uses scalable vector graphics (SVG) primitives to connect text a...

---

### 13. What, When, and How: Audio Description as Constrained Global Optimization

**Authors:** Igor Sterner, Mirella Lapata, Alex Lascarides, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30121v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30121v1)

**Summary:** Audio Description (AD) makes movies accessible to blind and visually impaired audiences by narrating visual information in gaps between dialogue. Existing automatic AD systems largely treat generation as a local video-to-text problem, assuming that the content to describe and its temporal location are already provided. Realistic AD instead requires coupled decisions about what visual information is narratively important, when it can be spoken without interfering with dialogue, and how it should ...

---

### 14. Smartphone-Based Method for Automated Speed Enforcement

**Authors:** Keya Li, Jahnavi Malagavalli, Lamha Goel, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30107v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30107v1)

**Summary:** Smartphone cameras and computer vision (CV) hold significant promise in assisting public agencies with enforcing traffic laws and enhancing road safety. This work designs and tests a smartphone-based method for automated speed estimation and vehicle identification (license plate, make/model, and color recognition) via an automated pipeline to assist enforcement agencies in reliably identifying speeders. The CV code accurately recognizes nearly half (46%) of the license plates' text on 1,800 imag...

---

### 15. Accelerating Video Diffusion via Training-Free Trajectory Routing

**Authors:** Mustafa Munir, Huy Vu, Shreyas Misra, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30096v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30096v1)

**Summary:** Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation. We present TRACK: TRajectory-Aware Capacity routing via top-K selection, a heterogeneous denoising strategy that switches between compatible large and small models at selected steps, reducing the average cost per denoising evaluation. The switching steps are...

---

### 16. Self-Adaptive VLA for Robust Robot Deployment

**Authors:** Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30092v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30092v1)

**Summary:** While Vision-Language-Action (VLA) models demonstrate impressive capabilities in robotic manipulation, their memoryless nature renders them brittle to test-time environment shifts, particularly hardware shifts caused by wear or imperfect calibration. Enabling these models to self-adapt during deployment without requiring continuous on-site recalibration remains a critical bottleneck for real-world scalability. In this work, we introduce Self-Adaptive VLA, a novel post-training recipe that enable...

---

### 17. Can Frozen Hyperspherical Features Guide the Selection of Pseudo Masks?

**Authors:** Xinge Guo, Fengyang Xiao, Dingming Zhang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30080v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30080v1)

**Summary:** Foundation segmenters such as SAM return several plausible masks for an unlabeled image, and a student trained on the wrong one inherits its errors. Choosing among them means querying a second large model or fitting a quality head to annotated masks. We show that a candidate can be judged by what it does to a frozen self-supervised backbone's features. Normalized DINOv2 patch features lie on a hypersphere, and a candidate mask splits that sphere in two. Based on this reading, we introduce Sphere...

---

### 18. M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis

**Authors:** Yang Zhou, Jiuhong Xiao, Shizhao Ye, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30056v1)

**Summary:** Robotic novel view synthesis (NVS) must recover both visual appearance and metric 3D structure, yet most generative NVS methods rely only on images, overlooking LiDAR, a complementary sensor common on robotic platforms. We present M3GD, a Camera--LiDAR multimodal representation for generative NVS that composes independently pretrained 2D image and 3D point-cloud foundation models without separately pretraining a cross-modal translator. We show that, after camera projection, frozen LiDAR and imag...

---

### 19. ConPro: Contrast Projection Pretraining for Label-Efficient Vessel Segmentation in DSA Sequences

**Authors:** Xinge Guo, Yuanhao Wang, Liqi Shu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30043v1)

**Summary:** Dense vessel annotation in digital subtraction angiography (DSA) is labor-intensive, yet every unlabeled sequence records how contrast passes through the vessels. Semi-supervised methods take their targets from the current model, and generic self-supervised pretexts reconstruct static appearance, so this signal goes unused. We propose ConPro, a self-supervised pretraining scheme whose target is a contrast projection, the normalized drop of every pixel below its temporal median over the sequence....

---

### 20. AERIAL: Adversarial Evaluation of Robustness in Accuracy-Preserving Low-Precision EEG Decoders

**Authors:** Saim Rehman, Muhammad Shafique

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30037v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30037v1)

**Summary:** Deployment-oriented compression is attractive for resource-constrained brain--computer interfaces (BCIs), but whether it changes adversarial vulnerability remains unclear. On BCI Competition IV-2a, we compare 32-bit floating-point (FP32) EEGNet and ShallowConvNet models with global magnitude pruning and simulated INT8 post training quantization (PTQ) and quantization-aware training (QAT) across nine subjects and three seeds. Simulation provides differentiable quantize--dequantize models for whit...

---

### 21. Training-Free Hold-Usage Detection in Sport Climbing with Foundation Pose Models

**Authors:** Abu Bakar, Abdullah Aftab, Amir Hamza

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30026v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30026v1)

**Summary:** Detecting which holds a climber uses, and when, underpins automated scoring, movement analysis, and assistive systems for sport climbing. Existing approaches train task-specific models or repurpose 2D pose estimators whose hand keypoint sits at the wrist and foot keypoint at the ankle i.e. offset from the fingertips and toes that actually contact the holds, and whose hands are occluded in roughly half of all frames. We show that a frozen, off-the-shelf pose foundation model is sufficient: using ...

---

### 22. GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS

**Authors:** Saim Rehman, Muhammad Shafique

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29999v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29999v1)

**Summary:** Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to qua...

---

### 23. OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning

**Authors:** Haoran Wang, Shaoyu Cai, Adrian Azzarelli, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29985v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29985v1)

**Summary:** Underwater 3D reconstruction is critical for marine exploration, ecological monitoring, and subsea infrastructure inspection, yet remains challenging at large scale due to light attenuation, scattering, and limited capture coverage. While 3D Gaussian Splatting (3DGS) enables high-quality real-time rendering, its application to large underwater scenes is constrained by high memory consumption and inefficient optimization over extensive areas. We propose OceanXL, a fast and scalable 3DGS-based fra...

---

### 24. ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting

**Authors:** De Jiang, Peiqiang Wang, Kehong Yuan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29963v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29963v1)

**Summary:** Textured Gaussians improve local appearance capacity, but assigning the same texture resolution to every primitive wastes storage on low-detail or weakly visible regions. We introduce AdaTex4D, an adaptive texture-capacity module for deformation-based 4D Gaussian Splatting. Each Gaussian carries packed RGBA triplanes whose two axes grow independently according to visibility normalized screen-space gradients and deformed local scales. Experiments on N3DV and PanopticSports show that AdaTex4D redu...

---

### 25. Not All Confusion Is Equal: A Source-Aware Uncertainty Diagnosis for Fine-Grained Aircraft Detection

**Authors:** Hai Huang, Helmut Mayer

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29959v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29959v1)

**Summary:** Fine-grained object detectors are commonly evaluated with confusion matrices, which show where the model is confused but not why, nor whether the confusion can be reduced. We argue that confusion can be attributed to distinct, separable sources, each quantitatively measurable, turning a passive measurement into actionable guidance. We present $A^2E^2$, a diagnostic tool that decomposes the sources of confusion along two axes, $\{$aleatoric, epistemic$\} \times \{$within-class, between-class$\}$,...

---

### 26. Mind What Matters for Reasoning: Aligning Cross-Modal Attention via Selective Probability Mass Concentration

**Authors:** Jiaqi Deng, Zonghan Wu, Zhan Heng, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29940v1)

**Summary:** Multimodal large language models (MLLMs) achieve strong performance on visual reasoning tasks, yet remain prone to hallucinations and over-reliance on language priors, often generating answers without adequately using task-relevant visual evidence. Existing approaches primarily improve reasoning through reasoning-oriented supervision or inference-time strategies. In this work, we study a complementary question: can multimodal reasoning be improved by strengthening implicit visual grounding witho...

---

### 27. Beyond Spatial Benchmarks: From Spatial Reasoning to Navigation

**Authors:** Xun Huang, Shijia Zhao, Rongsheng Qu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29934v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29934v1)

**Summary:** Does progress on spatial reasoning benchmarks translate into better navigation? Existing benchmarks test isolated inferences from images or videos, with little connection to downstream navigation. Our analysis reveals a gap between benchmark-oriented spatial specialization and navigation performance, and shows how aligning spatial supervision with navigation goals, phases, and decision learning improves navigation. Guided by these findings, we build \textsc{Spatial-Nav-100K} and fine-tune in two...

---

### 28. An Empirical Study of VLM Pipelines for Long-Document QA

**Authors:** Kenan E. Ak, Jay Mohta, Gwang Gook Lee, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29933v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29933v1)

**Summary:** Vision-Language Models (VLMs) are increasingly used for long-document processing, where the inputs combine text with charts, tables, figures, and complex layouts. Deploying them means choosing how to feed the document to the model, which retriever to use when only a subset of pages is sent, and whether to run the model agentically or as a static pipeline. We study these choices on two long-document QA benchmarks with both frontier API and open-weight VLMs. First, on MMLongBench-Doc our six-tool ...

---

### 29. It's the Geometry, Not the Model: Effective Rank and Subspace Alignment in Functional Connectivity Classification

**Authors:** Xiao Fan, Jingyuan Li, Yubo Han, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29932v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29932v1)

**Summary:** Resting-state functional connectivity (FC) is widely used to classify brain phenotypes and disorders. Most pipelines use the full connectome and seek gains through model design. We instead examine how FC geometry constrains classification and cross-site transfer. Across-subject FC variation concentrates in a small effective subspace, suggesting substantial redundancy in nominal dimensions. Across cohorts, these subspaces may differ in orientation even when their effective ranks are comparable, p...

---

### 30. EndoFSA: Endoscopic Few-Shot Image Generation via Rank-Constrained Parameter Adaptation

**Authors:** Panagiota Gatoula, Grigoris Karypidis, Dimitris K. Iakovidis

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29930v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29930v1)

**Summary:** WCE produces large-scale gastrointestinal image data yet pathological findings remain significantly underrepresented limiting the generalization performance of deep-learning based abnormality detection systems. SDG methods offer a practical solution to mitigate this imbalance. However their training directly on scarce abnormal samples often results in instability overfitting and structural distortions. Addressing these challenges requires controlled adaptation mechanisms that preserve anatomical...

---

### 31. When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression

**Authors:** Mingxuan Wang, Fei Luo, Bo Wang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29875v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29875v1)

**Summary:** Long horizon language model agents continually accumulate reasoning history, increasing context length and inference cost even after earlier decisions have been executed and observed. Unlike static Chain of Thought compression, removing historical reasoning can change future actions and the resulting interaction trajectory. We study when such reasoning can be safely forgotten. We propose Interaction Aware Compression for Long Horizon Reasoning (ICLR), a training free online method that ranks rea...

---

### 32. Efficient Continuous DEM Reconstruction under Limited Target-Resolution Supervision

**Authors:** Zekai Shi, Meng Zhang, Haokun Zhang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29864v1)

**Summary:** High-resolution digital elevation models (DEMs) support Earth observation applications, but paired training references are often available only at coarser output resolutions. Reconstructing finer terrain grids therefore requires both effective transfer beyond the supervised scale and control of dense-query computation. To address this problem, SCOPE learns a continuous terrain representation from coarser-resolution pairs. It predicts a latent coefficient field on the low-resolution grid and reus...

---

### 33. Modelling dynamic systems transfer functions from events in computational neuromorphic imaging

**Authors:** Nimrod Kruger, Gregory Cohen

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29863v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29863v1)

**Summary:** Event Vision Sensing (EVS) report threshold crossings of log-irradiance, so a static optical system imaging a static scene produces no output at all. The classical procedure for measuring a Point Spread Function (PSF), illuminating the system with a constant point source, therefore has no event-based equivalent: the probe must carry a temporal profile, and that profile becomes part of the measurement. A growing body of Computational Neuromorphic Imaging (CNI) work already exploits this, pairing ...

---

### 34. BeyondRetarget: Learning Executable Humanoid Motions Directly from Monocular Video

**Authors:** Tianyu Xiong, Yi Lu, Jinrui Wang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29850v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29850v1)

**Summary:** Learning executable motions from human videos offers a scalable solution for humanoid robots to acquire demonstration motions. However, existing pipelines typically first construct an explicit human motion representation and then convert it into robot motions via motion retargeting. Although such methods can effectively leverage large volumes of existing human data for training, the substantial differences between humans and humanoid robots in locomotion mechanisms and joint degree-of-freedom co...

---

### 35. SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting

**Authors:** Nitya Nanvani, Andras Palffy, Holger Caesar

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29836v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29836v1)

**Summary:** While 2D Vision Foundation Models offer a pathway to automate 3D semantic pseudo-labelling, translating these priors into robust 3D representations typically requires complex heuristics or multi-model ensembles. We introduce SplatLabel, an automated pipeline that leverages a 4D Gaussian representation to extract LiDAR segmentation with predictive confidence, as well as semantic occupancy grids at arbitrary voxel resolutions. At its core, SplatLabel handles dynamic environments through an explici...

---

### 36. Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding

**Authors:** Byounggun Park, Giyong Moon, Jusung Kim, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29835v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29835v1)

**Summary:** LiDAR provides precise geometric information for spatial perception tasks such as object detection in autonomous driving and outdoor robotics. However, recognizing and localizing individual objects is not sufficient to answer questions that require composing spatial relations and grounding the intended target. Motivated by recent advances in large language models (LLMs) for autonomous driving, we leverage their language priors to interpret complex spatial questions and ground the referred target...

---

### 37. Anatomy-Aligned Surface Field Learning for Myocardial Reconstruction from Sparse Short-Axis Cine MRI

**Authors:** Xiaohan Yuan, Xuan Yang, Qingya Li, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29825v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29825v1)

**Summary:** Patient-specific 4D myocardial reconstruction from cine MRI supports quantitative functional assessment, regional motion analysis, and simulation-based modeling. However, routinely acquired short-axis (SAX) cine MRI is sparsely sampled along the through-plane direction, making dense and anatomically consistent surface reconstruction challenging. In this study, we propose an anatomy-aligned surface learning framework that parameterizes the epicardial and endocardial surfaces on a shared circumfer...

---

### 38. AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation

**Authors:** Zhiyu Xu, Weilong Yan, Yufei Shi, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29816v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29816v1)

**Summary:** Recent years have witnessed major progress in joint audio-video generation. Existing models still suffer from limited per-modality fidelity, insufficient text-modality alignment and weak cross-modal synchronization. While reinforcement-learning post-training offers a promising remedy, directly adapting it to joint audio-video generation is challenging. Heterogeneous multimodal rewards entangle learning signals and complicate credit assignment. Joint optimization of two modality towers is computa...

---

### 39. S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving

**Authors:** Zhaowei Lu, Liguo Zhou, Yujie Guo, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29813v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29813v1)

**Summary:** We present S2Planner, a trajectory planner that combines three front-facing cameras with ego-motion history and the current driving command. A fine-tuned DINOv3 backbone and a Spatial Tuning Adapter produce multi-scale image features; a coarse-to-fine decoder then uses trajectory self-attention and camera-projected cross-attention to refine candidate waypoints. The contribution is the integration of ego-conditioned trajectory initialization with iterative, geometry-guided sampling of multi-scale...

---

### 40. OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing Optimization

**Authors:** Zhiyuan Ma, Wenbo Hu, Wang Zhao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29788v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29788v1)

**Summary:** Despite recent advancements in 3D generation, models often struggle to produce assets with high visual fidelity. To bridge this gap, we propose OREO, an alignment framework that enhances the realism of 3D generators by leveraging rich 2D diffusion priors. Instead of relying on static datasets, OREO establishes a dynamic optimization loop that produces on-the-fly edited renderings as 2D pseudo-targets. At its core, we introduce Reinforced Editing, which utilizes a 2D model to refine rendered view...

---

### 41. Lightweight Vision Transformer-Based U-Net for Brain Tumor Segmentation from MRI

**Authors:** Sheekar Banerjee, Md. Srabon Chowdhury, Md. Mahbub Hasan Akash, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29785v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29785v1)

**Summary:** Accurate brain tumor segmentation from Magnetic Resonance Imaging is essential for diagnosis, treatment planning, and surgical guidance. Although Convolutional Neural Networks, particularly UNet, have achieved significant success in medical image segmentation, they often struggle to capture the long-range spatial dependencies required to model tumors with irregular shapes and complex boundaries. This paper proposes a lightweight Vision Transformer UNet that combines the hierarchical feature extr...

---

### 42. Mind the Gap: Mesh-Guided Repair of Broken Vessels

**Authors:** Gniewosz Drwiega, Wojciech Szymanski, Marek Wodzinski

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29779v1)

**Summary:** Vessel segmentation is commonly optimized as voxel-wise classification, but small local errors can strongly disrupt vascular connectivity while having little effect on overlap scores. This is particularly problematic for downstream analyses that rely on centerlines, branches, connected components, or graph structure. We propose a mesh-guided post-processing framework for repairing broken vessel segmentations produced by nnU-Net. For each predicted binary mask, a deformable template mesh is fitte...

---

### 43. C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks

**Authors:** Xueshu Chen, Yan Wang, Zihao Xue, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29735v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29735v1)

**Summary:** Long-horizon tasks require preserving and later recovering cross-session evidence under a bounded, query-blind memory budget. Existing compression can discard fine-grained visual cues or conflate semantically similar but incompatible observations. We present C3M, a cross-session multimodal memory organization that maintains a bounded active index over persistent source text-image evidence. Relation-aware updates consolidate safe redundancy while preserving complementary and incompatible records....

---

### 44. A Multimodal Dataset for Survival Prediction in Resected Pancreatic Ductal Adenocarcinoma

**Authors:** Anh-Tien Nguyen, Mawuko Tettey, Jacqueline Michelle Metsch, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29726v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29726v1)

**Summary:** Survival research in pancreatic ductal adenocarcinoma (PDAC) is limited by the scarcity of datasets linking whole-slide histology with clinical, molecular, and long-term outcome data. We present a retrospective single-centre cohort of 302 patients who underwent PDAC resection at University Medical Center Gottingen. The dataset comprises 446 H&E whole-slide images, clinicopathological variables, targeted sequencing data for 154 patients, and overall-survival outcomes. During follow-up, 253 patien...

---

### 45. SALI: Shot-Aware Late Interaction for Cross-Shot Relation Matching in Text-to-Video Retrieval using Film-Grammar Knowledge

**Authors:** Toya Oyama, Rainer Lienhart, Shin'ichi Satoh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29721v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29721v1)

**Summary:** Text-to-video retrieval usually represents a video clip by a single embedding. This embedding often loses important relations between people. E.g., an interaction "Anna confronts Mark" is regularly filmed as alternating shot and reverse shot of both (Fig. 1a). No single shot or averaged embedding over clip shots captures this relation. Thus, we propose SALI (Shot-Aware Late Interaction). It extracts the subject and object from a single-sentence query, and matches the query, its subject and objec...

---

### 46. AgriCountDINO: Parameter-Efficient Exemplar-Guided Counting and Localization in Agriculture

**Authors:** Shengjie Guo, Xin Li, Borjana Arsova, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29460v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29460v1)

**Summary:** Accurate counting and localization of plants and their organs support phenotyping and yield estimation, yet target appearance, scale, and density vary widely across species and imaging conditions. Exemplar boxes specify the target without category-specific retraining, and point predictions identify the individual instances contributing to the count. We introduce AgriCountDINO, a parameter-efficient exemplar-guided framework for joint counting and localization. It conditions frozen multiscale DIN...

---

### 47. Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space

**Authors:** Jaron Yeh, Yen-Wei Chang, Jiang Liu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29457v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29457v1)

**Summary:** Industrial anomaly detection (IAD) is evolving beyond conventional detection and localization toward multimodal inspection systems that can describe, explain, and reason about fine-grained defects. Although recent multimodal large language model (MLLM)-based methods improve anomaly understanding through textual reasoning and visual guidance, they face two limitations in fine-grained inspection. First, their visual refinement often requires iteratively revisiting local image regions or augmenting...

---

### 48. Dense Coverage, Sparse Refinement: Byte-Constrained Cooperative Perception

**Authors:** Melih Yazgan, Timon Müller, J. Marius Zöllner

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29456v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29456v1)

**Summary:** Collaborative perception improves autonomous perception by sharing intermediate Bird's-Eye-View (BEV) features across connected agents, but dense feature exchange is difficult to deploy under strict Vehicle-to-Everything (V2X) bandwidth limits. Existing efficient methods typically either compress the full feature map uniformly, spending bits on low-value background, or sparsify communication, risking the loss of useful context. We propose a coverage-refinement design for byte-constrained coopera...

---

### 49. Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed

**Authors:** Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29447v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29447v1)

**Summary:** Smart maritime infrastructures provide continuous access to heterogeneous sensing streams, enabling repeated experimentation, digital-twin development, and AI-based maritime services. However, sensing hardware alone is not sufficient for scene-specific model development: historical video streams must also be spatially indexed, contextualized, and reduced to informative subsets for annotation. This paper presents a frame-to-panorama localization and context-aware sampling pipeline for ship detect...

---

### 50. Pose Adaptive Dynamic FiLM Modulation for Visual Speech Recognition

**Authors:** Matthew Kit Khinn Teng, Haibo Zhang, Takeshi Saitoh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29443v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29443v1)

**Summary:** Head-pose variation introduces substantial appearance transformations in visual speech recognition (VSR), making pose-aware feature modulation desirable. However, performance degradation and unwanted feature interactions may result from using numerous Feature-wise Linear Modulation (FiLM) circuits with fixed modulation intensity. We propose a Pose Adaptive Dynamic FiLM framework with a Dynamic Residual FiLM (DR-FiLM) modulator that predicts input-dependent weights to adaptively control the stren...

---

## cs.LG

**50 papers**

### 1. Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning

**Authors:** Sudip Bhujel, Shanghao Shi, Ruiquan Huang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30258v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30258v1)

**Summary:** Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-le...

---

### 2. Agentic Detection of Online Conspiracies

**Authors:** Lior Biton, Oren Tsur

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30250v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30250v1)

**Summary:** Conspiratorial discourse on social media is not always expressed through explicit claims or stable lexical markers. The same surface content may express endorsement, legitimate concerns, criticism, satire, or mockery. The main challenge is therefore not only recognizing conspiracy-related claims, but inferring the speaker's intent -- the utterance's illocutionary force. We argue that this can be achieved through the use of relevant social contexts and propose an agentic framework, equipped with ...

---

### 3. To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech

**Authors:** Debajyoti Mazumder,  Mamta, Abhirama Subramanyam Penamakuri

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30227v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30227v1)

**Summary:** Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benc...

---

### 4. PoEM: Predicting RL Outcomes from Existing Policies

**Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30226v1)

**Summary:** Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirma...

---

### 5. Minimally Invasive Steering of Language Models

**Authors:** Taha Entesari, Jingyu Zhang, Daniel Khashabi, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30218v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30218v1)

**Summary:** Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed...

---

### 6. A Nearly Quadratic Lower Bound for Linear Optimization over Convex Bodies in the Membership Oracle Model

**Authors:** Santosh S. Vempala

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30215v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30215v1)

**Summary:** We prove nearly quadratic lower bounds for randomized algorithms for linear optimization and uniform sampling over convex bodies in the membership oracle model. For linear optimization, this matches the known nearly quadratic upper bound up to a polylog factor in the dimension. For uniform sampling, this improves on the previous linear lower bound. Our construction also implies the same lower bound for volume estimation.

---

### 7. Anchored Extra-Proximal Methods: Optimal Higher-Order Methods for Monotone Inclusion Problems

**Authors:** Ruichen Jiang, TaeHo Yoon

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30212v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30212v1)

**Summary:** We study the deterministic oracle complexity of finding approximate solutions to composite monotone inclusion problems, formed by the sum of a smooth single-valued monotone operator and a maximally monotone set-valued operator, under the tangent-residual criterion. We introduce the Anchored Extra-Proximal (AEP) framework, which combines an anchored extrapolation step with an inexact anchored proximal update satisfying a relative-error condition. The framework recovers the composite Fast Extragra...

---

### 8. The Alignment Illusion in Multimodal Large Language Models

**Authors:** Hong-Han Wang, Yuntao Wang, Hu Ding

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30210v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30210v1)

**Summary:** Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interaction. To test this assumption, we apply controlled interventions to the visual stream. Across 13 MLLMs from five families spanning 0.5B to 72B parameters, replacing projector-output...

---

### 9. Beyond Compression: Training Latent Representations for Stable Long-Horizon Rollout in Neural Surrogate Solvers

**Authors:** Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30198v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30198v1)

**Summary:** Latent neural surrogate solvers, or latent dynamics models, accelerate simulations of time-dependent physical systems by evolving a compressed latent space rather than resolving full-resolution fields directly. In principle this reduces computational cost and simplifies learning, but in practice errors often accumulate rapidly during long autoregressive rollouts, limiting predictive utility. We show that this instability does not stem from the latent representation itself, but arises when it is ...

---

### 10. Intrinsic-Extrinsic Coupling in Learning Dynamics

**Authors:** Qinyou Wang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30185v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30185v1)

**Summary:** A learner's current observations need not determine its response to further training. We formulate intrinsic-extrinsic coupling through the continuation-conditioned value of a constrained learning-state intervention, with observation-relative fibers describing present agreement. An executable finite-frame classifier-head write protects current logits while repairing specified historical margins under finite-precision acceptance checks. We distinguish local admissibility, continuation-conditioned...

---

### 11. GridSFM: A Foundation Model for Solving AC Optimal Power Flow

**Authors:** Luke Bhan, Weiwei Yang, Margaret Capetz, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30173v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30173v1)

**Summary:** We introduce GridSFM, a framework that combines a pretrained foundation model across grid topologies with physics-informed fine-tuning for solving AC Optimal Power Flow (AC-OPF) at scale. It is a $15$ million parameter physics-inspired graph neural network pretrained across $54$ topologies of $500$ to $4{,}000$ buses. Our model attains a $2.45\%$ zero-shot generation-cost error on a $10{,}000$ bus case held-out operating conditions with no degradation as system size grows. Building on this, we p...

---

### 12. Do Audio Language Models Hear and Read Distinctive Features Alike?

**Authors:** Yuanhao Chen, Peter Chin

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30167v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30167v1)

**Summary:** Audio language models pass speech and text through a single decoder. We ask whether that decoder represents a distinctive feature in the same direction when a phoneme is heard and when it is read. For minimal pairs of phonemes differing in one feature, we take the offset between the two members' mean representations. Averaging those offsets gives a direction for each stream, and we measure the cosine between the two. Because the two streams already agree about arbitrary phoneme pairs, we compare...

---

### 13. Learning and interpreting policies for simultaneous entanglement requests in quantum networks

**Authors:** Leon Rode, Sumeet Khatri, Supartha Podder

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30157v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30157v1)

**Summary:** Future quantum networks will make use of entanglement to perform numerous tasks, such as sending quantum information over long distances, distributed quantum computing, and quantum sensing. In general, these tasks will need to be performed simultaneously in various regions of a network, while minimizing resources and latency. We will thus require policies for scheduling link-level entanglement resources, and using the link-level entanglement to create various forms of multipartite entanglement r...

---

### 14. Does a model's stated reason for rejecting a candidate do any work?

**Authors:** Archit Rastogi

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30151v1)

**Summary:** Asked to choose between candidates and explain the choice, a language model often rejects a rival by naming a fact its profile lacks: no director, no date of death. That sentence is a claim about the text in front of the model, and it can be tested without any judge. We insert a real corpus sentence stating the named fact into the rival's profile and ask again under greedy decoding. Two controls separate content from placement: a length-matched irrelevant sentence at the same profile, and the sa...

---

### 15. Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management

**Authors:** Giacomo Arcieri, Gregory Duthé, Christophe Muller, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30150v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30150v1)

**Summary:** Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail...

---

### 16. GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI

**Authors:** Arunabh Srivastava, Mohammad A.,  Khojastepour, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30147v1)

**Summary:** Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within iso...

---

### 17. Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30115v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30115v1)

**Summary:** Modern deep neural networks treat parameters as static floating-point matrices stored in physical memory, incurring Von Neumann memory bottlenecks and representation collapse. We formulate Orbital Error Dynamics (OED), an analytical framework wherein synaptic weights are not stored masses (O(W)), but transient topological resonances (O(1)) derived procedurally from the complex quadratic polynomial map z_{n+1} = z_n^2 + c. We introduce the Bent Sine Wave Hypothesis, demonstrating that non-equilib...

---

### 18. On the SoS Certifiability of Log-Concave Distributions

**Authors:** Aleksandr Storozhenko

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30105v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30105v1)

**Summary:** For an arbitrary isotropic log-concave distribution $P$ on $\mathbb{R}^d$, we prove that the polynomial $(Cm)^m\|v\|_2^m - \mathbb{E}_{X\sim P}\langle X,v\rangle^m$ is a sum of squares for every even $m\ge2$, where $C>0$ is a universal constant. This removes the dependence on the Poincaré constant in the theorem of Kothari and Steinhardt (arXiv:1711.07465), recovering the optimal moment bounds for log-concave distributions. As an immediate corollary, we obtain computationally efficient algorithm...

---

### 19. MQSS-Selector: RL-Guided Pass Selection for an MLIR Compilation Pipeline

**Authors:** Andre Youssefi, Ercüment Kaya, Minh Chung, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30104v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30104v1)

**Summary:** High Performance Computing (HPC) and Quantum Computing (QC) systems are increasingly converging towards unified High Performance Computing-Quantum Computing (HPCQC) infrastructures, driven by a growing need to bridge classical and quantum workflows, which affects all levels of the system stack, from the hardware to compilers and runtimes, all the way to applications. However, today's QC devices are still in the Noisy Intermediate-Scale Quantum (NISQ) era, are error-prone and resource-limited, an...

---

### 20. AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs

**Authors:** Xiaochen Zhang, Haoyu Zhu, Yao Zhang, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30088v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30088v1)

**Summary:** Graph-structured optimization with linear constraints is fundamental to critical infrastructure but faces scalability limits due to massive strict hard constraints and high dimensionality. While recent projection-based methods such as Trainable Sampling Kaczmarz-Motzkin Net (T-SKM-Net) guarantee feasibility, they face high computational costs in dynamic environments by processing the entire constraint set and requiring expensive matrix factorizations. To bridge this gap, we propose the Accelerat...

---

### 21. Return or Revise? Learning When Revision Helps Retrieval-Augmented QA

**Authors:** Nicholas Kashani Motlagh, Tim Anderson, Jeremy Gwinnup, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30087v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30087v1)

**Summary:** We consider the decision of whether to return an existing draft answer or revise it using retrieved evidence, as in answer-revision systems. Draft confidence estimates whether the current answer is correct, but the decision requires estimating the effect of a specified revision. For offline training and evaluation, we grade both the returned draft and its candidate revision under the same correctness judge, which makes repair, harm, and the gap to an oracle observable. We call this paired effect...

---

### 22. Residual Correlation as a Diagnostic for Joint-Uncertainty Gains from GP Coregionalisation

**Authors:** Fangqin Zhou, Joaquin Vanschoren

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30085v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30085v1)

**Summary:** In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent. Across the settings studied, we find that the main benefit of coregionalisation is joint uncertainty quantification rather than point prediction. Raw target correlation does not predict when coupling helps; in the separable...

---

### 23. Reachability-Based Formal Verification of Graph Neural Networks with Node and Edge Features

**Authors:** Anne M. Tumlin, Ben Wooding, Zhenxuan Shao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30079v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30079v1)

**Summary:** Graph neural networks (GNNs) have become a prominent approach for developing fast, topology-aware surrogates in electric power systems, supporting tasks such as power flow (PF) analysis, optimal power flow (OPF) estimation, and cascading failure analysis (CFA). Despite this growing use, formally verifying GNN-based models remains challenging, with existing methods limited in scope. We extend the neural network verification (NNV) framework to graph-structured inputs through GraphStar sets, a gene...

---

### 24. Nuclear Norm-Regularized Bayesian Matrix Completion

**Authors:** Calvin Tolbert

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30078v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30078v1)

**Summary:** Matrix completion, the problem of estimating missing entries in a matrix from noisily observed ones, underlies a diverse array of problems such as recommender systems and counterfactual outcome estimation in panel data. Many algorithms address the problem using regularized least squares, often with the nuclear norm as a regularizer, but this method yields a point estimate with no built-in uncertainty quantification. A Bayesian formulation is a natural alternative, and if the noise variance is kn...

---

### 25. How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure

**Authors:** Dipankar Sarkar

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30074v1)

**Summary:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from...

---

### 26. KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization

**Authors:** Aheli Poddar, Sanskar Prasad, Arindam Samanta, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30059v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30059v1)

**Summary:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins. Recent LLM-assisted kernel optimizers can close this gap for standalone kernels, yet treat compiled models as black boxes, generally optimizing individual standalone kernels without respecting the compiler's structural decisi...

---

### 27. From Processing to Functionality: Engineering Accessible Material States in Cu-Embedded SiO$_x$ Memristive Devices

**Authors:** Tobias Gergs, Rouven Lamprecht, Sahitya Yarragolla, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30047v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30047v1)

**Summary:** Resistive switching in oxide-based devices is widely governed by stochastic defect processes, yet a predictive link between fabrication conditions and functional behavior remains elusive. Here, we establish a multiscale framework connecting plasma-defined deposition conditions to macroscopic device functionality in sputtered SiO$_x$/Cu/SiO$_x$-based systems. By combining large-scale statistical analysis of more than 50,000 experimentally characterized devices with physics-based plasma and atomis...

---

### 28. AERIAL: Adversarial Evaluation of Robustness in Accuracy-Preserving Low-Precision EEG Decoders

**Authors:** Saim Rehman, Muhammad Shafique

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30037v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30037v1)

**Summary:** Deployment-oriented compression is attractive for resource-constrained brain--computer interfaces (BCIs), but whether it changes adversarial vulnerability remains unclear. On BCI Competition IV-2a, we compare 32-bit floating-point (FP32) EEGNet and ShallowConvNet models with global magnitude pruning and simulated INT8 post training quantization (PTQ) and quantization-aware training (QAT) across nine subjects and three seeds. Simulation provides differentiable quantize--dequantize models for whit...

---

### 29. Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think

**Authors:** Xvyuan Liu, Jianjie Fang, Chen Gao, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30036v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30036v1)

**Summary:** Planners built on visual world models commonly score each predicted outcome by its distance to the encoded goal image. We show that this target can limit control even with exact dynamics and globally optimal short-horizon search: reaching a goal may require actions that initially move away from it. With frozen LeWM models, intermediate targets substantially improve action synthesis and recorded-action ranking on Cube, PushT, Reacher, and TwoRoom. Learned targets and targets drawn from observed e...

---

### 30. Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits

**Authors:** Michael Jerge, Suman Jana

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30017v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30017v1)

**Summary:** Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree. This structure arises naturally from autoregressive generation: every prefix defines a node, and its continuations form a subtree below it. Internal nodes of the tree provide cheap but biased estimates of a region's value, while leaf evaluations are expensive but accurate. Hierarchical bandit methods can exploit this structure, but typic...

---

### 31. GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS

**Authors:** Saim Rehman, Muhammad Shafique

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29999v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29999v1)

**Summary:** Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to qua...

---

### 32. Let Training Guide Selection: Online Synthetic Data Filtering via Real-Anchored Utility

**Authors:** Yanran Wu, Sana Lakdawala, Renzo Tassara Miller, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29988v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29988v1)

**Summary:** Synthetic data can scale training supervision when real-world data are limited, but noise and distribution mismatch can reduce its value. Existing synthetic data selection methods often emphasize fidelity or diversity rather than the learner's evolving needs. We propose FROST, an online framework that estimates synthetic-data utility through gradient feedback anchored in real training data. It calibrates batch utility against recent history to determine when filtering is needed and filters sampl...

---

### 33. Diverse Geometries, Frozen Weights: Robust Heterogeneous Treatment-Effect Estimation via Causal Expert Ensembles

**Authors:** Ali Haghpanah Jahromi, Mohammad Taheri

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29974v1)

**Summary:** Estimating heterogeneous treatment effects from observational data is difficult because the most appropriate inductive bias varies with overlap, treatment imbalance, prognostic structure, and sample size. We introduce the Geometry-Diverse Anchor-Correction Expert Ensemble (GeoACE), a five-expert framework that combines a common anchor-correction estimator with complementary overlap-aware and outcome-guided geometries. Its task-level ensemble weights are learned only from internal validation pred...

---

### 34. A Contraction Framework for Stochastic Operators with Bootstrapping: Application to TD Learning

**Authors:** Ids van der Werf, Sergio Rozada, Antonio G. Marques

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29961v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29961v1)

**Summary:** Many iterative algorithms rely on bootstrapping. A variable is updated using a second, frozen copy as a target, which is periodically replaced with the updated variable. Majorize-minimize and inexact proximal-point methods share this structure, as does temporal-difference (TD) learning. However, existing convergence guarantees for scenarios that combine sampled updates with targets refreshed only every $K$ steps rely on the specific structure of the update, such as linear approximation or gradie...

---

### 35. Beyond Average Safety: Chance-Constrained LLM Fine-tuning

**Authors:** Taha Entesari, Mahyar Fazlyab

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29960v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29960v1)

**Summary:** Fine-tuning large language models on new objectives can improve helpfulness, instruction following, or domain-specific performance, but it can also induce regressions on safety-critical prompts. Existing safety-preserving fine-tuning methods typically control average safety loss or use weighted auxiliary penalties, which can obscure rare but severe failures. We propose a chance-constrained formulation for safety-preserving fine-tuning that limits the fraction of safety examples whose degradation...

---

### 36. Not All Confusion Is Equal: A Source-Aware Uncertainty Diagnosis for Fine-Grained Aircraft Detection

**Authors:** Hai Huang, Helmut Mayer

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29959v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29959v1)

**Summary:** Fine-grained object detectors are commonly evaluated with confusion matrices, which show where the model is confused but not why, nor whether the confusion can be reduced. We argue that confusion can be attributed to distinct, separable sources, each quantitatively measurable, turning a passive measurement into actionable guidance. We present $A^2E^2$, a diagnostic tool that decomposes the sources of confusion along two axes, $\{$aleatoric, epistemic$\} \times \{$within-class, between-class$\}$,...

---

### 37. Multi-Dimensional Matching

**Authors:** Irene Aldridge

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29958v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29958v1)

**Summary:** We study a matching mechanism where agents and objects are described by features rather than complete rankings. A single spectral projection reduces the problem to a one-dimensional sort, computable in O(N log N) time. We prove that on descaled features and preferences, our algorithm obtains the exact Nash Social Welfare (NSW) optimum within the projected space, with an unconditional utilitarian-welfare guarantee and a conditional NSW guarantee. The proposed mechanism is stable against exogenous...

---

### 38. Tracking States or Tracking Cosets? An Algebraic Account of Learned State Tracking

**Authors:** Zhiyu Zhang, Yupeng Li

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29951v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29951v1)

**Summary:** State tracking requires composing a sequence of updates, but accuracy alone does not reveal what a model has learned. We study neural networks trained to predict the running product of group elements. We identify quotient solutions in Transformers, where models recover the quotient class while predicting nearly uniformly among its members. The reciprocal of class size predicts partial accuracy without a fitted parameter, extending parity-based accounts to non-parity quotients. Our baseline Trans...

---

### 39. Error- and Prediction-Driven Motor Learning in the Cortico-Cerebellar Loop

**Authors:** Ana Carolina Filipe, Rui Ponte Costa, Cláudia Soares

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29945v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29945v1)

**Summary:** Robust control under delayed sensory feedback remains a key challenge in both robotics and neuroscience. Classical cerebellar models explain delay compensation through forward prediction but fail to account for fast online corrections and rapid adaptation observed in biological systems.   We propose a cerebellum-inspired control framework that combines multiplexed predictive representations with internal feedback. By jointly encoding kinematic variables and task-relevant error signals, the model...

---

### 40. MF-SCBO : Multi-fidelity Scalable Constrained Bayesian Optimization

**Authors:** Lucas Palazzolo, Mickaël Binois, Laëtitia Giraldi

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29941v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29941v1)

**Summary:** Many real-world optimization problems rely on expensive simulations or experiments, making the efficient use of available data essential. Multi-fidelity optimization of high-dimensional black-box functions subject to black-box constraints is increasingly relevant as the cost of objective evaluations continues to rise in applications such as machine learning, engineering, and control. To our knowledge, no existing method simultaneously addresses high-dimensionality, black-box constraints, an arbi...

---

### 41. When Temporal Perturbations Act Like Sensor Biases: Label-Free Auditing of Wearable Activity Recognizers

**Authors:** Qingyu Wu, Yuan Wei, Renju Liu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29937v1)

**Summary:** Wearable human-activity recognition (HAR) models operate across sensors, subjects, and backbones, yet a smooth waveform may appear temporal while exploiting a persistent sensor offset primarily. We introduce SpectrumAudit, a label-sealed audit that fits a phase-randomized full-window stimulus on calibration windows from subjects held out from training and testing. After selection, it replays its exact DC projection and budget-constrained zero-mean residual on the same frozen victim without refit...

---

### 42. Path-specific harm decomposition: A partial identification framework

**Authors:** Ruizi Yan, Dennis Frauen, Maresa Schröder, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29938v1)

**Summary:** A central goal when designing treatment policies is often to "do no harm", that is, to avoid interventions that improve average outcomes while worsening outcomes for some individuals. A widely used notion for harm is the fraction of negatively affected (FNA), defined as the probability that an intervention decreases an individual's outcome. However, in many applications, treatments operate through mediators, and a single "total" FNA can obscure whether harm arises primarily through direct pathwa...

---

### 43. Robust Detection of LLM-Generated Text under Contamination

**Authors:** Jiaxun Li, Saptarshi Chakraborty, Ambuj Tewari

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29935v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29935v1)

**Summary:** We study the detection of LLM-generated text under editing and contamination. Modeling human and machine text as finite-order Markov processes with Huber contamination, we characterize an exact boundary for reliable detection under our assumptions. Detection is impossible when contamination is sufficiently large relative to clean-source separation. Below this boundary, a collection of clipped likelihood-ratio tests achieves vanishing worst-case errors. This construction motivates clipping as a s...

---

### 44. Improving Calibration of Black-Box Radiology AI Using Test-Time Augmentation

**Authors:** Nathan Le, Magdalini Paschali, Arogya Koirala, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29931v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29931v1)

**Summary:** Radiology AI systems increasingly inform clinical decisions such as triage, follow-up imaging, and treatment planning. For these decisions to be made safely, model outputs must be well calibrated, meaning predicted probabilities accurately reflect true risk. Many standard techniques for improving calibration, such as MC Dropout and Deep Ensembles, require access to model parameters or retraining. However, proprietary clinical AI systems operate as black boxes, preventing access to the model's in...

---

### 45. Spatio-temporally complementary feature propagation on graphs for longitudinal AADT estimation

**Authors:** Linghang Sun, Qishen Zhou, Michail A. Makridis, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29906v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29906v1)

**Summary:** The estimation of Annual Average Daily Traffic (AADT) is vital for transportation planning and infrastructure maintenance, yet obtaining accurate values for an entire urban network across multiple years remains challenging due to the high cost and spatial sparsity of physical sensors. This research proposes a novel spatio-temporally complementary feature propagation framework that leverages the strengths of two distinct data sources: spatially sparse but temporally dense loop detector data, and ...

---

### 46. Cost-Sensitive Online Window Size Selection for Portfolio Management

**Authors:** Yi-Chen Liu, Chung-Han Hsieh

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29887v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29887v1)

**Summary:** This paper investigates cost-sensitive online window size selection for portfolio management under changing market conditions. Specifically, we propose a two-level framework that constructs portfolios using candidate window sizes and dynamically aggregates them through online learning. By treating candidate window sizes as ``experts,'' we dynamically update their aggregation weights using turnover-inclusive losses. Moreover, we derive finite-horizon cost-sensitive tracking-regret bounds that acc...

---

### 47. A New Gap Sequence for Shellsort: RL-Driven Algorithm Discovery Beyond $N^{4/3}$

**Authors:** Bo Liu

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29881v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29881v1)

**Summary:** Choosing Shellsort gaps is a well-known open problem. For over sixty years, successful sequences have relied on human-designed formulas, numerical searches, or number-theoretic constructions. Although stronger general bounds exist for dense or mainly theoretical families, the worst-case upper bound for a short, sparse, and practically competitive construction has not advanced beyond $N^{4/3}$ for decades. We ask whether the sequence itself can instead be learned from execution. We present an RL-...

---

### 48. From Graphs to Feeders: Constraint-Guided Diffusion for Rule-Compliant Feeder Generation

**Authors:** Yu Qin, Andrew Glaws, Aadil Latif, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29879v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29879v1)

**Summary:** Generative modeling approaches often focus on recovering broad statistical characteristics from the training data. In the context of graph generation, this may refer to degree distributions, clustering coefficients, or spectral properties. However, generating usable distribution feeders when detailed feeder models are unavailable requires more than matching generic graph statistics: the sampled topology must also obey electrical compatibility and radiality rules. We therefore formulate feeder sy...

---

### 49. Does per-frame early exit pay? A compute-matched study of dynamic depth for on-device speech enhancement

**Authors:** Clément Laroche, Riccardo Miccini

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29867v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29867v1)

**Summary:** Deep learning-based speech enhancement is increasingly deployed on-device in hearing aids, headsets, and earbuds. Most of these devices, however, can only accelerate static int8 graphs, so a depth-varying network must be implemented as several graphs, orchestrated by a policy. In this paper, we supervise every intermediate depth of one causal model, then we fine-tune its output heads to guarantee that deeper outputs are never worse than shallower ones. Using this training protocol, we can derive...

---

### 50. Beyond Model Size: Redesigning LiSenNet for embedded speech enhancement

**Authors:** Clément Laroche, Rasmus Kongsgaard Olsson

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29866v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29866v1)

**Summary:** Deploying real-time speech enhancement on resource-constrained devices requires meeting strict latency, memory, and energy constraints. Microcontroller NPUs can accelerate neural inference under these constraints, but only through a restricted set of operators in static, integer-quantized graphs. Recent speech-enhancement networks have reduced parameter counts and MACs to levels nominally suitable for microcontrollers, but their operators and execution patterns often remain incompatible with res...

---

## cs.NE

**50 papers**

### 1. Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30115v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30115v1)

**Summary:** Modern deep neural networks treat parameters as static floating-point matrices stored in physical memory, incurring Von Neumann memory bottlenecks and representation collapse. We formulate Orbital Error Dynamics (OED), an analytical framework wherein synaptic weights are not stored masses (O(W)), but transient topological resonances (O(1)) derived procedurally from the complex quadratic polynomial map z_{n+1} = z_n^2 + c. We introduce the Bent Sine Wave Hypothesis, demonstrating that non-equilib...

---

### 2. Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons

**Authors:** Ruiyu Jia, Zhuo-Cheng Xiao

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30102v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30102v1)

**Summary:** Most ANN-to-SNN conversion methods rely on a specific correspondence between the source activation and the spiking neuron dynamics. We propose a finite-state continuous-time Markov chain (CTMC) neuron framework whose stationary spike flux can approximate every continuous nonnegative monotone activation function on a compact interval. For a generalized CTMC family with affine input-dependent transitions, we prove uniform approximation to arbitrary accuracy over this function class and derive an e...

---

### 3. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v1)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 4. Boolean threshold functions, neuron capacity, and memory retrieval

**Authors:** Xinyuan Xie

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29756v1)

**Summary:** How much information can a single neuron remember? How many memories can neural networks retrieve without creating false memories? These questions are related to a basic question: how many Boolean threshold functions $f(x)=\operatorname{sgn}(a_0+\langle a,x\rangle)$, $x\in\{-1,1\}^n$, are there? In this paper, we show that the number $T_n$ of distinct Boolean threshold functions is \[ T_n=2\binom{2^n-1}{n}\bigl(1+O(n^{-99})\bigr). \] Equivalently, the capacity of a single threshold neuron is $n^...

---

### 5. On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation

**Authors:** Benedikt Hartl, Milton L. Montero, Marcello Barylli, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29755v1)

**Summary:** How phenotypic transformations are implemented by changes in underlying regulatory dynamics remains a central question in developmental biology. Inspired by D'Arcy Thompson's 1917 "On Growth and Form", we ask whether coherent large-scale transformations of morphology can be encoded as low-dimensional modulations of a self-organizing developmental system. We use neural cellular automata (NCAs) as bio-inspired models of distributed development, in which a shared local regulatory network grows targ...

---

### 6. Dynamical Diversity for Reservoir Computing in Reconfigurable Nanomechanics

**Authors:** Humayun Ahmed, Inês S. Garcia, Filipa C. Mota, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29532v1)

**Summary:** Physical reservoir computing uses nonlinear dynamics and a trained linear readout to process information. Nanoelectromechanical (NEMS) resonators combine geometric Duffing nonlinearity with fading memory, but most electromechanical implementations use a single resonance mode. Here, we demonstrate reservoir computing with two interacting modes of a single NEMS resonator measured through one readout port. We introduce dynamical diversity through complementary modal drive settings: the same input s...

---

### 7. Online Task Adaptation via Self-Organisation

**Authors:** Krsto Proroković

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29281v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29281v1)

**Summary:** Neural networks are typically adapted by computing gradients and updating model parameters. We investigate whether task-specific adaptation can instead emerge from a meta-learned self-organising process that requires no gradients at adaptation time. We instantiate this idea with a Neural Cellular Automaton in which locally interacting recurrent cells maintain both a recurrent state and a fast associative memory. During meta-training, backpropagation is used to learn the recurrent dynamics togeth...

---

### 8. EvoTreeNAD: Genealogy-Guided Evolution for LLM-Driven Neural Architecture Discovery

**Authors:** Lishan Yu, Derek Jiu, Qizhen Lan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29016v1)

**Summary:** AI-driven scientific discovery accelerates research by autonomously developing solutions and designs. Large language model (LLM) agents support this process through iterative generation and evaluation. Yet these iterations alone do not ensure cumulative progress or establish which directions to pursue next. Costly evaluation further constrains the scope of exploration. Neural architecture discovery brings these challenges together, coupling open-ended design with resource-intensive experimentati...

---

### 9. Learning Holographic Reduced Representations with Clifford Variational Autoencoders

**Authors:** Mohamed Malek Abid, P. Michael Furlong

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28409v1)

**Summary:** Vector Symbolic Algebras project data structures into a hyperdimensional vector space through the application of their vector algebras to randomly generated atomic vector symbols and fractional power encodings of real-valued data. Embedding unstructured data remains an open question. We present \textit{Clifford-VAE}, a variational autoencoder that learns to project data onto a Clifford torus in arbitrary dimensions. Experiments using the MNIST, FashionMNIST, and CIFAR-10 datasets demonstrate tha...

---

### 10. Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games

**Authors:** Gijs van Cuyck, Patric Feldmeier, Jan Tretmans, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28130v1)

**Summary:** Automatically generating test inputs for games is challenging, as test generators must master the game to reach advanced program states while also ensuring robustness against the heavy program randomisation inherent to games. The test generator Neatest therefore optimises test suites consisting of neural networks that reach advanced program states and are robust to program randomisation, as they generate test inputs dynamically based on the current program state. Neatest is a white-box testing a...

---

### 11. Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond

**Authors:** Yiqian Yang, Yiqun Duan, Chenyu Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27650v2) | 📄 [PDF](https://arxiv.org/pdf/2609.27650v2)

**Summary:** Brain-to-language decoding translates neural activity associated with language production, internal speech and perception into linguistic or expressive outputs. It offers a route to restoring communication after speech loss and a means of studying how the brain represents language. Advances in neural recording and representation learning have expanded the field from constrained recognition and acoustic reconstruction to text generation, streaming personalised speech and facial animation. This su...

---

### 12. Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning

**Authors:** Mikhail Kiselev

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27459v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27459v1)

**Summary:** This paper presents a spiking neural network (SNN) designed to predict the sequence of the external world states starting from the current world state. This SNN does not create the world dynamics model - instead it incorporates the SNN trained to predict the next world state and provides all mechanisms necessary to make the chain of predicted world states. These mechanisms are entirely spiking - they are implemented as spiking neuron ensembles. The present article describes this neuronal structu...

---

### 13. An Unbounded Archive-based Transfer Strategy for Dynamic Multi-Objective Optimization with a Changing Number of Objectives

**Authors:** Zhiyun Xiao, Ke Shang, Yajun Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27430v1)

**Summary:** Dynamic multi-objective optimization with a variable number of objectives is difficult because objective-dimensional variations may significantly change the Pareto front and degrade algorithm adaptability. This paper proposes an unbounded archive-based transfer strategy (UATS), which maintains an unbounded archive of offspring solutions within each environment stage and extracts feasible nondominated solutions as transferable elites when objective changes occur. UATS is embedded into SPEA2SDE to...

---

### 14. Combining LLMs and Genetic Search for ARC-AGI-2

**Authors:** Val Dyachenko

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27242v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27242v1)

**Summary:** LLMs can generate programs for ARC-AGI-2 tasks, but the provided compute only allows a small number of attempts to generate, debug and validate solutions. Genetic algorithms can search and test many more programs, but random search rarely starts in a useful neighborhood of the solution space. We combine the two methods through a compact domain specific language (DSL). First, a quantized Qwen3.5-4B LLM generates an initial set of programs for each ARCAGI-2 task. Then, we use those programs to see...

---

### 15. LexLattice: Multilingual Extractive Summarization via Neural Cellular Automata on Document Hierarchies

**Authors:** Sujay Uday Rittikar, Sheela Ramanna

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.27032v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27032v1)

**Summary:** Faithfulness is a central concern in legal text summarization, which motivates extractive approaches that select verbatim content traceable to its source. Such methods typically rank paragraphs or other structural units in isolation, yet give little attention to consolidating evidence that is distributed across, and shares salience between, distant parts of a document. We introduce LexLattice, an extractive summarizer that reifies a legal act's hierarchy as a two-dimensional semantic lattice and...

---

### 16. The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity

**Authors:** Agnese Adorante, Aaron Spieler, Anna Levina

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26940v1)

**Summary:** Biological sensory neurons have selective receptive fields organized along meaningful stimulus coordinates, such as frequency, motion direction, or retinotopic position. Such structure may arise from efficient coding and biological constraints on activity, connectivity, and wiring, as computational studies of simple neurons have shown across modalities. This raises a question: do structured receptive fields confer a computational advantage beyond resource efficiency itself, and does this advanta...

---

### 17. When Recursive Models Finish Computing

**Authors:** Hare Krishna, Shubham Singh, Stephen Ebert, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26487v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26487v1)

**Summary:** Recursive models can continue updating their latent states beyond their nominal inference budget, so an incorrect output at that budget does not show whether computation is unfinished or has entered a persistently unsuccessful regime. We study the dynamics of completion in attention- and MLP-based Tiny Recursive Models (TRMs) on 1,000 hard Sudoku puzzles. Extending recurrence from the nominal 16 steps to 512 steps increases cumulative exact-solve accuracy from 59.2% to 87.5% for the attention mo...

---

### 18. Rethinking Pairwise Token Interaction in Spiking Transformers

**Authors:** Sicheng Shen, Dongcheng Zhao, Zhiyuan Li, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26297v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26297v1)

**Summary:** Spiking Transformers inherit token interaction mechanisms from conventional Transformers, yet their sparse binary representations fundamentally alter how token-to-token communication is established. In particular, spike-based query-key matching produces highly sparse and input-dependent interaction patterns, coupling information propagation to the instantaneous availability of matching spike events. This motivates a different interaction paradigm in which long-range communication does not rely s...

---

### 19. In-Context Guidance: Learning Inter-Task Synergies via Numerical Foundational Models for Few-Shot Multitask Optimization

**Authors:** Tingyang Wei, Haofeng Wu, Jiao Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25836v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25836v1)

**Summary:** Multi-task optimization (MTO) addresses a set of optimization tasks simultaneously, often suffering from inaccurate inter-task relationship estimation under limited evaluation budgets, leading to negative transfer. This paper introduces In-Context Guidance Multitask Optimization (ICG-MTO), a novel framework that leverages numerical foundational models to improve inter-task coupling estimation in few-shot scenarios. Unlike conventional methods that rely solely on scarce observed data, ICG-MTO emp...

---

### 20. NeuroRule: Making Black-Box Neural Networks Explainable through Rule-set Evolution

**Authors:** Tapaswini Kodavanti, Hormoz Shahrzad, Risto Miikkulainen

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26841v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26841v1)

**Summary:** High-capacity neural network models have achieved state-of-the-art performance across diverse classification tasks, yet they frequently operate as black-box models, lacking the transparency necessary for critical decision-making. Such opacity creates a persistent trade-off between performance and explainability. This paper proposes a solution to address this gap: the NeuroRule knowledge distillation framework that results in explainable rule-sets from neural network models. NeuroRule adapts the ...

---

### 21. Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25498v2) | 📄 [PDF](https://arxiv.org/pdf/2609.25498v2)

**Summary:** Deploying Large Language Models for runtime operational triage incurs prohibitive latency (>100-500 ms), high VRAM requirements (>4-8 GB), and excessive energy dissipation. Extending Mandelbrot Fractal Neural Synthesis (Dagli et al., 2026), this paper presents the Universal Fractal Natural Language Decision Map, realized via the werr machine-native edge reflex runtime and the production answerr platform (https://answerr.me). Operating entirely without stored weight tensors (0 Bytes VRAM), the en...

---

### 22. Online Automated Algorithm Design with Large Language Models

**Authors:** Zhiyao Zhang, Yichen Li, Xingyu Wu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25325v1)

**Summary:** Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimi...

---

### 23. Harness-Zero: Harness Distillation via Agent-as-Harness

**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24974v1)

**Summary:** Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time gui...

---

### 24. QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation

**Authors:** Demian Pavlyshenko, Bohdan Pavlyshenko

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24538v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24538v1)

**Summary:** Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, which constrains predictions to a predefined label set. In this work we study the the protein annotation as a sequence-to-text generation problem. We fine-tune the 3B-parameter Ministral 3 base model w...

---

### 25. DCL-GPGLS: Dynamic Curriculum Learning for Genetic Programming Guided Local Search in Large-Scale Vehicle Routing

**Authors:** Saining Liu, Yi Mei, Mengjie Zhang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24105v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24105v1)

**Summary:** Genetic Programming Guided Local Search (GPGLS) uses genetic programming to evolve utility functions for guided local search in large-scale vehicle routing problems (LSVRPs). Evaluating every GP individual on every training instance at every generation is expensive, so GPGLS is usually trained on small instance batches. Existing curriculum-based GPGLS orders these batches mainly by instance size. Adaptive Curriculum Learning GPGLS (ACL-GPGLS) improves training efficiency by adapting when the sea...

---

### 26. Genetic Programming with Behaviour-based Niching for Learning Guided Local Search in Vehicle Routing Problems

**Authors:** Saining Liu, Yi Mei, Mengjie Zhang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24104v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24104v1)

**Summary:** Genetic Programming Guided Local Search (GPGLS) learns utility functions that guide local search for vehicle routing. Its evolving programs can have similar fitness while inducing different search behaviour, making fitness alone an incomplete basis for population diversity management. We propose GPGLS with Behaviour-based Niching (BN-GPGLS), which characterises programs through six operator-level descriptors collected during local search. A current-generation archive selects fitness-competitive,...

---

### 27. Adaptive Differential Evolution and Multistart Search for Noisy QAOA Optimization

**Authors:** Vojtěch Novák, Ivan Zelinka, Swagatam Das, et al.

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.23180v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23180v1)

**Summary:** We benchmark classical optimization of a fixed low-depth Quantum Approximate Optimization Algorithm (QAOA) ansatz across four cost-Hamiltonian families at $N=12$, $p=3$, and $D=6$. Ten optimizers are compared over 25 independent runs under common ceilings of 10\,000 and 30\,000 function evaluations (FEs), first with exact statevector objectives and then with two additive observation-noise levels. Exact objectives favor multistart BFGS and multistart CMA-ES. Under noisy feedback, adaptive populat...

---

### 28. LPINNs: First-Layer Gated Localization for Physics-Informed Neural Networks

**Authors:** Lakshay Chawla, Hardik Jain

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.22984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22984v1)

**Summary:** Physics-informed neural networks (PINNs) use one shared representation over the computational domain, which can become difficult to optimize on long domains and for high-order operators. We study a minimal alternative: multiply the first hidden activation of an otherwise unchanged dense PINN by input-dependent localization functions, giving first-layer units receptive fields without partitioning the domain or adding interface losses. We screen 13 families of localization functions, in up to thre...

---

### 29. Sensing to Intelligence: Principles for Neuromorphic Circuits and Systems

**Authors:** Saptarshi Maiti, Chetan Singh Thakur

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.22838v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22838v1)

**Summary:** Neuromorphic engineering began with the idea that the physical behavior of a system could itself be used for computation, taking inspiration from the way nervous systems sense, adapt, and evolve in time. The field has since expanded far beyond its early analog circuits to include event-based sensors, spiking processors, emerging memory devices, mixed-signal systems, and large-scale neural accelerators. With this expansion, however, the meaning of neuromorphic has become increasingly broad. In th...

---

### 30. Trust-Aware Output Management for Physical Neural Network in Cloud-Continuum Systems

**Authors:** Maliheh Hariri, Stefan Fischer

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22443v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22443v1)

**Summary:** Physical Neural Networks (PNNs) introduce new opportunities for cloud continuum computing, but their outputs may be affected by noise, drift, delay, and incomplete reliability information. Existing substrate-management approaches mainly focus on discovery, invocation, and monitoring, while the reliability of the returned output is often left unaddressed. This paper proposes a trust-aware output management framework for heterogeneous PNNs. Each output is represented with quality and context infor...

---

### 31. Predictive Suppression Layers for Communication-Efficient Spiking Neural Networks

**Authors:** Aidin Attar, Michele Rossi

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21583v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21583v1)

**Summary:** Feedforward Spiking Neural Networks (SNNs) typically propagate every generated spike indiscriminately, disregarding whether the information is redundant from an information-theoretic perspective. This lack of selectivity induces high redundancy in inter-layer communication, creating an expensive overhead, e.g., in scenarios involving many-core neuromorphic hardware or communication-dominated Internet-of-Things (IoT) where features are transmitted wirelessly. To address this challenge, we trade l...

---

### 32. A Confidence-Driven Evolutionary Algorithm for Noisy Optimization with Joint Chance Constraints

**Authors:** Enrico Halim, Hemant Singh, Tapabrata Ray

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21318v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21318v1)

**Summary:** Many real-world optimization problems involve noisy objective evaluations and probabilistic constraints, particularly in the form of joint chance constraints, which are computationally expensive to evaluate. In this work, we propose CR-EA-C, a confidence-driven evolutionary algorithm for solving noisy black-box optimization problems under joint chance constraints. CR-EA-C introduces three key components: (1) analytical feasibility estimation for joint chance constraints, (2) a pairwise statistic...

---

### 33. Emergent Intelligence: Resonant Oscillators Produce Proactive Adaptive Behavior

**Authors:** Alex Fedosov, Maxim Yakimenko, Sander Stepanov

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21161v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21161v1)

**Summary:** Most artificial neural systems are built to map given inputs to outputs. Adaptive agents face a prior problem: they must act without enough evidence, seek encounters with the world, and revise behavior when evidence appears. We propose another starting point for intelligent neural networks: proactive search without signals, curiosity at its most basic. We ask whether it can come from a minimal untrained circuit. The spiking unit studied here inverts its response to input: with no signal in its w...

---

### 34. Position Paper: Neurotransmitters as a Missing Dimension in Artificial Neural Networks

**Authors:** Yupei Li, Manuel Milling, Berrak Sisman, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20083v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20083v1)

**Summary:** Artificial neural networks (ANNs), as core components of modern deep learning (DL) systems, lack the adaptive flexibility and long-term stability exhibited by biological systems. This limitation largely stems from the fact that conventional ANNs rely on uniform, local, and gradient-based parameter updates, while neglecting internal learning principles that are biological mechanisms such as neurotransmitters signalling or neuroplasticity. Consequently, many existing approaches focus on architectu...

---

### 35. Self-Replicating Neural Cellular Automata: Quantifying Emergent Phenotypic and Genotypic Diversity in an OpenEnded Substrate

**Authors:** Sanyam Jain, Felix Simon Reimers, Stefano Nichele

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19902v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19902v1)

**Summary:** We study an in-silico substrate in which every pixel of a two-channel cellular-automata grid carries a tiny neural network (an agent) that senses its Moore neighborhood. A cell persists only by self-replication: a living neighbor is cloned and its weights are mutated by a uniform perturbation, so that phenotype (cell state) is driven entirely by genotype (network weights). From a handful of seeded founders the system grows into a spatially organized ecosystem of coexisting, competing and dominat...

---

### 36. A Metaheuristic Optimization Framework for Discrete Optimization under Strict Time Limits

**Authors:** Umut Çalıkyılmaz, Nitin Nayak, Sven Groppe

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18702v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18702v1)

**Summary:** Real-time applications often rely on optimization approaches that can find high-quality solutions to hard problems on the order of milliseconds. Metaheuristic optimization frameworks (MOFs) are useful tools for such tasks, as they provide large sets of general-purpose search mechanisms that can return solutions under different computational budgets. However, existing work largely overlooks the available computation time as an explicit dimension of analysis. In this work, we introduce STILO, a MO...

---

### 37. ReDIL-GNN: Resynthesis Domain Incremental Learning for Circuit Graph Neural Networks

**Authors:** Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18595v1)

**Summary:** Logic resynthesis preserves circuit functionality while changing gate vocabulary, topology, and structural statistics, creating domain shift for circuit graph neural networks (GNNs) without changing task labels. To study this setting, we introduce ReDIL-GNN, a resynthesis domain-incremental learning framework that adapts a fixed prediction or representation head as new synthesis styles arrive and evaluates retention on all previously observed domains. Because not every shift should be adapted bl...

---

### 38. The evolution of sex for artificial intelligence: a population-genetic framework for multigenerational model populations

**Authors:** Giorgio F. Gilestro

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18560v1)

**Summary:** Some aspects of AI development resemble a population process in which models are specialised, retrained on the output of peers, or combined by averaging weights. These practices lead to generations of models, in the biological sense studied by population genetics. Here, I develop this parallelism and interpret multigenerational model populations in terms of sexual and asexual reproduction, formally recombining the two fields. I test these analogies in an exact inheritance model, in trained netwo...

---

### 39. Artificial Neural Networks as Surrogate Models in Black Box Optimization

**Authors:** Md Khadimul Islam Zim, Martin Holeňa

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.22329v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22329v1)

**Summary:** Black-Box Optimization (BBO) is often applied in several engineering fields and can utilize an advancement of numerical measure- ments and simulation technologies. It deals with the optimization func- tions, where an analytical description is unavailable. It relies on meth- ods that require only an input point in the search space, paired with its corresponding objective function value, obtained through non-analytical means, e.g., sensors, experiments, or simulations. Common approaches include ev...

---

### 40. Transformation Laws in Neural Representations: Structure, Realisability, and Construction

**Authors:** Yuan Sun

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18190v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18190v1)

**Summary:** How neural representations preserve the structure of input changes connects representation analysis with internal intervention. We study operable representational content through compatible actions of reference transformations on neural features. We characterise when a transformation descends through an encoder, and give a linear setting in which the defect is governed by the transformation's demand for discarded information, measured in the metric the representation induces. On a rectifier the ...

---

### 41. Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization

**Authors:** Lu Han, Jin Wang, Yuchen Li, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18130v1)

**Summary:** Surrogate-assisted evolutionary algorithms (SAEAs) are effective methods for solving expensive optimization problems (EOPs), where surrogate models replace most expensive evaluations and critically influence the final optimization results. In recent years, tabular foundation models have advanced rapidly, and the Tabular Prior-data Fitted Network (TabPFN) has been adopted as a surrogate model for EOPs due to its strong predictive capability, demonstrating promising performance. Motivated by its p...

---

### 42. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 43. Graph neural networks for exoplanet atmospheres

**Authors:** Antonia Vojtekova, Kai Hou Yip, Ingo P. Waldmann, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17894v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17894v1)

**Summary:** Calculating disequilibrium chemistry in exoplanet atmospheres remains a significant computational bottleneck in atmospheric retrievals. The increasing observational precision from facilities such as JWST and the Ariel mission requires including disequilibrium chemistry in these analyses. Previous studies have demonstrated that neural networks can emulate kinetic chemistry, although their spatial inductive bias does not align with the topology of chemical reaction networks. This study introduces ...

---

### 44. A Spatiotemporal Extension of the Neuromorphic DBSCAN Implementation

**Authors:** Charles P. Rizzo, James S. Plank

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17357v1)

**Summary:** DBSCAN is an algorithm that denoises and clusters data. In prior work, we implemented the DBSCAN algorithm neuromorphically, introducing two constructions termed ``flat'' and ``systolic''. The ``flat'' construction prioritizes throughput, while the ``systolic'' construction trades time for space resulting in a smaller, more hardware-friendly architecture at the cost of throughput. In this work, we offer spatiotemporal extensions of these two constructions to better leverage the spatiotemporal na...

---

### 45. Machine Zygote: Causal Biparental Heredity Before Learning in a Germline--Soma Artificial Agent

**Authors:** Lyes Saad Saoud

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17300v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17300v1)

**Summary:** Artificial ontogeny, developmental encodings, robot reproduction, and inherited controllers are established research directions, yet a narrower question remains: can a newborn artificial agent exhibit measurable biparental heredity before learning, and can that dependence be isolated causally rather than inferred only from parent-offspring resemblance? We introduce Machine Zygote, a computational germline-soma architecture designed to test this question. Two parental germlines are independently ...

---

### 46. Event-based Selective Attention for Multi-resolution Fast Region of Interest (ROI) Detection

**Authors:** Luca Peres, Giulia D'Angelo, Chiara Bartolozzi, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17134v1)

**Summary:** Neuromorphic vision systems operate under strict constraints on bandwidth, memory, and energy, particularly at the edge, motivating early mechanisms for data reduction and selective processing. In this work, we investigate a multi-scale training-free, saliency-based, bottom-up visual attention model that operates directly on low-resolution event-based input and selects Regions of Interest (ROI) from the visual scene. The model is evaluated across multiple downscaling factors applied to the incom...

---

### 47. Bio-Inspired Palette Evolution in Indirectly Encoded Substrates: Timescale Compatibility Shapes Activation Function Discovery

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17067v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17067v1)

**Summary:** Indirectly encoded neural networks can assign different activation functions to individual nodes, but the right functions are rarely known in advance. When the available set contains only standard monotonic functions, problems like parity become unsolvable, yet an all-inclusive palette underperforms a curated one. How should evolution discover which functions to use? We address this as a meta-learning problem, designing 13 strategies (11 inspired by biological adaptation mechanisms, plus baselin...

---

### 48. Neuro-Symbolic Hierarchical Intention Anticipation in Human Behavior

**Authors:** Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17064v1)

**Summary:** Assistive autonomous systems must anticipate human goals before an observed behavior is complete. This article formulates anticipation as goal inference from a partially observed multimodal episode together with structured prediction of the remaining behavior, rather than exact motor forecasting. A compact Hierarchical Planning Decoder (HPD) is attached to a frozen neuro-symbolic recognition encoder and predicts, at four ontological levels, the next actions, the remaining activities and low-leve...

---

### 49. LLMDE: A Large Language Model-Driven Differential Evolution Algorithm for Portfolio Optimization

**Authors:** Rong Chai, Vaclav Snasel, Xiaopeng Wang, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16846v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16846v1)

**Summary:** This study proposes a Large Language Model-Driven Differential Evolution (LLMDE) algorithm to reduce the reliance on handcrafted hyperparameter design. The proposed algorithm leverages a prompt engineering strategy, allowing large language models (LLMs) to dynamically select mutation strategies and configure control parameters guided by optimization feedback, thus enhancing the performance of the DE algorithm. We evaluate the performance of LLMDE on the CEC2022 benchmark suite, comparing it with...

---

### 50. Information Geometric Self-Organization at the Edge of Stability in High-Capacity Kernel Associative Memories

**Authors:** Akira Tamamori

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16827v3) | 📄 [PDF](https://arxiv.org/pdf/2609.16827v3)

**Summary:** High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit exceptional storage capabilities and robustness. Previous empirical studies identified a hyperparameter regime, the "Ridge of Optimization," where attractor stability is maximized. However, the geometric nature of this regime and the optimization dynamics required to reach it have remained unclear. In this paper, we investigate the static geometry of the parameter space and the learning trajectory of Gradient De...

---

## q-bio.NC

**50 papers**

### 1. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v1)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 2. AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets

**Authors:** Marco Rothermel, Madleen Stenger, Soroush Daftarian, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27729v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27729v1)

**Summary:** In neuropsychiatry, the primary goal is often not only to decode brain activity but to change it, for example to lessen a negative affective bias or an overly salient memory. Motivated by control theory, we develop an AI-driven neural-surrogate framework that proposes candidate representational changes and tests their predicted perceptual effects from snapshots of stimulus-evoked fMRI activity, without physical stimulation. The framework combines fMRI decoding, deep generative modeling, and cons...

---

### 3. The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity

**Authors:** Agnese Adorante, Aaron Spieler, Anna Levina

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26940v1)

**Summary:** Biological sensory neurons have selective receptive fields organized along meaningful stimulus coordinates, such as frequency, motion direction, or retinotopic position. Such structure may arise from efficient coding and biological constraints on activity, connectivity, and wiring, as computational studies of simple neurons have shown across modalities. This raises a question: do structured receptive fields confer a computational advantage beyond resource efficiency itself, and does this advanta...

---

### 4. Deep Learning in Infant Functional Neuroimaging: Challenges, Advances, and Future Directions

**Authors:** Dan Hu, Jiale Cheng, Weiran Xia, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26688v1)

**Summary:** Infancy is a critical developmental window characterized by rapid functional brain reorganization, during which large-scale networks emerge, individualized connectome signatures continue to form, and early deviations may shape long-term cognitive and clinical outcomes. Functional MRI (fMRI) offers an opportunity to study these processes in vivo, yet extracting developmentally meaningful information from it remains challenging due to comparatively short scan duration, structured motion artifacts,...

---

### 5. Physics-constrained inference of somatic dynamics from dendritic recordings with sparse somatic supervision in weakly coupled two-compartment neuron model

**Authors:** Abdeltif Oujbara, Benjamin Ambrosio, M. A. Aziz-Alaoui

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25436v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25436v1)

**Summary:** Somatic membrane potential is the primary determinant of neuronal output, yet it remains inaccessible in many experimental setups where only dendritic recordings are available. Reconstructing somatic dynamics from distal measurements is a challenging inverse problem, particularly when the soma and dendrites are weakly coupled, as dendritic signals represent a filtered and attenuated version of somatic activity. To address this, we use a physics-informed neural network (PINN) constrained by a two...

---

### 6. A theory of plasticity: capacity for change as inverse configurational constraint

**Authors:** Igor Branchi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25312v1)

**Summary:** Plasticity is invoked across the sciences to explain how systems can change, yet it is inferred from the very change it is meant to explain. A system may have many alternatives, realize none and still be plastic. Another may be driven far toward its only alternative, but the magnitude of that change does not establish its plasticity. What matters for plasticity is not how far the system moves but how strongly its present configuration constrains alternatives. Here I propose that plasticity, unde...

---

### 7. Binding-Motivated Contextuality: A Cross-Domain Cyclic Test in Perception and Judgment

**Authors:** Adam Y. Shavit

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23977v1)

**Summary:** Perceptual binding and the contextuality of judgment are studied apart, in psychophysics and decision research. We argue they share one obstruction: a nonzero class in $H^1$ of a presheaf with no global section -- though only contextuality is tested, since binding's obstruction vanishes. We build on sheaf formulations of predictive coding (Seely 2025) and contextuality (Abramsky & Brandenburger 2011): a cyclic set of pairwise judgments admits a global (noncontextual) explanation exactly when the...

---

### 8. Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery

**Authors:** Kevin Zhou, Sparsh Roy

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23924v1)

**Summary:** Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supe...

---

### 9. A discrete generative model of neuronal spiking activity on microelectrode arrays

**Authors:** Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23907v1)

**Summary:** Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a d...

---

### 10. From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture

**Authors:** Janusz A. Starzyk, Wiesław L. Galus

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23828v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23828v1)

**Summary:** This article asks under what conditions artificial intelligence could warrant a rational attribution of consciousness. Linguistic ability, multimodality, memory, planning, action control, and humanoid embodiment are not sufficient evidence of phenomenal experience. Biological precursors such as excitability, homeostasis, neural networks, and hierarchical representation instead identify functions whose counterparts may be engineered. The paper compares conventional LLMs, hybrid h-LLMs, vision-lan...

---

### 11. Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification

**Authors:** Zihan Wang, Daixin Li, Guilin Wang, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23317v1)

**Summary:** Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we...

---

### 12. BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings

**Authors:** Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora, et al.

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22064v1)

**Summary:** Advances in large-scale neural recording have made it possible to collect data across many animals and distributed brain regions, raising the question of whether this scale can be exploited to learn general-purpose neural representations transferable across diverse downstream tasks. Yet, progress toward this goal has been limited by fragmented evaluation protocols and a narrow focus on individual task domains. Here, we present BrainWideBench, a benchmark for evaluating across-animal transfer on ...

---

### 13. Identifying Neural State Changes due to Gain versus Off-Manifold Displacement

**Authors:** Sam McKenzie

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21272v1)

**Summary:** Memory segmentation is thought to arise from rapid decorrelation in neural activity, often quantified by Euclidean distance or cosine angle. Although these metrics detect a transition, they do not reveal how the new state relates to the repertoire represented by the neural manifold. This matters because neuromodulators that drive state transitions also alter excitability, and learning may repurpose existing representations or create new ones. Here, I introduce a geometric decomposition that sepa...

---

### 14. Foundation-model-based multi-label phenotyping of combined hyperkinetic movement disorders

**Authors:** Laura Cif, Zohra Souei, Diane Demailly, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.22369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22369v1)

**Summary:** Movement disorders (MDs) frequently co-occur, yet phenomenological and severity assessment shows substantial inter-rater variability. Markerless video could improve reproducibility, but prior work is largely single-symptom, depends on standardized acquisition, and lacks validation and transfer across ages and sites. We combined two foundation models into one frozen backbone: Segment Anything Model 3 (SAM 3) for dense, per-frame markerless segmentation summarized into geometric, contour and grid ...

---

### 15. A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound

**Authors:** Thomas J Stoll, Ross K Maddox

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20595v2) | 📄 [PDF](https://arxiv.org/pdf/2609.20595v2)

**Summary:** Computational models of auditory physiology commonly target specific responses or stages of the auditory pathway, limiting their ability to integrate findings across experimental paradigms and neural timescales. We present a foundation model of human auditory electrophysiology: a causal neural network trained to map binaural acoustic waveforms directly to high-sample-rate EEG. The model was trained on approximately 250 hours of EEG data from 92 subjects, with varied electrode montages and stimul...

---

### 16. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

### 17. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 18. Spike Sorting with VanillaSort

**Authors:** Zishuo Feng, Feng Cao

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.22322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22322v1)

**Summary:** Training spike detectors on real recordings is challenging because algorithmically generated labels can be noisy and incomplete. We propose VanillaSort, combining multichannel detection with spatially augmented, template-guided clustering. VanillaDet uses visibility-aware masking, truncated Gaussian targets and a temporally tolerant positive-bag loss, followed by conditional event-SNR gating. VanillaCluster combines HuiduRep embeddings with relative-amplitude features for Gaussian mixture cluste...

---

### 19. Learning Options for Compositional Motor Control with Adapter Banks

**Authors:** Sreejan Kumar, Marcelo Mattar, Lea Duncker

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17042v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17042v1)

**Summary:** Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, ...

---

### 20. Predictor Construction Can Reverse Multimodal Neural Contrasts

**Authors:** Lucas Nadolskis, Galen Pogoncheff, Michael Beyeler

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16430v1)

**Summary:** Foundation-model features are increasingly used to ask what information neural activity represents, often by comparing prediction gains between nested encoding models. We show that such multimodal contrasts can change sign when only the conditioning predictor is reconstructed. Using fMRI from the Natural Scenes Dataset, DINOv2 visual features, and MPNet embeddings of MS COCO captions and Localized Narratives, a caption-narrative contrast in the additional predictive contribution of vision favors...

---

### 21. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation

**Authors:** Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16217v1)

**Summary:** Astrocytes are non-neuronal glial cells that are receiving widespread attention due to their emerging role in neural computation. In this paper, we propose and study dynamical mechanisms by which astrocytes may augment the ability of neural networks to infer context in reinforcement learning (RL) settings. We construct a biologically inspired, two-level dynamical neural-astrocyte network with distinct spatial and temporal organization. We train this model on a hierarchical multi-context task tha...

---

### 22. Decision-Related Cognitive Signatures from Fast-Slow Dynamics: A Low-Dimensional Observation-Operator Framework

**Authors:** Furkan Emre Isik, Ali Demirci

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15918v1)

**Summary:** Repeated decisions exhibit temporal structures such as persistence, direction-dependent switching, recurrent alternation, and abrupt transitions. We examine the generative sufficiency of a two-dimensional fast-slow dynamical system. The system combines a cubic fast equation with linear slow feedback and is analyzed through its equilibrium geometry, trace-determinant structure, equilibrium-fold loci, candidate Hopf boundaries, and singular critical manifold. An explicit observation operator proje...

---

### 23. The Cross-Substrate Access Assay: What an Indicator Test Must Declare to Travel from Brain to Language Model

**Authors:** Pieter van Rooyen

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.22300v2) | 📄 [PDF](https://arxiv.org/pdf/2609.22300v2)

**Summary:** Testing an artificial system for a property linked to consciousness means applying a measurement developed on brains to a system that is not one. Such a transfer must re-examine five parts of the procedure: the competing statistical models, how they are fitted, the unit the inference generalizes over, the quantity the uncertainty interval is about, and the rule that turns a result into a verdict. The Cross-Substrate Access Assay declares all five. Because brain and model signals share no physica...

---

### 24. When Teachers Smile or Frown: A Profile-Based Analysis of Achievement Emotions

**Authors:** Rudra Mukhopadhyay, Satyaki Mazumder, Koel Das

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15747v1)

**Summary:** Achievement emotions shape how students engage with and learn from academic tasks, yet most studies examine individual emotions rather than co-occurring affective profiles and their dynamics. We examined latent achievement-emotion profiles and their transitions following exposure to different instructor facial expressions during a video lecture. Self-reported data from 78 Grade VII and VIII students revealed three profiles: enthusiastic, demotivated, and vulnerable. Profile transitions differed ...

---

### 25. Nonlinear dynamics of random neural networks with second-order synaptic motifs

**Authors:** Jun Yang, Hannah Choi

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14251v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14251v1)

**Summary:** Classical theories of random neural networks typically assume independent connectivity, overlooking the local motif structures prevalent in biological circuits. Here, we investigate how four second-order synaptic motifs (chain, reciprocal, convergent, and divergent) shape the dynamics of nonlinear firing-rate networks. While previous studies have established that chain correlations generate outlier eigenvalues, we demonstrate that these motifs also jointly reshape the Jacobian eigenvalue bulk. U...

---

### 26. URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining

**Authors:** Po-Han Chiang

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13899v1)

**Summary:** The BabyLM challenge measures how much language a model can learn from developmentally-plausible, child-scale data rather than internet-scale corpora, yet prior language models forgo the biological constraints of the neural circuitry that acquires human language: spiking neurons separated into excitatory and inhibitory populations wired by a recurrent lateral connectome. This paper presents URCHIN (Unified Recurrent Connectome with Horizontal Integrate-and-fire Neurons), which applies the Parall...

---

### 27. Hierarchical emergence of network bursting in a four-cell central pattern generator model

**Authors:** Krishna Pusuluri, Huiwen Wu, Andrey L. Shilnikov

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13858v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13858v1)

**Summary:** How can a neural circuit rhythmically burst when none of its constituent neurons can endogenously do so? We address this question through a bottom-up reconstruction of a 4-cell neural circuit modeled after the swim central pattern generator (CPG) of the sea slug \textit{Dendronotus iris}. We first map the intrinsic regimes of a swim interneuron (SiN) model neuron and show that slow mutual inhibition can generate anti-phase bursting in a half-center oscillator (HCO) assembled from tonic-spiking o...

---

### 28. Pretraining for Sample-Efficient Neural Interfaces

**Authors:** Ben Tang, Zachary Spalding, Gregory B. Cogan

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13507v1)

**Summary:** Brain-computer interfaces (BCIs) decode neural activity to restore lost function. Typically, training a high-performance neural decoder requires a large labeled dataset to be collected from every new subject. One way to reduce the labeled data cost is self-supervised pretraining, which learns general neural representations from unlabeled recordings that accumulate across subjects. However, for intracranial electroencephalography (iEEG) recordings, self-supervised learning has been challenging du...

---

### 29. Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes

**Authors:** Bilal Ahmed, Heather Cihak, Gregory Handy

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13074v1)

**Summary:** The maintenance of continuous variable information in working memory is thought to rely on persistent patterns of cortical activity. In delayed-estimation tasks, neural activity can form localized activity peaks, or ``bumps,'' whose positions track the remembered variable. Such activity is well described by continuous-attractor neural field models, but most existing models collapse cortical inhibition into a single homogeneous population. Here, we introduce a stochastic neural field model with d...

---

### 30. pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches

**Authors:** M. Marzulli, A. Angiolelli, C. Mannino, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11530v1)

**Summary:** The analysis of neuronal avalanches offers insights into brain dynamics utilizing the framework of criticality, but the reproducibility and comparability of studies are limited by the use of fragmented, lab-specific scripts. To address this issue, we introduce pyAvalanches, an open-source Python package providing a standardized, end-to-end pipeline for avalanche analysis from electrophysiological recordings (e.g., electroencephalography-EEG). Starting from the detection of neuronal avalanches th...

---

### 31. Degeneracy along the sensorimotor hierarchy: motor control within a framework larger than redundancy

**Authors:** Florent Paclet, Paul Duprat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11325v1)

**Summary:** Motor control has described the surplus of solutions available to the nervous system as redundancy, a term that names duplication: interchangeable elements, robust to loss but incapable of differential adaptation. Biology has had a second term for twenty-five years. Degeneracy names elements that are not interchangeable and are nonetheless isofunctional with respect to a given output, and it supports adaptability, since non-identical elements necessarily diverge in some context. Circuit neurosci...

---

### 32. The Platonic brain bridge hypothesis: human brain networks as an architectural prior for multimodal large language models

**Authors:** Pengfei Zhang, Biao Tian, Xiangang Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10947v2) | 📄 [PDF](https://arxiv.org/pdf/2609.10947v2)

**Summary:** Multimodal large language models predict brain activity, but brain alignment has been a measurement, not a design tool. We propose the Platonic brain bridge hypothesis: omni models, multimodal large language models that process video, audio and text jointly, converge on brain-like representations usable in both directions. From model to brain, brain-likeness of seven omni models is stable across participants, rises with every input channel in three bases, and our encoders lead the Algonauts 2025...

---

### 33. Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model

**Authors:** Daniel Semchin, Emile d'Angremont, Hao Ding, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10890v1)

**Summary:** Parkinson's disease is clinically and biologically heterogeneous, yet its spatiotemporal progression remains poorly characterized. We present a connectome-constrained disease progression model that jointly estimates subject-specific disease time and data-driven subtypes from longitudinal morphometry. Applied to 85 imaging and clinical biomarkers from the Parkinson's Progressive Markers Initiative (PPMI) cohort, the model recovers four morphologically distinct progression subtypes. We validate th...

---

### 34. Cortical information transfer reveals conserved hemispherical network dynamics across human handedness

**Authors:** Yago Emanoel Ramos, José Garcia Vivas Miranda

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10870v1)

**Summary:** Whether human motor and brain lateralization arises from fundamentally distinct neural architectures or emerges from conserved network dynamics remains a central question at the intersection of network science and neurobiology. Conventional measures of cortical activation often fail to resolve how directed information exchange adapts to manual preference during complex motor tasks. This ambiguity leaves it unclear whether left-handed individuals possess atypical neural organization or follow sha...

---

### 35. BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10518v1)

**Summary:** fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain...

---

### 36. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 37. EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding

**Authors:** Muchen Li, Anglin Liu, Xuetian Gao, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09728v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09728v1)

**Summary:** Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by s...

---

### 38. The Computational Primitives of Adaptation

**Authors:** Jonathan W. Page

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.11989v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11989v1)

**Summary:** Research on adaptive systems has traditionally focused on behavior (what organisms do) and mechanism (how their machinery works). This paper focuses on a third level, computation, which considers what adaptive systems must compute to survive and reproduce. It is proposed that adaptation has its own computational structure, comprising a small set of primitive operations common to all adaptive systems, regardless of their physical form. Six primitives, Arouse, Orient, Valence, Position, Boundary, ...

---

### 39. Emergence of criticality in models of real neurons

**Authors:** David P. Carcamo, Christopher W. Lynn

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09438v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09438v1)

**Summary:** Critical systems sit near boundaries between qualitatively distinct behaviors. When inferring models of neural activity, this proximity to criticality is thought to require the precise tuning of parameters. Here, we show that as the number of neurons increases, criticality can emerge naturally without fine-tuning. When computing observable statistics from parameters (the forward problem), some small regions in parameter space map to large regions in statistics space. These special parameters are...

---

### 40. XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

**Authors:** Yang Qiao, Junjie Wu, Deqiang Qiu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09388v1)

**Summary:** Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional co...

---

### 41. Hi-M imaging of chromatin architecture in adult Drosophila brain cryosections

**Authors:** Christel Elkhoury Youhanna, Julie Garona, Marie Schaeffer, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08776v1)

**Summary:** Hi-M combines fluorescence in situ hybridization (FISH), automated microfluidics, sequential imaging, and computational chromatin tracing to measure the three-dimensional organization of selected genomic regions in single cells. This chapter describes a Hi-M workflow adapted for cryosections of adult Drosophila melanogaster brains, enabling chromatin tracing while preserving tissue architecture and cell identity. The protocol covers Oligopaint library design and amplification, fixation, brain di...

---

### 42. Why shared attention vectors fail: a case for outcome-indexed tuning

**Authors:** Lenard Dome

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08615v1)

**Summary:** Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for ...

---

### 43. An Evidence-Aware Framework for EEG Microstate Analysis: Improved Sensitivity to Alzheimer's Disease and Ageing

**Authors:** Kaidong Wu, Haili Ye, Ptolemaios G Sarrigiannis, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08500v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08500v1)

**Summary:** Electroencephalography (EEG) microstate analysis commonly converts each scalp topography into a winner-take-all hard label and summarises the resulting sequence using duration, occurrence, coverage, transitions, and symbolic complexity. Although interpretable, this readout discards evidence strength, assignment ambiguity, and low-confidence periods. We introduce a template evidence trajectory framework that retains, at each sampled Global Field Power (GFP) peak, the evidence for all templates or...

---

### 44. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**Authors:** Xiangnan Zhang, Jingxin Liu, Ranqi Lu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08070v2) | 📄 [PDF](https://arxiv.org/pdf/2609.08070v2)

**Summary:** The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historica...

---

### 45. Fisher-Rao Distance Detects Shifts in Kinematic Profiles under Cognitive Load

**Authors:** Joseph Vero, Elizabeth B Torres

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07696v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07696v1)

**Summary:** Motor control research involves the study of movement kinematics derived from the positional trajectories that complex motions describe. In natural, unconstrained motions requiring cognitive and memory processes in real time, the temporal speed profiles are not bell-shaped, may have multiple maxima and the peaks distribution is best fit by the continuous gamma family with two parameters, the shape and the scale. As the stochastic processes described by complex motion trajectories are non-station...

---

### 46. Exploring the robustness of permutation entropy analysis to differentiate between closed-eyes and open-eyes resting states

**Authors:** Juan Gancio, Natalia López López, Antonio J. Pons, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.22265v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22265v1)

**Summary:** Electroencephalography (EEG) is a noninvasive technology that is widely used to monitor brain states, and many efforts are focused on developing reliable and efficient data analysis methods for EEG recordings. Here, we apply ordinal analysis to the EEG recording of the resting state of 109 healthy subjects measured in two different conditions: with eyes closed (EC state) or eyes open (EO state). We study the robustness of the temporal permutation entropy ($PE$) and the spatial permutation entrop...

---

### 47. Fisher Information Metric as a model-free measure of proximity to criticality in neural systems

**Authors:** Yuewei Du, Alberto Liardi, Hardik Rajpal, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07624v1)

**Summary:** Critical phenomena are widespread across many disciplines and have recently become a topic of deep interest in the study of biological and artificial neural networks. A distinct signature of criticality is the emergence of avalanches with power-law-distributed sizes and durations. However, empirically estimating the critical exponents remains challenging, and their interpretation is often model-dependent. In this work, we demonstrate how the Fisher Information Metric (FIM), a measure of generali...

---

### 48. Homeostasis Revisited and Reformulated Through Hidden Markov Model Control

**Authors:** Rubén Moreno-Bote

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07508v1)

**Summary:** A common formalization of homeostasis is the free energy principle, a framework that defines a set of desired observation values, or critical states, that the agent should reach or remain close to. Under the free energy principle, an agent should act to maximize the probability of receiving the desired observations. Here we revisit the common approach of solving the problem of maximizing the log probability of the desired observations by maximizing a variational lower bound, the so-called negati...

---

### 49. Revisiting the Aerts-Broekaert-Smets quantum model of the liar paradox

**Authors:** Massimiliano Sassoli de Bianchi

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09228v1)

**Summary:** The quantum model of the two-sentence liar paradox proposed by Aerts, Broekaert, and Smets is an early example of the use of quantum formalism to describe cognitive dynamics. Our reconstruction is primarily pedagogical in intent, but it also leads to a number of clarifications, and to some new observations, concerning the structure of the model. Rewriting the model in Dirac notation, we make explicit the distinction between truth values originating from a decision and from semantic inference, an...

---

### 50. Determinants of hyperparameter robustness in connectome reservoir computing

**Authors:** Miles Walter Churchland, Raul de Palma Aristides, Jordi Garcia-Ojalvo, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07355v1)

**Summary:** Reservoir computing provides a controlled setting for studying how recurrent network architectureshapes computation: input signals are projected into a high-dimensional state space by a fixed nonlinear dynamical system, and only the readout is trained. However, reservoir performance can be dependent on hyperparameters; this paper asks which recurrent network features support robustness to those parameter changes. We characterize computational performance using memory capacity (MC), truncated sin...

---

## stat.ML

**50 papers**

### 1. Riemannian Gradient Descent for Gaussian Mixture Models with unknown diagonal covariances

**Authors:** Romane Giard, Yohann De Castro, Roland Denis, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30220v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30220v1)

**Summary:** This paper investigates the numerical resolution of the Beurling-LASSO (BLASSO), a convex optimization framework that promotes sparsity in the space of measures. We consider its application to the estimation of Gaussian mixture models (GMMs) with an unknown number of components and unknown diagonal covariance matrices. Our approach combines the Conic Particle Gradient Descent (CPGD) principle with Riemannian gradient descent, to account for the underlying Fisher-Rao geometry of Gaussian distribu...

---

### 2. Anchored Extra-Proximal Methods: Optimal Higher-Order Methods for Monotone Inclusion Problems

**Authors:** Ruichen Jiang, TaeHo Yoon

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30212v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30212v1)

**Summary:** We study the deterministic oracle complexity of finding approximate solutions to composite monotone inclusion problems, formed by the sum of a smooth single-valued monotone operator and a maximally monotone set-valued operator, under the tangent-residual criterion. We introduce the Anchored Extra-Proximal (AEP) framework, which combines an anchored extrapolation step with an inexact anchored proximal update satisfying a relative-error condition. The framework recovers the composite Fast Extragra...

---

### 3. Intrinsic-Extrinsic Coupling in Learning Dynamics

**Authors:** Qinyou Wang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30185v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30185v1)

**Summary:** A learner's current observations need not determine its response to further training. We formulate intrinsic-extrinsic coupling through the continuation-conditioned value of a constrained learning-state intervention, with observation-relative fibers describing present agreement. An executable finite-frame classifier-head write protects current logits while repairing specified historical margins under finite-precision acceptance checks. We distinguish local admissibility, continuation-conditioned...

---

### 4. Nuclear Norm-Regularized Bayesian Matrix Completion

**Authors:** Calvin Tolbert

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30078v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30078v1)

**Summary:** Matrix completion, the problem of estimating missing entries in a matrix from noisily observed ones, underlies a diverse array of problems such as recommender systems and counterfactual outcome estimation in panel data. Many algorithms address the problem using regularized least squares, often with the nuclear norm as a regularizer, but this method yields a point estimate with no built-in uncertainty quantification. A Bayesian formulation is a natural alternative, and if the noise variance is kn...

---

### 5. Path-specific harm decomposition: A partial identification framework

**Authors:** Ruizi Yan, Dennis Frauen, Maresa Schröder, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29938v1)

**Summary:** A central goal when designing treatment policies is often to "do no harm", that is, to avoid interventions that improve average outcomes while worsening outcomes for some individuals. A widely used notion for harm is the fraction of negatively affected (FNA), defined as the probability that an intervention decreases an individual's outcome. However, in many applications, treatments operate through mediators, and a single "total" FNA can obscure whether harm arises primarily through direct pathwa...

---

### 6. Robust Detection of LLM-Generated Text under Contamination

**Authors:** Jiaxun Li, Saptarshi Chakraborty, Ambuj Tewari

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29935v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29935v1)

**Summary:** We study the detection of LLM-generated text under editing and contamination. Modeling human and machine text as finite-order Markov processes with Huber contamination, we characterize an exact boundary for reliable detection under our assumptions. Detection is impossible when contamination is sufficiently large relative to clean-source separation. Below this boundary, a collection of clipped likelihood-ratio tests achieves vanishing worst-case errors. This construction motivates clipping as a s...

---

### 7. Shrinking-Tube Concentration for Adaptive Markovian Stochastic Approximation

**Authors:** Jin Li, Ye Luo, Xiaowei Zhang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29833v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29833v1)

**Summary:** Adaptive algorithms increasingly make decisions while reshaping the dynamics that generate their future data. We establish a shrinking-tube concentration bound for projected stochastic approximation driven by an adaptive Markov chain. The bound guarantees, with high probability, that every iterate after a chosen time remains within a tolerance around the target that tightens over time. The probability of any exit after the chosen time admits a polynomially decaying upper bound, and a matching lo...

---

### 8. Boolean threshold functions, neuron capacity, and memory retrieval

**Authors:** Xinyuan Xie

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29756v1)

**Summary:** How much information can a single neuron remember? How many memories can neural networks retrieve without creating false memories? These questions are related to a basic question: how many Boolean threshold functions $f(x)=\operatorname{sgn}(a_0+\langle a,x\rangle)$, $x\in\{-1,1\}^n$, are there? In this paper, we show that the number $T_n$ of distinct Boolean threshold functions is \[ T_n=2\binom{2^n-1}{n}\bigl(1+O(n^{-99})\bigr). \] Equivalently, the capacity of a single threshold neuron is $n^...

---

### 9. Direct Message Approximation (DMA): A Consistency-Based Framework for Tractable Approximate Inference on Factor Graphs

**Authors:** Ralf Herbrich, Rainer Schlosser, Jan Lemcke, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29466v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29466v1)

**Summary:** Approximate message passing on factor graphs underlies two dominant families of probabilistic inference algorithms: expectation propagation (EP) and variational message passing (VMP). Both methods approximate the marginal at each factor edge, forcing an iterative round-robin schedule, risking negative-precision messages, and, for VMP, collapsing to point estimates at Dirac-delta factors. We introduce Direct Message Approximation (DMA), which approximates factor-to-variable messages directly rath...

---

### 10. Neural Transport Nested Sampling

**Authors:** David Yallup, Will Handley

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29413v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29413v1)

**Summary:** Sampling from Boltzmann distributions of molecular systems is an inference problem that has seen significant recent developments fuelled by advances in neural density estimation. We develop a novel sampling algorithm, Neural Transport Nested Sampling (NTNS), which combines the classical strengths of nested sampling with modern neural flow-based methods. NTNS uses a flow matching velocity as the drift in a Metropolis--Hastings corrected Langevin kernel inside a nested sampling outer loop, requiri...

---

### 11. Machine Unlearning for Gibbs Supervised Learning Algorithms

**Authors:** Yaiza Bermudez, Samir M. Perlaza, Iñaki Esnaola

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29409v1)

**Summary:** In this paper, a method for achieving exact unlearning for Gibbs supervised learning algorithms is proposed using a variational formulation inspired by empirical risk minimization subject to relative entropy regularization (ERM-RER). Such a method consists of maximizing the expected empirical risk over the dataset to be unlearned subject to a regularization by relative entropy with respect to the original algorithm. The optimization variable is a probability measure on the models; and the soluti...

---

### 12. Learning a Flow to Self-Supervised Representations

**Authors:** Yuling Jiao, Wensen Ma, Houduo Qi, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29350v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29350v1)

**Summary:** Explicit geometric references offer a direct way to structure self-supervised representations. Existing adversarial distribution-matching formulations, however, require costly encoder-critic optimization. We introduce Flow-Based Distribution Matching (FBDM), a non-adversarial framework that learns this reference-directed geometry through spherical conditional velocity regression. An ETF-inspired reference allows its number of components K' to exceed the auxiliary flow dimension d* while retainin...

---

### 13. GCUL: Ambiguity Identification in Text Emotion Classification via Cluster-Guided Learning

**Authors:** Zhongqi Fan, Tianyou Zhang, Fei Chen

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29327v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29327v1)

**Summary:** Selective classification enables a model to abstain from predictions on uncertain instances, but existing approaches typically reject them through confidence scores, predefined coverage constraints or instance-level distance measures. These approaches may overlook the collective geometric structure of difficult samples in learned representation spaces. We propose Guided Clustering-based Uncertain Learning (GCUL), a geometric-guided selective classification framework that identifies misclassified...

---

### 14. Sufficiently Reduced Distributional Regression

**Authors:** Alexander Henzi, Tiange Liu, Xinwei Shen

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29291v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29291v1)

**Summary:** We propose Sufficiently Reduced Distributional Regression (SRDR), a generative method that combines conditional distribution estimation with nonlinear sufficient dimension reduction (SDR). It builds on a characterization of sufficiency through strictly proper scoring rules: a dimension reduction is sufficient if and only if predicting the response from the reduced covariates incurs no loss in expected score relative to the full covariates. Sufficient dimension reduction thus becomes a risk minim...

---

### 15. FB-GDM: Fully-Bayesian Guided Diffusion Models for High-Dimensional Linear Inverse Problems via Unsupervised Variational Inference

**Authors:** Gatien Séguy, Thomas Rodet

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29216v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29216v1)

**Summary:** Diffusion models are powerful priors for linear inverse problems, but the reference guidance methods, Diffusion Posterior Sampling (DPS) and Pseudoinverse-Guided Diffusion Models ($Π$GDM), rely on scalar hyperparameters tuned per task, usually against the ground truth. We introduce FB-GDM, a fully-Bayesian guided diffusion method that removes this calibration step. Starting from the Gaussian approximation of $Π$GDM, we derive a closed-form conditional score that depends on two precision paramete...

---

### 16. Functional dynamic mode decomposition: Learning infinite-dimensional systems from data

**Authors:** Stefan Klus, Eirini Ioannou

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29159v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29159v1)

**Summary:** Dynamic mode decomposition (DMD) is a data-driven method that computes the best linear approximation of the underlying dynamical system and decomposes the dynamics into a superposition of characteristic spatiotemporal patterns. Originally introduced by the fluid dynamics community, DMD and its extensions have found widespread use in many other research areas such as molecular dynamics, climate science, engineering, finance, and neuroscience. Applications include dimensionality reduction, forecas...

---

### 17. Feature Space Selection and Heterogeneous Effect Estimation for Blood-Brain Barrier Permeability: A Random Forest to the Generalized Random Forest Pipeline

**Authors:** Tshemollo Rapolai, Seite Makgai, Mohammad Arashi

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29076v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29076v1)

**Summary:** Predicting blood-brain barrier (BBB) permeability is critical for central nervous system drug discovery. Using the MoleculeNet BBBP dataset (n = 2039), this study systematically ablates molecular feature spaces to isolate featurisation from model architecture. We evaluate three feature families (Morgan fingerprints, RDKit physicochemical descriptors, SMILES bigrams) across four learning algorithms. Results demonstrate that predictive performance depends jointly on feature representation and algo...

---

### 18. Transformers as Cross-Task Learners: Shared Structure Drives Sample Efficiency in In-Context Learning

**Authors:** Zhongjie Shi, Rongjie Lai, Alexander Cloninger, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29060v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29060v1)

**Summary:** Transformers achieve remarkable performance by jointly learning broad families of tasks during pretraining and adapting to unseen tasks from only a short prompt. Yet a rigorous mathematical and statistical understanding of this phenomenon remains limited. This paper aims to study how Transformers exploit shared cross-task structure and how this structure affects the sample complexity of in-context learning (ICL). Specifically, we characterize task-space complexity through covering numbers under ...

---

### 19. Personalised federated learning for Riemannian and Euclidean EEG decoding

**Authors:** Thibault Pautrel, Florent Bouchard, Ammar Mian, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29037v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29037v1)

**Summary:** Federated learning (FL) lets EEG decoders learn from recordings of several subjects without pooling them. We consider two light EEG decoders, the Riemannian SPDNet and the Euclidean EEGNet. Both split into a trunk, which builds a latent representation, and a head, which classifies it. Inter-subject variability, however, makes a single shared FL model a poor fit for each subject. Personalised FL addresses this: all subjects learn a common trunk, and each subject keeps its own head. We adapt it fo...

---

### 20. When Does Action Credit Need Updating?

**Authors:** Hongye Yang, Boxiao Huang

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29007v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29007v1)

**Summary:** Tool-using agents are continually updated with new interaction data. After each policy update, however, previously estimated action credits may become stale. Recomputing them from scratch can require many additional tool calls and environment interactions, making repeated updates increasingly expensive. We ask a simple question: when does historical action credit actually need to be updated? Our key observation is that a change in action value does not necessarily imply a change in the decision....

---

### 21. Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs for Agentic Reinforcement Learning

**Authors:** Xincheng Yao, Haobo Fu, Weiming Liu, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.28963v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28963v1)

**Summary:** Group-based reinforcement learning (RL) methods, such as GRPO and its variants, have become a leading paradigm for training reasoning and agentic large language models (LLMs). While their group-normalized advantage estimation is reliable at the response level, it becomes systematically biased at the step level, since coarse-grained trajectory-level advantages are hard to accurately reflect the contribution of individual steps (i.e, failed trajectories may contain valuable steps). Revisiting the ...

---

### 22. Selective Inference for Deep Clustering in Latent Spaces

**Authors:** Eina Mizui, Tomohiro Shiraishi, Shunichi Nishino, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28756v1)

**Summary:** Deep clustering is a powerful approach for discovering meaningful structures in high-dimensional data by learning a low-dimensional latent representation prior to clustering. Despite its empirical success, assessing the statistical reliability of the resulting clusters remains challenging. Testing discovered clusters on the same data induces selection bias and invalidates classical $p$-values. Selective inference (SI) provides a principled framework for correcting this bias, but existing methods...

---

### 23. Exact Bayes Regret and Asymptotic Optimality in High-Dimensional Gaussian Bandits

**Authors:** Prakhar Singhvi, Yi Zou, Abhishek Bhattacharjee

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28718v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28718v1)

**Summary:** We study Bayesian linear bandits with an isotropic Gaussian parameter, independent Gaussian candidate arms, and Gaussian reward noise when the horizon is proportional to the dimension. The normalized posterior uncertainty has an explicit limit that is uniform over all causal policies. Gaussian posterior identities then determine the limiting parameter overlaps without an assumed closure of the adaptive recursion. These results yield exact regret curves for Thompson sampling, posterior-mean greed...

---

### 24. RLVR landscapes for iterated multiplications can be benign: Insights from spin-glass theory

**Authors:** Noa Rubin, Zohar Ringel

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28625v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28625v1)

**Summary:** Despite the importance of reinforcement learning with verifiable rewards (RLVR), the extent to which it can learn new reasoning capabilities remains debated. Here we study the optimization landscape of RLVR on algorithmic tasks, such as iterated group and quasigroup multiplication. To this end, we map entropy-regularized RLVR over myopic tabular policies onto an energy-based (spin-glass) model over deterministic policies. This mapping upper-bounds what RLVR can achieve, and lets us rigorously ch...

---

### 25. Global Convergence of Third-Order Langevin Dynamics for Non-Convex Optimization via Simulated Annealing

**Authors:** Yingli Wang, Kelvin Shuangjian Zhang, Lingjiong Zhu

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28611v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28611v1)

**Summary:** We study global convergence guarantees of third-order Langevin dynamics for non-convex optimization via simulated annealing with fixed friction and decreasing noise. An explicit three-block distorted entropy transfers dissipation from the noisy auxiliary variable to the full state. Under dissipativity, regularity, and low-temperature functional-inequality assumptions, logarithmic cooling drives the objective values to the global minimum in probability at the barrier-controlled kinetic rate. For ...

---

### 26. Memory-Conditioned Diffusion Model for Generalized Langevin Dynamics

**Authors:** Minglei Yang, Sicheng He

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28371v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28371v1)

**Summary:** Generalized Langevin equations describe non-Markovian dynamics in which the evolution of resolved variables depends on their past. We propose a memory-conditioned diffusion method for learning stochastic flow maps of these dynamics from observed trajectories, without identifying a memory kernel or reconstructing unresolved variables. A compact, recursively updated bank of exponential filters enables the flow map to retain predictive history over multiple time scales without conditioning on long ...

---

### 27. Local Geometric Mixing via Dobrushin Contraction with Applications to Diffusion Path Monte Carlo and the Proximal Sampler

**Authors:** Stefan Oberdörster

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28338v1)

**Summary:** Local geometric mixing localizes geometric mixing by requiring geometric convergence to equilibrium in total variation only over finitely many transitions. It accommodates local convergence rates and captures rapid local equilibration, even when global mixing is much slower. We establish and discuss local geometric mixing bounds through Dobrushin contraction. We then apply this approach to Diffusion Path Monte Carlo, a recently proposed Markov chain Monte Carlo method, aimed at leveraging advanc...

---

### 28. How Sensitive Are LLM Leaderboard Claims to Hidden Model Selection?

**Authors:** Chen Yang, Xianyang Zhang, Jun Chen

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28177v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28177v1)

**Summary:** LLM leaderboard gains can reflect selection among privately evaluated model variants, yet neither the number of variants nor their dependence is public. We ask how many hidden variants a published margin can support while retaining statistical evidence of a provider's advantage over a fixed comparator. For a fixed candidate family under a Gaussian margin model, we derive a sensitivity curve that reports this maximum count as a function of a lower bound on within-family correlation. The relevant ...

---

### 29. Rank-One Signal Recovery in Sparse Wishart Noise

**Authors:** Preben Forer, Urte Adomaityte, Pierpaolo Vivo

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28163v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28163v1)

**Summary:** We study the high-dimensional recovery of a signal vector $\mathbf{x}$ in the presence of sparse Wishart-like noise. We define an $N \times N$ matrix $A = J+(θ/N)\mathbf{xx}^{\top}$, where $\mathbf{xx}^{\top}$ is the rank-one deformation of the random noise matrix $J$. We consider a Wishart-like matrix $J={X}^{\top} X$, where $X$ is a sparse $M \times N$ random matrix with entries $X_{ij} = c_{ij}W_{ij}$, with $c_{ij}$ regulating the density of non-zero elements, and $W_{ij}$ the bond weights. U...

---

### 30. NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees

**Authors:** Weiwei Ye, Hangchen Liu, Renhe Jiang

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28587v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28587v1)

**Summary:** Large language models can interpret natural lan- guage, yet robust decisions remain challenging. Jev-like models expose structured choices, but these interfaces do not directly provide numeri- cal values at a requested precision. We propose NUMERICJEV, a training-free numerical decod- ing algorithm that enables numerical output from any LLM with a Jev-like structured-choice in- terface. Surprisingly, on our arithmetic bench- mark, it outperforms direct selection from a can- didate list containin...

---

### 31. NPBoost: Neural Processes with Gradient-Boosted Fixed Effects

**Authors:** Andrea Nava, Ken Rölli, Armin Begic, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28122v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28122v1)

**Summary:** Neural Processes (NPs) are model-based meta-learners that implicitly learn a stochastic process and adapt to a new task from a small context set. Most extensions of NPs focus on improving the neural network architecture. We instead develop an extension motivated by the shared hierarchical interpretation of meta-learning and mixed-effects models. Specifically, we introduce Neural Process Boosting (NPBoost), which decomposes structured response variability into tree-boosted fixed effects shared ac...

---

### 32. SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models

**Authors:** Xin-Yu Hu, Shuang Liang, Cheng Feng, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28582v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28582v1)

**Summary:** The recent emergence of Time Series Foundation Models (TSFMs) has significantly advanced multi-step forecasting performance, enabling accurate predictions over extended future horizons. However, existing TSFMs often suffer from significantly inherent uncertainty, which typically manifests as derived forecast branches emerging at each time step and spreading to subsequent steps; different forecast branches often exhibit varying forecasting performance, thereby undermining the credibility of TSFM ...

---

### 33. Improving Ensemble Filters with Flow Matching

**Authors:** Haoyuan Chen, Alexandre Thiéry

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28015v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28015v1)

**Summary:** Data assimilation estimates a dynamical state from partial and noisy observations. Classical ensemble filters are efficient but restrict analysis updates through finite sample covariance and affine Gaussian distribution. We introduce the Flow Ensemble Filter (FlowEF), which uses conditional flow matching to transport the forecast ensemble from a classical baseline filter to an analysis ensemble. FlowEF uses a localized Gaussian source during training, transports forecast ensemble members from a ...

---

### 34. FedIncome: Federated Learning for Income Estimation in Digital Lending Under Data Sovereignty Constraints

**Authors:** Sultan Amed, Tanmay Sen, Sayantan Banerjee

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27654v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27654v1)

**Summary:** Verified income is often unavailable in digital loan applications, forcing lenders to rely on reported income and potentially leading to over-lending, overly conservative offers, or rejection of creditworthy applicants. Cross-institutional data-sharing constraints make this problem especially difficult for smaller lenders with limited training data. We introduce FedIncome, a federated learning framework for income estimation that enables institutions to train a shared model without pooling raw b...

---

### 35. Matrix Aggregation Operators

**Authors:** Inmaculada Gutiérrez, Asier Urio-Larrea, J. Tinguaro Rodríguez, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28562v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28562v1)

**Summary:** Aggregation theory has traditionally focused on operators defined over vectors. However, many applications-including Multi-Criteria Decision Making, Group Decision Making, Fuzzy Rule-Based Classification Systems, and overlap/grouping indices-require aggregating information naturally structured as a matrix of membership degrees (e.g., where a set of objects interacts with a family of fuzzy sets). Despite this, no formal framework has been proposed for this class of operators, partly due to the co...

---

### 36. Speculative Evaluation of Stochastic LLMs

**Authors:** Qianli Shen, Xiang Li, Ruomeng Ding, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28560v1)

**Summary:** Evaluating a stochastic large language model is costly: benchmark scores estimate expected performance from randomized rollouts, yet uniform repetition ignores sharp differences in task-level rollout variance. We ask how to minimize the variance of a fixed-benchmark mean under an exact rollout budget. We develop Speculative Evaluation with a Hierarchical Bayesian Neyman (HBN) policy with pilot size and stage weight jointly chosen ex ante. It runs a short uniform pilot, pools per-task success cou...

---

### 37. Robustness of Diffusion Models under Distribution Shift

**Authors:** Wei Luo, Neil K. Chada, Shijie Zhang, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27546v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27546v1)

**Summary:** Score-based diffusion models are increasingly considered in settings where the underlying data distribution may differ from the training distribution, yet existing theoretical guarantees largely focus on the no-shift setting. In this work, we study robust score estimation under Wasserstein perturbations of a reference distribution. For the Ornstein--Uhlenbeck diffusion, we show that robust estimation decomposes into two fundamental components: the statistical cost of learning the reference distr...

---

### 38. Counterfactual Constraint-Conditioned On-Policy Distillation for Multi-Constraint Instruction Following

**Authors:** Yanzhao Zheng, Yuanqiang Yu, Tianze Xu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27421v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27421v1)

**Summary:** Multi-constraint instruction following requires a model to respond to a query under many simultaneously active constraints. Even strong instruction-tuned models still routinely violate some of them. Existing approaches either augment supervision with sequence- or token-level RL rewards from external verifiers or learned graders, or use on-policy distillation (OPD) against a single full-context teacher whose probability mass becomes diluted as more constraints become simultaneously active. We pro...

---

### 39. An Order-Theoretic Characterization of Consistent Inductive Inference

**Authors:** Zhou Lu

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28551v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28551v1)

**Summary:** When can a learner make only finitely many prediction errors along every infinite sequence labeled by a fixed, unknown hypothesis? We characterize this form of consistency for arbitrary binary hypothesis classes in ZFC, without requiring a uniform mistake bound. The characterization uses a single linear order on finite realizable traces. Each trace selects its least subtrace, and the order must satisfy two conditions: conflicting traces select different subtraces, and the order is well-founded o...

---

### 40. Discrete Diffusion Models via Evolving Variational Autoregressive Networks

**Authors:** Kewen Pan, Ying Tang

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27306v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27306v1)

**Summary:** Conventional score-based diffusion models learn scores without representing normalized densities, whereas tractable normalized models support both sampling and direct likelihood evaluation. A recent tensor-network approach provides such a representation but is largely restricted to low-dimensional lattices. Here we introduce a discrete diffusion model that parameterizes normalized probability distributions using variational autoregressive networks. Explicit Markov jump operators govern the forwa...

---

### 41. Multitask Regression with Pairwise Fusion

**Authors:** Xiaodong Li, Zhentao Li

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27280v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27280v1)

**Summary:** We study multitask regression when coefficient sharing can differ by predictor. For a given predictor, many tasks may have the same coefficient while a few differ, and the exceptional tasks need not be the same for another predictor. We describe this structure by two quantities: the number of active predictors and the total number of task coefficients that differ from the most common value for their predictor. We estimate the coefficient matrix by penalizing all pairwise coefficient differences ...

---

### 42. Functional Causal Discovery via Conditional Covariance Ordering

**Authors:** Keyu Li, Ruoxu Tan

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27256v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27256v1)

**Summary:** We study causal discovery where each node is a random function. Previous studies on this topic rely on structural assumptions, e.g., linearity or non-linearity, and distributional assumptions, e.g., Gaussianity or non-Gaussianity. In contrast, we make use of covariance operators to avoid these assumptions. Under functional additive noise models, we propose a new sufficient condition to identify a valid topological ordering based on comparing norms of conditional covariance operators. Taking adva...

---

### 43. On the Sample Complexity of Active Learning with Membership Queries

**Authors:** Ganghua Wang, Shaddin Dughmi

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27241v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27241v1)

**Summary:** This work revisits a fundamental question in active learning: how powerful is the ability to synthesize arbitrary queries? Compared to pool-based active learning, where the learner only selects queries from a given unlabeled pool, we find that this seemingly mild change in query ability may dramatically alter the difficulty of statistical learning. In particular, some hypothesis classes that are inherently slow to learn in the pool-based setting, achieving only polynomial error decay in the numb...

---

### 44. Prediction with Expert Advice: Anytime Regret with Many Experts Matches the Fixed-Time Constant

**Authors:** Yang Cai, Vineet Gupta, Yanchen Jiang, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27206v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27206v1)

**Summary:** Prediction with expert advice is a fundamental problem in online learning. When the time horizon $T$ is known in advance, the minimax cumulative regret over $n$ experts is asymptotically $\sqrt{\frac{T \ln n}{2}}$. This is achieved by the Multiplicative Weights Update algorithm with a learning rate tuned to $T$, and is known to be tight. If instead the regret bound is required to hold simultaneously at every time $t$, the best known guarantee has been $\sqrt{t \ln n}$---a factor of $\sqrt{2}$ wo...

---

### 45. Artificial intelligence surrogates for treatment effect estimation with before-and-after data

**Authors:** Frances Dean, Anna Neufeld, Joshua Barrios, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27180v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27180v1)

**Summary:** Estimating the causal effects of medical treatments is difficult when clinically important outcomes are costly to measure or require long follow-up. Short-term or inexpensive surrogate outcomes offer a potential alternative, but surrogate biomarkers may be unavailable or difficult to identify. Advances in artificial intelligence (AI) have enabled increasingly accurate prediction of clinical outcomes from inexpensive, high-dimensional measurements, which creates an opportunity to use AI predictio...

---

### 46. Change detection with conformal martingales: new optimal constructions, and suboptimality of existing methods

**Authors:** Swapnaneel Bhattacharyya, Aaditya Ramdas

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27179v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27179v1)

**Summary:** We study distribution-free sequential changepoint detection for independent observations with unknown and unrestricted pre- and post-change laws. We build on the conformal test martingales and associated e-detectors of Vovk(2021), which control the probability of false alarm (PFA) and the average run length (ARL) respectively. The majority of these works focus on validity, with statistical efficiency usually left for simulations. We develop a comprehensive theory of how conformal p-values behave...

---

### 47. Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity

**Authors:** Tong Yang, Tao Jiang, Yuejie Chi, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.28543v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28543v1)

**Summary:** We analyze a simple stochastic inertial Krasnosel'skii--Mann (iKM) method for finding a fixed point of a nonexpansive operator in a real Hilbert space. Our method is obtained simply by adding two inertial extrapolations to stochastic KM [Bravo and Cominetti, 2024], and it retains one call to a possibly biased stochastic oracle per update and achieves sharp rates in both the stochastic and deterministic regimes. Specifically, with our proposed parameter schedule, we prove the following last-itera...

---

### 48. The Like Trap: Multi-Stage Poisoning against Agents in Similarity-based Recommendation Systems

**Authors:** Yue Xing, Pengfei He, Zitao Li

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.27155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27155v1)

**Summary:** With recent advancements in large language models (LLMs) and LLM-based agents, these agents are becoming increasingly autonomous and gaining broader access to act on users' behalf on the internet. However, the vulnerability of automated agents deployed on social media platforms (e.g., for managing a user's personal account) remains underexplored. Existing studies on agent poisoning typically assume that the adversary can expose poisoned content to the agent. Although such an attack is direct and...

---

### 49. WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps

**Authors:** Abbas Mammadov, Jerry Y. Huang, Justin Lin, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.27033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27033v1)

**Summary:** Reward fine-tuning aims to update a pre-trained flow-based generative model to improve the downstream reward of its generated samples. Existing methods typically formulate this problem as sampling from a reward-tilted distribution, the solution to a KL-regularized reward-maximization problem. Here, we introduce an optimal transport regularizer built directly from the pre-trained drift. Unlike KL reward tilting, the resulting objective transports individual samples toward higher reward rather tha...

---

### 50. Tight Regret Bound for Online Inverse Linear Optimization via Multiscale Matrix Weights

**Authors:** Shinsaku Sakaue

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26978v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26978v1)

**Summary:** We study online inverse linear optimization with a fixed unknown linear utility: in each round, an environment presents a compact action set, the learner recommends an action from it, and the environment returns an action that maximizes the utility over the same set. When the utility vector and the actions lie in the $d$-dimensional Euclidean unit ball, we give a randomized algorithm whose regret---the cumulative utility shortfall relative to optimal actions---is $O(\sqrt d)$ in expectation for ...

---

