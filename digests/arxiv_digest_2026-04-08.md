# arXiv Daily Digest - 2026-04-08

Total papers: 250

---

## cs.AI

**50 papers**

### 1. In-Place Test-Time Training

**Authors:** Guhao Feng, Shengjie Luo, Kai Hua, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06169v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06169v1)

**Summary:** The static ``train then deploy" paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks. Test-Time Training (TTT) offers a compelling alternative by updating a subset of model parameters (fast weights) at inference time, yet its potential in the current LLM ecosystem is hindered by critical barriers including architectural incompatibility, computational inefficiency and mi...

---

### 2. DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models

**Authors:** Zhengming Yu, Li Ma, Mingming He, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06161v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06161v1)

**Summary:** Most digital videos are stored in 8-bit low dynamic range (LDR) formats, where much of the original high dynamic range (HDR) scene radiance is lost due to saturation and quantization. This loss of highlight and shadow detail precludes mapping accurate luminance to HDR displays and limits meaningful re-exposure in post-production workflows. Although techniques have been proposed to convert LDR images to HDR through dynamic range expansion, they struggle to restore realistic detail in the over- an...

---

### 3. MMEmb-R1: Reasoning-Enhanced Multimodal Embedding with Pair-Aware Selection and Adaptive Control

**Authors:** Yuchi Wang, Haiyang Yu, Weikang Bian, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06156v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06156v1)

**Summary:** MLLMs have been successfully applied to multimodal embedding tasks, yet their generative reasoning capabilities remain underutilized. Directly incorporating chain-of-thought reasoning into embedding learning introduces two fundamental challenges. First, structural misalignment between instance-level reasoning and pairwise contrastive supervision may lead to shortcut behavior, where the model merely learns the superficial format of reasoning. Second, reasoning is not universally beneficial for em...

---

### 4. Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement

**Authors:** Qimin Zhong, Hao Liao, Haiming Qin, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06155v1)

**Summary:** Whether Large Language Models (LLMs) develop coherent internal world models remains a core debate. While conventional Next-Token Prediction (NTP) focuses on one-step-ahead supervision, Multi-Token Prediction (MTP) has shown promise in learning more structured representations. In this work, we provide a theoretical perspective analyzing the gradient inductive bias of MTP, supported by empirical evidence, showing that MTP promotes the convergence toward internal belief states by inducing represent...

---

### 5. Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT) for AI Systems Operating Across Enterprise and Geopolitical Boundaries

**Authors:** Andrew Kurtz, Klaudia Krawiecka

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06148v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06148v1)

**Summary:** The governance of artificial intelligence has a blind spot: the machine identities that AI systems use to act. AI agents, service accounts, API tokens, and automated workflows now outnumber human identities in enterprise environments by ratios exceeding 80 to 1, yet no integrated framework exists to govern them. A single ungoverned automated agent produced $5.4-10 billion in losses in the 2024 CrowdStrike outage; nation-state actors including Silk Typhoon and Salt Typhoon have operationalized un...

---

### 6. Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization

**Authors:** Yanis Labrak, David Grünert, Séverin Baroudi, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06138v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06138v1)

**Summary:** Long-context audio reasoning is underserved in both training data and evaluation. Existing benchmarks target short-context tasks, and the open-ended generation tasks most relevant to long-context reasoning pose well-known challenges for automatic evaluation. We propose a synthetic data generation pipeline designed to serve both as a training resource and as a controlled evaluation environment, and instantiate it for first-visit doctor-patient conversations with SOAP note generation as the task. ...

---

### 7. Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks

**Authors:** Basil Kyriacou, Viktoria Patapovich, Maniraman Periyasamy, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06135v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06135v1)

**Summary:** Efficient data loading remains a bottleneck for near-term quantum machine-learning. Existing schemes (angle, amplitude, and basis encoding) either underuse the exponential Hilbert-space capacity or require circuit depths that exceed the coherence budgets of noisy intermediate-scale quantum hardware. We introduce Shot-Based Quantum Encoding (SBQE), a data embedding strategy that distributes the hardware's native resource, shots, according to a data-dependent classical distribution over multiple i...

---

### 8. Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents

**Authors:** Bowen Ye, Rang Li, Qibin Yang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06132v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06132v1)

**Summary:** Large language models are increasingly deployed as autonomous agents executing multi-step workflows in real-world software environments. However, existing agent benchmarks suffer from three critical limitations: (1) trajectory-opaque grading that checks only final outputs, (2) underspecified safety and robustness evaluation, and (3) narrow modality coverage and interaction paradigms. We introduce Claw-Eval, an end-to-end evaluation suite addressing all three gaps. It comprises 300 human-verified...

---

### 9. PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer

**Authors:** David Picard, Nicolas Dufour, Lucas Degeorge, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06129v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06129v1)

**Summary:** This paper introduces the Polynomial Mixer (PoM), a novel token mixing mechanism with linear complexity that serves as a drop-in replacement for self-attention. PoM aggregates input tokens into a compact representation through a learned polynomial function, from which each token retrieves contextual information. We prove that PoM satisfies the contextual mapping property, ensuring that transformers equipped with PoM remain universal sequence-to-sequence approximators. We replace standard self-at...

---

### 10. Gym-Anything: Turn any Software into an Agent Environment

**Authors:** Pranjal Aggarwal, Graham Neubig, Sean Welleck

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06126v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06126v1)

**Summary:** Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However, current research has largely focused on short-horizon tasks over a limited set of software with limited economic value, such as basic e-commerce and OS-configuration tasks. A key reason is that creating environments for complex software requires significant time and human effort, and therefore does not scale. To address this, we introduce Gym-Anything, a framework for converting any softwar...

---

### 11. Lightweight Multimodal Adaptation of Vision Language Models for Species Recognition and Habitat Context Interpretation in Drone Thermal Imagery

**Authors:** Hao Chen, Fang Qiu, Fangchao Dong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06124v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06124v1)

**Summary:** This study proposes a lightweight multimodal adaptation framework to bridge the representation gap between RGB-pretrained VLMs and thermal infrared imagery, and demonstrates its practical utility using a real drone-collected dataset. A thermal dataset was developed from drone-collected imagery and was used to fine-tune VLMs through multimodal projector alignment, enabling the transfer of information from RGB-based visual representations to thermal radiometric inputs. Three representative models,...

---

### 12. ACE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments

**Authors:** Wang Yang, Chaoda Song, Xinpeng Li, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06111v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06111v1)

**Summary:** Existing Agent benchmarks suffer from two critical limitations: high environment interaction overhead (up to 41\% of total evaluation time) and imbalanced task horizon and difficulty distributions that make aggregate scores unreliable. To address these issues, we propose ACE-Bench built around a unified grid-based planning task, where agents must fill hidden slots in a partially completed schedule subject to both local slot constraints and global constraints. Our benchmark offers fine-grained co...

---

### 13. Artificial Intelligence and the Structure of Mathematics

**Authors:** Maissam Barkeshli, Michael R. Douglas, Michael H. Freedman

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06107v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06107v1)

**Summary:** Recent progress in artificial intelligence (AI) is unlocking transformative capabilities for mathematics. There is great hope that AI will help solve major open problems and autonomously discover new mathematical concepts. In this essay, we further consider how AI may open a grand perspective on mathematics by forging a new route, complementary to mathematical\textbf{ logic,} to understanding the global structure of formal \textbf{proof}\textbf{s}. We begin by providing a sketch of the formal st...

---

### 14. LLM4CodeRE: Generative AI for Code Decompilation Analysis and Reverse Engineering

**Authors:** Hamed Jelodar, Samita Bai, Tochukwu Emmanuel Nwankwo, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06095v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06095v1)

**Summary:** Code decompilation analysis is a fundamental yet challenging task in malware reverse engineering, particularly due to the pervasive use of sophisticated obfuscation techniques. Although recent large language models (LLMs) have shown promise in translating low-level representations into high-level source code, most existing approaches rely on generic code pretraining and lack adaptation to malicious software. We propose LLM4CodeRE, a domain-adaptive LLM framework for bidirectional code reverse en...

---

### 15. Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives

**Authors:** Changgeon Ko, Jisu Shin, Hoyun Song, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06091v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06091v1)

**Summary:** Large language model (LLM) agents are increasingly acting as human delegates in multi-agent environments, where a representative agent integrates diverse peer perspectives to make a final decision. Drawing inspiration from social psychology, we investigate how the reliability of this representative agent is undermined by the social context of its network. We define four key phenomena-social conformity, perceived expertise, dominant speaker effect, and rhetorical persuasion-and systematically man...

---

### 16. LAG-XAI: A Lie-Inspired Affine Geometric Framework for Interpretable Paraphrasing in Transformer Latent Spaces

**Authors:** Olexander Mazurets, Olexander Barmak, Leonid Bedratyuk, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06086v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06086v1)

**Summary:** Modern Transformer-based language models achieve strong performance in natural language processing tasks, yet their latent semantic spaces remain largely uninterpretable black boxes. This paper introduces LAG-XAI (Lie Affine Geometry for Explainable AI), a novel geometric framework that models paraphrasing not as discrete word substitutions, but as a structured affine transformation within the embedding space. By conceptualizing paraphrasing as a continuous geometric flow on a semantic manifold,...

---

### 17. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning

**Authors:** Juekai Lin, Yun Zhu, Honglin Lin, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06079v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06079v1)

**Summary:** Graphics Program Synthesis is pivotal for interpreting and editing visual data, effectively facilitating the reverse-engineering of static visuals into editable TikZ code. While TikZ is the de facto standard for scientific schematics due to its programmatic flexibility, its requirement for rigorous spatial precision presents a significant challenge for Multimodal Large Language Models. Progress is currently stifled by two primary gaps: (1) Data Quality Gap: existing image-TikZ corpora often lack...

---

### 18. Graph-PiT: Enhancing Structural Coherence in Part-Based Image Synthesis via Graph Priors

**Authors:** Junbin Zhang, Meng Cao, Feng Tan, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06074v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06074v1)

**Summary:** Achieving fine-grained and structurally sound controllability is a cornerstone of advanced visual generation. Existing part-based frameworks treat user-provided parts as an unordered set and therefore ignore their intrinsic spatial and semantic relationships, which often results in compositions that lack structural integrity. To bridge this gap, we propose Graph-PiT, a framework that explicitly models the structural dependencies of visual components using a graph prior. Specifically, we represen...

---

### 19. Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles

**Authors:** Ben Wigler, Maria Tsfasman, Tiffany Matej Hrkalovic

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06071v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06071v1)

**Summary:** Personality traits are richly encoded in natural language, and large language models (LLMs) trained on human text can simulate personality when conditioned on persona descriptions. However, existing evaluations rely predominantly on questionnaire self-report by the conditioned model, are limited in architectural diversity, and rarely use real human psychometric data. Without addressing these limitations, it remains unclear whether personality conditioning produces psychometrically informative re...

---

### 20. A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models

**Authors:** Maria Mahbub, Gregory M. Dams, Josh Arnold, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06028v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06028v1)

**Summary:** Large language models (LLMs) show promise for extracting clinically meaningful information from unstructured health records, yet their translation into real-world settings is constrained by the lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily on annotation-intensive reference standards or incomplete structured data, limiting feasibility at population scale. We propose a multi-stage validation framework for LLM-based clinical information extract...

---

### 21. CritBench: A Framework for Evaluating Cybersecurity Capabilities of Large Language Models in IEC 61850 Digital Substation Environments

**Authors:** Gustav Keppler, Moritz Gstür, Veit Hagenmeyer

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06019v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06019v1)

**Summary:** The advancement of Large Language Models (LLMs) has raised concerns regarding their dual-use potential in cybersecurity. Existing evaluation frameworks overwhelmingly focus on Information Technology (IT) environments, failing to capture the constraints, and specialized protocols of Operational Technology (OT). To address this gap, we introduce CritBench, a novel framework designed to evaluate the cybersecurity capabilities of LLM agents within IEC 61850 Digital Substation environments. We assess...

---

### 22. Governance and Regulation of Artificial Intelligence in Developing Countries: A Case Study of Nigeria

**Authors:** Uloma Okoro, Tammy Mckenzie, Branislav Radeljic

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06018v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06018v1)

**Summary:** This study examines the perception of legal professionals on the governance of AI in developing countries, using Nigeria as a case study. The study focused on ethical risks, regulatory gaps, and institutional readiness. The study adopted a qualitative case study design. Data were collected through 27 semi-structured interviews with legal practitioners in Nigeria. A focus group discussion was also held with seven additional legal practitioners across sectors such as finance, insurance, and corpor...

---

### 23. How LLMs Follow Instructions: Skillful Coordination, Not a Universal Mechanism

**Authors:** Elisabetta Rocchetti, Alfio Ferrara

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06015v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06015v1)

**Summary:** Instruction tuning is commonly assumed to endow language models with a domain-general ability to follow instructions, yet the underlying mechanism remains poorly understood. Does instruction-following rely on a universal mechanism or compositional skill deployment? We investigate this through diagnostic probing across nine diverse tasks in three instruction-tuned models.   Our analysis provides converging evidence against a universal mechanism. First, general probes trained across all tasks cons...

---

### 24. Epistemic Blinding: An Inference-Time Protocol for Auditing Prior Contamination in LLM-Assisted Analysis

**Authors:** Michael Cuccarese

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06013v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06013v1)

**Summary:** This paper presents epistemic blinding in the context of an agentic system that uses large language models to reason across multiple biological datasets for drug target prioritization. During development, it became apparent that LLM outputs silently blend data-driven inference with memorized priors about named entities - and the blend is invisible: there is no way to determine, from a single output, how much came from the data on the page and how much came from the model's training memory. Epist...

---

### 25. The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models

**Authors:** Xiaojie Gu, Ziying Huang, Weicong Hong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05995v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05995v1)

**Summary:** Large Language Models (LLMs) internalize vast world knowledge as parametric memory, yet inevitably inherit the staleness and errors of their source corpora. Consequently, ensuring the reliability and malleability of these internal representations is imperative for trustworthy real-world deployment. Knowledge editing offers a pivotal paradigm for surgically modifying memory without retraining. However, while recent editors demonstrate high success rates on standard benchmarks, it remains question...

---

### 26. Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains

**Authors:** Eranga Bandara, Ross Gore, Sachin Shetty, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05987v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05987v1)

**Summary:** Retail supply chain operations in supermarket chains involve continuous, high-volume manual workflows spanning demand forecasting, procurement, supplier coordination, and inventory replenishment, processes that are repetitive, decision-intensive, and difficult to scale without significant human effort. Despite growing investment in data analytics, the decision-making and coordination layers of these workflows remain predominantly manual, reactive, and fragmented across outlets, distribution cent...

---

### 27. A Formal Security Framework for MCP-Based AI Agents: Threat Taxonomy, Verification Models, and Defense Mechanisms

**Authors:** Nirajan Acharya, Gaurav Kumar Gupta

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05969v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05969v1)

**Summary:** The Model Context Protocol (MCP), introduced by Anthropic in November 2024 and now governed by the Linux Foundation's Agentic AI Foundation, has rapidly become the de facto standard for connecting large language model (LLM)-based agents to external tools and data sources, with over 97 million monthly SDK downloads and more than 177000 registered tools. However, this explosive adoption has exposed a critical gap: the absence of a unified, formal security framework capable of systematically charac...

---

### 28. Beyond Compromise: Pareto-Lenient Consensus for Efficient Multi-Preference LLM Alignment

**Authors:** Renxuan Tan, Rongpeng Li, Zhifeng Zhao, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05965v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05965v1)

**Summary:** Transcending the single-preference paradigm, aligning LLMs with diverse human values is pivotal for robust deployment. Contemporary Multi-Objective Preference Alignment (MPA) approaches predominantly rely on static linear scalarization or rigid gradient projection to navigate these trade-offs. However, by enforcing strict conflict avoidance or simultaneous descent, these paradigms often prematurely converge to local stationary points. While mathematically stable, these points represent a conserv...

---

### 29. Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution

**Authors:** Kai Yu, Zhenhao Zhou, Junhao Zeng, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05955v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05955v1)

**Summary:** Repository-level issue resolution benchmarks have become a standard testbed for evaluating LLM-based agents, yet success is still predominantly measured by test pass rates. In practice, however, acceptable patches must also comply with project-specific design constraints, such as architectural conventions, error-handling policies, and maintainability requirements, which are rarely encoded in tests and are often documented only implicitly in code review discussions. This paper introduces \textit{...

---

### 30. Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences

**Authors:** Pasin Manurangsi, Krzysztof Sornat

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05953v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05953v1)

**Summary:** We present a polynomial-time algorithm for computing an optimal committee of size $k$ under any given Thiele voting rule for elections on the Voter Interval domain (i.e., when voters can be ordered so that each candidate is approved by a consecutive voters). Our result extends to the Generalized Thiele rule, in which each voter has an individual weight (scoring) sequence. This resolves a 10-year-old open problem that was originally posed for Proportional Approval Voting and later extended to eve...

---

### 31. Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Confidence Estimation and Calibration

**Authors:** Yi Yuan, Xuhong Wang, Shanzhe Lei

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05952v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05952v1)

**Summary:** As agent-based systems continue to evolve, deep research agents are capable of automatically generating research-style reports across diverse domains. While these agents promise to streamline information synthesis and knowledge exploration, existing evaluation frameworks-typically based on subjective dimensions-fail to capture a critical aspect of report quality: trustworthiness. In open-ended research scenarios where ground-truth answers are unavailable, current evaluation methods cannot effect...

---

### 32. MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning

**Authors:** Maria Nesterova, Mikhail Kolosov, Anton Andreychuk, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05943v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05943v1)

**Summary:** Recent advances in multi-agent reinforcement learning (MARL) have demonstrated success in numerous challenging domains and environments, but typically require specialized models for each task. In this work, we propose a coherent methodology that makes it possible for a single GPT-based model to learn and perform well across diverse MARL environments and tasks, including StarCraft Multi-Agent Challenge, Google Research Football and POGEMA. Our method, MARL-GPT, applies offline reinforcement learn...

---

### 33. Context-Value-Action Architecture for Value-Driven Large Language Model Agents

**Authors:** TianZe Zhang, Sirui Sun, Yuhang Xie, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05939v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05939v1)

