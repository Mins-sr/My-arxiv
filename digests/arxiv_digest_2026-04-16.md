# arXiv Daily Digest - 2026-04-16

Total papers: 350

---

## cs.AI

**50 papers**

### 1. From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space

**Authors:** Yuqiao Tan, Minzheng Wang, Bo Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14142v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14142v1)

**Summary:** While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribu...

---

### 2. LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning

**Authors:** Sumeet Ramesh Motwani, Daniel Nichols, Charles London, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14140v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14140v1)

**Summary:** As language models are increasingly deployed for complex autonomous tasks, their ability to reason accurately over longer horizons becomes critical. An essential component of this ability is planning and managing a long, complex chain-of-thought (CoT). We introduce LongCoT, a scalable benchmark of 2,500 expert-designed problems spanning chemistry, mathematics, computer science, chess, and logic to isolate and directly measure the long-horizon CoT reasoning capabilities of frontier models. Proble...

---

### 3. From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs

**Authors:** Itay Itzhak, Eliya Habba, Gabriel Stanovsky, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14137v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14137v1)

**Summary:** Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empi...

---

### 4. Rhetorical Questions in LLM Representations: A Linear Probing Study

**Authors:** Louie Hong Yao, Vishesh Anand, Yuan Zhuang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14128v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14128v1)

**Summary:** Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, a...

---

### 5. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System

**Authors:** Tianshuo Yang, Guanyu Chen, Yutian Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14125v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14125v1)

**Summary:** While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs tas...

---

### 6. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

**Authors:** Zerun Ma, Guoqiang Wang, Xinchen Xie, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14116v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14116v1)

**Summary:** While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formula...

---

### 7. UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding

**Authors:** Fei Tang, Bofan Chen, Zhengxi Lu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14113v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14113v1)

**Summary:** GUI grounding, which localizes interface elements from screenshots given natural language queries, remains challenging for small icons and dense layouts. Test-time zoom-in methods improve localization by cropping and re-running inference at higher resolution, but apply cropping uniformly across all instances with fixed crop sizes, ignoring whether the model is actually uncertain on each case. We propose \textbf{UI-Zoomer}, a training-free adaptive zoom-in framework that treats both the trigger a...

---

### 8. UMI-3D: Extending Universal Manipulation Interface from Vision-Limited to 3D Spatial Perception

**Authors:** Ziming Wang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14089v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14089v1)

**Summary:** We present UMI-3D, a multimodal extension of the Universal Manipulation Interface (UMI) for robust and scalable data collection in embodied manipulation. While UMI enables portable, wrist-mounted data acquisition, its reliance on monocular visual SLAM makes it vulnerable to occlusions, dynamic scenes, and tracking failures, limiting its applicability in real-world environments. UMI-3D addresses these limitations by introducing a lightweight and low-cost LiDAR sensor tightly integrated into the w...

---

### 9. TIP: Token Importance in On-Policy Distillation

**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14084v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14084v1)

**Summary:** On-policy knowledge distillation (OPD) trains a student on its own rollouts under token-level supervision from a teacher. Not all token positions matter equally, but existing views of token importance are incomplete. We ask a direct question: which tokens carry the most useful learning signal in OPD? Our answer is that informative tokens come from two regions: positions with high student entropy, and positions with low student entropy plus high teacher--student divergence, where the student is o...

---

### 10. First-See-Then-Design: A Multi-Stakeholder View for Optimal Performance-Fairness Trade-Offs

**Authors:** Kavya Gupta, Nektarios Kalampalikis, Christoph Heitz, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14035v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14035v1)

**Summary:** Fairness in algorithmic decision-making is often defined in the predictive space, where predictive performance - used as a proxy for decision-maker (DM) utility - is traded off against prediction-based fairness notions, such as demographic parity or equality of opportunity. This perspective, however, ignores how predictions translate into decisions and ultimately into utilities and welfare for both DM and decision subjects (DS), as well as their allocation across social-salient groups.   In this...

---

### 11. Large Language Models to Enhance Business Process Modeling: Past, Present, and Future Trends

**Authors:** João Bettencourt, Sérgio Guerreiro

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14034v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14034v1)

**Summary:** Recent advances in Generative Artificial Intelligence, particularly Large Language Models (LLMs), have stimulated growing interest in automating or assisting Business Process Modeling tasks using natural language. Several approaches have been proposed to transform textual process descriptions into BPMN and related workflow models. However, the extent to which these approaches effectively support complex process modeling in organizational settings remains unclear. This article presents a literatu...

---

### 12. Hierarchical Reinforcement Learning with Runtime Safety Shielding for Power Grid Operation

**Authors:** Gitesh Malik

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14032v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14032v1)

**Summary:** Reinforcement learning has shown promise for automating power-grid operation tasks such as topology control and congestion management. However, its deployment in real-world power systems remains limited by strict safety requirements, brittleness under rare disturbances, and poor generalization to unseen grid topologies. In safety-critical infrastructure, catastrophic failures cannot be tolerated, and learning-based controllers must operate within hard physical constraints.   This paper proposes ...

---

### 13. Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective

**Authors:** Weijie Wang, Qihang Cao, Sensen Gao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14025v1)

**Summary:** Reconstructing 3D representations from 2D inputs is a fundamental task in computer vision and graphics, serving as a cornerstone for understanding and interacting with the physical world. While traditional methods achieve high fidelity, they are limited by slow per-scene optimization or category-specific training, which hinders their practical deployment and scalability. Hence, generalizable feed-forward 3D reconstruction has witnessed rapid development in recent years. By learning a model that ...

---

### 14. MAny: Merge Anything for Multimodal Continual Instruction Tuning

**Authors:** Zijian Gao, Wangwang Jia, Xingxing Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14016v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14016v1)

**Summary:** Multimodal Continual Instruction Tuning (MCIT) is essential for sequential task adaptation of Multimodal Large Language Models (MLLMs) but is severely restricted by catastrophic forgetting. While existing literature focuses on the reasoning language backbone, in this work, we expose a critical yet neglected dual-forgetting phenomenon across both perception drift in Cross-modal Projection Space and reasoning collapse in Low-rank Parameter Space. To resolve this, we present \textbf{MAny} (\textbf{...

---

### 15. Towards Multi-Object-Tracking with Radar on a Fast Moving Vehicle: On the Potential of Processing Radar in the Frequency Domain

**Authors:** Tim Hansen, Arturo Gomez-Chavez, Ilya Shimchik, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14013v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14013v1)

**Summary:** We promote in this paper the processing of radar data in the frequency domain to achieve higher robustness against noise and structural errors, especially in comparison to feature-based methods. This holds also for high dynamics in the scene, i.e., ego-motion of the vehicle with the sensor plus the presence of an unknown number of other moving objects. In addition to the high robustness, the processing in the frequency domain has the so far neglected advantage that the underlying correlation bas...

---

### 16. Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

**Authors:** Kangsan Kim, Minki Kang, Taeil Kim, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14004v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14004v1)

**Summary:** Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We e...

---

### 17. Diffusion Language Models for Speech Recognition

**Authors:** Davyd Naveriani, Albert Zeyer, Ralf Schlüter, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14001v1)

**Summary:** Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC...

---

### 18. Reward Design for Physical Reasoning in Vision-Language Models

**Authors:** Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13993v1)

**Summary:** Physical reasoning over visual inputs demands tight integration of visual perception, domain knowledge, and multi-step symbolic inference. Yet even state-of-the-art Vision Language Models (VLMs) fall far short of human performance on physics benchmarks. While post-training algorithms such as Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) have demonstrated strong reasoning gains in language models, how reward design shapes VLM physical reasoning behavior remains poorly...

---

### 19. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models

**Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13991v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13991v1)

**Summary:** Large language models (LLMs) are prone to generating factually incorrect outputs. Recent work has applied conformal prediction to provide uncertainty estimates and statistical guarantees for the factuality of LLM generations. However, existing approaches are typically not prompt-adaptive, limiting their ability to capture input-dependent variability. As a result, they may filter out too few items (leading to over-coverage) or too many (under-coverage) for a given task or prompt. We propose an ad...

---

### 20. Leveraging LLM-GNN Integration for Open-World Question Answering over Knowledge Graphs

**Authors:** Hussein Abdallah, Ibrahim Abdelaziz, Panos Kalnis, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13979v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13979v1)

**Summary:** Open-world Question Answering (OW-QA) over knowledge graphs (KGs) aims to answer questions over incomplete or evolving KGs. Traditional KGQA assumes a closed world where answers must exist in the KG, limiting real-world applicability. In contrast, open-world QA requires inferring missing knowledge based on graph structure and context. Large language models (LLMs) excel at language understanding but lack structured reasoning. Graph neural networks (GNNs) model graph topology but struggle with sem...

---

### 21. How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data

**Authors:** Joel Niklaus, Atsuki Yamaguchi, Michal Štefánik, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13977v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13977v1)

**Summary:** Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform...

---

### 22. [Emerging Ideas] Artificial Tripartite Intelligence: A Bio-Inspired, Sensor-First Architecture for Physical AI

**Authors:** You Rim Choi, Subeom Park, Hyung-Sin Kim

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13959v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13959v1)

**Summary:** As AI moves from data centers to robots and wearables, scaling ever-larger models becomes insufficient. Physical AI operates under tight latency, energy, privacy, and reliability constraints, and its performance depends not only on model capacity but also on how signals are acquired through controllable sensors in dynamic environments. We present Artificial Tripartite Intelligence (ATI), a bio-inspired, sensor-first architectural contract for physical AI. ATI is tripartite at the systems level: ...

---

### 23. Creo: From One-Shot Image Generation to Progressive, Co-Creative Ideation

**Authors:** Zoe De Simone, Angie Boggust, Fredo Durand, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13956v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13956v1)

**Summary:** Text-to-image (T2I) systems enable rapid generation of high-fidelity imagery but are misaligned with how visual ideas develop. T2I systems generate outputs that make implicit visual decisions on behalf of the user, often introduce fine-grained details that can anchor users prematurely and limit their ability to keep options open early on, and cause unintended changes during editing that are difficult to correct and reduce users' sense of control. To address these concerns, we present Creo, a mul...

---

### 24. HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark

**Authors:** Jiacheng Wang, Jinchang Hou, Fabian Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13954v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13954v1)

**Summary:** Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benc...

---

### 25. AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot

**Authors:** Joydeep Biswas, Sheila Schoepp, Gautham Vasan, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13940v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13940v1)

**Summary:** Scientific peer review faces mounting strain as submission volumes surge, making it increasingly difficult to sustain review quality, consistency, and timeliness. Recent advances in AI have led the community to consider its use in peer review, yet a key unresolved question is whether AI can generate technically sound reviews at real-world conference scale. Here we report the first large-scale field deployment of AI-assisted peer review: every main-track submission at AAAI-26 received one clearly...

---

### 26. ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection

**Authors:** Romain Hermary, Samet Hicsonmez, Dan Pineau, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13924v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13924v1)

**Summary:** Time-series anomaly detection (TSAD) is critical in domains such as industrial monitoring, healthcare, and cybersecurity, but it remains challenging due to rare and heterogeneous anomalies and the scarcity of labelled data. This scarcity makes unsupervised approaches predominant, yet existing methods often rely on reconstruction or forecasting, which struggle with complex data, or on embedding-based approaches that require domain-specific anomaly synthesis and fixed distance metrics. We propose ...

---

### 27. Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection

**Authors:** Ahmad Dawar Hakimi, Lea Hirlimann, Isabelle Augenstein, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13899v1)

**Summary:** Instruction-tuned LLMs can annotate thousands of instances from a short prompt at negligible cost. This raises two questions for active learning (AL): can LLM labels replace human labels within the AL loop, and does AL remain necessary when entire corpora can be labelled at once? We investigate both questions on a new dataset of 277,902 German political TikTok comments (25,974 LLM-labelled, 5,000 human-annotated), comparing seven annotation strategies across four encoders to detect anti-immigran...

---

### 28. Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning

**Authors:** Saeed Rahmani, Gözde Körpe,  Zhenlin, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13891v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13891v1)

**Summary:** Automated driving at unsignalized intersections is challenging due to complex multi-vehicle interactions and the need to balance safety and efficiency. Model Predictive Control (MPC) offers structured constraint handling through optimization but relies on hand-crafted rules that often produce overly conservative behavior. Deep Reinforcement Learning (RL) learns adaptive behaviors from experience but often struggles with safety assurance and generalization to unseen environments. In this study, w...

---

### 29. GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis

**Authors:** Bo Yu, Cheng Yang, Dongyang Hou, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13888v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13888v1)

**Summary:** The integration of Large Language Models (LLMs) into Geographic Information Systems (GIS) marks a paradigm shift toward autonomous spatial analysis. However, evaluating these LLM-based agents remains challenging due to the complex, multi-step nature of geospatial workflows. Existing benchmarks primarily rely on static text or code matching, neglecting dynamic runtime feedback and the multimodal nature of spatial outputs. To address this gap, we introduce GeoAgentBench (GABench), a dynamic and in...

---

### 30. Evaluating Supervised Machine Learning Models: Principles, Pitfalls, and Metric Selection

**Authors:** Xuanyan Liu, Ignacio Cabrera Martin, Marcello Trovati, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13882v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13882v1)

**Summary:** The evaluation of supervised machine learning models is a critical stage in the development of reliable predictive systems. Despite the widespread availability of machine learning libraries and automated workflows, model assessment is often reduced to the reporting of a small set of aggregate metrics, which can lead to misleading conclusions about real-world performance. This paper examines the principles, challenges, and practical considerations involved in evaluating supervised learning algori...

---

### 31. MCPThreatHive: Automated Threat Intelligence for Model Context Protocol Ecosystems

**Authors:** Yi Ting Shen, Kentaroh Toyoda, Alex Leung

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13849v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13849v1)

**Summary:** The rapid proliferation of Model Context Protocol (MCP)-based agentic systems has introduced a new category of security threats that existing frameworks are inadequately equipped to address. We present MCPThreatHive, an open-source platform that automates the end-to-end lifecycle of MCP threat intelligence: from continuous, multi-source data collection through AI-driven threat extraction and classification, to structured knowledge graph storage and interactive visualization. The platform operati...

---

### 32. SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention

**Authors:** Hongtao Xu, Jianchao Tan, Yuxuan Hu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13847v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13847v1)

**Summary:** While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy. Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems. Therefore, we propose SparseBalance, a novel algorithm-system co-...

---

### 33. Sentiment analysis for software engineering: How far can zero-shot learning (ZSL) go?

**Authors:** Reem Alfayez, Manal Binkhonain

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13826v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13826v1)

**Summary:** Sentiment analysis in software engineering focuses on understanding emotions expressed in software artifacts. Previous research highlighted the limitations of applying general off-the-shelf sentiment analysis tools within the software engineering domain and indicated the need for specialized tools tailored to various software engineering contexts. The development of such tools heavily relies on supervised machine learning techniques that necessitate annotated datasets. Acquiring such datasets is...

---

### 34. Cognitive Offloading in Agile Teams: How Artificial Intelligence Reshapes Risk Assessment and Planning Quality

**Authors:** Adriana Caraeni, Alexander Shick, Andrew Lan

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13814v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13814v1)

**Summary:** Recent advances in artificial intelligence (AI) have shown promise in automating key aspects of Agile project management, yet their impact on team cognition remains underexplored. In this work, we investigate cognitive offloading in Agile sprint planning by conducting a controlled, three-condition experiment comparing AI-only, human-only, and hybrid planning models on a live client deliverable at a mid-sized digital agency. Using quantitative metrics -- including estimation accuracy, rework rate...

---

### 35. AlphaCNOT: Learning CNOT Minimization with Model-Based Planning

**Authors:** Jacopo Cossio, Daniele Lizzio Bosco, Riccardo Romanello, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13812v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13812v1)

**Summary:** Quantum circuit optimization is a central task in Quantum Computing, as current Noisy Intermediate Scale Quantum devices suffer from error propagation that often scales with the number of operations. Among quantum operations, the CNOT gate is of fundamental importance, being the only 2-qubit gate in the universal Clifford+T set. The problem of CNOT gates minimization has been addressed by heuristic algorithms such as the well-known Patel-Markov-Hayes (PMH) for linear reversible synthesis (i.e., ...

---

### 36. Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation

**Authors:** Arya Shah, Vaibhav Tripathi, Mayank Singh, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13803v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13803v1)

**Summary:** Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 ope...

---

### 37. Soft $Q(λ)$: A multi-step off-policy method for entropy regularised reinforcement learning using eligibility traces

**Authors:** Pranav Mahajan, Ben Seymour

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13780v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13780v1)

**Summary:** Soft Q-learning has emerged as a versatile model-free method for entropy-regularised reinforcement learning, optimising for returns augmented with a penalty on the divergence from a reference policy. Despite its success, the multi-step extensions of soft Q-learning remain relatively unexplored and limited to on-policy action sampling under the Boltzmann policy. In this brief research note, we first present a formal $n$-step formulation for soft Q-learning and then extend this framework to the fu...

---

### 38. From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models

**Authors:** Wenxuan Li, Zhenfei Zhang, Mi Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13777v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13777v1)

**Summary:** Large language models (LLMs) may memorize sensitive or copyrighted content, raising significant privacy and legal concerns. While machine unlearning has emerged as a potential remedy, prevailing paradigms rely on user-provided forget sets, making unlearning requests difficult to audit and exposing systems to secondary leakage and malicious abuse. We propose MAGE, a Memory-grAph Guided Erasure framework for user-minimized, corpus-free unlearning. Given only a lightweight user anchor that identifi...

---

### 39. A Dynamic-Growing Fuzzy-Neuro Controller, Application to a 3PSP Parallel Robot

**Authors:** Mohsen Jalaeian-Farimani, Mohammad-R Akbarzadeh-T, Alireza Akbarzadeh, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13763v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13763v1)

**Summary:** To date, various paradigms of soft-Computing have been used to solve many modern problems. Among them, a self organizing combination of fuzzy systems and neural networks can make a powerful decision making system. Here, a Dynamic Growing Fuzzy Neural Controller (DGFNC) is combined with an adaptive strategy and applied to a 3PSP parallel robot position control problem. Specifically, the dynamic growing mechanism is considered in more detail. In contrast to other self-organizing methods, DGFNC add...

---

### 40. The cognitive companion: a lightweight parallel monitoring architecture for detecting and recovering from reasoning degradation in LLM agents

**Authors:** Rafflesia Khan, Nafiul Islam Khan

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13759v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13759v1)

**Summary:** Large language model (LLM) agents on multi-step tasks suffer reasoning degradation, looping, drift, stuck states, at rates up to 30% on hard tasks. Current solutions include hard step limits (abrupt) or LLM-as-judge monitoring (10-15% overhead per step). This paper introduces the Cognitive Companion, a parallel monitoring architecture with two implementations: an LLM-based Companion and a novel zero-overhead Probe-based Companion. We report a three-batch feasibility study centered on Gemma 4 E4B...

---

### 41. Rethinking AI Hardware: A Three-Layer Cognitive Architecture for Autonomous Agents

**Authors:** Li Chen

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13757v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13757v1)

**Summary:** The next generation of autonomous AI systems will be constrained not only by model capability, but by how intelligence is structured across heterogeneous hardware. Current paradigms -- cloud-centric AI, on-device inference, and edge-cloud pipelines -- treat planning, reasoning, and execution as a monolithic process, leading to unnecessary latency, energy consumption, and fragmented behavioral continuity. We introduce the Tri-Spirit Architecture, a three-layer cognitive framework that decomposes ...

---

### 42. TokenFormer: Unify the Multi-Field and Sequential Recommendation Worlds

**Authors:** Yifeng Zhou, Yuehong Hu, Zhixiang Feng, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13737v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13737v1)

**Summary:** Recommender systems have historically developed along two largely independent paradigms: feature interaction models for modeling correlations among multi-field categorical features, and sequential models for capturing user behavior dynamics from historical interaction sequences. Although recent trends attempt to bridge these paradigms within shared backbones, we empirically reveal that naive unifying these two branches may lead to a failure mode of Sequential Collapse Propagation (SCP). That is,...

---

### 43. Jump-Start Reinforcement Learning with Vision-Language-Action Regularization

**Authors:** Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13733v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13733v1)

**Summary:** Reinforcement learning (RL) enables high-frequency, closed-loop control for robotic manipulation, but scaling to long-horizon tasks with sparse or imperfect rewards remains difficult due to inefficient exploration and poor credit assignment. Vision-Language-Action (VLA) models leverage large-scale multimodal pretraining to provide generalist, task-level reasoning, but current limitations hinder their direct use in fast and precise manipulation. In this paper, we propose Vision-Language-Action Ju...

---

### 44. FRAGATA: Semantic Retrieval of HPC Support Tickets via Hybrid RAG over 20 Years of Request Tracker History

**Authors:** Santiago Paramés-Estévez, Nicolás Filloy-Montesino, Jorge Fernández-Fabeiro, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13721v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13721v1)

**Summary:** The technical support team of a supercomputing centre accumulates, over the course of decades, a large volume of resolved incidents that constitute critical operational knowledge. At the Galician Supercomputing Center (CESGA) this history has been managed for over twenty years with Request Tracker (RT), whose built-in search engine has significant limitations that hinder knowledge reuse by the support staff. This paper presents Fragata, a semantic ticket search system that combines modern inform...

---

### 45. Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

**Authors:** Yanfeng Shi, Pengfei Cai, Jun Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13715v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13715v1)

**Summary:** Large Audio-Language Models (LALMs) enable general audio understanding and demonstrate remarkable performance across various audio tasks. However, these models still face challenges in temporal perception (e.g., inferring event onset and offset), leading to limited utility in fine-grained scenarios. To address this issue, we propose Audio-Side Time Prompt and leverage Reinforcement Learning (RL) to develop the TimePro-RL framework for fine-grained temporal perception. Specifically, we encode tim...

---

### 46. Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration

**Authors:** Sayan Kumar Chaki, Antoine Gourru, Julien Velcin

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13705v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13705v1)

**Summary:** Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchange. We study this via a controlled hospital triage framework in which two agents negotiate over three structured debate rounds. One agent is aligned to a specific ethical framework via retrieval-augmented generation (RAG), while the other is either unaligned or adversarially prom...

---

### 47. MIND: AI Co-Scientist for Material Research

**Authors:** Geonhee Ahn, Donghyun Lee, Hayoung Doo, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13699v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13699v1)

**Summary:** Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven framework for automated hypothesis validation in materials research. MIND organizes the scientific discovery process into hypothesis refinement, experimentation, and debate-based validation within a multi-agent pipeline. For experimental verification, the system integrates Machi...

---

### 48. Med-CAM: Minimal Evidence for Explaining Medical Decision Making

**Authors:** Pirzada Suhail, Aditya Anand, Amit Sethi

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13695v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13695v1)

**Summary:** Reliable and interpretable decision-making is essential in medical imaging, where diagnostic outcomes directly influence patient care. Despite advances in deep learning, most medical AI systems operate as opaque black boxes, providing little insight into why a particular diagnosis was reached. In this paper, we introduce Med-CAM, a framework for generating minimal and sharp maps as evidence-based explanations for Medical decision making via Classifier Activation Matching. Med-CAM trains a segmen...

---

### 49. Weight Patching: Toward Source-Level Mechanistic Localization in LLMs

**Authors:** Chenghao Sun, Chengsheng Zhang, Guanzheng Qin, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13694v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13694v1)

