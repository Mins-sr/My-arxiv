# arXiv Daily Digest - 2026-02-11

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Biases in the Blind Spot: Detecting What LLMs Fail to Mention

**Authors:** Iván Arcuschin, David Chanin, Adrià Garriga-Alonso, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10117v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10117v1)

**Summary:** Large Language Models (LLMs) often provide chain-of-thought (CoT) reasoning traces that appear plausible, but may hide internal biases. We call these *unverbalized biases*. Monitoring models via their stated reasoning is therefore unreliable, and existing bias evaluations typically require predefined categories and hand-crafted datasets. In this work, we introduce a fully automated, black-box pipeline for detecting task-specific unverbalized biases. Given a task dataset, the pipeline uses LLM au...

---

### 2. Olaf-World: Orienting Latent Actions for Video World Modeling

**Authors:** Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10104v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10104v1)

**Summary:** Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, the...

---

### 3. Step-resolved data attribution for looped transformers

**Authors:** Georgios Kaissis, David Mildenberger, Juan Felipe Gomez, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10097v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10097v1)

**Summary:** We study how individual training examples shape the internal computation of looped transformers, where a shared block is applied for $τ$ recurrent iterations to enable latent reasoning. Existing training-data influence estimators such as TracIn yield a single scalar score that aggregates over all loop iterations, obscuring when during the recurrent computation a training example matters. We introduce \textit{Step-Decomposed Influence (SDI)}, which decomposes TracIn into a length-$τ$ influence tr...

---

### 4. Causality in Video Diffusers is Separable from Denoising

**Authors:** Xingjian Bai, Guande He, Zhengqi Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10095v1)

**Summary:** Causality -- referring to temporal, uni-directional cause-effect relationships between components -- underlies many complex generative processes, including videos, language, and robot trajectories. Current causal diffusion models entangle temporal reasoning with iterative denoising, applying causal attention across all layers, at every denoising step, and over the entire context. In this paper, we show that the causal reasoning in these models is separable from the multi-step denoising process. ...

---

### 5. Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

**Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10090v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10090v1)

**Summary:** Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (...

---

### 6. CODE-SHARP: Continuous Open-ended Discovery and Evolution of Skills as Hierarchical Reward Programs

**Authors:** Richard Bornemann, Pierluigi Vito Amadori, Antoine Cully

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10085v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10085v1)

**Summary:** Developing agents capable of open-endedly discovering and learning novel skills is a grand challenge in Artificial Intelligence. While reinforcement learning offers a powerful framework for training agents to master complex skills, it typically relies on hand-designed reward functions. This is infeasible for open-ended skill discovery, where the set of meaningful skills is not known a priori. While recent methods have shown promising results towards automating reward function design, they remain...

---

### 7. Anagent For Enhancing Scientific Table & Figure Analysis

**Authors:** Xuehang Guo, Zhiyong Lu, Tom Hope, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10081v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10081v1)

**Summary:** In scientific research, analysis requires accurately interpreting complex multimodal knowledge, integrating evidence from different sources, and drawing inferences grounded in domain-specific knowledge. However, current artificial intelligence (AI) systems struggle to consistently demonstrate such capabilities. The complexity and variability of scientific tables and figures, combined with heterogeneous structures and long-context requirements, pose fundamental obstacles to scientific table \& fi...

---

### 8. Chain of Mindset: Reasoning with Adaptive Cognitive Modes

**Authors:** Tianyi Jiang, Arctanx An, Hengyi Feng, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10063v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10063v1)

**Summary:** Human problem-solving is never the repetition of a single mindset, by which we mean a distinct mode of cognitive processing. When tackling a specific task, we do not rely on a single mindset; instead, we integrate multiple mindsets within the single solution process. However, existing LLM reasoning methods fall into a common trap: they apply the same fixed mindset across all steps, overlooking that different stages of solving the same problem require fundamentally different mindsets. This single...

---

### 9. Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization

**Authors:** Xinchen Han, Hossam Afifi, Michel Marot, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10048v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10048v1)

**Summary:** Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) reasoning that increases computational costs and latency without proportional performance gains. In this paper, we propose \textbf{F}ine-grained \textbf{G}roup policy \textbf{O}ptimization (\textbf{FGO}), a Reinforcement Learning (RL) algorithm that refines group responses by subdividing them and assigning appropriate weights based on length and entropy, thereby enabling effective CoT compression. Meanwhile,...

---

### 10. Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning

**Authors:** Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10044v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10044v1)

**Summary:** Efficient exploration remains a central challenge in reinforcement learning (RL), particularly in sparse-reward environments. We introduce Optimistic World Models (OWMs), a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likelihood estimation (RBMLE) from adaptive control into deep RL. In contrast to upper confidence bound (UCB)-style exploration methods, OWMs incorporate optimism directly into model learning by augmentation with an optimi...

---

### 11. Fake-HR1: Rethinking reasoning of vision language model for synthetic image detection

**Authors:** Changjiang Jiang, Xinkuan Sha, Fengchang Yu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10042v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10042v1)

**Summary:** Recent studies have demonstrated that incorporating Chain-of-Thought (CoT) reasoning into the detection process can enhance a model's ability to detect synthetic images. However, excessively lengthy reasoning incurs substantial resource overhead, including token consumption and latency, which is particularly redundant when handling obviously generated forgeries. To address this issue, we propose Fake-HR1, a large-scale hybrid-reasoning model that, to the best of our knowledge, is the first to ad...

---

### 12. Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference

**Authors:** Wenxuan Xie, Yujia Wang, Xin Tan, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10021v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10021v1)

**Summary:** The integration of extensive, dynamic knowledge into Large Language Models (LLMs) remains a significant challenge due to the inherent entanglement of factual data and reasoning patterns. Existing solutions, ranging from non-parametric Retrieval-Augmented Generation (RAG) to parametric knowledge editing, are often constrained in practice by finite context windows, retriever noise, or the risk of catastrophic forgetting. In this paper, we propose DRIFT, a novel dual-model architecture designed to ...

---

### 13. ADORA: Training Reasoning Models with Dynamic Advantage Estimation on Reinforcement Learning

**Authors:** Qingnan Ren, Shiting Huang, Zhen Fang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10019v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10019v1)

**Summary:** Reinforcement learning has become a cornerstone technique for developing reasoning models in complex tasks, ranging from mathematical problem-solving to imaginary reasoning. The optimization of these models typically relies on policy gradient methods, whose efficacy hinges on the accurate estimation of an advantage function. However, prevailing methods typically employ static advantage estimation, a practice that leads to inefficient credit assignment by neglecting the dynamic utility of trainin...

---

### 14. Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design

**Authors:** Bojian Hou, Xiaolong Liu, Xiaoyi Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10016v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10016v1)

**Summary:** Deriving predictable scaling laws that govern the relationship between model performance and computational investment is crucial for designing and allocating resources in massive-scale recommendation systems. While such laws are established for large language models, they remain challenging for recommendation systems, especially those processing both user history and context features. We identify poor scaling efficiency as the main barrier to predictable power-law scaling, stemming from ineffici...

---

### 15. RoboSubtaskNet: Temporal Sub-task Segmentation for Human-to-Robot Skill Transfer in Real-World Environments

**Authors:** Dharmendra Sharma, Archit Sharma, John Reberio, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10015v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10015v1)

**Summary:** Temporally locating and classifying fine-grained sub-task segments in long, untrimmed videos is crucial to safe human-robot collaboration. Unlike generic activity recognition, collaborative manipulation requires sub-task labels that are directly robot-executable. We present RoboSubtaskNet, a multi-stage human-to-robot sub-task segmentation framework that couples attention-enhanced I3D features (RGB plus optical flow) with a modified MS-TCN employing a Fibonacci dilation schedule to capture bette...

---

### 16. Discovering High Level Patterns from Simulation Traces

**Authors:** Sean Memery, Kartic Subr

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10009v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10009v1)

**Summary:** Artificial intelligence (AI) agents embedded in environments with physics-based interaction face many challenges including reasoning, planning, summarization, and question answering. This problem is exacerbated when a human user wishes to either guide or interact with the agent in natural language. Although the use of Language Models (LMs) is the default choice, as an AI tool, they struggle with tasks involving physics. The LM's capability for physical reasoning is learned from observational dat...

---

### 17. A Collaborative Safety Shield for Safe and Efficient CAV Lane Changes in Congested On-Ramp Merging

**Authors:** Bharathkumar Hegde, Melanie Bouroche

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10007v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10007v1)

**Summary:** Lane changing in dense traffic is a significant challenge for Connected and Autonomous Vehicles (CAVs). Existing lane change controllers primarily either ensure safety or collaboratively improve traffic efficiency, but do not consider these conflicting objectives together. To address this, we propose the Multi-Agent Safety Shield (MASS), designed using Control Barrier Functions (CBFs) to enable safe and collaborative lane changes. The MASS enables collaboration by capturing multi-agent interacti...

---

### 18. ESTAR: Early-Stopping Token-Aware Reasoning For Efficient Inference

**Authors:** Junda Wang, Zhichao Yang, Dongxu Zhang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10004v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10004v1)

**Summary:** Large reasoning models (LRMs) achieve state-of-the-art performance by generating long chains-of-thought, but often waste computation on redundant reasoning after the correct answer has already been reached. We introduce Early-Stopping for Token-Aware Reasoning (ESTAR), which detects and reduces such reasoning redundancy to improve efficiency without sacrificing accuracy. Our method combines (i) a trajectory-based classifier that identifies when reasoning can be safely stopped, (ii) supervised fi...

---

### 19. A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models

**Authors:** Xiulin Yang, Arianna Bisazza, Nathan Schneider, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09992v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09992v1)

**Summary:** How can children acquire native-level syntax from limited input? According to the Poverty of the Stimulus Hypothesis (PoSH), the linguistic input children receive is insufficient to explain certain generalizations that are robustly learned; innate linguistic constraints, many have argued, are thus necessary to explain language learning. Neural language models, which lack such language-specific constraints in their design, offer a computational test of this longstanding (but controversial) claim....

---

### 20. Empirical Stability Analysis of Kolmogorov-Arnold Networks in Hard-Constrained Recurrent Physics-Informed Discovery

**Authors:** Enzo Nicolas Spotorno, Josafat Leal Filho, Antonio Augusto Medeiros Frohlich

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09988v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09988v1)

**Summary:** We investigate the integration of Kolmogorov-Arnold Networks (KANs) into hard-constrained recurrent physics-informed architectures (HRPINN) to evaluate the fidelity of learned residual manifolds in oscillatory systems. Motivated by the Kolmogorov-Arnold representation theorem and preliminary gray-box results, we hypothesized that KANs would enable efficient recovery of unknown terms compared to MLPs. Through initial sensitivity analysis on configuration sensitivity, parameter scale, and training...

---

### 21. Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions

**Authors:** J Rosser, Robert Kirk, Edward Grefenstette, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09987v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09987v1)

**Summary:** Influence functions are commonly used to attribute model behavior to training documents. We explore the reverse: crafting training data that induces model behavior. Our framework, Infusion, uses scalable influence-function approximations to compute small perturbations to training documents that induce targeted changes in model behavior through parameter shifts. We evaluate Infusion on data poisoning tasks across vision and language domains. On CIFAR-10, we show that making subtle edits via Infus...

---

### 22. Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings

**Authors:** Alexander Fertig, Karthikeyan Chandra Sekaran, Lakshman Balasubramanian, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09985v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09985v1)

**Summary:** As autonomous vehicles are rolled out, measures must be taken to ensure their safe operation. In order to supervise a system that is already in operation, monitoring frameworks are frequently employed. These run continuously online in the background, supervising the system status and recording anomalies. This work proposes an online monitoring framework to detect anomalies in object state representations. Thereby, a key challenge is creating a framework for anomaly detection without anomaly labe...

---

### 23. Coupled Inference in Diffusion Models for Semantic Decomposition

**Authors:** Calvin Yeung, Ali Zakeri, Zhuowen Zou, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09983v1)

**Summary:** Many visual scenes can be described as compositions of latent factors. Effective recognition, reasoning, and editing often require not only forming such compositional representations, but also solving the decomposition problem. One popular choice for constructing these representations is through the binding operation. Resonator networks, which can be understood as coupled Hopfield networks, were proposed as a way to perform decomposition on such bound representations. Recent works have shown not...

---

### 24. Supervised Metric Regularization Through Alternating Optimization for Multi-Regime Physics-Informed Neural Networks

**Authors:** Enzo Nicolas Spotorno, Josafat Ribeiro Leal, Antonio Augusto Frohlich

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09980v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09980v1)

**Summary:** Standard Physics-Informed Neural Networks (PINNs) often face challenges when modeling parameterized dynamical systems with sharp regime transitions, such as bifurcations. In these scenarios, the continuous mapping from parameters to solutions can result in spectral bias or "mode collapse", where the network averages distinct physical behaviors. We propose a Topology-Aware PINN (TAPINN) that aims to mitigate this challenge by structuring the latent space via Supervised Metric Regularization. Unli...

---

### 25. Drug Release Modeling using Physics-Informed Neural Networks

**Authors:** Daanish Aleem Qureshi, Khemraj Shukla, Vikas Srivastava

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09963v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09963v1)

**Summary:** Accurate modeling of drug release is essential for designing and developing controlled-release systems. Classical models (Fick, Higuchi, Peppas) rely on simplifying assumptions that limit their accuracy in complex geometries and release mechanisms. Here, we propose a novel approach using Physics-Informed Neural Networks (PINNs) and Bayesian PINNs (BPINNs) for predicting release from planar, 1D-wrinkled, and 2D-crumpled films. This approach uniquely integrates Fick's diffusion law with limited ex...

---

### 26. Bladder Vessel Segmentation using a Hybrid Attention-Convolution Framework

**Authors:** Franziska Krauß, Matthias Ege, Zoltan Lovasz, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09949v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09949v1)

**Summary:** Urinary bladder cancer surveillance requires tracking tumor sites across repeated interventions, yet the deformable and hollow bladder lacks stable landmarks for orientation. While blood vessels visible during endoscopy offer a patient-specific "vascular fingerprint" for navigation, automated segmentation is challenged by imperfect endoscopic data, including sparse labels, artifacts like bubbles or variable lighting, continuous deformation, and mucosal folds that mimic vessels. State-of-the-art ...

---

### 27. Closing Reasoning Gaps in Clinical Agents with Differential Reasoning Learning

**Authors:** Jinsong Liu, Yuhang Jiang, Ramayya Krishnan, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09945v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09945v1)

**Summary:** Clinical decision support requires not only correct answers but also clinically valid reasoning. We propose Differential Reasoning Learning (DRL), a framework that improves clinical agents by learning from reasoning discrepancies. From reference reasoning rationales (e.g., physician-authored clinical rationale, clinical guidelines, or outputs from more capable models) and the agent's free-form chain-of-thought (CoT), DRL extracts reasoning graphs as directed acyclic graphs (DAGs) and performs a ...

---

### 28. Instruct2Act: From Human Instruction to Actions Sequencing and Execution via Robot Action Network for Robotic Manipulation

**Authors:** Archit Sharma, Dharmendra Sharma, John Rebeiro, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09940v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09940v1)

**Summary:** Robots often struggle to follow free-form human instructions in real-world settings due to computational and sensing limitations. We address this gap with a lightweight, fully on-device pipeline that converts natural-language commands into reliable manipulation. Our approach has two stages: (i) the instruction to actions module (Instruct2Act), a compact BiLSTM with a multi-head-attention autoencoder that parses an instruction into an ordered sequence of atomic actions (e.g., reach, grasp, move, ...

---

### 29. Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?

**Authors:** Taeyoon Kim, Woohyeok Park, Hoyeong Yun, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09937v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09937v1)

**Summary:** Failures in large-scale cloud systems incur substantial financial losses, making automated Root Cause Analysis (RCA) essential for operational stability. Recent efforts leverage Large Language Model (LLM) agents to automate this task, yet existing systems exhibit low detection accuracy even with capable models, and current evaluation frameworks assess only final answer correctness without revealing why the agent's reasoning failed. This paper presents a process level failure analysis of LLM-base...

---

### 30. Unbalanced optimal transport for robust longitudinal lesion evolution with registration-aware and appearance-guided priors

**Authors:** Melika Qahqaie, Dominik Neumann, Tobias Heimann, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09933v1)

**Summary:** Evaluating lesion evolution in longitudinal CT scans of can cer patients is essential for assessing treatment response, yet establishing reliable lesion correspondence across time remains challenging. Standard bipartite matchers, which rely on geometric proximity, struggle when lesions appear, disappear, merge, or split. We propose a registration-aware matcher based on unbalanced optimal transport (UOT) that accommodates unequal lesion mass and adapts priors to patient-level tumor-load changes. ...

---

### 31. Monocular Normal Estimation via Shading Sequence Estimation

**Authors:** Zongrui Li, Xinhua Ma, Minghui Hu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09929v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09929v1)

**Summary:** Monocular normal estimation aims to estimate the normal map from a single RGB image of an object under arbitrary lights. Existing methods rely on deep models to directly predict normal maps. However, they often suffer from 3D misalignment: while the estimated normal maps may appear to have a correct appearance, the reconstructed surfaces often fail to align with the geometric details. We argue that this misalignment stems from the current paradigm: the model struggles to distinguish and reconstr...

---

### 32. LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

**Authors:** William Lugoloobi, Thomas Foster, William Bankes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09924v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09924v1)

**Summary:** Running LLMs with extended reasoning on every problem is expensive, but determining which inputs actually require additional compute remains challenging. We investigate whether their own likelihood of success is recoverable from their internal representations before generation, and if this signal can guide more efficient inference. We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as...

---

### 33. SARS: A Novel Face and Body Shape and Appearance Aware 3D Reconstruction System extends Morphable Models

**Authors:** Gulraiz Khan, Kenneth Y. Wertheim, Kevin Pimbblet, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09918v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09918v1)

**Summary:** Morphable Models (3DMMs) are a type of morphable model that takes 2D images as inputs and recreates the structure and physical appearance of 3D objects, especially human faces and bodies. 3DMM combines identity and expression blendshapes with a basic face mesh to create a detailed 3D model. The variability in the 3D Morphable models can be controlled by tuning diverse parameters. They are high-level image descriptors, such as shape, texture, illumination, and camera parameters. Previous research...

---

### 34. Self-Regulated Reading with AI Support: An Eight-Week Study with Students

**Authors:** Yue Fu, Joel Wester, Niels Van Berkel, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09907v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09907v1)

**Summary:** College students increasingly use AI chatbots to support academic reading, yet we lack granular understanding of how these interactions shape their reading experience and cognitive engagement. We conducted an eight-week longitudinal study with 15 undergraduates who used AI to support assigned readings in a course. We collected 838 prompts across 239 reading sessions and developed a coding schema categorizing prompts into four cognitive themes: Decoding, Comprehension, Reasoning, and Metacognitio...

---

### 35. Routing, Cascades, and User Choice for LLMs

**Authors:** Rafid Mahmood

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09902v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09902v1)

**Summary:** To mitigate the trade-offs between performance and costs, LLM providers route user tasks to different models based on task difficulty and latency. We study the effect of LLM routing with respect to user behavior. We propose a game between an LLM provider with two models (standard and reasoning) and a user who can re-prompt or abandon tasks if the routed model cannot solve them. The user's goal is to maximize their utility minus the delay from using the model, while the provider minimizes the cos...

---

### 36. TaCo: A Benchmark for Lossless and Lossy Codecs of Heterogeneous Tactile Data

**Authors:** Zhengxue Cheng, Yan Zhao, Keyu Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09893v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09893v1)

**Summary:** Tactile sensing is crucial for embodied intelligence, providing fine-grained perception and control in complex environments. However, efficient tactile data compression, which is essential for real-time robotic applications under strict bandwidth constraints, remains underexplored. The inherent heterogeneity and spatiotemporal complexity of tactile data further complicate this challenge. To bridge this gap, we introduce TaCo, the first comprehensive benchmark for Tactile data Codecs. TaCo evalua...

---

### 37. Code2World: A GUI World Model via Renderable Code Generation

**Authors:** Yuhao Zheng, Li'an Zhong, Yi Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09856v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09856v1)

**Summary:** Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generat...

---

### 38. Hybrid Responsible AI-Stochastic Approach for SLA Compliance in Multivendor 6G Networks

**Authors:** Emanuel Figetakis, Ahmed Refaey Hussein

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09841v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09841v1)

**Summary:** The convergence of AI and 6G network automation introduces new challenges in maintaining transparency, fairness, and accountability across multivendor management systems. Although closed-loop AI orchestration improves adaptability and self-optimization, it also creates a responsibility gap, where violations of SLAs cannot be causally attributed to specific agents or vendors. This paper presents a hybrid responsible AI-stochastic learning framework that embeds fairness, robustness, and auditabili...

---

### 39. Text summarization via global structure awareness

**Authors:** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09821v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09821v1)

**Summary:** Text summarization is a fundamental task in natural language processing (NLP), and the information explosion has made long-document processing increasingly demanding, making summarization essential. Existing research mainly focuses on model improvements and sentence-level pruning, but often overlooks global structure, leading to disrupted coherence and weakened downstream performance. Some studies employ large language models (LLMs), which achieve higher accuracy but incur substantial resource a...

---

### 40. Efficient Unsupervised Environment Design through Hierarchical Policy Representation Learning

**Authors:** Dexun Li, Sidney Tio, Pradeep Varakantham

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09813v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09813v1)

**Summary:** Unsupervised Environment Design (UED) has emerged as a promising approach to developing general-purpose agents through automated curriculum generation. Popular UED methods focus on Open-Endedness, where teacher algorithms rely on stochastic processes for infinite generation of useful environments. This assumption becomes impractical in resource-constrained scenarios where teacher-student interaction opportunities are limited. To address this challenge, we introduce a hierarchical Markov Decision...

---

### 41. A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer

**Authors:** Azka Nasir, Fatima Dossa, Muhammad Ahmed Atif, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09810v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09810v1)

**Summary:** Transfer learning in deep reinforcement learning is often motivated by improved stability and reduced training cost, but it can also fail under substantial domain shift. This paper presents a controlled empirical study examining how architectural differences between Double Deep Q-Networks (DDQN) and Dueling DQN influence transfer behavior across environments. Using CartPole as a source task and LunarLander as a structurally distinct target task, we evaluate a fixed layer-wise representation tran...

---

### 42. Decomposing Reasoning Efficiency in Large Language Models

**Authors:** Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09805v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09805v1)

**Summary:** Large language models trained for reasoning trade off inference tokens against accuracy, yet standard evaluations report only final accuracy, obscuring where tokens are spent or wasted. We introduce a trace-optional framework that decomposes token efficiency into interpretable factors: completion under a fixed token budget (avoiding truncation), conditional correctness given completion, and verbosity (token usage). When benchmark metadata provides per-instance workload proxies, we further factor...

---

### 43. Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices

**Authors:** Manon Reusens, Sofie Goethals, Toon Calders, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09802v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09802v1)

**Summary:** As Large Language Models (LLMs) are increasingly deployed in applications such as travel assistance and purchasing support, they are often required to make subjective choices on behalf of users in settings where no objectively correct answer exists. We study LLM decision-making in a travel-assistant context by presenting models with choice dilemmas and analyzing their responses using multinomial logit models to derive implied willingness to pay (WTP) estimates. These WTP values are subsequently ...

---

### 44. Symbolic Pattern Temporal Numeric Planning with Intermediate Conditions and Effects

**Authors:** Matteo Cardellini, Enrico Giunchiglia

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09798v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09798v1)

**Summary:** Recently, a Symbolic Pattern Planning (SPP) approach was proposed for numeric planning where a pattern (i.e., a finite sequence of actions) suggests a causal order between actions. The pattern is then encoded in a SMT formula whose models correspond to valid plans. If the suggestion by the pattern is inaccurate and no valid plan can be found, the pattern is extended until it contains the causal order of actions in a valid plan, making the approach complete. In this paper, we extend the SPP appro...

---

### 45. GHS-TDA: A Synergistic Reasoning Framework Integrating Global Hypothesis Space with Topological Data Analysis

**Authors:** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09794v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09794v1)

**Summary:** Chain-of-Thought (CoT) has been shown to significantly improve the reasoning accuracy of large language models (LLMs) on complex tasks. However, due to the autoregressive, step-by-step generation paradigm, existing CoT methods suffer from two fundamental limitations. First, the reasoning process is highly sensitive to early decisions: once an initial error is introduced, it tends to propagate and amplify through subsequent steps, while the lack of a global coordination and revision mechanism mak...

---

### 46. Flexible Entropy Control in RLVR with Gradient-Preserving Perspective