**Summary:** Large Language Models (LLMs) have shown promise in simulating human behavior, yet existing agents often exhibit behavioral rigidity, a flaw frequently masked by the self-referential bias of current "LLM-as-a-judge" evaluations. By evaluating against empirical ground truth, we reveal a counter-intuitive phenomenon: increasing the intensity of prompt-driven reasoning does not enhance fidelity but rather exacerbates value polarization, collapsing population diversity. To address this, we propose th...

---

### 34. Saliency-Guided Representation with Consistency Policy Learning for Visual Unsupervised Reinforcement Learning

**Authors:** Jingbo Sun, Qichao Zhang, Songjun Tu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05931v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05931v1)

**Summary:** Zero-shot unsupervised reinforcement learning (URL) offers a promising direction for building generalist agents capable of generalizing to unseen tasks without additional supervision. Among existing approaches, successor representations (SR) have emerged as a prominent paradigm due to their effectiveness in structured, low-dimensional settings. However, SR methods struggle to scale to high-dimensional visual environments. Through empirical analysis, we identify two key limitations of SR in visua...

---

### 35. "I See What You Did There": Can Large Vision-Language Models Understand Multimodal Puns?

**Authors:** Naen Xu, Jiayi Sheng, Changjiang Li, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05930v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05930v1)

**Summary:** Puns are a common form of rhetorical wordplay that exploits polysemy and phonetic similarity to create humor. In multimodal puns, visual and textual elements synergize to ground the literal sense and evoke the figurative meaning simultaneously. Although Vision-Language Models (VLMs) are widely used in multimodal understanding and generation, their ability to understand puns has not been systematically studied due to a scarcity of rigorous benchmarks. To address this, we first propose a multimoda...

---

### 36. ReLU Networks for Exact Generation of Similar Graphs

**Authors:** Mamoona Ghafoor, Tatsuya Akutsu

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05929v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05929v1)

**Summary:** Generation of graphs constrained by a specified graph edit distance from a source graph is important in applications such as cheminformatics, network anomaly synthesis, and structured data augmentation. Despite the growing demand for such constrained generative models in areas including molecule design and network perturbation analysis, the neural architectures required to provably generate graphs within a bounded graph edit distance remain largely unexplored. In addition, existing graph generat...

---

### 37. Selective Aggregation of Attention Maps Improves Diffusion-Based Visual Interpretation

**Authors:** Jungwon Park, Jungmin Ko, Dongnam Byun, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05906v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05906v1)

**Summary:** Numerous studies on text-to-image (T2I) generative models have utilized cross-attention maps to boost application performance and interpret model behavior. However, the distinct characteristics of attention maps from different attention heads remain relatively underexplored. In this study, we show that selectively aggregating cross-attention maps from heads most relevant to a target concept can improve visual interpretability. Compared to the diffusion-based segmentation method DAAM, our approac...

---

### 38. HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference

**Authors:** Bowen Zeng, Feiyang Ren, Jun Zhang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05887v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05887v1)

**Summary:** Multimodal Large Language Models (MLLMs) have advanced unified reasoning over text, images, and videos, but their inference is hindered by the rapid growth of key-value (KV) caches. Each visual input expands into thousands of tokens, causing caches to scale linearly with context length and remain resident in GPU memory throughout decoding, which leads to prohibitive memory overhead and latency even on high-end GPUs. A common solution is to compress caches under a fixed allocated budget at differ...

---

### 39. Automatic dental superimposition of 3D intraorals and 2D photographs for human identification

**Authors:** Antonio D. Villegas-Yeguas, Xavier Abreau-Freire, Guillermo R-García, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05877v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05877v1)

**Summary:** Dental comparison is considered a primary identification method, at the level of fingerprints and DNA profiling. One crucial but time-consuming step of this method is the morphological comparison. One of the main challenges to apply this method is the lack of ante-mortem medical records, specially on scenarios such as migrant death at the border and/or in countries where there is no universal healthcare. The availability of photos on social media where teeth are visible has led many odontologist...

---

### 40. Joint Knowledge Base Completion and Question Answering by Combining Large Language Models and Small Language Models

**Authors:** Yinan Liu, Dongying Lin, Sigang Luo, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05875v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05875v1)

**Summary:** Knowledge Bases (KBs) play a key role in various applications. As two representative KB-related tasks, knowledge base completion (KBC) and knowledge base question answering (KBQA) are closely related and inherently complementary with each other. Thus, it will be beneficial to solve the task of joint KBC and KBQA to make them reinforce each other. However, existing studies usually rely on the small language model (SLM) to enhance them jointly, and the large language model (LLM)'s strong reasoning...

---

### 41. Swiss-Bench 003: Evaluating LLM Reliability and Adversarial Security for Swiss Regulatory Contexts

**Authors:** Fatih Uenal

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05872v1)

**Summary:** The deployment of large language models (LLMs) in Swiss financial and regulatory contexts demands empirical evidence of both production reliability and adversarial security, dimensions not jointly operationalized in existing Swiss-focused evaluation frameworks. This paper introduces Swiss-Bench 003 (SBP-003), extending the HAAS (Helvetic AI Assessment Score) from six to eight dimensions by adding D7 (Self-Graded Reliability Proxy) and D8 (Adversarial Security). I evaluate ten frontier models acr...

---

### 42. JTON: A Token-Efficient JSON Superset with Zen Grid Tabular Encoding for Large Language Models

**Authors:** Gowthamkumar Nandakishore

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05865v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05865v1)

**Summary:** When LLMs process structured data, the serialization format directly affects cost and context utilization. Standard JSON wastes tokens repeating key names in every row of a tabular array--overhead that scales linearly with row count. This paper presents JTON (JSON Tabular Object Notation), a strict JSON superset whose main idea, Zen Grid, factors column headers into a single row and encodes values with semicolons, preserving JSON's type system while cutting redundancy. Across seven real-world do...

---

### 43. When Do We Need LLMs? A Diagnostic for Language-Driven Bandits

**Authors:** Uljad Berdica, Fernando Acero, Anton Ipsen, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05859v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05859v1)

**Summary:** We study Contextual Multi-Armed Bandits (CMABs) for non-episodic sequential decision making problems where the context includes both textual and numerical information (e.g., recommendation systems, dynamic portfolio adjustments, offer selection; all frequent problems in finance). While Large Language Models (LLMs) are increasingly applied to these settings, utilizing LLMs for reasoning at every decision step is computationally expensive and uncertainty estimates are difficult to obtain. To addre...

---

### 44. Neural Network Pruning via QUBO Optimization

**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05856v1)

**Summary:** Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic im...

---

### 45. Deep Researcher Agent: An Autonomous Framework for 24/7 Deep Learning Experimentation with Zero-Cost Monitoring

**Authors:** Xiangyue Zhang

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05854v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05854v1)

**Summary:** We present \textbf{Deep Researcher Agent}, an open-source framework that enables large language model (LLM) agents to autonomously conduct deep learning experiments around the clock. Unlike existing AI research assistants that focus on paper writing or code generation, our system addresses the full experiment lifecycle: hypothesis formation, code implementation, training execution, result analysis, and iterative refinement. The framework introduces three key innovations: (1) \textbf{Zero-Cost Mo...

---

### 46. Evaluating Learner Representations for Differentiation Prior to Instructional Outcomes

**Authors:** Junsoo Park, Youssef Medhat, Htet Phyo Wai, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05848v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05848v1)

**Summary:** Learner representations play a central role in educational AI systems, yet it is often unclear whether they preserve meaningful differences between students when instructional outcomes are unavailable or highly context-dependent. This work examines how to evaluate learner representations based on whether they retain separation between learners under a shared comparison rule. We introduce distinctiveness, a representation-level measure that evaluates how each learner differs from others in the co...

---

### 47. EEG-MFTNet: An Enhanced EEGNet Architecture with Multi-Scale Temporal Convolutions and Transformer Fusion for Cross-Session Motor Imagery Decoding

**Authors:** Panagiotis Andrikopoulos, Siamak Mehrkanoon

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05843v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05843v1)

**Summary:** Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices, providing critical support for individuals with motor impairments. However, accurate motor imagery (MI) decoding from electroencephalography (EEG) remains challenging due to noise and cross-session variability. This study introduces EEG-MFTNet, a novel deep learning model based on the EEGNet architecture, enhanced with multi-scale temporal convolutions and a Transformer encoder stream. These comp...

---

### 48. Vision-Guided Iterative Refinement for Frontend Code Generation

**Authors:** Hannah Sansford, Derek H. C. Law, Wei Liu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05839v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05839v1)

**Summary:** Code generation with large language models often relies on multi-stage human-in-the-loop refinement, which is effective but very costly - particularly in domains such as frontend web development where the solution quality depends on rendered visual output. We present a fully automated critic-in-the-loop framework in which a vision-language model serves as a visual critic that provides structured feedback on rendered webpages to guide iterative refinement of generated code. Across real-world user...

---

### 49. "OK Aura, Be Fair With Me": Demographics-Agnostic Training for Bias Mitigation in Wake-up Word Detection

**Authors:** Fernando López, Paula Delgado-Santos, Pablo Gómez, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05830v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05830v1)

**Summary:** Voice-based interfaces are widely used; however, achieving fair Wake-up Word detection across diverse speaker populations remains a critical challenge due to persistent demographic biases. This study evaluates the effectiveness of demographics-agnostic training techniques in mitigating performance disparities among speakers of varying sex, age, and accent. We utilize the OK Aura database for our experiments, employing a training methodology that excludes demographic labels, which are reserved fo...

---

### 50. Reciprocal Trust and Distrust in Artificial Intelligence Systems: The Hard Problem of Regulation

**Authors:** Martino Maggetti

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05826v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05826v1)

**Summary:** Policy makers, scientists, and the public are increasingly confronted with thorny questions about the regulation of artificial intelligence (AI) systems. A key common thread concerns whether AI can be trusted and the factors that can make it more trustworthy in front of stakeholders and users. This is indeed crucial, as the trustworthiness of AI systems is fundamental for both democratic governance and for the development and deployment of AI. This article advances the discussion by arguing that...

---

## cs.CV

**50 papers**

### 1. Action Images: End-to-End Policy Learning via Multiview Video Generation

**Authors:** Haoyu Zhen, Zixian Gao, Qiao Sun, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06168v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06168v1)

**Summary:** World action models (WAMs) have emerged as a promising direction for robot policy learning, as they can leverage powerful video backbones to model the future states. However, existing approaches often rely on separate action modules, or use action representations that are not pixel-grounded, making it difficult to fully exploit the pretrained knowledge of video models and limiting transfer across viewpoints and environments. In this work, we present Action Images, a unified world action model th...

---

### 2. HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models

**Authors:** Reihaneh Zohrabi, Hosein Hasani, Akshita Gupta, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06165v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06165v1)

**Summary:** Large vision-language models can produce object hallucinations in image descriptions, highlighting the need for effective detection and mitigation strategies. Prior work commonly relies on the model's attention weights on visual tokens as a detection signal. We reveal that coarse-grained attention-based analysis is unreliable due to hidden confounders, specifically token position and object repetition in a description. This leads to Simpson's paradox: the attention trends reverse or disappear wh...

---

### 3. DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models

**Authors:** Zhengming Yu, Li Ma, Mingming He, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06161v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06161v1)

**Summary:** Most digital videos are stored in 8-bit low dynamic range (LDR) formats, where much of the original high dynamic range (HDR) scene radiance is lost due to saturation and quantization. This loss of highlight and shadow detail precludes mapping accurate luminance to HDR displays and limits meaningful re-exposure in post-production workflows. Although techniques have been proposed to convert LDR images to HDR through dynamic range expansion, they struggle to restore realistic detail in the over- an...

---

### 4. The Character Error Vector: Decomposable errors for page-level OCR evaluation

**Authors:** Jonathan Bourne, Mwiza Simbeye, Joseph Nockels

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06160v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06160v1)

**Summary:** The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often not the case. Under page-parsing errors, CER becomes undefined, limiting its use as a metric and making evaluating page-level OCR challenging, particularly when using data that do not share a labelling schema. We introduce the Character Error Vector (CEV), a bag-of-characters evaluator for OCR. The CEV c...

---

### 5. MMEmb-R1: Reasoning-Enhanced Multimodal Embedding with Pair-Aware Selection and Adaptive Control

**Authors:** Yuchi Wang, Haiyang Yu, Weikang Bian, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06156v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06156v1)

**Summary:** MLLMs have been successfully applied to multimodal embedding tasks, yet their generative reasoning capabilities remain underutilized. Directly incorporating chain-of-thought reasoning into embedding learning introduces two fundamental challenges. First, structural misalignment between instance-level reasoning and pairwise contrastive supervision may lead to shortcut behavior, where the model merely learns the superficial format of reasoning. Second, reasoning is not universally beneficial for em...

---

### 6. PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer

**Authors:** David Picard, Nicolas Dufour, Lucas Degeorge, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06129v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06129v1)

**Summary:** This paper introduces the Polynomial Mixer (PoM), a novel token mixing mechanism with linear complexity that serves as a drop-in replacement for self-attention. PoM aggregates input tokens into a compact representation through a learned polynomial function, from which each token retrieves contextual information. We prove that PoM satisfies the contextual mapping property, ensuring that transformers equipped with PoM remain universal sequence-to-sequence approximators. We replace standard self-at...

---

### 7. Lightweight Multimodal Adaptation of Vision Language Models for Species Recognition and Habitat Context Interpretation in Drone Thermal Imagery

**Authors:** Hao Chen, Fang Qiu, Fangchao Dong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06124v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06124v1)

**Summary:** This study proposes a lightweight multimodal adaptation framework to bridge the representation gap between RGB-pretrained VLMs and thermal infrared imagery, and demonstrates its practical utility using a real drone-collected dataset. A thermal dataset was developed from drone-collected imagery and was used to fine-tune VLMs through multimodal projector alignment, enabling the transfer of information from RGB-based visual representations to thermal radiometric inputs. Three representative models,...

---

### 8. SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation

**Authors:** Hiba Dahmani, Nathan Piasco, Moussab Bennehar, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06113v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06113v1)

**Summary:** Scalable generation of outdoor driving scenes requires 3D representations that remain consistent across multiple viewpoints and scale to large areas. Existing solutions either rely on image or video generative models distilled to 3D space, harming the geometric coherence and restricting the rendering to training views, or are limited to small-scale 3D scene or object-centric generation. In this work, we propose a 3D generative framework based on $Σ$-Voxfield grid, a discrete representation where...

---

### 9. Extending ZACH-ViT to Robust Medical Imaging: Corruption and Adversarial Stress Testing in Low-Data Regimes

**Authors:** Athanasios Angelakis, Marta Gomez-Barrero

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06099v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06099v1)

**Summary:** The recently introduced ZACH-ViT (Zero-token Adaptive Compact Hierarchical Vision Transformer) formalized a compact permutation-invariant Vision Transformer for medical imaging and argued that architectural alignment with spatial structure can matter more than universal benchmark dominance. Its design was motivated by the observation that positional embeddings and a dedicated class token encode fixed spatial assumptions that may be suboptimal when spatial organization is weakly informative, loca...

---

### 10. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning

**Authors:** Juekai Lin, Yun Zhu, Honglin Lin, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06079v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06079v1)

**Summary:** Graphics Program Synthesis is pivotal for interpreting and editing visual data, effectively facilitating the reverse-engineering of static visuals into editable TikZ code. While TikZ is the de facto standard for scientific schematics due to its programmatic flexibility, its requirement for rigorous spatial precision presents a significant challenge for Multimodal Large Language Models. Progress is currently stifled by two primary gaps: (1) Data Quality Gap: existing image-TikZ corpora often lack...

---

### 11. Graph-PiT: Enhancing Structural Coherence in Part-Based Image Synthesis via Graph Priors

**Authors:** Junbin Zhang, Meng Cao, Feng Tan, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06074v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06074v1)

**Summary:** Achieving fine-grained and structurally sound controllability is a cornerstone of advanced visual generation. Existing part-based frameworks treat user-provided parts as an unordered set and therefore ignore their intrinsic spatial and semantic relationships, which often results in compositions that lack structural integrity. To bridge this gap, we propose Graph-PiT, a framework that explicitly models the structural dependencies of visual components using a graph prior. Specifically, we represen...

---

### 12. CoStream: Codec-Guided Resource-Efficient System for Video Streaming Analytics

**Authors:** Yulin Zou, Yan Chen, Wenyan Chen, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06036v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06036v1)

**Summary:** Video streaming analytics is a crucial workload for vision-language model serving, but the high cost of multimodal inference limits scalability. Prior systems reduce inference cost by exploiting temporal and spatial redundancy in video streams, but they target either the vision transformer (ViT) or the LLM with a limited view, leaving end-to-end opportunities untapped. Moreover, existing methods incur significant overhead to identify redundancy, either through offline profiling and training or c...

---

### 13. Toward Aristotelian Medical Representations: Backpropagation-Free Layer-wise Analysis for Interpretable Generalized Metric Learning on MedMNIST

**Authors:** Michael Karnes, Alper Yilmaz

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06017v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06017v1)

**Summary:** While deep learning has achieved remarkable success in medical imaging, the "black-box" nature of backpropagation-based models remains a significant barrier to clinical adoption. To bridge this gap, we propose Aristotelian Rapid Object Modeling (A-ROM), a framework built upon the Platonic Representation Hypothesis (PRH). This hypothesis posits that models trained on vast, diverse datasets converge toward a universal and objective representation of reality. By leveraging the generalizable metric ...

---

### 14. OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control

**Authors:** Yukun Wang, Ruihuang Li, Jiale Tao, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06010v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06010v1)

**Summary:** Video fundamentally intertwines two crucial axes: the dynamic content of a scene and the camera motion through which it is observed. However, existing generation models often entangle these factors, limiting independent control. In this work, we introduce OmniCamera, a unified framework designed to explicitly disentangle and command these two dimensions. This compositional approach enables flexible video generation by allowing arbitrary pairings of camera and content conditions, unlocking unprec...

---

### 15. Is CLIP Cross-Eyed? Revealing and Mitigating Center Bias in the CLIP Family

**Authors:** Oscar Chew, Hsiao-Ying Huang, Kunal Jain, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05971v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05971v1)

