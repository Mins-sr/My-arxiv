# arXiv Daily Digest - 2026-06-05

Total papers: 250

---

## cs.AI

**50 papers**

### 1. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

**Authors:** Lizhi Yang, Junheng Li, Nehar Poddar, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06493v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06493v1)

**Summary:** For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface that is intuitive, general, modular, and expressive enough for diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid...

---

### 2. Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution

**Authors:** Liliana Hotsko, Yinxi Li, Yuntian Deng, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06492v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06492v1)

**Summary:** Code language models need repository-level context to resolve imports, APIs, and project conventions. Existing methods inject this knowledge as long inputs (retrieved through RAG or dependency analysis) or through per-repository fine-tuning and LoRA -- costly at repository scale and brittle to evolving codebases. We introduce Code2LoRA, a hypernetwork framework that generates repository-specific LoRA adapters, effectively injecting repository knowledge with zero inference-time token overhead. Co...

---

### 3. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

**Authors:** Dong Jing, Jingchen Nie, Tianqi Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06491v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06491v1)

**Summary:** Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion. Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache reuse, or reinforcement learning only shift the policy from one fixed speed to another, and leave deceleration almost unexplored. We observe that the magnitude of ...

---

### 4. Regret Minimization with Adaptive Opponents in Repeated Games

**Authors:** Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06486v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06486v1)

**Summary:** In this paper, we study regret minimization in repeated games with \emph{adaptive} opponents who can respond based on histories of play. The standard metric of \emph{external regret} in online learning is known to fail to capture such adaptivity. To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the \emph{realized} and the \emph{best-in-hindsight} accumulated utility when all playe...

---

### 5. Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection

**Authors:** Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06481v1)

**Summary:** As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for study...

---

### 6. Pretraining Recurrent Networks without Recurrence

**Authors:** Akarsh Kumar, Phillip Isola

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06479v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06479v1)

**Summary:** Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supe...

---

### 7. RREDCoT: Segment-Level Reward Redistribution for Reasoning Models

**Authors:** Mykyta Ielanskyi, Kajetan Schweighofer, Lukas Aichberger, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06475v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06475v1)

**Summary:** Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modifications thereof to steer the models to produce Chain-of-Thought (CoT) traces. The final answer can only be verified, and the reward assigned, after the CoT trace is complete, making it a delayed reward problem. GRPO and its modifications correspond to Monte Carlo methods in standard RL, which are k...

---

### 8. Self-Augmenting Retrieval for Diffusion Language Models

**Authors:** Paul Jünger, Justin Lovelace, Linxi Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06474v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06474v1)

**Summary:** Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the output and discarding the unconfident ones. We show that the discarded tokens are in fact a useful lookahead signal for retrieval-augmented generation: even low-confidence tokens often surface salient entities early in the denoising trajectory, enabling retrieval of stronger evi...

---

### 9. MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

**Authors:** Shangheng Du, Xiangchao Yan, Jinxin Shi, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06473v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06473v1)

**Summary:** Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, existing MLE agents suffer from inter-branch information isolation, memoryless search, and lack of hierarchical control, which together hinder long-horizon optimization. We present MLEvolve, an LLM-based self-evolving multi-agent framework for end-to-end machine learning algorithm di...

---

### 10. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training

**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06470v1)

**Summary:** We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-t...

---

### 11. Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement

**Authors:** Jui-Hui Chung, Ziyang Cai, Zihao Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06468v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06468v1)

**Summary:** We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas that builds up to the main theorem. First, Goedel-Architect generates a blueprint of formally stated definitions and lemmas, along with declared dependencies. This blueprint is optionally guided by a natural language proof. Then, a tool-equipped Lean prover component closes each open lemma node in par...

---

### 12. You Only Index Once: Cross-Layer Sparse Attention with Shared Routing

**Authors:** Yutao Sun, Yanqi Zhang, Li Dong, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06467v1)

**Summary:** Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse methods typically provide stronger acceleration but incur noticeable quality loss, while token sparse methods are usually more accurate yet deliver limited end-to-end speedup because top-k routing over...

---

### 13. Benchmark Everything Everywhere All at Once

**Authors:** Shiyun Xiong, Dongming Wu, Peiwen Sun, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06462v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06462v1)

**Summary:** Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse, raising concerns about sustainability and scalability. Moreover, existing benchmarks often quickly reach performance saturation after their release, resulting in insufficient discrimination among state-of-the-art models. To address these challenges, we introduce Benchmark Agent, a fully autonomous ...

---

### 14. Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals

**Authors:** Thamilvendhan Munirathinam

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06460v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06460v1)

**Summary:** As autonomous LLM agents increasingly hold real credentials and operate infrastructure without a human in the loop, operators have no standard way to tell an agent that a resource is off-limits. Access controls either let the agent in (it has valid credentials) or hard-fail it (indistinguishable from any other client). We propose a third mode: a lightweight, published in-band deny signal -- the Recuse Signal -- that a server emits over a protocol's existing channels (an SSH banner, a PostgreSQL ...

---

### 15. In-Context Multiple Instance Learning

**Authors:** Alexander Möllers, Marvin Sextro, Julius Hense, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06458v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06458v1)

**Summary:** Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to satellite imagery. Nevertheless, existing algorithms struggle in the low-label regime that characterizes many real-world applications. Flexible models overfit and rigid ones fail to adapt to the task at hand. We show that pretraining an in-context learner with a Perceiver-style architecture on synt...

---

### 16. Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents

**Authors:** Zhuoming Chen, Xinrui Zhong, Qilong Feng, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06453v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06453v1)

**Summary:** Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms at scale remains highly engineering-intensive, slowing both human researchers and AI agents in exploring the sparse attention design. To address this challenge, we present Vortex, a system that combines a Python-embedded frontend language atop a page-centric tensor abstraction for expressing a broad ...

---

### 17. Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

**Authors:** Yasmine Omri, Ziyu Gan, Zachary Broveak, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06448v1)

**Summary:** LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza...

---

### 18. RiskFlow: Fast and Faithful Safety-Critical Traffic Scenario Generation

**Authors:** Qi Lan, Yining Tang, Yu Shen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06423v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06423v1)

**Summary:** Safety-critical traffic scenario generation is essential for evaluating autonomous driving systems under rare but high-risk interactions. Existing diffusion-based methods offer strong controllability in closed-loop generation, but their iterative denoising process is computationally expensive and may accumulate sampling and guidance errors over long rollouts, causing unrealistic motion artifacts such as jitter, abnormal acceleration, and off-road behavior. To address these issues, we propose Ris...

---

### 19. Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss

**Authors:** Thomas T. Zhang, Alok Shah, Yifei Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06418v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06418v1)

**Summary:** Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., $L^2$ regression, cross-entropy), but deploy the network by rolling out along its own predictions. Key examples include autoregressive language modeling, flow-based generative modeling, and robot policy learning. It is well-documented that these settings induce a phenomenon we call test-time feedback (TTF): the mismatch between the training/validation loss and downstream metrics of i...

---

### 20. Unsupervised Skill Discovery for Agentic Data Analysis

**Authors:** Zhisong Qiu, Kangqi Song, Shengwei Tang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06416v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06416v1)

**Summary:** Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guid...

---

### 21. Risk Assessment of Autonomous Driving: Integrating Technical Failures, Ethical Dilemmas, and Policy Frameworks

**Authors:** Boyi Chen, Shengqin Chu, Zicheng Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06396v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06396v1)

**Summary:** Autonomous driving technology has the potential to reduce the large number of road traffic accidents caused by human error each year, but it also brings new types of risks that need to be evaluated from the aspects of technology, ethics and regulations. Based on public crash data from the National Highway Traffic Safety Administration (NHTSA), disengagement reports from the California Department of Motor Vehicles (DMV), the MIT Moral Machines dataset, and a comparative regulatory analysis of fiv...

---

### 22. HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes

**Authors:** Wenbo Li, Xiaoliang Ju, Zipeng Qin, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06390v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06390v1)

**Summary:** Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing methods often rely on hand-crafted rules or focus on isolated sub-tasks (e.g., floorplan synthesis or single-room furnishing), producing whole-home scenes that lack global coherence, realism, and simulation readiness. To mitigate these limitations, we propose a unified hierarchical framework that decom...

---

### 23. Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration

**Authors:** Jiaju Chen, Yuxuan Lu, Jiayi Su, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06388v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06388v1)

**Summary:** Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effective collaboration, however, requires collaborators to continuously maintain and align mental models of their own reasoning,partners' intentions, and shared goals during the collaborative process. Today's agents rarely develop such capabilities since they are primarily optimized for task completion, a...

---

### 24. Emergent Language as an Approach to Conscious AI

**Authors:** Zengqing Wu, Chuan Xiao

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06380v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06380v1)

**Summary:** The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of sel...

---

### 25. EasyLens: A Training-Free Plug-and-Play Subtle-Lesion Representation Amplifier for Medical Vision-Language Models

**Authors:** Qiwei Zeng, Hao Wang, Jinghao Lin, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06379v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06379v1)

**Summary:** Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation, including lesion detection and report generation. However, their practical utility remains limited by insufficient sensitivity to subtle lesions, whose visual evidence is often sparse, low-contrast, and embedded within complex anatomical context. As local visual tokens are aggregated, these weak lesion cues can become underrepresented in global image representations, making them difficult for...

---

### 26. Rethinking Infrastructure Inspection as Image Difference Classification: A Traffic Sign Case Study

**Authors:** Ching Yau Fergus Mok, Lavindra de Silva, Varun Kumar Reja, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06375v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06375v1)

**Summary:** Digital twins (DTs) allow the digitalization of road infrastructure inspection, though this is hindered by limited annotated data. This work exploits the relational nature of continuous asset condition monitoring to reformulate image-based defect detection as image difference classification (IDC) to reduce data reliance. This was evaluated in a case study on low-resource traffic sign inspection with different IDC classifiers using a newly-curated, high quality dataset. Results indicate that the ...

---

### 27. LatentWave: JEPA Pretraining for Wireless Foundation Models

**Authors:** Ahmed Mohamed, Ahmed Aboulfotouh, Hatem Abou-Zeid

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06373v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06373v1)

**Summary:** Wireless foundation models have emerged as a promising alternative to building separate models for each wireless task. However, existing approaches rely on masked input reconstruction, which can bias representations toward low-level signal details. In this paper, we propose LatentWave, a wireless foundation model pretrained using a Joint-Embedding Predictive Architecture (JEPA) on diverse wireless spectrograms and channel state information (CSI). By predicting masked regions in latent space, Lat...

---

### 28. An Infectious Disease Spread Simulation Based on Large Language Model Decision Making

**Authors:** Yonchanok Khaokaew, Ruochen Kong, Andreas Zufle, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06360v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06360v1)

**Summary:** Modelling individual decision-making during infectious disease outbreaks is crucial for understanding behavioural dynamics and informing effective public health interventions. Prior work has shown that large language models can simulate realistic human behaviour by generating agent decisions based on demographic prompts and situational context. We build on this foundation with a spatially grounded, agent-based simulation framework that integrates LLM-generated decisions about self-reported influ...

---

### 29. F3-Tokenizer: Taming Audio Autoencoder Latents for Understanding and Generation

**Authors:** Dinghao Zhou, Xingchen Song, Di Wu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06357v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06357v1)

**Summary:** Continuous audio autoencoders reconstruct waveforms well but often produce latents with weak structure for understanding, while self-supervised audio encoders capture semantics but are not directly decodable. This mismatch complicates a single audio tokenizer that must support both understanding and generation. We adapt continuous autoencoder latents to this setting with two components: a noise-regularized autoencoder bottleneck and a latent-side representation encoder. The bottleneck uses chann...

---

### 30. Where Should Knowledge Enter? A Layered Framework for Knowledge Infusion in Multimodal Iterative Generative Mo

**Authors:** Renjith Prasad, Chathurangi Shyalika, Anushka Pawar, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06356v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06356v1)

**Summary:** Multimodal generative models produce fluent outputs but remain unreliable when generation must respect structured, domain-specific, or safety-critical knowledge. Existing methods incorporate knowledge through mechanisms such as prompt augmentation, guidance, latent editing, or fine-tuning, yet they are typically categorized by technique rather than by the component of the generative process they modify. We argue that knowledge infusion in iterative generative models is fundamentally aninterventi...

---

### 31. Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation

**Authors:** Yohann Benchetrit, Marlène Careil, Simon Dahan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06345v1)

**Summary:** Brain decoding is limited by the availability of labeled neural data, and remains challenging in low-data regimes. To address this issue, we investigate whether and when brain decoding can be boosted by augmenting small fMRI datasets with synthetic data generated by a pretrained model of fMRI responses to stimuli. We use TRIBE v2, a large encoding model pretrained on more than 1000 hours of fMRI responses to video, audio and language. For each dataset, we evaluate systematic grids that show how ...

---

### 32. TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management

**Authors:** Shweta Mishra

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06337v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06337v1)

**Summary:** Large language model (LLM) deployments for long-horizon tasks face a fundamental constraint: context windows are finite while productive work sessions are not. When history exceeds the Maximum Effective Context Window (MECW), critical structured information - architectural decisions, task transitions, file histories - is silently discarded. Existing mitigations treat history as flat text, destroying the relational structure that makes sessions resumable. We present TokenMizer, an open-source pro...

---

### 33. Bridging Domain Expertise and Generalization for Performance Estimation

**Authors:** Shuxuan Li, Zhilin Zhao, Quyu Kong, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06335v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06335v1)

**Summary:** Performance estimation under distribution shift aims to predict how a model behaves on an unlabeled test set whose distribution differs from the training data, a scenario that requires reliable indicators that can faithfully reflect model behavior without ground-truth labels. Existing approaches rely solely on the outputs of the given model whose biases are amplified once the distribution shifts, weakening the correlation with the true performance. Motivated by this limitation, we propose Fused ...

---

### 34. Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability

**Authors:** Seyed Arshan Dalili, Mehrdad Mahdavi

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06333v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06333v1)

**Summary:** Sparse Autoencoders (SAEs) are widely used for mechanistic interpretability in large language models, yet their formulation assigns each latent feature a single decoder direction, implicitly assuming features to be one-dimensional. We show that this assumption mismatches with the multi-dimensional structure of model features, provably inducing feature splitting through two distinct mechanisms. Geometrically, reconstructing a feature of intrinsic dimension $d_i \ge 2$ to error $\varepsilon$ with ...

---

### 35. PAMF: Prior-Aware Multimodal Fusion for Incomplete Time Series Data

**Authors:** Ziwen Kan, Wugeng Zheng, Tianlong Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06328v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06328v1)

**Summary:** In healthcare, multimodal time series tasks often operate on incomplete observations in practice, for example when ECG segments are lost because electrodes detach or an entire respiratory channel is unavailable during overnight monitoring. Such missingness typically appears in two structurally distinct patterns: within-modality missing, where values are absent within an otherwise observed modality, and modality-level missing, where an entire modality is unavailable. Existing methods typically re...

---

### 36. DragOn: A Benchmark and Dataset for Drag-Based GUI Interactions

**Authors:** Nathan Bout, Maxime Langevin, Ronan Riochet

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06322v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06322v1)

**Summary:** GUI agents - vision-based models that control desktops, web browsers, and mobile devices through graphical user interfaces - promise to automate a wide range of digital tasks. While million-scale datasets have enabled substantial progress on click-grounding, drag grounding (e.g. drag-and-drop, swipe, highlight) data remains an order of magnitude smaller and current models fall short on complex drag-based interactions. We introduce DragOn, a drag grounding benchmark and training dataset covering ...

---

### 37. Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

**Authors:** Gizem Yüce, Giorgos Nikolaou, Nicolas Flammarion

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06320v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06320v1)

**Summary:** Machine unlearning aims to remove targeted knowledge from a trained model while preserving its general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. Existing approaches either ignore this heterogeneity or rely on auxiliary models, heuristics, or external annotations to estimate each token's relevance for forgetting. We instead characterize it through the interaction with the retain objective: a token is forget-specific to ...

---

### 38. Quantum enhanced rare event discovery and sampling

**Authors:** Naixu Guo, Po-Wei Huang, Qisheng Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06316v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06316v1)

**Summary:** Financial crashes, cascading failures in infrastructure, and critical errors in AI systems are frequently triggered by events that occur with extremely small probability. Efficiently discovering and sampling events with probability below a threshold is therefore of critical interest. Yet this task is highly non-trivial using existing classical or quantum methods. Being rare, such events require an immense sampling overhead to collect sufficient data samples. Moreover, because the rare events are...

---

### 39. LLM Self-Recognition: Steering and Retrieving Activation Signatures

**Authors:** Thibaud Ardoin, Jonas Schäfer, Gerhard Wunder

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06315v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06315v1)

**Summary:** Recent advances in interpretability suggest that large language models (LLMs) implicitly encode signals in their generated text that enable self-recognition of their outputs. We demonstrate that this capability is reliable, even in low-entropy scenarios, and that it can be amplified through targeted intervention. By steering the internal residual stream during generation with a random sparse vector, we create a detectable fingerprint that enables attribution of a given text to a specific LLM. Th...

