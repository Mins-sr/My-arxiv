# arXiv Daily Digest - 2026-10-07

Total papers: 350

---

## cs.AI

**50 papers**

### 1. 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction

**Authors:** Shiqi Li, Sean Cho, Yijie Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08782v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08782v1)

**Summary:** Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-...

---

### 2. IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas

**Authors:** Ziyu Chen, Yilun Zhao, Jiashuo Sun, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08781v1)

**Summary:** Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-grounded ideation remains challenging, as existing approaches based on prompting or feedback lack structured supervision for how papers should be synthesized. We introduce IdeaAnchor, a paradigm for training LLMs to perform research ideation using structured specifications as privileged signals. Eac...

---

### 3. DepthWorld: 3D World Model for Robot Manipulation

**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08780v1)

**Summary:** World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absor...

---

### 4. Sherpa: Teaching LLMs to Teach Adaptively

**Authors:** Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08778v1)

**Summary:** Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address t...

---

### 5. Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?

**Authors:** Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08775v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08775v1)

**Summary:** Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed ti...

---

### 6. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08773v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08773v1)

**Summary:** Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a t...

---

### 7. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning

**Authors:** Zewei Zhou, Rachel Luo, Yulong Cao, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08761v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08761v1)

**Summary:** Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales ve...

---

### 8. WorldSonus: Bringing Sound to Worlds

**Authors:** Pengjun Fang, Jingyi Fa, Kam Man Wu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08760v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08760v1)

**Summary:** Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To address these demands, we introduce WorldSonus, an interactive video-to-audio framewo...

---

### 9. Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation

**Authors:** Wenwen Si, Honghao Wei

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08743v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08743v1)

**Summary:** Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which adapts the retained action set using critic scores and an online threshold. The threshold is updated from binary feedback indicating whether the set contains an action in a proxy target. We prove a deterministic bound on the observed proxy miss rate along adaptive trajectories. To quantify the effe...

---

### 10. EgoLAP: Learning from Egocentric Human Data through Language-Action Reasoning

**Authors:** Lihan Zha, Shresth Grover, Tenny Yin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08726v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08726v1)

**Summary:** Egocentric human data offer a path to scaling robot learning beyond costly robot demonstrations, yet the embodiment gap makes raw human trajectories a poor supervisory target for control. Our key insight is that, although low-level actions are embodiment-specific, their underlying motion intent can capture task-relevant structure that transfers across humans and robots. We introduce EgoLAP, a VLA pre-training framework that jointly learns from human and robot trajectories through a shared langua...

---

### 11. Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus

**Authors:** Egor Pakhomov, Erik Nijkamp

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08722v1)

**Summary:** Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that p...

---

### 12. WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?

**Authors:** Siru Jiang, Yongzhe Lyu, Shuo Lu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08720v1)

**Summary:** LLM-based agents are increasingly advancing scientific and engineering problem solving, with physics simulation emerging as a challenging yet practical testbed for reproducing complex physical phenomena with application in embodied AI, games and films. As the workhorse of such simulation, a solver computes how the state of a dynamic system evolves over time. Building such solvers requires physical understanding to identify appropriate models, mathematical reasoning to formulate the underlying dy...

---

### 13. nanoMuse: An Open-Source Personal Agent for Every Device You Own

**Authors:** Guangyi Liu, Yong Liu, Jiangning Zhang

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08699v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08699v1)

**Summary:** Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This rep...

---

### 14. ScienceClaw: Benchmarking Continual Self-Evolution of AI-for-Science Agents Across the Natural and Social Sciences

**Authors:** Mingda Zhang, Wenjin Liu, Tiesunlong Shen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08691v1)

**Summary:** Large language model agents are accelerating scientific automation, yet verified executions rarely become persistent program-level improvements, and existing evaluations do not examine this process across sequential tasks in both the natural and social sciences. We formalize ScienceClaw as fixed-parameter program self-evolution that unifies task solving, scientific verification, and program updates. ScienceClaw-Eval spans 23 disciplines and measures scientific correctness, evolutionary gain, ret...

---

### 15. Coupled but Late: Turn-Taking Between Full-Duplex Speech Models in Unscripted Dialogue

**Authors:** Lichen Zhu, Yueqian Lin, Yiheng Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08683v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08683v1)

**Summary:** Full-duplex speech models are trained to converse with a person, but they are increasingly made to converse with each other, in self-play data generation, agent societies, and model-based evaluation. In that loop no human absorbs a timing error: each model's turn-taking is the other's input. We ask what timing the loop settles into. Two PersonaPlex-7B instances exchange audio tokens on a shared clock in unscripted conversation, and one floor-transfer rule is applied to them and to Switchboard. T...

---

### 16. Secure Speculative Decoding for Large Language Models

**Authors:** Yichi Zhang, Zhiqi Wang, Neil Gong, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08678v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08678v1)

**Summary:** Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target model for acceptance or rejection. Prior studies primarily focused on the efficiency-utility trade-off of speculative decoding, e.g., lossy speculative decoding, leaving its security implications largely unexplored.   In this work, we bridge t...

---

### 17. Principled Under Pressure: Post-Training Decides Whether LLMs Act on Their Own Moral Judgment

**Authors:** Orion Reblitz-Richardson

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08670v1)

**Summary:** Language models increasingly act as agents. An agent that says an action is wrong and then takes it anyway is a different failure from one that does not know better, and evaluations of stated values cannot see it. We build a pre-registered panel of 248 scenarios across five kinds of pressure. Each scenario is posed twice to the same model, once as the agent choosing what to do and once in the third person asking which option is right, so the model's own judgment is the reference. Every scenario ...

---

### 18. MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge

**Authors:** Mehmet Emre Akbulut, Johannes Geier, Ulf Schlichtmann

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08669v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08669v1)

**Summary:** On-device learning is necessary when the model encounters user-,sensor-, or environment-specific shifts after deployment. Although parameter-efficient fine-tuning (PEFT) methods, particularly Low-Rank Adaptation (LoRA) variants, enable efficient adaptation at the edge, the limiting resource for Convolutional Neural Network (CNN) adaptation is often not the number of trainable parameters but the activation state that must be retained until the backward pass. This paper introduces Memory-Floor LoR...

---

### 19. Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents

**Authors:** Suxin Ji, Hungtao Wan, Shaoxuan Chen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08668v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08668v1)

**Summary:** Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks break in two ways. First, all three prior schemes bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched; in AgentMark's own robustness test, paraphrasing the observation alone drops bit-recovery to 16.8%. Second, every prior agent watermark studies only re...

---

### 20. ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding

**Authors:** Hanjun Luo, Xiucheng Zhang, Zhuoning Xu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08662v1)

**Summary:** As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. Existing work evaluates related agent behaviors from separate perspectives, but lacks a systematic framework for unifying these behaviors. To bridge this gap, we introduce ParanoiaEval, the first benchmark for unified evaluation of risk-treatment capabilities in coding agents. Grounded in the well-established Avoidance-Transfer-Mitigation-Acceptance fram...

---

### 21. Selective Transfer of RL Updates for Visual Reasoning

**Authors:** Suxin Ji, Hungtao Wan, Mingjun Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08659v1)

**Summary:** Model merging provides a training-free way to transfer reasoning capabilities from language models to vision-language models (VLMs), but endpoint-based transfer can conflate pre-existing model differences with changes acquired during reasoning post-training. We instead formulate capability transfer around the training-stage update, isolating the parameter changes induced by reinforcement learning (RL). Yet transferring this update in full remains suboptimal: we find that its components differ su...

---

### 22. A Case Study in Assuring AI-Written Software

**Authors:** Lindsey Ferris, Sierra Bonilla

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08651v1)

**Summary:** Software-engineering agents can enable people without formal software training to build systems they could not otherwise implement and simultaneously can produce more code than even experts can meaningfully inspect. In both cases, exhaustive code review is not reliable as the sole basis for human control. We report a case study of a production healthcare platform built through coding agents and governed by an operator without formal software-engineering training. Over time, its workflow grew int...

---

### 23. SquidAgent: Parallelize Wisely, Coordinate Efficiently

**Authors:** Yexiong Lin, Shanshan Ye, Yu Yao, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08647v1)

**Summary:** LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orch...

---

### 24. HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots

**Authors:** Yurun Chen, Josh Qixuan Sun, Jason Qin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08642v1)

**Summary:** Contact with contaminated objects can spread hazards through a household robot's grippers, tools, and shared surfaces, while new contacts can make an existing plan unsafe. Existing benchmarks do not jointly assess how planners identify hygiene risks from contact history and plan safe continuations after new contact events. Planners must do so within time and resource limits while respecting user priorities. We introduce HygieneRoboBench, with 624 instances across 134 task families, to evaluate s...

---

### 25. Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning

**Authors:** Wanjin Feng, Baobin Zhang, Ao Yu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08627v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08627v1)

**Summary:** Long-horizon world-model planning typically relies on autoregressive rollouts, where predicted states are repeatedly fed back into the model. This preserves temporal structure but creates a horizon-length sequential path and exposes later predictions to recursive decoded-state feedback. We introduce Parallel Predictive World Models (PPWM), which predict a finite-horizon trajectory in parallel while retaining causal interaction among future representations. Each horizon is conditioned on its caus...

---

### 26. Feature Information Dynamics in Diffusion

**Authors:** Jia-Shu Pan, Tao Zhang, Yufei Huang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08626v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08626v1)

**Summary:** Diffusion models generate data through a continuum of denoising problems, and are widely observed to reveal coarse structure before fine detail. Yet, this intuition is mostly empirical and qualitative. We introduce feature information dynamics, an information-theoretic framework for localizing when a feature is generated during diffusion. Using the I-MMSE identity, we connect the rate of feature mutual information change to a gap between optimal unconditional and feature-conditional denoising lo...

---

### 27. Early Memory Selection for Balanced Adam

**Authors:** Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08624v1)

**Summary:** We propose a method for choosing the shared memory parameter $β_1=β_2=β$ in Adam from a short pilot training. The selected $β$ remains fixed during the subsequent full training. A local model of Adam's normalized direction balances sampling variability against the delay introduced by averaging past gradients. This balance gives a cubic memory rule, whose two coefficients are estimated from gradient probes at a few pilot checkpoints. The estimator uses the numerator and denominator jointly, prese...

---

### 28. Agentic RCA for Internet-Scale Services Using Constrained Creativity

**Authors:** Sayan Sinha, Vipul Harsh, B. Aditya Prakash, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08622v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08622v1)

**Summary:** System administrators of Internet-scale services need to resolve failure incidents to maintain reliability of such services. Ideally, we want a troubleshooting system to be: (1) expressive to known and unknown incidents with high accuracy; (2) cost efficient at scale; (3) explainable to provide actionable insights operators can act on; and (4) entail low effort from the operators. Unfortunately, most existing systems, including emerging LLM-assisted agentic workflows and structured frameworks fo...

---

### 29. Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness

**Authors:** Jiajun Chen, Haoyu Wu, Mingda Jia, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08621v1)

**Summary:** Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer, Builder, Player, and Reviewer. The Designer translates user instructions and Reviewer's ...

---

### 30. A Swarm-Coordinated Multi-Robot System for Early Stress Detection in Agricultural Rows Using Multimodal Leaf Sensing

**Authors:** Rishi Gupta, Astha Goyal, Vinay Vishwakarma

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08603v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08603v1)

**Summary:** Early stress detection in crops is a necessity today to improve efficiency and reduce waste of time, money, and effort. However, most modern techniques, such as hyperspectral imaging and AI-based systems, are too costly and complex for medium and small-scale farmers to implement. This paper showcases CropSentry, a low-cost, ground-based multi-robot system that uses multimodal leaf sensing to continuously monitor crop health by tracking stress levels. The system comprises two autonomous bots that...

---

### 31. One for All, All for One: Coordinated Multi-Agent Diffusion Steering via Stochastic Optimal Control

**Authors:** Riccardo Barbano, Vincent Pauline, Runchang Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08595v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08595v1)

**Summary:** Deep generative models often produce structured outputs composed of interacting components. Modelling these outputs with a single model requires learning both the component distributions and their interactions. We pursue a modular alternative: reuse independently trained component generators and learn only how to coordinate them to produce coherent structured outputs. Our framework, Coordinated Multi-Agent Diffusion Steering (CMDS), treats frozen pretrained diffusion models as reusable generativ...

---

### 32. MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory

**Authors:** Sujato Dutta, Sreekruthy Tummala, Shashank Vanga, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08586v1)

**Summary:** Long conversational agents have become essential in our daily lives. They must remember what was said long back in order to help us efficiently complete a task without needing the user to repeat instructions and context repeatedly. However, the main issue is that instructions and context change over time and so the agents must be able to adapt accordingly. A useful memory system should preserve both current and historical states, distinguish stale information from active knowledge, retrieve evid...

---

### 33. How Learning Governs Unlearning across the Memorization-Generalization Spectrum

**Authors:** Hwiyeong Lee, Hyelim Lim, Ingyu Bang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08577v1)

**Summary:** While unlearning seeks to negate undesired capabilities acquired through learning, little research has examined how the way models learn shapes their subsequent unlearning. In this paper, we investigate this connection from the perspectives of memorization and generalization, the two most representative yet competing strategies that models employ during training. We first classify memorization- and generalization-heavy models using grokking in modular addition and compare their responses to unle...

---

### 34. FedDermaSeg: Federated Learning for Dermatological Image Segmentation

**Authors:** Anabik Pal, Ganesh Patidar, Bikash Santra

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08574v1)

**Summary:** Skin cancer is a major global health concern, and early detection and accurate lesion delineation are important for effective diagnosis and treatment planning. Automated skin lesion analysis can assist dermatologists, with lesion segmentation serving as a fundamental step in computer-aided diagnostic systems. Conventional deep learning-based segmentation models typically rely on centralized training, where images and their corresponding segmentation masks are collected on a central server. Such ...

---

### 35. RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems

**Authors:** Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08571v1)

**Summary:** Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train, validation, and protected-test splits. Using a leakage-aware construction pipeline and strict evaluation protocol, we compare keyword-based, semantic-reference, TF-IDF, and transformer-based detectors. DistilBERT achieves the best protected-tes...

---

### 36. Adaptive Power Sampling for LLM Reasoning

**Authors:** Bingnan Xiao, Chenhao Yang, Bingcong Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08563v1)

**Summary:** Sequence-level power sampling has recently emerged as a training-free approach to reasoning by sampling from a sharpened output distribution of a base large language model (LLM). Nevertheless, existing methods typically sharpen the base model distribution uniformly across queries, overlooking variations in query difficulty and in how well the base model already handles each query. The goal of this work is to equip power sampling with query adaptivity. Theoretically, we show that the benefits of ...

---

### 37. Latent space bias directions in LLMs capture confidence, not fairness

**Authors:** Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08559v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08559v1)

**Summary:** Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activatio...

---

### 38. Systemization of Knowledge (SoK): Human-Centered AI Safety for Youth

**Authors:** Pratyasha Saha, Yaman Yu, Yang Wang

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08554v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08554v1)

**Summary:** While HCI increasingly examines AI-safety for youth, the literature lacks a comprehensive view of what risks have been identified, how they are addressed, and whether proposed protections work in-practice. We systematically reviewed 100 empirical HCI studies involving children and youth interacting with or exposed to AI across schools, homes, care settings, and public services. Using the YAIR taxonomy for risks and the MIT Mitigation Taxonomy for countermeasures, we map which risks have been ide...

---

### 39. DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory

**Authors:** Yining Li, Dongchen Han, Jie Fu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08553v1)

**Summary:** Sequential test-time training adapts a memory network through successive updates, each computing an inner-loop gradient based on the network's previous state. Intuitively, this state dependence should allow each update to account for what the memory has already learned and better incorporate new information. However, we find that this expected advantage does not consistently materialize in nonlinear memories: a fixed-base parallel TTT baseline outperforms its serial counterpart. Our exploratory ...

---

### 40. AnyBottle: A Recipe to Only Keep the Concepts You Really Need

**Authors:** Wolfgang Stammer, Sukrut Rao, Hevra Petekkaya, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08552v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08552v1)

**Summary:** Concept bottleneck models (CBMs) make predictions inspectable and intervenable by routing them through human-interpretable concepts, but originally required concept annotations. Annotation-free variants remove this requirement, but typically use large concept vocabularies, static at both training and inference, producing bottlenecks larger than any task or prediction needs and harder to inspect. We propose AnyBottle, a single recipe for building compact, task-specific CBMs. AnyBottle assumes onl...

---

### 41. How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing

**Authors:** Pranjal Garg

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08544v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08544v1)

**Summary:** Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input already gives away, and the same score can mean different things on different data. We propose reading every probe score against two reference points: a floor, what a declared set of simple inputs already predicts, and a ceiling, what the full input can predict. The gap between them,...

---

### 42. Micro Neural Policies for Safe Real-Time Robotic Control

**Authors:** Hongpeng Cao, Riccardo Curcio, Daniele Ottaviano, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08541v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08541v1)

**Summary:** In this paper, we investigate the synthesis of Micro Neural Policies (MNP) to enable safe and robust real-time robotic control on computationally constrained embedded devices. We demonstrate that integrating Evolution Strategy (ES) and Statistical Model Checking (SMC)-based verification for policy search can drastically reduce neural network size without compromising safety and robustness. We conduct a large-scale training and evaluation of MNP on Cartpole and Quadrotor control tasks, varying co...

---

### 43. Toward Alignment Scaling Laws: A Framework and First Preregistered Measurements

**Authors:** Jeremy Canale

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08540v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08540v1)

**Summary:** Whether alignment gets easier or harder as models grow is often argued from isolated findings, as if alignment were one property. We treat it as a family of measurable scaling relations: for each risk category r, the alignment burden needed to hold a fixed safety target is modeled as B_r(N)=a_rN^alpha_r, with N a capability proxy; against a budget proportional to N, scaling helps if alpha_r<1, keeps pace if alpha_r~1, and accumulates alignment debt if alpha_r>1. We give three operationalizations...

---

### 44. From Shared Demand Patterns to Local Uncertainty: Probabilistic Load Forecasting by Mixing Compact Adaptations

**Authors:** Haoran Li, Zhe Cheng, Yang Weng

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08538v1)

**Summary:** Probabilistic load forecasting has been widely studied for power-system operation and planning, but customer- and transformer-level forecasting introduces a distinct scalability challenge. At these levels, load uncertainty is strongly affected by customer behavior, weather, and mixed load composition, making it difficult for a single shared model to capture heterogeneous patterns. Using separate probabilistic models can improve local accuracy, but becomes costly to train, store, update, and vali...

---

### 45. FlowCF: Sparse Counterfactual Explanations for Mixed-Type Tabular Data using Flow Matching

**Authors:** Emmanouil Panagiotou, Eirini Ntoutsi

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08537v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08537v1)

**Summary:** In the field of Explainable AI (XAI), counterfactual (CF) explanations interpret a model's decision by suggesting the changes to the input that would lead to a more favourable outcome. To be useful in practice, such an explanation should change few features and change them as little as possible, properties known as sparsity and proximity. We observe that existing methods remain limited in this respect, especially for numerical features, whether they are model-agnostic and amortised, or gradient-...

---

### 46. MedCORE: Criteria-Grounded Clinical Reasoning for Interpretable Medical Image Diagnosis

**Authors:** Asim Khan, Samee Ullah Khan, Dwarikanath Mahapatra

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08528v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08528v1)

**Summary:** Clinical diagnosis is inherently a structured reasoning process, yet existing deep learning models often bypass this structure by mapping image features directly to disease labels without explicitly interrogating the morphological and textural criteria that clinicians systematically evaluate. This limits diagnostic transparency and may compromise safe clinical deployment. We present MedCORE (Medical Criteria-Oriented Reasoning and Evidence), a structured diagnostic framework that operationalizes...

---

### 47. How Much Evidence Should a Coding Agent's Self-Correction Carry? Adaptive Dirichlet Evidence for Self-Distillation

**Authors:** Yunbo Long, Guangya Hao, Yuhan Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08514v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08514v1)

**Summary:** Execution feedback lets coding agents revise programs and learn from their own corrections. A correction's learning weight should reflect both the transitions supported by its executions and the amount of evidence behind that support. We introduce Effective-Evidence Self-Distillation (EESD), which represents these quantities separately. Normalized execution relevance determines relative transition support and an effective pseudo-count mass; a Dirichlet posterior then produces an uncertainty-pena...

---

### 48. Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions

**Authors:** Dennis Fucci, Andrea Bacciu, Dong Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08513v1)

**Summary:** LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from...

---

### 49. Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation

**Authors:** Onur Selim Kilic, Afra Nawar, Cem Okan Yaldiz, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08510v1)

**Summary:** Paired translation between quasiperiodic physiological waveforms (i.e., recovering a target oscillatory signal from the source) is central to the interpretation of cardiovascular signals derived from wearables placed at different body locations. This source-to-target mapping in these problems carries inherent geometric structure: the phase wraps around the cycle and must be treated as a circular variable, the amplitude remains strictly positive, and the beat-to-beat alignment can drift unpredict...

---

### 50. X-OPM: Explainable Automatic Digital On-Chip Power Modeling for Enhanced Robustness