**Summary:** Mechanistic interpretability seeks to localize model behavior to the internal components that causally realize it. Prior work has advanced activation-space localization and causal tracing, but modules that appear important in activation space may merely aggregate or amplify upstream signals rather than encode the target capability in their own parameters. To address this gap, we propose Weight Patching, a parameter-space intervention method for source-oriented analysis in paired same-architectur...

---

### 50. Beyond Voxel 3D Editing: Learning from 3D Masks and Self-Constructed Data

**Authors:** Yizhao Xu, Hongyuan Zhu, Caiyun Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13688v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13688v1)

**Summary:** 3D editing refers to the ability to apply local or global modifications to 3D assets. Effective 3D editing requires maintaining semantic consistency by performing localized changes according to prompts, while also preserving local invariance so that unchanged regions remain consistent with the original. However, existing approaches have significant limitations: multi-view editing methods incur losses when projecting back to 3D, while voxel-based editing is constrained in both the regions that ca...

---

## cs.CL

**50 papers**

### 1. SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments

**Authors:** Dinging Li, Yingxiu Zhao, Xinrui Cheng, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14144v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14144v1)

**Summary:** Spatial reasoning over three-dimensional scenes is a core capability for embodied intelligence, yet continuous model improvement remains bottlenecked by the cost of geometric annotation. The self-evolving paradigm offers a promising path, but its reliance on model consensus to construct pseudo-labels causes training to reinforce rather than correct the model's own geometric errors. We identify a property unique to 3D spatial reasoning that circumvents this limitation: ground truth is a determini...

---

### 2. From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space

**Authors:** Yuqiao Tan, Minzheng Wang, Bo Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14142v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14142v1)

**Summary:** While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribu...

---

### 3. From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs

**Authors:** Itay Itzhak, Eliya Habba, Gabriel Stanovsky, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14137v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14137v1)

**Summary:** Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empi...

---

### 4. Rhetorical Questions in LLM Representations: A Linear Probing Study

**Authors:** Louie Hong Yao, Vishesh Anand, Yuan Zhuang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14128v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14128v1)

**Summary:** Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, a...

---

### 5. Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis

**Authors:** Zipeng Ling, Shuliang Liu, Shenghong Fu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14121v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14121v1)

**Summary:** LLM reasoning traces suffer from complex flaws -- *Step Internal Flaws* (logical errors, hallucinations, etc.) and *Step-wise Flaws* (overthinking, underthinking), which vary by sample. A natural approach would be to provide ground-truth labels to guide LLMs' reasoning. Contrary to intuition, we show that this yields no improvement in reasoning ability. We then propose CRAFT, a unified framework that mitigates both types of Step flaws, which builds a Reasoning Knowledge Graph (RKG) based on the ...

---

### 6. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

**Authors:** Zerun Ma, Guoqiang Wang, Xinchen Xie, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14116v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14116v1)

**Summary:** While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formula...

---

### 7. UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding

**Authors:** Fei Tang, Bofan Chen, Zhengxi Lu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14113v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14113v1)

**Summary:** GUI grounding, which localizes interface elements from screenshots given natural language queries, remains challenging for small icons and dense layouts. Test-time zoom-in methods improve localization by cropping and re-running inference at higher resolution, but apply cropping uniformly across all instances with fixed crop sizes, ignoring whether the model is actually uncertain on each case. We propose \textbf{UI-Zoomer}, a training-free adaptive zoom-in framework that treats both the trigger a...

---

### 8. Interpretable Stylistic Variation in Human and LLM Writing Across Genres, Models, and Decoding Strategies

**Authors:** Swati Rallapalli, Shannon Gallagher, Ronald Yurko, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14111v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14111v1)

**Summary:** Large Language Models (LLMs) are now capable of generating highly fluent, human-like text. They enable many applications, but also raise concerns such as large scale spam, phishing, or academic misuse. While much work has focused on detecting LLM-generated text, only limited work has gone into understanding the stylistic differences between human-written and machine-generated text. In this work, we perform a large scale analysis of stylistic variation across human-written text and outputs from 1...

---

### 9. From Weights to Activations: Is Steering the Next Frontier of Adaptation?

**Authors:** Simon Ostermann, Daniil Gurgurov, Tanja Baeumel, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14090v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14090v1)

**Summary:** Post-training adaptation of language models is commonly achieved through parameter updates or input-based methods such as fine-tuning, parameter-efficient adaptation, and prompting. In parallel, a growing body of work modifies internal activations at inference time to influence model behavior, an approach known as steering. Despite increasing use, steering is rarely analyzed within the same conceptual framework as established adaptation methods.   In this work, we argue that steering should be r...

---

### 10. $π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

**Authors:** Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14054v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14054v1)

**Summary:** Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during t...

---

### 11. From Where Words Come: Efficient Regularization of Code Tokenizers Through Source Attribution

**Authors:** Pavel Chizhov, Egor Bogomolov, Ivan P. Yamshchikov

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14053v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14053v1)

**Summary:** Efficiency and safety of Large Language Models (LLMs), among other factors, rely on the quality of tokenization. A good tokenizer not only improves inference speed and language understanding but also provides extra defense against jailbreak attacks and lowers the risk of hallucinations. In this work, we investigate the efficiency of code tokenization, in particular from the perspective of data source diversity. We demonstrate that code tokenizers are prone to producing unused, and thus under-tra...

---

### 12. Dual-Enhancement Product Bundling: Bridging Interactive Graph and Large Language Model

**Authors:** Zhe Huang, Peng Wang, Yan Zheng, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14030v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14030v1)

**Summary:** Product bundling boosts e-commerce revenue by recommending complementary item combinations. However, existing methods face two critical challenges: (1) collaborative filtering approaches struggle with cold-start items owing to dependency on historical interactions, and (2) LLMs lack inherent capability to model interactive graph directly. To bridge this gap, we propose a dual-enhancement method that integrates interactive graph learning and LLM-based semantic understanding for product bundling. ...

---

### 13. Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning

**Authors:** Zekai Lin, Chao Xue, Di Liang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14010v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14010v1)

**Summary:** Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters during training. However, these methods represent a static solution to a dynamic problem, assuming that parameter importance remains fixed once identified. In this work, we empirically demonstrate that parameter importance exhibits temporal drift over the course of training. To address this, we propose...

---

### 14. Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

**Authors:** Kangsan Kim, Minki Kang, Taeil Kim, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14004v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14004v1)

**Summary:** Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We e...

---

### 15. Diffusion Language Models for Speech Recognition

**Authors:** Davyd Naveriani, Albert Zeyer, Ralf Schlüter, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14001v1)

**Summary:** Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC...

---

### 16. Reward Design for Physical Reasoning in Vision-Language Models

**Authors:** Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13993v1)

**Summary:** Physical reasoning over visual inputs demands tight integration of visual perception, domain knowledge, and multi-step symbolic inference. Yet even state-of-the-art Vision Language Models (VLMs) fall far short of human performance on physics benchmarks. While post-training algorithms such as Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) have demonstrated strong reasoning gains in language models, how reward design shapes VLM physical reasoning behavior remains poorly...

---

### 17. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models

**Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13991v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13991v1)

**Summary:** Large language models (LLMs) are prone to generating factually incorrect outputs. Recent work has applied conformal prediction to provide uncertainty estimates and statistical guarantees for the factuality of LLM generations. However, existing approaches are typically not prompt-adaptive, limiting their ability to capture input-dependent variability. As a result, they may filter out too few items (leading to over-coverage) or too many (under-coverage) for a given task or prompt. We propose an ad...

---

### 18. Leveraging LLM-GNN Integration for Open-World Question Answering over Knowledge Graphs

**Authors:** Hussein Abdallah, Ibrahim Abdelaziz, Panos Kalnis, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13979v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13979v1)

**Summary:** Open-world Question Answering (OW-QA) over knowledge graphs (KGs) aims to answer questions over incomplete or evolving KGs. Traditional KGQA assumes a closed world where answers must exist in the KG, limiting real-world applicability. In contrast, open-world QA requires inferring missing knowledge based on graph structure and context. Large language models (LLMs) excel at language understanding but lack structured reasoning. Graph neural networks (GNNs) model graph topology but struggle with sem...

---

### 19. How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data

**Authors:** Joel Niklaus, Atsuki Yamaguchi, Michal Štefánik, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13977v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13977v1)

**Summary:** Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform...

---

### 20. Causal Drawbridges: Characterizing Gradient Blocking of Syntactic Islands in Transformer LMs

**Authors:** Sasha Boguraev, Kyle Mahowald

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13950v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13950v1)

**Summary:** We show how causal interventions in Transformer models provide insights into English syntax by focusing on a long-standing challenge for syntactic theory: syntactic islands. Extraction from coordinated verb phrases is often degraded, yet acceptability varies gradiently with lexical content (e.g., "I know what he hates art and loves" vs. "I know what he looked down and saw"). We show that modern Transformer language models replicate human judgments across this gradient. Using causal interventions...

---

### 21. CollabCoder: Plan-Code Co-Evolution via Collaborative Decision-Making for Efficient Code Generation

**Authors:** Duy Tung Doan, Quang Huy Phung, Dzung Nguyen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13946v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13946v1)

**Summary:** Automated code generation remains a persistent challenge in software engineering, as conventional multi-agent frameworks are often constrained by static planning, isolated execution, high computational overhead, and limited adaptability to complex tasks. This paper introduces CollabCoder, a novel Plan-Code Co-Evolution framework that improves code generation through dynamic multi-agent collaboration. The core idea is to design a collaborative decision-making process between the plan module and t...

---

### 22. Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection

**Authors:** Ahmad Dawar Hakimi, Lea Hirlimann, Isabelle Augenstein, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13899v1)

**Summary:** Instruction-tuned LLMs can annotate thousands of instances from a short prompt at negligible cost. This raises two questions for active learning (AL): can LLM labels replace human labels within the AL loop, and does AL remain necessary when entire corpora can be labelled at once? We investigate both questions on a new dataset of 277,902 German political TikTok comments (25,974 LLM-labelled, 5,000 human-annotated), comparing seven annotation strategies across four encoders to detect anti-immigran...

---

### 23. Beyond Static Personas: Situational Personality Steering for Large Language Models

**Authors:** Zesheng Wei, Mengxiang Li, Zilei Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13846v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13846v1)

**Summary:** Personalized Large Language Models (LLMs) facilitate more natural, human-like interactions in human-centric applications. However, existing personalization methods are constrained by limited controllability and high resource demands. Furthermore, their reliance on static personality modeling restricts adaptability across varying situations. To address these limitations, we first demonstrate the existence of situation-dependency and consistent situation-behavior patterns within LLM personalities ...

---

### 24. Robust Reward Modeling for Large Language Models via Causal Decomposition

**Authors:** Yunsheng Lu, Zijiang Yang, Licheng Pan, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13833v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13833v1)

**Summary:** Reward models are central to aligning large language models, yet they often overfit to spurious cues such as response length and overly agreeable tone. Most prior work weakens these cues directly by penalizing or controlling specific artifacts, but it does not explicitly encourage the model to ground preferences in the prompt's intent. We learn a decoder that maps a candidate answer to the latent intent embedding of the input. The reconstruction error is used as a signal to regularize the reward...

---

### 25. MUSE: Multi-Domain Chinese User Simulation via Self-Evolving Profiles and Rubric-Guided Alignment

**Authors:** Zihao Liu, Hantao Zhou, Jiguo Li, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13828v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13828v1)

**Summary:** User simulators are essential for the scalable training and evaluation of interactive AI systems. However, existing approaches often rely on shallow user profiling, struggle to maintain persona consistency over long interactions, and are largely limited to English or single-domain settings. We present MUSE, a multi-domain Chinese user simulation framework designed to generate human-like, controllable, and behaviorally consistent responses. First, we propose Iterative Profile Self-Evolution (IPSE...

---

### 26. ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution

**Authors:** Shouzheng Huang, Meishan Zhang, Baotian Hu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13787v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13787v1)

**Summary:** Large Language Models (LLMs) enhance their problem-solving capability by utilizing external tools. However, in open-world scenarios with massive and evolving tool repositories, existing methods relying on static embedding retrieval or parameter memorization of tools struggle to align user intent with tool semantics or generalize to unseen tools, respectively, leading to suboptimal accuracy of open-world tool retrieval and execution. To address these, we present ToolOmni, a unified agentic framew...

---

### 27. QuantileMark: A Message-Symmetric Multi-bit Watermark for LLMs

**Authors:** Junlin Zhu, Baizhou Huang, Xiaojun Wan

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13786v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13786v1)

**Summary:** As large language models become standard backends for content generation, practical provenance increasingly requires multi-bit watermarking. In provider-internal deployments, a key requirement is message symmetry: the message itself should not systematically affect either text quality or verification outcomes. Vocabulary-partition watermarks can break message symmetry in low-entropy decoding: some messages are assigned most of the probability mass, while others are forced to use tail tokens. Thi...

---

### 28. From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models

**Authors:** Wenxuan Li, Zhenfei Zhang, Mi Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13777v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13777v1)

**Summary:** Large language models (LLMs) may memorize sensitive or copyrighted content, raising significant privacy and legal concerns. While machine unlearning has emerged as a potential remedy, prevailing paradigms rely on user-provided forget sets, making unlearning requests difficult to audit and exposing systems to secondary leakage and malicious abuse. We propose MAGE, a Memory-grAph Guided Erasure framework for user-minimized, corpus-free unlearning. Given only a lightweight user anchor that identifi...

---

### 29. Who Gets Flagged? The Pluralistic Evaluation Gap in AI Content Watermarking

**Authors:** Alexander Nemecek, Osama Zafar, Yuqiao Xu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13776v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13776v1)

**Summary:** Watermarking is becoming the default mechanism for AI content authentication, with governance policies and frameworks referencing it as infrastructure for content provenance. Yet across text, image, and audio modalities, watermark signal strength, detectability, and robustness depend on statistical properties of the content itself, properties that vary systematically across languages, cultural visual traditions, and demographic groups. We examine how this content dependence creates modality-spec...

---

### 30. MedRCube: A Multidimensional Framework for Fine-Grained and In-Depth Evaluation of MLLMs in Medical Imaging

**Authors:** Zhijie Bao, Fangke Chen, Licheng Bao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13756v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13756v1)

**Summary:** The potential of Multimodal Large Language Models (MLLMs) in domain of medical imaging raise the demands of systematic and rigorous evaluation frameworks that are aligned with the real-world medical imaging practice. Existing practices that report single or coarse-grained metrics are lack the granularity required for specialized clinical support and fail to assess the reliability of reasoning mechanisms. To address this, we propose a paradigm shift toward multidimensional, fine-grained and in-de...

---

### 31. Doc-V*:Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA

**Authors:** Yuanlei Zheng, Pei Fu, Hang Li, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13731v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13731v1)

**Summary:** Multi-page Document Visual Question Answering requires reasoning over semantics, layouts, and visual elements in long, visually dense documents. Existing OCR-free methods face a trade-off between capacity and precision: end-to-end models scale poorly with document length, while visual retrieval-based pipelines are brittle and passive. We propose Doc-$V^*$, an \textbf{OCR-free agentic} framework that casts multi-page DocVQA as sequential evidence aggregation. Doc-$V^*$ begins with a thumbnail ove...

---

### 32. Hybrid Retrieval for COVID-19 Literature: Comparing Rank Fusion and Projection Fusion with Diversity Reranking

**Authors:** Harishkumar Kishorkumar Prajapati

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13728v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13728v1)

**Summary:** We present a hybrid retrieval system for COVID-19 scientific literature, evaluated on the TREC-COVID benchmark (171,332 papers, 50 expert queries). The system implements six retrieval configurations spanning sparse (SPLADE), dense (BGE), rank-level fusion (RRF), and a projection-based vector fusion (B5) approach. RRF fusion achieves the best relevance (nDCG@10 = 0.828), outperforming dense-only by 6.1% and sparse-only by 14.9%. Our projection fusion variant reaches nDCG@10 = 0.678 on expert quer...

---

### 33. An Empirical Investigation of Practical LLM-as-a-Judge Improvement Techniques on RewardBench 2

**Authors:** Ryan Lail

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13717v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13717v1)

**Summary:** LLM-as-a-judge, using a language model to score or rank candidate responses, is widely used as a scalable alternative to human evaluation in RLHF pipelines, benchmarking, and application layer evaluations (evals). However, judgment reliability depends heavily on prompting and aggregation strategy. We present an empirical investigation of practical, drop-in techniques that improve GPT-5.4 judge accuracy on RewardBench 2 without any finetuning. Two techniques account for nearly all available gains...

---

### 34. Learning the Cue or Learning the Word? Analyzing Generalization in Metaphor Detection for Verbs

**Authors:** Sinan Kurtyigit, Sabine Schulte im Walde, Alexander Fraser

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13713v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13713v1)

**Summary:** Metaphor detection models achieve strong benchmark performance, yet it remains unclear whether this reflects transferable generalization or lexical memorization. To address this, we analyze generalization in metaphor detection through RoBERTa, the shared backbone of many state-of-the-art systems, focusing on English verbs using the VU Amsterdam Metaphor Corpus. We introduce a controlled lexical hold-out setup where all instances of selected target lemmas are strictly excluded from fine-tuning, a...

---

### 35. Co-FactChecker: A Framework for Human-AI Collaborative Claim Verification Using Large Reasoning Models

**Authors:** Dhruv Sahnan, Subhabrata Dutta, Tanmoy Chakraborty, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13706v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13706v1)

**Summary:** Professional fact-checkers rely on domain knowledge and deep contextual understanding to verify claims. Large language models (LLMs) and large reasoning models (LRMs) lack such grounding and primarily reason from available evidence alone, creating a mismatch between expert-led and fully automated claim verification. To mitigate this gap, we posit human-AI collaboration as a more promising path forward, where expert feedback, grounded in real-world knowledge and domain expertise, guides the model...

---

### 36. Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration

**Authors:** Sayan Kumar Chaki, Antoine Gourru, Julien Velcin

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13705v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13705v1)

**Summary:** Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchange. We study this via a controlled hospital triage framework in which two agents negotiate over three structured debate rounds. One agent is aligned to a specific ethical framework via retrieval-augmented generation (RAG), while the other is either unaligned or adversarially prom...

---

### 37. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection

**Authors:** Xiao Pu, Zepeng Cheng, Lin Yuan, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13692v1)

**Summary:** As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues that distinguish AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts. This generalizes unseen generators as a central and challenging problem for AI-text detection. To tackle this challenge, we propose a progressiv...

---

### 38. IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages

**Authors:** Aviral Dawar, Roshan Karanth, Vikram Goyal, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13686v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13686v1)

**Summary:** While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced from open-data platforms, including the National Data and Analytics Platform (NDAP) and the India Data ...

---

### 39. Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference

**Authors:** Xuwen Zhou, Fangxin Liu, Chao Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13634v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13634v1)

**Summary:** Speculative decoding accelerates autoregressive generation by letting draft tokens bypass full verification, but conventional frameworks suffer from frequent false rejections, particularly when draft models produce semantically correct but lexically divergent outputs. In this paper, we present Calibrated Speculative Decoding (CSD), a training-free framework that recovers valid tokens discarded by standard verification. Guided by the principle of "Frequency-Guided Candidate Selection and Probabil...

---

### 40. (How) Learning Rates Regulate Catastrophic Overtraining

**Authors:** Mark Rofin, Aditya Varre, Nicolas Flammarion

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13627v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13627v1)

**Summary:** Supervised fine-tuning (SFT) is a common first stage of LLM post-training, teaching the model to follow instructions and shaping its behavior as a helpful assistant. At the same time, SFT may harm the fundamental capabilities of an LLM, particularly after long pretraining: a phenomenon known as catastrophic overtraining (Springer et al., 2025). To understand overtraining, we first investigate catastrophic forgetting in finetuning through the lens of implicit regularization of the learning rate. ...

---

### 41. Syn-TurnTurk: A Synthetic Dataset for Turn-Taking Prediction in Turkish Dialogues

**Authors:** Ahmet Tuğrul Bayrak, Mustafa Sertaç Türkel, Fatma Nur Korkmaz

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13620v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13620v1)

**Summary:** Managing natural dialogue timing is a significant challenge for voice-based chatbots. Most current systems usually rely on simple silence detection, which often fails because human speech patterns involve irregular pauses. This causes bots to interrupt users, breaking the conversational flow. This problem is even more severe for languages like Turkish, which lack high-quality datasets for turn-taking prediction. This paper introduces Syn-TurnTurk, a synthetic Turkish dialogue dataset generated u...

---

### 42. C2: Scalable Rubric-Augmented Reward Modeling from Binary Preferences

**Authors:** Akira Kawabata, Saku Sugawara

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13618v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13618v1)

**Summary:** Rubric-augmented verification guides reward models with explicit evaluation criteria, yielding more reliable judgments than single-model verification. However, most existing methods require costly rubric annotations, limiting scalability. Moreover, we find that rubric generation is vulnerable to a failure of cooperation; low-quality rubrics actively mislead reward models rather than help. Inspired by the principle of cooperative communication, we propose Cooperative yet Critical reward modeling ...

---

### 43. Foresight Optimization for Strategic Reasoning in Large Language Models

**Authors:** Jiashuo Wang, Jiawen Duan, Jian Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13592v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13592v1)

**Summary:** Reasoning capabilities in large language models (LLMs) have generally advanced significantly. However, it is still challenging for existing reasoning-based LLMs to perform effective decision-making abilities in multi-agent environments, due to the absence of explicit foresight modeling. To this end, strategic reasoning, the most fundamental capability to anticipate the counterpart's behaviors and foresee its possible future actions, has been introduced to alleviate the above issues. Strategic re...

---

### 44. BenGER: A Collaborative Web Platform for End-to-End Benchmarking of German Legal Tasks

**Authors:** Sebastian Nagl, Matthias Grabmair

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13583v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13583v1)

**Summary:** Evaluating large language models (LLMs) for legal reasoning requires workflows that span task design, expert annotation, model execution, and metric-based evaluation. In practice, these steps are split across platforms and scripts, limiting transparency, reproducibility, and participation by non-technical legal experts. We present the BenGER (Benchmark for German Law) framework, an open-source web platform that integrates task creation, collaborative annotation, configurable LLM runs, and evalua...

---

### 45. MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning

**Authors:** Jiahang Lin, Kai Hu, Binghai Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13579v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13579v1)

**Summary:** Conventional Retrieval-Augmented Generation (RAG) systems often struggle with complex multi-hop queries over long documents due to their single-pass retrieval. We introduce MM-Doc-R1, a novel framework that employs an agentic, vision-aware workflow to address long document visual question answering through iterative information discovery and synthesis. To incentivize the information seeking capabilities of our agents, we propose Similarity-based Policy Optimization (SPO), addressing baseline est...

---

### 46. YOCO++: Enhancing YOCO with KV Residual Connections for Efficient LLM Inference

**Authors:** You Wu, Ziheng Chen, Yizhen Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13556v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13556v1)

**Summary:** Cross-layer key-value (KV) compression has been found to be effective in efficient inference of large language models (LLMs). Although they reduce the memory consumption of the KV cache, such methods usually introduce non-negligible performance degradation. In this work, we aim to enhance the performance of YOCO, a cross-layer KV compression method that shares the KVs of the middle layer with the top-half layers. We propose YOCO++, an enhanced YOCO that incorporates a weighted residual connectio...

---

### 47. Training-Free Test-Time Contrastive Learning for Large Language Models

**Authors:** Kaiwen Zheng, Kai Zhou, Jinwu Hu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13552v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13552v1)