**Summary:** Recent research has shown that contrastive vision-language models such as CLIP often lack fine-grained understanding of visual content. While a growing body of work has sought to address this limitation, we identify a distinct failure mode in the CLIP family, which we term center bias, that persists even in recent model variants. Specifically, CLIP tends to disproportionately focus on the central region of an image, overlooking important objects located near the boundaries. This limitation is fu...

---

### 16. HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation

**Authors:** Tao Hu, Varun Jampani

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05961v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05961v1)

**Summary:** Despite tremendous recent progress in human video generation, generative video diffusion models still struggle to capture the dynamics and physics of human motions faithfully. In this paper, we propose a new framework for human video generation, HumANDiff, which enhances the human motion control with three key designs: 1) Articulated motion-consistent noise sampling that correlates the spatiotemporal distribution of latent noise and replaces the unstructured random Gaussian noise with 3D articul...

---

### 17. Multi-Modal Landslide Detection from Sentinel-1 SAR and Sentinel-2 Optical Imagery Using Multi-Encoder Vision Transformers and Ensemble Learning

**Authors:** Ioannis Nasios

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05959v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05959v1)

**Summary:** Landslides represent a major geohazard with severe impacts on human life, infrastructure, and ecosystems, underscoring the need for accurate and timely detection approaches to support disaster risk reduction. This study proposes a modular, multi-model framework that fuses Sentinel-2 optical imagery with Sentinel-1 Synthetic Aperture Radar (SAR) data, for robust landslide detection. The methodology leverages multi-encoder vision transformers, where each data modality is processed through separate...

---

### 18. Mixture-of-Modality-Experts with Holistic Token Learning for Fine-Grained Multimodal Visual Analytics in Driver Action Recognition

**Authors:** Tianyi Liu, Yiming Li, Wenqian Wang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05947v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05947v1)

**Summary:** Robust multimodal visual analytics remains challenging when heterogeneous modalities provide complementary but input-dependent evidence for decision-making.Existing multimodal learning methods mainly rely on fixed fusion modules or predefined cross-modal interactions, which are often insufficient to adapt to changing modality reliability and to capture fine-grained action cues. To address this issue, we propose a Mixture-of-Modality-Experts (MoME) framework with a Holistic Token Learning (HTL) s...

---

### 19. Leveraging Image Editing Foundation Models for Data-Efficient CT Metal Artifact Reduction

**Authors:** Ahmet Rasim Emirdagi, Süleyman Aslan, Mısra Yavuz, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05934v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05934v1)

**Summary:** Metal artifacts from high-attenuation implants severely degrade CT image quality, obscuring critical anatomical structures and posing a challenge for standard deep learning methods that require extensive paired training data. We propose a paradigm shift: reframing artifact reduction as an in-context reasoning task by adapting a general-purpose vision-language diffusion foundation model via parameter-efficient Low-Rank Adaptation (LoRA). By leveraging rich visual priors, our approach achieves eff...

---

### 20. SonoSelect: Efficient Ultrasound Perception via Active Probe Exploration

**Authors:** Yixin Zhang, Yunzhong Hou, Longqi Li, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05933v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05933v1)

**Summary:** Ultrasound perception typically requires multiple scan views through probe movement to reduce diagnostic ambiguity, mitigate acoustic occlusions, and improve anatomical coverage. However, not all probe views are equally informative. Exhaustively acquiring a large number of views can introduce substantial redundancy, increase scanning and processing costs. To address this, we define an active view exploration task for ultrasound and propose SonoSelect, an ultrasound-specific method that adaptivel...

---

### 21. Saliency-Guided Representation with Consistency Policy Learning for Visual Unsupervised Reinforcement Learning

**Authors:** Jingbo Sun, Qichao Zhang, Songjun Tu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05931v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05931v1)

**Summary:** Zero-shot unsupervised reinforcement learning (URL) offers a promising direction for building generalist agents capable of generalizing to unseen tasks without additional supervision. Among existing approaches, successor representations (SR) have emerged as a prominent paradigm due to their effectiveness in structured, low-dimensional settings. However, SR methods struggle to scale to high-dimensional visual environments. Through empirical analysis, we identify two key limitations of SR in visua...

---

### 22. Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction

**Authors:** Yangyi Xiao, Siting Zhu, Baoquan Yang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05908v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05908v1)

**Summary:** Multi-traversal scene reconstruction is important for high-fidelity autonomous driving simulation and digital twin construction. This task involves integrating multiple sequences captured from the same geographical area at different times. In this context, a primary challenge is the significant appearance inconsistency across traversals caused by varying illumination and environmental conditions, despite the shared underlying geometry. This paper presents ADM-GS (Appearance Decomposition Gaussia...

---

### 23. Selective Aggregation of Attention Maps Improves Diffusion-Based Visual Interpretation

**Authors:** Jungwon Park, Jungmin Ko, Dongnam Byun, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05906v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05906v1)

**Summary:** Numerous studies on text-to-image (T2I) generative models have utilized cross-attention maps to boost application performance and interpret model behavior. However, the distinct characteristics of attention maps from different attention heads remain relatively underexplored. In this study, we show that selectively aggregating cross-attention maps from heads most relevant to a target concept can improve visual interpretability. Compared to the diffusion-based segmentation method DAAM, our approac...

---

### 24. AICA-Bench: Holistically Examining the Capabilities of VLMs in Affective Image Content Analysis

**Authors:** Dong She, Xianrong Yao, Liqun Chen, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05900v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05900v1)

**Summary:** Vision-Language Models (VLMs) have demonstrated strong capabilities in perception, yet holistic Affective Image Content Analysis (AICA), which integrates perception, reasoning, and generation into a unified framework, remains underexplored. To address this gap, we introduce AICA-Bench, a comprehensive benchmark with three core tasks: Emotion Understanding (EU), Emotion Reasoning (ER), and Emotion-Guided Content Generation (EGCG). We evaluate 23 VLMs and identify two major limitations: weak inten...

---

### 25. Physics-Aware Video Instance Removal Benchmark

**Authors:** Zirui Li, Xinghao Chen, Lingyu Jiang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05898v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05898v1)

**Summary:** Video Instance Removal (VIR) requires removing target objects while maintaining background integrity and physical consistency, such as specular reflections and illumination interactions. Despite advancements in text-guided editing, current benchmarks primarily assess visual plausibility, often overlooking the physical causalities, such as lingering shadows, triggered by object removal. We introduce the Physics-Aware Video Instance Removal (PVIR) benchmark, featuring 95 high-quality videos annota...

---

### 26. Automatic dental superimposition of 3D intraorals and 2D photographs for human identification

**Authors:** Antonio D. Villegas-Yeguas, Xavier Abreau-Freire, Guillermo R-García, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05877v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05877v1)

**Summary:** Dental comparison is considered a primary identification method, at the level of fingerprints and DNA profiling. One crucial but time-consuming step of this method is the morphological comparison. One of the main challenges to apply this method is the lack of ante-mortem medical records, specially on scenarios such as migrant death at the border and/or in countries where there is no universal healthcare. The availability of photos on social media where teeth are visible has led many odontologist...

---

### 27. Neural Network Pruning via QUBO Optimization

**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05856v1)

**Summary:** Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic im...

---

### 28. Reading Between the Pixels: An Inscriptive Jailbreak Attack on Text-to-Image Models

**Authors:** Zonghao Ying, Haowen Dai, Lianyu Hu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05853v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05853v1)

**Summary:** Modern text-to-image (T2I) models can now render legible, paragraph-length text, enabling a fundamentally new class of misuse. We identify and formalize the inscriptive jailbreak, where an adversary coerces a T2I system into generating images containing harmful textual payloads (e.g., fraudulent documents) embedded within visually benign scenes. Unlike traditional depictive jailbreaks that elicit visually objectionable imagery, inscriptive attacks weaponize the text-rendering capability itself. ...

---

### 29. Learn to Rank: Visual Attribution by Learning Importance Ranking

**Authors:** David Schinagl, Christian Fruhwirth-Reisinger, Alexander Prutsch, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05819v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05819v1)

**Summary:** Interpreting the decisions of complex computer vision models is crucial to establish trust and accountability, especially in safety-critical domains. An established approach to interpretability is generating visual attribution maps that highlight regions of the input most relevant to the model's prediction. However, existing methods face a three-way trade-off. Propagation-based approaches are efficient, but they can be biased and architecture-specific. Meanwhile, perturbation-based methods are c...

---

### 30. WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering

**Authors:** Yingjian Zhu, Xinming Wang, Kun Ding, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05818v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05818v1)

**Summary:** Multi-modal Retrieval-Augmented Generation (RAG) has emerged as a highly effective paradigm for Knowledge-Based Visual Question Answering (KB-VQA). Despite recent advancements, prevailing methods still primarily depend on images as the retrieval key, and often overlook or misplace the role of Vision-Language Models (VLMs), thereby failing to leverage their potential fully. In this paper, we introduce WikiSeeker, a novel multi-modal RAG framework that bridges these gaps by proposing a multi-modal...

---

### 31. EfficientMonoHair: Fast Strand-Level Reconstruction from Monocular Video via Multi-View Direction Fusion

**Authors:** Da Li, Dominik Engel, Deng Luo, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05794v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05794v1)

**Summary:** Strand-level hair geometry reconstruction is a fundamental problem in virtual human modeling and the digitization of hairstyles. However, existing methods still suffer from a significant trade-off between accuracy and efficiency. Implicit neural representations can capture the global hair shape but often fail to preserve fine-grained strand details, while explicit optimization-based approaches achieve high-fidelity reconstructions at the cost of heavy computation and poor scalability. To address...

---

### 32. BodhiPromptShield: Pre-Inference Prompt Mediation for Suppressing Privacy Propagation in LLM/VLM Agents

**Authors:** Bo Ma, Jinsong Wu, Weiqi Yan

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05793v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05793v1)

**Summary:** In LLM/VLM agents, prompt privacy risk propagates beyond a single model call because raw user content can flow into retrieval queries, memory writes, tool calls, and logs. Existing de-identification pipelines address document boundaries but not this cross-stage propagation. We propose BodhiPromptShield, a policy-aware framework that detects sensitive spans, routes them via typed placeholders, semantic abstraction, or secure symbolic mapping, and delays restoration to authorized boundaries. Relat...

---

### 33. Sparse Gain Radio Map Reconstruction With Geometry Priors and Uncertainty-Guided Measurement Selection

**Authors:** Zhihan Zeng, Ning Wei, Muhammad Baqer Mollah, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05788v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05788v1)

**Summary:** Radio maps are important for environment-aware wireless communication, network planning, and radio resource optimization. However, dense radio map construction remains challenging when only a limited number of measurements are available, especially in complex urban environments with strong blockages, irregular geometry, and restricted sensing accessibility. Existing methods have explored interpolation, low-rank cartography, deep completion, and channel knowledge map (CKM) construction, but many ...

---

### 34. RHVI-FDD: A Hierarchical Decoupling Framework for Low-Light Image Enhancement

**Authors:** Junhao Yang, Bo Yang, Hongwei Ge, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05781v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05781v1)

**Summary:** Low-light images often suffer from severe noise, detail loss, and color distortion, which hinder downstream multimedia analysis and retrieval tasks. The degradation in low-light images is complex: luminance and chrominance are coupled, while within the chrominance, noise and details are deeply entangled, preventing existing methods from simultaneously correcting color distortion, suppressing noise, and preserving fine details. To tackle the above challenges, we propose a novel hierarchical decou...

---

### 35. Sparsity-Aware Voxel Attention and Foreground Modulation for 3D Semantic Scene Completion

**Authors:** Yu Xue, Longjun Gao, Yuanqi Su, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05780v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05780v1)

**Summary:** Monocular Semantic Scene Completion (SSC) aims to reconstruct complete 3D semantic scenes from a single RGB image, offering a cost-effective solution for autonomous driving and robotics. However, the inherently imbalanced nature of voxel distributions, where over 93% of voxels are empty and foreground classes are rare, poses significant challenges. Existing methods often suffer from redundant emphasis on uninformative voxels and poor generalization to long-tailed categories. To address these iss...

---

### 36. PDMP: Rethinking Balanced Multimodal Learning via Performance-Dominant Modality Prioritization

**Authors:** Shicai Wei, Chunbo Luo, Qiang Zhu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05773v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05773v1)

**Summary:** Multimodal learning has attracted increasing attention due to its practicality. However, it often suffers from insufficient optimization, where the multimodal model underperforms even compared to its unimodal counterparts. Existing methods attribute this problem to the imbalanced learning between modalities and solve it by gradient modulation. This paper argues that balanced learning is not the optimal setting for multimodal learning. On the contrary, imbalanced learning driven by the performanc...

---

### 37. Beyond the Beep: Scalable Collision Anticipation and Real-Time Explainability with BADAS-2.0

**Authors:** Roni Goldshmidt, Hamish Scott, Lorenzo Niccolini, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05767v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05767v1)

**Summary:** We present BADAS-2.0, the second generation of our collision anticipation system, building on BADAS-1.0 [7], which showed that fine-tuning V-JEPA2 [1] on large-scale ego-centric dashcam data outperforms both academic baselines and production ADAS systems.   BADAS-2.0 advances the state of the art along three axes.   (i) Long-tail benchmark and accuracy: We introduce a 10-group long-tail benchmark targeting rare and safety-critical scenarios. To construct it, BADAS-1.0 is used as an active oracle...

---

### 38. Improving Controllable Generation: Faster Training and Better Performance via $x_0$-Supervision

**Authors:** Amadou S. Sangare, Adrien Maglo, Mohamed Chaouch, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05761v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05761v1)

**Summary:** Text-to-Image (T2I) diffusion/flow models have recently achieved remarkable progress in visual fidelity and text alignment. However, they remain limited when users need to precisely control image layouts, something that natural language alone cannot reliably express. Controllable generation methods augment the initial T2I model with additional conditions that more easily describe the scene. Prior works straightforwardly train the augmented network with the same loss as the initial network. Altho...

---

### 39. SVC 2026: the Second Multimodal Deception Detection Challenge and the First Domain Generalized Remote Physiological Measurement Challenge

**Authors:** Dongliang Zhu, Zhiyi Niu, Bo Zhao, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05748v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05748v1)

**Summary:** Subtle visual signals, although difficult to perceive with the naked eye, contain important information that can reveal hidden patterns in visual data. These signals play a key role in many applications, including biometric security, multimedia forensics, medical diagnosis, industrial inspection, and affective computing. With the rapid development of computer vision and representation learning techniques, detecting and interpreting such subtle signals has become an emerging research direction. H...

---

### 40. On the Robustness of Diffusion-Based Image Compression to Bit-Flip Errors

**Authors:** Amit Vaisman, Gal Pomerants, Raz Lapid

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05743v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05743v1)

**Summary:** Modern image compression methods are typically optimized for the rate--distortion--perception trade-off, whereas their robustness to bit-level corruption is rarely examined. We show that diffusion-based compressors built on the Reverse Channel Coding (RCC) paradigm are substantially more robust to bit flips than classical and learned codecs. We further introduce a more robust variant of Turbo-DDCM that significantly improves robustness while only minimally affecting the rate--distortion--percept...

---

### 41. ASSR-Net: Anisotropic Structure-Aware and Spectrally Recalibrated Network for Hyperspectral Image Fusion

**Authors:** Qiya Song, Hongzhi Zhou, Lishan Tan, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05742v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05742v1)

**Summary:** Hyperspectral image fusion aims to reconstruct high-spatial-resolution hyperspectral images (HR-HSI) by integrating complementary information from multi-source inputs. Despite recent progress, existing methods still face two critical challenges: (1) inadequate reconstruction of anisotropic spatial structures, resulting in blurred details and compromised spatial quality; and (2) spectral distortion during fusion, which hinders fine-grained spectral representation. To address these issues, we prop...

---

### 42. FoleyDesigner: Immersive Stereo Foley Generation with Precise Spatio-Temporal Alignment for Film Clips

**Authors:** Mengtian Li, Kunyan Dai, Yi Ding, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05731v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05731v1)

**Summary:** Foley art plays a pivotal role in enhancing immersive auditory experiences in film, yet manual creation of spatio-temporally aligned audio remains labor-intensive. We propose FoleyDesigner, a novel framework inspired by professional Foley workflows, integrating film clip analysis, spatio-temporally controllable Foley generation, and professional audio mixing capabilities. FoleyDesigner employs a multi-agent architecture for precise spatio-temporal analysis. It achieves spatio-temporal alignment ...

---

### 43. Single-Stage Signal Attenuation Diffusion Model for Low-Light Image Enhancement and Denoising

**Authors:** Ying Liu, Junchao Zhang, Caiyun Wu

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05727v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05727v1)

**Summary:** Diffusion models excel at image restoration via probabilistic modeling of forward noise addition and reverse denoising, and their ability to handle complex noise while preserving fine details makes them well-suited for Low-Light Image Enhancement (LLIE). Mainstream diffusion based LLIE methods either adopt a two-stage pipeline or an auxiliary correction network to refine U-Net outputs, which severs the intrinsic link between enhancement and denoising and leads to suboptimal performance owing to ...

---

### 44. Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP

**Authors:** Yusung Ro, Jaehyun Choi, Junmo Kim

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05724v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05724v1)

**Summary:** Sparse Autoencoders (SAEs) have emerged as a powerful tool for interpreting the internal representations of CLIP vision encoders, yet existing analyses largely focus on the semantic meaning of individual features. We introduce information scope as a complementary dimension of interpretability that characterizes how broadly an SAE feature aggregates visual evidence, ranging from localized, patch-specific cues to global, image-level signals. We observe that some SAE features respond consistently a...

---

### 45. GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

**Authors:** Weiqi Zhang, Junsheng Zhou, Haotian Geng, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05721v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05721v1)

**Summary:** 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors. Existing methods have explored predicting point maps as geometric references for inferring Gaussian primitives, while the unreliable estimated geometries may lead to poor generations. In this work, we introduce GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily ac...

---

### 46. MPM: Mutual Pair Merging for Efficient Vision Transformers

**Authors:** Simon Ravé, Pejman Rasti, David Rousseau

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05718v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05718v1)