**Authors:** Jingbo Jiang, Xizi Chen, Jian Peng, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08502v1)

**Summary:** Proactive power management systems reduce processor dynamic power through runtime power prediction and power-aware scheduling. Accurate, stable and low-overhead digital on-chip power meters (OPMs) are crucial for improving the prediction quality. Recent studies have explored various modeling methods, including using linear models, decision trees, and multi-layer perceptrons (MLPs) to construct OPMs. However, most current approaches train models end-to-end without analyzing the physical interpret...

---

## cs.CL

**50 papers**

### 1. IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas

**Authors:** Ziyu Chen, Yilun Zhao, Jiashuo Sun, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08781v1)

**Summary:** Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-grounded ideation remains challenging, as existing approaches based on prompting or feedback lack structured supervision for how papers should be synthesized. We introduce IdeaAnchor, a paradigm for training LLMs to perform research ideation using structured specifications as privileged signals. Eac...

---

### 2. Sherpa: Teaching LLMs to Teach Adaptively

**Authors:** Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08778v1)

**Summary:** Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address t...

---

### 3. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08773v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08773v1)

**Summary:** Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a t...

---

### 4. The Missing Minimal Pair: Stereotype Evaluation in LLMs

**Authors:** Nataliya Stepanova, Ivan Titov, Emily Allaway, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08747v1)

**Summary:** A common approach to measuring bias in Large Language Models is to compare the log-likelihoods of two contrastive stereotype sentences. We argue that such single-pair comparisons are often unreliable: simply rewriting the same stereotype with an alternative attribute can yield logically inconsistent preferences. To address this, we propose a dual minimal pair setup that introduces two axes of comparison for robust stereotype evaluation. First, we present a data-augmentation framework that fills ...

---

### 5. Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling

**Authors:** Mathias Ollu, Nikos Komodakis

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08738v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08738v1)

**Summary:** Diffusion Language Models (DLMs) hold the promise of order-agnostic, parallel text generation. Recently, continuous diffusion and flow matching models have seen substantial gains, driven by carefully crafted token representations and diffusion/flow spaces. In this work, we introduce Hierarchical Continuous Diffusion Language Models (H-CDLMs), a simple framework that further improves continuous DLMs with minimal compute and parameter overhead. Drawing on the discrete DLM and continuous image diff...

---

### 6. A Systematic Study of Semantic ID Spaces for Generative Information Retrieval

**Authors:** Alexia Allal, Hicham Randrianarivo, Sylvain Lamprier

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08732v1)

**Summary:** Generative Information Retrieval (GIR) has emerged as a transformative paradigm, shifting document retrieval from a traditional "retrieve-and-rank" workflow to sequence-to-sequence generation, where a model directly predicts document identifiers (DocIDs). While the semantic design of these DocIDs is known to be critical for performance, a fundamental question remains under-explored: what makes a good DocID? Current approaches rely heavily on computationally expensive downstream evaluations, hind...

---

### 7. Holdout Best-of-N: Unbiased Evaluation and Its Cost

**Authors:** Shrey Shah, Yinheng Li

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08719v1)

**Summary:** Reusing the scores that select a Best-of-$N$ winner can overstate its expected reward. We study evaluation from a fixed matrix of $K$ independent scores per candidate for a policy that selects using $J$ fresh scores. A single estimator based only on this matrix is exactly unbiased for expected judge reward under every independent, stable collection of candidate-specific score laws if and only if $J<K$, for every pool size $M\ge N\ge2$. At $J=K-1$, the selector deepens as $K$ grows. For independe...

---

### 8. When Forgetting is not Catastrophic: On the Mechanics of Spurious Forgetting

**Authors:** Vedant Palit, Florent Draye, Nicolas Zucchet, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08718v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08718v1)

**Summary:** Knowledge that a language model appears to forget during finetuning often remains stored and can be recovered, a phenomenon called spurious forgetting. Finetuning on new facts can even produce forgetting that undoes itself: recall of the old facts collapses, recovers as training continues on new facts alone, and only then erodes for good. We seek to understand when such forgetting is not catastrophic. A minimal associative memory reproduces these dynamics with three ingredients: keys with shared...

---

### 9. Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval

**Authors:** Hicham Randrianarivo, Logan Renaud, Alexia Allal

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08716v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08716v1)

**Summary:** Generative retrieval trains a language model to generate the identifier of a relevant document. Recent work replaces the autoregressive decoder with diffusion, but changes identifiers, training recipe and decoding at once, so differences cannot be credited to the paradigm. On NQ320K and MS300K, we train autoregressive, masked-diffusion and block-diffusion models with residual-quantised, product-quantised and random identifiers. With identifier length and training budget fixed, we decode each mod...

---

### 10. Agreement Is Not Validity: Cross-Model LLM Consensus in Diagnosing Student Failure Modes in K-12 Math Tutoring Dialogue

**Authors:** Clayton Cohn, Joyce Fonteles, Kirk Vanacore, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08703v1)

**Summary:** In K-12 mathematics tutoring, student-tutor dialogue provides rich evidence of learners' problem-solving processes and sources of difficulty. Learning analytics research increasingly relies on large language models (LLMs) to extract such information from dialogue for a variety of downstream tasks, including knowledge tracing, behavioral modeling, and diagnosis of student reasoning errors. However, the validity of these model-generated interpretations remains insufficiently understood. In this ex...

---

### 11. A Systematic Study of Small Language Models on Abstract Reasoning Tasks

**Authors:** Nur A Zarin Nishat, Jens Lehmann, Andrei Aioanei, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08680v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08680v1)

**Summary:** Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in small language models on the ARC-TGI benchmark, which organizes abstract grid transformations into controllable task families and supports resampling, spatial shifts, and cross-benchmark transfer. Across more than 1,000 runs, we profile decoder-only, encoder--decoder, and mixture-of-experts model famil...

---

### 12. Same-Number Citation Swaps: Stress-Testing Jev as a Financial Evidence Judge

**Authors:** Chuhong Xu, Bo Su, Ziyao Chen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08675v1)

**Summary:** Financial reports repeat values across periods, metrics and accounting lines, allowing an LLM-generated calculation to be numerically correct while citing the wrong financial role. We evaluate what probabilistic evidence verification adds beyond number matching using Jev as a source-support verifier for GPT-4.1-mini calculation traces. A signed-number-at-pointer baseline explains most recovery over exact quotation checks. To isolate the remaining role-recognition problem, we hold operands and ar...

---

### 13. Principled Under Pressure: Post-Training Decides Whether LLMs Act on Their Own Moral Judgment

**Authors:** Orion Reblitz-Richardson

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08670v1)

**Summary:** Language models increasingly act as agents. An agent that says an action is wrong and then takes it anyway is a different failure from one that does not know better, and evaluations of stated values cannot see it. We build a pre-registered panel of 248 scenarios across five kinds of pressure. Each scenario is posed twice to the same model, once as the agent choosing what to do and once in the third person asking which option is right, so the model's own judgment is the reference. Every scenario ...

---

### 14. Evidence-Bound Reasoning: Neuro-Semantic Verification of Biomedical AI in Glioblastoma Radiogenomics

**Authors:** Mariya Miteva, Maria Nisheva-Pavlova

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08660v1)

**Summary:** Background: Biomedical AI can generate plausible explanations without reliably verifying whether each statement is supported by patient-specific evidence. We developed a neuro-semantic verification framework that converts radiomic measurements into addressable evidence records and machine-checkable claims. Methods: UPenn-GBM radiomics were aligned with de novo CaPTk extraction from standardized MRI and expert-validated segmentations in an independent multicenter cohort. The shared space comprise...

---

### 15. SquidAgent: Parallelize Wisely, Coordinate Efficiently

**Authors:** Yexiong Lin, Shanshan Ye, Yu Yao, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08647v1)

**Summary:** LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orch...

---

### 16. Towards In-Parameter Memory Augmentation for Large Language Models

**Authors:** Haoyu Huang, Zhongwei Xie, Jiaxin Bai, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08630v1)

**Summary:** Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. \textbf{In-parameter memory} offers a complementary substrate: reusable memory information is represented in mo...

---

### 17. InterCorrect: Intersection-Aware Correction of Demographic Model Merging for Fair ASR

**Authors:** Ashley E. Bravo-Bravo, Yuchen Zhang, Haralambos Mouratidis, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08604v1)

**Summary:** Automatic Speech Recognition (ASR) systems often show uneven performance across demographic groups, and errors can be especially difficult to address for speakers belonging to multiple demographic groups. This work studies demographic-aware model merging for fair Speech-LLM-based ASR. Starting from a SLAM-ASR-based model, we fine-tune only the connector on demographic-specific subsets and merge the resulting subgroup-adapted connectors into a global model. We then identify critical cross-axis de...

---

### 18. Generative AI translations in high-stakes emergency messaging

**Authors:** Nune Ayvazan, Anthony Pym, Yu Hao

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08601v1)

**Summary:** Emergency messaging such as extreme-weather reports and earthquake instructions can involve high stakes, to the extent that translation errors can lead to tragic consequences. The use of machine translation or generative artificial intelligence might therefore not be recommended. On the other hand, time savings in the initial translation can allow greater investments of resources in revision and authorization processes, as well as a wider range of target languages. An experiment with generative ...

---

### 19. Incidental information contaminates patient notes and disrupts clinical reasoning in large language models

**Authors:** Krithik Vishwanath, Brandon Ye, Anton Alyakin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08585v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08585v1)

**Summary:** Large language models (LLMs) are increasingly relied upon to support ambient documentation and clinical reasoning. Here we examine the impact of a failure mode shared between these two applications by assessing their sensitivity to information incidental to the patient encounter. In 576 patient-clinician dialogues, we found that frontier models inserted small-talk exchanges into 35% of notes, while mean quality scores changed by at most 0.20 points on five-point scales. In 3.7% of frontier notes...

---

### 20. Have I Seen Enough? Frozen Video-Language Models Encode Evidence Readiness

**Authors:** Dan Ben-Ami, Kobi Cohen, Chaim Baskin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08560v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08560v1)

**Summary:** Streaming video-language models must decide not only what to answer, but whether the evidence needed for the current question has arrived. Existing systems learn that decision as a separate trigger; we ask whether an unmodified model already computes it. We show that frozen VideoLLMs carry a linearly readable evidence-readiness signal, labelled from timestamped evidence rather than from model output. It decodes in all seven models of a shared byte-identical evaluation (AUROC 0.733-0.905 under th...

---

### 21. Latent space bias directions in LLMs capture confidence, not fairness

**Authors:** Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08559v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08559v1)

**Summary:** Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activatio...

---

### 22. DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory

**Authors:** Yining Li, Dongchen Han, Jie Fu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08553v1)

**Summary:** Sequential test-time training adapts a memory network through successive updates, each computing an inner-loop gradient based on the network's previous state. Intuitively, this state dependence should allow each update to account for what the memory has already learned and better incorporate new information. However, we find that this expected advantage does not consistently materialize in nonlinear memories: a fixed-base parallel TTT baseline outperforms its serial counterpart. Our exploratory ...

---

### 23. How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing

**Authors:** Pranjal Garg

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08544v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08544v1)

**Summary:** Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input already gives away, and the same score can mean different things on different data. We propose reading every probe score against two reference points: a floor, what a declared set of simple inputs already predicts, and a ceiling, what the full input can predict. The gap between them,...

---

### 24. Toward Alignment Scaling Laws: A Framework and First Preregistered Measurements

**Authors:** Jeremy Canale

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08540v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08540v1)

**Summary:** Whether alignment gets easier or harder as models grow is often argued from isolated findings, as if alignment were one property. We treat it as a family of measurable scaling relations: for each risk category r, the alignment burden needed to hold a fixed safety target is modeled as B_r(N)=a_rN^alpha_r, with N a capability proxy; against a budget proportional to N, scaling helps if alpha_r<1, keeps pace if alpha_r~1, and accumulates alignment debt if alpha_r>1. We give three operationalizations...

---

### 25. Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions

**Authors:** Dennis Fucci, Andrea Bacciu, Dong Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08513v1)

**Summary:** LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from...

---

### 26. Language-model ratings of depression reflect the rater more than the patient

**Authors:** Baihan Lin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08501v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08501v1)

**Summary:** Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...

---

### 27. UNREAL: Unifying Retrieval and Long-Context with a Single Model

**Authors:** Edan Kinderman, Elad Hoffer, Yochai Blau, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08463v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08463v1)

**Summary:** Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales, from a single long prompt to an entire corpus. We ask whether a single model-internal mechanism can select evidence across this range. We introduce UNifying REtrieval And Long-Context with a Single Model (UNREAL), a model-native evidence selection framework to span corpus retrieval and long-context inference. UNREAL encodes chunks and derives retrieval queries directly from the f...

---

### 28. Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents

**Authors:** Lasse B. Strand, Robert Jakob, Kevin O'Sullivan, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08452v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08452v1)

**Summary:** Retrieval-augmented generation (RAG) is a widely used approach for grounding large language models (LLMs) in external knowledge. However, configuring a pipeline is an expensive hyperparameter optimization problem over many interacting choices, from chunking and embedding model to reranking and generation. Existing optimizers, from greedy search to Bayesian optimization, reduce each trial to an aggregate score and search without modeling why a configuration performed as it did, even though the re...

---

### 29. Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability

**Authors:** Bingxi Hou, Guochao Jiang, Guofeng Quan, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08448v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08448v1)

**Summary:** On-Policy Distillation (OPD) trains a student on its own generations using teacher feedback. With different tokenizers, comparing teacher and student predictions requires alignment at both sequence and vocabulary levels. In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1 groups already cover most student-generated tokens despite substantial vocabulary mi...

---

### 30. Knowing When Not to Answer: Cross-Domain and Multi-Turn Generalization of Latent Underspecification Signals

**Authors:** Jerzy Kamiński, Ilya Galyukshev, Artem Kuznetsov, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08413v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08413v1)

**Summary:** Large language models routinely answer questions that cannot be answered from the information given, and in dialogue they answer before enough has been said. Unanswerability is linearly decodable from hidden states, but it is unclear which of its forms share a representation and whether the signal is useful in dialogue. We contribute a turn-labeled multi-turn benchmark (423 conversations, 1,661 labeled turn-states) and an evaluation harness with a simulated user who answers clarifying questions,...

---

### 31. Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering

**Authors:** Yang Hong, Yajun Yang, Xin Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08388v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08388v1)

**Summary:** Large language models (LLMs) have demonstrated strong capabilities in question answering, yet they still frequently suffer from hallucinations on knowledge-intensive tasks. Knowledge graphs (KGs) provide LLMs with structured, interpretable, and updatable factual grounding, making them a promising external knowledge source for reliable reasoning. However, existing LLM-guided graph reasoning methods typically rely on hop-wise greedy or beam-style pruning during evidence retrieval. Such local decis...

---

### 32. CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs via Knowledge Consolidation and Decoupling

**Authors:** Maoqi Liu, Quan Fang, Yufei He

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08312v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08312v1)

**Summary:** Continual learning (CL) is essential for Large Language Models (LLMs) to sequentially adapt to evolving tasks. To mitigate catastrophic forgetting, recent advances implement low-rank adaptation with orthogonal projections (e.g., O-LoRA) to isolate task parameters. However, we reveal that such strict geometric constraints trigger an "Orthogonality Dilemma": rigid parameter isolation impedes the transfer and accumulation of shared representations across semantically related tasks. In this work, we...

---

### 33. Language Unalignability: Why Some Concepts Resist Cross-Cultural Benchmark Evaluation

**Authors:** Shu-Kai Hsieh, Da-Chen Lian

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08303v1)

**Summary:** Current evaluation of multilingual Large Language Models (LLMs) rests on an implicit Translation-Isomorphism Assumption (TIA): that semantic structures across languages are congruent and mutually mappable without loss of information. We argue that this assumption is not merely violated in practice, but ill-posed in principle for a typologically identifiable class of concepts, including pragmatic markers, honorifics, and diachronically stratified terms. We formalize this failure using a usage-clo...

---

### 34. Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval

**Authors:** Michael Andreev

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08300v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08300v1)

**Summary:** Long-term conversational memory is becoming an integral component of modern LLM systems. Proposed architectures group records by topics and events, construct hierarchies and graphs, and connect facts through causal and temporal relations. We experimentally study the interaction between two memory parameters: structural depth and the width of context supplied to the answer model. Using EverMemBench, we evaluate depths D1-D4, core budgets of 1,024/2,048/4,096 tokens, and additional Production and ...

---

### 35. STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty

**Authors:** Nina Nusbaumer, Iria de-Dios-Flores, Corentin Bel, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08208v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08208v1)

**Summary:** We introduce STRUCTURALCOST, a self-paced reading dataset of 475 participants and 40,800 observations isolating the processing cost of long-distance subject-verb dependency resolution. We replicate a low-powered psycholinguistic finding at NLP scale, namely that human reading times at the main verb increase with dependency length, driven by syntactic embedding beyond linear distance. Different language models -- spanning n-gram models, SSMs, and transformers -- partially mirror this graded diffi...

---

### 36. Align, Then Correct: Training-Free Two-Stage Low-Rank Compensation for Extremely Quantized Large Language Models

**Authors:** Seobin Song, Geonho Lee, Janghwan Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08164v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08164v1)

**Summary:** Low-rank quantization error compensation (LQEC) recovers the accuracy lost under aggressive weight quantization by attaching a closed-form rank-$r$ adapter beside each frozen quantized weight, without any training. We show that existing compensators are limited by two shared simplifications. They calibrate symmetrically, evaluating the full-precision and compensated weights on the same activation, which yields a compensation target that is inherently high-rank -- so a fixed rank budget captures ...

---

### 37. The Failure Is in the Readout: Fine-Grained Emotion Recognition Benchmarks Measure Elicitation, Not Perception

**Authors:** Tobias Hallmen, Fabian Deuser, Robin-Nico Kampa, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08162v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08162v1)

**Summary:** Fine-grained emotion recognition supports therapy tools and social robots, but it needs facial data, which raises privacy and data-protection concerns. EmoNet-Face-HQ answers that with generated portraits, expert-rated over a $40$-category taxonomy far finer than the usual six to eight basic emotions. Under the protocol it ships with, vision-language models (VLMs) score poorly on that taxonomy, and the benchmark concludes that a dedicated fine-tuned model is necessary: Empathic-Insight-Face (EIF...

---

### 38. Symphony for Text Generation: Benchmarking Clinical Note Generation

**Authors:** Daniel Varab, Victor Petrén Bach Hansen, Asbjørn W. Helge, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08161v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08161v1)

**Summary:** Ambient documentation systems are rapidly gaining adoption, yet their impact on clinical note quality remains poorly characterized. We introduce MedConv, a multilingual dataset of 300 clinical encounters in English, Danish, and German, and use it alongside the Ambient Clinical Intelligence benchmark (ACI-BENCH) to compare Corti, a clinical AI platform, with two leading, accessible ambient scribe software applications built on general-purpose AI. We present a controlled clinical evaluation framew...

---

### 39. Making COMET Comparable Across Scripts: Diagnosis and Correction of Tokeniser-Induced Script Bias in Indic MT Evaluation

**Authors:** G. L. John Salvin, Swapnil Hingmire

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08159v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08159v1)

**Summary:** COMET reports translation quality as a single number, and that number is routinely compared across target languages written in different scripts. Such a comparison assumes Script Invariance: the score should not depend on the writing system that carries the target. We test it on IndicMT Eval by re-encoding the target into Latin script, which changes orthographic form while holding content and human ratings fixed. Script identity then accounts for 22.9% of native-script COMET variance, and agreem...

---

### 40. Penalty-Framed No-Valid-Option MCQA: Analyzing LLM Abstention under Invalid Choices

**Authors:** Jinhyeok Kim, Hye-Young Jung

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08153v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08153v1)

**Summary:** Multiple-choice question answering (MCQA) is commonly used to evaluate large language models under the assumption that one of the provided options is correct, typically using answer-selection accuracy. However, in real deployments, users or retrieval systems may provide invalid option sets in which none of the listed choices is correct, and selecting one of them may incur downstream cost. We study this setting as penalty-framed no-valid-option MCQA. Using the mathematics subset of MMLU-Pro, we r...

---

### 41. Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models

**Authors:** Sungnyun Kim, Sungwoo Cho, Jihwan Oh, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08125v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08125v1)

**Summary:** Full-duplex spoken dialogue models listen and speak at the same time, enabling voice agents to have natural, low-latency interactions that turn-based systems cannot offer. However, they are commonly evaluated against single-sided interlocutors: pre-recorded audio that cannot react, or an automated examiner that reacts in real time but only administers a fixed sequence of tests and is never graded. These single-sided frameworks evaluate only half of a two-body problem, where turn-taking, overlap,...

---

### 42. Natural Language Questions as an Interface for Knowledge Graphs: QRAKEN Graph Distillation and Semantic Self-Healing

**Authors:** Remo Grillo, Lukas Klic, Giovanni Colavizza

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08095v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08095v1)

