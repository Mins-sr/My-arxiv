# arXiv Daily Digest - 2026-09-30

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Skill-Space Shooting for Autonomous Robot Policy Improvement

**Authors:** Zihang Rui, Renhao Wang, Haoxu Huang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38178v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38178v1)

**Summary:** Robots deployed in the physical world must be able to improve beyond their initial training as they encounter new situations and failures. For this improvement to scale across tasks, it must make effective use of experience without requiring human demonstration of each correction. Recent agentic systems offer a way to reduce this reliance on human effort by using foundation models to autonomously compose learned behaviors to complete tasks. Yet completing tasks this way does not itself teach a t...

---

### 2. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

**Authors:** Bingchen Yao, Haobo Xu, Haokun Lin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38169v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38169v1)

**Summary:** Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding st...

---

### 3. LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization

**Authors:** Yi Pan, Haocheng Xi, Kan Zhu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38166v1)

**Summary:** Recent LLMs increasingly adopt hybrid designs that replace standard attention with linear attention, such as Gated DeltaNet (GDN) and Kimi Delta Attention (KDA). Although they compress the context into a fixed-size recurrent state and substantially reduce the cost of long-context processing, repeatedly reading and updating that state remains a major inference bottleneck. Quantization offers a natural way to reduce this cost, but can significantly degrade model quality, due to the accumulation of...

---

### 4. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies

**Authors:** Hui Ren, Lei Fan, Henry Pao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38155v1)

**Summary:** Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Enti...

---

### 5. Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning

**Authors:** Paras Dahal, Anton Bakhtin, Taco Cohen, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38147v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38147v1)

**Summary:** As agents take on longer and more complex problems, controlling the execution becomes a task in its own right. Each step in the run brings new control choices, like which partial work to build on, whether to start fresh, or when to stop. We introduce agentic meta-reasoning, an inference-time harness that makes these choices an explicit and structured reasoning process. Workers carry out the task-level computation, while a controller consolidates what the run has established, explores next option...

---

### 6. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

**Authors:** Cheng Qian, Kunlun Zhu, Beibin Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38143v1)

**Summary:** Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the f...

---

### 7. AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation

**Authors:** Rishabh Agrawal, Hejie Cui, Shasha Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38142v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38142v1)

**Summary:** A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice ...

---

### 8. Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE

**Authors:** Yu Xu, Yuxin Zhang, Xiao Yang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38140v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38140v1)

**Summary:** Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models. However, conventional token-wise MoE routes tokens independently within a homogeneous expert pool and regularizes expert usage toward uniformity, making it poorly matched to video data that is spatiotemporally redundant and semantically long-tailed. We show that existing visual MoEs fall into a uniformity trap: semantically under-organized routing, compounded by uniform e...

---

### 9. Stochastic World Models for Verifying Vision-Based Neural Feedback Systems

**Authors:** I. Samuel Akinwande, Mykel J. Kochenderfer, Clark Barrett

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38120v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38120v1)

**Summary:** Verifying a vision-based neural feedback system requires a model of the observations its controller acts upon. Such a model must capture the variation the sensor produces, while remaining tractable for closed-loop analysis. Generative adversarial networks (GANs) have served as perception surrogates, but they are large, reproduce complex scenes poorly, and are hard to verify. We explore stochastic world models as a richer class of perception surrogates. We train a world model with physically grou...

---

### 10. How Local Mixing Encodes Relative Position in Global NoPE Attention

**Authors:** Cutter Dawes, Nick Alonso, Tom Figliolia, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38109v1)

**Summary:** The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in...

---

### 11. Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution

**Authors:** Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38108v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38108v1)

**Summary:** Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: selecting an appropriate plan for the task and executing it faithfully. Existing planner--executor systems can fail at either stage, while final task success alone cannot distinguish selection from execution failures. We therefore study the Plan Declaration--Execution Gap and introduce Planning-as-Rou...

---

### 12. Correct Answers, Invalid Traces: What Verifiable Grade-School Math Reveals About Chain-of-Thought Traces

**Authors:** Ratish Puduppully, Pranabendu Misra, Paarth Iyer, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38107v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38107v1)

**Summary:** Chain-of-thought traces are widely read as records of how models reach their answers, informing debugging, agent auditing, and claims about reasoning. Testing this interpretation is difficult because natural-language thinking traces are rarely mechanically verifiable. We revisit it in iGSM, a synthetic grade-school mathematics benchmark designed to study thinking traces and used to support claims of learned reasoning and planning. Crucially, iGSM exposes the exact quantities and dependencies tha...

---

### 13. NeuronEye: Query-Guided Visual Concept Activation for Vision-Language Reasoning

**Authors:** Ruiyu Yan, Bowen Chen, Shaowen Wan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38098v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38098v1)

**Summary:** Current vision-language models (VLMs) encode visual information in dense hidden states where object identity, spatial layout, and local attributes are implicitly entangled rather than explicitly disentangled, limiting their ability to isolate and modulate the specific visual evidence required by a given language query. Inspired by sparse population coding and top-down modulation in biological vision, we introduce NeuronEye, a plug-in framework that constructs a sparse, concept-level neuron vocab...

---

### 14. Character Training for Risk-Averse Agents

**Authors:** Arav Dhoot, Punya Syon Pandey, Jamie Johnson, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38093v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38093v1)

**Summary:** Risk aversion in resources could prevent misaligned AI agents from causing catastrophic harm. Misaligned but risk-averse agents would tend to favor safer strategies like making deals with humans over riskier strategies like rebelling. We train agents to be risk averse through character training, finding that persona traits provide a robust mechanism for instilling risk preferences. To do this, we construct a model constitution describing constant absolute risk aversion (CARA) over an agent's res...

---

### 15. Neural topology optimization of ship structures under propulsion machinery vibrations

**Authors:** Shengyu Yan, Muhammad Muztahidul Hakim Zareer, Jasmin Jelovica

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38089v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38089v1)

**Summary:** Ship structural vibrations contribute to noise, fatigue, and equipment damage, while dynamic-compliance topology optimization can produce pathological designs near resonance. This study extends neural-reparameterized topology optimization using a convolutional Kolmogorov-Arnold network (KATO) to forced-vibration design with active input power (AIP) as the objective. Applications include a 100 Hz engine-supporting deck panel and an 18 Hz thruster foundation frame. Helmholtz PDE filtering and Heav...

---

### 16. Probability is Not Enough: Exploring and Counting Divergent Tokens for Reasoning Uncertainty Quantification in LLMs

**Authors:** Feiyang Li, Shengjing Liu, Qi Zhan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38070v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38070v1)

**Summary:** As the chain-of-thought reasoning capabilities of large language models improve, evaluating and calibrating their reasoning confidence is becoming increasingly important for quantifying the uncertainty of their answers. Current methods for estimating the confidence of large language models are generally based on probabilities of selected key tokens, but the underlying mechanism remains unclear. Our pilot study finds that replacing selected token probabilities with coarse substitutes can also imp...

---

### 17. Jaxolotl: A Unified High-Performance Benchmark Suite for LTL-Based Multi-Task RL

**Authors:** Mathias Jackermeier, Jacques Cloete, Alessandro Abate

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38065v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38065v1)

**Summary:** Training agents to follow arbitrary instructions is an important goal of multi-task reinforcement learning (RL). Linear temporal logic (LTL) provides a precise and structured formalism for specifying instructions to agents, and has been successfully adopted for training generalist multi-task policies. However, differences in implementations, task distributions, and evaluation protocols make existing methods difficult to compare, while high computational costs limit the scale and statistical reli...

---

### 18. UserProxyBench: Evaluating LLM User Simulators for Agent Benchmarks and Training

**Authors:** Ashish Jain, Armaan Sandhu

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38043v1)

**Summary:** Interactive agent benchmarks and multi-turn reinforcement learning increasingly place a second language model in the role of the user. This simulated user controls what information the agent receives and when, yet current benchmarks score only the agent and do not directly measure whether the user correctly executed its assigned role. We introduce UserProxyBench, an evaluation layer over the tau-bench family, and the User Fidelity Score (UFS), which measures adherence to the benchmark's private ...

---

### 19. Gender bias across LLMs is common and highly heterogenous

**Authors:** Edoardo Bolzoni, Valerio Capraro

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38036v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38036v1)

**Summary:** Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and mor...

---

### 20. doPlan: A Variable-Horizon Dataset for Multi-Stage Language-Conditioned Planning in Autonomous Driving

**Authors:** Parthib Roy, Yash Tandon, Marcus Blennemann, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38028v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38028v1)

**Summary:** Autonomous vehicles interacting with passengers through natural language must reason beyond immediate commands. Passenger intent may span multiple stages of behavior, depend on future events, refer to surrounding agents or landmarks, and remain relevant as driving conditions evolve. Existing language-enabled driving datasets largely focus on short, localized interactions, leaving these longer-horizon forms of passenger intent comparatively underexplored. We introduce doPlan, to our knowledge the...

---

### 21. Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large Language Models

**Authors:** Zhenyu Wang, Tianze Wang, Linjun Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38025v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38025v1)

**Summary:** On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher. Vanilla OPD treats all teacher signals equally, assuming that the teacher's supervision is equally important for every token. However, teacher signals at different tokens may have very different effects on the student's performance: some correct important reasoning errors, while others have little effect on the final answer. Motivated by this observation, we ...

---

### 22. Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation

**Authors:** Jaewon Chu, Ji Soo Lee, Jihwan Park, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38024v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38024v1)

**Summary:** An agent skill is a reusable, actionable natural-language artifact that guides an agent to perform a task effectively under a given harness. Recent studies have explored the optimization of agent skills, contributing to a growing collection of publicly available skills spanning diverse tasks, domains, and harnesses. Despite millions of publicly shared skills, existing skill optimization methods largely overlook this accumulated knowledge, instead relying solely on expensive agent rollouts to ite...

---

### 23. PE-EK-PINN: Physics Embedding with Evolving Kernel for Scalable Physics-Informed Neural Networks

**Authors:** Huiwen Zhang, Feng Ye, Chu Ma

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38023v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38023v1)

**Summary:** Physics-Informed Neural Networks (PINNs) embed governing equations into deep learning, but enforce them only through loss residuals, leaving highly oscillatory wave behavior to be discovered by optimization. As a result, methods that achieve relative $L_2$ errors below $10^{-3}$ on standard manufactured Helmholtz benchmarks can fail on practical radiation problems involving singular excitations, absorbing boundaries, and wave fields spanning tens of wavelengths. Architectural physics embedding a...

---

### 24. Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S

**Authors:** Christopher J. Chanhnourack

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38021v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38021v1)

**Summary:** We evaluate an auditable long-term memory system on LongMemEval-S. Its retrieval chain uses hybrid candidate retrieval, cross-encoder reranking, coverage-first packet compilation, and deterministic reasoning scaffolds; an LLM is used only as a replaceable final reader. The chain places all gold sessions in the candidate pool for 468/470 answerable questions and produces gold-complete packets for 462/470. With a Claude Opus reader called through an unpinned CLI alias, two 500-question passes scor...

---

### 25. Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38016v1)

**Summary:** Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is...

---

### 26. From Unity Simulation to Diffusion-Based Augmentation: Quantifying Dataset Balance for Robust Object Detection

**Authors:** Mohamed Benkedadra, Aissa Saoudi, Maxime Gloesener, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38010v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38010v1)

**Summary:** Modern computer vision models achieve high accuracy when trained on large-scale annotated datasets. In critical domains such as construction safety monitoring, data collection is costly, hazardous, and ethically constrained. This paper presents a systematic study comparing two complementary data generation paradigms, (1) Unity Simulation-based rendering and (2) Controllable Diffusion-based generation (CIA), for object detection under real data-scarce conditions. A unified experimental framework ...

---

### 27. HARISSA: Inference-Time Self-Checks for Efficient and Safe Local Language Model Deployment

**Authors:** Kenan Alkiek, Moontae Lee, David Jurgens, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38006v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38006v1)

**Summary:** Running a language model locally offers advantages in privacy, latency, and cost, but local hardware fits only small models, which are less capable than frontier models. The usual remedy for a hard query, escalating it to a cloud model, gives up the privacy and cost advantages of running locally. A deployment that stays local faces two decisions for hard queries instead. First, it can spend more computation on a query, e.g., reasoning before answering, which raises accuracy at a cost in latency,...

---

### 28. Diagnosing and Improving Probabilistic Reasoning in Large Language Models

**Authors:** Huaman Sun, Dingcheng Wang, Jason Hartline, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38005v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38005v1)

**Summary:** Large language models (LLMs) are increasingly proposed as decision assistants who must reason probabilistically from available evidence under explicit decision costs. We propose a decision-theoretic framework that decomposes LLMs' decision loss into two components: forming accurate beliefs from provided evidence and translating those beliefs into actions that optimize a provided utility function. Using a synthetic benchmark with known ground truth, we apply the decomposition to characterize prob...

---

### 29. No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection

**Authors:** Jiaheng Guo, Haochen Zhang, Yu-Chao Huang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38004v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38004v1)

**Summary:** Time series anomaly detection (TSAD) plays a crucial role in healthcare, finance, industrial monitoring, and other sectors. Within and between these settings, anomalies span vastly different temporal scales, from sub-second point spikes to multi-hour drift patterns. However, most existing TSAD methods commit to a single temporal granularity, and multi-scale designs either analyze different scales in isolation or are constrained to a predefined coarse-to-fine hierarchy, both failing to sufficient...

---

### 30. BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from Agentic RAG Pipeline Signals

**Authors:** Julien Knafou, Luc Mottin, Alexandre Flament, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37993v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37993v1)

**Summary:** The BITEM team entered both subtasks of the NTCIR-19 R2C2 task with a single agentic pipeline, in which a model searches, reads and records evidence over a movie corpus while an orchestrator holds the record and rules on what may be submitted. A claim is admitted only once an entailment cascade has checked it against the passage it cites, and an answer is released only once enough checked evidence stands behind it. Each question is run three or four times, every pass retrieving from a corpus str...

---

### 31. Which Attention Heads are like the Human Head? Not the Ones that Compute

**Authors:** Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37991v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37991v1)

**Summary:** Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less d...

---

### 32. KV-Kaizen: Learning Context-Adaptive Cache Compression Choices

**Authors:** Joao Monteiro, Louis Béthune, Anastasiia Filippova, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37988v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37988v1)

**Summary:** As the context size of text processed with an LLM grows, the size of KV caches can outstrip the memory allocated for the original model weights. This impacts LLM throughput negatively, since decoding is memory-bound and decode cost grows with cache size. Recent work alleviates this bottleneck by discarding the least relevant tokens. Eviction introduces a tension, since a one-off decision to discard content may prove detrimental later. Instead, we focus on alternative choices that can lead to cac...

---

### 33. $S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient

**Authors:** Hongbo Ma, Sansheng Cao, Jiajun Fan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37976v1)

**Summary:** LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly...

---

### 34. On Trajectory-Aware Training for Masked Diffusion Language Models

**Authors:** Manuel Madeira, Amitis Shidani, Alice Bizeul, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37974v1)

**Summary:** Masked diffusion models (MDMs) generate text by unmasking several tokens per step, but they are trained and sampled under different conditions. The model is trained on randomly masked sequences, whereas inference follows a trajectory shaped by the model's own predictions. Additionally, each step has no access to what the previous one computed. Recent methods narrow these limitations from separate angles, leaving open how these choices interact. We introduce PUMBA, a unified framework for traject...

---

### 35. Dagger: Decoupling-based Model Stealing Attack against Graph Neural Networks

**Authors:** Ying Song, Xiaowei Jia, Balaji Palanisamy

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37972v1)

**Summary:** As Graph Neural Networks (GNNs) are widely deployed as Machine Learning-as-a-Service (MLaaS) APIs, model stealing attacks have emerged as a critical security threat. By querying a victim model's black-box API, an adversary can construct a functionally equivalent surrogate model, compromising proprietary intellectual property and downstream security. Existing GNN stealing attacks, however, rely on overly permissive assumptions, such as soft-label outputs, large query budgets, full-graph query acc...

---

### 36. SelfSearch: Reward-Free Search for Self-Improving Agents

**Authors:** Jungwoo Yang, In Jin Kong, Yohan Jo

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37968v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37968v1)

**Summary:** Advances in the coding capabilities of LLM agents allow them to inspect and modify their own instructions, tools, and execution procedures. Existing approaches use this ability to search for improved agents through repeated downstream evaluation, which incurs substantial costs and ties the search to the evaluated tasks. We introduce \textbf{SelfSearch}, a reward-free search procedure in which agents modify themselves using records of previous self-improvement episodes. These records capture the ...

---

### 37. BrainNet Studio: A Unified Toolkit for Brain Network Construction, Intelligent Analysis, and Visualization

**Authors:** Xiwei Zeng, Shengrong Li, Yiheng Liu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37956v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37956v1)

**Summary:** Brain networks characterize structural and functional relationships among brain regions and support research on cognition, brain disorders, and brain-computer interfaces. Their time-varying topology and higher-order spatiotemporal dependencies are not adequately represented by conventional static networks. Existing tools primarily focus on static connectomes and provide limited integration of dynamic network modeling with modern graph and sequence learning methods. We present BrainNet Studio, an...

---

### 38. Topological Coherence for Self-evolving Multi-agent Systems

**Authors:** Sen Zhao, Ruiqi Kong, Zuyu Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37953v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37953v1)

**Summary:** Complex tasks inherently couple workflow structure, agent responsibility, collaboration, and memory access: task regions delimit responsibility and tool scope, cross-region dependencies give rise to handoffs, and ownership boundaries delimit private and selectively shared memory. Existing methods can jointly optimize agent and communication structures, yet such optimization does not by itself require responsibility, handoff, and memory boundaries to remain consistent with task dependencies. We t...

---

### 39. Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

**Authors:** Bingjun Luo, Jialin Guo, Siqi Li

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37950v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37950v1)

**Summary:** Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video understanding agent uses its own language model to revise its harness. Through active vid...

---

### 40. Does Local Video Understanding Transfer Across Encounters? The EgoGears Benchmark

**Authors:** Yuedong Tan, Lei Qi, Yu Liu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37938v1)

**Summary:** Embodied systems must make knowledge acquired during one encounter usable in another despite changes in viewpoint, motion, and illumination. Yet aggregate cross-video accuracy conflates failures of local perception with failures to preserve observation identity, establish correspondence, and compose evidence, obscuring whether local video understanding actually transfers. We introduce EgoGears, a complementary single- and multi-video benchmark designed to diagnose this transition. It contains 56...

---

### 41. GRFBrain: Graph-Structured Rectified Flows for EEG Dynamic Modeling

**Authors:** Haohui Jia, Zheng Chen, Jathurshan Pradeepkumar, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37934v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37934v1)

**Summary:** Forecasting time-varying functional connectivity from electroencephalography (EEG) requires modeling both history-dependent trends and structured variability across channels. Conditional flow matching provides a framework for distributional forecasting, yet it remains unclear whether graph-informed source distributions offer practical advantages over isotropic noise and strong deterministic predictors. We introduce a graph-structured residual flow framework that separates conditional mean predic...

---

### 42. Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation

**Authors:** Chenjian Gao, Zhihao Hu, Jianqi Ma, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37925v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37925v1)

**Summary:** Autoregressive (AR) video diffusion enables low-latency, streamable video generation, but prediction errors often accumulate over long rollouts. Training the generator on its own rollouts exposes it to these imperfect histories. However, existing video-level distribution matching distillation (DMD) scores the whole rollout jointly. Because a chunk is evaluated together with its past and future, its correction can favor matching artifacts in the surrounding context merely to preserve temporal con...

---

### 43. RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust

**Authors:** Eugene Hauptmann, Nataliya Kosmyna

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37916v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37916v1)

**Summary:** Production machine learning (ML) stacks often split graph compilation and kernel execution across different layers and languages, making backend behavior, deployment guarantees, and performance fallbacks hard to reason about end-to-end. RLX addresses this gap with a single Rust codebase that combines compiler and runtime roles around one primitive-level, three-level intermediate representation (IR), plus a transparent dispatch contract that resolves each operator to native, common-IR, or rewritt...

---

### 44. The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment

**Authors:** Gonçalo Paulo, Louis Jaburi, Nora Belrose, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37914v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37914v1)

**Summary:** Fine-tuning large language models on narrow, misaligned tasks can undo their post-training alignment and induce novel misaligned behaviors -- a phenomenon known as \emph{emergent misalignment} (EM). EM has been linked to persona-like representations, where fine-tuning might reduce loss by amplifying a harmful or 'evil' persona. It remains unclear which properties of the training data drive this effect: whether all harmful examples contribute approximately equally to misalignment and whether diff...

---

### 45. Generated Query Expansion Still Helps Strong Sparse Retrieval: A Controlled Study with SPLADE-v3

**Authors:** Ryan C. Barron, Cade W. Trotter, Maksim E. Eren, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37911v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37911v1)

**Summary:** Scientific queries are often brief, while relevant papers use specialized vocabulary. Generated query expansion can bridge this mismatch, but earlier work suggests that its value shrinks as the underlying retriever becomes stronger. We test the four generated formats of term lists, a pseudo-document, multiple pseudo-references, and corpus-steered text all together with SPLADE-v3 on NFCorpus, TREC-COVID, and SciDocs. Every condition searches the same frozen document index and follows the same que...

---

### 46. Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics

**Authors:** Abhishek Pillai, Ekta Prashnani, Joohwan Kim, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37907v1)

**Summary:** Video games offer scalable environments for studying perception and control in embodied agents.Abundant online gameplay videos could supply demonstrations, but they rarely include player inputs for training. Inverse Dynamics Models (IDMs) have thus been proposed to infer inputs from frames. Large (up to 1B parameters) IDMs trained on $\sim$1K-2K gameplay hours demonstrate feasibility and cross-environment generalization at this scale, but researchers do not clarify what the key components are to...

---

### 47. Beyond Interaction Capacity: Estimator Scaling with Recursive Models for CTR Prediction

**Authors:** Shivang Chopra, Fotis Iliopoulos, Zsolt Kira, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37905v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37905v1)

**Summary:** Click-Through Rate prediction, a core task in recommendation and advertising systems, relies on modeling interactions among sparse categorical features. Explicit cross networks are a central paradigm for CTR prediction, and recent progress has largely come from increasing the interaction capacity of a single predictor through deeper cross networks and more expressive cross operators. We revisit whether continually increasing interaction capacity remains the most effective way to improve predicti...

---

### 48. You Cannot Pick a Provider From the Price List: Market-Aware Routing for Open-Weight LLM Inference

