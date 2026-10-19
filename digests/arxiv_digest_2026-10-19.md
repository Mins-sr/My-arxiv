# arXiv Daily Digest - 2026-10-19

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Rethinking the design space of Vanilla Pixel Diffusion Transformers

**Authors:** Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23854v1)

**Summary:** Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\boldsymbol{u}$-prediction) with clean image prediction ($\boldsymbol{x_0}$-prediction). In this work, we revisit this choice and introduce MFlow, an adaptive parameterization that learns...

---

### 2. Behavioral Couplings: From Formation to Behavioral Emergence in Language Models

**Authors:** Dongyoon Hahm, Woogyeol Jin, Dennis Wei, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23847v1)

**Summary:** Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is...

---

### 3. AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery

**Authors:** Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23845v1)

**Summary:** Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 publ...

---

### 4. Self-Building Labs

**Authors:** Jiaru Bai, Yuchi Zhao, Han Hao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23826v1)

**Summary:** Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setu...

---

### 5. Beyond SAEs: Consistent Concept Discovery with Sparse Coding

**Authors:** Jinho Choi, Hyesu Lim, Jaegul Choo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23801v1)

**Summary:** Sparse autoencoders (SAEs) explain foundation model representations by decomposing activations into sparse combinations of learned dictionary atoms. However, the learned dictionaries can vary across training runs, limiting the reliability and reproducibility of SAE-based analyses. We propose Consistent Sparse Dictionary Learning (ConSDL), which replaces the standard linear encoder with per-sample sparse coding. This is motivated by our synthetic analysis showing that coefficients from a single l...

---

### 6. FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper

**Authors:** Wei Wang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23796v1)

**Summary:** Transformer prefill reuses weights across tokens and is dominated by matrix multiplication and activation data movement; single-token decode has limited reuse and is dominated by weight and KV-cache reads. We present FUTRANSFORMER, a CUDA implementation of a Llama-style Transformer block for NVIDIA Hopper GPUs. It applies CODA's GEMM-plus-epilogue approach to inference, adding direct KV-cache placement, folding the fixed RMSNorm gain into weights, writing FP8 output directly with delayed scaling...

---

### 7. DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery

**Authors:** Yuxing Chen, Zhisheng Zhang, Cheng Tang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23791v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23791v1)

**Summary:** Computational drug discovery requires agents to compose scientific operations and adapt to changing evidence and constraints. Here we introduce DrugHarness, an evolvable agent harness coupling composable scientific execution with conditional skill induction. Its environment integrates over 80 scientific operations, biomedical resources and task-specific code, preserving associations among candidates, results and artifacts. From execution trajectories and outcome feedback, DrugHarness induces act...

---

### 8. Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability

**Authors:** Qingshi Wang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23722v1)

**Summary:** Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This pa...

---

### 9. Neural Expansion: A Unified Mechanism for How Deep Neural Networks Generalize

**Authors:** Chashi Mahiul Islam, Samuel Jacob Chacko, Mao Nishino, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23716v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23716v1)

**Summary:** Deep neural networks demonstrate remarkable generalization despite being highly over-parameterized, challenging traditional statistical learning theories. While several theoretical paradigms such as margin-based bounds, PAC-Bayesian analyses, and neural tangent kernels provide global explanations, they often lack mechanistic insight into how generalization emerges from training dynamics. We introduce Neural Expansion, a unified geometric framework that characterizes generalization through the ex...

---

### 10. GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search

**Authors:** Hyunseo Kim, Suil Choe, Sukkyoung So, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23709v1)

**Summary:** Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic fra...

---

### 11. On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management

**Authors:** Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23673v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23673v1)

**Summary:** Multi-criteria models for healthcare operations need weights that express how stakeholders trade off patient waiting time, provider workload, and operating cost, but these weights are difficult to quantify. Teams of large language model (LLM) agents, each prompted to represent a stakeholder, have been used to supply them. We propose a framework for assessing the reliability of LLM-generated preferences as inputs to multi-objective optimization and quantifying how their uncertainty affects decisi...

---

### 12. OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning

**Authors:** Lewen Yan, Yanxu Zhu, Jie Zhang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23670v1)

**Summary:** Chain-of-Thought (CoT) monitoring offers actionable evidence for oversight AI systems, with the potential to enable early detection and intervention. However, existing approaches are focused on specific tasks, whereas the regulation of AI, particularly reasoning models, requires monitoring a broader range of tasks. We introduce Factor for CoT monitoring, a strategy that supports customizing monitoring requirements in the prompt, which enables a single monitor to cover different tasks by relying ...

---

### 13. TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models

**Authors:** Yiqu Yang, Qiaoyuan Zheng, Yang Tian, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23668v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23668v1)

**Summary:** Typed decision models often return more than a selected category. They also expose probabilities for each candidate and, sometimes, a separate confidence score. These fields support downstream decisions but may reveal information beyond a recipient's authorization. We introduce TUPLE-Bench (Typed decision models' Utility and Privacy Leakage Evaluation Benchmark), a benchmark of paired synthetic cases in which recipients may learn a coarse operational category but not its fine-grained cause. Acro...

---

### 14. PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation to User State

**Authors:** Peña Arroyo Gallego, Mauro Ruiz Moreno, Alejandro Acien, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23625v1)

**Summary:** Presence-aware intelligence is the capacity of an AI system's intelligence layer to adapt appropriately to the functional state of the person it serves (here readiness, flow, and stability) while preserving task quality and safety. We introduce PresenceBench, an instrument for measuring it. PresenceBench evaluates how the intelligence layer uses a supplied state, not how that state is sensed, and breaks the capability into measurable properties. Two are tested here. Receptivity: does the model t...

---

### 15. GEMS: Molecular Structure Elucidation as Learned Search over Isomer Graphs

**Authors:** Utku Umur Acikalin, Yingheng Wang, Goncalo J. Gouveia, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23617v1)

**Summary:** Identifying small-molecule structures from molecular formulas and tandem mass spectra remains a bottleneck in untargeted metabolomics and natural-product discovery. Even when database retrieval or de novo prediction misses the exact structure, the resulting candidates can provide starting points for exploring nearby structures through a few bond edits. We introduce GEMS (Guided Editing of Molecular Structures), which refines candidates through learned 2-switch bond edits that preserve the molecu...

---

### 16. Beyond Action Prediction: Learning Search-Free Planning in Latent Space

**Authors:** Guanchen Du, Jinhao Du, Yanpeng Sun, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23615v1)

**Summary:** Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representati...

---

### 17. SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational Agents

**Authors:** Ravil Mussabayev, Saveliy Zavertyaev, Dmitriy Parpulov, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23612v1)

**Summary:** The rapid proliferation of conversational AI agents necessitates evaluation methods that assess performance across diverse dialogue scenarios, utilizing multiple situational criteria, as appropriate behavior depends on context and encompasses various aspects. Existing dialogue benchmarks typically use static natural conversations, which underrepresent rare situations---a critical safety gap, as low-probability events become frequent failures at production scale. However, limited sample sizes for...

---

### 18. From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents

**Authors:** Yewei Zhao, Derong Xu, Wei Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23599v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23599v1)

**Summary:** Large language model (LLM) agents tackle complex tasks through reasoning and interaction with external environments. Agent skills provide persistent, transferable capabilities that guide task planning, inform contextual decisions, support tool use, and enable executable procedures. Yet existing skill-evolution methods largely organize knowledge around skill artifacts, overlooking the functional heterogeneity within individual skills and its implications for knowledge maintenance and use. Inspire...

---

### 19. RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory

**Authors:** Dabin Sheng, Zhe Wu, Jinming Zhao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23598v1)

**Summary:** Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the disp...

---

### 20. Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents

**Authors:** Mingze Yin, Xiaohan Wang, Dian Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23574v1)

**Summary:** While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured behavioral patterns and compromised update controllability. Furthermore, as foundational LLM r...

---

### 21. SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents

**Authors:** Jin Ye, Yifan Jiang, Lan-zhe Guo

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23554v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23554v1)

**Summary:** Large language model agents increasingly rely on skills to extend their capabilities in complex tasks. However, scalable skill use requires Selective Skill Exposure (SSE): providing relevant procedural content when needed while avoiding unnecessary exposure that may disrupt reasoning. Existing paradigms fall short in complementary ways. Progressive disclosure exposes metadata for a growing skill library, introducing context pollution; retrieval limits catalog exposure, but static retrieval from ...

---

### 22. Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning

**Authors:** Anshul Nayak, Shahil Shaik, Jonathan Smereka, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23550v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23550v1)

**Summary:** Reinforcement learning (RL) policies optimized for task rewards may produce behaviors that are efficient but misaligned with human expectations, safety preferences, or intent. This paper presents a reason-guided preference-based reinforcement learning (PbRL) framework that learns a human reward model from trajectory-level feedback. In addition to preference labels, the framework incorporates reason tags explaining why a behavior is preferred, enabling the learned reward to capture both human cho...

---

### 23. From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation

**Authors:** Gabriel Hortea, Simon Pietro Romano, Juan Tapiador, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23534v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23534v1)

**Summary:** Small Language Models (SLMs) are increasingly attractive for resource-constrained environments due to their low computational footprint. These characteristics also make them candidates for future autonomous malware, where connectivity, latency, privacy, or operational constraints may preclude cloud-based inference. Yet the ability of ultra-compact models to support malware during post-exploitation remains poorly understood.   We systematically evaluate seven open-source SLMs (20M-1.5B parameters...

---

### 24. Truth in Contrast: Calibrated Factual Evidence from Language Model Likelihoods

**Authors:** Ponhvoan Srey, Jason Lucas, Pittawat Taveekitworachai, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23527v1)

**Summary:** Large Language Models (LLMs) encode substantial factual knowledge. Yet, estimating confidence in factual claims reliably remains challenging. We study likelihood-based factual confidence from the complementary perspectives of discrimination and calibration across multilingual factual statements. Specifically, we instantiate contrastive generative likelihoods as Contrastive Factual Evidence (CFE), which compares the likelihood of the same claim under competing factual and non-factual conditions, ...

---

### 25. Trapped in Your Story: Evaluating Narrative-Induced Sycophancy in Large Language Models

**Authors:** Runtai Yang, Dandan Zhu, Kaiwei Zhang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23525v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23525v1)

**Summary:** Large language models (LLMs) are known to exhibit sycophancy by adjusting their responses toward users' expressed views. However, real users often justify their opinions through reasons, personal experiences, causal explanations, and broader narratives, raising the question of whether such narratives can further steer model judgments. We construct a controlled benchmark of 500 debatable questions across ten domains, where the user stance is held fixed while its justification is systematically va...

---

### 26. LocalIntent: Outcome-Specific Structured Generation for Backend-Compatible Smart Building Automation with Local LLMs

**Authors:** Tianyang Liu, Jiayue Wang, Zhanhao Cheng, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23511v1)

**Summary:** Locally deployed large language models (LLMs) can reduce reliance on remote cloud services for natural language smart building automation, but backend-facing processing requires correct outcome selection, alignment with local capabilities, and valid structured outputs. We investigate whether a complete outcome-specific prompting design improves compact-model outputs beyond generic route-then-generate prompting. The proposed LocalIntent approach routes requests to ordinary or persistent-rule bran...

---

### 27. A Topological Signature of Learning under Noisy Labels

**Authors:** Zhongtian Sun, Fan Mo, Prayag Tiwari, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23491v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23491v1)

**Summary:** How does noisy supervision change the representations learned by a neural network? Training accuracy measures agreement with training labels but provides little information about representation geometry. We use persistent homology to track loop structure across distance thresholds in neural activations. Experiments span image classification, text classification, and modular arithmetic. On a fixed CIFAR-10/ResNet-18 training probe, equally sized clean-label and corrupted-label subsets show no det...

---

### 28. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

**Authors:** Takashi Ishida, Taro Makino, Issa Sugiura

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23470v1)

**Summary:** Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to target, comparing diverse, well-reasoned options can be more useful than a single ...

---

### 29. S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models

**Authors:** Wenda Li, Tongya Zheng, Shunyu Liu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23465v1)

**Summary:** Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherenc...

---

### 30. GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways

**Authors:** Yitian Zheng, Zhaorun Chen, Haoyu Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23449v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23449v1)

**Summary:** AI agents have increasingly interacted with external environments by invoking tools, with Model Context Protocol (MCP) emerging as a standard interface for connecting agents to heterogeneous tools and services. As organizations deploy agents at scale, MCP gateways have become a critical middleware layer for aggregating, governing, and shaping the tool surface exposed to agents. Despite the growing importance of MCP gateways in agentic systems, no prior work has systematically studied how gateway...

---

### 31. RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning

**Authors:** Alexander W. Goodall, Francesco Belardinelli

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23445v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23445v1)

**Summary:** In many real-world scenarios we need to consider formal requirements, such as safety and constraint compliance, to deploy Reinforcement Learning (RL) agents. In this paper we introduce RecReg, a safe RL framework capable of enforcing non-Markovian regular safety properties via recovery-based shielding. RecReg is a unified approach that supports different levels of a priori knowledge and safety guarantees. The paper primarily focuses on building the theoretical foundations for RecReg in the tabul...

---

### 32. ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals

**Authors:** Rajdeep Pandhare, Delzaan Bharucha

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23443v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23443v1)

**Summary:** Efficient expert routing is a fundamental challenge in Mixture-of-Experts (MoE) systems, particularly for heterogeneous collections of independently trained Large Language Mod els (LLMs). Existing routing approaches typically rely on jointly trained gating networks, prompt-based predictors, or computationally expensive multi-model inference, limiting their flexibility and efficiency. This paper presents ScoutRoute, a lightweight post-hoc routing framework that predicts expert competence using in...

---

### 33. Generative Policy Improvement from Observational Data

**Authors:** Jonas Schweisthal, Dennis Frauen, Stefan Feuerriegel, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23436v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23436v1)

**Summary:** We study how to improve decision policies from observational data to generate better actions when actions are complex, structured objects, such as text messages or images. This task is subject to two major challenges: (i) action-level overlap is often too weak for reliable off-policy evaluation and improvement, and (ii) generating new structured actions often requires expensive training or fine-tuning (e.g., of an LLM) and can be ill-defined due to information loss in action representations. To ...

---

### 34. AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation

**Authors:** Jiawei Geng, Zhenyang Liu, Yuzheng Wu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23396v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23396v1)

**Summary:** Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects. However, strong results in structured environments do not automatically transfer to open-world conditions, where clutter, occlusion, and changing viewpoints can obscure the spatial relationships required for action. To address this perceptual gap, a virtual active-perception paradigm is introduced. AWAM, an Active World-Action Model actively plans where ...

---

### 35. Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries

**Authors:** Junchi Liao

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23362v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23362v1)

**Summary:** Modern LLM applications rely on runtime monitors that inspect tool calls, traces, streams, detector outputs, and verifier inputs. This creates an interface-reliability problem: a framework path may remain operational while policy-relevant evidence never reaches its decision point. In one representative case, a regex detector returned a positive match, but the framework stranded the result before the block decision. This differs from jailbreaks and detector errors because the evidence is already ...

---

### 36. OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting

**Authors:** Kwangryeol Park, Seulki Lee

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23345v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23345v1)

**Summary:** Self-supervised representation learning has advanced time series forecasting by capturing robust features from unlabeled data. However, existing contrastive and masking-based methods often struggle to explicitly model the underlying temporal flow, either by treating time lag as noise or by disrupting the inherent temporal dynamics essential for forecasting. To address these limitations, we propose OliO (**O**DE-based **Li**near Transition **O**perator), a plug-and-play self-supervised learning m...

---

### 37. Language Models Learn to Improve Language Models

**Authors:** Minhua Lin, Zijun Wang, Zewen Liu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23344v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23344v1)

**Summary:** Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires evaluating tens of thousands of proposals, each potentially requiring a full model-tra...

---

### 38. Robust Function Calling for LLM Agents Under Interface Drift

**Authors:** Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23342v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23342v1)

**Summary:** Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method...

---

### 39. AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics

**Authors:** Dayan Pan, Bincheng Zuo, Xiaojian Wang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23317v1)

**Summary:** Enterprise data analysis requires agents to connect analytical requests with knowledge distributed across databases, business documents, and existing example tasks. Without an explicit representation of this knowledge, an agent may produce incorrect analytical results and cannot reliably incorporate feedback. We present AgentOnto, an ontology-guided LLM agent for enterprise data analytics. AgentOnto organizes heterogeneous enterprise knowledge into an ontology that directly guides analysis and i...

---

### 40. From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory

**Authors:** Shangze Li, Yanyu Yao, Derong Xu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23313v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23313v1)

**Summary:** Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions. Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the final context redundant or incomplete. To address this gap, we propose MemCompile, a query-conditioned evidence compilation framework for long-term conversational memory. Given a q...

---

### 41. Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs

**Authors:** Fabian Broszio, Michael Hoffmann, Adrian Paschke

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23311v1)

**Summary:** Large language models (LLMs) can generate fluent outputs that lack source support or conflict with local operational constraints. We introduce Self-Reflective Chain-of-Thought (SRCoT), a modular architecture that organizes generation as a closed Retrieve--Reflect--Revise loop. SRCoT separates environment state, persistent knowledge, accumulated experience, and short-term memory into provenance-labeled stores. BM25 retrieval supplies local context; subsequent passes expose intermediate drafts, mi...

---

### 42. MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection

**Authors:** Songping Wang, Peiyang Li, Yi Huang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23307v1)

**Summary:** Multimodal large language model (MLLM)-based mobile agents are rapidly evolving from conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments. This capability also exposes a new security risk: adversaries can embed malicious objectives in cross-application mobile content and steer agent behavior through indirect multimodal injection. Although prompt injection has been studied in desktop and web settings, its cross-modal properties in mobile...

---

### 43. SimOPD: Relational Knowledge Transfer for On-Policy Distillation

**Authors:** Kai Tang, Xing Zheng, Haobo Wang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23306v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23306v1)

**Summary:** A key challenge in on-policy distillation (OPD) is extracting effective supervision from teacher knowledge. Supervision from token probabilities may underutilize internal knowledge, while direct hidden-state matching forces the student to shift to the teacher's feature space and complicates cross-architecture transfer. Inspired by contrastive learning's use of relationships between instances, we propose \textbf{SimOPD} to transfer teacher internal knowledge through response similarities. Specifi...

---

### 44. Designing for Imperfect Prompts: A Simulation-Based Evaluation of an LLM-Based Enterprise Data Assistant Using Knowledge Graphs

**Authors:** Niklas Wagner, Alexander Mädche

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23304v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23304v1)

**Summary:** Enterprise data assistants using large language models (LLMs) promise democratized data access in organizations. Yet in our real-world deployment within the CFO unit's data lake at an industry partner, we observed that business users frequently pose imperfect prompts that include domain-specific vocabulary and lack schema references or structural information. This Design Science Research study examines automatic resolution using a semantic mediation layer. We design and evaluate two design varia...

---

### 45. Optimist Deep Research: An Iterative, State-Centric Agent for Autonomous Literature Research

**Authors:** Gihan Panapitiya

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23299v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23299v1)

**Summary:** Most retrieval-augmented systems treat literature search as a single retrieval step followed by summarization. Real literature research works differently: the investigator's understanding of the question changes as they read, new subquestions appear, and evidence is weighed, not just collected. We present Optimist Deep Research, an open-source agent that runs literature research as an iterative evidence-acquisition process over an explicit, mutable research state. A research question is broken i...

---

### 46. FlashReFocus: Interactive Image Refocusing in Seconds

**Authors:** Ching-Heng Cheng, Chia-Ming Lee, Ming-Ching Chang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23297v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23297v1)

**Summary:** Single-image refocusing changes the focal plane and depth of field of a photograph after capture. It is inherently interactive: users try many focal points and blur strengths on one image, so each edit should be fast and change only the blur. Recent generative methods, however, rerun large diffusion models for every edit. We observe that the two sub-problems differ in kind: recovering the all-in-focus image is ill-posed and needs a generative prior, whereas rendering blur is largely determined b...

---

### 47. CoTA++: Understanding the Repeat Curse in dMLLMs from an Information Flow Perspective

**Authors:** Qiyan Zhao, Xiaofeng Zhang, Xu-Yao Zhang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23290v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23290v1)

**Summary:** Diffusion-based multimodal large language models (dMLLMs) decode by iterative denoising with bidirectional attention, which precludes the standard autoregressive key--value cache. Practical deployments therefore rely on approximate caching that reuses intermediate states across denoising steps. Such caching, however, often makes a response repeat one token at adjacent positions in a run that breaks the sentence, a failure we term the \emph{Repeat Curse}. Tracing the context-token information flo...

---

### 48. Annotrace: A Workbench for Step-Level Annotation of Agent Traces

**Authors:** Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23284v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23284v1)

**Summary:** Every study of why LLM agents fail begins by labelling traces by hand, and every such study builds its own throwaway tool. Observability platforms record agent traces but offer no structured labelling; annotation tools label text but have no notion of a step, a delegation or a tool call, leaving it unclear what the smallest unit of execution to label should be. Annotrace reads six trace formats, including OpenTelemetry GenAI, LangSmith and Langfuse, and turns each run into an ordered, nested lis...

---

### 49. Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents

**Authors:** BHVSP Subrahmanyam, Neeraj Choudhary

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23266v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23266v1)