**Authors:** Kun Chen, Peng Shi, Fanfan Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09782v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09782v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a critical method for enhancing the reasoning capabilities of Large Language Models (LLMs). However, continuous training often leads to policy entropy collapse, characterized by a rapid decay in entropy that results in premature overconfidence, reduced output diversity, and vanishing gradient norms that inhibit learning. Gradient-Preserving Clipping is a primary factor influencing these dynamics, but existing mitigation strateg...

---

### 47. Explainability in Generative Medical Diffusion Models: A Faithfulness-Based Analysis on MRI Synthesis

**Authors:** Surjo Dey, Pallabi Saikia

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09781v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09781v1)

**Summary:** This study investigates the explainability of generative diffusion models in the context of medical imaging, focusing on Magnetic resonance imaging (MRI) synthesis. Although diffusion models have shown strong performance in generating realistic medical images, their internal decision making process remains largely opaque. We present a faithfulness-based explainability framework that analyzes how prototype-based explainability methods like ProtoPNet (PPNet), Enhanced ProtoPNet (EPPNet), and Proto...

---

### 48. Grounding LTL Tasks in Sub-Symbolic RL Environments for Zero-Shot Generalization

**Authors:** Matteo Pannacci, Andrea Fanti, Elena Umili, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09761v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09761v1)

**Summary:** In this work we address the problem of training a Reinforcement Learning agent to follow multiple temporally-extended instructions expressed in Linear Temporal Logic in sub-symbolic environments. Previous multi-task work has mostly relied on knowledge of the mapping between raw observations and symbols appearing in the formulae. We drop this unrealistic assumption by jointly training a multi-task policy and a symbol grounder with the same experience. The symbol grounder is trained only from raw ...

---

### 49. ExO-PPO: an Extended Off-policy Proximal Policy Optimization Algorithm

**Authors:** Hanyong Wang, Menglong Yang

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09726v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09726v1)

**Summary:** Deep reinforcement learning has been able to solve various tasks successfully, however, due to the construction of policy gradient and training dynamics, tuning deep reinforcement learning models remains challenging. As one of the most successful deep reinforcement-learning algorithm, the Proximal Policy Optimization algorithm (PPO) clips the policy gradient within a conservative on-policy updates, which ensures reliable and stable policy improvement. However, this training pattern may sacrifice...

---

### 50. From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet

**Authors:** Radib Bin Kabir, Tawsif Tashwar Dipto, Mehedi Ahamed, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09717v1)

**Summary:** Spiking Neural Networks (SNNs) are increasingly studied as energy-efficient alternatives to Convolutional Neural Networks (CNNs), particularly for edge intelligence. However, prior work has largely emphasized large-scale models, leaving the design and evaluation of lightweight CNN-to-SNN pipelines underexplored. In this paper, we present the first systematic benchmark of lightweight SNNs obtained by converting compact CNN architectures into spiking networks, where activations are modeled with Le...

---

## cs.CL

**50 papers**

### 1. Quantum-Audit: Evaluating the Reasoning Limits of LLMs on Quantum Computing

**Authors:** Mohamed Afane, Kayla Laufer, Wenqi Wei, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10092v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10092v1)

**Summary:** Language models have become practical tools for quantum computing education and research, from summarizing technical papers to explaining theoretical concepts and answering questions about recent developments in the field. While existing benchmarks evaluate quantum code generation and circuit design, their understanding of quantum computing concepts has not been systematically measured. Quantum-Audit addresses this gap with 2,700 questions covering core quantum computing topics. We evaluate 26 m...

---

### 2. Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

**Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10090v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10090v1)

**Summary:** Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (...

---

### 3. Anagent For Enhancing Scientific Table & Figure Analysis

**Authors:** Xuehang Guo, Zhiyong Lu, Tom Hope, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10081v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10081v1)

**Summary:** In scientific research, analysis requires accurately interpreting complex multimodal knowledge, integrating evidence from different sources, and drawing inferences grounded in domain-specific knowledge. However, current artificial intelligence (AI) systems struggle to consistently demonstrate such capabilities. The complexity and variability of scientific tables and figures, combined with heterogeneous structures and long-context requirements, pose fundamental obstacles to scientific table \& fi...

---

### 4. CAPID: Context-Aware PII Detection for Question-Answering Systems

**Authors:** Mariia Ponomarenko, Sepideh Abedini, Masoumeh Shafieinejad, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10074v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10074v1)

**Summary:** Detecting personally identifiable information (PII) in user queries is critical for ensuring privacy in question-answering systems. Current approaches mainly redact all PII, disregarding the fact that some of them may be contextually relevant to the user's question, resulting in a degradation of response quality. Large language models (LLMs) might be able to help determine which PII are relevant, but due to their closed source nature and lack of privacy guarantees, they are unsuitable for sensit...

---

### 5. Overview of the TREC 2025 RAGTIME Track

**Authors:** Dawn Lawrie, Sean MacAvaney, James Mayfield, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10024v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10024v1)

**Summary:** The principal goal of the RAG TREC Instrument for Multilingual Evaluation (RAGTIME) track at TREC is to study report generation from multilingual source documents. The track has created a document collection containing Arabic, Chinese, English, and Russian news stories. RAGTIME includes three task types: Multilingual Report Generation, English Report Generation, and Multilingual Information Retrieval (MLIR). A total of 125 runs were submitted by 13 participating teams (and as baselines by the tr...

---

### 6. MEVER: Multi-Modal and Explainable Claim Verification with Graph-based Evidence Retrieval

**Authors:** Delvin Ce Zhang, Suhan Cui, Zhelin Chu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10023v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10023v1)

**Summary:** Verifying the truthfulness of claims usually requires joint multi-modal reasoning over both textual and visual evidence, such as analyzing both textual caption and chart image for claim verification. In addition, to make the reasoning process transparent, a textual explanation is necessary to justify the verification result. However, most claim verification works mainly focus on the reasoning over textual evidence only or ignore the explainability, resulting in inaccurate and unconvincing verifi...

---

### 7. Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference

**Authors:** Wenxuan Xie, Yujia Wang, Xin Tan, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10021v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10021v1)

**Summary:** The integration of extensive, dynamic knowledge into Large Language Models (LLMs) remains a significant challenge due to the inherent entanglement of factual data and reasoning patterns. Existing solutions, ranging from non-parametric Retrieval-Augmented Generation (RAG) to parametric knowledge editing, are often constrained in practice by finite context windows, retriever noise, or the risk of catastrophic forgetting. In this paper, we propose DRIFT, a novel dual-model architecture designed to ...

---

### 8. SCORE: Specificity, Context Utilization, Robustness, and Relevance for Reference-Free LLM Evaluation

**Authors:** Homaira Huda Shomee, Rochana Chaturvedi, Yangxinyu Xie, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10017v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10017v1)

**Summary:** Large language models (LLMs) are increasingly used to support question answering and decision-making in high-stakes, domain-specific settings such as natural hazard response and infrastructure planning, where effective answers must convey fine-grained, decision-critical details. However, existing evaluation frameworks for retrieval-augmented generation (RAG) and open-ended question answering primarily rely on surface-level similarity, factual consistency, or semantic relevance, and often fail to...

---

### 9. ViSpeechFormer: A Phonemic Approach for Vietnamese Automatic Speech Recognition

**Authors:** Khoa Anh Nguyen, Long Minh Hoang, Nghia Hieu Nguyen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10003v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10003v1)

**Summary:** Vietnamese has a phonetic orthography, where each grapheme corresponds to at most one phoneme and vice versa. Exploiting this high grapheme-phoneme transparency, we propose ViSpeechFormer (\textbf{Vi}etnamese \textbf{Speech} Trans\textbf{Former}), a phoneme-based approach for Vietnamese Automatic Speech Recognition (ASR). To the best of our knowledge, this is the first Vietnamese ASR framework that explicitly models phonemic representations. Experiments on two publicly available Vietnamese ASR d...

---

### 10. A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models

**Authors:** Xiulin Yang, Arianna Bisazza, Nathan Schneider, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09992v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09992v1)

**Summary:** How can children acquire native-level syntax from limited input? According to the Poverty of the Stimulus Hypothesis (PoSH), the linguistic input children receive is insufficient to explain certain generalizations that are robustly learned; innate linguistic constraints, many have argued, are thus necessary to explain language learning. Neural language models, which lack such language-specific constraints in their design, offer a computational test of this longstanding (but controversial) claim....

---

### 11. ViMultiChoice: Toward a Method That Gives Explanation for Multiple-Choice Reading Comprehension in Vietnamese

**Authors:** Trung Tien Cao, Lam Minh Thai, Nghia Hieu Nguyen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09961v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09961v1)

**Summary:** Multiple-choice Reading Comprehension (MCRC) models aim to select the correct answer from a set of candidate options for a given question. However, they typically lack the ability to explain the reasoning behind their choices. In this paper, we introduce a novel Vietnamese dataset designed to train and evaluate MCRC models with explanation generation capabilities. Furthermore, we propose ViMultiChoice, a new method specifically designed for modeling Vietnamese reading comprehension that jointly ...

---

### 12. ATTNPO: Attention-Guided Process Supervision for Efficient Reasoning

**Authors:** Shuaiyi Nie, Siyu Ding, Wenyuan Zhang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09953v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09953v1)

**Summary:** Large reasoning models trained with reinforcement learning and verifiable rewards (RLVR) achieve strong performance on complex reasoning tasks, yet often overthink, generating redundant reasoning without performance gains. Existing trajectory-level length penalties often fail to effectively shorten reasoning length and degrade accuracy, as they uniformly treat all reasoning steps and lack fine-grained signals to distinguish redundancy from necessity. Meanwhile, process-supervised methods are typ...

---

### 13. LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

**Authors:** William Lugoloobi, Thomas Foster, William Bankes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09924v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09924v1)

**Summary:** Running LLMs with extended reasoning on every problem is expensive, but determining which inputs actually require additional compute remains challenging. We investigate whether their own likelihood of success is recoverable from their internal representations before generation, and if this signal can guide more efficient inference. We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as...

---

### 14. AmharicIR+Instr: A Two-Dataset Resource for Neural Retrieval and Instruction Tuning

**Authors:** Tilahun Yeshambel, Moncef Garouani, Josiane Mothe

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09914v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09914v1)

**Summary:** Neural retrieval and GPT-style generative models rely on large, high-quality supervised data, which is still scarce for low-resource languages such as Amharic. We release an Amharic data resource consisting of two datasets that supports research on (i) neural retrieval-ranking and (ii) instruction-following text generation. The retrieval-ranking dataset contains 1,091 manually verified query-positive-negative document triplets drawn from diverse Amharic sources and constructed to support contras...

---

### 15. QP-OneModel: A Unified Generative LLM for Multi-Task Query Understanding in Xiaohongshu Search

**Authors:** Jianzhao Huang, Xiaorui Huang, Fei Zhao, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09901v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09901v1)

**Summary:** Query Processing (QP) bridges user intent and content supply in large-scale Social Network Service (SNS) search engines. Traditional QP systems rely on pipelines of isolated discriminative models (e.g., BERT), suffering from limited semantic understanding and high maintenance overhead. While Large Language Models (LLMs) offer a potential solution, existing approaches often optimize sub-tasks in isolation, neglecting intrinsic semantic synergy and necessitating independent iterations. Moreover, s...

---

### 16. The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies

**Authors:** Chenxu Wang, Chaozhuo Li, Songyang Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09877v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09877v1)

**Summary:** The emergence of multi-agent systems built from large language models (LLMs) offers a promising paradigm for scalable collective intelligence and self-evolution. Ideally, such systems would achieve continuous self-improvement in a fully closed loop while maintaining robust safety alignment--a combination we term the self-evolution trilemma. However, we demonstrate both theoretically and empirically that an agent society satisfying continuous self-evolution, complete isolation, and safety invaria...

---

### 17. Steer2Edit: From Activation Steering to Component-Level Editing

**Authors:** Chung-En Sun, Ge Yan, Zimo Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09870v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09870v1)

**Summary:** Steering methods influence Large Language Model behavior by identifying semantic directions in hidden representations, but are typically realized through inference-time activation interventions that apply a fixed, global modification to the model's internal states. While effective, such interventions often induce unfavorable attribute-utility trade-offs under strong control, as they ignore the fact that many behaviors are governed by a small and heterogeneous subset of model components. We propo...

---

### 18. Code2World: A GUI World Model via Renderable Code Generation

**Authors:** Yuhao Zheng, Li'an Zhong, Yi Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09856v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09856v1)

**Summary:** Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generat...

---

### 19. How Do People Quantify Naturally: Evidence from Mandarin Picture Description

**Authors:** Yayun Zhang, Guanyi Chen, Fahime Same, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09838v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09838v1)

**Summary:** Quantification is a fundamental component of everyday language use, yet little is known about how speakers decide whether and how to quantify in naturalistic production. We investigate quantification in Mandarin Chinese using a picture-based elicited description task in which speakers freely described scenes containing multiple objects, without explicit instructions to count or quantify. Across both spoken and written modalities, we examine three aspects of quantification: whether speakers choos...

---

### 20. LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse

**Authors:** Bakhtawar Ahtisham, Kirk Vanacore, Zhuqian Zhou, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09832v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09832v1)

**Summary:** Large Language Models (LLMs) are increasingly deployed to automatically label and analyze educational dialogue at scale, yet current pipelines lack reliable ways to detect when models are wrong. We investigate whether reasoning generated by LLMs can be used to predict the correctness of a model's own predictions. We analyze 30,300 teacher utterances from classroom dialogue, each labeled by multiple state-of-the-art LLMs with an instructional move construct and an accompanying reasoning. Using hu...

---

### 21. From FusHa to Folk: Exploring Cross-Lingual Transfer in Arabic Language Models

**Authors:** Abdulmuizz Khalak, Abderrahmane Issam, Gerasimos Spanakis

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09826v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09826v1)

**Summary:** Arabic Language Models (LMs) are pretrained predominately on Modern Standard Arabic (MSA) and are expected to transfer to its dialects. While MSA as the standard written variety is commonly used in formal settings, people speak and write online in various dialects that are spread across the Arab region. This poses limitations for Arabic LMs, since its dialects vary in their similarity to MSA. In this work we study cross-lingual transfer of Arabic models using probing on 3 Natural Language Proces...

---

### 22. Covo-Audio Technical Report

**Authors:** Wenfu Wang, Chenxing Li, Liqiang Zhang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09823v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09823v1)

**Summary:** In this work, we present Covo-Audio, a 7B-parameter end-to-end LALM that directly processes continuous audio inputs and generates audio outputs within a single unified architecture. Through large-scale curated pretraining and targeted post-training, Covo-Audio achieves state-of-the-art or competitive performance among models of comparable scale across a broad spectrum of tasks, including speech-text modeling, spoken dialogue, speech understanding, audio understanding, and full-duplex voice inter...

---

### 23. Text summarization via global structure awareness

**Authors:** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09821v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09821v1)

**Summary:** Text summarization is a fundamental task in natural language processing (NLP), and the information explosion has made long-document processing increasingly demanding, making summarization essential. Existing research mainly focuses on model improvements and sentence-level pruning, but often overlooks global structure, leading to disrupted coherence and weakened downstream performance. Some studies employ large language models (LLMs), which achieve higher accuracy but incur substantial resource a...

---

### 24. AnalyticsGPT: An LLM Workflow for Scientometric Question Answering

**Authors:** Khang Ly, Georgios Cheirmpos, Adrian Raudaschl, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09817v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09817v1)

**Summary:** This paper introduces AnalyticsGPT, an intuitive and efficient large language model (LLM)-powered workflow for scientometric question answering. This underrepresented downstream task addresses the subcategory of meta-scientific questions concerning the "science of science." When compared to traditional scientific question answering based on papers, the task poses unique challenges in the planning phase. Namely, the need for named-entity recognition of academic entities within questions and multi...

---

### 25. Decomposing Reasoning Efficiency in Large Language Models

**Authors:** Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09805v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09805v1)

**Summary:** Large language models trained for reasoning trade off inference tokens against accuracy, yet standard evaluations report only final accuracy, obscuring where tokens are spent or wasted. We introduce a trace-optional framework that decomposes token efficiency into interpretable factors: completion under a fixed token budget (avoiding truncation), conditional correctness given completion, and verbosity (token usage). When benchmark metadata provides per-instance workload proxies, we further factor...

---

### 26. Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices

**Authors:** Manon Reusens, Sofie Goethals, Toon Calders, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09802v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09802v1)

**Summary:** As Large Language Models (LLMs) are increasingly deployed in applications such as travel assistance and purchasing support, they are often required to make subjective choices on behalf of users in settings where no objectively correct answer exists. We study LLM decision-making in a travel-assistant context by presenting models with choice dilemmas and analyzing their responses using multinomial logit models to derive implied willingness to pay (WTP) estimates. These WTP values are subsequently ...

---

### 27. Where Are We At with Automatic Speech Recognition for the Bambara Language?

**Authors:** Seydou Diallo, Yacouba Diarra, Mamadou K. Keita, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09785v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09785v1)

**Summary:** This paper introduces the first standardized benchmark for evaluating Automatic Speech Recognition (ASR) in the Bambara language, utilizing one hour of professionally recorded Malian constitutional text. Designed as a controlled reference set under near-optimal acoustic and linguistic conditions, the benchmark was used to evaluate 37 models, ranging from Bambara-trained systems to large-scale commercial models. Our findings reveal that current ASR performance remains significantly below deployme...

---

### 28. Circuit Fingerprints: How Answer Tokens Encode Their Geometrical Path

**Authors:** Andres Saurez, Neha Sengar, Dongsoo Har

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09784v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09784v1)

**Summary:** Circuit discovery and activation steering in transformers have developed as separate research threads, yet both operate on the same representational space. Are they two views of the same underlying structure? We show they follow a single geometric principle: answer tokens, processed in isolation, encode the directions that would produce them. This Circuit Fingerprint hypothesis enables circuit discovery without gradients or causal intervention -- recovering comparable structure to gradient-based...

---

### 29. Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints

**Authors:** Andres Saurez, Yousung Lee, Dongsoo Har

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09783v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09783v1)

**Summary:** Linear probes and sparse autoencoders consistently recover meaningful structure from transformer representations -- yet why should such simple methods succeed in deep, nonlinear systems? We show this is not merely an empirical regularity but a consequence of architectural necessity: transformers communicate information through linear interfaces (attention OV circuits, unembedding matrices), and any semantic feature decoded through such an interface must occupy a context-invariant linear subspace...

---

### 30. Flexible Entropy Control in RLVR with Gradient-Preserving Perspective

**Authors:** Kun Chen, Peng Shi, Fanfan Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09782v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09782v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a critical method for enhancing the reasoning capabilities of Large Language Models (LLMs). However, continuous training often leads to policy entropy collapse, characterized by a rapid decay in entropy that results in premature overconfidence, reduced output diversity, and vanishing gradient norms that inhibit learning. Gradient-Preserving Clipping is a primary factor influencing these dynamics, but existing mitigation strateg...

---

### 31. Improving Interpretability of Lexical Semantic Change with Neurobiological Features

**Authors:** Kohei Oda, Hiroya Takamura, Kiyoaki Shirai, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09760v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09760v1)

**Summary:** Lexical Semantic Change (LSC) is the phenomenon in which the meaning of a word change over time. Most studies on LSC focus on improving the performance of estimating the degree of LSC, however, it is often difficult to interpret how the meaning of a word change. Enhancing the interpretability of LSC is a significant challenge as it could lead to novel insights in this field. To tackle this challenge, we propose a method to map the semantic space of contextualized embeddings of words obtained by ...

---

### 32. Targum -- A Multilingual New Testament Translation Corpus

**Authors:** Maciej Rapacz, Aleksander Smywiński-Pohl

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09724v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09724v1)

**Summary:** Many European languages possess rich biblical translation histories, yet existing corpora - in prioritizing linguistic breadth - often fail to capture this depth. To address this gap, we introduce a multilingual corpus of 657 New Testament translations, of which 352 are unique, with unprecedented depth in five languages: English (208 unique versions from 396 total), French (41 from 78), Italian (18 from 33), Polish (30 from 48), and Spanish (55 from 102). Aggregated from 12 online biblical libra...

---

### 33. AI-Assisted Scientific Assessment: A Case Study on Climate Change

**Authors:** Christian Buck, Levke Caesar, Michelle Chen Huebscher, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09723v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09723v1)

**Summary:** The emerging paradigm of AI co-scientists focuses on tasks characterized by repeatable verification, where agents explore search spaces in 'guess and check' loops. This paradigm does not extend to problems where repeated evaluation is impossible and ground truth is established by the consensus synthesis of theory and existing evidence. We evaluate a Gemini-based AI environment designed to support collaborative scientific assessment, integrated into a standard scientific workflow. In collaboratio...

---

### 34. Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs

**Authors:** Longhuan Xu, Cunjian Chen, Feng Yin

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09719v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09719v1)

**Summary:** Test-time adaptation (TTA) for large language models (LLMs) updates model parameters at inference time using signals available at deployment. This paper focuses on a common yet under-explored regime: unsupervised, sample-specific TTA, where the model adapts independently for each prompt using only the prompt itself, without gold answers or external supervision. Although appealing, naive unsupervised TTA with a fixed, handcrafted learning rate can be unstable: updates may overfit to prompt-specif...

---

### 35. TraceMem: Weaving Narrative Memory Schemata from User Conversational Traces

**Authors:** Yiming Shu, Pei Liu, Tiange Zhang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09712v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09712v1)

**Summary:** Sustaining long-term interactions remains a bottleneck for Large Language Models (LLMs), as their limited context windows struggle to manage dialogue histories that extend over time. Existing memory systems often treat interactions as disjointed snippets, failing to capture the underlying narrative coherence of the dialogue stream. We propose TraceMem, a cognitively-inspired framework that weaves structured, narrative memory schemata from user conversational traces through a three-stage pipeline...

---

### 36. Maastricht University at AMIYA: Adapting LLMs for Dialectal Arabic using Fine-tuning and MBR Decoding

**Authors:** Abdulhai Alali, Abderrahmane Issam

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09703v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09703v1)

**Summary:** Large Language Models (LLMs) are becoming increasingly multilingual, supporting hundreds of languages, especially high resource ones. Unfortunately, Dialect variations are still underrepresented due to limited data and linguistic variation. In this work, we adapt a pre-trained LLM to improve dialectal performance. Specifically, we use Low Rank Adaptation (LoRA) fine-tuning on monolingual and English Dialect parallel data, adapter merging and dialect-aware MBR decoding to improve dialectal fideli...

---

### 37. Life Cycle-Aware Evaluation of Knowledge Distillation for Machine Translation: Environmental Impact and Translation Quality Trade-offs

**Authors:** Joseph Attieh, Timothee Mickus, Anne-Laure Ligozat, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09691v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09691v1)

**Summary:** Knowledge distillation (KD) is a tool to compress a larger system (teacher) into a smaller one (student). In machine translation, studies typically report only the translation quality of the student and omit the computational complexity of performing KD, making it difficult to select among the many available KD choices under compute-induced constraints. In this study, we evaluate representative KD methods by considering both translation quality and computational cost. We express computational co...

---

### 38. MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering

**Authors:** Sieun Hyeon, Jusang Oh, Sunghwan Steve Cho, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09642v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09642v1)

**Summary:** Recent advances in Large Language Models (LLMs) have significantly improved table understanding tasks such as Table Question Answering (TableQA), yet challenges remain in ensuring reliability, scalability, and efficiency, especially in resource-constrained or privacy-sensitive environments. In this paper, we introduce MATA, a multi-agent TableQA framework that leverages multiple complementary reasoning paths and a set of tools built with small language models. MATA generates candidate answers th...

---

### 39. MILE-RefHumEval: A Reference-Free, Multi-Independent LLM Framework for Human-Aligned Evaluation

**Authors:** Nalin Srun, Parisa Rastin, Guénaël Cabanes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09624v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09624v1)

**Summary:** We introduce MILE-RefHumEval, a reference-free framework for evaluating Large Language Models (LLMs) without ground-truth annotations or evaluator coordination. It leverages an ensemble of independently prompted evaluators guided by a human-aligned schema, supporting both discrete and continuous scoring judgement. With task-specific prompts from best candidate selection, summarization and image captioning to dialogue, MILE-RefHumEval provides flexible, interpretable, and scalable assessments. Ex...

---

### 40. AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models

**Authors:** R E Zera Marveen Lyngkhoi, Chirag Chawla, Pratinav Seth, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09621v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09621v1)

**Summary:** Post-training alignment is central to deploying large language models (LLMs), yet practical workflows remain split across backend-specific tools and ad-hoc glue code, making experiments hard to reproduce. We identify backend interference, reward fragmentation, and irreproducible pipelines as key obstacles in alignment research. We introduce AlignTune, a modular toolkit exposing a unified interface for supervised fine-tuning (SFT) and RLHF-style optimization with interchangeable TRL and Unsloth b...