**Summary:** Decreasing sequence length is a common way to accelerate transformers, but prior token reduction work often targets classification and reports proxy metrics rather than end-to-end latency. For semantic segmentation, token reduction is further constrained by the need to reconstruct dense, pixel-aligned features, and on modern accelerators the overhead of computing merge maps can erase expected gains. We propose Mutual Pair Merging (MPM), a training-free token aggregation module that forms mutual ...

---

### 47. In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting

**Authors:** Wenhui Xiao, Ethan Goan, Rodrigo Santa Cruz, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05715v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05715v1)

**Summary:** Using accurate depth priors in 3D Gaussian Splatting helps mitigate artifacts caused by sparse training data and textureless surfaces. However, acquiring accurate depth maps requires specialized acquisition systems. Foundation monocular depth estimation models offer a cost-effective alternative, but they suffer from scale ambiguity, multi-view inconsistency, and local geometric inaccuracies, which can degrade rendering performance when applied naively. This paper addresses the challenge of relia...

---

### 48. Let Geometry GUIDE: Layer-wise Unrolling of Geometric Priors in Multimodal LLMs

**Authors:** Chongyu Wang, Ting Huang, Chunyu Sun, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05695v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05695v1)

**Summary:** Multimodal Large Language Models (MLLMs) have achieved remarkable progress in 2D visual tasks but still exhibit limited physical spatial awareness when processing real-world visual streams. Recently, feed-forward geometric foundation models, which implicitly extract geometric priors, have provided a new pathway to address this issue. However, existing geometry-aware MLLMs are predominantly constrained by the paradigm of single deep-layer extraction and input-level fusion. This flattened fusion l...

---

### 49. CRFT: Consistent-Recurrent Feature Flow Transformer for Cross-Modal Image Registration

**Authors:** Xuecong Liu, Mengzhu Ding, Zixuan Sun, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05689v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05689v1)

**Summary:** We present Consistent-Recurrent Feature Flow Transformer (CRFT), a unified coarse-to-fine framework based on feature flow learning for robust cross-modal image registration. CRFT learns a modality-independent feature flow representation within a transformer-based architecture that jointly performs feature alignment and flow estimation. The coarse stage establishes global correspondences through multi-scale feature correlation, while the fine stage refines local details via hierarchical feature f...

---

### 50. 3D Smoke Scene Reconstruction Guided by Vision Priors from Multimodal Large Language Models

**Authors:** Xinye Zheng, Fei Wang, Yiqi Nie, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05687v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05687v1)

**Summary:** Reconstructing 3D scenes from smoke-degraded multi-view images is particularly difficult because smoke introduces strong scattering effects, view-dependent appearance changes, and severe degradation of cross-view consistency. To address these issues, we propose a framework that integrates visual priors with efficient 3D scene modeling. We employ Nano-Banana-Pro to enhance smoke-degraded images and provide clearer visual observations for reconstruction and develop Smoke-GS, a medium-aware 3D Gaus...

---

## cs.LG

**50 papers**

### 1. In-Place Test-Time Training

**Authors:** Guhao Feng, Shengjie Luo, Kai Hua, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06169v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06169v1)

**Summary:** The static ``train then deploy" paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks. Test-Time Training (TTT) offers a compelling alternative by updating a subset of model parameters (fast weights) at inference time, yet its potential in the current LLM ecosystem is hindered by critical barriers including architectural incompatibility, computational inefficiency and mi...

---

### 2. Topological Characterization of Churn Flow and Unsupervised Correction to the Wu Flow-Regime Map in Small-Diameter Vertical Pipes

**Authors:** Brady Koenig, Sushovan Majhi, Atish Mitra, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06167v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06167v1)

**Summary:** Churn flow-the chaotic, oscillatory regime in vertical two-phase flow-has lacked a quantitative mathematical definition for over $40$ years. We introduce the first topology-based characterization using Euler Characteristic Surfaces (ECS). We formulate unsupervised regime discovery as Multiple Kernel Learning (MKL), blending two complementary ECS-derived kernels-temporal alignment ($L^1$ distance on the $χ(s,t)$ surface) and amplitude statistics (scale-wise mean, standard deviation, max, min)-wit...

---

### 3. HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models

**Authors:** Reihaneh Zohrabi, Hosein Hasani, Akshita Gupta, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06165v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06165v1)

**Summary:** Large vision-language models can produce object hallucinations in image descriptions, highlighting the need for effective detection and mitigation strategies. Prior work commonly relies on the model's attention weights on visual tokens as a detection signal. We reveal that coarse-grained attention-based analysis is unreliable due to hidden confounders, specifically token position and object repetition in a description. This leads to Simpson's paradox: the attention trends reverse or disappear wh...

---

### 4. The Character Error Vector: Decomposable errors for page-level OCR evaluation

**Authors:** Jonathan Bourne, Mwiza Simbeye, Joseph Nockels

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06160v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06160v1)

**Summary:** The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often not the case. Under page-parsing errors, CER becomes undefined, limiting its use as a metric and making evaluating page-level OCR challenging, particularly when using data that do not share a labelling schema. We introduce the Character Error Vector (CEV), a bag-of-characters evaluator for OCR. The CEV c...

---

### 5. Target Policy Optimization

**Authors:** Jean Kaddour

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06159v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06159v1)

**Summary:** In RL, given a prompt, we sample a group of completions from a model and score them. Two questions follow: which completions should gain probability mass, and how should the parameters move to realize that change? Standard policy-gradient methods answer both at once, so the update can overshoot or undershoot depending on the learning rate, clipping, and other optimizer choices. We introduce \emph{Target Policy Optimization} (TPO), which separates the two questions. Given scored completions, TPO ...

---

### 6. Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement

**Authors:** Qimin Zhong, Hao Liao, Haiming Qin, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06155v1)

**Summary:** Whether Large Language Models (LLMs) develop coherent internal world models remains a core debate. While conventional Next-Token Prediction (NTP) focuses on one-step-ahead supervision, Multi-Token Prediction (MTP) has shown promise in learning more structured representations. In this work, we provide a theoretical perspective analyzing the gradient inductive bias of MTP, supported by empirical evidence, showing that MTP promotes the convergence toward internal belief states by inducing represent...

---

### 7. Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks

**Authors:** Basil Kyriacou, Viktoria Patapovich, Maniraman Periyasamy, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06135v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06135v1)

**Summary:** Efficient data loading remains a bottleneck for near-term quantum machine-learning. Existing schemes (angle, amplitude, and basis encoding) either underuse the exponential Hilbert-space capacity or require circuit depths that exceed the coherence budgets of noisy intermediate-scale quantum hardware. We introduce Shot-Based Quantum Encoding (SBQE), a data embedding strategy that distributes the hardware's native resource, shots, according to a data-dependent classical distribution over multiple i...

---

### 8. Gym-Anything: Turn any Software into an Agent Environment

**Authors:** Pranjal Aggarwal, Graham Neubig, Sean Welleck

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06126v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06126v1)

**Summary:** Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However, current research has largely focused on short-horizon tasks over a limited set of software with limited economic value, such as basic e-commerce and OS-configuration tasks. A key reason is that creating environments for complex software requires significant time and human effort, and therefore does not scale. To address this, we introduce Gym-Anything, a framework for converting any softwar...

---

### 9. A Large-Scale Empirical Comparison of Meta-Learners and Causal Forests for Heterogeneous Treatment Effect Estimation in Marketing Uplift Modeling

**Authors:** Aman Singh

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06123v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06123v1)

**Summary:** Estimating Conditional Average Treatment Effects (CATE) at the individual level is central to precision marketing, yet systematic benchmarking of uplift modeling methods at industrial scale remains limited. We present UpliftBench, an empirical evaluation of four CATE estimators: S-Learner, T-Learner, X-Learner (all with LightGBM base learners), and Causal Forest (EconML), applied to the Criteo Uplift v2.1 dataset comprising 13.98 million customer records. The near-random treatment assignment (pr...

---

### 10. Learning $\mathsf{AC}^0$ Under Graphical Models

**Authors:** Gautam Chandrasekaran, Jason Gaitonde, Ankur Moitra, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06109v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06109v1)

**Summary:** In a landmark result, Linial, Mansour and Nisan (J. ACM 1993) gave a quasipolynomial-time algorithm for learning constant-depth circuits given labeled i.i.d. samples under the uniform distribution. Their work has had a deep and lasting legacy in computational learning theory, in particular introducing the $\textit{low-degree algorithm}$. However, an important critique of many results and techniques in the area is the reliance on product structure, which is unlikely to hold in realistic settings....

---

### 11. Pixel-Translation-Equivariant Quantum Convolutional Neural Networks via Fourier Multiplexers

**Authors:** Dmitry Chirkov, Igor Lobanov

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06094v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06094v1)

**Summary:** Convolutional neural networks owe much of their success to hard-coding translation equivariance. Quantum convolutional neural networks (QCNNs) have been proposed as near-term quantum analogues, but the relevant notion of translation depends on the data encoding. For address/amplitude encodings such as FRQI, a pixel shift acts as modular addition on an index register, whereas many MERA-inspired QCNNs are equivariant only under cyclic permutations of physical qubits. We formalize this mismatch and...

---

### 12. eVTOL Aircraft Energy Overhead Estimation under Conflict Resolution in High-Density Airspaces

**Authors:** Alex Zongo, Peng Wei

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06093v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06093v1)

**Summary:** Electric vertical takeoff and landing (eVTOL) aircraft operating in high-density urban airspace must maintain safe separation through tactical conflict resolution, yet the energy cost of such maneuvers has not been systematically quantified. This paper investigates how conflict-resolution maneuvers under the Modified Voltage Potential (MVP) algorithm affect eVTOL energy consumption. Using a physics-based power model integrated within a traffic simulation, we analyze approximately 71,767 en route...

---

### 13. A machine learning framework for uncovering stochastic nonlinear dynamics from noisy data

**Authors:** Matteo Bosso, Giovanni Franzese, Kushal Swamy, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06081v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06081v1)

**Summary:** Modeling real-world systems requires accounting for noise - whether it arises from unpredictable fluctuations in financial markets, irregular rhythms in biological systems, or environmental variability in ecosystems. While the behavior of such systems can often be described by stochastic differential equations, a central challenge is understanding how noise influences the inference of system parameters and dynamics from data. Traditional symbolic regression methods can uncover governing equation...

---

### 14. Short Data, Long Context: Distilling Positional Knowledge in Transformers

**Authors:** Patrick Huber, Ernie Chang, Chinnadhurai Sankar, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06070v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06070v1)

**Summary:** Extending the context window of language models typically requires expensive long-context pre-training, posing significant challenges for both training efficiency and data collection. In this paper, we present evidence that long-context retrieval capabilities can be transferred to student models through logit-based knowledge distillation, even when training exclusively on packed short-context samples within a long-context window. We provide comprehensive insights through the lens of Rotary Posit...

---

### 15. Value Mirror Descent for Reinforcement Learning

**Authors:** Zhichao Jia, Guanghui Lan

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06039v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06039v1)

**Summary:** Value iteration-type methods have been extensively studied for computing a nearly optimal value function in reinforcement learning (RL). Under a generative sampling model, these methods can achieve sharper sample complexity than policy optimization approaches, particularly in their dependence on the discount factor. In practice, they are often employed for offline training or in simulated environments. In this paper, we consider discounted Markov decision processes with state space S, action spa...

---

### 16. CoStream: Codec-Guided Resource-Efficient System for Video Streaming Analytics

**Authors:** Yulin Zou, Yan Chen, Wenyan Chen, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06036v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06036v1)

**Summary:** Video streaming analytics is a crucial workload for vision-language model serving, but the high cost of multimodal inference limits scalability. Prior systems reduce inference cost by exploiting temporal and spatial redundancy in video streams, but they target either the vision transformer (ViT) or the LLM with a limited view, leaving end-to-end opportunities untapped. Moreover, existing methods incur significant overhead to identify redundancy, either through offline profiling and training or c...

---

### 17. Ensemble-Based Dirichlet Modeling for Predictive Uncertainty and Selective Classification

**Authors:** Courtney Franzen, Farhad Pourkamali-Anaraki

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06032v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06032v1)

**Summary:** Neural network classifiers trained with cross-entropy loss achieve strong predictive accuracy but lack the capability to provide inherent predictive uncertainty estimates, thus requiring external techniques to obtain these estimates. In addition, softmax scores for the true class can vary substantially across independent training runs, which limits the reliability of uncertainty-based decisions in downstream tasks. Evidential Deep Learning aims to address these limitations by producing uncertain...

---

### 18. Gated-SwinRMT: Unifying Swin Windowed Attention with Retentive Manhattan Decay via Input-Dependent Gating

**Authors:** Dipan Maity, Suman Mondal, Arindam Roy

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06014v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06014v1)

**Summary:** We introduce Gated-SwinRMT, a family of hybrid vision transformers that combine the shifted-window attention of the Swin Transformer with the Manhattan-distance spatial decay of Retentive Networks (RMT), augmented by input-dependent gating. Self-attention is decomposed into consecutive width-wise and height-wise retention passes within each shifted window, where per-head exponential decay masks provide a two-dimensional locality prior without learned positional biases.   Two variants are propose...

---

### 19. A deep learning framework for jointly solving transient Fokker-Planck equations with arbitrary parameters and initial distributions

**Authors:** Xiaolong Wang, Jing Feng, Qi Liu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06001v1)

**Summary:** Efficiently solving the Fokker-Planck equation (FPE) is central to analyzing complex parameterized stochastic systems. However, current numerical methods lack parallel computation capabilities across varying conditions, severely limiting comprehensive parameter exploration and transient analysis. This paper introduces a deep learning-based pseudo-analytical probability solution (PAPS) that, via a single training process, simultaneously resolves transient FPE solutions for arbitrary multi-modal i...

---

### 20. The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models

**Authors:** Xiaojie Gu, Ziying Huang, Weicong Hong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05995v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05995v1)

**Summary:** Large Language Models (LLMs) internalize vast world knowledge as parametric memory, yet inevitably inherit the staleness and errors of their source corpora. Consequently, ensuring the reliability and malleability of these internal representations is imperative for trustworthy real-world deployment. Knowledge editing offers a pivotal paradigm for surgically modifying memory without retraining. However, while recent editors demonstrate high success rates on standard benchmarks, it remains question...

---

### 21. Data Distribution Valuation Using Generalized Bayesian Inference

**Authors:** Cuong N. Nguyen, Cuong V. Nguyen

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05993v1)

**Summary:** We investigate the data distribution valuation problem, which aims to quantify the values of data distributions from their samples. This is a recently proposed problem that is related to but different from classical data valuation and can be applied to various applications. For this problem, we develop a novel framework called Generalized Bayes Valuation that utilizes generalized Bayesian inference with a loss constructed from transferability measures. This framework allows us to solve, in a uni...

---

### 22. On Dominant Manifolds in Reservoir Computing Networks

**Authors:** Noa Kaplan, Alberto Padoan, Anastasia Bizyaeva

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05967v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05967v1)

**Summary:** Understanding how training shapes the geometry of recurrent network dynamics is a central problem in time-series modeling. We study the emergence of low-dimensional dominant manifolds in the training of Reservoir Computing (RC) networks for temporal forecasting tasks. For a simplified linear and continuous-time reservoir model, we link the dimensionality and structure of the dominant modes directly to the intrinsic dimensionality and information content of the training data. In particular, for t...

---

### 23. QiMeng-PRepair: Precise Code Repair via Edit-Aware Reward Optimization

**Authors:** Changxin Ke, Rui Zhang, Jiaming Guo, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05963v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05963v1)

**Summary:** Large Language Models (LLMs) achieve strong program repair performance but often suffer from over-editing, where excessive modifications overwrite correct code and hinder bug localization. We systematically quantify its impact and introduce precise repair task, which maximizes reuse of correct code while fixing only buggy parts. Building on this insight, we propose PRepair, a framework that mitigates over-editing and improves repair accuracy. PRepair has two components: Self-Breaking, which gene...

---

### 24. A Mixture of Experts Foundation Model for Scanning Electron Microscopy Image Analysis

**Authors:** Sk Miraj Ahmed, Yuewei Lin, Chuntian Cao, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05960v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05960v1)

**Summary:** Scanning Electron Microscopy (SEM) is indispensable in modern materials science, enabling high-resolution imaging across a wide range of structural, chemical, and functional investigations. However, SEM imaging remains constrained by task-specific models and labor-intensive acquisition processes that limit its scalability across diverse applications. Here, we introduce the first foundation model for SEM images, pretrained on a large corpus of multi-instrument, multi-condition scientific microgra...

---

### 25. Multi-Modal Landslide Detection from Sentinel-1 SAR and Sentinel-2 Optical Imagery Using Multi-Encoder Vision Transformers and Ensemble Learning

**Authors:** Ioannis Nasios

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05959v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05959v1)

**Summary:** Landslides represent a major geohazard with severe impacts on human life, infrastructure, and ecosystems, underscoring the need for accurate and timely detection approaches to support disaster risk reduction. This study proposes a modular, multi-model framework that fuses Sentinel-2 optical imagery with Sentinel-1 Synthetic Aperture Radar (SAR) data, for robust landslide detection. The methodology leverages multi-encoder vision transformers, where each data modality is processed through separate...

---

### 26. ReLU Networks for Exact Generation of Similar Graphs

**Authors:** Mamoona Ghafoor, Tatsuya Akutsu

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05929v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05929v1)

**Summary:** Generation of graphs constrained by a specified graph edit distance from a source graph is important in applications such as cheminformatics, network anomaly synthesis, and structured data augmentation. Despite the growing demand for such constrained generative models in areas including molecule design and network perturbation analysis, the neural architectures required to provably generate graphs within a bounded graph edit distance remain largely unexplored. In addition, existing graph generat...

---

### 27. The UNDO Flip-Flop: A Controlled Probe for Reversible Semantic State Management in State Space Model

**Authors:** Hongxu Zhou

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05923v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05923v1)

**Summary:** State space models (SSMs) have been shown to possess the theoretical capacity to model both star-free sequential tasks and bounded hierarchical structures Sarrof et al. (2024). However, formal expressivity results do not guarantee that gradient-based optimisation will reliably discover the corresponding solutions. Existing benchmarks probe either monotonic state tracking, as in the standard Flip-Flop task, or structural nesting, as in the Dyck languages, but neither isolates reversible semantic ...

