# arXiv Daily Digest - 2026-09-19

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation

**Authors:** Bingxin Xu, Yuzhang Shang, Zhen Dong, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20822v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20822v1)

**Summary:** Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating ta...

---

### 2. Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision

**Authors:** Nitish Dashora, Douglas Chen, Idan Shenfeld, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20820v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20820v1)

**Summary:** Complex robotic manipulation tasks frequently require a long-term memory of past events and actions. As conditioning on full histories renders policies prone to spurious correlations and degrades performance, many approaches to policy memory involve compressing historical information through expensive VLM queries in-the-loop to process only task-salient information. In this paper, we propose an alternative approach in which computationally intensive VLM queries are made during train-time to lear...

---

### 3. FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations

**Authors:** Kevin Qu, Tao Sun, Massimiliano Viola, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20817v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20817v1)

**Summary:** Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a single observation and therefore rely heavily on learned category-level shape priors. We present FAMOS, a feed-forward model that predicts movable-part segmentation and joint parameters from a sparse, unordered set of partial point clouds. Our model jointly reasons over multiple observations and nat...

---

### 4. Paint-Anything: Unified Any-Color Control for Image Generation and Editing

**Authors:** Ji Xie, Dewei Zhou, Xinyu Huang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20816v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20816v1)

**Summary:** Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-...

---

### 5. ERCPMP-Gx: Endoscopic Image and Video Dataset for Morphological, Histopathological, and Genomic Characterization of Colorectal Polyposis

**Authors:** Zahra Ghaffari, Massih Bahar, Mojgan Forootan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20815v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20815v1)

**Summary:** Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these syndromes are essential for timely diagnosis, individualized patient management, and targeted surveillance strategies for affected families. However, public endoscopic datasets are largely organized around the individual sporadic polyp, and none links the polyposis phenotype to histopathology and ge...

---

### 6. Quantifying Overclaiming Propensity in Frontier LLM Agents

**Authors:** Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Jr Tikeng Notsawo, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20812v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20812v1)

**Summary:** Frontier coding agents are increasingly trusted to work autonomously for long periods, yet an agent's final response is often the only account of that work a user sees. We quantify the propensity of frontier agents to \emph{overclaim} task completion, a misrepresentation that can mislead the user. An agent overclaims when its final response contradicts information in its context. This definition requires no inference about intent and is independent of task success. We introduce \emph{OverclaimBe...

---

### 7. An Empirical Study of Harness Design for Coding Agents

**Authors:** Run-Ze Fan, Zihao Zhang, Simin Ma, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20804v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20804v1)

**Summary:** Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluate...

---

### 8. RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning

**Authors:** Yan Yu, Zhengxi Lu, Yizhou Liu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20784v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20784v1)

**Summary:** Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is undermined by two findings in agentic tasks: privileged information alone does not always make a teacher reliable, and the benefit of teacher supervision is stage-dependent. We theref...

---

### 9. Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations

**Authors:** Sarah Wyer, Sue Black, Noura Al Moubayed

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20779v1)

**Summary:** Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters ...

---

### 10. GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies

**Authors:** Xin Chen, Sen Chen, Yujuan Ding, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20776v1)

**Summary:** Action chunking is widely used for action generation and execution in Vision-Language-Action (VLA) policies, yet existing approaches commonly use a fixed action horizon. During a rollout, different task stages may require different levels of action continuity, control precision, and closed-loop feedback, making a fixed horizon unable to accommodate changing control requirements. We propose \textbf{GeoAAC}, a geometry-based adaptive action chunking method for flow-based VLA policies that adjusts ...

---

### 11. Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights

**Authors:** Tica Lin, Deepak Chandran, Gauri Jagatap, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20768v1)

**Summary:** Generative agents are increasingly used to select and narrate video highlights, but they typically operate over unstructured or frame-level representations. Their output is consequently difficult for a viewer to verify and steer toward individual preferences. We present the semantic action graph, a lightweight domain schema that represents a sports match as performer, action, recipient, moment, and state nodes connected by role, temporal, and outcome edges. The schema demonstrates three key prop...

---

### 12. Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation

**Authors:** Sho Kawano, Zehang Richard Li, Paul A. Parker

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20758v1)

**Summary:** Evaluating an AI system requires disaggregated assessment, as performance varies across domains such as benchmark task types or conversation types in deployed agents. Exhaustive testing is expensive, so evaluation rests on a sample of labeled units. We treat the evaluation set as a finite population and seek accurate point and interval estimates of each domain mean. Direct estimators, including prediction-powered inference (PPI), use only a domain's own labels and are imprecise where labels are ...

---

### 13. RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents

**Authors:** Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20754v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20754v1)

**Summary:** Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat support cases as static documents and overlook their multi-stage, stateful nature. We introduce RAFT (Retrieval-Augmented Framework for Troubleshooting Agents), a stateful RAG framework that abstracts each closed historical case into a directed chain of timeline entries and retrieves at the entry le...

---

### 14. Large Language Models as Falsifiers for Cyber-Physical Systems

**Authors:** Ali ArjomandBigdeli, Jiawei Zhou, Stanley Bak

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20752v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20752v1)

**Summary:** Falsification searches for counterexamples to formal specifications in cyber-physical systems (CPS). With specifications written in Signal Temporal Logic (STL), falsification can be formulated as a robustness optimization problem, traditionally tackled with black-box search algorithms. In parallel, large language models (LLMs) have recently emerged as surprisingly effective optimizers when coupled with iterative prompting. In this work, we connect these ideas and introduce LLM-Falsifier, an LLM-...

---

### 15. Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure

**Authors:** Zofia Smoleń

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20732v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20732v1)

**Summary:** Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We propose a novel framework of splitting any spreadsheet into interpretable chunks using cell role annotation. Our framework beats the state of the art, yet it faces a hard ceiling. Spreadsheets are fundamentally two-dimensional unstructured data with continuous relationships and infinite potential cell...

---

### 16. Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models

**Authors:** Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20722v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20722v1)

**Summary:** Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B a...

---

### 17. Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

**Authors:** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20715v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20715v1)

**Summary:** Agent trajectories record what an agent does and what happens next. Yet standard supervised fine-tuning (SFT) applies loss only to agent-authored action tokens, using environment observations as context but not as prediction targets. We ask whether this convention provides the best initialization for subsequent reinforcement learning. We introduce ActObs, which also supervises the observation tokens already present in each trajectory. Although deployed agents never generate observations, learnin...

---

### 18. HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface

**Authors:** Zimu Han, Yiming Zeng, Jiyao Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20659v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20659v1)

**Summary:** Large-scale vision-language-action (VLA) models provide powerful priors for robot manipulation, yet adapting them to a specific deployment remains challenging. Supervised fine-tuning (SFT) on task-specific demonstrations provides a step toward deployment, but faces two persistent limitations: static data provide limited coverage of out-of-distribution states, and standard imitation objectives do not distinguish progressing behavior from less useful data. Interactive post-training can address the...

---

### 19. Ownership in AI-Assisted Everyday Tasks

**Authors:** Megan Wei, Melanie Subbiah, Audrey Lee, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20658v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20658v1)

**Summary:** When does work done with AI still feel like ours? As AI becomes woven into everyday tasks, we must examine what happens to our sense of ownership and contribution when a machine shares in producing what we make. We report an exploratory qualitative survey in which participants were asked to describe two recent, self-selected tasks completed with AI: one that felt like their own and one that did not. We find that felt ownership depends on the process of collaboration: people disown work when they...

---

### 20. PAA: The Probabilistic Allen Algebra: A Generative and Complete Probabilistic Extension of Allen's Interval Relations

**Authors:** Julian Eggert

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20634v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20634v1)

**Summary:** Allen's interval algebra is a qualitative calculus for temporal relations, but its thirteen base relations are crisp predicates over exact interval boundaries. This is inadequate for temporal information from language, perception, databases, or uncertain histories, where times, durations, and boundaries are uncertain and expressions such as "just before" or "roughly during" have graded meaning. We develop the probabilistic Allen algebra (PAA): a generative and complete extension in which relatio...

---

### 21. Chronicle: Cut-Point Replay for Regression Testing of LLM Agents

**Authors:** Tisha Chawla, Susheem Koul

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20625v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20625v1)

**Summary:** Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundarie...

---

### 22. A Simulation Platform for AUV Fault Recovery: Exploring LLM-Based Diagnostic Strategies

**Authors:** Khalid Halba, Kylie Cooper, James G. Bellingham

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20620v1)

**Summary:** Autonomous underwater vehicles (AUVs) operating beyond reliable communications must recover from failures without human intervention. We investigate an architecture in which conventional deterministic layered control autonomy manages normal operations, while an invokable large language model (LLM) serves as a diagnostic and recovery planner when onboard anomaly detection identifies performance outside expected limits. Because language models are stochastic, rigorous evaluation requires ensemble ...

---

### 23. Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape

**Authors:** Sarah Radway, Andrew Cheng, Vijay Janapa Reddi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20614v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20614v1)

**Summary:** Frontier AI models are rapidly gaining the ability to exploit vulnerabilities in complex pieces of software. The risk is not theoretical, as evidenced by recent sandbox escapes performed by frontier models at OpenAI and Anthropic. Discussions of how to sandbox inference stack components often focus on components other than the inference engine itself (e.g., network proxies or code execution environments). However, the inference engine is an attractive target for a misaligned model. For example, ...

---

### 24. Limits of Confidence in Diffusion

**Authors:** Russ Webb, Amitis Shidani, Alice Bizeul, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20581v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20581v1)

**Summary:** Discrete diffusion, including remasking and uniform-state samplers, generate a sequence by writing multiple token positions per step, drawing each from a per-position distribution and choosing which positions to write from those same distributions. For domains of general interest (pixels, phonemes, or words) there are inherent dependencies between tokens. We show that a step matches the training distribution only when the positions it writes are conditionally independent given the tokens already...

---

### 25. Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control

**Authors:** Yilang Liu, Haoxiang You, Qian Wang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20575v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20575v1)

**Summary:** Learning visual policies for locomotion and manipulation requires coordinating contact with the environment and can incur substantial computation and GPU memory costs. First-order policy gradients (FoPG) reduce training cost through differentiable simulation, but local optimization can converge to unintended contact patterns. To address this shortfall, we propose Sampling-Guided Policy Search (SGPS), which couples recurring action-target refinement by sampling-based model-predictive control with...

---

### 26. Mitigating Retaliatory Algorithmic Collusion in Repeated Games

**Authors:** Karthik Sivachandran, Rohan Paleja

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20548v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20548v1)

**Summary:** Reinforcement learning agents trained to maximize their own reward in repeated interactions can converge to supra-competitive outcomes resembling explicit collusion, without communication or shared design. Existing mitigation approaches are largely tied to specific economic settings, like two-sided platforms and auctions, leaving open how to design interventions for general repeated games. We address this gap by formalizing the connection between empirical observations from prior work on Q-learn...

---

### 27. Language-model groups overstate consensus when replaying human deliberation on a reasoning task

**Authors:** Tengfei Shao

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20543v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20543v1)

**Summary:** Full-consensus rates are often treated as indicators of collective cognition, yet depend on how participation and final states are operationalized. We replayed 100 held-out human Wason groups with matched large language model (LLM) agent groups, seeding one belief-anchored agent per participant's pre-discussion answer and scoring agents and people with the same code. Across human scoring definitions, estimates ranged from 24.0% to 57.0%; about one fifth of participants never posted, whereas agen...

---

### 28. Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation

**Authors:** Peiying Zhu, Sidi Chang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20538v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20538v1)

**Summary:** An AI evaluation can be perfectly reproducible and still support the wrong claim. This risk is acute in closed-loop systems: policy determines visited states, observable components, and which failures leave a measurable trace. We propose a claim-safe protocol with three actions. Refuse: abstain when a clean reference stream or matched runtime comparison lacks support. Decompose: report protocol execution, operational false admission, and structural hypotheses separately rather than as one PASS/F...

---

### 29. FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned Transformer Foundation Model

**Authors:** Zaynab Raounak, Camille LHermine, Zhiguo Zeng

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20535v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20535v1)

**Summary:** Deep learning predictive maintenance models suffer from poor transferability across machines and operating conditions, especially when labelled data are scarce and signals span five orders of magnitude in sampling frequency (1 Hz to ~100 kHz). We propose FreqCondNorm, a Transformer-based architecture that introduces a FiLM-style frequency-conditioned normalization layer to unify heterogeneous time-series within a single model. The architecture is pretrained on five public predictive maintenance ...

---

### 30. SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

**Authors:** Haozhe Liu, Tian Ye, Sensen Gao, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20519v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20519v1)

**Summary:** As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvem...

---

### 31. Model-Agnostic and Language-Agnostic Voice Pipeline Improvement for the Agriculture Domain

**Authors:** Aakash Singh, Lakshmi Pedapudi, Chandrashekar M S, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20504v1)

**Summary:** FarmerChat is Digital Green's AI-powered agricultural advisory assistant for smallholder farmers, who access it in their own language through text, voice, or photographs. Voice is a critical channel for this population, yet field-recorded speech is challenging for general-purpose automatic speech recognition (ASR) because recordings frequently contain machinery noise, background media, competing speakers, and domain-specific agricultural vocabulary. These conditions disproportionately affect cro...

---

### 32. Edustories: A Collection of Real-world Case Studies from Classroom Practices

**Authors:** Michal Štefánik, Jan Nehyba, Jirina Karasova, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20484v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20484v1)

**Summary:** Despite the widely recognized potential of AI in education, most prior work has focused on individualized student assistance. In contrast, the majority of educational practice worldwide still takes place in collective classroom settings. To enable researchers to study AI assistance in collective teaching, we introduce Edustories, a dataset of 1,492 teacher-written case studies describing real elementary and high-school classroom situations involving challenging student behavior, pedagogical inte...

---

### 33. greCAPTCHA: Assessing Understanding as Evidence of Research Authorship Under Generative AI

**Authors:** Justin Payan, Bálint Gyevnár, Atoosa Kasirzadeh, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20481v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20481v1)

**Summary:** Conferences, journals, funders, schools, and universities are struggling with a surge of potentially AI-generated submissions from ostensibly human authors, who may not have exercised sufficient human oversight for their manuscripts. In turn, institutions evaluating submissions can no longer reliably credit expertise based solely on authors' names on submitted work. To address this problem, we propose greCAPTCHA, a proctored assessment approach that measures authors' understanding of research ma...

---

### 34. How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents

**Authors:** Yukun Zhang, Kemu Xu, Yishen Chen

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20474v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20474v1)

**Summary:** Agent harnesses supply planning guidance, organize execution, and check completion. We study how these components affect success, erroneous acceptance, and cost in two Retail experiments and an Airline pilot in $τ^2$-bench. The primary comparison pairs prewritten task-specific plans (Fixed) with shuffled policy text matched in word count (Sham), isolating the contribution of guidance content. Across 265 matched cells, Fixed improves oracle-verified success by 7.17 percentage points (90\% task-cl...

---

### 35. Deep Learning-Based Classification of Cognitive and Resting States Using Electroencephalography Signals

**Authors:** K. A. Januka S. Fernando, Harshit Srivastava

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20467v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20467v1)

**Summary:** The categorization of cognitive and resting states derived from electroencephalography (EEG) signals is crucial for comprehending fluctuations in brain activity linked to various mental states. EEG provides a non-intrusive approach for documenting brain function in both resting and task-oriented cognitive conditions, whilst deep learning techniques enable the automatic extraction of significant patterns from intricate EEG data. This study presents a deep learning framework to distinguish between...

---

### 36. Fingerprinting Multimodal Large Language Models

**Authors:** Chao Huang, Meng Tong, Kejiang Chen

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20457v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20457v1)

**Summary:** While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation. To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting. Inspired by recent findings tha...

---

### 37. SkillAA: Attribution-Guided Skill-Graph Updating with Targeted Validation and Rollback

**Authors:** Ziqiao Shang, Ling-Yue Ge, Lan-Zhe Guo

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20455v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20455v1)

**Summary:** External skills provide domain procedures without parameter updates, but existing methods often edit skills directly from failed rollouts without structured routing from an observed failure to an editable location; existing skill graphs also underuse semantic boundaries, object addresses, and topological dependencies for skill retrieval, targeted updating, and scoped validation. We introduce SkillAA (Skill Abductive Attribution), a structured skill-optimization framework for frozen language mode...

---

### 38. The Organization of Inference: Information, Resource Constraints, and AI Production

**Authors:** Yukun Zhang, Kemu Xu, Yishen Chen

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20449v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20449v1)

**Summary:** The economic value of inference depends on how capacity and task information are distributed across stages of AI production. We study these organizational margins using controlled workflow experiments on externally verified software-engineering tasks. In two matched resource panels, direct execution records the same success rate of 59.6 percent at logical-token ceilings of 12,000 and 24,000, while success under information-constrained planning rises from 36.2 to 51.2 percent. The planning disadv...

---

### 39. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

### 40. When Do Language-Grounded Explanations Help? A Graph-Bottleneck for Farm Monitoring Interpretable Sheep Facial Pain

**Authors:** Alam Noor, Miguel Guti'errez Gait'an

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20427v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20427v1)

**Summary:** Automated pain recognition from facial expression could make continuous welfare assessment practical in sheep, but adoption depends on trust: a stockperson cannot act on a score that arrives without justification. We ground a model in the Sheep Pain Facial Expression Scale (SPFES) by letting each detected facial region attend over text embeddings of the clinical descriptors and then test whether the resulting explanations mean anything. They do not. Ablating an entire descriptor changes the pred...

---

### 41. SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models

**Authors:** Xiaodong He, Xincheng Wang, Zhao Kang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20419v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20419v1)

**Summary:** Graph foundation models (GFMs) aim to learn transferable representations across severely heterogeneous graph domains. However, severe domain shifts in topology, graph scale, and feature semantics impede the construction of a unified, domain-agnostic representation space. To address this, we propose SCGFM-ART, a structure-centric GFM framework that aligns arbitrary graphs onto a shared relational atlas via Amortized Relational Transport (ART). The relational atlas serves as a universal coordinate...

---

### 42. TouchSight: Bare-Handed Tactile Prediction from Egocentric Video via Generative Visual Augmentation

**Authors:** Danyan Zhou, Jinxuan Lu, Jiawei Lin, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20414v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20414v1)

**Summary:** Tactile signals provide direct contact and force measurements that are essential for understanding physical interactions and enabling dexterous robotic manipulation. However, tactile sensing requires direct measurement at contact interfaces, making large-scale data collection reliant on intrusive, costly, and restrictive instrumentation. We present TouchSight, a monocular egocentric vision framework for dense full-hand contact force prediction that leverages 500 hours of pressure-glove recording...

---

### 43. Stress-testing Alignment Midtraining

**Authors:** Sid Baines, Jonathan Bostock, Maria Angelica Martinez, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20412v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20412v1)

**Summary:** When aligning frontier models through post-training techniques, it is not possible to directly demonstrate all of the behaviours we want a model to exhibit in all possible deployment environments; our model must generalise outside of the post-training distribution. One proposed solution is alignment midtraining (AMT), which continues pretraining on large volumes of alignment-relevant documents to encourage generalisation in later stages of training.   Despite the prominence of AMT as an alignmen...

---

### 44. Xeno-Interpretability: Investigating the Alien Minds of LLMs

**Authors:** F. Pierucci, M. Bracale Syrnikov, M. Prandi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20408v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20408v1)

**Summary:** Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native repr...

---

### 45. Accelerating Sharded Data Parallelism at Scale with Federated Learning

**Authors:** Gianluca Mittone, Marco Aldinucci

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20359v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20359v1)

**Summary:** The symbiotic scaling of artificial intelligence models and high-performance computing systems continually creates algorithmic challenges in their convergence. Foundation models (FMs) are a crucial example, requiring months-long training on thousands of cutting-edge GPUs. Sharded data parallelism (DP) is the dominant strategy to accelerate such computations by splitting data and models across multiple GPUs. However, it incurs prohibitive communication overhead when deployed at scale, particularl...

---

### 46. Generating Heterogeneous 3D Geological Microstructures from 2D Images via a Stable Diffusion-Adversarial Model

**Authors:** Ali Aouf, Eric Laloy, Bart Rogiers, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20358v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20358v1)

**Summary:** Characterizing the physical properties of clay and cementitious materials matters across many fields, from materials science to geological waste disposal. Property simulation typically calls for 3D imaging, which is expensive, not always accessible, and technically limited for certain materials. Recent progress in deep generative models offers a way around this, reconstructing 3D volumes from the more easily acquired 2D images.   Among GAN-based methods for 3D microstructure generation, SliceGAN...

---

### 47. A Qualitative Model for Reasoning about Path and Support

**Authors:** Abhishek Jaiswal, Zoe Falomir

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20349v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20349v1)

**Summary:** Spatial reasoning abilities correlate strongly with performance in STEM fields. Games offer a compelling medium for training these critical skills in developing children who have a natural proclivity for play. However, to facilitate human-like tutoring and player guidance, these games require an AI agent capable of making commonsense inferences from spatial events. Qualitative reasoning (QR) models appear to be a suitable framework for these application domains. As these models reason in symboli...

---

### 48. STR-Agent: An LLM-Driven Agent for QoS-Aware Routing in LEO Satellite Networks

**Authors:** Bowen Lu, Mugen Peng, Yaohua Sun, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20347v1)

**Summary:** LEO satellite networks feature dynamic topologies, time-varying links, and diverse service requirements, which make conventional routing schemes difficult to support fine-grained quality-of-service (QoS) provisioning. Existing studies mainly optimize routing over network states with predefined objectives, but rarely address the practical challenge of translating unstructured natural-language service requests into adaptive routing decisions. To bridge this gap, we propose STR-Agent, an LLM-driven...

---

### 49. Structured Four-Stage Legal Translation: From Natural-Language Traffic Rules to PROLOG

**Authors:** May Myo Zin, Wachara Fungwacharakorn, Ken Satoh, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20334v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20334v1)

**Summary:** Traffic regulations are written for human interpretation and therefore rely on shared background knowledge and flexible phrasing, which inherently introduce ambiguity, context dependence, and semantic underspecification. These linguistic characteristics conflict with the precision required by computational reasoning engines such as Prolog, which demand explicit logical structure. This study evaluates two baseline translation approaches, Natural Language to Prolog ($NL\rightarrow Prolog$) and Log...

---

### 50. NeuSOGA3D: A Neuro-Symbolic Framework for Explainable 3D Geometric Reconstruction

**Authors:** Qingde Li, Qingqi Hong, Zihan Li, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20323v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20323v1)

**Summary:** Three-dimensional reconstruction from unorganized point clouds remains a challenging problem in computer vision, geometric modeling, and computer-aided design. While neural implicit methods achieve impressive reconstruction accuracy, geometry is typically encoded in latent representations that limit interpretability and reuse within engineering workflows.   We present NeuSOGA3D (Neuro-Symbolic Geometric Abstraction in 3D), a hybrid framework that combines learned perceptual priors inherited from...