**Summary:** Large language models (LLMs) demonstrate strong reasoning capabilities, but their performance often degrades under distribution shift. Existing test-time adaptation (TTA) methods rely on gradient-based updates that require white-box access and need substantial overhead, while training-free alternatives are either static or depend on external guidance. In this paper, we propose Training-Free Test-Time Contrastive Learning TF-TTCL, a training-free adaptation framework that enables a frozen LLM to ...

---

### 48. Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate

**Authors:** Cunda Wang, Ziying Ma, Po Hu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13551v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13551v1)

**Summary:** Entity alignment (EA) aims to identify entities referring to the same real-world object across different knowledge graphs (KGs). Recent approaches based on large language models (LLMs) typically obtain entity embeddings through knowledge representation learning and use embedding similarity to identify an alignment-uncertain entity set. For each uncertain entity, a candidate entity set (CES) is then retrieved based on embedding similarity to support subsequent alignment reasoning and decision mak...

---

### 49. Synthesizing Instruction-Tuning Datasets with Contrastive Decoding

**Authors:** Tatsuya Ichinose, Youmi Ma, Masanari Oi, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13538v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13538v1)

**Summary:** Using responses generated by high-performing large language models (LLMs) for instruction tuning has become a widely adopted approach. However, the existing literature overlooks a property of LLM-generated responses: they conflate world knowledge acquired during pre-training with instruction-following capabilities acquired during post-training. We hypothesize that disentangling the instruction-following capabilities from pre-trained knowledge improves the effectiveness of instruction tuning. To ...

---

### 50. ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding

**Authors:** Heming Xia, Yongqi Li, Cunxiao Du, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13519v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13519v1)

**Summary:** Tool calling has greatly expanded the practical utility of large language models (LLMs) by enabling them to interact with external applications. As LLM capabilities advance, effective tool use increasingly involves multi-step, multi-turn interactions to solve complex tasks. However, the resulting growth in tool interactions incurs substantial latency, posing a key challenge for real-time LLM serving. Through empirical analysis, we find that tool-calling traces are highly structured, conform to c...

---

## cs.CV

**50 papers**

### 1. One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding

**Authors:** Zheyu Zhang, Ziqi Pang, Shixing Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14149v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14149v1)

**Summary:** Long video understanding is inherently challenging for vision-language models (VLMs) because of the extensive number of frames. With each video frame typically expanding into tens or hundreds of tokens, the limited context length of large language models (LLMs) forces the VLMs to perceive the frames sparsely and lose temporal information. To address this, we explore extreme video token compression towards \emph{one token per frame} at the final LLM layer. Our key insight is that heuristic-based ...

---

### 2. Seedance 2.0: Advancing Video Generation for World Complexity

**Authors:** Team Seedance, De Chen, Liyang Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14148v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14148v1)

**Summary:** Seedance 2.0 is a new native multi-modal audio-video generation model, officially released in China in early February 2026. Compared with its predecessors, Seedance 1.0 and 1.5 Pro, Seedance 2.0 adopts a unified, highly efficient, and large-scale architecture for multi-modal audio-video joint generation. This allows it to support four input modalities: text, image, audio, and video, by integrating one of the most comprehensive suites of multi-modal content reference and editing capabilities avai...

---

### 3. ROSE: Retrieval-Oriented Segmentation Enhancement

**Authors:** Song Tang, Guangquan Jie, Henghui Ding, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14147v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14147v1)

**Summary:** Existing segmentation models based on multimodal large language models (MLLMs), such as LISA, often struggle with novel or emerging entities due to their inability to incorporate up-to-date knowledge. To address this challenge, we introduce the Novel Emerging Segmentation Task (NEST), which focuses on segmenting (i) novel entities that MLLMs fail to recognize due to their absence from training data, and (ii) emerging entities that exist within the model's knowledge but demand up-to-date external...

---

### 4. SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments

**Authors:** Dinging Li, Yingxiu Zhao, Xinrui Cheng, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14144v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14144v1)

**Summary:** Spatial reasoning over three-dimensional scenes is a core capability for embodied intelligence, yet continuous model improvement remains bottlenecked by the cost of geometric annotation. The self-evolving paradigm offers a promising path, but its reliance on model consensus to construct pseudo-labels causes training to reinforce rather than correct the model's own geometric errors. We identify a property unique to 3D spatial reasoning that circumvents this limitation: ground truth is a determini...

---

### 5. Geometric Context Transformer for Streaming 3D Reconstruction

**Authors:** Lin-Zhuo Chen, Jian Gao, Yihang Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14141v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14141v1)

**Summary:** Streaming 3D reconstruction aims to recover 3D information, such as camera poses and point clouds, from a video stream, which necessitates geometric accuracy, temporal   consistency, and computational efficiency. Motivated by the principles of Simultaneous Localization and Mapping (SLAM), we introduce LingBot-Map, a feed-forward 3D foundation   model for reconstructing scenes from streaming data, built upon a geometric context transformer (GCT) architecture. A defining aspect of LingBot-Map lies...

---

### 6. Don't Let the Video Speak: Audio-Contrastive Preference Optimization for Audio-Visual Language Models

**Authors:** Ami Baid, Zihui Xue, Kristen Grauman

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14129v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14129v1)

**Summary:** While Audio-Visual Language Models (AVLMs) have achieved remarkable progress over recent years, their reliability is bottlenecked by cross-modal hallucination. A particularly pervasive manifestation is video-driven audio hallucination: models routinely exploit visual shortcuts to hallucinate expected sounds, discarding true auditory evidence. To counteract this deeply ingrained visual dominance, we propose Audio-Contrastive Preference Optimization (ACPO). This dual-axis preference learning frame...

---

### 7. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System

**Authors:** Tianshuo Yang, Guanyu Chen, Yutian Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14125v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14125v1)

**Summary:** While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs tas...

---

### 8. UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding

**Authors:** Fei Tang, Bofan Chen, Zhengxi Lu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14113v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14113v1)

**Summary:** GUI grounding, which localizes interface elements from screenshots given natural language queries, remains challenging for small icons and dense layouts. Test-time zoom-in methods improve localization by cropping and re-running inference at higher resolution, but apply cropping uniformly across all instances with fixed crop sizes, ignoring whether the model is actually uncertain on each case. We propose \textbf{UI-Zoomer}, a training-free adaptive zoom-in framework that treats both the trigger a...

---

### 9. Training-Free Semantic Multi-Object Tracking with Vision-Language Models

**Authors:** Laurence Bonat, Francesco Tonini, Elisa Ricci, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14074v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14074v1)

**Summary:** Semantic Multi-Object Tracking (SMOT) extends multi-object tracking with semantic outputs such as video summaries, instance-level captions, and interaction labels, aiming to move from trajectories to human-interpretable descriptions of dynamic scenes. Existing SMOT systems are trained end-to-end, coupling progress to expensive supervision, limiting the ability to rapidly adapt to new foundation models and new interactions. We propose TF-SMOT, a training-free SMOT pipeline that composes pretraine...

---

### 10. Towards Unconstrained Human-Object Interaction

**Authors:** Francesco Tonini, Alessandro Conti, Lorenzo Vaquero, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14069v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14069v1)

**Summary:** Human-Object Interaction (HOI) detection is a longstanding computer vision problem concerned with predicting the interaction between humans and objects. Current HOI models rely on a vocabulary of interactions at training and inference time, limiting their applicability to static environments. With the advent of Multimodal Large Language Models (MLLMs), it has become feasible to explore more flexible paradigms for interaction recognition. In this work, we revisit HOI detection through the lens of...

---

### 11. OneHOI: Unifying Human-Object Interaction Generation and Editing

**Authors:** Jiun Tian Hoe, Weipeng Hu, Xudong Jiang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14062v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14062v1)

**Summary:** Human-Object Interaction (HOI) modelling captures how humans act upon and relate to objects, typically expressed as <person, action, object> triplets. Existing approaches split into two disjoint families: HOI generation synthesises scenes from structured triplets and layout, but fails to integrate mixed conditions like HOI and object-only entities; and HOI editing modifies interactions via text, yet struggles to decouple pose from physical contact and scale to multiple interactions. We introduce...

---

### 12. Free Geometry: Refining 3D Reconstruction from Longer Versions of Itself

**Authors:** Yuhang Dai, Xingyi Yang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14048v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14048v1)

**Summary:** Feed-forward 3D reconstruction models are efficient but rigid: once trained, they perform inference in a zero-shot manner and cannot adapt to the test scene. As a result, visually plausible reconstructions often contain errors, particularly under occlusions, specularities, and ambiguous cues. To address this, we introduce Free Geometry, a framework that enables feed-forward 3D reconstruction models to self-evolve at test time without any 3D ground truth. Our key insight is that, when the model r...

---

### 13. Decoding the Delta: Unifying Remote Sensing Change Detection and Understanding with Multimodal Large Language Models

**Authors:** Xiaohe Li, Jiahao Li, Kaixin Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14044v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14044v1)

**Summary:** While Multimodal Large Language Models (MLLMs) excel in general vision-language tasks, their application to remote sensing change understanding is hindered by a fundamental "temporal blindness". Existing architectures lack intrinsic mechanisms for multi-temporal contrastive reasoning and struggle with precise spatial grounding. To address this, we first introduce Delta-QA, a comprehensive benchmark comprising 180k visual question-answering samples. Delta-QA unifies pixel-level segmentation and v...

---

### 14. Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios

**Authors:** Xiaomin Li, Tala Wang, Zichen Zhong, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14041v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14041v1)

**Summary:** Daily scenarios are characterized by visual richness, requiring Multimodal Large Language Models (MLLMs) to filter noise and identify decisive visual clues for accurate reasoning. Yet, current benchmarks predominantly aim at evaluating MLLMs' pre-existing knowledge or perceptual understanding, often neglecting the critical capability of reasoning. To bridge this gap, we introduce DailyClue, a benchmark designed for visual clue-driven reasoning in daily scenarios. Our construction is guided by tw...

---

### 15. POINTS-Seeker: Towards Training a Multimodal Agentic Search Model from Scratch

**Authors:** Yikun Liu, Yuan Liu, Le Tian, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14029v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14029v1)

**Summary:** While Large Multimodal Models (LMMs) demonstrate impressive visual perception, they remain epistemically constrained by their static parametric knowledge. To transcend these boundaries, multimodal search models have been adopted to actively interact with the external environment for evidence retrieval. Diverging from prevailing paradigms that merely retrofit general LMMs with search tools as modular extensions, we explore the potential of building a multimodal agentic search model from scratch. ...

---

### 16. Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective

**Authors:** Weijie Wang, Qihang Cao, Sensen Gao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14025v1)

**Summary:** Reconstructing 3D representations from 2D inputs is a fundamental task in computer vision and graphics, serving as a cornerstone for understanding and interacting with the physical world. While traditional methods achieve high fidelity, they are limited by slow per-scene optimization or category-specific training, which hinders their practical deployment and scalability. Hence, generalizable feed-forward 3D reconstruction has witnessed rapid development in recent years. By learning a model that ...

---

### 17. Towards Multi-Object-Tracking with Radar on a Fast Moving Vehicle: On the Potential of Processing Radar in the Frequency Domain

**Authors:** Tim Hansen, Arturo Gomez-Chavez, Ilya Shimchik, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14013v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14013v1)

**Summary:** We promote in this paper the processing of radar data in the frequency domain to achieve higher robustness against noise and structural errors, especially in comparison to feature-based methods. This holds also for high dynamics in the scene, i.e., ego-motion of the vehicle with the sensor plus the presence of an unknown number of other moving objects. In addition to the high robustness, the processing in the frequency domain has the so far neglected advantage that the underlying correlation bas...

---

### 18. Depth-Aware Image and Video Orientation Estimation

**Authors:** Muhammad Z. Alam, Larry Stetsiuk, M. Umair Mukati, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13995v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13995v1)

**Summary:** This paper introduces a novel approach for image and video orientation estimation by leveraging depth distribution in natural images. The proposed method estimates the orientation based on the depth distribution across different quadrants of the image, providing a robust framework for orientation estimation suited for applications such as virtual reality (VR), augmented reality (AR), autonomous navigation, and interactive surveillance systems. To further enhance fine-scale perceptual alignment, ...

---

### 19. Remote Sensing Image Super-Resolution for Imbalanced Textures: A Texture-Aware Diffusion Framework

**Authors:** Enzhuo Zhang, Sijie Zhao, Dilxat Muhtar, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13994v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13994v1)

**Summary:** Generative diffusion priors have recently achieved state-of-the-art performance in natural image super-resolution, demonstrating a powerful capability to synthesize photorealistic details. However, their direct application to remote sensing image super-resolution (RSISR) reveals significant shortcomings. Unlike natural images, remote sensing images exhibit a unique texture distribution where ground objects are globally stochastic yet locally clustered, leading to highly imbalanced textures. This...

---

### 20. Reward Design for Physical Reasoning in Vision-Language Models

**Authors:** Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13993v1)

**Summary:** Physical reasoning over visual inputs demands tight integration of visual perception, domain knowledge, and multi-step symbolic inference. Yet even state-of-the-art Vision Language Models (VLMs) fall far short of human performance on physics benchmarks. While post-training algorithms such as Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) have demonstrated strong reasoning gains in language models, how reward design shapes VLM physical reasoning behavior remains poorly...

---

### 21. HiProto: Hierarchical Prototype Learning for Interpretable Object Detection Under Low-quality Conditions

**Authors:** Jianlin Xiang, Linhui Dai, Xue Yang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13981v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13981v1)

**Summary:** Interpretability is essential for deploying object detection systems in critical applications, especially under low-quality imaging conditions that degrade visual information and increase prediction uncertainty. Existing methods either enhance image quality or design complex architectures, but often lack interpretability and fail to improve semantic discrimination. In contrast, prototype learning enables interpretable modeling by associating features with class-centered semantics, which can prov...

---

### 22. MApLe: Multi-instance Alignment of Diagnostic Reports and Large Medical Images

**Authors:** Felicia Bader, Philipp Seeböck, Anastasia Bartashova, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13970v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13970v1)

**Summary:** In diagnostic reports, experts encode complex imaging data into clinically actionable information. They describe subtle pathological findings that are meaningful in their anatomical context. Reports follow relatively consistent structures, expressing diagnostic information with few words that are often associated with tiny but consequential image observations. Standard vision language models struggle to identify the associations between these informative text components and small locations in th...

---

### 23. Creo: From One-Shot Image Generation to Progressive, Co-Creative Ideation

**Authors:** Zoe De Simone, Angie Boggust, Fredo Durand, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13956v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13956v1)

**Summary:** Text-to-image (T2I) systems enable rapid generation of high-fidelity imagery but are misaligned with how visual ideas develop. T2I systems generate outputs that make implicit visual decisions on behalf of the user, often introduce fine-grained details that can anchor users prematurely and limit their ability to keep options open early on, and cause unintended changes during editing that are difficult to correct and reduce users' sense of control. To address these concerns, we present Creo, a mul...

---

### 24. Heuristic Style Transfer for Real-Time, Efficient Weather Attribute Detection

**Authors:** Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13947v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13947v1)

**Summary:** We present lightweight and efficient architectures to detect weather conditions from RGB images, predicting the weather type (sunny, rain, snow, fog) and 11 complementary attributes such as intensity, visibility, and ground condition, for a total of 53 classes across the tasks. This work examines to what extent weather conditions manifest as variations in visual style. We investigate style-inspired techniques, including Gram matrices, a truncated ResNet-50 targeting lower and intermediate layers...

---

### 25. SceneGlue: Scene-Aware Transformer for Feature Matching without Scene-Level Annotation

**Authors:** Songlin Du, Xiaoyong Lu, Yaping Yan, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13941v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13941v1)

**Summary:** Local feature matching plays a critical role in understanding the correspondence between cross-view images. However, traditional methods are constrained by the inherent local nature of feature descriptors, limiting their ability to capture non-local scene information that is essential for accurate cross-view correspondence. In this paper, we introduce SceneGlue, a scene-aware feature matching framework designed to overcome these limitations. SceneGlue leverages a hybridizable matching paradigm t...

---

### 26. A Multi-Stage Optimization Pipeline for Bethesda Cell Detection in Pap Smear Cytology

**Authors:** Martin Amster, Camila María Polotto

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13939v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13939v1)

**Summary:** Computer vision techniques have advanced significantly in recent years, finding diverse and impactful applications within the medical field. In this paper, we introduce a new framework for the detection of Bethesda cells in Pap smear images, developed for Track B of the Riva Cytology Challenge held in association with the International Symposium on Biomedical Imaging (ISBI). This work focuses on enhancing computer vision models for cell detection, with performance evaluated using the mAP50-95 me...

---

### 27. ASTRA: Enhancing Multi-Subject Generation with Retrieval-Augmented Pose Guidance and Disentangled Position Embedding

**Authors:** Tianze Xia, Zijian Ning, Zonglin Zhao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13938v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13938v1)

**Summary:** Subject-driven image generation has shown great success in creating personalized content, but its capabilities are largely confined to single subjects in common poses. Current approaches face a fundamental conflict when handling multiple subjects with complex, distinct actions: preserving individual identities while enforcing precise pose structures. This challenge often leads to identity fusion and pose distortion, as appearance and structure signals become entangled within the model's architec...

---

### 28. ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection

**Authors:** Romain Hermary, Samet Hicsonmez, Dan Pineau, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13924v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13924v1)

**Summary:** Time-series anomaly detection (TSAD) is critical in domains such as industrial monitoring, healthcare, and cybersecurity, but it remains challenging due to rare and heterogeneous anomalies and the scarcity of labelled data. This scarcity makes unsupervised approaches predominant, yet existing methods often rely on reconstruction or forecasting, which struggle with complex data, or on embedding-based approaches that require domain-specific anomaly synthesis and fixed distance metrics. We propose ...

---

### 29. PartNerFace: Part-based Neural Radiance Fields for Animatable Facial Avatar Reconstruction

**Authors:** Xianggang Yu, Lingteng Qiu, Xiaohang Ren, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13918v1)

**Summary:** We present PartNerFace, a part-based neural radiance fields approach, for reconstructing animatable facial avatar from monocular RGB videos. Existing solutions either simply condition the implicit network with the morphable model parameters or learn an imaginary canonical radiance field, making them fail to generalize to unseen facial expressions and capture fine-scale motion details. To address these challenges, we first apply inverse skinning based on a parametric head model to map an observed...

---

### 30. Blind Bitstream-corrupted Video Recovery via Metadata-guided Diffusion Model

**Authors:** Shuyun Wang, Hu Zhang, Xin Shen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13906v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13906v1)

**Summary:** Bitstream-corrupted video recovery aims to restore realistic content degraded during video storage or transmission. Existing methods typically assume that predefined masks of corrupted regions are available, but manually annotating these masks is labor-intensive and impractical in real-world scenarios. To address this limitation, we introduce a new blind video recovery setting that removes the reliance on predefined masks. This setting presents two major challenges: accurately identifying corrup...

---

### 31. Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias

**Authors:** Zhiyuan Xu, Jiuming Liu, Yuxin Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13905v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13905v1)

**Summary:** We present SparseGen, a novel framework for efficient image-to-3D generation, which exhibits low input-view bias while being significantly faster. Unlike traditional approaches that rely on dense volumetric grids, triplanes, or pixel-aligned primitives, we model scenes with a compact sparse set of learned 3D anchor queries and a learned expansion operator that decodes each transformed query into a small local set of 3D Gaussian primitives. Trained under a rectified-flow reconstruction objective ...

---

### 32. Context Sensitivity Improves Human-Machine Visual Alignment

**Authors:** Frieda Born, Tom Neuhäuser, Lukas Muttenthaler, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13883v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13883v1)

**Summary:** Modern machine learning models typically represent inputs as fixed points in a high-dimensional embedding space. While this approach has been proven powerful for a wide range of downstream tasks, it fundamentally differs from the way humans process information. Because humans are constantly adapting to their environment, they represent objects and their relationships in a highly context-sensitive manner. To address this gap, we propose a method for context-sensitive similarity computation from n...

---

### 33. PostureObjectstitch: Anomaly Image Generation Considering Assembly Relationships in Industrial Scenarios

**Authors:** Zebei Tong, Hongchang Chen, Yujie Lei, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13863v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13863v1)

**Summary:** Image generation technology can synthesize condition-specific images to supplement real-world industrial anomaly data and enhance anomaly detection model performance. Existing generation techniques rarely account for the pose and orientation of industrial components in assembly, making the generated images difficult to utilize for downstream application. To solve this, we propose a novel image synthesis approach, called PostureObjectStitch, that achieves accurate generation to meet the requireme...

---

### 34. Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image

**Authors:** Yujie Gao, Yao Xiao, Xiangnan Zhu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13856v1)

**Summary:** Reconstructing a complete 3D head from a single portrait remains challenging because existing methods still face a sharp quality-speed trade-off: high-fidelity pipelines often rely on multi-stage processing and per-subject optimization, while fast feed-forward models struggle with complete geometry and fine appearance details. To bridge this gap, we propose Any3DAvatar, a fast and high-quality method for single-image 3D Gaussian head avatar generation, whose fastest setting reconstructs a full h...

---

### 35. DiffMagicFace: Identity Consistent Facial Editing of Real Videos

**Authors:** Huanghao Yin, Shenkun Xu, Kanle Shi, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13841v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13841v1)

**Summary:** Text-conditioned image editing has greatly benefitted from the advancements in Image Diffusion Models. However, extending these techniques to facial video editing introduces challenges in preserving facial identity throughout the source video and ensuring consistency of the edited subject across frames. In this paper, we introduce DiffMagicFace, a unique video editing framework that integrates two fine-tuned models for text and image control. These models operate concurrently during inference to...

---

### 36. A Resource-Efficient Hybrid CNN-LSTM network for image-based bean leaf disease classification

**Authors:** Hye Jin Rhee, Joseph Damilola Akinyemi

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13835v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13835v1)

**Summary:** Accurate and resource-efficient automated diagnosis is a cornerstone of modern agricultural expert systems. While Convolutional Neural Networks (CNNs) have established benchmarks in plant pathology, their ability to capture long-range spatial dependencies is often limited by standard pooling layers, and their high memory footprint hinders deployment on portable devices. This paper proposes a lightweight hybrid CNN-LSTM system for bean leaf disease classification. By integrating an LSTM layer to ...

---

### 37. Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation

**Authors:** Arya Shah, Vaibhav Tripathi, Mayank Singh, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13803v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13803v1)

**Summary:** Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 ope...

---

### 38. DRG-Font: Dynamic Reference-Guided Few-shot Font Generation via Contrastive Style-Content Disentanglement

**Authors:** Rejoy Chakraborty, Prasun Roy, Saumik Bhattacharya, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13797v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13797v1)

**Summary:** Few-shot Font Generation aims to generate stylistically consistent glyphs from a few reference glyphs. However, capturing complex font styles from a few exemplars remains challenging, and the existing methods often struggle to retain discernible local characteristics in generated samples. This paper introduces DRG-Font, a contrastive font generation strategy that learns complex glyph attributes by decomposing style and content embedding spaces. For optimal style supervision, the proposed archite...

---

### 39. Artificial intelligence application in lymphoma diagnosis with Vision Transformer using weakly supervised training

**Authors:**  Nghia,  Nguyen, Amer Wahed, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13795v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13795v1)