---

### 28. Transfer Learning for Neural Parameter Estimation applied to Building RC Models

**Authors:** Fabian Raisch, Timo Germann, J. Nathan Kutz, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05904v1)

**Summary:** Parameter estimation for dynamical systems remains challenging due to non-convexity and sensitivity to initial parameter guesses. Recent deep learning approaches enable accurate and fast parameter estimation but do not exploit transferable knowledge across systems. To address this, we introduce a transfer-learning-based neural parameter estimation framework based on a pretraining-fine-tuning paradigm. This approach improves accuracy and eliminates the need for an initial parameter guess. We appl...

---

### 29. A Tensor-Train Framework for Bayesian Inference in High-Dimensional Systems: Applications to MIMO Detection and Channel Decoding

**Authors:** Luca Schmid, Dominik Sulz, Shrinivas Chimmalgi, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05890v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05890v1)

**Summary:** Bayesian inference in high-dimensional discrete-input additive noise models is a fundamental challenge in communication systems, as the support of the required joint a posteriori probability (APP) mass function grows exponentially with the number of unknown variables. In this work, we propose a tensor-train (TT) framework for tractable, near-optimal Bayesian inference in discrete-input additive noise models. The central insight is that the joint log-APP mass function admits an exact low-rank rep...

---

### 30. Weight-Informed Self-Explaining Clustering for Mixed-Type Tabular Data

**Authors:** Lehao Li, Qiang Huang, Yihao Ang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05857v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05857v1)

**Summary:** Clustering mixed-type tabular data is fundamental for exploratory analysis, yet remains challenging due to misaligned numerical-categorical representations, uneven and context-dependent feature relevance, and disconnected and post-hoc explanation from the clustering process. We propose WISE, a Weight-Informed Self-Explaining framework that unifies representation, feature weighting, clustering, and interpretation in a fully unsupervised and transparent pipeline. WISE introduces Binary Encoding wi...

---

### 31. Neural Network Pruning via QUBO Optimization

**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05856v1)

**Summary:** Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic im...

---

### 32. JD-BP: A Joint-Decision Generative Framework for Auto-Bidding and Pricing

**Authors:** Linghui Meng, Chun Gan, Shengsheng Niu, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05845v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05845v1)

**Summary:** Auto-bidding services optimize real-time bidding strategies for advertisers under key performance indicator (KPI) constraints such as target return on investment and budget. However, uncertainties such as model prediction errors and feedback latency can cause bidding strategies to deviate from ex-post optimality, leading to inefficient allocation. To address this issue, we propose JD-BP, a Joint generative Decision framework for Bidding and Pricing. Unlike prior methods, JD-BP jointly outputs a ...

---

### 33. Modeling Patient Care Trajectories with Transformer Hawkes Processes

**Authors:** Saumya Pandey, Varun Chandola

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05844v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05844v1)

**Summary:** Patient healthcare utilization consists of irregularly time-stamped events, such as outpatient visits, inpatient admissions, and emergency encounters, forming individualized care trajectories. Modeling these trajectories is crucial for understanding utilization patterns and predicting future care needs, but is challenging due to temporal irregularity and severe class imbalance. In this work, we build on the Transformer Hawkes Process framework to model patient trajectories in continuous time. By...

---

### 34. EEG-MFTNet: An Enhanced EEGNet Architecture with Multi-Scale Temporal Convolutions and Transformer Fusion for Cross-Session Motor Imagery Decoding

**Authors:** Panagiotis Andrikopoulos, Siamak Mehrkanoon

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05843v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05843v1)

**Summary:** Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices, providing critical support for individuals with motor impairments. However, accurate motor imagery (MI) decoding from electroencephalography (EEG) remains challenging due to noise and cross-session variability. This study introduces EEG-MFTNet, a novel deep learning model based on the EEGNet architecture, enhanced with multi-scale temporal convolutions and a Transformer encoder stream. These comp...

---

### 35. Expectation Maximization (EM) Converges for General Agnostic Mixtures

**Authors:** Avishek Ghosh

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05842v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05842v1)

**Summary:** Mixture of linear regression is well studied in statistics and machine learning, where the data points are generated probabilistically using $k$ linear models. Algorithms like Expectation Maximization (EM) may be used to recover the ground truth regressors for this problem. Recently, in \cite{pal2022learning,ghosh_agnostic} the mixed linear regression problem is studied in the agnostic setting, where no generative model on data is assumed. Rather, given a set of data points, the objective is \em...

---

### 36. Hidden in the Multiplicative Interaction: Uncovering Fragility in Multimodal Contrastive Learning

**Authors:** Tillmann Rheude, Stefan Hegselmann, Roland Eils, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05834v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05834v1)

**Summary:** Multimodal contrastive learning is increasingly enriched by going beyond image-text pairs. Among recent contrastive methods, Symile is a strong approach for this challenge because its multiplicative interaction objective captures higher-order cross-modal dependence. Yet, we find that Symile treats all modalities symmetrically and does not explicitly model reliability differences, a limitation that becomes especially present in trimodal multiplicative interactions. In practice, modalities beyond ...

---

### 37. Bivariate Causal Discovery Using Rate-Distortion MDL: An Information Dimension Approach

**Authors:** Tiago Brogueira, Mário A. T. Figueiredo

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05829v1)

**Summary:** Approaches to bivariate causal discovery based on the minimum description length (MDL) principle approximate the (uncomputable) Kolmogorov complexity of the models in each causal direction, selecting the one with the lower total complexity. The premise is that nature's mechanisms are simpler in their true causal order. Inherently, the description length (complexity) in each direction includes the description of the cause variable and that of the causal mechanism. In this work, we argue that curr...

---

### 38. Learn to Rank: Visual Attribution by Learning Importance Ranking

**Authors:** David Schinagl, Christian Fruhwirth-Reisinger, Alexander Prutsch, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05819v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05819v1)

**Summary:** Interpreting the decisions of complex computer vision models is crucial to establish trust and accountability, especially in safety-critical domains. An established approach to interpretability is generating visual attribution maps that highlight regions of the input most relevant to the model's prediction. However, existing methods face a three-way trade-off. Propagation-based approaches are efficient, but they can be biased and architecture-specific. Meanwhile, perturbation-based methods are c...

---

### 39. Stealthy and Adjustable Text-Guided Backdoor Attacks on Multimodal Pretrained Models

**Authors:** Yiyang Zhang, Chaojian Yu, Ziming Hong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05809v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05809v1)

**Summary:** Multimodal pretrained models are vulnerable to backdoor attacks, yet most existing methods rely on visual or multimodal triggers, which are impractical since visually embedded triggers rarely occur in real-world data. To overcome this limitation, we propose a novel Text-Guided Backdoor (TGB) attack on multimodal pretrained models, where commonly occurring words in textual descriptions serve as backdoor triggers, significantly improving stealthiness and practicality. Furthermore, we introduce vis...

---

### 40. Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents

**Authors:** Shuai Zhen, Yanhua Yu, Ruopei Guo, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05808v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05808v1)

**Summary:** Large language model (LLM) agents have demonstrated strong capabilities in complex interactive decision-making tasks. However, existing LLM agents typically rely on increasingly long interaction histories, resulting in high computational cost and limited scalability. In this paper, we propose STEP-HRL, a hierarchical reinforcement learning (HRL) framework that enables step-level learning by conditioning only on single-step transitions rather than full interaction histories. STEP-HRL structures t...

---

### 41. Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction

**Authors:** Mohammed Salah Al-Radhi, Géza Németh, Andon Tchechmedjiev, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05751v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05751v1)

**Summary:** This chapter presents a novel approach to brain-to-speech (BTS) synthesis from intracranial electroencephalography (iEEG) data, emphasizing prosody-aware feature engineering and advanced transformer-based models for high-fidelity speech reconstruction. Driven by the increasing interest in decoding speech directly from brain activity, this work integrates neuroscience, artificial intelligence, and signal processing to generate accurate and natural speech. We introduce a novel pipeline for extract...

---

### 42. Graph Topology Information Enhanced Heterogeneous Graph Representation Learning

**Authors:** He Zhao, Zhiwei Zeng, Yongwei Wang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05732v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05732v1)

**Summary:** Real-world heterogeneous graphs are inherently noisy and usually not in the optimal graph structures for downstream tasks, which often adversely affects the performance of GRL models in downstream tasks. Although Graph Structure Learning (GSL) methods have been proposed to learn graph structures and downstream tasks simultaneously, existing methods are predominantly designed for homogeneous graphs, while GSL for heterogeneous graphs remains largely unexplored. Two challenges arise in this contex...

---

### 43. Controllable Image Generation with Composed Parallel Token Prediction

**Authors:** Jamie Stirling, Noura Al-Moubayed, Chris G. Willcocks, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05730v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05730v1)

**Summary:** Conditional discrete generative models struggle to faithfully compose multiple input conditions. To address this, we derive a theoretically-grounded formulation for composing discrete probabilistic generative processes, with masked generation (absorbing diffusion) as a special case. Our formulation enables precise specification of novel combinations and numbers of input conditions that lie outside the training data, with concept weighting enabling emphasis or negation of individual conditions. I...

---

### 44. Untargeted analysis of volatile markers of post-exercise fat oxidation in exhaled breath

**Authors:** André Homeyer, Júlia Blanka Sziládi, Jan-Philipp Redlich, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05707v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05707v1)

**Summary:** Breath acetone represents a promising non-invasive biomarker for monitoring fat oxidation during exercise. However, its utility is limited by confounding factors, as well as by the fact that significant changes in concentration occur only hours post-exercise, which makes real-time assessment difficult. We performed an untargeted screening for volatile organic compounds (VOCs) that could serve as markers of fat oxidation beyond acetone, and investigated whether breath measurements taken during ex...

---

### 45. Optimal-Transport-Guided Functional Flow Matching for Turbulent Field Generation in Hilbert Space

**Authors:** Li Kunpeng, Wan Chenguang, Qu Zhisong, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05700v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05700v1)

**Summary:** High-fidelity modeling of turbulent flows requires capturing complex spatiotemporal dynamics and multi-scale intermittency, posing a fundamental challenge for traditional knowledge-based systems. While deep generative models, such as diffusion models and Flow Matching, have shown promising performance, they are fundamentally constrained by their discrete, pixel-based nature. This limitation restricts their applicability in turbulence computing, where data inherently exists in a functional form. ...

---

### 46. LUDOBENCH: Evaluating LLM Behavioural Decision-Making Through Spot-Based Board Game Scenarios in Ludo

**Authors:** Ojas Jain, Dhruv Kumar

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05681v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05681v1)

**Summary:** We introduce LudoBench, a benchmark for evaluating LLM strategic reasoning in Ludo, a stochastic multi-agent board game whose dice mechanics, piece capture, safe-square navigation, and home-path progression introduce meaningful planning complexity. LudoBench comprises 480 handcrafted spot scenarios across 12 behaviorally distinct decision categories, each isolating a specific strategic choice. We additionally contribute a fully functional 4-player Ludo simulator supporting Random, Heuristic, Gam...

---

### 47. Intrinsic perturbation scale for certified oracle objectives with epigraphic information

**Authors:** Karim Bounja, Boujemaâ Achchab, Abdeljalil Sakat

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05678v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05678v1)

**Summary:** We introduce a natural displacement control for minimizer sets of oracle objectives equipped with certified epigraphic information. Formally, we replace the usual local uniform value control of objective perturbations - uncertifiable from finite pointwise information without additional structure - by the strictly weaker requirement of a cylinder-localized vertical epigraphic control, naturally provided by certified envelopes. Under set-based quadratic growth (allowing nonunique minimizers), this...

---

### 48. Efficient machine unlearning with minimax optimality

**Authors:** Jingyi Xie, Linjun Zhang, Sai Li

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05669v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05669v1)

**Summary:** There is a growing demand for efficient data removal to comply with regulations like the GDPR and to mitigate the influence of biased or corrupted data. This has motivated the field of machine unlearning, which aims to eliminate the influence of specific data subsets without the cost of full retraining. In this work, we propose a statistical framework for machine unlearning with generic loss functions and establish theoretical guarantees. For squared loss, especially, we develop Unlearning Least...

---

### 49. LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals

**Authors:** Lihao Sun, Hang Dong, Bo Qiao, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05655v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05655v1)

**Summary:** This work characterizes large language models' chain-of-thought generation as a structured trajectory through representation space. We show that mathematical reasoning traverses functionally ordered, step-specific subspaces that become increasingly separable with layer depth. This structure already exists in base models, while reasoning training primarily accelerates convergence toward termination-related subspaces rather than introducing new representational organization. While early reasoning ...

---

### 50. Multiscale Physics-Informed Neural Network for Complex Fluid Flows with Long-Range Dependencies

**Authors:** Prashant Kumar, Rajesh Ranjan

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05652v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05652v1)

**Summary:** Fluid flows are governed by the nonlinear Navier-Stokes equations, which can manifest multiscale dynamics even from predictable initial conditions. Predicting such phenomena remains a formidable challenge in scientific machine learning, particularly regarding convergence speed, data requirements, and solution accuracy. In complex fluid flows, these challenges are exacerbated by long-range spatial dependencies arising from distant boundary conditions, which typically necessitate extensive supervi...

---

## cs.NE

**50 papers**

### 1. Neural Network Pruning via QUBO Optimization

**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05856v1)

**Summary:** Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic im...

---

### 2. Constraint-Driven Warm-Freeze for Efficient Transfer Learning in Photovoltaic Systems

**Authors:** Yasmeen Saeed, Ahmed Sharshar, Mohsen Guizani

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05807v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05807v1)

**Summary:** Detecting cyberattacks in photovoltaic (PV) monitoring and MPPT control signals requires models that are robust to bias, drift, and transient spikes, yet lightweight enough for resource-constrained edge controllers. While deep learning outperforms traditional physics-based diagnostics and handcrafted features, standard fine-tuning is computationally prohibitive for edge devices. Furthermore, existing Parameter-Efficient Fine-Tuning (PEFT) methods typically apply uniform adaptation or rely on exp...

---

### 3. Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales

**Authors:** Tsung-Han Kuo, Tzu-Chia Tung

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04770v1)

**Summary:** Balanced spiking networks can transition between silent, asynchronous-irregular, and oscillatory states depending on interacting synaptic and temporal time scales, while their joint parameter structure remains incompletely characterized. In this work, we systematically map how postsynaptic decay (τs), conduction delay (d), and plasticity rate (λp) jointly shape oscillatory regimes in recurrent leaky integrate-and-fire networks. By combining Brian2 simulations across the (τs, d, λp) space with a ...

---

### 4. Ranking Constraints via Topological Dual-Directional Search in Evolutionary Multi-Objective Optimization

**Authors:** Ruiqing Sun, Dawei Feng, Sheng Qi, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04724v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04724v1)

**Summary:** Existing evolutionary algorithms for Constrained Multi-objective Optimization Problems (CMOPs) typically treat all constraints uniformly, overlooking their distinct geometric relationships with the true Constrained Pareto Front (CPF). In reality, constraints play different roles: some directly shape the final CPF, some create infeasible obstacles, while others are irrelevant. To exploit this insight, we propose a novel algorithm named RCCMO, which sequentially performs unconstrained exploration,...

---

### 5. Loop-Extrusion Linkage: Spectral Ordering and Interval-Based Structure Discovery for Continuous Optimization

**Authors:** Eren Unlu

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04273v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04273v1)

**Summary:** The rapid growth of nature-inspired metaheuristics has exposed a persistent gap between metaphorical novelty and genuine algorithmic advancement. Motivated by the biophysics of chromatin loop extrusion -- a well-characterized genome-folding process driven by SMC motor complexes and conditional barriers -- we introduce the Loop-Extrusion Linkage (LEL) operator, a structure-learning wrapper that combines online variable-interaction estimation, spectral seriation via the Fiedler vector, and adaptiv...

---

### 6. Parent Selection Mechanisms in Elitist Crossover-Based Algorithms

**Authors:** Andre Opris, Denis Antipov

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04083v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04083v1)

**Summary:** Parent selection methods are widely used in evolutionary computation to accelerate the optimization process, yet their theoretical benefits are still poorly understood. In this paper, we address this gap by incorporating different parent selection strategies into the $(μ+1)$ genetic algorithm (GA). We show that, with an appropriately chosen population size and a parent selection strategy that selects a pair of maximally distant parents with probability $Ω(1)$ for crossover, the resulting algorit...

---

### 7. Collapse-Free Prototype Readout Layer for Transformer Encoders

**Authors:** Giansalvo Cirrincione, Rahul Ranjeev Kumar

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03850v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03850v1)

**Summary:** DDCL-Attention is a prototype-based readout layer for transformer encoders that replaces simple pooling methods, such as mean pooling or class tokens, with a learned compression mechanism. It uses a small set of global prototype vectors and assigns tokens to them through soft probabilistic matching, producing compact token summaries at linear complexity in sequence length.   The method offers three main advantages. First, it avoids prototype collapse through an exact decomposition of the trainin...

---

### 8. An Imbalanced Dataset with Multiple Feature Representations for Studying Quality Control of Next-Generation Sequencing

**Authors:** Philipp Röchner, Clarissa Krämer, Johannes U Mayer, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.04981v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04981v1)

**Summary:** Next-generation sequencing (NGS) is a key technique for studying the DNA and RNA of organisms. However, identifying quality problems in NGS data across different experimental settings remains challenging. To develop automated quality-control tools, researchers require datasets with features that capture the characteristics of quality problems. Existing NGS repositories, however, offer only a limited number of quality-related features. To address this gap, we propose a dataset derived from 37.491...

---

### 9. RDEx-CMOP: Feasibility-Aware Indicator-Guided Differential Evolution for Fixed-Budget Constrained Multiobjective Optimization

**Authors:** Sichen Tao, Yifei Yang, Ruihan Zhao, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03708v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03708v1)

**Summary:** Constrained multiobjective optimisation requires fast feasibility attainment together with stable convergence and diversity preservation under strict evaluation budgets. This report documents RDEx-CMOP, the differential evolution variant used in the IEEE CEC 2025 numerical optimisation competition (C06 special session) constrained multiobjective track. RDEx-CMOP integrates an ε-level feasibility schedule, a SPEA2-style indicator-driven fitness assignment, and a fitness-oriented current-to-pbest/...