---

## cs.CL

**50 papers**

### 1. Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation

**Authors:** Bingxin Xu, Yuzhang Shang, Zhen Dong, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20822v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20822v1)

**Summary:** Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating ta...

---

### 2. Embedding Models Measure in Peculiar Ways

**Authors:** Juri Opitz, Andrianos Michail

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20821v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20821v1)

**Summary:** Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective notion of semantic equivalence and distance. We find that physical measurement is only weakly modeled in the embedding space, and that instead quite peculiar measurement patterns can be observed. Further analysis indicates that embedding representations of physical measurements are strongly influen...

---

### 3. Unifying Models of Intergroup Hostility in Online Discourse

**Authors:** Patrick Gerard, Julia Mendelsohn, Kristina Lerman

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20808v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20808v1)

**Summary:** Hostile rhetoric toward social groups can normalize exclusion and justify mistreatment, as well as contribute to rising polarization and political violence. Efforts to moderate hostile rhetoric in online speech draw on foundational theories in social and moral psychology, and political science. However, these theories were developed largely in parallel, often propose different and sometimes conflicting accounts of how hostility develops, and have rarely been tested against each other in real dis...

---

### 4. An Empirical Study of Harness Design for Coding Agents

**Authors:** Run-Ze Fan, Zihao Zhang, Simin Ma, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20804v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20804v1)

**Summary:** Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluate...

---

### 5. JEPA-Anything: Learning Predictive Models across Different Worlds

**Authors:** Taoyong Cui, Zhongyao Wang, Xinyue Xu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20800v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20800v1)

**Summary:** World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction. Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems? We introduce JEPA-Anything, a domain-agnostic framework based on orthogonal predictive factorization (OPF). Extending joint-embedding predictive architectures, OPF decomposes latent targets into complementary factors, learns them through dedicated pa...

---

### 6. RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning

**Authors:** Yan Yu, Zhengxi Lu, Yizhou Liu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20784v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20784v1)

**Summary:** Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is undermined by two findings in agentic tasks: privileged information alone does not always make a teacher reliable, and the benefit of teacher supervision is stage-dependent. We theref...

---

### 7. Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations

**Authors:** Sarah Wyer, Sue Black, Noura Al Moubayed

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20779v1)

**Summary:** Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters ...

---

### 8. dQwen3.5: Hybrid-Attention Diffusion Language Models

**Authors:** Anton Xue, Litu Rout, Aditya Akella, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20751v1)

**Summary:** Adapting a pretrained autoregressive (AR) model is a cost-efficient route to a diffusion language model (DLM). While nearly all such adaptations start from a full-attention transformer, AR modeling has shifted toward hybrid architectures that interleave attention and RNN layers. This creates an obstacle for adaptation: unlike attention, RNNs are structurally causal and nontrivial to bidirectionalize. Despite this mismatch, we investigate whether such backbones can become effective DLMs by adapti...

---

### 9. On-Demand Attention: Language Models Know When to Recall

**Authors:** Haibo Feng, Ruiqi Liang, Hanyang Peng, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20734v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20734v1)

**Summary:** Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, regardless of its benefit to the next prediction. We show that a pretrained model's decoding states already contain information predictive of this benefit, before the global read. Building on this finding, we introduce On-Demand Attention (ODA), a local-first decoding method that uses a lightweight recall head to selectively invoke global atte...

---

### 10. Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

**Authors:** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20715v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20715v1)

**Summary:** Agent trajectories record what an agent does and what happens next. Yet standard supervised fine-tuning (SFT) applies loss only to agent-authored action tokens, using environment observations as context but not as prediction targets. We ask whether this convention provides the best initialization for subsequent reinforcement learning. We introduce ActObs, which also supervises the observation tokens already present in each trajectory. Although deployed agents never generate observations, learnin...

---

### 11. Summarization Bias: The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models --- A Conceptual Framework and Registered Test Protocol

**Authors:** Levent Bulut

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20712v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20712v1)

**Summary:** This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as the reconstructable inferential structure that produces it. Within the Bulut Doctrine, narrative effect is theorized along a told-shown axis: in told mode, emotional and informational content is declared explicitly and requires little reader reconstruction; in shown mode, that content is suppressed ...

---

### 12. HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding of Women's Health Communication

**Authors:** Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20684v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20684v1)

**Summary:** Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We introduce HerHealthEval, a controlled evaluation framework for multilingual understanding of women's-health communication. For each clinical case, HerHealthEval provides matched versions in English, French, and Modern Standard Arabic using six communicative forms: canonical, clinical, layperson, indirect...

---

### 13. PAA: The Probabilistic Allen Algebra: A Generative and Complete Probabilistic Extension of Allen's Interval Relations

**Authors:** Julian Eggert

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20634v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20634v1)

**Summary:** Allen's interval algebra is a qualitative calculus for temporal relations, but its thirteen base relations are crisp predicates over exact interval boundaries. This is inadequate for temporal information from language, perception, databases, or uncertain histories, where times, durations, and boundaries are uncertain and expressions such as "just before" or "roughly during" have graded meaning. We develop the probabilistic Allen algebra (PAA): a generative and complete extension in which relatio...

---

### 14. UniPolicy: Unified Objective-Specific Policies for Generative Search Advertising

**Authors:** Kun Yao, Yuhang Zhou, Yichi Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20630v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20630v1)

**Summary:** Search advertising connects user intent with commercial content and plays a critical role in platform monetization. Recent systems typically align pretrained generative models with a single business reward, such as eCPM, or use naive reward fusion for preliminary multi-objective alignment. However, an ideal search advertising system must jointly account for heterogeneous objectives, including relevance, click propensity, and commercial value, to balance user experience and business value while m...

---

### 15. Chronicle: Cut-Point Replay for Regression Testing of LLM Agents

**Authors:** Tisha Chawla, Susheem Koul

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20625v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20625v1)

**Summary:** Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundarie...

---

### 16. What Does Privileged Information Add to On-Policy Self-Distillation?

**Authors:** XiuYu Zhang, Wei Chow, Junfeng Fang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20612v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20612v1)

**Summary:** On-policy self-distillation (OPSD) lets a language model learn from a frozen copy of itself that sees an answer or a worked solution. Giving the teacher this extra information seems to offer the student more to learn, but how much does it add beyond distillation itself? To isolate that contribution, we construct AMPLE-Math, a reusable suite of 5,319 mathematical problems with six reasoning views that share the same answer, and compare each view with matched reference-free distillation. With a th...

---

### 17. WiC is Not WSD: A Study on LLMs and Lexical Ambiguity Resolution

**Authors:** Yi Zhou, Kiamehr Rezaee, Danushka Bollegala, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20593v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20593v1)

**Summary:** Word-in-Context (WiC) remains challenging for language models, despite recent progress on lexical-semantic tasks. We hypothesise that this difficulty arises not only from comparing two contextual uses of a word, but also from the absence of an explicit sense inventory that specifies the relevant level of semantic granularity. We evaluate open LLMs on WiC and traditional Word Sense Disambiguation (WSD) under similar settings. We find that providing candidate senses, similar to what is done in tra...

---

### 18. SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk Assessment

**Authors:** Chenxi Wu, Zimu Wang, Haiyang Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20584v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20584v1)

**Summary:** Large language models (LLMs) are increasingly considered for safety-critical engineering, yet their reliability in regulated functional-safety workflows remains underexplored. We introduce SAFARI (Safety-Aware Functional Automotive Risk Inference), the first industrial benchmark for LLM-assisted automotive Hazard Analysis and Risk Assessment (HARA) under ISO 26262. It contains 3,000 de-identified industrial HARA cases and evaluates two coupled tasks: open-ended hazard analysis and standards-grou...

---

### 19. Steering the Compass: Aligning Dynamic Psychological Counseling Conversations with Cognitive Behavioral Therapy Strategies

**Authors:** Zimu Wang, Yiwen Jiang, Xiangyu Zhao, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20565v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20565v1)

**Summary:** Recent advancements in large language models have revolutionized the field of psychological counseling, especially in the context of Cognitive Behavioral Therapy (CBT). While the success of CBT relies heavily on dynamic decision-making informed by the client's real-time mental state, this aspect has often been overlooked in current research, limiting both flexibility and therapeutic outcomes. In this paper, we introduce StratCBT, a dataset specifically designed for psychological counseling conve...

---

### 20. Language-model groups overstate consensus when replaying human deliberation on a reasoning task

**Authors:** Tengfei Shao

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20543v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20543v1)

**Summary:** Full-consensus rates are often treated as indicators of collective cognition, yet depend on how participation and final states are operationalized. We replayed 100 held-out human Wason groups with matched large language model (LLM) agent groups, seeding one belief-anchored agent per participant's pre-discussion answer and scoring agents and people with the same code. Across human scoring definitions, estimates ranged from 24.0% to 57.0%; about one fifth of participants never posted, whereas agen...

---

### 21. An Analysis of Training-Free Self-Reported Confidence in Language Models

**Authors:** Lukas Meyer, Sofia Rossi, Wei Chen, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20541v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20541v1)

**Summary:** Large language models can report a numerical confidence together with generated content, but it is unclear whether this report is more than calibrated rhetoric. We analyze three training-free signals: confidence verbalized with the answer, post-hoc $P(\mathrm{True})$, and agreement with three additional generations on the same 100 TriviaQA questions for two model families. Direct verbalization is a surprisingly strong baseline: after auditing benchmark errors, it reaches AUROC 0.956 and 0.937 fo...

---

### 22. Relational Attention for Data-Efficient Language Modeling

**Authors:** Adrian Brasoveanu, Ece Takmaz, Jakub Dotlačil

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20530v1)

**Summary:** We present Relational BabyLM, a system submission to the BabyLM 2026 challenge that combines two cognitively motivated inductive biases in a single decoder-only Transformer. Architecturally, we replace standard self-attention with a Dual Attention Transformer (DAT), which separates the routing of object-level ("sensory") lexical features from structural/relational information (Altabaa and Lafferty, 2025; Altabaa et al., 2024; Webb et al., 2024; Kerg et al., 2022; Webb et al., 2021). Relational a...

---

### 23. Model-Agnostic and Language-Agnostic Voice Pipeline Improvement for the Agriculture Domain

**Authors:** Aakash Singh, Lakshmi Pedapudi, Chandrashekar M S, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20504v1)

**Summary:** FarmerChat is Digital Green's AI-powered agricultural advisory assistant for smallholder farmers, who access it in their own language through text, voice, or photographs. Voice is a critical channel for this population, yet field-recorded speech is challenging for general-purpose automatic speech recognition (ASR) because recordings frequently contain machinery noise, background media, competing speakers, and domain-specific agricultural vocabulary. These conditions disproportionately affect cro...

---

### 24. Edustories: A Collection of Real-world Case Studies from Classroom Practices

**Authors:** Michal Štefánik, Jan Nehyba, Jirina Karasova, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20484v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20484v1)

**Summary:** Despite the widely recognized potential of AI in education, most prior work has focused on individualized student assistance. In contrast, the majority of educational practice worldwide still takes place in collective classroom settings. To enable researchers to study AI assistance in collective teaching, we introduce Edustories, a dataset of 1,492 teacher-written case studies describing real elementary and high-school classroom situations involving challenging student behavior, pedagogical inte...

---

### 25. Stress-testing Alignment Midtraining

**Authors:** Sid Baines, Jonathan Bostock, Maria Angelica Martinez, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20412v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20412v1)

**Summary:** When aligning frontier models through post-training techniques, it is not possible to directly demonstrate all of the behaviours we want a model to exhibit in all possible deployment environments; our model must generalise outside of the post-training distribution. One proposed solution is alignment midtraining (AMT), which continues pretraining on large volumes of alignment-relevant documents to encourage generalisation in later stages of training.   Despite the prominence of AMT as an alignmen...

---

### 26. Xeno-Interpretability: Investigating the Alien Minds of LLMs

**Authors:** F. Pierucci, M. Bracale Syrnikov, M. Prandi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20408v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20408v1)

**Summary:** Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native repr...

---

### 27. Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base Question Answering

**Authors:** Guangze Gao, Zixuan Li, Sikui Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20398v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20398v1)

**Summary:** Semantic parsing (SP)-based knowledge base question answering aims to answer natural language questions by generating executable logical forms (LFs) over knowledge bases (KBs). When applying Large Language Models (LLMs) to this task, a key challenge over large, heterogeneous KBs is selecting question-related schema elements (i.e., relations and classes) and composing them into complex LFs. Recent LLM-based methods often make early discrete commitments to schema elements during intermediate reaso...

---

### 28. To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals

**Authors:** Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20186v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20186v1)

**Summary:** Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying. Neural drafts (e.g., EAGLE3) provide robust performance across diverse text settings, while copy-based methods achieve higher speedups in copy-intensive regimes by generating candidates faster and exploiting long repetition spans for near-perfect speculation. We analyze existin...

---

### 29. Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration for Text Reranking

**Authors:** Lijun Liu, Zhengzong Chen, Wenyan Li, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20131v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20131v1)

**Summary:** Reasoning-based reranking with Large Language Models (LLMs) has shown promising improvements in text ranking. However, current methods predominantly rely on a single reasoning trajectory, resulting in rankings that are susceptible to reasoning errors and inherently constrained in modeling the multifaceted signals underlying document relevance. To resolve this dilemma, we propose MERIT-Rank(Multi-perspective Evidence and Reasoning Integration for Text Reranking), a framework that models complemen...

---

### 30. Design of the IBM Granite 5.0 TurboCTC ASR Model

**Authors:** Brian Kingsbury, George Saon, Masayuki Suzuki, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20104v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20104v1)

**Summary:** We describe the architecture, training methodology and inference speedups of Granite 5.0 Turbo CTC, a 470 million parameter encoder-only model with an excellent speed-accuracy tradeoff. The architecture uses pyramidal temporal subsampling within Conformer blocks using strided depthwise convolutions, block-diagonal (chunk-wise) self-attention, and conditioning on intermediate predictions from the middle layer. Training highlights are the use of only publicly available data, the novel use of a Muo...

---

### 31. MATCH: Model-Aware Tool Learning with Curriculum Scheduling and Hierarchically Gated Rewards

**Authors:** Shihao Liu, Hao Yin, Lijun Liu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20082v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20082v1)

**Summary:** Tool learning enables large language models (LLMs) to use external tools for tasks beyond parametric knowledge. Reinforcement learning can optimize tool-call behavior from feedback, but current methods still face two problems: fixed-threshold curricula can become misaligned with the policy's evolving capability boundary, and additive rewards can leak argument-level credit when the predicted tool is wrong. To address these problems, we propose MATCH, a closed-loop framework for model-aware tool l...

---

### 32. Reading Emotions in the Token Space: Discriminative Adaptation of SpeechLLMs for Emotion Recognition

**Authors:** Hasindri Watawana, Sergio Burdisso, Esaú Villatoro-Tello, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20081v1)

**Summary:** SpeechLLMs have shown strong potential for emotion recognition, yet they read the predicted emotion off a generative decoder not suited for classification: it can emit labels outside the target set and favors frequent classes. We propose a discriminative adaptation that reads the final prompt token's hidden state through a classification head, producing a label in one forward pass without modifying the backbone. Because this readout starts from the hidden state the model would otherwise decode, ...

---

### 33. Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference

**Authors:** Caroline Gans Combe

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20068v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20068v1)

**Summary:** This paper builds a theoretical bridge between the economic notion of marginal utility and two machine-learning constructs, matrix factorization and the Key--Value cache of transformer language models. The singular value spectrum of a rating matrix is shown to be a diminishing marginal utility schedule for latent factors, the eigenvalue spectrum of the projected covariance operator to be the marginal utility schedule of a model's learned representation, and cache eviction and low-rank cache comp...

---

### 34. AI Should Facilitate Democratic Deliberation at Scale

**Authors:** José Ramón Enríquez, Jiaxin Pei, Alex Pentland

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20059v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20059v1)

**Summary:** AI systems can strengthen democracy by supporting deliberation at scale by addressing cognitive, social, platform-design, and market-driven frictions, while preserving human agency. Unlike proposals such as liquid democracy that restructure representation through vote delegation, in this position paper, we argue that AI-assisted deliberation offers a more promising path by lowering barriers to meaningful engagement without substituting machine judgment for human choice. Drawing on evidence from ...

---

### 35. The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents

**Authors:** Zhexi Feng, Ruiyi Zhang, Yongbo Yang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20050v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20050v1)

**Summary:** A coding agent halfway through an issue has already read much of what a retriever ranks highest. Relevance is scored per passage, but sufficiency belongs to the set: a ranker can fill its budget with variants of one required fact and leave the decision unsupported. We formulate state-conditioned minimal sufficient evidence recovery: given a captured agent state, recover a compact evidence combination that supplies the support its next decision still lacks. SERBench measures this on 500 held-out ...

---

### 36. Geopolitical Divisions Across Languages in Large Language Models

**Authors:** Maxim Chupilkin

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20005v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20005v1)

**Summary:** People increasingly turn to AI chatbots for news and explanations of world events. But do they receive the same political answers when they ask in different languages? Here we show that the language of a question can change how the same AI systems assess the war in Ukraine. We ask GPT, Claude and Gemini to evaluate twenty statements about the war in 112 languages, collecting 67,200 responses. The balance between Russia-leaning and Ukraine-leaning responses differs across languages. When we group...

---

### 37. Benchmarking LLM Compliance with China AI Generated Content Regulations

**Authors:** Chenrui Cui, Hongye Fang, Lisha Song, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19989v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19989v1)

**Summary:** The widespread adoption of LLMs has led to escalating content compliance risks. Prior works have contributed to addressing these risks in the English context, downplaying the complexity of Chinese language content. This paper follows China's current AI-Generated content compliance requirements and provides evaluation results on 20 notable LLMs, offering insight into China's regulatory landscape. We design a novel framework to assess the compliance and refusal rates with 2303 questions spanning s...

---

### 38. DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression

**Authors:**  DeepSeek-AI,  :, Anyi Xu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19969v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19969v1)

**Summary:** The widespread adoption of long-horizon agents has made model workloads increasingly input-heavy. Although prior work has substantially reduced the cost of long-context computation, prefill remains computationally expensive, and large KV caches continue to strain HBM and SSD capacity and data-transfer bandwidth. Together, these compute, storage, and bandwidth demands constitute the primary bottleneck to further lowering deployment costs. To address this challenge, we introduce DeepSeek-V4.1-Flas...

---

### 39. Before the Arrest: Benchmarking LLMs on Criminal Profiling from Incomplete Evidence

**Authors:** Yutong Yao, Yanjie Cao, Guanhua Chen, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19965v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19965v1)

**Summary:** Large Language Models (LLMs) are increasingly applied to legal and criminal justice tasks, yet existing work focuses almost exclusively on post-arrest scenarios where the suspect's identity is already known, leaving the critical pre-arrest challenge of inferring suspect characteristics from incomplete evidence largely unexplored. To fill this gap, we introduce the Profiling, Investigation, and Judgment (PIJ), comprising 2,500 real homicide cases from five countries. PIJ evaluates LLMs across thr...

---

### 40. Intrinsic Sequence-Likelihood Confidence in Retrieval-Dominated Extractive QA: Two Pre-Specified Negatives, and What They Do and Do Not Attribute

**Authors:** Gunwoo Lee, Changmin Sung, Sang-Hwan Gwak, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19942v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19942v1)

**Summary:** In extractive document question answering whose questions were generated from the passages that contain their answers -- so that retrieval recovers 92-99.8% of what any mode combination could reach, whatever its absolute accuracy -- confidence-driven mechanisms have little to gain. Fine-tuning an open language model on a specialized domain corpus yields a model whose own confidence is a tempting control signal: it could decide which queries warrant further adaptation, and which answers to trust....

---

### 41. KoNeoBench: A Curated Evaluation Dataset for LLM Understanding of Korean Neologisms

**Authors:** Soha Lee, Soojin Lee, Heesung Yang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19916v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19916v1)

**Summary:** Large language models (LLMs) are typically evaluated on static benchmarks, even though natural language constantly evolves through newly emerging words and meanings. Existing Korean benchmarks are centered on established vocabulary and therefore provide limited coverage of such recent lexical change, and their English-oriented design makes it difficult to assess the typological properties of Korean, in which content words combine productively with functional morphemes. In this paper, we introduc...

---

### 42. Generalization through Lexical Abstraction in Transformer Models: The Case of Functional Words

**Authors:** Giuseppe Samo, Vivi Nastase, Paola Merlo

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19887v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19887v1)

**Summary:** Pronouns, adverbs and other functional words (such as they, her, somewhere, there) are often used in language to replace concrete nouns or phrases, when their properties - such as gender, grammatical number - provide sufficient information for the given context. Do pretrained transformer models encode such functional words in a manner that allows them to be used like humans do? Can language models recognize the syntactic and semantic parallelism of sentences such as "The researchers wrote the pa...

---

### 43. Evaluating Communicative Success in Machine-Translated Conversation

**Authors:** Faiz Ghifari Haznitrama, Alice Oh

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19885v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19885v1)

**Summary:** Interpreter agents built on machine translation (MT) increasingly mediate live conversation between people who do not share a language, yet we still evaluate them with metrics built for isolated sentences, which measure fidelity rather than whether communication succeeds. We introduce a reusable three-layer checklist-and-judge framework that evaluates interpreter-mediated conversation across semantic, pragmatic, and cultural-social dimensions, covering the naturalness, intent, and social appropr...

---

### 44. PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces

**Authors:** Pyrros Koussios, Benjamin Jäger, John Hua Yao, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19883v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19883v1)

**Summary:** Characterizing LLM reasoning remains an open challenge, as many existing benchmarks isolate specific reasoning skills, rely on external knowledge, or are costly to extend. We introduce PetriBench, a compact, fully self-contained, and scalable benchmark for evaluating LLM reasoning over dynamic state spaces using Petri nets, a mature formalism for modeling real-world concurrent and distributed systems. PetriBench organizes reasoning into four task families varying by scope and temporal horizon, w...

---

### 45. D-Quant: Driftable Entropy Coding for KV Cache Quantization

**Authors:** Yi Su, Hong Liu, Guanghua Yu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19880v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19880v1)

**Summary:** The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bi...

---

### 46. VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering

**Authors:** Bhavana Akkiraju, Ravi Sastry Kolluru, Sri Charan D, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19879v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19879v1)

**Summary:** Question answering has advanced rapidly with large language models, but predominantly for high-resource languages, in both text and spoken settings. Spoken question answering (SQA) benchmark for Telugu remains unexplored, and the reliability of automatic evaluation in this setting remains unquantified. We introduce VākQA, a Telugu SQA benchmark of 2,001 factoid question-answer pairs across six domains, with 2.53 hours of speech audio, bilingual transcriptions, and human-verified reference answer...

