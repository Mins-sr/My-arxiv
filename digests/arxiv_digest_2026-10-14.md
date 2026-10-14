# arXiv Daily Digest - 2026-10-14

Total papers: 350

---

## cs.AI

**50 papers**

### 1. ChunkAct: Action Chunking for Agentic Robotics

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18874v1)

**Summary:** Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once ...

---

### 2. What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18869v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18869v1)

**Summary:** How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Ac...

---

### 3. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18868v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18868v1)

**Summary:** Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce ...

---

### 4. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning

**Authors:** Minghao Luo, Liang Chen

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18862v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18862v1)

**Summary:** Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heuristics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a training-free decoding method in which a much smaller reasoning model steers the large one t...

---

### 5. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards

**Authors:** Xin Gao, Yifan Yang, Xin Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18860v1)

**Summary:** Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and aesthetic quality. Image generators excel at visual design but can misrender requested content, making their outputs unreliable targets for direct reproduction. We therefore introduce AesCode, which gen...

---

### 6. Hybrid Reasoning Agents

**Authors:** Jiaru Zou, Yunzhe Qi, Sirui Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18861v1)

**Summary:** How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturall...

---

### 7. Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards

**Authors:** Yuante Li, Junwei Quan, Kai Qiu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18853v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18853v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in practical multi-step training. We develop a two-clock framework that separates the samples needed to make progress from those consumed before collapse. Under a local quadratic model, the square-root rule p...

---

### 8. MFG: Multi-turn Feedback Guided Molecular Optimization

**Authors:** Trieu Nguyen, Frazier N. Baker, Ruoxi Gao, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18851v1)

**Summary:** Multi-objective molecular optimization is a critical process in drug discovery that aims to modify a given molecule to simultaneously improve multiple properties while maintaining a similar overall structure. This process often requires iterative modifications guided by computational or experimental feedback. Recent large language model (LLM)-based methods have begun to explore this iterative approach; however, these methods are not explicitly trained to leverage such feedback, while existing ap...

---

### 9. LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

**Authors:** Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18843v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18843v1)

**Summary:** Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control ra...

---

### 10. Who Improves the Robot? Toward Physical Recursive Self-Improvement

**Authors:** Hai Zhou, Fan Yang, Zeyi Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18842v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18842v1)

**Summary:** Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improvement procedure, making subsequent improvement more effective across tasks. Physical RSI faces challenges from noisy observations, continuous dynamics, costly trials, and irreversible consequences. We present an L0-L5 fra...

---

### 11. Fast Rates for Offline Q-Learning with KL Regularization

**Authors:** Yize Hao, Guangxin Jiang, Shuang Qiu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18839v1)

**Summary:** This paper investigates offline Q-learning for finite-horizon Markov decision processes with Kullback-Leibler (KL) regularization. Recent studies have shown that KL regularization can yield fast rates in offline decision-making problems. However, it remains unclear whether Q-learning, which adopts incremental stochastic approximation updates, can achieve such fast rates in the offline setting. We first propose KL-regularized Q-Learning (KLQ), a simple variant of classical Q-learning. By exploiti...

---

### 12. RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Uksang Yoo, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18835v1)

**Summary:** It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choices of solver, contact model, and physical parameters explicit and editable, allowing both humans and coding agents to iteratively refine simulations based on observed physical behavior. We implement RSS with the open Newt...

---

### 13. Read the Room Before Your Model Generates

**Authors:** Muyao Kong, Zhihao Lin

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18820v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18820v1)

**Summary:** Large language models (LLMs) generally rely on sampling temperature to regulate the amount of randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed, heuristic global settings and context or token-level calibration, rather than a geometrically interpretable representation of the communicative scenario. In this work, we introduce a simple and interpretable temperature selection framework, the \textbf{Scenario-Actor}, which adapts decoding to the inferred...

---

### 14. Back-Translation Still Matters: Leveraging Monolingual Data for Low-Resource Machine Translation with LLMs

**Authors:** Divyanshu Bathla, Parag Singla, Jitin Singla

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18818v1)

**Summary:** Pre-trained Large Language Model (LLMs) are effective on many tasks in zero-shot and few-shot settings. For machine translation of low-resource languages, the obvious options are few-shot prompting and fine-tuning on a small parallel set. We ask: what if moderate amounts of low-resource monolingual data are also available? We argue that, rather than continued pretraining, a more effective use of this data is the pre-LLM era technique of back-translation (BT). The current fine-tuned LLM translate...

---

### 15. Self-Evolving Agent Harness

**Authors:** Chuyang Wei, Haoxiang Guan, Minghang Zhu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18813v1)

**Summary:** Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates update targets from proposal and admission mechanisms. It distinguishes changes to interpreted state from revisions to tools and code, repository-level control logic, and plugin composition. We characterize search through ev...

---

### 16. Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning

**Authors:** Svar Rajankumar Patel, Kshitij Jerath

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18808v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18808v1)

**Summary:** In cooperative Multi-Agent Reinforcement Learning (MARL), agents must learn to coordinate their actions to achieve shared objectives. A key indicator of effective coordination is behavioral diversity, i.e., the agents' potential to enact distinct yet complementary control policies given the same set of observations. Although behavioral diversity can enable role specialization and richer joint behaviors, its appropriate level is highly context- and task-dependent and often costly to tune. We prop...

---

### 17. SEAR: Self-Evolving Agentic Robotics

**Authors:** Xinyi Wang, Bangzheng Li, Hanyu Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18792v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18792v1)

**Summary:** Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy ...

---

### 18. Bytes to Threats: Byte-Sequence Transformer For Malware Detection

**Authors:** Abdelrahman Yassin Eljamal, Abdeltawab Hendawi

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18787v1)

**Summary:** Existing malware detection approaches heavily rely on handcrafted features derived from static or dynamic analysis of the executable files. These methods require specialized domain expertise, dedicated analysis tools, and time-consuming analysis, which limits their scalability and robustness in the face of the increasing complexity and diversity of modern malware. Consequently, there is a growing interest in approaches that operate directly on raw bytes, which contain rich semantic and structura...

---

### 19. Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity, and Aggregation

**Authors:** Donghwan Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18786v1)

**Summary:** LLM ensemble gains are often measured against a single baseline, but the value attributed to additional candidates can change with the comparison used. We study an LLM aggregator under four matched conditions: Direct (no candidates), Single-slot (one candidate in a multi-slot interface), Duplicate (one candidate repeated), and Multi-candidate (separately generated candidates). Under either non-diverse control, overall candidate gain (CIV) splits algebraically into an additional-candidate contras...

---

### 20. Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents

**Authors:** Yuchen Lu, Julian McAuley, Lei Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18784v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18784v1)

**Summary:** Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history that produced it? In this paper, we introduce CarryOn, an object-oriented context runtime that organizes continuation around reusable task objects. Rather than treating compressed histories or reconstructed accounts of ...

---

### 21. BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems

**Authors:** Xiaoguang Guo, Yaohao Long, Chuxu Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18780v1)

**Summary:** Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent and decisive error step. Recent methods trace dependencies, but knowing where information came from is not the same as knowing where it went wr...

---

### 22. Jeva: System One Models from First Principles

**Authors:** Qi Li, Xinchao Wang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18773v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18773v1)

**Summary:** System one models enable direct, low-latency decision-making. Yet recent practice of predicting an answer from serialized text does not, by itself, respect the structure of a decision problem. We argue that current designs underemphasize four important structural requirements. (i) null-aware: Models should distinguish answer absence from uncertainty among candidates; (ii) permutation-invariant: Reordering alternatives should not change the decision; (iii) option-scalable: Growing candidate sets ...

---

### 23. Beyond the Verdict: Agentic Code Judging with Verifiable Feedback

**Authors:** Zheye Deng, Sha Li, Changlong Yu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18760v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18760v1)

**Summary:** Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In competitive programming, however, official judging systems provide authoritative verdicts under finite submission budgets, without revealing failure explanations or failing inputs. To provide informative feedback without co...

---

### 24. PreciseCoder: Faithful and Generalizable Debugging Beyond Unit-Test Rewards

**Authors:** Yunkai Zhan, Miaosen Chai, Shangshang Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18755v1)

**Summary:** Reinforcement learning (RL) from unit tests is the common recipe for post-training code models, but a unit test only asks whether the final program passes. We analyze what this unit-test-only reward teaches a model during debugging and find that, while it raises pass rates, it also teaches the model to edit more and to hallucinate bugs in code that is already correct. We introduce PreciseCoder, a training algorithm that augments the unit-test reward with a signal for semantically verified, local...

---

### 25. SolBehave: Evaluating the Behavioural Correctness of LLM-Generated Smart Contracts

**Authors:** Giovanni Pio Delvecchio, Stefano Fantazzini, Giacomo Frisoni, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18745v1)

**Summary:** Large language models increasingly generate Solidity smart contracts that, once deployed, can never be patched, making a single latent fault permanent and exploitable. Yet current evaluations mostly ask only whether generated code compiles. We introduce SolBehave, a benchmark for evaluating the correctness of model-generated contracts at scale, moving beyond ad hoc unit tests. Across 250 real, reproducible Ethereum contracts, we apply three complementary tests of behavioural fidelity: differenti...

---

### 26. A Rate Transfer Method: Convergence Rates in Stochastic Gradient Descent via Stochastic Calculus

**Authors:** Neil Walton

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18739v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18739v1)

**Summary:** We develop a rate-transfer method that converts finite-time Lyapunov estimates for an associated stochastic differential equation (SDE) into finite-time convergence bounds for stochastic gradient algorithms. Under generic moment and smoothness conditions, the convergence analysis of the stochastic gradient method reduces to a calculus argument verifying a Lyapunov generator inequality for the SDE. The method recovers established rates for classical stochastic gradient methods and provides a way ...

---

### 27. Steertuning Policies from a Few Human Videos

**Authors:** Billy Yan, Isaac Tu, Kelly Lee, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18711v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18711v1)

**Summary:** Current recipes for robot learning require massive amounts of robot demonstrations to obtain robust and adaptive policies. In this work, we introduce Steertuning, a system that enables robots to learn new tasks in new environments from 5 human demonstrations in under 5   Steertuning consists of two parts. (1) We pretrain a 400M-parameter diffusion policy on our egocentric human dataset, which consists of 100 hours of densely annotated random interactions. This pretraining makes Steertuning robus...

---

### 28. Unlocking Token Rewards via Training-Free Reward Attribution

**Authors:** Sitong Wu, Haoru Tan, Bin Xia, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18704v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18704v1)

**Summary:** In this paper, we propose an extremely efficient, training-free method to extract token-level reward signals directly from an existing deep reward model. Our core idea is to attribute the overall process reward to individual tokens by estimating each token's influence. This influence is defined as the change in the final macroscopic reward (e.g., the process reward) when a token is replaced with a semantically null token. Naively calculating this influence is computationally infeasible, requirin...

---

### 29. UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

**Authors:** Jingbo Xu, Jianjie Fang, Zhuohang Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18697v1)

**Summary:** World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities req...

---

### 30. GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models

**Authors:** Rong Li, Shijie Li, Jiangyong Huang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18694v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18694v1)

**Summary:** Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features. Capturing geometry, however, does not ensure its use: zeroing the aligned latents of a released feature-alignment model leaves its accuracy uncha...

---

### 31. Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning

**Authors:** Tianhao Fu, Austin Wang, Charles Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18690v1)

**Summary:** Image-token compression must reduce computation without hurting the semantics. We introduce Varest, guided by semantic fungibility: tokens within a coherent semantic region can be summarized coarsely, while object boundaries and literal text require finer distinctions. Object and text localizers guide variable-resolution merging, preserving spatial coverage and finer detail at boundaries and text. Learned [REL] registers then prune visual tokens after early decoder processing. Training across bu...

---

### 32. RadarGSOcc: Doppler-Aware 3D Semantic Occupancy Prediction Using 4D Radar Tensor with Geometric-Semantic Feature Extraction

**Authors:** Christofel Rio Goenawan, Dong-Hee Paek, Seung-Hyun Kong

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18686v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18686v1)

**Summary:** 3D semantic occupancy prediction is crucial for autonomous driving, but camera-based methods degrade in low-light conditions and LiDAR-based methods are sensitive to adverse weather. 4D radar is more robust, yet its sparsity and the high cost of radar tensor processing limit its use. We propose Radar Geometric-Semantic Occupancy Prediction (RadarGSOcc), an efficient framework that directly processes 4D radar tensors by separately extracting geometric and semantic features, including Doppler info...

---

### 33. Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents

**Authors:** Jiajun Chen, Xinyue Chen, Yicheng Jiang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18684v1)

**Summary:** Personal-agent memory has largely focused on learning what users know, prefer, and want. However, knowing the user does not necessarily mean knowing what the user and the agent have established together. An assistant's proposal should not become an authorized instruction merely because it is remembered. We introduce Grounding Awareness, the ability to distinguish accepted, unacknowledged, revised, and scoped arrangements when selecting actions. We develop a controlled benchmark to test whether a...

---

### 34. ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning

**Authors:** Bowen Ding, Mingda Wan, Yuhan Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18683v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18683v1)

**Summary:** Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that this uniformity inherently reinforces structurally invalid actions in preferred trajectories and ignores the downstream cascading influence of early pivotal deviations in unpreferred...

---

### 35. Model-Based Online Decision Making via Generative Trajectory Planning

**Authors:** Haldun Balim, Yilun Du, Na Li

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18677v1)

**Summary:** Online decision-making faces a tension between efficient inference and long-horizon reasoning. Value-based methods rely on short-horizon bootstrapping that limits the propagation of long-term information, while trajectory optimization methods plan explicitly but must solve a high-dimensional optimization problem at every decision step. We propose Generative Trajectory Planning (GTP), a model-based framework that addresses this tension by learning a generative model as a proposal distribution ove...

---

### 36. From Relation-Specific Heads to Shared Interventions: Contextual Entrainment in Language Models

**Authors:** Jinghan Zheng, Jiajun Shi

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18674v1)

**Summary:** Large language models rely on prompt context to perform in-context learning, follow formats, and adapt to local evidence. This ability, however, also raises a robustness concern: models may reuse irrelevant tokens from earlier context when answering a later query. Prior work identifies this behavior as contextual entrainment and finds attention heads whose ablation reduces it, arguing that these heads are largely task- or relation-specific. But are the mechanisms behind contextual entrainment tr...

---

### 37. SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation

**Authors:** Ziyang Song, Lia Shen, Yixuan Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18672v1)

**Summary:** Biomedical language models (LMs) provide strong representations for clinical tasks, but they often fail to capture the hierarchical structure among medical concepts. This limitation is especially pronounced for rare and fine-grained clinical codes in long-tailed vocabularies, where hierarchy-agnostic LM representations become less informative as concept frequency decreases. We introduce Semantic Medical Identifier (SMI), a training-free framework for constructing ontology-grounded Semantic IDs a...

---

### 38. Known-Voice Cloning and the Limits of Personality Transfer for Character Design

**Authors:** Johanna Magdalena Kuch, Maud van Lier, Daksitha Senel Withanage Don, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18669v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18669v1)

**Summary:** Recent advances in zero-shot voice cloning systems make it possible to reproduce a recognizable voice from a short recording and attach it to arbitrary virtual characters. Prior work suggests that familiar vocal identity can carry over associated personality impressions to new targets such as robots or virtual characters. However, these works have mainly examined familiarity and personalization effects rather than directly testing whether a cloned familiar voice systematically transfers personal...

---

### 39. Kwai Summary Attention V2 Technical Report

**Authors:**  OneRec Team, Chenglong Chu, Guohong Mu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18654v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18654v1)

**Summary:** Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers with full attention to retain exact access to the original text. In such hybrid KSA-Full architecture, the interleaving inserted summary tokens are served as a streaming flow role across different layers. Although effective, however, it also introduce some bottlenecks: (1) the different layers summary compression chunk must ...

---

### 40. AMemOps: Evaluating Memory Updates in Long Audio Streams

**Authors:** Peiwei Chang, Li Zhang, Mark D. Plumbley, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18652v1)

**Summary:** Audio memory must recognise recurring sources across acoustic changes while keeping their attributes up to date. Overall accuracy does not reveal how these demands interact. We introduce Audio Memory Operations (AMemOps), a benchmark for latest-attribute retrieval, preservation of unchanged attributes and absent-source rejection in long audio streams. Paired controls vary recordings, training identities and earlier events to examine their effects on updating. Training on other recordings of the ...

---

### 41. Tiny Recursive Message Passing

**Authors:** Tommaso Salvatori, Matteo Forasassi, Alexis Toumi, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18649v1)

**Summary:** Message passing neural networks have shown remarkable performance in algorithmic and constraint reasoning, due to their ability to encode the structure of the task directly in the architecture. Recent work has shown that better results can be achieved using recursive transformers trained with deep supervision and truncated recursions, which make extremely deep loops stable to train, and equipped with test-time procedures such as discrete deduction lattices. In this work, we apply the same proced...

---

### 42. ST-GRU PredRNN-V2: A GRU-Based Reformulation of PredRNN-V2 for Video Prediction

**Authors:** Augusta van Haren, Hanna Hoogen, Luca Pattavina, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18645v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18645v1)

**Summary:** Video prediction requires models to capture complex spatiotemporal dependencies and to retain relevant information over long sequences. PredRNN and its successor PredRNN-V2 address this challenge with spatiotemporal Long Short-Term Memory (ST-LSTM) units that maintain two separate memory states, at the cost of a relatively complex recurrent building block. In this work, we investigate whether the simpler gating of Gated Recurrent Units (GRUs) can be transferred to spatiotemporal predictive learn...

---

### 43. To Align or Not To Align: Check Your COMPASS Before You Train

**Authors:** Fabian Gröger, Petar Damjanović, Maria Brbić

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18638v1)

**Summary:** Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a model pair will be compatible prior to alignment or merging. Building on the obs...

---

### 44. DTScribe: Generating Models for Digital Twin Reporting using Local Large Language Models

**Authors:** Kérian Fiter, Angelica Portocarrero, Bentley Oakes

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18635v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18635v1)

**Summary:** The development of a digital twin brings together many stakeholders and technical components. We have previously investigated the reporting of the conceptual architecture for these digital twins as an artifact for discussion. However, we find that the activity of modeling the digital twin for visualization and consensus-building can be quite tedious and time-consuming.   In this article, we explore the automation of model generation using large language models, targeting the model required for d...

---

### 45. Geometric Calibration of Supervised Fine-Tuning

**Authors:** Jianzhu Bao, Jia-Chen Gu, Qingyuan Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18634v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18634v1)

**Summary:** Recent studies investigate the weight geometry through its spectral structure, which characterizes how the weights transform different input directions. Within this view, supervised fine-tuning (SFT) is shown to induce dense updates that perturb the spectral geometry of pre-SFT weights along their principal directions, potentially disrupting the model's prior knowledge. These observations motivate using the geometry of pre-SFT weights as a reference for refining learned SFT updates. We study thi...

---

### 46. Falsification-proof non-market allocation mechanisms

**Authors:** Eduardo Perez-Richet, Vasiliki Skreta

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18625v1)

**Summary:** Relying on manipulable characteristics to target the allocation of resources is fraught with difficulties. Naively optimal rules lead to falsification and allocative inefficiency. Optimizing the rule for allocative efficiency while accounting for falsification typically induces falsification, at a heavy cost to the agents. Moreover, falsification generates negative externalities. We characterize optimal falsification-proof rules under a broad range of falsification technologies. We also provide ...

---

### 47. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 48. Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve

**Authors:** Yuyang Bai, Yu Wang, Yu Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18616v1)

**Summary:** Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge graph interaction (DKGI), a harness in which language model agents create graph access tools directly over complete node and edge files. The agent writes Python code to follow relations, combine node sets, and select text...

---

### 49. Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents

**Authors:** Ashutosh Hathidara

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18614v1)

**Summary:** Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence is the natural candidate, but existing reinforcement learning methods calibrate it against the correctness of a decision at the current step. We propose a method to calibrate it again...

---

### 50. Does self-distillation improve reasoning?

**Authors:** Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18613v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18613v1)

**Summary:** Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement learning (RL), but it remains unclear whether these gains extend beyond in-distribution evaluations and whether they stem from privileged distillation. In this paper, we revisit two representative methods, Self-Distillat...

