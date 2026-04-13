# arXiv Daily Digest - 2026-04-13

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism

**Authors:** Hadas Orgad, Boyi Wei, Kaden Zheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09544v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09544v1)

**Summary:** Large language models (LLMs) undergo alignment training to avoid harmful behaviors, yet the resulting safeguards remain brittle: jailbreaks routinely bypass them, and fine-tuning on narrow domains can induce ``emergent misalignment'' that generalizes broadly. Whether this brittleness reflects a fundamental lack of coherent internal organization for harmfulness remains unclear. Here we use targeted weight pruning as a causal intervention to probe the internal organization of harmfulness in LLMs. ...

---

### 2. Case-Grounded Evidence Verification: A Framework for Constructing Evidence-Sensitive Supervision

**Authors:** Soroosh Tayebi Arasteh, Mehdi Joodaki, Mahshad Lotfinia, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09537v1)

**Summary:** Evidence-grounded reasoning requires more than attaching retrieved text to a prediction: a model should make decisions that depend on whether the provided evidence supports the target claim. In practice, this often fails because supervision is weak, evidence is only loosely tied to the claim, and evaluation does not test evidence dependence directly. We introduce case-grounded evidence verification, a general framework in which a model receives a local case context, external evidence, and a stru...

---

### 3. Seeing is Believing: Robust Vision-Guided Cross-Modal Prompt Learning under Label Noise

**Authors:** Zibin Geng, Xuefeng Jiang, Jia Li, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09532v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09532v1)

**Summary:** Prompt learning is a parameter-efficient approach for vision-language models, yet its robustness under label noise is less investigated. Visual content contains richer and more reliable semantic information, which remains more robust under label noise. However, the prompt itself is highly susceptible to label noise. Motivated by this intuition, we propose VisPrompt, a lightweight and robust vision-guided prompt learning framework for noisy-label settings. Specifically, we exploit a cross-modal a...

---

### 4. VisionFoundry: Teaching VLMs Visual Perception with Synthetic Images

**Authors:** Guanyu Zhou, Yida Yin, Wenhao Chai, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09531v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09531v1)

**Summary:** Vision-language models (VLMs) still struggle with visual perception tasks such as spatial understanding and viewpoint recognition. One plausible contributing factor is that natural image datasets provide limited supervision for low-level visual skills. This motivates a practical question: can targeted synthetic supervision, generated from only a task keyword such as Depth Order, address these weaknesses? To investigate this question, we introduce VisionFoundry, a task-aware synthetic data genera...

---

### 5. VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning

**Authors:** Wenyi Xiao, Xinchi Xu, Leilei Gan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09529v1)

**Summary:** Large Vision Language Models (LVLMs) achieve strong multimodal reasoning but frequently exhibit hallucinations and incorrect responses with high certainty, which hinders their usage in high-stakes domains. Existing verbalized confidence calibration methods, largely developed for text-only LLMs, typically optimize a single holistic confidence score using binary answer-level correctness. This design is mismatched to LVLMs: an incorrect prediction may arise from perceptual failures or from reasonin...

---

### 6. Envisioning the Future, One Step at a Time

**Authors:** Stefan Andreas Baumann, Jannik Wiese, Tommaso Martorella, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09527v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09527v1)

**Summary:** Accurately anticipating how complex, diverse scenes will evolve requires models that represent uncertainty, simulate along extended interaction chains, and efficiently explore many plausible futures. Yet most existing approaches rely on dense video or latent-space prediction, expending substantial capacity on dense appearance rather than on the underlying sparse trajectories of points in the scene. This makes large-scale exploration of future hypotheses costly and limits performance when long-ho...

---

### 7. Semantic Rate-Distortion for Bounded Multi-Agent Communication: Capacity-Derived Semantic Spaces and the Communication Cost of Alignment

**Authors:** Anthony T. Nixon

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09521v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09521v1)

**Summary:** When two agents of different computational capacities interact with the same environment, they need not compress a common semantic alphabet differently; they can induce different semantic alphabets altogether. We show that the quotient POMDP $Q_{m,T}(M)$ - the unique coarsest abstraction consistent with an agent's capacity - serves as a capacity-derived semantic space for any bounded agent, and that communication between heterogeneous agents exhibits a sharp structural phase transition. Below a ...

---

### 8. VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning

**Authors:** Yucheng Shen, Jiulong Wu, Jizhou Huang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09508v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09508v1)

**Summary:** Visual Retrieval-Augmented Generation (VRAG) empowers Vision-Language Models to retrieve and reason over visually rich documents. To tackle complex queries requiring multi-step reasoning, agentic VRAG systems interleave reasoning with iterative retrieval.. However, existing agentic VRAG faces two critical bottlenecks. (1) Visual Evidence Sparsity: key evidence is scattered across pages yet processed in isolation, hindering cross-page reasoning; moreover, fine-grained intra-image evidence often r...

---

### 9. Strategic Algorithmic Monoculture:Experimental Evidence from Coordination Games

**Authors:** Gonzalo Ballestero, Hadi Hosseini, Samarth Khanna, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09502v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09502v1)

**Summary:** AI agents increasingly operate in multi-agent environments where outcomes depend on coordination. We distinguish primary algorithmic monoculture -- baseline action similarity -- from strategic algorithmic monoculture, whereby agents adjust similarity in response to incentives. We implement a simple experimental design that cleanly separates these forces, and deploy it on human and large language model (LLM) subjects. LLMs exhibit high levels of baseline similarity (primary monoculture) and, like...

---

### 10. BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation

**Authors:** Hippolyte Gisserot-Boukhlef, Nicolas Boizard, Emmanuel Malherbe, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09497v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09497v1)

**Summary:** Accurate evaluation is central to the large language model (LLM) ecosystem, guiding model selection and downstream adoption across diverse use cases. In practice, however, evaluating generative outputs typically relies on rigid lexical methods to extract and assess answers, which can conflate a model's true problem-solving ability with its compliance with predefined formatting guidelines. While recent LLM-as-a-Judge approaches mitigate this issue by assessing semantic correctness rather than str...

---

### 11. RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retrieval

**Authors:** Kyle Whitecross, Negin Rahimi

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09494v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09494v1)

**Summary:** We propose RecaLLM, a set of reasoning language models post-trained to make effective use of long-context information. In-context retrieval, which identifies relevant evidence from context, and reasoning are deeply intertwined: retrieval supports reasoning, while reasoning often determines what must be retrieved. However, their interaction remains largely underexplored. In preliminary experiments on several open-source LLMs, we observe that in-context retrieval performance substantially degrades...

---

### 12. XFED: Non-Collusive Model Poisoning Attack Against Byzantine-Robust Federated Classifiers

**Authors:** Israt Jahan Mouri, Muhammad Ridowan, Muhammad Abdullah Adnan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09489v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09489v1)

**Summary:** Model poisoning attacks pose a significant security threat to Federated Learning (FL). Most existing model poisoning attacks rely on collusion, requiring adversarial clients to coordinate by exchanging local benign models and synchronizing the generation of their poisoned updates. However, sustaining such coordination is increasingly impractical in real-world FL deployments, as it effectively requires botnet-like control over many devices. This approach is costly to maintain and highly vulnerabl...

---

### 13. Process Reward Agents for Steering Knowledge-Intensive Reasoning

**Authors:** Jiwoong Sohn, Tomasz Sternal, Kenneth Styppa, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09482v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09482v1)

**Summary:** Reasoning in knowledge-intensive domains remains challenging as intermediate steps are often not locally verifiable: unlike math or code, evaluating step correctness may require synthesizing clues across large external knowledge sources. As a result, subtle errors can propagate through reasoning traces, potentially never to be detected. Prior work has proposed process reward models (PRMs), including retrieval-augmented variants, but these methods operate post hoc, scoring completed trajectories,...

---

### 14. SafeMind: A Risk-Aware Differentiable Control Framework for Adaptive and Safe Quadruped Locomotion

**Authors:** Zukun Zhang, Kai Shu, Mingqiao Mo

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09474v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09474v1)

**Summary:** Learning-based quadruped controllers achieve impressive agility but typically lack formal safety guarantees under model uncertainty, perception noise, and unstructured contact conditions. We introduce SafeMind, a differentiable stochastic safety-control framework that unifies probabilistic Control Barrier Functions with semantic context understanding and meta-adaptive risk calibration. SafeMind explicitly models epistemic and aleatoric uncertainty through a variance-aware barrier constraint embe...

---

### 15. E3-TIR: Enhanced Experience Exploitation for Tool-Integrated Reasoning

**Authors:** Weiyang Guo, Zesheng Shi, Liye Zhao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09455v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09455v1)

**Summary:** While Large Language Models (LLMs) have demonstrated significant potential in Tool-Integrated Reasoning (TIR), existing training paradigms face significant limitations: Zero-RL suffers from inefficient exploration and mode degradation due to a lack of prior guidance, while SFT-then-RL is limited by high data costs and capability plateaus caused by low-entropy collapse. To address these challenges, we propose E3-TIR (Enhanced Experience Exploitation), a warm-up paradigm for the early stages of ag...

---

### 16. SafeAdapt: Provably Safe Policy Updates in Deep Reinforcement Learning

**Authors:** Maksim Anisimov, Francesco Belardinelli, Matthew Wicker

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09452v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09452v1)

**Summary:** Safety guarantees are a prerequisite to the deployment of reinforcement learning (RL) agents in safety-critical tasks. Often, deployment environments exhibit non-stationary dynamics or are subject to changing performance goals, requiring updates to the learned policy. This leads to a fundamental challenge: how to update an RL policy while preserving its safety properties on previously encountered tasks? The majority of current approaches either do not provide formal guarantees or verify policy s...

---

### 17. ECHO: Efficient Chest X-ray Report Generation with One-step Block Diffusion

**Authors:** Lifeng Chen, Tianqi You, Hao Liu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09450v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09450v1)

**Summary:** Chest X-ray report generation (CXR-RG) has the potential to substantially alleviate radiologists' workload. However, conventional autoregressive vision--language models (VLMs) suffer from high inference latency due to sequential token decoding. Diffusion-based models offer a promising alternative through parallel generation, but they still require multiple denoising iterations. Compressing multi-step denoising to a single step could further reduce latency, but often degrades textual coherence du...

---

### 18. Many-Tier Instruction Hierarchy in LLM Agents

**Authors:** Jingyu Zhang, Tianjian Li, William Jurayj, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09443v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09443v1)

**Summary:** Large language model agents receive instructions from many sources-system messages, user prompts, tool outputs, and more-each carrying different levels of trust and authority. When these instructions conflict, models must reliably follow the highest-privilege instruction to remain safe and effective. The dominant paradigm, instruction hierarchy (IH), assumes a fixed, small set of privilege levels (typically fewer than five) defined by rigid role labels (e.g., system > user). This is inadequate f...

---

### 19. TME-PSR: Time-aware, Multi-interest, and Explanation Personalization for Sequential Recommendation

**Authors:** Qingzhuo Wang, Leilei Wen, Juntao Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09439v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09439v1)

**Summary:** In this paper, we propose a sequential recommendation model that integrates Time-aware personalization, Multi-interest personalization, and Explanation personalization for Personalized Sequential Recommendation (TME-PSR). That is, we consider the differences across different users in temporal rhythm preference, multiple fine-grained latent interests, and the personalized semantic alignment between recommendations and explanations. Specifically, the proposed TME-PSR model employs a dual-view gate...

---

### 20. Physics-guided surrogate learning enables zero-shot control of turbulent wings

**Authors:** Yuning Wang, Pol Suarez, Mathis Bode, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09434v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09434v1)

**Summary:** Turbulent boundary layers over aerodynamic surfaces are a major source of aircraft drag, yet their control remains challenging due to multiscale dynamics and spatial variability, particularly under adverse pressure gradients. Reinforcement learning has outperformed state-of-the-art strategies in canonical flows, but its application to realistic geometries is limited by computational cost and transferability. Here we show that these limitations can be overcome by exploiting local structures of wa...

---

### 21. On the Representational Limits of Quantum-Inspired 1024-D Document Embeddings: An Experimental Evaluation Framework

**Authors:** Dario Maio

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09430v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09430v1)

**Summary:** Text embeddings are central to modern information retrieval and Retrieval-Augmented Generation (RAG). While dense models derived from Large Language Models (LLMs) dominate current practice, recent work has explored quantum-inspired alternatives motivated by the geometric properties of Hilbert-like spaces and their potential to encode richer semantic structure.   This paper presents an experimental framework for constructing quantum-inspired 1024-dimensional document embeddings based on overlappi...

---

### 22. Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories

**Authors:** Wonbong Jang, Shikun Liu, Soubhik Sanyal, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09429v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09429v1)

**Summary:** Recovering camera parameters from images and rendering scenes from novel viewpoints have long been treated as separate tasks in computer vision and graphics. This separation breaks down when image coverage is sparse or poses are ambiguous, since each task needs what the other produces. We propose Rays as Pixels, a Video Diffusion Model (VDM) that learns a joint distribution over videos and camera trajectories. We represent each camera as dense ray pixels (raxels) and denoise them jointly with vi...

---

### 23. Three Modalities, Two Design Probes, One Prototype, and No Vision: Experience-Based Co-Design of a Multi-modal 3D Data Visualization Tool

**Authors:** Sanchita S. Kamath, Aziz N Zeidieh, Venkatesh Potluri, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09426v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09426v1)

**Summary:** Three-dimensional (3D) data visualizations, such as surface plots, are vital in STEM fields from biomedical imaging to spectroscopy, yet remain largely inaccessible to blind and low-vision (BLV) people. To address this gap, we conducted an Experience-Based Co-Design with BLV co-designers with expertise in non-visual data representations to create an accessible, multi-modal, web-native visualization tool. Using a multi-phase methodology, our team of five BLV and one non-BLV researcher(s) particip...

---

### 24. Do We Really Need to Approach the Entire Pareto Front in Many-Objective Bayesian Optimisation?

**Authors:** Chao Jiang, Jingyu Huang, Miqing Li

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09417v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09417v1)

**Summary:** Many-objective optimisation, a subset of multi-objective optimisation, involves optimisation problems with more than three objectives. As the number of objectives increases, the number of solutions needed to adequately represent the entire Pareto front typically grows substantially. This makes it challenging, if not infeasible, to design a search algorithm capable of effectively exploring the entire Pareto front. This difficulty is particularly acute in the Bayesian optimisation paradigm, where ...

---

### 25. PhysInOne: Visual Physics Learning and Reasoning in One Suite

**Authors:** Siyuan Zhou, Hejun Wang, Hu Cheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09415v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09415v1)

**Summary:** We present PhysInOne, a large-scale synthetic dataset addressing the critical scarcity of physically-grounded training data for AI systems. Unlike existing datasets limited to merely hundreds or thousands of examples, PhysInOne provides 2 million videos across 153,810 dynamic 3D scenes, covering 71 basic physical phenomena in mechanics, optics, fluid dynamics, and magnetism. Distinct from previous works, our scenes feature multiobject interactions against complex backgrounds, with comprehensive ...

---

### 26. Yes, But Not Always. Generative AI Needs Nuanced Opt-in

**Authors:** Wiebke Hutiri, Morgan Scheuerman, Shruti Nagpal, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09413v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09413v1)

**Summary:** This paper argues that a one-size-fits-all approach to specifying consent for the use of creative works in generative AI is insufficient. Real-world ownership and rights holder structures, the imitation of artistic styles and likeness, and the limitless contexts of use of AI outputs make the status quo of binary consent with opt-in by default untenable. To move beyond the current impasse, we consider levers of control in generative AI workflows at training, inference, and dissemination. Based on...

---

### 27. HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?

**Authors:** Mohamed Elfeki, Tu Trinh, Kelvin Luu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09408v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09408v1)

**Summary:** Frontier coding agents solve complex tasks when given complete context but collapse when specifications are incomplete or ambiguous. The bottleneck is not raw capability, but judgment: knowing when to act autonomously and when to ask for help. Current benchmarks are blind to this failure mode. They supply unambiguous detailed instructions and solely reward execution correctness, so an agent that makes a lucky guess for a missing requirement will score identically to one that would have asked to ...

---

### 28. The AI Codebase Maturity Model: From Assisted Coding to Self-Sustaining Systems

**Authors:** Andy Anderson

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09388v1)

**Summary:** AI coding tools are widely adopted, but most teams plateau at prompt-and-review without a framework for systematic progression. This paper presents the AI Codebase Maturity Model (ACMM), a 5-level framework describing how codebases evolve from basic AI-assisted coding to self-sustaining systems. Inspired by CMMI, each level is defined by its feedback loop topology the specific mechanisms that must exist before the next level becomes possible. I validate the model through a 4-month experience rep...

---

### 29. BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning

**Authors:** Guiyao Tie, Jiawen Shi, Pan Zhou, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09378v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09378v1)

**Summary:** Agent ecosystems increasingly rely on installable skills to extend functionality, and some skills bundle learned model artifacts as part of their execution logic. This creates a supply-chain risk that is not captured by prompt injection or ordinary plugin misuse: a third-party skill may appear benign while concealing malicious behavior inside its bundled model. We present BadSkill, a backdoor attack formulation that targets this model-in-skill threat surface. In BadSkill, an adversary publishes ...

---

### 30. LLM-Rosetta: A Hub-and-Spoke Intermediate Representation for Cross-Provider LLM API Translation

**Authors:** Peng Ding

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09360v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09360v1)

**Summary:** The rapid proliferation of Large Language Model (LLM) providers--each exposing proprietary API formats--has created a fragmented ecosystem where applications become tightly coupled to individual vendors. Switching or bridging providers requires $O(N^2)$ bilateral adapters, impeding portability and multi-provider architectures. We observe that despite substantial syntactic divergence, the major LLM APIs share a common semantic core: the practical challenge is the combinatorial surface of syntacti...

---

### 31. Visually-Guided Policy Optimization for Multimodal Reasoning

**Authors:** Zengbin Wang, Feng Xiong, Liang Lin, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09349v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning ability of vision-language models (VLMs). However, the inherent text-dominated nature of VLMs often leads to insufficient visual faithfulness, characterized by sparse attention activation to visual tokens. More importantly, our empirical analysis reveals that temporal visual forgetting along reasoning steps exacerbates this deficiency. To bridge this gap, we propose Visually-Guided Policy Optimization ...

---

### 32. Mind the Gap Between Spatial Reasoning and Acting! Step-by-Step Evaluation of Agents With Spatial-Gym

**Authors:** Lars Benedikt Kaesberg, Tianyu Yang, Niklas Bauer, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09338v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09338v1)

**Summary:** Spatial reasoning is central to navigation and robotics, yet measuring model capabilities on these tasks remains difficult. Existing benchmarks evaluate models in a one-shot setting, requiring full solution generation in a single response, unlike humans, who work in interactive environments step-by-step. We introduce Spatial-Gym, a Gymnasium environment that isolates spatial constraint reasoning by testing pathfinding in 2D-grid puzzles as a sequential decision task with optional backtracking. W...

---

### 33. Constraint-Aware Corrective Memory for Language-Based Drug Discovery Agents

**Authors:** Maochen Sun, Youzhi Zhang, Gaofeng Meng

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09308v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09308v1)

**Summary:** Large language models are making autonomous drug discovery agents increasingly feasible, but reliable success in this setting is not determined by any single action or molecule. It is determined by whether the final returned set jointly satisfies protocol-level requirements such as set size, diversity, binding quality, and developability. This creates a fundamental control problem: the agent plans step by step, while task validity is decided at the level of the whole candidate set. Existing lang...

---

### 34. SatQNet: Satellite-assisted Quantum Network Entanglement Routing Using Directed Line Graph Neural Networks

**Authors:** Tobias Meuser, Jannis Weil, Aninda Lahiri, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09306v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09306v1)

**Summary:** Quantum networks are expected to become a key enabler for interconnecting quantum devices. In contrast to classical communication networks, however, information transfer in quantum networks is usually restricted to short distances due to physical constraints of entanglement distribution. Satellites can extend entanglement distribution over long distances, but routing in such networks is challenging because satellite motion and stochastic link generation create a highly dynamic quantum topology. ...

---

### 35. SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering

**Authors:** Jingzhi Gong, Ruizhen Gu, Zhiwei Fei, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09297v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09297v1)

**Summary:** Agent skills provide modular, task-specific guidance for LLM- based coding agents, but manually tuning skill bundles to balance success rate, cost, and runtime is expensive and fragile. We present SkillMOO, a multi-objective optimization framework that automatically evolves skill bundles using LLM-proposed edits and NSGA-II survivor selection: a solver agent evaluates candidate skill bundles on coding tasks and an optimizer agent proposes bundle edits based on failure analysis. On three SkillsBe...

---

### 36. SAGE: A Service Agent Graph-guided Evaluation Benchmark

**Authors:** Ling Shi, Yuqin Dai, Ziyin Wang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09285v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09285v1)

**Summary:** The development of Large Language Models (LLMs) has catalyzed automation in customer service, yet benchmarking their performance remains challenging. Existing benchmarks predominantly rely on static paradigms and single-dimensional metrics, failing to account for diverse user behaviors or the strict adherence to structured Standard Operating Procedures (SOPs) required in real-world deployments. To bridge this gap, we propose SAGE (Service Agent Graph-guided Evaluation), a universal multi-agent b...

---

### 37. Mosaic: Multimodal Jailbreak against Closed-Source VLMs via Multi-View Ensemble Optimization

**Authors:** Yuqin Lan, Gen Li, Yuanze Hu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09253v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09253v1)

**Summary:** Vision-Language Models (VLMs) are powerful but remain vulnerable to multimodal jailbreak attacks. Existing attacks mainly rely on either explicit visual prompt attacks or gradient-based adversarial optimization. While the former is easier to detect, the latter produces subtle perturbations that are less perceptible, but is usually optimized and evaluated under homogeneous open-source surrogate-target settings, leaving its effectiveness on commercial closed-source VLMs under heterogeneous setting...

---

### 38. DRBENCHER: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?

**Authors:** Young-Suk Lee, Ramon Fernandez Astudillo, Radu Florian

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09251v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09251v1)

**Summary:** Deep research agents increasingly interleave web browsing with multi-step computation, yet existing benchmarks evaluate these capabilities in isolation, creating a blind spot in assessing real-world performance. We introduce DRBENCHER, a synthetic benchmark generator for questions that require both browsing and computation. It enforces four criteria: verifiability (gold answers are computed by executing parameterized code over knowledge-graph values), complexity (multi-hop entity identification,...

---

### 39. DDSP-QbE++: Improving Speech Quality for Speech Anonymisation for Atypical Speech

**Authors:** Suhita Ghosh, Yamini Sinha, Sebastian Stober

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09246v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09246v1)

**Summary:** Differentiable Digital Signal Processing (DDSP) pipelines for voice conversion rely on subtractive synthesis, where a periodic excitation signal is shaped by a learned spectral envelope to reconstruct the target voice. In DDSP-QbE, the excitation is generated via phase accumulation, producing a sawtooth-like waveform whose abrupt discontinuities introduce aliasing artefacts that manifest perceptually as buzziness and spectral distortion, particularly at higher fundamental frequencies. We propose...

---

### 40. Statistical Properties of the King Wen Sequence: An Anti-Habituation Structure That Does Not Improve Neural Network Training

**Authors:** Augustin Chan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09234v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09234v1)

**Summary:** The King Wen sequence of the I-Ching (c. 1000 BC) orders 64 hexagrams -- states of a six-dimensional binary space -- in a pattern that has puzzled scholars for three millennia. We present a rigorous statistical characterization of this ordering using Monte Carlo permutation analysis against 100,000 random baselines. We find that the sequence has four statistically significant properties: higher-than-random transition distance (98.2nd percentile), negative lag-1 autocorrelation (p=0.037), yang-ba...

---

### 41. Neural Distribution Prior for LiDAR Out-of-Distribution Detection

**Authors:** Zizhao Li, Zhengkang Xiang, Jiayang Ao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09232v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09232v1)

**Summary:** LiDAR-based perception is critical for autonomous driving due to its robustness to poor lighting and visibility conditions. Yet, current models operate under the closed-set assumption and often fail to recognize unexpected out-of-distribution (OOD) objects in the open world. Existing OOD scoring functions exhibit limited performance because they ignore the pronounced class imbalance inherent in LiDAR OOD detection and assume a uniform class distribution. To address this limitation, we propose th...

---

### 42. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 43. GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking

**Authors:** Yunqiang Wang, Hengyuan Na, Di Wu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09222v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09222v1)

**Summary:** Audio large language models (ALLMs) enable rich speech-text interaction, but they also introduce jailbreak vulnerabilities in the audio modality. Existing audio jailbreak methods mainly optimize jailbreak success while overlooking utility preservation, as reflected in transcription quality and question answering performance. In practice, stronger attacks often come at the cost of degraded utility. To study this trade-off, we revisit existing attacks by varying their perturbation coverage in the ...

---

### 44. On the Role of DAG topology in Energy-Aware Cloud Scheduling : A GNN-Based Deep Reinforcement Learning Approach

**Authors:** Anas Hattay, Fred Ngole Mboula, Eric Gascard, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09202v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09202v1)

**Summary:** Cloud providers must assign heterogeneous compute resources to workflow DAGs while balancing competing objectives such as completion time, cost, and energy consumption. In this work, we study a single-workflow, queue-free scheduling setting and consider a graph neural network (GNN)-based deep reinforcement learning scheduler designed to minimize workflow completion time and energy usage. We identify specific out-of-distribution (OOD) conditions under which GNN-based deep reinforcement learning s...

---

### 45. Artificial intelligence can persuade people to take political actions

**Authors:** Kobi Hackenburg, Luke Hewitt, Caroline Wagner, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09200v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09200v1)

