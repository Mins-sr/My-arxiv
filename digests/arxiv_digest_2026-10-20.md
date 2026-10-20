# arXiv Daily Digest - 2026-10-20

Total papers: 350

---

## cs.AI

**50 papers**

### 1. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

**Authors:** Yu Zhou, Cheng-Fu Yang, Rui Sun, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26860v1)

**Summary:** Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retai...

---

### 2. Reinforcement Learning with Visually Attributable On-Policy Self-Distillation

**Authors:** Shiao Xie, Siyu Chen, Jianwei Lv, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26856v1)

**Summary:** Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate visual evidence with non-visual shifts induced by linguistic priors, response style, or the privilege...

---

### 3. CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting

**Authors:** Zehao Wang, Jianpeng Yao, Yuping Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26852v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26852v1)

**Summary:** Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusions and out-of-distribution (OOD) scenarios, where individual robots may overlook potential risks or make inaccurate predictions. Leveraging cooperation effectively for both prediction and navigation remains a major chall...

---

### 4. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

**Authors:** Zekai Li, Jiayi Yu, Jinlu Zhang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26848v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26848v1)

**Summary:** In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analysis of experimental results motivates the Physical Barrel Hypothesis: different capabilities may cons...

---

### 5. WeAct: Dynamic Weight Switching as Agent Actions

**Authors:** Rui Shi, Xunjian Yin, Jiacheng Sang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26847v1)

**Summary:** Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capab...

---

### 6. Train An Imaginative Agent

**Authors:** Jiaxin Ge, Junyi Zhang, Tianning Chai, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26845v1)

**Summary:** A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agentic Imagination (Agima), a training framework that trains an agent to imagine before acting, i.e. to be imaginative. Agima trains a single omni model to propose actions, generate images of their outcomes, and then reason ...

---

### 7. AnyGoal: On World Model Generalization Beyond Expert Rollouts

**Authors:** Heejeong Nam, Divyat Mahajan, Quentin Le Lidec, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26844v1)

**Summary:** The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics generalization, and downstream planning performance remains underexplored. We study this re...

---

### 8. LatComm: Reusable Context Compression for Latent Communication between Large Language Models

**Authors:** Huawei Lin, Jinting Liu, Tan Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26840v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26840v1)

**Summary:** Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provide only some of these properties. We introduce LatComm, a Latent Communication in...

---

### 9. Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy

**Authors:** Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26836v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26836v1)

**Summary:** LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC, a widely used geochemistry simulator from the USGS, whose reports reach 846.8k characters and whose determinism lets every printed value be traced. Agents use it to answer 158 execution-verified multiple-choice items. ...

---

### 10. Kronecker Delta Rule for Long Context Linear Attention

**Authors:** Anamaria-Roberta Hartl, Levente Zólyomi, Michael List, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26834v1)

**Summary:** We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information compared with delta-rule updates, making it particularly well suited for long-context ...

---

### 11. ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry

**Authors:** Matt Turk, Brandon L. Neel, Diana M. Lopez, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26829v1)

**Summary:** Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-structure tasks, using 4,249 rollouts from four frontier models and 4,486 further trials across 26 models. Three of the four frontier models fall within 0.031 of one another (0.785 to 0.816) with no difference between them r...

---

### 12. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis

**Authors:** Zhaoyang Wang, Qianhui Wu, Haorui Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26828v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26828v1)

**Summary:** Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interact...

---

### 13. RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development

**Authors:** Yuchi Wang, Rongyao Fang, Weihao Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26826v1)

**Summary:** Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of deve...

---

### 14. AfriBED: a Speech Recognition Bias Evaluation Dataset for Low Resource African Languages

**Authors:** Claytone Sikasote, Hussein Suleman, Jan Buys

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26821v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26821v1)

**Summary:** Despite advancements in automatic speech recognition systems (ASR), current systems exhibit speaker-attribute bias, i.e., their speech recognition performance is biased against certain speakers based on their demographic attributes such as gender, accents, and speaker type. However, accurately assessing speaker attribute bias in a given ASR system requires the availability of a bias evaluation dataset with comparable speech across subgroups of a speaker attribute. In this paper, we introduce Afr...

---

### 15. Next Best Action: Causal Constrained Offline RL for Business Action Targeting

**Authors:** Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26817v1)

**Summary:** Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints, and remain causally grounded. Existing approaches lack a rigorous framework for meeting these requirements jointly. We address this gap by formulating NBA as a Constrained Markov Decision Process (CMDP). We then integrate off-policy causal correction of the estimated customer dynamics directly int...

---

### 16. Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation

**Authors:** Yingshuang Zou, Xiaoyu Shi, Yawen Luo, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26801v1)

**Summary:** Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and fine-grained controllability. Existing multi-shot video generation approaches achieve strong consistency but still fall short in controllability. In this paper, we propose Mise-en-Video (MeV), a highly controllable multi-shot video generation framework that allows video creators to conduct staging ...

---

### 17. SOMA: Continuous Monitoring and Intervention for System Two Reasoning with System One Models

**Authors:** Ruizhi Qian, Lei Shi, Tianyu Hu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26793v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26793v1)

**Summary:** Reasoning models often run into problems without noticing them, even when symptoms are visible in their own text. In humans, metacognition separates monitoring from control: fast, intuitive signals keep watch while slow, deliberate reasoning unfolds and help decide whether to continue, change course, or stop. System One (S1) decision models, such as Jev, are a natural candidate for this role: they return a calibrated probability for a natural-language question about a text in one fast call, yet ...

---

### 18. LG-Bench: A Graph-Structured Evaluation Benchmark for Life Sciences

**Authors:** Lu Sun, Xiangyi Zhang, Xiangyang Zhu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26787v1)

**Summary:** Traditional evaluation benchmarks reduce inherently interconnected scientific knowledge in life sciences into flat lists of questions, disregarding the underlying topological structure of the knowledge. We introduce, the first graph-structured benchmark for life sciences, featuring over 10,000 high-quality multiple-choice questions across medicine, biology, and chemistry. Our approach constructs a weighted evaluation graph using bidirectional matching and semantic similarity algorithms, where no...

---

### 19. Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams

**Authors:** Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26781v1)

**Summary:** Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a proactive alternative but requires dynamic strategy adaptation that static systems cannot provide. We introduce a game-theoretic framework enabling LLMs to learn effective counter-strategies through in-context experienc...

---

### 20. TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning

**Authors:** Liana Patel, Rishabh Ranjan, Ion Stoica, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26754v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26754v1)

**Summary:** Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to...

---

### 21. recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models

**Authors:** Saurav Jha, Qianli Liao, Robert Vernon, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26747v1)

**Summary:** Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. Test-time scaling offers a complementary path, but methods developed for autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked pLMs, where a...

---

### 22. Towards Robust Model Organisms for Eliciting Latent Knowledge

**Authors:** Lennart Finke, Hardik Bhatnagar, Euodia Dodd, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26698v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26698v1)

**Summary:** A key problem in AI safety is eliciting latent knowledge (ELK), extracting information from a model that is misaligned and more knowledgeable than its overseer. For example, a misaligned model used to scan code for vulnerabilities may want to withhold its findings, i.e., sandbag, in order to exploit them later. To study ELK empirically, we need model organisms that mirror this setting. Existing model organisms fall short in several respects. In this work, we train model organisms to withhold sol...

---

### 23. Hierarchical Token Merging with Recursive Autoencoders for Unsupervised Grammar Induction

**Authors:** Murat Guney Kemal, Robert Lieck

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26695v1)

**Summary:** Hierarchical abstraction is a fundamental principle across many data modalities, enabling complex sequences to be represented compositionally at multiple levels. Learning such hierarchies directly from data, without explicit structural supervision, remains a central challenge in representation learning. We investigate whether meaningful hierarchical structure can emerge from compression alone. While autoencoders learn compressed representations through reconstruction, this objective does not nec...

---

### 24. Intra-Rubric Reward Divergence: Mitigating Rubric Hacking through Latent Dimension Recovery and Balancing

**Authors:** Jianqiang Xia, Han Xu, Dianxi Shi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26685v1)

**Summary:** Rubric hacking limits both performance and training robustness in rubric-based reinforcement learning. By decomposing rubrics into sub-dimensions, we reveal the Intra-Rubric Reward Divergence: as the total rubric score increases, certain sub-dimension scores systematically decrease, suggesting the model sacrifices specific quality aspects to optimize the aggregated objective. From the sub-dimension perspective, we observe two phenomena: (1) dimension imbalance, causing the policy to favor heavil...

---

### 25. StepBench: Diagnosing Real-World Procedural Understanding in AI Agents

**Authors:** Hossein A. Rahmani, Bin Wu, Chaeeun Lee, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26679v1)

**Summary:** Evaluating an agent's planning ability remains challenging for open-domain tasks, where verifying procedures through execution is often impractical. Existing evaluations typically assess only the final plan and do not distinguish procedural errors such as missing, incorrect, or misordered actions. We introduce STEPBENCH, a benchmark of 6,885 verified procedures crawled from wikiHow across 81 open-domain categories. From each procedure, we derive 5 diagnostic tasks: four with deterministic answer...

---

### 26. Honeypots for AI Agent Insider Threats

**Authors:** Jan Wehner, Jam Kraprayoon

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26664v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26664v1)

**Summary:** AI agents deployed inside organizations can pose an insider threat if they make mistakes, are compromised by an attacker, or pursue misaligned objectives. We propose honeypots as an AI control method to improve the security of internal agent deployments. Rather than only using honeypots for pre-deployment evaluations, defenders should plant decoy opportunities for harmful actions throughout the production environment to detect misbehavior, incriminate malicious agents, and deter attacks. Such ho...

---

### 27. AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes

**Authors:** Tian Zhang, Meng Li

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26662v1)

**Summary:** LLM trading agents are evaluated almost exclusively in backtests and autonomous benchmark harnesses. Deployment, where actions are irreversible, raises a different question: who verifies the agent's actions, and which failures can each verifier structurally catch? We report on AllPath, a personal LLM trading agent deployed against a live paper-brokerage account. The system watches positions through a deterministic rules engine, and each night it reviews its own day and proposes revisions to its ...

---

### 28. Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs

**Authors:** Zhuomin Chen, Jingchao Ni, Xu Zheng, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26660v1)

**Summary:** Smartphone GUI agents complete tasks in mobile apps by repeatedly reading the screen and asking a model for the next action. Mobile neural processing units (NPUs) enable local execution, keeping screen contents on the phone, but model latency accumulates with every action. Hybrid linear attention models reduce memory requirements, yet reusing their recurrent state requires checkpoints at the appropriate input positions. Agent requests retain instructions but rewrite recent history, so checkpoint...

---

### 29. The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training

**Authors:** Haonan Huang, Chengkun Cai

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26655v1)

**Summary:** Language models can change a committed answer to accommodate a user's opinion or pushback without new evidence. However, when this behaviour develops during training and what a released model inherits from earlier stages remain unclear. We follow 741 checkpoints of 30 open model lineages, from early pretraining to released models. We plant initial verdicts on moral scenarios and measure how far a model follows a user's stated opinion or abandons its verdict under pressure. In most lineages the b...

---

### 30. The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models

**Authors:** Aaron Maiwald, Roderick McNeill, Jaeyoung Lee, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26651v1)

**Summary:** Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filtering viral proteins from the pretraining data meaningfully degrades masked language modelling, mutation effect prediction and long-range contact prediction on viral proteins, while largely preserving performance on non-viral proteins. These effects are concentrated among protein...

---

### 31. From Outcomes to Components: A Counterfactual Evaluation Framework for LLM-Proposed Repairs

**Authors:** Hengyu Ye, Songhua Hu

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26650v1)

**Summary:** An LLM-generated repair action specifies which records to change and by how much. A failed action may still contain a useful target set or numerical update, depending on how the two are paired. We evaluate this problem in traffic networks and databases, where aggregate observations obscure the records that need correction. We examine the pairings by executing each combination from the same initial state, using a reference action that restores the affected records. In 76 of 114 traffic actions, t...

---

### 32. Reasoning-Aware Multicalibrated Reliability Predictors for Language Models

**Authors:** Ekaterina Fedorova, Alessandro Morosini, Chara Podimata

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26645v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26645v1)

**Summary:** As people increasingly rely on large language models (LLMs) for information, model providers need to communicate meaningful estimates of whether individual responses are correct or, more generally, reliable. In the context of hallucinations, existing work uses multicalibration to make such reliability predictions meaningful across application-relevant groups, such as prompt topics. Topic groups alone, however, can conceal systematic errors: within the same topic and confidence level, responses w...

---

### 33. Revision-Based Learning from Interactive Experience and Feedback

**Authors:** Jiawen Li, Chenming Ge, Alice Gao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26636v1)

**Summary:** Code generation models are increasingly used to produce interactive artifacts, such as websites and user interfaces. Many properties that determine whether these interfaces are useful only become apparent through realistic interaction, making them difficult to incorporate into model training. In this paper, we introduce RELIEF (REvision-based Learning from Interactive Experience and Feedback), a method for improving code generation models using feedback on their generated interfaces. RELIEF uses...

---

### 34. When the harness decides success: state that cannot be re-observed

**Authors:** Raimondas Lencevicius

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26632v1)

**Summary:** Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fa...

---

### 35. VaDar: Implicit Goal Conditioning via Value Disaggregation

**Authors:** Shashwat Saxena, Mehul Goel, Sreyas Venkataraman, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26629v1)

**Summary:** Long-horizon tasks are important for modern AI and robotics, yet pose a challenge for reinforcement learning. Historically, a popular approach has been to decompose a task into subgoals, and learn a subgoal-conditioned policy to execute each subtask in sequence.   We introduce an alternative called Value Disaggregation (VaDar), which trains a single subgoal-independent policy to maximize a linear combination of per-subgoal critic values. Because subgoal information is needed only at training-tim...

---

### 36. Conducting Reliable Keyword Estimation with Unreliable ASR in Police Audio Data

**Authors:** Robert Cole Molloy, Rhiannon N. Miller, Stephen Morgan, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26614v1)

**Summary:** Extracting insights from large audio data sets using human transcription is expensive and time-consuming. Off-the-shelf Automatic Speech Recognition (ASR) systems offer an easy-to-use scalable alternative, but systematic transcription errors, especially in domain-specific settings, can bias downstream analyses and lead to unreliable conclusions. We investigate whether imperfect ASR transcripts can still be used to obtain statistically valid keyword frequency estimates by combining model outputs ...

---

### 37. Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates

**Authors:** Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26595v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26595v1)

**Summary:** Jailbreak methods are commonly compared using Attack Success Rate (ASR), but these comparisons depend on how responses are generated and judged. In this paper, we examine eight attacks against three open-weight language models using three evaluation procedures. Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions. Changing the number and arrangement of attempts reverses the ranking of DeepInc...

---

### 38. WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting

**Authors:** Arjun Ashok, Mihir Parmar, Palash Goyal, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26582v1)

**Summary:** Recent time series foundation models (TSFMs) can consume covariates in-context, extending zero-shot forecasting to problems driven by external factors. This enables scenario analysis: forecasting how a target responds to events that set covariates to chosen future values. Whether they can do this reliably is an open question. We introduce WhatIf-Bench, a benchmark measuring how well forecasters use covariates to forecast a target's response to future events. WhatIf-Bench is semi-synthetic: time ...

---

### 39. Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games

**Authors:** Durgam Latha, Dion Reji, Dorde Zikelic, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26568v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26568v1)

**Summary:** Robust partially observable Markov decision processes model agents that act under partial observability while adversarial environment resolves uncertainty in the transition probabilities. Reward objectives such as discounted-sum, long-run average and cumulative reward under finite and infinite horizons allow quantifying the utility of an agent. We consider the problem of solving RPOMDPs under all four reward objectives, where the goal is to decide whether the value of a risk measure with respect...

---

### 40. BetaMem: Learning to Remember a Changing World for Embodied Agents

**Authors:** Mai Liu, He Sun, Siru Zhong, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26554v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26554v1)

**Summary:** Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A dual-level write contract constrains operation executability and source support for content: supervised fine-tuning learns compliant memory ...

---

### 41. Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior

**Authors:** Bart Jaworski, Nathaniel Mitrani, Fred Bruford, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26551v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26551v1)

**Summary:** One of the central concerns for the safety of advanced AI is scheming: when a model strategically complies under oversight but pursues its own goals when unobserved. Current demonstrations, such as Anthropic's Alignment Faking work, depend on design choices that make them less convincing: explicit test-time prompting, handcrafted backdoors, or training data that demonstrates or hints at the target behavior. Model organisms built in this way cannot tell us whether scheming tendencies would arise ...

---

### 42. Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing

**Authors:** Marla Grunewald, Fin Gentzen, Iulisloi Zacarias, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26548v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26548v1)

**Summary:** Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse Dataspace Components (EDC), the design separates concerns into cooperating agents. The orchestrator's role is to route and plan. The data extraction agent's role is to expose the DSP protocol's three composable tools (c...

---

### 43. Breaking Diffusion: Parallel Reasoning with Draft Refinement

**Authors:** Jaesang Yu, Seoyeon Byun, Yun Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26542v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26542v1)

**Summary:** Drafting an answer allows a reasoning model to reconsider each decision in the context of the others. Yet repeated diffusion denoising does not ensure that individually plausible token updates form a better answer together. We introduce Draft Refinement Language Models (DRLMs), which use a single denoiser to propose parallel revisions and evaluate a candidate draft. We train the denoiser to reconstruct every token from uniformly corrupted drafts, teaching both preservation and repair. Its predic...

---

### 44. A Semantic Knowledge Graph Construction Pipeline for Vehicle Intention Prediction in nuScenes

**Authors:** Khaled Nowara, Mohamed Manzour, Catherine Elias

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26528v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26528v1)

**Summary:** Knowledge graphs (KGs) are increasingly used in autonomous driving (AD) to make traffic scene entities and relations explicit for prediction and reasoning. Existing traffic-scene KGs, however, primarily emphasize trajectory forecasting or general scene understanding. This paper presents the nuScenes Intention Knowledge Graph (NIKG), a focused Web Ontology Language (OWL)-based semantic representation and construction pipeline for ego-centric vehicle intention context. NIKG instantiates nuScenes s...

---

### 45. Beyond Behavioral Accuracy: Evaluating Individual-Level Fidelity in LLM Investor Simulation

**Authors:** Jiajie He, Yuanhong Jiang, Xintong Chen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26524v1)

**Summary:** Large language models (LLMs) are increasingly used as user simulators, but can they faithfully reproduce an individual's behavior and decision logic over time? We investigate this question in a longitudinal paper-trading study with 80 participants. Using rolling next-day predictions, we evaluate trading activity, buy-sell structure, asset selection, and portfolio outcomes, complemented by controlled input ablations and participant-rated explanation alignment. No evaluated LLM reliably outperform...

---

### 46. Toward Structured Financial Foundation Models

**Authors:** Natraj Raman, Saumitra Mishra, Vamsi Potluru, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26516v1)

**Summary:** Foundation models promise reusable capabilities and step-change performance gains across tasks. In finance, large-scale pretraining of domain-specialized foundation models can advance both goals. However, prevailing architectures and objectives do not by themselves address the combined demands of financial systems: partial observability, interacting entities, asynchronous events, changing regimes, action-dependent outcomes, and rare states with disproportionate consequences. Moreover, independen...

---

### 47. RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing

**Authors:** Jinyang Li, Denis Emelin, Simone Tedeschi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26511v1)

**Summary:** Conversational AI systems built on Large Language Models (LLMs) require routing mechanisms that balance answer quality and response latency at scale. However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a first-class metric, and fragment evaluation across heterogeneous protocols misaligned with real-world settings. We introduce RouterWorld, a comprehensive benchmark for LLM routing in conversational GenAI. RouterWorld unif...

---

### 48. Learn the Task, Not the Schedule: Reducing Spurious Cross-Arm Coupling in Bimanual Imitation Learning

**Authors:** Shuyuan Hu, Deng-Ke Wu, Yifan Jin, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26507v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26507v1)

**Summary:** A bimanual demonstration specifies both what the robot should do and one particular schedule for when each arm should act. Standard imitation learning does not distinguish task-required cross-arm constraints from incidental scheduling choices, and may therefore exploit opposite-arm progress as a shortcut cue, creating spurious cross-arm coupling even where relative timing is irrelevant for the current task phase. We introduce Constraint-preserving Temporal Recombination (CTR), a training-time da...

