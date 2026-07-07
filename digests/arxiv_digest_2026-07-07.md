# arXiv Daily Digest - 2026-07-07

Total papers: 350

---

## cs.AI

**50 papers**

### 1. From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

**Authors:** Wenhao Li, Xueying Jiang, Quanhao Qian, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05396v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05396v1)

**Summary:** Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...

---

### 2. Weak-to-Strong Generalization via Direct On-Policy Distillation

**Authors:** Shiyuan Feng, Huan-ang Gao, Haohan Chi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05394v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05394v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL we...

---

### 3. Interpretable Human-Label-Free Deep Learning for Real-Bogus Classification with Uncertainty Quantification

**Authors:** Raphaël Bonnet-Guerrini, Bruno Sanchez, Dominique Fouchez, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05393v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05393v1)

**Summary:** Time-domain surveys generate many transient candidates, making Real-Bogus classification a critical step in automated discovery pipelines. Reliable labels are costly, while community labels can be noisy and survey-dependent. We aim to develop a Real-Bogus classification framework that can be trained without human-labeled data using injected transients and bogus-dominated survey data, remains robust under strong class contamination, and provides calibrated uncertainty quantification. We combine s...

---

### 4. LLM-as-a-Verifier: A General-Purpose Verification Framework

**Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05391v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05391v1)

**Summary:** Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that p...

---

### 5. Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation

**Authors:** Haozhe Wang, Weijia Feng, Jinpeng Yu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05382v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05382v1)

**Summary:** Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed mu...

---

### 6. What Does a Discrete Diffusion Model Learn?

**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05381v1)

**Summary:** What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the da...

---

### 7. Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation

**Authors:** Jiaqi Peng, Xiqian Yu, Delin Feng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05377v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05377v1)

**Summary:** While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...

---

### 8. GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Letian Fu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05369v1)

**Summary:** For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and in...

---

### 9. SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models

**Authors:** Thomas Thebaud, Yuzhe Wang, Hao Zhang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05365v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05365v1)

**Summary:** Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-a...

---

### 10. REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing

**Authors:** Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05364v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05364v1)

**Summary:** Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language s...

---

### 11. SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints

**Authors:** Dylan Zongmin Liu

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05363v1)

**Summary:** Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. W...

---

### 12. Graph Sparse Sampling: Breaking the Curse of the Horizon in Continuous MDP Planning

**Authors:** Idan Lev-Yehudi, Vadim Indelman

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05359v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05359v1)

**Summary:** Planning under uncertainty in continuous domains is essential for autonomous systems, yet computationally demanding. Tree-based search methods such as Monte Carlo Tree Search (MCTS) remain popular, but their branching structure can require sampling budgets that grow exponentially with lookahead depth in the worst case. From a tree perspective, continuous state or action spaces become especially challenging, since the planner must decide where to search in an infinite branching hierarchy. We prop...

---

### 13. Selective Disclosure Watermarking for Large Language Models

**Authors:** Xuyang Chen, Xiang Li, Yangxinyu Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05353v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05353v1)

**Summary:** Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...

---

### 14. Multiplayer Interactive World Models with Representation Autoencoders

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05352v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05352v1)

**Summary:** We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...

---

### 15. OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement

**Authors:** Adriana Laurindo Monteiro, Nayse Fagundes, Gabriel Mattos Langeloh, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05346v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05346v1)

**Summary:** We propose OptiAgent, a multi-agent framework that, given a natural language description of an Operations Research problem, is able to output a solver-ready mathematical formulation as well as executable code. Our architecture prioritizes the mathematical modeling step, where dedicated agents extract structures, such as decision variables and constraints, enabling iterative self-correction. We introduce a novel multi-loop validation architecture with four specialized feedback mechanisms, each ta...

---

### 16. TREK: Distill to Explore, Reinforce to Refine

**Authors:** Yuanda Xu, Zhengze Zhou, Kayhan Behdin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05339v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05339v1)

**Summary:** Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure that uses distillation not for imitation but for exploration support expansion. A key advantage of TREK is its generality: because it only consumes verified output trajectories, it ca...

---

### 17. Steering Optimisation Trajectories in Diffusion Representation Learning

**Authors:** Rajat Rasal, Avinash Kori, Tian Xia, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05319v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05319v1)

**Summary:** We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of image reconstruction against latent representation quality, revealing trajectories that organise around two distinct regimes early in training. Models in the reconstruction regime prioritise image fidelity early, whereas those in the disentanglement regime improve reconstruction and disentanglement m...

---

### 18. Topological Shape Representation for Aneurysm -- Bifurcation Detection

**Authors:** Akshay Gokhale, Mansi Dhamne

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05317v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05317v1)

**Summary:** Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteris...

---

### 19. Evaluating and Understanding Model Editing for Medical Vision Language Models

**Authors:** Guli Zhu, Chenwei Wu, Liyue Shen

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05310v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05310v1)

**Summary:** Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmarks focus on general-purpose tasks and do not reflect realistic clinical domain requirements and variability. To address this, we introduce M3Bench, a clinically grounded benchmark for multimodal model editing that evaluates whether an edit remains reliable, precise, and generalizable under the challe...

---

### 20. MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution

**Authors:** Zefeng Wang, Minxi Yan, Jinhe Bi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05297v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05297v1)

**Summary:** Recent LLM agents tackle increasingly long-horizon, open-ended tasks, and external skills, reusable procedural knowledge supplied to the agent, further extend this capability. However, a fixed, hand-authored skill is rarely optimal, and cannot adapt to the diversity of tasks an agent encounters. Self-improving agents address this by rewriting their own skill files from execution traces, yielding meaningful gains on challenging benchmarks. Yet such self-evolution remains non-recursive: it improve...

---

### 21. Air Quality Downscaling with Station-Guided Pseudo-Supervision

**Authors:** Guorun Wang, Simone Foti, Andreas D. Demou, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05292v1)

**Summary:** Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover...

---

### 22. Wavelet Scattering Transform for Interpretable Schizophrenia Biomarker Discovery and Classification from Resting-State EEG

**Authors:** Md. Taksimul Ahsan Tawhid, Nasif Ahmed Rafe, Alif Tahmid Priyom, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05282v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05282v1)

**Summary:** Schizophrenia is a debilitating neuropsychiatric disorder characterized by profound cortical network dysregulation, for which objective, clinically translatable EEG based biomarkers remain underdeveloped. Existing automated classification pipelines rely predominantly on static power spectral density features inherently blind to amplitude modulation dynamics and cross-frequency coupling, phenomena central to schizophrenia pathophysiology, while adopting epoch level cross validation strategies tha...

---

### 23. ProPS: Prompted Profile Synthesis for Natural Language-Conditioned Speaker Embedding Distributions

**Authors:** Thomas Thebaud, Junhyeok Lee, Laureano Moro-Velazquez, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05276v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05276v1)

**Summary:** Speaker embeddings, or x-vectors, are widely used to represent speaker identity and speaker-related attributes, but existing embedding extractors are typically descriptive rather than generative: they map an observed speech segment to an x-vector, which is then used for downstream applications. We introduce ProPS, Prompted Profile Synthesis, a framework for generating distributions of speaker embeddings conditioned on natural language prompts such as "a thirties male speaker with an Indian accen...

---

### 24. Adaptive Inference Batching using Policy Gradients

**Authors:** Ruslan Sharifullin

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05272v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05272v1)

**Summary:** Inference serving systems must balance throughput and latency under bursty, heterogeneous workloads, yet the industry standard remains static batching policies that require manual tuning and cannot adapt to shifting traffic. We investigate whether reinforcement learning (RL) can learn adaptive batching and routing policies that outperform these heuristics, training REINFORCE and PPO agents on a discrete-event simulator validated against queuing theory and production traces (Azure Functions, Burs...

---

### 25. Shifting from Discrete to Continuous Reference Data: QSM-Derived Horizontal Tree Biomass Distribution for Deep Learning Biomass Estimation

**Authors:** Nils Griese, Christoph Kleinn, Nils Nölke

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05260v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05260v1)

**Summary:** Conventional modeling approaches for LiDAR-based above-ground biomass (AGB) estimation rely on discrete plot-level inventory aggregates. This methodology introduces boundary-effect uncertainties that may severely degrade model performance within small field plots. To solve this limitation, we evaluate a Horizontal Biomass Distribution (HBD) reference mapped continuously from Quantitative Structure Models (QSMs). We trained a sparse 3D U-Net on simulated broadleaved forest structures using three ...

---

### 26. Privacy-Preserving Robustness Verification for Neural Networks

**Authors:** Nianyun Song, Xiaokun Luan, Yu Guo, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05251v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05251v1)

**Summary:** Neural network verification and data privacy are inherently in tension: verification demands full access to model parameters and input data, yet both are increasingly restricted by privacy regulations and intellectual property constraints. This tension has left robustness verification impractical in privacy-sensitive domains. In this work, we address this gap with SecureCROWN, the first framework for privacy-preserving neural network robustness verification. Built upon secure two-party computati...

---

### 27. CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling

**Authors:** Zuwang He, Shihao Shu, Yuli Qu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05242v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05242v1)

**Summary:** Personalized incentive allocation is vital for e-commerce, where uplift modeling is the standard for estimating Individual Treatment Effects (ITE). However, traditional models often fail in complex multi-seller environments with violations of the Stable Unit Treatment Value Assumption (SUTVA). We identify two critical challenges: Seller-level Cannibalization, where incentives shift expenditure between shops without growing the platform, and Incentive-level Cannibalization, where organic conversi...

---

### 28. Optimizing ML Workload Partitioning between CPUs and CIM Accelerators for Heterogeneous Computing

**Authors:** Joel Klein, Rebecca Pelke, Roberto Laudani, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05240v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05240v1)

**Summary:** Computing-in-Memory (CIM) accelerators execute Matrix-Vector Multiplications (MVMs) in memory, making them a compelling solution for Machine Learning (ML) workloads. However, existing ML workload partitioning approaches for CIM accelerators do not fully account for Resistive Random Access Memory (RRAM) constraints such as limited memory, high write latency, and limited endurance. They also neglect parallelism, low-level architectural effects, or the Central Processing Unit (CPU) as a complementa...

---

### 29. MoP-JEPA: Hard-Assigned Predictor Mixtures for Stochastic JEPA World Models

**Authors:** Zhi Song, Ximing Xing, Zhenchao Tang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05238v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05238v1)

**Summary:** JEPA world models predict the next latent state with a single deterministic predictor trained by latent regression. We show that this fails structurally when the environment is stochastic: at a branching transition, the regression-optimal predictor outputs the conditional mean of the successor embeddings, a point between the true next states that corresponds to no state at all. We prove this collapse for deterministic and gated mixture-of-experts predictors, and prove that MoP-JEPA's hard-assign...

---

### 30. EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer

**Authors:** Xingze Gao, Chuanrui Hu, Hongda Chen, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05202v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05202v1)

**Summary:** Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domai...

---

### 31. Reason, Reward, Refine: Step-Level Errors Corrections with Structured Feedback for Physics Reasoning in Small Language Models

**Authors:** Raj Jaiswal, Dhruv Jain, Rishabh Dhawan, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05199v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05199v1)

**Summary:** Physics reasoning fails structurally in small language models: an error at any step propagates forward, corrupting every inference that follows. Limited domain knowledge, hallucination under multi-step derivation, and distributional sensitivity compound this failure. We propose a step-level reward framework that identifies the first reasoning error, generates targeted structured feedback, and trains the model to revise its solution via policy gradient with KL regularization, without exposing it ...

---

### 32. Noisy-Channel Minimum Bayes Risk Decoding

**Authors:** Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05198v1)

**Summary:** Minimum Bayes Risk (MBR) decoding yields more robust and higher-quality text generation than maximum a posteriori (MAP) decoding by selecting hypotheses that maximize expected utility over sampled pseudo-references. However, there exists a discrepancy in the design: hypothesis selection calculates expected utility scores conditioned on given pseudo-references, while commonly used evaluation metrics, e.g., BLEU and COMET, are asymmetric. Therefore, it is important to consider both hypothesis-to-r...

---

### 33. Unified Audio Intelligence Without Regressing on Text Intelligence

**Authors:** Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05196v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05196v1)

**Summary:** Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...

---

### 34. When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents

**Authors:** Yechao Zhang, Shiqian Zhao, Jiawen Zhang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05189v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05189v1)

**Summary:** Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write po...

---

### 35. ClassicLogic: A Knowledge-Driven Benchmark of Classic Puzzle Games for Evaluating Compositional Generalization

**Authors:** Mahnoor Shahid, Hannes Rothe

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05185v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05185v1)

**Summary:** Compositional generalization, the ability to understand and produce novel combinations of known components, remains a fundamental challenge for modern artificial intelligence. While few benchmarks exist, many focus on linguistic tasks and lack complex, explicit compositional structures. We introduce ClassicLogic, a new benchmark suite designed to evaluate an agent's ability to learn and compose problem-solving strategies. The benchmark consists of four classic logic puzzles: Sudoku, KenKen, Kaku...

---

### 36. Rethinking On-Policy Self-Distillation for Thinking Models

**Authors:** Simran Kaur, Narutatsu Ri, Yinghui He, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05184v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05184v1)

**Summary:** Self-distillation is a promising recipe for self-improvement in language models. In this setting, a model can serve as its own teacher when given privileged information, such as a solution to a math problem. This seems especially appealing for thinking models, which can use test-time reasoning to absorb the privileged information. Surprisingly, we show that privileged self-distillation degrades thinking models on long reasoning traces: across five Qwen3 and OLMo thinking models evaluated on AIME...

---

### 37. Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets

**Authors:** Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05179v1)

**Summary:** In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning,...

---

### 38. CP-WSP: A Declarative CP-SAT Framework for Configurable Multi-Constraint Workforce Scheduling

**Authors:** Vipul Patel, Anirudh Deodhar, Dagnachew Birru

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05177v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05177v1)

**Summary:** Workforce scheduling is an NP-hard combinatorial optimization problem requiring simultaneous satisfaction of labor regulations, coverage requirements, employee preferences and operational objectives. Existing CP formulations typically model simplified instances with 6-12 constraints at shift-level granularity and critically lack explicit support for: mandatory break scheduling with midpoint placement control; acuity weighted workload equity; sub-shift temporal granularity enabling demand-driven ...

---

### 39. AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments

**Authors:** Zhiheng Xi, Dingwen Yang, Jiaqi Liu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05174v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05174v1)

**Summary:** Language agents, i.e., LLM agents, progress rapidly and are increasingly deployed in production environments. This trend underscores the urgent need for rigorous and realistic evaluations. However, most existing benchmarks evaluate agents in simplified, idealized settings. They typically rely on pre-packaged tool interfaces, overlook critical steps, and assume inputs are clean and fully specified. Consequently, they understate the difficulty of real deployments, where uncertainty and noise are u...

---

### 40. The Changing Role of Symbolic Methods in Artificial Intelligence

**Authors:** Jun Sun

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05168v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05168v1)

**Summary:** Why do intelligent systems need to perform explicit symbolic reasoning? Computer science has traditionally regarded symbolic reasoning as a defining component of intelligence. Yet the remarkable success of modern foundation models raises a fundamental question: if increasingly capable AI systems can operate with little explicit symbolic reasoning, what role do symbolic methods actually play?   This article argues that explicit symbolic reasoning is not a fundamental property of intelligence, but...

---

### 41. Open Problems in AI Incident Governance

**Authors:** Harleen Kaur Sidhu, Rebecca Scholefield, Nour Annan, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05163v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05163v1)

**Summary:** AI systems may produce failures after deployment that pre-deployment safety assessments do not anticipate. Managing these failures requires what we refer to as adequate \textit{AI incident governance}, where having good definitions, taxonomies, monitoring practices, reporting mechanisms, and incident analysis is essential. We examine existing frameworks related to AI incident governance by regulatory bodies and independent efforts, and find that while there are frameworks that describe how indiv...

---

### 42. DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation

**Authors:** Xin Cheng, Xingkai Yu, Chenze Shao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05147v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05147v1)

**Summary:** Speculative decoding accelerates Large Language Model (LLM) inference by decoupling draft generation from target verification. While recent parallel drafters efficiently propose long token sequences in a single forward pass, they suffer from rapid acceptance decay due to a lack of inter-token dependencies. Furthermore, indiscriminately verifying these extended blocks wastes critical batch capacity on tokens with high rejection risks, severely degrading throughput in high-concurrency serving syst...

---

### 43. PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference

**Authors:** Akshat Jani, Prathamesh Gadekar, Sakhinana Sagar Srinivas, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05134v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05134v1)

**Summary:** We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines. The workflow links problem specification, data generation, operator training, and checkpoint-based inference. A stateful input graph converts multi-turn natural-language input and user edits into validated problem specifications. The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element back...

---

### 44. TacReasoner: A Dynamic Tactile-Language Framework for Interactive Reasoning in Real-World Scenarios

**Authors:** Kailin Lyu, Di Wu, Long Xiao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05131v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05131v1)

**Summary:** Among the five primary human senses, tactile is arguably the most fundamental to survival, as it enables the perception of physical contact and interaction in real-world environments. In this paper, we explore two key challenges of integrating tactile sensing into intelligent systems for multimodal reasoning: (i) insufficient modeling of dynamic tactile signals, which restricts reasoning over temporally evolving properties, and (ii) hallucination in tactile foundation models caused by the absenc...

---

### 45. Three-Phase Evaluation of AI-Assisted Software Development Life Cycle

**Authors:** Joshua Strubel, Professor Carrie Russell, Carson Crockett, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05125v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05125v1)

**Summary:** This paper presents an exploratory evaluation of how increasing levels of AI autonomy affect software development productivity, requirement adherence, and developer cognitive workload. A team of four developers reimplemented the same full-stack web application across three sequential phases: partial AI-assisted development using GitHub Copilot, an AI-exclusive workflow using GitHub Copilot, and an AI-exclusive workflow using AWS Kiro. Evaluation metrics included development effort (hours), requi...

---

### 46. ASSEMCAD: Production-Ready CAD Assembly Generation from Natural Language

**Authors:** Yurui Dong, Shu Zou, Siqi Li, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05123v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05123v1)

**Summary:** Recent advances in large language models and programmatic CAD have significantly improved Text-to-CAD generation for individual parts. However, production-ready mechanical assembly generation remains largely unsolved. Unlike single-part modeling, assemblies require coordinated reasoning over multiple components, functional interfaces, assembly relations, engineering principles, and physical consistency. Consequently, directly generating executable CAD code is insufficient for constructing mechan...

---

### 47. Agent Data Injection Attacks are Realistic Threats to AI Agents

**Authors:** Woohyuk Choi, Juhee Kim, Taehyun Kang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05120v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05120v1)

**Summary:** AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection...

---

### 48. Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing

**Authors:** Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05114v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05114v1)

**Summary:** Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introd...

---

### 49. Grokking Is Conditional and Fragile: A Fully-Tractable, Multi-Seed Study at 12K Parameters

**Authors:** Yoshiyuki Ootani

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05104v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05104v1)