**Summary:** There is substantial concern about the ability of advanced artificial intelligence to influence people's behaviour. A rapidly growing body of research has found that AI can produce large persuasive effects on people's attitudes, but whether AI can persuade people to take consequential real-world actions has remained unclear. In two large preregistered experiments N=17,950 responses from 14,779 people), we used conversational AI models to persuade participants on a range of attitudinal and behavi...

---

### 46. Vision Transformers for Preoperative CT-Based Prediction of Histopathologic Chemotherapy Response Score in High-Grade Serous Ovarian Carcinoma

**Authors:** Francesca Fati, Felipe Coutinho, Marika Reinius, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09197v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09197v1)

**Summary:** Purpose. High-grade serous ovarian carcinoma (HGSOC) is characterized by pronounced biological and spatial heterogeneity and is frequently diagnosed at an advanced stage. Neoadjuvant chemotherapy (NACT) followed by delayed primary surgery is commonly employed in patients unsuitable for primary cytoreduction. The Chemotherapy Response Score (CRS) is a validated histopathological biomarker of response to NACT, but it is only available postoperatively. In this study, we investigate whether pre-trea...

---

### 47. Camera Artist: A Multi-Agent Framework for Cinematic Language Storytelling Video Generation

**Authors:** Haobo Hu, Qi Mao, Yuanhang Li, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09195v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09195v1)

**Summary:** We propose Camera Artist, a multi-agent framework that models a real-world filmmaking workflow to generate narrative videos with explicit cinematic language. While recent multi-agent systems have made substantial progress in automating filmmaking workflows from scripts to videos, they often lack explicit mechanisms to structure narrative progression across adjacent shots and deliberate use of cinematic language, resulting in fragmented storytelling and limited filmic quality. To address this, Ca...

---

### 48. Do LLMs Follow Their Own Rules? A Reflexive Audit of Self-Stated Safety Policies

**Authors:** Avni Mittal

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09189v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09189v1)

**Summary:** LLMs internalize safety policies through RLHF, yet these policies are never formally specified and remain difficult to inspect. Existing benchmarks evaluate models against external standards but do not measure whether models understand and enforce their own stated boundaries. We introduce the Symbolic-Neural Consistency Audit (SNCA), a framework that (1) extracts a model's self-stated safety rules via structured prompts, (2) formalizes them as typed predicates (Absolute, Conditional, Adaptive), ...

---

### 49. Generalization and Scaling Laws for Mixture-of-Experts Transformers

**Authors:** Mansour Zoubeirou a Mayaki

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09175v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09175v1)

**Summary:** We develop a theory of generalization and scaling for Mixture-of-Experts (MoE) Transformers that cleanly separates \emph{active} per-input capacity from routing combinatorics. By conditioning on fixed routing patterns and union-bounding across them, we derive a sup-norm covering-number bound whose metric entropy scales with the active parameter budget and incurs a MoE-specific routing overhead. Combined with a standard ERM analysis for squared loss, this yields a generalization bound under a $d$...

---

### 50. Persona-E$^2$: A Human-Grounded Dataset for Personality-Shaped Emotional Responses to Textual Events

**Authors:** Yuqin Yang, Haowu Zhou, Haoran Tu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09162v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09162v1)

**Summary:** Most affective computing research treats emotion as a static property of text, focusing on the writer's sentiment while overlooking the reader's perspective. This approach ignores how individual personalities lead to diverse emotional appraisals of the same event. Although role-playing Large Language Models (LLMs) attempt to simulate such nuanced reactions, they often suffer from "personality illusion'' -- relying on surface-level stereotypes rather than authentic cognitive logic. A critical bot...

---

## cs.CL

**50 papers**

### 1. Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism

**Authors:** Hadas Orgad, Boyi Wei, Kaden Zheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09544v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09544v1)

**Summary:** Large language models (LLMs) undergo alignment training to avoid harmful behaviors, yet the resulting safeguards remain brittle: jailbreaks routinely bypass them, and fine-tuning on narrow domains can induce ``emergent misalignment'' that generalizes broadly. Whether this brittleness reflects a fundamental lack of coherent internal organization for harmfulness remains unclear. Here we use targeted weight pruning as a causal intervention to probe the internal organization of harmfulness in LLMs. ...

---

### 2. Case-Grounded Evidence Verification: A Framework for Constructing Evidence-Sensitive Supervision

**Authors:** Soroosh Tayebi Arasteh, Mehdi Joodaki, Mahshad Lotfinia, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09537v1)

**Summary:** Evidence-grounded reasoning requires more than attaching retrieved text to a prediction: a model should make decisions that depend on whether the provided evidence supports the target claim. In practice, this often fails because supervision is weak, evidence is only loosely tied to the claim, and evaluation does not test evidence dependence directly. We introduce case-grounded evidence verification, a general framework in which a model receives a local case context, external evidence, and a stru...

---

### 3. VisionFoundry: Teaching VLMs Visual Perception with Synthetic Images

**Authors:** Guanyu Zhou, Yida Yin, Wenhao Chai, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09531v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09531v1)

**Summary:** Vision-language models (VLMs) still struggle with visual perception tasks such as spatial understanding and viewpoint recognition. One plausible contributing factor is that natural image datasets provide limited supervision for low-level visual skills. This motivates a practical question: can targeted synthetic supervision, generated from only a task keyword such as Depth Order, address these weaknesses? To investigate this question, we introduce VisionFoundry, a task-aware synthetic data genera...

---

### 4. VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning

**Authors:** Wenyi Xiao, Xinchi Xu, Leilei Gan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09529v1)

**Summary:** Large Vision Language Models (LVLMs) achieve strong multimodal reasoning but frequently exhibit hallucinations and incorrect responses with high certainty, which hinders their usage in high-stakes domains. Existing verbalized confidence calibration methods, largely developed for text-only LLMs, typically optimize a single holistic confidence score using binary answer-level correctness. This design is mismatched to LVLMs: an incorrect prediction may arise from perceptual failures or from reasonin...

---

### 5. Many Ways to Be Fake: Benchmarking Fake News Detection Under Strategy-Driven AI Generation

**Authors:** Xinyu Wang, Sai Koneru, Wenbo Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09514v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09514v1)

**Summary:** Recent advances in large language models (LLMs) have enabled the large-scale generation of highly fluent and deceptive news-like content. While prior work has often treated fake news detection as a binary classification problem, modern fake news increasingly arises through human-AI collaboration, where strategic inaccuracies are embedded within otherwise accurate and credible narratives. These mixed-truth cases represent a realistic and consequential threat, yet they remain underrepresented in e...

---

### 6. You Can't Fight in Here! This is BBS!

**Authors:** Richard Futrell, Kyle Mahowald

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09501v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09501v1)

**Summary:** Norm, the formal theoretical linguist, and Claudette, the computational language scientist, have a lovely time discussing whether modern language models can inform important questions in the language sciences. Just as they are about to part ways until they meet again, 25 of their closest friends show up -- from linguistics, neuroscience, cognitive science, psychology, philosophy, and computer science. We use this discussion to highlight what we see as some common underlying issues: the String St...

---

### 7. BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation

**Authors:** Hippolyte Gisserot-Boukhlef, Nicolas Boizard, Emmanuel Malherbe, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09497v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09497v1)

**Summary:** Accurate evaluation is central to the large language model (LLM) ecosystem, guiding model selection and downstream adoption across diverse use cases. In practice, however, evaluating generative outputs typically relies on rigid lexical methods to extract and assess answers, which can conflate a model's true problem-solving ability with its compliance with predefined formatting guidelines. While recent LLM-as-a-Judge approaches mitigate this issue by assessing semantic correctness rather than str...

---

### 8. RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retrieval

**Authors:** Kyle Whitecross, Negin Rahimi

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09494v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09494v1)

**Summary:** We propose RecaLLM, a set of reasoning language models post-trained to make effective use of long-context information. In-context retrieval, which identifies relevant evidence from context, and reasoning are deeply intertwined: retrieval supports reasoning, while reasoning often determines what must be retrieved. However, their interaction remains largely underexplored. In preliminary experiments on several open-source LLMs, we observe that in-context retrieval performance substantially degrades...

---

### 9. Agentic Jackal: Live Execution and Semantic Value Grounding for Text-to-JQL

**Authors:** Vishnu Murali, Anmol Gulati, Elias Lumer, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09470v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09470v1)

**Summary:** Translating natural language into Jira Query Language (JQL) requires resolving ambiguous field references, instance-specific categorical values, and complex Boolean predicates. Single-pass LLMs cannot discover which categorical values (e.g., component names or fix versions) actually exist in a given Jira instance, nor can they verify generated queries against a live data source, limiting accuracy on paraphrased or ambiguous requests. No open, execution-based benchmark exists for mapping natural ...

---

### 10. Across the Levels of Analysis: Explaining Predictive Processing in Humans Requires More Than Machine-Estimated Probabilities

**Authors:** Sathvik Nair, Colin Phillips

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09466v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09466v1)

**Summary:** Under the lens of Marr's levels of analysis, we critique and extend two claims about language models (LMs) and language processing: first, that predicting upcoming linguistic information based on context is central to language processing, and second, that many advances in psycholinguistics would be impossible without large language models (LLMs). We further outline future directions that combine the strengths of LLMs with psycholinguistic models.

---

### 11. From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models

**Authors:** Chenchen Zhang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09459v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09459v1)

**Summary:** Reinforcement learning (RL) for large language models (LLMs) increasingly relies on sparse, outcome-level rewards -- yet determining which actions within a long trajectory caused the outcome remains difficult. This credit assignment (CA) problem manifests in two regimes: reasoning RL, where credit must be distributed across tokens and steps within a single chain-of-thought generation (500--30K+ tokens); and agentic RL, where multi-turn environment interaction introduces stochastic transitions, p...

---

### 12. Many-Tier Instruction Hierarchy in LLM Agents

**Authors:** Jingyu Zhang, Tianjian Li, William Jurayj, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09443v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09443v1)

**Summary:** Large language model agents receive instructions from many sources-system messages, user prompts, tool outputs, and more-each carrying different levels of trust and authority. When these instructions conflict, models must reliably follow the highest-privilege instruction to remain safe and effective. The dominant paradigm, instruction hierarchy (IH), assumes a fixed, small set of privilege levels (typically fewer than five) defined by rigid role labels (e.g., system > user). This is inadequate f...

---

### 13. UIPress: Bringing Optical Token Compression to UI-to-Code Generation

**Authors:** Dasen Dai, Shuoqi Li, Ronghao Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09442v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09442v1)

**Summary:** UI-to-Code generation requires vision-language models (VLMs) to produce thousands of tokens of structured HTML/CSS from a single screenshot, making visual token efficiency critical. Existing compression methods either select tokens at inference time using task-agnostic heuristics, or zero out low-attention features without actually shortening the sequence -- neither truly reduces prefill latency or adapts to the non-uniform information density of UI screenshots. Meanwhile, optical (encoder-side ...

---

### 14. Automated Instruction Revision (AIR): A Structured Comparison of Task Adaptation Strategies for LLM

**Authors:** Solomiia Bilyk, Volodymyr Getmanskyi, Taras Firman

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09418v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09418v1)

**Summary:** This paper studies Automated Instruction Revision (AIR), a rule-induction-based method for adapting large language models (LLMs) to downstream tasks using limited task-specific examples. We position AIR within the broader landscape of adaptation strategies, including prompt optimization, retrieval-based methods, and fine-tuning. We then compare these approaches across a diverse benchmark suite designed to stress different task requirements, such as knowledge injection, structured extraction, lab...

---

### 15. Is More Data Worth the Cost? Dataset Scaling Laws in a Tiny Attention-Only Decoder

**Authors:** Götz-Henrik Wiegand, Lorena Raichle, Rico Städeli, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09389v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09389v1)

**Summary:** Training Transformer language models is expensive, as performance typically improves with increasing dataset size and computational budget. Although scaling laws describe this trend at large scale, their implications in controlled, smaller-scale settings remain less explored. In this work, we isolate dataset-size effects using a strongly reduced attention-only decoder architecture. By training on progressively larger power-of-two subsets, we observe smooth performance improvements accompanied by...

---

### 16. Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios

**Authors:** Hui Liu, Bin Zou, Kecheng Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09377v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09377v1)

**Summary:** Large language models (LLMs) exhibit substantial variability in performance and computational cost across tasks and queries, motivating routing systems that select models to meet user-specific cost-performance trade-offs. However, existing routers generalize poorly in cold-start scenarios where in-domain training data is unavailable. We address this limitation with a multi-level task-profile-guided data synthesis framework that constructs a hierarchical task taxonomy and produces diverse questio...

---

### 17. Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts

**Authors:** Farhad Nooralahzadeh, Omid Rohanian, Yi Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09364v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09364v1)

**Summary:** When a Vision-Language Model (VLM) sees a blue banana and answers "yellow", is the problem of perception or arbitration? We explore the question in ten VLMs with various sizes and reveal an Encoding--Grounding Dissociation: models that fail to report what they see (and thus provide a wrong answer) still encode the visual evidence as strongly as models that provide the correct answer. Using Multimodal Arbitration Crossover (MAC) analysis with layer-by-layer Logit Lens probing, we track the compet...

---

### 18. Visually-Guided Policy Optimization for Multimodal Reasoning

**Authors:** Zengbin Wang, Feng Xiong, Liang Lin, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09349v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning ability of vision-language models (VLMs). However, the inherent text-dominated nature of VLMs often leads to insufficient visual faithfulness, characterized by sparse attention activation to visual tokens. More importantly, our empirical analysis reveals that temporal visual forgetting along reasoning steps exacerbates this deficiency. To bridge this gap, we propose Visually-Guided Policy Optimization ...

---

### 19. Mind the Gap Between Spatial Reasoning and Acting! Step-by-Step Evaluation of Agents With Spatial-Gym

**Authors:** Lars Benedikt Kaesberg, Tianyu Yang, Niklas Bauer, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09338v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09338v1)

**Summary:** Spatial reasoning is central to navigation and robotics, yet measuring model capabilities on these tasks remains difficult. Existing benchmarks evaluate models in a one-shot setting, requiring full solution generation in a single response, unlike humans, who work in interactive environments step-by-step. We introduce Spatial-Gym, a Gymnasium environment that isolates spatial constraint reasoning by testing pathfinding in 2D-grid puzzles as a sequential decision task with optional backtracking. W...

---

### 20. EthicMind: A Risk-Aware Framework for Ethical-Emotional Alignment in Multi-Turn Dialogue

**Authors:** Jiawen Deng, Wei Li, Wentao Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09265v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09265v1)

**Summary:** Intelligent dialogue systems are increasingly deployed in emotionally and ethically sensitive settings, where failures in either emotional attunement or ethical judgment can cause significant harm. Existing dialogue models typically address empathy and ethical safety in isolation, and often fail to adapt their behavior as ethical risk and user emotion evolve across multi-turn interactions. We formulate ethical-emotional alignment in dialogue as an explicit turn-level decision problem, and propos...

---

### 21. ScheMatiQ: From Research Question to Structured Data through Interactive Schema Discovery

**Authors:** Shahar Levy, Eliya Habba, Reshef Mintz, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09237v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09237v1)

**Summary:** Many disciplines pose natural-language research questions over large document collections whose answers typically require structured evidence, traditionally obtained by manually designing an annotation schema and exhaustively labeling the corpus, a slow and error-prone process. We introduce ScheMatiQ, which leverages calls to a backbone LLM to take a question and a corpus to produce a schema and a grounded database, with a web interface that lets steer and revise the extraction. In collaboration...

---

### 22. SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation

**Authors:** Han Luo, Guy Laban

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09212v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09212v1)

**Summary:** Large language models are increasingly deployed in multi-turn settings such as tutoring, support, and counseling, where reliability depends on preserving consistent roles, personas, and goals across long horizons. This requirement becomes critical when LLMs are used to generate synthetic dialogues for training and evaluation, since LLM--LLM conversations can accumulate identity-related failures such as persona drift, role confusion, and "echoing", where one agent gradually mirrors its partner. W...

---

### 23. Do LLMs Follow Their Own Rules? A Reflexive Audit of Self-Stated Safety Policies

**Authors:** Avni Mittal

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09189v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09189v1)

**Summary:** LLMs internalize safety policies through RLHF, yet these policies are never formally specified and remain difficult to inspect. Existing benchmarks evaluate models against external standards but do not measure whether models understand and enforce their own stated boundaries. We introduce the Symbolic-Neural Consistency Audit (SNCA), a framework that (1) extracts a model's self-stated safety rules via structured prompts, (2) formalizes them as typed predicates (Absolute, Conditional, Adaptive), ...

---

### 24. Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG

**Authors:** Passant Elchafei, Monorama Swain, Shahed Masoudian, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09174v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09174v1)

**Summary:** Retrieval-Augmented Generation (RAG) aims to reduce hallucination by grounding answers in retrieved evidence, yet hallucinated answers remain common even when relevant documents are available. Existing evaluations focus on answer-level or passage-level accuracy, offering limited insight into how evidence is used during generation. In this work, we introduce a facet-level diagnostics framework for QA that decomposes each input question into atomic reasoning facets. For each facet, we assess evide...

---

### 25. Persona-E$^2$: A Human-Grounded Dataset for Personality-Shaped Emotional Responses to Textual Events

**Authors:** Yuqin Yang, Haowu Zhou, Haoran Tu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09162v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09162v1)

**Summary:** Most affective computing research treats emotion as a static property of text, focusing on the writer's sentiment while overlooking the reader's perspective. This approach ignores how individual personalities lead to diverse emotional appraisals of the same event. Although role-playing Large Language Models (LLMs) attempt to simulate such nuanced reactions, they often suffer from "personality illusion'' -- relying on surface-level stereotypes rather than authentic cognitive logic. A critical bot...

---

### 26. Think Less, Know More: State-Aware Reasoning Compression with Knowledge Guidance for Efficient Reasoning

**Authors:** Yi Sui, Chaozhuo Li, Dawei Song

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09150v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09150v1)

**Summary:** Large Reasoning Models (LRMs) achieve strong performance on complex tasks by leveraging long Chain-of-Thought (CoT), but often suffer from overthinking, leading to excessive reasoning steps and high inference latency. Existing CoT compression methods struggle to balance accuracy and efficiency, and lack fine-grained, step-level adaptation to redundancy and reasoning bias. Therefore, we propose State-Aware Reasoning Compression with Knowledge Guidance (STACK), a framework that performs step-wise ...

---

### 27. Prototype-Regularized Federated Learning for Cross-Domain Aspect Sentiment Triplet Extraction

**Authors:** Zongming Cai, Jianhang Tang, Zhenyong Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09123v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09123v1)

**Summary:** Aspect Sentiment Triplet Extraction (ASTE) aims to extract all sentiment triplets of aspect terms, opinion terms, and sentiment polarities from a sentence. Existing methods are typically trained on individual datasets in isolation, failing to jointly capture the common feature representations shared across domains. Moreover, data privacy constraints prevent centralized data aggregation. To address these challenges, we propose Prototype-based Cross-Domain Span Prototype extraction (PCD-SpanProto)...

---

### 28. Interactive ASR: Towards Human-Like Interaction and Semantic Coherence Evaluation for Agentic Speech Recognition

**Authors:** Peng Wang, Yanqiao Zhu, Zixuan Jiang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09121v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09121v1)

**Summary:** Recent years have witnessed remarkable progress in automatic speech recognition (ASR), driven by advances in model architectures and large-scale training data. However, two important aspects remain underexplored. First, Word Error Rate (WER), the dominant evaluation metric for decades, treats all words equally and often fails to reflect the semantic correctness of an utterance at the sentence level. Second, interactive correction-an essential component of human communication-has rarely been syst...

---

### 29. Few-Shot Contrastive Adaptation for Audio Abuse Detection in Low-Resource Indic Languages

**Authors:** Aditya Narayan Sankaran, Reza Farahbakhsh, Noel Crespi

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09094v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09094v1)

**Summary:** Abusive speech detection is becoming increasingly important as social media shifts towards voice-based interaction, particularly in multilingual and low-resource settings. Most current systems rely on automatic speech recognition (ASR) followed by text-based hate speech classification, but this pipeline is vulnerable to transcription errors and discards prosodic information carried in speech. We investigate whether Contrastive Language-Audio Pre-training (CLAP) can support abusive speech detecti...

---

### 30. Hierarchical Alignment: Enforcing Hierarchical Instruction-Following in LLMs through Logical Consistency

**Authors:** Shu Yang, Zihao Zhou, Di Wang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09075v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09075v1)

**Summary:** Large language models increasingly operate under multiple instructions from heterogeneous sources with different authority levels, including system policies, user requests, tool outputs, and retrieved context. While prior work on instruction hierarchy highlights the importance of respecting instruction priorities, it mainly focuses on adversarial attacks and overlooks the benign but common instruction conflicts that arise in real-world applications. In such settings, models must not only avoid s...

---

### 31. NyayaMind- A Framework for Transparent Legal Reasoning and Judgment Prediction in the Indian Legal System

**Authors:** Parjanya Aditya Shukla, Shubham Kumar Nigam, Debtanu Datta, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09069v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09069v1)

**Summary:** Court Judgment Prediction and Explanation (CJPE) aims to predict a judicial decision and provide a legally grounded explanation for a given case based on the facts, legal issues, arguments, cited statutes, and relevant precedents. For such systems to be practically useful in judicial or legal research settings, they must not only achieve high predictive performance but also generate transparent and structured legal reasoning that aligns with established judicial practices. In this work, we prese...

---

### 32. Anchored Sliding Window: Toward Robust and Imperceptible Linguistic Steganography

**Authors:** Ruiyi Yan, Shiao Meng, Yugo Murawaki

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09066v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09066v1)

**Summary:** Linguistic steganography based on language models typically assumes that steganographic texts are transmitted without alteration, making them fragile to even minor modifications. While previous work mitigates this fragility by limiting the context window, it significantly compromises text quality. In this paper, we propose the anchored sliding window (ASW) framework to improve imperceptibility and robustness. In addition to the latest tokens, the prompt and a bridge context are anchored within t...

---

### 33. SiMing-Bench: Evaluating Procedural Correctness from Continuous Interactions in Clinical Skill Videos

**Authors:** Xiyang Huang, Jiawei Lin, Keying Wu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09037v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09037v1)

**Summary:** Current video benchmarks for multimodal large language models (MLLMs) focus on event recognition, temporal ordering, and long-context recall, but overlook a harder capability required for expert procedural judgment: tracking how ongoing interactions update the procedural state and thereby determine the correctness of later actions. We introduce SiMing-Bench, the first benchmark for evaluating this capability from full-length clinical skill videos. It targets rubric-grounded process-level judgmen...

---

### 34. CONDESION-BENCH: Conditional Decision-Making of Large Language Models in Compositional Action Space

**Authors:** Yeonjun Hwang, Sungyong Park, Minju Kim, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09029v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09029v1)

**Summary:** Large language models have been widely explored as decision-support tools in high-stakes domains due to their contextual understanding and reasoning capabilities. However, existing decision-making benchmarks rely on two simplifying assumptions: actions are selected from a finite set of pre-defined candidates, and explicit conditions restricting action feasibility are not incorporated into the decision-making process. These assumptions fail to capture the compositional structure of real-world act...

---

### 35. Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA

**Authors:** Andre Bacellar

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09019v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09019v1)

**Summary:** Two-hop QA retrieval splits queries into two regimes determined by whether the hop-2 entity is explicitly named in the question (Q-dominant) or only in the bridge passage (B-dominant). We formalize this split with three theorems: (T1) per-query AUC is a monotone function of the cosine separation margin, with R^2 >= 0.90 for six of eight type-encoder pairs; (T2) regime is characterized by two surface-text predicates, with P1 decisive for routing and P2 qualifying the B-dominant case, holding acro...

---

### 36. Towards Linguistically-informed Representations for English as a Second or Foreign Language: Review, Construction and Application

**Authors:** Wenxi Li, Xihao Wang, Weiwei Sun

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09008v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09008v1)

**Summary:** The widespread use of English as a Second or Foreign Language (ESFL) has sparked a paradigm shift: ESFL is not seen merely as a deviation from standard English but as a distinct linguistic system in its own right. This shift highlights the need for dedicated, knowledge-intensive representations of ESFL. In response, this paper surveys existing ESFL resources, identifies their limitations, and proposes a novel solution. Grounded in constructivist theories, the paper treats constructions as the fu...

---

### 37. ASTRA: Adaptive Semantic Tree Reasoning Architecture for Complex Table Question Answering

**Authors:** Xiaoke Guo, Songze Li, Zhiqiang Liu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08999v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08999v1)

**Summary:** Table serialization remains a critical bottleneck for Large Language Models (LLMs) in complex table question answering, hindered by challenges such as structural neglect, representation gaps, and reasoning opacity. Existing serialization methods fail to capture explicit hierarchies and lack schema flexibility, while current tree-based approaches suffer from limited semantic adaptability. To address these limitations, we propose ASTRA (Adaptive Semantic Tree Reasoning Architecture) including two ...

---

### 38. PerMix-RLVR: Preserving Persona Expressivity under Verifiable-Reward Alignment

**Authors:** Jihwan Oh, Soowon Oh, Murad Aghazada, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08986v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08986v1)

**Summary:** Persona prompting has been widely adopted to steer large language models (LLMs) behavior and improve their instruction performance by assigning specific characters. However, identifying an optimal persona is time-consuming, and its impact on output quality remains poorly understood. Prior work has mainly addressed this issue at the prompt level via inference-time strategies, incurring additional computation. In this work, we avoid inference-time prompt search by tackling persona sensitivity duri...

---

### 39. Testing the Assumptions of Active Learning for Translation Tasks with Few Samples

**Authors:** Lorenzo Jaime Yu Flores, Cesare Spinoso di-Piano, Ori Ernst, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08977v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08977v1)