---

### 47. Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning

**Authors:** Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19878v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19878v1)

**Summary:** Multimodal reasoning requires models to draw on information from multiple modalities throughout the reasoning process. Yet existing methods often concatenate modality-specific thought tokens in a single sequence, leaving the model to bridge representational differences as it reasons across modalities. We introduce Uni-LaDiR (Unified Latent Diffusion Reasoner), a framework that brings these thoughts into a shared latent space for reasoning. A unified encoder maps teacher reasoning steps from diff...

---

### 48. JustMem: Just-Enough Memory Access for Long-Term Conversations

**Authors:** Guanhua Chen, Yanting Wang, Wenjing Zhi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19877v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19877v1)

**Summary:** Efficient long-term conversational memory requires retrieving sufficient evidence without indiscriminately expanding the context presented to the language model. This is challenging because relevant evidence may be distributed across multiple sessions, while compression may discard details needed for answering. Different queries therefore require different forms of memory access. To capture these demands, we formulate memory access along two dimensions: discovery breadth, which controls how broa...

---

### 49. Zarya: A Hybrid Autoregressive--Masked Diffusion Language Model with Flexible Training and Dual-Mode Inference

**Authors:** Leonid Sinev, Ilya Koziev, Vladislav Leshchuk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19868v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19868v1)

**Summary:** Autoregressive language models (ARMs) are constrained by sequential, left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but suffer from high computational overhead due to the inability to reuse Key-Value (KV) cache and from incoherent generation arising from learning dependencies over an intractable space of token combinations. We introduce Zarya, a family of hybrid language models that jointly optimizes an autoregressive (AR) objective and a masked-diffusion...

---

### 50. Reproducibility is not construct validity: LLM measurement of institutionally situated communication

**Authors:** Veronika Batzdorfer, Carlo Romano Marcello Alessandro Santagiustina

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19866v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19866v1)

**Summary:** High annotation reproducibility does not necessarily imply that an LLM-inferred measure captures the construct it is intended to measure. We test this distinction using a dataset from the European Commission's AI Act consultation, linking structured survey responses to free-text consultation submissions from the same stakeholders. LLM annotations of consultation submissions are highly reproducible (intraclass correlations > 0.99), yet show limited convergence with survey-reported measures of the...

---

## cs.CV

**50 papers**

### 1. Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation

**Authors:** Bingxin Xu, Yuzhang Shang, Zhen Dong, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20822v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20822v1)

**Summary:** Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating ta...

---

### 2. Can 4D Foundation Models Remember?

**Authors:** Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20819v1)

**Summary:** Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstruction models, can perceive and reconstruct dynamic environments, but how well they remember what they have perceived remains an open question. Existing benchmarks largely rely on pixel-level metrics and lack ground truth for objects once they leave the field of view, making them unable to evaluate visu...

---

### 3. SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos

**Authors:** Peiyu Liu, Dingxi Zhang, Federico Tombari, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20818v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20818v1)

**Summary:** A splash lives for a fraction of a second: sheets tear into ligaments and droplets, appearance is view-dependent and nearly textureless, and little persists long enough to track. Reconstruction research has consequently focused on smoke, synthetic liquids, or gently deforming surfaces. To our knowledge, no synchronized multi-view dataset of splashing liquids exists. We therefore introduce a benchmark of 20 real scenes, from coherent streams to violent splashes, captured by seven synchronized, ca...

---

### 4. FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations

**Authors:** Kevin Qu, Tao Sun, Massimiliano Viola, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20817v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20817v1)

**Summary:** Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a single observation and therefore rely heavily on learned category-level shape priors. We present FAMOS, a feed-forward model that predicts movable-part segmentation and joint parameters from a sparse, unordered set of partial point clouds. Our model jointly reasons over multiple observations and nat...

---

### 5. Paint-Anything: Unified Any-Color Control for Image Generation and Editing

**Authors:** Ji Xie, Dewei Zhou, Xinyu Huang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20816v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20816v1)

**Summary:** Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-...

---

### 6. ERCPMP-Gx: Endoscopic Image and Video Dataset for Morphological, Histopathological, and Genomic Characterization of Colorectal Polyposis

**Authors:** Zahra Ghaffari, Massih Bahar, Mojgan Forootan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20815v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20815v1)

**Summary:** Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these syndromes are essential for timely diagnosis, individualized patient management, and targeted surveillance strategies for affected families. However, public endoscopic datasets are largely organized around the individual sporadic polyp, and none links the polyposis phenotype to histopathology and ge...

---

### 7. FlowSGS: Improving Flow Matching Priors for Inverse Imaging with Stochastic Interpolants

**Authors:** Tianao Li, Xinhui Qian, Emma Alexander

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20769v1)

**Summary:** Flow matching has emerged as the state-of-the-art generative model and has been used for plug-and-play (PnP) priors to solve inverse problems in computational imaging. However, existing flow-based inverse solvers assume linear forward models and/or make simplifying approximations in posterior sampling. To circumvent these problems, we introduce FlowSGS, a flow-based posterior sampling method using Split Gibbs Sampling (SGS) to decompose the posterior into a likelihood step and a prior step. Spec...

---

### 8. OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher

**Authors:** Damiano Da Col, Maximilian Igl, Peter Karkus, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20756v1)

**Summary:** As scaling pre-training data alone yields diminishing returns, post-training is becoming increasingly important across physical AI domains such as autonomous driving. End-to-end driving policies are pre-trained in open loop with behavior cloning on human demonstrations. However, compounding errors during closed-loop deployment can take the vehicle outside the training data distribution, increasing the risk of safety-critical incidents. Closed-loop post-training can mitigate this risk but require...

---

### 9. Should This Case Be Adapted? Prediction Fragmentation Controls Test-Time Adaptation

**Authors:** Lili Wang, Jing Li, Xiaowen Sun, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20700v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20700v1)

**Summary:** Episodic test-time adaptation resets a frozen segmenter to source weights $M_0$ on each case and adapts for a fixed step count. A fixed horizon conflates a cohort-level question, how far to adapt, with an irreducibly per-case one, whether this case should be adapted at all. Cohort means hide that decision: on cross-vendor cardiac MRI the mean $Δ$Dice from adaptation is statistically indistinguishable from zero while 58.7% of cases are individually made worse. We quantify this harm as harmful acc...

---

### 10. Towards Scaling Marine Perception with Synthetic Data

**Authors:** Haoyu Ma, Onur Bagoren, Anja Sheppard, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20680v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20680v1)

**Summary:** Scalable machine learning in challenging underwater environments is strongly limited by the lack of labeled real-world training data. This data is often expensive and laborious to gather, making large-scale real-world data challenging to gather and curate. However, simulated data can help close the gap, enabling many learning-based tasks for underwater perception. In this work, we extend OceanSim, an IsaacSim-based underwater perception simulator, with a Synthetic Data Generation (SDG) pipeline ...

---

### 11. FunArt: Decoding Functional Structure and Articulation from Generative 3D Latents

**Authors:** Dennis Rotondi, Abdelrhman Werby, Kai O. Arras

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20673v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20673v1)

**Summary:** To operate effectively in human environments, robots must identify articulated objects, segment their movable and interactive parts, and estimate their kinematic models. Existing articulated scene representations typically recover kinematics from observed interactions, while methods operating on static scans often decouple articulation from functional interactive elements. We present FunArt, a framework that constructs articulation-aware functional 3D scene graphs from posed RGB-D observations c...

---

### 12. Learning Foresight without Explicit Trajectories for 3D Diffusion Policies

**Authors:** Zhongbo Zhang, Zaibin Zhang, Yifan Wang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20669v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20669v1)

**Summary:** 3D diffusion policies are strong at generating geometrically grounded actions from current observations, but successful manipulation requires not only knowing what motion is feasible now, but also anticipating where the interaction is heading. Existing policies largely leave such foresight to emerge implicitly from action learning. We introduce Movement Trend Guidance, a simple but effective way to provide this foresight without introducing an explicit plan. From a short observation history, the...

---

### 13. Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies

**Authors:** Jingtao Li, Qian Zhu, Xinyu Wang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20662v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20662v1)

**Summary:** Earth surface anomalies, driven by escalating climate change, and expanding human activities, are increasing in both frequency and diversity, yet their limited historical data and unpredictability make them fundamentally different from conventional remote sensing targets. Existing methods address specific anomaly categories or stop at localization, leaving a gap between detection and actionable information. Here we present ESIA, an Earth Surface Immune System whose architecture is constrained by...

---

### 14. DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation

**Authors:** Yan Qin, Yue Chen, Wenwei Lin, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20649v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20649v1)

**Summary:** Learning predictive models of contact-rich dexterous manipulation requires dense tactile interaction, but such data are costly to scale on real robots and remain tied to embodiment-specific sensors. We introduce DexTouch-WM, an action-conditioned world model that learns from scalable human touch to jointly predict future RGB observations and bilateral tactile dynamics. Our insight is that human and robot manipulation share transferable contact dynamics when their tactile observations and action ...

---

### 15. PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric Videos

**Authors:** Di Wen, Kailun Yang, Jimmy Weissert, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20638v1)

**Summary:** An assistant watching egocentric video should notice a mistake from past frames alone, before the next step begins, and keep working once the person recovers. A mistake changes the state of the work, so every later step has to be read against what was done rather than against the plan. The first-mistake protocol that current online methods report on cuts each recording at its first mistake, so a fixed-time rule that never looks at the video is right on every case. We evaluate on complete trials,...

---

### 16. Refinement Is Inherently Editable: Training-Free Prompt-to-Prompt Image Editing with Generative Refinement Network

**Authors:** Yulong Chen, Ziqian Zhang, Haoyu Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20633v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20633v1)

**Summary:** Text-guided image editing must introduce the requested changes while preserving unrelated source content. Diffusion-based editors rely on spatial controls whose inaccuracies can leave edits incomplete or alter unrelated regions. Causal autoregressive editors face a further constraint: their fixed decoding order limits revision of earlier decisions. We introduce RefineEdit, a training-free prompt-to-prompt image editing framework built on a Generative Refinement Network. Our key idea is to couple...

---

### 17. PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions

**Authors:** Rinto Yagawa, Han Cheng, Dieter Schmalstieg, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20623v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20623v1)

**Summary:** Recent single-view feed-forward 3D Gaussian Splatting (3DGS) generation predicts a fixed number of Gaussians per camera ray, introducing severe spatial redundancy. Most existing compaction strategies target multi-view setups to exploit cross-view consistency and are incompatible with single-image models. Instead of retraining the base feed-forward network to directly output compact representations, our insight is to keep the base models frozen and apply post-hoc pruning and recurrent refinement ...

---

### 18. INSPECT: Learning Robot View Selection from Assistant Use

**Authors:** Di Wen, Kailun Yang, Wenhao Guo, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20615v1)

**Summary:** Robots inspecting an assembly must determine which parts are present and whether they are correctly installed. During egocentric assembly assistance, head motion and workpiece handling reveal evidence for these checks, while spoken state confirmations link observations to procedural outcomes. We introduce INSPECT, which learns robot view preferences from records of a smart-glasses assistant that answers part queries and provides next-step guidance. Presence-Invariant TwinSwap (PI-TwinSwap) calib...

---

### 19. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

**Authors:** Marina Orozco González, Luis Merino

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20589v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20589v1)

**Summary:** Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure-from-Motion preprocessing and are not suited for large inter-frame motion. We present, to the best of our knowledge, the first online Gaussi...

---

### 20. CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding

**Authors:** Zhikun Zhou, Kunyu Peng, Runyi Yang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20586v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20586v1)

**Summary:** Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must...

---

### 21. DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering

**Authors:** Luca De Grandis, Silvia Cappelletti, William Raccagni, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20574v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20574v1)

**Summary:** Answer grounding in document visual question answering remains an open challenge: most benchmarks lack grounding annotations or provide limited-quality labels, while constructing grounded datasets still requires costly manual effort. We introduce DocAttriBench (DAB), a large-scale benchmark for fine-grained, element-level source attribution in Document VQA, grounding answers to specific layout elements such as text blocks, tables, and images. To build DAB, we propose a Mask-based Perplexity-Deri...

---

### 22. OmniMimic: Dynamics-completed Motion Augmentation for Multi-style Omnidirectional Quadruped Locomotion

**Authors:** Sheng Wu, Guoqiang Zhao, Zhe Yang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20566v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20566v1)

**Summary:** Animal demonstrations provide quadruped robots with natural and distinctive gait styles that are difficult to specify through hand-crafted rewards. However, their narrow directional coverage leaves little style-consistent supervision for backward, lateral, and turning commands. We present OmniMimic, a training framework that turns directionally limited animal demonstrations into a single multi-gait policy over target per-axis velocity ranges. OmniMimic first combines temporal reversal, constrain...

---

### 23. A Dual-Stream Regulated Reconstruction and Segmentation Network with Hierarchical Artifact-Prior Modeling for Ultra-Low-Field Pediatric Neuroimaging

**Authors:** Bahram Jafrasteh, Leo Milecki, Qingyu Zhao

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20562v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20562v1)

**Summary:** Automated quality assessment, enhancement, and segmentation of multiple structures in $0.064\,\mathrm{T}$ ultra-low-field pediatric MRI are limited by a low signal-to-noise ratio, weak anatomical boundaries, and frequent artifacts. We present a unified framework for the LISA 2026 Challenge that performs all three tasks together within one inference pipeline. A network with two coupled streams, built on a 3D U-Net, first reconstructs an enhanced uLF volume and then combines the original and enhan...

---

### 24. Automated Goldsmith's Mark Retrieval in Silverware

**Authors:** Atmik Tiwari, Vincent Christlein, Mark Fichtner, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20509v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20509v1)

**Summary:** For art historians, goldsmith marks play a critical role in the identification and dating of artifacts. In practice, experts must manually compare a query mark against hundreds of documented examples, a process that is both tedious and highly dependent on specialist knowledge. To address this, we present an AI-assisted retrieval pipeline that combines mark localization with metric-learning fine-tuning across three backbone architectures: an ImageNet-pretrained ResNet-50, a supervised ViT-S/16, a...

---

### 25. Grounded Product Understanding in Livestream Videos

**Authors:** Xinyu Zhang, Junjie Chen, Jiawei Ge, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20508v1)

**Summary:** E-commerce livestreams have emerged as an important channel for presenting products to online consumers, containing multiple products whose information is scattered in different moments. This poses significant challenges for downstream product understanding applications, such as product-centric livestream clipping, where models need to identify the product and its relevant segments for information gathering. However, existing benchmarks for general product understanding typically evaluate produc...

---

### 26. SenseFuse: Label-Free Fusion of Image and Shape Encoders for Open-Vocabulary 3D Instance Segmentation

**Authors:** Euiseok Han, Tri Ton, Hwanhee Kim, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20475v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20475v1)

**Summary:** Open-vocabulary scene understanding is fundamental for robotics, laying the groundwork for spatial reasoning and object manipulation. While closed-vocabulary 3D instance segmentation heavily leverages 3D shape information, state-of-the-art open-vocabulary methods remain predominantly restricted to 2D image features or image-distilled representations during mask labeling. In this paper, we propose SenseFuse, a label-free fusion method that balances 2D image and 3D shape encoders for robust open-v...

---

### 27. Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation

**Authors:** Fabian Schmalstieg, Karsten Mueller, Wojciech Samek

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20441v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20441v1)

**Summary:** Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware. We distill a 300-million-parameter Prithvi-EO-2.0 teacher, fine-tuned on the 252 manually labeled Sen1Floods11 training scenes, into a 0.7-million-parameter EfficientViT-B0 student. The teacher supervises additional unlabeled Sentinel-2 imagery, allowing the student training set to grow without new manual annotations. At the matched budget of 252 s...

---

### 28. When Do Language-Grounded Explanations Help? A Graph-Bottleneck for Farm Monitoring Interpretable Sheep Facial Pain

**Authors:** Alam Noor, Miguel Guti'errez Gait'an

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20427v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20427v1)

**Summary:** Automated pain recognition from facial expression could make continuous welfare assessment practical in sheep, but adoption depends on trust: a stockperson cannot act on a score that arrives without justification. We ground a model in the Sheep Pain Facial Expression Scale (SPFES) by letting each detected facial region attend over text embeddings of the clinical descriptors and then test whether the resulting explanations mean anything. They do not. Ablating an entire descriptor changes the pred...

---

### 29. WeVisDoc: From Coverage to Capability for Robust End-to-End Document Parsing

**Authors:** Hao Yu, Kang Liu, Linnan Zhao, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20423v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20423v1)

**Summary:** Document parsing converts document images into structured content and requires reliable performance across diverse layouts and acquisition conditions. Yet training corpora are biased toward common document types and clean digital pages, while expanding coverage alone does not specify how to address a parser's remaining weaknesses. We present WeVisDoc, a two-stage data-centric framework for robust end-to-end document parsing. Stage I broadens semantic, structural, and appearance coverage through ...

---

### 30. TouchSight: Bare-Handed Tactile Prediction from Egocentric Video via Generative Visual Augmentation

**Authors:** Danyan Zhou, Jinxuan Lu, Jiawei Lin, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20414v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20414v1)

**Summary:** Tactile signals provide direct contact and force measurements that are essential for understanding physical interactions and enabling dexterous robotic manipulation. However, tactile sensing requires direct measurement at contact interfaces, making large-scale data collection reliant on intrusive, costly, and restrictive instrumentation. We present TouchSight, a monocular egocentric vision framework for dense full-hand contact force prediction that leverages 500 hours of pressure-glove recording...

---

### 31. Navi-Agent: Unlocalized Monocular Navigation Agent

**Authors:** Wenyuan Xie, Mengyang Hong, Yongzhong Wang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20388v1)

**Summary:** Vision-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to execute long-horizon instructions in unknown environments. Existing zero-shot VLN-CE systems typically maintain spatial states through geometric localization or coordinate-based representations. Recent geometry-constrained navigation removes depth and globally consistent coordinates, but maintaining persistent spatial awareness for place confirmation, progress verification, and recovery remains challengi...

---

### 32. Compact Vision Models for Iris Presentation Attack Detection under Presentation Attack Instrument Shift and Environmental Degradation

**Authors:** Athanasios Angelakis, Marta Gomez-Barrero

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20386v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20386v1)

**Summary:** Iris presentation attack detection (PAD) is security-critical when a subsystem that appears reliable during development encounters presentation attack instruments (PAIs) or acquisition conditions absent from validation data. We benchmark three compact scratch-trained computer-vision models, each with at most approximately 0.26 million trainable parameters, on the Notre Dame subset of LivDet-Iris 2017 under PAI-driven domain shift and environmental degradation. All models are trained without exte...

---

### 33. MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving

**Authors:** Shuai Liu, Hechangle Gong, Hao Jiang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20377v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20377v1)

**Summary:** Autonomous driving involves coupled decision-making and scene evolution under multi-mode uncertainty. To capture this coupling and uncertainty, we introduce MM-Future, a world-action model that generates multiple paired scene-action hypotheses and models bidirectional interaction within each pair. Each hypothesis is initialized from a structured action prior and an independent future scene source, which are then co-evolved through a modality-aware diffusion Transformer. To support efficient mult...

---

### 34. EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute

**Authors:** Björn Ellensohn, Elmar Rueckert, Christian Rauch

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20348v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20348v1)

**Summary:** Conventional 3D Gaussian Splatting assumes a closed set of observations and long optimization schedules. Continual RGB-D mapping in contrast poses the problem that new observations arrive online, while previously reconstructed regions must be preserved. We present EliGSiR (Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay), a continual Gaussian mapper that controls how the available optimization budget is used as the reconstruction evolves. Map-Guided View Scheduling...

---

### 35. Fast Cross-Strength Multi-Contrast Brain MRI Translation using Latent Bridge Matching

**Authors:** Siddharth Srivastava, Till Bretschneider

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20341v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20341v1)

**Summary:** Magnetic Resonance Imaging (MRI) acquired at different field strengths exhibits pronounced variation in noise, resolution, homogeneity, and contrast, which limits comparability across acquisition settings and complicates downstream analysis. We address this with a unified conditional model for controllable field-to-field synthesis, built on the framework of conditional latent bridge matching. Our single model achieves highly competitive results across the validation phase for all three tasks of ...

---

### 36. FreqDINO++: A Frequency-Guided Multi-Task Routing Vision Foundation Model for Universal Ultrasound Analysis

**Authors:** Qing Xu, Yixuan Zhang, Yue Li, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20340v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20340v1)

**Summary:** Ultrasound image analysis plays a crucial role in cancer screening and prenatal diagnosis, yet comprehensive assessment requires jointly addressing tasks such as lesion segmentation and benign-malignant classification. While recent vision foundation models have shown remarkable universal representations, unlocking their potential for ultrasound is bottlenecked by the considerable domain gap from natural images. Existing methods typically fine-tune heavy vision encoders for isolated tasks, incurr...

---

### 37. AgriScope: Pixel-Grounded Multimodal Understanding for Agricultural Images

**Authors:** Abderrahmene Boudiaf, Mohamad Alanssari, Irfan Hussain, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20325v1)

**Summary:** Agricultural image understanding requires fine-grained recognition of plant diseases, pests, crop structures, and botanical species under complex real-world conditions. Despite recent advances in Multimodal Large Language Models (MLLMs), existing models remain limited to text-only outputs and lack pixel-level visual grounding capabilities. In this work, we introduce AgriScope, a unified pixel-grounded multimodal framework for agricultural image understanding. AgriScope jointly supports image-lev...

---

### 38. Needles in a Raystack: Ultra-Sparse LiDAR Occupancy Detection for Bat Tracks

**Authors:** Nico Klar, Pankaj Rana, Nizam Gifary, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20160v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20160v1)

**Summary:** Monitoring flying animals is important for understanding and protecting biodiversity, but nocturnal species such as bats are difficult to observe in the field. Using LiDAR, bat movements at night result in ultra-sparse 3D spatio-temporal data in which standard reconstruction losses tend to predict only background and miss real flight paths. We study this problem as voxel-wise occupancy detection in sensor-centric LiDAR raystacks. A lightweight 3D U-Net is proposed that preserves temporal resolut...

---

### 39. Ischemic Stroke Segmentation and Net Water Uptake Quantification on Multicenter Non-Contrast CT Using Supervised Target-Domain Adaptation

**Authors:** Linus Britt, Maximilian Nielsen, Susan Klapproth, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20151v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20151v1)

**Summary:** Objectives: Quantitative assessment of infarct hypodensity on non-contrast computed tomography (NCCT), including net water uptake (NWU), requires manual or semi-manual lesion delineation, often guided by CT perfusion or diffusion-weighted MRI, limiting clinical applicability. Automated segmentation on NCCT could enable efficient biomarker extraction such as NWU but remains challenging across heterogeneous multicenter data. This study aimed to develop and externally test a domain-aware deep learn...