**Authors:** Liang He, Jingbo Wen, Yixiong Chen, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37902v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37902v1)

**Summary:** Existing LLM routers choose among models using static per-model costs. We show that open-weight inference markets introduce a second, largely ignored decision axis: after choosing a model, a client must still choose which provider serves it. Measuring live endpoints across [nummodels] open models, competing providers, multiple task types, and three measurement waves, we find that provider choice cannot be inferred from the price list. The same model can vary sharply in quality, latency, availabi...

---

### 49. Guide, Then Let Go: Gap-Adaptive Teacher Scheduling for Sparse-Reward Agentic RL

**Authors:** Youling Huang, Tiankuo Xu, Jiaji Liu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37898v1)

**Summary:** Reinforcement learning for long-horizon agents typically relies on sparse outcome-based rewards. This leads to a severe cold-start problem, as early-stage policies often fail to solve sampled tasks, leaving little useful reward signal for learning. To mitigate this problem, we use on-policy distillation (OPD) to provide token-level guidance on the student's own rollouts. We find that the benefit of this guidance depends on the performance gap between the teacher and the student. When the teacher...

---

### 50. Boids of a Feather Flock Together - Evolving Prey Behaviours Under Different Predator Attack Strategies

**Authors:** Augusta van Haren, Hanna Hoogen, Luca Pattavina

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37885v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37885v1)

**Summary:** Flocking and schooling are thought to have evolved partly as defences against predation, but how prey should balance social and escape tendencies may depend on the predator's hunting strategy. We extend the predator-prey boids model of Ojo et al. (2023), itself based on Reynolds' boids, by combining six prey movement tendencies (alignment, cohesion, separation, dodge, repel and wiggle) into a single weighted acceleration update, and by reformulating wiggle as a sinusoidal manoeuvre. We then use ...

---

## cs.CL

**50 papers**

### 1. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

**Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38177v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38177v1)

**Summary:** Reasoning about the 3D world from multi-view images remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While modern MLLMs handle single-image inputs effectively, they struggle to integrate evidence across viewpoints into a coherent 3D understanding. A growing body of work attempts to close this gap by injecting 3D awareness into MLLMs, either by boosting fine-grained pixel-level cross-view correspondence or by fusing features from 3D geometry foundation models, yet a s...

---

### 2. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

**Authors:** Bingchen Yao, Haobo Xu, Haokun Lin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38169v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38169v1)

**Summary:** Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding st...

---

### 3. EmoRES-TTS: Residual-Enhanced Vector Steering for Emotional Speech Generation

**Authors:** Kuan-Po Huang, Haohe Liu, Puyuan Peng, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38157v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38157v1)

**Summary:** Emotion-conditioned text-to-speech (TTS) models may fail to express the requested emotion reliably, and improving controllability by additional training is costly in both computation and emotion-labeled speech training data. We therefore study vector steering, a training-free approach that modifies the internal representations of a frozen model. CoCoEmo, a conventional vector steering method for emotion TTS, treats each emotion vector as an indivisible direction controlled by a single global str...

---

### 4. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies

**Authors:** Hui Ren, Lei Fan, Henry Pao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38155v1)

**Summary:** Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Enti...

---

### 5. Pretraining Latent Information Feedback Transformers with Teacher Supervision

**Authors:** Dor Tirosh, Ido Amos, Mor Geva

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38149v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38149v1)

**Summary:** Transformer language models (LMs) are feed-forward: deep-layer representations are never fed back to shallower layers, and the only pathway for information to flow downward across generation steps is the decoded token. This narrow channel forces models to recompute intermediate results and to discard alternative continuations. In this work, we remove this bottleneck during pretraining, introducing the LIFT (Latent Information Feedback Transformer) architecture and training method which enable LM...

---

### 6. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

**Authors:** Cheng Qian, Kunlun Zhu, Beibin Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38143v1)

**Summary:** Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the f...

---

### 7. AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation

**Authors:** Rishabh Agrawal, Hejie Cui, Shasha Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38142v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38142v1)

**Summary:** A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice ...

---

### 8. LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning

**Authors:** Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38137v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38137v1)

**Summary:** Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic m...

---

### 9. From Routing Signals to Selective Review: Visual regrounding in MoE VLMs

**Authors:** Hongzhu Guo, Mohsen Fayyaz, Nanyun Peng

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38111v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38111v1)

**Summary:** Vision-language models (VLMs) may accept false visual premises, answering questions about a target object's color, count, location, or state even when it is absent. We call this reliability-critical behavior a target-absence grounding failure. Existing visual-grounding detectors primarily rely on generated responses, hidden states, or uncertainty measures. We present the first framework to leverage internal routing decisions in Mixture-of-Experts (MoE) VLMs to detect target absence before genera...

---

### 10. How Local Mixing Encodes Relative Position in Global NoPE Attention

**Authors:** Cutter Dawes, Nick Alonso, Tom Figliolia, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38109v1)

**Summary:** The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in...

---

### 11. Correct Answers, Invalid Traces: What Verifiable Grade-School Math Reveals About Chain-of-Thought Traces

**Authors:** Ratish Puduppully, Pranabendu Misra, Paarth Iyer, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38107v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38107v1)

**Summary:** Chain-of-thought traces are widely read as records of how models reach their answers, informing debugging, agent auditing, and claims about reasoning. Testing this interpretation is difficult because natural-language thinking traces are rarely mechanically verifiable. We revisit it in iGSM, a synthetic grade-school mathematics benchmark designed to study thinking traces and used to support claims of learned reasoning and planning. Crucially, iGSM exposes the exact quantities and dependencies tha...

---

### 12. Pruning for Efficiency, Paying in Fairness: Demographic Disparities in Pruned Speech-LLMs

**Authors:** Ganesh Pavan Kartikeya Bharadwaj Kolluri, Michael Kampouridis, Ravi Shekhar

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38106v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38106v1)

**Summary:** Speech-LLMs are expensive to run, making compression important for real-world deployment. However, compressed models are usually selected using aggregate word error rate (WER), which can hide how pruning affects different demographic groups. In this work, we systematically study the effect of audio encoder pruning on SLAM-ASR for different demographic groups. Using the Fair-Speech and Common Voice datasets, we found that the pruning does not affect all demographic groups equally; the gap between...

---

### 13. Effective Dense Retrieval using Only In-Context Examples

**Authors:** Nour Jedidi, Abdul Basit Ali, Hang Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38099v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38099v1)

**Summary:** Turning decoder-only large language models (LLMs) into strong dense retrievers typically requires some form of retriever training. In this paper, we ask whether LLMs can instead be prompted to produce effective representations for dense retrieval given only a few in-context examples. To answer this, we introduce RICE (Representations from In-Context Examples), a simple "training-free" approach that extracts high-quality dense representations from LLMs. To do so, RICE conditions the LLM on exampl...

---

### 14. Gender bias across LLMs is common and highly heterogenous

**Authors:** Edoardo Bolzoni, Valerio Capraro

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38036v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38036v1)

**Summary:** Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and mor...

---

### 15. Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large Language Models

**Authors:** Zhenyu Wang, Tianze Wang, Linjun Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38025v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38025v1)

**Summary:** On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher. Vanilla OPD treats all teacher signals equally, assuming that the teacher's supervision is equally important for every token. However, teacher signals at different tokens may have very different effects on the student's performance: some correct important reasoning errors, while others have little effect on the final answer. Motivated by this observation, we ...

---

### 16. Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S

**Authors:** Christopher J. Chanhnourack

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38021v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38021v1)

**Summary:** We evaluate an auditable long-term memory system on LongMemEval-S. Its retrieval chain uses hybrid candidate retrieval, cross-encoder reranking, coverage-first packet compilation, and deterministic reasoning scaffolds; an LLM is used only as a replaceable final reader. The chain places all gold sessions in the candidate pool for 468/470 answerable questions and produces gold-complete packets for 462/470. With a Claude Opus reader called through an unpinned CLI alias, two 500-question passes scor...

---

### 17. BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from Agentic RAG Pipeline Signals

**Authors:** Julien Knafou, Luc Mottin, Alexandre Flament, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37993v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37993v1)

**Summary:** The BITEM team entered both subtasks of the NTCIR-19 R2C2 task with a single agentic pipeline, in which a model searches, reads and records evidence over a movie corpus while an orchestrator holds the record and rules on what may be submitted. A claim is admitted only once an entailment cascade has checked it against the passage it cites, and an answer is released only once enough checked evidence stands behind it. Each question is run three or four times, every pass retrieving from a corpus str...

---

### 18. $S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient

**Authors:** Hongbo Ma, Sansheng Cao, Jiajun Fan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37976v1)

**Summary:** LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly...

---

### 19. On Trajectory-Aware Training for Masked Diffusion Language Models

**Authors:** Manuel Madeira, Amitis Shidani, Alice Bizeul, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37974v1)

**Summary:** Masked diffusion models (MDMs) generate text by unmasking several tokens per step, but they are trained and sampled under different conditions. The model is trained on randomly masked sequences, whereas inference follows a trajectory shaped by the model's own predictions. Additionally, each step has no access to what the previous one computed. Recent methods narrow these limitations from separate angles, leaving open how these choices interact. We introduce PUMBA, a unified framework for traject...

---

### 20. SelfSearch: Reward-Free Search for Self-Improving Agents

**Authors:** Jungwoo Yang, In Jin Kong, Yohan Jo

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37968v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37968v1)

**Summary:** Advances in the coding capabilities of LLM agents allow them to inspect and modify their own instructions, tools, and execution procedures. Existing approaches use this ability to search for improved agents through repeated downstream evaluation, which incurs substantial costs and ties the search to the evaluated tasks. We introduce \textbf{SelfSearch}, a reward-free search procedure in which agents modify themselves using records of previous self-improvement episodes. These records capture the ...

---

### 21. Learning What to Remember: Long-horizon Counterfactual Memory Optimization

**Authors:** Jiaming Tang, Mingyan Liu, Armin Sarabi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37930v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37930v1)

**Summary:** Persistent textual memory allows language models to carry information across long interactions, but learning what to remember is fundamentally a credit-assignment problem. A memory rewrite may only become useful many steps later, while much of the observed utility may be inherited from information already stored before the rewrite. We introduce Memory Gain Policy Optimization (MGPO), which isolates the incremental value of each memory rewrite by crediting it for its marginal contribution to curr...

---

### 22. Time-Anchored Diffusion Language Models: Latent-Space Caching for Fast Generation

**Authors:** Joel Anto Paul, Litu Rout, Aditya Akella, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37924v1)

**Summary:** Recent work on anchored diffusion language models improves denoising by shaping an intermediate latent space with supervised important-token targets. In this work, we introduce time-based (self-supervised) anchoring, which learns and reuses latent anchors without requiring such targets. Our key observation is that anchors encode persistent properties of the clean sequence, such as its semantic intent, global structure, or intermediate plan. Although their hidden representations become stale as t...

---

### 23. Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning

**Authors:** Md. Ismail Hossain, Humaira Kousar, Isidora Chara Tourni

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37915v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37915v1)

**Summary:** On-policy self-distillation (OPSD) trains a student to match a privileged teacher distribution along its own sampled trajectory. Standard OPSD applies this supervision to unverified student rollouts while conditioning the teacher on privileged context, typically a reference solution. We separate these roles in a factorial analysis and find that scaffold correctness has a stronger effect on downstream accuracy than context correctness. Unverified scaffolds create an imitation gap because the teac...

---

### 24. The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment

**Authors:** Gonçalo Paulo, Louis Jaburi, Nora Belrose, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37914v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37914v1)

**Summary:** Fine-tuning large language models on narrow, misaligned tasks can undo their post-training alignment and induce novel misaligned behaviors -- a phenomenon known as \emph{emergent misalignment} (EM). EM has been linked to persona-like representations, where fine-tuning might reduce loss by amplifying a harmful or 'evil' persona. It remains unclear which properties of the training data drive this effect: whether all harmful examples contribute approximately equally to misalignment and whether diff...

---

### 25. It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs

**Authors:** Pierre-Carl Langlais, Pieter Delobelle, Yannick Detrois, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37891v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37891v1)

**Summary:** Current pre-training datasets are derived from web crawls, with all their issues, and were not designed to support mid- and post-training pipelines--for instance, they contain little explicit reasoning. Thus, many frontier labs have begun to develop their own internal datasets, starting from state-of-the-art models, to augment their pre-training data mix, eg, with reasoning traces to address cold-start problems. While demonstratively effective, none of these datasets are public, and the effect o...

---

### 26. Zero-shot Dependency Parsing with Unsupervised Cross-Lingual Bootstrapping

**Authors:** Lalita Lowphansirikul, Attapol Rutherford, Jian Gang Ngui, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37883v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37883v1)

**Summary:** Pre-trained language models (PLMs) with encoder-based architectures have shown impressive capabilities in zero-shot cross-lingual transfer for various language understanding tasks. However, applying this technique to dependency parsing remains a significant challenge due to its syntactic nature. To boost model generalizability across linguistic typologies, we propose a cross-lingual unsupervised bootstrapping method to improve syntactic knowledge within the PLM. We show that our method achieves ...

---

### 27. How Many Labels Does a Language Need? Annotation Budgets and Cross-Lingual Pooling for African-Language Text Classification

**Authors:** Bhanu Prakash Vangala, Sowmya Guda, Navya Vangala

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37882v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37882v1)

**Summary:** Every text classifier for an African language begins with a budgeting question: how many labelled examples are needed, and can labels from other African languages stand in for them? We answer both questions empirically for 28 language-task pairs, news topic classification in 16 languages (MasakhaNEWS) and tweet sentiment in 12 languages (AfriSenti), using a character n-gram linear model that trains in seconds on two CPU cores with no pretrained weights and no accelerator. Monolingual learning cu...

---

### 28. Retrieval Capacity of Self-Attention Under Competition

**Authors:** Timur Mudarisov, Mikhail Burtsev, Radu State

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37879v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37879v1)

**Summary:** How many tokens from its context does a language model actually use, and what determines that number? We study this question through self-attention. Without retraining, we retain only the tokens with the highest attention weights at each head, layer, and query, keeping their original weights unchanged. By varying the selected set size and measuring the increase in negative log-likelihood (NLL), we estimate the effective attention set size needed to stay within a chosen loss tolerance. Relatively...

---

### 29. Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR

**Authors:** Doohyuk Jang, Yoonsik Park, Gyouk Chu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37868v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37868v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) methods such as GRPO rely on successful self-generated trajectories, but finite rollout budgets can produce all-fail groups with no reward-based policy-gradient signal. While additional rollouts improve the chance of success at higher cost, successful trajectories missing from one model's rollouts may already have been discovered by another. Indeed, we observe that heterogeneous models often succeed on complementary prompts, creating opportun...

---

### 30. It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them

**Authors:** Nagham Omar, Mahmoud Jabarin, Kinan Ibraheem, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37863v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37863v1)

**Summary:** Vision-language models (VLMs) are increasingly used in place of human annotators, making it important that substitutability tests reflect the model rather than incidental evaluation conditions. We introduce MIST, the Misleading-Image Stress Test: 200 English sentences, each built around a phrase readable either figuratively or literally and shown with an aligned image depicting its reading, a misleading image depicting the opposite, or no image at all. The guidelines require the label to be deci...

---

### 31. One Threshold Does Not Fit All Languages: Language-Conditional Deferral for Reliable and Efficient Low-Resource Text Classification

**Authors:** Bhanu Prakash Vangala, Vangala Navya

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37861v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37861v1)

**Summary:** In the Global South, the lower-income countries of Africa, Asia, and Latin America where most of the world's languages are spoken, a deployed text classifier usually runs on ordinary CPUs, serves many languages with a single model, has few labeled examples in any of them, and relies on people to catch its mistakes. Such a system is only useful if it can promise how often it will be wrong: at most a fixed fraction of the labels it assigns on its own may be incorrect, and everything else must go t...

---

### 32. Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning

**Authors:** Tianhao Qian, Ziming Hong, Chongyang Gao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37858v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37858v1)

**Summary:** Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization. The parameters most associated with a target, however, need not be the best ones to update, and candidate interventions can change value as optimization proceeds. In a controlled experiment, a storage-localization score reaches an area under the receiver operating characteristic curve (AUROC) of 0.981, yet storage identity agrees with the ...

---

### 33. AnthroDial: Benchmarking LLM Anthropomorphism in Autonomous Social Interaction

**Authors:** Wentao Liu, Xi Chen, Siyu Song, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37853v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37853v1)

**Summary:** Large language models (LLMs) are increasingly deployed as social agents, yet credible human-like interaction requires more than fluent responses or persona consistency. Agents must autonomously decide whether, when, and how to communicate while adapting to evolving contexts, goals, and relationships. Existing research, however, lacks a unified approach to enabling, evaluating, and improving such capabilities in continuous, open-ended interaction. We introduce AnthroDial, a unified framework for ...

---

### 34. Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment

**Authors:** Haotian Deng, Wenbin Xing, Gang Xu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37837v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37837v1)

**Summary:** Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses. Existing safety methods often require large preference datasets, costly multi-rollout training, or additional safeguards at inference time. They may also sacrifice helpfulness by directly refusing requests that could be answered safely. In this paper, we propose Intent-Privilege On-Policy Self-Distillation (OPSD), which leve...

---

### 35. Can a Cacheable Decision Model Follow Rules?

**Authors:** Dushyant Rajput, Nirdesh Chauhan, Siddharth Kosaraju

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37832v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37832v1)

**Summary:** Certo is a small non-generative decision model (Qwen3-4B): it scores candidate actions from their text and returns a probability, instead of generating an answer. The accurate design reads the state, the rules, and each candidate together (a joint scorer), so cost grows with the menu. Independent encoding lets each candidate be encoded once and reused across states (about 5x cheaper at 77 candidates), but separates state from candidate. We ask how much rule-sensitivity survives that move, and wh...

---

### 36. The Geometry of Inference in Transformer Residual Streams

**Authors:** Timur Mudarisov, Mikhail Burtsev, Radu State

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37824v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37824v1)

**Summary:** Transformer language models build predictions through successive residual updates, but how their representations become specific to an eventual outcome remains unclear. We study this process by comparing intermediate residual states with their own final states and an empirical bank of final states from other contexts. Across six pretrained language models, the own endpoint becomes preferable to the average alternative early, while many individual endpoints remain closer. These competing sets gen...

---

### 37. Thinking in Depth, Speaking Directly: Recurrent Latent Reasoning for Paralinguistically Grounded Spoken Dialogue

**Authors:** Shengbo Cai, Yuxiang Wang, Jingran Xie, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37818v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37818v1)

**Summary:** Empathetic spoken dialogue requires models to use both what is said and how it is said to decide how to respond. Explicit CoT can improve paralinguistic perception and make acoustic cues more explicit in replies, yet does not ensure their effective use in response planning. We call this mismatch the perception-reasoning gap. In addition, CoT may not fully capture acoustic cues in words, and generating it adds inference latency. To address these limitations, we introduce LoopSLM, which builds on ...

---

### 38. CompOrca: Corpus-Scale Compliance Labelling of Instruction-Tuning Data

**Authors:** Philipp E. Glass, Alina Miron

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37807v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37807v1)

**Summary:** Studying how fine-tuning shapes refusal and noncompliance behaviour requires identifying training examples that refuse, evade or otherwise fail to fulfil the requested task. But existing annotation covers evaluation sets of a few thousand prompts at most. We present CompOrca, a compliance labelling over the entirety of the 4,233,923-example OpenOrca corpus. Every example was classified as compliant or noncompliant by five independent passes of an open-weight LLM judge (LongCat-2.0, 1.6T paramete...

---

### 39. A Proposed Rubric for Evaluating Expressed Clinical Reasoning in Large Language Model Responses

**Authors:** Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37788v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37788v1)

**Summary:** Rubrics support the structured evaluation of language models. We propose a rubric for assessing expressed clinical reasoning in model responses, drawing on three bodies of work: medical education assessment frameworks (ART, SCT, Key Feature Problems and OSCE); clinical LLM benchmarks (MedR-Bench, HealthBench, TIMER-Bench, DR.BENCH, PrIME-LLM and PatientSafeBench); and general LLM reasoning evaluation research, including the Factuality-Validity-Coherence-Utility taxonomy, FaithCoT-Bench and C2-Fa...

---

### 40. Selecting What Matters: Semantic Compression-Guided Selective Pooling for Long-Context Embeddings

**Authors:** Zifeng Cheng, Jie Zheng, Zhiwei Jiang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37782v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37782v1)

**Summary:** Large language models (LLMs) have shown strong potential as training-free text encoders for long-context embeddings. Existing approaches primarily improve information flow under causal attention and typically construct embeddings by uniformly averaging all token representations. However, for long documents, such mean pooling can dilute salient semantic information with abundant redundant or weakly informative content. To this end, we propose SCSP, a training-free framework that leverages semanti...

---

### 41. Which papyrus HTR is good enough? Character-error-rate tolerance of four papyrological tasks on Greek texts

**Authors:** Anton Repushko, Elena Chepel

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37755v1)

**Summary:** Purpose: Most Greek papyri remain unpublished and undigitised; a handwritten text recognition (HTR) pipeline that transcribes them automatically would let scholars discover documents and literary works that have so far gone unread. Recognition systems for Ancient Greek papyri are in statu nascendi, and how accurate they must be for a given papyrological task has not been examined. To answer this and set a benchmark for Greek papyrus HTR, we test a range of character error rates (CER) against fou...

---

### 42. Context Language Models

**Authors:** Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37725v1)

**Summary:** We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety o...

---

### 43. Predictive Geometry of Hidden Trajectories in Transformers

**Authors:** Timur Mudarisov, Mikhail Burtsev, Tatiana Petrova, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37717v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37717v1)

**Summary:** Decoder-only transformers are trained only through a terminal next-token prediction loss, yet this loss constrains every intermediate hidden state through the fixed downstream computation. We formalize this constraint by studying layerwise loss-to-go functions: the terminal loss obtained by continuing a candidate hidden state through the remaining transformer blocks. Around successful validation trajectories, we show that the local second-order geometry of these functions is governed, up to low-...

---

### 44. Billiger.de Products: A Bilingual Entity Matching Benchmark

**Authors:** Aaron Steiner, Ksenia Elagin, Ralph Peeters, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37713v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37713v1)

**Summary:** Existing product matching benchmarks primarily contain English-language product data and are often dominated by a single product category, such as electronics. This paper introduces Billiger.de Products, a bilingual German and English entity matching benchmark covering thirteen consumer product categories, including difficult-to-handle categories such as clothing and furniture. The benchmark data originates from the German price comparison platform billiger.de. Following the design of WDC Produc...