**Summary:** Active learning (AL) is a training paradigm for selecting unlabeled samples for annotation to improve model performance on a test set, which is useful when only a limited number of samples can be annotated. These algorithms often work by optimizing for the informativeness and diversity of the training data to be annotated. Recent work found that AL strategies fail to outperform random sampling on various language generation tasks when using 100-500 samples. To understand AL's poor performance wh...

---

### 40. Quantisation Reshapes the Metacognitive Geometry of Language Models

**Authors:** Jon-Paul Cacioli

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08976v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08976v1)

**Summary:** We report that model quantisation restructures domain-level metacognitive efficiency in LLMs rather than degrading it uniformly. Evaluating Llama-3-8B-Instruct on the same 3,000 questions at Q5_K_M and f16 precision, we find that M-ratio profiles across four knowledge domains are uncorrelated between formats (Spearman rho = 0.00). Arts & Literature moves from worst-monitored (M-ratio = 0.606 at Q5_K_M) to best-monitored (1.542 at f16). Geography moves from well-monitored (1.210) to under-monitor...

---

### 41. Confident in a Confidence Score: Investigating the Sensitivity of Confidence Scores to Supervised Fine-Tuning

**Authors:** Lorenzo Jaime Yu Flores, Cesare Spinoso di-Piano, Jackie Chi Kit Cheung

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08974v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08974v1)

**Summary:** Uncertainty quantification is a set of techniques that measure confidence in language models. They can be used, for example, to detect hallucinations or alert users to review uncertain predictions. To be useful, these confidence scores must be correlated with the quality of the output. However, recent work found that fine-tuning can affect the correlation between confidence scores and quality. Hence, we investigate the underlying behavior of confidence scores to understand its sensitivity to sup...

---

### 42. Litmus (Re)Agent: A Benchmark and Agentic System for Predictive Evaluation of Multilingual Models

**Authors:** Avni Mittal, Shanu Kumar, Sandipan Dandapat, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08970v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08970v1)

**Summary:** We study predictive multilingual evaluation: estimating how well a model will perform on a task in a target language when direct benchmark results are missing. This problem is common in multilingual deployment, where evaluation coverage is sparse and published evidence is uneven across languages, tasks, and model families. We introduce a controlled benchmark of 1,500 questions spanning six tasks and five evidence scenarios. The benchmark separates accessible evidence from ground truth, enabling ...

---

### 43. Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models

**Authors:** Shun Zou, Yong Wang, Zehui Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08964v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08964v1)

**Summary:** Diffusion Large Language Models (dLLMs) have recently become a promising alternative to autoregressive large language models (ARMs). Semi-autoregressive (Semi-AR) decoding is widely employed in base dLLMs and advanced decoding strategies due to its superior performance. However, our observations reveal that Semi-AR decoding suffers from inherent block constraints, which cause the decoding of many cross-block stable tokens to be unnecessarily delayed. To address this challenge, we systematically ...

---

### 44. MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits

**Authors:** Yixin Xiang, Yunshan Ma, Xiaoyu Du, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08952v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08952v1)

**Summary:** Document Question Answering (DQA) involves generating answers from a document based on a user's query, representing a key task in document understanding. This task requires interpreting visual layouts, which has prompted recent studies to adopt multimodal Retrieval-Augmented Generation (RAG) that processes page images for answer generation. However, in multimodal RAG, visual DQA struggles to utilize a large number of images effectively, as the retrieval stage often retains only a few candidate p...

---

### 45. TaxPraBen: A Scalable Benchmark for Structured Evaluation of LLMs in Chinese Real-World Tax Practice

**Authors:** Gang Hu, Yating Chen, Haiyan Ding, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08948v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08948v1)

**Summary:** While Large Language Models (LLMs) excel in various general domains, they exhibit notable gaps in the highly specialized, knowledge-intensive, and legally regulated Chinese tax domain. Consequently, while tax-related benchmarks are gaining attention, many focus on isolated NLP tasks, neglecting real-world practical capabilities. To address this issue, we introduce TaxPraBen, the first dedicated benchmark for Chinese taxation practice. It combines 10 traditional application tasks, along with 3 pi...

---

### 46. MuTSE: A Human-in-the-Loop Multi-use Text Simplification Evaluator

**Authors:** Rares-Alexandru Roscan, Gabriel Petre1, Adrian-Marius Dumitran, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08947v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08947v1)

**Summary:** As Large Language Models (LLMs) become increasingly prevalent in text simplification, systematically evaluating their outputs across diverse prompting strategies and architectures remains a critical methodological challenge in both NLP research and Intelligent Tutoring Systems (ITS). Developing robust prompts is often hindered by the absence of structured, visual frameworks for comparative text analysis. While researchers typically rely on static computational scripts, educators are constrained ...

---

### 47. NCL-BU at SemEval-2026 Task 3: Fine-tuning XLM-RoBERTa for Multilingual Dimensional Sentiment Regression

**Authors:** Tong Wu, Nicolay Rusnachenko, Huizhi Liang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08923v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08923v1)

**Summary:** Dimensional Aspect-Based Sentiment Analysis (DimABSA) extends traditional ABSA from categorical polarity labels to continuous valence-arousal (VA) regression. This paper describes a system developed for Track A - Subtask 1 (Dimensional Aspect Sentiment Regression), aiming to predict real-valued VA scores in the [1, 9] range for each given aspect in a text. A fine-tuning approach based on XLM-RoBERTa-base is adopted, constructing the input as [CLS] T [SEP] a_i [SEP] and training dual regression h...

---

### 48. Beyond Relevance: Utility-Centric Retrieval in the LLM Era

**Authors:** Hengran Zhang, Minghao Tang, Keping Bi, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08920v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08920v1)

**Summary:** Information retrieval systems have traditionally optimized for topical relevance-the degree to which retrieved documents match a query. However, relevance only approximates a deeper goal: utility, namely, whether retrieved information helps accomplish a user's underlying task. The emergence of retrieval-augmented generation (RAG) fundamentally changes this paradigm. Retrieved documents are no longer consumed directly by users but instead serve as evidence for large language models (LLMs) that pr...

---

### 49. Revisiting the Capacity Gap in Chain-of-Thought Distillation from a Practical Perspective

**Authors:** Tokio Kajitsuka, Ukyo Honda, Sho Takase

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08880v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08880v1)

**Summary:** Chain-of-thought (CoT) distillation transfers reasoning behaviors from a strong teacher to a smaller student, but prior work reports a capacity gap: distillation may fail when the teacher-student capability mismatch is large. We revisit the capacity gap from a practical perspective by re-examining commonly used experimental settings. Notably, we find that CoT distillation often degrades performance compared to the student's pre-distillation baseline, an issue obscured when only post-distillation...

---

### 50. GRASP: Grounded CoT Reasoning with Dual-Stage Optimization for Multimodal Sarcasm Target Identification

**Authors:** Faxian Wan, Xiaocui Yang, Yifan Cao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08879v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08879v1)

**Summary:** Moving beyond the traditional binary classification paradigm of Multimodal Sarcasm Detection, Multimodal Sarcasm Target Identification (MSTI) presents a more formidable challenge, requiring precise localization of fine-grained targets such as textual phrases and visual regions. Existing approaches predominantly rely on implicit cross-modal alignment, offering limited interpretability and suboptimal fine-grained localization. To address these limitations, we propose GRASP, Grounded Chain-of-Thoug...

---

## cs.CV

**50 papers**

### 1. Tango: Taming Visual Signals for Efficient Video Large Language Models

**Authors:** Shukang Yin, Sirui Zhao, Hanchao Wang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09547v1)

**Summary:** Token pruning has emerged as a mainstream approach for developing efficient Video Large Language Models (Video LLMs). This work revisits and advances the two predominant token-pruning paradigms: attention-based selection and similarity-based clustering. Our study reveals two critical limitations in existing methods: (1) conventional top-k selection strategies fail to fully account for the attention distribution, which is often spatially multi-modal and long-tailed in magnitude; and (2) direct si...

---

### 2. EgoTL: Egocentric Think-Aloud Chains for Long-Horizon Tasks

**Authors:** Lulin Liu, Dayou Li, Yiqing Liang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09535v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09535v1)

**Summary:** Large foundation models have made significant advances in embodied intelligence, enabling synthesis and reasoning over egocentric input for household tasks. However, VLM-based auto-labeling is often noisy because the primary data sources lack accurate human action labels, chain-of-thought (CoT), and spatial annotations; these errors are amplified during long-horizon spatial instruction following. These issues stem from insufficient coverage of minute-long, daily household planning tasks and from...

---

### 3. Seeing is Believing: Robust Vision-Guided Cross-Modal Prompt Learning under Label Noise

**Authors:** Zibin Geng, Xuefeng Jiang, Jia Li, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09532v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09532v1)

**Summary:** Prompt learning is a parameter-efficient approach for vision-language models, yet its robustness under label noise is less investigated. Visual content contains richer and more reliable semantic information, which remains more robust under label noise. However, the prompt itself is highly susceptible to label noise. Motivated by this intuition, we propose VisPrompt, a lightweight and robust vision-guided prompt learning framework for noisy-label settings. Specifically, we exploit a cross-modal a...

---

### 4. VisionFoundry: Teaching VLMs Visual Perception with Synthetic Images

**Authors:** Guanyu Zhou, Yida Yin, Wenhao Chai, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09531v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09531v1)

**Summary:** Vision-language models (VLMs) still struggle with visual perception tasks such as spatial understanding and viewpoint recognition. One plausible contributing factor is that natural image datasets provide limited supervision for low-level visual skills. This motivates a practical question: can targeted synthetic supervision, generated from only a task keyword such as Depth Order, address these weaknesses? To investigate this question, we introduce VisionFoundry, a task-aware synthetic data genera...

---

### 5. VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning

**Authors:** Wenyi Xiao, Xinchi Xu, Leilei Gan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09529v1)

**Summary:** Large Vision Language Models (LVLMs) achieve strong multimodal reasoning but frequently exhibit hallucinations and incorrect responses with high certainty, which hinders their usage in high-stakes domains. Existing verbalized confidence calibration methods, largely developed for text-only LLMs, typically optimize a single holistic confidence score using binary answer-level correctness. This design is mismatched to LVLMs: an incorrect prediction may arise from perceptual failures or from reasonin...

---

### 6. Envisioning the Future, One Step at a Time

**Authors:** Stefan Andreas Baumann, Jannik Wiese, Tommaso Martorella, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09527v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09527v1)

**Summary:** Accurately anticipating how complex, diverse scenes will evolve requires models that represent uncertainty, simulate along extended interaction chains, and efficiently explore many plausible futures. Yet most existing approaches rely on dense video or latent-space prediction, expending substantial capacity on dense appearance rather than on the underlying sparse trajectories of points in the scene. This makes large-scale exploration of future hypotheses costly and limits performance when long-ho...

---

### 7. RIRF: Reasoning Image Restoration Framework

**Authors:** Wending Yan, Rongkai Zhang, Kaihua Tang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09511v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09511v1)

**Summary:** Universal image restoration (UIR) aims to recover clean images from diverse and unknown degradations using a unified model. Existing UIR methods primarily focus on pixel reconstruction and often lack explicit diagnostic reasoning over degradation composition, severity, and scene semantics prior to restoration. We propose Reason and Restore (R\&R), a novel framework that integrates structured Chain-of-Thought (CoT) reasoning into the image restoration pipeline. R\&R introduces an explicit reasone...

---

### 8. VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning

**Authors:** Yucheng Shen, Jiulong Wu, Jizhou Huang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09508v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09508v1)

**Summary:** Visual Retrieval-Augmented Generation (VRAG) empowers Vision-Language Models to retrieve and reason over visually rich documents. To tackle complex queries requiring multi-step reasoning, agentic VRAG systems interleave reasoning with iterative retrieval.. However, existing agentic VRAG faces two critical bottlenecks. (1) Visual Evidence Sparsity: key evidence is scattered across pages yet processed in isolation, hindering cross-page reasoning; moreover, fine-grained intra-image evidence often r...

---

### 9. Online3R: Online Learning for Consistent Sequential Reconstruction Based on Geometry Foundation Model

**Authors:** Shunkai Zhou, Zike Yan, Fei Xue, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09480v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09480v1)

**Summary:** We present Online3R, a new sequential reconstruction framework that is capable of adapting to new scenes through online learning, effectively resolving inconsistency issues. Specifically, we introduce a set of learnable lightweight visual prompts into a pretrained, frozen geometry foundation model to capture the knowledge of new environments while preserving the fundamental capability of the foundation model for geometry prediction. To solve the problems of missing groundtruth and the requiremen...

---

### 10. Incremental Semantics-Aided Meshing from LiDAR-Inertial Odometry and RGB Direct Label Transfer

**Authors:** Muhammad Affan, Ville Lehtola, George Vosselman

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09478v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09478v1)

**Summary:** Geometric high-fidelity mesh reconstruction from LiDAR-inertial scans remains challenging in large, complex indoor environments -- such as cultural buildings -- where point cloud sparsity, geometric drift, and fixed fusion parameters produce holes, over-smoothing, and spurious surfaces at structural boundaries. We propose a modular, incremental RGB+LiDAR pipeline that generates incremental semantics-aided high-quality meshes from indoor scans through scan frame-based direct label transfer. A vis...

---

### 11. Realizing Immersive Volumetric Video: A Multimodal Framework for 6-DoF VR Engagement

**Authors:** Zhengxian Yang, Shengqi Wang, Shi Pan, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09473v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09473v1)

**Summary:** Fully immersive experiences that tightly integrate 6-DoF visual and auditory interaction are essential for virtual and augmented reality. While such experiences can be achieved through computer-generated content, constructing them directly from real-world captured videos remains largely unexplored. We introduce Immersive Volumetric Videos, a new volumetric media format designed to provide large 6-DoF interaction spaces, audiovisual feedback, and high-resolution, high-frame-rate dynamic content. ...

---

### 12. DSVTLA: Deep Swin Vision Transformer-Based Transfer Learning Architecture for Multi-Type Cancer Histopathological Cancer Image Classification

**Authors:** Muazzem Hussain Khan, Tasdid Hasnain, Md. Jamil khan, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09468v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09468v1)

**Summary:** In this study, we proposed a deep Swin-Vision Transformer-based transfer learning architecture for robust multi-cancer histopathological image classification. The proposed framework integrates a hierarchical Swin Transformer with ResNet50-based convolution features extraction, enabling the model to capture both long-range contextual dependencies and fine-grained local morphological patterns within histopathological images. To validate the efficiency of the proposed architecture, an extensive exp...

---

### 13. AsymLoc: Towards Asymmetric Feature Matching for Efficient Visual Localization

**Authors:** Mohammad Omama, Gabriele Berton, Eric Foxlin, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09445v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09445v1)

**Summary:** Precise and real-time visual localization is critical for applications like AR/VR and robotics, especially on resource-constrained edge devices such as smart glasses, where battery life and heat dissipation can be a primary concerns. While many efficient models exist, further reducing compute without sacrificing accuracy is essential for practical deployment. To address this, we propose asymmetric visual localization: a large Teacher model processes pre-mapped database images offline, while a li...

---

### 14. SCoRe: Clean Image Generation from Diffusion Models Trained on Noisy Images

**Authors:** Yuta Matsuzaki, Seiichi Uchida, Shumpei Takezaki

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09436v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09436v1)

**Summary:** Diffusion models trained on noisy datasets often reproduce high-frequency training artifacts, significantly degrading generation quality. To address this, we propose SCoRe (Spectral Cutoff Regeneration), a training-free, generation-time spectral regeneration method for clean image generation from diffusion models trained on noisy images. Leveraging the spectral bias of diffusion models, which infer high-frequency details from low-frequency cues, SCoRe suppresses corrupted high-frequency componen...

---

### 15. Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories

**Authors:** Wonbong Jang, Shikun Liu, Soubhik Sanyal, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09429v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09429v1)

**Summary:** Recovering camera parameters from images and rendering scenes from novel viewpoints have long been treated as separate tasks in computer vision and graphics. This separation breaks down when image coverage is sparse or poses are ambiguous, since each task needs what the other produces. We propose Rays as Pixels, a Video Diffusion Model (VDM) that learns a joint distribution over videos and camera trajectories. We represent each camera as dense ray pixels (raxels) and denoise them jointly with vi...

---

### 16. Do Vision Language Models Need to Process Image Tokens?

**Authors:** Sambit Ghosh, R. Venkatesh Babu, Chirag Agarwal

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09425v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09425v1)

**Summary:** Vision Language Models (VLMs) have achieved remarkable success by integrating visual encoders with large language models (LLMs). While VLMs process dense image tokens across deep transformer stacks (incurring substantial computational overhead), it remains fundamentally unclear whether sustained image-token processing is necessary for their performance or visual representations meaningfully evolve from early to later layers. In this work, we systematically investigate the functional role of imag...

---

### 17. Multi-task Just Recognizable Difference for Video Coding for Machines: Database, Model, and Coding Application

**Authors:** Junqi Liu, Yun Zhang, Xiaoxia Huang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09421v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09421v1)

**Summary:** Just Recognizable Difference (JRD) boosts coding efficiency for machine vision through visibility threshold modeling, but is currently limited to a single-task scenario. To address this issue, we propose a Multi-Task JRD (MT-JRD) dataset and an Attribute-assisted MT-JRD (AMT-JRD) model for Video Coding for Machines (VCM), enhancing both prediction accuracy and coding efficiency. First, we construct a dataset comprising 27,264 JRD annotations from machines, supporting three representative tasks i...

---

### 18. PhysInOne: Visual Physics Learning and Reasoning in One Suite

**Authors:** Siyuan Zhou, Hejun Wang, Hu Cheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09415v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09415v1)

**Summary:** We present PhysInOne, a large-scale synthetic dataset addressing the critical scarcity of physically-grounded training data for AI systems. Unlike existing datasets limited to merely hundreds or thousands of examples, PhysInOne provides 2 million videos across 153,810 dynamic 3D scenes, covering 71 basic physical phenomena in mechanics, optics, fluid dynamics, and magnetism. Distinct from previous works, our scenes feature multiobject interactions against complex backgrounds, with comprehensive ...

---

### 19. SynFlow: Scaling Up LiDAR Scene Flow Estimation with Synthetic Data

**Authors:** Qingwen Zhang, Xiaomeng Zhu, Chenhan Jiang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09411v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09411v1)

**Summary:** Reliable 3D dynamic perception requires models that can anticipate motion beyond predefined categories, yet progress is hindered by the scarcity of dense, high-quality motion annotations. While self-supervision on unlabeled real data offers a path forward, empirical evidence suggests that scaling unlabeled data fails to close the performance gap due to noisy proxy signals. In this paper, we propose a shift in paradigm: learning robust real-world motion priors entirely from scalable simulation. W...

---

### 20. EGLOCE: Training-Free Energy-Guided Latent Optimization for Concept Erasure

**Authors:** Junyeong Ahn, Seojin Yoon, Sungyong Baik

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09405v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09405v1)

**Summary:** As text-to-image diffusion models grow increasingly prevalent, the ability to remove specific concepts-mostly explicit content and many copyrighted characters or styles-has become essential for safety and compliance. Existing unlearning approaches often require costly re-training, modify parameters at the cost of degradation of unrelated concept fidelity, or depend on indirect inference-time adjustment that compromise the effectiveness of concept erasure. Inspired by the success of energy-guided...

---

### 21. Efficient Unlearning through Maximizing Relearning Convergence Delay

**Authors:** Khoa Tran, Simon S. Woo

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09391v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09391v1)

**Summary:** Machine unlearning poses challenges in removing mislabeled, contaminated, or problematic data from a pretrained model. Current unlearning approaches and evaluation metrics are solely focused on model predictions, which limits insight into the model's true underlying data characteristics. To address this issue, we introduce a new metric called relearning convergence delay, which captures both changes in weight space and prediction space, providing a more comprehensive assessment of the model's un...

---

### 22. Region-Constrained Group Relative Policy Optimization for Flow-Based Image Editing

**Authors:** Zhuohan Ouyang, Zhe Qian, Wenhuo Cui, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09386v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09386v1)

**Summary:** Instruction-guided image editing requires balancing target modification with non-target preservation. Recently, flow-based models have emerged as a strong and increasingly adopted backbone for instruction-guided image editing, thanks to their high fidelity and efficient deterministic ODE sampling. Building on this foundation, GRPO-based reward-driven post-training has been explored to directly optimize editing-specific rewards, improving instruction following and editing consistency. However, ex...

---

### 23. Cluster-First Labelling: An Automated Pipeline for Segmentation and Morphological Clustering in Histology Whole Slide Images

**Authors:** Muhammad Haseeb Ahmad, Sharmila Rajendran, Damion Young, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09370v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09370v1)

**Summary:** Labelling tissue components in histology whole slide images (WSIs) is prohibitively labour-intensive: a single slide may contain tens of thousands of structures--cells, nuclei, and other morphologically distinct objects--each requiring manual boundary delineation and classification. We present a cloudnative, end-to-end pipeline that automates this process through a cluster-first paradigm. Our system tiles WSIs, filters out tiles deemed unlikely to contain valuable information, segments tissue co...

---

### 24. Through Their Eyes: Fixation-aligned Tuning for Personalized User Emulation

**Authors:** Lingfeng Huang, Huizhong Guo, Tianjun Wei, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09368v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09368v1)

**Summary:** Large language model (LLM) agents are increasingly deployed as scalable user simulators for recommender system evaluation. Yet existing simulators perceive recommendations through text or structured metadata rather than the visual interfaces real users browse-a critical gap, since attention over recommendation layouts is both visually driven and highly personalized. We investigate whether aligning a vision-language model's (VLM's) visual attention with user-specific gaze patterns can improve sim...

---

### 25. EpiAgent: An Agent-Centric System for Ancient Inscription Restoration

**Authors:** Shipeng Zhu, Ang Chen, Na Nie, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09367v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09367v1)

**Summary:** Ancient inscriptions, as repositories of cultural memory, have suffered from centuries of environmental and human-induced degradation. Restoring their intertwined visual and textual integrity poses one of the most demanding challenges in digital heritage preservation. However, existing AI-based approaches often rely on rigid pipelines, struggling to generalize across such complex and heterogeneous real-world degradations. Inspired by the skill-coordinated workflow of human epigraphers, we propos...

---

### 26. Robust 4D Visual Geometry Transformer with Uncertainty-Aware Priors

**Authors:** Ying Zang, Yidong Han, Chaotao Ding, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09366v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09366v1)

**Summary:** Reconstructing dynamic 4D scenes is an important yet challenging task. While 3D foundation models like VGGT excel in static settings, they often struggle with dynamic sequences where motion causes significant geometric ambiguity. To address this, we present a framework designed to disentangle dynamic and static components by modeling uncertainty across different stages of the reconstruction process. Our approach introduces three synergistic mechanisms: (1) Entropy-Guided Subspace Projection, whi...

---

### 27. Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts

**Authors:** Farhad Nooralahzadeh, Omid Rohanian, Yi Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09364v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09364v1)

**Summary:** When a Vision-Language Model (VLM) sees a blue banana and answers "yellow", is the problem of perception or arbitration? We explore the question in ten VLMs with various sizes and reveal an Encoding--Grounding Dissociation: models that fail to report what they see (and thus provide a wrong answer) still encode the visual evidence as strongly as models that provide the correct answer. Using Multimodal Arbitration Crossover (MAC) analysis with layer-by-layer Logit Lens probing, we track the compet...

---

### 28. LuMon: A Comprehensive Benchmark and Development Suite with Novel Datasets for Lunar Monocular Depth Estimation

**Authors:** Aytaç Sekmen, Fatih Emre Gunes, Furkan Horoz, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09352v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09352v1)

**Summary:** Monocular Depth Estimation (MDE) is crucial for autonomous lunar rover navigation using electro-optical cameras. However, deploying terrestrial MDE networks to the Moon brings a severe domain gap due to harsh shadows, textureless regolith, and zero atmospheric scattering. Existing evaluations rely on analogs that fail to replicate these conditions and lack actual metric ground truth. To address this, we present LuMon, a comprehensive benchmarking framework to evaluate MDE methods for lunar explo...

---

### 29. Visually-Guided Policy Optimization for Multimodal Reasoning

**Authors:** Zengbin Wang, Feng Xiong, Liang Lin, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09349v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning ability of vision-language models (VLMs). However, the inherent text-dominated nature of VLMs often leads to insufficient visual faithfulness, characterized by sparse attention activation to visual tokens. More importantly, our empirical analysis reveals that temporal visual forgetting along reasoning steps exacerbates this deficiency. To bridge this gap, we propose Visually-Guided Policy Optimization ...

---

### 30. VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis

**Authors:** Xiaolei Lang, Yang Wang, Yukun Zhou, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09330v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09330v1)

**Summary:** Recent advances in robot foundation models trained on large-scale human teleoperation data have enabled robots to perform increasingly complex real-world tasks. However, scaling these systems remains difficult because collecting task-specific demonstrations is expensive and labor-intensive. Synthetic data, especially generated videos, offer a promising direction, but existing World Models (WMs) are not directly suitable for policy learning since they do not provide paired action trajectories. Wo...

---

### 31. From Frames to Events: Rethinking Evaluation in Human-Centric Video Anomaly Detection

**Authors:** Narges Rashvand, Shanle Yao, Armin Danesh Pazho, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09327v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09327v1)

**Summary:** Pose-based Video Anomaly Detection (VAD) has gained significant attention for its privacy-preserving nature and robustness to environmental variations. However, traditional frame-level evaluations treat video as a collection of isolated frames, fundamentally misaligned with how anomalies manifest and are acted upon in the real world. In operational surveillance systems, what matters is not the flagging of individual frames, but the reliable detection, localization, and reporting of a coherent an...