**Summary:** LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence. Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence. We study per-decision memory sufficiency: selecting a small subset that preserves full-memory behavior. To separate search error from model error, we introduce JointCoreBench, a benchmark with nine interaction families, six workflow domains, natural-language decisions, and exact sufficient-set o...

---

### 50. Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To

**Authors:** Uriel Dolev, Idan Schwartz, Yoav Goldberg

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23257v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23257v1)

**Summary:** Chain-of-thought (CoT) controllability, the ability of reasoning models to control properties of their CoT, is consequential for both their usefulness and reliable oversight. Recent work evaluates this capability by measuring whether models follow CoT constraints given in the user prompt, and reports very low controllability across models. We argue that this low controllability may not reflect an inherent inability of reasoning models to control their CoT, but instead result from naively specify...

---

## cs.CL

**50 papers**

### 1. Behavioral Couplings: From Formation to Behavioral Emergence in Language Models

**Authors:** Dongyoon Hahm, Woogyeol Jin, Dennis Wei, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23847v1)

**Summary:** Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is...

---

### 2. AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery

**Authors:** Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23845v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23845v1)

**Summary:** Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 publ...

---

### 3. DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses

**Authors:** Jianyuan Zhong, Chenwei Wu, Zhaochen Yu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23839v1)

**Summary:** Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our DiscoveryRSI framework develops hypothesis trees through multi-agent evolutionary search, c...

---

### 4. Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation

**Authors:** Shaoang Li, Yanhang Shi, Yufei Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23831v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23831v1)

**Summary:** A reasoning trace can accompany a correct answer without providing effective supervision for a particular student. We study how to construct traces that improve learning beyond answer-only supervision by considering both their intermediate content and their accessibility to the target learner. We introduce ReDiST, a student-conditioned trace-construction and distillation framework for evidence-rich reasoning. Starting from the student's own attempts, ReDiST revises answer-correct drafts against ...

---

### 5. Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative Decoding

**Authors:** Chiatzen Wang, Bill Xu, Haochen Gu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23818v1)

**Summary:** Speculative decoding typically characterizes speedup by draft tokens accepted per verification round. Lossless verification preserves the target model's output distribution and thus expected completion length, making this metric a meaningful efficiency proxy. Relaxed (lossy) verification accepts tokens that lossless verification would reject, potentially altering that distribution. We identify a length inflation phenomenon: relaxed verification lengthens completions, primarily by extending reaso...

---

### 6. Steering beyond Language: Improving Multilingual Training-Free Text Embeddings via Paired-Residual Subspace Removal

**Authors:** Ailiang Lin, Zhuoyun Li, Yusong Wang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23807v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23807v1)

**Summary:** While deriving text embeddings directly from frozen LLMs has emerged as a promising direction, existing methods focus almost exclusively on English, leaving multilingual settings largely unexplored. In this work, we present the first systematic study of multilingual training-free text embeddings in LLMs. Our analysis reveals a language-conditioned embedding geometry in which semantically equivalent sentences remain misaligned across languages. We hypothesize that language-specific variation can ...

---

### 7. DLite: History-free Speculative Decoding for Agentic AI

**Authors:** Jiaming Xu, Hanzhen Wang, Tianlang Zhao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23787v1)

**Summary:** Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cac...

---

### 8. VocalGrad: Evaluating Acoustic Perception in Audio Language Models

**Authors:** Koki Ryu, Hitomi Yanaka

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23745v1)

**Summary:** Recent large audio language models (LALMs) have extended their capabilities beyond lexical speech understanding to tasks requiring paralinguistic and non-linguistic audio understanding, such as emotion recognition. However, these models still struggle to reliably utilize acoustic information, particularly when it co-occurs with spoken linguistic content. Existing benchmarks do not clearly distinguish acoustic perception from higher-level reasoning, making it difficult to identify the source of t...

---

### 9. The Italian lawmaking process: a unified and structured dataset

**Authors:** Matilde Contestabile, Chiara Ferrara, Giovanni Parrillo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23741v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23741v1)

**Summary:** The Italian legislative process is documented in detailed parliamentary records hosted in institutional websites. However, much of this information is available only as unstructured text, limiting its systematic reuse. We applied a controlled, systematic LLM-based extraction procedure, validated against manually annotated records, to convert these texts into ordered and dated events including, e.g., bill introduction, committee examination, plenary examination, and approval. The resulting datase...

---

### 10. Bridging the Language Gap in Scholarly Data II: Enhancing Gender Inference for Chinese Names

**Authors:** Lisette Espín-Noboa, Mingrong She, Ana Maria Jaramillo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23734v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23734v1)

**Summary:** Perceived gender inference from names is important for inclusive scientometrics research, yet existing methods perform poorly on non-Western scholars. We address this gap for Chinese names, which appear in two forms, Hanzi and Pinyin, its Romanized form (e.g., Zhang Wei, Li Na). In international bibliographic records, names are often available only in Pinyin. However, a single pinyin name can correspond to multiple distinct hanzi characters with different gender associations, so gender inference...

---

### 11. Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification

**Authors:** Mukand Krishna, Anoushka Harit, Chenghao Xiao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23721v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23721v1)

**Summary:** Publication count is not study count. A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence. We evaluate this behavior in medical LLM verification using 14 source-audited clinical families and five model conditions. The families span provenance, clinical applicability, result direction, and composition; the provenance families provide the direct lineage tests. Recognition and aggregation are separat...

---

### 12. The Cognitive Cost of LLM Writing: A Reading-Time Comparison with Human Text

**Authors:** Kamer Cekini, Elisabetta Biondi, Chiara Boldrini, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23715v1)

**Summary:** Although linguistic differences between human-written and Large Language Model (LLM)-generated texts have been extensively studied, their implications for the cognitive effort involved in reading remain less explored. In psycholinguistics, reading time is commonly used as an indirect measure of cognitive processing effort. Building on this perspective, we investigate whether human-written texts and their LLM-generated rewrites exhibit differences in predicted reading time that may reflect differ...

---

### 13. GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search

**Authors:** Hyunseo Kim, Suil Choe, Sukkyoung So, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23709v1)

**Summary:** Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic fra...

---

### 14. VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers

**Authors:** Yinuo Xu, Jadie Adams, Brian Hu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23702v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23702v1)

**Summary:** Personalizing a language model requires knowing what a person values, which stays largely consistent across tasks. Yet most methods either learn task-specific preferences or place the user's profile in the prompt, where models struggle to act on it. We introduce VISTA (Value-Informed Steering and Targeted Acquisition), which infers a latent profile from users' (full or partial) survey answers, and maps the profile through a hypernetwork to a user-specific steering intervention in a frozen LLM to...

---

### 15. Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS

**Authors:** Séverin Baroudi, Yanis Labrak, Petr Motlicek, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23678v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23678v1)

**Summary:** Qwen3-TTS reports state-of-the-art zero-shot voice cloning, but its technical report leaves open how the model should be conditioned, how it behaves outside read speech, and how it fails. We characterise its two cloning interfaces, in-context learning (ICL) and X-Vector, against Chatterbox, XTTS-v2 and F5-TTS on read, meeting, emotional and air-traffic-control (ATC) speech, using eighteen objective measures, an LLM judge, a spoofing countermeasure and a listening test. Neither interface dominate...

---

### 16. In Human Memories. Technology, Creativity and Self-Determination: An Ethical Proposal

**Authors:** Francesco Vitucci, Giuseppe Silvi, Francesco Abbrescia, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23651v1)

**Summary:** This research investigates the role of artificial intelligence (AI) in modern compositional practices, with a particular focus on two case studies: Convergence (2020/21) by Alexander Schubert, for String Ensemble and AI System, and In Human Memories (2024) by Francesco Vitucci, for four cellos and one electroacoustic player, whose installation was created by the Electronic Music School of the "N. Piccinni" Conservatory of Bari. The initial historical survey traces the evolving use of technology ...

---

### 17. PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation to User State

**Authors:** Peña Arroyo Gallego, Mauro Ruiz Moreno, Alejandro Acien, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23625v1)

**Summary:** Presence-aware intelligence is the capacity of an AI system's intelligence layer to adapt appropriately to the functional state of the person it serves (here readiness, flow, and stability) while preserving task quality and safety. We introduce PresenceBench, an instrument for measuring it. PresenceBench evaluates how the intelligence layer uses a supplied state, not how that state is sensed, and breaks the capability into measurable properties. Two are tested here. Receptivity: does the model t...

---

### 18. Trajectory-Triggered Sparse Collaborative Decoding

**Authors:** Amit Ranjan Trivedi, Sruthikesh Surineni, Kyong Ho Lee, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23613v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23613v1)

**Summary:** Dense assistance methods such as speculative decoding repeatedly verify draft tokens with a target model, keeping target computation coupled to generation. We study sparse collaborative decoding, where a draft model generates most tokens and a target model is invoked only for short corrective segments. The key problem is deciding when to call the target. We show that local uncertainty is a weak trigger: entropy, negative log-likelihood, logit margin, top-$k$ mass, and velocity features give near...

---

### 19. SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational Agents

**Authors:** Ravil Mussabayev, Saveliy Zavertyaev, Dmitriy Parpulov, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23612v1)

**Summary:** The rapid proliferation of conversational AI agents necessitates evaluation methods that assess performance across diverse dialogue scenarios, utilizing multiple situational criteria, as appropriate behavior depends on context and encompasses various aspects. Existing dialogue benchmarks typically use static natural conversations, which underrepresent rare situations---a critical safety gap, as low-probability events become frequent failures at production scale. However, limited sample sizes for...

---

### 20. Not Every Mention Is a Claim: Rethinking Object Hallucination Detection in Vision-Language Models

**Authors:** Hsin-Ling Hsu, Neeraja Kirtane, Kuan-Hao Huang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23610v1)

**Summary:** Object hallucination in vision-language models (VLMs) is usually measured by checking each object a caption names against the image. Most benchmarks and detectors alike treat every object mention as a claim that the object is present. This assumption fails when a caption names an object without asserting it, as in "a bench for people to sit on", which mentions people without claiming that any are in the image. We call such mentions non-assertive. Treating them as hallucinations inflates the erro...

---

### 21. Enhancing RAG-based Medical VQA with Gated Multimodal Representations

**Authors:** Daniela Jimenez-Pano, Hugo Jair Escalante, Delia Irazú Hernández-Farías

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23588v1)

**Summary:** Medical Vision-Language Models (Med-LVLMs) have shown strong performance in Medical Visual Question Answering (MVQA), yet they may still produce factually inconsistent responses. Retrieval-Augmented Generation (RAG) can mitigate this issue by incorporating external clinical evidence; however, retrieval is often guided by a single modality, potentially overlooking the joint semantics of medical images and clinical questions. We introduce a multimodal RAG framework that learns a joint query repres...

---

### 22. Analyzing Occupational Gender Bias across the LLM Training Lifecycle

**Authors:** Manthan Gadhia, Alexander Hoyle, Karolina Stańczak

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23587v1)

**Summary:** Post-training is widely assumed to reduce the social biases language models inherit from pretraining, yet direct evidence for this assumption remains mixed. In this paper, we examine how gender disparities evolve across the language modeling pipeline. In particular, we study occupational gender bias in OLMo 3, a fully open language model family, across its post-training stages by prompting each checkpoint to generate open-ended narratives about synthetic personas given their occupation and educa...

---

### 23. MARS: Memory-Aware Routing for Session-Level LLM Assistants

**Authors:** Minghan Wang, Jinhang Zuo, Zhongxiang Dai, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23583v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23583v1)

**Summary:** Long-term LLM assistants must repeatedly decide what prior context to expose and which model should answer as an interaction evolves. Existing memory systems and model routers usually make these decisions separately, although memory construction changes the evidence, distractors, and difficulty of the resulting input. We introduce MARS, a memory-aware routing framework that uses session state as a shared control interface between memory construction and model selection. A Query and Topic Manager...

---

### 24. Execution Before Memory: Diagnosing Memory Failures in Video World Models

**Authors:** Weiyang Jin, Jiwen Yu, Sihan Xu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23542v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23542v1)

**Summary:** A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the sc...

---

### 25. ConvexLLM: Scaling Convex-Hull Speech Interfaces to General-Purpose Audio Intelligence

**Authors:** Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23539v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23539v1)

**Summary:** Speech and audio language models connect continuous acoustic representations to decoders pretrained primarily on text data. Most such models use MLP or Q-Former interfaces to map acoustic features into the decoder's input space, requiring the decoder to learn how to interpret the resulting representations. We investigate whether grounding these representations in the decoder's existing text embeddings can help it use acoustic information while better preserving its pretrained text capabilities. ...

---

### 26. EduWild: How Teacher-Configured Chatbots Fail in Real-World Use and How to Fix Them

**Authors:** Ziqi Liu, Ruiwei Xiao, Yuxuan Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23530v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23530v1)

**Summary:** Teachers increasingly configure educational chatbots through natural-language instructions, but how these bots fail in real-world use remains poorly understood. We introduce EduWild, a dataset of 1,726 conversations with 217 teacher-configured chatbots, each paired with the instructions and configuration behind it, including 900 conversations from the intended end users of 35 deployed chatbots. We develop a 29-code taxonomy covering factual, workflow, diagnostic, and pedagogical failures and app...

---

### 27. Truth in Contrast: Calibrated Factual Evidence from Language Model Likelihoods

**Authors:** Ponhvoan Srey, Jason Lucas, Pittawat Taveekitworachai, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23527v1)

**Summary:** Large Language Models (LLMs) encode substantial factual knowledge. Yet, estimating confidence in factual claims reliably remains challenging. We study likelihood-based factual confidence from the complementary perspectives of discrimination and calibration across multilingual factual statements. Specifically, we instantiate contrastive generative likelihoods as Contrastive Factual Evidence (CFE), which compares the likelihood of the same claim under competing factual and non-factual conditions, ...

---

### 28. Perceive, Solve, Reason: Progressive Capability Formation in Time Series-LLMs

**Authors:** Xin Qiu, Junlong Tong, Wei Zhang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23521v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23521v1)

**Summary:** Large language models (LLMs) can now perceive, describe, and reason about images and audio, yet time series understanding remains underestimated: most work uses LLMs as forecasters and classifiers, reasoning studies are few and narrow, and no suite trains and evaluates the full range of capabilities. In this paper, we build the first such suite, with 337K training and 44K evaluation samples across three progressive capabilities, Perceive, Solve, and Reason, and use it to ask how time series shou...

---

### 29. MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups

**Authors:** Markus Fischer, Jens Meiler, Matthias Elgeti

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23480v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23480v1)

**Summary:** Research groups that want a language model grounded in their own literature face a choice between hosted services that receive their unpublished work and self-hosted deployments that keep the data local but give the model no access to the corpus. Munin is an open-source framework for a self-hosted scientific assistant that indexes a group's corpus and its citation graph, and wraps whichever open-weight model the group can serve in an agent harness with specialised reading, search, and computatio...

---

### 30. A low-dimensional dynamical basis for tongue shape control

**Authors:** Sam Kirkham, Patrycja Strycharczuk

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23456v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23456v1)

**Summary:** Speech production involves the control of a high-dimensional articulatory system with many degrees-of-freedom, but a widespread hypothesis is that speakers navigate this complexity using a set of lower-dimensional control variables. Common candidates for these control variables include individual articulators (e.g. tongue body) and abstract tract variables (e.g. tongue body constriction location), but identifying the most appropriate coordinate system for articulatory control remains an open que...

---

### 31. HydraLLM: Adaptive Width Slicing for Elastic Text and Vision-Language Models

**Authors:** Oscar Kemme, Janek Haberer, Ali Hojjat, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23455v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23455v1)

**Summary:** LLMs and LVLMs are increasingly deployed across heterogeneous hardware, ranging from data-center GPUs to resource-constrained edge devices. Their fixed-size architectures limit the ability to reuse a single model across deployment settings with different compute, latency, and model-size targets. We introduce HydraLLM, an elastic MQA-based architecture. Its number of active attention heads determines the effective widths of the embeddings, attention projections, feed-forward layers, and the outpu...

---

### 32. "You" Is Not Toxic: How LLM Labelers Rewrite the Web's Conversation Laws

**Authors:** Liang Yue, Eric A. Vance

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23446v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23446v1)

**Summary:** What the Web community believes about toxic conversations, such as that toxicity rises in longer and deeper threads, was measured mostly with Google's Perspective API, which is shutting down; large language models (LLMs) will make the next measurements. We find that LLM labelers mistake second-person address for toxicity, and that this one bias manufactures laws that human labels do not show. On 1.25 million news comments with crowd labels, Claude Haiku flags 12% of the non-toxic comments that c...

---

### 33. ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals

**Authors:** Rajdeep Pandhare, Delzaan Bharucha

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23443v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23443v1)

**Summary:** Efficient expert routing is a fundamental challenge in Mixture-of-Experts (MoE) systems, particularly for heterogeneous collections of independently trained Large Language Mod els (LLMs). Existing routing approaches typically rely on jointly trained gating networks, prompt-based predictors, or computationally expensive multi-model inference, limiting their flexibility and efficiency. This paper presents ScoutRoute, a lightweight post-hoc routing framework that predicts expert competence using in...

---

### 34. On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs

**Authors:** Jaewon Sok, Jewon Yeom, Seonghyeon Park, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23400v1)

**Summary:** Large language models often answer factual questions incorrectly in closed-book settings, and such errors are usually attributed to missing knowledge. Yet models often encode answers they fail to produce. We show that many closed-book errors are first-token recall failures: the model commits to a wrong first token, but once given the right one it completes the answer and often recognizes it as correct. We study this with First-Token Cueing, a behavioral probe that prefills the response with the ...

---

### 35. Sentence-Level Topic Modeling with Lexical and Contextual Evidence

**Authors:** Federica Granese, Serena Villata, Charles Bouveyron

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23388v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23388v1)

**Summary:** Topic modeling faces a fundamental granularity dilemma: probabilistic topic models assign topics at the word level, whereas transformer-based methods operate at the document level. The latter overlooks that real-world documents typically cover multiple topics, whereas the former relies on individual words, which rarely provide sufficient context to identify them. We introduce SentenceETM, a neural topic model that assigns a topic to each sentence by jointly using lexical and contextual evidence....

---

### 36. Language Models Learn to Improve Language Models

**Authors:** Minhua Lin, Zijun Wang, Zewen Liu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23344v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23344v1)

**Summary:** Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires evaluating tens of thousands of proposals, each potentially requiring a full model-tra...

---

### 37. Robust Function Calling for LLM Agents Under Interface Drift

**Authors:** Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23342v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23342v1)

**Summary:** Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method...

---

### 38. Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs

**Authors:** Fabian Broszio, Michael Hoffmann, Adrian Paschke

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23311v1)

**Summary:** Large language models (LLMs) can generate fluent outputs that lack source support or conflict with local operational constraints. We introduce Self-Reflective Chain-of-Thought (SRCoT), a modular architecture that organizes generation as a closed Retrieve--Reflect--Revise loop. SRCoT separates environment state, persistent knowledge, accumulated experience, and short-term memory into provenance-labeled stores. BM25 retrieval supplies local context; subsequent passes expose intermediate drafts, mi...

---

### 39. Inferring L1 Backgrounds from L2 English with LLM Token Probabilities

**Authors:** Ahmet Yavuz Uluslu, Mark Gales, Kate Knill, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23309v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23309v1)

**Summary:** Native language identification (NLI) infers a non-native speaker's first language (L1) from their second language (L2) production. We investigate a token probability approach that scores each text sample as a continuation of a prompt prefix specifying a candidate L1, then predicts the candidate with the highest score. We evaluate our approach using Llama 3.1 8B and 70B on three datasets: TOEFL9, Write and Improve 2024, and BULATS-L1. We compare its performance with previous prompting-based class...

---

### 40. SimOPD: Relational Knowledge Transfer for On-Policy Distillation

**Authors:** Kai Tang, Xing Zheng, Haobo Wang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23306v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23306v1)

**Summary:** A key challenge in on-policy distillation (OPD) is extracting effective supervision from teacher knowledge. Supervision from token probabilities may underutilize internal knowledge, while direct hidden-state matching forces the student to shift to the teacher's feature space and complicates cross-architecture transfer. Inspired by contrastive learning's use of relationships between instances, we propose \textbf{SimOPD} to transfer teacher internal knowledge through response similarities. Specifi...

---

### 41. Annotrace: A Workbench for Step-Level Annotation of Agent Traces

**Authors:** Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23284v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23284v1)

**Summary:** Every study of why LLM agents fail begins by labelling traces by hand, and every such study builds its own throwaway tool. Observability platforms record agent traces but offer no structured labelling; annotation tools label text but have no notion of a step, a delegation or a tool call, leaving it unclear what the smallest unit of execution to label should be. Annotrace reads six trace formats, including OpenTelemetry GenAI, LangSmith and Langfuse, and turns each run into an ordered, nested lis...

---

### 42. Verbalising Model's Computation for Chain-of-Thought Faithfulness Detection

**Authors:** Yujing Wang, Yulan He, Wenya Wang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23275v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23275v1)

**Summary:** Current Chain-of-Thought (CoT) verification methods detect reasoning faithfulness from model outputs or static activations, but are limited in explaining how unfaithfulness develops during generation. We introduce VERITAS to verbalise the model's computation: how different reasoning anchors emerge, transfer across layers, and surface in the output. VERITAS adopts the layer-wise Jacobian projection to produce a verbalised account of the model's internal reasoning evolution at each generated CoT t...