---

### 49. ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents

**Authors:** Zhicheng Zheng, Cheng Zhang, Shengping Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26503v1)

**Summary:** Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlled experiments show they primarily stem from action revision. The prefix learns to alter the model's default actions. However, this revision is unscoped because step-wise CE pushes outputs toward reference actions at ever...

---

### 50. Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties

**Authors:** Afonso Baldo, António Farinhas, Marcos Treviso, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26496v1)

**Summary:** Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We introduce Dynalize, which mitigates reward hacking online, during policy training. Period...

---

## cs.CL

**50 papers**

### 1. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

**Authors:** Yu Zhou, Cheng-Fu Yang, Rui Sun, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26860v1)

**Summary:** Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retai...

---

### 2. Can It Actually Work? Synthesizing Functional CAD Mechanisms

**Authors:** Wenqian Zhang, Yangyi Huang, Zigeng Xu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26861v1)

**Summary:** While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating...

---

### 3. WeAct: Dynamic Weight Switching as Agent Actions

**Authors:** Rui Shi, Xunjian Yin, Jiacheng Sang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26847v1)

**Summary:** Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capab...

---

### 4. LatComm: Reusable Context Compression for Latent Communication between Large Language Models

**Authors:** Huawei Lin, Jinting Liu, Tan Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26840v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26840v1)

**Summary:** Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provide only some of these properties. We introduce LatComm, a Latent Communication in...

---

### 5. Competing Learning in Hybrid Architectures

**Authors:** Xingyu Shen, Yingfa Chen, Ziqing Qiao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26830v1)

**Summary:** Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenomenon where different kinds of mixers compete to learn the same function, and when ...

---

### 6. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis

**Authors:** Zhaoyang Wang, Qianhui Wu, Haorui Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26828v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26828v1)

**Summary:** Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interact...

---

### 7. KEEP-Bench: Evaluating Evidence Preservation in Context Compression

**Authors:** Ziqing Man, Di Wu, Jia-Chen Gu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26827v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26827v1)

**Summary:** Context compression improves long-context efficiency but may introduce faithfulness issues through an information bottleneck. Existing evaluations rely on QA metrics, but a reader can still answer correctly from an unfaithful compression, so these metrics underestimate such loss. To bridge this gap, we introduce KEEP-Bench, a diagnostic benchmark that directly assesses compression faithfulness with 4,102 cases across three challenging settings that require keeping evidence for plausible referenc...

---

### 8. RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development

**Authors:** Yuchi Wang, Rongyao Fang, Weihao Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26826v1)

**Summary:** Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of deve...

---

### 9. MemT-1.0: Towards Memory-Native Evolution

**Authors:** Zhiyu Li, Zeyu Zhang, Linyun Liu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26825v1)

**Summary:** Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We further introduce Mixture-of-Storage to scale native memory capacity. Following ...

---

### 10. SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum

**Authors:** Zhongxin Chen, Songhao Wu, Heng Cui, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26824v1)

**Summary:** Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure that the leading portion provides a suitable compact encoding. To address this, we propose SpecMRL, which reorganizes the feature space to enable more effective prefix readout. Specifically, we extend MRL with a parameter-derived spectral basis organized with feature importance. SpecMRL otherwise f...

---

### 11. AfriBED: a Speech Recognition Bias Evaluation Dataset for Low Resource African Languages

**Authors:** Claytone Sikasote, Hussein Suleman, Jan Buys

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26821v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26821v1)

**Summary:** Despite advancements in automatic speech recognition systems (ASR), current systems exhibit speaker-attribute bias, i.e., their speech recognition performance is biased against certain speakers based on their demographic attributes such as gender, accents, and speaker type. However, accurately assessing speaker attribute bias in a given ASR system requires the availability of a bias evaluation dataset with comparable speech across subgroups of a speaker attribute. In this paper, we introduce Afr...

---

### 12. ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar

**Authors:** Amer Goel, Yeganeh Alimohammadi, Andrew Daw

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26819v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26819v1)

**Summary:** Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural language, large language models offer a natural tool for assisting with their solution. This has given rise to autoformulation, which focuses on using LLMs to translate natural-language descriptions of decision problems...

---

### 13. Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability

**Authors:** Zhengyue Zhao, Liwei Jiang, Yejin Choi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26809v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26809v1)

**Summary:** Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when later training no longer includes safety data, and gains in safety often come at the cost of general capability. This tension suggests that safety and general reasoning should not be treated as separate training goals. We instead view safety as an LLM capability that can be learned through a reason...

---

### 14. Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models

**Authors:** Agus Sudjianto, Denis Burakov

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26797v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26797v1)

**Summary:** Candidate-scoring decision models return a probability distribution over a presented set of answers. Public documentation of one such system, Jev, and of an open counterpart, JevAny, describes three training ingredients that determine what these probabilities estimate: soft targets from larger models, a frozen pretrained backbone and temperature calibration. We analyze each ingredient in Gaussian surrogates where the finite-sample risk can be computed exactly. A student trained on teacher target...

---

### 15. RESIN: Multi-Chain Reasoning with Entity-Structured Indexing

**Authors:** Xuanyu Meng, Jash Rajesh Parekh, Jiawei Han

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26782v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26782v1)

**Summary:** Multi-chain reasoning is a challenging task not only because the multi-chain evidence is dispersed, but also because different parts of reasoning may require distinct, interacting chains of support. Flat retrieval can flood a model with loosely related text, whereas early selection of a single reasoning path can discard evidence that becomes useful only after other facts are considered. We introduce RESIN (Reasoning with Entity Structured Indexing), which uses structure to locate evidence while ...

---

### 16. Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams

**Authors:** Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26781v1)

**Summary:** Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a proactive alternative but requires dynamic strategy adaptation that static systems cannot provide. We introduce a game-theoretic framework enabling LLMs to learn effective counter-strategies through in-context experienc...

---

### 17. Monsoon: Scalable Spontaneous Speech Collection for Low-Resource ASR in 50 Languages

**Authors:** Shobhit Banga, Manas Dhir, Aaditya Pareek, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26776v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26776v1)

**Summary:** For most languages, automatic speech recognition (ASR) is limited less by model architecture than by a lack of accurately transcribed spontaneous speech. We present Monsoon, a framework for collecting such data at scale. It elicits unscripted conversations between paired contributors, screens recordings with automated classifiers, corrects transcripts over five levels of human review, and selects segments for lexical and acoustic coverage. It has collected speech in 50 languages; we analyse seve...

---

### 18. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

**Authors:** Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26770v1)

**Summary:** Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated tests without access to ground-truth solutions or official tests. Specialized agents...

---

### 19. TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning

**Authors:** Liana Patel, Rishabh Ranjan, Ion Stoica, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26754v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26754v1)

**Summary:** Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to...

---

### 20. recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models

**Authors:** Saurav Jha, Qianli Liao, Robert Vernon, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26747v1)

**Summary:** Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. Test-time scaling offers a complementary path, but methods developed for autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked pLMs, where a...

---

### 21. EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition

**Authors:** Vincenzo Perri, Ciro Cattuto, Daniela Paolotti

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26730v1)

**Summary:** To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources. We present EpiLens, a lightweight, open-source retrieval-augmented generation package that applies a fixed retrieval template and output schema to every paper in a corpus and links outputs to source passages. We build a corpus of 2,297 papers from the sources of a multi-pathoge...

---

### 22. Copying Under Repetition: From Prefix Matching to Position Hashing

**Authors:** Anxin Guo, Tianlong Huang, Chenxiao Yang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26722v1)

**Summary:** Frontier LLMs can copy random text almost flawlessly, yet they often overrun or truncate long blocks of repeated characters. In repeated strings, matching local content no longer reliably identifies where copying should continue or when it should stop. Nevertheless, we show that a two-layer transformer with $O(\log\log N)$-bit precision and $O(\log N/\log\log N)$ width can copy every string up to a chosen design horizon $N$ and terminate correctly under arbitrary repetition. We use RoPE-style ro...

---

### 23. HoloCosm: Beyond Single-Metric Benchmark Compression Across Multiple Metrics

**Authors:** Yupei Lin, Zhongzhan Huang, Junxin Li, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26714v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26714v1)

**Summary:** Benchmark compression reduces evaluation cost by selecting a small set of samples. Existing methods typically guide selection using a single metric, although benchmarks often assess models along multiple dimensions. We find that model rankings are often weakly correlated across metrics, indicating that different metrics capture distinct aspects of model performance. Samples selected for one metric do not reliably preserve scores and rankings on others when used for compressed evaluation. At 80\%...

---

### 24. Hierarchical Token Merging with Recursive Autoencoders for Unsupervised Grammar Induction

**Authors:** Murat Guney Kemal, Robert Lieck

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26695v1)

**Summary:** Hierarchical abstraction is a fundamental principle across many data modalities, enabling complex sequences to be represented compositionally at multiple levels. Learning such hierarchies directly from data, without explicit structural supervision, remains a central challenge in representation learning. We investigate whether meaningful hierarchical structure can emerge from compression alone. While autoencoders learn compressed representations through reconstruction, this objective does not nec...

---

### 25. Parallel Language Models via Variational Decoding

**Authors:** Felix Draxler, Robin C. Geyer, Daniel Geyfman, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26693v1)

**Summary:** Autoregressive language models emit one token per forward pass. This causes high inference latency, in particular as models are scaled up for quality. In this paper, we introduce Parallel Language Models (PLMs), which generate mutually consistent tokens in one forward pass by routing dependencies through latent auxiliary variables. PLMs are trained using a variational bound that reduces to an autoregressive loss plus a parallel decoding loss. Empirically, PLMs are on a faster and better Pareto f...

---

### 26. Intra-Rubric Reward Divergence: Mitigating Rubric Hacking through Latent Dimension Recovery and Balancing

**Authors:** Jianqiang Xia, Han Xu, Dianxi Shi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26685v1)

**Summary:** Rubric hacking limits both performance and training robustness in rubric-based reinforcement learning. By decomposing rubrics into sub-dimensions, we reveal the Intra-Rubric Reward Divergence: as the total rubric score increases, certain sub-dimension scores systematically decrease, suggesting the model sacrifices specific quality aspects to optimize the aggregated objective. From the sub-dimension perspective, we observe two phenomena: (1) dimension imbalance, causing the policy to favor heavil...

---

### 27. Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows

**Authors:** Qian Xie, Wenyue Hua, Yueli He, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26676v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26676v1)

**Summary:** LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple candidates. We introduce Cost-Coupled Gittins (CC-Gittins), a multi-objective extension of single-objective cost-aware Gittins search for Pareto recommendation. It exploits the coupling between evaluation and deployment co...

---

### 28. SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26659v1)

**Summary:** Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target o...

---

### 29. The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training

**Authors:** Haonan Huang, Chengkun Cai

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26655v1)

**Summary:** Language models can change a committed answer to accommodate a user's opinion or pushback without new evidence. However, when this behaviour develops during training and what a released model inherits from earlier stages remain unclear. We follow 741 checkpoints of 30 open model lineages, from early pretraining to released models. We plant initial verdicts on moral scenarios and measure how far a model follows a user's stated opinion or abandons its verdict under pressure. In most lineages the b...

---

### 30. From Outcomes to Components: A Counterfactual Evaluation Framework for LLM-Proposed Repairs

**Authors:** Hengyu Ye, Songhua Hu

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26650v1)

**Summary:** An LLM-generated repair action specifies which records to change and by how much. A failed action may still contain a useful target set or numerical update, depending on how the two are paired. We evaluate this problem in traffic networks and databases, where aggregate observations obscure the records that need correction. We examine the pairings by executing each combination from the same initial state, using a reference action that restores the affected records. In 76 of 114 traffic actions, t...

---

### 31. When the harness decides success: state that cannot be re-observed

**Authors:** Raimondas Lencevicius

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26632v1)

**Summary:** Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fa...

---

### 32. Conducting Reliable Keyword Estimation with Unreliable ASR in Police Audio Data

**Authors:** Robert Cole Molloy, Rhiannon N. Miller, Stephen Morgan, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26614v1)

**Summary:** Extracting insights from large audio data sets using human transcription is expensive and time-consuming. Off-the-shelf Automatic Speech Recognition (ASR) systems offer an easy-to-use scalable alternative, but systematic transcription errors, especially in domain-specific settings, can bias downstream analyses and lead to unreliable conclusions. We investigate whether imperfect ASR transcripts can still be used to obtain statistically valid keyword frequency estimates by combining model outputs ...

---

### 33. BERT Is Already a Denoiser: Cheaply Unlocking Iterative Generation in Masked Language Models

**Authors:** Julio C. Amador Diaz Lopez

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26601v1)

**Summary:** Masked language models (MLMs) such as BERT are typically used for representation learning despite their denoising pretraining. We test whether this capability supports conditional generation without diffusion training. Our decoder repeatedly predicts masked tokens and commits high-confidence predictions using a cosine schedule. It requires no diffusion timestep or reverse-diffusion objective. Frozen BERT already exhibits substantial denoising capability, reconstructing 61.0%, 37.5%, and 24.4% of...

---

### 34. Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks

**Authors:** Rohan Menon, Chih-Hong Cheng

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26589v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26589v1)

**Summary:** Attack success rate (ASR) evaluates jailbreaks against large language models without accounting for repeated calls to the victim model. Yet each additional call gives the deployed system another opportunity to detect the attack and intervene. We introduce $\mathrm{ASR}_{\mathrm{STEP}}$, which penalizes additional victim-model calls while retaining binary success judgments. Our evaluation considers GCG~\cite{zou2023universal}, PAIR~\cite{chao2025jailbreaking} with a step budget, and a single-step...

---

### 35. ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting

**Authors:** Sanghyun Lee, Wonjin Nam, Seungho Jang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26531v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26531v1)

**Summary:** Block diffusion drafters accelerate speculative decoding by generating multiple draft tokens in a single forward pass. However, each pass produces only a fixed-length block from a single target-generated anchor, limiting how far the draft can extend. Meanwhile, target verification computes hidden states even at positions beyond the first rejection, but these states are typically discarded rather than reused. We propose ReAnchor, a training-free method that reanchors a pretrained drafter at shift...

---

### 36. A Fisher-Geometric View of Multi-Teacher On-Policy Distillation

**Authors:** Liu Kaiyuan, Zhuang Ziyuan, Ma Haoxuan, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26525v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26525v1)

**Summary:** Consolidating specialized foundation models into a unified generalist is a central goal of post-training. Two approaches are in common use: model merging, which is fast but treated as a heuristic, and multi-teacher on-policy distillation, which matches distributions but demands heavy rollout compute and suffers from cross-task gradient conflict. We show that the two are one objective seen at different orders. Within a shared basin of homologous specialists, the multi-teacher on-policy distillati...

---

### 37. RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing

**Authors:** Jinyang Li, Denis Emelin, Simone Tedeschi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26511v1)

**Summary:** Conversational AI systems built on Large Language Models (LLMs) require routing mechanisms that balance answer quality and response latency at scale. However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a first-class metric, and fragment evaluation across heterogeneous protocols misaligned with real-world settings. We introduce RouterWorld, a comprehensive benchmark for LLM routing in conversational GenAI. RouterWorld unif...

---

### 38. Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties

**Authors:** Afonso Baldo, António Farinhas, Marcos Treviso, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26496v1)

**Summary:** Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We introduce Dynalize, which mitigates reward hacking online, during policy training. Period...

---

### 39. Strength Controls Change How Interventions Compare Across Sparse Autoencoder Codes

**Authors:** Jinchen Zhang, Zheyuan Liu, Yihan Zhu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26489v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26489v1)

**Summary:** Changing sparse autoencoder (SAE) codes can alter both intervention direction and magnitude, so comparing intervention effects requires a strength control specifying what is held equal. Norm matching and output calibration provide different controls, but whether interventions yield different effects across codes after strength matching remains unclear. We compare intervention effects under these controls for fixed feature groups in Gemma and Llama and observe: (1) Whole-patch scaling. With one c...

---

### 40. AfriGuard: Safety and Robust Refusal For African Languages

**Authors:** Israel Abebe Azime, Jesujoba O. Alabi, Iffat Maab, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26474v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26474v1)

**Summary:** Large language models (LLMs) designed to interact with users are typically trained to respond appropriately to harmful or toxic content. However, ensuring appropriate responses becomes more challenging in diverse linguistic and cultural contexts, where safety risks may be expressed or interpreted differently. Building safe AI systems therefore requires detecting safety risks, understanding their nature, and responding appropriately, while accounting for linguistic and cultural variations that ad...

---

### 41. Training Negatives Still Matter After Calibrating Answerability Readouts

**Authors:** Jinchen Zhang, Zheyuan Liu, Yihan Zhu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26461v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26461v1)

**Summary:** Answerability readouts predict whether a passage supplies an answer, but whether calibration can compensate for removing negative passages during training remains unclear. We present a controlled study of how training-negative construction affects calibrated prediction, ranking, and downstream answer retention. We compare native training, which retains negative passages, with empty training, which removes them, holding questions, labels, positive examples, and model weights fixed. Both are calib...

---

### 42. TeleASR-Amharic: A Benchmark for Robust Amharic ASR in Realistic Telecommunication Conditions

**Authors:** Dagnachew Mekonnen Marilign, Enrique Molero, Abrham Haile, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26448v1)

**Summary:** The real-world usability of ASR models remains challenging, particularly for low-resource languages, where existing speech resources are often collected in clean studio environments. In this work, we introduce TeleASR-Amharic, a benchmark for evaluating Amharic ASR under various acoustic and telecommunication conditions. We analyze the major degradations observed in real telecommunications recordings and develop a benchmark that covers multiple channel conditions, environmental disturbances, and...

---

### 43. Label Authority in Speech Emotion Recognition: Intended and Perceived Ground Truth in Emozionalmente

**Authors:** Marco Giordano, Stefano Giacomelli, Claudia Rinaldi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26446v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26446v1)

**Summary:** Ground truth in Speech Emotion Recognition (SER) is often presented as a single categorical fact, yet an acted emotion and the emotion heard by listeners describe different aspects of the same recording. We examine this distinction in Emozionalmente, an acted Italian corpus that provides both an elicited production label and five listener judgements for every clip. Using frozen XLS-R, HuBERT, and WavLM representations with matched probes, we compare three label authorities: the expressed conditi...

---

### 44. WenSight-Decision-1 for Direct Decisions under E-commerce Rules

**Authors:** Mingwen Liu, Jun Sun, Sichen Wang

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26444v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26444v1)

**Summary:** E-commerce decisions require applying natural-language rules to the available case evidence. We introduce WenSight-Decision-1, a shared model that scores supplied options directly from rules and case information for six operational tasks, with examples spanning six languages. We fine-tune Qwen3.5-9B with reference options as supervision, using the same option scores for training and inference. On 1,440 synthetic operational cases reserved for final evaluation, accuracy rises from 61.60% for Qwen...

---

### 45. The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits

**Authors:** Iliya Zhechev, Radoslav Ralev, Chris Coleman, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26433v1)

**Summary:** We study whether geometric relationships between conversation turns, memory texts, and queries can predict answer correctness before generation. We evaluate four memory implementations with dense or hybrid retrieval and one observation-summary comparator. We embed these texts in a shared space. A logistic classifier uses 25 features describing query proximity, memory-conversation correspondence, and conversation structure. On LongMemEval-small, pooled AUROC is 0.640 over 2,367 question-system pa...

---

### 46. HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL

**Authors:** Xiaoqiang Wang, Ting-En Lin, Yuchuan Wu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26426v1)

**Summary:** Rubric-based reinforcement learning (RL) trains policies for open-ended generation with natural-language criteria as rewards, but these rewards can become ineffective as training progresses. We identify two failure modes. Under non-discriminative rewards, scores collapse to uniformly low or high values due to insufficient exploration or a mismatch between task difficulty and policy capability. Under spurious rewards, higher scores do not correspond to better responses. Both reflect a training co...

---

### 47. SNO-PI: Label-Scarce SNOMED CT Entity Linking with Pre-trained Encoders and Curated Terminology Knowledge

**Authors:** Piyawoot Songsiritat

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26425v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26425v1)