**Summary:** Vision transformers (ViT) have been shown to allow for more flexible feature detection and can outperform convolutional neural network (CNN) when pre-trained on sufficient data. Due to their promising feature detection capabilities, we deployed ViTs for morphological classification of anaplastic large cell lymphoma (ALCL) versus classic Hodgkin lymphoma (cHL). We had previously designed a ViT model which was trained on a small dataset of 1,200 image patches in fully supervised training. That mod...

---

### 40. From Synchrony to Sequence: Exo-to-Ego Generation via Interpolation

**Authors:** Mohammad Mahdi, Nedko Savov, Danda Pani Paudel, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13793v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13793v1)

**Summary:** Exo-to-Ego video generation aims to synthesize a first-person video from a synchronized third-person view and corresponding camera poses. While paired supervision is available, synchronized exo-ego data inherently introduces substantial spatio-temporal and geometric discontinuities, violating the smooth-motion assumptions of standard video generation benchmarks. We identify this synchronization-induced jump as the central challenge and propose Syn2Seq-Forcing, a sequential formulation that inter...

---

### 41. PBE-UNet: A light weight Progressive Boundary-Enhanced U-Net with Scale-Aware Aggregation for Ultrasound Image Segmentation

**Authors:** Chen Wang, Yixin Zhu, Yongbin Zhu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13791v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13791v1)

**Summary:** Accurate lesion segmentation in ultrasound images is essential for preventive screening and clinical diagnosis, yet remains challenging due to low contrast, blurry boundaries, and significant scale variations. Although existing deep learning-based methods have achieved remarkable performance, these methods still struggle with scale variations and indistinct tumor boundaries. To address these challenges, we propose a progressive boundary enhanced U-Net (PBE-UNet). Specially, we first introduce a ...

---

### 42. Temporally Consistent Long-Term Memory for 3D Single Object Tracking

**Authors:** Jaejoon Yoo, SuBeen Lee, Yerim Jeon, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13789v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13789v1)

**Summary:** 3D Single Object Tracking (3D-SOT) aims to localize a target object across a sequence of LiDAR point clouds, given its 3D bounding box in the first frame. Recent methods have adopted a memory-based approach to utilize previously observed features of the target object, but remain limited to only a few recent frames. This work reveals that their temporal capacity is fundamentally constrained to short-term context due to severe temporal feature inconsistency and excessive memory overhead. To this e...

---

### 43. Failure Identification in Imitation Learning Via Statistical and Semantic Filtering

**Authors:** Quentin Rolland, Fabrice Mayran de Chamisso, Jean-Baptiste Mouret

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13788v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13788v1)

**Summary:** Imitation learning (IL) policies in robotics deliver strong performance in controlled settings but remain brittle in real-world deployments: rare events such as hardware faults, defective parts, unexpected human actions, or any state that lies outside the training distribution can lead to failed executions. Vision-based Anomaly Detection (AD) methods emerged as an appropriate solution to detect these anomalous failure states but do not distinguish failures from benign deviations. We introduce FI...

---

### 44. Who Gets Flagged? The Pluralistic Evaluation Gap in AI Content Watermarking

**Authors:** Alexander Nemecek, Osama Zafar, Yuqiao Xu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13776v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13776v1)

**Summary:** Watermarking is becoming the default mechanism for AI content authentication, with governance policies and frameworks referencing it as infrastructure for content provenance. Yet across text, image, and audio modalities, watermark signal strength, detectability, and robustness depend on statistical properties of the content itself, properties that vary systematically across languages, cultural visual traditions, and demographic groups. We examine how this content dependence creates modality-spec...

---

### 45. Design and Behavior of Sparse Mixture-of-Experts Layers in CNN-based Semantic Segmentation

**Authors:** Svetlana Pavlitska, Haixi Fan, Konstantin Ditschuneit, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13761v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13761v1)

**Summary:** Sparse mixture-of-experts (MoE) layers have been shown to substantially increase model capacity without a proportional increase in computational cost and are widely used in transformer architectures, where they typically replace feed-forward network blocks. In contrast, integrating sparse MoE layers into convolutional neural networks (CNNs) remains inconsistent, with most prior work focusing on fine-grained MoEs operating at the filter or channel levels. In this work, we investigate a coarser, p...

---

### 46. MedRCube: A Multidimensional Framework for Fine-Grained and In-Depth Evaluation of MLLMs in Medical Imaging

**Authors:** Zhijie Bao, Fangke Chen, Licheng Bao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13756v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13756v1)

**Summary:** The potential of Multimodal Large Language Models (MLLMs) in domain of medical imaging raise the demands of systematic and rigorous evaluation frameworks that are aligned with the real-world medical imaging practice. Existing practices that report single or coarse-grained metrics are lack the granularity required for specialized clinical support and fail to assess the reliability of reasoning mechanisms. To address this, we propose a paradigm shift toward multidimensional, fine-grained and in-de...

---

### 47. ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction

**Authors:** Jie Liang, Jiahao Wu, Chao Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13746v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13746v1)

**Summary:** Dynamic 3D scene reconstruction is essential for immersive media such as VR, MR, and XR, yet remains challenging for long multi-view sequences with large-scale motion. Existing dynamic Gaussian approaches are either Frame-Stream, offering scalability but poor temporal stability, or Clip, achieving local consistency at the cost of high memory and limited sequence length. We propose ClipGStream, a hybrid reconstruction framework that performs stream optimization at the clip level rather than the f...

---

### 48. ReConText3D: Replay-based Continual Text-to-3D Generation

**Authors:** Muhammad Ahmed Ullah Khan, Muhammad Haris Bin Amir, Didier Stricker, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13730v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13730v1)

**Summary:** Continual learning enables models to acquire new knowledge over time while retaining previously learned capabilities. However, its application to text-to-3D generation remains unexplored. We present ReConText3D, the first framework for continual text-to-3D generation. We first demonstrate that existing text-to-3D models suffer from catastrophic forgetting under incremental training. ReConText3D enables generative models to incrementally learn new 3D categories from textual descriptions while pre...

---

### 49. Granularity-Aware Transfer for Tree Instance Segmentation in Synthetic and Real Forests

**Authors:** Pankaj Deoli, Atef Tej, Anmol Ashri, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13722v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13722v1)

**Summary:** We address the challenge of synthetic-to-real transfer in forestry perception where real data have only coarse Tree labels while synthetic data provide fine-grained trunk/crown annotations. We introduce MGTD, a mixed-granularity dataset with 53k synthetic and 3.6k real images, and a four-stage protocol isolating domain shift and granularity mismatch. Our core contribution is granularity-aware distillation, which transfers structural priors from fine-grained synthetic teachers to a coarse-label s...

---

### 50. SLQ: Bridging Modalities via Shared Latent Queries for Retrieval with Frozen MLLMs

**Authors:** Haoran Lou, Ziyan Liu, Chunxiao Fan, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13710v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13710v1)

**Summary:** Multimodal Large Language Models (MLLMs) exhibit strong reasoning and world knowledge, yet adapting them for retrieval remains challenging. Existing approaches rely on invasive parameter updates, such as full fine-tuning and LoRA, which may disrupt the pre-trained semantic space and impair the structured knowledge essential for reasoning. In this work, we argue that adapting MLLMs for retrieval should focus on eliciting pre-trained representations rather than overwriting them. To this end, we pr...

---

## cs.LG

**50 papers**

### 1. From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space

**Authors:** Yuqiao Tan, Minzheng Wang, Bo Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14142v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14142v1)

**Summary:** While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribu...

---

### 2. LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning

**Authors:** Sumeet Ramesh Motwani, Daniel Nichols, Charles London, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14140v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14140v1)

**Summary:** As language models are increasingly deployed for complex autonomous tasks, their ability to reason accurately over longer horizons becomes critical. An essential component of this ability is planning and managing a long, complex chain-of-thought (CoT). We introduce LongCoT, a scalable benchmark of 2,500 expert-designed problems spanning chemistry, mathematics, computer science, chess, and logic to isolate and directly measure the long-horizon CoT reasoning capabilities of frontier models. Proble...

---

### 3. From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs

**Authors:** Itay Itzhak, Eliya Habba, Gabriel Stanovsky, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14137v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14137v1)

**Summary:** Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empi...

---

### 4. Rhetorical Questions in LLM Representations: A Linear Probing Study

**Authors:** Louie Hong Yao, Vishesh Anand, Yuan Zhuang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14128v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14128v1)

**Summary:** Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, a...

---

### 5. Complex Interpolation of Matrices with an application to Multi-Manifold Learning

**Authors:** Adi Arbel, Stefan Steinerberger, Ronen Talmon

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14118v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14118v1)