---

### 40. AIS-Based Vessel Trajectory Prediction Using Memory-Augmented Neural Networks

**Authors:** Wonmo Koo, Sanha Chang, Heeyoung Kim

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06311v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06311v1)

**Summary:** Accurate vessel trajectory prediction is essential for safe and efficient maritime operations, enabling collision avoidance and supporting route optimization. Although memory-augmented neural networks have recently shown strong performance in pedestrian and road-vehicle trajectory prediction by selectively retrieving relevant information from an external memory, their potential for vessel trajectory prediction remains underexplored. This paper presents an empirical investigation of memory-based ...

---

### 41. Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction

**Authors:** Hongkun Dou, Zike Chen, Fengji Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06303v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06303v1)

**Summary:** Controllable generation with discrete diffusion models is often hindered by high computational overhead or the need for retraining. In this paper, we present \underline{\textbf{G}}radient-\underline{\textbf{I}}nformed \underline{\textbf{L}}ogit \underline{\textbf{C}}orrection (\textbf{GILC}), a plug-and-play framework that efficiently estimates guidance signals by repurposing the pretrained denoising network as a variational proxy. To circumvent the gradient instability inherent in high-dimensio...

---

### 42. Multi-ResNets for Subspace Preconditioning in Constrained Optimization

**Authors:** Merve Karakas, Christopher J. Williams, Emmanuel O. Balogun, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06300v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06300v1)

**Summary:** We propose MResOpt, a staged residual neural network architecture for constrained optimization problems. Our architecture fits within predict-complete-correct pipelines and decomposes constraint satisfaction by priority through intermediate re-completion and stage-aware losses. The framework enables domain-informed ordered constraint satisfaction which allows the network to utilize ordinal structure when present. Under an idealized infinite-width regime, we show that our design behaves as sequen...

---

### 43. Towards One-to-Many Temporal Grounding

**Authors:** Qi Xu, Yue Tan, Shihao Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06294v1)

**Summary:** Temporal Grounding (TG) aims to localize video segments corresponding to a textual query. Prior research predominantly focuses on single-segment retrieval. Real-world scenarios, however, often require localizing multiple disjoint segments for a single query -- a setting we term One-to-Many Temporal Grounding (OMTG). Previous state-of-the-art MLLMs, optimized for one-to-one settings, struggle in this context, often yielding near-zero scores due to a lack of event cardinality perception. To bridge...

---

### 44. LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs

**Authors:** Gianluca Barmina, Peter Schneider-Kamp, Lukas Galke Poech

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06286v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06286v1)

**Summary:** Large language models can reproduce training data, but existing memorization evaluations mostly measure whether models can be forced to do so, rather than whether they do so under ordinary use. We introduce PropMe, a propensity-aware framework for memorization evaluation that contrasts prefix-based capability attacks with non-adversarial evaluations. We propose a metric transformation that, applied to existing functions, allows to create propensity metrics. We further introduce SimpleTrace, a li...

---

### 45. TRACE: A Temporal Conditional Estimation for Multimodal Time Series Foundation Models

**Authors:** Ziwen Kan, Yishuo Chen, Kecheng Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06285v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06285v1)

**Summary:** Time series foundation models (TS-FMs) aim to learn generalizable temporal representations that can be adapted to a wide range of downstream tasks. In real-world multimodal settings, time series are frequently affected by temporal misalignment and partial modality missingness, where different modalities are observed at heterogeneous time scales or are partially absent. Existing approaches typically rely on naive imputation or masking strategies, which fail to account for cross-modal dependencies...

---

### 46. ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents

**Authors:** Rahul Suresh Babu, Laxmipriya Ganesh Iyer

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06284v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06284v1)

**Summary:** Large language model agents increasingly rely on external tools, but larger tool menus can reduce reliability and efficiency by increasing wrong-tool calls, premature actions, and token cost. Existing tool-selection methods often optimize semantic relevance, exposing tools whose names or descriptions match the user request. We argue that relevance is insufficient: a tool may be related to the task while still being unnecessary or premature at the current step.   We propose Causal Minimal Tool Fi...

---

### 47. Adapting Diffusion Language Models for Lossless Pixel-Level Image Transmission

**Authors:** Tianqi Ren, Rongpeng Li, Xianfu Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06273v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06273v1)

**Summary:** Lossless pixel-level image transmission is a fundamental regime beyond semantic communications, because exact recovery requires both accurate symbol probability modeling and reliable delivery over noisy channels. This paper proposes DDM-SSCC, a discrete-diffusion-model-based separate source-channel coding framework for lossless image transmission. Different from raster-order autoregressive coding, the proposed source codec adapts a diffusion language model to pixel-token restoration and performs...

---

### 48. Your GFlowNet Secretly Learns an Optimal Transport Plan

**Authors:** Ian Maksimov, Nikita Morozov, Denis Belomestny, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06272v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06272v1)

**Summary:** Generative Flow Networks (GFlowNets) are a framework for sampling structured objects via stochastic trajectories in a directed graph. In this work, we establish a theoretical connection between non-acyclic GFlowNets and optimal transport (OT). We show that fixing the initial flow distribution in a minimum-flow GFlowNet reduces its objective to a Kantorovich OT problem with graph-induced shortest path costs. At the optimum, the learned GFlowNet policy therefore encodes an optimal transport plan f...

---

### 49. DAST: A VLM-LLM Framework for Cross-Interface Anomaly Detection in O-RAN

**Authors:** Francesco Spinelli, Esteban Municio, Pau Baguer, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06261v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06261v1)

**Summary:** O-RAN enables a disaggregated baseband stack with programmable functions that communicate over standardized open interfaces. The same openness that enables multi-vendor composition also expands the attack surface across logically decoupled tiers that make up the compute continuum. Among these threats, Denial-of-Service and performance-degradation attacks, which account for the majority of catalogued O-RAN threats, are particularly difficult to detect. Traditional Time-Series Anomaly Detection (T...

---

### 50. OneReason Technical Report

**Authors:**  OneRec Team, Biao Yang, Boyang Ding, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06260v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06260v1)

**Summary:** Generative recommendation models in the OneRec family have been widely deployed in many real-world services, such as short-video, live-streaming, advertising, and e-commerce. However, these generative models can only benefit from the scaling advantage, while their reasoning ability is hard to activate, since we cannot construct meaningful Chain-of-Thought (CoT) sequences consisting of itemic tokens only. Inspired by the success of the reasoning-style ``think before answer'' paradigm in the LLM f...

---

## cs.CL

**50 papers**

### 1. Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution

**Authors:** Liliana Hotsko, Yinxi Li, Yuntian Deng, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06492v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06492v1)

**Summary:** Code language models need repository-level context to resolve imports, APIs, and project conventions. Existing methods inject this knowledge as long inputs (retrieved through RAG or dependency analysis) or through per-repository fine-tuning and LoRA -- costly at repository scale and brittle to evolving codebases. We introduce Code2LoRA, a hypernetwork framework that generates repository-specific LoRA adapters, effectively injecting repository knowledge with zero inference-time token overhead. Co...

---

### 2. Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection

**Authors:** Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06481v1)

**Summary:** As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for study...

---

### 3. Self-Augmenting Retrieval for Diffusion Language Models

**Authors:** Paul Jünger, Justin Lovelace, Linxi Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06474v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06474v1)

**Summary:** Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the output and discarding the unconfident ones. We show that the discarded tokens are in fact a useful lookahead signal for retrieval-augmented generation: even low-confidence tokens often surface salient entities early in the denoising trajectory, enabling retrieval of stronger evi...

---

### 4. MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

**Authors:** Shangheng Du, Xiangchao Yan, Jinxin Shi, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06473v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06473v1)

**Summary:** Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, existing MLE agents suffer from inter-branch information isolation, memoryless search, and lack of hierarchical control, which together hinder long-horizon optimization. We present MLEvolve, an LLM-based self-evolving multi-agent framework for end-to-end machine learning algorithm di...

---

### 5. You Only Index Once: Cross-Layer Sparse Attention with Shared Routing

**Authors:** Yutao Sun, Yanqi Zhang, Li Dong, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06467v1)

**Summary:** Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse methods typically provide stronger acceleration but incur noticeable quality loss, while token sparse methods are usually more accurate yet deliver limited end-to-end speedup because top-k routing over...

---

### 6. Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?

**Authors:** Mandana Samiei, Eunice Yiu, Anthony GX-Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06464v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06464v1)

**Summary:** A long-standing finding in the causal learning literature is that adults struggle to identify conjunctive causal rules, where an effect requires the simultaneous presence of multiple causes, while performing better in disjunctive settings. However, most demonstrations of this ``conjunctive handicap'' rely on passive observation paradigms with limited evidence, where learners have no control over evidence generation. This paper asks whether this bias persists when adults are granted agency throug...

---

### 7. Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Code-Generation Skill

**Authors:** Mehmet Iscan

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06454v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06454v1)

**Summary:** Large language models increasingly write, review, and judge code, and a fast-growing practice equips them with prompt 'skills' that ask the model to reason like a scientist. A prominent example tells the model to act as a Popperian falsificationist, and such skills are reported to improve generated code. But these gains are almost always read off an LLM-as-a-judge, an instrument with documented positional, self-preference, and stylistic biases. We ask: if it appears to help, is the gain from the...

---

### 8. Latent Reasoning with Normalizing Flows

**Authors:** Guancheng Tu, Xiangjun Fu, Suhao Yu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06447v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06447v1)

**Summary:** Large language models often improve reasoning by generating explicit chain-of-thought (CoT), demonstrating the importance of intermediate computation. However, textual CoT forces this computation through a discrete, serial, and communication-oriented token stream: each reasoning step must be verbalized before the model can proceed, even when the underlying update is semantic, uncertain, or only partially formed. Latent reasoning offers a higher-bandwidth alternative by performing intermediate co...

---

### 9. USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding

**Authors:** Heng-Jui Chang, Alexander H. Liu, Saurabhchand Bhati, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06444v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06444v1)

**Summary:** Audio encoders are critical to modern audio applications as large language models (LLMs) increasingly rely on a single encoder for diverse inputs. While self-supervised learning (SSL) has yielded strong domain-specific encoders like speech or music experts, multi-domain approaches like USAD and SPEAR remain limited in coverage and evaluation. Recent studies also suggest supervised encoders align better with audio LLMs. We present USAD 2.0, a universal encoder integrating knowledge from both SSL ...

---

### 10. Revising Context, Shifting Simulated Stance: Auditing LLM-Based Stance Simulation in Online Discussions

**Authors:** Xinnong Zhang, Wanting Shan, Hanjia Lyu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06443v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06443v1)

**Summary:** Large language models are increasingly used to simulate social media users and infer how individuals may respond to online discussions. However, it remains unclear whether these simulations reflect precise user-specific beliefs or whether they are highly sensitive to semantically independent changes in conversational contexts. In this work, we study counterfactual context revision as a framework for auditing LLM-based stance simulation. Given an original online conversation, we first infer a tar...

---

### 11. Reinforcement Learning Elicits Contextual Learning of Unseen Language Translation

**Authors:** Hanxu Hu, Zdeněk Šnajdr, Pinzhen Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06428v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06428v1)

**Summary:** Prior work has shown that large language models (LLMs) can translate unseen or low-resource languages by undergoing continued training or even by encoding a grammar book in their context. However, both methods typically overfit specific languages, with limited zero-shot transfer at test time. To translate extremely low-resource languages at scale, we argue that LLMs must acquire the meta-skill of utilizing in-context linguistic knowledge rather than memorizing specific languages. In this paper, ...

---

### 12. A Komi-Yazva--Russian Parallel Corpus and Evaluation Protocol for Zero- and Few-Shot LLM Translation

**Authors:** Petr Parshakov

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06420v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06420v1)

**Summary:** We present the first Komi-Yazva--Russian parallel corpus together with an explicit evaluation protocol for studying LLM translation in an endangered, extremely low-resource setting. The dataset contains 457 aligned sentence pairs from 74 narrative texts and is accompanied by documented provenance, sentence-level alignment, and story identifiers that enable leakage-aware evaluation. We use this setup to compare modern large language models on Komi-Yazva-to-Russian translation under severe paralle...

---

### 13. Unsupervised Skill Discovery for Agentic Data Analysis

**Authors:** Zhisong Qiu, Kangqi Song, Shengwei Tang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06416v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06416v1)

**Summary:** Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guid...

---

### 14. CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments

**Authors:** Jiaju Chen, Bo Sun, Yuxuan Lu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06399v1)

**Summary:** Multi-agent systems (MAS) built on large language models have shown growing promise, with their effectiveness resting on agents' ability to coordinate through text-based channels much as human teams do. Yet recent study suggests that MAS often falter not because agents lack individual task-solving ability, but because they lack collaborative competence: the capacity to establish common ground, maintain shared task understanding, balance individual and collective incentives, and repair misalignme...

---

### 15. Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration

**Authors:** Jiaju Chen, Yuxuan Lu, Jiayi Su, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06388v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06388v1)

**Summary:** Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effective collaboration, however, requires collaborators to continuously maintain and align mental models of their own reasoning,partners' intentions, and shared goals during the collaborative process. Today's agents rarely develop such capabilities since they are primarily optimized for task completion, a...

---

### 16. Emergent Language as an Approach to Conscious AI

**Authors:** Zengqing Wu, Chuan Xiao

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06380v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06380v1)

**Summary:** The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of sel...

---

### 17. EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading

**Authors:** Zhihao Wu, Linhai Zhang, Taiyi Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06350v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06350v1)

**Summary:** Reliable rubric grading requires more than accurate score prediction. Each judgement must be grounded in the mark scheme and evidence from the student answer. Existing credit-assignment and intervention methods, primarily designed for self-contained reasoning tasks such as mathematics reasoning, struggle in this setting because they do not identify where grading reasoning goes wrong or how the model's belief about the final mark changes during reasoning. We propose Evidence-Diagnosed Interventio...

---

### 18. "Chi nas dal soch el sent de legn" -- Auditing Text Corpora for Lombard

**Authors:** Edoardo Signoroni, Pavel Rychlý

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06349v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06349v1)

**Summary:** Several of the world's languages are still under-resourced in terms of Natural Language Processing (NLP) tools. This is mostly due to the lack of high-quality datasets to train, develop, and evaluate systems and models for several tasks, such as Machine Translation (MT). We conduct a manual audit of the parallel and monolingual corpora available for Lombard, an under-resourced language continuum from Italy. Our analysis reveals that the perceived abundance of web-scraped data is an illusion, wit...

---

### 19. Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

**Authors:** Gizem Yüce, Giorgos Nikolaou, Nicolas Flammarion

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06320v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06320v1)

**Summary:** Machine unlearning aims to remove targeted knowledge from a trained model while preserving its general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. Existing approaches either ignore this heterogeneity or rely on auxiliary models, heuristics, or external annotations to estimate each token's relevance for forgetting. We instead characterize it through the interaction with the retain objective: a token is forget-specific to ...

---

### 20. Decomposing Factual Sycophancy in Language Models: How Size and Instruction Tuning Shape Robustness

**Authors:** Victor De Marez, Luna De Bruyne, Walter Daelemans

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06306v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06306v1)

**Summary:** Factual sycophancy occurs when a language model abandons a correct, verifiable answer under social pressure. Because a flip occurs only when pressure toward a false answer exceeds the model's neutral preference for the truth, flip rates conflate two mechanisms: the strength of that baseline preference (truth margin), and how far pressure shifts it (manipulation sensitivity). We decompose factual sycophancy into these channels and use them to separate the effects of size and instruction tuning ac...

---

### 21. LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs

**Authors:** Gianluca Barmina, Peter Schneider-Kamp, Lukas Galke Poech

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06286v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06286v1)

**Summary:** Large language models can reproduce training data, but existing memorization evaluations mostly measure whether models can be forced to do so, rather than whether they do so under ordinary use. We introduce PropMe, a propensity-aware framework for memorization evaluation that contrasts prefix-based capability attacks with non-adversarial evaluations. We propose a metric transformation that, applied to existing functions, allows to create propensity metrics. We further introduce SimpleTrace, a li...

---

### 22. FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays

**Authors:** Yijun Liu, Yifan Song, John Gallagher, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06271v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06271v1)

**Summary:** While large language models (LLMs) are increasingly used to generate writing feedback, there remains no systematic comparison of LLM and expert feedback on the dimensions that writing research identifies as central to revision: goal-orientation, anchoring to specific sentences, and prioritization. We introduce FOXGLOVE, a dataset of 696 feedback comments written by trained writing instructors on 69 twelfth-grade argumentative essays, paired with 1,644 comments generated from four frontier LLMs u...

---

### 23. Many Circuits, One Mechanism: Input Variation and Evaluation Granularity in Circuit Discovery

**Authors:** Alireza Bayat Makou, Jingcheng Niu, Subhabrata Dutta, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06267v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06267v1)