**Summary:** We present SNO-PI, the top-performing submission on SNOMED International's SNOMED CT Entity Linking Benchmark as of 18 October 2026. SNO-PI achieves a macro character IoU of 0.5387, outperforming the organisers' reference system (0.4582; based on the 2024 challenge winner's approach) by 18% relative. Linking clinical mentions to SNOMED CT is a zero- and few-shot problem over a very large label space: the 272 annotated MIMIC-IV discharge summaries cover only 6,595 of the roughly 219,000 eligible ...

---

### 48. Governing the Rule Space. Ruliology, Computational Irreducibility and Anticipatory Governance of Quantum Technologies

**Authors:** Antonio Felice Uricchio, Francesco Scagliola

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26423v1)

**Summary:** The regulation of emerging technologies is often conceived as a strategy of catching up, because legislators arrive too late. Yet gathering signals, constructing scenarios and adapting rules to an anticipated future are fundamental tasks for those entrusted with governance, including the governance of rules themselves. The literature on so-called future law has already shown that anticipation means building institutional capabilities rather than predicting outcomes precisely (anticipatory govern...

---

### 49. Self-Consistency of Entity Sets and Citations in a Deep Research System under Repeated Prompting

**Authors:** Lauri Pykälä, Kimmo K. Kaski

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26421v1)

**Summary:** Deep research agents (DRA) are commonly used for open-ended synthesis tasks where closed-world QA benchmarks are poorly suited to characterize relevant aspects of performance. We study the self-consistency of one commercial deep research system under repeated identical prompting, representing each report with the set of named entities it mentions, categorised by a custom schema, and the set of citations it retrieves. Across repeated runs of a single open-ended cybersecurity related prompt, we qu...

---

### 50. Co-Evolving Policy and Reward for Code Generation: A Mechanistic Study of Single-Adapter Drift

**Authors:** Amarsaikhan Batjargal, Noriko Tomuro

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26416v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26416v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is particularly well suited to code generation because generated programs can be objectively evaluated through execution. Execution also provides behavioral information that can be reused as additional supervision. The Synergistic Policy and Reward Co-Evolving Framework (SPARK), originally proposed for reasoning tasks, exploits this idea by recycling training rollouts and their evaluation results to train a model not only to generate solution...

---

## cs.CV

**50 papers**

### 1. Text-to-Image Generative Modeling Without Language Pretraining

**Authors:** Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26863v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26863v1)

**Summary:** Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with 18.2$\times$ less pretraining compute. Further, Halcyon-1.6B outperforms JiT-T2I-XXL/8+...

---

### 2. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

**Authors:** Yu Zhou, Cheng-Fu Yang, Rui Sun, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26860v1)

**Summary:** Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retai...

---

### 3. Can It Actually Work? Synthesizing Functional CAD Mechanisms

**Authors:** Wenqian Zhang, Yangyi Huang, Zigeng Xu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26861v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26861v1)

**Summary:** While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating...

---

### 4. Reinforcement Learning with Visually Attributable On-Policy Self-Distillation

**Authors:** Shiao Xie, Siyu Chen, Jianwei Lv, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26856v1)

**Summary:** Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate visual evidence with non-visual shifts induced by linguistic priors, response style, or the privilege...

---

### 5. VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token

**Authors:** Sangbeom Lim, Seoung Wug Oh, Heeji Yoon, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26857v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26857v1)

**Summary:** Diffusion-based video matting has recently emerged as a leading approach, leveraging video diffusion priors from internet-scale pretraining to achieve strong zero-shot generalization from limited synthetic data. However, the heavy compute of these diffusion backbones limits inference to a short chunk of just 6 to 24 frames, so even ordinary videos span multiple chunks. Because each chunk is matted independently from coarse mask guidance, existing methods fail to maintain consistency across chunk...

---

### 6. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

**Authors:** Tianqi Liu, Hanfei Zhao, Qifeng Liang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26855v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26855v1)

**Summary:** World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotati...

---

### 7. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation

**Authors:** Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26853v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26853v1)

**Summary:** Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain largely constrained by predefined factories and APIs, limiting their ability to create novel asset t...

---

### 8. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning

**Authors:** Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26851v1)

**Summary:** Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-agent framework that grounds every stage of generation in the source manga. We decompose the task in...

---

### 9. GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries

**Authors:** Xi Hu, Martin Bell, Liang Zheng

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26850v1)

**Summary:** Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We introduce GenOlympiad, a benchmark which provides the most challenging text prompts from nine capability axes for stress-testing frontier text-to-image models. The assessed capabilities include generating large quantities, performing deep reasoning, ensuring hard physical consistency, following complex...

---

### 10. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

**Authors:** Zekai Li, Jiayi Yu, Jinlu Zhang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26848v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26848v1)

**Summary:** In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analysis of experimental results motivates the Physical Barrel Hypothesis: different capabilities may cons...

---

### 11. SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration

**Authors:** Javad Rajabi, Hakki Can Karaimer, David B. Lindell, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26837v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26837v1)

**Summary:** Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Feature caching reduces this cost by reusing features across denoising steps. Recent forecasting methods extend this idea by extrapolating features to skipped steps instead of reusing them. However, existing forecasting methods extrapolate the features they predict uniformly, even though the spatial-f...

---

### 12. RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development

**Authors:** Yuchi Wang, Rongyao Fang, Weihao Yu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26826v1)

**Summary:** Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of deve...

---

### 13. Open-Form Geometric Style Transfer

**Authors:** Adar Elad, Gal Metzer, Omer Dahari, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26820v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26820v1)

**Summary:** A geometric style learned from one family of shapes is typically applied to new shapes from the same family. We consider a more challenging setting: learning the geometric design language of a stylized Latin alphabet and applying it to new forms, from Greek glyphs to entirely different structures such as human poses. We introduce Open-Form Geometric Style Transfer, where the forms to which a learned geometric style can be applied are not restricted to the shape family in which that style was obs...

---

### 14. Real-Time Radar Semantic and Panoptic Scene Understanding

**Authors:** Santosh Parit, Julia Hindel, Rohit Mohan, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26816v1)

**Summary:** Robust scene understanding under varying environmental conditions is essential for safe autonomous driving. While cameras and LiDAR degrade in adverse weather and poor lighting, Frequency-Modulated Continuous-Wave (FMCW) spinning radar provides dependable 360° perception at extended ranges with minimal compute cost. However, real-time FMCW radar scene understanding is challenging due to complex signal returns, limited temporal resolution, and scarce annotated datasets. We introduce StreamRPS, a ...

---

### 15. PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

**Authors:** Yude Zou, Yifei Yao, Guanbo Jiao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26813v1)

**Summary:** World Action Models (WAMs) jointly predict future video and generate actions, yet remain sensitive to task-irrelevant visual perturbations, i.e., changes in visual appearance that should not affect robot behavior. We identify a gap in conventional WAM training: video prediction encourages representations to preserve appearance information, while action generation does not explicitly enforce invariance to task-irrelevant appearance. Data augmentation exposes WAMs to such perturbations but does no...

---

### 16. State World Models: Execute the Rules, Generate the Pixels

**Authors:** Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26811v1)

**Summary:** Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support stateful and rule-governed interaction. It maintains an evolving world state unde...

---

### 17. What Language Adds, and at What Cost: Four Controlled Probes of Pathology Vision-Language Models

**Authors:** Wenhao Zhang, Zhongliang Zhou, Yi Ping, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26805v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26805v1)

**Summary:** Vision--language models (VLMs) promise to make computational pathology queryable and able to draft reports, but how much language adds beyond the vision backbone is unclear, because almost every system is evaluated by its developers on test sets of their own choosing. We grade published evidence by how it was produced and test four claims with controlled probes that reuse released checkpoints and public data, varying one input at a time. Report text adds prognostic signal: adding a frozen embedd...

---

### 18. Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation

**Authors:** Yingshuang Zou, Xiaoyu Shi, Yawen Luo, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26801v1)

**Summary:** Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and fine-grained controllability. Existing multi-shot video generation approaches achieve strong consistency but still fall short in controllability. In this paper, we propose Mise-en-Video (MeV), a highly controllable multi-shot video generation framework that allows video creators to conduct staging ...

---

### 19. V-JEPA Hand: Simple, Accurate and Fast 3D Hand and Camera Trajectory Recovery from Egocentric Videos

**Authors:** Ruicheng Li, Qixiu Li, Yu Deng, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26780v1)

**Summary:** Egocentric video supports diverse applications, including robot learning, augmented reality, and human activity understanding. Recovering metric 3D hand trajectories from such video requires estimating both hand motion and camera egomotion to express the hands in a consistent reference frame. Many existing pipelines recover hand and camera motion in separate stages, combining hand detection, hand reconstruction, camera tracking, and trajectory refinement. We present V-JEPA Hand, a simple feed-fo...

---

### 20. Beyond Omni: A Unified MLLM for Embodied Sensory Understanding

**Authors:** Shiyun Xiong, Dongming Wu, Peiwen Sun, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26751v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26751v1)

**Summary:** Recent embodied systems increasingly build on multimodal large language models (MLLMs) for their pretrained understanding and reasoning capabilities, but their perception of the physical world remains largely limited to basic modalities such as vision and audio. However, broadening MLLMs to more diverse sensory modalities from the physical environment is challenging: their representations are often weakly connected to the MLLM and vary substantially in structure and statistics, while their inter...

---

### 21. CheckDistill: Adaptive Checklist Distillation for Efficient Distributional Reward Modeling in Image Editing

**Authors:** Yaqi Cai, Zuan Gao, Mengting Chen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26740v1)

**Summary:** Reinforcement learning for instruction-guided image editing requires reward models that provide reliable, accurate, and efficient feedback. Direct scalar prediction compresses multidimensional editing preferences, whereas generative evaluators can expose their judgment through explicit reasoning. However, broad scoring criteria do not specify all instance-dependent editing and preservation constraints, and generating long reasoning trajectories is costly for online optimization. We introduce Che...

---

### 22. CAVA: Complementary-Label-Aware Data Valuation

**Authors:** Tan-Ha Mai, Hsuan-Tien Lin, Vu Nguyen

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26734v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26734v1)

**Summary:** Complementary-label learning (CLL) trains a classifier from labels that name a class an instance does not belong to. Such labels are cheap to collect from crowdworkers or vision-language models (VLMs), making them attractive for large-scale annotation. However, both sources can mistakenly assign the true class as the complementary label. Such annotation errors are particularly harmful in CLL because the model is explicitly trained to suppress the correct answer. Optimal transport (OT) data valua...

---

### 23. PlanarCityLoc: Breaking Silhouette Ambiguity in LoD Aerial Localization via 3D Planes

**Authors:** Oussema Dhaouadi, Shao Jie Hu-Chen, Jakob Gollreiter, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26729v1)

**Summary:** Aerial visual localization is crucial for autonomous drone navigation in urban environments where GNSS signals are often degraded. Lightweight textureless Level-of-Detail (LoD) city models provide a geometric map alternative to textured assets. Existing silhouette-based methods rely on image-space alignment, which can leave different camera poses indistinguishable and favor incorrect poses when segmentation errors distort the building outlines. We present PlanarCityLoc, which moves beyond silhou...

---

### 24. A Flexible ROI Analysis Tool for Spatially Consistent Vegetation Index Extraction from Turfgrass Imagery

**Authors:** Kibon Ku, Thai Thanh Tuan, Jinhyun Ahn

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26719v1)

**Summary:** Time-series multispectral imaging is widely used to assess turfgrass condition; however, extracting plot-level vegetation index (VI) values remains labor-intensive when camera positions vary between acquisitions and automated plot tracking is unreliable. We developed an open-source software tool comprising (i) a graphical user interface (GUI) for the interactive placement of orientation-adjustable regions of interest (ROIs) with $N$-way subdivision to match plot geometry and (ii) a batch-process...

---

### 25. PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements

**Authors:** Kaiwei Chen, Moran Li, Zhenye Gan, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26711v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26711v1)

**Summary:** Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured. Physical plausibility asks whether generated objects obey geometry, kinematics, dynamics, and conservation laws. Existing benchmarks rely on coarse visual-language model judgments or target embodied world models rather than video generation itself. We introduce PVBench, a physical video benchmark that quantitatively measures the plausibility of generated videos across 46 d...

---

### 26. Foundation Model Driven Optical Flow

**Authors:** Praroop Chanda, Suryansh Kumar

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26690v1)

**Summary:** We investigate how frozen pretrained visual and depth representations support dense optical flow when coupled with a supervised matching network. Building on TTSFlow, this paper studies Dense Prediction Transformer (DPT) feature decoding and one coarse-to-fine refinement stage. Our method fuses features from frozen DINOv2 and Depth Anything V2 models and estimates optical flow through a trainable transformer-based matching pipeline. After optical-flow training on FlyingChairs and FlyingThings3D,...

---

### 27. BrushOff: Stroke-Based Re-rendering as a Watermark Removal Attack on Painting

**Authors:** Hao Chen, Junnan Xu

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26682v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26682v1)

**Summary:** Invisible watermarks are used to mark who owns a painting. We show that a simple attack removes the most robust one we test. The attack redraws the watermarked painting with brush strokes, using a pretrained stroke-based renderer. We call this attack BrushOff. It needs no training, no knowledge of the watermark, and no generative model. We test four watermarks on 500 paintings from five styles. VINE, a recent watermark built to survive image editing, survives all 14 conventional distortions we t...

---

### 28. From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping

**Authors:** Zekai Luo, Yuwei Liang, Ruiqi Ma, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26681v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26681v1)

**Summary:** Video face swapping transfers the reference identity to a target video while preserving its other attributes and motion. Despite recent progress in reference-guided flow-based methods, jointly achieving faithful identity transfer, high fidelity, and real-time generation over long video streams remains challenging. To address this challenge, we rethink the task-specific structure of reference-guided video face swapping. First, face swapping changes only identity while preserving most visual conte...

---

### 29. CaptionFuse: Training-Free Composed Product Retrieval Via VLM Intent Captioning and Weighted Embedding Fusion

**Authors:** Zhao Gao, Mina Metias, Mohamed Noordeen Alaudeen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26661v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26661v1)

**Summary:** Composed Image Retrieval (CIR) retrieves products matching a reference image modified by natural language---a core capability for eCommerce search. Existing training-free methods fuse CLIP embeddings via arithmetic, but we identify a fundamental limitation: user text modifications are attribute-sparse---a user who types ``make it red with shorter sleeves'' specifies what to change but not what to keep (the floral pattern, the V-neck, the fit-and-flare silhouette). We introduce language-space fus...

---

### 30. SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26659v1)

**Summary:** Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target o...

---

### 31. Dual-Scale Condition-Shift Editing for Robust Real-World Image Demoiréing

**Authors:** Shiyang Zhou, Haijin Zeng, Congpei Qiu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26644v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26644v1)

**Summary:** Robust demoiréing of screen-recaptured images remains challenging: moiré varies in frequency, color, and spatial support across display-camera pairs and capture conditions. Dedicated restoration networks trained on finite paired data struggle with this diversity, especially when low-frequency color banding and high-frequency stripes co-occur. We present DemoiréEdit, a content-preserving editing framework that adapts the natural-image prior of a pretrained flow-matching editor to demoiréing. Firs...

---

### 32. EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience

**Authors:** Xinhao Ji, Hui En Pang, Hao Li, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26625v1)

**Summary:** Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned supervision, yet existing methods and datasets offer limited support for either. We present EgoXperience, a full-stack paradigm that addresses these needs through data collection, automatic annotation, uni...

---

### 33. Scaling Vision Foundation Models for Toxicologic Pathology

**Authors:** Jessica Loo, Theodoros Pissas, Byunghak Kang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26586v1)

**Summary:** Here, we present TOX-FM, a family of non-clinical PFMs trained on large-scale diverse histopathology datasets of over one million whole slide images consisting of over 60 organs across six animal species from over 14,000 toxicology studies across six decades. We introduce a comprehensive benchmark of 18 non-clinical downstream tasks, incorporate an established benchmark of 9 clinical downstream tasks, and evaluate TOX-FM against state-of-the-art clinical PFMs across both non-clinical and clinica...

---

### 34. Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos

**Authors:** Tong Zhao, Zhiyuan Han, Lin Chen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26585v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26585v1)

**Summary:** Generating reusable driving environments requires both controllable future observations and an explicit representation that supports rendering from different viewpoints, yet existing methods still recover explicit scenes from generated RGB videos through optimization for each sequence. To overcome these limitations, we present Drive2Gauss, a feedforward framework that converts jointly generated RGB, metric depth, and dynamic flow into dynamic 4D Gaussian scenes. A Multimodal Video Generator pred...

---

### 35. DenseHap: Dense Hand Haptic Estimation from Monocular Images

**Authors:** Junhan Xue, Rolandos Alexandros Potamias

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26583v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26583v1)

**Summary:** As dexterous robotic manipulation advances, scalable annotations of human hand-object interactions are becoming increasingly important. Furthermore, previous hand contact estimation methods suffered from issues such as dorsal-side misclassifications and insufficient precision, while lacking a unified framework for integrating multiple hand to environment interaction modalities, including distance fields, contact thresholds, and pressure. To address that, we present DenseHap, a unified end-to-end...

---

### 36. PrismWAM: Decoupling State Representations in World Action Models

**Authors:** Tianyu Xin, Wanqi Zhong, Bowen Hu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26564v1)

**Summary:** World Action Models (WAMs) typically represent the world through latent embeddings from pretrained video models, which entangle heterogeneous aspects of the world, from how it looks (e.g., texture and color) to how it is physically configured (e.g., occupancy and pose). This raises an underexplored question: $\textbf{what should constitute the state of a WAM?}$ We argue that the world state should separate how the world appears from how the world evolves under action: the former captures semanti...

---

### 37. MRI Reconstruction Risk Estimation from Inference Dynamics

**Authors:** Tamir Shor, Alex Bronstein

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26558v1)

**Summary:** Iterative MRI reconstructors produce intermediate estimates before returning a final image. We study these inference trajectories as a model-internal representation of realized reconstruction risk, measured by log-NMSE. Model-native states are projected to magnitude images, summarized by a fixed 16-dimensional descriptor, and mapped to risk using a source-trained ridge readout. Across three reconstruction backbones, trajectory features are strongly predictive of reconstruction risk on held-out s...

---

### 38. Holi-World: Building Holistic World Intelligence from Human-Ego Experience

**Authors:** Hao Li, Xiyuan Zheng, Yuanyuan Gao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26549v1)

**Summary:** Human egocentric experience offers a rich foundation for learning how the world is organized and how it changes through interaction. Realizing this potential at scale requires turning growing volumes of recordings into learning resources that connect scene structure, object semantics, and interaction histories across viewpoints and time, while reducing dependence on costly manual annotation. We introduce HOLI-WORLD, an integrated ecosystem connecting experience capture, world representation, aut...

---

### 39. Small Average Error, Wide Individual Error: General-Purpose LLMs Estimating Energy Intake from Meal Photos in a Feeding Trial

**Authors:** Xiaomeng Li

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26538v1)

**Summary:** Photo-based estimation of food energy could ease dietary assessment, and general-purpose multimodal large language models (LLMs) make such estimates easy to obtain. Most evaluations use one photo taken before eating and compare with energy served, while dietary assessment needs energy eaten. We evaluated six models from two vendors (Claude Haiku, Sonnet and Opus 5.5; GPT-6 luna, 6.1 sol and 6 astra) on 802 meals from ACETADA, a controlled feeding trial with weighed intake, with the before photo ...

---

### 40. Interpretable Face Contrast Modeling for Smartphone Portrait Rendering

**Authors:** Yujin Cho, Benoît Pochon, Jean-Michel Morel, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26517v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26517v1)

**Summary:** The quality of smartphone portrait photography has become increasingly important to both manufacturers and users. Recent devices use complex computational pipelines to improve facial rendering under varied lighting. These pipelines vary widely across manufacturers, so the same portrait can look noticeably different across smartphones. These differences affect multiple aspects of facial appearance, making perceptual preference difficult to characterize with a single measure. To address this, we p...

---

### 41. PDNet: Exploring Pruning and Distillation for Real-Time Worker Activity Recognition in Industrial Assembly

**Authors:** Malek Baba, Thinesh Thiyakesan Ponbagavathi, Alina Roitberg

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26491v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26491v1)