**Summary:** Natural-language access to RDF knowledge graphs is a core Semantic Web ambition. Large language models (LLMs) have advanced Text-to-SPARQL, yet on unfamiliar graphs they often generate valid queries that misrepresent the populated data model. QRAKEN is a training-free, ontology-agnostic neurosymbolic pipeline grounding generation in empirical graph evidence rather than schema expectations. An offline distiller produces TTQL, a compact description of populated multi-hop patterns, conditional freq...

---

### 43. SAGE: Semantic Anchor-Guided Evolution for Grounded Medical QA Data Synthesis

**Authors:** Chuan Li, Chengyu Wang, Cen Chen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08093v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08093v1)

**Summary:** Developing reliable models for clinical tasks, such as Medical Question Answering (QA), is severely constrained by the limited availability of high-quality, expert-annotated training data. This challenge is exacerbated by stringent privacy requirements and the impracticality of utilizing large open-source corpora or proprietary cloud APIs within resource-limited clinical settings. To address these obstacles, we introduce SAGE (\textit{Semantic Anchor-Guided Evolution}), a novel data synthesis fr...

---

### 44. DirectSpeech2LLM: A Simple End-to-End Framework to Mitigate Prompt Overfitting in Speech-LLMs

**Authors:** Hemant Yadav, Sunayana Sitaram, Roger Zimmermann, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08085v1)

**Summary:** Speech-LLMs often exhibit prompt overfitting, where models solely trained on automatic speech recognition (ASR) instruction fail to generalize to new instructions such as speech translation and continue to behave primarily as ASR system. We propose DirectSpeech2LLM, a simple end-to-end framework that preserves the instruction-following ability of the LLM on unseen tasks when conditioned on speech. It computes distance-based CTC loss over the frozen LLM embedding matrix and uses greedy CTC labels...

---

### 45. POLAR: Ontology-Guided Risk Prevention for Tool-Calling LLM Agents

**Authors:** Yunju Kang, Seonghyeon Cho, Irene Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08082v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08082v1)

**Summary:** LLM tool-use agents operate in dynamic environments where many actions carry operational risk. However, most safety mechanisms react only after errors manifest. Existing pre-emptive approaches either fine-tune the agent on chain-of-thought deliberation or compile natural-language guardrails into runtime checks, but they do so without exposing a structural, auditable verdict. We propose POLAR, a guardrail framework for small tool-calling agents that assesses reversibility through a structured two...

---

### 46. Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

**Authors:** Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08077v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08077v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can hindsight teach an agent what it could have anticipated before acting? We introduce p...

---

### 47. HINTT Submission to the 2nd MLC-SLM Challenge: Comparing Cascaded and Unified Approaches to Diarization and ASR

**Authors:** Takanori Ashihara, Kohei Matsuura, Masato Mimura

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08063v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08063v1)

**Summary:** This paper presents the HINTT system submitted to the 2nd Challenge and Workshop on Multilingual Conversational Speech Language Model (MLC-SLM). We address multilingual speaker-attributed ASR, where systems must determine who spoke when and what was spoken. We investigate two modeling strategies for this problem: a cascaded pipeline that combines speaker diarization with speech-LLM-based ASR, and a unified speech LLM that directly generates speaker labels, timestamps, and transcriptions. Our fin...

---

### 48. Language Carries the Expert's Impression: Instrument-Anchored LLM Judges Transfer Counseling-Quality Assessment and Beat In-Domain Training

**Authors:** Tobias Hallmen, Elisabeth André

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08055v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08055v1)

**Summary:** Automatic assessment of communication quality in dyadic counseling conversations is bottlenecked by data: expert-rated corpora are small and expensive to grow. We study cross-domain transfer of expert overall-impression prediction across three German corpora of simulated counseling (two general-practice medical, one school-related parent-teacher; $n=195$ expert-rated sessions, one corpus after scale equating). Training on the other domains beats training in-domain: leave-one-domain-out transfer ...

---

### 49. DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks

**Authors:** Antoine Edy, Max Conti, Victor Xing, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08048v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08048v1)

**Summary:** LLM agents often lack the operational knowledge to act reliably in new environments, as they must discover specific tool behaviors or environment conventions on their own. Without memory of past attempts, they repeat the same mistakes across tasks, leading to more task failures and longer trajectories. To address this, agentic systems typically rely on human-written guidelines or on procedural memory built from training tasks and an oracle verifier, both of which require prior knowledge of the e...

---

### 50. Are Language Models Script-Aware?

**Authors:** David Kletz, Sandra Mitrović, Ljiljana Dolamić, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08037v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08037v1)

**Summary:** Language models frequently generate outputs in unintended languages or scripts, a phenomenon known as off-target generation. While existing research has focused on language selection, the dimension of script knowledge remains understudied: before any linguistic understanding can occur, users must recognize the graphic symbols in a model's response. We investigate whether Small and Large Language Models (SLMs and LLMs) possess script knowledge by testing them on multi-scriptic languages. Through ...

---

## cs.CV

**50 papers**

### 1. World Models' Last Exam in Physics

**Authors:** Mingju Gao, Qingle Liu, Yuzhao Peng, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08791v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08791v1)

**Summary:** Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks s...

---

### 2. Building Rome from a Single Image

**Authors:** Jiraphon Yenphraphai, Fang Li, Tianshuo Xu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08790v1)

**Summary:** Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that redesigns such an object-centric generator, e.g., Trellis 2, to work on both indoor an...

---

### 3. 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction

**Authors:** Shiqi Li, Sean Cho, Yijie Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08782v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08782v1)

**Summary:** Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-...

---

### 4. DepthWorld: 3D World Model for Robot Manipulation

**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08780v1)

**Summary:** World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absor...

---

### 5. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing

**Authors:** Zhenghong Zhou, Zhe Lin, Jiebo Luo, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08779v1)

**Summary:** Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs i...

---

### 6. CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching

**Authors:** Shangye Song, Dong Gong, Hong Jia, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08777v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08777v1)

**Summary:** Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explici...

---

### 7. Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation

**Authors:** Liao Ma, Jiayi Song, Yunfeng Wu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08772v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08772v1)

**Summary:** Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible...

---

### 8. Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap

**Authors:** Mohammed Q. Alkhatib

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08770v1)

**Summary:** Patch-based learning improves hyperspectral image (HSI) classification by exploiting local spectral-spatial information, but random train-test sampling from the same image can cause spatial patch overlap, leading to data leakage and optimistic performance estimates. This paper investigates same-class train-test spatial overlap in patch-based HSI classification using two measures: overlap percentage (OP), which quantifies the global amount of overlapped testing patch pixels, and average overlap r...

---

### 9. WorldSonus: Bringing Sound to Worlds

**Authors:** Pengjun Fang, Jingyi Fa, Kam Man Wu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08760v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08760v1)

**Summary:** Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To address these demands, we introduce WorldSonus, an interactive video-to-audio framewo...

---

### 10. Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error

**Authors:** Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08756v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08756v1)

**Summary:** The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combi...

---

### 11. Co-Evolving Paths and Flows via Path-Flow Alignment

**Authors:** Zeyu Michael Li, William Xingxu Chen, Xiang Cheng

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08717v1)

**Summary:** We study path-flow alignment as a unified training objective for flow matching. Instead of fixing the interpolation path and learning only the velocity field, we jointly train an endpoint-preserving path network and a flow network using the same alignment loss: the flow learns to match the path velocity, and the path learns to align its velocity to the current flow. Although every fixed learned path defines a valid flow-matching objective, the alignment loss alone is not a reliable criterion for...

---

### 12. SpaTime: Streaming Vision-Language Models for Spatio-temporal Reasoning

**Authors:** Hairong Yin, Huangying Zhan, Shin-Fang Chng, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08713v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08713v1)

**Summary:** Embodied agents must reason about 3D space while the video is still arriving, answering questions as soon as they have observed enough of the scene. VLMs that incorporate 3D geometric priors achieve strong spatial reasoning, but they operate offline, i.e., the full video must be available before they produce an answer. Streaming VLMs process frames causally and decide for themselves when to respond, yet they lack explicit 3D representations. We present SpaTime, a streaming VLM that fuses causal ...

---

### 13. Local Content-Style Control for Diffusion-based Image Stylization

**Authors:** Amir Semmo

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08704v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08704v1)

**Summary:** Image stylization with latent-diffusion models entangles two independently refined axes: what a region depicts and how it is depicted. Such pipelines expose only global controls, yet professional retouching demands deliberate, region-specific control. We lift two conditioning weights already present in a ControlNet + IP-Adapter stylization pipeline from global scalars to per-location spatial maps, yielding local, per-axis control of content and style in a single generative pass. Because the two ...

---

### 14. RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins

**Authors:** Dicong Qiu, Zhiyuan Xu, Yaosheng Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08684v1)

**Summary:** Modern video models can generate realistic videos from real appearance references and proxy renders that specify scene structure, viewpoint changes, and motion. Evaluating this render-to-real capability requires a real target video depicting the same scene evolution, paired with an editable, geometrically registered 3D replica. Such data has traditionally required substantial manual modeling, calibration, and animation effort. We introduce RenderBench, a benchmark of 12 reconstructed real-world ...

---

### 15. EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding

**Authors:** Yuhao Qin, Junbo Wang, Yuke Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08674v1)

**Summary:** Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal dependencies across events. Although retrieval-augmented approaches have been introduced to provide additional context, most of them operate at the frame or snippet level, which limits their ability to model how events evolve over time and relate to each other. In this paper, we propose Event Chain Retrie...

---

### 16. PDB: Point-Based Deformation Blending for Facial Animation Retargeting

**Authors:** Sihun Cha, Hyeonseung Shin, Suah Yu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08672v1)

**Summary:** Mesh-agnostic facial animation retargeting transfers expressions across meshes with different structures, but preserving facial motion without surface artifacts remains challenging. To address this, we present PDB, Point-Based Deformation Blending for facial animation retargeting. PDB predicts a compact set of deformed control points from a source neutral-expression pair and blending weights from the target neutral mesh. The weights are computed once per target and reused across frames, while th...

---

### 17. Knowing When to Trust a Prior: Reliability-Gated Cue Fusion for Video Gaze Prediction

**Authors:** Lichen Zhu, Yueqian Lin, Yiheng Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08663v1)

**Summary:** Video gaze prediction is led by gaze-trained models, yet gaze-free priors carry signal those models have not absorbed, if one knows when to trust them. We propose FocusGate, a gated ensemble of gaze-free priors whose members may abstain. A per-frame gate reads three shape statistics of a defocus map and selects the frames on which the estimator is above chance on average, so rejected frames reduce to the base exactly, while midrank normalisation lets an all-zero prior abstain at zero parameters....

---

### 18. Selective Transfer of RL Updates for Visual Reasoning

**Authors:** Suxin Ji, Hungtao Wan, Mingjun Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08659v1)

**Summary:** Model merging provides a training-free way to transfer reasoning capabilities from language models to vision-language models (VLMs), but endpoint-based transfer can conflate pre-existing model differences with changes acquired during reasoning post-training. We instead formulate capability transfer around the training-stage update, isolating the parameter changes induced by reinforcement learning (RL). Yet transferring this update in full remains suboptimal: we find that its components differ su...

---

### 19. Stable Scores, Unstable Answers: Frame Phase and Option Order in Video Multiple-Choice Evaluation

**Authors:** Lichen Zhu, Yiheng Wang, Yueqian Lin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08649v1)

**Summary:** Video-language models are ranked by multiple-choice accuracy on frames from a uniform grid. The grid has two parameters, a rate and a phase, and benchmarks report only the rate. The phase moves answers: two deployed samplers differing only by a half-step phase offset answer 23.6% of questions differently while scoring within a point, and across four releases from two families shifting only the phase changes roughly one answer in five after controlling option order. PHASEFUSION decodes three offs...

---

### 20. Forensic Reserve: Eliciting Latent Knowledge for Image Forgery Detection

**Authors:** Jiahua Li, Zixu John, Tom Zhong, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08639v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08639v1)

**Summary:** As generated images become increasingly realistic, reliable forgery detection is essential for maintaining trust in visual information. However, existing methods primarily rely on task-specific supervision to adapt vision foundation model representations, without fully exploiting internal forensic knowledge to guide detection. To address this limitation, we propose Reserve-Guided Elicitation (RGE), a framework that treats sparse, origin-sensitive internal components in pretrained models as a for...

---

### 21. LiDAR Resolution Recovery via Foundation-Model-Guided Diffusion

**Authors:** Samed Doğan, Nico Leuze, Alfred Schöttl

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08620v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08620v1)

**Summary:** High-beam-count LiDAR sensors are costly, yet many perception pipelines require dense angular sampling. Using a pretrained Stable Diffusion model as the backbone, we fine-tune a LiDAR-conditioned depth model with pseudo-depth targets from a 2D foundation model. During training, the LiDAR conditioning is randomly decimated at different beam budgets. We then investigate how much of a LiDAR scan can be recovered from heavily decimated input and characterize performance across the input beam budget....

---

### 22. FedDermaSeg: Federated Learning for Dermatological Image Segmentation

**Authors:** Anabik Pal, Ganesh Patidar, Bikash Santra

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08574v1)

**Summary:** Skin cancer is a major global health concern, and early detection and accurate lesion delineation are important for effective diagnosis and treatment planning. Automated skin lesion analysis can assist dermatologists, with lesion segmentation serving as a fundamental step in computer-aided diagnostic systems. Conventional deep learning-based segmentation models typically rely on centralized training, where images and their corresponding segmentation masks are collected on a central server. Such ...

---

### 23. Sparse2comm: Towards Robust Cooperative 3D Object Detection

**Authors:** Lei Yang, Boqi Li, Chunmian Lin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08573v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08573v1)

**Summary:** Cooperative perception improves autonomous driving by sharing complementary observations among vehicles and roadside infrastructure for 3D object detection. However, practical deployment is constrained by limited bandwidth and unreliable cooperation, where packet loss, transmission delay, and spatial misalignment jointly degrade the cooperative feature stream. Existing methods often reduce communication cost or compensate for one degradation type, leaving coupled disturbances insufficiently addr...

---

### 24. Less Is More: A Leakage-Controlled Study of Dermoscopic Preprocessing for Joint Skin Lesion Classification and Segmentation with YOLO26

**Authors:** Truong Viet Vu, Nguyen Chi Hai, Nguyen Phuc Nguyen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08570v1)

**Summary:** Handcrafted preprocessing is widely employed in automated dermoscopic analysis to suppress imaging artifacts and enhance lesion visibility. Nevertheless, its actual contribution to modern real-time models remains unclear, particularly when evaluation protocols do not adequately control correlations among images of the same lesion. This study presents a leakage-controlled, lesion-disjoint evaluation of dermoscopic preprocessing and augmentation for joint multi-class lesion classification and inst...

---

### 25. Have I Seen Enough? Frozen Video-Language Models Encode Evidence Readiness

**Authors:** Dan Ben-Ami, Kobi Cohen, Chaim Baskin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08560v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08560v1)

**Summary:** Streaming video-language models must decide not only what to answer, but whether the evidence needed for the current question has arrived. Existing systems learn that decision as a separate trigger; we ask whether an unmodified model already computes it. We show that frozen VideoLLMs carry a linearly readable evidence-readiness signal, labelled from timestamped evidence rather than from model output. It decodes in all seven models of a shared byte-identical evaluation (AUROC 0.733-0.905 under th...

---

### 26. RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models

**Authors:** Dongchen Si, Di Wang, Mingzhen Xu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08539v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08539v1)

**Summary:** Remote sensing scene classification is a fundamental task in Earth observation and geospatial analysis. Existing approaches mainly follow three paradigms: task-specific visual classification, vision-language similarity matching, and autoregressive multimodal generation. However, visual classifiers rely on predefined label spaces, CLIP-based methods perform recognition through static image-text alignment, and multimodal large language models (MLLMs) introduce unnecessary token-level generation fo...

---

### 27. Beyond Perturbation Magnitude: Direction-Dependent Responses in Multimodal Geometric Representations

**Authors:** Yongsheng Luo, Wengan He, Yu Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08533v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08533v1)

**Summary:** Geometric alignment scores based on Gram determinants provide a compact way to model higher-order consistency among modalities, yet how such scores respond to modality degradation is poorly understood. This paper asks whether the response of a multimodal geometric score is determined primarily by the magnitude of the perturbation-induced displacement. Using frozen cohorts from MSR-VTT (N=878) and DiDeMo (N=980), we apply controlled video blur and audio noise and analyze the response in the relat...

---

### 28. MedCORE: Criteria-Grounded Clinical Reasoning for Interpretable Medical Image Diagnosis

**Authors:** Asim Khan, Samee Ullah Khan, Dwarikanath Mahapatra

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08528v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08528v1)

**Summary:** Clinical diagnosis is inherently a structured reasoning process, yet existing deep learning models often bypass this structure by mapping image features directly to disease labels without explicitly interrogating the morphological and textural criteria that clinicians systematically evaluate. This limits diagnostic transparency and may compromise safe clinical deployment. We present MedCORE (Medical Criteria-Oriented Reasoning and Evidence), a structured diagnostic framework that operationalizes...

---

### 29. WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses

**Authors:** Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08526v1)

**Summary:** Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and data...

---

### 30. 2D Spatial Reasoning with Adaptive Neural Cellular Automata

**Authors:** Martin Spitznagel, Janis Keuper

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08518v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08518v1)

**Summary:** Many modern learning approaches are still struggling with spatial reasoning tasks, i.e. they lack the ability to utilize geometric information of perceived entities and their spatial relation to each other to solve problems. We introduce a novel Adaptive Neural Cellular Automata (aNCA) architecture which uses deformable convolutions to dynamically adapt the perceptive field and iteratively reason over 2D spatial relations on grid-like data structures (e.g. images). Empirical results on public be...

---

### 31. Knee3DVLM: Dual-Sequence Full-Volume Vision-Language Modeling for Comprehensive Knee MRI Assessment

**Authors:** Maryam Baizhigitova, Andrew Seohwan Yu, Po-Hao Chen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08482v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08482v1)

**Summary:** Vision-language models (VLMs) are increasingly being applied to three-dimensional medical imaging, but their application to knee MRI remains limited, particularly for interpreting the complementary sequences used in clinical practice. We introduce Knee3DVLM, a sequence-aware VLM that uses full-volume DESS and fluid-sensitive TSE MRI to predict 57 anatomically resolved binary diagnostic targets derived from the MRI Osteoarthritis Knee Score (MOAKS) for structured reporting. We evaluated DESS-only...

---

### 32. HuC-VideoMAE: Human-Centric Video Masked Autoencoding from synthetic data

**Authors:** Ricardo Pizarro, Roberto Valle, José M. Buenaposada, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08433v1)

**Summary:** Modern action recognition models rely on video transformers pretrained on massive collections of web-crawled videos, such as Kinetics-700. However, the use of such data raises ethical concerns, as subjects' consent is typically not obtained. Recent high-quality synthetic video datasets generated from motion-capture data, such as BEDLAM2.0, offer a promising ethical alternative. In this work, we investigate self-supervised pretraining of video transformers on synthetic human-motion datasets. We f...

---

### 33. Deformable CT-US Registration via Anatomy-Aware Implicit Neural Representations

**Authors:** Agnieszka Lach, Magdalena Wysocki, Feng Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08419v1)

**Summary:** Slice-to-volume registration between ultrasound (US) and preoperative computed tomography (CT) imaging would enhance many minimally invasive interventions, for example by locating soft tissue structures intra-operatively that are discernible in CT. While optical tracking enables initial rigid registration, contact from the probe induces soft tissue deformations that inhibit accurate alignment. In this work, we introduce a deformable CT-ultrasound registration framework that incorporates anatomic...

---

### 34. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 35. Ariadne's Thread of LipSync: Unraveling Forgeries via Inconsistency between Lip Motions and Head Poses

**Authors:** Tianyi She, Jiawei Liu, Weifeng Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08417v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08417v1)

**Summary:** Recent advances in LipSync generation technology have led to the creation of highly realistic videos, posing severe societal risks. However, existing defense strategies struggle against LipSync forgeries, as advanced LipSync generation methods not only achieve better lip synchronization but also eliminate visual artifacts. An important reason is that they overlook an inherent biological coupling between lip movements and head poses in natural speech videos. In this paper, we propose LipDA, a nov...

---

### 36. Image Bitstream Fine-grained Understanding for Privacy-Friendly AIoT

**Authors:** Zhen Yu, Wenyang Liu, Kejun Wu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08414v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08414v1)

**Summary:** Image Bitstream Fine-grained Understanding (IBFU) aims to directly perform fine-grained classification and semantic description generation from encoded image byte sequences. In contrast to conventional pixel-domain visual understanding, IBFU conducts semantic analysis without fully decoding images into the pixel domain. Since pixel-level visual content is not explicitly reconstructed during inference, this paradigm reduces visual exposure within the processing pipeline and suits privacy-friendly...

---

### 37. Decoy and disclosure radii of invariant shape descriptors

**Authors:** Tanush Shaska, Lubjana Beshaj

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08410v1)

**Summary:** A recognizer that compares rotation-invariant descriptors sees a surface only up to the fiber of the descriptor. We measure this fiber by its radius in the orbit distance from the enrolled surface. A large radius admits decoys, that is, distant shapes that pass the matcher. A small radius discloses the enrolled shape to anyone who captures the stored value. For star-shaped surfaces truncated to spherical harmonics of degree at most $L$, with $n$ coefficients, a descriptor of generic rank $r$ has...