**Summary:** Grokking -- the delayed onset of generalization long after a network has fit its training set - -is usually studied in models too large to read completely and reported from single training runs. We instead study a publicly released ~11,856-parameter Llama-style transformer (Glimmer-1-Base) on modular arithmetic, small enough to enumerate its weights, attention, and full input-output map, and we measure grokking as a multi-seed rate rather than a single outcome. In this fully-tractable regime gro...

---

### 50. AIFS-SUBS: Extending Data-Driven Forecasting to Sub-Seasonal Timescales

**Authors:** Jakob Schloer, Steffen Tietsche, Christopher D. Roberts, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05100v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05100v1)

**Summary:** Data-driven models now rival numerical weather prediction in the medium range, but extending them to sub-seasonal lead times raises challenges absent at shorter horizons. Errors accumulate over long autoregressive rollouts, systematic biases grow with lead time, and several years of data must be held out for independent verification, even though machine-learning models otherwise benefit from longer training records.   To address these challenges, we adapt ECMWF's AIFS-CRPS medium-range model. AI...

---

## cs.CL

**50 papers**

### 1. Weak-to-Strong Generalization via Direct On-Policy Distillation

**Authors:** Shiyuan Feng, Huan-ang Gao, Haohan Chi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05394v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05394v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL we...

---

### 2. LLM-as-a-Verifier: A General-Purpose Verification Framework

**Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05391v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05391v1)

**Summary:** Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that p...

---

### 3. What Does a Discrete Diffusion Model Learn?

**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05381v1)

**Summary:** What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the da...

---

### 4. GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Letian Fu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05369v1)

**Summary:** For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and in...

---

### 5. SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models

**Authors:** Thomas Thebaud, Yuzhe Wang, Hao Zhang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05365v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05365v1)

**Summary:** Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-a...

---

### 6. REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing

**Authors:** Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05364v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05364v1)

**Summary:** Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language s...

---

### 7. Faithfulness to Refusal: A Causal Audit of Neuron Selectors

**Authors:** Ananth Eswar, Pratinav Seth, Utsav Avaiya, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05355v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05355v1)

**Summary:** Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across fi...

---

### 8. Selective Disclosure Watermarking for Large Language Models

**Authors:** Xuyang Chen, Xiang Li, Yangxinyu Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05353v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05353v1)

**Summary:** Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...

---

### 9. How Much is Left? LLMs Linearly Encode Their Remaining Output Length

**Authors:** Mohamed Amine Merzouk, Dmitri Carpov, Mirko Bronzi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05316v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05316v1)

**Summary:** Large language models generate one token at a time, yet their responses show remarkably consistent length structure: step-by-step solutions converge in predictable token counts, retrievals stop after a few sentences, retractions extend responses by measurable amounts. We ask whether the model carries an internal estimate of how much response remains. Training minimal-capacity linear probes on frozen hidden states of three open-weight 7-8B models across seven completion-style datasets, we find th...

---

### 10. SalAngaBhava: A Sinhala Market Dataset for Aspect-based Sentiment Analysis

**Authors:** Lakshani Galwatta, Nisansa de Silva, Sarangi Aththanayake, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05259v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05259v1)

**Summary:** Sentiment analysis has been a primary domain under Natural Language Processing (NLP) from its inception as it plays a vital role in both real-world and research applications. In high-resource languages, this has been extended a step further, and instead of predicting sentiment at the sentence level, models have been developed to detect more fine-grained sentiments at aspect level. However, in order to conduct this fine-grained Aspect-based Sentiment Analysis (ABSA), datasets annotated with aspec...

---

### 11. Streaming Neural Speech Codecs through Time-Invariant Representations

**Authors:** Kélian Estève, Salima Mhdaffar, Mickael Rouvier, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05250v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05250v1)

**Summary:** Neural speech codecs are increasingly used as intermediate representations in codec-based speech generation systems. TiCodec introduces a factorized representation that separates time-varying speech content from time-invariant information through a Time-Invariant Representation Extraction (TIRE) module, potentially reducing the amount of information that must be modeled at the frame-level.   In this work, we investigate the nature of the information captured by TIRE representations and their sui...

---

### 12. Progressive Refinement: An Iterative Pseudo-Labeling Approach for Mandarin-English Code-Switching ASR

**Authors:** Qu Yang, Cakra Wardhana, Tim Ng

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05224v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05224v1)

**Summary:** Code-switching (CS), alternating languages within the same utterance, poses significant challenges for automatic speech recognition (ASR) due to limited CS training data. This paper applies an iterative pseudo-labeling training approach to CS-ASR for the first time, demonstrating its effectiveness in leveraging unlabeled data to improve CS-ASR performance. The approach comprises three phases: pseudo-label generation, two-stage bilingual model training, and iterative improvements. It begins by ge...

---

### 13. Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off

**Authors:** Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05217v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05217v1)

**Summary:** Public institutions increasingly use large language models (LLMs) to answer citizens' questions, often pairing a curated knowledge base with live web search, yet whether the sources behind these answers can be trusted has received little empirical scrutiny. We report a pre-launch expert evaluation of Evrópuvefur, an independent, government-funded service run by the University of Iceland that answers questions about the European Union, conducted as Iceland prepared for its referendum of 29 August...

---

### 14. Noisy-Channel Minimum Bayes Risk Decoding

**Authors:** Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05198v1)

**Summary:** Minimum Bayes Risk (MBR) decoding yields more robust and higher-quality text generation than maximum a posteriori (MAP) decoding by selecting hypotheses that maximize expected utility over sampled pseudo-references. However, there exists a discrepancy in the design: hypothesis selection calculates expected utility scores conditioned on given pseudo-references, while commonly used evaluation metrics, e.g., BLEU and COMET, are asymmetric. Therefore, it is important to consider both hypothesis-to-r...

---

### 15. Unified Audio Intelligence Without Regressing on Text Intelligence

**Authors:** Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05196v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05196v1)

**Summary:** Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...

---

### 16. RABBiT: Rapidly adaptive BOLD foundation model via brain-tuning for accurate zero-shot and few-shot prediction of speech-elicited responses in the brain

**Authors:** Omer Moussa, Mariya Toneva

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05171v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05171v1)

**Summary:** Language understanding in the brain is context-dependent, varying across experimental stimuli and individuals, which makes it difficult to build computational models that generalize across both. This calls for a foundation model of language-evoked brain activity that can capture shared structure while adapting efficiently to new participants and inputs. We introduce RABBiT (Rapidly Adaptive BOLD foundation model via BraIn-Tuning), a compact audio-to-fMRI encoder designed for accurate zero- and f...

---

### 17. EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments

**Authors:** Deyao Zhu, Xin Zhou, Shengling Qin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05155v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05155v1)

**Summary:** Pretraining scaling laws reveal that model capability improves predictably with data and compute. But learning from real world environments after deployment remains far less understood. Analyzing roughly 38,000 hours of agent interaction with the environment across 134 real world tasks, we find, to the best of our knowledge, the first evidence that overall performance during environment learning follows a log-sigmoid scaling law with remarkably high precision, reaching R^2 = 0.998. Across model ...

---

### 18. DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation

**Authors:** Xin Cheng, Xingkai Yu, Chenze Shao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05147v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05147v1)

**Summary:** Speculative decoding accelerates Large Language Model (LLM) inference by decoupling draft generation from target verification. While recent parallel drafters efficiently propose long token sequences in a single forward pass, they suffer from rapid acceptance decay due to a lack of inter-token dependencies. Furthermore, indiscriminately verifying these extended blocks wastes critical batch capacity on tokens with high rejection risks, severely degrading throughput in high-concurrency serving syst...

---

### 19. When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games

**Authors:** Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05132v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05132v1)

**Summary:** As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three fron...

---

### 20. Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing

**Authors:** Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05114v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05114v1)

**Summary:** Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introd...

---

### 21. Rating the Pitch, Not the Product: User Evaluations of LLMs Reflect Expectations More Than Performance

**Authors:** Robert Morabito, Tyler McDonald, Charitra Viswanath, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05113v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05113v1)

**Summary:** Imagine two users interact with the same LLM. One has been told it is the cutting-edge flagship model; the other, an older, weaker model. They walk away with markedly different ratings of its usefulness and intelligence, yet they used the same model. In a controlled study, 162 participants each used one of six LLMs from two families across three collaborative tasks, after first viewing a landing page that matched, overstated, or understated their model's true capability. This pre-interaction fra...

---

### 22. MIRAGE: Defending Long-Form RAG Against Misinformation Pollution

**Authors:** Saadeldine Eletter, Ruihong Zeng, Yuxia Wang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05069v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05069v1)

**Summary:** Retrieval-Augmented Generation (RAG) improves factuality by grounding LLMs in external evidence, but real-world retrieval is often polluted: semantically relevant passages may contain subtle misinformation, misleading framings, or fabrications. We introduce MIRAGE, a training-free, model-agnostic defense for long-form RAG. MIRAGE builds an NLI-based cross-document claim graph and applies a Defended-Claims Gate to either condition generation on a consistent, multi-source supported subset or to bl...

---

### 23. Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection

**Authors:** Víctor Yeste, Paolo Rosso

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05052v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05052v1)

**Summary:** Human value detection is commonly formulated as sentence-level multi-label classification over the 19 refined Schwartz values, typically predicted as independent labels. Schwartz theory, however, describes them as a circular motivational continuum, in which adjacent values are compatible and opposing values are in tension. We ask whether this structure can be operationalized as an explicit output-space geometry and used as a soft bias rather than a hard constraint. On a DeBERTa-v3-base classifie...

---

### 24. Multi-Large Language Model Orchestrated Severity Assessment of Clinical Records (MOSAIC)

**Authors:** Manuela Del Castillo Suero, Arnault-Quentin Vermillet, Nicole Sonne Heckmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05032v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05032v1)

**Summary:** Background: Disease severity is a multidimensional construct difficult to capture with rule-based approaches in Electronic Healthcare Records (EHR). Agentic large language model (LLM) systems could synthesise clinical evidence and reason over EHRs, but remain unevaluated for this task. Methods: MOSAIC is a two-phase agentic LLM framework for severity phenotyping, using type 2 diabetes (T2D) as a proof-of-concept. MOSAIC was evaluated on a synthetic cohort (SyntheticMass; open-weight N = 4,886; c...

---

### 25. Knowledge Knows, Verbalization Tells: Disentangling Latent Directions for Mathematical Solvability in LLMs

**Authors:** Nikolaos Xiros, Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05013v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05013v1)

**Summary:** Although LLMs have made significant progress in mathematical reasoning, determining whether a mathematical problem is solvable remains a fundamental yet challenging capability. While recent studies have probed internal representations of model solvability beliefs, verbalization has primarily been studied behaviorally rather than as an internal representation, limiting its analysis and manipulation. We address this gap by separately probing representations of solvability knowledge and verbalizati...

---

### 26. The syntax of wh-agreement in Yemeni Ibbi Arabic

**Authors:** Ashraf Naji, Mohammed Q. Shormani

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04986v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04986v1)

**Summary:** This article tackles an important phenomenon in the syntax of Yemeni Ibbi Arabic (YIA), viz., wh-agreement, a phenomenon common to several languages including Greek, Indonesian, Lubukusu, Irish, etc. In YIA, wh-agreement manifests itself via agreement inflections on the Wh-Op, C, T/V, v. To account for this phenomenon, we propose an Agree across phases (AAP) approach anchored in the mechanism of Feature Inheritance (FI) in which Agree as MATCHING (AM) is a bit separated from feature valuation (F...

---

### 27. Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM Training

**Authors:** Jingwei Zuo, Cong Zeng, Ilyas Chahed, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04969v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04969v1)

**Summary:** The training paradigm of large language models has shifted from traditional one-pass training to multi-epoch training, as reasonable reuse of limited high-quality data can improve both model performance and sample efficiency. Meanwhile, excessive repetition introduces the risk of overfitting and diminishing returns. Determining when and how to reuse data effectively thus emerges as a natural but under-explored question. Through a novel observation of model's "Memorization Window" signals derived...

---

### 28. Who's Behind It? Annotating and Extracting Conspiratorial Actors from German Telegram Posts

**Authors:** Helena Mihaljević, Jolanda Beer, Mareike Lisker, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04962v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04962v1)

**Summary:** Conspiracy theories commonly attribute important events to the actions of powerful and secretive actors. While computational research has largely focused on document-level analyses of conspiracy theories, less attention has been paid to identifying the actors that drive such narratives. We develop annotation guidelines for conspiratorial actors, present a span-annotated corpus of German Telegram posts, and investigate their automatic extraction using transformer-based models. We further apply th...

---

### 29. When Words Predict Workload

**Authors:** Anubhab Banerjee

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04951v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04951v1)

**Summary:** Standard distributed \ac{llm} schedulers rely on static token counts or rolling latency averages, making them susceptible to failures on statutorily constrained text. On \ac{epo} claims governed by Article 84 \ac{epc}, linguistic rigidity makes human and machine authorship statistically indistinguishable. Resolving this ambiguity mid-flight forces dynamic multi-model ensemble expansion, triggering unpredictable KV-cache and weight-allocation spikes that saturate consumer-grade edge GPU VRAM and ...

---

### 30. You Frame It: How Conceptual Representations Shape LLM Detection and Reasoning about Antisemitism

**Authors:** Katharina Soemer, Helena Mihaljević

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04945v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04945v1)

**Summary:** LLMs enable the integration of external conceptual resources at inference time, creating new opportunities for detecting ideologically and historically complex phenomena such as antisemitism. We investigate how different forms of conceptual grounding affect antisemitism detection and explanation behavior across four state-of-the-art LLMs.   Using two expert-annotated datasets, we compare definitional, fine-grained taxonomic, example-augmented, and large-context representations of antisemitism.  ...

---

### 31. DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling

**Authors:** Wataru Nakata, Yuki Saito, Hiroshi Saruwatari

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04941v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04941v1)

**Summary:** Full-duplex spoken dialogue models are trained on conversational speech in which each speaker is represented as a separate stream, but existing large-scale public speech corpora are mostly monaural, making them unsuited for SDLM training. We present DuplexChat, an open-source corpus for full-duplex spoken dialogue models, and DuplexChat-Pipe, a pipeline for constructing speaker-separated full-duplex dialogue speech from public podcast feeds. DuplexChat-Pipe filters language-specific podcast feed...

---

### 32. Ossetic-COT: Designing a morphologically annotated corpus and morphological analyzer for Ossetic

**Authors:** Anna Shatskikh, Alexey Sorokin

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04895v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04895v1)

**Summary:** In this work we present the first morphologically annotated corpus for Iron Ossetic that conforms to the Universal Dependencies schema. The corpus includes 5454 manually annotated sentences from the Iron Ossetic Corpus of Oral Texts, containing 74032 tokens. We use this corpus to train a BERT-based morphological analyzer. The analyzer achieves tag accuracy of 95.60%.

---

### 33. Evaluating Large Language Models for Antisemitic Incident Classification

**Authors:** Karina Halevy, Julia Mendelsohn, Chan Young Park, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04890v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04890v1)

**Summary:** Addressing hate and violence in society requires timely detection of hateful events from public reporting, but automated identification of hateful events remains underexplored. We introduce the task of hateful event detection and investigate the ability of AI systems, specifically large language models (LLMs), to discover and classify reports of antisemitic events with fine-grained labels. We evaluate OpenAI's GPT-4o and Meta's Llama-3.2-3B-Instruct on multiple expert-annotated datasets containi...

---

### 34. Semantic Homogenization in Italian Popular Music: A Diachronic Analysis

**Authors:** Lorenzo Canale, Stefano Scotta, Alberto Messina

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04832v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04832v1)

**Summary:** In recent years, studies have revealed a decline in semantic variety across popular music lyrics, particularly in English-language songs on streaming platforms like Spotify. This research examines whether a similar trend can be observed in a different linguistic and cultural context: the lyrics of all finalist songs from the 75 editions of the Sanremo Music Festival, Italy's most renowned music competition. What sets this work apart is the development of a flexible and efficient methodology for ...

---

### 35. Evaluating the Effect of Linguistic Relatedness on Cross-Lingual Transfer in Large Multilingual Automatic Speech Recognition

**Authors:** Andrei Florian, Cynthia Jayne Amol, Hope Kerubo Ombaba, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04814v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04814v1)

**Summary:** Extending automatic speech recognition (ASR) to low-resource African languages is constrained by the prohibitive demands of data collection at scale. A promising direction is to leverage linguistic relatedness to enhance cross-lingual transfer from a related auxiliary language to the low-resource target by sequentially adapting on both. Although this strategy has shown meaningful improvements in small ASR models, its effectiveness in large ASR remains unclear. We extend this framework to large m...

---

### 36. Multi-Turn On-Policy Distillation with Prefix Replay

**Authors:** Baohao Liao, Hanze Dong, Christof Monz, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04763v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04763v1)

**Summary:** We study on-policy distillation (OPD) for agentic tasks, where an LLM agent interacts with an environment over multiple turns and a student imitates a teacher over these multi-turn interaction histories. Fully online OPD is costly because each update requires fresh student rollouts through the environment and teacher queries at visited histories. We propose Replayed-Prefix On-Policy Distillation (ReOPD), an off-environment alternative that reuses pre-collected teacher trajectories as replayed pr...

---

### 37. LP-SFT: Local-Preserving Supervised Fine-Tuning via Multimodal Entropy Structure

**Authors:** Yueyang Wang, Baolong Bi, Shuo Lu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04733v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04733v1)

**Summary:** Supervised fine-tuning (SFT) is the standard approach for adapting pretrained language models to downstream domains, yet it often improves target-domain behavior at the cost of degrading pre-existing capabilities. Standard cross-entropy fine-tuning promotes only the observed label token and leaves unconstrained how probability mass is redistributed over other plausible alternatives, potentially distorting the rich local preference structure learned during pretraining. We first analyze next-token...

---

### 38. Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment

**Authors:** Yu Li, Xiuyu Li, Mingyang Yi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04728v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04728v1)

**Summary:** Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably results in off-policy training data. To resolve this, Importance sampling (IS) is proposed, while the token-level ratios compound over long sequences, causing severe variance exploded. A natural idea is "transferring" these off-policy token into on-policy token, so that the importance scores for correction are unnecessary. Following this idea, we prop...

---

### 39. What You See Is What You Get: Observation-Aligned Supervision for Chart-to-Code Generation

**Authors:** Tianhao Niu, Qingfu Zhu, Wanxiang Che

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04726v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04726v1)

**Summary:** Chart-to-code generation is commonly trained with supervised fine-tuning on reference plotting scripts, implicitly treating the gold code as a fully observable target. We argue that this assumption is often invalid: many chart programs contain latent raw variables that cannot be uniquely recovered from the rendered image. For example, a boxplot exposes summary statistics rather than original samples, a pie chart reveals proportions rather than arbitrary raw values, and a histogram shows bin-leve...

---

### 40. PAST-TIDE: Prototype-Anchored Statement Tuning with Topic-Invariant Normalization for Stance Detection

**Authors:** Md. Shakhoyat Rahman Shujon, MD Jahid Hasan Jim, Md. Milon Islam, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04690v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04690v1)

**Summary:** We introduce PAST-TIDE, our stance detection system addressing both subtasks of the StanceNakba Shared Task at NakbaNLP@LREC-COLING 2026. The main idea is statement tuning. We redefine stance as cloze-style masked language modeling (MLM), letting a verbalizer map label words to stance categories through the pre-trained MLM head rather than appending a randomly initialized classification head. We complement this with prototypical contrastive learning, which uses learnable class prototypes for bat...