---

### 40. Task-Oriented Semantic Feature Transmission for Multi-Task Satellite Remote Sensing over Low-SNR Channels

**Authors:** Shuoyuan Sun, Hongyu Wang, Mugen Peng, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20150v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20150v1)

**Summary:** Conventional satellite remote sensing transmission follows a reconstruct-then-infer paradigm that optimizes pixel-level fidelity, creating an objective mismatch with downstream tasks such as classification and detection, especially at low SNR. This paper investigates a task-oriented framework that bypasses image reconstruction and directly transmits semantic features extracted by a multitask-pretrained backbone. A lightweight channel adaptation module (CAM) compresses feature dimensionality for ...

---

### 41. Bridging Modalities on the Cortex: Surface-based MRI to PET Translation with a Diffusion Bridge

**Authors:** Yitong Li, Alexandra Samoylova, Fabian Bongratz, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20147v1)

**Summary:** Cortical hypometabolism measured by Fluorodeoxyglucose Positron Emission Tomography (FDG-PET) is a highly sensitive biomarker for dementia diagnosis. However, high costs, radiation exposure, and limited accessibility constrain its clinical utility. While cross-modal synthesis from Magnetic Resonance Imaging (MRI) offers a promising alternative, existing volumetric generation methods do not explicitly account for the highly folded cortical geometry, where disease-related patterns predominantly re...

---

### 42. Cross-Modal Attention Acts as a Frequency Filter: Why Verbose Prompts Improve Robustness in Vision-Language Models

**Authors:** Farooq Ahmad Wani, Maria Sofia Bucarelli, Mujtaba Hussain Mirza, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20139v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20139v1)

**Summary:** Vision-language models (VLMs) are fragile under image corruption. We find that the wording of the question affects VLMs in two opposite ways. Verbose questions make VLMs substantially more robust---e.g., rephrasing "Is there a cat?" into "Please look carefully and answer: is there a cat?". Conversely, VLMs become more fragile under corruption when the question is semantically complex or finer-grained, e.g., "what colour is the cup left of the chair?" instead of "is there a cup?". Both effects st...

---

### 43. AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention

**Authors:** Yuang Tu, Runjia Tan, Yujie Yan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20106v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20106v1)

**Summary:** Robotic reward models evaluate task execution from visual observations, but their predictions can change with camera viewpoint and occlusion even when the underlying task state is unchanged. Adapting a pretrained reward model to a local task therefore requires accounting for how that task is observed. We introduce AnyviewMeter, a geometry-conditioned adaptation framework for robotic reward models that represent task progress as a scalar reward signal. It combines low-rank fine-tuning with token-...

---

### 44. A Smaller Transformer in Your Transformer

**Authors:** Dhananjay Tomar, Marius Aasan, Andreas Kleppe, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20100v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20100v1)

**Summary:** Recent findings indicate that Vision Transformers settle into locally similar computational phases, implying a level of depthwise computational redundancy. However, existing methods to exploit this redundancy either fail to reduce inference compute or severely degrade model expressivity. In this work, we formalise a unified view of block redundancy that decouples the geometry from specific surrogate interventions. We then introduce Transformer-Within-Transformer (TWT), a post-hoc method that fus...

---

### 45. G^2RA-NET: Graph-based Cross-Slice Relation Modeling with Attention Gating for Medical Image Segmentation

**Authors:** Shengye Wang, Zonglin Wu, Liang Fan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20088v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20088v1)

**Summary:** Medical image segmentation supports quantitative clinical analysis and computer-aided diagnosis. Recent methods for medical image segmentation have improved both local feature representation and volumetric context modeling. However, existing methods still strug- gle to efficiently model cross-slice relations in anisotropic volumet- ric images, limiting segmentation consistency and accuracy. This pa- per proposes G^2RA-Net, a medical image segmentation framework that combines graph-based cross-sl...

---

### 46. PointEvent: Rethinking Event-based Tiny Object Detection via Serialized Motion Evidence Accumulation

**Authors:** Zongze Wu, Baofeng Jia, Weiqi Yan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20066v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20066v1)

**Summary:** Event cameras offer high temporal resolution and motion sensitivity for tiny UAV detection, yet distant targets generate sparse and fragmented events that are easily overwhelmed by clutter and ego-motion. Existing methods mainly rely on dense event representations or local sparse spatiotemporal modeling, resulting in redundant computation or fragmented modeling of motion continuity across distant asynchronous events. To address this limitation, we introduce serialized motion evidence accumulatio...

---

### 47. A Free Lunch? Adapting PP-OCRv6 for Historical Text Recognition

**Authors:** Benjamin Kiessling

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20064v1)

**Summary:** Despite impressive reported scores, large vision-language models have seen limited practical uptake in historical automatic text recognition because of their computational cost, dependence on large-scale pretraining, and hallucination. Historical ATR therefore continues to rely largely on compact CRNN line recognizers, which are visually grounded and trainable on modest data. Lightweight recurrence-free recognizers promise the accuracy of larger models with the practical advantages of CRNNs, yet...

---

### 48. Astronex-World 1.0: Real-Time Interactive World Model Foundation

**Authors:** Xin Zhou, Cong Miao

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20034v1)

**Summary:** We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV ...

---

### 49. GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction

**Authors:** Enpeng Li, Yunzhou Zhang, Zhiyao Zhang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20012v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20012v1)

**Summary:** Feed-forward 3D reconstruction provides an efficient paradigm for scene modeling from image sequences. Scaling these models to large monocular scenarios are constrained by excessive GPU memory footprint, degraded local geometry, and long-term trajectory drift. Existing chunk-based optimization strategies provide limited geometric constraints and fail to maintain global consistency over extended trajectories. We present a unified framework for stable and scalable feed-forward 3D reconstruction fr...

---

### 50. AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models

**Authors:** Longyin Zhang, Parth Sakhare Mahendra, Chengwei Wei, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19991v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19991v1)

**Summary:** Omni models can describe video content, but can they locate events in time, preserve event order, and judge audio-visual synchronization? We introduce AVTrace (Audio-Visual Temporal Reasoning Assessment and Capability Evaluation), a silver-standard diagnostic suite spanning onset and span grounding, synchronization, next-step prediction, cross-modal localization, chain parsing, and event-conditioned comprehension. It contains 34,114 training examples and category-balanced development and test sp...

---

## cs.LG

**50 papers**

### 1. Embedding Models Measure in Peculiar Ways

**Authors:** Juri Opitz, Andrianos Michail

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20821v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20821v1)

**Summary:** Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective notion of semantic equivalence and distance. We find that physical measurement is only weakly modeled in the embedding space, and that instead quite peculiar measurement patterns can be observed. Further analysis indicates that embedding representations of physical measurements are strongly influen...

---

### 2. Paint-Anything: Unified Any-Color Control for Image Generation and Editing

**Authors:** Ji Xie, Dewei Zhou, Xinyu Huang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20816v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20816v1)

**Summary:** Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-...

---

### 3. How Does Distribution Shift Shape Pretraining Gains in Neural PDE Surrogates?

**Authors:** Pochinapeddi Sai Bhargav, Nithin Somasekharan, Rohit Sunil Kanchi, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20814v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20814v1)

**Summary:** Pretraining a neural PDE surrogate can reduce the amount of new CFD data needed when geometry or modeled physics changes. However, it remains unclear how different components of distribution shift affect this benefit. We pretrain a surrogate on 254,909 RANS solutions from one airfoil family and fine-tune it on a new family under two target settings with matched freestream ranges: the same Spalart-Allmaras (SA) modeling and SA with added $e^N$ transition modeling. At $N=1000$, the pretrained mode...

---

### 4. Quantifying Overclaiming Propensity in Frontier LLM Agents

**Authors:** Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Jr Tikeng Notsawo, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20812v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20812v1)

**Summary:** Frontier coding agents are increasingly trusted to work autonomously for long periods, yet an agent's final response is often the only account of that work a user sees. We quantify the propensity of frontier agents to \emph{overclaim} task completion, a misrepresentation that can mislead the user. An agent overclaims when its final response contradicts information in its context. This definition requires no inference about intent and is independent of task success. We introduce \emph{OverclaimBe...

---

### 5. Score Centering Stabilizes Off-policy Reinforcement Learning

**Authors:** Martin Marek, Max Ryabinin

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20807v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20807v1)

**Summary:** Reinforcement learning (RL) of large language models is notoriously sensitive to small differences between training and inference engines, often referred to as the training-inference mismatch (TIM). However, completely eliminating TIM is impractical, as it would come at a major cost to rollout efficiency. In this paper, we show that the instability of RL under TIM is primarily caused by drift: a persistent bias between training and inference engines that accumulates with every training step. We ...

---

### 6. An Empirical Study of Harness Design for Coding Agents

**Authors:** Run-Ze Fan, Zihao Zhang, Simin Ma, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20804v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20804v1)

**Summary:** Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluate...

---

### 7. PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative Inverse Solvers

**Authors:** Jiachen Yao, Zi-Siang Hsu, Xi Deng, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20794v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20794v1)

**Summary:** Generative models are increasingly used to solve scientific inverse problems, but existing evaluations still focus primarily on whether a method can produce a single plausible reconstruction. This is insufficient for ill-posed problems, where multiple solutions may be consistent with the same sparse or noisy observations. In these settings, a method can achieve strong pointwise accuracy while still failing to capture the true posterior through mode collapse, overconfident uncertainty, or averagi...

---

### 8. GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies

**Authors:** Xin Chen, Sen Chen, Yujuan Ding, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20776v1)

**Summary:** Action chunking is widely used for action generation and execution in Vision-Language-Action (VLA) policies, yet existing approaches commonly use a fixed action horizon. During a rollout, different task stages may require different levels of action continuity, control precision, and closed-loop feedback, making a fixed horizon unable to accommodate changing control requirements. We propose \textbf{GeoAAC}, a geometry-based adaptive action chunking method for flow-based VLA policies that adjusts ...

---

### 9. Calibrated RF-Fingerprinting Under Interference With Heterogeneous Transmission Protocols

**Authors:** Tariq Abdul-Quddoos, Xiangfang Li, Lijun Qian

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20765v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20765v1)

**Summary:** Radio Frequency(RF)-Fingerprinting is a spectrum monitoring technique that identifies specific transmitters based on hardware impairments imprinted within the emitted signal. Although widely researched, studies almost exclusively consider scenarios where only one transmitter is emitting at a time, limiting real world applicability. In this work, we further the study of RF-Fingerprinting by considering co-channel interference, with multiple emitted signals interfering with each other, overlapping...

---

### 10. Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control

**Authors:** Hanchu Zhou, Brendan Lynch, Raman Goyal, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20761v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20761v1)

**Summary:** World Action Models (WAMs) advance beyond conventional visuomotor policies by jointly predicting future world states and robot actions, enabling the policy to learn physical dynamics that support effective control. However, recent tactile WAMs often rely on large-scale pretrained generative backbones to capture contact-rich physical dynamics, which limit their inference efficiency and flexible deployment. In this paper, we present \ABBR{}, an agile tactile World Action Model for contact-rich rob...

---

### 11. Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation

**Authors:** Sho Kawano, Zehang Richard Li, Paul A. Parker

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20758v1)

**Summary:** Evaluating an AI system requires disaggregated assessment, as performance varies across domains such as benchmark task types or conversation types in deployed agents. Exhaustive testing is expensive, so evaluation rests on a sample of labeled units. We treat the evaluation set as a finite population and seek accurate point and interval estimates of each domain mean. Direct estimators, including prediction-powered inference (PPI), use only a domain's own labels and are imprecise where labels are ...

---

### 12. OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher

**Authors:** Damiano Da Col, Maximilian Igl, Peter Karkus, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20756v1)

**Summary:** As scaling pre-training data alone yields diminishing returns, post-training is becoming increasingly important across physical AI domains such as autonomous driving. End-to-end driving policies are pre-trained in open loop with behavior cloning on human demonstrations. However, compounding errors during closed-loop deployment can take the vehicle outside the training data distribution, increasing the risk of safety-critical incidents. Closed-loop post-training can mitigate this risk but require...

---

### 13. dQwen3.5: Hybrid-Attention Diffusion Language Models

**Authors:** Anton Xue, Litu Rout, Aditya Akella, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20751v1)

**Summary:** Adapting a pretrained autoregressive (AR) model is a cost-efficient route to a diffusion language model (DLM). While nearly all such adaptations start from a full-attention transformer, AR modeling has shifted toward hybrid architectures that interleave attention and RNN layers. This creates an obstacle for adaptation: unlike attention, RNNs are structurally causal and nontrivial to bidirectionalize. Despite this mismatch, we investigate whether such backbones can become effective DLMs by adapti...

---

### 14. MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving

**Authors:** Thomas Steinecker, Denis Trescher, Alexander Bienemann, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20747v1)

**Summary:** Reinforcement learning constitutes a promising approach owing to its potential for superhuman performance and self-learned policies. However, its application to real-world autonomous driving remains scarce, particularly in unstructured environments, because of the challenges associated with sim-to-real transfer for unstructured environments. In this work, we present MILER, an end-to-end policy framework with zero-shot sim-to-real transfer. During offline training, we employ a custom semantic mid...

---

### 15. Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation

**Authors:** Haocheng Xi, Yiming Xie, Hexu Zhao, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20744v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20744v1)

**Summary:** Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for l...

---

### 16. Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

**Authors:** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20715v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20715v1)

**Summary:** Agent trajectories record what an agent does and what happens next. Yet standard supervised fine-tuning (SFT) applies loss only to agent-authored action tokens, using environment observations as context but not as prediction targets. We ask whether this convention provides the best initialization for subsequent reinforcement learning. We introduce ActObs, which also supervises the observation tokens already present in each trajectory. Although deployed agents never generate observations, learnin...

---

### 17. Stable Movement for Nondual Lipschitz Convex Optimization: Efficiency and Nearly Optimal Oracle Rates

**Authors:** David Martínez-Rubio, Cristóbal Guzmán

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20701v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20701v1)

**Summary:** We study efficient algorithms for realizing the first-order oracle complexity of optimization of $G$-Lipschitz convex functions with respect to the $\ell_{q}$-norm over an $\ell_{p}$-ball of radius $R$, where $1\leq p,q\leq \infty$. For $p<q$, we obtain error $\widetilde{O}_{p,q}(GR/T^{1/p-(1/q-1/2)_{+}})$ after $T$ oracle queries, efficiently realizing the nearly optimal rates of (MBG+26), thereby resolving the nonsmooth end of the COLT 2015 open problem (Guz15b). In particular, the rate is $\w...

---

### 18. TetrisCNN for interpretable detection of phases of matter from experimental quantum simulator data

**Authors:** Kacper Cybiński, Björn van Zwol, James Enouen, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20693v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20693v1)

**Summary:** Detecting phases of matter in general relies on identifying the correct order parameter - a task that remains notoriously difficult for unknown transitions and traditionally is guided by physical intuition and educated guess. Neural networks have recently offered an alternative route by locating phase transitions in known models without any a priori physical knowledge. Yet these approaches remain black boxes and only identify phases without elucidating their properties. Moreover, they often stru...

---

### 19. The First-Order Oracle Complexity of Lipschitz Convex Optimization in Nondual Settings

**Authors:** David Martínez-Rubio, Brian Bullins, Cristóbal Guzmán, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20687v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20687v1)

**Summary:** We study first-order black-box convex optimization over an $\ell_p$-ball for objectives Lipschitz in the $\ell_q$-norm, solving in the affirmative the nonsmooth version of the COLT open question (Guz15b) on whether the geometry of a smaller feasible set ($p < q$) can improve convergence rates in convex optimization, and matching prior lower bounds up to logarithmic factors. Our rates include \(\widetilde O(1/T)\) for convex Euclidean-Lipschitz optimization over the $\ell_1$-ball, improving on th...

---

### 20. RISC-V and machine learning: a survey

**Authors:** Shriman Keshri, Apparna Singh, Chinmaya Kumar Palo, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20677v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20677v1)

**Summary:** The intersection of open-source processor architectures and machine learning is driving the demand for customizable, efficient, and accessible hardware. This survey examines the state of the RISC-V ISA in machine learning applications, analyzing current capabilities, challenges, and future directions based on recent research. The analysis covers academic and commercial implementations, software frameworks, and real-world applications. The RISC-V machine learning ecosystem is evaluated, from inst...

---

### 21. Epidemiological Causal Graph Identification: Challenges, Identifiability and Algorithms

**Authors:** Sambit Mishra, Yingying Wang, Christine K. Johnson, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20676v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20676v1)

**Summary:** Causal discovery from observational data is fundamental to statistics and machine learning, yet determining causal direction without interventions necessitates structural assumptions. Existing identifiability research primarily focuses on continuous variables under additive noise models, often neglecting mixed datasets containing ordinal scales, counts, and continuous measurements. This paper investigates causal discovery in Directed Acyclic Graphs (DAGs) where nodes follow either an ordinal dis...

---

### 22. Multi-center Medical Data Mining with FL-Net - A One-stop Shop for Federated Learning

**Authors:** Simon Süwer, Julian Klemm, Elisa Acitelli, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20650v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20650v1)

**Summary:** Federated learning enables collaborative training without sharing patient-level data, but most studies remain simulations. Based on five requirements derived from the literature, we analyzed 14 FL frameworks and found that none fully satisfied these requirements. We present FL-Net, a novel federated clinical research framework to fulfill all requirements. It integrates modular data harmonization, data discovery, disclosure control, securely built versioned FL-Net-Tools and containerized federate...

---

### 23. Beyond PINNs: A Unified Gauss--Newton and Petrov--Galerkin Framework for Neural and Hybrid PDE Solvers

**Authors:** Nilo Schwencke, Roland Maier

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20641v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20641v1)

**Summary:** Physics-informed neural networks and finite element methods provide two different paradigms for the numerical approximation of partial differential equations: the former are commonly trained by minimizing pointwise strong residuals, whereas the latter are naturally built from weak variational formulations and the finite-dimensional systems obtained after discretization. In this work, we introduce a common framework based on the discretization of functional Gauss--Newton problems by finite famili...

---

### 24. COIN-GP: Cooperative Online Learning in Networked Distributed Systems with Partial Measurements via Gaussian Process Regression

**Authors:** Zewen Yang, Xiaobing Dai, Zhenxiao Yin, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20598v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20598v1)

**Summary:** In this paper, we tackle the problem of jointly estimating the system states and partially unknown dynamics within distributed sensor-equipped networks, particularly in scenarios where only partial state observations are available. To address this issue, we propose an observer-based dynamic cooperative learning framework incorporating online distributed Gaussian Process (GP) regression, which enables accurate estimation despite incomplete in measurements and deficient GP models. In addition, a n...

---

### 25. Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature Forecasting

**Authors:** Mu-En Lee, Yen-Ku Liu, Samuel Yen-Chi Chen, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20594v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20594v1)

**Summary:** Quantum long short-term memory (QLSTM) models extend recurrent sequence learning with variational quantum circuits, but their optimization behavior can vary substantially across random initializations and temporal contexts. This paper evaluates a recursive QLSTM architecture against a standard QLSTM for one-step-ahead prediction of daily minimum and maximum temperature. Using daily weather observations from Toronto and identical training settings, we compare convergence, predictive accuracy, and...

---

### 26. CrystalMO-TuRBO: Multi-Objective Trust-Region Bayesian Optimization for High-precision Joint Crystal Structure Refinement

**Authors:** Joseph Agada, Yishu Wang, Arpan Biswas

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20592v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20592v1)

**Summary:** Crystal structure refinement is a fundamental inverse problem in materials characterization, where structural parameters are optimized to reproduce experimental diffraction data. Conventional approaches, such as least-squares and likelihood-based optimization, rely on local search and often struggle with non-convex, noisy, and highly correlated parameter landscapes, particularly when integrating multiple diffraction modalities. Joint refinement of X-ray and neutron data is especially challenging...

---

### 27. NS3Learn: Transferring 5G NR Mode-2 Reception Realism from ns-3 to the Veins/SUMO Stack for Connected-Vehicle Safety Assessment

**Authors:** Rasheed Bello, Arthur Mukwaya, Gurcan Comert, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20578v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20578v1)

**Summary:** Connected-vehicle safety evaluations rely on coupled traffic and network simulations, but standard channel models ignore radio resource competition in 5G NR sidelink Mode-2, reporting unrealistically high message delivery in dense traffic. This study introduces resource-competition losses without requiring full protocol reimplementation. We labeled 10.5 million reception outcomes from ns-3 5G-LENA traces (calibrated on 3GPP scenarios and driven by SUMO trajectories) to fit NS3Learn - a closed-fo...

---

### 28. TAP Accuracy Below the Fluctuation Scale and Universal Posterior Geometry in Spherical Linear Models

**Authors:** Jingbo Liu, Zhiyuan Yu

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20577v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20577v1)

**Summary:** We study the Bayes-optimal spherical linear model as the ambient dimension and sample size grow proportionally, under a quantitative Marchenko--Pastur spectral-regularity condition on the design. This condition is satisfied by normalized i.i.d. designs with standardized entries of finite fourth moment, but does not require entrywise independence or impose conditions on the singular vectors. Under this condition, we prove a quantitative all-temperature TAP approximation and characterize the poste...

---

### 29. Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control

**Authors:** Yilang Liu, Haoxiang You, Qian Wang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20575v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20575v1)

**Summary:** Learning visual policies for locomotion and manipulation requires coordinating contact with the environment and can incur substantial computation and GPU memory costs. First-order policy gradients (FoPG) reduce training cost through differentiable simulation, but local optimization can converge to unintended contact patterns. To address this shortfall, we propose Sampling-Guided Policy Search (SGPS), which couples recurring action-target refinement by sampling-based model-predictive control with...

---

### 30. Mitigating Retaliatory Algorithmic Collusion in Repeated Games

**Authors:** Karthik Sivachandran, Rohan Paleja

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20548v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20548v1)

**Summary:** Reinforcement learning agents trained to maximize their own reward in repeated interactions can converge to supra-competitive outcomes resembling explicit collusion, without communication or shared design. Existing mitigation approaches are largely tied to specific economic settings, like two-sided platforms and auctions, leaving open how to design interventions for general repeated games. We address this gap by formalizing the connection between empirical observations from prior work on Q-learn...

---

### 31. Parallelism, critical windows, and separations among diffusion language models

**Authors:** Sitan Chen, Liye Wang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20539v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20539v1)

**Summary:** A popular selling point of diffusion large language models (dLLMs) is their capacity for parallelism: the ability to generate sequences of text far more efficiently than autoregressive models, which require one forward pass per token. Yet among the many competing paradigms for dLLMs, from masked to uniform to Gaussian diffusion, principled understanding of how these different proposals compare in parallelism remains limited. In this work, we initiate a fine-grained comparison of the capacity for...

---

### 32. Relational Attention for Data-Efficient Language Modeling