---

### 38. GeoPID: Decomposing and Steering Visual Information in Vision-Language Models

**Authors:** Seulgi Kim, Zhixiong Zhang, Xinwei Zhang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08401v1)

**Summary:** While recent vision-language models (VLMs) have shown outstanding performance across diverse applications, they tend to under-use visual information and over-rely on textual context. In this work, we propose \textsc{GeoPID}, a training-free framework that analyzes multimodal information within VLMs from a geometric perspective. \textsc{GeoPID} decomposes information into Redundant, Modality-Unique, and Synergistic components through the geometric relationships between visual and textual represen...

---

### 39. UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation

**Authors:** Taojie Zhu, Jing Jin, Yuan Xia, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08398v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08398v1)

**Summary:** On-policy distillation from multiple teachers combines expertise from different domains in a single student, but conflicting gradients can hinder this integration. Gradient corrections directly constrain parameter updates under plain SGD. With optimizers such as AdamW, however, momentum, adaptive scaling, and weight decay can turn a corrected gradient into an update that increases a domain loss to first order. To address this gap, we propose Update Projection for Multi-Teacher On-Policy Distilla...

---

### 40. UniCounting: Instance-Aware Proposal Consolidation for Image-Query-Free Multi-Category Counting

**Authors:** Jinshi Liu, Pan Liu, Lei He, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08379v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08379v1)

**Summary:** Visual counting is commonly formulated as counting a single specified target, with a model receiving an image-specific exemplar, text query, or target category and returning a single count. We instead study fixed-vocabulary image-query-free multi-category counting. A global vocabulary is fixed for each run, and, given only an RGB image, the model predicts a complete category--count vector without being told which categories appear. We present UniCounting, which casts counting as instance-aware s...

---

### 41. A Stevens's Power Law Check-up of GPT-5.5's Image-Based Visualization Reading

**Authors:** Kaichun Yang, Jian Chen

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08365v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08365v1)

**Summary:** We adapt Stevens's power law to measure the innate ability of AI models to read visualizations, which can reveal the built-in perceptual mechanisms of algorithmic models. In our pilot study, models see no legend. A model first views a reference visual representation and estimates its magnitude, then estimates the magnitude of each subsequent image of the same representation relative to that reference. Our evaluation of twelve visual variables makes how algorithmic models read visual encodings me...

---

### 42. Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration

**Authors:** Hyeongheon Cha, Young D. Kwon, Sung-Ju Lee

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08358v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08358v1)

**Summary:** Post-training quantization is a standard route to fitting vision transformers (ViTs) into edge compute and memory budgets, yet quantized models become especially brittle under distribution shift. Test-time adaptation (TTA) addresses such shifts without labels, but most existing approaches are poorly aligned with the constraints of quantized inference. Prevailing TTA methods recover accuracy through backpropagation, while backprop-free methods often still incur overhead from extra forward passes ...

---

### 43. PolarScale: A Physics-Grounded Benchmark for Radiometrically Consistent RGB-to-Stokes Estimation

**Authors:** Beibei Lin, Tingting Chen, Xin Zhang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08346v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08346v1)

**Summary:** Polarization imaging provides physical cues beyond intensity imaging but typically requires specialized hardware. Recent methods infer polarization from RGB-like inputs, yet predict only normalized Stokes components or relative descriptors, from which the radiometric scale needed for full Stokes reconstruction has been divided out. We introduce PolarScale, a benchmark that makes this scale an explicit prediction and evaluation target. Built on existing trichromatic full-Stokes measurements, Pola...

---

### 44. DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models

**Authors:** Shuo Yang, Changbai Li, Linlin Yang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08341v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08341v1)

**Summary:** Recent training-free pruning approaches for Multimodal Large Language Models (MLLMs) effectively cut computational overhead by exploiting visual redundancy or text-vision attention. However, they frequently suffer from semantic degradation due to their task-agnostic design or unreliable attention estimates. Based on our empirical analysis, we have found that this issue arises because salient tokens in shallow layers persistently suppress emerging semantic ones through numerical inertia, leading ...

---

### 45. Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction

**Authors:** Hojun Lim, Hyeongseok Jeon, Donghyun Kim, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08339v1)

**Summary:** Camera-based 3D perception for autonomous driving relies heavily on large annotated datasets, and deploying such a system to a new target region typically requires data collection and annotation. Generative augmentation has been proposed to reduce this cost, but existing approaches face a fundamental trade-off: label-conditioned methods consume the very annotations they aim to replace, while simulator-conditioned methods offer free annotations but lack visual grounding to specific real environme...

---

### 46. Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box Vision Language Models for Autonomous Driving

**Authors:** Heyam Bin Jahlan Areej Alhothali Abeer Alhothali

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08331v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08331v1)

**Summary:** The rapid integration of Vision Language Models (VLMs) into sensitive systems introduces critical safety vulnerabilities that remain unexplored in exist studies. While adversarial attack robustness has been extensively studied for image-based models, the susceptibility of VLMs to temporally-aware adversarial attacks against video in driving context poses a distinct and under examined threat. In this paper, we introduce novel adversarial attack against video targeting VLM models used for autonomo...

---

### 47. Catastrophic Forgetting in Sequential Thermal Anti-UAV Detection: The Role of Scale-Conditioned Gradient Imbalance

**Authors:** Khac Duc Giang Nguyen, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08315v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08315v1)

**Summary:** Counter-UAV systems based on thermal infrared detection must stay accurate as operational datasets evolve, yet sequential fine-tuning causes catastrophic forgetting of prior tasks, a problem that remains insufficiently characterized in this domain. This continual-learning study measures the stability-plasticity trade-off in YOLOMG, a YOLOv5-based detector run as a single thermal-infrared stream with the motion channel disabled, trained sequentially across three anti-UAV benchmarks of rising scal...

---

### 48. Event Detection in Table Tennis Videos using 2D Keypoints

**Authors:** Rainer Lienhart, Daniel Kienzle, Shin'ichi Satoh, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08286v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08286v1)

**Summary:** This paper addresses the challenge of automatic, frame-accurate event detection in table tennis videos. Current methods for estimating 3d ball trajectories and ball spin typically require that key events, such as ball-racket contacts, have already been identified in advance. This requirement makes it difficult to apply these methods to longer, unedited video recordings. To overcome this limitation, we propose EventNet, a two-stage pipeline to detect key events: (1) 2d keypoints are extracted of ...

---

### 49. Whose Face Is It Anyway? A Multi-Model Audit of Facial Affect Recognition on Children, and Why the Gap Is the Head, Not the Features

**Authors:** Tobias Hallmen, Robin-Nico Kampa, Elisabeth André

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08279v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08279v1)

**Summary:** Facial affect models are trained almost entirely on adults, yet are increasingly applied to children in education, health, and developmental research. We present a controlled, multi-model audit of five AffectNet-pretrained expression models (EmoNet, EmotiEffLib, DDAMFN++, OpenFace 3.0, LibreFace) on children, across four child image datasets, the AffectNet-8 validation set, and two spontaneous child video datasets, through one shared harness. Three findings emerge. First, the child gap is model-...

---

### 50. TSRN-RTVD: Real-Time Video Deblurring System

**Authors:** Nikita Alutis, Danila Evsyukov, Egor Chistov, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08230v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08230v1)

**Summary:** As video capture moves to handheld and edge devices, motion blur from camera shake has become a pervasive degradation that lowers perceptual quality and harms downstream vision tasks. The strongest deblurring networks recover impressive detail, yet they remain computationally heavy and overwhelmingly complex, so their quality comes at a cost that consumer hardware cannot pay in real time. This gap between restoration quality and on-device speed is exactly what makes real-time deblurring difficul...

---

## cs.LG

**50 papers**

### 1. QF3: Fast Flow RL with Filtered Q-Gradients

**Authors:** Chung Min Kim, Brent Yi, David McAllister, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08789v1)

**Summary:** Flow policies have become a standard policy class for learning robot behaviors from demonstrations, but reinforcement learning is still critical for improving pre-trained flow policies or learning them from scratch through interaction. We introduce QF3 (Fast Flow RL with Filtered Q-Gradients), an online off-policy RL algorithm that trains a flow policy with flow matching plus the critic's action gradient, backpropagated through a one-step prediction of the flow's output. To keep updates where th...

---

### 2. Conformal Prediction Sets Quantify Information Gain: A Theoretical Perspective

**Authors:** Kevin Zhang, Stephen Bates

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08785v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08785v1)

**Summary:** Conformal prediction is a popular tool for uncertainty quantification that outputs prediction sets with finite-sample coverage guarantees. While prediction set size is commonly used as a heuristic measure of uncertainty, the information-theoretic basis for this interpretation remains poorly understood. In this work, we provide such a foundation using a decision-theoretic generalization of entropy tailored to set-valued prediction. In particular, we introduce a family of generalized information m...

---

### 3. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08773v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08773v1)

**Summary:** Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a t...

---

### 4. Rapid Fredholm stabilization of the Kuramoto--Sivashinsky equation with unrestricted, spatially-varying anti-diffusion

**Authors:** Luke Bhan, Miroslav Krstic, Yuanyuan Shi

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08764v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08764v1)

**Summary:** We develop the first feedback design for rapid stabilization of the Kuramoto--Sivashinsky equation with a spatially varying anti-diffusion coefficient. For constant coefficients, the single-input Fredholm design of Coron and Lü (2015) excludes a discrete set of values at which repeated unstable eigenvalues cause a loss of controllability. We overcome this obstruction by introducing a second boundary input and assigning the two inputs distinct roles. The key idea, inspired by Heymann's Lemma, is ...

---

### 5. Neural Petri flows for chemical reactions

**Authors:** Jose Eduardo Escrig Molina, Daniel Probst

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08750v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08750v1)

**Summary:** Petri nets have been used to describe chemical processes such as reactions.They map well to chemistry: Places are the bonds between atoms and the free valence of each atom, a token is a unit of bond order, a transition forms or breaks a bond, the conserved quantities are the valence budgets of the atoms, and the enabling rule is the valence rule. These semantics are not guaranteed by learned models of reactions or neural networks that are built on Petri nets that use the net as a scaffold for me...

---

### 6. Linear Bandits under Exact Sliding-Window Constraints

**Authors:** Seyed Mohammad Hadi Hosseini, Yasin Abbasi-Yadkori, Sattar Vakili

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08745v1)

**Summary:** We study linear bandits under exact sliding-window constraints, where every consecutive block of actions must belong to a prescribed feasible set. In the offline setting, where the reward function is known, we show that convexity and cyclic-shift invariance make a stationary solution optimal when $w\mid T$ and within an additive $O(w)$ gap otherwise. In the online setting, we show that geometric structure alone is insufficient for learning, and sublinear regret can be impossible. We introduce a ...

---

### 7. Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation

**Authors:** Wenwen Si, Honghao Wei

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08743v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08743v1)

**Summary:** Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which adapts the retained action set using critic scores and an online threshold. The threshold is updated from binary feedback indicating whether the set contains an action in a proxy target. We prove a deterministic bound on the observed proxy miss rate along adaptive trajectories. To quantify the effe...

---

### 8. On the Computational Tractability of Robust Bandits

**Authors:** Vanessa Kosoy, Vinayak Pathak

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08740v1)

**Summary:** Learning when the environment does not belong to the learner's hypothesis class is typically handled using agnostic learning guarantees. However, for anything beyond supervised learning, agnostic guarantees are difficult to come by. Recently, imprecise bandits (Kosoy, 2025) (later renamed to robust bandits in Appel and Kosoy, 2025) were introduced as another approach to unrealizable learning in the bandits setting and a $Θ(\sqrt{T})$ regret learner was shown for a large class. However, no comput...

---

### 9. Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling

**Authors:** Mathias Ollu, Nikos Komodakis

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08738v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08738v1)

**Summary:** Diffusion Language Models (DLMs) hold the promise of order-agnostic, parallel text generation. Recently, continuous diffusion and flow matching models have seen substantial gains, driven by carefully crafted token representations and diffusion/flow spaces. In this work, we introduce Hierarchical Continuous Diffusion Language Models (H-CDLMs), a simple framework that further improves continuous DLMs with minimal compute and parameter overhead. Drawing on the discrete DLM and continuous image diff...

---

### 10. Optimal and Efficient Online Inverse Optimization

**Authors:** Anupam Gupta, Guru Guruganesh, Honghao Lin, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08735v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08735v1)

**Summary:** In online inverse linear optimization, a learner recommends an action and then observes the choice of an expert who maximizes a fixed, unknown linear objective on $\mathbb{R}^{d}$; the goal is to learn to optimize this objective without observing it. Sakaue recently obtained the optimal regret $O(\sqrt d)$ with a randomized algorithm making $(dT)^{O(d)}$ linear optimizations per round, and asked whether it can be attained in polynomial time. We answer positively: our deterministic algorithm has ...

---

### 11. Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus

**Authors:** Egor Pakhomov, Erik Nijkamp

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08722v1)

**Summary:** Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that p...

---

### 12. When Forgetting is not Catastrophic: On the Mechanics of Spurious Forgetting

**Authors:** Vedant Palit, Florent Draye, Nicolas Zucchet, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08718v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08718v1)

**Summary:** Knowledge that a language model appears to forget during finetuning often remains stored and can be recovered, a phenomenon called spurious forgetting. Finetuning on new facts can even produce forgetting that undoes itself: recall of the old facts collapses, recovers as training continues on new facts alone, and only then erodes for good. We seek to understand when such forgetting is not catastrophic. A minimal associative memory reproduces these dynamics with three ingredients: keys with shared...

---

### 13. Co-Evolving Paths and Flows via Path-Flow Alignment

**Authors:** Zeyu Michael Li, William Xingxu Chen, Xiang Cheng

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08717v1)

**Summary:** We study path-flow alignment as a unified training objective for flow matching. Instead of fixing the interpolation path and learning only the velocity field, we jointly train an endpoint-preserving path network and a flow network using the same alignment loss: the flow learns to match the path velocity, and the path learns to align its velocity to the current flow. Although every fixed learned path defines a valid flow-matching objective, the alignment loss alone is not a reliable criterion for...

---

### 14. Prediction-powered inference for time series across space

**Authors:** Shahzar Rizvi, David Burt, Vishwak Srinivasan, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08715v1)

**Summary:** The following motif is common in spatiotemporal settings: we have a sequence of covariate and label pairs observed for a relatively short, recent time period. We have access to unlabeled covariates over a longer time period. Data is observed over many spatial locations. For instance, crop yield might be observed over a large geographical area for recent years, but weather data (which is informative about crop yield) is available for a much longer period. The goal is to estimate, at each spatial ...

---

### 15. GeneICL: A Tabular Foundation Model for Bulk Transcriptomics

**Authors:** Michael Bohl, Alexander Theus, David Wissel, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08694v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08694v1)

**Summary:** Gene expression is widely measured in biomedicine, yet clinical outcome prediction remains challenging due to high dimensionality, strong feature correlations, and limited labeled data. Large self-supervised transcriptomic foundation models often fail to outperform simple supervised baselines. Tabular foundation models offer an alternative through in-context learning, but are typically pretrained on generic synthetic data rather than transcriptomic structure. We ask whether transcriptomics-aware...

---

### 16. Probabilistic Counterfactual Inference for Discrete Outcomes in Gaussian-Process Causal Models

**Authors:** Juliette Sinnott, Amir-Hossein Karimi, Mohammad Kohandel

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08689v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08689v1)

**Summary:** Counterfactual inference in Gaussian-process structural causal models (GP-SCMs) has been developed primarily for continuous endogenous variables, limiting applicability to causal graphs that contain discrete child nodes with continuous parents. We introduce a unified probabilistic framework for counterfactual inference with heterogeneous variable types by pairing GP predictors with explicit exogenous noise mechanisms. For discrete outcomes, we derive exact conditional noise-abduction procedures ...

---

### 17. A Systematic Study of Small Language Models on Abstract Reasoning Tasks

**Authors:** Nur A Zarin Nishat, Jens Lehmann, Andrei Aioanei, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08680v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08680v1)

**Summary:** Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in small language models on the ARC-TGI benchmark, which organizes abstract grid transformations into controllable task families and supports resampling, spatial shifts, and cross-benchmark transfer. Across more than 1,000 runs, we profile decoder-only, encoder--decoder, and mixture-of-experts model famil...

---

### 18. Secure Speculative Decoding for Large Language Models

**Authors:** Yichi Zhang, Zhiqi Wang, Neil Gong, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08678v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08678v1)

**Summary:** Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target model for acceptance or rejection. Prior studies primarily focused on the efficiency-utility trade-off of speculative decoding, e.g., lossy speculative decoding, leaving its security implications largely unexplored.   In this work, we bridge t...

---

### 19. Variance-Optimal Off-Policy Evaluation with Conjunct Effect Modeling

**Authors:** Nicolò Felicioni, Michael Benigni, Maurizio Ferrari Dacrema, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08677v1)

**Summary:** Off-policy evaluation (OPE) for contextual bandit policies becomes challenging when action-level importance weighting incurs excessive variance. Doubly robust (DR) estimation remains unbiased under common support but retains these high-variance action-level weights. A prior estimator, Off-policy evaluation with Conjunct Effect Model (OffCEM), replaces them with more stable cluster-level weights, at the cost of relying on local correctness of the reward model. In this paper, we show that, under t...

---

### 20. Principled Under Pressure: Post-Training Decides Whether LLMs Act on Their Own Moral Judgment

**Authors:** Orion Reblitz-Richardson

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08670v1)

**Summary:** Language models increasingly act as agents. An agent that says an action is wrong and then takes it anyway is a different failure from one that does not know better, and evaluations of stated values cannot see it. We build a pre-registered panel of 248 scenarios across five kinds of pressure. Each scenario is posed twice to the same model, once as the agent choosing what to do and once in the third person asking which option is right, so the model's own judgment is the reference. Every scenario ...

---

### 21. MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge

**Authors:** Mehmet Emre Akbulut, Johannes Geier, Ulf Schlichtmann

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08669v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08669v1)

**Summary:** On-device learning is necessary when the model encounters user-,sensor-, or environment-specific shifts after deployment. Although parameter-efficient fine-tuning (PEFT) methods, particularly Low-Rank Adaptation (LoRA) variants, enable efficient adaptation at the edge, the limiting resource for Convolutional Neural Network (CNN) adaptation is often not the number of trainable parameters but the activation state that must be retained until the backward pass. This paper introduces Memory-Floor LoR...

---

### 22. Steering Diffusion Models to Rare Events with Sequential Monte Carlo

**Authors:** Aavash Subedi, Tim Reichelt, Christopher Williams, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08652v1)

**Summary:** Diffusion models are increasingly used as surrogates for expensive simulators in weather prediction, molecular dynamics, and materials design. In these models, computing the probability $p_0[E]$ of an event $E$ is difficult, especially when the event of interest is rare. A stable estimate using Monte Carlo becomes computationally intractable, requiring a growing sample size $\propto\!1/p_0[E]$ to compensate for an increasing rarity. In this paper, we present Diffusion Importance Sampling of Rare...

---

### 23. SquidAgent: Parallelize Wisely, Coordinate Efficiently

**Authors:** Yexiong Lin, Shanshan Ye, Yu Yao, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08647v1)

**Summary:** LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orch...

---

### 24. Feature Information Dynamics in Diffusion

**Authors:** Jia-Shu Pan, Tao Zhang, Yufei Huang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08626v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08626v1)

**Summary:** Diffusion models generate data through a continuum of denoising problems, and are widely observed to reveal coarse structure before fine detail. Yet, this intuition is mostly empirical and qualitative. We introduce feature information dynamics, an information-theoretic framework for localizing when a feature is generated during diffusion. Using the I-MMSE identity, we connect the rate of feature mutual information change to a gap between optimal unconditional and feature-conditional denoising lo...

---

### 25. Early Memory Selection for Balanced Adam

**Authors:** Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08624v1)

**Summary:** We propose a method for choosing the shared memory parameter $β_1=β_2=β$ in Adam from a short pilot training. The selected $β$ remains fixed during the subsequent full training. A local model of Adam's normalized direction balances sampling variability against the delay introduced by averaging past gradients. This balance gives a cubic memory rule, whose two coefficients are estimated from gradient probes at a few pilot checkpoints. The estimator uses the numerator and denominator jointly, prese...

---

### 26. Multi-Label Perceptual Bug Detection in Video Games using Deep Learning on Gameplay Footage

**Authors:** Nahian Rifaat, Felix Morosov, Loutfouz Zaman

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08593v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08593v1)

**Summary:** Traditional approaches for automated bug detection in video games, such as manual testing, can be beneficial for the improvement of quality assurance, but they can be expensive and time-consuming. The scarce number of tools available to detect multiple perceptual bugs in the same video frame introduces detection challenges for automated bug detection tools in real-world scenarios. We propose a deep learning model for multi-label perceptual bug detection and compare it against video classificatio...

---

### 27. CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution

**Authors:** Marcel Crasmaru

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08592v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08592v1)