---

### 41. URSA: Chemistry-Aware Benchmark for Utilitarian Retrosynthesis Assessment

**Authors:** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04688v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04688v1)

**Summary:** Synthesis planning aiming to find pathways of reactions for a target molecule is one of the most important and challenging tasks in drug discovery. Recent progress has produced both specialized deep-learning retrosynthesis systems and general-purpose large language models, but objective comparison remains difficult due to the lack of flexible, chemically interpretable benchmarking protocols. In the current study, we are introducing the URSA (Utilitarian RetroSynthesis Assessment) evaluation fram...

---

### 42. ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents

**Authors:** Harsh Soni

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04686v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04686v1)

**Summary:** Tool calling is central to modern language model agents, but aggregate benchmark scores often hide where tool use fails. A model that never calls a needed tool and a model that calls the tool but ignores the result can look similar under final task accuracy. We introduce ToolFailBench, a diagnostic benchmark for measuring tool-use failures across 1,000 tasks in finance, medicine, law, cybersecurity, and real estate. Tool-required tasks return values the model wouldn't guess, forcing it to trust ...

---

### 43. Does It Fail to See or Fail to Know? Attributing Errors in Vision-Language Models

**Authors:** Khang Nhat Hoang Vo, Artem Vazhentsev, Artem Shelmanov, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04683v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04683v1)

**Summary:** Vision-language models (VLMs) perform well on visual question answering with high-quality images but struggle when questions require knowledge beyond what is clearly and directly visible. In such settings, uncertainty quantification should not only indicate whether the model is likely to fail but also diagnose why it is uncertain, across dimensions such as perception, entity recognition, and knowledge retrieval. While prior work has focused on individual failure modes in isolation or treated inc...

---

### 44. FormalRx: Rectify and eXamine Semantic Failures in Autoformalization

**Authors:** Haocheng Wang, Baiyu Huang, Yingjia Wan, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04655v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04655v1)

**Summary:** The veracious semantic alignment in autoformalization is significant for formal mathematical reasoning. However, existing evaluations provide only opaque binary verdicts or scalar scores, offering no interpretable insight into where or why translations fail. This opacity severely limits both human understanding and automated system improvement. To bridge this gap, we introduce FormalRx, a comprehensive diagnostic evaluation framework that transforms autoformalization assessment from black-box ju...

---

### 45. Retroactive Chain-of-Thought (RetroCoT): Forensic Reconstruction Prompts as a Safety Diagnostic Across Model Generations

**Authors:** Samira Hajizadeh

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04645v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04645v1)

**Summary:** Safety alignment in large language models is typically evaluated against direct, imperative harmful requests. We show that this alignment is highly conditioned on pragmatic register: models that refuse a direct request frequently comply when the same underlying objective is expressed through a different communicative stance. This suggests that current alignment policies are not invariant to semantic equivalence, but remain sensitive to how a request is pragmatically framed. We introduce Retroact...

---

### 46. Wrong Before Right: Late Rescue and Interface Failure in Aligned Language Models

**Authors:** Jiaqi Deng

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04640v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04640v1)

**Summary:** We study how correctness is assembled inside aligned language models, not only whether the final answer is right. Using layer-wise difference-in-differences (DiD) trajectories over polarity-controlled minimal pairs, we identify the wrong-dip: in mid layers (25-90% depth), internal preference transiently commits to the incorrect answer and is rescued only by late-layer correction. We verify this causally with patchscope-style activation transplantation across 17 models, three families, and 64x sc...

---

### 47. CARD: Cross-component Audio Representation Distillation for Encoder-Free Audio Captioning

**Authors:** Ganesh Pavan Kartikeya Bharadwaj Kolluri, Yuchen Zhang, Michael Kampouridis, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04619v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04619v1)

**Summary:** Modern automated audio captioning systems pair a frozen audio encoder with a large language model (LLM) via a trainable projector, incurring the encoder's inference cost and bottlenecking the model through its fixed acoustic features. We present CARD, an encoder-free audio captioning model that removes the encoder at inference: a 13.2M projector feeds a frozen LLM with merged LoRA adapters, while the teacher used to train it is discarded. CARD distills a pretrained audio teacher (CLAP-HTSAT) int...

---

### 48. Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval

**Authors:** Suhyeong Park, Junha Jung, Jungwoo Park, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04605v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04605v1)

**Summary:** Multi-vector vision-language retrieval preserves fine-grained visual evidence through maximum-similarity late interaction, but dense image-side tokens make storage and scoring expensive. Existing token compression methods reduce this cost, yet they can remove or collapse object- and region-level evidence that future query tokens may need to select. We propose SaMer, an object-aware token merging framework that compresses image-side post-projector tokens into $K$ representative centroids while pr...

---

### 49. MTEB-PT: A Text Embedding Benchmark for Brazilian Portuguese

**Authors:** Tardelli Ronan Coelho Stekel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04581v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04581v1)

**Summary:** Text embeddings for Portuguese have no dedicated benchmark: evaluation rests on translated corpora such as English MS MARCO or on thin multilingual coverage, with native tasks scattered and unconsolidated. We introduce MTEB-PT, a benchmark of 22 native Brazilian-Portuguese tasks across seven categories (classification, multilabel classification, pair classification, semantic textual similarity, clustering, retrieval, and reranking), admitting only data created or found in Portuguese and excludin...

---

### 50. Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation

**Authors:** Theodore O. Cochran

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04576v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04576v1)

**Summary:** LLM agents increasingly answer questions against knowledge bases they help maintain. A common intuition holds that progressive disclosure, a compact catalog plus a one-line summary per page so the agent loads only what it needs, should make this cheaper than consulting a large monolithic index. We test that on a real 709-page markdown wiki maintained by an LLM. We retrofit it for progressive disclosure and run a preregistered ablation in which four versions of the corpus differ only in how the a...

---

## cs.CV

**50 papers**

### 1. From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

**Authors:** Wenhao Li, Xueying Jiang, Quanhao Qian, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05396v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05396v1)

**Summary:** Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...

---

### 2. SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion

**Authors:** Paul Engstler, Iro Laina, Christian Rupprecht, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05392v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05392v1)

**Summary:** We present SynCity 3000, a framework for generating 3D scenes that are globally coherent while enabling fine-grained layout control. Building on the ability of current image-to-3D generators to produce complex 3D assets from a single image, we extend this capability to the scale of entire scenes by adapting the generator to be applicable as a convolutional operator. We achieve this by fine-tuning the model on scene-like data generated by a new synthetic data engine, which we propose to address t...

---

### 3. Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models

**Authors:** Hongyu Li, Wanjia Fu, Xiaoyan Cong, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05390v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05390v1)

**Summary:** Predicting object dynamics (i.e., world modeling) is a fundamental challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their high-dimensional state spaces and complex material properties. While current world models approach this through two distinct paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding of their relative strengths and limitations remains elusive due to ...

---

### 4. InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics

**Authors:** Erich Liang, Caleb Kha-Uong, Chinmaya Saran, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05389v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05389v1)

**Summary:** Camera intrinsics are vital for recovering 3D structure from 2D video. However, most 3D algorithms assume fixed intrinsics throughout a video, an assumption that often fails for real-world in-the-wild videos. Consequently, estimating per-frame intrinsics from RGB images is critical for making 3D methods robust to videos with dynamic intrinsics. InFlux previously advanced this research direction by establishing the first real-world benchmark with per-frame ground truth intrinsics for dynamic intr...

---

### 5. Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation

**Authors:** Haozhe Wang, Weijia Feng, Jinpeng Yu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05382v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05382v1)

**Summary:** Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed mu...

---

### 6. Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation

**Authors:** Jiaqi Peng, Xiqian Yu, Delin Feng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05377v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05377v1)

**Summary:** While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...

---

### 7. MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing

**Authors:** Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05376v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05376v1)

**Summary:** Recent advances in video diffusion models have enabled either long single-view generation through temporal autoregression, or short multi-view synthesis through bidirectional attention. However, generating long, multi-view consistent videos of dynamic scenes remains unsolved. In this work, we present MV-Forcing, a framework that composes temporal and view-wise autoregression within a single diffusion model by introducing a 4D geometric bridge between sequentially generated views. Our key insight...

---

### 8. PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space

**Authors:** Sensen Gao, Zhaoqing Wang, Qihang Cao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05373v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05373v1)

**Summary:** 3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoenco...

---

### 9. ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction

**Authors:** Xinze Li, Yiyuan Wang, Pengxu Chen, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05356v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05356v1)

**Summary:** Streaming 3D reconstruction relies on a compact recurrent scene state to process long image streams in linear time and bounded memory. However, repeated updates can gradually corrupt this state, causing reliable historical information to be overwritten by noisy or ambiguous observations. We introduce ReCal3R, a reliability-calibrated learning rate method for recurrent 3D reconstruction. Instead of directly applying a candidate learning rate, our method estimates state token reliability from the ...

---

### 10. Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation

**Authors:** Jingyi Lu, Kai Han

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05354v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05354v1)

**Summary:** Monocular-to-stereo conversion synthesizes stereoscopic content from 2D videos for immersive 3D experiences. In modern Depth-Image-Based Rendering (DIBR) approaches, stereo inpainting of disocclusions is the critical bottleneck. Training-based methods achieve superior quality but rely on scarce stereo pairs or synthetic data with domain gaps. We address this through the first self-supervised framework learning from monocular videos via cycle consistency. Our key contribution is the Geometric Rec...

---

### 11. Multiplayer Interactive World Models with Representation Autoencoders

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05352v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05352v1)

**Summary:** We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...

---

### 12. Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis

**Authors:** Xianhao Chen, Jiarui Hu, Yuanbo Yang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05348v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05348v1)

**Summary:** Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D und...

---

### 13. WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images

**Authors:** Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05347v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05347v1)

**Summary:** While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first feedforward 3D Gaussian Splatting framework capable of appearance-conditioned novel-view synthesis for unposed in-the-wild images. To handle inconsistent photometric conditions, we propose a dual-branch architecture that explicitly decouples geometry from appearance. The geometry branch extracts an app...

---

### 14. CenSynCMB: Centre Maps and Physics-Guided Synthesis for Microbleed Detection

**Authors:** Lucas He, Hanyuan Zhang, Krinos Li, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05325v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05325v1)

**Summary:** Cerebral microbleeds (CMBs) are MRI markers of small vessel disease and the microbleed component of amyloid related imaging abnormalities (ARIA-H), but their small size, sparsity, and similarity to vessels, calcification-like foci, and artefacts make automated detection difficult. We propose CenSynCMB, a centre-guided and mimic-aware framework combining a 3D Attention U-Net, auxiliary centre-map supervision, false-negative-driven reweighting, and fold-wise physics-guided synthesis of positive CM...

---

### 15. Steering Optimisation Trajectories in Diffusion Representation Learning

**Authors:** Rajat Rasal, Avinash Kori, Tian Xia, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05319v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05319v1)

**Summary:** We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of image reconstruction against latent representation quality, revealing trajectories that organise around two distinct regimes early in training. Models in the reconstruction regime prioritise image fidelity early, whereas those in the disentanglement regime improve reconstruction and disentanglement m...

---

### 16. Topological Shape Representation for Aneurysm -- Bifurcation Detection

**Authors:** Akshay Gokhale, Mansi Dhamne

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05317v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05317v1)

**Summary:** Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteris...

---

### 17. Deep Learning for Semen Analysis in Male Infertility: Computer Vision, Multimodal Fusion, and Clinical Translation

**Authors:** Runwei Guan, Shaofeng Liang, Jiacheng Weng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05311v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05311v1)

**Summary:** Male infertility contributes substantially to the global infertility burden, and sperm analysis remains central to diagnosis, treatment planning, and assisted reproductive technology. Conventional semen evaluation, however, is labor-intensive, operator-dependent, and limited by inter- and intra-observer variability, motivating the development of objective and reproducible computational approaches. This review provides a comprehensive and perspective-oriented synthesis of artificial intelligence-...

---

### 18. Air Quality Downscaling with Station-Guided Pseudo-Supervision

**Authors:** Guorun Wang, Simone Foti, Andreas D. Demou, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05292v1)

**Summary:** Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover...

---

### 19. ChatImage: Navigating Long-Form LLM Answers through Interactive Images

**Authors:** Wencan Jiang, Jiangning Zhang, Yong Liu

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05290v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05290v1)

**Summary:** Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second groundin...

---

### 20. Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models

**Authors:** Parth Upman, Nishita Jain, Shreyank N Gowda

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05274v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05274v1)

**Summary:** Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We intro...

---

### 21. Is the Geometry Doing the Work? An Operating-Point Audit of Hierarchy in Hyperbolic Vision-Language Models

**Authors:** Jaeyoung Kim, Eunseok Kim, Dongsuk Jang

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05268v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05268v1)

**Summary:** Whether a hyperbolic representation model uses its geometry cannot be read off its curvature parameter: what matters is the dimensionless operating point $\sqrt{c}ρ$ and whether the radial and cone machinery is active there. We develop a battery of necessary-condition diagnostics and audit three published hyperbolic vision-language families -- MERU, HyCoCLIP, and PHyCLIP -- across released checkpoints and controlled interventions on a fixed GRIT snapshot, identifying three failure modes. First, ...

---

### 22. SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments

**Authors:** Suryanarayana Reddy Yarrabothula, Manisha Chawla, Kunal Sinha, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05264v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05264v1)

**Summary:** Existing video benchmarks evaluate action recognition on consumer videos, egocentric recordings, or simulated industrial environments. They do not test vision-language models under the visual and procedural conditions of real industrial CCTV, where workers appear as distant figures amid dust, steam, low light, glare, occlusion, and overlapping activities. We introduce STEELBENCH, a diagnostic benchmark for industrial surveillance that jointly evaluates per-worker activity recognition, safety-rul...

---

### 23. Learning Probabilistic Embeddings for Unsupervised Action Segmentation

**Authors:** Shuai Li, Duc Manh Vu, Juergen Gall

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05263v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05263v1)

**Summary:** This paper concerns the problem of unsupervised temporal action segmentation for long, untrimmed videos. Recent successful approaches follow a joint representation learning and clustering paradigm, where optimal transport (OT) is adopted to produce pseudo labels for learning frame representations. These approaches alternate between estimating pseudo labels using OT and optimizing the parameters with gradient descent during training, where OT is used for obtaining the final temporal action segmen...

---

### 24. FlowMark: Mask-Guided Video Watermarking

**Authors:** Vishal Asnani, Shruti Agarwal, John Collomosse

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05261v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05261v1)

**Summary:** We present FlowMark, a video watermarking framework guided by automatically predicted object masks. In contrast to prior region-based approaches that require user-supplied mask guidance, FlowMark learns to identify optimal regions for watermark embedding through a dedicated Mask Predictor network. Our end-to-end trainable architecture combines region-aware encoding with noise-augmented training to ensure robustness against compression, geometric transformations, and content variation, while pres...

---

### 25. Shifting from Discrete to Continuous Reference Data: QSM-Derived Horizontal Tree Biomass Distribution for Deep Learning Biomass Estimation

**Authors:** Nils Griese, Christoph Kleinn, Nils Nölke

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05260v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05260v1)

**Summary:** Conventional modeling approaches for LiDAR-based above-ground biomass (AGB) estimation rely on discrete plot-level inventory aggregates. This methodology introduces boundary-effect uncertainties that may severely degrade model performance within small field plots. To solve this limitation, we evaluate a Horizontal Biomass Distribution (HBD) reference mapped continuously from Quantitative Structure Models (QSMs). We trained a sparse 3D U-Net on simulated broadleaved forest structures using three ...

---

### 26. Repurposing CLIP to Localize at Pixel Level

**Authors:** Jiaxiang Fang, Shiqiang Ma, Jing Wang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05253v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05253v1)

**Summary:** Large-scale Vision-Language Models like CLIP have demonstrated impressive open-set localization capabilities at the image level. However, adapting this capability to pixel-level dense prediction poses challenges due to global feature biases. In this paper, we introduce CLIPix, a simple yet effective framework that repurposes CLIP to perform pixel-level localization. By tracing back CLIP's classification process, CLIPix identifies object-specific attentive regions and repurposes them as pixel-lev...

---

### 27. Vision Pretraining for Dense Spatial Perception

**Authors:** Zelin Fu, Bin Tan, Changjiang Sun, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05247v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05247v1)

**Summary:** Dense spatial perception is essential for physical intelligence, where visual systems are expected to recover structured, metric, and actionable representations from pixel observations. Modern visual foundation models tend to prioritize semantic invariance, often at the expense of detailed spatial understanding. In this work, we study vision pretraining through a boundary-centric lens, motivated by the premise that boundaries and shape discontinuities offer essential cues for perceiving geometri...

---

### 28. GUSH3R: Everyone Everywhere All at Once as Gaussians

**Authors:** Keito Abe, Kaede Shiohara, Takashi Otonari, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05243v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05243v1)

**Summary:** Reconstructing dynamic human-scene environments from monocular videos is a challenging problem that requires jointly modeling scene geometry, camera motion, and non-rigid human dynamics while enabling photorealistic rendering. Recent feed-forward methods can efficiently predict geometry, but they are often limited to non-photorealistic representations such as point clouds and meshes, or they fail to handle non-rigid objects, particularly dynamic humans. To fill this gap, we present GUSH3R (Gauss...

---

### 29. A Multimodal Reasoning Typology for Grounding Chart-Image Coherence in Science Communication

**Authors:** Avina Nakarmi, Sohom Sen, Xun Song, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05222v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05222v1)

**Summary:** Charts and images appear together throughout scientific publications, yet most computational work does not characterize their coherence. We argue that a chart, its accompanying image, and the caption that links them form a multimodal unit, and that the inferential work required to read it varies systematically. To capture this variation, we develop a typology of reasoning gaps, R1 through R5, that characterizes how chart, image, and text jointly convey a scientific claim, and the interpretive wo...

---

### 30. Probing Geospatial SSL Representations with Environmental Signals

**Authors:** Rohita Mocharla, Vishal M. Patel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05207v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05207v1)

**Summary:** Self-supervised learning (SSL) is designed to learn generic, transferable representations rather than representations optimized for a single task. Most geospatial benchmarks evaluate representations solely through downstream tasks, providing limited insight into the information encoded within the representation itself. We ask a different question: do SSL representations of satellite imagery preserve statistical associations with environmental variables that co-vary with the imaging process? To a...

---

### 31. An event-driven framework for fly-inspired visual motion detection

**Authors:** Qinbing Fu, Jingyu Huang, Yan Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05205v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05205v1)

**Summary:** Fast and reliable motion detection is essential for machine vision and autonomous systems operating in dynamic environments. This work integrates emerging event-based sensing with biologically structured neural computation to establish an efficient computational paradigm for visual motion detection. The proposed framework is built upon a recently developed fly-inspired neural network that emulates motion-processing circuits in the optic lobe. Owing to its feed-forward and training-free architect...

---

### 32. Causal-RetiGraph: Cross-Cohort Retinal Support and Same-Subject Pathway Analysis for Diabetic Retinopathy