**Summary:** Circuit discovery methods identify subgraphs that explain specific model behaviors, and structural differences between discovered circuits are commonly interpreted as evidence of distinct mechanisms. We test this assumption by varying input statistics while holding the task fixed, and show that the resulting structural differences exhibit apparent specialization but do not correspond to functional differences, a pattern we term phantom specialization. Using Literal Sequence Copying across four t...

---

### 24. From Self to Other: Evaluating Demographic Perspective-Taking in LLM Hate Speech Annotation

**Authors:** Paloma Piot, Javier Parapar

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06266v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06266v1)

**Summary:** Hate speech detection is inherently subjective: people from different demographic groups perceive the same content very differently. Collecting enough annotations from multiple demographic groups is costly and difficult to scale. Persona-conditioned Large Language Models (models prompted to adopt a specific demographic identity) have been proposed as a way to simulate diverse perspectives at scale. But do they actually reflect how different groups disagree? We evaluate three aspects of human soc...

---

### 25. OneReason Technical Report

**Authors:**  OneRec Team, Biao Yang, Boyang Ding, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06260v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06260v1)

**Summary:** Generative recommendation models in the OneRec family have been widely deployed in many real-world services, such as short-video, live-streaming, advertising, and e-commerce. However, these generative models can only benefit from the scaling advantage, while their reasoning ability is hard to activate, since we cannot construct meaningful Chain-of-Thought (CoT) sequences consisting of itemic tokens only. Inspired by the success of the reasoning-style ``think before answer'' paradigm in the LLM f...

---

### 26. Benchmarking Open-Source Layout Detection Models for Data Snapshot Extraction from Institutional Documents

**Authors:** AJ Carl P. Dy, Aivin V. Solatorio

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06242v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06242v1)

**Summary:** Institutional documents contain substantial amounts of operational and analytical information embedded within figures and tables. Current approaches for extracting visual content from documents are largely built around generic document layout analysis, where figures and tables are treated as uniformly relevant document objects rather than semantically meaningful analytical artifacts. In this work, we introduce a benchmark dataset and evaluation framework for \textit{data snapshot extraction}, th...

---

### 27. FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition

**Authors:** Fernando López, Santosh Kesiraju, Jordi Luque

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06211v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06211v1)

**Summary:** Automatic speech recognition (ASR) has advanced remarkably for standard speech; however, pathological speech from neurological conditions remains a significant challenge. We investigate speaker conditioning via Feature-wise Linear Modulation (FiLM), injecting x-vector-derived information into each transformer layer of a frozen ASR encoder to adapt internal representations to individual pathological speakers without modifying base model weights. We benchmark this for the ASR task against standard...

---

### 28. Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs

**Authors:** Giovanni Dettori, Matteo Boffa, Danilo Giordano, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06203v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06203v1)

**Summary:** Input length and the position of relevant information are widely cited as the primary causes of degraded LLM long-context performance. Here, we study lexical density -- the rate at which a context introduces distinct information -- as a third, largely overlooked factor that systematically reduces the effective context window of LLMs. We quantify the impact of lexical density on open-weight LLMs (9B-685B) using three "find-the-needle" style benchmarks with identical length (~12k tokens) and contr...

---

### 29. Improving Answer Extraction in Context-based Question Answering Systems Using LLMs

**Authors:** Hafez Abdelghaffar, Ahmed Alansary, Ali Hamdi

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06197v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06197v1)

**Summary:** Question answering (QA) systems have achieved notable progress with the advent of large language models (LLMs). However, they still face challenges in accurately extracting and generating precise answers from given contexts, particularly when dealing with complex or ambiguous queries. Existing approaches often struggle with contextual understanding, answer consistency, and generalization across diverse domains. In this work, we propose a question answering system based on large language models, ...

---

### 30. The Tell-Tale Norm: $\ell_2$ Magnitude as a Signal for Reasoning Dynamics in Large Language Models

**Authors:** Jinyang Zhang, Hongxin Ding, Yue Fang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06188v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06188v1)

**Summary:** Recent work has sought to understand Large Language Models (LLMs) reasoning, yet a principled, model-intrinsic signal that captures its layer-wise reasoning dynamics remains underexplored. We bridge this gap by demonstrating that the l2 norm of hidden states serves as an endogenous signal of the model's reasoning intensity. Using Sparse Autoencoders (SAEs) as a diagnostic probe, we observe that LLMs' internal reasoning is marked by a sharp increase in reasoning feature activations concentrated i...

---

### 31. Revisiting Lexicon Evaluation in Unsupervised Word Discovery

**Authors:** Simon Malan, Danel Slabbert, Herman Kamper

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06183v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06183v1)

**Summary:** Building a lexicon from discovered word-like units is a central goal in zero-resource speech processing. But do our evaluations provide a trustworthy indication of lexicon quality? A common metric, normalized edit distance, averages the phoneme edit distances between discovered units in each cluster. We show that this metric has an inherent bias toward the quality of large clusters, inhibiting fair evaluation. Moreover, it ignores how well true classes are distributed across clusters. Based on e...

---

### 32. Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning

**Authors:** Jiahao Zeng, Ming Tang, Ningning Ding

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06178v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06178v1)

**Summary:** Large language models (LLMs) present a trade-off between performance and cost, where more powerful models incur greater expense. LLM routing aims to mitigate expenses while maintaining performance by sending queries to the most suitable model. However, existing methods cannot perform well for different user cost-performance preferences. To address this gap, we introduce a novel perceptive LLM routing paradigm for personalized and user-centric cost-performance optimization, which efficiently lear...

---

### 33. Ouvia: A User-centered Framework for Measuring Usability of Speech Translation in Real-World Communication Scenarios

**Authors:** Giuseppe Attanasio, Beatrice Savoldi, Daniel Chechelnitsky, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06177v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06177v1)

**Summary:** Speech translation (ST) is increasingly adopted in user applications, yet its evaluation largely focuses on decontextualized testbeds and holistic quality, rather than end users' communication needs. We introduce Ouvia, an evaluation framework for measuring user-perceived usability of speech translation outputs in real-world settings. Ouvia focuses on one-to-one communication: an English speaker needs to convey a request to a Portuguese speaker, and the message is automatically translated. Throu...

---

### 34. ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity

**Authors:** Prathamjyot Singh, Ashima Sood, Sahil Sharma, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06168v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06168v1)

**Summary:** We present ProSarc, an audio-only framework that detects sarcasm by modelling temporal prosodic incongruity, that is, the mismatch between local prosodic dynamics and the utterance-level emotional baseline. Dual encoding paths, a Global Emotion Encoder and a Temporal Prosody Encoder (BiLSTM + multi-head attention), feed a Prosodic Incongruity Analyzer that produces a scalar incongruity score for classification. Monte Carlo dropout provides uncertainty estimates, and an attention-based mechanism ...

---

### 35. Where does Absolute Position come from in decoder-only Transformers?

**Authors:** Valeria Ruscio, Umberto Nanni, Fabrizio Silvestri

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06160v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06160v1)

**Summary:** RoPE-trained transformers distinguish absolute position in their attention patterns, even though RoPE encodes only relative offsets in the inner product. We trace this leakage to two architectural components, The causal mask is responsible for the first: its per-query softmax denominator depends on the absolute query position by construction. The residual stream supplies the second. Under causal attention the activation at position $0$ attends only to itself and runs as a closed dynamical system...

---

### 36. Harnessing Structural Context for Entity Alignment Foundation Models

**Authors:** Xingyu Chen, Yuanning Cui, Zequn Sun, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06109v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06109v1)

**Summary:** Entity alignment (EA) aims to identify equivalent entities across heterogeneous knowledge graphs (KGs) and is a key component of knowledge fusion and cross-KG reasoning. The recent EA foundation model demonstrates that alignment knowledge, once pretrained, can be directly applied to diverse previously unseen KG pairs. However, it still underuses structural context in two places: cross-KG interaction is weak during encoding, and final candidate ranking still relies too heavily on coarse similarit...

---

### 37. IR3DE: A Linear Router for Large Language Models

**Authors:** Eros Fanì, Oğuzhan Ersoy

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06098v1)

**Summary:** Foundational Large Language Models (LLMs) demonstrate proficiency on a wide range of general tasks, and achieve remarkable results on various specialized tasks via domain-expert LLMs. With the ever-growing list of available LLMs, inference routers are being proposed to select the most appropriate LLM for each prompt. However, existing routing methods either optimize cost across weak-to-strong generalist LLMs or require substantial training to support domain-expertise routing. In this paper, we p...

---

### 38. OrderGrad: Optimizing Beyond the Mean with Order-Statistic Policy Gradient Estimation

**Authors:** Paavo Parmas, Yongmin Kim, Kohsei Matsutani, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06096v1)

**Summary:** Policy-gradient methods usually optimize expected return, but many real world applications care about distributional properties of returns: tail risk, outlier robustness, or best-of-K discovery. We introduce OrderGrad, a family of likelihood-ratio and reparameterization gradient estimators for order-statistic objectives. OrderGrad optimizes finite-sample L-statistics, i.e., weighted averages of sorted rewards or costs, recovering objectives such as VaR, CVaR, trimmed means, medians, and top-m/be...

---

### 39. CHALIS: A Challenge Dataset for Language Identification in Difficult Scenarios

**Authors:** Michal Tichý, Jindřich Libovický

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06088v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06088v1)

**Summary:** We present CHALIS (Challenging Language Identification Samples), a new benchmark dataset explicitly designed to address difficult cases in language identification: cousin languages and orthographic noise. Our dataset has two parts: First, we collected sentences shared across mutually intelligible language pairs (Czech/Slovak, Spanish/Catalan, Portuguese/Galician, Danish/Norwegian). The second part tests for orthography noise: we transliterate text across multiple scripts, remove diacritics, simu...

---

### 40. LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents

**Authors:** Aofan Yu, Chenyu Zhou, Tianyi Xu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06087v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06087v1)

**Summary:** Agent systems increasingly use textual skills to encode reusable task procedures, but injecting these skills into the prompt at every step incurs substantial context overhead and exposes skill content as plaintext. We present LatentSkill, a framework that converts textual skills into plug-and-play LoRA adapters through a pretrained hypernetwork. LatentSkill stores skill knowledge in weight space rather than context space, removing per-step skill tokens while preserving modular loading, scaling, ...

---

### 41. On Advantage Estimates for Max@K Policy Gradients

**Authors:** Shota Takashiro, Soichiro Nishimori, Paavo Parmas, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06080v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06080v1)

**Summary:** Reinforcement learning with verifiable rewards is widely used for post-training reasoning models, but sparse outcome rewards make exploration difficult. A complementary approach is to optimize inference-time objectives such as pass@K and max@K directly, yet existing policy-gradient estimators for these objectives use different signals, baselines, and normalizations, making their relationships unclear. We study this issue through baseline design and advantage centering. Starting from the advantag...

---

### 42. SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization

**Authors:** Qi Zhang, Zhaopeng Feng, Xiaonan Shi, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06079v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06079v1)

**Summary:** Agent skills, which consist of reusable strategies that guide agent reasoning and action, have shown strong potential for improving model capability at inference time. However, current skill construction methods treat the problem as one-shot extraction, overlooking a fundamental tension: a skill tailored to the specific task fails to transfer, while the abstracted skill often provides insufficient guidance. We attribute this fragility to the absence of explicit mechanisms for skill specification...

---

### 43. Multi-task Learning is Not Enough: Representational Entanglement in Dual-output Second Language Speech Recognition

**Authors:** Seung Hwan Cho, Young-Min Kim

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06065v1)

**Summary:** Second-language (L2) speech recognition often requires transcriptions of pronunciations and intended meanings. Multi-task learning (MTL) is a natural approach because it assumes that shared representations benefit both outputs. However, this paper shows that this assumption does not hold across Korean and English. MTL improves meaning but degrades surface transcription, especially in English, where the degradation scales with surface-meaning divergence measured by Levenshtein edit distance.Encod...

---

### 44. MDP-GRPO: Stabilized Group Relative Policy Optimization for Multi-Constraint Instruction Following

**Authors:** Mohammad Mahdi Salmani-Zarchi, Zahra Rahimi, Heshaam Faili, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06058v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06058v1)

**Summary:** Reinforcement learning with verifiable rewards is ideal for multi-constraint instruction following, yet standard group-relative policy optimization (GRPO) becomes unstable under discrete, low-dispersion rewards, where within-group reward distributions are frequently homogeneous. We identify and formalize three pathologies of z-score group normalization in this regime: low-variance amplification, mean-centering blindness, and zero-variance collapse. To address them, we propose MDP-GRPO, which sta...

---

### 45. Automatic Labelling of Speech Translation Errors

**Authors:** Dominik Macháček, Maike Züfle, Ondrej Klejch

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06047v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06047v1)

**Summary:** Errors in speech translations reduce trustworthiness of Speech Translation (ST) systems and can have serious consequences. Yet currently there is no established methodology for evaluating confidence and quality estimation of speech translations. To initiate progress in this direction, we propose Speech Translation Error Labelling (STEL). We create an annotation protocol, a small authentic end-to-end evaluation dataset, and we analyse how existing text-only and speech-processing systems perform t...

---

### 46. IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval

**Authors:** Xiaoman Wang, Yaoze Zhang, Wenzhuo Fan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06044v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06044v1)

**Summary:** Retrieval-Augmented Generation (RAG) has shown strong effectiveness in grounding Large Language Models (LLMs) with external knowledge. However, existing RAG and Graph RAG frameworks largely treat knowledge as static or associate time with coarse-grained timestamps or metadata, failing to capture rich temporal structures such as duration, overlap, and containment. We propose IA-RAG, a hierarchical temporal RAG framework that models knowledge as time intervals and performs retrieval under formal t...

---

### 47. English-to-Prakrit Machine Translation via Multilingual Transfer Learning

**Authors:** Om Choksi, Smit Kareliya, Shrikant Malviya, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06038v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06038v1)

**Summary:** We study English-to-Prakrit machine translation in a low-resource setting where the target language is unsupported by IndicTrans2. We adapt the multilingual model by mapping Prakrit to the Hindi language tag (hin_Deva) without modifying the tokenizer, vocabulary, or architecture. Using a 1,474-pair Maharashtri Prakrit parallel corpus and evaluation on a 20-sample Ardhamagadhi test set, we report corpus BLEU improvements over an untuned baseline. The results indicate that script-compatible langua...

---

### 48. NAVIRA: Decoupled Stochastic Remasking for Masked Diffusion Language Models

**Authors:** Andrey Fomenko, Maksim Kryzhanovskiy, Svetlana Glazyrina, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06031v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06031v1)

**Summary:** Masked diffusion language models generate text by iteratively unmasking many tokens in parallel, but this speed comes with a correction problem: tokens generated in the same step are predicted from marginal distributions, and early local dependency errors can later contaminate the context. PRISM addresses this by learning token-level quality scores and remasking unreliable tokens, but its inference rule is coupled: the same forward pass both detects low-quality tokens and computes logits for the...

---

### 49. RedditPersona: A Modular Framework for Community-Conditioned LLM Adaptation from Reddit

**Authors:** Amirhossein Ghaffari, Ali Goodarzi, Huong Nguyen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06027v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06027v1)

**Summary:** Community-conditioned language model adaptation requires choices about data collection, community definition, and evaluation that are currently made independently in each study, making it hard to compare assumptions or reuse artifacts. We present RedditPersona, a modular framework that standardizes these choices: it collects Reddit posts and comments, profiles active users, partitions them under five grouping strategies (subreddit-based, graph-structural, semantic, hybrid, and interaction-based)...

---

### 50. EGTR-Review: Efficient Evidence-Grounded Scientific Peer Review Generation via Multi-Agent Teacher Distillation

**Authors:** Xinpeng Qiu, Wang Yihu, Zhifeng Liu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06025v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06025v1)

**Summary:** Scientific peer review generation has attracted increasing attention for reducing reviewing burdens and providing timely feedback. However, existing Large Language Model (LLM)-based methods often produce generic comments with insufficient evidence support and weak source traceability, while complex multi-agent systems incur high inference costs. To address these challenges, we propose EGTR-Review, an Evidence-Grounded and Traceable Review Generation framework via Multi-Agent Teacher Distillation...

---

## cs.CV

**50 papers**

### 1. PAR3D: A Unified 3D-MLLM with Part-Aware Representation for Scene Understanding

**Authors:** Shaohui Dai, Yansong Qu, You Shen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06485v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06485v1)

**Summary:** Recent advances in 3D multimodal large language models (3D-MLLMs) have enabled unified solutions for 3D scene understanding tasks, including visual question answering, captioning, and referring segmentation. However, existing 3D-MLLMs remain largely object-centric, limiting their ability to model fine-grained part structures that are essential for embodied interaction with 3D environments. In this work, we present PAR3D, a unified part-aware 3D-MLLM framework that enables models to understand, r...

---

### 2. Complexity-Balanced Diffusion Splitting