---

### 32. Multimodal Anomaly Detection for Human-Robot Interaction

**Authors:** Guilherme Ribeiro, Iordanis Antypas, Leonardo Bizzaro, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09326v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09326v1)

**Summary:** Ensuring safety and reliability in human-robot interaction (HRI) requires the timely detection of unexpected events that could lead to system failures or unsafe behaviours. Anomaly detection thus plays a critical role in enabling robots to recognize and respond to deviations from normal operation during collaborative tasks. While reconstruction models have been actively explored in HRI, approaches that operate directly on feature vectors remain largely unexplored. In this work, we propose MADRI,...

---

### 33. Structure-Aware Fine-Grained Gaussian Splatting for Expressive Avatar Reconstruction

**Authors:** Yuze Su, Hongsong Wang, Jie Gui, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09324v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09324v1)

**Summary:** Reconstructing photorealistic and topology-aware human avatars from monocular videos remains a significant challenge in the fields of computer vision and graphics. While existing 3D human avatar modeling approaches can effectively capture body motion, they often fail to accurately model fine details such as hand movements and facial expressions. To address this, we propose Structure-aware Fine-grained Gaussian Splatting (SFGS), a novel method for reconstructing expressive and coherent full-body ...

---

### 34. UHD Low-Light Image Enhancement via Real-Time Enhancement Methods with Clifford Information Fusion

**Authors:** Xiaohan Wang, Chen Wu, Dawei Zhao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09321v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09321v1)

**Summary:** Considering efficiency, ultra-high-definition (UHD) low-light image restoration is extremely challenging. Existing methods based on Transformer architectures or high-dimensional complex convolutional neural networks often suffer from the "memory wall" bottleneck, failing to achieve millisecond-level inference on edge devices. To address this issue, we propose a novel real-time UHD low-light enhancement network based on geometric feature fusion using Clifford algebra in 2D Euclidean space. First,...

---

### 35. Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark

**Authors:** Jinquan Yan, Zhicheng Zhao, Zhengzheng Tu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09313v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09313v1)

**Summary:** UAV images are critical for applications such as large-area mapping, infrastructure inspection, and emergency response. However, in real-world flight environments, a single image is often affected by multiple degradation factors, including rain, haze, and noise, undermining downstream task performance. Current unified restoration approaches typically rely on implicit degradation representations that entangle multiple factors into a single condition, causing mutual interference among heterogeneou...

---

### 36. VAGNet: Vision-based accident anticipation with global features

**Authors:** Vipooshan Vipulananthan, Charith D. Chitraranjan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09305v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09305v1)

**Summary:** Traffic accidents are a leading cause of fatalities and injuries across the globe. Therefore, the ability to anticipate hazardous situations in advance is essential. Automated accident anticipation enables timely intervention through driver alerts and collision avoidance maneuvers, forming a key component of advanced driver assistance systems. In autonomous driving, such predictive capabilities support proactive safety behaviors, such as initiating defensive driving and human takeover when requi...

---

### 37. GeRM: A Generative Rendering Model From Physically Realistic to Photorealistic

**Authors:** Jiayuan Lu, Rengan Xie, Xuancheng Jin, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09304v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09304v1)

**Summary:** For decades, Physically-Based Rendering (PBR) is the fundation of synthesizing photorealisitic images, and therefore sometimes roughly referred as Photorealistic Rendering (PRR). While PBR is indeed a mathematical simulation of light transport that guarantees physical reality, photorealism has additional reliance on the realistic digital model of geometry and appearance of the real world, leaving a barely explored gap from PBR to PRR (P2P). Consequently, the path toward photorealism faces a crit...

---

### 38. Characterizing Lidar Range-Measurement Ambiguity due to Multiple Returns

**Authors:** Jason H. Rife, Yifan Li

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09282v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09282v1)

**Summary:** Reliable position and attitude sensing is critical for highly automated vehicles that operate on conventional roadways. Lidar sensors are increasingly incorporated into pose-estimation systems. Despite its great utility, lidar is a complex sensor, and its performance in roadway environments is not yet well understood. For instance, it is often assumed in lidar-localization algorithms that a lidar will always identify a unique surface along a given raypath. However, this assumption is not always ...

---

### 39. AMO-ENE: Attention-based Multi-Omics Fusion Model for Outcome Prediction in Extra Nodal Extension and HPV-associated Oropharyngeal Cancer

**Authors:** Gautier Hénique, William Le, Gabriel Dayan, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09280v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09280v1)

**Summary:** Extranodal extension (ENE) is an emerging prognostic factor in human papillomavirus (HPV)-associated oropharyngeal cancer (OPC), although it is currently omitted as a clinical staging criteria. Recent works have advocated for the inclusion of iENE as a prognostic marker in HPV-positive OPC staging. However, several practical limitations continue to hinder its clinical integration, including inconsistencies in segmentation, low contrast in the periphery of metastatic lymph nodes on CT imaging, an...

---

### 40. Beyond Segmentation: Structurally Informed Facade Parsing from Imperfect Images

**Authors:** Maciej Janicki, Aleksander Plocharski, Przemyslaw Musialski

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09260v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09260v1)

**Summary:** Standard object detectors typically treat architectural elements independently, often resulting in facade parsings that lack the structural coherence required for downstream procedural reconstruction. We address this limitation by augmenting the YOLOv8 training objective with a custom lightweight alignment loss. This regularization encourages grid-consistent arrangements of bounding boxes during training, effectively injecting geometric priors without altering the standard inference pipeline. Ex...

---

### 41. Mosaic: Multimodal Jailbreak against Closed-Source VLMs via Multi-View Ensemble Optimization

**Authors:** Yuqin Lan, Gen Li, Yuanze Hu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09253v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09253v1)

**Summary:** Vision-Language Models (VLMs) are powerful but remain vulnerable to multimodal jailbreak attacks. Existing attacks mainly rely on either explicit visual prompt attacks or gradient-based adversarial optimization. While the former is easier to detect, the latter produces subtle perturbations that are less perceptible, but is usually optimized and evaluated under homogeneous open-source surrogate-target settings, leaving its effectiveness on commercial closed-source VLMs under heterogeneous setting...

---

### 42. FashionStylist: An Expert Knowledge-enhanced Multimodal Dataset for Fashion Understanding

**Authors:** Kaidong Feng, Zhuoxuan Huang, Huizhong Guo, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09249v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09249v1)

**Summary:** Fashion understanding requires both visual perception and expert-level reasoning about style, occasion, compatibility, and outfit rationale. However, existing fashion datasets remain fragmented and task-specific, often focusing on item attributes, outfit co-occurrence, or weak textual supervision, and thus provide limited support for holistic outfit understanding. In this paper, we introduce FashionStylist, an expert-annotated benchmark for holistic and expert-level fashion understanding. Constr...

---

### 43. 2D or 3D: Who Governs Salience in VLA Models? -- Tri-Stage Token Pruning Framework with Modality Salience Awareness

**Authors:** Zihao Zheng, Sicheng Tian, Zhihao Mao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09244v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09244v1)

**Summary:** Vision-Language-Action (VLA) models have emerged as the mainstream of embodied intelligence. Recent VLA models have expanded their input modalities from 2D-only to 2D+3D paradigms, forming multi-visual-modal VLA (MVLA) models. Despite achieving improved spatial perception, MVLA faces a greater acceleration demand due to the increased number of input tokens caused by modal expansion. Token pruning is an effective optimization methods tailored to MVLA models. However, existing token pruning scheme...

---

### 44. Neural Distribution Prior for LiDAR Out-of-Distribution Detection

**Authors:** Zizhao Li, Zhengkang Xiang, Jiayang Ao, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09232v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09232v1)

**Summary:** LiDAR-based perception is critical for autonomous driving due to its robustness to poor lighting and visibility conditions. Yet, current models operate under the closed-set assumption and often fail to recognize unexpected out-of-distribution (OOD) objects in the open world. Existing OOD scoring functions exhibit limited performance because they ignore the pronounced class imbalance inherent in LiDAR OOD detection and assume a uniform class distribution. To address this limitation, we propose th...

---

### 45. Hitem3D 2.0: Multi-View Guided Native 3D Texture Generation

**Authors:** Huiang He, Shengchu Zhao, Jianwen Huang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09231v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09231v1)

**Summary:** Although recent advances have improved the quality of 3D texture generation, existing methods still struggle with incomplete texture coverage, cross-view inconsistency, and misalignment between geometry and texture. To address these limitations, we propose Hitem3D 2.0, a multi-view guided native 3D texture generation framework that enhances texture quality through the integration of 2D multi-view generation priors and native 3D texture representations. Hitem3D 2.0 comprises two key components: a...

---

### 46. Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models

**Authors:** Wongi Jeong, Hoigi Seo, Se Young Chun

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09227v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09227v1)

**Summary:** Image generative models have become indispensable tools to yield exquisite high-resolution (HR) images for everyone, ranging from general users to professional designers. However, a desired outcome often requires generating a large number of HR images with different prompts and seeds, resulting in high computational cost for both users and service providers. Generating low-resolution (LR) images first could alleviate computational burden, but it is not straightforward how to generate LR images t...

---

### 47. TinyNeRV: Compact Neural Video Representations via Capacity Scaling, Distillation, and Low-Precision Inference

**Authors:** Muhammad Hannan Akhtar, Ihab Amer, Tamer Shanableh

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09220v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09220v1)

**Summary:** Implicit neural video representations encode entire video sequences within the parameters of a neural network and enable constant time frame reconstruction. Recent work on Neural Representations for Videos (NeRV) has demonstrated competitive reconstruction performance while avoiding the sequential decoding process of conventional video codecs. However, most existing studies focus on moderate or high capacity models, leaving the behavior of extremely compact configurations required for constraine...

---

### 48. SHIFT: Steering Hidden Intermediates in Flow Transformers

**Authors:** Nina Konovalova, Andrey Kuznetsov, Aibek Alanov

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09213v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09213v1)

**Summary:** Diffusion models have become leading approaches for high-fidelity image generation. Recent DiT-based diffusion models, in particular, achieve strong prompt adherence while producing high-quality samples. We propose SHIFT, a simple but effective and lightweight framework for concept removal in DiT diffusion models via targeted manipulation of intermediate activations at inference time, inspired by activation steering in large language models. SHIFT learns steering vectors that are dynamically app...

---

### 49. Adding Another Dimension to Image-based Animal Detection

**Authors:** Vandita Shukla, Fabio Remondino, Benjamin Risse

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09210v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09210v1)

**Summary:** Monocular imaging of animals inherently reduces 3D structures to 2D projections. Detection algorithms lead to 2D bounding boxes that lack information about animal's orientation relative to the camera. To build 3D detection methods for RGB animal images, there is a lack of labeled datasets; such labeling processes require 3D input streams along with RGB data. We present a pipeline that utilises Skinned Multi Animal Linear models to estimate 3D bounding boxes and to project them as robust labels i...

---

### 50. Long-SCOPE: Fully Sparse Long-Range Cooperative 3D Perception

**Authors:** Jiahao Wang, Zikun Xu, Yuner Zhang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09206v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09206v1)

**Summary:** Cooperative 3D perception via Vehicle-to-Everything communication is a promising paradigm for enhancing autonomous driving, offering extended sensing horizons and occlusion resolution. However, the practical deployment of existing methods is hindered at long distances by two critical bottlenecks: the quadratic computational scaling of dense BEV representations and the fragility of feature association mechanisms under significant observation and alignment errors. To overcome these limitations, we...

---

## cs.LG

**50 papers**

### 1. Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism

**Authors:** Hadas Orgad, Boyi Wei, Kaden Zheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09544v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09544v1)

**Summary:** Large language models (LLMs) undergo alignment training to avoid harmful behaviors, yet the resulting safeguards remain brittle: jailbreaks routinely bypass them, and fine-tuning on narrow domains can induce ``emergent misalignment'' that generalizes broadly. Whether this brittleness reflects a fundamental lack of coherent internal organization for harmfulness remains unclear. Here we use targeted weight pruning as a causal intervention to probe the internal organization of harmfulness in LLMs. ...

---

### 2. ANTIC: Adaptive Neural Temporal In-situ Compressor

**Authors:** Sandeep S. Cranganore, Andrei Bodnar, Gianluca Galleti, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09543v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09543v1)

**Summary:** The persistent storage requirements for high-resolution, spatiotemporally evolving fields governed by large-scale and high-dimensional partial differential equations (PDEs) have reached the petabyte-to-exabyte scale. Transient simulations modeling Navier-Stokes equations, magnetohydrodynamics, plasma physics, or binary black hole mergers generate data volumes that are prohibitive for modern high-performance computing (HPC) infrastructures. To address this bottleneck, we introduce ANTIC (Adaptive...

---

### 3. Case-Grounded Evidence Verification: A Framework for Constructing Evidence-Sensitive Supervision

**Authors:** Soroosh Tayebi Arasteh, Mehdi Joodaki, Mahshad Lotfinia, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09537v1)

**Summary:** Evidence-grounded reasoning requires more than attaching retrieved text to a prediction: a model should make decisions that depend on whether the provided evidence supports the target claim. In practice, this often fails because supervision is weak, evidence is only loosely tied to the claim, and evaluation does not test evidence dependence directly. We introduce case-grounded evidence verification, a general framework in which a model receives a local case context, external evidence, and a stru...

---

### 4. Envisioning the Future, One Step at a Time

**Authors:** Stefan Andreas Baumann, Jannik Wiese, Tommaso Martorella, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09527v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09527v1)

**Summary:** Accurately anticipating how complex, diverse scenes will evolve requires models that represent uncertainty, simulate along extended interaction chains, and efficiently explore many plausible futures. Yet most existing approaches rely on dense video or latent-space prediction, expending substantial capacity on dense appearance rather than on the underlying sparse trajectories of points in the scene. This makes large-scale exploration of future hypotheses costly and limits performance when long-ho...

---

### 5. Event-Driven Temporal Graph Networks for Asynchronous Multi-Agent Cyber Defense in NetForge_RL

**Authors:** Igor Jankowski

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09523v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09523v1)

**Summary:** The transition of Multi-Agent Reinforcement Learning (MARL) policies from simulated cyber wargames to operational Security Operations Centers (SOCs) is fundamentally bottlenecked by the Sim2Real gap. Legacy simulators abstract away network protocol physics, rely on synchronous ticks, and provide clean state vectors rather than authentic, noisy telemetry. To resolve these limitations, we introduce NetForge_RL: a high-fidelity cyber operations simulator that reformulates network defense as an asyn...

---

### 6. Toward World Models for Epidemiology

**Authors:** Zeeshan Memon, Yiqi Su, Christo Kurisummoottil Thomas, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09519v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09519v1)

**Summary:** World models have emerged as a unifying paradigm for learning latent dynamics, simulating counterfactual futures, and supporting planning under uncertainty. In this paper, we argue that computational epidemiology is a natural and underdeveloped setting for world models. This is because epidemic decision-making requires reasoning about latent disease burden, imperfect and policy-dependent surveillance signals, and intervention effects are mediated by adaptive human behavior. We introduce a concep...

---

### 7. Integrated electro-optic attention nonlinearities for transformers

**Authors:** Luis Mickeler, Kai Lion, Alfonso Nardi, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09512v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09512v1)

**Summary:** Transformers have emerged as the dominant neural-network architecture, achieving state-of-the-art performance in language processing and computer vision. At the core of these models lies the attention mechanism, which requires a nonlinear, non-negative mapping using the Softmax function. However, although Softmax operations account for less than 1% of the total operation count, they can disproportionately bottleneck overall inference latency. Here, we use thin-film lithium niobate (TFLN) Mach-Ze...

---

### 8. RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retrieval

**Authors:** Kyle Whitecross, Negin Rahimi

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09494v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09494v1)

**Summary:** We propose RecaLLM, a set of reasoning language models post-trained to make effective use of long-context information. In-context retrieval, which identifies relevant evidence from context, and reasoning are deeply intertwined: retrieval supports reasoning, while reasoning often determines what must be retrieved. However, their interaction remains largely underexplored. In preliminary experiments on several open-source LLMs, we observe that in-context retrieval performance substantially degrades...

---

### 9. XFED: Non-Collusive Model Poisoning Attack Against Byzantine-Robust Federated Classifiers

**Authors:** Israt Jahan Mouri, Muhammad Ridowan, Muhammad Abdullah Adnan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09489v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09489v1)

**Summary:** Model poisoning attacks pose a significant security threat to Federated Learning (FL). Most existing model poisoning attacks rely on collusion, requiring adversarial clients to coordinate by exchanging local benign models and synchronizing the generation of their poisoned updates. However, sustaining such coordination is increasingly impractical in real-world FL deployments, as it effectively requires botnet-like control over many devices. This approach is costly to maintain and highly vulnerabl...

---

### 10. Sim-to-Real Transfer for Muscle-Actuated Robots via Generalized Actuator Networks

**Authors:** Jan Schneider, Mridul Mahajan, Le Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09487v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09487v1)

**Summary:** Tendon drives paired with soft muscle actuation enable faster and safer robots while potentially accelerating skill acquisition. Still, these systems are rarely used in practice due to inherent nonlinearities, friction, and hysteresis, which complicate modeling and control. So far, these challenges have hindered policy transfer from simulation to real systems. To bridge this gap, we propose a sim-to-real pipeline that learns a neural network model of this complex actuation and leverages establis...

---

### 11. SafeAdapt: Provably Safe Policy Updates in Deep Reinforcement Learning

**Authors:** Maksim Anisimov, Francesco Belardinelli, Matthew Wicker

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09452v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09452v1)

**Summary:** Safety guarantees are a prerequisite to the deployment of reinforcement learning (RL) agents in safety-critical tasks. Often, deployment environments exhibit non-stationary dynamics or are subject to changing performance goals, requiring updates to the learned policy. This leads to a fundamental challenge: how to update an RL policy while preserving its safety properties on previously encountered tasks? The majority of current approaches either do not provide formal guarantees or verify policy s...

---

### 12. An Open-Source, Open Data Approach to Activity Classification from Triaxial Accelerometry in an Ambulatory Setting

**Authors:** Sepideh Nikookar, Edward Tian, Harrison Hoffman, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09451v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09451v1)

**Summary:** The accelerometer has become an almost ubiquitous device, providing enormous opportunities in healthcare monitoring beyond step counting or other average energy estimates in 15-60 second epochs.   Objective: To develop an open data set with associated open-source code for processing 50 Hz tri-axial accelerometry-based to classify patient activity levels and natural types of movement.   Approach: Data were collected from 23 healthy subjects (16 males and seven females) aged between 23 and 62 year...

---

### 13. ECHO: Efficient Chest X-ray Report Generation with One-step Block Diffusion

**Authors:** Lifeng Chen, Tianqi You, Hao Liu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09450v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09450v1)

**Summary:** Chest X-ray report generation (CXR-RG) has the potential to substantially alleviate radiologists' workload. However, conventional autoregressive vision--language models (VLMs) suffer from high inference latency due to sequential token decoding. Diffusion-based models offer a promising alternative through parallel generation, but they still require multiple denoising iterations. Compressing multi-step denoising to a single step could further reduce latency, but often degrades textual coherence du...

---

### 14. Continuous Orthogonal Mode Decomposition: Haptic Signal Prediction in Tactile Internet

**Authors:** Mohammad Ali Vahedifar, Mojtaba Nazari, Qi Zhang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09446v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09446v1)

**Summary:** The Tactile Internet demands sub-millisecond latency and ultra-high reliability, as high latency or packet loss could lead to haptic control instability. To address this, we propose the Mode-Domain Architecture (MDA), a bilateral predictive neural network architecture designed to restore missing signals on both the human and robot sides. Unlike conventional models that extract features implicitly from raw data, MDA utilizes a novel Continuous-Orthogonal Mode Decomposition framework. By integrati...

---

### 15. AdaCubic: An Adaptive Cubic Regularization Optimizer for Deep Learning

**Authors:** Ioannis Tsingalis, Constantine Kotropoulos, Corentin Briat

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09437v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09437v1)

**Summary:** A novel regularization technique, AdaCubic, is proposed that adapts the weight of the cubic term. The heart of AdaCubic is an auxiliary optimization problem with cubic constraints that dynamically adjusts the weight of the cubic term in Newton's cubic regularized method. We use Hutchinson's method to approximate the Hessian matrix, thereby reducing computational cost. We demonstrate that AdaCubic inherits the cubically regularized Newton method's local convergence guarantees. Our experiments in ...

---

### 16. Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories

**Authors:** Wonbong Jang, Shikun Liu, Soubhik Sanyal, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09429v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09429v1)

**Summary:** Recovering camera parameters from images and rendering scenes from novel viewpoints have long been treated as separate tasks in computer vision and graphics. This separation breaks down when image coverage is sparse or poses are ambiguous, since each task needs what the other produces. We propose Rays as Pixels, a Video Diffusion Model (VDM) that learns a joint distribution over videos and camera trajectories. We represent each camera as dense ray pixels (raxels) and denoise them jointly with vi...

---

### 17. Offline Local Search for Online Stochastic Bandits

**Authors:** Gerdus Benadè, Rathish Das, Thomas Lavastida

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09423v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09423v1)

**Summary:** Combinatorial multi-armed bandits provide a fundamental online decision-making environment where a decision-maker interacts with an environment across $T$ time steps, each time selecting an action and learning the cost of that action. The goal is to minimize regret, defined as the loss compared to the optimal fixed action in hindsight under full-information. There has been substantial interest in leveraging what is known about offline algorithm design in this online setting. Offline greedy and l...

---

### 18. NOMAD: Generating Embeddings for Massive Distributed Graphs

**Authors:** Aishwarya Sarkar, Sayan Ghosh, Nathan R. Tallent, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09419v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09419v1)

**Summary:** Successful machine learning on graphs or networks requires embeddings that not only represent nodes and edges as low-dimensional vectors but also preserve the graph structure. Established methods for generating embeddings require flexible exploration of the entire graph through repeated use of random walks that capture graph structure with samples of nodes and edges. These methods create scalability challenges for massive graphs with millions-to-billions of edges because single-node solutions ha...

---

### 19. Automated Instruction Revision (AIR): A Structured Comparison of Task Adaptation Strategies for LLM

**Authors:** Solomiia Bilyk, Volodymyr Getmanskyi, Taras Firman

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09418v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09418v1)

**Summary:** This paper studies Automated Instruction Revision (AIR), a rule-induction-based method for adapting large language models (LLMs) to downstream tasks using limited task-specific examples. We position AIR within the broader landscape of adaptation strategies, including prompt optimization, retrieval-based methods, and fine-tuning. We then compare these approaches across a diverse benchmark suite designed to stress different task requirements, such as knowledge injection, structured extraction, lab...

---

### 20. PhysInOne: Visual Physics Learning and Reasoning in One Suite

**Authors:** Siyuan Zhou, Hejun Wang, Hu Cheng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09415v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09415v1)

**Summary:** We present PhysInOne, a large-scale synthetic dataset addressing the critical scarcity of physically-grounded training data for AI systems. Unlike existing datasets limited to merely hundreds or thousands of examples, PhysInOne provides 2 million videos across 153,810 dynamic 3D scenes, covering 71 basic physical phenomena in mechanics, optics, fluid dynamics, and magnetism. Distinct from previous works, our scenes feature multiobject interactions against complex backgrounds, with comprehensive ...

---

### 21. Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer

**Authors:** Yannis Montreuil, Axel Carlier, Lai Xing Ng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09414v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09414v1)

**Summary:** Learning-to-Defer routes each input to the expert that minimizes expected cost, but it assumes that the information available to every expert is fixed at decision time. Many modern systems violate this assumption: after selecting an expert, one may also choose what additional information that expert should receive, such as retrieved documents, tool outputs, or escalation context. We study this problem and call it Learning-to-Defer with advice. We show that a broad family of natural separated sur...

---

### 22. Sharp description of local minima in the loss landscape of high-dimensional two-layer ReLU neural networks

**Authors:** Jie Huang, Bruno Loureiro, Stefano Sarao Mannelli

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09412v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09412v1)

**Summary:** We study the population loss landscape of two-layer ReLU networks of the form $\sum_{k=1}^K \mathrm{ReLU}(w_k^\top x)$ in a realisable teacher-student setting with Gaussian covariates. We show that local minima admit an exact low-dimensional representation in terms of summary statistics, yielding a sharp and interpretable characterisation of the landscape. We further establish a direct link with one-pass SGD: local minima correspond to attractive fixed points of the dynamics in summary statistic...

---

### 23. OASIS: Online Activation Subspace Learning for Memory-Efficient Training

**Authors:** Sakshi Choudhary, Utkarsh Saxena, Kaushik Roy

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09406v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09406v1)

**Summary:** Training large language models (LLMs) is constrained by memory requirements, with activations accounting for a substantial fraction of the total footprint. Existing approaches reduce memory using low-rank weight parameterizations or low-rank gradient subspaces for optimizer states, while activation memory is addressed through architectural modifications or compression schemes based on periodically updated projections. We propose OASIS, an online activation subspace learning algorithm for memory-...

---

### 24. Efficient Unlearning through Maximizing Relearning Convergence Delay

**Authors:** Khoa Tran, Simon S. Woo

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09391v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09391v1)

**Summary:** Machine unlearning poses challenges in removing mislabeled, contaminated, or problematic data from a pretrained model. Current unlearning approaches and evaluation metrics are solely focused on model predictions, which limits insight into the model's true underlying data characteristics. To address this issue, we introduce a new metric called relearning convergence delay, which captures both changes in weight space and prediction space, providing a more comprehensive assessment of the model's un...

---

### 25. Is More Data Worth the Cost? Dataset Scaling Laws in a Tiny Attention-Only Decoder