---

### 10. TransGP: Task-Conditioned Transformer-Guided Genetic Programming for Multitask Dynamic Flexible Job Shop Scheduling

**Authors:** Meng Xu, Jiao Liu, Hua Yu, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03705v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03705v1)

**Summary:** Hyper-heuristics have become a popular approach for solving dynamic flexible job shop scheduling (DFJSS) problems. They use gradient-free optimization techniques like Genetic Programming (GP) to evolve non-differentiable heuristics. However, conventional GP methods tend to converge slowly because they rely solely on evolutionary search to find good heuristics. Existing multitask GP methods can solve multiple tasks simultaneously and speed up the search by transferring knowledge across similar ta...

---

### 11. L-SPINE: A Low-Precision SIMD Spiking Neural Compute Engine for Resource-efficient Edge Inference

**Authors:** Sonu Kumar, Mukul Lokhande, Santosh Kumar Vishvakarma

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03626v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03626v1)

**Summary:** Spiking Neural Networks (SNNs) offer a promising solution for energy-efficient edge intelligence; however, their hardware deployment is constrained by memory overhead, inefficient scaling operations, and limited parallelism. This work proposes L-SPINE, a low-precision SIMD-enabled spiking neural compute engine for efficient edge inference. The architecture features a unified multi-precision datapath supporting 2-bit, 4-bit, and 8-bit operations, leveraging a multiplier-less shift-add model for n...

---

### 12. Finding Sets of Pareto Sets in Real-World Scenarios -- A Multitask Multiobjective Perspective

**Authors:** Jiao Liu, Yew Soon Ong, Melvin Wong

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03570v1)

**Summary:** Recently, evolutionary multitasking has been employed to generate a ``set of Pareto sets" (SOS) for machine learning models, addressing diverse task settings across heterogeneous environments. This involves creating a repository of compact, specialized solution models that are collectively tailored to each specific task setting and environment, enabling users to select the most suitable model based on particular specifications and preferences. In this paper, we further demonstrate the versatilit...

---

### 13. Personality Requires Struggle: Three Regimes of the Baldwin Effect in Neuroevolved Chess Agents

**Authors:** Diego Armando Resendez Prado

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03565v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03565v1)

**Summary:** Can lifetime learning expand behavioral diversity over evolutionary time, rather than collapsing it? Prior theory predicts that plasticity reduces variance by buffering organisms against environmental noise. We test this in a competitive domain: chess agents with eight NEAT-evolved neural modules, Hebbian within-game plasticity, and a desirability-domain signal chain with imagination. Across 10~seeds per Hebbian condition, a variance crossover emerges: Hebbian ON starts with lower cross-seed var...

---

### 14. YANA: Bridging the Neuromorphic Simulation-to-Hardware Gap

**Authors:** Brian Pachideh, Sven Nitzsche, Moritz Neher, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03432v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03432v1)

**Summary:** Spiking Neural Networks (SNNs) promise significant advantages over conventional Artificial Neural Networks (ANNs) for applications requiring real-time processing of temporally sparse data streams under strict power constraints -- a concept known as the Neuromorphic Advantage. However, the limited availability of neuromorphic hardware creates a substantial simulation-to-hardware gap that impedes algorithmic innovation, hardware-software co-design, and the development of mature open-source ecosyst...

---

### 15. Activity-Dependent Plasticity in Morphogenetically-Grown Recurrent Networks

**Authors:** Sergii Medvid, Andrii Valenia, Mykola Glybovets

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03386v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03386v1)

**Summary:** Developmental approaches to neural architecture search grow functional networks from compact genomes through self-organisation, but the resulting networks operate with fixed post-growth weights. We characterise Hebbian and anti-Hebbian plasticity across 50,000 morphogenetically grown recurrent controllers (5M+ configurations on CartPole and Acrobot), then test whether co-evolutionary experiments -- where plasticity parameters are encoded in the genome and evolved alongside the developmental arch...

---

### 16. Biologically Realistic Dynamics for Nonlinear Classification in CMOS+X Neurons

**Authors:** Steven Louis, Hannah Bradley, Artem Litvinenko, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03187v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03187v1)

**Summary:** Spiking neural networks encode information in spike timing and offer a pathway toward energy efficient artificial intelligence. However, a key challenge in spiking neural networks is realizing nonlinear and expressive computation in compact, energy-efficient hardware without relying on additional circuit complexity. In this work, we examine nonlinear computation in a CMOS+X spiking neuron implemented with a magnetic tunnel junction connected in series with an NMOS transistor. Circuit simulations...

---

### 17. Accelerating Black-Box Bilevel Optimization with Rank-Based Upper-Level Value Function Approximation

**Authors:** Marc Ong, Youhei Akimoto

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02888v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02888v1)

**Summary:** Bilevel optimization is a field of significant theoretical and practical interest, yet solving such optimization problems remains challenging. Evolutionary methods have been employed to address these problems in the black-box setting; however, they incur high computational cost due to the nested nature of bilevel optimization. Although previous methods have attempted to reduce this cost through various heuristic techniques, such approaches limit versatility on challenging optimization landscapes...

---

### 18. Frame Theoretical Derivation of Three Factor Learning Rule for Oja's Subspace Rule

**Authors:** Taiki Yamada

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02849v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02849v1)

**Summary:** We show that the error-gated Hebbian rule for PCA (EGHR-PCA), a three-factor learning rule equivalent to Oja's subspace rule under Gaussian inputs, can be systematically derived from Oja's subspace rule using frame theory. The global third factor in EGHR-PCA arises exactly as a frame coefficient when the learning rule is expanded with respect to a natural frame on the space of symmetric matrices. This provides a principled, non-heuristic derivation of a biologically plausible learning rule from ...

---

### 19. Apparent Age Estimation: Challenges and Outcomes

**Authors:** Justin Rainier Go, Lorenz Bernard Marqueses, Mikaella Kaye Martinez, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03335v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03335v1)

**Summary:** Apparent age estimation is a valuable tool for business personalization, yet current models frequently exhibit demographic biases. We review prior works on the DEX method by applying distribution learning techniques such as Mean-Variance Loss (MVL) and Adaptive Mean-Residue Loss (AMRL), and evaluate them in both accuracy and fairness. Using IMDB-WIKI, APPA-REAL, and FairFace, we demonstrate that while AMRL achieves state-of-the-art accuracy, trade-offs between precision and demographic equity pe...

---

### 20. Wavelength-multiplexed massively parallel diffractive optical information storage and image projection

**Authors:** Che-Yung Shen, Yuhang Li, Cagatay Isil, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02624v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02624v1)

**Summary:** We introduce a wavelength-multiplexed massively parallel diffractive information storage platform composed of dielectric surfaces that are structurally optimized at the wavelength scale using deep learning to store and project thousands of distinct image patterns, each assigned to a unique wavelength. Through numerical simulations in the visible spectrum, we demonstrated that our wavelength-multiplexed diffractive system can store and project over 4,000 independent desired images/patterns within...

---

### 21. Computing with Living Neurons: Chaos-Controlled Reservoir Computing with Knowledge Transplant

**Authors:** Seung Hyun Kim, Zhi Dou, Gaurav Upadhyay, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02552v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02552v1)

**Summary:** We introduce chaos-controlled Reservoir Computing (cc-RC) for living neural cultures: dynamically rich substrates of unique potential for adaptive computation. To account for intrinsic biological variability, cc-RC combines: (i) pre-training identification of each culture's dynamical signature and phase-portrait attractor; (ii) low-power optical chaos control to stabilize spontaneous and stimulus-evoked activity; (iii) readout training within this controlled regime. Across hundreds of neural sam...

---

### 22. When does learning pay off? A study on DRL-based dynamic algorithm configuration for carbon-aware scheduling

**Authors:** Andrea Mencaroni, Robbert Reijnen, Yingqian Zhang, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01886v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01886v1)

**Summary:** Deep reinforcement learning (DRL) has recently emerged as a promising tool for Dynamic Algorithm Configuration (DAC), enabling evolutionary algorithms to adapt their parameters online rather than relying on static tuned configurations. While DRL can learn effective control policies, training is computationally expensive. This cost may be justified if learned policies generalize, allowing the training effort to transfer across instance types and problem scales. Yet, for real-world optimization pr...

---

### 23. DDCL-INCRT: A Self-Organising Transformer with Hierarchical Prototype Structure (Theoretical Foundations)

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01880v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01880v1)

**Summary:** Modern neural networks of the transformer family require the practitioner to decide, before training begins, how many attention heads to use, how deep the network should be, and how wide each component should be. These decisions are made without knowledge of the task, producing architectures that are systematically larger than necessary: empirical studies find that a substantial fraction of heads and layers can be removed after training without performance loss.   This paper introduces DDCL-INCR...

---

### 24. DDCL: Deep Dual Competitive Learning: A Differentiable End-to-End Framework for Unsupervised Prototype-Based Representation Learning

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01740v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01740v1)

**Summary:** A persistent structural weakness in deep clustering is the disconnect between feature learning and cluster assignment. Most architectures invoke an external clustering step, typically k-means, to produce pseudo-labels that guide training, preventing the backbone from directly optimising for cluster quality. This paper introduces Deep Dual Competitive Learning (DDCL), the first fully differentiable end-to-end framework for unsupervised prototype-based representation learning. The core contributio...

---

### 25. Oscillator-Based Associative Memory with Exponential Capacity: Theory, Algorithms, and Hardware Implementation

**Authors:** Arie Ogranovich, Taosha Guo, Arvind R. Venkatakrishnan, et al.

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01469v1)

**Summary:** Associative memory systems enable content-addressable storage and retrieval of patterns, a capability central to biological neural computation and artificial intelligence. Classical implementations such as Hopfield networks face fundamental limitations in memory capacity, scaling at most linearly with network size. We present an associative memory architecture based on Kuramoto oscillator networks with honeycomb topology in which memories are encoded as stable phase-locked configurations. The ho...

---

### 26. Evolutionary Multi-Objective Fusion of Deepfake Speech Detectors

**Authors:** Vojtěch Staněk, Martin Perešíni, Lukáš Sekanina, et al.

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01330v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01330v1)

**Summary:** While deepfake speech detectors built on large self-supervised learning (SSL) models achieve high accuracy, employing standard ensemble fusion to further enhance robustness often results in oversized systems with diminishing returns. To address this, we propose an evolutionary multi-objective score fusion framework that jointly minimizes detection error and system complexity. We explore two encodings optimized by NSGA-II: binary-coded detector selection for score averaging and a real-valued sche...

---

### 27. A Hierarchical Importance-Guided Multi-objective Evolutionary Framework for Deep Neural Network Pruning

**Authors:** Zak Khan, Azam Asilian Bidgoli

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01076v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01076v1)

**Summary:** The optimization of over-parameterized deep neural networks represents a large-scale, high-dimensional, and strongly non-convex decision problem that challenges existing optimization frameworks. Current evolutionary and gradient-based pruning methods often struggle to scale to such dimensionalities, as they rely on flat search spaces, scalarized objectives, or repeated retraining, leading to premature convergence and prohibitive computational cost. This paper introduces a hierarchical importance...

---

### 28. Integer-State Dynamics of Quantized Spiking Neural Networks for Efficient Hardware Acceleration

**Authors:** Lei Zhang

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01042v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01042v1)

**Summary:** Spiking neural networks (SNNs) support energy-efficient machine intelligence because event-driven computation and sparse activity map naturally to low-power digital hardware. In practical implementations, however, membrane states, synaptic weights, and thresholds are represented with finite-precision integer arithmetic. Quantization, clipping, and overflow can therefore alter network dynamics, not just approximate a higher-precision model. This paper adopts an integer-state dynamical perspective...

---

### 29. OkanNet: A Lightweight Deep Learning Architecture for Classification of Brain Tumor from MRI Images

**Authors:** Okan Uçar, Murat Kurt

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01264v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01264v1)

**Summary:** Medical imaging techniques, especially Magnetic Resonance Imaging (MRI), are accepted as the gold standard in the diagnosis and treatment planning of neurological diseases. However, the manual analysis of MRI images is a time-consuming process for radiologists and is prone to human error due to fatigue. In this study, two different Deep Learning approaches were developed and analyzed comparatively for the automatic detection and classification of brain tumors (Glioma, Meningioma, Pituitary, and ...

---

### 30. Finding Low Star Discrepancy 3D Kronecker Point Sets Using Algorithm Configuration Techniques

**Authors:** Imène Ait Abderrahim, Carola Doerr, Martin Durand

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.00786v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00786v1)

**Summary:** The L infinity star discrepancy is a measure for how uniformly a point set is distributed in a given space. Point sets of low star discrepancy are used as designs of experiments, as initial designs for Bayesian optimization algorithms, for quasi-Monte Carlo integration methods, and many other applications. Recent work has shown that classical constructions such as Sobol', Halton, or Hammersley sequences can be outperformed by large margins when considering point sets of fixed sizes rather than t...

---

### 31. G-ICSO-NAS: Shifting Gears between Gradient and Swarm for Robust Neural Architecture Search

**Authors:** Xingbang Du, Enzhi Zhang, Rui Zhong, et al.

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.00703v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00703v1)

**Summary:** Neural Architecture Search (NAS) has become a pivotal technique in automated machine learning. Evolutionary Algorithm (EA)-based methods demonstrate superior search quality but suffer from prohibitive computational costs, while gradient-based approaches like DARTS offer high efficiency but are prone to premature convergence and performance collapse. To bridge this gap, we propose G-ICSO-NAS, a hybrid framework implementing a three-stage optimization strategy. The Warm-up Phase pre-trains superne...

---

### 32. Generalized Heavy-tailed Mutation for Evolutionary Algorithms

**Authors:** Anton V. Eremeev, Dmitri V. Silaev, Valentin A. Topchii

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.00502v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00502v1)

**Summary:** The heavy-tailed mutation operator, proposed by Doerr, Le, Makhmara, and Nguyen (2017) for evolutionary algorithms, is based on the power-law assumption of mutation rate distribution. Here we generalize the power-law assumption using a regularly varying constraint on the distribution function of mutation rate. In this setting, we generalize the upper bounds on the expected optimization time of the $(1+(λ,λ))$ genetic algorithm obtained by Antipov, Buzdalov and Doerr (2022) for the OneMax functio...

---

### 33. Set-Based Value Function Characterization and Neural Approximation of Stabilization Domains for Input-Constrained Discrete-Time Systems

**Authors:** Mohamed Serry, S. Sivaranjani, Jun Liu

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2604.00305v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00305v1)

**Summary:** Analyzing nonlinear systems with stabilizable controlled invariant sets (CISs) requires accurate estimation of their domains of stabilization (DOS) together with associated stabilizing controllers. Despite extensive research, estimating DOSs for general nonlinear systems remains challenging due to fundamental theoretical and computational limitations. In this paper, we propose a novel framework for estimating DOSs for controlled input-constrained discrete-time systems. The DOS is characterized v...

---

### 34. Epileptic Seizure Detection in Separate Frequency Bands Using Feature Analysis and Graph Convolutional Neural Network (GCN) from Electroencephalogram (EEG) Signals

**Authors:** Ferdaus Anam Jibon, Fazlul Hasan Siddiqui, F. Deeba, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2604.00163v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00163v1)

**Summary:** Epileptic seizures are neurological disorders characterized by abnormal and excessive electrical activity in the brain, resulting in recurrent seizure events. Electroencephalogram (EEG) signals are widely used for seizure diagnosis due to their ability to capture temporal and spatial neural dynamics. While recent deep learning methods have achieved high detection accuracy, they often lack interpretability and neurophysiological relevance. This study presents a frequency-aware framework for epile...

---

### 35. Associative Constructive Evolution: Enhancing Metaheuristics through Hebbian-Learned Generative Guidance

**Authors:** Shanxian Lin, Yuichi Nagata, Haichuan Yang

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29774v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29774v1)

**Summary:** Metaheuristic algorithms such as Particle Swarm Optimization (PSO) and Evolutionary Algorithms (EA) excel at exploring solution spaces but lack mechanisms to accumulate and reuse procedural knowledge from successful search trajectories. This paper proposes Associative Constructive Evolution (ACE), a framework that enhances metaheuristics through learned generative guidance. ACE introduces a Generative Construction Automaton (GCA) -- a probabilistic model over operation sequences -- coupled with ...

---

### 36. Large-scale nonlinear optical computing with incoherent light via linear diffractive systems

**Authors:** Alexander Chen, Yuntian Wang, Md Sadman Sakib Rahman, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29131v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29131v1)

**Summary:** Nonlinear computation is essential for various information processing tasks. Optical implementations are attractive because passive light propagation can manipulate high-dimensional signals with extreme throughput and parallelism; yet realizing nonlinear mappings in optical hardware remains challenging due to the weak nonlinearity of optical materials and the large intensities required to induce nonlinear interactions. This challenge is further amplified in many systems that operate with incoher...

---

### 37. BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations

**Authors:** Kaushitha Silva, Srinath Perera

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28653v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28653v1)

**Summary:** Large Language Models (LLMs) have demonstrated impressive capabilities in code generation. While an interactive feedback loop can improve performance, writing effective tests is a non-trivial task. Early multi-agent frameworks, such as AgentCoder, automated this process but relied on generated tests as absolute ground truth. This approach is fragile: incorrect code frequently passes faulty or trivial tests, while valid solutions are often degraded to satisfy incorrect assertions. Addressing this...

---

### 38. Critic-Free Deep Reinforcement Learning for Maritime Coverage Path Planning on Irregular Hexagonal Grids

**Authors:** Carlos S. Sepúlveda, Gonzalo A. Ruz

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28385v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28385v1)

**Summary:** Maritime surveillance missions, such as search and rescue and environmental monitoring, rely on the efficient allocation of sensing assets over vast and geometrically complex areas. Traditional Coverage Path Planning (CPP) approaches depend on decomposition techniques that struggle with irregular coastlines, islands, and exclusion zones, or require computationally expensive re-planning for every instance. We propose a Deep Reinforcement Learning (DRL) framework to solve CPP on hexagonal grid rep...

---

### 39. Framework for identifying the equivalence between Nature-Inspired Metaheuristics