---

## cs.CL

**50 papers**

### 1. ChunkAct: Action Chunking for Agentic Robotics

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18874v1)

**Summary:** Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once ...

---

### 2. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18868v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18868v1)

**Summary:** Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce ...

---

### 3. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning

**Authors:** Minghao Luo, Liang Chen

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18862v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18862v1)

**Summary:** Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heuristics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a training-free decoding method in which a much smaller reasoning model steers the large one t...

---

### 4. Hybrid Reasoning Agents

**Authors:** Jiaru Zou, Yunzhe Qi, Sirui Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18861v1)

**Summary:** How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturall...

---

### 5. The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement

**Authors:** Sijie Zhao, Zeqi Zhou, Heli Qi, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18845v1)

**Summary:** Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines what the agent may use and the verifier defines what counts as success. Every EO task can be made verifiable, through labeled benchmarks, independent sensors, physical models or the repeated observation of the same place. G...

---

### 6. OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding

**Authors:** Xuyang Liu, Shihao Wang, Xinyu Wei, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18829v1)

**Summary:** With the rapid development of multimodal large language models (MLLMs), evaluating their video understanding capabilities has become increasingly important. Existing video understanding benchmarks cover only part of the evaluation dimensions, limiting systematic diagnosis of omni-modal video understanding. We introduce OmniCompass, a holistic benchmark for omni-modal video grounding and understanding. OmniCompass defines two evaluation tracks: OmniCompass-VL assesses vision-language models on ta...

---

### 7. Read the Room Before Your Model Generates

**Authors:** Muyao Kong, Zhihao Lin

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18820v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18820v1)

**Summary:** Large language models (LLMs) generally rely on sampling temperature to regulate the amount of randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed, heuristic global settings and context or token-level calibration, rather than a geometrically interpretable representation of the communicative scenario. In this work, we introduce a simple and interpretable temperature selection framework, the \textbf{Scenario-Actor}, which adapts decoding to the inferred...

---

### 8. Back-Translation Still Matters: Leveraging Monolingual Data for Low-Resource Machine Translation with LLMs

**Authors:** Divyanshu Bathla, Parag Singla, Jitin Singla

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18818v1)

**Summary:** Pre-trained Large Language Model (LLMs) are effective on many tasks in zero-shot and few-shot settings. For machine translation of low-resource languages, the obvious options are few-shot prompting and fine-tuning on a small parallel set. We ask: what if moderate amounts of low-resource monolingual data are also available? We argue that, rather than continued pretraining, a more effective use of this data is the pre-LLM era technique of back-translation (BT). The current fine-tuned LLM translate...

---

### 9. Self-Evolving Agent Harness

**Authors:** Chuyang Wei, Haoxiang Guan, Minghang Zhu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18813v1)

**Summary:** Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates update targets from proposal and admission mechanisms. It distinguishes changes to interpreted state from revisions to tools and code, repository-level control logic, and plugin composition. We characterize search through ev...

---

### 10. SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection

**Authors:** Wenlin Zhong, Hao Wang, Kun Yuan, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18807v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18807v1)

**Summary:** Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches often either assume skill injection is beneficial or rely on indirect feedback or rollout-intensive evaluation to assess its utility. Our pilot studies show that rollout-based utility estimation for skill credit assignment ...

---

### 11. SEAR: Self-Evolving Agentic Robotics

**Authors:** Xinyi Wang, Bangzheng Li, Hanyu Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18792v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18792v1)

**Summary:** Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy ...

---

### 12. Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity, and Aggregation

**Authors:** Donghwan Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18786v1)

**Summary:** LLM ensemble gains are often measured against a single baseline, but the value attributed to additional candidates can change with the comparison used. We study an LLM aggregator under four matched conditions: Direct (no candidates), Single-slot (one candidate in a multi-slot interface), Duplicate (one candidate repeated), and Multi-candidate (separately generated candidates). Under either non-diverse control, overall candidate gain (CIV) splits algebraically into an additional-candidate contras...

---

### 13. Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents

**Authors:** Yuchen Lu, Julian McAuley, Lei Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18784v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18784v1)

**Summary:** Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history that produced it? In this paper, we introduce CarryOn, an object-oriented context runtime that organizes continuation around reusable task objects. Rather than treating compressed histories or reconstructed accounts of ...

---

### 14. BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems

**Authors:** Xiaoguang Guo, Yaohao Long, Chuxu Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18780v1)

**Summary:** Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent and decisive error step. Recent methods trace dependencies, but knowing where information came from is not the same as knowing where it went wr...

---

### 15. Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges

**Authors:** Tianci Liu, Haoyu Wang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18766v1)

**Summary:** Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges provide only relative preferences, complicating their direct use for policy optimization. We propose ReVeR, a pointwise rubric RM that derives h...

---

### 16. Looking Complete Is Not Being Grounded: Evaluating LLM Sitreps Against Human-Authored Situation Reports

**Authors:** Sachin Kumar

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18762v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18762v1)

**Summary:** Evaluation for automatic crisis reporting should measure what practitioners need, not what is convenient to compare. Through LLM-assisted, author-approved content analysis, we derive a 15-slot information schema from professional humanitarian situation reports using qualitative content analysis, then evaluate 121 human and 261 LLM-generated reports across five disasters and three hazard types. Under google/gemini-3.7-flash on Cyclone Idai, the best machine arm is nominally above the empirical hu...

---

### 17. PreciseCoder: Faithful and Generalizable Debugging Beyond Unit-Test Rewards

**Authors:** Yunkai Zhan, Miaosen Chai, Shangshang Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18755v1)

**Summary:** Reinforcement learning (RL) from unit tests is the common recipe for post-training code models, but a unit test only asks whether the final program passes. We analyze what this unit-test-only reward teaches a model during debugging and find that, while it raises pass rates, it also teaches the model to edit more and to hallucinate bugs in code that is already correct. We introduce PreciseCoder, a training algorithm that augments the unit-test reward with a signal for semantically verified, local...

---

### 18. On the Monitorability of Natural Language Autoencoders: Identification vs Discrimination

**Authors:** Kevin Yandoka Denamganaï

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18727v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18727v1)

**Summary:** Natural Language Autoencoders (NLAs) are proposed as oversight tools for language models: an Activation Verbaliser (AV) writes an English explanation of an activation vector, and an Activation Reconstructor (AR) maps the explanation back to a vector. Their value for oversight depends on a human monitor being able to tell a true account of an activation from a false one, given the Av's explanation. We formalise NLA training and NLA oversight deployment as two different referential games from Emer...

---

### 19. Code-Switching Detection via Language-Selective Dimensions in Speech Foundation Models

**Authors:** Jie Chi, Zakaria Aldeneh, Masha Fedzechkina, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18726v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18726v1)

**Summary:** Code-switching (CS), the alternation between languages within an utterance, is common in multilingual speech but underrepresented in pretraining corpora. Increasing CS coverage requires finding relevant utterances in large speech collections so that they can be included in training data. One way to find such utterances is to transcribe the speech and detect language alternation in the text, but this depends on obtaining accurate multilingual transcriptions. We propose a lightweight method that d...

---

### 20. From Relation-Specific Heads to Shared Interventions: Contextual Entrainment in Language Models

**Authors:** Jinghan Zheng, Jiajun Shi

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18674v1)

**Summary:** Large language models rely on prompt context to perform in-context learning, follow formats, and adapt to local evidence. This ability, however, also raises a robustness concern: models may reuse irrelevant tokens from earlier context when answering a later query. Prior work identifies this behavior as contextual entrainment and finds attention heads whose ablation reduces it, arguing that these heads are largely task- or relation-specific. But are the mechanisms behind contextual entrainment tr...

---

### 21. SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation

**Authors:** Ziyang Song, Lia Shen, Yixuan Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18672v1)

**Summary:** Biomedical language models (LMs) provide strong representations for clinical tasks, but they often fail to capture the hierarchical structure among medical concepts. This limitation is especially pronounced for rare and fine-grained clinical codes in long-tailed vocabularies, where hierarchy-agnostic LM representations become less informative as concept frequency decreases. We introduce Semantic Medical Identifier (SMI), a training-free framework for constructing ontology-grounded Semantic IDs a...

---

### 22. Known-Voice Cloning and the Limits of Personality Transfer for Character Design

**Authors:** Johanna Magdalena Kuch, Maud van Lier, Daksitha Senel Withanage Don, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18669v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18669v1)

**Summary:** Recent advances in zero-shot voice cloning systems make it possible to reproduce a recognizable voice from a short recording and attach it to arbitrary virtual characters. Prior work suggests that familiar vocal identity can carry over associated personality impressions to new targets such as robots or virtual characters. However, these works have mainly examined familiarity and personalization effects rather than directly testing whether a cloned familiar voice systematically transfers personal...

---

### 23. Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback

**Authors:** Weida Liang, Kenji Kawaguchi

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18656v1)

**Summary:** Language model systems repeatedly make test-time decisions by comparing similarity: they retrieve exemplars, rank candidates, and revise responses. Yet similarity is not unique: lexical, semantic, structural, and stylistic resemblance can point to different candidates, and the task-aligned notion can change across instances. We introduce BASIS (Bayesian Axis Selection via Interactive Signals), a training-free Bayesian method that uses weak test-time feedback to infer which criterion in a supplie...

---

### 24. Does Pretraining Teach Chemical Language Models Chemistry?

**Authors:** Leif Sieben, Yoel Zimmermann

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18651v1)

**Summary:** Chemical language models (CLMs) are pretrained on large corpora of molecules with the aim of learning representations that transfer to diverse downstream tasks. Here, we systematically study the effects of pretraining using a series of such CLMs across 64 molecular property prediction datasets. We find that the downstream gains of pretraining in CLMs do not scale and performance saturates below gradient-boosting baselines. Across the regimes evaluated, only supervised pretraining on traditional ...

---

### 25. To Align or Not To Align: Check Your COMPASS Before You Train

**Authors:** Fabian Gröger, Petar Damjanović, Maria Brbić

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18638v1)

**Summary:** Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a model pair will be compatible prior to alignment or merging. Building on the obs...

---

### 26. Breakdown of Conversational Involvement: A Joint Multi-Modal Analysis of Conversation Floors and F-formation Detection with Multiple Features

**Authors:** Zonghuan Li, Chirag Raman, Hayley Hung

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18627v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18627v1)

**Summary:** Interactions happen universally and spontaneously in daily lives. Studying involvement in interactions helps us analyze who can influence who and has a wide potential in applications. Specifically, we consider conversational involvement in free-standing conversations. We study two operationalizations of an FCG: F-formations and conversation floors, and propose that current assumption that F-formations capture single conversations is insufficient. To illustrate how different implementations could...

---

### 27. Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve

**Authors:** Yuyang Bai, Yu Wang, Yu Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18616v1)

**Summary:** Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge graph interaction (DKGI), a harness in which language model agents create graph access tools directly over complete node and edge files. The agent writes Python code to follow relations, combine node sets, and select text...

---

### 28. Does self-distillation improve reasoning?

**Authors:** Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18613v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18613v1)

**Summary:** Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement learning (RL), but it remains unclear whether these gains extend beyond in-distribution evaluations and whether they stem from privileged distillation. In this paper, we revisit two representative methods, Self-Distillat...

---

### 29. Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning

**Authors:** Huaiwen Pang, Jiale Han, Junying Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18611v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18611v1)

**Summary:** Legal question answering requires answers that are not only plausible, but also grounded in legally valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot semantic matching, which is insufficient when legal evidence must be selected according to authority, applicability, and diversity across heterogeneous sources. We introduce Legal-R1, an agentic retrieval framework for evidence-based legal reasoning. Legal-R1 decomposes legal reasoning into a multi-agent w...

---

### 30. Jev-ToM: Evaluating Theory of Mind in Typed Decision Models

**Authors:** Kawai Chung, Chunkit Chan, Yuxuan Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18610v1)

**Summary:** Dialogue and collaborative assistants repeatedly judge what a partner knows, believes, or intends. Typed decision models offer a potential alternative to generative large language models for bounded Theory of Mind (ToM) selection. We present Jev-ToM, comparing five typed decision models and seven generative baselines on 11,117 English text questions from nine ToM benchmarks across six capability groups. TypeSafe Jev reaches 73.2% source-balanced accuracy including native controls and ranks first...

---

### 31. Beyond Answer Voting: Fine-Grained Correction of LLM Reasoning through Graph Alignment across Sampled Traces

**Authors:** Haotian Liu, Yingjian Chen, Xiaohang Xu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18606v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18606v1)

**Summary:** Large language models increasingly tackle tasks that require multi-step reasoning, where errors in intermediate claims can affect the final answer. Self-consistency (SC) improves reasoning by voting over sampled final answers, but its vote leaves intermediate disagreements unresolved. To address this problem, we introduce DDRG (Disagreement-Driven Verification Guided by Reasoning Graphs), a framework for selective correction from a frozen bank of reasoning traces. Our insight is that graph align...

---

### 32. From Hindsight to Foresight: Dissecting Clinical Evidence Acquisition in Large Language Models

**Authors:** Ziyang Ling

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18605v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18605v1)

**Summary:** Large language models (LLMs) often diagnose full sight, static clinical cases well yet struggle in foresight, dynamic diagnosis. Prior work has improved this limitation by quantifying the information models acquire and by developing stronger follow-up strategies to improve diagnostic accuracy. In contrast, we introduce a distinctive hindsight to systematically dissect why LLMs fail to acquire diagnostically critical evidence, tracing the failure from evidence identification, utilization and down...

---

### 33. Rethinking Projector Training in Multimodal LLMs

**Authors:** Fabian Gröger, Naël Ouerghemi, Shuo Wen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18598v1)

**Summary:** Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only $10$ to $20\%$ of the data for training the projector already recovers most downstream performance gains, and (ii) projectors trained on different datasets can be linea...

---

### 34. Decomposing and Predicting Annotation Disagreement in Harmful Content Across Languages

**Authors:** Irem Ecem Yelkanat, Faeze Ghorbanpour, Alexander Fraser

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18588v1)

**Summary:** Annotator disagreement is increasingly recognized as a meaningful property of subjective tasks, rather than merely noise to be removed. Predicting which items are likely to be contested could help allocate annotation effort and route difficult cases to human review. We propose predicting disagreement from interpretable semantic properties of the text. An LLM answers a set of binary questions covering harmful-content characteristics, disagreement-related cues such as borderline severity and missi...

---

### 35. The Many Morals of AI: The cautionary bias of North American news narratives in global perspective

**Authors:** Andrew Piper, Edie Pearman

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18573v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18573v1)

**Summary:** The stories told about artificial intelligence (AI) play a central role in shaping public understanding, policy debates, and expectations about technological change. News media are especially influential in this process. Using a cross-regional corpus of 12,924 English-language news articles about AI published since 2022, we examine how storytelling about AI varies across media systems in four regions: North America, China, India, and the Middle East. Leveraging large language models, we extract ...

---

### 36. CREATE: Creativity Evaluation of VLMs using the Visual Remote Associates Test

**Authors:** Ziqing Yang, Anubhav Jangra, Smaranda Muresan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18569v1)

**Summary:** Vision language models (VLMs) are used in creative tasks such as visual storytelling, design ideation, art interpretation, and advertising. Yet we lack principled ways to measure the lateral reasoning of these models compared to human potential. We introduce CREATE, a semi-automatically constructed benchmark containing 155 visual Remote Associates Test problems. These problems require a solver to find an underlying connection among three seemingly dissimilar images. We conduct a human study (N=2...

---

### 37. Empathy Is Not the Scapegoat for Declines in Factuality and Reliability

**Authors:** Letian Shi, Kanwal Mehreen, Deheng Zhang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18541v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18541v1)

**Summary:** Language models are increasingly expected to support users in stressful or uncertain situations, where warmth and empathy are desirable. While recent work associates warmer models with reduced reliability, we show that this conclusion is incomplete. Prior studies often train primarily on empathetic dialogue, making it difficult to separate tone effects from SFT-induced distribution shift. We revisit this issue at both the model and evaluation levels. We study prompting, SFT, and RL for inducing ...

---

### 38. How Reliable Are System-One Decisions in Medicine? A Comparative Study of Jev, Jev-like Models, and LLMs

**Authors:** Yanrui Du, Danyang Zhao, Sendong Zhao, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18529v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18529v1)

**Summary:** Jev has attracted considerable attention for its rapid, generalizable decision-making, yet its medical reliability remains under explored. To address this gap, our study compares various types of system-one decision models across 15 medical datasets comprising 8,742 instances under a unified protocol. Beyond accuracy, we assess decision stability and the ability to recognize unreliable decisions. Our results show that Jev rivals leading models on primarily text-driven tasks but is less effective...

---

### 39. Retrieval Disagreement as a Signal: Diagnosing and Steering Multilingual Dense Embedders

**Authors:** Faeze Ghorbanpour, Shaghayegh Kolli, Jana Diesner, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18526v1)

**Summary:** Multilingual dense retrievers place all languages in one shared space so that a question finds relevant documents, regardless of which language they are written in. We show that the same question, asked in different languages, retrieves substantially different documents, and this disagreement is not because of weak language understanding. Each language performs well on its own and ranks candidates consistently with the other languages; divergence appears only when languages share an index. We tr...

---

### 40. The Geometry of Language Model Logits: Generic Structure and Learned Departures

**Authors:** Swathi Shree Narashiman, Aravind Ramana Venkatramanan, Nambi Seshadri

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18520v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18520v1)

**Summary:** Autoregressive language models produce, at every prediction step, a vocabulary-sized logit vector whose structure determines the conditional next-token distribution. We empirically identify that the ordered vocabulary-head logits follow a remarkably consistent log-linear relation   \[ z_{(r)} \approx μ- α\log r. \] across prediction contexts, architectures, and scales, emerging progressively during pretraining. To our knowledge, this is the first systematic analysis of the logit geometry underly...

---

### 41. Imprinting: Knowledge Distillation Can Shift Student Behavior

**Authors:** Yu-Chien Tang, An-Zi Yen

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18517v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18517v1)

**Summary:** Knowledge distillation trains student models on teacher-generated responses to transfer task capability, but those responses may also carry behavioral tendencies of their source. We investigate whether the source teacher can shape student behavior beyond the capability that distillation is intended to transfer. We construct harm-accepting and harm-avoiding variants of the same base teacher, use them to generate responses to ordinary reasoning and knowledge questions unrelated to safety, and dist...

---

### 42. The Last Mile of Coding Agents for Long-Document Tasks: An Empirical Study on Clinical Trial Protocol Digitization

**Authors:** Jiacheng Lin, Geoffrey Low, Nishit Agarwal, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18507v1)

**Summary:** Clinical trial protocols serve as the source of truth for study design, but are mostly written and used as unstructured PDF documents. Digitizing protocols turns static content into structured, machine-readable data that clinical software can analyze, validate, and execute. Coding agents, which select tools, execute code, and revise their approach as they work, are increasingly applied to such long-document tasks, yet it remains unclear how reliably they turn complete documents into accurate str...

---

### 43. Aligning Faithfulness for Theory-Scale Autoformalization

**Authors:** Yuming Feng, Tadd Mao, Dhruva Arekar, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18498v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18498v1)

**Summary:** Autoformalization (AF) requires more than compilation: formal statements must preserve the meaning of their informal sources, a property known as faithfulness. An emerging frontier is the automated evaluation of this property, yet most existing methods operate at the statement level and produce whole-item verdicts, failing to reveal how individual expressions correspond or which contextual interpretations support the judgment. This omission is consequential because AF is inherently theory-scale:...

---

### 44. Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments

**Authors:** Linhai Ma, Yan Wang, Lingfei Qian, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18497v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18497v1)

**Summary:** Tool-call judges evaluate argument values proposed by LLM agents. We find that they accept a correct value less often when their input holds no reference for it, that is, no text that says what the value should be. This happens when the value is a default value from the function schema that the user did not mention, when it has to be inferred, or when the text it comes from was cut from the judge input. We call this drop in acceptance the derivation gap. It appears across all seven judges we eva...

---

### 45. How Safe Is ChatGPT Health Advice? Evidence from Real User Conversations in Four Global South Countries

**Authors:** Shreyasi Roy Chowdhury, Kiran Garimella

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18465v1)