**Authors:** Inam Ullah, Imran Razzak, Shoaib Jameel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05204v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05204v1)

**Summary:** Diabetic retinopathy (DR) is a local retinal lesion process and a visible manifestation of systemic microvascular injury. Modern retinal AI can grade images accurately, but often leaves unanswered how local lesion evidence, retinal vascular structure, and systemic disease pathways are connected. This paper introduces \emph{Causal-RetiGraph}, a compact biomedical informatics framework that links retinal graph phenotypes with NHANES-anchored pathway modelling. The retinal-image fold constructs an ...

---

### 33. VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving

**Authors:** Tianjia Yang, Ke Li, Ruwen Qin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05180v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05180v1)

**Summary:** Adverse driving conditions, such as bad weather, remain a principal barrier to autonomous driving because they degrade two things at once: what the vehicle can perceive and what it can physically do. Human drivers cope by anticipation, reasoning about the scene and re-budgeting speed, following distance, and steering before grip or sight is lost, whereas current autonomous driving systems at best react after the fact. This paper proposes VLM-CASE, a framework that gives an autonomous vehicle thi...

---

### 34. FSDC-DETR: A Frequency-Spatial Domain Collaborative DETR for Small Object Detection

**Authors:** Aiwen Liu, Chengguang Zhu, Gang Wang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05176v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05176v1)

**Summary:** Small object detection (SOD) remains a challenging task in real-world applications. Despite recent advances, existing detectors remain limited by rigid processing that entangle spatial aggregation with implicit frequency aliasing and truncation, leading to inadequate preservation of high-frequency components for SOD. To tackle these limitations, we propose a Frequency-Spatial Domain Collaborative Detection Transformer (FSDC-DETR), a novel collaborative framework that explicitly models complement...

---

### 35. Claim-Level Rubric Rewards for Video Caption Reinforcement Learning

**Authors:** Mingqi Gao, Hongyuan Dong, Yifei Chen, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05150v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05150v1)

**Summary:** In this paper, we introduce Claim-Level Rubric Rewards (CuRe), a structured reward framework designed to address the reward-design bottleneck in reinforcement learning for dense video captioning. Existing reward designs generally fall into two categories: holistic response-level judgment across heterogeneous criteria, or alignment-based evaluation against reference captions. However, both paradigms suffer from fundamental limitations. Holistic rewards struggle to ensure factual accuracy and are ...

---

### 36. Fully Rotation-Equivariant Spectral-Spatial Learning for Multispectral Object Detection

**Authors:** Peng Zhang, Tingfa Xu, Shuaihao Han, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05148v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05148v1)

**Summary:** Existing multispectral detectors are limited by discrete spectral processing, a scale-dependent shift in the relative reliability of spectral and spatial cues across pyramid levels, and the lack of explicit rotation-equivariant geometric priors for arbitrarily oriented objects. To tackle these limitations, we propose FressDet, a fully rotation-equivariant spectral-spatial learning framework for multispectral object detection, capable of capturing the continuous, ordered nature of spectral struct...

---

### 37. UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation

**Authors:** Mengmeng Liu, Diankun Zhang, Jiuming Liu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05133v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05133v1)

**Summary:** World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the ac...

---

### 38. ASSEMCAD: Production-Ready CAD Assembly Generation from Natural Language

**Authors:** Yurui Dong, Shu Zou, Siqi Li, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05123v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05123v1)

**Summary:** Recent advances in large language models and programmatic CAD have significantly improved Text-to-CAD generation for individual parts. However, production-ready mechanical assembly generation remains largely unsolved. Unlike single-part modeling, assemblies require coordinated reasoning over multiple components, functional interfaces, assembly relations, engineering principles, and physical consistency. Consequently, directly generating executable CAD code is insufficient for constructing mechan...

---

### 39. Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies

**Authors:** Adrian Szvoren, Dimitrios Kanoulas, Nilufer Tuptuk

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05122v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05122v1)

**Summary:** Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and...

---

### 40. Semantic Video Communication via Multi-Scale Convolution and Dynamic Routing for Next-Generation Networks

**Authors:** Gengtian Shi, Jinze Yu, Chenhao Wu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05093v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05093v1)

**Summary:** The exponential growth of video traffic demands novel semantic communication paradigms that transmit meaning rather than raw bits. We present a generative AI-enabled framework for semantic video communication addressing two critical challenges: efficient hierarchical temporal modeling for bandwidth-constrained transmission and robust semantic alignment between video content and natural language queries at network edge devices. Our approach introduces a multi-scale temporal convolutional encoder ...

---

### 41. Be Indiscrete: The Benefits of Learning Continuous Spine Degeneration Severity Scores

**Authors:** Maria Monzon, Andrew Zisserman, Robin Y. Park, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05090v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05090v1)

**Summary:** Lumbar spine degeneration is a major contributor to chronic low back pain and is routinely assessed on MRI using ordinal grading systems, e.g. normal, mild, moderate, severe. Consequently, most approaches to train models to grade these MRIs formulate grading as a multi-class classification problem, treating ordinal grades as categorical, ignoring differences in misclassification severity, and imposing hard decision boundaries on a continuous disease process. This work explores modeling spinal de...

---

### 42. TimeThink: Reasoning with Time for Video LLMs

**Authors:** Handong Li, Longteng Guo, Zikang Liu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05089v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05089v1)

**Summary:** Video reasoning requires models to identify and verify temporally localized evidence within long video sequences. Recent Video Large Language Models (Video-LLMs) have shown promising reasoning abilities when aligned with reinforcement learning, yet existing approaches typically rely on outcome-based rewards that supervise only the final prediction. Such supervision provides limited guidance on how models should discover the relevant temporal evidence during intermediate reasoning. In this work, ...

---

### 43. RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement

**Authors:** Zi-Xiang Ni, Bo-Lun Huang, Teng-Fang Hsiao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05088v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05088v1)

**Summary:** Text-to-image (T2I) diffusion models have achieved striking progress but still struggle to synthesize rare concepts involving unusual attribute-object pairings, often resulting in concept omission or semantic drift where a dominant entity overwhelms the generation. Tracing these failures to a lack of compositional balance during the denoising trajectory, we propose RADIANCE, a training-free framework that treats inference as a closed-loop feedback process. RADIANCE augments pretrained backbones ...

---

### 44. LangLoc: "Tell Me What You See"

**Authors:** Shaurya Kishore Panwar, Roham Zendehdel Nobari, Shirley Feng Yi Lau, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05077v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05077v1)

**Summary:** We tackle fine-grained indoor localization from natural language: given a free-form description of one's surroundings, estimate the observer's 2D position and heading within a known 3D environment. Language queries are lightweight, privacy-preserving, and need no camera - yet prior work stops at coarse scene retrieval and cannot resolve an intra-scene pose. We close this gap with LangLoc, a three-stage pipeline that (i) retrieves the correct scene via a dual-branch GATv2 encoder with CLIP semant...

---

### 45. Consistent and Editable: A Balanced Framework for Text-Guided Video Editing

**Authors:** Tao Jin, Li Xiao

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05056v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05056v1)

**Summary:** Recently, diffusion models have achieved considerable success in the text-guided video editing domain. However, existing works often struggle to balance the trade-off between temporal consistency and editability in video editing, with consistency and editability typically being inversely related. To address this, we propose a high-quality video editing framework enhanced for consistency and editability, named EquiEdit, which improves coordinatively the temporal consistency and editability of the...

---

### 46. RUFNet: Query-Guided Support Mask Refinement and Uncertainty Fusion based on Hybrid Mamba for Few-Shot Brain Tumor Segmentation

**Authors:** Dongyi He, Xiangkai Wang, Binbing Xu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05035v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05035v1)

**Summary:** Few-shot brain tumor segmentation remains challenging due to noisy support masks, inter-patient variations between support and query images, and the lack of pixel-wise confidence estimation. This study proposes RUFNet, a Hybrid Mamba-based few-shot framework that combines support mask refinement with uncertainty-aware posterior fusion. To preserve support-query dependencies with manageable cost, RUFNet adopts a Hybrid Mamba interaction backbone with linear complexity. To reduce support-mask nois...

---

### 47. Beyond Modality Fusion: Deep Ensembles for Multimodal Classification

**Authors:** Ilya Burenko, Dmitry Vetrov

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05019v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05019v1)

**Summary:** In multimodal classification, late-fusion approaches classify concatenated modality-specific features extracted by unimodal neural networks.   When modality imbalance is pronounced, various regularization techniques have been proposed to balance the learning process and overcome the inferior performance of late-fusion networks.   In contrast, this work demonstrates that multimodal data can be effectively classified without any explicit modality fusion, using deep ensembles of unimodal networks. ...

---

### 48. Comparison of Loss Functions for Robust Deep Learning-based Echocardiography Segmentation when Learning with Partially Labelled Data from Multiple Domains

**Authors:** Iman Islam, Esther Puyol-Antón, Bram Ruijsink, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05008v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05008v1)

**Summary:** Echocardiography is the first imaging modality used for assessing cardiac function, and accurate segmentation of cardiac structures is essential for deriving biomarkers. However, the development of effective automated segmentation models for multiple cardiac structures is challenged by the difficulty of training on datasets from different sources that are often partially-labelled. This study aims to address this challenge by evaluating the performance of three loss functions - adaptive categoric...

---

### 49. Unsupervised Pixel-Level Semantic Left-Right Understanding of In-the-Wild Images

**Authors:** Weikang Wang, Tobias Weißberg, Florian Bernard

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05006v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05006v1)

**Summary:** While various works address reflective symmetry understanding in 3D data and images, pixel-level semantic left-right prediction of in-the-wild images remains challenging, due to certain difficulties including the lack of 3D information, occlusion, object pose variation, partiality, etc. In this work, we propose an unsupervised learning framework to tackle this challenge. Leveraging recent advances in vertex-wise semantic left-right understanding of 3D data, our unsupervised learning method joint...

---

### 50. Geometry-aware Depth-guided Representation Learning for Structure-preserving Low-light Image Enhancement

**Authors:** Fang Gao, Jiongkai Qin, Jiabao Wang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05005v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05005v1)

**Summary:** Low-light degradation reduces image visibility and weakens structural cues that are important for visual representation and scene understanding. Existing low-light image enhancement methods mainly focus on appearance restoration, while insufficiently exploiting scene geometry to preserve structural consistency. To address this limitation, this paper proposes a Depth-guided Multi-scale Attention Network (DMSA-Net) for geometry-aware low-light image enhancement. DMSA-Net introduces depth-related s...

---

## cs.LG

**50 papers**

### 1. From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

**Authors:** Wenhao Li, Xueying Jiang, Quanhao Qian, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05396v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05396v1)

**Summary:** Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...

---

### 2. Weak-to-Strong Generalization via Direct On-Policy Distillation

**Authors:** Shiyuan Feng, Huan-ang Gao, Haohan Chi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05394v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05394v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL we...

---

### 3. Interpretable Human-Label-Free Deep Learning for Real-Bogus Classification with Uncertainty Quantification

**Authors:** Raphaël Bonnet-Guerrini, Bruno Sanchez, Dominique Fouchez, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05393v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05393v1)

**Summary:** Time-domain surveys generate many transient candidates, making Real-Bogus classification a critical step in automated discovery pipelines. Reliable labels are costly, while community labels can be noisy and survey-dependent. We aim to develop a Real-Bogus classification framework that can be trained without human-labeled data using injected transients and bogus-dominated survey data, remains robust under strong class contamination, and provides calibrated uncertainty quantification. We combine s...

---

### 4. LLM-as-a-Verifier: A General-Purpose Verification Framework

**Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05391v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05391v1)

**Summary:** Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that p...

---

### 5. What Does a Discrete Diffusion Model Learn?

**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05381v1)

**Summary:** What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the da...

---

### 6. TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning

**Authors:** Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05380v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05380v1)

**Summary:** In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyperparameters for all underlying MLPs, which requires hyperparameter tuning for achieving the best performance. In this work, we introduce TabPack, an efficient MLP ensemble with strong out-of-the-box performance and reduced reliance on traditional tuning. In a single run, TabPack samples and trains ma...

---

### 7. CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents

**Authors:** Yujiang Li, Zhenyu Hou, Yi Jing, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05378v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05378v1)

**Summary:** Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs wi...

---

### 8. Fitted Occupancy-Ratio Evaluation without Bellman Completeness

**Authors:** Lars van der Laan, Nathan Kallus

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05375v1)

**Summary:** Occupancy ratios correct distribution shift in offline reinforcement learning and are central to off-policy evaluation. Existing primal-dual and minimax methods typically estimate these ratios by enforcing occupancy-balance moments over a critic class. We propose fitted occupancy-ratio evaluation (FORE), a fitted fixed-point method that characterizes the discounted occupancy ratio through an adjoint Bellman recursion. At each iteration, FORE solves a single-level density-ratio objective on one-s...

---

### 9. GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Letian Fu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05369v1)

**Summary:** For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and in...

---

### 10. Faithfulness to Refusal: A Causal Audit of Neuron Selectors

**Authors:** Ananth Eswar, Pratinav Seth, Utsav Avaiya, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05355v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05355v1)

**Summary:** Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across fi...

---

### 11. Selective Disclosure Watermarking for Large Language Models

**Authors:** Xuyang Chen, Xiang Li, Yangxinyu Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05353v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05353v1)

**Summary:** Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...

---

### 12. Multiplayer Interactive World Models with Representation Autoencoders

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05352v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05352v1)

**Summary:** We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...

---

### 13. TREK: Distill to Explore, Reinforce to Refine

**Authors:** Yuanda Xu, Zhengze Zhou, Kayhan Behdin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05339v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05339v1)

**Summary:** Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure that uses distillation not for imitation but for exploration support expansion. A key advantage of TREK is its generality: because it only consumes verified output trajectories, it ca...

---

### 14. How Far is Too Far? Defining the Distance Threshold for Verification Siamese Networks

**Authors:** Heloísa Dias Viotto, Cauê Samonek, Lucas Garcia Pedroso, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05329v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05329v1)

**Summary:** Siamese verification networks are widely used to compare items such as faces, cars, or signatures. In these scenarios, the network is trained to learn an embedding space in which similar objects are mapped closer together, while dissimilar objects are mapped further apart. Two objects are considered to belong to the same class (e.g., the same person in two different images) when the distance between their embeddings falls below a predefined threshold. Defining this threshold, however, is a non-t...

---

### 15. Topological Shape Representation for Aneurysm -- Bifurcation Detection

**Authors:** Akshay Gokhale, Mansi Dhamne

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05317v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05317v1)

**Summary:** Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteris...

---

### 16. How Much is Left? LLMs Linearly Encode Their Remaining Output Length

**Authors:** Mohamed Amine Merzouk, Dmitri Carpov, Mirko Bronzi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05316v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05316v1)

**Summary:** Large language models generate one token at a time, yet their responses show remarkably consistent length structure: step-by-step solutions converge in predictable token counts, retrievals stop after a few sentences, retractions extend responses by measurable amounts. We ask whether the model carries an internal estimate of how much response remains. Training minimal-capacity linear probes on frozen hidden states of three open-weight 7-8B models across seven completion-style datasets, we find th...

---

### 17. Quantum Spectral Anomaly Detection

**Authors:** Yewei Yuan, Michele Minervini, Mark M. Wilde, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05307v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05307v1)

**Summary:** A core task in quantum anomaly detection is to compute an anomaly score that quantifies how strongly a test quantum state deviates from a given quantum dataset assumed to be normal. Classically, principal component analysis (PCA) for centered data computes the anomaly score by evaluating the test sample relative to the subspace spanned by the selected leading eigenvectors. However, for quantum data that lack a standard centering, explicitly recovering principal eigenvectors, constructing full Gr...

---

### 18. Biologically Informed Deep Neural Networks for Multi-Omic Integration, Pathway Activity Inference and Risk Stratification in Cancer

**Authors:** Pedro Henrique da Costa Avelar, Le Ou-Yang, Min Wu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05306v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05306v1)

**Summary:** Integrating complex, multi-omics data presents significant challenges. Existing approaches often face a trade-off between model interpretability and representational capacity, with most either relying on post-hoc interpretation or use linear models that may overlook complex interactions. We report Pathway Activity Autoencoders for the multi-omics setting, which embed prior knowledge via pathway-informed architectural constraints, fostering interpretability, while preserving representational powe...

---

### 19. Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning

**Authors:** Fabien Polly

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05300v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05300v1)

**Summary:** Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the eval...

---

### 20. Air Quality Downscaling with Station-Guided Pseudo-Supervision

**Authors:** Guorun Wang, Simone Foti, Andreas D. Demou, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05292v1)

**Summary:** Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover...

---

### 21. Wavelet Scattering Transform for Interpretable Schizophrenia Biomarker Discovery and Classification from Resting-State EEG

**Authors:** Md. Taksimul Ahsan Tawhid, Nasif Ahmed Rafe, Alif Tahmid Priyom, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05282v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05282v1)

**Summary:** Schizophrenia is a debilitating neuropsychiatric disorder characterized by profound cortical network dysregulation, for which objective, clinically translatable EEG based biomarkers remain underdeveloped. Existing automated classification pipelines rely predominantly on static power spectral density features inherently blind to amplitude modulation dynamics and cross-frequency coupling, phenomena central to schizophrenia pathophysiology, while adopting epoch level cross validation strategies tha...

---

### 22. Routing Anonymity and Identifiability of Noisy Quantum Hardware

**Authors:** Ben Priestley, Mina Doosti

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05281v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05281v1)

**Summary:** Present-day quantum computing is cloud-based, where a user submits a circuit to a service provider's proprietary backend hardware. While providers may wish to hide implementation details, scheduling choices, or even which physical device was used, noisy finite-shot outputs can carry backend-specific fingerprints: information imprinted in the classical output distribution that can reveal the backend identity. So far, such fingerprints have mostly been studied from a benchmarking perspective, with...

---

### 23. Advances in Neural Controlled Differential Equations

**Authors:** Benjamin Walker

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05280v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05280v1)

**Summary:** Many real-world systems evolve continuously, yet most machine learning models interpret time series as discrete sequences. Continuous-time approaches instead treat time series as samples from an underlying input path, a formulation that naturally accommodates irregularly sampled or oversampled data. Among these, Neural Controlled Differential Equations (NCDEs) are a maximally expressive class of models that parametrise a vector field using a neural network and evolve their hidden state by solvin...

---

### 24. Untrusted Content Masking for Web Agents with Security Guarantees

**Authors:** Kristina Nikolić, Egor Zverev, Javier Rando, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05277v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05277v1)

**Summary:** Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which int...

---

### 25. Adaptive Inference Batching using Policy Gradients

**Authors:** Ruslan Sharifullin

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05272v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05272v1)

**Summary:** Inference serving systems must balance throughput and latency under bursty, heterogeneous workloads, yet the industry standard remains static batching policies that require manual tuning and cannot adapt to shifting traffic. We investigate whether reinforcement learning (RL) can learn adaptive batching and routing policies that outperform these heuristics, training REINFORCE and PPO agents on a discrete-event simulator validated against queuing theory and production traces (Azure Functions, Burs...

---

### 26. Target-Guided Selective Reweighting for Physics-Informed Neural Network Inverse Problems: A Transfer Learning Approach

**Authors:** Qian Hu, Bin Fan, Yao Xiao, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05271v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05271v1)