---

### 45. Reader Proficiency Shapes Layer-wise Surprisal Profiles

**Authors:** Akio Hayakawa, Horacio Saggion

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37688v1)

**Summary:** Reading behaviour varies not only with linguistic input, but also with reader proficiency. In this study, we investigate whether the layer-wise relationship between surprisal from large language models (LLMs) and human gaze behaviour differs across readers with different levels of proficiency and across gaze measures. Using eye-tracking data from the MECO L2 corpus, we compare readers with high and low vocabulary proficiency on first-pass gaze duration (FPGD) and total gaze duration (TGD). We qu...

---

### 46. EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?

**Authors:** Hongcheng Gao, Hailong Qu, Yu Lei, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37686v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37686v1)

**Summary:** Autonomous agents have made rapid progress in general-purpose computer use, but reliable automation of professional industrial engineering remains out of reach, as engineering workflows demand reasoning over geometric and physical constraints and dependencies preserved across software and design stages. We present EngiWorld, the first benchmark structured around the complete design loop: 1,301 expert-curated tasks spanning 6 engineering domains (CAD, CAE, CAM, BIM, EDA, and 3D visualization) and...

---

### 47. When Models Don't Manipulate Manifolds: The Geometry of a Comparison Task

**Authors:** Sai Sumedh R. Hindupur, Hadas Orgad, Thomas Fel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37680v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37680v1)

**Summary:** One of the current premises of mechanistic interpretability research is that detailed accounts of the geometry of neural network representations can tell us how models perform computations, and how to effectively intervene on them. While low dimensional manifolds have been observed for multiple concepts in the literature (e.g. numbers encoded on helices, days of the week on a circle, ...), with structure believed to reflect properties of data and tasks, the extent to which models rely on them fo...

---

### 48. KUPAS MASTER: Distilling the Tacit Expertise of Master Practitioners into Agent-Ready Experience Corpora

**Authors:** Changmian Wang, Yuchao Ma, Xuchao Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37673v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37673v1)

**Summary:** Experienced professionals know more than just facts and conclusions. They know which cues matter, why a judgment is reasonable, and which action to take. Routine work records often leave out this tacit knowledge, making it difficult for Large Language Model (LLM) agents to use professional experience effectively. We introduce KUPAS MASTER, an experience engineering platform built around nine-layer cognitive corpus construction. It turns heterogeneous work records and practitioner interviews into...

---

### 49. Corpus-Guided Dual-Path Propagation for Graph Retrieval-Augmented Generation

**Authors:** Baoxian Liu, Tong Wei

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37661v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37661v1)

**Summary:** Graph-based retrieval-augmented generation supports multi-hop retrieval by organizing corpus information into graphs. However, existing relation-free graph retrieval methods rely primarily on query-sentence similarity to search for evidence. This can exclude useful bridging evidence with low query similarity and activate incidental entities unrelated to the reasoning chain. In this paper, we propose a simple and effective approach called NexusRAG, which augments the relation-free Tri-Graph with ...

---

### 50. Evaluating and Benchmarking the System One Model Jev

**Authors:** Tobias Deußer, Lorenz Sparrenberg, Rafet Sifa

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37647v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37647v1)

**Summary:** Jev is a commercial System One model from TypeSafe AI that does not generate text: given a state and typed questions, it returns a choice from fixed options, a position on a rubric, or the probability that a statement is true, with probabilities the vendor describes as calibrated. Such models target small decisions in information access pipelines, such as routing queries, checking grounding, moderating content, or rating against a rubric. We evaluate Jev (jev-1.13.0) zero-shot on 37 datasets spa...

---

## cs.CV

**50 papers**

### 1. Point2Part: Unified 3D Partitioning from Point Prompts

**Authors:** Hao-Tang Tsui, Yu-Rou Tuan, Xiaoxuan Ma, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38180v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38180v1)

**Summary:** Existing 3D part decomposition methods do not necessarily partition the original shape into non-overlapping parts that collectively cover the entire shape, allowing overlaps or gaps that hinder downstream part-level applications. We instead formulate part decomposition as a joint partitioning of the entire shape, where the predicted parts are non-overlapping and jointly recover the entire shape. Our key insight is that part decomposition should consider all desired parts jointly, rather than mod...

---

### 2. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

**Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38177v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38177v1)

**Summary:** Reasoning about the 3D world from multi-view images remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While modern MLLMs handle single-image inputs effectively, they struggle to integrate evidence across viewpoints into a coherent 3D understanding. A growing body of work attempts to close this gap by injecting 3D awareness into MLLMs, either by boosting fine-grained pixel-level cross-view correspondence or by fusing features from 3D geometry foundation models, yet a s...

---

### 3. Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation

**Authors:** Zihan Wang, Zhen Wu, Pieter Abbeel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38172v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38172v1)

**Summary:** Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse tra...

---

### 4. Adversarial Training for Pixel Diffusion

**Authors:** Xin Lin, Zhifei Zhang, Yuqian Zhou, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38170v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38170v1)

**Summary:** Pixel diffusion models generate RGB images directly, avoiding the bottleneck of an autoencoder, yet their outputs still systematically underrepresent fine-scale natural-image statistics. We show that adversarial learning provides an effective post-training correction for this deficiency. Starting from a pretrained model, we retain its original diffusion or flow-matching objective and add an adversarial loss to the predicted output at non-high-noise timesteps, leaving the model architecture and s...

---

### 5. Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data

**Authors:** Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38165v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38165v1)

**Summary:** The landscape of satellite imagery time series datasets and boundary-pushing architectures for cropland segmentation has never been richer. However, in this gold rush, important truths are being missed on both fronts, as a drive for the most novel concepts or the largest datasets pushes finer details to the side. In this paper, we present our hybrid transformer-convolutional model, Cropland Parallel Attention and Refinement Network for Segmentation (PAtteRNS), the first model to use self-attenti...

---

### 6. Rethinking Representations for World-Action Modeling

**Authors:** Haoyi Jiang, Liu Liu, Xinjiang Wang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38163v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38163v1)

**Summary:** World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction. We study the design of this space through controlled comparisons, finding that neither reconstruction fidelity nor pre-trained perceptual features alone ensure effective policy learning. These findings motivate ReWAM, a representation-centric world-action model built on pre-trained DINO features. Feature Calibration and a Temporal Represen...

---

### 7. DMA$^2$: Pixel-space Distribution Matching with Adversarial and Anchor Losses

**Authors:** Xin Lin, Zhifei Zhang, Yuqian Zhou, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38156v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38156v1)

**Summary:** Distribution matching distillation (DMD) provides a general framework for few-step diffusion generation, but its modern text-to-image instantiations have been developed primarily around latent diffusion. It therefore overlooks key properties and design opportunities of native RGB. We revisit two DMD interfaces for pixel-space teachers. On the teacher-matching side, diagnostics show low-noise RGB matching is dominated by a local-texture cue, motivating a fixed high-noise matching band. On the rea...

---

### 8. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies

**Authors:** Hui Ren, Lei Fan, Henry Pao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38155v1)

**Summary:** Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Enti...

---

### 9. LongLive-Plug: Once-for-All Distillation for Video Generation

**Authors:** Shuai Yang, Luozhou Wang, Wei Huang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38154v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38154v1)

**Summary:** Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or to improve long-video generation. This stage is typically repeated for every specialized model. We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs on a base model for training-free, plug-and-play deployment to compatible downstream models. Th...

---

### 10. PowerSim: Differentiable Physics Simulation and Rendering with Power Diagrams

**Authors:** Trong-Tung Nguyen, Anand Bhattad

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38153v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38153v1)

**Summary:** We introduce PowerSim, a method to bring physically grounded, differentiable dynamics to PowerFoam's power diagram based 3D representation. PowerSim directly couples a pre-trained PowerFoam scene to the Material Point Method (MPM) by exploiting a natural alignment between the two: the geometric and appearance properties of each primitive correspond closely to the quantities MPM already tracks as an object deforms. Consequently, simulated motion can drive the scene's geometry and appearance direc...

---

### 11. FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation

**Authors:** Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38152v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38152v1)

**Summary:** We introduce FracGen, a fracture-aware video generation model that produces plausible, controllable fracture dynamics from a single image of an intact object, conditioned on physics signals. To train FracGen, we build FracSim, a fracture-aware simulation framework that augments material point method (MPM) simulation with a continuum damage model, producing paired fracture videos and dense, pixel-aligned physical fields at no additional cost beyond standard rendering. FracGen leverages these maps...

---

### 12. LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation

**Authors:** Shengxiang Ji, Boyang Wang, Haiyang Xu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38146v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38146v1)

**Summary:** We introduce LIFT, a unified image-to-video generation framework that complements camera control with Layout-In-FuTure control, enabling users to specify what should appear in a future view and where it should appear. This addresses a practical need in controllable video generation: given an initial image, users often care not only about how the camera moves, but also about what the scene should look like at key future moments, especially the final frame. Existing camera controls specify viewpoi...

---

### 13. Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE

**Authors:** Yu Xu, Yuxin Zhang, Xiao Yang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38140v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38140v1)

**Summary:** Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models. However, conventional token-wise MoE routes tokens independently within a homogeneous expert pool and regularizes expert usage toward uniformity, making it poorly matched to video data that is spatiotemporally redundant and semantically long-tailed. We show that existing visual MoEs fall into a uniformity trap: semantically under-organized routing, compounded by uniform e...

---

### 14. CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer

**Authors:** Teng Zhou, Yunhao Chen

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38136v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38136v1)

**Summary:** Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference appear in the generated output. Although prior data-driven and training-free methods can reduce leakage, they often face a leakage-degradation dilemma: stronger content suppression may weaken style fidelity, while richer style preservation may reintroduce unwanted reference content. We identify this d...

---

### 15. HelixWorld: A Real-time Interactive Audio-Visual World Model

**Authors:** Lei Ke, Jiahao Pan, Zeyue Tian, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38123v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38123v1)

**Summary:** World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time. Yet prevailing interactive world models remain strictly silent, focusing exclusively on visual rendering and control while overlooking the acoustic dimension. We present HelixWorld, a real-time interactive audio-visual world model where visual scenes and camera-grounded spatial stereo sound co-evolve natively under user interaction. We curate a high-fidelity spatial audio-visual dataset...

---

### 16. VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents

**Authors:** Jinfa Huang, Jianming Xu, Jingyang Lin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38119v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38119v1)

**Summary:** Long-form video understanding requires multimodal agents to iteratively gather evidence over many reasoning steps. However, most existing agentic methods suffer from semantic thrashing: as append-only working memory grows, attention to key evidence collapses, and the agent loses access to what it has already found. First, we provide a structural argument showing that append-only memory can incorporate newly observed target evidence, but cannot remove accumulated noise or prevent ordered context ...

---

### 17. GA-EIRFS: A Geometry-Augmented Repeat-Factor Sampling Method for Long-Tailed LiDAR 3D Object Detection

**Authors:** Taufiq Ahmed, Constantino Álvarez Casado, Daniel Herrera Castro, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38116v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38116v1)

**Summary:** Long-tailed 3D object detection is treated as a class-frequency problem, but LiDAR supervision quality depends on object observability: similar frequencies can hide different geometric evidence. We introduce Geometry-Augmented Exponentially Weighted Instance-Aware Repeat Factor Sampling (GA-EIRFS), a detector-agnostic method that modulates a frequency-based repeat factor with a fixed geometry score combining point count, surface-normal entropy, and surface coverage. GA-EIRFS changes only frame-s...

---

### 18. Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History

**Authors:** Weiqiang Wang, Zhuokun Chen, Yusheng Dai, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38114v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38114v1)

**Summary:** Autoregressive video diffusion enables interactive streaming generation, but suffers from error accumulation over long rollouts. Self-rollout training reduces exposure bias, yet finite rollouts leave long-range drift unresolved. We observe that the noise level of the history key-value (K/V) representations trades visual quality against motion, and that restoring gradients through the history aligns causal training far more closely with bidirectional training. Motivated by these observations, we ...

---

### 19. From Routing Signals to Selective Review: Visual regrounding in MoE VLMs

**Authors:** Hongzhu Guo, Mohsen Fayyaz, Nanyun Peng

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38111v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38111v1)

**Summary:** Vision-language models (VLMs) may accept false visual premises, answering questions about a target object's color, count, location, or state even when it is absent. We call this reliability-critical behavior a target-absence grounding failure. Existing visual-grounding detectors primarily rely on generated responses, hidden states, or uncertainty measures. We present the first framework to leverage internal routing decisions in Mixture-of-Experts (MoE) VLMs to detect target absence before genera...

---

### 20. VISTA: Internalizing Collective Visual Experience via On-Policy Distillation for Active Multimodal Agents

**Authors:** Zheng Jiang, Houde Qian, Yiming Chen, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38086v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38086v1)

**Summary:** Active multimodal agents use visual tools to acquire task-relevant evidence while reasoning. Although reinforcement learning samples multiple interaction trajectories per input, outcome-based objectives primarily use the group to estimate scalar advantages, leaving complementary visual discoveries underused. We introduce VISTA, which internalizes collective visual experience through on-policy distillation by turning observations from same-input rollouts into shared supervision. Collective visual...

---

### 21. OmniTaskonomy: When Does Visual Generation Improve Visual Understanding?

**Authors:** Jiaxin Ge, Yiming Qin, Ji Xie, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38079v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38079v1)

**Summary:** Training a model to generate visual content can encourage it to learn rich perceptual capabilities related to geometry, spatial relationships, and objectness; yet, its benefits for visual understanding remain unclear. We ask: when and how does visual generation supervision improve visual understanding? We study controlled pairs of image-to-image (I2I) generation and image-to-text (I2T) understanding tasks that express the same underlying problem in different output modalities. We find that under...

---

### 22. MUGEN: Interactive Panoramic World Exploration via Camera Control

**Authors:** Jiaming Tan, Zhen Li, Shuwei Shi, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38077v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38077v1)

**Summary:** Interactive panoramic video generation aims to synthesize immersive 360\textdegree{} videos that remain visually coherent while following user-specified camera trajectories during exploration. However, progress is limited by a coupled data-and-model gap: existing panoramic video datasets are often short, weakly annotated, or lack camera trajectories, while existing camera-controlled video generation models are designed for perspective videos and do not directly support panoramic geometry. In thi...

---

### 23. RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA

**Authors:** Chengjie Jiang, Yunqi Zhou, Jiafeng Yan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38072v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38072v1)

**Summary:** Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires models to resolve small visual evidence within extremely large images. Existing approaches typically rely on token pruning, visual search, or tool-augmented reasoning at inference time. We instead investigate whether the benefit of zoom-in visual privilege can be internalized into the model. We introduce RS-OPSD, a reliable privileged on-policy self-distillation (OPSD) framework for UHR remote sensing VQA. To pro...

---

### 24. WorldLine: Action-Driven Visual Simulation for Robotic Manipulation

**Authors:** Shenghe Zheng, Wenbo Li, Jiyao Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38059v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38059v1)

**Summary:** Real-world robot learning is constrained by the cost of collecting experience and evaluating candidate behaviors. Video generation models offer a scalable foundation for visual simulators that predict action outcomes before physical execution. Yet they often favor visual plausibility over accurate action following and coherent robot--object dynamics, while action-conditioned simulators depend on scarce, embodiment-specific data that are difficult to share across incompatible control spaces. We i...

---

### 25. EVO-WAM: Evolving World Action Models through Video-Action Verification

**Authors:** Shiyang Zhou, Xionghao Wu, Wenbo Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38057v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38057v1)

**Summary:** Improving robot policies on new tasks without collecting additional expert demonstrations remains a central challenge in robot learning. World action models (WAMs) use broad video priors to jointly predict future videos and actions, offering a potential source of supervision for adapting to new tasks. However, generated videos may fail to depict task completion, and even visually successful videos may be paired with inconsistent actions that lead to execution failure. We propose EVO-WAM, a frame...

---

### 26. Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors

**Authors:** Christopher Kolios, Ishaan Mehta, Sasa Janjic, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38054v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38054v1)

**Summary:** We present Pow3R-SLAM, a real-time RGB-D simultaneous localization and mapping (SLAM) system that uses Pow3R for tracking and mapping. Inspired by MASt3R-SLAM, a recent work on monocular SLAM using two-view 3D reconstruction priors, we extend the work to incorporate depth as a prior on the network's prediction, rather than as geometry to fuse. Where traditional RGB-D SLAM systems struggle with sparsity in the depth images, Pow3R utilizes the available depth to give a better-conditioned pointmap,...

---

### 27. doPlan: A Variable-Horizon Dataset for Multi-Stage Language-Conditioned Planning in Autonomous Driving

**Authors:** Parthib Roy, Yash Tandon, Marcus Blennemann, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38028v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38028v1)

**Summary:** Autonomous vehicles interacting with passengers through natural language must reason beyond immediate commands. Passenger intent may span multiple stages of behavior, depend on future events, refer to surrounding agents or landmarks, and remain relevant as driving conditions evolve. Existing language-enabled driving datasets largely focus on short, localized interactions, leaving these longer-horizon forms of passenger intent comparatively underexplored. We introduce doPlan, to our knowledge the...

---

### 28. Beyond Lip Sync: Reference-Grounded Oral Refinement for Audio-Driven Portrait Animation

**Authors:** Bangxun Tang

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38019v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38019v1)

**Summary:** We present RGOR (Reference-Grounded Oral Refinement), an audio-driven lip-sync framework that renders the mouth of the specific person being dubbed rather than a generic one. Existing lip-sync systems follow the audio closely and keep the face recognizable, yet the mouth they render is an average mouth: the shape and texture of the lips, the arrangement of the teeth, and how much of them shows as the mouth opens are not that person's. The problem persists because nothing in current training or e...

---

### 29. Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38016v1)

**Summary:** Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is...

---

### 30. From Unity Simulation to Diffusion-Based Augmentation: Quantifying Dataset Balance for Robust Object Detection

**Authors:** Mohamed Benkedadra, Aissa Saoudi, Maxime Gloesener, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38010v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38010v1)

**Summary:** Modern computer vision models achieve high accuracy when trained on large-scale annotated datasets. In critical domains such as construction safety monitoring, data collection is costly, hazardous, and ethically constrained. This paper presents a systematic study comparing two complementary data generation paradigms, (1) Unity Simulation-based rendering and (2) Controllable Diffusion-based generation (CIA), for object detection under real data-scarce conditions. A unified experimental framework ...

---

### 31. HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents

**Authors:** Tongbo Chen, Junbo Niu, Zhengxi Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38008v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38008v1)

**Summary:** Computer use agents (CUAs) have demonstrated strong capabilities in completing digital tasks. However, existing CUAs either rely solely on graphical user interface (GUI) interactions, which are often inefficient and error prone, or augment GUI interactions with application specific APIs or tools, which require substantial engineering effort and are difficult to scale across applications. We argue that the next generation of CUAs should combine GUI interactions with the command line interface (CL...

---

### 32. ORMA: Optimization-based Monocular 4D Reconstruction of Articulated Animals

**Authors:** Xuyi Hu, Francesco Palandra, Shangzhe Wu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37986v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37986v1)

**Summary:** Recovering articulated 4D representations of animals from monocular videos remains challenging due to the large diversity of quadruped morphologies and lack of animal 4D supervision data. Existing learning-based reconstruction methods operate on individual images and rely on synthetic or model-fitted 3D supervision, which inherits the constraints of strong parametric priors and limits generalization to out-of-distribution species. When applied to out-of-distribution animals, they often recover a...

---

### 33. $S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient

**Authors:** Hongbo Ma, Sansheng Cao, Jiajun Fan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37976v1)

**Summary:** LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly...

---

### 34. PhysWAM: Physically Consistent World Action Model for Autonomous Driving

**Authors:** Dhruv Parikh, Fengcheng Yu, Quankai Gao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37970v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37970v1)

**Summary:** World-action models (WAMs) jointly predict how a scene will evolve and how an agent should act, however joint generation alone does not necessarily impose a shared geometric constraint on these predictions. We present PhysWAM, a unified world-action model for autonomous driving that co-denoises multiview video, metric depth, and ego motion within a single flow-matching transformer. To ground world and action generation in measured scene geometry, we introduce Coupled Point Projection (CPP) that ...

---

### 35. SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video

**Authors:** Haozhe Liu, Tian Ye, Shuchen Xue, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37969v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37969v1)

**Summary:** High-resolution video generation is expensive, as its cost grows rapidly with the number of spatiotemporal tokens. A practical alternative first generates a lower-resolution video and then applies a refiner, but conventional multi-step refinement introduces a second sampling bottleneck. We present SoL-Refiner, a one-step video refiner that transforms low-resolution model outputs into 4K videos with a single denoising step. Our three-stage recipe combines high-resolution continual training, reinf...

---

### 36. Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

**Authors:** Bingjun Luo, Jialin Guo, Siqi Li

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37950v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37950v1)

**Summary:** Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video understanding agent uses its own language model to revise its harness. Through active vid...

---

### 37. Does Local Video Understanding Transfer Across Encounters? The EgoGears Benchmark

**Authors:** Yuedong Tan, Lei Qi, Yu Liu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37938v1)

**Summary:** Embodied systems must make knowledge acquired during one encounter usable in another despite changes in viewpoint, motion, and illumination. Yet aggregate cross-video accuracy conflates failures of local perception with failures to preserve observation identity, establish correspondence, and compose evidence, obscuring whether local video understanding actually transfers. We introduce EgoGears, a complementary single- and multi-video benchmark designed to diagnose this transition. It contains 56...

---

### 38. Look Closer: Patch-wise Supervision for AI-Generated Image Detection

**Authors:** Zhida Zhang, Tao Wu, Siyu Liu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37937v1)

**Summary:** How much of an image does a detector need to see? Small RGB regions can retain useful evidence of image synthesis even when they reveal little of the full scene. Motivated by single-patch detection, we study patch-wise supervision: a shared backbone classifies explicit crops, each crop receives its own loss, and patch probabilities are averaged only at inference. The procedure requires neither handcrafted residual filtering nor a learned image-level fusion module. Experiments span single-patch s...

---

### 39. Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation

**Authors:** Chenjian Gao, Zhihao Hu, Jianqi Ma, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37925v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37925v1)

**Summary:** Autoregressive (AR) video diffusion enables low-latency, streamable video generation, but prediction errors often accumulate over long rollouts. Training the generator on its own rollouts exposes it to these imperfect histories. However, existing video-level distribution matching distillation (DMD) scores the whole rollout jointly. Because a chunk is evaluated together with its past and future, its correction can favor matching artifacts in the surrounding context merely to preserve temporal con...