**Summary:** People increasingly bring their health questions to ChatGPT, yet safety evaluations of LLM health advice rest almost entirely on clinician-authored vignettes, synthetic prompts, or simulated user profiles. The gap is widest for the Global South, where concerns about demographic bias and unsafe recommendations are well documented but have never been tested on real usage. We present, to our knowledge, the first demographically grounded safety evaluation of real-world health conversations with Chat...

---

### 46. Readout Scaling Shapes Sparse Feature Recovery

**Authors:** Brain Xiao, Sarah Wilson

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18462v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18462v1)

**Summary:** Readout scaling changes what a sparse autoencoder (SAE) learns, but the benefit of removing it depends on the data. We use readout-canonicalized decision-space (RC-DS) coordinates to remove singular-value gains while preserving retained decision information. At a fixed readout condition number, changing the generating distribution reverses which training coordinates recover known factors best. In our controlled coordinate-matching study, recovery is highest when training restores the space in wh...

---

### 47. Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL Constraints

**Authors:** Haoxuan Gao, Qin-Wen Luo, Xiang Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18459v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18459v1)

**Summary:** External tools can extend the capabilities of small language models (SLMs), enabling their deployment in resource constrained environments. However, their limited capabilities make it difficult for SLMs to discover effective tool use behaviors through reinforcement learning alone, while direct teacher supervision suffers from teacher student behavioral distribution mismatch and may propagate erroneous preferences. To address these challenges, we propose Selective Teacher guided Policy Optimizati...

---

### 48. Copying Is Not Grounding: Training Faithful Long-Form RAG with Authored-Sentence Credit

**Authors:** Hoang Pham, Duc Anh Vu, Duy Tung Doan, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18442v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18442v1)

**Summary:** In search engines and assistants, long-form RAG answers can mislead readers with claims their sources do not support. Faithfulness rewards, the share of supported sentences, train models toward fewer such claims. We show that these rewards are hacked by copying. A sentence copied from the passages is supported almost by construction, so trained models learn to copy rather than ground what they write. Common defenses only move the hack: a KL or copy penalty leaves copying in place or trades it fo...

---

### 49. Estimating Surprisal from the Speech Signal

**Authors:** Zachary Hopton, Samuel Kiegeland, Francesco Ignazio Re, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18439v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18439v1)

**Summary:** Although language is predominantly spoken, empirical tests of surprisal theory rely almost entirely on written text. In practice, surprisal is estimated using language models (LMs) trained on text and applied to transcriptions, creating a text bottleneck that limits evaluation of the theory in the spoken modality. We remove this bottleneck by estimating surprisal directly from the speech signal using a speech LM. This raises a key question: should surprisal be defined over realization-specific a...

---

### 50. Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments

**Authors:** Hoang Pham, Cong-Duy Nguyen, Dong Le, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18427v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18427v1)

**Summary:** Persistent textual memory lets language-model agents reuse lessons from past tasks to improve on future multi-step tasks without retraining. Systems such as ACE and Dynamic Cheatsheet keep it as a playbook: lessons the agent writes after each task and reads in its prompt. A key challenge is to decide which lessons improve later tasks. Current systems leave the decision to the agent itself, which makes performance unstable: the same procedure can write a playbook that helps or one that falls up t...

---

## cs.CV

**50 papers**

### 1. ChunkAct: Action Chunking for Agentic Robotics

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18874v1)

**Summary:** Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once ...

---

### 2. LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts

**Authors:** Wenxuan Guo, Yingping Liang, Zhaoguo Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18873v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18873v1)

**Summary:** Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment. Real-world rollouts contain successes, suboptimal behavior, and failures: imitating every recorded action can reinforce poor behavior, while filtering out failures discards evidence of physical interactions and their consequences. We introduce \textbf{LoopWAM}, a closed-loop world-action model that learns directly from this full quality spectrum, using rollouts from both itself and other dep...

---

### 3. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

**Authors:** Yunsong Zhou, Xuekun Jiang, Haiqi Shen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18872v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18872v1)

**Summary:** Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of human loco-manipulation built with a wearable system. With an emphasis on professiona...

---

### 4. Dog-Breed Text-to-image Flow Matching from Pretraining to Fine-Tuning on 4 Consumer GPUs

**Authors:** Reyhaneh Esmailizadeh, Xingjian Leng, Zhanhao Liang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18870v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18870v1)

**Summary:** We generally perceive that training text-to-image diffusion models requires heavy compute: it is true if we aim at a comprehensive frontier model. This understanding prevents people from training their own models when getting started in the field. We develop MiniDog, a framework that enables pretraining diffusion transformers in 55 minutes and fine-tuning in another 15 minutes on four 3090 GPUs. For data, we use 26k dog images from ImageNet and caption them for pretraining and use 2k images gene...

---

### 5. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion

**Authors:** Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18871v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18871v1)

**Summary:** Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale depends on unknown target motion, it cannot be measured directly at test time. We d...

---

### 6. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18868v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18868v1)

**Summary:** Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce ...

---

### 7. PLAYGROUND: Progressive Layout Generation with Render-Grounded Planning

**Authors:** Jaeho Lee, Junhwan Heo, Junghyun Park, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18865v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18865v1)

**Summary:** Generating editable graphic designs requires arranging visual and textual elements into a coherent composition while preserving their content and editability. Although recent MLLM-based approaches employ iterative generation and visual refinement to reflect the real-world design workflows, their high-level plans are predetermined prior to execution, limiting their adaptability as the design evolves. To address this limitation, we propose PlayGround, a progressive layout generation framework that...

---

### 8. Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs

**Authors:** Aimon Rahman, Joymallya Chakraborty, Vidit Bansal, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18858v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18858v1)

**Summary:** Multimodal large language models have advanced rapidly, but most remain optimized for single-image inputs. Multi-image reasoning is costly because each image adds many visual tokens, increasing encoding and attention demands. Existing techniques that address the above issue, including visual token pruning, token merging, visual token compression, learned resampling, hierarchical compression, retrieval-augmented visual reasoning, and memory-based architectures, have largely been designed for sing...

---

### 9. PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts

**Authors:** Ruixiao Dong, Jianmin Bao, Bozhi Luan, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18857v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18857v1)

**Summary:** Pixel-space diffusion models provide an appealing alternative to latent-space diffusion models by directly modeling raw images without relying on a learned tokenizer. However, scaling pixel-space models has predominantly followed dense strategies, tightly coupling model capacity with active computation. In this work, we show that standard LLM-style Mixture-of-Experts (MoE) architectures can be effectively transferred to pixel-space diffusion. Building on this finding, we introduce PixelMoE, a pi...

---

### 10. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

**Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18846v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18846v1)

**Summary:** Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud and camera poses estimated from the input images by a reconstruction model as a ...

---

### 11. The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement

**Authors:** Sijie Zhao, Zeqi Zhou, Heli Qi, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18845v1)

**Summary:** Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines what the agent may use and the verifier defines what counts as success. Every EO task can be made verifiable, through labeled benchmarks, independent sensors, physical models or the repeated observation of the same place. G...

---

### 12. RepProbe: Can Video Language Models Count Repeated Actions? A Diagnostic Benchmark

**Authors:** Mahsa Khoshnoodi, Sarah Adel Bargal

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18844v1)

**Summary:** Repetition counting requires identifying and enumerating action cycles over time. While state-of-the-art video language models describe actions fluently, they fail to reliably count how many times an action repeats. To investigate this limitation, we introduce RepProbe, a benchmark of 42K real and synthetic video clips containing exactly k in [1, 20] complete repetitions, with controls for clip position, temporal coverage, and duration. These controls allow us to study the counting failure direc...

---

### 13. Scaling Online Optimal Transport Minibatches for Flow Matching

**Authors:** Peter Chen, Sergey Levine

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18838v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18838v1)

**Summary:** A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are paired with data. Independent random pairing introduces substantial stochasticity, motivating minibatch optimal transport (OT) to construct online source-target couplings that reduce this randomness (Tong et al., 2024). However, as applications extend to larger and higher-dimensional datasets, small minibatches can limit th...

---

### 14. Plan-Bench: Can Existing VLMs Go Well Beyond Perception to Reason and Plan in Embodied Worlds?

**Authors:** Juntong Feng, Qingan Liu, Jingru Dong, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18836v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18836v1)

**Summary:** Vision-Language Models (VLMs) have achieved strong performance in visual perception and spatial reasoning, leading to growing interest in using them as high-level planners for embodied AI. However, physical tasks require models to integrate spatial information, reason over temporal states, and generate multi-step plans under various constraints, raising the question of whether current VLMs can reliably support such reasoning and planning independently of execution. We introduce Plan-Bench, a ben...

---

### 15. Game2Real-Bench: Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?

**Authors:** Qingan Liu, Juntong Feng, Yue Zhu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18834v1)

**Summary:** Visual reasoning is an important capability for vision-language models (VLMs) to understand visual evidence, spatial structure, constraints, and state changes. Existing evaluations mainly rely on real-world data or procedurally generated tasks. Real-world data preserve natural complexity, while procedural games provide controllable generation and verifiable solutions. However, it remains unclear whether abilities measured in toy games correspond to real-world visual reasoning and whether game ex...

---

### 16. OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding

**Authors:** Xuyang Liu, Shihao Wang, Xinyu Wei, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18829v1)

**Summary:** With the rapid development of multimodal large language models (MLLMs), evaluating their video understanding capabilities has become increasingly important. Existing video understanding benchmarks cover only part of the evaluation dimensions, limiting systematic diagnosis of omni-modal video understanding. We introduce OmniCompass, a holistic benchmark for omni-modal video grounding and understanding. OmniCompass defines two evaluation tracks: OmniCompass-VL assesses vision-language models on ta...

---

### 17. WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions

**Authors:** Haoyi Duan, Liliang Chen, Nan Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18826v1)

**Summary:** We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions. Given the same initial observation and low-level action sequence, WorldOracle asks whether a predicted rollout reproduces what happens in the real world, including physical consequences and task-state transitions. We evaluate models along four complementary dimensions: physical state correctness, interaction spatial alignment, key interaction area ...

---

### 18. DuplexBridge: Coordinating Understanding and Generation for Unified Image Editing

**Authors:** Yidi Liu, Jie Xiao, Chaojie Mao, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18819v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18819v1)

**Summary:** Complex image editing requires faithful task interpretation and accurate execution, but a failed edit does not reveal which responsibility failed. We present DuplexBridge, which uses a unified model's own understanding capability to enhance prompts for its own generation capability, without an external understanding module. A source-grounded bridge specifies targets, final-state changes, and preservation constraints. Understanding is supervised on fidelity to the original request without observi...

---

### 19. Registration is a Representation Problem: Solving Whole-Body PET/CT Registration

**Authors:** Neel Dey, Adrian V. Dalca

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18804v1)

**Summary:** Raw image intensities are a poor surrogate for similarity across images in correspondence problems. Further, while auxiliary segmentation labels can provide semantic identification and improve matching, they can assign only coarse identities to fine-grained anatomy and often cover only a subset of structures, particularly in whole-body settings. We present an approach that instead establishes correspondence using complementary representations of anatomy and demonstrate its utility for longitudin...

---

### 20. Trust Before Autonomy: Rethinking Agentic Remote Sensing for Crisis Response

**Authors:** Georgios Angelidis, Aggelos Psiris, Spyridon Evangelatos, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18789v1)

**Summary:** Agentic remote sensing is evaluated on how many questions it can answer, whereas crisis response depends on whether its answers can be relied on and how much of the decision can safely be handed to the agent. This paper argues that \emph{autonomy should be earned, not assumed}: An Earth-Observation (EO) agent should be granted autonomy in proportion to demonstrated reliability, epistemic honesty and verifiability. The position is supported by an evidential meta-analysis of twelve agentic RS/EO/G...

---

### 21. GAD: Geometry Attention Distillation for Consistent Video Generation

**Authors:** Junfeng Ni, Ziyu Zhu, Fan Jiang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18779v1)

**Summary:** Video diffusion models generate visually compelling short-term sequences but often struggle to preserve scene geometry and object structure over time. In this paper, we first demonstrate that current video attention cannot identify reliable correspondences across frames, with responses dispersed across multiple regions even after recognizable scene structure has emerged. We argue that reliable cross-frame associations are essential for information exchange as scene structure forms in video gener...

---

### 22. The Federated Tumor Segmentation and Classification (FeTS++) Challenge

**Authors:** Wenyi Tang, Carla Pitarch-Abaigar, Siddhesh Thakur, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18771v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18771v1)

**Summary:** International challenges have become the standard for developing and benchmarking biomedical image analysis methods using centralized multi-institutional data. Federated learning (FL) describes a paradigm-shift on multi-institutional collaborations, where models are trained across institutions while their data are always retained locally. The Federated Tumor Segmentation (FeTS) challenge, first held in 2021, was the first challenge dedicated to FL in medical imaging and editions in 2022 and 2024...

---

### 23. MIST: Multi-Scale Spatial Context for Gene Expression Prediction from Histology

**Authors:** Koushik Howlader, Tirtho Roy, Md Tauhidul Islam, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18769v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18769v1)

**Summary:** Predicting spatial gene expression from standard H&E images could extend molecular analysis to tissues without spatial transcriptomic measurements. A standard Transformer applies self-attention over spots but ignores where each spot sits in the tissue, whereas a spot's molecular state depends on tissue context at multiple spatial scales. Building on this insight, we introduce MIST, a Multi-context Spatial Transformer that augments the self-attention backbone with two context pathways applied in ...

---

### 24. LayerCanvas: Infographic Generation in AI Learning Assistants via Hybrid Layer-Set Diffusion

**Authors:** Keshav Gupta, Jeremy Owen, Christopher Lloyd, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18763v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18763v1)

**Summary:** Online learning platforms are increasingly deploying AI assistants to provide personalized, on-demand tutoring. These can leverage infographics to communicate complex information and improve the learning experience. However, automating effective infographic generation remains a challenging task, requiring a combination of visual richness with precise typography, structured layouts, and continued editability. Existing representation methods satisfy these goals only in part: Scalable Vector Graphi...

---

### 25. Context-aware Bayesian Fusion for Multimodal Object Detection

**Authors:** Arunachalam Venkatachalam, Mhafuzul Islam, Marwan Yusuf, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18741v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18741v1)

**Summary:** Reliable detection of pedestrians and road users is essential for the safe operation of autonomous vehicles. However, this task becomes increasingly challenging under adverse environmental conditions, such as poor weather and low lighting, where the performance of state-of-the-art pre-trained object detectors and on-board sensors tends to degrade, which limits their effectiveness and reliability. Moreover, retraining models for each operating context imposes significant constraints due to high d...

---

### 26. Concealed Handgun Detection using WiFi Signals

**Authors:** Erik Persson, David Gustafsson, Tomas Wilkinson

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18736v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18736v1)

**Summary:** While conventional camera-based surveillance systems and metal detectors can provide a sufficient level of security when used appropriately, they have fundamental limitations that reduce their applicability. Camera-based systems are unable to detect occluded or concealed threats and metal detectors require each person to enter through a narrow opening one at a time, leading to congestion issues and limited use in large crowds. A WiFi-based security system has the potential to be a complementary ...

---

### 27. Segment Where You Look: Attention as the Interface Between Language Models and Segmenters

**Authors:** Eslam Abdelrahman, Hamza Omar Alkaf, Yuheng Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18729v1)

**Summary:** Vision-language models (VLMs) that segment from language must pass the location of the referent to a pixel decoder. The dominant interface compresses it into the hidden state of a single [SEG] token, a d-dimensional vector with no spatial index, and leaves the decoder, which never sees the expression, to recover the referent's extent. We show that the VLM already computes a better signal: the [SEG] token's attention over the image tokens, which is defined on the patch grid by construction. Probi...

---

### 28. AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface

**Authors:** Emory Salaun, Syed Ayon, Kaleel Mahmood, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18724v1)

**Summary:** The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of...

---

### 29. UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

**Authors:** Jingbo Xu, Jianjie Fang, Zhuohang Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18697v1)

**Summary:** World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities req...

---

### 30. CryoTracer: A Synthetic-to-Real System for Filament Instance Tracing in Cryo-EM

**Authors:** Radosław Kuczbański, Wojciech Kozłowski, Mateusz Grzesiuk, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18696v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18696v1)

**Summary:** Particle picking in cryo-electron microscopy is commonly formulated as an object-detection problem in which individual particles are represented by bounding boxes, a natural representation for globular particles but a poor match for filaments that can extend across an entire micrograph. Existing methods reconstruct filament trajectories by linking local predictions in a separate post-processing stage, decoupling detection from instance formation and creating potential ambiguities at gaps and cro...

---

### 31. GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models

**Authors:** Rong Li, Shijie Li, Jiangyong Huang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18694v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18694v1)

**Summary:** Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features. Capturing geometry, however, does not ensure its use: zeroing the aligned latents of a released feature-alignment model leaves its accuracy uncha...

---

### 32. Orientation Estimation of Cryo-EM Images for Molecules with Arbitrary Symmetry by Semidefinite Programming

**Authors:** Yunpeng Shi, Amit Singer, Jinxin Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18691v1)

**Summary:** This paper extends the non-unique games framework introduced in Bandeira et al. (2020) to address symmetric structures. Precisely, we consider the problem \[ \begin{aligned}   \underset{g_1,\ldots,g_n\in \mathcal{G}}{\operatorname{min}}\,\, \frac{1}{|S|}\sum_{i,j=1}^n \sum_{s\in S} f_{ij}(g_i s g_j^{-1}), \end{aligned} \] where $\mathcal{G}$ is a compact group, $S\subset \mathcal{G}$ is a finite subgroup of symmetry elements, and $f_{ij}:\mathcal{G}\rightarrow \mathbb{R}$ is a loss function. A n...

---

### 33. Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning

**Authors:** Tianhao Fu, Austin Wang, Charles Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18690v1)

**Summary:** Image-token compression must reduce computation without hurting the semantics. We introduce Varest, guided by semantic fungibility: tokens within a coherent semantic region can be summarized coarsely, while object boundaries and literal text require finer distinctions. Object and text localizers guide variable-resolution merging, preserving spatial coverage and finer detail at boundaries and text. Learned [REL] registers then prune visual tokens after early decoder processing. Training across bu...

---

### 34. RSIgen: Reciprocal Self-Improvement for Agentic Visual Generation

**Authors:** Yidi Liu, Haozhe Wang, Jie Xiao, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18688v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18688v1)

**Summary:** Agentic visual generation produces experience that can improve the native understanding (agent) and generation roles of a unified multimodal backbone, but task success alone does not determine which role should learn. Generator updates can also make the agent's action supervision stale. We introduce RSIgen, a task-centric reciprocal self-improvement framework linking learning allocation, supervision refresh, and recursive curriculum construction. Dynamic Responsibility Routing (DRR) uses matched...

---

### 35. RadarGSOcc: Doppler-Aware 3D Semantic Occupancy Prediction Using 4D Radar Tensor with Geometric-Semantic Feature Extraction

**Authors:** Christofel Rio Goenawan, Dong-Hee Paek, Seung-Hyun Kong

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18686v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18686v1)

**Summary:** 3D semantic occupancy prediction is crucial for autonomous driving, but camera-based methods degrade in low-light conditions and LiDAR-based methods are sensitive to adverse weather. 4D radar is more robust, yet its sparsity and the high cost of radar tensor processing limit its use. We propose Radar Geometric-Semantic Occupancy Prediction (RadarGSOcc), an efficient framework that directly processes 4D radar tensors by separately extracting geometric and semantic features, including Doppler info...

---

### 36. Perception Beyond the Visible: Incompleteness-Aware Scene Understanding for Robot Autonomy

**Authors:** Rohit Mohan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18670v1)

**Summary:** Reliable robot autonomy requires reasoning about the world from partial and noisy observations. However, many perception systems model only visible scene regions, rely on fixed semantic categories, and assume reliable sensor measurements. These assumptions break under occlusion, novel object encounters, and sensor degradation. In this paper, I present a research vision for incompleteness-aware scene understanding. I organize this vision around three fundamental challenges: incomplete evidence, i...

---

### 37. PlanPath: Exploration-Guided Orchestration for Patient-Level Pathology Reasoning