**Summary:** Physics-informed neural networks (PINNs) encounter ill-posed optimization, loss competition, and parameter compensation in partial differential equation (PDE) inverse problems. Transfer learning can reuse representations from source tasks, but direct fine-tuning may introduce negative transfer when dominant physical mechanisms, governing parameters, or observation noise differ between source and target domains: the model achieves low field error yet recovers incorrect target physical parameters....

---

### 27. Is the Geometry Doing the Work? An Operating-Point Audit of Hierarchy in Hyperbolic Vision-Language Models

**Authors:** Jaeyoung Kim, Eunseok Kim, Dongsuk Jang

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05268v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05268v1)

**Summary:** Whether a hyperbolic representation model uses its geometry cannot be read off its curvature parameter: what matters is the dimensionless operating point $\sqrt{c}ρ$ and whether the radial and cone machinery is active there. We develop a battery of necessary-condition diagnostics and audit three published hyperbolic vision-language families -- MERU, HyCoCLIP, and PHyCLIP -- across released checkpoints and controlled interventions on a fixed GRIT snapshot, identifying three failure modes. First, ...

---

### 28. SalAngaBhava: A Sinhala Market Dataset for Aspect-based Sentiment Analysis

**Authors:** Lakshani Galwatta, Nisansa de Silva, Sarangi Aththanayake, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05259v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05259v1)

**Summary:** Sentiment analysis has been a primary domain under Natural Language Processing (NLP) from its inception as it plays a vital role in both real-world and research applications. In high-resource languages, this has been extended a step further, and instead of predicting sentiment at the sentence level, models have been developed to detect more fine-grained sentiments at aspect level. However, in order to conduct this fine-grained Aspect-based Sentiment Analysis (ABSA), datasets annotated with aspec...

---

### 29. GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation

**Authors:** Zherui Huang, Guanjie Zheng, Hao Xue, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05257v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05257v1)

**Summary:** Origin-destination (OD) flow modeling underpins urban planning and mobility analysis, but prevailing graph-based methods often neglect salient geographic attributes, limiting their ability to model long-range and multi-area dependencies. In this paper, we introduce GeoFlow, a novel framework that (i) augments area representations with geospatial attributes, including relative positions, k-hop and geodesic distances, (ii) employs a specialized geometric-intrinsic fusion encoder design that combin...

---

### 30. FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation

**Authors:** Weichen Qin, Yufan Xie, Peihao Wang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05252v1)

**Summary:** Simulation-Based Inference (SBI) is critical for scientific discovery, with generative models offering a promising path toward efficient inference. However, existing methods struggle with effective multimodal modeling. They often rely on brute-force fusion strategies that ignore the structural disparities between parameters and observations, thus limiting estimation fidelity. In this work, we introduce FUSE (Feynman-Kac steered mUlti-modal flow matching for efficient Simulation-based posterior E...

---

### 31. Privacy-Preserving Robustness Verification for Neural Networks

**Authors:** Nianyun Song, Xiaokun Luan, Yu Guo, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05251v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05251v1)

**Summary:** Neural network verification and data privacy are inherently in tension: verification demands full access to model parameters and input data, yet both are increasingly restricted by privacy regulations and intellectual property constraints. This tension has left robustness verification impractical in privacy-sensitive domains. In this work, we address this gap with SecureCROWN, the first framework for privacy-preserving neural network robustness verification. Built upon secure two-party computati...

---

### 32. CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling

**Authors:** Zuwang He, Shihao Shu, Yuli Qu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05242v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05242v1)

**Summary:** Personalized incentive allocation is vital for e-commerce, where uplift modeling is the standard for estimating Individual Treatment Effects (ITE). However, traditional models often fail in complex multi-seller environments with violations of the Stable Unit Treatment Value Assumption (SUTVA). We identify two critical challenges: Seller-level Cannibalization, where incentives shift expenditure between shops without growing the platform, and Incentive-level Cannibalization, where organic conversi...

---

### 33. Optimizing ML Workload Partitioning between CPUs and CIM Accelerators for Heterogeneous Computing

**Authors:** Joel Klein, Rebecca Pelke, Roberto Laudani, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05240v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05240v1)

**Summary:** Computing-in-Memory (CIM) accelerators execute Matrix-Vector Multiplications (MVMs) in memory, making them a compelling solution for Machine Learning (ML) workloads. However, existing ML workload partitioning approaches for CIM accelerators do not fully account for Resistive Random Access Memory (RRAM) constraints such as limited memory, high write latency, and limited endurance. They also neglect parallelism, low-level architectural effects, or the Central Processing Unit (CPU) as a complementa...

---

### 34. Video-based detection of cessation of breathing in pre-term infants using machine learning

**Authors:** Dineo Serame, Lionel Tarassenko, Mauricio Villarroel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05230v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05230v1)

**Summary:** Pre-term infants are susceptible to potentially harmful apnoea-related cessations of breathing due to immature respiratory control. However, reliable respiratory monitoring in the neonatal intensive care unit (NICU) remains challenging because motion artefacts, sensor displacement, and skin fragility can compromise contact-based measurements. Non-contact video monitoring offers a complementary approach that does not depend on adhesive sensors while providing additional respiratory information.  ...

---

### 35. msPCA: An R Package for Sparse PCA with Multiple Components

**Authors:** Ryan Cory-Wright, Jean Pauphilet

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05229v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05229v1)

**Summary:** We present msPCA: an open-source R package for sparse principal component analysis with multiple components. It implements an alternating maximization algorithm to generate a set of sparse loading vectors that collectively explain a large fraction of the variance in a dataset, while remaining non-redundant. The algorithm supports two definitions of non-redundancy: either orthogonality of the loading vectors or zero pairwise correlation between principal components (PCs). In the reported benchmar...

---

### 36. Probing Geospatial SSL Representations with Environmental Signals

**Authors:** Rohita Mocharla, Vishal M. Patel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05207v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05207v1)

**Summary:** Self-supervised learning (SSL) is designed to learn generic, transferable representations rather than representations optimized for a single task. Most geospatial benchmarks evaluate representations solely through downstream tasks, providing limited insight into the information encoded within the representation itself. We ask a different question: do SSL representations of satellite imagery preserve statistical associations with environmental variables that co-vary with the imaging process? To a...

---

### 37. FlatManifold: Robust Continual Learning under Severe Label Noise and Domain Shifts via Intrinsic Manifold Flattening

**Authors:** Rai Hisada, Kanji Tanaka

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05201v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05201v1)

**Summary:** In non-stationary streaming environments, simultaneously adapting to complex, non-linear domain shifts via continual learning while mitigating the catastrophic effects of severe, uncalibrated label noise poses a fundamental mathematical challenge. In this paper, we propose \FlatManifold{}, a novel, streamlined robust continual learning framework that utilizes a Nyström manifold flattening map based on the kernel trick and projection onto an orthogonalized Reproducing Kernel Hilbert Space (RKHS)....

---

### 38. Noisy-Channel Minimum Bayes Risk Decoding

**Authors:** Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05198v1)

**Summary:** Minimum Bayes Risk (MBR) decoding yields more robust and higher-quality text generation than maximum a posteriori (MAP) decoding by selecting hypotheses that maximize expected utility over sampled pseudo-references. However, there exists a discrepancy in the design: hypothesis selection calculates expected utility scores conditioned on given pseudo-references, while commonly used evaluation metrics, e.g., BLEU and COMET, are asymmetric. Therefore, it is important to consider both hypothesis-to-r...

---

### 39. Unified Audio Intelligence Without Regressing on Text Intelligence

**Authors:** Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05196v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05196v1)

**Summary:** Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...

---

### 40. Latent Programming Horizons in Coding Agents

**Authors:** André Silva, Han Tu, Martin Monperrus

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05188v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05188v1)

**Summary:** A coding agent solving a software-engineering task spends dozens of steps reasoning, editing code, and running tests, yet little is known about what the underlying language model internally represents about the program it is working on. We show that the residual streams of language models under coding agents linearly encode properties of the evolving program: a logistic-regression probe on hidden states is able to decode whether the current code parses, passes its test suite, reduces the number ...

---

### 41. SMART: A Machine Learning and Monte Carlo Framework for Rapid Analysis of Stochastic Transistor Aging and Process Variation in Digital Circuits

**Authors:** Arash Esshaghi, Siavash Es'haghi, Gholamreza Shahabadi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05187v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05187v1)

**Summary:** As CMOS technology scales into the deep nanometer regime, digital circuit reliability is increasingly threatened by the combined stochastic effects of Bias Temperature Instability (BTI) and Process Variation (PV). Traditional reliability analysis methods, which rely on computationally intensive simulations or extensive lookup tables, fail to scale efficiently for large designs, creating a critical bottleneck in design space exploration. To address this, we propose SMART, a novel framework that i...

---

### 42. Rethinking On-Policy Self-Distillation for Thinking Models

**Authors:** Simran Kaur, Narutatsu Ri, Yinghui He, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05184v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05184v1)

**Summary:** Self-distillation is a promising recipe for self-improvement in language models. In this setting, a model can serve as its own teacher when given privileged information, such as a solution to a math problem. This seems especially appealing for thinking models, which can use test-time reasoning to absorb the privileged information. Surprisingly, we show that privileged self-distillation degrades thinking models on long reasoning traces: across five Qwen3 and OLMo thinking models evaluated on AIME...

---

### 43. Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets

**Authors:** Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05179v1)

**Summary:** In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning,...

---

### 44. Platonic Projection Structures: Operator-Induced Observability in Representation Learning

**Authors:** Kazuo Ishii, Bishnu Prasad Gautam, Jieling Wu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05175v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05175v1)

**Summary:** We characterize observability in representation learning through Platonic Projection Structures (PPS), an operator-theoretic framework for analyzing representation accessibility under partial observation. Rather than treating observable outputs as direct reflections of latent representations, PPS models observation through a self-adjoint positive semidefinite operator acting on a latent representation space. A system is represented as a triple $(H, Π, O)$, where $H$ is a latent representation sp...

---

### 45. MeGA-MP: Metric Graph Advection Message Passing -- A Physics-Informed Message Passing Operator for Advection-Dominated Metric Graphs

**Authors:** Janine Strotherm, Luca Hermes, André Artelt, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05167v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05167v1)

**Summary:** Many real-world systems are organized as networks where spatio-temporal dynamics unfold along connections and not discretely between nodes. Examples include utility networks such as water distribution systems or gas networks, electrical grids, and traffic flow networks. Such systems are naturally modeled as metric graphs, where edges correspond to one-dimensional Euclidean subspaces connected at vertices. Metric graphs are independent of an underlying global Euclidean space, limiting direct appl...

---

### 46. Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech

**Authors:** Benjamin Ballyk, Teyun Kwon, Miran Özdogan, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05165v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05165v1)

**Summary:** Non-invasive brain-to-speech decoding aims to restore communication to patients suffering from neurodegenerative disease, without the risks of neurosurgery. Existing MEG- and EEG-based methods, while scalable, continue to suffer from high word error rates driven by relatively low signal-to-noise ratios compared to invasive recordings. We propose physiological noise augmentation (PNA), a data augmentation method that explicitly trains decoders to become invariant to task-agnostic artifacts (e.g. ...

---

### 47. EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments

**Authors:** Deyao Zhu, Xin Zhou, Shengling Qin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05155v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05155v1)

**Summary:** Pretraining scaling laws reveal that model capability improves predictably with data and compute. But learning from real world environments after deployment remains far less understood. Analyzing roughly 38,000 hours of agent interaction with the environment across 134 real world tasks, we find, to the best of our knowledge, the first evidence that overall performance during environment learning follows a log-sigmoid scaling law with remarkably high precision, reaching R^2 = 0.998. Across model ...

---

### 48. Geometric Causal Models

**Authors:** Eli N. Weinstein, David M. Blei

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05153v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05153v1)

**Summary:** Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...

---

### 49. PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference

**Authors:** Akshat Jani, Prathamesh Gadekar, Sakhinana Sagar Srinivas, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05134v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05134v1)

**Summary:** We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines. The workflow links problem specification, data generation, operator training, and checkpoint-based inference. A stateful input graph converts multi-turn natural-language input and user edits into validated problem specifications. The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element back...

---

### 50. Physically-Relevant Information Learning in High-Dimensional Time-Derivatives Spaces

**Authors:** Domiziano Doria, Matteo Becchi, Giovanni M. Pavan

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05127v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05127v1)

**Summary:** Understanding the physics of many-body complex dynamical systems is typically non-trivial. High-dimensional analysis approaches are often deemed necessary to prevent losing important information. Typically, these use order parameters or descriptors capturing information related to, e.g., relative positions, symmetries, etc., of the units in the studied system. However, in many cases, gaining information related to the relative positions (or velocities) of the constitutive units alone may be insu...

---

## cs.NE

**50 papers**

### 1. An event-driven framework for fly-inspired visual motion detection

**Authors:** Qinbing Fu, Jingyu Huang, Yan Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05205v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05205v1)

**Summary:** Fast and reliable motion detection is essential for machine vision and autonomous systems operating in dynamic environments. This work integrates emerging event-based sensing with biologically structured neural computation to establish an efficient computational paradigm for visual motion detection. The proposed framework is built upon a recently developed fly-inspired neural network that emulates motion-processing circuits in the optic lobe. Owing to its feed-forward and training-free architect...

---

### 2. LLM for the development of FCM

**Authors:** Alexis Kafantaris

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04983v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04983v1)

**Summary:** This article is about the development of a fuzzy cognitive map using a local large language model. In the light of recent advances it is evident that large language models, and even local large language models are capable of extracting quantities from textual data. In other words, a local LLM like Qwen2.5-32B, or probably larger, can accept entities as prompt input and determine relevant quantitative data as the model output. In turn, this output can be utilized for the construction of a data dr...

---

### 3. A Large-Scale Sparse Multiobjective Optimization Algorithm Based on Optimal Performance Scores

**Authors:** Jia-Lin Mai, Min-Rong Chen, Guo-Qiang Zeng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04765v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04765v1)

**Summary:** Large-scale sparse multiobjective optimization problems (LSSMOPs) involve a large number of decision variables and Pareto optimal solutions with only a few nonzero variables. However, as the number of decision variables grows, it becomes increasingly challenging to accurately identify the nonzero variables, and optimization performance is adversely affected. To address these issues, this paper proposes an evolutionary algorithm for LSSMOPs. Specifically, we propose a new initialization method ca...

---

### 4. Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models

**Authors:** MY Pitsane, Hope Mogale

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04562v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04562v1)

**Summary:** Large language models (LLMs) generate fluent outputs that can be wrong. Unlike humans, who often exhibit cues when providing false information, LLMs produce errors that are difficult to detect because autoregressive decoding provides no mechanism for verifying intermediate reasoning before state progression. We introduce Heaviside Continuity of Rolling Coefficients (HCRC), a verification-first execution framework that reformulates inference as predicate-gated state transitions governed by a Heav...

---

### 5. Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures

**Authors:** Joy Bose

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02967v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02967v1)

**Summary:** Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence betwee...

---

### 6. Microcosmos: Reimagining Artificial Life for the GPU Era

**Authors:** Mark Tensen, Ciaran Regan, Bert Wang-Chak Chan, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02954v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02954v1)

**Summary:** Most artificial life simulators either operate on abstract substrates disconnected from physical reality, or simulate physically grounded worlds that do not scale to the population sizes required for open-ended evolution. We present Microcosmos, a simulation engine in which artificial lifeforms are modeled as elastic filament chains inhabiting a two-dimensional viscous fluid world, designed from the ground up for modern GPU hardware and end-to-end differentiable simulation. We validate the engin...

---

### 7. A Spiking Sequence Generator for Polar Trajectories on Neuromorphic Hardware

**Authors:** William R. P. Nourse, Roger D. Quinn

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02753v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02753v1)

**Summary:** Neuromorphic controllers for size, weight, and power-constrained systems require neural architectures that are both energy-efficient and interpretable at the level of system dynamics. However, existing approaches either rely on end-to-end trained spiking networks with limited interpretability, or on converted classical controllers that fail to fully exploit neuromorphic dynamics. We present a spiking neural network (SNN) architecture for generating polar trajectories, using a winner-take-all (WT...

---

### 8. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 9. Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem

**Authors:** Zitouni Rania, Mostefai Mounir Sofiane, Tati Youcef, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02315v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02315v1)

**Summary:** The one-dimensional bin packing problem (1D-BPP) is a canonical NP-hard combinatorial optimization problem with broad industrial applications. We propose RL-HGGA, a hybrid algorithm that integrates Falkenauer's Hybrid Grouping Genetic Algorithm (HGGA) with a tabular Q-learning controller. Rather than applying genetic operators at fixed probabilities, a Q-learning agent dynamically selects among eight macro-actions -- including BPCX crossover, light and heavy mutation, Martello-Toth local search,...

---

### 10. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**Authors:** Juwei Shen, Yujie Wu, Changwen Chen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02283v1)

**Summary:** In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs. Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions. We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewin...

---

### 11. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 12. Electronic Bursting Neuron: design, equations and hardware implementation

**Authors:** Lev V. Takaishvili, Vladimir I. Ponomarenko, Maksim V. Kornilov, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02122v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02122v1)

**Summary:** Electronic neurons are a keystone for construction of the spiking neural networks which have numerous applications in neuroprosthetics, artificial memory, intensive calculations etc. A number of concepts of electronic neurons has been already proposedm with some of them implemented in hardware. However, new schemes are of significant interest since the existing ones do not fit all requirements: either they are too complex and expensive in realization, or they are not able to demonstrate all dema...

---

### 13. Evolutionary Wave Function Collapse

**Authors:** Dipika Rajesh, Ahmed Khalifa, Julian Togelius

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02082v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02082v1)

**Summary:** Wave Function Collapse (WFC) is a widely used procedural content generation method that learns local adjacency constraints from example inputs to generate larger outputs. In this paper, we explore combining WFC with evolutionary search by evolving the small input examples used by WFC rather than directly evolving complete levels. In this approach, WFC acts as a genotype-to-phenotype mapping. The generated levels are then evaluated through domain-specific fitness functions. We evaluate the method...

---

### 14. Mechanism and Stability Analysis of Metabolic Closed-Loop Metaheuristics

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01551v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01551v2)

**Summary:** This paper studies the Metabolic Multi-Agent Optimizer (MMAO) at the framework level rather than at the implementation or benchmark level. The central question is whether the metabolic resource loop of private energy, communal budget, role drift, and lifecycle turnover has a framework-level interpretation beyond narrative metaphor. We introduce a generic MMAO state model that abstracts away domain-specific move operators while retaining the resource bookkeeping that defines the framework. Under ...

---

### 15. MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01539v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01539v2)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation...

---

### 16. BFF: Simple explanations for complex phenomena

**Authors:** Charlotte Knierim, Luca Versari, Robert Obryk, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01483v1)

**Summary:** The ''Computational Life'' paper (Agüera y Arcas et al., 2024) argues that paired interactions in a computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found at least as easily using simple mutation random walks in program space. We also explore the claim that capping the maximum ''depth'' and ''width'' of the ancestry tree stops self-replicators...