---

### 43. Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To

**Authors:** Uriel Dolev, Idan Schwartz, Yoav Goldberg

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23257v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23257v1)

**Summary:** Chain-of-thought (CoT) controllability, the ability of reasoning models to control properties of their CoT, is consequential for both their usefulness and reliable oversight. Recent work evaluates this capability by measuring whether models follow CoT constraints given in the user prompt, and reports very low controllability across models. We argue that this low controllability may not reflect an inherent inability of reasoning models to control their CoT, but instead result from naively specify...

---

### 44. Sample, Mix, or Verify? Allocating Test-Time Compute under Imperfect Verifiers

**Authors:** Srinivasan Iyengar

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23255v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23255v1)

**Summary:** A common way to make language models and agents more accurate is to spend more compute at inference time: generate many candidate solutions and submit the one a verifier prefers. Success then requires that some candidate is correct and that the verifier picks it. The first grows predictably with the number of samples; the second does not, because real verifiers (unit tests, majority votes, LLM judges, reward models) accept wrong answers, reject right ones, and make correlated mistakes. With a fi...

---

### 45. Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents

**Authors:** Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23254v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23254v1)

**Summary:** Tool-using agents read untrusted external content, which exposes them to indirect prompt injection (IPI), where hidden instructions hijack the agent's tool calls. Benchmarks measure IPI security by the attack success rate (ASR), which treats every failed attack as a successful defense. To test this assumption, we audit 33,000 trajectories from eleven open-weight agents (2-14B parameters) on InjecAgent and AgentDojo. A label-blind LLM judge shows that most failed attacks are ignored (76-80%) rath...

---

### 46. Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages

**Authors:** Md Sabbir Hossen, Anichur Rahman, Pabon Shaha, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23249v1)

**Summary:** Small-to-large language model routing can reduce inference cost by escalating difficult inputs while retaining easier ones on a smaller model. Its success, however, depends on identifying examples that benefit from escalation, and the reliability of confidence across multilingual tasks remains unclear. We present a systematic evaluation of confidence-based routing across three model families, four languages, and three task types, covering 72 model, dataset, language, and scale configurations and...

---

### 47. Think More or Read More? A Token-Budget Theory of Reasoning with Shared Context

**Authors:** Manh Nguyen, Sunil Gupta, Hung Le

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23246v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23246v1)

**Summary:** Reasoning systems increasingly improve answers by incorporating additional context into the model's input, from multi-agent debate, where agents read their peers' responses, to self-refinement, where a model revisits its own drafts. In these systems, communication consumes context as one agent's output becomes another's input. We study the regime where token reading and generation draw on one fixed token window, so every token spent reading is a token that cannot be spent reasoning. We develop a...

---

### 48. MGE-PO: Entropy-Aware Credit Assignment for Mathematical Reasoning

**Authors:** Jihao Huang, Guangjia Chai, Zhirui Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23245v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23245v1)

**Summary:** GRPO assigns the same group-relative advantage to equally rewarded responses within a question, leaving their generation uncertainty unused. We introduce MGE-PO, centered on four-quadrant (4Q) advantage shaping that combines verified correctness with rollout generation entropy. Correctness determines the sign of an additional correction, while entropy controls its magnitude: lower-entropy successes receive larger bonuses and higher-entropy failures receive larger penalties. An online entropy-bas...

---

### 49. MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation

**Authors:** Yuhan Sun, Jiaxin Zhao, Yongdong Luo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23234v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23234v1)

**Summary:** In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter ...

---

### 50. ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling

**Authors:** Yuki Otsuka, Daisuke Oba, Naoaki Okazaki

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23225v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23225v1)

**Summary:** Drifting Models generate a sample with a single function evaluation, making them attractive for fast parallel language generation, but their one-step formulation does not support iterative refinement. We propose Recurrent Language Generation via Drifting (ReLaDrift), which uses a shared Drifting Model to generate an initial draft from noise and iteratively refine it in a continuous latent space. We train this recurrence by sampling the number of rounds and applying the drifting loss only at the ...

---

## cs.CV

**50 papers**

### 1. Learning to Correct Geometry in Generated Videos

**Authors:** Weijie Lyu, Tiancheng Shen, Jason Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23856v1)

**Summary:** Generated videos often lose geometric consistency under camera motion: structures warp under viewpoint change, parallax becomes inconsistent, and smooth camera movement may collapse into shot-like transitions. We argue that this failure is largely a data problem. In web-scale video corpora, most visible motion comes from dynamic objects captured by static or weakly moving cameras, leaving only sparse supervision for viewpoint-induced appearance changes. To address this, we propose Video Geometry...

---

### 2. Rethinking the design space of Vanilla Pixel Diffusion Transformers

**Authors:** Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23854v1)

**Summary:** Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\boldsymbol{u}$-prediction) with clean image prediction ($\boldsymbol{x_0}$-prediction). In this work, we revisit this choice and introduce MFlow, an adaptive parameterization that learns...

---

### 3. StopWatch: Goal Grounding for Object-goal Navigation

**Authors:** Xinhao Liu, Yunsheng Tian, Yuheng Qiu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23841v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23841v1)

**Summary:** Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack. Our diagnosis identifies goal grounding as the dominant failure. These policies explore well, yet often fail to notice that the goal is already in view or to estimate how far away it is. To address this failure, we grou...

---

### 4. Persistent Planar Memory for Video World Models

**Authors:** Yuze He, Bin Tan, Zelin Gao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23795v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23795v1)

**Summary:** Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced. Plane primitives offer a natural candidate: a compact set of oriented planes captures the dominant structural elements (e.g., walls, floors, facades) of indoor and outdoor scenes, while requiring only 7 parameters per primitive. We present PPMem, a video world model that adopts plane primitives as its persistent 3D memory. PPMem augments a video diffusion transformer with a ...

---

### 5. The Collection of a Real-World, Large-Scale Dataset for Automated Skill Evaluation in Central Line Dressing Change

**Authors:** Ummey Tanin, Shannan K. Hamlin, Hsin-Mei Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23789v1)

**Summary:** Central line-associated bloodstream infections (CLABSIs) remain a major source of preventable morbidity and mortality in healthcare settings. Proper execution of the central line dressing change (CLDC) procedure is essential for infection prevention, yet current approaches to competency assessment rely primarily on manual ob- servation by clinical educators, making evaluation time-intensive, difficult to scale, and limited in consistency and granularity. These challenges highlight the need for A...

---

### 6. Video Diffusion Avatars: Taming Video Diffusion Models into Controllable 3D Avatars

**Authors:** Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23772v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23772v1)

**Summary:** Video diffusion models (VDMs) trained on internet-scale data encode a rich prior on appearance, motion, and physics that is difficult to replicate with explicit 3D rendering and costly 3D data capture. We introduce Video Diffusion Avatars (VDAs), a method that creates photo-realistic, multi-view consistent avatars from a single image by fine-tuning a VDM for precise control over camera viewpoint, facial expression, and upper-body pose. Departing from 3D morphable models (3DMMs), VDAs use a learn...

---

### 7. A Paired RGB-Sonar Dataset for Fish Monitoring with Consumer Sonar

**Authors:** Mourad Derbedrosian, Michael Hobley, Pietro Perona

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23759v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23759v1)

**Summary:** Imaging sonar enables underwater observation in conditions where optical imaging is ineffective due to darkness and turbid water. However, imaging-sonar systems previously used for ecological monitoring have typically been expensive, limiting their accessibility. Consumer forward-looking sonar has the potential to make fish monitoring more accessible, but its noisy imagery makes annotation and the development of automated methods challenging. We introduce the Huntington and Caltech Koi RGB and S...

---

### 8. MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing

**Authors:** Houyuan Chen, Fanzhou Wang, Xiangyu Fan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23751v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23751v1)

**Summary:** Multi-turn image editing aims to modify an image according to a sequence of instructions, making it better aligned with human-AI collaborative creation than single-turn editing. However, constructing high-quality multi-turn training data remains challenging, as conventional sequential rollout accumulates errors and introduces visual-quality drift across editing turns. To address this challenge, we introduce MTEdit, a multi-turn image editing dataset built through a pipeline centered on packed tr...

---

### 9. Beyond Multi-Stage Pipelines: A Label-Correlation Ensemble for Multi-Label Retinal Fundus Disease Classification

**Authors:** Md Asif Uddin, Jannatul Ferdous, Asif Islam, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23747v1)

**Summary:** Retinal fundus images frequently carry more than one disease, and public fundus datasets are heterogeneous and severely long-tailed. Clinical triage suggests a staged design, in which a screening gate, a disease-group router and group-specific classifiers operate in sequence, but it is unclear whether this hierarchy earns its complexity. We present a controlled comparison of three architectures on a unified 39-target label space built from RFMiD 1.0, RFMiD 2.0 and ODIR-5K (12,652 images): (i) a ...

---

### 10. Synthetic Image Oversampling for Rare-Class Representation Learning in Deep Facial Phenotyping

**Authors:** Miles Liao, Zhanliang Wang, Hongzhuo Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23730v1)

**Summary:** Recent deep facial phenotyping methods can support the recognition of genetic syndromes, but patient images are often scarce and unevenly distributed across disorders. Synthetic facial images offer a way to supplement the training data without collecting additional patient photographs. Their usefulness, however, depends on whether they improve recognition of real patients: generated images may introduce artifacts or repeat features already represented in the training set. It is therefore necessa...

---

### 11. FedRAPP: Federated Test-Time Prompt Tuning for Vision-Language Models with Reliability-Aware Prompt Personalization

**Authors:** Syed Md. Ahnaf Hasan, Md Akil Raihan Iftee, Sajib Mistry, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23705v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23705v1)

**Summary:** Federated prompt learning enables vision-language models like CLIP to collaboratively adapt lightweight soft prompts across distributed clients without sharing raw data. However, existing federated prompt learning methods are designed primarily for supervised settings with labeled client data and assumed relatively stable training distributions. At test time, source-free federated prompt tuning remains largely unexplored. Clients may receive unlabeled target samples with heterogeneous, often non...

---

### 12. Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning

**Authors:** Xikang Guan, Shaocong Yang, Yanqi Bao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23677v1)

**Summary:** Physical plausibility is essential for realistic video generation. Existing methods impose physical guidance before synthesis via simulations or refined prompts, but this can limit dynamic diversity, miss errors that emerge only after generation, and require repeated regeneration when inconsistencies remain. We therefore study a generate-diagnose-repair paradigm that preserves the original generation capability and selectively repairs physical inconsistencies afterward, raising two key questions...

---

### 13. PCDFusion: Proposal-Context-Detail Bayesian Rendering for Infrared-Visible Image Fusion

**Authors:** Rui Liu, Lin Gu, Hesong Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23663v1)

**Summary:** Infrared-visible image fusion (IVIF) aims to combine visible and thermal infrared observations for human perception and downstream vision tasks. Visible and thermal infrared observations are physically complementary but unreliable in different ways. Existing deep IVIF methods mainly improve feature interaction and reconstruction, but often lack an explicit local rule for deciding when visible appearance should dominate and when thermal responses should contribute. To address this issue, we refor...

---

### 14. An Efficient Approach to Beetle Damage Detection of Banana Using Deep Learning

**Authors:** Md. Mehedi Hasan Naeem, Ishtiyak Ahmmad Araf, Md. Arefin Haque Mahir, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23661v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23661v1)

**Summary:** Visible surface damage of banana fruits by Basilepta subcostata (the banana fruit scarring beetle) can reduce their market value. Here, manual inspection of Banana fruits is subjective and difficult to scale. This study presents a lightweight framework based on YOLOv8n deep learning model for locating individual bananas and classifying their visible surface condition as healthy or unhealthy. The term beetle damage in the paper title is used operationally for the locally observed scar-like surfac...

---

### 15. FlexPart: Text-Controlled Semantics-Aware 3D Part Segmentation at Flexible Granularity

**Authors:** Yiqun Zhao, Jiachen Xu, Yihao Zhi, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23659v1)

**Summary:** A 3D asset admits multiple valid part decompositions, while semantics-aware segmentation should reflect both the desired granularity and the parts a user wants to extract. Ideally, a practical segmentation   model should strive for a simple principle: what you ask for is what you get. However, realizing this goal is hindered by two core obstacles: the lack of multi-granularity training data and the absence of a   holistic control mechanism. We propose FLEXPART, a unified framework for text-contr...

---

### 16. A Language-Informed Loss for Visual Generation

**Authors:** Suchir Agarwal, Keshigeyan Chandrasegaran, Ziyu Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23653v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23653v1)

**Summary:** End-to-end visual generation with pixel-space loss has recently achieved competitive performance without the need for learned image tokenizers. In this work, we study whether language-informed supervision can provide a richer training signal than pixel loss for visual generation. We introduce LILIE (pronounced "lily"), a Language-Informed and Lossless Image Encoder. LILIE is an invertible image transform trained such that a vision-language model can recover captions from noised features. The enc...

---

### 17. Diversity Without Labels: Task-Agnostic Coreset Selection Across Perception and Action

**Authors:** Julia Hindel, Benjamin Ramtoula, Kyuhwan Yeon, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23642v1)

**Summary:** While data collection for model training is relatively easy, curating high-quality datasets from large collections is inherently challenging. Coreset estimation methods address this problem by identifying the best data subsets to train models on. However, existing approaches often require proxy model training, extensive annotations, or task-specific tailoring. Unsupervised alternatives typically exploit geometric properties in foundation model feature spaces, but are limited to pairwise image-to...

---

### 18. Stereo LWIR-RGB Automatic Labeling for Low-Light Camera-Based VRU Detection

**Authors:** Dimitrios Bouzoulas, Pyry Jäppinen, Pejman Habibiroudkenar, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23621v1)

**Summary:** VRU detection in low-light conditions is a key component in ensuring VRU safety during the most collision prone time of the day. Currently, advances in low-light detection are limited due to the lack of large scale datasets and automated labeling methods. Most autolabeling methods use RGB detections as their labels source, which cannot be replicated in low-light conditions. To fill this gap in this paper we present an automated pipeline for low-light VRU labeling. We use LWIR-RGB image pairs and...

---

### 19. Not Every Mention Is a Claim: Rethinking Object Hallucination Detection in Vision-Language Models

**Authors:** Hsin-Ling Hsu, Neeraja Kirtane, Kuan-Hao Huang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23610v1)

**Summary:** Object hallucination in vision-language models (VLMs) is usually measured by checking each object a caption names against the image. Most benchmarks and detectors alike treat every object mention as a claim that the object is present. This assumption fails when a caption names an object without asserting it, as in "a bench for people to sit on", which mentions people without claiming that any are in the image. We call such mentions non-assertive. Treating them as hallucinations inflates the erro...

---

### 20. ADA 2025: A Multimodal Dataset for Water-Deficit Stress Detection in Sugar Beets

**Authors:** Piper Powell, Robert Franz, Amos Smith, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23609v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23609v1)

**Summary:** Research and development into artificial intelligence (AI) and machine learning (ML) applications in crop management are hindered by a lack of suitable public datasets. Whereas applications in disease and pest detection benefit from a comparatively higher amount of available data, applications like water-deficit stress detection often have very few if any public datasets available. Moreover, most datasets that are available are single-modality and frequently RGB-only, leaving the early detection...

---

### 21. Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable

**Authors:** Mengtan Zhang, Yuchuan Cui, Yu Ma, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23600v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23600v1)

**Summary:** Self-supervised monocular depth estimation is appealing for its potential to scale with unlabeled data, yet existing methods often degrade when trained on diverse scenes. This study finds that, under self-supervision, models tend to encode dataset-specific structural biases rather than transferable scene geometry, leading to cross-domain optimization conflicts. To address this issue, this study proposes the MaSS framework, aiming to make self-supervised depth learning scalable to diverse data. M...

---

### 22. SemPurify: Semantics-Aware Data Purification for Black-box Backdoor Defense

**Authors:** Jiawei Yu, Syed Irfan Ali Meerza, Yi Wu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23589v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23589v1)

**Summary:** Backdoor attacks have emerged as a critical security threat in machine learning, where adversaries embed triggers within poisoned training samples to manipulate a model's predictions on targeted inputs while leaving its general behavior unaffected. This stealthy nature makes backdoor attacks difficult to detect, as the model functions normally until activated by a specific malicious trigger. Current purification-based defenses use image transformations (e.g., blurring) to disrupt trigger pattern...

---

### 23. Enhancing RAG-based Medical VQA with Gated Multimodal Representations

**Authors:** Daniela Jimenez-Pano, Hugo Jair Escalante, Delia Irazú Hernández-Farías

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23588v1)

**Summary:** Medical Vision-Language Models (Med-LVLMs) have shown strong performance in Medical Visual Question Answering (MVQA), yet they may still produce factually inconsistent responses. Retrieval-Augmented Generation (RAG) can mitigate this issue by incorporating external clinical evidence; however, retrieval is often guided by a single modality, potentially overlooking the joint semantics of medical images and clinical questions. We introduce a multimodal RAG framework that learns a joint query repres...

---

### 24. CLEAR: Cooperative Latent Flow for Visual Counterfactual Explanations with Accurate Region Preservation

**Authors:** Yan Zeng, Changlu Guo, Oskar Kristoffersen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23577v1)

**Summary:** Visual counterfactual explanations (VCEs) should alter a classifier's prediction while remaining realistic and preserving decision-irrelevant content. Image-space methods provide high-quality counterfactuals but are computationally costly, whereas latent-space methods are more efficient but often less faithful. We identify two sources responsible for this gap. First, latent generation recovers a natural sample from a perturbed representation, whereas classifier guidance pushes it toward a target...

---

### 25. From Adult Renal Masses to Pediatric Wilms Tumors: Evaluating Cross-Domain Generalization of Kidney Lesion Segmentation on MRI

**Authors:** Sarah de Boer, Myrthe A. D. Buser, Hartmut Häntze, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23568v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23568v1)

**Summary:** Deep learning segmentation models for pediatric oncology are often trained on small, single-center cohorts, whereas much larger datasets exist for adult diseases, such as kidney cancer. Whether models trained on adult renal lesions generalize to pediatric Wilms tumors remains unclear. We trained a segmentation model on single-sequence T1- or T2-weighted adult kidney MRI and evaluated it on a held-out adult test set and a pediatric Wilms tumor cohort, where it was compared with a pediatric-specif...

---

### 26. LiveSync: Iterative Self-Training for Lip-Sync Generation

**Authors:** Huaishao Luo, Huan Zhang, Guanbo Bao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23558v1)

**Summary:** Audio-driven lip synchronization aims to match target speech through localized mouth and jaw articulation while preserving subject identity, head pose, and surrounding facial context. Naturally recorded videos provide synchronized reconstruction targets but rarely offer pairs that are matched in identity and pose yet differ primarily in speech-related articulation. Mask-based training enables reconstruction from these videos, but random-reference inputs differ from the aligned self-reference use...

---

### 27. Execution Before Memory: Diagnosing Memory Failures in Video World Models

**Authors:** Weiyang Jin, Jiwen Yu, Sihan Xu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23542v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23542v1)

**Summary:** A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the sc...

---

### 28. PanoBench: A Panoptic Occupancy Prediction Benchmark for Autonomous Driving

**Authors:** Yi Feng, Zizhan Guo, Junwu E, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23537v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23537v1)

**Summary:** Panoptic occupancy unifies 3D geometry, semantics, and instance identities, but its development is limited by scarce instance-aware annotations. Existing benchmarks mainly provide semantic labels reconstructed from incomplete sensor observations, while panoptic datasets have limited domain coverage or annotation completeness. We introduce PanoBench, a camera-centric panoptic occupancy prediction benchmark spanning synthetic and real-world driving scenes. It combines PanoBench-CarlaOcc, PanoBench...

---

### 29. PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing

**Authors:** Jingyi Wang, Xiao Lu

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23535v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23535v1)

**Summary:** Recent one-step text-to-image (T2I) models enable efficient image synthesis, opening up new possibilities for interactive Web-based image editing. However, existing one-step editing methods often construct a global transport field through simple vector operations between conditional predictions. While such strong transport can effectively drive the image toward the target semantics, it may be released along unreliable directions or over non-edited regions, leading to structural distortions withi...

---

### 30. ReVision: Reprogramming Image Generators for Dense Visual Perception

**Authors:** Yitong Yang, Yinglin Wang, Xuexin Liu, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23533v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23533v1)

**Summary:** Recent image generators exhibit rich visual priors that can support dense visual perception. However, existing approaches typically encode multiple perception tasks into a shared parameterization, making joint training sensitive to the mixture and weighting of heterogeneous data and prone to cross-task interference. To address this issue, we introduce ReVision, an instruction-conditioned parameter generation framework built on a frozen multimodal understanding model and a frozen image generator....

---

### 31. PONDER: Learning to Generate in the Right Order

**Authors:** Julius Erbach, Dominik Narnhofer, Bernt Schiele, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23531v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23531v1)

**Summary:** We introduce PONDER, a method that learns in which order an image generator should fill in content and which of its earlier predictions to revise. Masked generative models construct a sample by repeatedly filling in subsets of missing variables. The order of these partial predictions determines the context available in subsequent steps and therefore affects the quality of the final sample. Common strategies are to choose the order randomly or based on local confidence estimates. Conditioned on t...

---

### 32. TAN: A Size- and Form-Adaptive Masked-Convolution Encoder for Tissue Graphs

**Authors:** Jan Herschel, Anselm von Gladiss

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23475v1)