---

### 40. EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory

**Authors:** Ziyun Zeng, Hang Hua, Shaden Alshammari, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37923v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37923v1)

**Summary:** Agents can learn from past executions, but enabling different agents to reuse and build on one another's experience remains challenging. We introduce EpiCon, a shared multimodal memory framework for agent collective learning without updating host model parameters. EpiCon links question-level memory evolution to a persistent experience bank through two independently trained 2B models: a memory controller and a tree self-organizer. The controller jointly refines textual guidance and visual evidenc...

---

### 41. SYNCR: Diagnosing and Learning Cross-Video Reasoning from Simulation

**Authors:** Sara Ghazanfari, Siddharth Garg, Prashanth Krishnamurthy, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37918v1)

**Summary:** Reasoning across videos requires aligning events, matching identities, comparing motion, and integrating partial observations. Evaluating these capabilities and testing how to improve them requires both reliable labels and targeted supervision. We introduce SYNCR, a simulator-grounded framework that connects these two needs through shared task generators. Built on Habitat, Kubric, and CLEVRER, SYNCR derives answers from environment state and provides 4,000 evaluation questions and 15,960 trainin...

---

### 42. Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics

**Authors:** Abhishek Pillai, Ekta Prashnani, Joohwan Kim, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37907v1)

**Summary:** Video games offer scalable environments for studying perception and control in embodied agents.Abundant online gameplay videos could supply demonstrations, but they rarely include player inputs for training. Inverse Dynamics Models (IDMs) have thus been proposed to infer inputs from frames. Large (up to 1B parameters) IDMs trained on $\sim$1K-2K gameplay hours demonstrate feasibility and cross-environment generalization at this scale, but researchers do not clarify what the key components are to...

---

### 43. ReCAP: Retrieval-Guided Capability Reuse for Multimodal Continual Instruction Tuning

**Authors:** Tao Hu, Zhinuo Zhou, Xialiang Tong, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37889v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37889v1)

**Summary:** Multimodal continual instruction tuning (MCIT) aims to enable multimodal large language models to acquire new capabilities from sequential tasks while preserving previously learned knowledge. Existing methods primarily mitigate catastrophic forgetting by constraining parameter updates or separating task-specific adaptations. However, continual adaptation can also benefit from external knowledge that provides domain-specific information and reusable reasoning patterns for solving diverse instruct...

---

### 44. Visual Branch is What You Need for CLIP-based Class-Incremental Learning

**Authors:** Tao Hu, Zhen-Hao Xie, Jingcai Guo, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37888v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37888v1)

**Summary:** Class-Incremental Learning (CIL) requires models to recognize new classes over time without forgetting previously learned ones. With the rise of vision-language pre-training, CLIP has become a strong foundation for CIL. A common design in CLIP-based CIL is to construct textual classifier weights by encoding class-name templates with the CLIP text encoder, and then classify visual features by image-text cosine similarity. This design is appealing: since CLIP aligns images and text in a shared emb...

---

### 45. EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior

**Authors:** Jiaqi Huang, Shidong Wang, Tong Xin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37874v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37874v1)

**Summary:** Dynamic endoscopic reconstruction is fundamental to robotic surgery and computer-assisted interventions. While 3D Gaussian Splatting (3DGS) realises real-time rendering, its application to deformable intraoperative environments remains constrained by spurious geometry and varying illuminations. To address these limitations, we introduce EndoPrior-GS, a novel pipeline that explicitly couples frame-extracted vision heuristics and estimated depth maps. EndoPrior-GS derives a joint texture prior fro...

---

### 46. Learning from synthetic photorealistic raindrop for single image raindrop removal

**Authors:** Zhixiang Hao, Shaodi You, Yu Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37870v1)

**Summary:** Raindrops adhered to camera lens or windshield are inevitable in rainy scenes and can become an issue for many computer vision systems such as autonomous driving. Because raindrop appearance is affected by too many parameters, therefore it is unlikely to find an effective model based solution. Learning based methods are also problematic, because traditional learning method cannot properly model the complex appearance. Whereas deep learning method lacks sufficiently large and realistic training d...

---

### 47. It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them

**Authors:** Nagham Omar, Mahmoud Jabarin, Kinan Ibraheem, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37863v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37863v1)

**Summary:** Vision-language models (VLMs) are increasingly used in place of human annotators, making it important that substitutability tests reflect the model rather than incidental evaluation conditions. We introduce MIST, the Misleading-Image Stress Test: 200 English sentences, each built around a phrase readable either figuratively or literally and shown with an aligned image depicting its reading, a misleading image depicting the opposite, or no image at all. The guidelines require the label to be deci...

---

### 48. HandAnthro: Automated Hand Anthropometry from a Single Image

**Authors:** Fan Zhou, Shuairan Chen, Mengying Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37855v1)

**Summary:** Hand anthropometry supports protective-glove design, but existing measurement methods often require trained operators, specialized hardware, or manual landmarking. We present HandAnthro, which estimates 44 projected hand dimensions from a smartphone photograph of a palm-up hand on US letter-size paper. The pipeline reconstructs wrist-occluded paper boundaries for rectification, whitens non-hand pixels, and refines 41 anthropometry-specific landmarks from a fine-tuned You Only Look Once (YOLO) po...

---

### 49. FlowMap-OPD: Rollout--Kernel Separation for On-Policy Distillation of Few-Step Flow-Map Generators

**Authors:** Zhiqi Li, Bo Zhu

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37851v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37851v1)

**Summary:** Few-step flow-map generators, including MeanFlow and consistency models, enable efficient sampling through long-range transport, yet their on-policy distillation remains underexplored. We introduce FlowMap-OPD, an on-policy distillation framework that separates student-state acquisition from teacher--student distribution comparison. A formulation based on state marginals establishes this separation, while flow--velocity consistency connects local supervision to the deployed long-range map. Withi...

---

### 50. RelayVSR: Large-Small Model Collaboration for Efficient Real-World Video Super-Resolution

**Authors:** Xijun Wang, Xin Li, Zirui Lang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37850v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37850v1)

**Summary:** Large generative models can recover realistic detail in real-world video super-resolution (VSR), but processing an entire video with them is computationally expensive. In this work, we present RelayVSR, a streaming VSR framework built on the Sparse Generative Relay mechanism. A large generative model generates reference latents for sparse keyframes, while a lightweight VSR network uses these references and low-resolution video to super-resolve every frame. The lightweight VSR network, implemente...

---

## cs.LG

**50 papers**

### 1. Skill-Space Shooting for Autonomous Robot Policy Improvement

**Authors:** Zihang Rui, Renhao Wang, Haoxu Huang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38178v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38178v1)

**Summary:** Robots deployed in the physical world must be able to improve beyond their initial training as they encounter new situations and failures. For this improvement to scale across tasks, it must make effective use of experience without requiring human demonstration of each correction. Recent agentic systems offer a way to reduce this reliance on human effort by using foundation models to autonomously compose learned behaviors to complete tasks. Yet completing tasks this way does not itself teach a t...

---

### 2. Breakdown of Local Denoising as Semantic Speciation

**Authors:** Guangkuo Liu, Mert Okyay, Yifan F. Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38176v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38176v1)

**Summary:** The dynamics of generative models exhibit two apparently distinct temporal windows: a speciation window, in which a sample commits to a semantic class, and a nonlocality window, in which local context windows become insufficient for generation. Motivated by evidence of their near-concurrence in a variety of frontier models, we investigate their relationship through the spatial distribution of semantic information. Under a "common cause" hypothesis, we prove that the nonlocality window must lie i...

---

### 3. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

**Authors:** Bingchen Yao, Haobo Xu, Haokun Lin, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38169v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38169v1)

**Summary:** Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding st...

---

### 4. LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization

**Authors:** Yi Pan, Haocheng Xi, Kan Zhu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38166v1)

**Summary:** Recent LLMs increasingly adopt hybrid designs that replace standard attention with linear attention, such as Gated DeltaNet (GDN) and Kimi Delta Attention (KDA). Although they compress the context into a fixed-size recurrent state and substantially reduce the cost of long-context processing, repeatedly reading and updating that state remains a major inference bottleneck. Quantization offers a natural way to reduce this cost, but can significantly degrade model quality, due to the accumulation of...

---

### 5. Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data

**Authors:** Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38165v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38165v1)

**Summary:** The landscape of satellite imagery time series datasets and boundary-pushing architectures for cropland segmentation has never been richer. However, in this gold rush, important truths are being missed on both fronts, as a drive for the most novel concepts or the largest datasets pushes finer details to the side. In this paper, we present our hybrid transformer-convolutional model, Cropland Parallel Attention and Refinement Network for Segmentation (PAtteRNS), the first model to use self-attenti...

---

### 6. A Spectral Theory of Distortion in LLM Graph Reconstruction: Sharp Bounds and Empirical Characterization

**Authors:** Jianru Shen

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38161v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38161v1)

**Summary:** Evaluations of graph reconstruction by language models typically report a single aggregate distance between the original and the reconstructed graph. We prove that for the Wasserstein distance between Laplacian spectra such a summary is bracketed by two edge counts, the net change in edge number from below and the symmetric difference from above, each scaled by $2/n$ where $n$ is the number of vertices. The bracket is sharp: its two ends coincide exactly when the reconstruction only adds edges o...

---

### 7. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies

**Authors:** Hui Ren, Lei Fan, Henry Pao, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38155v1)

**Summary:** Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Enti...

---

### 8. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

**Authors:** Cheng Qian, Kunlun Zhu, Beibin Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38143v1)

**Summary:** Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the f...

---

### 9. AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation

**Authors:** Rishabh Agrawal, Hejie Cui, Shasha Li, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38142v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38142v1)

**Summary:** A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice ...

---

### 10. Multi-Agent Flow Matching with Decoupled Generative Guidance

**Authors:** Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38133v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38133v1)

**Summary:** Generative modeling is widely used for producing diverse objects from complex, multimodal distributions. However, its expressivity does not, in general, come with formal guarantees that the generated objects satisfy hard constraints or requirements. In multi-agent generation, this problem becomes more challenging because a hard requirement can depend on multiple agents, while each agent may need to determine its own guidance input without relying on the simultaneously computed guidance inputs of...

---

### 11. Achieving an $O(1/N)$ Optimality Gap in Average-Reward Weakly-Coupled MDPs

**Authors:** Yige Hong, Xiangcheng Zhang, Qiaomin Xie, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38132v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38132v1)

**Summary:** We study average-reward weakly-coupled Markov decision processes (WCMDPs), where a WCMDP consists of $N$ smaller MDPs, called arms, that share multiple per-step budget constraints. We consider the setting where the arms have identical model parameters, multiple actions, and state- and action-dependent costs. For restless bandits (RBs), a well-studied special case of WCMDPs, prior work has developed policies that achieve an $O(1/\sqrt{N})$ optimality gap under general conditions, and has further ...

---

### 12. WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms

**Authors:** Jiale Chen, Vage Egiazarian, Eldar Kurtić, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38121v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38121v1)

**Summary:** KV cache memory and bandwidth costs grow with context length and batch size, which limits efficient long-context inference. To address this bottleneck, we introduce WUSH-KV for low-bit KV-cache quantization. It adapts WUSH, which constructs a data-aware transform from the second-order statistics of both factors in a matrix product to reduce quantization error. WUSH-KV uses calibration data to construct separate key and value transforms, with the value transform folded into the model weights and ...

---

### 13. ReCIRC: Rectified Conformal Risk Control

**Authors:** Bruno Marcondes e Resende, Helton Graziadei, Thiago Rodrigo Ramos, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38112v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38112v1)

**Summary:** Many applications of black-box predictive models require controlling task-relevant error rates, such as missed lesion pixels in segmentation or missed labels in multilabel classification. Conformal risk control (CRC; Angelopoulos et al., arXiv:2208.02814) gives distribution-free guarantees for such losses, but it calibrates a single threshold shared by all inputs. Because conditional risk varies with the input, this marginal guarantee often overprotects easy cases and underprotects hard ones. We...

---

### 14. How Local Mixing Encodes Relative Position in Global NoPE Attention

**Authors:** Cutter Dawes, Nick Alonso, Tom Figliolia, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38109v1)

**Summary:** The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in...

---

### 15. Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution

**Authors:** Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38108v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38108v1)

**Summary:** Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: selecting an appropriate plan for the task and executing it faithfully. Existing planner--executor systems can fail at either stage, while final task success alone cannot distinguish selection from execution failures. We therefore study the Plan Declaration--Execution Gap and introduce Planning-as-Rou...

---

### 16. Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling

**Authors:** Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38104v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38104v1)

**Summary:** Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified under the base model without parameter updates or external rewards, avoiding the costly optimization and jagged generalization of RL. However, this approach faces a fundamental exploration--exploitation trade-off, as % strong sharpening restricts exploration, trapping samplers in plausible but inco...

---

### 17. Tail-Influence Sampling for CVaR Policy Evaluation

**Authors:** Pauline Bourigault, Xiaotong Ji, Matthieu Zimmer, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38096v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38096v1)

**Summary:** Policies with similar mean returns can differ sharply in rare failures, yet estimating lower-tail conditional value-at-risk (CVaR) accurately can require many costly rollouts. When different conditional components of a stochastic workflow can be queried separately, we ask how to allocate a fixed evaluation budget to estimate a fixed policy's CVaR most accurately. We derive a tail influence for each queryable conditional law that aggregates how its uncertainty affects CVaR across every Bellman re...

---

### 18. Probe-Space Preconditioning for Fast and Stable Zero-Order Training

**Authors:** Francois Chaubard, Mykel J. Kochenderfer, Chris Ré

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38095v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38095v1)

**Summary:** Backpropagation (BP) dominates deep learning but imposes a massive memory tax. For example, training OPT-30B with Adam requires $\approx$ 600GB of GPU memory (assuming batch size 8 and sequence length 2048). Alternatively, zero-order optimization (ZOO) trains in inference-mode (requiring only $\approx$ 60GB for the same model): no stored activations, no gradients, and no optimizer states. However, ZOO convergence has lagged behind BP. In this work, we evaluate two methods to close this gap. Firs...

---

### 19. Dimensionally consistent surrogate modelling through dimensional analysis and harmonic expansions

**Authors:** Ernest Tarrus, Hector Gisbert

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38094v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38094v1)

**Summary:** Dimensional homogeneity is a fundamental constraint on physically meaningful models, requiring invariance under changes of units. We present a data-driven method for constructing surrogate models that satisfy this constraint at the level of the hypothesis class. Starting from a dimension matrix of measured variables, the method derives Buckingham $Π$-groups, constructs admissible dimensional prefactors, and approximates the remaining dimensionless dependence using truncated harmonic expansions o...

---

### 20. Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging

**Authors:** Sanjali Yadav, Bahar Asgari

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38090v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38090v1)

**Summary:** Mixture-of-Experts (MoE) models are a compelling architecture for scaling model capacity, making them especially attractive for deployment on resource-constrained, single-GPU systems. However, this benefit is difficult to realize because expert parameters dominate memory, and token-level routing is dynamic, unpredictable, and skewed. Prior work using offloading and caching remains fundamentally reactive, as systems wait for router outputs before moving experts, leading to inefficient cache utili...

---

### 21. Neural topology optimization of ship structures under propulsion machinery vibrations

**Authors:** Shengyu Yan, Muhammad Muztahidul Hakim Zareer, Jasmin Jelovica

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38089v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38089v1)

**Summary:** Ship structural vibrations contribute to noise, fatigue, and equipment damage, while dynamic-compliance topology optimization can produce pathological designs near resonance. This study extends neural-reparameterized topology optimization using a convolutional Kolmogorov-Arnold network (KATO) to forced-vibration design with active input power (AIP) as the objective. Applications include a 100 Hz engine-supporting deck panel and an 18 Hz thruster foundation frame. Helmholtz PDE filtering and Heav...

---

### 22. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

### 23. Optimal Quantum-Classical Separations for Exact Learning

**Authors:** Srinivasan Arunachalam, Amin Shiraz Gilani, Nikhil S. Mande

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38073v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38073v1)

**Summary:** We study exact learning with membership queries for concept classes $\mathcal C\subseteq\{0,1\}^N$, focusing on the relationships among their deterministic, randomized, and quantum query complexities, denoted $\mathsf{D}(\mathcal C)$, $\mathsf{R}(\mathcal C)$, and $\mathsf{Q}(\mathcal C)$, respectively. The two canonical quantum speedups in this model are witnessed by Grover search and Bernstein-Vazirani, leading to the longstanding conjecture $$ \mathsf{R}(\mathcal C)=O(\mathsf{Q}(\mathcal C)^2...

---

### 24. A foundation model for energy and radiation systems built on heterogeneous scientific interfaces

**Authors:** Samrendra Roy, Tapas Tripura, Yoon Pyo Lee, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38067v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38067v1)

**Summary:** Scientific foundation models are commonly evaluated after heterogeneous physical problems have already been translated into a compatible gridded, tokenized or symbolic representation. This leaves the scientific interface outside both the pretrained model and the audit of what is actually reused. We study the complementary setting in which boundary histories, sparse monitor records and loading histories retain their native inference classes and their outputs remain on Cartesian, latitude-longitud...

---

### 25. Alpha Diffusion Language Models: Factorization Alone Is Not the Problem

**Authors:** Nikita Gushchin, Dmitry Baranchuk, Alexander Korotin

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38066v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38066v1)

**Summary:** Discrete diffusion language models can generate multiple tokens in parallel, but reducing the number of denoising steps can lead to inconsistent predictions. Standard cross-entropy training fits conditional token marginals, whereas parallel generation requires consistent joint predictions. We introduce Alpha Diffusion Language Models (AlphaDLM), trained with a sequence-level alpha loss that recovers cross-entropy in the limit of vanishing alpha and has a joint-mode optimum at alpha one. Our anal...

---

### 26. Jaxolotl: A Unified High-Performance Benchmark Suite for LTL-Based Multi-Task RL

**Authors:** Mathias Jackermeier, Jacques Cloete, Alessandro Abate

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38065v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38065v1)

**Summary:** Training agents to follow arbitrary instructions is an important goal of multi-task reinforcement learning (RL). Linear temporal logic (LTL) provides a precise and structured formalism for specifying instructions to agents, and has been successfully adopted for training generalist multi-task policies. However, differences in implementations, task distributions, and evaluation protocols make existing methods difficult to compare, while high computational costs limit the scale and statistical reli...

---

### 27. Latent Inference-Time Guidance of Time Series Foundation Models

**Authors:** Chloé Hashimoto-Cullen, Amaury Durand, Laurent Bozzi, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38058v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38058v1)

**Summary:** Time Series Foundation Models (TSFMs) currently provide state-of-the-art results in forecasting tasks. They are available out-of-the-box and rely on in-context learning to make their predictions, which makes the quality of their performance highly sensitive to the user-selected lookback, covariates, horizon and training data distributions. In practise, the quality of the forecasts are variable but complementary, which highlights the need for a principled ensembling approach, rather than selectin...

---

### 28. Improving Function Space Flow Matching with Kernel Optimal Transport

**Authors:** Fred Xu, Thomas Markovich, Barbora Barancikova, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38049v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38049v1)

**Summary:** Generative models for function-valued data, such as time series and solutions of partial differential equations, must learn distributions over infinite-dimensional spaces. Functional Flow Matching (FFM) extends Flow Matching to this setting, learning a velocity field whose flow transports a Gaussian prior to the data distribution, but it inherits the independent endpoint pairing of standard Flow Matching: in each batch, prior and data samples are matched arbitrarily, so the conditional bridge mu...

---

### 29. The finite-horizon five-expert prediction problem

**Authors:** Jeff Calder, Nadejda Drenska

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38035v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38035v1)

**Summary:** We give an explicit solution to the five expert prediction with expert advice partial differential equation (PDE) in the finite-time horizon setting. The solution formula establishes that the adversary's rank strategy $(1,0,1,0,0)$ is globally optimal, and the COMB strategy $(1,0,1,0,1)$ is optimal exactly on the set where $x_1=x_2$ and $x_3=x_4$. The formula is derived from the solution of the geometric-stopping problem given in our companion paper through the transform principle of Bayraktar, ...

---

### 30. doPlan: A Variable-Horizon Dataset for Multi-Stage Language-Conditioned Planning in Autonomous Driving

**Authors:** Parthib Roy, Yash Tandon, Marcus Blennemann, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38028v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38028v1)

**Summary:** Autonomous vehicles interacting with passengers through natural language must reason beyond immediate commands. Passenger intent may span multiple stages of behavior, depend on future events, refer to surrounding agents or landmarks, and remain relevant as driving conditions evolve. Existing language-enabled driving datasets largely focus on short, localized interactions, leaving these longer-horizon forms of passenger intent comparatively underexplored. We introduce doPlan, to our knowledge the...

---

### 31. Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large Language Models

**Authors:** Zhenyu Wang, Tianze Wang, Linjun Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38025v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38025v1)

**Summary:** On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher. Vanilla OPD treats all teacher signals equally, assuming that the teacher's supervision is equally important for every token. However, teacher signals at different tokens may have very different effects on the student's performance: some correct important reasoning errors, while others have little effect on the final answer. Motivated by this observation, we ...

---

### 32. Prompts Live on an Arc: Gaussian Curricula in Fisher--Rao Coordinates for Rollout-Efficient GRPO

**Authors:** Mei Okonkwo, Pixel Nomand, Julian Berg, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38018v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38018v1)

**Summary:** Group relative policy optimization (GRPO) learns only from prompts whose sampled responses disagree: a group that is entirely correct or entirely incorrect has zero reward variance, contributes no gradient, and still consumes its rollouts. Prompt-selection methods reduce this waste by steering sampling toward intermediate pass rates, but they choose the target, its width, and the uncertainty model heuristically, in raw pass-rate or logit coordinates. We show that GRPO comes with a natural coordi...

---

### 33. When do data mixtures improve scaling laws? Insights from high-dimensional regression

**Authors:** Diyuan Wu, Lehan Chen, Theodor Misiakiewicz, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38011v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38011v1)

**Summary:** Modern machine learning systems are trained on mixtures of data from different domains, and choosing the right mixture can substantially improve downstream performance. Despite an extensive literature on data mixing and reweighting, existing work is largely empirical and it remains unclear when auxiliary data genuinely improves scaling laws rather than merely providing more samples. To gain insight into this question, we study a high-dimensional mixed-data regression model with a shared regressi...

---

### 34. No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection

**Authors:** Jiaheng Guo, Haochen Zhang, Yu-Chao Huang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38004v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38004v1)

**Summary:** Time series anomaly detection (TSAD) plays a crucial role in healthcare, finance, industrial monitoring, and other sectors. Within and between these settings, anomalies span vastly different temporal scales, from sub-second point spikes to multi-hour drift patterns. However, most existing TSAD methods commit to a single temporal granularity, and multi-scale designs either analyze different scales in isolation or are constrained to a predefined coarse-to-fine hierarchy, both failing to sufficient...

---

### 35. Mutual Information Constrained Chernoff Bottleneck

**Authors:** Dier Tang, Guangyue Han

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37994v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37994v1)

**Summary:** The classical information bottleneck (IB) measures the relevance of a representation $U$ of $X$ to a target $Y$ by $I(U;Y)$, which does not directly characterize the error of downstream decisions. For a binary hypothesis $Y$ inferred from many separately encoded observations, the optimal error exponent is the Chernoff information between the two conditional distributions of $U$ given $Y$. We study the mutual information constrained Chernoff bottleneck, which seeks an encoder that maximizes this ...

---

### 36. TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models

**Authors:** Deqing Fu, Huangyuan Su, Rajat Sen, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37989v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37989v1)

**Summary:** Tabular foundation models achieve strong zero-shot accuracy on structured data by pretraining on synthetic tables, but they ignore the column names, task descriptions, and auxiliary files that carry dataset semantics. Meanwhile, self-evolving machine learning engineering (MLE) agents train models from scratch on each dataset, yet jointly searching over features, architectures, and hyperparameters is noisy and prone to overfitting. We introduce TabFM-Auto, which pairs a tabular foundation model, ...

---

### 37. $S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient

**Authors:** Hongbo Ma, Sansheng Cao, Jiajun Fan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37976v1)

**Summary:** LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly...

---

### 38. On Trajectory-Aware Training for Masked Diffusion Language Models

**Authors:** Manuel Madeira, Amitis Shidani, Alice Bizeul, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37974v1)

**Summary:** Masked diffusion models (MDMs) generate text by unmasking several tokens per step, but they are trained and sampled under different conditions. The model is trained on randomly masked sequences, whereas inference follows a trajectory shaped by the model's own predictions. Additionally, each step has no access to what the previous one computed. Recent methods narrow these limitations from separate angles, leaving open how these choices interact. We introduce PUMBA, a unified framework for traject...

---

### 39. Dagger: Decoupling-based Model Stealing Attack against Graph Neural Networks

**Authors:** Ying Song, Xiaowei Jia, Balaji Palanisamy

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37972v1)

**Summary:** As Graph Neural Networks (GNNs) are widely deployed as Machine Learning-as-a-Service (MLaaS) APIs, model stealing attacks have emerged as a critical security threat. By querying a victim model's black-box API, an adversary can construct a functionally equivalent surrogate model, compromising proprietary intellectual property and downstream security. Existing GNN stealing attacks, however, rely on overly permissive assumptions, such as soft-label outputs, large query budgets, full-graph query acc...

---

### 40. SelfSearch: Reward-Free Search for Self-Improving Agents

**Authors:** Jungwoo Yang, In Jin Kong, Yohan Jo

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37968v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37968v1)

**Summary:** Advances in the coding capabilities of LLM agents allow them to inspect and modify their own instructions, tools, and execution procedures. Existing approaches use this ability to search for improved agents through repeated downstream evaluation, which incurs substantial costs and ties the search to the evaluated tasks. We introduce \textbf{SelfSearch}, a reward-free search procedure in which agents modify themselves using records of previous self-improvement episodes. These records capture the ...

---

### 41. TabFM: A Zero-Shot Foundation Model for Tabular Data

**Authors:** Weihao Kong, Erez Louidor Ilan, Shuxin Nie, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37959v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37959v1)

**Summary:** Tabular machine learning typically relies on per-dataset workflows, fitting tree ensembles or running AutoML searches from scratch for every task. We present TabFM, a 400M-parameter tabular foundation model that formulates supervised tabular prediction as in-context learning. TabFM produces calibrated zero-shot predictions in a single forward pass without task-specific tuning. Trained entirely on synthetic tables generated from structural causal models, TabFM learns general tabular representatio...

---

### 42. Kolmogorov-Arnold Classifier Systems as Universal Approximators

**Authors:** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37958v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37958v1)

**Summary:** As the input dimension $n$ grows, rule-based machine learning, such as Learning Classifier Systems (LCSs), faces a fundamental scalability bottleneck for function approximation: both rule count and parameter count grow exponentially with $n$. Traditional LCSs partition the $n$-dimensional input space directly, requiring $\mathcal{O}(m^n)$ rules for adequate coverage, where $m$ is the per-variable resolution. This article breaks from this paradigm by reorganizing rules dimension-wise, guided by t...

---

### 43. Scene-Consistent Illumination Transfer for Inserted Advertising Graphics

**Authors:** Rameshwar Mishra, Bishshoy Das, A. V. Subramanyam, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37951v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37951v1)

**Summary:** Replacing a visible advertisement in a broadcast frame is geometrically straightforward but photometrically delicate. A pasted graphic can have the correct perspective and still appear detached when its brightness, shading, or shadow disagrees with the surface beneath it. This paper presents Ad-Relight, an inference-only procedure for transferring scene illumination to a supplied advertising graphic without collecting a banner-specific training set. The procedure first separates slowly varying s...

---

### 44. Identifiability Guarantees for Drivers and Dynamics of Delayed Physical Systems

**Authors:** Julien Boussard, Antoine Débouchage, Théo Saulus

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37944v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37944v1)

**Summary:** A wide range of methods have been proposed, including physics-informed neural networks, which are powerful but do not guarantee identifiability of the dynamics, symbolic regression, which requires a set of precomputed operations, and causal discovery, which is more principled but usually relies on strong assumptions that physical systems may violate. In this work, we develop a theory-grounded method and prove that under a set of permissive assumptions, the structural drivers and drift of stochas...

---

### 45. An Efficient Machine Learning Approach for Degradation Forecasting in AEM Water Electrolysis

**Authors:** Marco Veneriano, Ani Gjergji, Sebastiano Bellani, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37941v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37941v1)

**Summary:** This study provides a data-driven analysis of a novel dataset of single-cell Anion Exchange Membrane water electrolyzers (AEMWE), operated under constant current load across multiple heterogeneous experimental campaigns. We train and evaluate a range of machine learning models with different complexity, including linear baselines, LSTMs and CNNs, to perform medium-term forecasting of the cell voltage degradation curve. The models are assessed within a rigorous training and evaluation framework s...

---

### 46. Post-Anomaly Detection Inference for Deep SVDD

**Authors:** Cao Le Cong Thanh, Dang Quang Vinh, Vo Nguyen Le Duy

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37935v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37935v1)

**Summary:** Deep Support Vector Data Description (Deep SVDD) has become a prominent framework for unsupervised anomaly detection by learning latent representations that compactly characterize normal data around a center. Despite its empirical success, anomaly decisions produced by Deep SVDD are typically made solely based on anomaly scores without rigorous statistical guarantees, thereby limiting their reliability in safety-critical and high-stakes applications where false positives must be strictly control...

---

### 47. Learning When to Update: A Near-Optimal Timing Bandit Approach

**Authors:** Qiulin Lin, Junyan Su, Liyuan Wang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37932v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37932v1)

**Summary:** Systems operating in dynamic environments require timely updates to sustain performance. For resource-intensive systems such as machine learning models and digital twins, strategically timing updates is essential. Updating too frequently wastes resources, while updating too infrequently leads to costly performance degradation. The problem is particularly challenging when the system's degradation pattern is unknown a priori, as is common in new operating environments. We formalize this challenge ...

---

### 48. Learning What to Remember: Long-horizon Counterfactual Memory Optimization

**Authors:** Jiaming Tang, Mingyan Liu, Armin Sarabi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37930v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37930v1)

**Summary:** Persistent textual memory allows language models to carry information across long interactions, but learning what to remember is fundamentally a credit-assignment problem. A memory rewrite may only become useful many steps later, while much of the observed utility may be inherited from information already stored before the rewrite. We introduce Memory Gain Policy Optimization (MGPO), which isolates the incremental value of each memory rewrite by crediting it for its marginal contribution to curr...

---

### 49. Time-Anchored Diffusion Language Models: Latent-Space Caching for Fast Generation

**Authors:** Joel Anto Paul, Litu Rout, Aditya Akella, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37924v1)

**Summary:** Recent work on anchored diffusion language models improves denoising by shaping an intermediate latent space with supervised important-token targets. In this work, we introduce time-based (self-supervised) anchoring, which learns and reuses latent anchors without requiring such targets. Our key observation is that anchors encode persistent properties of the clean sequence, such as its semantic intent, global structure, or intermediate plan. Although their hidden representations become stale as t...

---

### 50. Pattern Formation in Transformers

**Authors:** Erkan Turan, Gaspard Abel, Maks Ovsjanikov

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37921v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37921v1)

**Summary:** What are the inductive biases of a Transformer architecture? Existing theory on how the forward pass shapes representations either considers whether Transformers escape from rank collapse or demonstrates that self-attention drives tokens toward cluster patterns. The latter view arises from an elegant dynamical systems perspective, but relies on simplified architectural assumptions, and does not explain the rich structures observed in practice. This leaves a major open question: when a full Trans...

---

## cs.NE

**50 papers**

### 1. Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38016v1)

**Summary:** Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is...

---

### 2. Kolmogorov-Arnold Classifier Systems as Universal Approximators

**Authors:** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37958v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37958v1)

**Summary:** As the input dimension $n$ grows, rule-based machine learning, such as Learning Classifier Systems (LCSs), faces a fundamental scalability bottleneck for function approximation: both rule count and parameter count grow exponentially with $n$. Traditional LCSs partition the $n$-dimensional input space directly, requiring $\mathcal{O}(m^n)$ rules for adequate coverage, where $m$ is the per-variable resolution. This article breaks from this paradigm by reorganizing rules dimension-wise, guided by t...

---

### 3. A neural network that maintains and retrieves memories based on context

**Authors:** Hayoung Song, JeongJun Park, Qihong Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37791v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37791v1)

**Summary:** Every day, people continuously infer situational context and adjust the way they understand and remember the world. Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited. Here, we train a recurrent neural network (RNN), augmented with an episodic memory buffer, to infer context using Bayesian inference as it continuously makes predictions of upcoming scenes while watching naturalis...

---

### 4. Hybrid Joint-Selective Optimization: Reduced-Space Levenberg-Marquardt Refinement of Low-Dimensional Parameters of Interest

**Authors:** Muhammad Luthfi Shahab, Gabriella Alfa Indahsari, Imam Mukhlash, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37308v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37308v1)

**Summary:** This paper introduces a hybrid joint-selective optimization (HJSO) framework for large-scale numerical problems in which a small subset of trainable quantities is of primary interest. We partition the full parameter vector into a high-dimensional remaining block and a low-dimensional block of parameters of interest (POIs), perform joint first-order optimization over the full parameter set, and then freeze the remaining variables while applying a reduced-space Levenberg-Marquardt (LM) refinement ...

---

### 5. Adaptive Rotation for iSOMA: Geometry, Benchmarking, and Noise Robustness in Variational Quantum Objectives

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37193v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37193v1)

**Summary:** We study whether the coordinate dependence of the improved Self-Organizing Migrating Algorithm (iSOMA) can be reduced while retaining its inexpensive leader-directed migration mechanism. We introduce iSOMA-AR, which learns a basis from successful migration displacements and selectively applies the standard perturbation mask in that basis. On the complete noiseless BBOB suite, iSOMA- AR significantly outperformed baseline iSOMA across matched conditions, with the largest gains on geometrically di...

---

### 6. Evolving Towards Better Codes: LLM-Guided Search for High-Distance Binary Linear Codes

**Authors:** Amal Seddas, Vladyslav Shashkov, Maryna Viazovska, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37056v1)

**Summary:** Evolutionary program search driven by large language models (LLMs) has produced record-breaking constructions for open problems in combinatorics and beyond. We apply this approach to the longstanding problem of improving the best-known bounds for binary linear codes. Building on the EvoTune evolutionary framework and the ShinkaEvolve codebase, we introduce LinCodeEvolve, which evolves code-construction programs against an exact minimum-distance evaluator. A strategy loop combines diversity-drive...

---

### 7. Multi-Depth Temporal Fusion for Feedforward, Locally Trained Spiking Neural Networks

**Authors:** Aidin Attar, Eleonora Cicciarella, Michele Rossi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37047v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37047v1)

**Summary:** We propose a new spiking neural network (SNN) design to process static images and event streams using time-to-first-spike (TTFS) latencies. Our key research question is which architectural choices best accommodate local and online learning in multi-layer convolutional SNNs. This question is addressed via an original framework combining residual-like connections with multi-depth feature aggregation and consensus. The full SNN pipeline features an early-vision front end, to convert raw visual data...

---

### 8. Where Does Randomness Matter in Neural Cellular Automata?

**Authors:** Fei Zuo, Jiaqi Shi, Yujing Liu

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36797v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36797v1)

**Summary:** Stochastic cell updates are often used throughout the life of a neural cellular automaton (NCA), from backpropagation through time to final rollout. This leaves two questions entangled: does update randomness help learn a useful rule, and must that randomness remain at execution? We separate training and evaluation update modes in controlled Growing NCA experiments, then vary the states shown during training. Under the standard constant-rate persist recipe, asynchronous training passes the short...

---

### 9. NeuroDyn-EEG: An Interpretable Pre-trained Model for EEG Based on Neural Dynamics

**Authors:** Yi Cui, Tong Zhao, Jiaxin Lei, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36773v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36773v1)

**Summary:** Clinical scalp electroencephalography (EEG) offers a noninvasive window into neural dynamics of neuropsychiatric disorders. However, discriminative deep models often lack anatomically indexed physiological interpretability. We propose NeuroDyn-EEG, a pretraining framework integrating generative priors from neural dynamics. It couples an extended Jansen-Rit neural mass model, leadfield-based source projection, and simulation-based parameter inversion. Trained on synthetic parameter-EEG pairs with...

---

### 10. Massively Parallel Reinforcement Learning with a Chaotic Reconfigurable Clockless Chip

**Authors:** Eric Oliveira-Gomes, Damien Rontani

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36347v1)

**Summary:** Hardware accelerators based on physical dynamical systems offer an attractive route toward energy-efficient reinforcement learning applications. However, their scalability is challenging because it requires many statistically independent entropy sources. Here, we introduce a quasi-analog decision-making architecture based on asynchronous Boolean networks (or lattices) implemented on a clockless reconfigurable chip. Each node in the network consists of a single logic element that acts as an auton...

---

### 11. HeurEvo: Agentic Evolution of Hybrid Solver-Augmented Heuristics for Time-Critical Mathematical Optimization

**Authors:** Feijie Wu, Hugo Barbalho, Konstantina Mellou, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36303v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36303v1)

**Summary:** Recent advances in agentic heuristic design use AI agents and execution feedback to automate algorithm discovery for challenging optimization problems. In many practical settings, high-quality solutions must be obtained under strict runtime constraints, motivating hybrid approaches that combine problem-specific heuristics with powerful mathematical programming solvers. However, existing approaches typically improve heuristic components within predefined procedures or tune solver configurations i...

---

### 12. CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

**Authors:** Mohammed Yusuf Mujawar, Shahram Rahimi, Noorbakhsh Amiri Golilarz

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35657v1)

**Summary:** Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior succeeded or failed. We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome. CMDO organizes these experiences across working, ep...

---

### 13. Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity

**Authors:** Zilan Cheng, Li-Lian Wang, Zhongjian Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35628v1)

**Summary:** We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks w...

---

### 14. EvE: An Alternate Optimizer to Adam

**Authors:** Shashank Raj, Kalyanmoy Deb

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35614v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35614v1)

**Summary:** Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutionary Explorer), a steady-state, population-of-four differential evolution (DE) optimizer with a targeted Adam fallback: each iteration proposes one candidate via DE, running a short burst of gradient de...

---

### 15. Deep Learning Methods in Neuroscience: From Modeling Molecular Mechanisms to Classifying States of Consciousness

**Authors:** Elena Benderskaya, Anastasiia Alifanova, Svetlana Batalova, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35372v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35372v1)

**Summary:** A critical analysis of contemporary approaches to the study of conscious states. The review focuses on methods of classification, clustering, modeling of brain states under anesthesia and identification of measurable neurobiological characteristics of brain function. A comparative analysis was conducted in the following three major areas: automatic detection of states of consciousness using neural networks based on EEG and fMRI data; modeling of the structural-functional dynamics of the brain un...

---

### 16. Graph neural networks for sampling-invariant embeddings of organized signal sets

**Authors:** Martin Bauw, Santiago Velasco-Forero, Jesus Angulo

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35934v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35934v1)

**Summary:** Sensor networks and radars can deliver signals as organized sets, e.g. ordered signals, signals describing range cells within a grid or signals perceived as graph nodes. Within such sets, individual signals may be characterized by distinct sampling parameters. This paper investigates organized signal sets neural network encoders. In the context of this work, the purpose of such encoders is to project heterogeneously sampled signal sets into an arbitrary fixed-size vectors space. This new represe...

---

### 17. Hidden Activations are not Enough I: Knowledge Matrices as Higher Representations

**Authors:** Marco Armenta

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34166v1)

**Summary:** We study the knowledge matrix of a trained feedforward network as a higher representation of its inputs. A network is a pair $(W,f)$, a thin representation $W$ of its quiver and an activation $f$; its function factorizes through the space of quiver representations, each input $x$ inducing a representation, and the knowledge matrix $M(x)\in\mathbb{R}^{C\times(d+1)}$ is the contraction of that representation to one matrix whose rows sum exactly to the logits. At one trained network we ask what det...

---

### 18. ADPTNet: Adaptive with Prescriptive Timescales Non-Linear SSM for Sequence Modelling

**Authors:** Matei-Ioan Stan, Oliver Rhodes

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34034v1)

**Summary:** A central aim of neuromorphic computing is to provide a viable alternative to highly energy-intensive Transformer-based AI. However, efficient alternatives struggle to capture the set of qualities that have secured the Transformer's status as the de facto standard in sequence modelling. Any realistic contender must be data-adaptive, able to capture long-range dependencies, and GPU-parallelisable, but also non-linearly recurrent to enable complex reasoning. Based on evidence suggesting the audito...

---

### 19. Neuron-Level Architecture Growth: A Controlled Evaluation for EEG Time-Series Decoding

**Authors:** Adam Mounir, Stella Douka, Arnault H. Caillet, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33880v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33880v1)

**Summary:** Convolutional EEG decoders are trained at a fixed width, usually set by their authors on other data. Growing methods add neurons during training where the loss could decrease the most, but whether they improve compared to a reference width is untested on EEG. Here, we grow three convolutional backbones on 12 motor-imagery datasets under three protocols and compare each with its reference model per subject. The growing ShallowFBCSPNet scores 2.9 points above its reference model with only half the...

---

### 20. Program-Verified Self-Evolution for Vision-Language Models

**Authors:** Ahmed Heakl, Sungik Choi, Moontae Lee, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33855v1)

**Summary:** Self-evolving vision-language models train on questions they generate from unlabeled images. Since these questions have no gold answers, prior methods label them by majority vote over sampled answers or by a model judge. In a human evaluation, we find that 24\% of majority-vote labels and 18\% of model-judge labels produced during self-evolution are wrong. To address this problem, we present Verifiable QA Generation for Self-Evolving Models (VQS), which changes how the model judges answers. Inst...

---

### 21. Raven: The Harness of Harnesses for Composable Agentic Intelligence

**Authors:** EverMind AI

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33439v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33439v1)

**Summary:** As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through ...

---

### 22. APEX: An Extensible Model for Agent-Assisted Production Scheduling

**Authors:** Felix J. Grumbach, Stefan Görlitz

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33430v1)

**Summary:** Production scheduling requires realistic models that reflect operational constraints and efficient methods that balance competing goals. Putting these methods into use also requires data integration, model adaptation and specialist expertise. We present APEX, an extensible production scheduling framework built around a general model and hybrid multiobjective search. Agent assistance supports both scheduling and model refinement: agents prepare data and explore scenarios in natural language, whil...

---

### 23. MTLiquid: Enabling Efficient Multi-Task Learning using Liquid Neural Networks for Lightweight Healthcare Monitoring Systems

**Authors:** Rachmad Vidya Wicaksana Putra, Fahad Abdul Rauf, Muhammad Shafique

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33232v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33232v1)

**Summary:** Continuous-time sensing and monitoring with timely and accurate decision-making are critical for many real-world applications. In healthcare monitoring systems, physiological signals are often available or sampled at irregular time intervals, hence requiring continuous-time processing to provide accurate prediction. Moreover, such systems often need to solve multiple detection/prediction tasks to provide a comprehensive patient review from different physiological aspects for more accurate decisi...

---

### 24. MorphAtt: A Neuromorphic Accelerator for Efficient Multi-Head Attention Processing in Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Amirhesam Jafari Rad, Muhammad Shafique

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33207v1)

**Summary:** Spiking Vision Transformers (SViTs) are developed as an energy-efficient alternative to conventional ViTs for computer vision tasks at the edge. However, huge parameter counts and complex multi-head self-attention (MHSA) operations make it challenging to achieve high energy efficiency in SViT inference, especially in tightly constrained applications. To maximize efficiency gains of SViT processing, we propose MorphAtt, a novel digital accelerator that expedites SViT inference through streamlined...

---

### 25. RIPE-MambaSpike: Resolution-Independent Spiking-State-Space Interfaces for Parameter-Efficient Event-Based Vision

**Authors:** Md Muhiminul Islam, Shoaib Ahmed Dipu, Sayeed Shafayet Chowdhury

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32537v1)

**Summary:** Spiking-Mamba hybrids reach strong accuracy on event-based vision, but existing designs often require tens of millions of parameters. Much of that cost comes from how the spiking front-end is connected to the state-space backbone rather than from the hybrid architecture itself. In a representative model, a single resolution-dependent projection accounts for 33.55M of 36.25M parameters. To that end, we introduce RIPE-MambaSpike (Resolution-Independent, Parameter-Efficient), which replaces that pr...

---

### 26. Analog-Friendly Predictive Coding without Activation Derivatives

**Authors:** Francesco Innocenti

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32350v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32350v1)