**Authors:** Noam Issachar, Dani Lischinski, Raanan Fattal

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06477v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06477v1)

**Summary:** Standard continuous-time generative models rely on monolithic architectures that must navigate vastly different signal regimes, from isotropic noise to intricate data distributions. While scaling model capacity improves performance, deploying a massive network uniformly across the entire generative timeline is inherently inefficient. In this work, we propose Complexity-Balanced Splitting (CBS), a principled framework for temporal capacity allocation that distributes the generative workload acros...

---

### 3. Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators

**Authors:** Chenming Zhu, Jingli Lin, Yilin Long, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06476v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06476v1)

**Summary:** While Vision-Language Models (VLMs) have shown strong visual reasoning capabilities, their spatial reasoning abilities remain largely constrained to the observed images and text-oriented chain-of-thought. They often struggle to infer unobserved layouts, maintain cross-view consistency, and reason from alternative viewpoints when only limited egocentric observations are available. In this work, we study this problem as thinking with imagination, where a VLM actively acquires imagined visual evide...

---

### 4. In-Context Multiple Instance Learning

**Authors:** Alexander Möllers, Marvin Sextro, Julius Hense, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06458v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06458v1)

**Summary:** Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to satellite imagery. Nevertheless, existing algorithms struggle in the low-label regime that characterizes many real-world applications. Flexible models overfit and rigid ones fail to adapt to the task at hand. We show that pretraining an in-context learner with a Perceiver-style architecture on synt...

---

### 5. A Vision-language Framework for Comparative Reasoning in Radiology

**Authors:** Tengfei Zhang, Ziheng Zhao, Lisong Dai, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06407v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06407v1)

**Summary:** Medical imaging artificial intelligence has achieved strong performance in isolated image interpretation, but remains poorly aligned with radiological practice, where diagnosis and follow-up rely on comparison across prior studies and analogous reference cases. Here we formulate radiological comparison as an entity-aware cross-image reasoning problem and introduce a framework that supports both reference-case retrieval and temporal comparative interpretation. We construct MedReCo-DB, a large-sca...

---

### 6. HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes

**Authors:** Wenbo Li, Xiaoliang Ju, Zipeng Qin, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06390v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06390v1)

**Summary:** Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing methods often rely on hand-crafted rules or focus on isolated sub-tasks (e.g., floorplan synthesis or single-room furnishing), producing whole-home scenes that lack global coherence, realism, and simulation readiness. To mitigate these limitations, we propose a unified hierarchical framework that decom...

---

### 7. EasyLens: A Training-Free Plug-and-Play Subtle-Lesion Representation Amplifier for Medical Vision-Language Models

**Authors:** Qiwei Zeng, Hao Wang, Jinghao Lin, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06379v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06379v1)

**Summary:** Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation, including lesion detection and report generation. However, their practical utility remains limited by insufficient sensitivity to subtle lesions, whose visual evidence is often sparse, low-contrast, and embedded within complex anatomical context. As local visual tokens are aggregated, these weak lesion cues can become underrepresented in global image representations, making them difficult for...

---

### 8. Visual Commonsense Driven Knowledge Refinements for Scene Graph Generation

**Authors:** Maëlic Neau, Salim Baloch, Jakob Suchan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06369v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06369v1)

**Summary:** Learning-driven Scene Graph Generation (SGG) models excel on frequent relation types but degrade sharply under annotation sparsity, failing to capture reliable visual commonsense knowledge. We propose a model-agnostic, semantically-guided knowledge refinement framework that systematically mines commonsense-grounded constraints from training data - capturing spatial, functional, and qualitative relational regularities - and uses general declarative commonsense reasoning to correct and refine rank...

---

### 9. GMBFormer: An NDVI-Guided Global Memory Bank Transformer for Urban Green-Space Extraction from Ultra-High-Resolution Imagery

**Authors:** Hao Lei, Xi Cheng, Chenlu Shu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06363v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06363v1)

**Summary:** Urban green-space extraction from ultra-high-resolution (UHR) imagery is commonly performed patch by patch, which limits semantic reuse among spatially separated but visually similar vegetation patterns. Directly injecting the Normalized Difference Vegetation Index (NDVI) into red-green-blue (RGB) backbones can also blur the roles of visual appearance learning and physical vegetation confidence. We propose GMBFormer, a SegFormer-based framework that replaces adjacency-driven feature propagation ...

---

### 10. Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them

**Authors:** Woojung Han, Seil Kang, Youngjun Jun, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06361v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06361v1)

**Summary:** Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generation often exhibits better physical consistency than a 50-step output from the same model. Through spectral analysis, we trace this to phase erosion during denoising; the phase degrades significantly (dropping by $\approx 18\%$ from step 2 to step 50), whereas the magnitude remains relatively stable....

---

### 11. Comparison of Deep Learning Frameworks For Rice Disease Mapping From UAV Multispectral Imaging

**Authors:** Yadav Raj Ghimire, Jagrati Talreja, Tewodros Syum Gebre, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06359v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06359v1)

**Summary:** In this study, UAV multispectral imagery is used to segment the severity of bacterial leaf blight (BLB) in rice using convolutional neural networks (CNNs) and transformer-based models. The evaluated architectures include U-Net with a ResNet- 101 encoder, U-Net++ with EfficientNet-B3 and EfficientNetB7, DeepLabV3+, and SegFormer, all trained under a common pipeline with three input configurations (multispectral only, multispectral+NDVI, and multispectral+NDRE). Experiments are conducted using the...

---

### 12. StoryVideoQA: Scaling Deep Video Understanding with a Large-Scale, Multi-Genre and Auto-Generated Dataset

**Authors:** Zhengqian Wu, Zhixian Liu, Aodong Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06338v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06338v1)

**Summary:** Video question answering (VideoQA) aims to answer questions about given videos. While existing approaches excel on factoid VideoQA, they struggle with deep video understanding (DVU), which requires the comprehension of complex storylines. This challenge arises from the inherent long-range video content, multi-faceted question types, and instance-level story elements, all of which constrain the scale and diversity of manually constructed DVU datasets.These difficulties constrain the scale and div...

---

### 13. Efficient Mean Curvature Computation on High-Dimensional Data Manifolds

**Authors:** Alexandre L. M. Levada

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06329v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06329v1)

**Summary:** Estimating local mean curvature at each point of a high-dimensional dataset is a key ingredient of geometry-aware machine learning algorithms, such as the Mean Curvature Boundary Points (MCBP) method. The naive implementation of this computation, based on a local shape operator approximated from k-nearest neighbor patches, involves an explicit construction of a matrix $H$ whose trace form yields an $O(m^4)$ cost per point, rendering the approach intractable for datasets with more than a few doze...

---

### 14. RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling

**Authors:** Chensheng Dai, Shengjun Zhang, Yifan Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06309v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06309v1)

**Summary:** Video generation models based on Diffusion Transformers (DiTs) have achieved remarkable performance in video synthesis, yet they suffer from high inference latency and computational costs due to the quadratic complexity of 3D attention. Existing acceleration methods primarily reduce computational complexity within each individual denoising steps through techniques such as sparse attention and KV-caching. However, they rigidly adhere to the inherent constraint of the standard diffusion pipeline: ...

---

### 15. Towards One-to-Many Temporal Grounding

**Authors:** Qi Xu, Yue Tan, Shihao Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06294v1)

**Summary:** Temporal Grounding (TG) aims to localize video segments corresponding to a textual query. Prior research predominantly focuses on single-segment retrieval. Real-world scenarios, however, often require localizing multiple disjoint segments for a single query -- a setting we term One-to-Many Temporal Grounding (OMTG). Previous state-of-the-art MLLMs, optimized for one-to-one settings, struggle in this context, often yielding near-zero scores due to a lack of event cardinality perception. To bridge...

---

### 16. Synthetic Data Generation and Vision-based Wrinkle and Keypoint Detection for Bimanual Cloth Manipulation

**Authors:** Ariel Herrera, Xueyang Kang, Atal Anil Kumar

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06292v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06292v1)

**Summary:** Robotic manipulation of textiles remains challenging because continuous deformation and self-occlusions hinder the robust visual perception required to estimate the cloth's state. To address the lack of annotated real-world data, we developed a Blender-based synthetic pipeline exporting auto-annotated keypoints, and combined manually labeled renders with real-world data to train a wrinkle detector. We present a perception framework integrating a CNN for permutation-invariant keypoint detection a...

---

### 17. Geodesic Flow Matching on a Riemannian Degradation Manifold for Blind Image Restoration

**Authors:** Akshay Janardan Bankar, Ankita Chatterjee, Sayan Banerjee, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06278v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06278v1)

**Summary:** Blind image restoration requires recovering clean images from observations corrupted by unknown and potentially mixed degradations. While recent deterministic flow-based methods model restoration as transport processes that map degraded images to clean ones, they typically rely on Euclidean interpolation, implicitly assuming linear degradation geometry. In this paper, we explicitly model degradations as points on a low-dimensional Riemannian manifold and formulate restoration as geodesic transpo...

---

### 18. RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning

**Authors:** Ziyang Yu, Xiang Li, Qiong Chang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06255v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06255v1)

**Summary:** Point clouds are a primary sensory representation for robotic perception, underpinning LiDAR-based autonomous driving, simultaneous localization and mapping (SLAM), and navigation. Within these pipelines, Farthest Point Sampling (FPS) is the most well-known downsampling operator, as its uniform coverage preserves the geometric structure on which downstream perception relies. However, the large time complexity of classical FPS scales poorly with the million-point-per-second rates of modern 3D sen...

---

### 19. GRAMformer: Any-Order Modality Interactions via Volumetric Multimodal Cross-Attention

**Authors:** Giordano Cicchetti, Eleonora Grassucci, Danilo Comminiello

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06249v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06249v1)

**Summary:** Transformer-based multimodal models rely on attention mechanisms to integrate information across heterogeneous modalities. Despite their success, existing multimodal attention formulations compute their scores through collections of pairwise dot-product interactions or by concatenating all the modalities into the keys, even when multiple modalities should be jointly involved. As a consequence, current approaches either incur quadratic complexity in the number of modalities or fail to explicitly ...

---

### 20. Benchmarking Open-Source Layout Detection Models for Data Snapshot Extraction from Institutional Documents

**Authors:** AJ Carl P. Dy, Aivin V. Solatorio

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06242v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06242v1)

**Summary:** Institutional documents contain substantial amounts of operational and analytical information embedded within figures and tables. Current approaches for extracting visual content from documents are largely built around generic document layout analysis, where figures and tables are treated as uniformly relevant document objects rather than semantically meaningful analytical artifacts. In this work, we introduce a benchmark dataset and evaluation framework for \textit{data snapshot extraction}, th...

---

### 21. SAM-Flow: Source-Anchored Masked Flow for Training-Free Image Editing

**Authors:** Haowang Cui, Rui Chen, Tao Luo, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06228v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06228v1)

**Summary:** Training-free image editing has recently attracted increasing attention due to its ability to modify real images using powerful pre-trained diffusion and flow-matching models without additional training. However, existing inversion-based and differential-flow-based methods usually perform global latent transport, which inevitably propagates editing effects to non-target regions and leads to background leakage. To address this problem, we propose SAM-Flow, a source-anchored masked flow framework ...

---

### 22. Symb-xMIL: Symbolic Explanations for Multiple Instance Learning in Digital Pathology

**Authors:** Yanqing Luo, Julius Hense, Niklas Prenißl, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06224v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06224v1)

**Summary:** Explanations of multiple instance learning (MIL) models are widely used for validation and discovery in digital histopathology. Existing methods primarily rely on heatmaps that highlight influential regions but do not explain how evidence from different tissue regions is combined to produce a prediction. This limits interpretability, especially when decisions depend on interactions between tissue features. We introduce Symbolic explainable MIL (Symb-xMIL), a post-hoc explanation framework that q...

---

### 23. DisasterBench: A Multimodal Benchmark for UAV-Based Disaster Response in Complex Environments

**Authors:** Tan Zhang, Quanyou Li, Lu Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06217v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06217v1)

**Summary:** When a disaster unfolds, responders must answer not only what is happening, but also why it is happening, what will happen next, and what to do now, often from noisy low-altitude UAV views and under tight on-site compute constraints. However, most existing multimodal benchmarks emphasize perception (e.g., recognition/description), cover limited disaster types, and provide insufficient support for the multi-stage reasoning required in practical emergency response. We introduce DisasterBench, a mu...

---

### 24. SC-MFJ: A Simple Haptic Quality Metric for Medical Image Segmentation

**Authors:** Souraj Adhikary, Negar Chabi, Andre Mastmeyer

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06199v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06199v1)

**Summary:** Standard segmentation metrics such as Dice and Hausdorff distance measure geometric overlap but say nothing about whether a segmented surface is suitable for haptic rendering in surgical simulation. We propose SC-MFJ (Surface-Constrained Mean Force Jerk), a simple, inexpensive metric that samples a segmented organ surface with many short virtual stylus walks and measures how jerky the resulting contact forces are. The metric is computed from existing segmentation outputs and uses roughly one min...

---

### 25. ActiveMimic: Egocentric Video Pretraining with Active Perception

**Authors:** Xingyao Lin, Guojin Zhong, Tianyi Lu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06194v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06194v1)

**Summary:** Egocentric human video offers a scalable alternative to robot data for pretraining, yet models pretrained on such video consistently underperform those pretrained on robot data. We attribute this gap to a missing signal, the active perception behavior in egocentric videos, where humans continuously reposition their viewpoint during manipulation, inducing camera motion that standard pipelines treat as noise. To address this, we present ActiveMimic, a pretraining framework that recovers synchroniz...

---

### 26. Adversarial Attacks Already Tell the Answer: Directional Bias-Guided Test-time Defense for Vision-Language Models

**Authors:** Liangsheng Liu, Si Chen, Jiamin Wu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06186v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06186v1)

**Summary:** Vision-Language Models (VLMs), such as CLIP, have shown strong zero-shot generalization but remain highly vulnerable to adversarial perturbations, posing serious risks in real-world applications. Test-time defenses for VLMs have recently emerged as a promising and efficient approach to defend against adversarial attacks without requiring costly large-scale retraining. In this work, we uncover a surprising phenomenon: under diverse input transformations, adversarial images in CLIP's feature space...

---

### 27. RQUL-UIE: Revitalizing Quality-Unstable Labels for Underwater Image Enhancement via In-Dataset Self-Supervision

**Authors:** Haochen Hu, Yanrui Bin, Chih-yung Wen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06176v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06176v1)

**Summary:** Underwater Image Enhancement (UIE) is essential for mitigating degradations caused by water medium. Although learning-based methods have advanced significantly, most rely on paired datasets with unstable label quality, which bottlenecks model performance. This paper proposes a diffusion-based, in-dataset self-supervised learning strategy designed to exploit the quality distribution of training labels. Specifically, we evaluate label quality via semantic perception embeddings from a pre-trained d...

---

### 28. Adaptive Tokenisation Via Temporal Redundancy Masking And Latent Inpainting

**Authors:** Kevin Dave, Sai Aditya Patkuri, Chhaya Kumar Das, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06158v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06158v1)

**Summary:** Adaptive video tokenisation seeks to dynamically allocate token budgets based on the underlying visual complexity of a sequence. Current continuous-regime approaches achieve this via iterative binarised searches or trained neural regressors, while discrete methods often require a full-rate decoder pass to estimate information content. We demonstrate that such computational overheads are not strictly necessary. We show that the latent space of a frozen continuous video tokeniser inherently encode...

---

### 29. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

**Authors:** Qize Yu, Jiadi You, Yuran Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06155v1)

**Summary:** Vision-Language-Action (VLA) models leverage the rich world knowledge of pretrained vision-language models (VLMs) to enable instruction-following robotic manipulation. However, the structural mismatch between VLM semantic spaces and embodied control policies often hinders the learning of precise perception--action mappings. To address this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces structured affordance forecasting as a task-oriented intermediate representa...

---

### 30. Computation-Aware Event-to-Frame Reconstruction via Selective Attention

**Authors:** Jingqian Wu, Yunbo Jia, Edmund Y. Lam

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06142v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06142v1)

**Summary:** Event-to-frame (E2F) reconstruction bridges asynchronous event streams with frame-based vision pipelines, but existing methods often face a trade-off between reconstruction quality and computational efficiency. In this work, we propose an efficient E2F framework that emphasizes causal temporal modeling and computation-aware design. The architecture adopts a recurrent encoder-decoder to incrementally aggregate event information with compact hidden states. To improve robustness under fast motion a...

---

### 31. Diff-CA: Separating Common and Salient Factors with Diffusion Models

**Authors:** Michaël Soumm, Alexandre Fournier Montgieux, Yunlong He, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06120v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06120v1)

**Summary:** Contrastive Analysis aims to separate factors that are common between two data distributions from those that are salient to only one of them. Existing contrastive methods are based on generative models (e.g., VAEs or GANs) that often suffer from limited reconstruction and image quality, which hampers effective latent factor separation and limits their applicability to high-fidelity image generation and edition. We propose a novel conditioning framework for diffusion models that enables contrasti...