**Summary:** Tissue graphs represent histology images as graphs over tissue-conforming superpixels, which keeps homogeneous tissue regions intact instead of cutting them into rectangular patches. To embed superpixels, current encoders crop them to bounding boxes and then pad, resize, or mask them, so background or fill values can leak into the node features. This matters in practice, and especially in medical imaging, where a prediction should depend on the tissue and not on an arbitrary preprocessing choice...

---

### 33. When Evidence Vanishes: Distilling Visual-Evidence Dependency in Medical Vision-Language Models

**Authors:** Qizhen Lan, Yiling Ma, Ruiqi Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23469v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23469v1)

**Summary:** Compact medical vision-language models (VLMs) can answer clinical questions correctly without reliably using the image, relying instead on question wording or learned priors. Standard knowledge distillation copies a teacher's answer preference on the original image, but it leaves unchecked whether that preference is conditional on the visual evidence required by the question. We study this missing target as medical visual evidence dependency: support for the correct answer should decrease when t...

---

### 34. TriINR: Unsupervised Atmospheric Turbulence Mitigation with Triple Implicit Neural Representations

**Authors:** Yuka Ogino, Rikuto Otsuka, Yuho Shoji, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23454v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23454v1)

**Summary:** Atmospheric turbulence degrades image quality in long-range imaging. The degradation is generally modeled with two spatio-temporally varying components, tilt and blur. Recent unsupervised turbulence mitigation methods have demonstrated the effectiveness of representing a sharp image as an implicit neural representation (INR). However, their tilt and blur representations remain frame-dependent, and the number of optimization parameters grows with the number of input frames. To address this limita...

---

### 35. ShadowCast: On-the-Fly Context-Aware Shadow Augmentation for Remote Sensing Image Segmentation

**Authors:** Yechan Kim, Dongho Yoon, Jongmin Joo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23440v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23440v1)

**Summary:** Shadows cast by elevated objects alter the spectral appearance and obscure the boundaries of objects in remote sensing images, thereby degrading semantic segmentation performance. Most existing approaches handle shadows as degradations to be detected and removed, requiring additional costs from dedicated networks and shadow-specific annotations. We propose ShadowCast, which takes the opposite approach: it synthesizes shadows and injects them during training for remote sensing segmentation. It ex...

---

### 36. Momentum: Persistent Dynamics for Video World Models

**Authors:** Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23423v1)

**Summary:** Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears. Existing approaches rely on observation history, static point clouds, or image caches constructed from past frames. These representations are often expensive and, more importantly, cannot update dynamic scene content outside the field of view: generated vehicles and pedestrians may be forgotten after leaving the field of view or reappear in physically...

---

### 37. mmPencil: Toward Writing-Style-Independent In-Air Handwriting Recognition via mmWave Radar and Large Vision-Language Model

**Authors:** Yifan Guo, Zhu Wang, Qian Qin, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23419v1)

**Summary:** In-air handwriting recognition based on radio frequency (RF) signals offers a promising solution for human-computer interaction, yet existing methods are often limited by predefined writing planes, constrained writing styles, and small recognition vocabularies. To address these limitations, we propose m^2VLMs, a modality mapping architecture that bridges millimeter-wave (mmWave) radar sensing and large vision-language models (VLMs), and develop mmPencil, a 3D in-air handwriting word recognition ...

---

### 38. GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation

**Authors:** Cheng Fan, Han Wu, Tingzhang Luo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23416v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23416v1)

**Summary:** Multimodal Large Language Models (MLLMs) have significantly advanced instruction-driven perception through the "Embedding-as-Mask" paradigm. However, extending this capability to Remote Sensing (RS) reasoning segmentation remains exceptionally challenging under cluttered geographical contexts and extreme scale variations, often leading to Spatial Fidelity Degradation and Target Misidentification. We identify a critical yet underexplored bottleneck: the sequential alienation of the segmentation t...

---

### 39. Can We Use Saliency Maps for the Evaluation of Generative Image Models?

**Authors:** Eleonora Ristori, Luca Bindini, Marco Lippi, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23411v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23411v1)

**Summary:** Evaluating generative image models remains challenging, as commonly used metrics depend on fixed pretrained feature extractors optimized for different tasks that do not always align with human realism perception across datasets and model families. To address this limitation, we investigate a human-inspired evaluation framework that avoids representations learned for unrelated tasks. Specifically, we train a generator-specific classifier to distinguish real images from samples produced by a given...

---

### 40. LithoWorld: An Endpoint World Model for Lithography Process-Window Recovery

**Authors:** Botong Zhao, Fang Yu, Xinyuan Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23408v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23408v1)

**Summary:** Lithography process drift can move a fabricated pattern outside its process window, producing unqualified scanning electron microscopy (SEM) morphology. We present LithoWorld, an endpoint world model for SEM-guided parameter recovery. Interior representative targets jointly determine qualified reference appearance and correction supervision. A causal predictive branch aligns currentimage features with endpoint representations, while a conditional flow policy generates a two-dimensional correctio...

---

### 41. FloodVLM-Pix: Language-Guided Pixel-Level Flood Understanding

**Authors:** Chengyang Zhang, Zhihao Wang, Zhiyu Long, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23377v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23377v1)

**Summary:** As climate change intensifies, floods are becoming more frequent and destructive, making accurate flood understanding an urgent priority. However, existing vision-language models perform poorly on flood-related tasks, suffering from attentional bias and inaccurate descriptions of flood magnitude. To bridge this gap, we construct the first large-scale remote sensing flood multi-modal benchmark that supports language-level flood understanding and pixel-level flood segmentation. The benchmark conta...

---

### 42. MOSS-Image Technical Report

**Authors:** MOSI. AI

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23374v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23374v1)

**Summary:** Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system that combines high-fidelity visual synthesis with intent-aware composition. First, we pretrain a 5B single-stream diffusion transformer (DiT) from scratch with a carefully designed recipe, enabling bil...

---

### 43. UniPolar: Joint Image and Polarimetric Restoration under Compound Degradations via Physical Consistency Learning

**Authors:** Yang Jin, Guangyu Guo, Linghao Shen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23360v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23360v1)

**Summary:** Polarimetric image restoration aims to recover polarization angle images and reliable polarimetric quantities from degraded observations. Beyond visual fidelity, it also requires preserving the physical relationships underlying reliable polarimetric estimation. However, existing methods typically address either device- or environment-induced degradations in isolation, limiting their applicability to color polarization filter array (CPFA) imaging, where both often coexist. Such compound degradati...

---

### 44. STC-MGNet: Spatial-Temporal-Channel Attention-Enhanced Multimodal Graph Network for Pedestrian Intention Prediction

**Authors:** Yuanzhe Li, Meng Wang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23356v1)

**Summary:** Accurate prediction of pedestrian crossing intentions plays a critical role in enhancing the safety of pedestrian-vehicle interactions in autonomous driving. However, effectively capturing subtle spatiotemporal patterns in pedestrian pose sequences and integrating complementary visual and ego-vehicle motion information remain challenging. This paper proposes a spatial-temporal-channel attention-enhanced multimodal graph network (STC-MGNet) for pedestrian crossing intention prediction. STC-MGNet ...

---

### 45. TransNSNet: A Transformer-Enhanced Multi-Scale Adversarial Framework for CT-to-PET Image Synthesis

**Authors:** Shaojun Li, Xiaoyu Deng, Ikuo Keshi

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23325v1)

**Summary:** This study investigates CT-to-PET image synthesis using TransNSNet, a Transformer-enhanced multi-scale adversarial framework. A paired CT-PET dataset was curated from the public non-small cell lung cancer (NSCLC) Radiogenomics collection through patient screening, slice-level matching, preprocessing, and patient-level train-test separation. The proposed framework generates PET-like predictions at multiple spatial scales and applies coarse-to-fine reconstruction supervision, while TransPatchGAN i...

---

### 46. CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models

**Authors:** Eunju Park, Uiwon Hwang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23324v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23324v1)

**Summary:** Large Vision-Language Models (LVLMs) repeatedly process hundreds of visual tokens across decoder layers, incurring substantial computation and memory costs. Existing inference-time visual token pruning methods often irreversibly remove low-ranked tokens, although the set of visual tokens receiving high query-conditioned attention can change across decoder depth. Recoverable routing preserves skipped tokens for later reconsideration, but re-admits them with stale representations after bypassing i...

---

### 47. Look, Reason, Draw a Region: Recursive Refinement for Spatial Context Prediction

**Authors:** Wajeeha Tahir, Anna Tegon, Lionnus Kesting, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23302v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23302v1)

**Summary:** Spatial context prediction requires visual grounding and spatial reasoning to identify vacant regions relative to objects in a scene. Spatial relationships and physical constraints remain challenging for large vision-language models (VLMs). Recursive reasoning has demonstrated strong performance on discrete and abstract reasoning tasks, motivating its use for improving spatial context prediction in natural images. Weight sharing enables higher accuracy with a small trainable parameter count. We ...

---

### 48. FlashReFocus: Interactive Image Refocusing in Seconds

**Authors:** Ching-Heng Cheng, Chia-Ming Lee, Ming-Ching Chang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23297v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23297v1)

**Summary:** Single-image refocusing changes the focal plane and depth of field of a photograph after capture. It is inherently interactive: users try many focal points and blur strengths on one image, so each edit should be fast and change only the blur. Recent generative methods, however, rerun large diffusion models for every edit. We observe that the two sub-problems differ in kind: recovering the all-in-focus image is ill-posed and needs a generative prior, whereas rendering blur is largely determined b...

---

### 49. The Optimal Ranking Tradeoffs Between Two Ranking Scores in Two-Class Classification

**Authors:** Sébastien Piérard, Adrien Deliège, Marc Van Droogenbroeck

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23294v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23294v1)

**Summary:** The accuracy, true negative rate (negative class recall), true positive rate (positive class recall), negative predictive value (negative class precision), positive predictive value (positive class precision), class-specific intersections over unions, class-specific F-scores, Cohen's kappa, and balanced accuracy are scores that one intuitively wants to maximize when developing machine learning methods. However, they lead to different rankings of such methods. So, how can we establish a ranking t...

---

### 50. I2V-DETACH: Source Grounding Detachment for Unauthorized Image-to-Video Generation

**Authors:** Chanhui Lee, Yeonghwan Song, Yewon Kang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23287v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23287v1)

**Summary:** Recent diffusion models have advanced image-conditioned video generation, but their accessibility raises risks of unauthorized manipulation. Image immunization has emerged as a promising defense for Image-to-Video (I2V) protection, yet existing methods often rely on degrading visual quality or temporal coherence. In this work, we revisit I2V immunization as reducing source-content preservation, shifting the focus from output degradation to weakening source-conditioned content propagation. To thi...

---

## cs.LG

**50 papers**

### 1. Behavioral Couplings: From Formation to Behavioral Emergence in Language Models

**Authors:** Dongyoon Hahm, Woogyeol Jin, Dennis Wei, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23847v1)

**Summary:** Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is...

---

### 2. Task-aligned spectral inductive biases in parameterized quantum circuits

**Authors:** Felix Frohnert, Adrián Pérez-Salinas, Sebastian Lange, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23834v1)

**Summary:** Parameterized quantum circuits are widely investigated in quantum machine learning, yet how their architecture can provide task-aligned inductive biases remains poorly understood. We study data reuploading quantum circuits with two distinct inputs: a signal that varies between samples and a fixed, task-defined spectral query that specifies how the signal should be probed. We show that encoding the query can change the circuit's hypothesis class over the signal by modulating how its existing sign...

---

### 3. Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation

**Authors:** Shaoang Li, Yanhang Shi, Yufei Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23831v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23831v1)

**Summary:** A reasoning trace can accompany a correct answer without providing effective supervision for a particular student. We study how to construct traces that improve learning beyond answer-only supervision by considering both their intermediate content and their accessibility to the target learner. We introduce ReDiST, a student-conditioned trace-construction and distillation framework for evidence-rich reasoning. Starting from the student's own attempts, ReDiST revises answer-correct drafts against ...

---

### 4. Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation

**Authors:** Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23830v1)

**Summary:** A planner with a fixed budget of preventive help must decide whom to help and when. Waiting reveals risk but removes intervention opportunities as higher-risk individuals leave first. We characterize this tradeoff under repeated noisy signals and risk-dependent attrition: in the canonical model, a length-$τ$ observation prefix identifies exactly the latent risk moments $m_j=\mathbb E[p^j]$ for $j=0,\ldots,2τ-1$, buying two new moments per additional period. These identify average next-period att...

---

### 5. Quality-of-Transmission Estimation in Quantum Networks: Compute, Simulate, or Learn?

**Authors:** Anis Bekri, Amar Abane, Van Sy Mai, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23827v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23827v1)

**Summary:** Future quantum networks will rely on control-plane decisions such as routing, scheduling, entanglement provisioning, purification, and memory allocation. Each decision depends on a timely and reliable estimate of the quality of the entanglement that a candidate path can deliver, with end-to-end fidelity as a central metric. Inspired by the optical-networking experience with quality-of-transmission (QoT) estimation, this article asks when a quantum controller should compute fidelity analytically,...

---

### 6. ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference

**Authors:** Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23825v1)

**Summary:** The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. $χ^2$. While versatile, the evidence is notoriously difficult to compute, even when the likelihood is available. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate s...

---

### 7. Learning without relearning physical symmetry: an SO(3)-equivariant convolutional network (CNN) on the sphere

**Authors:** Joshua Williamson, Niall Jeffrey, Lorne Whiteway

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23821v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23821v1)

**Summary:** Many of the most important datasets in the physical sciences live natively on the sphere, and these data often carry no preferred position or orientation. Using methods that do not reflect this symmetry leads to far higher simulation requirements, which can be catastrophic for scientific analyses (forcing reliance on cheap, imperfect models that bias results). We present a novel spherical implementation of a gauge equivariant mesh architecture that is specifically designed for the Hierarchical E...

---

### 8. CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning

**Authors:** Tianmeng Hu, Biao Luo, Ke Li

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23820v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23820v1)

**Summary:** Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design task by decomposing it into smaller sub-problems, each solved collaboratively by multiple agents. This approach reduces the complexity of the problem and improves the exploration of ...

---

### 9. Learning Personalized Memory Gating from Delayed One-Sided Feedback

**Authors:** Kaixuan Ji, Zixiang Chen, Wenting Zhao, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23812v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23812v1)

**Summary:** Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse. In this paper, we study memory gating at the fact level. We first propose a retrieval-based labeling strategy that labels each fact by whether it is later retrieved and incorporated into responses. We then formulat...

---

### 10. Explainable Machine Learning Analysis of Temperature Effects on Mechanical Strength of Fiber-Reinforced High-Performance Concrete

**Authors:** Jagaran Chakma, Zhiguang Zhou, Badhan Chakma, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23811v1)

**Summary:** Predicting the compressive strength of fiber-reinforced high-performance concrete subjected to temperature exposure is challenging because to the intricate interdependencies of mixture composition, fiber properties, curing conditions, and temperature. A data-driven framework to predict compressive strength utilizing 1,204 experimental records containing a diverse array of material designs and exposure situations. This study evaluates eight machine-learning models and demonstrate that ensemble ap...

---

### 11. Task-aware Kernel Stein certificates for Rényi differential privacy

**Authors:** Leoni Carla Wirth, Tara Trautwein, Gesine Reinert

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23798v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23798v1)

**Summary:** Rènyi differential privacy, based on Rènyi divergence, has become a notion of choice for privacy guarantees. However, outside the Gaussian setting, Rènyi divergence can be difficult to compute. In particular, Rènyi differential privacy guarantees that exploit task-specific information, as in Rènyi Pufferfish privacy, can be challenging. Here we use kernel Stein discrepancies based on escort distributions to provide certificates for Rènyi differential privacy. By designing the kernel to focus on ...

---

### 12. Parametric Resonance in Primal-Dual Learning for Slowly Non-Stationary Constrained MDPs

**Authors:** Maxime Baelde

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23788v1)

**Summary:** Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitivity oscillates, a coherent modulation carries no resonant forcing at any depth: the dual update's st...

---

### 13. Sampling the XY model with an attention-based neural network

**Authors:** Piotr Białas, Christian D. Morales, Tomasz Stebel, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23783v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23783v1)

**Summary:** We present a transformer-based variational autoregressive network for sampling lattice systems with continuous degrees of freedom and apply it to the two-dimensional XY model near the Berezinskii-Kosterlitz-Thouless transition. The architecture is combined with physics-informed ingredients: locality-informed attention and approximate probabilities. The resulting sampler significantly outperforms existing neural samplers. We train the model on lattices up to $96\times96$, verify with a mode-dropp...

---

### 14. Mesoscopic learning dynamics of extensive-width neural networks

**Authors:** Shu Zhou, Jean Barbier, Sebastian Goldt

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23779v1)

**Summary:** Understanding how stochastic gradient descent learns internal representations in wide neural networks trained on rich target functions is a central problem in machine learning. We study this question in two-layer neural networks learning target functions represented by networks of the same architecture, with arbitrary nonlinearity, and with network width and input dimension growing proportionally. In this regime, standard approaches for describing the learning dynamics require tracking a divergi...

---

### 15. Logic-Guided Graph Denoising Diffusion Models

**Authors:** Samuel Cognolato, Luciano Serafini, Alessandro Sperduti, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23766v1)

**Summary:** Graph diffusion models are competitive approaches for generating complex graph-structured data. However, when such distributions have strict structural constraints, diffusion models may fail to capture them exactly, resulting in the generation of invalid graphs. In this paper, we propose a method for grounding graph diffusion models in domain-specific knowledge via First Order Logic (FOL), leveraging its expressive and interpretable formalism to impose structural constraints on the generative pr...

---

### 16. Universal Semantic Enhancement for Weakly Supervised Anomaly Detection

**Authors:** Siyu Zhou, Yuqin Xie, Hao Yuan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23765v1)

**Summary:** Weakly supervised anomaly detection on tabular data is an essential task in many label-scarce applications, since tabular data is widely encountered and it is commonly observed in practice that only a limited number of labeled anomalies are available alongside abundant unlabeled samples. Most existing methods try to learn features that capture the inherent distribution patterns in the target domain. However, such features often struggle to provide a complete description of possible abnormal char...

---

### 17. From Flow-Box Invariants to Global Conservation Laws: Machine Learning-Assisted Detection of Singularities and Near-Integrability

**Authors:** Jimmie Adriazola, Ioannis G. Kevrekidis, Panayotis G. Kevrekidis, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23760v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23760v1)

**Summary:** Conservation laws reveal invariant structure in dynamical systems and constrain their evolution to lower-dimensional level sets. Locally, however, per the flow-box theorem, every $d$-dimensional system generically admits $d-1$ functionally independent conservation laws near a regular point even though, generically, only a few such laws persist globally. Data-driven methods typically learn conservation laws on a prescribed region of phase space from which training samples are drawn, leaving their...

---

### 18. LagNet: Lag-Structured Operators for Long-Term Time Series Forecasting

**Authors:** Zhenan Yu, Guangxin Jiang, Jiuyun Jiang, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23735v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23735v1)

**Summary:** Long-term time series forecasting maps a finite history window to an extended future horizon. Many existing models focus primarily on the design of input representations and model structures, while paying less attention to the structural form of the history-to-future forecasting operator itself. We examine this operator directly and find that, across model families, sensitivity matrices exhibit recurring diagonal patterns whose diagonals correspond to relative temporal lags. Motivated by this ob...

---

### 19. Bridging the Language Gap in Scholarly Data II: Enhancing Gender Inference for Chinese Names

**Authors:** Lisette Espín-Noboa, Mingrong She, Ana Maria Jaramillo, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23734v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23734v1)

**Summary:** Perceived gender inference from names is important for inclusive scientometrics research, yet existing methods perform poorly on non-Western scholars. We address this gap for Chinese names, which appear in two forms, Hanzi and Pinyin, its Romanized form (e.g., Zhang Wei, Li Na). In international bibliographic records, names are often available only in Pinyin. However, a single pinyin name can correspond to multiple distinct hanzi characters with different gender associations, so gender inference...

---

### 20. Escaping Parameter Space: Tight Generalization Bounds via Representation Quality

**Authors:** Niclas Göring, Shuofeng Zhang, Branton DeMoss, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23729v1)

**Summary:** We derive a tight generalization bound for deterministic neural We derive a tight generalization bound for deterministic neural networks based on their last hidden layer representations. By evaluating representation quality with a parameter-free $k$-nearest-neighbor ($k$-NN) classifier, our certificate avoids traditional parameter-space complexity measures, KL divergences to a posterior, weight norms, and compression. The bound is tight: trained from scratch, it reaches an 8.0 percentage point g...

---

### 21. ECG-SDI: Single-lead Electrocardiogram Enables Continuous Sleep Depth Index Profiling and Scalable Digital Biomarkers for Sleep Health

**Authors:** Donglin Xie, Qingshuo Zhao, Songchi Zhou, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23727v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23727v1)

**Summary:** Conventional sleep staging provides a coarse-grained representation that obscures within-stage depth variation. We developed ECG-SDI, a single-lead electrocardiography (ECG) framework for continuous sleep-depth profiling and digital biomarker extraction. Using 12,392 overnight polysomnographic recordings, we trained and validated a two-stage deep learning model supervised by conventional sleep-stage labels. Correlations with ordered stages excluding rapid eye movement (REM) sleep were 0.828 in t...