**Summary:** CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives. It takes a physics-native stance: a network is a cascade of complex -- and often unitary (the DFT) -- operations acting on an amplitude vector, and classification is a Born-rule measurement $p_k = |z_k|^2 / \|z\|^2$ rather than a softmax over real logits. Every layer ships a CP...

---

### 28. Random Feature Gaussian Process Attention: Linear-Time Probabilistic Attention with Calibrated Uncertainty

**Authors:** Amir Mohammad Mahfoozi, Zi Yang, Ying Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08578v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08578v1)

**Summary:** Transformers provide a state-of-the-art modeling framework, yet poor calibration limits their reliability in safety-critical applications. A promising direction addresses this issue by interpreting attention as a Gaussian process (GP) posterior, which enables principled uncertainty calibration but incurs cubic complexity in sequence length due to the inversion of the kernel; although decoupled GP variants reduced the cost to quadratic, the computation remains prohibitive in practice. In this pap...

---

### 29. How Learning Governs Unlearning across the Memorization-Generalization Spectrum

**Authors:** Hwiyeong Lee, Hyelim Lim, Ingyu Bang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08577v1)

**Summary:** While unlearning seeks to negate undesired capabilities acquired through learning, little research has examined how the way models learn shapes their subsequent unlearning. In this paper, we investigate this connection from the perspectives of memorization and generalization, the two most representative yet competing strategies that models employ during training. We first classify memorization- and generalization-heavy models using grokking in modular addition and compare their responses to unle...

---

### 30. FedDermaSeg: Federated Learning for Dermatological Image Segmentation

**Authors:** Anabik Pal, Ganesh Patidar, Bikash Santra

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08574v1)

**Summary:** Skin cancer is a major global health concern, and early detection and accurate lesion delineation are important for effective diagnosis and treatment planning. Automated skin lesion analysis can assist dermatologists, with lesion segmentation serving as a fundamental step in computer-aided diagnostic systems. Conventional deep learning-based segmentation models typically rely on centralized training, where images and their corresponding segmentation masks are collected on a central server. Such ...

---

### 31. RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems

**Authors:** Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08571v1)

**Summary:** Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train, validation, and protected-test splits. Using a leakage-aware construction pipeline and strict evaluation protocol, we compare keyword-based, semantic-reference, TF-IDF, and transformer-based detectors. DistilBERT achieves the best protected-tes...

---

### 32. Less Is More: A Leakage-Controlled Study of Dermoscopic Preprocessing for Joint Skin Lesion Classification and Segmentation with YOLO26

**Authors:** Truong Viet Vu, Nguyen Chi Hai, Nguyen Phuc Nguyen, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08570v1)

**Summary:** Handcrafted preprocessing is widely employed in automated dermoscopic analysis to suppress imaging artifacts and enhance lesion visibility. Nevertheless, its actual contribution to modern real-time models remains unclear, particularly when evaluation protocols do not adequately control correlations among images of the same lesion. This study presents a leakage-controlled, lesion-disjoint evaluation of dermoscopic preprocessing and augmentation for joint multi-class lesion classification and inst...

---

### 33. Singular Value Decomposition: A Geometric Rediscovery, Where Proofs Become Algorithms

**Authors:** Paul Agron

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08565v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08565v1)

**Summary:** This article is a geometric rediscovery of the singular value decomposition, with a further claim: the construction it builds is the machinery behind much of machine learning. The same argument that answers an idle question about ellipses is the algorithm behind principal component analysis, kernel methods, and PageRank, and it is not only the results that transfer but the proofs themselves, run as procedures.   The usual introduction states $A = UΣV^T$ and justifies it via the spectral theorem ...

---

### 34. Valid for Free: Homophily-Gated Conformal Prediction for Training-Free Node Classification with Tabular Foundation Models

**Authors:** Nguyen Duy Long, Phung Minh Hien, Nguyen Trong Viet, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08564v1)

**Summary:** Tabular foundation models (TFMs) can classify the nodes of a graph without training on it, by reading node and neighborhood features as table rows next to labeled context rows. Work in this line reports predictive performance, not conformal coverage or prediction-set size. To our knowledge, we give the first reliability study of the setting, with TabICL as the TFM and half of each graph as labeled context. As for any predictor fixed before calibration, a frozen in-context predictor makes split c...

---

### 35. Reinforcement Learning for Hierarchical Reasoning Rewards: Minimax-Optimal Rates with Transformers

**Authors:** Naoki Nishikawa, Taiji Suzuki

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08561v1)

**Summary:** Reinforcement learning (RL) has become a standard tool for post-training language models on reasoning tasks, where the policy is updated by reward feedback while exploring the space of responses. Despite its empirical success, theoretical understanding of RL post-training remains limited, in particular of why on-policy exploration combined with a neural reward model is effective. In this paper, we address this question by modeling the reward as a hierarchical function on the response space: the ...

---

### 36. Have I Seen Enough? Frozen Video-Language Models Encode Evidence Readiness

**Authors:** Dan Ben-Ami, Kobi Cohen, Chaim Baskin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08560v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08560v1)

**Summary:** Streaming video-language models must decide not only what to answer, but whether the evidence needed for the current question has arrived. Existing systems learn that decision as a separate trigger; we ask whether an unmodified model already computes it. We show that frozen VideoLLMs carry a linearly readable evidence-readiness signal, labelled from timestamped evidence rather than from model output. It decodes in all seven models of a shared byte-identical evaluation (AUROC 0.733-0.905 under th...

---

### 37. Latent space bias directions in LLMs capture confidence, not fairness

**Authors:** Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08559v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08559v1)

**Summary:** Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activatio...

---

### 38. Systemization of Knowledge (SoK): Human-Centered AI Safety for Youth

**Authors:** Pratyasha Saha, Yaman Yu, Yang Wang

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08554v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08554v1)

**Summary:** While HCI increasingly examines AI-safety for youth, the literature lacks a comprehensive view of what risks have been identified, how they are addressed, and whether proposed protections work in-practice. We systematically reviewed 100 empirical HCI studies involving children and youth interacting with or exposed to AI across schools, homes, care settings, and public services. Using the YAIR taxonomy for risks and the MIT Mitigation Taxonomy for countermeasures, we map which risks have been ide...

---

### 39. DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory

**Authors:** Yining Li, Dongchen Han, Jie Fu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08553v1)

**Summary:** Sequential test-time training adapts a memory network through successive updates, each computing an inner-loop gradient based on the network's previous state. Intuitively, this state dependence should allow each update to account for what the memory has already learned and better incorporate new information. However, we find that this expected advantage does not consistently materialize in nonlinear memories: a fixed-base parallel TTT baseline outperforms its serial counterpart. Our exploratory ...

---

### 40. AnyBottle: A Recipe to Only Keep the Concepts You Really Need

**Authors:** Wolfgang Stammer, Sukrut Rao, Hevra Petekkaya, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08552v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08552v1)

**Summary:** Concept bottleneck models (CBMs) make predictions inspectable and intervenable by routing them through human-interpretable concepts, but originally required concept annotations. Annotation-free variants remove this requirement, but typically use large concept vocabularies, static at both training and inference, producing bottlenecks larger than any task or prediction needs and harder to inspect. We propose AnyBottle, a single recipe for building compact, task-specific CBMs. AnyBottle assumes onl...

---

### 41. Toward Alignment Scaling Laws: A Framework and First Preregistered Measurements

**Authors:** Jeremy Canale

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08540v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08540v1)

**Summary:** Whether alignment gets easier or harder as models grow is often argued from isolated findings, as if alignment were one property. We treat it as a family of measurable scaling relations: for each risk category r, the alignment burden needed to hold a fixed safety target is modeled as B_r(N)=a_rN^alpha_r, with N a capability proxy; against a budget proportional to N, scaling helps if alpha_r<1, keeps pace if alpha_r~1, and accumulates alignment debt if alpha_r>1. We give three operationalizations...

---

### 42. From Shared Demand Patterns to Local Uncertainty: Probabilistic Load Forecasting by Mixing Compact Adaptations

**Authors:** Haoran Li, Zhe Cheng, Yang Weng

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08538v1)

**Summary:** Probabilistic load forecasting has been widely studied for power-system operation and planning, but customer- and transformer-level forecasting introduces a distinct scalability challenge. At these levels, load uncertainty is strongly affected by customer behavior, weather, and mixed load composition, making it difficult for a single shared model to capture heterogeneous patterns. Using separate probabilistic models can improve local accuracy, but becomes costly to train, store, update, and vali...

---

### 43. FlowCF: Sparse Counterfactual Explanations for Mixed-Type Tabular Data using Flow Matching

**Authors:** Emmanouil Panagiotou, Eirini Ntoutsi

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08537v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08537v1)

**Summary:** In the field of Explainable AI (XAI), counterfactual (CF) explanations interpret a model's decision by suggesting the changes to the input that would lead to a more favourable outcome. To be useful in practice, such an explanation should change few features and change them as little as possible, properties known as sparsity and proximity. We observe that existing methods remain limited in this respect, especially for numerical features, whether they are model-agnostic and amortised, or gradient-...

---

### 44. How Bregman Divergences Shape Shampoo

**Authors:** Bing Liu, Wenjie Zhou, Chengcheng Zhao, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08534v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08534v1)

**Summary:** Understanding the principles behind Shampoo has recently guided the development of more effective neural network optimizers. These methods learn a preconditioner by optimizing the Frobenius or Kullback-Leibler (KL) divergence against the gradient second moment. In this work, we investigate how the choice of divergence shapes preconditioning, which remains unclear and blocks further improvements. To do so, we develop a unified Bregman divergence framework that connects all popular divergences, al...

---

### 45. Beyond Perturbation Magnitude: Direction-Dependent Responses in Multimodal Geometric Representations

**Authors:** Yongsheng Luo, Wengan He, Yu Li, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08533v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08533v1)

**Summary:** Geometric alignment scores based on Gram determinants provide a compact way to model higher-order consistency among modalities, yet how such scores respond to modality degradation is poorly understood. This paper asks whether the response of a multimodal geometric score is determined primarily by the magnitude of the perturbation-induced displacement. Using frozen cohorts from MSR-VTT (N=878) and DiDeMo (N=980), we apply controlled video blur and audio noise and analyze the response in the relat...

---

### 46. PHBA: Prefix-State Hybrid Block Attention

**Authors:** Ruijie Li, Jiaxi Hu, Shiyu Wang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08527v1)

**Summary:** Hybrid architectures combining linear sequence models with softmax attention provide an effective balance between efficient long-context modeling and precise token retrieval. Existing designs such as Native Hybrid Attention (NHA) combine compressed long-term states with sliding-window attention, but their exact attention is restricted to a fixed local window. In this work, we introduce Prefix-State Hybrid Block Attention (PHBA), which replaces local sliding-window attention with top-k block-spar...

---

### 47. X-OPM: Explainable Automatic Digital On-Chip Power Modeling for Enhanced Robustness

**Authors:** Jingbo Jiang, Xizi Chen, Jian Peng, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08502v1)

**Summary:** Proactive power management systems reduce processor dynamic power through runtime power prediction and power-aware scheduling. Accurate, stable and low-overhead digital on-chip power meters (OPMs) are crucial for improving the prediction quality. Recent studies have explored various modeling methods, including using linear models, decision trees, and multi-layer perceptrons (MLPs) to construct OPMs. However, most current approaches train models end-to-end without analyzing the physical interpret...

---

### 48. Information-Dense Synthesis for Molecular Discovery

**Authors:** Kasper K. Jakobsen, Eli N. Weinstein

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08495v1)

**Summary:** Machine learning can accelerate molecular discovery by designing molecules and planning experiments. However, many scientific challenges demand molecules with very rare properties, and in this sparse setting, existing algorithms offer little gain over random guessing. We propose a method to efficiently search large regions of molecular space using algorithmically controlled stochastic synthesis. Rather than design, make and test individual molecules, we design and make complex mixtures, test the...

---

### 49. MetaLearnNCA: Few-Shot Offline Meta-Learning via Interacting Neural Cellular Automata

**Authors:** Etienne Guichard, Stefano Nichele

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08479v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08479v1)

**Summary:** Few-shot meta-learning traditionally formulates task adaptation either as analytical gradient descent through unrolled computational graphs or as metric-based distance comparisons over flattened 1D fea- ture vectors, which either incur costly test-time backpropagation or discard native 2D spatial geometry. In this work, we propose METALEARNNCA, a decentralized framework that achieves few-shot adapta- tion through the dynamical interaction of coupled Neural Cellular Automata (NCAs) without comput...

---

### 50. Learning PDE solution operators with variable initial conditions via Latent Dynamics Networks

**Authors:** Stefano Maria Pizzamiglio, Stefano Pagani, Francesco Regazzoni

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08475v1)

**Summary:** In many-query scenarios, data-driven surrogate models provide an efficient alternative to high-fidelity solvers for simulating physical systems governed by Partial Differential Equations (PDEs). In this context, the Latent Dynamics Network (LDNet) has recently demonstrated remarkable performance in predicting the response of spatio-temporal systems, combining Neural Ordinary Differential Equations with nonlinear dimensionality reduction. However, the original formulation assumes a fixed initial ...

---

## cs.NE

**50 papers**

### 1. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 2. Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design

**Authors:** Marcus Vukojevic, Erik Nielsen, Veronica Lachi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08367v1)

**Summary:** Several discrete design tasks, such as molecular discovery, require diverse collections of useful candidates at low computational cost. High validity alone does not guarantee a useful candidate library: repeatedly generating the same valid structures leaves few distinct alternatives. Training for both feasibility and diversity is challenging because many relevant criteria can only be evaluated after hard decoding. To address this challenge, we propose EGO (Evolutionary Generators with One-step i...

---

### 3. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 4. Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07825v1)

**Summary:** Time series forecasting models are typically compared on pointwise error, which scores a prediction in isolation from the decision it is produced for, and a lower forecast error does not imply a better decision downstream. A parallel debate asks whether modern transformer architectures forecast better than recurrent and other lightweight models. We compare linear, fixed recurrent, transformer, and mixing based architectures against recurrent networks evolved by neuroevolutionary architecture sea...

---

### 5. Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks

**Authors:** Zijie Xu, Bingrui Guo, Yiding Sun, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07808v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07808v1)

**Summary:** Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices. In value-based RL, deep spiking Q-networks (DSQNs) combine such efficiency with action-value estimation for decision making. However, existing DSQNs often require multiple simulation timesteps for competitive performance, increasing computational and energy costs, whereas reducing the timesteps can cause substantial performance degra...

---

### 6. Simplified Swarm Optimization for Surrogate-Assisted Reliability Design of Insulated-Gate Bipolar Transistor Power Modules Using an Open-Source Process Finite-Element Model

**Authors:** Wei-Chang Yeh

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07412v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07412v1)

**Summary:** Process-induced warpage, ceramic stress and solder strain limit the reliability of insulated-gate bipolar transistor (IGBT) modules on direct-bonded copper (DBC) substrates. Surrogate-assisted design studies train regression models on finite-element analysis (FEA) databases, but rarely check the optimized designs against new FEA or report how surrogate error interacts with the optimizer. This paper builds and evaluates an open pipeline: an open-source process finite-element model, surrogates tun...

---

### 7. Synapse Loss Estimation for the BrainScaleS Wafer-scale Neuromorphic System

**Authors:** Bernhard Vogginger, Christian Mayr

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07321v1)

**Summary:** Neuromorphic hardware combines memory (synapses) and computation (neurons) into the same silicon substrate to avoid the von-Neumann bottleneck. This way, neuromorphic computing aims to make computational neuroscience simulations and AI processing faster and more energy-efficient. The common crossbar architecture integrates a synapse matrix (analog, mixed-signal or digital) with a neuron array into a neurosynaptic core, whereas multiple cores are interconnected via a dedicated spike routing netwo...

---

### 8. Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design

**Authors:** Álvaro Díez, Fidel Aznar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06400v1)

**Summary:** Swarm robotics presents a robust and cost-effective paradigm for advanced automation in complex, dynamic environments, such as those encountered in search and rescue or environmental monitoring. A fundamental challenge for this field is the data-driven design of decentralized controllers capable of generating emergent collective behaviors. This paper proposes a novel, AI-driven hybrid methodology for the automatic synthesis of swarm robotic controllers for autonomous visual navigation. This appr...

---

### 9. A Flexible and Generic Approach for Explainable Landscape Analysis and the pyXla Toolbox

**Authors:** Tony Ombaso, Anna S. Bosman, Arnaud Liefooghe, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06359v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06359v1)

**Summary:** Landscape analysis has been successfully applied to understand complex optimisation problems, gain insights into algorithm behaviour, and automate algorithm selection and configuration. Although many landscape analysis techniques have been developed over the last decades, it remains difficult for researchers and practitioners to decide which approaches are appropriate and to implement them in practice. Some tools are available, but these are either restricted to particular problem domains (e.g.,...

---

### 10. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 11. Optimization Geometry of QAOA and Variational Quantum Algorithms

**Authors:** Vojtěch Novák, Ivan Zelinka, Silvie Illésová, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05524v1)

**Summary:** Variational quantum algorithms turn choices of Hamiltonian, ansatz, and parameterization into a classical nonconvex optimization problem. We study how this objective function can be visualized and characterized in ways that help explain optimizer behavior. We distinguish two properties of the objective: the number of local minima encountered along sampled directions and the differences in quality among local-search endpoints. We then ask how a local optimizer, represented by BFGS, compares with ...

---

### 12. AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding

**Authors:** Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05334v1)

**Summary:** Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests t...

---

### 13. MOXIE: Discovering Alternative Explanations for Biomedical Image Classifiers

**Authors:** Abiha Tahsin Chowdhury, Rahul Dubey

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04814v1)

**Summary:** Segment-based explanation methods such as LIME return a single explanation for each prediction, computed from one fixed image segmentation. This hides two important facts: a prediction can be supported by many different sets of image segments, and the segmentation itself shapes which explanations can be found. We introduce MOXIE (Multi-Objective eXplanation Imaging Engine), an evolutionary framework that searches for segment subsets that preserve the classifier's confidence while keeping as litt...

---

### 14. Active-DiNTS: Active Differentiable Network Topology Search

**Authors:** Gean Trindade Pereira, Thierry Urruty, Muriel Visani, et al.

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04787v1)

**Summary:** Neural Architecture Search (NAS) has proved to be a strong alternative to manual network design, but applying it to 3D medical image segmentation is limited by two well-known costs, large annotation budgets and multi-GPU clusters. Thus, this paper introduces Active-DiNTS (Active Differentiable Network Topology Search), an approach that embeds pool-based Active Learning (AL) into a bi-level differentiable topology search to perform architecture discovery and label curation jointly. At each query ...

---

### 15. Robust Optimization of Spring Design under Variable Manufacturing Tolerances

**Authors:** Grzegorz Sroka, Slawomir T. Wierzchon

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04656v1)

**Summary:** A reliable assessment of an optimizer robustness requires tracking controlled changes in parameters to identify sources of algorithmic weakness. Such an approach was applied to the problem of designing tension/compression springs with three continuous variables describing the spring geometry.   Three additional independent binary parameters reflect material variability, manufacturing-related geometric deviations, and an additional safety margin. Without expanding the decision space, these parame...

---

### 16. Chance-Constrained Bi-Objective Evolutionary Optimization for the Open-Pit Mining Operational Planning Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04227v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04227v1)

**Summary:** Open-pit mining operational planning involves allocating limited resources while satisfying production, equipment, and ore-quality requirements. Existing approaches often assume deterministic ore grades or rely on simulation-based evaluation under uncertainty. In this paper, we propose a chance-constrained bi-objective formulation of the open-pit mining operational planning problem under uncertain ore grades. We aim to maximize ore production and minimize fleet cost while satisfying stochastic q...

---

### 17. Adaptive Operator Selection in Bilevel Large Neighborhood Search for Electric Autonomous Dial-a-Ride Problem under Uncertainty

**Authors:** Ishara Hewa Pathiranange, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04219v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04219v1)

**Summary:** The electric autonomous dial-a-ride problem (EADARP) extends the classical dial-a-ride problem by incorporating battery and charging constraints for electric vehicles. In practice, travel-time uncertainty can cause violations of time-window constraints. Large neighborhood search is effective for solving the EADARP, but its performance can depend on the choice of insertion operator during the repair phase. This paper investigates insertion-operator selection within a bilevel large neighborhood se...

---

### 18. AdaEva: Accelerating LLM-Driven Algorithm Design with Adaptive Partial Evaluation

**Authors:** Tai Nguyen, Fei Liu, Phong Le, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03896v1)

**Summary:** Large Language Models (LLMs) are increasingly used for automated algorithm design. However the computational cost of evaluating the generated algorithms can be excessive. We consider the common LLM-driven automated algorithm design (LLM4AD) setting in which a candidate algorithm is evaluated by aggregating its performance over a shared set of training instances. This instance-wise structure raises a natural question: must every candidate be evaluated on the entire instance set before deciding wh...

---

### 19. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 20. Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference

**Authors:** Peng Xue, Wei Fang, Kaiwei Che, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03291v1)