---

### 32. Where, What, Why, and Importance: Structured Defect Grounding for Text-to-Image Feedback

**Authors:** Huaisong Zhang, Hao Yu, Yuxuan Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06113v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06113v1)

**Summary:** Despite generating increasingly photorealistic images, text-to-image (T2I) models still exhibit localized, subtle, and structurally complex failures. Diagnosing these failures requires instance-level feedback that answers where a defect occurs, what type it is, why it is defective, and its importance to overall image quality. While recent dense-feedback methods move beyond scalar supervision, their heatmap-centric representations still formulate diagnosis as pixel-field regression, making it dif...

---

### 33. MS-DKC: A Dataset Knowledge Card Framework for Designing and Adapting Medical Image Segmentation Models

**Authors:** Tariq M. Khan, Syed Saud Naqvi, Thantrira Porntaveetus, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06103v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06103v1)

**Summary:** Medical image segmentation is often framed as a search for stronger architectures, but this can obscure a more fundamental question: what does the dataset require from the model? In medical imaging, this requirement is shaped by foreground occupancy, morphology, boundary ambiguity, topology sensitivity, annotation quality, acquisition variation, and operating point.   This paper introduces the Medical Segmentation Dataset Knowledge Card (MS-DKC), a framework for making these factors explicit. MS...

---

### 34. HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning

**Authors:** Moshiur Farazi, Sameera Ramasinghe, Mahbub Ahmed Turza, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06100v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06100v1)

**Summary:** Vision-Language Models (VLMs) struggle with compositional reasoning that requires understanding inter-object relationships. A natural remedy is to inject explicit scene graph triplets $\langle s, p, o \rangle$ from an off-the-shelf scene graph generator (SGG), but we show this backfires: discrete text labels collide with the continuous visual modality, degrading GQA accuracy from 60.38\% to 58.86\%. We propose \textbf{HyperVis}, which bypasses the SGG semantic bottleneck entirely. From $N$ class...

---

### 35. Knowledge Distillation for Visual Autoregressive Models

**Authors:** Elia Peruzzo, Aritra Bhowmik, Guillaume Sautiere, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06078v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06078v1)

**Summary:** Autoregressive (AR) image generation models are highly expressive but computationally intensive, motivating effective model compression. Knowledge distillation (KD) is a natural approach for model compression and has been widely studied in language modeling, yet its behavior in visual AR generation remains underexplored. In this work, we present the first systematic study of distillation strategies for AR image models. Our analysis shows that while standard distillation can yield meaningful gain...

---

### 36. Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation

**Authors:** Haocheng Luo, Jiahui Liu, Ruicheng Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06076v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06076v1)

**Summary:** While vision-language models excel at general multimodal understanding, they still struggle with visual spatial planning. We attribute this to a perception-reasoning modality gap: visual planning requires models to infer latent state structures from pixels and then reason over the recovered structure to produce valid actions, whereas symbolic planning directly leverages explicit objects and constraints. This creates dual bottlenecks in visual state recovery and multi-step planning. To address th...

---

### 37. VZCrash: A Large-Scale IMU Dataset of Ego-Vehicle Crashes

**Authors:** Tommaso Bianconcini, Henrique Piñeiro Monteagudo, Aurel Pjetri, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06074v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06074v1)

**Summary:** We introduce VZCrash, the largest publicly available dataset of real-world vehicle collision data featuring Inertial Measurement Unit (IMU) telemetry. The dataset contains more than 31,000 validated crashes and 158,000 negative samples, including hard cases and distractors. Each sample includes acceleration and angular velocity at 100 Hz, and GPS speed at 1 Hz. Events in VZCrash were captured by devices installed on a fleet of 73,010 commercial vehicles of different sizes driving in the United S...

---

### 38. FontFusion: Enhancing Generative Text in Diffusion Models with Typographic Conditioning

**Authors:** Marian Lupascu, Nipun Jindal, Ionut Mironica, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06066v1)

**Summary:** Typography generation in diffusion models faces a persistent trade-off: enabling precise font control typically degrades text legibility, while maintaining readability often sacrifices typographic fidelity. We present FontFusion, a plug-and-play conditioning framework for Diffusion Transformer (DiT) architectures that resolves this dilemma through three core innovations: (1) a hierarchical token representation establishing explicit text-font relationships at multiple granularities, (2) position-...

---

### 39. ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE

**Authors:** Mishan Aliev, Eva Neudachina, Ilya Bykov, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06060v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06060v1)

**Summary:** Modern diffusion models generate high-quality images and videos, but their iterative denoising process makes inference expensive. Feature caching accelerates sampling by reusing or predicting intermediate activations across neighboring denoising steps, exploiting the redundancy of computations along the reverse trajectory. In this work, we focus on the caching schedule: selecting which denoising steps should be fully recomputed. Existing schedules are either fixed (e.g. uniform) or chosen adapti...

---

### 40. LLM-Conditioned Synthesis of Pathological Gaits via Structured Gait-Language Representations

**Authors:** Mritula Chandrasekaran, Sanket Kachole, Jarik Francik, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06048v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06048v1)

**Summary:** Pathological gait datasets remain scarce due to privacy, recruitment, cost, and movement variability. Our work presents a multimodal LLM-guided framework for pathology-aware 3D gait data synthesis from structured textual descriptions. The proposed method generates fixed-length synthetic skeleton-based gait sequences for pathological gait classification tasks. The framework combines motion tokenisation, pathology-aware language conditioning, LLM-based semantic augmentation, and language-to-gait g...

---

### 41. LoomVideo: Unifying Multimodal Inputs into Video Generation and Editing

**Authors:** Jianzong Wu, Hao Lian, Jiongfan Yang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06042v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06042v1)

**Summary:** Developing unified video generation and editing models capable of interpreting interleaved multimodal inputs is a promising yet challenging frontier field. Existing unified frameworks predominantly rely on massive models (typically 13B parameters or more) and incorporate source video conditions for editing by concatenating sequence tokens. This concatenation inevitably doubles the sequence length, quadrupling the computational complexity of the self-attention mechanism and introducing prohibitiv...

---

### 42. Texture-preserving implicit neural representation for Cone beam CT truncated reconstruction

**Authors:** Genyuan Zhang, Junyao Wang, Haoran Lan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06039v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06039v1)

**Summary:** Cone-beam computed tomography (CBCT) frequently suffers from data truncation, which introduces severe artifacts and limits the effective field of view (FOV). Existing deep learning methods for truncated cone-beam computed tomography (CBCT) reconstruction suffer from serious limitations, including a strict reliance on supervised ground truth and a failure to account for continuous 3D spatial truncation variations. To address these challenges, we introduce a self-supervised 3D reconstruction frame...

---

### 43. ReSAGE-PAR: Representational Similarity Assessment for Generative Expansion in Pedestrian Attribute Recognition

**Authors:** Pablo Ayuso-Albizu, Pablo Carballeira, Juan C. SanMiguel, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06020v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06020v1)

**Summary:** To address the limited diversity and data scarcity in Pedestrian Attribute Recognition (PAR), we explore image synthesis using diffusion models guided by attribute-based prompts. While this enables the controlled generation of pedestrian images, it faces two critical challenges: (i) the domain gap between high-quality pre-training data and low-resolution, non-standard surveillance crops, and (ii) the need for reliable attribute verification to prevent generative hallucinations. In this paper, we...

---

### 44. Global-Local Monte Carlo Tree Search in Vision-Language Models for Text-to-3D Indoor Scene Generation

**Authors:** Mengshi Qi, Wei Deng, Xianlin Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06002v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06002v1)

**Summary:** Large Vision-Language Models have achieved significant reasoning performance in various tasks.However, there are few studies on text-to-3D indoor scene generation with LVLMs. The main challenge is that prevailing LVLM-based methods employ chain-of-thought sequential decision mechanisms that cannot revise earlier decisions, causing error propagation.In this paper, we consider the task as a planning problem constrained by spatial and layout commonsense.To solve this problem, we model it as a tree ...

---

### 45. ATT-CR: Adaptive Triangular Transformer for Cloud Removal

**Authors:** Yang Wu, Ye Deng, Pengna Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05999v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05999v1)

**Summary:** Cloud removal aims to accurately reconstruct the ground objects obscured by clouds in remote sensing images. Existing Transformer-based methods utilizing self-attention have shown impressive results by effectively modeling long-range dependencies in cloudy images. However, they suffer from the following issues: 1) the high computational complexity of self-attention limits scalability; 2) treating both cloudy and clean pixels as valid within the attention computation brings disturbances in subseq...

---

### 46. Deep Learning-based 3D Oral Cavity Reconstruction Using 2D Intraoral Images

**Authors:** Jihun Cho, Soo-Yeon Jeong, Eun-Jeong Bae, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05998v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05998v1)

**Summary:** Oral 3D modelling is one of the most essential stages in dentistry, and many different approaches, such as impression taking and intraoral scanning, are commonly used for this phase, each with notable limitations. Impression taking, which involves placing alginate or silicone material in a tray and inserting it into the patient's oral cavity to form a negative mold, suffers from significant patient discomfort, material deformation errors, and difficulties in storage and transportation. Intraoral...

---

### 47. Multimodal Sexism Identification and Characterization using Large Language Models and Gradient Boosting

**Authors:** Kyriakos Chaviaras, Maria Lymperaiou, Athanasios Voulodimos

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05997v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05997v1)

**Summary:** We present the AILS-NTUA submission to the EXIST 2026 Lab at CLEF, addressing multimodal sexism identification and characterization in memes (Task 2) and short-form videos (Task 3). Our system follows a feature-engineered late-fusion pipeline built around gradient-boosted regression models and hierarchical post-processing. For memes, we combine visual, textual, demographic, biometric, and LLM-derived semantic indicators designed to capture high-level cues such as stereotyping, objectification, i...

---

### 48. Video-Rate Streaming Stylization on a Vision-Aware MLLM-Conditioned Edit Diffusion: Asymmetric Batched Inference on a Distilled UNet + MLLM Text Encoder

**Authors:** Yoshiyuki Ootani

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05981v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05981v1)

**Summary:** Aggressive distillation of the diffusion U-Net inverts the per-frame bottleneck of real-time text-to-image pipelines: once the denoiser is a 4-step or 1-step distilled student, the text encoder becomes the critical path. This inversion is most acute in vision-aware edit diffusion, where the encoder is a multimodal large language model (MLLM). We study the case of a 0.39B distilled edit U-Net paired with a 2.13B MLLM text encoder (Qwen3-VL) and present a streaming pipeline targeted at this regime...

---

### 49. T-FunS3D: Task-Driven Hierarchical Open-Vocabulary 3D Functionality Segmentation

**Authors:** Jingkun Feng, Reza Sabzevari

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05975v1)

**Summary:** Open-vocabulary 3D functionality segmentation enables robots to localize functional object components in 3D scenes. It is a challenging task that requires spatial understanding and task interpretation. Current open-vocabulary 3D segmentation methods primarily focus on object-level recognition, while scene-wide part segmentation methods attempt to segment the entire scene exhaustively, making them highly resource-intensive and time consuming. Balancing segmentation performance in terms of granula...

---

### 50. Faithful, Enriched, and Precise: Benchmarking Natural-Science Illustration Generation by T2I models

**Authors:** Yifan Chang, Jiaxin Ai, Jianwen Sun, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05949v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05949v1)

**Summary:** Scientific illustrations are essential tools for communicating research findings, especially in natural science, where they visualize complex concepts and processes. As Text-to-Image (T2I) models become increasingly capable, researchers have started to use them for scientific illustration generation. However, existing benchmarks often assess outputs at a holistic level, overlooking fine-grained elements, while scientific reasoning ability and output conciseness remain under-quantified. We introd...

---

## cs.LG

**50 papers**

### 1. TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning

**Authors:** Marius Dragoi, Ioana Pintilie, Alexandra Dragomir, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06494v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06494v1)

**Summary:** Parameter-efficient finetuning methods based on spectral decomposition have enabled progress in Continual Learning. In this paper we introduce TailLoR, which utilizes the singular bases U and V of the pre-trained weights as a fixed reference frame to learn a low-rank update applied to the singular value matrix. A soft spectral penalty discourages updates aligned with dominant singular directions, reducing interference while routing fine-grained adaptation into the highly flexible, long-tail spec...

---

### 2. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

**Authors:** Lizhi Yang, Junheng Li, Nehar Poddar, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06493v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06493v1)

**Summary:** For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface that is intuitive, general, modular, and expressive enough for diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid...

---

### 3. Regret Minimization with Adaptive Opponents in Repeated Games

**Authors:** Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06486v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06486v1)

**Summary:** In this paper, we study regret minimization in repeated games with \emph{adaptive} opponents who can respond based on histories of play. The standard metric of \emph{external regret} in online learning is known to fail to capture such adaptivity. To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the \emph{realized} and the \emph{best-in-hindsight} accumulated utility when all playe...

---

### 4. Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection

**Authors:** Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06481v1)

**Summary:** As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for study...

---

### 5. DNQ: Deep Nash Q-Network for Partially Observable n-Player Games

**Authors:** Qintong Xie, Edward Koh, Xavier Cadet, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06480v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06480v1)

**Summary:** Many real-world competitive systems require multiple decision-makers to act simultaneously under shared constraints, limited information, and repeated interaction, as in auctions, resource allocation, and security competition. We study multi-turn simultaneous bidding as a controlled testbed for such problems and propose DNQ, a solver-in-the-loop equilibrium supervision framework for training bidding agents. DNQ alternates between trajectory collection, critic-based payoff estimation, equilibrium...

---

### 6. Pretraining Recurrent Networks without Recurrence

**Authors:** Akarsh Kumar, Phillip Isola

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06479v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06479v1)

**Summary:** Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supe...

---

### 7. RREDCoT: Segment-Level Reward Redistribution for Reasoning Models

**Authors:** Mykyta Ielanskyi, Kajetan Schweighofer, Lukas Aichberger, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06475v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06475v1)

**Summary:** Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modifications thereof to steer the models to produce Chain-of-Thought (CoT) traces. The final answer can only be verified, and the reward assigned, after the CoT trace is complete, making it a delayed reward problem. GRPO and its modifications correspond to Monte Carlo methods in standard RL, which are k...

---

### 8. Self-Augmenting Retrieval for Diffusion Language Models

**Authors:** Paul Jünger, Justin Lovelace, Linxi Zhao, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06474v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06474v1)

**Summary:** Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the output and discarding the unconfident ones. We show that the discarded tokens are in fact a useful lookahead signal for retrieval-augmented generation: even low-confidence tokens often surface salient entities early in the denoising trajectory, enabling retrieval of stronger evi...

---

### 9. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training

**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06470v1)

**Summary:** We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-t...

---

### 10. How abundant are good interpolators?

**Authors:** August Y. Chen, Ahmed El Alaoui

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06469v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06469v1)

**Summary:** Let $S$ be the set of unit norm linear classifiers $θ\in \mathbb{R}^d$ which correctly classify every point of a labeled dataset $(X_i,y_i)_{i=1}^n$, $X_i \in \mathbb{R}^d$, $y_i \in \{-1,+1\}$, with a possibly negative margin $κ$ fixed in advance. Under two natural data-generating distributions of the $(X,y)$ pairs -- a Gaussian mixture model and a logistic model with Gaussian features -- and in the proportional regime $n/d \to α$ with small enough $α$, we establish a large deviation principle ...

---

### 11. You Only Index Once: Cross-Layer Sparse Attention with Shared Routing

**Authors:** Yutao Sun, Yanqi Zhang, Li Dong, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06467v1)

**Summary:** Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse methods typically provide stronger acceleration but incur noticeable quality loss, while token sparse methods are usually more accurate yet deliver limited end-to-end speedup because top-k routing over...

---

### 12. Event Detection for Parameter-to-KPI Dependency Learning for AI-RAN

**Authors:** Christie Djidjev, Nicholas Kaminski

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06459v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06459v1)

**Summary:** Next-generation wireless networks are expected to rely on multiple concurrent AI-driven control functions that optimize different network objectives simultaneously, particularly in AI-integrated and open radio access network architectures such as AI Radio Access Network (AI-RAN) and Open Radio Access Network (O-RAN). When these functions interact, they can interfere with one another in ways that are difficult to detect from raw network data alone. A key missing piece for managing such interactio...

---

### 13. In-Context Multiple Instance Learning

**Authors:** Alexander Möllers, Marvin Sextro, Julius Hense, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06458v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06458v1)

**Summary:** Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to satellite imagery. Nevertheless, existing algorithms struggle in the low-label regime that characterizes many real-world applications. Flexible models overfit and rigid ones fail to adapt to the task at hand. We show that pretraining an in-context learner with a Perceiver-style architecture on synt...

---

### 14. Latent Reasoning with Normalizing Flows