---

### 22. Neural Expansion: A Unified Mechanism for How Deep Neural Networks Generalize

**Authors:** Chashi Mahiul Islam, Samuel Jacob Chacko, Mao Nishino, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23716v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23716v1)

**Summary:** Deep neural networks demonstrate remarkable generalization despite being highly over-parameterized, challenging traditional statistical learning theories. While several theoretical paradigms such as margin-based bounds, PAC-Bayesian analyses, and neural tangent kernels provide global explanations, they often lack mechanistic insight into how generalization emerges from training dynamics. We introduce Neural Expansion, a unified geometric framework that characterizes generalization through the ex...

---

### 23. Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

**Authors:** Sam Partee, River Stevens, Thierry Damiba, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23707v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23707v1)

**Summary:** A multi-step agent task fails when a single tool it needs is missing, yet the tools an agent may need are too many to list: the roughly 8,200 tools on the platform we study have definitions that together exceed the context window of any model we evaluate. We present Tool Recommendation, a deployed system that gives an agent all of them, hundreds of times more than a typical MCP server exposes, through a fixed interface of three tools. It runs at the gateway between agent and tools, executing eve...

---

### 24. Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2

**Authors:** Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23703v1)

**Summary:** Diffusion-based protein structure prediction models produce all-atom structures in about 200 denoising steps, and that cost has driven a number of few-step samplers. We present Blitz, a few-step distillation framework that uses a geometric noise schedule to distribute steps more evenly across noise scales, then learns those updates through multistep consistency training. Physical steering and target-free candidate selection help reduce the remaining geometric defects at inference. We apply Blitz...

---

### 25. Equivalence testing and run-count design for stochastic machine-learning experiments

**Authors:** Dmytro Knopov, Nadiya Shvai

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23700v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23700v1)

**Summary:** Claims that two training methods perform equally well often rest on a non-significant difference between two or three runs per method. We develop a protocol, with its power theory, for certifying practical equivalence in per-run metrics such as the AUROC (area under the receiver operating characteristic curve). It rests on a two-level (seed x item) variance model separating between-run dispersion from item-level noise. Equivalence within a pre-specified margin is tested by two one-sided tests (T...

---

### 26. Expressivity of IQP Feature-Map Quantum Kernels via Reproducing Kernel Hilbert Spaces

**Authors:** Valeria Repetto, Stefano Melchionna, Romina D'Aurizio

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23692v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23692v1)

**Summary:** Quantum kernels are among the most promising methods in quantum machine learning, providing a natural way to embed data into high-dimensional Hilbert spaces via quantum circuits and capturing non-linear relationships in data. Their learning behaviour is governed by the function class they represent, which is formally characterized by the structure of the associated Reproducing Kernel Hilbert Space (RKHS). However, a theoretical characterization of this function class, and of how it depends on th...

---

### 27. HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation

**Authors:** Manohar Vellala, Soumya Banerjee, Sandip Roy, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23685v1)

**Summary:** Implementing Security Technical Implementation Guide (STIG) controls remains a demanding operating-system administration task. Each natural-language security requirement must be translated into a precise and persistent configuration change. These changes span Secure Shell (SSH) configuration, authentication policy, audit rules, and kernel parameters. Existing benchmarks do not measure whether a model can perform this task on a live system. Code benchmarks evaluate isolated programs without persi...

---

### 28. TriRouter: Sparse-to-Dense Electrode-Space Routing for Robust EEG Motor Imagery Decoding

**Authors:** Ying Zhou,  Yaoxin, Mengting Liu

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23665v1)

**Summary:** Motor imagery brain-computer interfaces require reliable decoding from multichannel EEG, but practical acquisition often yields sparse or corrupted electrode montages. We propose TriRouter, an electrode-space routing framework with discriminative-preservation, mask-robustness, and latent-compensation paths. A validation-calibrated router uses observable channel availability to allocate path contributions, preserving complete-channel discrimination while increasing representation recovery under s...

---

### 29. An Efficient Approach to Beetle Damage Detection of Banana Using Deep Learning

**Authors:** Md. Mehedi Hasan Naeem, Ishtiyak Ahmmad Araf, Md. Arefin Haque Mahir, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23661v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23661v1)

**Summary:** Visible surface damage of banana fruits by Basilepta subcostata (the banana fruit scarring beetle) can reduce their market value. Here, manual inspection of Banana fruits is subjective and difficult to scale. This study presents a lightweight framework based on YOLOv8n deep learning model for locating individual bananas and classifying their visible surface condition as healthy or unhealthy. The term beetle damage in the paper title is used operationally for the locally observed scar-like surfac...

---

### 30. A Language-Informed Loss for Visual Generation

**Authors:** Suchir Agarwal, Keshigeyan Chandrasegaran, Ziyu Chen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23653v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23653v1)

**Summary:** End-to-end visual generation with pixel-space loss has recently achieved competitive performance without the need for learned image tokenizers. In this work, we study whether language-informed supervision can provide a richer training signal than pixel loss for visual generation. We introduce LILIE (pronounced "lily"), a Language-Informed and Lossless Image Encoder. LILIE is an invertible image transform trained such that a vision-language model can recover captions from noised features. The enc...

---

### 31. JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment

**Authors:** Quentin Delfosse, Raban Emunds, Paul Seitz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23650v1)

**Summary:** The Arcade Learning Environment (ALE) has been a cornerstone of Deep Reinforcement Learning research, providing a standardized benchmark for evaluating general agents. However, its lack of native support for object-extraction and environment modification restricts research into evaluating whether agents learn robust causal models or rely on brittle visual heuristics. Furthermore, the ALE's dependence on CPU-based emulation creates a significant bottleneck in modern GPU-accelerated training pipel...

---

### 32. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

**Authors:** Yicheng Chen, Xiaoyun Yu, Hyejeong Song, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23643v1)

**Summary:** Accurate atomistic simulations of materials under electric fields require long-range electrostatics and electrical-response modeling at length scales beyond the reach of conventional first-principles methods. Yet these capabilities remain difficult to reconcile with the scalability of machine-learning interatomic potentials (MLIPs). Strictly local models enable efficient spatial parallelization but neglect long-range interactions, whereas existing electrostatic extensions introduce global depend...

---

### 33. No-Regret Language Generation

**Authors:** Jiaxun Li, Vinod Raman, Ambuj Tewari

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23641v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23641v1)

**Summary:** We introduce no-regret generation, which requires a generator to make a sublinear number of mistakes uniformly over all demonstration sequences and compatible target languages. We also formulate an agnostic variant that allows arbitrary demonstrations that may not be compatible with any languages. For both settings, we introduce tree-based mistake-forcing dimensions that exactly characterize finite-horizon minimax complexity and establish necessary and sufficient conditions for no-regret generat...

---

### 34. Deep LLM layers expose passage-level context in EEG during silent reading

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23638v1)

**Summary:** In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...

---

### 35. Deconstructing Multi-Task Active Learning: The Paradox of Gradient Conflict and Orthogonal Decomposition

**Authors:** Juho Jung, Seongjae Kang, Jinyoung Han

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23623v1)

**Summary:** Existing multi-task active learning (MTL-AL) methods predominantly rely on linear scalarization of heterogeneous objectives such as uncertainty, diversity, and gradient conflict. We argue that this entangled formulation is fundamentally limited, as linear combination fails to capture Pareto-optimal trade-offs under conflicting objectives. We propose a shift from combination to deconstruction and introduce a principled framework that rethinks MTL-AL along three orthogonal dimensions. First, we id...

---

### 36. GRAFT-EEG: Gauge-Aware Physical Field Transport for Cross-Dataset Motor-Imagery EEG

**Authors:** Ying Zhou, Mengting Liu

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23620v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23620v1)

**Summary:** Cross-dataset EEG decoding often treats montage, reference, and active-sensor changes as representation shift, although they also alter the observation operator. We study target-statistics-blind transfer: fitting receives no target signal, label, or empirical statistic, and electrode coordinates only instantiate a fixed prediction operator. method removes the active-set common-reference gauge and transports each native mask through a template motor leadfield. A source-fitted spectral classifier ...

---

### 37. ThetreStageAI: Multi-View Retrieval-Augmented Generation for Structured Bengali Theatre Production Planning

**Authors:** Md. Mehedi Hasan Naeem, Mst. Kamrunnahar Ruma, Shakila Sultana, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23618v1)

**Summary:** Staging a theatre performance requires coordinating dialogue, actor movement, stage directions, lighting focus, cue timing, and equipment constraints within the same production plan. This work presents ThetreStageAI, a retrieval augmented framework for structured Bengali theatre production planning. Rather than retrieving from one mixed corpus, the system maintains separate scene, actor-blocking, and lighting views. Bengali text is embedded with BGE-M3 and indexed in view-specific Qdrant collect...

---

### 38. The Sign Code: The Hidden Binary Nature of Deep Networks

**Authors:** Niclas Göring, Shuofeng Zhang, Roi Holtzman, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23616v1)

**Summary:** Every neuron in a trained network outputs a number that can be separated into its sign (positive or negative) and its magnitude (absolute size). We call the set of all neuron signs the \textit{sign code}. This raises a key question: does classification depend more on the sign code or on the magnitudes? For overparameterized vision classifiers with sign-preserving activations, the answer is overwhelmingly the sign code. A $k$-nearest neighbor classifier operating only on this binary sign code ach...

---

### 39. Trajectory-Triggered Sparse Collaborative Decoding

**Authors:** Amit Ranjan Trivedi, Sruthikesh Surineni, Kyong Ho Lee, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23613v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23613v1)

**Summary:** Dense assistance methods such as speculative decoding repeatedly verify draft tokens with a target model, keeping target computation coupled to generation. We study sparse collaborative decoding, where a draft model generates most tokens and a target model is invoked only for short corrective segments. The key problem is deciding when to call the target. We show that local uncertainty is a weak trigger: entropy, negative log-likelihood, logit margin, top-$k$ mass, and velocity features give near...

---

### 40. How Many, but How Sure? Class Competition as a Confidence Proxy in Multi-Class Density-Based Counting

**Authors:** Villanelle O'Reilly, Georgios Leontidis, Marc Hanheide

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23611v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23611v1)

**Summary:** Multi-class density estimators can count objects in crowded scenes, but their class-wise outputs offer no indication of how reliably density mass has been allocated. We introduce a training-free confidence proxy based on local competition between the strongest class channels. The resulting prominence measure requires only the predicted density maps, with no retraining or access to model internals. We test whether residual competition is diagnostic of cross-class leakage by attenuating contested ...

---

### 41. When Magnitude Suffices: Reconstructing Time-Domain-Gated Microwave Signals Without Phase on a Thoracic Phantom

**Authors:** Maciej Cichoń, Patrycja Gołaś, Maksymilian Bartosik, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23608v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23608v1)

**Summary:** Time-domain gating separates the arrivals that form a microwave S-parameter measurement. It requires the measurement of complex values, so this application almost always uses a vector network analyzer (VNA). We show that, on one calibrated measurement configuration, the gated magnitude the VNA would give can be reconstructed from a magnitude-only sweep of a spectrum analyzer with a tracking generator (SA). We select the gate center for separability of the measured states, correct each instrument...

---

### 42. Boundary Detection for High-Dimensional Point Clouds

**Authors:** Abigail Hickok, Valerio Galanti, Osama Al Dalahmah, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23590v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23590v1)

**Summary:** We introduce two new methods for boundary detection in high-dimensional point cloud data, intended to work in situations with non-uniform density, high ambient dimension, and substantial noise. Our first method fits a separating hyperplane on local neighborhoods after doing local dimension reduction---this method works best when one can reliably estimate the intrinsic dimension of the data. Our second method measures the directional uniformity of local neighborhoods, and has the best overall per...

---

### 43. BMuon: Budgeting Muon's Spectral Geometry for Structured Compressibility

**Authors:** Rida Assalouh, Tom Jacobs, Rebekka Burkholz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23571v1)

**Summary:** Muon has emerged as a strong optimizer for neural network training and admits an interpretation as steepest descent under a spectral-norm geometry. Yet we find that Muon-trained Transformers can degrade sharply when their MLP hidden channels are pruned after training. To reconcile Muon's optimization performance with structured compressibility, we introduce Budget Muon (BMuon), which modifies Muon's spectral geometry so that hidden channels across blocks compete for a shared allocation budget. T...

---

### 44. A general recipe for data-adaptive anytime-valid envelopes for iterative algorithms

**Authors:** Soham Bonnerjee, Aaditya Ramdas

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23570v1)

**Summary:** Most convergence guarantees for iterative stochastic algorithms are stated at a fixed iteration count and do not justify stopping at a data-dependent time. Recent work has constructed anytime-valid envelopes that do, but deterministic envelopes are typically too conservative for practical stopping, and existing data-adaptive ones are derived case-by-case, each coupling a specific algorithm to a specific noise model and boundary construction. This paper provides a general recipe for constructing ...

---

### 45. Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search

**Authors:** Quynh Trinh, Trung Nguyen, Nam Nguyen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23565v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23565v1)

**Summary:** Monte-Carlo Tree Search (MCTS) typically stores only scalar mean estimates, which makes it poorly suited for tail-risk objectives such as conditional value-at-risk (CVaR). We introduce Categorical Thompson Sampling with Optimism (CATSO) and Particle Thompson Sampling with Optimism (PATSO), two distributional MCTS algorithms that maintain finite-support empirical backup laws at Q-edges. CATSO represents Q-edge laws with categorical atoms and Dirichlet Thompson sampling, while PATSO represents the...

---

### 46. Beyond Latent Personalization: Integrating HRV-Conditioned Personalization via LLM for Interpretable Stress Detection

**Authors:** Wei-Hsiang Ma, Ya-Tse Wu, Hsing-Hang Chou, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23555v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23555v1)

**Summary:** Stress detection based on heart rate variability (HRV) has received increasing attention. However, existing personalized approaches integrate personal attributes with HRV through latent representations, limiting the interpretability of their interactions. In this work, we propose an LLM-enhanced personalized stress detection framework that integrates HRV features and personal attributes through LLM-based semantic interpretation. The proposed framework achieves a 29.9% relative MCC improvement ov...

---

### 47. Causal Discovery beyond Conditional Independence: Identifiability, Algorithms, and Statistical Inference for Directed Acyclic and Cyclic Graphs

**Authors:** Yang Ni

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23543v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23543v1)

**Summary:** Learning causal structure from data requires assumptions about mechanisms, noises, observation schemes, and interventions. Historically, causal discovery has relied primarily on conditional independence. This review focuses on modern causal discovery methods that exploit properties of distributions beyond conditional independence. Our organizing principle separates the source of identification from the statistical estimator and its computational implementation. This perspective connects conditio...

---

### 48. Out of Support, Not Out of Reach: In-Context Learning with Unsupported Instructions and Composed Tasks

**Authors:** Xuhan Tong, Yuchen Zeng, Jiawei Zhang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23528v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23528v1)

**Summary:** In-Context Learning (ICL) enables pretrained LLMs to adapt to downstream tasks from a small set of input-output demonstrations, without parameter updates. Yet existing theory primarily explains ICL as identifying a latent task already represented in pretraining, leaving unclear whether ICL can succeed when either the instruction or the target task falls outside the pretraining support. We develop a theoretical framework under mild assumptions that separates these two forms of distribution shift....

---

### 49. Interpreting SSL Representations for Spoof Detection: a WavLM Study

**Authors:** Mohamed Mallat, Michele Panariello, Massimiliano Todisco, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23526v1)

**Summary:** Self-supervised speech models such as WavLM achieve strong spoofing detection performance, yet which layers encode the most spoof-relevant information and what acoustic properties they capture remain opaque. We present a layer-wise interpretability study of WavLM using the ASVspoof 5 database, combining three complementary analyses: (i) per-layer linear probing with attack-level evaluation across speech synthesis, voice conversion, and adversarial attacks; (ii) a canonical correlation analysis (...

---

### 50. Uncertainty-aware AI-enabled framework for predicting hydrogen dispersion in confined spaces to enhance operator situational awareness

**Authors:** Niclas Flehmig, Mary Ann Lundteigen, Shen Yin

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23515v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23515v1)

**Summary:** We present a two-stage AI-enabled framework for enhancing operator situational awareness during compressed hydrogen bunkering in maritime confined spaces. In the event of a leak, the framework first estimates the unknown leakage rate from early sensor readings and then forecasts how the hydrogen cloud will disperse over the next time steps, providing operators with a predicted concentration map together with confidence bounds. The framework is based on two independent AI models building one AI s...

---

## cs.NE

**50 papers**

### 1. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

**Authors:** Takashi Ishida, Taro Makino, Issa Sugiura

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23470v1)

**Summary:** Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to target, comparing diverse, well-reasoned options can be more useful than a single ...

---

### 2. Algorithm Modelization: Transforming Optimization Algorithms into Evolvable Intelligence

**Authors:** Jian Yao, Zhiyao Zhang, Yichen Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23161v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23161v1)

**Summary:** Can algorithms be learned and evolved as models, rather than repeatedly redesigned as programs? We explore this question by introducing Algorithm Modelization, a new paradigm that turns iterative algorithms into trainable models. Its central idea is to regard algorithm execution trajectories as computational experience: by learning how algorithmic states evolve over iterations, a model can internalize the knowledge embodied in existing algorithms, reproduce their computational behaviors, and fur...

---

### 3. Wavelength Diversity Expands the Expressive Power of Optical Computing

**Authors:** Shiqi Chen, Che-Yung Shen, Parnian Ghapandar Kashani, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23070v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23070v1)

**Summary:** Universal function approximation underpins neural networks' capacity to represent nonlinear relationships, but realizing this capability in optical hardware requires engineering the computational features encoded in light. Here, we show that wavelength diversity enhances optical function-approximation expressivity through wavelength-scaled Fourier features generated by a shared phase encoder, without increasing the number of input-encoded harmonics. Multiple wavelengths contribute to the represe...

---

### 4. SpikeQ: Spike-Guided Post-Training Quantization for Spiking Neural Networks

**Authors:** Kai Sun, Peibo Duan, Zhanglu Yan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23046v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23046v1)

**Summary:** On neuromorphic chips, spiking neural networks (SNNs) consume far less energy than artificial neural networks (ANNs), but the limited memory of these chips requires low-bit synaptic weights and membrane potentials. Existing post-training quantization (PTQ) methods provide them without retraining and, like those for ANNs, minimize numerical errors such as the mean squared error (MSE). In an SNN, however, a quantization error reaches later layers only through the spikes it flips. We find that erro...

---

### 5. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 6. A restart rule for genetic algorithms based on Schnabel census

**Authors:** Anton Eremeev, Yulia Zakharova

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22211v1)

**Summary:** A new adaptive restart rule for Genetic Algorithms (GAs) is considered. The rule is based on the Schnabel Census method, originally developed for statistical estimation of a size of animal population. In this paper, the Schnabel Census method is applied as a heuristic to estimate the number of different solutions that may be visited with positive probability, given the current distribution of offspring. The rule consists in restarting a GA as soon as the maximum likelihood estimate reaches the n...

---

### 7. Attention over noisy examples: generalization and memorization in the exponential Hopfield network

**Authors:** Francesco Alemanno

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22191v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22191v1)

**Summary:** In Hebbian learning from examples a Hopfield network of $N$ neurons is not supplied with the $K$ archetypes it has to retrieve but with $M$ blurred examples of each, of quality $r$, and whether it can infer them depends on the load $α=K/N$ (interference among them) and on the dataset entropy $ρ=(1-r^2)/(Mr^2)$ (how little the examples say about them). We transfer this protocol to the exponential Hopfield model, whose zero-temperature update is a step of softmax attention with the unlabelled exam...

---

### 8. Beyond the Hamming Cliff: Compact Spatial Encodings Preserving Semantic Distance in Spiking Neural Networks

**Authors:** Sergio Davies, Muhammad Aitsam, Morgan-Tyler Stone, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22083v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22083v1)

**Summary:** By pre-processing input signals with Gray, Thermometer, Johnson and hybrid encodings before passing them to spiking neural networks running on SpiNNaker hardware, Davies et al.(2025) address the semantic-spatial disparity that causes the ``Hamming cliff'' in standard binary representations. Continuous semantic patterns are presented as a set of simultaneous spikes at the input layer, preserving ultra-low latency processing. Training the network on multiple continuous values under each scheme, an...

---

### 9. Approaching Backpropagation Accuracy with Weight Perturbation on MNIST

**Authors:** Patrick Inoue

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21665v1)

**Summary:** Weight perturbation (WP) estimates learning directions from random parameter perturbations and a scalar change in loss, without backpropagating derivatives. We examine how batch size, training duration, and estimator stabilization affect its attainable accuracy in fully connected MNIST networks. In the shallow configuration, large-batch training reaches approximately 97\% test accuracy, compared with an early backpropagation (BP) reference near 97.5--98\%. The same comparison exposes a substanti...

---

### 10. First Mathematical Runtime Analyses of Evolutionary Multitask Multi-Objective Optimization

**Authors:** Danyang Zhang, Weijie Zheng

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21311v1)

**Summary:** To facilitate the solving of complex problems, evolutionary multitask optimization is regarded as a promising technique due to its capacity for cross-task knowledge transfer. In contrast to empirical evidences, no mathematical runtime support exists for this technique within the domain of multi-objective optimization. In this work, we aim to fill this important gap. We analyze how the representative multiobjective multifactorial evolutionary algorithm (MO-MFEA) covers the Pareto fronts of two bi...