**Summary:** Given two symmetric positive-definite matrices $A, B \in \mathbb{R}^{n \times n}$, we study the spectral properties of the interpolation $A^{1-x} B^x$ for $0 \leq x \leq 1$. The presence of `common structures' in $A$ and $B$, eigenvectors pointing in a similar direction, can be investigated using this interpolation perspective. Generically, exact log-linearity of the operator norm $\|A^{1-x} B^x\|$ is equivalent to the existence of a shared eigenvector in the original matrices; stability bounds ...

---

### 6. ID and Graph View Contrastive Learning with Multi-View Attention Fusion for Sequential Recommendation

**Authors:** Xiaofan Zhou, Kyumin Lee

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14114v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14114v1)

**Summary:** Sequential recommendation has become increasingly prominent in both academia and industry, particularly in e-commerce. The primary goal is to extract user preferences from historical interaction sequences and predict items a user is likely to engage with next. Recent advances have leveraged contrastive learning and graph neural networks to learn more expressive representations from interaction histories -- graphs capture relational structure between nodes, while ID-based representations encode i...

---

### 7. Momentum Further Constrains Sharpness at the Edge of Stochastic Stability

**Authors:** Arseniy Andreyev, Advikar Ananthkumar, Marc Walden, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14108v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14108v1)

**Summary:** Recent work suggests that (stochastic) gradient descent self-organizes near an instability boundary, shaping both optimization and the solutions found. Momentum and mini-batch gradients are widely used in practical deep learning optimization, but it remains unclear whether they operate in a comparable regime of instability. We demonstrate that SGD with momentum exhibits an Edge of Stochastic Stability (EoSS)-like regime with batch-size-dependent behavior that cannot be explained by a single mome...

---

### 8. TIP: Token Importance in On-Policy Distillation

**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14084v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14084v1)

**Summary:** On-policy knowledge distillation (OPD) trains a student on its own rollouts under token-level supervision from a teacher. Not all token positions matter equally, but existing views of token importance are incomplete. We ask a direct question: which tokens carry the most useful learning signal in OPD? Our answer is that informative tokens come from two regions: positions with high student entropy, and positions with low student entropy plus high teacher--student divergence, where the student is o...

---

### 9. Multistage Conditional Compositional Optimization

**Authors:** Buse Şen, Yifan Hu, Daniel Kuhn

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14075v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14075v1)

**Summary:** We introduce Multistage Conditional Compositional Optimization (MCCO) as a new paradigm for decision-making under uncertainty that combines aspects of multistage stochastic programming and conditional stochastic optimization. MCCO minimizes a nest of conditional expectations and nonlinear cost functions. It has numerous applications and arises, for example, in optimal stopping, linear-quadratic regulator problems, distributionally robust contextual bandits, as well as in problems involving dynam...

---

### 10. Neural architectures for resolving references in program code

**Authors:** Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14073v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14073v1)

**Summary:** Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect indexing by permutation. We create synthetic benchmarks for these tasks and show that well-known sequence-to-sequence machine learning architectures are struggling on these benchmarks. We introduce new sequence-to-sequence architectures for both problems. Our measurements show that our architectures outp...

---

### 11. A Comparative Study of Dynamic Programming and Reinforcement Learning in Finite Horizon Dynamic Pricing

**Authors:** Lev Razumovskiy, Nikolay Karenin

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14059v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14059v1)

**Summary:** This paper provides a systematic comparison between Fitted Dynamic Programming (DP), where demand is estimated from data, and Reinforcement Learning (RL) methods in finite-horizon dynamic pricing problems. We analyze their performance across environments of increasing structural complexity, ranging from a single typology benchmark to multi-typology settings with heterogeneous demand and inter-temporal revenue constraints. Unlike simplified comparisons that restrict DP to low-dimensional settings...

---

### 12. $π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

**Authors:** Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14054v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14054v1)

**Summary:** Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during t...

---

### 13. A Complete Symmetry Classification of Shallow ReLU Networks

**Authors:** Pranavkrishnan Ramakrishnan

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14037v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14037v1)

**Summary:** Parameter space is not function space for neural network architectures. This fact, investigated as early as the 1990s under terms such as ``reverse engineering," or ``parameter identifiability", has led to the natural question of parameter space symmetries\textemdash the study of distinct parameters in neural architectures which realize the same function. Indeed, the quotient space obtained by identifying parameters giving rise to the same function, called the \textit{neuromanifold}, has been sh...

---

### 14. First-See-Then-Design: A Multi-Stakeholder View for Optimal Performance-Fairness Trade-Offs

**Authors:** Kavya Gupta, Nektarios Kalampalikis, Christoph Heitz, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14035v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14035v1)

**Summary:** Fairness in algorithmic decision-making is often defined in the predictive space, where predictive performance - used as a proxy for decision-maker (DM) utility - is traded off against prediction-based fairness notions, such as demographic parity or equality of opportunity. This perspective, however, ignores how predictions translate into decisions and ultimately into utilities and welfare for both DM and decision subjects (DS), as well as their allocation across social-salient groups.   In this...

---

### 15. Hierarchical Reinforcement Learning with Runtime Safety Shielding for Power Grid Operation

**Authors:** Gitesh Malik

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14032v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14032v1)

**Summary:** Reinforcement learning has shown promise for automating power-grid operation tasks such as topology control and congestion management. However, its deployment in real-world power systems remains limited by strict safety requirements, brittleness under rare disturbances, and poor generalization to unseen grid topologies. In safety-critical infrastructure, catastrophic failures cannot be tolerated, and learning-based controllers must operate within hard physical constraints.   This paper proposes ...

---

### 16. Stochastic Trust-Region Methods for Over-parameterized Models

**Authors:** Aike Yang, Hao Wang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14017v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14017v1)

**Summary:** Under interpolation-type assumptions such as the strong growth condition, stochastic optimization methods can attain convergence rates comparable to full-batch methods, but their performance, particularly for SGD, remains highly sensitive to step-size selection. To address this issue, we propose a unified stochastic trust-region framework that eliminates manual step-size tuning and extends naturally to equality-constrained problems. For unconstrained optimization, we develop a first-order stocha...

---

### 17. MAny: Merge Anything for Multimodal Continual Instruction Tuning

**Authors:** Zijian Gao, Wangwang Jia, Xingxing Zhang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14016v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14016v1)

**Summary:** Multimodal Continual Instruction Tuning (MCIT) is essential for sequential task adaptation of Multimodal Large Language Models (MLLMs) but is severely restricted by catastrophic forgetting. While existing literature focuses on the reasoning language backbone, in this work, we expose a critical yet neglected dual-forgetting phenomenon across both perception drift in Cross-modal Projection Space and reasoning collapse in Low-rank Parameter Space. To resolve this, we present \textbf{MAny} (\textbf{...

---

### 18. Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning

**Authors:** Zekai Lin, Chao Xue, Di Liang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14010v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14010v1)

**Summary:** Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters during training. However, these methods represent a static solution to a dynamic problem, assuming that parameter importance remains fixed once identified. In this work, we empirically demonstrate that parameter importance exhibits temporal drift over the course of training. To address this, we propose...

---

### 19. Diffusion Language Models for Speech Recognition

**Authors:** Davyd Naveriani, Albert Zeyer, Ralf Schlüter, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14001v1)

**Summary:** Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC...

---

### 20. Physics-Informed Neural Networks for Methane Sorption: Cross-Gas Transfer Learning, Ensemble Collapse Under Physics Constraints, and Monte Carlo Dropout Uncertainty Quantification

**Authors:** Mohammad Nooraiepour, Zezhang Song, Wei Li, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13992v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13992v1)

**Summary:** Accurate methane sorption prediction across heterogeneous coal ranks requires models that combine thermodynamic consistency, efficient knowledge transfer across data-scarce geological systems, and calibrated uncertainty estimates, capabilities that are rarely addressed together in existing frameworks. We present a physics-informed transfer learning framework that adapts a hydrogen sorption PINN to methane sorption prediction via Elastic Weight Consolidation, coal-specific feature engineering, an...

---

### 21. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models

**Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13991v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13991v1)

**Summary:** Large language models (LLMs) are prone to generating factually incorrect outputs. Recent work has applied conformal prediction to provide uncertainty estimates and statistical guarantees for the factuality of LLM generations. However, existing approaches are typically not prompt-adaptive, limiting their ability to capture input-dependent variability. As a result, they may filter out too few items (leading to over-coverage) or too many (under-coverage) for a given task or prompt. We propose an ad...

---

### 22. Unsupervised domain transfer: Overcoming signal degradation in sleep monitoring by increasing scoring realism

**Authors:** Mohammad Ahangarkiasari, Andreas Tind Damgaard, Casper Haurum, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13988v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13988v1)

**Summary:** Objective: Investigate whether hypnogram 'realism' can be used to guide an unsupervised method for handling arbitrary types of signal degradation in mobile sleep monitoring.   Approach: Combining a pretrained, state-of-the-art 'u-sleep' model with a 'discriminator' network, we align features from a target domain with a feature space learned during pretraining. To test the approach, we distort the source domain with realistic signal degradations, to see how well the method can adapt to different ...

---

### 23. PRiMeFlow: Capturing Complex Expression Heterogeneity in Perturbation Response Modelling

**Authors:** Zichao Yan, Yan Wu, Mica Xu Ji, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13986v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13986v1)

**Summary:** Predicting the effects of perturbations in-silico on cell state can identify drivers of cell behavior at scale and accelerate drug discovery. However, modeling challenges remain due to the inherent heterogeneity of single cell gene expression and the complex, latent gene dependencies. Here, we present PRiMeFlow, an end-to-end flow matching based approach to directly model the effects of genetic and small molecule perturbations in the gene expression space. The distribution-fitting approach taken...

---

### 24. BOAT: Navigating the Sea of In Silico Predictors for Antibody Design via Multi-Objective Bayesian Optimization

**Authors:** Jackie Rao, Ferran Gonzalez Hernandez, Leon Gerard, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13980v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13980v1)

**Summary:** Antibody lead optimization is inherently a multi-objective challenge in drug discovery. Achieving a balance between different drug-like properties is crucial for the development of viable candidates, and this search becomes exponentially challenging as desired properties grow. The ever-growing zoo of sophisticated in silico tools for predicting antibody properties calls for an efficient joint optimization procedure to overcome resource-intensive sequential filtering pipelines. We present BOAT, a...

---

### 25. How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data

**Authors:** Joel Niklaus, Atsuki Yamaguchi, Michal Štefánik, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13977v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13977v1)

**Summary:** Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform...

---

### 26. Provably Efficient Offline-to-Online Value Adaptation with General Function Approximation

**Authors:** Shangzhe Li, Weitong Zhang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13966v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13966v1)

**Summary:** We study value adaptation in offline-to-online reinforcement learning under general function approximation. Starting from an imperfect offline pretrained $Q$-function, the learner aims to adapt it to the target environment using only a limited amount of online interaction. We first characterize the difficulty of this setting by establishing a minimax lower bound, showing that even when the pretrained $Q$-function is close to optimal $Q^\star$, online adaptation can be no more efficient than pure...

---

### 27. HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark

**Authors:** Jiacheng Wang, Jinchang Hou, Fabian Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13954v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13954v1)

**Summary:** Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benc...

---

### 28. Quantum Machine Learning for Colorectal Cancer Data: Anastomotic Leak Classification and Risk Factors

**Authors:** Vojtěch Novák, Ivan Zelinka, Lenka Přibylová, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13951v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13951v1)

**Summary:** This study evaluates colorectal risk factors and compares classical models against Quantum Neural Networks (QNNs) for anastomotic leak prediction. Analyzing clinical data with 14\% leak prevalence, we tested ZZFeatureMap encodings with RealAmplitudes and EfficientSU2 ansatze under simulated noise. $F_β$-optimized quantum configurations yielded significantly higher sensitivity (83.3\%) than classical baselines (66.7\%). This demonstrates that quantum feature spaces better prioritize minority clas...

---

### 29. Unsupervised Anomaly Detection in Process-Complex Industrial Time Series: A Real-World Case Study

**Authors:** Sergej Krasnikov, Lukas Meitz, Samineh Bagheri, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13928v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13928v1)

**Summary:** Industrial time-series data from real production environments exhibits substantially higher complexity than commonly used benchmark datasets, primarily due to heterogeneous, multi-stage operational processes. As a result, anomaly detection methods validated under simplified conditions often fail to generalize to industrial settings. This work presents an empirical study on a unique dataset collected from fully operational industrial machinery, explicitly capturing pronounced process-induced vari...

---

### 30. ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection

**Authors:** Romain Hermary, Samet Hicsonmez, Dan Pineau, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13924v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13924v1)

**Summary:** Time-series anomaly detection (TSAD) is critical in domains such as industrial monitoring, healthcare, and cybersecurity, but it remains challenging due to rare and heterogeneous anomalies and the scarcity of labelled data. This scarcity makes unsupervised approaches predominant, yet existing methods often rely on reconstruction or forecasting, which struggle with complex data, or on embedding-based approaches that require domain-specific anomaly synthesis and fixed distance metrics. We propose ...

---

### 31. Nested Fourier-enhanced neural operator for efficient modeling of radiation transfer in fires

**Authors:** Anran Jiao, Wengyao Jiang, Xiaoyi Lu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13919v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13919v1)

**Summary:** Computational fluid dynamics (CFD) has become an essential tool for predicting fire behavior, yet maintaining both efficiency and accuracy remains challenging. A major source of computational cost in fire simulations is the modeling of radiation transfer, which is usually the dominant heat transfer mechanism in fires. Solving the high-dimensional radiative transfer equation (RTE) with traditional numerical methods can be a performance bottleneck. Here, we present a machine learning framework bas...

---

### 32. DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off

**Authors:** Xiaofan Li, Ming Yang, Zhiyuan Ma, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13902v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13902v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant advances in the reasoning capabilities of Large Language Models (LLMs). However, effectively managing the exploration and exploitation trade-off remains a critical challenge. In this paper, we fully analyze the exploration and exploitation dilemma of extremely hard and easy samples during the training and propose a new fine-grained trade-off mechanism. Concretely, we introduce a perplexity space disentangling strateg...

---

### 33. MolCryst-MLIPs: A Machine-Learned Interatomic Potentials Database for Molecular Crystals

**Authors:** Adam Lahouari, Shen Ai, Jihye Han, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13897v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13897v1)

**Summary:** We present an open Molecular Crystal (MC) database of Machine-Learned Interatomic Potentials (MLIP) called MolCryst-MLIPs. The first release comprises fine-tuned MACE models for nine molecular crystal systems -- Benzamide, Benzoic acid, Coumarin, Durene, Isonicotinamide, Niacinamide, Nicotinamide, Pyrazinamide, and Resorcinol -- developed using the Automated Machine Learning Pipeline (AMLP), which streamlines the entire MLIP development workflow, from reference data generation to model training ...

---

### 34. Sandpile Economics: Theory, Identification, and Evidence

**Authors:** Diego Vallarino

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13890v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13890v1)

**Summary:** Why do capitalist economies recurrently generate crises whose severity is disproportionate to the size of the triggering shock? This paper proposes a structural answer grounded in the evolutionary geometry of production networks. As economies evolve through specialization, integration, and competitive selection, their inter-sectoral linkages drift toward configurations of increasing geometric fragility, eventually crossing a threshold beyond which small disturbances generate disproportionately l...

---

### 35. Context Sensitivity Improves Human-Machine Visual Alignment

**Authors:** Frieda Born, Tom Neuhäuser, Lukas Muttenthaler, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13883v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13883v1)

**Summary:** Modern machine learning models typically represent inputs as fixed points in a high-dimensional embedding space. While this approach has been proven powerful for a wide range of downstream tasks, it fundamentally differs from the way humans process information. Because humans are constantly adapting to their environment, they represent objects and their relationships in a highly context-sensitive manner. To address this gap, we propose a method for context-sensitive similarity computation from n...

---

### 36. Evaluating Supervised Machine Learning Models: Principles, Pitfalls, and Metric Selection

**Authors:** Xuanyan Liu, Ignacio Cabrera Martin, Marcello Trovati, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13882v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13882v1)

**Summary:** The evaluation of supervised machine learning models is a critical stage in the development of reliable predictive systems. Despite the widespread availability of machine learning libraries and automated workflows, model assessment is often reduced to the reporting of a small set of aggregate metrics, which can lead to misleading conclusions about real-world performance. This paper examines the principles, challenges, and practical considerations involved in evaluating supervised learning algori...

---

### 37. Drowsiness-Aware Adaptive Autonomous Braking System based on Deep Reinforcement Learning for Enhanced Road Safety

**Authors:** Hossem Eddine Hafidi, Elisabetta De Giovanni, Teodoro Montanaro, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13878v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13878v1)

**Summary:** Driver drowsiness significantly impairs the ability to accurately judge safe braking distances and is estimated to contribute to 10%-20% of road accidents in Europe. Traditional driver-assistance systems lack adaptability to real-time physiological states such as drowsiness. This paper proposes a deep reinforcement learning-based autonomous braking system that integrates vehicle dynamics with driver physiological data. Drowsiness is detected from ECG signals using a Recurrent Neural Network (RNN...

---

### 38. Hardware-Efficient Neuro-Symbolic Networks with the Exp-Minus-Log Operator

**Authors:** Eymen Ipek

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13871v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13871v1)

**Summary:** Deep neural networks (DNNs) deliver state-of-the-art accuracy on regression and classification tasks, yet two structural deficits persistently obstruct their deployment in safety-critical, resource-constrained settings: (i) opacity of the learned function, which precludes formal verification, and (ii) reliance on heterogeneous, library-bound activation functions that inflate latency and silicon area on edge hardware. The recently introduced Exp-Minus-Log (EML) Sheffer operator, eml(x, y) = exp(x...

---

### 39. Gradient Descent's Last Iterate is Often (slightly) Suboptimal

**Authors:** Guy Kornowski, Ohad Shamir

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13870v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13870v1)

**Summary:** We consider the well-studied setting of minimizing a convex Lipschitz function using either gradient descent (GD) or its stochastic variant (SGD), and examine the last iterate convergence. By now, it is known that standard stepsize choices lead to a last iterate convergence rate of $\log T/\sqrt{T}$ after $T$ steps. A breakthrough result of Jain et al. [2019] recovered the optimal $1/\sqrt{T}$ rate by constructing a non-standard stepsize sequence. However, this sequence requires choosing $T$ in ...

---

### 40. Simulation-Based Optimisation of Batting Order and Bowling Plans in T20 Cricket

**Authors:** Tinniam V Ganesh

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13861v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13861v1)

**Summary:** This paper develops a unified Markov Decision Process (MDP) framework for optimising two recurring in-match decisions in T20 cricket namely batting order selection and bowling plan assignment, directly in terms of win and defend probability rather than expected runs. A three-phase player profile engine (Powerplay, Middle, Death) with James-Stein shrinkage is estimated from 1,161 IPL ball-by-ball records (2008-2025). Win/defend probabilities are evaluated by vectorised Monte Carlo simulation over...

---

### 41. SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention

**Authors:** Hongtao Xu, Jianchao Tan, Yuxuan Hu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13847v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13847v1)

**Summary:** While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy. Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems. Therefore, we propose SparseBalance, a novel algorithm-system co-...

---

### 42. Randomized Neural Networks for Integro-Differential Equations with Application to Neutron Transport

**Authors:** Haoning Dang, Fei Wang, Yifan Chen, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13830v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13830v1)

**Summary:** Integro-differential equations arise in a wide range of applications, including transport, kinetic theory, radiative transfer, and multiphysics modeling, where nonlocal integral operators couple the solution across phase space. Such nonlocality often introduces dense coupling blocks in deterministic discretizations, leading to increased computational cost and memory usage, while physics-informed neural networks may suffer from expensive nonconvex training and sensitivity to hyperparameter choice...

---

### 43. Beyond State Consistency: Behavior Consistency in Text-Based World Models

**Authors:** Youling Huang, Guanqiao Chen, Junchi Yao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13824v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13824v1)

**Summary:** World models have been emerging as critical components for assessing the consequences of actions generated by interactive agents in online planning and offline evaluation. In text-based environments, world models are typically evaluated and trained with single-step metrics such as Exact Match, aiming to improve the similarity between predicted and real-world states, but such metrics have been shown to be insufficient for capturing actual agent behavior. To address this issue, we introduce a new ...

---

### 44. UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization

**Authors:** Zhengxi Lu, Fei Tang, Guangyi Liu, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13822v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13822v1)

**Summary:** MLLM-based GUI agents have demonstrated strong capabilities in complex user interface interaction tasks. However, long-horizon scenarios remain challenging, as these agents are burdened with tasks beyond their intrinsic capabilities, suffering from memory degradation, progress confusion, and math hallucination. To address these challenges, we present UI-Copilot, a collaborative framework where the GUI agent focuses on task execution while a lightweight copilot provides on-demand assistance for m...

---

### 45. RPS: Information Elicitation with Reinforcement Prompt Selection

**Authors:** Tao Wang, Jingyao Lu, Xibo Wang, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13817v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13817v1)

**Summary:** Large language models (LLMs) have shown remarkable capabilities in dialogue generation and reasoning, yet their effectiveness in eliciting user-known but concealed information in open-ended conversations remains limited. In many interactive AI applications, such as personal assistants, tutoring systems, and legal or clinical support, users often withhold sensitive or uncertain information due to privacy concerns, ambiguity, or social hesitation. This makes it challenging for LLMs to gather compl...

---

### 46. Composite Silhouette: A Subsampling-based Aggregation Strategy

**Authors:** Aggelos Semoglou, Aristidis Likas, John Pavlopoulos

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13816v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13816v1)

**Summary:** Determining the number of clusters is a central challenge in unsupervised learning, where ground-truth labels are unavailable. The Silhouette coefficient is a widely used internal validation metric for this task, yet its standard micro-averaged form tends to favor larger clusters under size imbalance. Macro-averaging mitigates this bias by weighting clusters equally, but may overemphasize noise from under-represented groups. We introduce Composite Silhouette, an internal criterion for cluster-co...

---

### 47. Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate

**Authors:** Jaemin Kim, Sungkyun Kim, Junyeol Lee, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13806v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13806v1)

**Summary:** Large Language Models (LLMs) are widely used across many domains, but their scale makes deployment challenging. Post-Training Quantization (PTQ) reduces memory footprint without retraining by leveraging a small calibration set. Recent Hessian-based PTQ methods compensate quantization error via cross-channel dependencies, but such approaches degrade at low bit-widths due to noisy curvature estimates from limited calibration data. We propose DASH-Q, a robust PTQ framework using diagonal Hessian ap...

---

### 48. Character Beyond Speech: Leveraging Role-Playing Evaluation in Audio Large Language Models via Reinforcement Learning

**Authors:** Dongjie Fu, Fangming Feng, Xize Cheng, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13804v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13804v1)

**Summary:** The rapid evolution of multimodal large models has revolutionized the simulation of diverse characters in speech dialogue systems, enabling a novel interactive paradigm. Character attributes are manifested not only in textual responses but also through vocal features, as speech conveys rich paralinguistic information that is challenging to quantify. This poses significant difficulties in evaluating the character alignment of role-playing agents. To address these challenges, we present RoleJudge,...

---

### 49. Driving Engagement in Daily Fantasy Sports with a Scalable and Urgency-Aware Ranking Engine

**Authors:** Unmesh Padalkar

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13796v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13796v1)

**Summary:** In daily fantasy sports (DFS), match participation is highly time-sensitive. Users must act within a narrow window before a game begins, making match recommendation a time-critical task to prevent missed engagement and revenue loss. Existing recommender systems, typically designed for static item catalogs, are ill-equipped to handle the hard temporal deadlines inherent in these live events. To address this, we designed and deployed a recommendation engine using the Deep Interest Network (DIN) ar...

---

### 50. Artificial intelligence application in lymphoma diagnosis with Vision Transformer using weakly supervised training

**Authors:**  Nghia,  Nguyen, Amer Wahed, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13795v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13795v1)

**Summary:** Vision transformers (ViT) have been shown to allow for more flexible feature detection and can outperform convolutional neural network (CNN) when pre-trained on sufficient data. Due to their promising feature detection capabilities, we deployed ViTs for morphological classification of anaplastic large cell lymphoma (ALCL) versus classic Hodgkin lymphoma (cHL). We had previously designed a ViT model which was trained on a small dataset of 1,200 image patches in fully supervised training. That mod...

---

## cs.NE

**50 papers**

### 1. Neural architectures for resolving references in program code

**Authors:** Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14073v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14073v1)

**Summary:** Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect indexing by permutation. We create synthetic benchmarks for these tasks and show that well-known sequence-to-sequence machine learning architectures are struggling on these benchmarks. We introduce new sequence-to-sequence architectures for both problems. Our measurements show that our architectures outp...

---

### 2. Deep Neural Network-guided PSO for Tracking a Global Optimal Position in Complex Dynamic Environment

**Authors:** Stephen Raharja, Toshiharu Sugawara

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14064v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14064v1)

**Summary:** We propose novel particle swarm optimization (PSO) variants incorporated with deep neural networks (DNNs) for particles to pursue globally optimal positions in dynamic environments. PSO is a heuristic approach for solving complex optimization problems. However, canonical PSO and its variants struggle to adapt efficiently to dynamic environments, in which the global optimum moves over time, and to track them accurately. Many PSO algorithms improve convergence by increasing the swarm size beyond p...

---

### 3. Diffusion Language Models for Speech Recognition

**Authors:** Davyd Naveriani, Albert Zeyer, Ralf Schlüter, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14001v1)

**Summary:** Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC...

---

### 4. A Dynamic-Growing Fuzzy-Neuro Controller, Application to a 3PSP Parallel Robot

**Authors:** Mohsen Jalaeian-Farimani, Mohammad-R Akbarzadeh-T, Alireza Akbarzadeh, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13763v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13763v1)

**Summary:** To date, various paradigms of soft-Computing have been used to solve many modern problems. Among them, a self organizing combination of fuzzy systems and neural networks can make a powerful decision making system. Here, a Dynamic Growing Fuzzy Neural Controller (DGFNC) is combined with an adaptive strategy and applied to a 3PSP parallel robot position control problem. Specifically, the dynamic growing mechanism is considered in more detail. In contrast to other self-organizing methods, DGFNC add...

---

### 5. Modeling of Self-sustained Neuron Population without External Stimulus

**Authors:** İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13719v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13719v1)

**Summary:** Self-sustained neural activity in the absence of ongoing external input is a fundamental feature of nervous system dynamics, yet the conditions under which it can emerge in biophysically grounded network models remain incompletely understood. We studied whether a recurrent network of Hodgkin-Huxley neurons with spike-timing-dependent plasticity and intrinsic stochasticity can maintain autonomous activity after brief transient stimulation. The simulated network comprised 200 neurons (160 excitato...

---

### 6. General aspects of internal noise in spiking neural networks

**Authors:** I. D. Kolesnikov, D. A. Maksimov, V. M. Moskvitin, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13612v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13612v1)

**Summary:** This study examines the impact of additive and multiplicative noise on both a single leaky integrate-and-fire (LIF) neuron and a trained spiking neural network (SNN). Noise was introduced at different stages of neural processing, including the input current, membrane potential, and output spike generation. The results show that multiplicative noise applied to the membrane potential has the most detrimental effect on network performance, leading to a significant degradation in accuracy. This is p...

---

### 7. From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

**Authors:** Alexandre Muzy

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13574v1)

**Summary:** Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems, enabling mechanistic understanding and supporting prediction of clinical interventions. Yet current approaches remain fragmented across data pipelines, model classes, temporal scales, and computing platforms, which prevents the preservation of execution semantics across the end-toend workflow. This survey introduces physically constrained executability as a unifying perspecti...

---

### 8. Greedy Approaches for Packing While Travelling with Deterministic and Stochastic Constraints

**Authors:** Thilina Pathirage Don, Aneta Neumann, Frank Neumann

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13469v1)

**Summary:** The travelling thief problem (TTP) is a well-known multi-component optimisation problem that captures the interdependence between two components: the tour across cities and the packing of items. The packing while travelling problem (PWT) is an NP-hard subproblem of TTP where the packing of items should be optimised for a given fixed tour. In many solvers, the packing component is often addressed using greedy heuristics. Here, the use of suitable greedy functions is essential for the success of g...

---

### 9. On the Use of Evolutionary Optimization for the Dynamic Chance Constrained Open-Pit Mine Scheduling Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13385v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13385v1)

**Summary:** Open-pit mine scheduling is a complex real world optimization problem that involves uncertain economic values and dynamically changing resource capacities. Evolutionary algorithms are particularly effective in these scenarios, as they can easily adapt to uncertain and changing environments. However, uncertainty and dynamic changes are often studied in isolation in real-world problems. In this paper, we study a dynamic chance-constrained open-pit mine scheduling problem in which block economic va...

---

### 10. Attention to task structure for cognitive flexibility

**Authors:** Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13281v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13281v1)

**Summary:** Humans and artificial agents must often learn and switch between multiple tasks in dynamic environments. Success in such settings requires cognitive flexibility: the ability to retain prior knowledge (cognitive stability) while also transferring it to novel tasks (cognitive generalization). Cognitive flexibility research has largely focused on the role of model architecture to achieve these complementary goals. However, it is less well understood how the structure of the environment itself influ...

---

### 11. Analog Optical Inference on Million-Record Mortgage Data

**Authors:** Sofia Berloff, Pavel Koptev, Konstantin Malkov

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13251v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13251v1)

**Summary:** Analog optical computers promise large efficiency gains for machine learning inference, yet no demonstration has moved beyond small-scale image benchmarks. We benchmark the analog optical computer (AOC) digital twin on mortgage approval classification from 5.84 million U.S. HMDA records and separate three sources of accuracy loss. On the original 19 features, the AOC reaches 94.6% balanced accuracy with 5,126 parameters (1,024 optical), compared with 97.9% for XGBoost; the 3.3 percentage-point g...

---

### 12. Does Dimensionality Reduction via Random Projections Preserve Landscape Features?

**Authors:** Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13230v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13230v1)

**Summary:** Exploratory Landscape Analysis (ELA) provides numerical features for characterizing black-box optimization problems. In high-dimensional settings, however, ELA suffers from sparsity effects, high estimator variance, and the prohibitive cost of computing several feature classes. Dimensionality reduction has therefore been proposed as a way to make ELA applicable in such settings, but it remains unclear whether features computed in reduced spaces still reflect intrinsic properties of the original ...

---

### 13. An abstract model of nonrandom, non-Lamarckian mutation in evolution using a multivariate estimation-of-distribution algorithm

**Authors:** Liudmyla Vasylenko, Adi Livnat

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12884v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12884v1)

**Summary:** At the fundamental conceptual level, two alternatives have traditionally been considered for how mutations arise and how evolution happens: 1) random mutation and natural selection, and 2) Lamarckism. Recently, the theory of Interaction-based Evolution (IBE) has been proposed, according to which mutations are neither random nor Lamarckian, but are influenced by information accumulating internally in the genome over generations. Based on the estimation-of-distribution algorithms framework, we pre...

---

### 14. Algorithmic Analysis of Dense Associative Memory: Finite-Size Guarantees and Adversarial Robustness

**Authors:** Madhava Gaikwad

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12811v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12811v1)

**Summary:** Dense Associative Memory (DAM) generalizes Hopfield networks through higher-order interactions and achieves storage capacity that scales as $O(N^{n-1})$ under suitable pattern separation conditions. Existing dynamical analyses primarily study the thermodynamic limit $N\to\infty$ with randomly sampled patterns and therefore do not provide finite-size guarantees or explicit convergence rates.   We develop an algorithmic analysis of DAM retrieval dynamics that yields finite-$N$ guarantees under exp...

---

### 15. Stability and Geometry of Attractors in Neural Cellular Automata

**Authors:** Mia-Katrin Kvalsund, James Stovold

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12720v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12720v1)

**Summary:** Throughout the literature on Neural Cellular Automata (NCAs), it is often taken for granted that the systems learn attractors. This is shown through evolving the system for many timesteps and noting visual similarity to the goal state. There remain many questions after such an analysis. Namely, what kind of attractors do we have? Is their behavior ordered or chaotic? Can we estimate stability over very long time horizons? What really happens in the attractor when perturbations are applied? In th...

---

### 16. Adaptive Spiking Neurons for Vision and Language Modeling

**Authors:** Chenlin Zhou, Sihang Guo, Jiaqi Wang, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12365v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12365v1)

**Summary:** Regarded as the third generation of neural networks, Spiking Neural Networks (SNNs) have garnered significant traction due to their biological plausibility and energy efficiency. Recent advancements in large models necessitate spiking neurons capable of high performance, adaptability, and training efficiency. In this work, we first propose a novel functional perspective that provides general guidance for designing the new generation of spiking neurons. Following the insightful guidelines, we pro...

---

### 17. GeM-EA: A Generative and Meta-learning Enhanced Evolutionary Algorithm for Streaming Data-Driven Optimization

**Authors:** Yue Wu, Yuan-Ting Zhong, Ze-Yuan Ma, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12336v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12336v1)

**Summary:** Streaming Data-Driven Optimization (SDDO) problems arise in many applications where data arrive continuously and the optimization environment evolves over time. Concept drift produces non-stationary landscapes, making optimization methods challenging due to outdated models. Existing approaches often rely on simple surrogate combinations or directly injecting solutions, which may cause negative transfer under sudden environmental changes. We propose GeM-EA, a Generative and Meta-learning Enhanced...

---

### 18. Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown

**Authors:** Sandra Gómez-Gálvez, Tobias Olenyi, Gillian Dobbie, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12245v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12245v1)

**Summary:** Deep neural networks, despite their high accuracy, often exhibit poor confidence calibration, limiting their reliability in high-stakes applications. Current ad-hoc confidence calibration methods attempt to fix this during training but face a fundamental trade-off: two-phase training methods achieve strong classification performance at the cost of training instability and poorer confidence calibration, while single-loss methods are stable but underperform in classification. This paper addresses ...

---

### 19. EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture

**Authors:** William Savage

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12167v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12167v1)

**Summary:** We present (Experience-Modulated Biologically-inspired Emergent Reasoning), a hybrid cognitive architecture that reorganises the relationship between large language models (LLMs) and memory: rather than augmenting an LLM with retrieval tools, we place the LLM as a replaceable reasoning engine within a persistent, biologically-grounded associative substrate.   The architecture centres on a 220,000-neuron spiking neural network (SNN) with spike-timing-dependent plasticity (STDP), four-layer hierar...

---

### 20. Can AI Detect Life? Lessons from Artificial Life

**Authors:** Ankit Gupta, Christoph Adami

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11915v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11915v1)

**Summary:** Modern machine learning methods have been proposed to detect life in extraterrestrial samples, drawing on their ability to distinguish biotic from abiotic samples based on training models using natural and synthetic organic molecular mixtures. Here we show using Artificial Life that such methods are easily fooled into detecting life with near 100% confidence even if the analyzed sample is not capable of life. This is due to modern machine learning methods' propensity to be easily fooled by out-o...

---

### 21. Beyond LLMs, Sparse Distributed Memory, and Neuromorphics <A Hyper-Dimensional SRAM-CAM "VaCoAl" for Ultra-High Speed, Ultra-Low Power, and Low Cost>

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11665v2) | 📄 [PDF](https://arxiv.org/pdf/2604.11665v2)

**Summary:** This paper reports an unexpected finding: in a deterministic hyperdimensional computing (HDC) architecture based on Galois-field algebra, a path-dependent semantic selection mechanism emerges, equivalent to spike-timing-dependent plasticity (STDP), with magnitude predictable a priori by a closed-form expression matching large-scale measurements. This addresses limitations of modern AI including catastrophic forgetting, learning stagnation, and the Binding Problem at an algebraic level. We propos...

---

### 22. Winner-Take-All Spiking Transformer for Language Modeling

**Authors:** Chenlin Zhou, Sihang Guo, Jiaqi Wang, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11321v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11321v1)

**Summary:** Spiking Transformers, which combine the scalability of Transformers with the sparse, energy-efficient property of Spiking Neural Networks (SNNs), have achieved impressive results in neuromorphic and vision tasks and attracted increasing attention. However, existing directly trained spiking transformers primarily focus on vision tasks. For language modeling with spiking transformer, convergence relies heavily on softmax-based spiking self-attention, which incurs high energy costs and poses challe...

---

### 23. Evolving Many Worlds: Towards Open-Ended Discovery in Petri Dish NCA via Population-Based Training

**Authors:** Uljad Berdica, Jakob Foerster, Frank Hutter, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11248v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11248v1)

**Summary:** The generation of sustained, open-ended complexity from local interactions remains a fundamental challenge in artificial life. Differentiable multi-agent systems, such as Petri Dish Neural Cellular Automata (PD-NCA), exhibit rich self-organization driven purely by spatial competition; however, they are highly sensitive to hyperparameters and frequently collapse into uninteresting patterns and dynamics, such as frozen equilibria or structureless noise. In this paper, we introduce PBT-NCA, a meta-...

---

### 24. Frugal Knowledge Graph Construction with Local LLMs: A Zero-Shot Pipeline, Self-Consistency and Wisdom of Artificial Crowds

**Authors:** Pierre Jourlin

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11104v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11104v1)

**Summary:** This paper presents an empirical study of a multi-model zero-shot pipeline for knowledge graph construction and exploitation, executed entirely through local inference on consumer-grade hardware. We propose a reproducible evaluation framework integrating two external benchmarks (DocRED, HotpotQA), WebQuestionsSP-style synthetic data, and the RAGAS evaluation framework in an automated pipeline. On 500 document-level relations, our system achieves an F1 of 0.70 $\pm$ 0.041 in zero-shot, compared t...

---

### 25. K-Way Energy Probes for Metacognition Reduce to Softmax in Discriminative Predictive Coding Networks

**Authors:** Jon-Paul Cacioli

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11011v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11011v1)

**Summary:** We present this as a negative result with an explanatory mechanism, not as a formal upper bound.   Predictive coding networks (PCNs) admit a K-way energy probe in which each candidate class is fixed as a target, inference is run to settling, and the per-hypothesis settled energies are compared. The probe appears to read a richer signal source than softmax, since the per-hypothesis energy depends on the entire generative chain.   We argue this appearance is misleading under the standard Pinchetti...

---

### 26. On the Use of Bi-Objective Evolutionary Algorithms for the Stochastic MKP under Dynamic Constraints

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.10930v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10930v1)

**Summary:** The multiple knapsack problem (MKP) generalizes the classical knapsack problem by assigning items to multiple knapsacks subject to capacity constraints. It is used to model many real-world resource allocation and scheduling problems. In practice, these optimization problems often involve stochastic and dynamic components. Evolutionary algorithms provide a flexible framework for addressing such problems under uncertainty and dynamic changes. In this paper, we investigate a stochastic and dynamic ...

---

### 27. Retinal Cyst Detection from Optical Coherence Tomography Images

**Authors:** Abhishek Dharmaratnakar, Aadheeshwar Vijayakumar, Suchand Dayanand

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10843v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10843v1)

**Summary:** Retinal Cysts are formed by leakage and accumulation of fluid in the retina due to the incompetence of retinal vasculature. These cystic spaces have significance in several ocular diseases such as age-related macular degeneration, diabetic macular edema, etc. Optical coherence tomography is one of the predominant diagnosing techniques for imaging retinal pathologies. Segmenting and quantification of intraretinal cysts plays the vital role in predicting visual acuity. In literature, several metho...

---

### 28. INCRT: An Incremental Transformer That Determines Its Own Architecture

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10703v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10703v1)

**Summary:** Transformer architectures are designed by trial and error: the number of attention heads, the depth, and the head size are fixed before training begins, with no mathematical principle to guide the choice. The result is systematic structural redundancy -- between half and four-fifths of all heads in a trained model can be removed without measurable loss -- because the architecture allocates capacity without reference to the actual requirements of the task.This paper introduces INCRT (Incremental ...

---

### 29. Visualising the Attractor Landscape of Neural Cellular Automata

**Authors:** James Stovold, Mia-Katrin Kvalsund, Harald Michael Ludwig, et al.

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10639v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10639v1)

**Summary:** As Neural Cellular Automata (NCAs) are increasingly applied outside of the toy models in Artificial Life, there is a pressing need to understand how they behave and to build appropriate routes to interpret what they have learnt. By their very nature, the benefits of training NCAs are balanced with a lack of interpretability: we can engineer emergent behaviour, but have limited ability to understand what has been learnt.   In this paper, we apply a variety of techniques to pry open the NCA black ...

---

### 30. Universal statistical signatures of evolution in artificial intelligence architectures

**Authors:** Theodor Spiro

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10571v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10571v1)

**Summary:** We test whether artificial intelligence architectural evolution obeys the same statistical laws as biological evolution. Compiling 935 ablation experiments from 161 publications, we show that the distribution of fitness effects (DFE) of architectural modifications follows a heavy-tailed Student's t-distribution with proportions (68% deleterious, 19% neutral, 13% beneficial for major ablations, n=568) that place AI between compact viral genomes and simple eukaryotes. The DFE shape matches D. mela...

---

### 31. Heterogeneous Connectivity in Sparse Networks: Fan-in Profiles, Gradient Hierarchy, and Topological Equilibria

**Authors:** Nikodem Tomczak

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10560v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10560v1)

**Summary:** Profiled Sparse Networks (PSN) replace uniform connectivity with deterministic, heterogeneous fan-in profiles defined by continuous, nonlinear functions, creating neurons with both dense and sparse receptive fields. We benchmark PSN across four classification datasets spanning vision and tabular domains, input dimensions from 54 to 784, and network depths of 2--3 hidden layers. At 90% sparsity, all static profiles, including the uniform random baseline, achieve accuracy within 0.2-0.6% of dense ...

---

### 32. Wolkowicz-Styan Upper Bound on the Hessian Eigenspectrum for Cross-Entropy Loss in Nonlinear Smooth Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-04-11

🔗 [Paper](http://arxiv.org/abs/2604.10202v2) | 📄 [PDF](https://arxiv.org/pdf/2604.10202v2)

**Summary:** Neural networks (NNs) are central to modern machine learning and achieve state-of-the-art results in many applications. However, the relationship between loss geometry and generalization is still not well understood. The local geometry of the loss function near a critical point is well-approximated by its quadratic form, obtained through a second-order Taylor expansion. The coefficients of the quadratic term correspond to the Hessian matrix, whose eigenspectrum allows us to evaluate the sharpnes...

---

### 33. Evolutionary Token-Level Prompt Optimization for Diffusion Models

**Authors:** Domício Pereira Neto, João Correia, Penousal Machado

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09861v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09861v1)

**Summary:** Text-to-image diffusion models exhibit strong generative performance but remain highly sensitive to prompt formulation, often requiring extensive manual trial and error to obtain satisfactory results. This motivates the development of automated, model-agnostic prompt optimization methods that can systematically explore the conditioning space beyond conventional text rewriting. This work investigates the use of a Genetic Algorithm (GA) for prompt optimization by directly evolving the token vector...

---

### 34. Beyond Silicon: Materials, Mechanisms, and Methods for Physical Neural Computing

**Authors:** Stefan Fischer, Nihat Ay, Olaf Landsiedel, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09833v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09833v1)

**Summary:** Physical implementations of neural computation now extend far beyond silicon hardware, encompassing substrates such as memristive devices, photonic circuits, mechanical metamaterials, microfluidic networks, chemical reaction systems, and living neural tissue. By exploiting intrinsic physical processes such as charge transport, wave interference, elastic deformation, mass transport, and biochemical regulation, these substrates can realize neural inference and adaptation directly in matter. As sil...

---

### 35. Drift-Aware Online Dynamic Learning for Nonstationary Multivariate Time Series: Application to Sintering Quality Prediction

**Authors:** Yumeng Zhao, Shengxiang Yang, Xianpeng Wang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09358v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09358v1)

**Summary:** Accurate prediction of nonstationary multivariate time series remains a critical challenge in complex industrial systems such as iron ore sintering. In practice, pronounced concept drift compounded by significant label verification latency rapidly degrades the performance of offline-trained models. Existing methods based on static architectures or passive update strategies struggle to simultaneously extract multi-scale spatiotemporal features and overcome the stability-plasticity dilemma without...

---

### 36. A 0.5-V Linear Neuromorphic Voltage-to-Spike Encoder Using a Bulk-Driven Transconductor

**Authors:** Meysam Akbari, Erika Covi, Kea-Tiong Tang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09315v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09315v1)

**Summary:** This work introduces an ultralow-power voltage-to-spike encoder that achieves near-linear voltage-to-firing-rate conversion by pairing a linearized bulk-driven transconductor with a DPI-based LIF neuron. A tail-less bulk-driven differential pair improves large-signal linearity, while a translinear linearization network suppresses the dominant sinh nonlinearity and stabilizes the bias-tunable V-to-I gain. The resulting current feeds a DPI front-end that linearizes current-to-spike conversion. Fab...

---

### 37. Statistical Properties of the King Wen Sequence: An Anti-Habituation Structure That Does Not Improve Neural Network Training

**Authors:** Augustin Chan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09234v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09234v1)

**Summary:** The King Wen sequence of the I-Ching (c. 1000 BC) orders 64 hexagrams -- states of a six-dimensional binary space -- in a pattern that has puzzled scholars for three millennia. We present a rigorous statistical characterization of this ordering using Monte Carlo permutation analysis against 100,000 random baselines. We find that the sequence has four statistically significant properties: higher-than-random transition distance (98.2nd percentile), negative lag-1 autocorrelation (p=0.037), yang-ba...

---

### 38. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 39. Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity

**Authors:** Kentaro Nomura, Takato Horii

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09026v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09026v1)

**Summary:** Social agents both internalize collective norms and reshape them through creative action, yet computational models have not captured this bidirectional process within a unified framework. We propose a multi-agent simulation model grounded in active inference that formalizes the dialectical constitution of social reality on a structured social network. Each agent maintains an internal generative model, communicates with neighbors to form social priors, creates novel observations, and selectively ...

---

### 40. Ge$^\text{2}$mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer

**Authors:** Zecheng Hao, Shenghao Xie, Kang Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08894v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08894v1)

**Summary:** Spiking Neural Networks (SNNs) offer superior energy efficiency over Artificial Neural Networks (ANNs). However, they encounter significant deficiencies in training and inference metrics when applied to Spiking Vision Transformers (S-ViTs). Existing paradigms including ANN-SNN Conversion and Spatial-Temporal Backpropagation (STBP) suffer from inherent limitations, precluding concurrent optimization of memory, accuracy and energy consumption. To address these issues, we propose Ge$^\text{2}$mS-T,...

---

### 41. Hierarchical Kernel Transformer: Multi-Scale Attention with an Information-Theoretic Approximation Analysis

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08829v1)

**Summary:** The Hierarchical Kernel Transformer (HKT) is a multi-scale attention mechanism that processes sequences at L resolution levels via trainable causal downsampling, combining level-specific score matrices through learned convex weights. The total computational cost is bounded by 4/3 times that of standard attention, reaching 1.3125x for L = 3. Four theoretical results are established. (i) The hierarchical score matrix defines a positive semidefinite kernel under a sufficient condition on the symmet...

---

### 42. Memory Wall is not gone: A Critical Outlook on Memory Architecture in Digital Neuromorphic Computing

**Authors:** Amirreza Yousefzadeh, Sameed Sohail, Ana Lucia Varbanescu

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08774v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08774v1)

**Summary:** The rapid advancement of neuromorphic technology aims to address the memory wall challenge inherent in conventional von Neumann architectures. This paper critically examines current digital neuromorphic processors and their strategies to mitigate this bottleneck. While designed to bring computation closer to memory through distributed architectures, our findings indicate that on-chip memory systems, including SRAM and emerging technologies like STT-MRAM, have become significant consumers of area...

---

### 43. A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need

**Authors:** Hananel Hazan, Yanbo Zhang, Benedikt Hartl, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08749v2) | 📄 [PDF](https://arxiv.org/pdf/2604.08749v2)

**Summary:** How many of a neural network's parameters actually encode task-specific information? We investigate this question with LottaLoRA, a training paradigm in which every backbone weight is drawn at random and frozen; only low-rank LoRA adapters are trained. Across nine benchmarks spanning diverse architecture families from single-layer classifiers to 900M parameter Transformers low-rank adapters over frozen random backbones recover 96-100% of fully trained performance while training only 0.5-40% of t...

---

### 44. Multi-Modal Learning meets Genetic Programming: Analyzing Alignment in Latent Space Optimization

**Authors:** Benjamin Léger, Kazem Meidani, Christian Gagné

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08324v2) | 📄 [PDF](https://arxiv.org/pdf/2604.08324v2)

**Summary:** Symbolic regression (SR) aims to discover mathematical expressions from data, a task traditionally tackled using Genetic Programming (GP) through combinatorial search over symbolic structures. Latent Space Optimization (LSO) methods use neural encoders to map symbolic expressions into continuous spaces, transforming the combinatorial search into continuous optimization. SNIP (Meidani et al., 2024), a contrastive pre-training model inspired by CLIP, advances LSO by introducing a multi-modal appro...

---

### 45. Robust Multi-Objective Optimization for Bicycle Rebalancing in Shared Mobility Systems

**Authors:** Diego Daniel Pedroza-Perez, Gabriel Luque, Sergio Nesmachnow, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08296v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08296v1)

**Summary:** Dock-based bike-sharing systems exhibit spatial imbalances between bicycle supply and user demand, often addressed through overnight truck-based rebalancing. This work studies static overnight rebalancing under demand uncertainty modeled as a tri-objective optimization problem. The objectives minimize total travel distance, expected unmet demand, and a robustness-oriented unmet demand measure over high-demand scenarios.   Route plans are evaluated via a recourse simulation that enforces truck lo...

---

### 46. Introducing Echo Networks for Computational Neuroevolution

**Authors:** Christian Kroos, Fabian Küch

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08204v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08204v1)

**Summary:** For applications on the extreme edge, minimal networks of only a few dozen artificial neurons for event detection and classification in discrete time signals would be highly desirable. Feed-forward networks, RNNs, and CNNs evolved through evolutionary algorithms can all be successful in this respect but pose the problem of allowing little systematicity in mutation and recombination if the standard direct genetic encoding of the weights is used (as for instance in the classic NEAT algorithm). We ...

---

### 47. Exploration of Pareto-preserving Search Space Transformations in Multi-objective Test Functions

**Authors:** Diederick Vermetten, Jeroen Rook

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08173v2) | 📄 [PDF](https://arxiv.org/pdf/2604.08173v2)

**Summary:** Benchmark problems are an important tool for gaining understanding of optimization algorithms. Since algorithms often aim to perform well on benchmarks, biases in benchmark design provide misleading insights. In single-objective optimization, for example, many problems used to have their optimum in the center of the search domain. To remedy these issues, search space transformations have been widely adopted by benchmark suites, preventing algorithms from exploiting unintended structure.   In mul...

---

### 48. Internal noise in deep neural networks: interplay of depth, neuron number, and noise injection step

**Authors:** D. A. Maksimov, V. M. Moskvitin, N. Semenova

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08117v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08117v1)

**Summary:** This paper examines the influence of internal Gaussian noise on the performance of deep feedforward neural networks, focusing on the role of the noise injection stage relative to the activation function. Two scenarios are analyzed: noise introduced before and after the activation function, for both additive and multiplicative noise influence. The case of noise before activation function is similar to perturbations in the input channel of neuron, while the noise introduced after activation functi...

---

### 49. Analysis of Search Heuristics in the Multi-Armed Bandit Setting

**Authors:** Jasmin Brandt, Barbara Hammer, Timo Kötzing, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08109v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08109v1)

**Summary:** We consider the classic Multi-Armed Bandit setting to understand the exploration/exploitation tradeoffs made by different search heuristics. Since many search heuristics work by comparing different options (in evolutionary algorithms called "individuals"; in the Bandit literature called "arms"), we work with the "Dueling Bandits" setting. In each iteration, a comparison between different arms can be made; in the binary stochastic setting, each arm has a fixed winning probability against any othe...

---

### 50. Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency

**Authors:** Mingqing Xiao, Yansen Wang, Dongqi Han, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07904v1)

**Summary:** Spatiotemporal neural dynamics and oscillatory synchronization are widely implicated in biological information processing and have been hypothesized to support flexible coordination such as feature binding. By contrast, most deep learning architectures represent and propagate information through activation values, neglecting the joint dynamics of rate and phase. In this work, we introduce Kuramoto oscillatory Phase Encoding (KoPE) as an additional, evolving phase state to Vision Transformers, in...

---

## q-bio.NC

**50 papers**

### 1. Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

**Authors:** Laurent U Perrinet

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14096v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14096v1)

**Summary:** Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequen...

---

### 2. Modeling of Self-sustained Neuron Population without External Stimulus

**Authors:** İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13719v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13719v1)

**Summary:** Self-sustained neural activity in the absence of ongoing external input is a fundamental feature of nervous system dynamics, yet the conditions under which it can emerge in biophysically grounded network models remain incompletely understood. We studied whether a recurrent network of Hodgkin-Huxley neurons with spike-timing-dependent plasticity and intrinsic stochasticity can maintain autonomous activity after brief transient stimulation. The simulated network comprised 200 neurons (160 excitato...

---

### 3. From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

**Authors:** Alexandre Muzy

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13574v1)

**Summary:** Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems, enabling mechanistic understanding and supporting prediction of clinical interventions. Yet current approaches remain fragmented across data pipelines, model classes, temporal scales, and computing platforms, which prevents the preservation of execution semantics across the end-toend workflow. This survey introduces physically constrained executability as a unifying perspecti...

---

### 4. Attention to task structure for cognitive flexibility

**Authors:** Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13281v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13281v1)

**Summary:** Humans and artificial agents must often learn and switch between multiple tasks in dynamic environments. Success in such settings requires cognitive flexibility: the ability to retain prior knowledge (cognitive stability) while also transferring it to novel tasks (cognitive generalization). Cognitive flexibility research has largely focused on the role of model architecture to achieve these complementary goals. However, it is less well understood how the structure of the environment itself influ...

---

### 5. The illusory simplicity of the feedforward pass: evidence for the dynamical nature of stimulus encoding along the primate ventral stream

**Authors:** Daniel Anthes, Sushrut Thorat, Anna Mitola, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12825v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12825v1)

**Summary:** In studying primate vision, a large body of work focuses on the first feedforward sweep. During this initial time window, information is thought to pass through ventral stream regions in a stage-like fashion in an effort to extract high-level information from the retinal input. Consequently, electrophysiological analyses commonly focus on spatial response patterns, either by averaging data in time, or by applying decoders in a temporally local fashion. By analysing data recorded simultaneously a...

---

### 6. Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining

**Authors:** Junfeng Xia, Wenhao Ye, Xuanye Pan, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12683v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12683v1)

**Summary:** Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. We present \textit{Brain-DiT}, a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal space or a lat...

---

### 7. Integrated information theory: the good, the bad and the misunderstood

**Authors:** Adam B. Barrett, Borjan Milinkovic, Pedro A. M. Mediano, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11482v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11482v1)

**Summary:** The integrated information theory of consciousness (IIT) is uniquely ambitious in proposing a mathematical formula, derived from apparently fundamental properties of conscious experience, to describe the quantity and quality of consciousness for any physical system that possesses it. IIT has generated considerable debate, which has engendered some misunderstandings and misrepresentations. Here we address and hope to remedy this. We begin by concisely summarising the essentials of IIT. Given IIT ...

---

### 8. The Neurobiological Craving Signature (NCS) predicts social craving and responds to social isolation

**Authors:** Ana Defendini Cortes, Livia Tomova, Leonie Koban

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11208v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11208v1)

**Summary:** Humans are inherently social and seek connection with others for survival. Recent studies suggest that acute social isolation leads to craving for social interactions, but the brain mechanisms of social craving and their relationship to brain networks underlying drug and food craving remain incompletely understood. Here we harnessed an existing dataset and tested whether the Neurobiological Craving Signature (NCS)-a recently developed fMRI-based brain-signature of drug and food craving-also pred...

---

### 9. Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching

**Authors:** Nicole Rogalla, Yuzhen Qin, Mario Senden, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11178v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11178v1)

**Summary:** Forecasting neural activity in response to naturalistic stimuli remains a key challenge for understanding brain dynamics and enabling downstream neurotechnological applications. Here, we introduce a generative forecasting framework for modeling neural dynamics based on autoregressive flow matching (AFM). Building on recent advances in transport-based generative modeling, our approach probabilistically predicts neural responses at scale from multimodal sensory input. Specifically, we learn the co...

---

### 10. Relaxing in Warped Spaces: Generalized Hierarchical and Modular Dynamical Neural Network

**Authors:** Kazuyoshi Tsutsumi, Ernst Niebur

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10606v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10606v1)

**Summary:** We propose a dynamical neural network model with a hierarchical and modular structure. The network architecture can be derived by minimizing an energy function that is originally designed based on two kinds of neurons with quite different time constants. It has multiple subspaces that are spanned by neural parameters employed in the energy function, and adjacent subspaces are related to each other with a layered internetwork. Each internetwork further consists of a pair of a forward subnet and a...

---

### 11. Astrocytic resource diffusion stabilizes persistent activity in neural fields

**Authors:** Noah Palmer, Heather L. Cihak, Daniele Avitabile, et al.

**Published:** 2026-04-11

🔗 [Paper](http://arxiv.org/abs/2604.10036v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10036v1)

**Summary:** Persistent neural activity underlying working memory requires sustained synaptic transmission, yet the metabolic and neurotransmitter support provided by astrocyte networks is largely absent from spatially extended neural circuit models. We introduce a coupled astrocyte-neural field model in which synaptic efficacy is regulated by depletion and recovery of a conserved resource pool recycled and spatially redistributed through diffusively coupled astrocytes. We obtain explicit stationary bump pro...

---

### 12. The Rise and Fall of $G$ in AGI

**Authors:** David C. Krakauer

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09911v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09911v1)

**Summary:** In the psychological literature the term `general intelligence' describes correlations between abilities and not simply the number of abilities. This paper connects Spearman's $g$-factor from psychometrics, measuring a positive manifold, to the implicit ``$G$-factor'' in claims about artificial general intelligence (AGI) performance on temporally structured benchmarks. By treating LLM benchmark batteries as cognitive test batteries and model releases as subjects, principal component analysis is ...