**Authors:** Götz-Henrik Wiegand, Lorena Raichle, Rico Städeli, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09389v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09389v1)

**Summary:** Training Transformer language models is expensive, as performance typically improves with increasing dataset size and computational budget. Although scaling laws describe this trend at large scale, their implications in controlled, smaller-scale settings remain less explored. In this work, we isolate dataset-size effects using a strongly reduced attention-only decoder architecture. By training on progressively larger power-of-two subsets, we observe smooth performance improvements accompanied by...

---

### 26. Variational Quantum Physics-Informed Neural Networks for Hydrological PDE-Constrained Learning with Inherent Uncertainty Quantification

**Authors:** Prasad Nimantha Madusanka Ukwatta Hewage, Midhun Chakkravarthy, Ruvan Kumara Abeysekara

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09374v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09374v1)

**Summary:** We propose a Hybrid Quantum-Classical Physics-Informed Neural Network (HQC-PINN) that integrates parameterized variational quantum circuits into the PINN framework for hydrological PDE-constrained learning. Our architecture encodes multi-source remote sensing features into quantum states via trainable angle encoding, processes them through a hardware-efficient variational ansatz with entangling layers, and constrains the output using the Saint-Venant shallow water equations and Manning's flow eq...

---

### 27. Biologically-Grounded Multi-Encoder Architectures as Developability Oracles for Antibody Design

**Authors:** Simon J. Crouzet

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09369v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09369v1)

**Summary:** Generative models can now propose thousands of \emph{de novo} antibody sequences, yet translating these designs into viable therapeutics remains constrained by the cost of biophysical characterization. Here we present CrossAbSense, a framework of property-specific neural oracles that combine frozen protein language model encoders with configurable attention decoders, identified through a systematic hyperparameter campaign totaling over 200 runs per property. On the GDPa1 benchmark of 242 therape...

---

### 28. Stochastic-Dimension Frozen Sampled Neural Network for High-Dimensional Gross-Pitaevskii Equations on Unbounded Domains

**Authors:** Zhangyong Liang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09361v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09361v1)

**Summary:** In this paper, we propose a stochastic-dimension frozen sampled neural network (SD-FSNN) for solving a class of high-dimensional Gross-Pitaevskii equations (GPEs) on unbounded domains. SD-FSNN is unbiased across all dimensions, and its computational cost is independent of the dimension, avoiding the exponential growth in computational and memory costs associated with Hermite-basis discretizations. Additionally, we randomly sample the hidden weights and biases of the neural network, significantly...

---

### 29. Bringing Clustering to MLL: Weakly-Supervised Clustering for Partial Multi-Label Learning

**Authors:** Yu Chen, Weijun Lv, Yue Huang, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09359v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09359v1)

**Summary:** Label noise in multi-label learning (MLL) poses significant challenges for model training, particularly in partial multi-label learning (PML) where candidate labels contain both relevant and irrelevant labels. While clustering offers a natural approach to exploit data structure for noise identification, traditional clustering methods cannot be directly applied to multi-label scenarios due to a fundamental incompatibility: clustering produces membership values that sum to one per instance, wherea...

---

### 30. Drift-Aware Online Dynamic Learning for Nonstationary Multivariate Time Series: Application to Sintering Quality Prediction

**Authors:** Yumeng Zhao, Shengxiang Yang, Xianpeng Wang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09358v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09358v1)

**Summary:** Accurate prediction of nonstationary multivariate time series remains a critical challenge in complex industrial systems such as iron ore sintering. In practice, pronounced concept drift compounded by significant label verification latency rapidly degrades the performance of offline-trained models. Existing methods based on static architectures or passive update strategies struggle to simultaneously extract multi-scale spatiotemporal features and overcome the stability-plasticity dilemma without...

---

### 31. Hierarchical Flow Decomposition for Turning Movement Prediction at Signalized Intersections

**Authors:** Md Atiqur Rahman Mallick, Kamrul Hasan, Pulock Das, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09336v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09336v1)

**Summary:** Accurate prediction of intersection turning movements is essential for adaptive signal control but remains difficult due to the high volatility of directional flows. This study proposes HFD-TM (Hierarchical Flow-Decomposition for Turning Movement Prediction), a hierarchical deep learning framework that predicts turning movements by first forecasting corridor through-movements and then expanding these predictions to individual turning streams. This design is motivated by empirical traffic structu...

---

### 32. Stability Enhanced Gaussian Process Variational Autoencoders

**Authors:** Carl R. Richardson, Jichen Zhang, Ethan King, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09331v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09331v1)

**Summary:** A novel stability-enhanced Gaussian process variational autoencoder (SEGP-VAE) is proposed for indirectly training a low-dimensional linear time invariant (LTI) system, using high-dimensional video data. The mean and covariance function of the novel SEGP prior are derived from the definition of an LTI system, enabling the SEGP to capture the indirectly observed latent process using a combined probabilistic and interpretable physical model. The search space of LTI parameters is restricted to the ...

---

### 33. Transferable FB-GNN-MBE Framework for Potential Energy Surfaces: Data-Adaptive Transfer Learning in Deep Learned Many-Body Expansion Theory

**Authors:** Siqi Chen, Zhiqiang Wang, Yili Shen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09320v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09320v1)

**Summary:** Mechanistic understanding and rational design of complex chemical systems depend on fast and accurate predictions of electronic structures beyond individual building blocks. However, if the system exceeds hundreds of atoms, first-principles quantum mechanical (QM) modeling becomes impractical. In this study, we developed FB-GNN-MBE by integrating a fragment-based graph neural network (FB-GNN) into the many-body expansion (MBE) theory and demonstrated its capacity to reproduce first-principles po...

---

### 34. Iterative Identification Closure: Amplifying Causal Identifiability in Linear SEMs

**Authors:** Ziyi Ding, Xiao-Ping Zhang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09309v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09309v1)

**Summary:** The Half-Trek Criterion (HTC) is the primary graphical tool for determining generic identifiability of causal effect coefficients in linear structural equation models (SEMs) with latent confounders. However, HTC is inherently node-wise: it simultaneously resolves all incoming edges of a node, leaving a gap of "inconclusive" causal effects (15-23% in moderate graphs). We introduce Iterative Identification Closure (IIC), a general framework that decouples causal identification into two phases: (1)...

---

### 35. Online Intention Prediction via Control-Informed Learning

**Authors:** Tianyu Zhou, Zihao Liang, Zehui Lu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09303v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09303v1)

**Summary:** This paper presents an online intention prediction framework for estimating the goal state of autonomous systems in real time, even when intention is time-varying, and system dynamics or objectives include unknown parameters. The problem is formulated as an inverse optimal control / inverse reinforcement learning task, with the intention treated as a parameter in the objective. A shifting horizon strategy discounts outdated information, while online control-informed learning enables efficient gr...

---

### 36. Meta-Learned Basis Adaptation for Parametric Linear PDEs

**Authors:** Vikas Dwivedi, Monica Sigovan, Bruno Sixou

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09289v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09289v1)

**Summary:** We propose a hybrid physics-informed framework for solving families of parametric linear partial differential equations (PDEs) by combining a meta-learned predictor with a least-squares corrector. The predictor, termed \textbf{KAPI} (Kernel-Adaptive Physics-Informed meta-learner), is a shallow task-conditioned model that maps query coordinates and PDE parameters to solution values while internally generating an interpretable, task-adaptive Gaussian basis geometry. A lightweight meta-network maps...

---

### 37. Are Independently Estimated View Uncertainties Comparable? Unified Routing for Trusted Multi-View Classification

**Authors:** Yilin Zhang, Cai Xu, Haishun Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09288v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09288v1)

**Summary:** Trusted multi-view classification typically relies on a view-wise evidential fusion process: each view independently produces class evidence and uncertainty, and the final prediction is obtained by aggregating these independent opinions. While this design is modular and uncertainty-aware, it implicitly assumes that evidence from different views is numerically comparable. In practice, however, this assumption is fragile. Different views often differ in feature space, noise level, and semantic gra...

---

### 38. Distributed Online Convex Optimization with Compressed Communication: Optimal Regret and Applications

**Authors:** Sifan Yang, Dan-Yue Li, Lijun Zhang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09276v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09276v1)

**Summary:** Distributed online convex optimization (D-OCO) is a powerful paradigm for modeling distributed scenarios with streaming data. However, the communication cost between local learners and the central server is substantial in large-scale applications. To alleviate this bottleneck, we initiate the study of D-OCO with compressed communication. Firstly, to quantify the compression impact, we establish the $Ω(δ^{-1/2}\sqrt{T})$ and $Ω(δ^{-1}\log{T})$ lower bounds for convex and strongly convex loss func...

---

### 39. The causal relation between off-street parking and electric vehicle adoption in Scotland

**Authors:** Bernardino D'Amico, Achille Fonzone, Emma Hart

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09271v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09271v1)

**Summary:** The transition to electric mobility hinges on maximising aggregate adoption while also facilitating equitable access. This study examines whether the 'charging divide' between households with and without off-street parking reflects a genuine infrastructure constraint or a by-product of socio-economic disparity. Moving beyond conventional predictive models, we apply a probabilistic causal framework to a nationally representative dataset of Scottish households, enabling estimation of policy interv...

---

### 40. Natural Riemannian gradient for learning functional tensor networks

**Authors:** Nikolas Klug, Michael Ulbrich, Marius Willner, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09263v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09263v1)

**Summary:** We consider machine learning tasks with low-rank functional tree tensor networks (TTN) as the learning model. While in the case of least-squares regression, low-rank functional TTNs can be efficiently optimized using alternating optimization, this is not directly possible in other problems, such as multinomial logistic regression. We propose a natural Riemannian gradient descent type approach applicable to arbitrary losses which is based on the natural gradient by Amari. In particular, the searc...

---

### 41. Beyond Segmentation: Structurally Informed Facade Parsing from Imperfect Images

**Authors:** Maciej Janicki, Aleksander Plocharski, Przemyslaw Musialski

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09260v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09260v1)

**Summary:** Standard object detectors typically treat architectural elements independently, often resulting in facade parsings that lack the structural coherence required for downstream procedural reconstruction. We address this limitation by augmenting the YOLOv8 training objective with a custom lightweight alignment loss. This regularization encourages grid-consistent arrangements of bounding boxes during training, effectively injecting geometric priors without altering the standard inference pipeline. Ex...

---

### 42. Nexus: Same Pretraining Loss, Better Downstream Generalization via Common Minima

**Authors:** Huanran Chen, Huaqing Zhang, Xiao Li, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09258v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09258v1)

**Summary:** Pretraining is the cornerstone of Large Language Models (LLMs), dominating the vast majority of computational budget and data to serve as the primary engine for their capabilities. During pretraining, LLMs acquire foundational knowledge from an unprecedentedly massive and diverse data sources, encompassing a vast array of domains such as general language, mathematics, code, and complex reasoning. In this work, we investigate an interesting geometric question regarding the converged state of pret...

---

### 43. DiffHLS: Differential Learning for High-Level Synthesis QoR Prediction with GNNs and LLM Code Embeddings

**Authors:** Zedong Peng, Zeju Li, Qiang Xu, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09240v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09240v1)

**Summary:** High-Level Synthesis (HLS) compiles C/C++ into RTL, but exploring pragma-driven optimization choices remains expensive because each design point requires time-consuming synthesis. We propose \textbf{\DiffHLS}, a differential learning framework for HLS Quality-of-Result (QoR) prediction that learns from kernel--design pairs: a kernel baseline and a pragma-inserted design variant. \DiffHLS~encodes kernel and design intermediate-representation graphs with dedicated graph neural network (GNN) branch...

---

### 44. Statistical Properties of the King Wen Sequence: An Anti-Habituation Structure That Does Not Improve Neural Network Training

**Authors:** Augustin Chan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09234v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09234v1)

**Summary:** The King Wen sequence of the I-Ching (c. 1000 BC) orders 64 hexagrams -- states of a six-dimensional binary space -- in a pattern that has puzzled scholars for three millennia. We present a rigorous statistical characterization of this ordering using Monte Carlo permutation analysis against 100,000 random baselines. We find that the sequence has four statistically significant properties: higher-than-random transition distance (98.2nd percentile), negative lag-1 autocorrelation (p=0.037), yang-ba...

---

### 45. A Predictive View on Streaming Hidden Markov Models

**Authors:** Gerardo Duran-Martin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09208v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09208v1)

**Summary:** We develop a predictive-first optimisation framework for streaming hidden Markov models. Unlike classical approaches that prioritise full posterior recovery under a fully specified generative model, we assume access to regime-specific predictive models whose parameters are learned online while maintaining a fixed transition prior over regimes. Our objective is to sequentially identify latent regimes while maintaining accurate step-ahead predictive distributions. Because the number of possible re...

---

### 46. On the Role of DAG topology in Energy-Aware Cloud Scheduling : A GNN-Based Deep Reinforcement Learning Approach

**Authors:** Anas Hattay, Fred Ngole Mboula, Eric Gascard, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09202v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09202v1)

**Summary:** Cloud providers must assign heterogeneous compute resources to workflow DAGs while balancing competing objectives such as completion time, cost, and energy consumption. In this work, we study a single-workflow, queue-free scheduling setting and consider a graph neural network (GNN)-based deep reinforcement learning scheduler designed to minimize workflow completion time and energy usage. We identify specific out-of-distribution (OOD) conditions under which GNN-based deep reinforcement learning s...

---

### 47. Do LLMs Follow Their Own Rules? A Reflexive Audit of Self-Stated Safety Policies

**Authors:** Avni Mittal

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09189v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09189v1)

**Summary:** LLMs internalize safety policies through RLHF, yet these policies are never formally specified and remain difficult to inspect. Existing benchmarks evaluate models against external standards but do not measure whether models understand and enforce their own stated boundaries. We introduce the Symbolic-Neural Consistency Audit (SNCA), a framework that (1) extracts a model's self-stated safety rules via structured prompts, (2) formalizes them as typed predicates (Absolute, Conditional, Adaptive), ...

---

### 48. MixFlow: Mixed Source Distributions Improve Rectified Flows

**Authors:** Nazir Nayal, Christopher Wewer, Jan Eric Lenssen

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09181v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09181v1)

**Summary:** Diffusion models and their variations, such as rectified flows, generate diverse and high-quality images, but they are still hindered by slow iterative sampling caused by the highly curved generative paths they learn. An important cause of high curvature, as shown by previous work, is independence between the source distribution (standard Gaussian) and the data distribution. In this work, we tackle this limitation by two complementary contributions. First, we attempt to break away from the stand...

---

### 49. Generalization and Scaling Laws for Mixture-of-Experts Transformers

**Authors:** Mansour Zoubeirou a Mayaki

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09175v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09175v1)

**Summary:** We develop a theory of generalization and scaling for Mixture-of-Experts (MoE) Transformers that cleanly separates \emph{active} per-input capacity from routing combinatorics. By conditioning on fixed routing patterns and union-bounding across them, we derive a sup-norm covering-number bound whose metric entropy scales with the active parameter budget and incurs a MoE-specific routing overhead. Combined with a standard ERM analysis for squared loss, this yields a generalization bound under a $d$...

---

### 50. Automated Batch Distillation Process Simulation for a Large Hybrid Dataset for Deep Anomaly Detection

**Authors:** Jennifer Werner, Justus Arweiler, Indra Jungjohann, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09166v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09166v1)

**Summary:** Anomaly detection (AD) in chemical processes based on deep learning offers significant opportunities but requires large, diverse, and well-annotated training datasets that are rarely available from industrial operations. In a recent work, we introduced a large, fully annotated experimental dataset for batch distillation under normal and anomalous operating conditions. In the present study, we augment this dataset with a corresponding simulation dataset, creating a novel hybrid dataset. The simul...

---

## cs.NE

**50 papers**

### 1. Drift-Aware Online Dynamic Learning for Nonstationary Multivariate Time Series: Application to Sintering Quality Prediction

**Authors:** Yumeng Zhao, Shengxiang Yang, Xianpeng Wang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09358v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09358v1)

**Summary:** Accurate prediction of nonstationary multivariate time series remains a critical challenge in complex industrial systems such as iron ore sintering. In practice, pronounced concept drift compounded by significant label verification latency rapidly degrades the performance of offline-trained models. Existing methods based on static architectures or passive update strategies struggle to simultaneously extract multi-scale spatiotemporal features and overcome the stability-plasticity dilemma without...

---

### 2. A 0.5-V Linear Neuromorphic Voltage-to-Spike Encoder Using a Bulk-Driven Transconductor

**Authors:** Meysam Akbari, Erika Covi, Kea-Tiong Tang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09315v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09315v1)

**Summary:** This work introduces an ultralow-power voltage-to-spike encoder that achieves near-linear voltage-to-firing-rate conversion by pairing a linearized bulk-driven transconductor with a DPI-based LIF neuron. A tail-less bulk-driven differential pair improves large-signal linearity, while a translinear linearization network suppresses the dominant sinh nonlinearity and stabilizes the bias-tunable V-to-I gain. The resulting current feeds a DPI front-end that linearizes current-to-spike conversion. Fab...

---

### 3. Statistical Properties of the King Wen Sequence: An Anti-Habituation Structure That Does Not Improve Neural Network Training

**Authors:** Augustin Chan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09234v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09234v1)

**Summary:** The King Wen sequence of the I-Ching (c. 1000 BC) orders 64 hexagrams -- states of a six-dimensional binary space -- in a pattern that has puzzled scholars for three millennia. We present a rigorous statistical characterization of this ordering using Monte Carlo permutation analysis against 100,000 random baselines. We find that the sequence has four statistically significant properties: higher-than-random transition distance (98.2nd percentile), negative lag-1 autocorrelation (p=0.037), yang-ba...

---

### 4. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 5. Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity

**Authors:** Kentaro Nomura, Takato Horii

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09026v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09026v1)

**Summary:** Social agents both internalize collective norms and reshape them through creative action, yet computational models have not captured this bidirectional process within a unified framework. We propose a multi-agent simulation model grounded in active inference that formalizes the dialectical constitution of social reality on a structured social network. Each agent maintains an internal generative model, communicates with neighbors to form social priors, creates novel observations, and selectively ...

---

### 6. Ge$^\text{2}$mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer

**Authors:** Zecheng Hao, Shenghao Xie, Kang Chen, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08894v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08894v1)

**Summary:** Spiking Neural Networks (SNNs) offer superior energy efficiency over Artificial Neural Networks (ANNs). However, they encounter significant deficiencies in training and inference metrics when applied to Spiking Vision Transformers (S-ViTs). Existing paradigms including ANN-SNN Conversion and Spatial-Temporal Backpropagation (STBP) suffer from inherent limitations, precluding concurrent optimization of memory, accuracy and energy consumption. To address these issues, we propose Ge$^\text{2}$mS-T,...

---

### 7. Hierarchical Kernel Transformer: Multi-Scale Attention with an Information-Theoretic Approximation Analysis

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08829v1)

**Summary:** The Hierarchical Kernel Transformer (HKT) is a multi-scale attention mechanism that processes sequences at L resolution levels via trainable causal downsampling, combining level-specific score matrices through learned convex weights. The total computational cost is bounded by 4/3 times that of standard attention, reaching 1.3125x for L = 3. Four theoretical results are established. (i) The hierarchical score matrix defines a positive semidefinite kernel under a sufficient condition on the symmet...

---

### 8. Memory Wall is not gone: A Critical Outlook on Memory Architecture in Digital Neuromorphic Computing

**Authors:** Amirreza Yousefzadeh, Sameed Sohail, Ana Lucia Varbanescu

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08774v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08774v1)

**Summary:** The rapid advancement of neuromorphic technology aims to address the memory wall challenge inherent in conventional von Neumann architectures. This paper critically examines current digital neuromorphic processors and their strategies to mitigate this bottleneck. While designed to bring computation closer to memory through distributed architectures, our findings indicate that on-chip memory systems, including SRAM and emerging technologies like STT-MRAM, have become significant consumers of area...

---

### 9. A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need

**Authors:** Hananel Hazan, Yanbo Zhang, Benedikt Hartl, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08749v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08749v1)

**Summary:** How many of a neural network's parameters actually encode task-specific information? We investigate this question with LottaLoRA, a training paradigm in which every backbone weight is drawn at random and frozen; only low-rank LoRA adapters are trained. Across nine benchmarks spanning diverse architecture families from single-layer classifiers to 900M parameter Transformers low-rank adapters over frozen random backbones recover 96-100% of fully trained performance while training only 0.5-40% of t...

---

### 10. Multi-Modal Learning meets Genetic Programming: Analyzing Alignment in Latent Space Optimization

**Authors:** Benjamin Léger, Kazem Meidani, Christian Gagné

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08324v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08324v1)

**Summary:** Symbolic regression (SR) aims to discover mathematical expressions from data, a task traditionally tackled using Genetic Programming (GP) through combinatorial search over symbolic structures. Latent Space Optimization (LSO) methods use neural encoders to map symbolic expressions into continuous spaces, transforming the combinatorial search into continuous optimization. SNIP (Meidani et al., 2024), a contrastive pre-training model inspired by CLIP, advances LSO by introducing a multi-modal appro...

---

### 11. Robust Multi-Objective Optimization for Bicycle Rebalancing in Shared Mobility Systems

**Authors:** Diego Daniel Pedroza-Perez, Gabriel Luque, Sergio Nesmachnow, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08296v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08296v1)

**Summary:** Dock-based bike-sharing systems exhibit spatial imbalances between bicycle supply and user demand, often addressed through overnight truck-based rebalancing. This work studies static overnight rebalancing under demand uncertainty modeled as a tri-objective optimization problem. The objectives minimize total travel distance, expected unmet demand, and a robustness-oriented unmet demand measure over high-demand scenarios.   Route plans are evaluated via a recourse simulation that enforces truck lo...

---

### 12. Introducing Echo Networks for Computational Neuroevolution

**Authors:** Christian Kroos, Fabian Küch

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08204v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08204v1)

**Summary:** For applications on the extreme edge, minimal networks of only a few dozen artificial neurons for event detection and classification in discrete time signals would be highly desirable. Feed-forward networks, RNNs, and CNNs evolved through evolutionary algorithms can all be successful in this respect but pose the problem of allowing little systematicity in mutation and recombination if the standard direct genetic encoding of the weights is used (as for instance in the classic NEAT algorithm). We ...

---

### 13. Exploration of Pareto-preserving Search Space Transformations in Multi-objective Test Functions

**Authors:** Diedeerick Vermetten, Jeroen Rook

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08173v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08173v1)

**Summary:** Benchmark problems are an important tool for gaining understanding of optimization algorithms. Since algorithms often aim to perform well on benchmarks, biases in benchmark design provide misleading insights. In single-objective optimization, for example, many problems used to have their optimum in the center of the search domain. To remedy these issues, search space transformations have been widely adopted by benchmark suites, preventing algorithms from exploiting unintended structure.   In mul...

---

### 14. Internal noise in deep neural networks: interplay of depth, neuron number, and noise injection step

**Authors:** D. A. Maksimov, V. M. Moskvitin, N. Semenova

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08117v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08117v1)

**Summary:** This paper examines the influence of internal Gaussian noise on the performance of deep feedforward neural networks, focusing on the role of the noise injection stage relative to the activation function. Two scenarios are analyzed: noise introduced before and after the activation function, for both additive and multiplicative noise influence. The case of noise before activation function is similar to perturbations in the input channel of neuron, while the noise introduced after activation functi...

---

### 15. Analysis of Search Heuristics in the Multi-Armed Bandit Setting

**Authors:** Jasmin Brandt, Barbara Hammer, Timo Kötzing, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08109v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08109v1)

**Summary:** We consider the classic Multi-Armed Bandit setting to understand the exploration/exploitation tradeoffs made by different search heuristics. Since many search heuristics work by comparing different options (in evolutionary algorithms called "individuals"; in the Bandit literature called "arms"), we work with the "Dueling Bandits" setting. In each iteration, a comparison between different arms can be made; in the binary stochastic setting, each arm has a fixed winning probability against any othe...

---

### 16. Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency

**Authors:** Mingqing Xiao, Yansen Wang, Dongqi Han, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07904v1)

**Summary:** Spatiotemporal neural dynamics and oscillatory synchronization are widely implicated in biological information processing and have been hypothesized to support flexible coordination such as feature binding. By contrast, most deep learning architectures represent and propagate information through activation values, neglecting the joint dynamics of rate and phase. In this work, we introduce Kuramoto oscillatory Phase Encoding (KoPE) as an additional, evolving phase state to Vision Transformers, in...

---

### 17. PyVRP$^+$: LLM-Driven Metacognitive Heuristic Evolution for Hybrid Genetic Search in Vehicle Routing Problems

**Authors:** Manuj Malik, Jianan Zhou, Shashank Reddy Chirra, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07872v1)

**Summary:** Designing high-performing metaheuristics for NP-hard combinatorial optimization problems, such as the Vehicle Routing Problem (VRP), remains a significant challenge, often requiring extensive domain expertise and manual tuning. Recent advances have demonstrated the potential of large language models (LLMs) to automate this process through evolutionary search. However, existing methods are largely reactive, relying on immediate performance feedback to guide what are essentially black-box code mut...

---

### 18. Trilinear Compute-in-Memory Architecture for Energy-Efficient Transformer Acceleration

**Authors:** Md Zesun Ahmed Mia, Jiahui Duan, Kai Ni, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07628v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07628v1)

**Summary:** Self-attention in Transformers generates dynamic operands that force conventional Compute-in-Memory (CIM) accelerators into costly non-volatile memory (NVM) reprogramming cycles, degrading throughput and stressing device endurance. Existing solutions either reduce but retain NVM writes through matrix decomposition or sparsity, or move attention computation to digital CMOS at the expense of NVM density. We present TrilinearCIM, a Double-Gate FeFET (DG-FeFET)-based architecture that uses back-gate...