---

### 11. Controlling the latency in temporal coded spiking models for neuromorphic datasets

**Authors:** Alban Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19732v1)

**Summary:** Exploiting temporal information in datasets with high temporal dependencies (such as spoken keyword recognition) by spiking models is still an open problem. Promising frameworks include Time-To-First coding (TTFS) and the inclusion of synaptic delays into learning. In TTFS, neurons are forced to spike at most once, forcing the network to found its learning on the spiking times of neurons rather than their spiking rate. Some models use the TTFS framework to directly compute the spiking time of In...

---

### 12. When the implementation matters more than the algorithm: NSGA-II and other multi-objective optimizers in engineering design tools

**Authors:** Luciano Ambrosini

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.22397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22397v1)

**Summary:** Engineering design tools increasingly embed optimizers as ready-made components that users select by algorithm name, while operator settings and bound, integer and duplicate handling stay fixed inside each tool. This study tests whether the name predicts the result. A tool-agnostic harness exposes one deterministic black box, an emulator of a published 22-variable mixed-integer building-performance problem, to the native optimizers of three Grasshopper plug-ins, to canonical NSGA-II, SMS-EMOA an...

---

### 13. Design and Analysis of Temporal Representations in Neural Networks

**Authors:** Alban Colas-Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19730v1)

**Summary:** The ability to represent temporal information is often hypothesized to underlie the efficiency and learning capabilities of biological neural networks. This motivates the development of spiking neural networks. However, it remains unclear how temporal information is actually represented in neural networks and how different forms of temporal representation affect performance and computational efficiency. We introduce the notion of the degree of temporal representation of a neural network, defined...

---

### 14. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 15. Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine

**Authors:** Thomas Hannagan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19220v2) | 📄 [PDF](https://arxiv.org/pdf/2610.19220v2)

**Summary:** The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Thinking steps are attracting but strongly non-normal maps exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already presen...

---

### 16. Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization

**Authors:** Bum Jun Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18085v1)

**Summary:** We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the m...

---

### 17. Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**Authors:** Francesco Panetta, Federico Di Valerio, Michela Proietti

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17998v1)

**Summary:** Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only expla...

---

### 18. Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation

**Authors:** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17969v1)

**Summary:** Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...

---

### 19. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 20. FidLIF: Parallel Training of High-Fidelity Spiking Neurons with Exact BPTT

**Authors:** Kaixiang He, Yujie Wu

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16924v1)

**Summary:** Although spiking neural networks (SNNs) show promise in energy-efficient computing through event-driven computation and stateful temporal processing, their recurrent membrane dynamics render their training inherently sequential and inefficient for long sequences. Existing methods achieve full-sequence parallelism in SNNs through two main strategies: redesigning or approximating spiking dynamics to avoid reset-coupled temporal dependencies, or relying on iterative relaxed fixed-point solvers that...

---

### 21. Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**Authors:** Huan Luo, Na Lu, Xiaopeng Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16921v1)

**Summary:** Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...

---

### 22. DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning

**Authors:** Yuxiang Zeng, Kun Xie, Yang Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16822v1)

**Summary:** Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...

---

### 23. naspaclust: A hybridisation of spatial fuzzy clustering with nature-inspired optimisation

**Authors:** Bahrul Ilmi Nasution, Rezzy Eko Caraka, Robert Kurniawan

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16356v1)

**Summary:** We present an overview of R package called \texttt{naspaclust}, a tool for spatial fuzzy clustering improvement by hybridising the Fuzzy Geographically Weighted Clustering (FGWC) with nature-inspired optimisation algorithms. There are seven optimisation algorithms in general, namely Artificial Bee Colony, Flower Pollination Algorithm, Gravitational Search Algorithm, Harris-Hawk Optimisation, Intelligent Firefly Algorithm, Particle Swarm Optimisation, and Teaching-Learning Based optimisation. The...

---

### 24. CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization

**Authors:** Yuqing Cheng, Yan Jia, Yanjie Song, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16158v1)

**Summary:** Conflict-graph search can stagnate despite effective operators when interventions fail to address the conflicts blocking progress. A disruptive intervention may also require further search before its value emerges. We propose CIPHEUR, a large language model (LLM)-guided framework that connects conflict evidence to coordinated intervention and recovery through Structured Intervention Units (SIUs). The shared control interface supports offline synthesis of executable policies and online contextual...

---

### 25. Where Polanyi Meets Galois: Tacit Knowing as an Algebro-Deterministic Operation, Toward Re-rooting AI-Generated Science

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16102v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16102v1)

**Summary:** We argue that tacit knowing is better modelled as an operating regime of one memory substrate than as a kind of content. The substrate is VaCoAl, an algebro-deterministic XOR-and-shift hyperdimensional memory over GF(2), realized as CASRAM (commercial SRAM-CAM) and PyVaCoAl (DRAM-CAM).In VaCoAl/PyVaCoAl a directed acyclic graph (DAG) reads two ways. Repairing every collision (Rescue mode) makes the trace exactly auditable but ranks no path higher; tolerating collisions (Don't Care mode) yields a...

---

### 26. How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility

**Authors:** Toru Takahashi

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15830v1)

**Summary:** When several predictions use the same internal representation, information about some targets can remain easier to recover than information about others. We study how this specialization forms, persists, and changes in minimal artificial learners. With reconstruction errors weighted equally during learning, changing which target is observed precisely selects the favored target and redirects an already specialized learner. Removing current support can reduce a formed bias, whereas state-following...

---

### 27. REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming

**Authors:** Abrar Alotaibi, Moataz Ahmed

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15513v1)

**Summary:** Safety-aligned large language models (LLMs) remain vulnerable to adversarial prompts that bypass their safety training. Existing automated red-teaming methods either require privileged access unavailable in production, rely on manually engineered per-model templates, or optimize a single objective without population-level diversity. We present REPRO (Reflective Evolutionary Prompt Optimization), a pure black-box framework that discovers adversarial prompts through evolutionary optimization drive...

---

### 28. CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining

**Authors:** Ziteng Sui, Junfeng Xia, Wenhao Ye, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15450v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15450v1)

**Summary:** Functional magnetic resonance imaging (fMRI) commonly characterizes large-scale brain organization through functional connectivity (FC). However, an observed FC matrix is not a fixed brain graph but a statistical estimate determined by the finite BOLD frames used to compute it. Conventional FC-based approaches typically represent each scan with a single Pearson-correlation matrix, leaving frame-resolved variations in regional interactions unexploited. To address this limitation, we introduce CoF...

---

### 29. FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies

**Authors:** Yifeng Mao, Yuze Feng, Yutong Shen, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15307v1)

**Summary:** Efficient neural architecture search (NAS) requires accurate performance estimation under limited evaluation budgets. Existing zero-cost proxies (ZCPs) provide fast training-free signals, but each proxy usually captures only a partial property of an architecture, leading to unstable rankings across datasets and search spaces. In contrast, GNN-based predictors can improve accuracy, but often depend on labeled architectures, graph encoders, and costly representation learning, which makes them less...

---

### 30. Compute-Optimal Scaling Laws for Spiking Language Models

**Authors:** Dan Saunders, Benjamin Ren, Catherine He

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15146v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15146v1)

**Summary:** Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N...

---

### 31. RELAGRAM: Recursive Latent Graph Model for the Capacitated Vehicle Routing Problem

**Authors:** Vladimir Kirill Bickov, Neil Yorke-Smith

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15106v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15106v1)

**Summary:** Latent recursion repeatedly processes internal representations through the same neural network. Recent work has shown this approach to be effective on structured reasoning tasks such as Sudoku and maze solving. However, whether latent recursion can support neural routing remains unclear. We introduce RELAGRAM (Recursive Latent Graph Model), a novel approach that brings latent recursion to graph combinatorial optimization. RELAGRAM encodes a capacitated vehicle routing problem (CVRP) instance as ...

---

### 32. PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation

**Authors:** Alex Gower

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14409v2) | 📄 [PDF](https://arxiv.org/pdf/2610.14409v2)

**Summary:** Generating an image with a diffusion or flow-matching model typically involves integrating a velocity field for hundreds of sequential steps. That computation suits a GPU poorly and an analog neuromorphic substrate well, where one fast, low-power physical relaxation could replace the whole sequence. Two things are needed: a generative algorithm whose computation is a relaxation, and a way to train it without backpropagation, whose global gradient transport is hard to realise in analog. Energy Ma...

---

### 33. Do Artificial Neural Networks Need Dendritic Nanotubes? Two Reasons for Shrinking Importance Estimates in Continual Learning

**Authors:** Saurav K. Aryal

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.14258v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14258v1)

**Summary:** Regularization-based continual learning protects each parameter in proportion to an estimate of its importance, yet these estimates come from finite samples and heuristics and are used as if they were exact. We report four studies that start from a biologically inspired mechanism and end with a statistical explanation of it. Motivated by dendritic nanotubes, we let transient lateral links diffuse importance tags between hidden units. Links between co-active units gave no significant gain, but ra...

---

### 34. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 35. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 36. REMBGO for Evaluation-Limited Optimization: CEC2022 Benchmarking and EAF-STATCOM Generalization

**Authors:** Vikram Chekuri, Narapareddy Ramarao, Prashanth N A

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13471v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13471v1)

**Summary:** Metaheuristic comparisons are often reported at evaluation budgets far larger than an expensive engineering simulation can afford. This paper presents REMBGO, an evaluation-budget-aware refinement of EMBGO. Its contribution is not any single operator: it is the integration of population preservation, scale-normalized exploration and recovery mechanisms whose parent-relative benefit is concentrated under restricted function-evaluation budgets. REMBGO is evaluated on CEC2022 at a primary, applicat...

---

### 37. The value of information and the emergence of communication in evolved e-puck robots

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13118v1)

**Summary:** We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Em...

---

### 38. Universal Construction and Exact Self-Reproduction in Ternary McCulloch-Pitts Networks

**Authors:** Charles C. Norton

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12251v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12251v1)

**Summary:** A fixed network of McCulloch-Pitts threshold units with weights in {-1,0,1} can hold other threshold networks in its state and run them: the state is a ring of banks of records, each record a unit of a stored network, and each step evaluates one record. We use such a network to carry out von Neumann's universal construction and self-reproduction exactly. As a cellular automaton keeps its rule, the fixed network keeps its weights, and what reproduces is a stored network. A constructor of 143 reco...

---

### 39. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

**Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12183v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12183v1)

**Summary:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their resul...

---

### 40. EliteTable: Self-Improving Program Search for Executable Control Policies

**Authors:** Stuart Farmer

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12536v1)

**Summary:** EliteTable is a self-improving program-search algorithm guided by large language models (LLMs) that uses a fixed-capacity table of high-scoring solutions to guide new proposals, edits of existing solutions, and remixes of several solutions. Performance was evaluated across six Gymnasium control tasks, each with ten generations and fifty candidate slots per generation. Each task was evaluated across ten independently initialized searches. Candidate-score medians rose between the first and final g...

---

### 41. Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating

**Authors:** Lechen Li, Rongye Shi, Wanhuan Zhou

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11546v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11546v1)

**Summary:** Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architectures or fixed switching rules, resulting in disjointed search phases. To address this, this study proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-...

---

### 42. Evolutionary Architecture Search for Chlorophyll-$a$ Prediction in Lakes using Sentinel-2

**Authors:** Kursat Komurcu, Linas Petkevicius

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10496v1)

**Summary:** Small tabular datasets with expert-designed spectral features are the norm in   operational Earth observation, and the networks applied to them are typically   hand-designed. We revisit one such published model -- a Sentinel-2 algal   bloom classifier -- and ask what architecture search adds, holding the task,   the features and the lake-level train/test split of the original study fixed.   Searching an extended multilayer-perceptron space with regularized evolution,   and selecting on inner-cro...

---

### 43. Evolve on the Host, Predict on the Edge: Deploying Online Neuroevolutionary Architecture Search for Cross-sectional Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10038v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10038v1)

**Summary:** Accurate forecasting models are usually large, expensive to update online, and fixed in architecture once trained. We apply ONE-NAS, an online neuroevolutionary architecture search that evolves a population of small recurrent networks as each window of data arrives, to daily cross-sectional stock return prediction, and pilot it on a host and endpoint pipeline: the host runs the search and ships each generation's champion genomes over TCP/IP to a Raspberry Pi 4B, which predicts online. On the Pi ...

---

### 44. The Modular CMA-ES: A Framework for Modern Evolution Strategies

**Authors:** Jacob de Nobel, Diederick Vermetten, Anna V. Kononova, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09699v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09699v1)

**Summary:** Since their introduction, modern evolution strategies, such as the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), have become established as powerful methods for continuous black-box optimization. This success has led to a wide range of proposed modifications, each designed to improve performance or behavior in specific optimization scenarios. However, because these developments have largely been introduced and studied in isolation, their interactions remain comparatively underexplore...

---

### 45. Relocating Nonlinearity: How a Downstream Learner Reshapes What Genetic Programming Must Evolve

**Authors:** Nam H. Le

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09347v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09347v1)

**Summary:** Genetic programming was conceived as a way of evolving solutions: the program is the answer, and fitness is the error of its own output. A substantial line of work instead makes the program an input to a separate learner, so fitness measures the learner's output rather than the program's. Which learner to attach matters, with no account of what decides it. What makes a target hard for genetic programming is how much nonlinearity the program must build by composing primitives; whatever nonlineari...

---

### 46. Evaluating the Transfer of Co-Evolved Communication from 2D to 3D Simulation

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09280v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09280v1)

**Summary:** This work examines the transfer of a co-evolved communication mechanism between two robotic agents from a discrete two-dimensional (2D) simulator to a three-dimensional simulator with real physics (3D). The study focuses on whether a communication mechanism co-evolved in a 2D environment retains its functional role after transfer to a 3D physics-based simulator. To support this analysis, the effects of the episode time budget, the social cue, and the asymmetry between the two co-evolved roles we...

---

### 47. A Connectome Test of the Fly Hashing Algorithm

**Authors:** Sebastian Senge

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.09114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09114v1)

**Summary:** Dasgupta, Stevens and Navlakha (2017) showed that the Drosophila olfactory circuit, modelled as a random sparse projection followed by winner-take-all, is a locality-sensitive hash that beats classical LSH. The projection was random because the wiring was unknown. We test it against four electron-microscopy connectomes (MaleCNS, hemibrain, FlyWire, BANC; four animals, seven hemispheres). First, the 2017 pattern holds in a reimplementation of its protocol on SIFT, MNIST and odour mixtures (GloVe ...

---

### 48. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 49. Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design

**Authors:** Marcus Vukojevic, Erik Nielsen, Veronica Lachi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08367v1)

**Summary:** Several discrete design tasks, such as molecular discovery, require diverse collections of useful candidates at low computational cost. High validity alone does not guarantee a useful candidate library: repeatedly generating the same valid structures leaves few distinct alternatives. Training for both feasibility and diversity is challenging because many relevant criteria can only be evaluated after hard decoding. To address this challenge, we propose EGO (Evolutionary Generators with One-step i...

---

### 50. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

## q-bio.NC

**50 papers**

### 1. Deep LLM layers expose passage-level context in EEG during silent reading

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23638v1)

**Summary:** In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...

---

### 2. Distributional signatures of computation: inferring mechanisms from computation time distributions

**Authors:** Céline van Valkenhoef, Catherine Schuman, Nikolaus Kriegeskorte, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23607v1)

**Summary:** Computational complexity theory provides a framework for analysing abstract models of computation, whereas computational systems operate as finite physical implementations whose behaviour is shaped by their architecture and physical substrate. In such systems, computational organisation cannot be directly characterised from algorithms or internal representations. Building on the use of reaction time distributions to constrain mechanisms in cognitive science, we introduce an empirical framework f...

---

### 3. EEG Lempel-Ziv Complexity vis-à-vis Autocorrelation Function

**Authors:** Pedro Montoya, Ignacio Cifre, José Luis Rosselló Sanz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23231v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23231v1)

**Summary:** Measures of signal complexity have become increasingly popular in electroencephalography (EEG), where they are often interpreted as indicators of neural information processing, dynamical richness, or conscious state. In contrast, classical measures of temporal dependence, such as the autocorrelation function (ACF), remain more directly linked to known physiological mechanisms and are easier to interpret. The present work revisits, for the EEG practicioner, the relation between normalized Lempel-...

---

### 4. What Shapes Brain Alignment of Large Language Models during Dialogue? Insights from Language Production and Comprehension

**Authors:** Yuko Nakagi, Yuya Chiba, Yasue Kishino

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22961v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22961v1)

**Summary:** Brain alignment of large language models (LLMs) offers a way to investigate representational similarities between LLMs and the human brain during language processing. While previous studies have mainly focused on passive language comprehension, little is known about such alignment during dialogue, in which speakers engage in both language production and comprehension. In this study, using fMRI data collected during dialogue, we examine brain alignment during language production and comprehension...

---

### 5. Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies

**Authors:** Yiran Huang, Zeyong Zhang, Bharat Biswal, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22706v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22706v1)

**Summary:** Multimodal large language models (MLLMs) offer scalable annotations of social and affective content, but their temporal agreement with human judgments and neural predictive value require further evaluation. We compared diffusion-based and autoregressive MLLMs with continuous human Theory of Mind (ToM) and affective valence ratings across three short cartoon movies. Behavioral analyses assessed temporally aligned Pearson correlations, rating distributions, and the effects of preceding scene descr...

---

### 6. Alignment of visual brain encoding models with individual perceptual similarity judgments

**Authors:** Daniel Chong, Haomiao Chen, Keith W Jamison, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22569v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22569v1)

**Summary:** Encoding models that predict brain activation responses to images have traditionally been trained to maximize accuracy when predicting observed brain data. However, their internal representations may not reflect individual human perception. In this work, we investigate whether we can fine-tune brain encoding models to better align their representations with individuals' similarity judgments. Using similarity judgments of 100 images from 8 participants in the Natural Scenes Dataset (NSD), we adap...

---

### 7. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 8. Mutual Information in High-Dimensional Neural Coding

**Authors:** Zimo Li, Yuchang Tian, Matthew P. Leighton, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22206v1)

**Summary:** Estimating mutual information in large neural populations is limited by the exponential growth of possible neural response patterns. Here we apply a Monte Carlo framework to make this problem tractable by sampling from a conditionally independent population model fit from single-neuron responses. The estimator accurately recovers analytical ground truth, corrects finite-data bias, and scales to empirical recordings containing 100 to 10,000 neurons from visual cortex, hippocampus, and retina. Acr...

---

### 9. Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression

**Authors:** Nitin Sharma, Sicheng Dai, Francesco A. Mallus, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21660v1)

**Summary:** Normative models chart how brain measures vary across the lifespan, expressing each individual as a deviation from a healthy reference. However, most regional models of cortical thickness disregard dependencies between cortical and subcortical anatomy, and transferring them to a new site typically requires retraining or a recalibration of location and scale alone. We condition lifespan norms of cortical thickness on subcortical volume, such that each deviation indicates whether an individual's c...

---

### 10. Neural Computation Runs on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep

**Authors:** Javier Diaz

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21486v1)

**Summary:** Biological function operates far from thermodynamic equilibrium, sustained by metastable structures that continuously cycle through synthesis, function execution, and degradation--consuming energy and exporting entropy in the process. Neural computation exemplifies this dissipative organization, relying on low-entropy structures engaged in dynamic processes that define key information transfer and processing parameters such as gain, threshold, and integration time. This perspective proposes that...

---

### 11. Language Models Share a Readout Bottleneck in Working Memory

**Authors:** Dongyu Gong

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21176v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21176v1)

**Summary:** Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent it...

---

### 12. Statistical Mechanics of Spike Trains: Self-Consistent Activity Ensembles and Phase Transitions

**Authors:** Jan Pyrzowski, Laura Messio, Guillaume Marrelec, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20971v1)

**Summary:** We introduce a statistical-mechanical framework for spiking neuronal systems in which entire spike trains, defined as spatiotemporal configurations of discrete events, are treated as microstates of the system. Instead of modeling explicit network dynamics, we construct an ensemble over complete spike histories and assign to each configuration an effective energy functional that quantifies its consistency with intrinsic synaptic interactions.   This formulation leads to a Boltzmann-like distribut...

---

### 13. Cross-subject decoding of imagined speech from scalp EEG: a leakage-controlled evaluation on three public corpora

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20954v1)

**Summary:** Objective. A decoder of imagined speech that works for a new user without calibration would make a non-invasive speech interface practical. We tested whether imagined-speech content recorded with scalp electroencephalography (EEG) transfers across people, and examined why accuracy within a single person remains low. Approach. We analyzed three public corpora, ds003626, KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, under a protocol that enforces split integri...

---

### 14. How large an effect would we have seen? Positive controls, detection floors and dataset pitfalls in scalp-EEG speech decoding

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20942v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20942v1)

**Summary:** Objective. Studies that decode imagined speech from scalp electroencephalography (EEG) commonly validate their pipelines with a positive control, usually overt speech, and report null results without stating what effect size the pipeline could have detected. Approach. Using ds003626 ("Thinking out loud"), KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, we audited decoding of overt speech, articulator preparation and imagined speech with artifact-channel subset...

---

### 15. Awakening as a Trait-Level Transformation of Consciousness

**Authors:** Riku Ihalainen, Victor Oswald, Gulshan Kumar, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20856v1)