**Authors:** Jiusong Ge, Mingzhao He, Qidong Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18664v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18664v1)

**Summary:** A patient's pathology case spans tens of slides from distinct specimens and anatomical sites, each carrying non-redundant, site-specific evidence. Forming a patient-level conclusion therefore requires locating the slides relevant to a given question and integrating complementary findings across them. However, existing pathology agents analyze one slide at a time and describe morphology rather than measure it, leaving evidence acquisition across a patient's specimens and patient-level quantificat...

---

### 38. Texture Interpolation as Texton Matching

**Authors:** Ido Madar, Gal Oren, Shai Avidan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18655v1)

**Summary:** Texture interpolation asks what should lie between two textures. Standard methods typically blend pixels or features at corresponding spatial locations, implicitly assuming that co-located elements should be mixed. For unrelated textures, however, this correspondence is arbitrary: a crack at one location has no particular relationship to a fiber at the same location in another image. We study whether this hidden pairing choice is itself a major determinant of interpolation quality. We represent ...

---

### 39. ST-GRU PredRNN-V2: A GRU-Based Reformulation of PredRNN-V2 for Video Prediction

**Authors:** Augusta van Haren, Hanna Hoogen, Luca Pattavina, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18645v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18645v1)

**Summary:** Video prediction requires models to capture complex spatiotemporal dependencies and to retain relevant information over long sequences. PredRNN and its successor PredRNN-V2 address this challenge with spatiotemporal Long Short-Term Memory (ST-LSTM) units that maintain two separate memory states, at the cost of a relatively complex recurrent building block. In this work, we investigate whether the simpler gating of Gated Recurrent Units (GRUs) can be transferred to spatiotemporal predictive learn...

---

### 40. Grid or Nodes? Probing Object Memory in World Models Under Partial Observability

**Authors:** Justin McMillen, Yasin Yilmaz

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18637v1)

**Summary:** A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also sco...

---

### 41. MajorTOM:Elliot Pretrain, A Multi-Sensor, Multi-Temporal Pretraining Dataset for Earth Observation

**Authors:** Carmen Oliver Huidobro, Mikolaj Czerkawski, Kevin Monsalvez-Pozo, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18624v1)

**Summary:** Pretraining generalist Earth observation foundation models requires data that combine several sensors, varied temporal sampling and, increasingly, text, yet open datasets rarely provide all three in one consistent, easily accessible form. We introduce MajorTOM:Elliot Pretrain, a collection of 279,166 tiles of 10 km drawn from the Major-TOM grid by clustering AlphaEarth embeddings. Each tile stacks Sentinel-2 L1C, Landsat-8/9, Sentinel-1 RTC, Copernicus DEM and ESA WorldCover on a shared 1056x105...

---

### 42. VideoJev: System One Model for Video Understanding and Interaction

**Authors:** Yuhan Zhu, Xiangyu Zeng, Qingyi Si, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18615v1)

**Summary:** Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev, a family of models that cast video understanding and interaction as structured decision tasks. We adapt pretrained multimodal large language models (MLLMs) by replacing autoregressive answer decoding with a shared head that scores temporal intervals and textual options against video evidence. These scores yield event s...

---

### 43. DPOison-VL: Clean Preference Poisoning in Vision-Language Direct Preference Optimization

**Authors:** Chengtao Jian, Kai Yang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18609v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18609v1)

**Summary:** Direct Preference Optimization (DPO) has become a widely adopted approach for aligning vision-language models (VLMs), yet the security of multimodal preference data remains largely unexplored. Existing preference poisoning attacks either corrupt explicit supervision signals or require visible triggers, making them detectable under human inspection. We introduce DPOison-VL, the first clean preference poisoning attack against VLM-DPO, which manipulates model alignment solely through imperceptible ...

---

### 44. Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors

**Authors:** Yunuo Chen, Jingnan Gao, Bing He, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18607v1)

**Summary:** Pretrained diffusion models provide powerful generative priors for extreme image compression, but their stochastic, iterative generation processes are not designed to decode compressed representations directly. We present PrismCodec, which recasts a pretrained Diffusion Transformer (DiT) as a bitstream-grounded one-step generative decoder. PrismCodec uses the decoded representation in two complementary roles: a projected codec state defines the starting state for generation, while hierarchical v...

---

### 45. LLM2R: From Large Language Models to 3D Reassemblers

**Authors:** Zhouhan Zhong, Qiuhong Shen, Xingyi Yang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18604v1)

**Summary:** 3D part assembly aims to reconstruct a complete shape from a set of unassembled parts by predicting a rigid SE(3) transformation for each part. Because the placement of a part is rarely determined by its own geometry, the task demands reasoning over the entire part set, and existing methods, which rely on pairwise relations or iterative generation and verification, scale poorly to objects with many parts. We present LLM2R, which casts part assembly as sequence modeling with a pretrained decoder-...

---

### 46. Rethinking Projector Training in Multimodal LLMs

**Authors:** Fabian Gröger, Naël Ouerghemi, Shuo Wen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18598v1)

**Summary:** Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only $10$ to $20\%$ of the data for training the projector already recovers most downstream performance gains, and (ii) projectors trained on different datasets can be linea...

---

### 47. Detecting Unreliable Classifications from Quantized Models

**Authors:** Ananya Kotla, Jorge T. Gomez

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18575v1)

**Summary:** Post-training INT8 quantization is typically validated by checking accuracy retention, which requires ground-truth labels often unavailable in low-resource clinical settings. We show a label-free alternative: comparing a model's own output before and after quantization. We compute cosine similarity between the FP32 and INT8 models' output probability vectors for each prediction, which requires only a single forward pass. This output-agreement similarity separates lower-accuracy predictions acros...

---

### 48. Parameter-Efficient Multimodal Brain Tumor Segmentation With Stage-Wise Shared Adapters

**Authors:** Milad Rostamian, Mohammadreza Mohammadi, Ender Konukoglu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18571v1)

**Summary:** Different MRI modalities reveal different parts of a brain tumor. Segmentation models combine information from these modalities to outline tumor regions. Many models use a separate encoder for each modality. However, exchanging features among these encoders at several stages can increase model complexity. We introduce the Block-Wise Shared Adapter (BWSA), which combines compressed features from the modality encoders in a shared path and returns adapted features to each stream. In its fixed-blend...

---

### 49. Observation Quality in DSM-Assisted Aerial Localization: A Benchmark and Base-Anchored Uncertainty Calibration

**Authors:** Pengyu Yin, Junxiang Tan, Jie Pan, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18564v1)

**Summary:** Aerial map matching provides position observations for navigation, but a position error alone does not determine how an observation should be weighted. We define five benchmark tasks: position availability and agreement, grouped error structure, predictive uncertainty, controlled updates, and temporal accumulation. A case study in digital-surface-model-assisted localization evaluates base-anchored uncertainty calibration within this framework. The method combines propagated image and map sensiti...

---

### 50. Denoise X: Self-Supervised U-Net for Quantum Mottle Suppression in Chest Radiography

**Authors:** Parth Giramkar, Aryan Patle, Vanita Kshirsagar

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18556v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18556v1)

**Summary:** Deep learning for medical image restoration is often constrained by the need for paired training data. Acquiring perfectly registered clean-noisy radiographs in vivo is impractical due to patient motion and radiation-dose limits. To address this, we employ a self-supervised Noise2Noise paradigm that trains on independently corrupted observations without paired clean images. We propose Denoise X, a lightweight self-supervised U-Net model (7.79M parameters) for suppressing quantum mottle and elect...

---

## cs.LG

**50 papers**

### 1. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion

**Authors:** Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18871v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18871v1)

**Summary:** Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale depends on unknown target motion, it cannot be measured directly at test time. We d...

---

### 2. What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18869v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18869v1)

**Summary:** How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Ac...

---

### 3. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18868v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18868v1)

**Summary:** Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce ...

---

### 4. Data Free Training of Diffusion Models for Lattice Field Theories

**Authors:** Dennis Grinwald, Ankur Singha, Khaled Kahouli, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18863v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18863v1)

**Summary:** Sampling equilibrium field configurations remains a major computational bottleneck in lattice field theory, motivating the development of generative samplers that can produce independent configurations. Diffusion models are promising for this purpose, but their standard denoising score matching objective requires samples from the target distribution, seemingly reintroducing the original sampling problem. Here, we show that diffusion models can instead be trained from their own generated samples ...

---

### 5. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning

**Authors:** Minghao Luo, Liang Chen

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18862v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18862v1)

**Summary:** Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heuristics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a training-free decoding method in which a much smaller reasoning model steers the large one t...

---

### 6. Hybrid Reasoning Agents

**Authors:** Jiaru Zou, Yunzhe Qi, Sirui Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18861v1)

**Summary:** How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturall...

---

### 7. Exact Topological Compliance: Generating Persistence-Equivalent Graphs

**Authors:** Mattie Ji, Indradyumna Roy, Vikas Garg

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18856v1)

**Summary:** Persistent homology summarizes the topological evolution of a graph as persistence diagrams (PDs). Generating graphs whose topology matches a target descriptor is increasingly important, yet existing topology-aware generative models rely on soft regularization, producing graphs whose PDs may only be approximately similar. We initiate a principled investigation of the generation problem: produce graphs that realize a target PD exactly. We propose two approaches guided by the implicit local and gl...

---

### 8. Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards

**Authors:** Yuante Li, Junwei Quan, Kai Qiu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18853v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18853v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in practical multi-step training. We develop a two-clock framework that separates the samples needed to make progress from those consumed before collapse. Under a local quadratic model, the square-root rule p...

---

### 9. MFG: Multi-turn Feedback Guided Molecular Optimization

**Authors:** Trieu Nguyen, Frazier N. Baker, Ruoxi Gao, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18851v1)

**Summary:** Multi-objective molecular optimization is a critical process in drug discovery that aims to modify a given molecule to simultaneously improve multiple properties while maintaining a similar overall structure. This process often requires iterative modifications guided by computational or experimental feedback. Recent large language model (LLM)-based methods have begun to explore this iterative approach; however, these methods are not explicitly trained to leverage such feedback, while existing ap...

---

### 10. Who Improves the Robot? Toward Physical Recursive Self-Improvement

**Authors:** Hai Zhou, Fan Yang, Zeyi Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18842v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18842v1)

**Summary:** Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improvement procedure, making subsequent improvement more effective across tasks. Physical RSI faces challenges from noisy observations, continuous dynamics, costly trials, and irreversible consequences. We present an L0-L5 fra...

---

### 11. Fast Rates for Offline Q-Learning with KL Regularization

**Authors:** Yize Hao, Guangxin Jiang, Shuang Qiu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18839v1)

**Summary:** This paper investigates offline Q-learning for finite-horizon Markov decision processes with Kullback-Leibler (KL) regularization. Recent studies have shown that KL regularization can yield fast rates in offline decision-making problems. However, it remains unclear whether Q-learning, which adopts incremental stochastic approximation updates, can achieve such fast rates in the offline setting. We first propose KL-regularized Q-Learning (KLQ), a simple variant of classical Q-learning. By exploiti...

---

### 12. Scaling Online Optimal Transport Minibatches for Flow Matching

**Authors:** Peter Chen, Sergey Levine

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18838v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18838v1)

**Summary:** A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are paired with data. Independent random pairing introduces substantial stochasticity, motivating minibatch optimal transport (OT) to construct online source-target couplings that reduce this randomness (Tong et al., 2024). However, as applications extend to larger and higher-dimensional datasets, small minibatches can limit th...

---

### 13. RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Uksang Yoo, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18835v1)

**Summary:** It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choices of solver, contact model, and physical parameters explicit and editable, allowing both humans and coding agents to iteratively refine simulations based on observed physical behavior. We implement RSS with the open Newt...

---

### 14. Joint Neural Posterior Estimation and Model Selection for Chemical Reaction Networks

**Authors:** J. Arturo Esquivel, Jorge A. Campos-Gonzalez-Angulo, Sergio Pablo-García, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18825v1)

**Summary:** Simulation-based Bayesian inference for Chemical Reaction Networks (CRNs) must simultaneously solve two computationally demanding problems: discriminating between overlapping reaction pathways and estimating reaction rate constants. Classical approaches, such as Sequential Monte Carlo ABC, rely on handcrafted summary statistics and scale poorly across large parameter spaces. To overcome this, we introduce a neural inference architecture. Our pipeline utilizes shared 1D-CNNs and a permutation-inv...

---

### 15. Statistical Vignettes on the Grokking Phenomenon

**Authors:** Baye Malick Gning, Elvis Dohmatob

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18811v1)

**Summary:** In this work, we study grokking in a simple, analytically tractable setting whose rich phenomenology allows us to disentangle the effects of initialization, signal strength, weight decay, sample size, and input dimension. These factors can produce superficially similar learning curves through distinct mechanisms, complicating their interpretation. Our analysis distinguishes early fitting through nuisance features, core feature learning, and delayed generalization. We identify sharp conditions un...

---

### 16. Depth Memory

**Authors:** David González-Martínez, Philipp Nazari, T. Konstantin Rusch, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18809v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18809v1)

**Summary:** Residual connections propagate information through a network by additively accumulating layer outputs. Recently proposed alternatives, such as Manifold-Constrained Hyper-Connections (mHC) and Attention Residuals (AttnRes), instead use more expressive depth aggregation mechanisms that improve language modeling performance at scale. In this work, we consider the mixing of representations over depth as a problem of storing and retrieving information across layers. Formalizing this perspective, we i...

---

### 17. SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection

**Authors:** Wenlin Zhong, Hao Wang, Kun Yuan, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18807v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18807v1)

**Summary:** Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches often either assume skill injection is beneficial or rely on indirect feedback or rollout-intensive evaluation to assess its utility. Our pilot studies show that rollout-based utility estimation for skill credit assignment ...

---

### 18. Registration is a Representation Problem: Solving Whole-Body PET/CT Registration

**Authors:** Neel Dey, Adrian V. Dalca

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18804v1)

**Summary:** Raw image intensities are a poor surrogate for similarity across images in correspondence problems. Further, while auxiliary segmentation labels can provide semantic identification and improve matching, they can assign only coarse identities to fine-grained anatomy and often cover only a subset of structures, particularly in whole-body settings. We present an approach that instead establishes correspondence using complementary representations of anatomy and demonstrate its utility for longitudin...

---

### 19. Emergent Loop Geometry in Gauge-Equivariant Graph Neural Networks

**Authors:** Ali Rayat, Gia-Wei Chern

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18742v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18742v1)

**Summary:** Gauge-equivariant graph neural networks generate ordered products of gauge links through local message passing, but the geometry of these internal structures is not captured by the receptive field alone. We investigate the statistical ensemble of closed lattice walks generated by recursive node- and edge-feature operations, independently of network training. Analytical and numerical results reveal a separation between rapid growth of contour length and much slower spatial expansion: deeper compo...

---

### 20. A Rate Transfer Method: Convergence Rates in Stochastic Gradient Descent via Stochastic Calculus

**Authors:** Neil Walton

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18739v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18739v1)

**Summary:** We develop a rate-transfer method that converts finite-time Lyapunov estimates for an associated stochastic differential equation (SDE) into finite-time convergence bounds for stochastic gradient algorithms. Under generic moment and smoothness conditions, the convergence analysis of the stochastic gradient method reduces to a calculus argument verifying a Lyapunov generator inequality for the SDE. The method recovers established rates for classical stochastic gradient methods and provides a way ...

---

### 21. Enabling Token-wise Importance Sampling in Off-Policy RLVR with Proximal KL Regularization

**Authors:** Hao Bai, Jiarui Yao, Tong Zhang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18738v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18738v1)

**Summary:** Off-policy data in reinforcement learning with verifiable rewards (RLVR) can arise from asynchronous generation, rollout-training mismatch, and response reuse. Token-wise importance weighting avoids multiplying likelihood ratios across a response but generally biases policy gradients. We prove that, under coverage and local expressiveness conditions, full future KL credit makes the exact proximal optimizer the update's unique stationary policy, even for mixtures of older policies, without full-r...

---

### 22. SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models

**Authors:** Yuqi Huang, Xingyao Li, Yunlong Hou, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18735v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18735v1)

**Summary:** Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput. Self-speculative decoding reuses parts of the target model as a drafter which retains the multi-modal capability of the VLMs, yet its efficiency depends on choosing a suitable draft configuration for each prompt. We propose Single-Peak SPecu...

---

### 23. Learning When to Transfer: Reinforcement Learning for Carbon-Footprint Modeling in New Manufacturing Domains

**Authors:** Muhammad Umar Farooq, Daniel R. Cooper

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18730v1)

**Summary:** Manufacturers often need to characterize a new material, process, or product before enough operating data are available to train reliable predictive models for this new, target domain. Existing manufacturing operations contain potentially useful knowledge to accelerate this characterization, but indiscriminate reuse of data from existing source domains can cause negative transfer in learning of the new, target domain when the manufacturing domains differ sufficiently. This work proposes a reinfo...

---

### 24. On the Monitorability of Natural Language Autoencoders: Identification vs Discrimination

**Authors:** Kevin Yandoka Denamganaï

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18727v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18727v1)

**Summary:** Natural Language Autoencoders (NLAs) are proposed as oversight tools for language models: an Activation Verbaliser (AV) writes an English explanation of an activation vector, and an Activation Reconstructor (AR) maps the explanation back to a vector. Their value for oversight depends on a human monitor being able to tell a true account of an activation from a false one, given the Av's explanation. We formalise NLA training and NLA oversight deployment as two different referential games from Emer...

---

### 25. Learning Source Structure: Bayesian Prediction with Transformers

**Authors:** Meir Feder, Ruediger Urbanke

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18725v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18725v1)

**Summary:** A transformer trained on sequences whose source parameters are drawn afresh each time can learn only what the sequences share: the source family and its prior. The Bayesian predictor that knows both, which we call informed Bayes, is the unique minimizer of the training loss and is computable from the family alone; we use it as a quantitative, falsifiable reference. Where earlier work compared transformers with Bayes on sources whose contexts can be learned independently, we build Markov sources ...

---

### 26. AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface

**Authors:** Emory Salaun, Syed Ayon, Kaleel Mahmood, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18724v1)

**Summary:** The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of...

---

### 27. On Collusion-Free Teaching in Planar Graphs

**Authors:** Khazaliya Liana, Kuske Clemens

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18714v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18714v1)

**Summary:** Non-clashing teaching minimizes teaching complexity among models satisfying the Goldman--Mathias collusion-avoidance criterion. While the Vapnik--Chervonenkis dimension (VCdim) measures the complexity of learning from samples, non-clashing teaching dimension (NCTD) measures the number of examples required when a teacher can select them. Whether NCTD is always bounded above by VCdim remains a fundamental open question in learning theory.   In this paper, we investigate this question for the conce...

---

### 28. UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

**Authors:** Jingbo Xu, Jianjie Fang, Zhuohang Li, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18697v1)

**Summary:** World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities req...

---

### 29. A Refresh Interval Does Not Fully Specify a Refresh Schedule: Learning-Rate-Dependent Placement in Kronecker-Preconditioned Language Model Training

**Authors:** Xinyu Wang, Zhiwei Zhai, Yu Gu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18695v1)

**Summary:** Kronecker-preconditioned optimizers recompute a cached curvature eigendecomposition only periodically, and implementations and adaptive methods control this through the refresh frequency. We show that frequency leaves part of a schedule free: at a fixed number of refreshes, when they occur changes held-out loss at the same compute. Training GPT-style models with the Mousse optimizer across model sizes, we move the middle refreshes of a four-refresh schedule while fixing the first and last. On Fi...

---

### 30. GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models

**Authors:** Rong Li, Shijie Li, Jiangyong Huang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18694v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18694v1)

**Summary:** Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features. Capturing geometry, however, does not ensure its use: zeroing the aligned latents of a released feature-alignment model leaves its accuracy uncha...

---

### 31. Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning

**Authors:** Tianhao Fu, Austin Wang, Charles Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18690v1)

**Summary:** Image-token compression must reduce computation without hurting the semantics. We introduce Varest, guided by semantic fungibility: tokens within a coherent semantic region can be summarized coarsely, while object boundaries and literal text require finer distinctions. Object and text localizers guide variable-resolution merging, preserving spatial coverage and finer detail at boundaries and text. Learned [REL] registers then prune visual tokens after early decoder processing. Training across bu...