**Authors:** Adrian Brasoveanu, Ece Takmaz, Jakub Dotlačil

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20530v1)

**Summary:** We present Relational BabyLM, a system submission to the BabyLM 2026 challenge that combines two cognitively motivated inductive biases in a single decoder-only Transformer. Architecturally, we replace standard self-attention with a Dual Attention Transformer (DAT), which separates the routing of object-level ("sensory") lexical features from structural/relational information (Altabaa and Lafferty, 2025; Altabaa et al., 2024; Webb et al., 2024; Kerg et al., 2022; Webb et al., 2021). Relational a...

---

### 33. Noise-Robust Quantum State Characterization for Remote State Preparation with Deep Learning

**Authors:** Bo Tang, Zixuan Liao, Hao Li, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20523v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20523v1)

**Summary:** Quantum communication underpins secure information processing and scalable quantum networks. In particular, remote state preparation (RSP) enables efficient quantum state transfer, but accurately estimating target states under complex noise remains challenging. Here, we propose a Transformer-based Quantum State Characterizer (TQSC) model for noisy RSP experiments. Our model reconstructs experimentally prepared pure and mixed photonic polarization states from noisy measurements in complex scatter...

---

### 34. When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation

**Authors:** Yuxiao Yang, Tianrun Yu, Shangzhe Li, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20511v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20511v1)

**Summary:** We study length inflation in on-policy distillation (OPD), where student responses can become excessively long and even exhaust the generation budget. We identify \emph{termination-token mismatch} between base students and post-trained teachers as an important source of this behavior. Across Qwen3, Llama, and Gemma, the two models can place their stopping probability on different EOS tokens, even when their declared stopping sets are identical. This mismatch can suppress the student's preferred ...

---

### 35. Truncated automatic sparse differentiation for machine learning interatomic potentials

**Authors:** Marcel F. Langer, Adrian Hill, Michele Ceriotti

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20510v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20510v1)

**Summary:** Machine learning interatomic potentials (MLIPs) learn the mapping from atomic positions to potential energy. The forces, the negative gradient of this energy, drive molecular dynamics and are readily obtained using automatic differentiation. Higher-order derivatives, most notably the Hessian, describe collective motion and allow the direct prediction of experimental observables, but are considered computationally inaccessible for large systems. We suggest a solution: in physical systems, interac...

---

### 36. Radio Frequency Detection and Classification of Microplastics in Water

**Authors:** Jaden Tolbert, Md Saiful Islam, Pingshan Wang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20507v1)

**Summary:** Micro- and nano-plastic particles (MPs/NPs) are ubiquitous environmental contaminants whose increasing abundance and potential health impacts have created an urgent need for rapid, label-free detection methods. As particle size decreases to the low-micrometer range, conventional optical and spectroscopic techniques become increasingly challenging because of limited throughput and/or complex sample preparation. In this work, we present a machine learning (ML)-assisted radio-frequency (RF) dielect...

---

### 37. Distributionally Robust Federated Learning with Multi-Source Data

**Authors:** Yingzhu Liu, Zhongkui Li, Pengcheng You, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20501v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20501v1)

**Summary:** Federated learning trains a shared model from private client data. In practice, data-generating distributions may differ, and the true mixture across clients is often unknown, making the underlying group distribution difficult to specify. Existing approaches address cross-client mixture uncertainty by optimizing against the worst-case mixture, yet assume accurate client-wise distribution estimates. However, these estimates can be unreliable when based on finite samples. To handle both cross-clie...

---

### 38. Resolution limits for process comparison from event data

**Authors:** Antony R. Lee, Peter Tiňo, Iain B. Styles

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20489v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20489v1)

**Summary:** One hospital runs bloods and imaging at the same time. Another runs them one after the other, in either order, equally often. Knowing which actually happened, and how it is recorded in data, is critical for all operational managers. In process mining, the standard approach is to construct an event log, and attempt to discover concurrent and sequential processes in a data-driven way. We show this standard approach, built on the stochastic language of an event log, reports only the assumptions of ...

---

### 39. Deep Learning-Based Classification of Cognitive and Resting States Using Electroencephalography Signals

**Authors:** K. A. Januka S. Fernando, Harshit Srivastava

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20467v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20467v1)

**Summary:** The categorization of cognitive and resting states derived from electroencephalography (EEG) signals is crucial for comprehending fluctuations in brain activity linked to various mental states. EEG provides a non-intrusive approach for documenting brain function in both resting and task-oriented cognitive conditions, whilst deep learning techniques enable the automatic extraction of significant patterns from intricate EEG data. This study presents a deep learning framework to distinguish between...

---

### 40. Training Neural Networks to Approach the Optimum Bayes Estimator in Dense Multi-Emitter Localization

**Authors:** Yi Sun, Mona Sharifi, Muzna Yumman

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20465v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20465v1)

**Summary:** We train neural networks on synthesized frames to approach the optimum Bayes estimator for dense emitter localization. The result justifies the future work on training neural networks to achieve high-throughput large-FOV super spatiotemporal resolution SMLM.

---

### 41. Correlation-Free Transition Path Sampling through Shooting Point Generation Guided by Committor Learning

**Authors:** Maximilian Negedly, Sebastian Falkner, Alessandro Coretti, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20461v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20461v1)

**Summary:** Studying the dynamical behavior of a system often depends on characterizing how it transitions between long-lived states. Because such transitions are rare, observing them usually requires specialized enhanced sampling techniques. Transition Path Sampling (TPS) is a well-established method for generating reactive trajectories, which is simple to implement and does not require the definition of a preconceived reaction coordinate. However, its efficiency is limited by its sequential nature and the...

---

### 42. Online Supervised Dimension Reduction with Random Features: Diagnostics and Computational Trade-offs

**Authors:** Zhenlin Yao, Wei Xiong

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20454v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20454v1)

**Summary:** Accurate optimization of a supervised spectral objective need not produce an accurate population subspace or a better predictive representation. We investigate these distinctions for Online Kernel Supervised Principal Component Analysis (OKSPCA), which combines a centered cross-moment in finite random-feature coordinates with an Adam-style orthonormal basis update for an established objective. Fixed-map consistency, concentration and perturbation results describe the estimator and its exact subs...

---

### 43. Seismic Site Response Prediction from Sparse Observations Using Finite-Element-Pretrained Latent Dynamics

**Authors:** Yi Zhu, Su Chen, Xiaojun Li

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20451v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20451v1)

**Summary:** Numerical site-response predictions often deviate from observations, yet correcting these discrepancies is difficult because records are limited in both sensor coverage and number of events. This study proposes the Transfer-Enabled Forced Latent Autoencoder for Response Equations (FLARE-T) to improve these predictions by learning and calibrating low-dimensional latent dynamics that connect the base acceleration input to acceleration outputs at multiple depths. FLARE-T learns a low-dimensional re...

---

### 44. Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation

**Authors:** Fabian Schmalstieg, Karsten Mueller, Wojciech Samek

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20441v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20441v1)

**Summary:** Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware. We distill a 300-million-parameter Prithvi-EO-2.0 teacher, fine-tuned on the 252 manually labeled Sen1Floods11 training scenes, into a 0.7-million-parameter EfficientViT-B0 student. The teacher supervises additional unlabeled Sentinel-2 imagery, allowing the student training set to grow without new manual annotations. At the matched budget of 252 s...

---

### 45. SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models

**Authors:** Xiaodong He, Xincheng Wang, Zhao Kang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20419v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20419v1)

**Summary:** Graph foundation models (GFMs) aim to learn transferable representations across severely heterogeneous graph domains. However, severe domain shifts in topology, graph scale, and feature semantics impede the construction of a unified, domain-agnostic representation space. To address this, we propose SCGFM-ART, a structure-centric GFM framework that aligns arbitrary graphs onto a shared relational atlas via Amortized Relational Transport (ART). The relational atlas serves as a universal coordinate...

---

### 46. The Bias of Nonlinear Two-Time-scale Stochastic Approximation under Constant Step-Sizes

**Authors:** Djamel Rassem Lamouri, Dorian Baudry, Nicolas Gast

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20409v1)

**Summary:** Two-timescale stochastic approximation (TTSA) is a fundamental tool for analyzing coupled iterative algorithms in reinforcement learning, optimization, and stochastic control. However, finite-time guarantees for nonlinear two-timescale schemes remain difficult to obtain, especially under constant step-sizes. In this paper, we study nonlinear TTSA with step-sizes $α\ggβ$. Under standard stability, regularity, and Markovian noise assumptions, we upper bound the mean-squared error and the bias of b...

---

### 47. Learning Principal-Agent Contracts for Equitable Smallholder Carbon Farming under Moral Hazard and Adverse Selection

**Authors:** Rishi Bharadwaj, Yadati Narahari

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20404v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20404v1)

**Summary:** Agricultural soils are a major untapped carbon sink. Carbon farming is emerging as a promising practice for tapping this potential. Smallholder farmers, who dominate agriculture across South Asia and sub-Saharan Africa, are key to scaling climate mitigation via carbon farming. It is ironic that real-world carbon programs largely fail to reach them. We study this important gap through the lens of contract design. An aggregator offers a single pooled contract to a heterogeneous population of small...

---

### 48. Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning

**Authors:** Weiwei Wang, Yuqiang Li, Xianyi Wu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20389v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20389v1)

**Summary:** Offline policy evaluation (OPE) is crucial in high-stakes reinforcement learning applications, where new policies must be assessed reliably before deployment. In such settings, point estimates alone are insufficient; principled uncertainty quantification, such as confidence intervals and variance estimates, is essential for safe and risk-aware decision-making. A comprehensive way to unify these tasks is to estimate the sampling distribution of the evaluation error. Existing approaches, however, ...

---

### 49. Minimax-Optimal Online Contract Design with Unrestricted Bounded Contracts

**Authors:** Rui Ai, David Simchi-Levi, Han Zhong

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20353v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20353v1)

**Summary:** We study repeated contract design when a principal observes outcomes but not the actions that generate them. The principal may use any bounded outcome-contingent payment vector, and the agent's best response can make expected profit discontinuous in those payments. For every fixed number $m\ge2$ of outcomes, the minimax regret over $T$ rounds is of order $T^{m/(m+1)}$, up to logarithmic factors. The upper bound allows arbitrary action spaces and agent heterogeneity, without smoothness or monoton...

---

### 50. COMPASS: Ordered Clustered Routing at 100K Scale

**Authors:** Ido Greenberg, Hugo Linsenmaier, Piotr Sielski, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20352v1)

**Summary:** Large-scale routing often requires visiting clusters of nodes in a prescribed order, giving rise to the Ordered Clustered Traveling Salesman Problem (OCTSP). Optimizing each cluster independently seems natural, but misses non-local dependencies. We introduce the COMPASS algorithm for OCTSP, which combines search with learning-accelerated routing by orchestrating parallel sub-solvers. COMPASS has no quality ceiling and its solutions keep improving with compute. It exploits the clustered structure...

---

## cs.NE

**50 papers**

### 1. Position Paper: Neurotransmitters as a Missing Dimension in Artificial Neural Networks

**Authors:** Yupei Li, Manuel Milling, Berrak Sisman, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20083v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20083v1)

**Summary:** Artificial neural networks (ANNs), as core components of modern deep learning (DL) systems, lack the adaptive flexibility and long-term stability exhibited by biological systems. This limitation largely stems from the fact that conventional ANNs rely on uniform, local, and gradient-based parameter updates, while neglecting internal learning principles that are biological mechanisms such as neurotransmitters signalling or neuroplasticity. Consequently, many existing approaches focus on architectu...

---

### 2. Self-Replicating Neural Cellular Automata: Quantifying Emergent Phenotypic and Genotypic Diversity in an OpenEnded Substrate

**Authors:** Sanyam Jain, Felix Simon Reimers, Stefano Nichele

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19902v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19902v1)

**Summary:** We study an in-silico substrate in which every pixel of a two-channel cellular-automata grid carries a tiny neural network (an agent) that senses its Moore neighborhood. A cell persists only by self-replication: a living neighbor is cloned and its weights are mutated by a uniform perturbation, so that phenotype (cell state) is driven entirely by genotype (network weights). From a handful of seeded founders the system grows into a spatially organized ecosystem of coexisting, competing and dominat...

---

### 3. A Metaheuristic Optimization Framework for Discrete Optimization under Strict Time Limits

**Authors:** Umut Çalıkyılmaz, Nitin Nayak, Sven Groppe

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18702v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18702v1)

**Summary:** Real-time applications often rely on optimization approaches that can find high-quality solutions to hard problems on the order of milliseconds. Metaheuristic optimization frameworks (MOFs) are useful tools for such tasks, as they provide large sets of general-purpose search mechanisms that can return solutions under different computational budgets. However, existing work largely overlooks the available computation time as an explicit dimension of analysis. In this work, we introduce STILO, a MO...

---

### 4. ReDIL-GNN: Resynthesis Domain Incremental Learning for Circuit Graph Neural Networks

**Authors:** Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18595v1)

**Summary:** Logic resynthesis preserves circuit functionality while changing gate vocabulary, topology, and structural statistics, creating domain shift for circuit graph neural networks (GNNs) without changing task labels. To study this setting, we introduce ReDIL-GNN, a resynthesis domain-incremental learning framework that adapts a fixed prediction or representation head as new synthesis styles arrive and evaluates retention on all previously observed domains. Because not every shift should be adapted bl...

---

### 5. The evolution of sex for artificial intelligence: a population-genetic framework for multigenerational model populations

**Authors:** Giorgio F. Gilestro

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18560v1)

**Summary:** Some aspects of AI development resemble a population process in which models are specialised, retrained on the output of peers, or combined by averaging weights. These practices lead to generations of models, in the biological sense studied by population genetics. Here, I develop this parallelism and interpret multigenerational model populations in terms of sexual and asexual reproduction, formally recombining the two fields. I test these analogies in an exact inheritance model, in trained netwo...

---

### 6. Transformation Laws in Neural Representations: Structure, Realisability, and Construction

**Authors:** Yuan Sun

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18190v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18190v1)

**Summary:** How neural representations preserve the structure of input changes connects representation analysis with internal intervention. We study operable representational content through compatible actions of reference transformations on neural features. We characterise when a transformation descends through an encoder, and give a linear setting in which the defect is governed by the transformation's demand for discarded information, measured in the metric the representation induces. On a rectifier the ...

---

### 7. Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization

**Authors:** Lu Han, Jin Wang, Yuchen Li, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18130v1)

**Summary:** Surrogate-assisted evolutionary algorithms (SAEAs) are effective methods for solving expensive optimization problems (EOPs), where surrogate models replace most expensive evaluations and critically influence the final optimization results. In recent years, tabular foundation models have advanced rapidly, and the Tabular Prior-data Fitted Network (TabPFN) has been adopted as a surrogate model for EOPs due to its strong predictive capability, demonstrating promising performance. Motivated by its p...

---

### 8. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 9. Graph neural networks for exoplanet atmospheres

**Authors:** Antonia Vojtekova, Kai Hou Yip, Ingo P. Waldmann, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17894v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17894v1)

**Summary:** Calculating disequilibrium chemistry in exoplanet atmospheres remains a significant computational bottleneck in atmospheric retrievals. The increasing observational precision from facilities such as JWST and the Ariel mission requires including disequilibrium chemistry in these analyses. Previous studies have demonstrated that neural networks can emulate kinetic chemistry, although their spatial inductive bias does not align with the topology of chemical reaction networks. This study introduces ...

---

### 10. A Spatiotemporal Extension of the Neuromorphic DBSCAN Implementation

**Authors:** Charles P. Rizzo, James S. Plank

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17357v1)

**Summary:** DBSCAN is an algorithm that denoises and clusters data. In prior work, we implemented the DBSCAN algorithm neuromorphically, introducing two constructions termed ``flat'' and ``systolic''. The ``flat'' construction prioritizes throughput, while the ``systolic'' construction trades time for space resulting in a smaller, more hardware-friendly architecture at the cost of throughput. In this work, we offer spatiotemporal extensions of these two constructions to better leverage the spatiotemporal na...

---

### 11. Machine Zygote: Causal Biparental Heredity Before Learning in a Germline--Soma Artificial Agent

**Authors:** Lyes Saad Saoud

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17300v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17300v1)

**Summary:** Artificial ontogeny, developmental encodings, robot reproduction, and inherited controllers are established research directions, yet a narrower question remains: can a newborn artificial agent exhibit measurable biparental heredity before learning, and can that dependence be isolated causally rather than inferred only from parent-offspring resemblance? We introduce Machine Zygote, a computational germline-soma architecture designed to test this question. Two parental germlines are independently ...

---

### 12. Event-based Selective Attention for Multi-resolution Fast Region of Interest (ROI) Detection

**Authors:** Luca Peres, Giulia D'Angelo, Chiara Bartolozzi, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17134v1)

**Summary:** Neuromorphic vision systems operate under strict constraints on bandwidth, memory, and energy, particularly at the edge, motivating early mechanisms for data reduction and selective processing. In this work, we investigate a multi-scale training-free, saliency-based, bottom-up visual attention model that operates directly on low-resolution event-based input and selects Regions of Interest (ROI) from the visual scene. The model is evaluated across multiple downscaling factors applied to the incom...

---

### 13. Bio-Inspired Palette Evolution in Indirectly Encoded Substrates: Timescale Compatibility Shapes Activation Function Discovery

**Authors:** Romain Claret, Michael O'Neill, Paul Cotofrei, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17067v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17067v1)

**Summary:** Indirectly encoded neural networks can assign different activation functions to individual nodes, but the right functions are rarely known in advance. When the available set contains only standard monotonic functions, problems like parity become unsolvable, yet an all-inclusive palette underperforms a curated one. How should evolution discover which functions to use? We address this as a meta-learning problem, designing 13 strategies (11 inspired by biological adaptation mechanisms, plus baselin...

---

### 14. Neuro-Symbolic Hierarchical Intention Anticipation in Human Behavior

**Authors:** Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17064v1)

**Summary:** Assistive autonomous systems must anticipate human goals before an observed behavior is complete. This article formulates anticipation as goal inference from a partially observed multimodal episode together with structured prediction of the remaining behavior, rather than exact motor forecasting. A compact Hierarchical Planning Decoder (HPD) is attached to a frozen neuro-symbolic recognition encoder and predicts, at four ontological levels, the next actions, the remaining activities and low-leve...

---

### 15. LLMDE: A Large Language Model-Driven Differential Evolution Algorithm for Portfolio Optimization

**Authors:** Rong Chai, Vaclav Snasel, Xiaopeng Wang, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16846v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16846v1)

**Summary:** This study proposes a Large Language Model-Driven Differential Evolution (LLMDE) algorithm to reduce the reliance on handcrafted hyperparameter design. The proposed algorithm leverages a prompt engineering strategy, allowing large language models (LLMs) to dynamically select mutation strategies and configure control parameters guided by optimization feedback, thus enhancing the performance of the DE algorithm. We evaluate the performance of LLMDE on the CEC2022 benchmark suite, comparing it with...

---

### 16. Information Geometric Self-Organization at the Edge of Stability in High-Capacity Kernel Associative Memories

**Authors:** Akira Tamamori

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16827v2) | 📄 [PDF](https://arxiv.org/pdf/2609.16827v2)

**Summary:** High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit exceptional storage capabilities and robustness. Previous empirical studies identified a hyperparameter regime, the "Ridge of Optimization," where attractor stability is maximized. However, the geometric nature of this regime and the optimization dynamics required to reach it have remained unclear. In this paper, we investigate the static geometry of the parameter space and the learning trajectory of Gradient De...

---

### 17. Geometry of learning dynamics: Gradient descent versus natural gradient on the ridge of optimization

**Authors:** Akira Tamamori

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16805v2) | 📄 [PDF](https://arxiv.org/pdf/2609.16805v2)

**Summary:** High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit a "Ridge of Optimization" characterized by extreme stability and a highly skewed weight spectrum. However, the dynamical process by which learning converges to this critical regime has remained unclear. This paper provides a geometric analysis of the learning trajectories on the statistical manifold of a KLR-trained Hopfield network. By comparing the paths of Gradient Descent (GD) and Natural Gradient Descent (N...

---

### 18. Learning to Optimize UAV Path Planning for Data Sensing in Wireless Sensor Networks

**Authors:** Sijie Ma, Zeyuan Ma, Weijia Cao, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.16629v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16629v1)

**Summary:** UAVs have emerged as highly flexible platforms for data sensing in Wireless Sensor Networks (WSNs). Path planning for UAVs in such tasks plays a key role to assure remote sensing effectiveness and friendly energy consumption. However, existing approaches show two key limitations: i) they are primarily hand-crafted with certain design biases that harm adaptation on unseen tasks. ii) they predominantly assume idealized spatial complexities of actual environments through simplified simulation, caus...

---

### 19. Scaled Hippocampus-inspired Neural Networks on Neuromorphic Memristive Hardware

**Authors:** Joseph A. Kilgore, Jeffrey D. Kopsick, Zahin Ahmed, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16429v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16429v1)

**Summary:** The hippocampus, a key brain region for learning and memory, exhibits rich structural diversity, sparse communication, and robust dynamics with incredible energy efficiency. It offers promising insights for novel computing capabilities, particularly when co-designed with emerging hardware technologies. In this work, we draw inspiration from the rodent CA3 hippocampal subregion to develop the first spiking neural network with neuronal diversity and biologically-realistic resting state dynamics de...

---

### 20. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation

**Authors:** Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16217v1)

**Summary:** Astrocytes are non-neuronal glial cells that are receiving widespread attention due to their emerging role in neural computation. In this paper, we propose and study dynamical mechanisms by which astrocytes may augment the ability of neural networks to infer context in reinforcement learning (RL) settings. We construct a biologically inspired, two-level dynamical neural-astrocyte network with distinct spatial and temporal organization. We train this model on a hierarchical multi-context task tha...

---

### 21. Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability Preservation

**Authors:** Gautam Kishore

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16145v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16145v1)

**Summary:** We study a practical question: can a small correction module fix errors in a frozen language model's outputs without degrading its base capabilities? We propose CRN v2, a lightweight logit-level correction module (~34M trainable parameters, 0.73% of the 4.65B text module) that sits atop a fully frozen Gemma 4 E2B model. The base model is never updated; only the correction module learns, via supervised fine-tuning followed by reference-free DPO on 83,400 error-correction pairs. On a 60-question d...

---

### 22. HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses

**Authors:** Jieyuan Liu, Mengzhou Hu, Jefferson Chen, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15938v1)

**Summary:** Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore ...

---

### 23. Event-Native Symbolic-Temporal Spike Encoding Framework for Heterogeneous Cyber Streams

**Authors:** Dalton Diez, Peyton Andras, Max Shroyer, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15772v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15772v1)