**Summary:** Integer-valued leaky integrate-and-fire (I-LIF) neurons and spike firing approximation (SFA) reduce temporal training cost by representing spike trains as firing counts and normalized firing rates, respectively. However, applying spiking self-attention (SSA) directly to these compressed query, key, and value representations introduces cross-time interactions that are absent during spike-driven inference. We term this operator-level discrepancy Temporal Interaction Mismatch (TIM). We propose Para...

---

### 21. The Investment Acceleration Principle Revisited by means of a Neural Network

**Authors:** Guido Fioretti

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03282v1)

**Summary:** The investment acceleration principle is a heuristic for modelling investment time series out of consumption time series. The model presented herein develops a disaggregated accelerator equation whose coefficients are the weights of a Kohonen neural net that represents firms' decision-making. According to this model, investments take place when managers recognise emerging technological patterns. Furthermore, a technique borrowed from the theory of self-organising systems is used in order to dise...

---

### 22. Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift

**Authors:** Julian Lemmel, Pedro D. Wendel Garcia, Taisuke Kobayashi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03249v1)

**Summary:** Deploying a pretrained controller exposes it to conditions that are absent from its training data. Sensor drift, outright sensor failure and accumulating measurement noise all induce a distribution shift that can collapse an otherwise competent policy; typically at a point in time where no expert is available to supply corrective labels. We present a method that lets a policy recover from such shifts online and without supervision. Our controller is an ensemble of recurrent networks, each of whi...

---

### 23. Evolving Hybrid Quantum-Classical Architectures for Image Classification

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03220v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03220v1)

**Summary:** Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansätze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especiall...

---

### 24. Distribution Matching Evolutionary Algorithms for Rare Event Sampling

**Authors:** Yonatan Gideoni, Yarin Gal

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03833v1)

**Summary:** A novel discovery is one which is both useful and surprising: a generative model's output is a useful discovery if it has a low probability of being generated (it's surprising) and a high reward (it's useful). Global optimization can directly increase the probability of sampling high rewards but typically requires updating model weights. Such gradient based optimization is expensive and bars using capable closed-source models. Instead, modern search methods for discovery sacrifice the global tar...

---

### 25. Aggregate accuracy conceals concentrated temporal vulnerability in a spiking speech classifier

**Authors:** İsmail Can Dikmen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03155v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03155v1)

**Summary:** Aggregate accuracy cannot reveal which utterances are locally vulnerable or how internal activity changes when labels remain stable. We retain every prediction for 725,070 adjacent-bin, one-count changes around 100 validation utterances of a frozen SpikeSCR-based classifier. The canonical native-horizon GPU singleton path reaches 86.0836% validation accuracy. Equal-source expected accuracy under a uniformly chosen neighbor rises from 84.00% to 84.54%, although 13 of 84 initially correct sources ...

---

### 26. Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities

**Authors:** Yanxun Zhang, Yifei Wang, Changze Lv, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03149v1)

**Summary:** Edge intelligence requires models to sense continuously in real time and to keep adapting on-device, all under tight compute, energy, and memory budgets. Although spiking neural networks (SNNs) enable efficient event-driven inference, standard surrogate-gradient backpropagation (BP) serializes updates and blocks ongoing inference. We investigate Bidirectional Spike-Based Distillation (BSD) as an on-device learning principle that lets edge SNNs learn while inferring. BSD couples a stimulus-driven...

---

### 27. Small universal multiset reaction systems

**Authors:** Andrei Paun, Annemarie-Beatrix Messner

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03021v1)

**Summary:** This paper presents a construction of a small universal machine within the framework of Multi-set Reaction Systems. We encode the machine state using elements that represent registers and instruction labels, and we enforce sequential execution by ensuring that reaction chains for a given instruction can only activate after the corresponding label element appears. We implement a universal register machine with 8 registers and 23 instructions, showing that the priority-based model requires 87 dist...

---

### 28. Temporal Geometry of Deep Networks: Hyperbolic Representations of Training Dynamics for Intrinsic Explainability

**Authors:** Ambarish Moharil

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03000v1)

**Summary:** Intrinsic explainability remains a challenging problem, particularly in contexts where multilayer perceptrons (MLPs) require dynamic re-training within an optimization environment. This paper investigates how MLPs and their training dynamics can be represented and studied in non-Euclidean spaces; our representation features the Poincaré model of hyperbolic geometry. We aim to capture the geometric evolution of their weighted topology and self-organization over time. Instead of restricting the an...

---

### 29. Evolutionary Computation for Trustworthy AI: From Attacks and Defenses to Self-Evolving Era

**Authors:** Junhao Dong, Chenkai Wang, Xuanhui Lin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02996v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02996v1)

**Summary:** As Artificial Intelligence (AI) has evolved from task-specific models to foundation models and agents, the scope of trustworthy AI has expanded from model-level robustness to the reliability and safety of broader AI systems. This evolution has also expanded the attack surface from individual models to broader system-level interactions, including tool use, context, and interaction trajectories with dynamic environments. As a result, maintaining reliable and safe behavior under changing or deliber...

---

### 30. Evolutionary Giant Tour for CVRP using NSE and ML Heuristic]{Evolutionary Giant Tour approach for CVRP using Node Shift Encoding and Machine Learning repair heuristic

**Authors:** Souad Abdoune, Menouar Boulif

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.03816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03816v1)

**Summary:** The Capacitated Vehicle Routing Problem (CVRP) remains a central concern in logistics research, as route optimisation under rigid capacity and fleet restrictions directly affects operational performance. Genetic Algorithms are widely used for this problem, yet their effectiveness depends heavily on the choice of solution encoding and on the mechanisms used to preserve feasibility during the search. This paper proposes a sequential framework that separates the evolutionary process from route cons...

---

### 31. SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents

**Authors:** Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02361v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02361v1)

**Summary:** Large language model (LLM)-driven evolutionary search is a powerful paradigm for automated program and algorithm discovery, yet existing systems are largely memoryless: each run explores from scratch, so agents repeatedly rediscover the same improvements and re-encounter the same dead ends. We introduce SEDIMA, a persistent hierarchical insight memory for evolutionary search agents. SEDIMA distills raw traces into natural-language insights, clusters them by semantic similarity using attention-we...

---

### 32. Spiking neural networks for streaming qubit readout

**Authors:** Barry M. Dillon, Aqib Javed, Jim Harkin, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02129v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02129v1)

**Summary:** Fast and accurate qubit-state assignment is essential for feedback, calibration, and error correction in quantum processors. In superconducting platforms, frequency-multiplexed readout makes this task intrinsically multivariate as measured traces can encode crosstalk, qubit-state relaxation events, and other transient nonidealities that are not fully captured by conventional matched filtering. Here, we introduce spiking neural network (SNN) discriminators for superconducting qubit readout. By pr...

---

### 33. TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design

**Authors:** Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01887v1)

**Summary:** Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems ful...

---

### 34. Continual Reinforcement Learning with Neuroevolution

**Authors:** Eleni Nisioti, Andrea Cossu, Kathrin Korte, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01583v2) | 📄 [PDF](https://arxiv.org/pdf/2610.01583v2)

**Summary:** Despite many studies about causes and remedies of plasticity loss in Reinforcement Learning (RL) under continual task changes, no RL method has yet consistently achieved a good balance between adaptation and forgetting. Here we turn to an alternative optimization paradigm, neuroevolution (NE): algorithms that search directly in weight space through mutation and selection over a population of neural networks. Across a wide array of environments and environmental changes, with policies ranging fro...

---

### 35. Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks

**Authors:** Yujia Liu, Peiyu Liu, Yajing Zheng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01558v1)

**Summary:** Spiking Neural Networks (SNNs) have attracted increasing attention due to their impressive temporal dynamics, energy efficiency, and brain-inspired mechanisms. Although SNNs have demonstrated promising performance in image classification tasks, recent studies have shown that they remain vulnerable to adversarial attacks, where imperceptible perturbations are added to input images to mislead model predictions. Existing defense methods mainly focus on training strategies, while the role of input e...

---

### 36. LESS: Lightweight Evolutionary Supernet Search in Minutes

**Authors:** Aviral Gandhi, Jinglue Xu, Jialong Li, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01468v1)

**Summary:** Low-cost NAS must both explore high-performing architectures and identify them reliably, yet reducing evaluation cost often weakens the fidelity of candidate comparisons. Training-free methods reduce evaluation cost by replacing learned task feedback with proxy signals measured at initialization. We introduce LESS (Lightweight Evolutionary Supernet Search), a data-driven method that combines a brief fair hard-path warm-up with discrete search under a single CMA-ES distribution. Each proposal is ...

---

### 37. Inherited Learning in an Artificial Ecology: How Controls and Update Allocation Shape Benefits

**Authors:** Xuening Wu, Lei Li, Shan Yu

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01232v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01232v1)

**Summary:** Learning can improve an individual's behavior, yet a population risks losing that experience whenever individuals die and are replaced. Inheriting learned preferences offers a way to preserve useful behavior across generations, raising a question for artificial populations: when does inheritance improve collective performance, and how can its benefits be measured fairly? The challenge is that inheritance changes not only offspring behavior but also survival, reproduction, and opportunities for f...

---

### 38. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 39. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 40. The Quantum Sphere: A Physically Realizable Optimization Benchmark with Provable Linear Convergence in White- and Black-Box Settings

**Authors:** Ofer M. Shir

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.03788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03788v1)

**Summary:** We revisit an established Quantum Control objective, characterize its exact local metric geometry, and reposition it as a rigorous benchmark for Search and Optimization. The trap-free topology of the landscape, established two decades ago, guarantees unhindered optimal pathways, but global topology alone does not govern convergence speed. Although the so-called Quantum Sphere is defined by the fourth power of the control field, we show that its yield gap admits an exact representation as a nonne...

---

### 41. Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling

**Authors:** Ruoyu Zhao, Jiaqi Wu, Chenyu Zhu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40258v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40258v1)

**Summary:** Spiking neural networks (SNNs) offer low-energy sequence modeling through sparse, event-driven computation. However, interactions among spike encoding, neuronal dynamics, and information propagation complicate architecture design. Existing SNN sequence models often adapt artificial neural network (ANN) architectures designed for real-valued activations, potentially underusing spike-based communication and temporal state updates, motivating automated discovery of native SNN architectures. Most ev...

---

### 42. From DNA Design to DNA Slimming: Auditable Agentic Discovery of a Deletion-Only Designer

**Authors:** Joel Shor

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40143v1)

**Summary:** Compact regulatory DNA can free up space in vector payloads, reduce synthesis and assay burden, and expose which sequence features drive predicted activity. Yet most model-based nucleic-acid designers optimize fixed-length sequences through substitutions; they do not ask which bases of an existing functional element can be removed while retaining predicted activity. We define the task of sequence slimming as selecting an exact-length, order-preserving subsequence while retaining activity. Modele...

---

### 43. Toward Controlling Biology with Language:Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots

**Authors:** Nam H. Le, Douglas Blackiston, Michael Levin, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.02247v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02247v1)

**Summary:** Artificial intelligence increasingly serves as a natural-language interface to complex technical systems, letting people accomplish sophisticated tasks by describing what they want rather than specifying how to do it. Extending this interface to living systems is harder: unlike code or images, a biological intervention has no closed-form linguistic meaning, and the paired language-intervention-outcome data needed to learn such a mapping is expensive to collect, since each example requires its ow...

---

### 44. From Search to Signal: Online Post-Training in Automatic Heuristic Design

**Authors:** Yilun Yuan, Tianyu Zhou, Zhenzhou Tang

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39383v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39383v1)

**Summary:** Large language model (LLM)-based automatic heuristic design (AHD) iteratively proposes and refines heuristics, pairing design rationales with executable code. Task-specific evaluators assess programs; execution outcomes and performance scores guide search. Many AHD systems keep the generator frozen; EvoTune and Co-Evolution of Algorithms and Language Model (CALM) instead update it from evaluated candidates. When such outcomes drive reinforcement learning with verifiable rewards (RLVR), they crea...

---

### 45. An Island-Based Parallel Biased Random-Key Genetic Algorithm for the Three-Dimensional Trailer Loading Problem

**Authors:** A. del Río, L. Díaz, L. C. de Vicente, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39272v1)

**Summary:** The Three-Dimensional Trailer Loading Problem (3D-TLP) involves determining the optimal placement and orientation of heterogeneous items within the confined space of a trailer while maximizing volume utilization and satisfying a wide range of complex logistical and safety constraints. The 3D-TLP is NP-hard, rendering exact optimization approaches computationally impractical for large-scale industrial applications. To address this challenge, we propose an enhanced Biased Random-Key Genetic Algori...

---

### 46. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 47. Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes

**Authors:** Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39239v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39239v1)

**Summary:** How search strategies evolve in finite, depletable landscapes remains a question in foraging theory. We study this problem with an evolutionary simulation in which agents forage on a two-dimensional toroidal lattice containing non-renewable resources distributed uniformly or as Lévy dust. Each agent carries a heritable genome encoding step lengths, velocities, and turning angles, and selection acts on a fitness function combining energetic gain, movement cost, and coverage efficiency. By allowin...

---

### 48. T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning

**Authors:** Liuxian Ma, Jiale Dai, Jiaqi Li, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39109v1)

**Summary:** Parameter-efficient reinforcement learning aims to improve reasoning with a compact trainable interface to a pretrained model. We introduce the Thalamic Router (T-Router), which concentrates adaptation on the reuse of completed computations. A compressed, addressable bank preserves block changes; a depth-recurrent controller conditions their selection and relative-scale writeback. This coupling gives thalamic context-dependent routing a concrete computational form: learn which earlier contributi...

---

### 49. Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

**Authors:** Chen Lu, Ke Xue, Siyuan Xu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38757v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38757v1)

**Summary:** Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce...

---

### 50. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

## q-bio.NC

**50 papers**

### 1. Language-model ratings of depression reflect the rater more than the patient

**Authors:** Baihan Lin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08501v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08501v1)

**Summary:** Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...

---

### 2. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 3. A Time-Resolved Framework for Quantifying Neuronal Network State Transitions

**Authors:** Ilya Auslender, Yasaman Heydari, Asiye Malkoç, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08392v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08392v1)

**Summary:** Electrophysiological recordings provide powerful tools for characterizing the dynamics of neuronal networks. In vitro neuronal cultures offer a controlled setting for investigating network responses to diverse interventions, including pharmacological and optogenetic stimulation. However, conventional analyses often reduce electrophysiological activity to aggregate measures calculated over fixed temporal windows, providing only a static representation of the network state. Here, we introduce a co...

---

### 4. Confidence-Ordering Reversal under Contextual Priors in Neural Decoding

**Authors:** Xinyu Zhang, Sichao Liu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08229v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08229v1)

**Summary:** Contextual priors improve neural-to-language decoding by reshaping candidate scores. However, confidence is read from the same reshaped scores, so the errors a prior leaves behind can become more confident with no change in accuracy to reveal it. We study how a prior shapes confidence in speech retrieval on MEG-MASC and MOUS using local decoding scores, a contextual prior combined by additive shallow fusion, and the fused top-two margin as confidence. Among initially incorrect predictions, we fi...

---

### 5. Neural networks as decision trees: an analytical solution for learning and neural selectivity

**Authors:** Hugo Tissot, Jonas Ranft, Yves Boubenec

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08228v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08228v1)

**Summary:** Nonlinear neural networks develop structured internal representations, yet how their geometry is determined by the tasks being learned remains poorly understood. Here, we develop an analytical framework for piecewise-linear feedforward and recurrent networks that links learning, activation-region structure, and neural selectivity. We show that, at any stationary point of gradient-aligned learning, a nonlinear network decomposes into local linear regressions over its activation regions. Deviation...

---

### 6. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 7. CANDLE: Cortical Null-Space Decomposition for Noninvasive Brain Source Imaging

**Authors:** Shuntaro Suzuki, Yuiga Wada, Komei Sugiura

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07824v1)

**Summary:** Electrophysiological source imaging (ESI) aims to estimate cortical source activity from noninvasive electrophysiological measurements such as electroencephalogram (EEG). However, ESI is fundamentally ill-posed because source activity is substantially higher-dimensional than sensor observations, resulting in non-unique solutions. Recent learning-based approaches address this ambiguity by learning data-driven source priors, yet they often struggle to generalize across subject-specific cortical ge...

---

### 8. Interplay between Excitability and Noise in Analog Spiking Neurons

**Authors:** Léopold Van Brandt, Alon Ascoli, Michele Bonnin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06720v1)

**Summary:** A spiking neuron is a dynamical system exhibiting a limit cycle (a spike) when subject to sufficiently excitatory input. Famous neuroscience experiments by Bryant and Segundo as well as Mainen and Sejnowski revealed that the spike times of some biological neurons are more reliable when subject to time-varying stimuli compared to constant ones. Provided with an industrial physics-based transient noise SPICE simulation framework compatible with foundry transistor compact models, we have demonstrat...

---

### 9. COMPASS 2.0: psychometric representational similarity analysis distinguishes symptom structure from personal signal

**Authors:** Baihan Lin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06615v1)

**Summary:** Language models can score psychiatric questionnaires from speech, but agreement with self-report may reflect the questionnaire rather than the person. We introduce psychometric representational similarity analysis, a framework for comparing the structure of speech-derived scores, self-report, item wording and theory, and implement it alongside person-level construct scoring in COMPASS 2.0. We show how similarly worded items induce covariance without psychological signal. In pre-registered discov...

---

### 10. NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI

**Authors:** Felix Nieto-del-Amor, Jingru Fu, J. -Sebastian Muehlboeck, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06502v1)

**Summary:** Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.   Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 corti...

---

### 11. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 12. CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05913v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05913v1)

**Summary:** Task-fMRI connectomes reveal state-dependent neural reconfigurations, yet conventional methods marginalize these signals by aggregating distinct conditions into static pairwise graphs, thereby obscuring condition-specific multi-ROI organization. We introduce CoHyFuse, a condition-aware ROI-centered hypergraph framework that constructs a task-state-specific incidence matrix from condition-wise functional connectivity (FC)-profile embeddings, allowing the same ROI to form different multi-ROI hyper...

---

### 13. Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05503v1)

**Summary:** Large-scale EEG foundation models have demonstrated promising transferability across neurological disorders, but often require millions of parameters and substantial computational resources. In this paper, we present the Universal Semantic EEG Foundation Model (USE-FM), a lightweight EEG foundation model that learns transferable neural representations through self-supervised signal reconstruction on the Temple University Hospital EEG Corpus (TUEG). After pretraining, the encoder is frozen and ev...

---

### 14. Recurrent network dynamics explain the time course of perceptual grouping in natural scenes

**Authors:** Sami Mollard, Alekh K. Ashok, Lore Goetschalckx, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05419v1)

**Summary:** How the brain groups image elements into coherent objects in natural scenes remains unclear. Existing models for grouping in biological vision rely on simplified stimuli with explicit boundaries and cannot explain human behavior in naturalistic settings. We propose a mechanistic framework in which recurrent interactions propagate enhanced neuronal activity within and between cortical areas. The framework links computational principles, neural circuitry and perceptual psychology. Local boundary s...

---

### 15. Efficiency and robustness partition the solution space for memory in recurrent networks

**Authors:** William Qian, Cengiz Pehlevan

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04697v1)

**Summary:** In computational neuroscience, task-trained recurrent neural networks (RNNs) are commonly used as a testbed for exploring the space of recurrent circuit solutions compatible with a particular function. However, these networks are subject to inductive biases that may be misaligned with those of biological circuits, which operate under various efficiency and robustness constraints. Here, using a minimal stimulus recall task, we systematically characterize how the solution space of recurrent neural...

---

### 16. Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command

**Authors:** Luiz Pessoa, Andrea Gambarotto

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04643v1)

**Summary:** Neuroscience treats the brain as a control hierarchy, with cortical systems governing subcortical mechanisms. We argue that this mistakes a configuration for an architecture. Local asymmetries of influence are real, but control is relational and process-specific; because neural elements constrain one another across concurrent processes, relations can form cycles that resist a stable ranking. Evidence from learned action, cortico-cerebellar and thalamocortical loops, and defensive behavior shows ...

---

### 17. Beyond Completion Time: A Multimodal Approach to Characterizing Eye-Hand Coordination During the Nine-Hole Peg Test in Multiple Sclerosis

**Authors:** Mahya Beheshti, Rajvardhan Gadde, Diana Maloku, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04145v1)

**Summary:** Multiple sclerosis (MS) can impair upper-extremity function through motor, sensory, cognitive, and visual deficits. Although the Nine-Hole Peg Test (9-HPT) is widely used to assess dexterity, completion time alone provides limited insight into the eye-hand coordination underlying performance. We characterized 9-HPT performance in nine people with MS (PwMS) and nine healthy controls using simultaneous eye tracking, markerless hand tracking, and object detection. Each peg cycle was divided into tr...

---

### 18. Multimodal Physiological Decoding Reveals Individualized Arousal Dynamics in Closed-Loop Neurofeedback

**Authors:** Anirudh Natarajan, Paul Sajda

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04113v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04113v1)