**Authors:** Guancheng Tu, Xiangjun Fu, Suhao Yu, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06447v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06447v1)

**Summary:** Large language models often improve reasoning by generating explicit chain-of-thought (CoT), demonstrating the importance of intermediate computation. However, textual CoT forces this computation through a discrete, serial, and communication-oriented token stream: each reasoning step must be verbalized before the model can proceed, even when the underlying update is semantic, uncertain, or only partially formed. Latent reasoning offers a higher-bandwidth alternative by performing intermediate co...

---

### 15. Causal Atlases from Entropic Inference: Bayesian Networks beyond Optimal DAGs

**Authors:** Hazhir Aliahmadi, Irina Babayan, Greg van Anders

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06440v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06440v1)

**Summary:** Data-driven causal relationship identification is pertinent to advancing understanding of complex systems both within and beyond science. Bayesian networks offer a probabilistic method for modelling generic causal relationships via directed acyclic graphs (DAGs). However, typical techniques for constructing Bayesian networks rely on optimization, which can be ill-suited for learning causal relationships because the underlying data may admit multiple chains of causation. More data-faithful repres...

---

### 16. Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss

**Authors:** Thomas T. Zhang, Alok Shah, Yifei Zhang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06418v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06418v1)

**Summary:** Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., $L^2$ regression, cross-entropy), but deploy the network by rolling out along its own predictions. Key examples include autoregressive language modeling, flow-based generative modeling, and robot policy learning. It is well-documented that these settings induce a phenomenon we call test-time feedback (TTF): the mismatch between the training/validation loss and downstream metrics of i...

---

### 17. Unsupervised Skill Discovery for Agentic Data Analysis

**Authors:** Zhisong Qiu, Kangqi Song, Shengwei Tang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06416v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06416v1)

**Summary:** Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guid...

---

### 18. A Vision-language Framework for Comparative Reasoning in Radiology

**Authors:** Tengfei Zhang, Ziheng Zhao, Lisong Dai, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06407v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06407v1)

**Summary:** Medical imaging artificial intelligence has achieved strong performance in isolated image interpretation, but remains poorly aligned with radiological practice, where diagnosis and follow-up rely on comparison across prior studies and analogous reference cases. Here we formulate radiological comparison as an entity-aware cross-image reasoning problem and introduce a framework that supports both reference-case retrieval and temporal comparative interpretation. We construct MedReCo-DB, a large-sca...

---

### 19. The Post-GCN Decade Revisited: Curvature-Stratified Evaluation of Relational Learning

**Authors:** Shuo Wang, Xiangyu Wang, Quanxin Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06397v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06397v1)

**Summary:** Current evaluation practices in relational learning rely heavily on flat leaderboards that average performance across heterogeneous datasets, implicitly assuming a uniform underlying structure. We show that this assumption introduces systematic bias: it obscures geometry-dependent performance variations and can lead to misleading conclusions about model generalization. In this work, we identify intrinsic geometry as a key latent factor governing model effectiveness. We demonstrate that conventio...

---

### 20. Proper Scoring Rules for Right-Censored Survival Data

**Authors:** Jef Jonkers, Glenn Van Wallendael, Luc Duchateau, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06393v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06393v1)

**Summary:** Proper scoring rules provide a rigorous theoretical basis for the training and evaluation of probabilistic forecasts. However, in the presence of right censoring, the event time is only partially observed, rendering conventional scoring rules inapplicable in their standard form. We propose a framework for proper scoring of right-censored survival outcomes based on a simple idea: first, map the predictive distribution through the censoring mechanism, then apply the underlying proper score on the ...

---

### 21. Conformal Risk Sharing: Certified Cost Allocation with Participation Guarantees

**Authors:** Ieva Kazlauskaite

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06391v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06391v1)

**Summary:** Sharing the financial impact of rare adverse events across a group can soften extreme individual burdens, but any participant made worse off by the arrangement has reason to leave. A credible mechanism must therefore provide each agent with a trustworthy cap on their future obligation and should be deployed only if the aggregate harm across participants is bounded. We formalise this as the Certified Allocation Problem: from finite data and without distributional assumptions, find a redistributio...

---

### 22. Learned Response-Field Inertia Operator for HEC-RAS 2D Water-Surface Elevation Prediction

**Authors:** Edward Holmberg, Elias Ioup, Md Meftahul Ferdaus, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06385v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06385v1)

**Summary:** This article presents a cross-dataset evaluation of learned native-cell surrogate models for solver-consistent water-surface elevation (WSE) prediction in HEC-RAS 2D. To avoid raster remapping error and information-access confounding, surrogates are evaluated directly on the original nonuniform computational cells under an explicit policy that separates static project inputs, current hydraulic state, project-input forcing, calibration-derived quantities, and future solver-output targets. We intr...

---

### 23. End-to-End Subgraph Detection with GraphDETR

**Authors:** Dexiong Chen, Till Hendrik Schulz, Karsten Borgwardt

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06364v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06364v1)

**Summary:** Subgraph detection seeks to identify whether and where instances of query patterns occur within a larger graph. This problem is fundamental across scientific domains and is closely related to subgraph isomorphism, which is NP-complete, limiting combinatorial approaches to small patterns or moderately sized graphs. We introduce GraphDETR, a deep learning framework that formulates subgraph detection as a set prediction problem, analogous to DETR in object detection. GraphDETR encodes the target gr...

---

### 24. Maximising the Set-Piece Return: Optimising Football Corner Tactics with Graph Reinforcement Learning

**Authors:** Sean Groom, Michael Groom, Francisco Belo, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06353v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06353v1)

**Summary:** Machine learning is increasingly employed for the evaluation of football tactics. However, existing approaches focus on characterising historical actions or analyst-specified counterfactual scenarios. In this work, we seek to go beyond the imitation of historically observed patterns towards discovering new generalisable player configurations and strategies. To tackle this, we focus on optimising corner kick routines, and formulate a decision-making problem in which a central policy makes adjustm...

---

### 25. Function-Space Priors for Bayesian Neural ODEs with Application to Vessel Trajectory Prediction

**Authors:** Jaeyeong Lee, Wonmo Koo, Heeyoung Kim

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06351v1)

**Summary:** Vessel trajectory prediction from Automatic Identification System (AIS) data is essential for maritime situational awareness, yet it remains challenging due to irregular sampling, missing reports, and complex dynamics. Beyond accurate point forecasts, maritime applications also demand well-calibrated uncertainty estimates for reliable decision-making. Bayesian Neural Ordinary Differential Equations (ODEs) offer a principled framework for continuous-time trajectory modeling with uncertainty quant...

---

### 26. Performance Evaluation of GraphCast for Medium-Range Weather Forecasting over Brazil

**Authors:** Wolfgang R. Rowell, Lucas S. Kupssinskü

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06348v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06348v1)

**Summary:** The paradigm of global weather forecasting is rapidly shifting with the emergence of Machine Learning Weather Prediction models (MLWP). While these data-driven architectures demonstrate remarkable global skill, regional benchmarks in the Global South remain scarce, leaving their efficacy in complex, highly convective environments largely unverified. This study evaluates the performance of GraphCast operational against the deterministic ECMWF IFS HRES as baseline across four distinct Brazilian cl...

---

### 27. Attack Detection using Time Series Foundation Models

**Authors:** Sribalaji C. Anand, Anh Tung Nguyen, George J. Pappas

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06347v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06347v1)

**Summary:** This paper addresses the problem of attack detection in cyber-physical systems without any knowledge of the plant model or its structure. A remotely located plant transmits sensor measurements to an operator over a network that is assumed to be under attack. We consider two classes of attacks: model-free replay attacks and model-based stealthy attacks. For the latter, we derive closed-form expressions for the optimal stealthy attack policy against a $χ^2$ detector, for both linear and nonlinear ...

---

### 28. Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation

**Authors:** Yohann Benchetrit, Marlène Careil, Simon Dahan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06345v1)

**Summary:** Brain decoding is limited by the availability of labeled neural data, and remains challenging in low-data regimes. To address this issue, we investigate whether and when brain decoding can be boosted by augmenting small fMRI datasets with synthetic data generated by a pretrained model of fMRI responses to stimuli. We use TRIBE v2, a large encoding model pretrained on more than 1000 hours of fMRI responses to video, audio and language. For each dataset, we evaluate systematic grids that show how ...

---

### 29. Equivariant Neural Belief Propagation

**Authors:** Zehua Cheng, Wei Dai, Jiahao Sun

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06344v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06344v1)

**Summary:** Probabilistic inference over spatially embedded variables requires beliefs that respect $SE(3)$ symmetry, yet existing equivariant networks produce only scalars and vectors -- not the rank-2 precision tensors needed for anisotropic uncertainty, and single-component messages collapse multi-modal energy landscapes to physically meaningless averages. We introduce Equivariant Neural Belief Propagation (ENBP), a factor-graph framework whose messages are equivariant Gaussian mixture models with suffic...

---

### 30. Symmetric Divergence and Normalized Similarity: A Unified Topological Framework for Representation Analysis

**Authors:** Yan Wang, Tianyang Hu

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06342v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06342v1)

**Summary:** Topological Data Analysis (TDA) offers a principled, intrinsic lens for comparing neural representations. However, existing paired topological divergences (e.g., RTD) are limited by heuristic asymmetry and, more critically, unbounded scores that depend on sample size, hindering reliable cross-scenario benchmarking. To address these challenges, we develop a unified topological toolkit serving two complementary needs: fine-grained structural diagnosis and robust, standardized evaluation. First, we...

---

### 31. Bridging Domain Expertise and Generalization for Performance Estimation

**Authors:** Shuxuan Li, Zhilin Zhao, Quyu Kong, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06335v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06335v1)

**Summary:** Performance estimation under distribution shift aims to predict how a model behaves on an unlabeled test set whose distribution differs from the training data, a scenario that requires reliable indicators that can faithfully reflect model behavior without ground-truth labels. Existing approaches rely solely on the outputs of the given model whose biases are amplified once the distribution shifts, weakening the correlation with the true performance. Motivated by this limitation, we propose Fused ...

---

### 32. Quantifying the Privacy of Counterfactuals by Leveraging Membership Inference Attacks Against Synthetic Data

**Authors:** Maryam Babaei, Yingke Wang, Hadrien Lautraite, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06334v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06334v1)

**Summary:** Counterfactuals are typically used in high-stakes decision areas to explain a machine learning model by showing how changes to the user profiles result in the desired outcome. However, explaining the model's decisions through counterfactuals can also be exploited by an adversary to conduct privacy attacks against the model or its training data. Drawing on the analogy that counterfactuals provide realistic substitutes for real training data, similar to synthetic data, we demonstrate in this paper...

---

### 33. Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability

**Authors:** Seyed Arshan Dalili, Mehrdad Mahdavi

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06333v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06333v1)

**Summary:** Sparse Autoencoders (SAEs) are widely used for mechanistic interpretability in large language models, yet their formulation assigns each latent feature a single decoder direction, implicitly assuming features to be one-dimensional. We show that this assumption mismatches with the multi-dimensional structure of model features, provably inducing feature splitting through two distinct mechanisms. Geometrically, reconstructing a feature of intrinsic dimension $d_i \ge 2$ to error $\varepsilon$ with ...

---

### 34. Efficient Mean Curvature Computation on High-Dimensional Data Manifolds

**Authors:** Alexandre L. M. Levada

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06329v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06329v1)

**Summary:** Estimating local mean curvature at each point of a high-dimensional dataset is a key ingredient of geometry-aware machine learning algorithms, such as the Mean Curvature Boundary Points (MCBP) method. The naive implementation of this computation, based on a local shape operator approximated from k-nearest neighbor patches, involves an explicit construction of a matrix $H$ whose trace form yields an $O(m^4)$ cost per point, rendering the approach intractable for datasets with more than a few doze...

---

### 35. PAMF: Prior-Aware Multimodal Fusion for Incomplete Time Series Data

**Authors:** Ziwen Kan, Wugeng Zheng, Tianlong Chen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06328v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06328v1)

**Summary:** In healthcare, multimodal time series tasks often operate on incomplete observations in practice, for example when ECG segments are lost because electrodes detach or an entire respiratory channel is unavailable during overnight monitoring. Such missingness typically appears in two structurally distinct patterns: within-modality missing, where values are absent within an otherwise observed modality, and modality-level missing, where an entire modality is unavailable. Existing methods typically re...

---

### 36. Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

**Authors:** Gizem Yüce, Giorgos Nikolaou, Nicolas Flammarion

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06320v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06320v1)

**Summary:** Machine unlearning aims to remove targeted knowledge from a trained model while preserving its general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. Existing approaches either ignore this heterogeneity or rely on auxiliary models, heuristics, or external annotations to estimate each token's relevance for forgetting. We instead characterize it through the interaction with the retain objective: a token is forget-specific to ...

---

### 37. DAS-PINNs for high-dimensional partial differential equations: extending deep adaptive sampling to spacetime domains

**Authors:** Anshima Singh, David J. Silvester

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06314v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06314v1)

**Summary:** Time-dependent high-dimensional partial differential equations (PDEs) with spatially localised and dynamically evolving solutions pose a fundamental challenge for physics-informed neural networks (PINNs), as uniform collocation sampling becomes increasingly ineffective in high-dimensional spatiotemporal domains. In this work, a deep adaptive sampling framework for PINNs is extended to the time-dependent setting by treating space and time as a unified domain without any explicit time marching. A ...

---

### 38. Wall Shear Stress Reconstruction from Concentration: Differentiable Physics and Physics-Informed Neural Networks

**Authors:** Mahmoud Elhadidy, Siva Viknesh, Roshan M. D'Souza, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06313v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06313v1)

**Summary:** Wall shear stress (WSS) governs near-wall transport dynamics and is a key hemodynamic indicator in cardiovascular flows, yet remains difficult to infer accurately due to the need for precise computation of near-wall velocity gradients. Passive scalar fields, such as concentration or temperature, are advected by the same underlying velocity field and have the potential to uncover hidden flow physics metrics such as WSS. In this work, we demonstrate such reconstruction from spatially limited passi...

---

### 39. Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction

**Authors:** Hongkun Dou, Zike Chen, Fengji Li, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06303v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06303v1)

**Summary:** Controllable generation with discrete diffusion models is often hindered by high computational overhead or the need for retraining. In this paper, we present \underline{\textbf{G}}radient-\underline{\textbf{I}}nformed \underline{\textbf{L}}ogit \underline{\textbf{C}}orrection (\textbf{GILC}), a plug-and-play framework that efficiently estimates guidance signals by repurposing the pretrained denoising network as a variational proxy. To circumvent the gradient instability inherent in high-dimensio...

---

### 40. Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving

**Authors:** Hyungmin Kim, Minsoo Kim, Hongseok Kim, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06302v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06302v1)

**Summary:** Multi-turn Large Language Model (LLM) serving is critical for consistent user experiences, yet the linear growth of the Key-Value (KV) cache imposes significant pressure on GPU memory and bandwidth. Non-uniform KV compression effectively preserves more information by considering the individual importance of each KV cache. However, such KV cache heterogeneity introduces various systemic challenges - including memory fragmentation, scheduling complexities, and diminished kernel utilization - which...

---

### 41. Reactive Flux Matching: Mechanism Discovery and Adaptive Sampling of Rare Events

**Authors:** Rishal Aggarwal, David Ryan Koes, Nicholas M. Boffi, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06295v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06295v1)

**Summary:** Path sampling methods generate ensembles of reactive trajectories connecting metastable states, but extracting mechanistic insight from these data remains nontrivial. We introduce Flux Matching, a framework that learns two complementary objects directly from reactive trajectory data: a current velocity $u(z)$, whose streamlines trace the dominant reaction pathways, and a scalar potential $h(z)$, obtained from a weighted Helmholtz-Hodge decomposition of the reactive current, that serves as a data...

---

### 42. PAC-Bayesian Adversarially Robust Generalization for Message Passing Graph Neural Networks: A Sensitivity Analysis

**Authors:** Ziling Liang, Xinping Yi, Qingsong Wen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06293v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06293v1)

**Summary:** Whilst the vulnerability of graph neural networks (GNNs) to adversarial attacks poses a critical threat to graph representation learning, the understanding of the robust generalization behavior remains a fundamental challenge in the adversarial setting. Recently, PAC-Bayesian margin-based generalization analysis substantially advances this line of research by providing a flexible and data-dependent analytical framework. However, existing robust analyses often rely on isotropic Gaussian posterior...

---

### 43. Discrete Causal Representations from Heterogeneous Domains: A Bayesian Approach with Social Survey Applications

**Authors:** Ankur Garg, Michael Stettler, Aaron Schein, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06288v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06288v1)

**Summary:** Causal representation learning aims to infer the high-level latent causal concepts that give rise to observed low-level measurements. This is particularly relevant for heterogeneous data from different environments or domains since distribution shifts often arise through sparse, localized changes in some of the underlying causal mechanisms, while other parts of the generative process remain unchanged. Whereas identifiability of causal representations has been studied extensively, practical uncer...