**Summary:** Spiking neural networks (SNNs) have shown promise for sparse, event-driven computation through stateful processing that is naturally compatible with low-power edge hardware. These properties align with cyber monitoring, where data arrives asynchronously, and malicious behavior often emerges through temporal patterns across event sequences. However, cyber streams are not composed solely of continuous numeric signals: their informative structure is also carried by categorical identifiers, irregula...

---

### 24. Complete Suffix Prediction for Recommendation via Latent Retrieval over Process Graphs

**Authors:** Sarra Madad, Myriam Maumy, Fr{é}d{é}ric Bertrand, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15692v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15692v1)

**Summary:** Complete suffix prediction is challenging in sequential decision settings, where the same prefix can remain compatible with several plausible suffixes. We propose a graphbased metric-learning framework that reformulates complete suffix prediction as latent retrieval over process graphs. Prefixes and suffixes are represented as directed attributed graphs and encoded by edge-conditioned graph neural networks, allowing event-level activities and transition-level durations to be modelled jointly. Pr...

---

### 25. Big Brains and Changing Environments: Cause or Consequence?

**Authors:** Sian Heesom-Green, Jonathan Shock, Geoff Nitschke

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15569v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15569v1)

**Summary:** Large brains are metabolically costly, and associations with changing environments do not imply they evolved there, as the Cognitive Buffer Hypothesis (CBH) would suggest. They may instead evolve in stable conditions and later facilitate colonization of changing environments. Using neuro-evolution in an artificial seasonal foraging task, we compared agents evolving exclusively in changing environments to agents first evolved in static environments before transitioning. Results show that larger n...

---

### 26. A Memristive Synapse for Online STDP Learning and Inference in SNNs

**Authors:** Elia Mateu-Barriendos, Álvaro Gómez-Pau, Daniel Arumí, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15339v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15339v1)

**Summary:** This work presents a fully analog memristive synaptic circuit for online spike-timing-dependent plasticity (STDP) learning in spiking neural networks (SNNs). The proposed synapse integrates a local STDP circuit generating gradual timing-dependent conductance updates directly from pre- and post-synaptic spikes. Learning occurs during normal network operation without requiring external digital control or explicit STDP waveform synthesis.   Post-layout simulations of the memristive synapse implemen...

---

### 27. Ensemble-Conditioned Molecular Design

**Authors:** Ross Irwin, Alessandro Tibo, Jon Paul Janet, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15077v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15077v1)

**Summary:** Molecular design is typically approached as a problem of finding molecules which can adopt a single bioactive conformation. In reality, molecules occupy a distribution over conformations, and many of the properties which determine whether a candidate is viable depend on that distribution rather than on any single conformer. We reframe molecular design as an optimisation of both the modes and properties of molecules' conformational ensembles, where modes can be represented as shapes, pharmacophor...

---

### 28. Sensory Precision Inference for Multimodal Arbitration under Uncertainty

**Authors:** Tin Mišić, Takato Horii

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15065v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15065v1)

**Summary:** Autonomous agents operating on multisensory data cannot assume that all sensory modalities remain consistently informative. In real environments, sensory streams are frequently corrupted by noise, missing data, or inter-modal incongruence, requiring adaptive arbitration between competing sensory hypotheses. While active inference provides a principled framework for uncertainty-guided inference, the role of dynamically inferred sensory precision in generative multimodal arbitration under sensory ...

---

### 29. The Cost of Becoming: Developmental Encoding Increases Phenotypic Diversity but Reduces Locality and Recombination Robustness in Evolved Robots

**Authors:** Lyes Saad Saoud

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.17606v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17606v1)

**Summary:** Developmental encodings are often motivated by the expectation that a structured genotype-to-phenotype process can improve evolvability, robustness, and adaptation. Yet an encoding that expands phenotypic variation may simultaneously make useful parental structure harder to preserve under mutation and recombination. We test this trade-off in a controlled evolutionary-robotics benchmark comparing three matched representations: direct encoding, a static generative encoding, and a temporal zygotic ...

---

### 30. When is global evolutionary search useful for variational quantum algorithms? A landscape-first study

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14594v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14594v1)

**Summary:** Variational quantum algorithms recast state preparation as classical nonconvex optimization, but it is often unclear when multistart local search suffices and when population-based global search justifies its evaluation cost. Using a landscape-first design, controlled QAOA experiments identify two mechanisms making local search unreliable: parameter reuse across circuit layers and competition between 2-local and 3-local cost terms. Increasing QAOA depth alone does not replicate this effect. We t...

---

### 31. Surrogate-Assisted Genetic Programming with Phenotypic Characterisation in Dynamic Multi-Mode Project Scheduling

**Authors:** Yuan Tian, Yi Mei, Mengjie Zhang

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14418v1)

**Summary:** Dynamic multi-mode resource-constrained project scheduling requires decisions to be made under precedence constraints, limited resources, multiple execution modes, and uncertain activity durations. Genetic programming (GP) can automatically evolve heuristic rules for such problems, but its simulation-based fitness evaluation is computationally expensive. This study investigates phenotypic characterisation (PC) in surrogate-assisted GP to evolve higher-quality scheduling heuristics under a fixed ...

---

### 32. Early-Stopping Thresholds for ES-HyperNEAT: A Data-Driven Approach from Fitness Dynamics

**Authors:** Romain Claret, Arthur Gygax, Michael O'Neill, et al.

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13533v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13533v1)

**Summary:** Most hyperparameter configurations for Evolvable-Substrate HyperNEAT (ES-HyperNEAT) produce networks that stagnate at random-guessing performance, wasting computational resources. We frame early stopping as binary classification on early fitness trajectories: for each trial, we compute the cumulative median of best-per-generation fitness and test it against a threshold derived by maximizing the F1 score on an initial 90-trial dataset. The resulting rule (generation G* = 3, threshold T* = 0.140) ...

---

### 33. nBMS, a Neuromorphic Battery Management System with a Silicon-Validated Spiking State-of-Charge Core for eVTOL Aircraft

**Authors:** İsmail Can Dikmen

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13506v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13506v1)

**Summary:** State-of-charge (SoC) estimation for electric vertical take-off and landing (eVTOL) aircraft must run on the vehicle under hard energy and certification budgets, on a duty cycle unlike anything in the automotive literature. In this study an event-driven spiking network, the state-estimation core of the nBMS neuromorphic battery management architecture, is designed for per-timestep SoC estimation and evaluated on a public 22-cell eVTOL dataset with an automotive cross-check. A delta and populatio...

---

### 34. Evolutionary Ensemble Search: Council-Guided Program Evolution with Persistent Memory

**Authors:** Juan P. Madrigal-Cianci, Eshan Chordia

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.17590v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17590v1)

**Summary:** Evolutionary Ensemble Search (EES) constructs machine-learning procedures through expert-guided program evolution. A role-specialized council turns task evidence and experimental results into structured search directions. An orchestrator allocates these directions to execution specialists and an evolutionary engine. The engine selects measured parents, diagnoses their errors, and produces descendants through code mutation, structured pipeline edits, and crossover. Each child must execute and acq...

---

### 35. Real-time Learning and Evolution in Robotic Art Installations

**Authors:** Sofian Audry, Stephen Kelly

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13352v1)

**Summary:** We present three robotic art installations which explore the aesthetics of adaptive behavior. Through embodied machine leaning and digital evolution, these works draw viewers into an artificial ecosystem in which open-ended novelty, trial-and-error learning, competition, and cooperation emerge in real time. Research-creation practices are examined in relation to these works, focusing on how they redefine the role of artists within a human-machine collective while examining points of convergence ...

---

### 36. MAAPO:an innovative membrane algorithm based on artificial protozoa optimizer for multilevel threshold image segmentation

**Authors:** Xiaopeng Wang, Vaclav Snasel, Seyedali Mirjalili, et al.

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.12756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.12756v1)

**Summary:** This paper proposes a novel membrane algorithm based on artificial protozoa optimizer (MAAPO) for global optimization problems. The artificial protozoa optimizer (APO) is adopted as the base meta-heuristic algorithm due to its novelty and competitive performance. MAAPO integrates two key innovations:(1) a membrane computing (MC) framework that introduces a parallel distributed paradigm to improve population diversity and search dynamics, and (2) an enhanced autotrophic model within APO that uses...

---

### 37. Signed Sensitivity of Expected Hitting Time to Mutation Rate in the (1+1) EA: Per-State Sign Theorems and Verifiable Certificates for Non-Lumpable Families

**Authors:** RenKai Wang

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.12510v1) | 📄 [PDF](https://arxiv.org/pdf/2609.12510v1)

**Summary:** For the (1+1) evolutionary algorithm with standard bit mutation, we study the sensitivity of the expected hitting time $H_p=\mathbb{E}_x T$ to the mutation rate. We first point out an easily overlooked formalization pitfall: the improvement event is not monotone in the mutation mask, so the unsigned (total-influence) form of the Margulis-Russo formula does not apply; the correct object is the signed endpoint difference. Second, we give an exact three-dimensional separation: two fitness functions...

---

### 38. T-GADE: Thermodynamical Generative-AI-Driven Evolution of LLM Artifacts

**Authors:** Kyoko Ogawa, Naoki Mori

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.12286v1) | 📄 [PDF](https://arxiv.org/pdf/2609.12286v1)

**Summary:** Integrating evolutionary computation and large language models (LLMs) requires control of population diversity as well as generative capability. Among LLM outputs, those with explicit structure, such as a description paired with code, are structured artifacts; we use artifact for short. We propose T-GADE, which evolves these artifacts by extending thermodynamical genetic algorithms through LLM-based genetic operators and artifact-level diversity evaluation. A common free-energy objective support...

---

### 39. Feasibility and Memory Mechanisms of Chern-Simons Context Reservoir Computation

**Authors:** Jyotiranjan Beuria, Venkatesh H. Chembrolu

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.13315v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13315v1)

**Summary:** We investigate whether a Chern-Simons (CS) context reservoir is a viable computational substrate and whether evolving its gauge connection provides a benefit beyond simpler mechanisms. The reservoir state is a density fluctuation on a two-dimensional context manifold, whose drift is generated by a density-sourced connection. To separate generic reservoir behavior from gauge-specific effects, we compare four matched models: reciprocal transport, instantaneous transverse reconstruction, local nonl...

---

### 40. Predicting Privacy Leakage from Weight Spectral Density

**Authors:** Richard J. Preen, Jim Smith

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11780v1)

**Summary:** Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive shadow models, making large-scale privacy evaluation impractical. In this work, we investigate whether inexpensive spectral metrics derived from the heavy-tailed self-regularisation framework can serve as proxies for MIA vulnerability. We evaluate several WeightWatcher spectral metrics on image and...

---

### 41. Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based Neuroevolution

**Authors:** Romain Claret, Arthur Gygax, Michael O'Neill, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11518v1)

**Summary:** Evolvable-Substrate HyperNEAT (ES-HyperNEAT), a bio-inspired indirect encoding that determines neuron placement and connection weights from spatial coordinates, exhibits a failure mode on MNIST as a diagnostic benchmark. Because input pixels map to a coordinate space centered at the origin, evolved networks converge on a small central cluster of input pixels, a spatial-concentration bias; prior work observed only 21% mean accuracy in this regime. Is this bias an optimization artifact or an archi...

---

### 42. GeoTrussRover: Morphological Computation with Contact-Semantic Control Primitives

**Authors:** Muyuan Ma, Yi Zhang, Yang Yang, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11361v1)

**Summary:** Reconfigurable robots can change their contact geometry when a fixed body cannot negotiate an obstacle. A variable-geometry truss (VGT) distributes this shape change through a load-bearing structure, but coupling it to a mobile base creates a high-dimensional coordination problem. GeoTrussRover combines an electrically actuated VGT, a wheeled base, and contact-semantic morphology planning and control. We solve one source traversal and extract four contact-semantic primitives that describe coordi...

---

### 43. Solving Few-Shot Multiobjective Multitask Optimization via Iterative Sequential Transfer

**Authors:** Tingyang Wei, Haofeng Wu, Ananda Phan Iman, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11228v1)

**Summary:** Applying knowledge transfer across multiple optimization tasks, multitask optimization (MTO) emerges as a promising approach to solving synergistic optimization tasks simultaneously. However, the development of effective knowledge transfer mechanisms in MTO fundamentally relies on aligning elite solution distributions across tasks. This dependency creates a critical bottleneck in few-shot optimization regimes, as restricted evaluation budgets impede the identification of elite solution distribut...

---

### 44. Phases in a class of associative memories via hidden neurons

**Authors:** Toshihiro Ota, Masato Taki

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10976v1)

**Summary:** Associative memory in the Hopfield network is attractor dynamics in a disordered many-body system, and higher-order and exponential extensions turn its retrieval update into softmax attention. The polynomial and exponential regimes have been analyzed by different methods, with no common architecture in which to ask what fixes the storage scale. In this paper we study the bipartite architecture of Krotov and Hopfield, which we call the class $H$, whose model is fixed by a Lagrangian for each laye...

---

### 45. Fractional-order hardware for neuromorphic computing: Is the order really the problem?

**Authors:** Christof Teuscher

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10882v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10882v1)

**Summary:** Does a neuromorphic system need a true power-law memory kernel, and if so, can anyone build one? Neuromorphic systems process signals spanning many timescales at once, from milliseconds to tens of seconds. Integer-order circuits buy each additional timescale with an additional state variable. Fractional-order dynamics offer a different bargain: one operator whose power-law kernel carries a continuum of timescales, tuned by one parameter, the order alpha. A fractional derivative is non-local, so ...

---

### 46. Training Trajectories Determine Circuit Removability in Annealable Soft-Prior Transformers

**Authors:** Zonglin Yang, Ziming Zhao, Wei Tang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10287v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10287v1)

**Summary:** Soft positional priors can help small Transformers learn retrieval circuits, but it is unclear whether the resulting circuits remain functional once the prior is removed. We test this with an annealable soft-prior Transformer whose attention biases can be learned, faded, or zeroed during training and evaluation. On associative recall, unforced models perform well with the prior active ($0.772 \pm 0.020$) but collapse at zero gate ($0.095 \pm 0.009$). Smooth fade-to-zero training preserves high z...

---

### 47. Structural Fusion of Bayesian Networks with Limited Treewidth Using Genetic Algorithms

**Authors:** Pablo Torrijos, José A. Gámez, José M. Puerta

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10276v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10276v1)

**Summary:** This paper introduces an evolutionary computation approach for consensus in structural Bayesian Network (BN) fusion under the constraint of limited treewidth. The consensus BN aims to reconcile multiple input BNs into a single one that retains key structural features present in the original networks. Treewidth, a graph-based parameter associated with computationally tractable inference, is utilized to restrict the complexity of the resulting network. A genetic algorithm is proposed to look for a...

---

### 48. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 49. Teacher Geometry Shapes Learnability in Teacher-Student Networks

**Authors:** Kai J. Sandbrink, Flavio Martinelli, Alexander van Meegen, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09595v1)

**Summary:** Teacher-student systems, in which a teacher neural network generates training labels so that a student neural network can learn to implement the same function, are widely used as an abstract setting to study learning. However, the structure of the teachers is often overlooked by assuming randomly-generated, normally-distributed parameters. This hides substantial variation in how learnable different teachers are. We formalize learnability as the success rate of converging to the global minimum, a...

---

### 50. Robust Industrial Cyber Physical Classification Using Neuromorphic Temporal Embeddings and Hybrid SNN XGBoost Under Machine Unlearning Attacks

**Authors:** Ammar Kamoona, Sajad Koushkbaghi, Mahdi Jalili, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09564v1)

**Summary:** The digitalisation of electrical distribution networks has increased the exposure of power-grid infrastructure to cyber attacks. Existing intrusion detection systems (IDSs), however, often rely on computationally expensive deep learning models that are difficult to deploy at the edge. Periodic retraining also exposes these systems to machine unlearning attacks, where selective data removal can degrade detection performance. We propose a hybrid Spiking Neural Network (SNN) and XGBoost architectur...

---

## q-bio.NC

**50 papers**

### 1. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

### 2. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 3. Learning Options for Compositional Motor Control with Adapter Banks

**Authors:** Sreejan Kumar, Marcelo Mattar, Lea Duncker

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17042v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17042v1)

**Summary:** Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, ...

---

### 4. Predictor Construction Can Reverse Multimodal Neural Contrasts

**Authors:** Lucas Nadolskis, Galen Pogoncheff, Michael Beyeler

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16430v1)

**Summary:** Foundation-model features are increasingly used to ask what information neural activity represents, often by comparing prediction gains between nested encoding models. We show that such multimodal contrasts can change sign when only the conditioning predictor is reconstructed. Using fMRI from the Natural Scenes Dataset, DINOv2 visual features, and MPNet embeddings of MS COCO captions and Localized Narratives, a caption-narrative contrast in the additional predictive contribution of vision favors...

---

### 5. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation

**Authors:** Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16217v1)

**Summary:** Astrocytes are non-neuronal glial cells that are receiving widespread attention due to their emerging role in neural computation. In this paper, we propose and study dynamical mechanisms by which astrocytes may augment the ability of neural networks to infer context in reinforcement learning (RL) settings. We construct a biologically inspired, two-level dynamical neural-astrocyte network with distinct spatial and temporal organization. We train this model on a hierarchical multi-context task tha...

---

### 6. Decision-Related Cognitive Signatures from Fast-Slow Dynamics: A Low-Dimensional Observation-Operator Framework

**Authors:** Furkan Emre Isik, Ali Demirci

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15918v1)

**Summary:** Repeated decisions exhibit temporal structures such as persistence, direction-dependent switching, recurrent alternation, and abrupt transitions. We examine the generative sufficiency of a two-dimensional fast-slow dynamical system. The system combines a cubic fast equation with linear slow feedback and is analyzed through its equilibrium geometry, trace-determinant structure, equilibrium-fold loci, candidate Hopf boundaries, and singular critical manifold. An explicit observation operator proje...

---

### 7. When Teachers Smile or Frown: A Profile-Based Analysis of Achievement Emotions

**Authors:** Rudra Mukhopadhyay, Satyaki Mazumder, Koel Das

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15747v1)

**Summary:** Achievement emotions shape how students engage with and learn from academic tasks, yet most studies examine individual emotions rather than co-occurring affective profiles and their dynamics. We examined latent achievement-emotion profiles and their transitions following exposure to different instructor facial expressions during a video lecture. Self-reported data from 78 Grade VII and VIII students revealed three profiles: enthusiastic, demotivated, and vulnerable. Profile transitions differed ...

---

### 8. Nonlinear dynamics of random neural networks with second-order synaptic motifs

**Authors:** Jun Yang, Hannah Choi

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14251v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14251v1)

**Summary:** Classical theories of random neural networks typically assume independent connectivity, overlooking the local motif structures prevalent in biological circuits. Here, we investigate how four second-order synaptic motifs (chain, reciprocal, convergent, and divergent) shape the dynamics of nonlinear firing-rate networks. While previous studies have established that chain correlations generate outlier eigenvalues, we demonstrate that these motifs also jointly reshape the Jacobian eigenvalue bulk. U...

---

### 9. URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining

**Authors:** Po-Han Chiang

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13899v1)

**Summary:** The BabyLM challenge measures how much language a model can learn from developmentally-plausible, child-scale data rather than internet-scale corpora, yet prior language models forgo the biological constraints of the neural circuitry that acquires human language: spiking neurons separated into excitatory and inhibitory populations wired by a recurrent lateral connectome. This paper presents URCHIN (Unified Recurrent Connectome with Horizontal Integrate-and-fire Neurons), which applies the Parall...

---

### 10. Hierarchical emergence of network bursting in a four-cell central pattern generator model

**Authors:** Krishna Pusuluri, Huiwen Wu, Andrey L. Shilnikov

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13858v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13858v1)

**Summary:** How can a neural circuit rhythmically burst when none of its constituent neurons can endogenously do so? We address this question through a bottom-up reconstruction of a 4-cell neural circuit modeled after the swim central pattern generator (CPG) of the sea slug \textit{Dendronotus iris}. We first map the intrinsic regimes of a swim interneuron (SiN) model neuron and show that slow mutual inhibition can generate anti-phase bursting in a half-center oscillator (HCO) assembled from tonic-spiking o...

---

### 11. Pretraining for Sample-Efficient Neural Interfaces

**Authors:** Ben Tang, Zachary Spalding, Gregory B. Cogan

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13507v1)

**Summary:** Brain-computer interfaces (BCIs) decode neural activity to restore lost function. Typically, training a high-performance neural decoder requires a large labeled dataset to be collected from every new subject. One way to reduce the labeled data cost is self-supervised pretraining, which learns general neural representations from unlabeled recordings that accumulate across subjects. However, for intracranial electroencephalography (iEEG) recordings, self-supervised learning has been challenging du...

---

### 12. Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes

**Authors:** Bilal Ahmed, Heather Cihak, Gregory Handy

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13074v1)

**Summary:** The maintenance of continuous variable information in working memory is thought to rely on persistent patterns of cortical activity. In delayed-estimation tasks, neural activity can form localized activity peaks, or ``bumps,'' whose positions track the remembered variable. Such activity is well described by continuous-attractor neural field models, but most existing models collapse cortical inhibition into a single homogeneous population. Here, we introduce a stochastic neural field model with d...

---

### 13. pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches

**Authors:** M. Marzulli, A. Angiolelli, C. Mannino, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11530v1)

**Summary:** The analysis of neuronal avalanches offers insights into brain dynamics utilizing the framework of criticality, but the reproducibility and comparability of studies are limited by the use of fragmented, lab-specific scripts. To address this issue, we introduce pyAvalanches, an open-source Python package providing a standardized, end-to-end pipeline for avalanche analysis from electrophysiological recordings (e.g., electroencephalography-EEG). Starting from the detection of neuronal avalanches th...

---

### 14. Degeneracy along the sensorimotor hierarchy: motor control within a framework larger than redundancy

**Authors:** Florent Paclet, Paul Duprat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11325v1)

**Summary:** Motor control has described the surplus of solutions available to the nervous system as redundancy, a term that names duplication: interchangeable elements, robust to loss but incapable of differential adaptation. Biology has had a second term for twenty-five years. Degeneracy names elements that are not interchangeable and are nonetheless isofunctional with respect to a given output, and it supports adaptability, since non-identical elements necessarily diverge in some context. Circuit neurosci...

---

### 15. The Platonic brain bridge hypothesis: human brain networks as an architectural prior for multimodal large language models