---

### 41. Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning

**Authors:** Qiao Liang, Yuke Zhu, Chao Ge, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09598v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09598v1)

**Summary:** Tool-integrated reasoning (TIR) enables LLM agents to solve tasks through planning, tool use, and iterative revision, but outcome-only reinforcement learning in this setting suffers from sparse, delayed rewards and weak step-level credit assignment. In long-horizon TIR trajectories, an early irrecoverable mistake can determine success or failure, making it crucial to localize the first irrecoverable step and leverage it for fine-grained credit assignment. We propose Error-Localized Policy Optimi...

---

### 42. On the Optimal Reasoning Length for RL-Trained Language Models

**Authors:** Daisuke Nohara, Taishi Nakamura, Rio Yokota

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09591v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09591v1)

**Summary:** Reinforcement learning substantially improves reasoning in large language models, but it also tends to lengthen chain of thought outputs and increase computational cost during both training and inference. Though length control methods have been proposed, it remains unclear what the optimal output length is for balancing efficiency and performance. In this work, we compare several length control methods on two models, Qwen3-1.7B Base and DeepSeek-R1-Distill-Qwen-1.5B. Our results indicate that le...

---

### 43. Context-Aware Counterfactual Data Augmentation for Gender Bias Mitigation in Language Models

**Authors:** Shweta Parihar, Liu Guangliang, Natalie Parde, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09590v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09590v1)

**Summary:** A challenge in mitigating social bias in fine-tuned language models (LMs) is the potential reduction in language modeling capability, which can harm downstream performance. Counterfactual data augmentation (CDA), a widely used method for fine-tuning, highlights this issue by generating synthetic data that may align poorly with real-world distributions or creating overly simplistic counterfactuals that ignore the social context of altered sensitive attributes (e.g., gender) in the pretraining cor...

---

### 44. Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs

**Authors:** Sora Miyamoto, Daisuke Oba, Naoaki Okazaki

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09574v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09574v1)

**Summary:** Tree-search decoding is an effective form of test-time scaling for large language models (LLMs), but real-world deployment imposes a fixed per-query token budget that varies across settings. Existing tree-search policies are largely budget-agnostic, treating the budget as a termination condition, which can lead to late-stage over-branching or premature termination. We propose {Budget-Guided MCTS} (BG-MCTS), a tree-search decoding algorithm that aligns its search policy with the remaining token b...

---

### 45. LEMUR: A Corpus for Robust Fine-Tuning of Multilingual Law Embedding Models for Retrieval

**Authors:** Narges Baba Ahmadi, Jan Strich, Martin Semmann, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09570v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09570v1)

**Summary:** Large language models (LLMs) are increasingly used to access legal information. Yet, their deployment in multilingual legal settings is constrained by unreliable retrieval and the lack of domain-adapted, open-embedding models. In particular, existing multilingual legal corpora are not designed for semantic retrieval, and PDF-based legislative sources introduce substantial noise due to imperfect text extraction. To address these challenges, we introduce LEMUR, a large-scale multilingual corpus of...

---

### 46. Advancing Block Diffusion Language Models for Test-Time Scaling

**Authors:** Yi Lu, Deyang Kong, Jianing Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09555v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09555v1)

**Summary:** Recent advances in block diffusion language models have demonstrated competitive performance and strong scalability on reasoning tasks. However, existing BDLMs have limited exploration under the test-time scaling setting and face more severe decoding challenges in long Chain-of-Thought reasoning, particularly in balancing the decoding speed and effectiveness. In this work, we propose a unified framework for test-time scaling in BDLMs that introduces adaptivity in both decoding and block-wise gen...

---

### 47. Comprehensive Comparison of RAG Methods Across Multi-Domain Conversational QA

**Authors:** Klejda Alushi, Jan Strich, Chris Biemann, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09552v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09552v1)

**Summary:** Conversational question answering increasingly relies on retrieval-augmented generation (RAG) to ground large language models (LLMs) in external knowledge. Yet, most existing studies evaluate RAG methods in isolation and primarily focus on single-turn settings. This paper addresses the lack of a systematic comparison of RAG methods for multi-turn conversational QA, where dialogue history, coreference, and shifting user intent substantially complicate retrieval. We present a comprehensive empiric...

---

### 48. UniARM: Towards a Unified Autoregressive Reward Model for Multi-Objective Test-Time Alignment

**Authors:** Hongyan Xie, Yikun Ban, Ruiyu Fang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09538v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09538v1)

**Summary:** Multi-objective alignment aims to align LLM responses with multiple human preference objectives. Among existing methods, guiding the generation of frozen LLMs through autoregressive reward models (ARMs) to accomplish multi-objective test-time alignment is a low-cost solution. However, these methods typically rely on independent parameters for each preference objective, either by training ARMs independently across preference dimensions, which neglects interactions among preference features, or by...

---

### 49. Knowledge Integration Decay in Search-Augmented Reasoning of Large Language Models

**Authors:** Sangwon Yu, Ik-hwan Kim, Donghun Kang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09517v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09517v1)

**Summary:** Modern Large Language Models (LLMs) have demonstrated remarkable capabilities in complex tasks by employing search-augmented reasoning to incorporate external knowledge into long chains of thought. However, we identify a critical yet underexplored bottleneck in this paradigm, termed Knowledge Integration Decay (KID). Specifically, we observe that as the length of reasoning generated before search grows, models increasingly fail to integrate retrieved evidence into subsequent reasoning steps, lim...

---

### 50. The CLEF-2026 CheckThat! Lab: Advancing Multilingual Fact-Checking

**Authors:** Julia Maria Struß, Sebastian Schellhammer, Stefan Dietze, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09516v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09516v1)

**Summary:** The CheckThat! lab aims to advance the development of innovative technologies combating disinformation and manipulation efforts in online communication across a multitude of languages and platforms. While in early editions the focus has been on core tasks of the verification pipeline (check-worthiness, evidence retrieval, and verification), in the past three editions, the lab added additional tasks linked to the verification process. In this year's edition, the verification pipeline is at the ce...

---

## cs.CV

**50 papers**

### 1. SAGE: Scalable Agentic 3D Scene Generation for Embodied AI

**Authors:** Hongchi Xia, Xuan Li, Zhaoshuo Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10116v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10116v1)

**Summary:** Real-world data collection for embodied agents remains costly and unsafe, calling for scalable, realistic, and simulator-ready 3D environments. However, existing scene-generation systems often rely on rule-based or task-specific pipelines, yielding artifacts and physically invalid scenes. We present SAGE, an agentic framework that, given a user-specified embodied task (e.g., "pick up a bowl and place it on the table"), understands the intent and automatically generates simulation-ready environme...

---

### 2. Quantum Multiple Rotation Averaging

**Authors:** Shuteng Wang, Natacha Kuete Meli, Michael Möller, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10115v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10115v1)

**Summary:** Multiple rotation averaging (MRA) is a fundamental optimization problem in 3D vision and robotics that aims to recover globally consistent absolute rotations from noisy relative measurements. Established classical methods, such as L1-IRLS and Shonan, face limitations including local minima susceptibility and reliance on convex relaxations that fail to preserve the exact manifold geometry, leading to reduced accuracy in high-noise scenarios. We introduce IQARS (Iterative Quantum Annealing for Rot...

---

### 3. ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation

**Authors:** Mingyang Wu, Ashirbad Mishra, Soumik Dey, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10113v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10113v1)

**Summary:** Image-to-Video generation (I2V) animates a static image into a temporally coherent video sequence following textual instructions, yet preserving fine-grained object identity under changing viewpoints remains a persistent challenge. Unlike text-to-video models, existing I2V pipelines often suffer from appearance drift and geometric distortion, artifacts we attribute to the sparsity of single-view 2D observations and weak cross-modal alignment. Here we address this problem from both data and model...

---

### 4. Olaf-World: Orienting Latent Actions for Video World Modeling

**Authors:** Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10104v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10104v1)

**Summary:** Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, the...

---

### 5. VideoWorld 2: Learning Transferable Knowledge from Real-world Videos

**Authors:** Zhongwei Ren, Yunchao Wei, Xiao Yu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10102v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10102v1)

**Summary:** Learning transferable knowledge from unlabeled video data and applying it in new environments is a fundamental capability of intelligent agents. This work presents VideoWorld 2, which extends VideoWorld and offers the first investigation into learning transferable knowledge directly from raw real-world videos. At its core, VideoWorld 2 introduces a dynamic-enhanced Latent Dynamics Model (dLDM) that decouples action dynamics from visual appearance: a pretrained video diffusion model handles visua...

---

### 6. Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders

**Authors:** Amandeep Kumar, Vishal M. Patel

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10099v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10099v1)

**Summary:** Leveraging representation encoders for generative modeling offers a path for efficient, high-fidelity synthesis. However, standard diffusion transformers fail to converge on these representations directly. While recent work attributes this to a capacity bottleneck proposing computationally expensive width scaling of diffusion transformers we demonstrate that the failure is fundamentally geometric. We identify Geometric Interference as the root cause: standard Euclidean flow matching forces proba...

---

### 7. VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model

**Authors:** Jingwen Sun, Wenyao Zhang, Zekun Qi, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10098v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10098v1)

**Summary:** Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a JEPA-style pretraining framework that sidesteps these pitfalls by design. The key idea is \emph{leakage-free state prediction}: a target encoder prod...

---

### 8. Causality in Video Diffusers is Separable from Denoising

**Authors:** Xingjian Bai, Guande He, Zhengqi Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10095v1)

**Summary:** Causality -- referring to temporal, uni-directional cause-effect relationships between components -- underlies many complex generative processes, including videos, language, and robot trajectories. Current causal diffusion models entangle temporal reasoning with iterative denoising, applying causal attention across all layers, at every denoising step, and over the entire context. In this paper, we show that the causal reasoning in these models is separable from the multi-step denoising process. ...

---

### 9. 4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere

**Authors:** Yihang Luo, Shangchen Zhou, Yushi Lan, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10094v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10094v1)

**Summary:** We present 4RC, a unified feed-forward framework for 4D reconstruction from monocular videos. Unlike existing approaches that typically decouple motion from geometry or produce limited 4D attributes such as sparse trajectories or two-view scene flow, 4RC learns a holistic 4D representation that jointly captures dense scene geometry and motion dynamics. At its core, 4RC introduces a novel encode-once, query-anywhere and anytime paradigm: a transformer backbone encodes the entire video into a comp...

---

### 10. Can Image Splicing and Copy-Move Forgery Be Detected by the Same Model? Forensim: An Attention-Based State-Space Approach

**Authors:** Soumyaroop Nandi, Prem Natarajan

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10079v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10079v1)

**Summary:** We introduce Forensim, an attention-based state-space framework for image forgery detection that jointly localizes both manipulated (target) and source regions. Unlike traditional approaches that rely solely on artifact cues to detect spliced or forged areas, Forensim is designed to capture duplication patterns crucial for understanding context. In scenarios such as protest imagery, detecting only the forged region, for example a duplicated act of violence inserted into a peaceful crowd, can mis...

---

### 11. Vendi Novelty Scores for Out-of-Distribution Detection

**Authors:** Amey P. Pasarkar, Adji Bousso Dieng

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10062v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10062v1)

**Summary:** Out-of-distribution (OOD) detection is critical for the safe deployment of machine learning systems. Existing post-hoc detectors typically rely on model confidence scores or likelihood estimates in feature space, often under restrictive distributional assumptions. In this work, we introduce a third paradigm and formulate OOD detection from a diversity perspective. We propose the Vendi Novelty Score (VNS), an OOD detector based on the Vendi Scores (VS), a family of similarity-based diversity metr...

---

### 12. Spatio-Temporal Attention for Consistent Video Semantic Segmentation in Automated Driving

**Authors:** Serin Varghese, Kevin Ross, Fabian Hueger, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10052v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10052v1)

**Summary:** Deep neural networks, especially transformer-based architectures, have achieved remarkable success in semantic segmentation for environmental perception. However, existing models process video frames independently, thus failing to leverage temporal consistency, which could significantly improve both accuracy and stability in dynamic scenes. In this work, we propose a Spatio-Temporal Attention (STA) mechanism that extends transformer attention blocks to incorporate multi-frame context, enabling r...

---

### 13. Conformal Prediction Sets for Instance Segmentation

**Authors:** Kerri Lu, Dan M. Kluger, Stephen Bates, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10045v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10045v1)

**Summary:** Current instance segmentation models achieve high performance on average predictions, but lack principled uncertainty quantification: their outputs are not calibrated, and there is no guarantee that a predicted mask is close to the ground truth. To address this limitation, we introduce a conformal prediction algorithm to generate adaptive confidence sets for instance segmentation. Given an image and a pixel coordinate query, our algorithm generates a confidence set of instance predictions for th...

---

### 14. Simple Image Processing and Similarity Measures Can Link Data Samples across Databases through Brain MRI

**Authors:** Gaurang Sharma, Harri Polonen, Juha Pajula, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10043v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10043v1)

**Summary:** Head Magnetic Resonance Imaging (MRI) is routinely collected and shared for research under strict regulatory frameworks. These frameworks require removing potential identifiers before sharing. But, even after skull stripping, the brain parenchyma contains unique signatures that can match other MRIs from the same participants across databases, posing a privacy risk if additional data features are available. Current regulatory frameworks often mandate evaluating such risks based on the assessment ...

---

### 15. Fake-HR1: Rethinking reasoning of vision language model for synthetic image detection

**Authors:** Changjiang Jiang, Xinkuan Sha, Fengchang Yu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10042v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10042v1)

**Summary:** Recent studies have demonstrated that incorporating Chain-of-Thought (CoT) reasoning into the detection process can enhance a model's ability to detect synthetic images. However, excessively lengthy reasoning incurs substantial resource overhead, including token consumption and latency, which is particularly redundant when handling obviously generated forgeries. To address this issue, we propose Fake-HR1, a large-scale hybrid-reasoning model that, to the best of our knowledge, is the first to ad...

---

### 16. Perception with Guarantees: Certified Pose Estimation via Reachability Analysis

**Authors:** Tobias Ladner, Yasser Shoukry, Matthias Althoff

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10032v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10032v1)

**Summary:** Agents in cyber-physical systems are increasingly entrusted with safety-critical tasks. Ensuring safety of these agents often requires localizing the pose for subsequent actions. Pose estimates can, e.g., be obtained from various combinations of lidar sensors, cameras, and external services such as GPS. Crucially, in safety-critical domains, a rough estimate is insufficient to formally determine safety, i.e., guaranteeing safety even in the worst-case scenario, and external services might additi...

---

### 17. Faster-GS: Analyzing and Improving Gaussian Splatting Optimization

**Authors:** Florian Hahlbohm, Linus Franke, Martin Eisemann, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09999v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09999v1)

**Summary:** Recent advances in 3D Gaussian Splatting (3DGS) have focused on accelerating optimization while preserving reconstruction quality. However, many proposed methods entangle implementation-level improvements with fundamental algorithmic modifications or trade performance for fidelity, leading to a fragmented research landscape that complicates fair comparison. In this work, we consolidate and evaluate the most effective and broadly applicable strategies from prior 3DGS research and augment them wit...

---

### 18. Efficient Special Stain Classification

**Authors:** Oskar Thaeter, Christian Grashei, Anette Haas, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09989v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09989v1)

**Summary:** Stains are essential in histopathology to visualize specific tissue characteristics, with Haematoxylin and Eosin (H&E) serving as the clinical standard. However, pathologists frequently   utilize a variety of special stains for the diagnosis of specific morphologies. Maintaining accurate metadata for these slides is critical for quality control in clinical archives and for   the integrity of computational pathology datasets. In this work, we compare two approaches for automated classification of...

---

### 19. Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings

**Authors:** Alexander Fertig, Karthikeyan Chandra Sekaran, Lakshman Balasubramanian, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09985v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09985v1)

**Summary:** As autonomous vehicles are rolled out, measures must be taken to ensure their safe operation. In order to supervise a system that is already in operation, monitoring frameworks are frequently employed. These run continuously online in the background, supervising the system status and recording anomalies. This work proposes an online monitoring framework to detect anomalies in object state representations. Thereby, a key challenge is creating a framework for anomaly detection without anomaly labe...

---

### 20. Coupled Inference in Diffusion Models for Semantic Decomposition

**Authors:** Calvin Yeung, Ali Zakeri, Zhuowen Zou, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09983v1)

**Summary:** Many visual scenes can be described as compositions of latent factors. Effective recognition, reasoning, and editing often require not only forming such compositional representations, but also solving the decomposition problem. One popular choice for constructing these representations is through the binding operation. Resonator networks, which can be understood as coupled Hopfield networks, were proposed as a way to perform decomposition on such bound representations. Recent works have shown not...

---

### 21. Learning to Detect Baked Goods with Limited Supervision

**Authors:** Thomas H. Schmitt, Maximilian Bundscherer, Tobias Bocklet

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09979v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09979v1)

**Summary:** Monitoring leftover products provides valuable insights that can be used to optimize future production. This is especially important for German bakeries because freshly baked goods have a very short shelf life. Automating this process can reduce labor costs, improve accuracy, and streamline operations. We propose automating this process using an object detection model to identify baked goods from images. However, the large diversity of German baked goods makes fully supervised training prohibiti...

---

### 22. Bladder Vessel Segmentation using a Hybrid Attention-Convolution Framework

**Authors:** Franziska Krauß, Matthias Ege, Zoltan Lovasz, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09949v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09949v1)

**Summary:** Urinary bladder cancer surveillance requires tracking tumor sites across repeated interventions, yet the deformable and hollow bladder lacks stable landmarks for orientation. While blood vessels visible during endoscopy offer a patient-specific "vascular fingerprint" for navigation, automated segmentation is challenged by imperfect endoscopic data, including sparse labels, artifacts like bubbles or variable lighting, continuous deformation, and mucosal folds that mimic vessels. State-of-the-art ...

---

### 23. VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization

**Authors:** Yikun Liu, Yuan Liu, Shangzhe Di, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09934v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09934v1)

**Summary:** Multimodal Large Language Models (MLLMs) have recently achieved remarkable success in visual-language understanding, demonstrating superior high-level semantic alignment within their vision encoders. An important question thus arises: Can these encoders serve as versatile vision backbones, capable of reliably performing classic vision-centric tasks as well? To address the question, we make the following contributions: (i) we identify that the vision encoders within MLLMs exhibit deficiencies in ...

---

### 24. Unbalanced optimal transport for robust longitudinal lesion evolution with registration-aware and appearance-guided priors

**Authors:** Melika Qahqaie, Dominik Neumann, Tobias Heimann, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09933v1)

**Summary:** Evaluating lesion evolution in longitudinal CT scans of can cer patients is essential for assessing treatment response, yet establishing reliable lesion correspondence across time remains challenging. Standard bipartite matchers, which rely on geometric proximity, struggle when lesions appear, disappear, merge, or split. We propose a registration-aware matcher based on unbalanced optimal transport (UOT) that accommodates unequal lesion mass and adapts priors to patient-level tumor-load changes. ...

---

### 25. GeoFormer: A Swin Transformer-Based Framework for Scene-Level Building Height and Footprint Estimation from Sentinel Imagery

**Authors:** Han Jinzhen, JinByeong Lee, JiSung Kim, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09932v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09932v1)

**Summary:** Accurate three-dimensional urban data are critical for climate modelling, disaster risk assessment, and urban planning, yet remain scarce due to reliance on proprietary sensors or poor cross-city generalisation. We propose GeoFormer, an open-source Swin Transformer framework that jointly estimates building height (BH) and footprint (BF) on a 100 m grid using only Sentinel-1/2 imagery and open DEM data. A geo-blocked splitting strategy ensures strict spatial independence between training and test...

---

### 26. Monocular Normal Estimation via Shading Sequence Estimation

**Authors:** Zongrui Li, Xinhua Ma, Minghui Hu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09929v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09929v1)

**Summary:** Monocular normal estimation aims to estimate the normal map from a single RGB image of an object under arbitrary lights. Existing methods rely on deep models to directly predict normal maps. However, they often suffer from 3D misalignment: while the estimated normal maps may appear to have a correct appearance, the reconstructed surfaces often fail to align with the geometric details. We argue that this misalignment stems from the current paradigm: the model struggles to distinguish and reconstr...

---

### 27. A benchmark for video-based laparoscopic skill analysis and assessment

**Authors:** Isabel Funke, Sebastian Bodenstedt, Felix von Bechtolsheim, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09927v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09927v1)

**Summary:** Laparoscopic surgery is a complex surgical technique that requires extensive training. Recent advances in deep learning have shown promise in supporting this training by enabling automatic video-based assessment of surgical skills. However, the development and evaluation of deep learning models is currently hindered by the limited size of available annotated datasets. To address this gap, we introduce the Laparoscopic Skill Analysis and Assessment (LASANA) dataset, comprising 1270 stereo video r...

---

### 28. SARS: A Novel Face and Body Shape and Appearance Aware 3D Reconstruction System extends Morphable Models

**Authors:** Gulraiz Khan, Kenneth Y. Wertheim, Kevin Pimbblet, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09918v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09918v1)

**Summary:** Morphable Models (3DMMs) are a type of morphable model that takes 2D images as inputs and recreates the structure and physical appearance of 3D objects, especially human faces and bodies. 3DMM combines identity and expression blendshapes with a basic face mesh to create a detailed 3D model. The variability in the 3D Morphable models can be controlled by tuning diverse parameters. They are high-level image descriptors, such as shape, texture, illumination, and camera parameters. Previous research...

---

### 29. AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization

**Authors:** Shaoqiu Zhang, Zizhong Ding, Kaicheng Yang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09883v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09883v1)

**Summary:** Diffusion Transformers (DiTs) have emerged as the state-of-the-art backbone for high-fidelity image and video generation. However, their massive computational cost and memory footprint hinder deployment on edge devices. While post-training quantization (PTQ) has proven effective for large language models (LLMs), directly applying existing methods to DiTs yields suboptimal results due to the neglect of the unique temporal dynamics inherent in diffusion processes. In this paper, we propose AdaTSQ,...

---

### 30. MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation

**Authors:** Jiaxu Wang, Yicheng Jiang, Tianlun He, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09878v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09878v1)

**Summary:** World-model-based imagine-then-act becomes a promising paradigm for robotic manipulation, yet existing approaches typically support either purely image-based forecasting or reasoning over partial 3D geometry, limiting their ability to predict complete 4D scene dynamics. This work proposes a novel embodied 4D world model that enables geometrically consistent, arbitrary-view RGBD generation: given only a single-view RGBD observation as input, the model imagines the remaining viewpoints, which can ...

---

### 31. BabyMamba-HAR: Lightweight Selective State Space Models for Efficient Human Activity Recognition on Resource Constrained Devices

**Authors:** Mridankan Mandal

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09872v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09872v1)

**Summary:** Human activity recognition (HAR) on wearable and mobile devices is constrained by memory footprint and computational budget, yet competitive accuracy must be maintained across heterogeneous sensor configurations. Selective state space models (SSMs) offer linear time sequence processing with input dependent gating, presenting a compelling alternative to quadratic complexity attention mechanisms. However, the design space for deploying SSMs in the TinyML regime remains largely unexplored. In this ...

---

### 32. Free-GVC: Towards Training-Free Extreme Generative Video Compression with Temporal Coherence

**Authors:** Xiaoyue Ling, Chuqin Zhou, Chunyi Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09868v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09868v1)

**Summary:** Building on recent advances in video generation, generative video compression has emerged as a new paradigm for achieving visually pleasing reconstructions. However, existing methods exhibit limited exploitation of temporal correlations, causing noticeable flicker and degraded temporal coherence at ultra-low bitrates. In this paper, we propose Free-GVC, a training-free generative video compression framework that reformulates video coding as latent trajectory compression guided by a video diffusi...

---

### 33. Code2World: A GUI World Model via Renderable Code Generation

**Authors:** Yuhao Zheng, Li'an Zhong, Yi Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09856v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09856v1)

**Summary:** Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generat...

---

### 34. Reason-IAD: Knowledge-Guided Dynamic Latent Reasoning for Explainable Industrial Anomaly Detection

**Authors:** Peng Chen, Chao Huang, Yunkang Cao, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09850v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09850v1)

**Summary:** Industrial anomaly detection demands precise reasoning over fine-grained defect patterns. However, existing multimodal large language models (MLLMs), pretrained on general-domain data, often struggle to capture category-specific anomalies, thereby limiting both detection accuracy and interpretability. To address these limitations, we propose Reason-IAD, a knowledge-guided dynamic latent reasoning framework for explainable industrial anomaly detection. Reason-IAD comprises two core components. Fi...

---

### 35. Kelix Technique Report

**Authors:** Boyang Ding, Chenglong Chu, Dunju Zang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09843v1)