---

### 32. Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents

**Authors:** Jiajun Chen, Xinyue Chen, Yicheng Jiang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18684v1)

**Summary:** Personal-agent memory has largely focused on learning what users know, prefer, and want. However, knowing the user does not necessarily mean knowing what the user and the agent have established together. An assistant's proposal should not become an authorized instruction merely because it is remembered. We introduce Grounding Awareness, the ability to distinguish accepted, unacknowledged, revised, and scoped arrangements when selecting actions. We develop a controlled benchmark to test whether a...

---

### 33. ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning

**Authors:** Bowen Ding, Mingda Wan, Yuhan Chen, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18683v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18683v1)

**Summary:** Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that this uniformity inherently reinforces structurally invalid actions in preferred trajectories and ignores the downstream cascading influence of early pivotal deviations in unpreferred...

---

### 34. Model-Based Online Decision Making via Generative Trajectory Planning

**Authors:** Haldun Balim, Yilun Du, Na Li

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18677v1)

**Summary:** Online decision-making faces a tension between efficient inference and long-horizon reasoning. Value-based methods rely on short-horizon bootstrapping that limits the propagation of long-term information, while trajectory optimization methods plan explicitly but must solve a high-dimensional optimization problem at every decision step. We propose Generative Trajectory Planning (GTP), a model-based framework that addresses this tension by learning a generative model as a proposal distribution ove...

---

### 35. BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling

**Authors:** Mengyu Li, Qianqian Qu, Jun S. Liu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18658v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18658v1)

**Summary:** Generative models are often required to serve many downstream conditional tasks. In the training-free setting, a pretrained unconditional model is reused as a prior and combined with a task-specific likelihood to sample from the corresponding posterior. While such training-free samplers have been developed for diffusion and flow models, their counterpart for Schrödinger bridge (SB) models remains unexplored, despite the growing appeal of SBs as flexible stochastic transport models between genera...

---

### 36. Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback

**Authors:** Weida Liang, Kenji Kawaguchi

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18656v1)

**Summary:** Language model systems repeatedly make test-time decisions by comparing similarity: they retrieve exemplars, rank candidates, and revise responses. Yet similarity is not unique: lexical, semantic, structural, and stylistic resemblance can point to different candidates, and the task-aligned notion can change across instances. We introduce BASIS (Bayesian Axis Selection via Interactive Signals), a training-free Bayesian method that uses weak test-time feedback to infer which criterion in a supplie...

---

### 37. Texture Interpolation as Texton Matching

**Authors:** Ido Madar, Gal Oren, Shai Avidan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18655v1)

**Summary:** Texture interpolation asks what should lie between two textures. Standard methods typically blend pixels or features at corresponding spatial locations, implicitly assuming that co-located elements should be mixed. For unrelated textures, however, this correspondence is arbitrary: a crack at one location has no particular relationship to a fiber at the same location in another image. We study whether this hidden pairing choice is itself a major determinant of interpolation quality. We represent ...

---

### 38. Kwai Summary Attention V2 Technical Report

**Authors:**  OneRec Team, Chenglong Chu, Guohong Mu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18654v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18654v1)

**Summary:** Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers with full attention to retain exact access to the original text. In such hybrid KSA-Full architecture, the interleaving inserted summary tokens are served as a streaming flow role across different layers. Although effective, however, it also introduce some bottlenecks: (1) the different layers summary compression chunk must ...

---

### 39. AMemOps: Evaluating Memory Updates in Long Audio Streams

**Authors:** Peiwei Chang, Li Zhang, Mark D. Plumbley, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18652v1)

**Summary:** Audio memory must recognise recurring sources across acoustic changes while keeping their attributes up to date. Overall accuracy does not reveal how these demands interact. We introduce Audio Memory Operations (AMemOps), a benchmark for latest-attribute retrieval, preservation of unchanged attributes and absent-source rejection in long audio streams. Paired controls vary recordings, training identities and earlier events to examine their effects on updating. Training on other recordings of the ...

---

### 40. Does Pretraining Teach Chemical Language Models Chemistry?

**Authors:** Leif Sieben, Yoel Zimmermann

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18651v1)

**Summary:** Chemical language models (CLMs) are pretrained on large corpora of molecules with the aim of learning representations that transfer to diverse downstream tasks. Here, we systematically study the effects of pretraining using a series of such CLMs across 64 molecular property prediction datasets. We find that the downstream gains of pretraining in CLMs do not scale and performance saturates below gradient-boosting baselines. Across the regimes evaluated, only supervised pretraining on traditional ...

---

### 41. Tiny Recursive Message Passing

**Authors:** Tommaso Salvatori, Matteo Forasassi, Alexis Toumi, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18649v1)

**Summary:** Message passing neural networks have shown remarkable performance in algorithmic and constraint reasoning, due to their ability to encode the structure of the task directly in the architecture. Recent work has shown that better results can be achieved using recursive transformers trained with deep supervision and truncated recursions, which make extremely deep loops stable to train, and equipped with test-time procedures such as discrete deduction lattices. In this work, we apply the same proced...

---

### 42. MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization

**Authors:** Yangchengyu Zhou, Zhiping Wu, Runchang Jiang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18642v1)

**Summary:** The Key-Value (KV) cache constitutes a dominant source of memory consumption during large language model (LLM) inference, particularly in long-context and complex reasoning scenarios. Existing KV cache quantization methods have explored different compression granularities, including layer-wise precision adjustment and token-level information preservation. In practical deployment, however, the key challenge is not merely compression, but how to allocate limited quantization resources among hetero...

---

### 43. To Align or Not To Align: Check Your COMPASS Before You Train

**Authors:** Fabian Gröger, Petar Damjanović, Maria Brbić

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18638v1)

**Summary:** Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a model pair will be compatible prior to alignment or merging. Building on the obs...

---

### 44. Grid or Nodes? Probing Object Memory in World Models Under Partial Observability

**Authors:** Justin McMillen, Yasin Yilmaz

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18637v1)

**Summary:** A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also sco...

---

### 45. Geometric Calibration of Supervised Fine-Tuning

**Authors:** Jianzhu Bao, Jia-Chen Gu, Qingyuan Liu, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18634v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18634v1)

**Summary:** Recent studies investigate the weight geometry through its spectral structure, which characterizes how the weights transform different input directions. Within this view, supervised fine-tuning (SFT) is shown to induce dense updates that perturb the spectral geometry of pre-SFT weights along their principal directions, potentially disrupting the model's prior knowledge. These observations motivate using the geometry of pre-SFT weights as a reference for refining learned SFT updates. We study thi...

---

### 46. MajorTOM:Elliot Pretrain, A Multi-Sensor, Multi-Temporal Pretraining Dataset for Earth Observation

**Authors:** Carmen Oliver Huidobro, Mikolaj Czerkawski, Kevin Monsalvez-Pozo, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18624v1)

**Summary:** Pretraining generalist Earth observation foundation models requires data that combine several sensors, varied temporal sampling and, increasingly, text, yet open datasets rarely provide all three in one consistent, easily accessible form. We introduce MajorTOM:Elliot Pretrain, a collection of 279,166 tiles of 10 km drawn from the Major-TOM grid by clustering AlphaEarth embeddings. Each tile stacks Sentinel-2 L1C, Landsat-8/9, Sentinel-1 RTC, Copernicus DEM and ESA WorldCover on a shared 1056x105...

---

### 47. Minimax rates for pointwise CATE estimation: the role of design smoothness

**Authors:** Yuxuan Hou, Zhenghan Li

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18623v1)

**Summary:** We study the role of design smoothness in the minimax estimation of conditional average treatment effects at a fixed covariate point. For design densities bounded above and away from zero, without further regularity, we derive upper and lower risk bounds with an arbitrarily small gap in the convergence-rate exponent. Under uniform design, we obtain matching upper and lower bounds at interior points in the regime of low nuisance smoothness. These results show that rough covariate designs can lead...

---

### 48. Deterministic Prediction as Global Velocity: Flow Matching for Probabilistic Time-Series Forecast

**Authors:** Jiajing Hu, Xu Han, Li-Ping Liu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18621v1)

**Summary:** Accurate uncertainty quantification is critical for many time series forecasting applications, and recent studies have increasingly adopted generative models to capture predictive uncertainty. Existing approaches often combine deterministic forecasting with generative modeling to improve predictive performance. However, their joint training is typically unstable because the deterministic model is embedded within the generative process, resulting in deep computational graphs and changing the prob...

---

### 49. Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents

**Authors:** Ashutosh Hathidara

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18614v1)

**Summary:** Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence is the natural candidate, but existing reinforcement learning methods calibrate it against the correctness of a decision at the current step. We propose a method to calibrate it again...

---

### 50. Does self-distillation improve reasoning?

**Authors:** Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18613v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18613v1)

**Summary:** Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement learning (RL), but it remains unclear whether these gains extend beyond in-distribution evaluations and whether they stem from privileged distillation. In this paper, we revisit two representative methods, Self-Distillat...

---

## cs.NE

**50 papers**

### 1. Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization

**Authors:** Bum Jun Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18085v1)

**Summary:** We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the m...

---

### 2. Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**Authors:** Francesco Panetta, Federico Di Valerio, Michela Proietti

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17998v1)

**Summary:** Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only expla...

---

### 3. Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation

**Authors:** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17969v1)

**Summary:** Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...

---

### 4. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 5. FidLIF: Parallel Training of High-Fidelity Spiking Neurons with Exact BPTT

**Authors:** Kaixiang He, Yujie Wu

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16924v1)

**Summary:** Although spiking neural networks (SNNs) show promise in energy-efficient computing through event-driven computation and stateful temporal processing, their recurrent membrane dynamics render their training inherently sequential and inefficient for long sequences. Existing methods achieve full-sequence parallelism in SNNs through two main strategies: redesigning or approximating spiking dynamics to avoid reset-coupled temporal dependencies, or relying on iterative relaxed fixed-point solvers that...

---

### 6. Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**Authors:** Huan Luo, Na Lu, Xiaopeng Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16921v1)

**Summary:** Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...

---

### 7. DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning

**Authors:** Yuxiang Zeng, Kun Xie, Yang Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16822v1)

**Summary:** Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...

---

### 8. naspaclust: A hybridisation of spatial fuzzy clustering with nature-inspired optimisation

**Authors:** Bahrul Ilmi Nasution, Rezzy Eko Caraka, Robert Kurniawan

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16356v1)

**Summary:** We present an overview of R package called \texttt{naspaclust}, a tool for spatial fuzzy clustering improvement by hybridising the Fuzzy Geographically Weighted Clustering (FGWC) with nature-inspired optimisation algorithms. There are seven optimisation algorithms in general, namely Artificial Bee Colony, Flower Pollination Algorithm, Gravitational Search Algorithm, Harris-Hawk Optimisation, Intelligent Firefly Algorithm, Particle Swarm Optimisation, and Teaching-Learning Based optimisation. The...

---

### 9. CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization

**Authors:** Yuqing Cheng, Yan Jia, Yanjie Song, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16158v1)

**Summary:** Conflict-graph search can stagnate despite effective operators when interventions fail to address the conflicts blocking progress. A disruptive intervention may also require further search before its value emerges. We propose CIPHEUR, a large language model (LLM)-guided framework that connects conflict evidence to coordinated intervention and recovery through Structured Intervention Units (SIUs). The shared control interface supports offline synthesis of executable policies and online contextual...

---

### 10. Where Polanyi Meets Galois: Tacit Knowing as an Algebro-Deterministic Operation, Toward Re-rooting AI-Generated Science

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16102v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16102v1)

**Summary:** We argue that tacit knowing is better modelled as an operating regime of one memory substrate than as a kind of content. The substrate is VaCoAl, an algebro-deterministic XOR-and-shift hyperdimensional memory over GF(2), realized as CASRAM (commercial SRAM-CAM) and PyVaCoAl (DRAM-CAM).In VaCoAl/PyVaCoAl a directed acyclic graph (DAG) reads two ways. Repairing every collision (Rescue mode) makes the trace exactly auditable but ranks no path higher; tolerating collisions (Don't Care mode) yields a...

---

### 11. How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility

**Authors:** Toru Takahashi

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15830v1)

**Summary:** When several predictions use the same internal representation, information about some targets can remain easier to recover than information about others. We study how this specialization forms, persists, and changes in minimal artificial learners. With reconstruction errors weighted equally during learning, changing which target is observed precisely selects the favored target and redirects an already specialized learner. Removing current support can reduce a formed bias, whereas state-following...

---

### 12. REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming

**Authors:** Abrar Alotaibi, Moataz Ahmed

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15513v1)

**Summary:** Safety-aligned large language models (LLMs) remain vulnerable to adversarial prompts that bypass their safety training. Existing automated red-teaming methods either require privileged access unavailable in production, rely on manually engineered per-model templates, or optimize a single objective without population-level diversity. We present REPRO (Reflective Evolutionary Prompt Optimization), a pure black-box framework that discovers adversarial prompts through evolutionary optimization drive...

---

### 13. CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining

**Authors:** Ziteng Sui, Junfeng Xia, Wenhao Ye, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15450v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15450v1)

**Summary:** Functional magnetic resonance imaging (fMRI) commonly characterizes large-scale brain organization through functional connectivity (FC). However, an observed FC matrix is not a fixed brain graph but a statistical estimate determined by the finite BOLD frames used to compute it. Conventional FC-based approaches typically represent each scan with a single Pearson-correlation matrix, leaving frame-resolved variations in regional interactions unexploited. To address this limitation, we introduce CoF...

---

### 14. FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies

**Authors:** Yifeng Mao, Yuze Feng, Yutong Shen, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15307v1)

**Summary:** Efficient neural architecture search (NAS) requires accurate performance estimation under limited evaluation budgets. Existing zero-cost proxies (ZCPs) provide fast training-free signals, but each proxy usually captures only a partial property of an architecture, leading to unstable rankings across datasets and search spaces. In contrast, GNN-based predictors can improve accuracy, but often depend on labeled architectures, graph encoders, and costly representation learning, which makes them less...

---

### 15. Compute-Optimal Scaling Laws for Spiking Language Models

**Authors:** Dan Saunders, Benjamin Ren, Catherine He

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15146v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15146v1)

**Summary:** Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N...

---

### 16. RELAGRAM: Recursive Latent Graph Model for the Capacitated Vehicle Routing Problem

**Authors:** Vladimir Kirill Bickov, Neil Yorke-Smith

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15106v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15106v1)

**Summary:** Latent recursion repeatedly processes internal representations through the same neural network. Recent work has shown this approach to be effective on structured reasoning tasks such as Sudoku and maze solving. However, whether latent recursion can support neural routing remains unclear. We introduce RELAGRAM (Recursive Latent Graph Model), a novel approach that brings latent recursion to graph combinatorial optimization. RELAGRAM encodes a capacitated vehicle routing problem (CVRP) instance as ...

---

### 17. PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation

**Authors:** Alex Gower

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14409v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14409v1)

**Summary:** Generating an image with a diffusion or flow-matching model typically involves integrating a velocity field for hundreds of sequential steps. That computation suits a GPU poorly and an analog neuromorphic substrate well, where one fast, low-power physical relaxation could replace the whole sequence. Two things are needed: a generative algorithm whose computation is a relaxation, and a way to train it without backpropagation, whose global gradient transport is hard to realise in analog. Energy Ma...

---

### 18. Do Artificial Neural Networks Need Dendritic Nanotubes? Two Reasons for Shrinking Importance Estimates in Continual Learning

**Authors:** Saurav K. Aryal

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.14258v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14258v1)

**Summary:** Regularization-based continual learning protects each parameter in proportion to an estimate of its importance, yet these estimates come from finite samples and heuristics and are used as if they were exact. We report four studies that start from a biologically inspired mechanism and end with a statistical explanation of it. Motivated by dendritic nanotubes, we let transient lateral links diffuse importance tags between hidden units. Links between co-active units gave no significant gain, but ra...

---

### 19. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 20. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 21. REMBGO for Evaluation-Limited Optimization: CEC2022 Benchmarking and EAF-STATCOM Generalization

**Authors:** Vikram Chekuri, Narapareddy Ramarao, Prashanth N A

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13471v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13471v1)

**Summary:** Metaheuristic comparisons are often reported at evaluation budgets far larger than an expensive engineering simulation can afford. This paper presents REMBGO, an evaluation-budget-aware refinement of EMBGO. Its contribution is not any single operator: it is the integration of population preservation, scale-normalized exploration and recovery mechanisms whose parent-relative benefit is concentrated under restricted function-evaluation budgets. REMBGO is evaluated on CEC2022 at a primary, applicat...

---

### 22. The value of information and the emergence of communication in evolved e-puck robots

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13118v1)

**Summary:** We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Em...

---

### 23. Universal Construction and Exact Self-Reproduction in Ternary McCulloch-Pitts Networks

**Authors:** Charles C. Norton

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12251v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12251v1)

**Summary:** A fixed network of McCulloch-Pitts threshold units with weights in {-1,0,1} can hold other threshold networks in its state and run them: the state is a ring of banks of records, each record a unit of a stored network, and each step evaluates one record. We use such a network to carry out von Neumann's universal construction and self-reproduction exactly. As a cellular automaton keeps its rule, the fixed network keeps its weights, and what reproduces is a stored network. A constructor of 143 reco...

---

### 24. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

**Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12183v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12183v1)

**Summary:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their resul...

---

### 25. EliteTable: Self-Improving Program Search for Executable Control Policies

**Authors:** Stuart Farmer

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12536v1)

**Summary:** EliteTable is a self-improving program-search algorithm guided by large language models (LLMs) that uses a fixed-capacity table of high-scoring solutions to guide new proposals, edits of existing solutions, and remixes of several solutions. Performance was evaluated across six Gymnasium control tasks, each with ten generations and fifty candidate slots per generation. Each task was evaluated across ten independently initialized searches. Candidate-score medians rose between the first and final g...

---

### 26. Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating

**Authors:** Lechen Li, Rongye Shi, Wanhuan Zhou

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11546v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11546v1)

**Summary:** Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architectures or fixed switching rules, resulting in disjointed search phases. To address this, this study proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-...

---

### 27. Evolutionary Architecture Search for Chlorophyll-$a$ Prediction in Lakes using Sentinel-2

**Authors:** Kursat Komurcu, Linas Petkevicius

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10496v1)

**Summary:** Small tabular datasets with expert-designed spectral features are the norm in   operational Earth observation, and the networks applied to them are typically   hand-designed. We revisit one such published model -- a Sentinel-2 algal   bloom classifier -- and ask what architecture search adds, holding the task,   the features and the lake-level train/test split of the original study fixed.   Searching an extended multilayer-perceptron space with regularized evolution,   and selecting on inner-cro...

---

### 28. Evolve on the Host, Predict on the Edge: Deploying Online Neuroevolutionary Architecture Search for Cross-sectional Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10038v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10038v1)

**Summary:** Accurate forecasting models are usually large, expensive to update online, and fixed in architecture once trained. We apply ONE-NAS, an online neuroevolutionary architecture search that evolves a population of small recurrent networks as each window of data arrives, to daily cross-sectional stock return prediction, and pilot it on a host and endpoint pipeline: the host runs the search and ships each generation's champion genomes over TCP/IP to a Raspberry Pi 4B, which predicts online. On the Pi ...

---

### 29. The Modular CMA-ES: A Framework for Modern Evolution Strategies

**Authors:** Jacob de Nobel, Diederick Vermetten, Anna V. Kononova, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09699v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09699v1)

**Summary:** Since their introduction, modern evolution strategies, such as the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), have become established as powerful methods for continuous black-box optimization. This success has led to a wide range of proposed modifications, each designed to improve performance or behavior in specific optimization scenarios. However, because these developments have largely been introduced and studied in isolation, their interactions remain comparatively underexplore...

---

### 30. Relocating Nonlinearity: How a Downstream Learner Reshapes What Genetic Programming Must Evolve

**Authors:** Nam H. Le

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09347v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09347v1)

**Summary:** Genetic programming was conceived as a way of evolving solutions: the program is the answer, and fitness is the error of its own output. A substantial line of work instead makes the program an input to a separate learner, so fitness measures the learner's output rather than the program's. Which learner to attach matters, with no account of what decides it. What makes a target hard for genetic programming is how much nonlinearity the program must build by composing primitives; whatever nonlineari...