**Summary:** Most arousal-based brain-computer interfaces (BCIs) use EEG to decode cognitive state. But arousal is an autonomic process. We examined if peripheral physiological signals give a better decode of task-related arousal. We used a public dataset from a difficult boundary-avoidance flight task. In this task, participants received EEG-based BCI neurofeedback, sham feedback, or no feedback. We trained a multimodal deep learning decoder on heart rate, heart rate variability (HRV), respiration, electrod...

---

### 19. MEM as an Extension of Recurrent Processing Theory: Toward a Motivational Account of Consciousness

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04057v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04057v1)

**Summary:** Victor Lamme's Recurrent Processing Theory (RPT) proposes that the feedforward sweep (FFS) can extract and categorize visual features unconsciously, while conscious vision emerges through recurrent processing and feedback interactions across representational levels. The Motivated Emotional Mind (MEM) model, developed by Wiesław L. Galus and Janusz A. Starzyk, retains this core principle but embeds it in an embodied architecture integrating multilayer networks, semi-hierarchical semblions, recept...

---

### 20. Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons

**Authors:** XinYe Cheng, Sue Ann Campbell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04025v1)

**Summary:** The Izhikevich model is a computationally efficient neuron model that can exhibit a wide range of firing patterns observed in the brain. However, it is a discontinuous dynamical system, which means the methods for applying weakly coupled oscillator theory developed for continuous dynamical systems cannot be applied. Therefore, the collective behaviour of coupled Izhikevich model has not been fully studied. To our knowledge, we carry out the first computation of the phase model for an Izhikevich ...

---

### 21. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 22. Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role

**Authors:** Hubert Huang, Michelle McCleod, Brendan Ames, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03410v1)

**Summary:** Contrastive representation learning is increasingly used to recover low-dimensional structure from neural recordings, but its output is typically validated by decoding accuracy rather than by the geometry of the manifold it produces. We apply CEBRA to EEG recorded from dyads in conversation, and analyze the resulting embedding, which training constrains to the 2D sphere. Labels describing the dyads, including the absolute difference between partners' autism-quotient scores, decode well above cha...

---

### 23. The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer

**Authors:** Saman Rahbar

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03827v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03827v1)

**Summary:** Researchers often support the claim that a model shares structure with the brain, or across languages, by reporting a similarity score. We ask what such a score reads when the shared structure is absent, or when the tool that measures it does not work. We check two settings, and in both the score is not what it appears. First, a probe trained to tell grammatical from ungrammatical sentences in one language transfers worse to more distant languages, the usual evidence for shared structure. But th...

---

### 24. Response Variability and Stability in Human Reasoning

**Authors:** Clemens Bombach, Rajmadan Lakshmanan, Marco Ragni

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03008v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03008v1)

**Summary:** Understanding how humans reason -- and how reasoning responses vary across tasks and individuals -- remains a core challenge for modeling and explanation in cognitive science. We investigate the stability of response patterns within reasoners and whether variation in these patterns can be used to predict learning effects. We introduce a formal, geometry-based method to quantify distances between individual reasoning patterns and their internal variability, grounded in heuristic theories. The pro...

---

### 25. NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings

**Authors:** Hanrui Lyu, Baiyuan Chen, Tianshu Tan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02864v1)

**Summary:** Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, seman...

---

### 26. A foundation for systematic analysis of transformers and RNNs for tractography

**Authors:** Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01894v1)

**Summary:** Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-...

---

### 27. Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems

**Authors:** Lulu Gong, Yongxu Zhang, Shreya Saxena

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01786v1)

**Summary:** Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-d...

---

### 28. A High-Density EEG Dataset for Stimulus-Driven Auditory Attention

**Authors:** Ruofan Yan, Na Lu, Shu Peng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01303v1)

**Summary:** Stimulus-driven auditory attention determines which sound gains priority when multiple sources compete without an explicit listening goal, yet most computational studies focus either on acoustic salience or on decoding predefined attended targets. This study investigates instruction-free auditory competition using the Stimulus-driven Auditory Attention (SAAD) paradigm and develops a neurophysiologically informed framework that integrates stimulus-derived sound priority with trial-specific EEG ev...

---

### 29. Selection rules for the harmonic spectroscopy of animal decisions

**Authors:** Mohammad Salahshour

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00990v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00990v1)

**Summary:** Spectroscopy reads structure by sending a structured probe into a system and measuring what comes back. Here we apply this principle to animal decision-making. Harmonic Theory casts choice as motion on an angular landscape over heading, whose Fourier components form an animal's decision spectrum. We show that the arrangement of cues enters that landscape as a structure factor, so it factors like a diffraction amplitude, and symmetry imposes selection rules: a p-fold cue array annihilates every h...

---

### 30. One Inference, Four Failure Modes: Formal Models of Why Pain Location Fails

**Authors:** Adam Y. Shavit

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00866v1)

**Summary:** Patient-reported pain location is diagnostically decisive for some presentations and nearly uninformative for others. A companion paper argues this is not one gradient of diagnostic utility but three distinct failures of localization. This paper gives those failures their mathematics and shows they are one object: a single Bayesian generative model failing at different nodes - the likelihood, the model class, and group- or context-dependence in that same likelihood. The count is not in dispute: ...

---

### 31. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 32. MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography

**Authors:** Chetan Gohil, SungJun Cho, Oiwi Parker Jones, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00746v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00746v1)

**Summary:** Magnetoencephalography (MEG) is an imaging technique that offers a non-invasive, millisecond-resolution view of human brain activity. The increasing availability of MEG data presents an opportunity to take advantage of a recent advance in artificial intelligence, namely self-supervised foundation models. Existing foundation models for MEG (and electroencephalography) have been built on a transformer architecture. Here, we introduce MEG-Mamba: a generative foundation model for neural activity (so...

---

### 33. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 34. Synaptic placement reflects shared input in Drosophila descending neurons

**Authors:** Xizhe Zhang

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00690v1)

**Summary:** Network topology describes connections between neurons, whereas synaptic placement specifies how those connections are arranged within individual cells. How these levels of organization correspond remains incompletely understood. Here we show that connectivity between presynaptic neurons is reflected in relative input placement within Drosophila descending neurons (DNs). Across thousands of one-way DN connections in the independently reconstructed MaleCNS and FlyWire brains, inputs from sources ...

---

### 35. Stochastic Dynamics of Large-Scale Motif-Embedded Spiking Neuronal Networks

**Authors:** Gurpreet Jagdev, Richard Bertram, Na Yu

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00616v1)

**Summary:** We examine how local motif structure and global network topology jointly shape spiking dynamics in stochastic neuronal networks. Using networks of Izhikevich neurons with Erdős-Rényi (ER) and scale-free (SF) background connectivity, we compare motif-embedded networks with synapse-count-matched, non-motif controls under noise- and stimulus-driven protocols. Motif embedding increases noise-induced coherence in both topologies and provides a smaller improvement in signal transmission, while SF-base...

---

### 36. Stochastic dynamics and synchronization in motif-based neuronal networks

**Authors:** Gurpreet Jagdev, Yifei Lu, Richard Bertram, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00597v1)

**Summary:** Neuronal networks exhibit complex dynamics shaped by connectivity and stochastic input. Empirical studies show that neuronal networks contain recurring subgraphs, or motifs, but the collective influence of different motif types after embedding in large stochastic networks remains less well understood. We construct a spiking network composed of six representative structural classes and examine how intrinsic noise, coupling strength, inter-motif connectivity, network size, and neuronal heterogenei...

---

### 37. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40359v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40359v1)

**Summary:** We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between...

---

### 38. Disentangling Computation in Multi-Task Neural Networks with the Green's Operator

**Authors:** James Hazelden

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40292v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40292v1)

**Summary:** How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. We instead study the network's global first-order perturbation response. The finite-horizon Green's operator maps perturbations at each source along a trajectory to their downstream state-space responses and therefore directly represents perturbation routing. Simple reductions of this operator provid...

---

### 39. Attraction to hierarchical feature memory explains orientation bias

**Authors:** Kira Michaela Düsterwald, Peter Vincent, Ana Kapros, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40204v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40204v1)

**Summary:** When recalling the orientation of recent stimuli, observers are systematically biased away from the cardinal axes. The prevailing explanation is that this ''anti-cardinal bias'' arises because cardinal orientations are encoded with greater neural resources and therefore less noise, consistent with efficient coding of environmentally common features. Under this account, the bias should occur independently for each stimulus; any serial attraction towards previously seen orientations should be inde...

---

### 40. Belief-Based Maximum Occupancy Principle and Active Inference

**Authors:** Manolis Mylonas, Rubén Moreno Bote

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39342v1)

**Summary:** Intrinsic motivation plays a central role in adaptive and goal-directed behavior by conferring agents reward-independent objectives and biases useful to act in noisy and uncertain environments. Active Inference addresses the problem of acting in a partially observable environment through a principled framework for belief updating and action selection. A key component of Active Inference is the specification of prior preferences, which shapes behavior by encoding desirable future outcomes. An int...

---

### 41. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 42. Association profile conditioning in a set-temporal transformer for cross-session intracortical motor decoding

**Authors:** Xinyuan Zhang, Handong Mo, Pengfei Wen, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39080v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39080v1)

**Summary:** Intracortical motor decoders degrade across sessions because the set of recorded units changes and persisting units can alter how their firing relates to behavior. Most existing methods update network weights on each new session or rely on unlabeled activity, which does not directly reveal such changes. We present APST, an Association Profile-conditioned Set-Temporal transformer that adapts to new sessions with all network weights frozen. From a few labeled calibration trials, APST summarizes ho...

---

### 43. Not all solutions are created equal: An analytical dissociation of functional and representational similarity in deep linear neural networks

**Authors:** Lukas Braun, Erin Grant, Andrew M. Saxe

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38998v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38998v1)

**Summary:** A foundational principle of connectionism is that perception, action, and cognition emerge from parallel computations among simple, interconnected units that generate and rely on neural representations. Accordingly, researchers employ multivariate pattern analysis to decode and compare the neural codes of artificial and biological networks, aiming to uncover their functions. However, there is limited analytical understanding of how a network's representation and function relate, despite this bei...

---

### 44. Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video

**Authors:** Chang-Bae Bang, Hyungjin Chung, Byung-Hoon Kim

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38819v1)

**Summary:** Studying the alignment between the internal representations of vision models and the responses of the visual cortex to the same observed visual stimuli has enabled us to better understand human visual processing. However, studies so far have largely overlooked the fact that the human brain not only processes observed visual stimuli, but also predicts upcoming stimuli based on what has been observed. Accordingly, we hypothesize that internal representations for generating future video frames are ...

---

### 45. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

### 46. TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion

**Authors:** Merkourios Simos, Chengkun Li, Bianca Ziliotto, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38653v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38653v1)

**Summary:** Recent advances in musculoskeletal modeling and reinforcement learning have enabled muscle-actuated agents to reproduce increasingly complex human motions. Yet these capabilities remain largely confined to flat ground, in part because motion datasets rarely include aligned terrain geometry and because retargeting terrain interactions to complex musculoskeletal bodies is challenging. We present TERRA, an end-to-end pipeline for terrain-aware retargeting and control of musculoskeletal locomotion. ...

---

### 47. Autoregressive Frontier Expansion: Growing Trees with Graph Machine Learning

**Authors:** Umer Gupta, Saku Peltonen, Martin Ritzert

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38506v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38506v1)

**Summary:** Tree-like branching structures are common in nature, from botanical trees to neurons, blood vessels and respiratory trees. Their branching shape often reflects function, making structural modelling central to understanding how these systems work. Because acquiring real-world 3D data is often expensive or infeasible, realistic generative models are valuable for simulation and data augmentation. Existing morphology-specific models either constrain how topology is generated or rely on hand-tuned, m...

---

### 48. Does Global Neuronal Workspace Theory Explain Phenomenal Consciousness? The Motivated Emotional Mind Challenge

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38495v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38495v1)

**Summary:** Global Neuronal Workspace Theory (GNWT) is one of the most extensively developed empirical research programmes on access consciousness. By contrast, the Motivated Emotional Mind (MEM) model proposes an embodied, semi-hierarchical associative memory in which representational selection, action, recurrent reconstruction of modality-specific fields, interoception, and valence form a single functional cycle. This article assesses whether MEM mechanisms can reproduce the functions explained by GNWT an...

---

### 49. Embodiment-aware control by inference over the operator: a simulation study

**Authors:** Sara Falcone

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38437v1)

**Summary:** Teleoperation systems are tuned for channel fidelity, while whether the operator experiences the device as part of the body, the Sense of Embodiment (SoE), is measured only afterwards, by questionnaire. Predictive-processing accounts suggest controlling devices to reduce the mismatch between the operator's predictions and the returned feedback, but those predictions are unobservable, and an objective that only penalizes mismatch is minimized by removing feedback. We formulate an embodiment-aware...

---

### 50. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

## stat.ML

**50 papers**

### 1. Prediction-powered inference for time series across space

**Authors:** Shahzar Rizvi, David Burt, Vishwak Srinivasan, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08715v1)

**Summary:** The following motif is common in spatiotemporal settings: we have a sequence of covariate and label pairs observed for a relatively short, recent time period. We have access to unlabeled covariates over a longer time period. Data is observed over many spatial locations. For instance, crop yield might be observed over a large geographical area for recent years, but weather data (which is informative about crop yield) is available for a much longer period. The goal is to estimate, at each spatial ...

---

### 2. Steering Diffusion Models to Rare Events with Sequential Monte Carlo

**Authors:** Aavash Subedi, Tim Reichelt, Christopher Williams, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08652v1)

**Summary:** Diffusion models are increasingly used as surrogates for expensive simulators in weather prediction, molecular dynamics, and materials design. In these models, computing the probability $p_0[E]$ of an event $E$ is difficult, especially when the event of interest is rare. A stable estimate using Monte Carlo becomes computationally intractable, requiring a growing sample size $\propto\!1/p_0[E]$ to compensate for an increasing rarity. In this paper, we present Diffusion Importance Sampling of Rare...

---

### 3. Spectral Recovery of Point Clouds from Noisy Geometric Graphs

**Authors:** Tatiana Brailovskaya, Nicholas A. Cook, Sofia Poinelli

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08634v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08634v1)

**Summary:** We study the problem of recovering low-dimensional latent geometry from a random geometric graph generated by noisy, high-dimensional data. Specifically, we analyze the performance of a spectral embedding algorithm on the Signal+Noise Graph Model, in which vertices are associated to points perturbed by Gaussian noise, and edges are included for pairs whose inner product exceeds a specified alignment threshold. In the high-dimensional regime where the number $n$ of points and the ambient dimensio...

---

### 4. Feature Information Dynamics in Diffusion

**Authors:** Jia-Shu Pan, Tao Zhang, Yufei Huang, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08626v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08626v1)

**Summary:** Diffusion models generate data through a continuum of denoising problems, and are widely observed to reveal coarse structure before fine detail. Yet, this intuition is mostly empirical and qualitative. We introduce feature information dynamics, an information-theoretic framework for localizing when a feature is generated during diffusion. Using the I-MMSE identity, we connect the rate of feature mutual information change to a gap between optimal unconditional and feature-conditional denoising lo...

---

### 5. Early Memory Selection for Balanced Adam

**Authors:** Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08624v1)

**Summary:** We propose a method for choosing the shared memory parameter $β_1=β_2=β$ in Adam from a short pilot training. The selected $β$ remains fixed during the subsequent full training. A local model of Adam's normalized direction balances sampling variability against the delay introduced by averaging past gradients. This balance gives a cubic memory rule, whose two coefficients are estimated from gradient probes at a few pilot checkpoints. The estimator uses the numerator and denominator jointly, prese...

---

### 6. Classifications in modular restricted Boltzmann machines

**Authors:** Elena Agliari, Andrea Lepre, Edoardo Roscani

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08612v1)

**Summary:** We consider a modular associative neural network made of $L$ Hopfield models (HMs), coupled so that intra-module interactions are Hebbian and inter-module interactions are anti-Hebbian; this competitive coupling is known to endow the network with pattern-disentanglement capabilities. The integral representation of this system coincides with an assembly of $L$ restricted Boltzmann machines (RBMs) whose hidden layers are coupled, thereby extending the HM-RBM duality to the modular setting. We then...

---

### 7. When does conformal calibration need censoring weights? Cause-of-failure prediction sets under competing risks

**Authors:** Sunny Yang, Weiyan Zhao

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08602v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08602v1)

**Summary:** Split conformal prediction sets for competing-risks labels at a fixed horizon require calibration labels that right censoring can leave unobserved. Complete-case calibration guarantees coverage for the label-complete subpopulation, but its population coverage can deviate in either direction, even at the true class probabilities. We study how selection changes the score distribution near the population quantile. At the true score in our main simulation family, with independent draws, complete-cas...

---

### 8. Reinforcement Learning for Hierarchical Reasoning Rewards: Minimax-Optimal Rates with Transformers

**Authors:** Naoki Nishikawa, Taiji Suzuki

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08561v1)

**Summary:** Reinforcement learning (RL) has become a standard tool for post-training language models on reasoning tasks, where the policy is updated by reward feedback while exploring the space of responses. Despite its empirical success, theoretical understanding of RL post-training remains limited, in particular of why on-policy exploration combined with a neural reward model is effective. In this paper, we address this question by modeling the reward as a hierarchical function on the response space: the ...

---

### 9. Information-Dense Synthesis for Molecular Discovery

**Authors:** Kasper K. Jakobsen, Eli N. Weinstein

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08495v1)

**Summary:** Machine learning can accelerate molecular discovery by designing molecules and planning experiments. However, many scientific challenges demand molecules with very rare properties, and in this sparse setting, existing algorithms offer little gain over random guessing. We propose a method to efficiently search large regions of molecular space using algorithmically controlled stochastic synthesis. Rather than design, make and test individual molecules, we design and make complex mixtures, test the...

---

### 10. One-Shot Private Confidence Regions via Resampling

**Authors:** Shourya Pandey, Purnamrita Sarkar, Po-Ling Loh, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08460v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08460v1)

**Summary:** We propose a simple framework for constructing differentially private confidence regions \textit{in one shot}, i.e., by adding noise only to the final resampling quantile instead of privatizing the estimator computed on each resample. The cost of privacy of our procedure is only logarithmic in the number of resamples $B$ under with-replacement ($m$-out-of-$n$) sampling and independent of $B$ under without replacement sampling (subsampling), avoiding the $\sqrt{B}$ factor that arises in previous ...

---

### 11. Scalable Regularized Vector Multiplicative Error Models for Positive-valued Financial Time Series

**Authors:** Rohan Hemant Chhatre, Chiranjit Dutta, Nalini Ravishanker, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08443v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08443v1)

**Summary:** The logarithmic multiplicative error model (log-vMEM) has been useful in modeling and forecasting multivariate positive-valued financial time series. The number of parameters grow rapidly with the dimension of the system and the lag order, making estimation computationally demanding in high-dimensional settings. This paper describes regularized estimation via hierarchical lag structures (Nicholson et al., 2020) for log-vMEM models with multivariate gamma error distribution of Tsionas (2004). The...

---

### 12. Symmetry-Aware Feature Learning: A Polynomial Separation for Multi-Index Models

**Authors:** Jivan Waber, Vanessa Piccolo, Yatin Dandi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08420v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08420v1)

**Summary:** We establish a polynomial sample complexity separation between symmetry-aware and symmetry-agnostic feature learning. We study growing-rank multi-index models with high-dimensional Gaussian covariates in $\mathbb{R}^d$ and $r=Θ(d^δ)$ teacher directions forming a cyclic symmetry orbit, where $0<δ<1/2$. We compare three ways of exploiting this structure: architectural weight sharing, data augmentation over the full symmetry group, and learning without access to the symmetry. In particular, we anal...

---

### 13. Network Intervention by Polling Strategic Agents

**Authors:** Chenyu Zhang, Rohit Parasnis, Saurabh Amin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08347v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08347v1)

**Summary:** A planner in a network of strategic agents faces three entangled challenges: the optimum depends on agents' private information, queried agents may misreport to steer the outcome, and exact computation does not scale. We study these challenges in multi-activity network games with heterogeneous private technologies, in which the planner sets non-discriminatory prices. We show that the optimal prices admit a centrality-based decomposition of the welfare kernel: each agent's contribution scales wit...

---

### 14. High-Dimensional Statistical Inference for Sparse Support Vector Machines

**Authors:** Peng Zeng, Hanwen Huang

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08345v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08345v1)

**Summary:** Using a replica-symmetric high-dimensional characterization, we develop an inferential framework for sparse support vector machines when the sample size and number of features grow proportionally. The main challenge is the nonsmooth hinge loss, which prevents direct application of debiasing arguments developed for smooth classification losses. We overcome this difficulty by representing the $L_1$-penalized support vector machine (SVM) as a linear program and identifying the hinge-loss subgradien...

---

### 15. Two-Sample Testing via Generative Processes

**Authors:** Eshant English, Kenji Fukumizu, Taiji Suzuki

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08277v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08277v1)

**Summary:** Deciding whether two samples come from the same distribution is a classical problem in statistics, and generative transport offers a new way to approach it. We build a stochastic interpolant directly between the two samples and observe that, for a symmetric schedule, its law is invariant under the time reflection $t \mapsto 1-t$ whenever the two distributions coincide. We therefore test whether the marginals at times t and 1-t agree by computing their Jensen--Shannon divergence. Both marginals a...