**Summary:** Autoregressive large language models (LLMs) scale well by expressing diverse tasks as sequences of discrete natural-language tokens and training with next-token prediction, which unifies comprehension and generation under self-supervision. Extending this paradigm to multimodal data requires a shared, discrete representation across modalities. However, most vision-language models (VLMs) still rely on a hybrid interface: discrete text tokens paired with continuous Vision Transformer (ViT) features...

---

### 36. ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge

**Authors:** Yijie Lin, Guofeng Ding, Haochen Zhou, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09839v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09839v1)

**Summary:** Existing multimodal retrieval benchmarks largely emphasize semantic matching on daily-life images and offer limited diagnostics of professional knowledge and complex reasoning. To address this gap, we introduce ARK, a benchmark designed to analyze multimodal retrieval from two complementary perspectives: (i) knowledge domains (five domains with 17 subtypes), which characterize the content and expertise retrieval relies on, and (ii) reasoning skills (six categories), which characterize the type o...

---

### 37. SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding

**Authors:** Zhaoxu Li, Chenqi Kong, Peijun Bao, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09825v1)

**Summary:** Hallucinations in Large Vision-Language Models (LVLMs) pose significant security and reliability risks in real-world applications. Inspired by the observation that humans are more error-prone when uncertain or hesitant, we investigate how instability in a model 's internal knowledge contributes to LVLM hallucinations. We conduct extensive empirical analyses from three perspectives, namely attention heads, model layers, and decoding tokens, and identify three key hallucination patterns: (i) visua...

---

### 38. CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video

**Authors:** Hojun Song, Heejung Choi, Aro Kim, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09816v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09816v1)

**Summary:** High-quality novel view synthesis (NVS) from real-world videos is crucial for applications such as cultural heritage preservation, digital twins, and immersive media. However, real-world videos typically contain long sequences with irregular camera trajectories and unknown poses, leading to pose drift, feature misalignment, and geometric distortion during reconstruction. Moreover, lossy compression amplifies these issues by introducing inconsistencies that gradually degrade geometry and renderin...

---

### 39. SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing

**Authors:** Tong Zhang, Honglin Lin, Zhou Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09809v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09809v1)

**Summary:** Scientific diagrams convey explicit structural information, yet modern text-to-image models often produce visually plausible but structurally incorrect results. Existing benchmarks either rely on image-centric or subjective metrics insensitive to structure, or evaluate intermediate symbolic representations rather than final rendered images, leaving pixel-based diagram generation underexplored. We introduce SciFlow-Bench, a structure-first benchmark for evaluating scientific diagram generation di...

---

### 40. Where Do Images Come From? Analyzing Captions to Geographically Profile Datasets

**Authors:** Abhipsa Basu, Yugam Bahl, Kirti Bhagat, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09775v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09775v1)

**Summary:** Recent studies show that text-to-image models often fail to generate geographically representative images, raising concerns about the representativeness of their training data and motivating the question: which parts of the world do these training examples come from? We geographically profile large-scale multimodal datasets by mapping image-caption pairs to countries based on location information extracted from captions using LLMs. Studying English captions from three widely used datasets (Re-LA...

---

### 41. Self-Supervised Learning as Discrete Communication

**Authors:** Kawtar Zaher, Ilyass Moummad, Olivier Buisson, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09764v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09764v1)

**Summary:** Most self-supervised learning (SSL) methods learn continuous visual representations by aligning different views of the same input, offering limited control over how information is structured across representation dimensions. In this work, we frame visual self-supervised learning as a discrete communication process between a teacher and a student network, where semantic information is transmitted through a fixed-capacity binary channel. Rather than aligning continuous features, the student predic...

---

### 42. Robust Vision Systems for Connected and Autonomous Vehicles: Security Challenges and Attack Vectors

**Authors:** Sandeep Gupta, Roberto Passerone

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09740v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09740v1)

**Summary:** This article investigates the robustness of vision systems in Connected and Autonomous Vehicles (CAVs), which is critical for developing Level-5 autonomous driving capabilities. Safe and reliable CAV navigation undeniably depends on robust vision systems that enable accurate detection of objects, lane markings, and traffic signage. We analyze the key sensors and vision components essential for CAV navigation to derive a reference architecture for CAV vision system (CAVVS). This reference archite...

---

### 43. Toward Fine-Grained Facial Control in 3D Talking Head Generation

**Authors:** Shaoyang Xie, Xiaofeng Cong, Baosheng Yu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09736v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09736v1)

**Summary:** Audio-driven talking head generation is a core component of digital avatars, and 3D Gaussian Splatting has shown strong performance in real-time rendering of high-fidelity talking heads. However, achieving precise control over fine-grained facial movements remains a significant challenge, particularly due to lip-synchronization inaccuracies and facial jitter, both of which can contribute to the uncanny valley effect. To address these challenges, we propose Fine-Grained 3D Gaussian Splatting (FG-...

---

### 44. Allure of Craquelure: A Variational-Generative Approach to Crack Detection in Paintings

**Authors:** Laura Paul, Holger Rauhut, Martin Burger, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09730v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09730v1)

**Summary:** Recent advances in imaging technologies, deep learning and numerical performance have enabled non-invasive detailed analysis of artworks, supporting their documentation and conservation. In particular, automated detection of craquelure in digitized paintings is crucial for assessing degradation and guiding restoration, yet remains challenging due to the possibly complex scenery and the visual similarity between cracks and crack-like artistic features such as brush strokes or hair. We propose a h...

---

### 45. From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet

**Authors:** Radib Bin Kabir, Tawsif Tashwar Dipto, Mehedi Ahamed, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09717v1)

**Summary:** Spiking Neural Networks (SNNs) are increasingly studied as energy-efficient alternatives to Convolutional Neural Networks (CNNs), particularly for edge intelligence. However, prior work has largely emphasized large-scale models, leaving the design and evaluation of lightweight CNN-to-SNN pipelines underexplored. In this paper, we present the first systematic benchmark of lightweight SNNs obtained by converting compact CNN architectures into spiking networks, where activations are modeled with Le...

---

### 46. Stroke3D: Lifting 2D strokes into rigged 3D model via latent diffusion models

**Authors:** Ruisi Zhao, Haoren Zheng, Zongxin Yang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09713v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09713v1)

**Summary:** Rigged 3D assets are fundamental to 3D deformation and animation. However, existing 3D generation methods face challenges in generating animatable geometry, while rigging techniques lack fine-grained structural control over skeleton creation. To address these limitations, we introduce Stroke3D, a novel framework that directly generates rigged meshes from user inputs: 2D drawn strokes and a descriptive text prompt. Our approach pioneers a two-stage pipeline that separates the generation into: 1) ...

---

### 47. Physics-informed diffusion models in spectral space

**Authors:** Davide Gallon, Philippe von Wurstemberger, Patrick Cheridito, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09708v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09708v1)

**Summary:** We propose a methodology that combines generative latent diffusion models with physics-informed machine learning to generate solutions of parametric partial differential equations (PDEs) conditioned on partial observations, which includes, in particular, forward and inverse PDE problems. We learn the joint distribution of PDE parameters and solutions via a diffusion process in a latent space of scaled spectral representations, where Gaussian noise corresponds to functions with controlled regular...

---

### 48. GenSeg-R1: RL-Driven Vision-Language Grounding for Fine-Grained Referring Segmentation

**Authors:** Sandesh Hegde, Jaison Saji Chacko, Debarshi Banerjee, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09701v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09701v1)

**Summary:** We study fine-grained referring image segmentation via a decoupled reason-then-segment pipeline. A vision-language model (VLM) receives an image and a natural-language query, reasons about the scene, and emits structured spatial prompts: a bounding box plus two interior keypoints for every referred instance. A frozen promptable segmenter (SAM 2) converts these prompts into high-quality masks.   Within our GenSeg-R1 framework we finetune Qwen3-VL models (4B and 8B parameters) using Group Relative...

---

### 49. Semi-supervised Liver Segmentation and Patch-based Fibrosis Staging with Registration-aided Multi-parametric MRI

**Authors:** Boya Wang, Ruizhe Li, Chao Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09686v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09686v1)

**Summary:** Liver fibrosis poses a substantial challenge in clinical practice, emphasizing the necessity for precise liver segmentation and accurate disease staging. Based on the CARE Liver 2025 Track 4 Challenge, this study introduces a multi-task deep learning framework developed for liver segmentation (LiSeg) and liver fibrosis staging (LiFS) using multiparametric MRI. The LiSeg phase addresses the challenge of limited annotated images and the complexities of multi-parametric MRI data by employing a semi...

---

### 50. TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution

**Authors:** Deyang Jiang, Jing Huang, Xuanle Zhao, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09662v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09662v1)

**Summary:** Effectively scaling GUI automation is essential for computer-use agents (CUAs); however, existing work primarily focuses on scaling GUI grounding rather than the more crucial GUI planning, which requires more sophisticated data collection. In reality, the exploration process of a CUA across apps/desktops/web pages typically follows a tree structure, with earlier functional entry points often being explored more frequently. Thus, organizing large-scale trajectories into tree structures can reduce...

---

## cs.LG

**50 papers**

### 1. Biases in the Blind Spot: Detecting What LLMs Fail to Mention

**Authors:** Iván Arcuschin, David Chanin, Adrià Garriga-Alonso, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10117v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10117v1)

**Summary:** Large Language Models (LLMs) often provide chain-of-thought (CoT) reasoning traces that appear plausible, but may hide internal biases. We call these *unverbalized biases*. Monitoring models via their stated reasoning is therefore unreliable, and existing bias evaluations typically require predefined categories and hand-crafted datasets. In this work, we introduce a fully automated, black-box pipeline for detecting task-specific unverbalized biases. Given a task dataset, the pipeline uses LLM au...

---

### 2. Olaf-World: Orienting Latent Actions for Video World Modeling

**Authors:** Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10104v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10104v1)

**Summary:** Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, the...

---

### 3. Towards Explainable Federated Learning: Understanding the Impact of Differential Privacy

**Authors:** Júlio Oliveira, Rodrigo Ferreira, André Riker, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10100v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10100v1)

**Summary:** Data privacy and eXplainable Artificial Intelligence (XAI) are two important aspects for modern Machine Learning systems. To enhance data privacy, recent machine learning models have been designed as a Federated Learning (FL) system. On top of that, additional privacy layers can be added, via Differential Privacy (DP). On the other hand, to improve explainability, ML must consider more interpretable approaches with reduced number of features and less complex internal architecture. In this contex...

---

### 4. Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders

**Authors:** Amandeep Kumar, Vishal M. Patel

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10099v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10099v1)

**Summary:** Leveraging representation encoders for generative modeling offers a path for efficient, high-fidelity synthesis. However, standard diffusion transformers fail to converge on these representations directly. While recent work attributes this to a capacity bottleneck proposing computationally expensive width scaling of diffusion transformers we demonstrate that the failure is fundamentally geometric. We identify Geometric Interference as the root cause: standard Euclidean flow matching forces proba...

---

### 5. Step-resolved data attribution for looped transformers

**Authors:** Georgios Kaissis, David Mildenberger, Juan Felipe Gomez, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10097v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10097v1)

**Summary:** We study how individual training examples shape the internal computation of looped transformers, where a shared block is applied for $τ$ recurrent iterations to enable latent reasoning. Existing training-data influence estimators such as TracIn yield a single scalar score that aggregates over all loop iterations, obscuring when during the recurrent computation a training example matters. We introduce \textit{Step-Decomposed Influence (SDI)}, which decomposes TracIn into a length-$τ$ influence tr...

---

### 6. Causality in Video Diffusers is Separable from Denoising

**Authors:** Xingjian Bai, Guande He, Zhengqi Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10095v1)

**Summary:** Causality -- referring to temporal, uni-directional cause-effect relationships between components -- underlies many complex generative processes, including videos, language, and robot trajectories. Current causal diffusion models entangle temporal reasoning with iterative denoising, applying causal attention across all layers, at every denoising step, and over the entire context. In this paper, we show that the causal reasoning in these models is separable from the multi-step denoising process. ...

---

### 7. Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

**Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10090v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10090v1)

**Summary:** Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (...

---

### 8. Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability

**Authors:** Aaditya Vikram Prasad, Connor Watts, Jack Merullo, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10067v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10067v1)

**Summary:** Language models trained on large-scale datasets have been shown to learn features that encode abstract concepts such as factuality or intent. Such features are traditionally used for test-time monitoring or steering. We present an alternative affordance: features as scalable supervision for open-ended tasks. We consider the case of hallucination-reduction as a desirable, yet open-ended behavior and design a reinforcement learning (RL) pipeline, titled RLFR (Reinforcement Learning from Feature Re...

---

### 9. Vendi Novelty Scores for Out-of-Distribution Detection

**Authors:** Amey P. Pasarkar, Adji Bousso Dieng

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10062v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10062v1)

**Summary:** Out-of-distribution (OOD) detection is critical for the safe deployment of machine learning systems. Existing post-hoc detectors typically rely on model confidence scores or likelihood estimates in feature space, often under restrictive distributional assumptions. In this work, we introduce a third paradigm and formulate OOD detection from a diversity perspective. We propose the Vendi Novelty Score (VNS), an OOD detector based on the Vendi Scores (VS), a family of similarity-based diversity metr...

---

### 10. Evaluating Disentangled Representations for Controllable Music Generation

**Authors:** Laura Ibáñez-Martínez, Chukwuemeka Nkama, Andrea Poltronieri, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10058v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10058v1)

**Summary:** Recent approaches in music generation rely on disentangled representations, often labeled as structure and timbre or local and global, to enable controllable synthesis. Yet the underlying properties of these embeddings remain underexplored. In this work, we evaluate such disentangled representations in a set of music audio models for controllable generation using a probing-based framework that goes beyond standard downstream tasks. The selected models reflect diverse unsupervised disentanglement...

---

### 11. WildCat: Near-Linear Attention in Theory and Practice

**Authors:** Tobias Schröder, Lester Mackey

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10056v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10056v1)

**Summary:** We introduce WildCat, a high-accuracy, low-cost approach to compressing the attention mechanism in neural networks. While attention is a staple of modern network architectures, it is also notoriously expensive to deploy due to resource requirements that scale quadratically with the input sequence length $n$. WildCat avoids these quadratic costs by only attending over a small weighted coreset. Crucially, we select the coreset using a fast but spectrally-accurate subsampling algorithm -- randomly ...

---

### 12. Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization

**Authors:** Xinchen Han, Hossam Afifi, Michel Marot, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10048v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10048v1)

**Summary:** Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) reasoning that increases computational costs and latency without proportional performance gains. In this paper, we propose \textbf{F}ine-grained \textbf{G}roup policy \textbf{O}ptimization (\textbf{FGO}), a Reinforcement Learning (RL) algorithm that refines group responses by subdividing them and assigning appropriate weights based on length and entropy, thereby enabling effective CoT compression. Meanwhile,...

---

### 13. Conformal Prediction Sets for Instance Segmentation

**Authors:** Kerri Lu, Dan M. Kluger, Stephen Bates, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10045v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10045v1)

**Summary:** Current instance segmentation models achieve high performance on average predictions, but lack principled uncertainty quantification: their outputs are not calibrated, and there is no guarantee that a predicted mask is close to the ground truth. To address this limitation, we introduce a conformal prediction algorithm to generate adaptive confidence sets for instance segmentation. Given an image and a pixel coordinate query, our algorithm generates a confidence set of instance predictions for th...

---

### 14. Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning

**Authors:** Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10044v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10044v1)

**Summary:** Efficient exploration remains a central challenge in reinforcement learning (RL), particularly in sparse-reward environments. We introduce Optimistic World Models (OWMs), a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likelihood estimation (RBMLE) from adaptive control into deep RL. In contrast to upper confidence bound (UCB)-style exploration methods, OWMs incorporate optimism directly into model learning by augmentation with an optimi...

---

### 15. Effectiveness of Binary Autoencoders for QUBO-Based Optimization Problems

**Authors:** Tetsuro Abe, Masashi Yamashita, Shu Tanaka

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10037v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10037v1)

**Summary:** In black-box combinatorial optimization, objective evaluations are often expensive, so high quality solutions must be found under a limited budget. Factorization machine with quantum annealing (FMQA) builds a quadratic surrogate model from evaluated samples and optimizes it on an Ising machine. However, FMQA requires binary decision variables, and for nonbinary structures such as integer permutations, the choice of binary encoding strongly affects search efficiency. If the encoding fails to refl...

---

### 16. Position: Message-passing and spectral GNNs are two sides of the same coin

**Authors:** Antonis Vasileiou, Juan Cervino, Pascal Frossard, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10031v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10031v1)

**Summary:** Graph neural networks (GNNs) are commonly divided into message-passing neural networks (MPNNs) and spectral graph neural networks, reflecting two largely separate research traditions in machine learning and signal processing. This paper argues that this divide is mostly artificial, hindering progress in the field. We propose a viewpoint in which both MPNNs and spectral GNNs are understood as different parametrizations of permutation-equivariant operators acting on graph signals. From this perspe...

---

### 17. ADORA: Training Reasoning Models with Dynamic Advantage Estimation on Reinforcement Learning

**Authors:** Qingnan Ren, Shiting Huang, Zhen Fang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10019v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10019v1)

**Summary:** Reinforcement learning has become a cornerstone technique for developing reasoning models in complex tasks, ranging from mathematical problem-solving to imaginary reasoning. The optimization of these models typically relies on policy gradient methods, whose efficacy hinges on the accurate estimation of an advantage function. However, prevailing methods typically employ static advantage estimation, a practice that leads to inefficient credit assignment by neglecting the dynamic utility of trainin...

---

### 18. A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula

**Authors:** Chenruo Liu, Yijun Dong, Yiqiu Shen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10014v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10014v1)

**Summary:** Iterative self-improvement fine-tunes an autoregressive large language model (LLM) on reward-verified outputs generated by the LLM itself. In contrast to the empirical success of self-improvement, the theoretical foundation of this generative, iterative procedure in a practical, finite-sample setting remains limited. We make progress toward this goal by modeling each round of self-improvement as maximum-likelihood fine-tuning on a reward-filtered distribution and deriving finite-sample guarantee...

---

### 19. Answer First, Reason Later: Aligning Search Relevance via Mode-Balanced Reinforcement Learning

**Authors:** Shijie Zhang, Xiang Guo, Rujun Guo, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10006v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10006v1)

**Summary:** Building a search relevance model that achieves both low latency and high performance is a long-standing challenge in the search industry. To satisfy the millisecond-level response requirements of online systems while retaining the interpretable reasoning traces of Large Language Models (LLMs), we propose a novel \textbf{Answer-First, Reason Later (AFRL)} paradigm. This paradigm requires the model to output the definitive relevance score in the very first token, followed by a structured logical ...

---

### 20. Empirical Stability Analysis of Kolmogorov-Arnold Networks in Hard-Constrained Recurrent Physics-Informed Discovery

**Authors:** Enzo Nicolas Spotorno, Josafat Leal Filho, Antonio Augusto Medeiros Frohlich

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09988v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09988v1)

**Summary:** We investigate the integration of Kolmogorov-Arnold Networks (KANs) into hard-constrained recurrent physics-informed architectures (HRPINN) to evaluate the fidelity of learned residual manifolds in oscillatory systems. Motivated by the Kolmogorov-Arnold representation theorem and preliminary gray-box results, we hypothesized that KANs would enable efficient recovery of unknown terms compared to MLPs. Through initial sensitivity analysis on configuration sensitivity, parameter scale, and training...

---

### 21. Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions

**Authors:** J Rosser, Robert Kirk, Edward Grefenstette, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09987v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09987v1)

**Summary:** Influence functions are commonly used to attribute model behavior to training documents. We explore the reverse: crafting training data that induces model behavior. Our framework, Infusion, uses scalable influence-function approximations to compute small perturbations to training documents that induce targeted changes in model behavior through parameter shifts. We evaluate Infusion on data poisoning tasks across vision and language domains. On CIFAR-10, we show that making subtle edits via Infus...

---

### 22. Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings

**Authors:** Alexander Fertig, Karthikeyan Chandra Sekaran, Lakshman Balasubramanian, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09985v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09985v1)

**Summary:** As autonomous vehicles are rolled out, measures must be taken to ensure their safe operation. In order to supervise a system that is already in operation, monitoring frameworks are frequently employed. These run continuously online in the background, supervising the system status and recording anomalies. This work proposes an online monitoring framework to detect anomalies in object state representations. Thereby, a key challenge is creating a framework for anomaly detection without anomaly labe...

---

### 23. Coupled Inference in Diffusion Models for Semantic Decomposition

**Authors:** Calvin Yeung, Ali Zakeri, Zhuowen Zou, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09983v1)

**Summary:** Many visual scenes can be described as compositions of latent factors. Effective recognition, reasoning, and editing often require not only forming such compositional representations, but also solving the decomposition problem. One popular choice for constructing these representations is through the binding operation. Resonator networks, which can be understood as coupled Hopfield networks, were proposed as a way to perform decomposition on such bound representations. Recent works have shown not...

---

### 24. Supervised Metric Regularization Through Alternating Optimization for Multi-Regime Physics-Informed Neural Networks

**Authors:** Enzo Nicolas Spotorno, Josafat Ribeiro Leal, Antonio Augusto Frohlich

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09980v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09980v1)

**Summary:** Standard Physics-Informed Neural Networks (PINNs) often face challenges when modeling parameterized dynamical systems with sharp regime transitions, such as bifurcations. In these scenarios, the continuous mapping from parameters to solutions can result in spectral bias or "mode collapse", where the network averages distinct physical behaviors. We propose a Topology-Aware PINN (TAPINN) that aims to mitigate this challenge by structuring the latent space via Supervised Metric Regularization. Unli...

---

### 25. Causal Identification in Multi-Task Demand Learning with Confounding

**Authors:** Varun Gupta, Vijay Kamble

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09969v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09969v1)

**Summary:** We study a canonical multi-task demand learning problem motivated by retail pricing, in which a firm seeks to estimate heterogeneous linear price-response functions across a large collection of decision contexts. Each context is characterized by rich observable covariates yet typically exhibits only limited historical price variation, motivating the use of multi-task learning to borrow strength across tasks. A central challenge in this setting is endogeneity: historical prices are chosen by mana...

---

### 26. Drug Release Modeling using Physics-Informed Neural Networks

**Authors:** Daanish Aleem Qureshi, Khemraj Shukla, Vikas Srivastava

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09963v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09963v1)

**Summary:** Accurate modeling of drug release is essential for designing and developing controlled-release systems. Classical models (Fick, Higuchi, Peppas) rely on simplifying assumptions that limit their accuracy in complex geometries and release mechanisms. Here, we propose a novel approach using Physics-Informed Neural Networks (PINNs) and Bayesian PINNs (BPINNs) for predicting release from planar, 1D-wrinkled, and 2D-crumpled films. This approach uniquely integrates Fick's diffusion law with limited ex...

---

### 27. Statistical-Computational Trade-offs in Learning Multi-Index Models via Harmonic Analysis

**Authors:** Hugo Latourelle-Vigeant, Theodor Misiakiewicz

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09959v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09959v1)

**Summary:** We study the problem of learning multi-index models (MIMs), where the label depends on the input $\boldsymbol{x} \in \mathbb{R}^d$ only through an unknown $\mathsf{s}$-dimensional projection $\boldsymbol{W}_*^\mathsf{T} \boldsymbol{x} \in \mathbb{R}^\mathsf{s}$. Exploiting the equivariance of this problem under the orthogonal group $\mathcal{O}_d$, we obtain a sharp harmonic-analytic characterization of the learning complexity for MIMs with spherically symmetric inputs -- which refines and gener...

---

### 28. The Catastrophic Failure of The k-Means Algorithm in High Dimensions, and How Hartigan's Algorithm Avoids It

**Authors:** Roy R. Lederman, David Silva-Sánchez, Ziling Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09936v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09936v1)

**Summary:** Lloyd's k-means algorithm is one of the most widely used clustering methods. We prove that in high-dimensional, high-noise settings, the algorithm exhibits catastrophic failure: with high probability, essentially every partition of the data is a fixed point. Consequently, Lloyd's algorithm simply returns its initial partition - even when the underlying clusters are trivially recoverable by other methods. In contrast, we prove that Hartigan's k-means algorithm does not exhibit this pathology. Our...

---

### 29. LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

**Authors:** William Lugoloobi, Thomas Foster, William Bankes, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09924v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09924v1)

**Summary:** Running LLMs with extended reasoning on every problem is expensive, but determining which inputs actually require additional compute remains challenging. We investigate whether their own likelihood of success is recoverable from their internal representations before generation, and if this signal can guide more efficient inference. We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as...

---

### 30. Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education