**Summary:** In this work, we address real-time fine-grained human activity recognition (HAR) in industrial assembly and introduce PDNet, a new framework that jointly exploits structured pruning and knowledge distillation for 3D convolutional networks. We start by training a 3D-CNN backbone in a supervised manner. Then, PDNet applies channel-wise structured pruning to obtain a more compact network. In the third step, our method is optimized using knowledge distillation from the large unpruned teacher to reco...

---

### 42. 3D Diffusion Models for Medical Imaging

**Authors:** Frank-Peter Schilling, Daniel Barco, Philipp Denzel, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26475v1)

**Summary:** Generative deep learning methods such as Variational Autoencoders, Generative Adversarial Networks or Diffusion Models have achieved remarkable results in image synthesis. In particular, Diffusion Models have demonstrated superior image fidelity and sample diversity compared to other approaches on standard benchmarks, while also offering more flexible training dynamics as evidenced both in natural image domains and in medical applications. In medical imaging including Computed Tomography, Magnet...

---

### 43. YUTELA: A Scalable Edge Cloud AIoT System for Multi-Site Video Anomaly Detection with Scene Specific Adaptation

**Authors:** Shanle Yao, Babak Rahimi Ardabili, Amir Kimiyaie, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26468v1)

**Summary:** Building upon our previous Ancilia framework, this work presents \emph{YUTELA}, an edge--server--cloud AIoT system for long-term, multi-site video anomaly detection. YUTELA replaces workstation-based on-site processing with NVIDIA Jetson Thor edge devices and redesigns the multi-camera pipeline through camera batching and redistribution, shared memory, reduced inter-stage data transfer, task integration, and TensorRT-accelerated inference. It maintains a separate anomaly model per camera, retrai...

---

### 44. Progressive multi-scale tumor-state memory for incomplete multimodal brain tumor segmentation

**Authors:** Milad Rostamian, Mohammadreza Mohammadi, Mohsen Soryani

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26457v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26457v1)

**Summary:** Brain tumor segmentation uses complementary magnetic resonance imaging (MRI) sequences, but some sequences may be unavailable in practice. Their absence changes the information available for segmenting different tumor regions. Fusion methods can support different input subsets. However, fusion at several scales does not by itself specify how tumor evidence is retained and updated to guide fusion at later stages. We propose a progressive multi-scale tumor-state memory network (PMTM) for segmentat...

---

### 45. When Guidance Becomes a Guard: Early Interception of Unsafe Inputs in Text-to-Image Generation

**Authors:** Yanchun Li, Yujin Wu, Gangkai Shen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26452v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26452v1)

**Summary:** Text-to-image diffusion models can produce unsafe content, while output filtering intervenes only after synthesis. We investigate whether native generation signals enable early detection of unsafe and adversarial inputs. We find that classifier-free guidance exposes strong safety signals in conditional responses, accessible through compact statistics and linear readouts. Based on this finding, we propose Conditional Semantic Trajectory Interception (CSTI), which aggregates activation contrasts b...

---

### 46. Long-form Video-to-Text Summarization using Recursive Language Models

**Authors:** Alessia Intini, Lorenzo Vaiani, Enrico Chen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26431v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26431v1)

**Summary:** While VideoLLMs have made significant progress in understanding short video benchmarks, they often struggle to summarize long-form ones. This is mainly due to performance degradation caused by long-context prompts, the inherent difficulty of preserving temporal continuity and a lack of semantically rich concepts in event descriptions. To tackle these issues, this paper introduces the first recursive Video Language Summarization Model (RVLSM) designed for video processing and tailored to long-for...

---

### 47. Policy-Adaptive Credit Assignment for Spatial Reasoning with Verifiable Rewards

**Authors:** Hailiang Yang, Shengchao Chen

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26410v1)

**Summary:** Image-based spatial reasoning requires perception, decomposition, and inference, but the stage that limits accuracy can change during training. Answer-level rewards neither localize failures to individual stages nor provide discriminative group-relative feedback when all rollouts receive the same reward. Process supervision provides intermediate feedback, but fixed weights cannot adapt reward allocation to these changing bottlenecks. To address this gap, we propose CALIPER, an adaptive process-r...

---

### 48. LaMER: Language-Conditioned Multi-Expert Routing for Weakly Supervised Referring Expression Comprehension

**Authors:** Yu Yu Chang, Tzu-Hsuan Weng, Youssef Mohamed Amin, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26404v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26404v1)

**Summary:** Referring Expression Comprehension (REC) localizes the image region described by a natural language expression, underpinning applications such as autonomous navigation, human-robot interaction, and medical image analysis. Under weak supervision, REC is challenged by the visual-linguistic semantic gap and the difficulty of inferring region-text correspondences from coarse image-level signals alone. Moreover, no single visual encoder captures all complementary properties---semantic alignment, fine...

---

### 49. One Fact, Many Places: Redundant Evidence in Long Visual Documents Breaks Single-Gold Evaluation of Retrieval, Citation and Attribution

**Authors:** Xiaokang Yuan, Binhui Yao, Luwei Yang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26401v1)

**Summary:** Document understanding is increasingly judged on where an answer comes from, scored against annotated gold locations as if each fact lived in one place. In long visual documents, a fact often lives in several places: a chart value is restated in the text, a key figure reappears in the summary. We ask how often such copies occur in standard benchmarks and what they do to evaluation. We annotate 420 questions from MMLongBench-Doc and MMDocRAG with the locations that independently establish each re...

---

### 50. From Legacy to Contemporary: Scalable Color Modernization for Long Video

**Authors:** Dongyun Kim, Jiwoo Choi, Jaeseong Lee, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26391v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26391v1)

**Summary:** Bringing legacy video back to contemporary screens does not necessarily make it look contemporary. Earlier imaging pipelines often leave color casts, muted chroma, weak con- trast, and tonal imbalance, while correcting these character- istics still relies heavily on expert colorists and scales poorly to long, multi-shot videos. We formulate long video color modernization, a task that updates the chromatic and tonal appearance of legacy color footage while preserving scene content and coherence a...

---

## cs.LG

**50 papers**

### 1. Text-to-Image Generative Modeling Without Language Pretraining

**Authors:** Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26863v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26863v1)

**Summary:** Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with 18.2$\times$ less pretraining compute. Further, Halcyon-1.6B outperforms JiT-T2I-XXL/8+...

---

### 2. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

**Authors:** Yu Zhou, Cheng-Fu Yang, Rui Sun, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26860v1)

**Summary:** Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retai...

---

### 3. CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting

**Authors:** Zehao Wang, Jianpeng Yao, Yuping Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26852v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26852v1)

**Summary:** Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusions and out-of-distribution (OOD) scenarios, where individual robots may overlook potential risks or make inaccurate predictions. Leveraging cooperation effectively for both prediction and navigation remains a major chall...

---

### 4. WeAct: Dynamic Weight Switching as Agent Actions

**Authors:** Rui Shi, Xunjian Yin, Jiacheng Sang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26847v1)

**Summary:** Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capab...

---

### 5. Newton-Based Methods for Bilevel Optimization Beyond Lower-Level Strong Convexity

**Authors:** Youran Dong, Junfeng Yang, Wei Yao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26839v1)

**Summary:** Bilevel optimization provides a framework for machine learning tasks such as hyperparameter optimization, data reweighting, and meta-learning. Existing Newton-based bilevel methods typically rely on the classical hypergradient formula, which is generally unavailable when lower-level solutions are nonunique and the lower-level Hessian is singular. We develop two Newton-based methods beyond lower-level strong convexity by exploiting curvature shared by the lower-level and multiplier updates. Newto...

---

### 6. Kronecker Delta Rule for Long Context Linear Attention

**Authors:** Anamaria-Roberta Hartl, Levente Zólyomi, Michael List, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26834v1)

**Summary:** We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information compared with delta-rule updates, making it particularly well suited for long-context ...

---

### 7. Supervised Learning with Quantum Hamiltonian Embeddings

**Authors:** Riccardo Molteni, Minjun Jeon, Paolo Braccia, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26833v1)

**Summary:** Machine learning is widely regarded as a promising application in which quantum computing could offer a computational advantage. However, general quantum machine learning models with provable guarantees on performance, trainability, and efficient inference remain limited. In this work, we introduce quantum Hamiltonian embeddings, a supervised learning framework in which a classical training dataset is encoded into a single effective, parameterized Hamiltonian. Training optimizes the parameters o...

---

### 8. ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry

**Authors:** Matt Turk, Brandon L. Neel, Diana M. Lopez, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26829v1)

**Summary:** Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-structure tasks, using 4,249 rollouts from four frontier models and 4,486 further trials across 26 models. Three of the four frontier models fall within 0.031 of one another (0.785 to 0.816) with no difference between them r...

---

### 9. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis

**Authors:** Zhaoyang Wang, Qianhui Wu, Haorui Wang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26828v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26828v1)

**Summary:** Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interact...

---

### 10. MemT-1.0: Towards Memory-Native Evolution

**Authors:** Zhiyu Li, Zeyu Zhang, Linyun Liu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26825v1)

**Summary:** Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We further introduce Mixture-of-Storage to scale native memory capacity. Following ...

---

### 11. Next Best Action: Causal Constrained Offline RL for Business Action Targeting

**Authors:** Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26817v1)

**Summary:** Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints, and remain causally grounded. Existing approaches lack a rigorous framework for meeting these requirements jointly. We address this gap by formulating NBA as a Constrained Markov Decision Process (CMDP). We then integrate off-policy causal correction of the estimated customer dynamics directly int...

---

### 12. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding

**Authors:** Zhuofan Josh Ying, Guanglong Sun, Nolan Ho, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26802v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26802v1)

**Summary:** Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained backbones for brain encoding with a small number of trainable parameters. To make it c...

---

### 13. Learning to Refer: Inference-Time Collaboration in Decentralized Federated Learning

**Authors:** Yuheng Ma, Chendi Wang, Qiong Zhang

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26800v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26800v1)

**Summary:** In decentralized federated learning, heterogeneous clients may develop complementary expertise, yet each query is typically evaluated only by the client where it arrives. To exploit this distributed expertise without global coordination, we formulate inference-time collaboration as budgeted local expert referral, a graph-constrained routing process in which a query can move only between neighboring clients and only visited clients contribute to its final prediction. EdgeDRM implements this frame...

---

### 14. Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models

**Authors:** Agus Sudjianto, Denis Burakov

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26797v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26797v1)

**Summary:** Candidate-scoring decision models return a probability distribution over a presented set of answers. Public documentation of one such system, Jev, and of an open counterpart, JevAny, describes three training ingredients that determine what these probabilities estimate: soft targets from larger models, a frozen pretrained backbone and temperature calibration. We analyze each ingredient in Gaussian surrogates where the finite-sample risk can be computed exactly. A student trained on teacher target...

---

### 15. Two hidden layer suffice: the caterpillar net

**Authors:** Jakob Paul Zimmermann

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26795v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26795v1)

**Summary:** Every continuous piecewise linear (CPWL) function is a finite signed sum of maxima of affine functions, making maximum representation a central problem in the study of the expressiveness of ReLU networks. A now-disproved conjecture predicted logarithmic depth for maxima. Inspired by the proof by Brunck et al. (2026) that two hidden layers suffice for general CPWL functions, we give the Caterpillar Net, a nonrecursive construction for the maximum of $N$ inputs with two hidden layers of widths $O(...

---

### 16. On Data Scaling in Tabular ML: More Data, Better Generalization?

**Authors:** Ivan Rubachev, Nikita Lazarev, Artem Babenko

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26794v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26794v1)

**Summary:** Recent work in tabular machine learning has emphasized the importance of diverse and realistic evaluation settings. The niche of large-scale (1M+) data, however, remains under-explored. To study training-data scaling, we assemble eight real-world tabular datasets with up to around ten million training examples, retaining the natural distribution shifts of the tasks and using random-split evaluation as a control. We find that GBDTs and MLP-based models show broadly similar scaling trends, with ga...

---

### 17. Training with ML-labeled Data via Stochastic First- and Zeroth-Order Optimization

**Authors:** Maria-Eleni Sfyraki, Jun-Kun Wang

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26790v1)

**Summary:** Training a machine learning (ML) model is an optimization process that typically requires a set of examples with ground-truth labels beforehand. Obtaining these ground truths usually requires laborious human effort and can be costly. The scalability of human labeling becomes a concern when there are a large number of data points that need to be labeled. To address this practical issue, we consider an optimization setting where a subset of samples has ground-truth labels, while the remaining data...

---

### 18. Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books

**Authors:** Skander Lejmi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26789v1)

**Summary:** A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose distinct challenges. Three challenges underpin this research: adverse selection may cause a policy trained on real data to stop quoting; the consequences of a quote can arrive many steps after the action; and prediction-marke...

---

### 19. Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions

**Authors:** Steven Motta, Davide Mambelli, Alessandro Rozza

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26777v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26777v1)

**Summary:** Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from system capability. A task is represented by an interaction complex $K$ and a capacity sheaf $\mathcal{F}$; nonzero $H^n(K;\mathcal{F})$ defines a structural signature, while registered interventions test capability. For cocy...

---

### 20. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

**Authors:** Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26770v1)

**Summary:** Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated tests without access to ground-truth solutions or official tests. Specialized agents...

---

### 21. Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing

**Authors:** Adrian Remonda, Jiajun Xi, Nicklas Hansen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26757v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26757v1)

**Summary:** Reinforcement learning enables learning high-performance control policies, but its reliance on extensive interaction limits deployment on physical systems where data collection is costly, and failures are unsafe. We introduce Prior-Informed Adaptation (PIA), an offline-to-online model-based RL framework that uses structured simulation priors for rapid adaptation. PIA pretrains a world model on heterogeneous low- and high-fidelity simulated trajectories, then adapts it with limited target-domain ...

---

### 22. Trajectory Replay: Continuous-Time Mixture Transport for Lifelong Generative Models

**Authors:** Alessandro Palma, Charles Jones, Tristan Cinquin, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26749v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26749v1)

**Summary:** Adapting pre-trained continuous-time generative models to sequentially incoming data without forgetting earlier tasks is a central challenge in lifelong learning. A leading strategy, generative replay, uses a generative model trained on historical tasks to augment its own continual update with synthetic samples from experience. However, it requires full trajectory simulations at every training step, which accumulate discretization errors and can degrade the replayed historical distribution. Here...

---

### 23. Gradient descent reaches arbitrary accuracy in a fixed number of large steps on multiclass logistic regression

**Authors:** Andreea-Alexandra Musat, Nicolas Boumal

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26748v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26748v1)

**Summary:** We show that gradient descent (GD) with step size $η$ can achieve $\varepsilon$ optimality gap on the multiclass logistic regression loss in a number of iterations $T$ that is independent of $\varepsilon$. To do so, the step size $η$ must be chosen large enough as a function of $\varepsilon$ (and properties of the linearly separable dataset), while $T$ is a constant that only depends on the data. The relevant properties of the data include the number of points and their margin (for $T$), and one...

---

### 24. recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models

**Authors:** Saurav Jha, Qianli Liao, Robert Vernon, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26747v1)

**Summary:** Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. Test-time scaling offers a complementary path, but methods developed for autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked pLMs, where a...

---

### 25. Polar Switch: Fast Muon Orthogonalization with Polynomial Circuits

**Authors:** Zhehang Du, Weijie Su

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26742v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26742v1)

**Summary:** Muon, a 2024-born optimizer for language models, differs from the 2015-born spectral gradient descent mainly in its fast, GPU-friendly Newton--Schulz polynomial for orthogonalizing the gradient matrix. Accordingly, a line of research proposes faster polynomial iterations for gradient orthogonalization, such as Polar Express and Gram Newton--Schulz, both built on quintic polynomials. In this paper, we introduce Polar Switch, a new approach to polynomial gradient orthogonalization. Using simple po...

---

### 26. CAVA: Complementary-Label-Aware Data Valuation

**Authors:** Tan-Ha Mai, Hsuan-Tien Lin, Vu Nguyen

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26734v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26734v1)

**Summary:** Complementary-label learning (CLL) trains a classifier from labels that name a class an instance does not belong to. Such labels are cheap to collect from crowdworkers or vision-language models (VLMs), making them attractive for large-scale annotation. However, both sources can mistakenly assign the true class as the complementary label. Such annotation errors are particularly harmful in CLL because the model is explicitly trained to suppress the correct answer. Optimal transport (OT) data valua...

---

### 27. Cross-Fitting for Neural Posterior Estimation

**Authors:** Jeffrey Regier

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26733v1)

**Summary:** Neural Posterior Estimation (NPE) fits an amortized conditional density estimator to a simulated training set of complete-data realizations. NPE's training objective, log-likelihood, favors posterior approximations that assign arbitrarily high density to the training points, and typical families of amortized conditional density estimators (e.g., normalizing flows, Gaussian encoders) are flexible enough to oblige. The resulting policy of extreme overconfidence translates poorly to held-out data. ...

---

### 28. Injection of Space Radiation Errors on Low-power NVM using Generative Deep Learning

**Authors:** Eleonora Giudici, Antonio Miele, Luca Mottola

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26724v1)

**Summary:** We develop an error model for a Non-Volatile Memory (NVM) device that represents the effects of physical faults experienced in a CubeSat mission in Low Earth Orbit (LEO). The CubeSat carries an off-the-shelf low-power Ferroelectric RAM (FRAM) chip and runs repeated read/write tests according to a predefined pattern. We compare every memory snapshot received from the satellite with a reference bitmap to identify bit errors. We visually analyze erroneous values distributions in the memory snapshot...

---

### 29. Copying Under Repetition: From Prefix Matching to Position Hashing

**Authors:** Anxin Guo, Tianlong Huang, Chenxiao Yang, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26722v1)

**Summary:** Frontier LLMs can copy random text almost flawlessly, yet they often overrun or truncate long blocks of repeated characters. In repeated strings, matching local content no longer reliably identifies where copying should continue or when it should stop. Nevertheless, we show that a two-layer transformer with $O(\log\log N)$-bit precision and $O(\log N/\log\log N)$ width can copy every string up to a chosen design horizon $N$ and terminate correctly under arbitrary repetition. We use RoPE-style ro...

---

### 30. Deep Pontryagin Learning for Continuous-Time Stochastic Control with Jumps

**Authors:** Jean-Loup Dupret, Patrick Cheridito

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26718v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26718v1)

**Summary:** We develop a deep Pontryagin learning framework for high-dimensional continuous-time stochastic control problems that naturally accommodates jump-diffusions. In contrast to direct policy optimization, which repeatedly differentiates the objective through the entire time-discretized dynamics, our method separates adjoint learning from policy improvement by explicitly incorporating state-sensitivity information from the Pontryagin stochastic maximum principle. For a fixed Markov control, we first ...

---

### 31. Doubly Robust Learning of Heterogeneous Survival Treatment Effects under Time-Varying Treatments

**Authors:** Tomàs Garriga, Munib Mesinovic, Luke De Bretton-Gordon, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26710v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26710v1)

**Summary:** Estimating heterogeneous survival treatment effects (HSTEs) from time-to-event data under time-varying treatments is important in fields such as medicine (e.g., to decide which sequence of treatments is better in terms of survival probability). However, this task is challenging because treatment decisions, patient characteristics, and censoring probability often evolve together, requiring sequential adjustment for both treatments and censoring. Existing survival learners mostly consider a single...

---

### 32. GeoSplit: Selective Edge--Server Map Acquisition for Cross-User Travel-Mode Recognition

**Authors:** Zepu Wang, Luyao Niu, Ruolin Li, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26707v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26707v1)

**Summary:** Networked mobility sensing couples local trajectory inference with remote geospatial context, making communication decisions part of the prediction system. We present GeoSplit, an edge--server framework for travel-mode recognition that separates the utility of map evidence, its training-time transfer, and its selective acquisition at runtime. On GeoLife with 10% labels, we evaluate these components under user-day and user-disjoint grouping. For unseen users, aligned full-map context raises macro...

---

### 33. Parallel Language Models via Variational Decoding

**Authors:** Felix Draxler, Robin C. Geyer, Daniel Geyfman, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26693v1)

**Summary:** Autoregressive language models emit one token per forward pass. This causes high inference latency, in particular as models are scaled up for quality. In this paper, we introduce Parallel Language Models (PLMs), which generate mutually consistent tokens in one forward pass by routing dependencies through latent auxiliary variables. PLMs are trained using a variational bound that reduces to an autoregressive loss plus a parallel decoding loss. Empirically, PLMs are on a faster and better Pareto f...