---

### 44. Your GFlowNet Secretly Learns an Optimal Transport Plan

**Authors:** Ian Maksimov, Nikita Morozov, Denis Belomestny, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06272v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06272v1)

**Summary:** Generative Flow Networks (GFlowNets) are a framework for sampling structured objects via stochastic trajectories in a directed graph. In this work, we establish a theoretical connection between non-acyclic GFlowNets and optimal transport (OT). We show that fixing the initial flow distribution in a minimum-flow GFlowNet reduces its objective to a Kantorovich OT problem with graph-induced shortest path costs. At the optimum, the learned GFlowNet policy therefore encodes an optimal transport plan f...

---

### 45. GRAMformer: Any-Order Modality Interactions via Volumetric Multimodal Cross-Attention

**Authors:** Giordano Cicchetti, Eleonora Grassucci, Danilo Comminiello

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06249v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06249v1)

**Summary:** Transformer-based multimodal models rely on attention mechanisms to integrate information across heterogeneous modalities. Despite their success, existing multimodal attention formulations compute their scores through collections of pairwise dot-product interactions or by concatenating all the modalities into the keys, even when multiple modalities should be jointly involved. As a consequence, current approaches either incur quadratic complexity in the number of modalities or fail to explicitly ...

---

### 46. Generative Criticality in Large Language Model Temperature Scaling

**Authors:** Huajian Ruan, Jinyang Li, Xingyu Guo, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06238v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06238v1)

**Summary:** We propose a statistical-field framework for text generated by large language models (LLMs), treating token embeddings as continuous spin variables on a one-dimensional chain. Defining a susceptibility from the connected two-point correlator and an order parameter from the ensemble-averaged embedding field, we vary the \texttt{softmax} temperature $T$ and observe a sharp susceptibility peak near a characteristic $T_c$ with power-law-like scaling, a concurrent rapid change in the order parameter,...

---

### 47. Tracing the Oracle: Improving Diffusion Timestep Scheduling for 3D CT Reconstruction

**Authors:** Yujia Wu, Zhaoqiang Liu

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06236v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06236v1)

**Summary:** Pretrained diffusion models demonstrate impressive potential in solving highly ill-posed 3D computed tomography (CT) inverse problems, while the inference process suffers from significant computational overhead. Furthermore, existing uniform timestep schedules fail to capture the non-uniform evolution of the reverse conditional diffusion stochastic differential equation, thereby introducing substantial truncation errors. To overcome this limitation, we propose Tracing the Oracle (TrO), a plug-an...

---

### 48. Design a Reliable LLM-Integrated Interface for Mortality Forecasting

**Authors:** Thi Kim Ngan Nguyen

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06235v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06235v1)

**Summary:** Mortality forecasting plays an important role in actuarial and policy decision-making, but its implementation remains technically complex and inaccessible to non-expert users. This project proposes a reliable large language model (LLM)-integrated interface that improves usability while maintaining statistical power. The LLM is designed as a constrained orchestration layer that translates natural-language inputs into structured configurations for a deterministic forecasting pipeline. A three-phas...

---

### 49. Anchor PCA

**Authors:** Benedikt Seiter, Anya Fries, Julius von Kügelgen, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06233v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06233v1)

**Summary:** Principal component analysis (PCA) is one of the most widely used unsupervised dimension reduction techniques. We study PCA for data from multiple related domains. Since principal components generally differ across domains, one way to obtain a shared low-rank embedding is to perform PCA on the pooled data. However, this approach can focus on spurious directions that exhibit high variation in only a few domains. To find a robust embedding that still explains most variance in unseen but similar do...

---

### 50. Drag reduction or reward hacking? Recurrent multi-agent reinforcement learning that earns its reward

**Authors:** Giorgio Maria Cavallazzi, Miguel Pérez-Cuadrado, Alfredo Pinelli

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06227v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06227v1)

**Summary:** A reinforcement-learning agent maximises its reward, which can diverge from the outcome its designer intended. In physical control the reward rarely closes that gap, and drag reduction in wall turbulence makes it concrete. A mass-conservation projection couples agents' outputs and erases the per-agent credit the policy gradient needs; a memoryless policy cannot resolve the slow near-wall cycle it acts on; and a pressure-gradient reward pays for nominal drag reduction by pumping power through the...

---

## cs.NE

**50 papers**

### 1. Emergent Language as an Approach to Conscious AI

**Authors:** Zengqing Wu, Chuan Xiao

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06380v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06380v1)

**Summary:** The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of sel...

---

### 2. Hub-Aware Hybrid Search: Accelerating the Locally Aligned Ant Technique

**Authors:** Simone Vilardi, Reynier Peletier, Felipe Contreras, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06198v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06198v1)

**Summary:** Finding manifold structures in noisy and high-dimensional point clouds is a challenging but important problem. In astronomical observation survey and simulation data the detection of filaments, streams (1D), walls (2D) and clusters (3D) gives rise to deeper understanding of the evolution of our universe. The Locally Aligned Ant Technique (LAAT) uses biologically inspired agents to efficiently recover faint and multidimensional structures. However, very dense hubs (e.g. nodes or globular clusters...

---

### 3. ITP-STDP: An Intrinsic-Timing Power-of-Two Learning Engine for On-Chip SNN Training

**Authors:** Haihang Xia, Xinyu Zhao, Xuecheng Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06159v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06159v1)

**Summary:** Spiking neural networks (SNNs) have the potential to emerge as the third generation of neural networks and have attracted increasing attention across a wide range of applications. However, the large number of synaptic connections in SNNs leads to intensive weight-update computation by on-chip learning algorithms during training, resulting in substantial hardware resource utilization and energy consumption. Among existing SNN learning algorithms, spike-timing-dependent plasticity (STDP) is one of...

---

### 4. Sample-efficient Low-level Motion Planning for Robotic Manipulation Tasks via Zero-shot Transfer Learning

**Authors:** Yuanzhi He, Victor Romero-Cano, José J. Patiño, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06041v1)

**Summary:** As robotic systems become more sophisticated, the growing complexity of their motion planning models and the longer training times pose substantial challenges. Evolutionary algorithms such as the Sample-efficient Cross-Entropy Method (iCEM) have recently demonstrated promising potential for low-level real-time planning by leveraging efficient knowledge reuse strategies to improve performance. Although effective in many control tasks, iCEM's performance can be constrained in more complex scenario...

---

### 5. Quantifying Uncertainty In Wide Two-Layer Neural Networks: On The Law Of The Limiting Fluctuation Process

**Authors:** Arnaud Descours, Arnaud Guillin, Geoffrey Lacour, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05982v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05982v1)

**Summary:** Uncertainty quantification in neural networks prediction is a main issue for usual applications. Our approach seeks at reducing computation costs by directly evaluating uncertainty using PDE's information on the asymptotic variance, rather than the deep ensemble method which may be seen as a Monte Carlo estimation of the prediction, requiring the training of multiple networks. We thus study the law of the limiting process describing the random fluctuations around the mean-field limit of wide two...

---

### 6. From Prediction to Self: Developmental Conditions for Agency in Minimal Neural Systems

**Authors:** Evan Ye

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05605v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05605v1)

**Summary:** How does a system that merely predicts the world come to distinguish its own causal influence from everything else? We trace this transition in a minimal 192-dimensional GRU through 40 controlled experiments arranged as a developmental sequence, adding components one at a time and tracking whether the system can distinguish self-caused from world-caused changes.   The developmental path reveals four conditions that must be satisfied in strict order: (1) persistent state forming stable attractors...

---

### 7. Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution

**Authors:** Can Gurkan, Forrest Stonedahl, Uri Wilensky

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.05408v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05408v1)

**Summary:** When an LLM repeatedly mutates a program, does it explore new forms or circle back to the same ones? We study this question by analyzing LLM-driven mutation chains in the absence of selection pressure within a domain-specific language, varying prompt design, model family, and stochastic replication. We find that LLM-based mutation consistently converges toward restricted attractor regions in program space. Convergence is especially severe at the structural level: in 87% of chains, over 93% of mu...

---

### 8. Multi-Column RBF Neural Network Using Adaptive and Non-Adaptive Particle Swarm Optimization

**Authors:** Ammar Hoori, Yuichi Motai

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.05150v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05150v1)

**Summary:** The radial basis function neural network (RBFN) trained with a gradient descending algorithm provides an effective fully connected structure in both shallow and deep networks. The error correction (ErrCor), a state-of-the-art gradient-based training method, selects optimal hidden units to improve accuracy. Alternatively, as a population-based algorithm, the particle swarm optimization algorithm (PSO) uses the swarm experience to optimize RBFN parameters, offering global search and robustness to ...

---

### 9. U-Net-Accelerated Quality-Diversity Optimization for Climate-Adaptive Urban Layouts

**Authors:** Alexander Hagg, Tania Guerrero, Dirk Reith

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04658v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04658v1)

**Summary:** Optimizing urban layouts for climate adaptation requires balancing building density with cold-air ventilation. Because physics-based climate simulations are computationally expensive, planners typically evaluate fewer than ten manual designs. \gls{qd} algorithms offer a way to systematically illuminate the design space, but they require surrogate models to be practical.   In this paper, we replace a slow, regulatory physics simulator with a spatial deep-learning surrogate (U-Net) inside an offli...

---

### 10. Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning

**Authors:** Damian Lebiedź, Robert Ślepaczuk

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04574v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04574v1)

**Summary:** This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair trading in highly volatile cryptocurrency markets. Although classical implementations of the strategy have proven successful in traditional equities, they frequently exhibit rigidity and suffer from severe divergence risks when applied to high-variance environments. To address this need, this research introduces novel concepts. To construct a robust system...

---

### 11. ParetoPilot: Zero-Surrogate Offline Multi-Objective Optimization via Infer-Perturb-Guide Diffusion

**Authors:** Ruiqing Sun, Sen Yang, Dawei Feng, et al.

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04468v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04468v1)

**Summary:** Offline multi-objective optimization (Offline MOO) aims to discover novel Pareto-optimal designs based on static datasets without expensive environment interactions. While recent generative methods have achieved notable success, they predominantly rely on external surrogate models. This dependency introduces significant computational overhead, suffers from deceptive evaluations, and deviates from the prevailing paradigm of jointly training mainstream generative models with conditions. To address...

---

### 12. Quadratic integrate-and-fire neurons exhibit less fragmented loss landscapes and outperform leaky integrate-and-fire neurons in spike-based gradient descent

**Authors:** Carlo Wenig, Raoul-Martin Memmesheimer, Christian Klos

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03935v1)

**Summary:** The ability to train spiking neural networks is essential for modeling biological neural networks as well as for neuromorphic computing. However, for the extensively used leaky integrate-and-fire (LIF) neurons, arbitrarily small parameter changes can induce spike (dis)appearances that disrupt subsequent activity, leading to unstable neural representations and permanently silent neurons during exact spike-based gradient descent. Recent work shows that a class of neuron models, which includes the ...

---

### 13. Calibrating Urban Traffic Simulation from Sparse Road Observations via Genetic Optimization

**Authors:** Hunter Sawyer, Jesse Roberts, Simon Matei

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03823v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03823v1)

**Summary:** Urban traffic simulation is a critical tool for infrastructure planning, including the placement of electric vehicle charging stations. However, realistic traffic simulation across many cities is hindered by two fundamental data limitations: detailed real-world traffic measurements are available for only a small fraction of road segments in most cities, and employment distribution data critical for modeling commuter traffic is rarely available at the resolution needed for simulation. This paper ...

---

### 14. Signed Spiking Neuron Enabled by an Orthogonal-Easy-Axis Magnetic Tunnel Junction

**Authors:** Huannan Zheng, Jingli Liu, Kezhou Yang

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03796v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03796v1)

**Summary:** Signed spiking neurons carry richer information than standard spiking neurons. This work proposes a compact magnetic tunnel junction (MTJ)-based neuron for signed leaky integrate-and-fire (LIF) operation. With orthogonal easy axes in the free and pinned layers, the device enables bipolar spike generation and maps magnetic-moment dynamics to signed LIF membrane-potential evolution. Landau--Lifshitz--Gilbert simulations show that proper free-layer dimensions allow the device response to follow a s...

---

### 15. Training a Predictive Coding Network on ImageNet using Equilibrium Propagation

**Authors:** Tugdual Kerjan, Rasmus Høier, Benjamin Scellier

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03584v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03584v1)

**Summary:** Equilibrium Propagation (EP) is a physics-based training framework that has primarily been employed in energy-based models, including continuous Hopfield networks, nonlinear resistive networks and coupled phase oscillators. However, EP's practical applications have so far remained limited to relatively small-scale problems. Predictive coding networks (PCNs), another class of energy-based models rooted in computational neuroscience, are typically trained with a specialized algorithm and have like...

---

### 16. Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics in a PFC-Inspired Reservoir Model for Multistep Goal-Directed Action Planning

**Authors:** Jin Nakamura, Yuichi Katori

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03481v1)

**Summary:** The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. Here we ask whether short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics. We incorporated STP into a PFC-inspired reservoir computing model with basal-ganglia-inspired temporal-difference readout learning, and evaluated paired models with and without STP ac...

---

### 17. PrimeSVT: An Automated Memory-aware Pruning Framework with Prioritized Compression Policy for Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Achyuta Muthuvelan, Alberto Marchisio, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03428v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03428v1)

**Summary:** The large sizes of Spiking Vision Transformers (SViTs) still hinder their embedded implementation, highlighting the need for model compression. State-of-the-art works compress SViT models through unstructured pruning, which needs specialized hardware accelerators for their specific sparsity patterns to maximize efficiency gains. Moreover, their manual approach requires a huge design time to find an appropriate pruning setting for each network, thus making this approach not scalable. To address t...

---

### 18. Optimizing Explicit Unit-Distance Lower-Bound Certificates

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03419v2) | 📄 [PDF](https://arxiv.org/pdf/2606.03419v2)

**Summary:** The 2026 disproof of Erdős's unit-distance conjecture and Sawin's subsequent explicit quantitative refinement show that the maximum number $u(n)$ of unit distances among $n$ planar points can exceed $n^{1+\varepsilon}$ for a fixed positive $\varepsilon$. Sawin's explicit bound gives more than $n^{1.014}$ unit distances for arbitrarily large $n$ and exposes integer parameters whose choice is not fully optimized. This report starts from Sawin's nonlinear integer optimization problem and develops a...

---

### 19. PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Achyuta Muthuvelan, Alberto Marchisio, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03257v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03257v1)

**Summary:** Spiking Vision Transformer (SViT) models are promising low-power ViT models for solving vision-based tasks with state-of-the-art performance. However, their large sizes limit their deployments for resource-constrained embedded platforms, underscoring the needs of model compression. One of prominent compression techniques is pruning, and the state-of-the-art works employ unstructured pruning techniques to compress SViT models. Such techniques require specialized hardware architectures tailored fo...

---

### 20. Beyond Static Priors: Dynamic Neural Guidance for Large-Scale Ant Colony Optimization

**Authors:** Dat Thanh Tran, Van Khu Vu, Yining Ma

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.04039v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04039v1)

**Summary:** Neural-guided Ant Colony Optimization (ACO) suffers from a fundamental training-inference misalignment: policies are typically trained to generate static priors (e.g., heatmaps), yet deployed to guide iterative, long-horizon search processes. In this paper, we present DyNACO, a novel framework that achieves dynamic neural guidance by periodically observing the pheromone distribution and the incumbent solution. To make DyNACO tractable at scale, we pair the policy with a perturbation-based ACO ba...

---

### 21. Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity CPUs

**Authors:** Ting Liu

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03026v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03026v1)

**Summary:** Spiking language models expose activation sparsity that dense Transformer runtimes do not directly exploit. This paper studies that property from a systems perspective. Building on the SymbolicLight V1 spike-gated language model family, we implement a C++ CPU inference runtime that treats sparse binary spike states as an execution primitive rather than only applying post-hoc weight compression. The runtime combines a manifest-driven weight loader, mixed row/column memory layout, AVX2/FMA kernels...

---

### 22. Self-Regulation through Communication in Evolved Neural Agents

**Authors:** Joshua Nunley

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02840v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02840v1)

**Summary:** Communication is typically understood as indication: signals that transfer information from sender to receiver. We present a minimal predator avoidance task in which pairs of evolved CTRNN agents use communication for robust survival, and in which agents hear their own vocalizations, as in natural systems. Across 112 perfect-fitness agents from over 2,000 evolutionary runs, three dominant strategies emerge (accounting for 81% of agents): safety calling (39%), where agents signal from safe cover;...

---

### 23. Simultaneous Model-Based Evolution of Constants and Expression Structure in GP-GOMEA for Symbolic Regression

**Authors:** Johannes Koch, Tanja Alderliesten, Peter A. N. Bosman

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02236v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02236v1)