---

### 19. Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting

**Authors:** Yumeng Zha, Shengxiang Yang, Xianpeng Wang

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07610v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07610v1)

**Summary:** Industrial forecasting often involves multi-source asynchronous signals and multi-output targets, while deployment requires explicit trade-offs between prediction error and model complexity. Current practices typically fix alignment strategies or network designs, making it difficult to systematically co-design preprocessing, architecture, and hyperparameters in budget-limited training-based evaluations. To address this issue, we propose an auto-configuration framework that outputs a deployable P...

---

### 20. The Principle of Maximum Heterogeneity Optimises Productivity in Distributed Production Systems Across Biology, Economics, and Computing

**Authors:** Guillhem Artis, Danyal Akarca, Jascha Achterberg

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07602v1)

**Summary:** The world is full of systems of distributed agents, collaborating and competing in complex ways: firms and workers specialise within economies, neurons adapt their tuning across brain circuits, and species compete and coexist within ecosystems. In that context, individual research fields built theories explaining how comparative advantage drives trade specialisation, how balanced neural representations emerge from sensory coding, and how biodiversity sustains ecological productivity. Here we pro...

---

### 21. When Switching Algorithms Helps: A Theoretical Study of Online Algorithm Selection

**Authors:** Denis Antipov, Carola Doerr

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07473v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07473v1)

**Summary:** Online algorithm selection (OAS) aims to adapt the optimization process to changes in the fitness landscape and is expected to outperform any single algorithm from a given portfolio. Although this expectation is supported by numerous empirical studies, there are currently no theoretical results proving that OAS can yield asymptotic speedups (apart from some artificial examples for hyper-heuristics). Moreover, theory-based guidelines for when and how to switch between algorithms are largely missi...

---

### 22. Anytime Analysis on BinVal: Adaptive Parameters Help

**Authors:** Timo Kötzing, Jurek Sander

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06976v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06976v1)

**Summary:** While most theoretical run time analyses of discrete randomized search heuristics provide bounds on the expected number of evaluations to find the global optimum, we consider the anytime performance of evolutionary and estimation-of-distribution algorithms. For this purpose, we analyze the fixed-target run time of various algorithms using BinVal as fitness function and bound the run time to optimize the most significant $k \in o(n)$ bits of a bit string with length $n$. We analyze the run times ...

---

### 23. Block-Bench: A Framework for Controllable and Transparent Discrete Optimization Benchmarking

**Authors:** Furong Ye, Frank Neumann, Thomas Bäck, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06973v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06973v1)

**Summary:** We present a novel approach for constructing discrete optimization benchmarks that enables fine-grained control over problem properties, and such benchmarks can facilitate analyzing discrete algorithm behaviors. We build benchmark problems based on a set of block functions, where each block function maps a subset of variables to a real value. Problems are instantiated through a set of block functions, weight factors, and an adjacency graph representing the dependency among the block functions. T...

---

### 24. Evaluating PQC KEMs, Combiners, and Cascade Encryption via Adaptive IND-CPA Testing Using Deep Learning

**Authors:** Simon Calderon, Niklas Johansson, Onur Günlü

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06942v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06942v1)

**Summary:** Ensuring ciphertext indistinguishability is fundamental to cryptographic security, but empirically validating this property in real implementations and hybrid settings presents practical challenges. The transition to post-quantum cryptography (PQC), with its hybrid constructions combining classical and quantum-resistant primitives, makes empirical validation approaches increasingly valuable. By modeling IND-CPA games as binary classification tasks and training on labeled ciphertext data with BCE...

---

### 25. The Traveling Thief Problem with Time Windows: Benchmarks and Heuristics

**Authors:** Helen Yuliana Angmalisang, Frank Neumann

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06724v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06724v1)

**Summary:** While traditional optimization problems were often studied in isolation, many real-world problems today require interdependence among multiple optimization components. The traveling thief problem (TTP) is a multi-component problem that has been widely studied in the literature. In this paper, we introduce and investigate the TTP with time window constraints which provides a TTP variant highly relevant to real-world situations where good can only be collected at given time intervals. We examine a...

---

### 26. Neural Network Pruning via QUBO Optimization

**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05856v1)

**Summary:** Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic im...

---

### 27. Constraint-Driven Warm-Freeze for Efficient Transfer Learning in Photovoltaic Systems

**Authors:** Yasmeen Saeed, Ahmed Sharshar, Mohsen Guizani

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.05807v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05807v1)

**Summary:** Detecting cyberattacks in photovoltaic (PV) monitoring and MPPT control signals requires models that are robust to bias, drift, and transient spikes, yet lightweight enough for resource-constrained edge controllers. While deep learning outperforms traditional physics-based diagnostics and handcrafted features, standard fine-tuning is computationally prohibitive for edge devices. Furthermore, existing Parameter-Efficient Fine-Tuning (PEFT) methods typically apply uniform adaptation or rely on exp...

---

### 28. Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales

**Authors:** Tsung-Han Kuo, Tzu-Chia Tung

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04770v1)

**Summary:** Balanced spiking networks can transition between silent, asynchronous-irregular, and oscillatory states depending on interacting synaptic and temporal time scales, while their joint parameter structure remains incompletely characterized. In this work, we systematically map how postsynaptic decay (τs), conduction delay (d), and plasticity rate (λp) jointly shape oscillatory regimes in recurrent leaky integrate-and-fire networks. By combining Brian2 simulations across the (τs, d, λp) space with a ...

---

### 29. Ranking Constraints via Topological Dual-Directional Search in Evolutionary Multi-Objective Optimization

**Authors:** Ruiqing Sun, Dawei Feng, Sheng Qi, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04724v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04724v1)

**Summary:** Existing evolutionary algorithms for Constrained Multi-objective Optimization Problems (CMOPs) typically treat all constraints uniformly, overlooking their distinct geometric relationships with the true Constrained Pareto Front (CPF). In reality, constraints play different roles: some directly shape the final CPF, some create infeasible obstacles, while others are irrelevant. To exploit this insight, we propose a novel algorithm named RCCMO, which sequentially performs unconstrained exploration,...

---

### 30. Loop-Extrusion Linkage: Spectral Ordering and Interval-Based Structure Discovery for Continuous Optimization

**Authors:** Eren Unlu

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04273v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04273v1)

**Summary:** The rapid growth of nature-inspired metaheuristics has exposed a persistent gap between metaphorical novelty and genuine algorithmic advancement. Motivated by the biophysics of chromatin loop extrusion -- a well-characterized genome-folding process driven by SMC motor complexes and conditional barriers -- we introduce the Loop-Extrusion Linkage (LEL) operator, a structure-learning wrapper that combines online variable-interaction estimation, spectral seriation via the Fiedler vector, and adaptiv...

---

### 31. Parent Selection Mechanisms in Elitist Crossover-Based Algorithms

**Authors:** Andre Opris, Denis Antipov

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04083v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04083v2)

**Summary:** Parent selection methods are widely used in evolutionary computation to accelerate the optimization process, yet their theoretical benefits are still poorly understood. In this paper, we address this gap by proposing a parent selection strategy for the $(μ+1)$ genetic algorithm (GA) that prioritizes the selection of maximally distant parents for crossover. We show that, with an appropriately chosen population size, the resulting algorithm solves the Jump$_k$ problem in $O(k4^kn\log(n))$ expected...

---

### 32. Collapse-Free Prototype Readout Layer for Transformer Encoders

**Authors:** Giansalvo Cirrincione, Rahul Ranjeev Kumar

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03850v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03850v1)

**Summary:** DDCL-Attention is a prototype-based readout layer for transformer encoders that replaces simple pooling methods, such as mean pooling or class tokens, with a learned compression mechanism. It uses a small set of global prototype vectors and assigns tokens to them through soft probabilistic matching, producing compact token summaries at linear complexity in sequence length.   The method offers three main advantages. First, it avoids prototype collapse through an exact decomposition of the trainin...

---

### 33. An Imbalanced Dataset with Multiple Feature Representations for Studying Quality Control of Next-Generation Sequencing

**Authors:** Philipp Röchner, Clarissa Krämer, Johannes U Mayer, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.04981v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04981v1)

**Summary:** Next-generation sequencing (NGS) is a key technique for studying the DNA and RNA of organisms. However, identifying quality problems in NGS data across different experimental settings remains challenging. To develop automated quality-control tools, researchers require datasets with features that capture the characteristics of quality problems. Existing NGS repositories, however, offer only a limited number of quality-related features. To address this gap, we propose a dataset derived from 37.491...

---

### 34. RDEx-CMOP: Feasibility-Aware Indicator-Guided Differential Evolution for Fixed-Budget Constrained Multiobjective Optimization

**Authors:** Sichen Tao, Yifei Yang, Ruihan Zhao, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03708v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03708v1)

**Summary:** Constrained multiobjective optimisation requires fast feasibility attainment together with stable convergence and diversity preservation under strict evaluation budgets. This report documents RDEx-CMOP, the differential evolution variant used in the IEEE CEC 2025 numerical optimisation competition (C06 special session) constrained multiobjective track. RDEx-CMOP integrates an ε-level feasibility schedule, a SPEA2-style indicator-driven fitness assignment, and a fitness-oriented current-to-pbest/...

---

### 35. TransGP: Task-Conditioned Transformer-Guided Genetic Programming for Multitask Dynamic Flexible Job Shop Scheduling

**Authors:** Meng Xu, Jiao Liu, Hua Yu, et al.

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03705v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03705v1)

**Summary:** Hyper-heuristics have become a popular approach for solving dynamic flexible job shop scheduling (DFJSS) problems. They use gradient-free optimization techniques like Genetic Programming (GP) to evolve non-differentiable heuristics. However, conventional GP methods tend to converge slowly because they rely solely on evolutionary search to find good heuristics. Existing multitask GP methods can solve multiple tasks simultaneously and speed up the search by transferring knowledge across similar ta...

---

### 36. L-SPINE: A Low-Precision SIMD Spiking Neural Compute Engine for Resource-efficient Edge Inference

**Authors:** Sonu Kumar, Mukul Lokhande, Santosh Kumar Vishvakarma

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03626v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03626v1)

**Summary:** Spiking Neural Networks (SNNs) offer a promising solution for energy-efficient edge intelligence; however, their hardware deployment is constrained by memory overhead, inefficient scaling operations, and limited parallelism. This work proposes L-SPINE, a low-precision SIMD-enabled spiking neural compute engine for efficient edge inference. The architecture features a unified multi-precision datapath supporting 2-bit, 4-bit, and 8-bit operations, leveraging a multiplier-less shift-add model for n...

---

### 37. Finding Sets of Pareto Sets in Real-World Scenarios -- A Multitask Multiobjective Perspective

**Authors:** Jiao Liu, Yew Soon Ong, Melvin Wong

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03570v1)

**Summary:** Recently, evolutionary multitasking has been employed to generate a ``set of Pareto sets" (SOS) for machine learning models, addressing diverse task settings across heterogeneous environments. This involves creating a repository of compact, specialized solution models that are collectively tailored to each specific task setting and environment, enabling users to select the most suitable model based on particular specifications and preferences. In this paper, we further demonstrate the versatilit...

---

### 38. Personality Requires Struggle: Three Regimes of the Baldwin Effect in Neuroevolved Chess Agents

**Authors:** Diego Armando Resendez Prado

**Published:** 2026-04-04

🔗 [Paper](http://arxiv.org/abs/2604.03565v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03565v1)

**Summary:** Can lifetime learning expand behavioral diversity over evolutionary time, rather than collapsing it? Prior theory predicts that plasticity reduces variance by buffering organisms against environmental noise. We test this in a competitive domain: chess agents with eight NEAT-evolved neural modules, Hebbian within-game plasticity, and a desirability-domain signal chain with imagination. Across 10~seeds per Hebbian condition, a variance crossover emerges: Hebbian ON starts with lower cross-seed var...

---

### 39. YANA: Bridging the Neuromorphic Simulation-to-Hardware Gap

**Authors:** Brian Pachideh, Sven Nitzsche, Moritz Neher, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03432v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03432v1)

**Summary:** Spiking Neural Networks (SNNs) promise significant advantages over conventional Artificial Neural Networks (ANNs) for applications requiring real-time processing of temporally sparse data streams under strict power constraints -- a concept known as the Neuromorphic Advantage. However, the limited availability of neuromorphic hardware creates a substantial simulation-to-hardware gap that impedes algorithmic innovation, hardware-software co-design, and the development of mature open-source ecosyst...

---

### 40. Activity-Dependent Plasticity in Morphogenetically-Grown Recurrent Networks

**Authors:** Sergii Medvid, Andrii Valenia, Mykola Glybovets

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03386v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03386v1)

**Summary:** Developmental approaches to neural architecture search grow functional networks from compact genomes through self-organisation, but the resulting networks operate with fixed post-growth weights. We characterise Hebbian and anti-Hebbian plasticity across 50,000 morphogenetically grown recurrent controllers (5M+ configurations on CartPole and Acrobot), then test whether co-evolutionary experiments -- where plasticity parameters are encoded in the genome and evolved alongside the developmental arch...

---

### 41. Biologically Realistic Dynamics for Nonlinear Classification in CMOS+X Neurons

**Authors:** Steven Louis, Hannah Bradley, Artem Litvinenko, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03187v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03187v1)

**Summary:** Spiking neural networks encode information in spike timing and offer a pathway toward energy efficient artificial intelligence. However, a key challenge in spiking neural networks is realizing nonlinear and expressive computation in compact, energy-efficient hardware without relying on additional circuit complexity. In this work, we examine nonlinear computation in a CMOS+X spiking neuron implemented with a magnetic tunnel junction connected in series with an NMOS transistor. Circuit simulations...

---

### 42. Accelerating Black-Box Bilevel Optimization with Rank-Based Upper-Level Value Function Approximation

**Authors:** Marc Ong, Youhei Akimoto

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02888v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02888v1)

**Summary:** Bilevel optimization is a field of significant theoretical and practical interest, yet solving such optimization problems remains challenging. Evolutionary methods have been employed to address these problems in the black-box setting; however, they incur high computational cost due to the nested nature of bilevel optimization. Although previous methods have attempted to reduce this cost through various heuristic techniques, such approaches limit versatility on challenging optimization landscapes...

---

### 43. Frame Theoretical Derivation of Three Factor Learning Rule for Oja's Subspace Rule

**Authors:** Taiki Yamada

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02849v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02849v1)

**Summary:** We show that the error-gated Hebbian rule for PCA (EGHR-PCA), a three-factor learning rule equivalent to Oja's subspace rule under Gaussian inputs, can be systematically derived from Oja's subspace rule using frame theory. The global third factor in EGHR-PCA arises exactly as a frame coefficient when the learning rule is expanded with respect to a natural frame on the space of symmetric matrices. This provides a principled, non-heuristic derivation of a biologically plausible learning rule from ...

---

### 44. Apparent Age Estimation: Challenges and Outcomes

**Authors:** Justin Rainier Go, Lorenz Bernard Marqueses, Mikaella Kaye Martinez, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03335v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03335v1)

**Summary:** Apparent age estimation is a valuable tool for business personalization, yet current models frequently exhibit demographic biases. We review prior works on the DEX method by applying distribution learning techniques such as Mean-Variance Loss (MVL) and Adaptive Mean-Residue Loss (AMRL), and evaluate them in both accuracy and fairness. Using IMDB-WIKI, APPA-REAL, and FairFace, we demonstrate that while AMRL achieves state-of-the-art accuracy, trade-offs between precision and demographic equity pe...

---

### 45. Wavelength-multiplexed massively parallel diffractive optical information storage and image projection

**Authors:** Che-Yung Shen, Yuhang Li, Cagatay Isil, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.02624v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02624v1)

**Summary:** We introduce a wavelength-multiplexed massively parallel diffractive information storage platform composed of dielectric surfaces that are structurally optimized at the wavelength scale using deep learning to store and project thousands of distinct image patterns, each assigned to a unique wavelength. Through numerical simulations in the visible spectrum, we demonstrated that our wavelength-multiplexed diffractive system can store and project over 4,000 independent desired images/patterns within...

---

### 46. Computing with Living Neurons: Chaos-Controlled Reservoir Computing with Knowledge Transplant

**Authors:** Seung Hyun Kim, Zhi Dou, Gaurav Upadhyay, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02552v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02552v1)

**Summary:** We introduce chaos-controlled Reservoir Computing (cc-RC) for living neural cultures: dynamically rich substrates of unique potential for adaptive computation. To account for intrinsic biological variability, cc-RC combines: (i) pre-training identification of each culture's dynamical signature and phase-portrait attractor; (ii) low-power optical chaos control to stabilize spontaneous and stimulus-evoked activity; (iii) readout training within this controlled regime. Across hundreds of neural sam...

---

### 47. When does learning pay off? A study on DRL-based dynamic algorithm configuration for carbon-aware scheduling

**Authors:** Andrea Mencaroni, Robbert Reijnen, Yingqian Zhang, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01886v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01886v1)

**Summary:** Deep reinforcement learning (DRL) has recently emerged as a promising tool for Dynamic Algorithm Configuration (DAC), enabling evolutionary algorithms to adapt their parameters online rather than relying on static tuned configurations. While DRL can learn effective control policies, training is computationally expensive. This cost may be justified if learned policies generalize, allowing the training effort to transfer across instance types and problem scales. Yet, for real-world optimization pr...

---

### 48. DDCL-INCRT: A Self-Organising Transformer with Hierarchical Prototype Structure (Theoretical Foundations)

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01880v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01880v1)

**Summary:** Modern neural networks of the transformer family require the practitioner to decide, before training begins, how many attention heads to use, how deep the network should be, and how wide each component should be. These decisions are made without knowledge of the task, producing architectures that are systematically larger than necessary: empirical studies find that a substantial fraction of heads and layers can be removed after training without performance loss.   This paper introduces DDCL-INCR...

---

### 49. DDCL: Deep Dual Competitive Learning: A Differentiable End-to-End Framework for Unsupervised Prototype-Based Representation Learning

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.01740v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01740v1)

**Summary:** A persistent structural weakness in deep clustering is the disconnect between feature learning and cluster assignment. Most architectures invoke an external clustering step, typically k-means, to produce pseudo-labels that guide training, preventing the backbone from directly optimising for cluster quality. This paper introduces Deep Dual Competitive Learning (DDCL), the first fully differentiable end-to-end framework for unsupervised prototype-based representation learning. The core contributio...

---

### 50. Oscillator-Based Associative Memory with Exponential Capacity: Theory, Algorithms, and Hardware Implementation

**Authors:** Arie Ogranovich, Taosha Guo, Arvind R. Venkatakrishnan, et al.

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01469v1)

**Summary:** Associative memory systems enable content-addressable storage and retrieval of patterns, a capability central to biological neural computation and artificial intelligence. Classical implementations such as Hopfield networks face fundamental limitations in memory capacity, scaling at most linearly with network size. We present an associative memory architecture based on Kuramoto oscillator networks with honeycomb topology in which memories are encoded as stable phase-locked configurations. The ho...

---

## q-bio.NC

**50 papers**

### 1. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 2. Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

**Authors:** Mu Nan, Muquan Yu, Weijian Mai, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08537v1)

**Summary:** Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge...

---

### 3. Neuromodulation supports robust rhythmic pattern transitions in degenerate central pattern generators with fixed connectivity

**Authors:** Arthur Fyon, Alessio Franci, Pierre Sacré, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08312v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08312v1)

**Summary:** Many essential biological functions, such as breathing and locomotion, rely on the coordination of robust and adaptable rhythmic patterns, governed by specific network architectures known as connectomes. Rhythmic adaptation is often linked to slow structural modifications of the connectome through synaptic plasticity, but such mechanisms are too slow to support rapid, localized rhythmic transitions. Here, we propose a neuromodulation-based control architecture for dynamically reconfiguring rhyth...

---

### 4. The Cartesian Cut in Agentic AI

**Authors:** Tim Sainburg, Caleb Weinreb

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07745v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07745v1)

**Summary:** LLMs gain competence by predicting words in human text, which often reflects how people perform tasks. Consequently, coupling an LLM to an engineered runtime turns prediction into control: outputs trigger interventions that enact goal-oriented behavior. We argue that a central design lever is where control resides in these systems. Brains embed prediction within layered feedback controllers calibrated by the consequences of action. By contrast, LLM agents implement Cartesian agency: a learned co...

---

### 5. The Principle of Maximum Heterogeneity Optimises Productivity in Distributed Production Systems Across Biology, Economics, and Computing

**Authors:** Guillhem Artis, Danyal Akarca, Jascha Achterberg

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07602v1)

**Summary:** The world is full of systems of distributed agents, collaborating and competing in complex ways: firms and workers specialise within economies, neurons adapt their tuning across brain circuits, and species compete and coexist within ecosystems. In that context, individual research fields built theories explaining how comparative advantage drives trade specialisation, how balanced neural representations emerge from sensory coding, and how biodiversity sustains ecological productivity. Here we pro...

---

### 6. Exploring the proprioceptive potential of joint receptors using a biomimetic robotic joint

**Authors:** Akihiro Miki, Shun Hasegawa, Sota Yuzaki, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07038v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07038v1)

**Summary:** In neuroscience, joint receptors have traditionally been viewed as limit detectors, providing positional information only at extreme joint angles, while muscle spindles are considered the primary sensors of joint angle position. However, joint receptors are widely distributed throughout the joint capsule, and their full role in proprioception remains unclear. In this study, we specifically focused on mimicking Type I joint receptors, which respond to slow and sustained movements, and quantified ...

---

### 7. Quantum-like Cognition in Process Theories: An Analysis

**Authors:** Sean Tull, Masanao Ozawa

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.08604v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08604v1)