---

### 13. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 14. Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

**Authors:** Mu Nan, Muquan Yu, Weijian Mai, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08537v1)

**Summary:** Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge...

---

### 15. Neuromodulation supports robust rhythmic pattern transitions in degenerate central pattern generators with fixed connectivity

**Authors:** Arthur Fyon, Alessio Franci, Pierre Sacré, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08312v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08312v1)

**Summary:** Many essential biological functions, such as breathing and locomotion, rely on the coordination of robust and adaptable rhythmic patterns, governed by specific network architectures known as connectomes. Rhythmic adaptation is often linked to slow structural modifications of the connectome through synaptic plasticity, but such mechanisms are too slow to support rapid, localized rhythmic transitions. Here, we propose a neuromodulation-based control architecture for dynamically reconfiguring rhyth...

---

### 16. The Cartesian Cut in Agentic AI

**Authors:** Tim Sainburg, Caleb Weinreb

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07745v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07745v1)

**Summary:** LLMs gain competence by predicting words in human text, which often reflects how people perform tasks. Consequently, coupling an LLM to an engineered runtime turns prediction into control: outputs trigger interventions that enact goal-oriented behavior. We argue that a central design lever is where control resides in these systems. Brains embed prediction within layered feedback controllers calibrated by the consequences of action. By contrast, LLM agents implement Cartesian agency: a learned co...

---

### 17. The Principle of Maximum Heterogeneity Optimises Productivity in Distributed Production Systems Across Biology, Economics, and Computing

**Authors:** Guillhem Artis, Danyal Akarca, Jascha Achterberg

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07602v1)

**Summary:** The world is full of systems of distributed agents, collaborating and competing in complex ways: firms and workers specialise within economies, neurons adapt their tuning across brain circuits, and species compete and coexist within ecosystems. In that context, individual research fields built theories explaining how comparative advantage drives trade specialisation, how balanced neural representations emerge from sensory coding, and how biodiversity sustains ecological productivity. Here we pro...

---

### 18. Exploring the proprioceptive potential of joint receptors using a biomimetic robotic joint

**Authors:** Akihiro Miki, Shun Hasegawa, Sota Yuzaki, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07038v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07038v1)

**Summary:** In neuroscience, joint receptors have traditionally been viewed as limit detectors, providing positional information only at extreme joint angles, while muscle spindles are considered the primary sensors of joint angle position. However, joint receptors are widely distributed throughout the joint capsule, and their full role in proprioception remains unclear. In this study, we specifically focused on mimicking Type I joint receptors, which respond to slow and sustained movements, and quantified ...

---

### 19. Quantum-like Cognition in Process Theories: An Analysis

**Authors:** Sean Tull, Masanao Ozawa

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.08604v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08604v1)