**Authors:** Anna Bodonhelyi, Mengdi Wang, Efe Bozkir, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09904v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09904v1)

**Summary:** Since the COVID-19 pandemic, online courses have expanded access to education, yet the absence of direct instructor support challenges learners' ability to self-regulate attention and engagement. Mind wandering and disengagement can be detrimental to learning outcomes, making their automated detection via video-based indicators a promising approach for real-time learner support. However, machine learning-based approaches often require sharing sensitive data, raising privacy concerns. Federated l...

---

### 31. Routing, Cascades, and User Choice for LLMs

**Authors:** Rafid Mahmood

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09902v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09902v1)

**Summary:** To mitigate the trade-offs between performance and costs, LLM providers route user tasks to different models based on task difficulty and latency. We study the effect of LLM routing with respect to user behavior. We propose a game between an LLM provider with two models (standard and reasoning) and a user who can re-prompt or abandon tasks if the routed model cannot solve them. The user's goal is to maximize their utility minus the delay from using the model, while the provider minimizes the cos...

---

### 32. Stemphonic: All-at-once Flexible Multi-stem Music Generation

**Authors:** Shih-Lun Wu, Ge Zhu, Juan-Pablo Caceres, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09891v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09891v1)

**Summary:** Music stem generation, the task of producing musically-synchronized and isolated instrument audio clips, offers the potential of greater user control and better alignment with musician workflows compared to conventional text-to-music models. Existing stem generation approaches, however, either rely on fixed architectures that output a predefined set of stems in parallel, or generate only one stem at a time, resulting in slow inference despite flexibility in stem combination. We propose Stemphoni...

---

### 33. Statistical benchmarking of transformer models in low signal-to-noise time-series forecasting

**Authors:** Cyril Garcia, Guillaume Remy

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09869v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09869v1)

**Summary:** We study the performance of transformer architectures for multivariate time-series forecasting in low-data regimes consisting of only a few years of daily observations. Using synthetically generated processes with known temporal and cross-sectional dependency structures and varying signal-to-noise ratios, we conduct bootstrapped experiments that enable direct evaluation via out-of-sample correlations with the optimal ground-truth predictor. We show that two-way attention transformers, which alte...

---

### 34. Differentiable Tripartite Modularity for Clustering Heterogeneous Graphs

**Authors:** Benoît Hurpeau

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09864v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09864v1)

**Summary:** Clustering heterogeneous relational data remains a central challenge in graph learning, particularly when interactions involve more than two types of entities. While differentiable modularity objectives such as DMoN have enabled end-to-end community detection on homogeneous and bipartite graphs, extending these approaches to higher-order relational structures remains non-trivial.   In this work, we introduce a differentiable formulation of tripartite modularity for graphs composed of three node ...

---

### 35. CoFEH: LLM-driven Feature Engineering Empowered by Collaborative Bayesian Hyperparameter Optimization

**Authors:** Beicheng Xu, Keyao Ding, Wei Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09851v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09851v1)

**Summary:** Feature Engineering (FE) is pivotal in automated machine learning (AutoML) but remains a bottleneck for traditional methods, which treat it as a black-box search, operating within rigid, predefined search spaces and lacking domain awareness. While Large Language Models (LLMs) offer a promising alternative by leveraging semantic reasoning to generate unbounded operators, existing methods fail to construct free-form FE pipelines, remaining confined to isolated subtasks such as feature generation. ...

---

### 36. Robust Processing and Learning: Principles, Methods, and Wireless Applications

**Authors:** Shixiong Wang, Wei Dai, Li-Chun Wang, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09848v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09848v1)

**Summary:** This tutorial-style overview article examines the fundamental principles and methods of robustness, using wireless sensing and communication (WSC) as the narrative and exemplifying framework. First, we formalize the conceptual and mathematical foundations of robustness, highlighting the interpretations and relations across robust statistics, optimization, and machine learning. Key techniques, such as robust estimation and testing, distributionally robust optimization, and regularized and adversa...

---

### 37. Stabilized Maximum-Likelihood Iterative Quantum Amplitude Estimation for Structural CVaR under Correlated Random Fields

**Authors:** Alireza Tabarraei

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09847v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09847v1)

**Summary:** Conditional Value-at-Risk (CVaR) is a central tail-risk measure in stochastic structural mechanics, yet its accurate evaluation under high-dimensional, spatially correlated material uncertainty remains computationally prohibitive for classical Monte Carlo methods. Leveraging bounded-expectation reformulations of CVaR compatible with quantum amplitude estimation, we develop a quantum-enhanced inference framework that casts CVaR evaluation as a statistically consistent, confidence-constrained maxi...

---

### 38. Step-Size Stability in Stochastic Optimization: A Theoretical Perspective

**Authors:** Fabian Schaipp, Robert M. Gower, Adrien Taylor

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09842v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09842v1)

**Summary:** We present a theoretical analysis of stochastic optimization methods in terms of their sensitivity with respect to the step size. We identify a key quantity that, for each method, describes how the performance degrades as the step size becomes too large. For convex problems, we show that this quantity directly impacts the suboptimality bound of the method. Most importantly, our analysis provides direct theoretical evidence that adaptive step-size methods, such as SPS or NGN, are more robust than...

---

### 39. Hybrid Responsible AI-Stochastic Approach for SLA Compliance in Multivendor 6G Networks

**Authors:** Emanuel Figetakis, Ahmed Refaey Hussein

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09841v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09841v1)

**Summary:** The convergence of AI and 6G network automation introduces new challenges in maintaining transparency, fairness, and accountability across multivendor management systems. Although closed-loop AI orchestration improves adaptability and self-optimization, it also creates a responsibility gap, where violations of SLAs cannot be causally attributed to specific agents or vendors. This paper presents a hybrid responsible AI-stochastic learning framework that embeds fairness, robustness, and auditabili...

---

### 40. PlugSI: Plug-and-Play Test-Time Graph Adaptation for Spatial Interpolation

**Authors:** Xuhang Wu, Zhuoxuan Liang, Wei Li, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09824v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09824v1)

**Summary:** With the rapid advancement of IoT and edge computing, sensor networks have become indispensable, driving the need for large-scale sensor deployment. However, the high deployment cost hinders their scalability. To tackle the issues, Spatial Interpolation (SI) introduces virtual sensors to infer readings from observed sensors, leveraging graph structure. However, current graph-based SI methods rely on pre-trained models, lack adaptation to larger and unseen graphs at test-time, and overlook test d...

---

### 41. A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer

**Authors:** Azka Nasir, Fatima Dossa, Muhammad Ahmed Atif, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09810v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09810v1)

**Summary:** Transfer learning in deep reinforcement learning is often motivated by improved stability and reduced training cost, but it can also fail under substantial domain shift. This paper presents a controlled empirical study examining how architectural differences between Double Deep Q-Networks (DDQN) and Dueling DQN influence transfer behavior across environments. Using CartPole as a source task and LunarLander as a structurally distinct target task, we evaluate a fixed layer-wise representation tran...

---

### 42. Decomposing Reasoning Efficiency in Large Language Models

**Authors:** Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09805v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09805v1)

**Summary:** Large language models trained for reasoning trade off inference tokens against accuracy, yet standard evaluations report only final accuracy, obscuring where tokens are spent or wasted. We introduce a trace-optional framework that decomposes token efficiency into interpretable factors: completion under a fixed token budget (avoiding truncation), conditional correctness given completion, and verbosity (token usage). When benchmark metadata provides per-instance workload proxies, we further factor...

---

### 43. Fully-automated sleep staging: multicenter validation of a generalizable deep neural network for Parkinson's disease and isolated REM sleep behavior disorder

**Authors:** Jesper Strøm, Casper Skjærbæk, Natasha Becker Bertelsen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09793v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09793v1)

**Summary:** Isolated REM sleep behavior disorder (iRBD) is a key prodromal marker of Parkinson's disease (PD), and video-polysomnography (vPSG) remains the diagnostic gold standard. However, manual sleep staging is particularly challenging in neurodegenerative diseases due to EEG abnormalities and fragmented sleep, making PSG assessments a bottleneck for deploying new RBD screening technologies at scale. We adapted U-Sleep, a deep neural network, for generalizable sleep staging in PD and iRBD. A pretrained ...

---

### 44. Toeplitz Based Spectral Methods for Data-driven Dynamical Systems

**Authors:** Vladimir R. Kostic, Karim Lounici, Massimiliano Pontil

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09791v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09791v1)

**Summary:** We introduce a Toeplitz-based framework for data-driven spectral estimation of linear evolution operators in dynamical systems. Focusing on transfer and Koopman operators from equilibrium trajectories without access to the underlying equations of motion, our method applies Toeplitz filters to the infinitesimal generator to extract eigenvalues, eigenfunctions, and spectral measures. Structural prior knowledge, such as self-adjointness or skew-symmetry, can be incorporated by design. The approach ...

---

### 45. When Less is More: The LLM Scaling Paradox in Context Compression

**Authors:** Ruishan Guo, Yibing Liu, Guoxin Ma, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09789v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09789v1)

**Summary:** Scaling up model parameters has long been a prevalent training paradigm driven by the assumption that larger models yield superior generation capabilities. However, under lossy context compression in a compressor-decoder setup, we observe a Size-Fidelity Paradox: increasing the compressor size can lessen the faithfulness of reconstructed contexts though training loss decreases. Through extensive experiments across models from 0.6B to 90B, we coin this paradox arising from two dominant factors: 1...

---

### 46. Circuit Fingerprints: How Answer Tokens Encode Their Geometrical Path

**Authors:** Andres Saurez, Neha Sengar, Dongsoo Har

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09784v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09784v1)

**Summary:** Circuit discovery and activation steering in transformers have developed as separate research threads, yet both operate on the same representational space. Are they two views of the same underlying structure? We show they follow a single geometric principle: answer tokens, processed in isolation, encode the directions that would produce them. This Circuit Fingerprint hypothesis enables circuit discovery without gradients or causal intervention -- recovering comparable structure to gradient-based...

---

### 47. Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints

**Authors:** Andres Saurez, Yousung Lee, Dongsoo Har

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09783v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09783v1)

**Summary:** Linear probes and sparse autoencoders consistently recover meaningful structure from transformer representations -- yet why should such simple methods succeed in deep, nonlinear systems? We show this is not merely an empirical regularity but a consequence of architectural necessity: transformers communicate information through linear interfaces (attention OV circuits, unembedding matrices), and any semantic feature decoded through such an interface must occupy a context-invariant linear subspace...

---

### 48. Flexible Entropy Control in RLVR with Gradient-Preserving Perspective

**Authors:** Kun Chen, Peng Shi, Fanfan Liu, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09782v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09782v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a critical method for enhancing the reasoning capabilities of Large Language Models (LLMs). However, continuous training often leads to policy entropy collapse, characterized by a rapid decay in entropy that results in premature overconfidence, reduced output diversity, and vanishing gradient norms that inhibit learning. Gradient-Preserving Clipping is a primary factor influencing these dynamics, but existing mitigation strateg...

---

### 49. Explainability in Generative Medical Diffusion Models: A Faithfulness-Based Analysis on MRI Synthesis

**Authors:** Surjo Dey, Pallabi Saikia

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09781v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09781v1)

**Summary:** This study investigates the explainability of generative diffusion models in the context of medical imaging, focusing on Magnetic resonance imaging (MRI) synthesis. Although diffusion models have shown strong performance in generating realistic medical images, their internal decision making process remains largely opaque. We present a faithfulness-based explainability framework that analyzes how prototype-based explainability methods like ProtoPNet (PPNet), Enhanced ProtoPNet (EPPNet), and Proto...

---

### 50. Self-Supervised Learning as Discrete Communication

**Authors:** Kawtar Zaher, Ilyass Moummad, Olivier Buisson, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09764v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09764v1)

**Summary:** Most self-supervised learning (SSL) methods learn continuous visual representations by aligning different views of the same input, offering limited control over how information is structured across representation dimensions. In this work, we frame visual self-supervised learning as a discrete communication process between a teacher and a student network, where semantic information is transmitted through a fixed-capacity binary channel. Rather than aligning continuous features, the student predic...

---

## cs.NE

**50 papers**

### 1. Sparse Axonal and Dendritic Delays Enable Competitive SNNs for Keyword Classification

**Authors:** Younes Bouhadjar, Emre Neftci

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09746v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09746v1)

**Summary:** Training transmission delays in spiking neural networks (SNNs) has been shown to substantially improve their performance on complex temporal tasks. In this work, we show that learning either axonal or dendritic delays enables deep feedforward SNNs composed of leaky integrate-and-fire (LIF) neurons to reach accuracy comparable to existing synaptic delay learning approaches, while significantly reducing memory and computational overhead. SNN models with either axonal or dendritic delays achieve up...

---

### 2. From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet

**Authors:** Radib Bin Kabir, Tawsif Tashwar Dipto, Mehedi Ahamed, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09717v1)

**Summary:** Spiking Neural Networks (SNNs) are increasingly studied as energy-efficient alternatives to Convolutional Neural Networks (CNNs), particularly for edge intelligence. However, prior work has largely emphasized large-scale models, leaving the design and evaluation of lightweight CNN-to-SNN pipelines underexplored. In this paper, we present the first systematic benchmark of lightweight SNNs obtained by converting compact CNN architectures into spiking networks, where activations are modeled with Le...

---

### 3. Provably robust learning of regression neural networks using $β$-divergences

**Authors:** Abhik Ghosh, Suryasis Jana

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08933v1)

**Summary:** Regression neural networks (NNs) are most commonly trained by minimizing the mean squared prediction error, which is highly sensitive to outliers and data contamination. Existing robust training methods for regression NNs are often limited in scope and rely primarily on empirical validation, with only a few offering partial theoretical guarantees. In this paper, we propose a new robust learning framework for regression NNs based on the $β$-divergence (also known as the density power divergence) ...

---

### 4. A Methodology for Effective Surrogate Learning in Complex Optimization

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08825v1)

**Summary:** Solving complex problems requires continuous effort in developing theory and practice to cope with larger, more difficult scenarios. Working with surrogates is normal for creating a proxy that realistically models the problem into the computer. Thus, the question of how to best define and characterize such a surrogate model is of the utmost importance. In this paper, we introduce the PTME methodology to study deep learning surrogates by analyzing their Precision, Time, Memory, and Energy consump...

---

### 5. Enhancing Genetic Algorithms with Graph Neural Networks: A Timetabling Case Study

**Authors:** Laura-Maria Cornei, Mihaela-Elena Breabăn

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08619v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08619v1)

**Summary:** This paper investigates the impact of hybridizing a multi-modal Genetic Algorithm with a Graph Neural Network for timetabling optimization. The Graph Neural Network is designed to encapsulate general domain knowledge to improve schedule quality, while the Genetic Algorithm explores different regions of the search space and integrates the deep learning model as an enhancement operator to guide the solution search towards optimality. Initially, both components of the hybrid technique were designed...

---

### 6. Do physics-informed neural networks (PINNs) need to be deep? Shallow PINNs using the Levenberg-Marquardt algorithm

**Authors:** Muhammad Luthfi Shahab, Imam Mukhlash, Hadi Susanto

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08515v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08515v1)

**Summary:** This work investigates the use of shallow physics-informed neural networks (PINNs) for solving forward and inverse problems of nonlinear partial differential equations (PDEs). By reformulating PINNs as nonlinear systems, the Levenberg-Marquardt (LM) algorithm is employed to efficiently optimize the network parameters. Analytical expressions for the neural network derivatives with respect to the input variables are derived, enabling accurate and efficient computation of the Jacobian matrix requir...

---

### 7. A Multi-objective Evolutionary Algorithm Based on Bi-population with Uniform Sampling for Neural Architecture Search

**Authors:** Yu Xue, Pengcheng Jiang, Chenchen Zhu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08513v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08513v1)

**Summary:** Neural architecture search (NAS) automates neural network design, improving efficiency over manual approaches. However, efficiently discovering high-performance neural network architectures that simultaneously optimize multiple objectives remains a significant challenge in NAS. Existing methods often suffer from limited population diversity and inadequate exploration of the search space, particularly in regions with extreme complexity values. To address these challenges, we propose MOEA-BUS, an ...

---

### 8. Approximating Matrix Functions with Deep Neural Networks and Transformers

**Authors:** Rahul Padmanabhan, Simone Brugiapaglia

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.07800v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07800v1)

**Summary:** Transformers have revolutionized natural language processing, but their use for numerical computation has received less attention. We study the approximation of matrix functions, which map scalar functions to matrices, using neural networks including transformers. We focus on functions mapping square matrices to square matrices of the same dimension. These types of matrix functions appear throughout scientific computing, e.g., the matrix exponential in continuous-time Markov chains and the matri...

---

### 9. Generative structural elucidation from mass spectra as an iterative optimization problem

**Authors:** Mrunali Manjrekar, Runzhong Wang, Samuel Goldman, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07709v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07709v1)

**Summary:** Liquid chromatography tandem mass spectrometry (LC-MS/MS) is a critical analytical technique for molecular identification across metabolomics, environmental chemistry, and chemical forensics. A variety of computational methods have emerged for structural annotation of spectral features of interest, but many of these features cannot be confidently annotated with reference structures or spectra. Here, we introduce FOAM (Formula-constrained Optimization for Annotating Metabolites), a computational ...

---

### 10. On the Infinite Width and Depth Limits of Predictive Coding Networks

**Authors:** Francesco Innocenti, El Mehdi Achour, Rafal Bogacz

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07697v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07697v1)

**Summary:** Predictive coding (PC) is a biologically plausible alternative to standard backpropagation (BP) that minimises an energy function with respect to network activities before updating weights. Recent work has improved the training stability of deep PC networks (PCNs) by leveraging some BP-inspired reparameterisations. However, the full scalability and theoretical basis of these approaches remains unclear. To address this, we study the infinite width and depth limits of PCNs. For linear residual net...

---

### 11. Optimizing Chlorination in Water Distribution Systems via Surrogate-assisted Neuroevolution

**Authors:** Rivaaj Monsia, Daniel Young, Olivier Francon, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07299v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07299v1)

**Summary:** Ensuring the microbiological safety of large, heterogeneous water distribution systems (WDS) typically requires managing appropriate levels of disinfectant residuals including chlorine. WDS include complex fluid interactions that are nonlinear and noisy, making such maintenance a challenging problem for traditional control algorithms. This paper proposes an evolutionary framework to this problem based on neuroevolution, multi-objective optimization, and surrogate modeling. Neural networks were e...

---

### 12. Evolving LLM-Derived Control Policies for Residential EV Charging and Vehicle-to-Grid Energy Optimization

**Authors:** Vishesh Purnananda, Benjamin John Wruck, Mingyu Guo

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07275v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07275v1)

**Summary:** This research presents a novel application of Evolutionary Computation to the domain of residential electric vehicle (EV) energy management. While reinforcement learning (RL) achieves high performance in vehicle-to-grid (V2G) optimization, it typically produces opaque "black-box" neural networks that are difficult for consumers and regulators to audit. Addressing this interpretability gap, we propose a program search framework that leverages Large Language Models (LLMs) as intelligent mutation o...

---

### 13. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 14. Sparse Spike Encoding of Channel Responses for Energy Efficient Human Activity Recognition

**Authors:** Eleonora Cicciarella, Riccardo Mazzieri, Jacopo Pegoraro, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06766v1)

**Summary:** ISAC enables pervasive monitoring, but modern sensing algorithms are often too complex for energy-constrained edge devices. This motivates the development of learning techniques that balance accuracy performance and energy efficiency. Spiking Neural Networks (SNNs) are a promising alternative, processing information as sparse binary spike trains and potentially reducing energy consumption by orders of magnitude. In this work, we propose a spiking convolutional autoencoder (SCAE) that learns tail...

---

### 15. Structural bias in multi-objective optimisation

**Authors:** Jakub Kudela, Niki van Stein, Thomas Bäck, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06742v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06742v1)

**Summary:** Structural bias (SB) refers to systematic preferences of an optimisation algorithm for particular regions of the search space that arise independently of the objective function. While SB has been studied extensively in single-objective optimisation, its role in multi-objective optimisation remains largely unexplored. This is problematic, as dominance relations, diversity preservation and Pareto-based selection mechanisms may introduce or amplify structural effects.   In this paper, we extend the...

---

### 16. Green Optimization: Energy-aware Design of Metaheuristics by Using Machine Learning Surrogates to Cope with Real Problems

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06610v2) | 📄 [PDF](https://arxiv.org/pdf/2602.06610v2)

**Summary:** Addressing real-world optimization challenges requires not only advanced metaheuristics but also continuous refinement of their internal mechanisms. This paper explores the integration of machine learning in the form of neural surrogate models into metaheuristics through a recent lens: energy consumption. While surrogates are widely used to reduce the computational cost of expensive objective functions, their combined impact on energy efficiency, algorithmic performance, and solution accuracy re...

---

### 17. Energy-Aware Metaheuristics

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06595v2) | 📄 [PDF](https://arxiv.org/pdf/2602.06595v2)

**Summary:** This paper presents a principled framework for designing energy-aware metaheuristics that operate under fixed energy budgets. We introduce a unified operator-level model that quantifies both numerical gain and energy usage, and define a robust Expected Improvement per Joule (EI/J) score that guides adaptive selection among operator variants during the search. The resulting energy-aware solvers dynamically choose between operators to self-control exploration and exploitation, aiming to maximize f...

---

### 18. A neuromorphic model of the insect visual system for natural image processing

**Authors:** Adam D. Hines, Karin Nordström, Andrew B. Barron

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06405v1)

**Summary:** Insect vision supports complex behaviors including associative learning, navigation, and object detection, and has long motivated computational models for understanding biological visual processing. However, many contemporary models prioritize task performance while neglecting biologically grounded processing pathways. Here, we introduce a bio-inspired vision model that captures principles of the insect visual system to transform dense visual input into sparse, discriminative codes. The model is...

---

### 19. DARWIN: Dynamic Agentically Rewriting Self-Improving Network

**Authors:** Henry Jiang

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05848v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05848v1)

**Summary:** DARWIN is an evolutionary GPT model, utilizing a genetic-algorithm like optimization structure with several independent GPT agents being trained individually using unique training code. Each iteration, the GPT models are prompted to modify the training code of one another in an attempt to improve their performance in a mutation-like manner, and the best GPT agents are then benchmarked and selected for the next iteration by genetic algorithm. For demonstration purposes and due to budget and time ...

---

### 20. Neuro-Inspired Visual Pattern Recognition via Biological Reservoir Computing

**Authors:** Luca Ciampi, Ludovico Iannello, Fabrizio Tonelli, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05737v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05737v1)

**Summary:** In this paper, we present a neuro-inspired approach to reservoir computing (RC) in which a network of in vitro cultured cortical neurons serves as the physical reservoir. Rather than relying on artificial recurrent models to approximate neural dynamics, our biological reservoir computing (BRC) system leverages the spontaneous and stimulus-evoked activity of living neural circuits as its computational substrate. A high-density multi-electrode array (HD-MEA) provides simultaneous stimulation and r...

---

### 21. Variable Search Stepsize for Randomized Local Search in Multi-Objective Combinatorial Optimization

**Authors:** Xuepeng Ren, Maocai Wang, Guangming Dai, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05675v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05675v1)

**Summary:** Over the past two decades, research in evolutionary multi-objective optimization has predominantly focused on continuous domains, with comparatively limited attention given to multi-objective combinatorial optimization problems (MOCOPs). Combinatorial problems differ significantly from continuous ones in terms of problem structure and landscape. Recent studies have shown that on MOCOPs multi-objective evolutionary algorithms (MOEAs) can even be outperformed by simple randomised local search. Sta...

---

### 22. Optimization is Not Enough: Why Problem Formulation Deserves Equal Attention

**Authors:** Iván Olarte Rodríguez, Gokhan Serhat, Mariusz Bujny, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05466v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05466v1)

**Summary:** Black-box optimization is increasingly used in engineering design problems where simulation-based evaluations are costly and gradients are unavailable. In this context, the optimization community has largely analyzed algorithm performance in context-free setups, while not enough attention has been devoted to how problem formulation and domain knowledge may affect the optimization outcomes. We address this gap through a case study in the topology optimization of laminated composite structures, fo...

---

### 23. Assessing Reproducibility in Evolutionary Computation: A Case Study using Human- and LLM-based Assessment

**Authors:** Francesca Da Ros, Tarik Začiragić, Aske Plaat, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.07059v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07059v1)

**Summary:** Reproducibility is an important requirement in evolutionary computation, where results largely depend on computational experiments. In practice, reproducibility relies on how algorithms, experimental protocols, and artifacts are documented and shared. Despite growing awareness, there is still limited empirical evidence on the actual reproducibility levels of published work in the field. In this paper, we study the reproducibility practices in papers published in the Evolutionary Combinatorial Op...