**Summary:** Predictive coding (PC) is a local, energy-based alternative to backpropagation (BP) whose iterative inference dynamics make it attractive for implementation on analog hardware. However, standard nonlinear PC requires evaluating the derivative of the activation function during both inference and learning, which can be difficult to realise physically. Here, we introduce \textit{activation-matched Bregman PC}, replacing standard squared-error energies with Bregman divergences matched to the activat...

---

### 27. All On-Board: Fully On-Chip Neuromorphic Q-Learning with Embedded CartPole Simulation

**Authors:** Steven C. Nesbit, Giovanni T. Michel, Gerd J. Kunde, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32317v1)

**Summary:** As AI models grow in size and usage, their energy demands increase dramatically, raising sustainability and economic concerns. Neuromorphic hardware, inspired by the energy efficiency of the brain, seeks to address this challenge by offering low-power, fast-processing alternatives to conventional computing. Such hardware is particularly well-suited to control systems deployed in resource-constrained environments, which are best trained via reinforcement learning (RL). This contribution presents ...

---

### 28. DS-VLA: A Dendritic-inspired Vision-Language-Action Model for Robust Action Control

**Authors:** Yaxing Lyu, Jingyi Li, Mingkun Xu, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32253v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32253v1)

**Summary:** Vision-language-action (VLA) models have achieved strong performance in language-conditioned manipulation, yet success under nominal evaluation does not necessarily translate into robust closed-loop behavior when executed actions are transiently corrupted. We introduce DS-VLA, a dendritic-inspired action architecture that incorporates dendritic spiking dynamics into VLA control to address this limitation. Specifically, to enable modularized feature processing and temporal information integration...

---

### 29. Distance-Residual Physics-Informed Neural Networks: A Deep Learning Framework for Differential and Partial Differential Inclusions

**Authors:** Maria Filipkovska, Juan José Marín, Isil Oner, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.32043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32043v1)

**Summary:** We introduce Distance-Residual Physics-Informed Neural Networks (DR-PINNs), a physics-informed learning framework for approximating solutions of ordinary and partial differential inclusions (DIs), governing laws in which a differential operator is constrained to lie in a set-valued map rather than equaling a prescribed function. The method replaces the classical pointwise PDE/ODE residual by the squared distance from the differential operator to the admissible set. This distance vanishes exactly...

---

### 30. A Voltage-controlled MTJ-CMOS Neuron Emulating Tunable Izhikevich-Inspired Dynamics

**Authors:** Kayode Oluwaseyi Adebunmi, Jordan Athas, Allison Fleming, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.32031v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32031v1)

**Summary:** Biological neurons exhibit diverse firing dynamics that enable adaptive and stimulus-dependent signalling, yet reproducing these dynamics in hardware has remained an enduring challenge. In this work, we present an Izhikevich- inspired reconfigurable neuron that co-designs voltage-controlled magnetic tunnel junction (V-MTJ) dynamics with CMOS circuitry. The proposed architecture combines V-MTJ excitability dynamics, enabled by a tunable energy landscape, with CMOS recovery dynamics to generate fi...

---

### 31. SNIP++: Fine-Grained Symbolic-Numerical Alignment for Symbolic Regression

**Authors:** Benjamin Léger, Shubham Gupta, Samy Mammeri, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31965v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31965v1)

**Summary:** Mathematical expressions and the numerical behavior they produce are two views of the same underlying function, and connecting them is central to scientific discovery. Symbolic Regression (SR) relies on this connection directly: it searches for an expression that reproduces a given behavior. Recent multi-modal models learn this connection by embedding symbolic expressions and their numerical behavior in a shared representation space. We show that this embedding space is only globally aligned: co...

---

### 32. Common-Mode Collapse and Recovery in Direct Feedback Alignment

**Authors:** Varun Reddy, Bernardo L. Sabatini, Houman Safaai

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31589v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31589v1)

**Summary:** Direct feedback alignment (DFA) trains hidden layers through fixed random projections of output error. With tanh hidden units and independent sigmoid outputs, plain stochastic gradient descent can stall near the loss of a constant predictor of class frequencies. We trace this stall to the error's common mode, the component shared across inputs. An exact mean-covariance decomposition separates a rank-one update formed by the mean teaching signal and mean presynaptic activity. Its leading componen...

---

### 33. Purin: A Biology-inspired Mechanism for Artificial Neural Networks

**Authors:** Zishu Liu, Chunbo Luo, Christos Grecos

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31235v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31235v1)

**Summary:** Artificial neural networks (ANNs) usually represent neural transmission with fixed trainable weights during a training batch, which omits short-term changes in synaptic efficacy. In addition, the discrete time-step simulation requires additional temporal processing that many conventional ANN architectures do not use. To overcome these challenges, we propose Purin, a biology-inspired and ANN-compatible mechanism, that introduces synaptic efficacy modulation into conventional convolutional neural ...

---

### 34. Modeling quantum neural network gradient with reinforcement learning

**Authors:** Nhan Trong Luu, Duong Trung Luu, Nam Ngoc Pham, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31066v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31066v1)

**Summary:** Training quantum neural networks (QNNs) on near-term hardware remains hampered by two compounding difficulties: the exponential vanishing of gradient variance known as the barren plateau, and the $\mathcal{O}(L \cdot 2^n)$ time and memory cost of differentiating through an $n$-qubit, $L$-layer circuit. We propose RLQ-Grad, a reinforcement-learning-based optimizer in which a classical policy $π_φ$ (a spectrally-normalized PPO agent) learns to propose parameter updates directly, conditioned on the...

---

### 35. Landscape Limits of Quantum-Inspired Evolutionary Optimization across 256 continuous functions

**Authors:** Rishi Govind, Ferdin Sagai Don Bosco, Kasturi Venkata Srikanth, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.30938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30938v1)

**Summary:** Quantum-inspired evolutionary optimization (QIEO) represents design variables as a set of qubits and searches a continuous, multi-dimensional landscape through rotation of the qubit's amplitude pair. Every generation rotates those amplitudes toward a single elite, which corresponds to that generation's best. The update is cheap, almost parameter-free, and well-suited for massive parallel implementation, which has encouraged its adoption in engineering, design, and planning applications. However,...

---

### 36. Structured Bayesian Modeling of Dynamic Receptive1 Fields in Salamander Retinal Ganglion Cells

**Authors:** Alokesh Manna

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.30731v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30731v1)

**Summary:** Neurons in the visual system are selective for specific spatial and temporal stimulus features, described by their \emph{receptive field}. Estimating one means a coefficient per pixel per time bin from few trials -- a high-dimensional problem requiring regularization. Sparse regularizers such as the LASSO handle the dimension but select pixels independently at each time point, with nothing to keep the region coherent in space or smooth in time; it can fragment or reorganize discontinuously even ...

---

### 37. Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30115v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30115v1)

**Summary:** Modern deep neural networks treat parameters as static floating-point matrices stored in physical memory, incurring Von Neumann memory bottlenecks and representation collapse. We formulate Orbital Error Dynamics (OED), an analytical framework wherein synaptic weights are not stored masses (O(W)), but transient topological resonances (O(1)) derived procedurally from the complex quadratic polynomial map z_{n+1} = z_n^2 + c. We introduce the Bent Sine Wave Hypothesis, demonstrating that non-equilib...

---

### 38. Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons

**Authors:** Ruiyu Jia, Zhuo-Cheng Xiao

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30102v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30102v1)

**Summary:** Most ANN-to-SNN conversion methods rely on a specific correspondence between the source activation and the spiking neuron dynamics. We propose a finite-state continuous-time Markov chain (CTMC) neuron framework whose stationary spike flux can approximate every continuous nonnegative monotone activation function on a compact interval. For a generalized CTMC family with affine input-dependent transitions, we prove uniform approximation to arbitrary accuracy over this function class and derive an e...

---

### 39. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v2) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v2)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 40. Boolean threshold functions, neuron capacity, and memory retrieval

**Authors:** Xinyuan Xie

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29756v1)

**Summary:** How much information can a single neuron remember? How many memories can neural networks retrieve without creating false memories? These questions are related to a basic question: how many Boolean threshold functions $f(x)=\operatorname{sgn}(a_0+\langle a,x\rangle)$, $x\in\{-1,1\}^n$, are there? In this paper, we show that the number $T_n$ of distinct Boolean threshold functions is \[ T_n=2\binom{2^n-1}{n}\bigl(1+O(n^{-99})\bigr). \] Equivalently, the capacity of a single threshold neuron is $n^...

---

### 41. On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation

**Authors:** Benedikt Hartl, Milton L. Montero, Marcello Barylli, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29755v1)

**Summary:** How phenotypic transformations are implemented by changes in underlying regulatory dynamics remains a central question in developmental biology. Inspired by D'Arcy Thompson's 1917 "On Growth and Form", we ask whether coherent large-scale transformations of morphology can be encoded as low-dimensional modulations of a self-organizing developmental system. We use neural cellular automata (NCAs) as bio-inspired models of distributed development, in which a shared local regulatory network grows targ...

---

### 42. Dynamical Diversity for Reservoir Computing in Reconfigurable Nanomechanics

**Authors:** Humayun Ahmed, Inês S. Garcia, Filipa C. Mota, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29532v3) | 📄 [PDF](https://arxiv.org/pdf/2609.29532v3)

**Summary:** Physical reservoir computing uses nonlinear dynamics and a trained linear readout to process information. Nanoelectromechanical (NEMS) resonators combine geometric Duffing nonlinearity with fading memory, but most electromechanical implementations use a single resonance mode. Here, we demonstrate reservoir computing with two interacting modes of a single NEMS resonator measured through one readout port. We introduce dynamical diversity through complementary modal drive settings: the same input s...

---

### 43. Online Task Adaptation via Self-Organisation

**Authors:** Krsto Proroković

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29281v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29281v1)

**Summary:** Neural networks are typically adapted by computing gradients and updating model parameters. We investigate whether task-specific adaptation can instead emerge from a meta-learned self-organising process that requires no gradients at adaptation time. We instantiate this idea with a Neural Cellular Automaton in which locally interacting recurrent cells maintain both a recurrent state and a fast associative memory. During meta-training, backpropagation is used to learn the recurrent dynamics togeth...

---

### 44. EvoTreeNAD: Genealogy-Guided Evolution for LLM-Driven Neural Architecture Discovery

**Authors:** Lishan Yu, Derek Jiu, Qizhen Lan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29016v1)

**Summary:** AI-driven scientific discovery accelerates research by autonomously developing solutions and designs. Large language model (LLM) agents support this process through iterative generation and evaluation. Yet these iterations alone do not ensure cumulative progress or establish which directions to pursue next. Costly evaluation further constrains the scope of exploration. Neural architecture discovery brings these challenges together, coupling open-ended design with resource-intensive experimentati...

---

### 45. Learning Holographic Reduced Representations with Clifford Variational Autoencoders

**Authors:** Mohamed Malek Abid, P. Michael Furlong

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28409v1)

**Summary:** Vector Symbolic Algebras project data structures into a hyperdimensional vector space through the application of their vector algebras to randomly generated atomic vector symbols and fractional power encodings of real-valued data. Embedding unstructured data remains an open question. We present \textit{Clifford-VAE}, a variational autoencoder that learns to project data onto a Clifford torus in arbitrary dimensions. Experiments using the MNIST, FashionMNIST, and CIFAR-10 datasets demonstrate tha...

---

### 46. Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games

**Authors:** Gijs van Cuyck, Patric Feldmeier, Jan Tretmans, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28130v1)

**Summary:** Automatically generating test inputs for games is challenging, as test generators must master the game to reach advanced program states while also ensuring robustness against the heavy program randomisation inherent to games. The test generator Neatest therefore optimises test suites consisting of neural networks that reach advanced program states and are robust to program randomisation, as they generate test inputs dynamically based on the current program state. Neatest is a white-box testing a...

---

### 47. Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond

**Authors:** Yiqian Yang, Yiqun Duan, Chenyu Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27650v2) | 📄 [PDF](https://arxiv.org/pdf/2609.27650v2)

**Summary:** Brain-to-language decoding translates neural activity associated with language production, internal speech and perception into linguistic or expressive outputs. It offers a route to restoring communication after speech loss and a means of studying how the brain represents language. Advances in neural recording and representation learning have expanded the field from constrained recognition and acoustic reconstruction to text generation, streaming personalised speech and facial animation. This su...

---

### 48. Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning

**Authors:** Mikhail Kiselev

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27459v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27459v1)

**Summary:** This paper presents a spiking neural network (SNN) designed to predict the sequence of the external world states starting from the current world state. This SNN does not create the world dynamics model - instead it incorporates the SNN trained to predict the next world state and provides all mechanisms necessary to make the chain of predicted world states. These mechanisms are entirely spiking - they are implemented as spiking neuron ensembles. The present article describes this neuronal structu...

---

### 49. An Unbounded Archive-based Transfer Strategy for Dynamic Multi-Objective Optimization with a Changing Number of Objectives

**Authors:** Zhiyun Xiao, Ke Shang, Yajun Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27430v1)

**Summary:** Dynamic multi-objective optimization with a variable number of objectives is difficult because objective-dimensional variations may significantly change the Pareto front and degrade algorithm adaptability. This paper proposes an unbounded archive-based transfer strategy (UATS), which maintains an unbounded archive of offspring solutions within each environment stage and extracts feasible nondominated solutions as transferable elites when objective changes occur. UATS is embedded into SPEA2SDE to...

---

### 50. Combining LLMs and Genetic Search for ARC-AGI-2

**Authors:** Val Dyachenko

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27242v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27242v1)

**Summary:** LLMs can generate programs for ARC-AGI-2 tasks, but the provided compute only allows a small number of attempts to generate, debug and validate solutions. Genetic algorithms can search and test many more programs, but random search rarely starts in a useful neighborhood of the solution space. We combine the two methods through a compact domain specific language (DSL). First, a quantized Qwen3.5-4B LLM generates an initial set of programs for each ARCAGI-2 task. Then, we use those programs to see...

---

## q-bio.NC

**50 papers**

### 1. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

### 2. Which Attention Heads are like the Human Head? Not the Ones that Compute

**Authors:** Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37991v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37991v1)

**Summary:** Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less d...

---

### 3. Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders

**Authors:** Giovanni Marraffini, Victoria Shevchenko, Carlo Alberto Barbano, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37642v1)

**Summary:** Self-supervised pretraining reshaped prediction in language and vision, and brain foundation models (BFMs) inherited its promise. Representations learned from large unlabelled corpora should capture individual functional dynamics and generalise across cohorts. However, kernel ridge regression (KRR) fitted on functional connectivity (FC) matrices still predicts individual phenotypes more accurately than any BFM we tested. In this paper, we show that KRR is weighted by the eigenvalues of the FC wh...

---

### 4. An adaptive fractional state links circuit mechanisms to cortical dynamics across the visual hierarchy

**Authors:** Brendan Harris, Pulin Gong

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37355v1)

**Summary:** Cortical circuits must respond flexibly to new inputs while integrating information about the past, yet the way in which neural activity reconciles these competing demands remains unclear. Combining Neuropixels recordings from six mouse visual areas with mechanistic circuit modeling, we identify a dynamical regime in which heavy-tailed superdiffusive fluctuations coexist with long-range temporal dependence and oscillations. We formalize this regime as the adaptive fractional (AF) state, using an...

---

### 5. Volcanite: Commodity-Hardware Segmentation Volume Visualization for Connectomics and Beyond

**Authors:** Max Piochowiak, Reiner Dolp, Julian Herold, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36898v1)

**Summary:** Modern imaging produces terabyte-scale segmentation volumes, assigning each voxel an object label. These categorical, boundary-sensitive and label-rich data underpin connectomics and other imaging-driven fields, yet their scale often forces interpretation through slices, approximate meshes or distributed workflows that obscure spatial context and voxel-level defects. Here we show that such volumes can be explored directly on commodity hardware with Volcanite, an open-source framework for dense-s...

---

### 6. From Neurons to Conversation: Speech Brain-Computer Interfaces

**Authors:** Moein Khajehnejad, Forough Habibollahi, Tommaso Boccato, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36736v1)

**Summary:** Speech brain-computer interfaces (BCIs) aim to restore communication by transforming neural activity related to speech, language, or communicative intent into external outputs such as text, synthesized voice, or avatar control. Recent advances in intracortical and electrocorticographic recording, deep sequence models, and language-model-assisted decoding have enabled rapid progress, including high-performance attempted-speech decoding and increasingly naturalistic speech synthesis. Yet these ach...

---

### 7. Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge

**Authors:** Zixing Jia, Yuhang Pan, Ni Ji

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36620v1)

**Summary:** Structural reasoning, the ability to recognize and make inferences over the relational structure between objects and concepts, is a hallmark of human cognition, yet prevailing methods often collapse relational topology into flat embeddings, cannot discover hidden structure and lack interpretability. We introduce Neural Structural Reasoner (NSR), a brain-inspired network that preserves relational structure directly in the connectivity and dynamics of coupled neuronal populations. NSR draws inspir...

---

### 8. Large-scale factor analysis shows machine intelligence is only partially interpretable

**Authors:** Faiz Ghifari Haznitrama, Afrizal Hasbi Azizy, Faeyza Rishad Ardi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36515v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36515v1)

**Summary:** A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like fluid intelligence in humans. This assumption is rarely tested directly, and prior attempts have done so only at a much smaller scale. We take a latent variable approach to intelligence in language models, similar to how psychometricians study psychological constructs. Performance in every specific problem set is influenced by a domain-specific and a...

---

### 9. Receptive-field-constrained stimulus optimization for human early and intermediate visual cortex

**Authors:** Junru Zhao, Hanfei Guo, Andrew Luo, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36391v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36391v1)

**Summary:** An ongoing challenge in sensory neuroscience is to characterize the feature dimensions encoded by cortical populations. Recent approaches probe feature selectivity in a data-driven way, by synthesizing a most-exciting-input (MEI) for a target neural population. While this approach has been successfully applied to human higher visual cortex using fMRI data, generating MEIs for early- and mid-level retinotopic visual areas requires additional modeling constraints due to small receptive field sizes...

---

### 10. Cross-attention encoding models reveal dynamic spatiotemporal routing across human higher visual cortex

**Authors:** Iishaan Inabathini, Margaret M. Henderson

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36366v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36366v1)

**Summary:** Understanding how the brain parses actions and events from time-varying natural inputs is a central challenge in neuroscience. Recent work has used deep neural network (DNN) models to build stimulus-computable fMRI encoding models that predict single-voxel responses to complex natural videos. However, the majority of video-computable encoding models predict responses using simple linear mappings from model tokens, overlooking the spatiotemporal structure shared by video representations and neura...

---

### 11. Socio-cognitive models in a patch foraging setting: a case study for model selection and parameter identifiability methods

**Authors:** Lisa Blum Moyse, Ahmed El Hady

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36231v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36231v1)

**Summary:** Collective patch-foraging experiments in the laboratory provide a controlled setting in which social information use can be quantified. Here, we consider a go/no-go task in which groups choose between two patches differing in food reward probability. We use agent-based simulations, underpinned by an augmented collective drift-diffusion model, to investigate alternative mechanisms for representing and integrating social information. We consider two representations, continuous (counting representa...

---

### 12. Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice

**Authors:** Hanbo Xie

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36097v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36097v1)

**Summary:** Using predictive models to explain cognition requires more than accurate behavioral predictions. Input ablations offer an appealing route: remove information from a model and interpret the resulting performance change as evidence of its importance for behavior. Yet this inference assumes that the model's dependence on information reflects the dependence of the process generating the behavior. We test it in two synthetic sequential bandit tasks with known generating policies, where past choices c...

---

### 13. NeuronSifter: Intervention Planning in CNS Microenvironments

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35445v2) | 📄 [PDF](https://arxiv.org/pdf/2609.35445v2)

**Summary:** Prioritizing central nervous system (CNS) interventions requires predicting how a dose, route, and schedule act on a partially observed microenvironment, then choosing the measurement that would change the decision. Action-conditioned predictors reduce a regimen to an identity token or a scalar exposure, discarding where and when the target is engaged; handing a point estimate to a separate planner then discards the joint uncertainty that makes a measurement worth running. We therefore treat dec...

---

### 14. NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35338v1)

**Summary:** Mechanistic discovery in neuronal microenvironments requires interventions and measurements that separate competing explanations of solute transport and neuronal response. Predictive accuracy cannot settle the question: a real mechanistic change and an error in the computational twin leave the same signature in sparse observations. We formalize this twin confounding and reason over a joint mechanism--discrepancy belief, designing experiments that separate the two. NeuronDiscover is an Agent-in-T...

---

### 15. High-rank connectivity scaffolds support precision and generalisation in recurrent neural networks

**Authors:** Ian Hawes, Matt Nolan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35207v1)

**Summary:** A major challenge in neuroscience and machine learning is to connect single-neuron influence, population dynamics, and circuit connectivity in a causal account of computation. Much previous work has shown that low-rank connectivity can generate low-dimensional dynamics in trained artificial neural networks, but this leaves unclear the functional relevance of the higher-rank structure of biological neural circuits and many artificial neuronal networks. Here we analyse recurrent neural networks tr...

---

### 16. Scaling Laws for EEG Decoding: How Much Data Is Enough?

**Authors:** José Maurício Nunes de Oliveira, Bruna J. Lopes, Léo Burgund, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35056v1)

**Summary:** Deep learning has become a cornerstone of EEG-based brain decoding, with a growing number of architectures proposed every day. However, how the performance of these different models scales with data volume is not clear. Although this relationship has been characterized in other fields under the name of scaling laws, it remains poorly understood in the EEG domain. The present study addresses this gap by investigating how scan time and subject diversity affect the performance of different architec...

---

### 17. On the Limits of Metacognitive Monitoring in LLMs

**Authors:** Dongqi Han, Yifan Yang, Dongsheng Li

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34864v1)

**Summary:** Reliable decisions depend on recognizing when an answer may be wrong. In biological cognition, metacognitive monitoring can dissociate from task performance, raising the question of how closely solving and judging are linked in language models. Here we study the confidence reports of four frontier models across 15 benchmarks. High task accuracy can coexist with weak error discrimination: a model solves 97% of competition mathematics problems while its answer-time confidence ranks correct answers...

---

### 18. Separating personal from population gains when calibrating EEG foundation models for new users

**Authors:** Xilin Tao, Kani Chen

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34801v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34801v1)

**Summary:** Foundation models are increasingly adapted to individual users, but an apparent personalization gain can simply reflect a stronger population model. This distinction matters for brain-computer interfaces, where every new user must be calibrated. We evaluated personal adaptation of three frozen EEG foundation models (CBraMod, REVE and LaBraM) in 235 held-out subjects from three motor-imagery datasets, comparing each subject's adapter with the population model and with adapters fitted to other sub...