**Authors:** Pengfei Zhang, Biao Tian, Xiangang Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10947v2) | 📄 [PDF](https://arxiv.org/pdf/2609.10947v2)

**Summary:** Multimodal large language models predict brain activity, but brain alignment has been a measurement, not a design tool. We propose the Platonic brain bridge hypothesis: omni models, multimodal large language models that process video, audio and text jointly, converge on brain-like representations usable in both directions. From model to brain, brain-likeness of seven omni models is stable across participants, rises with every input channel in three bases, and our encoders lead the Algonauts 2025...

---

### 16. Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model

**Authors:** Daniel Semchin, Emile d'Angremont, Hao Ding, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10890v1)

**Summary:** Parkinson's disease is clinically and biologically heterogeneous, yet its spatiotemporal progression remains poorly characterized. We present a connectome-constrained disease progression model that jointly estimates subject-specific disease time and data-driven subtypes from longitudinal morphometry. Applied to 85 imaging and clinical biomarkers from the Parkinson's Progressive Markers Initiative (PPMI) cohort, the model recovers four morphologically distinct progression subtypes. We validate th...

---

### 17. Cortical information transfer reveals conserved hemispherical network dynamics across human handedness

**Authors:** Yago Emanoel Ramos, José Garcia Vivas Miranda

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10870v1)

**Summary:** Whether human motor and brain lateralization arises from fundamentally distinct neural architectures or emerges from conserved network dynamics remains a central question at the intersection of network science and neurobiology. Conventional measures of cortical activation often fail to resolve how directed information exchange adapts to manual preference during complex motor tasks. This ambiguity leaves it unclear whether left-handed individuals possess atypical neural organization or follow sha...

---

### 18. BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10518v1)

**Summary:** fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain...

---

### 19. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 20. EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding

**Authors:** Muchen Li, Anglin Liu, Xuetian Gao, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09728v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09728v1)

**Summary:** Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by s...

---

### 21. The Computational Primitives of Adaptation

**Authors:** Jonathan W. Page

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.11989v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11989v1)

**Summary:** Research on adaptive systems has traditionally focused on behavior (what organisms do) and mechanism (how their machinery works). This paper focuses on a third level, computation, which considers what adaptive systems must compute to survive and reproduce. It is proposed that adaptation has its own computational structure, comprising a small set of primitive operations common to all adaptive systems, regardless of their physical form. Six primitives, Arouse, Orient, Valence, Position, Boundary, ...

---

### 22. Emergence of criticality in models of real neurons

**Authors:** David P. Carcamo, Christopher W. Lynn

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09438v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09438v1)

**Summary:** Critical systems sit near boundaries between qualitatively distinct behaviors. When inferring models of neural activity, this proximity to criticality is thought to require the precise tuning of parameters. Here, we show that as the number of neurons increases, criticality can emerge naturally without fine-tuning. When computing observable statistics from parameters (the forward problem), some small regions in parameter space map to large regions in statistics space. These special parameters are...

---

### 23. XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

**Authors:** Yang Qiao, Junjie Wu, Deqiang Qiu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09388v1)

**Summary:** Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional co...

---

### 24. Hi-M imaging of chromatin architecture in adult Drosophila brain cryosections

**Authors:** Christel Elkhoury Youhanna, Julie Garona, Marie Schaeffer, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08776v1)

**Summary:** Hi-M combines fluorescence in situ hybridization (FISH), automated microfluidics, sequential imaging, and computational chromatin tracing to measure the three-dimensional organization of selected genomic regions in single cells. This chapter describes a Hi-M workflow adapted for cryosections of adult Drosophila melanogaster brains, enabling chromatin tracing while preserving tissue architecture and cell identity. The protocol covers Oligopaint library design and amplification, fixation, brain di...

---

### 25. Why shared attention vectors fail: a case for outcome-indexed tuning

**Authors:** Lenard Dome

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08615v1)

**Summary:** Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for ...

---

### 26. An Evidence-Aware Framework for EEG Microstate Analysis: Improved Sensitivity to Alzheimer's Disease and Ageing

**Authors:** Kaidong Wu, Haili Ye, Ptolemaios G Sarrigiannis, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08500v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08500v1)

**Summary:** Electroencephalography (EEG) microstate analysis commonly converts each scalp topography into a winner-take-all hard label and summarises the resulting sequence using duration, occurrence, coverage, transitions, and symbolic complexity. Although interpretable, this readout discards evidence strength, assignment ambiguity, and low-confidence periods. We introduce a template evidence trajectory framework that retains, at each sampled Global Field Power (GFP) peak, the evidence for all templates or...

---

### 27. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**Authors:** Xiangnan Zhang, Jingxin Liu, Ranqi Lu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08070v2) | 📄 [PDF](https://arxiv.org/pdf/2609.08070v2)

**Summary:** The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historica...

---

### 28. Fisher-Rao Distance Detects Shifts in Kinematic Profiles under Cognitive Load

**Authors:** Joseph Vero, Elizabeth B Torres

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07696v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07696v1)

**Summary:** Motor control research involves the study of movement kinematics derived from the positional trajectories that complex motions describe. In natural, unconstrained motions requiring cognitive and memory processes in real time, the temporal speed profiles are not bell-shaped, may have multiple maxima and the peaks distribution is best fit by the continuous gamma family with two parameters, the shape and the scale. As the stochastic processes described by complex motion trajectories are non-station...

---

### 29. Fisher Information Metric as a model-free measure of proximity to criticality in neural systems

**Authors:** Yuewei Du, Alberto Liardi, Hardik Rajpal, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07624v1)

**Summary:** Critical phenomena are widespread across many disciplines and have recently become a topic of deep interest in the study of biological and artificial neural networks. A distinct signature of criticality is the emergence of avalanches with power-law-distributed sizes and durations. However, empirically estimating the critical exponents remains challenging, and their interpretation is often model-dependent. In this work, we demonstrate how the Fisher Information Metric (FIM), a measure of generali...

---

### 30. Homeostasis Revisited and Reformulated Through Hidden Markov Model Control

**Authors:** Rubén Moreno-Bote

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07508v1)

**Summary:** A common formalization of homeostasis is the free energy principle, a framework that defines a set of desired observation values, or critical states, that the agent should reach or remain close to. Under the free energy principle, an agent should act to maximize the probability of receiving the desired observations. Here we revisit the common approach of solving the problem of maximizing the log probability of the desired observations by maximizing a variational lower bound, the so-called negati...

---

### 31. Revisiting the Aerts-Broekaert-Smets quantum model of the liar paradox

**Authors:** Massimiliano Sassoli de Bianchi

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09228v1)

**Summary:** The quantum model of the two-sentence liar paradox proposed by Aerts, Broekaert, and Smets is an early example of the use of quantum formalism to describe cognitive dynamics. Our reconstruction is primarily pedagogical in intent, but it also leads to a number of clarifications, and to some new observations, concerning the structure of the model. Rewriting the model in Dirac notation, we make explicit the distinction between truth values originating from a decision and from semantic inference, an...

---

### 32. Determinants of hyperparameter robustness in connectome reservoir computing

**Authors:** Miles Walter Churchland, Raul de Palma Aristides, Jordi Garcia-Ojalvo, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07355v1)

**Summary:** Reservoir computing provides a controlled setting for studying how recurrent network architectureshapes computation: input signals are projected into a high-dimensional state space by a fixed nonlinear dynamical system, and only the readout is trained. However, reservoir performance can be dependent on hyperparameters; this paper asks which recurrent network features support robustness to those parameter changes. We characterize computational performance using memory capacity (MC), truncated sin...

---

### 33. Adaptive Entangled Game Modules in Artificial General Intelligence

**Authors:** Haochen Li, Xinshuai Guo, Jingdong Ouyang, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09226v1)

**Summary:** We introduce a probability-wave framework for modeling the collective behavior of interacting adaptive agents, deriving testable eigenmodes through a generalized behavioral intelligence (GBI) nonlocal probability-wave equation. This framework captures a broad range of human intelligence behaviors with analytical mechanisms and offers an indirect method to examine the Liu-Chen-Ao (LCA) hypothesis of nonlocal entangled nerve fibers in the brain through collective trader behaviors. Our empirical an...

---

### 34. Formation of structural attractors in neuromorphic systems

**Authors:** Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin, et al.

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.06826v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06826v1)

**Summary:** This paper examines the theory of Invariant Structural Learning (ISL), which proposes a non-optimization approach to concept formation. Learning is interpreted as convergence to structural attractors in a hypergraph space, rather than as the minimization of a global loss function. The paper presents the ISL model, including its mathematical formalization, computational verification, and a hypothetical neurobiological interpretation. The mathematical section introduces the formal apparatus of the...

---

### 35. A Roadmap for MEG Foundation Models

**Authors:** Philipp Thölke, Hamza Abdelhedi, Yorguin Mantilla-Ramos, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04461v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04461v1)

**Summary:** Foundation models are beginning to reshape brain-signal analysis by moving the field beyond task-specific decoding pipelines toward reusable models pretrained on broad neural datasets. Magnetoencephalography (MEG) is a compelling but still underdeveloped target for this shift: it captures human cortical dynamics at millisecond resolution while offering stronger spatial interpretability than EEG, making it especially valuable for source-resolved studies of perception, language, cognition, and cli...

---

### 36. Axonal delay dispersion decides whether a neuron detects an event or a sequence, and predicts cortical column diameter

**Authors:** Cheng Bi, Jipeng Sun

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04195v1)

**Summary:** Cortical neurons fire sparsely -- often fewer than one spike per sensory window -- making rate coding insufficient and temporal coding a necessity. That conduction delays convert firing order into synchrony is long established. What governs which class of temporal feature a neuron detects -- one volley of coincident input, or two in a particular order -- has not been examined. We propose a delay-signature framework in which the axonal conduction delays converging on a dendritic branch constitute...

---

### 37. Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks

**Authors:** Shivang Rawat, Mirko Morello, Flaviano Morone, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.04134v1)

**Summary:** Temporal integration gives continuous-time recurrent networks memory, but in deep stacks it also delays bottom-up signals and attenuates top-down errors. We develop Recursive Quadrature Filters (RQFs), biologically motivated complex-valued temporal filters that are a special case of diagonal state-space models (SSMs), and ask whether this failure mode can be addressed by making each layer's bottom-up input prospective. Starting from an energy model, we derive the RQF dynamics and show that each ...

---

### 38. High-Order Triadic Functional Connectivity in the Brain and Beyond

**Authors:** Qiang Li, Masoud Seraji, Yu-Ping Wang, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03987v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03987v1)

**Summary:** Here, we report high-order functional network connectivity as a promising way for studying the brain connectome. Traditional functional connectivity approaches capture only pairwise relationships between brain regions, overlooking complex multivariate dependencies that underlie cognition and behavior. First, we demonstrated that high-order interactions capture more information and can distinguish between resting-state and task-state brain activity. Second, we introduce a matrix-based entropy-fun...

---

### 39. Inferring Affective Consciousness in an Artificial Agent: A Case Study

**Authors:** Mark Solms, St John Grimbly, Bruce Bassett, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03883v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03883v1)

**Summary:** Creatures that display 'hedonic place preference behaviour' are thought by many scientists to experience feelings, on the assumption that their attraction to pleasure-producing substances which lack nutritional value (e.g. cocaine, morphine) cannot easily be attributed to unconscious instinctual behaviour. In this paper, we discuss how a simple artificial agent that instantiates attributes of an affective system engaging in felt uncertainty about its intrinsic needs in relation to environmental ...

---

### 40. Tensor-based Brain Surface Modeling and Analysis

**Authors:** Moo K. Chung, Keith J. Worsley, Steve Robbins, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.03302v1) | 📄 [PDF](https://arxiv.org/pdf/2609.03302v1)

**Summary:** We present a unified computational approach to tensor-based morphometry in detecting the brain surface shape differences between two clinical groups based on magnetic resonance images. Our approach is novel in a sense that we combined surface modeling, surface data smoothing and statistical analysis in a coherent unified mathematical framework. The cerebral cortex has the topology of a 2D highly convoluted sheet. Between two different clinical groups, the local surface area and curvature of the ...

---

### 41. A Common Measure of Communication for Speech Brain-Computer Interfaces

**Authors:** Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02887v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02887v1)

**Summary:** Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so their reported scores are rarely comparable. Underlying this measurement problem are two unresolved ques...

---

### 42. Prediction emerges in RNNs trained for perception

**Authors:** Akanksha Gupta, Alejandro Tabas

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02739v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02739v1)

**Summary:** The brain is highly proficient at making sense of noisy and ambiguous sensory inputs. Predictive processing hypothesises that this ability relies on prediction. However, it is unclear why the brain would have evolved to predict the sensory world, a computationally expensive process, in order to aid perception. Here we use simulations to argue that prediction naturally emerges in systems optimised for perception. We train recurrent neural networks (RNNs) to denoise a tokenised version of Bach's c...

---

### 43. Fungal Memory and Minimal Cognition

**Authors:** Kristina Šekrst

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02345v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02345v1)

**Summary:** This paper argues that fungal mycelial networks exhibit minimal cognition through memory-integrated adaptive regulation. Drawing on cybernetic and enactivist frameworks, I develop a non-representational account of memory as the organism's capacity to modulate behavior based on temporally extended environmental coupling. I propose four operational criteria for minimal cognition: feedback-guided regulation of behavior, maintenance of internal viability conditions, structural modulation based on pa...

---

### 44. Mus siliconus: A Neuro-Musculoskeletal Digital Twin of the Mouse Integrating Neural Dynamics, Biomechanics, and Tactile Sensing

**Authors:** Satoshi Oota, Hideo Yokota, Hiroki Mori

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02243v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02243v1)

**Summary:** Digital twin technologies could transform neuroscience and biomedicine by creating predictive computational representations of living organisms. However, most animal digital twins model neural circuits, anatomy, or biomechanics separately rather than integrating the processes that generate behavior. We argue that animal digital twins should instead be conceived as embodied dynamical systems that unify neural activity, body mechanics, sensory feedback, and environmental interactions.   We propose...

---

### 45. Memory as an Energy Landscape---Hopfield

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02195v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02195v1)

**Summary:** This chapter reconstructs the Hopfield network as a physical theory of memory rather than merely an early neural-network algorithm. It begins with the problem as it stood before 1982-threshold logic, Hebbian association, correlation memories, and recurrent binary networks-and isolates what Hopfield's synthesis added: a dynamical definition of content-addressable memory, a symmetric recurrent architecture with a Lyapunov function, a Hebbian embedding of patterns in its couplings, and a physical a...

---

### 46. Neural Logic, Invariance, and the Retina---McCulloch and Pitts

**Authors:** Nima Dehghani

**Published:** 2026-09-02

🔗 [Paper](http://arxiv.org/abs/2609.02183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.02183v1)

**Summary:** This chapter reconstructs the McCulloch-Pitts program as a physics of neural computation rather than the familiar cartoon of a binary neuron. The 1943 logical calculus is developed in both directions: given a net, characterize the propositions realized by its activity; given an admissible logical expression, construct a net that realizes it. We recover the original distinction between thresholded excitatory summation and absolute inhibitory veto-one the weighted-threshold form cannot preserve fo...

---

### 47. Adversarial Vulnerabilities of Neural Biomarker Identification Systems

**Authors:** Polina Tapal, Bryce-Allen Bagley

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01856v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01856v1)

**Summary:** There is growing interest in the proposed use of EEG signals as biometric credentials, but thus far there has been little research on the reliability and security of such biometrics. Prior adversarial tests have focused on deep-learning classifiers and assumed attackers have full access to the classifier model. This has left unexamined other, more popular categories of neural signature methods as well as the more realistic case of an adversary having only black-box access to a classifier. In thi...

---

### 48. Interpretable Symptom Vectors for Depression in a Large Language Model

**Authors:** Fangyi Zhu, Ajay Subramanian, Allison Constant, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01832v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01832v1)

**Summary:** Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using me...

---

### 49. Slow-Fast Brain-Computer Interfaces: Preventing Neuroadaptive Overfitting in AI-Mediated Neural Interfaces

**Authors:** Aarthy Nagarajan

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01767v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01767v1)

**Summary:** Artificial intelligence (AI) is transforming brain-computer interfaces (BCIs) from task-specific neural decoders into adaptive systems that complete language, smooth movement, regulate rehabilitation support and adjust stimulation. These capabilities can increase speed, fluency, usability and clinical reach, yet conventional performance metrics may overlook losses in intent fidelity, authorship, agency, therapeutic challenge and durable clinical benefit. I define neuroadaptive overfitting as a c...

---

### 50. Active Visual Semantics: A large-scale MEG and eye-tracking dataset for understanding visual intelligence in action

**Authors:** Philip Sulewski, Carmen Amme, Peter König, et al.

**Published:** 2026-09-01

🔗 [Paper](http://arxiv.org/abs/2609.01055v1) | 📄 [PDF](https://arxiv.org/pdf/2609.01055v1)

**Summary:** Here we present the Active Visual Semantics (AVS) dataset, a large-scale collection of magnetoencephalography (MEG) and eye-tracking data recorded while five participants freely explored 4,080 natural scenes over 10 sessions each, yielding more than 200,000 fixation epochs in total. Unlike existing neuroimaging datasets that rely on passive viewing with enforced central fixation, AVS captures brain activity during active scene exploration, including self-generated saccades and fixations. A seman...

---

## stat.ML

**50 papers**

### 1. Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation

**Authors:** Sho Kawano, Zehang Richard Li, Paul A. Parker

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20758v1)

**Summary:** Evaluating an AI system requires disaggregated assessment, as performance varies across domains such as benchmark task types or conversation types in deployed agents. Exhaustive testing is expensive, so evaluation rests on a sample of labeled units. We treat the evaluation set as a finite population and seek accurate point and interval estimates of each domain mean. Direct estimators, including prediction-powered inference (PPI), use only a domain's own labels and are imprecise where labels are ...

---

### 2. Instance-Optimal Adaptive Location Estimation via Multiscale Mid-Summaries

**Authors:** Qiaosen Wang, Chao Gao

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20749v1)

**Summary:** Location estimation exhibits markedly different finite-sample behavior across noise distributions: regular families typically yield root-\(n\) rates, whereas compactly supported laws may admit faster, boundary-driven rates. We question whether a single estimator, without knowledge of the density's shape, can adapt to the instance-wise optimal estimation rate, as an oracle that knows the underlying location family can.   For a known location family with symmetric log-concave noise density \(f\), ...

---

### 3. Robust Multi-Task Learning for Principal Component Analysis

**Authors:** Dali Liu, Haolei Weng

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20733v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20733v1)

**Summary:** Principal component analysis (PCA) is a fundamental tool for learning low-dimensional structure from high-dimensional data. When data are collected from multiple sources, the underlying task distributions may exhibit unknown degrees of similarity, with some tasks potentially arising from arbitrary distributions. We propose new multi-task PCA procedures that exploit similarity structure across tasks to improve eigenspace estimation while remaining robust to outlier tasks. We establish non-asympto...

---

### 4. Epidemiological Causal Graph Identification: Challenges, Identifiability and Algorithms

**Authors:** Sambit Mishra, Yingying Wang, Christine K. Johnson, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20676v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20676v1)

**Summary:** Causal discovery from observational data is fundamental to statistics and machine learning, yet determining causal direction without interventions necessitates structural assumptions. Existing identifiability research primarily focuses on continuous variables under additive noise models, often neglecting mixed datasets containing ordinal scales, counts, and continuous measurements. This paper investigates causal discovery in Directed Acyclic Graphs (DAGs) where nodes follow either an ordinal dis...

---

### 5. TAP Accuracy Below the Fluctuation Scale and Universal Posterior Geometry in Spherical Linear Models

**Authors:** Jingbo Liu, Zhiyuan Yu

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20577v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20577v1)

**Summary:** We study the Bayes-optimal spherical linear model as the ambient dimension and sample size grow proportionally, under a quantitative Marchenko--Pastur spectral-regularity condition on the design. This condition is satisfied by normalized i.i.d. designs with standardized entries of finite fourth moment, but does not require entrywise independence or impose conditions on the singular vectors. Under this condition, we prove a quantitative all-temperature TAP approximation and characterize the poste...

---

### 6. Parallelism, critical windows, and separations among diffusion language models

**Authors:** Sitan Chen, Liye Wang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20539v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20539v1)

**Summary:** A popular selling point of diffusion large language models (dLLMs) is their capacity for parallelism: the ability to generate sequences of text far more efficiently than autoregressive models, which require one forward pass per token. Yet among the many competing paradigms for dLLMs, from masked to uniform to Gaussian diffusion, principled understanding of how these different proposals compare in parallelism remains limited. In this work, we initiate a fine-grained comparison of the capacity for...

---

### 7. Sharp spectral norm concentration of sparse random tensors

**Authors:** Zhixin Zhou, Yizhe Zhu

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20520v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20520v1)

**Summary:** We prove a sharp concentration inequality for the spectral norm of sparse random tensors with independent Bernoulli entries. Let $T$ be an order-$k$ tensor of dimension $n\times\cdots\times n$ with independent Bernoulli$(p)$ entries, where $k$ is fixed. For any $c,r>0$, we show that $\|T-\mathbb E T\|\le C_{k,r,c}\sqrt{np}$ with probability at least $1-n^{-r}$ whenever $np\ge c\log n$. We extend this bound to inhomogeneous Bernoulli sampling with deterministic entrywise weights. This removes the...

---

### 8. Resolution limits for process comparison from event data

**Authors:** Antony R. Lee, Peter Tiňo, Iain B. Styles

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20489v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20489v1)

**Summary:** One hospital runs bloods and imaging at the same time. Another runs them one after the other, in either order, equally often. Knowing which actually happened, and how it is recorded in data, is critical for all operational managers. In process mining, the standard approach is to construct an event log, and attempt to discover concurrent and sequential processes in a data-driven way. We show this standard approach, built on the stochastic language of an event log, reports only the assumptions of ...

---

### 9. Online Supervised Dimension Reduction with Random Features: Diagnostics and Computational Trade-offs

**Authors:** Zhenlin Yao, Wei Xiong

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20454v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20454v1)

**Summary:** Accurate optimization of a supervised spectral objective need not produce an accurate population subspace or a better predictive representation. We investigate these distinctions for Online Kernel Supervised Principal Component Analysis (OKSPCA), which combines a centered cross-moment in finite random-feature coordinates with an Adam-style orthonormal basis update for an established objective. Fixed-map consistency, concentration and perturbation results describe the estimator and its exact subs...

---

### 10. The Bias of Nonlinear Two-Time-scale Stochastic Approximation under Constant Step-Sizes

**Authors:** Djamel Rassem Lamouri, Dorian Baudry, Nicolas Gast

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20409v1)

**Summary:** Two-timescale stochastic approximation (TTSA) is a fundamental tool for analyzing coupled iterative algorithms in reinforcement learning, optimization, and stochastic control. However, finite-time guarantees for nonlinear two-timescale schemes remain difficult to obtain, especially under constant step-sizes. In this paper, we study nonlinear TTSA with step-sizes $α\ggβ$. Under standard stability, regularity, and Markovian noise assumptions, we upper bound the mean-squared error and the bias of b...

---

### 11. Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning

**Authors:** Weiwei Wang, Yuqiang Li, Xianyi Wu, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20389v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20389v1)