---

### 34. Intra-Rubric Reward Divergence: Mitigating Rubric Hacking through Latent Dimension Recovery and Balancing

**Authors:** Jianqiang Xia, Han Xu, Dianxi Shi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26685v1)

**Summary:** Rubric hacking limits both performance and training robustness in rubric-based reinforcement learning. By decomposing rubrics into sub-dimensions, we reveal the Intra-Rubric Reward Divergence: as the total rubric score increases, certain sub-dimension scores systematically decrease, suggesting the model sacrifices specific quality aspects to optimize the aggregated objective. From the sub-dimension perspective, we observe two phenomena: (1) dimension imbalance, causing the policy to favor heavil...

---

### 35. Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows

**Authors:** Qian Xie, Wenyue Hua, Yueli He, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26676v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26676v1)

**Summary:** LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple candidates. We introduce Cost-Coupled Gittins (CC-Gittins), a multi-objective extension of single-objective cost-aware Gittins search for Pareto recommendation. It exploits the coupling between evaluation and deployment co...

---

### 36. PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization

**Authors:** Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26671v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26671v1)

**Summary:** Multi-agent approaches have been investigated recently as a means of improving the scalability of reinforcement learning for neural combinatorial optimization. Existing methods assume that all problem instance information is known upfront. However, real-world problems are often dynamic: relevant information is progressively revealed as the agents take actions (e.g., arriving at an edge in a routing problem only to discover it is untraversable). In such cases, existing methods fail to coordinate ...

---

### 37. Nested Shared-Operator Recursion on ARC-AGI-1: An Empirical Study of HRM, TRM and URM

**Authors:** Sara Neri, Eugenio Gaeta, Andrea Ceschini, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26666v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26666v1)

**Summary:** Recursive reasoning models refine persistent internal states by repeatedly applying learned operators. We investigate whether adding a persistent intermediate state that integrates repeated updates of a faster state through the same operator improves predictive performance relative to each model family's baseline at matched parameter counts. We define this organisation operationally and implement it within three architectures: the Hierarchical Reasoning Model (HRM), Tiny Recursive Model (TRM) an...

---

### 38. The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training

**Authors:** Haonan Huang, Chengkun Cai

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26655v1)

**Summary:** Language models can change a committed answer to accommodate a user's opinion or pushback without new evidence. However, when this behaviour develops during training and what a released model inherits from earlier stages remain unclear. We follow 741 checkpoints of 30 open model lineages, from early pretraining to released models. We plant initial verdicts on moral scenarios and measure how far a model follows a user's stated opinion or abandons its verdict under pressure. In most lineages the b...

---

### 39. The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models

**Authors:** Aaron Maiwald, Roderick McNeill, Jaeyoung Lee, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26651v1)

**Summary:** Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filtering viral proteins from the pretraining data meaningfully degrades masked language modelling, mutation effect prediction and long-range contact prediction on viral proteins, while largely preserving performance on non-viral proteins. These effects are concentrated among protein...

---

### 40. When the harness decides success: state that cannot be re-observed

**Authors:** Raimondas Lencevicius

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26632v1)

**Summary:** Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fa...

---

### 41. VaDar: Implicit Goal Conditioning via Value Disaggregation

**Authors:** Shashwat Saxena, Mehul Goel, Sreyas Venkataraman, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26629v1)

**Summary:** Long-horizon tasks are important for modern AI and robotics, yet pose a challenge for reinforcement learning. Historically, a popular approach has been to decompose a task into subgoals, and learn a subgoal-conditioned policy to execute each subtask in sequence.   We introduce an alternative called Value Disaggregation (VaDar), which trains a single subgoal-independent policy to maximize a linear combination of per-subgoal critic values. Because subgoal information is needed only at training-tim...

---

### 42. SleepPairNet: Learning Multimodal Pediatric Sleep Representations with Random-Pair Cross-Attention

**Authors:** Saurav Raj Pandey, Harlin Lee

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26628v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26628v1)

**Summary:** Analyzing physiological sleep signals is important for assessing sleep quality and detecting sleep-related disorders. Learning inter-modal relationships across physiological signals can provide richer representations for downstream sleep analysis. We introduce \textbf{SleepPairNet}, a multimodal self-supervised learning (SSL) framework that learns pairwise interactions between physiological signals through cross-attention. We propose a random modality-pair selection strategy that exposes the mod...

---

### 43. Global Time-Aware Conditioning (GTC): A Mechanism for Time-Aware Pediatric Sleep Representation Learning

**Authors:** Saurav Raj Pandey, Harlin Lee

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26618v1)

**Summary:** Sleep physiology evolves throughout the night, with changes in sleep cycles, respiratory stability, and cardiovascular dynamics. However, self-supervised learning (SSL) methods for sleep typically process short, fixed-duration windows without explicitly modeling where each window occurs within the full sleep session. We introduce Global Time-Aware Conditioning (GTC), a mechanism that complements local positional encodings by conditioning latent representations on the global time-of-sleep of each...

---

### 44. Degree Bounds for Separating Polynomial and Neural Invariants for Point Clouds

**Authors:** Snir Hordan, Harm Derksen, Mircea Petrache, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26612v1)

**Summary:** Neural networks that respect the symmetries of point clouds commonly compute high-order representations of the rotation group to improve their expressivity. Such models are known to be universal, and thus able to separate any pair of point clouds, when using representations of sufficiently high order, yet no precise bound on this order, as a function of the number of points, was previously known. We establish the first quadratic lower and upper degree bounds for polynomials that separate point c...

---

### 45. A Probabilistic, Rotation-Preserving Kernel Operator Surrogate for Continuum-Robot Design Spaces

**Authors:** Branden Frieden, Alan Kuntz, Varun Shankar

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26605v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26605v1)

**Summary:** We develop an uncertainty-aware, operator-learning-based surrogate for tendon-driven continuum robots (TDCRs) that generalizes across robot design and actuation while predicting the complete equilibrium configuration. Our central idea is a nonstationary Gaussian-process (GP) kernel whose metric is learned by a shallow neural network from mechanics-aware design coordinates. The network learns how similarity changes across design space, while the resulting kernel defines the design-to-pose operato...

---

### 46. ITU-DESC: a missingness-aware machine-learning dementia risk score in the UK Biobank cohort

**Authors:** Abdullah Kavaklı, Faik Boray Tek

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26604v1)

**Summary:** Background: Existing dementia risk scores rely on fixed, pre-selected features and linear models, or ignore bias from informative missingness in cohort data. Here we introduce the Istanbul Technical University Dementia Risk Score (ITU-DESC), an explainable machine-learning score for incident all-cause dementia that combines broad feature selection across roughly 8,000 candidate features with explicit control of missingness bias.   Results: We studied approximately 500,000 UK Biobank participants...

---

### 47. Bombadil: A Foundation Model for Plant Electrophysiology

**Authors:** James Kirk, Piotr Bednarski, Filip Twardy, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26597v1)

**Summary:** Living plants, like animals, use electrical signals to carry information about their physiological state across their body, from roots to branches. These signals can be recorded, as they are in animals, from a pair of differential extracellular electrodes inserted into signal-conducting tissue. While machine-learning models have been trained to predict specific plant stress states from these signals, each of these models has been trained for only a single task and none have been designed to tran...

---

### 48. Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates

**Authors:** Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26595v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26595v1)

**Summary:** Jailbreak methods are commonly compared using Attack Success Rate (ASR), but these comparisons depend on how responses are generated and judged. In this paper, we examine eight attacks against three open-weight language models using three evaluation procedures. Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions. Changing the number and arrangement of attempts reverses the ranking of DeepInc...

---

### 49. WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting

**Authors:** Arjun Ashok, Mihir Parmar, Palash Goyal, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26582v1)

**Summary:** Recent time series foundation models (TSFMs) can consume covariates in-context, extending zero-shot forecasting to problems driven by external factors. This enables scenario analysis: forecasting how a target responds to events that set covariates to chosen future values. Whether they can do this reliably is an open question. We introduce WhatIf-Bench, a benchmark measuring how well forecasters use covariates to forecast a target's response to future events. WhatIf-Bench is semi-synthetic: time ...

---

### 50. SafeWall: A Risk-Aware Job Walltime Recommendation for HPC Scheduling

**Authors:** Kanglin Xu, Michael Papka, Zhiling Lan

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26577v1)

**Summary:** In high-performance computing (HPC), users must submit resource requirements for their jobs, with user-supplied walltime being a critical parameter. However, these estimates are notoriously inaccurate, as users tend to overestimate walltime to prevent the scheduler from terminating their jobs prematurely. While existing work on learning-based walltime prediction primarily focuses on maximizing prediction accuracy, such predictions are inherently risky for walltime recommendations. Specifically, ...

---

## cs.NE

**50 papers**

### 1. Hybrid metaheuristics for architectural design optimization under small evaluation and wall-clock budgets

**Authors:** Luciano Ambrosini

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26202v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26202v1)

**Summary:** Architectural and structural design optimization in parametric software affords about a thousand evaluations of an expensive model for problems with tens of variables, a regime for which most metaheuristics were not designed. On the side of artificial intelligence, two hybrid metaheuristics are proposed: a covariance matrix adaptation evolution strategy (CMA-ES) whose sampling is enriched with differential-evolution trial vectors, and a particle swarm with success-history parameter adaptation, d...

---

### 2. A Spiking Ring-Attractor Architecture for Representation and Control of Revolute Robot Joints

**Authors:** Aung Htet, Alejandro Rodriguez Jimenez, Ruidong Ma, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26027v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26027v1)

**Summary:** Robotic systems with revolute joints evolve on circular state spaces, yet most control architectures represent these states using Euclidean variables that ignore this underlying geometry. We propose a fully spiking neural control architecture in which ring attractors encode joint states, enforcing representations consistent with the topology of revolute systems. Homeostatic regulation computes goal-state mismatch directly over these distributed representations, and opponent gain-modulated popula...

---

### 3. Sector-Ring Linear Reservoirs: Sector-Wise Decay-Timescale Allocation With State Reuse Across Candidate Settings

**Authors:** Yudai Ebato, Sou Nobukawa, Yusuke Sakemi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25806v1)

**Summary:** In reservoir computing, performance depends on whether the fixed dynamics of the reservoir suit the task, and the appropriate memory length and frequency response differ across tasks. The reservoir settings are found by a search on each task, and driving the reservoir with the input and collecting its states for every candidate setting dominates the cost of the search. In a reservoir with a linear recurrence, the dynamics decompose into modes, one per eigenvalue, and the eigenvalue distribution ...

---

### 4. Peer-Relative Trust-Guided Update Screening for Robust Semi-Decentralized Federated Learning under Label-Flipping Attacks

**Authors:** Ajay Kumar Shrestha, Sandhya Joshi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25714v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25714v1)

**Summary:** Trust and reputation mechanisms can reduce the influence of malicious clients in federated learning (FL), but strict update filtering is difficult under non-independent and identically distributed (non-IID) data because honest local updates may temporarily reduce performance on a shared validation proxy. Building on our earlier trust-based semi-decentralized FL (SDFL) framework, this paper operationalizes the trust signals and introduces peer-relative update screening that combines a robust vali...

---

### 5. Let Them Sleep: Recursive Self-Pruning Memory for Long-Horizon LLM Agents

**Authors:** Kargi Chauhan, Sadiba Nusrat Nur, Pratibha Revankar, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25561v1)

**Summary:** Agents that run for a long time have a memory problem, and it is not the one most systems optimize for. Storing every trace and retrieving the nearest neighbors works early and quietly stops working later: the store fills up with failures the agent then repeats, and with facts that were true fifty turns ago. RSPM (Recursive Self-Pruning Memory) borrows the fix biology already found. At intervals the agent sleeps. It clusters its recent failures, distills each cluster into a short rule, and delet...

---

### 6. Small-scale neural simulation of Caenorhabditis elegans on Loihi-2 using NeuroML2Loihi

**Authors:** Danny Rosen, Ramashish Gaurav, Yang Yi

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25424v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25424v1)

**Summary:** Neural simulation is an essential methodology for studying biological nervous systems, but it remains limited by the computational costs of repeatedly updating neural and synaptic states over many timesteps. Neuromorphic hardware is a promising substrate for this class of workloads because such devices combine event-driven execution, localized memory, and spike-based communication. However, neuromorphic \textit{software} remains comparatively fragmented and difficult to integrate with the model-...

---

### 7. Length-Independent Stability and $L_2$-Gain Certificates for Chains of Delayed Neural Modules

**Authors:** Ömer Faruk İşcanlı

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25147v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25147v1)

**Summary:** Networks of repeated neural modules with delayed neighbour coupling need stability guarantees for every number of modules, but delay-dependent criteria certify one network at a time and grow with its size. This paper derives stability and $L_2$-gain certificates of length-independent size for open chains and rings of modules of two alternating types with slope-restricted activations. A local and a transmission delay act independently and are only bounded and continuous. A Lyapunov-Krasovskii fun...

---

### 8. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

**Authors:** Takashi Ishida, Taro Makino, Issa Sugiura

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23470v2) | 📄 [PDF](https://arxiv.org/pdf/2610.23470v2)

**Summary:** Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to target, comparing diverse, well-reasoned options can be more useful than a single ...

---

### 9. Algorithm Modelization: Transforming Optimization Algorithms into Evolvable Intelligence

**Authors:** Jian Yao, Zhiyao Zhang, Yichen Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23161v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23161v1)

**Summary:** Can algorithms be learned and evolved as models, rather than repeatedly redesigned as programs? We explore this question by introducing Algorithm Modelization, a new paradigm that turns iterative algorithms into trainable models. Its central idea is to regard algorithm execution trajectories as computational experience: by learning how algorithmic states evolve over iterations, a model can internalize the knowledge embodied in existing algorithms, reproduce their computational behaviors, and fur...

---

### 10. Wavelength Diversity Expands the Expressive Power of Optical Computing

**Authors:** Shiqi Chen, Che-Yung Shen, Parnian Ghapandar Kashani, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23070v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23070v1)

**Summary:** Universal function approximation underpins neural networks' capacity to represent nonlinear relationships, but realizing this capability in optical hardware requires engineering the computational features encoded in light. Here, we show that wavelength diversity enhances optical function-approximation expressivity through wavelength-scaled Fourier features generated by a shared phase encoder, without increasing the number of input-encoded harmonics. Multiple wavelengths contribute to the represe...

---

### 11. SpikeQ: Spike-Guided Post-Training Quantization for Spiking Neural Networks

**Authors:** Kai Sun, Peibo Duan, Zhanglu Yan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23046v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23046v1)

**Summary:** On neuromorphic chips, spiking neural networks (SNNs) consume far less energy than artificial neural networks (ANNs), but the limited memory of these chips requires low-bit synaptic weights and membrane potentials. Existing post-training quantization (PTQ) methods provide them without retraining and, like those for ANNs, minimize numerical errors such as the mean squared error (MSE). In an SNN, however, a quantization error reaches later layers only through the spikes it flips. We find that erro...

---

### 12. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 13. A restart rule for genetic algorithms based on Schnabel census

**Authors:** Anton Eremeev, Yulia Zakharova

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22211v1)

**Summary:** A new adaptive restart rule for Genetic Algorithms (GAs) is considered. The rule is based on the Schnabel Census method, originally developed for statistical estimation of a size of animal population. In this paper, the Schnabel Census method is applied as a heuristic to estimate the number of different solutions that may be visited with positive probability, given the current distribution of offspring. The rule consists in restarting a GA as soon as the maximum likelihood estimate reaches the n...

---

### 14. Attention over noisy examples: generalization and memorization in the exponential Hopfield network

**Authors:** Francesco Alemanno

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22191v2) | 📄 [PDF](https://arxiv.org/pdf/2610.22191v2)

**Summary:** In Hebbian learning from examples, a Hopfield network retrieves archetypes seen only through noisy examples. We study it in the exponential Hopfield model: one softmax attention step with the unlabelled examples as keys. A signal-to-noise analysis gives the overlap with an unseen archetype in closed form: a majority-rule law in which an attention entropy replaces the dataset entropy. At high temperature the archetype is lost in the crosstalk; at low temperature the softmax freezes on the closest...

---

### 15. Beyond the Hamming Cliff: Compact Spatial Encodings Preserving Semantic Distance in Spiking Neural Networks

**Authors:** Sergio Davies, Muhammad Aitsam, Morgan-Tyler Stone, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22083v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22083v1)

**Summary:** By pre-processing input signals with Gray, Thermometer, Johnson and hybrid encodings before passing them to spiking neural networks running on SpiNNaker hardware, Davies et al.(2025) address the semantic-spatial disparity that causes the ``Hamming cliff'' in standard binary representations. Continuous semantic patterns are presented as a set of simultaneous spikes at the input layer, preserving ultra-low latency processing. Training the network on multiple continuous values under each scheme, an...

---

### 16. Approaching Backpropagation Accuracy with Weight Perturbation on MNIST

**Authors:** Patrick Inoue

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21665v1)

**Summary:** Weight perturbation (WP) estimates learning directions from random parameter perturbations and a scalar change in loss, without backpropagating derivatives. We examine how batch size, training duration, and estimator stabilization affect its attainable accuracy in fully connected MNIST networks. In the shallow configuration, large-batch training reaches approximately 97\% test accuracy, compared with an early backpropagation (BP) reference near 97.5--98\%. The same comparison exposes a substanti...

---

### 17. First Mathematical Runtime Analyses of Evolutionary Multitask Multi-Objective Optimization

**Authors:** Danyang Zhang, Weijie Zheng

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21311v1)

**Summary:** To facilitate the solving of complex problems, evolutionary multitask optimization is regarded as a promising technique due to its capacity for cross-task knowledge transfer. In contrast to empirical evidences, no mathematical runtime support exists for this technique within the domain of multi-objective optimization. In this work, we aim to fill this important gap. We analyze how the representative multiobjective multifactorial evolutionary algorithm (MO-MFEA) covers the Pareto fronts of two bi...

---

### 18. IWOO: Wave Optics Optimizer Improved with Hybrid Strategies for Numerical Optimization and Engineering Applications

**Authors:** Rui Du, Yaming Zhang, Yongpeng Wen, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.23994v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23994v1)

**Summary:** The Wave Optics Optimizer (WOO) incorporates optical diffraction and interference into numerical optimization and has shown competitive performance in benchmarks and engineering applications. However, it can converge slowly, become trapped in local optima, and lose search effectiveness in later iterations. This paper proposes an Improved Wave Optics Optimizer (IWOO) that integrates four complementary strategies. First, a good point set and opposition-based learning are combined in GPS--OBL initi...

---

### 19. Controlling the latency in temporal coded spiking models for neuromorphic datasets

**Authors:** Alban Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19732v1)

**Summary:** Exploiting temporal information in datasets with high temporal dependencies (such as spoken keyword recognition) by spiking models is still an open problem. Promising frameworks include Time-To-First coding (TTFS) and the inclusion of synaptic delays into learning. In TTFS, neurons are forced to spike at most once, forcing the network to found its learning on the spiking times of neurons rather than their spiking rate. Some models use the TTFS framework to directly compute the spiking time of In...

---

### 20. When the implementation matters more than the algorithm: NSGA-II and other multi-objective optimizers in engineering design tools

**Authors:** Luciano Ambrosini

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.22397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22397v1)

**Summary:** Engineering design tools increasingly embed optimizers as ready-made components that users select by algorithm name, while operator settings and bound, integer and duplicate handling stay fixed inside each tool. This study tests whether the name predicts the result. A tool-agnostic harness exposes one deterministic black box, an emulator of a published 22-variable mixed-integer building-performance problem, to the native optimizers of three Grasshopper plug-ins, to canonical NSGA-II, SMS-EMOA an...

---

### 21. Design and Analysis of Temporal Representations in Neural Networks

**Authors:** Alban Colas-Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19730v1)

**Summary:** The ability to represent temporal information is often hypothesized to underlie the efficiency and learning capabilities of biological neural networks. This motivates the development of spiking neural networks. However, it remains unclear how temporal information is actually represented in neural networks and how different forms of temporal representation affect performance and computational efficiency. We introduce the notion of the degree of temporal representation of a neural network, defined...

---

### 22. A Time-Variant Spiking Neuron from a Unified State-Dynamics Perspective

**Authors:** Jing Yang, Qianhui Liu, Gang Pan, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.23981v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23981v1)