---

### 24. It's not a Lottery, it's a Race: Understanding How Gradient Descent Adapts the Network's Capacity to the Task

**Authors:** Hannah Pinson

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04832v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04832v1)

**Summary:** Our theoretical understanding of neural networks is lagging behind their empirical success. One of the important unexplained phenomena is why and how, during the process of training with gradient descent, the theoretical capacity of neural networks is reduced to an effective capacity that fits the task. We here investigate the mechanism by which gradient descent achieves this through analyzing the learning dynamics at the level of individual neurons in single hidden layer ReLU networks. We ident...

---

### 25. Impact of diversity on bounded archives for multi-objective local search

**Authors:** Amadeu A. Coco, Cyprien Borée, Julien Baste, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04745v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04745v1)

**Summary:** This work tackles two critical challenges related to the development of metaheuristics for Multi-Objective Optimization Problems (MOOPs): the exponential growth of non-dominated solutions and the tendency of metaheuristics to disproportionately concentrate their search on a subset of the Pareto Front. To counteract the first, bounded archives are employed as a strategic mechanism for effectively managing the increasing number of non-dominated solutions. Addressing the second challenge involves a...

---

### 26. Evolutionary Mapping of Neural Networks to Spatial Accelerators

**Authors:** Alessandro Pierro, Jonathan Timcheck, Jason Yik, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04717v1)

**Summary:** Spatial accelerators, composed of arrays of compute-memory integrated units, offer an attractive platform for deploying inference workloads with low latency and low energy consumption. However, fully exploiting their architectural advantages typically requires careful, expert-driven mapping of computational graphs to distributed processing elements. In this work, we automate this process by framing the mapping challenge as a black-box optimization problem. We introduce the first evolutionary, ha...

---

### 27. Neural Sentinel: Unified Vision Language Model (VLM) for License Plate Recognition with Human-in-the-Loop Continual Learning

**Authors:** Karthik Sivakoti

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.07051v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07051v1)

**Summary:** Traditional Automatic License Plate Recognition (ALPR) systems employ multi-stage pipelines consisting of object detection networks followed by separate Optical Character Recognition (OCR) modules, introducing compounding errors, increased latency, and architectural complexity. This research presents Neural Sentinel, a novel unified approach that leverages Vision Language Models (VLMs) to perform license plate recognition, state classification, and vehicle attribute extraction through a single f...

---

### 28. Real-time processing of analog signals on accelerated neuromorphic hardware

**Authors:** Yannik Stradmann, Johannes Schemmel, Mihai A. Petrovici, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04582v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04582v1)

**Summary:** Sensory processing with neuromorphic systems is typically done by using either event-based sensors or translating input signals to spikes before presenting them to the neuromorphic processor. Here, we offer an alternative approach: direct analog signal injection eliminates superfluous and power-intensive analog-to-digital and digital-to-analog conversions, making it particularly suitable for efficient near-sensor processing. We demonstrate this by using the accelerated BrainScaleS-2 mixed-signal...

---

### 29. Landscape-aware Automated Algorithm Design: An Efficient Framework for Real-world Optimization

**Authors:** Haoran Yin, Shuaiqun Pan, Zhao Wei, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04529v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04529v1)

**Summary:** The advent of Large Language Models (LLMs) has opened new frontiers in automated algorithm design, giving rise to numerous powerful methods. However, these approaches retain critical limitations: they require extensive evaluation of the target problem to guide the search process, making them impractical for real-world optimization tasks, where each evaluation consumes substantial computational resources. This research proposes an innovative and efficient framework that decouples algorithm discov...

---

### 30. A logical re-conception of neural networks: Hamiltonian bitwise part-whole architecture

**Authors:** E Bowen, R Granger, A Rodriguez

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04911v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04911v1)

**Summary:** We introduce a simple initial working system in which relations (such as part-whole) are directly represented via an architecture with operating and learning rules fundamentally distinct from standard artificial neural network methods. Arbitrary data are straightforwardly encoded as graphs whose edges correspond to codes from a small fixed primitive set of elemental pairwise relations, such that simple relational encoding is not an add-on, but occurs intrinsically within the most basic component...

---

### 31. Statistical Guarantees for Reasoning Probes on Looped Boolean Circuits

**Authors:** Anastasis Kratsios, Giulia Livieri, A. Martina Neuman

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03970v2) | 📄 [PDF](https://arxiv.org/pdf/2602.03970v2)

**Summary:** We study the statistical behaviour of reasoning probes in a stylized model of looped reasoning, given by Boolean circuits whose computational graph is a perfect $ν$-ary tree ($ν\ge 2$) and whose output is appended to the input and fed back iteratively for subsequent computation rounds. A reasoning probe has access to a sampled subset of internal computation nodes, possibly without covering the entire graph, and seeks to infer which $ν$-ary Boolean gate is executed at each queried node, represent...

---

### 32. Non-linear PCA via Evolution Strategies: a Novel Objective Function

**Authors:** Thomas Uriot, Elise Chung

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03967v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03967v1)

**Summary:** Principal Component Analysis (PCA) is a powerful and popular dimensionality reduction technique. However, due to its linear nature, it often fails to capture the complex underlying structure of real-world data. While Kernel PCA (kPCA) addresses non-linearity, it sacrifices interpretability and struggles with hyperparameter selection. In this paper, we propose a robust non-linear PCA framework that unifies the interpretability of PCA with the flexibility of neural networks. Our method parametrize...

---

### 33. Investigating Quantum Circuit Designs Using Neuro-Evolution

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03840v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03840v1)

**Summary:** Designing effective quantum circuits remains a central challenge in quantum computing, as circuit structure strongly influences expressivity, trainability, and hardware feasibility. Current approaches, whether using manually designed circuit templates, fixed heuristics, or automated rules, face limitations in scalability, flexibility, and adaptability, often producing circuits that are poorly matched to the specific problem or quantum hardware. In this work, we propose the Evolutionary eXplorati...

---

### 34. FOVI: A biologically-inspired foveated interface for deep vision models

**Authors:** Nicholas M. Blauch, George A. Alvarez, Talia Konkle

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03766v1)

**Summary:** Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the...

---

### 35. Equilibrium Propagation for Non-Conservative Systems

**Authors:** Antonino Emanuele Scurria, Dimitri Vanden Abeele, Bortolo Matteo Mognetti, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03670v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03670v1)

**Summary:** Equilibrium Propagation (EP) is a physics-inspired learning algorithm that uses stationary states of a dynamical system both for inference and learning. In its original formulation it is limited to conservative systems, $\textit{i.e.}$ to dynamics which derive from an energy function. Given their importance in applications, it is important to extend EP to nonconservative systems, $\textit{i.e.}$ systems with non-reciprocal interactions. Previous attempts to generalize EP to such systems failed t...

---

### 36. Stochastic Spiking Neuron Based SNN Can be Inherently Bayesian

**Authors:** Huannan Zheng, Jingli Liu, Kezhou Yang

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.07037v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07037v1)

**Summary:** Uncertainty in biological neural systems appears to be computationally beneficial rather than detrimental. However, in neuromorphic computing systems, device variability often limits performance, including accuracy and efficiency. In this work, we propose a spiking Bayesian neural network (SBNN) framework that unifies the dynamic models of intrinsic device stochasticity (based on Magnetic Tunnel Junctions) and stochastic threshold neurons to leverage noise as a functional Bayesian resource. Expe...

---

### 37. NeuroPareto: Calibrated Acquisition for Costly Many-Goal Search in Vast Parameter Spaces

**Authors:** Rong Fu, Wenxin Zhang, Chunlei Meng, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03901v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03901v1)

**Summary:** The pursuit of optimal trade-offs in high-dimensional search spaces under stringent computational constraints poses a fundamental challenge for contemporary multi-objective optimization. We develop NeuroPareto, a cohesive architecture that integrates rank-centric filtering, uncertainty disentanglement, and history-conditioned acquisition strategies to navigate complex objective landscapes. A calibrated Bayesian classifier estimates epistemic uncertainty across non-domination tiers, enabling rapi...

---

### 38. Contrastive Concept-Tree Search for LLM-Assisted Algorithm Discovery

**Authors:** Timothee Leleu, Sudeera Gunathilaka, Federico Ghimenti, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03132v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03132v1)

**Summary:** Large language Model (LLM)-assisted algorithm discovery is an iterative, black-box optimization process over programs to approximatively solve a target task, where an LLM proposes candidate programs and an external evaluator provides task feedback. Despite intense recent research on the topic and promising results, how can the LLM internal representation of the space of possible programs be maximally exploited to improve performance is an open question. Here, we introduce Contrastive Concept-Tre...

---

### 39. RPG-AE: Neuro-Symbolic Graph Autoencoders with Rare Pattern Mining for Provenance-Based Anomaly Detection

**Authors:** Asif Tauhid, Sidahmed Benabderrahmane, Mohamad Altrabulsi, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.02929v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02929v1)

**Summary:** Advanced Persistent Threats (APTs) are sophisticated, long-term cyberattacks that are difficult to detect because they operate stealthily and often blend into normal system behavior. This paper presents a neuro-symbolic anomaly detection framework that combines a Graph Autoencoder (GAE) with rare pattern mining to identify APT-like activities in system-level provenance data. Our approach first constructs a process behavioral graph using k-Nearest Neighbors based on feature similarity, then learn...

---

### 40. Refining Decision Boundaries In Anomaly Detection Using Similarity Search Within the Feature Space

**Authors:** Sidahmed Benabderrahmane, Petko Valtchev, James Cheney, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02925v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02925v1)

**Summary:** Detecting rare and diverse anomalies in highly imbalanced datasets-such as Advanced Persistent Threats (APTs) in cybersecurity-remains a fundamental challenge for machine learning systems. Active learning offers a promising direction by strategically querying an oracle to minimize labeling effort, yet conventional approaches often fail to exploit the intrinsic geometric structure of the feature space for model refinement. In this paper, we introduce SDA2E, a Sparse Dual Adversarial Attention-bas...

---

### 41. Automatic Design of Optimization Test Problems with Large Language Models

**Authors:** Wojciech Achtelik, Hubert Guzowski, Maciej Smołka, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02724v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02724v1)

**Summary:** The development of black-box optimization algorithms depends on the availability of benchmark suites that are both diverse and representative of real-world problem landscapes. Widely used collections such as BBOB and CEC remain dominated by hand-crafted synthetic functions and provide limited coverage of the high-dimensional space of Exploratory Landscape Analysis (ELA) features, which in turn biases evaluation and hinders training of meta-black-box optimizers. We introduce Evolution of Test Fun...

---

### 42. Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization

**Authors:** Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02439v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02439v1)

**Summary:** Edge AI applications increasingly require ultra-low-power, low-latency inference. Neuromorphic computing based on event-driven spiking neural networks (SNNs) offers an attractive path, but practical deployment on resource-constrained devices is limited by training difficulty, hardware-mapping overheads, and sensitivity to temporal dynamics. We present NeuEdge, a framework that combines adaptive SNN models with hardware-aware optimization for edge deployment. NeuEdge uses a temporal coding scheme...

---

### 43. Introns and Templates Matter: Rethinking Linkage in GP-GOMEA

**Authors:** Johannes Koch, Tanja Alderliesten, Peter A. N. Bosman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02311v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02311v1)

**Summary:** GP-GOMEA is among the state-of-the-art for symbolic regression, especially when it comes to finding small and potentially interpretable solutions. A key mechanism employed in any GOMEA variant is the exploitation of linkage, the dependencies between variables, to ensure efficient evolution. In GP-GOMEA, mutual information between node positions in GP trees has so far been used to learn linkage. For this, a fixed expression template is used. This however leads to introns for expressions smaller t...

---

### 44. Spark: Modular Spiking Neural Networks

**Authors:** Mario Franco, Carlos Gershenson

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02306v2) | 📄 [PDF](https://arxiv.org/pdf/2602.02306v2)

**Summary:** Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity ...

---

### 45. Backpropagation as Physical Relaxation: Exact Gradients in Finite Time

**Authors:** Antonino Emanuele Scurria

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02281v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02281v1)

**Summary:** Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activation...

---

### 46. Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL

**Authors:** Julian Lemmel, Felix Resch, Mónika Farsang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02236v2) | 📄 [PDF](https://arxiv.org/pdf/2602.02236v2)

**Summary:** Deploying pretrained policies in real-world applications presents substantial challenges that fundamentally limit the practical applicability of learning-based control systems. When autonomous systems encounter environmental changes in system dynamics, sensor drift, or task objectives, fixed policies rapidly degrade in performance. We show that employing Real-Time Recurrent Reinforcement Learning (RTRRL), a biologically plausible algorithm for online adaptation, can effectively fine-tune a pretr...

---

### 47. Scale-covariant spiking wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02020v2) | 📄 [PDF](https://arxiv.org/pdf/2602.02020v2)

**Summary:** We establish a theoretical connection between wavelet transforms and spiking neural networks through scale-space theory. We rely on the scale-covariant guarantees in the leaky integrate-and-fire neurons to implement discrete mother wavelets that approximate continuous wavelets. A reconstruction experiment demonstrates the feasibility of the approach and warrants further analysis to mitigate current approximation errors. Our work suggests a novel spiking signal representation that could enable mo...

---

### 48. SpikingGamma: Surrogate-Gradient Free and Temporally Precise Online Training of Spiking Neural Networks with Smoothed Delays

**Authors:** Roel Koopman, Sebastian Otte, Sander Bohté

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01978v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01978v1)

**Summary:** Neuromorphic hardware implementations of Spiking Neural Networks (SNNs) promise energy-efficient, low-latency AI through sparse, event-driven computation. Yet, training SNNs under fine temporal discretization remains a major challenge, hindering both low-latency responsiveness and the mapping of software-trained SNNs to efficient hardware. In current approaches, spiking neurons are modeled as self-recurrent units, embedded into recurrent networks to maintain state over time, and trained with BPT...

---

### 49. Fine-Tuning Language Models to Know What They Know

**Authors:** Sangjun Park, Elliot Meyerson, Xin Qiu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02605v1)

**Summary:** Metacognition is a critical component of intelligence, specifically regarding the awareness of one's own knowledge. While humans rely on shared internal memory for both answering questions and reporting their knowledge state, this dependency in LLMs remains underexplored. This study proposes a framework to measure metacognitive ability $d_{\rm{type2}}'$ using a dual-prompt method, followed by the introduction of Evolution Strategy for Metacognitive Alignment (ESMA) to bind a model's internal kno...

---

### 50. Enhancing Generalization in Evolutionary Feature Construction for Symbolic Regression through Vicinal Jensen Gap Minimization

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01510v1)

**Summary:** Genetic programming-based feature construction has achieved significant success in recent years as an automated machine learning technique to enhance learning performance. However, overfitting remains a challenge that limits its broader applicability. To improve generalization, we prove that vicinal risk, estimated through noise perturbation or mixup-based data augmentation, is bounded by the sum of empirical risk and a regularization term-either finite difference or the vicinal Jensen gap. Leve...

---

## q-bio.NC

**50 papers**

### 1. Popularity Feedback Constrains Innovation in Cultural Markets

**Authors:** Lucas Gautheron, Raja Marjieh, Dalton C. Conley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09997v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09997v1)

**Summary:** Real-world creative processes ranging from art to science rely on social feedback-loops between selection and creation. Yet, the effects of popularity feedback on collective creativity remain poorly understood. We investigate how popularity ratings influence cultural dynamics in a large-scale online experiment where participants ($N = 1\,008$) iteratively \textit{select} images from evolving markets and \textit{produce} their own modifications. Results show that exposing the popularity of images...

---

### 2. Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release

**Authors:** Peter N. Taylor, Gerard Hall, Jonathan Horsley, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09852v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09852v1)

**Summary:** Epileptic seizures are generated in cerebral networks that propagate ictal and interictal activity. The structure of cerebral networks underpinning epileptic activity can be inferred from diffusion-weighted MRI (DWI). However, publicly available DWI data in individuals with epilepsy are scarce, and processing is technically challenging due to scan-specific artifacts, limiting research progress. Here, we release raw DWI data from 216 individuals with epilepsy and 98 healthy controls. Subject iden...

---

### 3. Finite integration time can shift optimal sensitivity away from criticality

**Authors:** Sahel Azizpour, Viola Priesemann, Johannes Zierenberg, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09491v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09491v1)

**Summary:** Sensitivity to small changes in the environment is crucial for many real-world tasks, enabling living and artificial systems to make correct behavioral decisions. It has been shown that such sensitivity is maximized when a system operates near the critical point of a phase transition. However, proximity to criticality introduces large fluctuations and diverging timescales. Hence, to leverage the maximal sensitivity, it would require impractically long integration periods. Here, we analytically a...

---

### 4. Structural coarse-graining enables noise-robust functional connectivity and reveals hidden inter-subject variability

**Authors:** Izaro Fernandez-Iriondo, Antonio Jimenez-Marin, Jesus Cortes, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08910v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08910v1)

**Summary:** Functional connectivity estimates are highly sensitive to analysis choices and can be dominated by noise when the number of sampled time points is small relative to network dimensionality. This issue is particularly acute in fMRI, where scan resolution is limited. Because scan duration is constrained by practical factors (e.g., motion and fatigue), many datasets remain statistically underpowered for high-dimensional correlation estimation. We introduce a framework that combines diffusion-based s...

---

### 5. Universal Approximation Theorems for Dynamical Systems with Infinite-Time Horizon Guarantees

**Authors:** Abel Sagodi, Il Memming Park

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08640v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08640v1)

**Summary:** Universal approximation theorems establish the expressive capacity of neural network architectures. For dynamical systems, existing results are limited to finite time horizons or systems with a globally stable equilibrium, leaving multistability and limit cycles unaddressed. We prove that Neural ODEs achieve $\varepsilon$-$δ$ closeness -- trajectories within error $\varepsilon$ except for initial conditions of measure $< δ$ -- over the \emph{infinite} time horizon $[0,\infty)$ for three target c...

---

### 6. Linguistics and Human Brain: A Perspective of Computational Neuroscience

**Authors:** Fudong Zhang, Bo Chai, Yujie Wu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08275v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08275v1)

**Summary:** Elucidating the language-brain relationship requires bridging the methodological gap between the abstract theoretical frameworks of linguistics and the empirical neural data of neuroscience. Serving as an interdisciplinary cornerstone, computational neuroscience formalizes the hierarchical and dynamic structures of language into testable neural models through modeling, simulation, and data analysis. This enables a computational dialogue between linguistic hypotheses and neural mechanisms. Recent...

---

### 7. Bootstrapping Life-Inspired Machine Intelligence: The Biological Route from Chemistry to Cognition and Creativity

**Authors:** Giovanni Pezzulo, Michael Levin

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.08079v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08079v1)

**Summary:** Achieving advanced machine intelligence remains a central challenge in AI research, often approached through scaling neural architectures and generative models. However, biological systems offer a broader repertoire of strategies for adaptive, goal-directed behavior - strategies that emerged long before nervous systems evolved. This paper advocates a genuinely life-inspired approach to machine intelligence, drawing on principles from biology that enable robustness, autonomy, and open-ended probl...

---

### 8. Beyond Expertise: Stable Individual Differences in Predictive Eye-Hand Coordination

**Authors:** Emiko Shishido

**Published:** 2026-02-08

🔗 [Paper](http://arxiv.org/abs/2602.07816v2) | 📄 [PDF](https://arxiv.org/pdf/2602.07816v2)

**Summary:** Human eye-hand coordination relies on internal forward models that predict future states and compensate for sensory delays. During line tracing, the gaze typically leads the hand through predictive saccades, yet the extent to which this predictive window reflects expertise or intrinsic individual traits remains unclear. In this study, I examined eye-hand coordination in professional calligraphers and non-experts performing a controlled line tracing task. The temporal coupling between saccade dis...

---

### 9. How does longer temporal context enhance multimodal narrative video processing in the brain?

**Authors:** Prachi Jindal, Anant Khandelwal, Manish Gupta, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07570v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07570v1)

**Summary:** Understanding how humans and artificial intelligence systems process complex narrative videos is a fundamental challenge at the intersection of neuroscience and machine learning. This study investigates how the temporal context length of video clips (3--12 s clips) and the narrative-task prompting shape brain-model alignment during naturalistic movie watching. Using fMRI recordings from participants viewing full-length movies, we examine how brain regions sensitive to narrative context dynamical...

---

### 10. Linguistic properties and model scale in brain encoding: from small to compressed language models

**Authors:** Subba Reddy Oota, Vijay Rowtula, Satya Sai Srinath Namburi, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07547v1)

**Summary:** Recent work has shown that scaling large language models (LLMs) improves their alignment with human brain activity, yet it remains unclear what drives these gains and which representational properties are responsible. Although larger models often yield better task performance and brain alignment, they are increasingly difficult to analyze mechanistically. This raises a fundamental question: what is the minimal model capacity required to capture brain-relevant representations? To address this que...

---

### 11. Training-Driven Representational Geometry Modularization Predicts Brain Alignment in Language Models

**Authors:** Yixuan Liu, Zhiyuan Ma, Likai Tang, et al.

**Published:** 2026-02-07

🔗 [Paper](http://arxiv.org/abs/2602.07539v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07539v1)

**Summary:** How large language models (LLMs) align with the neural representation and computation of human language is a central question in cognitive science. Using representational geometry as a mechanistic lens, we addressed this by tracking entropy, curvature, and fMRI encoding scores throughout Pythia (70M-1B) training. We identified a geometric modularization where layers self-organize into stable low- and high-complexity clusters. The low-complexity module, characterized by reduced entropy and curvat...

---

### 12. Cognitive algorithms and systems of episodic memory, semantic memory and their learnings

**Authors:** Qi Zhang

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07261v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07261v1)

**Summary:** Declarative memory, the memory that can be "declared" in words or languages, is made up of two dissociated parts: episodic memory and semantic memory. This dissociation has its neuroanatomical basis episodic memory is mostly associated with the hippocampus and semantic memory with the neocortex. The two memories, on the other hand, are closely related. Lesions in the hippocampus often result in various impairments of explicit memory, e.g., anterograde, retrograde and developmental amnesias, and ...

---

### 13. Extracting Root-Causal Brain Activity Driving Psychopathology from Resting State fMRI

**Authors:** Eric V. Strobl

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07233v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07233v1)

**Summary:** Neuroimaging studies of psychiatric disorders often correlate imaging patterns with diagnostic labels or composite symptom scores, yielding diffuse associations that obscure underlying mechanisms. We instead seek to identify root-causal maps -- localized BOLD disturbances that initiate pathological cascades -- and to link them selectively to symptom dimensions. We introduce a bilevel structural causal model that connects between-subject symptom structure to within-subject resting-state fMRI via ...

---

### 14. Behavior Score Prediction in Resting-State Functional MRI by Deep State Space Modeling

**Authors:** Javier Salazar Cavazos, Maximillian Egan, Krisanne Litinas, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.07131v1) | 📄 [PDF](https://arxiv.org/pdf/2602.07131v1)

**Summary:** Early clinical assessment of Alzheimer's disease relies on behavior scores that measure a subject's language, memory, and cognitive skills. On the medical imaging side, functional magnetic resonance imaging has provided invaluable insights into the neural pathways underlying Alzheimer's disease. While prior studies have used resting-state functional MRI by extracting functional connectivity matrices, these approaches neglect the temporal dynamics inherent in functional data. In this work, we pre...

---

### 15. Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space

**Authors:** Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05971v1)

**Summary:** Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to ...

---

### 16. BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction

**Authors:** Xuanhua Yin, Runkai Zhao, Lina Yao, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04512v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04512v1)

**Summary:** Naturalistic fMRI characterizes the brain as a dynamic predictive engine driven by continuous sensory streams. However, modeling the causal forward evolution in realistic neural simulation is impeded by the timescale mismatch between multimodal inputs and the complex topology of cortical networks. To address these challenges, we introduce BrainVista, a multimodal autoregressive framework designed to model the causal evolution of brain states. BrainVista incorporates Network-wise Tokenizers to di...

---

### 17. Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish

**Authors:** Jan-Matthis Lueckmann, Viren Jain, Michał Januszewski

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04492v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04492v1)

**Summary:** Constructing mechanistic models of neural circuits is a fundamental goal of neuroscience, yet verifying such models is limited by the lack of ground truth. To rigorously test model discovery, we establish an in silico testbed using neuromechanical simulations of a larval zebrafish as a transparent ground truth. We find that LLM-based tree search autonomously discovers predictive models that significantly outperform established forecasting baselines. Conditioning on sensory drive is necessary but...

---

### 18. Multi-Integration of Labels across Categories for Component Identification (MILCCI)

**Authors:** Noga Mudrik, Yuxi Chen, Gal Mishne, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04270v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04270v1)