**Summary:** Awakening is reported across contemplative traditions yet remains poorly defined in science, where it is often conflated with transient states induced by meditation or psychedelics, obscuring its significance for theories of consciousness and cognitive architecture. We treat awakening as a functional construct capturing convergence across Hindu and Buddhist sources, phenomenological and psychometric findings, and neuroimaging evidence. Synthesizing these literatures, we find convergent evidence ...

---

### 16. Two dissociable axes of brain hierarchical dynamics track universal and population-specific effects of mindfulness

**Authors:** Victor Oswald, David Zarka, Riku Johannes Ihalainen, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20854v1)

**Summary:** How mental training reshapes the temporal architecture of large-scale brain dynamics and how these mechanisms differ between healthy and clinically vulnerable populations remains poorly understood. Time-averaged neural measures collapse the multi-scale nature of brain activity, obscuring the dynamic processes through which behavioural interventions reorganise hierarchical brain function. Here, applying a sliding-window Temporal Irreversibility Index to source-reconstructed EEG across three compl...

---

### 17. Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech

**Authors:** Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20766v1)

**Summary:** Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained wit...

---

### 18. EEG Correlates of Verbal and Perceptual Reasoning

**Authors:** Gwyneth Rolph

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19979v1)

**Summary:** Identifying the neural underpinnings of intelligence is one of the major goals of modern intelligence research. However, few imaging studies explore the high extremes of intelligence, and most use only a single composite IQ score. This study used quantitative EEG recordings to investigate correlations between the EEG variables of individual alpha peak frequency, relative power, and coherence, and scores on verbal and perceptual reasoning tests in participants with IQs from the low-average to exc...

---

### 19. Reciprocity coordinates a three-way trade-off in recurrent neural circuits

**Authors:** Xiaoyu Zhang, Mingyi Huang, Yixuan Cui, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19949v1)

**Summary:** Biological neural circuits contain both unidirectional and reciprocal connections, but how reciprocity affects circuit computation remains unclear. We varied reciprocity \r{ho} across 21 levels in recurrent-network simulations while holding network size, connection density, and directed-edge count fixed. Low-reciprocity networks produced more diverse stimulus-driven activity and performed better on four continuous-input tasks, whereas higher reciprocity generally improved performance on three de...

---

### 20. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 21. Effects of cortisol time-scales in a model of emotion regulation

**Authors:** Michael Buccino, Joshua Ginart, Eva Kaslik, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19282v1)

**Summary:** Stress reshapes cortico-limbic dynamics across multiple timescales, with important consequences for healthy and pathological arousal responses. We develop and analyze a Wilson-Cowan model of prefrontal-amygdala circuitry, incorporating excitatory and inhibitory populations involved in emotional regulation. The effects of stress cortisol are represented as history-dependent modulations of two stress-sensitive interactions: recurrent prefrontal excitation and inhibition of basolateral amygdala pri...

---

### 22. Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome

**Authors:** Taeho Jo

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19153v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19153v1)

**Summary:** In Alzheimer's disease, the amount of pathology in the brain is an imperfect predictor of how much function is lost. Pathology leads to that loss through neural circuits, but these cannot be observed neuron by neuron in patients. This study therefore simulated the central nervous system of the adult male Drosophila melanogaster: 166,700 integrate-and-fire neurons wired by the MaleCNS connectome. The simulator reproduced a published fly brain model (rate correlation 0.9997). Three kinds of damage...

---

### 23. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 24. Sense-Making phase transition framework for Affect

**Authors:** Miguel Bosch, Laura Fanfarillo, Gustavo Diez, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18115v1)

**Summary:** Contemporary accounts of affect emphasize different perspectives, ranging from the regulation of bodily states in allostatic approaches to the relational and sense-making character stressed by enactive theories. Here, we show that affect can be made explicit within the sense-making phase transition framework previously introduced for the perception of an inner sensation. Within this same formal structure, each stable minimum of the sense-making potential defines an affective state: its position ...

---

### 25. Rewiring of adult neural networks - learning from structural plasticity across multiple scales

**Authors:** Michael Fauth, Han Lu, Jannik Luboeinski, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18024v1)

**Summary:** Synaptic connections are continuously formed and eliminated even in adult neuronal networks. This process - called structural plasticity - allows networks to change their topology to learn and adapt to their environment or compensate for lesions. Yet, in contrast to synaptic plasticity, structural plasticity is less well studied and understood. We here present the current state of knowledge as well as open problems in the field along three guiding questions: (1) What regulates structural plastic...

---

### 26. Rethinking World Models for Biosignals

**Authors:** Xianglong Bao, Bosong Huang, Xiaoda Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17510v1)

**Summary:** World models promise to learn how systems evolve and respond to actions, enabling simulation, planning and decision-making. Bringing this promise to biosignals requires more than accurate prediction of physiological recordings. We examine existing biosignal world models through two requirements for intervention use: a genuine action and evidence of its causal effect. We identify three fundamental bottlenecks rooted in physiology: Temporal Latency, the variable delay between an action and its obs...

---

### 27. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 28. Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models

**Authors:** Hanbo Xie, Yue Zhao, Robert C. Wilson

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17310v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17310v1)

**Summary:** Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptiv...

---

### 29. Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors

**Authors:** Farhad Pashakhanloo, Venkatesh N. Murthy

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17164v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17164v1)

**Summary:** The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 mo...

---

### 30. Simple model of neurogliovascular unit activity with noradrenaline leading force

**Authors:** Andrey Yu. Verisokin, Darya V. Verveyko, Alexey R. Brazhe, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15263v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15263v1)

**Summary:** In this work we present a model of a neuroglivascular unit associated with a neuronal ensemble. We combine calcium dynamics in the astrocyte, the cascade of synthesis of arachidonic acid and its derivatives, as well as the activity of the network of inhibitory and excitatory neurons with changes in local blood flow. We add equations to the model for extracellular neurotransmitters such as GABA, glutamate, and norepinephrine. We show that the resulting model can exhibit different types of behavio...

---

### 31. Predicting Cognitive Tasks from Single-Channel EEG through Task-Semantic Alignment

**Authors:** Ryota Kanai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15104v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15104v1)

**Summary:** Studies of data scaling in electroencephalography (EEG) and related noninvasive recordings suggest that simple wearable devices could eventually reveal more about cognitive states. However, publicly available EEG data are difficult to combine. Different laboratories record different tasks, participants, and devices. Task-agnostic self-supervised learning can exploit such data, but representations learned only with EEG signals have not consistently produced feature representations that are direct...

---

### 32. Bayesian adaptive design for neural recruitment curves

**Authors:** Vishweshwar Tyagi, Saihari S. Dukkipati, Daniel Twili, et al.

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.15000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15000v1)

**Summary:** Nonlinear response models remain ubiquitous across disciplines with recruitment curves describing muscle response to neural stimulation. Conventional acquisition methods typically rely on static uniform sampling, requiring many stimuli, while adaptive threshold-hunting designs such as ML-PEST forfeit accurate characterization of the overall curve. We present a Bayesian adaptive design that uses posterior uncertainty over curve parameters to propose stimuli that maximize information gain across t...

---

### 33. Full Lyapunov Spectra of Random Neural Networks, Part I: Finite-Time and Asymptotic Theory

**Authors:** Haoyu Albert Wang, Wei P. Dai

**Published:** 2026-10-10

🔗 [Paper](http://arxiv.org/abs/2610.14922v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14922v1)

**Summary:** We develop a dynamical mean-field framework for the full finite-time and stationary asymptotic Lyapunov spectra of random recurrent neural networks. At finite observation time, an exact log-determinant representation of tangent-propagator singular values leads to a closed-contour matrix Dyson equation for the smoothed spectral tail. In the stationary setting, a cocycle representation yields an operator equation for the asymptotic cumulative spectrum. Both formulations retain complete local gain ...

---

### 34. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 35. EEG Entrainment to Non-Speech Rhythmic Patterns Associated with Dimensions of Language Performance

**Authors:** Francisco J. Martínez-Murcia, Nicolás J. Gallego-Molina, Marco A. Formoso, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13419v1)

**Summary:** Developmental dyslexia (DLX) affects 5-12% of the global population and impairs learning to read. Its biological basis, particularly the difficulties observed in oral phonological tasks, remains debated. Entrainment, the coupling of brain oscillations to speech rhythms, is essential for encoding phonological representations. We investigated whether brain entrainment to non-speech rhythms could predict DLX in 48 participants listening to white noise amplitude-modulated at rates matching Spanish s...

---

### 36. Beyond Anxiety and Avoidance: A Dynamic Feedback-Regulation Framework for Adult Romantic Attachment

**Authors:** Mateusz Pomianek

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13312v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13312v1)

**Summary:** Adult attachment is commonly represented by attachment anxiety and avoidance, but these person-level dimensions do not by themselves specify how momentary relational conditions are perceived, compared with desired conditions, translated into action, and updated after interpersonal feedback. We present the Attachment Regulation and Control (ARC) framework as an integrative feedback-regulation account that makes these temporal assumptions explicit and empirically testable. In ARC, control refers t...

---

### 37. Excitability across scales: a unifying EI model

**Authors:** Thomas S. J. Burger, Rodolphe Sepulchre

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13275v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13275v1)

**Summary:** Neuronal excitability is commonly modeled using different principles at the cellular and population scales, making it difficult to study how microscopic mechanisms shape macroscopic activity. We introduce a spatiotemporal excitatory-inhibitory (EI) model that unifies these scales through a common mixed-feedback architecture. The model retains the conductance-based circuit structure of Hodgkin-Huxley models and describes intrinsic and synaptic currents through memductances whose temporal and spat...

---

### 38. FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model

**Authors:** Aashish Dhawan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13018v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13018v1)

**Summary:** Connectome-constrained neural networks make biological components directly accessible to intervention, but their mechanistic conclusions can still depend on the comparison model, intervention, circuit representation and trained solution. We stress-test these dependencies in flyvis, a \emph{Drosophila} motion-vision model, using its 50-model ensemble, task-matched causal CNN controls and replicated interventions. At the level of model behaviour, three-level reverse-phi reversal in flyvis is stron...

---

### 39. Energy, Information, and the Limits of Neuropsychiatric Classification

**Authors:** Farbod Khodadadi, Mina Kheirkhah, Bita Shariatpanahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.14095v1) | 📄 [PDF](https://arxiv.org/pdf/2610.14095v1)

**Summary:** Importance: The search for reliable neuroimaging biomarkers of mental disorders has remained elusive despite decades of research. Why clinically consequential disorders yield weak neuroimaging separability remains unresolved. Drawing on statistical thermodynamics and the metabolic costs of neural coding, we propose that psychiatric disorders produce constrained deformations of a largely shared repertoire of brain activity patterns, limiting the class-specific information available for classifica...

---

### 40. Lyapunov spectrum of random neural networks

**Authors:** David G. Clark

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12426v1)

**Summary:** The Lyapunov spectrum of a nonlinear recurrent neural network with random asymmetric couplings is calculated in the limit $N\to\infty$. The calculation is based on a finite-$N$ identity that expresses the cumulative distribution of Lyapunov exponents as a response function of the tangent-space dynamics, with the tangent trajectory selected by a minimum-norm condition rather than by an initial condition. A cavity method then determines this response function at large $N$ through a self-consistent...

---

### 41. Neural Decoding as Cognitive Inference

**Authors:** Yi Guo, Changhong Jing, Yong Hu, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11923v1)

**Summary:** The brain maintains stable cognition despite continuously changing neural activity. How to extract stable cognitive states from variable neural observations remains a central problem in neural decoding. Existing neural decoding methods map neural observations to predefined external labels based on the stimulus-response principle, often capturing recording-specific spurious correlations. Inspired by how the brain infers the world, and specifically by Bayesian brain theory, we recast neural decodi...

---

### 42. Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy

**Authors:** Marko Tvrdic, Justin Richmond Domingo, Jae Ann Buenaluz, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11222v1)

**Summary:** Preclinical models poorly predict human drug efficacy, particularly in neurological disorders. Neural activity offers a uniquely rich source of translational information because it captures high-dimensional variation in nervous-system function that can be measured in both animals and humans. However, its high dimensionality makes it difficult to distinguish conserved disease-related features from variation arising from species, recording modality and experimental context. Here, we test whether s...

---

### 43. If the brain were so simple: Information-based drivers of intelligence and their interaction through an n-body-inspired framework

**Authors:** Brett J. Kagan, Johnson Zhou, Forough Habibollahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11142v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11142v1)

**Summary:** Theories of how the brain processes information and returns intelligent outputs are numerous and often difficult to conclusively test. Here, we consider an approach grounded in informatics and algorithmic thermodynamics for how neural systems respond to different patterns of information in different ways, with a focus on the relationship between the information entropy of a signal and a new proposed quantity we term information enthalpy, which represents the internal resource of structured infor...

---

### 44. Mean Field Theory Based on the Spike Time Response Curve for Synchronization Within and Between Two Alternating Populations of Neural Oscillators with Delays

**Authors:** Ananth Vedururu Srinivas, Carmen C. Canavier

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10977v1)

**Summary:** In order to study oscillators coupled by pulses emitted at discrete times, it is generally assumed that the effect of each pulse is an instantaneous phase shift, with a possible conduction delay between emission and receipt. However, we are interested in neural oscillators in which each pulse (action potential) activates a biexponential synapse, and at high frequencies, the duration of the synaptic conductance may be greater than the network period. Therefore, the effect of received pulses can s...

---

### 45. Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10850v1)

**Summary:** As AI models move toward clinical decision-making and personalized treatment, understanding \emph{what} a model learns is important beyond predictive accuracy alone. We investigate whether personalized latent dynamics reveal clinically associated differences even when predictive fit is similar. A lightweight CNN--Transformer EEG foundation model pretrained on the Temple University EEG Corpus (TUEG) extracts segment-level representations. Using the Temple University Epilepsy Corpus (TUEP), repres...

---

### 46. Learning infinite context windows in recurrent architectures via spatial neural computing

**Authors:** Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10690v1)

**Summary:** Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical...

---

### 47. Structure alone supports efficient visual computation in the Drosophila visual system

**Authors:** Eudald Correig-Fraga, Roger Guimerà, Marta Sales-Pardo

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10023v1)

**Summary:** Understanding the extent to which measured synaptic wiring determines computation remains a central challenge. Here, we couple the proofread adult Drosophila melanogaster connectome to an anatomically faithful model of its eye. Visual information is inputted in the eye model, then passed to the connectome, and finally read from a Kenyon-cell-centered linear decoder. This creates a connectome-only model in which the anatomical graph and eye geometry are fixed and only scalar synaptic gains and ne...

---

### 48. Feedback to the primary visual cortex is highly concentrated on the central visual field representation

**Authors:** Piotr Majka, Emmanuel K L Cho, Karolina Łabuszewska, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09983v1)

**Summary:** Retrograde tracer injections in marmoset monkeys revealed a striking feature of neural circuitry in primate visual system: among neurons projecting to the primary visual cortex (striate cortex, V1), the proportion of extrastriate feedback neurons relative to thalamic feedforward neurons decreases markedly with visual field eccentricity. This supports the Central-Peripheral Dichotomy theory, which proposes fundamentally distinct computational specializations --- visual recognition and attentional...

---

### 49. Do Generative Priors Align with Human Naturalness Perception?

**Authors:** Taiki Fukiage

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09928v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09928v1)

**Summary:** Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relation...

---

### 50. CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies

**Authors:** Gabriel Ocana-Santero, Marko Tvrdic

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09643v1)

**Summary:** Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It ...

---

## stat.ML

**50 papers**

### 1. ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference

**Authors:** Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23825v1)

**Summary:** The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. $χ^2$. While versatile, the evidence is notoriously difficult to compute, even when the likelihood is available. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate s...

---

### 2. Learning without relearning physical symmetry: an SO(3)-equivariant convolutional network (CNN) on the sphere

**Authors:** Joshua Williamson, Niall Jeffrey, Lorne Whiteway

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23821v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23821v1)

**Summary:** Many of the most important datasets in the physical sciences live natively on the sphere, and these data often carry no preferred position or orientation. Using methods that do not reflect this symmetry leads to far higher simulation requirements, which can be catastrophic for scientific analyses (forcing reliance on cheap, imperfect models that bias results). We present a novel spherical implementation of a gauge equivariant mesh architecture that is specifically designed for the Hierarchical E...

---

### 3. Task-aware Kernel Stein certificates for Rényi differential privacy

**Authors:** Leoni Carla Wirth, Tara Trautwein, Gesine Reinert

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23798v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23798v1)

**Summary:** Rènyi differential privacy, based on Rènyi divergence, has become a notion of choice for privacy guarantees. However, outside the Gaussian setting, Rènyi divergence can be difficult to compute. In particular, Rènyi differential privacy guarantees that exploit task-specific information, as in Rènyi Pufferfish privacy, can be challenging. Here we use kernel Stein discrepancies based on escort distributions to provide certificates for Rènyi differential privacy. By designing the kernel to focus on ...

---

### 4. Parametric Resonance in Primal-Dual Learning for Slowly Non-Stationary Constrained MDPs

**Authors:** Maxime Baelde

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23788v1)

**Summary:** Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitivity oscillates, a coherent modulation carries no resonant forcing at any depth: the dual update's st...

---

### 5. Mesoscopic learning dynamics of extensive-width neural networks

**Authors:** Shu Zhou, Jean Barbier, Sebastian Goldt

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23779v1)

**Summary:** Understanding how stochastic gradient descent learns internal representations in wide neural networks trained on rich target functions is a central problem in machine learning. We study this question in two-layer neural networks learning target functions represented by networks of the same architecture, with arbitrary nonlinearity, and with network width and input dimension growing proportionally. In this regime, standard approaches for describing the learning dynamics require tracking a divergi...

---

### 6. Exact Tail Laws for Nonlinear SGD with Infinite-Variance Gradients

**Authors:** Xiaoli Li, Qianqian Lei, Ziyang Wei, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23750v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23750v1)

**Summary:** With infinite-variance gradient noise, SGD can have infinite expected excess objective even when most iterates are close to the optimum. We characterize its accuracy through exact first-order tail probabilities for the last iterate of nonlinear, constant-stepsize SGD. For regularly varying innovations of index $t\in(1,2)$, the leading measure transports one large gradient shock through the local Hessian flow. This is the same measure that governs the central stable Ornstein--Uhlenbeck limit; we ...

---

### 7. Equivalence testing and run-count design for stochastic machine-learning experiments

**Authors:** Dmytro Knopov, Nadiya Shvai

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23700v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23700v1)

**Summary:** Claims that two training methods perform equally well often rest on a non-significant difference between two or three runs per method. We develop a protocol, with its power theory, for certifying practical equivalence in per-run metrics such as the AUROC (area under the receiver operating characteristic curve). It rests on a two-level (seed x item) variance model separating between-run dispersion from item-level noise. Equivalence within a pre-specified margin is tested by two one-sided tests (T...

---

### 8. No-Regret Language Generation

**Authors:** Jiaxun Li, Vinod Raman, Ambuj Tewari

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23641v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23641v1)

**Summary:** We introduce no-regret generation, which requires a generator to make a sublinear number of mistakes uniformly over all demonstration sequences and compatible target languages. We also formulate an agnostic variant that allows arbitrary demonstrations that may not be compatible with any languages. For both settings, we introduce tree-based mistake-forcing dimensions that exactly characterize finite-horizon minimax complexity and establish necessary and sufficient conditions for no-regret generat...

---

### 9. Boundary Detection for High-Dimensional Point Clouds

**Authors:** Abigail Hickok, Valerio Galanti, Osama Al Dalahmah, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23590v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23590v1)

**Summary:** We introduce two new methods for boundary detection in high-dimensional point cloud data, intended to work in situations with non-uniform density, high ambient dimension, and substantial noise. Our first method fits a separating hyperplane on local neighborhoods after doing local dimension reduction---this method works best when one can reliably estimate the intrinsic dimension of the data. Our second method measures the directional uniformity of local neighborhoods, and has the best overall per...

---

### 10. A general recipe for data-adaptive anytime-valid envelopes for iterative algorithms

**Authors:** Soham Bonnerjee, Aaditya Ramdas

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23570v1)

**Summary:** Most convergence guarantees for iterative stochastic algorithms are stated at a fixed iteration count and do not justify stopping at a data-dependent time. Recent work has constructed anytime-valid envelopes that do, but deterministic envelopes are typically too conservative for practical stopping, and existing data-adaptive ones are derived case-by-case, each coupling a specific algorithm to a specific noise model and boundary construction. This paper provides a general recipe for constructing ...

---

### 11. Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search

**Authors:** Quynh Trinh, Trung Nguyen, Nam Nguyen, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23565v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23565v1)

**Summary:** Monte-Carlo Tree Search (MCTS) typically stores only scalar mean estimates, which makes it poorly suited for tail-risk objectives such as conditional value-at-risk (CVaR). We introduce Categorical Thompson Sampling with Optimism (CATSO) and Particle Thompson Sampling with Optimism (PATSO), two distributional MCTS algorithms that maintain finite-support empirical backup laws at Q-edges. CATSO represents Q-edge laws with categorical atoms and Dirichlet Thompson sampling, while PATSO represents the...

---

### 12. Causal Discovery beyond Conditional Independence: Identifiability, Algorithms, and Statistical Inference for Directed Acyclic and Cyclic Graphs

**Authors:** Yang Ni

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23543v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23543v1)