---

### 31. Evaluating the Transfer of Co-Evolved Communication from 2D to 3D Simulation

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09280v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09280v1)

**Summary:** This work examines the transfer of a co-evolved communication mechanism between two robotic agents from a discrete two-dimensional (2D) simulator to a three-dimensional simulator with real physics (3D). The study focuses on whether a communication mechanism co-evolved in a 2D environment retains its functional role after transfer to a 3D physics-based simulator. To support this analysis, the effects of the episode time budget, the social cue, and the asymmetry between the two co-evolved roles we...

---

### 32. A Connectome Test of the Fly Hashing Algorithm

**Authors:** Sebastian Senge

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.09114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09114v1)

**Summary:** Dasgupta, Stevens and Navlakha (2017) showed that the Drosophila olfactory circuit, modelled as a random sparse projection followed by winner-take-all, is a locality-sensitive hash that beats classical LSH. The projection was random because the wiring was unknown. We test it against four electron-microscopy connectomes (MaleCNS, hemibrain, FlyWire, BANC; four animals, seven hemispheres). First, the 2017 pattern holds in a reimplementation of its protocol on SIFT, MNIST and odour mixtures (GloVe ...

---

### 33. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 34. Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design

**Authors:** Marcus Vukojevic, Erik Nielsen, Veronica Lachi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08367v1)

**Summary:** Several discrete design tasks, such as molecular discovery, require diverse collections of useful candidates at low computational cost. High validity alone does not guarantee a useful candidate library: repeatedly generating the same valid structures leaves few distinct alternatives. Training for both feasibility and diversity is challenging because many relevant criteria can only be evaluated after hard decoding. To address this challenge, we propose EGO (Evolutionary Generators with One-step i...

---

### 35. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 36. Energy-Efficient Spiking Neural Networks for Sensing-Aided Beam Prediction

**Authors:** Nhan Thanh Nguyen, Phuong Nam Tran, Mengyuan Ma, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.12507v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12507v1)

**Summary:** Sensing-aided beam prediction can reduce the beam-training overhead of millimeter-wave (mmWave) systems by leveraging environmental information from complementary modalities such as vision and position. However, the resulting sensing and inference pipeline can be energy-intensive, motivating the use of energy-efficient spiking neural networks (SNNs) as an alternative to conventional artificial neural networks (ANNs). In this work, we develop SNN architectures for beam prediction and systematical...

---

### 37. Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07825v1)

**Summary:** Time series forecasting models are typically compared on pointwise error, which scores a prediction in isolation from the decision it is produced for, and a lower forecast error does not imply a better decision downstream. A parallel debate asks whether modern transformer architectures forecast better than recurrent and other lightweight models. We compare linear, fixed recurrent, transformer, and mixing based architectures against recurrent networks evolved by neuroevolutionary architecture sea...

---

### 38. Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks

**Authors:** Zijie Xu, Bingrui Guo, Yiding Sun, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07808v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07808v1)

**Summary:** Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices. In value-based RL, deep spiking Q-networks (DSQNs) combine such efficiency with action-value estimation for decision making. However, existing DSQNs often require multiple simulation timesteps for competitive performance, increasing computational and energy costs, whereas reducing the timesteps can cause substantial performance degra...

---

### 39. Simplified Swarm Optimization for Surrogate-Assisted Reliability Design of Insulated-Gate Bipolar Transistor Power Modules Using an Open-Source Process Finite-Element Model

**Authors:** Wei-Chang Yeh

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07412v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07412v1)

**Summary:** Process-induced warpage, ceramic stress and solder strain limit the reliability of insulated-gate bipolar transistor (IGBT) modules on direct-bonded copper (DBC) substrates. Surrogate-assisted design studies train regression models on finite-element analysis (FEA) databases, but rarely check the optimized designs against new FEA or report how surrogate error interacts with the optimizer. This paper builds and evaluates an open pipeline: an open-source process finite-element model, surrogates tun...

---

### 40. Synapse Loss Estimation for the BrainScaleS Wafer-scale Neuromorphic System

**Authors:** Bernhard Vogginger, Christian Mayr

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07321v1)

**Summary:** Neuromorphic hardware combines memory (synapses) and computation (neurons) into the same silicon substrate to avoid the von-Neumann bottleneck. This way, neuromorphic computing aims to make computational neuroscience simulations and AI processing faster and more energy-efficient. The common crossbar architecture integrates a synapse matrix (analog, mixed-signal or digital) with a neuron array into a neurosynaptic core, whereas multiple cores are interconnected via a dedicated spike routing netwo...

---

### 41. Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design

**Authors:** Álvaro Díez, Fidel Aznar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06400v1)

**Summary:** Swarm robotics presents a robust and cost-effective paradigm for advanced automation in complex, dynamic environments, such as those encountered in search and rescue or environmental monitoring. A fundamental challenge for this field is the data-driven design of decentralized controllers capable of generating emergent collective behaviors. This paper proposes a novel, AI-driven hybrid methodology for the automatic synthesis of swarm robotic controllers for autonomous visual navigation. This appr...

---

### 42. A Flexible and Generic Approach for Explainable Landscape Analysis and the pyXla Toolbox

**Authors:** Tony Ombaso, Anna S. Bosman, Arnaud Liefooghe, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06359v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06359v1)

**Summary:** Landscape analysis has been successfully applied to understand complex optimisation problems, gain insights into algorithm behaviour, and automate algorithm selection and configuration. Although many landscape analysis techniques have been developed over the last decades, it remains difficult for researchers and practitioners to decide which approaches are appropriate and to implement them in practice. Some tools are available, but these are either restricted to particular problem domains (e.g.,...

---

### 43. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 44. Optimization Geometry of QAOA and Variational Quantum Algorithms

**Authors:** Vojtěch Novák, Ivan Zelinka, Silvie Illésová, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05524v1)

**Summary:** Variational quantum algorithms turn choices of Hamiltonian, ansatz, and parameterization into a classical nonconvex optimization problem. We study how this objective function can be visualized and characterized in ways that help explain optimizer behavior. We distinguish two properties of the objective: the number of local minima encountered along sampled directions and the differences in quality among local-search endpoints. We then ask how a local optimizer, represented by BFGS, compares with ...

---

### 45. AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding

**Authors:** Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05334v1)

**Summary:** Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests t...

---

### 46. MOXIE: Discovering Alternative Explanations for Biomedical Image Classifiers

**Authors:** Abiha Tahsin Chowdhury, Rahul Dubey

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04814v1)

**Summary:** Segment-based explanation methods such as LIME return a single explanation for each prediction, computed from one fixed image segmentation. This hides two important facts: a prediction can be supported by many different sets of image segments, and the segmentation itself shapes which explanations can be found. We introduce MOXIE (Multi-Objective eXplanation Imaging Engine), an evolutionary framework that searches for segment subsets that preserve the classifier's confidence while keeping as litt...

---

### 47. Active-DiNTS: Active Differentiable Network Topology Search

**Authors:** Gean Trindade Pereira, Thierry Urruty, Muriel Visani, et al.

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04787v1)

**Summary:** Neural Architecture Search (NAS) has proved to be a strong alternative to manual network design, but applying it to 3D medical image segmentation is limited by two well-known costs, large annotation budgets and multi-GPU clusters. Thus, this paper introduces Active-DiNTS (Active Differentiable Network Topology Search), an approach that embeds pool-based Active Learning (AL) into a bi-level differentiable topology search to perform architecture discovery and label curation jointly. At each query ...

---

### 48. Robust Optimization of Spring Design under Variable Manufacturing Tolerances

**Authors:** Grzegorz Sroka, Slawomir T. Wierzchon

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04656v1)

**Summary:** A reliable assessment of an optimizer robustness requires tracking controlled changes in parameters to identify sources of algorithmic weakness. Such an approach was applied to the problem of designing tension/compression springs with three continuous variables describing the spring geometry.   Three additional independent binary parameters reflect material variability, manufacturing-related geometric deviations, and an additional safety margin. Without expanding the decision space, these parame...

---

### 49. Chance-Constrained Bi-Objective Evolutionary Optimization for the Open-Pit Mining Operational Planning Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04227v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04227v1)

**Summary:** Open-pit mining operational planning involves allocating limited resources while satisfying production, equipment, and ore-quality requirements. Existing approaches often assume deterministic ore grades or rely on simulation-based evaluation under uncertainty. In this paper, we propose a chance-constrained bi-objective formulation of the open-pit mining operational planning problem under uncertain ore grades. We aim to maximize ore production and minimize fleet cost while satisfying stochastic q...

---

### 50. Adaptive Operator Selection in Bilevel Large Neighborhood Search for Electric Autonomous Dial-a-Ride Problem under Uncertainty

**Authors:** Ishara Hewa Pathiranange, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04219v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04219v1)

**Summary:** The electric autonomous dial-a-ride problem (EADARP) extends the classical dial-a-ride problem by incorporating battery and charging constraints for electric vehicles. In practice, travel-time uncertainty can cause violations of time-window constraints. Large neighborhood search is effective for solving the EADARP, but its performance can depend on the choice of insertion operator during the repair phase. This paper investigates insertion-operator selection within a bilevel large neighborhood se...

---

## q-bio.NC

**50 papers**

### 1. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 2. Sense-Making phase transition framework for Affect

**Authors:** Miguel Bosch, Laura Fanfarillo, Gustavo Diez, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18115v1)

**Summary:** Contemporary accounts of affect emphasize different perspectives, ranging from the regulation of bodily states in allostatic approaches to the relational and sense-making character stressed by enactive theories. Here, we show that affect can be made explicit within the sense-making phase transition framework previously introduced for the perception of an inner sensation. Within this same formal structure, each stable minimum of the sense-making potential defines an affective state: its position ...

---

### 3. Rewiring of adult neural networks - learning from structural plasticity across multiple scales

**Authors:** Michael Fauth, Han Lu, Jannik Luboeinski, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18024v1)

**Summary:** Synaptic connections are continuously formed and eliminated even in adult neuronal networks. This process - called structural plasticity - allows networks to change their topology to learn and adapt to their environment or compensate for lesions. Yet, in contrast to synaptic plasticity, structural plasticity is less well studied and understood. We here present the current state of knowledge as well as open problems in the field along three guiding questions: (1) What regulates structural plastic...

---

### 4. Rethinking World Models for Biosignals

**Authors:** Xianglong Bao, Bosong Huang, Xiaoda Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17510v1)

**Summary:** World models promise to learn how systems evolve and respond to actions, enabling simulation, planning and decision-making. Bringing this promise to biosignals requires more than accurate prediction of physiological recordings. We examine existing biosignal world models through two requirements for intervention use: a genuine action and evidence of its causal effect. We identify three fundamental bottlenecks rooted in physiology: Temporal Latency, the variable delay between an action and its obs...

---

### 5. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 6. Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models

**Authors:** Hanbo Xie, Yue Zhao, Robert C. Wilson

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17310v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17310v1)

**Summary:** Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptiv...

---

### 7. Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors

**Authors:** Farhad Pashakhanloo, Venkatesh N. Murthy

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17164v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17164v1)

**Summary:** The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 mo...

---

### 8. Simple model of neurogliovascular unit activity with noradrenaline leading force

**Authors:** Andrey Yu. Verisokin, Darya V. Verveyko, Alexey R. Brazhe, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15263v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15263v1)

**Summary:** In this work we present a model of a neuroglivascular unit associated with a neuronal ensemble. We combine calcium dynamics in the astrocyte, the cascade of synthesis of arachidonic acid and its derivatives, as well as the activity of the network of inhibitory and excitatory neurons with changes in local blood flow. We add equations to the model for extracellular neurotransmitters such as GABA, glutamate, and norepinephrine. We show that the resulting model can exhibit different types of behavio...

---

### 9. Predicting Cognitive Tasks from Single-Channel EEG through Task-Semantic Alignment

**Authors:** Ryota Kanai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15104v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15104v1)

**Summary:** Studies of data scaling in electroencephalography (EEG) and related noninvasive recordings suggest that simple wearable devices could eventually reveal more about cognitive states. However, publicly available EEG data are difficult to combine. Different laboratories record different tasks, participants, and devices. Task-agnostic self-supervised learning can exploit such data, but representations learned only with EEG signals have not consistently produced feature representations that are direct...

---

### 10. Bayesian adaptive design for neural recruitment curves

**Authors:** Vishweshwar Tyagi, Saihari S. Dukkipati, Daniel Twili, et al.

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15000v1)

**Summary:** Nonlinear response models remain ubiquitous across disciplines with recruitment curves describing muscle response to neural stimulation. Conventional acquisition methods typically rely on static uniform sampling, requiring many stimuli, while adaptive threshold-hunting designs such as ML-PEST forfeit accurate characterization of the overall curve. We present a Bayesian adaptive design that uses posterior uncertainty over curve parameters to propose stimuli that maximize information gain across t...

---

### 11. Full Lyapunov Spectra of Random Neural Networks, Part I: Finite-Time and Asymptotic Theory

**Authors:** Haoyu Albert Wang, Wei P. Dai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14922v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14922v1)

**Summary:** We develop a dynamical mean-field framework for the full finite-time and stationary asymptotic Lyapunov spectra of random recurrent neural networks. At finite observation time, an exact log-determinant representation of tangent-propagator singular values leads to a closed-contour matrix Dyson equation for the smoothed spectral tail. In the stationary setting, a cocycle representation yields an operator equation for the asymptotic cumulative spectrum. Both formulations retain complete local gain ...

---

### 12. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 13. EEG Entrainment to Non-Speech Rhythmic Patterns Associated with Dimensions of Language Performance

**Authors:** Francisco J. Martínez-Murcia, Nicolás J. Gallego-Molina, Marco A. Formoso, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13419v1)

**Summary:** Developmental dyslexia (DLX) affects 5-12% of the global population and impairs learning to read. Its biological basis, particularly the difficulties observed in oral phonological tasks, remains debated. Entrainment, the coupling of brain oscillations to speech rhythms, is essential for encoding phonological representations. We investigated whether brain entrainment to non-speech rhythms could predict DLX in 48 participants listening to white noise amplitude-modulated at rates matching Spanish s...

---

### 14. Beyond Anxiety and Avoidance: A Dynamic Feedback-Regulation Framework for Adult Romantic Attachment

**Authors:** Mateusz Pomianek

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13312v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13312v1)

**Summary:** Adult attachment is commonly represented by attachment anxiety and avoidance, but these person-level dimensions do not by themselves specify how momentary relational conditions are perceived, compared with desired conditions, translated into action, and updated after interpersonal feedback. We present the Attachment Regulation and Control (ARC) framework as an integrative feedback-regulation account that makes these temporal assumptions explicit and empirically testable. In ARC, control refers t...

---

### 15. Excitability across scales: a unifying EI model

**Authors:** Thomas S. J. Burger, Rodolphe Sepulchre

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13275v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13275v1)

**Summary:** Neuronal excitability is commonly modeled using different principles at the cellular and population scales, making it difficult to study how microscopic mechanisms shape macroscopic activity. We introduce a spatiotemporal excitatory-inhibitory (EI) model that unifies these scales through a common mixed-feedback architecture. The model retains the conductance-based circuit structure of Hodgkin-Huxley models and describes intrinsic and synaptic currents through memductances whose temporal and spat...

---

### 16. FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model

**Authors:** Aashish Dhawan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13018v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13018v1)

**Summary:** Connectome-constrained neural networks make biological components directly accessible to intervention, but their mechanistic conclusions can still depend on the comparison model, intervention, circuit representation and trained solution. We stress-test these dependencies in flyvis, a \emph{Drosophila} motion-vision model, using its 50-model ensemble, task-matched causal CNN controls and replicated interventions. At the level of model behaviour, three-level reverse-phi reversal in flyvis is stron...

---

### 17. Energy, Information, and the Limits of Neuropsychiatric Classification

**Authors:** Farbod Khodadadi, Mina Kheirkhah, Bita Shariatpanahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.14095v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14095v1)

**Summary:** Importance: The search for reliable neuroimaging biomarkers of mental disorders has remained elusive despite decades of research. Why clinically consequential disorders yield weak neuroimaging separability remains unresolved. Drawing on statistical thermodynamics and the metabolic costs of neural coding, we propose that psychiatric disorders produce constrained deformations of a largely shared repertoire of brain activity patterns, limiting the class-specific information available for classifica...

---

### 18. Lyapunov spectrum of random neural networks

**Authors:** David G. Clark

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12426v1)

**Summary:** The Lyapunov spectrum of a nonlinear recurrent neural network with random asymmetric couplings is calculated in the limit $N\to\infty$. The calculation is based on a finite-$N$ identity that expresses the cumulative distribution of Lyapunov exponents as a response function of the tangent-space dynamics, with the tangent trajectory selected by a minimum-norm condition rather than by an initial condition. A cavity method then determines this response function at large $N$ through a self-consistent...

---

### 19. Neural Decoding as Cognitive Inference

**Authors:** Yi Guo, Changhong Jing, Yong Hu, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11923v1)

**Summary:** The brain maintains stable cognition despite continuously changing neural activity. How to extract stable cognitive states from variable neural observations remains a central problem in neural decoding. Existing neural decoding methods map neural observations to predefined external labels based on the stimulus-response principle, often capturing recording-specific spurious correlations. Inspired by how the brain infers the world, and specifically by Bayesian brain theory, we recast neural decodi...

---

### 20. Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy

**Authors:** Marko Tvrdic, Justin Richmond Domingo, Jae Ann Buenaluz, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11222v1)

**Summary:** Preclinical models poorly predict human drug efficacy, particularly in neurological disorders. Neural activity offers a uniquely rich source of translational information because it captures high-dimensional variation in nervous-system function that can be measured in both animals and humans. However, its high dimensionality makes it difficult to distinguish conserved disease-related features from variation arising from species, recording modality and experimental context. Here, we test whether s...

---

### 21. If the brain were so simple: Information-based drivers of intelligence and their interaction through an n-body-inspired framework

**Authors:** Brett J. Kagan, Johnson Zhou, Forough Habibollahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11142v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11142v1)

**Summary:** Theories of how the brain processes information and returns intelligent outputs are numerous and often difficult to conclusively test. Here, we consider an approach grounded in informatics and algorithmic thermodynamics for how neural systems respond to different patterns of information in different ways, with a focus on the relationship between the information entropy of a signal and a new proposed quantity we term information enthalpy, which represents the internal resource of structured infor...

---

### 22. Mean Field Theory Based on the Spike Time Response Curve for Synchronization Within and Between Two Alternating Populations of Neural Oscillators with Delays

**Authors:** Ananth Vedururu Srinivas, Carmen C. Canavier

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10977v1)

**Summary:** In order to study oscillators coupled by pulses emitted at discrete times, it is generally assumed that the effect of each pulse is an instantaneous phase shift, with a possible conduction delay between emission and receipt. However, we are interested in neural oscillators in which each pulse (action potential) activates a biexponential synapse, and at high frequencies, the duration of the synaptic conductance may be greater than the network period. Therefore, the effect of received pulses can s...

---

### 23. Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10850v1)

**Summary:** As AI models move toward clinical decision-making and personalized treatment, understanding \emph{what} a model learns is important beyond predictive accuracy alone. We investigate whether personalized latent dynamics reveal clinically associated differences even when predictive fit is similar. A lightweight CNN--Transformer EEG foundation model pretrained on the Temple University EEG Corpus (TUEG) extracts segment-level representations. Using the Temple University Epilepsy Corpus (TUEP), repres...

---

### 24. Learning infinite context windows in recurrent architectures via spatial neural computing

**Authors:** Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10690v1)

**Summary:** Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical...

---

### 25. Structure alone supports efficient visual computation in the Drosophila visual system

**Authors:** Eudald Correig-Fraga, Roger Guimerà, Marta Sales-Pardo

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10023v1)

**Summary:** Understanding the extent to which measured synaptic wiring determines computation remains a central challenge. Here, we couple the proofread adult Drosophila melanogaster connectome to an anatomically faithful model of its eye. Visual information is inputted in the eye model, then passed to the connectome, and finally read from a Kenyon-cell-centered linear decoder. This creates a connectome-only model in which the anatomical graph and eye geometry are fixed and only scalar synaptic gains and ne...