**Summary:** Spiking neural networks (SNNs) have increasingly incorporated rich neuronal dynamics to enhance temporal processing. However, richer dynamics do not necessarily enable neurons to adapt how information is processed over time. To examine this issue systematically, we introduce a unified state-dynamics framework that characterizes diverse spiking neurons through a common formulation and enables direct comparison of their dynamical designs. The framework reveals a common limitation of existing neuro...

---

### 23. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 24. Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine

**Authors:** Thomas Hannagan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19220v2) | 📄 [PDF](https://arxiv.org/pdf/2610.19220v2)

**Summary:** The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Thinking steps are attracting but strongly non-normal maps exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already presen...

---

### 25. LLM Evolutionary Search Strategies Should be Compared by Tokens

**Authors:** Tal Oved, Roi Pony, Oshri Naparstek, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23977v1)

**Summary:** LLM evolutionary search is currently evaluated by counting proposals (candidate programs). We demonstrate this metric hides the true cost of search, and redo the comparison using tokens. By replaying 600 logged runs across 5 tasks and 3 methods, we show that proposal costs vary wildly from 16k to 39k tokens. In equal-proposal comparisons, this silently grants some methods up to 1.9x the compute of others, and gives evolution roughly 6x the budget of independent sampling. When we match token budg...

---

### 26. Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization

**Authors:** Bum Jun Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18085v1)

**Summary:** We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the m...

---

### 27. Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**Authors:** Francesco Panetta, Federico Di Valerio, Michela Proietti

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17998v1)

**Summary:** Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only expla...

---

### 28. Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation

**Authors:** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17969v1)

**Summary:** Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...

---

### 29. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 30. FidLIF: Parallel Training of High-Fidelity Spiking Neurons with Exact BPTT

**Authors:** Kaixiang He, Yujie Wu

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16924v1)

**Summary:** Although spiking neural networks (SNNs) show promise in energy-efficient computing through event-driven computation and stateful temporal processing, their recurrent membrane dynamics render their training inherently sequential and inefficient for long sequences. Existing methods achieve full-sequence parallelism in SNNs through two main strategies: redesigning or approximating spiking dynamics to avoid reset-coupled temporal dependencies, or relying on iterative relaxed fixed-point solvers that...

---

### 31. Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**Authors:** Huan Luo, Na Lu, Xiaopeng Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16921v1)

**Summary:** Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...

---

### 32. DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning

**Authors:** Yuxiang Zeng, Kun Xie, Yang Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16822v1)

**Summary:** Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...

---

### 33. naspaclust: A hybridisation of spatial fuzzy clustering with nature-inspired optimisation

**Authors:** Bahrul Ilmi Nasution, Rezzy Eko Caraka, Robert Kurniawan

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16356v1)

**Summary:** We present an overview of R package called \texttt{naspaclust}, a tool for spatial fuzzy clustering improvement by hybridising the Fuzzy Geographically Weighted Clustering (FGWC) with nature-inspired optimisation algorithms. There are seven optimisation algorithms in general, namely Artificial Bee Colony, Flower Pollination Algorithm, Gravitational Search Algorithm, Harris-Hawk Optimisation, Intelligent Firefly Algorithm, Particle Swarm Optimisation, and Teaching-Learning Based optimisation. The...

---

### 34. CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization

**Authors:** Yuqing Cheng, Yan Jia, Yanjie Song, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16158v1)

**Summary:** Conflict-graph search can stagnate despite effective operators when interventions fail to address the conflicts blocking progress. A disruptive intervention may also require further search before its value emerges. We propose CIPHEUR, a large language model (LLM)-guided framework that connects conflict evidence to coordinated intervention and recovery through Structured Intervention Units (SIUs). The shared control interface supports offline synthesis of executable policies and online contextual...

---

### 35. Where Polanyi Meets Galois: Tacit Knowing as an Algebro-Deterministic Operation, Toward Re-rooting AI-Generated Science

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16102v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16102v1)

**Summary:** We argue that tacit knowing is better modelled as an operating regime of one memory substrate than as a kind of content. The substrate is VaCoAl, an algebro-deterministic XOR-and-shift hyperdimensional memory over GF(2), realized as CASRAM (commercial SRAM-CAM) and PyVaCoAl (DRAM-CAM).In VaCoAl/PyVaCoAl a directed acyclic graph (DAG) reads two ways. Repairing every collision (Rescue mode) makes the trace exactly auditable but ranks no path higher; tolerating collisions (Don't Care mode) yields a...

---

### 36. How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility

**Authors:** Toru Takahashi

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15830v1)

**Summary:** When several predictions use the same internal representation, information about some targets can remain easier to recover than information about others. We study how this specialization forms, persists, and changes in minimal artificial learners. With reconstruction errors weighted equally during learning, changing which target is observed precisely selects the favored target and redirects an already specialized learner. Removing current support can reduce a formed bias, whereas state-following...

---

### 37. REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming

**Authors:** Abrar Alotaibi, Moataz Ahmed

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15513v1)

**Summary:** Safety-aligned large language models (LLMs) remain vulnerable to adversarial prompts that bypass their safety training. Existing automated red-teaming methods either require privileged access unavailable in production, rely on manually engineered per-model templates, or optimize a single objective without population-level diversity. We present REPRO (Reflective Evolutionary Prompt Optimization), a pure black-box framework that discovers adversarial prompts through evolutionary optimization drive...

---

### 38. CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining

**Authors:** Ziteng Sui, Junfeng Xia, Wenhao Ye, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15450v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15450v1)

**Summary:** Functional magnetic resonance imaging (fMRI) commonly characterizes large-scale brain organization through functional connectivity (FC). However, an observed FC matrix is not a fixed brain graph but a statistical estimate determined by the finite BOLD frames used to compute it. Conventional FC-based approaches typically represent each scan with a single Pearson-correlation matrix, leaving frame-resolved variations in regional interactions unexploited. To address this limitation, we introduce CoF...

---

### 39. FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies

**Authors:** Yifeng Mao, Yuze Feng, Yutong Shen, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15307v1)

**Summary:** Efficient neural architecture search (NAS) requires accurate performance estimation under limited evaluation budgets. Existing zero-cost proxies (ZCPs) provide fast training-free signals, but each proxy usually captures only a partial property of an architecture, leading to unstable rankings across datasets and search spaces. In contrast, GNN-based predictors can improve accuracy, but often depend on labeled architectures, graph encoders, and costly representation learning, which makes them less...

---

### 40. Compute-Optimal Scaling Laws for Spiking Language Models

**Authors:** Dan Saunders, Benjamin Ren, Catherine He

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15146v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15146v1)

**Summary:** Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N...

---

### 41. RELAGRAM: Recursive Latent Graph Model for the Capacitated Vehicle Routing Problem

**Authors:** Vladimir Kirill Bickov, Neil Yorke-Smith

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15106v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15106v1)

**Summary:** Latent recursion repeatedly processes internal representations through the same neural network. Recent work has shown this approach to be effective on structured reasoning tasks such as Sudoku and maze solving. However, whether latent recursion can support neural routing remains unclear. We introduce RELAGRAM (Recursive Latent Graph Model), a novel approach that brings latent recursion to graph combinatorial optimization. RELAGRAM encodes a capacitated vehicle routing problem (CVRP) instance as ...

---

### 42. PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation

**Authors:** Alex Gower

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14409v2) | 📄 [PDF](https://arxiv.org/pdf/2610.14409v2)

**Summary:** Generating an image with a diffusion or flow-matching model typically involves integrating a velocity field for hundreds of sequential steps. That computation suits a GPU poorly and an analog neuromorphic substrate well, where one fast, low-power physical relaxation could replace the whole sequence. Two things are needed: a generative algorithm whose computation is a relaxation, and a way to train it without backpropagation, whose global gradient transport is hard to realise in analog. Energy Ma...

---

### 43. Do Artificial Neural Networks Need Dendritic Nanotubes? Two Reasons for Shrinking Importance Estimates in Continual Learning

**Authors:** Saurav K. Aryal

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.14258v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14258v1)

**Summary:** Regularization-based continual learning protects each parameter in proportion to an estimate of its importance, yet these estimates come from finite samples and heuristics and are used as if they were exact. We report four studies that start from a biologically inspired mechanism and end with a statistical explanation of it. Motivated by dendritic nanotubes, we let transient lateral links diffuse importance tags between hidden units. Links between co-active units gave no significant gain, but ra...

---

### 44. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 45. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 46. REMBGO for Evaluation-Limited Optimization: CEC2022 Benchmarking and EAF-STATCOM Generalization

**Authors:** Vikram Chekuri, Narapareddy Ramarao, Prashanth N A

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13471v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13471v1)

**Summary:** Metaheuristic comparisons are often reported at evaluation budgets far larger than an expensive engineering simulation can afford. This paper presents REMBGO, an evaluation-budget-aware refinement of EMBGO. Its contribution is not any single operator: it is the integration of population preservation, scale-normalized exploration and recovery mechanisms whose parent-relative benefit is concentrated under restricted function-evaluation budgets. REMBGO is evaluated on CEC2022 at a primary, applicat...

---

### 47. The value of information and the emergence of communication in evolved e-puck robots

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13118v1)

**Summary:** We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Em...

---

### 48. Universal Construction and Exact Self-Reproduction in Ternary McCulloch-Pitts Networks

**Authors:** Charles C. Norton

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12251v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12251v1)

**Summary:** A fixed network of McCulloch-Pitts threshold units with weights in {-1,0,1} can hold other threshold networks in its state and run them: the state is a ring of banks of records, each record a unit of a stored network, and each step evaluates one record. We use such a network to carry out von Neumann's universal construction and self-reproduction exactly. As a cellular automaton keeps its rule, the fixed network keeps its weights, and what reproduces is a stored network. A constructor of 143 reco...

---

### 49. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

**Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12183v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12183v1)

**Summary:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their resul...

---

### 50. EliteTable: Self-Improving Program Search for Executable Control Policies

**Authors:** Stuart Farmer

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12536v1)

**Summary:** EliteTable is a self-improving program-search algorithm guided by large language models (LLMs) that uses a fixed-capacity table of high-scoring solutions to guide new proposals, edits of existing solutions, and remixes of several solutions. Performance was evaluated across six Gymnasium control tasks, each with ten generations and fifty candidate slots per generation. Each task was evaluated across ten independently initialized searches. Candidate-score medians rose between the first and final g...

---

## q-bio.NC

**50 papers**

### 1. Affective Valence as the Interoceptive Rate of Change of Jacobian Scale

**Authors:** David Balduzzi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26350v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26350v1)

**Summary:** Affect is widely held to depend on interoception. This paper proposes that valence is the rate at which interoception moves a self-sustaining system's responsiveness relative to its terminal set (roughly, death). Responsiveness is formalised as the scale of the system's Jacobian and interoception as its internal inputs: receptors, signals and forecasts of its energy reserve. Changes in responsiveness that bypass interoception, such as brain damage, are not felt. Language models have no valence b...

---

### 2. PyGPLA: A Python Package for Generalized Phase Locking Analysis

**Authors:** Amir Khani, Christian Beste, Shervin Safavi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26304v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26304v1)

**Summary:** Spike-field couplings measure the links between neuronal spiking and local field potential (LFP) and provide a tool to study how neural populations coordinate activity across spatial and temporal scales. While modern high-density electrophysiology enables the simultaneous recording of numerous LFP channels and neuronal units, this massive scale poses significant statistical and computational challenges for conventional pairwise coupling analyses. The number of channel-unit comparisons grows rapi...

---

### 3. HP-GSBS: Accelerating greedy state boundary search with reusable interval statistics

**Authors:** Yanzhe Zhao, Yongzhang Ji

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25898v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25898v1)

**Summary:** Greedy State Boundary Search (GSBS) identifies transitions between relatively stable neural activity patterns, but repeated candidate evaluation makes large analyses expensive. HP-GSBS is an open-source Python package that reorganizes the search around reusable interval contributions and correlation statistics. Streaming candidate reduction and local refinement further reduce repeated work; CPU, PyTorch CUDA and Triton backends share sequential segmentation decisions. Across seven controlled wor...

---

### 4. Simulating Infant Senses with Age-Tuned Networks

**Authors:** Somesh Mohapatra

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25377v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25377v1)

**Summary:** What a newborn sees, hears and feels, and how this changes month by month, has been measured sense by sense, with different methods and in different units. We bring these measurements together for the first two years of life and ask whether small neural networks tuned to a given age can turn them into a quick, inspectable simulation of sensory perception. Each sense's immaturity is written as a fixed, age-indexed filter on the input, and a small prediction network learns behind it over the first...

---

### 5. Spontaneous brain-wide rotational dynamics constrain cue-evoked behavior

**Authors:** Sihan Chen, Yunlong Xu, Doruk Efe Gökmen, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25061v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25061v1)

**Summary:** Uncovering low-dimensional representations of brain-wide neural dynamics and their relationship to behavior remains a central challenge. Here, we show that spontaneous brain-wide rotational dynamics constrain cue-evoked behavior and learning. To systematically establish these findings, we developed a dimensionality-reduction technique called Rotational Component Analysis (RCA) that optimizes the detection of low-variance rotational modes even within individual trials. We applied RCA to motor-cor...

---

### 6. Longitudinal fMRI reveals multi-network reconfiguration and a recurrent frontoparietal shift across rest and task states during adult aging

**Authors:** Tingshan Liu, Wanxin Dong, Hairong Zheng, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24433v1)

**Summary:** Functional connectivity changes across adult aging, but most evidence is cross-sectional, and covariance-based connectivity depends on blood oxygenation level dependent (BOLD) fluctuation amplitude. Covariance decline can reflect changing fluctuation amplitude, and its interpretation may depend on whether normalization uses signal amplitude or includes estimated noise. It is also unclear which longitudinal changes recur across brain states. We analyzed 852 adults (baseline age 36-89 years) from ...

---

### 7. Spaceflight-associated Motion Sickness in Commercial Crew Astronauts

**Authors:** Torin K. Clark, Aaron A. Allred, Jaime Mateus, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24216v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24216v1)

**Summary:** Spaceflight-associated motion sickness, including space motion sickness (SMS) and terrestrial readaptation motion sickness (TRMS), has presented as the most operationally limiting effect on the human in the days following a gravity transition. Published data suggest that astronaut head movements provoke symptoms, but those studies rarely controlled for them. Most previous studies use postflight retrospective reporting and have not quantified temporal dynamics or persistence of symptoms; no study...

---

### 8. Deep LLM layers expose passage-level context in EEG during silent reading

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23638v1)

**Summary:** In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...

---

### 9. Distributional signatures of computation: inferring mechanisms from computation time distributions

**Authors:** Céline van Valkenhoef, Catherine Schuman, Nikolaus Kriegeskorte, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23607v1)

**Summary:** Computational complexity theory provides a framework for analysing abstract models of computation, whereas computational systems operate as finite physical implementations whose behaviour is shaped by their architecture and physical substrate. In such systems, computational organisation cannot be directly characterised from algorithms or internal representations. Building on the use of reaction time distributions to constrain mechanisms in cognitive science, we introduce an empirical framework f...

---

### 10. EEG Lempel-Ziv Complexity vis-à-vis Autocorrelation Function

**Authors:** Pedro Montoya, Ignacio Cifre, José Luis Rosselló Sanz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23231v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23231v1)

**Summary:** Measures of signal complexity have become increasingly popular in electroencephalography (EEG), where they are often interpreted as indicators of neural information processing, dynamical richness, or conscious state. In contrast, classical measures of temporal dependence, such as the autocorrelation function (ACF), remain more directly linked to known physiological mechanisms and are easier to interpret. The present work revisits, for the EEG practicioner, the relation between normalized Lempel-...

---

### 11. What Shapes Brain Alignment of Large Language Models during Dialogue? Insights from Language Production and Comprehension

**Authors:** Yuko Nakagi, Yuya Chiba, Yasue Kishino

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22961v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22961v1)

**Summary:** Brain alignment of large language models (LLMs) offers a way to investigate representational similarities between LLMs and the human brain during language processing. While previous studies have mainly focused on passive language comprehension, little is known about such alignment during dialogue, in which speakers engage in both language production and comprehension. In this study, using fMRI data collected during dialogue, we examine brain alignment during language production and comprehension...

---

### 12. Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies

**Authors:** Yiran Huang, Zeyong Zhang, Bharat Biswal, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22706v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22706v1)

**Summary:** Multimodal large language models (MLLMs) offer scalable annotations of social and affective content, but their temporal agreement with human judgments and neural predictive value require further evaluation. We compared diffusion-based and autoregressive MLLMs with continuous human Theory of Mind (ToM) and affective valence ratings across three short cartoon movies. Behavioral analyses assessed temporally aligned Pearson correlations, rating distributions, and the effects of preceding scene descr...

---

### 13. Alignment of visual brain encoding models with individual perceptual similarity judgments

**Authors:** Daniel Chong, Haomiao Chen, Keith W Jamison, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22569v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22569v1)

**Summary:** Encoding models that predict brain activation responses to images have traditionally been trained to maximize accuracy when predicting observed brain data. However, their internal representations may not reflect individual human perception. In this work, we investigate whether we can fine-tune brain encoding models to better align their representations with individuals' similarity judgments. Using similarity judgments of 100 images from 8 participants in the Natural Scenes Dataset (NSD), we adap...

---

### 14. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 15. Mutual Information in High-Dimensional Neural Coding

**Authors:** Zimo Li, Yuchang Tian, Matthew P. Leighton, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22206v1)

**Summary:** Estimating mutual information in large neural populations is limited by the exponential growth of possible neural response patterns. Here we apply a Monte Carlo framework to make this problem tractable by sampling from a conditionally independent population model fit from single-neuron responses. The estimator accurately recovers analytical ground truth, corrects finite-data bias, and scales to empirical recordings containing 100 to 10,000 neurons from visual cortex, hippocampus, and retina. Acr...

---

### 16. Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression

**Authors:** Nitin Sharma, Sicheng Dai, Francesco A. Mallus, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21660v1)

**Summary:** Normative models chart how brain measures vary across the lifespan, expressing each individual as a deviation from a healthy reference. However, most regional models of cortical thickness disregard dependencies between cortical and subcortical anatomy, and transferring them to a new site typically requires retraining or a recalibration of location and scale alone. We condition lifespan norms of cortical thickness on subcortical volume, such that each deviation indicates whether an individual's c...

---

### 17. Neural Computation Runs on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep

**Authors:** Javier Diaz

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21486v1)

**Summary:** Biological function operates far from thermodynamic equilibrium, sustained by metastable structures that continuously cycle through synthesis, function execution, and degradation--consuming energy and exporting entropy in the process. Neural computation exemplifies this dissipative organization, relying on low-entropy structures engaged in dynamic processes that define key information transfer and processing parameters such as gain, threshold, and integration time. This perspective proposes that...

---

### 18. Language Models Share a Readout Bottleneck in Working Memory

**Authors:** Dongyu Gong

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21176v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21176v1)

**Summary:** Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent it...

---

### 19. Statistical Mechanics of Spike Trains: Self-Consistent Activity Ensembles and Phase Transitions

**Authors:** Jan Pyrzowski, Laura Messio, Guillaume Marrelec, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20971v1)

**Summary:** We introduce a statistical-mechanical framework for spiking neuronal systems in which entire spike trains, defined as spatiotemporal configurations of discrete events, are treated as microstates of the system. Instead of modeling explicit network dynamics, we construct an ensemble over complete spike histories and assign to each configuration an effective energy functional that quantifies its consistency with intrinsic synaptic interactions.   This formulation leads to a Boltzmann-like distribut...

---

### 20. Cross-subject decoding of imagined speech from scalp EEG: a leakage-controlled evaluation on three public corpora

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20954v1)

**Summary:** Objective. A decoder of imagined speech that works for a new user without calibration would make a non-invasive speech interface practical. We tested whether imagined-speech content recorded with scalp electroencephalography (EEG) transfers across people, and examined why accuracy within a single person remains low. Approach. We analyzed three public corpora, ds003626, KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, under a protocol that enforces split integri...

---

### 21. How large an effect would we have seen? Positive controls, detection floors and dataset pitfalls in scalp-EEG speech decoding

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20942v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20942v1)