---

### 16. How Many Independent Samples Does a Satellite Image Contain? Generalization Bounds for Spatially Dependent Data

**Authors:** Robin Young

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08227v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08227v1)

**Summary:** Machine learning classifiers for remote sensing imagery are typically evaluated as though every pixel were an independent sample. Spatial autocorrelation violates this assumption, since neighboring pixels carry redundant information which inflates sample sizes. How many independent samples does a satellite image actually contain? For an $n \times n$ image whose spatial correlation persists over a range of $r$ pixels, the effective sample size is $Θ(n^2/r^2)$, not $n^2$. We prove this as a finite...

---

### 17. Anytime-valid simulation-based hypothesis testing

**Authors:** Patrick Forré, Lydia Brenner

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08210v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08210v1)

**Summary:** For a given data distribution $(X_t)_{t \in \mathbb{N}} \sim Q$ i.i.d., we investigate the hypothesis testing problem: $H_0: Q = P_0$ vs. $H_1: Q = P_1$, for two different model probability distributions $P_0$ and $P_1$. In contrast to the standard setting, where analytic densities $p_0$ and $p_1$ are given, here, we consider the density-free setting, where we only have access to i.i.d. simulations $(Z^0_t)_{t \in \mathbb{N}} \sim P_0$ and $(Z^1_t)_{t \in \mathbb{N}} \sim P_1$. For this simulati...

---

### 18. Beyond Marginal Monitoring: Distributed Joint-Distribution Testing for Data Concept Drift in Large Scale E-Commerce Operations

**Authors:** Cagdas Pullu, Mahmut Emir Arslan, Bugra Balkac, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08132v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08132v1)

**Summary:** Concept drift threatens production machine learning, yet the empirical behavior of multivariate two-sample drift detectors at scale remains under-characterized. Existing benchmarks rarely address the hundreds of millions of rows and high-cardinality features typical of industrial-operational datasets. We evaluate five multi-column two-sample tests (marginal, projection-based, and kernel embedding methods) across three complementary environments: the Harvard Dataverse, a validated Failing Loudly ...

---

### 19. ProximalFM: Amortized Proximal Causal Inference under Hidden Confounding

**Authors:** Christophe Muller, Ayub Kharel, Alex Luedtke, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08078v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08078v1)

**Summary:** Standard causal identification methods often assume no unmeasured confounding and can fail when relevant confounders are unobserved. Proximal causal inference instead uses proxy variables to identify effects under hidden confounding. However, nonparametric proximal estimation can be challenging in practice: recovering causal estimands such as the conditional average treatment effect (CATE) requires solving an ill-posed integral equation that is data-hungry, hyperparameter-sensitive, and optimiza...

---

### 20. Detecting a Shift Is Not Enough: Exact Minimax Limits of Linear Representation Repair

**Authors:** Anuar Aimoldin, Yankai Chen, Ayana Mussabayeva, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08069v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08069v1)

**Summary:** A mean shift between two data sources can be easy to detect but hard to remove without substantially changing their representations. We cast its removal as a statistical decision problem: from noisy differences between paired calibration measurements in $\mathbb{R}^d$, learn one linear map, applied to both sources under a hard distortion budget, that leaves as little of the shift as possible on fresh data. We derive the exact finite-sample minimax risk over all such maps, $(d-k) \mathbb{E}[1/(d+...

---

### 21. Spectra: Exact Component Transport for Test-Time Prior Adaptation in Simulation-Based Inference

**Authors:** Xin Zhao, Nico Scherf, Robert Trampel, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08021v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08021v1)

**Summary:** Simulation-based inference (SBI) has become a powerful approach to Bayesian inference in complex scientific models whose likelihoods are difficult or impossible to evaluate. Amortized SBI learns reusable inference models from simulated data, enabling rapid posterior inference for new observations, and modern generative models have made these models increasingly expressive. However, this reuse is limited to the prior distribution chosen during training, whereas scientific analyses often need revi...

---

### 22. Stochastic Gradient Descent Ascent is Suboptimal for Nonconvex-PL Min-Max Games

**Authors:** Junsoo Ha

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07814v1)

**Summary:** How far can stochastic gradient descent ascent (SGDA) go by tuning its timescale ratio and step sizes in nonconvex min-max games? We answer this question for nonconvex-PL (NC-PL) games by establishing the first tight complexity of two-timescale SGDA with a fixed timescale ratio and non-increasing step sizes. For $\ell$-smooth games with an inner $μ$-PL inequality, we prove a complexity lower bound $Ω(κ^2\ell\varepsilon^{-2}+κ^4\ellσ^2\varepsilon^{-4})$, where $κ=\ell/μ$ is the condition number, ...

---

### 23. Adaptive Mean Estimation by In-Context Learning: A Gradient-Flow Analysis

**Authors:** Martin Eppert, Krishna Balasubramanian, Subhro Ghosh, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07804v1)

**Summary:** Prior Fitted Networks (PFNs) such as TabPFN now rival established statistical procedures across prediction and estimation tasks. A natural explanation is that PFNs have the property of statistical adaptivity, that is, they perform nearly as well as a method tailored to the true data-generating model for a heterogeneous set of models, while not being told which model the data comes from. We study how such adaptivity is learned in a controlled location-estimation problem. Each task is an unlabeled...

---

### 24. Extending Pathwise Gradients to Discrete Random Variables via Finite-Order Relaxation

**Authors:** Donghan He, Luhuan Wu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07786v1)

**Summary:** Pathwise gradients are preferred for continuous random variables because they are unbiased, low variance, and work with a single sample. For discrete variables, however, the pathwise identity cannot generally be exact for every differentiable function. We propose a general framework to construct finite-order exact pathwise gradient estimators for a range of common discrete variables such as Poisson. The estimator is the least-norm solution among all solutions that are unbiased for polynomials of...

---

### 25. Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects

**Authors:** Tianxi Li, Jie Ding

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07755v1)

**Summary:** Large language models (LLMs) are increasingly used as judges for automated AI evaluation. A common practice is to randomize prompt sequences and average the resulting scores, but its statistical validity remains unclear. We show that LLM evaluation mechanisms can be approximated by a class of Markov generalized linear mixed models (GLMMs), supported by out-of-sample predictions across three major commercial LLMs. Using a first-order Markov GLMM, we study leaderboard ranking and group comparison....

---

### 26. Adversarially Trained Linear Transformers Are Optimal Robust In-Context Learners for Gaussian Mixtures

**Authors:** Soichiro Kumano

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07754v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07754v1)

**Summary:** Adversarial training is one of the most reliable defenses against adversarial attacks, but its high computational cost must generally be paid anew for each task. Robust foundation models offer a promising alternative: adversarially pretrain a model once and then transfer its robustness to downstream tasks through lightweight adaptation. However, a fundamental question remains open: can robustness acquired during pretraining transfer to unseen tasks without further adversarial training? In this s...

---

### 27. High-dimensional online calibration from harmonic weights

**Authors:** Maxwell Fishelson, Mehryar Mohri

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07740v1)

**Summary:** We study the online calibration of multidimensional forecasts over an arbitrary convex set $Y\subseteq\mathbb{R}^d$ relative to an arbitrary error norm $\|\cdot\|_{L}$. For forecasting $d$ binary outcomes simultaneously ($Y=[0,1]^d$), we give the first algorithm that achieves $\varepsilon$-calibration in a number of rounds that is polynomial in $d$ for every fixed accuracy. It requires $d^{O(1/\varepsilon)}$ rounds, exponentially improving the dimension dependence of previous bounds. For multi-c...

---

### 28. Nash Social Welfare for Multi Armed Bandits: Trajectory-wise Expected and High Probability Regret

**Authors:** Avishek Ghosh

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07737v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07737v1)

**Summary:** We study fair multi-armed bandits under the Nash Social Welfare (NSW) objective, which measures performance via the geometric mean of accumulated rewards. Existing work defines Nash regret as $\mathrm{NR}_T = μ^\star - (\prod_{t=1}^T \mathbb{E}μ_{I_t})^{1/T}$, where $μ_{I_t}$ is the mean reward of the recommended arm $I_t$ and $T$ is the horizon. Since it applies the geometric mean to per-round marginal expectations, it ignores the joint distribution of rewards across rounds, leaving the NSW fai...

---

### 29. Exact Calibration and Sharp Risk Geometry for Volume-Sampled Ridge Regression

**Authors:** Kihun Rhee

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07721v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07721v1)

**Summary:** We study ridge regression from exactly $s$ distinct rows of a fixed design. Responses are fixed, and only the subset is random. The determinant law and selected ridge fit share one positive definite penalty. Established mean identities and exponential-family duality give the unique penalty that matches a prescribed full-data ridge fit in expectation. It exists exactly when $s$ exceeds the target's effective dimension. Our main result concerns centered covariance risk normalized by full-data pena...

---

### 30. Stability of Measure-to-Measure Transformers on Sub-Gaussian Data

**Authors:** Frank Cole, Nicholas H. Nelsen, Takashi Furuya

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07717v1)

**Summary:** Transformers have exhibited impressive empirical success across various domains, but their theoretical foundations remain less developed. This work constitutes a mathematical study of the measure-to-measure operators defined by transformers. We show that transformers map sub-Gaussian inputs to sub-Gaussian outputs; this ensures that taking arbitrary-length compositions of the softmax operator is well-defined. We then show that transformers are Hölder continuous with respect to the 1-Wasserstein ...

---

### 31. Uniform Discrete Diffusion Models are Minimax Optimal for Estimating Distributions with Small Effective Support Size

**Authors:** Dongsun Yoon, Saptarshi Chakraborty

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07655v1)

**Summary:** Discrete diffusion models have emerged as a practically successful framework for generative modeling on discrete product spaces, yet their statistical generalization properties remain poorly understood. Discrete real-world data such as text or biological sequences often concentrate on a small fraction of the astronomically large ambient space because of semantic or physical constraints, but existing bounds fail to capture this distributional structure and instead scale with the size of the ambie...

---

### 32. Asymptotic Analysis of Empirical Risk Minimization on Entry-wise i.i.d. Heavy-Tailed Data

**Authors:** Kaito Takanami, Takashi Takahashi, Yoshiyuki Kabashima

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07637v1)

**Summary:** Many real-world datasets exhibit unusually large values far more frequently than predicted by Gaussian models. Heavy-tailed distributions capture this behavior, yet evaluating learning performance under them remains challenging because rare, large feature entries retain non-vanishing effects even in high dimensions. Even in the canonical setting of empirical risk minimization for linear regression with entry-wise i.i.d. symmetric $α$-stable data, a precise asymptotic characterization of predicti...

---

### 33. Explicit Asymptotic Bounds for Sequential Calibration Beyond $T^{2/3}$

**Authors:** Eric Dai, Maxwell Fishelson

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07623v1)

**Summary:** Probability forecasts are calibrated when predicted probabilities match empirical outcome frequencies: among events assigned a probability $p$, we'd hope that the fraction of positive outcomes is close to $p$. We study the problem of sequential forecasting of binary outcomes. The classical $O(T^{2/3})$ bound on expected cumulative $\ell_1$-calibration error established by Foster and Vohra stood for over two decades until Dagan et al. reduced the exponent $2/3$ by an unspecified constant.   We es...

---

### 34. Vine Copula VAR:From Recursive Margins to Joint Forecast Inference

**Authors:** Hunter Ng, Yubo Tao

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07589v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07589v1)

**Summary:** Joint-event forecasts often combine a dependence estimate based on past forecast errors with newly estimated marginal distributions. When each historical error retains the marginal fit available at its issue date, inference must account for an overlapping sequence of estimation errors. We derive their joint influence with the terminal forecast estimates in a stable Vine Copula VAR with normal innovation margins and a fixed, correctly specified Gaussian or positive Clayton vine. An intercept iden...

---

### 35. Learning a Mixture of GFlowNets

**Authors:** Tiago da Silva, Amauri H. Souza, Salem Lahlou

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07562v1)

**Summary:** Learning an ensemble of GFlowNets to sample from a discrete target distribution has become a common approach for achieving better state space exploration and convergence than that of a monolithic sampler. However, these methods often add a substantial runtime overhead to the base model, and their conceptual connection remains elusive. To address this, we first propose a general-purpose theoretical framework for describing a mixture of GFlowNets, which we specialize into continuously (CI) and dis...

---

### 36. Is $\sqrt{d}$ Separation Necessary for Gradient EM to Learn Gaussian Mixtures in High Dimensions?

**Authors:** Yiran Zhang, Mo Zhou, Weihang Xu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07551v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07551v1)

**Summary:** Learning Gaussian mixture models (GMMs) using the Expectation-Maximization (EM) algorithm and its gradient-based variants is a fundamental problem in machine learning. It is known that randomly initialized (gradient) EM fails to learn multi-component GMMs in the exact-parameterized setting, where the number of components matches that of the ground-truth GMM. Recently, global convergence of gradient EM has been established in the over-parameterized setting, where more components are used, provide...

---

### 37. Two-Sample Testing for Random Graphs without Vertex Correspondence

**Authors:** Soham Dan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07503v1)

**Summary:** Two populations of graphs often have to be compared without any correspondence between their vertices, for instance when networks come from different communities, or when a graph generative model is evaluated against held-out graphs. We study how many graphs such an unaligned two-sample test needs, and which graph statistics can detect which differences. For an Erdős--Rényi null and a planted two-block difference that leaves every expected degree unchanged, we show that $m\asymp t^{-3}$ graphs p...

---

### 38. Does Muon Need Fine-Grained Spectral Shaping?

**Authors:** Meher Chaitanya, Tianyi Zhou, Aristides Gionis

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07497v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07497v1)

**Summary:** Muon combines current and past gradients into matrix momentum. For $M=UΣV^\top$, the idealized polar update $Q=UV^\top$ gives every singular direction the same weight. We refer to this as the flat profile. Several recent optimizers replace this flat profile with fine-grained spectral maps that give each direction its own gain. We ask how much of this spectral detail a Muon update needs. Our spectral diagnostics show that approximately $94$--$97\%$ of measured singular modes lie below an estimate...

---

### 39. The interface of data assimilation and machine learning

**Authors:** Eviatar Bach

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07496v1)

**Summary:** Data assimilation (DA) is the process of combining forecasts from a model with observations in order to optimally estimate the state of a system. This is critical for chaotic systems, such as the atmosphere, since if observations are not continually assimilated the model will quickly lose skill. DA is routinely performed (usually every 6 hours) at operational forecasting centres around the world.   In this article we discuss the interface of machine learning (ML) and DA. This is still an emergin...

---

### 40. Structure, Not Belief: Correlated Thompson Sampling from LLM-Derived Covariance in Combinatorial Semi-Bandits

**Authors:** Vikram Kakaria, Anish Kataria, Anany Kotawala

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07470v1)

**Summary:** Combinatorial Thompson sampling (CTS) draws independent posterior samples for every arm, so its exploration dynamics ignore any relation among arms. We study a minimal change to those dynamics: an LLM is queried once for a partition of the arms, the partition becomes a positive-definite correlation matrix $Σ$ through an RBF kernel on cluster ranks, and the per-round posterior sample is drawn with covariance $Σ$ while the Beta posteriors are updated from real rewards only, so the LLM shapes how t...

---

### 41. Active Feature Acquisition for Cost-Efficient Temporal Prediction with Reduced Participant Burden

**Authors:** Yunni Qu, Bing Cai Kok, Whitney Ringwald, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07452v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07452v1)

**Summary:** Accurate forecasting of pathological outcomes is a central problem in psychology. To do so, psychologists often collect intensive longitudinal data. However, in such studies, the desire to acquire a large number of variables for the sake of accurate prediction is often counteracted by the need to minimize participant burden. Acquiring more variables per occasion can yield better predictions, but having too many acquisitions increase the risk of non-response and attrition. Longitudinal Active Fea...

---

### 42. Bayesian Optimization on Function Spaces via Sparse RKHS Manifolds

**Authors:** Davide Sartor, Meghan E. Huber, Donghyun Kim, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07417v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07417v1)

**Summary:** Bayesian Optimization (BO) has become an established methodology for minimizing black-box functions of a vector input. Often, however, this parameter vector arises from the discretization of an inherently functional relationship. Several recent articles have considered the Functional Bayesian Optimization (FBO) setting, in which the variable to be optimized is not a member of a finite dimensional vector space, but rather an infinite dimensional function space. In this work, we propose $L^0$ Mani...

---

### 43. A perspective note on likelihood approximation and inference for complex simulation models using a chain of aggregated normalizing flows

**Authors:** Getachew K Befekadu

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07391v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07391v1)

**Summary:** We present a new perspective on the problem of likelihood approximation within the framework of simulation-based inference that promotes scalable and controllable simulation routines for large-scale data analysis, allows efficient parameter space exploration or smooth interpolation in high-dimensions and, thus, supports valid statistical treatments of hypothesis testings as well as uncertainty quantification. In particular, we consider a chain of $n$-aggregated normalizing flows for likelihood a...

---

### 44. DeepAJM: Deep Association Joint Model for Irregularly Sampled data

**Authors:** Barsha Halder, Jeffrey A. Thompson

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07388v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07388v1)

**Summary:** Joint Models simultaneously model longitudinal and survival outcomes, leveraging patterns in patients' longitudinal trajectory to improve the prediction of survival outcomes. The classical parametric joint models, however, rely on fixed parametric assumptions, making them susceptible to bias under model misspecification and smaller sample sizes. We propose a deep joint model, DeepAJM, that does not require any parametric assumptions, while retaining a partially interpretable, per-longitudinal-ou...

---

### 45. HyperNSDE: Personalized Neural SDEs for Joint Static-Longitudinal Clinical Data Generation

**Authors:** Perrine Chassat, Agathe Guilloux

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07383v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07383v1)

**Summary:** Synthetic patient data generation is a promising solution to the dual challenge of data scarcity and privacy constraints in healthcare machine learning. Realistic synthesis of patient-level clinical data requires jointly modeling heterogeneous static covariates, irregularly sampled longitudinal trajectories, and informative observation times - three tightly coupled components in practice yet rarely addressed together. We propose HyperNSDE, a continuous-time generative model that conditions a lat...

---

### 46. Redundancy and synergy in multivariate Gaussians via the Blackwell order

**Authors:** Artemy Kolchinsky

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07360v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07360v1)

**Summary:** The goal of the partial information decomposition (PID) is to quantify the redundant and synergistic information that multiple sources provide about a target. PID has many applications in machine learning, neuroscience, and other fields, but defining and computing it for high-dimensional continuous systems remains challenging. Here, we define a PID for multivariate Gaussian systems based on the Blackwell order, which formalizes when one channel is more informative than another. We prove that Gau...

---

### 47. Assumption-lean logistic regression with missing covariates

**Authors:** Jyotishka Ray Choudhury, Kabir Aladin Verchand, Richard J. Samworth, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07292v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07292v1)

**Summary:** Missing covariates are frequently encountered in supervised learning problems, and classical methods for estimation using such data use carefully chosen imputation schemes for missing data, or likelihood approximations that lead to nonconvex $M$-estimation problems. These methods and their relatives are suitable for scenarios in which the covariate distribution is known, and more broadly, have enjoyed tremendous success in linear models. But even in basic nonlinear problems such as logistic regr...

---

### 48. Empirical-Bayes spectral partial pooling across related tasks

**Authors:** Lorenzo Mauri

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07284v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07284v1)

**Summary:** Spectral methods are central to high-dimensional statistics and machine learning, underlying procedures for covariance estimation, matrix denoising, representation learning, clustering, and latent variable modeling. In this work, we focus primarily on spectral estimators for high-dimensional factor models, where leading singular vectors of the data matrix are used to estimate latent structure and covariance parameters. In many modern applications, however, data are collected across related but h...

---

### 49. Conditional Flow Matching for Transport Between Markov Processes

**Authors:** Syamantak Kumar, Dheeraj Nagaraj, Saptarshi Roy, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07229v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07229v1)

**Summary:** Motivated by sequence-to-sequence transport in the context time-series domain adaptation, we study the problem of transportation between trajectories of Markov processes. Given a limited number of trajectories from source distribution and the target distribution, we formulate a flow matching based algorithm which learns a transport map from the source to target trajectory distribution, while preserving the Markov structure. We show that this is consistent in the population limit and derive finit...

---

### 50. How Inefficient Is Natural Gradient Descent? From Exact Optimality to Θ( \sqrt{ \log d } ) Divergence

**Authors:** Guni Sharon, Alan Kuhnle

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07228v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07228v1)

**Summary:** Natural gradient descent (NGD) underlies common methods in ML. For dually flat families, idealized NGD on the forward Kullback--Leibler objective follows the mixture geodesic which is often longer than the shortest Fisher--Rao path. We quantify this overhead by the inefficiency ratio \(R \ge 1\), the Fisher length of the mixture geodesic divided by the Fisher--Rao distance, and bound its supremum over endpoint pairs as a function of the parameter dimension \(d\). A tensor criterion identifies th...

---