---

### 26. Feedback to the primary visual cortex is highly concentrated on the central visual field representation

**Authors:** Piotr Majka, Emmanuel K L Cho, Karolina Łabuszewska, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09983v1)

**Summary:** Retrograde tracer injections in marmoset monkeys revealed a striking feature of neural circuitry in primate visual system: among neurons projecting to the primary visual cortex (striate cortex, V1), the proportion of extrastriate feedback neurons relative to thalamic feedforward neurons decreases markedly with visual field eccentricity. This supports the Central-Peripheral Dichotomy theory, which proposes fundamentally distinct computational specializations --- visual recognition and attentional...

---

### 27. Do Generative Priors Align with Human Naturalness Perception?

**Authors:** Taiki Fukiage

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09928v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09928v1)

**Summary:** Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relation...

---

### 28. CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies

**Authors:** Gabriel Ocana-Santero, Marko Tvrdic

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09643v1)

**Summary:** Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It ...

---

### 29. Predicting Long-Term ADAS-Cog Change From Early Response After Repetitive Transcranial Magnetic Stimulation in Alzheimer Disease

**Authors:** Mohammad Alamgir Chowdhury, Hina Shaheen

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09629v1)

**Summary:** Early cognitive response after repetitive transcranial magnetic stimulation (rTMS) may predict later cognitive change in Alzheimer disease, but the incremental value of domain-specific response is unclear. We analyzed data from 112 randomized participants; 101 entered a Week-5 landmark cohort and 91 had complete predictors and outcomes at 8, 16, and 24 weeks post-treatment. Nested predictor-set comparisons used ridge regression to evaluate baseline information, trial variables, early total-score...

---

### 30. Connectome-Based Modeling of Mutation-Specific Amyloid-$β$ Aggregation in Familial Alzheimer's Disease

**Authors:** Mohammad Alamgir Chowdhury, Hina Shaheen

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09583v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09583v1)

**Summary:** Familial amyloid-$β$ (A$β$) variants alter aggregation kinetics, but their interaction with structural brain connectivity remains incompletely understood. We developed a mutation-aware mechanistic model coupling a coarse-grained monomer--oligomer--fibril aggregation--fragmentation system to graph diffusion on the 540-node Budapest Reference Connectome component. Experimental A$β_{42}$ nucleation scores scaled primary nucleation rates for seven variants relative to wild type. Robustness was exami...

---

### 31. Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding

**Authors:** Moein Khajehnejad, Michelangelo Tronti, Forough Habibollahi, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09352v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09352v1)

**Summary:** Visual decoding from fMRI is typically siloed by participant and experiment, obscuring whether heterogeneous neural measurements can be organized within a common computational geometry. Here we introduce BRAID-fMRI (Brain Representation Alignment across Individuals and Datasets), a shared CLIP-supervised decoding framework. BRAID-fMRI uses a single ROI-wise Transformer with optional participant conditioning across eight visual-fMRI datasets comprising 93 dataset-specific participant entries, 430...

---

### 32. MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI ADHD Classification

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09306v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09306v1)

**Summary:** Naturalistic movie-fMRI provides a shared, temporally structured probe of brain dynamics, yet predictive models commonly rely on whole-run functional connectivity (FC) or temporally generic representations that are not aligned with narrative events. We introduce MovieSTAGE (Scene, Transition, and Global Encoding), a multiscale framework that combines hypergraph-structured FC-profile organization within scenes, unsigned FC-profile differences across adjacent scenes, and whole-movie FC. We evaluat...

---

### 33. Scaling subjects in cross-modal alignment: video decoding with EEG foundation model

**Authors:** Dung Truong, Kuntal Kokate, Arnaud Delorme

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09287v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09287v1)

**Summary:** Naturalistic visual decoding from EEG has long been constrained by cohort size: existing scaling literature caps out at a few dozen subjects, leading prior work to conclude that scaling subject cohorts yields minimal performance gains. Training a cross-modal EEG--video contrastive encoder on a cohort larger by more than an order of magnitude, we find the axis is productive but has an onset. Below $S\approx50$ --- the entirety of the range prior work occupies --- no model improves meaningfully ov...

---

### 34. A Connectome Test of the Fly Hashing Algorithm

**Authors:** Sebastian Senge

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.09114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09114v1)

**Summary:** Dasgupta, Stevens and Navlakha (2017) showed that the Drosophila olfactory circuit, modelled as a random sparse projection followed by winner-take-all, is a locality-sensitive hash that beats classical LSH. The projection was random because the wiring was unknown. We test it against four electron-microscopy connectomes (MaleCNS, hemibrain, FlyWire, BANC; four animals, seven hemispheres). First, the 2017 pattern holds in a reimplementation of its protocol on SIFT, MNIST and odour mixtures (GloVe ...

---

### 35. Language-model ratings of depression reflect the rater more than the patient

**Authors:** Baihan Lin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08501v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08501v1)

**Summary:** Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...

---

### 36. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 37. A Time-Resolved Framework for Quantifying Neuronal Network State Transitions

**Authors:** Ilya Auslender, Yasaman Heydari, Asiye Malkoç, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08392v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08392v1)

**Summary:** Electrophysiological recordings provide powerful tools for characterizing the dynamics of neuronal networks. In vitro neuronal cultures offer a controlled setting for investigating network responses to diverse interventions, including pharmacological and optogenetic stimulation. However, conventional analyses often reduce electrophysiological activity to aggregate measures calculated over fixed temporal windows, providing only a static representation of the network state. Here, we introduce a co...

---

### 38. Confidence-Ordering Reversal under Contextual Priors in Neural Decoding

**Authors:** Xinyu Zhang, Sichao Liu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08229v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08229v1)

**Summary:** Contextual priors improve neural-to-language decoding by reshaping candidate scores. However, confidence is read from the same reshaped scores, so the errors a prior leaves behind can become more confident with no change in accuracy to reveal it. We study how a prior shapes confidence in speech retrieval on MEG-MASC and MOUS using local decoding scores, a contextual prior combined by additive shallow fusion, and the fused top-two margin as confidence. Among initially incorrect predictions, we fi...

---

### 39. Neural networks as decision trees: an analytical solution for learning and neural selectivity

**Authors:** Hugo Tissot, Jonas Ranft, Yves Boubenec

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08228v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08228v1)

**Summary:** Nonlinear neural networks develop structured internal representations, yet how their geometry is determined by the tasks being learned remains poorly understood. Here, we develop an analytical framework for piecewise-linear feedforward and recurrent networks that links learning, activation-region structure, and neural selectivity. We show that, at any stationary point of gradient-aligned learning, a nonlinear network decomposes into local linear regressions over its activation regions. Deviation...

---

### 40. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 41. CANDLE: Cortical Null-Space Decomposition for Noninvasive Brain Source Imaging

**Authors:** Shuntaro Suzuki, Yuiga Wada, Komei Sugiura

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07824v1)

**Summary:** Electrophysiological source imaging (ESI) aims to estimate cortical source activity from noninvasive electrophysiological measurements such as electroencephalogram (EEG). However, ESI is fundamentally ill-posed because source activity is substantially higher-dimensional than sensor observations, resulting in non-unique solutions. Recent learning-based approaches address this ambiguity by learning data-driven source priors, yet they often struggle to generalize across subject-specific cortical ge...

---

### 42. Interplay between Excitability and Noise in Analog Spiking Neurons

**Authors:** Léopold Van Brandt, Alon Ascoli, Michele Bonnin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06720v1)

**Summary:** A spiking neuron is a dynamical system exhibiting a limit cycle (a spike) when subject to sufficiently excitatory input. Famous neuroscience experiments by Bryant and Segundo as well as Mainen and Sejnowski revealed that the spike times of some biological neurons are more reliable when subject to time-varying stimuli compared to constant ones. Provided with an industrial physics-based transient noise SPICE simulation framework compatible with foundry transistor compact models, we have demonstrat...

---

### 43. COMPASS 2.0: psychometric representational similarity analysis distinguishes symptom structure from personal signal

**Authors:** Baihan Lin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06615v1)

**Summary:** Language models can score psychiatric questionnaires from speech, but agreement with self-report may reflect the questionnaire rather than the person. We introduce psychometric representational similarity analysis, a framework for comparing the structure of speech-derived scores, self-report, item wording and theory, and implement it alongside person-level construct scoring in COMPASS 2.0. We show how similarly worded items induce covariance without psychological signal. In pre-registered discov...

---

### 44. NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI

**Authors:** Felix Nieto-del-Amor, Jingru Fu, J. -Sebastian Muehlboeck, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06502v1)

**Summary:** Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.   Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 corti...

---

### 45. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 46. CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05913v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05913v1)

**Summary:** Task-fMRI connectomes reveal state-dependent neural reconfigurations, yet conventional methods marginalize these signals by aggregating distinct conditions into static pairwise graphs, thereby obscuring condition-specific multi-ROI organization. We introduce CoHyFuse, a condition-aware ROI-centered hypergraph framework that constructs a task-state-specific incidence matrix from condition-wise functional connectivity (FC)-profile embeddings, allowing the same ROI to form different multi-ROI hyper...

---

### 47. Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05503v1)

**Summary:** Large-scale EEG foundation models have demonstrated promising transferability across neurological disorders, but often require millions of parameters and substantial computational resources. In this paper, we present the Universal Semantic EEG Foundation Model (USE-FM), a lightweight EEG foundation model that learns transferable neural representations through self-supervised signal reconstruction on the Temple University Hospital EEG Corpus (TUEG). After pretraining, the encoder is frozen and ev...

---

### 48. Recurrent network dynamics explain the time course of perceptual grouping in natural scenes

**Authors:** Sami Mollard, Alekh K. Ashok, Lore Goetschalckx, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05419v1)

**Summary:** How the brain groups image elements into coherent objects in natural scenes remains unclear. Existing models for grouping in biological vision rely on simplified stimuli with explicit boundaries and cannot explain human behavior in naturalistic settings. We propose a mechanistic framework in which recurrent interactions propagate enhanced neuronal activity within and between cortical areas. The framework links computational principles, neural circuitry and perceptual psychology. Local boundary s...

---

### 49. Efficiency and robustness partition the solution space for memory in recurrent networks

**Authors:** William Qian, Cengiz Pehlevan

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04697v1)

**Summary:** In computational neuroscience, task-trained recurrent neural networks (RNNs) are commonly used as a testbed for exploring the space of recurrent circuit solutions compatible with a particular function. However, these networks are subject to inductive biases that may be misaligned with those of biological circuits, which operate under various efficiency and robustness constraints. Here, using a minimal stimulus recall task, we systematically characterize how the solution space of recurrent neural...

---

### 50. Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command

**Authors:** Luiz Pessoa, Andrea Gambarotto

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04643v1)

**Summary:** Neuroscience treats the brain as a control hierarchy, with cortical systems governing subcortical mechanisms. We argue that this mistakes a configuration for an architecture. Local asymmetries of influence are real, but control is relational and process-specific; because neural elements constrain one another across concurrent processes, relations can form cycles that resist a stable ranking. Evidence from learned action, cortico-cerebellar and thalamocortical loops, and defensive behavior shows ...

---

## stat.ML

**50 papers**

### 1. Joint Neural Posterior Estimation and Model Selection for Chemical Reaction Networks

**Authors:** J. Arturo Esquivel, Jorge A. Campos-Gonzalez-Angulo, Sergio Pablo-García, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18825v1)

**Summary:** Simulation-based Bayesian inference for Chemical Reaction Networks (CRNs) must simultaneously solve two computationally demanding problems: discriminating between overlapping reaction pathways and estimating reaction rate constants. Classical approaches, such as Sequential Monte Carlo ABC, rely on handcrafted summary statistics and scale poorly across large parameter spaces. To overcome this, we introduce a neural inference architecture. Our pipeline utilizes shared 1D-CNNs and a permutation-inv...

---

### 2. Designing for Prediction: Planning Formulas for Expected Out-of-Sample $R^2$ and $r$

**Authors:** Elizabeth Tipton

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18781v1)

**Summary:** Design calculations let researchers gauge, before data is collected, whether a planned study is likely to detect an effect. In this paper, we develop such calculations for predictive models using ordinary least squares and ridge regression under leave-one-out cross-validation. To do so, we derive closed-form expressions relating the expected out-of-sample $R^2$ and the expected correlation between observed and predicted outcomes to four design-stage quantities: sample size, number of predictors,...

---

### 3. A Rate Transfer Method: Convergence Rates in Stochastic Gradient Descent via Stochastic Calculus

**Authors:** Neil Walton

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18739v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18739v1)

**Summary:** We develop a rate-transfer method that converts finite-time Lyapunov estimates for an associated stochastic differential equation (SDE) into finite-time convergence bounds for stochastic gradient algorithms. Under generic moment and smoothness conditions, the convergence analysis of the stochastic gradient method reduces to a calculus argument verifying a Lyapunov generator inequality for the SDE. The method recovers established rates for classical stochastic gradient methods and provides a way ...

---

### 4. From Fourier Amplitudes to Persistence Images for Impact-Echo Defect Detection

**Authors:** Keunsu Kim, Suyoung Choi, Meiyan Kang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18732v1)

**Summary:** Impact-echo testing is a nondestructive testing method used to detect internal defects in concrete structures. However, boundary reflections, structured interference, and measurement noise can produce complex Fourier amplitude spectra, making defect classification difficult. We constructed a two-dimensional frequency--amplitude persistence image (FA-PI) from the Fourier amplitude spectrum. Using a fixed parameterization of exact multi-parameter persistent homology, each retained Fourier componen...

---

### 5. BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling

**Authors:** Mengyu Li, Qianqian Qu, Jun S. Liu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18658v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18658v1)

**Summary:** Generative models are often required to serve many downstream conditional tasks. In the training-free setting, a pretrained unconditional model is reused as a prior and combined with a task-specific likelihood to sample from the corresponding posterior. While such training-free samplers have been developed for diffusion and flow models, their counterpart for Schrödinger bridge (SB) models remains unexplored, despite the growing appeal of SBs as flexible stochastic transport models between genera...

---

### 6. Minimax rates for pointwise CATE estimation: the role of design smoothness

**Authors:** Yuxuan Hou, Zhenghan Li

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18623v1)

**Summary:** We study the role of design smoothness in the minimax estimation of conditional average treatment effects at a fixed covariate point. For design densities bounded above and away from zero, without further regularity, we derive upper and lower risk bounds with an arbitrarily small gap in the convergence-rate exponent. Under uniform design, we obtain matching upper and lower bounds at interior points in the regime of low nuisance smoothness. These results show that rough covariate designs can lead...

---

### 7. Understanding Circulant Permutation to Extend the CMinHash Estimator

**Authors:** Keegan Kang, Avery Hood, Benedict H. W. Wong

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18551v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18551v1)

**Summary:** CMinHash promises a new direction for designing MinHash algorithms with reduced variance and storage space via circulant permutations. However, the original variance analysis is difficult to extend to other MinHash estimators. We present a new approach that gives explicit and easily comparable approximate variance expressions, and use it to analyze the Minner estimator. Numerical experiments show that our variance expression matches the empirical mean square error (MSE) of estimates. Our work th...

---

### 8. Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too

**Authors:** Mehdi Makni, Natalia Ponomareva, Rahul Mazumder

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18516v1)

**Summary:** Post-training pruning enables efficient deployment, but conventional methods do not explicitly preserve internal-gradient alignment between sparse and dense models. We study novel connections between downstream performance of compressed models and the ability to retain gradient information via influence-function preservation. Central to this connection is a curvature-aware objective that accounts for both layer activations and backpropagated gradients. Despite its promise, this objective remains...

---

### 9. How Low Can You Go: Fine-Tuning LLMs with Bayesian Optimization (LlMBO)

**Authors:** Aditya Kulkarni, Davide Sartor, Carlos Soto, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18504v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18504v1)

**Summary:** Recently, Morris et al. introduced TinyLoRA, a strategy for LLM fine-tuning which introduces arbitrarily few parameters, and demonstrated accuracy improvements using less than $10$ parameters rather than the ${\gtrsim 10,000}$ typically demanded by LoRA-based methods. However, that study continued to use gradient-based local search methods of the kind deployed for training multi-billion parameter LLMs in the first place. This article is predicated on the observation that, in the low dimensional ...

---

### 10. Recalibrating Many Questions with Few Labels: Minimax Rates and Identification Limits

**Authors:** Xiaoyu Li, Chiwun Yang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18488v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18488v1)

**Summary:** Many related prediction problems, which we call questions, come with few labels each. What information can be shared across them, and what is actually necessary for good decisions? We answer both for recalibration, motivated by decision models such as Jev (TypeSafe AI, 2026) that return a probability for any yes/no question a developer writes. A predictor reports a probability $P$ with output law $μ$ on $m$ questions, each with $n$ labels and a nondecreasing map $g_j(p)=\mathbb{P}(Y=1\mid P=p)$;...

---

### 11. Convergence-Rate-Guided Algorithm Design of Expected Improvement for Continuous Simulation Optimization

**Authors:** Songhao Wang, Jianglin Xia, Haowei Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18434v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18434v1)

**Summary:** Expected improvement (EI) based on stochastic kriging (SK) surrogate is widely used in continuous simulation optimization, but unknown heteroscedastic noise on simulation output makes three basic design choices consequential: the incumbent used to define improvement, the replication level at each sampled point, and the terminal recommendation. Existing methods typically either assume the noise levels are known or choose these components separately through heuristic rules or empirical calibration...

---

### 12. On the Optimality of Random Features under General Conditions: Misspecified Cases and Robust Learning

**Authors:** Caixing Wang

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18333v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18333v1)

**Summary:** Random features provide a standard approach to scaling kernel methods to large datasets by approximating the kernel with a finite-dimensional feature map. Existing works of random feature methods primarily focus on well-specified models and light-tailed noise conditions, leaving a gap in understanding their performance under more general conditions, such as misspecified models and heavy-tailed noise. In this paper, we provide a comprehensive and improved analysis of kernel ridge regression with ...

---

### 13. Operator Surrogates

**Authors:** Christoph Schwab, Josephine Westermann, Jakob Zech

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18210v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18210v1)

**Summary:** This chapter provides a mathematical introduction to operator surrogates, which are finite-parametric maps approximating complex (typically nonlinear) operators between infinite-dimensional (function) spaces.   A typical approach to constructing operator surrogates is the encoder-approximator-decoder paradigm, whereby infinite-dimensional inputs are mapped to a finite-dimensional latent space, processed, and then mapped back to the infinite-dimensional output space. We discuss various methods fo...

---

### 14. Hierarchical Time Series Forecasting with Operator-Valued Kernels

**Authors:** Junjie Yang, Adeline Fermanian, Claire Boyer, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18196v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18196v1)

**Summary:** Hierarchical time series forecasting requires generating accurate predictions that are coherent across multiple levels of aggregation. Existing methods either rely on two-stage pipelines with post-hoc reconciliation or on end-to-end models that often lack statistical guarantees. We introduce a unified framework that formulates hierarchical forecasting as a multivariate regression problem in a vector-valued reproducing kernel Hilbert space. By designing structured operator-valued kernels, our app...

---

### 15. Lifting Finite-Sample Gaussian Approximation of Wide Neural Networks to Functional Convergence

**Authors:** Luis Wiederhold, Nil Ayday, Debarghya Ghoshdastidar

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18166v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18166v1)

**Summary:** Randomly initialised neural networks of width $m$ converge to Gaussian processes as $m \to \infty$, with two types of quantitative bounds characterising this convergence. Finite-sample bounds compare the network with its Gaussian limit at a fixed finite sample set, on an arbitrary domain, in the quadratic Wasserstein distance $\mathcal W_2$, achieving a convergence rate of $m^{-1/2}$ with explicit constants. However, these constants grow with the number of samples, so the bound becomes uninforma...

---

### 16. Learning a Group Element from Its Action: Galois Correspondences, Optimal ERM, and an Abel-Ruffini Threshold for the Natarajan Dimension

**Authors:** Xiaoyu Li

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18154v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18154v1)