**Summary:** Objective. Studies that decode imagined speech from scalp electroencephalography (EEG) commonly validate their pipelines with a positive control, usually overt speech, and report null results without stating what effect size the pipeline could have detected. Approach. Using ds003626 ("Thinking out loud"), KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, we audited decoding of overt speech, articulator preparation and imagined speech with artifact-channel subset...

---

### 22. Awakening as a Trait-Level Transformation of Consciousness

**Authors:** Riku Ihalainen, Victor Oswald, Gulshan Kumar, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20856v1)

**Summary:** Awakening is reported across contemplative traditions yet remains poorly defined in science, where it is often conflated with transient states induced by meditation or psychedelics, obscuring its significance for theories of consciousness and cognitive architecture. We treat awakening as a functional construct capturing convergence across Hindu and Buddhist sources, phenomenological and psychometric findings, and neuroimaging evidence. Synthesizing these literatures, we find convergent evidence ...

---

### 23. Two dissociable axes of brain hierarchical dynamics track universal and population-specific effects of mindfulness

**Authors:** Victor Oswald, David Zarka, Riku Johannes Ihalainen, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20854v1)

**Summary:** How mental training reshapes the temporal architecture of large-scale brain dynamics and how these mechanisms differ between healthy and clinically vulnerable populations remains poorly understood. Time-averaged neural measures collapse the multi-scale nature of brain activity, obscuring the dynamic processes through which behavioural interventions reorganise hierarchical brain function. Here, applying a sliding-window Temporal Irreversibility Index to source-reconstructed EEG across three compl...

---

### 24. Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech

**Authors:** Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20766v1)

**Summary:** Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained wit...

---

### 25. EEG Correlates of Verbal and Perceptual Reasoning

**Authors:** Gwyneth Rolph

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19979v1)

**Summary:** Identifying the neural underpinnings of intelligence is one of the major goals of modern intelligence research. However, few imaging studies explore the high extremes of intelligence, and most use only a single composite IQ score. This study used quantitative EEG recordings to investigate correlations between the EEG variables of individual alpha peak frequency, relative power, and coherence, and scores on verbal and perceptual reasoning tests in participants with IQs from the low-average to exc...

---

### 26. Reciprocity coordinates a three-way trade-off in recurrent neural circuits

**Authors:** Xiaoyu Zhang, Mingyi Huang, Yixuan Cui, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19949v1)

**Summary:** Biological neural circuits contain both unidirectional and reciprocal connections, but how reciprocity affects circuit computation remains unclear. We varied reciprocity \r{ho} across 21 levels in recurrent-network simulations while holding network size, connection density, and directed-edge count fixed. Low-reciprocity networks produced more diverse stimulus-driven activity and performed better on four continuous-input tasks, whereas higher reciprocity generally improved performance on three de...

---

### 27. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 28. Effects of cortisol time-scales in a model of emotion regulation

**Authors:** Michael Buccino, Joshua Ginart, Eva Kaslik, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19282v1)

**Summary:** Stress reshapes cortico-limbic dynamics across multiple timescales, with important consequences for healthy and pathological arousal responses. We develop and analyze a Wilson-Cowan model of prefrontal-amygdala circuitry, incorporating excitatory and inhibitory populations involved in emotional regulation. The effects of stress cortisol are represented as history-dependent modulations of two stress-sensitive interactions: recurrent prefrontal excitation and inhibition of basolateral amygdala pri...

---

### 29. Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome

**Authors:** Taeho Jo

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19153v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19153v1)

**Summary:** In Alzheimer's disease, the amount of pathology in the brain is an imperfect predictor of how much function is lost. Pathology leads to that loss through neural circuits, but these cannot be observed neuron by neuron in patients. This study therefore simulated the central nervous system of the adult male Drosophila melanogaster: 166,700 integrate-and-fire neurons wired by the MaleCNS connectome. The simulator reproduced a published fly brain model (rate correlation 0.9997). Three kinds of damage...

---

### 30. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 31. Sense-Making phase transition framework for Affect

**Authors:** Miguel Bosch, Laura Fanfarillo, Gustavo Diez, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18115v1)

**Summary:** Contemporary accounts of affect emphasize different perspectives, ranging from the regulation of bodily states in allostatic approaches to the relational and sense-making character stressed by enactive theories. Here, we show that affect can be made explicit within the sense-making phase transition framework previously introduced for the perception of an inner sensation. Within this same formal structure, each stable minimum of the sense-making potential defines an affective state: its position ...

---

### 32. Rewiring of adult neural networks - learning from structural plasticity across multiple scales

**Authors:** Michael Fauth, Han Lu, Jannik Luboeinski, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18024v1)

**Summary:** Synaptic connections are continuously formed and eliminated even in adult neuronal networks. This process - called structural plasticity - allows networks to change their topology to learn and adapt to their environment or compensate for lesions. Yet, in contrast to synaptic plasticity, structural plasticity is less well studied and understood. We here present the current state of knowledge as well as open problems in the field along three guiding questions: (1) What regulates structural plastic...

---

### 33. Rethinking World Models for Biosignals

**Authors:** Xianglong Bao, Bosong Huang, Xiaoda Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17510v1)

**Summary:** World models promise to learn how systems evolve and respond to actions, enabling simulation, planning and decision-making. Bringing this promise to biosignals requires more than accurate prediction of physiological recordings. We examine existing biosignal world models through two requirements for intervention use: a genuine action and evidence of its causal effect. We identify three fundamental bottlenecks rooted in physiology: Temporal Latency, the variable delay between an action and its obs...

---

### 34. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 35. Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models

**Authors:** Hanbo Xie, Yue Zhao, Robert C. Wilson

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17310v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17310v1)

**Summary:** Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptiv...

---

### 36. Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors

**Authors:** Farhad Pashakhanloo, Venkatesh N. Murthy

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17164v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17164v1)

**Summary:** The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 mo...

---

### 37. Simple model of neurogliovascular unit activity with noradrenaline leading force

**Authors:** Andrey Yu. Verisokin, Darya V. Verveyko, Alexey R. Brazhe, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15263v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15263v1)

**Summary:** In this work we present a model of a neuroglivascular unit associated with a neuronal ensemble. We combine calcium dynamics in the astrocyte, the cascade of synthesis of arachidonic acid and its derivatives, as well as the activity of the network of inhibitory and excitatory neurons with changes in local blood flow. We add equations to the model for extracellular neurotransmitters such as GABA, glutamate, and norepinephrine. We show that the resulting model can exhibit different types of behavio...

---

### 38. Predicting Cognitive Tasks from Single-Channel EEG through Task-Semantic Alignment

**Authors:** Ryota Kanai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15104v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15104v1)

**Summary:** Studies of data scaling in electroencephalography (EEG) and related noninvasive recordings suggest that simple wearable devices could eventually reveal more about cognitive states. However, publicly available EEG data are difficult to combine. Different laboratories record different tasks, participants, and devices. Task-agnostic self-supervised learning can exploit such data, but representations learned only with EEG signals have not consistently produced feature representations that are direct...

---

### 39. Bayesian adaptive design for neural recruitment curves

**Authors:** Vishweshwar Tyagi, Saihari S. Dukkipati, Daniel Twili, et al.

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15000v1)

**Summary:** Nonlinear response models remain ubiquitous across disciplines with recruitment curves describing muscle response to neural stimulation. Conventional acquisition methods typically rely on static uniform sampling, requiring many stimuli, while adaptive threshold-hunting designs such as ML-PEST forfeit accurate characterization of the overall curve. We present a Bayesian adaptive design that uses posterior uncertainty over curve parameters to propose stimuli that maximize information gain across t...

---

### 40. Full Lyapunov Spectra of Random Neural Networks, Part I: Finite-Time and Asymptotic Theory

**Authors:** Haoyu Albert Wang, Wei P. Dai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14922v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14922v1)

**Summary:** We develop a dynamical mean-field framework for the full finite-time and stationary asymptotic Lyapunov spectra of random recurrent neural networks. At finite observation time, an exact log-determinant representation of tangent-propagator singular values leads to a closed-contour matrix Dyson equation for the smoothed spectral tail. In the stationary setting, a cocycle representation yields an operator equation for the asymptotic cumulative spectrum. Both formulations retain complete local gain ...

---

### 41. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 42. EEG Entrainment to Non-Speech Rhythmic Patterns Associated with Dimensions of Language Performance

**Authors:** Francisco J. Martínez-Murcia, Nicolás J. Gallego-Molina, Marco A. Formoso, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13419v1)

**Summary:** Developmental dyslexia (DLX) affects 5-12% of the global population and impairs learning to read. Its biological basis, particularly the difficulties observed in oral phonological tasks, remains debated. Entrainment, the coupling of brain oscillations to speech rhythms, is essential for encoding phonological representations. We investigated whether brain entrainment to non-speech rhythms could predict DLX in 48 participants listening to white noise amplitude-modulated at rates matching Spanish s...

---

### 43. Beyond Anxiety and Avoidance: A Dynamic Feedback-Regulation Framework for Adult Romantic Attachment

**Authors:** Mateusz Pomianek

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13312v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13312v1)

**Summary:** Adult attachment is commonly represented by attachment anxiety and avoidance, but these person-level dimensions do not by themselves specify how momentary relational conditions are perceived, compared with desired conditions, translated into action, and updated after interpersonal feedback. We present the Attachment Regulation and Control (ARC) framework as an integrative feedback-regulation account that makes these temporal assumptions explicit and empirically testable. In ARC, control refers t...

---

### 44. Excitability across scales: a unifying EI model

**Authors:** Thomas S. J. Burger, Rodolphe Sepulchre

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13275v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13275v1)

**Summary:** Neuronal excitability is commonly modeled using different principles at the cellular and population scales, making it difficult to study how microscopic mechanisms shape macroscopic activity. We introduce a spatiotemporal excitatory-inhibitory (EI) model that unifies these scales through a common mixed-feedback architecture. The model retains the conductance-based circuit structure of Hodgkin-Huxley models and describes intrinsic and synaptic currents through memductances whose temporal and spat...

---

### 45. FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model

**Authors:** Aashish Dhawan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13018v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13018v1)

**Summary:** Connectome-constrained neural networks make biological components directly accessible to intervention, but their mechanistic conclusions can still depend on the comparison model, intervention, circuit representation and trained solution. We stress-test these dependencies in flyvis, a \emph{Drosophila} motion-vision model, using its 50-model ensemble, task-matched causal CNN controls and replicated interventions. At the level of model behaviour, three-level reverse-phi reversal in flyvis is stron...

---

### 46. Energy, Information, and the Limits of Neuropsychiatric Classification

**Authors:** Farbod Khodadadi, Mina Kheirkhah, Bita Shariatpanahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.14095v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14095v1)

**Summary:** Importance: The search for reliable neuroimaging biomarkers of mental disorders has remained elusive despite decades of research. Why clinically consequential disorders yield weak neuroimaging separability remains unresolved. Drawing on statistical thermodynamics and the metabolic costs of neural coding, we propose that psychiatric disorders produce constrained deformations of a largely shared repertoire of brain activity patterns, limiting the class-specific information available for classifica...

---

### 47. Lyapunov spectrum of random neural networks

**Authors:** David G. Clark

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12426v1)

**Summary:** The Lyapunov spectrum of a nonlinear recurrent neural network with random asymmetric couplings is calculated in the limit $N\to\infty$. The calculation is based on a finite-$N$ identity that expresses the cumulative distribution of Lyapunov exponents as a response function of the tangent-space dynamics, with the tangent trajectory selected by a minimum-norm condition rather than by an initial condition. A cavity method then determines this response function at large $N$ through a self-consistent...

---

### 48. Neural Decoding as Cognitive Inference

**Authors:** Yi Guo, Changhong Jing, Yong Hu, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11923v1)

**Summary:** The brain maintains stable cognition despite continuously changing neural activity. How to extract stable cognitive states from variable neural observations remains a central problem in neural decoding. Existing neural decoding methods map neural observations to predefined external labels based on the stimulus-response principle, often capturing recording-specific spurious correlations. Inspired by how the brain infers the world, and specifically by Bayesian brain theory, we recast neural decodi...

---

### 49. Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy

**Authors:** Marko Tvrdic, Justin Richmond Domingo, Jae Ann Buenaluz, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11222v1)

**Summary:** Preclinical models poorly predict human drug efficacy, particularly in neurological disorders. Neural activity offers a uniquely rich source of translational information because it captures high-dimensional variation in nervous-system function that can be measured in both animals and humans. However, its high dimensionality makes it difficult to distinguish conserved disease-related features from variation arising from species, recording modality and experimental context. Here, we test whether s...

---

### 50. If the brain were so simple: Information-based drivers of intelligence and their interaction through an n-body-inspired framework

**Authors:** Brett J. Kagan, Johnson Zhou, Forough Habibollahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11142v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11142v1)

**Summary:** Theories of how the brain processes information and returns intelligent outputs are numerous and often difficult to conclusively test. Here, we consider an approach grounded in informatics and algorithmic thermodynamics for how neural systems respond to different patterns of information in different ways, with a focus on the relationship between the information entropy of a signal and a new proposed quantity we term information enthalpy, which represents the internal resource of structured infor...

---

## stat.ML

**50 papers**

### 1. Learning to Refer: Inference-Time Collaboration in Decentralized Federated Learning

**Authors:** Yuheng Ma, Chendi Wang, Qiong Zhang

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26800v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26800v1)

**Summary:** In decentralized federated learning, heterogeneous clients may develop complementary expertise, yet each query is typically evaluated only by the client where it arrives. To exploit this distributed expertise without global coordination, we formulate inference-time collaboration as budgeted local expert referral, a graph-constrained routing process in which a query can move only between neighboring clients and only visited clients contribute to its final prediction. EdgeDRM implements this frame...

---

### 2. Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models

**Authors:** Agus Sudjianto, Denis Burakov

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26797v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26797v1)

**Summary:** Candidate-scoring decision models return a probability distribution over a presented set of answers. Public documentation of one such system, Jev, and of an open counterpart, JevAny, describes three training ingredients that determine what these probabilities estimate: soft targets from larger models, a frozen pretrained backbone and temperature calibration. We analyze each ingredient in Gaussian surrogates where the finite-sample risk can be computed exactly. A student trained on teacher target...

---

### 3. High-dimensional covariate-assisted ranking

**Authors:** Yujia Liu, Yuanyuan Lin, Ruijian Han, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26796v1)

**Summary:** Ranking data in modern applications often involves covariate vectors whose dimension grows with the number of objects. Identifying relevant covariates and integrating them with item-specific utilities can yield better predictive performance. In this work, we study a Plackett--Luce model that incorporates both item-specific utilities and high-dimensional covariate effects. Under a sparsity assumption on the covariate coefficients, we establish a necessary and sufficient condition for identifiabil...

---

### 4. Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books

**Authors:** Skander Lejmi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26789v1)

**Summary:** A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose distinct challenges. Three challenges underpin this research: adverse selection may cause a policy trained on real data to stop quoting; the consequences of a quote can arrive many steps after the action; and prediction-marke...

---

### 5. Cross-Fitting for Neural Posterior Estimation

**Authors:** Jeffrey Regier

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26733v1)

**Summary:** Neural Posterior Estimation (NPE) fits an amortized conditional density estimator to a simulated training set of complete-data realizations. NPE's training objective, log-likelihood, favors posterior approximations that assign arbitrarily high density to the training points, and typical families of amortized conditional density estimators (e.g., normalizing flows, Gaussian encoders) are flexible enough to oblige. The resulting policy of extreme overconfidence translates poorly to held-out data. ...

---

### 6. Dirichlet-Tree Allocation Priors for Bayesian Causal Forests

**Authors:** Javier Enrique Aguilar, Daniel Klippert, Yusufhan Balci, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26728v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26728v1)

**Summary:** Bayesian Causal Forests (BCF) estimate heterogeneous treatment effects with a separate ensemble of treatment trees. The prior on the leaf values of the treatment trees determines whether sampling variability is attributed to the treatment effect. Independent shrinkage priors exert no control over how a tree allocates variability across its leaves, and their total prior variance grows as leaves are added. We propose the Dirichlet-Tree Bayesian Causal Forest, which jointly regularizes the leaf val...

---

### 7. Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows

**Authors:** Qian Xie, Wenyue Hua, Yueli He, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26676v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26676v1)

**Summary:** LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple candidates. We introduce Cost-Coupled Gittins (CC-Gittins), a multi-objective extension of single-objective cost-aware Gittins search for Pareto recommendation. It exploits the coupling between evaluation and deployment co...

---

### 8. WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting

**Authors:** Arjun Ashok, Mihir Parmar, Palash Goyal, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26582v1)

**Summary:** Recent time series foundation models (TSFMs) can consume covariates in-context, extending zero-shot forecasting to problems driven by external factors. This enables scenario analysis: forecasting how a target responds to events that set covariates to chosen future values. Whether they can do this reliably is an open question. We introduce WhatIf-Bench, a benchmark measuring how well forecasters use covariates to forecast a target's response to future events. WhatIf-Bench is semi-synthetic: time ...

---

### 9. R2-GP: Variance-Calibrated Priors for Additive Gaussian Processes

**Authors:** Javier Enrique Aguilar, Soham Mukherjee, David Kohns

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26437v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26437v1)

**Summary:** We develop R2-GP, an R2D2-type prior for Gaussian process (GP) generalised additive models (GAMs) that calibrates explained variance ($R^2$) for Matérn covariance kernels. The function variance for standard Matérn kernels depends jointly on the effect magnitude and length-scale. As such, smooth and rough components with identical amplitudes contribute very different amounts of variation. With independent priors on component amplitudes, this variation results in variance overestimation, especiall...

---

### 10. Local data augmentation for imbalanced binary classification

**Authors:** Harold Gu{é}neau, Alain Celisse, Pascal Delange

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26418v1)

**Summary:** Facing imbalanced binary classification, we aim at maximizing the recall while limiting the proportion of false detections in the minority class. For doing that, the present work studies the effect of several rebalancing strategies, from the uniform subsampling of the observations from the minority class, to a more involved local data augmentation scheme. To be more specific, we establish that only rebalancing class proportions cannot modify the classification performance, whereas local data aug...

---

### 11. A Simple and General Approach to top-$k$ Selection

**Authors:** Motti Goldberger, Nils Rudi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26407v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26407v1)

**Summary:** This paper considers the Bayesian top-$k$ identification problem, wherein a decision maker is tasked with selecting $k$ items from a pool of items of unknown quality. To assess the items, the decision maker adaptively allocates a fixed sampling budget, where each sample of an item yields a noisy observation of its quality, with the objective of minimizing the expected opportunity cost of the selected set. We propose an approach that allocates each batch of samples by minimizing a surrogate objec...

---

### 12. Selecting the Best Few with Human Evaluators: Adaptively Combining Ratings and Pairwise Comparisons

**Authors:** Motti Goldberger, Nils Rudi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26380v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26380v1)

**Summary:** This paper considers a decision-maker tasked with identifying the $k$ best items from a large pool of candidates, such as job applicants, LLMs, award nominees, or new product ideas. The decision-maker learns about the items' quality by soliciting human evaluations. Each evaluation can be costly, so the decision-maker aims to use the limited evaluation budget efficiently by allocating evaluations adaptively. A key consideration is the form of evaluation to solicit, which should be something evalu...

---

### 13. Causal Robustness from Synthetic Environments

**Authors:** Linying Yang, Cyrill Scheidegger, Xinwei Shen, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26250v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26250v1)

**Summary:** We study robust prediction when the training data come from a single observational distribution. Causality-oriented methods for robust prediction usually use heterogeneity across observed environments both to learn an invariant prediction function and to determine the perturbations against which it is robust. We show that both can be recovered from one distribution under a structural additive-noise mechanism for the response. Under the structural model considered here, the causal prediction func...

---

### 14. A general condition for fast rates in multi-group learning

**Authors:** Hanqi Sun, Evgenii Chzhen, Luca Ganassali, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26198v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26198v1)

**Summary:** In multi-group learning, a single predictor must control its excess risk simultaneously over overlapping groups. Tosh and Hsu (2022) obtained $1/\sqrt{n}$ slow rates via a reduction to online learning with sleeping experts, and $1/n$ rates only under realizability (and for a different strategy). We identify a group-wise Bernstein condition under which the same adaptive predictor attains the fast rate $1/n$ without knowing whether the condition holds, while retaining the slow rates on the groups ...

---

### 15. Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation

**Authors:** Xuyuan Xiong, Siyu Chen, Zihan Shao, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26030v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26030v1)

**Summary:** Looped transformers reuse a shared block of layers to increase computational depth without increasing the number of trainable parameters. They are trained with backpropagation through time (BPTT). To save training compute, BPTT is often truncated to the last few loops, although this may weaken the benefit of looping. To study this tradeoff systematically, we jointly vary model size, training tokens, and forward and backward loop counts across nearly 600 training runs and fit a unified scaling la...

---

### 16. Towards instance-dependent regret optimality in Episodic MDPs with Posterior Sampling

**Authors:** Victor Boone, Cyrille Kone, Waris Radji, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26029v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26029v1)

**Summary:** We study regret minimization in finite-horizon episodic Markov Decision Processes (MDPs). While minimax-optimal algorithms are known, tractable approaches to instance-dependent optimality are still lacking. Motivated by this gap, we introduce $π_0$-PSRL, a variant of PSRL that uses posterior samples to decide when exploration is needed, while following a fixed reference policy $π_0$ during exploration episodes. This decouples the test for exploration, triggered when the sampled and empirical MDP...

---

### 17. Mediation and moderation in distance-based regression with triangular fuzzy data: simulation evidence and an application to academic performance

**Authors:** Fabrizio Maturo, Annamaria Porreca

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26011v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26011v1)

**Summary:** We study mediation and moderation in the distance-based regression model for triangular fuzzy responses, in which the center and transformed spreads of the response are linear in the components of fuzzy and crisp covariates. With a common design, componentwise least squares minimizes the unconstrained quadratic extension of the Yang--Ko distance on the transformed scale, for any choice of its shape parameters. Direct, indirect and total effects are defined separately for the center and the sprea...

---

### 18. Federated Community Detection in Bipartite Networks

**Authors:** Wanjie Wang

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25997v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25997v1)

**Summary:** We study federated spectral estimation when a large matrix is horizontally partitioned across servers that cannot share raw data. We propose FLICKER, a target-specific gradient-based power iteration that recovers a singular direction associated with a prescribed spectral target using only matrix-vector products on local blocks. Different target directions can be recovered independently and in parallel. We establish non-asymptotic convergence guarantees and provide a recursive grid-search procedu...

---

### 19. Keep the Lineages Alive: Diversity-Preserving SMC for Diffusion LLM Decoding

**Authors:** Minoo Ahmadi, Seyedarmin Azizi, Mehdi Kamal, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25932v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25932v1)

**Summary:** Inference-time sequential Monte Carlo (SMC) decoding can improve the reasoning accuracy of masked diffusion language models (diffusion LLMs) without post-training by resampling a population of partial generations according to a reward. Its effectiveness therefore depends on the resampling step, which must concentrate computation on promising candidates while retaining enough diversity to explore alternative reasoning paths. The reward can be internal, the decoder's own confidence on the committe...

---

### 20. Statistical Learning Theory for Direct Preference Optimization

**Authors:** Joel Wills, Yuanfan Li, Yiming Ying, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25856v1)

**Summary:** Direct Preference Optimization (DPO) learns from pairwise preferences through a logistic objective whose score-difference parameterization follows the Bradley--Terry model. We study how failure of this modeling assumption limits DPO, distinguishing structural misspecification from limited model capacity and finite-sample estimation. Our main contribution is a characterization of structural approximation error through the triangle-curl of the preference log-odds, which vanishes exactly when prefe...

---

### 21. Fair Regression under Approximate Demographic Parity

**Authors:** Weiwei Wang, Xianyang Zhang, Raymond K. W. Wong

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25796v1)

**Summary:** Exact demographic parity requires the same prediction distribution across sensitive groups. In regression, this can be too restrictive and reduce predictive accuracy. We instead bound every pairwise Wasserstein distance between group-specific prediction distributions by a chosen tolerance, allowing the groups to differ while keeping fairness tunable.   On the real line, the prediction and constrained transport problems have the same infimum. If the transport problem attains this value and suitab...

---

### 22. Detection Augmented Learning In Non-Stationary Bandit Environments

**Authors:** Argyrios Gerogiannis, Yu-Han Huang, Subhonmesh Bose, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25782v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25782v1)

**Summary:** We study the problem of non-stationary bandits without knowledge of the environmental changes. We propose Detection Augmented Learning (DAL) a black-box paradigm that comprises three modular components: a bandit algorithm, a change detector, and a forced exploration schedule. This modular design enables its applicability across a broad spectrum of bandit problems, from classical to highly structured settings. First, we provide theoretical insights into DAL's strong empirical performance: a singl...

---

### 23. Corrected Block Sparse Spectral Optimization: Exact Models, Finite Identification, and Local Dynamics

**Authors:** Omid Shams Solari

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25721v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25721v1)

**Summary:** The block generalized-power method pairs threshold-based support selection with inexpensive Stiefel updates, but the standard block formulation conflates two nonequivalent objectives and leaves inactive components, threshold ties, and post-selection refitting ill-specified. We rebuild the model from the primal. Eliminating each loading column from the normalized loading-ball problem gives a sum of soft-thresholded Euclidean norms (A-SUM); the squared-threshold objective in common use arises from...

---

### 24. Divergence based Ranked Preference Alignment for LLMs

**Authors:** Rajdeep Haldar, Yue Xing, Qifan Song

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25588v1)

**Summary:** Alignment of large language models typically relies on pairwise preference feedback, though ranked feedback can capture more comprehensive information across multiple responses within a single annotation. However, ranked-preference alignment is underexplored in practice compared to simpler pairwise approaches, potentially resulting in suboptimal behavior. Concurrently, recent research has conceptualized large language model alignment objectives as divergence estimators between aligned (preferred...

---

### 25. Reinforcement learning on the EPRI AI-ccelerating Unit Commitment benchmark: diagnosing over-commitment and guiding MILP with learned policies

**Authors:** Maharani Devira Pramita, Aidan O'Sullivan

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25544v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25544v1)

**Summary:** Reinforcement learning (RL) is increasingly proposed as a fast solver for unit commitment (UC), but standalone agents remain far more expensive than mixed-integer linear programming (MILP). In the first study of RL on the 51-generator, 72-hour benchmark of the Electric Power Research Institute (EPRI) AI-ccelerating Unit Commitment competition, we trace this gap to the agents' own exploration, close most of it, and show that the resulting policy can accelerate an exact solver. In every configurat...

---

### 26. DR-Learners for Generalizing CATEs from a Randomized Controlled Trial

**Authors:** Vanessa Rodriguez, Brieuc Lehmann, Karla Diaz-Ordaz

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25405v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25405v1)

**Summary:** Randomized clinical trials are essential for evaluating interventions, yet average treatment effects can obscure treatment effect heterogeneity, making conditional average treatment effects (CATEs) a natural target. However, restrictive eligibility criteria and differential trial participation can limit the generalizability of these effects to broader target populations. Building on existing DR-Learners, we develop the gDR-Learner for generalizing RCT CATEs to a target population, using cross-fi...

---

### 27. A Distribution-Free Separation Between Learned and Fixed Features

**Authors:** Daniel Barzilai

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25335v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25335v1)

**Summary:** The success of neural networks is largely attributed to their ability to learn useful representations from training data. However, known results that prove a computational advantage of learned features over fixed ones are restricted to specific input distributions. We settle the COLT open question of Feldman, Kamath, and Srebro (2026) by showing that this advantage can persist in the distribution-free setting.   We construct a family of hypothesis classes that can be efficiently learned by a nat...

---

### 28. Decision-Target Reversal under Informative Label Missingness

**Authors:** Farinborz Setoudehtazangi, Geoffrey J. McLachlan

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25128v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25128v1)

**Summary:** Informative label missingness can improve classification efficiency because the pattern of label availability may itself contain information about the discriminant structure. We show that this advantage need not persist across deployment objectives: with the data-generating model and statistical experiments held fixed, informative partial classification can be favourable under one loss and unfavourable under another. We call this phenomenon decision-target reversal. For binary Gaussian discrimin...

---

### 29. Dimension-free comparison inequalities between $f$-divergences for Gaussian location mixtures

**Authors:** Jeonghwan Lee, Cong Ma

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25070v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25070v1)

**Summary:** We establish dimension-free comparison inequalities between the Kullback-Leibler (KL) and $χ^2$-divergences and the squared Hellinger distance for Gaussian location mixtures with compactly supported mixing distributions. We show that both divergences are bounded by the squared Hellinger distance up to constants depending only on the radius of the support, independently of the ambient dimension and the number of mixture components. These results resolve an open question raised by \cite{jia2023ent...

---

### 30. Robust Direct Preference Optimization under Preference Label-Flip Attacks

**Authors:** Chenye Yang, Weiyu Xu, Lifeng Lai

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.24945v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24945v1)

**Summary:** Direct Preference Optimization (DPO) is widely used for offline Reinforcement Learning from Human Feedback. However, recent works have shown that DPO can be easily manipulated by adversarial preference label flip attacks, which are specifically designed to mislead the learner toward an attacker-chosen target policy. To address this issue, we design robust DPO methods that can defend against such attacks. Building on the property that lable flips induce parameter-independent gradient shifts in lo...

---

### 31. Scalable and Adaptive Distribution Regression via Random Features

**Authors:** Yinsong Wang, Xiao Liu, Yu Ding

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24892v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24892v1)

**Summary:** Distribution regression seeks to learn mappings from probability distributions to response variables and has emerged as a unifying framework for kernel methods, multi-instance learning, and set-valued learning. Despite its success, kernel-based distribution regression remains computationally expensive and sensitive to kernel choice, motivating scalable and adaptive representations. Building on random feature approximations, we develop a finite-sample analysis of Random Feature Distribution Regre...

---

### 32. A Statistical Viewpoint on Adam, Shampoo and Muon

**Authors:** Tetiana Parshakova, Robert M. Gower, Paulo Orenstein

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24839v1)

**Summary:** We provide new statistical insights into designing stochastic optimization methods. By modeling the gradient via a normal distribution, we argue that the stochastic gradient should be whitened using its covariance. We give an online method for estimating the mean and variance of the gradients based on regularized likelihood or, equivalently, through a maximum a posteriori estimate. We then show how to use structured approximations to the covariance within this same framework, which includes diag...

---

### 33. Tilted Mondrian: Triage and Mitigation of Fine-grained Disparities in Conformal Prediction

**Authors:** Ziang Gao, Pengqi Liu, Archer Yi Yang, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24813v1)

**Summary:** Fairness in conformal prediction is often pursued through Mondrian calibration, which provides finite-sample coverage guarantees separately across groups. These guarantees, however, are coarse: substantial disparities can remain within finer strata. This coarse-to-fine fairness issue raises two questions: how severe can such disparities be, and how can they be mitigated? Aggregate disparities can depend on how groups are distributed across strata. For severity assessment, we introduce propensity...

---

### 34. Martingale Posterior Cox Processes

**Authors:** Joshua Rooijakkers, Edwin Fong

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24787v1)

**Summary:** Cox processes provide a principled Bayesian nonparametric framework for modeling event-based data through an underlying intensity function. However, existing inference methods for estimating the intensity typically rely on computationally expensive Markov chain Monte Carlo sampling or approximate inference techniques. In addition, to ensure tractability, these methods often define priors over indirect latent structures, making them challenging to interpret. In this paper, we introduce the Martin...

---

### 35. Gaussian Process Bandits with Paired Auxiliary Observations

**Authors:** Weibo Huang, Qing Feng, Ruihao Zhu, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24737v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24737v1)

**Summary:** Bayesian optimization (BO) is widely used for expensive black-box optimization, yet observation noise makes each evaluation less informative and slows posterior learning. Standard BO learns from costly outcomes gathered during optimization. In many applications, however, low-cost auxiliary data are available beforehand. We introduce Auxiliary-Informed Gaussian Process Bandit (AI-GPB), a variance-reduction method that combines an offline estimate of the auxiliary mean with a correction coefficien...

---

### 36. Conditional Weight of Evidence for Gradient-Boosted Credit Models: Estimation, Additivity and Its Relation to Adverse Action Reasons

**Authors:** Agus Sudjianto, Denis Burakov

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24586v1)

**Summary:** Traditional weight of evidence assigns a credit characteristic a value based on its association with default across a population. Credit analysis also requires an assessment of that characteristic in the context of an individual applicant's record. We study conditional weight of evidence for this purpose. It measures the change in default log odds from observing a characteristic after the remaining credit information is known. Its sign identifies whether the characteristic adds adverse or favora...

---

### 37. Accelerating Finite-Sum Bilevel Optimization with Fully First-Order Oracles

**Authors:** Qihao Zhou, Shanshui Niu

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24538v1)

**Summary:** We study nonconvex--strongly-convex bilevel optimization with finite-sum objectives and fully first-order oracles. We propose Sampled Implicit Corrections for Bilevel Optimization (SICBO), which combines a penalty approximation with variance-reduced corrections for the lower-level variables. Under componentwise lower strong convexity, SICBO finds a point $x$ satisfying $\mathbb{E}\|\nablaΦ(x)\|^2\le\varepsilon^2$ within $\tilde{O}(N+\sqrt{N}κ^{7/2}\varepsilon^{-2})$ component-gradient calls, whe...

---

### 38. Denoising Implicit Variational Inference

**Authors:** Zitong Wang, Zekun Wu, Longlin Yu, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24509v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24509v1)

**Summary:** Semi-implicit variational inference (SIVI) expands the representational capacity of variational families, but optimizing the Evidence Lower Bound (ELBO) remains challenging because the marginal score of the semi-implicit distribution is generally intractable. Unbiased Implicit Variational Inference (UIVI) and related methods address this difficulty through reparameterized ELBO gradients, but existing approaches estimate the required score indirectly through reverse-conditional sampling or approx...

---

### 39. Private Evaluation of High-Dimensional Functions

**Authors:** Mohammad Afzali, Hassan Ashtiani, Adam Smith

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24477v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24477v1)

**Summary:** We study differentially private black-box evaluation of arbitrary high-dimensional functions. Given a dataset $S$ and query access to a function $f$---whose sensitivity may be unknown or unbounded---the goal is to privately output an approximation to $f(S)$. The black-box evaluator can only query the value of $f$ over a down neighborhood of $S$ (i.e., those subsets of $S$ that are obtained by removing a bounded number of elements from $S$). We design generic black-box evaluators for both pure an...

---

### 40. The Certification Exponent: Instance-Optimal Sequential Certification of Policy Improvement from History Dependent Logs

**Authors:** Rui Wang

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24345v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24345v1)

**Summary:** Before a new policy replaces a deployed one, we often want a certificate, computed from logged episodes, that it is better. We ask how many episodes such a certificate needs when the logging policy is known but history-dependent, and the error probability must stay below $δ$ in every environment consistent with the logs. The answer is an exponent $K^\star$: the smallest KL divergence from the logged law to a law with the same logged action probabilities under which the target does not improve. N...

---

### 41. Uniform convergence at optimal rate and scale

**Authors:** Noga Alon, Steve Hanneke, Shay Moran, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24336v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24336v1)

**Summary:** Uniform convergence asks how many random samples suffice for empirical averages to approximate expectations simultaneously over an entire class of functions. It is a central concept in probability and a foundation of statistical learning. For binary-valued classes, the Vapnik--Chervonenkis theorem characterizes uniform convergence by finiteness of the VC dimension. For dimension $d$, the sharp worst-case sample complexity for additive error $\varepsilon$ is of order $d/\varepsilon^2$. For real-v...

---

### 42. Morpheus-2.0: Multiscale Probabilistic Forecasting with Dual-Axis Attention

**Authors:**  Aakriti, Manoj Cherukumalli, Prathamesh Patil, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24321v1)

**Summary:** A universal forecaster is trained once and applied everywhere, so it must serve tasks whose schemas, forecast horizons, and temporal resolutions all differ. The number of targets and covariates changes from dataset to dataset, horizons vary by orders of magnitude, and sampling rates range from seconds to years. Existing time-series foundation models address these only in part, since they isolate each series or visit the two grid relations in separate blocks, and they fix the horizon and resoluti...

---

### 43. Constructive Universal Approximation by Infinite-Dimensional Neural Networks via Gaussian-Weighted Ridgelet Transform

**Authors:** Sho Sonoda, Luca Galimberti, Yuanchao Xu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24293v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24293v1)

**Summary:** Neural networks whose inputs are functions, as in operator learning, are usually shown to be universal by existence arguments, either by reduction to finite-dimensional networks or by Stone--Weierstrass-type density; these prove that approximants exist but say little about how the parameters depend on the target. We take a constructive route. We extend the ridgelet transform, an integral transform related to the Fourier, Radon, and wavelet transforms, to continuous maps on a separable infinite-d...

---

### 44. CoCoNet: Convex Conformal Network for Multi-Dimensional Uncertainty Regions

**Authors:** Alireza Moradi, Thomas Bruys, Pascal Van Hentenryck, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24246v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24246v1)

**Summary:** Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability, but the efficiency of its prediction regions depends critically on the choice of the conformity score. This is particularly important in multivariate regression, where dependencies across output dimensions induce complex joint uncertainty structures. This paper introduces CoCoNet (Convex Conformal Network) for learning convex conformity scores that induce flexible, data-adaptive prediction regions. Co...

---

### 45. Censored Flow Matching for Synthetic Time-to-Event Generation

**Authors:** Jianbin Tan, Xingran Chen, Kevin He, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24233v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24233v1)

**Summary:** Generating time-to-event data is increasingly important in survival analysis, but it remains statistically challenging because event times are often censored and thus prevent flexible generative modeling. To fill this gap, we propose a novel method called censored flow matching (CFM), aiming at providing a flexible flow-based generative mechanism for synthesizing time-to-event data as well as learning their corresponding probabilistic densities. Unlike existing methods, CFM does not rely on surv...

---

### 46. Certifiably Correct Fréchet Means in Orbit Spaaces

**Authors:** Dustin G. Mixon, Tom Needham, Nathan Willey

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24191v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24191v1)

**Summary:** We study Fréchet means in orbit spaces of finite orthogonal group actions. Since computing these means is NP-hard in general, we take inspiration from group synchronization to develop tractable spectral and semidefinite relaxations. Pairwise alignment certifies global optimality and we develop a semidefinite certificate that can extend beyond this condition. For Gaussian data modulo sign, we prove that our certificate succeeds in a high-noise regime where alignment fails. Numerical experiments e...

---

### 47. On Reparameterizing the Score Function

**Authors:** Mohammad Hossein Amani, Leonardo Bocchieri, Maxime Peyrard, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24188v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24188v1)

**Summary:** Policy gradients for autoregressive sequence models differentiate each token's log-probability while holding the conditioning history fixed. This discards information about how earlier decisions shape later conditional distributions, creating a credit-assignment bottleneck when rewards are sparse. We introduce History-Reparameterized (HR) policy gradients, which replace the frozen prefix in the score function with a differentiable reparameterized or relaxed history, allowing gradients of downstr...

---

### 48. Margin Certificates for Voting Classifiers under Mixing Dependence

**Authors:** Adria Binte Habib, Ibne Farabi Shihab

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24166v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24166v1)

**Summary:** Margin bounds explain why weighted votes generalize after training error vanishes, but dependent observations require concentration arguments that keep the dependence model and failure budget explicit. We study stationary mixing streams without treating dependence as a formal substitution of an "effective sample size." For a finite base class, we combine independent-block Rademacher theory for stationary $β$-mixing processes with a clipped margin loss to obtain an explicit uniform voting-margin ...

---

### 49. Graph-Regularized Synthetic Control for Stable Counterfactual Estimation under Donor Redundancy

**Authors:** Yanlin Zhang, Sungyong Chung, Alireza Talebpour

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24113v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24113v1)

**Summary:** Synthetic control methods estimate counterfactual outcomes by weighting untreated donor units to match a treated unit before treatment. In recent applications, however, the donor pool can be large, highly correlated, and short in pre-treatment history, yielding many near-equivalent solutions with unstable and difficult-to-interpret donor weights. We propose Graph-Regularized Synthetic Control (Graph-SC), a convex estimator that augments the classical pre-treatment matching objective with a graph...

---

### 50. ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference

**Authors:** Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23825v1)

**Summary:** The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. $χ^2$. While versatile, the evidence is notoriously difficult to compute, even when the likelihood is available. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate s...

---