**Summary:** Many fields collect large-scale temporal data through repeated measurements (trials), where each trial is labeled with a set of metadata variables spanning several categories. For example, a trial in a neuroscience study may be linked to a value from category (a): task difficulty, and category (b): animal choice. A critical challenge in time-series analysis is to understand how these labels are encoded within the multi-trial observations, and disentangle the distinct effect of each label entry a...

---

### 19. A computational account of dreaming: learning and memory consolidation

**Authors:** Qi Zhang

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04095v1)

**Summary:** A number of studies have concluded that dreaming is mostly caused by randomly arriving internal signals because "dream contents are random impulses", and argued that dream sleep is unlikely to play an important part in our intellectual capacity. On the contrary, numerous functional studies have revealed that dream sleep does play an important role in our learning and other intellectual functions. Specifically, recent studies have suggested the importance of dream sleep in memory consolidation, f...

---

### 20. FOVI: A biologically-inspired foveated interface for deep vision models

**Authors:** Nicholas M. Blauch, George A. Alvarez, Talia Konkle

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03766v1)

**Summary:** Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the...

---

### 21. A Minimal Task Reveals Emergent Path Integration and Object-Location Binding in a Predictive Sequence Model

**Authors:** Linda Ariel Ventura, Victoria Bosch, Tim C Kietzmann, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03490v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03490v1)

**Summary:** Adaptive cognition requires structured internal models representing objects and their relations. Predictive neural networks are often proposed to form such "world models", yet their underlying mechanisms remain unclear. One hypothesis is that action-conditioned sequential prediction suffices for learning such world models. In this work, we investigate this possibility in a minimal in-silico setting. Sequentially sampling tokens from 2D continuous token scenes, a recurrent neural network is train...

---

### 22. Systematic review of self-supervised foundation models for brain network representation using electroencephalography

**Authors:** Hannah Portmann, Yosuke Morishima

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03269v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03269v1)

**Summary:** Automated analysis of electroencephalography (EEG) has recently undergone a paradigm shift. The introduction of transformer architectures and self-supervised pretraining (SSL) has led to the development of EEG foundation models. These models are pretrained on large amounts of unlabeled data and can be adapted to a range of downstream tasks. This systematic review summarizes recent SSL-trained EEG foundation models that learn whole-brain representations from multichannel EEG rather than represent...

---

### 23. A Hitchhiker's Guide to Poisson Gradient Estimation

**Authors:** Michael Ibrahim, Hanqi Zhao, Eli Sennesh, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03896v1)

**Summary:** Poisson-distributed latent variable models are widely used in computational neuroscience, but differentiating through discrete stochastic samples remains challenging. Two approaches address this: Exponential Arrival Time (EAT) simulation and Gumbel-SoftMax (GSM) relaxation. We provide the first systematic comparison of these methods, along with practical guidance for practitioners. Our main technical contribution is a modification to the EAT method that theoretically guarantees an unbiased first...

---

### 24. Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging

**Authors:** Chetan Gohil, Oliver M. Cliff, James M. Shine, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03240v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03240v1)

**Summary:** Cognition is increasingly framed in terms of information processing, yet most fMRI analyses focus on activation or functional connectivity rather than quantifying how information is stored and transferred. To remedy this problem, we propose a framework for estimating measures of information processing: active information storage (AIS), transfer entropy (TE), and net synergy from task-based fMRI. AIS measures information maintained within a region, TE captures directed information flow, and net s...

---

### 25. Adversarial construction as a potential solution to the experiment design problem in large task spaces

**Authors:** Prakhar Godara, Frederick Callaway, Marcelo G. Mattar

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03172v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03172v1)

**Summary:** Despite decades of work, we still lack a robust, task-general theory of human behavior even in the simplest domains. In this paper we tackle the generality problem head-on, by aiming to develop a unified model for all tasks embedded in a task-space. In particular we consider the space of binary sequence prediction tasks where the observations are generated by the space parameterized by hidden Markov models (HMM). As the space of tasks is large, experimental exploration of the entire space is inf...

---

### 26. A Reproducible Framework for Bias-Resistant Machine Learning on Small-Sample Neuroimaging Data

**Authors:** Jagan Mohan Reddy Dwarampudi, Jennifer L Purks, Joshua Wong, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02920v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02920v1)

**Summary:** We introduce a reproducible, bias-resistant machine learning framework that integrates domain-informed feature engineering, nested cross-validation, and calibrated decision-threshold optimization for small-sample neuroimaging data. Conventional cross-validation frameworks that reuse the same folds for both model selection and performance estimation yield optimistically biased results, limiting reproducibility and generalization. Demonstrated on a high-dimensional structural MRI dataset of deep b...

---

### 27. MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02494v1)

**Summary:** Clinical brain-to-text interfaces are designed for paralysed patients who cannot provide extensive training recordings. Pre-training improves data-efficient generalisation by learning statistical priors across subjects, but these priors critically depend on context. While natural speech might unfold gradually over minutes, most methods pre-train with only a few seconds of context. Thus, we propose MEG-XL, a model pre-trained with 2.5 minutes of MEG context per sample, 5-300x longer than prior wo...

---

### 28. Fine-Tuning Language Models to Know What They Know

**Authors:** Sangjun Park, Elliot Meyerson, Xin Qiu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02605v1)

**Summary:** Metacognition is a critical component of intelligence, specifically regarding the awareness of one's own knowledge. While humans rely on shared internal memory for both answering questions and reporting their knowledge state, this dependency in LLMs remains underexplored. This study proposes a framework to measure metacognitive ability $d_{\rm{type2}}'$ using a dual-prompt method, followed by the introduction of Evolution Strategy for Metacognitive Alignment (ESMA) to bind a model's internal kno...

---

### 29. Community-Level Modeling of Gyral Folding Patterns for Robust and Anatomically Informed Individualized Brain Mapping

**Authors:** Minheng Chen, Tong Chen, Yan Zhuang, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01482v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01482v1)

**Summary:** Cortical folding exhibits substantial inter-individual variability while preserving stable anatomical landmarks that enable fine-scale characterization of cortical organization. Among these, the three-hinge gyrus (3HG) serves as a key folding primitive, showing consistent topology yet meaningful variations in morphology, connectivity, and function. Existing landmark-based methods typically model each 3HG independently, ignoring that 3HGs form higher-order folding communities that capture mesosca...

---

### 30. Vulnerability-Amplifying Interaction Loops: a systematic failure mode in AI chatbot mental-health interactions

**Authors:** Veith Weilnhammer, Kevin YC Hou, Raymond Dolan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01347v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01347v1)

**Summary:** Millions of users turn to consumer AI chatbots to discuss behavioral and mental health concerns. While this presents unprecedented opportunities to deliver population-level support, it also highlights an urgent need to develop rigorous and scalable safety evaluations. Here we introduce SIM-VAIL, an AI chatbot auditing framework that captures how harmful AI chatbot responses manifest across a range of mental-health contexts. SIM-VAIL pairs a simulated human user, harboring a distinct psychiatric ...

---

### 31. Inter- and Intra-Subject Variability in EEG: A Systematic Survey

**Authors:** Xuan-The Tran, Thien-Nhan Vo, Son-Tung Vu, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01019v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01019v1)

**Summary:** Electroencephalography (EEG) underpins neuroscience, clinical neurophysiology, and brain-computer interfaces (BCIs), yet pronounced inter- and intra-subject variability limits reliability, reproducibility, and translation. This systematic review studies that quantified or modeled EEG variability across resting-state, event-related potentials (ERPs), and task-related/BCI paradigms (including motor imagery and SSVEP) in healthy and clinical cohorts. Across paradigms, inter-subject differences are ...

---

### 32. A Distinct Communication Strategies Model of the Double Empathy Problem

**Authors:** Enrique Calderoli, Maria Cristina Varriale, Flávio Kapczinski

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2602.02562v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02562v1)

**Summary:** The double empathy problem recasts the difficulty of forming empathy bonds in social interactions between autistic and neurotypical individuals as a bidirectional problem, rather than due to a deficit exclusive to the person on the spectrum. However, no explicit mechanism to explain such a phenomenon has been proposed. Here we build a feedback-loop mathematical model that would theoretically induce the empathy degradation observed during communication in neurotypical-autistic pairs solely due to...

---

### 33. The Where and How of Touch: A Review of Tactile Localization Research

**Authors:** Xaver Fuchs, Jason A. M. Khoury, Sergiu Tcaci Popescu, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.23023v1) | 📄 [PDF](https://arxiv.org/pdf/2601.23023v1)

**Summary:** Tactile localization is the seemingly simple ability to 'tell' where a touch has occurred. However, how this ability is assessed, and what conclusions are drawn from experiments, depends on the theoretical ideas that inspire the research. Here, we review both theoretical frameworks and methodological approaches based on a systematic web-based literature search on tactile localization. After presenting current theories of tactile localization, we discuss task characteristics that differentiate cu...

---

### 34. Recovering Whole-Brain Causal Connectivity under Indirect Observation with Applications to Human EEG and fMRI

**Authors:** Sangyoon Bae, Miruna Oprescu, David Keetae Park, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2602.09034v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09034v1)

**Summary:** Inferring directed connectivity from neuroimaging is an ill-posed inverse problem: recorded signals are distorted by hemodynamic filtering and volume conduction, which can mask true neural interactions. Many existing methods conflate these observation artifacts with genuine neural influence, risking spurious causal graphs driven by the measurement process. We introduce INCAMA (INdirect CAusal MAmba), a latent-space causal discovery framework that explicitly accounts for measurement physics to se...

---

### 35. Deep Learning Pose Estimation for Multi-Label Recognition of Combined Hyperkinetic Movement Disorders

**Authors:** Laura Cif, Diane Demailly, Gabriella A. Horvàth, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2602.00163v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00163v1)

**Summary:** Hyperkinetic movement disorders (HMDs) such as dystonia, tremor, chorea, myoclonus, and tics are disabling motor manifestations across childhood and adulthood. Their fluctuating, intermittent, and frequently co-occurring expressions hinder clinical recognition and longitudinal monitoring, which remain largely subjective and vulnerable to inter-rater variability. Objective and scalable methods to distinguish overlapping HMD phenotypes from routine clinical videos are still lacking. Here, we devel...

---

### 36. How 'Neural' is a Neural Foundation Model?

**Authors:** Johannes Bertram, Luciano Dyballa, Anderson Keller, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21508v1)

**Summary:** Foundation models have shown remarkable success in fitting biological visual systems; however, their black-box nature inherently limits their utility for understanding brain function. Here, we peek inside a SOTA foundation model of neural activity (Wang et al., 2025) as a physiologist might, characterizing each 'neuron' based on its temporal response properties to parametric stimuli. We analyze how different stimuli are represented in neural activity space by building decoding manifolds, and we ...

---

### 37. Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons

**Authors:** Kang You, Gary Green, Jian Zhang

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21478v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21478v1)

**Summary:** Pathophysiolpgical modelling of brain systems from microscale to macroscale remains difficult in group comparisons partly because of the infeasibility of modelling the interactions of thousands of neurons at the scales involved. Here, to address the challenge, we present a novel approach to construct differential causal networks directly from electroencephalogram (EEG) data. The proposed network is based on conditionally coupled neuronal circuits which describe the average behaviour of interacti...

---

### 38. BrainFuse: a unified infrastructure integrating realistic biological modeling and core AI methodology

**Authors:** Baiyu Chen, Yujie Wu, Siyuan Xu, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21407v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21407v1)

**Summary:** Neuroscience and artificial intelligence represent distinct yet complementary pathways to general intelligence. However, amid the ongoing boom in AI research and applications, the translational synergy between these two fields has grown increasingly elusive-hampered by a widening infrastructural incompatibility: modern AI frameworks lack native support for biophysical realism, while neural simulation tools are poorly suited for gradient-based optimization and neuromorphic hardware deployment. To...

---

### 39. An explainable framework for the relationship between dementia and glucose metabolism patterns

**Authors:** C. Vázquez-García, F. J. Martínez-Murcia, F. Segovia Román, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20480v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20480v1)

**Summary:** High-dimensional neuroimaging data presents challenges for assessing neurodegenerative diseases due to complex non-linear relationships. Variational Autoencoders (VAEs) can encode scans into lower-dimensional latent spaces capturing disease-relevant features. We propose a semi-supervised VAE framework with a flexible similarity regularization term that aligns selected latent variables with clinical or biomarker measures of dementia progression. This allows adapting the similarity metric and supe...

---

### 40. Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding

**Authors:** Jiahe Li, Junru Chen, Fanqi Shen, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20447v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20447v1)

**Summary:** Enabling natural communication through brain-computer interfaces (BCIs) remains one of the most profound challenges in neuroscience and neurotechnology. While existing frameworks offer partial solutions, they are constrained by oversimplified semantic representations and a lack of interpretability. To overcome these limitations, we introduce Semantic Intent Decoding (SID), a novel framework that translates neural activity into natural language by modeling meaning as a flexible set of composition...

---

### 41. SurfAge-Net: A Hierarchical Surface-Based Network for Interpretable Fine-Grained Brain Age Prediction

**Authors:** Rongzhao He, Dalin Zhu, Ying Wang, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2602.06994v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06994v1)

**Summary:** Brain age prediction serves as a powerful framework for assessing brain status and detecting deviations associated with neurodevelopmental and neurodegenerative disorders. However, most existing approaches emphasize whole-brain age prediction and therefore overlook the pronounced regional heterogeneity of brain maturation that is crucial for detecting localized atypical trajectories. To address this limitation, we propose a novel spherical surface-based brain age prediction network (SurfAge-Net)...

---

### 42. Implications of temporal sampling in voltage imaging microscopy

**Authors:** Jakub Czuchnowski, Jerome Mertz

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20236v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20236v1)

**Summary:** Significance: Voltage imaging microscopy has emerged as a powerful tool to investigate neural activity both in vivo and in vitro. Various imaging approaches have been developed, including point-scanning, line-scanning and wide-field microscopes, however the effects of their different temporal sampling methods on signal fidelity have not yet been fully investigated. Aim: To provide an analysis of the inherent advantages and disadvantages of temporal sampling in scanning and wide-field microscopes...

---

### 43. Stroboscopic motion reversals in delay-coupled neural fields

**Authors:** Noah Parks, Zachary P Kilpatrick

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19125v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19125v1)

**Summary:** Visual illusions provide a window into the mechanisms underlying visual processing, and dynamical neural circuit models offer a natural framework for proposing and testing theories of their emergence. We propose and analyze a delay-coupled neural field model that explains stroboscopic percepts arising from the subsampling of a moving, often rotating, stimulus, such as the wagon-wheel illusion. Motivated by the role of activity propagation delays in shaping visual percepts, we study neural fields...

---

### 44. Smooth embeddings in contracting recurrent networks driven by regular dynamics: A synthesis for neural representation

**Authors:** Vikas N. O'Reilly-Shah, Alessandro Maria Selvitella

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.19019v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19019v1)

**Summary:** Recurrent neural networks trained for time-series prediction often develop latent trajectories that preserve qualitative structure of the dynamical systems generating their inputs. Recent empirical work has documented topology-preserving latent organization in trained recurrent models, and recent theoretical results in reservoir computing establish conditions under which the synchronization map is an embedding. Here we synthesize these threads into a unified account of when contracting recurrent...

---

### 45. Schema-based active inference supports rapid generalization of experience and frontal cortical coding of abstract structure

**Authors:** Toon Van de Maele, Tim Verbelen, Dileep George, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18946v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18946v1)

**Summary:** Schemas -- abstract relational structures that capture the commonalities across experiences -- are thought to underlie humans' and animals' ability to rapidly generalize knowledge, rebind new experiences to existing structures, and flexibly adapt behavior across contexts. Despite their central role in cognition, the computational principles and neural mechanisms supporting schema formation and use remain elusive. Here, we introduce schema-based hierarchical active inference (S-HAI), a novel comp...

---

### 46. Closed Eyes and Coil Size -- Effects on Motor Threshold and Intracortical Inhibition, measured with TMS

**Authors:** Meher Sabharwal, Narin Suleyman, Gabriel R. Palma, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18286v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18286v1)

**Summary:** Rationale: Transcranial magnetic stimulation (TMS)-based measures such as resting motor threshold (RMT) and short interval intracortical inhibition (SICI) are widely employed to study motor cortical and corticospinal tract function, and effects of diseases and drug therapies thereon. However, the effect of key experimental factors, including as eye state (open or closed) or stimulating coil size, remain unclear. As such, it is unknown whether these factors must be kept consistent across multi-ce...

---

### 47. AI and World Models

**Authors:** Robert Worden

**Published:** 2026-01-25

🔗 [Paper](http://arxiv.org/abs/2601.17796v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17796v1)

**Summary:** While large neural nets perform impressively on specific tasks, they are unreliable and unsafe, as is shown by the persistent hallucinations of large language models. This paper shows that large neural nets are intrinsically unreliable, because it is not possible to make or validate a tractable theory of how a neural net works. There is no reliable way to extrapolate its performance from a limited number of test cases to an unlimited set of use cases. To have confidence in the performance of a n...

---

### 48. Sampling in the Euclidean Motion Group and a Problem from Brain's Primary Visual Cortex

**Authors:** Davide Barbieri

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17528v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17528v1)

**Summary:** We study a sampling problem for the abstract wavelet transform associated with the quasiregular representation of the $SE(2)$ group, for a modulated gaussian mother wavelet. This problem is motivated by the behavior of brain's primary visual cortex. We provide a characterization in terms of a dual Gramian matrix, and study numerically the relationships among the parameters defining the sampling and the mother wavelet.

---

### 49. Unsupervised sleep-like intra- and inter-layer plasticity categorizes and improves energy efficiency in a multilayer spiking network

**Authors:** Leonardo Tonielli, Cosimo Lupo, Elena Pastorelli, et al.

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17523v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17523v1)

**Summary:** Sleep is thought to support memory consolidation and the recovery of optimal energetic regime by reorganizing synaptic connectivity, yet how plasticity across hierarchical brain circuits contributes to abstraction and energy efficiency remains unclear. Here we study a spiking multi-layer network alternating wake-like and deep-sleep-like states, with state-dependent dendritic integration and synaptic plasticity in a biologically inspired thalamo-cortical framework. During wakefulness, the model l...

---

### 50. Neural Agonist-Antagonist Coupling in the Absence of Mechanical Coupling after Targeted Muscle Reinnervation

**Authors:** Laura Ferrante, Anna Boesendorfer, Benedikt Baumgartner, et al.

**Published:** 2026-01-23

🔗 [Paper](http://arxiv.org/abs/2601.16689v1) | 📄 [PDF](https://arxiv.org/pdf/2601.16689v1)

**Summary:** Following limb amputation and targeted muscle reinnervation (TMR), nerves supplying agonist and antagonist muscles are rerouted into separate targeted muscles, disrupting natural neuromechanical coupling between muscle groups. Using high-density intramuscular microelectrode arrays in reinnervated muscles, we show that neural signals for agonist and antagonist tasks remain functionally coupled: motor units active during agonist tasks were also recruited during corresponding antagonist tasks, desp...

---

## stat.ML

**50 papers**

### 1. WildCat: Near-Linear Attention in Theory and Practice

**Authors:** Tobias Schröder, Lester Mackey

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10056v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10056v1)

**Summary:** We introduce WildCat, a high-accuracy, low-cost approach to compressing the attention mechanism in neural networks. While attention is a staple of modern network architectures, it is also notoriously expensive to deploy due to resource requirements that scale quadratically with the input sequence length $n$. WildCat avoids these quadratic costs by only attending over a small weighted coreset. Crucially, we select the coreset using a fast but spectrally-accurate subsampling algorithm -- randomly ...

---

### 2. Conformal Prediction Sets for Instance Segmentation

**Authors:** Kerri Lu, Dan M. Kluger, Stephen Bates, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10045v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10045v1)

**Summary:** Current instance segmentation models achieve high performance on average predictions, but lack principled uncertainty quantification: their outputs are not calibrated, and there is no guarantee that a predicted mask is close to the ground truth. To address this limitation, we introduce a conformal prediction algorithm to generate adaptive confidence sets for instance segmentation. Given an image and a pixel coordinate query, our algorithm generates a confidence set of instance predictions for th...

---

### 3. Online Selective Conformal Prediction with Asymmetric Rules: A Permutation Test Approach

**Authors:** Mingyi Zheng, Ying Jin

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10018v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10018v1)

**Summary:** Selective conformal prediction aims to construct prediction sets with valid coverage for a test unit conditional on it being selected by a data-driven mechanism. While existing methods in the offline setting handle any selection mechanism that is permutation invariant to the labeled data, their extension to the online setting -- where data arrives sequentially and later decisions depend on earlier ones -- is challenged by the fact that the selection mechanism is naturally asymmetric. As such, ex...

---

### 4. A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula

**Authors:** Chenruo Liu, Yijun Dong, Yiqiu Shen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.10014v1) | 📄 [PDF](https://arxiv.org/pdf/2602.10014v1)

**Summary:** Iterative self-improvement fine-tunes an autoregressive large language model (LLM) on reward-verified outputs generated by the LLM itself. In contrast to the empirical success of self-improvement, the theoretical foundation of this generative, iterative procedure in a practical, finite-sample setting remains limited. We make progress toward this goal by modeling each round of self-improvement as maximum-likelihood fine-tuning on a reward-filtered distribution and deriving finite-sample guarantee...

---

### 5. Causal Identification in Multi-Task Demand Learning with Confounding

**Authors:** Varun Gupta, Vijay Kamble

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09969v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09969v1)

**Summary:** We study a canonical multi-task demand learning problem motivated by retail pricing, in which a firm seeks to estimate heterogeneous linear price-response functions across a large collection of decision contexts. Each context is characterized by rich observable covariates yet typically exhibits only limited historical price variation, motivating the use of multi-task learning to borrow strength across tasks. A central challenge in this setting is endogeneity: historical prices are chosen by mana...

---

### 6. Statistical-Computational Trade-offs in Learning Multi-Index Models via Harmonic Analysis

**Authors:** Hugo Latourelle-Vigeant, Theodor Misiakiewicz

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09959v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09959v1)

**Summary:** We study the problem of learning multi-index models (MIMs), where the label depends on the input $\boldsymbol{x} \in \mathbb{R}^d$ only through an unknown $\mathsf{s}$-dimensional projection $\boldsymbol{W}_*^\mathsf{T} \boldsymbol{x} \in \mathbb{R}^\mathsf{s}$. Exploiting the equivariance of this problem under the orthogonal group $\mathcal{O}_d$, we obtain a sharp harmonic-analytic characterization of the learning complexity for MIMs with spherically symmetric inputs -- which refines and gener...

---

### 7. The Catastrophic Failure of The k-Means Algorithm in High Dimensions, and How Hartigan's Algorithm Avoids It

**Authors:** Roy R. Lederman, David Silva-Sánchez, Ziling Chen, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09936v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09936v1)

**Summary:** Lloyd's k-means algorithm is one of the most widely used clustering methods. We prove that in high-dimensional, high-noise settings, the algorithm exhibits catastrophic failure: with high probability, essentially every partition of the data is a fixed point. Consequently, Lloyd's algorithm simply returns its initial partition - even when the underlying clusters are trivially recoverable by other methods. In contrast, we prove that Hartigan's k-means algorithm does not exhibit this pathology. Our...

---

### 8. Stabilized Maximum-Likelihood Iterative Quantum Amplitude Estimation for Structural CVaR under Correlated Random Fields

**Authors:** Alireza Tabarraei

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09847v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09847v1)

**Summary:** Conditional Value-at-Risk (CVaR) is a central tail-risk measure in stochastic structural mechanics, yet its accurate evaluation under high-dimensional, spatially correlated material uncertainty remains computationally prohibitive for classical Monte Carlo methods. Leveraging bounded-expectation reformulations of CVaR compatible with quantum amplitude estimation, we develop a quantum-enhanced inference framework that casts CVaR evaluation as a statistically consistent, confidence-constrained maxi...

---

### 9. Continual Learning for non-stationary regression via Memory-Efficient Replay

**Authors:** Pablo García-Santaclara, Bruno Fernández-Castro, RebecaP. Díaz-Redondo, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09720v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09720v1)

**Summary:** Data streams are rarely static in dynamic environments like Industry 4.0. Instead, they constantly change, making traditional offline models outdated unless they can quickly adjust to the new data. This need can be adequately addressed by continual learning (CL), which allows systems to gradually acquire knowledge without incurring the prohibitive costs of retraining them from scratch. Most research on continual learning focuses on classification problems, while very few studies address regressi...

---

### 10. Extended Isolation Forest with feature sensitivities

**Authors:** Illia Donhauzer

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09704v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09704v1)