**Summary:** We study learning an unknown element $g$ of a group acting with finite orbits on a countable set, from examples $(x,gx)$. After a sample on $A$, the consistent hypotheses are the restrictions of a coset of the pointwise stabilizer of $A$, and the sample forces exactly the labels of points this stabilizer fixes; for a Galois group, they form the field generated by the data. Through this correspondence, multiclass dimensions become group invariants: the DS and graph dimensions equal the height, th...

---

### 17. Reliable Scale-Free Bandits via Empirical Likelihood

**Authors:** Pratham Gupta, Alhad Sethi, Shubhada Agrawal

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18055v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18055v1)

**Summary:** We study stochastic bandits without knowledge of reward scales or tail parameters. Almost-sure regret guarantees describe eventual learning but do not quantify expected performance or the risk of large regret in a finite run. We introduce $\texttt{EL-F}$, an anytime empirical-likelihood (EL) extension of the $g$-Forcing policy of Cowan and Katehakis (2020), and characterize its performance at three levels. First, for integrable rewards and non-decreasing, diverging exploration schedules $g$ with...

---

### 18. ndscape: a structural map of the nested dichotomy space

**Authors:** Maxwell Dix-Matthews, Melinda Hodkiewicz, Adriano Polpo

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18050v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18050v1)

**Summary:** Nested dichotomies (NDs) reduce multiclass classification to a tree of binary classifiers. Tree structure can change accuracy, bias, and variance, but the full space of structures has not been mapped in aggregate. We introduce ndscape, a two-dimensional mapping of ND structures based on depth-weighted structural tokens. We use this embedding to conduct what is, to our knowledge, the first bias-variance analysis across the ND structure space. In simulations with 6 to 10 classes, NDs with similar ...

---

### 19. Weighting-Based Strategies for Classification: Analysis and Local Peak Dynamics with CART Trees

**Authors:** Abdoulaye Sakho, Emmanuel Malherbe, Erwan Scornet

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18037v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18037v1)

**Summary:** Tabular learning tasks often suffer from class imbalance, which is often addressed via weighting-based strategies. In this work, we compare the naive approach (unweighted) with the weighting-based rebalancing strategies. Somewhat surprisingly, we demonstrate that, asymptotically, as the predictor complexity increases with sample size, weighting strategies yield predictive performance identical to unweighted approaches across all evaluation metrics, up to a shift in the final threshold. To go bey...

---

### 20. Counterfactual Certification for Sequential Unlearning with Long-Run Performance Guarantees

**Authors:** Hanna Benarroch, Jamal Atif, Olivier Cappé

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17993v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17993v1)

**Summary:** Certified machine unlearning ensures the proximity between the unlearned model and a model retrained without the data to be forgotten. Extending this framework to sequential deletion requests, typically arriving as groups of variable size (e.g., all records of one user or of coordinated users), is challenging. For unlearning methods based on fine-tuning on the retain sets, this leads to either degrading performance or increasing computation as the number of unlearning requests grows. For indepen...

---

### 21. Learning Distributions from Samples and Qualities

**Authors:** Marc Jourdan, Nicolas Flammarion

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17956v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17956v1)

**Summary:** We study parameter estimation when each sample from a continuous parametric distribution is accompanied by a binary quality label governed by the same unknown parameter. By imposing hard feasibility constraints, deterministic labels can accelerate estimation from the classical $n^{-1/2}$ rate of smooth quality-aware M-estimators to $n^{-1}$. Combining PAC guarantees with local error-to-parameter conversions, we establish this rate for both identifiable and finitely ambiguous quality classifiers,...

---

### 22. Follow the Perturbed Leader for Linear Bandits: $\sqrt{T}$ Regret over General Convex Sets

**Authors:** Chen-Yu Wei

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17818v1)

**Summary:** We give the first adversarial linear bandit algorithm based on Follow-the-Perturbed-Leader (FTPL) that achieves $\sqrt{T}$ regret over general convex action sets. Our algorithm attains $\widetilde{\mathcal{O}}(d^{5/4}\sqrt{T})$ regret using only linear optimization oracles, and the near-optimal $\widetilde{\mathcal{O}}(d\sqrt{T})$ regret when an optimal-design exploration distribution is further available. This improves on the $T^{2/3}$ regret of the FTPL algorithm of Dani and Hayes (2006) for g...

---

### 23. Linear Regression Beyond Covariance: Latent Slope Spectra from Higher-Order Cumulants

**Authors:** Anirban Nath, Ming Yuan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17772v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17772v1)

**Summary:** Least squares summarizes the joint distribution of a response and regressor through second-order information. When an observed regressor is composed of latent components carrying different relationships with the response, this summary can average over distinct linear effects. We study the additional linear information contained in higher-order mixed cumulants and formalize it through the latent slope spectrum. Ordinary least squares is a variance-weighted barycenter of this spectrum, whereas hig...

---

### 24. Gaussian Process Bandits for AI System Optimization with Selectively Verified Feedback

**Authors:** Shuang Wu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17760v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17760v1)

**Summary:** Gaussian process bandits exploit similarities among configurations to optimize prompts, retrieval systems, and agent workflows. In these applications, however, inexpensive model-based evaluations can disagree with trusted task outcomes. We study selective verification when an action is chosen before a diagnostic is observed and trusted feedback is informative on an unknown set of diagnostic states. A finite reliability class and a finite RKHS signal dictionary describe these two sources of uncer...

---

### 25. Structured SDEs for Realized GARCH: Continuous-Time Volatility Modelling and Component-Level Analysis

**Authors:** Hongyu Yao, Zhengyang Chi, Junbin Gao

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17732v1)

**Summary:** We propose a structured continuous-time stochastic volatility model for one-day-ahead integrated-variance forecasting. The model introduces a jointly evolving realized-measure state that feeds directly into latent variance dynamics, while correlated Brownian innovations capture return-linked dependence. Parameters are estimated through simulation-based predictive learning, and Monte Carlo simulation forecasts integrated variance. Across 17 equity indices, the proposed model shows strong out-of-s...

---

### 26. textGrain watermarking is harder to detect: can sum-tests still do it optimally?

**Authors:** Swapnaneel Bhattacharyya, Soham Bonnerjee

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17655v1)

**Summary:** Watermarking embeds an imperceptible signal in text from large language models that is statistically detectable with a secret key. The recent textGrain watermark (Li et. al. (2026b)) calibrates this signal against the model's sampling entropy through an explicit entropy budget, combining the stochasticity of Red-Green and the unbiasedness of Gumbel-max watermarks, and its accompanying report proposes a detector that sums pivotal statistics. We study when, and how efficiently, textGrain can be de...

---

### 27. Risk-Averse Inference-Time Diffusion Model Alignment with Finite-Sample Guarantees

**Authors:** Yuchen Liang, Xian Yu

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17579v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17579v1)

**Summary:** Inference-time alignment steers diffusion models toward downstream objectives without costly fine-tuning, but existing methods typically optimize expected cost (or reward) without explicitly controlling tail risk. In this work, we propose a risk-averse framework for inference-time alignment of diffusion models that balances expected cost and Conditional Value-at-Risk (CVaR) under trajectory-level Kullback-Leibler regularization. We characterize the optimal path distribution and reverse transitio...

---

### 28. Effect of Spherical Parameter Space on Number of Non-Forgetting Tasks and Capacity of Continual Learning

**Authors:** Nazanin Mirhosseini

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17453v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17453v1)

**Summary:** We propose a continuous learning formulation for $T$ non-forgetting tasks with the spherical parameter space $\mathbb{S}^{d-1}(\sqrt{d})$ in asymptotic regime $d\rightarrow \infty$. Each task $i$ has an optimum $\bmΘ_i$, minimizing its corresponding loss function $R_i(\bm{w})$ on sphere. We reduce each task $i$ to an acceptable loss region modeled by a geodesic ball $B_{\bmΘ_i}(r_i(d))$ on $\mathbb{S}^{d-1}(\sqrt{d})$ centered at $\bmΘ_i$ with radius $r_i(d)$. To model task dependencies (similar...

---

### 29. Learning to Detect Shifts in Unstructured Data Streams via Monitoring-by-Betting

**Authors:** Siyu Zhou, Jialin Ouyang, Fan Xia, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17399v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17399v1)

**Summary:** Continuous monitoring of generative AI systems requires detecting distribution shifts in the unstructured data they ingest and generate. Existing monitoring methods typically control false alarms by requiring the discrepancy measure used to detect shifts to be *pre-specified*. However, for unstructured data, pre-specification creates a sensitivity--breadth trade-off: a narrowly defined measure is sensitive to the anticipated shift but may miss unexpected changes, whereas a broadly defined measur...

---

### 30. Measure Neural Mappings

**Authors:** Ricardo Baptista, Edoardo Calvello, Bohan Chen, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17384v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17384v1)

**Summary:** We introduce and define measure neural mappings (MNMs), which combine measure-dependent neural transport with ensemble consistency for learning operators on probability measures. Ensemble consistency requires outputs from growing ensembles sampled from an input law to converge to the specified population output in probability. We establish quantitative continuum limits for attention on noncompact laws under strong sub-Gaussian and tail-integrability assumptions. These laws accommodate unbounded ...

---

### 31. On the Statistical Mechanics of Attention

**Authors:** Jerry Yao-Chieh Hu, Yu-An Chen, Maojiang Su, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17347v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17347v1)

**Summary:** We revisit the statistical mechanics of Transformer attention via modern Hopfield models. We present a free-energy formalism to characterize parameter regimes and critical thresholds for robust attention inference. The resulting free-energy landscape incorporates randomness in query states and attention weights. Attention then emerges as the equation of motion of the corresponding statistical-mechanical system (i.e., modern Hopfield model) through the standard free-energy minimization principle....

---

### 32. Monitoring for Shifts at Unknown Times: Parameter-Free Conditional Conformal Martingales

**Authors:** Tuo Liu, Drew Prinster, Francesco Orabona

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17343v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17343v1)

**Summary:** Conditional conformal test martingales provide sequential tests for detecting distribution shifts, using a fixed reference dataset to avoid contamination from test-time samples. Prior work used a penalized betting function via online optimization with smoothing, clipping, and other hyperparameters, which can adapt slowly when a shift occurs after a long stationary period. In this work, we introduce an approach that requires no hyperparameters and provably adapts quickly to shifts occurring at un...

---

### 33. Accounting for model error in ensemble variational data assimilation through learned generative dynamics

**Authors:** Marc Bocquet, Tobias S. Finn, Sibo Cheng

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17333v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17333v1)

**Summary:** Many approaches have recently been proposed to combine data assimilation with machine learning for improved forecasts with geophysical models. Here, we focus on combining advanced sequential data assimilation schemes with a generative forecasting model which accounts for complex model errors. This generative model provides a stochastic approximation of the conditional distribution of the successor state given the current state. The proposed variational formulation is a novel one-step weak-constr...

---

### 34. Near-Optimal Regret Bounds for Monotone Stochastic Optimization under Semi-Bandit Feedback

**Authors:** Tao Hu, Rohan Ghuge

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17320v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17320v1)

**Summary:** Stochastic optimization models sequential decision-making under uncertainty, typically assuming known input distributions. When these distributions are unknown, \citet{agarwal2026semibandit} give an online-to-offline reduction for monotone stochastic optimization under semi-bandit feedback, where only probed variables are observed. Its expected regret relative to the offline guarantee is $\widetilde O(n\sqrt T)$, where $n$ is the number of variables and $T$ the horizon. For optimal stopping and ...

---

### 35. Deeply unrolled alternating projections for phase retrieval

**Authors:** Jiayi Yao, Vasileios Charisopoulos, Rebecca Willett

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17316v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17316v1)

**Summary:** Deep unrolling methods for inverse problems augment traditional reconstruction algorithms with learned priors to improve their performance. These methods have been developed under the implicit assumption that the geometry of the measurement operator does not change between training and deployment; when this is no longer the case, the quality of obtained reconstructions can degrade significantly. In this paper, we argue that this is not an inherent limitation of the deep unrolling paradigm and ca...

---

### 36. The Surprising Expressivity of a Single Neuron with Autoregressive Chain-of-Thought

**Authors:** Roey Magen, Nirmit Joshi, Gal Vardi

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17283v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17283v1)

**Summary:** The success of autoregressive language models trained with Chain-of-Thought~(CoT) supervision raises a fundamental question: How simple can a next-token predictor be while still enabling the efficient simulation of general computation through its autoregressively generated CoT? Surprisingly, we show that a single neuron suffices. For a broad family of activations, including threshold and ReLU, a single autoregressive neuron can simulate any feedforward circuit with the same activation. Specifica...

---

### 37. Tight End-to-End Accounting for Differentially Private Synthetic Data

**Authors:** Georgi Ganev, Vadym Doroshenko, Arun Ganesh, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17249v1)

**Summary:** Differentially private (DP) pipelines often combine heterogeneous mechanisms, yet their guarantees are best analyzed using different notions of privacy (e.g., bounded range, zCDP, ADP). When composing them, we have to analyze the guarantees through a reduced common representation that loses accounting precision. This issue is particularly relevant in DP synthetic data generation, where data preprocessing, generation algorithms, and DP-SGD could appear within the same pipeline. We develop novel t...

---

### 38. Online LLM Personalization from Pairwise Preferences Across Users

**Authors:** Romain Puech, Georgy Salakhutdinov, Dimitris Bertsimas

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17203v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17203v1)

**Summary:** Large language models can answer the same question in different styles, but users' preferred styles are hidden and vary across users and questions. We study inference-time personalization through online selection from a fixed set of prompts, each representing a persona. Users arrive sequentially, each asks a short sequence of questions, and the system displays two responses per question and observes one pairwise choice. We formulate this interaction as a variant of the contextual dueling bandit ...

---

### 39. A Generalized McDiarmid Inequality: Sample Reuse and Non-Uniform Unbounded Differences

**Authors:** Jeremiah Birrell

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17159v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17159v1)

**Summary:** We develop a novel generalization of McDiarmid's concentration inequality and use it to obtain a uniform law of large numbers result and error bounds on stochastic optimization problems which simultaneously incorporate two key features: 1) They capture the benefit of training sample reuse in algorithms that also employ easily-sampled auxiliary random variables. 2) They allow for one-component mean-difference bounding functions which are both unbounded in the component of interest and have non-un...

---

### 40. SCOPE Before You Sample: Conformal Scores Guide Posterior Exploration for Fast and Calibrated Bayesian Predictive Inference

**Authors:** Zahra Moslemi, Ziyi Liang, Babak Shahbaba

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17146v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17146v1)

**Summary:** Bayesian predictive regions account for parameter uncertainty but can be poorly calibrated under model misspecification, even with expensive full MCMC. Cheaper approximations such as variational inference reduce the cost but often yield less accurate predictive distributions. We propose SCOPE (Score-guided Conformal Posterior Exploration), which retains the predictive quality of full MCMC while achieving calibrated coverage at a fraction of its cost. The key observation is that a prediction regi...

---

### 41. Can Rényi Accountants Beat Lossless Accountants for DP-SGD?

**Authors:** Jinho Bok

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17120v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17120v1)

**Summary:** Recent frameworks in differential privacy (DP), such as privacy loss distributions and $f$-DP, provide lossless representations of the privacy leakage of mechanisms. These approaches are often considered to yield tighter $(\varepsilon, δ)$-DP guarantees than those obtained from relaxed notions such as Rényi DP. But is that always the case? We study this question for differentially private stochastic gradient descent (DP-SGD) with fixed-size batches under replace adjacency. Our key observation is...

---

### 42. In-context classification: Calibration and noise in linear attention with softmax readout

**Authors:** Arman Rysmakhanov, Mary Letey, Yue M. Lu, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17061v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17061v1)

**Summary:** We study in-context binary classification in a simple attention model trained to minimise a logistic loss. Each prompt has a latent logistic teacher, and the learner must infer its direction from Bernoulli-labeled context examples. We derive an asymptotic prediction for the test logit in a high-dimensional regime with context length proportional to token dimension, and total training prompts proportional to dimension squared. Our formula cleanly separates calibration, test-time context noise, an...

---

### 43. Measuring Variable Importance Using Proportional Inclusive Marginal Effects

**Authors:** Youngseo Cho, V. Roshan Joseph

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17053v1)

**Summary:** Shapley-based measures are widely used for measuring variable importance in statistics and machine learning. However, these measures have a serious issue--a nonactive variable can get a positive importance measure when it is correlated with an active variable. Herin et al. recently proposed a measure called proportional marginal effects (PME) that mitigates this spurious effect. However, PME is developed for deterministic models and has high computational cost. In this article, we propose a new ...

---

### 44. CLASSO: a practical primal path-following algorithm for the constrained LASSO

**Authors:** Michael Hobson, Luke Butcher, Lindley Lentati

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17024v1)

**Summary:** We present CLASSO, a path-following method for the LASSO subject to general linear equality and inequality constraints. The local direction is obtained from a quadratic programme on an augmented active set, which determines both the coefficients that leave zero and the weakly active inequalities that remain binding. For a positive-definite Hessian and a nonempty feasible set, this programme has a unique primal minimiser, even when the binding constraint rows are dependent, and gives the local de...

---

### 45. ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty

**Authors:** Yuyang Dai, Yuting Tang, Futoshi Futami, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17016v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17016v1)

**Summary:** Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class probabilities across three simulated text-based domains: peer review, covert information transfer, and credit risk. By explicitly defining the full data-generating process for each environment, we analytically compute bo...

---

### 46. Minimax Optimality of Shampoo for Nonstationary Stochastic Optimization

**Authors:** Abir Sarkar, Nirmalya Mandal, Martin T. Wells

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16923v1)

**Summary:** We develop a comprehensive theoretical analysis of Matrix Shampoo for tracking time-varying optima in nonstationary stochastic optimization. We derive finite-horizon high-probability bounds for average tracking error that disentangle initialization, optimizer drift, momentum-induced drift penalty, stochastic noise, and adaptive preconditioning, with explicit dependence on momentum parameter \(β_1\) and stabilization parameter \(\varepsilon\). These bounds reveal an explicit drift--noise and stab...

---

### 47. Radial Tail Repair: Post-Training Correction for Diffusion and Flow Models

**Authors:** Hamza Cherkaoui, Hélène Halconruy, Antonio Ocello

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16851v1)

**Summary:** Diffusion and flow-matching models may struggle to accurately represent distributional tails, especially for heavy-tailed data. Existing approaches often use heavy-tailed noise or modify the generative dynamics, requiring dedicated retraining and more difficult estimation. We take a simpler approach: rather than relearning the full distribution, we correct only the model's behavior in the extreme regime. Our method builds on the radial-angular decomposition of multivariate heavy tails, where rad...

---

### 48. Feature Normalization under Finite Training Budgets

**Authors:** Johan Larsson

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16845v1)

**Summary:** Standardizing a rare feature can help stochastic gradient descent learn its effect within a finite budget, but it also changes the noise cost of learning. We characterize the lowest rare-subgroup risks attainable by standardized and unscaled training when each chooses a nonnegative constant learning rate and a deterministic stopping time under the same observation cap. For two independent binary features, we derive both optimized risks as prevalence vanishes while the expected number of rare obs...

---

### 49. Sample-Size Extrapolation in Simulation-Based Inference via Statistical Scaling

**Authors:** Shiyi Sun, Lei Fang, Geoff K Nicholls

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16820v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16820v1)

**Summary:** In simulation-based inference (SBI), neural posterior estimators trained on a bounded range of sample sizes can become inaccurate on larger datasets because their parameterizations do not specify how posterior location, uncertainty and shape must change as observations accumulate. We propose center-estimated NPE (CE-NPE), which combines a statistical center with an explicit contraction rate and learns a local center correction and residual densities in posterior-scale coordinates. The center is ...

---

### 50. On the Calibration of Crowdsourcing Aggregators

**Authors:** Gabriel Singer, Reda Arab, Maïssa Frikha, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16815v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16815v1)

**Summary:** Calibration has been extensively studied for classifiers, but remains largely unexplored for crowdsourcing aggregation methods, which are increasingly used for making probabilistic decisions. To the best of our knowledge, we provide the first theoretical and empirical study of calibration in label aggregation. To our great surprise, we find that widely used aggregation methods can be severely miscalibrated, and in opposite directions: Majority Vote is underconfident while model-based aggregators...

---