**Authors:** Iztok Fister, Žan Hozjan, Iztok Fister,, et al.

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28255v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28255v1)

**Summary:** The domain of metaheuristic optimization has become vibrant due to a flood of new algorithms using a new nature-inspired metaphor but lacking clear methodological novelty. The Criticism behind the development of these algorithms has reached such an extent that the critics started to assert that all novel algorithms are only copies of already developed ones. In this study, we try to show that the situation is not so black and white. Therefore, we define a strong equivalence theorem for estimating...

---

### 40. Evolutionary Algorithms for Generating Graphs Matching Desired Laplacian Spectra

**Authors:** Hendrik Richter, Frank Neumann

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28151v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28151v1)

**Summary:** Graphs with diverse structural characteristics play a central role in modelling and optimization tasks. The ability to generate different types of graphs that exhibit shared properties is likewise essential for algorithm selection and configuration. However, constructing graphs that preserve high-level properties across a broad range of graph classes remains a challenging problem. We present a novel evolutionary approach to evolve graphs based on the Laplacian graph spectra descriptor. This desc...

---

### 41. A Learning-Based Cooperative Coevolution Framework for Heterogeneous Large-Scale Global Optimization

**Authors:** Wenjie Qiu, Zixin Wang, Hongyu Fang, et al.

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2604.01241v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01241v1)

**Summary:** Cooperative Coevolution (CC) effectively addresses Large-Scale Global Optimization (LSGO) via decomposition but struggles with the emerging class of Heterogeneous LSGO (H-LSGO) problems arising from real-world applications, where subproblems exhibit diverse dimensions and distinct landscapes. The prevailing CC paradigm, relying on a fixed low-dimensional optimizer, often fails to navigate this heterogeneity. To address this limitation, we propose the Learning-Based Heterogeneous Cooperative Coev...

---

### 42. The role of neuromorphic principles in the future of biomedicine and healthcare

**Authors:** Grace M. Hwang, Jessica D. Falcone, Joseph D. Monaco, et al.

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27716v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27716v1)

**Summary:** Neuromorphic engineering has matured over the past four decades and is currently experiencing explosive growth with the potential to transform biomedical engineering and neurotechnologies. Participants at the Neuromorphic Principles in Biomedicine and Healthcare (NPBH) Workshop (October 2024) -- representing a broad cross-section of the community, including early-career and established scholars, engineers, scientists, clinicians, industry, and funders -- convened to discuss the state of the fiel...

---

### 43. A Novel Immune Algorithm for Multiparty Multiobjective Optimization

**Authors:** Kesheng Chen, Wenjian Luo, Qi Zhou, et al.

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27541v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27541v1)

**Summary:** Traditional multiobjective optimization problems (MOPs) are insufficiently equipped for scenarios involving multiple decision makers (DMs), which are prevalent in many practical applications. These scenarios are categorized as multiparty multiobjective optimization problems (MPMOPs). For MPMOPs, the goal is to find a solution set that is as close to the Pareto front of each DM as much as possible. This poses challenges for evolutionary algorithms in terms of searching and selecting. To better so...

---

### 44. Persistent Memory Through Triple-Loop Consolidation in a Non-Gradient Dissipative Cognitive Architecture

**Authors:** Jianwei Lou

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27188v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27188v1)

**Summary:** Dissipative cognitive architectures maintain computation through continuous energy expenditure, where units that exhaust their energy are stochastically replaced with fresh random state. This creates a fundamental challenge: how can persistent, context-specific memory survive when all learnable state is periodically destroyed? Existing memory mechanisms -- including elastic weight consolidation, synaptic intelligence, and surprise-driven gating -- rely on gradient computation and are inapplicabl...

---

### 45. The Price of Meaning: Why Every Semantic Memory System Forgets

**Authors:** Sambartha Ray Barman, Andrey Starenky, Sofia Bodnar, et al.

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27116v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27116v1)

**Summary:** Every major AI memory system in production today organises information by meaning. That organisation enables generalisation, analogy, and conceptual retrieval -- but it comes at a price. We prove that the same geometric structure enabling semantic generalisation makes interference, forgetting, and false recall inescapable. We formalise this tradeoff for \textit{semantically continuous kernel-threshold memories}: systems whose retrieval score is a monotone function of an inner product in a semant...

---

### 46. RDEx-MOP: Indicator-Guided Reconstructed Differential Evolution for Fixed-Budget Multiobjective Optimization

**Authors:** Sichen Tao, Yifei Yang, Ruihan Zhao, et al.

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27092v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27092v1)

**Summary:** Multiobjective optimisation in the CEC 2025 MOP track is evaluated not only by final IGD values but also by how quickly an algorithm reaches the target region under a fixed evaluation budget. This report documents RDEx-MOP, the reconstructed differential evolution variant used in the IEEE CEC 2025 numerical optimisation competition (C06 special session) bound-constrained multiobjective track. RDEx-MOP integrates indicator-based environmental selection, a niche-maintained Pareto-candidate set, an...

---

### 47. RDEx-CSOP: Feasibility-Aware Reconstructed Differential Evolution with Adaptive epsilon-Constraint Ranking

**Authors:** Sichen Tao, Yifei Yang, Ruihan Zhao, et al.

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27090v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27090v1)

**Summary:** Constrained single-objective numerical optimisation requires both feasibility maintenance and strong objective-value convergence under limited evaluation budgets. This report documents RDEx-CSOP, a constrained differential evolution variant used in the IEEE CEC 2025 numerical optimisation competition (C06 special session). RDEx-CSOP combines success-history parameter adaptation with an exploitation-biased hybrid search and an ε-constraint handling mechanism with a time-varying threshold. We eval...

---

### 48. RDEx-SOP: Exploitation-Biased Reconstructed Differential Evolution for Fixed-Budget Bound-Constrained Single-Objective Optimization

**Authors:** Sichen Tao, Yifei Yang, Ruihan Zhao, et al.

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27089v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27089v1)

**Summary:** Bound-constrained single-objective numerical optimisation remains a key benchmark for assessing the robustness and efficiency of evolutionary algorithms. This report documents RDEx-SOP, an exploitation-biased success-history differential evolution variant used in the IEEE CEC 2025 numerical optimisation competition (C06 special session). RDEx-SOP combines success-history parameter adaptation, an exploitation-biased hybrid branch, and lightweight local perturbations to balance fast convergence an...

---

### 49. SwarmCoDe: A Scalable Co-Design Framework for Heterogeneous Robot Swarms via Dynamic Speciation

**Authors:** Andrew Wilhelm, Josie Hughes

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26240v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26240v1)

**Summary:** Robot swarms offer inherent robustness and the capacity to execute complex, collaborative tasks surpassing the capabilities of single-agent systems. Co-designing these systems is critical, as marginal improvements in individual performance or unit cost compound significantly at scale. However, under traditional frameworks, this scale renders co-design intractable due to exponentially large, non-intuitive design spaces. To address this, we propose SwarmCoDe, a novel Collaborative Co-Evolutionary ...

---

### 50. H-Node Attack and Defense in Large Language Models

**Authors:** Eric Yocam, Varghese Vaidyan, Yong Wang

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26045v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26045v1)

**Summary:** We present H-Node Adversarial Noise Cancellation (H-Node ANC), a mechanistic framework that identifies, exploits, and defends hallucination representations in transformer-based large language models (LLMs) at the level of individual hidden-state dimensions. A logistic regression probe trained on last-token hidden states localizes hallucination signal to a small set of high-variance dimensions -- termed Hallucination Nodes (H-Nodes) -- with probe AUC reaching 0.90 across four architectures. A whi...

---

## stat.ML

**50 papers**

### 1. In-Place Test-Time Training

**Authors:** Guhao Feng, Shengjie Luo, Kai Hua, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06169v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06169v1)

**Summary:** The static ``train then deploy" paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks. Test-Time Training (TTT) offers a compelling alternative by updating a subset of model parameters (fast weights) at inference time, yet its potential in the current LLM ecosystem is hindered by critical barriers including architectural incompatibility, computational inefficiency and mi...

---

### 2. Sequential Audit Sampling with Statistical Guarantees

**Authors:** Masahiro Kato, Kei Nakagawa

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06116v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06116v1)

**Summary:** Financial statement auditing is conducted under a risk-based evidence approach to obtain reasonable assurance. In practice, auditors often perform additional sampling or related procedures when an initial sample does not provide a sufficient basis for a conclusion. Across jurisdictions, current standards and practice manuals acknowledge such extensions, while the statistical design of sequential audit procedures has not been fully explored. This study formulates audit sampling with additional, s...

---

### 3. Lipschitz regularity in Flow Matching and Diffusion Models: sharp sampling rates and functional inequalities

**Authors:** Arthur Stéphanovitch

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06065v1)

**Summary:** Under general assumptions on the target distribution $p^\star$, we establish a sharp Lipschitz regularity theory for flow-matching vector fields and diffusion-model scores, with optimal dependence on time and dimension. As applications, we obtain Wasserstein discretization bounds for Euler-type samplers in dimension $d$: with $N$ discretization steps, the error achieves the optimal rate $\sqrt{d}/N$ up to logarithmic factors. Moreover, the constants do not deteriorate exponentially with the spat...

---

### 4. Ensemble-Based Dirichlet Modeling for Predictive Uncertainty and Selective Classification

**Authors:** Courtney Franzen, Farhad Pourkamali-Anaraki

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06032v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06032v1)

**Summary:** Neural network classifiers trained with cross-entropy loss achieve strong predictive accuracy but lack the capability to provide inherent predictive uncertainty estimates, thus requiring external techniques to obtain these estimates. In addition, softmax scores for the true class can vary substantially across independent training runs, which limits the reliability of uncertainty-based decisions in downstream tasks. Evidential Deep Learning aims to address these limitations by producing uncertain...

---

### 5. Data Distribution Valuation Using Generalized Bayesian Inference

**Authors:** Cuong N. Nguyen, Cuong V. Nguyen

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05993v1)

**Summary:** We investigate the data distribution valuation problem, which aims to quantify the values of data distributions from their samples. This is a recently proposed problem that is related to but different from classical data valuation and can be applied to various applications. For this problem, we develop a novel framework called Generalized Bayes Valuation that utilizes generalized Bayesian inference with a loss constructed from transferability measures. This framework allows us to solve, in a uni...

---

### 6. Expectation Maximization (EM) Converges for General Agnostic Mixtures

**Authors:** Avishek Ghosh

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05842v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05842v1)

**Summary:** Mixture of linear regression is well studied in statistics and machine learning, where the data points are generated probabilistically using $k$ linear models. Algorithms like Expectation Maximization (EM) may be used to recover the ground truth regressors for this problem. Recently, in \cite{pal2022learning,ghosh_agnostic} the mixed linear regression problem is studied in the agnostic setting, where no generative model on data is assumed. Rather, given a set of data points, the objective is \em...

---

### 7. Bivariate Causal Discovery Using Rate-Distortion MDL: An Information Dimension Approach

**Authors:** Tiago Brogueira, Mário A. T. Figueiredo

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05829v1)

**Summary:** Approaches to bivariate causal discovery based on the minimum description length (MDL) principle approximate the (uncomputable) Kolmogorov complexity of the models in each causal direction, selecting the one with the lower total complexity. The premise is that nature's mechanisms are simpler in their true causal order. Inherently, the description length (complexity) in each direction includes the description of the cause variable and that of the causal mechanism. In this work, we argue that curr...

---

### 8. Effective Dynamics and Transition Pathways from Koopman-Inspired Neural Learning of Collective Variables

**Authors:** Alexander Sikorski, Luca Donati, Marcus Weber, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05778v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05778v1)

**Summary:** The ISOKANN (Invariant Subspaces of Koopman Operators Learned by Artificial Neural Networks) framework provides a data-driven route to extract collective variables (CVs) and effective dynamics from complex molecular systems. In this work, we integrate the theoretical foundation of Koopman operators with Krylov-like subspace algorithms, and reduced dynamical modeling to build a coherent picture of how to describe metastable transitions in high-dimensional systems based on CVs. Starting from the i...

---

### 9. High-dimensional reliability-based design optimization using stochastic emulators

**Authors:** M. Moustapha, B. Sudret

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05759v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05759v1)

**Summary:** Reliability-based design optimization (RBDO) is traditionally formulated as a nested optimization and reliability problem. Although surrogate models are generally employed to improve efficiency, the approach remains computationally prohibitive in high-dimensional settings. This paper proposes a novel RBDO framework based on a stochastic simulator viewpoint, in which the deterministic limit-state function and the uncertainty in the model inputs are combined into a unified stochastic representatio...

---

### 10. Efficient machine unlearning with minimax optimality

**Authors:** Jingyi Xie, Linjun Zhang, Sai Li

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05669v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05669v1)

**Summary:** There is a growing demand for efficient data removal to comply with regulations like the GDPR and to mitigate the influence of biased or corrupted data. This has motivated the field of machine unlearning, which aims to eliminate the influence of specific data subsets without the cost of full retraining. In this work, we propose a statistical framework for machine unlearning with generic loss functions and establish theoretical guarantees. For squared loss, especially, we develop Unlearning Least...

---

### 11. Optimal Centered Active Excitation in Linear System Identification

**Authors:** Kaito Ito, Alexandre Proutiere

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05518v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05518v1)

**Summary:** We propose an active learning algorithm for linear system identification with optimal centered noise excitation. Notably, our algorithm, based on ordinary least squares and semidefinite programming, attains the minimal sample complexity while allowing for efficient computation of an estimate of a system matrix. More specifically, we first establish lower bounds of the sample complexity for any active learning algorithm to attain the prescribed accuracy and confidence levels. Next, we derive a sa...

---

### 12. Task Ecologies and the Evolution of World-Tracking Representations in Large Language Models

**Authors:** Giulio Valentino Dalla Riva

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05469v1)

**Summary:** We study language models as evolving model organisms and ask when autoregressive next-token learning selects for world-tracking representations. For any encoding of latent world states, the Bayes-optimal next-token cross-entropy decomposes into the irreducible conditional entropy plus a Jensen--Shannon excess term. That excess vanishes if and only if the encoding preserves the training ecology's equivalence classes. This yields a precise notion of ecological veridicality for language models and ...

---

### 13. Hierarchical Contrastive Learning for Multimodal Data

**Authors:** Huichao Li, Junhan Yu, Doudou Zhou

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05462v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05462v1)

**Summary:** Multimodal representation learning is commonly built on a shared-private decomposition, treating latent information as either common to all modalities or specific to one. This binary view is often inadequate: many factors are shared by only subsets of modalities, and ignoring such partial sharing can over-align unrelated signals and obscure complementary information. We propose Hierarchical Contrastive Learning (HCL), a framework that learns globally shared, partially shared, and modality-specif...

---

### 14. MEC: Machine-Learning-Assisted Generalized Entropy Calibration for Semi-Supervised Mean Estimation

**Authors:** Se Yoon Lee, Jae Kwang Kim

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05446v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05446v1)

**Summary:** Obtaining high-quality labels is costly, whereas unlabeled covariates are often abundant, motivating semi-supervised inference methods with reliable uncertainty quantification. Prediction-powered inference (PPI) leverages a machine-learning predictor trained on a small labeled sample to improve efficiency, but it can lose efficiency under model misspecification and suffer from coverage distortions due to label reuse. We introduce Machine-Learning-Assisted Generalized Entropy Calibration (MEC), a...

---

### 15. Individual-heterogeneous sub-Gaussian Mixture Models

**Authors:** Huan Qing

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05337v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05337v1)

**Summary:** The classical Gaussian mixture model assumes homogeneity within clusters, an assumption that often fails in real-world data where observations naturally exhibit varying scales or intensities. To address this, we introduce the individual-heterogeneous sub-Gaussian mixture model, a flexible framework that assigns each observation its own heterogeneity parameter, thereby explicitly capturing the heterogeneity inherent in practical applications. Built upon this model, we propose an efficient spectra...

---

### 16. Jeffreys Flow: Robust Boltzmann Generators for Rare Event Sampling via Parallel Tempering Distillation

**Authors:** Guang Lin, Christian Moya, Di Qi, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05303v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05303v1)

**Summary:** Sampling physical systems with rough energy landscapes is hindered by rare events and metastable trapping. While Boltzmann generators already offer a solution, their reliance on the reverse Kullback--Leibler divergence frequently induces catastrophic mode collapse, missing specific modes in multi-modal distributions. Here, we introduce the Jeffreys Flow, a robust generative framework that mitigates this failure by distilling empirical sampling data from Parallel Tempering trajectories using the ...

---

### 17. fastml: Guarded Resampling Workflows for Safer Automated Machine Learning in R

**Authors:** Selcuk Korkmaz, Dincer Goksuluk, Eda Karaismailoglu

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05225v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05225v1)

**Summary:** Preprocessing leakage arises when scaling, imputation, or other data-dependent transformations are estimated before resampling, inflating apparent performance while remaining hard to detect. We present fastml, an R package that provides a single-call interface for leakage-aware machine learning through guarded resampling, where preprocessing is re-estimated inside each resample and applied to the corresponding assessment data. The package supports grouped and time-ordered resampling, blocks high...

---

### 18. Blind-Spot Mass: A Good-Turing Framework for Quantifying Deployment Coverage Risk in Machine Learning Systems

**Authors:** Biplab Pal, Santanu Bhattacharya, Madanjit Singh

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05057v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05057v1)

**Summary:** Blind-spot mass is a Good-Turing framework for quantifying deployment coverage risk in machine learning. In modern ML systems, operational state distributions are often heavy-tailed, implying that a long tail of valid but rare states is structurally under-supported in finite training and evaluation data. This creates a form of 'coverage blindness': models can appear accurate on standard test sets yet remain unreliable across large regions of the deployment state space.   We propose blind-spot ma...

---

### 19. Muon Dynamics as a Spectral Wasserstein Flow

**Authors:** Gabriel Peyré

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04891v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04891v1)

**Summary:** Gradient normalization is central in deep-learning optimization because it stabilizes training and reduces sensitivity to scale. For deep architectures, parameters are naturally grouped into matrices or blocks, so spectral normalizations are often more faithful than coordinatewise Euclidean ones; Muon is the main motivating example of this paper. More broadly, we study a family of spectral normalization rules, ranging from ordinary gradient descent to Muon and intermediate Schatten-type schemes,...