---

### 19. Automatic Generation of Expert-Level Neuron Segmentation Masks from Fluorescence Microscopy Images for Non-Invasive Deep Learning Analysis of Phase-Contrast Images

**Authors:** Gerard Villarroya-Piqué, Víctor M. González, Esther Serrano-Pertierra, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34464v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34464v1)

**Summary:** Background & Objective Accurate segmentation of neurons in microscopy images of neuronal cultures is crucial for research on neurodegenerative diseases and neurotoxicity. Manual annotation of such images is time-consuming, subjective, and inconsistent across experts. Deep learning (DL) models offer an effective alternative, but require high-quality training datasets composed of microscopy images with accurately segmented neurons, typically created by experts. Neuronal cultures can be imaged usin...

---

### 20. FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model

**Authors:** Shucheng Liu, Changchun Shi, Kai Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34354v1)

**Summary:** Modeling resting-state functional magnetic resonance imaging (rs-fMRI) data is crucial for understanding brain-wide neural activity. However, traditional methods struggle to capture complex temporal dynamics over long horizons, to account for the brain's anatomical spatial structure, and to model high-dimensional ambient signals that lie on a low-dimensional intrinsic subspace. We propose FAST-Brain, a unified flow-aligned spatio-temporal surrogate brain model that addresses all three challenges...

---

### 21. T-SNN: Temporal Simplicial Neural Network for EEG Decoding

**Authors:** Nikita Malik, Shubhajit Roy, Mohit Kataria, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34002v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34002v1)

**Summary:** Decoding brain states requires models that capture both the evolution of neural activity and interactions among groups of brain regions. Existing EEG methods often treat recordings as multivariate time series or represent functional connectivity with pairwise graphs, leaving dynamic higher-order interactions largely unmodeled. We introduce the Temporal Simplicial Neural Network (T-SNN), which represents EEG recordings as sequences of evolving simplicial complexes. By combining simplicial convolu...

---

### 22. Harmonic Theory of Behavior

**Authors:** Mohammad Salahshour, Iain D. Couzin

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33896v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33896v1)

**Summary:** Traditional models of collective behavior rely on prescribed interaction rules, leaving unresolved the question of how behavior arises from neural representations of space. Here, we develop a first-principles theory in which movement, decision-making, and collective organization emerge by coarse-graining fast neural dynamics on a topological representation of directional space. For a ring manifold encoding heading, this reduction yields a macroscopic theory of behavior: a decision landscape over...

---

### 23. Explainable Deep Learning of Resting-State Functional Connectomes Reveals Network Biomarkers of Adolescent Intelligence

**Authors:** Md. Tanvir Rahman, Nabil Anan Orka, Asaduzzaman Khan, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33422v1)

**Summary:** Mapping resting-state brain organization to individual differences in cognitive ability remains a major challenge in population neuroinformatics. Although deep learning enables flexible modeling of brain connectivity, limited interpretability restricts its scientific and clinical utility. To address this objective, we developed an explainable deep learning framework based on sparse projected residual networks to predict fluid, crystallized, and total intelligence from resting-state functional ma...

---

### 24. Towards a full-stack functionalist theory of consciousness: Identifying its functional profile

**Authors:** Sushrut Thorat, Paras Chopra

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33366v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33366v1)

**Summary:** If consciousness is functional, a basic question is what awareness of a content actually changes in how a system operates on it. We ask, for a particular content X and mental or bodily process Y, whether awareness of X changes whether, or how well, X can be used in process Y. Crucially, X-aware and X-unaware conditions must be compared in ways that rule out poorer information about X as a sufficient explanation. Our current literature sweep yields a small but informative functional profile. The ...

---

### 25. Pre-registered spectral and certified mixing analysis of the male Drosophila central nervous system connectome

**Authors:** Eran Kopel

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33054v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33054v1)

**Summary:** We report a pre-registered test of five hypotheses about the synapse-flow random walk on the connectome of the male Drosophila central nervous system (166,700 neurons, 124 million synapses), in which a walker moves to a postsynaptic partner in proportion to synapse number. The hypotheses concern the spectral gap and its dependence on the neck connective, the localisation of the leading modes of an input-normalised signed map, the certified mixing depth measured by the Dobrushin coefficient, its ...

---

### 26. Periodically modulated traveling waves in integrate-and-fire networks: recursive speed law and propagation failure

**Authors:** Jie Nissel, Ricardo Erazo-Toscano, Rosahn Bhattarai, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.33006v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33006v1)

**Summary:** Traveling waves of activity in neural tissue can be halted by spatial inhomogeneity in synaptic coupling. We study an integrate-and-fire network in which each neuron fires once and the coupling decays exponentially. For this model the leading-edge firing map reduces exactly to a scalar equation for the wave speed in space, with a slow unstable and a fast stable homogeneous speed, $c_1$ and $c_2$, and a periodic modulation of the coupling enters this equation pointwise. Positive periodic waves te...

---

### 27. Beyond Gaussian Assumptions: Distribution-Aware Channel Capacity for Effective Connectivity

**Authors:** Jianan Jian, Jacob Kang, Nurahmed Multezem, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32774v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32774v1)

**Summary:** Effective-connectivity estimation from brain signals often relies on Gaussian residual modeling, which enables tractable estimation but can discard informative distributional structure and distort inferred directed interactions when empirical residuals are non-Gaussian. We show across multiple modalities, species, and experimental conditions that both brain signals and fitted channel residuals frequently deviate from Gaussianity. We therefore introduce a distribution-aware, information-theoretic...

---

### 28. Space versus Context: Competition for limited neural resources determines engram cell allocation in the hippocampus

**Authors:** Kensuke Chiba, Jun-nosuke Teramae

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32620v1)

**Summary:** Engram cells in hippocampal CA1 represent contextual information associated with events experienced by animals and constitute a cellular substrate of episodic memory. Recent experiments have shown that a subset of hippocampal place cells is recruited as engram cells for individual contexts. However, the principle governing engram cell allocation across contexts remains unclear. Here, we develop an information-theoretic framework that quantifies the trade-off between spatial and contextual inform...

---

### 29. Recovery-Directed Symbolic Distillation of Neural Likelihoods

**Authors:** Kianté Fernandez, Xinwei Li

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32409v1)

**Summary:** Amortized neural likelihoods enable computationally expensive inference for models with analytically intractable or unspecified likelihoods, but their black-box nature limits interpretability. We introduce a symbolic distillation pipeline that converts trained neural likelihoods into explicit, interpretable expressions optimized for efficient parameter estimation. Our approach uses a recovery-directed objective to guide symbolic regression toward expressions that preserve parameter-recovery accu...

---

### 30. From Signals to Trajectories: A Primer on Low-Dimensional Dynamics in Human EEG and MEG

**Authors:** Vanessa Hadid, Hamza Abdelhedi, Annalisa Pascarella, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32315v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32315v1)

**Summary:** Neural activity unfolds not as a set of independent signals, but as a coordinated dynamical process that can be described as a point moving through a high-dimensional state space. This perspective has contributed substantially to recent developments in systems neuroscience, especially through studies of directly recorded neuronal population activity, but remains comparatively underused in non-invasive human recordings such as EEG and MEG. In this primer, we present a neural trajectory analysis b...

---

### 31. MAESTRO: a Multimodal Auditory-attention Egocentric Speech-TRacking Open corpus

**Authors:** K M Naimul Hassan, Ali Alavi, Donald S. Williamson

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31898v1)

**Summary:** Humans rely on gaze, head movements, and visual cues to attend to speakers in noisy environments, yet auditory attention decoding (AAD) has been studied primarily using electroencephalography (EEG). We introduce the Multimodal Auditory-attention Egocentric Speech-TRacking Open (MAESTRO) corpus, the first AAD dataset to simultaneously record EEG, eye gaze, pupillometry, egocentric video, and head inertial measurement unit (IMU) data. MAESTRO includes four competing speakers and background noise a...

---

### 32. FlatClip: A Geometry-Aware Surface-Level Baseline for fMRI Representation Learning

**Authors:** Mo Wang, Wenhao Ye, Zihan Ning, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31204v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31204v1)

**Summary:** Recent fMRI foundation models differ substantially in the spatial scale at which they represent brain activity. ROI- and connectivity-based models are efficient but coarse, whereas voxel-level models preserve fine-grained spatial structure but require specialized 3D/4D architectures and costly fMRI-specific pretraining. We ask how effectively an image-pretrained encoder can reuse the spatial organization of cortical activity. Motivated by evidence that macroscale brain activity is strongly const...

---

### 33. Learning a non-linguistic code for inferred rules from reward

**Authors:** Cristiano Capone

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31192v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31192v1)

**Summary:** How can a rule inferred from examples reach someone who never saw them, without a shared code? Patients with severe aphasia do it by gesture or sketch. One network sees worked examples and emits eight invented symbols; a second, blind to them, applies them to a new input. Rewarded for the second's success, the first learns a code carrying rules to three-step transformations training never presents, which new learners acquire. Like invented human languages, the code has two regimes: under reward ...

---

### 34. Grid-cell firing fields lack local sixfold symmetry

**Authors:** Anian Kerscher

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31145v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31145v1)

**Summary:** The firing fields of a grid cell form a hexagonal lattice, yet each field's intrinsic geometric structure remains unclear: Are individual grid fields radially symmetric or do they exhibit (weak) sixfold modulation inherited from the global lattice? To address this question, we quantified the within-field angular structure using harmonic analysis and per-cell matched simulations that preserved sampling statistics, field scale, and lattice geometry after correction for global elliptic deformation....

---

### 35. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v2) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v2)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 36. AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets

**Authors:** Marco Rothermel, Madleen Stenger, Soroush Daftarian, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27729v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27729v1)

**Summary:** In neuropsychiatry, the primary goal is often not only to decode brain activity but to change it, for example to lessen a negative affective bias or an overly salient memory. Motivated by control theory, we develop an AI-driven neural-surrogate framework that proposes candidate representational changes and tests their predicted perceptual effects from snapshots of stimulus-evoked fMRI activity, without physical stimulation. The framework combines fMRI decoding, deep generative modeling, and cons...

---

### 37. The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity

**Authors:** Agnese Adorante, Aaron Spieler, Anna Levina

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26940v1)

**Summary:** Biological sensory neurons have selective receptive fields organized along meaningful stimulus coordinates, such as frequency, motion direction, or retinotopic position. Such structure may arise from efficient coding and biological constraints on activity, connectivity, and wiring, as computational studies of simple neurons have shown across modalities. This raises a question: do structured receptive fields confer a computational advantage beyond resource efficiency itself, and does this advanta...

---

### 38. Deep Learning in Infant Functional Neuroimaging: Challenges, Advances, and Future Directions

**Authors:** Dan Hu, Jiale Cheng, Weiran Xia, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26688v1)

**Summary:** Infancy is a critical developmental window characterized by rapid functional brain reorganization, during which large-scale networks emerge, individualized connectome signatures continue to form, and early deviations may shape long-term cognitive and clinical outcomes. Functional MRI (fMRI) offers an opportunity to study these processes in vivo, yet extracting developmentally meaningful information from it remains challenging due to comparatively short scan duration, structured motion artifacts,...

---

### 39. Physics-constrained inference of somatic dynamics from dendritic recordings with sparse somatic supervision in weakly coupled two-compartment neuron model

**Authors:** Abdeltif Oujbara, Benjamin Ambrosio, M. A. Aziz-Alaoui

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25436v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25436v1)

**Summary:** Somatic membrane potential is the primary determinant of neuronal output, yet it remains inaccessible in many experimental setups where only dendritic recordings are available. Reconstructing somatic dynamics from distal measurements is a challenging inverse problem, particularly when the soma and dendrites are weakly coupled, as dendritic signals represent a filtered and attenuated version of somatic activity. To address this, we use a physics-informed neural network (PINN) constrained by a two...

---

### 40. A theory of plasticity: capacity for change as inverse configurational constraint

**Authors:** Igor Branchi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25312v1)

**Summary:** Plasticity is invoked across the sciences to explain how systems can change, yet it is inferred from the very change it is meant to explain. A system may have many alternatives, realize none and still be plastic. Another may be driven far toward its only alternative, but the magnitude of that change does not establish its plasticity. What matters for plasticity is not how far the system moves but how strongly its present configuration constrains alternatives. Here I propose that plasticity, unde...

---

### 41. Binding-Motivated Contextuality: A Cross-Domain Cyclic Test in Perception and Judgment

**Authors:** Adam Y. Shavit

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23977v2) | 📄 [PDF](https://arxiv.org/pdf/2609.23977v2)

**Summary:** Psychophysics and decision research study perceptual binding and judgment contextuality apart. We argue both are scored against the same cyclic noncontextuality inequalities and share one convex global-consistency geometry -- not one cohomology class -- though only contextuality is tested, since binding's own residual vanishes here. Building on sheaf formulations of predictive coding (Seely 2025) and contextuality (Abramsky & Brandenburger 2011), a cyclic set of pairwise judgments admits a nonco...

---

### 42. Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery

**Authors:** Kevin Zhou, Sparsh Roy

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23924v1)

**Summary:** Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supe...

---

### 43. A discrete generative model of neuronal spiking activity on microelectrode arrays

**Authors:** Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23907v1)

**Summary:** Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a d...

---

### 44. From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture

**Authors:** Janusz A. Starzyk, Wiesław L. Galus

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23828v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23828v1)

**Summary:** This article asks under what conditions artificial intelligence could warrant a rational attribution of consciousness. Linguistic ability, multimodality, memory, planning, action control, and humanoid embodiment are not sufficient evidence of phenomenal experience. Biological precursors such as excitability, homeostasis, neural networks, and hierarchical representation instead identify functions whose counterparts may be engineered. The paper compares conventional LLMs, hybrid h-LLMs, vision-lan...

---

### 45. Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification

**Authors:** Zihan Wang, Daixin Li, Guilin Wang, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23317v1)

**Summary:** Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we...

---

### 46. BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings

**Authors:** Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora, et al.

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22064v1)

**Summary:** Advances in large-scale neural recording have made it possible to collect data across many animals and distributed brain regions, raising the question of whether this scale can be exploited to learn general-purpose neural representations transferable across diverse downstream tasks. Yet, progress toward this goal has been limited by fragmented evaluation protocols and a narrow focus on individual task domains. Here, we present BrainWideBench, a benchmark for evaluating across-animal transfer on ...

---

### 47. Identifying Neural State Changes due to Gain versus Off-Manifold Displacement

**Authors:** Sam McKenzie

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21272v1)

**Summary:** Memory segmentation is thought to arise from rapid decorrelation in neural activity, often quantified by Euclidean distance or cosine angle. Although these metrics detect a transition, they do not reveal how the new state relates to the repertoire represented by the neural manifold. This matters because neuromodulators that drive state transitions also alter excitability, and learning may repurpose existing representations or create new ones. Here, I introduce a geometric decomposition that sepa...

---

### 48. Foundation-model-based multi-label phenotyping of combined hyperkinetic movement disorders

**Authors:** Laura Cif, Zohra Souei, Diane Demailly, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.22369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22369v1)

**Summary:** Movement disorders (MDs) frequently co-occur, yet phenomenological and severity assessment shows substantial inter-rater variability. Markerless video could improve reproducibility, but prior work is largely single-symptom, depends on standardized acquisition, and lacks validation and transfer across ages and sites. We combined two foundation models into one frozen backbone: Segment Anything Model 3 (SAM 3) for dense, per-frame markerless segmentation summarized into geometric, contour and grid ...

---

### 49. A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound

**Authors:** Thomas J Stoll, Ross K Maddox

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20595v2) | 📄 [PDF](https://arxiv.org/pdf/2609.20595v2)

**Summary:** Computational models of auditory physiology commonly target specific responses or stages of the auditory pathway, limiting their ability to integrate findings across experimental paradigms and neural timescales. We present a foundation model of human auditory electrophysiology: a causal neural network trained to map binaural acoustic waveforms directly to high-sample-rate EEG. The model was trained on approximately 250 hours of EEG data from 92 subjects, with varied electrode montages and stimul...

---

### 50. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

## stat.ML

**50 papers**

### 1. ReCIRC: Rectified Conformal Risk Control

**Authors:** Bruno Marcondes e Resende, Helton Graziadei, Thiago Rodrigo Ramos, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38112v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38112v1)

**Summary:** Many applications of black-box predictive models require controlling task-relevant error rates, such as missed lesion pixels in segmentation or missed labels in multilabel classification. Conformal risk control (CRC; Angelopoulos et al., arXiv:2208.02814) gives distribution-free guarantees for such losses, but it calibrates a single threshold shared by all inputs. Because conditional risk varies with the input, this marginal guarantee often overprotects easy cases and underprotects hard ones. We...

---

### 2. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

### 3. Latent Inference-Time Guidance of Time Series Foundation Models

**Authors:** Chloé Hashimoto-Cullen, Amaury Durand, Laurent Bozzi, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38058v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38058v1)

**Summary:** Time Series Foundation Models (TSFMs) currently provide state-of-the-art results in forecasting tasks. They are available out-of-the-box and rely on in-context learning to make their predictions, which makes the quality of their performance highly sensitive to the user-selected lookback, covariates, horizon and training data distributions. In practise, the quality of the forecasts are variable but complementary, which highlights the need for a principled ensembling approach, rather than selectin...

---

### 4. When do data mixtures improve scaling laws? Insights from high-dimensional regression

**Authors:** Diyuan Wu, Lehan Chen, Theodor Misiakiewicz, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38011v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38011v1)

**Summary:** Modern machine learning systems are trained on mixtures of data from different domains, and choosing the right mixture can substantially improve downstream performance. Despite an extensive literature on data mixing and reweighting, existing work is largely empirical and it remains unclear when auxiliary data genuinely improves scaling laws rather than merely providing more samples. To gain insight into this question, we study a high-dimensional mixed-data regression model with a shared regressi...

---

### 5. Mutual Information Constrained Chernoff Bottleneck

**Authors:** Dier Tang, Guangyue Han

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37994v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37994v1)

**Summary:** The classical information bottleneck (IB) measures the relevance of a representation $U$ of $X$ to a target $Y$ by $I(U;Y)$, which does not directly characterize the error of downstream decisions. For a binary hypothesis $Y$ inferred from many separately encoded observations, the optimal error exponent is the Chernoff information between the two conditional distributions of $U$ given $Y$. We study the mutual information constrained Chernoff bottleneck, which seeks an encoder that maximizes this ...

---

### 6. A shape-similarity latent space for fluid interfaces: invertible reduced-order modelling of droplet morphology

**Authors:** Ali R. Hashemi, Mohammad R. Hashemi, Pavel B. Ryzhakov

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37947v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37947v1)

**Summary:** A droplet breaks up in tens of microseconds, and a recording captures perhaps a dozen frames. The states in between cannot be recovered without repeating the experiment, and simulating them is too costly to sweep an operating envelope. Yet they are present in the corpus as a whole: a campaign spanning a device's actuation range produces morphologies resembling those any single recording missed. Exploiting that requires a representation that is low-dimensional, invertible, and faithful to shape r...

---

### 7. Identifiability Guarantees for Drivers and Dynamics of Delayed Physical Systems

**Authors:** Julien Boussard, Antoine Débouchage, Théo Saulus

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37944v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37944v1)

**Summary:** A wide range of methods have been proposed, including physics-informed neural networks, which are powerful but do not guarantee identifiability of the dynamics, symbolic regression, which requires a set of precomputed operations, and causal discovery, which is more principled but usually relies on strong assumptions that physical systems may violate. In this work, we develop a theory-grounded method and prove that under a set of permissive assumptions, the structural drivers and drift of stochas...

---

### 8. Post-Anomaly Detection Inference for Deep SVDD

**Authors:** Cao Le Cong Thanh, Dang Quang Vinh, Vo Nguyen Le Duy

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37935v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37935v1)

**Summary:** Deep Support Vector Data Description (Deep SVDD) has become a prominent framework for unsupervised anomaly detection by learning latent representations that compactly characterize normal data around a center. Despite its empirical success, anomaly decisions produced by Deep SVDD are typically made solely based on anomaly scores without rigorous statistical guarantees, thereby limiting their reliability in safety-critical and high-stakes applications where false positives must be strictly control...

---

### 9. Search Dimension in Unlabeled Projection Pursuit: A Scaling Law for Subspace Restriction

**Authors:** Rares Dimitrie Grozavescu, Mark Girolami

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37917v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37917v1)

**Summary:** Projection pursuit searches for a direction along which the data look least Gaussian. When the observation space contains a large Gaussian complement, the empirical objective can be minimized by a direction that carries no signal, with empirical kurtosis as low as at the truth. Sample splitting exposes rather than repairs this failure. Appending coordinates independent of the latent regime degrades the search while leaving Bayes recoverability unchanged. Restricting the search to the column spac...

---

### 10. Counterfactual Probing for Parallel Unmasking with Hidden Forest Structure

**Authors:** Ryotaro Kawata, Satoshi Hayakawa, Taiji Suzuki

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37841v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37841v1)

**Summary:** Masked generative models offer parallel token prediction, but accurate parallel sampling must account for dependencies among tokens. When dependencies are unknown, finding safe batches also costs model evaluations. We study whether total evaluations, including discovery, can be sublinear in sequence length $N$; sublinear sequential depth then follows. We consider discrete distributions with hidden forest structure, accessed through a fixed approximate conditional oracle. Under explicit regularit...

---

### 11. When Noise Estimation Hides Basis Misspecification in Repeated Bayesian Inverse Problems

**Authors:** Rares Dimitrie Grozavescu, Mark Girolami

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37762v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37762v1)

**Summary:** Basis-restricted priors in Bayesian inverse problems can lose coverage when the truth has components outside the basis. We show that estimating the observation-noise variance can hide this loss. Under a linear forward model, when the in-span prior variance dominates the noise, the maximum-likelihood noise estimate absorbs the out-of-basis energy in the complement of the model range. Residual-magnitude and observation-coverage checks then stay near nominal while field coverage falls. We study rep...

---

### 12. SPARK: A General Goodness-of-Fit Assessment via Residual Projection

**Authors:** Xingwei Liu, Yuhong Yang, Wangli Xu

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37705v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37705v1)

**Summary:** Goodness-of-fit testing is a basic tool for assessing whether a fitted procedure has captured the systematic information contained in the covariates. While traditional theory has largely focused on parametric regression models, modern data analysis increasingly relies on flexible black-box learners, whose predictive success alone is insufficient to assess model accuracy. In this paper, we propose SPARK, a general framework for goodness-of-fit testing that applies to traditional statistical model...