**Summary:** Offline policy evaluation (OPE) is crucial in high-stakes reinforcement learning applications, where new policies must be assessed reliably before deployment. In such settings, point estimates alone are insufficient; principled uncertainty quantification, such as confidence intervals and variance estimates, is essential for safe and risk-aware decision-making. A comprehensive way to unify these tasks is to estimate the sampling distribution of the evaluation error. Existing approaches, however, ...

---

### 12. Near-Optimal Pure Single-Loop Extragradient Method for Strongly Convex--Strongly Concave Minimax Optimization

**Authors:** Minhao Zhang, Zi Xu

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20327v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20327v1)

**Summary:** We study smooth strongly convex--strongly concave minimax optimization with general nonlinear coupling in the deterministic unconstrained setting. We propose a pure single-loop damped extragradient method with fixed parameters and two new full-gradient evaluations per iteration after one initialization query. The method uses an auxiliary feedback recursion and requires no inner solves, accuracy schedules, or staged restarts. We establish last-iterate linear convergence and show that reducing the...

---

### 13. Equivalence Between Nested Gibbs Measures and Log-Linear Combinations of Gibbs Measures

**Authors:** Yaiza Bermudez, Samir M. Perlaza, Iñaki Esnaola

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19988v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19988v1)

**Summary:** In this paper, three operations on Gibbs probability measures are studied. The first operation, often referred to as renormalization, takes one Gibbs probability measure and generates a new Gibbs measure by normalizing a power of its density. This normalization has a twofold effect: it changes the regularization factor and concentrates the support within a subset of the original support. Interestingly, these effects can be independently controlled by different parameters. The second operation co...

---

### 14. Error bounds in Sobolev norms for approximations with norm constrained ReLU neural networks

**Authors:** Xianjun Li, Yunfei Yang

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19937v1)

**Summary:** Recent studies have shown that smooth functions can be well approximated by ReLU neural networks with path norm constraint on the weights. We extend these results from uniform approximation to approximation in Sobolev norm. Specifically, we analyze how well Sobolev functions in $W^{n,p}$ can be approximated by neural networks with width $W$, depth $L$ and path norm bounded by $K$, when the approximation error is measured in the $W^{1,p}$-norm. For shallow networks with depth $L=1$, we derive the...

---

### 15. Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization

**Authors:** Yingxuan Zhuang, Binhe Yu, Jingxiao Yang, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19830v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19830v1)

**Summary:** Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian ...

---

### 16. Learn Your Own Thoughts: Abstract Token Curriculum

**Authors:** Khashayar Gatmiry, Avrajit Ghosh, Parsa Mirtaheri, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19717v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19717v1)

**Summary:** Large Language Models (LLMs) have achieved remarkable reasoning capabilities by utilizing chain-of-thought (CoT) as a scratchpad for intermediate stages of thinking. However, CoT techniques require explicit supervision on thinking tokens, which requires rich, task-specific data. In this work, we propose Abstract Token Curriculum (ATC), a novel curriculum learning framework that elicits effective continuous intermediate representations without direct supervision or manual scratchpad design. ATC g...

---

### 17. Improving Sample Efficiency in Peptide-HLA Binding Prediction with Hybrid Quantum-Classical Neural Networks

**Authors:** Chenyan Jia, Cong Guo, Siyue Chen, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19642v1)

**Summary:** Peptide-HLA binding prediction is a critical step in neoantigen identification for personalized cancer immunotherapy and holds significant clinical value. However, the training data available for many HLA alleles are extremely limited, which severely constrains the performance of conventional methods on this task. Parameterized quantum circuits are hypothesized to induce inductive biases beneficial for learning from small datasets, yet their application to biological sequence prediction remains ...

---

### 18. Portfolio-Based Constrained Multi-Objective Bayesian Optimization for Materials Design

**Authors:** Sushant Sinha, Christofer Hardcastle, Robert Robinson, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19550v1)

**Summary:** Materials discovery and design campaigns can be formulated as constrained multi-objective Bayesian optimization (CMOBO) problems, within which each experimental decision negotiates between two coupled but competing goals: discovering feasible candidates and refining the underlying Pareto front. Here we recast acquisition-function choice as an adaptive policy-selection problem over a portfolio of conventional and feasibility-focused acquisition functions. This was done using two controllers: UCB-...

---

### 19. Compressed Active Subspaces for Scalable Bayesian Inference

**Authors:** Thomas Flynn, Sanket Jantre, Byung-Jun Yoon, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19539v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19539v1)

**Summary:** Active subspace methods provide a framework for quantifying predictive uncertainty in high-dimensional models by identifying and performing inference along parameter directions that have the greatest influence on the model output. However, the construction of active subspaces requires storing many full-dimensional model gradients, which becomes prohibitive as model size increases. We address this limitation by proposing Compressed Active Subspaces (CAS), a scalable approach that first maps the m...

---

### 20. Next-token functional estimation

**Authors:** Milind Nakul, Vidya Muthukumar, Ashwin Pananjady

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.19529v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19529v1)

**Summary:** Suppose we observe the first $n$ points of a sequence of random variables having length $n+1$, and wish to estimate a functional of the unobserved final point and the empirical measure of the $n$ observed training points. Such next-token functionals include the probability that the next token is novel (also known as the surprise probability), the tail probability of the minimum distance between the next token and training points, and the test error of a classifier trained on the observed points....

---

### 21. Null importance: Disentangling relevance for interpretable machine learning

**Authors:** Garvesh Raskutti, Kris Sankaran, Jiaxin Ye

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19511v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19511v1)

**Summary:** Feature importance is central to interpretable machine learning, but the term "importance" encompasses several fundamentally different notions of relevance. We develop a unified perspective based on null importance: a population-level characterization of when a feature is irrelevant under a specified notion of relevance. We consider standard notions of null importance arising from marginal and conditional statistical relevance, predictive risk, functional invariance, and causal effects, and show...

---

### 22. Sharpness-Aware Minimization (SAM) Improves Classification Accuracy of Bacterial Raman Spectral Data Enabling Portable Diagnostics

**Authors:** Kaitlin Zareno, Jarett Dewbury, Siamak K. Sorooshyari, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19453v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19453v1)

**Summary:** Antimicrobial resistance is expected to claim 10 million lives per year by 2050, and resource-limited regions are most affected. Raman spectroscopy is a novel pathogen diagnostic approach promising rapid and portable antibiotic resistance testing within a few hours, compared to days when using gold standard methods. However, current algorithms for Raman spectra analysis 1) are unable to generalize well on limited datasets across diverse patient populations and 2) require increased complexity due...

---

### 23. Stable Policy Learning

**Authors:** Harvey Barnhard, Giacomo Opocher, Rahul Singh

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19418v1)

**Summary:** In evidence-based policymaking, typically one experimental sample is observed, then a learned policy recommendation is implemented at scale. Policies learned from the experimental data can perform well in expected welfare, yet random sampling in the experiment can produce recommendations with poor welfare outcomes. In this paper, we ask: how should policy learning algorithms balance expected welfare against sampling risk? Our main contribution is to show that algorithmic stability plays a centra...

---

### 24. Learning Submanifolds for Subsequent Inference on Random Dot Product Graphs, Part 1: Theory

**Authors:** Michael W. Trosset, Carey E. Priebe

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19357v1)

**Summary:** We propose a framework for restricted inference on random dot product graphs whose latent positions lie on an unknown low-dimensional support manifold. For general decision problems, we propose semisupervised decision rules that use auxiliary data to learn the support manifold. Specifically, our rules use the Isomap manifold learning procedure to construct a low-dimensional Euclidean representation of the observed graph, in which space an isometrically invariant function maps configurations of p...

---

### 25. A General Kernel Framework for Non-CND Distance Measures Using |D|-Dimensional Sparse Landmark Embeddings

**Authors:** Marcus M. Noack, Maher B. Alghalayini, Mark D. Risser

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19083v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19083v1)

**Summary:** Kernel methods, and Gaussian Processes (GPs) in particular, require a Hilbertian distance measure---one whose square is conditionally negative definite (CND)---to guarantee positive semi-definiteness (PSD) of the kernel matrix; a condition that fails for many natural input spaces, including smooth manifolds and spaces of probability distributions. We propose the Sparse Landmark Embedding (SLE) kernel, which eliminates this requirement entirely. Each input is embedded into a sparse feature vector...

---

### 26. Fast Learning Rates for Physics-Informed Kernel Methods

**Authors:** Luc Brogat-Motte, Joachim Bona-Pellissier, Giacomo Meanti, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18901v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18901v1)

**Summary:** In physics-informed machine learning, a target function $u^*$ is learned from noisy value observations $y_i=u^*(x_i)+ \varepsilon_i$, together with differential information, given either by noisy observations $d_j=(Du^*)(z_j)+ξ_j$ or by a known physical constraint $Du^*=v$. We consider the setting where $D$ is a linear differential operator and analyze a physics-informed kernel estimator $\hat u$ combining $n$ value observations and $m$ differential observations. In this context, we ask how much...

---

### 27. Stable Filters for Generative Modeling of Graph Signals

**Authors:** Martin Schmidt, Gonzalo Mateos

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18759v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18759v1)

**Summary:** Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While recent graph-aware Schrödinger bridge models incorporate topology information directly into their reference dynamics, it is unclear how perturbations of the graph propagate through these dynamics and affect the resulting generated distributions. In this paper, we analyze the structural stability of graph-aware continuous-time generative models whose...

---

### 28. When Edit Flows are Edit Jumps: replicating Edit Flows and EvoFlows

**Authors:** Gabriel Bénédict, Melanie Buechler, Gerard Riera-Solà, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18745v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18745v1)

**Summary:** Antibody lead optimization calls for a small, bounded set of edits to an existing candidate: substitutions, but also insertions and deletions. Edit-based generative models are the only ones that allocate such an edit budget without fixing the edit positions, the edit count, or the output length in advance. However, the existing approaches Edit Flows and EvoFlows did not release code or complete training specifications. Here, we show that both methods follow the same underlying process -- edits f...

---

### 29. Rank and computation of the pathlifting Jacobian of a DAG ReLU network

**Authors:** Manon Verbockhaven

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18682v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18682v1)

**Summary:** This paper provides a self-contained proof of the rank of the pathlifting Jacobian of a DAG ReLU network by performing an induction on the network's number of hidden nodes. In fact, the induction is elementary, and the key recipe is to consider the skeleton matrix of the network, a sparse matrix encoding the network paths, and transform the representation of one of its hidden neurons into an output node. The proof relies on intermediate propositions which link the pathlifting, its Jacobian, the ...

---

### 30. When a High Score Is an Illusion: Certifying Genuine versus Repackaged Forecasting Skill

**Authors:** Pin Ni, Francesca Medda, Ramin Okhrati

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19223v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19223v1)

**Summary:** Ranks depend on the observations used for comparison. Reusing those observations can add association between forecast and outcome rank contrasts even when the evaluated forecast and outcome stay fixed. We characterize assignments that preserve association between specified population-rank contrasts, including forecast rank minus baseline rank compared with outcome rank minus baseline rank. Conditional on independent training, whole trajectories are sampled independently from a common law, with u...

---

### 31. Revisiting Distributed Sign-Based Variance Reduction

**Authors:** Wei Jiang, Zechao Li, Lijun Zhang

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18656v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18656v1)

**Summary:** Sign-based methods reduce communication costs in distributed environments, but aggregating local signs can introduce bias when data are heterogeneous. As a result, existing sign-based variance reduction methods fail to obtain the optimal convergence rates. In this paper, we solve this problem and obtain optimal rates for both nonconvex stochastic and finite-sum optimization. We first give a counterexample showing that majority voting can fail to approach stationary points even with exact local g...

---

### 32. How Many Labels Does Model Choice Need? Certificates and Budgets for Selective Prediction

**Authors:** Tetsuji Kuboyama

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18622v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18622v1)

**Summary:** Classifiers can make identical predictions yet require labels to compare their selective performance: confidence ranks weight the same errors differently. We quantify this requirement for the area under the generalized risk-coverage curve (AUGRC). A prelabel lower bound rules out insufficient budgets. With all labels known, a covering linear program bounds the minimum number of labels sufficient to fix the winner (the certificate size) within $K-1$ labels for $K$ candidates. For fixed $K$, indep...

---

### 33. Provable Guarantees and Efficient Learning of Structural Equation Models with Latent Confounders

**Authors:** Weijian Yu, Jean Honorio

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18535v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18535v1)

**Summary:** Causal discovery aims to recover causal relationships from observed data. In various fields, exploring causal relationships among variables remains an important topic, but this task becomes challenging due to the existence of latent confounders. Ignoring such confounders can lead to false associations and incorrect edge directions. In this paper, we study the linear structural equation model with latent confounders. We propose an algorithm that iteratively identifies terminal (observed) nodes an...

---

### 34. Not All Nodes Are Created Equal: Homophily-Aware Stratification for Stable GNN Evaluation

**Authors:** Naga Venkata Sai Jitin Jami, Thomas Altstidl, Sebastian Hoefler, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19210v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19210v1)

**Summary:** Graph neural networks are widely used for transductive node classification, with accuracy typically measured on randomly drawn train/validation/test splits. Reported accuracy has been shown to shift substantially across different random splits of the same dataset, making published comparisons between architectures unreliable. The classical remedy in non-graph settings is stratified $k$-fold cross-validation, which ensures each test fold reflects the full class distribution of the dataset. We arg...

---

### 35. Spatially Adaptive Noise Injection

**Authors:** Frantzeska Lavda, Maciej Falkiewicz, Van Khoa Nguyen, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18466v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18466v1)

**Summary:** Diffusion samplers reverse a learned noising process using either stochastic (DDPM) or deterministic (DDIM) updates, which represent endpoints of a single family controlled by a scalar noise-injection variance that is applied identically at every spatial location. This uniform approach neglects the geometry of natural images: high-curvature regions such as edges and textures, where the denoiser is uncertain, benefit from stochastic correction, whereas smooth regions, where the score is precise, ...

---

### 36. Gradient Descent with Stochastic Subspaces via Persistence of Memory

**Authors:** Subhroshekhar Ghosh, Clement Z. Q. Ng, Pierre-Louis Poirion, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18416v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18416v1)

**Summary:** Stochastic subspace methods have gained popularity as gradient descent based techniques for large scale optimisation problems, especially in distributed settings. In this paper, we introduce the technique of "persistence of memory" to greatly extend and improve the random subspace methods. To this end, we leverage a vector that is only weakly correlated with the gradient in order to provide a guiding structure to the generative process of the random subspace along which the descent is going to t...

---

### 37. Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts

**Authors:** Guojun Zhu, Xunheng Huang, Peng Yin, et al.

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18366v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18366v1)

**Summary:** Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts, memory, retrieval, tools, and control code around a fixed target agent. Task holdout varies semantic tasks but leaves the benchmark protocol fixed, so a "bad genius" Proposer can produce a cheating harness whose released-benchmark gain depends on a benchmark-wide shortcut. We introduce Counterfactual Harness Search and E...

---

### 38. Federated Soft Clustering via Generalized Total Variation Minimization

**Authors:** Shamsiiat Abdurakhmanova, Alexander Jung

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.19202v1) | 📄 [PDF](https://arxiv.org/pdf/2609.19202v1)

**Summary:** We study federated soft clustering over federated learning (FL) networks of devices that each hold a private local dataset and fit a personalized Gaussian mixture model (GMM). Generalized total variation minimization (GTVMin) couples the local maximum likelihood problems through a graph regularizer that penalizes a discrepancy between the models of connected nodes. The choice of discrepancy measure is a key design decision: we compare a squared Euclidean distance between model parameters, which ...

---

### 39. Beyond Quadratic Loss: The Stability Phase Diagram of Adam

**Authors:** Gaoxiang Tang, Huanran Chen, Ziming Liu

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18314v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18314v1)

**Summary:** Loss spikes are recurrent instabilities in neural-network training and can arise from multiple mechanisms. For Adam in particular, macroscopic loss spikes have been linked to optimizer dynamics, yet how its two momentum timescales govern them remains unclear. We investigate this dependence by mapping training dynamics across the $(β_1,β_2)$ plane. Across a range of model--task settings, an approximately linear boundary, $1-β_2=C(1-β_1)$, separates spiky from non-spiky dynamics, whereas a one-dim...

---

### 40. Preservation of Log-Concavity and Convergence of Wasserstein-Fisher-Rao Gradient Flows

**Authors:** Francesca Romana Crucinio, Sahani Pathiraja

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18118v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18118v1)

**Summary:** We study the convergence of Wasserstein-Fisher-Rao (WFR) gradient flows for sampling from probability distributions known up to a normalisation constant. By combining Wasserstein transport with Fisher-Rao birth-death dynamics, WFR flows balance exploration and selection. These flows have been recognised as a promising mechanism to accelerate convergence beyond Langevin dynamics. We show that for a class of strongly log-concave target distributions satisfying additional curvature conditions, WFR ...

---

### 41. Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex--Concave Minimax Optimization

**Authors:** Minghao Zhang, Zi Xu

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.17973v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17973v1)

**Summary:** We introduce a new single-loop algorithmic framework for smooth nonconvex--concave minimax optimization. The resulting projected damped extragradient method combines projected extragradient updates, dual momentum, and a moving proximal center. Under both the optimization-stationarity and game-stationarity criteria, our method achieves the best-known complexity among single-loop first-order methods. For optimization stationarity, our method achieves a gradient complexity of $O(L^2D_Y\barΔ_0\varep...

---

### 42. On the Identifiability of Mixed Ordinal and Exponential Family Causal DAGs under Linear Parametric Models

**Authors:** Sambit Mishra, Urbashi Mitra

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.17942v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17942v1)

**Summary:** The problem of identifiability in linear parametric models (LPMs) whose nodes follow either an ordered logit model or a regular one-parameter exponential family is evaluated. The results go beyond classical structural equation models as well as results for nodes with observations from a homogeneous family of distributions. The main result establishes that the orientation of every edge joining an ordinal node to an exponential-family node is identifiable from the joint distribution alone at every...

---

### 43. Symmetry without a manifold: intrinsic dimension on orbits

**Authors:** Chon-Fai Kam, Miloud Bessafi, Frédéric Cadet

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17926v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17926v1)

**Summary:** The standard geometric derivation of neural scaling exponents takes the intrinsic dimension of a data manifold as its input. On modular addition in $\mathbb{Z}_p$ that derivation has no input. The exact algebraic solution is an orbit of $\mathbb{Z}_p$ acting by isometries. Transitivity alone makes the ratio statistic underlying the standard dimension estimator a point mass, so the estimator is undefined, and here the two nearest neighbour distances coincide exactly. Breaking the symmetry at scal...

---

### 44. Generalized DCCQ: From Binary Quotients to Multinomial Simplex Geometry and Critical-Strip Coordinates

**Authors:** Y. Kenan Yılmaz

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17899v1)

**Summary:** We extend the discrete complex complement quotient (DCCQ) framework from binary Bernoulli counts to multinomial count compositions. For m+1 categories, m is the number of independent probability degrees of freedom. Integer count vectors modulo common scaling determine rational points of the m-dimensional probability simplex. Building on standard simplex and log-ratio coordinate geometry, for m >= 2 we define the full multinomial DCCQ coordinate map and show that it is a real-analytic diffeomorph...

---

### 45. TabPFN-3.5: Technical Report

**Authors:** Benjamin Jäger, Nick Erickson, Léo Grinsztajn, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17895v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17895v1)

**Summary:** We introduce TabPFN-3.5, our new flagship Tabular Foundation Model. It significantly outperforms its predecessor, TabPFN-3, and all existing baselines across a broad range of tabular problems. TabPFN-3.5 sets a new state of the art on standard tabular prediction in TabArena, and extends it to the data practitioners encounter in practice: non-i.i.d. data with temporal or grouped splits, tables with strings, text and images, high-cardinality categorical features, and wide tables with many features...

---

### 46. Bracketing Uncertainty in Clustering Under the Manifold Hypothesis

**Authors:** Savik Kinger, Luciano Dyballa, Steven W. Zucker

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17892v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17892v1)

**Summary:** The manifold hypothesis suggests a natural criterion for clustering: partition data according to the manifold component from which each point is drawn. Whether two components are separable depends on a geometric tradeoff: the ambient separation between components versus the largest gap in sampling. In practice, this tradeoff is rarely assessed explicitly, leading standard methods to over-commit to a single clustering assignment even when the data do not support a unique answer. We formalize this...

---

### 47. Sharp margin-based generalization bounds for realizable SVM

**Authors:** Steve Hanneke, Aryeh Kontorovich

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17845v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17845v1)

**Summary:** Let the exact homogeneous hard-margin support vector machine be trained on \(m\) independent observations from a Borel probability law on a real Hilbert space. We prove that, with score zero counted as an error, there is a universal numerical constant \(C\) such that \[   \Pp\left(   γ_m>0,\quad   \Risk(u_m)>   \frac{C}{m}   \left(   K_m+\log\frac1δ   \right)   \right)   \le δ. \] Here \(γ_m\) is the empirical homogeneous margin, \(u_m\) is the exact minimum-norm unit-margin separator, \(r_m\) i...

---

### 48. METALICA: METAdynamics and repLICA exchange for enhanced diffusion sampling

**Authors:** Alireza Omidi, Jiajun He, Jörg Gsponer, et al.

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17823v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17823v1)

**Summary:** Many proteins function through transitions between conformational states, yet rare states are rarely sampled by diffusion models trained on an equilibrium ensemble, demanding better sampling methods. We introduce METALICA, which implements Metadynamics on a pretrained diffusion model via Replica Exchange. It accumulates a bias potential along a Collective Variable, repels new samples from previous ones through biased sampling, and reweights samples onto the unbiased distribution. METALICA holds ...

---

### 49. Approximating Measures on Function Spaces: Transport and Truncation

**Authors:** Ricardo Baptista, Bamdad Hosseini, Alexander W. Hsu

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17802v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17802v1)

**Summary:** Measures on function spaces arise throughout Bayesian inverse problems and generative modeling, often with low-dimensional structure relative to a tractable reference measure. We introduce the class $\mathcal{P}_ψ(μ)$ of measures that differ from a reference measure $μ$ only through a finite-dimensional map $ψ$ while preserving the reference conditionals on its fibers. Class members are determined by their $d$-dimensional pushforwards under $ψ$ and admit convenient block-triangular transport map...

---

### 50. Random tilts to find stationary points in stochastic convex optimization

**Authors:** Felipe Areces, John C. Duchi, Malo Sommers

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17798v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17798v1)

**Summary:** We consider the problem of finding stationary points of stochastic convex functions and related variational inequalities. For each, we show that regularized empirical risk minimization, coupled with a random tilting perturbation, obtains stationarity residual order $\sqrt{d/n}$ for $d$-dimensional problems given $n$ observations. We present a few complementary results that show that some dimension dependence is necessary, in distinction from standard stochastic optimization and empirical risk mi...

---