**Summary:** Various effects in human cognition, often considered `non-classical', have been argued to be most naturally modelled by quantum-like models of decision making. We extend this approach to describe models of cognition and decision-making in general probabilistic process theories, which include both classical probabilistic models and quantum instrument models as special cases. We show how many aspects of quantum-like cognition can be described diagrammatically in process theories, before using our ...

---

### 20. Bridging Theory and Practice in Crafting Robust Spiking Reservoirs

**Authors:** Ruggero Freddi, Nicolas Seseri, Diana Nigrisoli, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06395v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06395v1)

**Summary:** Spiking reservoir computing provides an energy-efficient approach to temporal processing, but reliably tuning reservoirs to operate at the edge-of-chaos is challenging due to experimental uncertainty. This work bridges abstract notions of criticality and practical stability by introducing and exploiting the robustness interval, an operational measure of the hyperparameter range over which a reservoir maintains performance above task-dependent thresholds. Through systematic evaluations of Leaky I...

---

### 21. Hierarchical Mesh Transformers with Topology-Guided Pretraining for Morphometric Analysis of Brain Structures

**Authors:** Yujian Xiong, Mohammad Farazi, Yanxi Chen, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05215v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05215v1)

**Summary:** Representation learning on large-scale unstructured volumetric and surface meshes poses significant challenges in neuroimaging, especially when models must incorporate diverse vertex-level morphometric descriptors, such as cortical thickness, curvature, sulcal depth, and myelin content, which carry subtle disease-related signals. Current approaches either ignore these clinically informative features or support only a single mesh topology, restricting their use across imaging pipelines. We introd...

---

### 22. Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization

**Authors:** Arthur N. Montanari, Francesco Bullo, Dmitry Krotov, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05042v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05042v1)

**Summary:** Recent advances at the intersection of control theory, neuroscience, and machine learning have revealed novel mechanisms by which dynamical systems perform computation. These advances encompass a wide range of conceptual, mathematical, and computational ideas, with applications for model learning and training, memory retrieval, data-driven control, and optimization. This tutorial focuses on neuro-inspired approaches to computation that aim to improve scalability, robustness, and energy efficienc...

---

### 23. Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales

**Authors:** Tsung-Han Kuo, Tzu-Chia Tung

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04770v1)

**Summary:** Balanced spiking networks can transition between silent, asynchronous-irregular, and oscillatory states depending on interacting synaptic and temporal time scales, while their joint parameter structure remains incompletely characterized. In this work, we systematically map how postsynaptic decay (τs), conduction delay (d), and plasticity rate (λp) jointly shape oscillatory regimes in recurrent leaky integrate-and-fire networks. By combining Brian2 simulations across the (τs, d, λp) space with a ...

---

### 24. Causal Stance

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05004v2) | 📄 [PDF](https://arxiv.org/pdf/2604.05004v2)

**Summary:** What exactly is the meaning of physical causal closure, a concept frequently discussed in the philosophy of mind? Jaegwon Kim explicitly adopts a conception of causation according to which physical causation is effectively identified with deterministic physical lawfulness, and on this basis equates physical determinism with physical causal closure. While this conception is internally coherent, it differs from the currently dominant theories of causation, which emphasize asymmetry between cause a...

---

### 25. Non-Equilibrium Stochastic Dynamics as a Unified Framework for Insight and Repetitive Learning: A Kramers Escape Approach to Continual Learning

**Authors:** Gunn Kim

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04154v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04154v1)

**Summary:** Continual learning in artificial neural networks is fundamentally limited by the stability--plasticity dilemma: systems that retain prior knowledge tend to resist acquiring new knowledge, and vice versa. Existing approaches, most notably elastic weight consolidation~(EWC), address this empirically without a physical account of why plasticity eventually collapses as tasks accumulate. Separately, the distinction between sudden insight and gradual skill acquisition through repetitive practice has l...

---

### 26. The physical basis of information flow in neural matter: a thermocoherent perspective on cognitive dynamics

**Authors:** Onur Pusuluk

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04069v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04069v2)

**Summary:** Information flow is central to contemporary accounts of cognition, yet its physical basis in living neural matter remains poorly specified. Here, we develop a multiscale resource-theoretical framework motivated by the \textit{thermocoherent effect}, where heat flow is reciprocally coupled to a delocalized information flow carried by shared coherence and not reducible to local subsystem variables. Extending this line of work in light of recent results on correlation-enabled Mpemba-type thermal re...

---

### 27. Topological Sensitivity in Connectome-Constrained Neural Networks

**Authors:** Nalin Dhiman

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04033v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04033v1)

**Summary:** Connectome-constrained neural networks are often evaluated against sparse random controls and then interpreted as evidence that biological graph topology improves learning efficiency. We revisit that claim in a controlled flyvis-based study using a Drosophila connectome, a naive self-loop-matched random graph, and a degree-preserving rewired null. Under weak controls, in which both models were recovered from a connectome-trained checkpoint and the null matched only global graph counts, the conne...

---

### 28. Neurological Plausibility of AI-Generated Music for Commercial Environments: An In-Silico Cortical Investigation Using Wubble and TRIBE v2

**Authors:** Shaad Sufi

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04025v1)

**Summary:** Background music shapes attention, affect, and approach behavior in commercial environments, yet the neural plausibility of AI-generated music for such settings remains poorly characterized. We present an in-silico pilot study that combines Wubble, a generative music system, with TRIBE v2, a publicly released whole-brain encoding model, to estimate cortical response profiles for prompt-conditioned retail music. Five fully instrumental tracks were generated to span low-to-high arousal, sparse-to-...

---

### 29. Large Language Models Align with the Human Brain during Creative Thinking

**Authors:** Mete Ismayilzada, Simone A. Luchini, Abdulkadir Gokce, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03480v1)

**Summary:** Creative thinking is a fundamental aspect of human cognition, and divergent thinking-the capacity to generate novel and varied ideas-is widely regarded as its core generative engine. Large language models (LLMs) have recently demonstrated impressive performance on divergent thinking tests and prior work has shown that models with higher task performance tend to be more aligned to human brain activity. However, existing brain-LLM alignment studies have focused on passive, non-creative tasks. Here...

---

### 30. Self-Supervised Foundation Model for Calcium-imaging Population Dynamics

**Authors:** Xinhong Xu, Yimeng Zhang, Qichen Qian, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.04958v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04958v2)

**Summary:** Recent work suggests that large-scale, multi-animal modeling can significantly improve neural recording analysis. However, for functional calcium traces, existing approaches remain task-specific, limiting transfer across common neuroscience objectives. To address this challenge, we propose \textbf{CalM}, a self-supervised neural foundation model trained solely on neuronal calcium traces and adaptable to multiple downstream tasks, including forecasting and decoding. Our key contribution is a pret...

---

### 31. Temporal structure of the language hierarchy within small cortical patches

**Authors:** Julien Gadonneix, Mingfang Zhang, Jérémy Rapin, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03021v1)

**Summary:** Speech production requires the rapid coordination of a complex hierarchy of linguistic units, transforming a semantic representation into a precise sequence of articulatory movements. To unravel the neural mechanisms underlying this feat, we leverage recordings from eight 3.2 x 3.2 mm 64-microelectrode arrays implanted in the motor cortex and inferior frontal gyrus of two patients tasked to produce twenty thousand sentences. We show that a hierarchy of linguistic features are robustly encoded in...

---

### 32. Mapping generative AI use in the human brain: divergent neural, academic, and mental health profiles of functional versus socio emotional AI use

**Authors:** Junjie Wang, Xianyang Gan, Dan Liu, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.08594v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08594v1)

**Summary:** The widespread adoption of generative artificial intelligence conversational agents (AICAs) among university students constitutes a novel cognitive social environment whose impact on the maturing brain remains elusive. Combining surveys with high resolution structural MRI, we examined patterns of general, functional, and socio emotional AICA use, academic performance, mental health, and brain structural signatures in a comparatively large sample of 222 young individuals. Across computational ana...

---

### 33. Phase estimation with autoregressive padding (PEAP): addressing inaccuracies and biases in EEG analysis

**Authors:** Miriam Kirchhoff, Johanna Rösch, Maria Ermolova, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02212v1)

**Summary:** Accurate phase estimation at the edge of data segments is crucial for EEG applications such as EEG-TMS in offline and real-time data analysis. Our research evaluates the phase estimation performance of four commonly used methods (Phastimate, SSPE, ETP, and PhastPadding) for accuracy and systemic biases, using data from young and elderly healthy controls and chronic stroke participants. To address the identified limitations of the established methods, we introduce Phase Estimation with Autoregres...

---

### 34. Thermodynamic connectivity reveals functional specialization and multiplex organization of extrasynaptic signaling

**Authors:** Giridhar Sunil, Habib Benali, Elkaïoum M. Moutuou

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02057v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02057v1)

**Summary:** Neural communication operates on both fast synaptic transmission and slower, diffusive extrasynaptic signaling, yet how these two modes jointly organize brain function remains unclear. Here, using the complete synaptic and neuropeptidergic connectomes of \emph{Caenorhabditis elegans}, we develop a unified multiplex framework linking anatomical wiring to functional communication. We infer structure-derived functional connectivity from the synaptic connectome using equilibrium principles from stat...

---

### 35. Interpretable Electrophysiological Features of Resting-State EEG Capture Cortical Network Dynamics in Parkinsons Disease

**Authors:** Antonios G. Dougalis

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01475v2) | 📄 [PDF](https://arxiv.org/pdf/2604.01475v2)

**Summary:** Parkinsons disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive. This study examined whether interpretable EEG features capturing complementary aspects of neural dynamics can discriminate Parkinsonian neural states. A comprehensive set of interpretable features was extracted and grouped into Standard descriptors (spectral power, phase synchronization, time-domain statistics) and Dynamical descriptors (aperiodic activity, cross-fre...

---

### 36. Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models

**Authors:** Po-Han Chiang

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01295v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01295v1)

**Summary:** This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Conventional SSMs achieve high-speed sequence processing through parallel scans, yet are limited to temporal recurrence without lateral or feedback interactions within a single timestep. PHC maps the diagonal SSM core to a shared Neuron Layer and inter-neuronal communication to a shared Synapse Layer, where neurons ar...

---

### 37. Ultrasonic Brain Computer Interfaces for Enhancing Human-Machine Cognition

**Authors:** William J. Tyler

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.00349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00349v1)

**Summary:** Low-intensity transcranial focused ultrasound (tFUS) is rapidly emerging as a transformative non-invasive brain stimulation (NIBS) modality characterized by high spatial resolution and ability to target deep brain circuits. Unlike electromagnetic techniques such as transcranial magnetic stimulation and transcranial direct current stimulation, which are constrained by centimeter-scale resolution and a depth-focality tradeoff, tFUS leverages mechanical pressure waves to modulate both superficial c...

---

### 38. From Patterns to Policy: A Scoping Review Based on Bibliometric Analysis (ScoRBA) of Intelligent and Secure Smart Hospital Ecosystems

**Authors:** Adi Wijaya, Budi Hermawan, Wiga Maulana Baihaqi, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.30004v1) | 📄 [PDF](https://arxiv.org/pdf/2603.30004v1)

**Summary:** This study examines the evolution of Intelligent and Secure Smart Hospital Ecosystems using a Scoping Review with Bibliometric Analysis (ScoRBA) to map research patterns, identify gaps, and derive policy implications. Analyzing 891 journal articles from Scopus (2006-2025) through co-occurrence analysis, network visualization, overlay analysis, and the Enhanced Strategic Diagram (ESD), the study applies the PAGER framework to link Patterns, Advances, Gaps, Research directions, and Evidence-based ...

---

### 39. Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective

**Authors:** Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29903v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29903v1)

**Summary:** Brain connectomics is still largely dominated by pairwise-based models, such as graphs, which cannot represent circulatory or higher-order functional interactions. In this paper, we propose a multimodal framework based on Topological Signal Processing (TSP) that models the brain as a higher-order topological domain and treats functional interactions as discrete vector fields. We integrate diffusion MRI and resting-state fMRI to learn subject-specific brain cell complexes, where statistically val...

---

### 40. Counterfactual Analysis of Brain Network Dynamics

**Authors:** Moo K. Chung, Luigi Maccotta, Aaron Struck

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29843v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29843v1)

**Summary:** Causal inference in brain networks has traditionally relied on regression-based models such as Granger causality, structural equation modeling, and dynamic causal modeling. While effective for identifying directed associations, these methods remain descriptive and acyclic, leaving open the fundamental question of intervention: what would the causal organization become if a pathway were disrupted or externally modulated? We introduce a unified framework for counterfactual causal analysis that mod...

---

### 41. Copy-Spread-Annihilate Dynamics in Degree-Assortative Networks

**Authors:** Yan Hao, Daniel J. Graham, Marc-Thorsten Hütt

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29833v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29833v1)

**Summary:** In many systems, communication proceeds by broadcasting rather than single source-target routing, but network structures that maximize signal lifetime are not well understood. Degree correlations are known to influence robustness and spreading, yet their effect on signal persistence has remained unclear. Here we introduce Copy-Spread-Annihilate dynamics, a minimal synchronous broadcasting model with annihilation. We show that signal lifetimes vary non-monotonically with assortativity and are max...

---

### 42. Covariant quantum error correction in a three-layer quantum brain model: computational analysis of layer-specific coherence dynamics

**Authors:** Hikaru Wakaura

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2604.08587v2) | 📄 [PDF](https://arxiv.org/pdf/2604.08587v2)

**Summary:** Quantum brain proposals require coherence on behaviorally relevant timescales, yet the gap between spin coherence times and neural decision windows has remained a quantitative obstacle. We evaluate approximate covariant quantum error correction (CQEC) -- a purification protocol constrained by the Eastin-Knill theorem -- across two radical-pair proteins parameterized by \textit{ab initio} spin Hamiltonians: monoamine oxidase~A (MAO-A) and cryptochrome (CRY, PDB~4I6G). Both share a three-layer arc...

---

### 43. Convergent Representations of Linguistic Constructions in Human and Artificial Neural Systems

**Authors:** Pegah Ramezani, Thomas Kinfe, Andreas Maier, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29617v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29617v1)

**Summary:** Understanding how the brain processes linguistic constructions is a central challenge in cognitive neuroscience and linguistics. Recent computational studies show that artificial neural language models spontaneously develop differentiated representations of Argument Structure Constructions (ASCs), generating predictions about when and how construction-level information emerges during processing. The present study tests these predictions in human neural activity using electroencephalography (EEG)...

---

### 44. Structural and dynamical strategies to prevent runaway excitation in reservoir computing

**Authors:** Claus Metzner, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29597v1)

**Summary:** Reservoirs, typically implemented as recurrent neural networks with fixed random connection weights, can be combined with a simple trained readout layer to perform a wide range of computational tasks. However, increasing the magnitude of reservoir connection weights to exploit nonlinear dynamics can cause the network to develop strong spontaneous activity that drives neurons into saturation, dramatically degrading performance. In this work, we investigate two distinct countermeasures against suc...

---

### 45. Predicting Neuromodulation Outcome for Parkinson's Disease with Generative Virtual Brain Model

**Authors:** Siyuan Du, Siyi Li, Shuwei Bai, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29176v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29176v1)

**Summary:** Parkinson's disease (PD) affects over ten million people worldwide. Although temporal interference (TI) and deep brain stimulation (DBS) are promising therapies, inter-individual variability limits empirical treatment selection, increasing non-negligible surgical risk and cost. Previous explorations either resort to limited statistical biomarkers that are insufficient to characterize variability, or employ AI-driven methods which is prone to overfitting and opacity. We bridge this gap with a pre...

---

### 46. Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds

**Authors:** N Alex Cayco-Gajic, Arthur Pellegrino

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28764v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28764v1)

**Summary:** Similarity measures are widely used to interpret the representational geometries used by neural networks to solve tasks. Yet, because existing methods compare the extrinsic geometry of representations in state space, rather than their intrinsic geometry, they may fail to capture subtle yet crucial distinctions between fundamentally different neural network solutions. Here, we introduce metric similarity analysis (MSA), a novel method which leverages tools from Riemannian geometry to compare the ...

---

### 47. A Normative Theory of Decision Making from Multiple Stimuli: The Contextual Diffusion Decision Model

**Authors:** Michael Shvartsman, Vaibhav Srivastava, Narayanan Sundaram, et al.

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28600v1)

**Summary:** The dynamics of simple two-alternative forced-choice (2AFC) decisions are well-modeled by a class of random walk models (e.g. Laming, 1968; Ratcliff, 1978; Usher & McClelland, 2001; Bogacz et al., 2006). However, in real-life, even simple decisions involve dynamically changing influence of additional information. In this work, we describe a computational theory of decision making from multiple sources of information, grounded in Bayesian inference and consistent with a simple neural network. Thi...

---

### 48. Allocentric Navigation Is Computationally Universal

**Authors:** Gualtiero Piccinini

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.27926v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27926v1)

**Summary:** This report presents three proofs showing that idealized architectures capable of navigation guided by allocentric maps with landmark structure can be computationally universal. The navigation may occur either online (in the environment) or offline (in the animal's head). The first proof proceeds from a universal two-counter machine by encoding counters as the positions of two movable markers on orthogonal coordinate axes. The second proof directly simulates an ordinary one-tape Turing machine b...

---

### 49. The role of neuromorphic principles in the future of biomedicine and healthcare

**Authors:** Grace M. Hwang, Jessica D. Falcone, Joseph D. Monaco, et al.

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27716v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27716v1)

**Summary:** Neuromorphic engineering has matured over the past four decades and is currently experiencing explosive growth with the potential to transform biomedical engineering and neurotechnologies. Participants at the Neuromorphic Principles in Biomedicine and Healthcare (NPBH) Workshop (October 2024) -- representing a broad cross-section of the community, including early-career and established scholars, engineers, scientists, clinicians, industry, and funders -- convened to discuss the state of the fiel...

---

### 50. Energy Landscapes of Emotion: Quantifying Brain Network Stability During Happy and Sad Face Processing Using EEG-Based Hopfield Energy

**Authors:** Barry Djibrina, Jiajia Li

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27644v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27644v1)

**Summary:** Understanding how the human brain instantiates distinct emotional states is a key challenge in affective neuroscience. While network-based approaches have advanced emotion processing research,they remain largely descriptive,leaving the dynamical stability of emotional brain states unquantified.This study introduces a novel framework to quantify this stability by applying Hopfield network energy to empirically derived functional connectivity. High density EEG was recorded from 20 healthy adults d...

---

## stat.ML

**50 papers**

### 1. Momentum Further Constrains Sharpness at the Edge of Stochastic Stability

**Authors:** Arseniy Andreyev, Advikar Ananthkumar, Marc Walden, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14108v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14108v1)

**Summary:** Recent work suggests that (stochastic) gradient descent self-organizes near an instability boundary, shaping both optimization and the solutions found. Momentum and mini-batch gradients are widely used in practical deep learning optimization, but it remains unclear whether they operate in a comparable regime of instability. We demonstrate that SGD with momentum exhibits an Edge of Stochastic Stability (EoSS)-like regime with batch-size-dependent behavior that cannot be explained by a single mome...

---

### 2. Multistage Conditional Compositional Optimization

**Authors:** Buse Şen, Yifan Hu, Daniel Kuhn

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14075v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14075v1)

**Summary:** We introduce Multistage Conditional Compositional Optimization (MCCO) as a new paradigm for decision-making under uncertainty that combines aspects of multistage stochastic programming and conditional stochastic optimization. MCCO minimizes a nest of conditional expectations and nonlinear cost functions. It has numerous applications and arises, for example, in optimal stopping, linear-quadratic regulator problems, distributionally robust contextual bandits, as well as in problems involving dynam...

---

### 3. Two-Sided Bounds for Entropic Optimal Transport via a Rate-Distortion Integral

**Authors:** Jingbo Liu

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14061v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14061v1)

**Summary:** We show that the maximum expected inner product between a random vector and the standard normal vector over all couplings subject to a mutual information constraint or regularization is equivalent to a truncated integral involving the rate-distortion function, up to universal multiplicative constants. The proof is based on a lifting technique, which constructs a Gaussian process indexed by a random subset of the type class of the probability distribution involved in the information-theoretic ine...

---

### 4. BOAT: Navigating the Sea of In Silico Predictors for Antibody Design via Multi-Objective Bayesian Optimization

**Authors:** Jackie Rao, Ferran Gonzalez Hernandez, Leon Gerard, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13980v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13980v1)

**Summary:** Antibody lead optimization is inherently a multi-objective challenge in drug discovery. Achieving a balance between different drug-like properties is crucial for the development of viable candidates, and this search becomes exponentially challenging as desired properties grow. The ever-growing zoo of sophisticated in silico tools for predicting antibody properties calls for an efficient joint optimization procedure to overcome resource-intensive sequential filtering pipelines. We present BOAT, a...

---

### 5. Sandpile Economics: Theory, Identification, and Evidence

**Authors:** Diego Vallarino

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13890v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13890v1)

**Summary:** Why do capitalist economies recurrently generate crises whose severity is disproportionate to the size of the triggering shock? This paper proposes a structural answer grounded in the evolutionary geometry of production networks. As economies evolve through specialization, integration, and competitive selection, their inter-sectoral linkages drift toward configurations of increasing geometric fragility, eventually crossing a threshold beyond which small disturbances generate disproportionately l...

---

### 6. Forecasting Multivariate Time Series under Predictive Heterogeneity: A Validation-Driven Clustering Framework

**Authors:** Ziling Ma, Ángel López Oriona, Hernando Ombao, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13748v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13748v1)

**Summary:** We study adaptive pooling under predictive heterogeneity in high-dimensional multivariate time series forecasting, where global models improve statistical efficiency but may fail to capture heterogeneous predictive structure, while naive specialization can induce negative transfer. We formulate adaptive pooling as a statistical decision problem and propose a validation-driven framework that determines when and how specialization should be applied. Rather than grouping series based on representat...

---

### 7. Online learning with noisy side observations

**Authors:** Tomáš Kocák, Gergely Neu, Michal Valko

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13740v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13740v1)

**Summary:** We propose a new partial-observability model for online learning problems where the learner, besides its own loss, also observes some noisy feedback about the other actions, depending on the underlying structure of the problem. We represent this structure by a weighted directed graph, where the edge weights are related to the quality of the feedback shared by the connected nodes. Our main contribution is an efficient algorithm that guarantees a regret of $\widetilde{O}(\sqrt{α^* T})$ after $T$ r...

---

### 8. Spectral Thompson sampling

**Authors:** Tomas Kocak, Michal Valko, Remi Munos, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13739v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13739v1)

**Summary:** Thompson Sampling (TS) has attracted a lot of interest due to its good empirical performance, in particular in the computational advertising. Though successful, the tools for its performance analysis appeared only recently. In this paper, we describe and analyze SpectralTS algorithm for a bandit problem, where the payoffs of the choices are smooth given an underlying graph. In this setting, each choice is a node of a graph and the expected payoffs of the neighboring nodes are assumed to be simil...

---

### 9. Covariance-adapting algorithm for semi-bandits with application to sparse rewards

**Authors:** Pierre Perrault, Vianney Perchet, Michal Valko

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13738v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13738v1)

**Summary:** We investigate stochastic combinatorial semi-bandits, where the entire joint distribution of outcomes impacts the complexity of the problem instance (unlike in the standard bandits). Typical distributions considered depend on specific parameter values, whose prior knowledge is required in theory but quite difficult to estimate in practice; an example is the commonly assumed sub-Gaussian family. We alleviate this issue by instead considering a new general family of sub-exponential distributions, ...

---

### 10. Ordinary Least Squares is a Special Case of Transformer

**Authors:** Xiaojun Tan, Yuchen Zhao

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13656v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13656v1)

**Summary:** The statistical essence of the Transformer architecture has long remained elusive: Is it a universal approximator, or a neural network version of known computational algorithms? Through rigorous algebraic proof, we show that the latter better describes Transformer's basic nature: Ordinary Least Squares (OLS) is a special case of the single-layer Linear Transformer. Using the spectral decomposition of the empirical covariance matrix, we construct a specific parameter setting where the attention m...

---

### 11. Robust Low-Rank Tensor Completion based on M-product with Weighted Correlated Total Variation and Sparse Regularization

**Authors:** Biswarup Karmakar, Ratikanta Behera

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13525v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13525v1)

**Summary:** The robust low-rank tensor completion problem addresses the challenge of recovering corrupted high-dimensional tensor data with missing entries, outliers, and sparse noise commonly found in real-world applications. Existing methodologies have encountered fundamental limitations due to their reliance on uniform regularization schemes, particularly the tensor nuclear norm and $\ell_1$ norm regularization approaches, which indiscriminately apply equal shrinkage to all singular values and sparse com...

---

### 12. Joint Representation Learning and Clustering via Gradient-Based Manifold Optimization

**Authors:** Sida Liu, Yangzi Guo, Mingyuan Wang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13484v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13484v1)

**Summary:** Clustering and dimensionality reduction have been crucial topics in machine learning and computer vision. Clustering high-dimensional data has been challenging for a long time due to the curse of dimensionality. For that reason, a more promising direction is the joint learning of dimension reduction and clustering. In this work, we propose a Manifold Learning Framework that learns dimensionality reduction and clustering simultaneously. The proposed framework is able to jointly learn the paramete...

---

### 13. Universality of Gaussian-Mixture Reverse Kernels in Conditional Diffusion

**Authors:** Nafiz Ishtiaque, Syed Arefinul Haque, Kazi Ashraful Alam, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13470v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13470v1)

**Summary:** We prove that conditional diffusion models whose reverse kernels are finite Gaussian mixtures with ReLU-network logits can approximate suitably regular target distributions arbitrarily well in context-averaged conditional KL divergence, up to an irreducible terminal mismatch that typically vanishes with increasing diffusion horizon. A path-space decomposition reduces the output error to this mismatch plus per-step reverse-kernel errors; assuming each reverse kernel factors through a finite-dimen...

---

### 14. Estimating Continuous Treatment Effects with Two-Stage Kernel Ridge Regression

**Authors:** Seok-Jin Kim, Kaizheng Wang

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13410v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13410v1)

**Summary:** We study the problem of estimating the effect function for a continuous treatment, which maps each treatment value to a population-averaged outcome. A central challenge in this setting is confounding: treatment assignment often depends on covariates, creating selection bias that makes direct regression of the response on treatment unreliable. To address this issue, we propose a two-stage kernel ridge regression method. In the first stage, we learn a model for the response as a function of both t...

---

### 15. A short proof of near-linear convergence of adaptive gradient descent under fourth-order growth and convexity

**Authors:** Damek Davis, Dmitriy Drusvyatskiy

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13393v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13393v1)

**Summary:** Davis, Drusvyatskiy, and Jiang showed that gradient descent with an adaptive stepsize converges locally at a nearly-linear rate for smooth functions that grow at least quartically away from their minimizers. The argument is intricate, relying on monitoring the performance of the algorithm relative to a certain manifold of slow growth -- called the ravine. In this work, we provide a direct Lyapunov-based argument that bypasses these difficulties when the objective is in addition convex and a has ...

---

### 16. Some Theoretical Limitations of t-SNE

**Authors:** Rupert Li, Elchanan Mossel

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13295v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13295v1)

**Summary:** t-SNE has gained popularity as a dimension reduction technique, especially for visualizing data. It is well-known that all dimension reduction techniques may lose important features of the data. We provide a mathematical framework for understanding this loss for t-SNE by establishing a number of results in different scenarios showing how important features of data are lost by using t-SNE.

---

### 17. Bias-Corrected Adaptive Conformal Inference for Multi-Horizon Time Series Forecasting

**Authors:** Ankit Lade, Sai Krishna J., Indar Kumar

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13253v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13253v1)

**Summary:** Adaptive Conformal Inference (ACI) provides distribution-free prediction intervals with asymptotic coverage guarantees for time series under distribution shift. However, ACI only adapts the quantile threshold -- it cannot shift the interval center. When a base forecaster develops persistent bias after a regime change, ACI compensates by widening intervals symmetrically, producing unnecessarily conservative bands. We propose Bias-Corrected ACI (BC-ACI), which augments standard ACI with an online ...

---

### 18. Identifiability of Potentially Degenerate Gaussian Mixture Models With Piecewise Affine Mixing

**Authors:** Danru Xu, Sébastien Lachapelle, Sara Magliacane

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13218v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13218v1)

**Summary:** Causal representation learning (CRL) aims to identify the underlying latent variables from high-dimensional observations, even when variables are dependent with each other. We study this problem for latent variables that follow a potentially degenerate Gaussian mixture distribution and that are only observed through the transformation via a piecewise affine mixing function. We provide a series of progressively stronger identifiability results for this challenging setting in which the probability...

---

### 19. Rare Event Analysis via Stochastic Optimal Control

**Authors:** Yuanqi Du, Jiajun He, Dinghuai Zhang, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13213v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13213v1)

**Summary:** Rare events such as conformational changes in biomolecules, phase transitions, and chemical reactions are central to the behavior of many physical systems, yet they are extremely difficult to study computationally because unbiased simulations seldom produce them. Transition Path Theory (TPT) provides a rigorous statistical framework for analyzing such events: it characterizes the ensemble of reactive trajectories between two designated metastable states (reactant and product), and its central ob...

---

### 20. Classical and Quantum Speedups for Non-Convex Optimization via Energy Conserving Descent

**Authors:** Yihang Sun, Huaijin Wang, Patrick Hayden, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13022v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13022v1)

**Summary:** The Energy Conserving Descent (ECD) algorithm was recently proposed (De Luca & Silverstein, 2022) as a global non-convex optimization method. Unlike gradient descent, appropriately configured ECD dynamics escape strict local minima and converge to a global minimum, making it appealing for machine learning optimization.   We present the first analytical study of ECD, focusing on the one-dimensional setting for this first installment. We formalize a stochastic ECD dynamics (sECD) with energy-prese...

---

### 21. Nonparametric efficient inference for network quantile causal effects under partial interference

**Authors:** Chao Cheng, Fan Li

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13008v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13008v1)

**Summary:** Interference arises when the treatment assigned to one individual affects the outcomes of other individuals. Commonly, individuals are naturally grouped into clusters, and interference occurs only among individuals within the same cluster, a setting referred to as partial interference. We study network causal effects on outcome quantiles in the presence of partial interference. We develop a general nonparametric efficiency theory for estimating these network quantile causal effects, which leads ...

---

### 22. Causal Diffusion Models for Counterfactual Outcome Distributions in Longitudinal Data

**Authors:** Farbod Alinezhad, Jianfei Cao, Gary J. Young, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12992v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12992v1)

**Summary:** Predicting counterfactual outcomes in longitudinal data, where sequential treatment decisions heavily depend on evolving patient states, is critical yet notoriously challenging due to complex time-dependent confounding and inadequate uncertainty quantification in existing methods. We introduce the Causal Diffusion Model (CDM), the first denoising diffusion probabilistic approach explicitly designed to generate full probabilistic distributions of counterfactual outcomes under sequential intervent...

---

### 23. An Optimal Sauer Lemma Over $k$-ary Alphabets

**Authors:** Steve Hanneke, Qinglin Meng, Shay Moran, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12952v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12952v1)

**Summary:** The Sauer-Shelah-Perles Lemma is a cornerstone of combinatorics and learning theory, bounding the size of a binary hypothesis class in terms of its Vapnik-Chervonenkis (VC) dimension. For classes of functions over a $k$-ary alphabet, namely the multiclass setting, the Natarajan dimension has long served as an analogue of VC dimension, yet the corresponding Sauer-type bounds are suboptimal for alphabet sizes $k>2$.   In this work, we establish a sharp Sauer inequality for multiclass and list pred...

---

### 24. Adaptive Learning via Off-Model Training and Importance Sampling for Fully Non-Markovian Optimal Stochastic Control. Complete version

**Authors:** Dorival Leão, Alberto Ohashi, Simone Scotti, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13147v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13147v1)

**Summary:** This paper studies continuous-time stochastic control problems whose controlled states are fully non-Markovian and depend on unknown model parameters. Such problems arise naturally in path-dependent stochastic differential equations, rough-volatility hedging, and systems driven by fractional Brownian motion. Building on the discrete skeleton approach developed in earlier work, we propose a Monte Carlo learning methodology for the associated embedded backward dynamic programming equation. Our mai...

---

### 25. Loop Corrections to the Training and Generalization Errors of Random Feature Models

**Authors:** Taeyoung Kim

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12827v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12827v1)

**Summary:** We investigate random feature models in which neural networks sampled from a prescribed initialization ensemble are frozen and used as random features, with only the readout weights optimized. Adopting a statistical-physics viewpoint, we study the training, test, and generalization errors beyond the mean-kernel approximation. Since the predictor is a nonlinear functional of the induced random kernel, the ensemble-averaged errors depend not only on the mean kernel but also on higher-order fluctua...

---

### 26. Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory

**Authors:** Shaopeng Fu, Di Wang

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12817v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12817v1)

**Summary:** Adversarial training (AT) is an effective defense for large language models (LLMs) against jailbreak attacks, but performing AT on LLMs is costly. To improve the efficiency of AT for LLMs, recent studies propose continuous AT (CAT) that searches for adversarial inputs within the continuous embedding space of LLMs during AT. While CAT has achieved empirical success, its underlying mechanism, i.e., why adversarial perturbations in the embedding space can help LLMs defend against jailbreak prompts ...

---

### 27. Asymptotic Theory for Graphical SLOPE: Precision Estimation and Pattern Convergence

**Authors:** Ivan Hejný, Giovanni Bonaccolto, Philipp Kremer, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12771v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12771v1)

**Summary:** This paper studies Graphical SLOPE for precision matrix estimation, with emphasis on its ability to recover both sparsity and clusters of edges with equal or similar strength. In a fixed-dimensional regime, we establish that the root-$n$ scaled estimation error converges to the unique minimizer of a strictly convex optimization problem defined through the directional derivative of the SLOPE penalty. We also establish convergence of the induced SLOPE pattern, thereby obtaining an asymptotic chara...

---

### 28. Monte Carlo Stochastic Depth for Uncertainty Estimation in Deep Learning

**Authors:** Adam T. Müller, Tobias Rögelein, Nicolaj C. Stache

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12719v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12719v1)

**Summary:** The deployment of deep neural networks in safety-critical systems necessitates reliable and efficient uncertainty quantification (UQ). A practical and widespread strategy for UQ is repurposing stochastic regularizers as scalable approximate Bayesian inference methods, such as Monte Carlo Dropout (MCD) and MC-DropBlock (MCDB). However, this paradigm remains under-explored for Stochastic Depth (SD), a regularizer integral to the residual-based backbones of most modern architectures. While prior wo...

---

### 29. MCAnalysis: An Open-Source Package for Preprocessing, Modelling, and Visualisation of Menstrual Cycle Effects in Digital Health Data

**Authors:** Kyra Delray, Glyn Lewis, Bola Grace, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12536v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12536v1)

**Summary:** The menstrual cycle influences numerous physiological and psychological outcomes, yet standardised, open-source statistical methods for quantifying these cyclic effects remain lacking. We developed mcanalysis, an open-source package in R and Python implementing a Fourier-basis generalised additive model (GAM) for menstrual cycle research. The package provides a complete pipeline: processing period dates, labelling cycle days relative to menstruation onset, filtering physiologically plausible cyc...

---

### 30. Adaptive Budget Allocation in LLM-Augmented Surveys

**Authors:** Zikun Ye, Jiameng Lyu, Rui Tao

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12497v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12497v1)

**Summary:** Large language models (LLMs) can generate survey responses at low cost, but their reliability varies substantially across questions and is unknown before data collection. Deploying LLMs in surveys still requires costly human responses for verification and correction. How should a limited human-labeling budget be allocated across questions in real time? We propose an adaptive allocation algorithm that learns which questions are hardest for the LLM while simultaneously collecting human responses. ...

---

### 31. A Bayesian Perspective on the Role of Epistemic Uncertainty for Delayed Generalization in In-Context Learning

**Authors:** Abdessamed Qchohi, Simone Rossi

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12434v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12434v1)

**Summary:** In-context learning enables transformers to adapt to new tasks from a few examples at inference time, while grokking highlights that this generalization can emerge abruptly only after prolonged training. We study task generalization and grokking in in-context learning using a Bayesian perspective, asking what enables the delayed transition from memorization to generalization. Concretely, we consider modular arithmetic tasks in which a transformer must infer a latent linear function solely from i...

---

### 32. Information-Geometric Decomposition of Generalization Error in Unsupervised Learning

**Authors:** Gilhan Kim

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12340v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12340v1)

**Summary:** We decompose the Kullback--Leibler generalization error (GE) -- the expected KL divergence from the data distribution to the trained model -- of unsupervised learning into three non-negative components: model error, data bias, and variance. The decomposition is exact for any e-flat model class and follows from two identities of information geometry: the generalized Pythagorean theorem and a dual e-mixture variance identity. As an analytically tractable demonstration, we apply the framework to $ε...

---

### 33. Fine-tuning Factor Augmented Neural Lasso for Heterogeneous Environments

**Authors:** Jinhang Chai, Jianqing Fan, Cheng Gao, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12288v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12288v1)

**Summary:** Fine-tuning is a widely used strategy for adapting pre-trained models to new tasks, yet its methodology and theoretical properties in high-dimensional nonparametric settings with variable selection have not yet been developed. This paper introduces the fine-tuning factor augmented neural Lasso (FAN-Lasso), a transfer learning framework for high-dimensional nonparametric regression with variable selection that simultaneously handles covariate and posterior shifts. We use a low-rank factor structu...

---

### 34. Generalization Guarantees on Data-Driven Tuning of Gradient Descent with Langevin Updates

**Authors:** Saumya Goyal, Rohith Rongali, Ritabrata Ray, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.13130v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13130v1)

**Summary:** We study learning to learn for regression problems through the lens of hyperparameter tuning. We propose the Langevin Gradient Descent Algorithm (LGD), which approximates the mean of the posterior distribution defined by the loss function and regularizer of a convex regression task. We prove the existence of an optimal hyperparameter configuration for which the LGD algorithm achieves the Bayes' optimal solution for squared loss. Subsequently, we study generalization guarantees on meta-learning o...

---

### 35. A Nonparametric Adaptive EWMA Control Chart for Binary Monitoring of Multiple Stream Processes

**Authors:** Faruk Muritala, Austin Brown, Dhrubajyoti Ghosh, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.12095v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12095v1)

**Summary:** Monitoring binomial proportions across multiple independent streams is a critical challenge in Statistical Process Control (SPC), with applications from manufacturing to cybersecurity. While EWMA charts offer sensitivity to small shifts, existing implementations rely on asymptotic variance approximations that fail during early-phase monitoring. We introduce a Cumulative Standardized Binomial EWMA (CSB-EWMA) chart that overcomes this limitation by deriving the exact time-varying variance of the E...

---

### 36. On the continuum limit of t-SNE for data visualization

**Authors:** Jeff Calder, Zhonggan Huang, Ryan Murray, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.12041v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12041v1)

**Summary:** This work is concerned with the continuum limit of a graph-based data visualization technique called the t-Distributed Stochastic Neighbor Embedding (t-SNE), which is widely used for visualizing data in a variety of applications, but is still poorly understood from a theoretical standpoint. The t-SNE algorithm produces visualizations by minimizing the Kullback-Leibler divergence between similarity matrices representing the high dimensional data and its low dimensional representation. We prove th...

---

### 37. Convolutional Maximum Mean Discrepancy for Inference in Noisy Data

**Authors:** Ritwik Vashistha, Jeff M. Phillips, Abhra Sarkar, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.12022v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12022v1)

**Summary:** Modern data analyses frequently encounter settings where samples of variables are contaminated by measurement error. Ignoring measurement noise can substantially degrade statistical inference, while existing correction techniques are often computationally costly and inefficient. Recent advances in kernel methods, particularly those based on Maximum Mean Discrepancy (MMD), have enabled flexible, distribution-free inference, yet typically assume precise data and overlook contamination by measureme...

---

### 38. Offline-Online Reinforcement Learning for Linear Mixture MDPs

**Authors:** Zhongjun Zhang, Sean R. Sinclair

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11994v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11994v1)

**Summary:** We study offline-online reinforcement learning in linear mixture Markov decision processes (MDPs) under environment shift. In the offline phase, data are collected by an unknown behavior policy and may come from a mismatched environment, while in the online phase the learner interacts with the target environment. We propose an algorithm that adaptively leverages offline data. When the offline data are informative, either due to sufficient coverage or small environment shift, the algorithm provab...

---

### 39. Subcritical Signal Propagation at Initialization in Normalization-Free Transformers

**Authors:** Sergey Alekseev

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11890v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11890v1)

**Summary:** We study signal propagation at initialization in transformers through the averaged partial Jacobian norm (APJN), a measure of gradient amplification across layers. We extend APJN analysis to transformers with bidirectional attention and permutation-symmetric input token configurations by deriving recurrence relations for activation statistics and APJNs across layers. Our theory predicts how attention modifies the asymptotic behavior of the APJN at large depth and matches APJNs measured in deep v...

---

### 40. MosaicMRI: A Diverse Dataset and Benchmark for Raw Musculoskeletal MRI

**Authors:** Paula Arguello, Berk Tinaz, Mohammad Shahab Sepehri, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11762v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11762v1)

**Summary:** Deep learning underpins a wide range of applications in MRI, including reconstruction, artifact removal, and segmentation. However, progress has been driven largely by public datasets focused on brain and knee imaging, shaping how models are trained and evaluated. As a result, careful studies of the reliability of these models across diverse anatomical settings remain limited. In this work, we introduce MosaicMRI, a large and diverse collection of fully sampled raw musculoskeletal (MSK) MR measu...

---

### 41. Inferring Change Points in Regression via Sample Weighting

**Authors:** Gabriel Arpino, Ramji Venkataramanan

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11746v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11746v1)

**Summary:** We study the problem of identifying change points in high-dimensional generalized linear models, and propose an approach based on sample-weighted empirical risk minimization. Our method, Weighted ERM, encodes priors on the change points via weights assigned to each sample, to obtain weighted versions of standard estimators such as M-estimators and maximum-likelihood estimators. Under mild assumptions on the data, we obtain a precise asymptotic characterization of the performance of our method fo...

---

### 42. Nested Atoms Model with Application to Clustering Big Population-Scale Single-Cell Data

**Authors:** Arhit Chakrabarti, Yang Ni, Yuchao Jiang, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11731v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11731v1)

**Summary:** We consider the problem of clustering nested or hierarchical data, where observations are grouped and there are both group-level and observation-level variables. In our motivating OneK1K dataset, observations consist of single-cell RNA-sequencing (scRNA-seq) data from 982 individuals (groups), totaling 1.27 million cells (observations), along with individual-specific genotype data. This type of data would enable the identification of cell types and the investigation of how genetic variations amo...

---

### 43. Minimizing classical resources in variational measurement-based quantum computation for generative modeling

**Authors:** Arunava Majumder, Hendrik Poulsen Nautrup, Hans J. Briegel

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11578v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11578v1)

**Summary:** Measurement-based quantum computation (MBQC) is a framework for quantum information processing in which a computational task is carried out through one-qubit measurements on a highly entangled resource state. Due to the indeterminacy of the outcomes of a quantum measurement, the random outcomes of these operations, if not corrected, yield a variational quantum channel family. Traditionally, this randomness is corrected through classical processing in order to ensure deterministic unitary computa...

---

### 44. Obtaining Partition Crossover masks using Statistical Linkage Learning for solving noised optimization problems with hidden variable dependency structure

**Authors:** M. W. Przewozniczek, B. Frej, M. M. Komarnicki, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11862v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11862v1)

**Summary:** In optimization problems, some variable subsets may have a joint non-linear or non-monotonical influence on the function value. Therefore, knowledge of variable dependencies may be crucial for effective optimization, and many state-of-the-art optimizers leverage it to improve performance. However, some real-world problem instances may be the subject of noise of various origins. In such a case, variable dependencies relevant to optimization may be hard or impossible to tell using dependency check...

---

### 45. Deep Learning for Sequential Decision Making under Uncertainty: Foundations, Frameworks, and Frontiers

**Authors:** I. Esra Buyuktahtakin

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11507v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11507v1)

**Summary:** Artificial intelligence (AI) is moving increasingly beyond prediction to support decisions in complex, uncertain, and dynamic environments. This shift creates a natural intersection with operations research and management sciences (OR/MS), which have long offered conceptual and methodological foundations for sequential decision-making under uncertainty. At the same time, recent advances in deep learning, including feedforward neural networks, LSTMs, transformers, and deep reinforcement learning,...

---

### 46. ADD for Multi-Bit Image Watermarking

**Authors:** An Luo, Jie Ding

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11491v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11491v1)

**Summary:** As generative models enable rapid creation of high-fidelity images, societal concerns about misinformation and authenticity have intensified. A promising remedy is multi-bit image watermarking, which embeds a multi-bit message into an image so that a verifier can later detect whether the image is generated by someone and further identify the source by decoding the embedded message. Existing approaches often fall short in capacity, resilience to common image distortions, and theoretical justifica...

---

### 47. Learning Discrete Diffusion of Graphs via Free-Energy Gradient Flows

**Authors:** Dario Rancati, Jan Maas, Francesco Locatello

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11311v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11311v1)

**Summary:** Diffusion-based models on continuous spaces have seen substantial recent progress through the mathematical framework of gradient flows, leveraging the Wasserstein-2 (${W}_2$) metric via the Jordan-Kinderlehrer-Otto (JKO) scheme. Despite the increasing popularity of diffusion models on discrete spaces using continuous-time Markov chains, a parallel theoretical framework based on gradient flows has remained elusive due to intrinsic challenges in translating the ${W}_2$ distance directly into these...

---

### 48. Beyond Fixed False Discovery Rates: Post-Hoc Conformal Selection with E-Variables

**Authors:** Meiyi Zhu, Osvaldo Simeone

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11305v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11305v1)

**Summary:** Conformal selection (CS) uses calibration data to identify test inputs whose unobserved outcomes are likely to satisfy a pre-specified minimal quality requirement, while controlling the false discovery rate (FDR). Existing methods fix the target FDR level before observing data, which prevents the user from adapting the balance between number of selected test inputs and FDR to downstream needs and constraints based on the available data. For example, in genomics or neuroimaging, researchers often...

---

### 49. Trustworthy Feature Importance Avoids Unrestricted Permutations

**Authors:** Emanuele Borgonovo, Francesco Cappelli, Xuefei Lu, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11253v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11253v1)

**Summary:** Feature importance methods using unrestricted permutations are flawed due to extrapolation errors; such errors appear in all non-trivial variable importance approaches. We propose three new approaches: conditional model reliance and Knockoffs with Gaussian transformation, and restricted ALE plot designs. Theoretical and numerical results show our strategies reduce/eliminate extrapolation.

---

### 50. Regional Explanations: Bridging Local and Global Variable Importance

**Authors:** Salim I. Amoukou, Nicolas J-B. Brunel

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11223v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11223v1)

**Summary:** We analyze two widely used local attribution methods, Local Shapley Values and LIME, which aim to quantify the contribution of a feature value $x_i$ to a specific prediction $f(x_1, \dots, x_p)$. Despite their widespread use, we identify fundamental limitations in their ability to reliably detect locally important features, even under ideal conditions with exact computations and independent features. We argue that a sound local attribution method should not assign importance to features that nei...

---