---

### 13. The double descent and Runge phenomena in overparametrized polynomial interpolation

**Authors:** Jason Wein, Stephan Wojtowytsch

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37657v1)

**Summary:** The Runge phenomenon in polynomial interpolation is often considered a classical analogue of the double descent phenomenon in machine learning. In this note, we explore overparameterized polynomial interpolation in three popular polynomial bases: Monomial, Chebyshev and Legendre basis with coefficients that are minimal in the $\ell^2$-norm (and, for the monomial basis, also those minimal in the $\ell^1$-norm). We present our results primarily for equidistant and Chebyshev data points, but many r...

---

### 14. A Finslerian Approach for Embedding Directed Data

**Authors:** Gwendal Debaussart-Joniec, Théau Blanchard, Argyris Kalogeratos

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37649v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37649v1)

**Summary:** Many datasets carry an intrinsic directionality: citations point backward in time, cells differentiate along lineages, and traffic follows preferred routes. Spectral embedding methods, including most of their extensions to directed graphs, discard this information: they symmetrize the data and map it into a Euclidean space where asymmetry cannot be represented. We instead model directed data as sampled from a Finsler manifold, whose distance depends on the direction of travel, and study the kern...

---

### 15. RLTL;DR: Self-improvement by Internalizing Self-generated Feedback

**Authors:** Michael Kirchhof, Eleonora Gualdoni, Andrew Szot, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37633v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37633v1)

**Summary:** The common paradigm of reinforcement learning with verifiable rewards (RLVR) is to let agents make multiple attempts at a task, and optimize towards the successful ones. This becomes problematic in the realms of self-improvement, where tasks are so difficult that the agent has a low or even no chance of success, and where there are no teacher models or example solutions to distill from. In this paper, we introduce RLTL;DR. After each failed attempt, we show the policy the verifier outputs and le...

---

### 16. XU-RS: Explaining Credal Width in Random-Set Language Models

**Authors:** David Achara, Maryam Sultana, Alexander D. Rast, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37594v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37594v1)

**Summary:** Uncertainty estimates tell us how unsure a model is, but not why. Without knowing which parts of an input influences a model's uncertainty, we cannot tell whether that uncertainty score depends on input features that are relevant for the task. We study this problem in randomset classifiers built using pretrained language models. These classifiers assign probability to individual answers and to groups of answers, producing lower and upper probabilities for each answer; The difference between thes...

---

### 17. Ornstein-Uhlenbeck Is Hard to Beat, Yet Superlinear Drift Ships Lower Transport Costs

**Authors:** Attila Lovas, Lóránt Nagy

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37579v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37579v1)

**Summary:** Brešar and Mijatović \cite{bresar2025} show that Ornstein--Uhlenbeck diffusion is hard to beat in forward convergence under assumptions that exclude superlinear drift. We instead test superlinear Langevin diffusions for score-based image generation, computing their conditional scores numerically from a Fokker--Planck equation. In our experiments, the superlinear models beat the Ornstein--Uhlenbeck baseline on empirical Wasserstein distance across nearly the entire tested grid and show less varia...

---

### 18. Why Adaptive Optimizers Underestimate Rare Tokens

**Authors:** Sangsidhya Kar

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37535v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37535v1)

**Summary:** In the softmax output layer, a rare token receives a small positive logit gradient on most steps and a much larger negative gradient on the few steps when it is the target. SGD simply adds these contributions. Coordinate-wise adaptive methods such as Adam, RMSProp, and sign descent instead divide each update by a running estimate of its magnitude, and that estimate is largest immediately after the token appears. This imbalance has two effects. At the level of the whole output layer, we character...

---

### 19. Physical Muon: Orthogonalization as an Equilibrium Computation

**Authors:** Yuren Hao

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37525v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37525v1)

**Summary:** Physical neural networks and analog in-memory computing could reduce the energy cost of neural network training. Realizing this potential, however, requires optimizers that combine effective learning with physical implementability. SGD fits local analog updates but struggles on transformers, while Adam family is unstable against analog bias. Muon offers strong training performance, but its Newton--Schulz orthogonalization relies on dense matrix-matrix products. To address this obstacle, we intro...

---

### 20. A stochastic subgradient method with optimal failure exponent

**Authors:** Bart P. G. van Parys

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37425v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37425v1)

**Summary:** Fix a target accuracy $\varepsilon$, a gradient-noise level $s$, and a horizon $N$. We wish to design algorithms which minimize the probability of observing a suboptimality gap which exceeds the target accuracy, i.e., $\mathcal{E}_N = -\log \sup_{f,P} \mathbb{P}_P(f(x_A) - f_\star \ge \varepsilon)$, with the noise law $P$ known only to be sub-Gaussian. We single out a uniformly averaged schedule which is harmonic (of the form $h_k = R^2/(\varepsilon (N+m-k))$) and prove, via an optimized exponen...

---

### 21. High-Dimensional Simulation-Based Inference in Latent Spaces

**Authors:** Lars Kühmichel, Stefan T. Radev, Bhanu Prasanna Koppolu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37381v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37381v1)

**Summary:** Neural simulation-based inference (SBI) has been widely successful in inferring a relatively small number of interpretable parameters from potentially high-dimensional observations, such as images or time series. Accordingly, representation learning in SBI has focused almost exclusively on compressing the observations used to condition the posterior. More recently, however, SBI has begun to target increasingly high-dimensional parameter spaces, raising the complementary question of whether the i...

---

### 22. A Sharp Transition in Data Reconstruction under Differential Privacy

**Authors:** Max Cairney-Leeming, Simone Bombari, Marco Mondelli

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37344v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37344v1)

**Summary:** Data reconstruction attacks have empirically been successful in recovering training samples from learned models, raising privacy concerns and motivating defenses with guarantees that remain valid against future threats. While differential privacy (DP) provides formal protection, choosing the privacy budget remains a challenge: small budgets severely reduce utility, but it is hard to quantify how large the budget can be without allowing accurate reconstruction. In this work, we study informed att...

---

### 23. Interacting particle guidance for sampling reward-tilted generative priors

**Authors:** Adhithyan Kalaivanan, Zheng Zhao, Jens Sjölund, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37227v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37227v1)

**Summary:** Inference-time steering adapts pretrained diffusion and flow-based models to new tasks, e.g., to generate samples from a conditional distribution or samples with desired properties, without retraining. This can be formalized as sampling from a reward-tilted generative prior. As exact sampling from this distribution is intractable, guidance-based methods rely on approximations producing biased samples, and sequential Monte Carlo (SMC) methods correct for this bias using importance weights. Howeve...

---

### 24. Pointwise or Pairwise: When Do Pairwise Losses Help Reward Learning, Provably?

**Authors:** Junghyun Lee, Minsoo Ha, Sanghwa Kim, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37209v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37209v1)

**Summary:** Pairwise losses are increasingly used for reward learning even when pointwise rewards are observed, with mixed empirical results. When and why do pairwise losses outperform pointwise losses? We study this question in a grouped offline contextual-bandit setting allowing multiple actions per context, capturing many reward learning scenarios. We compare Value Regression (VR), which regresses observed rewards pointwise, with Value Difference Regression (VDR), which regresses reward differences betwe...

---

### 25. Interpretable intrinsic dimension estimation through componentwise calibration of distance and angle

**Authors:** Chih-Hsuan Huang, Chih-Wei Chen, Szu-Chi Chung

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37114v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37114v1)

**Summary:** DANCo (Dimensionality from Angle and Norm Concentration) jointly calibrates nearest-neighbor distance and angular statistics and consistently reaches state-of-the-art accuracy on clean intrinsic-dimension (ID) benchmarks. Practical data, however, introduce neighborhood-relative noise and sample-amplitude heterogeneity that can distort these geometric signals. We reformulate DANCo componentwise, retaining separate distance and angular discrepancy curves so that the source of an estimate can be id...

---

### 26. Identifying ODEs from Unstructured Data with Causal Representation Learning

**Authors:** Alessandro Trenta, Riccardo Massidda, Davide Bacciu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37083v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37083v1)

**Summary:** We study the problem of recovering the governing ODE of a dynamical system from unstructured, high-dimensional observations such as images. Existing methods for ODE discovery typically assume direct measurements of the variables, or do not provide theoretical guarantees on the learned variables and equations. While Causal Representation Learning (CRL) methods provide guarantees on identifying variables from high-dimensional observations up to component-wise diffeomorphisms, we show that in gener...

---

### 27. Iterative Exact Discrete Guidance for Energy-Based Sampling

**Authors:** Yuwen Qian, Yidong Ouyang, Zhengyan Wan, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37043v1)

**Summary:** Sampling from unnormalized distributions over large discrete state spaces becomes difficult when a multimodal target is far from a tractable reference. We introduce Iterative Exact Discrete Guidance (IEDG), a population-exact, trajectory-wise guidance framework for unnormalized discrete targets. Rather than learn the full reference-to-target correction in one step, IEDG introduces a global Boltzmann tilt along an annealing trajectory. Each stage learns a stage-local posterior correction for an i...

---

### 28. Scalable Diffusion SBI for Compositional Inference under Simulator Misspecification

**Authors:** Vincent D. Zaballa, Elliot E. Hui

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36950v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36950v1)

**Summary:** Simulation-based inference is challenging when many heterogeneous observations must be composed, hierarchical latent structure must be preserved, and the simulator is misspecified relative to observed data. We develop sampling and fine-tuning methods for diffusion-based inference in design-conditional settings, where the same simulator is queried across different experimental conditions $ξ$. We extend compositional score-based inference with a continuous-time diffusion coefficient that accounts ...

---

### 29. Beyond Conditional Independence: Root Cause Analysis with Deep Causal Models

**Authors:** Md Musfiqur Rahman, Kenneth Lee, Ziwei Jiang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36771v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36771v1)

**Summary:** Root cause analysis (RCA) is a critical problem in many real-world scenarios. RCA enables the identification of faulty or failing mechanisms in a system by comparing anomalous observations with corresponding reference (i.e., regular) observations. However, existing approaches rely either on heuristic methods or on conditional independence tests with a strong unconfoundedness assumption, and thus fail to exploit other complicated distributional constraints in the presence of latent variables. To ...

---

### 30. Federated Clustering with Unknown Local and Global Cluster Cardinalities

**Authors:** Mitushi Goyal, Tarun S., Riddhanya Senapathi, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36762v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36762v1)

**Summary:** Federated clustering methods that do not require the global number of clusters $K$ still assume that each client knows its local number $K_g$. This assumption is hard to justify when clients know no more about their data than the server does, as in fault diagnosis across independently operated industrial sites. We propose a two-phase framework in which neither count is known: each client first estimates $K_g$ from its own data, and an aggregator that requires local counts, such as FedGEM, then u...

---

### 31. Into the danger zone: stable extrapolation in high-dimensional function and operator learning

**Authors:** Ben Adcock, Simone Brugiapaglia, Xuemeng Wang

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36709v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36709v1)

**Summary:** Out-of-distribution (OOD) generalization is a central challenge in scientific machine learning. We study regression problems in which the test distribution differs from the training distribution and ask: under what assumptions on the target function or operator is stable extrapolation possible, and how far beyond the training domain can one extrapolate? Existing theory controls the test error through additive penalties measuring the discrepancy between the training and test distributions. Such g...

---

### 32. When Is Coarse Supervision Worth It? Cost-Aware Learning under Unknown Aggregation

**Authors:** Jianyu Xu, Smriti Jha, Aarti Singh, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36704v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36704v1)

**Summary:** Modern learning systems often acquire supervision at multiple resolutions, trading annotation cost against information content. We study cost-aware two-resolution learning, where expensive fine labels reveal a vector response and cheaper coarse labels reveal a scalar aggregate formed with unknown weights, while the target remains the full response. The challenge is that unknown aggregation changes which directions coarse data can identify, so the value of coarse supervision depends jointly on co...

---

### 33. Understanding Private Evolution as Learning-Augmented Clustering

**Authors:** Audra McMillan, Kunal Talwar, Felix Zhou

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36678v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36678v1)

**Summary:** Private Evolution (PE) is a differentially private algorithm for synthetic data generation. While it can be viewed as a Wasserstein learning algorithm, it performs much better in practice than worst-case Wasserstein analyses would predict. We recast PE as generative model-augmented Wasserstein learning. We show theoretically that when we take into account the use of a generative model that is able to capture something about the true distribution, then we can obtain much better performance bounds...

---

### 34. Second-Moment Stochastic Approximation Methods

**Authors:** Tao Jiang, Lin Xiao

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36600v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36600v1)

**Summary:** Classical stochastic approximation methods rely on estimators of the first moment (mean) of a random regression function. We study methods that employ estimators of both the first and the second moments, which include modern deep-learning optimizers such as Adam and Muon as special cases. We derive second-moment stochastic approximation methods through the lens of optimal preconditioning for solving matrix equations, and develop a two-stage framework for their convergence analysis. The first sta...

---

### 35. Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond

**Authors:** Xiaokai Luo, Chenghao Xu, Haotian Xu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36594v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36594v1)

**Summary:** We study multiple change-point detection in multivariate time series whose distributions change in a piecewise constant manner. Distributional changes can manifest across different moment orders, from shifts in the mean and covariance to changes in higher-order moments. Higher-order moments capture increasingly rich distributional features but become difficult to estimate in high dimensions. Our tensor representation unifies moments of different orders within a common linear algebraic framework,...

---

### 36. Hierarchical Utility Calibration for Structured Multiclass Decisions

**Authors:** Futoshi Futami, Jerry Huang, Ichiro Takeuchi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36532v1)

**Summary:** In multiclass probabilistic prediction, Utility Calibration (UC), which focuses auditing on specified utilities, has recently received attention as a way to guarantee downstream decisions while controlling computational and sample requirements. At the same time, some multiclass problems have meaningful label hierarchies that play important roles in medicine and image classification, yet how UC evaluates utility within a hierarchy remains insufficiently understood. We show that the difference bet...

---

### 37. Optimal Multi-Reward Reinforcement Learning

**Authors:** Zijun Chen, Zihan Zhang

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36486v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36486v1)

**Summary:** We study an unknown-transition finite-horizon Markov decision process (MDP) with a finite collection of known reward functions $\{r^1, r^2, \ldots, r^M\}$. The goal is to output an $ε$-optimal policy for every reward using online episodic interaction only. Performance is measured by the policy error $V_{0}^{*, m} - V_{0}^{\widehatπ^{m}, m}$ where $m\in [M]$ represents the reward function and $V_{0}^{*, m}=\mathbb{E}_{s_1\sim μ}[V_{1}^{*, m}(s_1)]$. Under this setting, we design a provably effici...

---

### 38. LOCO-AdaMP: Built-in LOCO Inference for Adaptive Minipatch Ensembles with Enhanced Prediction

**Authors:** Yinan Cheng, Lili Zheng

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36396v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36396v1)

**Summary:** As black-box machine learning models become increasingly common, extracting interpretations with uncertainty quantification has become a critical challenge. One popular type of interpretation is leave-one-covariate-out (LOCO) feature importance, while prior LOCO inference methods often require data-splitting or model-refitting. A recent ensemble framework, LOCO-MP, addresses these challenges using minipatches that subsample both observations and features, but massive feature subsampling can hurt...

---

### 39. Finite-Sample Theory for Fitted Q-Iteration When Actions Are Functions

**Authors:** Gefei Lin, Rui Miao, Xiaoke Zhang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36390v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36390v1)

**Summary:** Offline reinforcement learning seeks optimal decision rules from previously collected data. In some applications, a decision can be an entire function, such as a fluence map in radiation therapy or a smooth movement trajectory in robotics. In this paper, we study the finite-sample theory for fitted Q-iteration (FQI) with functional actions in a discounted infinite-horizon setting. Three major difficulties arise in this setting: first, the absence of a Lebesgue probability density for functional ...

---

### 40. Adapting Linear-Time Architectures for Tabular In-Context Learning

**Authors:** David Schnurr, Felix Sarnthein, Thomas Hofmann, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36337v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36337v1)

**Summary:** Tabular foundation models achieve strong performance by conditioning on labelled examples in context, but softmax attention limits their use on large datasets. Existing linear-time alternatives, however, are mostly causal, and their potential for tabular in-context learning (ICL) remains underexplored. To address this, we (1) revisit causal training setups, (2) compare linear sequence mixers, and (3) investigate their ICL generalisation beyond the pretraining context length. First, we show that ...

---

### 41. Cheap and Powerful Tests for Supervised Subspaces: Per-Component Inference for PLS

**Authors:** Paweł Lenartowicz, Hubert Plisiecki

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36307v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36307v1)

**Summary:** Partial Least Squares (PLS) regression extracts a few outcome-aligned directions in a high-dimensional X and is widely used across applied science, but inference on the resulting fit is either expensive, biased and discouraged, or absent. We reduce inference to held-out OLS refits of the supervised subspace, a primitive shared by PLS, supervised PCA, and linear probes, and supply two tests using held-out correlations: a Nadeau-Bengio corrected asymptotic t-test as a fast approximation, and a per...

---

### 42. MoRE: Scaling mixture of experts with hardware-aware low-rank routing

**Authors:** Honam Wong, Surbhi Goel, Enric Boix-Adserà

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36301v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36301v1)

**Summary:** Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts. In this regime, the standard linear router becomes a bottleneck: with $M$ experts and hidden dimension $h$, its per-token cost $Θ(Mh)$ dominates the MoE layer once $M$ is large. We introduce MoRE (Mixture of Rank-reduced-routed Experts), which factorizes the router weight matrix at rank $r$ and reduces the routing cost to $O((h + M)r)$. We prove that rank logari...

---

### 43. GNA: Granular Neighbor Assembly for Retrieval-Augmented Multivariate Time-Series Forecasting

**Authors:** Vincent Uhse

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36281v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36281v1)

**Summary:** Deep forecasters predict from a fixed-length lookback window, and lengthening it gives diminishing returns at a growing cost. Retrieval augmentation instead shows the model how similar past situations continued. Retrieving a whole past window gives every variate the continuation of the same past moment. In multivariate series, however, the best past match differs from variate to variate. We present GNA (Granular Neighbor Assembly), a retrieval layer for forecasting backbones that assembles neigh...

---

### 44. Stochastic Optimization Under Power-Law Spectra: Tight Bounds and Shuffling Analysis

**Authors:** Thomas Dybdahl Ahle, Yaroslav Bulatov, Christopher De Sa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36271v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36271v1)

**Summary:** Recent work has established that power-law spectral conditions on data enable tight convergence bounds for deterministic gradient descent, resolving the conflict between classical exponential bounds and observed power-law learning curves. In this work, we extend this result to the stochastic regime of high-dimensional machine learning. We provide two main contributions: (1) We generalize the power-law spectral theory to Stochastic Gradient Descent (SGD), showing that the same spectral exponents ...

---

### 45. OTROPE: Optimal Transport-based Robust Off-policy Evaluation for Large Language Models

**Authors:** Liner Xiang, Wenbo Zhang, Hengrui Cai

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36264v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36264v1)

**Summary:** Reliable evaluation of large language models (LLMs) is essential for their development and deployment, yet is often costly, risky, and difficult to perform safely online. We study off-policy evaluation for LLMs, where limited human-labeled data from a behavior model are used to evaluate a newer target LLM. This setting is challenging because labels are scarce, behavior--target distribution shift is common, and response likelihoods are often unavailable for black-box LLMs. We propose the Optimal ...

---

### 46. The Signed Geometry of One-Shot Recourse: On-Path Validity and the Signed-Curvature Criterion

**Authors:** Hazar Yueksel

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36252v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36252v1)

**Summary:** Closed-form recourse moves a rejected user along the unit gradient $\hat g$ of the classifier score $f$ by the promised distance $d_p=|f(x)|/\|\nabla f(x)\|$, at which the linearized score reaches zero. We ask when this one-shot step succeeds and what additional model queries change. To leading order the step ends on the favorable side exactly when the path curvature $κ=\hat g^\top\nabla^2 f(x)\,\hat g$ is nonnegative. Across 80 shallow models, the fraction of rejected users whose step ends ther...

---

### 47. Can Representation Learning Decouple from Loss Minimization? Polar Updates Have an Answer

**Authors:** Akash Kumar

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36240v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36240v1)

**Summary:** Does representation learning stop when the training loss stops improving? We study this question for matrix Muon, whose polar-normalised updates have a step length set by the gradient's rank rather than its norm. Near the edge of stability, full-batch Muon on teacher-student problems enters approximately period-2 loss oscillations that persist for thousands of steps: the cycle-mean loss stays flat or rises, yet the weights keep moving and the learned features continue to align with the teacher s...

---

### 48. One-Step Next-Latent Prediction Is Not a World Model

**Authors:** Shitong Wang, Zhongang Cai, Yuzhou Hong

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36227v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36227v1)

**Summary:** Next-latent prediction fits a map from the current embedding to the next one. LeNEPA carries this objective to time series, replacing the stop-gradient of next-embedding prediction with the isotropy penalty of LeJEPA. A world model is a transition kernel that can be rolled out. The one-step regression identifies a conditional mean, and a mean is a kernel only in special cases. For a linear-Gaussian Markov latent, the mean transition and the innovation covariance are fixed by the one-step problem...

---

### 49. Copula Active Subspaces I: A Score-Covariance Method for Reduced-Order Non-Gaussian Density Estimation

**Authors:** Joshua Chen, Peter Jan van Leeuwen

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36142v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36142v1)

**Summary:** In Bayesian inference problems with non-Gaussian observation noise, the posterior is only as accurate as the noise density, and gradient-based samplers need that density and its gradient evaluable pointwise, whether from an explicit expression or from code, and without an inner solve. We propose Copula Active Subspaces (CAS) to represent this noise density. A componentwise rank transform isolates the noise law's dependence in its copula, and a rank-$r$ reduction keeps only the directions along w...

---

### 50. Graph-Split Bayesian Causal Forest for Spatial Heterogeneous Treatment Effect Estimation

**Authors:** Shuren He, Huiyan Sang, Ligang Lu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36046v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36046v1)

**Summary:** In spatial observational studies, treatment assignment and outcomes often exhibit spatial dependence patterns, and treatment effects may vary across space and subpopulations due to both measured and unmeasured spatially structured confounders. Accounting for spatial dependence while estimating heterogeneous treatment effects (HTEs) is a central task in spatial causal inference. Causal Bayesian additive regression tree methods are popular nonparametric methods for modeling and estimating HTEs. De...

---