---

### 17. Towards transferable lightweight neuromorphic computing through a model-free temporal-switch framework

**Authors:** Zefeng Zhang, Chao Li, Siyao Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.02608v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02608v1)

**Summary:** Lightweight neuromorphic computing offers a promising route to efficient AI, with particular benefits for resource-constrained edge deployments. However, its scalable deployment that can reliably transfer the expected performance has long been hindered by device-to-device variations, which necessitate costly and repeated re-training on new copies and undermine the practical advantages. To address this issue, we introduce a model-free temporal-switch (TS) framework to improve the direct transfer ...

---

### 18. MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00846v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00846v2)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic cont...

---

### 19. From Consistency to Collaborative Discovery: MFEA-CoD for Multitask Novelty Search

**Authors:** Jiao Liu, Yanchi Li, Hua Yu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00761v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00761v2)

**Summary:** Evolutionary multitasking (EMT) has shown strong capability in solving multiple optimization problems simultaneously by exploiting latent inter-task consistency, such as similarities in promising solutions or search directions. However, most existing EMT studies remain focused on objective-driven optimization, where such consistency is mainly used to accelerate convergence toward predefined optima. In this paper, we move EMT from consistency to collaborative discovery and propose a multifactoria...

---

### 20. Self-Organized Learning in Oscillatory Neural Networks with Memristive Signed Couplings

**Authors:** Riley Acker, Aman Desai, Garrett Kenyon, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00286v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00286v1)

**Summary:** Oscillatory neural networks (ONNs) have emerged as a promising neuromorphic architecture, leveraging coupled dynamical systems to perform computation and represent information through phase relationships. Their interactions can be designed to support intrinsic energy-minimizing dynamics, enabling tasks such as associative memory and optimization, and positioning them as a candidate architecture for continuous learning and inference. We present a neuromorphic primitive implemented using memristiv...

---

### 21. EVOTS: Evolutionary Transformer Search for Time Series Forecasting

**Authors:** AbdElRahman ElSaid, Damir Pulatov

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00154v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00154v1)

**Summary:** Evolutionary neural architecture design for multivariate time-series forecasting remains underexplored, with most approaches relying on fixed Transformer architectures despite substantial variation across tasks and forecasting settings. This paper introduces an evolutionary neural architecture search framework for discovering task-adaptive Transformer-like models for time-series forecasting (EVOTS). Architectures are encoded using a modular genome representation that enables flexible composition...

---

### 22. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 23. Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

**Authors:** Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31789v1)

**Summary:** Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associ...

---

### 24. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 25. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31584v2) | 📄 [PDF](https://arxiv.org/pdf/2606.31584v2)

**Summary:** This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...

---

### 26. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 27. Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization

**Authors:** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30836v1)

**Summary:** Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, w...

---

### 28. Why can genetic algorithms work in high-dimensional search spaces?

**Authors:** Stephen Whitelam

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30619v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30619v1)

**Summary:** We show that the effective dynamics of the elitist $(1+M)$ genetic algorithm is, in the limit of small mutations, clipped gradient descent on the loss in the presence of anisotropic Gaussian white noise. In expectation, therefore, a simple mutation-selection genetic algorithm follows the gradient of the loss, without explicit calculation of gradients and without averaging over loss evaluations. The genetic algorithm is slower than gradient descent because of the noise that acts in directions tra...

---

### 29. Computing the Integral R2 Indicator by Perspective Mapping and Box Decomposition

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30530v4) | 📄 [PDF](https://arxiv.org/pdf/2606.30530v4)

**Summary:** The continuous integral R2 indicator is a Pareto-compliant refinement of the classical finite-weight-vector R2 indicator, used in performance assessment, bounded archiving for a-posteriori multi-objective optimization, and skyline selection in databases. This work introduces a bidirectional perspective mapping between continuous integral R2 computation and integration over unions of anchored axis-aligned boxes. After translating the ideal point of a minimization problem to the origin, approximat...

---

### 30. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30450v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30450v2)

**Summary:** This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. ...

---

### 31. From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent

**Authors:** Haoliang Han

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30191v1)

**Summary:** How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer r...

---

### 32. Semantics-Aware Bilevel Co-Evolution: Towards Automated Multicomponent Algorithm Design

**Authors:** Zhiyao Zhang, Shenghao Wu, Xingyu Wu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29953v1)

**Summary:** LLM-assisted evolutionary search (LES) has emerged as a promising paradigm for automated algorithm design. However, existing methods usually suffer from two inherent limitations when facing the automated design of real-world complex algorithms that usually consist of multiple components. The first limitation is that they either focus on modifying entire algorithms, making it difficult to reuse high-quality components, or concentrate on component refinement within a limited set of predefined mult...

---

### 33. Evolutionary Hyperparameter Optimization to Find Lightweight CNN Models for Autonomous Steering

**Authors:** Devson Butani, Ryan Kaddis, Chan-Jin Chung

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29684v1)

**Summary:** This research investigates the optimization of Convolutional and Dense Neural Networks (CNNs and DNNs) for autonomous steering using the (N+M) Evolution Strategy (ES) with the 1/5th success rule. The primary objective is to develop a lightweight CNN based model capable of real-time steering angle prediction, mimicking human driving behavior on predefined paths. The ES algorithm automates hyperparameter tuning, dynamically adjusting parameters such as filter sizes and layer configurations. Data c...

---

### 34. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 35. Supervised Hebbian learning in Deep Counterstream Associative Networks

**Authors:** Andreas Knoblauch

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29528v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29528v1)

**Summary:** Modern machine learning applications employ deep neural networks training with the error backpropagation algorithm. Although this algorithm is very effective, it lacks biological realism. For example, backpropagation requires symmetric connectivity, and a separate neural processing channel for error signals. Prior works have therefore proposed a number of more realistic alternatives for error backpropagation. However, most of them still suffer from demanding preassumptions that may be not fulfil...

---

### 36. When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**Authors:** Zhengqi Pei, Qingming Huang, Shuhui Wang

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29354v1)

**Summary:** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the a...

---

### 37. Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs

**Authors:** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, et al.

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29254v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29254v1)

**Summary:** Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reaso...

---

### 38. Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning

**Authors:** Reza Ahmadvand, Sarah Safura Sharif, Yaser Mike Banad

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29099v1)

**Summary:** Artificial neural networks (ANN) provide accurate continuous-valued representation, whereas spiking neural networks (SNN) offer event-driven temporal processing, yet both paradigms face limitations when value encoding and timing dynamics must be learned within a single computational structure. This paper introduces a network based on Unified Complex-valued Neuron (UCN), a new neural computational model that integrates continuous activation and phase-driven event generation through an asymmetric ...

---

### 39. Road to scalability for efficient graph search on massively parallel neuromorphic hardware

**Authors:** Oskar von Seeler, Elena C. Offenberg, Carlo Michaelis, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28907v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28907v1)

**Summary:** Efficient computation of shortest paths in weighted graphs is a fundamental problem with many applications. Neuromorphic hardware platforms promise massively parallel, efficient computation, changing parallelism tradeoffs. In this work, we introduce NEURO-MAPP (Neuromorphic-based Min-Add Parallel Propagation), a distributed shortest path algorithm designed to use the local computation and network communication available in neuromorphic systems. We provide an optimized implementation of the algor...

---

### 40. Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28662v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28662v1)

**Summary:** The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studie...

---

### 41. Analysis of Parameter Settings for the Bat Algorithm Using Variance Evolution

**Authors:** Xin-She Yang, Mehmet Karamanoglu

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28644v1)

**Summary:** Parameter settings in evolutionary algorithms and metaheuristics are important because such parameter values can influence the performance of algorithms under evaluation. For a given algorithm, there are many different numerical experiments to show that the algorithm can work well in practice; however, in most cases there is no theoretical analysis of parameter settings. In this work, we show that theoretical analysis using the theory of dynamical systems and evolution of population variance can...

---

### 42. Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

**Authors:** Binh Nguyen, Colleen Josephson, Mircea Teodorescu, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28600v1)

**Summary:** Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement le...

---

### 43. Comparing Scalar Objective Functions for Multi-Criteria Engineering Optimization

**Authors:** Olaf Frommann

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28541v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28541v1)

**Summary:** Scalar objective functions are required when a multi-criteria optimization problem must yield a single preferred design rather than only a Pareto set. The choice of scalarization influences which compromise is selected, how preference parameters are interpreted, and whether non-supported Pareto regions can be reached. This paper compares four formulations for normalized bi-criteria minimization: weighted sums, achievement scalarizing functions, desirability functions, and a fuzzy-logic-based for...

---

### 44. MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28109v2) | 📄 [PDF](https://arxiv.org/pdf/2606.28109v2)

**Summary:** Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a comm...

---

### 45. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 46. Co-Optimization of Analog Kolmogorov-Arnold Networks for Low-Power Function Approximation in Flexible Electronics

**Authors:** Paula Carolina Lozano Duarte, Georgios Zervakis, Mehdi Tahoori, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27892v1)

**Summary:** Wearable devices and Internet of Things (IoT) sensors require on-sensor processing of biosignals and environmental data, including computationally demanding operations such as nonlinear activation functions for neural network inference, sensor calibration curves to map raw readings to physical units, and signal preprocessing functions like logarithmic compression and power operations for feature extraction. These functions exhibit significant complexity, often involving transcendental operations...

---

### 47. Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring

**Authors:** Muhammad Hamza

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.30676v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30676v1)

**Summary:** Deploying spiking neural networks (SNNs) on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies either neglect neuronal criticality or rely on convex relaxations of the inherently combinatorial pruning problem whose fractional masks, upon binarisation, destroy accuracy at moderate-to-high sparsity. We present Criticality-Constrained Quadratic Pruning (CQP), a native PyTorch pipeline that fuses weight magnitude with surrog...

---

### 48. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 49. DE-2LS: Differential Evolution with Lightweight Late Local Search for Constrained Numerical Optimization

**Authors:** Dikshit Chauhan, Anupam Trivedi

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27764v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27764v1)

**Summary:** Constrained single-objective numerical optimization requires a careful balance among feasibility, objective convergence, and computational efficiency under a fixed function-evaluation budget. This paper proposes DE-2LS, a late-stage, locally search-enhanced variant of differential evolution built on the RDEx framework. The proposed method preserves the original RDEx components, including mutation and crossover operators, success-history adaptation, archive mechanism, population-size reduction, a...

---

### 50. DE-2LS: Differential Evolution with Late-Stage local-search for Unconstrained Single-Objective Numerical Optimization

**Authors:** Dikshit Chauhan

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27762v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27762v1)

**Summary:** Unconstrained single-objective numerical optimization requires a careful balance among global exploration, late-stage exploitation, and function-evaluation efficiency. This paper presents DE-2LS, a late-stage, local-search-enhanced differential evolution framework built on RDEx for unconstrained single-objective optimization with variable bounds. The proposed method preserves the original RDEx evolutionary search engine and introduces two conservative refinements: a smoothed exploitation-biased ...

---

## q-bio.NC

**50 papers**

### 1. Beyond DSA: Conjugacy-based Comparison of Dynamical Systems

**Authors:** Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04493v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04493v1)

**Summary:** Comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements is a central problem in neuroscience and machine learning. Dynamical Similarity Analysis [DSA; Ostrow et al., 2023] addresses this problem by aligning finite-dimensional Koopman approximations through an orthogonal similarity transformation. Here we show that orthogonal alignment is neither necessary nor sufficient for topological conjugacy: conjugate systems may require a no...

---

### 2. Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

**Authors:** Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04063v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04063v1)

**Summary:** Multi-compartment Hodgkin-Huxley (HH) models provide a principled framework for predicting neural dynamics and responses to electrical stimulation. However, fitting HH biophysical parameters typically requires intracellular recordings, which are invasive and low-throughput, limiting the ability to capture the geometry and cell-specific properties of many neurons in a given neural circuit. Multi-electrode arrays (MEAs) offer a scalable alternative - high-density extracellular measurements from fu...

---

### 3. Microsecond-precision sound localization emerges from slow equilibrium dynamics

**Authors:** Toshio Irino

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03890v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03890v1)

**Summary:** Precise sound localization relies on microsecond sensitivity to interaural time differences (ITDs), yet binaural perception exhibits sluggish tracking of dynamic acoustic cues. How these properties coexist remains unresolved. Here, ITD is represented as a stable equilibrium of neural population dynamics rather than by the classical place-coding framework originally proposed by Jeffress in 1948. In this framework, excitatory and inhibitory interactions across frequency channels generate a populat...

---

### 4. Diffusion learning reveals viable parameter manifolds and compensation geometry in biological dynamical systems

**Authors:** Ruilin Zhang, Louis Tao, Zhuo-Cheng Xiao

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03671v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03671v1)

**Summary:** Models of complex systems often have many parameters, yet are constrained by far fewer experimentally accessible observables: similar activity can emerge from coordinated parameter changes. We formalize these compatible parameter sets as \emph{viable parameter manifolds}: the inverse images of a system's target dynamical behaviors under a parameter-to-feature map. The relevant codimension is not the number of reported features, but the effective rank of that map at the target scale. Co-varying f...

---

### 5. Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment

**Authors:** Houman Safaai, Maceo Richards, Bernardo L. Sabatini

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03556v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03556v1)

**Summary:** Biological neurons assign credit across branching dendrites, where synaptic drive, dendritic conductance, local voltage, and somatic teaching signals interact to shape synaptic plasticity. We study conductance-based dendritic networks with E/I synapse banks, shunting inhibition, and tree-structured branch-to-soma coupling, and examine when restricted somatic feedback can approximate compartment-specific backpropagated errors. Exact gradients factor into local eligibility x compartment error term...

---

### 6. Modeling the Impact of Visual Brand Language on Attention, Object Recognition, and Memory Retrieval

**Authors:** Rachel F. Heaton, John E. Hummel

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02929v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02929v1)

**Summary:** Visual brand language is the set of visual properties that convey brand identity for a product. What is the impact of visual brand language on a person's ability to recognize and understand the functional identity of an object? Using an empirically supported modeling framework based on the JIM model of object recognition and the LISA model of analogical inference, we simulated the impact of visual brand language on object recognition, the allocation of attention, and retrieval of functional info...

---

### 7. A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps

**Authors:** Barada Sahu, Shivesh Pandey

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01400v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01400v2)

**Summary:** Deep multimodal brain-encoding models now predict fMRI responses to naturalistic video with high accuracy; whether their predicted neural signals also forecast behavioral engagement is unknown. We run TRIBE, the winning model of the 2025 Algonauts challenge (Llama-3.2 + V-JEPA 2 + Wav2Vec-BERT), on 48 YouTube videos and reduce its predicted cortical response to a per-second engagement curve, the global field power. Correlated against each video's "most replayed" heatmap, a proxy for re-watch, it...

---

### 8. DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00851v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00851v1)

**Summary:** Brain activity spans single-neuron, population, and network levels, and core questions in neural coding require moving between them. Yet current tools target a single paradigm and incompatible data formats, leaving cross-level questions hard to address. We present DRIADA, an open-source Python framework that unifies neural signals and time-aligned behavior in a shared data model, so selectivity testing, dimensionality reduction, and network analysis operate within a unified workflow. We evaluate...

---

### 9. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00397v1)

**Summary:** Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...

---

### 10. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 11. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 12. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v2)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 13. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 14. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 15. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 16. Interpretable machine learning predicts Parkinson's disease severity using motion-corrected QSM MRI and multiband multiecho fMRI features

**Authors:** Aixa X. Andrade

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2607.02553v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02553v1)

**Summary:** Introduction: Objective neuroimaging biomarkers may improve Parkinson's disease motor assessment by capturing brain variation not directly observable from clinical examination. We used interpretable machine learning to predict current motor severity, measured by MDS-UPDRS Part III, from QSM and multiband multi-echo resting-state fMRI-derived ReHo features.   Methods: Regional QSM and ReHo features were extracted from 28 participants, including 24 individuals with Parkinson's disease and 4 contro...

---

### 17. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 18. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 19. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 20. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 21. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 22. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 23. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 24. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

### 25. Weight geometry governs functional memory in complex systems

**Authors:** Elkaïoum M. Moutuou, Habib Benali

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25826v1)

**Summary:** Complex systems, from gene regulatory networks to neural circuits and transportation infrastructures, exhibit rich functional behaviour that topology alone does not capture. Here we show that functional memory exhibits a universal organisational regularity: in every biological, ecological, social, and technological domain studied, real interaction strengths organise memory at greater hierarchical depth than random weight assignment on the same topology, across thirty-four networks spanning sever...

---

### 26. Meta-learning as a principle for human-like visual representations

**Authors:** Can Demircan, Marcel Binz, Alireza Modirshanechi, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.28399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28399v1)

**Summary:** The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few obse...

---

### 27. A pilot study examining transcranial photobiomodulation therapy intervention in college students with insomnia

**Authors:** Jiangshan He, Lianghua Zhang, Dan Liang, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24668v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24668v1)

**Summary:** College students commonly report insufficient sleep and poor sleep quality, with ~30% meeting insomnia criteria, posing significant threats to their physical growth, cognitive development, and overall well-being, as well as imposing a substantial economic burden on society [1]. The hyperarousal model of insomnia [2] emphasizes that hyperarousal across cognitive, emotional, and physiological domains mutually reinforces one another. Neuroimaging studies have further identified prefrontal hypoactiv...

---

### 28. EEG Interpretation Across Chant Listening: A Single-Subject Pilot Investigation Using Spectral and Functional Connectivity Analysis

**Authors:** Prerna Singh, Aishwarya Ghosh, Neelam Sinha, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24406v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24406v1)

**Summary:** This technical report presents an EEG-based investigation of neural activity across five auditory conditions: Resting State (RS), Shiv Tandav Stotra (STS), Mahasudarshan Mantra (MM), Aum Chant, and Tanpura Listening. EEG recordings acquired from a healthy 5-year-old participant were analyzed using spectral power estimation and functional connectivity measures based on the weighted Phase Lag Index (wPLI). Spectral analysis revealed condition-specific modulation of neural oscillatory activity, wit...

---

### 29. Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**Authors:** Xavier Vasques, Paul Barbaste, Olivier Oullier

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24394v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24394v1)

**Summary:** Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (fea...

---

### 30. Graph-based analysis of inflammatory profiles in New Onset Refractory Status Epilepticus (NORSE)

**Authors:** Linon Denis, Martin Guillemaud, Vincent Navarro, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24351v1)

**Summary:** Background and Objectives: Cryptogenic new-onset refractory status epilepticus (cNORSE) represents one of the most severe forms of status epilepticus, occurring in patients without prior neurological disease, and remaining of unknown aetiology despite extensive diagnostic evaluation. Emerging evidence supports a role for immune dysregulation in cNORSE; however, marked heterogeneity in inflammatory signatures has been reported, complicating the selection of targeted immunotherapies. Therefore, a ...

---

### 31. The Morality Game: An online multiplayer platform to standardize, expedite, and expand research on cooperation

**Authors:** Gregory N. Stanley, Alan Yang, Liam Tsimhoni, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24037v1)