**Summary:** Genetic programming (GP) approaches are among the state-of-the-art for symbolic regression, the task of constructing symbolic expressions that fit well with data. To find highly accurate symbolic expressions, both the expression structure and any contained real-valued constants, are important. GP-GOMEA, a modern model-based evolutionary algorithm, is one of the leading algorithms for finding accurate, yet compact expressions. Yet, GP-GOMEA does not perform dedicated constant optimization, but ra...

---

### 24. On the Evaluation of Spiking Neural Network Configurations for Network Intrusion Detection

**Authors:** Raj Patel, David Amebley, Taye Akinrele, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01442v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01442v1)

**Summary:** Network intrusion detection is a core component of modern cybersecurity infrastructure, yet the deep learning models that dominate the field are computationally demanding, motivating interest in lightweight alternatives suited to edge and neuromorphic deployment. Spiking Neural Networks (SNNs) are therefore a natural candidate, but their design space, spanning the choice of neuron model and spike encoding scheme, remains poorly characterized for intrusion detection. We bridge this gap by using a...

---

### 25. Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition

**Authors:** Tauseef Ahmed, Tao Sun, Jeronimo Castrillon, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01135v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01135v1)

**Summary:** Deep learning has greatly advanced automatic speech recognition (ASR), enabling widespread deployment on edge devices such as smartphones and smart home systems. However, the computational and energy demands of deep neural networks pose significant challenges for such resource-constrained deployments, introducing latency and limiting real-time interaction. Neuromorphic computing offers a promising solution by introducing activation sparsity through spiking neural networks (SNNs) and event-driven...

---

### 26. Breaking the Cascade: Compact Nonlinear Optical Computing with Single-Layer Encoder-Decoder Co-Localization

**Authors:** Yuntian Wang, Alexander Chen, Md Sadman Sakib Rahman, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01032v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01032v1)

**Summary:** We demonstrate that nonlinear computing can be achieved with a single linear diffractive surface under coherent illumination. We introduce a compact encoder-decoder co-localization (E+D) architecture in which an input-dependent dynamic encoder and a static optimized decoder are integrated within the same phase-only diffractive plane. Following free-space propagation, coherent interference between the encoder and decoder fields, combined with intensity detection, generates programmable nonlinear ...

---

### 27. Meta-Black-Box Optimization with Ensemble Surrogate Modeling for Robustness-Accuracy Trade-off within SAEA

**Authors:** Xiao Jin, Yongxiong Wang, Haobo Liu, et al.

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00862v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00862v1)

**Summary:** Surrogate-assisted evolutionary algorithms (SAEAs) have been widely used for expensive black-box optimization problems. However, their reliance on rigid and manually designed components limits their flexibility and generalization across tasks. Meta-black-box optimization (MetaBBO) provides a promising paradigm for adaptively configuring algorithmic components. Nevertheless, existing MetaBBO methods usually control only a single component, and few studies have investigated the unified control of ...

---

### 28. Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs

**Authors:** Subhadip Mitra

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00813v1)

**Summary:** Safety alignment in LLMs does not improve monotonically across model generations. Studying four generations of Google's Gemma family (7B-31B) with quality-diversity evolution (MAP-Elites) as an automated red-teaming probe, we find that Gemma 3 (12B) exhibits 68.7% +/- 5.7% attack success rate (ASR; mean +/- std, 3 seeds), significantly higher than its predecessor Gemma 2 (45.5% +/- 7.2%; p = 0.030, paired bootstrap) and its successor Gemma 4 (33.9% +/- 1.8%). Replaying evolved attack archives ac...

---

### 29. Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety

**Authors:** Subhadip Mitra

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00801v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00801v1)

**Summary:** Current approaches to LLM adversarial testing suffer from coverage gaps: manual red-teaming does not scale, LLM-as-attacker methods exhibit mode collapse, and gradient-based approaches produce uninterpretable gibberish. We introduce a quality-diversity evolutionary framework that operates at the semantic level, evolving interpretable attack strategies rather than token sequences. Using MAP-Elites, we maintain a diverse archive of attacks across behavioral dimensions (strategy type, encoding meth...

---

### 30. Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks

**Authors:** Ezekiel Williams, Alexandre Payeur, Guillaume Lajoie

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.00243v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00243v1)

**Summary:** Biological and neuromorphic recurrent neural networks (RNNs) are subject to spatial and temporal locality constraints on the information that can plausibly be used during learning. A common strategy to satisfy these constraints is to modify gradient descent by neglecting non-local terms to varying degrees, as in random feedback local online (RFLO) learning and truncated backpropagation through time (tBPTT). However, the learning dynamics of these algorithms, and how they compare with BPTT, remai...

---

### 31. Institutions and the transmission of upper-tail human capital: scientific lineages across a millennium

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.31470v1) | 📄 [PDF](https://arxiv.org/pdf/2605.31470v1)

**Summary:** What made useful knowledge cumulative was not discovery alone but the institutions that transmitted it. We provide the first exhaustive structural measurement of the network through which upper-tail human capital passed from master to student across a millennium. Using 470,000 mentor-student records from Wikidata (which integrates the Mathematics Genealogy Project and MacTutor Archive), and all 64 historical Fields Medalists as a fixed, ex ante tracer set, backward traversal yields a directed ac...

---

### 32. Memristor-Based Spiking Neural Network Accelerator for Bio-inspired Interception Task

**Authors:** Qianhou Qu, Sheng Lu, Liuting Shang, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.31299v1) | 📄 [PDF](https://arxiv.org/pdf/2605.31299v1)

**Summary:** Spiking neural networks (SNNs) provide event-driven and low-power computation inspired by biological neural systems, but current implementations rely on von Neumann graphics processing units (GPUs) and central processing units (CPUs) platforms, where memory and computation bottlenecks limit energy efficiency. To address this challenge, this paper proposes an analog memristor-based spiking neural network (SNN) accelerator that integrates in-memory synaptic computation with analog integrate-and-fi...

---

### 33. Developing a novel Comorbidities Index for predicting 10-year mortality in Prostate Cancer patients: A computational data-driven approach

**Authors:** Davide Farinati, Francesco Barletta, Paolo Zaurito, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.31213v2) | 📄 [PDF](https://arxiv.org/pdf/2605.31213v2)

**Summary:** The Charlson Comorbidities Index (CCI) is a weighted additive index widely used to estimate ten-year mortality risk, but its original weights may not reflect contemporary prognoses. This limitation is critical in Prostate Cancer (PCa), where radical treatment is recommended only for patients with a life expectancy of at least ten years. For candidates eligible for Radical Prostatectomy (RP), accurate estimation of ten-year other-cause mortality is essential to balance oncological benefit against...

---

### 34. Oscillatory State-Space Models as Inductive Biases for Physics-Informed Neural PDE Solvers

**Authors:** Abhishek Chandra, Taniya Kapoor

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.02623v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02623v1)

**Summary:** Solving time-dependent partial differential equations (PDEs) is an important problem in computational science and engineering. Physics-informed neural networks (PINNs) learn PDE solutions from governing equations. However, accurately capturing temporal evolution remains challenging. Recent sequence-model-based approaches parameterize time evolution using general-purpose sequence models, which capture temporal dependencies but do not explicitly encode the structured dynamics of PDE solutions. In ...

---

### 35. Linear Ordering Problem: Time for a Change

**Authors:** Fabrizio Fagiolo, Marco Baioletti, Valentino Santucci

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.31051v1) | 📄 [PDF](https://arxiv.org/pdf/2605.31051v1)

**Summary:** The Linear Ordering Problem (LOP) is a fundamental combinatorial optimization problem with important applications in areas such as economics, social choice, and machine learning. Its most prominent use is the triangulation of economic input-output tables, which helps identify critical industries in an economy. Most existing algorithms have been evaluated on benchmarks derived from outdated macroeconomic data, which no longer reflect the structure of contemporary economies. Furthermore, LOP insta...

---

### 36. GP-GOMEA with GPU-Based Fitness Evaluations: Design and Performance Analysis

**Authors:** Jasper Post, Johannes Koch, Anton Bouter, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.30954v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30954v1)

**Summary:** GP-GOMEA is a state-of-the-art evolutionary algorithm for symbolic regression, known for discovering small and interpretable models. However, its computational cost remains substantial, limiting its applicability to larger datasets and more complex target expressions. In contrast, the rise of modern subsymbolic approaches, particularly deep learning, has been driven largely by the massive parallelism offered by GPUs. In this work, we take the first major step toward a fully GPU-accelerated GP-GO...

---

### 37. Agnosiophobia in a virtual agent: behavioral and dynamical architecture in Lenia

**Authors:** Jesse Cool, Benedikt Hartl, Michael Levin, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.30708v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30708v1)

**Summary:** All embodied agents are fundamentally patterns in physiological or other excitable media, blurring the distinction between objects and processes. Emergent patterns with complex behaviors, such as Gliders in the Game of Life and virtual patterns in Lenia, are powerful model systems in which to understand the properties and origins of behavioral traits in novel agents. To evaluate the behavior of patterns in Lenia, we introduce regions into their environment from which no sensory information is av...

---

### 38. Deep Binarized Photonic Reservoir Computing for Ultrafast Multimedia Signal Processing

**Authors:** Muhammad Waqar Iqbal, Mohamad Alassir, Nicolas Marsal, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.30149v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30149v1)

**Summary:** We present a deep photonic neural network architecture based on ultrafast binary optical modulation from a digital micro-mirror device (DMD), optical scattering in random medium, high-speed photodetection with a CMOS sensor, and time-multiplexed deep layer structure. Operating at Gigabit-per-second (Gb/s) processing rates, our system based on the reservoir computing (RC) framework achieves state-of-the-art performance across various multimedia tasks, including video, image and speech recognition...

---

### 39. Evolving Features vs Evolving Entire Trees with GP for Interpretable Survival Analysis

**Authors:** Thalea Schlender, Peter A. N. Bosman, Tanja Alderliesten

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.30119v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30119v1)

**Summary:** Survival analysis concerns the task of predicting the time until an event occurs. Often used in the medical field, survival analysis deals with incomplete (i.e., censored) data, for instance, from patients who did not experience the event during the duration of the study. For practical use, both accuracy and interpretability are important.   Survival trees are easy-to-follow survival models that split the patient cohort recursively into discrete patient groups. Whilst survival trees can capture ...

---

### 40. Selection Hyper-heuristics Can Automatically Adjust the Learning Period to Optimally Solve Pseudo-Boolean Problems

**Authors:** Benjamin Doerr, Pietro S. Oliveto, John Alasdair Warwicker

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29916v1) | 📄 [PDF](https://arxiv.org/pdf/2605.29916v1)

**Summary:** The Random Gradient hyper-heuristic was recently shown to be able to learn the optimal neighbourhood size when optimizing the LeadingOnes benchmark via the Randomised Local Search (RLS) meta-heuristic. However, for this to happen, a learning period of a certain length $τ$ had to be used, differently from classic hyper-heuristics, which change their behaviour based on the success of only the previous iteration. In this paper, we show how to automatically set this new parameter value, relieving th...

---

### 41. Evolutionary Rule Extraction from Corporate Default Prediction Models

**Authors:** Desirè Fabbretti, Matteo Pasquino, Elia Pacioni, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29478v1) | 📄 [PDF](https://arxiv.org/pdf/2605.29478v1)

**Summary:** Small and medium-sized enterprises (SMEs) represent the majority of firms in most economies and often face financial constraints and higher vulnerability to financial distress. Predicting SME default is therefore crucial for financial institutions, policymakers, and researchers. Recent advances in machine learning (ML) have improved predictive performance in credit risk modeling. Yet, the limited interpretability of complex models raises concerns regarding transparency and regulatory compliance....

---

### 42. Runtime Analysis of a Compact Genetic Algorithm on a Truly Multi-valued OneMax Function

**Authors:** Martin S. Krejca, Carsten Witt

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29477v2) | 📄 [PDF](https://arxiv.org/pdf/2605.29477v2)

**Summary:** Recently, the runtime analysis of multi-valued estimation-of-distribution algorithms in the framework of Ben Jedidia et al. (TCS 2024) has made significant advancements. However, almost all existing analyses are limited to multi-valued objective functions that in each dimension only distinguish between two types, also called categories, of values and hence can be treated with similar methods as pseudo-Boolean problems. Only recently, Adak and Witt (GECCO 2025) have presented a first runtime anal...

---

### 43. EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization

**Authors:** Tao Jiang, Xinmeng Yu, Chenhao Yi, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29295v1) | 📄 [PDF](https://arxiv.org/pdf/2605.29295v1)

**Summary:** Evolutionary model merging provides a powerful framework for the automated, training-free composition of LLMs through parameter-space search. However, existing methods predominantly rely on stochastic, hand-crafted operators that overlook the underlying performance landscape of the coefficient space. We propose Evolutionary Generative Merging (EvoGM), a framework that transcends manual heuristics by employing learnable generative modeling to optimize merging coefficients. Specifically, EvoGM fea...

---

### 44. Compute Allocation in Evolutionary Search: From Depth-Breadth to Multi-Armed Bandits

**Authors:** Sixue Xing, Haoyu He, Kerui Wu, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29268v2) | 📄 [PDF](https://arxiv.org/pdf/2605.29268v2)

**Summary:** LLM-guided evolutionary search (Evolve systems) has reached state-of-the-art results on mathematical and combinatorial tasks, yet most existing systems report only the best of many runs and leave the run-to-run distribution undocumented. We ask how a fixed budget of LLM calls should be allocated, and how reliably a single run reaches the reported numbers. Sweeping the depth-breadth grid over five models and three tasks, we identify two empirical regularities: a fitness-compute envelope along whi...

---

### 45. Real-rootedness of the Poincaré polynomials of $\overline{\mathcal M}_{0,n}$: an AI-assisted proof

**Authors:** Gergely Bérczi, Young-Hoon Kiem

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.29151v1) | 📄 [PDF](https://arxiv.org/pdf/2605.29151v1)

**Summary:** We prove real-rootedness for the Poincaré polynomial \[   P_n(t)=\sum_{i=0}^{n-3} \dim H^{2i}(\overline{\mathcal M}_{0,n};\mathbb{Q})t^i \] of the Deligne--Mumford moduli space $\overline{\mathcal M}_{0,n}$ of stable $n$-pointed rational curves, proving a conjecture of Aluffi--Chen--Marcolli. The proof starts from the Keel--Manin--Getzler recurrence, but its main new idea is a bivariate deformation $F_m(y,t)$ of the Poincaré polynomial. This deformation reveals a hidden interlacing structure not...

---

### 46. Preference-Shaped Expected Hypervolume and R2 Improvement: Exact Computation and Monotonicity

**Authors:** Michael T. M. Emmerich

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28746v2) | 📄 [PDF](https://arxiv.org/pdf/2605.28746v2)

**Summary:** This paper studies preference-shaped expected improvement criteria for Bayesian multiobjective optimization. We consider two indicator families which are often used for similar algorithmic purposes, but which are geometrically different. The hypervolume indicator is based on a dystopian reference point and measures dominated volume in objective space. The R2 indicator is based on a utopian point and evaluates approximation sets through weighted Tchebycheff scalarization envelopes. The purpose of...

---

### 47. BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks

**Authors:** Tirtharaj Dash

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28739v1)

**Summary:** Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two f...

---

### 48. A Fresh Look at Lamarckian Evolution and the Baldwin Effect

**Authors:** Inès Benito, Johannes F. Lutzeyer, Benjamin Doerr

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28703v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28703v1)

**Summary:** Baldwinian and Lamarckian evolution have existed for a long time in evolutionary algorithms (EAs) without ever dominating the academic literature or practical applications. In this work, we use modern empirical and theoretical methods to revisit Lamarckian and Baldwinian evolution and rigorously compare them with the generic Darwinian evolution. On the empirical side, we run a comprehensive suite of experiments on graphs from six different datasets from the recent GraphBench benchmark on Maximum...

---

### 49. CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras

**Authors:** Elvin Hajizada, Michael Neumeier, Edward Paxon Frady, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28387v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28387v1)

**Summary:** Recognizing and continuously learning novel human actions without forgetting prior classes is a requirement for emerging AR/VR and robotics applications. For these applications, both on-device processing and learning are essential for privacy and low-latency adaptation. Event cameras address the efficiency of visual sensing with sparse, asynchronous output that is naturally compatible with neuromorphic processing. Yet no prior system has deployed a continual on-device learning pipeline for event...

---

### 50. Improving Evaluation of Recombination-based Cartesian Genetic Programming

**Authors:** Duy Long Tran, Anja Jankovic, Marie Anastacio, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28353v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28353v1)

**Summary:** Cartesian Genetic Programming has traditionally been using mutation as its main and often sole genetic operator to drive evolutionary search. Despite advancements in recent years, recombinationbased approaches have long been avoided, due to apparent lack of performance gains. This study examines two recently suggested recombination-based operators, subgraph crossover and discrete phenotypic recombination on SRBench, a benchmarking platform for symbolic regression. Using the implementations provi...

---