**Summary:** Compared to theoretical frameworks that assume equal sensitivity to deviations in all features of data, the theory of anomaly detection allowing for variable sensitivity across features is less developed. To the best of our knowledge, this issue has not yet been addressed in the context of isolation-based methods, and this paper represents the first attempt to do so. This paper introduces an Extended Isolation Forest with feature sensitivities, which we refer to as the Anisotropic Isolation Fore...

---

### 11. The Entropic Signature of Class Speciation in Diffusion Models

**Authors:** Florian Handke, Dejan Stančević, Felix Koulischer, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09651v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09651v1)

**Summary:** Diffusion models do not recover semantic structure uniformly over time. Instead, samples transition from semantic ambiguity to class commitment within a narrow regime. Recent theoretical work attributes this transition to dynamical instabilities along class-separating directions, but practical methods to detect and exploit these windows in trained models are still limited. We show that tracking the class-conditional entropy of a latent semantic variable given the noisy state provides a reliable ...

---

### 12. Blind denoising diffusion models and the blessings of dimensionality

**Authors:** Zahra Kadkhodaie, Aram-Alexandre Pooladian, Sinho Chewi, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09639v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09639v1)

**Summary:** We analyze, theoretically and empirically, the performance of generative diffusion models based on \emph{blind denoisers}, in which the denoiser is not given the noise amplitude in either the training or sampling processes. Assuming that the data distribution has low intrinsic dimensionality, we prove that blind denoising diffusion models (BDDMs), despite not having access to the noise amplitude, \emph{automatically} track a particular \emph{implicit} noise schedule along the reverse process. Ou...

---

### 13. From Average Sensitivity to Small-Loss Regret Bounds under Random-Order Model

**Authors:** Shinsaku Sakaue, Yuichi Yoshida

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09457v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09457v1)

**Summary:** We study online learning in the random-order model, where the multiset of loss functions is chosen adversarially but revealed in a uniformly random order. Building on the batch-to-online conversion by Dong and Yoshida (2023), we show that if an offline algorithm admits a $(1+\varepsilon)$-approximation guarantee and the effect of $\varepsilon$ on its average sensitivity is characterized by a function $\varphi(\varepsilon)$, then an adaptive choice of $\varepsilon$ yields a small-loss regret boun...

---

### 14. Taming the Monster Every Context: Complexity Measure and Unified Framework for Offline-Oracle Efficient Contextual Bandits

**Authors:** Hao Qin, Chicheng Zhang

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09456v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09456v1)

**Summary:** We propose an algorithmic framework, Offline Estimation to Decisions (OE2D), that reduces contextual bandit learning with general reward function approximation to offline regression. The framework allows near-optimal regret for contextual bandits with large action spaces with $O(log(T))$ calls to an offline regression oracle over $T$ rounds, and makes $O(loglog(T))$ calls when $T$ is known. The design of OE2D algorithm generalizes Falcon~\citep{simchi2022bypassing} and its linear reward version~...

---

### 15. Is Memorization Helpful or Harmful? Prior Information Sets the Threshold

**Authors:** Chen Cheng, Rina Foygel Barber

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09405v1)

**Summary:** We examine the connection between training error and generalization error for arbitrary estimating procedures, working in an overparameterized linear model under general priors in a Bayesian setup. We find determining factors inherent to the prior distribution $π$, giving explicit conditions under which optimal generalization necessitates that the training error be (i) near interpolating relative to the noise size (i.e., memorization is necessary), or (ii) close to the noise level (i.e., overfit...

---

### 16. The Critical Horizon: Inspection Design Principles for Multi-Stage Operations and Deep Reasoning

**Authors:** Seyed Morteza Emadi

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09394v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09394v1)

**Summary:** Manufacturing lines, service journeys, supply chains, and AI reasoning chains share a common challenge: attributing a terminal outcome to the intermediate stage that caused it. We establish an information-theoretic barrier to this credit assignment problem: the signal connecting early steps to final outcomes decays exponentially with depth, creating a critical horizon beyond which no algorithm can learn from endpoint data alone. We prove four results. First, a Signal Decay Bound: sample complexi...

---

### 17. SnareNet: Flexible Repair Layers for Neural Networks with Hard Constraints

**Authors:** Ya-Chi Chu, Alkiviades Boukas, Madeleine Udell

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09317v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09317v1)

**Summary:** Neural networks are increasingly used as surrogate solvers and control policies, but unconstrained predictions can violate physical, operational, or safety requirements. We propose SnareNet, a feasibility-controlled architecture for learning mappings whose outputs must satisfy input-dependent nonlinear constraints. SnareNet appends a differentiable repair layer that navigates in the constraint map's range space, steering iterates toward feasibility and producing a repaired output that satisfies ...

---

### 18. Clarifying Shampoo: Adapting Spectral Descent to Stochasticity and the Parameter Trajectory

**Authors:** Runa Eschenhagen, Anna Cai, Tsung-Hsien Lee, et al.

**Published:** 2026-02-10

🔗 [Paper](http://arxiv.org/abs/2602.09314v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09314v1)

**Summary:** Optimizers leveraging the matrix structure in neural networks, such as Shampoo and Muon, are more data-efficient than element-wise algorithms like Adam and Signum. While in specific settings, Shampoo and Muon reduce to spectral descent analogous to how Adam and Signum reduce to sign descent, their general relationship and relative data efficiency under controlled settings remain unclear. Through extensive experiments on language models, we demonstrate that Shampoo achieves higher token efficienc...

---

### 19. Mutual Information Collapse Explains Disentanglement Failure in $β$-VAEs

**Authors:** Minh Vu, Xiaoliang Wan, Shuangqing Wei

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.09277v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09277v1)

**Summary:** The $β$-VAE is a foundational framework for unsupervised disentanglement, using $β$ to regulate the trade-off between latent factorization and reconstruction fidelity. Empirically, however, disentanglement performance exhibits a pervasive non-monotonic trend: benchmarks such as MIG and SAP typically peak at intermediate $β$ and collapse as regularization increases. We demonstrate that this collapse is a fundamental information-theoretic failure, where strong Kullback-Leibler pressure promotes ma...

---

### 20. Optimal Estimation in Orthogonally Invariant Generalized Linear Models: Spectral Initialization and Approximate Message Passing

**Authors:** Yihan Zhang, Hong Chang Ji, Ramji Venkataramanan, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.09240v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09240v1)

**Summary:** We consider the problem of parameter estimation from a generalized linear model with a random design matrix that is orthogonally invariant in law. Such a model allows the design have an arbitrary distribution of singular values and only assumes that its singular vectors are generic. It is a vast generalization of the i.i.d. Gaussian design typically considered in the theoretical literature, and is motivated by the fact that real data often have a complex correlation structure so that methods rel...

---

### 21. Fair Feature Importance Scores via Feature Occlusion and Permutation

**Authors:** Camille Little, Madeline Navarro, Santiago Segarra, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.09196v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09196v1)

**Summary:** As machine learning models increasingly impact society, their opaque nature poses challenges to trust and accountability, particularly in fairness contexts. Understanding how individual features influence model outcomes is crucial for building interpretable and equitable models. While feature importance metrics for accuracy are well-established, methods for assessing feature contributions to fairness remain underexplored. We propose two model-agnostic approaches to measure fair feature importanc...

---

### 22. Quantifying Epistemic Uncertainty in Diffusion Models

**Authors:** Aditi Gupta, Raphael A. Meyer, Yotam Yaniv, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.09170v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09170v1)

**Summary:** To ensure high quality outputs, it is important to quantify the epistemic uncertainty of diffusion models.Existing methods are often unreliable because they mix epistemic and aleatoric uncertainty. We introduce a method based on Fisher information that explicitly isolates epistemic variance, producing more reliable plausibility scores for generated data. To make this approach scalable, we propose FLARE (Fisher-Laplace Randomized Estimator), which approximates the Fisher information using a unifo...

---

### 23. Minimum Distance Summaries for Robust Neural Posterior Estimation

**Authors:** Sherman Khoo, Dennis Prangle, Song Liu, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.09161v1) | 📄 [PDF](https://arxiv.org/pdf/2602.09161v1)

**Summary:** Simulation-based inference (SBI) enables amortized Bayesian inference by first training a neural posterior estimator (NPE) on prior-simulator pairs, typically through low-dimensional summary statistics, which can then be cheaply reused for fast inference by querying it on new test observations. Because NPE is estimated under the training data distribution, it is susceptible to misspecification when observations deviate from the training distribution. Many robust SBI approaches address this by mo...

---

### 24. Universal Coefficients and Mayer-Vietoris Sequence for Groupoid Homology

**Authors:** Luciano Melodia

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08998v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08998v1)

**Summary:** We study homology of ample groupoids via the compactly supported Moore complex of the nerve. Let $A$ be a topological abelian group. For $n\ge 0$ set $C_n(\mathcal G;A) := C_c(\mathcal G_n,A)$ and define $\partial_n^A=\sum_{i=0}^n(-1)^i(d_i)_*$. This defines $H_n(\mathcal G;A)$. The theory is functorial for continuous étale homomorphisms. It is compatible with standard reductions, including restriction to saturated clopen subsets. In the ample setting it is invariant under Kakutani equivalence. ...

---

### 25. When do neural ordinary differential equations generalize on complex networks?

**Authors:** Moritz Laber, Tina Eliassi-Rad, Brennan Klein

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08980v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08980v1)

**Summary:** Neural ordinary differential equations (neural ODEs) can effectively learn dynamical systems from time series data, but their behavior on graph-structured data remains poorly understood, especially when applied to graphs with different size or structure than encountered during training. We study neural ODEs ($\mathtt{nODE}$s) with vector fields following the Barabási-Barzel form, trained on synthetic data from five common dynamical systems on graphs. Using the $\mathbb{S}^1$-model to generate gr...

---

### 26. Provably robust learning of regression neural networks using $β$-divergences

**Authors:** Abhik Ghosh, Suryasis Jana

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08933v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08933v1)

**Summary:** Regression neural networks (NNs) are most commonly trained by minimizing the mean squared prediction error, which is highly sensitive to outliers and data contamination. Existing robust training methods for regression NNs are often limited in scope and rely primarily on empirical validation, with only a few offering partial theoretical guarantees. In this paper, we propose a new robust learning framework for regression NNs based on the $β$-divergence (also known as the density power divergence) ...

---

### 27. Online monotone density estimation and log-optimal calibration

**Authors:** Rohan Hore, Ruodu Wang, Aaditya Ramdas

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08927v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08927v1)

**Summary:** We study the problem of online monotone density estimation, where density estimators must be constructed in a predictable manner from sequentially observed data. We propose two online estimators: an online analogue of the classical Grenander estimator, and an expert aggregation estimator inspired by exponential weighting methods from the online learning literature. In the well-specified stochastic setting, where the underlying density is monotone, we show that the expected cumulative log-likelih...

---

### 28. GEMSS: A Variational Bayesian Method for Discovering Multiple Sparse Solutions in Classification and Regression Problems

**Authors:** Kateřina Henclová, Václav Šmídl

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08913v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08913v1)

**Summary:** Selecting interpretable feature sets in underdetermined ($n \ll p$) and highly correlated regimes constitutes a fundamental challenge in data science, particularly when analyzing physical measurements. In such settings, multiple distinct sparse subsets may explain the response equally well. Identifying these alternatives is crucial for generating domain-specific insights into the underlying mechanisms, yet conventional methods typically isolate a single solution, obscuring the full spectrum of p...

---

### 29. Positive Distribution Shift as a Framework for Understanding Tractable Learning

**Authors:** Marko Medvedev, Idan Attias, Elisabetta Cornacchia, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08907v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08907v1)

**Summary:** We study a setting where the goal is to learn a target function f(x) with respect to a target distribution D(x), but training is done on i.i.d. samples from a different training distribution D'(x), labeled by the true target f(x). Such a distribution shift (here in the form of covariate shift) is usually viewed negatively, as hurting or making learning harder, and the traditional distribution shift literature is mostly concerned with limiting or avoiding this negative effect. In contrast, we arg...

---

### 30. Winner's Curse Drives False Promises in Data-Driven Decisions: A Case Study in Refugee Matching

**Authors:** Hamsa Bastani, Osbert Bastani, Bryce McLaughlin

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08892v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08892v1)

**Summary:** A major challenge in data-driven decision-making is accurate policy evaluation-i.e., guaranteeing that a learned decision-making policy achieves the promised benefits. A popular strategy is model-based policy evaluation, which estimates a model from data to infer counterfactual outcomes. This strategy is known to produce unwarrantedly optimistic estimates of the true benefit due to the winner's curse. We searched the recent literature on data-driven decision-making, identifying a sample of 55 pa...

---

### 31. Near-optimal Swap Regret Minimization for Convex Losses

**Authors:** Lunjia Hu, Jon Schneider, Yifan Wu

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08862v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08862v1)

**Summary:** We give a randomized online algorithm that guarantees near-optimal $\widetilde O(\sqrt T)$ expected swap regret against any sequence of $T$ adaptively chosen Lipschitz convex losses on the unit interval. This improves the previous best bound of $\widetilde O(T^{2/3})$ and answers an open question of Fishelson et al. [2025b]. In addition, our algorithm is efficient: it runs in $\mathsf{poly}(T)$ time. A key technical idea we develop to obtain this result is to discretize the unit interval into bi...

---

### 32. Cutting Through the Noise: On-the-fly Outlier Detection for Robust Training of Machine Learning Interatomic Potentials

**Authors:** Terry C. W. Lam, Niamh O'Neill, Christoph Schran, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08849v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08849v1)

**Summary:** The accuracy of machine learning interatomic potentials suffers from reference data that contains numerical noise. Often originating from unconverged or inconsistent electronic-structure calculations, this noise is challenging to identify. Existing mitigation strategies such as manual filtering or iterative refinement of outliers, require either substantial expert effort or multiple expensive retraining cycles, making them difficult to scale to large datasets. Here, we introduce an on-the-fly ou...

---

### 33. Amortising Inference and Meta-Learning Priors in Neural Networks

**Authors:** Tommy Rochussen, Vincent Fortuin

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08782v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08782v1)

**Summary:** One of the core facets of Bayesianism is in the updating of prior beliefs in light of new evidence$\text{ -- }$so how can we maintain a Bayesian approach if we have no prior beliefs in the first place? This is one of the central challenges in the field of Bayesian deep learning, where it is not clear how to represent beliefs about a prediction task by prior distributions over model parameters. Bridging the fields of Bayesian deep learning and probabilistic meta-learning, we introduce a way to $\...

---

### 34. Data Reconstruction: Identifiability and Optimization with Sample Splitting

**Authors:** Yujie Shen, Zihan Wang, Jian Qian, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08723v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08723v1)

**Summary:** Training data reconstruction from KKT conditions has shown striking empirical success, yet it remains unclear when the resulting KKT equations have unique solutions and, even in identifiable regimes, how to reliably recover solutions by optimization. This work hereby focuses on these two complementary questions: identifiability and optimization. On the identifiability side, we discuss the sufficient conditions for KKT system of two-layer networks with polynomial activations to uniquely determine...

---

### 35. The Theory and Practice of MAP Inference over Non-Convex Constraints

**Authors:** Leander Kurscheidt, Gabriele Masina, Roberto Sebastiani, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08681v2) | 📄 [PDF](https://arxiv.org/pdf/2602.08681v2)

**Summary:** In many safety-critical settings, probabilistic ML systems have to make predictions subject to algebraic constraints, e.g., predicting the most likely trajectory that does not cross obstacles. These real-world constraints are rarely convex, nor the densities considered are (log-)concave. This makes computing this constrained maximum a posteriori (MAP) prediction efficiently and reliably extremely challenging. In this paper, we first investigate under which conditions we can perform constrained M...

---

### 36. CauScale: Neural Causal Discovery at Scale

**Authors:** Bo Peng, Sirui Chen, Jiaguo Tian, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08629v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08629v1)

**Summary:** Causal discovery is essential for advancing data-driven fields such as scientific AI and data analysis, yet existing approaches face significant time- and space-efficiency bottlenecks when scaling to large graphs. To address this challenge, we present CauScale, a neural architecture designed for efficient causal discovery that scales inference to graphs with up to 1000 nodes. CauScale improves time efficiency via a reduction unit that compresses data embeddings and improves space efficiency by a...

---

### 37. Rho-Perfect: Correlation Ceiling For Subjective Evaluation Datasets

**Authors:** Fredrik Cumlin

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08552v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08552v1)

**Summary:** Subjective ratings contain inherent noise that limits the model-human correlation, but this reliability issue is rarely quantified. In this paper, we present $ρ$-Perfect, a practical estimation of the highest achievable correlation of a model on subjectively rated datasets. We define $ρ$-Perfect to be the correlation between a perfect predictor and human ratings, and derive an estimate of the value based on heteroscedastic noise scenarios, a common occurrence in subjectively rated datasets. We s...

---

### 38. Learning Credal Ensembles via Distributionally Robust Optimization

**Authors:** Kaizheng Wang, Ghifari Adam Faza, Fabio Cuzzolin, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08470v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08470v1)

**Summary:** Credal predictors are models that are aware of epistemic uncertainty and produce a convex set of probabilistic predictions. They offer a principled way to quantify predictive epistemic uncertainty (EU) and have been shown to improve model robustness in various settings. However, most state-of-the-art methods mainly define EU as disagreement caused by random training initializations, which mostly reflects sensitivity to optimization randomness rather than uncertainty from deeper sources. To addre...

---

### 39. Low Rank Transformer for Multivariate Time Series Anomaly Detection and Localization

**Authors:** Charalampos Shimillas, Kleanthis Malialis, Konstantinos Fokianos, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08467v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08467v1)

**Summary:** Multivariate time series (MTS) anomaly diagnosis, which encompasses both anomaly detection and localization, is critical for the safety and reliability of complex, large-scale real-world systems. The vast majority of existing anomaly diagnosis methods offer limited theoretical insights, especially for anomaly localization, which is a vital but largely unexplored area. The aim of this contribution is to study the learning process of a Transformer when applied to MTS by revealing connections to st...

---

### 40. Schrödinger bridge problem via empirical risk minimization

**Authors:** Denis Belomestny, Alexey Naumov, Nikita Puchkin, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08374v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08374v1)

**Summary:** We study the Schrödinger bridge problem when the endpoint distributions are available only through samples. Classical computational approaches estimate Schrödinger potentials via Sinkhorn iterations on empirical measures and then construct a time-inhomogeneous drift by differentiating a kernel-smoothed dual solution. In contrast, we propose a learning-theoretic route: we rewrite the Schrödinger system in terms of a single positive transformed potential that satisfies a nonlinear fixed-point equa...

---

### 41. All ERMs Can Fail in Stochastic Convex Optimization Lower Bounds in Linear Dimension

**Authors:** Tal Burla, Roi Livni

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08350v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08350v1)

**Summary:** We study the sample complexity of the best-case Empirical Risk Minimizer in the setting of stochastic convex optimization. We show that there exists an instance in which the sample size is linear in the dimension, learning is possible, but the Empirical Risk Minimizer is likely to be unique and to overfit. This resolves an open question by Feldman. We also extend this to approximate ERMs.   Building on our construction we also show that (constrained) Gradient Descent potentially overfits when ho...

---

### 42. Is Flow Matching Just Trajectory Replay for Sequential Data?

**Authors:** Soon Hoe Lim, Shizheng Lin, Michael W. Mahoney, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08318v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08318v1)

**Summary:** Flow matching (FM) is increasingly used for time-series generation, but it is not well understood whether it learns a general dynamical structure or simply performs an effective "trajectory replay". We study this question by deriving the velocity field targeted by the empirical FM objective on sequential data, in the limit of perfect function approximation. For the Gaussian conditional paths commonly used in practice, we show that the implied sampler is an ODE whose dynamics constitutes a nonpar...

---

### 43. Fast Flow Matching based Conditional Independence Tests for Causal Discovery

**Authors:** Shunyu Zhao, Yanfeng Yang, Shuai Li, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08315v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08315v1)

**Summary:** Constraint-based causal discovery methods require a large number of conditional independence (CI) tests, which severely limits their practical applicability due to high computational complexity. Therefore, it is crucial to design an algorithm that accelerates each individual test. To this end, we propose the Flow Matching-based Conditional Independence Test (FMCIT). The proposed test leverages the high computational efficiency of flow matching and requires the model to be trained only once throu...

---

### 44. Interaction-Grounded Learning for Contextual Markov Decision Processes with Personalized Feedback

**Authors:** Mengxiao Zhang, Yuheng Zhang, Haipeng Luo, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08307v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08307v1)

**Summary:** In this paper, we study Interaction-Grounded Learning (IGL) [Xie et al., 2021], a paradigm designed for realistic scenarios where the learner receives indirect feedback generated by an unknown mechanism, rather than explicit numerical rewards. While prior work on IGL provides efficient algorithms with provable guarantees, those results are confined to single-step settings, restricting their applicability to modern sequential decision-making systems such as multi-turn Large Language Model (LLM) d...

---

### 45. Noise Stability of Transformer Models

**Authors:** Themistoklis Haris, Zihan Zhang, Yuichi Yoshida

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08287v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08287v1)

**Summary:** Understanding simplicity biases in deep learning offers a promising path toward developing reliable AI. A common metric for this, inspired by Boolean function analysis, is average sensitivity, which captures a model's robustness to single-token perturbations. We argue that average sensitivity has two key limitations: it lacks a natural generalization to real-valued domains and fails to explain the "junta-like" input dependence we empirically observe in modern LLMs. To address these limitations, ...

---

### 46. A Statistical Framework for Alignment with Biased AI Feedback

**Authors:** Xintao Xia, Zhiqiu Xia, Linjun Zhang, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08259v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08259v1)

**Summary:** Modern alignment pipelines are increasingly replacing expensive human preference labels with evaluations from large language models (LLM-as-Judge). However, AI labels can be systematically biased compared to high-quality human feedback datasets. In this paper, we develop two debiased alignment methods within a general framework that accommodates heterogeneous prompt-response distributions and external human feedback sources. Debiased Direct Preference Optimization (DDPO) augments standard DPO wi...

---

### 47. Discrete Adjoint Schrödinger Bridge Sampler

**Authors:** Wei Guo, Yuchen Zhu, Xiaochen Du, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08243v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08243v1)

**Summary:** Learning discrete neural samplers is challenging due to the lack of gradients and combinatorial complexity. While stochastic optimal control (SOC) and Schrödinger bridge (SB) provide principled solutions, efficient SOC solvers like adjoint matching (AM), which excel in continuous domains, remain unexplored for discrete spaces. We bridge this gap by revealing that the core mechanism of AM is $\mathit{state}\text{-}\mathit{space~agnostic}$, and introduce $\mathbf{discrete~ASBS}$, a unified framewo...

---

### 48. Adaptive Matrix Online Learning through Smoothing with Guarantees for Nonsmooth Nonconvex Optimization

**Authors:** Ruichen Jiang, Zakaria Mhammedi, Mehryar Mohri, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08232v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08232v1)

**Summary:** We study online linear optimization with matrix variables constrained by the operator norm, a setting where the geometry renders designing data-dependent and efficient adaptive algorithms challenging. The best-known adaptive regret bounds are achieved by Shampoo-like methods, but they require solving a costly quadratic projection subproblem. To address this, we extend the gradient-based prediction scheme to adaptive matrix online learning and cast algorithm design as constructing a family of smo...

---

### 49. Thermodynamic Isomorphism of Transformers: A Lagrangian Approach to Attention Dynamics

**Authors:** Gunn Kim

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08216v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08216v1)

**Summary:** Although the Transformer architecture has revolutionized artificial intelligence, its underlying mechanisms remain largely heuristic and lack a unified physical theory. In this work, we propose a first-principles framework for information dynamics, treating the attention mechanism as a physical system governed by the principle of least action rather than as an algorithmic optimization. By mapping information states to a Riemannian manifold with the Fisher information metric, we derive the intell...

---

### 50. CADO: From Imitation to Cost Minimization for Heatmap-based Solvers in Combinatorial Optimization

**Authors:** Hyungseok Song, Deunsol Yoon, Kanghoon Lee, et al.

**Published:** 2026-02-09

🔗 [Paper](http://arxiv.org/abs/2602.08210v1) | 📄 [PDF](https://arxiv.org/pdf/2602.08210v1)

**Summary:** Heatmap-based solvers have emerged as a promising paradigm for Combinatorial Optimization (CO). However, we argue that the dominant Supervised Learning (SL) training paradigm suffers from a fundamental objective mismatch: minimizing imitation loss (e.g., cross-entropy) does not guarantee solution cost minimization. We dissect this mismatch into two deficiencies: Decoder-Blindness (being oblivious to the non-differentiable decoding process) and Cost-Blindness (prioritizing structural imitation ov...

---