**Summary:** This paper presents the Morality Game, a platform designed to standardize and accelerate research on cooperation and morality through game theory-based experiments. The Morality Game functions as a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process. It allows researchers to launch customized online multiplayer experiments with zero coding, using game trees to simulate moral dilemmas. The platform automates part...

---

### 32. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 33. The adaptive nature of confirmation bias

**Authors:** Dorje C. Brody, Karl J. Friston, Bernhard K. Meister, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23325v1)

**Summary:** In this paper, the phenomenon generally classified as confirmation bias is formulated on the space of square-root probabilities (or equivalently, using the structures of quantum probability). In this framework, observations are modelled by matrices, rather than random variables on a probability space. In the problem of binary hypothesis testing, an optimal evidence choice minimises the expected error probability. We show that the resulting optimal choice of evidence leads to a confirmation bias,...

---

### 34. Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg

**Authors:** Helio V. Cabral, Giacomo Valli, Roberto Zanotti, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23066v1)

**Summary:** Common synaptic input is considered a fundamental principle of motor neuron control and represents the dominant component of the neural drive transmitted from the motor neurons to muscle. Recent advances in High-Density surface Electromyography (HDsEMG) and motor unit (MU) decomposition algorithms have enabled the concurrent identification of increasingly large populations of MUs and substantially expanded the possibility of estimating common synaptic input from MU spike trains, making this appr...

---

### 35. SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings

**Authors:** Yisi S. Zhang, Daniel Y. Takahashi

**Published:** 2026-06-21

🔗 [Paper](http://arxiv.org/abs/2606.22695v2) | 📄 [PDF](https://arxiv.org/pdf/2606.22695v2)

**Summary:** Mapping the directed flow of information between brain regions -- their effective connectivity -- is central to understanding brain function, yet large-scale recordings sample only a fraction of the brain at a time: sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established directed-connectivity methods (Granger causality, dynamic causal modeling, partial directed coherence, PDC) require all regions to be recorded ...

---

### 36. DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**Authors:** Jayadratha Gayen, Bradly Alicea

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21940v1)

**Summary:** Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed...

---

### 37. Dynamic Computerized Tumbling-E Testing for Temporal Reliability of Human Sequential Perceptual Decisions

**Authors:** Avneek Sandhu, Bin Hu

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21818v1)

**Summary:** OBJECTIVES: Visual acuity and tumbling-E tasks are often treated as static threshold measures, yet sequential perceptual decisions unfold over time. A computerized tumbling-E task preserves response latency, timeouts, and stimulus-size adaptation, creating a temporal reliability dataset rather than only a chart-line score. This matters for human-AI comparison because the Temporal Hallucination Index (THI) shows how static accuracy can obscure delays, drift, persistence, and unstable convergence....

---

### 38. Mostly-monocular responses and other visual functions in a multiscale network model of Macaque V1

**Authors:** Zhuo-Cheng Xiao, Kevin K. Lin, Lai-Sang Young

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21785v2) | 📄 [PDF](https://arxiv.org/pdf/2606.21785v2)

**Summary:** Visual signals from the two eyes merge gradually as they pass through the primary visual cortex (V1). Here we use a computational model of Macaque V1 to study the first stage of this integration along the magnocellular pathway, in layer 4C$α$, aiming to infer neuroanatomical origins of binocular response. It is known that neurons in layer 4C$α$ are predominantly monocular, though some do exhibit varying degrees of binocularity. We find (1) the emergence of narrow binocular strips along borders o...

---

### 39. Delay coordinates synchronization and induces abrupt transition in excitable networks

**Authors:** Bruno R. R. Boaretto, Kalel L. Rossi, Lyle E. Muller, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21703v1)

**Summary:** Neuronal communication is inherently time-delayed, due to the finite speed of signal propagation. Although often considered challenging or disruptive, such time delays can also endow neural circuits with useful capabilities. Here, we show that delays in excitatory connections between excitable neurons coordinate their synchronization patterns by creating self-sustained oscillations that may be out-of-phase or in-phase. The emergence of these oscillations leads to an abrupt, explosive, transition...

---

### 40. Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks

**Authors:** Stephen Coombes, Rüdiger Thul, Stefan Ruschel, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21508v1)

**Summary:** We develop a theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model as an analytically tractable event-based description of neural dynamics. For networks with fixed delays, we derive self-consistency conditions for phase-locked states and an associated linear stability theory formulated directly in terms of spike-time perturbations. The framework is illustrated for a delayed autapse, a reciprocally coupled two-cell network, and spatially structured rings wit...

---

### 41. Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity

**Authors:** Ch. Meessen

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21432v1)

**Summary:** We construct a minimal but biologically plausible spiking neuron model operating in discrete time, combining multiplicative spike-timing-dependent plasticity (WSTDP), divisive normalization of synaptic integration, homeostatic threshold adaptation, and a one-step refractory period. We show that this normalization admits a biologically plausible dendritic implementation in which each binary junction operates using only locally available information.   Assembling excitatory-inhibitory pairs of suc...

---

### 42. Relational Gaze Transitions During Encoding Predict Episodic Recall of Naturalistic Scenes

**Authors:** Hugo Rydel, Alex Kafkas

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20844v1)

**Summary:** Remembering a visual scene requires organizing distinct details into a cohesive event. This study investigates whether relation-guided gaze transitions provide a behavioural marker of this cognitive organization during episodic encoding and retrieval. By applying scene graph annotations to eye-tracking data, we measured whether gaze moved between objects that were meaningfully related within complex scenes. This approach allowed us to quantify relational scanning within naturalistic environments...

---

### 43. Synchronization modes in bipartite oscillator networks

**Authors:** Pau Pomés, Bastian Pietras, Ernest Montbrió

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20345v2) | 📄 [PDF](https://arxiv.org/pdf/2606.20345v2)

**Summary:** Collective oscillations in neuronal systems often arise from interactions between excitatory and inhibitory populations rather than from recurrent coupling within a single ensemble. Motivated by the coexistence of strongly and partially synchronized regimes in such systems, we study the Kuramoto Sakaguchi model on a bipartite network. Despite its minimal structure, the model exhibits rich collective dynamics, including both continuous and discontinuous transitions from full synchrony to partial ...

---

### 44. Quadratic Forms for Measuring Geometric Trees in 3-dimensional Space

**Authors:** Yossi Bokor Bleile, Emanuele Cortinovis, Herbert Edelsbrunner, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20096v1)

**Summary:** Tree-like structures appear in many areas of science, and their shapes can help understand the underlying processes they drive or that give rise to them.   By thinking of these structures as geometric graphs in $\mathbb{R}^3$, we gain access to tools from computational geometry and topology to study them.   In this paper, we adopt the theory of quadratic forms to measure the directional spread of geometric graphs, and we introduce the hexplot model -- equipped with a metric derived from the Fish...

---

### 45. Robust probabilistic measurement of structural-functional module consistency in infant brain development

**Authors:** Lingbin Bian, Feihong Liu, Qian Wang, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.19739v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19739v1)

**Summary:** Brain network is commonly divided into modules for analyzing their functionally segregated roles for group-level analysis in neuroimaging studies. Here, we introduce stochastic modules within brain networks for a robust probabilistic measurement of structural-functional module consistency (SFMC) in a group of subjects. Specifically, a stochastic module can be regarded as the chance of a brain region across subjects potentially being assigned to a group-level sub-network, characterized as an assi...

---

### 46. Retrieval-Based Brain Decoding by Alignment, not Complexity

**Authors:** Matteo Ciferri, Matteo Ferrante, Nicola Toschi

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.19081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19081v1)

**Summary:** A prominent theory in cognitive science suggests that concepts in the brain are organized as high-dimensional vectors, with semantic meaning captured by directions and relative angles in this space. Brain decoding is the effort of reconstructing or retrieving stimuli (or their representations) from neural activity and involves finding a function that approximates how the brain represents concepts. This motivates the investigation of contrastive objectives as biologically plausible candidates to ...

---

### 47. Dissecting emerging slow rhythms in delay-coupled neural oscillators

**Authors:** Xinxin Qie, Matteo Martin, Shenquan Liu, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.20733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20733v1)

**Summary:** Synaptic transmission delays are ubiquitous in neural circuits and can alter the dynamical repertoire of coupled oscillators quantitatively and qualitatively. Here, we demonstrate that delayed coupling in inhibitory networks introduces an effective slow-fast structure in the phase-difference dynamics, generating low-frequency components that are not due to intrinsic cellular properties, and we show that this behavior is not specific to a particular model structure. The origin of this generic phe...

---

### 48. Can neurons speak? Semantic narration of vision at single-cell resolution

**Authors:** Arnau Marin-Llobet, Richard Hakim, Sara Matias, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.18667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.18667v1)

**Summary:** Identifying what individual neurons encode in higher-order visual cortex is an open problem. Responses resist intuitive parameterization, and the deep-network embeddings used in their place are black boxes. Here, we introduce NEURRATOR, a framework that decodes spiking activity into free-form natural-language narration of the viewed scene at single-neuron resolution. A learned encoder maps spike trains from arbitrary subsets of simultaneously-recorded neurons into the patch-embedding space of a ...

---

### 49. A frozen rate operator from the complete larval connectome: degree and weight govern the gross response, exact wiring governs input routing and mushroom-body modes

**Authors:** Stavros Therianos

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17745v2) | 📄 [PDF](https://arxiv.org/pdf/2606.17745v2)

**Summary:** Connectome-constrained models now reproduce neural activity in several systems, yet each inherits a circuit's degree and weight statistics along with its exact wiring, leaving open which dynamical properties the wiring fixes beyond those statistics. We separate the two by running the complete larval Drosophila connectome, 2'825 neurons in its strongly connected core, as a frozen leaky-tanh rate operator with no single-neuron parameter fitted, and comparing it against a degree-and-weight-matched ...

---

### 50. BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17742v1)

**Summary:** Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than...

---

## stat.ML

**50 papers**

### 1. What Does a Discrete Diffusion Model Learn?

**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05381v1)

**Summary:** What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the da...

---

### 2. Fitted Occupancy-Ratio Evaluation without Bellman Completeness

**Authors:** Lars van der Laan, Nathan Kallus

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05375v1)

**Summary:** Occupancy ratios correct distribution shift in offline reinforcement learning and are central to off-policy evaluation. Existing primal-dual and minimax methods typically estimate these ratios by enforcing occupancy-balance moments over a critic class. We propose fitted occupancy-ratio evaluation (FORE), a fitted fixed-point method that characterizes the discounted occupancy ratio through an adjoint Bellman recursion. At each iteration, FORE solves a single-level density-ratio objective on one-s...

---

### 3. TREK: Distill to Explore, Reinforce to Refine

**Authors:** Yuanda Xu, Zhengze Zhou, Kayhan Behdin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05339v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05339v1)

**Summary:** Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure that uses distillation not for imitation but for exploration support expansion. A key advantage of TREK is its generality: because it only consumes verified output trajectories, it ca...

---

### 4. Locally Private Online Quantile Regression: Estimation and Inference

**Authors:** Yi Liu, Qirui Hu

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05312v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05312v1)

**Summary:** We study estimation and inference for online quantile regression under a one-report user-level $\eps$-locally differentially private ($\eps$-LDP) protocol. The main difficulty is that the standard quantile-regression estimating-equation contribution couples covariates with a residual comparison, so a server that receives only privatized reports cannot form the usual online update. We address this by developing a finite-alphabet channel in which each user computes the contribution locally, applie...

---

### 5. Emputation: Identification-Guided Neural Imputation Framework

**Authors:** Yanjiao Yang, Yikun Zhang, Xinwei Shen, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05279v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05279v1)

**Summary:** We propose Emputation, a deep generative framework for learning imputation models. Emputation targets the extrapolation distribution of missing variables given observed variables, and training is guided by specific missingness assumptions that guarantee identification of the target distribution. The training objective, called the emputation risk, is an energy-score-based risk in which the identification assumption determines how observed entries are masked and which observations contribute to tr...

---

### 6. msPCA: An R Package for Sparse PCA with Multiple Components

**Authors:** Ryan Cory-Wright, Jean Pauphilet

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05229v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05229v1)

**Summary:** We present msPCA: an open-source R package for sparse principal component analysis with multiple components. It implements an alternating maximization algorithm to generate a set of sparse loading vectors that collectively explain a large fraction of the variance in a dataset, while remaining non-redundant. The algorithm supports two definitions of non-redundancy: either orthogonality of the loading vectors or zero pairwise correlation between principal components (PCs). In the reported benchmar...

---

### 7. The Exact Worst-Case Tail Probability under Bounded Kurtosis

**Authors:** Xiaoyu Li, Andi Han, Jiaojiao Jiang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05226v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05226v1)

**Summary:** We determine exactly what a kurtosis bound buys for one-sided tail control. For the class $\mathcal{C}(κ)$ of real random variables with mean $0$, variance $1$, and fourth moment at most $κ$, the skewness left free, we compute the worst-case tail probability $V_1(t,κ)=\sup_{X\in\mathcal{C}(κ)}\mathbb{P}(X\geq t)$ for every threshold $t>0$ and every $κ\geq 1$. The answer is a four-regime map: a Cantelli tongue $b(κ)\le t\le c(κ)$ on which the two-moment bound $1/(1+t^2)$ remains tight and the kur...

---

### 8. Geometric Causal Models

**Authors:** Eli N. Weinstein, David M. Blei

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05153v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05153v1)

**Summary:** Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...

---

### 9. Functional Bilevel Optimization for Predictive Fairness

**Authors:** Ieva Petrulionyte, Julien Mairal, Michael Arbel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05098v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05098v1)

**Summary:** When sensitive attributes are continuous and high-dimensional $-$ demographic score vectors, posteriors over attributes, age or income profiles $-$ enforcing full statistical independence is often too restrictive, and existing relaxations rely on indirect dependence penalties or adversarial schemes that do not directly target the fairness-accuracy trade-off. We instead consider mean demographic parity through DPVar, the variance of the conditional-mean prediction given the sensitive attribute, a...

---

### 10. Geometry-Aware Bayesian Quantification via Compositional Data Analysis

**Authors:** Alejandro Moreo, Pablo González, Juan José del Coz

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04977v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04977v1)

**Summary:** Accurately estimating the unknown target label distribution is the critical first step for adapting to label shift. This task, widely known as quantification or class prevalence estimation, has recently seen significant advances through continuous KDE-based methods which model the density of multiclass classifier posteriors. Posterior vectors might be regarded as compositional data, since they lie on the probability simplex. However, existing KDE-based quantifiers typically rely on Euclidean Gau...

---

### 11. Identification and Bounding of Central Moments of Causal Effects Using Marginal Moments Information

**Authors:** Naoya Hashimoto, Yuta Kawakami, Jin Tian

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04957v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04957v1)

**Summary:** Evaluating the causal effect of a treatment on an outcome is a central objective in causal inference. While the average causal effect summarizes the mean impact of treatment, the central moments of the individual causal effect (ICE) characterize the shape of the ICE distribution, thereby revealing the extent and structure of treatment effect heterogeneity across individuals. This paper investigates the identification and bounding of the central moments of the ICE using only the marginal central ...

---

### 12. On the Complexity of Entrywise Power Matrix Factorization

**Authors:** Nicolas Gillis, Subhayan Saha, Stefano Sicilia, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04875v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04875v1)

**Summary:** Given a nonnegative matrix $X$, a factorization rank $r$ and a real parameter $p$, entrywise power matrix factorization (EPMF) looks for a low-rank matrix $X_r$ such that $X = |X_r|^{\circ p}$ (exact case) or $X \approx |X_r|^{\circ p}$ (approximate case), where $(\cdot)^{\circ p}$ denotes the component-wise exponent. EPMF includes the modulus model ($p=1$) and component-wise square factorization ($p=2$) as special cases, the latter being closely related to the square root rank. We analyze the c...

---

### 13. Active Learning on Adversarially Corrupted Graphs