**Summary:** Various effects in human cognition, often considered `non-classical', have been argued to be most naturally modelled by quantum-like models of decision making. We extend this approach to describe models of cognition and decision-making in general probabilistic process theories, which include both classical probabilistic models and quantum instrument models as special cases. We show how many aspects of quantum-like cognition can be described diagrammatically in process theories, before using our ...

---

### 8. Bridging Theory and Practice in Crafting Robust Spiking Reservoirs

**Authors:** Ruggero Freddi, Nicolas Seseri, Diana Nigrisoli, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06395v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06395v1)

**Summary:** Spiking reservoir computing provides an energy-efficient approach to temporal processing, but reliably tuning reservoirs to operate at the edge-of-chaos is challenging due to experimental uncertainty. This work bridges abstract notions of criticality and practical stability by introducing and exploiting the robustness interval, an operational measure of the hyperparameter range over which a reservoir maintains performance above task-dependent thresholds. Through systematic evaluations of Leaky I...

---

### 9. Hierarchical Mesh Transformers with Topology-Guided Pretraining for Morphometric Analysis of Brain Structures

**Authors:** Yujian Xiong, Mohammad Farazi, Yanxi Chen, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05215v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05215v1)

**Summary:** Representation learning on large-scale unstructured volumetric and surface meshes poses significant challenges in neuroimaging, especially when models must incorporate diverse vertex-level morphometric descriptors, such as cortical thickness, curvature, sulcal depth, and myelin content, which carry subtle disease-related signals. Current approaches either ignore these clinically informative features or support only a single mesh topology, restricting their use across imaging pipelines. We introd...

---

### 10. Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization

**Authors:** Arthur N. Montanari, Francesco Bullo, Dmitry Krotov, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05042v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05042v1)

**Summary:** Recent advances at the intersection of control theory, neuroscience, and machine learning have revealed novel mechanisms by which dynamical systems perform computation. These advances encompass a wide range of conceptual, mathematical, and computational ideas, with applications for model learning and training, memory retrieval, data-driven control, and optimization. This tutorial focuses on neuro-inspired approaches to computation that aim to improve scalability, robustness, and energy efficienc...

---

### 11. Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales

**Authors:** Tsung-Han Kuo, Tzu-Chia Tung

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04770v1)

**Summary:** Balanced spiking networks can transition between silent, asynchronous-irregular, and oscillatory states depending on interacting synaptic and temporal time scales, while their joint parameter structure remains incompletely characterized. In this work, we systematically map how postsynaptic decay (τs), conduction delay (d), and plasticity rate (λp) jointly shape oscillatory regimes in recurrent leaky integrate-and-fire networks. By combining Brian2 simulations across the (τs, d, λp) space with a ...

---

### 12. Causal Stance

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05004v2) | 📄 [PDF](https://arxiv.org/pdf/2604.05004v2)

**Summary:** What exactly is the meaning of physical causal closure, a concept frequently discussed in the philosophy of mind? Jaegwon Kim explicitly adopts a conception of causation according to which physical causation is effectively identified with deterministic physical lawfulness, and on this basis equates physical determinism with physical causal closure. While this conception is internally coherent, it differs from the currently dominant theories of causation, which emphasize asymmetry between cause a...

---

### 13. Non-Equilibrium Stochastic Dynamics as a Unified Framework for Insight and Repetitive Learning: A Kramers Escape Approach to Continual Learning

**Authors:** Gunn Kim

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04154v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04154v1)

**Summary:** Continual learning in artificial neural networks is fundamentally limited by the stability--plasticity dilemma: systems that retain prior knowledge tend to resist acquiring new knowledge, and vice versa. Existing approaches, most notably elastic weight consolidation~(EWC), address this empirically without a physical account of why plasticity eventually collapses as tasks accumulate. Separately, the distinction between sudden insight and gradual skill acquisition through repetitive practice has l...

---

### 14. The physical basis of information flow in neural matter: a thermocoherent perspective on cognitive dynamics

**Authors:** Onur Pusuluk

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04069v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04069v1)

**Summary:** Information flow is central to contemporary accounts of cognition, yet its physical basis in living neural matter remains poorly specified. Here, we develop a multiscale resource-theoretical framework motivated by the \textit{thermocoherent effect}, where heat flow is reciprocally coupled to a delocalized information flow carried by shared coherence and not reducible to local subsystem variables. Extending this line of work in light of recent results on correlation-enabled Mpemba-type thermal re...

---

### 15. Topological Sensitivity in Connectome-Constrained Neural Networks

**Authors:** Nalin Dhiman

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04033v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04033v1)

**Summary:** Connectome-constrained neural networks are often evaluated against sparse random controls and then interpreted as evidence that biological graph topology improves learning efficiency. We revisit that claim in a controlled flyvis-based study using a Drosophila connectome, a naive self-loop-matched random graph, and a degree-preserving rewired null. Under weak controls, in which both models were recovered from a connectome-trained checkpoint and the null matched only global graph counts, the conne...

---

### 16. Neurological Plausibility of AI-Generated Music for Commercial Environments: An In-Silico Cortical Investigation Using Wubble and TRIBE v2

**Authors:** Shaad Sufi

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04025v1)

**Summary:** Background music shapes attention, affect, and approach behavior in commercial environments, yet the neural plausibility of AI-generated music for such settings remains poorly characterized. We present an in-silico pilot study that combines Wubble, a generative music system, with TRIBE v2, a publicly released whole-brain encoding model, to estimate cortical response profiles for prompt-conditioned retail music. Five fully instrumental tracks were generated to span low-to-high arousal, sparse-to-...

---

### 17. Large Language Models Align with the Human Brain during Creative Thinking

**Authors:** Mete Ismayilzada, Simone A. Luchini, Abdulkadir Gokce, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03480v1)

**Summary:** Creative thinking is a fundamental aspect of human cognition, and divergent thinking-the capacity to generate novel and varied ideas-is widely regarded as its core generative engine. Large language models (LLMs) have recently demonstrated impressive performance on divergent thinking tests and prior work has shown that models with higher task performance tend to be more aligned to human brain activity. However, existing brain-LLM alignment studies have focused on passive, non-creative tasks. Here...

---

### 18. Self-Supervised Foundation Model for Calcium-imaging Population Dynamics

**Authors:** Xinhong Xu, Yimeng Zhang, Qichen Qian, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.04958v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04958v2)

**Summary:** Recent work suggests that large-scale, multi-animal modeling can significantly improve neural recording analysis. However, for functional calcium traces, existing approaches remain task-specific, limiting transfer across common neuroscience objectives. To address this challenge, we propose \textbf{CalM}, a self-supervised neural foundation model trained solely on neuronal calcium traces and adaptable to multiple downstream tasks, including forecasting and decoding. Our key contribution is a pret...

---

### 19. Temporal structure of the language hierarchy within small cortical patches

**Authors:** Julien Gadonneix, Mingfang Zhang, Jérémy Rapin, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03021v1)

**Summary:** Speech production requires the rapid coordination of a complex hierarchy of linguistic units, transforming a semantic representation into a precise sequence of articulatory movements. To unravel the neural mechanisms underlying this feat, we leverage recordings from eight 3.2 x 3.2 mm 64-microelectrode arrays implanted in the motor cortex and inferior frontal gyrus of two patients tasked to produce twenty thousand sentences. We show that a hierarchy of linguistic features are robustly encoded in...

---

### 20. Mapping generative AI use in the human brain: divergent neural, academic, and mental health profiles of functional versus socio emotional AI use

**Authors:** Junjie Wang, Xianyang Gan, Dan Liu, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.08594v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08594v1)

**Summary:** The widespread adoption of generative artificial intelligence conversational agents (AICAs) among university students constitutes a novel cognitive social environment whose impact on the maturing brain remains elusive. Combining surveys with high resolution structural MRI, we examined patterns of general, functional, and socio emotional AICA use, academic performance, mental health, and brain structural signatures in a comparatively large sample of 222 young individuals. Across computational ana...

---

### 21. Phase estimation with autoregressive padding (PEAP): addressing inaccuracies and biases in EEG analysis

**Authors:** Miriam Kirchhoff, Johanna Rösch, Maria Ermolova, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02212v1)

**Summary:** Accurate phase estimation at the edge of data segments is crucial for EEG applications such as EEG-TMS in offline and real-time data analysis. Our research evaluates the phase estimation performance of four commonly used methods (Phastimate, SSPE, ETP, and PhastPadding) for accuracy and systemic biases, using data from young and elderly healthy controls and chronic stroke participants. To address the identified limitations of the established methods, we introduce Phase Estimation with Autoregres...

---

### 22. Thermodynamic connectivity reveals functional specialization and multiplex organization of extrasynaptic signaling

**Authors:** Giridhar Sunil, Habib Benali, Elkaïoum M. Moutuou

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02057v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02057v1)

**Summary:** Neural communication operates on both fast synaptic transmission and slower, diffusive extrasynaptic signaling, yet how these two modes jointly organize brain function remains unclear. Here, using the complete synaptic and neuropeptidergic connectomes of \emph{Caenorhabditis elegans}, we develop a unified multiplex framework linking anatomical wiring to functional communication. We infer structure-derived functional connectivity from the synaptic connectome using equilibrium principles from stat...

---

### 23. Interpretable Electrophysiological Features of Resting-State EEG Capture Cortical Network Dynamics in Parkinsons Disease

**Authors:** Antonios G. Dougalis

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01475v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01475v1)

**Summary:** Parkinsons disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive. This study examined whether interpretable EEG features capturing complementary aspects of neural dynamics can discriminate Parkinsonian neural states. A comprehensive set of interpretable features was extracted and grouped into Standard descriptors (spectral power, phase synchronization, time-domain statistics) and Dynamical descriptors (aperiodic activity, cross-fre...

---

### 24. Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models

**Authors:** Po-Han Chiang

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.01295v1) | 📄 [PDF](https://arxiv.org/pdf/2604.01295v1)

**Summary:** This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Conventional SSMs achieve high-speed sequence processing through parallel scans, yet are limited to temporal recurrence without lateral or feedback interactions within a single timestep. PHC maps the diagonal SSM core to a shared Neuron Layer and inter-neuronal communication to a shared Synapse Layer, where neurons ar...

---

### 25. Ultrasonic Brain Computer Interfaces for Enhancing Human-Machine Cognition

**Authors:** William J. Tyler

**Published:** 2026-04-01

🔗 [Paper](http://arxiv.org/abs/2604.00349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.00349v1)

**Summary:** Low-intensity transcranial focused ultrasound (tFUS) is rapidly emerging as a transformative non-invasive brain stimulation (NIBS) modality characterized by high spatial resolution and ability to target deep brain circuits. Unlike electromagnetic techniques such as transcranial magnetic stimulation and transcranial direct current stimulation, which are constrained by centimeter-scale resolution and a depth-focality tradeoff, tFUS leverages mechanical pressure waves to modulate both superficial c...

---

### 26. From Patterns to Policy: A Scoping Review Based on Bibliometric Analysis (ScoRBA) of Intelligent and Secure Smart Hospital Ecosystems

**Authors:** Adi Wijaya, Budi Hermawan, Wiga Maulana Baihaqi, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.30004v1) | 📄 [PDF](https://arxiv.org/pdf/2603.30004v1)

**Summary:** This study examines the evolution of Intelligent and Secure Smart Hospital Ecosystems using a Scoping Review with Bibliometric Analysis (ScoRBA) to map research patterns, identify gaps, and derive policy implications. Analyzing 891 journal articles from Scopus (2006-2025) through co-occurrence analysis, network visualization, overlay analysis, and the Enhanced Strategic Diagram (ESD), the study applies the PAGER framework to link Patterns, Advances, Gaps, Research directions, and Evidence-based ...

---

### 27. Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective

**Authors:** Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29903v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29903v1)

**Summary:** Brain connectomics is still largely dominated by pairwise-based models, such as graphs, which cannot represent circulatory or higher-order functional interactions. In this paper, we propose a multimodal framework based on Topological Signal Processing (TSP) that models the brain as a higher-order topological domain and treats functional interactions as discrete vector fields. We integrate diffusion MRI and resting-state fMRI to learn subject-specific brain cell complexes, where statistically val...

---

### 28. Counterfactual Analysis of Brain Network Dynamics

**Authors:** Moo K. Chung, Luigi Maccotta, Aaron Struck

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29843v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29843v1)

**Summary:** Causal inference in brain networks has traditionally relied on regression-based models such as Granger causality, structural equation modeling, and dynamic causal modeling. While effective for identifying directed associations, these methods remain descriptive and acyclic, leaving open the fundamental question of intervention: what would the causal organization become if a pathway were disrupted or externally modulated? We introduce a unified framework for counterfactual causal analysis that mod...

---

### 29. Copy-Spread-Annihilate Dynamics in Degree-Assortative Networks

**Authors:** Yan Hao, Daniel J. Graham, Marc-Thorsten Hütt

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29833v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29833v1)

**Summary:** In many systems, communication proceeds by broadcasting rather than single source-target routing, but network structures that maximize signal lifetime are not well understood. Degree correlations are known to influence robustness and spreading, yet their effect on signal persistence has remained unclear. Here we introduce Copy-Spread-Annihilate dynamics, a minimal synchronous broadcasting model with annihilation. We show that signal lifetimes vary non-monotonically with assortativity and are max...

---

### 30. Covariant quantum error correction in a three-layer quantum brain model: computational analysis of layer-specific coherence dynamics

**Authors:** Hikaru Wakaura

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2604.08587v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08587v1)

**Summary:** Proposals for quantum coherence in neural computation lack quantitative frameworks for evaluating when -- and whether -- coherence provides computational benefits at biologically calibrated parameters. Here we construct such a framework by integrating a three-layer model parameterized by \textit{ab initio} spin Hamiltonian calculations of monoamine oxidase~A (MAO-A) with approximate covariant quantum error correction (CQEC) based on energy-conserving recursive swap tests. The three layers -- ${}...

---

### 31. Convergent Representations of Linguistic Constructions in Human and Artificial Neural Systems

**Authors:** Pegah Ramezani, Thomas Kinfe, Andreas Maier, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29617v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29617v1)

**Summary:** Understanding how the brain processes linguistic constructions is a central challenge in cognitive neuroscience and linguistics. Recent computational studies show that artificial neural language models spontaneously develop differentiated representations of Argument Structure Constructions (ASCs), generating predictions about when and how construction-level information emerges during processing. The present study tests these predictions in human neural activity using electroencephalography (EEG)...

---

### 32. Structural and dynamical strategies to prevent runaway excitation in reservoir computing

**Authors:** Claus Metzner, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29597v1)

**Summary:** Reservoirs, typically implemented as recurrent neural networks with fixed random connection weights, can be combined with a simple trained readout layer to perform a wide range of computational tasks. However, increasing the magnitude of reservoir connection weights to exploit nonlinear dynamics can cause the network to develop strong spontaneous activity that drives neurons into saturation, dramatically degrading performance. In this work, we investigate two distinct countermeasures against suc...

---

### 33. Predicting Neuromodulation Outcome for Parkinson's Disease with Generative Virtual Brain Model

**Authors:** Siyuan Du, Siyi Li, Shuwei Bai, et al.

**Published:** 2026-03-31

🔗 [Paper](http://arxiv.org/abs/2603.29176v1) | 📄 [PDF](https://arxiv.org/pdf/2603.29176v1)

**Summary:** Parkinson's disease (PD) affects over ten million people worldwide. Although temporal interference (TI) and deep brain stimulation (DBS) are promising therapies, inter-individual variability limits empirical treatment selection, increasing non-negligible surgical risk and cost. Previous explorations either resort to limited statistical biomarkers that are insufficient to characterize variability, or employ AI-driven methods which is prone to overfitting and opacity. We bridge this gap with a pre...

---

### 34. Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds

**Authors:** N Alex Cayco-Gajic, Arthur Pellegrino

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28764v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28764v1)

**Summary:** Similarity measures are widely used to interpret the representational geometries used by neural networks to solve tasks. Yet, because existing methods compare the extrinsic geometry of representations in state space, rather than their intrinsic geometry, they may fail to capture subtle yet crucial distinctions between fundamentally different neural network solutions. Here, we introduce metric similarity analysis (MSA), a novel method which leverages tools from Riemannian geometry to compare the ...

---

### 35. A Normative Theory of Decision Making from Multiple Stimuli: The Contextual Diffusion Decision Model

**Authors:** Michael Shvartsman, Vaibhav Srivastava, Narayanan Sundaram, et al.

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2603.28600v1)

**Summary:** The dynamics of simple two-alternative forced-choice (2AFC) decisions are well-modeled by a class of random walk models (e.g. Laming, 1968; Ratcliff, 1978; Usher & McClelland, 2001; Bogacz et al., 2006). However, in real-life, even simple decisions involve dynamically changing influence of additional information. In this work, we describe a computational theory of decision making from multiple sources of information, grounded in Bayesian inference and consistent with a simple neural network. Thi...

---

### 36. Allocentric Navigation Is Computationally Universal

**Authors:** Gualtiero Piccinini

**Published:** 2026-03-30

🔗 [Paper](http://arxiv.org/abs/2603.27926v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27926v1)

**Summary:** This report presents three proofs showing that idealized architectures capable of navigation guided by allocentric maps with landmark structure can be computationally universal. The navigation may occur either online (in the environment) or offline (in the animal's head). The first proof proceeds from a universal two-counter machine by encoding counters as the positions of two movable markers on orthogonal coordinate axes. The second proof directly simulates an ordinary one-tape Turing machine b...

---

### 37. The role of neuromorphic principles in the future of biomedicine and healthcare

**Authors:** Grace M. Hwang, Jessica D. Falcone, Joseph D. Monaco, et al.

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27716v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27716v1)

**Summary:** Neuromorphic engineering has matured over the past four decades and is currently experiencing explosive growth with the potential to transform biomedical engineering and neurotechnologies. Participants at the Neuromorphic Principles in Biomedicine and Healthcare (NPBH) Workshop (October 2024) -- representing a broad cross-section of the community, including early-career and established scholars, engineers, scientists, clinicians, industry, and funders -- convened to discuss the state of the fiel...

---

### 38. Energy Landscapes of Emotion: Quantifying Brain Network Stability During Happy and Sad Face Processing Using EEG-Based Hopfield Energy

**Authors:** Barry Djibrina, Jiajia Li

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27644v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27644v1)

**Summary:** Understanding how the human brain instantiates distinct emotional states is a key challenge in affective neuroscience. While network-based approaches have advanced emotion processing research,they remain largely descriptive,leaving the dynamical stability of emotional brain states unquantified.This study introduces a novel framework to quantify this stability by applying Hopfield network energy to empirically derived functional connectivity. High density EEG was recorded from 20 healthy adults d...

---

### 39. What does a system modify when it modifies itself?

**Authors:** Florentin Koch

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27611v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27611v1)

**Summary:** When a cognitive system modifies its own functioning, what exactly does it modify: a low-level rule, a control rule, or the norm that evaluates its own revisions? Cognitive science describes executive control, metacognition, and hierarchical learning with precision, but lacks a formal framework distinguishing these targets of transformation. Contemporary artificial intelligence likewise exhibits self-modification without common criteria for comparison with biological cognition.   We show that th...

---

### 40. From indicators to biology: the calibration problem in artificial consciousness

**Authors:** Florentin Koch

**Published:** 2026-03-29

🔗 [Paper](http://arxiv.org/abs/2603.27597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27597v1)

**Summary:** Recent work on artificial consciousness shifts evaluation from behaviour to internal architecture, deriving indicators from theories of consciousness and updating credences accordingly. This is progress beyond naive Turing-style tests. But the indicator-based programme remains epistemically under-calibrated: consciousness science is theoretically fragmented, indicators lack independent validation, and no ground truth of artificial phenomenality exists. Under these conditions, probabilistic consc...

---

### 41. Grounding Social Perception in Intuitive Physics

**Authors:** Lance Ying, Aydan Y. Huang, Aviv Netanyahu, et al.

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27410v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27410v1)

**Summary:** People infer rich social information from others' actions. These inferences are often constrained by the physical world: what agents can do, what obstacles permit, and how the physical actions of agents causally change an environment and other agents' mental states and behavior. We propose that such rich social perception is more than visual pattern matching, but rather a reasoning process grounded in an integration of intuitive psychology with intuitive physics. To test this hypothesis, we intr...

---

### 42. Information in a recurrent Retina-V1 network with realistic noise, feedback and nonlinearities

**Authors:** Javier Rodríguez, Raquel Giménez, Jesús Malo

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27347v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27347v1)

**Summary:** Quantitative estimation of information flow in early vision with psychophysically realistic networks is still an open issue. This is because, up to date, the necessary elements (general and plausible network, accurate noise, and reliable information measures) have not been put together. As a result, previous works made different approximations that limit the generality of their results.   This work combines the following elements for the first time: (1) General and plausible recurrent net: a cas...

---

### 43. Persistent Memory Through Triple-Loop Consolidation in a Non-Gradient Dissipative Cognitive Architecture

**Authors:** Jianwei Lou

**Published:** 2026-03-28

🔗 [Paper](http://arxiv.org/abs/2603.27188v1) | 📄 [PDF](https://arxiv.org/pdf/2603.27188v1)

**Summary:** Dissipative cognitive architectures maintain computation through continuous energy expenditure, where units that exhaust their energy are stochastically replaced with fresh random state. This creates a fundamental challenge: how can persistent, context-specific memory survive when all learnable state is periodically destroyed? Existing memory mechanisms -- including elastic weight consolidation, synaptic intelligence, and surprise-driven gating -- rely on gradient computation and are inapplicabl...

---

### 44. Revisiting claims of extracranial biophoton detection from the human brain

**Authors:** Vahid Salari, Vishnu Seshan, Rishabh Rishabh, et al.

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26630v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26630v1)

**Summary:** Ultraweak photon emission is the spontaneous emission of extremely low levels of light from a broad range of biological systems. Recent studies have reported that UPE measured extracranially can serve as a potential non-invasive biomarker of brain activity. Here, we show that this interpretation suffers from serious problems. First, when observed under properly dark conditions, the UPE from the head is much weaker than what is reported in certain papers on 'brain UPE' from human heads. Signals d...

---

### 45. Identifying Connectivity Distributions from Neural Dynamics Using Flows

**Authors:** Timothy Doyeon Kim, Ulises Pereira-Obilinovic, Yiliu Wang, et al.

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26506v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26506v1)

**Summary:** Connectivity structure shapes neural computation, but inferring this structure from population recordings is degenerate: multiple connectivity structures can generate identical dynamics. Recent work uses low-rank recurrent neural networks (lrRNNs) to infer low-dimensional latent dynamics and connectivity structure from observed activity, enabling a mechanistic interpretation of the dynamics. However, standard approaches for training lrRNNs can recover spurious structures irrelevant to the underl...

---

### 46. On the RAID dataset of perceptual responses: analysis and statistical causes

**Authors:** Paula Daudén-Oliver, David Agost-Beltran, Emilio Sansano-Sansano, et al.

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26267v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26267v1)

**Summary:** This work analyzes the RAID dataset to evaluate human responses to affine image distortions, including rotation, translation, scaling, and Gaussian noise. Using Mean Squared Error (MSE), the study establishes human detection thresholds for these distortions, enabling comparison across types. Statistical analysis with ANOVA and Tukey Kramer tests reveals that observers are significantly more sensitive to Gaussian noise, which consistently produced the lowest detection thresholds. Fourier analysis...

---

### 47. The Geometry of Forgetting

**Authors:** Sambartha Ray Barman, Andrey Starenky, Sophia Bodnar, et al.

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2604.06222v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06222v1)

**Summary:** Why do we forget? Why do we remember things that never happened? The conventional answer points to biological hardware. We propose a different one: geometry. Here we show that high-dimensional embedding spaces, subjected to noise, interference, and temporal degradation, reproduce quantitative signatures of human memory with no phenomenon-specific engineering. Power-law forgetting ($b = 0.460 \pm 0.183$, human $b \approx 0.5$) arises from interference among competing memories, not from decay. The...

---

### 48. Longitudinal Boundary Sharpness Coefficient Slopes Predict Time to Alzheimer's Disease Conversion in Mild Cognitive Impairment: A Survival Analysis Using the ADNI Cohort

**Authors:** Ishaan Cherukuri

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.26007v1) | 📄 [PDF](https://arxiv.org/pdf/2603.26007v1)

**Summary:** Predicting whether someone with mild cognitive impairment (MCI) will progress to Alzheimer's disease (AD) is crucial in the early stages of neurodegeneration. This uncertainty limits enrollment in clinical trials and delays urgent treatment. The Boundary Sharpness Coefficient (BSC) measures how well-defined the gray-white matter boundary looks on structural MRI. This study measures how BSC changes over time, namely, how fast the boundary degrades each year works much better than looking at a sin...

---

### 49. Passivity-Based Control of Electrographic Seizures in a Neural Mass Model of Epilepsy

**Authors:** Gagan Acharya, Erfan Nozari

**Published:** 2026-03-27

🔗 [Paper](http://arxiv.org/abs/2603.25991v1) | 📄 [PDF](https://arxiv.org/pdf/2603.25991v1)

**Summary:** Recent advances in neurotechnologies and decades of scientific and clinical research have made closed-loop electrical neuromodulation one of the most promising avenues for the treatment of drug-resistant epilepsy (DRE), a condition that affects over 15 million individuals globally. Yet, with the existing clinical state of the art, only 18% of patients with DRE who undergo closed-loop neuromodulation become seizure-free. In a recent study, we demonstrated that a simple proportional feedback polic...

---

### 50. Compiling molecular ultrastructure into neural dynamics

**Authors:** Konrad P. Kording, Anton Arkhipov, Davy Deng, et al.

**Published:** 2026-03-26

🔗 [Paper](http://arxiv.org/abs/2603.25713v1) | 📄 [PDF](https://arxiv.org/pdf/2603.25713v1)

**Summary:** High-resolution brain imaging can now capture not just synapse locations but their molecular composition, with the cost of such mapping falling exponentially. Yet such ultrastructural data has so far told us little about local neuronal physiology - specifically, the parameters (e.g., synaptic efficacies, local conductances) that govern neural dynamics. We propose to translate molecularly annotated ultrastructure into physiology, introducing the concept of an ultrastructure-to-dynamics compiler: ...

---

## stat.ML

**50 papers**

### 1. Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer

**Authors:** Yannis Montreuil, Axel Carlier, Lai Xing Ng, et al.

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09414v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09414v1)

**Summary:** Learning-to-Defer routes each input to the expert that minimizes expected cost, but it assumes that the information available to every expert is fixed at decision time. Many modern systems violate this assumption: after selecting an expert, one may also choose what additional information that expert should receive, such as retrieved documents, tool outputs, or escalation context. We study this problem and call it Learning-to-Defer with advice. We show that a broad family of natural separated sur...

---

### 2. Sharp description of local minima in the loss landscape of high-dimensional two-layer ReLU neural networks

**Authors:** Jie Huang, Bruno Loureiro, Stefano Sarao Mannelli

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09412v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09412v1)

**Summary:** We study the population loss landscape of two-layer ReLU networks of the form $\sum_{k=1}^K \mathrm{ReLU}(w_k^\top x)$ in a realisable teacher-student setting with Gaussian covariates. We show that local minima admit an exact low-dimensional representation in terms of summary statistics, yielding a sharp and interpretable characterisation of the landscape. We further establish a direct link with one-pass SGD: local minima correspond to attractive fixed points of the dynamics in summary statistic...

---

### 3. Data-Efficient Non-Gaussian Semi-Nonparametric Density Estimation for Nonlinear Dynamical Systems

**Authors:** Aaron R. Liao, Kenshiro Oguri, Michele D. Carpenter

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09375v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09375v1)

**Summary:** Accurate representation of non-Gaussian distributions of quantities of interest in nonlinear dynamical systems is critical for estimation, control, and decision-making, but can be challenging when forward propagations are expensive to carry out. This paper presents an approach for estimating probability density functions of states evolving under nonlinear dynamics using Seminonparametric (SNP), or Gallant-Nychka, densities. SNP densities employ a probabilists' Hermite polynomial basis to model n...

---

### 4. Iterative Identification Closure: Amplifying Causal Identifiability in Linear SEMs

**Authors:** Ziyi Ding, Xiao-Ping Zhang

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09309v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09309v1)

**Summary:** The Half-Trek Criterion (HTC) is the primary graphical tool for determining generic identifiability of causal effect coefficients in linear structural equation models (SEMs) with latent confounders. However, HTC is inherently node-wise: it simultaneously resolves all incoming edges of a node, leaving a gap of "inconclusive" causal effects (15-23% in moderate graphs). We introduce Iterative Identification Closure (IIC), a general framework that decouples causal identification into two phases: (1)...

---

### 5. High-dimensional Adaptive MCMC with Reduced Computational Complexity

**Authors:** Max Hird, Samuel Livingstone

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09286v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09286v1)

**Summary:** We propose an adaptive MCMC method that learns a linear preconditioner which is dense in its off-diagonal elements but sparse in its parametrisation. Due to this sparsity, we achieve a per-iteration computational complexity of $O(m^2d)$ for a user-determined parameter $m$, compared with the $O(d^2)$ complexity of existing adaptive strategies that can capture correlation information from the target. Diagonal preconditioning has an $O(d)$ per-iteration complexity, but is known to fail in the case ...

---

### 6. A Predictive View on Streaming Hidden Markov Models

**Authors:** Gerardo Duran-Martin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09208v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09208v1)

**Summary:** We develop a predictive-first optimisation framework for streaming hidden Markov models. Unlike classical approaches that prioritise full posterior recovery under a fully specified generative model, we assume access to regime-specific predictive models whose parameters are learned online while maintaining a fixed transition prior over regimes. Our objective is to sequentially identify latent regimes while maintaining accurate step-ahead predictive distributions. Because the number of possible re...

---

### 7. Generalization and Scaling Laws for Mixture-of-Experts Transformers

**Authors:** Mansour Zoubeirou a Mayaki

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09175v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09175v1)

**Summary:** We develop a theory of generalization and scaling for Mixture-of-Experts (MoE) Transformers that cleanly separates \emph{active} per-input capacity from routing combinatorics. By conditioning on fixed routing patterns and union-bounding across them, we derive a sup-norm covering-number bound whose metric entropy scales with the active parameter budget and incurs a MoE-specific routing overhead. Combined with a standard ERM analysis for squared loss, this yields a generalization bound under a $d$...

---

### 8. Identifying Causal Effects Using a Single Proxy Variable

**Authors:** Silvan Vollmer, Niklas Pfister, Sebastian Weichwald

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09135v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09135v1)

**Summary:** Unobserved confounding is a key challenge when estimating causal effects from a treatment on an outcome in scientific applications. In this work, we assume that we observe a single, potentially multi-dimensional proxy variable of the unobserved confounder and that we know the mechanism that generates the proxy from the confounder. Under a completeness assumption on this mechanism, which we call Single Proxy Identifiability of Causal Effects or simply SPICE, we prove that causal effects are ident...

---

### 9. U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster

**Authors:** Salva Rühling Cachay, Duncan Watson-Parris, Rose Yu

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09041v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09041v1)

**Summary:** AI-based weather forecasting now rivals traditional physics-based ensembles, but state-of-the-art (SOTA) models rely on specialized architectures and massive computational budgets, creating a high barrier to entry. We demonstrate that such complexity is unnecessary for frontier performance. We introduce U-Cast, a probabilistic forecaster built on a standard U-Net backbone trained with a simple recipe: deterministic pre-training on Mean Absolute Error followed by short probabilistic fine-tuning o...

---

### 10. Online Quantile Regression for Nonparametric Additive Models

**Authors:** Haoran Zhan

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08969v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08969v1)

**Summary:** This paper introduces a projected functional gradient descent algorithm (P-FGD) for training nonparametric additive quantile regression models in online settings. This algorithm extends the functional stochastic gradient descent framework to the pinball loss. An advantage of P-FGD is that it does not need to store historical data while maintaining $O(J_t\ln J_t)$ computational complexity per step where $J_t$ denotes the number of basis functions. Besides, we only need $O(J_t)$ computational time...

---

### 11. A novel hybrid approach for positive-valued DAG learning

**Authors:** Yao Zhao

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08935v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08935v1)

**Summary:** Causal discovery from observational data remains a fundamental challenge in machine learning and statistics, particularly when variables represent inherently positive quantities such as gene expression levels, asset prices, company revenues, or population counts, which often follow multiplicative rather than additive dynamics. We propose the Hybrid Moment-Ratio Scoring (H-MRS) algorithm, a novel method for learning directed acyclic graphs (DAGs) from positive-valued data by combining moment-base...

---

### 12. Hierarchical Kernel Transformer: Multi-Scale Attention with an Information-Theoretic Approximation Analysis

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.08829v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08829v1)

**Summary:** The Hierarchical Kernel Transformer (HKT) is a multi-scale attention mechanism that processes sequences at L resolution levels via trainable causal downsampling, combining level-specific score matrices through learned convex weights. The total computational cost is bounded by 4/3 times that of standard attention, reaching 1.3125x for L = 3. Four theoretical results are established. (i) The hierarchical score matrix defines a positive semidefinite kernel under a sufficient condition on the symmet...

---

### 13. Policy-Aware Design of Large-Scale Factorial Experiments

**Authors:** Xin Wen, Xi Chen, Will Wei Sun, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08804v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08804v1)

**Summary:** Digital firms routinely run many online experiments on shared user populations. When product decisions are compositional, such as combinations of interface elements, flows, messages, or incentives, the number of feasible interventions grows combinatorially, while available traffic remains limited. Overlapping experiments can therefore generate interaction effects that are poorly handled by decentralized A/B testing. We study how to design large-scale factorial experiments when the objective is n...

---

### 14. Accurate and Reliable Uncertainty Estimates for Deterministic Predictions Extensions to Under and Overpredictions

**Authors:** Rileigh Bandy, Enrico Camporeale, Andong Hu, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08755v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08755v1)

**Summary:** Computational models support high-stakes decisions across engineering and science, and practitioners increasingly seek probabilistic predictions to quantify uncertainty in such models. Existing approaches generate predictions either by sampling input parameter distributions or by augmenting deterministic outputs with uncertainty representations, including distribution-free and distributional methods. However, sampling-based methods are often computationally prohibitive for real-time applications...

---

### 15. Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts

**Authors:** Jiayuan Ye, Vitaly Feldman, Kunal Talwar

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08519v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08519v1)

**Summary:** Large language models (LLMs) can struggle to memorize factual knowledge in their parameters, often leading to hallucinations and poor performance on knowledge-intensive tasks. In this paper, we formalize fact memorization from an information-theoretic perspective and study how training data distributions affect fact accuracy. We show that fact accuracy is suboptimal (below the capacity limit) whenever the amount of information contained in the training data facts exceeds model capacity. This is ...

---

### 16. Differentially Private Language Generation and Identification in the Limit

**Authors:** Anay Mehrotra, Grigoris Velegkas, Xifan Yu, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08504v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08504v1)

**Summary:** We initiate the study of language generation in the limit, a model recently introduced by Kleinberg and Mullainathan [KM24], under the constraint of differential privacy. We consider the continual release model, where a generator must eventually output a stream of valid strings while protecting the privacy of the entire input sequence. Our first main result is that for countable collections of languages, privacy comes at no qualitative cost: we provide an $\varepsilon$-differentially-private alg...

---

### 17. Synthetic Data for any Differentiable Target

**Authors:** Tristan Thrush, Sung Min Park, Herman Brunborg, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08423v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08423v1)

**Summary:** What are the limits of controlling language models via synthetic training data? We develop a reinforcement learning (RL) primitive, the Dataset Policy Gradient (DPG), which can precisely optimize synthetic data generators to produce a dataset of targeted examples. When used for supervised fine-tuning (SFT) of a target model, these examples cause the target model to do well on a differentiable metric of our choice. Our approach achieves this by taking exact data attribution via higher-order gradi...

---

### 18. Adversarial Label Invariant Graph Data Augmentations for Out-of-Distribution Generalization

**Authors:** Simon Zhang, Ryan P. DeMilt, Kun Jin, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08404v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08404v1)

**Summary:** Out-of-distribution (OoD) generalization occurs when representation learning encounters a distribution shift. This occurs frequently in practice when training and testing data come from different environments. Covariate shift is a type of distribution shift that occurs only in the input data, while the concept distribution stays invariant. We propose RIA - Regularization for Invariance with Adversarial training, a new method for OoD generalization under convariate shift. Motivated by an analogy ...

---

### 19. Spectral-Transport Stability and Benign Overfitting in Interpolating Learning

**Authors:** Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08625v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08625v1)

**Summary:** We develop a theoretical framework for generalization in the interpolating regime of statistical learning. The central question is why highly overparameterized estimators can attain zero empirical risk while still achieving nontrivial predictive accuracy, and how to characterize the boundary between benign and destructive overfitting. We introduce a spectral-transport stability framework in which excess risk is controlled jointly by the spectral geometry of the data distribution, the sensitivity...

---

### 20. A Direct Approach for Handling Contextual Bandits with Latent State Dynamics

**Authors:** Zhen Li, Gilles Stoltz

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08149v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08149v1)

**Summary:** We revisit the finite-armed linear bandit model by Nelson et al. (2022), where contexts and rewards are governed by a finite hidden Markov chain. Nelson et al. (2022) approach this model by a reduction to linear contextual bandits; but to do so, they actually introduce a simplification in which rewards are linear functions of the posterior probabilities over the hidden states given the observed contexts, rather than functions of the hidden states themselves. Their analysis (but not their algorit...

---

### 21. A unifying view of contrastive learning, importance sampling, and bridge sampling for energy-based models

**Authors:** Luca Martino

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08116v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08116v1)

**Summary:** In the last decades, energy-based models (EBMs) have become an important class of probabilistic models in which a component of the likelihood is intractable and therefore cannot be evaluated explicitly. Consequently, parameter estimation in EBMs is challenging for conventional inference methods. In this work, we provide a unified framework that connects noise contrastive estimation (NCE), reverse logistic regression (RLR), multiple importance sampling (MIS), and bridge sampling within the contex...

---

### 22. The ecosystem of machine learning competitions: Platforms, participants, and their impact on AI development

**Authors:** Ioannis Nasios

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08001v1)

**Summary:** Machine learning competitions (MLCs) play a pivotal role in advancing artificial intelligence (AI) by fostering innovation, skill development, and practical problem-solving. This study provides a comprehensive analysis of major competition platforms such as Kaggle and Zindi, examining their workflows, evaluation methodologies, and reward structures. It further assesses competition quality, participant expertise, and global reach, with particular attention to demographic trends among top-performi...

---

### 23. Unified Precision-Guaranteed Stopping Rules for Contextual Learning

**Authors:** Mingrui Ding, Qiuhong Zhao, Siyang Gao, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07913v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07913v1)

**Summary:** Contextual learning seeks to learn a decision policy that maps an individual's characteristics to an action through data collection. In operations management, such data may come from various sources, and a central question is when data collection can stop while still guaranteeing that the learned policy is sufficiently accurate. We study this question under two precision criteria: a context-wise criterion and an aggregate policy-value criterion. We develop unified stopping rules for contextual l...

---

### 24. Intensity Dot Product Graphs

**Authors:** Giulio Valentino Dalla Riva, Matteo Dalla Riva

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07810v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07810v1)

**Summary:** Latent-position random graph models usually treat the node set as fixed once the sample size is chosen, while graphon-based and random-measure constructions allow more randomness at the cost of weaker geometric interpretability. We introduce \emph{Intensity Dot Product Graphs} (IDPGs), which extend Random Dot Product Graphs by replacing a fixed collection of latent positions with a Poisson point process on a Euclidean latent space. This yields a model with random node populations, RDPG-style dot...

---

### 25. Order-Optimal Sequential 1-Bit Mean Estimation in General Tail Regimes

**Authors:** Ivan Lau, Jonathan Scarlett

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07796v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07796v1)

**Summary:** In this paper, we study the problem of mean estimation under strict 1-bit communication constraints. We propose a novel adaptive mean estimator based solely on randomized threshold queries, where each 1-bit outcome indicates whether a given sample exceeds a sequentially chosen threshold. Our estimator is $(ε, δ)$-PAC for any distribution with a bounded mean $μ\in [-λ, λ]$ and a bounded $k$-th central moment $\mathbb{E}[|X-μ|^k] \le σ^k$ for any fixed $k > 1$. Crucially, our sample complexity is ...

---

### 26. Sparse $ε$ insensitive zone bounded asymmetric elastic net support vector machines for pattern classification

**Authors:** Haiyan Du, Hu Yang

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07748v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07748v1)

**Summary:** Existing support vector machines(SVM) models are sensitive to noise and lack sparsity, which limits their performance. To address these issues, we combine the elastic net loss with a robust loss framework to construct a sparse $\varepsilon$-insensitive bounded asymmetric elastic net loss, and integrate it with SVM to build $\varepsilon$ Insensitive Zone Bounded Asymmetric Elastic Net Loss-based SVM($\varepsilon$-BAEN-SVM). $\varepsilon$-BAEN-SVM is both sparse and robust. Sparsity is proven by s...

---

### 27. The Condition-Number Principle for Prototype Clustering

**Authors:** Romano Li, Jianfei Cao

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07744v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07744v1)

**Summary:** We develop a geometric framework that links objective accuracy to structural recovery in prototype-based clustering. The analysis is algorithm-agnostic and applies to a broad class of admissible loss functions. We define a clustering condition number that compares within-cluster scale to the minimum loss increase required to move a point across a cluster boundary. When this quantity is small, any solution with a small suboptimality gap must also have a small misclassification error relative to a...

---

### 28. On the Unique Recovery of Transport Maps and Vector Fields from Finite Measure-Valued Data

**Authors:** Jonah Botvinick-Greenhouse, Yunan Yang

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07671v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07671v1)

**Summary:** We establish guarantees for the unique recovery of vector fields and transport maps from finite measure-valued data, yielding new insights into generative models, data-driven dynamical systems, and PDE inverse problems. In particular, we provide general conditions under which a diffeomorphism can be uniquely identified from its pushforward action on finitely many densities, i.e., when the data $\{(ρ_j,f_\#ρ_j)\}_{j=1}^m$ uniquely determines $f$. As a corollary, we introduce a new metric which co...

---

### 29. Variational Approximated Restricted Maximum Likelihood Estimation for Spatial Data

**Authors:** Debjoy Thakur

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07635v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07635v1)

**Summary:** This research considers a scalable inference for spatial data modeled through Gaussian intrinsic conditional autoregressive (ICAR) structures. The classical estimation method, restricted maximum likelihood (REML), requires repeated inversion and factorization of large, sparse precision matrices, which makes this computation costly. To sort this problem out, we propose a variational restricted maximum likelihood (VREML) framework that approximates the intractable marginal likelihood using a Gauss...

---

### 30. From Ground Truth to Measurement: A Statistical Framework for Human Labeling

**Authors:** Robert Chew, Stephanie Eckman, Christoph Kern, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07591v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07591v1)

**Summary:** Supervised machine learning assumes that labeled data provide accurate measurements of the concepts models are meant to learn. Yet in practice, human labeling introduces systematic variation arising from ambiguous items, divergent interpretations, and simple mistakes. Machine learning research commonly treats all disagreement as noise, which obscures these distinctions and limits our understanding of what models actually learn. This paper reframes annotation as a measurement process and introduc...

---

### 31. Virtual Dummies: Enabling Scalable FDR-Controlled Variable Selection via Sequential Sampling of Null Features

**Authors:** Taulant Koka, Jasin Machkour, Daniel P. Palomar, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07464v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07464v1)

**Summary:** High-dimensional variable selection, particularly in genomics, requires error-controlling procedures that scale to millions of predictors. The Terminating-Random Experiments (T-Rex) selector achieves false discovery rate (FDR) control by aggregating results of early terminated random experiments, each combining original predictors with i.i.d. synthetic null variables (dummies). At biobank scales, however, explicit dummy augmentation requires terabytes of memory. We demonstrate that this bottlene...

---

### 32. Conformal Prediction with Time-Series Data via Sequential Conformalized Density Regions

**Authors:** M. Sampson, K. S. Chan

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07325v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07325v1)

**Summary:** We propose a new conformal prediction method for time-series data with a guaranteed asymptotic conditional coverage rate, Sequential Conformalized Density Regions (SCDR), which is flexible enough to produce both prediction intervals and disconnected prediction sets, signifying the emergence of bifurcations. Our approach uses existing estimated conditional highest density predictive regions to form initial predictive regions. We then use a quantile random forest conformal adjustment to provide gu...

---

### 33. Gaussian Approximation for Asynchronous Q-learning

**Authors:** Artemy Rubtsov, Sergey Samsonov, Vladimir Ulyanov, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07323v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07323v1)

**Summary:** In this paper, we derive rates of convergence in the high-dimensional central limit theorem for Polyak-Ruppert averaged iterates generated by the asynchronous Q-learning algorithm with a polynomial stepsize $k^{-ω},\, ω\in (1/2, 1]$. Assuming that the sequence of state-action-next-state triples $(s_k, a_k, s_{k+1})_{k \geq 0}$ forms a uniformly geometrically ergodic Markov chain, we establish a rate of order up to $n^{-1/6} \log^{4} (nS A)$ over the class of hyper-rectangles, where $n$ is the nu...

---

### 34. The Theory and Practice of Highly Scalable Gaussian Process Regression with Nearest Neighbours

**Authors:** Robert Allison, Tomasz Maciazek, Anthony Stephenson

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07267v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07267v1)

**Summary:** Gaussian process ($GP$) regression is a widely used non-parametric modeling tool, but its cubic complexity in the training size limits its use on massive data sets. A practical remedy is to predict using only the nearest neighbours of each test point, as in Nearest Neighbour Gaussian Process ($NNGP$) regression for geospatial problems and the related scalable $GPnn$ method for more general machine-learning applications. Despite their strong empirical performance, the large-$n$ theory of $NNGP/GP...

---

### 35. Amortized Filtering and Smoothing with Conditional Normalizing Flows

**Authors:** Tiangang Cui, Xiaodong Feng, Chenlong Pei, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07169v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07169v1)

**Summary:** Bayesian filtering and smoothing for high-dimensional nonlinear dynamical systems are fundamental yet challenging problems in many areas of science and engineering. In this work, we propose AFSF, a unified amortized framework for filtering and smoothing with conditional normalizing flows. The core idea is to encode each observation history into a fixed-dimensional summary statistic and use this shared representation to learn both a forward flow for the filtering distribution and a backward flow ...

---

### 36. SBBTS: A Unified Schrödinger-Bass Framework for Synthetic Financial Time Series

**Authors:** Alexandre Alouadi, Grégoire Loeper, Célian Marsala, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07159v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07159v1)

**Summary:** We study the problem of generating synthetic time series that reproduce both marginal distributions and temporal dynamics, a central challenge in financial machine learning. Existing approaches typically fail to jointly model drift and stochastic volatility, as diffusion-based methods fix the volatility while martingale transport models ignore drift. We introduce the Schrödinger-Bass Bridge for Time Series (SBBTS), a unified framework that extends the Schrödinger-Bass formulation to multi-step t...

---

### 37. Lumbermark: Resistant Clustering by Chopping Up Mutual Reachability Minimum Spanning Trees

**Authors:** Marek Gagolewski

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07143v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07143v1)

**Summary:** We introduce Lumbermark, a robust divisive clustering algorithm capable of detecting clusters of varying sizes, densities, and shapes. Lumbermark iteratively chops off large limbs connected by protruding segments of a dataset's mutual reachability minimum spanning tree. The use of mutual reachability distances smoothens the data distribution and decreases the influence of low-density objects, such as noise points between clusters or outliers at their peripheries. The algorithm can be viewed as a...

---

### 38. Are Stochastic Multi-objective Bandits Harder than Single-objective Bandits?

**Authors:** Changkun Guan, Mengfan Xu

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07096v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07096v1)

**Summary:** Multi-objective bandits have attracted increasing attention because of their broad applicability and mathematical elegance, where the reward of each arm is a multi-dimensional vector rather than a scalar. This naturally introduces Pareto order relations and Pareto regret. A long-standing question in this area is whether performance is fundamentally harder to optimize because of this added complexity. A recent surprising result shows that, in the adversarial setting, Pareto regret is no larger th...

---

### 39. Time Series Gaussian Chain Graph Models

**Authors:** Qin Fang, Xinghao Qiao, Zihan Wang

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07018v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07018v1)

**Summary:** Time series graphical models have recently received considerable attention for characterizing (conditional) dependence structures in multivariate time series. In many applications, the multivariate series exhibit variable-partitioned blockwise dependence, with distinct patterns within and across blocks. In this paper, we introduce a new class of time series Gaussian chain graph models that represent contemporaneous and lagged causal relations via directed edges across blocks, while capturing wit...

---

### 40. Score Shocks: The Burgers Equation Structure of Diffusion Generative Models

**Authors:** Krisanu Sarkar

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07404v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07404v1)

**Summary:** We analyze the score field of a diffusion generative model through a Burgers-type evolution law. For VE diffusion, the heat-evolved data density implies that the score obeys viscous Burgers in one dimension and the corresponding irrotational vector Burgers system in $\R^d$, giving a PDE view of \emph{speciation transitions} as the sharpening of inter-mode interfaces. For any binary decomposition of the noised density into two positive heat solutions, the score separates into a smooth background ...

---

### 41. A Data-Informed Variational Clustering Framework for Noisy High-Dimensional Data

**Authors:** Wan Ping Chen

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06864v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06864v1)

**Summary:** Clustering in high-dimensional settings with severe feature noise remains challenging, especially when only a small subset of dimensions is informative and the final number of clusters is not specified in advance. In such regimes, partition recovery, feature relevance learning, and structural adaptation are tightly coupled, and standard likelihood-based methods can become unstable or overly sensitive to noisy dimensions. We propose DIVI, a data-informed variational clustering framework that comb...

---

### 42. Bi-Lipschitz Autoencoder With Injectivity Guarantee

**Authors:** Qipeng Zhan, Zhuoping Zhou, Zexuan Wang, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06701v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06701v1)

**Summary:** Autoencoders are widely used for dimensionality reduction, based on the assumption that high-dimensional data lies on low-dimensional manifolds. Regularized autoencoders aim to preserve manifold geometry during dimensionality reduction, but existing approaches often suffer from non-injective mappings and overly rigid constraints that limit their effectiveness and robustness. In this work, we identify encoder non-injectivity as a core bottleneck that leads to poor convergence and distorted latent...

---

### 43. Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective

**Authors:** Qipeng Zhan, Zhuoping Zhou, Li Shen

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06689v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06689v1)

**Summary:** Accurate classification requires not only high predictive accuracy but also well-calibrated confidence estimates. Yet, modern deep neural networks (DNNs) are often overconfident, primarily due to overfitting on the negative log-likelihood (NLL). While focal loss variants alleviate this issue, they typically reduce accuracy, revealing a persistent trade-off between calibration and predictive performance. Motivated by the complementary strengths of generative and discriminative classifiers, we pro...

---

### 44. The Theorems of Dr. David Blackwell and Their Contributions to Artificial Intelligence

**Authors:** Napoleon Paxton

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06621v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06621v1)

**Summary:** Dr. David Blackwell was a mathematician and statistician of the first rank, whose contributions to statistical theory, game theory, and decision theory predated many of the algorithmic breakthroughs that define modern artificial intelligence. This survey examines three of his most consequential theoretical results the Rao Blackwell theorem, the Blackwell Approachability theorem, and the Blackwell Informativeness theorem (comparison of experiments) and traces their direct influence on contemporar...

---

### 45. A Generalized Sinkhorn Algorithm for Mean-Field Schrödinger Bridge

**Authors:** Asmaa Eldesoukey, Yongxin Chen, Abhishek Halder

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.06531v2) | 📄 [PDF](https://arxiv.org/pdf/2604.06531v2)

**Summary:** The mean-field Schrödinger bridge (MFSB) problem concerns designing a minimum-effort controller that guides a diffusion process with nonlocal interaction to reach a given distribution from another by a fixed deadline. Unlike the standard Schrödinger bridge, the dynamical constraint for MFSB is the mean-field limit of a population of interacting agents with controls. It serves as a natural model for large-scale multi-agent systems. The MFSB is computationally challenging because the nonlocal inte...

---

### 46. Equivalence Testing Under Privacy Constraints

**Authors:** Savita Pareek, Luca Insolia, Roberto Molinari, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06499v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06499v1)

**Summary:** Protecting individual privacy is essential across research domains, from socio-economic surveys to big-tech user data. This need is particularly acute in healthcare, where analyses often involve sensitive patient information. A typical example is comparing treatment efficacy across hospitals or ensuring consistency in diagnostic laboratory calibrations, both requiring privacy-preserving statistical procedures. However, standard equivalence testing procedures for differences in proportions or mea...

---

### 47. Optimal Rates for Pure {\varepsilon}-Differentially Private Stochastic Convex Optimization with Heavy Tails

**Authors:** Andrew Lowy

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06492v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06492v1)

**Summary:** We study stochastic convex optimization (SCO) with heavy-tailed gradients under pure epsilon-differential privacy (DP). Instead of assuming a bound on the worst-case Lipschitz parameter of the loss, we assume only a bounded k-th moment. This assumption allows for unbounded, heavy-tailed stochastic gradient distributions, and can yield sharper excess risk bounds. The minimax optimal rate for approximate (epsilon, delta)-DP SCO is known in this setting, but the pure epsilon-DP case has remained op...

---

### 48. Conformal Margin Risk Minimization: An Envelope Framework for Robust Learning under Label Noise

**Authors:** Yuanjie Shi, Peihong Li, Zijian Zhang, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06468v2) | 📄 [PDF](https://arxiv.org/pdf/2604.06468v2)

**Summary:** Most methods for learning with noisy labels require privileged knowledge such as noise transition matrices, clean subsets or pretrained feature extractors, resources typically unavailable when robustness is most needed. We propose Conformal Margin Risk Minimization (CMRM), a plug-and-play envelope framework that improves any classification loss under label noise by adding a single quantile-calibrated regularization term, with no privileged knowledge or training pipeline modification. CMRM measur...

---

### 49. Weighted Bayesian Conformal Prediction

**Authors:** Xiayin Lou, Peng Luo

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06464v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06464v1)

**Summary:** Conformal prediction provides distribution-free prediction intervals with finite-sample coverage guarantees, and recent work by Snell \& Griffiths reframes it as Bayesian Quadrature (BQ-CP), yielding powerful data-conditional guarantees via Dirichlet posteriors over thresholds. However, BQ-CP fundamentally requires the i.i.d. assumption -- a limitation the authors themselves identify. Meanwhile, weighted conformal prediction handles distribution shift via importance weights but remains frequenti...

---

### 50. Bridging Theory and Practice in Crafting Robust Spiking Reservoirs

**Authors:** Ruggero Freddi, Nicolas Seseri, Diana Nigrisoli, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06395v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06395v1)

**Summary:** Spiking reservoir computing provides an energy-efficient approach to temporal processing, but reliably tuning reservoirs to operate at the edge-of-chaos is challenging due to experimental uncertainty. This work bridges abstract notions of criticality and practical stability by introducing and exploiting the robustness interval, an operational measure of the hyperparameter range over which a reservoir maintains performance above task-dependent thresholds. Through systematic evaluations of Leaky I...

---