**Summary:** Learning causal structure from data requires assumptions about mechanisms, noises, observation schemes, and interventions. Historically, causal discovery has relied primarily on conditional independence. This review focuses on modern causal discovery methods that exploit properties of distributions beyond conditional independence. Our organizing principle separates the source of identification from the statistical estimator and its computational implementation. This perspective connects conditio...

---

### 13. Adaptive conformal prediction on the Grassmannian

**Authors:** Dimitrios Loukrezis, Zachary J. Grey, Dimitris G. Giovanis

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23508v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23508v1)

**Summary:** We introduce a conformal prediction framework for regression with Grassmann-valued responses. The proposed method constructs prediction regions in the form of metric balls directly on the Grassmann manifold, using basis-invariant geometric distances as non-conformity measures and scaling the corresponding non-conformity scores through a learned prediction difficulty estimator. This yields locally adaptive, input-dependent prediction regions that respect the underlying manifold geometry, while re...

---

### 14. Towards optimal selection schedules for online active learning

**Authors:** Hugo Cui, Francesca Mignacco, Francesco Mori

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23477v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23477v1)

**Summary:** We consider the problem of online linear classification, where a stream of unlabeled samples is available, and annotation is costly. We investigate the optimal query policy, that prescribes whether and when a sample should be labeled and used for a training step, or instead discarded, so as to minimize a given objective. We focus on the realizable case, under Gaussian design, in the high-dimensional regime where data dimension and number of unlabeled samples grow proportionally. We consider two ...

---

### 15. Minimax-optimal Scaling Laws in Ridge Regression via Transfer Learning

**Authors:** Yalda Shabanzadeh, Diyuan Wu, Marco Mondelli

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23337v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23337v1)

**Summary:** Pretrained models are often reused across downstream tasks, motivating the question of whether this transfer learning procedure can provide a substantial performance improvement, namely, in terms of the scaling law. We address this question in the prototypical setting of high-dimensional regression, where (i) a pretrained \emph{source} model is trained via ridge regression, and (ii) a fine-tuned \emph{target} model is regularized via the $L_2$ distance from the source estimator. First, we establ...

---

### 16. The Loss or the Architecture? What Matters in Survival Analysis with Competing Risks

**Authors:** Julie Alberge, Gaël Varoquaux, Judith Abécassis

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23322v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23322v1)

**Summary:** Often, \emph{eg} in healthcare and predictive maintenance, what matters is which of several competing causes will strike first, and with what probability: survival analysis with competing risks. Corresponding deep learning methods are developed as bundles: a new architecture together with a new training loss, tested on one to five datasets against a handful of baselines. Thus, a state-of-the-art result cannot be attributed to the architecture, the loss, or the evaluation protocol. The coupling i...

---

### 17. A Class of Rényi-based Concentration Metrics for Kolmogorov-Arnold Geometry in Multilayer Perceptrons

**Authors:** Juan Carlos Fernández, Asunción Jiménez-Cordero, José Francisco Paris

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23267v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23267v1)

**Summary:** The interpretability of artificial intelligence models has become a central concern, especially for black-box models such as multilayer perceptrons (MLPs). Kolmogorov-Arnold Geometry has recently emerged as a framework for analysing the internal representations of these networks, by examining how the hidden layer locally responds to changes in the input through the minors of its Jacobian. The degree to which a few of these minors dominate the rest, known as their concentration, has so far been m...

---

### 18. Information-Geometric Blind Spots of Conformal Test Martingales

**Authors:** Johan Hallberg Szabadváry

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23131v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23131v1)

**Summary:** Conformal test martingales (CTMs) are e-processes for sequentially testing exchangeability via p-values produced by a conformity function $A$. However, any distribution shift that preserves the push-forward $P\circ A^{-1}$ leaves the p-value distribution invariant, rendering it invisible to every CTM based on $A$. We formalise this blind spot through the \emph{$A$-equivalence class} $[P]_A$ and show that, for any target distribution $T$, there is a unique closest element $Q^\ast\in[P]_A$ in KL d...

---

### 19. Distinguishability and Recovery for a Doubly Sparse Spiked Wigner Model

**Authors:** Ioana Dumitriu, JD Flynn, Zhichao Wang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23033v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23033v1)

**Summary:** We study distinguishability and recovery of a sparse rank-one signal in a spiked Wigner model with independently sparse noise through a variety of algorithms and parameter regimes. The signal and noise have separate sparsity parameters, while the signal-to-noise ratio (SNR) remains of constant order as the matrix size grows. For sub-Gaussian noise and spikes whose nonzero coordinates are bounded away from zero, a leave-one-out quadratic thresholding procedure (a generalization of Ding et al., 20...

---

### 20. Towards Hyperparameter Transfer for Differentially Private Optimization

**Authors:** Tianze Wang, Zhiqi Bu, Linjun Zhang

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22976v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22976v1)

**Summary:** Scaling laws and hyperparameter tuning remain central challenges in training large-scale models, particularly under differential privacy (DP), where optimization is further complicated by noise injection and per-sample gradient clipping. While Maximal Update Parametrization ($μ$P) allows for zero-shot hyperparameter transfer in standard training, we show that it fails under DP constraints due to the distinct spectral properties of high-dimensional noise versus low-rank gradients. In this work, w...

---

### 21. Conformal Policy Selection: When to Deploy AI Decisions for Targeted Intervention

**Authors:** Junyu Cao, Ruijiang Gao, Maytal Saar-Tsechansky, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22930v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22930v1)

**Summary:** Artificial-intelligence (AI) policies are increasingly used to make consequential decisions in medicine, finance, education, and public services, yet deploying them responsibly requires knowing not only whether a policy helps on average, but for whom. Existing tools for off-policy evaluation and safe policy learning provide population-level guarantees, but some individuals may experience adverse treatment effects. We recast targeted deployment as a multiple-testing problem: for each candidate un...

---

### 22. Unit-level aggregation breaks coverage in causal foundation models

**Authors:** Gabe Schulman, Lucius E. J. Bynum, Yoav Wald

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22770v1)

**Summary:** Causal foundation models (CFMs) show promising results for treatment-effect estimation, with unit-level estimates that are competitive on standard benchmarks. Many causal analyses, however, inform decisions through effects averaged over groups of units, such as the full sample, the treated units, or a subgroup, and for such decisions a CFM is useful only if its credible intervals are calibrated. We examine these intervals and find that their coverage degrades, both in simple synthetic settings a...

---

### 23. Optimal approximation of smooth functions by ReLU neural networks

**Authors:** Thomas Nagler

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22693v1)

**Summary:** We study uniform approximation of the Hölder ball $\mathcal H_1^s([0,1]^D)$ by fully connected ReLU networks. Except in the one-dimensional Lipschitz case, existing constructions remain separated from the information-theoretic efficiency limit. This article closes the gap for every $s>0$ and $D\ge1$: networks with width $O(N)$, depth $O(L)$, and parameter magnitude $O(1)$ attain uniform approximation error of order $(N^2L^2\log N)^{-s/D}$. No relation between width and depth is required. The con...

---

### 24. Is a Linear Probe Evidence of a Linear Representation?

**Authors:** Nadir Kutluozen, Christian Internò, David Klindt

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22655v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22655v1)

**Summary:** The linear representation hypothesis holds that pretrained vision models encode generative factors as linearly decodable directions in feature space, and comes with a standard methodology: train a linear probe, declare a factor represented if accuracy is high. We show this test is too permissive. Asymptotically, any sufficiently rich feature map, including a random one, admits a linear readout, so high probe accuracy is consistent with two very different geometries: a true linear world model, wh...

---

### 25. Flat Loss, Evolving Features: Grokking in Modular Addition

**Authors:** Akash Kumar, Karthik Sankaranarayanan

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22593v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22593v1)

**Summary:** Can a network keep learning while its training cross-entropy stays nearly flat at a positive level? We show that it can. On modular addition, a standard testbed for grokking, ReLU networks trained with supported-Polar hidden updates, normalized output-layer updates and weight decay can keep 100% training accuracy while their hidden features change and held-out accuracy rises from zero to above 90%, at relatively flat training cross-entropy. Correct classification need not minimize cross-entropy,...

---

### 26. Computing Fréchet on Unknown Submanifolds of Riemannian Manifolds

**Authors:** Ian McPherson, Mauro Maggioni

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22592v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22592v1)

**Summary:** Empirical averages are fundamental statistical primitives. On nonlinear spaces, their generalization, the Fréchet mean, generally lacks a closed-form solution, and its computation requires solving an optimization problem. We study the computation of intrinsic Fréchet means for data supported on an unknown compact $d$-dimensional Riemannian manifold $M_{1}$ embedded in an ambient metric space $(X,d_{\operatorname{obs}})$. Such settings arise when observations are better represented in non-Euclide...

---

### 27. Learning smooth dynamics via Kinematic Interpolants

**Authors:**  Yiheng,  Jiang, Youssef Marzouk, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22519v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22519v1)

**Summary:** Inferring dynamics from real-world experimental data is inherently ambiguous, as many plausible dynamical systems can explain the same positional observations at measurement times. For higher fidelity modeling of applications ranging from single-cell RNA to vortex dynamics and even flocking of birds, scientific observables increasingly also include velocity estimates that serve to resolve this issue. However, incorporating this rich information in a scalable manner, free of simulation or unneces...

---

### 28. Source-Aware Dynamic Pricing with Strategic Buyers

**Authors:** Jinjiang Zou, Yang Li, Zemin Zheng

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22516v1)

**Summary:** In modern commerce, firms and platforms typically use customer features from different sources to personalize prices: some features are verified using seller records or third-party data, while others are self-reported and may be strategically manipulated by buyers seeking lower prices. We therefore introduce a novel source-aware framework for contextual dynamic pricing with strategic buyers in a high-dimensional semiparametric setting, where buyer valuations follow a sparse linear model with an ...

---

### 29. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 30. Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear Bandits

**Authors:** Spyros Dragazis, Yilei Chen, Aldo Pacchiano

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22252v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22252v1)

**Summary:** We study how to evaluate $K$ target policies simultaneously in stochastic contextual bandits with linear reward structure. Given a known $d$-dimensional feature map and reward-free access to policy queries, we propose PRISMA (Policy evaluation through Regularized Information Sharing and Mixture Allocation), an algorithm that estimates every target policy's value to accuracy $\varepsilon$ with probability at least $1-δ$. The algorithm uses $\widetilde{\mathcal{O}}\!\left( \frac{(L^2S^2+β^2)(1\vee...

---

### 31. SurvICL: a Foundation Model for in-context Survival Analysis

**Authors:** Julie Alberge, Linus Bleistein, Judith Abécassis, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22242v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22242v1)

**Summary:** Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model. We address this issue by introducing SurvICL, a TFM that predicts survival curves in-context. SurvICL is pretrained on purely synthetic datasets generated from a novel flexible proportional-odds prior that outperf...

---

### 32. Query-Efficient Rejection Sampling for Parallel Masked Diffusion

**Authors:** Shiyuan Zhang, Xuheng Li, Qiwei Di, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22238v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22238v1)

**Summary:** Masked diffusion models (MDMs) accelerate generation by unmasking multiple tokens in parallel, but sampling these tokens independently ignores their correlations and biases the output. Anari et al. (2026) corrected this bias with rejection sampling, decomposing the log acceptance probability into a sum of token-level terms, but the evaluation requires one score query per unmasked token. We propose the Single-Increment Rejection Sampler (SIRS), which provides an estimate of the log acceptance pro...

---

### 33. Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths

**Authors:** Joran Michiels, Anis Ismail, Maarten De Vos, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22126v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22126v1)

**Summary:** Existing feature attribution methods that account for feature dependencies do not scale to high dimensions. We propose causal integrated gradients (CIG) and causal expected gradients (CEG), which extend integrated gradients to incorporate prior causal structure among input features while retaining its computational efficiency and, under conditions on the causal graph, its axiomatic guarantees. In many settings, some causal structure between features is already known, for example, that a transcri...

---

### 34. Learning Changes the World and Then What Was Learned has Changed: Training and Deploying Neural Networks in the Control Loop

**Authors:** Vittorio Lippi

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22084v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22084v1)

**Summary:** Neural networks offer critical adaptability for controlling complex systems where nominal modeling proves intractable. However, when offline-trained neural networks are deployed within closed-loop control systems, their actions fundamentally alter the state distribution upon which they were trained. This paper introduces a unified taxonomy to categorize these sequential failure modes: the initial Closed-Loop Identification Error, the deployment-induced Action Error, and the continuous Tracking E...

---

### 35. Rethinking Successive Rejects Algorithms

**Authors:** Mohamed Khair, Junpei Komiyama

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22051v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22051v1)

**Summary:** In the best-arm identification problem, an algorithm adaptively selects arms to find the arm of the largest mean reward. Successive Rejects (SR) is a simple fixed-budget best-arm identification algorithm that eliminates one candidate arm at each phase. At first glance, SR seems to have limited adaptivity, since it follows predetermined phase lengths. However, for Gaussian arms with common variance, SR's worst-instance error exponent normalized by the popular complexity measure $H_1(P)$ is optima...

---

### 36. Designing Experiments for External Decision Makers

**Authors:** Sahel Iqbal, Tom Rainforth

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22032v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22032v1)

**Summary:** Standard Bayesian experimental design (BED) methods assume the experimenter alone will act on the data, choosing the best action given their own beliefs and goals. In practice, data are often acted on by external parties whose procedures the experimenter cannot change and may not know, particularly when the data are released publicly. To extend BED to such settings, we introduce usage-aware experimental design, a framework in which an adaptive design policy is trained to minimise the usage risk:...

---

### 37. Why Shallow Neural Networks Learn Sinusoidal Components First: An Orthogonal Polynomial Dynamics Framework

**Authors:** Yanyang Xiao

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21964v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21964v1)

**Summary:** Neural networks often learn low-frequency components before high-frequency ones --- a phenomenon called spectral bias or termed F-principle. Many numerical studies have demonstrated this phenomenon, and theoretical studies have sought to explain it. However, several goals remain insufficiently addressed: (1) explaining spectral bias asymptotically, including its origin and why the preferred components are generally sinusoidal; (2) extending the explanation to general activation functions, such a...

---

### 38. SelectPFN: Amortized Bayesian Variable Selection for Sparse Nonlinear Regression with Prior-Data Fitted Networks

**Authors:** Bin Luo

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21950v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21950v1)

**Summary:** Tabular foundation models based on prior-data fitted networks (PFNs) predict on a new data set in a single forward pass, but they cannot report which inputs their predictions depend on. We propose SelectPFN, a PFN that performs Bayesian variable selection and prediction jointly for sparse nonlinear regression. In one forward pass it returns posterior inclusion probabilities for every variable, and its predictions are computed from sampled subsets only, so excluded variables provably cannot affec...

---

### 39. The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic Regret

**Authors:** Mohammad Pedramfar, Siamak Ravanbakhsh

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21908v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21908v1)

**Summary:** Many modern learning systems are used not to select a single best action, but to sample diverse high-quality outputs. Examples include entropy-regularized reinforcement learning, RLHF, and reward-guided generative modeling. Motivated by these settings, we study tilted sampling: an online learning problem in which the goal is to sample from the Gibbs distribution induced by an unknown reward function. We define sampling regret as the temperature-normalized cumulative KL divergence between the lea...

---

### 40. In-Context Learning Before Specialisation: Theory of Learning in a Solvable Topic Model

**Authors:** Francesco Cagnetta, Casper L. Christensen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21901v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21901v1)

**Summary:** Sequence models can generalise in fundamentally distinct ways: extrapolating structures seen in training, or using their prompt to adapt to novel tasks. The prevailing strategy determines how the model behaves beyond its training distribution, controlling potential capabilities and risks. Recent work has characterised many different strategies theoretically, and empirically described the transition between them as the quality and quantity of pretraining data vary. However, there is no learning t...

---

### 41. Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents

**Authors:** Hanzhen Wang, Boxiang Lyu, Zhongxiang Dai, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21870v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21870v1)

**Summary:** Risk-sensitive reinforcement learning (RL) addresses decision-making under uncertainty and adverse outcomes. Learning risk-sensitive policies from fixed datasets is important when additional interaction with the environment is costly. Existing work on risk-sensitive RL focuses on online settings or specific risk measures, leaving a general theoretical understanding of its offline setting underdeveloped. In this work, we investigate efficient offline risk-sensitive RL using the optimized certaint...

---

### 42. Robust Covariance Estimation for Entry-wise Contaminated and Partially Observed Data via Expectation Maximization Algorithm

**Authors:** Matys Savidan, Mohammed Nabil El Korso

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21709v1)

**Summary:** Robust covariance estimation under entry-wise contamination and missing data is challenging in various signal processing applications. Under the Student-$t$ model, observation-level reweighting induces a uniform attenuation across samples, which can lead to cumulative information loss even when most coordinates remain informative. The alternative Student-$t^*$ model enables coordinate-wise robustness, but its E-step is not available in closed form. We extend inference for the Student-$t^*$ model...

---

### 43. Classical methods for modern applications: synthetic tabular data generation using lightweight discrete response continuous latent variable model

**Authors:** Bartosz Barzdajn, Mateusz Krzysztoń

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21674v1)

**Summary:** In this paper, we present a lightweight algorithm for modelling tabular data containing both continuous and discrete variables. The method uses empirical marginal distributions and a selected quantile function to transform the data into a continuous latent space, where a distribution of choice, e.g. a multivariate Gaussian, can be efficiently estimated and applied. While this approach is closely related to classical well-established machine learning methods, we present a novel adaptation that fi...

---

### 44. Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference

**Authors:** Jonas Arruda, Jan Hasenauer, Stefan T. Radev

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21657v1)

**Summary:** Flow matching has emerged as a powerful generative family for simulation-based inference (SBI). However, sampling and density evaluation require numerical integration at inference time. This makes posterior sampling in neural posterior estimation costly. More importantly, it can make repeated likelihood evaluation prohibitively expensive and impractical for Markov chain Monte Carlo (MCMC) sampling, which may require thousands of repeated density evaluations. Here, we develop conditional mean flo...

---

### 45. Market Incentives for AI Safety Investment

**Authors:** Nikita Tsoy

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21607v1)

**Summary:** Despite their practical significance, modern AI systems pose significant societal risks, including toxicity, malicious use, and misinformation. Their mitigation depends not only on technical feasibility but also on the incentives of firms that develop and deploy these systems. We show how profit maximization shapes safety investment in an AI supply chain with an upstream LLM provider and several competing downstream firms. In our game-theoretic model, we derive the market-driven level of safety ...

---

### 46. Sharp and Stable Label-Free Calibration Certificates from Logical Coherence

**Authors:** Takahiro Kato

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21567v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21567v1)

**Summary:** Query-conditioned probabilistic predictors answer logically related questions one at a time, and labels to check their calibration are often missing. For each restriction on what a bettor's stakes may use, a minimax theorem identifies, for finitely supported laws of the answers, the sharp label-free lower bound on the corresponding calibration residual. On bundles of different events its mean, marginal and joint stages can separate strictly, and a bundle's bound cannot be attributed to one quest...

---

### 47. When Is Muon Optimal? Radial Fragility and Minimax Geometry

**Authors:** Ao Xu

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21549v1)

**Summary:** Muon replaces a matrix gradient by an approximate polar factor and has shown strong empirical performance in neural-network training. The Isotropic Curvature Model (ICM) provides a curvature-based explanation for this update by asking when gradient orthogonalization minimizes a one-step local-loss surrogate. We investigate the stability of this explanation when the fixed input radius of the ICM is replaced by a general radial law. We introduce the Random-Radius Isotropic Curvature Model (RR-ICM)...

---

### 48. Two Sample Sizes in Test-Time LLM Ensembling: Buffered ERM and Minimax Theory

**Authors:** Zhi Zhang, Arash A. Amini

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21363v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21363v1)

**Summary:** Test-time scaling can improve the performance of large language models by generating multiple answers to a question and aggregating them. Weighted ensembles extend this idea by drawing answers from several models, with the weights determining how often each model is used. Learning these weights from a training dataset involves two sample sizes: $Q$ labeled questions and $N$ generations per model and question. We study their interplay through the clean risk, the population error of the ensemble's...

---

### 49. Controlling the False Discovery Rate via Model-Agnostic Importance Measures

**Authors:** Mengtao Wen, Haojie Ren, Changliang Zou

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21360v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21360v1)

**Summary:** Selecting covariates while controlling the false discovery rate (FDR) is critical for interpretable scientific discovery, especially with complex machine learning models. Traditional variable selection methods often rely on specific model assumptions, while Model-X knockoffs provide a general way that leverages knowledge of the covariate distribution to produce a variable selection algorithm. This study puts forward a complementary method to Model-X knockoffs, named Model-Agnostic Selection with...

---

### 50. Dimension-Free PAC-Bayes Generalization for Deep Neural Networks via Dirichlet Processes

**Authors:** Sumit Vashishtha

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21340v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21340v1)

**Summary:** Classical PAC-Bayesian generalization theory places prior distributions over Euclidean parameter space $Θ\subseteq \mathbb{R}^D$, causing relative entropy to scale with network dimension $D$. For modern overparameterized neural networks where $D \gg n$, this parameter-counting dependency yields vacuous generalization bounds ($> 1{,}000\%$). In this work, we resolve this barrier by shifting prior specification from internal parameters to the non-parametric space of data distributions $\mathcal{M}...

---