**Authors:** Marco Bressan, Nicolò Cesa-Bianchi, Tommaso d`Orsi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04869v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04869v1)

**Summary:** Motivated by real-world scenarios where malicious entities tamper with existing networks, we define a model where an adversary seeks to hide a set of \emph{corrupted vertices} inside a graph $G^*$. To this end, the adversary can add edges between the corrupted vertices, as well as edges between the corrupted vertices and $G^*$, and its power is then measured by the size of the \emph{neighborhood} of the corrupted vertices in $G^*$. Our goal is to design an active learning algorithm that efficien...

---

### 14. Probably Correct Optimal Stable Matching under Two-Sided Uncertainty

**Authors:** Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04824v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04824v1)

**Summary:** We study a sequential learning problem for stable matchings in two-sided markets where preferences on both sides are initially unknown. We focus on a centralized setting where an algorithm matches agents at each time step and receives noisy rewards that reflect the preferences of the matched agents, following a semi-bandit feedback structure. We adopt a pure exploration perspective, aiming to efficiently identify the optimal stable matching with high probability. Our work extends prior results b...

---

### 15. Context-Constrained Transfer Learning for Tabular Foundation Models via Data Distillation

**Authors:** Yijun Lin, Sai Li

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04809v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04809v1)

**Summary:** Tabular Foundation Models (TFMs) have demonstrated strong empirical performance as black-box inference engines through in-context learning. However, their use in transfer learning is limited by two obstacles: strict context-size constraints and sensitivity to distribution shifts between source and target tasks. Directly pooling heterogeneous source data can therefore lead to negative transfer. To address these challenges, we propose Context-Constrained Transfer Learning via ANchoring and DIstill...

---

### 16. Non-Asymptotic Error Bounds for SMC with Biased Proposals: Application to Conditional Diffusion Sampling

**Authors:** Stanislas Strasman, Gabriel Victorino Cardoso, Sylvain Le Corff, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04780v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04780v1)

**Summary:** Sequential Monte Carlo (SMC) methods are a natural tool for post-hoc conditioning of pretrained generative models, but in many applications the mutation kernels used by the particle system are biased approximations of an ideal Feynman--Kac flow. This paper develops a non-asymptotic error analysis for such SMC samplers. Under forward-smoothing forgetting conditions, we decompose the total error into a kernel bias, measuring the effect of replacing the ideal transition kernels by approximate ones,...

---

### 17. Non-asymptotic Convergence of Stochastic Gradient Descent in Score-based Generative Models

**Authors:** Stanislas Strasman, Sobihan Surendran, Sylvain Le Corff

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04775v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04775v1)

**Summary:** Score-based Generative Models (SGMs) have achieved impressive performance in data generation across a wide range of applications. While the statistical properties of their sampling procedures are increasingly well understood, the optimization dynamics underlying their training remain less explored. SGMs are typically trained by minimizing a weighted denoising scorematching objective, yet optimization guarantees with stochastic gradients remain limited. In this work, we study Stochastic Gradient ...

---

### 18. Multi-Turn On-Policy Distillation with Prefix Replay

**Authors:** Baohao Liao, Hanze Dong, Christof Monz, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04763v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04763v1)

**Summary:** We study on-policy distillation (OPD) for agentic tasks, where an LLM agent interacts with an environment over multiple turns and a student imitates a teacher over these multi-turn interaction histories. Fully online OPD is costly because each update requires fresh student rollouts through the environment and teacher queries at visited histories. We propose Replayed-Prefix On-Policy Distillation (ReOPD), an off-environment alternative that reuses pre-collected teacher trajectories as replayed pr...

---

### 19. Stabilized Higher-Order Influence Functions: Statistical Theory of a Class of Bilinear Forms

**Authors:** Na Liu, Chang Li, Yujia Gu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04743v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04743v1)

**Summary:** Higher-order influence functions, introduced in a series of articles (Robins et al., 2008, 2009a; van der Vaart, 2014; Robins et al., 2016, 2023; Liu et al., 2017), are a unified framework for constructing rate-optimal point estimates of a class of statistical functionals, under various complexity-reducing assumptions on the posited statistical model that generates the observed data. Although higher-order (influence functions) estimators are theoretically appealing, they have very limited practi...

---

### 20. Wasserstein Residuals: Learning Gradient Flows from Population Dynamics

**Authors:** Markus Heinonen, Yair Shenfeld, Ricardo Baptista, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04738v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04738v1)

**Summary:** Reconstructing population dynamics is a central problem in the physical and data sciences. Often, the dynamics are modeled as a Wasserstein gradient flow (WGF): a curve of distributions driven by an energy functional. Though there are multiple mathematical characterizations of a WGF, the dominant algorithmic approach relies on the Jordan--Kinderlehrer--Otto (JKO) scheme. JKO-based methods are inflexible to time discretisation and require solving costly optimal transport problems. We take a resid...

---

### 21. Decomposition for Bayesian Networks: Local and Parallel Inference

**Authors:** Pei Heng, Xinyi Hu, Yi Sun

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04650v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04650v1)

**Summary:** Probabilistic inference in high-dimensional Bayesian networks is difficult because exact manipulation of the joint distribution scales exponentially with network size. We propose a decomposition framework based on directed convex subgraphs and introduce a minimal d-decomposition tree. Together, they provide a principled alternative to classical junction-tree constructions. The proposed framework represents the joint distribution by lower-dimensional sub-models that can be learned and stored sepa...

---

### 22. Integrating Neural Encoders in Bayesian Generalized Linear Mixed Models for Multimodal Data

**Authors:** Yuankang Zhao, Youngsoo Baek, Felipe A. Medeiros, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04647v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04647v1)

**Summary:** Scalable Bayesian inference for generalized linear mixed models (GLMMs) provides uncertainty-aware analysis of correlated longitudinal data, but existing scalable approaches largely assume low-dimensional tabular predictors and do not directly accommodate high-dimensional modalities such as images and text. We address this limitation by learning one or more modality-specific neural encoders jointly with a GLMM objective, then performing variance-corrected stochasticgradient MCMC for the GLMM par...

---

### 23. Minimum Block Width for Universal Approximation by Residual Neural Networks with Inner Width One

**Authors:** Qi Zhou, Xuan Zhou, Xiao-Song Yang

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04597v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04597v1)

**Summary:** In this paper, we study the universal approximation property of residual neural networks, and obtain some new results. For input and output dimensions $d_x$ and $d_y$, and LeakyReLU, ReLU, ReLU-like activation functions, the upper and lower bounds of the block width are established. To achieve $L^p$ approximation $(1\leq p <+\infty)$ on any compact domain, we show that the exact minimum block width is $\max\{d_x,d_y\}$ when the inner width is 1. Furthermore, we show that residual neural networks...

---

### 24. Score Distributions, Not Cells: Evaluating Single-Cell Perturbations Under Class Overlap

**Authors:** Youssef Marrakchi, Davide D'Ascenzo, Sebastiano Cultrera di Montesano

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04595v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04595v1)

**Summary:** Most classification problems assume the classes are roughly separable, so that an individual sample can usually be assigned to one class. Single-cell perturbation data violates this assumption: two perturbations can produce different populations of cells while overlapping so much that an individual cell could belong to either. Per-cell accuracy then measures this overlap rather than model quality. We see this on Tahoe-100M and the Virtual Cell Challenge, where a linear classifier, an MLP, and a ...

---

### 25. ManifoldFlow: SPD-Relaxed Stiefel Layers with Learnable Singular Spectrum

**Authors:** Haiwen Yi, Xinyuan Song

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04535v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04535v1)

**Summary:** Orthogonal and Stiefel layers give neural weights exact spectral control, but they also impose a strong modeling constraint: all represented singular values are fixed at one. Many settings that benefit from an orthonormal basis still need direction-dependent attenuation or amplification. We introduce ManifoldFlow, a minimal relaxation of a fixed-spectrum Stiefel layer that keeps the basis on the Stiefel manifold while learning a bounded positive spectrum through W = Q S^{1/2}, with Q^T Q = I and...

---

### 26. Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data

**Authors:** Stephen Asiedu, David Watson

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04527v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04527v1)

**Summary:** Biological systems exhibit a hierarchical structure, characterised by directed flow from upstream regulators to downstream effects. Although this ordering provides a natural scaffold for causal inference, most causal discovery and GRN methods either ignore the tiered organisation or condition on all upstream variables, which becomes infeasible for high-dimensional omics data. We present ASCEND (Ancestral Scalable Causal discovEry via iNherited Descent), a constraint-based framework that leverage...

---

### 27. Knowledge-Informed Local Causal Discovery of Optimal Adjustment Sets

**Authors:** Seong Woo Ahn, Alessandro Leite, José Lucas De Melo Costa, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04447v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04447v1)

**Summary:** Local causal discovery is a scalable alternative to global structure learning. However, it can struggle to identify valid adjustment sets in data-scarce settings because of finite-sample uncertainty, incomplete local neighborhoods, and unresolved Markov equivalence. Although many application domains provide structured background knowledge, its integration into local causal discovery remains limited. We propose b-LOAD, a knowledge-informed extension of the LOAD algorithm for local discovery of op...

---

### 28. Tightening the Score Matching Gap for Diffusion Models

**Authors:** Benjamin Dupuis, Tyler Farghly, Maxime Haddouche, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04442v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04442v1)

**Summary:** Diffusion models (DMs) are a state-of-the-art generative method to approximately sample from an unknown distribution. Their training and evaluation primarily rely on an Evidence Lower Bound (ELBO), which relates the Kullback-Leibler (KL) divergence of model samples to the score matching loss along the path, which serves as a tractable surrogate. The difference between sample quality and the score matching loss produced by this bound leads to the \emph{score matching gap}, which is known to be ti...

---

### 29. On Pairwise Quantile Regression -- Statistical Guarantees and Applications

**Authors:** Romain Thérézien, Stephan Clémençon, Fantin Girard, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04431v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04431v1)

**Summary:** Quantile regression provides a powerful tool for summarizing the conditional distribution of a real valued random variable (r.v.) of interest $Y$ as a function of covariates $Z$ in cases where it shows a large dispersion with high probability, going beyond the situation where standard least square regression is informative/predictive. This article aims to extend this methodology to the pairwise case, when the variable to be explained takes the form of a similarity function between two independen...

---

### 30. Optimal Mixture-of-Experts Model Averaging for Conditional Generative Models

**Authors:** Shijin Gong, Baihua He, Xinyu Zhang

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04360v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04360v1)

**Summary:** Conditional generative models have emerged as powerful tools for sampling from target conditional distributions, driving substantial advances across a wide range of scientific and applied domains. As these models proliferate, practitioners often face multiple plausible generators whose performance can vary with the task, data, or input condition. We propose an optimal model averaging framework for conditional generative models, allowing candidate generators to be combined even when they are acce...

---

### 31. Fixed-Confidence Best-Arm Identification for Causal Mediation Analysis

**Authors:** Harsh Shrivastava, Yuta Kawakami, Junpei Komiyama, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04315v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04315v1)

**Summary:** This paper studies the problem of identifying the treatment that maximizes the expected natural direct potential outcome (NDPO), which captures the potential outcome of an intervention while excluding the pathway transmitted through a mediator that researchers may wish to remove from evaluation. We first establish population-level identification of the expected NDPO in a causal bandit setting using observable interventional distributions. We then develop a fixed-confidence best-arm identificatio...

---

### 32. CausalGame: Benchmarking Causal Thinking of LLM Agents in Games

**Authors:** Zhenhao Chen, Yongqiang Chen, Chenxi Liu, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04293v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04293v1)

**Summary:** Building AI Scientist agents with Large Language Models (LLMs) has recently attracted growing attention. Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capability of causal thinking, i.e., distinguishing causation from correlation and recognizing hidden biases, is essential to LLM agents. Although a number of benchmarks exist for AI Scientists, none explicitly incorporate challenges from selection bias, measurement error, and hidden conf...

---

### 33. Deep Learning for Dynamic Programming with Recursive Utility

**Authors:** Xianhua Peng, Wu Guo

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04278v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04278v1)

**Summary:** We propose the first deep learning algorithm, the Certainty Equivalent Learning (CEL) algorithm, for solving high-dimensional discrete-time dynamic programming problems with recursive utility. Dynamic programming with recursive utility is numerically challenging because the recursive utility does not have an explicit representation and the Bellman equation contains a certainty equivalent that is difficult to evaluate. The CEL algorithm learns this certainty-equivalent value directly with neural ...

---

### 34. Robust Bayes-Assisted Conformal Prediction

**Authors:** Kianoosh Ashouritaklimi, Stefano Cortinovis, François Caron

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04236v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04236v1)

**Summary:** Bayes-assisted conformal prediction combines the strengths of Bayesian modelling with exact, distribution-free frequentist coverage guarantees. Although conformal validity is preserved even when the Bayesian working model (BWM) is misspecified, the size of the resulting prediction sets can degrade substantially when the prior is poorly aligned with the observed data. We address this limitation by introducing RoBAS (Robust Bayes-Assisted Shrinkage): a Bayes-assisted framework for constructing rob...

---

### 35. A Unified Framework for In-Context Learning with Causal and Masked Language Models

**Authors:** Chenrui Liu, Chuanlong Xie, Falong Tan, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04081v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04081v1)

**Summary:** In-context learning (ICL) has emerged as a central capability of pretrained language models, yet its theoretical analysis has focused primarily on causal language models trained by left-to-right autoregressive prediction, such as GPT-style models. Masked language models instead recover masked tokens from bidirectional context, and their role in ICL remains less understood. We develop a statistical learning framework that represents the context examples by their empirical measure and models predi...

---

### 36. Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability

**Authors:** Christopher Nassif, Josh F. Cooper

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04061v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04061v1)

**Summary:** Distinguishing Large Language Model (LLM) generated text from human writing is a critical and difficult challenge. While LLMs are trained to write like humans, we hypothesize that this training leaves an indelible mark. LLMs develop a particularly strong aversion to token repetition very early in training. This bias persists as a ''Vestigial Heuristic'' (a developmental artifact) that is activated in LLM-generated text, separating LLM from human writing. To probe this phenomenon, we introduce Te...

---

### 37. SiamJEPA: On the Role of Siamese Student Encoders in JEPA

**Authors:** Makoto Yamada

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.04044v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04044v1)

**Summary:** Recently, Joint Embedding Predictive Architectures (JEPAs) have attracted significant attention in the computer vision and machine learning communities as a promising framework for self-supervised representation learning. Unlike masked autoencoders that reconstruct pixels, JEPA models learn representations by predicting latent embeddings of masked regions. Existing JEPA-based methods, such as I-JEPA and V-JEPA, typically employ a single encoder in the student network. In contrast, using Siamese ...

---

### 38. Significance-First Splitting: Aligning Treatment Heterogeneity Detection with Honest Estimation

**Authors:** Pantelis Z. Hadjipantelis, Josephine Chiang, Karthik Nagesh

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03999v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03999v1)

**Summary:** Estimating heterogeneous treatment effects (CATE) requires simultaneously detecting effect modification and quantifying estimation uncertainty. Existing tree-based methods make an uneasy trade-off: significance-based approaches (Radcliffe and Surry 2011)  identify subgroup interactions directly but lack valid inference; honest causal trees (Athey and Imbens 2016) deliver nominal confidence interval coverage but use outcome-agnostic splitting criteria that sacrifice interaction sensitivity. We in...

---

### 39. A Gradient Flow Perspective on Minimum MMD Estimation

**Authors:** Sophia Seulkee Kang, Louis Sharrock, Xiaoyuan Cheng, et al.

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03871v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03871v1)

**Summary:** Minimum maximum mean discrepancy (MMD) estimation has emerged as a robust and likelihood-free alternative to maximum likelihood estimation for parameter estimation. Yet, despite its practical success, the associated optimization problem remains poorly understood, with theoretical guarantees for existing algorithms hinging on convexity assumptions that rarely hold in practice. We address this gap by proposing a preconditioned gradient descent (PGD) scheme, establishing its asymptotic \emph{global...

---

### 40. Targeted Highly Adaptive Lasso Minimum Loss Estimation of Target Functions

**Authors:** Vanessa Rodriguez, Karla Diaz-Ordaz, Brieuc Lehmann, et al.

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03824v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03824v1)

**Summary:** We propose a Targeted Highly Adaptive Lasso for estimation of non-pathwise differentiable functional parameters such as the dose-response curve (DRC) for continuous exposure. We assume the target function lies in the $k$-th order smoothness class used to define the $k$-th order Highly Adaptive Lasso (HAL), which can be well approximated by linear spans of $k$-th order spline basis functions. We construct a projection of the true target function onto a large finite dimensional working model spann...

---

### 41. Stable Global Weighting of Flow Mixtures using Simplex Exponential Moving Average

**Authors:** Benjamin Wiriyapong, Oktay Karakus, Can Eyupoglu, et al.

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03809v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03809v1)

**Summary:** Normalising flows provide a powerful variational family for approximate inference, yet individual architectures often fail to generalise across heterogeneous posterior geometries. We revisit mixture-based flow formulations and introduce \emph{AMF\mbox{-}VI\mbox{-}sEMA}, a two-stage framework featuring a \emph{stable global weighting} mechanism based on a \emph{Simplex Exponential Moving Average} (sEMA) update. In Stage~1, a heterogeneous set of experts (\textsc{RealNVP}, \textsc{MAF}, \textsc{RB...

---

### 42. A Structural Interpretation of GELU and Threshold-Transmission Activations via the First-Order Loss Function

**Authors:** Roberto Rossi

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03664v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03664v1)

**Summary:** The Gaussian Error Linear Unit is usually motivated as the expected output of an input-dependent stochastic Bernoulli gate. This work gives a complementary interpretation based on the Gaussian complementary first-order loss function: GELU is the signal-transmission term of the expected surplus of a hard linear gate with a Gaussian random threshold. This view separates loss accounting from forward signal transmission and generalises to a threshold-transmission family that includes ReLU, GELU, SiL...

---

### 43. Sequential Correlations Change In-Context Learning: Effective Context Length and Architectural Mismatch

**Authors:** Mary Letey, Yue M. Lu, Cengiz Pehlevan, et al.

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03660v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03660v1)

**Summary:** Modern sequence models have a striking capacity for in-context learning (ICL); they can perform new tasks based only on examples given in the prompt. Understanding how this ability emerges requires theory that captures important properties of natural data. Linear regression has served as a useful sandbox for ICL theory, but existing work has largely focused on prompts with independent examples. In this work, we extend this setting to sequentially correlated data, a basic feature of real sequence...

---

### 44. Missing Data Imputation under Manifold Hypothesis

**Authors:** Zelong Bi, Amuchechukwu Ibenegbu, Sarat Moka

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03641v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03641v1)

**Summary:** The manifold hypothesis posits that high-dimensional data are concentrated near a low-dimensional embedded manifold. Recent advances in mixture variational autoencoders (VAEs) provide a powerful tool for extracting such underlying structure in a faithful manner. The resulting geometric structure naturally introduces local and global relationships among variables, thereby providing a systematic way of imputing missing data. We propose a model-based imputation method that enables sampling from \( ...

---

### 45. Reflected Schrödinger Bridge Matching

**Authors:** Marcus Häggbom, Viktor Nilsson, Pierre Nyquist, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03626v1)

**Summary:** Recent advances in generative modeling have enabled the efficient computation of Schrödinger bridges (SB) in high-dimensional settings by leveraging partially simulation-free training methods inspired by flow matching. However, these have not covered SBs with reflecting dynamics, a useful model choice with built-in guarantees that generated samples stay in the data domain. Existing alternatives for reflected SBs instead rely on more complex training based on forward--backward SDE theory, requiri...

---

### 46. Empirical Bayes for correlated Gaussian sequence model

**Authors:** Qiyang Han, Cun-Hui Zhang

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03596v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03596v1)

**Summary:** Empirical Bayes methods are among the most widely used statistical methods for large-scale inference. A central paradigm is the NPMLE, whose theoretical guarantees are by now well understood for the independent Gaussian sequence model.   In this paper, we study empirical Bayes estimation from dependent observations in the Gaussian sequence model. We show that the maximum Composite Marginal Likelihood (CML) estimator, which ignores all correlations in the likelihood, converges in weighted Helling...

---

### 47. Tightening Control in Neyman--Pearson Linear Classification

**Authors:** Yijian Huang

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03590v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03590v1)

**Summary:** Neyman--Pearson classification prioritizes one class by constraining its accuracy above a prespecified level, and then takes the accuracy of the other class as the utility objective. This paradigm is well suited for disease screening and diagnosis, among other applications. Statistical learning under this framework is complicated since classifier performance determines its acceptability. Furthermore, no learned classifier that is consistent for the oracle classifier can guarantee satisfaction of...

---

### 48. On the Convergence of Adam, Revisited

**Authors:** Steven Heilman, Sampad Mohanty

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03519v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03519v1)

**Summary:** We show that projected Adam for online optimization with arbitrary moment decay parameters $β_1,β_2\in[0,1)$ can have average regret bounded away from zero. A similar result of Reddi-Kale-Kumar from 2018 required $β_1<\sqrt{β_2}$. Similar to their result, we use a three-periodic sequence of linear functions on $[-1,1]$ with slopes $c,-1,-1$, though we use $c$ slightly larger than $2$. This nonzero average regret result extends to Adam variants such as AdamW, RMSProp, NAdam, Adan, AdaMax, Muon, a...

---

### 49. A Hierarchy of Policy Learning Problems

**Authors:** Hamsa Bastani, Osbert Bastani, Shihan Chen

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03385v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03385v1)

**Summary:** Policy learning has received substantial attention with the goal of learning policies from observational data for decision-making. A majority of work in this space has focused on developing algorithms for computing policies that minimize regret compared to the optimal policy. However, in many practical settings, there is insufficient data to obtain low regret. As a result, recent work has shifted attention to alternative objectives, most notably, studying whether it is possible to learn an impro...

---

### 50. Minimax Estimation of Kernel Stein Discrepancy: Trace versus Hilbert-Schmidt Scales

**Authors:** Davit Gogolashvili

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03367v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03367v1)

**Summary:** Kernel Stein Discrepancy (KSD) compares a sample to a fixed target distribution known only through its score, and is widely used for goodness-of-fit testing, sample quality assessment, and approximate inference. We study the estimation of $\operatorname{KSD}(P_0,P)$ from $n$ independent observations and identify the sharp spectral constant governing the minimax risk: it is the Hilbert-Schmidt norm of the Stein covariance operator $C_\star$, giving the minimax scale $\sqrt{\|C_\star\|_{\mathrm{HS...

---