---

### 20. Noise Immunity in In-Context Tabular Learning: An Empirical Robustness Analysis of TabPFN's Attention Mechanisms

**Authors:** James Hu, Mahdi Ghelichi

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04868v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04868v1)

**Summary:** Tabular foundation models (TFMs) such as TabPFN (Tabular Prior-Data Fitted Network) are designed to generalize across heterogeneous tabular datasets through in-context learning (ICL). They perform prediction in a single forward pass conditioned on labeled examples without dataset-specific parameter updates. This paradigm is particularly attractive in industrial domains (e.g., finance and healthcare) where tabular prediction is pervasive. Retraining a bespoke model for each new table can be costl...

---

### 21. A Robust SINDy Autoencoder for Noisy Dynamical System Identification

**Authors:** Kairui Ding

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04829v1)

**Summary:** Sparse identification of nonlinear dynamics (SINDy) has been widely used to discover the governing equations of a dynamical system from data. It uses sparse regression techniques to identify parsimonious models of unknown systems from a library of candidate functions. Therefore, it relies on the assumption that the dynamics are sparsely represented in the coordinate system used. To address this limitation, one seeks a coordinate transformation that provides reduced coordinates capable of reconst...

---

### 22. Partially deterministic sampling for compressed sensing with denoising guarantees

**Authors:** Yaniv Plan, Matthew S. Scott, Ozgur Yilmaz

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04802v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04802v1)

**Summary:** We study compressed sensing when the sampling vectors are chosen from the rows of a unitary matrix. In the literature, these sampling vectors are typically chosen randomly; the use of randomness has enabled major empirical and theoretical advances in the field. However, in practice there are often certain crucial sampling vectors, in which case practitioners will depart from the theory and sample such rows deterministically. In this work, we derive an optimized sampling scheme for Bernoulli sele...

---

### 23. A Muon-Accelerated Algorithm for Low Separation Rank Tensor Generalized Linear Models

**Authors:** Xiao Liang, Shuang Li

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04726v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04726v1)

**Summary:** Tensor-valued data arise naturally in multidimensional signal and imaging problems, such as biomedical imaging. When incorporated into generalized linear models (GLMs), naive vectorization can destroy their multi-way structure and lead to high-dimensional, ill-posed estimation. To address this challenge, Low Separation Rank (LSR) decompositions reduce model complexity by imposing low-rank multilinear structure on the coefficient tensor. A representative approach for estimating LSR-based tensor G...

---

### 24. The Infinite-Dimensional Nature of Spectroscopy and Why Models Succeed, Fail, and Mislead

**Authors:** Umberto Michelucci, Francesca Venturini

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04717v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04717v1)

**Summary:** Machine learning (ML) models have achieved strikingly high accuracies in spectroscopic classification tasks, often without a clear proof that those models used chemically meaningful features. Existing studies have linked these results to data preprocessing choices, noise sensitivity, and model complexity, but no unifying explanation is available so far. In this work, we show that these phenomena arise naturally from the intrinsic high dimensionality of spectral data. Using a theoretical analysis...

---

### 25. Minimaxity and Admissibility of Bayesian Neural Networks

**Authors:** Daniel Andrew Coulson, Martin T. Wells

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04673v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04673v1)

**Summary:** Bayesian neural networks (BNNs) offer a natural probabilistic formulation for inference in deep learning models. Despite their popularity, their optimality has received limited attention through the lens of statistical decision theory. In this paper, we study decision rules induced by deep, fully connected feedforward ReLU BNNs in the normal location model under quadratic loss. We show that, for fixed prior scales, the induced Bayes decision rule is not minimax. We then propose a hyperprior on t...

---

### 26. Generative Path-Law Jump-Diffusion: Sequential MMD-Gradient Flows and Generalisation Bounds in Marcus-Signature RKHS

**Authors:** Daniel Bloch

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05008v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05008v1)

**Summary:** This paper introduces a novel generative framework for synthesising forward-looking, càdlàg stochastic trajectories that are sequentially consistent with time-evolving path-law proxies, thereby incorporating anticipated structural breaks, regime shifts, and non-autonomous dynamics. By framing path synthesis as a sequential matching problem on restricted Skorokhod manifolds, we develop the \textit{Anticipatory Neural Jump-Diffusion} (ANJD) flow, a generative mechanism that effectively inverts the...

---

### 27. Noisy Nonreciprocal Pairwise Comparisons: Scale Variation, Noise Calibration, and Admissible Ranking Regions

**Authors:** Jean-Pierre Magnot

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04588v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04588v1)

**Summary:** Pairwise comparisons are widely used in decision analysis, preference modeling, and evaluation problems. In many practical situations, the observed comparison matrix is not reciprocal. This lack of reciprocity is often treated as a defect to be corrected immediately. In this article, we adopt a different point of view: part of the nonreciprocity may reflect a genuine variation in the evaluation scale, while another part is due to random perturbations.   We introduce an additive model in which th...

---

### 28. Generative Modeling under Non-Monotonic MAR Missingness via Approximate Wasserstein Gradient Flows

**Authors:** Gitte Kremling, Jeffrey Näf, Johannes Lederer

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04567v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04567v1)

**Summary:** The prevalence of missing values in data science poses a substantial risk to any further analyses. Despite a wealth of research, principled nonparametric methods to deal with general non-monotone missingness are still scarce. Instead, ad-hoc imputation methods are often used, for which it remains unclear whether the correct distribution can be recovered. In this paper, we propose FLOWGEM, a principled iterative method for generating a complete dataset from a dataset with values Missing at Random...

---

### 29. Relative Density Ratio Optimization for Stable and Statistically Consistent Model Alignment

**Authors:** Hiroshi Takahashi, Tomoharu Iwata, Atsutoshi Kumagai, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04410v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04410v1)

**Summary:** Aligning language models with human preferences is essential for ensuring their safety and reliability. Although most existing approaches assume specific human preference models such as the Bradley-Terry model, this assumption may fail to accurately capture true human preferences, and consequently, these methods lack statistical consistency, i.e., the guarantee that language models converge to the true human preference as the number of samples increases. In contrast, direct density ratio optimiz...

---

### 30. Attributed Network Alignment: Statistical Limits and Efficient Algorithm

**Authors:** Dong Huang, Chenyang Tian, Pengkun Yang

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04365v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04365v1)

**Summary:** This paper studies the problem of recovering a hidden vertex correspondence between two correlated graphs when both edge weights and node features are observed. While most existing work on graph alignment relies primarily on edge information, many real-world applications provide informative node features in addition to graph topology. To capture this setting, we introduce the featured correlated Gaussian Wigner model, where two graphs are coupled through an unknown vertex permutation, and the no...

---

### 31. Generative models for decision-making under distributional shift

**Authors:** Xiuyuan Cheng, Yunqin Zhu, Yao Xie

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04342v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04342v1)

**Summary:** Many data-driven decision problems are formulated using a nominal distribution estimated from historical data, while performance is ultimately determined by a deployment distribution that may be shifted, context-dependent, partially observed, or stress-induced. This tutorial presents modern generative models, particularly flow- and score-based methods, as mathematical tools for constructing decision-relevant distributions. From an operations research perspective, their primary value lies not in ...

---

### 32. Avoiding Non-Integrable Beliefs in Expectation Propagation

**Authors:** Zilu Zhao, Jichao Chen, Dirk Slock

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04264v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04264v1)

**Summary:** Expectation Propagation (EP) is a widely used iterative message-passing algorithm that decomposes a global inference problem into multiple local ones. It approximates marginal distributions as ``beliefs'' using intermediate functions called ``messages''. It has been shown that the stationary points of EP are the same as corresponding constrained Bethe Free Energy (BFE) optimization problem. Therefore, EP is an iterative method of optimizing the constrained BFE. However, the iterative method may ...

---

### 33. Robust Regression with Adaptive Contamination in Response: Optimal Rates and Computational Barriers

**Authors:** Ilias Diakonikolas, Chao Gao, Daniel M. Kane, et al.

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04228v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04228v1)

**Summary:** We study robust regression under a contamination model in which covariates are clean while the responses may be corrupted in an adaptive manner. Unlike the classical Huber's contamination model, where both covariates and responses may be contaminated and consistent estimation is impossible when the contamination proportion is a non-vanishing constant, it turns out that the clean-covariate setting admits strictly improved statistical guarantees. Specifically, we show that the additional informati...

---

### 34. Sharp asymptotic theory for Q-learning with LDTZ learning rate and its generalization

**Authors:** Soham Bonnerjee, Zhipeng Lou, Wei Biao Wu

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04218v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04218v1)

**Summary:** Despite the sustained popularity of Q-learning as a practical tool for policy determination, a majority of relevant theoretical literature deals with either constant ($η_{t}\equiv η$) or polynomially decaying ($η_{t} = ηt^{-α}$) learning schedules. However, it is well known that these choices suffer from either persistent bias or prohibitively slow convergence. In contrast, the recently proposed linear decay to zero (\texttt{LD2Z}: $η_{t,n}=η(1-t/n)$) schedule has shown appreciable empirical per...

---

### 35. The Geometric Alignment Tax: Tokenization vs. Continuous Geometry in Scientific Foundation Models

**Authors:** Prashant C. Raju

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04155v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04155v1)

**Summary:** Foundation models for biology and physics optimize predictive accuracy, but their internal representations systematically fail to preserve the continuous geometry of the systems they model. We identify the root cause: the Geometric Alignment Tax, an intrinsic cost of forcing continuous manifolds through discrete categorical bottlenecks. Controlled ablations on synthetic dynamical systems demonstrate that replacing cross-entropy with a continuous head on an identical encoder reduces geometric dis...

---

### 36. The Hiremath Early Detection (HED) Score: A Measure-Theoretic Evaluation Standard for Temporal Intelligence

**Authors:** Prakul Sunil Hiremath

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04993v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04993v1)

**Summary:** We introduce the Hiremath Early Detection (HED) Score, a principled, measure-theoretic evaluation criterion for quantifying the time-value of information in systems operating over non-stationary stochastic processes subject to abrupt regime transitions. Existing evaluation paradigms, chiefly the ROC/AUC framework and its downstream variants, are temporally agnostic: they assign identical credit to a detection at t + 1 and a detection at t + tau for arbitrarily large tau. This indifference to lat...

---

### 37. Autoencoder-Based Parameter Estimation for Superposed Multi-Component Damped Sinusoidal Signals

**Authors:** Momoka Iida, Hayato Motohashi, Hirotaka Takahashi

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.03985v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03985v1)

**Summary:** Damped sinusoidal oscillations are widely observed in many physical systems, and their analysis provides access to underlying physical properties. However, parameter estimation becomes difficult when the signal decays rapidly, multiple components are superposed, and observational noise is present. In this study, we develop an autoencoder-based method that uses the latent space to estimate the frequency, phase, decay time, and amplitude of each component in noisy multi-component damped sinusoidal...

---

### 38. Nearly Optimal Best Arm Identification for Semiparametric Bandits

**Authors:** Seok-Jin Kim

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.03969v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03969v1)

**Summary:** We study fixed-confidence Best Arm Identification (BAI) in semiparametric bandits, where rewards are linear in arm features plus an unknown additive baseline shift. Unlike linear-bandit BAI, this setting requires orthogonalized regression, and its instance-optimal sample complexity has remained open. For the transductive setting, we establish an attainable instance-dependent lower bound characterized by the corresponding linear-bandit complexity on shifted features. We then propose a computation...

---

### 39. Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling

**Authors:** Yongchang Hao, Lili Mou

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04987v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04987v1)

**Summary:** Speculative sampling (SpS) has been successful in accelerating the decoding throughput of auto-regressive large language models by leveraging smaller draft models. SpS strictly enforces the generated distribution to match that of the verifier LLM. This is unnecessarily restrictive as slight variations of the verifier's distribution, such as sampling with top-$k$ or temperature, would also be acceptable. Typical acceptance sampling (TAS) alleviates this issue by accepting more tokens using entrop...

---

### 40. Fused Multinomial Logistic Regression Utilizing Summary-Level External Machine-learning Information

**Authors:** Chi-Shian Dai, Jun Shao

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.03939v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03939v1)

**Summary:** In many modern applications, a carefully designed primary study provides individual-level data for interpretable modeling, while summary-level external information is available through black-box, efficient, and nonparametric machine-learning predictions. Although summary-level external information has been studied in the data integration literature, there is limited methodology for leveraging external nonparametric machine-learning predictions to improve statistical inference in the primary stud...

---

### 41. Biconvex Biclustering

**Authors:** Sam Rosen, Eric C. Chi, Jason Xu

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.03936v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03936v1)

**Summary:** This article proposes a biconvex modification to convex biclustering in order to improve its performance in high-dimensional settings. In contrast to heuristics that discard a subset of noisy features a priori, our method jointly learns and accordingly weighs informative features while discovering biclusters. Moreover, the method is adaptive to the data, and is accompanied by an efficient algorithm based on proximal alternating minimization, complete with detailed guidance on hyperparameter tuni...

---

### 42. A Bayesian Information-Theoretic Approach to Data Attribution

**Authors:** Dharmesh Tailor, Nicolò Felicioni, Kamil Ciosek

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03858v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03858v1)

**Summary:** Training Data Attribution (TDA) seeks to trace model predictions back to influential training examples, enhancing interpretability and safety. We formulate TDA as a Bayesian information-theoretic problem: subsets are scored by the information loss they induce - the entropy increase at a query when removed. This criterion credits examples for resolving predictive uncertainty rather than label noise. To scale to modern networks, we approximate information loss using a Gaussian Process surrogate bu...

---

### 43. Cross Spectra Break the Single-Channel Impossibility

**Authors:** Yuda Bi, Vince D Calhoun

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03775v2) | 📄 [PDF](https://arxiv.org/pdf/2604.03775v2)

**Summary:** Lucente et al. proved that no time-irreversibility measure can detect departure from equilibrium in a scalar Gaussian time series from a linear system. We show that a second observed channel sharing the same hidden driver overcomes this impossibility: the cross-spectral block, structurally inaccessible to any single-channel measure, provides qualitatively new detectability. Under the diagonal null hypothesis, the cross-spectral detectability coefficient $\Scross$ (the leading quartic-order cross...

---

### 44. Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding

**Authors:** Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03772v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03772v1)

**Summary:** Data-driven decision making frequently relies on predicting counterfactual outcomes. In practice, researchers commonly train counterfactual prediction models on a source dataset to inform decisions on a possibly separate target population. Conformal prediction has arisen as a popular method for producing assumption-lean prediction intervals for counterfactual outcomes that would arise under different treatment decisions in the target population of interest. However, existing methods require that...

---

### 45. StrADiff: A Structured Source-Wise Adaptive Diffusion Framework for Linear and Nonlinear Blind Source Separation

**Authors:** Yuan-Hao Wei

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.04973v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04973v1)

**Summary:** This paper presents a Structured Source-Wise Adaptive Diffusion Framework for linear and nonlinear blind source separation. The framework interprets each latent dimension as a source component and assigns to it an individual adaptive diffusion mechanism, thereby establishing source-wise latent modeling rather than relying on a single shared latent prior. The resulting formulation learns source recovery and the mixing/reconstruction process jointly within a unified end-to-end objective, allowing ...

---

### 46. The Generalised Kernel Covariance Measure

**Authors:** Luca Bergen, Dino Sejdinovic, Vanessa Didelez

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03721v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03721v1)

**Summary:** We consider the problem of conditional independence (CI) testing and adopt a kernel-based approach. Kernel-based CI tests embed variables in reproducing kernel Hilbert spaces, regress their embeddings on the conditioning variables, and test the resulting residuals for marginal independence. This approach yields tests that are sensitive to a broad range of conditional dependencies. Existing methods, however, rely heavily on kernel ridge regression, which is computationally expensive when properly...

---

### 47. Fréchet Regression on the Bures-Wasserstein Manifold

**Authors:** Duc Toan Nguyen, César A. Uribe

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03566v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03566v1)

**Summary:** Fréchet regression, or conditional Barycenters, is a flexible framework for modeling relationships between covariates (usually Euclidean) and response variables on general metric spaces, e.g., probability distributions or positive definite matrices. However, in contrast to classical barycenter problems, computing conditional counterparts in many non-Euclidean spaces remains an open challenge, as they yield non-convex optimization problems with an affine structure. In this work, we study the exis...

---

### 48. Choosing the Right Regularizer for Applied ML: Simulation Benchmarks of Popular Scikit-learn Regularization Frameworks

**Authors:** Benjamin S. Knight, Ahsaas Bajaj

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03541v2) | 📄 [PDF](https://arxiv.org/pdf/2604.03541v2)

**Summary:** This study surveys the historical development of regularization, tracing its evolution from stepwise regression in the 1960s to recent advancements in formal error control, structured penalties for non-independent features, Bayesian methods, and l0-based regularization (among other techniques). We empirically evaluate the performance of four canonical frameworks -- Ridge, Lasso, ElasticNet, and Post-Lasso OLS -- across 134,400 simulations spanning a 7-dimensional manifold grounded in eight produ...

---

### 49. Nonparametric Regression Discontinuity Designs with Survival Outcomes

**Authors:** Maximilian Schuessler, Erik Sverdrup, Robert Tibshirani, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03502v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03502v1)

**Summary:** Quasi-experimental evaluations are central for generating real-world causal evidence and complementing insights from randomized trials. The regression discontinuity design (RDD) is a quasi-experimental design that can be used to estimate the causal effect of treatments that are assigned based on a running variable crossing a threshold. Such threshold-based rules are ubiquitous in healthcare, where predictive and prognostic biomarkers frequently guide treatment decisions. However, standard RD est...

---

### 50. Learning Nonlinear Regime Transitions via Semi-Parametric State-Space Models

**Authors:** Prakul Sunil Hiremath

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.04963v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04963v1)

**Summary:** We develop a semi-parametric state-space model for time-series data with latent regime transitions. Classical Markov-switching models use fixed parametric transition functions, such as logistic or probit links, which restrict flexibility when transitions depend on nonlinear and context-dependent effects. We replace this assumption with learned functions $f_0, f_1 \in \calH$, where $\calH$ is either a reproducing kernel Hilbert space or a spline approximation space, and define transition probabil...

---

